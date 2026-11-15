# Injectivity of the full infinite-volume physical transfer at the endpoint

Author supplement to [the local-block construction](../MASS_GAP_LOCAL_BLOCK_ASTRA.md),
sections 1, 3-5. It strengthens the original link-reflection null-quotient
argument by proving that the transfer has no kernel on the entire invariant
slice Hilbert space. The first frozen endpoint draft is preserved as
[massgap_block_initial_endpoint.txt](massgap_block_initial_endpoint.txt), SHA256
`f7e1405bb263ea82898c96ca0c80edc8afa90aa76d45a6676f7ccab34fef0fe6`.
Both versions remain author candidates pending independent review. This is
still a fixed-spacing result for SU(N), N>=2, 0<beta<=1/32, a>0, and does
not supply the continuum mass-gap estimate or a new physical premise.

## 1. A canonical unprojected kernel for every boundary field

Use the exact open-time temporal-gauge slab representation (12), with
spatial plaquettes at coefficient beta and temporal pairs
beta w(U_(e,t) U_(e,t+1)^dagger). The free-link majorant has row 14 beta<1.
The same existence and comparison construction as (15)-(17), on the
countable half-space of times t>=1, gives a unique Gibbs probability
rho_U^+ for EVERY bottom configuration U in X=SU(N)^(E(Z^3)).
All boundary fields are allowed; this is not an almost-everywhere choice
of conditional versions. For continuous local functions the finite-volume
expectations are Cauchy by the comparison tails, uniformly in boundary
values. Their consistent limits define rho_U^+, and their dependence on U
is measurable (indeed continuous for local tests). The resulting family is
a probability kernel on the standard Borel countable product space.

Let Q_U be its first-slice marginal. The unique full temporal-gauge Gibbs
state has a stationary slice marginal pi. Its finite spatial-volume
marginals are the limits from the same unprojected A k A transfer, hence
pi is the same slice marginal as in the main construction. Conditioning
on U_0 separates the two half-spaces; uniqueness identifies the future
conditional with rho_U^+. Thus

    pi Q=pi.                                                       (I1)

Time reversal gives reversibility. Positivity of the finite unprojected
A k A quadratic forms passes on all local slice functions, so Q is a
positive self-adjoint contraction on L2(pi). Simultaneous spatial gauge
transformations commute with Q. On the COMPLETE invariant subspace its
action equals the projected physical transition P_infinity, by the exact
finite identity (19)-(20) followed by the local limits. This construction
does not identify Q and P_infinity on gauge-variant functions.

If U' differs from U on a finite set B of b links, the change in the
half-space weight is exactly the bounded first-slice term

    H_(U,U';B)(V)=beta sum_(e in B)
           [w(U'_e V_e^dagger)-w(U_e V_e^dagger)],
    |H_(U,U';B)|<=2 beta b.

The probability exp(H) rho_U^+/rho_U^+(exp(H)) has precisely the Gibbs
specification with bottom U'. Uniqueness therefore proves, for ALL U,U',

    Q_(U')(dV)= exp[H_(U,U';B)(V)] Q_U(dV)/Q_U(exp[H_(U,U';B)]).    (I2)

In particular its Radon-Nikodym derivative lies between exp(-4 beta b)
and exp(4 beta b). The normalizer is retained. This proves the limiting
tilt identity directly; it is not inferred from weak convergence of
arbitrarily chosen conditional versions. No global infinite-volume
wavefunction psi relative to product Haar is postulated.

## 2. Local finite-energy bounds provide the common measure sets

For finite spatial volume the main construction (3) implies, for each
fixed exterior, the conditional density bounds

    exp(-L_B) <= d pi_Gamma(U_B | U_out)/d Haar_B <= exp(L_B),
    L_B=2 beta p_B+4 beta b.                                      (I3)

For a fixed finite B, its b and p_B do not grow with Gamma. Apply (I3) to
nonnegative local test functions f(U_B), g(U_out), integrate, and pass to
the slice limit. Cylinder approximation and the monotone-class theorem
then give the same measure domination for all bounded nonnegative tests.
Disintegration yields

    exp(-L_B) Haar_B <= pi(dU_B | U_out) <= exp(L_B) Haar_B         (I4)

for pi_out-almost every exterior. This use of finite-energy comparability
transports null sets. It is not an assertion that such comparability
proves mixing.

Assume F in L2(pi) and QF=0 pi-almost everywhere. Stationarity gives
Q_U|F|<infinity for pi-almost every U. Let N be the union of the exceptional
sets for these two statements, so pi(N)=0. Choose increasing finite blocks
B_j exhausting all spatial edges. For each j, disintegration of pi(N)=0
and (I4) imply that, for pi_out-almost every exterior z,

    Haar_(B_j){u : (u,z) belongs to N}=0.                          (I5)

Intersect these exterior-good sets for the COUNTABLE sequence B_j and
remove N. This gives one set X_0 with pi(X_0)=1. For U in X_0, all the
following arguments hold simultaneously for every j. Equation (I2) and
Q_U|F|<infinity also make Q_(u,U_out)F well-defined for EVERY u, because
the change of probability is bounded. For Haar_(B_j)-almost every u,
(I5) says its value is zero.

## 3. Positive character multipliers force all conditional measures to vanish

Fix U in X_0 and B=B_j. Define the finite signed (or complex) measure on
G^B by

    alpha_(U,B)(dV_B)
      = exp[-beta sum_(e in B) w(U_e V_e^dagger)]
        E_(Q_U)[F | V_B] Q_U(dV_B).                               (I6)

It is finite because Q_U|F|<infinity and the exponential is bounded on a
finite block. The zero expectations from (I2),(I5), multiplied by their
positive denominators, say that

    integral exp[beta sum_(e in B) w(u_e V_e^dagger)]
             alpha_(U,B)(dV_B) = 0                               (I7)

for Haar_B-almost every u. The left side is a continuous convolution.
For the supplied SU(N) Wilson weight at beta>0, every Peter-Weyl
convolution multiplier is c_R(beta)/d_R>0, as proved in the reviewed
[finite-transfer source, section 1](../MASS_GAP_CONSTRUCTION_ASTRA.md).
The product kernel on B therefore multiplies each matrix Fourier
coefficient by a strictly positive product. Equation (I7) forces every
matrix Fourier coefficient of alpha_(U,B) to vanish. Peter-Weyl matrix
coefficients are uniformly dense in continuous functions on the compact
finite product G^B, so uniqueness of finite signed measures gives
alpha_(U,B)=0. The bounded strictly positive multiplier in (I6) then gives

    E_(Q_U)[F | V_(B_j)]=0    Q_U-almost everywhere, for every j.  (I8)

This argument applies to signed measures; it does not assume that their
densities are in L2(Haar). Operator nonnegativity without strictly nonzero
multipliers would not suffice. At beta=0 the Haar kernel supplies exactly
that counterexample.

For each fixed U in X_0, F is in L1(Q_U), and the finite coordinate sigma
algebras of the B_j exhaust the output sigma algebra. The L1 martingale
convergence theorem applied to (I8) gives F=0 Q_U-almost everywhere.
Finally (I1) gives

    integral |F| d pi = integral pi(dU) Q_U|F| = 0.                (I9)

Thus Q is injective on the ENTIRE slice L2(pi), and its restriction
P_infinity is injective on the entire gauge-invariant slice Hilbert space.
There has been no uncountable intersection of measure-one sets, no assumed
limit of finite-volume injectivity, and no use of a single observable
witness as an injectivity surrogate.

## 4. Physical consequence and checks

The full invariant slice space is therefore the closure of
Ran(P_infinity^(1/2)). The link-reflection OS construction in the main note
is canonically unitarily equivalent to that entire space, and
H=-a^(-1) log P_infinity is densely defined there. The main contraction and
plaquette witness give the finite, positive spectral interval (30), with
no further discarded slice directions. All positive-time invariant local
products are included before the reflection quotient. This still concerns
fixed beta,a, and proves no cutoff-uniform continuum statement.

The [additional criteria](massgap_block_injectivity_criteria.md),
[finite runner](massgap_block_injectivity_exact.py) and
[results](massgap_block_injectivity_results.json) check the finite tilt,
normalization and Fourier controls only. They do not test the limiting
measure, the Fubini/common-set step or martingale convergence. Those are
analytic steps above and require independent review with the main unit.
