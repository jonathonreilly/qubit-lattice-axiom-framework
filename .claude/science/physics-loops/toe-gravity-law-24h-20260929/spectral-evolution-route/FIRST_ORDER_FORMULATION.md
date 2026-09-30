# Exact finite variation and candidate uniform estimate

Work in the six independent metric coordinates g_A with density momenta p_A;
pi_ii=p_ii, pi_ij=p_ij/2. Set B^ij=sqrt(det g)g^ij,
q_l,A=D_l g_A and r_l,ij=D_l B^ij. Let Gamma(g,q) have its literal Christoffel
formula. Define the algebraic function

 V(g,q,r)=K[r_k,ij Gamma^k_ij-r_j,ij Gamma^k_ik
       -B^ij(Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik)].

All repeated spatial indices are summed, including both symmetric matrix
entries in the B/r slots. Treat r as nine entries for algebraic variation;
its actual symmetry is preserved on the consistency manifold. T is the ADM
kinetic density. Exact skew summation by parts, without product/chain rules,
gives H_J=mean[T(g,p)+V(g,Dg,D B(g))]. Consequently, with ordinary local
partial derivatives in the independent g,p coordinates,

 A_A=T_(p_A),
 gdot_A=A_A,
 pdot_A=-T_(g_A)-V_(g_A)+sum_l D_l V_(q_l,A)
                     +sum_l,ij B^ij_(g_A) D_l V_(r_l,ij),
 qdot_l,A=D_l A_A,
 rdot_l,ij=D_l(sum_A B^ij_(g_A) A_A).

The minus sign from skew D occurs inside the Hamiltonian gradient and is
reversed by pdot=-H_g. Differentiating the constraints q-Dg and r-D B(g)
in time gives zero EXACTLY. Thus this is an augmented analysis of the same
finite canonical dynamics, not an enlargement of its physical carrier.
No D B(g)=B_g Dg assertion is made. Every displayed RHS contains at most
one D acting on an algebraic analytic function of the augmented variables.

For Fourier Wiener norm |u|_sigma=sum_k |u_k|exp(sigma |k|_1), circular
convolution satisfies the same algebra inequality as ordinary convolution,
because |wrap(k+l)|_1<=|k|_1+|l|_1. If N_sigma(u)=sum_k |k|_1|u_k|exp(sigma|k|_1),
then N_sigma(uv)<=|u|N(v)+N(u)|v|, with wrap retained. Absolutely convergent
analytic coefficient majorants extend this inequality to local analytic
functions. On |h|<=r<1 and total augmented norm<=M, the finite RHS therefore
obeys |F_J(U)|_sigma<=C0+C1 N_sigma(U), uniformly in J. A separate algebraic
bound |A(g,p)|_sigma<=C_h controls hdot without any spatial derivative.
These constants must be concretized from the finite displayed expression,
not presumed independent of the inverse-metric margin.

Candidate proof: choose sigma(t)=sigma0-vt, v>C1 on the bootstrap ball.
Upper Dini differentiation gives d|U|_sigma(t)/dt<=C0 and
 d|h|_sigma(t)/dt<=C_h. Bootstrap metric and total norm margins, then finite
ODE continuation gives a common positive time. Initial q/r norms are bounded
from original analytic data at2sigma0 by the derivative loss. A compactness
argument in strictly smaller radii can construct the continuum solution.
This would avoid invoking unverified strong hyperbolicity. The limits and
uniqueness still require complete written estimates.

Sampling I_J is a point-evaluation algebra homomorphism, including analytic
matrix functions while the series converges. It is a contraction from infinite
Wiener norm to the corresponding finite representative norm. Its derivative
commutator satisfies, for delta=sigma-sigma'>0,

 |(D_J I_J-I_J partial)f|_sigma'
 <=4/(e delta) exp[-delta(J+1)/2] |f|_sigma.

Indeed the summand vanishes inside Q_J; outside it |k|_1>=J+1 and
|wrap(k)_j-k_j|<=2|k|_1. Use x exp(-delta x/2)<=2/(e delta).
In the augmented system local analytic maps commute with sampling exactly,
so only these derivative commutators enter the consistency source.

For a linearized difference equation with scale Lipschitz constant C/(rho-rho'),
allocate a fixed radius reserve d equally among m time-ordered factors.
The mth Dyson bound is (Cm/d)^m t^m/m! <=(eCt/d)^m. Thus for eCT<d a
uniform bounded difference obeys |w(t)|_(rho-d)<=
(|w0|_rho+T sup|R|_rho)/(1-eCT/d). An actual proof must also bound the
iterated remainder before passing m to infinity, and place every intermediate
solution on a common convex metric-safe analytic ball.

For unit lapse/zero shift the continuum algebra yields Jdot_i=0 and
 Cdot=partial_j(aK g^ij J_i). Hence compatible initial continuum constraints
remain zero. The finite C density uses one D Gamma, and the actual finite
momentum density is J_k=pi^ij q_k,ij-2D_j(g_ik pi^ij). Convergence in one
larger analytic radius controls these densities in a smaller radius. None of
these observations yet certifies a uniform error constant without finishing
the bootstrap, consistency, stability and continuum construction.
