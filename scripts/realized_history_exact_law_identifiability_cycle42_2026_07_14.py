#!/usr/bin/env python3
"""Cycle 42 exact controls for realized-history law identifiability."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "REALIZED_HISTORY_EXACT_LAW_IDENTIFIABILITY_CYCLE42_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
CENSUS = REVIEW / "FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md"
FREQUENCY = REVIEW / "CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md"
ACTUALITY = REVIEW / "STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md"
ADAPTIVE = REVIEW / "ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md"

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
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def markdown_subsection(text: str, number: int) -> str:
    """Return one N-section without relying on source line numbers."""
    lowered = text.lower()
    start_marker = f"### n{number} —"
    end_marker = f"### n{number + 1} —" if number < 8 else "## bottom line"
    start = lowered.index(start_marker)
    end = lowered.index(end_marker, start)
    return lowered[start:end]


def source_contract() -> None:
    section("A - Source, authority, and foundation boundary")
    for path in (NOTE, AXIOMS, REALIZED, CENSUS, FREQUENCY, ACTUALITY, ADAPTIVE):
        check(f"A source exists: {path.name}", path.is_file())
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    realized = normalized(REALIZED)
    census = normalized(CENSUS)
    frequency = normalized(FREQUENCY)
    check("A note is authority-free", "authority: none" in note)
    check("A note disclaims axiom amendment", "does not amend an axiom" in note)
    check("A note disclaims law selection", "does not" in note and "identify the physical law" in note)
    check("A note carries N1-N8", all(f"n{i} —" in note for i in range(1, 9)))
    check("A live state remains records", "a state is a configuration of records" in axioms)
    check("A Admissibility remains non-dynamics", "admissibility is not a dynamics axiom" in axioms)
    check("A realized primitive is pointwise", "pointwise evaluation" in realized)
    check("A realized primitive supplies no state", "does not supply a state, state-selection rule" in realized)
    check("A realized primitive supplies no typicality", "no typical or generic claim" in realized)
    check(
        "A Cycle 42 types the primitive as a pointwise reference form",
        "licenses pointwise evaluation at a supplied law-admissible realized state" in note,
    )
    check(
        "A Cycle 42 separates pointwise state from complete history",
        "pointwise state versus complete history" in note,
    )
    check(
        "A Cycle 42 types complete H as additional contingent data",
        "complete history h additional contingent record-history datum" in note,
    )
    check(
        "A Cycle 42 does not claim that the primitive supplies H",
        "It supplies `H`" not in note_raw and "primitive supplies `H`" not in note_raw,
    )
    check("A final census keeps history contingent", "contingent realized-history data" in census)
    check("A frequency theorem retains component means", "component-mean condition" in frequency)
    check("A no live edit is authorized", "no live edit is authorized" in note)


def pointwise_state_history_boundary() -> None:
    section("P - Pointwise-state versus complete-history boundary")
    s_star = "a"
    l0 = {"a": "b", "b": "b", "c": "a"}
    l1 = {"a": "c", "b": "b", "c": "c"}
    h0 = (s_star, l0[s_star])
    h1 = (s_star, l1[s_star])

    check("P supplied s_* is law-admissible for both rivals", s_star in l0 and s_star in l1)
    check("P one pointwise state is shared", h0[0] == h1[0] == s_star)
    check("P rival next-state answers differ", l0[s_star] != l1[s_star])
    check("P complete two-state histories therefore differ", h0 != h1)
    check("P pointwise state is not a history tuple", not isinstance(s_star, tuple))
    check(
        "P pointwise reference alone contains no transition answer",
        s_star == h0[0] == h1[0] and h0[1] != h1[1],
    )


def deterministic_off_path() -> None:
    section("B - Deterministic off-path separation")
    l0 = {"a": "b", "b": "b", "c": "a"}
    l1 = {"a": "b", "b": "b", "c": "c"}
    history = ("a", "b", "b", "b", "b", "b")

    def generates(law: dict[str, str]) -> bool:
        return all(law[x] == y for x, y in zip(history, history[1:]))

    check("B L0 generates the actual path", generates(l0))
    check("B L1 generates the actual path", generates(l1))
    check("B laws agree on every visited state", all(l0[s] == l1[s] for s in set(history)))
    check("B unvisited state exists", "c" not in history)
    check("B legal preparation at c separates laws", l0["c"] != l1["c"])
    check("B both laws are deterministic one-answer maps", all(v in l0 for v in ("a", "b", "c")) and all(v in l1 for v in ("a", "b", "c")))


def bernoulli_finite_history() -> None:
    section("C - Finite transcript statistical separation")
    transcript = (0, 0, 1, 0, 1, 1, 0)
    ones = sum(transcript)
    zeros = len(transcript) - ones
    parameters = (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3))
    likelihoods = tuple(p**ones * (1 - p) ** zeros for p in parameters)
    check("C transcript has both outcomes", ones > 0 and zeros > 0)
    check("C all candidate likelihoods are positive", all(value > 0 for value in likelihoods))
    check("C candidates predict different next weights", len(set(parameters)) == 3)
    check("C empirical frequency is rational statistic", Fraction(ones, len(transcript)) == Fraction(3, 7))
    check("C empirical frequency selects none of the three exactly", Fraction(ones, len(transcript)) not in parameters)
    check("C finite likelihood does not identify one law", sum(value > 0 for value in likelihoods) == 3)


def causal_intervention_separation() -> None:
    section("D - Observational equality and intervention difference")
    u_values = (0, 1)
    weight = Fraction(1, 2)

    observational_a: dict[tuple[int, int], Fraction] = {}
    observational_b: dict[tuple[int, int], Fraction] = {}
    for u in u_values:
        x_a, y_a = u, u
        x_b, y_b = u, u
        observational_a[(x_a, y_a)] = observational_a.get((x_a, y_a), 0) + weight
        observational_b[(x_b, y_b)] = observational_b.get((x_b, y_b), 0) + weight

    check("D observational laws are identical", observational_a == observational_b)
    check("D observational support is exact diagonal pair", observational_a == {(0, 0): Fraction(1, 2), (1, 1): Fraction(1, 2)})

    # do(X=0): A has Y=X; B retains Y=U.
    do_a = {0: Fraction(1), 1: Fraction(0)}
    do_b = {0: Fraction(1, 2), 1: Fraction(1, 2)}
    check("D intervention laws differ", do_a != do_b)
    check("D Model A intervention is deterministic", do_a[0] == 1)
    check("D Model B intervention remains fair", do_b[0] == do_b[1] == Fraction(1, 2))
    check("D observational equality is weaker than protocol equality", observational_a == observational_b and do_a != do_b)


def positive_markov_reconstruction() -> None:
    section("E - Positive exact finite-class reconstruction")
    kernel = (
        (Fraction(3, 4), Fraction(1, 4)),
        (Fraction(1, 3), Fraction(2, 3)),
    )
    # Exact limiting conditional frequencies are represented directly as row
    # counts in a common denominator. The reconstruction must return K.
    counts = ((3, 1), (1, 2))
    reconstructed = tuple(
        tuple(Fraction(value, sum(row)) for value in row)
        for row in counts
    )
    check("E every kernel row normalizes", all(sum(row) == 1 for row in kernel))
    check("E every conditioning row is represented", all(sum(row) > 0 for row in counts))
    check("E exact conditional rows reconstruct K", reconstructed == kernel)
    check("E distinct row change changes reconstructed law", reconstructed != ((Fraction(1, 2), Fraction(1, 2)), kernel[1]))
    check("E reconstruction assumes a first-order binary class", len(kernel) == 2 and all(len(row) == 2 for row in kernel))


def classification_contract() -> None:
    section("F - Constitutional and no-go classification")
    note = normalized(NOTE)
    required = (
        # Retained only as an explicitly rejected shorthand so the Cycle 41
        # compatibility needle does not misread it as an affirmed boundary.
        "realized-state primitive closes actuality, not law identity",
        "pointwise state reference, not a complete history or law identity",
        "complete history h additional contingent record-history datum",
        "separating reconstruction theorem",
        "complete counterfactual map l",
        "claim-specific condition",
        "no second atom is added",
        "hostile steelman:",
        "outcome:",
        "broad no-go is demoted",
        "pointwise-reference-only",
        "not a claim that empirical or mathematical law reconstruction is impossible",
    )
    for phrase in required:
        check(f"F note contains: {phrase}", phrase in note)
    check("F all N sections remain explicit", all(f"n{i} —" in note for i in range(1, 9)))
    check(
        "F conclusion retains the narrow exact-law residue",
        "neither the pointwise realized-state reference nor an unseparated supplied h replaces the missing exact-law referent" in note,
    )
    check(
        "F complete-H theorem remains a positive route",
        "a separating complete-h theorem remains a live zero-edit route" in note,
    )


def no_go_discipline_contract() -> None:
    section("G - N1-N8 no-go-discipline structure")
    raw = NOTE.read_text(encoding="utf-8")
    parts = {number: markdown_subsection(raw, number) for number in range(1, 9)}
    compact = {number: " ".join(part.split()) for number, part in parts.items()}

    n1_rows = [line.lower() for line in parts[1].splitlines() if line.startswith("|")]
    attempted_rows = [line for line in n1_rows if "| attempted |" in line]
    ruled_out_rows = [line for line in n1_rows if "| ruled out by prior |" in line]
    check("G N1 marks at least five routes ATTEMPTED", len(attempted_rows) >= 5, f"count={len(attempted_rows)}")
    check("G N1 rules out no table route by prior", not ruled_out_rows)
    check("G N1 retains direct axiom derivation open", "direct unique derivation from the four axioms | open" in parts[1])

    for wall in ("w_d", "w_s", "w_p"):
        check(f"G N2 names {wall}", wall in parts[2])
    for pair in (("`w_d`, `w_s`",), ("`w_d`, `w_p`",), ("`w_s`, `w_p`",)):
        check(f"G N2 tests pair {pair[0]}", pair[0] in parts[2])
    check("G N2 states collapsed wall set", "{w_d,w_s,w_p}" in parts[2].replace("`", ""))
    check("G N2 distinguishes temporal completeness", "temporal completeness is not domain, sampling, or protocol completeness" in compact[2])

    for trigger in ("registered", "complete history", "compatible", "same law", "observed", "all experiments", "generic", "learned"):
        check(f"G N3 classifies trigger: {trigger}", trigger in parts[3])
    check("G N3 resolves all hidden conditions", "unresolved hidden conditions: **0**" in parts[3])

    n4_paths = (
        "section 2 / runner b (`:116-130`)",
        "section 3 / runner c (`:133-145`)",
        "section 4 / runner d (`:148-170`)",
        "section 5 / runner e (`:173-190`)",
    )
    for path in n4_paths:
        check(f"G N4 maps evidence: {path}", path in parts[4])
    check("G N4 drops Markov control as negative evidence", "positive closure route; drop as negative evidence" in parts[4].replace("*", ""))
    check("G N4 limits negative support to first three", "only the first three controls support the scoped negative" in parts[4])

    for resolution in (
        "pointwise state `s_*`",
        "one finite history/corpus",
        "infinite single deterministic path",
        "exact observational distribution",
        "separating complete-`h` corpus over all legal protocols",
        "all law space / universal histories",
    ):
        check(f"G N5 scopes resolution: {resolution}", resolution in parts[5])
    check("G N5 leaves high-resolution routes open", parts[5].count("not tested / open") >= 2)
    check("G N5 forbids a universal negative", "no universal nonidentifiability result is licensed" in parts[5])

    check("G N6 has path/status/closure columns", all(term in parts[6] for term in ("| path | status | what it closes |", "approved realized-state primitive", "universal self-testing complete `h`", "direct unique derivation from the axioms")))
    check("G N6 keeps primitive off the wall list", "it closes neither `h` nor law identity" in parts[6])
    check("G N6 forbids a new Record clause", "do not justify a new record clause" in parts[6])

    for phrase in ("hostile steelman:", "outcome:", "broad no-go is demoted", "pointwise-reference-only"):
        check(f"G N7 contains: {phrase}", phrase in parts[7].replace("*", ""))
    check("G N7 says the steelman defeats the broad claim", "steelman defeats the broad claim" in parts[7])

    for filename in (ACTUALITY.name.lower(), FREQUENCY.name.lower(), ADAPTIVE.name.lower()):
        check(f"G N8 cites: {filename}", filename in parts[8])
    check("G N8 maps retired/mechanism/applicability", all(term in parts[8] for term in ("retired?", "mechanism carried forward", "applicable residue here")))
    check("G N8 does not make H primitive content", "none of these prior mechanisms makes a complete `h` part of the realized-state primitive" in compact[8])
    check("G gate passes only narrow claim", "gate result: pass for the narrow pointwise-reference-only claim" in parts[8].replace("*", ""))
    check("G gate records broad demotion", "broad universal nonidentifiability claim is demoted" in parts[8].replace("*", ""))


def main() -> int:
    source_contract()
    pointwise_state_history_boundary()
    deterministic_off_path()
    bernoulli_finite_history()
    causal_intervention_separation()
    positive_markov_reconstruction()
    classification_contract()
    no_go_discipline_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: a pointwise state reference is neither complete H nor an exact law; a separating complete-H theorem remains open")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
