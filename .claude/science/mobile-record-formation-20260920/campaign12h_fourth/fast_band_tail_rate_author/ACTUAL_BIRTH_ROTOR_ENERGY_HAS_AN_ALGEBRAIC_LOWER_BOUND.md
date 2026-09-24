# Actual first-birth rotor fast energy has an algebraic lower bound

This is a conditional corollary for the original lambda=0 rotor cube and its
three specified zero-field first-mark vectors. Take the compact-time joint
limit first. It is not a fixed-positive-physical-time microscopic statement,
a sharp decay asymptotic, or a statement about a physical heat destination.

Let V(tau), G(theta), Gamma and the physical five-cycle Fourier representation
be exactly those in the bound rotor-tail source. Fix delta,kappa>0. For each
resolved-plus, resolved-minus or coherent first mark, set

    r_i=R_i/sqrt(b_i),      f_i(tau)=||V(tau)r_i||^2.

There is a constant c_i>0, depending on the fixed model parameters and this
input, such that for every tau>=0,

    f_i(tau) >= c_i (1+tau)^(-5/2).                                    (1)

Together with the separately proved strong decay, this says f_i tends to zero
but has no exponential upper bound A exp(-a tau) with finite A and a>0.
The exponent5/2 in (1) is a sufficient lower bound, not a claimed exact power
law. Other exceptional phases or flatter dispersion may give slower decay.

## Premises carried from the rotor-tail theorem

The full physical N=6, charge-four, W=1 sector is L2(T5;C96). In this
representation the bounded generator is the analytic finite matrix

    L(theta)=-i delta G(theta)-kappa P_bright.

The24-dimensional dark charge block of G(theta) is identically zero as a
Laurent polynomial. At theta=0 its bright-from-dark block has rank23, with
kernel spanned by the normalized uniform dark vector u. One has

    L(0)u=L(0)*u=0.

Every other eigenvalue has strictly negative real part. Indeed an eigenvector
on the imaginary axis must lie in the dark kernel, and its dark component
equation then forces eigenvalue zero. The orthogonal complement of u is
invariant under both L(0) and its adjoint. Restricted there it has no zero or
imaginary eigenvalue. The zero eigenvalue is therefore algebraically simple:
the reducing decomposition is the zero1x1 block plus an invertible95x95 block.

The actual finite physical-word inputs have nonzero flat-phase overlaps,

    ||u u* rhat_i(0)||^2 = 1/12, 1/12, 1/6,                           (2)

respectively. These are overlaps at a fiber, not probabilities of being in
that measure-zero phase. They are exact path coefficients in the bound source.
The finite-word Fourier vectors rhat_i(theta) are analytic near zero.

## Local simple eigenvalue estimate

Choose a small complex spectral circle enclosing only zero for L(0). By
continuity and the finite resolvent identity the same circle defines a
rank-one Riesz projector P(theta) for all sufficiently small real theta.
The matrix entries are analytic in theta, and the contour integral makes
P(theta) analytic. Put lambda(theta)=Tr[L(theta)P(theta)]. This is its simple
eigenvalue and is analytic, with lambda(0)=0 and P(0)=u u*.

The derivative of the simple eigenvalue is

    partial_j lambda(0) = u* partial_j L(0) u = 0.                    (3)

For clarity, (3) follows by differentiating L(theta)v(theta)=lambda(theta)
v(theta) at zero and multiplying by u*, using u*L(0)=0 and u*v(0)=1.
The loss matrix is constant. The remaining expectation vanishes because u
lies in the dark charge space and its G dark/dark block vanishes identically,
not just at the single phase. Thus all five first derivatives vanish.

Taylor's formula on a smaller closed real ball supplies finite M>=0 and r>0
such that

    |lambda(theta)| <= M |theta|^2       for |theta|<=r.                (4)

No sign or positive-definiteness of a Hessian is needed for this estimate.
Dissipativity also gives Re lambda(theta)<=0. The bound needed below is
Re lambda(theta)>=-M|theta|^2, supplied by (4).

## A positive-measure neighborhood gives the lower bound

Continuity of P and the nonzero overlap (2) allow shrinking r, separately for
each of the three inputs if necessary, so that constants a_i>0 and B<infinity
satisfy

    ||P(theta)rhat_i(theta)|| >= a_i,
    ||P(theta)|| <= B                         for |theta|<=r.

The rank-one projector commutes with the exponential and obeys

    P(theta) exp[tau L(theta)] = exp[tau lambda(theta)] P(theta).

Hence, without subtracting a complementary mode or assuming a normal matrix,

    ||exp[tau L(theta)]rhat_i(theta)||
      >= exp[tau Re lambda(theta)] a_i/B.                              (5)

Integrate the square of (5) only over the physical five-dimensional phase
ball |theta|<=r/sqrt(1+tau). On this ball

    tau Re lambda(theta) >= -M r^2,

while its normalized Haar volume is

    Vol(B5(1)) r^5 / [(2*pi)^5 (1+tau)^(5/2)].

Plancherel therefore proves (1), for example with the strictly positive
constant

    c_i = (a_i/B)^2 exp(-2 M r^2) Vol(B5(1)) r^5/(2*pi)^5.

The local angular ball is chosen within a coordinate chart of the torus.
No claim of optimal constants, optimal radius or exact late-time exponent is
made. The construction works for fixed positive delta,kappa; it is not
uniform as either parameter tends to zero.

## Why the phase-zero exception now affects the actual input

A delta-supported flat-phase state is not physical. The lower bound integrates
an entire neighborhood of that phase, of shrinking but positive measure, in
the actual input's smooth Fourier distribution. It does not substitute the
exceptional fiber for the physical state and does not choose a new initial
wave packet for each tau. The initial vector r_i is fixed throughout.

An assumed bound f_i(tau)<=A exp(-a tau) would conflict with (1) for large tau,
since exp(a tau)/(1+tau)^(5/2) diverges. This excludes such an exponential
upper bound only for these stated limiting curves and parameters. It is not
a universal damping, reservoir or autonomous-physics no-go theorem.

## Verification and open scope

This corollary uses the exact flat-kernel rank, identically zero dark block and
actual-state overlaps of the sealed rotor-tail packet. It adds the analytic
simple-eigenvalue argument and the positive-measure integration; no numerical
fit or new matrix scan is used as evidence. Those premises and the new proof
must survive independent comparison before publication.

The general infinite-time classification at finite spin, a rate upper bound,
the complete exceptional phase set, fixed laboratory time, and the physical
energy destination remain unresolved. The result does not justify exchanging
the scale, spin and time limits. This is a personal root candidate with a
proposed bounded independent check; no audit verdict, axiom or TOE claim.
