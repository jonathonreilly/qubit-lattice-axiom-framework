# POST failure details

No PRE bytes were modified.

POST_RUN_01_runner.py and POST_RESULTS_01.json preserve the first POST
execution. It stopped after 134 successful checks at "slow root correction
agrees". The source polynomial was correct. The variable substitution

    expand(polynomial).subs(epsilon**4, eta**2).subs(epsilon**2, eta)

produced

    6*I*delta*kappa + 3*I*delta*z*sqrt(eta**2)
      + I*delta*z + eta**2*z**2 + 2*kappa*z*sqrt(eta**2).

Because epsilon was positive and eta had no positivity assumption, the
sqrt(eta²) terms survived. Extracting a polynomial coefficient in eta from
that expression was invalid and yielded the spurious z1=0.

The corrected POST runner first obtains Poly(polynomial,epsilon), checks
that every exponent is even, and maps each monomial epsilon^(2n) to eta^n.
This does not change the polynomial or any scientific target. The corrected
derived coefficient is 18*kappa - 12*I*kappa**2/delta.

An intermediate ten-line shell diagnostic attempted to demonstrate the
substitution on independently named symbols, but mistakenly declared all
symbols positive:

    x,d,k,eta,z,z1=s.symbols('x d k eta z z1',positive=True)
    ...
    zz=s.solve(pp.subs(eta,0),z)[0]

Since the root z=-6k was then excluded by the diagnostic's positivity
assumption, solve returned an empty list and indexing raised:

    IndexError: list index out of range

This diagnostic did not write artifacts or modify any source. A subsequent
diagnostic projected the actual frozen PRE matrices, used unrestricted z,
and printed the exact surviving sqrt(eta²) terms above. The completed
POST run 02 uses the even-polynomial construction and passed 249 checks.
