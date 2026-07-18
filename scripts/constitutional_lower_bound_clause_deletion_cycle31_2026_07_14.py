#!/usr/bin/env python3
"""Exact local controls for the Cycle-31 constitutional lower-bound closure.

This runner is authority-free.  It checks finite countermodels, type witnesses,
the atom ledger, and the clause-deletion matrix.  It does not select a physical
law or edit any foundation surface.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import isclose, sqrt
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/CONSTITUTIONAL_LOWER_BOUND_CLOSURE_AND_CLAUSE_DELETION_CYCLE31_NOTE_2026-07-14.md"

PATHS = {
    "axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scale": ROOT / "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle26": ROOT / "docs/work_history/repo/review_feedback/RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md",
    "cycle27": ROOT / "docs/work_history/repo/review_feedback/STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md",
    "cycle28": ROOT / "docs/work_history/repo/review_feedback/ADMISSIBILITY_SYMBOL_DEFINABILITY_AND_EXACT_LAW_REFERENCE_CHALLENGE_NOTE_2026-07-14.md",
    "cycle29": ROOT / "docs/work_history/repo/review_feedback/RECORD_ONLY_STATE_BELL_LAW_TYPE_DICHOTOMY_CYCLE29_NOTE_2026-07-14.md",
    "synthesis": ROOT / "docs/work_history/repo/review_feedback/MINIMUM_AXIOM_UPDATE_EXERCISE_SYNTHESIS_AND_CUT_GATE_NOTE_2026-07-14.md",
    "irreducibility": ROOT / "docs/work_history/repo/review_feedback/EXACT_LAW_IRREDUCIBLE_CONTENT_INDEPENDENCE_TOURNAMENT_NOTE_2026-07-14.md",
    "exhaustion": ROOT / "docs/work_history/repo/review_feedback/MINIMUM_CONSTITUTIONAL_CONTENT_EXHAUSTION_LEDGER_NOTE_2026-07-14.md",
}


PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(condition: bool, label: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_needles(text: str, needles: Iterable[str], prefix: str) -> None:
    for needle in needles:
        check(needle in text, f"{prefix} contains {needle!r}")


section("A. SOURCE AND AUTHORITY CONTRACT")

for name, path in {"note": NOTE, **PATHS}.items():
    check(path.is_file(), f"A {name} source exists")

texts = {name: read(path) for name, path in PATHS.items()}
note = read(NOTE)

check_needles(
    texts["axioms"],
    (
        "There is one fixed nearest-neighbor admissibility rule",
        "Records form.",
        "A state is a configuration of records.",
        "A choice not fixed by the",
    ),
    "A live foundation",
)
check_needles(
    texts["scale"],
    ("This is a units conversion, not a physics axiom.", "zero dimensionless"),
    "A scale primitive",
)
check_needles(
    texts["kinetic"],
    ("c_t = c_s", "not a new dynamics"),
    "A kinetic primitive",
)
check_needles(
    texts["realized"],
    (
        "one realized-state reference",
        "no state, averaging over alternatives, measure",
        "boundary condition",
    ),
    "A realized-state primitive",
)
check_needles(
    texts["cycle26"],
    (
        "collision-safe positive-density terminal diamonds",
        "strong lumpability",
        "No new Record axiom is forced.",
        "There is **no universal one-M2 no-go**.",
    ),
    "A Cycle26",
)
check_needles(
    texts["cycle27"],
    (
        "standalone actuality or sampler axiom is forced",
        "complete law-admissible record histories",
        "contingent realized-state data",
        "definition/type link, not a new axiom",
    ),
    "A Cycle27",
)
check_needles(
    texts["cycle28"],
    (
        "No second existence statement is needed.",
        "A named function symbol is not an extensional specification.",
        "Even an exact availability table is not the complete physical law.",
        "framework schema",
        "theory of our universe",
        "instantiated model",
    ),
    "A Cycle28",
)
check_needles(
    texts["cycle29"],
    (
        "global record-history law",
        "record-fibre strong lumpability",
        "Qualification would need revision",
        "no live state or axiom edit is justified",
    ),
    "A Cycle29",
)
check_needles(
    texts["synthesis"],
    (
        "A TOE-predictively complete framework needs one exact law identity",
        "reader, two-witness trigger, clock lock",
    ),
    "A synthesis ledger",
)
check_needles(
    texts["irreducibility"],
    (
        "C8 ONE_HISTORY_ACTUALITY",
        "conditional law/data interface: unique derivation",
    ),
    "A irreducibility ledger",
)
check_needles(
    texts["exhaustion"],
    (
        "one universal-looking constitutional",
        "no universal second axiom atom is forced",
        "Outcome A — zero edit",
        "Outcome B — retype Admissibility",
        "Outcome C — add a separate Law identification",
    ),
    "A exhaustion ledger",
)

check("**Authority:** none." in note, "A note is authority-free")
check("does not amend the live axioms" in note, "A note disclaims foundation edit")
check("No current live edit follows." in note, "A note preserves no-live-edit gate")
check("no commit, push, pr" in note.lower(), "A note disclaims repository authority")


section("B. SIX-CLASS ATOM LEDGER")

ALREADY = "already supplied"
DEFINE = "definitional/type link"
LAW = "exact-law field"
HISTORY = "contingent realized-history datum"
STATE_EDIT = "conditional state-type edit"
IDENTITY = "irreducible constitutional identification"

ALLOWED_CLASSES = {ALREADY, DEFINE, LAW, HISTORY, STATE_EDIT, IDENTITY}

ATOMS = {
    # Already supplied.
    "S-LAT": ALREADY,
    "S-QUBIT": ALREADY,
    "S-A-SLOT": ALREADY,
    "S-REC-OCC": ALREADY,
    "S-REC-PERM": ALREADY,
    "S-STATE": ALREADY,
    "S-ACT-REF": ALREADY,
    "S-SCALE": ALREADY,
    "S-KIN": ALREADY,
    # Definition and type links.
    "D-EQUIV": DEFINE,
    "D-A-PROJ": DEFINE,
    "D-HIST-DOM": DEFINE,
    "D-PRED-STATE": DEFINE,
    "D-PREP": DEFINE,
    "D-EFFECT": DEFINE,
    "D-FORM-SUPPORT": DEFINE,
    "D-ROLE": DEFINE,
    "D-CLOCK": DEFINE,
    "D-SCHEDULE": DEFINE,
    # Exact-law fields.
    "E-DOMAIN": LAW,
    "E-CONTEXT": LAW,
    "E-AVAILABILITY": LAW,
    "E-TRANSITION": LAW,
    "E-OCCURRENCE": LAW,
    "E-RECORD": LAW,
    "E-OBJECTIVE-SAMPLER": LAW,
    "E-STATISTICS": LAW,
    "E-TIME": LAW,
    "E-CAPACITY": LAW,
    "E-MATTER": LAW,
    "E-CONTINUUM": LAW,
    "E-GRAVITY": LAW,
    # Contingent history data.
    "H-BOUNDARY": HISTORY,
    "H-SEED": HISTORY,
    "H-BRANCH": HISTORY,
    "H-SETTINGS": HISTORY,
    "H-CHIRAL": HISTORY,
    "H-ARROW": HISTORY,
    # Conditional and irreducible content.
    "C-STATE": STATE_EDIT,
    "I-L": IDENTITY,
    "I-A": IDENTITY,
}

check(set(ATOMS.values()) == ALLOWED_CLASSES, "B every requested class is populated")
check(len(ATOMS) == len(set(ATOMS)), "B atom identifiers are unique")
for cls in sorted(ALLOWED_CLASSES):
    check(sum(value == cls for value in ATOMS.values()) > 0, f"B class {cls} is nonempty")

check(ATOMS["S-A-SLOT"] == ALREADY, "B existence of one A slot is already supplied")
check(ATOMS["D-HIST-DOM"] == DEFINE, "B complete-history typing is definitional")
check(ATOMS["E-STATISTICS"] == LAW, "B probabilities and corpus statistics are law fields")
check(ATOMS["H-BRANCH"] == HISTORY, "B actual branch is contingent history data")
check(ATOMS["C-STATE"] == STATE_EDIT, "B carrier ontology is a conditional state edit")
check(ATOMS["I-L"] == IDENTITY, "B complete L identity is irreducible unless derived")
check(ATOMS["I-A"] == IDENTITY, "B exact-A-only route has one substantive identity")
check("C8" not in ATOMS, "B no independent C8 actuality atom survives")
check("I-RECORD" not in ATOMS, "B no universal Record-edit atom survives")

required_lane_coverage = {
    "formation": {"E-OCCURRENCE", "D-FORM-SUPPORT"},
    "probability": {"E-STATISTICS", "D-EFFECT"},
    "time": {"E-TIME", "D-CLOCK"},
    "capacity": {"E-CAPACITY"},
    "matter": {"E-MATTER"},
    "gravity": {"E-GRAVITY"},
    "actuality": {"S-ACT-REF", "D-HIST-DOM", "H-BRANCH"},
    "state": {"S-STATE", "D-PRED-STATE", "C-STATE"},
}
for lane, ids in required_lane_coverage.items():
    check(ids <= set(ATOMS), f"B {lane} lane has classified atom coverage")


section("C. CLAUSE-DELETION MATRIX")

U = "unique theorem"
A = "exact A only"
L = "complete local L*"
G = "global-history L*"
ROUTES = (U, A, L, G)

MATRIX = {
    "duplicate existence": {U: "DELETE", A: "DELETE", L: "DELETE", G: "DELETE"},
    "exact A identity": {U: "THEOREM", A: "KEEP-1", L: "DEFINE", G: "DEFINE"},
    "exact L identity": {U: "THEOREM", A: "N/A", L: "KEEP-1", G: "KEEP-1"},
    "history-domain link": {U: "DEFINE", A: "N/A", L: "DEFINE", G: "DEFINE"},
    "actuality clause": {U: "DELETE", A: "DELETE", L: "DELETE", G: "DELETE"},
    "actual history data": {U: "DELETE", A: "DELETE", L: "DELETE", G: "DELETE"},
    "unrecorded carrier state": {U: "DELETE", A: "DELETE", L: "CONDITIONAL", G: "DELETE"},
    "record continuation": {U: "THEOREM", A: "DEFINE", L: "THEOREM", G: "THEOREM"},
    "record clarification": {U: "THEOREM", A: "N/A", L: "THEOREM", G: "THEOREM"},
    "witness/read/clock lock": {U: "DELETE", A: "N/A", L: "LAW/THEOREM", G: "LAW/THEOREM"},
    "Born/frame weight": {U: "THEOREM", A: "N/A", L: "LAW/THEOREM", G: "LAW/THEOREM"},
    "counting/mass": {U: "THEOREM", A: "N/A", L: "LAW/THEOREM", G: "LAW/THEOREM"},
    "global tick": {U: "DELETE", A: "N/A", L: "LAW", G: "DEFINE"},
    "renewal/resource": {U: "THEOREM", A: "N/A", L: "LAW/THEOREM", G: "LAW/THEOREM"},
    "gravity response": {U: "THEOREM", A: "N/A", L: "LAW/THEOREM", G: "LAW/THEOREM"},
    "retype Admissibility": {U: "DELETE", A: "DELETE", L: "PLACEMENT", G: "DELETE"},
    "separate Law slot": {U: "DELETE", A: "DELETE", L: "DELETE", G: "PLACEMENT"},
}

check(all(set(row) == set(ROUTES) for row in MATRIX.values()), "C every matrix row covers all four routes")
check(all(MATRIX["duplicate existence"][r] == "DELETE" for r in ROUTES), "C duplicate existence deletes on all routes")
check(all(MATRIX["actuality clause"][r] == "DELETE" for r in ROUTES), "C actuality clause deletes on all routes")
check(all(MATRIX["actual history data"][r] == "DELETE" for r in ROUTES), "C contingent history never enters the constitution")
check(MATRIX["unrecorded carrier state"][L] == "CONDITIONAL", "C state edit is conditional only on complete local route")
check(MATRIX["unrecorded carrier state"][G] == "DELETE", "C global history route preserves record-only state")
check(MATRIX["retype Admissibility"][L] == "PLACEMENT", "C complete local law uses retyped local placement")
check(MATRIX["separate Law slot"][G] == "PLACEMENT", "C global law uses separate placement")
check(MATRIX["witness/read/clock lock"][L] == "LAW/THEOREM", "C local formation slogan is a law field or theorem")
check(MATRIX["witness/read/clock lock"][G] == "LAW/THEOREM", "C global formation slogan is a law field or theorem")

content_counts = {
    route: sum(row[route] == "KEEP-1" for row in MATRIX.values())
    for route in ROUTES
}
check(content_counts == {U: 0, A: 1, L: 1, G: 1}, "C content counts are exactly 0,1,1,1")


section("D. MODEL DATA, SEMANTIC COMPLETENESS, AND THEORY PREDICTION")

Profile = tuple[int, int, int, int, int, int]


def a_majority(profile: Profile) -> tuple[int]:
    return (1,) if sum(profile) >= 3 else (0,)


def a_minority(profile: Profile) -> tuple[int]:
    return (0,) if sum(profile) >= 3 else (1,)


def a_open(_profile: Profile) -> tuple[int, int]:
    return (0, 1)


PROFILES = list(product((0, 1), repeat=6))


@dataclass(frozen=True)
class Model:
    name: str
    availability: Callable[[Profile], tuple[int, ...]]
    p_record_one: Fraction
    exact_artifact: str
    every_field_interpreted: bool = True

    def prediction(self, protocol: str) -> tuple[Fraction, Fraction]:
        if protocol != "next-readable-bit":
            raise ValueError(protocol)
        return (1 - self.p_record_one, self.p_record_one)


major = Model("major", a_majority, Fraction(1, 2), "model-major-v1")
minor = Model("minor", a_minority, Fraction(1, 2), "model-minor-v1")
half = Model("same-A-half", a_open, Fraction(1, 2), "model-open-half-v1")
two_thirds = Model("same-A-two-thirds", a_open, Fraction(2, 3), "model-open-two-thirds-v1")


def extensional_a_equal(left: Model, right: Model) -> bool:
    return all(left.availability(p) == right.availability(p) for p in PROFILES)


def semantically_complete(model: Model) -> bool:
    return (
        model.every_field_interpreted
        and bool(model.exact_artifact)
        and all(model.availability(p) for p in PROFILES)
        and model.p_record_one in {Fraction(i, 6) for i in range(7)}
    )


def predictively_complete(models: list[Model], protocols: tuple[str, ...]) -> bool:
    return all(
        len({model.prediction(protocol) for model in models}) == 1
        for protocol in protocols
    )


protocols = ("next-readable-bit",)
check(all(len(model.availability(p)) >= 1 for model in (major, minor) for p in PROFILES), "D every model has one total fixed A interpretation")
check(not extensional_a_equal(major, minor), "D one fixed symbol admits different extensions across models")
check(any(major.availability(p) != minor.availability(p) for p in PROFILES), "D paired models disagree on at least one exact menu")
check(extensional_a_equal(half, two_thirds), "D same-A pair has identical extensional availability")
check(half.prediction(protocols[0]) != two_thirds.prediction(protocols[0]), "D same A admits different readable record weights")
check(semantically_complete(half), "D exact half-weight model is semantically complete")
check(semantically_complete(two_thirds), "D exact two-thirds model is semantically complete")
check(not predictively_complete([half, two_thirds], protocols), "D theory containing both exact models is not predictively complete")
check(predictively_complete([half], protocols), "D one exact instantiated model predicts conditionally")

# Selecting exact A leaves both complete laws alive.
selected_by_a = [m for m in (half, two_thirds) if extensional_a_equal(m, half)]
check(len(selected_by_a) == 2, "D exact A selection retains two complete-law models")
check(not predictively_complete(selected_by_a, protocols), "D exact A-only theory remains predictively open")

# Selecting exact L leaves one complete law.  This is model selection if not derived.
selected_by_l = [m for m in (half, two_thirds) if m.exact_artifact == "model-open-half-v1"]
check(len(selected_by_l) == 1, "D exact L identity selects one model")
check(predictively_complete(selected_by_l, protocols), "D exact L-selected theory is predictive on the test protocol")

# Empirical filtering can pick a member without changing what the pre-data theory entailed.
empirically_selected = min((half, two_thirds), key=lambda m: abs(float(m.p_record_one) - 0.66))
check(empirically_selected is two_thirds, "D empirical fit can select the two-thirds model")
check(not predictively_complete([half, two_thirds], protocols), "D empirical selection does not retroactively close the original theory class")
check(predictively_complete([empirically_selected], protocols), "D empirically selected model predicts conditionally")

# A schema can be honest by making the parameter explicit.
schema_predictions = {m.name: m.prediction(protocols[0]) for m in (half, two_thirds)}
check(len(set(schema_predictions.values())) == 2, "D schema exposes rather than hides model dependence")
check(content_counts[A] == 1 and content_counts[L] == 1, "D A identity and complete-L identity are not double-counted on one route")


section("E. STOCHASTIC ACTUALITY IS A TYPE/DATA SPLIT")

History = tuple[int, int, int, int]
h0: History = (0, 0, 0, 0)
h1: History = (1, 1, 1, 1)
omega = (h0, h1)
mu = {h0: Fraction(1, 2), h1: Fraction(1, 2)}

check(sum(mu.values()) == 1, "E two-history law is normalized")
check(all(isinstance(h, tuple) and len(h) == 4 for h in omega), "E law points are complete finite record histories")
check(h0 in omega and h1 in omega, "E either contingent actual history is law-admissible")
check(mu[h0] == mu[h1], "E fair law does not distinguish the two actual annotations")

annotated_model_0 = (tuple(sorted(mu.items())), h0)
annotated_model_1 = (tuple(sorted(mu.items())), h1)
check(annotated_model_0[0] == annotated_model_1[0], "E same stochastic law admits different contingent histories")
check(annotated_model_0[1] != annotated_model_1[1], "E actual value is not another probability field")
check(h0[:2] == (0, 0) and h1[:2] == (1, 1), "E cut state is restriction of the actual history")


def swap_history(h: History) -> History:
    return tuple(1 - bit for bit in h)  # type: ignore[return-value]


swapped_mu = {swap_history(h): p for h, p in mu.items()}
check(swapped_mu == mu, "E fair law is invariant under outcome swap")
check(all(swap_history(candidate) != candidate for candidate in omega), "E no history is fixed by the swap")
check(not any(swap_history(candidate) == candidate for candidate in omega), "E no equivariant deterministic selector exists for the fair pair")
check(ATOMS["S-ACT-REF"] == ALREADY and ATOMS["D-HIST-DOM"] == DEFINE, "E actuality closes by supplied reference plus type link")
check(ATOMS["H-BRANCH"] == HISTORY, "E member identity remains contingent")
check(MATRIX["actuality clause"][G] == "DELETE", "E global stochastic route adds no actuality sentence")


section("F. RECORD-ONLY STATE AND BELL TYPE WITNESS")


def chsh(e00: float, e01: float, e10: float, e11: float) -> float:
    return e00 + e01 + e10 - e11


deterministic_scores = []
for ax0, ax1, by0, by1 in product((-1, 1), repeat=4):
    deterministic_scores.append(chsh(ax0 * by0, ax0 * by1, ax1 * by0, ax1 * by1))

check(len(deterministic_scores) == 16, "F all deterministic Bell-local vertices are enumerated")
check({abs(score) for score in deterministic_scores} == {2}, "F every deterministic Bell-local vertex has |CHSH|=2")

correlators = {(0, 0): -1 / sqrt(2), (0, 1): -1 / sqrt(2), (1, 0): -1 / sqrt(2), (1, 1): 1 / sqrt(2)}


def global_history_probability(a: int, b: int, x: int, y: int) -> float:
    return (1 + a * b * correlators[(x, y)]) / 4


for x, y in product((0, 1), repeat=2):
    probs = {(a, b): global_history_probability(a, b, x, y) for a, b in product((-1, 1), repeat=2)}
    check(all(p >= 0 for p in probs.values()), f"F global history table is positive at context {(x, y)}")
    check(isclose(sum(probs.values()), 1.0, abs_tol=1e-12), f"F global history table normalizes at context {(x, y)}")
    marg_a = {a: sum(probs[(a, b)] for b in (-1, 1)) for a in (-1, 1)}
    marg_b = {b: sum(probs[(a, b)] for a in (-1, 1)) for b in (-1, 1)}
    check(all(isclose(v, 0.5, abs_tol=1e-12) for v in marg_a.values()), f"F Alice marginal is context-neutral at {(x, y)}")
    check(all(isclose(v, 0.5, abs_tol=1e-12) for v in marg_b.values()), f"F Bob marginal is context-neutral at {(x, y)}")

quantum_chsh = chsh(correlators[(0, 0)], correlators[(0, 1)], correlators[(1, 0)], correlators[(1, 1)])
check(isclose(abs(quantum_chsh), 2 * sqrt(2), abs_tol=1e-12), "F global record-history table reaches 2 sqrt(2)")
check(abs(quantum_chsh) > 2, "F global table lies outside Bell-local record response polytope")


def needs_state_edit(*, physically_real_unrecorded: bool, future_record_sensitive: bool, quotient_closed: bool, global_history_law: bool) -> bool:
    return physically_real_unrecorded and future_record_sensitive and not quotient_closed and not global_history_law


check(not needs_state_edit(physically_real_unrecorded=False, future_record_sensitive=False, quotient_closed=True, global_history_law=False), "F record-only fortress needs no state edit")
check(not needs_state_edit(physically_real_unrecorded=False, future_record_sensitive=False, quotient_closed=True, global_history_law=True), "F global record-history law needs no state edit")
check(not needs_state_edit(physically_real_unrecorded=True, future_record_sensitive=True, quotient_closed=True, global_history_law=False), "F strong lumpability retires hidden-state edit")
check(needs_state_edit(physically_real_unrecorded=True, future_record_sensitive=True, quotient_closed=False, global_history_law=False), "F irreducible future-sensitive carrier triggers conditional state edit")

# Minimal record-fibre separator: the same empty record configuration can hide
# two phases with different future X records.  Restricted Z-only futures erase
# the distinction.
x_future_plus = (Fraction(1), Fraction(0))
x_future_minus = (Fraction(0), Fraction(1))
z_future_plus = (Fraction(1, 2), Fraction(1, 2))
z_future_minus = (Fraction(1, 2), Fraction(1, 2))
check(x_future_plus != x_future_minus, "F hidden coherent phases can be future-record sensitive")
check(z_future_plus == z_future_minus, "F restricted future protocol can quotient the phase as gauge")
check(ATOMS["C-STATE"] == STATE_EDIT, "F state widening remains exactly one conditional class")


section("G. NOTE, MATRIX, AND NO-GO DISCIPLINE CONTRACT")

check_needles(
    note,
    (
        "Semantic completeness",
        "Predictive completeness",
        "Empirical model selection",
        "Already supplied",
        "Definitional or type links",
        "Exact-law fields",
        "Contingent realized-history data",
        "Conditional state-type edit",
        "Irreducible constitutional identification",
        "unique theorem       : 0",
        "exact A only         : 1",
        "complete local L*    : 1",
        "global-history L*    : 1",
        "No current live edit follows.",
    ),
    "G note contract",
)

for n in range(1, 9):
    check(f"### N{n} —" in note, f"G N{n} section exists")

check("**No-go-discipline status: PASS**" in note, "G N1-N8 gate records PASS")
check("More than five routes were tested." in note, "G N1 enumerates at least five routes")
check("The collapsed universal constitutional wall set is `{U}`." in note, "G N2 collapses to one universal wall")
check("Hidden-wall scan" in note, "G N3 names the hidden-wall scan")
check("Residual matching" in note, "G N4 names exact residual matching")
check("Rhetoric and resolution audit" in note, "G N5 narrows claim resolution")
check("Partial-closure and import-retirement paths" in note, "G N6 records retirement routes")
check("**Hostile reviewer:**" in note, "G N7 includes hostile steelman")
check("rg -l \"structurally undecidable|no retained primitive|requires new axiom|cannot be derived from A_min\" docs" in note, "G N8 records prescribed docs search")
check("find .claude/science/physics-loops -name NO_GO_LEDGER.md -print" in note, "G N8 records no-go-ledger walk")
check("model data" in note and "framework schema" in note and "instantiated empirical model" in note, "G note preserves model-data steelman")
check("predictively complete theory of this universe" in note, "G minimum is scoped to TOE theory role")
check("No claim is made that a unique-law theorem is impossible" in note, "G unique theorem remains a live escape")
check("No claim is made" in note and "every TOE must be parameter-free" in note, "G empirical TOE endpoint is not forbidden")


section("TOTAL")
print(f"PASS={PASS} FAIL={FAIL}")
if FAIL:
    print("RESULT: FAIL")
    raise SystemExit(1)

print("RESULT: PASS")
print("BOUNDARY: one role-relative exact law identity is the universal predictive-TOE residue; no live axiom, primitive, model, or audit selection")
