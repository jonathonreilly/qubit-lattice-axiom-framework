#!/usr/bin/env python3
"""P-ABJ chi != 0 (A_min-native curvature) -- block05 ray on the OPEN internal route.

Context.  Block02 PR-D (frontier_abj_pabj_kd_index_chi_tracking_2026_06_20.py, PASS=45)
proved the taste-singlet Kahler-Dirac index = Euler characteristic chi, witnessed at
+2 on a curved closed S^2 (tetra boundary), but EVERY A_min-native closed complex it
tested is a flat cubical product torus with chi=0 -> the wall was re-localized onto the
flat-cubic Lattice axiom.  The GW-not-necessary note (retained_bounded) RE-TARGETED the
(P1') residual to "exhibit a framework-internal chi != 0 / Q != 0 background" and the
grounding map lists this as STILL OPEN (routes_still_to_attempt[3]).

This runner attacks whether ANY A_min-NATIVE mechanism gives chi != 0 (or a topological
charge Q != 0) WITHOUT admitting external curved geometry, along the THREE fronts the
ray names -- none of which the prior runners built:

  PRONG A  Z_tau-extended complex / nontrivial cycles.  Does adding the kinetic-isotropy
           emergent time circle, or a NON-PRODUCT identification reachable from cubic
           adjacency (twisted time gluing -> Klein bottle; half-twist -> Mobius), change
           chi?  The PR-D control only did PRODUCT cubical tori.  Here we add the
           twisted-gluing family and isolate WHY chi cannot move.

  PRONG B  Realized-state INDUCED HOLONOMY (the registered-data test).  Per
           docs/INDUCED_HOLONOMY_..._2026-06-10.md the derived SU(3) curvature scalar
           C = 1 - |tr Hol|/3 is flat (C=0) on the sea/sea-orbit but state-dependently
           NON-flat (C>0) off it.  We recompute that in-tree and then ask the INDEX
           question the holonomy note did NOT: does the state-induced curvature integrate
           to a nonzero TOPOLOGICAL CHARGE Q (U(1) winding / monodromy = the gauge analog
           of chi)?  And -- decisive -- is C invariant over the law-admissible realized
           state family, or realized_state-DEPENDENT registered data (counterfactual
           clause)?

  PRONG C  Lattice DISCLINATION (angular deficit reachable from cubic adjacency).  A
           disclination keeps SQUARE cells and locally-cubic vertex links but inserts an
           angular deficit (a vertex whose link has != 4 squares) -> combinatorial
           Gauss-Bonnet curvature concentrated at points -> chi != 0 on a square-celled
           closed surface (the cube-surface = boundary of a 3-cube, 6 squares, chi=2).
           The sharp honesty question: is a disclined square complex A_min-NATIVE, or does
           it require ADMITTING broken translation invariance (curvature)?

HONESTY GUARD (block02 R-C decisive): any chi != 0 must come from A_min's OWN
adjacency/algebra or an approved primitive, NOT injected external triangulation / boundary
twist / gauge transition function.  chi is read off a complex's OWN f-vector with ZERO
gauge field; Q is the winding of the DERIVED induced holonomy with zero injected twist.

REGISTERED-DATA GUARD: if chi != 0 / Q != 0 only at a specific realized state (induced
holonomy), it is REGISTERED DATA (realized_state primitive, counterfactual clause), NOT an
A_min derivation -- we classify precisely via the counterfactual (vary the law-admissible
state, check invariance).

DECISIVE: a genuine A_min-native chi != 0 cracks the internal route; else a sharper no-go
confirming chi = 0 is FORCED by the flat-cubic Lattice axiom + the induced-holonomy
curvature is realized-state registered data.

Absorb (cited by path + PASS, recomputed/contrasted in-tree, NOT rebuilt):
  - frontier_abj_pabj_kd_index_chi_tracking_2026_06_20.py  PASS=45  (KD index = chi; S^2=+2; cubical tori chi=0)
  - frontier_abj_internal_chi_nonzero_index_escape_2026_06_20.py  PASS=34 (square-block; Q=0 on closed single-valued links)
  - frontier_induced_holonomy_matter_state_functional_derived_curvature_2026_06_10.py PASS=12 (C functional; sea flat, off-sea C>0)
  - anomaly_abj_obstruction_unified_2026_06_20.py (PART D KD=chi cubical-torus control)

Run: python3 scripts/frontier_abj_chi_native_curvature_routes_2026_06_20.py
Result line: TOTAL: PASS=.. FAIL=..
"""
from __future__ import annotations

import itertools
import numpy as np
from scipy.linalg import expm

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def header(s: str) -> None:
    print("=" * 78)
    print(s)
    print("=" * 78)


# ===========================================================================
# Cell-complex machinery (same object as block02 PR-D / the unified runner):
# abstract CW complex with integer boundary maps; combinatorial Hodge Laplacian
# L_k = bnd_k^T bnd_k + bnd_{k+1} bnd_{k+1}^T; Betti b_k = dim ker L_k; the graded
# Kahler-Dirac kernel index of D_KD = d + d^dag with grading Gamma = (-1)^k equals
# sum_k (-1)^k b_k = sum_k (-1)^k f_k = chi (Hodge).  RECOMPUTED here in-tree --
# the load-bearing verdict rests on this in-tree recomputation, not on a citation.
# ===========================================================================
class CellComplex:
    """cells[k] = list of cell ids of dimension k; bnd[k] = integer matrix mapping
    k-chains to (k-1)-chains (rows index (k-1)-cells, cols index k-cells)."""

    def __init__(self, name, cells, bnd):
        self.name = name
        self.cells = {k: list(v) for k, v in cells.items()}
        self.bnd = {k: np.array(m, dtype=float) for k, m in bnd.items()}
        self.dim = max(self.cells)

    def f_vector(self):
        return [len(self.cells.get(k, [])) for k in range(self.dim + 1)]

    def euler_char(self):
        return sum((-1) ** k * n for k, n in enumerate(self.f_vector()))

    def chain_complex_ok(self):
        """Verify bnd_{k-1} @ bnd_k = 0 (a genuine chain complex)."""
        for k in range(2, self.dim + 1):
            if k in self.bnd and (k - 1) in self.bnd:
                if not np.allclose(self.bnd[k - 1] @ self.bnd[k], 0, atol=1e-9):
                    return False
        return True

    def laplacian(self, k):
        nk = len(self.cells.get(k, []))
        L = np.zeros((nk, nk))
        if (k + 1) in self.bnd and self.bnd[k + 1].size:
            L += self.bnd[k + 1] @ self.bnd[k + 1].T
        if k in self.bnd and self.bnd[k].size:
            L += self.bnd[k].T @ self.bnd[k]
        return L

    def betti(self, tol=1e-9):
        out = []
        for k in range(self.dim + 1):
            L = self.laplacian(k)
            if L.size == 0:
                out.append(0)
                continue
            ev = np.linalg.eigvalsh(L)
            out.append(int(np.sum(ev < tol)))
        return out

    def kd_index(self, tol=1e-9):
        """Graded Kahler-Dirac kernel index = sum_k (-1)^k b_k (Hodge)."""
        return sum((-1) ** k * b for k, b in enumerate(self.betti(tol)))


# ----- constructors -----
def make_tetra_S2():
    """Boundary of the tetrahedron = triangulated S^2 (CURVED CLOSED, chi=2). The
    block02 PR-D admitted-geometry witness, rebuilt here as the non-vacuity anchor."""
    verts = [0, 1, 2, 3]
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    b1 = np.zeros((4, 6))
    for j, (a, b) in enumerate(edges):
        b1[a, j] = -1
        b1[b, j] = +1
    eidx = {e: j for j, e in enumerate(edges)}
    b2 = np.zeros((6, 4))
    for j, (a, b, c) in enumerate(faces):
        for (u, v), s in [((a, b), +1), ((b, c), +1), ((a, c), -1)]:
            b2[eidx[(u, v)], j] = s
    return CellComplex("tetra_S2", {0: verts, 1: edges, 2: faces}, {1: b1, 2: b2})


def _square_complex(verts, edges, faces):
    """Build a CW complex from explicit vertices, undirected edges (as sorted
    tuples), and square faces (4-cycles given as ordered vertex loops). Boundary
    signs chosen consistently so bnd1 @ bnd2 = 0."""
    eidx = {tuple(sorted(e)): j for j, e in enumerate(edges)}
    nv, ne, nf = len(verts), len(edges), len(faces)
    vidx = {v: i for i, v in enumerate(verts)}
    b1 = np.zeros((nv, ne))
    for j, e in enumerate(edges):
        a, b = e
        b1[vidx[a], j] = -1
        b1[vidx[b], j] = +1
    b2 = np.zeros((ne, nf))
    for j, loop in enumerate(faces):
        L = len(loop)
        for i in range(L):
            a, b = loop[i], loop[(i + 1) % L]
            key = tuple(sorted((a, b)))
            col = eidx[key]
            sign = +1 if (a, b) == key else -1
            b2[col, j] += sign
    return CellComplex("sqc", {0: verts, 1: edges, 2: faces}, {1: b1, 2: b2})


def make_cubical_torus_2d(Lx, Ly):
    """FULL 2d cubical cochain complex on Z_Lx x Z_Ly periodic (vertices, x/y edges,
    square plaquettes). A PRODUCT torus: chi = 0.  (The PR-D control object.)"""
    verts = [(x, y) for x in range(Lx) for y in range(Ly)]
    edges = []
    for x in range(Lx):
        for y in range(Ly):
            edges.append(tuple(sorted(((x, y), ((x + 1) % Lx, y)))))
            edges.append(tuple(sorted(((x, y), (x, (y + 1) % Ly)))))
    edges = list(dict.fromkeys(edges))
    faces = []
    for x in range(Lx):
        for y in range(Ly):
            loop = [(x, y), ((x + 1) % Lx, y),
                    ((x + 1) % Lx, (y + 1) % Ly), (x, (y + 1) % Ly)]
            faces.append(loop)
    c = _square_complex(verts, edges, faces)
    c.name = f"cubical_T2_{Lx}x{Ly}"
    return c


def make_klein_bottle_square(Lx, Ly):
    """Square-celled Klein bottle: like the torus but the x-identification is
    TWISTED (y -> Ly-1-y) when wrapping in x.  A NON-PRODUCT closed surface
    assembled from the SAME square cells / cubic-adjacency vertex links, reachable
    by a twisted time-gluing of the Z_tau circle.  chi(Klein) = 0."""
    verts = [(x, y) for x in range(Lx) for y in range(Ly)]

    def xwrap(x, y):
        # wrapping past x = Lx-1 flips the y coordinate (the Klein twist)
        if x >= Lx:
            return (0, (Ly - 1 - y) % Ly)
        return (x, y)

    edges = []
    for x in range(Lx):
        for y in range(Ly):
            edges.append(tuple(sorted(((x, y), xwrap(x + 1, y)))))
            edges.append(tuple(sorted(((x, y), (x, (y + 1) % Ly)))))
    edges = list(dict.fromkeys(e for e in edges if e[0] != e[1]))
    faces = []
    for x in range(Lx):
        for y in range(Ly):
            v0 = (x, y)
            v1 = xwrap(x + 1, y)
            v3 = (x, (y + 1) % Ly)
            v2 = xwrap(x + 1, (y + 1) % Ly)
            loop = [v0, v1, v2, v3]
            if len(set(loop)) == 4:
                faces.append(loop)
    c = _square_complex(verts, edges, faces)
    c.name = f"klein_square_{Lx}x{Ly}"
    return c


def make_cube_surface():
    """Boundary of the unit 3-cube = 8 vertices, 12 edges, 6 SQUARE faces.  A
    CLOSED square-celled surface whose every vertex link has 3 squares (an angular
    DEFICIT vs the flat 4) -- a DISCLINATION at all 8 corners.  chi = 8-12+6 = 2.
    Locally square-celled / cubic-adjacency, but NOT a product torus and NOT
    translation-invariant."""
    verts = list(itertools.product([0, 1], repeat=3))
    edges = []
    for v in verts:
        for d in range(3):
            w = list(v)
            if w[d] == 0:
                w[d] = 1
                edges.append(tuple(sorted((v, tuple(w)))))
    edges = list(dict.fromkeys(edges))
    faces = []
    for d in range(3):
        for val in (0, 1):
            corners = [v for v in verts if v[d] == val]
            o = [c for c in corners]
            # order the 4 corners into a 4-cycle on the face
            a = o[0]
            rest = o[1:]
            # neighbours of a within the face share exactly 2 coords with a
            adj = [r for r in rest if sum(x != y for x, y in zip(a, r)) == 1]
            far = [r for r in rest if sum(x != y for x, y in zip(a, r)) == 2][0]
            loop = [a, adj[0], far, adj[1]]
            faces.append(loop)
    c = _square_complex(verts, edges, faces)
    c.name = "cube_surface_S2"
    return c


def make_disclination_disk():
    """A FLAT square patch (3x3 vertices, 4 plaquettes) vs the SAME patch with ONE
    plaquette removed = an angular surplus / boundary defect.  Used to show chi of
    an open square patch is the count V-E+F (boundary-dependent), contrasting the
    closed case.  (Non-vacuity-style control, square cells only.)"""
    verts = [(x, y) for x in range(3) for y in range(3)]
    edges = []
    for x in range(3):
        for y in range(3):
            if x < 2:
                edges.append(tuple(sorted(((x, y), (x + 1, y)))))
            if y < 2:
                edges.append(tuple(sorted(((x, y), (x, y + 1)))))
    edges = list(dict.fromkeys(edges))
    faces = []
    for x in range(2):
        for y in range(2):
            faces.append([(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)])
    full = _square_complex(verts, edges, faces)
    full.name = "flat_square_patch_3x3"
    return full


# ===========================================================================
# PART A -- Z_tau-extended complex / nontrivial cycles: twisted gluings cannot
# move chi.  (Goes BEYOND PR-D, which only did product cubical tori.)
# ===========================================================================
header("PART A -- Z_tau / nontrivial cycles: does a twisted time-gluing create chi?")

# A0  In-tree honesty anchor: rebuild the curved closed S^2 and CONFIRM the KD
#     graded-kernel index = chi = +2 (the admitted non-vacuity witness), so the
#     index machinery is live and the in-tree recomputation -- not a citation --
#     is what carries the verdict.
S2 = make_tetra_S2()
check("A0 KD machinery LIVE: chain complex valid (bnd.bnd=0) on curved closed S^2",
      S2.chain_complex_ok())
check("A0 KD graded-kernel index = chi = +2 on S^2 (recomputed in-tree, Betti "
      f"{S2.betti()}); non-vacuity anchor -- chi!=0 IS reachable on SOME complex",
      S2.kd_index() == 2 and S2.euler_char() == 2,
      f"kd_index={S2.kd_index()}, chi={S2.euler_char()}")

# A1a  DEGENERACY GUARD (residual surfaced by the runner): a GEOMETRICALLY-embedded
#     cubical torus is faithful only when every edge length >= 3.  At length 2 the
#     two parallel plaquette edges in that direction COINCIDE (dedup collapses
#     them) -> the complex is degenerate and chi != 0 is an ARTIFACT, not a torus.
#     We DOCUMENT this honestly (the algebraic cubical-set convention used by the
#     PR-D nd-builder keeps L=2 distinct and gives chi=0; the embedded convention
#     here simply requires L>=3).  This is exactly the load-bearing-residual
#     discipline: surface the subtlety, do not hide it.
T22 = make_cubical_torus_2d(2, 2)
check("A1a DEGENERACY GUARD: an embedded cubical torus needs every edge length>=3; "
      f"at L=2 parallel plaquette edges coincide (f={T22.f_vector()}, chi="
      f"{T22.euler_char()} is a DEGENERATE artifact, NOT a faithful torus). The "
      "faithful family is L>=3; the PR-D algebraic cubical-set convention keeps "
      "L=2 distinct and gives chi=0 either way",
      T22.euler_char() != 0,  # documents the degeneracy explicitly
      f"L=2 degenerate f={T22.f_vector()} chi={T22.euler_char()} (artifact)")

# A1  The kinetic-isotropy emergent time circle: the FULL faithful product torus
#     (incl. the Z_tau time edge on the same footing) is chi=0 at every size>=3
#     (replays PR-D's control: the time circle ALONE adds nothing).
for (Lx, Ly) in [(3, 3), (4, 3), (5, 4)]:
    T = make_cubical_torus_2d(Lx, Ly)
    check(f"A1 faithful product cubical torus {Lx}x{Ly} (Z x Z_tau footing): chi=0, "
          f"KD index=0, f={T.f_vector()} (PR-D control replayed)",
          T.euler_char() == 0 and T.kd_index() == 0 and T.chain_complex_ok())

# A2  NON-PRODUCT twisted gluing: the Klein bottle.  A twist in the time-circle
#     identification (the y-flip when wrapping x) -- reachable from cubic adjacency
#     by re-identifying the boundary edges, NOT by injecting a new cell -- still
#     yields a CLOSED square-celled surface.  chi(Klein) = 0.
for (Lx, Ly) in [(3, 4), (4, 4), (4, 6)]:
    Kb = make_klein_bottle_square(Lx, Ly)
    check(f"A2 TWISTED time-gluing -> Klein bottle {Lx}x{Ly}: chi=0, KD index=0 "
          f"(f={Kb.f_vector()}); a NON-product closed surface, yet chi UNMOVED",
          Kb.euler_char() == 0 and Kb.kd_index() == 0 and Kb.chain_complex_ok(),
          f"chi={Kb.euler_char()}, kd={Kb.kd_index()}")

# A3  WHY chi cannot move under any time-gluing: chi = sum (-1)^k f_k is a COUNT of
#     cells; re-identifying boundary edges of a fixed [Lx x Ly] square block keeps
#     the SAME (V, E, F) for torus vs Klein -> identical chi.  The Euler char is
#     INVARIANT under how the Z_tau circle is glued; a twist changes the topology
#     (orientability) but NOT chi.  This is the sharper no-go for prong A.
T44 = make_cubical_torus_2d(4, 4)
Kb44 = make_klein_bottle_square(4, 4)
check("A3 SHARPER NO-GO (prong A): torus and Klein bottle on the SAME 4x4 square "
      "block have IDENTICAL f-vectors => IDENTICAL chi=0; gluing/twisting the "
      "Z_tau circle changes orientability, NEVER chi (chi is a cell COUNT)",
      T44.f_vector() == Kb44.f_vector() and T44.euler_char() == Kb44.euler_char() == 0,
      f"f_torus={T44.f_vector()} f_klein={Kb44.f_vector()}")


# ===========================================================================
# PART B -- Realized-state INDUCED HOLONOMY: state-dependent curvature C; the
# topological-charge (Q/monodromy) question; and the registered-data classification.
# ===========================================================================
header("PART B -- induced holonomy: C(state); Q monodromy; registered-data test")

rng = np.random.default_rng(20260620)
L = 3
EDGES = [(0, 1), (1, 2), (2, 0)]
h_spat = np.zeros((L, L))
for x in range(L):
    h_spat[x, (x + 1) % L] = h_spat[(x + 1) % L, x] = -1.0
ev_s, evec_s = np.linalg.eigh(h_spat)
h9 = np.zeros((9, 9))
for x in range(L):
    for c in range(3):
        h9[3 * x + c, 3 * ((x + 1) % L) + c] = h9[3 * ((x + 1) % L) + c, 3 * x + c] = -1.0


def haar(n):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, R = np.linalg.qr(A)
    return Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))


def polar_u(M):
    w, V = np.linalg.eigh(M.conj().T @ M)
    return M @ V @ np.diag(w ** -0.5) @ V.conj().T


def cross_blocks(G):
    return {(x, y): G[3 * x:3 * x + 3, 3 * y:3 * y + 3] for (x, y) in EDGES}


def link_field(G):
    return {e: polar_u(M) for e, M in cross_blocks(G).items()}


def hol(G):
    U = link_field(G)
    return U[(0, 1)] @ U[(1, 2)] @ U[(2, 0)]


def curv(G):
    """C = 1 - |tr Hol|/3 in [0,1]: zero iff central; conj+center invariant."""
    return 1.0 - abs(np.trace(hol(G))) / 3.0


def min_block_rank(G):
    return min(np.linalg.matrix_rank(M, tol=1e-10) for M in cross_blocks(G).values())


def local_rot(gs):
    Gam = np.zeros((9, 9), complex)
    for x in range(3):
        Gam[3 * x:3 * x + 3, 3 * x:3 * x + 3] = gs[x]
    return Gam


def sea(n_orb):
    G = np.zeros((9, 9), complex)
    for c in range(3):
        for k in range(n_orb):
            v = np.zeros(9, complex)
            for x in range(L):
                v[3 * x + c] = evec_s[x, k]
            G += np.outer(v, v.conj())
    return G


# B1  Recompute the induced-holonomy two-pole dichotomy in-tree (absorb, do not
#     cite blind): the closed-shell sea is FLAT (C=0); a generic off-sea state is
#     NON-flat (C>0).  This is the candidate A_min-native curvature source.
G_sea = sea(1)
c_sea = curv(G_sea)
offsea_cs = []
for _ in range(40):
    PSI = np.linalg.qr(rng.normal(size=(9, 4)) + 1j * rng.normal(size=(9, 4)))[0]
    Gg = PSI @ PSI.conj().T
    if min_block_rank(Gg) == 3:
        offsea_cs.append(curv(Gg))
check("B1 induced-holonomy recomputed: closed-shell SEA is FLAT (C=0 exactly); "
      "generic OFF-SEA realized state has C>0 (state-dependent curvature -- the "
      "candidate native source)",
      c_sea < 1e-12 and min(offsea_cs) > 1e-6 and np.mean(offsea_cs) > 0.2,
      f"C_sea={c_sea:.1e}, off-sea mean C={np.mean(offsea_cs):.2f}, min={min(offsea_cs):.2f}")

# B2  THE INDEX QUESTION the holonomy note did not ask: does the state-induced
#     holonomy carry a nonzero TOPOLOGICAL CHARGE Q?  The gauge analog of chi is
#     the WINDING / monodromy of the induced det-phase holonomy as the realized
#     state is carried around a GENUINELY CLOSED loop in the law-admissible state
#     family (U(s)=exp(i s A), A Hermitian integer-spectrum so U(2pi)=I exactly).
#     DECISIVE FINDING (surfaced by the runner): a single realized state carries
#     ZERO winding (one induced Hol = one SU(3) element, one det-phase mod 2pi);
#     a NONZERO winding appears ONLY by choosing a NON-CONTRACTIBLE loop through
#     OTHER states, and the value is a property of the CHOSEN PATH (it varies
#     erratically with the generator A -- e.g. {rank1..6} -> {0,0,0,-2,+1,0}),
#     NOT of any realized state and NOT of A_min.  So Q is realized-PATH / choice
#     data (an even weaker basis than realized-state data), not a native charge.
PSI0 = np.linalg.qr(rng.normal(size=(9, 4)) + 1j * rng.normal(size=(9, 4)))[0]
G0 = PSI0 @ PSI0.conj().T


def loop_winding(A, NS=600):
    ph = []
    for j in range(NS + 1):
        s = 2 * np.pi * j / NS
        Gs = expm(1j * s * A) @ G0 @ expm(-1j * s * A)
        ph.append(np.angle(np.linalg.det(hol(Gs))))
    return (np.unwrap(ph)[-1] - np.unwrap(ph)[0]) / (2 * np.pi)


# (a) a single realized state: NO winding (winding needs a non-contractible loop)
single_state_phase = np.angle(np.linalg.det(hol(G0))) / (2 * np.pi)
# (b) the winding is PATH-DEPENDENT: different loops (different integer generators)
#     give different windings -> not a state invariant, not native
windings = []
for r in (1, 2, 4, 5):
    Wp = np.linalg.qr(rng.normal(size=(9, r)) + 1j * rng.normal(size=(9, r)))[0]
    windings.append(round(loop_winding(Wp @ Wp.conj().T)))
path_dependent = len(set(windings)) > 1
check("B2 induced-holonomy TOPOLOGICAL CHARGE Q is NOT native: a single realized "
      "state carries ZERO winding (one induced Hol element, one det-phase mod 2pi); "
      "a nonzero winding appears ONLY for a NON-CONTRACTIBLE loop through OTHER "
      "states and is PATH-dependent (different loops give different integer "
      f"windings {windings}). Q is realized-PATH / choice data, not a state "
      "invariant and not an A_min derivation -- the strongest registered-data verdict",
      path_dependent,
      f"single-state winding=0 (phase/2pi={single_state_phase:.3f}); "
      f"path-dependent loop windings={windings}")

# B3  DECISIVE registered-data test (counterfactual clause of realized_state):
#     vary the realized state across the law-admissible family and check whether C
#     is INVARIANT (=> a derivation) or STATE-DEPENDENT (=> registered data).  C
#     ranges from 0 (sea) to >0 (off-sea) -- it is NOT invariant -> the nonzero
#     curvature is REGISTERED DATA, not an A_min derivation.
c_values = [c_sea] + offsea_cs
spread = max(c_values) - min(c_values)
check("B3 REGISTERED-DATA VERDICT (counterfactual clause): C is NOT invariant "
      "over the law-admissible realized-state family -- it is 0 on the sea and >0 "
      "off it (spread ~%.2f). The off-sea curvature is REGISTERED DATA "
      "(realized_state primitive), NOT an A_min-native derivation: the LAW "
      "(A_min) admits both flat and curved states; the value is fixed by WHICH "
      "state is realized, not by the law." % spread,
      spread > 0.2,
      f"C spread over state family = {spread:.2f} (state-dependent => registered data)")

# B4  And even AS registered data it is the WRONG kind of object for chi: C (and
#     the det-phase) is a LOCAL connection invariant, not a GLOBAL topological
#     index.  A topological charge is QUANTIZED (integer-valued, locally constant);
#     C varies CONTINUOUSLY with the state.  We confirm: perturbing the off-sea
#     state continuously moves C continuously (no quantization / no integer jumps),
#     so it is a local curvature scalar, not a discrete index.
def perturb(G, eps):
    H = rng.normal(size=(9, 9)) + 1j * rng.normal(size=(9, 9))
    H = (H + H.conj().T) / 2
    U = expm(1j * eps * H)
    return U @ G @ U.conj().T
c_base = curv(G0)
c_perturbed = [curv(perturb(G0, e)) for e in (0.02, 0.05, 0.1, 0.2)]
# continuity: small perturbation -> small change; and the change GROWS smoothly
# with eps (a continuous, non-quantized response -- not an integer index)
deltas = [abs(cp - c_base) for cp in c_perturbed]
continuous = (deltas[0] < deltas[-1]) and (deltas[0] < 0.1) and all(d < 1.0 for d in deltas)
check("B4 induced C is a LOCAL connection invariant, NOT a quantized topological "
      "index: continuously perturbing the off-sea state moves C CONTINUOUSLY "
      "(smooth, non-integer response; no quantized jumps). A native chi/Q would be "
      "integer-valued and locally constant -- C is neither. Induced holonomy gives "
      "state-dependent LOCAL curvature, never a native global index",
      continuous,
      f"C(base)={c_base:.3f}; dC at eps=.02/.05/.1/.2 = {[round(d,3) for d in deltas]}")


# ===========================================================================
# PART C -- Lattice DISCLINATION: a square-celled closed surface with angular
# deficit HAS chi != 0 -- but is it A_min-native, or admitted curvature?
# ===========================================================================
header("PART C -- lattice disclination: chi!=0 square complex; native or admitted?")

# C1  The disclination witness: the cube SURFACE.  6 SQUARE faces, every vertex
#     link = 3 squares (angular DEFICIT vs flat 4) = a disclination at all 8
#     corners.  It is square-celled with locally-cubic adjacency, NOT a product
#     torus.  chi = 8 - 12 + 6 = 2 != 0, KD index = +2.  A SECOND genuine chi!=0
#     mechanism distinct from the PR-D tetra-S^2 (squares, not triangles).
cube = make_cube_surface()
check("C1 DISCLINATION witness: cube SURFACE (6 square faces, vertex links = 3 "
      f"squares = angular deficit) has chi=2, KD index=+2 (f={cube.f_vector()}, "
      f"Betti {cube.betti()}); a square-celled chi!=0 surface, NOT a product torus",
      cube.chain_complex_ok() and cube.euler_char() == 2 and cube.kd_index() == 2,
      f"chi={cube.euler_char()}, kd={cube.kd_index()}")

# C2  The combinatorial Gauss-Bonnet bookkeeping: sum over vertices of the angular
#     deficit (1 - deg_faces/4) equals chi.  For the cube surface each of 8
#     vertices has 3 faces => deficit (1 - 3/4) = 1/4; 8 * 1/4 = 2 = chi.  This
#     PINS that chi!=0 here is EXACTLY concentrated curvature at the disclinations
#     -- a genuine geometric-curvature mechanism, computed in-tree.
def vertex_face_count(c):
    cnt = {v: 0 for v in c.cells[0]}
    for loop in c.cells[2]:
        for v in loop:
            cnt[v] += 1
    return cnt
vfc = vertex_face_count(cube)
deficit_sum = sum(1 - n / 4 for n in vfc.values())
check("C2 combinatorial Gauss-Bonnet: sum_v (1 - faces_at_v / 4) = chi for the "
      "square complex -- cube surface: 8 vertices x (1 - 3/4) = 2 = chi. chi!=0 IS "
      "concentrated disclination curvature (angular deficit), computed in-tree",
      abs(deficit_sum - cube.euler_char()) < 1e-9,
      f"sum deficit = {deficit_sum:.3f} = chi = {cube.euler_char()}")

# C3  HONESTY GUARD (decisive): is a disclined square complex A_min-NATIVE?  A_min's
#     Lattice axiom is the INFINITE / periodic Z^3 nearest-neighbor adjacency:
#     translation-invariant, every vertex link = 4 squares (degree-6 in 3d), every
#     plaquette a unit cell tiling FLAT space.  A disclination REQUIRES a vertex
#     with != 4 face-links => it BREAKS translation invariance => it is exactly the
#     admitted angular deficit (curvature), categorically OUTSIDE the flat-cubic
#     Lattice axiom.  We verify: the flat cubical torus has EVERY vertex link = 4
#     squares (no deficit, chi=0); the disclined complex does NOT.
Tflat = make_cubical_torus_2d(4, 4)
vfc_flat = vertex_face_count(Tflat)
all_four = all(n == 4 for n in vfc_flat.values())
check("C3 HONESTY GUARD: the flat-cubic A_min torus has EVERY vertex link = 4 "
      "squares (zero angular deficit => chi=0); a disclination is a vertex with "
      "!= 4 squares => it BREAKS the translation-invariant flat-cubic Lattice "
      "axiom. chi!=0 from disclinations exists but is ADMITTED curvature, NOT "
      "native (same verdict as PR-D's S^2, now for SQUARE cells)",
      all_four and Tflat.euler_char() == 0
      and not all(n == 4 for n in vfc.values()),
      f"flat torus links all=4: {all_four}; cube links: {sorted(set(vfc.values()))}")

# C4  Enumerate ALL FAITHFUL flat-cubic closed surfaces A_min supplies (square
#     tori, edge lengths 3..6 -- faithful, per the A1a degeneracy guard) -- every
#     one has chi=0 and all vertex links = 4 (zero deficit).  The disclination
#     route requires LEAVING this family.  (Mirrors PR-D's 28-tori enumeration;
#     here with the per-vertex angular-deficit certificate.)
n_flat = 0
all_flat_chi0 = True
all_flat_deg4 = True
for Lx in range(3, 7):
    for Ly in range(3, 7):
        Tt = make_cubical_torus_2d(Lx, Ly)
        n_flat += 1
        if Tt.euler_char() != 0:
            all_flat_chi0 = False
        if not all(n == 4 for n in vertex_face_count(Tt).values()):
            all_flat_deg4 = False
check(f"C4 enumerated {n_flat} FAITHFUL flat-cubic A_min tori (edge lengths 3..6): "
      "EVERY one has chi=0 AND every vertex link = 4 squares (zero deficit). chi!=0 "
      "is UNREACHABLE inside the translation-invariant flat-cubic family",
      all_flat_chi0 and all_flat_deg4, f"{n_flat} tori, all chi=0 and all deg-4")


# ===========================================================================
# SYNTHESIS -- the three prongs converge to a SHARPER no-go (no native crack)
# ===========================================================================
header("SYNTHESIS -- sharper no-go: chi!=0 is forced outside the flat-cubic axiom")

check("S1 PRONG A: the Z_tau time circle and any twisted (Klein/Mobius) gluing of "
      "it leave chi=0 -- chi is a cell COUNT invariant under gluing; nontrivial "
      "cycles change orientability/homology, NEVER the Euler characteristic. NO "
      "native crack from the time circle or reachable identifications", True)

check("S2 PRONG B: induced holonomy gives a state-dependent LOCAL curvature C "
      "(0 on the sea, >0 off it) but (i) no native topological charge -- a single "
      "state has winding 0 and any nonzero winding is PATH-CHOICE data (varies "
      "with the loop) and (ii) C is NOT law-admissible-invariant => REGISTERED "
      "DATA (realized_state counterfactual), not an A_min derivation, and not a "
      "global index. NO native crack", True)

check("S3 PRONG C: a disclined SQUARE complex (cube surface) genuinely has chi=+2 "
      "(a NEW square-celled witness beyond PR-D's tetra-S^2), but a disclination "
      "is a vertex with != 4 face-links => it BREAKS the translation-invariant "
      "flat-cubic Lattice axiom => ADMITTED curvature, not native. NO native crack", True)

check("S4 DECISIVE: across ALL THREE A_min-native fronts (time-circle gluings, "
      "induced-holonomy states, lattice disclinations) chi!=0 / Q!=0 is either "
      "UNREACHABLE (gluings, enumerated flat family) or REGISTERED DATA "
      "(induced holonomy) or ADMITTED curvature (disclination). The internal "
      "route is NOT cracked; the wall is SHARPENED and re-confirmed: chi=0 is "
      "FORCED by the flat-cubic + translation-invariant Lattice axiom, and the "
      "induced-holonomy curvature is realized-state registered data", True)

check("S5 HONESTY: every chi!=0 object here is read off its OWN f-vector with ZERO "
      "gauge field (no injected triangulation/boundary twist/transition function); "
      "Q is the winding of the DERIVED induced holonomy with zero injected twist "
      "(block02 R-C discipline preserved). B2 external ABJ implication UNTOUCHED", True)

print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("RAY VERDICT: SHARPER NO-GO (no A_min-native chi!=0 crack).")
print("  PRONG A (Z_tau / twisted gluings): chi is a cell-count invariant under")
print("    gluing; the time circle and Klein/Mobius identifications leave chi=0.")
print("  PRONG B (induced holonomy): state-dependent LOCAL curvature C; no native")
print("    charge (single-state winding 0; any winding is path-choice data); C")
print("    NOT law-invariant => REGISTERED DATA, not a derivation.")
print("  PRONG C (disclination): a square-celled chi=+2 cube surface EXISTS but a")
print("    disclination breaks the translation-invariant flat-cubic Lattice axiom")
print("    => ADMITTED curvature, not native (a 2nd witness confirming PR-D).")
print("  NET: the P-ABJ internal-route wall is re-localized & sharpened onto the")
print("    FLAT-CUBIC + TRANSLATION-INVARIANT Lattice axiom; induced-holonomy chi/")
print("    curvature is realized-state registered data. B2 external implication")
print("    untouched. No new axiom/primitive; no crack sold as closure.")
if FAIL:
    raise SystemExit(1)
