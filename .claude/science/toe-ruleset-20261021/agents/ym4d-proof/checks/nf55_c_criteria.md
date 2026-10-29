# nf55_c — criteria (written before nf55_c.py exists)

Owner: NONFREE55 (claude-opus-5-5). Exact symbolic arithmetic (sympy; Euler's constant kept as a symbol gE; no floats).
Purpose: verify the only analytic import of Theorem FS — the small-z series of K_1 (Abramowitz-Stegun 9.6.11) — independently
of any Bessel implementation, by the modified Bessel ODE, and record its log structure.

Object: Y_M(z) := 1/z + Lg * I1_M(z) - (1/2) sum_{k=0}^{M} (psi(k+1) + psi(k+2)) (z/2)^{2k+1} / (k! (k+1)!),
I1_M(z) := sum_{k=0}^{M} (z/2)^{2k+1}/(k!(k+1)!), Lg a symbol standing for log(z/2) with d(Lg)/dz = 1/z,
psi(n) = -gE + H_{n-1} (harmonic numbers, exact rationals). M = 6.

Gates:
- C1 (ODE): R := z^2 Y'' + z Y' - (z^2 + 1) Y, with the chain rule d/dz Lg = 1/z. Every coefficient of z^n Lg^j in R with
  n <= 2M + 1 vanishes identically (as a polynomial in gE). PASS iff all vanish.
  Control C1-F: replace the factor (1/2) in front of the psi-sum by 1; at least one coefficient with n <= 2M+1 must be nonzero.
  FIRES if nonzero.
- C2 (structure): z * Y_M(z) = 1 + sum_k (alpha_k + beta_k Lg) z^(2k+2): the maximal power of Lg is 1, no negative powers of z
  other than those cancelled, the constant term is 1, and the coefficient of z^2 Lg is 1/2. PASS iff all hold.
- C3 (products keep nonnegative log powers): expand (z*Y_M)^3 to order z^6: every monomial has Lg-power in {0,1,2,3}, and the
  z^0 coefficient is 1. PASS iff both hold. (A sanity check of FS step 3; it cannot fail unless the series has a 1/Lg term.)
Verdict: PASS iff C1, C2, C3 pass and C1-F fires.
