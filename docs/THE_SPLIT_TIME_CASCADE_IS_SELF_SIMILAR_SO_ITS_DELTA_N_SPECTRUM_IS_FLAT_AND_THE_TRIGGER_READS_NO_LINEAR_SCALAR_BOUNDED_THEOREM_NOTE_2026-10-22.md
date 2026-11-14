---
claim_id: the_split_time_cascade_is_self_similar_so_its_delta_n_spectrum_is_flat_and_the_trigger_reads_no_linear_scalar_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's glued split (a block splits when the mean of its cube's edge registers reaches 4s, its children's edges along parent edges take the parent's value minus s, held edges block a child, and the trigger needs each unsplit +x, +y, +z face neighbour's shared edges full): (A) exact register arithmetic: a generation is s register steps, ln 2 of log-length, for every s; over the 18 edges of a five-tetrahedron block cube the trigger's mean log-length is tr h/6 at first order, so no traceless strain moves it, and on a tensor wave along z it is -(9 h+^2 + 2 hx^2)/72 at second order. (B) An infinite-level cascade whose level-l split-time spread has a level-independent shape, variance sig^2 lam^l, no cross-level covariance (or covariances with the same scaling) and a convergent level sum has Delta^2(2k) = lam Delta^2(k), so its octave-averaged index is n_s - 1 = log2 lam; the identity allows Delta^2 = k^(log2 lam) f(log2 k) with any period-one f, so it does not fix the local index (witness f = 1 + 0.1 cos 2 pi x; the 1D blocky shape itself gives a local index between -2.5 and +2.8 at lam = 1), and a finite cascade has boundary terms. In a 2D block-tree toy that keeps the trigger rule, with Poisson stepping of each register supplied to give the trigger a timing spread, the mean wait per generation stays ln 2 e-folds, the coupled (max-plus) trigger raises the wait variance by 1.8 and correlates waits (neighbours +0.32, parent-child -0.14), and the deep levels are stationary (deepest per-level ratio 0.9994 against the 0.976 that n_s = 0.965 needs); the per-level spread (ln 2)^2/(m s) contains only register numbers, so s and the window set the amplitude, never the tilt. (C) Given the cited stationary-shift reading of the read lapse (zeta = 0 at k != 0, PR #9933, not checked here), the laws give no linear split-time fluctuation; the tensors reach it at second order, blue and at most about 2e-21 at r < 0.036. (D) If every rule component is a function of local edge length, the uniform-length slice is the uniform-density slice and split-time spread carries zeta = 0; it becomes zeta = H delta T only through a supplied exit that reads ticks. Not computed: the 3D trigger with all 18 registers, the quantum volume-mode width per block, the second-order constraint that sources the trace from tensors."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_split_time_cascade_is_self_similar_so_its_delta_n_spectrum_is_flat_and_the_trigger_reads_no_linear_scalar_2026_10_22.py
---

# The split-time cascade is self-similar in the toy, so its octave-averaged delta-N index is zero, and the trigger reads no linear scalar

Claim type: bounded_theorem.
Primary runner: `scripts/the_split_time_cascade_is_self_similar_so_its_delta_n_spectrum_is_flat_and_the_trigger_reads_no_linear_scalar_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its predictions sheet lists the scalar index (n_s = 1 exactly against 0.9649 +- 0.0042, about 8 sigma) and the scalar seed (absent against A_s = 2.1e-9) as tensions. The update law's split is a discrete scale-generating process: every block splits once per doubling of its edges, when a register threshold is crossed. This note asks whether the record of when each block split, a delta-N field, gives a curvature perturbation, and with what index and amplitude. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Register arithmetic and what the trigger reads (exact).

1. An edge register's length is its flat length times 2^(n/s - 3). The trigger mean 4s is twice the flat length; the children's value 4s - s = 3s is their own flat length, and two children span the parent edge. A generation is therefore s register steps, ln 2 of log-length, for every s, and the window [0, (4 + Delta)s] holds the whole cycle for every Delta >= 0.
2. Over the 18 edges of a block cube (12 axis edges and the 6 face diagonals of the even corners, the five-tetrahedron cube), the mean log-length is tr h/6 at first order in a strain h. No traceless strain moves the trigger, since the 18 directions have mean e e^T = 1/3.
3. At second order, on a tensor wave along z, the mean log-length moves by -(9 h+^2 + 2 hx^2)/72. The trigger reads tensors quadratically, with a weight that depends on the polarisation.

B. Split cascades.

1. Theorem (narrowed 2026-11-14). Suppose the split-time spread is a sum over levels l in Z, the level-l contribution has a level-independent spatial shape w (in units of the level's block) and variance sig^2 lam^l, the levels are uncorrelated (or their covariances depend only on the level difference and scale the same way), and the level sum converges at k. Then Delta^2(2k) = lam Delta^2(k). This fixes the octave-averaged index exactly: [ln Delta^2(2k) - ln Delta^2(k)]/ln 2 = log2 lam, and self-similar levels give an octave-averaged n_s = 1. It does not fix the local index d ln Delta^2/d ln k: every Delta^2 = k^(log2 lam) f(log2 k) with f positive and of period one obeys the identity. Negative results, computed: the witness f(x) = 1 + 0.1 cos(2 pi x) obeys the identity at lam = 1 to 2e-16, but its local index swings between -0.911 and +0.911; and the runner's own 1D blocky shape w(u) = u sinc^2(u/2) gives, at lam = 1, a local index between -2.51 and +2.75 inside each octave (Delta^2 max/min 1.19), because the shape's zeros at even u line up across levels at k = 2^n. A finite cascade (levels 0 to G) is not exactly self-similar: Delta^2_G(2k) - lam Delta^2_G(k) = w(2k) - lam^(G+1) w(2^-G k), boundary terms up to 0.41 of Delta^2 near the box scale at G = 9. This rederives the cascade item in the register's cosmology work and narrows its "flat spectrum" to the octave average.
2. Toy with the trigger rule (2D block tree, 512^2 finest blocks, block-mean registers), with Poisson stepping of each register supplied to give the trigger a timing spread. In the free trigger (mean reaches 4s, children start at the parent's value minus s), the mean wait is ln 2 e-folds, the wait variance is (ln 2)^2/(m s), and the per-level variance does not depend on the level.
3. In the coupled trigger (+x and +y unsplit neighbours full, held edges block, 2:1 balance), the max-plus coupling raises the wait variance by 1.8. Neighbour waits correlate at +0.32. Parent and child waits anticorrelate at -0.14, because a delayed parent's registers keep rising and the excess passes to its children. The mean wait stays ln 2, since the geometry and not the split sets it. The deep levels are stationary: the effective per-level variance at levels 8 and 9 agrees to 0.9994, against the 0.976 that n_s = 0.965 needs. Held edges bind rarely (0.3% of the ready block-steps); the neighbour-full condition binds 90%.
4. The split-time field is made of sharp blocks. At fixed |k| the power along the axes exceeds the power along the diagonals by about 1.5, a statistical anisotropy on top of the octave-averaged n_s = 1.
5. The e-fold wait Gamma(m s) ln 2/(m s) contains only register numbers (s, and m, the registers the trigger averages). Neither H, eps0 nor the window size enters, so rule-constant s and m give lam = 1 for every expansion history. s = 64 gives the same result.

C. The laws' own channel.

1. At linear order the trigger reads only tr h/6 (A2). Given the stationary-shift reading of the read lapse, cited from the read-lapse note (PR #9933, not found on `main` or this branch, not rerun or checked here), the scalar sector has zeta = 0 at every k != 0. So, conditional on that citation, the laws give no linear split-time fluctuation at k != 0. The runner prints this as a CONDITIONAL line, not a counted check.
2. The quadratic readout of a flat Gaussian field is blue, from the infrared logarithm. On the runner's 64^3 grid (three seeds) n - 1 = +0.72 and Delta^2(h^2)/Delta_h^4 = 6.74. This is a finite example of a blue readout, not a precise exponent (corrected 2026-11-14: the earlier text said +0.3 and about 9, which did not match the cache).

D. When the split-time record is a curvature perturbation.

1. Suppose every rule component is a function of the local edge length: the constant, the sea carried from vacuum to vacuum, and injection at the fixed-length trigger. Then rho = F(a) in every patch, the uniform-length slice is the uniform-density slice, and zeta = delta N(flat to uniform rho) = 0 for any split-time spread.
2. Only a tick-integrating quantity separates the patches, for example the record count, which no law reads. An exit law that read it would give zeta = H delta T per level, that is, the cascade spectrum of B.

## Derivation

A1 is substitution into the length rule. For A2 and A3, ln l = (1/2) ln(1 + x) with x = e^T h e, so the mean over the 18 edges is <x>/2 - <x^2>/4. The six even-corner face diagonals contain each face-diagonal direction once, so their e e^T sum is 2 times 1, and the axis edges give 4 times 1; the mean is 1/3 and the first-order term is tr h/6. For B1, Delta^2(k) = sum_l lam^l sig^2 w(k 2^-l) over all integers l, and the shift l -> l - 1 gives Delta^2(2k) = lam Delta^2(k); over levels 0 to G the same shift leaves the two boundary terms of B1.

For B3, the stationarity follows from self-similarity. Each level repeats the same register problem: children start from their parent's values minus s, the trigger reads a fixed set of registers, and the coupling reads only neighbours at the same level or the next coarser one. Only the top of the cascade breaks the self-similarity, and its effect decays with depth (the per-level ratio is within 1% of 1 by level 7). For C1, the read-lapse note proves zeta = 0 at k != 0 with a stationary shift; A2 then gives delta T = 0 at O(h). For D1, delta-N measures zeta from a flat slice to a uniform-density slice; if rho is a function of a alone, these slices coincide.

## Checks

The runner prints 12 counted checks and exits nonzero if any fails: A1-A3 exact (sympy); B1 exact to 1e-13; B1b (the witness and the blocky local index) and B1c (finite-cascade boundary identity) exact; B2-B5 finite diagnostics, seeded; C2 a finite diagnostic; E1 estimate arithmetic. C1 (conditional on the cited read lapse), D1 and D2 (identities that hold by construction) are printed but not counted; before 2026-11-14 they were counted checks that could not fail.

## Estimates against measurement

- Index. Every split-time channel computed here with rule-constant numbers gives an octave-averaged n_s = 1: 8.4 sigma from Planck and further from ACT. The local index within an octave is not fixed by the cascade and is O(1) log-periodic for the 1D blocky shape (B1). The measured index needs lam = 2^(n_s - 1) = 0.976 per split. In the Poisson model that means the product m s of the registers read and the steps per octave must grow by 2.46% per split, which no rule supplies.
- Amplitude. A_s needs a per-level spread of 3.8e-5 e-folds. In the Poisson model that is m s = ln 2/A_s = 3.3e8, against at most 18 x 113 = 2034 for the rules, so the supplied Poisson model overshoots the amplitude by about 1.6e5. The laws' own channel is zero at linear order. At second order it is at most about 1.5e-21 at r < 0.036, and blue (an estimate: it uses the finite C2 size 6.74 and a supplied log factor of 10). CL-3's only de Sitter phase is today's (P_t of about 5e-122), so in the rules it is zero in practice.
- Isotropy. Sharp blocks give axis-aligned excess power of order 1.5 in the toy.

## Boundary

Supplied: Poisson stepping of each register, used only in B to give the trigger a timing spread (a stochastic model, not a law); one mean register per block, averaging m = 3 in the toy; the 2D block tree; "full" read as a neighbour mean >= 4s; interior child edges at the parent mean minus s; a scalar stand-in for one tensor polarisation in C2; the injection fraction in D1, any value.

Forced, given those: the register arithmetic; the first-order trace readout and the second-order tensor form; Delta^2(2k) = lam Delta^2(k) for an infinite self-similar cascade, hence its octave-averaged index; a mean wait of ln 2 per generation; stationarity of the coupled cascade in the toy; zeta = 0 when rho = F(a).

Not computed: the local (sub-octave) spectrum of the 2D toy and of a 3D trigger; the 3D trigger on all 18 registers with the three neighbour faces; the quantum volume-mode width per block; the second-order constraint that sources the trace from tensors, which could change the coefficient in A3 but not the order; any exit law.

Navigation (2026-11-14): the [Born split-time note](BORN_SPLIT_TIMES_ARE_WHITE_INHERITED_OFFSETS_AND_THE_PASSING_LEAVES_NO_REMAINDER_SO_NO_LAW_SEEDS_CURVATURE_BOUNDED_THEOREM_NOTE_2026-10-22.md) on this branch treats split-time offsets under the fewest-change (quantile) transport as inherited, not redrawn. B2-B5 redraw supplied Poisson steps, so their n_s = 1 and their factor 1.8 rise in wait variance hold for this toy only; the Born note's factor 0.43 fall in split-time spread uses a different model and quantity, and neither note reconciles the two. A1-A3 and B1 are not affected.

Not claimed: that a tilt is impossible. A tilt needs a rule number that changes from one generation to the next (lam = 0.976 to 0.982), or a clock, and that is a named supplied number, not a gap the cascade fills.

## Dependencies

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [candidate_laws](CANDIDATE_LAWS.md)
- Used: the read-lapse note (zeta = 0 at k != 0 with a stationary shift, inhomog-volume #9933); the cascade theorem and the 3.81e-5 per-level spread (cosmology); the reset at fixed local e-fold number (one-cell-start C3); the Born spread of split time (split-creation B5). None of these was found as a file on `main` or this branch; they are recorded only in the consolidation's map ([VACUUM_COSMOLOGY_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md](VACUUM_COSMOLOGY_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md)) and enter as cited inputs.

## How to run

python3 scripts/the_split_time_cascade_is_self_similar_so_its_delta_n_spectrum_is_flat_and_the_trigger_reads_no_linear_scalar_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120; about 13 s, peak about 120 MB; ends with TOTAL: PASS=12 FAIL=0 (13 at the held head, which counted C1, D1 and D2).
