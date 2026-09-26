# Pre-code reconstruction: fixed-rate geometric matching growth

This is the selective simulation/observable check requested by the primary author. It is not a phase theorem or a replay of the production experiment. Before this document was written I had read the complete fixed-rate protocol and analysis plan and reused the previously checked geometric-partner model at its unchanged identity. I have not read the C++ implementation, wrapper, analyzer, production outputs, screen values, or phase conclusions for this check. Source hashes and lengths alone were inspected for the three implementation files. All subsequent test output will be generated inside this independent directory.

## Intended finite generator

On the even cubic torus of side N (N>=4 in the model, 16 and larger in the declared production grid), let M be a nearest-neighbor matching. Every *unoriented* edge joining two vacancies is a birth channel of rate beta. Every ordered length-two path (a,b,c) with ab in M and c vacant is a slide channel of rate kappa. The two immutable records at a,b move to b,c, respectively, and the matching becomes M-ab+bc. Turns are allowed. This has an inverse channel (c,b,a) at the same rate. There is one slide for each occupied-vacant nearest-neighbor edge bc, since b has a unique partner a. Thus the slide count equals the number of occupied-vacant bonds; it is not doubled for the two descriptions of the occupied dimer. Conversely both endpoints of any occupied dimer may act as the middle b in different channels. Vacant edges are counted once.

With nu=0 as in the follow-up, the exit rate is lambda=beta B(M)+kappa H(M). An Exp(lambda) waiting time, followed by a channel chosen in proportion to its rate, gives the intended generator. Choosing the birth category with probability beta B/lambda and a uniformly random active birth, or the slide category and a uniformly random active slide, is equivalent. At lambda=0 or full occupancy no further events occur. Initial empty even tori have a perfect matching; the already checked augmenting-path result supplies almost-sure finite filling for beta,kappa>0, but it supplies no useful numerical cap or uniform filling-time bound.

Birth eligibility depends on its two endpoints. The slide indexed by middle b and vacant neighbor c depends on b's partner and c's vacancy. After an event every indexed channel with a changed occupancy endpoint must be reconsidered, as must channels whose stored partner changed if the catalog stores triples rather than only (b,c). One must separately check catalog membership, multiplicity, sampling and record-identity updates. Births add two new records; slides only permute the existing records with a vacancy. Total births at full packing are V/2, but a site can participate in repeated births after earlier records leave.

## Staggered field and Fourier normalization

Write n_i(x)=1 if the positive edge (x,x+e_i) lies in M, and sigma_x=(-1)^(x_1+x_2+x_3). Let F_i(x)=sigma_x[n_i(x)-1/6]. On an even periodic torus,

    sum_i [F_i(x)-F_i(x-e_i)] = -sigma_x 1_{x vacant}.

At full occupancy the right side is zero. For the unnormalized site FFT z_i(k)=sum_x exp(-i k.x) F_i(x), define d_i(k)=1-exp(-i k_i). The exact constraint is sum_i d_i z_i=0. The Hermitian longitudinal projector is d* d^T/|d|^2. Accordingly

    S_L(k) = |sum_i d_i z_i|^2 / (V |d|^2),
    S_T(k) = [sum_i |z_i|^2 - |sum_i d_i z_i|^2/|d|^2] / (2V).

Here S_T is *per transverse polarization*. Equivalently multiply each z_i by exp(-i k_i/2) to obtain the bond-centered transform and use the real vector sin(k_i/2). Omitting this component-dependent phase while projecting against the continuum vector k is generally wrong. At k=0 the longitudinal projector is undefined and winding is treated separately.

At full occupancy the plane sum Phi_i(c)=sum_{x:x_i=c} F_i(x) is independent of c. Hence sum_x F_i(x)=N Phi_i, and

    W = sum_i Phi_i^2/(3N) = |sum_x F(x)|^2/(3V).

The field, Gauss constraint and winding are geometric matching observables, not assertions about electromagnetic fields. Capped, nonfull configurations carry the explicit vacancy charge and cannot be silently included among full-state spectra.

## Conditional Gaussian benchmarks

Suppose, as an additional comparison hypothesis only, that the three nonconjugate first-axis Fourier modes are independent circular Gaussian transverse vectors with common per-polarization variance gV, and that the three real zero-mode components are independent centered Gaussians of variance gV. One nonzero mode has two complex polarizations, so S_T/g is Gamma(shape=2,scale=1/2): E[S_T^2]/E[S_T]^2=3/2. The mean of the three independent axis powers has relative second moment 1+1/6=7/6. The winding scalar W/g is chi-square_3/3, with ratio 1+2/3=5/3. Also E W=E S_T=g. These references require the stated independence, equal variances and nonselfconjugate modes. Gauss alone establishes none of these distributional hypotheses.

For a cell, the three reported ratios must be computed as E_history[mean_modes S_T^2]/E_history[mean_modes S_T]^2; E_history[(mean_modes S_T)^2]/E_history[mean_modes S_T]^2; and E_history[W^2]/E_history[W]^2. The first two numerators differ. Shell ratios and winding/shell ratios are ratios of cell means, not means of within-history ratios.

## Statistical unit and boundaries

The sampling unit is a complete independently seeded growth history. First average modes within each history. Bootstrap complete rows, using common resampling indices for every numerator and denominator so correlations within a history are preserved. A pointwise percentile interval describes the empirical resampling law conditional on the recorded sample and completion rule; it is not simultaneous coverage, a simulator correctness guarantee, a fixed-rate thermodynamic limit, or a phase theorem. Failed/capped histories must remain in counts and any exclusion from full-state summaries must be explicit. No production observable value is needed for these code and definition checks.
