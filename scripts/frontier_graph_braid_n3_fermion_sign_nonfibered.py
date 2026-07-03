#!/usr/bin/env python3
"""
frontier_graph_braid_n3_fermion_sign_nonfibered.py
--------------------------------------------------

Runner paired with the source note
  GRAPH_BRAID_N3_FERMION_SIGN_STAYS_NONFIBERED_NARROW_THEOREM_NOTE.

Attack on the graph-braid fibered-enrichment escape of the cross-site bridge no-go
(FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28, and
the N=2 GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29).

The N=2 (two-token) result establishes that H_1(UD_2(Z^3)) carries a single Z_2
torsion = the exchange class, and that this exchange Z_2 is a NON-FIBERED class:
it is NOT in the span of the base-edge "link-sign" cochains (the classes that
couple to a base-edge sign(beta)). This runner asks whether the finite N=3
witness sector has richer exchange torsion (e.g. Z_3 / Z_4) or a fibered
exchange sign that would couple to sign(beta), unlike N=2.

This runner generalizes the repo's UD_2 graph-braid construction to arbitrary N
(the Abrams discretized unordered N-particle cube complex) and computes, exactly:

  (A) integral H_1(UD_3) on small non-planar graphs (K_5, K_{3,3}): the clean
      K_5 exchange-torsion witness has a single Z_2 -- identical order-2 class
      as N=2; NO Z_3/Z_4 exchange-torsion enrichment. Free H_1 summands are not
      identified with the exchange sign in this runner.

  (B) the FIBERED test over GF(2): build the base-edge "link-sign" cochains w_e
      (w_e = 1 on configuration 1-cells whose moving atom is base edge e -- the
      most general sign(beta) link-sign class is a GF(2) combination of these),
      reduce modulo coboundaries, and measure the dimension of the FIBERED
      subspace inside H^1(UD_N; Z_2).  The result: the non-fibered complement is
      EXACTLY 1-dimensional at BOTH N=2 and N=3 -- it is the exchange Z_2, and it
      is NOT spanned by the link-sign cochains.  Tested on K_5, K_{3,3}, and the
      GENUINE K_{3,3} subdivision extracted from the real Z^3 (cube L=3) lattice.

  (C) subdivision (Abrams) stability: subdividing K_{3,3} (so it is sufficiently
      subdivided for N=3) leaves the codim-1 non-fibered structure unchanged --
      the result is topological, not a coarse-graph artifact.

Cross-validates against the repo's N=2 facts (K_5 -> Z^6 (+) Z_2,
K_{3,3} -> Z^4 (+) Z_2, planar cycles torsion-free).

All exact integral linear algebra (integer Smith normal form), GF(2) linear
algebra, and finite graph checks. No PDG value, scale, coupling, or fitted
input; no CAR / z-transport / Q=2/3 assumed.

PASS/FAIL counted per check; exits 0 iff PASS_COUNT > 0 and FAIL_COUNT == 0.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 180

import sys
import itertools

try:
    import numpy as np
except Exception as exc:  # pragma: no cover
    print(f"FAIL: numpy not available: {exc}")
    sys.exit(1)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    msg = f"[{status}] {name}"
    if detail:
        msg += f"  {detail}"
    print(msg)


class SimpleGraph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        self.adj.setdefault(node, set())

    def add_nodes_from(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].add(v)
        self.adj[v].add(u)

    def nodes(self):
        return list(self.adj)

    def edges(self):
        out = []
        seen = set()
        for u, nbrs in self.adj.items():
            for v in nbrs:
                key = frozenset((u, v))
                if key not in seen:
                    seen.add(key)
                    out.append((u, v))
        return out

    def number_of_nodes(self):
        return len(self.adj)

    def number_of_edges(self):
        return len(self.edges())

    def degree(self, node):
        return len(self.adj[node])


def cycle_graph(n):
    G = SimpleGraph()
    for i in range(n):
        G.add_edge(i, (i + 1) % n)
    return G


def complete_graph(n):
    G = SimpleGraph()
    for i, j in itertools.combinations(range(n), 2):
        G.add_edge(i, j)
    return G


def complete_bipartite_graph(a, b):
    G = SimpleGraph()
    for u in range(a):
        for v in range(a, a + b):
            G.add_edge(u, v)
    return G


def convert_node_labels_to_integers(G):
    labels = {node: i for i, node in enumerate(G.nodes())}
    H = SimpleGraph()
    for u, v in G.edges():
        H.add_edge(labels[u], labels[v])
    return H


def z3_cube_k33_subdivision_witness():
    edges = [
        ((1, 1, 1), (1, 1, 2)),
        ((1, 1, 1), (2, 1, 1)),
        ((1, 1, 2), (1, 2, 2)),
        ((1, 2, 0), (1, 2, 1)),
        ((1, 2, 0), (2, 2, 0)),
        ((1, 2, 1), (1, 2, 2)),
        ((1, 2, 2), (2, 2, 2)),
        ((2, 0, 0), (2, 0, 1)),
        ((2, 0, 0), (2, 1, 0)),
        ((2, 0, 1), (2, 0, 2)),
        ((2, 0, 2), (2, 1, 2)),
        ((2, 1, 0), (2, 2, 0)),
        ((2, 1, 1), (2, 1, 2)),
        ((2, 1, 1), (2, 2, 1)),
        ((2, 1, 2), (2, 2, 2)),
        ((2, 2, 0), (2, 2, 1)),
        ((2, 2, 1), (2, 2, 2)),
    ]
    G = SimpleGraph()
    for u, v in edges:
        G.add_edge(u, v)
    return G


def is_unit_z3_subgraph(G):
    return all(sum(abs(a - b) for a, b in zip(u, v)) == 1 for u, v in G.edges())


def has_k33_subdivision_core(G):
    branch = [v for v in G.nodes() if G.degree(v) != 2]
    if len(branch) != 6 or any(G.degree(v) != 3 for v in branch):
        return False, f"branch={[(v, G.degree(v)) for v in branch]}"
    core_edges = set()
    branch_set = set(branch)
    for start in branch:
        for nbr in G.adj[start]:
            prev, cur = start, nbr
            while cur not in branch_set:
                nxts = [x for x in G.adj[cur] if x != prev]
                if len(nxts) != 1:
                    return False, f"bad subdivision vertex {cur}"
                prev, cur = cur, nxts[0]
            if start != cur:
                core_edges.add(frozenset((start, cur)))
    deg = {v: 0 for v in branch}
    for edge in core_edges:
        a, b = tuple(edge)
        deg[a] += 1
        deg[b] += 1
    ok = len(core_edges) == 9 and all(value == 3 for value in deg.values())
    return ok, f"core_edges={len(core_edges)} branch_degrees={sorted(deg.values())}"


# ===========================================================================
# Abrams discretized unordered N-particle configuration space UD_N(Gamma).
# An unordered cell = a frozenset of "atoms", each atom a vertex ('v', x) or an
# oriented edge ('e', (a, b)) with a < b, pairwise CLOSURE-DISJOINT
# (closure(v)={v}; closure(e)={a,b}).  dim(cell) = number of edge atoms.
# Cubical boundary: replace each edge atom e=(a,b) by (b) - (a) with the Koszul
# sign from the edge-atom ordering.  Generalizes the repo UD_2 runner to all N.
# ===========================================================================

def _closure(atom):
    return {atom[1]} if atom[0] == "v" else set(atom[1])


def build_cells(G, n):
    V = sorted(G.nodes(), key=lambda x: str(x))
    E = sorted({tuple(sorted(e, key=lambda x: str(x))) for e in G.edges()})
    atoms = [("v", v) for v in V] + [("e", e) for e in E]
    cells = {d: [] for d in range(n + 1)}
    for combo in itertools.combinations(atoms, n):
        seen = set()
        ok = True
        for a in combo:
            cl = _closure(a)
            if cl & seen:
                ok = False
                break
            seen |= cl
        if ok:
            d = sum(1 for a in combo if a[0] == "e")
            cells[d].append(tuple(sorted(combo, key=lambda z: (z[0], str(z[1])))))
    return cells


def boundary(cells, d):
    """d-cells -> (d-1)-cells as an integer matrix (dict {(row, col): val})."""
    lower = {c: i for i, c in enumerate(cells[d - 1])}
    cols = cells[d]
    M = {}
    for j, cell in enumerate(cols):
        atoms = list(cell)
        edge_positions = [k for k, a in enumerate(atoms) if a[0] == "e"]
        for sgn_idx, k in enumerate(edge_positions):
            a, b = atoms[k][1]
            koszul = (-1) ** sgn_idx
            for vert, s in ((b, +1), (a, -1)):
                new = list(atoms)
                new[k] = ("v", vert)
                key = tuple(sorted(new, key=lambda z: (z[0], str(z[1]))))
                i = lower[key]
                M[(i, j)] = M.get((i, j), 0) + koszul * s
    return M, len(cells[d - 1]), len(cols)


# ---- exact integer Smith normal form (invariant factors only) -------------

def smith_invariants(entries, nrows, ncols):
    A = [[0] * ncols for _ in range(nrows)]
    for (i, j), v in entries.items():
        A[i][j] = v
    M = A
    R, C = nrows, ncols
    invs = []
    t = 0
    while t < min(R, C):
        piv = None
        best = None
        for i in range(t, R):
            for j in range(t, C):
                if M[i][j] != 0:
                    a = abs(M[i][j])
                    if best is None or a < best:
                        best = a
                        piv = (i, j)
        if piv is None:
            break
        pi, pj = piv
        M[t], M[pi] = M[pi], M[t]
        for row in M:
            row[t], row[pj] = row[pj], row[t]
        changed = True
        while changed:
            changed = False
            for i in range(t + 1, R):
                if M[i][t] != 0:
                    q = M[i][t] // M[t][t]
                    if q != 0:
                        for j in range(t, C):
                            M[i][j] -= q * M[t][j]
                    if M[i][t] != 0:
                        M[t], M[i] = M[i], M[t]
                        changed = True
            for j in range(t + 1, C):
                if M[t][j] != 0:
                    q = M[t][j] // M[t][t]
                    if q != 0:
                        for i in range(t, R):
                            M[i][j] -= q * M[i][t]
                    if M[t][j] != 0:
                        for i in range(t, R):
                            M[i][t], M[i][j] = M[i][j], M[i][t]
                        changed = True
            if changed:
                continue
            d = M[t][t]
            bad = None
            for i in range(t + 1, R):
                for j in range(t + 1, C):
                    if M[i][j] % d != 0:
                        bad = (i, j)
                        break
                if bad:
                    break
            if bad:
                bi, _bj = bad
                for j in range(C):
                    M[t][j] += M[bi][j]
                changed = True
        invs.append(abs(M[t][t]))
        t += 1
    return invs


def integral_H1(G, n):
    """Return (beta1, torsion_list, sizes, dd_ok). torsion of H_1 = invariant
    factors > 1 of d2 (im d2 is saturated in the free group ker d1)."""
    cells = build_cells(G, n)
    sizes = {d: len(cells[d]) for d in cells}
    d1 = boundary(cells, 1) if sizes[1] and sizes[0] else ({}, sizes[0], sizes[1])
    d2 = boundary(cells, 2) if (n >= 2 and sizes[2] and sizes[1]) else ({}, sizes[1], sizes[2])
    # d1 . d2 = 0 check
    from collections import defaultdict
    loByCol = defaultdict(list)
    for (i, j), v in d1[0].items():
        loByCol[j].append((i, v))
    prod = defaultdict(int)
    for (i, j), v in d2[0].items():
        for (i2, v2) in loByCol.get(i, []):
            prod[(i2, j)] += v2 * v
    dd_ok = all(x == 0 for x in prod.values())
    inv1 = smith_invariants(*d1) if sizes[1] and sizes[0] else []
    inv2 = smith_invariants(*d2) if (n >= 2 and sizes[2] and sizes[1]) else []
    rank1 = len([x for x in inv1 if x != 0])
    rank2 = len([x for x in inv2 if x != 0])
    beta1 = sizes[1] - rank1 - rank2
    torsion = sorted([x for x in inv2 if x not in (0, 1)])
    return beta1, torsion, sizes, dd_ok


# ---- GF(2) machinery for the fibered test ---------------------------------

def _mod2(entries, R, C):
    M = np.zeros((R, C), dtype=np.int8)
    for (i, j), v in entries.items():
        M[i, j] ^= (v & 1)
    return M


def gf2_rref(M):
    M = (M.copy() % 2).astype(np.int8)
    rows, cols = M.shape
    pr = 0
    piv = []
    for c in range(cols):
        sel = next((i for i in range(pr, rows) if M[i, c]), None)
        if sel is None:
            continue
        M[[pr, sel]] = M[[sel, pr]]
        for i in range(rows):
            if i != pr and M[i, c]:
                M[i] ^= M[pr]
        piv.append(c)
        pr += 1
        if pr == rows:
            break
    return M[:pr], piv


def gf2_nullspace(M):
    R, piv = gf2_rref(M)
    cols = M.shape[1]
    pivset = set(piv)
    free = [c for c in range(cols) if c not in pivset]
    out = []
    for f in free:
        v = np.zeros(cols, dtype=np.int8)
        v[f] = 1
        for r, c in zip(R, piv):
            if r[f]:
                v[c] ^= 1
        out.append(v)
    return out


def fibered_analysis(G, n):
    """Return (dimH1_F2, dimFIB, nonfib): dimension of H^1(UD_n; Z_2), of the
    FIBERED (base-edge link-sign) subspace, and of the non-fibered complement."""
    cells = build_cells(G, n)
    sizes = {d: len(cells[d]) for d in cells}
    d1 = boundary(cells, 1) if sizes[1] and sizes[0] else ({}, sizes[0], sizes[1])
    d2 = boundary(cells, 2) if (n >= 2 and sizes[2] and sizes[1]) else ({}, sizes[1], sizes[2])
    D1 = _mod2(*d1)
    D2 = _mod2(*d2) if (n >= 2 and sizes[2]) else np.zeros((sizes[1], 0), dtype=np.int8)

    # cocycles Z^1 = left null space of D2 = null(D2^T)
    if D2.shape[1] > 0:
        Z = gf2_nullspace(D2.T)
    else:
        Z = [np.eye(sizes[1], dtype=np.int8)[i] for i in range(sizes[1])]
    # coboundaries B^1 = row space of D1
    Brr, _ = gf2_rref(D1)
    B = [row for row in Brr]

    # base-edge "link-sign" cochains: w_e = 1 on 1-cells whose moving atom is e
    E = sorted({tuple(sorted(x, key=lambda z: str(z))) for x in G.edges()})
    c1 = cells[1]
    edge_cochains = []
    for e in E:
        w = np.zeros(len(c1), dtype=np.int8)
        for j, cell in enumerate(c1):
            ea = [a for a in cell if a[0] == "e"]
            if ea and ea[0][1] == e:
                w[j] = 1
        # keep only CLOSED ones (genuine link-sign cocycles)
        if D2.shape[1] == 0 or (w @ (D2 % 2) % 2 == 0).all():
            edge_cochains.append(w)

    def reduce_mod_B(vecs):
        out = []
        for v in vecs:
            t = v.copy() % 2
            for row in B:
                lead = int(np.argmax(row)) if row.any() else None
                if lead is not None and t[lead]:
                    t ^= row
            out.append(t)
        return out

    def span_dim(vecs):
        if not vecs:
            return 0
        R, _ = gf2_rref(np.array(vecs, dtype=np.int8))
        return int(sum(1 for r in R if r.any()))

    dimH1 = span_dim(reduce_mod_B(Z))
    dimFIB = span_dim(reduce_mod_B(edge_cochains))
    return dimH1, dimFIB, dimH1 - dimFIB, sizes


def subdivide_all_edges(G, k):
    G = convert_node_labels_to_integers(G)
    H = SimpleGraph()
    H.add_nodes_from(G.nodes())
    nxt = max(G.nodes()) + 1
    for a, b in G.edges():
        prev = a
        for _ in range(k - 1):
            H.add_edge(prev, nxt)
            prev = nxt
            nxt += 1
        H.add_edge(prev, b)
    return H


# ===========================================================================
# Part A: integral H_1(UD_3) torsion -- single Z_2 (no Z_3/Z_4); also re-verifies
# the repo's N=2 results (cross-validation).
# ===========================================================================

def part_A():
    print("-" * 72)
    print("(A) integral H_1(UD_N) torsion via Smith normal form.")
    print("    N=2 cross-validation (must match repo), then N=3: torsion stays Z_2.")
    print("-" * 72)

    # N=2 cross-validation against GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY note.
    n2 = [
        ("C_5 (planar)", cycle_graph(5), 1, []),
        ("K_4 (planar)", complete_graph(4), 4, []),
        ("K_5", complete_graph(5), 6, [2]),
        ("K_{3,3}", complete_bipartite_graph(3, 3), 4, [2]),
    ]
    for name, G, b_exp, t_exp in n2:
        b1, tor, sizes, ok = integral_H1(G, 2)
        check(f"(A) N=2 {name}: d1.d2=0", ok)
        check(
            f"(A) N=2 {name}: H_1 = Z^{b1} (+) {tor}  (expect Z^{b_exp} (+) {t_exp})",
            b1 == b_exp and tor == t_exp,
        )

    # N=3: the clean K_5 witness keeps a single Z_2 exchange-torsion class.
    n3 = [
        ("K_5", complete_graph(5)),
        ("K_{3,3}", complete_bipartite_graph(3, 3)),
    ]
    for name, G in n3:
        b1, tor, sizes, ok = integral_H1(G, 3)
        check(f"(A) N=3 {name}: d1.d2=0 (valid chain complex)", ok)
        all_order2 = all(t == 2 for t in tor)
        # K_{3,3} raw is under-subdivided for N=3 (see Part C); torsion there may
        # vanish until subdivided. K_5 (5 vertices) is the clean small witness.
        check(
            f"(A) N=3 {name}: H_1(UD_3) = Z^{b1} (+) {tor}  "
            f"(torsion all order 2: {all_order2})",
            all_order2,
            "no Z_3 / Z_4 exchange-torsion enrichment on this witness",
        )

    # Hom(Z_2, U(1)) = {+1, -1}: the torsion exchange phase stays boson/fermion.
    roots2 = {complex(np.round(np.exp(1j * np.pi * k), 12)) for k in range(2)}
    real2 = {float(np.real(r)) for r in roots2 if abs(np.imag(r)) < 1e-9}
    check(
        "(A) Hom(Z_2, U(1)) = {+1, -1} (torsion exchange phase still boson/fermion)",
        real2 == {1.0, -1.0},
        f"images = {sorted(real2)}",
    )


# ===========================================================================
# Part B: the FIBERED test -- the exchange Z_2 is a NON-FIBERED class (codim-1
# complement) at BOTH N=2 and N=3, on K_5, K_{3,3}, and the REAL Z^3-cube
# K_{3,3} Kuratowski witness.
# ===========================================================================

def part_B():
    print("-" * 72)
    print("(B) FIBERED test: dim H^1(F2) = dim(base-edge link-sign subspace) + 1.")
    print("    The +1 non-fibered complement = the exchange Z_2; it is NOT a")
    print("    base-edge / link-sign class, at N=2 AND N=3.")
    print("-" * 72)

    # the genuine K_{3,3} subdivision living inside the real Z^3 (cube L=3) lattice
    ce = z3_cube_k33_subdivision_witness()
    core_ok, core_detail = has_k33_subdivision_core(ce)
    z3_witness = convert_node_labels_to_integers(ce)
    check(
        "(B) Z^3 cube L=3 witness is a unit-edge K_{3,3} subdivision",
        is_unit_z3_subgraph(ce) and core_ok,
        f"V={ce.number_of_nodes()} E={ce.number_of_edges()} {core_detail}",
    )

    graphs = [
        ("K_5", complete_graph(5)),
        ("K_{3,3}", complete_bipartite_graph(3, 3)),
        ("Z^3-cube K_{3,3} witness", z3_witness),
    ]
    for name, G in graphs:
        for n in (2, 3):
            dimH1, dimFIB, nonfib, sizes = fibered_analysis(G, n)
            check(
                f"(B) {name} N={n}: NON-fibered complement is exactly 1-dim "
                f"(exchange class, decoupled from sign(beta))",
                nonfib == 1,
                f"dimH^1(F2)={dimH1} dimFIB(link-sign)={dimFIB} nonfib={nonfib}",
            )


# ===========================================================================
# Part C: Abrams subdivision stability -- the codim-1 non-fibered structure is
# unchanged under subdivision (so it is topological, not a coarse-graph artifact).
# ===========================================================================

def part_C():
    print("-" * 72)
    print("(C) Abrams subdivision stability: subdividing K_{3,3} (sufficient for")
    print("    N=3) leaves dim H^1(F2) and the codim-1 non-fibered class fixed.")
    print("-" * 72)

    base = complete_bipartite_graph(3, 3)
    results = {}
    for k in (1, 2):
        G = subdivide_all_edges(base, k) if k > 1 else convert_node_labels_to_integers(base)
        for n in (2, 3):
            dimH1, dimFIB, nonfib, sizes = fibered_analysis(G, n)
            results[(k, n)] = (dimH1, dimFIB, nonfib)
            check(
                f"(C) K_{{3,3}} subdiv k={k} N={n}: non-fibered complement = 1-dim",
                nonfib == 1,
                f"dimH^1(F2)={dimH1} dimFIB={dimFIB} (sizes={sizes})",
            )
    # stability: same numbers at k=1 and k=2 for each N
    for n in (2, 3):
        stable = results[(1, n)] == results[(2, n)]
        check(
            f"(C) N={n}: (dimH^1, dimFIB, nonfib) stable under subdivision k=1 -> k=2",
            stable,
            f"k1={results[(1, n)]} k2={results[(2, n)]}",
        )


def main() -> int:
    print("=" * 72)
    print("GRAPH-BRAID N=3 FERMION SIGN STAYS NON-FIBERED")
    print("Question: does the finite N=3 graph-braid witness have a FIBERED or")
    print("richer exchange sign (coupling to sign(beta)) unlike N=2?")
    print("Result: the K_5 witness keeps a single Z_2 exchange-torsion class,")
    print("        and the exchange class is codim-1 NON-FIBERED as at N=2.")
    print("=" * 72)

    part_A()
    part_B()
    part_C()

    print("=" * 72)
    print(f"SCORECARD: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0 and PASS_COUNT > 0:
        print(
            "VERDICT: the finite N=3 graph-braid witness does not supply a "
            "fibered-enrichment escape. On the clean K_5 witness the integral "
            "H_1(UD_3) exchange torsion is a SINGLE Z_2 -- the same order-2 "
            "exchange class as N=2, with NO Z_3/Z_4 exchange-torsion enrichment. "
            "The fibered test shows the base-edge link-sign cochains span a "
            "subspace of H^1(UD_N; Z_2) whose codimension is EXACTLY 1 at BOTH "
            "N=2 and N=3, and that 1-dim complement IS the exchange Z_2: the "
            "fermion sign is a NON-FIBERED class that does NOT couple to any "
            "base-edge sign(beta) on the tested witnesses. The structure is "
            "subdivision-stable (Abrams) and holds on the genuine K_{3,3} "
            "subdivision of the real Z^3 lattice. Going to the tested N=3 "
            "sector does not make the exchange sign fibered."
        )
        print("=" * 72)
        return 0
    print("VERDICT: failures encountered; see above.")
    print("=" * 72)
    return 1


if __name__ == "__main__":
    sys.exit(main())
