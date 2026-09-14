# Closed integer currents: density does not bound infrared response

Author-proposed inference counterexample, independent review pending. This is
an explicit comparison ensemble, not the determinant-coupled Villain gas.
It rules out only an argument from small density and current conservation
alone. The action's Coulomb energy and loop interaction structure remain
available and must be used in a successful phase proof.

On the dual Z^4 lattice choose the oriented boundary j_L of an L by L square
in the 1,2 plane, with 4L unit current edges. For every translated square
anchor x take independent centered integer variables Z_x distributed as the
difference of two Poisson(lambda/2) variables. Thus E Z_x=0 and Var Z_x=lambda.
Define the stationary integer current j=sum_x Z_x tau_x j_L. Each edge sees
only finitely many terms (2L in each of the two active orientations), so this
is a well-defined translation-invariant probability field. Every square
boundary is divergence-free, hence delta j=0 exactly. Lattice Hodge duality
identifies it, up to orientation shifts and signs, with an integer closed
three-cochain m.

For either active edge orientation,

    E j_e^2=2L lambda.

Set lambda=rho/(2L), for arbitrary rho>0. Every component's second moment is
then at most rho, and P(j_e !=0)<=rho. This is a uniform small-density bound,
including integer-current conservation.

Use Fourier convention sum_x f(x) exp(-i k.x), q_mu=exp(i k_mu)-1. The square
surface is a product of geometric sums S_L(-k_1)S_L(-k_2), with
S_L(k)=sum_(r=0)^(L-1) exp(i k r). Its boundary Fourier vector obeys

    jhat_L,1 = (1-exp(-i k_2)) S_L(-k_1) S_L(-k_2),
    jhat_L,2 = -(1-exp(-i k_1)) S_L(-k_1) S_L(-k_2),

for the square with bottom edge in the positive 1 direction. Its squared
norm is (|q_1|^2+|q_2|^2)|S_L(k_1)S_L(k_2)|^2, and it is transverse in the
matching divergence convention. The current spectral covariance is exactly

    H_j(k)=lambda jhat_L(k) jhat_L(k)^*.

For k=(u,0,0,0), its active transverse eigenvalue divided by |q(k)|^2 is
lambda L^2 |S_L(u)|^2. Consequently

    lim_(u->0) ||H_j(u,0,0,0)||/|q(u,0,0,0)|^2
       =lambda L^4=rho L^3/2.

Any inequality H_j(k)<=epsilon |q|^2 P_transverse(k), equivalently the
Hodge-dual current-response comparison, requires epsilon>=rho L^3/2.
At fixed arbitrarily small density rho this necessary coefficient is
unbounded as L grows. Thus density and exact closedness alone cannot supply
the small response coefficient needed by the proposed compact photon
consumer. A quantitative large-loop area or susceptibility bound is essential.

This ensemble is intentionally not claimed to satisfy the derived sector
weight comparison or the Wilson determinant action. It does not show that
the actual model lacks a compact Coulomb phase, or that any axiom is wrong.
The affirmative alternative is to exploit the actual loop-energy penalty
and control the area-weighted response, as in the pure-model renormalized
current machinery, with the determinant perturbation's hypotheses checked.
