#!/usr/bin/env python3
"""Color link-index routing: the cross-site matter bilinear is a native link-law carrier.

Class-A finite-dimensional verification for the source note

    docs/COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md

CONTEXT.  The color residual map (COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05) names
"route that color index onto links" as a live residual, and PRUNES the candidate "primitive
one-qubit link algebra already supplies color" (a qubit link natively carries only u(2);
QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04: no faithful su(3) on a
single qubit link).  The QUANTUM axiom supplies one qubit per SITE and no edge degrees of
freedom, so a fundamental SU(3)-valued link variable has no native carrier.

THESIS (a bounded link-index-routing EXISTENCE construction -- conditional on the SAME
supplied color carrier as the sister notes; NOT a dynamics, NOT a selection):
  GIVEN the supplied per-cube color carrier C^3 (the taste-cube symmetric base; supplied per
  the residual map / graph_first_su3 -- the same conditionality as the carrier notes), the
  CROSS-SITE MATTER BILINEAR

      M(x,y)_ij = sum_alpha psi_alpha(x)_i psi_alpha(y)_j^*     (occupied matter modes alpha)

  natively carries the link transformation law M -> g_x M g_y^dag, and its polar
  unitarization U = M (M^dag M)^{-1/2} is an exactly-unitary link variable obeying the SAME
  law; the determinant reduction S = U det(U)^{-1/3} gives an SU(3)-valued link obeying the
  law up to the Z_3 center.  Composite Wilson loops built from these links are EXACTLY
  invariant under LOCAL color rotations.  No edge degree of freedom, no quantum-link
  ontology, and no new axiom is needed: the routing lives on objects the matter sector
  already supplies.

HONEST BOUNDARIES (named, load-bearing):
  - CONDITIONAL on the supplied C^3 color carrier (the MR_color residual) -- exactly as the
    sister carrier notes; this is NOT an axiom-level derivation of color.
  - RANK: unitarization needs rank-3 M.  This requires at least three independent occupied
    matter modes, but rank-deficient three-mode configurations remain outside the construction;
    a single-mode bilinear is rank 1 and CANNOT be unitarized (Part 4 control).
  - Z_3 CENTER: the SU(3) reduction is canonical only up to the Z_3 center (det branch).
  - NO DYNAMICS: this supplies a KINEMATIC carrier/routing, not a generator/rate -- the
    undelivered continuous-time gauge-link dynamics (the ST1/ST2 same-wall residual,
    capstone note) is UNTOUCHED.
  - NO SELECTION: it does NOT claim the framework's physical link IS this composite (that
    identification belongs to the open gauging-selection gate); it proves EXISTENCE of a
    native carrier, pruning only the "edge-DOF import is required for the routing" branch.
  - Does NOT discharge ADM-1 (frame-referencing cross-site operators still exist; the
    construction is frame-COVARIANT, compatible with either reading).

Standard math cited for METHOD only (not imports): polar decomposition; the composite/
auxiliary-field gauge construction (CP^{N-1} sigma models, hidden local symmetry) as the
literature analogue of bilinear-built links.

Run: python3 scripts/frontier_color_link_index_routing_matter_bilinear_unitarization_2026_06_08.py
"""

from __future__ import annotations

import numpy as np

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


rng = np.random.default_rng(20260608)
NC = 3
W3 = [1.0, np.exp(2j * np.pi / 3), np.exp(-2j * np.pi / 3)]   # Z_3 center


def haar_su(n=NC):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, R = np.linalg.qr(A)
    Q = Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))
    return Q / np.linalg.det(Q) ** (1.0 / n)


def modes(k=3):
    """k occupied matter modes' color amplitudes at one site: rows alpha, cols color i."""
    return rng.normal(size=(k, NC)) + 1j * rng.normal(size=(k, NC))


def bilinear(PSIx, PSIy):
    """M(x,y)_ij = sum_alpha psi_alpha(x)_i psi_alpha(y)_j^*  =  PSIx^T PSIy^*  (3x3)."""
    return PSIx.T @ PSIy.conj()


def polar_u(M):
    """U = M (M^dag M)^{-1/2} (exact eigendecomposition)."""
    w, V = np.linalg.eigh(M.conj().T @ M)
    return M @ V @ np.diag(w ** -0.5) @ V.conj().T


def su3_of(U):
    return U * np.linalg.det(U) ** (-1.0 / NC)


def center_dev(A, B):
    """min over Z_3 center of max|A - w B| (the canonical SU(3) comparison)."""
    return min(float(np.max(np.abs(A - w * B))) for w in W3)


# ===========================================================================
# Part 1.  The cross-site matter bilinear natively carries the LINK LAW.
#   Under per-site color rotations psi(x) -> g_x psi(x), psi(y) -> g_y psi(y):
#   M(x,y) -> g_x M(x,y) g_y^dag  -- exactly the connection transformation law.
# ===========================================================================
print("=" * 78)
print("Part 1  Bilinear law: M(x,y) -> g_x M g_y^dag (the link law, natively)")
print("=" * 78)

worst = 0.0
for _ in range(100):
    PSIx, PSIy = modes(), modes()
    gx, gy = haar_su(), haar_su()
    M = bilinear(PSIx, PSIy)
    M_rot = bilinear((gx @ PSIx.T).T, (gy @ PSIy.T).T)
    worst = max(worst, float(np.max(np.abs(M_rot - gx @ M @ gy.conj().T))))
check("M(x,y) transforms as a LINK: M -> g_x M g_y^dag (100 random configs)",
      worst < 1e-12, f"max dev {worst:.1e}")

# ===========================================================================
# Part 2.  Polar unitarization PRESERVES the law -> an exactly-unitary link.
#   U(g_x M g_y^dag) = g_x U(M) g_y^dag  because (M^dag M) -> g_y (M^dag M) g_y^dag.
# ===========================================================================
print("=" * 78)
print("Part 2  Polar unitarization: U = M(M^dag M)^{-1/2} is unitary and obeys the law")
print("=" * 78)

worst_u, worst_law = 0.0, 0.0
for _ in range(100):
    PSIx, PSIy = modes(), modes()
    gx, gy = haar_su(), haar_su()
    M = bilinear(PSIx, PSIy)
    U = polar_u(M)
    worst_u = max(worst_u, float(np.max(np.abs(U.conj().T @ U - np.eye(NC)))))
    U_rot = polar_u(gx @ M @ gy.conj().T)
    worst_law = max(worst_law, float(np.max(np.abs(U_rot - gx @ U @ gy.conj().T))))
check("U is exactly unitary (U^dag U = I)", worst_u < 1e-9, f"max dev {worst_u:.1e}")
check("U obeys the link law: U(g_x M g_y^dag) = g_x U(M) g_y^dag (100 configs)",
      worst_law < 1e-9, f"max dev {worst_law:.1e}")

# ===========================================================================
# Part 3.  SU(3) reduction: S = U det(U)^{-1/3} obeys the law up to the Z_3 center.
# ===========================================================================
print("=" * 78)
print("Part 3  SU(3) reduction: det(S)=1; the law holds up to the Z_3 center")
print("=" * 78)

worst_det, worst_c, worst_naive = 0.0, 0.0, 0.0
for _ in range(100):
    PSIx, PSIy = modes(), modes()
    gx, gy = haar_su(), haar_su()
    M = bilinear(PSIx, PSIy)
    S = su3_of(polar_u(M))
    worst_det = max(worst_det, abs(np.linalg.det(S) - 1.0))
    S_rot = su3_of(polar_u(gx @ M @ gy.conj().T))
    worst_c = max(worst_c, center_dev(S_rot, gx @ S @ gy.conj().T))
    worst_naive = max(worst_naive, float(np.max(np.abs(S_rot - gx @ S @ gy.conj().T))))
check("det(S) = 1 exactly (SU(3)-valued link)", worst_det < 1e-9, f"max |det-1| {worst_det:.1e}")
check("S obeys the link law up to the Z_3 center (the canonical det-branch ambiguity)",
      worst_c < 1e-9, f"max center-dev {worst_c:.1e}")
# Referee-hardening: the UN-min'd deviation is reported too, so the center-min cannot mask a
# law failure.  For SU(3) endpoint rotations det(M) is invariant, so the cube-root branch
# never moves and the naive law in fact holds exactly (the center caveat is conservative).
check("UN-min'd law deviation also ~0 for SU(3) endpoints (center-min masks nothing; "
      "det(M) is SU(3)-invariant so the branch never moves)",
      worst_naive < 1e-9, f"max naive dev {worst_naive:.1e}")

# ===========================================================================
# Part 4.  RANK BOUNDARY (control): a single-mode bilinear is rank 1 -> NOT unitarizable.
# ===========================================================================
print("=" * 78)
print("Part 4  Rank boundary: single occupied mode -> rank-1 M -> unitarization FAILS")
print("=" * 78)

PSIx1, PSIy1 = modes(k=1), modes(k=1)
M1 = bilinear(PSIx1, PSIy1)
rank1 = np.linalg.matrix_rank(M1)
check("single-mode bilinear has rank 1 (< 3): M^dag M singular -> no polar unitary",
      rank1 == 1, f"rank = {rank1}; construction needs >= 3 occupied matter modes")
ranks_ok = all(np.linalg.matrix_rank(bilinear(modes(), modes())) == NC for _ in range(50))
check("with >= 3 occupied modes the bilinear is generically full-rank (50/50 configs)",
      ranks_ok)

# ===========================================================================
# Part 5.  TEETH: a basis-dependent unitarization (QR/Gram-Schmidt) BREAKS the law.
#   Only the polar (basis-free) unitarization is covariant.
# ===========================================================================
print("=" * 78)
print("Part 5  Teeth: QR/Gram-Schmidt unitarization is NOT covariant (polar is special)")
print("=" * 78)


def qr_u(M):
    Q, R = np.linalg.qr(M)
    return Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))   # fix diag phases; still basis-dep


bad = 0.0
for _ in range(50):
    PSIx, PSIy = modes(), modes()
    gx, gy = haar_su(), haar_su()
    M = bilinear(PSIx, PSIy)
    Q1 = qr_u(gx @ M @ gy.conj().T)
    bad = max(bad, float(np.max(np.abs(Q1 - gx @ qr_u(M) @ gy.conj().T))))
check("CONTROL: QR-based unitarization VIOLATES the link law (basis-dependent)",
      bad > 0.1, f"max law-violation {bad:.2f} (polar's covariance is not generic)")

# ===========================================================================
# Part 6.  Composite Wilson loops are EXACTLY invariant under LOCAL rotations.
# ===========================================================================
print("=" * 78)
print("Part 6  Composite plaquette Tr(U_xy U_yz U_zw U_wx) is LOCALLY gauge-invariant")
print("=" * 78)

sites = ["x", "y", "z", "w"]
PSI = {s: modes() for s in sites}
g = {s: haar_su() for s in sites}
loop = [("x", "y"), ("y", "z"), ("z", "w"), ("w", "x")]
U_loop = {ab: polar_u(bilinear(PSI[ab[0]], PSI[ab[1]])) for ab in loop}
P = np.trace(U_loop[loop[0]] @ U_loop[loop[1]] @ U_loop[loop[2]] @ U_loop[loop[3]])
PSI_rot = {s: (g[s] @ PSI[s].T).T for s in sites}
U_rot = {ab: polar_u(bilinear(PSI_rot[ab[0]], PSI_rot[ab[1]])) for ab in loop}
P_rot = np.trace(U_rot[loop[0]] @ U_rot[loop[1]] @ U_rot[loop[2]] @ U_rot[loop[3]])
check("composite plaquette trace is invariant under INDEPENDENT local rotations g_x..g_w",
      abs(P - P_rot) < 1e-9, f"|dTr| = {abs(P-P_rot):.1e}")
# and an OPEN composite line is NOT invariant (sanity: gauge content is the loops)
L_open = U_loop[("x", "y")]
L_open_rot = U_rot[("x", "y")]
check("an OPEN composite link is NOT locally invariant (gauge content = closed loops)",
      float(np.max(np.abs(L_open - L_open_rot))) > 0.1)

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: GIVEN the supplied per-cube C^3 color carrier (the MR_color residual -- the")
print("  same conditionality as the sister carrier notes), the cross-site matter bilinear")
print("  natively carries the link law M -> g_x M g_y^dag; its polar unitarization is an")
print("  exactly-unitary link with the same law (SU(3) up to the Z_3 center), and composite")
print("  Wilson loops are exactly locally gauge-invariant.  This routes the color index onto")
print("  links (the residual map's named residual) with NO edge DOF / quantum-link import --")
print("  the qubit-link u(2) boundary is respected, the routing lives on matter bilinears.")
print("  BOUNDARIES: full-rank bilinear required (single-mode FAILS, Part 4); Z_3")
print("  center ambiguity; KINEMATIC routing only -- supplies NO dynamics (the ST1/ST2")
print("  same-wall continuous-time gauge-link dynamics residual is UNTOUCHED), NO selection")
print("  (does not claim the physical link IS this composite -- the gauging-selection gate")
print("  stays open), does NOT discharge ADM-1.  No new axiom; no ranking of gates.")
if FAIL:
    raise SystemExit(1)
