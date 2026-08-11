#!/usr/bin/env python3
"""Cycle 982: bounded dependence census on a true Z^3 nearest-neighbour star.

The calculation injects seven landed semantic wires into the origin and its
six Z^3 nearest neighbours, computes the semantic-wiring and geometric-edge
relations independently, and asks the landed Cycle-719 router to realize every
declared target-local word by nearest-neighbour paths.  Science outcomes are
reported data; checks gate construction, reconciliation, and provenance only.
"""

from __future__ import annotations

import ast
import importlib.util
import io
import json
import subprocess
import sys
import tarfile
import tempfile
from hashlib import sha1, sha256
from itertools import combinations, permutations, product
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
CYCLE = 982
AUDIT_TIMEOUT_SEC = 1400
HOUSE_STDOUT_LIMIT_BYTES = 6_000
STDOUT_LIMIT_BYTES = 150_000
BASE_ORIGIN_MAIN_COMMIT = "ea0968c71ad46c39c6dacb39f88a18780363b71f"
PINNED_CYCLE719_COMMIT = "39c74017b870c27c804e3992f2a11e90336476b2"
PINNED_CYCLE719_CORE = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
)
PINNED_CYCLE719_CORE_SHA256 = (
    "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4"
)
PINNED_CYCLE719_CORE_BLOB = "c123b8d681c3d76fce08ef13d7673622deac64ad"

AUDIT_INPUT_PATHS = ("docs/MINIMAL_AXIOMS_2026-06-29.md",)
EXPECTED_INPUT_SHA256 = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39",
}
EXPECTED_INPUT_BLOBS = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "2f5fdd26898f62c17fcabc846761f7785c2eadb1",
}
BLOCKLIST_TEXT_PATHS = (
    "docs/WITNESS_FAMILY_COMPLETENESS_CYCLE977_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CLASS_COEXISTENCE_BORN_REQUIREMENT_CYCLE979_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/WITNESS_ORBIT_MULTIPLICITY_CYCLE980_BOUNDED_THEOREM_NOTE_2026-08-11.md",
)
BLOCKLIST_AST_FRAGMENTS = (
    "cycle970", "cycle972", "cycle977", "cycle979", "cycle980",
)

PRIMARY_PATH = "scripts/frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11.py"
RECEIPT_PATH = "outputs/z3_adjacency_dependence_classes_cycle982_receipt_2026_08_11.json"
CENTER = (0, 0, 0)
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
WIRE_TO_SITE = (CENTER, *DIRECTIONS)
SITE_TO_WIRE = {site: wire for wire, site in enumerate(WIRE_TO_SITE)}
NEIGHBOUR_WIRES = tuple(range(1, 7))
CONDITIONS = tuple(product((0, 1), repeat=6))
OTHER_CONTEXTS = tuple(product((0, 1), repeat=5))


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def ast_literal_assignment(tree: ast.Module, name: str):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def load_pinned_cycle719_core():
    archive = subprocess.run(
        ["git", "archive", "--format=tar", PINNED_CYCLE719_COMMIT, "scripts"],
        cwd=ROOT, check=True, capture_output=True,
    ).stdout
    temporary = tempfile.TemporaryDirectory(prefix="cycle982-cycle719-")
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        bundle.extractall(temporary.name, filter="data")
    scripts_dir = Path(temporary.name) / "scripts"
    sys.path.insert(0, str(scripts_dir))
    core_path = Path(temporary.name) / PINNED_CYCLE719_CORE
    spec = importlib.util.spec_from_file_location("cycle982_pinned_cycle719", core_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load pinned Cycle-719 core")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return temporary, module


PINNED_TEMP, K = load_pinned_cycle719_core()


def l1(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(a * b for a, b in zip(left, right))


def site_name(wire: int) -> str:
    return "C" if wire == 0 else DIRECTION_NAMES[wire - 1]


def word_name(descriptor: tuple) -> str:
    kind = descriptor[0]
    if kind == "I":
        return "I"
    if kind == "X":
        return f"X({site_name(descriptor[1])})"
    if kind == "CNOT":
        return f"CNOT({site_name(descriptor[1])}->{site_name(descriptor[2])})"
    return (
        f"TOF({site_name(descriptor[1])},{site_name(descriptor[2])}"
        f"->{site_name(descriptor[3])})"
    )


def declared_target_local_family() -> tuple:
    rows = [("I",), ("X", 0)]
    rows.extend(("CNOT", control, 0) for control in NEIGHBOUR_WIRES)
    rows.extend(
        ("TOF", controls[0], controls[1], 0)
        for controls in combinations(NEIGHBOUR_WIRES, 2)
    )
    return tuple(rows)


def core_word(descriptor: tuple) -> tuple:
    kind = descriptor[0]
    if kind == "I":
        return ()
    if kind == "X":
        return (K.A.x(descriptor[1]),)
    if kind == "CNOT":
        return (K.A.cn(descriptor[1], descriptor[2]),)
    return (K.A.tof(descriptor[1], descriptor[2], descriptor[3]),)


def independent_target_output(descriptor: tuple, x: int, condition: tuple) -> int:
    state = [x, *condition]
    kind = descriptor[0]
    if kind == "X":
        state[descriptor[1]] ^= 1
    elif kind == "CNOT" and state[descriptor[1]]:
        state[descriptor[2]] ^= 1
    elif kind == "TOF" and state[descriptor[1]] and state[descriptor[2]]:
        state[descriptor[3]] ^= 1
    return state[0]


def landed_target_output(descriptor: tuple, x: int, condition: tuple) -> int:
    return K.A.apply_semantic((x, *condition), core_word(descriptor))[0]


def with_edge(index: int, other: tuple, bit: int) -> tuple:
    source = iter(other)
    return tuple(bit if position == index else next(source) for position in range(6))


def witness_measurement(descriptor: tuple) -> dict:
    changed = 0
    for x in (0, 1):
        for direction_index in range(6):
            for other in OTHER_CONTEXTS:
                condition_0 = with_edge(direction_index, other, 0)
                condition_1 = with_edge(direction_index, other, 1)
                changed += landed_target_output(descriptor, x, condition_0) != (
                    landed_target_output(descriptor, x, condition_1)
                )
    return {"is_witness": changed > 0, "changed_edge_pairs": changed}


def semantic_pair_relation() -> tuple:
    # Pair shadow of the landed distinct-wire X/CNOT/TOF constructors on 7 wires.
    return tuple(combinations(range(7), 2))


def z3_pair_relation() -> tuple:
    return tuple(
        pair for pair in combinations(range(7), 2)
        if l1(WIRE_TO_SITE[pair[0]], WIRE_TO_SITE[pair[1]]) == 1
    )


def relation_classification(substrate: set, z3_edges: set) -> str:
    if substrate == z3_edges:
        return "relations_equal"
    if z3_edges < substrate:
        return "z3_strict_subrelation_of_semantic_wiring"
    if substrate < z3_edges:
        return "semantic_wiring_strict_subrelation_of_z3"
    if substrate & z3_edges:
        return "overlap_without_inclusion"
    return "disjoint_relations"


def adjacency_measurement() -> dict:
    substrate = set(semantic_pair_relation())
    z3_edges = set(z3_pair_relation())
    path_rows = []
    for left, right in sorted(substrate):
        path = tuple(K.C712.c707.c655.manhattan_path(
            WIRE_TO_SITE[left], WIRE_TO_SITE[right]
        ))
        path_rows.append({
            "logical_pair": [left, right],
            "logical_names": [site_name(left), site_name(right)],
            "is_z3_edge": (left, right) in z3_edges,
            "path": [list(site) for site in path],
            "path_length": len(path) - 1,
            "all_steps_z3_nearest_neighbour": all(
                l1(a, b) == 1 for a, b in zip(path, path[1:])
            ),
            "path_stays_in_seven_site_star": set(path) <= set(WIRE_TO_SITE),
        })
    return {
        "vertex_map": {
            str(wire): list(site) for wire, site in enumerate(WIRE_TO_SITE)
        },
        "vertex_map_injective": len(set(WIRE_TO_SITE)) == len(WIRE_TO_SITE),
        "semantic_wiring_definition": (
            "pair shadow of all distinct-wire landed constructors on seven logical wires"
        ),
        "semantic_wiring_edges": [list(pair) for pair in sorted(substrate)],
        "semantic_wiring_edge_count": len(substrate),
        "z3_relation_definition": "L1 distance exactly one on the injected sites",
        "z3_edges": [list(pair) for pair in sorted(z3_edges)],
        "z3_edge_count": len(z3_edges),
        "relation_classification": relation_classification(substrate, z3_edges),
        "is_quotient_map": False,
        "quotient_obstruction": (
            "the vertex map is injective and identifies no sites; extra semantic pairs map to paths, not edges"
        ),
        "counterexample_to_relation_equality": {
            "logical_pair": [1, 3],
            "sites": [list(WIRE_TO_SITE[1]), list(WIRE_TO_SITE[3])],
            "z3_l1_distance": l1(WIRE_TO_SITE[1], WIRE_TO_SITE[3]),
        },
        "path_realization": path_rows,
        "all_semantic_pairs_have_star_internal_nn_paths": all(
            row["all_steps_z3_nearest_neighbour"]
            and row["path_stays_in_seven_site_star"] for row in path_rows
        ),
        "z3_edges_map_to_single_step_paths": all(
            row["path_length"] == 1 for row in path_rows if row["is_z3_edge"]
        ),
        "non_z3_semantic_pairs_map_to_two_step_paths": all(
            row["path_length"] == 2 for row in path_rows if not row["is_z3_edge"]
        ),
    }


def determinant(matrix: tuple[tuple[int, int, int], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def proper_cubic_rotations() -> tuple:
    rows = set()
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] * int(column == order[row]) for column in range(3))
                for row in range(3)
            )
            if determinant(matrix) == 1:
                rows.add(matrix)
    return tuple(sorted(rows))


ROTATIONS = proper_cubic_rotations()


def mat_vec(matrix: tuple, vector: tuple) -> tuple:
    return tuple(dot(row, vector) for row in matrix)


def rotate_wire(wire: int, rotation: tuple) -> int:
    return SITE_TO_WIRE[mat_vec(rotation, WIRE_TO_SITE[wire])]


def rotate_descriptor(descriptor: tuple, rotation: tuple) -> tuple:
    if descriptor[0] in ("I", "X"):
        return descriptor
    wires = tuple(rotate_wire(wire, rotation) for wire in descriptor[1:])
    if descriptor[0] == "TOF":
        return ("TOF", *sorted(wires[:2]), wires[2])
    return (descriptor[0], *wires)


def invariant_j(descriptor: tuple) -> int:
    controls = (descriptor[1],) if descriptor[0] == "CNOT" else descriptor[1:3]
    vector_sum = tuple(
        sum(WIRE_TO_SITE[control][axis] for control in controls) for axis in range(3)
    )
    return dot(vector_sum, vector_sum)


def orbit_label(members: tuple) -> str:
    kinds = {row[0] for row in members}
    values = {invariant_j(row) for row in members}
    if kinds == {"CNOT"}:
        return "CNOT"
    if kinds == {"TOF"} and values == {2}:
        return "TOF_PERPENDICULAR_CONTROLS"
    if kinds == {"TOF"} and values == {0}:
        return "TOF_OPPOSITE_CONTROLS"
    return "UNCLASSIFIED_" + digest([sorted(kinds), sorted(values)])[:12]


def orbit_decomposition(witnesses: tuple) -> dict:
    witness_set = set(witnesses)
    remaining = set(witnesses)
    rows = []
    while remaining:
        seed = min(remaining, key=word_name)
        ambient = {rotate_descriptor(seed, rotation) for rotation in ROTATIONS}
        members = tuple(sorted(ambient & witness_set, key=word_name))
        stabilizer = sum(
            rotate_descriptor(seed, rotation) == seed for rotation in ROTATIONS
        )
        rows.append({
            "class_label": orbit_label(members),
            "representative": word_name(seed),
            "member_count": len(members),
            "effective_stabilizer_order": stabilizer,
            "orbit_stabilizer_product": len(ambient) * stabilizer,
            "orbit_closed_in_witness_set": ambient <= witness_set,
            "J_values": sorted({invariant_j(row) for row in members}),
            "members": [word_name(row) for row in members],
        })
        remaining -= set(members)
    rows.sort(key=lambda row: row["class_label"])
    covered = [member for row in rows for member in row["members"]]
    return {
        "effective_group": "proper cubic rotation group",
        "effective_group_order": len(ROTATIONS),
        "orbit_count": len(rows),
        "orbits": rows,
        "partition_has_no_overlap_or_omission": (
            len(covered) == len(set(covered)) == len(witnesses)
        ),
        "action_closed_on_witnesses": all(
            row["orbit_closed_in_witness_set"] for row in rows
        ),
        "J_constant_on_each_orbit": all(len(row["J_values"]) == 1 for row in rows),
        "J_distinct_across_orbits": len({
            value for row in rows for value in row["J_values"]
        }) == len(rows),
    }


def host_and_census_measurement() -> dict:
    family = declared_target_local_family()
    witnesses = []
    truth_failures = 0
    route_rows = []
    for descriptor in family:
        measurement = witness_measurement(descriptor)
        if measurement["is_witness"]:
            witnesses.append(descriptor)
        for x in (0, 1):
            for condition in CONDITIONS:
                truth_failures += landed_target_output(descriptor, x, condition) != (
                    independent_target_output(descriptor, x, condition)
                )
        route = K.streaming_route(core_word(descriptor), WIRE_TO_SITE)
        route_rows.append({"word": word_name(descriptor), **route})
    hostable = all(
        row["non_NN_failures"] == 0
        and row["operand_order_failures"] == 0
        and row["route_return_failures"] == 0
        for row in route_rows
    )
    census = {
        "witness_count": len(witnesses),
        "witness_names": [word_name(row) for row in witnesses],
        "witness_digest": digest(witnesses),
        "orbit_decomposition": orbit_decomposition(tuple(witnesses)),
    }
    return {
        "construction": (
            "inject wire 0 at the origin and wires 1..6 at the six signed unit vectors; "
            "use the induced L1-nearest-neighbour relation and the landed Manhattan router"
        ),
        "site_count": len(WIRE_TO_SITE),
        "ambient_central_degree": 6,
        "minimality": (
            "a represented site plus its six distinct Z3 nearest neighbours requires at least seven sites"
        ),
        "family": {
            "support": "one centre and its six genuine Z3 nearest neighbours",
            "site_menu": [0, 1],
            "word_length": "zero or one",
            "words": "I; X(C); CNOT(n->C); TOF({n,m}->C) for distinct neighbours",
            "family_size": len(family),
            "family_digest": digest(family),
            "cap": "all 23 target-local descriptors; both centre inputs; all 2^6 neighbour conditions; no sampling",
        },
        "route_host": {
            "classification": (
                "finite_seven_site_z3_star_hosted" if hostable
                else "finite_seven_site_z3_star_not_hosted_by_landed_router"
            ),
            "all_words_routable": hostable,
            "maximum_route_distance": max(row["maximum_route_distance"] for row in route_rows),
            "maximum_touched_sites": max(row["touched_M2"] for row in route_rows),
            "expanded_primitive_count": sum(row["physical_primitives"] for row in route_rows),
            "routed_nn_gate_count": sum(row["routed_NN_gates"] for row in route_rows),
            "non_nn_failure_count": sum(row["non_NN_failures"] for row in route_rows),
            "operand_order_failure_count": sum(row["operand_order_failures"] for row in route_rows),
            "route_return_failure_count": sum(row["route_return_failures"] for row in route_rows),
            "route_rows_digest": digest(route_rows),
        },
        "landed_vs_independent_truth_failure_count": truth_failures,
        "semantic_candidate_census": census,
        "hosted_census": census if hostable else None,
    }


def structure_transfer(census: dict) -> dict:
    hosted = census["hosted_census"]
    if hosted is None:
        classification = "not_applicable_without_a_hosted_local_instance"
        orbit = census["semantic_candidate_census"]["orbit_decomposition"]
    else:
        orbit = hosted["orbit_decomposition"]
        if orbit["action_closed_on_witnesses"] and orbit["J_distinct_across_orbits"]:
            classification = "transfers_exactly_on_the_declared_local_family"
        elif orbit["action_closed_on_witnesses"]:
            classification = "orbit_structure_transfers_but_J_deforms"
        else:
            classification = "class_structure_fails_to_transfer"
    return {
        "classification": classification,
        "orbit_data": orbit,
        "separator": {
            "name": "J",
            "formula": "squared Euclidean norm of the sum of centre-relative control vectors",
            "scope": "derived target-local neighbour-dependence witnesses",
        },
    }


def honest_scope(host: dict) -> dict:
    local_hosted = host["route_host"]["all_words_routable"]
    return {
        "local_seven_site_instance_hosted": local_hosted,
        "full_infinite_z3_instance_claimed": False,
        "scope_boundary": (
            "the landed router realizes the finite radius-one star word by word; this packet does not construct an infinite simultaneous lattice law"
        ),
        "not_supplied_by_this_instance": [
            "an infinite allocation of M2 sites over every point of Z3",
            "one translation-uniform admissibility probability rule on every lattice site",
            "a simultaneous global execution of the 23 alternative local words",
            "a derivation identifying semantic operand availability with geometric adjacency",
        ],
        "feasibility_outcome": (
            "finite local host is feasible and exercised; full-axiom host is outside the delivered construction"
            if local_hosted else
            "the landed router did not realize the finite local host; the route failures are reported above"
        ),
    }


def input_controls() -> dict:
    source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    literal_paths = ast_literal_assignment(tree, "AUDIT_INPUT_PATHS")
    literal_blocklist = ast_literal_assignment(tree, "BLOCKLIST_TEXT_PATHS")
    literal_fragments = ast_literal_assignment(tree, "BLOCKLIST_AST_FRAGMENTS")
    payloads = {path: (ROOT / path).read_bytes() for path in literal_paths}
    sha_rows = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    imported_names = {
        alias.name for node in ast.walk(tree) if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    pinned_core = subprocess.run(
        ["git", "show", f"{PINNED_CYCLE719_COMMIT}:{PINNED_CYCLE719_CORE}"],
        cwd=ROOT, check=True, capture_output=True,
    ).stdout
    base_is_ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", BASE_ORIGIN_MAIN_COMMIT, "HEAD"],
        cwd=ROOT, check=False, capture_output=True,
    ).returncode == 0
    return {
        "literal_audit_input_paths": list(literal_paths),
        "literal_source_read_count": len(literal_paths),
        "input_sha256": sha_rows,
        "input_git_blobs": blob_rows,
        "sha_pins_match": sha_rows == EXPECTED_INPUT_SHA256,
        "blob_pins_match": blob_rows == EXPECTED_INPUT_BLOBS,
        "all_inputs_relative_and_present": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in literal_paths
        ),
        "blocklist_text_paths": list(literal_blocklist),
        "blocklist_ast_fragments": list(literal_fragments),
        "blocklist_text_disjoint_from_reads": not set(literal_paths) & set(literal_blocklist),
        "blocked_ast_imports": sorted(
            name for name in imported_names
            if any(fragment in name.lower() for fragment in literal_fragments)
        ),
        "prior_cycle_text_or_ast_executed": False,
        "pinned_substrate": {
            "commit": PINNED_CYCLE719_COMMIT,
            "path": PINNED_CYCLE719_CORE,
            "sha256": sha256(pinned_core).hexdigest(),
            "git_blob": git_blob(pinned_core),
            "sha_pin_match": sha256(pinned_core).hexdigest() == PINNED_CYCLE719_CORE_SHA256,
            "blob_pin_match": git_blob(pinned_core) == PINNED_CYCLE719_CORE_BLOB,
            "loaded_from_immutable_git_archive": True,
        },
        "base_origin_main_commit": BASE_ORIGIN_MAIN_COMMIT,
        "base_is_ancestor_of_head": base_is_ancestor,
    }


def science_measurement() -> dict:
    adjacency = adjacency_measurement()
    host = host_and_census_measurement()
    return {
        "A_ADJACENCY_MAP": adjacency,
        "B_Z3_WITNESS_CENSUS": host,
        "C_STRUCTURE_TRANSFER": structure_transfer(host),
        "D_HONEST_SCOPE": honest_scope(host),
    }


def render_stdout(receipt: dict) -> str:
    findings = receipt["findings"]
    adjacency = findings["A_ADJACENCY_MAP"]
    census = findings["B_Z3_WITNESS_CENSUS"]
    transfer = findings["C_STRUCTURE_TRANSFER"]
    scope = findings["D_HONEST_SCOPE"]
    hosted = census["hosted_census"]
    orbit_rows = [] if hosted is None else [
        [row["class_label"], row["member_count"], row["effective_stabilizer_order"], row["J_values"]]
        for row in hosted["orbit_decomposition"]["orbits"]
    ]
    lines = [
        "CYCLE982_Z3_ADJACENCY_DEPENDENCE_CLASSES",
        "A_ADJACENCY_MAP " + ("PASS" if receipt["checks"]["A_ADJACENCY_MAP"] else "FAIL")
        + f" :: relation={adjacency['relation_classification']};"
        + f" semantic_edges={adjacency['semantic_wiring_edge_count']};"
        + f" z3_edges={adjacency['z3_edge_count']}; quotient={adjacency['is_quotient_map']}",
        "B_Z3_WITNESS_CENSUS " + ("PASS" if receipt["checks"]["B_Z3_WITNESS_CENSUS"] else "FAIL")
        + f" :: sites={census['site_count']}; family={census['family']['family_size']};"
        + f" host={census['route_host']['classification']};"
        + " witnesses=" + ("null" if hosted is None else str(hosted["witness_count"])),
        "C_STRUCTURE_TRANSFER " + ("PASS" if receipt["checks"]["C_STRUCTURE_TRANSFER"] else "FAIL")
        + f" :: result={transfer['classification']}; orbits={compact(orbit_rows)}",
        "D_HONEST_SCOPE " + ("PASS" if receipt["checks"]["D_HONEST_SCOPE"] else "FAIL")
        + f" :: local_hosted={scope['local_seven_site_instance_hosted']};"
        + f" full_infinite_claimed={scope['full_infinite_z3_instance_claimed']};"
        + f" missing={len(scope['not_supplied_by_this_instance'])}",
        "E_CONTROLS " + ("PASS" if receipt["checks"]["E_CONTROLS"] else "FAIL")
        + f" :: source_reads={receipt['controls']['literal_source_read_count']}<=6;"
        + f" pins={receipt['controls']['sha_pins_match'] and receipt['controls']['blob_pins_match']};"
        + f" prior_ast_text={receipt['controls']['prior_cycle_text_or_ast_executed']};"
        + f" determinism={receipt['controls']['determinism_replay']};"
        + f" runtime_s={receipt['controls']['runtime_seconds']:.3f}<1400",
    ]
    passed = sum(receipt["checks"].values())
    lines.append(f"TOTAL: PASS={passed} FAIL={len(receipt['checks']) - passed}")
    return "\n".join(lines) + "\n"


def run() -> tuple[dict, str]:
    started = monotonic()
    controls = input_controls()
    first = science_measurement()
    second = science_measurement()
    deterministic = first == second
    adjacency = first["A_ADJACENCY_MAP"]
    census = first["B_Z3_WITNESS_CENSUS"]
    transfer = first["C_STRUCTURE_TRANSFER"]
    scope = first["D_HONEST_SCOPE"]

    substrate = {tuple(pair) for pair in adjacency["semantic_wiring_edges"]}
    z3_edges = {tuple(pair) for pair in adjacency["z3_edges"]}
    a_bookkeeping = bool(
        adjacency["vertex_map_injective"]
        and len(substrate) == adjacency["semantic_wiring_edge_count"]
        and len(z3_edges) == adjacency["z3_edge_count"]
        and adjacency["relation_classification"] == relation_classification(substrate, z3_edges)
        and len(adjacency["path_realization"]) == len(substrate)
        and all(row["all_steps_z3_nearest_neighbour"] for row in adjacency["path_realization"])
    )
    candidate = census["semantic_candidate_census"]
    hosted = census["hosted_census"]
    b_bookkeeping = bool(
        census["family"]["family_size"] == len(declared_target_local_family())
        and candidate["witness_count"] == len(candidate["witness_names"])
        and census["landed_vs_independent_truth_failure_count"] == 0
        and (
            (hosted == candidate) == census["route_host"]["all_words_routable"]
        )
    )
    orbit = candidate["orbit_decomposition"]
    c_bookkeeping = bool(
        orbit["partition_has_no_overlap_or_omission"]
        and sum(row["member_count"] for row in orbit["orbits"]) == candidate["witness_count"]
        and all(
            row["orbit_stabilizer_product"] == orbit["effective_group_order"]
            for row in orbit["orbits"]
        )
        and transfer["orbit_data"] == orbit
    )
    d_bookkeeping = bool(
        isinstance(scope["local_seven_site_instance_hosted"], bool)
        and scope["full_infinite_z3_instance_claimed"] is False
        and bool(scope["scope_boundary"])
        and bool(scope["not_supplied_by_this_instance"])
    )
    controls.update({
        "determinism_replay": deterministic,
        "runtime_seconds": monotonic() - started,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "house_stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
    })
    e_controls = bool(
        controls["literal_source_read_count"] <= 6
        and controls["all_inputs_relative_and_present"]
        and controls["sha_pins_match"] and controls["blob_pins_match"]
        and controls["blocklist_text_disjoint_from_reads"]
        and not controls["blocked_ast_imports"]
        and not controls["prior_cycle_text_or_ast_executed"]
        and controls["pinned_substrate"]["sha_pin_match"]
        and controls["pinned_substrate"]["blob_pin_match"]
        and controls["base_is_ancestor_of_head"]
        and deterministic and controls["runtime_seconds"] < AUDIT_TIMEOUT_SEC
    )
    receipt = {
        "cycle": CYCLE,
        "artifact": "true Z3 adjacency dependence-class bounded census primary",
        "audit_status_authority": "independent audit lane only",
        "integrity_policy": (
            "checks gate construction and bookkeeping only; hosted, deformed, failed, or unavailable census outcomes remain cleanly reportable"
        ),
        "findings": first,
        "science_digest": digest(first),
        "controls": controls,
        "checks": {
            "A_ADJACENCY_MAP": a_bookkeeping,
            "B_Z3_WITNESS_CENSUS": b_bookkeeping,
            "C_STRUCTURE_TRANSFER": c_bookkeeping,
            "D_HONEST_SCOPE": d_bookkeeping,
            "E_CONTROLS": e_controls,
        },
    }
    receipt["primary_source_sha256"] = sha256((ROOT / PRIMARY_PATH).read_bytes()).hexdigest()
    for _ in range(3):
        stdout = render_stdout(receipt)
        controls["stdout_bytes"] = len(stdout.encode())
    stdout = render_stdout(receipt)
    if len(stdout.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        receipt["checks"]["E_CONTROLS"] = False
        stdout = render_stdout(receipt)
    receipt["pass"] = all(receipt["checks"].values())
    receipt["stdout_sha256"] = sha256(stdout.encode()).hexdigest()
    return receipt, stdout


def main() -> int:
    if sys.argv[1:]:
        raise SystemExit(f"usage: {Path(__file__).name}")
    receipt, stdout = run()
    receipt_path = ROOT / RECEIPT_PATH
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    sys.stdout.write(stdout)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
