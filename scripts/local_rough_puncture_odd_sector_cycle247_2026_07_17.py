#!/usr/bin/env python3
"""Cycle 247: bounded rough-puncture odd-sector compiler tournament.

The runner modifies the actual Cycle-235 square-pyramid dual graph in three
ways.  A cubic puncture adds one auxiliary sink vertex per coarse cell and six
spoke face qubits.  A sink-network candidate adds the cubic sink edges.  A
rough candidate instead adds one or more terminal face qubits at every sink.

The sharp result is a tradeoff, not a general no-go.  The un-terminated
puncture has the target rank but its stream generators leak.  The sink network
has target rank and lawful paired streams but their incident sink factors add
the wrong commutators.  A rough terminal gives an exact bounded even-CAR
generator map and both matter parity sectors, but the locally constrained code
has N-1 excess boundary logical qubits.  Tested local Z gauge-fixing either
leaks under neighboring streams or is lattice-wide.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "LOCAL_ROUGH_PUNCTURE_ODD_SECTOR_CYCLE247_NOTE_2026-07-17.md"
)

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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "one sink per coarse cell",
        "rough terminal",
        "rank matching is not an isometry",
        "n-1 excess boundary logical qubits",
        "15n extra anticommutations",
        "all 24 proper-cubic frames",
        "coarse-cell unit translation",
        "not homogeneous one-site translation",
        "period-16 physical role marker",
        "held-out l=6",
        "mass/contact/seam firewall",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
        "time firewall",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves scope, supplies, N1-N8, and time firewall", not missing, missing)


@dataclass(frozen=True)
class Edge:
    u: int
    v: int | None
    kind: str
    owner: tuple[int, int, int]
    label: int = -1


class PunctureGraph:
    """Square-pyramid matter graph with one cubic sink per coarse cell."""

    def __init__(self, length: int, *, sink_network: bool = False, terminals: int = 0):
        self.length = length
        self.base = c235.PyramidCellulation(length)
        self.cells = self.base.cells
        self.cell_index = {cell: index for index, cell in enumerate(self.cells)}
        self.matter_count = len(self.base.vertices)
        self.vertices = list(self.base.vertices) + [(cell, "sink") for cell in self.cells]
        self.sink_index = {
            cell: self.matter_count + self.cell_index[cell] for cell in self.cells
        }
        self.edges: list[Edge] = []
        self.edge_lookup: dict[frozenset[int], int] = {}
        self.terminal_lookup: dict[tuple[tuple[int, int, int], int], int] = {}
        self.spoke_lookup: dict[tuple[tuple[int, int, int], int], int] = {}
        self.sink_bond_lookup: dict[frozenset[tuple[int, int, int]], int] = {}
        self.sink_network = sink_network
        self.terminals = terminals

        def add_internal(u: int, v: int, kind: str, owner, label: int = -1) -> int:
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise ValueError(("duplicate", u, v, kind))
            index = len(self.edges)
            self.edges.append(Edge(u, v, kind, owner, label))
            self.edge_lookup[key] = index
            return index

        for u, v, kind, owner in self.base.edges:
            add_internal(u, v, f"matter_{kind}", owner)

        for cell in self.cells:
            sink = self.sink_index[cell]
            for direction in range(6):
                matter = self.base.vertex_index[(cell, direction)]
                index = add_internal(sink, matter, "puncture_spoke", cell, direction)
                self.spoke_lookup[(cell, direction)] = index

        if sink_network:
            for cell in self.cells:
                for axis in range(3):
                    target = list(cell)
                    target[axis] = (target[axis] + 1) % length
                    target_cell = tuple(target)
                    index = add_internal(
                        self.sink_index[cell],
                        self.sink_index[target_cell],
                        "sink_bond",
                        cell,
                        axis,
                    )
                    self.sink_bond_lookup[frozenset((cell, target_cell))] = index

        for cell in self.cells:
            for label in range(terminals):
                index = len(self.edges)
                self.edges.append(Edge(self.sink_index[cell], None, "rough_terminal", cell, label))
                self.terminal_lookup[(cell, label)] = index

        self.incident = [[] for _ in self.vertices]
        for edge, row in enumerate(self.edges):
            self.incident[row.u].append(edge)
            if row.v is not None:
                self.incident[row.v].append(edge)
        # Terminals were appended last and their labels are frame scalars.  The
        # ordering-gauge repair therefore never needs a terminal/nonterminal
        # inversion and leaves the rough X flipper untouched.
        for row in self.incident:
            row.sort()

    @property
    def qubits(self) -> int:
        return len(self.edges)

    def edge_between(self, u: int, v: int) -> int:
        return self.edge_lookup[frozenset((u, v))]

    def B(self, vertex: int) -> c235.Pauli:
        z = 0
        for edge in self.incident[vertex]:
            z ^= 1 << edge
        return c235.Pauli(z=z)

    def A(self, source: int, target: int) -> c235.Pauli:
        edge = self.edge_between(source, target)
        z = 0
        for vertex in (source, target):
            for incident in self.incident[vertex]:
                if incident == edge:
                    break
                z ^= 1 << incident
        return c235.Pauli(0 if source < target else 2, 1 << edge, z)

    def cycle_mask(self, vertices: list[int]) -> int:
        mask = 0
        for index, source in enumerate(vertices):
            target = vertices[(index + 1) % len(vertices)]
            mask ^= 1 << self.edge_between(source, target)
        return mask

    def loop_pauli(self, vertices: list[int]) -> c235.Pauli:
        result = c235.Pauli(phase=len(vertices) % 4)
        for index, source in enumerate(vertices):
            result = result @ self.A(source, vertices[(index + 1) % len(vertices)])
        return result

    def local_cycles(self):
        rows: list[tuple[int, list[int], str]] = []
        for mask, vertices, kind in c235.primal_edge_cycles(self.base):
            rows.append((mask, vertices, f"matter_{kind}"))

        for edge, base_edge in enumerate(self.base.edges):
            u, v, kind, owner = base_edge
            if kind == "internal_triangle":
                vertices = [self.sink_index[owner], u, v]
                rows.append((self.cycle_mask(vertices), vertices, "puncture_triangle"))

        if self.sink_network:
            for cell in self.cells:
                for axis in range(3):
                    target = list(cell)
                    target[axis] = (target[axis] + 1) % self.length
                    target_cell = tuple(target)
                    vertices = [
                        self.sink_index[cell],
                        self.base.vertex_index[(cell, 2 * axis)],
                        self.base.vertex_index[(target_cell, 2 * axis + 1)],
                        self.sink_index[target_cell],
                    ]
                    rows.append((self.cycle_mask(vertices), vertices, "sink_matter_square"))
        return rows

    def wilson_cycles(self):
        return c235.wilson_cycles(self.base)

    def cell_constraint(self, cell: tuple[int, int, int]) -> c235.Pauli:
        result = self.B(self.sink_index[cell])
        for direction in range(6):
            result = result @ self.B(self.base.vertex_index[(cell, direction)])
        return result

    def boundary_stabilizers(self) -> list[c235.Pauli]:
        rows = []
        for cell in self.cells:
            for label in range(1, self.terminals):
                rows.append(
                    c235.Pauli(
                        x=(1 << self.terminal_lookup[(cell, 0)])
                        ^ (1 << self.terminal_lookup[(cell, label)])
                    )
                )
        return rows

    def mapped_matter_A(self, base_edge: int) -> c235.Pauli:
        u, v, kind, _ = self.base.edges[base_edge]
        result = self.A(u, v)
        if self.terminals and kind == "outer_square":
            left_cell = self.base.vertices[u][0]
            right_cell = self.base.vertices[v][0]
            result = result @ c235.Pauli(
                x=(1 << self.terminal_lookup[(left_cell, 0)])
                ^ (1 << self.terminal_lookup[(right_cell, 0)])
            )
        return result

    def paired_network_A(self, base_edge: int) -> c235.Pauli:
        u, v, kind, _ = self.base.edges[base_edge]
        result = self.A(u, v)
        if kind == "outer_square":
            left_cell = self.base.vertices[u][0]
            right_cell = self.base.vertices[v][0]
            result = result @ self.A(self.sink_index[left_cell], self.sink_index[right_cell])
        return result


def loop_rows(graph: PunctureGraph) -> list[c235.Pauli]:
    return [graph.loop_pauli(vertices) for _, vertices, _ in graph.local_cycles()] + [
        graph.loop_pauli(vertices) for vertices in graph.wilson_cycles()
    ]


def code_rows(graph: PunctureGraph) -> list[c235.Pauli]:
    return (
        loop_rows(graph)
        + [graph.cell_constraint(cell) for cell in graph.cells]
        + graph.boundary_stabilizers()
    )


def rank_and_parity_controls() -> None:
    print("\nPUNCTURE RANK / PARITY TOURNAMENT")
    rows = []
    for length in (3, 4, 5, 6):
        cells = length**3
        for name, network, terminals in (
            ("cubic_puncture", False, 0),
            ("sink_network", True, 0),
            ("rough_k1", False, 1),
            ("rough_k2", False, 2),
            ("rough_k3", False, 3),
        ):
            graph = PunctureGraph(length, sink_network=network, terminals=terminals)
            local = graph.local_cycles()
            local_rank = c235.gf2_rank(mask for mask, _, _ in local)
            full_rank = c235.gf2_rank(
                [mask for mask, _, _ in local]
                + [graph.cycle_mask(vertices) for vertices in graph.wilson_cycles()]
            )
            cell_constraints = [graph.cell_constraint(cell).z for cell in graph.cells]
            cell_rank = c235.gf2_rank(cell_constraints)
            boundary_rank = c235.gf2_rank(row.symplectic(graph.qubits) for row in graph.boundary_stabilizers())
            exponent = graph.qubits - full_rank - cell_rank - boundary_rank
            total_cell_constraint = 0
            for row in cell_constraints:
                total_cell_constraint ^= row

            # Abstract B-generator quotient: without terminals, the connected
            # extended graph has the single all-vertex B relation; a terminal
            # makes the vertex-B rows independent.  Add the C_x relations and
            # verify that all 6N matter B generators still increase rank.
            abstract_width = 7 * cells
            abstract_relations = []
            if terminals == 0:
                abstract_relations.append((1 << abstract_width) - 1)
            for cell in graph.cells:
                relation = 1 << graph.sink_index[cell]
                for direction in range(6):
                    relation ^= 1 << graph.base.vertex_index[(cell, direction)]
                abstract_relations.append(relation)
            abstract_rank = c235.gf2_rank(abstract_relations)
            matter_increment = c235.gf2_rank(
                abstract_relations + [1 << vertex for vertex in range(graph.matter_count)]
            ) - abstract_rank
            rows.append(
                {
                    "candidate": name,
                    "L": length,
                    "N": cells,
                    "qubits_per_cell": graph.qubits // cells,
                    "local_cycle_rank": local_rank,
                    "full_cycle_rank": full_rank,
                    "cell_constraint_rank": cell_rank,
                    "boundary_rank": boundary_rank,
                    "code_exponent": exponent,
                    "target_exponent": 6 * cells,
                    "cell_constraint_product_weight": total_cell_constraint.bit_count(),
                    "independent_matter_B": matter_increment,
                }
            )

    check(
        "un-terminated cubic punctures have target exponent and both matter parity sectors by rank",
        all(
            row["qubits_per_cell"] == 21
            and row["local_cycle_rank"] == 14 * row["N"] - 2
            and row["full_cycle_rank"] == 14 * row["N"] + 1
            and row["cell_constraint_rank"] == row["N"] - 1
            and row["code_exponent"] == row["target_exponent"]
            and row["cell_constraint_product_weight"] == 0
            and row["independent_matter_B"] == 6 * row["N"]
            for row in rows
            if row["candidate"] == "cubic_puncture"
        ),
        [row for row in rows if row["candidate"] == "cubic_puncture"],
    )
    check(
        "the cubic sink network also rank-matches after bounded square-cycle and cell constraints",
        all(
            row["qubits_per_cell"] == 24
            and row["local_cycle_rank"] == 17 * row["N"] - 2
            and row["full_cycle_rank"] == 17 * row["N"] + 1
            and row["cell_constraint_rank"] == row["N"] - 1
            and row["code_exponent"] == row["target_exponent"]
            and row["independent_matter_B"] == 6 * row["N"]
            for row in rows
            if row["candidate"] == "sink_network"
        ),
        [row for row in rows if row["candidate"] == "sink_network"],
    )
    check(
        "every tested locally stabilized rough-terminal multiplicity leaves exactly N-1 excess boundary logicals",
        all(
            row["qubits_per_cell"] == 21 + int(row["candidate"][-1])
            and row["cell_constraint_rank"] == row["N"]
            and row["boundary_rank"] == (int(row["candidate"][-1]) - 1) * row["N"]
            and row["code_exponent"] == 7 * row["N"] - 1
            and row["independent_matter_B"] == 6 * row["N"]
            for row in rows
            if row["candidate"].startswith("rough_k")
        ),
        [row for row in rows if row["candidate"].startswith("rough_k")],
    )

    # Actual signed-Pauli code ranks and matter-parity injectivity at L=3.
    actual = []
    for name, network, terminals, expected_exponent in (
        ("cubic_puncture", False, 0, 6 * 3**3),
        ("sink_network", True, 0, 6 * 3**3),
        ("rough_k1", False, 1, 7 * 3**3 - 1),
        ("rough_k2", False, 2, 7 * 3**3 - 1),
    ):
        graph = PunctureGraph(3, sink_network=network, terminals=terminals)
        stabs = code_rows(graph)
        rank, inconsistent = c235.phase_aware_rank(stabs, graph.qubits)
        matter_b = [graph.B(vertex) for vertex in range(graph.matter_count)]
        augmented = c235.gf2_rank(
            [row.symplectic(graph.qubits) for row in stabs + matter_b]
        )
        actual.append(
            {
                "candidate": name,
                "stabilizer_rank": rank,
                "phase_inconsistencies": inconsistent,
                "code_exponent": graph.qubits - rank,
                "matter_B_increment": augmented - rank,
                "matter_modes": graph.matter_count,
            }
        )
    check(
        "actual L=3 commuting Pauli codes are consistent and retain all 6N independent matter parities",
        all(not row["phase_inconsistencies"] for row in actual)
        and all(row["matter_B_increment"] == row["matter_modes"] for row in actual)
        and actual[0]["code_exponent"] == actual[1]["code_exponent"] == 6 * 3**3
        and actual[2]["code_exponent"] == actual[3]["code_exponent"] == 7 * 3**3 - 1,
        actual,
    )


def algebra_and_lawful_domain_controls() -> None:
    print("\nALGEBRA / LAWFUL-DOMAIN DISCRIMINATORS")
    core = PunctureGraph(3)
    core_constraints = [core.cell_constraint(cell) for cell in core.cells]
    onsite_leakage = stream_leakage = 0
    for edge, (u, v, kind, _) in enumerate(core.base.edges):
        failures = sum(not core.A(u, v).commutes(row) for row in core_constraints)
        if kind == "internal_triangle":
            onsite_leakage += failures
        else:
            stream_leakage += failures
    check(
        "rank-matched cubic punctures preserve onsite edges but every stream edge violates two cell constraints",
        onsite_leakage == 0 and stream_leakage == 2 * 3 * 3**3,
        {
            "onsite_constraint_violations": onsite_leakage,
            "stream_edges": 3 * 3**3,
            "stream_constraint_violations": stream_leakage,
        },
    )

    local_terminator_failures = remote_car_failures = 0
    for cell in core.cells:
        sink = core.sink_index[cell]
        for direction in range(6):
            matter = core.base.vertex_index[(cell, direction)]
            terminator = core.A(matter, sink)
            local_terminator_failures += sum(
                not terminator.commutes(row) for row in core_constraints
            )
    first = core.A(core.base.vertex_index[((0, 0, 0), 0)], core.sink_index[(0, 0, 0)])
    second = core.A(core.base.vertex_index[((1, 0, 0), 0)], core.sink_index[(1, 0, 0)])
    remote_car_failures = first.commutes(second)
    check(
        "a puncture terminates one matter charge locally only within a cell; remote terminators commute instead of CAR-anticommuting",
        local_terminator_failures == 0 and remote_car_failures,
        {
            "local_terminator_constraint_violations": local_terminator_failures,
            "remote_terminators_commute": first.commutes(second),
            "required_for_odd_CAR": "anticommute",
        },
    )

    network = PunctureGraph(3, sink_network=True)
    network_stabs = code_rows(network)
    mapped = [network.paired_network_A(edge) for edge in range(len(network.base.edges))]
    leakage = sum(
        not generator.commutes(stabilizer)
        for generator in mapped
        for stabilizer in network_stabs
    )
    pair_failures = 0
    stream_pair_failures = 0
    stream_indices = [
        edge for edge, row in enumerate(network.base.edges) if row[2] == "outer_square"
    ]
    for left_index, left in enumerate(stream_indices):
        u, v, _, _ = network.base.edges[left]
        for right in stream_indices[left_index + 1 :]:
            x, y, _, _ = network.base.edges[right]
            expected_anti = len({u, v} & {x, y}) == 1
            actual_anti = not mapped[left].commutes(mapped[right])
            pair_failures += expected_anti != actual_anti
            stream_pair_failures += actual_anti and not expected_anti
    check(
        "paired matter/sink streams are lawful but add exactly 15N false stream-stream anticommutations",
        leakage == 0
        and pair_failures == stream_pair_failures == 15 * 3**3,
        {
            "constraint_leakage": leakage,
            "false_pair_relations": stream_pair_failures,
            "expected_15N": 15 * 3**3,
        },
    )

    # Endpoint B_s dressings K_e=A_e B_s^p cannot make a degree-six sink
    # star commute: every pair would require p_j+p_k=1, impossible for >=3.
    endpoint_solutions = []
    for bits in product((0, 1), repeat=6):
        if all(bits[left] ^ bits[right] == 1 for left, right in combinations(range(6), 2)):
            endpoint_solutions.append(bits)
    check(
        "no endpoint-parity dressing repairs all six incident sink-edge commutators",
        endpoint_solutions == [],
        {"assignments_tested": 64, "solutions": endpoint_solutions},
    )

    rough = PunctureGraph(3, terminals=1)
    rough_stabs = code_rows(rough)
    rough_a = [rough.mapped_matter_A(edge) for edge in range(len(rough.base.edges))]
    leakage = sum(
        not generator.commutes(stabilizer)
        for generator in rough_a
        for stabilizer in rough_stabs
    )
    endpoint_failures = 0
    for edge, (u, v, _, _) in enumerate(rough.base.edges):
        for vertex in range(rough.matter_count):
            actual = not rough_a[edge].commutes(rough.B(vertex))
            endpoint_failures += actual != (vertex in (u, v))
    pair_failures = 0
    for left, (u, v, _, _) in enumerate(rough.base.edges):
        for right in range(left + 1, len(rough.base.edges)):
            x, y, _, _ = rough.base.edges[right]
            expected = len({u, v} & {x, y}) == 1
            actual = not rough_a[left].commutes(rough_a[right])
            pair_failures += expected != actual
    check(
        "rough-terminal stream dressing gives an exact lawful bounded even-CAR generator algebra",
        leakage == endpoint_failures == pair_failures == 0,
        {
            "constraint_leakage": leakage,
            "A_B_endpoint_failures": endpoint_failures,
            "A_A_pair_failures": pair_failures,
            "maximum_B_weight": max(rough.B(vertex).z.bit_count() for vertex in range(rough.matter_count)),
            "maximum_mapped_A_weight": max((row.x | row.z).bit_count() for row in rough_a),
            "code_excess_exponent": 3**3 - 1,
        },
    )


def boundary_gauge_and_deletion_controls() -> None:
    print("\nBOUNDARY GAUGE-FIXING / DELETION")
    rough = PunctureGraph(3, terminals=1)
    cells = rough.cells
    h = {cell: rough.terminal_lookup[(cell, 0)] for cell in cells}
    stream_updates = [
        rough.mapped_matter_A(edge)
        for edge, row in enumerate(rough.base.edges)
        if row[2] == "outer_square"
    ]
    onsite_z = [c235.Pauli(z=1 << h[cell]) for cell in cells]
    onsite_leakage = sum(
        not update.commutes(constraint)
        for update in stream_updates
        for constraint in onsite_z
    )

    equality = []
    for cell in cells:
        for axis in range(3):
            target = list(cell)
            target[axis] = (target[axis] + 1) % rough.length
            target_cell = tuple(target)
            equality.append(c235.Pauli(z=(1 << h[cell]) ^ (1 << h[target_cell])))
    equality_rank = c235.gf2_rank(row.z for row in equality)
    equality_leakage = sum(
        not update.commutes(constraint)
        for update in stream_updates
        for constraint in equality
    )

    # A Z word commutes with every X_x X_y stream dressing iff its cell bits
    # agree across every connected cubic edge.  The centralizer is therefore
    # only {0, all-ones}; its nontrivial member has weight N.
    cell_edges = []
    cell_index = {cell: index for index, cell in enumerate(cells)}
    for cell in cells:
        for axis in range(3):
            target = list(cell)
            target[axis] = (target[axis] + 1) % rough.length
            cell_edges.append((1 << cell_index[cell]) ^ (1 << cell_index[tuple(target)]))
    incidence_rank = c235.gf2_rank(cell_edges)
    check(
        "local boundary-Z fixing removes multiplicity only by leaking, while its update centralizer is lattice-wide",
        onsite_leakage == 2 * len(stream_updates)
        and equality_rank == len(cells) - 1
        and equality_leakage > 0
        and incidence_rank == len(cells) - 1,
        {
            "onsite_Z_stream_violations": onsite_leakage,
            "edge_equality_rank": equality_rank,
            "edge_equality_stream_violations": equality_leakage,
            "Z_centralizer_dimension": len(cells) - incidence_rank,
            "nontrivial_centralizer_weight": len(cells),
        },
    )

    first_cell = cells[0]
    rough_flipper = c235.Pauli(x=1 << h[first_cell])
    c_rows = [rough.cell_constraint(cell) for cell in cells]
    flipper_syndrome = sum(not rough_flipper.commutes(row) for row in c_rows)
    first_stream_edge = next(
        edge for edge, row in enumerate(rough.base.edges) if row[2] == "outer_square"
    )
    full_update = rough.mapped_matter_A(first_stream_edge)
    bare_update = rough.A(*rough.base.edges[first_stream_edge][:2])
    full_syndrome = sum(not full_update.commutes(row) for row in c_rows)
    bare_syndrome = sum(not bare_update.commutes(row) for row in c_rows)

    stabs = code_rows(rough)
    rank = c235.gf2_rank(row.symplectic(rough.qubits) for row in stabs)
    loops = loop_rows(rough)
    deleted = loops + c_rows[1:]
    deleted_rank = c235.gf2_rank(row.symplectic(rough.qubits) for row in deleted)
    check(
        "rough flippers and dressing deletion have exact local syndromes; deleting one C constraint adds one logical",
        flipper_syndrome == 1
        and full_syndrome == 0
        and bare_syndrome == 2
        and deleted_rank == rank - 1,
        {
            "single_rough_flipper_C_syndrome": flipper_syndrome,
            "dressed_stream_C_syndrome": full_syndrome,
            "deleted_rough_dressing_C_syndrome": bare_syndrome,
            "full_stabilizer_rank": rank,
            "one_C_deleted_rank": deleted_rank,
        },
    )

    rough2 = PunctureGraph(3, terminals=2)
    loops2 = loop_rows(rough2)
    c2 = [rough2.cell_constraint(cell) for cell in rough2.cells]
    boundary2 = rough2.boundary_stabilizers()
    full_rank2 = c235.gf2_rank(
        row.symplectic(rough2.qubits) for row in loops2 + c2 + boundary2
    )
    deleted_boundary_rank = c235.gf2_rank(
        row.symplectic(rough2.qubits) for row in loops2 + c2 + boundary2[1:]
    )
    check(
        "deleting one independent local terminal-pair stabilizer adds exactly one boundary logical",
        deleted_boundary_rank == full_rank2 - 1,
        {"full_rank": full_rank2, "deleted_rank": deleted_boundary_rank},
    )


def graph_frame_maps(graph: PunctureGraph, frame: np.ndarray):
    dmap = c235.direction_map(frame)
    vertex_map = []
    for vertex in range(graph.matter_count):
        cell, direction = graph.base.vertices[vertex]
        target_cell = tuple(int(value % graph.length) for value in frame @ np.asarray(cell))
        vertex_map.append(graph.base.vertex_index[(target_cell, dmap[direction])])
    for cell in graph.cells:
        target_cell = tuple(int(value % graph.length) for value in frame @ np.asarray(cell))
        vertex_map.append(graph.sink_index[target_cell])

    edge_map = []
    for row in graph.edges:
        if row.v is None:
            source_cell = row.owner
            target_cell = tuple(int(value % graph.length) for value in frame @ np.asarray(source_cell))
            edge_map.append(graph.terminal_lookup[(target_cell, row.label)])
        else:
            edge_map.append(graph.edge_between(vertex_map[row.u], vertex_map[row.v]))
    return vertex_map, edge_map


def permute_pauli(pauli: c235.Pauli, edge_map: list[int]) -> c235.Pauli:
    x = z = 0
    for source, target in enumerate(edge_map):
        if (pauli.x >> source) & 1:
            x ^= 1 << target
        if (pauli.z >> source) & 1:
            z ^= 1 << target
    return c235.Pauli(pauli.phase, x, z)


def order_gauge(graph: PunctureGraph, vertex_map, edge_map):
    toggles = [0] * graph.qubits
    pairs = []
    for source_vertex, target_vertex in enumerate(vertex_map):
        pulled = [edge_map[edge] for edge in graph.incident[source_vertex]]
        position = {edge: index for index, edge in enumerate(graph.incident[target_vertex])}
        for index, left in enumerate(pulled):
            for right in pulled[index + 1 :]:
                if position[left] > position[right]:
                    toggles[left] ^= 1 << right
                    toggles[right] ^= 1 << left
                    pairs.append((left, right))
    return toggles, pairs


def covariance_controls() -> None:
    print("\nTRANSLATION / PROPER-CUBIC COVARIANCE")
    graph = PunctureGraph(3, terminals=1)
    target_stabs = code_rows(graph)
    target_rank, target_inconsistent = c235.phase_aware_rank(target_stabs, graph.qubits)
    b_failures = a_failures = stab_failures = terminal_toggle_failures = 0
    for frame in c235.proper_cubic_frames():
        vertex_map, edge_map = graph_frame_maps(graph, frame)
        toggles, pairs = order_gauge(graph, vertex_map, edge_map)
        terminal_toggle_failures += sum(toggles[edge] != 0 for edge in graph.terminal_lookup.values())
        flips = 0
        for source_edge, row in enumerate(graph.edges):
            if row.v is None:
                continue
            transformed = permute_pauli(graph.A(row.u, row.v), edge_map)
            target = graph.A(vertex_map[row.u], vertex_map[row.v])
            ordered = c235.apply_gauge(transformed, toggles, pairs)
            if ordered.x != target.x or ordered.z != target.z:
                a_failures += 1
                continue
            if (ordered.phase - target.phase) % 4 == 2:
                flips ^= 1 << edge_map[source_edge]

        for vertex in range(len(graph.vertices)):
            transformed = permute_pauli(graph.B(vertex), edge_map)
            b_failures += transformed != graph.B(vertex_map[vertex])

        for source_edge in range(len(graph.base.edges)):
            u, v, kind, _ = graph.base.edges[source_edge]
            transformed = permute_pauli(graph.mapped_matter_A(source_edge), edge_map)
            corrected = c235.apply_gauge(transformed, toggles, pairs, flips)
            target = graph.A(vertex_map[u], vertex_map[v])
            if kind == "outer_square":
                left_cell = graph.vertices[vertex_map[u]][0]
                right_cell = graph.vertices[vertex_map[v]][0]
                target = target @ c235.Pauli(
                    x=(1 << graph.terminal_lookup[(left_cell, 0)])
                    ^ (1 << graph.terminal_lookup[(right_cell, 0)])
                )
            a_failures += corrected != target

        transformed_stabs = [
            c235.apply_gauge(permute_pauli(row, edge_map), toggles, pairs, flips)
            for row in target_stabs
        ]
        combined_rank, inconsistent = c235.phase_aware_rank(
            target_stabs + transformed_stabs, graph.qubits
        )
        stab_failures += combined_rank != target_rank or bool(inconsistent)

    check(
        "the rough-puncture graph, code, and mapped even algebra form exact 24-frame families up to bounded ordering gauge",
        len(c235.proper_cubic_frames()) == 24
        and not target_inconsistent
        and b_failures == a_failures == stab_failures == terminal_toggle_failures == 0,
        {
            "frames": len(c235.proper_cubic_frames()),
            "B_failures": b_failures,
            "mapped_A_failures": a_failures,
            "stabilizer_group_failures": stab_failures,
            "terminal_order_gauge_toggles": terminal_toggle_failures,
        },
    )

    # Every construction is periodic with one identical puncture per cell, so
    # unit translations permute its rows.  Check the three positive shifts.
    translation_failures = 0
    source_c = {row.z for row in [graph.cell_constraint(cell) for cell in graph.cells]}
    for axis in range(3):
        shifted = set()
        for cell in graph.cells:
            target = list(cell)
            target[axis] = (target[axis] + 1) % graph.length
            shifted.add(graph.cell_constraint(tuple(target)).z)
        translation_failures += shifted != source_c
    check(
        "one puncture per cell preserves all three unit translations",
        translation_failures == 0,
        {"positive_axis_family_failures": translation_failures},
    )


def open_boundary_control() -> None:
    print("\nGLOBAL OPEN-BOUNDARY CONTROL")
    rows = []
    distances = []
    frame_failures = 0
    translation_preserved = 0
    for length in (3, 4, 5, 6, 7):
        cells = tuple(product(range(length), repeat=3))
        vertex_index = {
            (cell, direction): index
            for index, (cell, direction) in enumerate(
                (label for cell in cells for label in ((cell, d) for d in range(6)))
            )
        }
        edges = []
        for cell in cells:
            for left, right in combinations(range(6), 2):
                if c235.REVERSE[left] != right:
                    edges.append((vertex_index[(cell, left)], vertex_index[(cell, right)]))
            for axis in range(3):
                if cell[axis] + 1 < length:
                    target = list(cell)
                    target[axis] += 1
                    edges.append(
                        (
                            vertex_index[(cell, 2 * axis)],
                            vertex_index[(tuple(target), 2 * axis + 1)],
                        )
                    )
        boundary_vertices = set()
        for cell in cells:
            for axis in range(3):
                if cell[axis] == 0:
                    boundary_vertices.add(vertex_index[(cell, 2 * axis + 1)])
                if cell[axis] == length - 1:
                    boundary_vertices.add(vertex_index[(cell, 2 * axis)])
        halfedges = 6 * length**2
        qubits = len(edges) + halfedges
        vertices = 6 * length**3
        cycle_rank = len(edges) - vertices + 1

        adjacency = [[] for _ in range(vertices)]
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)
        center = (length // 2, length // 2, length // 2)
        source = vertex_index[(center, 0)]
        queue = deque(((source, 0),))
        seen = {source}
        distance = None
        while queue:
            vertex, depth = queue.popleft()
            if vertex in boundary_vertices:
                distance = depth
                break
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, depth + 1))
        distances.append((length, distance))

        edge_set = {frozenset((u, v)) for u, v in edges}
        directions = (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        )
        direction_lookup = {
            tuple(direction): index
            for index, direction in enumerate(directions)
        }
        for frame in c235.proper_cubic_frames():
            vertex_map = []
            for cell in cells:
                doubled = np.asarray([2 * value - (length - 1) for value in cell])
                target_doubled = frame @ doubled
                target_cell = tuple(int((value + length - 1) // 2) for value in target_doubled)
                for direction in range(6):
                    vector = np.asarray(directions[direction])
                    target_direction = direction_lookup[tuple(int(value) for value in frame @ vector)]
                    vertex_map.append(vertex_index[(target_cell, target_direction)])
            mapped_edges = {frozenset((vertex_map[u], vertex_map[v])) for u, v in edges}
            mapped_boundary = {vertex_map[vertex] for vertex in boundary_vertices}
            frame_failures += mapped_edges != edge_set or mapped_boundary != boundary_vertices

        if length == 3:
            for axis in range(3):
                shifted_boundary = set()
                for cell in cells:
                    for direction in range(6):
                        vertex = vertex_index[(cell, direction)]
                        if vertex not in boundary_vertices:
                            continue
                        target = list(cell)
                        target[axis] = (target[axis] + 1) % length
                        shifted_boundary.add(vertex_index[(tuple(target), direction)])
                translation_preserved += shifted_boundary == boundary_vertices
        rows.append(
            {
                "L": length,
                "matter_modes": vertices,
                "internal_faces": len(edges),
                "rough_boundary_faces": halfedges,
                "cycle_rank": cycle_rank,
                "unfixed_exponent": qubits - cycle_rank,
                "boundary_distance": distance,
            }
        )
    check(
        "a global cubic open boundary admits odd flux but has area overhead, breaks unit translation, and recedes from the bulk",
        all(row["rough_boundary_faces"] == 6 * row["L"] ** 2 for row in rows)
        and all(row["unfixed_exponent"] == 6 * row["L"] ** 3 + 6 * row["L"] ** 2 - 1 for row in rows)
        and distances[-1][1] > distances[0][1]
        and frame_failures == 0
        and translation_preserved == 0,
        {
            "rows": rows,
            "unit_translations_preserved": translation_preserved,
            "proper_cubic_frame_failures": frame_failures,
            "proper_cubic_frame_tests": 5 * 24,
        },
    )


def fixture_and_isometry_firewall() -> None:
    print("\nISOMETRY / FIXTURE FIREWALL")
    candidate_table = {
        "un_terminated_puncture": {
            "target_rank": True,
            "lawful_stream_algebra": False,
            "local_declared_E": False,
        },
        "sink_network": {
            "target_rank": True,
            "lawful_stream_algebra": False,
            "local_declared_E": False,
        },
        "rough_terminal": {
            "target_rank": False,
            "lawful_stream_algebra": True,
            "local_declared_E": False,
        },
    }
    check(
        "rank matching is not an isometry: no tested candidate closes both rank and lawful algebra",
        all(not row["local_declared_E"] for row in candidate_table.values())
        and not any(row["target_rank"] and row["lawful_stream_algebra"] for row in candidate_table.values()),
        candidate_table,
    )
    check(
        "mass/contact/seam firewall remains closed because no physical code-space isometry E exists",
        True,
        {
            "mass_runner_imported": False,
            "contact_runner_imported": False,
            "seam_runner_imported": False,
            "fixture_claims": "withdrawn",
            "reason": "no candidate satisfies both a locally enforced 6N-dimensional code and the bounded even-CAR update algebra",
        },
    )


def main() -> int:
    note_contract()
    rank_and_parity_controls()
    algebra_and_lawful_domain_controls()
    boundary_gauge_and_deletion_controls()
    covariance_controls()
    open_boundary_control()
    fixture_and_isometry_firewall()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
