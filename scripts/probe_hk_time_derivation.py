"""Trace/Wilson identities and formal leading short-time Gaussian matching.

The heat-kernel quadratic coefficient is not exactly1/(2t) at fixed t.
Substituting beta6 into t_leading=2Nc/beta is illustrative, not finite-time
matching or action selection. Original source recoverable at f24d17d97d372df977476e4a69674577f31af575.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300

from fractions import Fraction
from typing import Tuple

import sympy as sp
import math


def gell_mann() -> list[sp.Matrix]:
    """Hermitian Gell-Mann matrices λ_a (a=1..8); T_a = λ_a / 2.

    Standard SU(3) basis with normalization Tr(λ_a λ_b) = 2 δ_{ab},
    equivalently Tr(T_a T_b) = δ_{ab}/2.
    """
    s = sp.sqrt(3)
    L = [None] * 9  # 1-indexed
    L[1] = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    L[2] = sp.Matrix([[0, -sp.I, 0], [sp.I, 0, 0], [0, 0, 0]])
    L[3] = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    L[4] = sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
    L[5] = sp.Matrix([[0, 0, -sp.I], [0, 0, 0], [sp.I, 0, 0]])
    L[6] = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    L[7] = sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]])
    L[8] = (1 / s) * sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]])
    return [L[i] for i in range(1, 9)]


def check_canonical_normalization() -> Tuple[bool, str]:
    """Verify Tr(T_a T_b) = δ_{ab}/2 with T_a = λ_a/2."""
    L = gell_mann()
    T = [l / 2 for l in L]
    issues = []
    for a in range(8):
        for b in range(8):
            tr = sp.trace(T[a] * T[b])
            tr = sp.simplify(tr)
            expected = sp.Rational(1, 2) if a == b else sp.S.Zero
            if tr != expected:
                issues.append(f"Tr(T_{a+1} T_{b+1}) = {tr}, expected {expected}")
    if issues:
        return False, "Tr-form check failed: " + "; ".join(issues[:3])
    return True, f"Tr(T_a T_b) = δ_{{ab}}/2 verified for all 8×8=64 pairs"


def check_orthonormal_basis_under_inner_product() -> Tuple[bool, str]:
    """Verify {T_a} is orthonormal under ⟨X, Y⟩ = 2·Tr(X Y).

    By definition: ⟨T_a, T_b⟩ = 2 · Tr(T_a T_b) = 2 · δ_{ab}/2 = δ_{ab}.
    """
    L = gell_mann()
    T = [l / 2 for l in L]
    issues = []
    for a in range(8):
        for b in range(8):
            ip = sp.simplify(2 * sp.trace(T[a] * T[b]))
            expected = sp.S.One if a == b else sp.S.Zero
            if ip != expected:
                issues.append(f"⟨T_{a+1}, T_{b+1}⟩ = {ip}, expected {expected}")
    if issues:
        return False, "Orthonormal check failed: " + "; ".join(issues[:3])
    return True, "{T_a} orthonormal under ⟨X,Y⟩ = 2·Tr(XY): all 64 inner products correct"


def check_small_u_wilson_expansion() -> Tuple[bool, str]:
    """Verify Re Tr exp(iX) = N_c - (1/2) Tr(X²) + O(X⁴) at quadratic order.

    Uses sympy symbolic expansion in a small parameter ε; truncates to
    O(ε²) and confirms the coefficient matches.
    """
    L = gell_mann()
    T = [l / 2 for l in L]
    eps = sp.Symbol('eps', real=True, positive=True)

    # Pick a test X = ε · T_3 (diagonal Cartan element); generalizable
    # since the result is basis-independent.
    X = eps * T[2]  # T_3 in 0-indexed = T_3 in 1-indexed naming
    iX = sp.I * X

    # exp(iX) = I + iX - X²/2 + ... — keep through O(ε²)
    I3 = sp.eye(3)
    U = I3 + iX + sp.Rational(1, 2) * iX * iX

    re_tr_U = sp.simplify(sp.re(sp.trace(U)))
    # re_tr_U should equal N_c - (1/2) Tr(X²) + O(ε⁴)
    expected = 3 - sp.Rational(1, 2) * sp.trace(X * X)
    expected = sp.simplify(expected)

    diff = sp.simplify(re_tr_U - expected)
    if diff != 0:
        return False, f"Wilson small-U expansion mismatch: re_tr_U - expected = {diff}"
    return True, f"Re Tr exp(iX) = N_c - (1/2)Tr(X²) verified: re_tr_U = {re_tr_U}"


def check_norm_squared_under_canonical_basis() -> Tuple[bool, str]:
    """Verify Tr(X²) = (1/2) |X|² where |X|² = Σ_a (X^a)² (canonical basis).

    For X = X^a T_a with Tr(T_a T_b) = δ_{ab}/2:
       Tr(X²) = X^a X^b Tr(T_a T_b) = X^a X^b · δ_{ab}/2 = (1/2) |X|²
    """
    L = gell_mann()
    T = [l / 2 for l in L]
    X_a = sp.symbols('X1:9', real=True)
    X = sp.zeros(3, 3)
    for a in range(8):
        X = X + X_a[a] * T[a]
    tr_x_sq = sp.simplify(sp.trace(X * X))
    expected = sp.Rational(1, 2) * sum(X_a[a] ** 2 for a in range(8))
    expected = sp.simplify(expected)
    diff = sp.simplify(tr_x_sq - expected)
    if diff != 0:
        return False, f"Tr(X²) ≠ (1/2)|X|²: diff = {diff}"
    return True, "Tr(X²) = (1/2) Σ_a (X^a)² verified symbolically"


def derive_t_from_canonical_match(beta: sp.Expr, N_c: int = 3) -> sp.Expr:
    """Derive t from the formal leading short-time Gaussian matching.

    Wilson per-plaquette small-U:
       S_W = β · (1 - (1/N_c) Re Tr U)
           = β · (1/N_c) · (1/2) Tr(X²)
           = β · (1/N_c) · (1/2) · (1/2) |X|²
           = (β / (4 N_c)) |X|²

    Assumed leading short-time Gaussian:
       S_HK_dyn = |X|² / (2 t)

    Match: β / (4 N_c) = 1 / (2 t) → t = 2 N_c / β
    """
    return 2 * N_c / beta


def main() -> None:
    print("=" * 72)
    print("Block 01 R1.A — Conditional Gaussian matching and trace identities")
    print("Companion: docs/BRIDGE_GAP_HK_TIME_DERIVATION_NOTE_2026-05-06.md")
    print("=" * 72)
    print()

    checks = []

    # K1 — canonical Tr-form
    ok, msg = check_canonical_normalization()
    checks.append(("K1 canonical Tr-form", ok, msg))

    # K2 — orthonormal {T_a} under ⟨X,Y⟩ = 2·Tr(XY)
    ok, msg = check_orthonormal_basis_under_inner_product()
    checks.append(("K2 orthonormal basis", ok, msg))

    # K3 — Wilson small-U expansion
    ok, msg = check_small_u_wilson_expansion()
    checks.append(("K3 Wilson small-U expansion", ok, msg))

    # K4 — Tr(X²) = (1/2) |X|²
    ok, msg = check_norm_squared_under_canonical_basis()
    checks.append(("K4 Tr(X²) → (1/2) |X|²", ok, msg))

    # K5 — formal leading Gaussian parameter evaluated at supplied beta6
    beta = sp.Symbol('beta', positive=True)
    t_general = derive_t_from_canonical_match(beta, N_c=3)
    t_at_6 = t_general.subs(beta, 6)
    expected_t = sp.S.One
    ok = sp.simplify(t_at_6 - expected_t) == 0
    msg = (
        f"t(β) = {t_general} = 2·N_c/β; t(6) = {t_at_6} (expected 1)"
    )
    checks.append(("K5 formal Gaussian parameter at beta6 = 1", ok, msg))

    # K6 — supplied beta=2Nc/g² convention in the formal leading identity
    g_bare = sp.Symbol('g_bare', positive=True)
    beta_in_terms_of_g = 2 * 3 / g_bare ** 2  # SU(3): β = 2 N_c / g²
    t_in_terms_of_g = derive_t_from_canonical_match(beta_in_terms_of_g, N_c=3)
    t_simplified = sp.simplify(t_in_terms_of_g)
    expected = g_bare ** 2
    ok = sp.simplify(t_simplified - expected) == 0
    msg = f"t = 2·N_c/β = {t_simplified}; expected g_bare² = {expected}"
    checks.append(("K6 formal Gaussian parameter = supplied g_bare²", ok, msg))

    # K7 — Casimir-form preview: ⟨P⟩_HK,1plaq(t) = exp(-2t/3) at t=1 = exp(-2/3)
    t = sp.S.One
    avg = sp.exp(-2 * t / 3)
    avg_eval = sp.N(avg, 15)
    msg = f"⟨P⟩_HK,1plaq(t=1) = exp(-2/3) = {avg_eval}"
    print("SUPPLIED t=1 character expectation preview (not a new check): " + msg)

    # Numerical diagnostic of the exact-character Hessian, truncated in p,q.
    # No infinite-tail bound is claimed by the agreement of two cutoffs.
    coefficients=[]
    for cutoff in (8,12,20,30):
        normalizer=weighted=0.0
        for p in range(cutoff+1):
            for q in range(cutoff+1):
                dim=(p+1)*(q+1)*(p+q+2)/2
                casimir=(p*p+p*q+q*q+3*p+3*q)/3
                weight=dim**2*math.exp(-casimir/2)
                normalizer+=weight
                weighted+=weight*casimir
        coefficient=weighted/(16*normalizer)
        coefficients.append(coefficient)
        print(f"NUMERICAL t1 Hessian coefficient, p,q<={cutoff}: {coefficient:.16g}")
    checks.append(("K8 finite-cutoff Hessian sums stabilize",abs(coefficients[-1]-coefficients[-2])<1e-12,"No infinite-tail certificate"))
    checks.append(("K9 fixed-time Gaussian negative control",abs(coefficients[-1]-.5)>.05,"Numerical discrepancy from assumed0.5"))

    # Print results
    n_pass = sum(1 for _, ok, _ in checks if ok)
    n_total = len(checks)
    for name, ok, msg in checks:
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: {msg}")
    print()
    print(f"SUMMARY: PASS={n_pass} FAIL={n_total - n_pass}")
    print()
    print("Conditional leading Gaussian coefficient identity: t_leading = 2 N_c / beta.")
    print("At supplied beta6 the formal substitution is1; exact finite-time matching is not proved.")
    print()
    print("Supplied t=1 preview: ⟨P⟩_HK,1plaq(t=1) = exp(-2/3) ≈ 0.5134171190")

    raise SystemExit(0 if all(ok for _, ok, _ in checks) else 1)

if __name__ == "__main__":
    main()
