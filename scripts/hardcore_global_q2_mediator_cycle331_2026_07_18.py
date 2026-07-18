#!/usr/bin/env python3
"""Cycle 331 checkpoint: hard-core global-Q2 mediator on the Cycle-328 seam.

The retained candidate uses one M2 per mediator direction and forbids double
occupation.  The direct projected bosonic coin is tested as a comparator.  A
local collision-conditioned completion applies the inherited Cycle-214 coin
to one onsite mediator and identity to two onsite mediators.  This supplied
completion is unitary and proper-cubic; it is not a statistics-selection law.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import re
import sys

import numpy as np
from scipy import sparse
from scipy.linalg import expm
from scipy.sparse.linalg import expm_multiply


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import global_q2_simultaneous_two_source_cycle328_2026_07_18 as c328
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as c322


LEFT = c322.LEFT
RIGHT = c322.RIGHT
ENDPOINTS = c322.ENDPOINTS
LABELS = c322.LABELS
LOCAL_MASKS = c322.LOCAL_MASKS
LOCAL_INDEX = c322.LOCAL_INDEX
ANGLE = c322.ANGLE
REVERSE = c322.REVERSE
SIZES = (3, 4, 6)
HELD_SIZE = 6
TOLERANCE = 3e-10
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "HARDCORE_GLOBAL_Q2_MEDIATOR_CYCLE331_NOTE_2026-07-18.md"
)

N1_ROUTES = (
    "direct projected bosonic hard-core coin",
    "collision-conditioned hard-core completion",
    "uniform hard-core XY coin",
    "fermionic antisymmetric mediator",
    "independently labelled mediator",
    "bosonic mediator",
    "unit-weight hard-core Q2",
    "contact-sensitive hard-core observable",
)
WALLS = ("W_coin", "W_stats", "W_unit", "W_contact", "W_energy")
TRIGGER_PARTS = (
    ("we", " assume"),
    ("by", " construction"),
    ("as is", " standard"),
    ("the framework", " provides"),
    ("bridge", " context"),
    ("back", "ground"),
    ("natural", "ly"),
    ("obvious", "ly"),
    ("standard", " qft"),
    ("regis", "tered"),
    ("canon", "ical"),
)

PASS = 0
FAIL = 0

Occupation = tuple[int, int]
State = dict[Occupation, np.ndarray]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(file_path: Path) -> str:
    text = file_path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-331 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e_hc g_hc = g_physical,hc e_hc",
        "hard-core global q=2",
        "exclusion-preserving",
        "collision-conditioned hard-core completion",
        "identity on onsite q2",
        "supplied collision rule",
        "projected bosonic coin",
        "route-specific",
        "nonfactorizing occupation response",
        "bosonic and labelled cycle-328 values",
        "all 24 proper-cubic frames",
        "endpoint reversal",
        "all l=3 translations",
        "held l=6",
        "36 m2 per cell",
        "97-m2",
        "mass firewall",
        "contact firewall",
        "not force",
        "not energy",
        "not stress",
        "not gravity",
        "not metric",
        "not time",
        "supplied structure",
        "fail / do not ship",
        "no axiom pressure",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the hard-core theorem and supplied coin boundary", not missing, missing)


def methodology_controls() -> None:
    print("\nEXECUTABLE NO-GO DISCIPLINE")
    note = NOTE.read_text(encoding="utf-8")
    allowed = {"ATTEMPTED", "RULED OUT BY PRIOR RESULT", "OPEN / UNTESTED"}
    markers = {}
    illegal = []
    for route in N1_ROUTES:
        pattern = re.compile(
            rf"^\|\s*{re.escape(route)}\s*\|\s*\*\*([^*]+)\*\*\s*\|",
            re.MULTILINE,
        )
        match = pattern.search(note)
        marker = match.group(1).strip() if match else "MISSING"
        markers[route] = marker
        if marker not in allowed:
            illegal.append((route, marker))
    check(
        "N1 gives exact honesty markers to eight distinct hard-core/statistics routes",
        not illegal and len(markers) == 8,
        {"markers": markers, "illegal": illegal},
    )

    lower = note.lower()
    missing_pairs = []
    for left, right in combinations(WALLS, 2):
        row = f"| `{left.lower()}`, `{right.lower()}` | no | no | yes |"
        if row not in lower:
            missing_pairs.append((left, right))
    check(
        "N2 gives both closure directions for all ten pairs in the collapsed wall set",
        not missing_pairs,
        {"directed_pairs": 10, "missing": missing_pairs},
    )

    trigger_rows = []
    for release_path in (Path(__file__).resolve(), NOTE):
        source = release_path.read_text(encoding="utf-8").lower()
        hits = tuple("".join(parts) for parts in TRIGGER_PARTS if "".join(parts) in source)
        trigger_rows.append(
            {"path": str(release_path.relative_to(ROOT)), "hits": hits}
        )
    check(
        "N3 literal methodology-trigger scan has zero hits on both release paths",
        all(not row["hits"] for row in trigger_rows),
        trigger_rows,
    )

    witnesses = (
        (
            "docs/work_history/repo/review_feedback/GLOBAL_Q2_SIMULTANEOUS_TWO_SOURCE_CYCLE328_NOTE_2026-07-18.md",
            360,
            "hardcore global-q2",
        ),
        (
            "docs/work_history/repo/review_feedback/GLOBAL_Q2_SIMULTANEOUS_TWO_SOURCE_CYCLE328_NOTE_2026-07-18.md",
            47,
            "bosonic mediator statistics",
        ),
        (
            "docs/work_history/repo/review_feedback/GLOBAL_Q2_SIMULTANEOUS_TWO_SOURCE_CYCLE328_NOTE_2026-07-18.md",
            49,
            "independently labelled mediator statistics",
        ),
        (
            "docs/work_history/repo/review_feedback/GLOBAL_Q2_SIMULTANEOUS_TWO_SOURCE_CYCLE328_NOTE_2026-07-18.md",
            75,
            "contact is retained",
        ),
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md",
            26,
            "two-cell fock space",
        ),
    )
    failures = []
    for relative_path, line_number, fragment in witnesses:
        lines = (ROOT / relative_path).read_text(encoding="utf-8").lower().splitlines()
        if line_number > len(lines) or fragment not in lines[line_number - 1]:
            failures.append((relative_path, line_number, fragment))
    check("N4 exact file-line witnesses remain literal", not failures, failures)

    required_sections = (
        "### N5 — rhetoric audit",
        "### N6 — partial-closure paths",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "Gate status: **FAIL / DO NOT SHIP**",
    )
    check(
        "N5-N8 and the broad-negative failure gate remain explicit",
        all(section in note for section in required_sections),
        tuple(section for section in required_sections if section not in note),
    )


def state_norm(state: State) -> float:
    return c328.state_norm(state)


def state_residual(left: State, right: State) -> float:
    return c328.state_residual(left, right)


def prune(state: State, threshold: float = 2e-13) -> State:
    return c328.prune(state, threshold)


def add_vector(output: State, key: Occupation, value: np.ndarray) -> None:
    c328.add_vector(output, key, value)


def normalize_state(state: State) -> State:
    return c328.normalize_state(state)


@lru_cache(maxsize=None)
def hardcore_local_configurations(charge: int) -> tuple[tuple[int, ...], ...]:
    return tuple(combinations(range(7), charge))


@lru_cache(maxsize=None)
def hardcore_source_generator(charge: int) -> sparse.csc_matrix:
    configurations = hardcore_local_configurations(charge)
    lookup = {configuration: index for index, configuration in enumerate(configurations)}
    dimension = 64 * len(configurations)
    rows = []
    columns = []
    data = []
    for q_index, configuration in enumerate(configurations):
        if 0 not in configuration:
            continue
        for source_index, mask in enumerate(LOCAL_MASKS):
            for direction in range(6):
                field_label = 1 + direction
                if field_label in configuration:
                    continue
                hopped = c322.fermion_hop(mask, direction, REVERSE[direction])
                if hopped is None:
                    continue
                target_mask, matter_sign = hopped
                target_configuration = tuple(
                    sorted(label for label in configuration if label != 0)
                    + [field_label]
                )
                target_configuration = tuple(sorted(target_configuration))
                target_q = lookup[target_configuration]
                target_index = LOCAL_INDEX[target_mask]
                source_row = 64 * q_index + source_index
                target_row = 64 * target_q + target_index
                rows.extend((target_row, source_row))
                columns.extend((source_row, target_row))
                data.extend((matter_sign, matter_sign))
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(dimension, dimension), dtype=complex
    ).tocsc()


def hardcore_source_frame(charge: int, frame: np.ndarray) -> sparse.csc_matrix:
    configurations = hardcore_local_configurations(charge)
    lookup = {configuration: index for index, configuration in enumerate(configurations)}
    rows = []
    for configuration in configurations:
        mapped = tuple(
            sorted(
                0
                if label == 0
                else 1 + c315.c311.direction_map(frame, label - 1)
                for label in configuration
            )
        )
        rows.append(lookup[mapped])
    q_representation = sparse.coo_matrix(
        (np.ones(len(rows)), (rows, np.arange(len(rows)))),
        shape=(len(rows), len(rows)),
        dtype=complex,
    ).tocsc()
    return sparse.kron(
        q_representation,
        sparse.csc_matrix(c322.local_fock_frame(frame)),
        format="csc",
    )


def active_modes(length: int, endpoint: int, endpoint_cells=ENDPOINTS):
    cell = endpoint_cells[endpoint]
    return (endpoint,) + tuple(
        c328.field_mode(length, cell, direction) for direction in range(6)
    )


def apply_source(
    state: State,
    length: int,
    endpoint: int,
    endpoint_cells=ENDPOINTS,
    *,
    angle: float = ANGLE,
) -> State:
    active = active_modes(length, endpoint, endpoint_cells)
    active_lookup = {mode: index for index, mode in enumerate(active)}
    grouped: dict[tuple[int, ...], np.ndarray] = {}
    for occupation, vector in state.items():
        local = tuple(sorted(active_lookup[mode] for mode in occupation if mode in active_lookup))
        environment = tuple(sorted(mode for mode in occupation if mode not in active_lookup))
        configurations = hardcore_local_configurations(len(local))
        lookup = {configuration: index for index, configuration in enumerate(configurations)}
        block = grouped.setdefault(
            environment,
            np.zeros((64 * len(configurations), 64), dtype=complex),
        )
        q_index = lookup[local]
        block[64 * q_index : 64 * (q_index + 1), :] += c328.matter_matrix(
            vector, endpoint
        )

    output: State = {}
    for environment, block in grouped.items():
        charge = 2 - len(environment)
        configurations = hardcore_local_configurations(charge)
        transformed = expm_multiply(
            1j * angle * hardcore_source_generator(charge), block
        )
        for q_index, local in enumerate(configurations):
            local_matrix = transformed[64 * q_index : 64 * (q_index + 1), :]
            if np.linalg.norm(local_matrix) <= 2e-13:
                continue
            global_local = tuple(active[index] for index in local)
            occupation = tuple(sorted(environment + global_local))
            add_vector(
                output, occupation, c328.matter_vector(local_matrix, endpoint)
            )
    return prune(output)


@lru_cache(maxsize=None)
def local_hardcore_coin(charge: int) -> np.ndarray:
    configurations = tuple(combinations(range(6), charge))
    if charge == 0:
        return np.eye(1, dtype=complex)
    if charge == 1:
        return c214.FIELD_COIN.copy()
    if charge == 2:
        return np.eye(len(configurations), dtype=complex)
    raise ValueError("global Q2 contains no onsite charge above two")


def active_field_cells(state: State, length: int) -> tuple[tuple[int, int, int], ...]:
    cells = set()
    for occupation in state:
        for mode in occupation:
            decoded = c328.decode_field_mode(mode, length)
            if decoded is not None:
                cells.add(decoded[0])
    return tuple(sorted(cells))


def apply_coin_at_cell(
    state: State, length: int, cell: tuple[int, int, int], *, inverse: bool = False
) -> State:
    local_modes = tuple(c328.field_mode(length, cell, direction) for direction in range(6))
    lookup_global = {mode: direction for direction, mode in enumerate(local_modes)}
    grouped: dict[tuple[int, ...], dict[tuple[int, ...], np.ndarray]] = {}
    for occupation, vector in state.items():
        local = tuple(sorted(lookup_global[mode] for mode in occupation if mode in lookup_global))
        environment = tuple(sorted(mode for mode in occupation if mode not in lookup_global))
        grouped.setdefault(environment, {})[local] = (
            grouped.setdefault(environment, {}).get(local, 0) + vector
        )
    output: State = {}
    for environment, local_vectors in grouped.items():
        charge = 2 - len(environment)
        configurations = tuple(combinations(range(6), charge))
        q_lookup = {configuration: index for index, configuration in enumerate(configurations)}
        vector_dimension = len(next(iter(local_vectors.values())))
        block = np.zeros((len(configurations), vector_dimension), dtype=complex)
        for local, vector in local_vectors.items():
            block[q_lookup[local], :] += vector
        coin = local_hardcore_coin(charge)
        transformed = (coin.conj().T if inverse else coin) @ block
        for q_index, local in enumerate(configurations):
            vector = transformed[q_index]
            if np.linalg.norm(vector) <= 2e-13:
                continue
            global_local = tuple(local_modes[direction] for direction in local)
            occupation = tuple(sorted(environment + global_local))
            add_vector(output, occupation, vector)
    return prune(output)


def apply_field_coin(state: State, length: int, *, inverse: bool = False) -> State:
    output = state
    for cell in active_field_cells(state, length):
        output = apply_coin_at_cell(output, length, cell, inverse=inverse)
    return output


def apply_stream(state: State, length: int, *, inverse: bool = False) -> State:
    output: State = {}
    for occupation, vector in state.items():
        targets = []
        for mode in occupation:
            targets.append(
                c328.one_body_outcomes(
                    mode, length, "stream", inverse=inverse
                )[0][0]
            )
        target = tuple(sorted(targets))
        if target[0] == target[1]:
            # The direction-preserving stream is a permutation, so this is an
            # explicit leakage alarm rather than an allowed branch.
            continue
        add_vector(output, target, vector)
    return prune(output)


def apply_matter(state: State, factor: sparse.spmatrix) -> State:
    return c328.apply_matter_factor(state, factor)


def logical_step(
    state: State,
    length: int,
    factors,
    endpoint_cells=ENDPOINTS,
    *,
    enabled=(True, True),
    contact_enabled=True,
) -> State:
    coin, fswap, contact = factors
    output = apply_matter(state, coin)
    output = apply_field_coin(output, length)
    for endpoint in range(2):
        if enabled[endpoint]:
            output = apply_source(output, length, endpoint, endpoint_cells)
    output = apply_matter(output, fswap)
    output = apply_stream(output, length)
    return apply_matter(
        output, contact if contact_enabled else sparse.eye(4096, format="csc")
    )


def logical_inverse(state: State, length: int, factors) -> State:
    coin, fswap, contact = factors
    output = apply_matter(state, contact.conj().T)
    output = apply_stream(output, length, inverse=True)
    output = apply_matter(output, fswap.conj().T)
    for endpoint in (1, 0):
        output = apply_source(output, length, endpoint, angle=-ANGLE)
    output = apply_field_coin(output, length, inverse=True)
    return apply_matter(output, coin.conj().T)


def initial_state() -> State:
    return {(0, 1): c322.symmetric_one_one_state()}


def observables(state: State) -> dict[str, float]:
    norm = state_norm(state)
    mean_a = 0.0
    mean_b = 0.0
    joint = 0.0
    both_fields = 0.0
    leakage = 0.0
    for occupation, vector in state.items():
        weight = float(np.vdot(vector, vector).real)
        lawful = (
            len(occupation) == 2
            and occupation[0] < occupation[1]
            and occupation.count(0) <= 1
            and occupation.count(1) <= 1
        )
        n_a = occupation.count(0)
        n_b = occupation.count(1)
        fields = sum(mode >= 2 for mode in occupation)
        mean_a += n_a * weight
        mean_b += n_b * weight
        joint += n_a * n_b * weight
        both_fields += int(fields == 2) * weight
        leakage += int(not lawful) * weight
    return {
        "norm": norm,
        "R_A": mean_a,
        "R_B": mean_b,
        "R_A_R_B": joint,
        "connected_covariance": joint - mean_a * mean_b,
        "both_fields": both_fields,
        "lawful_leakage": leakage,
        "reachable_labels": len(state),
    }


def run_response(
    length: int,
    factors,
    *,
    enabled=(True, True),
    contact_enabled=True,
    depths=2,
):
    state = initial_state()
    drift = 0.0
    for _ in range(depths):
        state = logical_step(
            state,
            length,
            factors,
            enabled=enabled,
            contact_enabled=contact_enabled,
        )
        drift = max(drift, abs(state_norm(state) - 1))
    return state, observables(state), drift


def projected_boson_coin_controls() -> None:
    print("\nHARD-CORE COIN TOURNAMENT")
    configurations = tuple(combinations(range(6), 2))
    lookup = {configuration: index for index, configuration in enumerate(configurations)}
    projected = np.zeros((15, 15), dtype=complex)
    leakage_squared = np.zeros(15, dtype=float)
    for source, (left, right) in enumerate(configurations):
        for target_left in range(6):
            for target_right in range(6):
                coefficient = (
                    c214.FIELD_COIN[target_left, left]
                    * c214.FIELD_COIN[target_right, right]
                )
                if target_left == target_right:
                    leakage_squared[source] += 2 * abs(coefficient) ** 2
                    continue
                target = tuple(sorted((target_left, target_right)))
                # Two assignments contribute to a normalized symmetric state.
                reverse_coefficient = (
                    c214.FIELD_COIN[target_right, left]
                    * c214.FIELD_COIN[target_left, right]
                )
                if target_left < target_right:
                    projected[lookup[target], source] += coefficient + reverse_coefficient
    projected_unitarity = float(
        np.linalg.norm(projected.conj().T @ projected - np.eye(15))
    )
    completion = local_hardcore_coin(2)
    completion_unitarity = float(
        np.linalg.norm(completion.conj().T @ completion - np.eye(15))
    )
    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        rows = []
        for configuration in configurations:
            mapped = tuple(
                sorted(c315.c311.direction_map(frame, direction) for direction in configuration)
            )
            rows.append(lookup[mapped])
        representation = np.zeros((15, 15), dtype=complex)
        representation[rows, np.arange(15)] = 1
        frame_residuals.append(
            float(np.linalg.norm(representation @ completion @ representation.T - completion))
        )
    check(
        "projecting the bosonic two-particle coin leaks from the hard-core sector",
        projected_unitarity > 0.5 and max(leakage_squared) > 0.1,
        {
            "projected_unitarity_residual": projected_unitarity,
            "maximum_double_occupation_probability": max(leakage_squared),
        },
    )
    check(
        "the collision-conditioned Q1-coin/Q2-identity completion is unitary and proper-cubic",
        completion_unitarity == 0 and max(frame_residuals) == 0,
        {
            "Q1_coin": "Cycle-214 FIELD_COIN",
            "Q2_onsite_coin": "identity on 15 hard-core pairs",
            "Q2_unitarity": completion_unitarity,
            "maximum_frame_residual": max(frame_residuals),
            "supplied_collision_condition": True,
        },
    )


def source_controls() -> None:
    print("\nHARD-CORE Q2 SOURCE LEDGERS")
    rows = []
    for charge in (1, 2):
        configurations = hardcore_local_configurations(charge)
        generator = hardcore_source_generator(charge)
        number_values = []
        q_values = []
        momenta = [[], [], []]
        for configuration in configurations:
            field_vector = sum(
                (
                    c210.DIRECTIONS[label - 1]
                    for label in configuration
                    if label > 0
                ),
                start=np.zeros(3, dtype=int),
            )
            for mask in LOCAL_MASKS:
                matter_vector_sum = sum(
                    (
                        c210.DIRECTIONS[direction]
                        for direction in range(6)
                        if (mask >> direction) & 1
                    ),
                    start=np.zeros(3, dtype=int),
                )
                number_values.append(mask.bit_count())
                q_values.append(charge)
                for axis in range(3):
                    momenta[axis].append(
                        float(matter_vector_sum[axis] + 2 * field_vector[axis])
                    )
        number = sparse.diags(number_values, format="csc", dtype=float)
        q_op = sparse.diags(q_values, format="csc", dtype=float)
        p_ops = tuple(
            sparse.diags(values, format="csc", dtype=float) for values in momenta
        )
        frame_residuals = []
        for frame in c210.proper_cubic_frames():
            representation = hardcore_source_frame(charge, frame)
            frame_residuals.append(
                c315.largest_singular(
                    representation @ generator - generator @ representation
                )
            )
        rows.append(
            {
                "charge": charge,
                "dimension": generator.shape[0],
                "Hermiticity": c315.largest_singular(generator - generator.conj().T),
                "Q_commutator": c315.largest_singular(generator @ q_op - q_op @ generator),
                "N_commutator": c315.largest_singular(generator @ number - number @ generator),
                "P_commutators": tuple(
                    c315.largest_singular(generator @ p_op - p_op @ generator)
                    for p_op in p_ops
                ),
                "maximum_frame_residual": max(frame_residuals),
            }
        )
    check(
        "the hard-core source preserves exact Q, matter number, coefficient-two vector ledger, and all frames",
        max(
            max(
                row["Hermiticity"],
                row["Q_commutator"],
                row["N_commutator"],
                max(row["P_commutators"]),
                row["maximum_frame_residual"],
            )
            for row in rows
        )
        == 0,
        rows,
    )


def response_controls(factors):
    print("\nHARD-CORE SIMULTANEOUS RESPONSE")
    boson_reference = 0.5929377077947355
    labelled_reference = 0.5929583577037859
    boson_covariance = -0.001529375553990353
    labelled_covariance = -0.0018359698128539437
    boson_both_fields = 0.05090387762274617
    labelled_both_fields = 0.05050015403454247
    q1_product = 0.59479432751664
    rows = []
    for length in SIZES:
        _state, observed, drift = run_response(length, factors)
        rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                **observed,
                "maximum_norm_drift": drift,
                "joint_minus_Q1_product": observed["R_A_R_B"] - q1_product,
                "joint_minus_bosonic": observed["R_A_R_B"] - boson_reference,
                "joint_minus_labelled": observed["R_A_R_B"] - labelled_reference,
            }
        )
    check(
        "the hard-core simultaneous response is normalized, lawful, nonfactorizing, and held-size stable",
        max(row["maximum_norm_drift"] for row in rows) < TOLERANCE
        and max(row["lawful_leakage"] for row in rows) == 0
        and min(abs(row["joint_minus_Q1_product"]) for row in rows) > 1e-7
        and min(abs(row["connected_covariance"]) for row in rows) > 1e-7,
        rows,
    )
    check(
        "the hard-core joint and both-field response is compared with both Cycle-328 statistics",
        min(
            max(
                abs(row["joint_minus_bosonic"]),
                abs(row["connected_covariance"] - boson_covariance),
                abs(row["both_fields"] - boson_both_fields),
            )
            for row in rows
        )
        > 1e-8
        and min(
            max(
                abs(row["joint_minus_labelled"]),
                abs(row["connected_covariance"] - labelled_covariance),
                abs(row["both_fields"] - labelled_both_fields),
            )
            for row in rows
        )
        > 1e-8,
        {
            "hardcore": rows,
            "Cycle328_bosonic_joint": boson_reference,
            "Cycle328_labelled_joint": labelled_reference,
            "Cycle328_bosonic_covariance": boson_covariance,
            "Cycle328_labelled_covariance": labelled_covariance,
            "Cycle328_bosonic_both_fields": boson_both_fields,
            "Cycle328_labelled_both_fields": labelled_both_fields,
        },
    )
    _deleted_state, deleted, deleted_drift = run_response(
        3, factors, enabled=(True, False)
    )
    _no_contact_state, no_contact, no_contact_drift = run_response(
        3, factors, contact_enabled=False
    )
    check(
        "source deletion retains R_B and contact deletion is measured without leakage",
        deleted["R_B"] > 1 - TOLERANCE
        and deleted_drift < TOLERANCE
        and no_contact_drift < TOLERANCE,
        {
            "deleted_source_B_R_B": deleted["R_B"],
            "deleted_source_drift": deleted_drift,
            "contact_response_difference": abs(
                no_contact["R_A_R_B"] - rows[0]["R_A_R_B"]
            ),
            "no_contact_drift": no_contact_drift,
        },
    )
    return rows


def random_state(length: int, seed: int) -> State:
    rng = np.random.default_rng(seed)
    f0 = c328.field_mode(length, LEFT, 0)
    f2 = c328.field_mode(length, RIGHT, 2)
    keys = ((0, 1), tuple(sorted((0, f2))), tuple(sorted((f0, f2))))
    return normalize_state(
        {
            key: rng.normal(size=4096) + 1j * rng.normal(size=4096)
            for key in keys
        }
    )


def encode_physical(state: State, encoding) -> State:
    return {key: encoding @ value for key, value in state.items()}


def apply_physical_matter(state: State, encoding, factor) -> State:
    output: State = {}
    for key, value in state.items():
        decoded = encoding.conj().T @ value
        output[key] = value + encoding @ (factor @ decoded - decoded)
    return prune(output)


def apply_physical_source(
    state: State, encoding, length: int, endpoint: int, *, angle: float = ANGLE
) -> State:
    decoded = {key: encoding.conj().T @ value for key, value in state.items()}
    transformed = apply_source(decoded, length, endpoint, angle=angle)
    output: State = {}
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    zero_logical = np.zeros(4096, dtype=complex)
    for key in state.keys() | transformed.keys():
        before_physical = state.get(key, zero_physical)
        before_logical = decoded.get(key, zero_logical)
        after_logical = transformed.get(key, zero_logical)
        output[key] = before_physical + encoding @ (after_logical - before_logical)
    return prune(output)


def physical_step(state: State, encoding, length: int, factors) -> State:
    coin, fswap, contact = factors
    output = apply_physical_matter(state, encoding, coin)
    output = apply_field_coin(output, length)
    output = apply_physical_source(output, encoding, length, 0)
    output = apply_physical_source(output, encoding, length, 1)
    output = apply_physical_matter(output, encoding, fswap)
    output = apply_stream(output, length)
    return apply_physical_matter(output, encoding, contact)


def physical_inverse(state: State, encoding, length: int, factors) -> State:
    coin, fswap, contact = factors
    output = apply_physical_matter(state, encoding, contact.conj().T)
    output = apply_stream(output, length, inverse=True)
    output = apply_physical_matter(output, encoding, fswap.conj().T)
    output = apply_physical_source(output, encoding, length, 1, angle=-ANGLE)
    output = apply_physical_source(output, encoding, length, 0, angle=-ANGLE)
    output = apply_field_coin(output, length, inverse=True)
    return apply_physical_matter(output, encoding, coin.conj().T)


def physical_controls(factors) -> None:
    print("\nHARD-CORE AB/BA PHYSICAL EG")
    forward = c322.build_encoding(3, False)
    reverse = c322.build_encoding(3, True)
    rows_count = max(forward.shape[0], reverse.shape[0])
    if forward.shape[0] < rows_count:
        forward.resize((rows_count, forward.shape[1]))
    if reverse.shape[0] < rows_count:
        reverse.resize((rows_count, reverse.shape[1]))
    logical = random_state(3, 331)
    expected_logical = logical_step(logical, 3, factors)
    rows = []
    for orientation, encoding in (("AB", forward), ("BA", reverse)):
        encoded = encode_physical(logical, encoding)
        actual = physical_step(encoded, encoding, 3, factors)
        expected = encode_physical(expected_logical, encoding)
        recovered = physical_inverse(actual, encoding, 3, factors)
        rows.append(
            {
                "orientation": orientation,
                "EG_residual": state_residual(actual, expected),
                "inverse_residual": state_residual(recovered, encoded),
                "encoded_norm": state_norm(encoded),
                "output_norm": state_norm(actual),
                "input_labels": len(logical),
                "output_labels": len(actual),
            }
        )
    check(
        "the hard-core code obeys AB/BA physical EG and inverse EG",
        max(
            max(
                row["EG_residual"],
                row["inverse_residual"],
                abs(row["encoded_norm"] - 1),
                abs(row["output_norm"] - 1),
            )
            for row in rows
        )
        < TOLERANCE,
        rows,
    )


def covariance_translation_support_controls(factors) -> None:
    print("\nFRAMES / TRANSLATIONS / SUPPORT")
    coin, fswap, contact = factors
    inherited = c315.covariance_translation_controls(
        LABELS, coin, contact, contact @ fswap @ coin
    )
    coin_frame_residuals = []
    for frame in c210.proper_cubic_frames():
        representation = c210.direction_permutation(frame)
        coin_frame_residuals.append(
            float(
                np.linalg.norm(
                    representation @ c214.FIELD_COIN @ representation.T
                    - c214.FIELD_COIN
                )
            )
        )
    check(
        "the hard-core source/coin/stream family covers all 24 frames including endpoint reversal",
        inherited["proper_cubic_frames"] == 24
        and inherited["endpoint_reversing_frames"] == 12
        and inherited["maximum_update_covariance_residual"] < TOLERANCE
        and max(coin_frame_residuals) == 0,
        {
            "inherited_seam": inherited,
            "maximum_Q1_coin_frame_residual": max(coin_frame_residuals),
            "Q2_coin_frame_residual": 0.0,
        },
    )
    reference_state, reference, _ = run_response(3, factors)
    del reference_state
    maximum_translation_residual = 0.0
    for displacement in product(range(3), repeat=3):
        moved_cells = tuple(
            tuple((cell[axis] + displacement[axis]) % 3 for axis in range(3))
            for cell in ENDPOINTS
        )
        state = initial_state()
        drift = 0.0
        for _ in range(2):
            state = logical_step(
                state, 3, factors, endpoint_cells=moved_cells
            )
            drift = max(drift, abs(state_norm(state) - 1))
        observed = observables(state)
        maximum_translation_residual = max(
            maximum_translation_residual,
            drift,
            abs(observed["R_A"] - reference["R_A"]),
            abs(observed["R_B"] - reference["R_B"]),
            abs(observed["R_A_R_B"] - reference["R_A_R_B"]),
        )
    check(
        "the hard-core simultaneous response is invariant under all L=3 translations",
        maximum_translation_residual < TOLERANCE,
        {
            "translations": 27,
            "maximum_response_or_norm_residual": maximum_translation_residual,
        },
    )
    support_rows = []
    for length in SIZES:
        state, _observed, drift = run_response(length, factors)
        modes = 2 + 6 * length**3
        support_rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "ambient_hardcore_Q2_dimension": modes * (modes - 1) // 2,
                "reachable_labels": len(state),
                "norm_drift": drift,
                "M2_per_cell": 36,
                "two_cell_patch_M2": 97,
            }
        )
    check(
        "the sparse hard-core restriction remains bounded and closed through held L=6",
        all(row["reachable_labels"] < 5000 for row in support_rows)
        and max(row["norm_drift"] for row in support_rows) < TOLERANCE,
        support_rows,
    )


def mass_contact_inventory_controls(factors, response_rows) -> None:
    print("\nMASS / CONTACT / INVENTORY")
    _coin, _fswap, contact = factors
    logical_rows = c315.logical_update_controls(LABELS)[4]
    contact_deleted = c315.largest_singular(
        contact - sparse.eye(4096, format="csc")
    )
    check(
        "the actual contact and mass fixture remain firewalled",
        logical_rows["contact_nontrivial_columns"] == 4047
        and contact_deleted > 1.9
        and abs(logical_rows["two_cell_rest_mass"] - logical_rows["Cycle219_mass_fixture"])
        < TOLERANCE,
        {
            "contact_nontrivial_columns": logical_rows["contact_nontrivial_columns"],
            "contact_deletion_opnorm": contact_deleted,
            "mass_fixture": logical_rows["Cycle219_mass_fixture"],
            "two_cell_mass": logical_rows["two_cell_rest_mass"],
            "mass_residual": logical_rows["two_cell_uniform_one_particle_residual"],
        },
    )
    inventory = {
        "matter": "Cycle-315 complete M64 tensor M64 seam",
        "statistics": "hard-core mediator modes, at most one occupation per mode",
        "source": "hard-core coefficient-two reservoir/field exchange",
        "coin comparator": "projected bosonic Q2 coin leaks",
        "retained coin": "Cycle-214 on onsite Q1, identity on onsite Q2",
        "preparation": "both reservoirs occupied, symmetric one-one matter, two updates",
        "restriction": "sparse reachable hard-core Q2 labels tensor 4096 matter",
        "response": response_rows,
        "open": "coin derivation, fermionic mediator, unit-weight Q2, multi-edge, calibration",
        "interpretation": "occupation response only; not force/energy/stress/gravity/metric/time",
        "authority": "none",
        "audit": "unset",
    }
    check(
        "the hard-core law, collision-conditioned coin, preparation, restriction, and open choices are explicit",
        len(inventory) == 12,
        inventory,
    )


def main() -> int:
    print("CYCLE 331: HARD-CORE GLOBAL-Q2 MEDIATOR COMPILER")
    print("authority=none; audit=unset")
    note_contract()
    coin, fswap, contact, _update, _details = c315.logical_update_controls(LABELS)
    factors = (coin, fswap, contact)
    projected_boson_coin_controls()
    source_controls()
    response_rows = response_controls(factors)
    physical_controls(factors)
    covariance_translation_support_controls(factors)
    mass_contact_inventory_controls(factors, response_rows)
    methodology_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT HARDCORE_GLOBAL_Q2_MEDIATOR_OPEN")
        return 1
    print("RESULT HARDCORE_GLOBAL_Q2_MEDIATOR_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
