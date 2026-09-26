# Exact initial-drift ambiguity in the six-moment mixed quantum encoding

**Status:** root-derived finite counterexample; independent check pending.
Not a published no-go or a claim against other quantum encodings.
**Date:** 2026-09-21.

The mixed singlet-triplet encoding in
DIMER_COVARIANT_QUANTUM_FLUCTUATION_ENCODING.md uses

    rho_a = [[q, w_a^dagger], [w_a, r I_3]],
    w_a=lambda_A e_a+i lambda_B b_a,  q+3r=1.

Choose q=1/2, r=1/6, lambda_A=1/8, lambda_B=1/12. Each state is positive:
max(lambda_A^2,3lambda_B^2)<qr. A probabilistic color mixture has density

    rho(p)=[[q,lambda_A X^T-i lambda_B Y^T],
            [lambda_A X+i lambda_B Y,r I_3]].

It contains only X and Y, not D,Z,w. The following exact finite-lattice
example checks whether the classical initial drift is well-defined on these
density operators. No quantum Hamiltonian is assumed.

Use the existing fixed-winding process on N=12, gamma=1, k0=11/10.
Let A=1/8, zeta=1/28, and for physical first coordinate x set

    c_x = cos(pi x/3),  Y=(0,0,A c_x),  X=0,
    p_(A,i,sigma)=1/14,
    p_(B,b)=1/14 + b_3 A c_x/8.

All probabilities are strictly positive. Define p' by increasing each
A_2 probability by zeta/2 and decreasing each A_1 probability by zeta/2,
at every site. Then p' is also strictly positive, X'=X, Y'=Y, and

    rho(p'(u))=rho(p(u)) for every black u.

Consequently the full tensor-product encoded density operators are equal
exactly, even though the classical preparations have different D_2.
The preparations are fixed smooth cosine profiles sampled on this finite
torus; this calculation only concerns their exact time-zero derivative.

For these states, every initial X_i vanishes. The exact four-context current
from DIMER_NONLINEAR_INITIAL_DRIFT.md gives

    J_(delta,X_2)(x)
        =gamma D_2/4 * delta.[e_2 cross (Y_l+Y_r)].

Only delta=-e_1 has a nonzero displacement and a nonzero scalar contraction.
Its route displacement is -2e_1, hence

    J_(-e1,X2)(x)=-gamma D_2 [Y_3(x+2)+Y_3(x-4)]/4.

The six-periodic profile makes the two Y entries equal. At x=1, the exact
incoming-minus-outgoing microscopic derivative is

    d_t X_2(1)|_0 =-3 gamma D_2 A/4.

Replacing D_2 by D_2+zeta changes this derivative by

    -3 gamma zeta A/4 = -3/896.

For the pair observable A_2=|0><2|+|2><0|, whose mixture mean is
2lambda_A X_2, the assigned derivative changes by -3/3584. Euler acceleration
would multiply both derivatives and their difference by N; it is not needed
for the counterexample. There are black sites with x=1, for example(1,1,0).

Thus this specified six-moment encoding assigns the same complete density
operator two distinct initial observable derivatives when combined with the
specified classical color law. A density-operator evolution cannot have both
assignments. This does not use a long-time limit, large-volume approximation
or the new hydrodynamic theorem.

The conclusion is deliberately narrow. It tests this particular encoding
and a domain containing both preparations. It leaves open encodings that
retain more color moments, larger physical blocks, restricted preparation
families, different microscopic generators, or an interpretation in which
these labels include additional physical information. None is silently
excluded. The positive quantum Hamiltonian constructions already explored
are different laws and are not refuted by this calculation.

This witness is raw research, not a completed no-go-discipline package or
an independently audited result. Its purpose is to make the missing
classical-to-quantum compatibility condition concrete for the next campaign.

