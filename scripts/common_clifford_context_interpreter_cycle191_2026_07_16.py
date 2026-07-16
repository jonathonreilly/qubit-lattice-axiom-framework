#!/usr/bin/env python3
"""Cycle 191: common Clifford interpreter for the Cycle-189 instruments.

The runner synthesizes exact signed-Pauli Clifford basis decoders, compiles
all six Peres--Mermin pointer instruments from one H/CNOT interpreter, and
accounts for program, gate, depth, pointer, phase, and containment costs.

It changes no authority surface and does not claim a microscopic lattice
implementation, a Born-rule derivation, or actuality.
"""

from __future__ import annotations

import hashlib
from collections import Counter, deque
from dataclasses import dataclass
from itertools import product
from pathlib import Path

import sympy as sp

import preterminal_context_quantum_process_cycle189_2026_07_16 as c189


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COMMON_CLIFFORD_CONTEXT_INTERPRETER_CYCLE191_NOTE_2026-07-16.md"
)
CYCLE189 = (
    ROOT
    / "scripts/preterminal_context_quantum_process_cycle189_2026_07_16.py"
)
CYCLE189_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PRETERMINAL_CONTEXT_QUANTUM_PROCESS_CYCLE189_NOTE_2026-07-16.md"
)
FROZEN = {
    CYCLE189: "a06853a529723332c774112d5aad8e53d9a91ad486de70de201cfcb8b501fe34",
    CYCLE189_NOTE: "97c2e98f90cef08063a3589d31555fbe76a18cbbbd3b8fb677c3b03603c54ded",
}

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_zero(matrix: sp.Matrix) -> bool:
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


I2 = c189.I2
X = c189.X
Y = c189.Y
Z = c189.Z
H = c189.H
I4 = c189.I4
I16 = c189.I16
S = sp.diag(1, sp.I)


def cnot_matrix(
    qubit_count: int,
    control: int,
    target: int,
) -> sp.Matrix:
    matrix = sp.zeros(2**qubit_count)
    for index in range(2**qubit_count):
        bits = [
            (index >> (qubit_count - 1 - qubit)) & 1
            for qubit in range(qubit_count)
        ]
        output = list(bits)
        output[target] ^= output[control]
        output_index = 0
        for bit in output:
            output_index = 2 * output_index + bit
        matrix[output_index, index] = 1
    return matrix


TWO_QUBIT_GATES = {
    "H0": c189.tensor(H, I2),
    "H1": c189.tensor(I2, H),
    "S0": c189.tensor(S, I2),
    "S1": c189.tensor(I2, S),
    "CX01": cnot_matrix(2, 0, 1),
    "CX10": cnot_matrix(2, 1, 0),
}
FULL_ALPHABET = ("H0", "H1", "S0", "S1", "CX01", "CX10")
REAL_ALPHABET = ("H0", "H1", "CX01", "CX10")

PAULI_WORDS = tuple(
    left + right
    for left, right in product(("I", "X", "Y", "Z"), repeat=2)
    if left + right != "II"
)
PAULI_MATRICES = {
    word: c189.tensor(
        c189.PAULI_ONE[word[0]],
        c189.PAULI_ONE[word[1]],
    )
    for word in PAULI_WORDS
}
WORD_INDEX = {
    word: index + 1
    for index, word in enumerate(PAULI_WORDS)
}


def encode_signed(sign: int, word: str) -> int:
    return sign * WORD_INDEX[word]


def decode_signed(code: int) -> tuple[int, str]:
    return (
        1 if code > 0 else -1,
        PAULI_WORDS[abs(code) - 1],
    )


def gate_conjugation_tables() -> dict[str, dict[str, tuple[int, str]]]:
    tables = {}
    for gate_name, gate in TWO_QUBIT_GATES.items():
        table = {}
        for word, matrix in PAULI_MATRICES.items():
            moved = sp.simplify(gate * matrix * gate.H)
            matches = []
            for candidate, candidate_matrix in PAULI_MATRICES.items():
                if exact_zero(moved - candidate_matrix):
                    matches.append((1, candidate))
                if exact_zero(moved + candidate_matrix):
                    matches.append((-1, candidate))
            if len(matches) != 1:
                raise ValueError(
                    ("non-Pauli-conjugation", gate_name, word, matches)
                )
            table[word] = matches[0]
        tables[gate_name] = table
    return tables


CONJUGATION = gate_conjugation_tables()
IDENTITY_ACTION = tuple(WORD_INDEX[word] for word in PAULI_WORDS)


def act_gate(
    action: tuple[int, ...],
    gate_name: str,
) -> tuple[int, ...]:
    moved = []
    for code in action:
        sign, word = decode_signed(code)
        gate_sign, gate_word = CONJUGATION[gate_name][word]
        moved.append(encode_signed(sign * gate_sign, gate_word))
    return tuple(moved)


def action_image(
    action: tuple[int, ...],
    word: str,
) -> tuple[int, str]:
    return decode_signed(action[PAULI_WORDS.index(word)])


@dataclass(frozen=True)
class SearchResult:
    state_count: int
    maximum_depth: int
    depth_histogram: Counter[int]
    programs: dict[str, tuple[str, ...]]
    depths: dict[str, int]


CONTEXT_GENERATORS = {
    context.label: context.observables[:2]
    for context in c189.CONTEXTS
}


def target_labels(action: tuple[int, ...]) -> tuple[str, ...]:
    return tuple(
        label
        for label, (first, second) in CONTEXT_GENERATORS.items()
        if action_image(action, first) == (1, "ZI")
        and action_image(action, second) == (1, "IZ")
    )


def clifford_search(alphabet: tuple[str, ...]) -> SearchResult:
    parent: dict[
        tuple[int, ...],
        tuple[tuple[int, ...] | None, str | None],
    ] = {IDENTITY_ACTION: (None, None)}
    depth = {IDENTITY_ACTION: 0}
    queue = deque((IDENTITY_ACTION,))
    target_states: dict[str, tuple[int, ...]] = {}
    histogram: Counter[int] = Counter((0,))

    while queue:
        action = queue.popleft()
        for label in target_labels(action):
            target_states.setdefault(label, action)
        for gate_name in alphabet:
            moved = act_gate(action, gate_name)
            if moved in parent:
                continue
            parent[moved] = (action, gate_name)
            depth[moved] = depth[action] + 1
            histogram[depth[moved]] += 1
            queue.append(moved)

    programs = {}
    depths = {}
    for label, state in target_states.items():
        reversed_program = []
        cursor = state
        while parent[cursor][0] is not None:
            previous, gate_name = parent[cursor]
            if previous is None or gate_name is None:
                raise ValueError(("broken-parent", label))
            reversed_program.append(gate_name)
            cursor = previous
        programs[label] = tuple(reversed(reversed_program))
        depths[label] = depth[state]

    return SearchResult(
        state_count=len(parent),
        maximum_depth=max(depth.values()),
        depth_histogram=histogram,
        programs=programs,
        depths=depths,
    )


EXPECTED_PROGRAMS = {
    "R1": (),
    "R2": ("H0", "CX10", "CX01", "H0"),
    "R3": ("H0", "CX01", "H0"),
    "C1": ("H1",),
    "C2": ("CX01", "CX10", "H1"),
    "C3": ("CX10", "H1"),
}


def circuit_matrix(program: tuple[str, ...]) -> sp.Matrix:
    matrix = I4
    for gate_name in program:
        matrix = sp.simplify(TWO_QUBIT_GATES[gate_name] * matrix)
    return matrix


def four_qubit_lift(system_unitary: sp.Matrix) -> sp.Matrix:
    return c189.tensor(system_unitary, sp.eye(4))


COPY_02 = cnot_matrix(4, 0, 2)
COPY_13 = cnot_matrix(4, 1, 3)
COMMON_POINTER_COPY = sp.simplify(COPY_02 * COPY_13)


def interpreted_context_unitary(
    program: tuple[str, ...],
) -> sp.Matrix:
    decoder = circuit_matrix(program)
    return sp.simplify(
        four_qubit_lift(decoder.H)
        * COMMON_POINTER_COPY
        * four_qubit_lift(decoder)
    )


CONTEXT_CODES = {
    "R1": (0, 0, 0),
    "R2": (0, 0, 1),
    "R3": (0, 1, 0),
    "C1": (0, 1, 1),
    "C2": (1, 0, 0),
    "C3": (1, 0, 1),
    "OMIT": (1, 1, 0),
    "INVALID": (1, 1, 1),
}
CODE_TO_LABEL = {
    code: label
    for label, code in CONTEXT_CODES.items()
}


def interpret_context_code(
    code: tuple[int, int, int],
) -> sp.Matrix:
    label = CODE_TO_LABEL[code]
    if label == "OMIT":
        return I16
    if label == "INVALID":
        raise ValueError(("invalid-context-program", code))
    return interpreted_context_unitary(EXPECTED_PROGRAMS[label])


PREPARATION_PROGRAMS = {
    "prep:Z0Z0": (),
    "prep:X+X+": ("H0", "H1"),
}
PREPARATION_CODES = {
    "prep:Z0Z0": (0,),
    "prep:X+X+": (1,),
}


GATE_SUPPORT_2 = {
    "H0": frozenset((0,)),
    "H1": frozenset((1,)),
    "S0": frozenset((0,)),
    "S1": frozenset((1,)),
    "CX01": frozenset((0, 1)),
    "CX10": frozenset((0, 1)),
}


def scheduled_depth(
    program: tuple[str, ...],
    supports: dict[str, frozenset[int]],
) -> int:
    last_layer: dict[int, int] = {}
    maximum = 0
    for gate_name in program:
        support = supports[gate_name]
        layer = 1 + max(
            (last_layer.get(qubit, 0) for qubit in support),
            default=0,
        )
        for qubit in support:
            last_layer[qubit] = layer
        maximum = max(maximum, layer)
    return maximum


GATE_SUPPORT_4 = {
    **GATE_SUPPORT_2,
    "COPY02": frozenset((0, 2)),
    "COPY13": frozenset((1, 3)),
}


def instrument_instruction_tape(
    decoder_program: tuple[str, ...],
) -> tuple[str, ...]:
    return (
        decoder_program
        + ("COPY02", "COPY13")
        + tuple(reversed(decoder_program))
    )


def third_observable_sign(label: str) -> tuple[int, str]:
    context = c189.CONTEXT_BY_LABEL[label]
    first, second, third = context.observables
    product_matrix = sp.simplify(
        c189.OBSERVABLES[first] * c189.OBSERVABLES[second]
    )
    third_matrix = c189.OBSERVABLES[third]
    if exact_zero(product_matrix - third_matrix):
        return 1, third
    if exact_zero(product_matrix + third_matrix):
        return -1, third
    raise ValueError(("third-product", label))


def matrix_is_real(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(sp.im(entry)) == 0 for entry in matrix)


def program_nonselective_state(
    preparation: str,
    code: tuple[int, int, int],
) -> sp.Matrix:
    system = c189.PREPARATIONS[preparation]
    pointer = c189.density(c189.POINTER_BLANK)
    unitary = interpret_context_code(code)
    joint = sp.simplify(
        unitary
        * c189.tensor(system, pointer)
        * unitary.H
    )
    return sp.simplify(c189.partial_trace_pointer(joint))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN CYCLE-189 PROCESS")
    observed_hashes = {path: sha256(path) for path in FROZEN}
    check(
        "Cycle 189 runner and note remain frozen",
        observed_hashes == FROZEN,
        {path.name: digest for path, digest in observed_hashes.items()},
    )

    print("\nSIGNED-PAULI CLIFFORD SYNTHESIS")
    full = clifford_search(FULL_ALPHABET)
    real = clifford_search(REAL_ALPHABET)
    check(
        "the signed-Pauli BFS enumerates the full two-qubit Clifford action group",
        full.state_count == 11_520
        and full.maximum_depth == 11
        and sum(full.depth_histogram.values()) == 11_520,
        {
            "states": full.state_count,
            "diameter": full.maximum_depth,
            "histogram": full.depth_histogram,
        },
    )
    check(
        "H and CNOT alone generate the exact real Clifford subgroup",
        real.state_count == 1_152
        and real.maximum_depth == 15
        and sum(real.depth_histogram.values()) == 1_152,
        {
            "states": real.state_count,
            "diameter": real.maximum_depth,
        },
    )
    check(
        "all six shortest full-Clifford decoder programs use only H and CNOT",
        full.programs == EXPECTED_PROGRAMS
        and real.programs == EXPECTED_PROGRAMS
        and full.depths == real.depths,
        {
            "programs": full.programs,
            "depths": full.depths,
        },
    )

    print("\nCONTEXT GENERATOR DECODING")
    decoder_failures = []
    for label, program in EXPECTED_PROGRAMS.items():
        decoder = circuit_matrix(program)
        context = c189.CONTEXT_BY_LABEL[label]
        first, second, third = context.observables
        if not exact_zero(
            decoder
            * c189.OBSERVABLES[first]
            * decoder.H
            - c189.OBSERVABLES["ZI"]
        ):
            decoder_failures.append((label, first, "ZI"))
        if not exact_zero(
            decoder
            * c189.OBSERVABLES[second]
            * decoder.H
            - c189.OBSERVABLES["IZ"]
        ):
            decoder_failures.append((label, second, "IZ"))
        sign, derived_third = third_observable_sign(label)
        wanted_third = sign * c189.OBSERVABLES["ZZ"]
        if derived_third != third or not exact_zero(
            decoder
            * c189.OBSERVABLES[third]
            * decoder.H
            - wanted_third
        ):
            decoder_failures.append(
                (label, third, sign, derived_third)
            )
    check(
        "each short program maps its two independent generators to ZI and IZ",
        not decoder_failures,
        decoder_failures,
    )
    sign_map = {
        label: third_observable_sign(label)
        for label in EXPECTED_PROGRAMS
    }
    check(
        "the third outcome sign is derived, with C3 the unique negative product",
        sign_map
        == {
            "R1": (1, "ZZ"),
            "R2": (1, "XX"),
            "R3": (1, "YY"),
            "C1": (1, "ZX"),
            "C2": (1, "XZ"),
            "C3": (-1, "YY"),
        },
        sign_map,
    )

    print("\nONE UNIFORM POINTER INTERPRETER")
    interpreter_failures = []
    for label, program in EXPECTED_PROGRAMS.items():
        generated = interpreted_context_unitary(program)
        reference = c189.context_dilation(label)
        if not exact_zero(generated - reference):
            interpreter_failures.append(label)
    check(
        "decoder-copy-undecoder reproduces all six Cycle-189 dilations exactly",
        not interpreter_failures,
        interpreter_failures,
    )
    check(
        "the common pointer copy is two commuting disjoint CNOTs",
        COPY_02 * COPY_13 == COPY_13 * COPY_02
        and COMMON_POINTER_COPY.H * COMMON_POINTER_COPY == I16,
        "",
    )
    code_failures = []
    for label in EXPECTED_PROGRAMS:
        if not exact_zero(
            interpret_context_code(CONTEXT_CODES[label])
            - c189.context_dilation(label)
        ):
            code_failures.append(label)
    check(
        "one three-bit context program selects every physical pointer instrument",
        not code_failures
        and len(set(CONTEXT_CODES.values())) == 8
        and 2**2 < 7 <= 2**3,
        {
            "codes": CONTEXT_CODES,
            "failures": code_failures,
        },
    )

    print("\nPREPARATION PROGRAMS")
    preparation_failures = []
    for label, program in PREPARATION_PROGRAMS.items():
        generated = circuit_matrix(program)
        if not exact_zero(
            generated - c189.PREPARATION_UNITARIES[label]
        ):
            preparation_failures.append((label, program))
    preparation_cost = {
        label: {
            "gates": len(program),
            "depth": scheduled_depth(program, GATE_SUPPORT_2),
            "code": PREPARATION_CODES[label],
        }
        for label, program in PREPARATION_PROGRAMS.items()
    }
    check(
        "both Cycle-189 preparations use the same H/CNOT interpreter",
        not preparation_failures
        and preparation_cost
        == {
            "prep:Z0Z0": {"gates": 0, "depth": 0, "code": (0,)},
            "prep:X+X+": {"gates": 2, "depth": 1, "code": (1,)},
        },
        {
            "cost": preparation_cost,
            "failures": preparation_failures,
        },
    )

    print("\nGATE, DEPTH, POINTER, AND PROGRAM COST")
    context_cost = {}
    for label, program in EXPECTED_PROGRAMS.items():
        tape = instrument_instruction_tape(program)
        context_cost[label] = {
            "basis_gates": len(program),
            "instrument_gates": len(tape),
            "instrument_depth": scheduled_depth(tape, GATE_SUPPORT_4),
            "program_code": CONTEXT_CODES[label],
        }
    check(
        "the six exact instrument costs are 2|V|+2 gates and 2depth(V)+1 layers",
        context_cost
        == {
            "R1": {
                "basis_gates": 0,
                "instrument_gates": 2,
                "instrument_depth": 1,
                "program_code": (0, 0, 0),
            },
            "R2": {
                "basis_gates": 4,
                "instrument_gates": 10,
                "instrument_depth": 9,
                "program_code": (0, 0, 1),
            },
            "R3": {
                "basis_gates": 3,
                "instrument_gates": 8,
                "instrument_depth": 7,
                "program_code": (0, 1, 0),
            },
            "C1": {
                "basis_gates": 1,
                "instrument_gates": 4,
                "instrument_depth": 3,
                "program_code": (0, 1, 1),
            },
            "C2": {
                "basis_gates": 3,
                "instrument_gates": 8,
                "instrument_depth": 7,
                "program_code": (1, 0, 0),
            },
            "C3": {
                "basis_gates": 2,
                "instrument_gates": 6,
                "instrument_depth": 5,
                "program_code": (1, 0, 1),
            },
        },
        context_cost,
    )
    pointer_words = tuple(product((0, 1), repeat=2))
    pointer_vectors = tuple(
        c189.tensor(
            c189.KET1 if first else c189.KET0,
            c189.KET1 if second else c189.KET0,
        )
        for first, second in pointer_words
    )
    pointer_gram = sp.Matrix(
        [
            [
                sp.simplify((left.H * right)[0])
                for right in pointer_vectors
            ]
            for left in pointer_vectors
        ]
    )
    check(
        "two pointer qubits exactly and minimally host four orthogonal records",
        pointer_gram == sp.eye(4)
        and 2**1 < 4 <= 2**2,
        pointer_gram,
    )

    print("\nPHASE AND SIGN RESOURCE")
    dynamic_tokens = {
        token
        for program in EXPECTED_PROGRAMS.values()
        for token in program
    } | {
        token
        for program in PREPARATION_PROGRAMS.values()
        for token in program
    }
    all_generated_real = all(
        matrix_is_real(interpreted_context_unitary(program))
        for program in EXPECTED_PROGRAMS.values()
    ) and all(
        matrix_is_real(circuit_matrix(program))
        for program in PREPARATION_PROGRAMS.values()
    )
    check(
        "the complete preparation and context program bank consumes zero phase gates",
        dynamic_tokens <= {"H0", "H1", "CX01", "CX10"}
        and not dynamic_tokens & {"S0", "S1"}
        and all_generated_real,
        {
            "tokens": sorted(dynamic_tokens),
            "all_real": all_generated_real,
        },
    )
    check(
        "YY and the C3 minus sign arise from Pauli multiplication, not an S gate",
        exact_zero(
            c189.OBSERVABLES["ZX"]
            * c189.OBSERVABLES["XZ"]
            - c189.OBSERVABLES["YY"]
        )
        and exact_zero(
            c189.OBSERVABLES["ZZ"]
            * c189.OBSERVABLES["XX"]
            + c189.OBSERVABLES["YY"]
        ),
        sign_map,
    )

    print("\nIDENTITY CONTAINMENT")
    omitted = interpret_context_code(CONTEXT_CODES["OMIT"])
    r1 = interpret_context_code(CONTEXT_CODES["R1"])
    omit_state = program_nonselective_state(
        "prep:X+X+",
        CONTEXT_CODES["OMIT"],
    )
    r1_state = program_nonselective_state(
        "prep:X+X+",
        CONTEXT_CODES["R1"],
    )
    omit_xx = c189.tester_distribution(omit_state, "XX")
    r1_xx = c189.tester_distribution(r1_state, "XX")
    check(
        "OMIT skips the common copy while R1 executes it despite an empty decoder",
        omitted == I16
        and r1 == COMMON_POINTER_COPY
        and r1 != omitted,
        "",
    )
    check(
        "circuit-generated identity and R1 measure-and-forget retain the Cycle-189 separation",
        omit_xx == (1, 0)
        and r1_xx == (sp.Rational(1, 2), sp.Rational(1, 2)),
        {"OMIT": omit_xx, "R1": r1_xx},
    )

    print("\nALGEBRAIC / MICROSCOPIC FIREWALL")
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    normalized = " ".join(note_text.lower().split())
    required_phrases = (
        "one common h/cnot interpreter",
        "six short context programs",
        "three-bit context-program register",
        "one-bit preparation program",
        "zero dynamic phase gates",
        "c3 minus sign is derived",
        "two pointer qubits are minimal",
        "identity containment",
        "algebraic circuit generation",
        "not a microscopic nearest-neighbour lattice derivation",
        "classical program dispatch remains imported",
        "born trace pairing remains imported",
        "actuality and frequency remain open",
        "no axiom conclusion follows",
    )
    missing = tuple(
        phrase for phrase in required_phrases
        if phrase not in normalized
    )
    check(
        "the Cycle-191 note preserves the compression and authority boundary",
        not missing,
        missing,
    )

    print("\nACCOUNTING")
    print(
        "CLIFFORD",
        {
            "full_states": full.state_count,
            "full_diameter": full.maximum_depth,
            "real_states": real.state_count,
            "real_diameter": real.maximum_depth,
        },
    )
    print("PROGRAMS", EXPECTED_PROGRAMS)
    print("CONTEXT_COST", context_cost)
    print("PREPARATION_COST", preparation_cost)
    print(
        "PROGRAM_STORAGE",
        {
            "context_bits": 3,
            "preparation_bits": 1,
            "basis_tokens": sum(map(len, EXPECTED_PROGRAMS.values())),
            "legal_context_codes": 7,
            "reserved_codes": 1,
        },
    )
    print("PHASE", {"dynamic_phase_gates": 0, "signs": sign_map})
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE191_COMMON_CLIFFORD_INTERPRETER_GREEN"
        if FAIL == 0
        else "CYCLE191_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
