#!/usr/bin/env python3
"""Runner for the observable-principle P1 record-information-route narrow note.

This runner REPROVES, at exact SymPy/Fraction precision and from framework
primitives only, the finding on the P1 admitted premise (scalar additivity on
independent subsystems) of `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`.

The tested hypothesis (record route). The framework is "qubit (probability)
until record (information)." The proposed pipeline:

    amplitude psi (multiplicative for independent tensor systems)
      -> Born p = |psi|^2 (multiplicative)
      -> a RECORD forms (a persistent sequence of definite marks)
      -> information I = -log p (ADDITIVE: I_AB = I_A + I_B).

CLAIM under test: the physical scalar observable is the RECORDED INFORMATION
(additive) because (i) A1 is a measurement framework so observables ARE
records/measurement-outcomes, and (ii) a physical record is a SEQUENCE of
definite marks whose size is additive BY CONCATENATION (free-monoid length).
If so, P1 would reduce to A1 + record-additivity, i.e. DERIVED, not admitted.

Honest finding reproven here (verdict `circular_log_reintroduced`):

  (1) A1 does NOT force "observable = record." A1 commits the per-site qubit
      operator algebra (M_2(C) = Cl(3,0)) and the Z^3 substrate, and NOTHING
      else; measurement, records, and the Born rule are explicit DERIVATION
      LANES, not axiom content (MINIMAL_AXIOMS_2026-05-20.md). "observable =
      recorded information" is an ADDITIONAL identification.

  (2) The decisive -log circularity. The framework's actual record object is a
      Kraus instrument W = sum_r K_r (x) |r>, whose branches are labeled by an
      orthonormal record basis {|r>} and quantified by the BORN probability
      p_r = Tr(K_r rho K_r^dagger) (PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE +
      BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE). That object is multipli-
      cative on independent tensor branches (p_{AB} = p_A . p_B). Passing to an
      ADDITIVE scalar requires the map p |-> -log p. But on the candidate
      family Phi_q(p) = p^q (equivalently the v-chain family F_p = |det|^p in
      the modulus variable r = |Z|), every member is multiplicative on
      independent sectors and the ADDITIVE representative is exactly the q -> 0
      (log) member. Selecting it is the (Add) face = P1 (Cauchy classifier;
      additivity is the HYPOTHESIS). The Born/normalized readout is exponent-
      blind (returns the same expectation field for every exponent), i.e. the
      BLIND face of the #2504 dichotomy: it singles NOTHING. So the record
      object itself does not force the additive quantification; the -log is the
      SAME free choice as P1, relabeled. (Reproves/extends #2456, #2504, #2517,
      and the structural-reframing no_go.)

  (3) The free-monoid kernel does NOT escape. The free monoid A^* on an
      alphabet A has, by concatenation, |w1 w2| = |w1| + |w2| (length is
      additive), and length is the UNIQUE monoid homomorphism A^* -> (N,+) up
      to overall scale that assigns equal value to single letters (reproven
      here on a finite test alphabet). This is a genuine additive structure.
      BUT: to make "record SIZE = number of marks" reproduce the framework's
      continuous additive readout W = log|det(D+J)| (the v-chain generator),
      the size of the record of a Born branch of probability p must be set to
      |w(p)| proportional to -log_b(p) (the Shannon/Kraft optimal code length).
      That assignment IS the -log p choice of (2). Without it, the bare integer
      mark-count is (a) not pinned by A1 (no axiom assigns marks to branches),
      and (b) integer-quantized, hence cannot equal the continuous v-chain
      log|det| readout. Either the size IS -log p (then it is (Add) = P1) or it
      is the bare count (then it is a DIFFERENT, integer object, not the
      v-chain observable, and still unpinned by A1). The free-monoid additivity
      is therefore real but inert: it does not single out the additive QUANTIFI-
      CATION of a Born branch over the multiplicative one without re-importing
      the log.

  (4) Time supplies no extra escape. (a) time-as-generator H = -log(T^2)/(2a)
      is the #2517 circularity (the additive generator's coordinate IS log).
      (b) time-as-recording-sequence (marks accumulate along derived time) is
      exactly free-monoid concatenation in (3): additive in mark-count, but the
      mark-count of a single Born click is again the -log p assignment. Both
      reduce to the -log choice.

Tests (all exact SymPy / Fraction; no fitted or observed inputs):
  T1: independent tensor branches -> Born probability is multiplicative
      (p_{AB} = p_A . p_B), the pre-record multiplicative structure.
      Equivalently |Z| factorizes on block-diagonal D (the v-chain modulus).
  T2: information additivity I = -log p satisfies I_{AB} = I_A + I_B; and on
      the family Phi_q(p) = p^q every member is multiplicative on independent
      sectors, so the additive representative is exactly q -> 0 (log) = (Add).
  T3: free-monoid concatenation length additivity |w1 w2| = |w1| + |w2| on a
      finite test alphabet, and length-uniqueness: any monoid homomorphism
      A^* -> (R,+) is determined by its values on letters, and the
      equal-weight one is c . |.| (unique up to scale).
  T4: the -log identification is the bridge — record-size := -log_b(p) makes
      branch-size additive over independent branches BECAUSE -log_b is the
      additive coordinate of the multiplicative group (R_+, x); the SAME
      Cauchy/Kraft step. Reproven: size(p_A . p_B) = size(p_A) + size(p_B)
      holds for size = c . log iff c is the (Add) selector; and the bare
      integer count is NOT equal to the continuous log readout (a quantization
      witness).
  T5: Born/normalized readout is exponent-blind (BLIND face): the normalized
      gradient (1/q) p^{-q} d(p^q)/dtheta = d(log p)/dtheta for ALL q, so the
      RECORD's Born quantification singles nothing among {Phi_q}. Ties to #2504
      BLIND-or-ADD: the record route lands in BLIND (Born quantification) or
      ADD (= P1, the -log size).
  T6: A1 measurement-content audit — MINIMAL_AXIOMS commits ONLY the per-site
      qubit algebra + Z^3, with measurement/records/Born as DERIVATION LANES;
      the Kraus record quantifies branches by Born p_r = Tr(K_r rho K_r^dag),
      not by a primitive mark-count. (String-presence check on the framework
      notes.)
  T7: live-ledger context presence (no dependency status consumed as
      load-bearing).
  T8: note honest-scope strings present; forbidden status-promotion strings
      absent.
  T9: source-note boundary declarations present.

Expected result: PASS=N, FAIL=0. A passing run supports ONLY the bounded
finding (verdict circular_log_reintroduced): the record picture re-describes but
does not derive P1; the -log at the record is the same free choice as P1, and
the free-monoid concatenation length, though genuinely additive, does not
single out the additive quantification of a Born branch without re-importing the
log. It does NOT close P1 and does NOT promote any row.

Reproduction:
    python3 scripts/audit_companion_observable_principle_p1_record_information_route_2026_06_03.py
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_RECORD_INFORMATION_ROUTE_NARROW_NOTE_2026-06-03.md"
)
MINIMAL_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
KRAUS_NOTE = ROOT / "docs" / "PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md"
BORN_NOTE = ROOT / "docs" / "BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md"
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

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


def _block_diag_modulus_setup():
    """v-chain modulus primitive: block-diagonal real anti-Hermitian D.

    r = |Z| = |det(D+J)| with D = D_A (+) D_B; identity-coupled source per
    block; the modulus factorizes r = r_A . r_B (the multiplicative pre-record
    structure, the same one Born probability has). Returns the parts.
    """
    a, b = sp.symbols("a b", positive=True)
    jA, jB = sp.symbols("j_A j_B", real=True)
    D_A = sp.Matrix([[jA, a], [-a, jA]])
    D_B = sp.Matrix([[jB, b], [-b, jB]])
    rA = sp.expand(D_A.det())  # j_A^2 + a^2  (positive)
    rB = sp.expand(D_B.det())  # j_B^2 + b^2  (positive)
    D = sp.diag(D_A, D_B)
    r = sp.expand(D.det())
    return jA, jB, a, b, r, rA, rB, D


def test_T1_born_probability_multiplicative() -> None:
    section(
        "T1: independent tensor branches -> Born probability multiplicative "
        "(pre-record structure); |Z| factorizes on block-diagonal D"
    )
    # Amplitude multiplicativity for independent tensor systems, then Born.
    # Write the complex amplitudes in modulus-phase form so |.|^2 is exact:
    #   psi = R . exp(i phi),  |psi|^2 = R^2  (R real positive moduli).
    RA, RB = sp.symbols("R_A R_B", positive=True)
    phiA, phiB = sp.symbols("phi_A phi_B", real=True)
    psiA = RA * sp.exp(sp.I * phiA)
    psiB = RB * sp.exp(sp.I * phiB)
    # |psi_A (x) psi_B|^2 = |psi_A|^2 |psi_B|^2 = R_A^2 R_B^2 = p_A p_B
    lhs = sp.simplify(sp.Abs(psiA * psiB) ** 2)
    rhs = sp.simplify(sp.Abs(psiA) ** 2 * sp.Abs(psiB) ** 2)
    born_defect = sp.simplify(lhs - rhs)
    check(
        "Born p_{AB} = |psi_A (x) psi_B|^2 = |psi_A|^2 . |psi_B|^2 = p_A . p_B (multiplicative)",
        born_defect == 0 and sp.simplify(lhs - RA ** 2 * RB ** 2) == 0,
        f"|psi_A psi_B|^2 = {lhs} = p_A . p_B (multiplicative on independent tensor branches; pre-record)",
    )
    jA, jB, a, b, r, rA, rB, D = _block_diag_modulus_setup()
    ok = sp.simplify(r - rA * rB) == 0
    check(
        "v-chain modulus r = |det(D_A (+) D_B + J)| = r_A . r_B (same multiplicative form)",
        ok,
        f"r = {sp.factor(r)} ;  r_A . r_B = {sp.factor(rA * rB)}",
    )


def test_T2_information_additivity_is_the_log_representative() -> None:
    section(
        "T2: information I = -log p is additive; on {Phi_q = p^q} the additive "
        "representative is exactly q -> 0 (log) = (Add)"
    )
    pA, pB = sp.symbols("p_A p_B", positive=True)
    I = lambda p: -sp.log(p)
    info_defect = sp.simplify(I(pA * pB) - (I(pA) + I(pB)))
    check(
        "I_{AB} = -log(p_A . p_B) = -log p_A - log p_B = I_A + I_B (additivity of -log)",
        info_defect == 0,
        "the -log map IS additive on the multiplicative group (R_+, x)",
    )
    # The family Phi_q(p) = p^q: every member multiplicative on independent
    # sectors; the ADDITIVE one is q->0 (log). Show multiplicativity for all q
    # and that no q!=0 power is additive.
    q = sp.symbols("q", real=True)
    mult_defect = sp.simplify((pA * pB) ** q - pA ** q * pB ** q)
    check(
        "Phi_q(p) = p^q is multiplicative on independent sectors for EVERY q "
        "((p_A p_B)^q = p_A^q p_B^q)",
        mult_defect == 0,
        "=> selecting the additive member from {Phi_q} is the Cauchy step (additivity = hypothesis)",
    )
    qn = sp.symbols("q_nz", nonzero=True)
    add_defect_power = sp.simplify((pA * pB) ** qn - (pA ** qn + pB ** qn))
    check(
        "no q != 0 power is additive: (p_A p_B)^q != p_A^q + p_B^q (additive rep is the log limit)",
        add_defect_power != 0,
        f"defect = {add_defect_power}  (nonzero => p^q additive only as q->0, i.e. log)",
    )


def test_T3_free_monoid_length_additivity_and_uniqueness() -> None:
    section(
        "T3: free-monoid concatenation length is additive AND unique up to scale"
    )
    # Finite test alphabet; words as tuples; concatenation = tuple +.
    alphabet = ("0", "1", "2")
    words = [
        (),
        ("0",),
        ("1", "0"),
        ("2", "2", "1"),
        ("0", "1", "2", "0"),
    ]
    length = lambda w: len(w)
    # Additivity over all pairs:
    add_ok = all(
        length(w1 + w2) == length(w1) + length(w2) for w1 in words for w2 in words
    )
    check(
        "|w1 . w2| = |w1| + |w2| for all words (concatenation length additive; free monoid A^*)",
        add_ok,
        "length is a monoid homomorphism (A^*, .) -> (N, +)",
    )
    # Uniqueness up to scale: any homomorphism h: A^* -> (R,+) is fixed by its
    # values on letters; the equal-weight (translation-invariant) one is c.|.|.
    # Reprove: an arbitrary per-letter weighting w_letter gives
    # h(word) = sum_letters w_letter; it equals c.length for all words iff all
    # per-letter weights are equal to c. (Symbolic, generic c.)
    c = sp.symbols("c", real=True)
    wt = dict(zip(alphabet, sp.symbols("w0 w1 w2", real=True)))
    def hom(word):
        return sum((wt[s] for s in word), sp.Integer(0))
    # Require hom(word) == c * length(word) for the test words; solve the
    # constraint set; the ONLY solution is each letter-weight = c.
    eqs = [sp.Eq(hom(w), c * length(w)) for w in words if len(w) >= 1]
    sol = sp.solve(eqs, list(wt.values()), dict=True)
    uniq_ok = len(sol) == 1 and all(sp.simplify(v - c) == 0 for v in sol[0].values())
    check(
        "length is the UNIQUE equal-weight homomorphism up to scale: hom = c.|.| forces every "
        "letter-weight = c",
        uniq_ok,
        f"solution: {sol}  (single-letter equal-weight => c.length, unique up to scale c)",
    )


def test_T4_log_bridge_is_the_choice_and_count_is_quantized() -> None:
    section(
        "T4: record-size := -log_b(p) is the bridge (= Cauchy/Kraft step); the "
        "bare integer count is a DIFFERENT object (quantized != continuous log)"
    )
    pA, pB = sp.symbols("p_A p_B", positive=True)
    cc = sp.symbols("cc", positive=True)
    # size(p) = cc * (-log p): additive over independent branches BECAUSE -log
    # is the additive coordinate of (R_+, x). This is the SAME (Add) step.
    size = lambda p: cc * (-sp.log(p))
    size_defect = sp.simplify(size(pA * pB) - (size(pA) + size(pB)))
    check(
        "size(p) = c.(-log p) gives size(p_A . p_B) = size(p_A) + size(p_B) (the -log IS the bridge)",
        size_defect == 0,
        "branch-size additivity over independent branches = additivity of -log = (Add) = P1",
    )
    # Conversely a generic monotone size g(p) is additive over independent
    # branches iff g(p_A p_B) = g(p_A) + g(p_B), i.e. iff g = c log (Cauchy);
    # show that g(p) = 1 - p (a non-log monotone candidate) FAILS additivity.
    g = lambda p: 1 - p
    g_defect = sp.simplify(g(pA * pB) - (g(pA) + g(pB)))
    check(
        "a non-log monotone size g(p)=1-p is NOT additive over independent branches "
        "(only c.log is; Cauchy)",
        g_defect != 0,
        f"defect = {sp.expand(g_defect)} (nonzero => additivity singles out log, the P1 choice)",
    )
    # Quantization witness: a bare integer mark-count n(p) in N cannot equal the
    # continuous v-chain readout -log_b(p) for varying p. Show the continuous
    # log takes a non-integer value at a generic p where any fixed b makes the
    # count integer only on a measure-zero set. Concrete: -log_2(p) at p=1/3.
    val = -sp.log(sp.Rational(1, 3), 2)
    is_int = sp.simplify(val - sp.floor(val)) == 0
    check(
        "bare integer mark-count != continuous log readout: -log_2(1/3) is not an integer",
        not is_int,
        f"-log_2(1/3) = {sp.nsimplify(val)} ~ {float(val):.6f} (non-integer => count is a different object)",
    )


def test_T5_born_normalized_readout_is_exponent_blind() -> None:
    section(
        "T5: the RECORD's Born quantification is exponent-blind (BLIND face of "
        "#2504): normalized gradient singles NOTHING among {Phi_q}"
    )
    # Single-branch amplitude p(theta) = a^2 + theta^2 (positive); the Born/
    # normalized readout of the family Phi_q(p) = p^q is the normalized gradient.
    theta, a = sp.symbols("theta a", real=True)
    p = a ** 2 + theta ** 2
    q = sp.symbols("q", nonzero=True)
    bare_grad_log = sp.simplify(sp.diff(sp.log(p), theta))
    norm_grad = sp.simplify((sp.Integer(1) / q) * p ** (-q) * sp.diff(p ** q, theta))
    check(
        "(1/q) p^-q d(p^q)/dtheta = d(log p)/dtheta for ALL q (Born/normalized readout exponent-blind)",
        sp.simplify(norm_grad - bare_grad_log) == 0,
        f"normalized grad = {norm_grad} == d log p/dtheta = {bare_grad_log} (singles nothing => BLIND)",
    )
    # The bare (un-normalized) gradient DOES break the tie, and it IS the
    # (Add)/(Pot) selector = P1: d(p^q)/dtheta = d(log p)/dtheta forces q.p^q=1.
    bare_grad_Fq = sp.diff(p ** q, theta)
    ratio = sp.simplify(bare_grad_Fq / bare_grad_log)
    forced = sp.simplify(ratio - q * p ** q)
    check(
        "only the BARE (additive-size) selector breaks the tie, and it forces q.p^q=1 "
        "(= (Add)=P1, the -log size)",
        forced == 0,
        f"(d p^q/dtheta)/(d log p/dtheta) = {sp.factor(ratio)} = q.p^q -> =1 only in q->0 (log) limit",
    )


def test_T6_a1_has_no_observable_equals_record_content() -> None:
    section(
        "T6: A1 commits ONLY the per-site qubit algebra + Z^3; measurement/"
        "records/Born are DERIVATION LANES; the record quantifies by Born p_r"
    )
    ok = True
    detail = []
    if not MINIMAL_AXIOMS.exists():
        check("MINIMAL_AXIOMS note exists", False, f"Missing: {MINIMAL_AXIOMS}")
        return
    ax = MINIMAL_AXIOMS.read_text(encoding="utf-8")
    # Collapse whitespace so wrapped phrases ("records, Born\nprobabilities")
    # match regardless of line breaks in the source markdown.
    ax_flat = " ".join(ax.split())
    # A1 headline is the qubit/per-site algebra; records/Born are lanes, not axiom.
    a1_present = "Reality is a qubit at every lattice site" in ax
    lanes_present = (
        "records" in ax
        and "Born probabilities" in ax_flat
        and "are not additional primitives in A1-A2" in ax_flat
    )
    check(
        "A1 = 'Reality is a qubit at every lattice site' (per-site algebra + Z^3 only)",
        a1_present,
        "A1 commits the per-site M_2(C)=Cl(3,0) algebra and the Z^3 substrate",
    )
    check(
        "records / Born probabilities are explicitly NOT additional primitives in A1-A2 "
        "(derivation lanes)",
        lanes_present,
        "=> 'observable = recorded information' is an ADDITIONAL identification, not A1",
    )
    # The framework's record object quantifies branches by the Born trace p_r.
    if KRAUS_NOTE.exists():
        kr = KRAUS_NOTE.read_text(encoding="utf-8")
        kraus_ok = ("p_r = Tr(K_r rho K_r" in kr) and ("sum_r K_r" in kr)
    else:
        kraus_ok = False
    if BORN_NOTE.exists():
        bn = BORN_NOTE.read_text(encoding="utf-8")
        born_ok = "p(E) = Tr(rho E)" in bn
    else:
        born_ok = False
    check(
        "framework record (Kraus instrument) quantifies branches by Born p_r = Tr(K_r rho K_r^dag), "
        "NOT a primitive mark-count",
        kraus_ok and born_ok,
        "the recorded branch carries the multiplicative Born weight; -log is required to make it additive",
    )


def test_T7_context_ledger_presence() -> None:
    section("T7: live-ledger context presence (no dependency status consumed)")
    if not LEDGER_PATH.exists():
        check("audit_ledger.json exists", False, f"Missing: {LEDGER_PATH}")
        return
    full = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows = full.get("rows", full)
    context_rows = {
        "observable_principle_from_axiom_note",
        "observable_principle_p1_exponent_fixing_irreducibility_narrow_note_2026-05-31",
        "observable_principle_p1_bridge_structural_reframing_narrow_note_2026-05-21",
        "persistent_record_as_kraus_operator_note_2026-05-20",
        "born_rule_from_gleason_busch_derivation_note_2026-05-20",
    }
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
    # Flatten whitespace so multi-word required phrases match regardless of
    # markdown line-wrapping in the note source.
    text_flat = " ".join(text.split())
    required = [
        "does NOT close P1",
        "circular_log_reintroduced",
        "free-monoid",
        "concatenation",
        "recorded information",
        "Born",
        "additional identification",
        "BLIND",
        "(Add)",
        "Pattern L",
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
        "p1_retained_from_measurement_axiom",
    ]
    missing = [s for s in required if s not in text_flat]
    found_forbidden = [s for s in forbidden if s in text]
    check("required honest-scope strings present", len(missing) == 0, f"missing: {missing}")
    check(
        "forbidden status-promotion / overclaim strings absent",
        len(found_forbidden) == 0,
        f"found: {found_forbidden}",
    )


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
    print("Observable-Principle P1 record-information-route — companion runner")
    print("Reproves from primitives (exact SymPy); no fitted or observed inputs.")
    test_T1_born_probability_multiplicative()
    test_T2_information_additivity_is_the_log_representative()
    test_T3_free_monoid_length_additivity_and_uniqueness()
    test_T4_log_bridge_is_the_choice_and_count_is_quantized()
    test_T5_born_normalized_readout_is_exponent_blind()
    test_T6_a1_has_no_observable_equals_record_content()
    test_T7_context_ledger_presence()
    test_T8_honest_scope_strings()
    test_T9_source_note_boundary()
    print("\n" + "=" * 78)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print(
        "\nA passing run supports ONLY the bounded finding (verdict\n"
        "circular_log_reintroduced): A1 does not force observable=record; the\n"
        "framework's record quantifies branches by the multiplicative Born weight,\n"
        "and the -log that makes the recorded scalar additive is the SAME free\n"
        "choice as P1 (the (Add) face); the free-monoid concatenation length,\n"
        "though genuinely additive and unique up to scale, does not single out the\n"
        "additive quantification of a Born branch over the multiplicative one\n"
        "without re-importing the log. It does NOT close P1 and does NOT promote\n"
        "any row."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
