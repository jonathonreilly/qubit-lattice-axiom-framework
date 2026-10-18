# Focused native energy-fluctuation moment check

Disposition: PASS for the exact infinite-temperature moments, spectral concentration, conserved overlap, and finite-volume high-temperature coefficient under the stated supplied model/state. These are not a nonzero beta-zero susceptibility or a physical scalar identification. No repository edits or formal audit.

## Exact moments

Use normalized Hilbert-Schmidt trace. Distinct nearest-neighbor bond Pauli strings are orthogonal, including their signs and Fourier phases. There are V bonds per orientation, so m0=sum_a Ja² exactly.

For each perpendicular orientation pair a,b there are four unordered incident bond pairs per site, with centers displaced by (s ea-t eb)/2, s,t=±1. Each commutator has squared HS norm4Ja²Jb². The sum of the four squared phase differences is8[1-cos(qa/2)cos(qb/2)]. This gives

    m2=32 sum_(a<b) Ja²Jb²[1-cos(qa/2)cos(qb/2)].

The resulting three-site Pauli string determines its right-angle center and endpoint axes uniquely on the stipulated large torus. Thus distinct corners cannot interfere; same-axis pairs commute. Lengths at least5 avoid the short-wrap aliases relevant to this argument.

An independent bit-Pauli enumeration on a5³ torus, with anisotropic J=(.7,1.1,1.3) and allowed q=(2pi/5)(1,2,1), finds1500 distinct corner strings and m2=72.4624484313303, matching72.4624484313297 from the formula. m0=3.39. The implementation and output are neutral-energy-moment-independent.py/json.

Expanding the cosine product gives m2=4 sum_(a<b)Ja²Jb²(qa²+qb²)+O(|q|^4). At isotropy this is8J^4|q|²+O(|q|^4); dividing by3J² gives(8/3)J²|q|²+O(|q|^4). All prefactors check.

## Spectral meaning

The displayed spectral measure is positive even though E_q need not be Hermitian: its coefficients are absolute matrix-element squares. Its mass is m0 and second moment is ||[H,E_q]||HS². Chebyshev therefore gives the normalized bound

    mu_q(|omega|>Omega)/m0 <= m2/(m0*Omega²).

For fixed nonzero isotropic J and Omega=J|q|^alpha, 0<alpha<1, this tends to zero as O(|q|^(2-2alpha)). On finite tori q must be an allowed reciprocal momentum; the exact uniform formulas permit a compatible growing-volume sequence. No assumed existence of a limiting spectral density is required for this concentration statement.

This proves low-frequency concentration of fluctuation weight. It does not distinguish elastic weight from a narrow inelastic component, exclude a broad distribution inside the shrinking window, or prove a delta pole, diffusion, relativistic dynamics, or a zero-temperature excitation. At q=0 the measure is exactly conserved zero-frequency weight.

At beta0, the expectation of EVERY commutator is zero by cyclicity of the trace, including the retarded E_q/E_-q response. Thus the root correctly separates this positive fluctuation measure from a nonzero susceptibility. A finite-beta response or a beta-rescaled classical limit would be a different statement.

## Q overlap

For Hermitian Ha,

    <[Ha,[H,Ha]],H>_HS = -||[H,Ha]||HS².

Each perpendicular axis pair contributes16V Ja²Jb² to the squared commutator for each of its two axes. Thus <Q,H>=-32V sum_(a<b)Ja²Jb², giving -96VJ^4 at isotropy. Since <H²>=3VJ², the ratio is exactly-32J². This independently checks the sign and coefficient without assuming the proposed Q decomposition.

In the nested Pauli commutator, the two-site outputs arise only when the outer bond repeats one of the original perpendicular bonds; otherwise a nonzero output has four sites. Cubic symmetry makes the native two-site component proportional to H. Hence Q=-32J²H+Q4 with Q4 HS-orthogonal to H is consistent with the same calculation. Projection of Q/sqrt(V) onto conserved H/sqrt(V) gives zero-frequency mass at least1024J^4*3J²=3072J^6. Other conserved components may add more. Without the full norm of Q this is an absolute lower bound, not a fraction. The q=0 overlap alone does not establish a finite-q Q-density projection.

## Original distance-two readout

At beta0 Cz is HS-orthogonal to H. In the finite-volume Gibbs expansion the first nonzero term comes from two adjacent z bonds: each distance-two path occurs twice in H², canceling the expansion factor1/2. Therefore <Cz>=V beta² Jz²+O(beta³). Differentiating with respect to beta gives cov(Cz,H)=-2V beta Jz²+O(beta²), and var(H)=V sum Ja²+O(beta), yielding the stated g_C(beta). The covariance is legitimate here because H generates the Gibbs derivative; no generic noncommuting quantum response covariance is being substituted.

These expansions are finite-volume coefficients. Uniform thermodynamic remainders require the separately stated cluster/locality control. The Gibbs state and beta remain supplied, and Cz is directional. Neither this conditional overlap nor the neutral energy fluctuation determines a physical detector coupling, cosmological state, or autonomous scalar field.
