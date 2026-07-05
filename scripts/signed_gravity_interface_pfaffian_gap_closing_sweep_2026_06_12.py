#!/usr/bin/env python3
"""Gap-closing sweeps for the signed-gravity interface Pfaffian label.

Finite dense single-particle runner.  It reuses only the native staggered
cylinder construction recorded in the companion Pfaffian line note:

  Lx periodic, Ly open, eta_x = 1, eta_y = (-1)^x,
  H = -i D, K = 2 asinh(sqrt(m^2 + H^2)),
  K_odd = (K - R Kbar R)/2.

The measured label is the relative-tolerance support-frame Pfaffian sign,
with Procrustes transport and real-Schur Pfaffian sign.  Degenerate endpoints
where K_odd collapses are reported as degeneracies, not as sign flips.

No randomness, no network, no timestamps.  Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from typing import Callable

import numpy as np
import scipy.linalg as sla

AUDIT_TIMEOUT_SEC = 600

PASS = 0
FAIL = 0

REL_TOL = 5.0e-2
ZERO_TOP_TOL = 1.0e-12
SUPPORT_ZERO_TOL = 1.0e-8
BASE_THETA = 1.0
BASE_MASS = 0.5


def check(name: str, ok: bool, detail: str) -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {name} :: {detail}")


def site_index(x: int, y: int, lx: int) -> int:
    return y * lx + x


def row_profile(y: int, ly: int, profile: str) -> float:
    yc = y + 0.5
    if profile == "step":
        return 1.0 if yc >= 0.5 * ly else -1.0
    if profile == "tanh":
        return math.tanh((yc - 0.5 * ly) / 2.0)
    raise ValueError(f"unknown profile: {profile}")


def format_rank_changes(changes: list[tuple[float, int]]) -> str:
    return ", ".join(f"{p:.12g}->{r}" for p, r in changes)


def format_points(points: list[float]) -> str:
    return "[" + ", ".join(f"{p:.12g}" for p in points) + "]"


@dataclass
class Carrier:
    lx: int
    ly: int
    reflection: np.ndarray
    oreal_basis: np.ndarray

    @classmethod
    def build(cls, lx: int, ly: int) -> "Carrier":
        n = lx * ly
        reflection = np.zeros((n, n), dtype=float)
        for y in range(ly):
            yr = ly - 1 - y
            for x in range(lx):
                reflection[site_index(x, yr, lx), site_index(x, y, lx)] = 1.0

        r_eval, r_vec = np.linalg.eigh(reflection)
        oreal_basis = r_vec.astype(complex)
        oreal_basis[:, r_eval < 0.0] *= 1j
        return cls(lx=lx, ly=ly, reflection=reflection, oreal_basis=oreal_basis)

    def staggered_hop(self, phi: Callable[[int], float]) -> np.ndarray:
        n = self.lx * self.ly
        d = np.zeros((n, n), dtype=complex)

        for y in range(self.ly):
            phase = np.exp(1j * phi(y))
            for x in range(self.lx):
                i = site_index(x, y, self.lx)

                j = site_index((x + 1) % self.lx, y, self.lx)
                amp = 0.5 * phase
                d[i, j] += amp
                d[j, i] += -np.conj(amp)

                if y + 1 < self.ly:
                    j = site_index(x, y + 1, self.lx)
                    amp = 0.5 * ((-1.0) ** x)
                    d[i, j] += amp
                    d[j, i] += -amp

        h = -1j * d
        return 0.5 * (h + h.conj().T)

    def k_odd_and_b(self, mass: float, phi: Callable[[int], float]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        h = self.staggered_hop(phi)
        evals, evecs = np.linalg.eigh(h)
        kvals = 2.0 * np.arcsinh(np.sqrt(mass * mass + evals * evals))
        k = (evecs * kvals) @ evecs.conj().T
        k = 0.5 * (k + k.conj().T)

        r = self.reflection
        k_odd = 0.5 * (k - r @ k.conj() @ r)
        k_odd = 0.5 * (k_odd + k_odd.conj().T)

        b_complex = -1j * (self.oreal_basis.conj().T @ k_odd @ self.oreal_basis)
        b_real = np.real(b_complex)
        b_real = 0.5 * (b_real - b_real.T)
        return k_odd, b_complex, b_real


def theta_phi(carrier: Carrier, theta: float, profile: str) -> Callable[[int], float]:
    amp = theta / carrier.lx
    return lambda y: amp * row_profile(y, carrier.ly, profile)


def amplitude_phi(carrier: Carrier, amplitude: float, profile: str) -> Callable[[int], float]:
    return lambda y: amplitude * row_profile(y, carrier.ly, profile)


def direct_pair_phi(carrier: Carrier, s: float) -> Callable[[int], float]:
    amp = BASE_THETA / carrier.lx
    return lambda y: amp * s * row_profile(y, carrier.ly, "step")


def tanh_detour_phi(carrier: Carrier, s: float) -> Callable[[int], float]:
    amp = BASE_THETA / carrier.lx

    def phi(y: int) -> float:
        step = row_profile(y, carrier.ly, "step")
        detour = row_profile(y, carrier.ly, "tanh")
        return amp * (s * step + (1.0 - abs(s)) * detour)

    return phi


def pfaffian_sign_real_schur(a: np.ndarray) -> tuple[int, float]:
    a = 0.5 * (a - a.T)
    t, q = sla.schur(a, output="real")
    sign = 1
    log_abs = 0.0
    for i in range(0, a.shape[0], 2):
        b = float(t[i, i + 1])
        c = float(t[i + 1, i])
        block = b if abs(b) >= abs(c) else -c
        if block == 0.0:
            return 0, -math.inf
        sign *= 1 if block > 0.0 else -1
        log_abs += math.log(abs(block))
    det_q = float(np.linalg.det(q))
    sign *= 1 if det_q > 0.0 else -1
    return sign, log_abs


def polar_factor(m: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    u, s, vt = np.linalg.svd(m, full_matrices=False)
    return u @ vt, s


@dataclass
class LineResult:
    label: str
    params: list[float]
    ranks: list[int]
    rank_changes: list[tuple[float, int]]
    sign_changes: list[tuple[float, float, int, int]]
    degenerate_params: list[float]
    raw_orientation_flips: int
    min_overlap_sv: float
    min_support_abs_eig: float
    min_support_param: float | None
    min_top_abs: float
    min_top_param: float
    max_below_rel: float
    min_above_rel: float


def transport_line(
    carrier: Carrier,
    label: str,
    params: list[float],
    b_for_param: Callable[[float], np.ndarray],
) -> LineResult:
    prev_w: np.ndarray | None = None
    prev_rank: int | None = None
    ref_sign: int | None = None
    prev_rel_sign: int | None = None
    prev_param: float | None = None

    ranks: list[int] = []
    rank_changes: list[tuple[float, int]] = []
    sign_changes: list[tuple[float, float, int, int]] = []
    degenerate_params: list[float] = []
    raw_orientation_flips = 0
    min_overlap_sv = 1.0
    min_support_abs_eig = float("inf")
    min_support_param: float | None = None
    min_top_abs = float("inf")
    min_top_param = params[0]
    max_below_rel = 0.0
    min_above_rel = float("inf")

    for param in params:
        b = b_for_param(param)
        u, s, _vt = np.linalg.svd(b, full_matrices=False)
        top = float(s[0])
        if top < min_top_abs:
            min_top_abs = top
            min_top_param = param

        if top <= ZERO_TOP_TOL:
            rank = 0
            degenerate_params.append(param)
        else:
            scaled = s / top
            rank = int(np.count_nonzero(scaled > REL_TOL))
            if rank > 0:
                min_above_rel = min(min_above_rel, float(scaled[rank - 1]))
            if rank < len(scaled):
                max_below_rel = max(max_below_rel, float(scaled[rank]))

        ranks.append(rank)
        if len(ranks) == 1 or rank != ranks[-2]:
            rank_changes.append((param, rank))

        if rank == 0 or rank % 2 != 0:
            prev_w = None
            prev_rank = rank
            ref_sign = None
            prev_rel_sign = None
            prev_param = param
            continue

        w = np.array(u[:, :rank], copy=True)
        if prev_w is not None and prev_rank == rank:
            overlap = prev_w.T @ w
            det_overlap = float(np.linalg.det(overlap))
            if det_overlap < 0.0:
                w[:, -1] *= -1.0
                overlap = prev_w.T @ w
                raw_orientation_flips += 1
            q, overlap_s = polar_factor(overlap)
            min_overlap_sv = min(min_overlap_sv, float(overlap_s[-1]))
            w = w @ q.T
        else:
            ref_sign = None
            prev_rel_sign = None

        restricted = w.T @ b @ w
        restricted_s = np.linalg.svd(restricted, compute_uv=False)
        local_min = float(restricted_s[-1])
        if local_min < min_support_abs_eig:
            min_support_abs_eig = local_min
            min_support_param = param

        pf_sign, _pf_log_abs = pfaffian_sign_real_schur(restricted)
        if ref_sign is None:
            ref_sign = pf_sign
            rel_sign = 1
        else:
            rel_sign = pf_sign * ref_sign

        if prev_rel_sign is not None and prev_param is not None and rel_sign != prev_rel_sign:
            sign_changes.append((prev_param, param, prev_rel_sign, rel_sign))

        prev_w = w
        prev_rank = rank
        prev_rel_sign = rel_sign
        prev_param = param

    return LineResult(
        label=label,
        params=params,
        ranks=ranks,
        rank_changes=rank_changes,
        sign_changes=sign_changes,
        degenerate_params=degenerate_params,
        raw_orientation_flips=raw_orientation_flips,
        min_overlap_sv=min_overlap_sv,
        min_support_abs_eig=min_support_abs_eig,
        min_support_param=min_support_param,
        min_top_abs=min_top_abs,
        min_top_param=min_top_param,
        max_below_rel=max_below_rel,
        min_above_rel=min_above_rel,
    )


def print_line(res: LineResult) -> None:
    min_support = (
        f"{res.min_support_abs_eig:.12g} at {res.min_support_param:.12g}"
        if res.min_support_param is not None
        else "none"
    )
    print(
        "MEASURE: line "
        f"{res.label} params={format_points(res.params)} "
        f"rank_changes=[{format_rank_changes(res.rank_changes)}] "
        f"degenerate_params={format_points(res.degenerate_params)} "
        f"sign_changes={res.sign_changes} "
        f"raw_svd_orientation_flips={res.raw_orientation_flips} "
        f"min_overlap_sv={res.min_overlap_sv:.12g} "
        f"min_support_abs_eig={min_support} "
        f"min_top_abs={res.min_top_abs:.12g} at {res.min_top_param:.12g} "
        f"rel_gap_above_min={res.min_above_rel:.12g} "
        f"rel_gap_below_max={res.max_below_rel:.12g}"
    )


def run_gate() -> None:
    carrier = Carrier.build(20, 30)
    k_odd, b_complex, _b = carrier.k_odd_and_b(
        BASE_MASS,
        theta_phi(carrier, math.pi, "step"),
    )
    n = carrier.lx * carrier.ly
    r = carrier.reflection

    o2_res = float(np.max(np.abs(r @ r - np.eye(n))))
    odd_res = float(np.max(np.abs(r @ k_odd.conj() @ r + k_odd)))
    imag_res = float(np.max(np.abs(np.imag(b_complex))))
    asym_res = float(np.max(np.abs(np.real(b_complex) + np.real(b_complex).T)))

    print("MEASURE: gate theta=pi size=20x30 profile=step")
    print(
        "MEASURE: O-real residuals "
        f"O2={o2_res:.3e} O_anticomm={odd_res:.3e} "
        f"B_imag={imag_res:.3e} B_asym={asym_res:.3e}"
    )
    check("gate O^2 residual", o2_res <= 1.0e-14, f"{o2_res:.3e}")
    check("gate O anticommutes with K_odd", odd_res <= 1.0e-14, f"{odd_res:.3e}")
    check("gate O-real B imaginary residual", imag_res <= 1.0e-15, f"{imag_res:.3e}")
    check("gate O-real B antisymmetry residual", asym_res <= 1.0e-14, f"{asym_res:.3e}")


def run_mass_sweeps() -> list[LineResult]:
    mass_grid = [1.0, 0.75, 0.5, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.02, 0.01, 0.0]
    control_grid = [1.0, 0.5, 0.25, 0.1, 0.0]
    results: list[LineResult] = []

    for lx, ly, profile, grid in [
        (20, 30, "step", mass_grid),
        (20, 30, "tanh", mass_grid),
        (28, 44, "step", control_grid),
    ]:
        carrier = Carrier.build(lx, ly)

        def b_for_mass(mass: float, c: Carrier = carrier, prof: str = profile) -> np.ndarray:
            return c.k_odd_and_b(mass, theta_phi(c, BASE_THETA, prof))[2]

        res = transport_line(carrier, f"mass:{lx}x{ly}:{profile}:theta1", grid, b_for_mass)
        results.append(res)
        print_line(res)
        check(
            f"{res.label} has no degenerate mass point",
            len(res.degenerate_params) == 0,
            f"degenerate={format_points(res.degenerate_params)}",
        )
        check(
            f"{res.label} measured no same-rank transported sign flip",
            len(res.sign_changes) == 0,
            f"sign_changes={res.sign_changes}",
        )
        check(
            f"{res.label} support floor stays above zero threshold",
            res.min_support_abs_eig > SUPPORT_ZERO_TOL,
            f"min_support_abs_eig={res.min_support_abs_eig:.6g}",
        )
    return results


def run_amplitude_sweeps() -> list[LineResult]:
    amp_grid = [0.0, 0.005, 0.01, 0.025, 0.05, 0.1, 0.2, 0.4, 0.8, 1.2, math.pi / 2.0]
    control_grid = [0.0, 0.01, 0.05, 0.4, math.pi / 2.0]
    results: list[LineResult] = []

    for lx, ly, profile, grid in [
        (20, 30, "step", amp_grid),
        (20, 30, "tanh", control_grid),
        (28, 44, "step", control_grid),
    ]:
        carrier = Carrier.build(lx, ly)

        def b_for_amp(amp: float, c: Carrier = carrier, prof: str = profile) -> np.ndarray:
            return c.k_odd_and_b(BASE_MASS, amplitude_phi(c, amp, prof))[2]

        res = transport_line(carrier, f"amplitude:{lx}x{ly}:{profile}:m0.5", grid, b_for_amp)
        results.append(res)
        print_line(res)
        check(
            f"{res.label} has only the zero-amplitude degeneracy",
            res.degenerate_params == [0.0],
            f"degenerate={format_points(res.degenerate_params)}",
        )
        check(
            f"{res.label} measured no positive-amplitude transported sign flip",
            len(res.sign_changes) == 0,
            f"sign_changes={res.sign_changes}",
        )
        check(
            f"{res.label} positive-amplitude support floor stays above zero threshold",
            res.min_support_abs_eig > SUPPORT_ZERO_TOL,
            f"min_support_abs_eig={res.min_support_abs_eig:.6g}",
        )
    return results


def run_pair_sweeps() -> list[LineResult]:
    direct_grid = [1.0, 0.5, 0.1, 0.0, -0.1, -0.5, -1.0]
    detour_grid = [1.0, 0.8, 0.6, 0.4, 0.2, 0.0, -0.2, -0.4, -0.6, -0.8, -1.0]
    control_grid = [1.0, 0.5, 0.0, -0.5, -1.0]
    results: list[LineResult] = []

    carrier = Carrier.build(20, 30)
    direct = transport_line(
        carrier,
        "pair_direct:20x30:step_scale:m0.5",
        direct_grid,
        lambda s: carrier.k_odd_and_b(BASE_MASS, direct_pair_phi(carrier, s))[2],
    )
    results.append(direct)
    print_line(direct)
    check(
        "pair direct path exposes the trivial-point degeneration",
        direct.degenerate_params == [0.0],
        f"degenerate={format_points(direct.degenerate_params)} min_top={direct.min_top_abs:.6g}",
    )
    check(
        "pair direct nondegenerate segments have no same-rank transported sign flip",
        len(direct.sign_changes) == 0,
        f"sign_changes={direct.sign_changes}",
    )

    for lx, ly, grid in [(20, 30, detour_grid), (28, 44, control_grid)]:
        c = Carrier.build(lx, ly)
        detour = transport_line(
            c,
            f"pair_tanh_detour:{lx}x{ly}:m0.5",
            grid,
            lambda s, carrier=c: carrier.k_odd_and_b(BASE_MASS, tanh_detour_phi(carrier, s))[2],
        )
        results.append(detour)
        print_line(detour)
        check(
            f"{detour.label} avoids the all-zero K_odd point",
            len(detour.degenerate_params) == 0,
            f"degenerate={format_points(detour.degenerate_params)} min_top={detour.min_top_abs:.6g}",
        )
        check(
            f"{detour.label} measured no same-rank transported sign flip",
            len(detour.sign_changes) == 0,
            f"sign_changes={detour.sign_changes}",
        )
        check(
            f"{detour.label} support floor stays above zero threshold",
            detour.min_support_abs_eig > SUPPORT_ZERO_TOL,
            f"min_support_abs_eig={detour.min_support_abs_eig:.6g}",
        )
        check(
            f"{detour.label} relative support is not one fixed-rank line",
            len(detour.rank_changes) > 1,
            f"rank_changes=[{format_rank_changes(detour.rank_changes)}]",
        )
    return results


def main() -> int:
    run_gate()
    run_mass_sweeps()
    run_amplitude_sweeps()
    run_pair_sweeps()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
