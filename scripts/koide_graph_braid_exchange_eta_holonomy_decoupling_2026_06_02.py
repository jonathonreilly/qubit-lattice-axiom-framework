#!/usr/bin/env python3
"""
koide_graph_braid_exchange_eta_holonomy_decoupling_2026_06_02.py
----------------------------------------------------------------

Runner paired with
  KOIDE_GRAPH_BRAID_EXCHANGE_ETA_HOLONOMY_DECOUPLING_NARROW_NO_GO_NOTE_2026-06-02.md

Source-only proposal. Status authority: independent audit lane only.

QUESTION (the lattice-native graph-braid route R1 to the charged-lepton carrier
bridge). The retained graph-braid theorem
  graph_braid_z3_anyon_exclusion_dichotomy_narrow_theorem_note_2026-05-29
proves H_1(UD_2(Z^3)) = Z^b1 (+) Z_2, with the two-particle EXCHANGE class
generating the Z_2 torsion. The open R1 route asks: can the EXCHANGE Z_2,
WEIGHTED by the staggered cross-site hopping sign eta (a base-graph link sign,
= the carrier's sign(beta) connection), carry a NONTRIVIAL fermionic sign --
i.e. is the graph-braid exchange NATIVELY the sign(beta)/CAR exchange, discharging
the records-Z_2 without any continuum Finkelstein-Rubinstein import?

ANSWER (this runner, exactly): NO. The integral Z_2 exchange generator t of
UD_2(Gamma) has, for every base edge e, a NET-EVEN moving-token multiplicity, so
its base-edge projection P(t) = 0 (mod 2). Therefore for EVERY base-graph Z_2
link connection eta : E -> {0,1} (the staggered hopping sign included), the
eta-holonomy of the exchange class is
    Hol_eta(t) = (-1)^<eta, P(t)> = (-1)^0 = +1.
The exchange Z_2 is DECOUPLED from every base-edge connection: no staggered
hopping sign / sign(beta) can be put onto the swap. Equivalently, the fermionic
swap sign DOES exist as a config-space 1-cocycle on UD_2 (H^1(UD_2;Z_2) has a
class that is -1 on t), but that cocycle is NOT the lift of any base-edge
connection -- it is non-fibered config-space ('framing') data. And the on-site
discrete-rotation moves are exactly the 2-cells (im d2), which the exchange
torsion class survives by construction, so no discrete on-site 2O rotation loop
is homotopic to the swap (centrality obstruction, made exact).

VERDICT (c)+(d): R1's eta-weighted cross-site route does NOT discharge the
records-Z_2 natively. The graph-braid exchange Z_2 is decoupled from sign(beta)
by an exact homological invariant (P(t)=0 mod 2), verified on K_{3,3}, K_5,
subdivided (tokens-have-room) variants, AND a genuine non-planar cubic-lattice
slab 3x3x2 of Z^3. The fermion swap sign is config-space ('framing') data not
carried by any link connection -- the precise residual the next path must supply.

This is a NEGATIVE narrowing. It does NOT assume CAR, sign(beta), or Q=2/3 as
inputs; it tests them. It introduces NO axiom and NO import. It does NOT overturn
the retained graph-braid theorem (it builds on it) and does NOT close any positive
theorem. Standard mathematics only (graph-braid cube complex, integral Smith
normal form, GF(2) cohomology).

PASS/FAIL counted per-check; exits 0 iff PASS_COUNT > 0 and FAIL_COUNT == 0.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300

import sys
from itertools import combinations
from collections import defaultdict

try:
    import numpy as np
except Exception as exc:  # pragma: no cover
    print(f"FAIL: numpy not available: {exc}")
    sys.exit(1)

try:
    import networkx as nx
except Exception as exc:  # pragma: no cover
    print(f"FAIL: networkx not available: {exc}")
    sys.exit(1)

try:
    import sympy
except Exception as exc:  # pragma: no cover
    print(f"FAIL: sympy not available: {exc}")
    sys.exit(1)


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"[{status}] {name}"
    if detail:
        msg += f"  {detail}"
    print(msg)


# ===========================================================================
# Abrams discretized unordered 2-particle configuration space UD_2(Gamma).
# (Construction identical to the retained graph-braid runner; reused, not redone.)
#   0-cells {u,v}  : distinct vertex pairs
#   1-cells {w,e}  : vertex w not an endpoint of edge e  (w stationary, other moves on e)
#   2-cells {e,f}  : vertex-disjoint edge pair          (both tokens move simultaneously)
#   d1{w,e=(a,b)} = {w,b}-{w,a}
#   d2{e=(a,b),f=(c,d)} = {b,f}-{a,f}-{d,e}+{c,e}
# ===========================================================================

def cells_UD2(G):
    V = sorted(G.nodes(), key=lambda x: (str(type(x)), x))
    E = sorted({tuple(sorted(e, key=lambda x: (str(type(x)), x))) for e in G.edges()})
    c0 = [frozenset(p) for p in combinations(V, 2)]
    c1 = [(w, e) for w in V for e in E if w not in e]
    c2 = [(e, f) for e, f in combinations(E, 2) if set(e).isdisjoint(set(f))]
    return V, E, c0, c1, c2


def boundary1(c0, c1):
    idx0 = {c: i for i, c in enumerate(c0)}
    M = sympy.zeros(len(c0), len(c1))
    for j, (w, e) in enumerate(c1):
        a, b = e
        M[idx0[frozenset((w, b))], j] += 1
        M[idx0[frozenset((w, a))], j] -= 1
    return M


def boundary2(c1, c2):
    idx1 = {c: i for i, c in enumerate(c1)}
    M = sympy.zeros(len(c1), len(c2))
    for j, (e, f) in enumerate(c2):
        a, b = e
        c_, d_ = f
        for vert, edge, sgn in ((b, f, +1), (a, f, -1), (d_, e, -1), (c_, e, +1)):
            M[idx1[(vert, edge)], j] += sgn
    return M


def smith_with_transforms(A):
    """Integer Smith normal form: returns (D, U, V) with U*A*V = D, U,V unimodular."""
    A = A.copy().applyfunc(lambda x: sympy.Integer(int(x)))
    m, n = A.shape
    U = sympy.eye(m)
    V = sympy.eye(n)
    t = 0
    while t < min(m, n):
        piv = None
        best = None
        for i in range(t, m):
            for j in range(t, n):
                if A[i, j] != 0:
                    v = abs(A[i, j])
                    if best is None or v < best:
                        best = v
                        piv = (i, j)
        if piv is None:
            break
        pi, pj = piv
        if pi != t:
            A.row_swap(t, pi)
            U.row_swap(t, pi)
        if pj != t:
            A.col_swap(t, pj)
            V.col_swap(t, pj)
        changed = True
        while changed:
            changed = False
            for i in range(t + 1, m):
                if A[i, t] != 0:
                    q = A[i, t] // A[t, t]
                    A[i, :] = A[i, :] - q * A[t, :]
                    U[i, :] = U[i, :] - q * U[t, :]
                    if A[i, t] != 0:
                        A.row_swap(t, i)
                        U.row_swap(t, i)
                        changed = True
            for j in range(t + 1, n):
                if A[t, j] != 0:
                    q = A[t, j] // A[t, t]
                    A[:, j] = A[:, j] - q * A[:, t]
                    V[:, j] = V[:, j] - q * V[:, t]
                    if A[t, j] != 0:
                        A.col_swap(t, j)
                        V.col_swap(t, j)
                        changed = True
        t += 1
    return A, U, V


def torsion_generators(d2, order=2):
    """Integral coords of cycles generating each Z_order torsion summand of
    C_1/im(d2). With U*d2*V=D, im(d2)=im(U^{-1} D); in the basis (U^{-1})[:,i] the
    invariant factor D[i,i]=m>1 gives a Z_m class generated by (U^{-1})[:,i]."""
    D, U, V = smith_with_transforms(d2)
    Uinv = U.inv()
    gens = []
    for i in range(min(D.shape)):
        if abs(int(D[i, i])) == order:
            gens.append(Uinv[:, i])
    return gens, D


def integral_in_image(d2, target):
    """True iff target is in im(d2) over Z (via SNF transforms)."""
    D, U, V = smith_with_transforms(d2)
    y = U * target
    r = min(D.shape)
    for i in range(D.shape[0]):
        di = int(D[i, i]) if i < r else 0
        if di == 0:
            if int(y[i]) != 0:
                return False
        else:
            if int(y[i]) % di != 0:
                return False
    return True


def base_edge_multiplicities(coords, c1):
    """Net integer multiplicity of each base edge in the moving-token slot of a chain."""
    mult = defaultdict(int)
    for i in range(len(c1)):
        ci = int(coords[i])
        if ci:
            w, e = c1[i]
            mult[e] += ci
    return dict(mult)


def gf2_nullspace_rows(M_rows, ncols):
    """Right-nullspace basis over GF(2) of the matrix whose rows are M_rows (each len ncols)."""
    A = (np.array(M_rows, dtype=np.int64) % 2) if M_rows else np.zeros((0, ncols), dtype=np.int64)
    m = A.shape[0]
    n = ncols
    where = [-1] * n
    piv = []
    row = 0
    A = A.copy()
    for col in range(n):
        sel = -1
        for r in range(row, m):
            if A[r, col]:
                sel = r
                break
        if sel == -1:
            continue
        A[[row, sel]] = A[[sel, row]]
        for r in range(m):
            if r != row and A[r, col]:
                A[r] ^= A[row]
        where[col] = row
        piv.append(col)
        row += 1
    free = [c for c in range(n) if where[c] == -1]
    basis = []
    for f in free:
        v = np.zeros(n, dtype=np.int8)
        v[f] = 1
        for col in piv:
            if A[where[col], f]:
                v[col] = 1
        basis.append(v)
    return basis


# ===========================================================================
# Part A. Exchange-class base-edge holonomy decoupling: P(t)=0 mod 2.
# ===========================================================================

def analyze_decoupling(name, G, expect_torsion=True, do_cocycle=True, rng_trials=400):
    G = nx.convert_node_labels_to_integers(G)
    V, E, c0, c1, c2 = cells_UD2(G)
    d1 = boundary1(c0, c1)
    d2 = boundary2(c1, c2)
    d1d2_zero = all(v == 0 for v in (d1 * d2)) if (c1 and c2) else True
    check(f"(A) {name}: d1.d2 = 0 (valid cube complex)", d1d2_zero,
          f"|V|={len(V)} |E|={len(E)} |c1|={len(c1)} |c2|={len(c2)}")

    gens, D = torsion_generators(d2, 2)
    if expect_torsion:
        check(f"(A) {name}: H_1(UD_2) carries a Z_2 exchange-torsion summand",
              len(gens) >= 1, f"#Z_2 gens={len(gens)}")
    if not gens:
        return

    t = gens[0]
    is_cycle = all(v == 0 for v in (d1 * t))
    check(f"(A) {name}: exchange generator t is a 1-cycle (d1 t = 0)", is_cycle)

    # t is an honest order-2 torsion class: t NOT integrally in im(d2), but 2t IS.
    t_in = integral_in_image(d2, t)
    twot_in = integral_in_image(d2, 2 * t)
    check(f"(A) {name}: t NOT integrally in im(d2)  (generates Z_2)", not t_in)
    check(f"(A) {name}: 2t IS integrally in im(d2)  (order exactly 2)", twot_in)

    # THE DECISIVE INVARIANT: base-edge projection P(t) = 0 mod 2.
    mult = base_edge_multiplicities(t, c1)
    odd_edges = [e for e, m in mult.items() if m % 2 != 0]
    check(f"(A) {name}: P(t) = 0 mod 2  (every base edge net-EVEN in the swap)",
          len(odd_edges) == 0, f"#odd-multiplicity base edges = {len(odd_edges)}")

    # CONSEQUENCE: every base-edge Z_2 connection eta gives Hol_eta(t) = +1.
    edge_list = list(E)
    tvec = np.array([int(t[i]) % 2 for i in range(len(c1))], dtype=np.int8)
    cell_edge = [c1[i][1] for i in range(len(c1))]
    eidx = {e: i for i, e in enumerate(edge_list)}
    all_plus = True
    worst = None
    rng = np.random.default_rng(12345)
    for _ in range(rng_trials):
        eta = rng.integers(0, 2, size=len(edge_list))
        expo = 0
        for i in range(len(c1)):
            if tvec[i]:
                expo ^= int(eta[eidx[cell_edge[i]]])
        if expo != 0:
            all_plus = False
            worst = expo
            break
    check(f"(A) {name}: EVERY base-edge eta gives Hol_eta(exchange)=+1 "
          f"({rng_trials} random eta, incl. staggered-type sign)",
          all_plus, "" if all_plus else f"counterexample exponent={worst}")
    # Two explicit, concrete base-edge Z_2 connections (the staggered hopping
    # sign is exactly an object of this form): (i) the uniform all-ones link sign;
    # (ii) a Kogut-Susskind-type staggered link sign eta(e) = (lower-endpoint
    # label parity). Both are honest elements of C^1(Gamma; Z_2); each is shown
    # to give Hol_eta(exchange) = +1, as P(t)=0 mod 2 forces.
    for label, eta_map in (
        ("uniform all-ones link sign", {e: 1 for e in edge_list}),
        ("Kogut-Susskind-type staggered link sign (lower-endpoint parity)",
         {e: (min(e) % 2) for e in edge_list}),
    ):
        expo = 0
        for i in range(len(c1)):
            if tvec[i]:
                expo ^= eta_map[cell_edge[i]]
        check(f"(A) {name}: explicit {label} -> Hol_eta(exchange) = "
              f"{'+1' if expo == 0 else '-1'}", expo == 0)

    if do_cocycle:
        # The swap sign DOES exist as a config-space cocycle, but it is NOT a base-eta lift.
        # Cocycles over GF(2): c with c.d2 = 0 (delta c = 0). Columns of d2 give the
        # constraints; nullspace of d2^T over GF(2) = the 1-cocycles.
        # rows of d2^T = columns of d2 -> length |c1|
        d2_arr = np.array(d2.tolist(), dtype=object).astype(np.int64) % 2  # |c1| x |c2|
        d2T_rows = [d2_arr[:, j].tolist() for j in range(d2_arr.shape[1])]
        cocycles = gf2_nullspace_rows(d2T_rows, len(c1))
        found = None
        for cc in cocycles:
            if int(cc @ tvec) % 2 == 1:
                found = cc
                break
        check(f"(A) {name}: a UD_2 1-cocycle phi with phi(exchange) = -1 EXISTS "
              f"(fermion swap sign is realizable config-space data)",
              found is not None, f"dim Z^1(GF2)={len(cocycles)}")
        if found is not None:
            fiber = defaultdict(set)
            for i in range(len(c1)):
                fiber[cell_edge[i]].add(int(found[i]))
            is_baselift = all(len(s) == 1 for s in fiber.values())
            check(f"(A) {name}: that swap-sign cocycle is NOT a base-edge (eta) lift "
                  f"(non-fibered = framing data, not a hopping connection)",
                  not is_baselift)


# ===========================================================================
# Part B. On-site discrete-rotation moves are the 2-cells; exchange survives them.
# ===========================================================================

def analyze_onsite(name, G):
    """Simultaneous on-site moves (a discrete rotation moving both tokens) are
    exactly the 2-cells {e,f} -> their boundaries lie in im(d2). The exchange
    torsion class is, by definition, ker(d1)/im(d2): it is NOT in im(d2), so it
    survives every combination of simultaneous (rotation) moves. Hence no discrete
    on-site rotation loop is homologous to the swap -- the on-site 2O Z_2 and the
    positional exchange Z_2 are decoupled (centrality obstruction, exact)."""
    G = nx.convert_node_labels_to_integers(G)
    V, E, c0, c1, c2 = cells_UD2(G)
    d1 = boundary1(c0, c1)
    d2 = boundary2(c1, c2)
    gens, D = torsion_generators(d2, 2)
    if not gens:
        check(f"(B) {name}: (no torsion to test)", True)
        return
    t = gens[0]
    # Any cycle built from simultaneous-move (2-cell) boundaries is in im(d2);
    # the exchange t is NOT in im(d2). So no rotation-2-cell combination equals t.
    not_reachable = not integral_in_image(d2, t)
    check(f"(B) {name}: exchange t NOT reachable by simultaneous-move (2-cell) "
          f"boundaries => no on-site rotation loop is homotopic to the swap",
          not_reachable)
    # Sanity: the 2-cells (rotation moves) generate im(d2), whose homology image is 0.
    # A pure rotation loop (sum of 2-cell boundaries) has trivial H_1 class.
    if c2:
        sample_col = d2[:, 0]
        sample_is_boundary = integral_in_image(d2, sample_col)
        check(f"(B) {name}: a simultaneous-move (2-cell) boundary is in im(d2) "
              f"(trivial in H_1) -- carries no exchange sign", sample_is_boundary)


# ===========================================================================
# Main
# ===========================================================================

def main() -> int:
    print("=" * 74)
    print("GRAPH-BRAID EXCHANGE vs STAGGERED HOPPING SIGN (eta) HOLONOMY")
    print("Note: KOIDE_GRAPH_BRAID_EXCHANGE_ETA_HOLONOMY_DECOUPLING_NARROW_NO_GO_"
          "NOTE_2026-06-02.md")
    print("Builds ON retained graph_braid_z3_anyon_exclusion_dichotomy "
          "(H_1(UD_2(Z^3))=Z^b1(+)Z_2).")
    print("Tests R1: can eta (= sign(beta) link connection) sign the exchange Z_2?")
    print("=" * 74)

    print("-" * 74)
    print("(A) Base-edge projection of the exchange class: P(t)=0 mod 2 =>")
    print("    every base-graph Z_2 connection eta (staggered hopping sign included)")
    print("    has Hol_eta(exchange)=+1.  The swap sign exists only as non-fibered")
    print("    config-space (framing) data, NOT as a hopping connection.")
    print("-" * 74)
    # K_{3,3} and K_5: smallest non-planar graphs carrying the Z_2 (the Z^3
    # Kuratowski obstructions). Subdivided variants: tokens genuinely have room to
    # pass. 3x3x2 slab: a GENUINE non-planar cubic-lattice piece of Z^3.
    analyze_decoupling("K_{3,3}", nx.complete_bipartite_graph(3, 3))
    analyze_decoupling("K_5", nx.complete_graph(5))
    analyze_decoupling("K_{3,3} subdivided x1 (room to pass)",
                       _subdivide(nx.complete_bipartite_graph(3, 3), 1),
                       do_cocycle=False)
    analyze_decoupling("Z^3 cubic-lattice slab 3x3x2 (non-planar)",
                       nx.grid_graph(dim=[3, 3, 2]), do_cocycle=False)

    print("-" * 74)
    print("(B) On-site discrete-rotation moves = 2-cells (im d2); the exchange")
    print("    torsion survives them => no on-site 2O rotation loop is homotopic")
    print("    to the swap (centrality obstruction, exact).")
    print("-" * 74)
    analyze_onsite("K_{3,3}", nx.complete_bipartite_graph(3, 3))
    analyze_onsite("K_5", nx.complete_graph(5))

    print("=" * 74)
    print(f"SCORECARD: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0 and PASS_COUNT > 0:
        print(
            "VERDICT: R1's eta-weighted cross-site route does NOT discharge the "
            "records-Z_2 natively. The integral Z_2 exchange generator t of "
            "UD_2(Gamma) has base-edge projection P(t)=0 mod 2 (every base edge "
            "net-even in the swap), on K_{3,3}, K_5, a subdivided variant, AND a "
            "genuine non-planar cubic-lattice slab 3x3x2 of Z^3. So EVERY base-graph "
            "Z_2 link connection eta -- the staggered hopping sign / sign(beta) "
            "included -- gives Hol_eta(exchange)=+1: the graph-braid exchange Z_2 is "
            "DECOUPLED from sign(beta). The fermionic swap sign exists as a UD_2 "
            "config-space 1-cocycle (H^1(UD_2;Z_2)) but is NOT the lift of any "
            "hopping connection (non-fibered framing data). On-site discrete-rotation "
            "moves are the 2-cells, which the exchange survives, so no on-site 2O "
            "rotation loop is homotopic to the swap. NET: verdict (c)+(d) -- the route "
            "reduces to the (now exact, holonomy-level) centrality obstruction, with "
            "the precise residual = the non-fibered config-space FRAMING the next path "
            "must supply. Builds on the retained graph-braid theorem; assumes no CAR / "
            "sign(beta) / Q=2/3; imports nothing."
        )
        print("=" * 74)
        return 0
    print("VERDICT: failures encountered; see above.")
    print("=" * 74)
    return 1


def _subdivide(G, k):
    G = nx.convert_node_labels_to_integers(G)
    H = nx.Graph()
    nid = max(G.nodes()) + 1
    for u, v in G.edges():
        prev = u
        for _ in range(k):
            H.add_edge(prev, nid)
            prev = nid
            nid += 1
        H.add_edge(prev, v)
    for n in G.nodes():
        H.add_node(n)
    return nx.convert_node_labels_to_integers(H)


if __name__ == "__main__":
    sys.exit(main())
