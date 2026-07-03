#!/usr/bin/env python3
"""Induced holonomy: the composite link field's loops are a derived, gauge-covariant
functional of the matter state -- exactly central on the sea and its orbit, non-central
off it (filling-dependent magnitude) -- and the derived flow leaves the flat stratum
(t^4-tangentially) from non-stationary flat data.  Zero new inputs.

Class-A exact verification for the source note

    docs/INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md

CONTEXT (the holonomy demand addressed CONDITIONALLY at the kinematic/state-functional
level).  The local-frame orbit note shows that FRAME fields supply only the flat sector.
This note exhibits a candidate supplier the framework already contains: the COMPOSITE
LINK (U_eff = polar(M(x,y))).  Magnitudes are filling- and seed-dependent and labeled so;
creation is a t^4 TANGENTIAL departure (small at small t, O(0.1) only at t = O(1)); the
dynamics is SLAVED (no autonomous law); H2/H3a/H4 restate the landed block-01 trajectory
note at holonomy level (corollaries, cited); the
genuinely NEW content is (i) the conjugation+center-invariant curvature scalar
C = 1 - |tr Hol|/3, (ii) the two-pole dichotomy (sea/sea-orbit CENTRAL vs generic
NON-central, with the curvature INDUCED BY THE STATE rather than fed in), and (iii) the
creation-from-flat exhibit.

THE CURVATURE FUNCTIONAL: C = 1 - |tr Hol|/3 in [0,1]; exactly zero iff Hol is central
(flat mod center); invariant under conjugation AND the center.  The U(1)/det holonomy
that C deliberately quotients is itself a derived covariant state functional -- a NAMED
OPEN THREAD (candidate U(1) datum), not a silent quotient.

MANDATORY RECONCILIATIONS (objects distinguished; argued in the note):
  - COLOR_EINSELECTION_MATTER_UNITARY_PRIMITIVITY_..._2026-06-09 (unaudited sibling note):
    its object is the single-hop color TRANSPORTER of the flow (color-inert for the color-diagonal
    hopping: verified in-runner, scalar*I3); THIS note's object is the holonomy of
    polar(M(x,y)), the unitarized cross-site STATE bilinear -- a different functional of
    a different argument.  That note's own steelman EXPLICITLY leaves this route open
    ("multi-step matter dynamics might generate an effective primitive U without a fixed
    background link").
  - NATIVE_HOLONOMY_PLAQUETTE_CENTER_FLUX_NO_GO_2026-05-23 (retained_no_go): the native
    plaquette of the HOP operators is exactly scalar -- again a different object (the
    operator loop, not the state-bilinear loop).  No contradiction.
  - The campaign pack's block-12 probe ("inherited, not induced") was scoped to links
    fed into H plus sea-like states (on which this note agrees); pack-internal, no
    landed claim contradicted.

Run: python3 scripts/frontier_induced_holonomy_matter_state_functional_derived_curvature_2026_06_10.py
"""

from __future__ import annotations

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


rng = np.random.default_rng(20260610)
L = 3
EDGES = [(0, 1), (1, 2), (2, 0)]


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
    """C = 1 - |tr Hol|/3: zero iff central; conjugation- and center-invariant."""
    return 1.0 - abs(np.trace(hol(G))) / 3.0


def min_block_rank(G):
    return min(np.linalg.matrix_rank(M, tol=1e-10) for M in cross_blocks(G).values())


h9 = np.zeros((9, 9))
for x in range(L):
    for c in range(3):
        h9[3 * x + c, 3 * ((x + 1) % L) + c] = h9[3 * ((x + 1) % L) + c, 3 * x + c] = -1.0


def flow(G, t):
    U = expm(1j * h9.T * t)
    return U @ G @ U.conj().T


h_spat = np.zeros((L, L))
for x in range(L):
    h_spat[x, (x + 1) % L] = h_spat[(x + 1) % L, x] = -1.0
ev_s, evec_s = np.linalg.eigh(h_spat)


def sea(n_orb):
    G = np.zeros((9, 9), complex)
    for c in range(3):
        for k in range(n_orb):
            v = np.zeros(9, complex)
            for x in range(L):
                v[3 * x + c] = evec_s[x, k]
            G += np.outer(v, v.conj())
    return G


def local_rot(gs):
    Gam = np.zeros((9, 9), complex)
    for x in range(3):
        Gam[3 * x:3 * x + 3, 3 * x:3 * x + 3] = gs[x]
    return Gam


# ===========================================================================
# Part 1.  (H1) the two poles + filling-resolved genericity + near-sea robustness.
# ===========================================================================
print("=" * 78)
print("Part 1  (H1) poles: sea/sea-orbit -> C = 0 exactly; off-sea: C > 0, filling-dep.")
print("=" * 78)

G_sea = sea(1)
B = cross_blocks(G_sea)
check("the closed-shell sea induces scalar*I3 cross-blocks => links = I, C = 0 "
      "(the sea induces the FLAT sector; closed-shell/local-frame consistency)",
      all(np.allclose(M, M[0, 0] * np.eye(3), atol=1e-12) for M in B.values())
      and curv(G_sea) < 1e-12, f"C_sea = {curv(G_sea):.1e}")
gs = [haar(3) for _ in range(3)]
G_orbit = local_rot(gs) @ sea(2) @ local_rot(gs).conj().T
H_orbit = hol(G_orbit)
check("sea-ORBIT states induce CENTRAL holonomy (e^{i theta} I -- the color-link U(1)/center "
      "phase; that det phase is a NAMED OPEN THREAD, not a silent quotient) => C = 0",
      np.allclose(H_orbit, H_orbit[0, 0] * np.eye(3), atol=1e-9)
      and curv(G_orbit) < 1e-9, f"C_orbit = {curv(G_orbit):.1e}")
# filling-resolved genericity: magnitudes are FILLING-DEPENDENT.
stats = {}
for K in (3, 4, 5):
    cs = []
    for trial in range(20):
        PSI = np.linalg.qr(rng.normal(size=(9, K)) + 1j * rng.normal(size=(9, K)))[0]
        Gg = PSI @ PSI.conj().T
        if min_block_rank(Gg) == 3:
            cs.append(curv(Gg))
    stats[K] = (float(np.mean(cs)), float(np.min(cs)), len(cs))
check("off-sea states have C > 0 (strict; the load-bearing fact) with FILLING-DEPENDENT "
      "magnitude: near-half-filling K=4,5 give mean C = O(0.7); minimal K=3 gives "
      "mean C = O(0.2) (all values seed/filling-specific magnitudes, not constants)",
      all(stats[K][1] > 1e-6 for K in stats) and stats[4][0] > 0.3 and stats[3][0] < 0.5,
      f"mean C: K=3 {stats[3][0]:.2f}, K=4 {stats[4][0]:.2f}, K=5 {stats[5][0]:.2f}")
# near-sea robustness: low excitations stay (nearly) flat.
G_ph_same = sea(2).copy()
v2, v0 = np.zeros(9, complex), np.zeros(9, complex)
for x in range(L):
    v2[3 * x + 0] = evec_s[x, 2]
    v0[3 * x + 0] = evec_s[x, 0]
G_ph_same += np.outer(v2, v2.conj()) - np.outer(v0, v0.conj())   # same-color p-h
check("NEAR-SEA QUALIFIER: a same-color particle-hole excitation stays color-diagonal "
      "=> C = 0 EXACTLY ('generic' must not be read as 'typical near-sea')",
      curv(G_ph_same) < 1e-12, f"C = {curv(G_ph_same):.1e}")

# ===========================================================================
# Part 2.  (H2) covariance (corollary of the color-link/block-01 law) + C invariance.
# ===========================================================================
print("=" * 78)
print("Part 2  (H2) covariance [corollary of color-link/block-01]; C exactly invariant (new)")
print("=" * 78)

K = 5
PSI = np.linalg.qr(rng.normal(size=(9, K)) + 1j * rng.normal(size=(9, K)))[0]
G1 = PSI @ PSI.conj().T
gs2 = [haar(3) for _ in range(3)]
G1r = local_rot(gs2) @ G1 @ local_rot(gs2).conj().T
check("covariance Hol(g.G) = g_0 Hol(G) g_0^dag exactly [the block-01 covariant law "
      "U_eff -> g_x U_eff g_y^dag at loop level -- corollary, cited]",
      np.allclose(hol(G1r), gs2[0] @ hol(G1) @ gs2[0].conj().T, atol=1e-9))
check("C is EXACTLY invariant under local rotations (the NEW conjugation+center-"
      "invariant curvature scalar; max-entry distances are not conjugation-invariant "
      "and are not used)",
      abs(curv(G1r) - curv(G1)) < 1e-10, f"|dC| = {abs(curv(G1r) - curv(G1)):.1e}")

# ===========================================================================
# Part 3.  (H3) derived dynamics: motion [corollary]; CREATION from flat (new, t^4).
# ===========================================================================
print("=" * 78)
print("Part 3  (H3) flow: C(t) moves [corollary]; creation from flat = t^4 TANGENTIAL")
print("=" * 78)

c_traj = [curv(flow(G1, t)) for t in (0.0, 0.4, 0.8)]
ranks = [min_block_rank(flow(G1, t)) for t in np.linspace(0, 1.2, 9)]
check("from an off-sea state the derived flow moves C(t) [the block-01 induced "
      "trajectory at curvature level -- corollary, cited]; rank-3 verified along the "
      "sampled trajectory",
      max(abs(c_traj[i] - c_traj[0]) for i in (1, 2)) > 1e-3 and all(r == 3 for r in ranks),
      f"C(t) = {[round(c, 4) for c in c_traj]}")
# CREATION (new): norb=1 sea-orbit (robust instance), exact t^4 liftoff
gs3 = [haar(3) for _ in range(3)]
G_flat1 = local_rot(gs3) @ sea(1) @ local_rot(gs3).conj().T
c0 = curv(G_flat1)
t0 = 1e-3
p_order = float(np.log2(curv(flow(G_flat1, 2 * t0)) / curv(flow(G_flat1, t0))))
c_late = curv(flow(G_flat1, 1.2))
ranks2 = [min_block_rank(flow(G_flat1, t)) for t in np.linspace(0.05, 1.2, 8)]
check("CREATION: from FLAT non-stationary data (norb=1 sea-orbit, "
      "C(0) = 0 exactly) the flow leaves the flat stratum TANGENTIALLY -- quartic "
      "liftoff (Richardson order ~4), numerically small at small t, reaching O(0.1) "
      "only at t = O(1); an almost-periodic excursion, NOT relaxation",
      c0 < 1e-9 and 3.5 < p_order < 4.5 and c_late > 0.05 and all(r == 3 for r in ranks2),
      f"C(0) = {c0:.1e}; liftoff order p = {p_order:.2f}; C(1.2) = {c_late:.4f} "
      f"(seed-specific magnitude)")
c_sea_t = [curv(flow(G_sea, t)) for t in (0.5, 1.0)]
check("consistency: the STATIONARY sea stays exactly flat (creation requires "
      "non-stationary flat data; the vacuum does NOT spontaneously curve)",
      max(c_sea_t) < 1e-12, f"C_sea(t) = {[f'{c:.1e}' for c in c_sea_t]}")
# the transporter reconciliation (the sibling primitivity note's object, in-runner):
U_free = expm(-1j * h9 * 0.7)
blk = U_free[0:3, 3:6]
check("RECONCILIATION (sibling primitivity note): the free flow's single-hop color "
      "TRANSPORTER is color-inert (scalar*I3) -- a DIFFERENT object from the state-"
      "bilinear loop above; that note's steelman explicitly leaves the composed-link "
      "route open, and this note walks through exactly that door",
      np.allclose(blk, blk[0, 0] * np.eye(3), atol=1e-12))

# ===========================================================================
# Part 4.  (H4) slaving [corollary of block-01], with PHYSICAL states.
# ===========================================================================
print("=" * 78)
print("Part 4  (H4) slaving with VALID one-body densities [corollary of block-01]")
print("=" * 78)

GA = 0.9 * G1 + 0.05 * np.eye(9)                  # interior mixed density; same links
D = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
D = (D + D.conj().T) / 2
D -= np.trace(D) / 3 * np.eye(3)                  # traceless: particle number preserved
Demb = np.zeros((9, 9), complex)
Demb[0:3, 0:3] = D / np.max(np.abs(np.linalg.eigvalsh(D)))
GB = GA + 0.04 * Demb
eA, eB = np.linalg.eigvalsh(GA), np.linalg.eigvalsh(GB)
check("BOTH states are VALID one-body densities (0 <= eig <= 1 asserted in-runner; "
      "equal particle number)",
      eA.min() > -1e-12 and eA.max() < 1 + 1e-12 and eB.min() > -1e-12
      and eB.max() < 1 + 1e-12 and abs(np.trace(GA) - np.trace(GB)) < 1e-12,
      f"eig ranges [{eA.min():.3f},{eA.max():.3f}] / [{eB.min():.3f},{eB.max():.3f}]")
same_links = all(np.allclose(link_field(GA)[e], link_field(GB)[e], atol=1e-10)
                 for e in EDGES)
dt = 1e-5
dHA = (hol(flow(GA, dt)) - hol(GA)) / dt
dHB = (hol(flow(GB, dt)) - hol(GB)) / dt
check("same induced link field (polar is scale-invariant; diagonal-block change only) "
      "but DIFFERENT dHol/dt: the holonomy trajectory is SLAVED to the matter flow "
      "[block-01's non-autonomy at holonomy level -- corollary, cited]; no autonomous "
      "holonomy law is claimed",
      same_links and not np.allclose(dHA, dHB, atol=1e-3),
      f"||dH_A - dH_B|| = {float(np.max(np.abs(dHA - dHB))):.3f}")

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: the matter sector supplies gauge-covariant link")
print("  coordinates whose loops are generically non-central -- the holonomy demand")
print("  (local-frame orbit note: frames supply only flat) is ADDRESSED CONDITIONALLY at the kinematic/")
print("  state-functional level, with the dynamics SLAVED and the physical")
print("  identification gate OPEN.  NEW content: (i) the curvature scalar C = 1-|tr Hol|/3")
print("  (conjugation+center-invariant); (ii) the two-pole dichotomy -- sea/sea-orbit")
print("  CENTRAL (C=0 exactly) vs off-sea NON-central with FILLING-DEPENDENT magnitude")
print("  (near-sea excitations stay ~flat; decimals are seed/filling-specific); (iii)")
print("  creation-from-flat: a t^4-tangential, almost-periodic excursion off the flat")
print("  stratum from non-stationary flat data (the stationary sea stays exactly flat).")
print("  H2/H3a/H4 are corollaries of the landed block-01 trajectory note (cited).")
print("  C(t) from the fixed finite H is almost-periodic (no relaxation, no stationary")
print("  measure): HK-vs-Wilson discrimination on the induced trajectory is NOT yet")
print("  well-posed -- it still gates on the undelivered R1 (autonomous generator) and")
print("  R2 (mixing) residuals of the same-wall note.  WHICH holonomy is realized =")
print("  WHICH state is realized (the open-shell locus clause, state-side).  The U(1)/det holonomy")
print("  is a NAMED open thread.  Reconciled with the sibling primitivity note (object")
print("  distinction verified in-runner; its steelman leaves this route open) and the")
print("  native-plaquette retained_no_go (different object).  No new axiom/primitive/")
print("  measure/weight; r untouched; QUANTUM no-edge-DOF respected (derived data).")
print("  Audit lane grades.")
if FAIL:
    raise SystemExit(1)
