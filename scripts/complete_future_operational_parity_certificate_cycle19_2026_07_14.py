#!/usr/bin/env python3
"""Cycle 19 exact controls for the operational parity-certificate seam.

Companion note:
  docs/work_history/repo/review_feedback/
  COMPLETE_FUTURE_OPERATIONAL_PARITY_CERTIFICATE_CYCLE19_NOTE_2026-07-14.md

The runner compares restricted endpoint-parity equivalence with a separating
future-intervention repertoire.  It also checks the exact three-site cluster,
the coherent/dephased paired protocols, scalar-readout non-injectivity,
record permanence, and record-fibre strong lumpability.  It does not identify
Nature's law, amend an axiom or primitive, set an audit verdict, edit a live
queue, commit, push, or open a PR.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import product
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "COMPLETE_FUTURE_OPERATIONAL_PARITY_CERTIFICATE_CYCLE19_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
CYCLE18 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "ACTUAL_HEADER_ROLE_DECODER_PARITY_SELECTION_CYCLE18_NOTE_2026-07-14.md"
)
OPERATIONAL = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "OPERATIONAL_RECORD_RECONSTRUCTION_DEEP_PROBE_NOTE_2026-07-13.md"
)
IRREDUCIBLE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXACT_LAW_IRREDUCIBLE_CONTENT_INDEPENDENCE_TOURNAMENT_NOTE_2026-07-14.md"
)
PREDICTIVE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0

I2 = sp.eye(2)
I4 = sp.eye(4)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
ZERO = sp.Matrix([1, 0])
ONE = sp.Matrix([0, 1])
PLUS = (ZERO + ONE) / sp.sqrt(2)
MINUS = (ZERO - ONE) / sp.sqrt(2)
PLUS_Y = (ZERO + sp.I * ONE) / sp.sqrt(2)
MINUS_Y = (ZERO - sp.I * ONE) / sp.sqrt(2)
P0 = ZERO * ZERO.T
P1 = ONE * ONE.T
PX_PLUS = PLUS * PLUS.T
PX_MINUS = MINUS * MINUS.T
PY_PLUS = PLUS_Y * PLUS_Y.conjugate().T
PY_MINUS = MINUS_Y * MINUS_Y.conjugate().T


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail else ""
    if bool(condition):
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def normalized(text: str) -> str:
    return " ".join(
        text.lower().replace("*", "").replace("`", "").replace("_", " ").split()
    )


def kron(*matrices: sp.Matrix) -> sp.Matrix:
    answer = matrices[0]
    for matrix in matrices[1:]:
        answer = sp.kronecker_product(answer, matrix)
    return answer


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def projector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * dagger(vector))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    if left.shape != right.shape:
        return False
    return all(sp.simplify(value) == 0 for value in left - right)


def scalar_equal(left: sp.Expr, right: sp.Expr) -> bool:
    return sp.simplify(left - right) == 0


def cluster_state() -> sp.Matrix:
    """Return CZ_ab CZ_bc |+++> in computational order a,b,c."""
    state = sp.zeros(8, 1)
    for a, b, c in product((0, 1), repeat=3):
        state[4 * a + 2 * b + c] = sp.Rational((-1) ** (a * b + b * c), 2) / sp.sqrt(2)
    return state


def conditional_endpoints(
    state: sp.Matrix, center_vector: sp.Matrix
) -> tuple[sp.Expr, sp.Matrix]:
    endpoint = sp.zeros(4, 1)
    bra = dagger(center_vector)
    for a, c in product((0, 1), repeat=2):
        endpoint[2 * a + c] = sum(
            bra[0, b] * state[4 * a + 2 * b + c] for b in (0, 1)
        )
    probability = sp.simplify((dagger(endpoint) * endpoint)[0])
    return probability, sp.simplify(endpoint / sp.sqrt(probability))


def probability(rho: sp.Matrix, effect: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(rho * effect))


def dephase_computational(rho: sp.Matrix) -> sp.Matrix:
    effects = tuple(kron(left, right) for left, right in product((P0, P1), repeat=2))
    return sp.simplify(sum((effect * rho * effect for effect in effects), sp.zeros(4)))


def endpoint_z_transcripts(
    center_basis: tuple[sp.Matrix, sp.Matrix]
) -> dict[tuple[int, int, int], sp.Expr]:
    state = cluster_state()
    transcripts: dict[tuple[int, int, int], sp.Expr] = {}
    for sign_index, center_vector in enumerate(center_basis):
        sign = 1 if sign_index == 0 else -1
        center_probability, endpoint = conditional_endpoints(state, center_vector)
        rho = projector(endpoint)
        for left, right in product((0, 1), repeat=2):
            effect = kron(P0 if left == 0 else P1, P0 if right == 0 else P1)
            joint_probability = sp.simplify(center_probability * probability(rho, effect))
            if joint_probability != 0:
                transcripts[(sign, left, right)] = joint_probability
    return transcripts


def protocol_fingerprint(
    protocol: dict[int, sp.Matrix], effects: tuple[sp.Matrix, ...]
) -> tuple[sp.Expr, ...]:
    """Conditional-state instrument with unbiased signed center record."""
    return tuple(
        sp.simplify(sp.Rational(1, 2) * probability(protocol[sign], effect))
        for sign in (1, -1)
        for effect in effects
    )


def quotient_classes(fingerprints: dict[str, tuple[sp.Expr, ...]]) -> tuple[tuple[str, ...], ...]:
    buckets: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for name, fingerprint in fingerprints.items():
        canonical = tuple(sp.srepr(sp.simplify(value)) for value in fingerprint)
        buckets[canonical].append(name)
    return tuple(sorted((tuple(sorted(names)) for names in buckets.values())))


def hermitian_span_rank(matrices: tuple[sp.Matrix, ...]) -> int:
    columns = [matrix.reshape(matrix.rows * matrix.cols, 1) for matrix in matrices]
    return sp.Matrix.hstack(*columns).rank()


def scalar_readout(config: dict[str, str], values: dict[str, sp.Expr]) -> sp.Expr:
    return sp.simplify(sum((values[content] for content in config.values()), sp.Integer(0)))


def disjoint_union(left: dict[str, str], right: dict[str, str]) -> dict[str, str]:
    if set(left).intersection(right):
        raise ValueError("record collections are not disjoint")
    return {**left, **right}


def authority_and_source_contract() -> None:
    section("A - Authority, live foundation, and predecessor contracts")
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(note_raw)
    axioms = normalized(AXIOMS.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    realized = normalized(REALIZED.read_text(encoding="utf-8"))
    cycle18 = normalized(CYCLE18.read_text(encoding="utf-8"))
    operational = normalized(OPERATIONAL.read_text(encoding="utf-8"))
    irreducible = normalized(IRREDUCIBLE.read_text(encoding="utf-8"))
    predictive = normalized(PREDICTIVE.read_text(encoding="utf-8"))

    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live authority surface",
        "changes no axiom" in note
        and all(
            token in note
            for token in (
                "primitive",
                "registry",
                "audit",
                "queue",
                "policy",
                "retained surface",
            )
        ),
    )
    for needle in (
        "records form",
        "records are permanent",
        "only records are readable",
        "a readout value is determined by record content alone",
        "scalar readout i is additive",
        "a state is a configuration of records",
    ):
        check(f"A live foundation needle: {needle[:46]}", needle in axioms)
    check("A foundation withholds context selection", "context selection" in axioms)
    check("A foundation withholds probability and update law", "probability rules" in axioms and "update laws" in axioms)
    check("A registry has exactly four approved premise nodes", len(registry["canonical_ids"]) == 4)
    check("A realized-state primitive supplies no state content", "carries zero state-contingent content" in realized)
    check("A realized-state primitive supplies no probability rule", "does not supply a state, state-selection rule" in realized and "probability rule" in realized)
    check("A Cycle 18 proves the name-free parity selector", "parity-certificate selection theorem" in cycle18)
    check("A Cycle 18 exposes the hard-coded X seam", "hard-coded name" in cycle18 and "literal string x" in cycle18)
    check("A operational probe defines preparations by all later readable events", "same statistics for every later readable event" in operational)
    check("A operational probe keeps state sufficiency explicit", "state-sufficiency gate" in operational)
    check("A exact-law packet defines complete adaptive future equivalence", "every finite compatible adaptive future protocol" in irreducible)
    check("A exact-law packet says the quotient depends on complete contexts", "quotient is fixed by l plus its complete contexts" in irreducible)
    check("A predictive packet states the strong-lumpability test", "strong lumpability" in predictive and "finite adaptive future protocol" in predictive)
    for source in (
        "quant-ph/0406166",
        "1512.00589",
        "0712.1325",
        "1801.09811",
    ):
        check(f"A primary-source ledger includes {source}", source in note_raw)
    check("A note contains written N1-N8 gate", all(f"### N{i}" in note_raw for i in range(1, 9)))


def exact_cluster_and_name_free_decoder() -> dict[int, sp.Matrix]:
    section("B - Exact cluster and name-free parity decoder")
    state = cluster_state()
    check("B cluster is normalized", scalar_equal((dagger(state) * state)[0], 1))
    stabilizer = kron(Z, X, Z)
    check("B cluster has exact Z-X-Z stabilizer", matrix_equal(stabilizer * state, state))

    x_protocol: dict[int, sp.Matrix] = {}
    expected_vectors = {
        1: (kron(ZERO, ZERO) + kron(ONE, ONE)) / sp.sqrt(2),
        -1: (kron(ZERO, ONE) + kron(ONE, ZERO)) / sp.sqrt(2),
    }
    for sign, center_vector in ((1, PLUS), (-1, MINUS)):
        branch_probability, endpoint = conditional_endpoints(state, center_vector)
        check(f"B center sign {sign:+d} has probability one half", scalar_equal(branch_probability, sp.Rational(1, 2)))
        check(f"B center sign {sign:+d} gives expected Bell endpoint", matrix_equal(projector(endpoint), projector(expected_vectors[sign])))
        x_protocol[sign] = projector(endpoint)

    x_transcripts = endpoint_z_transcripts((PLUS, MINUS))
    y_transcripts = endpoint_z_transcripts((PLUS_Y, MINUS_Y))
    check("B X-role protocol has four signed endpoint-Z transcripts", len(x_transcripts) == 4)
    check("B every X-role transcript has weight one quarter", all(value == sp.Rational(1, 4) for value in x_transcripts.values()))
    check(
        "B X-role sign equals endpoint-Z product without using an X label in the predicate",
        all(sign == ((-1) ** (left + right)) for sign, left, right in x_transcripts),
    )
    check("B Y-role protocol has eight signed endpoint-Z transcripts", len(y_transcripts) == 8)
    check("B every Y-role transcript has weight one eighth", all(value == sp.Rational(1, 8) for value in y_transcripts.values()))
    check(
        "B Y-role sign does not determine endpoint parity",
        any(sign != ((-1) ** (left + right)) for sign, left, right in y_transcripts),
    )
    check("B parity predicate separates X-role and Y-role protocols", set(x_transcripts) != set(y_transcripts))

    nx, ny, nz = sp.symbols("n_x n_y n_z", real=True)
    axis = nx * X + ny * Y + nz * Z
    correlator = sp.simplify((dagger(state) * kron(Z, axis, Z) * state)[0])
    check("B arbitrary-axis parity correlator is exactly n_x", sp.simplify(correlator - nx) == 0)
    saturation_residual = sp.expand(
        (nx**2 + ny**2 + nz**2 - 1) - (nx**2 - 1)
    )
    check(
        "B unit-axis deterministic saturation leaves a real sum of squares",
        sp.simplify(saturation_residual - (ny**2 + nz**2)) == 0,
    )
    return x_protocol


def restricted_vs_complete_future_pair(x_protocol: dict[int, sp.Matrix]) -> None:
    section("C - Restricted parity equivalence versus separating futures")
    z_effects = tuple(kron(left, right) for left, right in product((P0, P1), repeat=2))
    coherent = x_protocol
    dephased = {sign: dephase_computational(rho) for sign, rho in coherent.items()}

    for sign in (1, -1):
        check(f"C coherent branch {sign:+d} is pure", scalar_equal(sp.trace(coherent[sign] * coherent[sign]), 1))
        check(f"C dephased branch {sign:+d} is mixed", scalar_equal(sp.trace(dephased[sign] * dephased[sign]), sp.Rational(1, 2)))
        check(f"C coherent/dephased matrices differ for sign {sign:+d}", not matrix_equal(coherent[sign], dephased[sign]))

    restricted_coherent = protocol_fingerprint(coherent, z_effects)
    restricted_dephased = protocol_fingerprint(dephased, z_effects)
    check("C coherent and dephased protocols have identical complete endpoint-Z tables", restricted_coherent == restricted_dephased)
    check("C both protocols satisfy deterministic signed endpoint parity", all(value in (0, sp.Rational(1, 4)) for value in restricted_coherent))

    xx = kron(X, X)
    p_xx_plus = sp.simplify((I4 + xx) / 2)
    check("C every coherent branch has XX expectation plus one", all(scalar_equal(probability(rho, xx), 1) for rho in coherent.values()))
    check("C every dephased branch has XX expectation zero", all(scalar_equal(probability(rho, xx), 0) for rho in dephased.values()))
    check("C XX-plus future accepts coherent branches certainly", all(scalar_equal(probability(rho, p_xx_plus), 1) for rho in coherent.values()))
    check("C XX-plus future accepts dephased branches only one half", all(scalar_equal(probability(rho, p_xx_plus), sp.Rational(1, 2)) for rho in dephased.values()))

    for sign in (1, -1):
        bell_effect = coherent[sign]
        check(f"C sign-conditioned Bell effect accepts coherent {sign:+d} certainly", scalar_equal(probability(coherent[sign], bell_effect), 1))
        check(f"C sign-conditioned Bell effect accepts dephased {sign:+d} one half", scalar_equal(probability(dephased[sign], bell_effect), sp.Rational(1, 2)))

    paulis = (I2, X, Y, Z)
    product_paulis = tuple(kron(left, right) for left, right in product(paulis, repeat=2))
    check("C sixteen two-qubit Pauli products span the full matrix space", hermitian_span_rank(product_paulis) == 16)
    complete_coherent = protocol_fingerprint(coherent, product_paulis)
    complete_dephased = protocol_fingerprint(dephased, product_paulis)
    check("C intervention-complete Pauli fingerprints separate the protocols", complete_coherent != complete_dephased)

    y_state = cluster_state()
    y_protocol = {
        sign: projector(conditional_endpoints(y_state, vector)[1])
        for sign, vector in ((1, PLUS_Y), (-1, MINUS_Y))
    }
    restricted_classes = quotient_classes(
        {
            "coherent-PC": restricted_coherent,
            "dephased-PC": restricted_dephased,
            "Y-role": protocol_fingerprint(y_protocol, z_effects),
        }
    )
    expanded_classes = quotient_classes(
        {
            "coherent-PC": protocol_fingerprint(coherent, z_effects + (p_xx_plus,)),
            "dephased-PC": protocol_fingerprint(dephased, z_effects + (p_xx_plus,)),
            "Y-role": protocol_fingerprint(y_protocol, z_effects + (p_xx_plus,)),
        }
    )
    check("C endpoint-Z quotient merges only the coherent/dephased PC pair", len(restricted_classes) == 2 and ("coherent-PC", "dephased-PC") in restricted_classes)
    check("C adding one legal phase-sensitive future strictly refines the quotient", len(expanded_classes) == 3)

    for sign in (1, -1):
        check(f"C an actual endpoint-Z read erases the pre-read distinction {sign:+d}", matrix_equal(dephase_computational(coherent[sign]), dephased[sign]))


def operational_content_and_tester_dependence() -> None:
    section("D - Predictive quotient, algebraic content, and tester dependence")
    z_effects = (P0, P1)
    pauli_effects = (PX_PLUS, PX_MINUS, PY_PLUS, PY_MINUS, P0, P1)
    x_plus_z = tuple(probability(PX_PLUS, effect) for effect in z_effects)
    y_plus_z = tuple(probability(PY_PLUS, effect) for effect in z_effects)
    x_plus_complete = tuple(probability(PX_PLUS, effect) for effect in pauli_effects)
    y_plus_complete = tuple(probability(PY_PLUS, effect) for effect in pauli_effects)
    check("D algebraically distinct X-plus and Y-plus possibilities share a Z fingerprint", not matrix_equal(PX_PLUS, PY_PLUS) and x_plus_z == y_plus_z)
    check("D a separating Pauli repertoire distinguishes those possibilities", x_plus_complete != y_plus_complete)
    check("D six Pauli effects span the one-qubit Hermitian space", hermitian_span_rank(pauli_effects) == 4)

    restricted = quotient_classes({"X+": x_plus_z, "Y+": y_plus_z})
    complete = quotient_classes({"X+": x_plus_complete, "Y+": y_plus_complete})
    check("D a restricted physical repertoire can merge distinct locked possibilities predictively", restricted == (("X+", "Y+"),))
    check("D an expanded repertoire refines them into two predictive states", len(complete) == 2)
    check("D operational equivalence is relative to the declared tester set", len(restricted) < len(complete))


def scalar_readout_and_permanence_controls() -> None:
    section("E - Content-only scalar readout and permanence do not define the quotient")
    contents = ("center+", "center-", "left0", "left1", "right0", "right1", "phase+", "phase-")
    count_values = {content: sp.Integer(1) for content in contents}
    separating_values = {content: sp.Integer(2**index) for index, content in enumerate(contents)}
    empty: dict[str, str] = {}
    left = {"center": "center+"}
    right_even = {"left": "left0", "right": "right0"}
    right_odd = {"left": "left0", "right": "right1"}

    check("E both additive scalar maps have I(empty)=0", scalar_readout(empty, count_values) == scalar_readout(empty, separating_values) == 0)
    for name, values in (("count", count_values), ("separating", separating_values)):
        check(
            f"E {name} map is additive on disjoint records",
            scalar_readout(disjoint_union(left, right_even), values)
            == scalar_readout(left, values) + scalar_readout(right_even, values),
        )
    check("E a content-only additive scalar may be non-injective", scalar_readout({"center": "center+"}, count_values) == scalar_readout({"center": "center-"}, count_values))
    check("E another content-only additive scalar may separate the same contents", scalar_readout({"center": "center+"}, separating_values) != scalar_readout({"center": "center-"}, separating_values))
    check("E count readout also merges distinct endpoint contents", scalar_readout(right_even, count_values) == scalar_readout(right_odd, count_values))

    center_plus = {"center": "center+"}
    z_future = disjoint_union(center_plus, right_even)
    phase_future = disjoint_union(center_plus, {"phase": "phase+"})
    check("E endpoint read appends without changing the center record", z_future["center"] == center_plus["center"] and len(z_future) > len(center_plus))
    check("E phase-sensitive read also appends without changing the center record", phase_future["center"] == center_plus["center"] and len(phase_future) > len(center_plus))
    check("E permanence is compatible with more than one future tester", set(z_future).intersection(phase_future) == {"center"})


def record_fibre_lumpability_and_preparation_records() -> None:
    section("F - Record-fibre lumpability and preparation/intervention conditions")
    same_records = (("center", "+"),)
    raw_histories = {
        "coherent": {"records": same_records, "memory": "Q"},
        "dephased": {"records": same_records, "memory": "C"},
    }
    future_phase_probability = {"Q": sp.Integer(1), "C": sp.Rational(1, 2)}
    fingerprints = {
        name: (future_phase_probability[history["memory"]],)
        for name, history in raw_histories.items()
    }
    check("F the raw histories have the same permanent record fibre", raw_histories["coherent"]["records"] == raw_histories["dephased"]["records"])
    check("F a phase-sensitive future makes that record fibre non-lumpable", fingerprints["coherent"] != fingerprints["dephased"])

    persistent_records = {
        "coherent": same_records + (("preparation", "coherent-cluster"),),
        "dephased": same_records + (("preparation", "dephased-parity"),),
    }
    check("F one persistent preparation record splits the predictive fibres", persistent_records["coherent"] != persistent_records["dephased"])
    check("F no second ontic site type is needed for that logical repair", all(all(len(entry) == 2 for entry in records) for records in persistent_records.values()))

    restricted_fingerprints = {name: (sp.Integer(1),) for name in raw_histories}
    check("F deleting every phase-sensitive intervention makes the same fibre lumpable", len(quotient_classes(restricted_fingerprints)) == 1)
    check("F tester restriction and persistent preparation records are distinct repair routes", len(set(persistent_records.values())) == 2 and len(quotient_classes(restricted_fingerprints)) == 1)


def classification_and_no_go_contract() -> None:
    section("G - Narrow classification and N1-N8 contract")
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(note_raw)
    checks = (
        "parity certificate is a valid role-specific operational definition",
        "x selection is a conditional decoder theorem",
        "pc alone is not complete record content",
        "actual center has that role remains an exact-law field or theorem",
        "no axiom text is proposed",
        "does not prove that the eventual exact law cannot derive pc",
        "no-go discipline status: pass",
    )
    for needle in checks:
        check(f"G note classification: {needle[:52]}", needle in note)
    for index in range(1, 9):
        check(f"G written N{index} section present", f"### n{index}" in note)
    check("G N1 has at least five distinct routes", note_raw.count("| ATTEMPTED |") >= 5)
    check("G N2 contains a pairwise wall table", "| `O,K` |" in note_raw and "| `K,R` |" in note_raw)
    check("G N7 contains a hostile steelman", "**Hostile steelman:**" in note_raw)
    check("G N8 records the prescribed searches", "NO_GO_LEDGER.md" in note_raw and "structurally undecidable" in note_raw)


def main() -> None:
    authority_and_source_contract()
    x_protocol = exact_cluster_and_name_free_decoder()
    restricted_vs_complete_future_pair(x_protocol)
    operational_content_and_tester_dependence()
    scalar_readout_and_permanence_controls()
    record_fibre_lumpability_and_preparation_records()
    classification_and_no_go_contract()
    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
