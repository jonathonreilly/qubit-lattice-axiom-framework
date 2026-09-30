# T30 pre-registration (written before running t30_flow.py)

Question tested: is a *perturbative* (1-, 2-, 3-loop) SU(3) flow from the framework's cutoff
coupling alpha_LM = 0.0907 at M_Pl (Planck lattice, g_bare = 1) to v = 246 GeV determined and
controlled once the framework's own content is fixed (16 tastes at the cutoff, taste
staircase of the YT_P2 notes)? Inputs used are only the repo's numbers: alpha_bare = 1/(4pi),
u0 = 0.8777, alpha_LM = 0.09067, L = ln(M_Pl/v) = 38.44, targets alpha_s(v) = 0.1033
(and g ratio 1.132 => alpha(v)/alpha(M_Pl) = 1.281, i.e. alpha(v) = 0.1162 if started from
alpha_LM), b_k = SU(3) MSbar coefficients with n_taste in place of n_f (as the repo does).
Scheme conversion lattice -> MSbar is NOT applied (same as the repo); flagged as uncontrolled.

## Blocks
A. Constant content n = 0..16, 2- and 3-loop: IR fate (Landau pole at alpha=alpha_max, conformal
   fixed point, or reaches v), ln(M_Pl/Lambda) if it diverges.
B. Repo staircase mu_k = M_Pl * alpha_LM^k, n = 16-k, 1/2/3 loops: does it reach v? alpha at
   the last rung? Ratio of successive-loop shifts (control indicator).
C. Existence/determinacy: one-threshold family (n=16 above mu_1, n=n_low below): scan mu_1 and
   record the set of alpha(v) reached. Then pin the free position needed for alpha(v)=0.1033.
D. Continuous-n transmutation map: for real n in [8,16], ln(M_Pl/Lambda*) with alpha*=1 as the
   strong-coupling marker (also 0.785); width of the n-window giving Lambda in [1e-21,1e-19] M_Pl.
E. Self-consistency of the hierarchy formula with running: with mu_{k+1}/mu_k = alpha(mu_k)
   (instead of the frozen alpha_LM), how many e-folds does the 16-rung staircase span?

## Pass / fail readings (fixed now)
- P1 "bridge is perturbatively determined and controlled": the repo staircase (block B) reaches
  v at 2 loops with alpha(v) within 15% of 0.1033 or 0.1162 AND the 3-loop result differs
  from 2-loop by < 20% at every rung.
- P2 "bridge not perturbatively controlled": staircase diverges before v at 2 loops, OR reaches
  v with alpha(v) outside both targets by more than 15%, OR the 3-loop/2-loop shift exceeds 20%
  anywhere where alpha > 0.1.
- Block A expected (prediction): n >= 12 or 13 are IR-conformal (no Lambda); n <= ~10 gives
  Lambda/M_Pl >= 1e-12; NO integer n gives Lambda/M_Pl within 10^{+-1.5} of 1.6e-20.
  Fail of this prediction (some integer n lands in the window) would mean the constant-content
  bridge is fine and the wall is only about the coupling value.
- Block C expected: alpha(v) covers a continuum from 0.077 to Landau pole as mu_1 varies, so
  0.1033 is reached at some mu_1: the bridge is existent but underdetermined (threshold law
  is the load). Fail: the reachable set misses 0.1033 => the perturbative bridge does not exist
  for any threshold placement.
- Block D expected: the window in n has width < 0.05 (tuning of a few percent in a matter
  count that is an integer in the framework).
- Block E expected: running shifts the span by more than 10% => frozen-alpha_LM rung ratio and
  a running coupling are inconsistent beyond the QFP-flat point n ~ 15.5.
Overall test outcome mapping: P1 => wall weakened (STANDS not dominated by control); P2 with
determinacy failure (Block C) => PRICED at the threshold law / taste-mass spectrum.
