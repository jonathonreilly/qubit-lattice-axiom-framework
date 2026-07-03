#!/usr/bin/env python3
"""Unraveled record trajectories supply a CONDITIONAL non-degenerate Born-weighted
single-edge step distribution on the induced link, on the GENERIC FULL-RANK domain.
Four named residuals remain before any heat-kernel CLT use. Exact outcome-tree
enumeration; no Monte Carlo.

Class-A exact verification for the source note

    docs/UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md

CONTEXT. The interleaved mean-map source note proved mean-level convergence and
explicitly did not supply a step measure. This runner studies the separate
outcome-resolved question: under named weak instruments and a conditional Born-weighted
unraveling, what single-edge induced-link increments do the exact finite outcome trees
produce?

BORN PROVENANCE. Born outcome weights enter as a CONDITIONAL DEPENDENCY routed through
the framework's existing Born-rule chain (Gleason projection-lattice theorem, the
Busch/POVM qubit-authority bridge, and the Born assembly note). They are NOT supplied
by Record; the post-record count-probability firewall is respected. This runner
therefore supports only the bounded conditional theorem, not a Record-derived
probability rule.

THE RESULTS (exact):
  (U1) THE UNRAVELING, EXACTLY.  Two-outcome weak instruments (exact Kraus completeness)
       for both named classes -- I-B-type (color-blind, a function of the site-total
       N_x) and I-A-type (frame-naming, a function of one mode number) -- interleaved
       with the derived flow.  Exact Born weights sum to 1; the weighted average
       reproduces the deterministic channel exactly (unraveling consistency).
  (U2) THE DOMAIN, GUARDED.  dU = U_eff(n) U_eff(n-1)^dag exists only
       where the inter-site coherence block is FULL RANK.  Sub-minimal occupancy
       (K < 3) is an EXACT rank-deficient locus, and the sea's block is scalar
       (spread-degenerate). The polar is SVD-based and EVERY branch used is
       rank-guarded in-runner.  On the generic full-rank domain -- including a
       FULL-RANK NEAR-SEA state (exhibited) -- the Born-weighted step distribution has
       STRICTLY POSITIVE spread for BOTH instrument classes (instance-labeled
       variances; spread -> 0 as eps -> 0 as expected for a weak instrument, with
       var ~ eps^2 -- which rules out a numerical floor and claims nothing more).
  (U3) THE HONEST GAPS -- the CLT route needs FOUR named residuals:
       (1) STATIONARITY: increments are state-dependent (exact exhibit) -- trajectory
           equilibration is unproven;
       (2) CENTRALITY: on generic states E[dU] is non-scalar, and the off-scalar part
           is EPS-INDEPENDENT (verified) -- a STRUCTURAL property of this increment,
           not a small residual that can be assumed to disappear without argument
           (and instance-dependent: special states can have scalar E[dU]);
       (3) IDENTICAL DISTRIBUTION ACROSS EDGES: FAILS as-is (E[dU] differs O(1)
           between edges -- exhibited);
       (4) MANY-EDGE STRUCTURE: cross-edge independence / the multi-edge convolution
           are untested here (single-edge increments only).
  (U4) THE COVARIANCE SPLIT.  The I-B (color-blind)
       unraveling is EXACTLY covariant (conjugate-representation Fock lift, pinned
       in-runner); the I-A (frame-naming) unraveling breaks covariance at order 1 (its
       anchor = the {P_r} datum).  Finite eps is the weak-record regime; it is not in
       tension with the projective full-strength erasure limit of the named
       record-instrument note.

REPO-NEW CONTENT: U2 -- the existence of the non-degenerate Born-weighted step
distribution on the generic guarded domain -- plus the finite-eps trajectory-level
orientation spread.  U1 is textbook machinery instantiated; U3/U4 are boundary and
covariance checks needed to keep the CLT route honest.

Run: python3 scripts/frontier_unraveled_record_step_distribution_nondegenerate_2026_06_10.py
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
L, NM = 3, 9                          # mode index = site*3 + color
RANK_TOL = 1e-8


def ann(j, n):
    sz = np.array([[1, 0], [0, -1]], float)
    sm = np.array([[0, 1], [0, 0]], float)
    ops = [sz] * j + [sm] + [np.eye(2)] * (n - j - 1)
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out


A9 = [ann(j, NM) for j in range(NM)]
AD9 = [a.T for a in A9]
h9 = np.zeros((NM, NM))
for x in range(L):
    for c in range(3):
        h9[3 * x + c, 3 * ((x + 1) % L) + c] = h9[3 * ((x + 1) % L) + c, 3 * x + c] = -1.0
H = sum(h9[i, j] * (AD9[i] @ A9[j]).astype(complex) for i in range(NM) for j in range(NM))
U_step = expm(-1j * H * 0.35)


def polar_u(M):
    """SVD-based polar factor for the guarded full-rank domain."""
    U, s, Vh = np.linalg.svd(M)
    return U @ Vh


def min_sv(M):
    return float(np.linalg.svd(M, compute_uv=False)[-1])


def Gof(psi):
    return np.array([[psi.conj() @ (AD9[i] @ A9[j]).astype(complex) @ psi
                      for j in range(NM)] for i in range(NM)])


def kraus_pair(Nop, eps):
    w, V = np.linalg.eigh(Nop)
    Nt = (w - w.mean()) / max(abs(w - w.mean()))
    Kp = (V @ np.diag(np.sqrt((1 + eps * Nt) / 2)) @ V.T).astype(complex)
    Km = (V @ np.diag(np.sqrt((1 - eps * Nt) / 2)) @ V.T).astype(complex)
    return Kp, Km


N_site0 = sum(AD9[c] @ A9[c] for c in range(3))            # color-blind (I-B-type)
N_mode0 = AD9[0] @ A9[0]                                   # frame-naming (I-A-type)
EPS = 0.6
KB = kraus_pair(N_site0, EPS)
KA = kraus_pair(N_mode0, EPS)


def slater_fock(PSI):
    vac = np.zeros(2 ** NM)
    vac[int(np.argmin(np.diag(sum(AD9[m] @ A9[m] for m in range(NM)).real)))] = 1.0
    psi = vac.astype(complex)
    for k in range(PSI.shape[1]):
        psi = sum(PSI[m, k] * AD9[m].astype(complex) for m in range(NM)) @ psi
    return psi / np.linalg.norm(psi)


K = 5
PSI0 = np.linalg.qr(rng.normal(size=(NM, K)) + 1j * rng.normal(size=(NM, K)))[0]
psi0 = slater_fock(PSI0)


def tree(Kpair, depth, psi_init, edge=(0, 1)):
    """EXACT outcome-tree enumeration with per-branch RANK GUARDS.
    Returns (branches, worst cross-block min-sv over every branch used)."""
    x, y = edge
    branches = [(1.0, psi_init, [])]
    worst_sv = np.inf
    for n in range(depth):
        new = []
        for (w, psi, hist) in branches:
            psi_f = U_step @ psi
            for Kop in Kpair:
                phi = Kop @ psi_f
                p = float(np.real(phi.conj() @ phi))
                if p < 1e-12:
                    continue
                phi = phi / np.sqrt(p)
                M = Gof(phi)[3 * x:3 * x + 3, 3 * y:3 * y + 3]
                worst_sv = min(worst_sv, min_sv(M))
                new.append((w * p, phi, hist + [polar_u(M)]))
        branches = new
    return branches, worst_sv


def increments(branches):
    return [(w, h[-1] @ h[-2].conj().T) for (w, _, h) in branches]


def spread(incs):
    Z = sum(w for w, _ in incs)
    Em = sum(w * d for w, d in incs) / Z
    return float(sum(w * np.linalg.norm(d - Em) ** 2 for w, d in incs) / Z), Em


# ===========================================================================
# Part 1.  (U1) the unraveling, exactly.
# ===========================================================================
print("=" * 78)
print("Part 1  (U1) exact outcome tree: completeness; weights; mean-consistency")
print("=" * 78)

for tag, Kp in (("I-B", KB), ("I-A", KA)):
    comp = Kp[0].conj().T @ Kp[0] + Kp[1].conj().T @ Kp[1]
    check(f"{tag} Kraus completeness K+†K+ + K-†K- = I exactly",
          np.max(np.abs(comp - np.eye(2 ** NM))) < 1e-10)
br, sv_B = tree(KB, 5, psi0)
check("the depth-5 outcome tree's exact Born weights sum to 1",
      abs(sum(w for w, _, _ in br) - 1) < 1e-10,
      f"{len(br)} branches; |sum-1| = {abs(sum(w for w,_,_ in br)-1):.1e}")
rho0 = np.outer(psi0, psi0.conj())
rho_f = U_step @ rho0 @ U_step.conj().T
rho_chan = KB[0] @ rho_f @ KB[0].conj().T + KB[1] @ rho_f @ KB[1].conj().T
br1, _ = tree(KB, 1, psi0)
rho_avg = sum(w * np.outer(p, p.conj()) for (w, p, _) in br1)
check("UNRAVELING CONSISTENCY: Born-weighted average of conditional states = the "
      "deterministic channel EXACTLY", np.max(np.abs(rho_avg - rho_chan)) < 1e-12)

# ===========================================================================
# Part 2.  (U2) the domain guarded; non-degenerate spread on the generic domain.
# ===========================================================================
print("=" * 78)
print("Part 2  (U2) domain guards; non-degenerate spread on the generic full-rank domain")
print("=" * 78)

check("RANK GUARD: every branch of the generic-state tree has a FULL-RANK cross block "
      "(the increment is well-defined on every branch used)",
      sv_B > RANK_TOL, f"worst branch min-sv {sv_B:.4f}")
# THE STRUCTURAL LOCUS, exhibited two ways: (a) sub-minimal occupancy K=2 forces
# rank(M) <= 2 EXACTLY (rank G <= K, matching the color-link precondition);
# (b) the nf=1-per-color sea itself has a SCALAR cross block (full-rank but with
# trivial polar -- its dU is the identity's orbit, spread-degenerate).
PSI_K2 = np.linalg.qr(rng.normal(size=(NM, 2)) + 1j * rng.normal(size=(NM, 2)))[0]
psi_K2 = slater_fock(PSI_K2)
M_K2 = Gof(psi_K2)[0:3, 3:6]
check("THE STRUCTURAL LOCUS, exhibited: at sub-minimal occupancy K=2 the cross block "
      "is EXACTLY rank-deficient (rank <= K, algebraic; color-link precondition); dU "
      "does not exist there; the existence headline is restricted to the generic "
      "full-rank (K >= 3, full-rank-realized) domain",
      min_sv(M_K2) < 1e-12, f"K=2 cross-block min-sv {min_sv(M_K2):.1e}")
h_spat = np.zeros((L, L))
for x in range(L):
    h_spat[x, (x + 1) % L] = h_spat[(x + 1) % L, x] = -1.0
evs, evec = np.linalg.eigh(h_spat)
PSI_sea = np.zeros((NM, 3))
for c in range(3):
    for x in range(L):
        PSI_sea[3 * x + c, c] = evec[x, 0]
psi_sea = slater_fock(PSI_sea)
M_sea = Gof(psi_sea)[0:3, 3:6]
check("the nf=1-per-color sea: a SCALAR cross block (full rank, trivial polar = I) -- "
      "the sea sits at the spread-DEGENERATE point even where defined",
      np.allclose(M_sea, M_sea[0, 0] * np.eye(3), atol=1e-12),
      f"||M_sea - scalar*I|| = {np.max(np.abs(M_sea - M_sea[0,0]*np.eye(3))):.1e}")
var_B, Em_B = spread(increments(br))
br_A, sv_A = tree(KA, 5, psi0)
var_A, Em_A = spread(increments(br_A))
check("I-B (color-blind) step spread strictly positive on the generic domain "
      "(instance-labeled)", var_B > 1e-3 and sv_B > RANK_TOL, f"variance {var_B:.4f}")
check("I-A (frame-naming) step spread strictly positive on the generic domain "
      "(instance-labeled)", var_A > 1e-3 and sv_A > RANK_TOL, f"variance {var_A:.4f}")
PSI_near = np.linalg.qr(PSI_sea + 0.15 * (rng.normal(size=(NM, 3))
                                          + 1j * rng.normal(size=(NM, 3))))[0]
psi_near = slater_fock(PSI_near)
br_near, sv_near = tree(KB, 5, psi_near)
var_near, _ = spread(increments(br_near))
check("NEAR-SEA CONTROL: a full-rank near-sea state has strictly positive spread -- "
      "the phenomenon survives near the sea exactly where the increment is defined",
      sv_near > RANK_TOL and var_near > 1e-3,
      f"min-sv {sv_near:.4f}; variance {var_near:.4f}")
KB_small = kraus_pair(N_site0, 0.05)
br_s, _ = tree(KB_small, 5, psi0)
var_small, _ = spread(increments(br_s))
check("eps -> small: the spread vanishes as expected for a weak instrument "
      "(var ~ eps^2 -- this rules out a numerical floor and claims nothing more)",
      var_small < 0.05 * var_B, f"variance(eps=0.05) = {var_small:.6f}")

# ===========================================================================
# Part 3.  (U3) the four named residuals on the CLT route.
# ===========================================================================
print("=" * 78)
print("Part 3  (U3) the CLT route's FOUR residuals: stationarity, centrality, "
      "edge-identity, many-edge")
print("=" * 78)

br3, _ = tree(KB, 3, psi0)
d_first = br3[0][2][-1] @ br3[0][2][-2].conj().T
d_last = br3[-1][2][-1] @ br3[-1][2][-2].conj().T
check("RESIDUAL 1 (stationarity): increments are STATE-DEPENDENT (two tree nodes give "
      "different increments) -- trajectory equilibration unproven",
      np.max(np.abs(d_first - d_last)) > 0.05,
      f"difference {np.max(np.abs(d_first - d_last)):.3f}")
off_B = Em_B - (np.trace(Em_B) / 3) * np.eye(3)
KB_mid = kraus_pair(N_site0, 0.3)
br_mid, _ = tree(KB_mid, 5, psi0)
_, Em_mid = spread(increments(br_mid))
off_mid = Em_mid - (np.trace(Em_mid) / 3) * np.eye(3)
check("RESIDUAL 2 (centrality): on the generic state E[dU] is NON-SCALAR and the "
      "off-scalar part is EPS-INDEPENDENT (a STRUCTURAL property of this increment, "
      "not a small residual; instance-dependent -- special states can be scalar)",
      np.linalg.norm(off_B) > 1e-2
      and abs(np.linalg.norm(off_B) - np.linalg.norm(off_mid)) < 0.1 * np.linalg.norm(off_B),
      f"off-scalar {np.linalg.norm(off_B):.4f} (eps=0.6) vs {np.linalg.norm(off_mid):.4f} (eps=0.3)")
br_e2, sv_e2 = tree(KB, 5, psi0, edge=(1, 2))
_, Em_e2 = spread(increments(br_e2))
check("RESIDUAL 3 (identical distribution across edges): FAILS as-is -- E[dU] differs "
      "at order 1 between edges (0,1) and (1,2)",
      sv_e2 > RANK_TOL and np.max(np.abs(Em_B - Em_e2)) > 0.05,
      f"edge difference {np.max(np.abs(Em_B - Em_e2)):.3f}")
print("   RESIDUAL 4 (many-edge structure): cross-edge independence and the multi-edge")
print("   convolution are UNTESTED here (single-edge increments only) -- named, open.")

# ===========================================================================
# Part 4.  (U4) the covariance split.
# ===========================================================================
print("=" * 78)
print("Part 4  (U4) covariance split (trajectory-level re-exhibit; regime reconciliation)")
print("=" * 78)


def haar3():
    A = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Q, R = np.linalg.qr(A)
    Q = Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))
    return Q / np.linalg.det(Q) ** (1 / 3)


def logu(u):
    w, V = np.linalg.eig(u)
    return V @ np.diag(np.log(w)) @ np.linalg.inv(V)


g = haar3()
Kg = sum(np.conj(logu(g))[i, j] * sum((AD9[3 * x + i] @ A9[3 * x + j]).astype(complex)
                                      for x in range(3)) for i in range(3) for j in range(3))
Gam = expm(Kg)
GB9 = np.zeros((NM, NM), complex)
for x in range(3):
    GB9[3 * x:3 * x + 3, 3 * x:3 * x + 3] = g
check("the conjugate-representation lift, pinned: G(Gamma psi) = g G(psi) g† exactly",
      np.max(np.abs(Gof(Gam @ psi0) - GB9 @ Gof(psi0) @ GB9.conj().T)) < 1e-9)
br_rot, _ = tree(KB, 5, Gam @ psi0)
_, Em_rot = spread(increments(br_rot))
check("I-B COVARIANCE, exact: E[dU](g.psi) = g E[dU](psi) g† -- the color-blind "
      "unraveling's noise is gauge-covariant",
      np.max(np.abs(Em_rot - g @ Em_B @ g.conj().T)) < 1e-9,
      f"dev {np.max(np.abs(Em_rot - g @ Em_B @ g.conj().T)):.1e}")
br_rotA, _ = tree(KA, 5, Gam @ psi0)
_, Em_rotA = spread(increments(br_rotA))
check("I-A breaks covariance at order 1 (anchored to ITS frame -- the {P_r} datum; "
      "the frame-naming boundary)",
      np.max(np.abs(Em_rotA - g @ Em_A @ g.conj().T)) > 0.05,
      f"dev {np.max(np.abs(Em_rotA - g @ Em_A @ g.conj().T)):.3f}")
check("the color-blind orientation increments are non-degenerate at finite eps "
      "(weak-record regime; no tension with projective full-strength erasure)",
      var_B > 0.05, f"I-B spread {var_B:.4f}")

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: conditional Born-weighted unraveling of the named weak instruments. On")
print("  the GENERIC FULL-RANK domain (guarded per-branch; sub-minimal occupancy K<3")
print("  is an exact rank-deficient locus; the sea's block is scalar), the single-edge")
print("  induced-link step distribution exists and is non-degenerate for both named")
print("  instrument classes (near-sea full-rank control included), and is exactly")
print("  covariant for the color-blind class. Born enters as an explicit dependency,")
print("  NOT as Record-supplied probability. The CLT route's remaining inputs are four")
print("  named residuals: stationarity, centrality (eps-independent/structural),")
print("  identical-distribution-across-edges (fails as-is), and many-edge independence/")
print("  convolution structure (untested). Discrete-time throughout; no continuous")
print("  generator, stationary law, central-increment law, edge-identity law, or")
print("  cross-edge convolution is supplied. The outcome tree is enumerated exactly")
print("  (no MC); all spreads/variances are instance-labeled. No new axiom/primitive")
print("  or Record-supplied measure/weight/probability rule; r untouched. Audit lane")
print("  grades.")
if FAIL:
    raise SystemExit(1)
