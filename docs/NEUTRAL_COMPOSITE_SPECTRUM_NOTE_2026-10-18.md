# Neutral composite features in the supplied one-qubit-grid candidate

**Type:** bounded_theorem
**Status:** partial-narrowing; independently checked conditional mathematics and development numerics; unaudited. This does not claim a general no-go packet PASS.

Runner: [neutral_composite_spectrum.py](../scripts/neutral_composite_spectrum.py).

Inputs: [stored candidate](../data/collective_corner_response/candidate.json), with provenance in the [previous response note](COLLECTIVE_CORNER_RESPONSE_NOTE_2026-10-17.md). The earlier qubit encoding distributes a chosen coarse-cell model across one-qubit fine sites; it does not derive a uniform fine-grid Hamiltonian, a self-bound fermion, or a physical background state.

The objective is to derive a neutral mode and its source coupling without supplying another interaction. The observational bridge would require a propagating response with a derived transformation law, normalization and consistent source/detector behavior. This block tests those prerequisites inside the existing supplied candidate. No observational dataset is fitted or independently tested. The numerical ensembles and source choices are exposed model-development inputs.

The coherent result has two parts: extended neutral preparations can be constructed and checked, but exact spectral certificates constrain how they can become sharp. The certificate extends beyond bilinears to finite-degree balanced composites under explicit regularity and state assumptions. It does not settle arbitrary qubit Hamiltonians or cosmological identification.

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

If the source spectral measure has no atom at omega, any normalized sequence with r tending to zero must have source overlap tending to zero. First hold epsilon fixed while r tends to zero, then send epsilon to zero. This is a conditional theorem, not evidence that this Hamiltonian's thermodynamic spectral measure has no atom. Finite grids always have discrete transition atoms. A physical limiting claim requires control of volume and state before arbitrarily fine spectral filtering.

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

## Consequence in the infinite-volume bilinear space

For any real frequency omega, det(L_Q(k)-omega I) is a real-analytic function on the connected momentum torus. If its zero set had positive Lebesgue measure, it would vanish identically. Then omega would be a common root at the two certificate points, contradiction. Thus each frequency level set has measure zero.

For square-integrable bilinear source coefficients, the spectral measure is obtained by integrating finite-matrix spectral projections against momentum Lebesgue measure. A frequency atom would require positive-measure support on the corresponding level set. There are therefore no frequency atoms in this fixed-Q bilinear space. The same inference holds with absolutely-continuous positive thermal weights; it does not cover singular state measures or delta-function probes.

Combining this with the residual/source-overlap bound in NEUTRAL_FEATURE_DERIVATION.md shows: at fixed infinite-volume operator, metric and normalized source, any normalized bilinear sequence whose frequency residual tends to zero at a fixed omega must have source overlap tending to zero. Arbitrarily extending a bilinear feature does not evade this statement. Generalized single-transition delta functions are outside the square-integrable domain. Finite boxes still have discrete transition lines.

## What this does and does not settle

This closes the exact flat-transition exception for the supplied fixed-Q bilinear channel. It does not establish a smooth spectral density, a rate of overlap loss, a dispersion law, a higher-composite obstruction, or an absence theorem for all one-qubit Hamiltonians. The supplied mass source is a pseudoscalar upstream, so this result cannot be relabelled as a general scalar-field theorem.

The original parameter values and intended unrounded construction are not silently identified with their stored decimals. A separately checked exact rational residual enclosure gives cross-spectrum separation greater than 8.241208801e-7 at the same two momenta. The property persists when every complex hopping entry changes in modulus by less than 2.4527407145e-9, provided hopping-pair Hermiticity is preserved. The bound follows from seven12-dimensional hopping blocks: each Hamiltonian changes by at most84epsilon in operator norm, and the separation of two transition spectra can fall by at most336epsilon. This is a certified neighborhood, not an identification of any particular unrounded upstream construction.

The research decision is to keep the constructive approximate excitations as useful conditional evidence and move toward symmetry-correct channels and genuinely higher composites. The source, dynamics, background state and physical measurement bridge still need derivation.


## Higher neutral composites: independently checked conditional extension

This is an independently checked mathematical extension, not a physical identification. Keep its state/domain assumptions separate from the existing bilinear certificate.

Consider a fixed finite n and a balanced n-creation/n-annihilation operator of total momentum q in the same translation-invariant quadratic fermion Hamiltonian. Parametrize its kernel by annihilation momenta k1,...,kn and creation momenta p2,...,pn, with

    p1=q+sum_i ki-sum_(i>=2) pi.

The corresponding finite internal fiber generator is the sum of n creation Hamiltonians minus n transposed annihilation Hamiltonians. Its dimension is d^(2n) before fermionic antisymmetry. Every matrix entry and its characteristic determinant is real analytic in the independent momenta because h is a finite Fourier polynomial. CAR antisymmetry restricts the allowed kernels and cannot introduce a frequency absent from this full fiber matrix.

Suppose some real omega is an atom for an absolutely-continuously weighted square-integrable kernel. The fiber matrix must have eigenvalue omega on a positive-measure set. Its characteristic determinant is therefore identically zero by real analyticity. This conclusion applies to the unrestricted analytic determinant, including its continuation to coincident-momentum configurations; it does not require a nonzero fermionic wavefunction on those configurations.

Now restrict spectator momenta pi=ki=ai for i>=2, with each ai fixed. Then p1=k1+q. The fiber generator is a Kronecker sum of the bilinear L_q(k1) and a finite constant spectator generator C. Let the finite eigenvalues of C be delta_j, with multiplicity. The restricted characteristic determinant is

    product_j det(L_q(k1)-(omega-delta_j)I).

If the bilinear determinant is not identically zero at any real frequency, every factor here is a nonzero real-analytic function. A finite product of such functions cannot vanish identically on a connected torus. This contradicts the assumed identity.

Thus the bilinear non-flat-frequency property implies absence of frequency atoms at the same total q for every fixed finite balanced degree, in the specified L2 kernel space with absolutely-continuous weights. This proof does not require a numerical search over the exponentially large higher-degree matrix.

## Boundaries requiring explicit retention

- It is the same supplied free Hamiltonian. Existing interactions in another one-qubit model are not ruled out.
- Fixed total q=Q is the certified application here; other momenta remain separate questions.
- This is an infinite-volume L2 statement, not removal of finite-box lines.
- Singular momentum distributions and singular state measures are outside the stated domain.
- Finite-degree Wick-ordered kernels in a stationary quasifree thermal state give a clean application. Arbitrary un-ordered products need their contractions/domains handled before use.
- Passing from each finite degree to an infinite sum requires an actual Hilbert direct-sum decomposition and a self-adjoint generator preserving it. Do not assume that step for arbitrary large-feature limits or encoded-sector states.
- The result does not prove decay rates, smooth spectral density, scalar transformation law, canonical coupling, or a cosmological relation.

The constructive implication is that if this theorem is confirmed, merely assembling more neutral free fermionic factors cannot produce an isolated sharp mode at Q within this regular domain. The next productive questions become which native nonquadratic dynamics or different symmetry/momentum channel the microscopic qubit Hamiltonian actually supplies, and whether that supply can be derived rather than chosen.

## Independent checks, failures, and reproduction

The analytic zero-set step uses the established theorem in [Mityagin, *The Zero Set of a Real Analytic Function*](https://arxiv.org/abs/1512.07276); its application to this particular stored candidate is supplied by the exact certificate above. No novelty is claimed for free bilinear closure, spectral filtering, or the zero-set theorem.

The [campaign evidence pack](../.claude/science/physics-loops/neutral-composite-24h-20261018/) contains separate reports for the spectral metric, parity, filtering, resolvent bound, higher-composite proof, modular computation and rational enclosure. Independent direct144-dimensional characteristic polynomials match every coefficient. Independent momentum-space norms and thermal matrix covariances agree with the finite-range computation. Exact rational enclosure replay matches the recorded separation bound. These are independent checks, not formal audit verdicts.

A real numerical failure was found and repaired: unscaled adaptive quadrature missed the narrow Gaussian second-moment peak at tau256 and returned zero. Rescaling the integration variable and checking against analytic Gaussian moments repaired it. The corrected pure-continuum width is .002762135864, not zero. The parity probe also had an ordinary NumPy-integer JSON serialization failure; explicit conversion repaired it. Neither operational failure supports a physics conclusion.

Run `OPENBLAS_NUM_THREADS=1 python3 scripts/neutral_composite_spectrum.py`. It reproduces the exact certificate, rational enclosures, finite-range constructions, independent momentum check, synthetic atom control, unrestricted filters and parity control. The higher-degree statement is an analytic proof, independently checked; the runner does not numerically enumerate its exponentially large matrices. Development outputs are in `outputs/neutral_composite_spectrum/result.json`. Exploratory earlier scans remain in the pack and do not carry the exact theorem.

## No-Go Discipline Gate

**Disposition: partial-narrowing, not a general no-go packet PASS.** The five-family submission quota is not established. This is a submission limitation separate from the stated conditional proof. No claim is made that every one-qubit-grid route has been exhausted.

**N1 — Alternatives.** The actual mechanisms examined here are free neutral spectral composites (onsite, extended and higher-degree constructions) and source-selected narrow preparations. These related calculations are not inflated into five independent route families. Singular macroscopic/state representations, different momentum/symmetry channels and genuinely interacting microscopic Hamiltonians remain unclosed alternatives. No retained authority is invented to close them.

**N2 — Dependencies.** The spectral result depends jointly on supplied quadratic dynamics, analytic translation-invariant coefficients, the certified momentum and the regular positive-metric domain. These are hypotheses of one implication, not a counted set of independently proved physical walls. The higher-degree result follows from the bilinear certificate; it is not an independent obstruction.

**N3 — Hidden conditions.** Exact decimal inputs, the coefficient neighborhood, L2 kernels, total momentum, fixed source in the overlap limit, state metric, finite versus infinite volume, and selected frequency are explicit. The chosen thermal state is not a derived initial state. A source norm is not a canonical matter coupling. The coarse-cell qubit embedding is not a derived uniform fine-grid law.

**N4 — Residual matching.** The earlier response note supplies the exact model identity and source definition; it is not cited as proof of absent atoms. The independent modular certificate addresses fixed-Q flat transition frequencies. The higher-composite proof addresses regular balanced finite-degree kernels of the same free model. No earlier environmental or single-flux result is used to dismiss a different composite mechanism.

**N5 — Resolution.** Per-entry Hermiticity and rational arithmetic are checked; per-mode fixed-Q spectral structure and per-block finite-range operators are checked. The lattice-wide implication is the stated analytic L2 theorem. Native fine-site dynamics, all momenta, all representations and a cosmological measurement map are not checked. The runner prints this execution scope explicitly.

**N6 — Partial closure.** Approximate neutral excitations with appreciable source overlap are constructed and preserved. Derived source response is useful conditional structure even without a scalar particle. Reframing a preparation or choosing canonical units does not alter a spectral atom, but other existing microscopic terms or a different representation could change the question. No claim that a new physical axiom is logically required is made.

**N7 — Steelman.** A large feature may live in a different symmetry channel, a nonquasifree state or a macroscopic representation not captured by regular finite-degree kernels. It may be a sufficiently long-lived resonance rather than an exact pole, and its operational coupling could require a different normalization than our source overlap. The present theorem does not dismiss those possibilities; each needs its own microscopic construction and observational criterion.

**N8 — Prior-wall comparison.** Earlier failure of an onsite or single-flux probe did not exclude neutral composites. This block explicitly enlarged the operator class and found constructive approximate modes before deriving its scoped spectral certificate. Its next route must similarly challenge the remaining representation, symmetry and native-dynamics assumptions; repeating this fixed-Q free-model obstruction would add no closure.
