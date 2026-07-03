#!/usr/bin/env python3
"""Frame-transported Pfaffian sign for the interface K_odd carrier.

Finite dense single-particle runner.  It uses the native 2D staggered
cylinder described in the companion note:

  Lx periodic, Ly open, m = 0.5,
  eta_x = 1, eta_y = (-1)^x,
  H = -i D,
  K = 2 asinh(sqrt(m^2 + H^2)).

The flux wall is antisymmetric under y-reflection.  The smooth profile uses
row centers, y + 1/2, so the lattice profile is exactly odd under
y -> Ly - 1 - y.

No randomness, no network, no dates.  Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import numpy as np
import scipy.linalg as sla

AUDIT_TIMEOUT_SEC = 600

PASS = 0
FAIL = 0

MASS = 0.5
REL_TOL = 5.0e-2
ABS_TRAP_TOL = 1.0e-10
GRID_STEP = 0.05
GATE_THETA = math.pi


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


def theta_grid(step: float = GRID_STEP) -> list[float]:
    vals: list[float] = []
    theta = step
    while theta < math.pi - 1.0e-14:
        vals.append(round(theta, 12))
        theta += step
    if not vals or abs(vals[-1] - math.pi) > 1.0e-14:
        vals.append(math.pi)
    return vals


def flux_phi(theta: float, lx: int, ly: int, y: int, profile: str) -> float:
    yc = y + 0.5
    if profile == "step":
        return (theta / lx) * (1.0 if yc >= 0.5 * ly else -1.0)
    if profile == "smooth":
        return (theta / lx) * math.tanh((yc - 0.5 * ly) / 2.0)
    raise ValueError(f"unknown profile: {profile}")


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

    def staggered_hop(self, theta: float, profile: str) -> np.ndarray:
        n = self.lx * self.ly
        d = np.zeros((n, n), dtype=complex)

        for y in range(self.ly):
            phase = np.exp(1j * flux_phi(theta, self.lx, self.ly, y, profile))
            for x in range(self.lx):
                i = site_index(x, y, self.lx)

                # x-link: periodic, eta_x = 1.
                j = site_index((x + 1) % self.lx, y, self.lx)
                amp = 0.5 * phase
                d[i, j] += amp
                d[j, i] += -np.conj(amp)

                # y-link: open, eta_y = (-1)^x.
                if y + 1 < self.ly:
                    j = site_index(x, y + 1, self.lx)
                    amp = 0.5 * ((-1.0) ** x)
                    d[i, j] += amp
                    d[j, i] += -amp

        h = -1j * d
        return 0.5 * (h + h.conj().T)

    def k_odd_and_b(self, theta: float, profile: str) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        h = self.staggered_hop(theta, profile)
        evals, evecs = np.linalg.eigh(h)
        kvals = 2.0 * np.arcsinh(np.sqrt(MASS * MASS + evals * evals))
        k = (evecs * kvals) @ evecs.conj().T
        k = 0.5 * (k + k.conj().T)

        r = self.reflection
        k_odd = 0.5 * (k - r @ k.conj() @ r)
        k_odd = 0.5 * (k_odd + k_odd.conj().T)

        b_complex = -1j * (self.oreal_basis.conj().T @ k_odd @ self.oreal_basis)
        b_real = np.real(b_complex)
        b_real = 0.5 * (b_real - b_real.T)
        return k_odd, b_complex, b_real


def pfaffian_sign_real_schur(a: np.ndarray) -> tuple[int, float]:
    """Return sign Pf(a) using real Schur blocks and det(Q) correction.

    For a real skew matrix, real Schur gives 2x2 skew blocks in an orthogonal
    basis: a = Q T Q^T and Pf(a) = det(Q) prod_j T[2j, 2j+1].
    The accumulated log absolute value is returned only as a diagnostic.
    """
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
    ranks: list[int]
    rank_changes: list[tuple[float, int]]
    sign_changes: list[tuple[float, float, int, int]]
    transport_events: list[tuple[float, float]]
    raw_orientation_flips: int
    min_overlap_sv: float
    min_support_abs_eig: float
    min_support_theta: float
    max_support_abs_eig: float
    gap_above_min: float
    gap_below_max: float
    gap_ratio_min: float
    theta_count: int


def support_line(
    carrier: Carrier,
    profile: str,
    policy: str,
    tol: float,
    rel: bool,
    grid: list[float],
    label: str,
) -> LineResult:
    prev_w: np.ndarray | None = None
    ref_sign: int | None = None
    prev_rel_sign: int | None = None
    prev_theta: float | None = None

    ranks: list[int] = []
    rank_changes: list[tuple[float, int]] = []
    sign_changes: list[tuple[float, float, int, int]] = []
    transport_events: list[tuple[float, float]] = []
    raw_orientation_flips = 0
    min_overlap_sv = 1.0
    min_support_abs_eig = float("inf")
    min_support_theta = grid[0]
    max_support_abs_eig = 0.0
    gap_above_min = float("inf")
    gap_below_max = 0.0
    gap_ratio_min = float("inf")

    for theta in grid:
        _k_odd, _b_complex, b = carrier.k_odd_and_b(theta, profile)
        u, s, _vt = np.linalg.svd(b, full_matrices=False)
        if rel:
            scaled = s / s[0]
            rank = int(np.count_nonzero(scaled > tol))
            above = float(scaled[rank - 1]) if rank > 0 else 0.0
            below = float(scaled[rank]) if rank < len(scaled) else 0.0
        else:
            rank = int(np.count_nonzero(s > tol))
            above = float(s[rank - 1]) if rank > 0 else 0.0
            below = float(s[rank]) if rank < len(s) else 0.0

        ranks.append(rank)
        if len(ranks) == 1 or rank != ranks[-2]:
            rank_changes.append((theta, rank))

        gap_above_min = min(gap_above_min, above)
        gap_below_max = max(gap_below_max, below)
        if below > 0.0:
            gap_ratio_min = min(gap_ratio_min, above / below)

        if rank == 0 or rank % 2 != 0:
            prev_w = None
            ref_sign = None
            prev_rel_sign = None
            prev_theta = theta
            continue

        w = np.array(u[:, :rank], copy=True)

        if prev_w is not None and prev_w.shape[1] == rank:
            overlap = prev_w.T @ w
            det_overlap = float(np.linalg.det(overlap))
            if det_overlap < 0.0:
                # SVD frames carry arbitrary orientation.  Choose the
                # representative in the same orientation class before taking
                # the polar factor; raw flips are reported as gauge flips.
                w[:, -1] *= -1.0
                overlap = prev_w.T @ w
                raw_orientation_flips += 1

            q, overlap_s = polar_factor(overlap)
            det_q = float(np.linalg.det(q))
            min_overlap_sv = min(min_overlap_sv, float(overlap_s[-1]))
            if det_q < 0.0:
                transport_events.append((theta, det_q))
            w = w @ q.T
        elif prev_w is not None and prev_w.shape[1] != rank:
            ref_sign = None
            prev_rel_sign = None

        restricted = w.T @ b @ w
        restricted_s = np.linalg.svd(restricted, compute_uv=False)
        local_min = float(restricted_s[-1])
        local_max = float(restricted_s[0])
        if local_min < min_support_abs_eig:
            min_support_abs_eig = local_min
            min_support_theta = theta
        max_support_abs_eig = max(max_support_abs_eig, local_max)

        pf_sign, _pf_log_abs = pfaffian_sign_real_schur(restricted)
        if ref_sign is None:
            ref_sign = pf_sign
            rel_sign = 1
        else:
            rel_sign = pf_sign * ref_sign

        if prev_rel_sign is not None and prev_theta is not None and rel_sign != prev_rel_sign:
            sign_changes.append((prev_theta, theta, prev_rel_sign, rel_sign))

        prev_w = w
        prev_rel_sign = rel_sign
        prev_theta = theta

    return LineResult(
        label=label,
        ranks=ranks,
        rank_changes=rank_changes,
        sign_changes=sign_changes,
        transport_events=transport_events,
        raw_orientation_flips=raw_orientation_flips,
        min_overlap_sv=min_overlap_sv,
        min_support_abs_eig=min_support_abs_eig,
        min_support_theta=min_support_theta,
        max_support_abs_eig=max_support_abs_eig,
        gap_above_min=gap_above_min,
        gap_below_max=gap_below_max,
        gap_ratio_min=gap_ratio_min,
        theta_count=len(grid),
    )


def rank_for_abs(carrier: Carrier, theta: float, profile: str, tol: float) -> int:
    _k_odd, _b_complex, b = carrier.k_odd_and_b(theta, profile)
    s = np.linalg.svd(b, compute_uv=False)
    return int(np.count_nonzero(s > tol))


def refine_rank_crossings(
    carrier: Carrier,
    profile: str,
    tol: float,
    grid: list[float],
) -> list[tuple[float, float, int, int]]:
    ranks = [rank_for_abs(carrier, theta, profile, tol) for theta in grid]
    crossings: list[tuple[float, float, int, int]] = []

    def refine_interval(left: float, right: float, left_rank: int, right_rank: int) -> None:
        if left_rank == right_rank:
            return
        if right - left <= 1.0e-8:
            crossings.append((left, right, left_rank, right_rank))
            return

        mid = 0.5 * (left + right)
        mid_rank = rank_for_abs(carrier, mid, profile, tol)
        if mid_rank == left_rank:
            refine_interval(mid, right, mid_rank, right_rank)
        elif mid_rank == right_rank:
            refine_interval(left, mid, left_rank, mid_rank)
        else:
            refine_interval(left, mid, left_rank, mid_rank)
            refine_interval(mid, right, mid_rank, right_rank)

    for i in range(1, len(grid)):
        left_rank = ranks[i - 1]
        right_rank = ranks[i]
        if left_rank == right_rank:
            continue
        refine_interval(grid[i - 1], grid[i], left_rank, right_rank)
    return crossings


def compact_rank_changes(changes: list[tuple[float, int]]) -> str:
    return ", ".join(f"{theta:.6f}->{rank}" for theta, rank in changes)


def run_gate() -> None:
    carrier = Carrier.build(20, 30)
    k_odd, b_complex, b = carrier.k_odd_and_b(GATE_THETA, "step")
    n = carrier.lx * carrier.ly
    r = carrier.reflection

    o2_res = float(np.max(np.abs(r @ r - np.eye(n))))
    odd_res = float(np.max(np.abs(r @ k_odd.conj() @ r + k_odd)))
    imag_res = float(np.max(np.abs(np.imag(b_complex))))
    asym_res = float(np.max(np.abs(np.real(b_complex) + np.real(b_complex).T)))

    evals, evecs = np.linalg.eigh(k_odd)
    pair_res = float(np.max(np.abs(evals + evals[::-1])))
    order = np.argsort(np.abs(evals))[::-1]
    rows = list(range(carrier.ly // 2 - 2, carrier.ly // 2 + 2))
    interface_weights: list[float] = []
    peak_rows: list[int] = []
    for col in order[:4]:
        vec = evecs[:, col]
        row_weights = np.array([
            float(np.sum(np.abs(vec[y * carrier.lx:(y + 1) * carrier.lx]) ** 2))
            for y in range(carrier.ly)
        ])
        interface_weights.append(float(np.sum(row_weights[rows])))
        peak_rows.append(int(np.argmax(row_weights)))

    print("MEASURE: gate theta=pi size=20x30 profile=step")
    print(
        "MEASURE: O-real residuals "
        f"O2={o2_res:.3e} O_anticomm={odd_res:.3e} "
        f"B_imag={imag_res:.3e} B_asym={asym_res:.3e}"
    )
    print(
        "MEASURE: interface localization "
        f"rows={rows} min_top4_weight={min(interface_weights):.12f} "
        f"peak_rows={peak_rows} pair_res={pair_res:.3e}"
    )

    check("O^2 residual", o2_res <= 1.0e-14, f"{o2_res:.3e}")
    check("O anticommutes with K_odd", odd_res <= 1.0e-14, f"{odd_res:.3e}")
    check("O-real B imaginary residual", imag_res <= 1.0e-15, f"{imag_res:.3e}")
    check("O-real B antisymmetry residual", asym_res <= 1.0e-14, f"{asym_res:.3e}")
    check(
        "top |K_odd| states are interface-localized",
        min(interface_weights) >= 0.98,
        f"min_top4_weight={min(interface_weights):.12f}",
    )
    check("K_odd spectrum has +/- pairing", pair_res <= 1.0e-12, f"{pair_res:.3e}")


def run_relative_lines() -> list[LineResult]:
    grid = theta_grid()
    configs = [
        (20, 30, "step"),
        (28, 44, "step"),
        (20, 30, "smooth"),
        (28, 44, "smooth"),
    ]
    results: list[LineResult] = []
    for lx, ly, profile in configs:
        carrier = Carrier.build(lx, ly)
        label = f"{lx}x{ly}:{profile}:rel{REL_TOL:g}"
        res = support_line(
            carrier=carrier,
            profile=profile,
            policy="relative",
            tol=REL_TOL,
            rel=True,
            grid=grid,
            label=label,
        )
        results.append(res)
        print(
            "MEASURE: line "
            f"{label} theta_count={res.theta_count} "
            f"rank_changes=[{compact_rank_changes(res.rank_changes)}] "
            f"gap_rel_above_min={res.gap_above_min:.12g} "
            f"gap_rel_tol={REL_TOL:.12g} "
            f"gap_rel_below_max={res.gap_below_max:.12g} "
            f"gap_ratio_min={res.gap_ratio_min:.6g} "
            f"raw_svd_orientation_flips={res.raw_orientation_flips} "
            f"transport_events={len(res.transport_events)} "
            f"sign_changes={res.sign_changes} "
            f"min_overlap_sv={res.min_overlap_sv:.12g} "
            f"min_support_abs_eig={res.min_support_abs_eig:.12g} "
            f"min_support_theta={res.min_support_theta:.12g} "
            f"max_support_abs_eig={res.max_support_abs_eig:.12g}"
        )

        check(
            f"{label} relative tol lies inside measured gap",
            res.gap_above_min > REL_TOL > res.gap_below_max,
            (
                f"above_min={res.gap_above_min:.6g} "
                f"tol={REL_TOL:.6g} below_max={res.gap_below_max:.6g}"
            ),
        )
        check(
            f"{label} rank is constant on grid",
            len(res.rank_changes) == 1,
            f"changes=[{compact_rank_changes(res.rank_changes)}]",
        )
        check(
            f"{label} alignment has no orientation-transport event",
            len(res.transport_events) == 0,
            f"events={res.transport_events}",
        )
        check(
            f"{label} transported Pf sign has no flip",
            len(res.sign_changes) == 0,
            f"sign_changes={res.sign_changes}",
        )
        check(
            f"{label} support spectrum stays away from zero",
            res.min_support_abs_eig > 1.0e-6 if profile == "step" else res.min_support_abs_eig > 1.0e-6,
            f"min_abs_eig={res.min_support_abs_eig:.6g} at theta={res.min_support_theta:.6g}",
        )
    return results


def run_absolute_trap() -> None:
    grid = theta_grid()
    carrier = Carrier.build(20, 30)
    res = support_line(
        carrier=carrier,
        profile="step",
        policy="absolute",
        tol=ABS_TRAP_TOL,
        rel=False,
        grid=grid,
        label="20x30:step:absolute1e-10",
    )
    crossings = refine_rank_crossings(carrier, "step", ABS_TRAP_TOL, grid)

    sample_thetas = [0.3, 1.0, 2.0, math.pi]
    sample_ranks = {
        theta: rank_for_abs(carrier, theta, "step", ABS_TRAP_TOL)
        for theta in sample_thetas
    }
    crossing_text = ", ".join(
        f"[{lo:.8f},{hi:.8f}]:{r0}->{r1}" for lo, hi, r0, r1 in crossings
    )
    print(
        "MEASURE: absolute_tol_trap "
        f"tol={ABS_TRAP_TOL:.1e} sample_ranks="
        + ", ".join(f"{theta:.12g}->{rank}" for theta, rank in sample_ranks.items())
    )
    print(
        "MEASURE: absolute_tol_trap_line "
        f"rank_changes=[{compact_rank_changes(res.rank_changes)}] "
        f"refined_rank_crossings={crossing_text} "
        f"transport_events={len(res.transport_events)} "
        f"same-rank_sign_changes={res.sign_changes} "
        f"min_included_abs_eig={res.min_support_abs_eig:.12g} "
        f"min_included_theta={res.min_support_theta:.12g}"
    )

    check(
        "absolute 1e-10 reproduces reviewer rank-jump scale",
        sample_ranks[0.3] == 140 and sample_ranks[1.0] == 148
        and sample_ranks[2.0] == 156 and sample_ranks[math.pi] == 164,
        ", ".join(f"{theta:.12g}->{rank}" for theta, rank in sample_ranks.items()),
    )
    check(
        "absolute 1e-10 lane has rank-policy crossings",
        len(crossings) > 0,
        crossing_text,
    )
    check(
        "absolute 1e-10 crossings are threshold events not zero modes",
        res.min_support_abs_eig > 0.5 * ABS_TRAP_TOL,
        f"min_included_abs_eig={res.min_support_abs_eig:.6g}",
    )


def main() -> int:
    run_gate()
    run_relative_lines()
    run_absolute_trap()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
