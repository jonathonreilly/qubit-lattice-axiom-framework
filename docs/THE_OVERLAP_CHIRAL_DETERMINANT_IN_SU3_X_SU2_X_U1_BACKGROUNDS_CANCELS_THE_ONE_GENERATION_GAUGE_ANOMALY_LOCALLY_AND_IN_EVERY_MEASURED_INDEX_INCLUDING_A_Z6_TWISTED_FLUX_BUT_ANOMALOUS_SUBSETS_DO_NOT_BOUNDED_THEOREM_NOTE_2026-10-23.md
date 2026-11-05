---
claim_id: the_overlap_chiral_determinant_in_su3_x_su2_x_u1_backgrounds_cancels_the_one_generation_gauge_anomaly_locally_and_in_every_measured_index_including_a_z6_twisted_flux_but_anomalous_subsets_do_not_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "The overlap D = 1 + V of the cube walk's Euclidean Wilson kernel (m0 = 1.6) with Luscher's P_hat_- = (1 + sign H)/2, in supplied SU(3) x SU(2) x U(1)_Y link backgrounds on the 3^4 torus (largest dense dimension 1944, the Q multiplet), for one generation of supplied left-handed content Q(3,2,1/6), u^c(3b,1,-2/3), d^c(3b,1,1/3), L(1,2,-1/2), e^c(1,1,1), nu^c(1,1,0). Exact to rounding: GW, g5-hermiticity and the P_hat split for an antitriplet; lattice charge conjugation (antitriplet SU(3) density = -triplet's, U(1) density equal) and hence exact site-by-site vanishing of the family's SU(3)^3 and SU(3)^2 Y densities in pure SU(3) backgrounds and of SU(2)^2 Y in pure SU(2) backgrounds. Integers: in a simply-connected Cartan SU(3) flux and in one Z6-twisted fractional flux, each with a random non-abelian SU(3) x SU(2) x U(1) perturbation, every measured index equals -sum f^2 and sum Y index = 0 for the family. Finite diagnostic: in generic backgrounds the family's covariant anomaly density falls as eps^4 (3.98, 4.07, 4.05 in U(1)_Y, SU(3), SU(2) directions), lone Q as eps^2; three contrast sets fail exactly in the directions their charge sums predict (15/15). Not covered: a non-perturbative existence proof (open), the gravitational Tr Y (no curved background), larger lattices, other Z6 bundles, the pi_4 / Witten anomaly, derivation of the content."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_bounded_theorem_note_2026-10-23
  - the_overlap_chiral_determinant_in_su2_x_u1_backgrounds_cancels_the_family_gauge_anomaly_through_cubic_order_and_in_every_measured_index_but_a_single_doublet_does_not_bounded_theorem_note_2026-10-23
runner: scripts/the_overlap_chiral_determinant_in_su3_x_su2_x_u1_backgrounds_cancels_the_one_generation_gauge_anomaly_locally_and_in_every_measured_index_including_a_z6_twisted_flux_but_anomalous_subsets_do_not_2026_10_23.py
---

# The overlap chiral determinant in SU(3) x SU(2) x U(1) backgrounds cancels the one-generation gauge anomaly locally and in every measured index, including a Z6-twisted flux, but anomalous subsets do not

Claim type: bounded_theorem (exact lattice identities plus labelled finite diagnostics). Runner: runner.py,
TOTAL: PASS=10 FAIL=0, 39-46 s, peak RSS 313 MB, 3.6 k characters of stdout; tested under a unique filename
(exit 0), not yet through scripts/runner_cache. Axioms unchanged. No candidate law or axiom-level rule is
proposed or edited.

## Question

CL-1 history-level matter weighting uses the overlap with Luscher's P_hat. The SU(2) x U(1) probe (PR #10051)
left SU(3) colour as a spectator multiplicity. With colour as a dynamical SU(3) link field, does the P_hat
determinant for one generation show the full SM anomaly cancellation (SU(3)^3, SU(3)^2 Y, SU(2)^2 Y, Y^3), and
fail for subsets that should fail?

## Repo check

- PR #10049 (overlap from the walk) and PR #10051 (SU(2) x U(1)): conventions kept (X = D_W - m0, H = g5 X,
  D = 1 + g5 sign H, m0 = 1.6, same flux construction). This note extends #10051 to SU(3).
- Main: AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03, COLOR_SU3_MATTER_REALIZATION_
  RESIDUAL_MAP_2026-06-05 (trace identities / colour residuals on supplied content). Not re-claimed; the exact
  charge sums printed by the runner agree with them.

## Supplied

- Group SU(3) x SU(2) x U(1)_Y, one generation's content and hypercharges (from the earlier 5-mode / Spin(10)
  results; not derived here). Contrast field X(3,1,-1/3) (chosen to be a rep of the Z6 quotient).
- m0 = 1.6; seeded smooth random backgrounds (momenta in {-1,0,1}^4); lattice 3^4 only.
- The Z6 global form in A2: one twisted flux, SU(3) centre direction (1/3,1/3,-2/3), SU(2) (1/2,-1/2), U(1)
  1/6 per unit 6Y, in both the (12) and (34) planes.

## Results (out.txt)

Exact charge coefficients (Tr Y^3, Tr_3 Y, Tr_2 Y, SU(3)^3 count, Tr Y): family 0,0,0,0,0; lone Q
1/36,1/3,1/2,2,1; no u^c 8/9,2/3,0,1,2; quarks only -3/4,0,1/2,0,0; family + X -1/9,-1/3,0,1,-1.
Note: quarks alone pass Tr Y (gravitational) and SU(3)^2 Y; they fail Tr Y^3 and SU(2)^2 Y.

A. Topology (3^4, random SU(3)xSU(2)xU(1) perturbation 0.15, H gap >= 0.50):
- A1 simply-connected SU(3) Cartan flux diag(1,-1,0): indices Q,u,d,L,e,nu,X = -4,-2,-2,0,0,0,-2, all = -sum f^2.
  sum Y index: family 0 (SU(3)^2 Y); lone Q -2/3; no u^c -4/3; quarks 0; +X 2/3 (each = charge prediction).
- A2 Z6-twisted fractional flux: indices -3,-2,-1,-1,-1,0,-1, all = -sum f^2. sum Y index: family 0 (probes
  Y^3, SU(3)^2 Y, SU(2)^2 Y together); lone Q -1/2; no u^c -4/3; quarks 1/2; +X 1/3.
- A3 abelian blocks (component index idx(f) = -f^2 measured for f = -1,0,1): colour diag(1,1,-2)-weighted
  integrated anomaly (SU(3)^3) and weak-T3-weighted (SU(2)^2 Y) are 0 for the family in A1 and A2; no u^c -2,
  +X -2/+2 (colour); quarks -1/2 (weak, A2). This step is charge algebra on measured component indices.
- A4: every 16 field (and X) has integer component fluxes in the twisted background; (3,1,0) and (1,2,0) do
  not; (3,1,2/3) does. Arithmetic, not a lattice measurement.

B. Single-factor backgrounds (3^4, eps = 0.3), exact:
- B1 pure SU(3): antitriplet tr(T g5 D(x,x)) = -triplet's and tr(g5 D) equal, to 1e-14 (lattice C). Family
  SU(3) density 1e-14 and Y-weighted density 5e-15 at every site; no u^c 2.2e-3 / 4.2e-3; +X 2.2e-3; lone Q 4.4e-3.
- B2 pure SU(2): family Y-weighted density 4e-15 (3 colours x Q + L); quarks only 1.1e-3.
- B3 pure U(1)_Y scan eps = 0.2, 0.1, 0.05: exponents family 3.95, lone Q 2.00, no u^c 1.98, quarks 1.99, +X 2.11.

C. Generic SU(3) x SU(2) x U(1) backgrounds (3^4, all three factors at strength eps = 0.2, 0.1, 0.05). Fitted
exponents of max_x |anomaly density| in U(1)_Y / SU(3) / SU(2) directions, pre-set prediction from the charge
sums (x anomalous: |s-2| < 0.3; o cancelled: s >= 2.7):
- family     o 3.98  o 4.07  o 4.05
- lone Q     x 2.00  x 1.99  x 1.97
- no u^c     x 1.96  x 2.01  o 4.05
- quarks     x 2.03  o 4.07  x 1.97
- family + X x 1.96  x 1.98  o 4.05
All 15 match. Family / lone Q at eps = 0.2: 0.19 (Y), 0.063 (SU(3)), 0.079 (SU(2)); at eps = 0.05: 1.2e-2,
3.5e-3, 4.4e-3.
Unexpected (observed, not explained here): the residual is order 4, not 3, even though a d_abc-weighted order-3
charge sum (sum_coloured Y x (+-1) x dim_w = 2/3) does not vanish for the family. A gauge-invariant order-3
covariant density (eps FFF type) evidently vanishes on this lattice/background class; the cause (hypercubic or
C x P structure) is not proved. The pre-set criterion was s >= 2.7, so this does not affect the pass.

D. GW, g5-hermiticity, P_hat projector and D P_hat_- = P_+ D for u^c in a generic SU(3) x U(1) background: 1e-14.

## Verdict

Within these finite 3^4 backgrounds, the P_hat chiral determinant shows the full one-generation SM anomaly
structure: integrated U(1)_Y anomaly cancels exactly (integers) in a simply-connected and in a Z6-twisted
topological background; the local covariant anomaly cancels at the continuum (eps^2) order in all three gauge
directions, with an eps^4 remainder; and three subsets fail in exactly the predicted directions. This is a
finite numerical diagnostic, not a non-perturbative existence proof (open in the literature; Luscher's
non-abelian construction is all-orders perturbative).

Global form, honestly: tested is one twisted bundle of the Z6 quotient (n = 1, fractional fluxes 1/3, 1/2, 1/6
per factor, integer per component), in which all 16 fields are admissible and give integer indices; not tested
are other Z6 bundles, Z2/Z3-only quotients, or any statement that the lattice prefers the quotient. The other
sections use the simply-connected group.

## Anti-smuggling gate

No rule proposed; this tests CL-1. The group, content, hypercharges and the Z6 form are supplied test inputs
(would fail criterion 2 if they were rule content). Gate: N/A. CL-1's SU(3) open item narrows; it does not close.

## Smuggling review

Forced by the construction: GW / C / pseudo-reality identities; integer indices; the order-2 cancellation given
the content. Supplied: group, content, Y values, Z6 twist, m0, backgrounds, lattice size, the eps^4 reading.
Not measured: Tr Y (gravitational), the pi_4 global anomaly, rough fields, continuum and larger volumes.
