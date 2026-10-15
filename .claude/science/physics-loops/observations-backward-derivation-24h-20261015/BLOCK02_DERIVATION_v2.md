# Primitive observation errors and finite radar-bin constraints

Author /root, 2026-10-15. Conditional mathematical extension of the checked
block-01 inverse. No observed metric, actual clock calibration or statistical
confidence level is supplied here. No novelty is claimed for Cauchy–Schwarz or
Lipschitz estimates; their role is to expose precisely what finite measurements
can and cannot replace in this proposed scalar reconstruction.

Exact target: express the relative scalar inverse on a shared observation label,
derive a deterministic error bound retaining radius and shared-clock errors,
and obtain a one-sided integral constraint from finite radar increments without
interpolating their derivative. All physical class premises of block 01 persist.

## 1. Shared label and primitive quantities

Use a fixed outward monotone record label z on [z0,z1]. Values from the different
channels must refer to the same physical configurations. This alignment is an
explicit condition, not an inference from the present formulas. Let

    r=r(z)>0, q=dr/dz>0,
    rho=rho(z)=c*tau_roundtrip(z)/2, P=d rho/dz>0,
    R=nu_received(r0)/nu_emitted(r)>0,
    Omega=dphi/dtau0, A=1-r^2 Omega^2/(c^2 R^2)>0,
    D=R^2-r^2 Omega^2/c^2=R^2 A.

r is independently identified areal radius; rho uses the reference static
clock. Omega comes from a separate circular-orbit measurement, but the derived
local speed uses the same measured R. No stochastic independence of those
derived quantities is asserted. R(z0)=1 in the ideal convention. Timing,
frequency, radius, orbit and cross-channel alignment errors remain real inputs.
The smooth underlying scalar chart is that of block 01, with nonzero d and u;
the observable functional below can also be evaluated on lower-regularity
positive data without claiming those data solve the field equations.

The inverse from block 01 reads

    F(r)/F(r0) = [S/S0] [r0/r] [A0/A]
                exp integral_(r0)^r R^2 S^2/(s A) ds,
    S=d rho/dr=P/q.

On the common z label this becomes

    L(z)=log(F(z)/F(z0))=E(z)-E(z0)+integral_(z0)^z J(t)dt,
    E=log P-log q-log r-log D+2 log R,
    J=R^4 P^2/(q r D).                                      (1)

Derivation: substitute S=P/q, dr=q dz and A=D/R^2 in the endpoint
and integral factors separately. The R appearing twice in D and explicitly
in (1) is the same function. In particular, replacing its two occurrences
with independent fitted channels changes the proposed observation map.

Equation (1) is invariant under a common smooth relabeling of z whose
derivative is strictly positive throughout the interval:
P and q acquire the same derivative factor, their endpoint quotient cancels,
and J dz is unchanged. It is not invariant under independently shifting the
records of different channels, or under changing the physical radius scale
while leaving all other dimensional data fixed.

## 2. A deterministic primitive-input bound

Compare two aligned sets of functions, unadorned and hatted, on the same fixed
label interval. Both obey common certified bounds

    r>=r_*>0, R>=R_*>0, q>=q_*>0, P>=P_*>0, D>=D_*>0,
    r<=r^*, R<=R^*, |Omega|<=O^*, P<=P^*.

Let uniform absolute differences of r,R,Omega,P,q be e_r,e_R,e_O,e_P,e_q.
No independence or probability distribution is required. Elementary product
differences give the valid (possibly conservative) bound

    e_D = 2 R^* e_R
          +2 r^* (O^*)^2 e_r/c^2
          +2 (r^*)^2 O^* e_O/c^2.                         (2)

For example, split rhat^2 Omegahat^2-r^2 Omega^2 into its radius
and orbit differences, and bound each difference of squares by twice the
common upper bound times its absolute discrepancy. Actual D error can be
smaller due to shared errors; (2) needs no cancellation to hold.

Define

    K_R=4 (R^*)^3 (P^*)^2/(q_* r_* D_*),
    K_P=2 (R^*)^4 P^*/(q_* r_* D_*),
    K_q=(R^*)^4 (P^*)^2/(q_*^2 r_* D_*),
    K_r=(R^*)^4 (P^*)^2/(q_* r_*^2 D_*),
    K_D=(R^*)^4 (P^*)^2/(q_* r_* D_*^2).

Then

    |Lhat(z)-L(z)| <= B(z),
    B(z)=2e_P/P_*+2e_q/q_*+2e_r/r_*+2e_D/D_*+4e_R/R_*
         +|z-z0|(K_R e_R+K_P e_P+K_q e_q+K_r e_r+K_D e_D).  (3)

Proof: for the endpoint terms, |log a-log b|<=|a-b|/a_*.
There are two endpoints, and the coefficient of log R is two. For the
integral, view J as a smooth function of the five positive arguments
(R,P,q,r,D) in their rectangular domain. Its absolute partial derivatives
are bounded by the displayed K values. Telescope one coordinate at a time
or integrate its gradient along the straight segment in that positive box.
The intermediate tuples need not be physical data: they are used solely to
bound this rational function. Substitute (2), integrate the resulting uniform
bound over z, and add the endpoint estimates. This proves (3). The physical
correlation between D and R was never replaced by an independence premise.

Thus the inferred relative F differs by at most exp(+/-B). These are bounds
on aligned functions including the derivatives P and q, not bounds inferred
from finite noisy samples alone. Near D=0, q=0 or an unbounded inferred P the
certificate deteriorates. No chosen smoothness penalty is a derivation of its
own error or derivative bounds. A bound on record misalignment would additionally
require controlled variation of the channel functions; it is not included.

## 3. What finite radar increments already constrain

Return to physical r and define the positive weight

    w(r)=R(r)^2/[r A(r)],    I_ab=integral_a^b w(r) S(r)^2 dr.

For a<b in the same chart, a radar increment is
Delta rho_ab=integral_a^b S dr. Cauchy–Schwarz applied to
sqrt(w)S and 1/sqrt(w) gives

    I_ab >= (Delta rho_ab)^2 / H_ab,
    H_ab=integral_a^b 1/w dr=integral_a^b r A/R^2 dr.         (4)

Equality holds for S(r)=k/w(r) on that interval. This is a mathematical
equality case, not a chosen physical radar curve. For a partition, add the
bin lower bounds. Refinement never weakens the bound when increments and H
are exact: (x+y)^2/(h+k)<=x^2/h+y^2/k for h,k>0, with equality
when x/h=y/k. This follows by subtracting the two sides to obtain
(k*x-h*y)^2/[h*k*(h+k)].

With uncertain increments, if their true positive values are at least
delta_j^- and H_j<=H_j^+ with H_j^+>0, the rigorous lower bound is
sum_j (max(0,delta_j^-))^2/H_j^+. Known uniform w>=w_*>0
and bin width at most h^+ allow H_j^+=h^+/w_*. These bounds must come
from measurements and their stated domain, not from an assumed interpolation.

The exponent I contributes to

    log(F(b)/F(a))=log[S(b)/S(a)]-log(b/a)+log[A(a)/A(b)]+I_ab.

Equation (4) therefore constrains a combination with endpoint slowness and
orbit factors still present. It is not an endpoint-independent F measurement.
For R=1, Omega=0, w=1/r, one exact-bin lower bound is

    I_ab >= 2(Delta rho_ab)^2/(b^2-a^2).                    (5)

This zero-speed example is only a mathematical static-map control, as in
block 01. No observed set of circular orbits is implied.

## 4. Explicit finite-sample ambiguity retained as a boundary

In one unsampled open gap (a,b), choose a smooth baseline S0>0 equal to 1
near both ends, with integral S0 dr=(b-a)-A for fixed 0<A<b-a.
Let psi>=0 be a nonzero C-infinity bump of compact support in (-1/2,1/2),
with integral psi=1. Place its center rc inside the gap and set

    S_epsilon(r)=S0(r)+(A/epsilon)psi((r-rc)/epsilon).

For small epsilon its support remains in the gap. Every curve is smooth,
positive, matches S=1 near the gap endpoints and has the same radar increment
b-a. Define rho by integrating from the gap's left endpoint, and set S=1
outside the gap. Every sampled rho value and even sampled endpoint S value
is unchanged. Nevertheless, for a common positive lower bound w_* on the gap,

    integral_a^b w S_epsilon^2 dr
        >= w_* A^2/epsilon * integral psi(t)^2 dt.          (6)

The right side grows without bound. This is an explicit family of smooth
observation functions with identical finite samples and increasing quadratic
integral. It identifies the exact missing derivative/shape-control input in
turning those samples into (3). It is not a family of demonstrated healthy
solutions of one scalar action: some profiles can leave the nonzero-u chart.
It is not a proof against measurements supplemented by dynamics, derivative
bounds or an independently justified response bandwidth. Those would add
information, whose origin must be derived or measured.

## 5. Consequence for the campaign and checks

The assumed exact areal coordinate is now an explicit input function r(z) with
value and derivative errors, and the shared redshift error is carried without
declaring independent derived channels. Finite radar increments provide the
one-sided exponent constraint (4), requiring no selected S interpolation.
Neither development selects the action, initial state, absolute F or a shared
F range. No new empirical observations were opened for this calculation.

Checks to execute: independently pull (1) back to the block-01 metric formula;
verify relabeling and the exact Cauchy refinement identity; test (2)–(3) on
jointly perturbed analytic channels against bounds with mathematically certified
envelopes; detect wrong Jacobian, inverted endpoint and shared-clock omissions;
and evaluate the finite-bin inequality with equality and strict examples.
Numerical examples corroborate the analytic proofs and do not prove a universal
bound. Preserve the constructed ambiguity without promoting it to a global
physical no-go. Obtain a focused independent check before extensive reuse.

Next physical obligation: derive a cross-environment normalization transport from
material stress and a justified connected field solution, rather than setting
C1=C2. A first candidate is to retain the material angular-minus-time stress
difference in the inverse equation and test whether regularity fixes any remaining
integration constant. This is a planned calculation, not an already checked result.
