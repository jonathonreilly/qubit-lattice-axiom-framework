# Uniform soft-photon closure for the fixed-point rate limit

Author supplement v2, 2026-10-12. Replaces the provisional angular argument in EMISSION_ENDPOINT_PROOF.md; the earlier bytes are preserved. Fixed n, A=sum n_i^4<1, b>0, b^2<M(A), mu=b r^2. Exclude b^2=F_A(1) and multiple zeros of F_A-b^2 on (0,1). Constants need not be uniform near these excluded boundaries, onset, the axis or b=0. No interacting or observational closure.

The checked kinematic localization gives k=O(r), |q|>=c r and |q|+|k|-r=O(r^3) on a nontrivial shell. For any fixed epsilon>0, |k|>=epsilon r therefore confines the shell to q=y r n+r^2 t with y bounded away from zero and bounded t. Compact coarea expansion gives the proposed leading integrand. Simple longitudinal roots cause no nonintegrable factor: the delta integral of a positive quadratic form in two transverse coordinates stays bounded as its radius tends to zero. Shifted stationary centers change the scaled shell by o(1).

For 0<|k|=lambda<epsilon r, with epsilon<1/2 fixed, write k=lambda u. On p-s lambda u (0<=s<=1), electron momentum has norm at least (1-epsilon)r. Uniformly on this segment,
 grad e(v)=v/|v|+O(r^2).
The function (p-s lambda u).u/|p-s lambda u| decreases in s, since its derivative is minus lambda times a nonnegative transverse square divided by |p-s lambda u|^3. Thus
 [e(p)-e(p-lambda u)]/lambda <= n.u+C r^2.
Since omega(lambda u)/lambda>=1-C lambda^2, equality on the energy shell implies n.u>=1-C' r^2. This proves a uniform O(r) photon cone even as lambda/r tends to zero.

Parameterize that cone by
 x=lambda/r in (0,epsilon),
 u=sqrt(1-r^2|z|^2)n+r z, z.n=0, |z|<=C.
Use q=r(n-xu). With y=1-x, the exact energy gap has the uniform C^2_z expansion
 G(r,x,z):=[e(rn)-e(r(n-xu))-omega(rxu)]/(r^3 x)
          =[F_A(1-x)-b^2-|z|^2]/[2(1-x)]+O(r).
The quotient at x=0 is defined by its derivative in x; the fundamental theorem of calculus removes any apparent 1/x singularity. The norm |n-xu|>=1-epsilon ensures a smooth expansion on x in [0,epsilon], bounded z, with two z derivatives. Expanding the elementary sine/cosine symbols gives the displayed polynomial; no assumption about a photon infrared cutoff is used.

Choose epsilon small enough that F_A(1-x)-b^2 retains the nonzero sign of F_A(1)-b^2. If this sign is negative, no soft shell exists. If positive, G is uniformly strictly concave in z, has a bounded stationary center and a compact simple closed zero curve with positive radius bounded away from zero for the fixed scaling point. Its angular delta integral is uniformly bounded. Explicitly dOmega=r^2[1+O(r^2)]d^2z and delta(Delta)=(lambda r^2)^(-1)delta(G), giving
 integral dOmega delta(Delta) <= C/lambda.
This construction avoids the coordinate singularity of a polar angle at the cone axis.

The exact projector trace obeys sum S_lambda<=C r^2 on this cone. The incoming/outgoing Clifford unit vectors differ by O(lambda): their directions differ by O(lambda) because the photon angle is O(r), and their Wilson-mass ratios have bounded derivative along the collinear segment. Each transverse vertex expectation is O(r). Insert these facts into the exact trace identity (or its equivalent squared-matrix norm). Since omega>=c lambda,
 integral_(|k|<epsilon r) d^3k [sum S/omega]delta(Delta)
 <= C integral_0^(epsilon r) lambda^2 (r^2/lambda)(1/lambda)d lambda
 <= C epsilon r^3.
The same bound with an additional omega gives O(epsilon^2 r^4) for radiated power. The finite polynomial integrand is bounded at y=1. Taking r to zero first and then epsilon to zero completes the rate and power limits at the stated fixed nondegenerate points.

Consequently Gamma=alpha r^3/2 integral_(F_A>b^2) I_A,b(y)dy+o(r^3), with the integrand in EMISSION_RATE_DERIVATION.md, has no missing soft contribution in this domain. The onset formulas are subsequently limits of this polynomial integral, not a claim that r and distance-to-onset limits commute. Independent checking remains required before theorem-facing reuse.
