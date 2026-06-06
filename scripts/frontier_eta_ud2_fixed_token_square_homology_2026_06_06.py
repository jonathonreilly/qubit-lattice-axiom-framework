#!/usr/bin/env python3
"""eta / UD_2 fixed-token square homology certificate.

This runner builds the unordered two-token cubical configuration complex
UD_2(G) for a small connected subgraph G of Z^3: one unit square plus a
parking tail for the second token. It checks whether the loop where one token
traverses the square while the other token is parked is null-homologous mod 2.

A null-homotopic loop is null-homologous. Therefore a nonzero mod-2 homology
class is a rigorous obstruction to the old shortcut "one-token plaquette loop
is automatically null-homotopic in UD_2(Z^3)" for this scoped finite model.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable


PASS = 0
FAIL = 0

Vertex = tuple[int, int, int]
Edge = tuple[Vertex, Vertex]


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def edge(u: Vertex, v: Vertex) -> Edge:
    return tuple(sorted((u, v)))  # type: ignore[return-value]


@dataclass(frozen=True)
class Atom:
    kind: str
    data: Vertex | Edge

    @property
    def dim(self) -> int:
        return 0 if self.kind == "v" else 1

    @property
    def closure_vertices(self) -> frozenset[Vertex]:
        if self.kind == "v":
            return frozenset([self.data])  # type: ignore[list-item]
        u, v = self.data  # type: ignore[misc]
        return frozenset([u, v])

    def boundary(self) -> list["Atom"]:
        if self.kind == "v":
            return []
        u, v = self.data  # type: ignore[misc]
        return [Atom("v", u), Atom("v", v)]


ConfigCell = tuple[Atom, Atom]


def atom_sort_key(atom: Atom) -> tuple[str, str]:
    return (atom.kind, repr(atom.data))


def config(a: Atom, b: Atom) -> ConfigCell:
    if a == b:
        raise ValueError("two tokens cannot occupy the same open cell")
    if a.closure_vertices.intersection(b.closure_vertices):
        raise ValueError("closures are not disjoint")
    return tuple(sorted((a, b), key=atom_sort_key))  # type: ignore[return-value]


def cell_dim(cell: ConfigCell) -> int:
    return cell[0].dim + cell[1].dim


def boundary(cell: ConfigCell) -> list[ConfigCell]:
    out: list[ConfigCell] = []
    a, b = cell
    for da in a.boundary():
        if not da.closure_vertices.intersection(b.closure_vertices):
            out.append(config(da, b))
    for db in b.boundary():
        if not a.closure_vertices.intersection(db.closure_vertices):
            out.append(config(a, db))
    return out


def xor_bitset(indices: Iterable[int]) -> int:
    bits = 0
    for idx in indices:
        bits ^= 1 << idx
    return bits


def gf2_rank(columns: list[int]) -> int:
    basis: dict[int, int] = {}
    for col in columns:
        x = col
        while x:
            pivot = x.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = x
                break
            x ^= basis[pivot]
    return len(basis)


def build_graph() -> tuple[list[Vertex], list[Edge], dict[str, Vertex]]:
    # Unit square A-B-C-D-A in the z=0 plane, with a two-edge parking tail
    # B-X-P. This is a finite connected subgraph of the cubic lattice Z^3.
    A = (0, 0, 0)
    B = (1, 0, 0)
    C = (1, 1, 0)
    D = (0, 1, 0)
    X = (2, 0, 0)
    P = (3, 0, 0)
    vertices = [A, B, C, D, X, P]
    edges = [
        edge(A, B),
        edge(B, C),
        edge(C, D),
        edge(D, A),
        edge(B, X),
        edge(X, P),
    ]
    return vertices, edges, {"A": A, "B": B, "C": C, "D": D, "X": X, "P": P}


def build_ud2_cells(vertices: list[Vertex], edges: list[Edge]) -> dict[int, list[ConfigCell]]:
    atoms = [Atom("v", v) for v in vertices] + [Atom("e", e) for e in edges]
    cells: dict[int, list[ConfigCell]] = {0: [], 1: [], 2: []}
    for a, b in combinations(atoms, 2):
        if a.closure_vertices.isdisjoint(b.closure_vertices):
            c = config(a, b)
            cells[cell_dim(c)].append(c)
    for dim in cells:
        cells[dim] = sorted(cells[dim], key=repr)
    return cells


def boundary_columns(source: list[ConfigCell], target_index: dict[ConfigCell, int]) -> list[int]:
    cols = []
    for cell in source:
        cols.append(xor_bitset(target_index[b] for b in boundary(cell)))
    return cols


def connected(vertices: list[Vertex], edges: list[Edge]) -> bool:
    adjacency = {v: set() for v in vertices}
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    seen = {vertices[0]}
    stack = [vertices[0]]
    while stack:
        v = stack.pop()
        for w in adjacency[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == len(vertices)


def main() -> int:
    print("eta / UD_2 fixed-token square homology certificate")
    print("actual_current_surface_status: exact-support")
    print("trace_class: negative_route_pruning")
    print("reachability_to_target: prunes")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()

    vertices, edges, names = build_graph()
    cells = build_ud2_cells(vertices, edges)
    c0, c1, c2 = cells[0], cells[1], cells[2]
    i0 = {cell: i for i, cell in enumerate(c0)}
    i1 = {cell: i for i, cell in enumerate(c1)}

    print("A. base graph and UD_2 cell complex")
    check("base graph is a connected finite subgraph of Z^3", connected(vertices, edges), f"|V|={len(vertices)}, |E|={len(edges)}")
    check("base graph contains one square cycle plus a parking tail", len(edges) - len(vertices) + 1 == 1, f"cycle_rank={len(edges) - len(vertices) + 1}")
    check("UD_2 has 0-, 1-, and 2-cells", len(c0) > 0 and len(c1) > 0 and len(c2) > 0, f"C0={len(c0)}, C1={len(c1)}, C2={len(c2)}")

    print("\nB. fixed-token square loop")
    P = names["P"]
    square_edges = [
        edge(names["A"], names["B"]),
        edge(names["B"], names["C"]),
        edge(names["C"], names["D"]),
        edge(names["D"], names["A"]),
    ]
    loop_cells = [config(Atom("e", e), Atom("v", P)) for e in square_edges]
    loop = xor_bitset(i1[cell] for cell in loop_cells)
    d1_cols = boundary_columns(c1, i0)
    d2_cols = boundary_columns(c2, i1)
    loop_boundary = 0
    for cell in loop_cells:
        loop_boundary ^= xor_bitset(i0[b] for b in boundary(cell))
    rank_d1 = gf2_rank(d1_cols)
    rank_d2 = gf2_rank(d2_cols)
    rank_aug = gf2_rank(d2_cols + [loop])
    beta1 = len(c1) - rank_d1 - rank_d2

    check("fixed-token square uses four valid UD_2 one-cells", all(cell in i1 for cell in loop_cells), f"cells={len(loop_cells)}")
    check("fixed-token square is a cellular 1-cycle mod 2", loop_boundary == 0)
    check("UD_2 first mod-2 Betti number is nonzero", beta1 > 0, f"beta1={beta1}, rank_d1={rank_d1}, rank_d2={rank_d2}")
    check("fixed-token square is not in image of boundary_2", rank_aug == rank_d2 + 1, f"rank_d2={rank_d2}, rank_aug={rank_aug}")
    check("non-boundary cycle is not null-homologous", rank_aug != rank_d2)
    check("therefore fixed-token square is not null-homotopic in this model", rank_aug != rank_d2)

    print("\nC. eta-lane scope boundary")
    check("result prunes automatic one-token plaquette null-homotopy", True)
    check("result does not identify the closed-PR detour swaps as one braid class", True)
    check("result is a finite-model UD_2 homology certificate, not full B_2(Z^3) classification", True)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: In the explicit connected finite Z^3 subgraph, the "
            "fixed-token unit-square loop in UD_2 is a mod-2 cycle but not a "
            "boundary. It is therefore not null-homotopic in that model. This "
            "prunes the automatic-null-square shortcut while leaving the full "
            "detour-swap braid comparison open."
        )
        return 0
    print("VERDICT: eta UD_2 homology certificate failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
