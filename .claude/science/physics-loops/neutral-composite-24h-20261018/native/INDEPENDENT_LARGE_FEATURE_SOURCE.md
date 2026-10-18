# Near-threshold original-source normalization check

Read `/tmp/neutral_threshold_root.md`. The proposed positive source-weight asymptotic has the correct derivative sign, factor two, and root normalization, provided the energy-dependent cavity expansion is differentiated using the underlying lattice Green functions rather than a bare undifferentiated O(log^-2) remainder.

## Cavity derivative

Write delta=E_h-E>0 and L=log(1/delta). The free two-dimensional quadratic band minimum gives

g00=-c L+O(1), c=1/(8pi sqrt(b)),
g00'=-c/delta+O(log(1/delta)).

The minus sign in the derivative is required: d(E-H)^(-1)/dE=-(E-H)^(-2). For differences D_r=g_r-g00 with fixed r, the numerator exp(ikr)-1 vanishes quadratically after parity integration, giving D_r=D_r(edge)+O(delta L) and D_r'=O(L). These estimates hold uniformly near the stated positive critical b, away from b=0.

Use the exact cavity formula before differentiating. Its singular correction is -2 D D^T/g00, and hence

-G_hole'(E)=2 D D^T/[c delta L^2]+o(1/(delta L^2)).

Terms from D', the finite Green differences, and the regular part of g00 are lower order. Differentiating an unspecified O(L^-2) function without these local derivative estimates would not by itself justify this conclusion.

## Full state norm, including rays

Let u be the two-component host-root amplitude. The host wavefunction is R_host sigma P u, so its norm is sigma^2 u^T(-G_hole')u. If u=rho v_E with v_E normalized and v_E->v at criticality, its leading norm is

rho^2 sigma^2 * 2(D.v)^2/[c delta L^2].

The eliminated-ray norm is -sigma'(E)|u|^2, finite relative to |u|^2 because E_h(b_c)<-4 is strictly below the ray band edge. It is negligible compared with the diverging host norm, but should be acknowledged in the normalization equation. No extra root norm should be added to the host term: that term already includes the host roots.

Therefore, for a unit-normalized full bound state,

|u|^2 ~ c delta L^2/[2 sigma^2(D.v)^2].

The ground-dressed leading source is lambda(-1,b) in the normalized root basis. Its positive bound-state weight is consequently

lambda^2 delta L^2 * c[(-1,b).v]^2/[2 sigma^2(D.v)^2].

This is a real positive Hilbert-space weight below the continuum, unlike the complex bilinear residue of an outgoing resonance. An arbitrary overall sign of v cancels. The positivity of the lower-bound-state root vector also ensures D.v>0 when both D components are positive.

## Independent critical-point numerical check

An independent one-dimensional quadrature of the edge Green differences, followed by a two-by-two eigensolve, is saved in `/private/tmp/neutral_threshold_source_control.py`. At the supplied b_c=0.23475690092702978 it gives approximately

D=(0.17819171,0.30588363), sigma=-1.02089431505,
Birman eigenvalues=(0.25696130,1.00000000),
v=(0.49068949,0.87133451),
(-1,b_c).v=-0.28613770028,
D.v=0.35396376082.

The source factor is comfortably nonzero numerically, and the weight prefactor c[(-1,b).v]^2/[2sigma^2(D.v)^2] is approximately0.02574494410. This is an independent quadrature check, not a rigorous interval certificate for the exact critical root. If an analytic nonzero claim is required, retain either an explicit certified error enclosure for these quantities and b_c or a separate exact inequality; the decimal alone must not be called such a certificate.

## Limits and premises

The normalization result concerns the explicit K1 coefficient model and its leading dressed source. As b approaches the binding threshold, delta is exponentially small in the distance to threshold and the spatial extent grows. Higher native coefficients can shift the edge, critical momentum, source, and binding energy. Fixed small lambda does not justify taking delta arbitrarily below those omitted scales. A joint limit needs bounds comparing the higher-order spectral perturbations with the shrinking gap and comparing source errors with lambda sqrt(delta) log(1/delta). A global O(lambda^2) source bound alone can exceed that fading leading amplitude.

Thus the formula exhibits a coefficient-model relation between large extent and vanishing local readout. It does not establish the same scaling in full H arbitrarily near threshold, a selected momentum/state, empirical scalar coupling, or a measured particle. The supplied asymptotic delta law also needs its own uniform energy/b dependence estimates; the source calculation does not prove critical-point uniqueness.

## Follow-up: critical source nonzero is now interval certified

Inspected `/tmp/neutral_threshold_interval.py` and its JSON, then replayed the interval calculation without its output-writing statement. The source uses closed edge formulas Dx=atan(1/sqrt(b))/(2pi), Dy=atan(sqrt(b))/(2pi b), Dxy=1/(2pi sqrt(b)), consistent with the prior independent quadrature. Its interval arithmetic operates at 40 decimal digits and reproduces the reported signs:

mu_max(0.2347569009270)>1,
mu_max(0.2347569009271)<1.

Continuity supplies a root in this interval; the separately established monotonicity identifies it as the critical root. For the two-by-two Birman matrix with entries (A,B;B,D), the eigenvalue-one relation is v_x/v_y=B/(1-A). Interval evaluation over the whole bracket gives

0.56314708582620379347 < v_x/v_y < 0.56314708582793521538.

I also explicitly checked that B>0 and 1-A>0 throughout the interval, so the ratio formula has no singular denominator or sign ambiguity. Its lower endpoint exceeds the upper bound on b_c by more than0.328. Therefore (-1,b_c).v=v_y(b_c-v_x/v_y) is strictly negative for the positive normalized eigenvector. The leading critical source overlap is rigorously nonzero within these interval arithmetic and closed-form inputs.

This resolves the numerical-only nonzero qualification in the earlier section. It does not remove the separate higher-native-order/joint-limit qualifications: the binding gap still shrinks exponentially, and a coefficient-model interval certificate does not control omitted microscopic perturbations at that scale.

The first replay attempted the tensor virtual environment, which lacks mpmath; replay with the system Python succeeded and reproduced every interval. This was a runtime dependency issue, not a scientific discrepancy. No root-owned output files were changed by this check.
