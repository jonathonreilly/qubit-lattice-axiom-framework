# Outgoing COM pole envelope: focused check

Disposition: PASS as a conditional Fourier-multiplier lemma for the defined outgoing pole component. It does not strengthen the exact pole derivative theorem and does not identify a physical wavefunction probability.

Use a unitary Fourier convention, for example Psi(x)=integral a(p) exp(ipx) dp/(2pi) on the integer lattice with Parseval measure dp/(2pi). Let f be fixed in L2 with support in a fixed small compact momentum interval, put r_lambda=R_lambda/lambda^6, and assume uniformly there r_lambda -> R, E_lambda-E_app=O(J lambda^(14/3)), and bounded r_lambda. Take t=T0/(J lambda^4), fixed T0>=0. Assume the stated outgoing sign, or merely uniform boundedness of both time multipliers on this time scale. Uniformly negative leading imaginary part supplies the outgoing sign for sufficiently small lambda.

Then |(E_lambda-E_app)t|=O(T0 lambda^(2/3)). The exponential difference identity bounds the multiplier difference by O(lambda^(2/3)), with a constant depending on fixed T0. Parseval and the uniform residue convergence give

 ||Psi_lambda-Psi_app||_ell2 <= C_T0 ||f||_L2 [sup|r_lambda-R|+O(lambda^(2/3))] = o(1),

where Psi_app has Fourier amplitude f(p) R(p) exp[-i E_app(p)t]. An additional energy error O(J lambda^5 log(1/lambda)) has phase error O(lambda log(1/lambda)), also vanishing. No derivatives of E_lambda or R_lambda enter this statement.

For the squared-kernel measure, define its UNNORMALIZED characteristic transform

 Chi_lambda(k)=sum_x exp(ik lambda^2 x)|Psi_lambda(x,t)|^2.

Its difference from the approximate transform is o(1), since the position multiplier is unitary and the L2 norms are uniformly bounded. With delta=k lambda^2, exact Fourier translation gives the approximate integrand

 a(p) conjugate[a(p+delta)] exp{it[conjugate(E_app(p+delta))-E_app(p)]},

where a=fR. This fixes the sign for the exp(ipx) Fourier convention. Translation continuity in L2 controls a(p+delta)-a(p), so f need not be differentiable. Smoothness of the APPROXIMATE coefficients gives

 t Re[E_app(p+delta)-E_app(p)] -> k T0 e2'(p)=k T0 sin(p/2).

The Airy term contributes O(lambda^(4/3)) to this phase difference and the fourth-order term contributes O(lambda^2). Also

 t Im[E_app(p+delta)+E_app(p)] -> 2T0 Im e4(p)=-T0 g(p),

because c is real, Im e4=Im a_p/8, and g=-Im a_p/4. Consequently

 Chi_lambda(k) -> integral |f(p)R(p)|^2 exp[-T0 g(p)] exp[ik T0 sin(p/2)] dp/(2pi).

There is no missing factor of two in the damping. If the requested transform is a probability characteristic function, divide this expression by its k=0 value, assuming nonzero fR. As written it is a finite positive measure with decaying total mass, not a normalized probability. With Lebesgue-unitary rather than lattice-normalized Fourier conventions, replace dp/(2pi) by the corresponding Parseval measure consistently.

The lattice must be specified in the definition. Integer x has a 2pi Brillouin period. If x denotes physical half-integer interval centers, use the matching lattice spacing, Fourier measure and internal fiber convention instead. The fixed compact momentum support away from a chosen seam prevents wraparound/alias terms for delta=k lambda^2; there is no scaling obstruction. A finite periodic volume additionally needs its circumference much larger than lambda^(-2), or a separately stated discrete-momentum limit. The lemma as given applies directly to the infinite lattice/continuous Bloch fiber definition.

This proves a pushforward limit for the defined pole-component intensity under velocity sin(p/2), with damping weight exp[-T0 g]. It does not establish that the full microscopic response is dominated by this component, remove continuum backgrounds, select a physical state, prove a particle interpretation, or bound the exact pole's pointwise momentum derivatives. In particular the previously identified fast-strip complex-gamma gap remains open and is not a global no-go theorem.
