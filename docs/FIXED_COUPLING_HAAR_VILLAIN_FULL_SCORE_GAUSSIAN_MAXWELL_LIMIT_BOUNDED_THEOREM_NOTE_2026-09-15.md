---
claim_id: fixed_coupling_haar_villain_full_score_gaussian_maxwell_limit_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For sufficiently large fixed beta, the supplied continuous-Haar U(1) Villain law on free four-dimensional cubes has a selected mixing Gibbs state whose full flux and bounded local score converge under macroscopic rescaling to Gaussian two-form distributions; the score covariance is a nonnegative white contact term plus a strictly positive Maxwell term with a two-polarization continuum reconstruction."
upstream_dependencies:
  - preconditioned_extended_gradient_gaussian_remainder_and_free_cubic_riesz_bounded_theorem_note_2026-09-15
  - small_contrast_cochain_gibbs_state_matching_and_spectral_homogenization_bounded_theorem_note_2026-09-15
  - free_cubic_magnetic_local_fillings_and_positive_electric_current_convex_extension_bounded_theorem_note_2026-09-15
runner: scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py
---

# A fixed-coupling Gaussian Maxwell limit of the Haar Villain score

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

For sufficiently large fixed beta, the supplied continuous-Haar U(1) Villain law on free four-dimensional cubes has a selected mixing Gibbs state whose full flux and bounded local score converge under macroscopic rescaling to Gaussian two-form distributions; the score covariance is a nonnegative white contact term plus a strictly positive Maxwell term with a two-polarization continuum reconstruction.

This is an author theorem proposal. The written proof and its provisional
upstream sources await independent mathematical review and formal audit.
The supplied continuous-angle law is an explicit model input; it is not
derived from the framework axioms, and no axiom or primitive is changed.

## Status, scope and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Establish a fixed-law full physical-score limit while preserving the probability law, observable and state."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently check this fixed-Haar proof chain, then address the separate quantized electric defects before making a finite-clock inference."
conditional_surface_status: "The explicitly supplied law, cubic exhaustion, carrier conditions and operator smallness conditions in the proof."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A quantified analytic theorem proposal with finite challenges of distinct calculation paths; the supplied-law and independent-review boundaries remain explicit."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The single-sentence claim above is the target contract. An auxiliary
Langevin time below is a proof parameter, distinct from all four Euclidean
coordinates. Finite calculations challenge the argument; they do not
execute an infinite-volume theorem or ratify its status.

## Imports and obligation graph

| Input or step | Provenance and proof status |
|---|---|
| Continuous Haar links and the positive Villain image law | Supplied microscopic probability law; not selected by framework axioms |
| [Carrier and cubic derivative estimates](PRECONDITIONED_EXTENDED_GRADIENT_GAUSSIAN_REMAINDER_AND_FREE_CUBIC_RIESZ_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Same cumulative review unit; finite source variation, Riesz bound and explicit provisional carrier/filling inputs |
| [Auxiliary state and covariance](SMALL_CONTRAST_COCHAIN_GIBBS_STATE_MATCHING_AND_SPECTRAL_HOMOGENIZATION_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Same cumulative review unit; mixing, free-box matching, replica concentration and spectral limit proved there |
| [Free-cube integer topology and filling](FREE_CUBIC_MAGNETIC_LOCAL_FILLINGS_AND_POSITIVE_ELECTRIC_CURRENT_CONVEX_EXTENSION_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Provisional parent at f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8, sections1-2; the exact flux unfolding is also derived below |
| Exact full-flux real tilt | Derived here without a small-defect approximation |
| Physical Gibbs state and score noise | Derived here from the same limiting flux law |
| Gaussian positive-time reconstruction | Derived directly for the identified continuum covariance |

Every limit below uses the same uniform-root free-cube exhaustion. No
finite-clock summation is replaced by Haar integration. Standard finite
Poisson summation, Gaussian integration, ergodic averaging and Gaussian
reconstruction are mathematical tools with the relevant domains specified
in the proof. No observed physical value is fitted or imported.

The parent source must land before separate child review, or be covered
in the same frozen cumulative review unit. The strongest remaining
verification obligation is independent examination of that complete
analytic chain. Establishing a finite-clock law, a phase of the supplied
N=3 penalty Hamiltonian, a native law, matter or gravity is outside this
theorem and remains additional scientific work.

## 1. Statement and exact state selection

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

Under the stated conditions the theorem proposed here gives a spatially
mixing selected Gibbs state and joint Gaussian limits of all the full flux and score tests:

 X(J_a f) -> X_cont(f), Cov(X_cont)=I-kappa R,
 Y(J_a f) -> Y_cont(f), Cov(Y_cont)=a_contact I+kappa P,

 P=d Delta^(-1)d*, R=I-P=d*Delta^(-1)d on two-forms,
 a_contact=1-kappa-vbar>=0,
 vbar=E v_beta((d_1 theta)_p)>0,
 1/(1+delta)<=kappa<=1-vbar<1.                         (C.1)

The same limits hold for all joint moments and locally as distributions
in H^(-s) for s>2. The Gaussian continuum score has a direct positive-time
OS reconstruction with two transverse photons and energy |p|. The white
contact term contributes only the vacuum to that reconstruction.
This is a statement about the identified continuum limit; microscopic
periodic-state matching and the finite-clock phase are additional work.

## 2. Exact finite free-box flux unfolding

Let the cell complex be a finite free cubic box in dimension four. Write
D=d_1, B=d_2, C=d_3, H=B B*+C* C on real three-cochains, and G=H^-1.
For this boundary convention H>0, cohomology in degrees1,2,3 is zero, and
integer coboundaries are saturated. Define orthogonal two-form projections

 P=D(D*D)^+D*, R=B*G B=I-P.

The supplied compact-U(1) Villain law has link Haar measure and positive
image weights exp[-beta||D theta-2pi k||^2/2], k integer two-cochains.
Its real lifted flux is X=sqrt(beta)(D theta-2pi k). Gauge fixing and
unfolding the exact integer shifts gives the positive decomposition

 X = P W - 2pi sqrt(beta) B*G q,                      (E.1)
 q in Q:=B Z^P=ker(C) intersect Z^C3,
 nu(q) proportional to exp[-2pi^2 beta(q,Gq)],

where W is a standard real Gaussian two-cochain independent of q.
To see the independence, Haar link measure pushes forward to Haar measure
on range(D)/(2pi D Z^E). Integer contractibility gives
ker B intersect Z^P=D Z^E, so the image integers in a fixed q coset are
k_q+D ell, modulo the kernel of D. Their translates tile range(D), up to
measure-zero boundaries. The torus Haar normalization and lattice cell
volume are independent of q. The representative's orthogonal part is B*Gq.
The exact part Pk_q is absorbed into the
unfolded real D theta integral. The remaining Gaussian density factorizes
between range(D) and its orthogonal complement. The gauge volume and
integer-lattice Jacobian are independent of q and cancel in normalization.
This uses continuous Haar integration. A finite clock sum does not unfold
into this Gaussian integral and retains the second electric-current gas.

For real h, define Z(s)=sum_q exp[-2pi^2 beta(q,Gq)+2pi i(q,s)]. Then

 E exp[i(h,X)] = exp[-(h,Ph)/2] Z(s)/Z(0),
 s=-sqrt(beta) G B h.                                 (E.2)

The full source h is arbitrary. Restricting to Bh=0 would erase the
magnetic factor and would not characterize the full field.

The original X also has the centered real-MGF bound
E exp[(h,X)]<=exp[||h||^2/2]. Complete the square in the centered q
lattice Gaussian in (E.1); its shifted theta is at most its centered value
by Poisson summation on span(Q). Its contribution is at most
exp[(h,Rh)/2], and the independent P Gaussian supplies exp[(h,Ph)/2].
Jensen gives the same bound for Y=E[X|theta]. This supplies uniform moments
for the finite-box linear sources, without assuming the clock proof also
holds for Haar integration merely by analogy.

## 3. Positive auxiliary measure and the real-tilt identity

Choose 0<c<1/||H||; on all free four-dimensional cubic boxes one may use
c=1/32, since ||H||<=16. Set

 A=beta(G-cI)>0, T=(I-cH)^-1,
 Theta_c(phi)=sum_(q in Q) exp[-2pi^2 beta c||q||^2+2pi i(q,phi)].

Q is a full-rank lattice in its real span. Poisson summation in that span
writes Theta_c as a strictly positive sum of shifted Gaussians. It is
constant in the orthogonal complement, hence is positive for every phi.
Absolute convergence follows from the positive scalar quadratic weight.
Define the proper positive probability measure

 mu(dphi) = Theta_c(phi) gamma_A(dphi) / E_gamma_A Theta_c.

Gaussian integration gives E_gamma_A Theta_c(phi+s)=Z(s). All exchanges
are justified by summability of exp[-2pi^2 beta c||q||^2]. Translating the
real Gaussian integration variable by s therefore gives the exact identity

 Z(s)/Z(0)=exp[-(s,A^-1s)/2] E_mu exp[(phi,A^-1s)].      (E.3)

Inserting (E.2), using A^-1=beta^-1 T H and GT=G+cT, gives

 E exp[i(h,X)]
 =exp[-||h||^2/2-c(Bh,T Bh)/2]
  E_mu exp[-beta^-1/2(phi,T Bh)].                      (E.4)

This is a REAL moment-generating function on the right. Replacing it by
an auxiliary characteristic function changes the sign of its contribution
to the flux covariance and is incorrect. Formula (E.4) is exact at fixed beta
and finite volume; no small-defect or asymptotic hypothesis is needed.

For any real j, a second completion of the square gives

 E_mu exp[(j,phi)]
 =exp[(j,Aj)/2] Z(Aj)/Z(0) <= exp[(j,Aj)/2].           (E.5)

The ratio is positive by the Gaussian-integrated theta representation and
at most one by the positive symmetric q weights. Thus mu is centered and
Cov_mu(phi)<=A<=beta G. This centered domination is not an all-tilt Hessian
bound. It yields uniform exponential integrability of the linear sources
used below. No convexity claim is smuggled into (E.5).

Differentiating (E.4) twice gives the finite covariance check

 Cov(X)=I+c B*T B-beta^-1 B*T Cov_mu(phi) T B.          (E.6)

Equivalently, differentiating (E.3) and the magnetic theta directly gives
Cov_mu(phi)=A-4pi^2 A Cov_nu(q) A and recovers (E.1). The minus sign in (E.6)
is consistent with Cov(X)=P+4pi^2 beta B*G Cov_nu(q)G B.

## 4. Exact flux identity in gradient variables

Write B=d_2, H_3=B B*+d_3*d_3, G_3=H_3^(-1), c=1/32, and
T_r=(I-c H_r)^(-1). The auxiliary variable is

 omega=beta^(-1/2)(d_2*phi,d_3 phi),
 K=(d_2*,d_3)(G_3-cI)(d_2*,d_3)*.

It has Gaussian reference covariance K on its compatible range and the
even carrier potential R_L. Its first block is a two-form. The exact
finite characteristic identity is

 E exp[i(h,X)]
 =exp[-||h||2^2/2-c(Bh,T_3 Bh)/2]
    E_mu exp[-(T_2 h,omega_first)].                    (C.2)

The right side uses a real MGF. The cochain identity T_3 B=B T_2 fixes
both the source and its normalization. The finite auxiliary law obeys
E exp(omega(j))<=exp[(j,Kj)/2]; the physical X and Y each obey the
centered bound exp(||h||2^2/2). These follow from the exact Gaussian/theta
identities and conditional Jensen inequality.

The matching theorem passes (C.2) to infinite volume. T_r have exponentially
decaying kernels and norm at most2 on ell2 and ell3; their free-box bulk
limits follow from their finite-range Neumann series. The MGF bound
controls source truncations. Thus the selected full-flux local law is
uniquely specified by the matched auxiliary law.

For macroscopically rescaled h_a, ||B h_a||2=O(a). The finite-time
Gaussianity bound, inherited by the infinite auxiliary state through
the replica argument, gives

 |log E exp[-(T_2 h_a,omega_first)]
       -Var((T_2 h_a,omega_first))/2|
 <=(4/3) M3 C3^3 ||h_a||3^3=O_beta(a^2).               (C.3)

The spectral response theorem gives the quadratic limit kappa(f,Rf).
The T_2 correction vanishes because its multiplier tends to I at zero
frequency; boundedness and smooth-source Fourier tails justify passage.
The explicit second term in (C.2)'s prefactor also vanishes. Hence

 E exp[i X(J_a f)] -> exp[-(||f||2^2-kappa(f,Rf))/2].   (C.4)

Every finite real linear combination of tests obeys the same estimate,
so this is joint Gaussian convergence, not merely a two-point bound.
The spectral upper and score lower inequalities give
1/(1+delta)<=kappa<=1 at this stage.

## 5. The selected physical state is mixing and Gibbs

For compact sources h,g separated by a lattice translation z, the cross
term in the Gaussian prefactor of (C.2) tends to0. Its nonlocal part has
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

The selected link state is also mixing. For two finite link-current
characters at sufficiently separated translates, their divergence supports
are disjoint. Their combined current is conserved exactly when each is
conserved. If either is not, both the relevant expectation and its
factorized value vanish by local gauge invariance. If both are conserved,
choose finite plaquette fillings; mixing follows from the already proved
plaquette mixing. Fourier polynomials and L2 density extend this to bounded
local link observables.

## 6. Conditional image noise and the score

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
 =exp[-sum_p h_a,p^2 v_beta(u_p)/2+o(1)],              (C.5)

with an error tending to0 uniformly in theta. The weighted ergodic theorem
for the mixing plaquette state, applied first to spatial step functions
and then smooth squares, gives

 sum_p h_a,p^2 v_beta(u_p) -> vbar ||f||2^2

in probability and L1. The same holds for mixed tests. The limit in (C.5)
is consequently a constant in L1. Multiplying by the bounded variable
exp(iY(h_a)) proves the factorization needed to combine (C.4) and (C.5):

 E exp[iY(J_a f)]
 ->exp[-((1-kappa-vbar)||f||2^2+kappa(f,Pf))/2].       (C.6)

For separate tests f,g, the same conditional identity yields
E exp[iY(J_a f)+i xi(J_a g)]
=E exp[iY(J_a f)] exp[-vbar||g||2^2/2]+o(1).
Thus xi has an independent white Gaussian limit jointly with Y, and
X=Y+xi gives the asserted joint flux/score limit. Real linear combinations
of any finite list of tests give the same conclusion.

This derivation does not assume Gaussianity of Y in advance. The resulting
quadratic form is nonnegative because it is the limit of characteristic
functions (also by the exact total-covariance identity). Testing nonzero
coexact forms shows a_contact=1-kappa-vbar>=0. The continuous positive
image variance has a positive minimum at fixed beta, so vbar>0 and the
strict upper bound on kappa in (C.1) follows.

The uniform centered MGF bounds for X and Y make all powers of any fixed
finite set of their rescaled tests uniformly integrable. Joint moments
therefore converge as well. For distribution tightness, a local L2-test
covariance bound implies a uniform expected H^(-s') norm for every s'>2,
because the embedding from L2 into H^(-s') on a bounded four-dimensional
region is Hilbert-Schmidt. Choose2<s'<s and use compact embedding into
H^(-s). A smooth localization and a countable exhaustion give local
distribution convergence. This is the usual distribution realization
of the Gaussian limits already identified by their tests.

## 7. Direct two-polarization reconstruction of the Gaussian limit

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
       |P_transverse(p)J_spatial(p)|^2>=0.             (C.7)

There are exactly two transverse components for p!=0. To establish density,
first extend the positive-time test space from compact spatial support to
Schwartz spatial tests: spatial cutoffs approximate in L2, and the bounded
continuum covariance makes the reflection form continuous in that norm.
Their one-particle image is dense: take f_0i(t,p)=tau(t)u_i(p), f_ij=0,
with u transverse, supported
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

## 8. An actual-state correlation consequence

The selected fixed-beta score state cannot have absolutely summable
covariances for every component; in particular it cannot have exponential
clustering of this field. An absolutely summable covariance kernel would
have a continuous Fourier multiplier at0 and hence a constant matrix
multiplier in its rescaled covariance limit. The multiplier in (C.6) is
a_contact I+kappa P(p), with kappa>0, and is not constant in direction.
For example P_(01,01)(p)=(p_0^2+p_1^2)/|p|^2. The same argument applied
to that single component excludes absolute summability of its kernel.
Cubic symmetry gives the corresponding statement for each orientation.

This is a long-range correlation consequence of the proposed theorem
for the actual selected infinite-volume Gibbs observable.
It does not identify a microscopic Hamiltonian energy gap or transfer
the result to the separate finite-clock law.

## 9. Quantifier and boundary checks

The order of limits is first uniform-root thermodynamic averaging at fixed
beta, then a decreasing macroscopic mesh in the selected stationary state.
The proof supplies no unspecified simultaneous finite-box/mesh rate.
Beta is any fixed value above a finite sufficient threshold satisfying the
explicit carrier and operator inequalities. The Riesz constant is finite;
no unsupported numerical beta threshold is assigned to the full theorem.
Zero test forms give zero covariance. Coexact tests see only the contact
part of the score; exact tests also see the nonzero Maxwell coefficient.
The single zero Fourier point has zero continuum measure. Contact noise
can have zero coefficient and still has only the vacuum positive-time
quotient. Free cubic boundaries are part of the hypothesis; arbitrary
thin rectangles, periodic harmonic sectors and finite clocks are not
silently included. Strictly positive-time tests exclude boundary-plane
contact terms in the reconstruction.

## Finite evidence and No-Go Discipline Gate

The paired runner reads no repository scientific input or package-integrity
file and writes only stdout. It constructs integer cochains, compares
independent positive Gaussian/image integrations and Poisson sums, inverts
Gaussian precision on an independently chosen compatible basis, and solves
symmetry commutants exactly. Floating errors and quadrature cutoff changes
are reported as observed comparisons, not rigorous interval certificates.
The all-volume assertions are carried by the written proof and await
independent review. One shared runner supplies the complete finite packet
for the three companion notes; no undeclared helper is required.

### N1 — Attempted inference controls

| Honesty | Attempted inference | Witness and actual conclusion |
|---|---|---|
| ATTEMPTED | Treat the auxiliary factor as a characteristic function | `three_cube` compares the original magnetic sum, Poisson comb and positive integral; the wrong-sign factor disagrees for nonclosed sources. The exact map uses a real MGF. |
| ATTEMPTED | Use the same zero-extension rule for closed charges and co-closed gradients | `nested_projection` embeds exact finite cochains: codifferentials extend, while the specified closed three-charge develops a nonzero exterior derivative. The proof uses the appropriate space. |
| ATTEMPTED | Infer diffuse-source Gaussianity from a small Hessian alone | `collective_control` has a dimension-independent non-Gaussian collective coordinate; its third-influence constant grows. The uniform third-order hypothesis is retained. |
| ATTEMPTED | Substitute the mean Hessian for the effective covariance response | `layered_checks` compares full Gaussian precision with the response and its Schur limit; the mean-Hessian shortcut has a persistent discrepancy. The fluctuation term is retained. |
| ATTEMPTED | Obtain an ergodic Gaussian limit by averaging a global anisotropic orientation | `invariant_mixture_control` has a positive fourth cumulant, computed as three times the variance of component variances. The actual proof symmetrizes the potential and constructs an ergodic factor. |
| ATTEMPTED | Infer theta upper domination from small uniform convexity | `theta_upper_hypothesis_control` gives variance greater than the Gaussian reference. The physical theta inequality is a separately derived structural fact. |
| ATTEMPTED | Count four reflected current components as photon polarizations | `image_score_and_reflection` imposes current conservation and obtains a positive rank-two projector; the unreduced time metric has a negative direction. |

These are explicit positive counterexample witnesses and proof-hypothesis
checks. None is a no-go for a physical phase or an axiom update. No route
is marked RULED OUT BY PRIOR.

### N2 — Dependencies and collapse

There is no asserted collection of independent physical walls, so the
pairwise physical-wall table is empty and the physical-wall count is zero.
The controls are not added as independent evidence of phase failure.
Source unfolding, finite cumulant control, thermodynamic identification,
replica concentration and spectral response instead form one dependent
positive proof chain. Failure of a linked input invalidates its dependents;
it does not prove a separate axiom obstruction. The two averaging controls
challenge different steps of that same state/covariance chain and are not
counted as two independent phase exclusions.

### N3 — Hidden-hypothesis scan

The law, continuous link domain, counting metric, free cubic boundaries,
integer topology, order of limits, real sources, smallness conditions and
carrier bounds are explicit. The auxiliary time is distinguished from
physical Euclidean time. Standard SDE, interpolation, spectral and Gaussian
machinery is mathematical input with checked domains, not an imported
photon phase. The source has no assumed Maxwell covariance or Gaussian
limit at a terminal step. The provisional parent proofs and independent
review requirement remain explicit. No framework primitive is introduced.

### N4 — Residual matching

| Packet witness | Residual tested | Match and limit |
|---|---|---|
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:180` (`exact_hodge`), `three_cube` | Actual source, sign, Gaussian split and covariance normalization | Yes, exact finite cochains and the same normalized three-cube flux; no all-volume proof is executed |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:63` (`reflection`), `nested_projection` | Boundary incidence and compatible-space embedding | Yes, finite instances of the specified free-box construction |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:115` (`positive_integrals`), `collective_control` | Finite source derivatives and the third-influence hypothesis | Yes, positive finite measures with the stated comparison geometry |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:306` (`layered_checks`), `symmetry_commutant`, `invariant_mixture_control` | Fiber convention, fluctuation elimination and invariant sector | Yes, explicitly quadratic comparison models and exact group algebra; not simulations of the nonlinear Gibbs state |
| `scripts/haar_villain_fixed_coupling_full_score_2026_09_15.py:404` (`image_score_and_reflection`) | Local score/image normalization and conserved continuum reflection form | Yes, the supplied image kernel and exact finite momentum algebra |

No numerical witness is cited as executing the nonlinear thermodynamic
or continuum theorem. Written lemmas supply those obligations.

### N5 — Resolution and rhetoric

The primary cached stdout contains substantive per_element, per_site,
per_mode, per_block and lattice_wide certificates. Finite cochains,
quadratures, spectra and algebra are executed. Uniform Riesz estimates,
carrier expansions, state matching, ergodic averaging and continuum
reconstruction are checked and not executed; their analytic proofs are
the evidence at that resolution. No number of PASS lines supplies
independent review. The actual score's nonsummability conclusion, when
used in the companion physical theorem, follows from its nonconstant
low-frequency covariance symbol, not from a finite numerical tail fit.

### N6 — Remaining positive paths

The supplied Haar law is a concrete positive comparison route. Its finite-
clock counterpart retains quantized electric defects, which can be studied
through the exact coupled representation, its positive integer marginal,
or a direct physical-score argument. None is excluded by this theorem.
A new axiom is not requested or inferred. No primitive inadequacy claim
is made, so no primitive-registry exclusion is needed.

### N7 — Strongest objection

A hostile reviewer can correctly reject a full physical conclusion if the
carrier extension fails the uniform local bounds, if an averaged state is
misidentified, or if the source map loses a defect or noise term. The proof
therefore gives each of those steps explicitly and keeps the parent
sources in the reviewed dependency closure. The finite checks cannot settle
the remaining independent examination of the infinite-state argument.
Even a correct Haar theorem would leave finite-clock electric defects and
the native-law identification as distinct open targets. A broad TOE or
axiom-wall claim would be unsupported and is not made.

### N8 — Prior-route comparison

The parent carrier/filling argument supplied uniform convexity and exact
source control, while leaving a physical infrared limit open. This proposal
adds source-derivative control, an actual mixing-state construction,
replica concentration and spectral response. Earlier growing-coupling
constructions remove entire defect sectors by changing their parameters;
that is not used here. The image-noise distinction is retained and proved
for this Haar law. No previous failed route is promoted to an impossibility
claim, and no claim is made that this method includes finite clocks.

## Review record

All derivation and checks were performed personally without subagents.
This is an author check, not independent review, audit or main landing.
The parent f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8 and all three companion
notes form a provisional dependent chain. Hard review/landing condition:
review the needed parent content in the same frozen cumulative unit or
wait for it to land, and independently examine the complete final source.
Focused execution, mutation, cache and conformance receipts are recorded
in the branch-local handoff. Combined current-main pipeline, strict lint
and changed-evidence validation remain required at authorized integration.
