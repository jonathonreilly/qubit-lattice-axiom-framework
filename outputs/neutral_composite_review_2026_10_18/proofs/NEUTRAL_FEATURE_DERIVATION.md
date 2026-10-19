# Neutral large features from the supplied quadratic Hamiltonian

Status: direct-root exploratory derivation and numerical controls, awaiting source review. This is conditional reconstruction from the existing candidate, not a derivation of that Hamiltonian from observations. No additional interaction is adopted.

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
