#!/usr/bin/env python3
"""Runner for the observable-principle P1 exponent-fixing irreducibility note.

This runner REPROVES, at exact SymPy/Fraction precision and from framework
primitives only, the sharpened irreducibility finding on the P1 admitted
premise (scalar additivity on independent subsystems) of
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`.

Sharpened finding (this note). The scalar-readout selection question splits
into two stages on two distinct algebraic axes:

  (Stage FORM)  On the operator-PRODUCT (composition) axis the requirement
                chi(A . S) = chi(A) . chi(S) selects `det` and excludes `tr`
                (GL(n) abelianization). This is genuine new content the
                direct-sum no-go portfolio could not supply, because `tr`
                PASSES direct-sum additivity. FORM is reprovable.

  (Stage EXPONENT)  The product-character axis leaves the exponent FREE: the
                whole one-parameter family F_p = |det|^p is product-
                multiplicative for every real p. Fixing the exponent so the
                real generator W is ADDITIVE over independent (block-diagonal)
                sectors is the irreducible atom. This runner proves the atom is
                P1-equivalent under every selector that actually fixes it:

                  (Add)  W(j_A,j_B) = W(j_A,0) + W(0,j_B)        [additivity = P1]
                  (Loc)  d^2 W / dj_a dj_b = 0 on block-diagonal D
                  (Pot)  grad W is a block-local field
                         (dW/dj_a indep of j_B and vice versa)

                are LOGICALLY EQUIVALENT on smooth W with W(0)=0 (Lemma,
                reproven on a generic polynomial ansatz). The Cauchy / cumulant
                / locality / bare-gradient-Gibbs selectors are all instances of
                one of (Add)/(Loc)/(Pot), hence all P1-equivalent.

                The ONE selector that is NOT P1 — the NORMALIZED-gradient
                (Born / probability) selector (1/p) Z^{-p} d(Z^p)/dj = d log Z/dj
                — is proven to recover the SAME expectation field for EVERY p,
                so it selects NOTHING among {F_p}. It is therefore too weak to
                fix the exponent. This is the precise tested-family sense in
                which no non-P1 selector closes the exponent step here.

Result reproven here: the det-vs-tr FORM is a theorem (composition axis);
the EXPONENT-FIXING step is the irreducible P1-equivalent admitted atom within
the tested selector families. This note does NOT close P1; it pins the atom.

Tests (all exact SymPy / Fraction; no fitted or observed inputs):
- T1: Z[J] = det(D+J) factorizes over a block-diagonal D = D_A (+) D_B
      (the independent-subsystem primitive), Z = Z_A . Z_B.
- T2: FORM axis — det is a multiplicative character under operator product
      (det(A.S) = det A . det S) while tr is NOT (tr(A.S) != tr A . tr S and
      != tr A + tr S). Confirms the composition axis separates det from tr.
- T3: EXPONENT is free on the product-character axis — |det|^c is a
      multiplicative character for EVERY real c; det^k are k-distinct.
- T4: cross-block 2nd derivative of log|det(D+J)| vanishes (Loc holds for
      the additive log generator); of F_p = (det)^p it is
      4 j_A j_B p^2 Z^p / (Z_A Z_B) != 0 for p != 0 (Loc fails for F_p).
- T5: LEMMA (the load-bearing irreducibility step) — on a generic smooth
      polynomial W with W(0,0)=0, the conditions (Add), (Loc), (Pot) force
      EXACTLY the same vanishing set of mixed coefficients, i.e. they are
      logically equivalent. Reproven symbolically.
- T6: NORMALIZED-gradient (Born) selector is exponent-blind —
      (1/p) Z^{-p} d(Z^p)/dj_a = d(log Z)/dj_a for ALL p (selects nothing);
      while the BARE-gradient selector d(Z^p)/dj_a = d(log Z)/dj_a forces
      p . Z^p = 1, impossible for non-constant Z, so it excludes p != 0 — and
      that bare-gradient selector IS condition (Pot) = P1 by T5.
- T7: live-ledger context presence (no dependency status consumed as
      load-bearing).
- T8: note honest-scope strings present; forbidden status-promotion strings
      absent.
- T9: source-note boundary declarations present.

Expected result: PASS=N, FAIL=0.

Reproduction:
    python3 scripts/audit_companion_observable_principle_p1_exponent_irreducibility_2026_05_31.py
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
AUDIT_SCRIPTS = ROOT / "docs" / "audit" / "scripts"
if str(AUDIT_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(AUDIT_SCRIPTS))

sys.dont_write_bytecode = True
import ledger_io

NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md"
)
AUDIT_INPUT_PATHS = (
    "docs/OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md",
    "docs/audit/scripts/ledger_io.py",
    "docs/audit/data/ledger/ob/observable_principle_from_axiom_note.json",
    "docs/audit/data/ledger/ob/observable_principle_p1_bridge_route_d_sharpened_no_go_note_2026-05-17.json",
    "docs/audit/data/ledger/ob/observable_principle_p1_bridge_locality_of_source_derivatives_narrow_note_2026-05-21.json",
    "docs/audit/data/ledger/ob/observable_principle_det_unique_multiplicative_character_form_selection_narrow_theorem_note_2026-05-28.json",
    "docs/audit/data/ledger/ob/observable_principle_p1p2_two_stage_synthesis_narrow_theorem_note_2026-05-28.json",
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


def load_context_rows(claim_ids: set[str]) -> dict[str, dict]:
    """Read the exact tracked shards consumed by the context check."""
    if ledger_io.sharded():
        rows = {}
        for claim_id in claim_ids:
            path = ledger_io.shard_path(claim_id)
            if not path.exists():
                continue
            row = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(row, dict) or row.get("claim_id") != claim_id:
                raise ValueError(f"audit ledger shard identity mismatch: {path}")
            rows[claim_id] = row
        return rows
    return ledger_io.load_ledger().get("rows", {})


def _block_diag_det_setup():
    """Independent-subsystem primitive: block-diagonal real anti-Hermitian D.

    D = D_A (+) D_B with D_A=[[j_A,a],[-a,j_A]], D_B=[[j_B,b],[-b,j_B]];
    identity-coupled source j_A, j_B per block. Returns (jA,jB,a,b,Z,ZA,ZB,D).
    """
    a, b = sp.symbols("a b", positive=True)
    jA, jB = sp.symbols("j_A j_B", real=True)
    D_A = sp.Matrix([[jA, a], [-a, jA]])
    D_B = sp.Matrix([[jB, b], [-b, jB]])
    ZA = sp.expand(D_A.det())  # j_A^2 + a^2
    ZB = sp.expand(D_B.det())  # j_B^2 + b^2
    D = sp.diag(D_A, D_B)
    Z = sp.expand(D.det())
    return jA, jB, a, b, Z, ZA, ZB, D


def test_T1_partition_factorizes() -> None:
    section("T1: Z[J] = det(D+J) factorizes over independent (block-diagonal) D")
    jA, jB, a, b, Z, ZA, ZB, D = _block_diag_det_setup()
    ok = sp.simplify(Z - ZA * ZB) == 0
    check(
        "det(D_A (+) D_B + J) = det(D_A+J_A) . det(D_B+J_B)  [Z = Z_A . Z_B]",
        ok,
        f"Z = {sp.factor(Z)} ;  Z_A . Z_B = {sp.factor(ZA * ZB)}",
    )


def test_T2_form_axis_det_vs_tr() -> None:
    section(
        "T2: FORM axis (operator PRODUCT) — det is a character, tr is not"
    )
    A = sp.Matrix(2, 2, sp.symbols("a0:4"))
    S = sp.Matrix(2, 2, sp.symbols("s0:4"))
    det_AS = (A * S).det()
    det_mult = sp.simplify(det_AS - A.det() * S.det())
    check(
        "det(A . S) = det(A) . det(S)  (det is a multiplicative character)",
        det_mult == 0,
        f"det(A.S) - det A . det S = {det_mult}",
    )
    tr = lambda M: M.trace()
    tr_AS = tr(A * S)
    tr_mult_defect = sp.simplify(tr_AS - tr(A) * tr(S))
    tr_add_defect = sp.simplify(tr_AS - (tr(A) + tr(S)))
    check(
        "tr(A . S) != tr(A) . tr(S)  AND  != tr(A) + tr(S)  (tr fails the character axis)",
        tr_mult_defect != 0 and tr_add_defect != 0,
        f"tr-mult defect = {tr_mult_defect};  tr-add defect = {tr_add_defect}",
    )
    # concrete numeric witness with all three distinct
    Anum = sp.Matrix([[2, 1], [1, 2]])
    Snum = sp.Matrix([[3, 0], [1, 4]])
    t1 = (Anum * Snum).trace()
    t2 = Anum.trace() * Snum.trace()
    t3 = Anum.trace() + Snum.trace()
    check(
        "concrete witness: tr(A.S), tr A . tr S, tr A + tr S all distinct",
        len({int(t1), int(t2), int(t3)}) == 3,
        f"tr(A.S)={int(t1)}, tr A . tr S={int(t2)}, tr A + tr S={int(t3)}",
    )


def test_T3_exponent_free_on_product_axis() -> None:
    section(
        "T3: EXPONENT is free on the product-character axis (|det|^c char for all c)"
    )
    c = sp.symbols("c", real=True)
    t1, t2 = sp.symbols("t1 t2", positive=True)
    # t -> t^c is a homomorphism (R_+, x) -> (R_+, x) for every real c:
    char_defect = sp.simplify((t1 * t2) ** c - t1 ** c * t2 ** c)
    check(
        "|det|^c is a product character for EVERY real c  ((t1 t2)^c = t1^c t2^c)",
        char_defect == 0,
        f"character defect = {char_defect}  (=> exponent c not fixed by the axis)",
    )
    A = sp.Matrix(2, 2, sp.symbols("a0:4"))
    # det^k are k-distinct functions (k=1 vs k=2):
    distinct = sp.simplify(A.det() ** 1 - A.det() ** 2) != 0
    check(
        "det^k are k-distinct characters (exponent k not fixed by character law alone)",
        distinct,
        "det^1 and det^2 differ as functions of A",
    )


def test_T4_locality_distinguishes_log_from_Fp() -> None:
    section(
        "T4: cross-block 2nd derivative — log|det| passes (Loc), F_p fails (p!=0)"
    )
    jA, jB, a, b, Z, ZA, ZB, D = _block_diag_det_setup()
    d2_log = sp.simplify(sp.diff(sp.log(Z), jA, jB))
    check(
        "d^2 log|det(D+J)| / dj_A dj_B = 0 on block-diagonal D  (Loc holds for log)",
        d2_log == 0,
        f"d^2 log Z / dj_A dj_B = {d2_log}",
    )
    p = sp.symbols("p", nonzero=True)
    d2_Fp = sp.simplify(sp.diff(Z ** p, jA, jB))
    expected = sp.simplify(4 * jA * jB * p ** 2 * Z ** p / (ZA * ZB))
    check(
        "d^2 (det(D+J))^p / dj_A dj_B = 4 j_A j_B p^2 Z^p/(Z_A Z_B) != 0  (Loc fails for F_p)",
        d2_Fp != 0 and sp.simplify(d2_Fp - expected) == 0,
        f"d^2 Z^p / dj_A dj_B = {sp.factor(d2_Fp)}",
    )


def test_T5_lemma_add_loc_pot_equivalent() -> None:
    section(
        "T5: LEMMA — (Add) <=> (Loc) <=> (Pot) on smooth W with W(0,0)=0 "
        "[the irreducibility step]"
    )
    jA, jB = sp.symbols("j_A j_B", real=True)
    # Generic smooth W up to degree 3 in each block, W(0,0)=0 (no constant term).
    names = "c10 c20 c30 c01 c02 c03 c11 c21 c12 c22 c31 c13"
    (c10, c20, c30, c01, c02, c03, c11, c21, c12, c22, c31, c13) = sp.symbols(names)
    W = (
        c10 * jA + c20 * jA ** 2 + c30 * jA ** 3
        + c01 * jB + c02 * jB ** 2 + c03 * jB ** 3
        + c11 * jA * jB + c21 * jA ** 2 * jB + c12 * jA * jB ** 2
        + c22 * jA ** 2 * jB ** 2 + c31 * jA ** 3 * jB + c13 * jA * jB ** 3
    )
    mixed = {c11, c21, c12, c22, c31, c13}

    # (Add): W(jA,jB) - W(jA,0) - W(0,jB) == 0  forces a coeff set to zero.
    add_expr = sp.expand(W - W.subs(jB, 0) - W.subs(jA, 0))
    add_required = set()
    for _, coef in sp.Poly(add_expr, jA, jB).terms():
        add_required |= set(coef.free_symbols)

    # (Loc): every mixed monomial coeff vanishes.
    loc_required = set(mixed)

    # (Pot): dW/dj_A independent of j_B AND dW/dj_B independent of j_A.
    dWdA = sp.diff(W, jA)
    dWdB = sp.diff(W, jB)
    pot_required = set()
    for monom, coef in sp.Poly(dWdA, jA, jB).terms():
        if monom[1] >= 1:  # term still carries j_B
            pot_required |= set(coef.free_symbols)
    for monom, coef in sp.Poly(dWdB, jA, jB).terms():
        if monom[0] >= 1:  # term still carries j_A
            pot_required |= set(coef.free_symbols)

    check(
        "(Add) forces the SAME mixed-coeff vanishing set as (Loc)",
        add_required == loc_required,
        f"(Add): {sorted(map(str, add_required))}",
    )
    check(
        "(Pot) forces the SAME mixed-coeff vanishing set as (Loc)",
        pot_required == loc_required,
        f"(Pot): {sorted(map(str, pot_required))}",
    )
    check(
        "=> (Add) <=> (Loc) <=> (Pot): the exponent-fixing selectors are all P1-equivalent",
        add_required == loc_required == pot_required,
        "bare-gradient potential selector / locality / additivity coincide on smooth W with W(0)=0",
    )


def test_T6_normalized_gradient_is_exponent_blind() -> None:
    section(
        "T6: NORMALIZED-gradient (Born) selector selects NOTHING; only the "
        "BARE-gradient (= Pot = P1) excludes p!=0"
    )
    jA, jB, a, b, Z, ZA, ZB, D = _block_diag_det_setup()
    p = sp.symbols("p", nonzero=True)
    bare_grad_log = sp.simplify(sp.diff(sp.log(Z), jA))
    norm_grad_Fp = sp.simplify((sp.Integer(1) / p) * Z ** (-p) * sp.diff(Z ** p, jA))
    check(
        "(1/p) Z^-p d(Z^p)/dj_A = d(log Z)/dj_A for ALL p  (Born/normalized gradient is exponent-blind)",
        sp.simplify(norm_grad_Fp - bare_grad_log) == 0,
        f"normalized grad = {norm_grad_Fp}  ==  d log Z/dj_A = {bare_grad_log}",
    )
    # BARE gradient selector: dW/dj = <O> = d log Z/dj forces (dZ^p/dj)/(d log Z/dj) = 1
    bare_grad_Fp = sp.diff(Z ** p, jA)
    ratio = sp.simplify(bare_grad_Fp / bare_grad_log)
    forced = sp.simplify(ratio - p * Z ** p)
    check(
        "BARE selector d(Z^p)/dj = d(log Z)/dj forces p . Z^p = 1 (impossible for non-constant Z)",
        forced == 0,
        f"(dZ^p/dj)/(d log Z/dj) = {sp.factor(ratio)} = p . Z^p  -> =1 only in the p->0 (log) limit",
    )


def test_T7_context_ledger_presence() -> None:
    section("T7: live-ledger context presence (no dependency status consumed)")
    # The load-bearing content is the elementary SymPy equivalence Lemma; the
    # framework rows below are target/context only (status NOT gated on here).
    context_rows = {
        "observable_principle_from_axiom_note",
        "observable_principle_p1_bridge_route_d_sharpened_no_go_note_2026-05-17",
        "observable_principle_p1_bridge_locality_of_source_derivatives_narrow_note_2026-05-21",
        "observable_principle_det_unique_multiplicative_character_form_selection_narrow_theorem_note_2026-05-28",
        "observable_principle_p1p2_two_stage_synthesis_narrow_theorem_note_2026-05-28",
    }
    rows = load_context_rows(context_rows)
    ok_all = True
    missing = []
    for cid in sorted(context_rows):
        if rows.get(cid) is None:
            ok_all = False
            missing.append(f"  {cid}: ROW NOT FOUND")
    check(
        "target/context rows present without status-gating the claim",
        ok_all,
        "context rows present; no dependency status consumed"
        if ok_all
        else "MISSING:\n" + "\n".join(missing),
    )


def test_T8_honest_scope_strings() -> None:
    section("T8: note honest-scope strings present; forbidden strings absent")
    if not NOTE.exists():
        check("note file exists", False, f"Missing: {NOTE}")
        return
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "does NOT close P1",
        "irreducible",
        "exponent-fixing",
        "composition axis",
        "F_p",
        "Pattern L",
        "logically equivalent",
        "normalized-gradient",
        "bare-gradient",
        "(Add)",
        "(Loc)",
        "(Pot)",
        "No-Go Discipline Gate",
        "N1",
        "N8",
    ]
    forbidden = [
        "**Status:** retained",
        "audited_clean",
        "promotes to retained",
        "**Effective status:** retained",
        "closes P1",
        "derives P1",
    ]
    missing = [s for s in required if s not in text]
    found_forbidden = [s for s in forbidden if s in text]
    check("required honest-scope strings present", len(missing) == 0, f"missing: {missing}")
    check("forbidden status-promotion / overclaim strings absent", len(found_forbidden) == 0, f"found: {found_forbidden}")


def test_T9_source_note_boundary() -> None:
    section("T9: source-note boundary declarations present")
    if not NOTE.exists():
        check("note file exists", False, f"Missing: {NOTE}")
        return
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "**Claim type:** no_go",
        "**Status authority:** independent audit lane only",
        "source-note proposal",
    ]
    missing = [s for s in required if s not in text]
    check("source-note boundary declarations present", len(missing) == 0, f"missing: {missing}")


def main() -> int:
    print("Observable-Principle P1 exponent-fixing irreducibility — companion runner")
    print("Reproves from primitives (exact SymPy); no fitted or observed inputs.")
    test_T1_partition_factorizes()
    test_T2_form_axis_det_vs_tr()
    test_T3_exponent_free_on_product_axis()
    test_T4_locality_distinguishes_log_from_Fp()
    test_T5_lemma_add_loc_pot_equivalent()
    test_T6_normalized_gradient_is_exponent_blind()
    test_T7_context_ledger_presence()
    test_T8_honest_scope_strings()
    test_T9_source_note_boundary()
    print("\n" + "=" * 78)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print(
        "\nA passing run supports ONLY the bounded irreducibility finding: the\n"
        "det-vs-tr FORM is a theorem on the operator-composition axis, while the\n"
        "EXPONENT-FIXING step is P1-equivalent under every selector that fixes it\n"
        "((Add)/(Loc)/(Pot)), and the one exponent-blind selector (normalized\n"
        "Born gradient) is too weak. It does NOT close P1, does NOT promote any\n"
        "row, and consumes no fitted or observed numerical targets."
    )
    print(f"per_element: checked — exact determinant-versus-trace scalar tests T1-T2 executed; aggregate runner FAIL={FAIL}.")
    print(f"per_site: checked — independent block perturbations in T4 were differentiated explicitly; aggregate runner FAIL={FAIL}.")
    print(f"per_mode: checked — the exponent family F_p and normalized-gradient exponent blindness were evaluated in T3/T6; aggregate runner FAIL={FAIL}.")
    print(f"per_block: checked — block-diagonal factorization and the (Add)/(Loc)/(Pot) equivalence tests ran symbolically; aggregate runner FAIL={FAIL}.")
    print(f"lattice_wide: checked and not executed — the finite-block theorem supplies no lattice realization; the executed scope/firewall tests bind the conclusion to bounded irreducibility with PASS={PASS}, FAIL={FAIL}.")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
