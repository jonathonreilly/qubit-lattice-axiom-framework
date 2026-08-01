#!/usr/bin/env python3
"""Independent 142-factor neutral-controlled FSWAP acceptance checker.

This executable reconstructs its witness from the landed Cycle821,
Cycle822, and Cycle823 opcode definitions.  It intentionally imports no
Cycle864 implementation.  Its finite claim domain is two charged target M2,
one neutral control M2, two clean neutral work M2, and clean returned route
sites on the explicit local patch below.

It was constructed independently of the eleven-factor Cycle864 compiler and
is included as an alternate acceptance route, not as a factor minimum.
Authority: none.  Audit: unset.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TOL = 1.0e-12

LANDED_SOURCE_SHA256 = {
    "scripts/frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30.py":
        "e010b4d407e38c7832ff94b8d7886bf5369e06be4eef44c01e35688f56d103bd",
    "scripts/frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30.py":
        "17af3e27463c94a1e98f6bfe578b6d7b1a575af50bccd96b472ab0ede44f775c",
    "scripts/frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30.py":
        "1c70bf782005bbf90608c99417470dcb0f964749644849c8835ef6314c61a737",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py":
        "e79b733bd3b8e273a2094679e6175b5d1f253ebef1a33b96544519cbdf278e13",
}

EXPECTED_DICTIONARY_SHA256 = (
    "fe71ebf6e5fe525ba3b62a9b414288892b08b3a7d400245c24248fbe49013faa"
)
EXPECTED_SEQUENCE_SHA256 = (
    "4cb9cf8fe1ea9474a9716a79303356120bec4ad53fe2703811f363edbd711298"
)
EXPECTED_LAYOUT_SHA256 = (
    "673b21414d98f84b1a23098862eb9cac779015b85daa76ed14bd27235e2827fc"
)
EXPECTED_TARGET_SHA256 = (
    "bb740365ae861806f2565112baf82a1d94657de9750a6a6820d09c5fbc722a92"
)


def require(condition: bool, detail: object) -> None:
    if not condition:
        raise AssertionError(detail)


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def matrix_digest(matrix: np.ndarray) -> str:
    rounded = np.round(np.asarray(matrix, dtype=complex), 14)
    return sha256(rounded.tobytes()).hexdigest()


I2 = np.eye(2, dtype=complex)
X = np.asarray(((0, 1), (1, 0)), dtype=complex)
Y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
H = np.asarray(((1, 1), (1, -1)), dtype=complex) / math.sqrt(2.0)
T = np.diag((1.0, np.exp(0.25j * np.pi))).astype(complex)
TDG = T.conj().T
SWAP = np.asarray(
    ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)),
    dtype=complex,
)
FSWAP = SWAP.copy()
FSWAP[3, 3] = -1
CNOT = np.asarray(
    ((1, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0)),
    dtype=complex,
)
CZ = np.diag((1, 1, 1, -1)).astype(complex)

# Cycle821 pair_rotation_generator(0, "X", 1, "X") is Y_0 X_1.
# In the landed little-endian local basis this is kron(X_1, Y_0).
K_Y0_X1 = np.kron(X, Y)
PAIR_R_XX_MINUS = (np.eye(4) + 1j * K_Y0_X1) / math.sqrt(2.0)
PAIR_R_XX_PLUS = (np.eye(4) - 1j * K_Y0_X1) / math.sqrt(2.0)

MATRICES = {
    "CP_Z": CZ,
    "FSWAP": FSWAP,
    "PAIR_R_XX_+1": PAIR_R_XX_PLUS,
    "PAIR_R_XX_-1": PAIR_R_XX_MINUS,
    "SWAP": SWAP,
    "endpoint_CNOT": CNOT,
    "endpoint_H": H,
    "endpoint_T": T,
    "endpoint_Tdg": TDG,
}


Coord = tuple[int, int, int]

A: Coord = (0, 0, 0)
B: Coord = (1, 1, 0)
Q: Coord = (1, 0, 0)
R: Coord = (0, 1, 0)
C: Coord = (2, 0, 0)
X_RAIL: Coord = (0, 0, 1)
Y_RAIL: Coord = (1, 0, 1)
Z_RAIL: Coord = (1, 1, 1)
N1: Coord = (2, 0, -1)
N2: Coord = (1, 0, -1)
N3: Coord = (0, 0, -1)
N4: Coord = (0, 1, -1)

CHARGED = (A, B, X_RAIL, Y_RAIL, Z_RAIL)
NEUTRAL = (C, Q, R, N1, N2, N3, N4)
SITES = (C, A, B, Q, R, X_RAIL, Y_RAIL, Z_RAIL, N1, N2, N3, N4)
SITE_INDEX = {site: index for index, site in enumerate(SITES)}

PATH_AB = (A, X_RAIL, Y_RAIL, Z_RAIL, B)
PATH_QR = (Q, N2, N3, N4, R)
PATH_CR = (C, N1, N2, N3, N4, R)
PATH_CQ = (C, Q)


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


Factor = tuple[str, np.ndarray, tuple[Coord, ...], str]


def inverse_opcode(opcode: str) -> str:
    return {
        "endpoint_T": "endpoint_Tdg",
        "endpoint_Tdg": "endpoint_T",
        "PAIR_R_XX_-1": "PAIR_R_XX_+1",
        "PAIR_R_XX_+1": "PAIR_R_XX_-1",
    }.get(opcode, opcode)


def build_word() -> tuple[Factor, ...]:
    output: list[Factor] = []

    def emit(opcode: str, sites: tuple[Coord, ...], logical: str) -> None:
        require(opcode in MATRICES, ("unknown opcode", opcode))
        require(len(sites) in (1, 2), (opcode, sites))
        if len(sites) == 2:
            require(manhattan(sites[0], sites[1]) == 1, (opcode, sites))
        output.append((opcode, MATRICES[opcode], sites, logical))

    def route(
        opcode: str,
        path: tuple[Coord, ...],
        exchange: str,
        logical: str,
    ) -> None:
        edges = tuple(zip(path[:-2], path[1:-1]))
        for edge in edges:
            emit(exchange, edge, logical + ":route_fwd")
        emit(opcode, (path[-2], path[-1]), logical + ":local")
        for edge in reversed(edges):
            emit(exchange, edge, logical + ":route_ret")

    def endpoint_cnot(control: Coord, target: Coord, logical: str) -> None:
        if control in CHARGED:
            require(target in NEUTRAL, (control, target))
            emit("endpoint_CNOT", (control, target), logical)
        elif (control, target) == (Q, R):
            route("endpoint_CNOT", PATH_QR, "SWAP", logical)
        elif (control, target) == (C, R):
            route("endpoint_CNOT", PATH_CR, "SWAP", logical)
        elif (control, target) == (C, Q):
            emit("endpoint_CNOT", (C, Q), logical)
        else:
            raise AssertionError(("unrouted CNOT", control, target))

    # The landed 15-factor Cycle823 Toffoli word, specialized to clean R=0.
    # The omitted first CNOT(Q->R) acts immediately after H(R), hence fixes
    # the target |+> exactly for either value of Q.
    clean_and = (
        ("endpoint_H", (R,)),
        ("endpoint_Tdg", (R,)),
        ("endpoint_CNOT", (C, R)),
        ("endpoint_T", (R,)),
        ("endpoint_CNOT", (Q, R)),
        ("endpoint_Tdg", (R,)),
        ("endpoint_CNOT", (C, R)),
        ("endpoint_T", (Q,)),
        ("endpoint_T", (R,)),
        ("endpoint_H", (R,)),
        ("endpoint_CNOT", (C, Q)),
        ("endpoint_T", (C,)),
        ("endpoint_Tdg", (Q,)),
        ("endpoint_CNOT", (C, Q)),
    )

    def emit_rows(rows: tuple[tuple[str, tuple[Coord, ...]], ...], prefix: str) -> None:
        for index, (opcode, sites) in enumerate(rows):
            logical = f"{prefix}:{index:02d}"
            if opcode == "endpoint_CNOT":
                endpoint_cnot(sites[0], sites[1], logical)
            else:
                emit(opcode, sites, logical)

    def emit_cs(control: Coord, target: Coord, prefix: str, dagger: bool) -> None:
        if dagger:
            rows = (
                ("endpoint_Tdg", (control,)),
                ("endpoint_Tdg", (target,)),
                ("endpoint_CNOT", (control, target)),
                ("endpoint_T", (target,)),
                ("endpoint_CNOT", (control, target)),
            )
        else:
            rows = (
                ("endpoint_T", (control,)),
                ("endpoint_T", (target,)),
                ("endpoint_CNOT", (control, target)),
                ("endpoint_Tdg", (target,)),
                ("endpoint_CNOT", (control, target)),
            )
        emit_rows(rows, prefix)

    # Q = A xor B.
    endpoint_cnot(A, Q, "xor:a_to_q")
    endpoint_cnot(B, Q, "xor:b_to_q")

    # R = C Q; apply controlled XX; return R with the exact inverse.
    emit_rows(clean_and, "and_compute")
    route("PAIR_R_XX_-1", PATH_AB, "FSWAP", "cxx:pair_minus")
    emit("CP_Z", (R, A), "cxx:cz")
    route("PAIR_R_XX_+1", PATH_AB, "FSWAP", "cxx:pair_plus")
    clean_and_dagger = tuple(
        (inverse_opcode(opcode), sites)
        for opcode, sites in reversed(clean_and)
    )
    emit_rows(clean_and_dagger, "and_uncompute")

    # The fermionic sign is CS(C,A) CS(C,B) CSdg(C,A xor B).  R is reused
    # as a clean neutral copy so every T/Tdg remains on a neutral coordinate.
    endpoint_cnot(A, R, "phase:copy_a")
    emit_cs(C, R, "phase:CS_a", dagger=False)
    endpoint_cnot(A, R, "phase:uncopy_a")
    endpoint_cnot(B, R, "phase:copy_b")
    emit_cs(C, R, "phase:CS_b", dagger=False)
    endpoint_cnot(B, R, "phase:uncopy_b")
    emit_cs(C, Q, "phase:CSdg_xor", dagger=True)

    # Return Q.
    endpoint_cnot(B, Q, "xor:uncompute_b")
    endpoint_cnot(A, Q, "xor:uncompute_a")
    return tuple(output)


def apply_local(
    columns: np.ndarray,
    matrix: np.ndarray,
    physical_sites: tuple[Coord, ...],
) -> np.ndarray:
    width = len(SITES)
    dimension = 1 << width
    wires = tuple(SITE_INDEX[site] for site in physical_sites)
    local_width = len(wires)
    output = np.zeros_like(columns)
    for source in range(dimension):
        local_source = sum(
            ((source >> wire) & 1) << local_index
            for local_index, wire in enumerate(wires)
        )
        base = source
        for wire in wires:
            base &= ~(1 << wire)
        for local_target in range(1 << local_width):
            amplitude = matrix[local_target, local_source]
            if abs(amplitude) < 1.0e-15:
                continue
            target = base
            for local_index, wire in enumerate(wires):
                target |= ((local_target >> local_index) & 1) << wire
            output[target] += amplitude * columns[source]
    return output


def clean_input_columns() -> np.ndarray:
    columns = np.zeros((1 << len(SITES), 8), dtype=complex)
    for column in range(8):
        c_value = column & 1
        a_value = (column >> 1) & 1
        b_value = (column >> 2) & 1
        basis = (
            (c_value << SITE_INDEX[C])
            | (a_value << SITE_INDEX[A])
            | (b_value << SITE_INDEX[B])
        )
        columns[basis, column] = 1.0
    return columns


def exact_target_columns() -> tuple[np.ndarray, list[dict[str, object]]]:
    columns = np.zeros((1 << len(SITES), 8), dtype=complex)
    mapping = []
    for column in range(8):
        c_value = column & 1
        a_value = (column >> 1) & 1
        b_value = (column >> 2) & 1
        a_out = b_value if c_value else a_value
        b_out = a_value if c_value else b_value
        phase = -1 if c_value and a_value and b_value else 1
        basis = (
            (c_value << SITE_INDEX[C])
            | (a_out << SITE_INDEX[A])
            | (b_out << SITE_INDEX[B])
        )
        columns[basis, column] = phase
        mapping.append({
            "column": column,
            "input_cab": [c_value, a_value, b_value],
            "output_cab": [c_value, a_out, b_out],
            "phase": phase,
        })
    return columns, mapping


def target_matrix() -> np.ndarray:
    matrix = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        c_value = source & 1
        a_value = (source >> 1) & 1
        b_value = (source >> 2) & 1
        a_out = b_value if c_value else a_value
        b_out = a_value if c_value else b_value
        phase = -1 if c_value and a_value and b_value else 1
        target = c_value | (a_out << 1) | (b_out << 2)
        matrix[target, source] = phase
    return matrix


def main() -> None:
    require(len(SITE_INDEX) == len(SITES), "duplicate layout coordinate")
    require(not (set(CHARGED) & set(NEUTRAL)), "charged/neutral overlap")
    for path in (PATH_AB, PATH_QR, PATH_CR, PATH_CQ):
        require(
            all(manhattan(left, right) == 1 for left, right in zip(path, path[1:])),
            ("non-NN path", path),
        )

    source_hashes = {
        path: file_sha256(ROOT / path)
        for path in LANDED_SOURCE_SHA256
    }
    require(source_hashes == LANDED_SOURCE_SHA256, ("source hash drift", source_hashes))

    # Compare the independently reconstructed matrices to landed Cycle822/823
    # functions only after constructing them locally.
    sys.path.insert(0, str(ROOT / "scripts"))
    import frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30 as cycle822
    import frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30 as cycle823

    landed = {
        opcode: np.asarray(
            cycle823.primitive_matrix(opcode)
            if opcode.startswith("endpoint_")
            else cycle822.primitive_matrix(opcode),
            dtype=complex,
        )
        for opcode in MATRICES
    }
    membership = {}
    for opcode, matrix in sorted(MATRICES.items()):
        landed_matrix = landed[opcode]
        independent_digest = matrix_digest(matrix)
        landed_digest = matrix_digest(landed_matrix)
        residual = float(np.linalg.norm(matrix - landed_matrix))
        require(independent_digest == landed_digest, (opcode, independent_digest, landed_digest))
        require(residual == 0.0, (opcode, residual))
        membership[opcode] = {
            "matrix_sha256": independent_digest,
            "landed_matrix_sha256": landed_digest,
            "matrix_residual": residual,
        }

    word = build_word()
    census = dict(sorted(Counter(factor[0] for factor in word).items()))
    require(len(word) == 142, ("factor census", len(word), census))
    nn_failures = sum(
        manhattan(sites[0], sites[1]) != 1
        for _opcode, _matrix, sites, _logical in word
        if len(sites) == 2
    )
    untyped_uses = sum(
        site not in CHARGED and site not in NEUTRAL
        for _opcode, _matrix, sites, _logical in word
        for site in sites
    )
    require(nn_failures == 0, ("NN failures", nn_failures))
    require(untyped_uses == 0, ("untyped uses", untyped_uses))

    records = [
        {
            "index": index,
            "opcode": opcode,
            "matrix_sha256": matrix_digest(matrix),
            "sites": [list(site) for site in sites],
            "logical": logical,
        }
        for index, (opcode, matrix, sites, logical) in enumerate(word)
    ]
    layout = {
        "charged": [list(site) for site in CHARGED],
        "neutral": [list(site) for site in NEUTRAL],
        "logical": {
            "c": list(C), "a": list(A), "b": list(B),
            "q": list(Q), "r": list(R),
        },
        "paths": {
            "a_b": [list(site) for site in PATH_AB],
            "q_r": [list(site) for site in PATH_QR],
            "c_r": [list(site) for site in PATH_CR],
            "c_q": [list(site) for site in PATH_CQ],
        },
    }
    used_opcodes = sorted(census)
    dictionary_digest = sha256("|".join(
        f"{opcode}:{matrix_digest(MATRICES[opcode])}"
        for opcode in used_opcodes
    ).encode()).hexdigest()
    sequence_digest = sha256(canonical_json(records).encode()).hexdigest()
    layout_digest = sha256(canonical_json(layout).encode()).hexdigest()
    require(dictionary_digest == EXPECTED_DICTIONARY_SHA256, dictionary_digest)
    require(sequence_digest == EXPECTED_SEQUENCE_SHA256, sequence_digest)
    require(layout_digest == EXPECTED_LAYOUT_SHA256, layout_digest)

    target = target_matrix()
    target_digest = matrix_digest(target)
    require(target_digest == EXPECTED_TARGET_SHA256, target_digest)
    require(float(np.linalg.norm(target @ target - np.eye(8))) == 0.0, "target square")
    require(float(np.linalg.norm(target.conj().T - target)) == 0.0, "target inverse")

    input_columns = clean_input_columns()
    expected_columns, column_mapping = exact_target_columns()
    state = input_columns.copy()
    deletion_rows = []
    parity_rows = []
    maximum_unitarity_residual = 0.0
    for index, (opcode, matrix, sites, logical) in enumerate(word):
        local_parity = np.diag(tuple(
            (-1) ** sum(
                (basis >> local_index) & 1
                for local_index, site in enumerate(sites)
                if site in CHARGED
            )
            for basis in range(1 << len(sites))
        )).astype(complex)
        parity_residual = float(np.linalg.norm(
            matrix @ local_parity - local_parity @ matrix
        ))
        parity_rows.append(parity_residual)
        maximum_unitarity_residual = max(
            maximum_unitarity_residual,
            float(np.linalg.norm(
                matrix.conj().T @ matrix - np.eye(matrix.shape[0])
            )),
        )

        next_state = apply_local(state, matrix, sites)
        # If S is the unchanged unitary suffix, deleting this factor changes
        # S G prefix into S prefix.  Hence this prefix residual is exactly the
        # final deleted-word residual by unitary invariance of Frobenius norm.
        deletion_rows.append({
            "index": index,
            "opcode": opcode,
            "logical": logical,
            "deleted_word_residual": float(np.linalg.norm(next_state - state)),
        })
        state = next_state

    target_residual = float(np.linalg.norm(state - expected_columns))
    factor_parity_failures = sum(value > TOL for value in parity_rows)
    prefix_parity_failures = 0 if factor_parity_failures == 0 else len(word)
    maximum_parity_residual = max(parity_rows, default=0.0)
    require(target_residual < TOL, ("target residual", target_residual))
    require(factor_parity_failures == 0, ("factor parity", factor_parity_failures))
    require(prefix_parity_failures == 0, ("prefix parity", prefix_parity_failures))
    require(maximum_unitarity_residual < TOL, maximum_unitarity_residual)

    squared = state.copy()
    for _opcode, matrix, sites, _logical in word:
        squared = apply_local(squared, matrix, sites)
    square_residual = float(np.linalg.norm(squared - input_columns))

    inverted = state.copy()
    for _opcode, matrix, sites, _logical in reversed(word):
        inverted = apply_local(inverted, matrix.conj().T, sites)
    inverse_residual = float(np.linalg.norm(inverted - input_columns))
    require(square_residual < TOL, ("square residual", square_residual))
    require(inverse_residual < TOL, ("inverse residual", inverse_residual))

    nondata = set(SITES) - {C, A, B}
    return_leakages = []
    control_leakages = []
    for column in range(8):
        expected_control = column & 1
        return_leakages.append(math.sqrt(sum(
            abs(state[basis, column]) ** 2
            for basis in range(1 << len(SITES))
            if any((basis >> SITE_INDEX[site]) & 1 for site in nondata)
        )))
        control_leakages.append(math.sqrt(sum(
            abs(state[basis, column]) ** 2
            for basis in range(1 << len(SITES))
            if ((basis >> SITE_INDEX[C]) & 1) != expected_control
        )))
    maximum_return_leakage = max(return_leakages)
    maximum_control_leakage = max(control_leakages)
    require(maximum_return_leakage < TOL, maximum_return_leakage)
    require(maximum_control_leakage < TOL, maximum_control_leakage)

    deletion_failures = sum(
        row["deleted_word_residual"] <= 1.0e-10
        for row in deletion_rows
    )
    deletion_minimum = min(
        row["deleted_word_residual"] for row in deletion_rows
    )
    deletion_maximum = max(
        row["deleted_word_residual"] for row in deletion_rows
    )
    require(deletion_failures == 0, ("inactive deletion", deletion_rows))

    # Independently execute the clean-target AND subword on all four C,Q columns.
    clean_and_input = np.zeros((1 << len(SITES), 4), dtype=complex)
    clean_and_expected = np.zeros_like(clean_and_input)
    for column in range(4):
        c_value = column & 1
        q_value = (column >> 1) & 1
        source = (c_value << SITE_INDEX[C]) | (q_value << SITE_INDEX[Q])
        target_basis = source | ((c_value & q_value) << SITE_INDEX[R])
        clean_and_input[source, column] = 1.0
        clean_and_expected[target_basis, column] = 1.0
    clean_and_observed = clean_and_input.copy()
    for _opcode, matrix, sites, logical in word:
        if logical.startswith("and_compute"):
            clean_and_observed = apply_local(clean_and_observed, matrix, sites)
    clean_and_residual = float(np.linalg.norm(
        clean_and_observed - clean_and_expected
    ))
    require(clean_and_residual < TOL, clean_and_residual)

    # Exact target differs from controlled ordinary SWAP in the |111> column.
    controlled_swap = target.copy()
    controlled_swap[7, 7] = 1
    literal_fswap_sign_residual = float(np.linalg.norm(target - controlled_swap))
    require(literal_fswap_sign_residual == 2.0, literal_fswap_sign_residual)

    for opcode in membership:
        membership[opcode]["count"] = census.get(opcode, 0)

    receipt = {
        "schema": "cycle864_independent_cfswap_142_factor_acceptance_v1",
        "independence_boundary": (
            "landed Cycle821/822/823 sources only; no Cycle864 implementation imported"
        ),
        "source_sha256": source_hashes,
        "target": {
            "basis_order": "little-endian c+2a+4b",
            "controlled_fswap_matrix_sha256": target_digest,
            "literal_fswap_matrix_sha256": matrix_digest(FSWAP),
            "columns": column_mapping,
            "target_residual": target_residual,
            "inverse_residual": inverse_residual,
            "square_residual": square_residual,
            "literal_fswap_vs_controlled_swap_residual": literal_fswap_sign_residual,
        },
        "dictionary": {
            "opcode_dictionary_sha256": dictionary_digest,
            "membership": membership,
            "census": census,
        },
        "emission": {
            "logical_factors": 54,
            "routed_factors": len(word),
            "sequence_sha256": sequence_digest,
            "layout_sha256": layout_digest,
            "layout": layout,
            "nearest_neighbour_failures": nn_failures,
            "untyped_coordinate_uses": untyped_uses,
        },
        "parity": {
            "P_ext_coordinate_sha256": sha256(
                repr(tuple(sorted(CHARGED))).encode()
            ).hexdigest(),
            "elementary_factors_tested": len(word),
            "factor_commutator_failures": factor_parity_failures,
            "maximum_factor_commutator_residual": maximum_parity_residual,
            "prefixes_certified_by_common_commutant": len(word),
            "prefix_commutator_failures": prefix_parity_failures,
        },
        "returns": {
            "maximum_control_value_leakage": maximum_control_leakage,
            "maximum_work_and_route_leakage": maximum_return_leakage,
            "clean_and_four_column_residual": clean_and_residual,
        },
        "deletion_controls": {
            "factors_tested": len(deletion_rows),
            "undetected_deletions": deletion_failures,
            "minimum_deleted_word_residual": deletion_minimum,
            "maximum_deleted_word_residual": deletion_maximum,
            "residual_identity": "norm(S G P - S P) = norm(G P - P)",
        },
        "maximum_opcode_unitarity_residual": maximum_unitarity_residual,
    }
    receipt_digest = sha256(canonical_json(receipt).encode()).hexdigest()
    receipt["receipt_sha256"] = receipt_digest
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
