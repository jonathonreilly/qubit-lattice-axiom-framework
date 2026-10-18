# Large energy features and their composite overlap in the one-qubit compass model

**Type:** bounded_theorem. **Status:** conditional-support, independently checked mathematics and development controls; unaudited.

Runner: [native_energy_features.py](../scripts/native_energy_features.py).

The result is a broad slow energy feature with a derived, state-dependent composite overlap, under the supplied native Hamiltonian and thermal preparation. It does not establish a scalar particle, stable fermion, universal matter coupling, or empirical validation. The earlier exact native transport is in [the transport note](NATIVE_COMPOSITE_TRANSPORT_NOTE_2026-10-18.md).

## Energy–composite bridge from the same interaction

Root derivation, 2026-10-18. Existing supplied H=K sum_(x,a) sigma_x^a sigma_(x+e_a)^a, one qubit/site. Define e_x=(K/2)sum_a sigma_x^a(sigma_(x−e_a)^a+sigma_(x+e_a)^a) and C_x=sum_a sigma_(x−e_a)^a sigma_(x+e_a)^a, so C_x=2e_x²/K²−3I. No microscopic interaction is added. Gibbs preparation, K and the compass law remain premises. There is no fitted or independent observational dataset in this block.

## An exact failed linear route

At each integer site define Pauli conjugation signs f(X)=x+z, f(Y)=y, f(Z)=x+y+z modulo2. Since f(Z)=f(X)+f(Y), these signs are implemented by conjugation with an onsite Pauli. The resulting local-algebra automorphism sends H to −H, e_x to −e_x, and C_x to C_x. It is valid on Z³ and compatible even periodic tori; odd periodic seams break it.

In normalized trace, the mixed correlation S_Ce(r,t)=tr[C_0(t)e_r] is odd under t→−t by this automorphism and even by time reversal. Therefore S_Ce(r,t)=0 exactly for every r,t. Equivalently, even derivative overlaps vanish by the sign symmetry and odd ones by Pauli-word weight parity. Direct local enumeration through four commutators confirms the cancellation, but the symmetry proves all orders and all times.

This is not a proof of absence of thermal or ground-state coupling. It also means that a bulk inference drawn from a symmetry-breaking odd thin torus would be unreliable.

## The state activates a mixed response

Write <A>_beta=tr(exp(−beta H)A)/tr(exp(−beta H)). For a formal probe −f(t)e_r, use chi_Ce(r,t)=i theta(t)<[C_0(t),e_r]>_beta. A probe defines a response function; it is not an autonomous term adopted into H.

The beta^0 coefficient is zero by trace cyclicity. The beta^1 coefficient is −beta dS_Ce/dt=0 by the preceding theorem. Define

F_r(t)=tr[H{C_0(t),e_r}]/2.

Since [H²,A]={H,[H,A]} and D=i[H,.],

chi_Ce(r,t)=beta² theta(t) dF_r(t)/dt+O(beta³).

This formula is a high-temperature coefficient at fixed t, not a finite-beta approximation with a supplied error bound. In finite compatible systems the same symmetries actually make chi even in beta. Temperature is not determined here.

## Exact local coefficients

The runner compass_thermal_bridge.py enumerates F_n(r)=tr[H{D^n C_0,e_r}]/2 at K=1. The output stores 2F_n as integers. A product contributing to the trace must match two native bond words, so only derivative words of weight at most4 need be tested. All incident possibilities are enumerated, rather than estimating the trace with random vectors.

F0: center3; six nearest centers1/2; elsewhere0.
F2: center−48; twelve face diagonals4; elsewhere0.

Restoring units, F_n carries K^(n+2). In momentum space:

F0(q)=K²[3+sum_a cos(q_a)],
F2(q)=K⁴[−48+16 sum_(a<b)cos(q_a)cos(q_b)].

For small dimensionless q, F2(q)=−16K⁴|q|²+O(q⁴). Thus the first time coefficient of the beta² mixed response is proportional to an energy-profile gradient. For a deliberately chosen broad Gaussian source profile of widthR, its leading center coefficient is proportional to 48[exp(−1/R²)−1], approaching −48/R². This profile is a diagnostic preparation, not a derived stable fermion. The short-time gradient dependence is not a proof about the long-time infrared force.

The next exact coefficients have small-q limits

F4(q)=128K⁶|q|²+O(q⁴),
F6(q)=17664K⁸|q|²+O(q⁴).

A single-oscillator fit to F2 and F4 would choose omega²=8K². It then incorrectly predicts F6=−1024K⁸|q|². Preserve this failed closure: the full leading-gradient response is not that one oscillator. This does not exclude an isolated low-energy pole plus other spectral weight.

An independent binary-Pauli implementation verifies every coefficient through n6, including all93 nonzero displacements at n6. A direct512-dimensional Gibbs calculation on an explicitly open9-qubit graph verifies chi/beta²→F'(t) at three times and four beta values. This dense control validates the expansion/sign on its graph; it does not substitute small-graph numbers for the bulk coefficients.

## Uniform source and preparation are different operations

Summing e_r gives H. In a stationary Gibbs state <[C_0(t),H]>=0 exactly, so the uniform closed-system retarded response vanishes. The computed sums of F_n vanish for every n>0, providing a conservation control.

In contrast, changing H to (1−f)H and re-equilibrating at fixed beta changes the preparation. Local linked traces give tr(C_0 H²)=6K² and therefore <C_0>_beta=3beta²K²+O(beta⁴). The uniform isothermal derivative is consequently −6beta²K²+O(beta⁴). This is consistent with zero isolated retarded response: re-equilibration requires a state-changing operation. A cosmological environment map cannot silently interchange these limits.

## An actual conserved collective component, with a strict scope

In a finite nonaliasing compatible periodic volume (for these leading static coefficients, an even cubic side L>=6 suffices), let C=sum_x C_x and center C,H by their Gibbs means. The thermal positive inner product defines the exact projection

C_parallel = a(beta) (H−<H>),
a(beta)=Cov(C,H)/Var(H).

Because H is conserved, this component is stationary. Ordinary thermal derivatives yield

<C>/N=3beta²K²+O(beta⁴),
<H>/N=−3beta K²+O(beta³),
a(beta)=−2beta+O(beta³).

At beta0, Var(C)/N=3 and Var(H)/N=3K². Thus the fraction of the C variance certified in this conserved projection is 4beta²K²+O(beta⁴). The full zero-frequency spectral weight can be larger. This is a standard conserved-quantity projection (Mazur/Suzuki reasoning), not a newly invented mechanism: see https://arxiv.org/abs/2007.04562 . The finite-volume projection is exact; a thermodynamic or finite-q pole assertion requires additional limiting arguments.

This derives a state-dependent energy overlap without fitting a coupling. It does not produce an independent propagating scalar particle, canonical scalar normalization, stable matter source, or universal gravitational coupling. Calling the conserved q0 component a massless boson would be an overclaim. The next useful target is the finite-q energy dynamics and whether its derived response can support a genuine large-feature mode, rather than assume a diffusion law or a relativistic propagator.

## Relation to the observation-facing target

The current-main LARGE_FEATURE_SPECTRAL_RECONSTRUCTION_NOTE_2026-10-17.md identifies the actual conditional comparator: common gap response A must accompany inverse inertial-curvature response1/A, with independently derived clock/ruler responses L=U/g. The present thermal overlap does not compute those quantities, and this native compass candidate has not been identified with the corner Hamiltonian used in that note. No common-scale response, matter identity, clock or ruler is supplied by naming C a composite. A useful next result must either construct and test that shared microscopic bridge or record a failure and pursue a different candidate; these distinct Hamiltonians cannot be spliced by terminology.

## A slow large feature without another interaction

Root calculation, conditional on the same native compass H and initially the normalized tracial operator inner product. This constructs an extended operator excitation, not a self-bound particle or a selected physical state.

Let E_f=sum_x f_x e_x, with real square-summable f. Its normalized residual at frequency zero is r_f=||i[H,E_f]||/||E_f||. Finite-support approximants define the same limit for a Gaussian envelope. Exact translation kernels in compass_energy_modes.json use E_x=2e_x/K, hence divide stored kernels by4 and restore K powers.

For a momentum component, the norm per site is

N_e(q)=K²[3/2+(1/2)sum_a cos q_a],
N_De(q)=K⁴[24−8 sum_(a<b)cos q_a cos q_b].

At q=(pi,pi,pi), e_q itself is the zero operator and normalized ratios are undefined there. The following limits concern q near zero. At q=0 the second expression is zero by energy conservation. The first is3K². Near zero,

r_q²=(8/3)K²|q|²+O(q⁴).

For f_x=exp(−|x|²/(2R²)), Parseval and Gaussian rescaling give

r_f²=4K²/R²+O(R^−4).

This is a constructive large-feature estimate obtained from the existing bond interaction. It does not add a boson, a kinetic term, a phenomenological propagation speed or another qubit per site. Square-summability makes the fluctuation-normalized packet distinct from an exactly uniform infinite operator. The Hilbert norm here is the tracial fluctuation norm, not the operator norm or a particle wavefunction norm.

Unitary dynamics in this operator Hilbert space gives the exact inequality

||E_f(t)−E_f||/||E_f|| <= |t| r_f.

Thus for any selected tolerance epsilon the normalized feature changes by no more than epsilon for |t|<=epsilon/r_f. For largeR this guaranteed time grows as epsilon R/(2|K|). A Chebyshev spectral bound also gives weight outside |omega|<=Omega no greater than r_f²/Omega². These are bounds on slowness and spectral concentration, not on ballistic motion or a relativistic pole.

The fourth-moment kernel is192K⁶|q|²+O(q⁴); its normalized value is64K⁴|q|²+O(q⁴). For Gaussian packets the fourth moment is96K⁴/R²+O(R^−4), not of orderR^−4. Therefore one cannot set a sound speed from the second moment and call the whole response a single oscillator. A shrinking amount of higher-frequency weight is compatible with the residual bound and these higher moments. Diffusive, ballistic, anomalous or other infrared behavior still requires actual long-time information.

The Gaussian sum runner compares cutoffs8R and10R, at widths1,2,4,8,16,32. AtR32, R²r_f²=3.9995117585 and R²m4=96.0507593210, approaching the exact asymptotes4 and96. These are numerical development controls of an analytic asymptotic, not empirical observations.

At beta0, the C/e mixed channel vanishes. The finite-temperature calculation in THERMAL_BRIDGE_DERIVATION.md supplies a nonzero conserved-energy projection of the uniform composite, with coefficient−2beta+O(beta³) and certified variance fraction4beta²K²+O(beta⁴). The fixed-temperature section below supplies the required uniform control on an explicit high-temperature family. The tracial constants4 and96 are not silently assigned to the thermal metric. The candidate state, finite-q mode, normalization and matter/source identifications remain separate questions.

A physically prepared density perturbation proportional to E_f can be defined in a finite system at sufficiently small amplitude to preserve positivity. That construction would be a supplied preparation, not a derivation of a stable fermion or of the background history. The observed clock/ruler and universal-matter comparator has still not been matched.

## Fixed-temperature large features: controlling the change of metric

Root derivation, independently checked. The physical hypotheses remain the supplied compass Hamiltonian and a high-temperature Gibbs state. This result does not derive the preparation or identify temperature with a cosmological field.

## Current follows from the same bonds

For E_f=sum_x f_x e_x, let p be a site, a<b two axes, s,t=±1, c the remaining axis, and epsilon_abc the Levi-Civita sign. Direct commutation gives

D E_f = −K² sum_(p,a<b,s,t) epsilon_abc [f_(p+t e_b)−f_(p+s e_a)] sigma_(p+s e_a)^a sigma_p^c sigma_(p+t e_b)^b.

Indeed E_f weights each bond(i,j) by(f_i+f_j)/2. Combining the two orderings of a pair of touching bonds leaves the difference of these weights; the shared endpoint cancels. Parallel-axis bonds commute. This proves the displayed identity. Compact-support integer profiles independently exercise the exact Pauli identity in energy_current_identity.py. No current or interaction coefficient is fitted.

## Mathematical high-temperature input

[Kliesch et al., Locality of temperature](https://arxiv.org/pdf/1309.0816), Theorem2 and Corollary2, bound generalized Gibbs covariances and finite-buffer errors uniformly in volume. Ordinary covariance is included at the parameter endpoints. For interaction norm J and animal-growth bound alpha, their window is |beta|<log[(1+sqrt(1+4/alpha))/2]/(2J). We use this mathematical result, not a physical state-selection rule.

For this bond graph J=|K|. Each bond touches at most ten other bonds. A rooted connected set of m bonds admits a deterministic spanning-tree depth-first walk of length2(m−1) in that adjacency graph. The walk identifies the visited set, and there are at most10^(2m−2) such walks. Thus alpha=100 is a safe, deliberately loose bound. K=0 is excluded from this scale formula and is trivially static.

The theorem implies summable connected correlations for the finite set of local current types above. Its decay factor b=alpha exp(2|beta|J)[exp(2|beta|J)−1] is O(|beta|) near zero. We need no numerical claim that the entire clustering window has a chosen susceptibility lower bound.

## Residual in the thermal metric

Center operators by their thermal means and write ||A||_beta²=<A†A>_beta. Let J_(p,a,b,s,t) be the unit-norm three-spin Pauli word in the current. Time reversal sets its mean to zero. Exponential clustering supplies the finite Schur constant

M_beta = sup_i sum_j |<J_i J_j>_beta|.

Applying the Schur bound to the exact current sum gives

||D E_f||_beta² <= K⁴ M_beta sum_(p,a<b,s,t) |f_(p+t e_b)−f_(p+s e_a)|².

For the widthR Gaussian the last sum divided by sum_x f_x² is12/R²+O(R^−4). The energy covariance is absolutely summable; its Fourier transform S_e(q,beta) is continuous and nonnegative. At beta0, S_e(0,0)=3K². Local finite-buffer continuity and a uniform summable tail imply continuity of S_e(0,beta), so it remains positive on some smaller open interval around zero.

For a broad Gaussian, convolution and dominated convergence yield

Var_beta(E_f)/sum_x f_x² → S_e(0,beta).

This is a low-momentum packet statement, not a lower bound for every envelope. The checkerboard source e_(pi,pi,pi) is identically zero. Combining the estimates proves, at each fixed beta in the smaller interval,

limsup_(R→infinity) R² ||D E_f||_beta² / Var_beta(E_f)
 <= 12K⁴ M_beta / S_e(0,beta) < infinity.

Stationarity makes the thermal operator dynamics unitary, so the same exact time-change inequality as in the tracial calculation holds for centered E_f. Thus broad slow features are not an artifact of using beta=0. No diffusion constant, wave speed or particle pole has been presumed.

## Uniform composite overlap

Apply the same covariance summability to C_f=sum_x f_x C_x. For fixed beta the largeR normalized overlap tends to

S_Ce(0,beta)/sqrt[S_C(0,beta) S_e(0,beta)].

Continuity alone is insufficient to assign its beta derivative. To obtain the leading coefficients uniformly in volume, truncate covariance sums beyond a fixed sufficiently large support distance. The bound b^distance and the polynomial growth of distance shells make the tail O(beta^m), for any prescribed finite m after choosing a sufficiently distant fixed cutoff. For the finitely many remaining pairs, a fixed wider buffer gives a local-state error O(beta^(m+1)) by the locality estimate. Finite-box Taylor coefficients therefore determine the thermodynamic coefficients through the required order. The bond-reflection symmetry makes the mixed susceptibility odd and both diagonal susceptibilities even in beta.

The already enumerated local traces give

S_Ce(0,beta)=−6beta K²+O(beta³),
S_e(0,beta)=3K²+O(beta²),
S_C(0,beta)=3+O(beta²).

Hence the limiting normalized overlap is −2beta |K|+O(beta³), and its square is4beta²K²+O(beta⁴). The projection coefficient in energy units is S_Ce/S_e=−2beta+O(beta³). These are distinct normalizations. For sufficiently small fixed nonzero beta the overlap is nonzero while the energy-feature residual tends to zero as R grows.

This establishes a shared slow component under stated thermal premises. It does not identify the whole composite with that component, retire the temperature/history input, produce an autonomous relativistic scalar, or derive a universal matter coupling. In particular the small-inverse-temperature interval is existential beyond the explicit clustering threshold; no numerical safe interval for all the strengthened conclusions is claimed.


## Static-mediator test: slowness is insufficient

The same high-temperature theorem bounds the imaginary-time covariance uniformly in its parameter. The isothermal response to a weak local source −f e_0 is

chi_static(x)=beta integral_0^1 cov_tau(C_x,e_0) d tau.

It therefore decays exponentially in separation in the phase used above. Its Fourier transform is bounded and analytic near real q=0; there is no1/|q|² static singularity in this local channel. Equivalently, the quadratic cross term in equilibrium free energy for two distant weak local probes is exponentially bounded. One may not reinterpret the long-lived broad energy packet as a massless long-range force mediator on this evidence.

This rules out that specific static-response identification in the verified high-temperature phase. It does not rule out a short-range scalar, an additional tensor sector, different phases or preparations of the same Hamiltonian, nonlinear sources, or a critical limit outside the controlled window. No general one-qubit-grid obstruction is claimed. The distinction is useful for the observations-first program: the response must pass the required static-range comparator as well as a slowness test. The next state/phase route must be explicit rather than chosen retrospectively to supply the missing pole.
