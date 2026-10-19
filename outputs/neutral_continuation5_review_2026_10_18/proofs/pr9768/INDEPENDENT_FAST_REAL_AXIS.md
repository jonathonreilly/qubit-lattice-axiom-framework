<!-- Original PR9768 source SHA256 8de1eb7e6ac3c3e8fee18330c6b63befe6d14d01bc4523610849213f61c03230. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Nearest-neighbor confined fast arm: upper-half-plane Weyl check

Disposition: PASS for the specified NN model, with signs and normalization below. This is not a proof for the corrected range-two/native arm or the complete source response.

Let H on n=1,2,... have diagonal f(n+1), off-diagonal -2, f=lambda^3/16>0. Define g(z)=<1|(z-H)^(-1)|1>, Im z>0. Then Im g<0 and

 g(z)=1/[z-2f-4/(z-3f-4/(z-4f-...))].

Put x=4/f and nu=1-z/f. The square-summable solution at infinity is psi_n=J_(n+1-z/f)(x): its recurrence is 2(psi_(n-1)+psi_(n+1))=[f(n+1)-z]psi_n. At the boundary (z-2f)psi_1+2psi_2=-2psi_0. Therefore the exact ratio is

 g(z)=-J_(nu+1)(x)/[2 J_nu(x)].

The minus sign, order offset 1-z/f, and factor 2 are essential. This choice has the correct negative imaginary part.

For z=E+i eta with E=O(lambda), eta=beta lambda^3, fixed beta>0, nu/x=(f-z)/4 tends to zero and Im nu=-eta/f=-16 beta. Choose analytic branches a=acos(nu/x) near pi/2 and kappa=sqrt(x^2-nu^2) near positive x, and set

 theta=kappa-nu a-pi/4.

Uniform oscillatory Debye/stationary-phase expansion in this compact interior regime gives J_nu(x)=(2/(pi kappa))^(1/2)[cos(theta)+O_beta(1/x)], and the adjacent-order formula yields

 g(z)=-[cos(a)+sin(a) tan(theta)]/2+O_beta(f).

Here the order is allowed to grow like x lambda; the relevant uniform parameter is nu/x bounded away from +/-1, not bounded nu. One can obtain the expansion directly from the Bessel integral: the two nondegenerate saddles stay separated with curvatures comparable to x; the complex order has fixed bounded imaginary part. The adjacent-order phase increment is -a+O(1/x), and amplitude ratio is 1+O(1/x). Since Im theta stays strictly positive for fixed beta, division by cos(theta) is uniform. Constants may depend on beta; no assertion uniform as beta down to zero is made.

Since d theta/d nu=-a, for real E,

 Im theta=(eta/f) acos((f-E)/4)+o(1) -> 8 pi beta.

Thus, writing theta_R=Re theta,

 g(z)=-(1/2) tan(theta_R+i 8 pi beta)+o(1).

In particular

 (1/2)tanh(8 pi beta)-o(1) <= |g(z)| <= (1/2)coth(8 pi beta)+o(1).

These are finite positive bounds for each fixed beta>0. Likewise -Im g is bounded below by (1/2)tanh(8 pi beta)-o(1). Finite bounds for the reciprocal follow immediately.

For an explicit ripple representation set q=exp(2i theta), with |q| -> exp(-16 pi beta). The leading tangent formula is

 g(z)=-(i/2)(1-q)/(1+q)+o(1).

Hence the expected damping exp[-pi eta/f]=exp[-16 pi beta] is correct in the limit E=O(lambda). More exactly the phase factor has magnitude exp[-2(eta/f) acos((f-E)/4)+o(1)]. For fixed beta this is nonzero, although it can be exponentially tiny. The ripple does not disappear as lambda tends to zero along generic paths.

For the explicit path E=-6lambda, theta_R diverges with leading term 64lambda^(-3) and is eventually strictly monotone; it traverses infinitely many periods, so distinct phase subsequences give different limiting values of g. An unspecified approximate E can change this phase: an error much larger than f is NOT negligible for pointwise g. Persistent ripple as a function of real energy follows from d theta/d E=a/f, with period Delta E approximately pi f/a approximately 2f. A claim of nonconvergence along an arbitrary deliberately phase-locked E(lambda)= -6lambda+o(lambda) would be too strong.

If a separately derived full-host Schur identity gives R_dd=-1/(4g)+o(1), the above model gives the leading expression

 R_dd=-(i/2)(1+q)/(1-q)+o(1),

again bounded and with persistent phase ripple. R_dd itself is O(1) in these fast resolvent units, not O(lambda). An original source of amplitude O(lambda), together with the physical resolvent factor 1/(Jz lambda), produces an O(lambda/Jz) source response; this separate normalization is needed to call the baseline O(lambda). The NN calculation alone does not establish that Schur identity or the native source contrast. For comparison on the claimed slow linewidth scale, eta=O(lambda^3) in fast units is physical imaginary energy O(Jz lambda^4).

A small numerical sign check using the exact Bessel ratio at lambda=.5,.3 and beta=.02 agrees with the Debye formula (absolute errors approximately 7.55e-4 and 1.34e-4). These checks supplement the recurrence/asymptotics, not the proof.

The real-axis limit eta=0, a beta tending to zero, the corrected range-two long arm, and the full native response require separate estimates. Nothing here repairs the earlier fixed-complex-gamma derivative gap or proves a global no-go.
