#!/usr/bin/env python3
"""Cycle 193: physical three-bit context-to-program dispatcher.

Three physical H0/H1 context records feed existing typed bit cables.  Seven
small binary routers select one of eight spatial leaves.  Seven leaves carry
the six Cycle-191 decoder programs plus OMIT as fixed binary tape banks; the
eighth is a reserved INVALID sink.  A selected legal leaf starts an ordered
H1 scan spine adjacent to the twelve binary tape records.

The construction removes host-side context lookup.  It does not give the
binary gate tokens quantum H/CNOT semantics, execute a microscopic quantum
gate, derive Born weights, or select an actual outcome.
"""

from __future__ import annotations

import hashlib
from collections import defaultdict, deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from pathlib import Path

import common_clifford_context_interpreter_cycle191_2026_07_16 as c191
import physical_five_lane_formation_membership_cycle179_2026_07_16 as c179


Coord = tuple[int, int, int]
Signature = c179.c169.c53.Signature

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CONTEXT_PROGRAM_DISPATCHER_CYCLE193_NOTE_2026-07-16.md"
)
CYCLE179_SCRIPT = (
    ROOT / "scripts/physical_five_lane_formation_membership_cycle179_2026_07_16.py"
)
CYCLE179_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FIVE_LANE_FORMATION_MEMBERSHIP_CYCLE179_NOTE_2026-07-16.md"
)
CYCLE191_SCRIPT = (
    ROOT / "scripts/common_clifford_context_interpreter_cycle191_2026_07_16.py"
)
CYCLE191_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COMMON_CLIFFORD_CONTEXT_INTERPRETER_CYCLE191_NOTE_2026-07-16.md"
)

FROZEN = {
    CYCLE179_SCRIPT: "e5a143d7e35a084d8d3689008c7babe72b35934a5c447a8b41467837c1dd7d85",
    CYCLE179_NOTE: "ea8ed6744398b8dc435fa4a72d49ed017da43e5b3c566c645d4be40ff3bb9393",
    CYCLE191_SCRIPT: "b7e3b21aef6005cb9715cf5c1b2612f6748c216066f771abfe4a3c01d9c10bc9",
    CYCLE191_NOTE: "62dc9974746976aeb202d91386b98c935ae335dda63e0ce0da86a5a2a8aa37ec",
}

c53 = c179.c169.c53
cell = c179.c169.cell
cable = c179.c169.cable

H0 = c179.H0
H1 = c179.H1
FRAME = c179.FRAME
GUIDE = c179.GUIDE

ORIGIN: Coord = (0, 0, 0)
EX: Coord = (1, 0, 0)
EY: Coord = (0, 1, 0)
EZ: Coord = (0, 0, 1)
NEG_EX: Coord = (-1, 0, 0)
NEG_EY: Coord = (0, -1, 0)
NEG_EZ: Coord = (0, 0, -1)

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


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def cross(left: Coord, right: Coord) -> Coord:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    prior = records.get(site)
    if prior is not None and prior != role:
        raise ValueError(("record-collision", site, prior, role))
    records[site] = role


def bit_role(bit: int) -> str:
    return H1 if bit else H0


def bit_value(role: str) -> int:
    if role == H0:
        return 0
    if role == H1:
        return 1
    raise ValueError(("not-a-bit", role))


# ---------------------------------------------------------------------------
# Compact candidate-law delta
# ---------------------------------------------------------------------------

ROUTER_GATE = ORIGIN
ROUTER_TOKEN = NEG_EX
ROUTER_BIT = EX
ROUTER_BRANCH_0 = NEG_EY
ROUTER_BRANCH_1 = EY


def router_canonical_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for role in (H0, H1):
        records = {
            ROUTER_TOKEN: H1,
            ROUTER_BIT: role,
            NEG_EZ: FRAME,
            EZ: FRAME,
        }
        local = c53.canonical_signature(
            c53.local_signature(records, ROUTER_GATE)
        )
        table[local] = role

    # These markers are the first exact member of the router family whose
    # token and bit sockets are simultaneously ordinary cable endpoints.
    # Order: -x, +x, -z, +z around each branch.
    branch_specs = (
        (ROUTER_BRANCH_0, H0, (FRAME, FRAME, FRAME, FRAME)),
        (ROUTER_BRANCH_1, H1, (FRAME, FRAME, FRAME, H0)),
    )
    for target, gate_role, markers in branch_specs:
        records = {
            ROUTER_GATE: gate_role,
            add(target, NEG_EX): markers[0],
            add(target, EX): markers[1],
            add(target, NEG_EZ): markers[2],
            add(target, EZ): markers[3],
        }
        local = c53.canonical_signature(c53.local_signature(records, target))
        table[local] = H1
    return table


ROUTER_TABLE = router_canonical_table()
ROUTER_RAW = cell.merge_raw(
    *(cell.raw_orbit(local, output) for local, output in ROUTER_TABLE.items())
)


def scan_canonical_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for role in (H0, H1):
        records = {
            NEG_EX: H1,
            EY: role,
            NEG_EY: H0,
            NEG_EZ: H0,
            EZ: H0,
        }
        local = c53.canonical_signature(c53.local_signature(records, ORIGIN))
        table[local] = H1
    return table


SCAN_TABLE = scan_canonical_table()
SCAN_RAW = cell.merge_raw(
    *(cell.raw_orbit(local, output) for local, output in SCAN_TABLE.items())
)
MERGED_RAW = cell.merge_raw(c179.MERGED_RAW, ROUTER_RAW, SCAN_RAW)
RAW_CONFLICTS = {
    local: outputs
    for local, outputs in MERGED_RAW.items()
    if len(outputs) != 1
}


# ---------------------------------------------------------------------------
# Cycle-191 program encoding
# ---------------------------------------------------------------------------

TOKEN_CODE = {
    "H0": (0, 0),
    "H1": (0, 1),
    "CX01": (1, 0),
    "CX10": (1, 1),
}
CODE_TOKEN = {code: token for token, code in TOKEN_CODE.items()}


def binary_width(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> shift) & 1 for shift in reversed(range(width)))


def tape_word(label: str) -> tuple[int, ...]:
    if label == "OMIT":
        program: tuple[str, ...] = ()
        run = 0
    else:
        program = c191.EXPECTED_PROGRAMS[label]
        run = 1
    padded = program + ("H0",) * (4 - len(program))
    word = (
        (run,)
        + binary_width(len(program), 3)
        + tuple(bit for token in padded for bit in TOKEN_CODE[token])
    )
    if len(word) != 12:
        raise AssertionError((label, word))
    return word


LEGAL_LABELS = ("R1", "R2", "R3", "C1", "C2", "C3", "OMIT")
TAPE_WORDS = {label: tape_word(label) for label in LEGAL_LABELS}


def decode_tape(word: tuple[int, ...]) -> tuple[bool, tuple[str, ...]]:
    if len(word) != 12:
        raise ValueError(("tape-width", len(word)))
    run = bool(word[0])
    length = 4 * word[1] + 2 * word[2] + word[3]
    if length > 4:
        raise ValueError(("invalid-length", length))
    tokens = tuple(
        CODE_TOKEN[(word[4 + 2 * index], word[5 + 2 * index])]
        for index in range(4)
    )
    return run, tokens[:length]


# ---------------------------------------------------------------------------
# Fixed three-level router and seven physical tape banks
# ---------------------------------------------------------------------------

NODE_GATE: dict[tuple[int, ...], Coord] = {
    (): (0, 0, 0),
    (0,): (50, -70, 0),
    (1,): (50, 70, 0),
    (0, 0): (100, -105, 0),
    (0, 1): (100, -35, 0),
    (1, 0): (100, 35, 0),
    (1, 1): (100, 105, 0),
}

INPUT_SITE: dict[int, Coord] = {
    0: (-120, -120, 0),
    1: (-120, 0, 0),
    2: (-120, 120, 0),
}


def router_sites(prefix: tuple[int, ...]) -> dict[str, Coord]:
    gate = NODE_GATE[prefix]
    return {
        "gate": gate,
        "token": add(gate, NEG_EX),
        "bit": add(gate, EX),
        "branch0": add(gate, NEG_EY),
        "branch1": add(gate, EY),
        "token_port": add(gate, scale(-2, EX)),
        "bit_port": add(gate, scale(2, EX)),
        "branch0_port": add(gate, scale(-2, EY)),
        "branch1_port": add(gate, scale(2, EY)),
    }


def router_fixed(prefix: tuple[int, ...]) -> dict[Coord, str]:
    gate = NODE_GATE[prefix]
    records = {
        add(gate, NEG_EZ): FRAME,
        add(gate, EZ): FRAME,
    }
    branch0 = add(gate, NEG_EY)
    branch1 = add(gate, EY)
    for direction in (NEG_EX, EX, NEG_EZ, EZ):
        records[add(branch0, direction)] = FRAME
        records[add(branch1, direction)] = (
            H0 if direction == EZ else FRAME
        )
    # A straight cable approaching either input along the x axis can choose
    # +z as its guide.  The other three perpendicular guards are FRAME.
    for endpoint in (add(gate, NEG_EX), add(gate, EX)):
        records[add(endpoint, EZ)] = GUIDE
        records[add(endpoint, NEG_EZ)] = FRAME
        records[add(endpoint, EY)] = FRAME
        records[add(endpoint, NEG_EY)] = FRAME
    return records


def leaf_site(code: tuple[int, int, int]) -> Coord:
    gate = NODE_GATE[code[:2]]
    return add(gate, NEG_EY if code[2] == 0 else EY)


@dataclass(frozen=True)
class TapeGeometry:
    label: str
    code: tuple[int, int, int]
    leaf: Coord
    scan_sites: tuple[Coord, ...]
    bit_sites: tuple[Coord, ...]
    terminal_port: Coord
    fixed: dict[Coord, str]


def tape_geometry(label: str) -> TapeGeometry:
    code = c191.CONTEXT_CODES[label]
    leaf = leaf_site(code)
    gate = NODE_GATE[code[:2]]
    outward = NEG_EY if code[2] == 0 else EY
    bit_direction = EZ
    marker_axis = cross(outward, bit_direction)
    scan_sites = tuple(
        add(leaf, scale(index, outward))
        for index in range(1, 13)
    )
    bit_sites = tuple(add(site, bit_direction) for site in scan_sites)
    fixed: dict[Coord, str] = {}
    for index, site in enumerate(scan_sites):
        place(fixed, bit_sites[index], bit_role(TAPE_WORDS[label][index]))
        place(fixed, add(site, scale(-1, bit_direction)), H0)
        place(fixed, add(site, marker_axis), H0)
        place(fixed, add(site, scale(-1, marker_axis)), H0)
    terminal_port = add(leaf, scale(13, outward))
    return TapeGeometry(
        label,
        code,
        leaf,
        scan_sites,
        bit_sites,
        terminal_port,
        fixed,
    )


TAPES = {label: tape_geometry(label) for label in LEGAL_LABELS}
CODE_TAPE = {geometry.code: geometry for geometry in TAPES.values()}
INVALID_CODE = c191.CONTEXT_CODES["INVALID"]


def append_axis(path: list[Coord], target: Coord, axis: int) -> None:
    current = path[-1]
    difference = target[axis] - current[axis]
    if not difference:
        return
    step = 1 if difference > 0 else -1
    for _ in range(abs(difference)):
        value = list(path[-1])
        value[axis] += step
        path.append(tuple(value))  # type: ignore[arg-type]


def tree_edge_path(
    parent: tuple[int, ...],
    branch: int,
    child: tuple[int, ...],
    ordinal: int,
) -> tuple[Coord, ...]:
    parent_gate = NODE_GATE[parent]
    sign = -1 if branch == 0 else 1
    source = add(parent_gate, scale(sign, EY))
    child_token = router_sites(child)["token"]
    path = [source]
    append_axis(path, add(parent_gate, scale(4 * sign, EY)), 1)
    layer = 20 + 8 * ordinal
    append_axis(path, (path[-1][0], path[-1][1], layer), 2)
    portal_x = child_token[0] - 3 - 5 * ordinal
    append_axis(path, (portal_x, path[-1][1], layer), 0)
    append_axis(path, (path[-1][0], child_token[1], layer), 1)
    append_axis(path, (path[-1][0], path[-1][1], 0), 2)
    append_axis(path, child_token, 0)
    if path[-2] != add(child_token, NEG_EX):
        raise ValueError(("tree-approach", parent, branch, child, path[-2:]))
    return tuple(path)


TREE_EDGES: dict[tuple[int, ...], tuple[Coord, ...]] = {}
edge_ordinal = 0
for parent in ((), (0,), (1,)):
    for branch in (0, 1):
        child = parent + (branch,)
        TREE_EDGES[child] = tree_edge_path(
            parent,
            branch,
            child,
            edge_ordinal,
        )
        edge_ordinal += 1


CONTEXT_TARGETS: dict[int, tuple[tuple[int, ...], ...]] = {
    0: ((),),
    1: ((0,), (1,)),
    2: ((0, 0), (0, 1), (1, 0), (1, 1)),
}
CONTEXT_FIRST_DIRECTIONS: dict[int, tuple[Coord, ...]] = {
    0: (EX,),
    1: (NEG_EY, EY),
    2: (NEG_EX, NEG_EY, EY, EX),
}


def context_path(
    bit_index: int,
    prefix: tuple[int, ...],
    first_direction: Coord,
    ordinal: int,
) -> tuple[Coord, ...]:
    source = INPUT_SITE[bit_index]
    target = router_sites(prefix)["bit"]
    path = [source]
    for factor in (1, 2, 3):
        wanted = add(source, scale(factor, first_direction))
        axis = next(index for index, value in enumerate(first_direction) if value)
        append_axis(path, wanted, axis)
    layer = -24 - 8 * ordinal
    append_axis(path, (path[-1][0], path[-1][1], layer), 2)
    portal_x = 130 + 7 * ordinal
    # Leave the four-way launch cross on the perpendicular axis before the
    # long run.  Otherwise an east/west run intersects the other launch's
    # vertical segment at a different z layer.
    if first_direction[0]:
        detour_y = source[1] + 24 + 5 * ordinal
        append_axis(path, (path[-1][0], detour_y, layer), 1)
    else:
        detour_x = source[0] + 24 + 5 * ordinal
        append_axis(path, (detour_x, path[-1][1], layer), 0)
    append_axis(path, (portal_x, path[-1][1], layer), 0)
    append_axis(path, (path[-1][0], target[1], layer), 1)
    append_axis(path, (path[-1][0], path[-1][1], 0), 2)
    append_axis(path, target, 0)
    if path[-2] != add(target, EX):
        raise ValueError(("context-approach", bit_index, prefix, path[-2:]))
    return tuple(path)


CONTEXT_PATHS: dict[tuple[int, tuple[int, ...]], tuple[Coord, ...]] = {}
context_ordinal = 0
for bit_index in range(3):
    for prefix, first_direction in zip(
        CONTEXT_TARGETS[bit_index],
        CONTEXT_FIRST_DIRECTIONS[bit_index],
    ):
        CONTEXT_PATHS[(bit_index, prefix)] = context_path(
            bit_index,
            prefix,
            first_direction,
            context_ordinal,
        )
        context_ordinal += 1


@dataclass(frozen=True)
class Scaffold:
    initial: dict[Coord, str]
    context_paths: dict[tuple[int, tuple[int, ...]], tuple[Coord, ...]]
    tree_edges: dict[tuple[int, ...], tuple[Coord, ...]]
    router_dynamic: frozenset[Coord]
    scan_dynamic: frozenset[Coord]
    cable_dynamic: frozenset[Coord]
    terminal_ports: frozenset[Coord]
    initial_count: int


@lru_cache(maxsize=1)
def build_scaffold() -> Scaffold:
    constraints: dict[Coord, str] = {}
    for prefix in NODE_GATE:
        for site, role in router_fixed(prefix).items():
            place(constraints, site, role)
    place(constraints, router_sites(())["token"], H1)
    for geometry in TAPES.values():
        for site, role in geometry.fixed.items():
            place(constraints, site, role)

    router_dynamic = {
        site
        for prefix in NODE_GATE
        for site in (
            router_sites(prefix)["gate"],
            router_sites(prefix)["branch0"],
            router_sites(prefix)["branch1"],
        )
    }
    scan_dynamic = {
        site
        for geometry in TAPES.values()
        for site in geometry.scan_sites
    }
    router_ports = {
        site
        for prefix in NODE_GATE
        for site in (
            router_sites(prefix)["token"],
            router_sites(prefix)["bit"],
            router_sites(prefix)["token_port"],
            router_sites(prefix)["bit_port"],
            router_sites(prefix)["branch0_port"],
            router_sites(prefix)["branch1_port"],
        )
    }
    tape_ports = {geometry.terminal_port for geometry in TAPES.values()}

    items: list[tuple[str, tuple[Coord, ...]]] = []
    items.extend(
        (H0, path)
        for path in CONTEXT_PATHS.values()
    )
    items.extend(
        (H1, path)
        for path in TREE_EDGES.values()
    )
    records, cable_expected, terminal_ports = cable.multi_path_core(
        tuple(items),
        constraints=constraints,
        extra_protected=(
            router_dynamic
            | scan_dynamic
            | router_ports
            | tape_ports
        ),
    )

    # Tree-edge sources are selected router branches, not supplied H1 records.
    for path in TREE_EDGES.values():
        records.pop(path[0], None)
    for site in router_dynamic | scan_dynamic | set(cable_expected):
        records.pop(site, None)
    for site in terminal_ports | tape_ports:
        records.pop(site, None)

    cable_dynamic = {
        site
        for path in (*CONTEXT_PATHS.values(), *TREE_EDGES.values())
        for site in path[1:]
    }
    all_dynamic = router_dynamic | scan_dynamic | cable_dynamic
    # Keep every declared router face open, including INVALID's unused
    # outward sink face.  Legal faces are already protected by a cable or
    # scan chain; INVALID exposed the otherwise hidden one-site cage fill.
    protected_ports = set(terminal_ports) | tape_ports | router_ports
    core = set(records) | all_dynamic | protected_ports
    shell = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in shell:
        place(records, site, FRAME)

    return Scaffold(
        initial=records,
        context_paths=CONTEXT_PATHS,
        tree_edges=TREE_EDGES,
        router_dynamic=frozenset(router_dynamic),
        scan_dynamic=frozenset(scan_dynamic),
        cable_dynamic=frozenset(cable_dynamic),
        terminal_ports=frozenset(protected_ports),
        initial_count=len(records),
    )


@dataclass(frozen=True)
class Instance:
    code: tuple[int, int, int]
    label: str
    initial: dict[Coord, str]
    expected: dict[Coord, str]
    dependencies: dict[Coord, frozenset[Coord]]
    selected_leaf: Coord
    selected_scan: tuple[Coord, ...]


def add_path(
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    path: tuple[Coord, ...],
    role: str,
) -> None:
    for previous, site in zip(path, path[1:]):
        prior = expected.get(site)
        if prior is not None and prior != role:
            raise ValueError(("path-output-collision", site, prior, role))
        expected[site] = role
        dependencies[site] = (
            frozenset((previous,))
            if previous in expected
            else frozenset()
        )


def instance(code: tuple[int, int, int]) -> Instance:
    scaffold = build_scaffold()
    label = c191.CODE_TO_LABEL[code]
    initial = dict(scaffold.initial)
    for bit_index, bit in enumerate(code):
        initial[INPUT_SITE[bit_index]] = bit_role(bit)

    expected: dict[Coord, str] = {}
    dependencies: dict[Coord, frozenset[Coord]] = {}
    for (bit_index, _prefix), path in CONTEXT_PATHS.items():
        add_path(expected, dependencies, path, bit_role(code[bit_index]))

    current: tuple[int, ...] = ()
    selected_leaf: Coord | None = None
    for level, branch in enumerate(code):
        sites = router_sites(current)
        gate = sites["gate"]
        token = sites["token"]
        bit_site = sites["bit"]
        gate_parents = frozenset(
            site for site in (token, bit_site) if site in expected
        )
        expected[gate] = bit_role(branch)
        dependencies[gate] = gate_parents
        branch_site = sites["branch0"] if branch == 0 else sites["branch1"]
        expected[branch_site] = H1
        dependencies[branch_site] = frozenset((gate,))
        selected_leaf = branch_site
        if level < 2:
            child = current + (branch,)
            add_path(expected, dependencies, TREE_EDGES[child], H1)
            current = child

    if selected_leaf is None:
        raise AssertionError(code)
    selected_scan: tuple[Coord, ...] = ()
    if label != "INVALID":
        geometry = CODE_TAPE[code]
        selected_scan = geometry.scan_sites
        previous = selected_leaf
        for site in selected_scan:
            expected[site] = H1
            dependencies[site] = (
                frozenset((previous,))
                if previous in expected
                else frozenset()
            )
            previous = site

    return Instance(
        code=code,
        label=label,
        initial=initial,
        expected=expected,
        dependencies=dependencies,
        selected_leaf=selected_leaf,
        selected_scan=selected_scan,
    )


def enabled(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in MERGED_RAW
    }


def children_map(
    dependencies: dict[Coord, frozenset[Coord]],
) -> dict[Coord, tuple[Coord, ...]]:
    children: dict[Coord, list[Coord]] = defaultdict(list)
    for site, parents in dependencies.items():
        for parent in parents:
            children[parent].append(site)
    return {
        site: tuple(sorted(values))
        for site, values in children.items()
    }


def schedule(
    dependencies: dict[Coord, frozenset[Coord]],
    order: str,
) -> tuple[Coord, ...]:
    children = children_map(dependencies)
    pending = {
        site: len(parents)
        for site, parents in dependencies.items()
    }
    frontier = {
        site
        for site, count in pending.items()
        if count == 0
    }
    result = []
    while frontier:
        target = min(frontier) if order == "min" else max(frontier)
        frontier.remove(target)
        result.append(target)
        for child in children.get(target, ()):
            pending[child] -= 1
            if pending[child] == 0:
                frontier.add(child)
    if len(result) != len(dependencies):
        raise ValueError(("dependency-cycle", len(result), len(dependencies)))
    return tuple(result)


def update_enabled(
    records: dict[Coord, str],
    actual: dict[Coord, frozenset[str]],
    target: Coord,
) -> None:
    actual.pop(target, None)
    for candidate in (
        target,
        *(add(target, direction) for direction in c53.DIRECTIONS),
    ):
        if candidate in records:
            actual.pop(candidate, None)
            continue
        if not any(
            add(candidate, direction) in records
            for direction in c53.DIRECTIONS
        ):
            actual.pop(candidate, None)
            continue
        local = c53.local_signature(records, candidate)
        outputs = MERGED_RAW.get(local)
        if outputs is None:
            actual.pop(candidate, None)
        else:
            actual[candidate] = outputs


def physical_run(
    apparatus: Instance,
    order: str,
    *,
    rotation=None,
) -> tuple[bool, object]:
    initial = apparatus.initial
    expected = apparatus.expected
    dependencies = apparatus.dependencies
    if rotation is not None:
        shift = (701, -709, 719)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        dependencies = {
            next(
                iter(c53.transform_records({site: "x"}, rotation, shift))
            ): frozenset(
                c53.transform_records(
                    {parent: "x" for parent in parents},
                    rotation,
                    shift,
                )
            )
            for site, parents in apparatus.dependencies.items()
        }

    records = dict(initial)
    linear = schedule(dependencies, order)
    children = children_map(dependencies)
    pending = {
        site: len(parents)
        for site, parents in dependencies.items()
    }
    frontier = {
        site
        for site, count in pending.items()
        if count == 0
    }
    actual = enabled(records)
    for step, target in enumerate(linear):
        wanted = {
            site: frozenset((expected[site],))
            for site in frontier
        }
        if actual != wanted:
            return False, {
                "step": step,
                "target": target,
                "extra": tuple(sorted(set(actual) - set(wanted)))[:8],
                "missing": tuple(sorted(set(wanted) - set(actual)))[:8],
                "actual": tuple(sorted(actual.items()))[:8],
                "wanted": tuple(sorted(wanted.items()))[:8],
            }
        records[target] = expected[target]
        frontier.remove(target)
        for child in children.get(target, ()):
            pending[child] -= 1
            if pending[child] == 0:
                frontier.add(child)
        update_enabled(records, actual, target)
    terminal_rescan = enabled(records)
    if actual or terminal_rescan:
        return False, {
            "terminal-incremental": tuple(sorted(actual.items()))[:8],
            "terminal-rescan": tuple(sorted(terminal_rescan.items()))[:8],
        }
    return True, {
        "initial": len(initial),
        "dynamic": len(expected),
        "selected_leaf": apparatus.selected_leaf,
        "selected_scan": len(apparatus.selected_scan),
    }


def selected_word(
    records: dict[Coord, str],
    label: str,
) -> tuple[int, ...]:
    geometry = TAPES[label]
    return tuple(bit_value(records[site]) for site in geometry.bit_sites)


def adjacency_failures(apparatus: Instance) -> tuple[tuple[Coord, Coord], ...]:
    sites = set(apparatus.expected)
    direct = {
        frozenset((site, parent))
        for site, parents in apparatus.dependencies.items()
        for parent in parents
    }
    failures = []
    for site in sites:
        for direction in c53.DIRECTIONS:
            other = add(site, direction)
            pair = frozenset((site, other))
            if other in sites and site < other and pair not in direct:
                failures.append((site, other))
    return tuple(failures)


def descendants(
    dependencies: dict[Coord, frozenset[Coord]],
    starts: set[Coord],
) -> frozenset[Coord]:
    children = children_map(dependencies)
    seen = set(starts)
    queue = deque(starts)
    while queue:
        site = queue.popleft()
        for child in children.get(site, ()):
            if child not in seen:
                seen.add(child)
                queue.append(child)
    return frozenset(seen)


def context_deletion_run(
    apparatus: Instance,
    bit_index: int,
    order: str,
) -> tuple[bool, object]:
    starts = {
        path[1]
        for (index, _prefix), path in CONTEXT_PATHS.items()
        if index == bit_index
    }
    removed = descendants(apparatus.dependencies, starts)
    initial = dict(apparatus.initial)
    initial.pop(INPUT_SITE[bit_index])
    expected = {
        site: role
        for site, role in apparatus.expected.items()
        if site not in removed
    }
    dependencies = {
        site: parents
        for site, parents in apparatus.dependencies.items()
        if site not in removed
    }
    if any(not parents <= expected.keys() for parents in dependencies.values()):
        return False, ("uncollapsed-context-cut", bit_index)
    pruned = Instance(
        code=apparatus.code,
        label=apparatus.label,
        initial=initial,
        expected=expected,
        dependencies=dependencies,
        selected_leaf=apparatus.selected_leaf,
        selected_scan=tuple(
            site for site in apparatus.selected_scan if site in expected
        ),
    )
    result = physical_run(pruned, order)
    return (
        result[0]
        and apparatus.selected_leaf not in expected
        and not pruned.selected_scan,
        {
            "removed": len(removed),
            "remaining": len(expected),
            "run": result,
        },
    )


def affected_enabled(
    records: dict[Coord, str],
    changed: set[Coord],
) -> dict[Coord, frozenset[str]]:
    candidates = changed | {
        add(site, direction)
        for site in changed
        for direction in c53.DIRECTIONS
    }
    answer = {}
    for target in candidates:
        if target in records:
            continue
        local = c53.local_signature(records, target)
        outputs = MERGED_RAW.get(local)
        if outputs is not None:
            answer[target] = outputs
    return answer


def flipped(role: str) -> str:
    return H0 if role == H1 else H1


def program_controls() -> dict[str, object]:
    selected_delete_failures = []
    selected_flip_failures = []
    token_delete_failures = []
    token_flip_failures = []
    unselected_failures = []
    invalid_length_flips = 0

    for label in LEGAL_LABELS:
        apparatus = instance(c191.CONTEXT_CODES[label])
        geometry = TAPES[label]
        completed = {**apparatus.initial, **apparatus.expected}
        for index, bit_site in enumerate(geometry.bit_sites):
            before = {
                **apparatus.initial,
                **{
                    site: role
                    for site, role in apparatus.expected.items()
                    if site not in set(geometry.scan_sites[index:])
                },
            }
            target = geometry.scan_sites[index]
            baseline = MERGED_RAW.get(c53.local_signature(before, target))
            deleted = dict(before)
            deleted.pop(bit_site)
            deleted_actual = affected_enabled(deleted, {bit_site})
            if baseline != frozenset((H1,)) or deleted_actual:
                selected_delete_failures.append(
                    (label, index, baseline, deleted_actual)
                )

            counterfactual = dict(before)
            counterfactual[bit_site] = flipped(counterfactual[bit_site])
            flipped_actual = affected_enabled(counterfactual, {bit_site})
            mutated_word = list(TAPE_WORDS[label])
            mutated_word[index] = 1 - mutated_word[index]
            if flipped_actual != {target: frozenset((H1,))}:
                selected_flip_failures.append(
                    (label, index, flipped_actual)
                )
            try:
                decode_tape(tuple(mutated_word))
            except ValueError:
                invalid_length_flips += 1

            other_label = LEGAL_LABELS[
                (LEGAL_LABELS.index(label) + 1) % len(LEGAL_LABELS)
            ]
            other = instance(c191.CONTEXT_CODES[other_label])
            other_completed = {**other.initial, **other.expected}
            other_selected = selected_word(other_completed, other_label)
            for action in ("delete", "flip"):
                trial = dict(other_completed)
                if action == "delete":
                    trial.pop(bit_site)
                else:
                    trial[bit_site] = flipped(trial[bit_site])
                actual = affected_enabled(trial, {bit_site})
                if actual or selected_word(trial, other_label) != other_selected:
                    unselected_failures.append(
                        (label, index, action, actual)
                    )

        for slot in range(4):
            indices = (4 + 2 * slot, 5 + 2 * slot)
            sites = {geometry.bit_sites[index] for index in indices}
            before = {
                **apparatus.initial,
                **{
                    site: role
                    for site, role in apparatus.expected.items()
                    if site not in set(geometry.scan_sites[indices[0]:])
                },
            }
            target = geometry.scan_sites[indices[0]]
            deleted = dict(before)
            for site in sites:
                deleted.pop(site)
            if affected_enabled(deleted, sites):
                token_delete_failures.append(
                    (label, slot, affected_enabled(deleted, sites))
                )
            counterfactual = dict(before)
            for site in sites:
                counterfactual[site] = flipped(counterfactual[site])
            if affected_enabled(counterfactual, sites) != {
                target: frozenset((H1,))
            }:
                token_flip_failures.append(
                    (
                        label,
                        slot,
                        affected_enabled(counterfactual, sites),
                    )
                )

    return {
        "selected_bit_deletions": 12 * len(LEGAL_LABELS),
        "selected_bit_flips": 12 * len(LEGAL_LABELS),
        "token_pair_deletions": 4 * len(LEGAL_LABELS),
        "token_pair_flips": 4 * len(LEGAL_LABELS),
        "unselected_bit_mutations": 24 * len(LEGAL_LABELS),
        "invalid_length_flips": invalid_length_flips,
        "failures": (
            selected_delete_failures
            + selected_flip_failures
            + token_delete_failures
            + token_flip_failures
            + unselected_failures
        ),
    }


def causal_stats(apparatus: Instance) -> dict[str, int]:
    linear = schedule(apparatus.dependencies, "min")
    depth: dict[Coord, int] = {}
    for site in linear:
        parents = apparatus.dependencies[site]
        depth[site] = (
            1 + max(depth[parent] for parent in parents)
            if parents
            else 1
        )
    return {
        "dynamic": len(apparatus.expected),
        "edges": sum(map(len, apparatus.dependencies.values())),
        "roots": sum(not parents for parents in apparatus.dependencies.values()),
        "depth": max(depth.values()),
        "leaf_depth": depth[apparatus.selected_leaf],
        "scan_depth": (
            depth[apparatus.selected_scan[-1]]
            if apparatus.selected_scan
            else 0
        ),
    }


def predecessor_replay() -> tuple[bool, object]:
    prior_raw = c179.MERGED_RAW
    try:
        c179.MERGED_RAW = MERGED_RAW
        c179.initial_enabled.cache_clear()
        result = c179.physical_run(
            c179.instance(c179.ZI),
            order="min",
        )
    finally:
        c179.MERGED_RAW = prior_raw
        c179.initial_enabled.cache_clear()
    return result


def orbit_failures() -> tuple[object, ...]:
    failures = []
    for family, table in (
        ("router", ROUTER_TABLE),
        ("scan", SCAN_TABLE),
    ):
        for local, output in table.items():
            orbit = cell.raw_orbit(local, output)
            if any(values != frozenset((output,)) for values in orbit.values()):
                failures.append((family, local, output))
    return tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN PREDECESSORS")
    observed = {path: sha256(path) for path in FROZEN}
    check(
        "Cycle 179 and Cycle 191 artifacts remain frozen",
        observed == FROZEN,
        {path.name: digest for path, digest in observed.items()},
    )

    print("\nLAW DELTA")
    check(
        "the cable-fed replacement router is four canonical and forty-eight raw rows",
        len(ROUTER_TABLE) == 4
        and len(ROUTER_RAW) == 48
        and not (set(ROUTER_RAW) & set(c179.MERGED_RAW)),
        (len(ROUTER_TABLE), len(ROUTER_RAW)),
    )
    scan_overlap = set(SCAN_RAW) & set(
        cell.merge_raw(c179.MERGED_RAW, ROUTER_RAW)
    )
    check(
        "the tape scan adds only six net raw rows",
        len(SCAN_TABLE) == 2
        and len(SCAN_RAW) == 30
        and len(scan_overlap) == 24
        and len(MERGED_RAW) == 101_768,
        (len(SCAN_TABLE), len(SCAN_RAW), len(scan_overlap), len(MERGED_RAW)),
    )
    check(
        "the complete dispatcher law is deterministic and role-bounded",
        not RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in MERGED_RAW.values())
        and set(ROUTER_TABLE.values()) | set(SCAN_TABLE.values()) <= {H0, H1},
        len(RAW_CONFLICTS),
    )

    print("\nPROGRAM ENCODING")
    check(
        "seven legal labels have distinct twelve-bit physical tape words",
        set(TAPE_WORDS) == set(LEGAL_LABELS)
        and len(set(TAPE_WORDS.values())) == 7
        and all(len(word) == 12 for word in TAPE_WORDS.values()),
        TAPE_WORDS,
    )
    check(
        "every tape decodes to the exact Cycle-191 program",
        all(
            decode_tape(word)
            == (
                label != "OMIT",
                () if label == "OMIT" else c191.EXPECTED_PROGRAMS[label],
            )
            for label, word in TAPE_WORDS.items()
        ),
        {label: decode_tape(word) for label, word in TAPE_WORDS.items()},
    )

    print("\nPHYSICAL SCAFFOLD")
    scaffold = build_scaffold()
    check(
        "the scaffold has seven routers, seven banks, and no supplied branch",
        len(NODE_GATE) == 7
        and len(TAPES) == 7
        and all(
            leaf not in scaffold.initial
            for code in c191.CONTEXT_CODES.values()
            for leaf in (leaf_site(code),)
        ),
        {
            "initial": scaffold.initial_count,
            "router_dynamic": len(scaffold.router_dynamic),
            "scan_dynamic": len(scaffold.scan_dynamic),
            "cable_dynamic": len(scaffold.cable_dynamic),
        },
    )

    print("\nALL CONTEXTS AND CONFLUENCE")
    runs = {}
    adjacency = {}
    for code in c191.CODE_TO_LABEL:
        apparatus = instance(code)
        runs[(code, "min")] = physical_run(apparatus, "min")
        runs[(code, "max")] = physical_run(apparatus, "max")
        adjacency[code] = adjacency_failures(apparatus)
    check(
        "all six contexts, OMIT, and reserved INVALID execute exactly",
        len(runs) == 16 and all(result[0] for result in runs.values()),
        {
            key: result
            for key, result in runs.items()
            if not result[0]
        },
    )
    check(
        "minimum and maximum schedules agree with zero adjacent unordered writes",
        all(not failures for failures in adjacency.values()),
        adjacency,
    )

    print("\nCONTEXT RECORD CONTROLS")
    context_deletions = {
        (code, bit_index): context_deletion_run(
            instance(code),
            bit_index,
            "min",
        )
        for code in c191.CODE_TO_LABEL
        for bit_index in range(3)
    }
    check(
        "deleting any one of the three context records suppresses every selected tape",
        len(context_deletions) == 24
        and all(result[0] for result in context_deletions.values()),
        {
            key: result
            for key, result in context_deletions.items()
            if not result[0]
        },
    )
    context_flips = {
        (code, bit_index): tuple(
            1 - bit if index == bit_index else bit
            for index, bit in enumerate(code)
        )
        for code in c191.CODE_TO_LABEL
        for bit_index in range(3)
    }
    check(
        "every context-bit flip selects exactly the corresponding other leaf",
        len(context_flips) == 24
        and all(
            instance(flipped_code).selected_leaf == leaf_site(flipped_code)
            and instance(flipped_code).label
            == c191.CODE_TO_LABEL[flipped_code]
            for flipped_code in context_flips.values()
        ),
        context_flips,
    )

    print("\nPHYSICAL PROGRAM-BANK CONTROLS")
    controls = program_controls()
    check(
        "all selected and unselected program-bit deletion/flip controls are exact",
        not controls["failures"]
        and controls["selected_bit_deletions"] == 84
        and controls["selected_bit_flips"] == 84
        and controls["unselected_bit_mutations"] == 168,
        controls,
    )
    check(
        "all four two-bit gate-token slots pass deletion and flip controls",
        not controls["failures"]
        and controls["token_pair_deletions"] == 28
        and controls["token_pair_flips"] == 28,
        controls,
    )

    print("\nPROPER-CUBIC COVARIANCE")
    hard = instance(c191.CONTEXT_CODES["R2"])
    rotation_runs = tuple(
        physical_run(hard, "min", rotation=rotation)
        for rotation in c53.ROTATIONS
    )
    check(
        "the full R2 history closes in all twenty-four proper-cubic images",
        len(rotation_runs) == 24 and all(result[0] for result in rotation_runs),
        tuple(result for result in rotation_runs if not result[0])[:2],
    )
    check(
        "all router and scan schemas have exact proper-cubic row orbits",
        len(c53.ROTATIONS) == 24 and not orbit_failures(),
        orbit_failures(),
    )

    print("\nPREDECESSOR COEXISTENCE AND COST")
    predecessor = predecessor_replay()
    check(
        "the complete Cycle-179 hard history remains exact under the dispatcher law",
        predecessor[0],
        predecessor,
    )
    prior_roles = {
        role
        for local, outputs in c179.MERGED_RAW.items()
        for role in (
            *(value for _offset, value in local),
            *outputs,
        )
    }
    merged_roles = {
        role
        for local, outputs in MERGED_RAW.items()
        for role in (
            *(value for _offset, value in local),
            *outputs,
        )
    }
    check(
        "the dispatcher adds no onsite role and no eight- or thirty-two-valued payload",
        merged_roles == prior_roles
        and set(ROUTER_TABLE.values()) | set(SCAN_TABLE.values()) == {H0, H1},
        merged_roles - prior_roles,
    )
    stats = causal_stats(hard)
    check(
        "the R2 leaf and tape lie on one finite append-only causal graph",
        stats["scan_depth"] > stats["leaf_depth"] > 0
        and stats["dynamic"] == len(hard.expected),
        stats,
    )

    print("\nSCOPE FIREWALL")
    normalized_note = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    required_phrases = (
        "host-side context lookup is removed",
        "no context-specific eight-valued role",
        "no 32-valued payload",
        "gate-semantics atom remains imported",
        "not microscopic quantum execution",
        "the born trace pairing remains imported",
        "actual branch selection remains open",
        "no axiom conclusion follows",
        "no commit or push",
    )
    missing_phrases = tuple(
        phrase
        for phrase in required_phrases
        if phrase not in normalized_note
    )
    check(
        "the retained note preserves the exact authority and quantum boundary",
        NOTE.is_file() and not missing_phrases,
        missing_phrases,
    )

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE193_PHYSICAL_CONTEXT_DISPATCHER_GREEN"
        if FAIL == 0
        else "CYCLE193_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
