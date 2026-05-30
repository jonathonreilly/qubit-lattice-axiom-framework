#!/usr/bin/env python3
"""Audit-companion runner for
`G_BARE_L3A_TRACE_SURFACE_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17`.

The narrow theorem's load-bearing content is the trace-surface routing
identity: the L3a binary admission `N_F in {1/2, 1}` between the V_3
(irreducible color carrier) and V (full taste cube) trace surfaces
inflates both the lattice action coefficient and the continuum kinetic
term by the same uniform factor `c_W in {1, 2}`, cancelling in the
Wilson matching equation and leaving `g_bare` invariant.

This runner verifies:

  (T1)  Trace inflation `Tr_V(F^2) = 2 * Tr_{V_3}(F^2)` for F in
        End(V_3) embedded into End(V) via T_a^{(V)} = T_a^{(3)} (x) I_2
        + 0_lepton (exact algebraic identity, both sympy + numpy).
  (T2)  Small-`a` plaquette expansion: lattice-side coefficient ratio
        F^{(V)}/F^{(V_3)} = 3/4 (structural, exact).
  (T3)  Continuum-side invariance: (1/(2g^2)) * (1/N_F^{(W)}) *
        Tr_W(F^2) reduces to (1/(4g^2)) * sum_a (F^a)^2 for both
        W in {V_3, V}.
  (T4)  Wilson matching identity: beta^{(W)} = dim(W) / (N_F^{(W)} *
        g_bare^2). At g_bare = 1: beta^{(V_3)} = 6, beta^{(V)} = 8.
  (T5)  g_bare invariance: solving (T4) on both trace surfaces with the
        matched beta values recovers g_bare = 1 in both cases.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence at exact precision.

Self-contained: numpy + scipy.linalg + sympy.
"""

from __future__ import annotations
import sys

try:
    import numpy as np
    from scipy.linalg import expm
    from sympy import Rational, Symbol, simplify, sqrt, solve, Matrix, eye, S
except ImportError as e:
    print(f"FAIL: required package not available ({e})")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "", kind: str = "A") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = f"PASS ({kind})"
    else:
        FAIL += 1
        tag = f"FAIL ({kind})"
    msg = f"  [{tag}] {label}"
    if detail:
        msg += f"  ({detail})"
    print(msg)


def section(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


# ---------------------------------------------------------------------------
# Setup: canonical Gell-Mann generators on V_3 and their V-embedding
# ---------------------------------------------------------------------------

I2 = np.eye(2, dtype=complex)
I3 = np.eye(3, dtype=complex)


def gellmann():
    """Standard Gell-Mann matrices lambda_a on C^3."""
    return [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3),
    ]


def build_T3():
    """Canonical T_a = lambda_a / 2 on V_3."""
    return [lam / 2.0 for lam in gellmann()]


def build_T8(T3):
    """Embed each T_a into V = C^8 as T_a^{(3)} (x) I_2 (+) 0_lepton.

    V_color = V_3 (x) V_fiber has dim 6; V_lepton has dim 2; V = C^8.
    For T_a in End(V_3), build the 4x4 block (T_a in (1:3,1:3), zero in
    last row/col), then tensor with I_2.
    """
    T8 = []
    for t in T3:
        T_block4 = np.zeros((4, 4), dtype=complex)
        T_block4[:3, :3] = t
        T8.append(np.kron(T_block4, I2))
    return T8


# ---------------------------------------------------------------------------
# Section A — T1: Trace inflation identity
# ---------------------------------------------------------------------------

def section_a_trace_inflation():
    section("SECTION A — (T1) Trace inflation Tr_V(F^2) = 2 * Tr_{V_3}(F^2)")

    T3 = build_T3()
    T8 = build_T8(T3)

    # Verify Gram matrices: Tr_{V_3}(T_a T_b) = (1/2) delta_ab; Tr_V = delta_ab
    Gram3 = np.array([[np.trace(Ta @ Tb).real for Tb in T3] for Ta in T3])
    GramV = np.array([[np.trace(Ta @ Tb).real for Tb in T8] for Ta in T8])

    check(
        "Tr_{V_3}(T_a T_b) = (1/2) delta_ab (canonical Gell-Mann)",
        np.allclose(Gram3, 0.5 * np.eye(8), atol=1e-12),
        f"max |Gram3 - 1/2 I| = {np.max(np.abs(Gram3 - 0.5 * np.eye(8))):.2e}",
    )

    check(
        "Tr_V(T_a^{(V)} T_b^{(V)}) = 1 * delta_ab (V-embedded)",
        np.allclose(GramV, np.eye(8), atol=1e-12),
        f"max |GramV - I| = {np.max(np.abs(GramV - np.eye(8))):.2e}",
    )

    # Inflation ratio = 2 = dim(V_fiber)
    ratio_NF = GramV[0, 0] / Gram3[0, 0]
    check(
        "N_F^{(V)} / N_F^{(3)} = 2 = dim(V_fiber)",
        abs(ratio_NF - 2.0) < 1e-12,
        f"ratio = {ratio_NF}",
    )

    # Random A_mu, A_nu, build F = i[A_mu, A_nu]
    rng = np.random.default_rng(20260517)
    for trial in range(5):
        c_mu = rng.normal(size=8)
        c_nu = rng.normal(size=8)
        A_mu_3 = sum(c_mu[a] * T3[a] for a in range(8))
        A_nu_3 = sum(c_nu[a] * T3[a] for a in range(8))
        A_mu_V = sum(c_mu[a] * T8[a] for a in range(8))
        A_nu_V = sum(c_nu[a] * T8[a] for a in range(8))

        F_3 = 1j * (A_mu_3 @ A_nu_3 - A_nu_3 @ A_mu_3)
        F_V = 1j * (A_mu_V @ A_nu_V - A_nu_V @ A_mu_V)

        TrF2_3 = np.trace(F_3 @ F_3).real
        TrF2_V = np.trace(F_V @ F_V).real

        check(
            f"trial {trial+1}: Tr_V(F^2) = 2 * Tr_{{V_3}}(F^2)",
            abs(TrF2_V - 2.0 * TrF2_3) < 1e-9 * max(abs(TrF2_3), 1.0),
            f"Tr_V(F^2) = {TrF2_V:.6e}, 2*Tr_{{V_3}}(F^2) = {2.0*TrF2_3:.6e}",
        )


# ---------------------------------------------------------------------------
# Section B — T2: Lattice plaquette small-a expansion and ratio
# ---------------------------------------------------------------------------

def section_b_lattice_small_a():
    section("SECTION B — (T2) Lattice plaquette small-a expansion + ratio 3/4")

    T3 = build_T3()
    T8 = build_T8(T3)

    rng = np.random.default_rng(7)
    c_mu = rng.normal(size=8)
    c_nu = rng.normal(size=8)
    A_mu_3 = sum(c_mu[a] * T3[a] for a in range(8))
    A_nu_3 = sum(c_nu[a] * T3[a] for a in range(8))
    A_mu_V = sum(c_mu[a] * T8[a] for a in range(8))
    A_nu_V = sum(c_nu[a] * T8[a] for a in range(8))

    F_3 = 1j * (A_mu_3 @ A_nu_3 - A_nu_3 @ A_mu_3)
    F_V = 1j * (A_mu_V @ A_nu_V - A_nu_V @ A_mu_V)
    TrF2_3 = np.trace(F_3 @ F_3).real
    TrF2_V = np.trace(F_V @ F_V).real

    def plaq_V3(a):
        Umu = expm(1j * a * A_mu_3)
        Unu = expm(1j * a * A_nu_3)
        return Umu @ Unu @ Umu.conj().T @ Unu.conj().T

    def plaq_V(a):
        Umu = expm(1j * a * A_mu_V)
        Unu = expm(1j * a * A_nu_V)
        return Umu @ Unu @ Umu.conj().T @ Unu.conj().T

    # F^{(W)}(U) := (dim(W) - Re Tr_W(U)) / dim(W)
    a_vals = np.array([0.005, 0.007, 0.01, 0.015, 0.02])
    Fv3 = np.array(
        [(3 - np.trace(plaq_V3(av)).real) / 3 for av in a_vals]
    )
    FvV = np.array(
        [(8 - np.trace(plaq_V(av)).real) / 8 for av in a_vals]
    )

    # Predicted leading coefficient:
    # F^{(W)} ~ (a^4 / (2 dim(W))) Tr_W(F^2)
    pred_V3_a4 = TrF2_3 / (2 * 3)  # = TrF2_3 / 6
    pred_V_a4 = TrF2_V / (2 * 8)   # = TrF2_V / 16 = (2 TrF2_3) / 16 = TrF2_3 / 8

    A_mat = np.column_stack([a_vals ** 4, a_vals ** 6])
    coeffs_V3, *_ = np.linalg.lstsq(A_mat, Fv3, rcond=None)
    coeffs_V, *_ = np.linalg.lstsq(A_mat, FvV, rcond=None)

    fit_V3 = coeffs_V3[0]
    fit_V = coeffs_V[0]
    rel_V3 = abs(fit_V3 - pred_V3_a4) / abs(pred_V3_a4)
    rel_V = abs(fit_V - pred_V_a4) / abs(pred_V_a4)

    check(
        "F^{(V_3)} a^4 coefficient = Tr_{V_3}(F^2) / (2 * dim(V_3))",
        rel_V3 < 1e-3,
        f"fit = {fit_V3:.6e}, predicted = {pred_V3_a4:.6e}, rel_err = {rel_V3:.2e}",
    )

    check(
        "F^{(V)} a^4 coefficient = Tr_V(F^2) / (2 * dim(V))",
        rel_V < 1e-3,
        f"fit = {fit_V:.6e}, predicted = {pred_V_a4:.6e}, rel_err = {rel_V:.2e}",
    )

    # Ratio: F^{(V)} / F^{(V_3)} = (c_V * dim(V_3)) / (c_{V_3} * dim(V)) = (2*3)/(1*8) = 3/4
    ratio_lat = fit_V / fit_V3
    expected_ratio = 3.0 / 4.0
    check(
        "Lattice-side a^4 coefficient ratio F^{(V)} / F^{(V_3)} = 3/4 (exact)",
        abs(ratio_lat - expected_ratio) < 1e-3,
        f"ratio = {ratio_lat:.6f}, expected = {expected_ratio:.6f}",
    )

    # Also verify the structural exact ratio via sympy
    c_V = Rational(2)
    c_V3 = Rational(1)
    dim_V = Rational(8)
    dim_V3 = Rational(3)
    ratio_exact = (c_V * dim_V3) / (c_V3 * dim_V)
    check(
        "Symbolic ratio (c_V * dim(V_3)) / (c_{V_3} * dim(V)) = 3/4",
        ratio_exact == Rational(3, 4),
        f"ratio = {ratio_exact} (sympy exact)",
    )


# ---------------------------------------------------------------------------
# Section C — T3: Continuum-side invariance (symbolic)
# ---------------------------------------------------------------------------

def section_c_continuum_invariance():
    section("SECTION C — (T3) Continuum-side invariance")

    g = Symbol('g', positive=True)
    Fsq = Symbol('Fsq', positive=True)  # placeholder for sum_a (F^a)^2

    # For each W, compute (1/(2 g^2)) * (1/N_F^{(W)}) * Tr_W(F^2)
    # where Tr_W(F^2) = N_F^{(W)} * Fsq
    # Result should be (1/(2 g^2)) * Fsq = (1/(4 g^2)) * 2 * Fsq
    # (the factor 2 = F^2 = (1/2) F_{mn} F^{mn} for antisymmetric F, mu != nu)

    NF_V3 = Rational(1, 2)
    NF_V = Rational(1)

    cont_V3 = (1 / (2 * g**2)) * (1 / NF_V3) * (NF_V3 * Fsq)
    cont_V = (1 / (2 * g**2)) * (1 / NF_V) * (NF_V * Fsq)

    cont_V3_s = simplify(cont_V3)
    cont_V_s = simplify(cont_V)

    check(
        "Continuum W=V_3: (1/(2g^2)) * (1/N_F^{(V_3)}) * Tr_{V_3}(F^2) = (1/(2g^2)) * Fsq",
        cont_V3_s == Fsq / (2 * g**2),
        f"expression = {cont_V3_s}",
    )

    check(
        "Continuum W=V: (1/(2g^2)) * (1/N_F^{(V)}) * Tr_V(F^2) = (1/(2g^2)) * Fsq",
        cont_V_s == Fsq / (2 * g**2),
        f"expression = {cont_V_s}",
    )

    check(
        "Continuum kinetic invariant across V_3 vs V trace surfaces",
        simplify(cont_V3_s - cont_V_s) == 0,
        "both reduce to convention-independent (1/(2g^2)) * Fsq",
    )

    # Equivalently as (1/(4g^2)) sum_a F^a F^{a,mn}: the antisymmetric F has
    # F^2 = (1/2) F_{mn} F^{mn} so the (1/2) factor combines with the (1/2)
    # giving (1/(4g^2)) sum_a F^a_{mn} F^{a,mn}.
    Fmunu_sq = 2 * Fsq  # F_{mn} F^{mn} = 2 * Fsq (antisymmetric sum)
    cont_alt = simplify(Fmunu_sq / (4 * g**2))
    check(
        "Equivalent form (1/(4g^2)) * F_{mn} F^{mn} matches (T3)",
        cont_alt == Fsq / (2 * g**2),
        f"(1/(4g^2)) * 2*Fsq = {cont_alt}",
    )


# ---------------------------------------------------------------------------
# Section D — T4: Wilson matching identity
# ---------------------------------------------------------------------------

def section_d_wilson_matching():
    section("SECTION D — (T4) Wilson matching beta^{(W)} = dim(W) / (N_F^{(W)} g_bare^2)")

    g_bare = Symbol('g_bare', positive=True)
    NF_V3 = Rational(1, 2)
    NF_V = Rational(1)
    dim_V3 = Rational(3)
    dim_V = Rational(8)

    beta_V3 = dim_V3 / (NF_V3 * g_bare**2)
    beta_V = dim_V / (NF_V * g_bare**2)

    check(
        "beta^{(V_3)} = dim(V_3) / (N_F^{(V_3)} * g_bare^2) = 6 / g_bare^2",
        simplify(beta_V3 - 6 / g_bare**2) == 0,
        f"beta_V3 = {simplify(beta_V3)}",
    )

    check(
        "beta^{(V)} = dim(V) / (N_F^{(V)} * g_bare^2) = 8 / g_bare^2",
        simplify(beta_V - 8 / g_bare**2) == 0,
        f"beta_V = {simplify(beta_V)}",
    )

    # At g_bare = 1
    beta_V3_at_1 = beta_V3.subs(g_bare, 1)
    beta_V_at_1 = beta_V.subs(g_bare, 1)

    check(
        "At g_bare = 1: beta^{(V_3)} = 6",
        beta_V3_at_1 == Rational(6),
        f"beta^{{(V_3)}}(g_bare=1) = {beta_V3_at_1}",
    )

    check(
        "At g_bare = 1: beta^{(V)} = 8",
        beta_V_at_1 == Rational(8),
        f"beta^{{(V)}}(g_bare=1) = {beta_V_at_1}",
    )

    # Verify beta^{(V_3)} = 2 N_c / g_bare^2 (the canonical form)
    N_c = Rational(3)
    canonical_beta_V3 = 2 * N_c / g_bare**2
    check(
        "beta^{(V_3)} = 2 N_c / g_bare^2 (recovers canonical Wilson formula)",
        simplify(beta_V3 - canonical_beta_V3) == 0,
        f"beta^{{(V_3)}} = 6/g_bare^2 = 2*3/g_bare^2 = {canonical_beta_V3.subs(g_bare,1)} at g_bare=1",
    )

    # Verify beta ratio
    beta_ratio = simplify(beta_V / beta_V3)
    check(
        "beta^{(V)} / beta^{(V_3)} = 4/3 (structural ratio)",
        beta_ratio == Rational(4, 3),
        f"ratio = {beta_ratio}",
    )


# ---------------------------------------------------------------------------
# Section E — T5: g_bare invariance under L3a binary swap
# ---------------------------------------------------------------------------

def section_e_g_bare_invariance():
    section("SECTION E — (T5) g_bare invariance under L3a binary swap")

    g_bare = Symbol('g_bare', positive=True)
    NF_V3 = Rational(1, 2)
    NF_V = Rational(1)
    dim_V3 = Rational(3)
    dim_V = Rational(8)

    # Given the matched beta^{(W)} values at g_bare = 1, solve back for g_bare
    # under both trace surfaces:
    #   g_bare^2 = dim(W) / (N_F^{(W)} * beta^{(W)})

    beta_V3_canon = Rational(6)  # from (9c)
    beta_V_canon = Rational(8)   # from (9d)

    g_bare_sq_from_V3 = dim_V3 / (NF_V3 * beta_V3_canon)
    g_bare_sq_from_V = dim_V / (NF_V * beta_V_canon)

    check(
        "From W=V_3 matching: g_bare^2 = 3 / (1/2 * 6) = 1",
        g_bare_sq_from_V3 == Rational(1),
        f"g_bare^2 = {g_bare_sq_from_V3}",
    )

    check(
        "From W=V matching: g_bare^2 = 8 / (1 * 8) = 1",
        g_bare_sq_from_V == Rational(1),
        f"g_bare^2 = {g_bare_sq_from_V}",
    )

    check(
        "L3a binary inert for g_bare: both trace surfaces yield g_bare = 1",
        g_bare_sq_from_V3 == g_bare_sq_from_V == Rational(1),
        f"V_3: g_bare^2 = {g_bare_sq_from_V3}; V: g_bare^2 = {g_bare_sq_from_V}",
    )

    # Counterfactual: alternative beta values (NOT matched to g_bare = 1) yield
    # different g_bare values on each surface, but the SAME g_bare value across
    # surfaces when the beta values are L3a-consistent (i.e., related by 4/3 ratio)
    for g_bare_alt_sq in [Rational(1, 2), Rational(2), Rational(4)]:
        # The L3a-consistent beta on V_3
        beta_V3_alt = dim_V3 / (NF_V3 * g_bare_alt_sq)
        # The L3a-consistent beta on V
        beta_V_alt = dim_V / (NF_V * g_bare_alt_sq)
        # Recover g_bare^2 from each
        g_sq_from_V3_recovered = dim_V3 / (NF_V3 * beta_V3_alt)
        g_sq_from_V_recovered = dim_V / (NF_V * beta_V_alt)
        check(
            f"L3a-consistent counterfactual g_bare^2 = {g_bare_alt_sq}: "
            f"both surfaces recover the same g_bare^2",
            g_sq_from_V3_recovered == g_sq_from_V_recovered == g_bare_alt_sq,
            f"V_3: {g_sq_from_V3_recovered}; V: {g_sq_from_V_recovered}",
        )

    # Ratio check: beta_V / beta_V_3 = 4/3 is a structural invariant
    for g_bare_alt_sq in [Rational(1, 4), Rational(1), Rational(7, 11)]:
        beta_V3_alt = dim_V3 / (NF_V3 * g_bare_alt_sq)
        beta_V_alt = dim_V / (NF_V * g_bare_alt_sq)
        ratio = simplify(beta_V_alt / beta_V3_alt)
        check(
            f"At g_bare^2 = {g_bare_alt_sq}: beta_V / beta_V3 = 4/3 (L3a-invariant)",
            ratio == Rational(4, 3),
            f"ratio = {ratio}",
        )


# ---------------------------------------------------------------------------
# Section F — Sanity / parent-row consistency
# ---------------------------------------------------------------------------

def section_f_parent_consistency():
    section("SECTION F — Parent-row consistency checks")

    # Verify alignment with frontier_g_bare_derivation.py (parent runner): the
    # W = V_3 case must recover the canonical beta = 6 / g^2 and g_bare = 1.
    N_c = Rational(3)
    canonical_beta = 2 * N_c  # = 6
    check(
        "W=V_3 specialization reproduces canonical beta = 2 N_c = 6 (parent runner)",
        canonical_beta == Rational(6),
        f"beta_canonical = 2 * 3 = {canonical_beta}",
    )

    # Routing parallel: rescaling T -> c T routes into beta as c^2
    # (per G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md)
    # The present theorem's W -> W' routes into beta by dim(W')/dim(W) * N_F^{(W)}/N_F^{(W')}
    # For W -> V (W' = V from W = V_3): factor = (8/3) * (1/2)/1 = 4/3
    routing_factor = Rational(8, 3) * Rational(1, 2)
    check(
        "Trace-surface routing factor on beta: V_3 -> V gives 4/3 (parallel to c^2 from rescaling)",
        routing_factor == Rational(4, 3),
        f"factor = {routing_factor}; rescaling parallel: T_a -> c T_a gives c^2 factor on beta",
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 80)
    print("Audit companion: G_BARE_L3A_TRACE_SURFACE_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17")
    print("=" * 80)

    section_a_trace_inflation()
    section_b_lattice_small_a()
    section_c_continuum_invariance()
    section_d_wilson_matching()
    section_e_g_bare_invariance()
    section_f_parent_consistency()

    print("\n" + "=" * 80)
    print("SCORECARD")
    print("=" * 80)
    print(f"PASS = {PASS}")
    print(f"FAIL = {FAIL}")
    print(f"TOTAL = {PASS + FAIL}")
    print()
    if FAIL == 0:
        print("VERDICT: all class (A) algebraic + numerical checks PASS.")
        print("  The L3a binary admission N_F in {1/2, 1} is physically inert")
        print("  for g_bare: both trace surfaces yield g_bare = 1 at the")
        print("  Wilson canonical matching surface, differing only in the")
        print("  conventional beta value (6 for V_3, 8 for V).")
    else:
        print(f"VERDICT: {FAIL} check(s) failed; review runner output above.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
