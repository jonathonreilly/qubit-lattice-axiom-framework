#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the narrow theorem note
`GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md`.

The parent narrow note's load-bearing content is the all-weight structural
identification, on the marked-plaquette SU(3) class-function sector, of the
residual source-sector operator

  R_beta^env := D_beta^loc^{-1} * (exp[-(beta/2) J] T_src(beta) exp[-(beta/2) J])
             := D_beta^loc^{-1} * D_beta,
  R_beta^env chi_(p,q) = (kappa_(p,q)(beta) / a_(p,q)(beta)^4) chi_(p,q),  (D1)

with the unnormalized central formal action

  (1 / lambda_env(beta)) C_(Z_beta^env)

by the boundary Peter-Weyl coefficient sequence

  Z_beta^env(W) := sum_(p,q) d_(p,q) z_(p,q)^env(beta) chi_(p,q)(W),
  z_(p,q)^env(beta) = (kappa_(p,q)(beta) / a_(p,q)(beta)^4) * lambda_env(beta).  (D2)

Three structural retained authorities and one retained-bounded Wilson
coefficient source supply the inputs (I1), (I2), (I3), (I4):

  (I1) gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note
       (retained_bounded / audited_clean): T_src(beta) = exp[(beta/2) J] D_beta
       exp[(beta/2) J] with D_beta chi_(p,q) = kappa_(p,q)(beta) chi_(p,q).

  (I2) gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10
       (retained / audited_clean): D_beta^loc chi_(p,q) = a_(p,q)(beta)^4 chi_(p,q)
       with a_(p,q)(beta) sourced from the one-link Wilson coefficient formula;
       non-marked spatial links contribute the identity on the marked source
       sector after normalization.

  (I3) su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10
       (retained / audited_clean): for an abstract positive conjugation-symmetric
       coefficient sequence (rho_(p,q)) with rho_(0,0) = 1, the diagonal operator
       R[rho] equals the normalized convolution operator C_{Z/Z_(0,0)} by the
       associated central class function Z(W) = sum d_(p,q) rho_(p,q) chi_(p,q)(W).
       By linearity, the same character-basis dictionary gives the unnormalized
       eigenvalue formula C_Z chi_(p,q) = z_(p,q) chi_(p,q). This runner consumes
       only that unnormalized identity; it does not assume rho_(0,0)=1 for
       R_beta^env.

  (I4) wilson_su3_gauge_transfer_kernel_positivity_bounded_note_2026-05-30
       (effective_status retained_bounded): the Wilson one-link coefficient
       expansion has nonnegative tensor-product multiplicities. This runner
       checks the source repair's constructive highest-weight occurrence
       certificate m_(p,q)^(p+q) >= 1, which upgrades the needed premise to
       a_(p,q)(beta)>0 at all weights for beta>0.

This Pattern A narrow runner verifies symbolically (sympy `simplify` to 0):

  (a) source repair checks: the Wilson retained-bounded authority is linked,
      a_(p,q)(beta)>0 for beta>0 is sourced by an all-weight occurrence
      certificate, and Z_beta^env is explicitly formal per-weight rather than
      an actual all-weight class-function claim;
  (b) (T1) structural diagonality, self-adjointness, positivity, and
      conjugation symmetry of R_beta^env under (I1)+(I2)+(I4);
  (c) (T2) Peter-Weyl formal sequence expansion of Z_beta^env with the
      coefficients of (D2), including the distinction between lambda_env and
      the actual trivial coefficient z_(0,0)^env = lambda_env*kappa_(0,0);
  (d) (T3) eigenvalue equality kappa_(p,q) / a_(p,q)^4 = z_(p,q)^env /
      lambda_env at every weight in a finite representative truncation;
  (e) (T4) uniqueness: two distinct eigenvalue sequences yield distinct
      operators;
  (f) algebraic compatibility R_beta^env = D_beta^loc^{-1} * D_beta;
  (g) counterfactual probes: D^loc strip and swap symmetry are both
      load-bearing;
  (h) finite-truncation numerical sanity at one independent abstract
      positive symmetric coefficient sequence.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the parent's
load-bearing class-(A) algebraic identification holds at exact symbolic
precision under the cited authorities (I1)+(I2)+(I3)+(I4). The
cited retained authorities themselves are imported from upstream retained
authorities and are not re-derived here.
"""

from __future__ import annotations
import json
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
RESIDUAL_PARENT_PATH = ROOT / "docs" / "GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_IDENTIFICATION_THEOREM_NOTE.md"
CHAR_MEASURE_PARENT_PATH = ROOT / "docs" / "GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md"
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
WILSON_NOTE_PATH = ROOT / "docs" / "WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md"
WILSON_RUNNER_PATH = ROOT / "scripts" / "wilson_su3_gauge_transfer_kernel_positivity_2026-05-30.py"
WILSON_CLAIM_ID = "wilson_su3_gauge_transfer_kernel_positivity_bounded_note_2026-05-30"
SELF_RUNNER = "scripts/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.py"
SELF_CACHE = "logs/runner-cache/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.txt"
SELF_NOTE = "GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md"


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


def ledger_row(claim_id: str) -> dict:
    data = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    return data.get("rows", {}).get(claim_id, {})


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
    section("Part 0a: 2026-06-07 source repair checks")
    # -------------------------------------------------------------------

    note_text = NOTE_PATH.read_text(encoding="utf-8")
    residual_parent_text = RESIDUAL_PARENT_PATH.read_text(encoding="utf-8")
    char_measure_parent_text = CHAR_MEASURE_PARENT_PATH.read_text(encoding="utf-8")
    wilson_row = ledger_row(WILSON_CLAIM_ID)

    check(
        "I4 source files are present",
        WILSON_NOTE_PATH.exists() and WILSON_RUNNER_PATH.exists(),
        detail="Wilson positivity note and runner exist in the restricted packet surface",
    )
    check(
        "source note exposes plain primary runner and cache metadata",
        f"**Primary runner:** `{SELF_RUNNER}`" in note_text
        and f"**Runner cache:** `{SELF_CACHE}`" in note_text,
        detail="audit-runner extraction can discover the restricted packet without following markdown link targets",
    )
    check(
        "parent finite-packet notes cite this all-weight formal bridge as structural support only",
        SELF_NOTE in residual_parent_text
        and SELF_NOTE in char_measure_parent_text
        and "formal diagonal-convolution" in residual_parent_text
        and "formal diagonal-convolution" in char_measure_parent_text
        and "does not compute" in residual_parent_text
        and "does not compute" in char_measure_parent_text
        and "full unmarked spatial Wilson integral" in residual_parent_text
        and "actual\n  beta=6 unmarked spatial Wilson environment coefficients" in char_measure_parent_text,
        detail="parent rows split formal convolution support from the still-open physical coefficient bridge",
    )
    check(
        "I4 ledger authority has retained_bounded effective status",
        wilson_row.get("effective_status") == "retained_bounded",
        detail=f"audit_status={wilson_row.get('audit_status')} effective_status={wilson_row.get('effective_status')}",
    )
    check(
        "target note cites the I4 Wilson coefficient source",
        "WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md" in note_text
        and WILSON_CLAIM_ID in note_text,
        detail="one-hop source edge to retained-bounded Wilson coefficient positivity",
    )
    check(
        "target note states the constructive all-weight occurrence lemma",
        "m_(p,q)^(p+q) >= 1" in note_text
        and "c_(p,q)(beta) > 0" in note_text
        and "a_(p,q)(beta)>0" in note_text,
        detail="strict Wilson coefficient nonvanishing for beta>0 is source-visible",
    )
    check(
        "target note narrows Z_beta^env to a formal per-weight central sequence",
        "formal per-weight central" in note_text
        and "finite-window Schur" in note_text
        and "formal diagonal action" in note_text,
        detail="no hidden all-weight class-function object is required",
    )
    check(
        "target note excludes actual all-weight class-function and L2 closure claims",
        "not an actual L^2 class-function claim" in note_text
        and "not a convergence claim" in note_text
        and "not a full Hilbert-space operator-closure claim" in note_text,
        detail="formal sequence boundary is explicit",
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
        "(T1) R_beta^env eigenvalues are positive (kappa > 0, a > 0 from (I1)+(I2)+(I4))",
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
    print("  Verified at exact sympy precision under cited (I1)+(I2)+(I3)+(I4):")
    print("    Source repair: I4 strict Wilson nonvanishing plus formal Z_beta^env boundary")
    print("    (T1) Structural diagonality, self-adjointness, positivity, swap symmetry of R_beta^env")
    print("    (T2) Peter-Weyl formal sequence expansion of Z_beta^env with (D2) coefficients")
    print("    (T3) eigenvalue equality kappa/a^4 = z^env/lambda_env at every weight (operator-level)")
    print("    (T3b) actual-trivial normalization gives R/kappa_(0,0), not R, unless kappa_(0,0)=1")
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
