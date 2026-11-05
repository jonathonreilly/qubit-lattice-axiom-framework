D4 zoom fixed-point fermion: overlap index = topological charge, and a domain-wall slab whose light chiral mode keeps dim 6 = 0 (the mirror is unchanged)

Date: 2026-10-26
Claim type: bounded_theorem (exact identities plus finite diagnostics on a supplied free kernel in smooth abelian backgrounds)
Status authority: independent audit lane only. This draft sets no audit outcome.
Runner: runner.py (this folder). AUDIT_TIMEOUT_SEC = 120. 41 s, 576 MB peak, seeded, 10/10, output 3.3 k characters.
  A re-run under a unique filename (scratchpad copy) gave identical output.
Pre-registration: criteria_pre_run.txt, written before any computation. Labels: [T] exact/theorem; [F] finite diagnostic;
[A] supplied literature theorem; [S] reading. Axioms unchanged. No CL edit. Nothing adopted.

Sources used
- d4-zoom-fixed-point-fermion (PR #10098): D* = G*^-1, alpha = 1/2, GW exact, no doublers, dim 6 = 0. Its kernel code is reused.
- History-level matter weighting (CL-1, adopted 2026-10-23), the chiral-tick-form slab, copy-flip-slab (#10063: static slab
  forces q_mirror = q_light), floquet-pi-slab (#10064), overlap-nonabelian / overlap-colour (anomaly sums), luscher-L8 (#10083).
- git grep origin/main finds no W(F4)/D4 overlap or slab note. Open PR #10094 (D4 time-blind events) is the dim-6 base. Nothing is contradicted.

1. Overlap and Luscher projector on the D4 kernel
- [F] 1a. Position-space D* from the L = 12 D4 torus, truncated to the W(F4)-complete shells |d|^2 <= 8 (169 hops):
  symbol error 3.6e-2, min sv(D_R - m0)/m0 = 0.98. DEVIATION: the pre-registered shells |d|^2 <= 4 miss the 5e-2 bar (0.19).
- [F] 1b. U(1) constant fluxes (n12, n34), Landau gauge, straight-line transporters, twisted 6^4 torus of D4 sites (648 sites):
  H = g5 (D_R - m0) Hermitian to 3e-16, so the transition functions are consistent.
- [F] 1c. Index -(1/2) Tr sign(H) = -Q exactly for Q = 0, 1, -1, 2. A charge-q field in Q = 1 gives -q^2 for q = 2, 3, 4, 6.
  Admissibility min|eig H|/m0 = 0.98 ... 0.32; q = 6 is marginal at 0.053 (pre-registered gate 0.05).
- [F] 1d. Q = 1: sign(H) by Newton-Schulz (6 iterations, 1e-14). GW holds to 3e-14 and g5-hermiticity to 2e-15.
  P_hat = (1 - g5_hat)/2 is a projector to 6e-15, and Tr g5_hat = -2.0000 = 2 x index.
  |g5_hat(x,y)| = 7.7e-2, 1.6e-3, 3.6e-4 at |x - y| = 1.41, 2.83, 4.0: decay rate 1.89 per unit (D* itself gave 1.90).
- [T] Gauging breaks the free identity "overlap of D* = D*" only through the truncation and the links. The overlap restores GW exactly.

2. Domain-wall slab with D* along an internal fifth direction
- [T] The fifth coordinate is a layer label. The 5D operator acts on spinors and layers only, so the wall cannot break 4D W(F4).
  [F] 2c: all 576 rotations satisfy D5(Ap) = S D5(p) S^-1 to 5e-15. All 576 reflections give the wall-swapped slab (s -> Ls+1-s) to 5e-15.
  This is the D4 face-swap parity: a reflection exchanges the light Weyl and the mirror.
- [F] 2a. At p = 0 (Ls = 8, M = m0), both the Borici (b5 = c5 = 1/2) and the Shamir forms have exactly 4 null vectors.
  These are one 2-component Weyl per wall: g5 = -1 on wall 1 and +1 on wall Ls, half-slab weight >= 0.9998, next singular value >= 1.
  The 15 doubler classes of pi D4* carry no light modes (min sv 1.04). DEVIATION: the pre-registration said "2 singular values"; the Weyl pair is 2 + 2 components.
- [T] 2b. Borici: (g5 (D* - m0))^2 = m0^2 exactly (the GW circle), so |H_T| is momentum-independent and
  D_eff(Ls) = (1-t)/2 + t alpha D*, with t = ((1+h)^Ls - (1-h)^Ls)/((1+h)^Ls + (1-h)^Ls).
  At finite Ls the light mode is D* plus a momentum-INDEPENDENT residual mass, (1-t)/t = 3.0e-4 at Ls = 8.
  The finite slab adds no new momentum dependence. [F] Checks: 5D Schur complement vs the Moebius formula 6e-16 (Ls = 4, 8; mf = 0, 0.1);
  the identity 3e-16 (Ls = 2..16); (g5 A)^2 - m0^2 = 7e-16. [A] The Moebius D_eff formula is Brower-Neff-Orginos; it is re-verified here.
- [F+T] 2d. Dim 6 of the light chiral mode. The direction anisotropy of the wall mode's vector part, b(eps n)/eps over 5 directions
  (the 4 W(F4) orbit types plus a generic one), scales as eps^5.6-6.0 for the Borici and Shamir Ls = 8 slabs and the Shamir Ls -> inf limit.
  Its size is <= 5e-9 at eps = 0.2, so the dim-6 coefficient is bounded at <= 1e-7. The Z^4 Wilson slab control has exponents 1.6-1.9
  and coefficient 0.12. [T] Molien counts for the rotation group W(F4)+: 1 quartic invariant and 1 cubic vector covariant (both
  isotropic), so dim-6 LIV is forbidden. The first freedom is sextic (2 invariants, i.e. J6). The B4+ hypercube control has 2 of each.
  So the chiral zero mode keeps dim 6 = 0, and the slab's chirality costs no LIV.

3. Anomaly content and the mirror
- [T] 3a. The one-family 16 (left-handed): Y^3, Y-gravity, SU(3)^2 Y, SU(2)^2 Y and SU(3)^3 sums are all 0, and there are 4 doublets (even).
  Lattice: sum mult x (6Y) x index(6Y), with the MEASURED D4 indices (-1, -4, -9, -16, -36), is 0. A lone L gives 54 and a lone Q gives -6.
  Only abelian backgrounds are used here; the non-abelian indices on D4 are not computed (they are covered on Z^4 by overlap-colour).
- [T+F] 3b. The slab acts identically on every gauge label, so the far-wall Weyl carries the light Weyl's charges.
  Under the 8 spatial three-fold turns of the root slice, P- and P+ have the same spectrum {e^{+-2pi i/3}}, so q_mirror = q_light.
  The slab is static (no Floquet pi gap), so the #10063 theorem applies unchanged. The slab is vector-like, and the mirror wall still needs gapping. Nothing got worse.

Verdict (pre-registered rule): CHIRALITY CARRIES OVER (Tests 1-3 PASS)
Two pre-registered details missed, both stated: the shell set (|d|^2 <= 4 -> 8) and the null-vector count (2 -> 4 components).
It carries over at the same level as on Z^4: index = Q, P_hat local, one Weyl per wall, the mirror on the far wall.
Improvement: the light chiral mode now has dim 6 = 0 by symmetry at every Ls. The Borici slab's finite-Ls error is a pure mass.

Does the D4 law now cover gravity-free SM content? Not yet. Remaining rebuilds:
- (i) the far-wall gapping (SMG; unchanged and still the chirality wall);
- (ii) the copy sign's role: D4 has no copies, so the 16 is supplied per field as before;
- (iii) families: the cube-turn/Floquet mod-3 machinery (#10064) was built on the cubic cell and has no D4 counterpart yet;
  the W(F4) three-fold turns exist, but q_mirror = q_light on the static slab;
- (iv) non-abelian indices and the measure term on D4;
- (v) gravity hinge sums on D4;
- (vi) a tick (transfer-matrix) form of the slab (D*'s two-slice buffer).

Proposed CL amendment (UNTESTED for review; NOT adopted)
  Append to the candidate D4 law: "Chiral content is selected by the Luscher projector of the fixed-point weight. Its
  slab form carries the layer label as an internal role coordinate with the Borici step (b5 = c5), so a finite slab adds
  only a momentum-independent residual mass." No new number: m0 = 1/(2 alpha) is forced, and b5 = c5 is the choice that keeps |H_T| flat.
Smuggling gate
- (1) No fitted number. Supplied: alpha, Ls, a5 (each inert for chirality and dim 6). PASS.
- (2) No observed structure is named by the rule. The 16's charges enter only the anomaly CHECK. PASS.
- (3) Untested predictions: there is no chirality-induced LIV at dim 6 for any chiral species. A reflection relates light and mirror walls.
  The residual mass is exactly momentum-independent. UNTESTED.
- (4) It bends the CL-1 matter tick (a history weight plus an internal layer label, as already adopted).
  The infinite image tower (Qubit axiom question) is inherited from #10098 and not resolved here.
- Gate: PASS on (1)-(3). (4) is the same bend as the parent D4 law.

Smuggling review
- Forced or exact: W(F4) covariance of the slab; the Borici identity (from the GW circle); m0 = 1/(2 alpha); the Molien counts; anomaly arithmetic.
- Supplied: the free D* (continuum Dirac inside the image sum, from #10098); the truncation shells; U(1) constant backgrounds and the
  straight-line transporters; the slab forms (Borici, Shamir) and Ls = 8; the Moebius formula [A]; the 16's hypercharges (as a check only).
- Fitted: none.
Deviations from pre-registration: the shell set (1a); the null-vector count wording (2a); q = 6 admissibility marginal (0.053 vs 0.05);
the run's memory is 576 MB (under the probe's 1 GB cap; above the brief's generic 300 MB).
