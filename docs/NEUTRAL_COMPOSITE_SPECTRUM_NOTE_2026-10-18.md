# Neutral composite features in the supplied one-qubit-grid candidate

**Type:** bounded_theorem
**Status:** conditional constructive mathematics and development diagnostics; unaudited. Negative spectral conclusions are explicitly deferred.

Runner: [neutral_composite_spectrum.py](../scripts/neutral_composite_spectrum.py).

Inputs: [stored candidate](../data/collective_corner_response/candidate.json), with provenance in the [previous response note](COLLECTIVE_CORNER_RESPONSE_NOTE_2026-10-17.md). The earlier qubit encoding distributes a chosen coarse-cell model across one-qubit fine sites; it does not derive a uniform fine-grid Hamiltonian, a self-bound fermion, or a physical background state.

The objective is to derive a neutral mode and its source coupling without supplying another interaction. The observational bridge would require a propagating response with a derived transformation law, normalization and consistent source/detector behavior. This block tests those prerequisites inside the existing supplied candidate. No observational dataset is fitted or independently tested. The numerical ensembles and source choices are exposed model-development inputs.

This note promotes extended neutral preparations, their positive norm bounds and exact finite certificate computations. The infinite-volume spectral exclusion and higher-degree extension are preserved separately as deferred scientific arguments, because their negative packet is incomplete.

## Neutral large features from the supplied quadratic Hamiltonian

Status: direct-root derivation and numerical controls, independently checked. This is conditional reconstruction from the existing candidate, not a derivation of that Hamiltonian from observations. No additional interaction is adopted.

## What would resolve the requested obstacle

A useful scalar candidate needs a neutral propagating response, the correct transformation law, stable spectral weight in the large-system limit, and a source/detector coupling obtained from that same microscopic law. A selected narrow-band preparation alone does not satisfy these requirements. In particular the inherited staggered mass operator has a pseudoscalar interpretation upstream; its neutral character does not establish an ordinary scalar. A measured cosmological identification remains open.

## Exact bilinear dynamics

For H=sum_k c_k^dagger h(k)c_k, take O_q[M]=sum_k c_(k+q)^dagger M(k)c_k. Then

    [H,O_q[M]]=O_q[L_q M],
    L_q M=h(k+q)M(k)-M(k)h(k).

This closure follows from canonical anticommutation and does not add a boson. With h(k)=sum_s exp(ik.s)B_s and M(k)=sum_r exp(ik.r)M_r, the coefficient at r+s is

    exp(iq.s)B_s M_r-M_r B_s.

A range-R input generally has range-(R+1) output for this nearest-coarse-cell hopping. Retaining that output is essential: projecting it away would mistake boundary leakage for an eigenoperator. The implemented optimization retains it.

Let A=L_q-omega on these finite-support inputs, s the normalized original source, and eta>0. The selected vector is proportional to

    (A^dagger A+eta I)^(-1)s.

This minimizes ||Av||^2+eta||v||^2-2 Re<s,v> before normalization. It is a source-regularized response construction, not the lowest residual among every normalized vector and not a proof that no dark mode exists.

## Two distinct metrics

The coefficient calculation uses the Hilbert-Schmidt momentum norm integral tr(M^dagger M). Parseval gives the sum of coefficient norms. In the chosen free stationary ensemble the physical positive structure norm instead weights transitions by

    f(E_a(k))[1-f(E_b(k+q))]|(U_(k+q)^dagger M U_k)_(ba)|^2.

It includes both signs of transition frequency. Positive-frequency retarded weights would give a different metric. The two norms cannot be interchanged: the radius-3 example has HS overlap squared .37416 but thermal overlap squared .90518. Neither number is a normalized relativistic scalar coupling. Thermal parameters and the matrix source are supplied development choices.

The R3,eta=.001 feature at N24 has mean frequency .259081 and standard deviation .061280 in model units. It is a moderately coherent neutral preparation with appreciable source overlap, not an established sharp pole. Fourier residual agrees with direct momentum evaluation on N16 and N24 to better than 1e-10. N8 can alias the squared output polynomial and is not used for this exact check.

## A bound for arbitrary large features

Work in a positive stationary operator Hilbert space with self-adjoint L (quotient null operators if necessary). Normalize s and v. For chosen omega let r=||(L-omega)v||. Cauchy-Schwarz applied to the positive operator K=(L-omega)^2+eta gives

    |<s,v>|^2 <= (r^2+eta)<s,K^(-1)s>.

This bound does not require v to be a bilinear or a chosen filter, provided the dynamics and metric satisfy the stated hypotheses. For spectral projector P_epsilon onto |L-omega|<=epsilon, another bound is

    |<s,v>| <= sqrt(<s,P_epsilon s>)+r/epsilon.

The promoted results are the two displayed positive bounds. Their no-atom asymptotic consequence is preserved as a deferred negative theorem, without N1 packet approval. Finite grids always have discrete transition atoms. A physical limiting claim requires control of volume and state before arbitrarily fine spectral filtering.

## Constructive filters and their limitation

In an unrestricted spectral space, the source-regularized filter multiplies each source transition by 1/[(Delta-omega)^2+eta]. Writing epsilon=sqrt(eta), and assuming a smooth, nonzero normalized source density s0 near the center, its normalized overlap squared behaves as 2*pi*s0*epsilon and residual squared as epsilon^2. Multiplying the filter by eta changes no normalized result. A genuine source atom instead retains finite overlap as the filter narrows. Synthetic continuum-plus-atom controls distinguish these cases without pretending to be observations.

N36 thermal results at eta=.1,.01,.001,.0001,.00001 give overlaps squared .9280,.8105,.4888,.2066,.0733. The corresponding spreads are .06635,.04509,.02327,.00878,.00270. This is evidence of a narrowing/overlap tradeoff in the tested source, with finite-grid sensitivity at the narrowest filter. It is not a general no-go for neutral composites, arbitrary interactions already present in other candidate Hamiltonians, or one-qubit-per-site systems.

## Remaining imports and next discriminator

The supplied hopping matrices, encoded sector, chosen ensemble, source symmetry and frequency center remain inputs. No action selector, scalar mass, canonical normalization, universal matter coupling, cosmological background or bound fermion feature has been derived here. The next useful discriminator is whether a symmetry-correct neutral channel or higher composite has stable pole weight and autonomous dynamics, rather than continuing to sharpen a chosen pseudoscalar continuum preparation indefinitely.

Numerical ensemble caveat: these thermal results use grand-canonical weights, not exact finite-box parity projection; the separate parity derivation controls that distinction only under its stated sector and finite-box assumptions. Fixed q=Q supplies no dispersion law. Frequency-centered operators generally need not be Hermitian.


## A scoped spectral certificate for the supplied neutral channel

This is a conditional mathematical result for the stored candidate, not an exclusion of one-qubit-per-site physics or a conclusion from observed data. The supplied Hamiltonian remains a development input.

At total momentum Q=(pi,pi,pi), the bilinear Liouvillian is multiplication by the Hermitian144-dimensional matrix

    L_Q(k)=I tensor h(k+Q) - h(k)^T tensor I

in column-major vectorization. Its characteristic polynomial is monic of degree144. No common root exists between the characteristic polynomials at the two rational unit-circle momentum triples stored in probes/exact_no_flat_transition.json.

## Exact certificate

Every decimal literal in data/collective_corner_response/candidate.json is interpreted as the exact rational it spells. Exact hopping-pair Hermiticity is checked. Unit-circle phases (a+i b)/c satisfy a²+b²=c² exactly. All matrices at the selected points therefore have entries in Q(i).

Reduce the coefficient ring Z[i,1/D], for the finite set of denominators involved, modulo prime p with a chosen square root of -1. This is a ring reduction, not a field embedding of Q(i). Neither prime1009 nor1013 divides the denominators. The two characteristic polynomials have gcd1 after reduction, independently for both primes. Hence their reduced resultant is nonzero. The exact resultant cannot be zero, so their exact characteristic polynomials are coprime over Q(i), and have no common complex root.

The primary calculation uses trace convolution of the two12-dimensional Hamiltonians and Newton identities. An independent checker constructs the144-dimensional matrix entry by entry and uses similarity to Hessenberg form and its characteristic-polynomial recurrence. All145 coefficients match at both momenta for both primes. Additional direct determinant evaluations provide controls. One successful prime would suffice; the second is redundancy.

Controls are sensitive to real changes: replacing Q by0 gives a common polynomial factor of degree12 (conserved bilinears), and replacing the Hamiltonian by0 gives degree144. No empirical fit or chosen scalar interaction enters this certificate.

## Deferred spectral conclusions

The original infinite-volume absence-of-atoms argument, finite-degree higher-composite extension and their source-overlap obstruction are preserved as deferred scientific source. They are not promoted claims of this note. Their submission has only the actually examined related route families; the five-family N1 minimum has not been established. The complete frozen argument remains recoverable from the source-package recovery map, with its exact hypotheses and calculations. No correctness rejection or general no-go approval is implied by this deferral.

The promoted results are the constructive bilinear evolution, positive norm bounds, source-regularized preparations, synthetic controls and finite exact certificate computations. A future promotion of the deferred theorems needs a qualifying residual-matched packet and independent confirmation.

## Independent checks, failures, and reproduction

The deferred analytic zero-set argument uses the established theorem in [Mityagin, *The Zero Set of a Real Analytic Function*](https://arxiv.org/abs/1512.07276); its historical application to this stored candidate is preserved in the deferred original argument and is not promoted by the finite certificate alone. No novelty is claimed for free bilinear closure, spectral filtering, or the zero-set theorem.

Original campaign reports, preserved in the recovery archive described by the source package (`outputs/neutral_composite_review_2026_10_18/README.md`), record spectral-metric, parity, filtering, resolvent-bound, higher-composite, modular-computation and rational-enclosure checks. Those historical reports record agreement of direct144-dimensional characteristic polynomials, momentum norms, thermal covariances and enclosure replays. They are provenance, not fresh execution evidence or formal audit verdicts.

The original campaign records a real numerical failure and its repair: unscaled adaptive quadrature missed the narrow Gaussian second-moment peak at tau256 and returned zero. Rescaling the integration variable and checking against analytic Gaussian moments repaired it. The corrected pure-continuum width is .002762135864, not zero. The parity probe also had an ordinary NumPy-integer JSON serialization failure; explicit conversion repaired it. Neither operational failure supports a physics conclusion.

Run `OPENBLAS_NUM_THREADS=1 python3 scripts/neutral_composite_spectrum.py`. It reproduces the exact certificate, rational enclosures, finite-range constructions, independent momentum check, synthetic atom control, unrestricted filters and parity control. The deferred higher-degree argument is analytic; the runner does not numerically enumerate its exponentially large matrices or supply its missing negative packet. Development outputs are in `outputs/neutral_composite_spectrum/result.json`. Exploratory earlier scans remain in the recovery archive and supply no promoted theorem.

## Source package and execution provenance

The source package (`outputs/neutral_composite_review_2026_10_18/README.md`) preserves the mathematical arguments and lists the live helpers, declared inputs and deferred negative conclusions. Supporting proofs for this note are NEUTRAL_FEATURE_DERIVATION.md (`outputs/neutral_composite_review_2026_10_18/proofs/NEUTRAL_FEATURE_DERIVATION.md`), SCOPED_SPECTRAL_CERTIFICATE.md (`outputs/neutral_composite_review_2026_10_18/proofs/SCOPED_SPECTRAL_CERTIFICATE.md`), HIGHER_NEUTRAL_COMPOSITES.md (`outputs/neutral_composite_review_2026_10_18/proofs/HIGHER_NEUTRAL_COMPOSITES.md`), INDEPENDENT_POLAR_MATH.md (`outputs/neutral_composite_review_2026_10_18/proofs/INDEPENDENT_POLAR_MATH.md`). The primary runner hashes these source files as explicit inputs. Original campaign execution reports are historical provenance, not current execution or audit authority. Fresh bounded reproduction is recorded separately by the integration coordinator.
