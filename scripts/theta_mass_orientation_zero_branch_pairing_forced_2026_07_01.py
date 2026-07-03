"""Theta mass-orientation zero branch is pairing-forced on the K-real surface.

Companion runner for
docs/THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md

Class-A finite checks (deterministic, no comparator):
  T1a-e  Case-A structure: antisymmetry, imaginary spectrum, +/-lambda pairing,
         {eps, M_KS} = 0, even kernel dimension.
  T2a-d  det(M_KS + m I) = prod_pairs (m^2 + lambda^2) * m^(2z) >= 0 for ALL
         real m (both signs), evenness in m, strict positivity at m < 0.
  T3a-c  det(M_KS (x) I_3 + I (x) A) = prod_k det(M_KS + a_k I) >= 0 across a
         Brannen dial grid including negative signed roots.
  T4a-b  det(A^2) = (det A)^2 >= 0 with det A < 0 exhibited.
  T5a-b  refutation: real symmetric (pairing-breaking) perturbation gives
         det < 0 at a real mass where the unperturbed det is > 0.
  T6a-b  refutation: non-K-real flavor block leaves {0, pi}; restoring
         Hermiticity returns arg det to 0.
"""
from __future__ import annotations

import numpy as np
import warnings

AUDIT_TIMEOUT_SEC = 120

PASS_COUNT = 0
FAIL_COUNT = 0
TOL_ZERO = 1e-10


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        tag = "[PASS]"
    else:
        FAIL_COUNT += 1
        tag = "[FAIL]"
    suffix = f"  ({detail})" if detail else ""
    print(f"  {tag} {name}{suffix}")


def det_quiet(matrix: np.ndarray) -> complex:
    """Evaluate a determinant while suppressing overflow warnings from scans."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return np.linalg.det(matrix)


# ----------------------------------------------------------------------------
# Case-A operators: real antisymmetric staggered hopping with bipartite grading
# ----------------------------------------------------------------------------

def mks_1d(n: int) -> tuple[np.ndarray, np.ndarray]:
    """1d staggered-only hopping (n even), antiperiodic; eps = (-1)^x."""
    M = np.zeros((n, n))
    for x in range(n):
        s = -1.0 if x == n - 1 else 1.0
        M[x, (x + 1) % n] += 0.5 * s
        M[(x + 1) % n, x] -= 0.5 * s
    eps = np.diag([(-1.0) ** x for x in range(n)])
    return M, eps


def mks_2d(L: int, z2_seed: int | None) -> tuple[np.ndarray, np.ndarray]:
    """2d staggered hopping on L x L (L even), antiperiodic in x, staggered
    phase eta_2 = (-1)^x; optional real Z2 background (preserves reality and
    antisymmetry); eps = (-1)^(x+y)."""
    rng = np.random.default_rng(z2_seed) if z2_seed is not None else None
    N = L * L
    M = np.zeros((N, N))
    idx = lambda x, y: (x % L) * L + (y % L)
    for x in range(L):
        for y in range(L):
            i = idx(x, y)
            s = -1.0 if x == L - 1 else 1.0
            u1 = float(rng.choice([1.0, -1.0])) if rng is not None else 1.0
            j = idx(x + 1, y)
            M[i, j] += 0.5 * s * u1
            M[j, i] -= 0.5 * s * u1
            eta2 = (-1.0) ** x
            u2 = float(rng.choice([1.0, -1.0])) if rng is not None else 1.0
            j2 = idx(x, y + 1)
            M[i, j2] += 0.5 * eta2 * u2
            M[j2, i] -= 0.5 * eta2 * u2
    eps = np.diag([(-1.0) ** ((i // L) + (i % L)) for i in range(N)])
    return M, eps


CONFIGS = [
    ("d=1 n=8 free", *mks_1d(8)),
    ("d=2 L=4 free", *mks_2d(4, None)),
    ("d=2 L=4 Z2(seed 1)", *mks_2d(4, 1)),
    ("d=2 L=4 Z2(seed 2)", *mks_2d(4, 2)),
]

M_GRID = [-1.3, -0.7, -0.4, -0.05, 0.05, 0.4, 0.7, 1.3]


def paired_positive_and_zeros(M: np.ndarray) -> tuple[np.ndarray, int]:
    """Split the (purely imaginary) spectrum into positive lambdas and the
    zero-eigenvalue count, with a clean partition (no double counting)."""
    lam = np.sort(np.linalg.eigvals(M).imag)
    zeros = int(np.sum(np.abs(lam) <= TOL_ZERO))
    pos = lam[lam > TOL_ZERO]
    return pos, zeros


def brannen(a: float, babs: float, delta: float) -> np.ndarray:
    C = np.roll(np.eye(3), 1, axis=0)
    b = babs * np.exp(1j * delta)
    return a * np.eye(3) + b * C + np.conj(b) * C.T


def test_T1_structure() -> None:
    print("T1 — Case-A structure on every tested configuration")
    ok_anti, ok_imag, ok_pair, ok_grad, ok_even = True, True, True, True, True
    details = []
    for name, M, eps in CONFIGS:
        if np.max(np.abs(M + M.T)) != 0.0:
            ok_anti = False
        ev = np.linalg.eigvals(M)
        if np.max(np.abs(ev.real)) > 1e-12:
            ok_imag = False
        lam = np.sort(ev.imag)
        if np.max(np.abs(lam + lam[::-1])) > 1e-10:
            ok_pair = False
        if np.max(np.abs(eps @ M + M @ eps)) != 0.0:
            ok_grad = False
        _, zeros = paired_positive_and_zeros(M)
        if zeros % 2 != 0:
            ok_even = False
        details.append(f"{name}: kernel={zeros}")
    check("T1a [A] M_KS is exactly real antisymmetric on all configs", ok_anti)
    check("T1b [A] spectrum purely imaginary (max |Re| < 1e-12)", ok_imag)
    check("T1c [A] exact +/-lambda pairing of the spectrum", ok_pair)
    check("T1d [A] bipartite grading {eps, M_KS} = 0 exactly", ok_grad)
    check("T1e [A] kernel dimension is even", ok_even, "; ".join(details))


def test_T2_scalar_mass() -> None:
    print("T2 — det(M_KS + m I) for ALL real m: pairing formula, sign, evenness")
    ok_formula, ok_pos, ok_even, ok_neg = True, True, True, True
    worst_ratio, min_det_neg = 0.0, np.inf
    for name, M, _ in CONFIGS:
        n = M.shape[0]
        pos, zeros = paired_positive_and_zeros(M)
        for m in M_GRID:
            d = float(det_quiet(M + m * np.eye(n)).real)
            pred = float(np.prod(m * m + pos * pos)) * (m ** zeros)
            ratio_err = abs(d / pred - 1.0)
            worst_ratio = max(worst_ratio, ratio_err)
            if ratio_err > 1e-8:
                ok_formula = False
            if not d > 0.0:
                ok_pos = False
            d_flip = float(det_quiet(M - m * np.eye(n)).real)
            if abs(d - d_flip) > 1e-9 * abs(d):
                ok_even = False
            if m < 0:
                min_det_neg = min(min_det_neg, d)
    if not (min_det_neg > 0.0):
        ok_neg = False
    check("T2a [A] pairing formula det = prod(m^2 + lambda^2) * m^(2z) at "
          "machine precision on every config and mass", ok_formula,
          f"worst |ratio - 1| = {worst_ratio:.2e}")
    check("T2b [A] det(M_KS + m I) > 0 for every tested real m of BOTH signs",
          ok_pos)
    check("T2c [A] det is an EVEN function of m: det(M+mI) = det(M-mI)",
          ok_even)
    check("T2d [A] strict positivity specifically on the m < 0 half: the "
          "positive-mass convention is not load-bearing for the orientation",
          ok_neg, f"min det over m<0 grid = {min_det_neg:.3e} > 0")


def test_T3_flavor_tensor() -> None:
    print("T3 — Hermitian generation mass on the flavor factor, signed roots")
    name, M, _ = CONFIGS[1]
    N = M.shape[0]
    ok_fact, ok_pos = True, True
    worst = 0.0
    n_negroot, n_dials = 0, 0
    dial_grid = [(a, babs, delta)
                 for a in (0.5, 1.0)
                 for babs in (0.2, 0.8, 1.2)
                 for delta in (0.0, 0.3, 2.0)]
    for (a, babs, delta) in dial_grid:
        A = brannen(a, babs, delta)
        ak = np.linalg.eigvalsh(A)
        n_dials += 1
        if np.min(ak) < 0:
            n_negroot += 1
        big = np.kron(M, np.eye(3)) + np.kron(np.eye(N), A)
        d = det_quiet(big)
        dfac = float(np.prod([det_quiet(M + x * np.eye(N)).real for x in ak]))
        err = abs(d / dfac - 1.0)
        worst = max(worst, err)
        if err > 1e-8:
            ok_fact = False
        if not (d.real > 0.0 and abs(d.imag) < 1e-6 * abs(d.real)):
            ok_pos = False
    check("T3a [A] exact tensor factorization det(M(x)I + I(x)A) = "
          "prod_k det(M + a_k I) across the dial grid", ok_fact,
          f"worst |ratio - 1| = {worst:.2e} ({name})")
    check("T3b [A] determinant > 0 (zero branch) on EVERY dial, negative "
          "signed-Brannen roots included", ok_pos,
          f"{n_dials} dials, {n_negroot} with a negative root")
    A = brannen(1.0, 1.2, 0.3)
    ak = np.linalg.eigvalsh(A)
    big = np.kron(M, np.eye(3)) + np.kron(np.eye(N), A)
    d = det_quiet(big).real
    check("T3c [A] explicit negative-root dial (a=1, |b|=1.2, delta=0.3): "
          "min eigenvalue < 0 AND composed det > 0", bool(np.min(ak) < 0 and d > 0),
          f"roots = {np.round(ak, 4)}, det = {d:.3e}")


def test_T4_squared_class() -> None:
    print("T4 — squared mass class: det(A^2) = (det A)^2")
    ok_id, saw_neg = True, False
    for a in (0.5, 1.0):
        for babs in (0.2, 0.8, 1.2):
            for delta in (0.0, 0.3, 2.0):
                A = brannen(a, babs, delta)
                dA = det_quiet(A).real
                d2 = det_quiet(A @ A).real
                if abs(d2 - dA * dA) > 1e-9 * max(1.0, dA * dA):
                    ok_id = False
                if dA < 0:
                    saw_neg = True
    check("T4a [A] det(A^2) = (det A)^2 identically across the dial grid", ok_id)
    check("T4b [A] dials with det A < 0 exist, and their squared-class det is "
          "still on the zero branch: the sign of det A never reaches the "
          "orientation", saw_neg)


def test_T5_pairing_refutation() -> None:
    print("T5 — refutation: breaking the pairing (real symmetric perturbation)")
    _, M, _ = CONFIGS[1]
    N = M.shape[0]
    rng = np.random.default_rng(11)
    S = rng.standard_normal((N, N))
    S = (S + S.T) / 2.0
    Dp = M + 0.8 * S
    found_m, found_d = None, None
    for m in np.linspace(-3.0, 3.0, 601):
        d = float(det_quiet(Dp + m * np.eye(N)).real)
        if not np.isfinite(d):
            continue
        if d < 0.0:
            found_m, found_d = float(m), d
            break
    check("T5a [C] a real symmetric pairing-breaking perturbation yields "
          "det < 0 at a real mass: the pairing (not realness alone) selects "
          "the zero branch", found_m is not None,
          f"det = {found_d:.3e} at m = {found_m:.3f}" if found_m is not None else "none found")
    if found_m is not None:
        d0 = float(det_quiet(M + found_m * np.eye(N)).real)
        check("T5b [C] at the same real mass the UNPERTURBED Case-A operator "
              "stays on the zero branch", d0 > 0.0, f"unperturbed det = {d0:.3e}")
    else:
        check("T5b [C] contrast check reachable", False)


def test_T6_kreality_refutation() -> None:
    print("T6 — refutation: non-K-real flavor block leaves {0, pi}")
    _, M, _ = CONFIGS[1]
    N = M.shape[0]
    Anr = brannen(1.0, 1.2, 0.3) + 0.5j * np.diag([1.0, -0.3, 0.2])
    big = np.kron(M, np.eye(3)) + np.kron(np.eye(N), Anr)
    ang = float(np.angle(det_quiet(big)))
    dist = min(abs(ang), abs(abs(ang) - np.pi))
    check("T6a [C] non-Hermitian flavor block: arg det leaves {0, pi} by a "
          "finite margin — K-reality is what discretizes the orientation",
          dist > 0.1, f"arg det = {ang:.4f} rad, distance from {{0, pi}} = {dist:.4f}")
    Ah = brannen(1.0, 1.2, 0.3)
    bigh = np.kron(M, np.eye(3)) + np.kron(np.eye(N), Ah)
    angh = float(np.angle(det_quiet(bigh)))
    check("T6b [C] restoring Hermiticity returns arg det to 0 exactly",
          abs(angh) < 1e-8, f"arg det = {angh:.2e}")


def main() -> int:
    print()
    print("=" * 72)
    print("THETA MASS-ORIENTATION ZERO BRANCH — PAIRING-FORCED ON K-REAL SURFACE")
    print("=" * 72)
    print()
    print("Companion: docs/THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md")
    print("Object: Case-A staggered M_KS (real antisymmetric, {eps, M} = 0) with")
    print("real scalar mass m of EITHER sign, or a Hermitian generation mass A on")
    print("the flavor tensor factor (Brannen dial, signed roots included).")
    print()
    test_T1_structure()
    test_T2_scalar_mass()
    test_T3_flavor_tensor()
    test_T4_squared_class()
    test_T5_pairing_refutation()
    test_T6_kreality_refutation()
    print()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print("  Scope: staggered-only Case-A surface; scalar real mass (both signs)")
    print("  or Hermitian flavor-factor mass; Wilson shifts, non-commuting")
    print("  flavor-kinetic couplings, theta_gauge, and the physical determinant-")
    print("  channel identification are OUTSIDE this runner's claims.")
    print(f"  TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"  OVERALL: {'PASS' if FAIL_COUNT == 0 else 'FAIL'}")
    print()
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
