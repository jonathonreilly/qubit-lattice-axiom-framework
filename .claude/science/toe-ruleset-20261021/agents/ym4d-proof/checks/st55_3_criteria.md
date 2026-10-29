# st55_3 — pre-registered criteria (written before any st55_3 script exists)

Object: STEP55 §3.5 erratum S4 — the one-step positivity window at the stripe was only bracketed (PD at τ = 1/20, not PD at
τ = 1/10, κ_0 = 1) and its κ_0-scaling was an extrapolation. This check brackets the threshold τ_c(κ_0) on H_red(0) (st55_2's
36-dimensional subspace S_{(0)}, its G_fl-horizontal part) for κ_0 ∈ {1/4, 1, 4}, using st55_2_stripe.py's functions unchanged
(its definitions are executed, its main loop is not), exact arithmetic only.
Grid: τ ∈ {1/80, 1/60, 1/50, 1/40, 1/35, 1/30, 1/25, 1/22, 1/20, 1/18, 1/17, 1/16, 1/15, 1/14, 1/13, 1/12, 1/11, 1/10, 1/9, 1/8,
1/7, 1/6, 1/5, 1/4}; at each τ: is H_cond = H_bare + κ_0H_ker positive definite on H_red(0)?

Predictions (made before running):
- W1 (κ_0 = 1): the answers are monotone along the grid (PD for every τ below some grid value, not PD for every τ above), and the
  last PD grid value τ_+ and first non-PD value τ_− satisfy 1/18 ≤ τ_+ < τ_− ≤ 1/14 (my estimate τ_c ≈ 0.059 from st55_2's certified
  margins).
- W2 (κ_0 = 4): monotone; τ_c(4)/τ_c(1) ∈ [1.4, 2.6], judged on the bracket midpoints (√κ_0 scaling would give 2).
- W3 (κ_0 = 1/4): monotone; τ_c(1/4)/τ_c(1) ∈ [0.35, 0.65] on the bracket midpoints.
- Controls: C1 at τ = 0, H_cond PD for all three κ_0 (the one-step gap 2κ_0/9); C2 at τ = 1/4, H_cond NOT PD for κ_0 ∈ {1/4, 1}.
PASS: W1, W2, W3 and both controls as predicted. A failed prediction is reported as such (with the observed brackets); it does
not change st55_2's certified facts, only the interpolation/extrapolation statement of STEP55 erratum S4.
