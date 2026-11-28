# Running and Gaussian-transport tests for witness item 11

Author: openai/gpt-6-astra/max macbook-codex, 2026-11-01.
Source: 45b3989670a64c7d0ce7b293a56ed6beb37dee14.
Status: discharged finite-dimensional identities and conditional implications;
no continuum Yang–Mills construction, independent review, audit or numerical run.
Credit: the quadratic transport is gate `witness-3b7fd4e57.md`, D2 (L3).
It is rebuilt below rather than taking that gate's simulations as a premise.
The conditional dilation-mixture test and the elementary flow summation are
written here. No lemma from an external paper is used.

## A. The leading logarithm [implication]

Assume precisely H-SCALE and H-FLOW of witness Text 8.1. Count m towards
the ultraviolet from the fixed physical top. After shifting the origin to m_0,
write u_m=gamma_m^(-2), w_m=u_m-d_m. Then

    w_m = w_0 + m b_W log L + sum_(ell=1)^m rho_ell,
    |d_m|<=C_0,
    |rho_ell|<=C gamma_ell [1+log(1/gamma_ell)]^q,
    (b_W/2)log L <= w_ell-w_(ell-1) <= (3b_W/2)log L.

The last bounds and bounded d give c(ell+1)<=u_ell<=C'(ell+1), with positive
constants after absorbing finitely many top levels. Therefore

    |sum rho_ell| <= C'' sqrt(m+1)[1+log(m+2)]^q = o(m),
    u_m = b_W m log L + O(sqrt(m+1)[1+log(m+2)]^q)+O(1).       (A1)

For the sum bound use log(1/gamma_ell)<=C log(ell+2) and
sum_(ell=1)^m ell^(-1/2)<=2 sqrt(m), obtained by comparison with the
integral of t^(-1/2). Thus gamma_m^(-2)/(m log L)->b_W. If an observable
anchor gives g_m/gamma_m->1, the same limit holds for g_m. This proves
only the implication: the value of b_W and all flow assumptions remain inputs.

The stronger difference statement does not follow: choose rho_m=0,
d_m=c(-1)^m, and u_m=u_0+b_W m log L+d_m-d_0, with u_0 sufficiently large.
This obeys the displayed hypotheses, but u_(m+1)-u_m oscillates by 2c.
This is a counterexample to that stronger inference, not to (NT2-R).

## B. Finite-cutoff cubic Gaussian transport [discharged]

Let X be a finite-dimensional centred Gaussian with positive covariance C,
with gauge zero modes removed by a fixed chart. Let F_3 be a homogeneous
cubic with tr(C Hess F_3)=0. This last property holds for the colour-isotropic
SU(2) cubic: contracting any two colour indices in its epsilon tensor gives
zero. Define

    B(X)=-(1/3) C grad F_3(X),       A_h=h X+h^2 B(X).

For a polynomial f, integration by parts against the Gaussian density gives

    E[Df(X) B(X)]
       = -E[f(X){div B(X)-X.C^(-1)B(X)}]
       = -E[f(X) F_3(X)].                                     (B1)

Indeed div B=0 and X.C^(-1)B=-(1/3)X.grad F_3=-F_3 by homogeneity.
The boundary terms vanish because polynomials times a Gaussian density are
integrable. This proves (B1) without a perturbative measure or a simulation.
With nonzero tadpoles one must first specify the Wick-ordered cubic and its
associated linear correction; no such correction is hidden here.

Let a bounded smooth holonomy observable have Taylor terms f_p,f_(p+1),...
at A=0. Taylor's integral remainder is integrable under A_h: derivatives of
products of SU(2) exponentials of fixed finite paths are bounded and B is a
polynomial. Consequently

    E f(A_h) = h^p E f_p(X)
       +h^(p+1){E f_(p+1)(X)-E[f_p(X)F_3(X)]}+O(h^(p+2)).     (B2)

All constants here depend on the finite regulator and the fixed paths. For T,
p=3 and E t_3=0, so

    E T(A_h)=h^4{E t_4-E[t_3 F_3]}+O(h^6).                   (B3)

The improvement from h^5 to h^6 follows by expanding one more order: the
law of A_h equals the law of A_(-h), by X->-X and B(-X)=B(X), so every odd
Taylor coefficient of its expectation vanishes. For B and k energies,
the leading coefficients are their Gaussian values, with remainders
O(h^4) and O(h^(2k+2)), respectively. All triples in the fixed regulator
obey (B3), not just a selected rectangle.

In the Wilson normalization F_2=(1/8) sum |dX|^2, C=4G and
F_3=(1/4) sum_p Phi_p(X).Q_p(X). Thus A_h is precisely
`a-(1/3)G grad S3tilde(a)` with a=hX and
S3tilde=sum Phi.Q as in the gate. The sign and factor follow from (B1).

**Running test [implication, finite-cutoff marginal version only].** Choose
h_m^(-2)=c+b_W m log L. At a fixed regulator let c_*=E e_p,2>0. Then the
observable anchor gives g_m^2=E s_p(A_hm)/c_*=h_m^2(1+O(h_m^2)), and hence
(NT2-R). Equations (B2)-(B3) give all the finite-family matching clauses with
that g_m and with the cubic-vertex contribution included. Running has not
removed the field-redefinition ambiguity.

**Gap / exact boundary.** Separate draws of these laws at different m,
or their product on a scale-labelled space, do NOT give
M_*mu_(m+1)=mu_m for the specified block map. That equality, for every
finite-window continuous test f,

    E_mu_(m+1)[f(M(V))] = E_mu_m[f(V)],                        (B4)

is the missing consistency equation. Uniform infinite-volume estimates and
reflection positivity of the nonlocal map are also unproved. A Gaussian
source is not by itself a proof of RP for observables depending on both
sides of a reflection plane. Thus (B3) is not advertised as a counterexample
to the coherent NT2 of Text 8.1, or as a free local QFT equivalent to it.
Nor does being a Gaussian push-forward alone prove a law is not Yang–Mills.

## C. Local nonlinear and fixed-amplitude mixture attacks [discharged at stated scope]

First test the gate's square-symmetric Proca covariance itself. Let
Cov(X_b^a,X_c^d)=C_bc delta_ad on the four bonds of one plaquette,
with all C_bb=v. Write epsilon_b for the circulation signs,
L=sum_b epsilon_b X_b, r_b=Cov(L^a,X_b^a) (no colour sum), and
u=Var(L^a)>0. Rotation of the oriented square makes the covariance in
circulation-oriented coordinates circulant. Hence r_b=lambda epsilon_b
with lambda>0 and u=4 lambda. Positivity follows from the nonzero
variance of the circulation in the massive Proca covariance.

Put Phi_kappa=sum_b epsilon_b X_b(1+kappa |X_b|^2). Direct Gaussian
conditioning L=(r_b/v)X_b+eta_b, with eta_b independent of X_b and
variance u-r_b^2/v, gives

    E[L.X_b |X_b|^2]=15 v r_b,
    E[|L|^2 L.X_b |X_b|^2]=30 r_b^3+75 u v r_b.

Here E|X_b|^(2n) follows from the recurrence below. Expanding the two
radial moments to first order therefore gives

    d/dkappa at 0 {E|Phi_kappa|^4
                    -(5/3)(E|Phi_kappa|^2)^2}
       =120 sum_b epsilon_b r_b^3=480 lambda^3>0.             (C1)

At C=I this is 480, agreeing algebraically with four times the linear
coefficient 120 in the independent-link formula below. This is an author
cross-check of the two derivations, not an independent review or a code run.

Both moments are polynomials in kappa, so their excess is positive for
all sufficiently small fixed kappa>0 (the neighbourhood may depend on C).
The plaquette-energy mean and second moment consequently cannot both match
the Gaussian leading coefficients in ANY scalar coupling normalization.
For a scale family with this fixed dimensionless covariance and fixed kappa,
the excess persists when its overall amplitude runs to zero. No uniform
neighbourhood of kappa over scale-dependent covariances is asserted.
This is a direct small-kappa rejection of that symmetric Proca law,
not a claim for every kappa or every covariance. No Proca spectral or RP
property is used beyond that covariance symmetry and positivity.

For a concrete local L1 subcase take independent colour vectors
X_b~N(0,I_3) and Y_b=X_b(1+kappa |X_b|^2), kappa>0. With R=|X_b|^2,
integration by parts in the three Gaussian coordinates gives
E R^(n+1)=(2n+3)E R^n and E R^0=1: sum the identities
E[X_i (X_i R^n)]=E[partial_i(X_i R^n)] over i=1,2,3.
Thus

    E|Y|^2=3+30 kappa+105 kappa^2,
    E|Y|^4=15+420 kappa+5670 kappa^2+41580 kappa^3+135135 kappa^4,
    E|Y|^4-(5/3)(E|Y|^2)^2
      =120 kappa+3120 kappa^2+31080 kappa^3+116760 kappa^4>0.

For the linear plaquette flux Y_1+Y_2-Y_3-Y_4 the last excess is four times
this value. To verify additivity, expand the fourth moment of a sum of two
independent centred isotropic vectors; their mixed contribution is
(10/3) E|Y|^2 E|Z|^2, exactly cancelled by the corresponding term in
(5/3)(E|Y+Z|^2)^2. The single-plaquette energy first and second moments
therefore cannot both have their Gaussian leading values under any scalar
rescaling. Adding a nominal running h_m does not change that normalized
excess. This proves rejection for this concrete fixed-kappa local law;
it is not a calculation for every Proca covariance or every sign of kappa.

For L2, if a Gaussian flux covariance is multiplied by an independent
s taking 1-delta and 1+delta with equal probabilities, 0<delta<1, its
leading energy mean is unchanged and its leading energy second moment is
multiplied by E s^2=1+delta^2. Its normalized energy kurtosis is
(5/3)(1+delta^2), so anchoring g by the mean cannot remove the discrepancy.
This tests the gate's colour-isotropic Proca mixture as well as a Maxwell
mixture; any additional mismatch of its covariance does not repair this
one-plaquette ratio. Fixed disorder amplitude fails (NT2-M).

If kappa_m or delta_m tend to zero, this obstruction can vanish. The above
argument does not rule out such laws, nor does matching the Gaussian moments
supply K_vert. Combining a vanishing-amplitude mixture with B leaves the
finite-cutoff marginal ambiguity. No exhaustive exclusion is claimed.

## D. A coherent scale mixture [conditional counterexample to QFT identification]

Assume a state omega satisfying coherent NT2 exists and clusters for its
bounded local observables. Assume its fixed block scheme is covariant under
the discrete dilation that identifies a template at r_m with the same
template at r_(m+1). This is a further structural assumption, not a theorem
about either producer's actual map. Write omega'=omega composed with that
dilation, and nu=(omega+omega')/2 on the SAME observable algebra.

Positivity, all block-consistency identities, translation/hypercubic
invariance and RP (if omega has them) are linear identities/inequalities
preserved by this mixture and by a positive dilation. Its anchored coupling is

    g_nu,m^2=(g_m^2+g_(m+1)^2)/2.

(NT2-R) implies g_(m+1)/g_m->1. Therefore for every fixed integer k,

    (g_m^(2k)+g_(m+1)^(2k))/2 = g_nu,m^(2k)(1+o(1)).

Apply this identity to each raw energy product, B and T. Their common,
scale-independent tree coefficients are unchanged, and their o(1) relative
errors stay o(1). Thus nu satisfies the ENTIRE proposed NT2, including its
observable running and scale consistency. No cross-scale factorization
was assumed. The same fact holds for every fixed finite-template leading
order, not just the list in Text 8.1.

There must be an m with g_m^2!=g_(m+1)^2: otherwise the positive sequence
would be constant and could not tend to zero. Choose A=s_p at that scale,
with a=omega(A), a'=omega'(A), a!=a'. Clustering in the two components gives

    lim_(|x|->infinity) Cov_nu(A,tau_x A) = (a-a')^2/4 > 0.    (D1)

This is a static disorder sector, incompatible with the clustering vacuum
of an axiomatic vacuum QFT. If omega has NT1, so does nu: choose an OS
vector with strictly decreasing positive-time autocorrelation in omega;
the corresponding autocorrelations in both components are nonincreasing,
so their positive mixture cannot become constant. The added sector does
not supply a mass gap or a unique vacuum.

**Scope.** This is an exact construction GIVEN the stated existence,
clustering and dilation hypotheses. It does not construct an unconditional
4D continuum measure; none is claimed. It shows that even coherent NT2
cannot enforce vacuum selection or complete Yang–Mills identification when
a desired solution exists. It does not show that the specified Wilson
trajectory produces nu. The Wilson-origin condition in T1 is additional.
