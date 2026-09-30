# T58 pre-registration (written before any T58 script was run)

Attacker: Claude Sonnet 5.5. Wall: T58 (L12-W6, L13-W7, L13-W8). All checks same-family, unrefereed.

## Question the test decides

T58 says "eta is imported; leptogenesis and its CP sign are not derived". The lane
blames (a) one phenomenological import g_weak = 0.653 for the size of eta, and (b) a
free one-bit CP sheet for its sign. The test asks which supplied inputs actually
carry the size and the sign of the lane's own chain (scripts/dm_leptogenesis_exact_common.py,
read-only import, no repo file written), so the wall can be priced against the right sibling.

## Script: t58_chain_test.py (own re-implementation, cross-checked against the repo helper)

### S0 reproduction
PASS: my re-implementation reproduces eta/eta_obs = 0.188785929502 (cache of
frontier_dm_leptogenesis_transport_status.txt) to relative 1e-6.
FAIL: any larger mismatch => the wall is misstated numerically; stop and report.

### S1 log-sensitivities d ln(eta) / d ln(p), finite difference +-1 %
Hypotheses (H-size) for the strong-washout chain (K ~ 47):
 - g_weak: |d ln eta / d ln g_weak| < 1.0 (naive power counting says 4). PASS = the
   "isolated import" is NOT what carries the size. FAIL (>= 1.0) = the import does carry it.
 - M1 scale (M1, M2, M3 all scaled, x-ratios fixed): d ln eta / d ln M1 in [0.6, 1.1]. PASS = the
   size is carried by the heavy-Majorana scale (neutrino lane, T50), not by Y0.
 - CP source amplitude gamma: exactly 1.000 (+-0.001).
 - N1-N2 splitting eps/B: in [-1.2, -0.6].
 - g_star: in [-0.9, -0.3].

### S2 cost to reach eta/eta_obs = 1, one supplied input at a time
Reported as factors. Reading: if g_weak alone would need a factor > 3 (or no root below 20),
the shortfall is not a coupling tweak.

### S3 ladder k_B in {6..10} (k_A = k_B - 1)
PASS for "size is a ladder-rung consequence": eta/eta_obs(k_B = 7) in [1, 4] and (k_B = 9) in [0.01, 0.05];
and m3 = Y0^2 v^2 / M1 hits 0.05 eV only at k_B = 8. FAIL = neighbouring rungs give eta near 1 too.

### S4 sign structure
Compute the raw (signed) epsilon_1 = (1/8pi) Y0^2 (cp1 f(x23) + cp2 f(x3))/K00 for all eight sign
patterns of (gamma, E1, E2), before the repo's abs(). Compute the PMNS sin(delta_CP) on the L10
chart for gamma = +-1/2 (read-only reuse of walls/L10_scratch/gamma_flip_check.py).
Hypotheses:
 - (H-sign-1) the repo's chain never computes the physical sign of eta: abs() sits in exact_package
   (epsilon_1) and in kappa_axiom_reference (direct). PASS = confirmed by source read.
 - (H-sign-2) gamma -> -gamma flips the raw sign of epsilon_1 and sin(delta_CP) together, so the
   chain fixes the correlation sign(eps_raw) * sign(sin delta_CP) = +1 for the constructive-sign
   (E1, E2 > 0) family. PASS = product +1 in every sampled point; FAIL = product changes sign
   inside the chamber (then the correlation is not fixed by the chain).

## What each outcome would mean
- H-size passes (g_weak weak, M1 strong): the size half of T58 is priced at the heavy-Majorana
  scale (T50/T49), not at a coupling import.
- H-sign-2 passes: the sign half is the same bit as T53 (PMNS sheet), and its content is a
  cross-sector correlation, not an unsourced absolute sign.
- Either fails: report and revise the route table.
