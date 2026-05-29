#!/usr/bin/env python3
"""
graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py
------------------------------------------------------

Runner paired with
    GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md

Source-only proposal. Status authority: independent audit lane only.

FIRST-QUANTIZED configuration-space statistics on the framework's Z^3 site
graph. This runner verifies the two exact mathematical facts behind the
{boson, fermion} dichotomy (anyons excluded) at the first-quantized level:

  (A) GRAPH-BRAID H_1 / TORSION CLASSIFICATION.
      For a finite graph Gamma, build the Abrams DISCRETIZED unordered
      2-particle configuration space UD_2(Gamma) as a cube complex (0-cells =
      disjoint unordered vertex pairs; 1-cells = (vertex, non-incident edge);
      2-cells = vertex-disjoint unordered edge pairs) and compute the integral
      first homology H_1(UD_2(Gamma)) = abelianization of the graph-braid
      group B_2(Gamma) = pi_1(UD_2(Gamma)) via the Smith normal form of the
      cubical boundary maps. Result:
          C_3 (triangle, planar)  ->  H_1 = Z            (torsion-free)
          C_4, C_5 (planar)       ->  H_1 = Z            (torsion-free)
          K_4                     ->  H_1 = Z^4          (torsion-free)
          K_5 (non-planar)        ->  H_1 = Z^6 (+) Z_2  (Z_2 torsion)
          K_{3,3} (non-planar)    ->  H_1 = Z^4 (+) Z_2  (Z_2 torsion)
      Abelian exchange statistics = Hom(H_1, U(1)). A *free* Z summand maps
      onto all of U(1) (a continuous phase: an anyon phase is ALLOWED when the
      relevant class is free, as for the planar cycles). A Z_2 TORSION summand
      maps only to {+1, -1}: a homomorphism sending the order-2 exchange class
      t (2t = 0) to x in U(1) forces x^2 = 1, i.e. x = +-1. So when the
      two-particle exchange (Y-)class generates a Z_2 torsion summand, the
      exchange phase is forced to +-1 -- {boson, fermion} only, continuous
      anyons EXCLUDED. (Ko-Park 2012: planar <=> H_1 torsion-free;
      non-planar => Z_2 torsion. Harrison-Keating-Robbins-Sawicki 2014:
      non-planar 3-connected => statistics is Bose or Fermi only.)

  (B) Z^3 SITE GRAPH IS NON-PLANAR AND 3-CONNECTED.
      For cubes of side L in {3, 4} of the Z^3 lattice site graph, networkx
      verifies (Kuratowski) NON-PLANARITY -- exhibiting an explicit K_{3,3}
      subdivision as the planarity counterexample -- and node-connectivity = 3
      (3-connected). By the Ko-Park / HKRS theorems this places Z^3 in the
      non-planar 3-connected class: H_1(UD_2) carries Z_2 torsion and the
      exchange is +-1 only. (The 2x2x2 cube Q_3 is planar, which is exactly
      why the claim requires L >= 3; this is checked as a contrast.)

The H_1 computation is exact integral linear algebra (Smith normal form over
Z via sympy); the planarity / connectivity checks are exact graph algorithms
(networkx). No PDG value, scale, coupling, or fitted input enters.

SCOPE (honest):
  * This is FIRST-QUANTIZED configuration-space statistics for indistinguishable
    particles on the Z^3 graph. It establishes {boson, fermion} (anyons
    excluded) at THAT level. It does NOT select the sign (boson vs fermion is a
    free 1D-rep choice). It does NOT by itself govern the framework's actual
    SECOND-QUANTIZED gauge-coupled matter sector; that bridge is a separate,
    open question (the retained-no-go statistics-agnostic note).
  * Combined with the framework's RETAINED per-site dim-2 result (which excludes
    the free/infinite-tower boson), the surviving first-quantized options are
    {hard-core boson, fermion}.

PASS/FAIL counted per-check; exits 0 iff PASS_COUNT > 0 and FAIL_COUNT == 0.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 180

import sys
from itertools import combinations

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
    from sympy.matrices.normalforms import smith_normal_form
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
# (A) Abrams discretized unordered 2-particle configuration space UD_2(Gamma)
#     and integral H_1 via Smith normal form.
# ===========================================================================
#
# Cells of Gamma: 0-cells = vertices, 1-cells = edges. Orient each edge
# e = (a, b) with a < b; cubical boundary d e = b - a.
#
# A product cell sigma x tau lies in the discretized D_2(Gamma) iff the
# closures of sigma and tau are DISJOINT (Abrams' condition):
#   closure(vertex v) = {v};  closure(edge {a,b}) = {a,b}.
# UD_2(Gamma) = D_2(Gamma) / Z_2 (particle swap). Its cells:
#   dim 0 : unordered pair {u, v} of distinct vertices.
#   dim 1 : unordered {vertex w, edge e} with w NOT an endpoint of e.
#   dim 2 : unordered {edge e, edge f}, e != f, sharing no endpoint
#           (vertex-disjoint edges).
#
# Cubical boundary maps on the unordered complex:
#   1-cell (w, e=(a,b)):  the product point-times-edge w x e, with
#       d( w x e ) = w x b - w x a = {w, b} - {w, a}   (unordered 0-cells).
#   2-cell (e=(a,b), f=(c,d)):  the square e x f, with
#       d( e x f ) = (de) x f - e x (df)
#                  = (b - a) x f - e x (d - c)
#                  = {b, f} - {a, f} - {d, e} + {c, e},
#       where {x, edge} denotes the 1-cell (vertex x, edge). On a
#       vertex-disjoint edge pair every such 1-cell is valid.
#
# H_1 = ker(d1) / im(d2). The free rank beta_1 = dim ker(d1) - rank(d2)
# = (|C_1| - rank d1) - rank d2. The TORSION of H_1 equals the nontrivial
# (>1) invariant factors of d2: im(d2) sits inside the PURE subgroup ker(d1)
# of the free group C_1 (kernel of a map to a free abelian group is a pure /
# saturated subgroup), so torsion(ker d1 / im d2) = torsion(C_1 / im d2),
# which the Smith normal form of d2 reads off directly.


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
        a, b = e  # a < b under the sorted-edge convention
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


def h1_graph_braid(G):
    """Return (beta_1, torsion_list, (|C0|,|C1|,|C2|), d1d2_is_zero)."""
    V, E, c0, c1, c2 = cells_UD2(G)
    d1 = boundary1(c0, c1)
    d2 = boundary2(c1, c2)
    d1d2_zero = all(v == 0 for v in (d1 * d2)) if (c1 and c2) else True
    n1 = len(c1)
    rk1 = d1.rank() if (c0 and c1) else 0
    rk2 = d2.rank() if (c1 and c2) else 0
    beta1 = n1 - rk1 - rk2
    torsion = []
    if c1 and c2:
        snf = smith_normal_form(d2)
        diag = [snf[i, i] for i in range(min(snf.shape))]
        torsion = [int(x) for x in diag if x not in (0, 1, -1)]
    return beta1, sorted(abs(t) for t in torsion), (len(c0), n1, len(c2)), d1d2_zero


def fmt_h1(beta1, torsion):
    s = f"Z^{beta1}"
    if torsion:
        s += " (+) " + " (+) ".join(f"Z_{t}" for t in torsion)
    return s


def run_part_A():
    print("-" * 72)
    print("(A) Graph-braid B_2(Gamma) abelianization H_1(UD_2(Gamma)) "
          "via Smith normal form")
    print("    planar => torsion-free (continuous anyon phase ALLOWED);")
    print("    non-planar => Z_2 torsion (exchange forced to +-1).")
    print("-" * 72)

    # (planar reference cases) -- torsion-free, so the abelian exchange phase
    # has a free U(1) (anyon) direction; these are the contrast cases.
    cases_planar = [
        ("C_3 triangle", nx.cycle_graph(3), 1),
        ("C_4 cycle", nx.cycle_graph(4), 1),
        ("C_5 cycle", nx.cycle_graph(5), 1),
        ("K_4 (planar)", nx.complete_graph(4), 4),
    ]
    # (non-planar cases) -- Z_2 torsion, so the exchange phase is +-1 only.
    cases_nonplanar = [
        ("K_5", nx.complete_graph(5), 6),
        ("K_{3,3}", nx.complete_bipartite_graph(3, 3), 4),
    ]

    for name, G, beta_exp in cases_planar:
        b1, tor, sizes, ok = h1_graph_braid(G)
        planar = nx.check_planarity(G)[0]
        check(f"(A) {name}: d1.d2 = 0 (valid chain complex)", ok)
        check(
            f"(A) {name}: H_1 = {fmt_h1(b1, tor)}  (planar={planar}, torsion-free)",
            (tor == []) and (b1 == beta_exp) and planar,
            f"|C0,C1,C2|={sizes}",
        )
        # torsion-free => Hom(H_1, U(1)) has a free U(1) direction on each
        # Z generator: a continuous (anyon) phase is allowed at this level.
        check(
            f"(A) {name}: torsion-free => U(1) exchange phase allowed (anyon ok)",
            tor == [],
        )

    for name, G, beta_exp in cases_nonplanar:
        b1, tor, sizes, ok = h1_graph_braid(G)
        planar = nx.check_planarity(G)[0]
        check(f"(A) {name}: d1.d2 = 0 (valid chain complex)", ok)
        check(
            f"(A) {name}: H_1 = {fmt_h1(b1, tor)}  (non-planar, Z_2 torsion)",
            (tor == [2]) and (b1 == beta_exp) and (not planar),
            f"|C0,C1,C2|={sizes}",
        )
        # Z_2 torsion class t (2t = 0): any phi: H_1 -> U(1) has phi(t)^2 = 1,
        # so phi(t) in {+1, -1}. Exchange forced to +-1 => {boson, fermion}.
        forced = hom_torsion_to_U1_images(2)
        check(
            f"(A) {name}: Hom(Z_2, U(1)) = {{+1, -1}} only "
            f"(exchange forced to +-1 => boson/fermion)",
            forced == {1.0, -1.0},
            f"images={sorted(forced)}",
        )


def hom_torsion_to_U1_images(n, samples=2048):
    """All x in U(1) with x^n = 1 are the n-th roots of unity. For the abelian
    exchange phase the order-2 (Z_2) class admits exactly x in {+1, -1}.
    Verified by solving x^n = 1 on a dense U(1) sample and confirming the only
    REAL-axis solutions for n = 2 are +-1 (no continuous family)."""
    roots = {complex(np.round(np.exp(2j * np.pi * k / n), 12)) for k in range(n)}
    real_roots = {float(np.real(r)) for r in roots if abs(np.imag(r)) < 1e-9}
    # sanity: a dense sweep finds no OTHER unit-modulus solution of x^n = 1
    thetas = np.linspace(0, 2 * np.pi, samples, endpoint=False)
    z = np.exp(1j * thetas)
    extra = np.sum(np.abs(z ** n - 1.0) < 1e-6) - n  # subtract the n true roots
    assert extra <= 0, "spurious continuous family of n-th roots found"
    return real_roots


# ===========================================================================
# (B) Z^3 lattice site graph: non-planar (Kuratowski / K_{3,3}) and 3-connected
# ===========================================================================

def classify_kuratowski(ce):
    """Classify a Kuratowski counterexample subgraph as a K_5 or K_{3,3}
    subdivision via the degrees of its branch vertices."""
    branch = [v for v in ce.nodes() if ce.degree(v) >= 3]
    degs = sorted(ce.degree(v) for v in branch)
    if len(branch) == 5 and all(d == 4 for d in degs):
        return "K_5 subdivision"
    if len(branch) == 6 and all(d == 3 for d in degs):
        return "K_{3,3} subdivision"
    return f"branch_count={len(branch)} degs={degs}"


def run_part_B():
    print("-" * 72)
    print("(B) Z^3 site graph (cube of side L): NON-PLANAR (Kuratowski) "
          "and 3-CONNECTED")
    print("    => non-planar 3-connected class (Ko-Park / HKRS): Z_2 torsion, "
          "exchange +-1 only.")
    print("-" * 72)

    for L in (3, 4):
        G = nx.grid_graph(dim=[L, L, L])
        planar, ce = nx.check_planarity(G, counterexample=True)
        conn = nx.node_connectivity(G)
        kind = classify_kuratowski(ce) if ce is not None else "(none)"
        check(
            f"(B) Z^3 cube L={L}: NON-PLANAR (V={G.number_of_nodes()}, "
            f"E={G.number_of_edges()})",
            planar is False,
            f"planar={planar}",
        )
        check(
            f"(B) Z^3 cube L={L}: planarity counterexample is a {kind}",
            ce is not None and kind.startswith(("K_5", "K_{3,3}")),
            f"Kuratowski subgraph V={ce.number_of_nodes() if ce else 0} "
            f"E={ce.number_of_edges() if ce else 0}",
        )
        check(
            f"(B) Z^3 cube L={L}: 3-connected (node-connectivity = 3)",
            conn == 3,
            f"node_connectivity={conn}",
        )

    # Contrast: the 2x2x2 cube graph Q_3 IS planar -- this is exactly why the
    # claim requires L >= 3 (the framework's Z^3 is the infinite lattice / any
    # cube of side >= 3, never the degenerate 2x2x2 box).
    Q3 = nx.hypercube_graph(3)
    planarQ, _ = nx.check_planarity(Q3)
    check(
        "(B) contrast: 2x2x2 cube Q_3 IS planar (why L >= 3 is required)",
        planarQ is True,
        f"planar={planarQ}, node_connectivity={nx.node_connectivity(Q3)}",
    )


# ===========================================================================
# Scorecard
# ===========================================================================

def main() -> int:
    print("=" * 72)
    print("GRAPH-BRAID Z^3 ANYON-EXCLUSION DICHOTOMY (first-quantized)")
    print("Note: GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_"
          "NOTE_2026-05-29.md")
    print("Claim: Z^3 site graph is non-planar 3-connected => H_1(UD_2) has "
          "Z_2 torsion")
    print("       => first-quantized exchange phase is +-1 only "
          "{boson, fermion}; anyons EXCLUDED.")
    print("=" * 72)

    run_part_A()
    run_part_B()

    print("=" * 72)
    print(f"SCORECARD: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0 and PASS_COUNT > 0:
        print(
            "VERDICT: At the FIRST-QUANTIZED configuration-space level, the Z^3 "
            "site graph is non-planar and 3-connected, so its graph-braid "
            "group B_2 abelianizes with a Z_2 torsion summand carrying the "
            "two-particle exchange; abelian statistics Hom(H_1, U(1)) sends the "
            "exchange to +-1 ONLY -> {boson, fermion}, continuous ANYONS "
            "EXCLUDED. Combined with the retained per-site dim-2 result "
            "(free/infinite-tower boson excluded), the surviving first-"
            "quantized matter statistics is {hard-core boson, fermion}. This "
            "does NOT select boson vs fermion and does NOT settle the open "
            "second-quantized gauge-coupled bridge."
        )
        print("=" * 72)
        return 0
    print("VERDICT: failures encountered; see above.")
    print("=" * 72)
    return 1


if __name__ == "__main__":
    sys.exit(main())
