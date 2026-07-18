#!/usr/bin/env python3
"""Cycle 58 operational binary macrocode compiler.

The exact Cycle-43/47 H0/H1 seed pair is used as the binary alphabet for a
six-site macrocode.  A finite seed-relative harness copies one six-bit program
word into an append-only DATA spine while a second append-only certificate
spine follows it.  VALID can form only after both spines are complete, and a
spatial READY/launch port can form only after VALID.  The combined exact-NN
table is tested on all 64 words, every reachable partial interleaving, all 24
proper-cubic rotations, and adversarial partial DATA subsets.

This is a bounded candidate-law object.  It does not construct the harness
from the official seed or compile the Cycle-52 logical rule table.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from itertools import product
from pathlib import Path

import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "OPERATIONAL_BINARY_MACROCODE_COMPILER_CYCLE58_NOTE_2026-07-14.md"
CYCLE41 = REVIEW / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md"
CYCLE52 = REVIEW / "SELF_EXTENDING_FRAME_CAGE_RAIL_CYCLE52_NOTE_2026-07-14.md"
CYCLE56 = REVIEW / "FIRST_ROLE_DIFFERENTIATION_CYCLE56_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Word = tuple[int, int, int, int, int, int]
Signature = c53.Signature
StateKey = tuple[tuple[Coord, str], ...]

H0 = "H0"
H1 = "H1"
BIT_CONTENT = (H0, H1)
MACRO_ORIGIN: Coord = (12, -5, 5)
COVARIANCE_SHIFT: Coord = (31, -23, 13)

# The seed frame calls these directions d, e, and u.  No coordinate congruence
# class is used by the rules; this is the natural presentation only.
DATA_LOCAL: tuple[Coord, ...] = tuple((index, 0, 0) for index in range(6))
CERT_LOCAL: tuple[Coord, ...] = tuple((index, 1, 0) for index in range(6))
VALID_LOCAL: Coord = (5, 2, 0)
READY_LOCAL: Coord = (5, 3, 0)
START_DATA_LOCAL: Coord = (-1, 0, 0)
START_CERT_LOCAL: Coord = (-1, 1, 0)

CONTROL_LABELS: tuple[str, ...] = (
    "BACKSTOP",
    "Z0",
    "H0",
    "H1",
    "AUX",
    "JOINT",
    "RING",
    "JOIN",
    "COMPLETE",
    "P0",
    "P1",
    "ARM",
    "START",
    "VALID",
)


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


def state_key(records: dict[Coord, str]) -> StateKey:
    return tuple(sorted(records.items()))


def translate(position: Coord, shift: Coord) -> Coord:
    return c53.add(position, shift)


def translated_records(records: dict[Coord, str], shift: Coord) -> dict[Coord, str]:
    return {translate(position, shift): content for position, content in records.items()}


def translated_map(records: dict[Coord, str]) -> dict[Coord, str]:
    return translated_records(records, MACRO_ORIGIN)


def two_bits(value: int) -> tuple[int, int]:
    assert 0 <= value < 4
    return ((value >> 1) & 1, value & 1)


def rail_codebook() -> dict[str, Word]:
    answer: dict[str, Word] = {}
    for phase_index, phase in enumerate(("A", "B", "C", "D")):
        for y in range(4):
            for z in range(3):
                word = two_bits(phase_index) + two_bits(y) + two_bits(z)
                answer[c52.role(phase, (y, z))] = word  # type: ignore[assignment]
    return answer


def control_codebook() -> dict[str, Word]:
    answer: dict[str, Word] = {}
    for index, label in enumerate(CONTROL_LABELS):
        prefix = two_bits(index >> 2) + two_bits(index & 3)
        answer[label] = prefix + (1, 1)  # type: ignore[assignment]
    return answer


LABEL_TO_WORD = rail_codebook() | control_codebook()
USED_WORD_TO_LABEL = {word: label for label, word in LABEL_TO_WORD.items()}
ALL_WORDS: tuple[Word, ...] = tuple(product((0, 1), repeat=6))  # type: ignore[assignment]
RESERVED_WORDS: tuple[Word, ...] = tuple(
    word for word in ALL_WORDS if word not in USED_WORD_TO_LABEL
)
WORD_TO_LABEL = dict(USED_WORD_TO_LABEL)
for _index, _word in enumerate(RESERVED_WORDS):
    WORD_TO_LABEL[_word] = f"RESERVED_{_index}"


def local_harness(word: Word) -> dict[Coord, str]:
    """Thirty supplied H0/H1 records surrounding an open DATA/CERT tunnel."""

    records: dict[Coord, str] = {
        START_DATA_LOCAL: H1,
        START_CERT_LOCAL: H1,
    }
    for index, bit in enumerate(word):
        # DATA[index] sees a lower marker, its variable program bit, a fixed H1
        # reference opposite that bit, and the preceding DATA record.  Its
        # successor and certificate site stay open.
        records[(index, -1, 0)] = H0
        records[(index, 0, -1)] = BIT_CONTENT[bit]
        records[(index, 0, 1)] = H1
        # CERT[index] sees this marker, DATA[index], and preceding CERT.
        records[(index, 1, 1)] = H0

    # Three-neighbour signatures distinguish the post-certificate VALID and
    # READY sites.  The overlaps that remain all demand the same H1 output.
    records[(6, 2, 0)] = H0
    records[(5, 2, 1)] = H1
    records[(6, 3, 0)] = H1
    records[(5, 3, 1)] = H0
    return records


def local_additions(word: Word) -> dict[Coord, str]:
    records = {
        DATA_LOCAL[index]: BIT_CONTENT[bit]
        for index, bit in enumerate(word)
    }
    records.update({position: H1 for position in CERT_LOCAL})
    records[VALID_LOCAL] = H1
    records[READY_LOCAL] = H1
    return records


def source_records(word: Word) -> dict[Coord, str]:
    official = c53.seed_records()
    macro = translated_map(local_harness(word))
    assert set(official).isdisjoint(macro)
    return official | macro


def allowed_additions(word: Word) -> dict[Coord, str]:
    return translated_map(local_additions(word))


@dataclass(frozen=True)
class Stage:
    data_count: int
    cert_count: int
    valid: bool = False
    ready: bool = False


def local_stage_records(word: Word, stage: Stage) -> dict[Coord, str]:
    records = local_harness(word)
    for index in range(stage.data_count):
        records[DATA_LOCAL[index]] = BIT_CONTENT[word[index]]
    for index in range(stage.cert_count):
        records[CERT_LOCAL[index]] = H1
    if stage.valid:
        records[VALID_LOCAL] = H1
    if stage.ready:
        records[READY_LOCAL] = H1
    return records


def stages() -> tuple[Stage, ...]:
    answer = [
        Stage(data_count, cert_count)
        for data_count in range(7)
        for cert_count in range(data_count + 1)
    ]
    answer.append(Stage(6, 6, valid=True))
    answer.append(Stage(6, 6, valid=True, ready=True))
    return tuple(answer)


STAGES = stages()


def expected_local_writes(word: Word, stage: Stage) -> dict[Coord, str]:
    writes: dict[Coord, str] = {}
    if stage.data_count < 6:
        index = stage.data_count
        writes[DATA_LOCAL[index]] = BIT_CONTENT[word[index]]
    if stage.cert_count < stage.data_count:
        writes[CERT_LOCAL[stage.cert_count]] = H1
    if stage.data_count == stage.cert_count == 6 and not stage.valid:
        writes[VALID_LOCAL] = H1
    if stage.valid and not stage.ready:
        writes[READY_LOCAL] = H1
    return writes


def local_signature(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.local_signature(records, target)


def build_raw_rule_outputs() -> tuple[
    dict[Signature, frozenset[str]],
    dict[Signature, frozenset[str]],
]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    kinds: dict[Signature, set[str]] = defaultdict(set)
    for word in ALL_WORDS:
        for stage in STAGES:
            records = local_stage_records(word, stage)
            for target, output in expected_local_writes(word, stage).items():
                if target in DATA_LOCAL:
                    kind = "DATA"
                elif target in CERT_LOCAL:
                    kind = "CERT"
                elif target == VALID_LOCAL:
                    kind = "VALID"
                else:
                    kind = "READY"
                signature = local_signature(records, target)
                for rotation in c53.ROTATIONS:
                    raw = c53.rotate_signature(signature, rotation)
                    outputs[raw].add(output)
                    kinds[raw].add(kind)
    return (
        {signature: frozenset(values) for signature, values in outputs.items()},
        {signature: frozenset(values) for signature, values in kinds.items()},
    )


RAW_OUTPUTS, RAW_KINDS = build_raw_rule_outputs()
RAW_CONFLICTS = {
    signature: outputs
    for signature, outputs in RAW_OUTPUTS.items()
    if len(outputs) != 1
}
RULE_TABLE = {
    signature: next(iter(outputs))
    for signature, outputs in RAW_OUTPUTS.items()
    if len(outputs) == 1
}


def enabled_outputs(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: RAW_OUTPUTS[signature]
        for target in c53.open_candidates(records)
        if (signature := local_signature(records, target)) in RAW_OUTPUTS
    }


def enabled_assignments(records: dict[Coord, str]) -> dict[Coord, str]:
    return {
        target: next(iter(outputs))
        for target, outputs in enabled_outputs(records).items()
        if len(outputs) == 1
    }


def full_stage_records(word: Word, stage: Stage) -> dict[Coord, str]:
    return c53.seed_records() | translated_map(local_stage_records(word, stage))


def full_expected_writes(word: Word, stage: Stage) -> dict[Coord, str]:
    return translated_map(expected_local_writes(word, stage))


def decode(records: dict[Coord, str]) -> str | None:
    valid = translate(VALID_LOCAL, MACRO_ORIGIN)
    if valid not in records:
        return None
    contents = tuple(
        records.get(translate(position, MACRO_ORIGIN))
        for position in DATA_LOCAL
    )
    if any(content not in BIT_CONTENT for content in contents):
        return None
    word: Word = tuple(1 if content == H1 else 0 for content in contents)  # type: ignore[assignment]
    return WORD_TO_LABEL[word]


@dataclass(frozen=True)
class Graph:
    states: frozenset[StateKey]
    edges: int
    terminals: frozenset[StateKey]
    parasite_states: frozenset[StateKey]
    output_conflicts: int
    overwrite_attempts: int
    maximum_enabled: int


def exhaustive_graph(seed: dict[Coord, str], allowed: dict[Coord, str]) -> Graph:
    initial = state_key(seed)
    queue = deque((initial,))
    seen = {initial}
    terminals: set[StateKey] = set()
    parasites: set[StateKey] = set()
    edges = 0
    conflicts = 0
    overwrites = 0
    maximum_enabled = 0
    while queue:
        encoded = queue.popleft()
        records = dict(encoded)
        outputs = enabled_outputs(records)
        conflicts += sum(len(values) != 1 for values in outputs.values())
        writes = {
            target: next(iter(values))
            for target, values in outputs.items()
            if len(values) == 1
        }
        maximum_enabled = max(maximum_enabled, len(writes))
        if not writes:
            terminals.add(encoded)
        for target, output in sorted(writes.items()):
            if target in records:
                overwrites += 1
                continue
            future = dict(records)
            future[target] = output
            future_key = state_key(future)
            edges += 1
            if allowed.get(target) != output:
                parasites.add(future_key)
            if future_key not in seen:
                seen.add(future_key)
                queue.append(future_key)
    return Graph(
        frozenset(seen), edges, frozenset(terminals),
        frozenset(parasites), conflicts, overwrites, maximum_enabled,
    )


def canonical_records(records: dict[Coord, str]) -> tuple[tuple[Coord, str], ...]:
    minima = tuple(min(position[axis] for position in records) for axis in range(3))
    return tuple(sorted(
        (
            tuple(position[axis] - minima[axis] for axis in range(3)),
            content,
        )
        for position, content in records.items()
    ))


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_and_authority_contract() -> None:
    section("A - Authority, live source, and seed-relative binary pair")
    for path in (NOTE, CYCLE41, CYCLE52, CYCLE56, AXIOMS):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    cycle41 = normalized(CYCLE41)
    axioms = normalized(AXIOMS)
    check("A authority is none", "authority: none" in note)
    check("A no foundation or audit edit", "no live foundation or audit edit is authorized" in note)
    check("A no audit verdict", "no audit verdict" in note)
    check("A no axiom need claim", "no axiom need" in note)
    check("A live law is exact nearest-neighbour", "fixed nearest-neighbor admissibility rule" in axioms)
    check("A live records are permanent", "records are permanent" in axioms)
    check("A Cycle-41 exact dictionary names H1/H0", "h1/h0" in cycle41 and "+/- (0,1,0)" in cycle41)
    official = c53.seed_records()
    check("A official source is exactly seven records", len(official) == 7)
    check("A official source contains both H0 and H1", {H0, H1} <= set(official.values()))
    check("A macro harness uses only the seed-relative pair", all(
        set(local_harness(word).values()) <= {H0, H1} for word in ALL_WORDS
    ))
    check("A every local harness has exactly thirty records", all(
        len(local_harness(word)) == 30 for word in ALL_WORDS
    ))
    check("A official seed and translated harness are disjoint", all(
        set(c53.seed_records()).isdisjoint(translated_map(local_harness(word)))
        for word in ALL_WORDS
    ))
    h1_bloch = (0, 1, 0)
    h0_bloch = tuple(-component for component in h1_bloch)
    overlap = (1 + sum(left * right for left, right in zip(h1_bloch, h0_bloch))) / 2
    check(
        "A H1/H0 Bloch projectors are exactly orthogonal complements",
        h0_bloch == (0, -1, 0) and overlap == 0,
    )


def codebook_contract() -> None:
    section("B - Six-bit role/control codebook and exact capacity")
    rails = rail_codebook()
    controls = control_codebook()
    check("B Cycle-52 role inventory has exactly 48 entries", len(rails) == 48)
    check("B four launch roles are included in the 48", {
        "LAUNCH_A", "LAUNCH_B", "LAUNCH_C", "LAUNCH_D"
    } <= set(rails))
    check("B every rail code avoids reserved z=11 band", all(word[-2:] != (1, 1) for word in rails.values()))
    check("B every control code occupies reserved z=11 band", all(word[-2:] == (1, 1) for word in controls.values()))
    check("B codebook has 62 distinct named words", len(LABEL_TO_WORD) == len(set(LABEL_TO_WORD.values())) == 62)
    check("B exact capacity leaves two words reserved", len(RESERVED_WORDS) == 2)
    check("B all 64 words decode after VALID", len(WORD_TO_LABEL) == 64)
    check("B five bits are insufficient for 49 Cycle-52 labels", 2 ** 5 < 49 <= 2 ** 6)
    check("B A_2_1 has structural code 001001", rails["A_2_1"] == (0, 0, 1, 0, 0, 1))
    check("B A_1_2 has structural code 000110", rails["A_1_2"] == (0, 0, 0, 1, 1, 0))
    check("B Cycle-55 pair has Hamming distance four", sum(
        left != right for left, right in zip(rails["A_2_1"], rails["A_1_2"])
    ) == 4)


def geometry_and_rule_contract() -> None:
    section("C - Strict radius-one geometry and mixed raw table")
    check("C Gamma6 is exactly six ordered DATA sites", len(DATA_LOCAL) == len(set(DATA_LOCAL)) == 6)
    check("C Gamma6 is one connected nearest-neighbour spine", all(
        c53.subtract(DATA_LOCAL[index + 1], DATA_LOCAL[index]) in c53.DIRECTIONS
        for index in range(5)
    ))
    check("C DATA and CERT spines are pairwise disjoint", set(DATA_LOCAL).isdisjoint(CERT_LOCAL))
    check("C every DATA site is adjacent to its CERT site", all(
        c53.subtract(CERT_LOCAL[index], DATA_LOCAL[index]) in c53.DIRECTIONS
        for index in range(6)
    ))
    check("C all rule offsets have exact lattice radius one", all(
        offset in c53.DIRECTIONS
        for signature in RAW_OUTPUTS
        for offset, _content in signature
    ))
    check("C every exact input has only three or four recorded neighbours", {
        len(signature) for signature in RAW_OUTPUTS
    } == {3, 4})
    check("C combined 64-word table has exactly 132 raw signatures", len(RAW_OUTPUTS) == 132, str(len(RAW_OUTPUTS)))
    check("C every rotated raw signature is output-single-valued", not RAW_CONFLICTS)
    check("C every newly written content is H0 or H1", set().union(*RAW_OUTPUTS.values()) == {H0, H1})
    check("C cross-stage signature overlaps agree on H1", all(
        RAW_OUTPUTS[signature] == frozenset((H1,))
        for signature, kinds in RAW_KINDS.items()
        if len(kinds) > 1
    ))
    check("C no exact raw input collides with extensional Cycle-52 table", not (set(RAW_OUTPUTS) & set(c52.RULE_OUTPUTS)))
    check("C macro table is quiet on official seven-record seed", enabled_assignments(c53.seed_records()) == {})
    check("C full harness has trivial proper-cubic stabilizer for every word", all(
        sum(
            canonical_records({
                c53.matvec(rotation, position): content
                for position, content in local_harness(word).items()
            }) == canonical_records(local_harness(word))
            for rotation in c53.ROTATIONS
        ) == 1
        for word in ALL_WORDS
    ))

    mismatches = []
    maximum_enabled = 0
    for word in ALL_WORDS:
        for stage in STAGES:
            records = full_stage_records(word, stage)
            actual = enabled_assignments(records)
            expected = full_expected_writes(word, stage)
            maximum_enabled = max(maximum_enabled, len(actual))
            if actual != expected:
                mismatches.append((word, stage, actual, expected))
    check("C every one of 1920 intended partial states has exact frontier", not mismatches, str(mismatches[:1]))
    check("C no partial state exposes more than DATA+CERT", maximum_enabled == 2)


def natural_graph_and_partial_inertness() -> None:
    section("D - All 64 complete asynchronous graphs and partial-word controls")
    graph_failures = []
    state_failures = []
    total_states = 0
    total_edges = 0
    for word in ALL_WORDS:
        source = source_records(word)
        allowed = allowed_additions(word)
        graph = exhaustive_graph(source, allowed)
        expected_states = frozenset(
            state_key(full_stage_records(word, stage)) for stage in STAGES
        )
        terminal = dict(next(iter(graph.terminals))) if len(graph.terminals) == 1 else {}
        terminal_additions = {
            position: content for position, content in terminal.items()
            if position not in source
        }
        census = (
            len(graph.states), graph.edges, len(graph.terminals),
            len(graph.parasite_states), graph.output_conflicts,
            graph.overwrite_attempts, graph.maximum_enabled,
        )
        if census != (30, 44, 1, 0, 0, 0, 2):
            graph_failures.append((word, census))
        if graph.states != expected_states or terminal_additions != allowed:
            graph_failures.append((word, "state/terminal mismatch"))
        total_states += len(graph.states)
        total_edges += graph.edges

        for encoded in graph.states:
            records = dict(encoded)
            data_present = [
                translate(position, MACRO_ORIGIN) in records
                for position in DATA_LOCAL
            ]
            cert_present = [
                translate(position, MACRO_ORIGIN) in records
                for position in CERT_LOCAL
            ]
            valid_present = translate(VALID_LOCAL, MACRO_ORIGIN) in records
            ready_present = translate(READY_LOCAL, MACRO_ORIGIN) in records
            if data_present != sorted(data_present, reverse=True):
                state_failures.append((word, "non-prefix DATA"))
            if cert_present != sorted(cert_present, reverse=True):
                state_failures.append((word, "non-prefix CERT"))
            if sum(cert_present) > sum(data_present):
                state_failures.append((word, "CERT outran DATA"))
            if valid_present and not (all(data_present) and all(cert_present)):
                state_failures.append((word, "early VALID"))
            if ready_present and not valid_present:
                state_failures.append((word, "early READY"))
            decoded = decode(records)
            if (decoded is not None) != valid_present:
                state_failures.append((word, "decoder/VALID mismatch"))
            if decoded is not None and decoded != WORD_TO_LABEL[word]:
                state_failures.append((word, "wrong decode"))

    check("D every word graph is exactly 30 states and 44 edges", not graph_failures, str(graph_failures[:1]))
    check("D aggregate natural census is 1920 states and 2816 edges", (total_states, total_edges) == (1920, 2816))
    check("D every reachable partial schedule is DATA/CERT prefix-safe", not state_failures, str(state_failures[:1]))

    direct_partial_failures = []
    for word in ALL_WORDS:
        base = source_records(word)
        for mask in range(64):
            records = dict(base)
            for index in range(6):
                if mask & (1 << index):
                    records[translate(DATA_LOCAL[index], MACRO_ORIGIN)] = BIT_CONTENT[word[index]]
            enabled = enabled_assignments(records)
            if translate(VALID_LOCAL, MACRO_ORIGIN) in enabled:
                direct_partial_failures.append((word, mask, "VALID"))
            if translate(READY_LOCAL, MACRO_ORIGIN) in enabled:
                direct_partial_failures.append((word, mask, "READY"))
            if decode(records) is not None:
                direct_partial_failures.append((word, mask, "DECODE"))
    check("D all 4096 arbitrary DATA subsets have no direct VALID/READY/decode", not direct_partial_failures, str(direct_partial_failures[:1]))


def covariance_contract() -> None:
    section("E - All 24 proper-cubic images of all 64 word graphs")
    failures = []
    total_instances = 0
    total_states = 0
    total_edges = 0
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for word in ALL_WORDS:
            source = c53.transform_records(source_records(word), rotation, COVARIANCE_SHIFT)
            allowed = c53.transform_records(allowed_additions(word), rotation, COVARIANCE_SHIFT)
            graph = exhaustive_graph(source, allowed)
            expected_states = frozenset(
                state_key(c53.transform_records(
                    full_stage_records(word, stage), rotation, COVARIANCE_SHIFT
                ))
                for stage in STAGES
            )
            census = (
                len(graph.states), graph.edges, len(graph.terminals),
                len(graph.parasite_states), graph.output_conflicts,
                graph.overwrite_attempts, graph.maximum_enabled,
            )
            terminal = dict(next(iter(graph.terminals))) if len(graph.terminals) == 1 else {}
            terminal_additions = {
                position: content for position, content in terminal.items()
                if position not in source
            }
            if census != (30, 44, 1, 0, 0, 0, 2):
                failures.append((rotation_index, word, census))
            if graph.states != expected_states or terminal_additions != allowed:
                failures.append((rotation_index, word, "state/terminal mismatch"))
            total_instances += 1
            total_states += len(graph.states)
            total_edges += graph.edges
    check("E all 1536 rotated word graphs are exact isomorphisms", not failures, str(failures[:1]))
    check("E rotated aggregate has 46080 states and 67584 edges", (
        total_instances, total_states, total_edges
    ) == (1536, 46080, 67584))


def documentation_gate() -> None:
    section("F - Exact scope, operational residuals, and constitutional boundary")
    note = normalized(NOTE)
    phrases = (
        "binary_data_valid_handshake",
        "seed_to_binary_harness",
        "validated_word_to_exact_nn_rule_match",
        "30 reachable states",
        "44 directed edges",
        "all 64 words",
        "all 24 proper-cubic rotations",
        "no live foundation or audit edit is authorized",
        "no audit verdict",
        "no axiom need",
        "formation occurrence",
        "scalar readout",
    )
    for phrase in phrases:
        check(f"F note contains: {phrase}", phrase in note)
    check("F exact runner count replaces placeholder", "pass_count_placeholder" not in note)


def main() -> int:
    source_and_authority_contract()
    codebook_contract()
    geometry_and_rule_contract()
    natural_graph_and_partial_inertness()
    covariance_contract()
    documentation_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: BINARY_DATA_VALID_HANDSHAKE is positive; "
        "SEED_TO_BINARY_HARNESS and VALIDATED_WORD_TO_EXACT_NN_RULE_MATCH remain"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
