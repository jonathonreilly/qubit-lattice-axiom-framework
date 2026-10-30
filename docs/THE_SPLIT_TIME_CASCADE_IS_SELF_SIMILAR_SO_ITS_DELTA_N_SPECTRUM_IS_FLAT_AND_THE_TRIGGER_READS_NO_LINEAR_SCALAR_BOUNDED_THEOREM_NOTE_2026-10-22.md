---
claim_id: the_split_time_cascade_is_self_similar_so_its_delta_n_spectrum_is_flat_and_the_trigger_reads_no_linear_scalar_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's glued split (a block splits when the mean of its cube's edge registers reaches 4s, its children's edges along parent edges take the parent's value minus s, held edges block a child, and the trigger needs each unsplit +x, +y, +z face neighbour's shared edges full): (A) exact register arithmetic: a generation is s register steps, ln 2 of log-length, for every s; over the 18 edges of a five-tetrahedron block cube the trigger's mean log-length is tr h/6 at first order, so no traceless strain moves it, and on a tensor wave along z it is -(9 h+^2 + 2 hx^2)/72 at second order. (B) A cascade whose level-l split-time spread has a level-independent shape and variance sig^2 lam^l has Delta^2(2k) = lam Delta^2(k), so n_s - 1 = log2 lam. In a 2D block-tree toy that keeps the trigger rule, with Poisson stepping of each register supplied to give the trigger a timing spread, the mean wait per generation stays ln 2 e-folds, the coupled (max-plus) trigger raises the wait variance by 1.8 and correlates waits (neighbours +0.32, parent-child -0.14), and the deep levels are stationary (deepest per-level ratio 0.9994 against the 0.976 that n_s = 0.965 needs); the per-level spread (ln 2)^2/(m s) contains only register numbers, so s and the window set the amplitude, never the tilt. (C) With the stationary-shift reading of the read lapse (zeta = 0 at k != 0), the laws give no linear split-time fluctuation; the tensors reach it at second order, blue and at most about 2e-21 at r < 0.036. (D) If every rule component is a function of local edge length, the uniform-length slice is the uniform-density slice and split-time spread carries zeta = 0; it becomes zeta = H delta T only through a supplied exit that reads ticks. Not computed: the 3D trigger with all 18 registers, the quantum volume-mode width per block, the second-order constraint that sources the trace from tensors."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_split_time_cascade_is_self_similar_so_its_delta_n_spectrum_is_flat_and_the_trigger_reads_no_linear_scalar_2026_10_22.py
---

# The split-time cascade is self-similar, so its delta-N spectrum is flat, and the trigger reads no linear scalar

Claim type: bounded_theorem.
Primary runner: `scripts/the_split_time_cascade_is_self_similar_so_its_delta_n_spectrum_is_flat_and_the_trigger_reads_no_linear_scalar_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its predictions sheet lists the scalar index (n_s = 1 exactly against 0.9649 +- 0.0042, about 8 sigma) and the scalar seed (absent against A_s = 2.1e-9) as tensions. The update law's split is a discrete scale-generating process: every block splits once per doubling of its edges, when a register threshold is crossed. This note asks whether the record of when each block split, a delta-N field, gives a curvature perturbation, and with what index and amplitude. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Register arithmetic and what the trigger reads (exact).

1. An edge register's length is its flat length times 2^(n/s - 3). The trigger mean 4s is twice the flat length; the children's value 4s - s = 3s is their own flat length, and two children span the parent edge. A generation is therefore s register steps, ln 2 of log-length, for every s, and the window [0, (4 + Delta)s] holds the whole cycle for every Delta >= 0.
2. Over the 18 edges of a block cube (12 axis edges and the 6 face diagonals of the even corners, the five-tetrahedron cube), the mean log-length is tr h/6 at first order in a strain h. No traceless strain moves the trigger, since the 18 directions have mean e e^T = 1/3.
3. At second order, on a tensor wave along z, the mean log-length moves by -(9 h+^2 + 2 hx^2)/72. The trigger reads tensors quadratically, with a weight that depends on the polarisation.

B. Split cascades.

1. Theorem. If the split-time spread contributed at level l has a level-independent spatial shape (in units of the level's block) and variance sig^2 lam^l, then Delta^2(2k) = lam Delta^2(k), so n_s - 1 = log2 lam exactly. Self-similar levels give n_s = 1. This rederives the cascade item in the register's cosmology work.
2. Toy with the trigger rule (2D block tree, 512^2 finest blocks, block-mean registers), with Poisson stepping of each register supplied to give the trigger a timing spread. In the free trigger (mean reaches 4s, children start at the parent's value minus s), the mean wait is ln 2 e-folds, the wait variance is (ln 2)^2/(m s), and the per-level variance does not depend on the level.
3. In the coupled trigger (+x and +y unsplit neighbours full, held edges block, 2:1 balance), the max-plus coupling raises the wait variance by 1.8. Neighbour waits correlate at +0.32. Parent and child waits anticorrelate at -0.14, because a delayed parent's registers keep rising and the excess passes to its children. The mean wait stays ln 2, since the geometry and not the split sets it. The deep levels are stationary: the effective per-level variance at levels 8 and 9 agrees to 0.9994, against the 0.976 that n_s = 0.965 needs. Held edges bind rarely (0.3% of the ready block-steps); the neighbour-full condition binds 90%.
4. The split-time field is made of sharp blocks. At fixed |k| the power along the axes exceeds the power along the diagonals by about 1.5, a statistical anisotropy on top of n_s = 1.
5. The e-fold wait Gamma(m s) ln 2/(m s) contains only register numbers (s, and m, the registers the trigger averages). Neither H, eps0 nor the window size enters, so rule-constant s and m give lam = 1 for every expansion history. s = 64 gives the same result.

C. The laws' own channel.

1. At linear order the trigger reads only tr h/6 (A2). With the stationary-shift reading of the read lapse, the scalar sector has zeta = 0 at every k != 0. So the laws give no linear split-time fluctuation at k != 0.
2. The quadratic readout of a flat Gaussian field is blue (n - 1 of about +0.3 on a 64^3 grid, from the infrared logarithm) and of size about 9 Delta_h^4.

D. When the split-time record is a curvature perturbation.

1. Suppose every rule component is a function of the local edge length: the constant, the sea carried from vacuum to vacuum, and injection at the fixed-length trigger. Then rho = F(a) in every patch, the uniform-length slice is the uniform-density slice, and zeta = delta N(flat to uniform rho) = 0 for any split-time spread.
2. Only a tick-integrating quantity separates the patches, for example the record count, which no law reads. An exit law that read it would give zeta = H delta T per level, that is, the cascade spectrum of B.

## Derivation

A1 is substitution into the length rule. For A2 and A3, ln l = (1/2) ln(1 + x) with x = e^T h e, so the mean over the 18 edges is <x>/2 - <x^2>/4. The six even-corner face diagonals contain each face-diagonal direction once, so their e e^T sum is 2 times 1, and the axis edges give 4 times 1; the mean is 1/3 and the first-order term is tr h/6. For B1, Delta^2(k) = sum_l lam^l sig^2 w(k 2^-l), and the shift l -> l - 1 gives Delta^2(2k) = lam Delta^2(k).

For B3, the stationarity follows from self-similarity. Each level repeats the same register problem: children start from their parent's values minus s, the trigger reads a fixed set of registers, and the coupling reads only neighbours at the same level or the next coarser one. Only the top of the cascade breaks the self-similarity, and its effect decays with depth (the per-level ratio is within 1% of 1 by level 7). For C1, the read-lapse note proves zeta = 0 at k != 0 with a stationary shift; A2 then gives delta T = 0 at O(h). For D1, delta-N measures zeta from a flat slice to a uniform-density slice; if rho is a function of a alone, these slices coincide.

## Checks

The runner prints 13 checks: A1-A3 exact (sympy); B1 exact to 1e-13; B2-B5 finite diagnostics, seeded; C1 exact (with the read-lapse note); C2 a finite diagnostic; D1-D2 exact toy arithmetic; E1 estimate arithmetic.

## Estimates against measurement

- Index. Every split-time channel with rule-constant numbers gives n_s = 1: 8.4 sigma from Planck and further from ACT. The measured index needs lam = 2^(n_s - 1) = 0.976 per split. In the Poisson model that means the product m s of the registers read and the steps per octave must grow by 2.46% per split, which no rule supplies.
- Amplitude. A_s needs a per-level spread of 3.8e-5 e-folds. In the Poisson model that is m s = ln 2/A_s = 3.3e8, against at most 18 x 113 = 2034 for the rules, so the supplied Poisson model overshoots the amplitude by about 1.6e5. The laws' own channel is zero at linear order. At second order it is at most about 2e-21 at r < 0.036, and blue. CL-3's only de Sitter phase is today's (P_t of about 5e-122), so in the rules it is zero in practice.
- Isotropy. Sharp blocks give axis-aligned excess power of order 1.5 in the toy.

## Boundary

Supplied: Poisson stepping of each register, used only in B to give the trigger a timing spread (a stochastic model, not a law); one mean register per block, averaging m = 3 in the toy; the 2D block tree; "full" read as a neighbour mean >= 4s; interior child edges at the parent mean minus s; a scalar stand-in for one tensor polarisation in C2; the injection fraction in D1, any value.

Forced, given those: the register arithmetic; the first-order trace readout and the second-order tensor form; Delta^2(2k) = lam Delta^2(k); a mean wait of ln 2 per generation; stationarity of the coupled cascade in the toy; zeta = 0 when rho = F(a).

Not computed: the 3D trigger on all 18 registers with the three neighbour faces; the quantum volume-mode width per block; the second-order constraint that sources the trace from tensors, which could change the coefficient in A3 but not the order; any exit law.

Not claimed: that a tilt is impossible. A tilt needs a rule number that changes from one generation to the next (lam = 0.976 to 0.982), or a clock, and that is a named supplied number, not a gap the cascade fills.

## Dependencies

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [candidate_laws](CANDIDATE_LAWS.md)
- Used: the read-lapse note (zeta = 0 at k != 0 with a stationary shift, inhomog-volume #9933); the cascade theorem and the 3.81e-5 per-level spread (cosmology); the reset at fixed local e-fold number (one-cell-start C3); the Born spread of split time (split-creation B5).

## How to run

python3 scripts/the_split_time_cascade_is_self_similar_so_its_delta_n_spectrum_is_flat_and_the_trigger_reads_no_linear_scalar_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120; about 10 s, peak about 120 MB; ends with TOTAL: PASS=13 FAIL=0.
