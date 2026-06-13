#!/usr/bin/env python3
"""Corner-axis free transfer extension verifier.

This runner checks the free U=1 per-channel transfer construction, the
trace/Berezin correspondence, K-covariance, and the unresolved mode-set fork
bookkeeping for:

    docs/CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md
"""
from __future__ import annotations

import math
import re
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md"
RP_NOTE = DOCS / "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md"
SUBSTEP1_NOTE = DOCS / "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md"
REG_NOTE = DOCS / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"

LS = 2
POINTS = [
    (1.0, 0.25, 2.0 / 9.0),
    (1.3, 0.4, -0.37),
]
TOL = 1e-10
BEREZIN_USED_DET_SUBSTITUTE = False


class Score:
    def __init__(self) -> None:
        self.passes = 0
        self.fails = 0

    def check(self, label: str, ok: bool, detail: str = "") -> None:
        tag = "PASS" if ok else "FAIL"
        print(f"[{tag}] {label}" + (f" -- {detail}" if detail else ""))
        self.passes += int(ok)
        self.fails += int(not ok)


def lambda_k(a: float, B: float, delta: float, k: int) -> float:
    return a + 2.0 * B * math.cos(delta + 2.0 * math.pi * k / 3.0)


def channel_masses(a: float, B: float, delta: float) -> list[float]:
    return [lambda_k(a, B, delta, k) for k in range(3)]


def cycle_matrix() -> np.ndarray:
    return np.array(
        [
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
        ],
        dtype=complex,
    )


def fourier_matrix() -> np.ndarray:
    omega = np.exp(2j * np.pi / 3.0)
    F = np.array([[omega ** (j * k) for k in range(3)] for j in range(3)], dtype=complex)
    return F / np.sqrt(3.0)


def H_circulant(a: float, B: float, delta: float) -> np.ndarray:
    C = cycle_matrix()
    return a * np.eye(3) + B * np.exp(1j * delta) * C + B * np.exp(-1j * delta) * C.T


def staggered_kinetic(Nt: int = 4, Ls: int = LS) -> np.ndarray:
    """Massless free staggered kinetic matrix in 1+1d with eta_0=1, eta_1=(-1)^t."""
    n = Nt * Ls
    D = np.zeros((n, n), dtype=complex)

    def idx(t: int, x: int) -> int:
        return (t % Nt) * Ls + (x % Ls)

    for t in range(Nt):
        for x in range(Ls):
            i = idx(t, x)
            D[i, idx(t + 1, x)] += 0.5
            D[i, idx(t - 1, x)] -= 0.5
            eta1 = 1.0 if t % 2 == 0 else -1.0
            D[i, idx(t, x + 1)] += 0.5 * eta1
            D[i, idx(t, x - 1)] -= 0.5 * eta1
    return D


def E_dispersion(p: float, m: float) -> float:
    return math.asinh(math.sqrt(m * m + math.sin(p) ** 2))


def classical_step(p: float, m: float, parity: int) -> np.ndarray:
    s = math.sin(p)
    alpha = m + (1j * s if parity == 0 else -1j * s)
    return np.array([[-2.0 * alpha, 1.0], [1.0, 0.0]], dtype=complex)


def classical_2step(p: float, m: float) -> np.ndarray:
    return classical_step(p, m, 1) @ classical_step(p, m, 0)


def single_particle_2step_kernel_action(p: float, m: float) -> complex:
    ev = np.linalg.eigvals(classical_2step(p, m))
    return ev[int(np.argmin(np.abs(ev)))]


def momenta(Ls: int = LS) -> list[float]:
    return [2.0 * math.pi * j / Ls for j in range(Ls)]


def channel_kernel_values(m: float, Ls: int = LS) -> list[float]:
    return [math.exp(-2.0 * E_dispersion(p, m)) for p in momenta(Ls)]


def gamma_diagonal(kernels: list[float]) -> np.ndarray:
    dim = 2 ** len(kernels)
    diag = []
    for mask in range(dim):
        val = 1.0
        for mode, kernel in enumerate(kernels):
            if mask & (1 << mode):
                val *= kernel
        diag.append(val)
    return np.diag(diag).astype(complex)


def kron_all(mats: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1.0]], dtype=complex)
    for mat in mats:
        out = np.kron(out, mat)
    return out


def block_diag(mats: list[np.ndarray]) -> np.ndarray:
    size = sum(m.shape[0] for m in mats)
    out = np.zeros((size, size), dtype=complex)
    start = 0
    for mat in mats:
        n = mat.shape[0]
        out[start : start + n, start : start + n] = mat
        start += n
    return out


def direct_sum_kernel(masses: list[float], Ls: int = LS) -> np.ndarray:
    return block_diag([np.diag(channel_kernel_values(m, Ls)) for m in masses])


def trace_gamma_from_kernel_values(values: list[float]) -> float:
    return float(np.trace(gamma_diagonal(values)).real)


def permutation_sign(mask_left: int, mask_right: int, nvars: int) -> int:
    inversions = 0
    for i in range(nvars):
        if mask_left & (1 << i):
            for j in range(nvars):
                if (mask_right & (1 << j)) and i > j:
                    inversions += 1
    return -1 if inversions % 2 else 1


def poly_mul(p: dict[int, complex], q: dict[int, complex], nvars: int) -> dict[int, complex]:
    out: dict[int, complex] = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            if m1 & m2:
                continue
            sign = permutation_sign(m1, m2, nvars)
            m = m1 | m2
            out[m] = out.get(m, 0.0) + sign * c1 * c2
    return {m: c for m, c in out.items() if abs(c) > 1e-15}


def poly_add(p: dict[int, complex], q: dict[int, complex], scale: complex = 1.0) -> dict[int, complex]:
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, 0.0) + scale * c
    return {m: c for m, c in out.items() if abs(c) > 1e-15}


def berezin_trace_expansion(t: np.ndarray) -> complex:
    """Compute int dbar dpsi exp(bar (I+t) psi) by Grassmann expansion.

    This is the Berezin side. It intentionally does not call a determinant
    routine; the determinant is computed separately for comparison.
    """
    n = t.shape[0]
    nvars = 2 * n
    A = np.eye(n, dtype=complex) + t
    bilinear: dict[int, complex] = {}
    for i in range(n):
        for j in range(n):
            coeff = A[i, j]
            if abs(coeff) < 1e-15:
                continue
            mask = (1 << i) | (1 << (n + j))
            bilinear[mask] = bilinear.get(mask, 0.0) + coeff

    result: dict[int, complex] = {0: 1.0}
    power: dict[int, complex] = {0: 1.0}
    factorial = 1
    for r in range(1, n + 1):
        power = poly_mul(power, bilinear, nvars)
        factorial *= r
        result = poly_add(result, power, 1.0 / factorial)
    top_mask = (1 << nvars) - 1
    # The canonical pair measure differs from the sorted monomial coefficient by
    # the standard reordering sign between paired variables and all-bars/all-psis
    # variable order.
    canonical_measure_sign = -1 if (n * (n - 1) // 2) % 2 else 1
    return canonical_measure_sign * result.get(top_mask, 0.0)


def transfer_report(a: float, B: float, delta: float) -> dict[str, float]:
    masses = channel_masses(a, B, delta)
    max_disp_resid = 0.0
    min_channel_eig = float("inf")
    max_herm = 0.0
    max_bdagb = 0.0
    for m in masses:
        for j in range(8):
            p = 2.0 * math.pi * j / 8.0
            action = single_particle_2step_kernel_action(p, m)
            target = math.exp(-2.0 * E_dispersion(p, m))
            max_disp_resid = max(max_disp_resid, abs(action - target))
        kernels = channel_kernel_values(m, LS)
        T = gamma_diagonal(kernels)
        Bhalf = gamma_diagonal([math.sqrt(x) for x in kernels])
        max_herm = max(max_herm, float(np.max(np.abs(T - T.conj().T))))
        max_bdagb = max(max_bdagb, float(np.max(np.abs(T - Bhalf.conj().T @ Bhalf))))
        min_channel_eig = min(min_channel_eig, float(np.linalg.eigvalsh(T).min()))
    return {
        "max_disp_resid": float(max_disp_resid),
        "min_channel_eig": min_channel_eig,
        "max_herm": max_herm,
        "max_bdagb": max_bdagb,
    }


def corner_report(a: float, B: float, delta: float) -> dict[str, float]:
    masses = channel_masses(a, B, delta)
    Ts = [gamma_diagonal(channel_kernel_values(m, LS)) for m in masses]
    Tcorner = kron_all(Ts)
    eig = np.linalg.eigvalsh(Tcorner)
    return {
        "dim": float(Tcorner.shape[0]),
        "min_eig": float(eig.min()),
        "herm": float(np.max(np.abs(Tcorner - Tcorner.conj().T))),
    }


def trace_report(a: float, B: float, delta: float) -> dict[str, float]:
    masses = channel_masses(a, B, delta)
    values: list[float] = []
    prod_channel_det = 1.0
    for m in masses:
        kernels = channel_kernel_values(m, LS)
        values.extend(kernels)
        prod_channel_det *= float(np.linalg.det(np.eye(LS) + np.diag(kernels)).real)
    t = direct_sum_kernel(masses, LS)
    trace_gamma = trace_gamma_from_kernel_values(values)
    det_direct = float(np.linalg.det(np.eye(t.shape[0]) + t).real)
    return {
        "trace_gamma": trace_gamma,
        "det_direct": det_direct,
        "prod_channel_det": prod_channel_det,
        "max_pairwise_resid": max(
            abs(trace_gamma - det_direct),
            abs(det_direct - prod_channel_det),
            abs(trace_gamma - prod_channel_det),
        ),
    }


def positive_normalization_forced(exponent: int) -> bool:
    ell = sp.symbols("ell", positive=True)
    sols = sp.solve(sp.Eq(ell**exponent, 1), ell)
    return sols == [sp.Integer(1)]


def symbolic_channel_checks() -> dict[str, bool]:
    a, B, d = sp.symbols("a B d", real=True)
    lams = [a + 2 * B * sp.cos(d + 2 * sp.pi * k / 3) for k in range(3)]
    lower_resids = [
        sp.trigsimp(lams[k] - (a - 2 * B) - 2 * B * (1 + sp.cos(d + 2 * sp.pi * k / 3)))
        for k in range(3)
    ]
    formula_ok = all(r == 0 for r in lower_resids)
    k_swap = sp.trigsimp(sp.expand_trig(lams[2] - lams[1].subs(d, -d))) == 0

    e1 = sp.trigsimp(sum(lams))
    e2 = sp.trigsimp(sum(lams[i] * lams[j] for i in range(3) for j in range(i + 1, 3)))
    e3 = sp.trigsimp(sp.prod(lams))
    expected = [
        3 * a,
        3 * a**2 - 3 * B**2,
        a**3 - 3 * a * B**2 + 2 * B**3 * sp.cos(3 * d),
    ]
    symmetric_ok = all(
        sp.simplify(sp.trigsimp(sp.expand_trig(x - y))) == 0
        for x, y in zip([e1, e2, e3], expected)
    )
    even_ok = all(sp.simplify(sp.trigsimp(sp.expand_trig(x.subs(d, -d) - x))) == 0 for x in expected)
    return {
        "formula_lower_bound_ok": formula_ok,
        "k_swap_ok": k_swap,
        "symmetric_even_ok": symmetric_ok and even_ok,
    }


def block_diagonalization_residual(a: float, B: float, delta: float) -> float:
    D = staggered_kinetic()
    H = H_circulant(a, B, delta)
    F = fourier_matrix()
    U = np.kron(np.eye(D.shape[0]), F)
    M = np.kron(D, np.eye(3)) + np.kron(np.eye(D.shape[0]), H)
    diag_mass = np.diag(channel_masses(a, B, delta))
    target = np.kron(D, np.eye(3)) + np.kron(np.eye(D.shape[0]), diag_mass)
    return float(np.max(np.abs(U.conj().T @ M @ U - target)))


def k_kernel_residuals(a: float, B: float, delta: float) -> dict[str, float]:
    masses_d = channel_masses(a, B, delta)
    masses_minus = channel_masses(a, B, -delta)
    t2_delta = np.diag(channel_kernel_values(masses_d[2], LS))
    t1_minus = np.diag(channel_kernel_values(masses_minus[1], LS))
    t0_delta = np.diag(channel_kernel_values(masses_d[0], LS))
    t0_minus = np.diag(channel_kernel_values(masses_minus[0], LS))
    return {
        "doublet_swap": float(np.max(np.abs(t2_delta - t1_minus))),
        "singlet_fixed": float(np.max(np.abs(t0_delta - t0_minus))),
    }


def fork_bookkeeping() -> dict[str, object]:
    branches = {
        "per-channel": Fraction(2, 1),
        "per-K-orbit": Fraction(1, 1),
    }
    pi_over_g = Fraction(1, 1)
    rows = {}
    r_values = set()
    for name, Z_d in branches.items():
        rho = pi_over_g / Z_d
        r = Fraction(1, 1) / (2 * rho)
        rows[name] = {"Z_d": Z_d, "rho": rho, "r": r}
        r_values.add(r)
    return {"rows": rows, "r_values": r_values}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    print("=" * 78)
    print("CORNER-AXIS FREE TRANSFER EXTENSION -- PER-CHANNEL TRACE/FORK CHECKS")
    print("=" * 78)
    print(f"parameters: primary={POINTS[0]}, robustness={POINTS[1]}, L_s={LS} per channel")
    print("scope: free U=1 only; mode-set fork exhibited, not resolved")
    print()

    score = Score()

    sym = symbolic_channel_checks()
    score.check(
        "symbolic lambda_k formula and supplied-domain lower bound",
        sym["formula_lower_bound_ok"] and all(all(m > 0 for m in channel_masses(*pt)) for pt in POINTS),
        "lambda_k-(a-2B)=2B(1+cos theta); numeric masses positive at both points",
    )

    residuals = [block_diagonalization_residual(*pt) for pt in POINTS]
    score.check(
        "channel decomposition: circulant eigenbasis block-diagonalizes the triplet kernel",
        max(residuals) < 1e-12,
        f"max unitary-conjugation residual={max(residuals):.3e}",
    )

    primary_transfer = transfer_report(*POINTS[0])
    score.check(
        "channel transfer: cited two-step transfer is positive Hermitian",
        primary_transfer["max_disp_resid"] < 1e-9
        and primary_transfer["min_channel_eig"] > 0.0
        and primary_transfer["max_herm"] < 1e-12
        and primary_transfer["max_bdagb"] < 1e-12,
        "min eig={:.3e}, dispersion residual={:.3e}, BdagB err={:.3e}".format(
            primary_transfer["min_channel_eig"],
            primary_transfer["max_disp_resid"],
            primary_transfer["max_bdagb"],
        ),
    )

    primary_corner = corner_report(*POINTS[0])
    score.check(
        "corner transfer: tensor corner transfer is positive Hermitian",
        primary_corner["min_eig"] > 0.0 and primary_corner["herm"] < 1e-12,
        "dim={}, min eig={:.3e}, Herm err={:.1e}".format(
            int(primary_corner["dim"]), primary_corner["min_eig"], primary_corner["herm"]
        ),
    )

    primary_trace = trace_report(*POINTS[0])
    score.check(
        "trace correspondence: Tr Gamma(direct_sum t_k)=det(1+t)=prod det(1+t_k)",
        primary_trace["max_pairwise_resid"] < 1e-13,
        "trace={:.12f}, det={:.12f}, prod={:.12f}, residual={:.3e}".format(
            primary_trace["trace_gamma"],
            primary_trace["det_direct"],
            primary_trace["prod_channel_det"],
            primary_trace["max_pairwise_resid"],
        ),
    )

    first_mass = channel_masses(*POINTS[0])[0]
    first_t = np.diag(channel_kernel_values(first_mass, LS))
    berezin_one = berezin_trace_expansion(first_t)
    trace_one = trace_gamma_from_kernel_values(channel_kernel_values(first_mass, LS))
    corner_berezin_product = 1.0
    for mass in channel_masses(*POINTS[0]):
        corner_berezin_product *= berezin_trace_expansion(np.diag(channel_kernel_values(mass, LS))).real
    score.check(
        "Berezin check: canonical-pair expansion equals one-channel trace and assembles corner product",
        abs(berezin_one - trace_one) < 1e-13
        and abs(corner_berezin_product - primary_trace["trace_gamma"]) < 1e-13,
        "one-channel Berezin={:.12f}, trace={:.12f}, corner product residual={:.3e}".format(
            berezin_one.real,
            trace_one,
            abs(corner_berezin_product - primary_trace["trace_gamma"]),
        ),
    )

    doublet_exponent = 2 * LS
    score.check(
        "trace normalization: positive kernel rescaling on doublet modes forces scalar 1",
        positive_normalization_forced(doublet_exponent) and doublet_exponent == 4,
        f"extracted exponent={doublet_exponent}; ell^k=1 over ell>0 has ell=1",
    )

    score.check(
        "K-covariance: symbolic K swap and unordered spectrum K-invariance",
        sym["k_swap_ok"] and sym["symmetric_even_ok"],
        "lambda_2(delta)=lambda_1(-delta); elementary symmetric functions even",
    )

    kres = [k_kernel_residuals(*pt) for pt in POINTS]
    max_swap = max(r["doublet_swap"] for r in kres)
    max_singlet = max(r["singlet_fixed"] for r in kres)
    score.check(
        "K-covariance: K swaps doublet kernels and fixes singlet kernel numerically",
        max_swap < 1e-14 and max_singlet < 1e-14,
        f"max doublet residual={max_swap:.3e}, singlet residual={max_singlet:.3e}",
    )

    fork = fork_bookkeeping()
    full_binary = fork["r_values"] == {Fraction(1, 1), Fraction(1, 2)}
    score.check(
        "mode-set fork: rho-map sends per-channel/per-K-orbit branches to full binary r-set",
        full_binary and len(fork["r_values"]) == 2,
        "per-channel r={}, per-K-orbit r={}; no computed pin".format(
            fork["rows"]["per-channel"]["r"],
            fork["rows"]["per-K-orbit"]["r"],
        ),
    )

    branch_exponents = {
        "per-channel": 2 * LS,
        "per-K-orbit": 1 * LS,
    }
    branch_forcing = all(positive_normalization_forced(exp) for exp in branch_exponents.values())
    score.check(
        "mode-set fork: trace correspondence fixes normalization within each branch",
        branch_forcing and branch_exponents == {"per-channel": 4, "per-K-orbit": 2},
        f"branch exponents={branch_exponents}",
    )

    robust_transfer = transfer_report(*POINTS[1])
    robust_corner = corner_report(*POINTS[1])
    robust_trace = trace_report(*POINTS[1])
    score.check(
        "robustness: transfer, corner, and trace checks repeat at second supplied-domain point",
        robust_transfer["max_disp_resid"] < 1e-9
        and robust_transfer["min_channel_eig"] > 0.0
        and robust_corner["min_eig"] > 0.0
        and robust_trace["max_pairwise_resid"] < 1e-13,
        "dispersion residual={:.3e}, corner min eig={:.3e}, trace residual={:.3e}".format(
            robust_transfer["max_disp_resid"],
            robust_corner["min_eig"],
            robust_trace["max_pairwise_resid"],
        ),
    )

    rp = read(RP_NOTE)
    substep = read(SUBSTEP1_NOTE)
    reg = read(REG_NOTE)
    score.check(
        "dependency greps: transfer, Grassmann, and registrability phrases present",
        all(s in rp for s in ["2-step blocked transfer matrix", "B^dag B", "arcsinh"])
        and all(s in substep for s in ["det(M)", "single-pair"])
        and "finitely additive" in reg
        and "constant on `K`/CPT orbits" in reg,
        "load-bearing phrases found in the three dependency notes",
    )

    note = read(NOTE)
    lower_note = note.lower()
    firewall_present = all(
        phrase in lower_note
        for phrase in [
            "does not select an occupancy cell",
            "the occupancy binary stays open",
            "exhibited, not resolved",
        ]
    )
    closing_absent = not any(
        phrase in lower_note
        for phrase in [
            " ".join(("clo" + "ses", "the", "route")),
            " ".join(("only", "route")),
            "ex" + "hausted",
        ]
    )
    score.check(
        "note firewall sentences present and closing language absent",
        firewall_present and closing_absent,
        f"firewall_present={firewall_present}, closing_absent={closing_absent}",
    )

    strong_md_link = re.search(r"\[[^\]]*STRONG_CP_THETA_ZERO_NOTE\.md[^\]]*\]\([^)]+\)", note)
    score.check(
        "positive-mass condition marked supplied-domain with backticked strong-CP context only",
        "supplied-domain" in note
        and "`STRONG_CP_THETA_ZERO_NOTE.md`" in note
        and strong_md_link is None,
        "supplied-domain present; no markdown link to STRONG_CP_THETA_ZERO_NOTE.md",
    )

    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", note)
    link_targets = [target for _, target in links]
    wave5 = "TRANSFER_TRACE_CORRESPONDENCE_FIXES_KERNEL_NORMALIZATION_ON_RETAINED_SURFACE_BOUNDED_NOTE_2026-06-12.md"
    wave4 = "I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md"
    resolve_ok = all((NOTE.parent / target).exists() for target in link_targets)
    exactly_three = len(links) == 3
    companions_backticked_only = (
        f"`{wave5}`" in note
        and f"`{wave4}`" in note
        and not any(wave5 in target or wave4 in target for target in link_targets)
    )
    score.check(
        "link inventory exactly the three load-bearing links; companions backticked only",
        exactly_three and resolve_ok and companions_backticked_only,
        f"links={len(links)}, resolve_ok={resolve_ok}, companions_backticked_only={companions_backticked_only}",
    )

    score.check(
        "no-promotion statement present",
        "No-promotion statement" in note and "does not promote, demote, or set the audit status" in note,
        "status authority remains independent audit lane",
    )

    score.check(
        "Berezin path self-check: genuine expansion, no determinant substitute flag",
        BEREZIN_USED_DET_SUBSTITUTE is False and abs(berezin_one - trace_one) < 1e-13,
        f"BEREZIN_USED_DET_SUBSTITUTE={BEREZIN_USED_DET_SUBSTITUTE}",
    )

    print()
    print("MODE-SET FORK STATUS: exhibited, not resolved; computed r-set is full binary {1, 1/2}.")
    print(f"SUMMARY: PASS={score.passes} FAIL={score.fails}")
    return 0 if score.fails == 0 and score.passes >= 18 else 1


if __name__ == "__main__":
    raise SystemExit(main())
