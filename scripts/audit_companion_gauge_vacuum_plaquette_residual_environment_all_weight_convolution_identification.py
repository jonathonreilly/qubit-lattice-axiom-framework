#!/usr/bin/env python3
"""Exact symbolic checks for supplied diagonal quotient/convolution algebra.

The runner assumes two explicit character-diagonal coefficient families,

    D chi_(p,q) = kappa_(p,q) chi_(p,q),
    D_loc chi_(p,q) = a_(p,q)^4 chi_(p,q),

with kappa nonnegative and a strictly positive.  It checks exactly that
R=D_loc^{-1}D has eigenvalues kappa/a^4 and that the same supplied sequence
has the finite-window formal central-convolution packaging given by Schur
orthogonality.

This runner does not derive D from a Wilson kernel, does not prove that a
stripped Wilson compression is character-diagonal, and does not identify the
formal sequence with an independently constructed physical environment.
"""

from __future__ import annotations
import math
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

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md"
WILSON_NOTE_PATH = ROOT / "docs" / "WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md"
WILSON_RUNNER_PATH = ROOT / "scripts" / "wilson_su3_gauge_transfer_kernel_positivity_2026-05-30.py"
SELF_RUNNER = "scripts/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.py"
SELF_CACHE = "logs/runner-cache/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.txt"


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


def tensor_fundamental_counts(counts: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    """SU(3) tensor rule for multiplying by (1,0)."""
    out: dict[tuple[int, int], int] = {}
    for (p, q), mult in counts.items():
        for nxt in ((p + 1, q), (p - 1, q + 1), (p, q - 1)):
            if nxt[0] >= 0 and nxt[1] >= 0:
                out[nxt] = out.get(nxt, 0) + mult
    return out


def tensor_antifundamental_counts(counts: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    """SU(3) tensor rule for multiplying by (0,1)."""
    out: dict[tuple[int, int], int] = {}
    for (p, q), mult in counts.items():
        for nxt in ((p, q + 1), (p + 1, q - 1), (p - 1, q)):
            if nxt[0] >= 0 and nxt[1] >= 0:
                out[nxt] = out.get(nxt, 0) + mult
    return out


def occurrence_multiplicity_after_constructive_path(p: int, q: int) -> int:
    """Multiplicity of (p,q) after p fundamentals then q antifundamentals."""
    counts: dict[tuple[int, int], int] = {(0, 0): 1}
    for _ in range(p):
        counts = tensor_fundamental_counts(counts)
    for _ in range(q):
        counts = tensor_antifundamental_counts(counts)
    return counts.get((p, q), 0)


def strict_wilson_lower_term(p: int, q: int, beta: float) -> float:
    """Positive n=p+q exponential-series term in c_(p,q)(beta)."""
    n = p + q
    mult = occurrence_multiplicity_after_constructive_path(p, q)
    return (beta / 6.0) ** n * mult / math.factorial(n)


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
    print("Goal: source repair + sympy-symbolic verification of (T1)-(T4) under cited (I1)-(I4)")
    print("=" * 88)

    # -------------------------------------------------------------------
    section("Part 0a: supplied-input scope and source checks")
    # -------------------------------------------------------------------

    check(
        "the theorem note and constructive Wilson support files are present",
        NOTE_PATH.is_file() and WILSON_NOTE_PATH.is_file() and WILSON_RUNNER_PATH.is_file(),
        detail="all paths are durable repository files",
    )
    check(
        "the paired runner and cache paths are present",
        (ROOT / SELF_RUNNER).is_file() and (ROOT / SELF_CACHE).is_file(),
        detail="runner/cache discovery does not depend on note prose",
    )

    scope_weights = weights_box(1)
    scope_swap, scope_index = swap_matrix(scope_weights)
    scope_kappa = [
        sympy.Integer(0),
        sympy.Integer(2),
        sympy.Integer(2),
        sympy.Integer(3),
    ]
    scope_a = [
        sympy.Integer(1),
        sympy.Integer(2),
        sympy.Integer(2),
        sympy.Integer(3),
    ]
    scope_D = diag_matrix(scope_kappa)
    scope_Dloc = diag_matrix([value**4 for value in scope_a])
    scope_R = diag_matrix(
        [scope_kappa[i] / scope_a[i] ** 4 for i in range(len(scope_weights))]
    )
    check(
        "exact supplied diagonal quotient equals D_loc^{-1} D",
        scope_Dloc.inv() * scope_D == scope_R,
        detail="representative zero-trivial semidefinite packet checked exactly",
    )
    check(
        "the supplied quotient is positive semidefinite and swap-symmetric",
        all(scope_R[i, i] >= 0 for i in range(len(scope_weights)))
        and scope_swap * scope_R == scope_R * scope_swap,
        detail="nonnegativity and conjugation symmetry are exact",
    )
    check(
        "zero trivial kappa is admitted while actual-trivial normalization is unavailable",
        scope_kappa[scope_index[(0, 0)]] == 0,
        detail="the unnormalized quotient exists but division by z_(0,0) does not",
    )

    scope_v = zeros(len(scope_weights), 1)
    scope_v[scope_index[(0, 0)]] = 1
    scope_v[scope_index[(1, 1)]] = 1
    scope_hostile = sympy.eye(len(scope_weights)) + scope_v * scope_v.T
    leading_minors = [
        scope_hostile[:size, :size].det()
        for size in range(1, len(scope_weights) + 1)
    ]
    check(
        "hostile C is exactly positive definite, self-adjoint, swap-symmetric, and off-diagonal",
        all(minor > 0 for minor in leading_minors)
        and scope_hostile == scope_hostile.T
        and scope_swap * scope_hostile == scope_hostile * scope_swap
        and scope_hostile[scope_index[(0, 0)], scope_index[(1, 1)]] == 1,
        detail="Sylvester minors and the explicit mixing entry are exact",
    )
    check(
        "diagonal projection loses the hostile operator",
        diag_matrix(
            [scope_hostile[i, i] for i in range(len(scope_weights))]
        )
        != scope_hostile,
        detail="a kappa-only helper discards exact off-diagonal data",
    )
    scope_schur_map = diag_matrix(
        [sympy.Integer(dim_su3(p, q)) for p, q in scope_weights]
    )
    check(
        "finite-window Peter-Weyl coefficient map is injective",
        scope_schur_map.rank() == len(scope_weights)
        and scope_schur_map.det() != 0,
        detail="nonzero irrep dimensions give a full-rank diagonal map",
    )

    occurrence_box = 8
    constructive_ok = True
    min_mult = None
    for p in range(occurrence_box + 1):
        for q in range(occurrence_box + 1):
            mult = occurrence_multiplicity_after_constructive_path(p, q)
            min_mult = mult if min_mult is None else min(min_mult, mult)
            if mult < 1:
                constructive_ok = False
                break
        if not constructive_ok:
            break
    check(
        "constructive SU(3) tensor path reaches every sampled weight",
        constructive_ok,
        detail=f"checked 0<=p,q<={occurrence_box}; min multiplicity={min_mult}",
    )

    beta_samples = (0.25, 1.0, 6.0)
    strict_terms_positive = all(
        strict_wilson_lower_term(p, q, beta) > 0
        for beta in beta_samples
        for p in range(occurrence_box + 1)
        for q in range(occurrence_box + 1)
    )
    beta_zero_boundary = all(
        strict_wilson_lower_term(p, q, 0.0) == (1.0 if (p, q) == (0, 0) else 0.0)
        for p in range(4)
        for q in range(4)
    )
    check(
        "strict beta>0 Wilson lower term is positive on the source certificate grid",
        strict_terms_positive and beta_zero_boundary,
        detail="n=p+q term positive for beta>0; beta=0 boundary not overclaimed",
    )

    # -------------------------------------------------------------------
    section("Part 0b: symbolic setup")
    # -------------------------------------------------------------------

    # Representative finite truncation N_MAX = 3 for sympy-feasible symbolic algebra.
    N_MAX = 3
    weights = weights_box(N_MAX)
    S, index = swap_matrix(weights)
    n = len(weights)

    # Abstract nonnegative kappa and strictly positive a coefficient sequences.
    # Enforce conjugation symmetry: kappa_(p,q) = kappa_(q,p), a_(p,q) = a_(q,p).
    # Implementation: use one symbol per unordered pair {(p,q), (q,p)}.
    unique_pairs = []
    pair_to_sym_kappa = {}
    pair_to_sym_a = {}
    for (p, q) in weights:
        key = tuple(sorted((p, q)))
        if key not in pair_to_sym_kappa:
            unique_pairs.append(key)
            pair_to_sym_kappa[key] = Symbol(f"kappa_{key[0]}_{key[1]}", nonnegative=True, real=True)
            pair_to_sym_a[key] = Symbol(f"a_{key[0]}_{key[1]}", positive=True, real=True)

    # Normalization conventions for the actual-trivial-coefficient subsection:
    #   kappa_(0,0)(beta) > 0
    #   a_(0,0)(beta) = 1      (I2: trivial-channel normalization)
    pair_to_sym_kappa[(0, 0)] = Symbol("kappa_0_0", positive=True, real=True)
    pair_to_sym_a[(0, 0)] = sympy.Integer(1)

    kappa = [pair_to_sym_kappa[tuple(sorted(w))] for w in weights]
    a = [pair_to_sym_a[tuple(sorted(w))] for w in weights]

    # Build the diagonal central operators (matrices in character basis).
    D_beta = diag_matrix(kappa)
    D_beta_loc = diag_matrix([ai**4 for ai in a])

    # R_beta^env = D_beta_loc^{-1} * D_beta (by (D1)).
    # Equivalent eigenvalue sequence: r_(p,q)^env = kappa_(p,q) / a_(p,q)^4.
    rho_env = [kappa[i] / a[i]**4 for i in range(n)]
    R_env = diag_matrix(rho_env)

    print(f"  N_MAX = {N_MAX}  ({n} weights in finite truncation)")
    print(f"  Distinct abstract symbol pairs: kappa = {len(set(kappa))}, a (incl. fixed a_00=1) = {len(set(a))}")
    print(f"  r_(0,0)^env = kappa_(0,0) / a_(0,0)^4 = kappa_(0,0) (since a_(0,0)=1)")

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
        detail="all eigenvalues kappa/(a^4) are real symbols",
    )

    # Check positive semidefiniteness: every eigenvalue is nonnegative when
    # kappa>=0 and a>0.
    nonnegative_eigenvalues = all(
        R_env[i, i].is_nonnegative is True for i in range(n)
    )
    check(
        "(T1) R_beta^env eigenvalues are nonnegative (kappa >= 0, a > 0)",
        nonnegative_eigenvalues,
        detail="every eigenvalue is a nonnegative symbol divided by a positive fourth power",
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

    # Define z_(p,q)^env := (kappa_(p,q) / a_(p,q)^4) * lambda_env, with
    # lambda_env > 0. The actual trivial coefficient is
    # z_(0,0)^env = lambda_env * kappa_(0,0), so lambda_env is not a
    # trivial-channel normalization unless kappa_(0,0) = 1 is separately added.
    lambda_env = Symbol("lambda_env", positive=True, real=True)
    z_env = [rho_env[i] * lambda_env for i in range(n)]
    actual_z_00_env = z_env[index[(0, 0)]]

    # r_(p,q)^env := z_(p,q)^env / lambda_env, and the unnormalized convolution
    # operator divided by lambda_env has eigenvalue r_(p,q)^env on chi_(p,q).
    r_env_from_z = [simplify(z_env[i] / lambda_env) for i in range(n)]

    check(
        "(T2) Z_beta^env character coefficient (D2) matches r^env on every basis weight",
        all(simplify(r_env_from_z[i] - rho_env[i]) == 0 for i in range(n)),
        detail="z_(p,q)^env / lambda_env = kappa_(p,q) / a_(p,q)^4 at every weight",
    )

    check(
        "(T2) actual trivial coefficient is lambda_env * kappa_(0,0), not lambda_env",
        simplify(actual_z_00_env - lambda_env * kappa[index[(0, 0)]]) == 0,
        detail="no kappa_(0,0)=1 normalization premise is used",
    )

    # r conjugation symmetry on r_env_from_z.
    r_sym = True
    for (p, q) in weights:
        i = index[(p, q)]
        j = index[(q, p)]
        if simplify(r_env_from_z[i] - r_env_from_z[j]) != 0:
            r_sym = False
            break
    check(
        "(T2) r_(p,q)^env = r_(q,p)^env (conjugation symmetry)",
        r_sym,
        detail="follows from kappa_(p,q) = kappa_(q,p) and a_(p,q) = a_(q,p)",
    )

    # -------------------------------------------------------------------
    section("Part 3: (T3) all-weight structural identification")
    # -------------------------------------------------------------------

    # By the unnormalized character-basis convolution dictionary, C_Z is
    # diagonal on characters with eigenvalues z_(p,q)^env. So (1/lambda_env) C_Z
    # and R_env have the same eigenvalue sequence iff the symbolic identity
    # kappa_(p,q)/a_(p,q)^4 = z_(p,q)^env/lambda_env holds at every weight.
    T3_holds_pointwise = True
    for i in range(n):
        diff = simplify(rho_env[i] - r_env_from_z[i])
        if diff != 0:
            T3_holds_pointwise = False
            break
    check(
        "(T3) eigenvalue equality kappa_(p,q)/a_(p,q)^4 = z_(p,q)^env/lambda_env on every basis weight",
        T3_holds_pointwise,
        detail="symbolic reduction at exact sympy precision on N_MAX=3 truncation",
    )

    # Operator-level equality: matrices match on every entry.
    C_Z_over_lambda = diag_matrix(r_env_from_z)
    R_minus_C = R_env - C_Z_over_lambda
    T3_operator = all(simplify(R_minus_C[i, j]) == 0 for i in range(n) for j in range(n))
    check(
        "(T3) R_beta^env = (1/lambda_env) C_(Z_beta^env) at the operator level",
        T3_operator,
        detail="matrix difference reduces to zero on every entry symbolically",
    )

    C_Z_over_actual_z00 = diag_matrix([simplify(z_env[i] / actual_z_00_env) for i in range(n)])
    R_over_kappa00 = diag_matrix([simplify(rho_env[i] / kappa[index[(0, 0)]]) for i in range(n)])
    normalized_matches_rescaled = all(
        simplify((C_Z_over_actual_z00 - R_over_kappa00)[i, j]) == 0
        for i in range(n)
        for j in range(n)
    )
    check(
        "(T3) normalizing by actual z_(0,0)^env gives R_beta^env / kappa_(0,0)",
        normalized_matches_rescaled,
        detail="separates the out-of-scope kappa_(0,0)=1 hypothesis from the unnormalized theorem",
    )

    normalized_not_R_expr = simplify(
        C_Z_over_actual_z00[index[(0, 0)], index[(0, 0)]] - R_env[index[(0, 0)], index[(0, 0)]]
    )
    check(
        "(T3) without kappa_(0,0)=1, normalized convolution is not asserted equal to R_beta^env",
        normalized_not_R_expr != 0,
        detail=f"trivial-channel difference = {normalized_not_R_expr}",
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
    # The hypotheses allow a_(p,q)=1, so nontrivial weights need not differ.
    # Exhibit one admissible exact probe where the local strip changes the
    # eigenvalue: kappa_(1,0)=1 and a_(1,0)=2.
    probe_i = index[(1, 0)]
    counterfactual_probe = simplify(
        diff_from_correct[probe_i].subs(
            {kappa[probe_i]: sympy.Integer(1), a[probe_i]: sympy.Integer(2)}
        )
    )
    check(
        "counterfactual: an admissible a_(1,0)=2 probe shows that omitting D^loc can change the quotient",
        counterfactual_probe == Rational(15, 16),
        detail=f"kappa-kappa/a^4 = {counterfactual_probe} for kappa=1, a=2",
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
        pair_to_sym_kappa[(0, 0)]: Rational(7, 5),  # deliberately not normalized
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
    # operator built from z^env/lambda_env = kappa/a^4 at the sample.
    C_Z_over_lambda_concrete = C_Z_over_lambda.subs({**sample_kappa, **sample_a})
    R_env_concrete_minus_C_Z_concrete = R_env_concrete - C_Z_over_lambda_concrete
    convolution_match = all(
        R_env_concrete_minus_C_Z_concrete[i, j] == 0 for i in range(n) for j in range(n)
    )
    check(
        "(numerical sanity) R_beta^env = (1/lambda_env) C_Z at the abstract sample (exact)",
        convolution_match,
        detail="diagonal-operator match exact in rationals on every basis weight",
    )

    C_Z_over_actual_concrete = C_Z_over_actual_z00.subs({**sample_kappa, **sample_a})
    normalized_delta_concrete = simplify(
        C_Z_over_actual_concrete[index[(0, 0)], index[(0, 0)]]
        - R_env_concrete[index[(0, 0)], index[(0, 0)]]
    )
    check(
        "(numerical sanity) actual-trivial normalization differs from R_beta^env when kappa_(0,0) != 1",
        normalized_delta_concrete != 0,
        detail=f"sample trivial-channel difference = {normalized_delta_concrete}",
    )

    # -------------------------------------------------------------------
    section("Summary")
    # -------------------------------------------------------------------
    print("  Verified at exact sympy precision for supplied diagonal inputs:")
    print("    Local strict nonvanishing plus finite-window formal Z packaging")
    print("    (T1) Diagonality, self-adjointness, positivity, swap symmetry of supplied quotient R")
    print("    (T2) Peter-Weyl formal sequence expansion of Z with supplied coefficients")
    print("    (T3) eigenvalue equality kappa/a^4 = z^env/lambda_env at every weight (operator-level)")
    print("    (T3b) actual-trivial normalization gives R/kappa_(0,0), not R, unless kappa_(0,0)=1")
    print("    (T4) uniqueness: distinct eigenvalue sequences yield distinct operators")
    print("    Algebraic compatibility R = D_beta^loc^{-1} * D_beta")
    print("    Counterfactuals: D^loc strip + swap symmetry are both load-bearing")
    print("    Finite-truncation numerical sanity at one independent abstract sample")
    print("    No Wilson residual diagonality or physical environment identification is tested")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
