# A degree-three reflection witness and an explicit sampling experiment

Direct parent derivation, 2026-10-12. Conditional mathematics for a prospective
experiment; no new empirical observation or novelty claim. This construction
does not use the pending all-order sphere-classification proof.

## Quantum bound

Let mu be normalized area on S2, and let C(a,b) be any binary bipartite
quantum correlation from one normal state and measurable local observables
on separable tensor Hilbert spaces. Fair marginals and isotropy are not
required. Vector factorization gives C(a,b)=u(a) dot v(b) with norms at most
one, using realification and purification as needed.

Let Pi3 project L2(mu) onto degree-three spherical harmonics. The addition
theorem gives its kernel 7 P3(a dot b), with P3(c)=(5c^3-3c)/2. The
reflection S=I-2 Pi3 has operator norm one. Apply it componentwise to the
vector-valued L2 functions. Cauchy-Schwarz gives the exact bound

    B(C) = - integral C(a,a) dmu(a)
           +14 double_integral P3(a dot b) C(a,b) dmu(a)dmu(b),
    |B(C)| <= 1.

The diagonal integral is an actual shared-setting measurement term, not an
illicit trace of a general L2 integral kernel. The bound follows from
B=-<u,Sv>; no trace or evaluation continuity is needed. Measurability makes
the diagonal vector inner product integrable.

For C(a,b)=-V f_k(a dot b), f_k(1)=1, and degree-three coefficient a3(k),

    B = V [1-2 a3(k)].

Thus a rigorously negative a3 gives a visibility threshold for this witness
without any tail summability assumption. This is a sufficient obstruction
to a common quantum realization, not the exact full-sphere threshold.

Fix the already prospective value

    k* = sqrt(2) [atanh(1/sqrt(2))-atanh(1/2)],

and V=.9,.95,1 before the new certificate calculation. No experimental data
or visibility is fitted. The exact cosine control has a3=0 and B=V. A
normalized signed polynomial control f=(1+eta)P1-eta P3 gives B=V(1+2eta).
For the unnormalized control f=P1-eta P3, the general formula is instead
B=V[f(1)-2a3]=V(1+eta). This distinction guards the diagonal normalization
in arbitrary controls.

## Exact interval certificate for a3 at the fixed k*

Write theta in [0,pi/2], a=2/pi, u=1-a theta, t=tanh(k cos(theta)), and
g=(u+t)/(1+ut). Then

    a3(k)=7 integral_0^(pi/2) g(theta) P3(cos(theta)) sin(theta) dtheta.

For 0<=k<=1/2, 0<=u,t<=1: |g_u|,|g_t|<=1;
|g_uu|,|g_tt|<=2 and |g_ut|<=4. Also |t'|<=k and
|t''|<=k+2k^2. Since a<2/3,

    |g'|<=7/6,
    |g''|<=2a^2+8ak+4k^2+k<=91/18<6.

For H=P3(cos(theta)) sin(theta), |H|<=1, |H'|<=7, and
|H''|<=25. The last bound uses |P3''|<=15, |P3'|<=6 and
|sin(theta)cos(theta)|<=1/2. Therefore |(gH)''|<48.
The composite midpoint error with n equal panels is at most

    7*48*(pi/2)^3/(24 n^2) < 7*48*(11/7)^3/(24 n^2).

The new checker uses n=2048 and exact outward fixed-point interval arithmetic
with rational Taylor remainders from the pinned arithmetic helpers in
sphere_certificate.py. It does not call that file's old certify_a3 function,
whose derivative bound was stated only for k<=.32. The bound48 and its wider
scope are derived above. The script independently encloses sqrt(2) using an
integer square root, encloses both atanh values by a positive series with
geometric tail, and propagates this interval for the exact k*. Midpoint
sine/cosine/exponential values have explicit Taylor remainders. The resulting
certificate contains rational endpoints and a rational quadrature error.
A separate mpmath integral is only a numerical consistency control.

## One bounded trial estimator

The exact integral of |P3(c)| on [-1,1] is13/20. Consequently the total
absolute coefficient weight of B is

    J = 1 + 14*(13/40) = 111/20.

For each heralded trial, select a branch independently of the source:

1. With probability20/111, choose uniform a, set b=a, and record Z=-J A B.
2. With probability91/111, choose uniform a; draw c on [-1,1] with density
   (20/13)|P3(c)| and a uniform azimuth about a to obtain b; record
   Z=J sign(P3(c)) A B.

Both local setting marginals are uniform in either branch. The branch must
not change the source or the local observable assigned to the same local
setting. In particular the devices must not be given a branch flag that
allows branch-dependent observables. Correlation between Alice and Bob's
settings is intentional; independence of the fresh joint setting choice
from the source is the required premise. Direct substitution gives E Z=B,
and every included trial has |Z|<=J. Undefined signs at P3=0 have probability
zero and can be assigned arbitrarily.

If the quantum conditional expectation per trial is at most one given the
past, bounded martingale Hoeffding gives

    Prob(mean Z >= 1+epsilon) <= exp[-N epsilon^2/(2J^2)].

Fresh independent random choices and the same local map across the two
branches must hold conditionally on the past. This accommodates source
memory under these premises; it does not cover setting leakage or selection
of coincidences. For the alternative, require E[Z_i | past]>=1+Delta on every included
trial; an iid stable source is one sufficient condition. This conditional
mean premise, rather than an unconditional average alone, gives the same
lower-tail bound around1+Delta. With decision threshold
1+Delta/2, both conservative error bounds are at most .01 when

    N >= 8 J^2 ln(100)/Delta^2.

This is an idealized prospective sample bound, not a power analysis of the
released drifting experiment. Real apparatus angular resolution, calibration,
random choices, detection and the definition of an included trial still need
an explicit measurement map. The finite 300-setting witness remains a
separate option with numerical candidate evaluation; this continuum
certificate does not retroactively certify its rounded implementation.

## Source continuity

This version adds only the explicit alternative conditional-mean premise
requested in independent reflection review R1. The pinned original note,
checker, freeze and rational result remain unchanged. Their arithmetic and
quantum bound apply without modification; this sentence makes the sampling
interpretation explicit. DIRECT_REFLECTION_WITNESS_V2.md is the current
complete statement. The original note is preserved for exact reproduction.
