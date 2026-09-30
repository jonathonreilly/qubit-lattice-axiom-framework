"""T63 lemma check: S(k) of a short-range stationary field is analytic (S0 + S2 k^2 + ...), so its small-k exponent is 0 or 2
(4 if momentum-like conservation); a non-integer exponent needs power-law correlations h(r) ~ r^-(3+alpha).
Numerical illustration on a 1D ring: exponentially correlated h(r) = exp(-|r|/xi) has S(k) = sinh(1/xi)/(cosh(1/xi)-cos k),
power-law h(r) = |r|^-(1+alpha) (alpha=0.965, 1D analogue, sign-corrected so S(0)=0) has S ~ |k|^alpha."""
import numpy as np
xi = 3.0
k = np.array([0.02, 0.04, 0.08, 0.16])
S_exp = np.sinh(1/xi)/(np.cosh(1/xi) - np.cos(k))
slope = np.diff(np.log(S_exp))/np.diff(np.log(k))
print("exp-correlated (xi=3): local log-slopes at k=0.02..0.16:", np.round(slope, 4), "-> 0 at small k, analytic")
# conserved case: h(r) with sum h = 0: h(r) = exp(-|r|/xi) - 2 exp(-|r|/(2 xi)) * c ... use S = S2 k^2 * lorentz
S_cons = (2 - 2*np.cos(k)) * (np.sinh(1/xi)/(np.cosh(1/xi) - np.cos(k)))
slope = np.diff(np.log(S_cons))/np.diff(np.log(k))
print("conserved (sum h = 0) short-range: local log-slopes:", np.round(slope, 4), "-> 2 at small k, analytic")
alpha = 0.965; r = np.arange(1, 200001); kk = np.array([0.001, 0.002, 0.004, 0.008])
h = r**(-(1+alpha))
# S(k) - S(0) part: power-law tail gives S(k) = S0 - c |k|^alpha (non-analytic); fit the k-dependence of S(0)-S(k)
S = 1 + 2*np.array([np.sum(h*np.cos(q*r)) for q in kk]); S0 = 1 + 2*np.sum(h)
d = S0 - S
print("power-law tail alpha=0.965: local log-slopes of S(0)-S(k):", np.round(np.diff(np.log(d))/np.diff(np.log(kk)), 3), "-> ~alpha: non-analytic")
