# Energy–composite bridge from the same interaction

Root derivation, 2026-10-18. Existing supplied H=K sum_(x,a) sigma_x^a sigma_(x+e_a)^a, one qubit/site. Define e_x=(K/2)sum_a sigma_x^a(sigma_(x−e_a)^a+sigma_(x+e_a)^a) and C_x=sum_a sigma_(x−e_a)^a sigma_(x+e_a)^a, so C_x=2e_x²/K²−3I. No microscopic interaction is added. Gibbs preparation, K and the compass law remain premises. There is no fitted or independent observational dataset in this block.

## Exact tracial symmetry identities

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

A single-oscillator fit to F2 and F4 would choose omega²=8K². It then incorrectly predicts F6=−1024K⁸|q|². The coefficient comparison is retained as a diagnostic. The single-oscillator exclusion interpretation is deferred; this package does not promote an exclusion of spectral poles.

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
