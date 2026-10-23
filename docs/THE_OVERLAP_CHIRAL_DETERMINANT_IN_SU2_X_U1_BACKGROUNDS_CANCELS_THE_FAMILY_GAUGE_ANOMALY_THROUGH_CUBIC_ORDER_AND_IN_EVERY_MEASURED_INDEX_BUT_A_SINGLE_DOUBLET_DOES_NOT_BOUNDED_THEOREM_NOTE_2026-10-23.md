---
claim_id: the_overlap_chiral_determinant_in_su2_x_u1_backgrounds_cancels_the_family_gauge_anomaly_through_cubic_order_and_in_every_measured_index_but_a_single_doublet_does_not_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "The overlap D = 1 + V of the cube walk's Euclidean Wilson kernel (m0 = 1.6) in supplied SU(2) x U(1)_Y link backgrounds on small Z^4 tori (3^4, 4^3x3, 4^4), with Luscher's projector P_hat_- = (1 + sign H)/2. Exact (algebra, checked to rounding): GW, g5-hermiticity and D P_hat_- = P_+ D in non-abelian backgrounds; lattice pseudo-reality makes the Y = 0 doublet's SU(2) covariant anomaly tr(T^a g5 D(x,x)) vanish at every site, tr(T^a g5 D) odd and tr(g5 D) even in Y; the fixed-psi-bar-basis, parallel-transported Weyl determinant phase changes under a gauge rotation by -(1/2) sum_x omega(x) tr(T g5 D(x,x)). Consequence (exact charge algebra plus those parities): for the 16 per colour-summed family every term of order 2 and 3 in the background in the covariant anomaly cancels identically on the lattice (sum Y = sum Y^3 = sum_doublets Y = 0); order-4 coefficients (sum Y^5 = 5/9, sum_doublets Y^3 = -1/9) do not. Finite diagnostics: (a) one doublet's anomaly scales as eps^2 (exponents 1.97, 2.01), (b) the family's as eps^4 (4.02, 4.03); on 4^3x3 at eps = 0.1, (b)/(a) = 0.060 (U(1)_Y) and 0.0065 (SU(2)). Indices in 4^4 non-abelian backgrounds with abelian flux equal -sum f^2 for every flavour, including the (SU(2) x U(1))/Z2 half-flux background (Q, L, u, d, e, nu = -1, -5, -4, -1, -9, 0), and sum_f Y index = 0 exactly for the family but not for one doublet. Mod-2: one Q doublet has odd index; the family's doublets give -8. Not covered: a non-perturbative existence proof (open in the literature); the removability of the order-4 remainder by a local measure term; the pi_4 Witten anomaly itself; Q = 1 SU(2) instantons; continuum limits; SU(3)."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_bounded_theorem_note_2026-10-23
runner: scripts/the_overlap_chiral_determinant_in_su2_x_u1_backgrounds_cancels_the_family_gauge_anomaly_through_cubic_order_and_in_every_measured_index_but_a_single_doublet_does_not_2026_10_23.py
---

# The overlap chiral determinant in SU(2) x U(1) backgrounds cancels the family gauge anomaly through cubic order and in every measured index, but a single doublet does not

Claim type: bounded_theorem (exact lattice identities plus labelled finite diagnostics; literature results cited
as supplied). Runner: runner.py, TOTAL: PASS=10 FAIL=0, 19.4 s, peak footprint 381 MB, 2.7 k characters of
stdout; tested directly under a unique filename (exit 0), not yet through scripts/runner_cache. Axioms unchanged.
No candidate law or axiom-level rule is proposed or edited.

## Question

The register adopts history-level matter weighting by the overlap, with chiral content picked by Luscher's
P_hat. Its open item is non-abelian chiral gauge fields. In small SU(2) and SU(2) x U(1)_Y lattice backgrounds,
does the P_hat chiral determinant show the anomaly structure that makes the 16's content consistent, and does it
fail for content that should fail?

## Repo check

- PR #10049 (overlap from the walk): construction, U(1) results, adopted clause. This note extends it to
  non-abelian backgrounds and keeps its conventions (X = D_W - m0, H = g5 X, D = 1 + g5 sign H).
- On main: SU2_WITTEN_Z2_ANOMALY_THEOREM_NOTE_2026-04-24, LH_DOUBLET_SU2_SQUARED_HYPERCHARGE_ANOMALY_CANCELLATION
  _NOTE_2026-05-01, AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03. These are trace
  identities on supplied content. This note does not re-claim them; it measures the lattice operator they would
  apply to, and its charge sums (B4) agree with them.
- Open PRs #9879 (anomaly-free currents fix hypercharge on supplied chiral content), #10014, #9903, #10004:
  not contradicted; none builds a non-abelian lattice chiral determinant.

## Set-up (what is supplied)

- Gauge group SU(2) x U(1)_Y and the 16's left-handed content per family: Q (doublet, Y = 1/6, 3 colours),
  L (doublet, -1/2), u^c (-2/3, x3), d^c (1/3, x3), e^c (1), nu^c (0). Colour is a spectator multiplicity
  (no SU(3) field). Test (a) is one doublet alone (L; Q alone is also printed).
- m0 = 1.6, inside the one-species window 0 < m0 < 2 of #10049. It was chosen because at m0 = 1 a flux-3
  singlet on 4^4 has index 0 (lattice too coarse; exploratory scan: m0 = 1.4, 1.8 give -9, 0.6 fails at
  flux 2). It is a resolution choice, not a fit.
- Backgrounds: smooth random SU(2) links exp(i eps A.sigma/2) and U(1)_Y phases exp(i 2 eps Y B), with A, B
  built from momenta in {-1, 0, 1}^4 (seeded). Topological backgrounds: abelian flux in the (12) and (34) planes
  inside SU(2) x U(1), times a random smooth SU(2) x U(1) perturbation (strength 0.15), so they are genuinely
  non-abelian.
- The (SU(2) x U(1))/Z2 global form in A2 (half SU(2) flux plus half hypercharge flux per unit 6Y). It is
  consistent because every doublet of the 16 has odd 6Y and every singlet even 6Y. This global form is supplied.

## Observable, and its ambiguity

Fixed-basis Weyl determinant: W(U) = det(ubar^+ D v), with ubar a field-independent basis of P_+ and v a
basis of P_hat_-(U) obtained by Lowdin (to first order, parallel) transport of a reference basis V0. Exact
lemma (D1, also derived): under U -> U^g, g = exp(i eps Omega),

  d arg W / d eps = -(1/2) Tr(sign H Omega) = -(1/2) sum_x omega(x) tr(T g5 D(x,x)).

So the gauge variation of the chiral phase is the smeared covariant anomaly density tr(T g5 D(x,x)), the
quantity measured in B. Known ambiguity: v -> v Q(U) multiplies W by det Q(U), an arbitrary phase function on
field space (the measure term). The phase is therefore defined only up to this choice. The anomaly-free
condition (Luscher) is that some local, smooth, integrable choice makes W gauge invariant. A nonzero lattice
density does not by itself prove an anomaly, and a small one does not prove that a valid choice exists. What
the measurement can decide is whether the density cancels between multiplets, at which order, and whether the
integrated (topological) part cancels exactly.

## A. Topology: exact integers in non-abelian backgrounds (4^4, doublet dim 2048)

- A1. SU(2) flux nW = 2 (component fluxes +-1 in both planes; instanton number 2). Measured indices are
  Q = L = -2 and 0 for the singlets, matching -sum f^2. Integrated Y anomaly sum_x Y tr(g5 D) = -2 Y index:
  (a) L alone gives Y index = 1, not 0. (b) For the family, 3(1/6)(-2) + (-1/2)(-2) = 0 exactly (SU(2)^2 Y).
- A2. (SU(2) x U(1))/Z2 half-flux background nW = mY = 1. Component fluxes are f = (s + 6Y)/2 for doublets and
  6Y/2 for singlets. Measured indices Q, L, u, d, e, nu = -1, -5, -4, -1, -9, 0 all equal -sum f^2 (H gap
  0.195). sum_f mult Y index = 3(1/6)(-1) + (-1/2)(-5) + 3(-2/3)(-4) + 3(1/3)(-1) + (1)(-9) = 0 exactly. This
  one background tests Y^3 and T^2 Y together. (a) L alone gives 5/2.
- A3. Mod-2 count. One Q doublet has odd index (-1) in A2; the family's doublets give 3(-1) + (-5) = -8, even.
  The Witten count is 4 doublets per family (even). The pi_4(SU(2)) global anomaly is NOT measured: a torus
  lattice in 4D has no mapping-torus direction, and no Q = 1 pure SU(2) background was built. Periodic
  abelian-embedded SU(2) flux always has even instanton number 2 n12 n34, which is why A2 needs the Z2 form.
  A3 is the index-parity input of Witten's argument, not the global anomaly.

## B. Local anomaly density: (a) one doublet versus (b) the family

- B4 (exact arithmetic, with C2's parities). Expand tr(g5 D_f(x,x)) and tr(T^a g5 D_f(x,x)) in powers of the
  background, where the flavour sees W (SU(2)) and Y B (U(1)). C2 shows tr(g5 D) is even in Y and tr(T^a g5 D)
  is odd in Y, and pseudo-reality kills the Y = 0 SU(2) part. Then the U(1)_Y density sum_f Y_f tr(g5 D_f) is,
  order by order:
  - order 2: proportional to sum Y^3 (BB) and sum_doublets Y (WW);
  - order 3: proportional to sum_doublets Y (WWW); the (YB)^2 W term carries tr T = 0;
  - order 4: proportional to sum Y^5 (B^4), sum_doublets Y^3 (B^2 W^2) and sum_doublets Y (W^4).
  The SU(2) density follows the same pattern: sum_doublets Y at orders 2 and 3, sum_doublets Y^3 at order 4.
  For the 16, sum Y = sum Y^3 = sum_doublets Y = 0, but sum Y^5 = 5/9 and sum_doublets Y^3 = -1/9. So on the
  lattice, for any background, the family's covariant anomaly cancels identically through cubic order and not
  at quartic order. This is exact, but it is a statement about expansion orders, not a proof of removability.
- B3 (3^4, eps = 0.2, 0.1, 0.05). Fitted exponents: (a) 1.97 (Y), 2.01 (SU(2)); (b) 4.02, 4.03. At eps = 0.05,
  (b)/(a) = 1.6e-2 (Y) and 2.1e-3 (SU(2)).
- B1, B2 (4^3 x 3, doublet dim 1536). At eps = 0.2: U(1)_Y max_x |density| (a) 1.40e-3, (b) 3.14e-4 = 0.22(a),
  which is 2.5% of the sum of |terms| (1.25e-2). The e^c term (Y^5) dominates the order-4 remainder. At
  eps = 0.1, (b)/(a) = 0.060 (it falls by 3.7; eps^2 predicts 4). SU(2): (a) 1.60e-3, (b) 4.0e-5 at eps = 0.2;
  (b)/(a) = 0.0065 at eps = 0.1. sum_x of (b) is 0 (topologically trivial background).
  Exploratory (not in the runner, superseded for memory): 4^4 at eps = 0.2 gave Y (b) = 0.16(a), 2% of
  |terms|, and SU(2) (b) = 0.021(a). An earlier fixed 15% threshold on the 4^4 Y ratio FAILED (0.16); the
  runner instead tests the predicted eps^2 fall, a criterion fixed from B4 before it was run on 4^3 x 3.
- Reading. Gauge covariance makes the order-4 remainder gauge-invariant built from field strengths: F^4-type
  densities of dimension 8, suppressed by a^4 in the classical continuum limit. That dimension count is
  supplied by argument, not measured here. Whether a local measure term removes the remainder at finite
  spacing is exactly the non-abelian existence question. Luscher's all-orders perturbative construction says
  yes for anomaly-free content (supplied).

## C, D. Exact structure

- C1 (3^4, Q doublet, eps = 0.3). GW 9e-15, g5-hermiticity 4e-16, P_hat_- = (1 + sign H)/2 is a projector,
  D P_hat_- = P_+ D to 4e-15; H gap 0.70.
- C2. Y = 0 doublet: tr(T^a g5 D(x,x)) = 3e-15 at every site (SU(2) has d_abc = 0, so a doublet alone has no
  perturbative SU(2) anomaly, and on the lattice this holds exactly by U* = s2 U s2). Y-parities hold to 1e-14.
- D1. The finite-difference fixed-basis phase variation equals the lemma: 8.366e-5 (U(1)_Y) and -1.262e-3
  (SU(2) T^3), both to more than 4 digits.

## Verdict

Within these finite backgrounds, the P_hat chiral determinant has the anomaly structure the 16 needs:
- exact integer cancellation of the integrated U(1)_Y anomaly in non-abelian topological backgrounds, including
  the Z2 one that probes Y^3 and T^2 Y together;
- exact lattice cancellation of the local covariant anomaly through cubic order in the background;
- a quartic remainder that is small and shrinks as eps^2 relative to the anomalous case.
A single doublet (a) fails all of these at O(1) relative size: its density is order 2, and its integrated
anomaly is nonzero (Y index = 1 and 5/2). This is a finite numerical diagnostic, not a non-perturbative
existence proof. That problem remains open in the literature: Luscher proved the abelian case exactly and the
non-abelian case to all orders of perturbation theory; Kikukawa, Suzuki et al. have partial non-perturbative
results (supplied as cited).

## Anti-smuggling gate

No rule is proposed; this is a test of the adopted clause. Supplied by name for the test: SU(2) x U(1)_Y, the
16's hypercharges, and the Z2 global form. If these were rule content they would fail criterion 2, but here they
are only test inputs. The clause's prediction that "chiral content must be anomaly-free" is a postdiction for
the 16. The non-trivial outputs are the exact order-by-order cancellation pattern and the integer index sums;
these are standard consequences, now observed on the walk's overlap. Gate: N/A (no rule); the clause's open
item narrows but does not close.

## Smuggling review

Forced by the construction: the GW, pseudo-reality and parity identities; the phase-variation lemma; the
integer indices; and the order-2/3 cancellation, given the content. Supplied: the gauge group and content;
m0 = 1.6 (resolution); the Z2 global form; background shapes and strengths; the 3^4, 4^3 x 3, 4^4 sizes; the
continuum dimension-counting reading of the order-4 remainder; and the literature existence results.

## Not covered

A non-perturbative existence proof or an explicit local measure term; the pi_4 Witten anomaly; pure SU(2)
Q = 1 instantons; SU(3) colour fields; rough (non-admissible) fields; continuum and infinite-volume limits; a
tick (transfer-matrix) form; gravitational sum Y (no curved background).
