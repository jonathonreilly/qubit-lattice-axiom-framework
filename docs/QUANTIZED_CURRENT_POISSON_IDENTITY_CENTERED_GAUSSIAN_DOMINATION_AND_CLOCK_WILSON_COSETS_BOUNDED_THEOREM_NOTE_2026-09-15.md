---
claim_id: quantized_current_poisson_identity_centered_gaussian_domination_and_clock_wilson_cosets_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "A lattice Gaussian times the characteristic function of a symmetric probability measure, with nonnegative lattice weights, satisfies an exact positive dual moment identity and centered Gaussian domination. Applied to the supplied clock current law, it gives all-coupling current moment and density bounds and exact Wilson cosets with charge-N aliases. A separate plaquette-Fourier proof checks the same bound. An explicit half-shifted discrete Gaussian prevents an all-tilt continuous variance inference; no nondegenerate infrared limit follows."
upstream_dependencies:
  - finite_clock_exact_coupled_electric_magnetic_defect_representation_bounded_theorem_note_2026-09-15
  - free_cubic_magnetic_local_fillings_and_positive_electric_current_convex_extension_bounded_theorem_note_2026-09-15
runner: scripts/quantized_current_poisson_identity_centered_gaussian_domination_and_clock_wilson_cosets_2026_09_15.py
---

# Quantized-current Poisson identities, centered domination and Wilson cosets

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

A lattice Gaussian times the characteristic function of a symmetric probability measure, with nonnegative lattice weights, satisfies an exact positive dual moment identity and centered Gaussian domination. Applied to the supplied clock current law, it gives all-coupling current moment and density bounds and exact Wilson cosets with charge-N aliases. A separate plaquette-Fourier proof checks the same bound. An explicit half-shifted discrete Gaussian prevents an all-tilt continuous variance inference; no nondegenerate infrared limit follows.

These proposed analytic results await independent review and formal audit.
No native law, primitive, axiom or physical parameter is selected or changed.

## Status and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Identify a controlled effective field and the exact coupled-defect law needed for a fixed-clock physical-score theorem."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Review the exact identities and then combine current quantization with local magnetic source control to prove nondegenerate physical-score correlations at fixed parameters."
conditional_surface_status: "The supplied finite-volume law, integer topology, boundary kernel and explicit lattice/source conditions in the proof."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Self-contained derivation with distinct exact-cochain, Gaussian, Fourier and finite-enumeration challenges, without a phase inference."
```

The general lattice theorem and direct Fourier current estimate are derived
here. Matching the previously regrouped magnetic representation uses two
explicit same-PR provisional sources, both pending independent review.
The finite executable reads no repository helper or scientific input file.
The infinite-volume physical limit and native-law identification remain
separate obligations; neither is inferred from the finite checks.


| Provisional input | Precise use |
|---|---|
| [Exact coupled-defect representation](FINITE_CLOCK_EXACT_COUPLED_ELECTRIC_MAGNETIC_DEFECT_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Matching both defects and external integer characters to the regrouped current law |
| [Free-cubic source and filling bridge](FREE_CUBIC_MAGNETIC_LOCAL_FILLINGS_AND_POSITIVE_ELECTRIC_CURRENT_CONVEX_EXTENSION_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Physical current/Hodge coordinates and the chosen local real interpolation |
| General lattice Poisson theorem and direct Fourier proof | Derived below; neither uses a convexity or smallness premise |

## 1. A lattice Gaussian times a probability characteristic function

Let E be a finite-dimensional real Euclidean space, Lambda a full-rank lattice
in E, A a positive definite symmetric operator, and nu a symmetric probability
measure on E. Define

 chi(x)=integral exp(2pi i<b,x>) nu(db),
 w(x)=exp(-<x,Ax>/2) chi(x).

Assume only that w(a)>=0 for every a in Lambda. Positivity between lattice
points is not required. Since chi(0)=1, w(0)=1, the normalization Z=sum_a w(a)
is positive and finite. The lattice law is P(a)=w(a)/Z. It is symmetric and
has Gaussian tails at every fixed dimension. No convexity hypothesis is needed.

Let Lambda*={k:<k,a> integer for all a in Lambda}. Put

 C_A=(2pi)^(dim E/2)/(covol(Lambda)*sqrt(det A)),
 R=k-b,
 dPi(b,k)=C_A/Z * exp[-2pi^2<R,A^-1 R>] nu(db), k in Lambda*.

This is a positive probability measure. To prove normalization and the moment
identity, apply Gaussian Poisson summation for each b:

 sum_{a in Lambda} exp[-<a,Aa>/2+<h,a>+2pi i<b,a>]
 =C_A exp[<h,A^-1h>/2]
   sum_{k in Lambda*} exp[-2pi^2<k-b,A^-1(k-b)>]
                        exp[-2pi i<h,A^-1(k-b)>].          (1)

The left series is uniformly absolutely summable in b for fixed real h.
The right absolute sum is a shifted Gaussian theta, periodic in b modulo
Lambda* and bounded on a compact fundamental cell. Fubini with any probability
nu is therefore justified. This avoids assuming a density or moments for nu.
Putting h=0 proves Pi is a probability. Integrating (1) yields EXACTLY

 E_P exp<h,a> = exp[<h,A^-1h>/2]
                    E_Pi exp[-2pi i<h,A^-1R>].             (2)

Symmetry (b,k)->(-b,-k) makes the last expectation real. The left side is
strictly positive, so this dual characteristic function is positive for every
real h. Its modulus is at most1. Consequently

 1 <= E_P exp<h,a> <= exp[<h,A^-1h>/2].                    (3)

The lower bound uses symmetry/Jensen. Differentiating at h=0 gives

 Cov_P(a)=A^-1-4pi^2 A^-1 Cov_Pi(R) A^-1,
 0 <= Cov_P(a) <= A^-1.                                  (4)

All differentiated shifted-Gaussian sums have uniform moment bounds on a
fundamental cell, so this step remains valid without nu moment assumptions.
Formula(4) is a centered covariance identity. Under a real tilt h, the dual
measure in(2) acquires a complex phase; its covariance is no longer a positive
measure covariance. There is no all-tilt covariance conclusion.

More generally, periodizing w gives

 T(s)=sum_{a in Lambda}w(a+s)
 =C_A integral sum_{k in Lambda*}
   exp[-2pi^2<k-b,A^-1(k-b)>] exp[2pi i<k,s>] nu(db).       (5)

Here the sign of the phase is fixed by Fourier inversion and the convention
exp(-2pi i<k,x>) for the Fourier transform. In particular T(s)/T(0) is the
characteristic function of the Pi marginal of k, and |T(s)|<=T(0).
The Fourier transform of w itself is the positive Gaussian mixture

 hat w(k)=(2pi)^(dim E/2)/sqrt(det A)
               integral exp[-2pi^2<k-b,A^-1(k-b)>] nu(db).

These formulas hold even if w is signed off the lattice. If the shifted
lattice weights are nonnegative and at least one is positive, T(s)>0.
Nonnegativity alone permits T(s)=0: chi(x)=cos(pi x)^2 on Lambda=Z
vanishes on every half-integer. Physical integer-current cosets below
have strictly positive weights, a separate property of that model.

## 2. Application to the exact finite-clock current marginal

Take a contractible free four-dimensional cubic box as in the free-cubic source. Let C=ker d_0^* be the real
conserved1-current space and Lambda=C intersect Z^edges. It is full rank in C:
a spanning tree gives an integer fundamental-cycle basis. Let G=H_1^-1|C,
where H_1=d_0d_0^*+d_1^*d_1. It is positive definite on C.

The exact coupled-defect source representation, written in physical current coordinates,
has magnetic charges q=d_2k, law

 nu_m(q)=Z_m^-1 exp[-2pi^2 beta<q,H_3^-1q>].

Choose any odd integer filling n(q) with d_2n(q)=q. For example use the local
component filling constructed in the free-cubic source. Define b(q)=N G d_1^*n(q), an
E=C valued random vector, and A=(N^2/beta)G. Then

 chi(a)=E_nu_m exp[2pi i<N n(q),d_1G a>],
 w_N(a)=exp[-N^2<a,G a>/(2beta)] chi(a).                  (6)

This is precisely the positive integer-current marginal in the two linked provisional sources,
with both defect species retained. At large beta chi=exp F for the local
source extension, but the integer identity and its positivity hold for ALL
beta>0 and integer N>=1. Positivity follows without the large-beta expansion:
for any integer current J, its U(1) Villain character numerator is a sum of
strictly positive plaquette Fourier weights constrained by d_1^*m=J.
Every integer conserved J on a contractible box bounds an integer plaquette
chain, so the constrained sum is nonempty. The Villain Fourier weights are
positive Gaussian coefficients. Hence w_N(a)>0 for each a in Lambda.

Integer-filling changes n'(q)-n(q)=d_1ell(q) change b by N ell projected to C.
For every a in Lambda its inner product is N<ell,a>, an integer. Thus b changes
by an element of Lambda*. The centered dual variable R=k-b has an invariant
law after reindexing k. Both P and (2)–(4) are filling-independent. The
periodized T(s) at arbitrary real s may depend on the filling; the physical
cosets specified below do not.

Equations(3)–(4) give the exact finite-volume estimates

 E exp<h,a> <= exp[ beta/(2N^2) <P_C h,H_1 P_C h>],
 Cov(a) <= (beta/N^2) H_1|C.                             (7)

The bound is uniform in box size as a quadratic-form statement. It does not
say that a nontrivial continuum current survives. For a single edge e,
<P_C e,H_1 P_C e>=<e,d_1^*d_1e><=2(d-1), since H_1 commutes with the
orthogonal conserved/exact decomposition and an edge belongs to at most
2(d-1) plaquettes.
Chernoff optimization then gives, for u>0,

 Pr(|a_e|>=u)<=min(1,2 exp[-N^2 u^2/(4(d-1) beta)]).          (8)

Here the sharper coefficient uses H_1 P_C=d_1^*d_1, whose edge diagonal
is exactly the number of incident plaquettes, at most2(d-1). In d=4, the
denominator is12beta. Because a_e is integer,

 E number of occupied electric edges
 <=2|edges| exp[-N^2/(12beta)].                           (9)

This is a density bound for the positive auxiliary Fourier-current law at
fixed parameters. It is not a statement that link angles and these Fourier
currents have been put in a single positive joint law, nor a selected
empirical charged-particle density. Making the probability of no
electric edge tend to1 by a union bound still requires growing N^2/beta
relative to log(volume). No fixed-parameter phase exclusion follows.

### 2a. A shorter, independent route to the same current bound

The centered estimate is also an immediate consequence of the plaquette
Fourier representation, and therefore is not a new independent phase result.
This second derivation avoids magnetic fillings and convexity altogether.
Write the Villain weight as a positive constant times
sum_{m in Z} exp[-m^2/(2beta)] exp(i m t). Summing the finite link angles gives
exactly the centered discrete Gaussian on the full-rank plaquette lattice

 L_N={m in Z^plaquettes: d_1^*m in N Z^edges},
 P(m) proportional to exp[-||m||^2/(2beta)].

It contains N Z^plaquettes and is thus full rank even on complexes with
nontrivial topology. Completing the square and applying Gaussian Poisson
summation shows, for every real plaquette source t,

 E exp<t,m> = exp[beta||t||^2/2]
   theta_(L_N)(beta t)/theta_(L_N)(0)
 <=exp[beta||t||^2/2],

where theta_(L_N)(s)=sum_{m in L_N}exp[-||m-s||^2/(2beta)] is maximal at0:
its Fourier coefficients on the dual lattice are positive Gaussians.
The sign of s is irrelevant by symmetry. The electric current is the
integer pushforward a=d_1^*m/N. Setting t=d_1 h/N proves exactly

 E exp<h,a> <=exp[beta||d_1 h||^2/(2N^2)].              (7a)

This holds on every finite complex for that pushforward current law. The
free-cubic assumptions are needed for the matched magnetic filling and
identification with the full conserved-current lattice, not for(7a).
The diagonal bound in(8) follows directly because||d_1 e||^2 counts incident
plaquettes. This independent Fourier derivation agrees with(7); neither
requires an affine-coset lower covariance theorem or a convexity assumption.

The earlier periodic-covariance milestone contains the underlying plaquette
duality and centered covariance domination. The present current estimate is
an explicit moment-generating consequence and a check on the magnetic
regrouping, not a second independent discovery of Gaussian domination.

## 3. Exact Wilson cosets, including clock aliases

Let J in Lambda be an external integer current. In the coupled-defect source numerator
the current is J+Na. Therefore

 <exp[i<J,theta>]>_clock
 =sum_{a in Lambda} w_N(a+J/N) / sum_{a in Lambda}w_N(a)
 =T(J/N)/T(0).                                          (10)

Every sampled N(a+J/N) is an integer current, so these weights are positive
and their values are independent of the chosen magnetic filling. Replacing
n by n+dell changes the phase in(5) by exp[2pi i<N P_C ell,J/N>]=1.
Equation(5) rewrites(10) as

 E_Pi exp[2pi i<k,J/N>].                                 (11)

This is an exact positive probability representation for Wilson characters,
not a continuum Gaussian approximation. If J=N c with c in Lambda, reindexing
a shows(10)=1, while(11) is identically1 pointwise. Any continuum replacement
that loses this alias cannot represent the entire finite-clock character
algebra. Fixed low-frequency observables or a scaling limit may remain valid.

The covariance identity(4) and Wilson law(11) constrain different observables:
R=k-b appears in the current moment identity, k in the Wilson character. They
must not be interchanged. The magnetic shift b is part of the original law.

## 4. Why the exact centered result cannot be used at arbitrary tilt

Even in dimension1, take Lambda=Z, nu=delta0, A=alpha>0. This centered discrete
Gaussian obeys(3)–(4). Apply the linear tilt h=alpha/2. Its normalized law is
proportional to exp[-alpha(n-1/2)^2/2], symmetric about1/2. Hence

 Var_h(n)=E_h(n-1/2)^2 >=1/4.

The continuous potential has Hessian alpha everywhere. For alpha>4 this
violates the putative all-tilt continuous variance bound1/alpha. There is no
contradiction with the centered bound or centered sub-Gaussian moment estimate.
Indeed a sub-Gaussian moment estimate at the origin need not bound the Hessian
of its log moment generating function at every nonzero tilt.

This is a counterexample to one transfer of a continuous variance theorem to
an integer measure. It is neither a no-go for lattice methods nor an actual
clock phase counterexample. The centered identity, Poisson representation,
cluster/locality estimates, and integer-current renormalization remain routes.

## 5. What this adds and what remains

The exact positive magnetic regrouping supplies more than an unspecified
convex extension: a Gaussian times a probability characteristic function gives
centered Gaussian domination on the actual current lattice, at every beta.
The proof explicitly retains quantization and both defects. This is standard
Gaussian Poisson machinery organized for the current representation; no novelty
claim is made for Poisson summation or its Gaussian domination consequences.

It does not supply a lower current covariance, a fixed-parameter scaling law,
Gaussian higher cumulants, full physical-score correlators, local photon
reconstruction, charged matter, or a microscopic/native formation law. In
particular the exact alpha-centered bound also holds for a concentrated
large-alpha discrete Gaussian with vanishing variance. Explicitly, with
r=exp(-alpha/2), its variance is at most
2 sum_(n>=1)n^2 r^(n^2)<=2r(1+r)/(1-r)^3, which tends to zero.
Two-sided nondegenerate
infrared control is a separate obligation.

The magnetic positive image-charge bound from the earlier direct scaling
work is another pushforward of a centered dual lattice Gaussian. It and
the electric bound describe different positive auxiliary representations;
they must not be read as independent samples of a joint positive electric
and magnetic gas. The mutual phase in the coupled-defect source is still present.

The next decisive route is to combine the local magnetic source curvature
with the integer-current dual law to control long-distance physical score
correlators at fixed beta,N. Proving that route requires actual scale-local
estimates or a verified integer-current homogenization theorem, not the
continuous Brascamp–Lieb inequality alone. No axiom wall has been established.

## 6. Finite evidence and inference checks

Four finite families compare a nonorthogonal two-dimensional lattice of
covolume6 with its distinct Poisson dual; the actual single-three-cube current,
shifted-dual,32-state clock and six-plaquette Fourier sums; exact Hodge/current
basis identities on three/four-cubes; and half-shift, concentration and
hypothesis controls. The three-cube Wilson expectation is approximately
0.78930863427393 in all four representations. Replacing k by R in its dual
character gives approximately0.76544129638199 and is rejected. Charge-N
aliases and integer filling changes are checked separately.

### N1 — Distinct attempted inferences

| Honesty | Route attempted | Result |
|---|---|---|
| ATTEMPTED | Infer an integer law's all-tilt variance from the continuous Hessian | The half-shifted one-dimensional discrete Gaussian violates that bound for alpha>4. |
| ATTEMPTED | Use the positive magnetic characteristic factor directly | Poisson summation gives the exact centered moment identity, retaining the positive dual law. |
| ATTEMPTED | Derive current bounds from the original plaquette Fourier law | The independent modular-lattice calculation proves the same bound without convexity or magnetic fillings. |
| ATTEMPTED | Replace the Wilson variable k by the moment variable R=k-b | Direct clock and three dual/current evaluations distinguish the variables numerically and algebraically. |
| ATTEMPTED | Remove the positive mixing-measure hypothesis | An everywhere positive lattice weight built from a signed mixing measure violates the Gaussian bound. |
| ATTEMPTED | Drop lattice-weight positivity when the mixing measure is positive | A cosine characteristic produces negative lattice weights; there is no probability law to bound. |
| ATTEMPTED | Infer a nondegenerate field from a centered Gaussian upper bound | Exact large-alpha discrete Gaussians concentrate at zero while satisfying every centered upper bound. |

No route is declared ruled out by prior retained authority. These concern
separate inference hypotheses and are not independent axiom walls.

### N2 — Dependencies and scope

The two representation inputs are explicitly provisional. The general
lattice identity and direct modular-Fourier proof are derived independently
of them. Agreement is a calculation check, not an independent audit.
The centered domination already follows from the earlier periodic duality;
it is not counted as a second phase breakthrough. Native-law selection,
charged matter and the N=3 penalty-Hamiltonian phase remain unresolved.

### N3 — Hidden hypotheses

The general lattice is full rank, its quadratic form positive definite,
the mixing measure symmetric and positive, and all integer weights
nonnegative. Off-lattice positivity is unnecessary. The free-cubic matching
uses integer contractibility and fixed odd fillings. Positivity at arbitrary
real source is invoked only where previously proved, never inferred from
the centered lattice inequality. Current and magnetic auxiliary descriptions
are not silently combined into an independent positive joint defect law.

### N4 — Matched residuals

The actual three-cube test uses identical N=2,beta=1/2 and the same plaquette
Wilson current in four representations. The source-N alias tests the finite
character algebra. Generic lattice and half-shift controls are mathematical
examples, not four-dimensional phases. Finite cutoffs are numerical controls
on the identities, not a substitute for the absolute-convergence proof.

### N5 — Resolution

The executable emits per_element,per_site,per_mode,per_block,lattice_wide
lines. Finite Poisson/current/clock calculations and exact incidence identities
are executed. The all-lattice identities, arbitrary-volume bounds and
nondegenerate infrared question are checked and not executed: written
proofs carry the first two, and the infrared result remains open.

### N6 — Partial paths remain open

Centered domination, exact Wilson cosets, magnetic source curvature and
integer-current renormalization remain compatible routes. The half-shift
example excludes a particular all-tilt continuous variance inference only.
It does not exclude an appropriately proved discrete variance theorem,
local scale estimates, direct score analysis or a fixed-clock phase.

### N7 — Steelman

Gaussian upper domination can hold while the lattice law approaches a
point mass. This criticism is correct and made explicit by the concentration
control. A nonzero limiting transverse covariance and higher-cumulant control
are needed before a physical photon inference. The exact identities identify
the variables and preserve clock aliases; they do not supply those estimates.

### N8 — Cross-cycle comparison

The earlier periodic covariance note already has centered plaquette duality.
This source gives a current MGF consequence and an independent check of the
new magnetic regrouping. The free-cubic convex extension does not justify
an all-tilt discrete variance bound. Growing-parameter Maxwell constructions
retain their earlier scope; this source neither upgrades them to a fixed-law
photon limit nor replaces the stated N=3 Hamiltonian by a selected clock law.

## 7. Review status

All derivations and finite challenges were performed personally. Independent
review and formal audit remain pending. No axiom, primitive, empirical
parameter or editable prompt was changed.
