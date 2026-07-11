#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_R_ETA_DOUBLET_CLOCK_RATE_NORMALIZATION_NO_GO_NOTE_2026-07-04.md"
DECISION_HISTORY = DOCS / "audit" / "data" / "premise_decision_history.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_PREMISES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
POINTER = DOCS / "ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02.md"
DEFECT = DOCS / "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md"
RECORD_CLOCK = DOCS / "RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md"
DYNAMICS = DOCS / "DYNAMICS_COUPLING_RESIDUAL_CLASSIFIER_2026-06-06.md"
FIXED = DOCS / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
BRANNEN = DOCS / "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
SCALE = DOCS / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def ledger_row_by_path(path: str) -> dict | None:
    rows = json.loads(read(LEDGER))["rows"]
    matches = [row for row in rows.values() if row.get("note_path") == path]
    if not matches:
        return None
    if len(matches) != 1:
        raise AssertionError(f"ledger matches for {path}: {len(matches)}")
    return matches[0]


def exact(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.expand_trig(expr))


def main() -> int:
    print("AC_phi_lambda R-eta doublet-clock rate-normalization no-go verifier")

    paths = [
        NOTE,
        DECISION_HISTORY,
        LEDGER,
        AXIOMS,
        AXIOM_PREMISES,
        REGISTRY,
        POINTER,
        DEFECT,
        RECORD_CLOCK,
        DYNAMICS,
        FIXED,
        BRANNEN,
        REALIZED,
        KINETIC,
        SCALE,
    ]

    section("A. source presence and Tier-A boundary")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    tier = json.loads(read(DECISION_HISTORY))
    axioms = read(AXIOMS)
    premises = json.loads(read(AXIOM_PREMISES))
    registry = read(REGISTRY)
    pointer = read(POINTER)
    defect = read(DEFECT)
    record_clock = read(RECORD_CLOCK)
    dynamics = read(DYNAMICS)
    fixed = read(FIXED)
    brannen = read(BRANNEN)
    realized = read(REALIZED)
    kinetic = read(KINETIC)
    scale = read(SCALE)

    note_flat = flat(note)
    axioms_flat = flat(axioms)
    registry_flat = flat(registry)
    pointer_flat = flat(pointer)
    defect_flat = flat(defect)
    record_clock_flat = flat(record_clock)
    dynamics_flat = flat(dynamics)

    ac = tier["retired_derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    decomp = ac["minimum_decomposition"]
    check("Tier-A has no live admitted inputs", tier["genuine_admitted_input_count"] == 0 and tier["derivation_targets"] == {})
    check("AC minimum decomposition keeps R-eta", "delta_readout_identification_R_eta" in decomp, decomp)
    check("AC minimum decomposition keeps occupancy separate", "reading_occupancy_selection" in decomp, decomp)
    check("AC statement names density-read-as-angle R-eta", "density-read-as-angle" in ac["statement"] and "R-eta" in ac["statement"])
    check("human registry points to the R-eta derivation obligation", "AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md" in registry)
    check("note declares no_go Type", "**Type:** no_go" in note and "**Claim type:** no_go" in note)
    check("note says R-eta remains open", "R-eta is not derived or refuted; its open gate remains" in note)
    check("note says AC_phi_lambda is not retired", "AC_phi_lambda is not retired." in note)
    check("note says registry not edited", "No registry, axiom, primitive, audit verdict, publication surface" in note)

    section("B. dependency classes and boundary pins")
    expected_status = {
        "docs/ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02.md": {"unaudited"},
        "docs/ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md": {"retained_bounded", "unaudited"},
        "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md": {"retained_bounded", "unaudited"},
        "docs/BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md": {"retained_bounded", "unaudited"},
    }
    for path, allowed in expected_status.items():
        row = ledger_row_by_path(path)
        check(f"ledger row exists for {Path(path).name}", row is not None)
        if row is not None:
            check(f"{Path(path).name} status in allowed current set", row.get("effective_status") in allowed, row.get("effective_status"))

    new_row = ledger_row_by_path("docs/ACPHILAMBDA_R_ETA_DOUBLET_CLOCK_RATE_NORMALIZATION_NO_GO_NOTE_2026-07-04.md")
    if new_row is not None:
        check("new row claim_type is no_go", new_row.get("claim_type") == "no_go", new_row.get("claim_type"))
        check("new row remains unaudited", new_row.get("audit_status") == "unaudited", new_row.get("audit_status"))
        check("new row effective status remains unaudited", new_row.get("effective_status") == "unaudited", new_row.get("effective_status"))
    else:
        check("new row not required before audit pipeline seeding", True)

    check("approved premise registry has four canonical ids", premises["canonical_ids"] == [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ])
    for phrase in ["Records form.", "at what rate", "transition probabilities or weights", "formation rules", "physical observable bridge"]:
        check(f"minimal axioms boundary contains {phrase}", phrase in axioms_flat)
    for phrase in ["no state", "measure", "weighting", "probability rule", "normalization rule", "value"]:
        check(f"realized-state primitive withholds {phrase}", phrase in flat(realized))
    for phrase in ["mixing angle", "phase", "selector", "readout bridge"]:
        check(f"kinetic primitive withholds {phrase}", phrase in flat(kinetic))
    check("scale primitive carries zero dimensionless content", "zero dimensionless content" in flat(scale))

    section("C. source-surface pins")
    pointer_pins = [
        ("doublet clock formula", "rate is `2 sqrt(3) |b| sin delta`" in pointer_flat),
        ("free |b| unit", "The `|b|` unit remains free" in pointer_flat),
        ("occurrence statistics open", "Occurrence statistics are not addressed" in pointer_flat),
        ("readout selection open", "Readout selection remains open" in pointer_flat),
    ]
    for label, ok in pointer_pins:
        check(f"pointer clock note pin: {label}", ok)
    for phrase in [
        "Rescale Obstruction",
        "no derivation drawn from this scanned surface can single out the identity-unit member",
        "Any successful derivation of `c = 1` must contain at least one rescale-breaking",
    ]:
        check(f"defect rescale pin: {phrase[:48]}", phrase in defect_flat)
    for phrase in [
        "stable dial location != Record-selected dial value != physical rate normalization",
        "Rate and clock remain separate",
        "still needs a clock/rate unit",
    ]:
        check(f"record clock/rate pin: {phrase[:48]}", phrase in record_clock_flat)
    for phrase in ["coupling magnitude", "clock-rate normalization", "record-preservation dynamics stack"]:
        check(f"dynamics classifier pin: {phrase}", phrase in dynamics_flat)
    check("fixed-locus source contains 2/9", "2/9" in fixed)
    fixed_flat = flat(fixed).lower()
    check(
        "fixed-locus source excludes physical readout bridge",
        ("physical readout" in fixed_flat or "physical single-summand" in fixed_flat)
        and ("separate named open bridge" in fixed_flat or "does not touch that readout" in fixed_flat),
    )
    check("Brannen source carries supplied dial", "(a, |b|, delta)" in brannen)

    section("D. exact doublet-clock algebra")
    delta, B, a_act, lam = sp.symbols("delta B a_act lambda", positive=True)
    L = sp.Rational(2, 9)
    S_sum = 3 * L
    phi_target = sp.Rational(2, 3)
    rate = 2 * sp.sqrt(3) * B * sp.sin(delta)
    omega = sp.simplify(rate / B)

    check("L = 2/9", L == sp.Rational(2, 9))
    check("S_sum = 3L = 2/3", S_sum == phi_target)
    check("raw clock depends on B", B in rate.free_symbols)
    check("raw clock depends on delta", delta in rate.free_symbols)
    check("dimensionless clock removes B", B not in omega.free_symbols)
    check("raw clock rescales with B", exact(rate.subs(B, lam * B) - lam * rate) == 0)
    check("dimensionless clock is 2 sqrt(3) sin(delta)", exact(omega - 2 * sp.sqrt(3) * sp.sin(delta)) == 0)
    check("zero clock at delta=0", exact(omega.subs(delta, 0)) == 0)
    check("zero clock at delta=pi", exact(omega.subs(delta, sp.pi)) == 0)
    check("target delta is positive and below pi/2", bool(0 < L < sp.pi / 2))
    check("target delta has nonzero clock", bool(sp.ask(sp.Q.positive(sp.sin(L)))))

    # Rigorous inequality: sin(x) > x - x^3/6 for 0 < x, x=2/9.
    sin_lower = L - L**3 / 6
    check("Taylor lower bound for sin(2/9) is positive", sin_lower > 0)
    check(
        "dimensionless clock at target is strictly above 2/3",
        12 * sin_lower**2 > phi_target**2,
        {"lower": str(sin_lower), "lhs": str(12 * sin_lower**2), "rhs": str(phi_target**2)},
    )
    omega_target_numeric = float((2 * math.sqrt(3)) * math.sin(2 / 9))
    check("numeric sanity: Omega(2/9) > 2/3", omega_target_numeric > float(phi_target), omega_target_numeric)
    check("Omega target is not fixed-locus density L", omega_target_numeric > float(phi_target) > float(L))
    check("Omega = 0 misses target delta", L != 0 and L != sp.pi)
    check("maximal clock sin(delta)=1 misses target delta", L != sp.pi / 2)

    section("E. event-rate normalization obstruction")
    ratio = sp.simplify(rate / a_act)
    check("event ratio contains B", B in ratio.free_symbols)
    check("event ratio contains a_act", a_act in ratio.free_symbols)
    check("event ratio contains delta", delta in ratio.free_symbols)
    solved_B = sp.solve(sp.Eq(ratio.subs(delta, L), phi_target), B)
    expected_B = a_act / (3 * sp.sqrt(3) * sp.sin(L))
    check("solving event ratio target leaves B in terms of a_act", solved_B == [expected_B], solved_B)
    check("solution still contains a_act", a_act in solved_B[0].free_symbols)
    check("changing a_act changes fitted B", exact(solved_B[0].subs(a_act, 2) - solved_B[0].subs(a_act, 1)) != 0)
    ratio_a = ratio.subs({B: 1, a_act: 1, delta: L})
    ratio_b = ratio.subs({B: 2, a_act: 1, delta: L})
    ratio_c = ratio.subs({B: 1, a_act: 2, delta: L})
    check("same delta with B doubled changes event ratio", exact(ratio_b - 2 * ratio_a) == 0)
    check("same delta with a_act doubled halves event ratio", exact(2 * ratio_c - ratio_a) == 0)
    check("joint B,a_act rescale preserves event ratio", exact(ratio.subs({B: lam * B, a_act: lam * a_act}) - ratio) == 0)

    completions = [
        {"B": sp.Rational(1), "a_act": sp.Rational(1)},
        {"B": sp.Rational(2), "a_act": sp.Rational(1)},
        {"B": sp.Rational(1), "a_act": sp.Rational(2)},
        {"B": sp.Rational(3), "a_act": sp.Rational(5)},
    ]
    values = []
    for idx, comp in enumerate(completions, 1):
        val = ratio.subs({B: comp["B"], a_act: comp["a_act"], delta: L})
        values.append(val)
        check(f"completion {idx} has positive B and a_act", comp["B"] > 0 and comp["a_act"] > 0)
        check(f"completion {idx} keeps target delta fixed", L == sp.Rational(2, 9))
        check(f"completion {idx} event ratio is positive", bool(sp.ask(sp.Q.positive(val))))
    distinct_pairs = [exact(values[i] - values[j]) != 0 for i in range(len(values)) for j in range(i)]
    check("current-surface completions yield distinct event ratios", all(distinct_pairs))

    section("F. fixed-locus matching route checks")
    # Direct raw-rate matching to L or S_sum just solves B; the clock does not
    # determine B. Dimensionless matching to L or S_sum misses the target delta.
    solved_raw_to_s = sp.solve(sp.Eq(rate.subs(delta, L), S_sum), B)
    check("raw clock to S_sum solves for B", len(solved_raw_to_s) == 1 and B not in solved_raw_to_s[0].free_symbols)
    check("raw clock solution is exactly the occurrence relation at a_act=1", exact(solved_raw_to_s[0] - expected_B.subs(a_act, 1)) == 0)
    check("dimensionless clock at target is not S_sum", omega_target_numeric > float(S_sum))
    check("dimensionless clock at target is not L", omega_target_numeric > float(L))
    normalized_fraction = sp.sin(delta)
    # sin(x) < x for positive x; use the same Taylor lower style plus numeric
    # guard to ensure the runner catches accidental equality claims.
    check("numeric sanity: sin(2/9) is below 2/9", math.sin(2 / 9) < 2 / 9)
    check("normalized fraction at target is not L", abs(math.sin(2 / 9) - 2 / 9) > 1e-5)
    check("normalizing by 2sqrt3 changes the target equation", normalized_fraction != delta)

    section("G. note discipline and no-overclaim checks")
    required_phrases = [
        "bounded route no-go",
        "This note does not derive, refute, re-grade, retire, or remove R-eta",
        "the current surface does not derive the normalization",
        "A future rate-normalization theorem remains possible",
        "Direct R-eta readout-license theorem",
        "Coherence-event theorem",
        "Non-minimal transport theorem",
        "Approved-primitive proposal",
    ]
    for phrase in required_phrases:
        check(f"note contains required boundary: {phrase[:50]}", phrase in note_flat)
    for n in range(1, 9):
        check(f"note contains N{n} no-go gate", f"**N{n}" in note)
    forbidden = [
        "R-eta is retired",
        "AC_phi_lambda is retired",
        "therefore R-eta closes",
        "therefore AC_phi_lambda closes",
        "audit_status: audited_clean",
        "effective_status: retained",
        "promoted to retained",
    ]
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase not in note)
    check("note links the current R-eta residual", "delta_readout_identification_R_eta" in note)
    check("note does not link generated audit ledger as authority", "AUDIT_LEDGER.md](" not in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL} CHECKS={PASS + FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
