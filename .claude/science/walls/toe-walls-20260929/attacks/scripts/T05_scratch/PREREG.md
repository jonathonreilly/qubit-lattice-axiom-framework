# T05 pre-registration (written 2026-09-29 13:57Z, before any script was run)

Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family check).

## What is being tested

Route R1 claims: on the repository's own formation process (block 01 setting:
six-axis menu, product rule with orbit weights (p,q,r) = (3,1,2), records-only
reading, open window), the axioms' odds are *predictive* probabilities of a
sequential process, so
  (i)   frequencies are calibrated to the predictive odds for every ADAPTED
        formation scheme (random or value-dependent order), with no clustering or
        IID premise;
  (ii)  the same frequencies are NOT calibrated to the static-law conditionals
        computed from the final pattern (the two laws differ, block 01 Theorem B),
        and conversely a static (heat-bath) world is calibrated to the static
        conditionals but not to a post-hoc predictive object with an imposed order;
  (iii) a content-dependent formation hazard (would-be content changes whether the
        site forms) breaks (i) unless the odds are defined as the content law given
        formation.
Route R2 claims: the Born form is free for a positive local law (Rokhsar-Kivelson
parent Hamiltonian): psi = sqrt(mu) is the exact zero-energy state of a local
frustration-free projector Hamiltonian.

## Setting (fixed now)

- Menu values 0..5 = +x,-x,+y,-y,+z,-z. phi(s,t) = 3 if s=t, 1 if s=-t, 2 otherwise.
- Rule: r(s | eta) proportional to prod over recorded neighbours y of phi(s, v_y);
  r(s | empty) = 1/6.
- Window: open 4x4x4 grid (64 sites). M = 30000 histories per world.
- World F: uniform random total order, sequential draws from r.
- World F2: value-dependent ADAPTED order (next site = unrecorded site with most
  recorded +z neighbours, random tie-break); draws from r.
- World S: static law mu(v) proportional to prod over edges phi(v_x, v_y), sampled by
  checkerboard heat-bath, 150 sweeps from a random start.
- World H: as F but the locked content is drawn from h(s) r(s|eta) / normaliser with
  h = (1,1,1,1,2,2) (a content-dependent clock; would-be +-z content forms faster).
- Observer Pred(k): p_t = r(. | neighbours recorded before x_t in the true (or, for S,
  an imposed random) order). Uses all 64 steps of each history.
- Observer Stat: q_x = r(. | ALL window neighbours' final values), on the even-parity
  coding set only (Besag coding: given the odd sites the even sites are independent
  with exactly these laws, so the chi-square below is exact in world S).
- Calibration statistic: for each value s, bins of the predicted probability p(s)
  (greedy merge of sorted distinct values to >= 5% of trials per bin), z_b =
  sum_b (X_s - p_s) / sqrt(sum_b p_s (1 - p_s)); chi2 = sum z_b^2, df = number of
  bins. Report chi2/df pooled over s, max |z|, and ECE = sum_b (n_b/K) |mean X - mean p|.

## Pass / fail readings, fixed in advance

R1 is SUPPORTED on the repo's own object if ALL of:
  (a) F x Pred(true order): pooled chi2/df in [0.6, 1.6] and max|z| < 4.5.
  (a2) F2 x Pred (value-dependent adapted order): same band.
  (b) S x Stat (coding set): pooled chi2/df in [0.6, 1.6] and max|z| < 4.5
      (this also validates the heat-bath sampler).
  (c) F x Stat: pooled chi2/df >= 5.
  (d) S x Pred(imposed random order): pooled chi2/df >= 5.
  (e) H x Pred(r): pooled chi2/df >= 5, while H x Pred(r_h) is in [0.6, 1.6].
R1 is KILLED (or the implementation is wrong; investigate before any claim) if (a),
(a2) or (b) fails.
R1 is WOUNDED in its usefulness if (c) or (d) has chi2/df < 2 at these sizes: the
two candidate laws are then not separable by a scorer at ~10^6 trials, so the
"which law" fork is not empirically resolvable this way.
Anything between the bands is reported as measured, with no verdict.

Also computed, no threshold: the record count N needed for a 4-sigma separation of
F from Stat, from the measured per-trial excess chi2 (excess chi2 per trial x N = 16).

Exact arm C (cat vs product, n = 8, 12; random 6-qubit states): the frequency F of
outcome 0 minus the mean predictive probability D = F - (1/n) sum_t p_t satisfies
Var D <= 1/(4n) for EVERY state (cat and product included). PASS if the exact
variances obey the bound for all cases; FAIL (theorem violated) otherwise.

## Test R2 (parent Hamiltonian), open 2x2x2 cube, static law of the same rule

psi = sqrt(mu), mu proportional to prod over the 12 edges phi(v_x, v_y). A_x = projector
onto the site-x conditional state given its window neighbours. H = sum_x (1 - A_x).
PASS: max_x ||A_x psi - psi||_inf < 1e-12; lowest eigenvalue < 1e-9; second eigenvalue
> 0.05 (unique gapped local frustration-free parent). FAIL: psi not annihilated, or a
degenerate ground space (second eigenvalue < 1e-6).
