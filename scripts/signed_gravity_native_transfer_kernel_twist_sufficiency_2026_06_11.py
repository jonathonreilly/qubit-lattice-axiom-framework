#!/usr/bin/env python3
"""Native transfer-kernel sufficiency test for the signed-gravity twist datum.

This runner uses only the single-particle staggered spatial carrier.  It first
reconstructs the retained two-step transfer kernel in 1D from the RP note's
action-derived classical transfer, then applies the same decaying-channel
spectral calculus to the 2D staggered cylinder.

No many-body Fock spaces are built.  Largest dense matrix in the default run is
1120 x 1120.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 600

import math
import sys
from dataclasses import dataclass

import numpy as np


MASS = 0.5
DELTA = 1.0e-8
EDGE_THRESHOLD = 0.99
TOL = 1.0e-9
SIZES = ((20, 30), (28, 40))
THETAS = (0.0, 0.6, 1.0, math.pi)
STEP3_THETAS = (0.0, 1.0, math.pi)
LAMBDA_SWEEP = (0.20, 0.35, 0.48)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    msg = f"[{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)


def dispersion_1d(p: float | np.ndarray, m: float = MASS) -> float | np.ndarray:
    return np.arcsinh(np.sqrt(m * m + np.sin(p) ** 2))


def eta_star(m: float = MASS) -> float:
    return float(np.arcsinh(m))


def classical_step_1d(p: float, parity: int, m: float = MASS) -> np.ndarray:
    """Action-derived one-step classical transfer matrix.

    parity=0 is the even time slice, eta_1=+1; parity=1 is eta_1=-1.
    """
    alpha = m + (1j * math.sin(p) if parity == 0 else -1j * math.sin(p))
    return np.array([[-2.0 * alpha, 1.0], [1.0, 0.0]], dtype=np.complex128)


def classical_2step_1d(p: float, m: float = MASS) -> np.ndarray:
    return classical_step_1d(p, 1, m) @ classical_step_1d(p, 0, m)


def check_step1_1d_native_kernel() -> bool:
    print("STEP 1 -- native 1D two-step transfer kernel")
    ok = True

    L = 64
    max_spec_resid = 0.0
    max_imag = 0.0
    for n in range(L):
        p = 2.0 * math.pi * n / L
        eig = np.linalg.eigvals(classical_2step_1d(p))
        decaying = eig[int(np.argmin(np.abs(eig)))]
        k_measured = -np.log(decaying)
        k_target = 2.0 * float(dispersion_1d(p))
        max_spec_resid = max(max_spec_resid, abs(k_measured.real - k_target))
        max_imag = max(max_imag, abs(k_measured.imag))
    cond = max_spec_resid < 1.0e-10 and max_imag < 1.0e-10
    check(
        "Step 1 spectrum convention: -log(T_hat^2) = 2 E(p)",
        cond,
        f"L={L}, max real residual={max_spec_resid:.2e}, max imag={max_imag:.2e}",
    )
    ok &= cond

    p = 2.0 * np.pi * np.arange(L) / L
    k_symbol = 2.0 * dispersion_1d(p)
    kernel = np.fft.ifft(k_symbol)
    odd_max = float(np.max(np.abs(kernel[1::2])))
    even_max = float(np.max(np.abs(kernel[::2])))
    cond = odd_max < 1.0e-13 and even_max > 1.0e-2
    check(
        "Step 1 even-distance support",
        cond,
        f"max |K(r odd)|={odd_max:.2e}, max |K(r even)|={even_max:.3e}",
    )
    ok &= cond

    n_fft = 8192
    p_fit = 2.0 * np.pi * np.arange(n_fft) / n_fft
    h_fit = np.fft.ifft(2.0 * dispersion_1d(p_fit)).real
    offsets = np.arange(10, 42, 2, dtype=float)
    vals = np.abs(h_fit[offsets.astype(int)])
    # Include the branch-point algebraic prefactor in the fit so the slope is
    # the exponential rate, not the rate plus finite-window curvature.
    design = np.column_stack(
        [offsets, np.log(offsets), np.ones_like(offsets), 1.0 / offsets]
    )
    coef, *_ = np.linalg.lstsq(design, np.log(vals), rcond=None)
    fitted_rate = -float(coef[0])
    sharp = eta_star()
    cond = fitted_rate >= sharp and fitted_rate < 1.01 * sharp
    check(
        "Step 1 quasilocality rate fit reaches the sharp retained rate",
        cond,
        f"fit={fitted_rate:.6f}, arcsinh(m)={sharp:.6f}, m={MASS}",
    )
    ok &= cond
    return ok


def site_index(x: int, y: int, ly: int) -> int:
    return x * ly + y


def parity_vector(lx: int, ly: int) -> np.ndarray:
    return np.array(
        [1.0 if (x + y) % 2 == 0 else -1.0 for x in range(lx) for y in range(ly)]
    )


def reflection_y(lx: int, ly: int) -> np.ndarray:
    n = lx * ly
    r = np.zeros((n, n), dtype=np.float64)
    for x in range(lx):
        for y in range(ly):
            r[site_index(x, ly - 1 - y, ly), site_index(x, y, ly)] = 1.0
    return r


def staggered_spatial_D(
    lx: int,
    ly: int,
    theta: float,
    *,
    uniform_holonomy: bool = True,
    periodic_y: bool = False,
) -> np.ndarray:
    """Anti-Hermitian staggered spatial hop D on a cylinder.

    x is periodic and carries the U(1) holonomy.  y is open unless
    periodic_y=True for the bulk-gap comparison.
    """
    n = lx * ly
    d = np.zeros((n, n), dtype=np.complex128)
    ux_uniform = np.exp(1j * theta / lx)
    for x in range(lx):
        for y in range(ly):
            i = site_index(x, y, ly)

            xp = (x + 1) % lx
            xm = (x - 1) % lx
            if uniform_holonomy:
                ux_f = ux_uniform
                ux_b = ux_uniform
            else:
                ux_f = np.exp(1j * theta) if x == lx - 1 else 1.0
                ux_b = np.exp(1j * theta) if xm == lx - 1 else 1.0
            d[i, site_index(xp, y, ly)] += 0.5 * ux_f
            d[i, site_index(xm, y, ly)] += -0.5 * np.conj(ux_b)

            eta_y = 1.0 if x % 2 == 0 else -1.0
            if y + 1 < ly:
                d[i, site_index(x, y + 1, ly)] += 0.5 * eta_y
            elif periodic_y:
                d[i, site_index(x, 0, ly)] += 0.5 * eta_y
            if y - 1 >= 0:
                d[i, site_index(x, y - 1, ly)] += -0.5 * eta_y
            elif periodic_y:
                d[i, site_index(x, ly - 1, ly)] += -0.5 * eta_y
    return d


def staggered_spatial_D_block(lx: int, ly: int, theta: float, cell_momentum: int) -> np.ndarray:
    """Two-site-cell mixed (p_x,y) block for the anti-Hermitian hop.

    The standard eta_y=(-1)^x phase leaves translation by two x-sites
    manifest.  This block is used as a check that p_x remains a good quantum
    number after two-site blocking.
    """
    if lx % 2:
        raise ValueError("lx must be even for the two-site-cell block")
    lc = lx // 2
    q = 2.0 * math.pi * cell_momentum / lc
    ux = np.exp(1j * theta / lx)
    b = np.zeros((2 * ly, 2 * ly), dtype=np.complex128)

    def ib(s: int, y: int) -> int:
        return s * ly + y

    for y in range(ly):
        b[ib(0, y), ib(1, y)] += 0.5 * ux - 0.5 * np.conj(ux) * np.exp(-1j * q)
        b[ib(1, y), ib(0, y)] += 0.5 * ux * np.exp(1j * q) - 0.5 * np.conj(ux)
        for s in (0, 1):
            eta_y = 1.0 if s == 0 else -1.0
            if y + 1 < ly:
                b[ib(s, y), ib(s, y + 1)] += 0.5 * eta_y
            if y - 1 >= 0:
                b[ib(s, y), ib(s, y - 1)] += -0.5 * eta_y
    return b


def hermitian_hop_from_D(d: np.ndarray) -> np.ndarray:
    h = -1j * d
    return 0.5 * (h + h.conj().T)


def native_log_from_hop(h_hop: np.ndarray, m: float = MASS) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """K=-log(T_hat^2)=2*arcsinh(sqrt(m^2+lambda_hop^2)) by the retained
    decaying-channel transfer formula."""
    evals, evecs = np.linalg.eigh(h_hop)
    k_evals = 2.0 * np.arcsinh(np.sqrt(m * m + evals * evals))
    k = (evecs * k_evals) @ evecs.conj().T
    return 0.5 * (k + k.conj().T), k_evals, evecs


def same_parity_part(mat: np.ndarray, lx: int, ly: int) -> np.ndarray:
    p = parity_vector(lx, ly)
    return np.where(p[:, None] == p[None, :], mat, 0.0)


def parity_flipping_part(mat: np.ndarray, lx: int, ly: int) -> np.ndarray:
    p = parity_vector(lx, ly)
    return np.where(p[:, None] != p[None, :], mat, 0.0)


def op_norm_hermitian(mat: np.ndarray) -> float:
    mat_h = 0.5 * (mat + mat.conj().T)
    return float(np.max(np.abs(np.linalg.eigvalsh(mat_h))))


def counting_eta(vals: np.ndarray, delta: float = DELTA) -> tuple[int, int]:
    vals = np.asarray(vals, dtype=float)
    eta = int(np.sum(vals > delta) - np.sum(vals < -delta))
    h = int(np.sum(np.abs(vals) <= delta))
    return eta, h


@dataclass
class VerdictRow:
    lx: int
    ly: int
    theta: float
    gap0: float
    bulk_gap0: float
    threshold: float
    orient_odd_fro: float
    in_gap_count: int
    edge99_count: int
    max_edge_weight: float
    eta_bottom: tuple[int, ...]
    eta_top: tuple[int, ...]
    h_bottom: tuple[int, ...]
    h_top: tuple[int, ...]

    @property
    def condition_i(self) -> bool:
        return self.gap0 > 1.0e-8 and self.bulk_gap0 > 1.0e-8

    @property
    def condition_orientation(self) -> bool:
        if abs(self.theta) < 1.0e-12:
            return False
        return self.orient_odd_fro > 1.0e-8

    @property
    def condition_ii(self) -> bool:
        return self.in_gap_count > 0 and self.edge99_count > 0

    @property
    def condition_iii(self) -> bool:
        if not self.condition_ii:
            return False
        stable_bottom = len(set(self.eta_bottom)) == 1 and len(set(self.h_bottom)) == 1
        stable_top = len(set(self.eta_top)) == 1 and len(set(self.h_top)) == 1
        if not (stable_bottom and stable_top):
            return False
        eb = self.eta_bottom[0]
        et = self.eta_top[0]
        hb = self.h_bottom[0]
        ht = self.h_top[0]
        return hb == 0 and ht == 0 and eb != 0 and et == -eb


def check_gauge_and_momentum_controls() -> None:
    print("\nSTEP 2 -- geometry and gauge controls")
    lx, ly, theta = 12, 14, 1.0
    h_uniform = hermitian_hop_from_D(staggered_spatial_D(lx, ly, theta, uniform_holonomy=True))
    h_single = hermitian_hop_from_D(staggered_spatial_D(lx, ly, theta, uniform_holonomy=False))
    _, ku, _ = native_log_from_hop(h_uniform)
    _, ks, _ = native_log_from_hop(h_single)
    gauge_err = float(np.max(np.abs(np.sort(ku) - np.sort(ks))))
    check(
        "Uniform holonomy and single twisted bond are spectrally gauge-equivalent",
        gauge_err < 1.0e-10,
        f"max |sort(K_uniform)-sort(K_single_bond)|={gauge_err:.2e}",
    )

    full_eigs = np.linalg.eigvalsh(h_uniform)
    block_eigs: list[float] = []
    for n in range(lx // 2):
        hb = hermitian_hop_from_D(staggered_spatial_D_block(lx, ly, theta, n))
        block_eigs.extend(float(x) for x in np.linalg.eigvalsh(hb))
    block_err = float(np.max(np.abs(np.sort(full_eigs) - np.sort(block_eigs))))
    check(
        "Two-site-cell mixed (p_x,y) representation reproduces the full cylinder spectrum",
        block_err < 1.0e-10,
        f"max spectral residual={block_err:.2e}, blocks={lx//2}, block_dim={2*ly}",
    )


def run_step3_dichotomy_gates() -> dict[float, float]:
    print("\nSTEP 3 -- parity and orientation dichotomy gates on K_2D")
    lx, ly = SIZES[0]
    gamma = np.diag(parity_vector(lx, ly))
    refl = reflection_y(lx, ly)
    orient_odd_op: dict[float, float] = {}
    max_hop_anti = 0.0
    max_k_flip = 0.0

    for theta in STEP3_THETAS:
        h_hop = hermitian_hop_from_D(staggered_spatial_D(lx, ly, theta))
        k, _k_evals, _evecs = native_log_from_hop(h_hop)
        raw_massive = h_hop + MASS * gamma

        k_comm = float(np.linalg.norm(gamma @ k - k @ gamma, ord=2))
        k_anti = float(np.linalg.norm(gamma @ k + k @ gamma, ord=2))
        hop_anti = float(np.linalg.norm(gamma @ h_hop + h_hop @ gamma, ord=2))
        raw_anti = float(np.linalg.norm(gamma @ raw_massive + raw_massive @ gamma, ord=2))
        raw_comm = float(np.linalg.norm(gamma @ raw_massive - raw_massive @ gamma, ord=2))

        same = same_parity_part(k, lx, ly)
        flip = parity_flipping_part(k, lx, ly)
        same_norm = op_norm_hermitian(same)
        flip_norm = float(np.linalg.norm(flip, ord=2))
        max_hop_anti = max(max_hop_anti, hop_anti)
        max_k_flip = max(max_k_flip, flip_norm)
        orient_image = refl @ same.conj() @ refl.T
        orient_even = 0.5 * (same + orient_image)
        orient_odd = 0.5 * (same - orient_image)
        even_norm = op_norm_hermitian(orient_even)
        odd_norm = op_norm_hermitian(orient_odd)
        orient_odd_op[theta] = odd_norm

        print(
            "  theta={:.6g}: ||[Gamma,K]||={:.2e}, ||{{Gamma,K}}||={:.3e}; "
            "raw massive ||[Gamma,H]||={:.3e}, ||{{Gamma,H}}||={:.3e}; "
            "pure-hop anti floor={:.2e}".format(
                theta, k_comm, k_anti, raw_comm, raw_anti, hop_anti
            )
        )
        print(
            "             ||K_same||={:.6f}, ||K_flip||={:.2e}, "
            "orientation-even={:.6f}, orientation-odd={:.6f}".format(
                same_norm, flip_norm, even_norm, odd_norm
            )
        )

    theta0_floor = orient_odd_op[0.0]
    check(
        "Parity-flipping raw hop anticommutes with Gamma before the log",
        max_hop_anti < 1.0e-12,
        "max ||{{Gamma,H_hop}}||={:.2e}".format(max_hop_anti),
    )
    check(
        "Native K_2D is same-parity and not in the parity-flipping-only class",
        max_k_flip < 1.0e-10 and theta0_floor < 1.0e-10 and orient_odd_op[1.0] > 1.0e-3,
        "max ||K_flip||={:.2e}, theta=0 orientation-odd floor={:.2e}, "
        "theta=1.0 orientation-odd={:.3e}".format(
            max_k_flip, theta0_floor, orient_odd_op[1.0]
        ),
    )
    return orient_odd_op


def analyze_size_theta(lx: int, ly: int, theta: float) -> VerdictRow:
    gamma_diag = parity_vector(lx, ly)
    gamma = np.diag(gamma_diag)
    h_hop = hermitian_hop_from_D(staggered_spatial_D(lx, ly, theta))
    k, k_evals, evecs = native_log_from_hop(h_hop)

    h_bulk = hermitian_hop_from_D(staggered_spatial_D(lx, ly, theta, periodic_y=True))
    _k_bulk, k_bulk_evals, _ = native_log_from_hop(h_bulk)
    bulk_gap0 = float(np.min(np.abs(k_bulk_evals)))
    gap0 = float(np.min(np.abs(k_evals)))
    threshold = 0.5 * bulk_gap0

    refl = reflection_y(lx, ly)
    same = same_parity_part(k, lx, ly)
    orient_odd = 0.5 * (same - refl @ same.conj() @ refl.T)
    orient_odd_fro = float(np.linalg.norm(orient_odd, ord="fro"))

    in_gap = np.abs(k_evals) <= threshold
    bottom_weights = []
    top_weights = []
    for j in range(evecs.shape[1]):
        vec = evecs[:, j].reshape((lx, ly))
        bottom_weights.append(float(np.sum(np.abs(vec[:, 0]) ** 2)))
        top_weights.append(float(np.sum(np.abs(vec[:, ly - 1]) ** 2)))
    bottom_weights_arr = np.asarray(bottom_weights)
    top_weights_arr = np.asarray(top_weights)
    edge99 = in_gap & (
        (bottom_weights_arr >= EDGE_THRESHOLD) | (top_weights_arr >= EDGE_THRESHOLD)
    )
    max_edge_weight = float(np.max(np.maximum(bottom_weights_arr, top_weights_arr)))

    eta_bottom: list[int] = []
    eta_top: list[int] = []
    h_bottom: list[int] = []
    h_top: list[int] = []
    for lam in LAMBDA_SWEEP:
        spectral = in_gap & (np.abs(k_evals) <= lam)
        bottom = spectral & (bottom_weights_arr >= EDGE_THRESHOLD)
        top = spectral & (top_weights_arr >= EDGE_THRESHOLD)
        eb, hb = counting_eta(k_evals[bottom])
        et, ht = counting_eta(k_evals[top])
        eta_bottom.append(eb)
        eta_top.append(et)
        h_bottom.append(hb)
        h_top.append(ht)

    # The native log must commute with the parity grading to be a sector
    # selector rather than a mirror-enforcing parity-flipping operator.
    comm = float(np.linalg.norm(gamma @ k - k @ gamma, ord=2))
    if comm >= 1.0e-8:
        print(f"WARNING: parity commutator unexpectedly large at {(lx, ly, theta)}: {comm:.2e}")

    return VerdictRow(
        lx=lx,
        ly=ly,
        theta=theta,
        gap0=gap0,
        bulk_gap0=bulk_gap0,
        threshold=threshold,
        orient_odd_fro=orient_odd_fro,
        in_gap_count=int(np.sum(in_gap)),
        edge99_count=int(np.sum(edge99)),
        max_edge_weight=max_edge_weight,
        eta_bottom=tuple(eta_bottom),
        eta_top=tuple(eta_top),
        h_bottom=tuple(h_bottom),
        h_top=tuple(h_top),
    )


def print_verdict_table(rows: list[VerdictRow]) -> None:
    print("\nVERDICT TABLE")
    header = (
        "condition | theta | size | measured value | met\n"
        "--- | ---: | ---: | --- | ---"
    )
    print(header)
    for row in rows:
        size = f"{row.lx}x{row.ly}"
        print(
            "gapped zero window | {:.6g} | {} | gap0={:.6f}, periodic-bulk gap0={:.6f} | {}".format(
                row.theta,
                size,
                row.gap0,
                row.bulk_gap0,
                "met" if row.condition_i else "not-met",
            )
        )
        print(
            "orientation-odd same-parity coupling | {:.6g} | {} | Fro norm={:.6f} | {}".format(
                row.theta,
                size,
                row.orient_odd_fro,
                "met" if row.condition_orientation else "not-met",
            )
        )
        print(
            "in-gap edge tower | {:.6g} | {} | |lambda|<=bulk_gap/2={:.6f}: states={}, edge99={} | {}".format(
                row.theta,
                size,
                row.threshold,
                row.in_gap_count,
                row.edge99_count,
                "met" if row.condition_ii else "not-met",
            )
        )
        print(
            "spectral eta labels | {:.6g} | {} | Lambda={} bottom_eta={} top_eta={} bottom_h={} top_h={} | {}".format(
                row.theta,
                size,
                tuple(f"{x:.2f}" for x in LAMBDA_SWEEP),
                row.eta_bottom,
                row.eta_top,
                row.h_bottom,
                row.h_top,
                "met" if row.condition_iii else "not-met",
            )
        )


def run_step4_sufficiency_table() -> list[VerdictRow]:
    print("\nSTEP 4 -- #3585 sufficiency conditions")
    rows: list[VerdictRow] = []
    for lx, ly in SIZES:
        for theta in THETAS:
            row = analyze_size_theta(lx, ly, theta)
            rows.append(row)
            print(
                "  size={}x{}, theta={:.6g}: gap0={:.6f}, threshold={:.6f}, "
                "in_gap={}, edge99={}, max_edge_weight_any_state={:.3f}, "
                "eta_bottom={}, eta_top={}".format(
                    lx,
                    ly,
                    theta,
                    row.gap0,
                    row.threshold,
                    row.in_gap_count,
                    row.edge99_count,
                    row.max_edge_weight,
                    row.eta_bottom,
                    row.eta_top,
                )
            )
    print_verdict_table(rows)

    no_edge_tower = all((row.in_gap_count == 0 and row.edge99_count == 0) for row in rows)
    labels_absent = all(not row.condition_iii for row in rows)
    gaps_present = all(row.condition_i for row in rows)
    generic_orient = all(
        row.condition_orientation for row in rows if abs(row.theta) > 1.0e-12
    )
    check(
        "Condition (i) gapped zero window is present on all tested native cylinders",
        gaps_present,
        "min gap0={:.6f}".format(min(row.gap0 for row in rows)),
    )
    check(
        "Orientation-odd same-parity content appears at nonzero holonomy",
        generic_orient,
        "theta=0 is the untwisted no-label control",
    )
    check(
        "Condition (ii) fails sharply: no in-gap edge tower is present",
        no_edge_tower,
        "all tested rows have in_gap=0 and edge99=0",
    )
    check(
        "Condition (iii) fails without an edge tower: spectral eta labels are undefined",
        labels_absent,
        "all Lambda-sweep eta counts on edge99 in-gap states are zero",
    )
    structural_floor = 2.0 * float(np.arcsinh(MASS))
    floor_holds = all(row.gap0 >= structural_floor - 1.0e-9 for row in rows)
    window_below_floor = all(row.threshold < structural_floor for row in rows)
    check(
        "Structural emptiness on tested carriers: spec(K) floor 2*arcsinh(m) sits above every tested zero window",
        floor_holds and window_below_floor,
        "floor={:.6f}; the in-gap scan instantiates a positivity theorem, "
        "not a size-limited search".format(structural_floor),
    )
    return rows


def main() -> int:
    print("Native transfer-kernel sufficiency test")
    print(f"mass m={MASS}; edge localization threshold={EDGE_THRESHOLD}")
    step1_ok = check_step1_1d_native_kernel()
    if not step1_ok:
        print("STEP-1-DISCREPANCY: native 1D construction did not match the retained RP object.")
        print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
        return 1

    check_gauge_and_momentum_controls()
    run_step3_dichotomy_gates()
    run_step4_sufficiency_table()
    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
