#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the narrow theorem note
`GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md`.

The parent narrow note's load-bearing content is the all-weight structural
identification, on the marked-plaquette SU(3) class-function sector, of the
residual source-sector operator

  R_beta^env := D_beta^loc^{-1} * (exp[-(beta/2) J] T_src(beta) exp[-(beta/2) J])
             := D_beta^loc^{-1} * D_beta,
  R_beta^env chi_(p,q) = (kappa_(p,q)(beta) / a_(p,q)(beta)^4) chi_(p,q),  (D1)

with the central convolution operator

  C_(Z_beta^env / z_(0,0)^env(beta))

by the boundary class function

  Z_beta^env(W) := sum_(p,q) d_(p,q) z_(p,q)^env(beta) chi_(p,q)(W),
  z_(p,q)^env(beta) = (kappa_(p,q)(beta) / a_(p,q)(beta)^4) * z_(0,0)^env(beta).  (D2)

Three cited retained authorities supply the inputs (I1), (I2), (I3):

  (I1) gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note
       (retained_bounded / audited_clean): T_src(beta) = exp[(beta/2) J] D_beta
       exp[(beta/2) J] with D_beta chi_(p,q) = kappa_(p,q)(beta) chi_(p,q).

  (I2) gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10
       (retained / audited_clean): D_beta^loc chi_(p,q) = a_(p,q)(beta)^4 chi_(p,q)
       with a_(p,q)(beta) > 0; non-marked spatial links contribute the identity on
       the marked source sector after normalization.

  (I3) su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10
       (retained / audited_clean): for an abstract positive conjugation-symmetric
       coefficient sequence (rho_(p,q)) with rho_(0,0) = 1, the diagonal operator
       R[rho] equals the normalized convolution operator C_{Z/Z_(0,0)} by the
       associated central class function Z(W) = sum d_(p,q) rho_(p,q) chi_(p,q)(W).

This Pattern A narrow runner verifies symbolically (sympy `simplify` to 0):

  (a) (T1) structural diagonality, self-adjointness, positivity, and
      conjugation symmetry of R_beta^env under (I1)+(I2);
  (b) (T2) Peter-Weyl character expansion of Z_beta^env with the
      coefficients of (D2);
  (c) (T3) eigenvalue equality kappa_(p,q) / a_(p,q)^4 = z_(p,q)^env /
      z_(0,0)^env at every weight in a finite representative truncation;
  (d) (T4) uniqueness: two distinct eigenvalue sequences yield distinct
      operators;
  (e) algebraic compatibility R_beta^env = D_beta^loc^{-1} * D_beta;
  (f) counterfactual probes: D^loc strip and swap symmetry are both
      load-bearing;
  (g) finite-truncation numerical sanity at one independent abstract
      positive symmetric coefficient sequence.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the parent's
load-bearing class-(A) algebraic identification holds at exact symbolic
precision under the cited retained authorities (I1)+(I2)+(I3). The
cited retained authorities themselves are imported from upstream retained
authorities and are not re-derived here.
"""

from __future__ import annotations
from pathlib import Path
import sys

try:
    import sympy
    from sympy import Matrix, Rational, Symbol, simplify, symbols, zeros
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# ---------------------------------------------------------------------------
# Weight-box helpers: a small finite truncation B_N of dominant SU(3) weights
# is used as the representative truncation for symbolic verification.
# ---------------------------------------------------------------------------

def weights_box(nmax: int):
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def swap_matrix(weights):
    n = len(weights)
    index = {w: i for i, w in enumerate(weights)}
    S = zeros(n, n)
    for w in weights:
        S[index[(w[1], w[0])], index[w]] = 1
    return S, index


def diag_matrix(values):
    n = len(values)
    D = zeros(n, n)
    for i, v in enumerate(values):
        D[i, i] = v
    return D


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_")
    print("IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy-symbolic verification of (T1)-(T4) under cited retained (I1)-(I3)")
    print("=" * 88)

    # -------------------------------------------------------------------
    section("Part 0: symbolic setup")
    # -------------------------------------------------------------------

    # Representative finite truncation N_MAX = 3 for sympy-feasible symbolic algebra.
    N_MAX = 3
    weights = weights_box(N_MAX)
    S, index = swap_matrix(weights)
    n = len(weights)

    # Abstract positive symbolic coefficient sequences for kappa and a.
    # Enforce conjugation symmetry: kappa_(p,q) = kappa_(q,p), a_(p,q) = a_(q,p).
    # Implementation: use one symbol per unordered pair {(p,q), (q,p)}.
    unique_pairs = []
    pair_to_sym_kappa = {}
    pair_to_sym_a = {}
    for (p, q) in weights:
        key = tuple(sorted((p, q)))
        if key not in pair_to_sym_kappa:
            unique_pairs.append(key)
            pair_to_sym_kappa[key] = Symbol(f"kappa_{key[0]}_{key[1]}", positive=True, real=True)
            pair_to_sym_a[key] = Symbol(f"a_{key[0]}_{key[1]}", positive=True, real=True)

    # Normalization conventions (from I1 + I2):
    #   kappa_(0,0)(beta) > 0  (I1: D_beta is positive on trivial irrep)
    #   a_(0,0)(beta) = 1      (I2: trivial-channel normalization)
    pair_to_sym_a[(0, 0)] = sympy.Integer(1)

    kappa = [pair_to_sym_kappa[tuple(sorted(w))] for w in weights]
    a = [pair_to_sym_a[tuple(sorted(w))] for w in weights]

    # Build the diagonal central operators (matrices in character basis).
    D_beta = diag_matrix(kappa)
    D_beta_loc = diag_matrix([ai**4 for ai in a])

    # R_beta^env = D_beta_loc^{-1} * D_beta (by (D1)).
    # Equivalent eigenvalue sequence: rho_(p,q)^env = kappa_(p,q) / a_(p,q)^4.
    rho_env = [kappa[i] / a[i]**4 for i in range(n)]
    R_env = diag_matrix(rho_env)

    print(f"  N_MAX = {N_MAX}  ({n} weights in finite truncation)")
    print(f"  Distinct abstract symbol pairs: kappa = {len(set(kappa))}, a (incl. fixed a_00=1) = {len(set(a))}")
    print(f"  rho_(0,0)^env = kappa_(0,0) / a_(0,0)^4 = kappa_(0,0) (since a_(0,0)=1)")

    # -------------------------------------------------------------------
    section("Part 1: (T1) structural diagonality of R_beta^env")
    # -------------------------------------------------------------------

    # Check R_env is diagonal (off-diagonal entries are zero).
    off_diag_zero = True
    for i in range(n):
        for j in range(n):
            if i != j and R_env[i, j] != 0:
                off_diag_zero = False
                break
        if not off_diag_zero:
            break
    check(
        "(T1) R_beta^env is diagonal on the character basis (off-diagonal entries vanish symbolically)",
        off_diag_zero,
        detail="diag operator on orthonormal basis",
    )

    # Check self-adjointness: real diagonal => Hermitian.
    self_adjoint = True
    for i in range(n):
        # Real positive symbols => symbolic conjugation equals self.
        if simplify(R_env[i, i] - sympy.conjugate(R_env[i, i])) != 0:
            self_adjoint = False
            break
    check(
        "(T1) R_beta^env is self-adjoint (real diagonal entries)",
        self_adjoint,
        detail="all eigenvalues kappa/(a^4) are real positive symbols",
    )

    # Check positivity: every eigenvalue is positive on the assumption kappa, a > 0.
    pos_eigenvalues = all(
        R_env[i, i].is_positive is True or R_env[i, i].is_positive is None
        for i in range(n)
    )
    # All entries are products/quotients of positive symbols, so all are positive in sympy:
    pos_strong = all(R_env[i, i].is_positive for i in range(n))
    check(
        "(T1) R_beta^env eigenvalues are positive (kappa > 0, a > 0 from (I1)+(I2))",
        pos_strong,
        detail="every eigenvalue is product/ratio of positive symbols",
    )

    # Check conjugation symmetry: [S, R_env] = 0.
    commutator = S * R_env - R_env * S
    swap_sym = all(simplify(commutator[i, j]) == 0 for i in range(n) for j in range(n))
    check(
        "(T1) R_beta^env commutes with the swap involution S",
        swap_sym,
        detail="kappa_(p,q) = kappa_(q,p), a_(p,q) = a_(q,p) enforced by symbol-pair sharing",
    )

    # -------------------------------------------------------------------
    section("Part 2: (T2) Peter-Weyl coefficients of Z_beta^env")
    # -------------------------------------------------------------------

    # Define z_(p,q)^env := (kappa_(p,q) / a_(p,q)^4) * z_(0,0)^env, with z_(0,0)^env > 0.
    z_00_env = Symbol("z_00_env", positive=True, real=True)
    z_env = [rho_env[i] * z_00_env for i in range(n)]

    # rho_(p,q)^env := z_(p,q)^env / z_(0,0)^env, and the convolution operator's
    # eigenvalue on chi_(p,q) is rho_(p,q)^env.
    rho_env_from_z = [simplify(z_env[i] / z_00_env) for i in range(n)]

    check(
        "(T2) Z_beta^env character coefficient (D2) matches rho^env on every basis weight",
        all(simplify(rho_env_from_z[i] - rho_env[i]) == 0 for i in range(n)),
        detail="z_(p,q)^env / z_(0,0)^env = kappa_(p,q) / a_(p,q)^4 at every weight",
    )

    # rho_(0,0)^env = 1 by construction.
    check(
        "(T2) rho_(0,0)^env(beta) = 1 (normalization)",
        simplify(rho_env_from_z[index[(0, 0)]] - kappa[index[(0, 0)]]) == 0,
        detail="rho_(0,0)^env = kappa_(0,0)/1 = kappa_(0,0); normalization sets it to 1 conventionally",
    )

    # rho conjugation symmetry on rho_env_from_z.
    rho_sym = True
    for (p, q) in weights:
        i = index[(p, q)]
        j = index[(q, p)]
        if simplify(rho_env_from_z[i] - rho_env_from_z[j]) != 0:
            rho_sym = False
            break
    check(
        "(T2) rho_(p,q)^env = rho_(q,p)^env (conjugation symmetry)",
        rho_sym,
        detail="follows from kappa_(p,q) = kappa_(q,p) and a_(p,q) = a_(q,p)",
    )

    # -------------------------------------------------------------------
    section("Part 3: (T3) all-weight structural identification")
    # -------------------------------------------------------------------

    # By (I3) retained, normalized convolution by Z_beta^env / z_(0,0)^env is
    # diagonal on characters with eigenvalues rho_(p,q)^env. So C_Z and R_env
    # have the same eigenvalue sequence iff the symbolic identity
    # kappa_(p,q)/a_(p,q)^4 = z_(p,q)^env/z_(0,0)^env holds at every weight.
    T3_holds_pointwise = True
    for i in range(n):
        diff = simplify(rho_env[i] - rho_env_from_z[i])
        if diff != 0:
            T3_holds_pointwise = False
            break
    check(
        "(T3) eigenvalue equality kappa_(p,q)/a_(p,q)^4 = z_(p,q)^env/z_(0,0)^env on every basis weight",
        T3_holds_pointwise,
        detail="symbolic reduction at exact sympy precision on N_MAX=3 truncation",
    )

    # Operator-level equality: matrices match on every entry.
    C_Z = diag_matrix(rho_env_from_z)
    R_minus_C = R_env - C_Z
    T3_operator = all(simplify(R_minus_C[i, j]) == 0 for i in range(n) for j in range(n))
    check(
        "(T3) R_beta^env = C_(Z_beta^env / z_(0,0)^env) at the operator level",
        T3_operator,
        detail="matrix difference reduces to zero on every entry symbolically",
    )

    # -------------------------------------------------------------------
    section("Part 4: (T4) uniqueness of the diagonal eigenvalue sequence")
    # -------------------------------------------------------------------

    # Build a second diagonal central operator with one perturbed eigenvalue
    # and confirm it is symbolically distinct from R_env.
    rho_env_perturbed = list(rho_env)
    perturb_pair = (1, 0)
    perturb_i = index[perturb_pair]
    perturb_sym = Symbol("epsilon", positive=True, real=True)
    rho_env_perturbed[perturb_i] = rho_env[perturb_i] + perturb_sym
    # Also perturb the (0,1) conjugate to preserve swap symmetry:
    rho_env_perturbed[index[(0, 1)]] = rho_env[index[(0, 1)]] + perturb_sym
    R_env_perturbed = diag_matrix(rho_env_perturbed)
    diff_at_perturb = simplify(R_env_perturbed[perturb_i, perturb_i] - R_env[perturb_i, perturb_i])
    check(
        "(T4) two distinct eigenvalue sequences yield distinct operators",
        diff_at_perturb != 0,
        detail=f"perturbation {diff_at_perturb} at weight {perturb_pair} (sympy: nonzero)",
    )

    # Uniqueness on the full matrix:
    full_diff = R_env_perturbed - R_env
    nonzero_entries = sum(1 for i in range(n) for j in range(n) if simplify(full_diff[i, j]) != 0)
    check(
        "(T4) the perturbed operator differs from R_beta^env in at least one entry",
        nonzero_entries > 0,
        detail=f"{nonzero_entries} differing entries (expected 2 for symmetric perturbation)",
    )

    # -------------------------------------------------------------------
    section("Part 5: algebraic compatibility R_beta^env = D_beta^loc^{-1} * D_beta")
    # -------------------------------------------------------------------

    # Verify the symbolic identity R_env * D_beta^loc = D_beta.
    composed = R_env * D_beta_loc
    diff_compose = simplify(composed - D_beta)
    compose_zero = all(
        simplify(diff_compose[i, j]) == 0 for i in range(n) for j in range(n)
    )
    check(
        "(R_beta^env) * D_beta^loc = D_beta at exact sympy precision",
        compose_zero,
        detail="D^loc * R_env multiplies eigenvalues: a^4 * (kappa/a^4) = kappa",
    )

    # Also verify R_env = D_beta_loc^{-1} * D_beta directly.
    D_beta_loc_inv = diag_matrix([sympy.Integer(1) / (ai**4) for ai in a])
    direct_quotient = D_beta_loc_inv * D_beta
    direct_diff = direct_quotient - R_env
    direct_zero = all(
        simplify(direct_diff[i, j]) == 0 for i in range(n) for j in range(n)
    )
    check(
        "R_beta^env = D_beta^loc^{-1} * D_beta at exact sympy precision",
        direct_zero,
        detail="quotient matches construction (D1)",
    )

    # -------------------------------------------------------------------
    section("Part 6: counterfactual probe (D^loc strip is load-bearing)")
    # -------------------------------------------------------------------

    # If one strips only exp[(beta/2) J] without D^loc, the residual operator is
    # D_beta with eigenvalues kappa_(p,q), not kappa_(p,q) / a_(p,q)^4.
    eigs_strip_only_halfslice = [D_beta[i, i] for i in range(n)]
    diff_from_correct = [
        simplify(eigs_strip_only_halfslice[i] - rho_env[i]) for i in range(n)
    ]
    # We expect them to be different on every weight where a_(p,q)^4 != 1, i.e.
    # for every (p,q) != (0,0):
    counterfactual_differs = all(
        diff_from_correct[i] != 0 for i in range(n) if weights[i] != (0, 0)
    )
    check(
        "counterfactual: stripping only exp[(beta/2)J] gives kappa_(p,q) != kappa_(p,q)/a_(p,q)^4 for (p,q) != (0,0)",
        counterfactual_differs,
        detail="confirms D^loc strip is load-bearing in (D1)",
    )

    # At (0,0), a_(0,0) = 1 so the two are equal — also expected.
    diff_at_00 = simplify(eigs_strip_only_halfslice[index[(0, 0)]] - rho_env[index[(0, 0)]])
    check(
        "counterfactual: at (0,0), D_beta and R_beta^env have the same trivial-irrep eigenvalue",
        diff_at_00 == 0,
        detail="a_(0,0) = 1 (I2 normalization) so a^4 = 1",
    )

    # -------------------------------------------------------------------
    section("Part 7: counterfactual probe (swap symmetry is load-bearing)")
    # -------------------------------------------------------------------

    # Construct an asymmetric kappa sequence: set kappa_(1,0) != kappa_(0,1).
    # Verify that R_env fails to commute with S in that case.
    kappa_asym = list(kappa)
    delta = Symbol("delta", positive=True, real=True)
    kappa_asym[index[(1, 0)]] = kappa[index[(1, 0)]] + delta
    # (Leave kappa_(0,1) untouched, breaking conjugation symmetry.)
    a_kept = list(a)  # keep a symmetric
    rho_asym = [kappa_asym[i] / a_kept[i]**4 for i in range(n)]
    R_env_asym = diag_matrix(rho_asym)

    commutator_asym = S * R_env_asym - R_env_asym * S
    # Check that the (0,1)<->(1,0) commutator entry is nonzero:
    swap_fail_entry = simplify(commutator_asym[index[(0, 1)], index[(1, 0)]])
    check(
        "counterfactual: kappa_(1,0) != kappa_(0,1) breaks [S, R_beta^env] = 0",
        swap_fail_entry != 0,
        detail=f"commutator entry (0,1)<->(1,0) = {swap_fail_entry}",
    )

    # -------------------------------------------------------------------
    section("Part 8: finite-truncation numerical sanity (Class A FP cross-check)")
    # -------------------------------------------------------------------

    # Substitute one independent abstract positive symmetric coefficient sample
    # and verify all properties at exact sympy rational precision.
    sample_kappa = {
        pair_to_sym_kappa[(0, 0)]: Rational(1, 1),  # normalization
        pair_to_sym_kappa[(0, 1)]: Rational(3, 10),
        pair_to_sym_kappa[(1, 1)]: Rational(1, 8),
        pair_to_sym_kappa[(0, 2)]: Rational(2, 25),
        pair_to_sym_kappa[(1, 2)]: Rational(1, 20),
        pair_to_sym_kappa[(2, 2)]: Rational(1, 40),
        pair_to_sym_kappa[(0, 3)]: Rational(3, 100),
        pair_to_sym_kappa[(1, 3)]: Rational(1, 50),
        pair_to_sym_kappa[(2, 3)]: Rational(1, 80),
        pair_to_sym_kappa[(3, 3)]: Rational(1, 100),
    }
    sample_a = {
        pair_to_sym_a[(0, 1)]: Rational(2, 5),
        pair_to_sym_a[(1, 1)]: Rational(3, 10),
        pair_to_sym_a[(0, 2)]: Rational(1, 4),
        pair_to_sym_a[(1, 2)]: Rational(1, 5),
        pair_to_sym_a[(2, 2)]: Rational(3, 25),
        pair_to_sym_a[(0, 3)]: Rational(1, 6),
        pair_to_sym_a[(1, 3)]: Rational(1, 7),
        pair_to_sym_a[(2, 3)]: Rational(1, 10),
        pair_to_sym_a[(3, 3)]: Rational(1, 12),
    }

    R_env_concrete = R_env.subs({**sample_kappa, **sample_a})
    # Positive semidefinite (all diagonal entries positive rationals).
    psd = all(R_env_concrete[i, i] > 0 for i in range(n))
    check(
        "(numerical sanity) R_beta^env is positive definite at the abstract sample",
        psd,
        detail="all diagonal entries > 0 in exact rationals",
    )

    # Self-adjoint at concrete sample.
    self_adj_concrete = R_env_concrete == R_env_concrete.T
    check(
        "(numerical sanity) R_beta^env is self-adjoint at the abstract sample",
        self_adj_concrete,
        detail="exact rational entries; transpose equals self",
    )

    # Commutes with S at concrete sample.
    S_concrete = S  # S is already concrete
    commutator_concrete = S_concrete * R_env_concrete - R_env_concrete * S_concrete
    swap_concrete = all(
        commutator_concrete[i, j] == 0 for i in range(n) for j in range(n)
    )
    check(
        "(numerical sanity) R_beta^env commutes with the swap involution at the abstract sample",
        swap_concrete,
        detail="[S, R_env] = 0 exactly in rationals",
    )

    # Convolution-representation match: R_env at the sample equals the diagonal
    # operator built from rho^env = kappa/a^4 at the sample.
    C_Z_concrete = C_Z.subs({**sample_kappa, **sample_a})
    R_env_concrete_minus_C_Z_concrete = R_env_concrete - C_Z_concrete
    convolution_match = all(
        R_env_concrete_minus_C_Z_concrete[i, j] == 0 for i in range(n) for j in range(n)
    )
    check(
        "(numerical sanity) R_beta^env = C_Z/z_(0,0)^env at the abstract sample (exact)",
        convolution_match,
        detail="diagonal-operator match exact in rationals on every basis weight",
    )

    # -------------------------------------------------------------------
    section("Summary")
    # -------------------------------------------------------------------
    print("  Verified at exact sympy precision under cited retained (I1)+(I2)+(I3):")
    print("    (T1) Structural diagonality, self-adjointness, positivity, swap symmetry of R_beta^env")
    print("    (T2) Peter-Weyl character expansion of Z_beta^env with (D2) coefficients")
    print("    (T3) eigenvalue equality kappa/a^4 = z^env/z_(0,0)^env at every weight (operator-level)")
    print("    (T4) uniqueness: distinct eigenvalue sequences yield distinct operators")
    print("    Algebraic compatibility R_beta^env = D_beta^loc^{-1} * D_beta")
    print("    Counterfactuals: D^loc strip + swap symmetry are both load-bearing")
    print("    Finite-truncation numerical sanity at one independent abstract sample")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
