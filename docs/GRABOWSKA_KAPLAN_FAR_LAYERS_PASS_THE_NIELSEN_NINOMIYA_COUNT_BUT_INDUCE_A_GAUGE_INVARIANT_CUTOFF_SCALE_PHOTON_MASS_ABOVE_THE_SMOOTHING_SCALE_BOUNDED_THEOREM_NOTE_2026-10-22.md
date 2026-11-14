---
claim_id: grabowska_kaplan_far_layers_pass_the_nielsen_ninomiya_count_but_induce_a_gauge_invariant_cutoff_scale_photon_mass_above_the_smoothing_scale_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For free Shamir domain-wall slabs (Wilson kernel, M = 1, Ls = 8 and 16, Pauli-Villars subtraction) in 2D and 4D momentum space, their overlap (infinite-Ls) form, an 8 x 8 2D SU(2) lattice and a 1+1D Chern-strip Hamiltonian slab (N = 32, Ls = 8): (A) the light-end chiral propagator element has its pole at p = 0 and zeros of opposite net chirality at the three doubler corners, the mirror element is its mirror image, and the boundary field is one vector-like pair, so the gauge-off slab meets the generalized Nielsen-Ninomiya theorem and is evaded only at gauging, through the mirror's range-r coupling; (B) when the far layers read A_* != A, the effective action gains (c/2)(A - A_*)^2, with c = d^2 Gamma/dA^2 the curvature, which is gauge invariant and protected by nothing: c = -0.0221 per q^2 in lattice units for the Shamir slab at constant layer fields, the same for the cut positions, ramp widths and Ls tested, and c = 2 <g_00> = 0.0997 in the overlap form, with g the quantum metric of the Wilson bands, nonzero whenever the bands carry the light chiral cone; in 4D, at constant layer fields (the window k >> 1/r; the finite-k response is not computed), this is a conditional estimate of a photon mass 0.2-0.4/a, 4e17-9e17 GeV if a = sqrt(8 pi) l_P (supplied), while in 2D the term is marginal (0.23 per q^2), which is why the 2D toy passed; (C) the slab is exactly gauge invariant at every r, and the mirror's residual field-strength coupling for block reading is |sin(kb/2)/(b sin(k/2))| <= pi/(b|k|) for 0 < |k| <= pi (O(1/b) at fixed k; the small-k envelope 2/(kb) is not a bound in the zone: at b = 8, k = 7 pi/8 the filter is 0.1274 > 0.0909) and gaussian in r for flow, but the induced term grows to its full value; (D) 2D SU(2) block-flux spreading with comb-tree anchor transports is per-site covariant to 2e-15, spreads every block's flux evenly, and keeps block loops, boundary-line holonomies and the 't Hooft twist exactly; (E) a layer-blind fold quench fills the light and mirror edge modes equally (exact end-exchange symmetry), so a thermal mirror would give Delta N_eff = 2.25 (a conditional estimate; 14 sigma from the supplied Planck value). Supplied model, finite diagnostic; no rule is adopted."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - far_layers_reading_a_smoothed_field_decouple_the_mirror_from_field_strength_but_not_from_gauge_turns_topology_or_long_wavelengths_bounded_theorem_note_2026-10-22
runner: scripts/grabowska_kaplan_far_layers_pass_the_nielsen_ninomiya_count_but_induce_a_gauge_invariant_cutoff_scale_photon_mass_above_the_smoothing_scale_2026_10_22.py
---

# Grabowska-Kaplan far layers pass the Nielsen-Ninomiya count but induce a gauge-invariant mismatch term, a cutoff-scale photon mass in 4D slab models at constant layer fields (conditional estimate)

Claim type: bounded_theorem.
Primary runner: `scripts/grabowska_kaplan_far_layers_pass_the_nielsen_ninomiya_count_but_induce_a_gauge_invariant_cutoff_scale_photon_mass_above_the_smoothing_scale_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The [smoothed far-layer note](FAR_LAYERS_READING_A_SMOOTHED_FIELD_DECOUPLE_THE_MIRROR_FROM_FIELD_STRENGTH_BUT_NOT_FROM_GAUGE_TURNS_TOPOLOGY_OR_LONG_WAVELENGTHS_BOUNDED_THEOREM_NOTE_2026-10-22.md) (PR #9980; that file is not in this repository and is recorded only in the consolidation's source map, so this link resolves only on its source branch) proposed the leading chirality route: a layer slab inside each role block, where layer s hops on rung-s flux-smoothed links and the light end reads fine links. This note is a hostile check of that route against four known obstructions:
- the generalized Nielsen-Ninomiya theorem of Golterman and Shamir;
- the problems known for Grabowska-Kaplan (GK);
- the non-abelian extension;
- the requirement that the mirror starts empty.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

Local labels (2026-11-14). "CL rules" and "CL-3" below are this note's source labels for rules as the source notes stated them (the fold, its misfolds, the split, a vacuum standard). They are not clauses of the current [candidate-law register](CANDIDATE_LAWS.md), whose CL-1, CL-2 and CL-3 are historical aliases with zero premise weight. Statements that use them are conditional on those supplied rules. Sources named here only by a short name (gk-smoothed-layers, rung-dimension-chirality, fold-inflaton, neighbourhood-roles) are recorded only in the consolidation's source map; where a step rests on one of them, it is a historical reported result, unverified here.

Repo check: origin/main contains no note on Grabowska-Kaplan or on smoothed far layers. The Golterman hits on main are corner-fermion and reflection-positivity notes and do not engage the generalized theorem. The Spin(10) atomic-gap note (2026-09-14) treats a frozen mirror boundary, which is a different mechanism. Open PRs: #9980 (the route under test) and #9944 (zeros-ghosts: propagator zeros sit on the partner's line). This note builds on #9980 and narrows its sections C and E. It is consistent with #9944: the zeros in A1 below are kinematical.

## Statement

A. The spectrum count (gauge off).
1. Theorem (argument principle). On the zone torus, the windings of a chiral propagator element around its singular points sum to zero. In the free 2D slab, the light-end element (layer 0, P_-) has its pole at p = 0, with winding +1, and zeros at (pi,0), (0,pi) and (pi,pi), with windings -1, -1 and +1. The light end alone is therefore one Weyl pole plus kinematical zeros of opposite net chirality. The mirror element (layer Ls-1, P_+) is its mirror image, so the boundary field is one vector-like pair (A1).
2. Which assumption fails. None of them. The theorem's conditions in 2505.20436 are:
   - a finite-range, fermion-only Hamiltonian;
   - an unbroken compact symmetry G;
   - a free massless relativistic continuum;
   - a zero-free complete set of interpolating fields.

   The gauge-off slab meets all four, and its spectrum is vector-like, as the theorem demands: the mirror pole is present. GK evades only a corollary, "a vector-like spectrum gives a vector-like gauge theory". That corollary needs both ends to couple to the field through the local conserved current. In the slab the mirror reads A_*, a functional of range r whose form factor satisfies f(0) = 1 exactly, because flow and block reading keep the k = 0 mode. The gauge theory is therefore chiral only for 1/r << k << 1/a. Below 1/r it is vector-like, and the mirror's charge is visible in Gauss's law beyond r (A2).

B. The induced term (the decisive result).
1. Diagnostic (4D Shamir slab, DW minus PV, constant layer fields). The layer response Pi^{st}, the second derivative of -log det with respect to a constant A on layers s and t, has rows that sum to zero (the Ward identity; 7e-4 at N = 16, falling with N). Let the near layers read A and the far layers read A_* = 0, as in the window k >> 1/r. Then Gamma gains (c/2) A^2 per q^2, where c = d^2 Gamma/dA^2 = -0.0221 (lattice units) is the curvature that the runner computes. This value is the same for:
   - every cut position j = 2..6 (-0.0219 to -0.0221);
   - ramp widths 1, 2 and 4 layers (-0.0221 to -0.0220);
   - Ls = 8 and Ls = 16 (-0.0218 and -0.0217 at N = 12).

   So it is an end term (the light Weyl and the mirror separated in field), not a bulk F_{s mu}^2 term, and spreading the transition over many layers does not remove it (B1).
2. Theorem (overlap form). For Ls -> infinity, |det| = |<v(A)|v(A_*)>|^2 at each momentum. For a constant A and A_* = 0, -log|<v(p+A)|v(p)>|^2 = g_00(p) A^2 + O(A^3), where g is the quantum (Fubini-Study) metric of the filled bands of H_W = g5 D_W(-M). So Gamma = <g_00> A^2 = (c/2) A^2 with curvature c = 2 <g_00>_BZ = 0.0997, equal to the direct second difference 0.09970. Since g >= 0, c vanishes only if g_00 = 0 everywhere, that is, if the filled projector does not depend on p_0, the direction of A. Then D = 1 + g5 sign(H_W) does not depend on p_0 either, so it cannot have the cone D = i p-slash/M at p = 0 that the light mode needs. The light chiral cone therefore forces the term (B2). (Corrected 2026-11-14: the earlier text said "momentum independent" and wrote the action term as c (A - A_*)^2; with c the curvature the Taylor coefficient is c/2.)
3. Why gauge invariance does not help. A and A_* turn alike, so A - A_* is gauge invariant, and (c/2)(A - A_*)^2 is allowed. It vanishes for k << 1/r, where A_* -> A, and takes its full value in the window. The exact gauge invariance of the smoothed slab (#9980 A1, C2) is real but irrelevant to this term.
4. Conditional estimate (inputs: e^2 = 4 pi/137, sum Q^2 = 16 over three families, a = sqrt(8 pi) l_P, constant layer fields). With Gamma = (1/2) m^2 A^2 and c the curvature, m^2 a^2 = e^2 c sum Q^2, so m_gamma a = 0.18 (Shamir, with m^2 < 0, tachyonic) or 0.38 (overlap), that is 4e17 to 9e17 GeV, in the window k >> 1/r at constant layer fields (the finite-k 4D response is not computed). If it holds there, there is no electromagnetism at distances below r, while r >> 1/m_e is needed (#9980 E2, a historical reported result). A local A^2 counterterm is not gauge invariant. Only a supplied -(c/2)(A - A_*)^2 clause, tuned to about 1e-90 (the photon mass bound against 1/a, squared), cancels it (B3).
5. 2D. The same term is dimensionless there: c2 = 0.227 per q^2 in the overlap form, comparable to the Weyl Schwinger-type term (ratio 1.43). It is marginal, not a cutoff mass. This is why the 2D toy passed: #9980 C2 has smoothed/unsmoothed photon response 0.26-0.33 rather than 1/2, and that is this term (B4).

C. Scaling with the smoothing radius r (abelian). The slab is exactly gauge invariant at every r, so no gauge non-invariance appears that could fall with r. What does fall is the mirror's residual field-strength coupling at fixed k:
- block (box) reading: |sin(kb/2)/(b sin(k/2))| <= 1/(b |sin(k/2)|) <= pi/(b|k|) for 0 < |k| <= pi (Jordan's inequality sin x >= 2x/pi on [0, pi/2]), so the coupling is O(1/b) at fixed k in amplitude and O(1/b^2) in the action (measured 0.97, 0.53, 0.11, 0.024 for b = 16, 64, 256, 1024 at k = 2 pi 37/4096). The envelope 2/(kb) holds only for small kb and is not a bound in the zone. Negative result (corrected 2026-11-14): at b = 8, k = 7 pi/8 the filter is 1/(8 sin(7 pi/16)) = 0.1274, above 2/(kb) = 2/(7 pi) = 0.0909 (runner C1b);
- flow: (1 - eps khat^2)^n, gaussian in r ~ sqrt(n).

The induced term (c/2)(1 - f(kr))^2 grows to its full value as r grows. It does not fall (C1, C1b).

D. Non-abelian (SU(2), 8 x 8).
1. Theorem (covariant block-flux spreading). In each b x b block, take the comb tree from the anchor c: down the column, then along the bottom row. The tree-frame links phi(a)^dag U phi(b) turn only by g(c). The block loop W is read from the tree-frame top links. Every plaquette lasso is set to X = W^(1/b^2), the principal root, which is conjugation covariant. The explicit solution is:
   - interior row-k links X^(-k);
   - the top link of each interior column V_x, with V_(x+1) = X^b V_x T_x;
   - boundary links untouched.

   The closure V_(X+b) = 1 is exactly the statement X^(b^2) = W. Measured: covariance residual 1e-15 (b = 2) and 2e-15 (b = 4); closure 2e-15; within-block angle spread 2e-14; max plaquette angle 2.61 -> 0.67 (b = 2) and 0.12 (b = 4). Link averaging without transports gives 1.57 (D1).
2. Theorem (topology). Block loops and the torus holonomies along block-boundary lines are untouched. The 't Hooft twist (1/2 tr[P_x, P_y] = -0.926 with noise) is kept exactly while its thin plaquette (angle 3.03) is spread to 0.19. A vortex pair with commuting holonomies (twist +1) is spread likewise. The twist is never lost, unlike the abelian anchor reading's Q in #9980 A2. The principal root is undefined only at W = -1 exactly (D2).
3. So the non-abelian smoothing rule exists and is clean. It is not the obstruction.

E. Does any rule fill the far layers?
1. Theorem (end exchange). The Chern-strip slab has the symmetry (x, s) -> (-x, Ls-1-s) with sigma_z, which exchanges the ends. A fold-type order on every site (period 2), ending suddenly, respects it, so it fills light and mirror edge modes equally: 0.6606 each. The same fold on layer 0 alone gives 0.577 against 4.5e-4 (E1).
2. Estimate, on source-local premises (the rules as the source notes state them; historical reported results, unverified here). Every CL rule that creates excitations is layer-blind:
   - the fold and its relaxation into misfolds (free sites on every layer of the role block, neighbourhood-roles, fold-inflaton E);
   - the split's ~0.04 K^2 flips.

   If so, reheating gives the mirror the SM temperature: Delta N_eff = 48 (10.75/106.75)^(4/3) = 2.25 against Planck's 2.99 +- 0.17 (supplied), 14 sigma away. A safe mirror would need rho_mirror/rho_SM <~ 0.1 at reheating, a lopsided reheating that none of those rules supplies (E2, a conditional estimate).
3. Estimate. After reheating:
   - gravity gives Gamma/H ~ (T/M_P)^3 <= 1e-30;
   - sphalerons fill the mirror only with the net winding of each r-cell, ~sqrt(Gamma_sph r^3/H), a density ratio ~1e-45 at 130 GeV for r = R_Earth;
   - a massless mirror, charged for k < 1/r, is pair-produced without mass suppression by any smoothed field with E^2 > B^2 or E.B != 0, so r must exceed the coherence length of every such field. r ~ c/H0, the 200 layers of #9980 E1, is safe (E3).

## Verdict

In the 4D slab models at constant layer fields the route as stated induces a gauge-invariant (c/2)(A - A_*)^2 term. Its exact gauge invariance, its covariant non-abelian smoothing and its topology bookkeeping all hold. But reading a different field at the two ends induces that term, whose curvature c is forced nonzero by the light chiral cone (B2), and in 4D it is a cutoff-scale photon mass in the window k >> 1/r (a conditional estimate with supplied a, alpha and charges; finite k not computed). The route then needs a supplied, fine-tuned gauge-invariant mismatch clause -(c/2)(A_fine - A_read)^2 (one tuned number per gauge factor and charge assignment, to ~1e-90), and, conditional on the source-local reheating premise of E2, a new rule that reheats only the near layers. The 2D toy survives because there the term is marginal.

## Candidate law text (not adopted; what the route would need)

> "Each layer's links enter the response with the mismatch term that cancels the slab's induced (A_s - A_*)^2, measured in the vacuum's own units at every rung."

This is a candidate reading (zero premise weight) of the source notes' CL-3 vacuum standard, applied per rung to the mass part of the link response but not to its F^2 part. It is untested, and as stated it is a tuned subtraction. Reheating would also need a clause that confines excitation creation to layer 0. No such clause is derived, and the fold acts on every site.

## Smuggling check

Supplied: the Shamir and overlap kernels; M = 1; Ls = 8 and 16; the BZ grids (N = 12, 16, 512) and the PV subtraction; the cut and ramp profiles; constant layer fields as the k -> 0 window probe (continuity of the 4D polarization is assumed, not computed at finite k); the SU(2) fields, noise levels and twist eaters; the Chern strip (u = -1) and the period-2 fold of amplitude 0.6; sum Q^2 = 16, alpha, a = sqrt(8 pi) l_P; Planck N_eff.

Forced, given those:
- the winding count and kinematical zeros;
- the Ward identity;
- the cut-, ramp- and Ls-independence of c;
- c = 2 <g> and its positivity;
- the gauge invariance of A - A_*;
- the filter scalings;
- SU(2) covariance, closure and twist conservation;
- the end-exchange equality.

Not derived:
- the sign of c, which depends on the regulator (Shamir/PV negative, overlap positive): only its nonvanishing is forced;
- the finite-k photon response in 4D;
- the non-abelian slab's fermion response;
- the full GK effective action (Ago-Kikukawa 1911.10925 find nonlocal fluff vertices, cited from the abstract only);
- whether any CL-3 reading can supply the subtraction.

## Boundary

These are free-fermion quadratic responses at constant layer fields, plus exact winding, covariance and symmetry checks. Not established:
- interacting (SMG-type) far ends;
- finite-k 4D responses;
- SU(2) x SU(3) fermion slabs;
- real-time far-layer dynamics.

The literature engaged at abstract level is Golterman-Shamir 2311.12790 and 2603.15985, Hamada-Kawai 1705.01317 and Ago-Kikukawa 1911.10925. The conditions of Golterman-Shamir 2505.20436 are taken from its HTML text. No rule is adopted.
