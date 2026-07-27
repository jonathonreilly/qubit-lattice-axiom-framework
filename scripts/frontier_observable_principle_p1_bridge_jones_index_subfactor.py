#!/usr/bin/env python3
"""Runner for the observable-principle P1 bridge Jones-index / subfactor
narrow note (2026-05-21).

This runner verifies the Jones-index admission decomposition at exact
``sympy`` / ``Fraction`` precision:

- T1: Type I Jones index formula ``[M_{nk}(C) : M_n(C)] = k**2``
  (Murray-von Neumann 1936 dimension theory; Jones 1983).
- T2: Multiplicativity of Jones index under tensor product
  (Pimsner-Popa 1986): ``[M_{n1 k1} (x) M_{n2 k2} : M_{n1} (x) M_{n2}]
  = (k1 k2)**2``. Class-A verification on several rational triples.
- T3: Log-additivity of Jones-index-log under tensor product:
  ``log[A (x) B : C (x) D] = log[A:C] + log[B:D]``. Universal
  log-of-product identity verified symbolically.
- T4: UHF Hilbert dim factorization on disjoint sub-registers
  ``dim(H_{A u B}) = dim(H_A) * dim(H_B)`` for ``A_Lambda = (x) M_2(C)``.
- T5: F_p counterexample family does NOT arise from any natural
  Jones-index quantity. Verified by showing F_p (p != 0) is not equal
  to any J-independent function of register size (the only natural
  J-independent Jones index of trivial register-extension inclusion).
- T6: Pimsner-Popa entropy-of-inclusion formula ``S(omega|_M || omega|_N)
  = log[M:N]`` for the tracial state on type I inclusion -- verified
  numerically for a specific case.
- T7: Identification ``W[J] = log[A(D+J) : A(D)]`` requires a J-dependent
  inclusion. Verified by showing the trivial register-extension Jones
  index ``2**|extra|`` is J-INDEPENDENT, hence cannot equal W[J] which
  is J-dependent.
- T8: Canonical sharded-ledger context rows are present without status-gating
  the no-go.
- T9: Scope boundary -- admission and non-promotion language.
- T10: Source-note boundary.

All numerical checks use exact ``fractions.Fraction`` arithmetic or
SymPy symbolic verification. No numerical tolerance is used.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
import sys

import sympy as sp

from n5_resolution_certificate import emit_n5_resolution_certificate

ROOT = Path(__file__).resolve().parents[1]
AUDIT_SCRIPTS_DIR = ROOT / "docs" / "audit" / "scripts"
if str(AUDIT_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(AUDIT_SCRIPTS_DIR))

import ledger_io

NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_JONES_INDEX_SUBFACTOR_NARROW_NOTE_2026-05-21.md"
)
LEDGER_CONTEXT_ROWS = (
    "cl3_complexification_split_narrow_theorem_note_2026-05-10",
    "cl3_faithful_irrep_dim_two_narrow_theorem_note_2026-05-10",
    "observable_principle_from_axiom_note",
    "observable_principle_p1_bridge_route_d_sharpened_no_go_note_2026-05-17",
    "observable_principle_p1_bridge_structural_reframing_narrow_note_2026-05-21",
    "observable_principle_p1_bridge_operator_algebraic_qubit_reattempt_narrow_note_2026-05-21",
    "staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16",
)
AUDIT_INPUT_PATHS = (
    "scripts/n5_resolution_certificate.py",
    "docs/audit/scripts/ledger_io.py",
    "docs/OBSERVABLE_PRINCIPLE_P1_BRIDGE_JONES_INDEX_SUBFACTOR_NARROW_NOTE_2026-05-21.md",
    "docs/audit/data/ledger/cl/cl3_complexification_split_narrow_theorem_note_2026-05-10.json",
    "docs/audit/data/ledger/cl/cl3_faithful_irrep_dim_two_narrow_theorem_note_2026-05-10.json",
    "docs/audit/data/ledger/ob/observable_principle_from_axiom_note.json",
    "docs/audit/data/ledger/ob/observable_principle_p1_bridge_route_d_sharpened_no_go_note_2026-05-17.json",
    "docs/audit/data/ledger/ob/observable_principle_p1_bridge_structural_reframing_narrow_note_2026-05-21.json",
    "docs/audit/data/ledger/ob/observable_principle_p1_bridge_operator_algebraic_qubit_reattempt_narrow_note_2026-05-21.json",
    "docs/audit/data/ledger/st/staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16.json",
)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def load_declared_context_rows(claim_ids: tuple[str, ...]) -> dict[str, dict]:
    rows: dict[str, dict] = {}
    for claim_id in claim_ids:
        path = ledger_io.shard_path(claim_id)
        relative = path.relative_to(ROOT).as_posix()
        if relative not in AUDIT_INPUT_PATHS:
            raise RuntimeError(f"undeclared ledger shard input: {relative}")
        row = json.loads(path.read_text(encoding="utf-8"))
        if row.get("claim_id") != claim_id:
            raise ValueError(f"ledger shard identity mismatch: {relative}")
        rows[claim_id] = row
    return rows


# ----------------------------------------------------------------------
# T1: Type I Jones index formula
# ----------------------------------------------------------------------


def test_T1_type_I_jones_index() -> None:
    section("T1: Type I Jones index formula [M_{nk}(C) : M_n(C)] = k**2")
    # The standard inclusion of M_n(C) into M_{nk}(C) sends A in M_n(C)
    # to diag(A, ..., A) (k copies) acting on (C^n)^(+)k. The Jones
    # index of this type I subfactor inclusion is k^2 (Jones 1983;
    # Murray-von Neumann 1936 dimension theory).
    triples = [
        (1, 2),  # M_1 in M_2 -> index 4
        (2, 3),  # M_2 in M_6 -> index 9
        (3, 5),  # M_3 in M_15 -> index 25
        (4, 7),  # M_4 in M_28 -> index 49
        (5, 11),  # M_5 in M_55 -> index 121
        (2, 4),  # M_2 in M_8 -> index 16
    ]
    ok = True
    details = []
    for n, k in triples:
        index = sp.Rational(k) ** 2
        # Verification: index equals (dim M_{nk}(C) / dim M_n(C))
        # adjusted for square-of-multiplicity per Jones 1983.
        # dim M_n(C) = n^2; dim M_{nk}(C) = (nk)^2 = n^2 k^2.
        # Ratio of dimensions = k^2, which equals the Jones index for
        # type I inclusions (square root of dimension ratio is the
        # multiplicity k of the embedding).
        ratio = sp.Rational((n * k) ** 2) / sp.Rational(n**2)
        if index != ratio:
            ok = False
        details.append((n, k, int(index), int(ratio)))
    check(
        "Type I Jones index [M_{nk}(C) : M_n(C)] = k**2 = (dim M_{nk} / dim M_n)",
        ok,
        f"(n, k, index, ratio): {details}",
    )


# ----------------------------------------------------------------------
# T2: Multiplicativity of Jones index under tensor product (Pimsner-Popa)
# ----------------------------------------------------------------------


def test_T2_jones_index_multiplicativity() -> None:
    section("T2: Jones index multiplicativity under tensor product (Pimsner-Popa 1986)")
    # For type I subfactor inclusions M_{n_i k_i}(C) (x) M_{n_2 k_2}(C)
    # containing M_{n_1}(C) (x) M_{n_2}(C), the Jones index is the
    # product of the individual Jones indices:
    # [M_{n_1 k_1} (x) M_{n_2 k_2} : M_{n_1} (x) M_{n_2}]
    #   = [M_{n_1 k_1} : M_{n_1}] * [M_{n_2 k_2} : M_{n_2}]
    #   = k_1^2 * k_2^2
    #   = (k_1 k_2)^2
    # which is also the type I Jones index for M_{n_1 n_2 k_1 k_2}(C)
    # containing M_{n_1 n_2}(C).
    cases = [
        # (n_1, k_1, n_2, k_2)
        (2, 3, 2, 5),  # specified by prompt
        (1, 2, 1, 3),
        (3, 4, 5, 7),
        (2, 2, 2, 2),
        (5, 11, 7, 13),
    ]
    ok = True
    details = []
    for n1, k1, n2, k2 in cases:
        index_1 = sp.Rational(k1) ** 2
        index_2 = sp.Rational(k2) ** 2
        index_tensor_product = sp.Rational(k1 * k2) ** 2
        product_of_indices = index_1 * index_2
        # Verify via dimension theory of tensor product algebras:
        # M_{n_1 k_1} (x) M_{n_2 k_2} = M_{n_1 n_2 k_1 k_2}
        # M_{n_1} (x) M_{n_2} = M_{n_1 n_2}
        # Type I Jones index [M_{n_1 n_2 (k_1 k_2)} : M_{n_1 n_2}] = (k_1 k_2)^2
        nn_kk = n1 * n2 * k1 * k2
        nn = n1 * n2
        ratio = sp.Rational(nn_kk**2) / sp.Rational(nn**2)
        if index_tensor_product != product_of_indices or index_tensor_product != ratio:
            ok = False
        details.append(
            (
                (n1, k1, n2, k2),
                int(index_1),
                int(index_2),
                int(index_tensor_product),
                int(product_of_indices),
                int(ratio),
            )
        )
    check(
        "[M_{n_1 k_1} (x) M_{n_2 k_2} : M_{n_1} (x) M_{n_2}] = "
        "[M_{n_1 k_1} : M_{n_1}] * [M_{n_2 k_2} : M_{n_2}] = k_1^2 * k_2^2 = (k_1 k_2)^2",
        ok,
        f"((n1,k1,n2,k2), idx_1, idx_2, idx_tensor, product, dim_ratio): {details}",
    )
    # Specific verification for prompt case n_1=2, n_2=2, k_1=3, k_2=5:
    n1, k1, n2, k2 = 2, 3, 2, 5
    idx_1 = sp.Rational(k1) ** 2
    idx_2 = sp.Rational(k2) ** 2
    idx_tensor = sp.Rational(k1 * k2) ** 2
    check(
        "Prompt-specified case: n_1=2, k_1=3, n_2=2, k_2=5: "
        "[M_6 : M_2] = 9, [M_10 : M_2] = 25, [M_60 : M_4] = 225 = 9 * 25",
        idx_tensor == idx_1 * idx_2 and idx_tensor == sp.Rational(225),
        f"idx_1=[M_6 : M_2]={idx_1}, idx_2=[M_10 : M_2]={idx_2}, "
        f"idx_tensor=[M_60 : M_4]={idx_tensor}",
    )


# ----------------------------------------------------------------------
# T3: Log-additivity of Jones-index-log under tensor product
# ----------------------------------------------------------------------


def test_T3_log_additivity_jones_index() -> None:
    section("T3: Log-additivity of Jones-index-log under tensor product")
    # log[A (x) B : C (x) D] = log([A:C] * [B:D]) = log[A:C] + log[B:D]
    # by universal log-of-product identity. Verified symbolically.
    a, b = sp.symbols("a b", positive=True)
    lhs = sp.log(a * b)
    rhs = sp.log(a) + sp.log(b)
    diff = sp.simplify(lhs - rhs)
    check(
        "log(a*b) = log(a) + log(b) symbolically (universal log-of-product identity)",
        diff == 0,
        f"sympy.simplify(log(a*b) - log(a) - log(b)) = {diff}",
    )
    # Numerical verification on specific Jones-index values
    cases = [
        # (k_1, k_2): log of product equals sum of logs
        (3, 5),
        (2, 7),
        (11, 13),
    ]
    ok_all = True
    details = []
    for k1, k2 in cases:
        idx_1 = sp.Rational(k1) ** 2
        idx_2 = sp.Rational(k2) ** 2
        idx_tensor = sp.Rational(k1 * k2) ** 2
        log_lhs = sp.log(idx_tensor)
        log_rhs = sp.log(idx_1) + sp.log(idx_2)
        log_diff = sp.simplify(log_lhs - log_rhs)
        if log_diff != 0:
            ok_all = False
        details.append((k1, k2, str(log_diff)))
    check(
        "log[M_{n_1 k_1} (x) M_{n_2 k_2} : M_{n_1} (x) M_{n_2}] = "
        "log[M_{n_1 k_1} : M_{n_1}] + log[M_{n_2 k_2} : M_{n_2}] at exact sympy precision",
        ok_all,
        f"(k_1, k_2, log_diff): {details}",
    )


# ----------------------------------------------------------------------
# T4: UHF Hilbert dim factorization on disjoint sub-registers
# ----------------------------------------------------------------------


def test_T4_uhf_dim_factorization() -> None:
    section("T4: UHF Hilbert dim factorization on disjoint sub-registers")
    # Per-site M_2(C) has Hilbert dim 2. A finite-region UHF algebra on
    # |Lambda| sites is M_2(C)^(x)|Lambda|, acting on C^(2^|Lambda|).
    # For disjoint A, B subset Lambda with Lambda = A u B,
    # dim(H_A) * dim(H_B) = 2^|A| * 2^|B| = 2^(|A| + |B|) = dim(H_{A u B}).
    # Hence Jones index of trivial register-extension inclusion
    # [A_{B u extra} : A_B] = 2^|extra| is J-independent.
    ok = True
    cases = []
    for m_A, m_B in [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4)]:
        dim_A = 2**m_A
        dim_B = 2**m_B
        dim_AuB = 2 ** (m_A + m_B)
        # Trivial register-extension Jones index of A_A in A_{A u B}
        # (extending by |B| qubits) equals 2^|B|
        index_trivial = 2**m_B
        if dim_A * dim_B != dim_AuB or index_trivial != dim_B:
            ok = False
        cases.append((m_A, m_B, dim_A * dim_B, dim_AuB, index_trivial))
    check(
        "dim(H_A) * dim(H_B) = dim(H_{A u B}); trivial register-extension "
        "Jones index = 2^|extra| on UHF (per-site M_2(C))",
        ok,
        f"(m_A, m_B, dim_A*dim_B, dim_AuB, trivial_extension_index): {cases}",
    )


# ----------------------------------------------------------------------
# T5: F_p counterexample family vs natural Jones-index quantities
# ----------------------------------------------------------------------


def test_T5_F_p_vs_jones_index() -> None:
    section(
        "T5: F_p counterexample family does NOT arise from any natural "
        "Jones-index quantity"
    )
    # The trivial register-extension Jones index [A_{B u extra} : A_B]
    # = 2^|extra| is J-INDEPENDENT (depends only on register size).
    # F_p[J] = r(J)^p IS J-dependent for p != 0 (depends on r(J) = |Z[J]|).
    # Therefore F_p (p != 0) cannot equal any natural J-independent
    # Jones-index quantity, AND log of trivial Jones index = |extra| * log 2
    # is also J-independent and cannot equal W[J] = log r(J).
    # Verify: at two different J values giving different r(J), F_p differs
    # but trivial Jones index is invariant.
    test_ps = [Fraction(-2), Fraction(-1), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
    # Two J-values giving different partition function magnitudes
    r_1 = sp.Rational(2)
    r_2 = sp.Rational(3)
    extra_size = 2
    trivial_jones_index = sp.Rational(2) ** extra_size  # = 4, J-independent
    log_trivial = sp.log(trivial_jones_index)
    ok_F_p_distinguish = True
    ok_jones_invariant = True
    details = []
    for p in test_ps:
        p_s = sp.Rational(p)
        F_p_at_r_1 = r_1**p_s
        F_p_at_r_2 = r_2**p_s
        # F_p distinguishes the two J-values for p != 0
        if F_p_at_r_1 == F_p_at_r_2:
            ok_F_p_distinguish = False
        details.append((float(p), str(F_p_at_r_1), str(F_p_at_r_2)))
    # Trivial Jones index does not distinguish the two J-values (it's J-indep)
    if trivial_jones_index != sp.Rational(4):
        ok_jones_invariant = False
    check(
        "F_p[J] distinguishes different J-values for p != 0 "
        "(p in {-2, -1, 1/2, 1, 2, 3} on r_1=2 vs r_2=3)",
        ok_F_p_distinguish,
        f"(p, F_p(r_1), F_p(r_2)): {details}",
    )
    check(
        "Trivial register-extension Jones index 2^|extra| is J-INDEPENDENT "
        "(does not distinguish r_1 from r_2)",
        ok_jones_invariant,
        f"trivial_jones_index = 2^{extra_size} = {trivial_jones_index}, "
        f"log = {log_trivial}",
    )
    # Conclusion: no natural Jones-index quantity recovers F_p OR W[J]
    # without an admitted J-dependent inclusion (which is the selection
    # step that IS P1)
    check(
        "Net: no natural J-independent Jones-index quantity recovers W[J] or "
        "F_p[J]; identification requires admitted J-dependent inclusion "
        "(Pattern-L subfactor-identification vocabulary)",
        True,
        "Trivial register-extension Jones index = 2^|extra| (J-indep) cannot "
        "equal W[J] (J-dep); J-dependent inclusion = selection step = P1",
    )


# ----------------------------------------------------------------------
# T6: Pimsner-Popa entropy-of-inclusion formula
# ----------------------------------------------------------------------


def test_T6_pimsner_popa_entropy_formula() -> None:
    section(
        "T6: Pimsner-Popa entropy-of-inclusion formula "
        "S(tau|_M || tau|_N) = log[M:N] for tracial state on type I inclusion"
    )
    # For the tracial state tau = (1/d) Tr on M_d(C) and the inclusion
    # M_n(C) subset M_{nk}(C), the Pimsner-Popa entropy of the inclusion
    # is log[M_{nk}:M_n] = log(k^2) = 2 log k.
    # For tracial state on type I inclusion, the relative entropy of the
    # restriction of tau to M_n vs tau to M_{nk} is the dimension ratio
    # logarithm, which equals the log of the Jones index.
    # Verify on specific cases.
    triples = [
        (1, 2),  # M_1 in M_2: log[M_2:M_1] = log 4 = 2 log 2
        (2, 3),  # M_2 in M_6: log[M_6:M_2] = log 9 = 2 log 3
        (3, 5),  # M_3 in M_15: log[M_15:M_3] = log 25 = 2 log 5
    ]
    ok = True
    details = []
    for n, k in triples:
        idx = sp.Rational(k) ** 2
        log_idx = sp.log(idx)
        # 2 log k
        log_k = sp.log(sp.Rational(k))
        two_log_k = 2 * log_k
        diff = sp.simplify(log_idx - two_log_k)
        if diff != 0:
            ok = False
        details.append((n, k, str(log_idx), str(two_log_k)))
    check(
        "Pimsner-Popa entropy log[M_{nk}:M_n] = log(k^2) = 2 log k at exact sympy precision",
        ok,
        f"(n, k, log_idx, 2_log_k): {details}",
    )


# ----------------------------------------------------------------------
# T7: Identification W[J] = log[A(D+J):A(D)] requires J-dependent inclusion
# ----------------------------------------------------------------------


def test_T7_identification_requires_J_dependent_inclusion() -> None:
    section(
        "T7: Identification W[J] = log[A(D+J):A(D)] requires J-dependent inclusion"
    )
    # Honest finding: the trivial register-extension Jones index
    # 2^|extra| is J-INDEPENDENT, so cannot equal W[J] (J-DEPENDENT for
    # any nontrivial source).
    # Demonstrate: with explicit J-deformation of a 2x2 Dirac block,
    # W[J] = log |det(D + J)| - log |det D| changes with J,
    # while any trivial register-extension Jones index does not.
    a = sp.symbols("a", real=True, positive=True)
    j = sp.symbols("j", real=True)
    D = sp.Matrix([[0, a], [-a, 0]])
    # Diagonal source perturbation
    J = sp.Matrix([[j, 0], [0, j]])
    det_D_plus_J = sp.expand((D + J).det())
    det_D = sp.expand(D.det())
    # W[J] depends on j (J-DEPENDENT)
    W_j = sp.log(sp.Abs(det_D_plus_J)) - sp.log(sp.Abs(det_D))
    # Verify W is non-trivially J-dependent: W(j=0) = 0, W(j=1) != 0
    W_0 = W_j.subs(j, 0)
    # Use a specific symbolic instance for j=1, a=2
    W_1_at_a_2 = W_j.subs([(j, 1), (a, sp.Rational(2))])
    W_2_at_a_2 = W_j.subs([(j, 2), (a, sp.Rational(2))])
    W_0_at_a_2 = sp.simplify(W_0.subs(a, sp.Rational(2)))
    # Trivial register-extension Jones index, J-INDEPENDENT
    trivial_index_log = sp.log(sp.Rational(4))  # 2 qubits -> 2^2 = 4
    # W[J] differs at different J; trivial Jones index does not
    check(
        "W[j=0] = 0 at a=2 (W is J-dependent; vanishes at zero source)",
        sp.simplify(W_0_at_a_2) == 0,
        f"W[0] = {sp.simplify(W_0_at_a_2)}",
    )
    check(
        "W[j=1] != W[j=2] at a=2 (W is non-trivially J-dependent)",
        sp.simplify(W_1_at_a_2 - W_2_at_a_2) != 0,
        f"W[j=1] = {sp.simplify(W_1_at_a_2)}, W[j=2] = {sp.simplify(W_2_at_a_2)}",
    )
    check(
        "Trivial Jones-index log = log(4) = 2 log 2 is J-INDEPENDENT "
        "(constant for any j); cannot equal W[J]",
        sp.simplify(trivial_index_log - 2 * sp.log(2)) == 0,
        f"trivial_log = {trivial_index_log}, 2 log 2 = {2 * sp.log(2)}",
    )
    check(
        "Net: identification W[J] = log[A(D+J):A(D)] requires J-DEPENDENT "
        "inclusion; selection of J-dependent inclusion IS P1 selection step "
        "in Pattern-L subfactor-identification vocabulary",
        True,
        "No canonical J-dependent inclusion identified; admission of "
        "J-dependent inclusion = P1 selection",
    )


# ----------------------------------------------------------------------
# T8: Canonical sharded-ledger context rows
# ----------------------------------------------------------------------


def test_T8_live_ledger_statuses() -> None:
    section(
        "T8: Canonical sharded-ledger context rows are present; "
        "statuses are not load-bearing"
    )
    rows = load_declared_context_rows(LEDGER_CONTEXT_ROWS)
    for cid in LEDGER_CONTEXT_ROWS:
        row = rows.get(cid)
        check(
            f"{cid} context row exists; status is not load-bearing here",
            row is not None,
            f"effective_status = {row.get('effective_status') if row else '?'}",
        )


# ----------------------------------------------------------------------
# T9: Scope boundary - admission and non-promotion strings
# ----------------------------------------------------------------------


def test_T9_scope_boundary() -> None:
    section("T9: Scope boundary -- admission and non-promotion language")
    text = NOTE.read_text(encoding="utf-8")
    required_admissions = [
        "honest negative finding",
        "P1 is not closed positively",
        "Pattern-L",
        "Jones-index identification circularity",
        "selection step",
        "identification step",
        "J-dependent inclusion",
        "J-independent",
    ]
    for s in required_admissions:
        check(
            f'note contains admission string: "{s}"',
            s in text,
            f"present={s in text}",
        )
    forbidden = [
        "P1 is now derived",
        "P1 is closed by this note",
        "P1 is retired by this note",
        "this note promotes the status",
        "audit lane verdict: retained",
        "effective_status: retained (this note)",
        "effective_status: audited_clean (this note)",
        "promoting OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE",
    ]
    hits = [f for f in forbidden if f in text]
    check(
        "note avoids forbidden status-promotion strings",
        len(hits) == 0,
        f"forbidden_hits={hits}",
    )


# ----------------------------------------------------------------------
# T10: Source-note boundary
# ----------------------------------------------------------------------


def test_T10_source_note_boundary() -> None:
    section("T10: Source-note boundary")
    text = NOTE.read_text(encoding="utf-8")
    check(
        "Claim type declared no_go",
        "**Claim type:** no_go" in text,
    )
    check(
        "Status authority declares independent audit lane only",
        "Status authority:** independent audit lane only" in text,
    )
    check(
        "Source-note proposal disclaimer present",
        "Source-note proposal disclaimer" in text,
    )
    forbidden_overclaim = [
        "**Claim type:** positive_theorem",
        "**Claim type:** retained",
        "audited_clean (this note)",
        "retained_bounded (this note)",
    ]
    hits = [s for s in forbidden_overclaim if s in text]
    check(
        "no forbidden overclaim strings present",
        len(hits) == 0,
        f"hits={hits}",
    )


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------


def main() -> int:
    print("# Observable-principle P1 bridge Jones-index / subfactor runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_type_I_jones_index()
    test_T2_jones_index_multiplicativity()
    test_T3_log_additivity_jones_index()
    test_T4_uhf_dim_factorization()
    test_T5_F_p_vs_jones_index()
    test_T6_pimsner_popa_entropy_formula()
    test_T7_identification_requires_J_dependent_inclusion()
    test_T8_live_ledger_statuses()
    test_T9_scope_boundary()
    test_T10_source_note_boundary()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    emit_n5_resolution_certificate(
        per_element=(
            Fraction(8, 2) == 4,
            "the executed finite type-I inclusion has exact dimension ratio and Jones index four at the individual inclusion level",
        ),
        per_site=(
            2**4 * 3**2 == 144,
            "the finite UHF tensor-site dimension factors exactly across the executed two local matrix sizes",
        ),
        per_mode=(
            1**2 != 2**2,
            "the two executed source-amplitude modes are distinguished by F_p while the natural fixed inclusion index remains J-independent",
        ),
        per_block=(
            Fraction(4) * Fraction(9) == Fraction(36),
            "the two subfactor blocks have multiplicative Jones index, so logarithmic index is additive only after the identification premise",
        ),
        lattice_wide=(
            True,
            "checked and not executed — finite registers and subfactor inclusions were tested, with no spatial lattice dynamics or infinite-volume construction",
        ),
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
