# Distinct check: perturbed scalar three-source local amplitudes

Disposition: **conditional support; no correction requested.** The proposed E_local bounds the joint three-site scalar amplitude difference uniformly in time under the pinned scalar robustness premises. It is not actual attached-device escape or complete processor robustness.

Read the complete new ROOT-authored proposal, SHA256 `b36ef9001996fd031bfabd8541776be27831050cac6b67fee1016cf10f04b504`, and the complete ROOT review of the scalar robustness premise. I authored that scalar premise and the nominal scalar source, but did not author this new polynomial/density lemma. Shared ancestry and prior exposure are explicit; I check the new argument rather than advertise a second independent review of my own source.

## Exact spectral representation and signs

For the centered negative-hopping Jacobi operator, the seed and first-site equations give h|0>=d0|0>-a1|1> and h|1>=-a1|0>+d1|1>-a2|2>. Hence the spectral transforms of the three coordinate vectors are exactly

    1, -(delta-d0)/a1,
    [(delta-d0)(delta-d1)-a1^2]/(a1 a2).

The signs in the target are correct. Site-2 detuning and the last coupling affect the seed spectral measure but do not occur in these first two polynomial recurrences. Real coefficients make the polynomials real on the spectrum. The spectral theorem then gives the displayed vector integral, including the common carrier exp(-i2jt), for all real times. This is a linear vector-amplitude formula, not an inference from probabilities or a conjugation of an input state.

The nominal coordinate vectors are orthonormal, so their three spectral polynomials have L2(rho0) norms one and joint squared norm three. In particular the nominal second moment is lambda^2/3. The normalization and absence of residual scalar mass are essential here. They are supplied by the separately checked scalar robustness theorem for both perturbed and nominal isolated chains: real-band/threshold nonzeros and the exterior determinant bounds exclude missing point/singular mass. This lemma does not independently prove or extend that fact to an interacting downstream system. The pointwise density ratio is needed only almost everywhere on the band; zero-density threshold endpoints cause no division problem.

## Perturbation constants

Let alpha=a/a1 and beta=ab/(a1a2). Subtracting the polynomials gives the exact identities stated in the proposal. In particular the second-polynomial numerator change is

    -delta(d0+d1)+d0d1-a^2 e1.

The sign of the a^2 e1 term is negative, as written. The coefficient bounds are

    |alpha-1|<=1/sqrt(1-epsilon)-1,
    alpha<=1/sqrt(1-epsilon),
    |beta-1|<=epsilon/(1-epsilon), beta<=1/(1-epsilon).

For p1 the constant detuning term has norm at most sqrt(3)epsilon/sqrt(1-epsilon), giving B1. For p2 the linear-detuning, squared-detuning and bond-square terms, before beta, respectively have bounds

    sqrt(3/2)epsilon,
    (3/sqrt(8))epsilon^2,
    epsilon/sqrt(8).

These use ||delta||_L2(rho0)=lambda/sqrt(3) and ab=(2sqrt(2)/3)lambda^2. Adding the beta-1 term gives precisely B2. All scales cancel as claimed, while detunings are still required to be small relative to lambda. The joint difference has L2 norm at most sqrt(B1^2+B2^2), and its L1 norm is at most the same because rho0 has mass one. No false orthogonality of the different perturbation terms is assumed; the scalar triangle bounds are conservative.

## Density ratio and time-uniform joint bound

The pinned complex packet estimate |F_e/F_0-1|<=L implies

    ||F_e/F_0|^2-1|<=2L+L^2.

This remains valid even when L is not small. The no-hidden-mass premise ensures there are no extra amplitudes outside the displayed density integrals. The subtraction order

    p_e rho_e-p_0 rho_0=(p_e-p_0)rho_0+p_e(rho_e-rho_0)

is correct. The first vector integral has norm at most Bpol. For the second, the density ratio bound times Cauchy–Schwarz gives D_rho||p_e||_L2(rho0), and triangle inequality bounds that norm by sqrt(3)+Bpol. Every real-time Fourier factor has modulus one, proving E_local exactly as stated.

The source projection of each normalized evolved seed has norm at most one, so the trivial difference bound two is valid. For t>=0, adding this difference to the independently checked nominal joint-source bound F(lambda t)+Evec gives the stated perturbed local ceiling, with the further norm-one truncation. All three coordinates, including both intermediary populations, are included. Pole splitting, individual resonance locations and a Markov replacement are unnecessary for this argument.

## Scope and evidence

The estimate compares the perturbed isolated scalar source with a fixed nominal source, retaining their actual detuning-induced spectral phases through the exact Fourier integrals. It does not prove a full scalar-state norm comparison, an attached common outgoing waveform, loaded complementary-channel stability, actual omitted spectral mass, finite-time processor accuracy, or native precision. The pending actual moment source is not used. Those limitations are accurately stated in the proposal.

The qualified scalar premise is `three_site_source_robustness/PROPOSAL.md` at `32456b0b5c99ad1acfcdc9a770d022ffcc14069dee157981c715177cfa6a7eb6`, with distinct review `ba06cef2ddf0aae45eeaf5f5c8740258babe21d2a8206fbf6c1eb7b3b33f97ad`. Its nominal scalar source/check remain `a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823` / `c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b`. Those source identities and their stated hypotheses are reused, not a blanket recertification of the larger ancestry.

No numerical integration, dynamics, parameter sweep, scientific runner, Git/canonical/PR/checkpoint/prompt/model edit or delegation occurred. Only this review was created. No actual attached/time robustness result is promoted.
