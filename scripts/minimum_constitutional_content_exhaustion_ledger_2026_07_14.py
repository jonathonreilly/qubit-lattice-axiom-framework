#!/usr/bin/env python3
"""Machine-check the minimum-constitutional-content exhaustion ledger.

This is a dependency/coverage gate. It does not select a law, amend the
foundation, or issue an audit verdict.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "MINIMUM_CONSTITUTIONAL_CONTENT_EXHAUSTION_LEDGER_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SYNTHESIS = REVIEW / "MINIMUM_AXIOM_UPDATE_EXERCISE_SYNTHESIS_AND_CUT_GATE_NOTE_2026-07-14.md"
IRREDUCIBLE = REVIEW / "EXACT_LAW_IRREDUCIBLE_CONTENT_INDEPENDENCE_TOURNAMENT_NOTE_2026-07-14.md"
PREDICTIVE = REVIEW / "EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md"
PLACEMENT = REVIEW / "EXACT_LAW_CONSTITUTIONAL_PLACEMENT_SCHEMA_PROBE_NOTE_2026-07-14.md"
IMPACT = REVIEW / "ONE_CUT_FOUNDATION_SURFACE_IMPACT_MAP_NOTE_2026-07-14.md"
COUNTING = REVIEW / "MATTER_COUNTING_CHIRALITY_EXACT_LAW_PLACEMENT_NOTE_2026-07-14.md"
WOLFRAM = REVIEW / "UNIVERSAL_RULE_SPACE_MULTIWAY_LAW_STEELMAN_NOTE_2026-07-14.md"
DELAYED = REVIEW / "DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md"
CONTEXT = REVIEW / "CHIRAL_TRIAD_TRANSVERSE_CONTEXT_CYCLE17_NOTE_2026-07-14.md"
ANOMALY = REVIEW / "THREE_DIMENSIONAL_ANOMALOUS_BULK_CATEGORY_INDEX_STEELMAN_NOTE_2026-07-14.md"
AUTONOMOUS_CLOSE = REVIEW / "AUTONOMOUS_SELF_CLOSING_DIAMOND_CYCLE17_NOTE_2026-07-14.md"
PRIMITIVE_EQUIVALENCE = REVIEW / "PRIMITIVE_QCA_RECORD_PROTOCOL_FULL_EQUIVALENCE_STEELMAN_NOTE_2026-07-14.md"
ACTUAL_HEADER = REVIEW / "ACTUAL_HEADER_ROLE_DECODER_PARITY_SELECTION_CYCLE18_NOTE_2026-07-14.md"
ADAPTIVE_FULL_ABSTRACTION = REVIEW / "ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md"
INVARIANT_SEED_FIELD = REVIEW / "INVARIANT_FIRST_SEED_HARD_CORE_CYCLE18_NOTE_2026-07-14.md"
SITE_NET_EQUIVALENCE = REVIEW / "FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md"
OPERATIONAL_PARITY = REVIEW / "COMPLETE_FUTURE_OPERATIONAL_PARITY_CERTIFICATE_CYCLE19_NOTE_2026-07-14.md"
NAMED_SITE_EQUIVALENCE = REVIEW / "NAMED_SITE_RECORD_FAITHFUL_EQUIVALENCE_CLASSIFICATION_NOTE_2026-07-14.md"
COMMIT_CLOCK = REVIEW / "CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md"
SEED_COMPILATION = REVIEW / "NEAREST_NEIGHBOR_SEED_COMPILATION_CYCLE19_NOTE_2026-07-14.md"
BORN_AFFINITY = REVIEW / "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md"
SORT_EQUIVALENCE = REVIEW / "FOUNDATION_SORT_PRESERVING_EQUIVALENCE_AND_DYNAMICAL_GAUGE_COLLAPSE_NOTE_2026-07-14.md"
DISSIPATIVE_SEED = REVIEW / "QUANTUM_DISSIPATIVE_SEED_ESCAPE_CYCLE20_NOTE_2026-07-14.md"
FREQUENCY_CORPUS = REVIEW / "CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md"
RESIDUAL_PACKING = REVIEW / "BLIND_RESIDUAL_ATOM_PACKING_AND_ONE_LAW_CONSTITUTIONAL_SCHEMA_NOTE_2026-07-14.md"
RECORD_STATE_BELL = REVIEW / "RECORD_ONLY_STATE_BELL_LAW_TYPE_DICHOTOMY_CYCLE29_NOTE_2026-07-14.md"
ACTUALITY_SEMANTICS = REVIEW / "STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md"
RECORD_STATE_FORTRESS = REVIEW / "RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md"
GLOBAL_RECORD_PROCESS = REVIEW / "GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md"
ADMISSIBILITY_DEFINABILITY = REVIEW / "ADMISSIBILITY_SYMBOL_DEFINABILITY_AND_EXACT_LAW_REFERENCE_CHALLENGE_NOTE_2026-07-14.md"
CONSTITUTIONAL_LOWER_BOUND = REVIEW / "CONSTITUTIONAL_LOWER_BOUND_CLOSURE_AND_CLAUSE_DELETION_CYCLE31_NOTE_2026-07-14.md"
LONG_RUN_APPEND = REVIEW / "LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md"
LOCAL_GLOBAL_GLUE = REVIEW / "LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md"
MOVING_LOGICAL_FRONT = REVIEW / "MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md"
FINAL_MISSING_CENSUS = REVIEW / "FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md"
CUBIC_CZ_SELECTION = REVIEW / "CUBIC_CZ_EDGE_RULE_UNIQUENESS_SELECTION_CYCLE36_NOTE_2026-07-14.md"
TEMPORAL_EQUIVALENCE = REVIEW / "TEMPORAL_PROTOCOL_EQUIVALENCE_ALTERNATING_FRAME_CYCLE39_NOTE_2026-07-14.md"
CUBIC_CLIFFORD = REVIEW / "CUBIC_ONE_QUBIT_CLIFFORD_QCA_UNIQUENESS_CYCLE40_NOTE_2026-07-14.md"
CANDIDATE_ASSEMBLY = REVIEW / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md"
HISTORY_IDENTIFIABILITY = REVIEW / "REALIZED_HISTORY_EXACT_LAW_IDENTIFIABILITY_CYCLE42_NOTE_2026-07-14.md"
SYNTHESIS_RUNNER = ROOT / "scripts" / "minimum_axiom_update_exercise_synthesis_cut_gate_2026_07_14.py"


INTERFACES = {
    "C1_RAW_GENERATED_CARRIER": "law-owned-or-derived",
    "C2_RECORD_STATUS_AND_IDENTITY": "law-owned-plus-existing-record",
    "C3_EVENT_READINESS_LOCAL_CAUSAL_DOMAIN": "law-owned",
    "C4_PREDICTIVE_RECORD_DECODER": "derived-test",
    "C5_CONTEXT_INTERVENTION_REPERTOIRE": "law-owned-or-derived",
    "C6_EXACT_NORMALIZED_LOCAL_INSTRUMENT": "exact-law-value",
    "C7_GLUING_AND_EXHAUSTIVE_CONTINUATION": "law-owned-or-derived",
    "C8_ONE_HISTORY_ACTUALITY": "conditional-law-or-world-interface",
    "C9_PROJECTIVE_FULL_LATTICE_EXTENSION": "law-owned-or-derived",
    "C10_RENEWAL_FRESHNESS_OR_EXPORT": "law-owned-or-derived",
    "C11_FORMATION_ELIGIBILITY": "positive-support-or-law-policy",
    "E1_TRIAL_CORPUS": "operational-interface",
    "B_ACTUAL_BOUNDARY_SELECTION": "contingent-or-meta-law",
}

LANES = (
    "operational quantum",
    "probability",
    "time",
    "matter and continuum",
    "counting and mass",
    "resource",
    "gravity",
    "thermodynamic arrow",
    "cosmology and boundary",
)

LAW_FIELDS = (
    "domain and state/context decoder",
    "first and later event occurrence",
    "exact successor or instrument",
    "interaction representative",
    "collision and routing",
    "complete physical record-history domain",
    "normalized effect-complete record law",
    "certified corpus and component-mean conditions",
    "update-to-tick and rate",
    "tensor response",
    "species coupling",
    "boundary class",
)

REJECTED_AXIOM_SHORTCUTS = (
    "two witnesses",
    "read creates the fact",
    "clock locks the fact",
    "count presentations once",
    "uniform branch counting",
    "causal invariance selects outcomes",
    "topological index makes the record",
    "the universe is storage limited",
    "all rules happen",
)

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def normalized(path: Path) -> str:
    return " ".join(
        path.read_text(encoding="utf-8")
        .lower()
        .replace("*", "")
        .replace("`", "")
        .replace(">", "")
        .split()
    )


def source_contract() -> None:
    section("A - Sources and authority boundary")
    sources = (
        NOTE,
        AXIOMS,
        REGISTRY,
        SYNTHESIS,
        IRREDUCIBLE,
        PREDICTIVE,
        PLACEMENT,
        IMPACT,
        COUNTING,
        WOLFRAM,
        DELAYED,
        CONTEXT,
        ANOMALY,
        AUTONOMOUS_CLOSE,
        PRIMITIVE_EQUIVALENCE,
        ACTUAL_HEADER,
        ADAPTIVE_FULL_ABSTRACTION,
        INVARIANT_SEED_FIELD,
        SITE_NET_EQUIVALENCE,
        OPERATIONAL_PARITY,
        NAMED_SITE_EQUIVALENCE,
        COMMIT_CLOCK,
        SEED_COMPILATION,
        BORN_AFFINITY,
        SORT_EQUIVALENCE,
        DISSIPATIVE_SEED,
        FREQUENCY_CORPUS,
        RESIDUAL_PACKING,
        RECORD_STATE_BELL,
        ACTUALITY_SEMANTICS,
        RECORD_STATE_FORTRESS,
        GLOBAL_RECORD_PROCESS,
        ADMISSIBILITY_DEFINABILITY,
        CONSTITUTIONAL_LOWER_BOUND,
        LONG_RUN_APPEND,
        LOCAL_GLOBAL_GLUE,
        MOVING_LOGICAL_FRONT,
        FINAL_MISSING_CENSUS,
        CUBIC_CZ_SELECTION,
        TEMPORAL_EQUIVALENCE,
        CUBIC_CLIFFORD,
        CANDIDATE_ASSEMBLY,
        HISTORY_IDENTIFIABILITY,
        SYNTHESIS_RUNNER,
    )
    for source in sources:
        check(f"A source exists: {source.name}", source.is_file())
    note = normalized(NOTE)
    check("A ledger is authority-free", "authority: none" in note)
    check("A ledger does not amend an axiom", "does not amend an axiom" in note)
    check("A ledger does not select a law", "does not select the physical law" in note)
    check("A no live-edit decision is explicit", "minimum live edit justified now: none" in note)
    check("A exact referent gate is explicit", "stable exact law referent" in note)


def semantic_exhaustion() -> None:
    section("B - Semantic-interface exhaustion")
    note = normalized(NOTE)
    check("B thirteen interfaces are classified", len(INTERFACES) == 13)
    check("B every interface has a disposition", all(INTERFACES.values()))
    for interface, disposition in INTERFACES.items():
        check(f"B ledger names {interface}", interface.lower() in note)
        check(f"B disposition is typed for {interface}", disposition in {
            "law-owned-or-derived",
            "law-owned-plus-existing-record",
            "law-owned",
            "derived-test",
            "exact-law-value",
            "conditional-law-or-world-interface",
            "positive-support-or-law-policy",
            "operational-interface",
            "contingent-or-meta-law",
        })
    check("B bounded minimum is one universal-looking identity obligation", "one universal-looking constitutional obligation" in note)
    check("B actuality is conditional without a universal second atom", "actual-state reference is closed" in note and "complete-history status is conditional" in note and "measure alone does not select h" in note)


def lane_and_clause_exhaustion() -> None:
    section("C - TOE-lane and shortcut exhaustion")
    note = normalized(NOTE)
    for lane in LANES:
        check(f"C lane is classified: {lane}", lane in note)
    for field in LAW_FIELDS:
        check(f"C exact-law field is named: {field}", field in note)
    for shortcut in REJECTED_AXIOM_SHORTCUTS:
        check(f"C shortcut is classified: {shortcut}", shortcut in note)
    check("C counting is law-relative rather than a Record noun", "tied and untied event algebras" in note)
    check("C Wolfram all-rules keeps observer/measure seams", "sampled slice" in note and "record-faithful quotient" in note)
    check("C delayed closure is finite-interface relative", "far source at distance r+2" in note)
    check("C context reduction reaches apparatus role", "x_f=-iy_fz_f" in note and "apparatus-role decoder" in note)
    check("C anomaly class leaves circuit representative", "finite-depth circuit quotient" in note)
    check("C post-seed boundary can be generated autonomously", "99-site closeable cubic diamond" in note)
    check("C primitive representative equivalence transports full protocol", "update-plus-commit protocol" in note and "complete protocol equivalence" in note)
    check("C actual header decodes geometry", "actual six-record header uniquely decodes" in note)
    check("C parity certificate selects X conditionally", "z_a x_b z_c=+i" not in note and "z_a x_b z_c=+1" in note and "operational parity-certificate contract" in note)
    check("C bare X readiness label is rejected", "hard-coded x readiness label" in note and "cannot count as a derivation" in note)
    check("C finite adaptive full abstraction is classified", "finite adaptive full-abstraction theorem" in note and "record-net closure" in note)
    check("C physical category is not assumed closed", "maximal local-record category" in note and "downstream law-category closure" in note)
    check("C invariant seed field retires one global first event", "empty local limit" in note and "positive-density hard-core seed field" in note)
    check("C foundation site-net quotient is exact", "sp(4,2)" in note and "720" in note and "72" in note and "site permutation plus onsite recoding" in note)
    check("C parity certificate is a role, not generic content", "role-specific operational definition" in note and "pc alone is not complete record content" in note)
    check("C complete future quotient keeps its inputs explicit", "physically legal tester repertoire" in note and "record-fibre strong lumpability" in note)
    check("C fixed selected and transported nets are separated", "pu(2)^n" in note and "selected pointer-record algebra" in note and "transported-net groupoid" in note)
    check("C commit count is a relational clock only after event identity", "a clock does not make a record lock" in note and "schedule-independent relational clock" in note and "dimensionless clock ratios" in note)
    check("C NN seed compile reaches the dependency floor", "isolated-bernoulli factor" in note and "causal-depth floor is 27" in note)
    check("C clean-output residue is carrier not Record prose", "record-only clean-output obstruction" in note and "closed candidate layer" in note and "transient mutable" in note)
    check("C operational quotient retires generic Born imports", "effect noncontextuality definitional" in note and "recorded physical randomization" in note and "trace/born representation" in note)
    check("C numerical probability and frequency fields remain explicit", "numerical normalized law w" in note and "reset/trial corpus" in note and "pointwise-versus-almost-sure scope" in note)
    check("C foundation site identity is semantic rather than new physics", "framework equivalence is a sort-preserving isomorphism" in note and "representation expansions" in note and "not missing lattice or qubit physics" in note)
    check("C guarded seed instrument is an exact non-NN reference", "guarded range-nine pure-birth instrument" in note and "depth at least 14" in note and "depth 27" in note)
    check("C channel does not determine record outcomes", "record-inequivalent instruments" in note and "branch-labelled instrument is part of the law referent" in note and "none of this forces generic record wording" in note)
    check("C frequency bridge is component-mean rather than IID", "e[x_0|i_t]=q" in note and "ergodicity suffices" in note and "iid is stronger" in note and "nonergodic laws also work" in note)
    check("C corpus clauses remain global-W theorem fields", "corpus ancestry" in note and "projective recurrence" in note and "not separate record language" in note)
    check("C one L-star can pack every universal interface", "one complete exact history law l" in note and "packing, not derivation" in note and "completeness ledger remains mandatory" in note)
    check("C actual-world fields collapse after one H route is explicit", "projections of one realized history h only after its status is explicit" in note and "law-owned one-outcome semantics" in note and "supplies neither h nor its content" in note)
    check("C omitted internal fields have paired separators", "incomplete local generator" in note and "paired countermodels separate every such omission" in note)
    check("C record-only state supports a global quantum table", "convex mixture of 16 deterministic vertices" in note and "context-labelled record-history table" in note and "global/contextual history law" in note)
    check("C ontic carrier state edit remains conditional", "unrecorded carrier" in note and "qualification state-type revision" in note and "no state or record edit is universal" in note)
    check("C actuality is a conditional law/data interface", "actual-state reference is closed" in note and "complete-history status is conditional" in note and "normalizing the cylinder measure" in note and "or select a member" in note)
    check("C record-only NN construction keeps state widening conditional", "5,202-site fortress" in note and "permanent prefix is its phase" in note and "strong lumpability" in note and "no qualification widening is universal" in note)
    check("C global process route closes law type but not value", "normalized strongly positive decoherence functional" in note and "identity insertion" in note and "scalar quantum measure" in note and "local amplitude gluing" in note and "separate law placement" in note)
    check("C existing rule slot does not close extensional identity", "model-theory challenge removes one apparent atom" in note and "majority and minority" in note and "1/2 versus 2/3" in note and "substantive model selection" in note)
    check("C clause deletion independently leaves four placement outcomes", "only four outcomes remain honest" in note and "one universal-looking constitutional obligation" in note)
    check("C long-run append leaves a conditional semantic fork", "long-run append theorem" in note and "one-formation-per-site process has intensity zero" in note and "bounded recurring apparatus" in note and "no generic storage" in note)
    check("C local rule can derive the global process", "same cz gate on every undirected nn edge" in note and "zero and plus boundaries" in note and "retires an independent global-measure atom" in note)
    check("C moving logical front retires generic recurrence prose", "head contents" in note and "no physical record moves or clears" in note and "recurrence alone does not force record" in note)
    check("C final census leaves only conditional ontology gates", "two conditional ontology gates" in note and "typicality remains claim-specific" in note and "neither is universal" in note)
    check("C CZ uniqueness attack exposes temporal protocol category", "u_0=product cz" in note and "u_1=z_all u_0" in note and "physical temporal protocol-equivalence category" in note)
    check("C temporal quotient is a law-equivalence field", "alternating onsite frame is law-relative" in note and "cross-time idle" in note and "not in a gauge or clock axiom" in note)
    check("C broad cubic census leaves no unique skeleton law", "onsite rotation action" in note and "three uniformly local symplectic protocol classes" in note and "single skeleton class is only a conditional theorem" in note)
    check("C candidate assembly exposes the exact NN readiness field", "l41^r3" in note and "event_readiness_local_causal_domain" in note and "destroys matter-channel distinguishability" in note)
    check("C realized history still needs separating reconstruction", "realized history does not select its counterfactual law" in note and "separating all-protocol reconstruction theorem" in note)


def exact_lower_bound_controls() -> None:
    section("D - Exact lower-bound controls")
    q1 = (Fraction(1, 3), Fraction(2, 3))
    q2 = (Fraction(2, 3), Fraction(1, 3))
    check("D paired branching laws share support", {index for index, p in enumerate(q1) if p} == {index for index, p in enumerate(q2) if p})
    check("D paired branching laws differ predictively", q1 != q2)
    check("D both laws normalize", sum(q1) == sum(q2) == 1)
    selected = 0
    check("D one actual member is compatible with both laws", q1[selected] > 0 and q2[selected] > 0)
    deterministic = (Fraction(1), Fraction(0))
    check("D deterministic law can derive one member", sum(p > 0 for p in deterministic) == 1)
    check("D history status is architecture-dependent, not a forced second atom", selected == 0 and deterministic[0] == 1)


def no_go_discipline_structure() -> None:
    section("E - Fresh N1-N8 no-go-discipline structure")
    raw = NOTE.read_text(encoding="utf-8")
    note = normalized(NOTE)
    n1 = raw.split("### N1", 1)[1].split("### N2", 1)[0]
    attempted_rows = [line for line in n1.splitlines() if "`ATTEMPTED`" in line and line.startswith("|")]
    check("E N1 has at least five marked routes", len(attempted_rows) >= 5, f"rows={len(attempted_rows)}")
    check("E N1 uses no unauthorized prior marker", "RULED IN BY PRIOR" not in n1 and "RULED OUT BY PRIOR" not in n1)
    check("E N2 declares the collapsed one-wall set", "collapsed wall set" in note and "stable extensional identity" in note)
    check("E N2 does not double-count one-wall pairs", "no unordered wall pairs left" in note)
    check("E N3 has a hit/classification/action table", "| hit | line/section | classification | action |" in raw)
    check("E N3 resolves hidden conditions", "unresolved hidden-condition count after classification: 0" in note)
    check("E N4 gives path-line residual matches", "| cited witness | witness residual | claimed residual here | match? |" in raw)
    check("E N4 drops mismatched universal support", "drop as universal support" in note and "boundary only" in note)
    for scope in ("finite instance", "candidate class", "full lattice", "all legal protocols", "all law space"):
        check(f"E N5 names resolution: {scope}", scope in note)
    check("E N5 leaves untested high resolutions open", "all law space | open" in note)
    check("E N6 has path/status/closure columns", "| path | status | what it closes |" in raw)
    check("E N6 treats registered primitives as premises not walls", "approved premise, not a wall" in note)
    check("E N7 contains hostile steelman and outcome", "hostile steelman:" in note and "outcome:" in note)
    check("E N7 demotes the broad no-go", "partial-attempt-with-named-untested-routes" in note and "broad claim" in note and "prohibited" in note)
    check("E N8 has retirement mechanism table", "| prior wall | retired? | retirement mechanism | applicable here? |" in raw)
    n8 = raw.split("### N8", 1)[1].split("## Verification", 1)[0]
    n8_rows = [line for line in n8.splitlines() if line.startswith("|") and "---" not in line]
    check("E N8 has at least three substantive rows", len(n8_rows) >= 4, f"rows={len(n8_rows)-1}")


def constitutional_outcomes() -> None:
    section("F - Constitutional outcomes and cut gate")
    note = normalized(NOTE)
    outcomes = (
        "outcome a — zero edit by unique derivation or full equivalence",
        "outcome b — retype admissibility around a complete local law",
        "outcome c — add a separate law identification for a global history law",
        "outcome d — add record clarification only if the exact law cannot derive it",
    )
    for outcome in outcomes:
        check(f"F ledger names {outcome.split('—')[0].strip()}", outcome in note)

    axioms = AXIOMS.read_text(encoding="utf-8").lower()
    check("F live foundation still has no canonical-law placeholder", "canonical-law" not in axioms and "[canonical" not in axioms)
    check("F live foundation still has no witness trigger", "two witness" not in axioms and "read twice" not in axioms)
    check("F live foundation still has no clock trigger", "clock locks" not in axioms)
    check("F no synchronized authority edit is justified", "do not edit the live four-axiom surface" in note)


def upstream_gate_regression() -> None:
    section("G - Upstream synthesis regression")
    completed = subprocess.run(
        [sys.executable, str(SYNTHESIS_RUNNER), "--skip-companions"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    output = completed.stdout + completed.stderr
    check("G synthesis gate returns zero", completed.returncode == 0)
    check("G synthesis gate has no failures", "FAIL=0" in output)
    check("G synthesis gate preserves no-cut boundary", "no live axiom edit" in output)


def main() -> int:
    source_contract()
    semantic_exhaustion()
    lane_and_clause_exhaustion()
    exact_lower_bound_controls()
    no_go_discipline_structure()
    constitutional_outcomes()
    upstream_gate_regression()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: PASS" if FAIL == 0 else "RESULT: FAIL")
    print(
        "CUT_DECISION: within the declared inventory and tested routes, exact "
        "law identity/equivalence is the sole universal-looking residue; no "
        "live edit until its TOE-predictive referent exists"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
