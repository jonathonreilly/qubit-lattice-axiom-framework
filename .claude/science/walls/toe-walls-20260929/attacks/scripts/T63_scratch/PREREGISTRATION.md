# T63 pre-registration (written before any T63 script was run)

Wall: T63 = L13-W9, "Inflation and the primordial spectrum are asserted, not derived".
Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family checks).

Working hypotheses to be attacked by the tests:
 H1  The companion runner (scripts/frontier_primordial_spectrum_dim_scan.py) is not evidence about
     graph growth: it draws every node position i.i.d. uniform (a Poisson process) and never uses
     the edges, so its "tilt" is a property of the seed-lattice clump plus white noise.
 H2  Record patterns made by the landed local rules (crowding, arrival next to existing records)
     have an analytic small-k structure factor S(k) = S0 + S2 k^2 (exponent 0 or 2), never the
     non-analytic k^alpha with alpha ~ 0.965 that a Harrison-Zeldovich matter field has.
 H3  On the fixed Z^3 with one light cone (c = 1 site per tick) the causal-patch site count obeys
     N(t) <= (2t+1)^3, so ln-growth of N is at most logarithmic in t, so 60 e-folds of
     a = N^(1/3) cannot happen in the ticks that an inflation epoch has, and the horizon-exit
     mechanism of the note (comoving Hubble radius shrinking) is unavailable.
 H4  The note's amplitude/e-fold arithmetic is internally inconsistent (A_s, r, 10^78 vs 10^183).

## Test A (runner audit, t63_runner_audit.py)
 A0 reproduce the registered numbers (d=3: n_s = -0.165 +- 0.313 at N_e,graph = 1.386).
 A1 static check: the adjacency dict is never read by the density/spectrum/fit code.
 A2 control with NO seed clump: all final nodes i.i.d. uniform in the final box; same binning, same fit.
 A3 vary the growth factor (N_e,graph = ln f): formula (*) predicts n_s that moves as 1-2/N_e;
    measure whether the runner's n_s follows it.
 PASS-for-lane (runner is evidence): control A2 gives the same n_s as the runner within 1 sigma AND
   the runner's n_s tracks (*) as N_e moves (all |z| < 2 over f = 2,3,4,8).
 FAIL-for-lane (my prediction): A2 differs from the runner by > 3 sigma, or A3 departs from (*) by
   > 3 sigma at two or more values of f.

## Test B (record-pattern structure factors, t63_spectra.py)
 3D periodic L = 48 and 64, >= 16 seeds. Patterns: Bernoulli(0.25) control; random-order frozen
 crowding rules A = {0..m}, m = 0,1,2,3 (the landed T62/probe-19 rules); Eden-type arrival
 (records form only next to an existing record) from a sparse random seed set, read at fill 0.15,
 0.30, 0.60; chessboard control (crystal).
 Measure S(k) = <|rho_hat(k)|^2>/N in integer shells n = |k| L / 2pi = 1..6, fit
   (i) power law A k^alpha,  (ii) analytic S0 + S2 k^2.
 PASS-for-lane: some non-crystal pattern has a power-law alpha in [0.7, 1.3] at both sizes AND the
   power law beats the analytic fit by Delta chi^2 > 9.
 FAIL-for-lane (my prediction): every disordered pattern has the analytic form within errors
   (alpha_eff between 0 and 2, no preference for a non-integer power law); alpha_eff ~ 0 for the
   random-order rules (S(0) finite, like T62 s ~ 3).

## Test C (cone bound on growth, t63_cone_bound.py)
 C1 simulate maximal cone-limited growth (Eden with attach probability 1, then q<1) in 3D from one
    seed and from n0 seeds; record N(t). Check N(t) <= (2t+1)^3 and H_eff t = (1/3)(dlnN/dlnt) <= 1.
 C2 e-fold budget: N_e^max(t) = ln(2t+1). For inflation lasting N_e/H ticks, the largest N_e
    compatible with the bound at each H a.  Find H a for which N_e = 60 is allowed.
 PASS-for-lane: some H a in the range allowed by A_s = 2.1e-9 and r < 0.036 admits 60 e-folds.
 FAIL-for-lane (prediction): N_e^max <= ~20 for every allowed H a; 60 e-folds needs H a <~ 1e-24.

## Test D (arithmetic of the note, t63_arith.py)
 D1 n_s and sigma for N_e = 60, 56.98, (1/3) ln 10^183 = 140.5.
 D2 Poisson-cell amplitude A_s = (H a)^3 vs 2.1e-9, and r from GR tensors at that H (a = 1/M_Pl).
 D3 Poisson-only tilt -d/N_e vs the note's formula; size of the added term at d = 3.

What each result would change:
 A FAIL + B FAIL + C FAIL -> the note's growth mechanism is not evidence and not available inside the
   axioms; the spectrum (tilt, amplitude, superhorizon correlation) is realized-state data at best
   => PRICED (to realized_state_primitive / T16 past hypothesis), unless a route gives non-analytic S(k).
 B PASS -> route survives (wounded): a local mechanism with a non-integer small-k exponent exists;
   then the mapping to n_s and the tuning of the control parameter become the obligations.

## Addendum B2 (written AFTER the first L=32 conserved-hop scan; disclosed)
The first CLG scan (t63_clg_output.txt, t63_clg_near_output.txt; L=32, 8 seeds) gave alpha_eff = -0.44, -0.18, +0.28
at rho = 0.19, 0.20, 0.21 (absorbing states; active phase from about 0.22). So the outside route "conserved
local hop dynamics near its absorbing-state critical density gives suppressed large-scale fluctuations"
was NOT pre-registered as a prediction of failure at rho = 0.21; it is now tested on NEW runs:
 B2 test: L = 32 (16 seeds) and L = 48 (8 seeds), rho in {0.205, 0.21, 0.215, 0.22}, up to 15000 sweeps,
   S(k) shells n = 1..4, alpha_eff from the power-law fit.
 PASS (route survives, wounded): at the density with the smallest S(n=1)/S(n=4) alpha_eff lies in [0.7, 1.3]
   at both sizes, i.e. a non-integer power law near the HZ exponent 0.965 with no N_e input.
 FAIL: alpha_eff <= 0.5 at both sizes (non-analytic at best, but the wrong exponent), or no non-monotone
   trend with L.  Prediction (from the literature, not from my runs): alpha < 1 (it is a universality-class
   number, not adjustable), so FAIL.
