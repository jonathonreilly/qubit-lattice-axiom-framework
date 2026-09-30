# T31 pre-registration (written BEFORE any run; Sonnet 5.5, 2026-09-29)

Wall T31 = L07-W3 (origin of alpha_LM^16, gate B4) + L07-W5 (which quantity is v, endpoint L_t=4, gate B5)
+ L07-W12 (undisclosed trial factors). Formula: v = M_Pl (7/8)^(1/4) (alpha_bare/u0)^16, u0 = <P>^(1/4),
<P> = 0.5934 (quenched pure-gauge Wilson SU(3) plaquette at beta = 6, "admitted reuse number").

## Hidden premise HP-Q (found while attacking W3/W12; not in the lane's wall entries)
The formula's own determinant is (2 u0)^16 = 16 DYNAMICAL colored tastes (the lane's E4 beta function
uses n = 16 active colored tastes at M_Pl, b3(16) = 1/3). But u0 is taken from the QUENCHED plaquette.
A consistent u0 would be the plaquette of the theory with those 16 tastes in the measure.
The formula's elasticity is d ln v / d ln P = -4, so any plaquette shift dP moves v by -4 dP/P.

## TEST A (decisive for HP-Q). Script: hmc_unquench.py
SU(3) Wilson gauge action, beta = 6, L=4 periodic lattice (antiperiodic time for fermions),
staggered D with eta phases, weight det(D+m)^Ns, Ns = number of staggered fields (4 tastes each);
Ns = 4 is the formula's 16 tastes. Exact dense determinant + exact dense fermion force, HMC.
Baseline: Ns = 0 (quenched) on the same lattice (repo smoke value at L=4: 0.59601 +/- 0.00078).
Quantity: dP = <P>(Ns=4, m) - <P>(Ns=0), same L, same beta.
Validity gates (must hold or the run is void): (g1) analytic force = finite-difference force to 1e-5 rel;
(g2) HMC acceptance >= 50% and mean |dH| < 1; (g3) quenched baseline within 3 sigma of 0.5960 +/- 0.001.
Readings:
  PASS (u0 robust to unquenching): |dP| <= 5e-4  (v moves <= 0.34%, inside the lane's own quoted MC ambiguity).
  FAIL (HP-Q is a load-bearing premise): |dP| >= 2e-3 (v moves >= 1.4%, i.e. >= 50x the headline 0.026%).
  In between: inconclusive, needs larger volume.
PREDICTION (recorded before running): FAIL, dP > 0 (fermion loops screen the gauge field), likely +0.02..+0.10.
Finite-volume caveat is stated in advance: L=4 is a bounded demonstration of sign and size, not an
infinite-volume value; the PASS/FAIL readings are about the SIZE relative to 5e-4 / 2e-3, which a
finite-volume error of a few 1e-3 cannot turn around if dP is O(1e-2).

## TEST B (forking-paths ledger, W12). Script: forking_ledger.py
Family F160: prefactor in 5 endpoints L_t {2,4,6,8,inf} x {4th root, 16th root}  (10)
  x coupling in {alpha_bare, alpha_LM, alpha_bare/u0^2, alpha_bare/u0^4} (4)
  x M_Pl in {1.2209e19, 2.435e18} (2)  x target in {246.22, 174.10 = 246.22/sqrt2} (2)
  = 160 members, exponent N free integer 1..40.
Family Fmin: 5 endpoints x 4th root x {alpha_bare, alpha_LM} x M_Pl 1.2209e19 x target 246.22 = 10 members.
Quantity: p_LEE(tau) = fraction of log-uniform random targets in [50,1000] GeV that some member (N free)
  hits within +/- tau. Compare with tau_obs = 0.026% (quoted), 0.2%, 0.4% (lane's own MC ambiguity).
Readings: p_LEE(tau_obs) < 1% under F160 => the hit is not a selection artifact even allowing every
  listed choice; p_LEE >= 10% => it cannot count as independent evidence.
PREDICTION: p_LEE(0.026%) ~ 3% (F160), ~0.3% (Fmin); p_LEE(0.4%) ~ 40% (F160).

## TEST C (only if time): quenched beta=6 plaquette at L=8 in C, to see which side of 0.5934 it lies on.

## TEST D (route R2 falsifier; written before running). Script: staircase2loop.py
Literal staircase: SU(3) with n = 16-k colored Dirac tastes active between rungs mu_k = M_Pl alpha_LM^k (k=0..16),
2-loop beta (b0 = 11-2n/3, b1 = 102-38n/3), start alpha(M_Pl) in {alpha_bare, alpha_LM, alpha_s=0.1033}.
Quantity: rung at which alpha first reaches 1 (strong coupling). Lane's E4 = same at 1 loop (Landau crossing).
PASS (perturbative staircase consistent with a 16-rung hierarchy): alpha stays < 1 through rung 15 and reaches 1 within
  +/-1 rung of rung 16 for alpha_s.
FAIL: alpha reaches 1 at rung <= 12, or never (Banks-Zaks trapping) => the colored-decoupling staircase does not
  reproduce the 16 rungs perturbatively, so the rung law would have to be entirely non-perturbative.
PREDICTION (before running): FAIL, strong coupling around rung 9-12.

## TEST A2 (finite-time-extent robustness of A; added after A's first results, disclosed as post-hoc)
Same code with anisotropic extents (LT,LS) = (6,4) and (8,4): Ns=4, m=0.02 and matching quenched runs.
Reading: dP within a factor 3 of the 4^4 value (0.065) counts as robust.  Purpose: show the shift is not a 4^4 artifact.
