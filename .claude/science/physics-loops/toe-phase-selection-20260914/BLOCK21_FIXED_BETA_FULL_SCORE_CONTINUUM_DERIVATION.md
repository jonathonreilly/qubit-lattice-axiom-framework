# Fixed-coupling full-score continuum limit for the supplied Haar Villain law

Personal theorem candidate, 2026-09-15. This combines the block21 analytic
proof candidates with the provisional carrier and free-cube filling inputs
from PR8133 at f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8. Independent review
of this argument and those inputs remains pending. No retained status,
finite-clock phase, native law or axiom update is asserted.

The intended advance over the earlier growing-coupling construction is
that beta is held fixed while the observation scale changes. The supplied
microscopic law here still uses continuous Haar link angles. It is a
specific Abelian comparison model, not the N=3 penalty Hamiltonian and
not a derivation of that law from the framework axioms.

## 1. Proposed statement and exact state selection

Let theta_e be U(1) link angles on a free four-dimensional cubic box, with
Villain plaquette weight

 w_beta(u)=sum_(k in Z) exp[-beta(u-2pi k)^2/2].

Adjoin conditionally independent image integers and define

 X_p=sqrt(beta)[(d_1 theta)_p-2pi k_p],
 Y_p=E[X_p|theta]
    =-beta^(-1/2)(d/du)log w_beta(u) at u=(d_1 theta)_p.

The definition is invariant under changing the representatives of link
angles. Y is a bounded smooth periodic plaquette function. Set
v_beta(u)=Var(X_p|u); it is continuous, periodic and strictly positive.

Choose beta large enough for the carrier expansion, delta<1/2, and
k3 delta<1 in the preconditioned Gaussianity lemma. All constants are
uniform over free cubes. Since delta tends exponentially to0 with beta
and k3 is finite and independent of beta and volume, this gives a finite
threshold beta0. No numerical value of the Riesz constant is guessed.

First take the thermodynamic limit of the finite law averaged over a
uniformly chosen root in the box. Then, in the resulting stationary law,
take lattice sources h_a=J_a f for smooth compactly supported real
two-forms f on R4, with the usual four-dimensional normalization a^2.
Cell averages or sampled smooth values have the same limit.

For definiteness set
J_a f_I(x)=a^(-2) integral_(a(x+[0,1)^4)) f_I(y)dy for each orientation I.
Then ||J_a f||2<=||f||2, ||J_a f||3^3=O(a^2), and the associated
piecewise constant random distribution pairs with f exactly by J_a f.
Orientation-dependent bounded cell-center shifts give the same limit.

Conditional on the written upstream and block21 proofs being correct,
the proposed conclusion is a spatially mixing selected Gibbs plaquette
state and joint Gaussian limits of all the full flux and score tests:

 X(J_a f) -> X_cont(f), Cov(X_cont)=I-kappa R,
 Y(J_a f) -> Y_cont(f), Cov(Y_cont)=a_contact I+kappa P,

 P=d Delta^(-1)d*, R=I-P=d*Delta^(-1)d on two-forms,
 a_contact=1-kappa-vbar>=0,
 vbar=E v_beta((d_1 theta)_p)>0,
 1/(1+delta)<=kappa<=1-vbar<1.                         (1)

The same limits hold for all joint moments and locally as distributions
in H^(-s) for s>2. The Gaussian continuum score has a direct positive-time
OS reconstruction with two transverse photons and energy |p|. The white
contact term contributes only the vacuum to that reconstruction.
This is a statement about the identified continuum limit; microscopic
periodic-state matching and the finite-clock phase are additional work.

## 2. Inputs and what each discharges

The carrier-preserving charge expansion and its actual free-cube filling
bridge are the two explicit provisional upstream premises. They produce
a positive auxiliary measure with a translation-covariant, summably local
gradient extension, uniform Schur Hessian bound delta and third-influence
bound M3. Full carrier mass is retained even when net charge cancels.

BLOCK21_PRECONDITIONED_GRADIENT_GAUSSIANITY.md gives the finite-time
source-variation proof and uniform ell3 remainder, plus the explicit
free-cube reflection and direct periodic Riesz bound.

BLOCK21_THERMODYNAMIC_MATCHING_DERIVATION.md constructs the selected
mixing auxiliary state as a factor of stationary Gaussian OU noise,
matches it to averaged free-box Gibbs measures, passes their covariance
response, and uses two replicas to prevent a hidden root-dependent
variance mixture when passing the Gaussian remainder.

BLOCK21_STATIONARY_SPECTRAL_RESPONSE_DERIVATION.md separates the invariant
environment frequency, eliminates its fluctuations, and uses the full
two-form signed-permutation symmetry to identify the auxiliary covariance
limit as kappa R. It does not replace the Hessian by its expectation.

The finite flux map is independently derived and checked in
BLOCK21_FIXED_LAW_FULL_FLUX_BRIDGE_DERIVATION.md. The remaining steps are
spelled out below so that an auxiliary Gaussian field is not silently
substituted for the actual physical observable.

## 3. Exact flux identity in gradient variables

Write B=d_2, H_3=B B*+d_3*d_3, G_3=H_3^(-1), c=1/32, and
T_r=(I-c H_r)^(-1). The auxiliary variable is

 omega=beta^(-1/2)(d_2*phi,d_3 phi),
 K=(d_2*,d_3)(G_3-cI)(d_2*,d_3)*.

It has Gaussian reference covariance K on its compatible range and the
even carrier potential R_L. Its first block is a two-form. The exact
finite characteristic identity is

 E exp[i(h,X)]
 =exp[-||h||2^2/2-c(Bh,T_3 Bh)/2]
    E_mu exp[-(T_2 h,omega_first)].                    (2)

The right side uses a real MGF. The cochain identity T_3 B=B T_2 fixes
both the source and its normalization. The finite auxiliary law obeys
E exp(omega(j))<=exp[(j,Kj)/2]; the physical X and Y each obey the
centered bound exp(||h||2^2/2). These follow from the exact Gaussian/theta
identities and conditional Jensen inequality.

The matching theorem passes(2) to infinite volume. T_r have exponentially
decaying kernels and norm at most2 on ell2 and ell3; their free-box bulk
limits follow from their finite-range Neumann series. The MGF bound
controls source truncations. Thus the selected full-flux local law is
uniquely specified by the matched auxiliary law.

For macroscopically rescaled h_a, ||B h_a||2=O(a). The finite-time
Gaussianity bound, inherited by the infinite auxiliary state through
the replica argument, gives

 |log E exp[-(T_2 h_a,omega_first)]
       -Var((T_2 h_a,omega_first))/2|
 <=(4/3) M3 C3^3 ||h_a||3^3=O_beta(a^2).               (3)

The spectral response theorem gives the quadratic limit kappa(f,Rf).
The T_2 correction vanishes because its multiplier tends to I at zero
frequency; boundedness and smooth-source Fourier tails justify passage.
The explicit second term in(2)'s prefactor also vanishes. Hence

 E exp[i X(J_a f)] -> exp[-(||f||2^2-kappa(f,Rf))/2].   (4)

Every finite real linear combination of tests obeys the same estimate,
so this is joint Gaussian convergence, not merely a two-point bound.
The spectral upper and score lower inequalities give
1/(1+delta)<=kappa<=1 at this stage.

## 4. The selected physical state is mixing and Gibbs

For compact sources h,g separated by a lattice translation z, the cross
term in the Gaussian prefactor of(2) tends to0. Its nonlocal part has
exponential range. The two auxiliary exponentials with sources T_2 h
and the translate of T_2 g decorrelate because the auxiliary noise-factor
state is mixing. First truncate the sources; then control the L2 error
with their exponential-moment bounds. Thus the characteristic cylinder
observables of X are mixing. Such observables are dense in the L2 spaces
of finite coordinate marginals, so bounded local observables mix as well.

The plaquette angle is X_p/sqrt(beta) modulo2pi. Its law, Y, and v_beta
are local measurable factors and inherit mixing. In particular their
translation-invariant sigma field is trivial. Cubic symmetry gives the
same expectation vbar for each of the six orientations.

To match an actual link-angle Gibbs state, retain theta jointly in the
finite root averages and extend unused outer links by independent Haar
angles. Compactness of the link variables and the flux moment bounds
give a joint subsequential limit. For each fixed finite link region,
almost every selected root places that region and its neighboring
plaquettes inside the original box. Its exact finite conditional Gibbs
identity therefore passes to the limit. The specification is continuous
and bounded on the compact angle variables, since the positive smooth
Villain weights have a positive minimum. Thus the limiting theta law
is a Gibbs state of the supplied infinite Haar Villain interaction.

Local gauge invariance is preserved. Every finite conserved integer link
current bounds a finite integer plaquette chain in Z4. Its character is
therefore determined by the plaquette law. Nonconserved characters have
zero expectation by local gauge invariance. Fourier polynomials then
determine the link law from its plaquette law. This identifies the chosen
gauge-invariant link state without claiming uniqueness for arbitrary
boundary-selected or externally tilted Gibbs states.

## 5. Conditional image noise and the score

Put xi_p=X_p-Y_p. Conditional on the full plaquette-angle configuration,
the image variables remain independent, centered, with variances
v_beta(u_p). Their third absolute moments are uniformly bounded at fixed
beta because u lies on a compact circle and the image weights have
Gaussian tails. The finite product conditional identities pass to the
joint thermodynamic limit. They can be tested with bounded continuous
functions of X and circle-valued angles; the image sum is continuous
on the circle after reindexing at a representative cut.

For a fixed smooth test, max_p |h_a,p|=O(a^2) and
sum_p |h_a,p|^3=O(a^2). The conditional characteristic expansion thus gives

 E[exp(i xi(h_a))|theta]
 =exp[-sum_p h_a,p^2 v_beta(u_p)/2+o(1)],              (5)

with an error tending to0 uniformly in theta. The weighted ergodic theorem
for the mixing plaquette state, applied first to spatial step functions
and then smooth squares, gives

 sum_p h_a,p^2 v_beta(u_p) -> vbar ||f||2^2

in probability and L1. The same holds for mixed tests. The limit in(5)
is consequently a constant in L1. Multiplying by the bounded variable
exp(iY(h_a)) proves the factorization needed to combine(4) and(5):

 E exp[iY(J_a f)]
 ->exp[-((1-kappa-vbar)||f||2^2+kappa(f,Pf))/2].       (6)

This derivation does not assume Gaussianity of Y in advance. The resulting
quadratic form is nonnegative because it is the limit of characteristic
functions (also by the exact total-covariance identity). Testing nonzero
coexact forms shows a_contact=1-kappa-vbar>=0. The continuous positive
image variance has a positive minimum at fixed beta, so vbar>0 and the
strict upper bound on kappa in(1) follows.

The uniform centered MGF bounds for X and Y make all powers of any fixed
finite set of their rescaled tests uniformly integrable. Joint moments
therefore converge as well. For distribution tightness, a local L2-test
covariance bound implies a uniform expected H^(-s') norm for every s'>2,
because the embedding from L2 into H^(-s') on a bounded four-dimensional
region is Hilbert-Schmidt. Choose2<s'<s and use compact embedding into
H^(-s). A smooth localization and a countable exhaustion give local
distribution convergence. This is the usual distribution realization
of the Gaussian limits already identified by their tests.

## 6. Direct two-polarization reconstruction of the Gaussian limit

Write Y_cont as the sum of an independent white two-form of covariance
a_contact I and a Maxwell field strength of covariance kappa P. For
test forms supported strictly at positive Euclidean time, the white
cross-reflection covariance is zero. Its Gaussian positive-time algebra
therefore supplies only a vacuum factor in the OS quotient.

For the Maxwell part put j=d*f. Then d*j=0 and
(f,Pg)=(d*f,Delta^(-1)d*g). At spatial momentum p!=0 write w=|p| and

 J_alpha(p)=integral_0^infinity exp(-w t) jhat_alpha(t,p) dt.

Reflection changes the sign of the time component of the one-form j.
The scalar time Green kernel is exp(-w|t-s|)/(2w), so its reflected
quadratic form is

 integral d^3p/(2pi)^3 * kappa/(2w)
       [|J_spatial(p)|^2-|J_0(p)|^2].

Conservation and support away from the reflection plane imply
w J_0+i p.J_spatial=0. Thus the form equals

 integral d^3p/(2pi)^3 * kappa/(2|p|)
       |P_transverse(p)J_spatial(p)|^2>=0.             (7)

There are exactly two transverse components for p!=0. Their image is
dense: take f_0i(t,p)=tau(t)u_i(p), f_ij=0, with u transverse, supported
away from p=0, and a positive smooth tau supported at positive time.
Its Laplace transform is nonzero, so multiplication by the resulting
w-dependent factor has dense range. Time translation multiplies the
one-particle image by exp(-|p|s), giving energy |p|. The zero spatial
momentum has zero measure in the one-particle integral and contributes
no extra polarization. Gaussian Wick/Fock reconstruction then gives
the free two-polarization field. Kappa changes normalization, not energy.

This checks reflection positivity and the photon space of the identified
continuum Gaussian directly. It does not infer microscopic reflection
positivity from an asymmetric finite box or prove a phase of the separate
N=3 Hamiltonian. No charged particles, non-Abelian sector or gravity is
supplied by this Abelian reconstruction.

## 7. An actual-state correlation consequence

The selected fixed-beta score state cannot have absolutely summable
covariances for every component; in particular it cannot have exponential
clustering of this field. An absolutely summable covariance kernel would
have a continuous Fourier multiplier at0 and hence a constant matrix
multiplier in its rescaled covariance limit. The multiplier in(6) is
a_contact I+kappa P(p), with kappa>0, and is not constant in direction.
For example P_(01,01)(p)=(p_0^2+p_1^2)/|p|^2. The same argument applied
to that single component excludes absolute summability of its kernel.
Cubic symmetry gives the corresponding statement for each orientation.

This is a long-range correlation statement for an actual selected
infinite-volume Gibbs observable, conditional on the proof chain above.
It does not identify a microscopic Hamiltonian energy gap or transfer
the result to the separate finite-clock law.

## 8. Current verification boundary

The exact flux/theta map has independent finite Hodge, direct magnetic
sum, Poisson and positive-integration checks. The Gaussianity lemma has
finite reflection and positive non-Gaussian integration challenges. The
spectral response has exact cochain and symmetry constructions and a
direct Gaussian precision comparison, including controls against mean-
Hessian and nonergodic-mixture shortcuts. The new thermodynamic proof
uses a distinct nested-projection argument and a two-replica limit.

These author checks support this proposed chain; they are not independent
review or formal audit. A public milestone should preserve the exact
upstream revisions and the full analytic assumptions. Fixed-clock
electric defects, periodic topology/state matching, actual native law,
matter and TOE closure remain separate targets after this candidate.
