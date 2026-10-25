---
claim_id: the_one_family_u1_anomaly_at_wilson_mass_one_passes_luschers_kernel_locality_tests_but_its_small_momentum_four_field_coefficient_does_not_visibly_vanish_bounded_theorem_note_2026-10-25
claim_type: bounded_theorem
claim_scope: "Pre-registered rerun at Wilson mass m0 = 1.0 (control m0 = 0.6) of the momentum-space Luscher locality test for the U(1)_Y covariant anomaly density of the Wilson-kernel overlap (r = 1): the one-family 16 and a lone L doublet, axis-restricted factorised backgrounds, L x T x L x T lattices with L = 6..24 along x1, x3 and T = 24 (16 for L = 24) along x2, x4, exact block sign(H). Exact: block = full 4D density on 4^4 (7e-15); GW per block. Finite diagnostics, pre-set criteria: per-charge order-2 kernel and its Luscher-split currents exponentially local with an L-independent length (xi 0.49-0.53; K1 0.53/0.57), zero-momentum value within 0.5% for L >= 10, doublet keeps a non-decaying current tail = |gamma_L| (within 10% on all L, 2% only for L >= 10) and its single-mode intercept 0.990 gamma_L. NOT met: the 16's single-mode coefficient criteria P5, P5', P5b and the T = 16 volume check; R16 is at most 1e-4 |gamma_L| for s <= 0.07 but changes sign, and the post-hoc two-eps split shows the leading (density order eps^4) coefficient c4 = 1.3-1.4e-4 at s = 0.038 and 0.017, flat rather than tending to zero. Control m0 = 0.6: the pre-set slow-scale reading min(m0, 2 - m0) is NOT met. Not covered: the measure, non-abelian locality, the gauge-field integral, non-axis backgrounds, momenta below |p_hat| = 0.26, T-convergence of the L = 24 points."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_one_family_u1_anomaly_passes_luschers_zero_momentum_tests_on_lattices_to_24_but_its_momentum_space_locality_test_is_scale_limited_at_m0_1p6_bounded_theorem_note_2026-10-24
  - the_u1_hypercharge_anomaly_of_the_one_family_overlap_passes_luschers_zero_momentum_condition_but_finite_range_current_fits_on_4_to_the_4_cannot_test_locality_bounded_theorem_note_2026-10-24
  - the_overlap_chiral_determinant_in_su2_x_u1_backgrounds_cancels_the_family_gauge_anomaly_through_cubic_order_and_in_every_measured_index_but_a_single_doublet_does_not_bounded_theorem_note_2026-10-23
runner: scripts/the_one_family_u1_anomaly_at_wilson_mass_one_passes_luschers_kernel_locality_tests_but_its_small_momentum_four_field_coefficient_does_not_visibly_vanish_2026_10_25.py
---

# The one-family U(1) anomaly at Wilson mass 1 passes Luscher's kernel locality tests, but its small-momentum four-field coefficient does not visibly vanish

Claim type: bounded_theorem (exact lattice identities, pre-registered finite diagnostics, labelled post-hoc
analyses). Labels: [T] exact, [F] finite diagnostic, [S] reading. Runner: runner.py, TOTAL: PASS=19 FAIL=0, 75 s
on the laptop, peak RSS 131 MB, 5.6 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120, no data files read
(Mac-mini results are an embedded JSON literal). Tested under a unique filename (scratch
luscher_m0_1_test_run.py, exit 0). Each pre-set criterion prints MET or NOT MET; the runner line certifies that the
recorded verdict reproduces from the data, so a PASS line can carry a NOT MET verdict. Axioms unchanged; no rule
proposed; no CL edit.

## Pre-registration

- criteria_pre_run.txt was written before any computation of this probe. It copies luscher-L8's P1-P6 (only m0
  changed), adds the task-stated thresholds as primed variants (P1', P4', P5'), a volume check V, and controls
  C1, C2 at m0 = 0.6.
- Disclosed prior knowledge: luscher-L8's post-hoc m0 = 1.0 numbers had been seen. No m0 = 0.6 number had been seen.
- One fit-range rule was declared in advance, because the m0 = 1.0 kernel decays faster: fits run over
  d = 2..d_max, with the envelope at least 30 x the numerical floor. K3's last point is capped at L/2 - 2, which is
  L8's construction finding.
- The L = 24 extent rule was also pre-set: a 2304-dim eigh took 6.7 s against the 6 s threshold, so T = 16.
- One cost addendum (03:20, before any result file existed) dropped 7 L = 16 single-mode points and one m0 = 0.6
  point. Under nice 10 the jobs ran on efficiency cores, about 2.9x slower. No threshold changed.

## Set-up

- The machinery is copied from luscher-L8 (runner functions, unchanged except M0): H = g5 (D_W - m0),
  q_Y = tr sign H_Y(x,x) by exact per-(p2,p4) block eigh, axis-restricted backgrounds, M1 (order-2 kernel, seed
  1000+L, Richardson) and M2 (single mode, eps = 0.3; R = 4 x Fourier coefficient / eps^2).
- Mac mini: 50 jobs, 4 single-thread workers at nice 10, about 12 h wall; peak about 1 GB per job.
- Post-hoc additions:
  - (24,1,1) at T = 8;
  - (24,1,1) at eps = 0.15 (block-split over 3 workers; the split was validated against (8,1,1) to 1e-14).
- Live re-checks in the runner: m0 = 1.0 and 0.6 kernels on 6 x 24 x 6 x 24 match the mini to 2e-13. The
  (8,1,1) single-mode values match the mini and luscher-L8's embedded m0 = 1.0 values to 3e-14.

## Results against the pre-set criteria (m0 = 1.0)

| criterion | outcome | numbers |
|---|---|---|
| P0 exactness | MET | block = full 4D 7e-15; GW 4e-15 |
| P1 kernel xi L-independent within 10%; common momentum <= 1e-3 gamma | MET | xi 0.490, 0.503, 0.529 (spread 7.7%); 1.3e-5 gamma |
| P1' current kernel K1 xi at L = 12, 16 within 20% | MET | 0.525, 0.568 |
| P2 sum Q within 1% for L >= 10 | MET | -0.43, -0.105, -0.006 % |
| P3 current tails < 1e-3 gamma; xi(K1), xi(K3) within 15% | MET | tail 3e-6 gamma; 0.568, 0.570 vs 0.529 |
| P4 doublet tail = abs(gamma_L) within 2% on EVERY L = 6..16 | NOT MET | -7.95% (L6), -1.83% (L8), then -0.43 ... -0.01% |
| P4' same within 10% | MET | max 7.95% |
| P4b doublet single-mode intercept within 3% | MET | 0.9897 gamma_L (33 points) |
| P5 R16 intercept small and abs(p)-exponent in [1.6, 2.4] | NOT MET | intercept 3.1e-5 (> 0.05 max R16 = 7.3e-6); exponent 5.79 |
| P5' L = 24: one sign and exponent >= 1.8 | NOT MET | R16 = +1.35e-6, -9.00e-6, -4.44e-5 (sign change) |
| P5b eps^4 scaling within 0.3 | NOT MET | eps = 0.3 / 0.15 opposite signs at (12,1,1), (16,1,1); 4.33 at (16,2,2) |
| P6 finite size, R16(12,3,3) vs (16,4,4) | MET | 5.2e-4 of max R16 |
| V T = 16 vs 32 and holonomy shift within max(10%, 1e-5 abs(gamma_L)) | NOT MET (T part) | T16 -7.06e-7, T24 -9.032e-7, T32 -9.031e-7; shift -9.026e-7 (met) |

Control m0 = 0.6:
- C1 is NOT MET. The pre-set reading predicted mu(0.6) in [0.353, 0.530] with mu(1.6) < mu(0.6) < mu(1.0). The
  measured values are mu(1.6) 0.298, mu(0.6) 0.768, mu(1.0) 0.716.
- C2 is MET: xi_16 ordering 0.529 (m0 1.0) < 0.562 (0.6) < 0.914 (1.6).

## Post-hoc analyses (labelled; not criteria)

- H1 [F]: split R16 = c4 eps^2 + c6 eps^4 using eps = 0.3 and 0.15. Here c4 is the leading term, density order
  eps^4, weight sum m Y^5 = 0.556.

  | s | L | c4 | c6 |
  |---|---|---|---|
  | 0.017 | 24 (T = 16) | +1.42e-4 | -1.41e-3 |
  | 0.038 | 16 | +1.28e-4 | -1.53e-3 |
  | 0.067 | 12 | +4.8e-5 | -1.71e-3 |
  | 0.146 | 16 | -3.6e-4 | -1.48e-3 |

  - At s <= 0.038, c6 eps^2 cancels c4 to 10% at eps = 0.3. That cancellation is why R16 is tiny there and changes
    sign.
  - So luscher-L8's post-hoc m0 = 1.0 statement ("falls faster than p^2", exponent 5.8) was an eps-order
    cancellation, not a p^2 regime. This note CORRECTS that reading.
  - The leading coefficient c4 flattens near 1.4e-4 (about 1.1% of abs(gamma_L) in R units at eps = 1) at the two
    smallest momenta, instead of tending to zero.
- H2 [F]: x2/x4 extent.
  - At L = 24, T = 8 gives R16 = +1.98e-4, against +1.35e-6 at T = 16. That is the Polyakov-loop artefact found by
    L8.
  - At L = 16, T = 24 and 32 agree to 7e-11, while T = 16 is off by 2e-7 (the V failure). The L = 24 points
    (T = 16) therefore carry an offset of order 1e-7, which is not quantified.
  - The L = 16, s = 0.038 c4 value uses T = 24 data and is T-converged at eps = 0.3.
- H3 [F] control reading. The zero-momentum finite-size rate of sum Q is about 0.72/site at m0 = 1.0 (0.72, 0.71,
  0.72 over L pairs 8-10, 10-12, 12-16) and 0.75-0.83 at m0 = 0.6, against 0.30 at m0 = 1.6. Both "min(m0, 2 - m0)"
  (pre-set C1) and plain "2 - m0" fail quantitatively. [S] The rate drops only when the doubler-side gap 2 - m0 is
  small, and saturates near 0.75 otherwise. The kernel decay lengths (C2) do follow the min-gap ordering.

## Answer

| question | answer |
|---|---|
| per-charge order-2 kernel and Luscher-split currents local, L-independent at m0 = 1.0? | yes (P1, P1', P2, P3 MET; xi ~ 0.5) |
| lone doublet fails Luscher's condition? | yes: non-decaying current tail = abs(gamma_L), single-mode intercept 0.99 gamma_L (P4 only misses the 2% bound on L = 6, 8) |
| does the 16's density vanish like p_mu j_mu (j analytic) at small momentum? | NOT demonstrated. At eps = 0.3, R16 <= 1e-4 abs(gamma_L) for s <= 0.07, but the pre-set exponent and eps-scaling criteria fail. The leading four-field coefficient c4 stays at 1.3-1.4e-4 down to abs(p_hat) = 0.26 |
| is the m0 = 1.6 slow scale min(m0, 2 - m0)? | no (C1 NOT MET); the finite-size rate is about 0.75 at m0 = 0.6 and 1.0 |

[S] Why c4 matters:
- For constant fields the 16's density is exactly zero at every order: Luscher's T is exactly bilinear, and
  sum m Y^3 = 0.
- A local current therefore forces c4(s) -> 0 as s -> 0.
- c4 staying at 1.4e-4 down to s = 0.017 means one of three things:
  - (a) a turnover below abs(p_hat) = 0.26. That is a scale of about 4 sites, 8x the kernel decay length 0.53, so the
    order-2 kernel does not explain it;
  - (b) a finite x2/x4-extent effect at order eps^4. The background vanishes along lines where massless modes
    propagate, and T = 16-24 is the only extent tested at L = 24;
  - (c) a genuine non-local piece.
- Perturbative locality of the abelian overlap anomaly (supplied, all orders) argues against (c). This probe cannot
  separate (a) from (b).

## What this establishes, and what remains

- Establishes:
  - [T] the exact block method at m0 = 1.0;
  - [F] at m0 = 1.0, the pre-registered kernel-locality criteria (P1, P1', P2, P3) and the doublet-failure criteria
    (P4', P4b) pass;
  - [F] the 16's single-mode criteria do NOT pass;
  - [F] the post-hoc eps split, which corrects L8's m0 = 1.0 reading;
  - [F] the control falsifies the min(m0, 2 - m0) slow-scale reading.
- Next tests, so that route A's locality premise is decided by measurement rather than read:
  - (i) c4 at L = 24 with T = 24 and 32;
  - (ii) a third eps value (0.075) at s = 0.017 and 0.038, to fix c4 independently of c6 and c8;
  - (iii) L = 32 (s = 0.0096) at T >= 24.
  - (i) and (ii) cost about 1-2 days of single-thread mini time; a block-split cuts that about 3x.

## Smuggling review

- Supplied:
  - U(1)_Y and the 16's hypercharges (test inputs; as rule content they would fail gate criterion 2);
  - the kernel and m0 = 1.0 / 0.6 (kernel parameters, not measured numbers);
  - the axis-restricted backgrounds, eps, T and the fit rules (pre-set);
  - Luscher's theorem and T normalisation.
- Forced: GW, sum m Y^3 = 0, the constant-field zero, and the exact zeros at p = pi.
- Post-hoc (labelled): H1-H3, the T = 8 and eps = 0.15 L = 24 runs, and the [S] readings.
- Gate: N/A (no rule).
- Route A stays open: its U(1) zero-momentum premise is measured; its locality premise is supported for the per-charge
  kernel and NOT yet for the 16's four-field term.

Uses: luscher-L8 (machinery, criteria, Polyakov-loop fix and its post-hoc m0 = 1.0 data, now corrected),
luscher-local-current (conventions), overlap-nonabelian (kernel).
Narrows: luscher-L8's post-hoc "at m0 = 1.0 the 16's coefficient falls faster than p^2 ... consistent with d* of a
local current", which is an eps-order cancellation at eps = 0.3, and its slow-scale reading "2 - m0" (the rate is
not set by min(m0, 2 - m0) either).
Caveats: U(1) only; finite lattices; axis-restricted backgrounds with eps = 0.3 / 0.15, above Luscher's
admissibility bound; not the non-abelian measure; not the gauge-field integral.
