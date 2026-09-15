---
claim_id: fixed_clock_transverse_spectral_concentration_and_linear_energy_band_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: >-
  Conditional on the uniform all-affine covariance and same-state reflection
  positivity supplied by the complete periodic finite-clock proof in this PR,
  each specified isotropic four-dimensional Villain periodic-limit state at
  fixed beta and N with beta,beta_d>=2000 has, for almost every spatial
  momentum with 0<r<=1, two transverse magnetic-score
  response directions with nonzero OS spectral weight in an energy band
  proportional to spatial momentum. Over 99.96 percent of each transverse
  static susceptibility lies in the displayed narrow band. Ordinary band
  weight is bounded above and below by constants times momentum. A pole,
  Gaussianity, group velocity, exact photon dispersion, the N=3 penalty phase,
  native law selection and an axiom update are not inferred.
upstream_dependencies:
  - periodic_finite_clock_villain_covariance_and_observable_masslessness_bounded_theorem_note_2026-09-14
runner: scripts/fixed_clock_transverse_spectral_concentration_2026_09_15.py
---

# Fixed-clock transverse spectral concentration and a linear energy band

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** conditional-support; independent review pending

For almost every sufficiently small nonzero spatial momentum, the specified
fixed-parameter clock model's covariance input implies two transverse
response directions with nonzero spectral weight at energies
proportional to spatial momentum, and concentrates over 99.96 percent of
their static susceptibility in the explicit band below. This is a conditional
mathematical implication for the supplied isotropic model. Its complete
provisional input is included in this PR's review delta.

The additional mechanism is a positive two-frequency Stieltjes identity.
It extracts quantitative energy information without assuming a Gaussian
scaling field. Positive spectral representations are standard machinery;
no novelty priority for that machinery or finite-group Coulomb phases is
claimed. The new contribution is this explicit implication and its bounds
for the linked clock covariance packet.

## Status, dependency contract and proof obligations

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: periodic_finite_clock_villain_covariance_and_observable_masslessness_bounded_theorem_note_2026-09-14
target_blocker_text: "Extract quantitative fixed-clock energy-momentum information from the actual-state covariance theorem without assuming a Gaussian limit."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the complete covariance input and this spectral implication; pursue Gaussianity and microscopic physical identification separately."
conditional_surface_status: "Uniform all-affine covariance and same-state site/link reflection positivity from the complete same-delta provisional source."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "An analytic quantitative spectral implication with explicit fixed-parameter hypotheses and finite mathematical challenges."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

| Obligation | Disposition | Scope preserved |
|---|---|---|
| All-affine curl covariance and its dual application | Explicit provisional input in the linked complete same-delta source | Fixed beta,beta_d>=2000; every specified periodic-limit state |
| Site/link reflection positivity and positive transfer in that state | Same provisional source, section 11 | Gauge-invariant observables; no unmatched Hamiltonian |
| Physical score contact and uniform projector approximation | Section 2, exact finite Poisson duality and conditional moments | Image variance retained; no all-affine upper bound |
| Magnetic midpoint symbol and time-zero representation | Sections 3-4, direct algebra and spectral theorem | Spatial, time-even plaquettes; almost every nonzero spatial momentum |
| Positive localization and ordinary band weight | Sections 5-6, exact rational identity and positive matrix integration | Static susceptibility distinguished from ordinary OS norm |
| Fixed numerical sufficient region | Section 7, rational inequalities | Small spatial r<=1; supplied isotropic units |
| A pole or full Gaussian field at fixed clock order | Open, not an input to this implication | Explicit continuous-spectrum and moment controls in section 8 |

The strongest mathematical validation obligation is independent review of
both the upstream all-affine proof and the new same-state spectral argument.
The full fixed-clock Gaussian limit remains a separate open theorem. The
microscopic law and observable identification are supplied; they do not
follow from this result's research objective or its finite checks.

| Input | Role | Provenance | Open physical bridge |
|---|---|---|---|
| Isotropic four-dimensional clock law and its periodic-limit states | Supplied probability model | Definition in section 1 and the complete same-PR source | Native law and state selection remain open |
| Uniform covariance and both reflections in that state | Provisional mathematical input | Exact source revision and hash in section 1 | Independent proof validation is pending, not a physical axiom |
| Poisson summation, joint spectral theorem and positive matrix integration | Mathematical machinery | Hypotheses and normalization derived in sections 2-6 | No empirical parameter import |
| Bounded score, spatial magnetic components and midpoint units | Chosen observable and coordinate convention | Definitions in sections 1-3 | Empirical identification and absolute speed are not selected |

## 1. Exact input and provenance

The model is the four-dimensional periodic finite-clock Villain law

    theta_e in 2 pi Z/N modulo 2 pi,
    probability(theta) proportional to product_p phi_beta((d theta)_p),
    phi_beta(t)=sum_n exp(-n²/(2 beta)) exp(i n t),
    beta_d=N²/(4 pi² beta).

Fix beta,beta_d >=2000 and any local limit along equal even tori. The
substantial provisional input is the complete proposed theorem in
[the periodic finite-clock covariance source](PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md)
at predecessor revision `d46526dc07fc1f4f6530c7b4d98c1d5feb8f6eee`, source
SHA-256 `bfedf452ec4e5b4b19c7099cb4c5e7ebc69aca4198fbdfba1c8788647ddea237`. Its complete proof is carried in the same PR
and remains unchanged in this addition. In particular we require its all-affine
covariance argument, physical contact identity, and site/link reflection
positivity in the same infinite-volume state. Independent review is pending.

Write P_e,P_c for the infinite-volume exact/coexact two-form projections.
The input gives a bounded positive Fourier density C_n/beta with

    (1-delta(beta)) P_c <= C_n/beta
       <= P_c+delta(beta_d)P_e,     C_n/beta <= I.       (1)

Here delta(s) is exactly the upstream explicit function:

    b1=(107 log3+log4)/(4 pi²), a(s)=s/384-b1,
    q(s)=exp(-2 pi² a(s)), S_j(q)=sum_(r>=1) r^j q^r,
    delta(s)=s[8503056 S_6(q(s))+262144 S_5(q(s))]/[a(s)e].

Finite torus harmonics have already been kept and removed in the local
limit by the input. They are not discarded at finite volume here.

The physical bounded observable is Y_p=-phi_beta'/[sqrt(beta)phi_beta]
at the clock plaquette angle. Put B=(Y_23,-Y_13,Y_12). These three spatial
plaquettes are even under time reflection and live on integer time slices.
Charge conjugation of the specified periodic-limit state centers all scores.

## 2. Physical covariance is uniformly close to the exact projector

Augment the clock law by independent conditional Gaussian image integers:
X_p=sqrt(beta)((d theta)_p-2 pi m_p). Its joint marginal is a centered
Gaussian on a full-rank lattice, with covariance at most I. More strongly,
completion of the square and the nonnegative Fourier coefficients of its
theta function give E exp(h.X)<=exp(||h||²/2). This centered MGF bound uses
only finite-dimensional Poisson summation, not the all-affine input.
Explicitly, write theta=2 pi a/N with integer link representatives. The
integer field z=d a-N m ranges over M_N=N Z^P+d Z^E, and each admissible z
has the same number |ker(d mod N)| of clock/image preimages. Thus
X=z/sqrt(beta_d) has precisely the centered Gaussian law on this full-rank
lattice. Finite Poisson duality from the input gives Cov(X)=I-C_n/beta.

Conditional on theta, image integers on distinct plaquettes are independent,
Y=E[X|theta], and v_p(theta)=Var(X_p|theta)>=0. Translation and cubic
invariance give a common vbar=E v_p. Total covariance and the exact duality
just stated give

    C_Y=(1-vbar)I-C_n/beta.                            (2)

For completeness a uniform explicit bound on vbar follows from the same
centered MGF. Let v be the principal flux angle. If |X_p|<pi sqrt(beta),
then sqrt(beta)v=X_p. Otherwise their difference has magnitude at most
2|X_p|. Conditional expectation minimizes squared prediction error, so

    vbar <=4 E[X_p² 1_(|X_p|>=pi sqrt(beta))]
          <= (8 pi² beta+16) exp(-pi² beta/2)=eta(beta). (3)

The last inequality integrates the Chernoff bound
Pr(|X_p|>=u)<=2 exp(-u²/2). Conditional image variances are bounded functions
of the finite clock angle, so this bound passes to every specified local
limit. We do not need to reconstruct an infinite-volume image process.

Set R=C_n/beta-P_c and

    epsilon=max(delta(beta),delta(beta_d))+eta(beta).

Equation (1) implies -delta(beta)I<=R<=delta(beta_d)I. Therefore

    ||C_Y(k)-P_e(k)||_op <= epsilon                  (4)

for almost every four-momentum k. The contact contribution -vbar I is
retained. No assumption that the score itself is a closed two-form is made.

## 3. Spatial midpoint convention and the transverse block

Fourier transform every spatial plaquette using its spatial midpoint. The
change from lattice-origin Fourier coordinates is a diagonal unitary
depending only on spatial momentum p, so it preserves positivity of the
time spectral measure. Put

    xi_i=2 sin(p_i/2), r²=sum_i xi_i², w²=4 sin(omega/2)²,
    P_T=I-xi xi^T/r², r>0.

In midpoint coordinates the coboundary symbol is exterior multiplication
by i(2 sin(omega/2),xi). Direct exterior algebra gives

    [P_e(omega,p)]_BB = r²/(r²+w²) P_T.

Let S_p(w²) be the compression of the physical B covariance density to
the two-dimensional range of P_T. Equation (4) yields

    ||S_p(z)-[r²/(r²+z)] I_T|| <= epsilon,
    z=4 sin(omega/2)².                              (5)

This holds initially for almost every (omega,p). The spectral representation
below supplies the continuous version at z>0 and the monotone value at z=0.
The longitudinal compression obeys 0<=S_L(z)<=epsilon as well. Small
longitudinal response is allowed; it is not claimed to vanish exactly.

## 4. The positive transfer spectral measure, including contact states

Use the site-reflection OS space on gauge-invariant functions supported at
times >=0. The upstream construction gives a positive self-adjoint
contraction T and commuting spatial translation unitaries. For the B
observables on time 0, their reflected inner product equals their ordinary
equal-time covariance. In particular, for t>=0,

    E[B_i(0,0) B_j(t,x)] = ([B_i],T^t U_x[B_j]).       (6)

This identity has no one-time-step displacement: that displacement was
needed upstream for general slabs including temporal plaquettes. Here the
observables lie on the reflection plane and are time-even.
Time-reflection invariance makes their negative-time covariances equal to
the corresponding positive-time ones, justifying the two-sided sum below.

The joint spectral theorem for T and spatial translations produces a
positive 3x3 matrix measure on [0,1] x the spatial Brillouin torus. Its
spatial marginal is the equal-time covariance, which has a bounded Fourier
density by (4). Hence the joint measure disintegrates as dnu_p(lambda) dp
with the normalized spatial Haar measure understood. Compress nu_p to the
transverse plane. All following matrix inequalities hold for almost every p.

An atom at lambda=1 would create a temporal Fourier atom at omega=0,
contradicting the bounded four-dimensional density. It has zero measure.
An atom at lambda=0 is allowed: it contributes only at t=0 and therefore
a constant Fourier density. This is an infinite-energy/contact component,
and is retained until the positive localization estimate bounds it.

For 0<lambda<1 put E=-log(lambda). Summing the two-sided geometric series
gives the Poisson kernel

    sum_(t in Z) lambda^|t| exp(i omega t)
      =(1-lambda²)/(1-2lambda cos(omega)+lambda²)
      =sinh(E)/(cosh(E)-cos(omega)).                   (7)

The kernel is nonnegative and has normalized temporal integral 1. Tonelli
and uniqueness of Fourier coefficients identify its integral against nu_p
with the covariance density. The kernel is uniformly bounded for omega
separated from 0, giving continuity there. Consequently(5), originally an
almost-everywhere inequality, holds at every 0<z<=4 for almost every p.

Use the energy coordinate u=4 sinh(E/2)². Reweight the measure by

    dchi_p(u)=coth(E/2) dnu_p(E) for E in (0,infinity),
    chi_p({infinity})=nu_p({lambda=0}).

Then the exact Stieltjes representation is

    S_p(z)=int_[0,infinity] [u/(u+z)] dchi_p(u),       (8)

where the integrand at infinity is 1. As z decreases to 0, monotone
convergence and(5) show that chi_p is finite, with

    (1-epsilon)I_T <= chi_p(total) <= (1+epsilon)I_T.  (9)

There is no mass at E=0. Possible unbounded weight near E=0 is ruled out
by this same bound, not by assuming an energy gap. Equation (8) at z=0
means its finite monotone limit. This chi is the static susceptibility
measure; it is different from the ordinary OS spectral weight nu.

## 5. A positive two-frequency localization identity

Fix 0<r<=1 and set a=r², so the two frequencies z=a and z=4a are available
on the lattice. For x>=0, including x=infinity by its limit, define

    Phi(x)=(x-1)²/[(x+1)(x+4)]
          =1/4-(4/3)x/(x+1)+(25/12)x/(x+4).          (10)

This identity is exact. Phi>=0, Phi(1)=0, Phi(infinity)=1, and

    Phi'(x)=(x-1)(7x+13)/[(x+1)²(x+4)²].

It decreases on [0,1] and increases on [1,infinity]. Substituting (8) gives

    0 <= int Phi(u/a) dchi_p(u)
      = chi_p(total)/4 -(4/3)S_p(a)+(25/12)S_p(4a)
      <= (11/3)epsilon I_T.                         (11)

The reference values 1,1/2,1/5 cancel exactly. The upper bound is the sum
of three norm errors with total coefficient 1/4+4/3+25/12=11/3. Positivity
comes from the integral, despite the negative coefficient in this linear
combination. No derivative or analytic continuation of noisy covariance
data is required.

For 0<alpha<1<gamma let

    m(alpha,gamma)=min(Phi(alpha),Phi(gamma))>0,
    I_r=[alpha r²,gamma r²], K=11/[3m(alpha,gamma)].

Equation (11) and the monotonicity of Phi imply

    chi_p(I_r^c) <= K epsilon I_T,
    chi_p(I_r) >= [1-(K+1)epsilon] I_T.             (12)

The complement includes the contact atom at infinity. For every unit
transverse v the fraction of its static susceptibility in I_r is at least

    1-K epsilon/(1-epsilon).                        (13)

This is a statement for positive scalar compressions v*chi_p v; no quotient
of noncommuting matrices is used.

## 6. Ordinary spectral weight and two energy-response directions

Transforming I_r back to energy gives

    J_r=[2 asinh(sqrt(alpha)r/2),
         2 asinh(sqrt(gamma)r/2)].                   (14)

Because dnu=tanh(E/2)dchi, equations (9),(12) give

    sqrt(alpha)r/sqrt(alpha r²+4) [1-(K+1)epsilon]I_T
        <= nu_p(J_r)
        <= sqrt(gamma)r/sqrt(gamma r²+4)(1+epsilon)I_T. (15)

If the lower coefficient is positive, the map from a transverse source v
to its band-projected OS vector is injective. Thus the energy band has two
nonzero response directions for almost every such p. Wave packets with
measurable transverse polarizations give actual Hilbert-space vectors;
point-momentum plane waves are not claimed normalizable eigenvectors.

The interval endpoints are asymptotic to sqrt(alpha)|p| and
sqrt(gamma)|p| as p->0. Both bounds on ordinary band weight are proportional
to r. The conclusion is quantitative low-energy spectral concentration,
not merely the existence of spectral values approaching zero.

Most *static susceptibility* in the band does not imply most equal-time
OS norm there. A small contact weight of order epsilon can dominate a band
weight of order r as r->0. Equation (15) preserves this distinction.

## 7. A fixed-parameter certificate

The upstream delta bound can be sharpened using only elementary rational
inequalities, without estimating a critical coupling. For s>=2000,
log3<11/10, log4<7/5 and pi>157/50 give b1<31/10. Hence

    a(2000)>253/120, 2000/a(2000)<1000,
    2 pi² a(2000)>6236197/150000>59(7/10)>59 log2.

Thus q<2^-59, and s/a(s) decreases with s. The upstream rational identities
for S_5,S_6 imply S_j(q)<=2q for q<=1/1024. Using e>2,

    delta(s)<8765200000/2^59 <1/50000000.             (16)

Also eta(beta) decreases for beta>=2000. The bounds 3<pi<4 and e>2 give
eta(beta)<256016*2^-9000 <1/50000000. Consequently the deliberately loose
choice epsilon_*=1/10000000 bounds epsilon for every admitted beta,beta_d.

Take alpha=9/10 and gamma=11/10. Then

    m=1/1071, K=3927,
    chi_p(I_r)> (1-3928/10000000)I_T,
    [v*chi_p(I_r)v]/[v*chi_p(total)v]>0.9996 for every v!=0. (17)

The last line is the scalar ratio in(13) on the transverse plane.
Over 99.96 percent of each transverse static susceptibility is therefore
in the energy band (14). As momentum tends to 0 its lower and upper slopes
are 3/sqrt(10) and sqrt(11/10), approximately 0.94868 and 1.04881 in the
supplied isotropic units. The example beta=2000,N=16384 remains a fixed
finite clock model satisfying the required dual inequality.

The constants are sufficient bounds for this particular model. They are
not measured speeds, a selected physical normalization, or transition
estimates. Exact E=|p| is not inferred from a narrow interval.

## 8. What this still permits

A positive spectral distribution spread continuously through J_r can meet
the same bounds. The argument does not force a spectral atom, stable
one-particle states, Gaussian joint laws, exactly two total polarizations,
a unique infinite-volume phase, or a local continuous-time Hamiltonian.
It does not bound a group velocity or prove coherent wave-packet transport.
It does identify two robust transverse directions with linear energy scale
in the actual isotropic OS state, conditional on the stated covariance input.

The finite-clock Gaussian limit with both defect species remains open. So
does the selected N=3 penalty-Hamiltonian phase, and the framework's native
law/observable identification. No axiom change is requested or forced.

A precise control preserving the distinction from a pole takes chi uniform
on u in [a(1-h),a(1+h)], with 0<h<1. For z>=0 its Stieltjes function is

    S(z)=1-z/(2ah) log[(a(1+h)+z)/(a(1-h)+z)],
    S(0)=1.

Put b=ah/(a+z). Expanding atanh(b)/b shows

    0<=a/(a+z)-S(z)
      =z/(a+z)[atanh(b)/b-1]
      <= z a² h²/[3(a+z)^3(1-h²)]
      <=4h²/[81(1-h²)].

The last step maximizes x/(1+x)^3 at x=1/2. At h=1/1000 this is below
1/10000000 for every z, but the energy measure has no atom. This is an
abstract positive spectral control, not a claimed alternative realization
of the full four-dimensional clock law. Likewise a Gaussian scale mixture
with equiprobable squared amplitudes 1/2 and 3/2 has unit variance and fourth
moment 15/4. Two-point data do not establish its Gaussianity. Neither control
is used as an axiom obstruction or an assertion about the clock's actual
higher-point functions.

## 9. Finite challenges and author review

The self-contained primary runner is
`scripts/fixed_clock_transverse_spectral_concentration_2026_09_15.py`. It reads no external or repository scientific input and
has no package-local integrity reads or helper runners. Its eight families
are finite mathematical challenges:

| Family | Comparison and actual finite domain |
|---|---|
| Positive localization probe | Symbolic rational identity, derivative, endpoint limits and three exact interval constants |
| Physical score contact | One-plaquette N=5,9 clock controls at beta=2.3; independently computed Gaussian images and Fourier scores at 65 digits |
| Positive transfer | A five-state lazy nearest-neighbor Markov chain; all paths at separations 0 through 5 versus transfer powers and spectral moments; four frequency comparisons |
| Magnetic symbol | Direct origin-based exterior derivative versus midpoint conversion and three magnetic projectors |
| Matrix energy band | Direct Gram projection through a diagonal transfer versus noncommuting positive susceptibility atoms and a two-frequency probe |
| Spectral endpoints | A retained zero-transfer contact atom, a nondecaying invariant atom, and a tiny-momentum example distinguishing static and ordinary weight |
| Continuous spectrum and moments | Uniform continuous spectral measures at three scales and six frequency ratios, independent quadrature, and an exact Gaussian scale-mixture fourth moment |
| Parameters and dispersion coordinate | Exact rational sufficient inequalities and twelve inverse-energy comparisons |

The finite domains are not samples of the infinite-volume clock phase.
The one-plaquette model checks an exact observable identity, and the chain
checks transfer normalization; neither is relabeled a four-dimensional
phase computation. Truncated Fourier/image sums and numerical quadrature
have explicit cutoffs and tolerances, but no certified infinite-series or
quadrature error estimates are asserted.

Sixteen actual source faults were caught: rational-probe coefficient;
physical score sign and normalization; omitted conditional image variance;
displaced time-zero moment; Poisson numerator; reciprocal susceptibility
weight; midpoint phase; magnetic orientation; matrix-probe coefficient;
halved energy; reciprocal ordinary weight; complemented energy band;
deleted contact atom; continuous-density normalization; and an error bound
too loose for the asserted percentage. Direct path enumeration, symbolic
algebra, separate Fourier/image sums, Gram projection and quadrature provide
distinct calculation paths. These remain author checks.

The initial double-precision score comparison exceeded 1e-13 because of
Fourier cancellation, with maximum observed error 3.17e-12. Its exact source
and failure are preserved in the private campaign checkpoint
`24dd899464e2d353da36d2f5a5d72ccc77a5ca3e`, and its receipt is copied into
this PR's review pack as provenance only. At 65-digit precision the same
comparison agrees below 1.5e-62; the final tolerance is 1e-55. No tolerance
was relaxed. The primary runner contains all final scientific checks and
does not consume the private checkpoint or failure receipt.

The complete new proof and runner were read personally after derivation.
The author check preserved contact states, the finite-versus-infinite
momentum distinction, two response directions versus two particle species,
and static versus ordinary spectral weight. Independent review of the full
same-delta input and implication remains required. No audit verdict or
retained status is established by source checks or a cache.

## 10. Primary literature and source comparison

The spectral method is standard. Kouta Usui's
[A Note on Reflection Positivity and the Umezawa-Kamefuchi-Kallen-Lehmann
Representation](https://arxiv.org/pdf/1201.3415), v3, gives a careful lattice
reconstruction discussion. The opening through Theorem 2.1 and the initial
reconstruction, together with complete section 3.3, were read. Its theorem
under link positivity alone treats odd time separations; site positivity
strengthens the transfer statement. Here both reflections are explicit and
the spatial-plaquette time-zero identity is derived directly. No unchecked
version of the literature theorem replaces section 4.

Hao Shen's [harmonic-extension RG paper](https://arxiv.org/pdf/1311.2305),
v2, opening through Proposition 1, was read when considering a full Gaussian
limit. Its scalar-gradient dipole model is not identified with this clock
law. No RG theorem is used in this spectral implication.

## No-Go Discipline Gate

This gate scopes the conditional theorem and the controls against stronger
inferences. It claims no exhausted physical routes or axiom obstruction.

### N1 — Distinct attempted failures and stronger inferences

| Honesty | Object and attempted failure | Disposition and authority |
|---|---|---|
| ATTEMPTED | Observable conditioning: omit the image variance or change the score scale | Section 2 and the independent one-plaquette Fourier/image calculation retain the contact term and normalization. This is author derivation, not retained authority. |
| ATTEMPTED | Time geometry: use the general slab displacement for a reflection-plane observable | Section 4 uses spatial time-even plaquettes at time 0. Exhaustive finite chain paths detect the displaced moment. Both reflection hypotheses stay explicit. |
| ATTEMPTED | Spectral endpoints: assign the response to an invariant state or silently delete a contact state | The bounded Fourier density excludes an invariant atom, while the positive probe retains and bounds contact weight. Both endpoint controls are executed. |
| ATTEMPTED | Vector geometry: use origin phases, a wrong magnetic orientation, or commuting scalar weights to claim the transverse rank | Sections 3,5,6 and separate exterior/Gram calculations preserve midpoint phases and noncommuting matrix measures. The lower band matrix has rank two. |
| ATTEMPTED | Probability and spectral law: infer a pole or Gaussianity from a narrow two-point response | The explicit continuous measure and scale mixture in section 8 preserve these alternatives. The band theorem survives, but the stronger inference is not made. |

These are different observable, time, spectral-endpoint, vector, and
probability objects. Their number is a packet requirement, not a proof of
exhaustiveness. No route is marked ruled out by prior retained authority.

### N2 — Dependency accounting

The substantial provisional input is one same-state covariance/reflection
bundle whose complete proof is in the review delta. The construction does
not count its duality, contact term, or spectral reformulation as independent
framework walls. A full Gaussian limit, a particle pole, and native law
selection remain open; no pairwise independence or implication between
those broader targets is asserted. The continuous control defeats a narrow
inference from two-point bounds alone, not the actual clock model.

### N3 — Hidden-hypothesis scan

The explicit conditions are four dimensions, the supplied isotropic finite
clock law, fixed beta,beta_d>=2000, the chosen periodic-limit state, both
reflections in that state, gauge-invariant time-even spatial scores, midpoint
Fourier coordinates, almost every p with 0<r<=1, and the positive transfer.
The zero-frequency value is a monotone limit; no regularity in spatial
momentum or isolated spectral eigenvalue is assumed. Contact and invariant
atoms receive different treatments. Plane waves are not normalizable states.

### N4 — Exact residual matching

| Source or witness | Residual addressed | Match and use |
|---|---|---|
| Linked covariance source, sections 2-11, exact revision and hash in section 1 | Uniform all-affine covariance, physical contact and same-state reflection positivity | Yes; complete provisional mathematical input inside the same review delta |
| This source, sections 2-7 and the corresponding finite families | Observable normalization, spectral reconstruction and localization | Yes; new analytic implication with finite checks at their disclosed domains |
| This source, section 8 | Inferring a pole or Gaussianity from the two-point bound alone | Yes for that narrow inference; no statement about the actual clock's higher correlations |
| Usui, Theorem 2.1 and section 3.3 | General lattice spectral-representation method | Method context only; the matching time-zero representation is derived here |
| Shen, sections 2.2-2.3 through Proposition 1 | A possible scalar-gradient RG route | Not a matching clock theorem and not counted as mathematical support |

No scalar RG, oscillator or different gravity carrier is used to establish
or refute this clock phase. The separate Regge comparison in N8 concerns
source scope only and supplies no proof premise.

### N5 — Resolution and rhetoric

Per-element calculations test image moments and rational factors. Per-site
calculations enumerate the finite chain. Per-mode calculations compare
midpoint projectors, Poisson kernels and spectral bands. Per-block checks
retain matrix weights, endpoint controls and continuous spectral examples.
The lattice-wide spectral concentration is an analytic conditional
implication, checked and not executed by the finite runner. Its canonical
cache states all five resolutions. Counts do not validate the upstream
uniform phase proof or create independent review.

### N6 — Partial result and remaining physics

Two transverse response directions with linear energy scale are a useful
partial result beyond gaplessness. Fixed-clock Gaussianity, stable particle
states, transport, the selected N=3 Hamiltonian and a native physical law
remain separate questions. The isotropic units and model parameters are
supplied. No axiom, approved primitive, premise registry, or physical
constant is selected or altered.

### N7 — Steelman

A hostile reviewer should first challenge the all-affine covariance proof
and the reflection-positive state match. Their failure invalidates this
application even if the Stieltjes algebra is correct. Conversely a correct
band theorem can still describe a continuous spectrum, and its two response
directions do not establish a photon Fock space. The proof and explicit
controls preserve both objections; finite agreement cannot remove them.

### N8 — Cross-cycle comparison

The same-delta periodic covariance source stopped at observable gaplessness;
this note extracts a quantitative fixed-parameter energy band. The same-delta
Gaussian scaling source obtains a full Maxwell field while varying clock
order and couplings; that stronger limit is not transferred to fixed N here.
At main `5deabeb698a27c2c3f68c5df685af2521ef15307`,
`ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md`,
opening and sections 4-5, checks necessary positive-transfer moments for a
different supplied Regge carrier. Its finite failures neither supply nor
contradict the clock's reflection positivity. No audit status is imported
from any source's historical prose.

## Falsifiers and verification limits

This implication fails if the stated uniform covariance input fails, the
physical contact normalization is wrong, the same state lacks the positive
transfer, the midpoint magnetic compression is incorrect, an endpoint
spectral atom is mishandled, or the positive rational localization identity
and ordinary-weight conversion are wrong. Its explicit finite challenges
address accessible instances; the quantified proof still requires review.

Run the primary executable through `scripts/runner_cache.py` with its
explicit 180-second timeout. It has eight finite families and no helper
runner. Focused source/cache/N5/vocabulary/graph/diff checks precede the PR
update. Full pipeline, strict lint, and exact combined-tree changed-evidence
validation remain shared landing gates after independent review. This author
packet neither merges to main nor applies an audit verdict.
