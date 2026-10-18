# Finite-order native local normal form for neutral composites

Status: conditional bounded mathematical bridge, with focused equation checks and a final scoped review. No empirical data, cosmological identification, exact native pole or selected ground state is claimed. The supplied directional Hamiltonian, positive rung parity, periodic tube geometry, strong longitudinal regime and explicitly prepared state remain premises.

Dependencies: [complete scalar band and local wall proof](NATIVE_SCALAR_BAND_LOCAL_PROOF_NOTE_2026-10-18.md), [zone-boundary coefficients and crossover](NATIVE_ZONE_BOUNDARY_COMPOSITE_NOTE_2026-10-18.md), and [native domain readout derivation](NATIVE_NEUTRAL_DOMAIN_RESONANCE_NOTE_2026-10-18.md).

Replay: [native_local_normal_form.py](../scripts/native_local_normal_form.py), covering exact local cancellation, canonical K2 and leading packet controls. The analytic uniform proof is stated separately below.

## Native starting point

Use Jz energy units and dimensionless time. On the positive-parity four-physical-qubit rung space,

H = 4 N + lambda V + constant,
N = sum_j (4 - sum_a Z_(j,a) Z_(j+1,a))/4,
V = sum_j h_j, lambda = Jperp/Jz.

All bond number operators commute and have eigenvalues 0, 1, 2. The periodic N=0 sector consists of eight uniform colors. N=2 is exactly the two-distance-two-wall band. These statements do not extend unchanged to open boundaries or unequal asymptotic colors. Each h_j is the existing transverse directional interaction; no coupling is appended.

## Local inversion without a volume denominator

For a local operator A define

P(A) = (2 pi)^(-1) integral_0^(2 pi) exp(i t N) A exp(-i t N) dt,
T(A) = sum_(m != 0) A_m/m,
[N,T(A)] = A - P(A).

The integer energy-difference filter has norm at most pi times the operator norm. Since the bond terms commute, only bonds touching the original support enter the rotation: P and T enlarge a rung interval by at most one rung at each end. T sends Hermitian operators to anti-Hermitian operators. These maps commute with every symmetry preserving N.

Set S1=T(V)/4. Then [S1,4N]=-(V-P(V)); the first two diagonal coefficients are

D1=P(V), D2=P([S1,V])/2.

D2 has the same fixed-N matrix elements as the canonical second-order resolvent P V Q (E-H0)^(-1) Q V P. The native 512-dimensional periodic three-rung check reproduces the complete N=2 K2 matrix exactly, after the previously derived vacuum subtraction. A central three-rung check also verifies the vacuum annihilator used below. Finite checks support the algebra, not the uniform theorem by themselves.

Recursively, at order k remove the off-diagonal coefficient A_k with S_k=T(A_k)/4 and retain D_k=P(A_k). At any fixed order n this uses finitely many connected local commutators and local filters. Every coefficient therefore has finite range depending on n, not volume. Symmetry averaging can be applied to each local coefficient, preserving its range, Hermiticity and norm bound. It makes every retained term separately N-conserving and invariant under the global color operations.

## Explicit local BCH control

For an interval interaction A={A_I} use

a_mu(A)=sup_x sum_(I containing x) exp(mu |I|) ||A_I||.

If delta=mu-mu'>0, decomposition into overlapping intervals gives

a_mu'([A,B]) <= (4/delta) a_mu(A) a_mu(B).

Indeed, the two cases x in I or x in J cost the interval length; |I| exp(-delta |I|)<=1/delta, and each commutator costs a factor two. Assign delta/m of decay loss to each of m nested commutators. Using m! >= (m/e)^m yields

a_mu'(ad_S^m A)/m! <= [4 e a_mu(S)/delta]^m a_mu(A).

Thus exact local conjugation converges for 4 e a_mu(S)<delta. Split a fixed decay margin among the n conjugations. The generators are finite-range coefficients multiplied by lambda^k, so a small complex-lambda disk exists at every fixed n, uniformly in ring length. The convergent composition is analytic there. Formal cancellation through n and its Cauchy Taylor remainder then imply

Y_n H Y_n^(-1) = D^(n) + R_n,
D^(n)=4N+sum_(k=1..n)lambda^k D_k,
a_mu'(R_n) <= C_n |lambda|^(n+1).

For real lambda, Y_n is unitary. R_n is quasilocal, not finite range. Constants and the allowed lambda interval can deteriorate strongly with n; this does not assert an exponential lifetime or a useful numerical interval. It avoids the invalid global operator norm estimate proportional to volume.

## Uniform restriction to a few walls

Take a Hermitian local coefficient d_I commuting with N and invariant under the global color operations. Its uniform-color diagonal value c_I is independent of color. If the configuration is uniform on I and adjacent rungs, any nontrivial local change creates positive walls while leaving the outside unchanged. N conservation forbids it. Consequently, with Q_I the projector onto at least one wall on a bond touching I,

d_I-c_I I = Q_I (d_I-c_I I) Q_I.

Let a_k=sup_x sum_(I containing x)||d_I||. Since Q_I is bounded by the sum of touched wall projectors, on the W-wall subspace

sum_I ||d_I|| Q_I <= 2 a_k W,
||D_k-E_vac,k|| <= 4 a_k W.

For periodic N=2, W=2 and the bound is 8 a_k, independent of circumference. This uses a termwise symmetry-preserving decomposition, not cancellation only after summing the Hamiltonian. Circumferences must exceed every retained support. On N=0 the truncated operator acts as a scalar; any specified vacuum superposition is stationary for D^(n). The dressed image Y_n^(-1)|vac> is an explicitly prepared state, not a derived exact-H ground state.

## Conditional mode and finite-time physical scope

The native reflection/checkerboard identity at q=pi makes all odd coefficients vanish in the chosen scalar N=2 fiber. The uniform restriction therefore has relative excitation operator

8 + lambda^2 K2 + O(lambda^4).

The previously derived reflection-even halfline K2 has isolated level 9/16, decay ratio 1/4, residue 15/16 and original-source weight 15 lambda^2/4. Ordinary isolated-eigenvalue stability applies to the finite-order normal-form fiber for sufficiently small lambda. It does not give an exact-H pole. The finite-ring-to-halfline limit and the fiber must remain explicit. This is a lattice-zone-boundary excitation, not a long-wavelength relativistic scalar.

At q=pi-lambda*kappa away from the two known thresholds, the crossover operator supplies the analogous candidate. Near the upper threshold its binding is proportional to lambda^2 delta^2; omitted lambda^4 terms require delta much greater than lambda. Arbitrary feature size at fixed lambda is not controlled.

For a fixed local observable, Duhamel comparison and a capped one-dimensional Lieb-Robinson bound give

||tau_(D+R)(O)-tau_D(O)|| <= C_n(O) |lambda|^(n+1) (|t|+t^2).

The cap inside the light cone is essential; a bare exponentially growing bound would not establish this estimate. Use the same state and consistently dressed observables in the two frames. This compares finite-time dynamics, not equilibrium spectral measures.

For a packet O_f=sum_j f_j O_j with sum|f_j|^2=1 and M sites, sum|f_j|<=sqrt(M). Sum the translated local error bounds first, then multiply by the other correlation factor. The connected two-time correlation error is bounded by

C_n M |lambda|^(n+1) (1+|t|)^2.

At t<=T lambda^(-2), choosing n=7 and M=ceil(lambda^(-3/2)) makes this O(lambda^(5/2)), smaller than the predicted O(lambda^2) readout weight. Packet momentum width 1/M is also smaller than lambda. This establishes a possible norm-control regime; proving spectral concentration and a lower visible packet signal is a separate step. A time filter with uniformly bounded L1 kernel preserves the error bound. No infinite-time delta-function pole follows.

## Open obligations

Focused checks confirm the interaction-norm estimate, few-wall restriction and packet argument with the stated source and finite-ring qualifications. Quantify the small-lambda interval and constants before claiming numerical usefulness; a finite-duration measurement needs an explicit filter truncation. State preparation, equal-coupling continuation, three-dimensional isotropy, physical units and the relation to measured gravity remain open. No observational test has been performed in this block.

## Explicit packet lower signal (root continuation)

Choose the compact sine envelope

f_j=(-1)^j sqrt(2/(M+1)) sin(pi j/(M+1)), 1<=j<=M,
M=ceil(lambda^(-3/2)).

Its Fourier distribution has the exact centered discrete-Laplacian moment

integral 4 sin^2((q-pi)/2) |fhat(q)|^2 dq/(2pi)
=4 sin^2(pi/(2(M+1))).

With eta=lambda^(1/8), the probability outside |q-pi|<=lambda eta is at most the right-hand side divided by 4 sin^2(lambda eta/2), hence O(lambda^(3/4)). In the remaining window kappa tends uniformly to zero. The isolated crossover eigenvector consequently approaches the odd-edge state of residue 15/16. The inherited native source is 2 lambda cos(q)|E1> at leading order. Its mode contribution is therefore (15/4+o(1))lambda^2, provided the uniform fiber/source bounds below are retained.

The first-order source can be checked directly: on any uniform vacuum, [S1,O_j]|vac>=(h_j+h_(j+2))|vac>/2 for O_j=sum_a Z_(j,a)Z_(j+2,a). Distinct single-rung flips are orthogonal and ||h_j|vac>||^2=4. Hence the leading source Gram kernel is 2 delta_(r,0)+delta_(r,2)+delta_(r,-2), with Fourier density 4 cos^2(q). This recovers the source normalization without an assumed detector coupling.

The required higher-order source bound is stronger than its global operator norm. Let B_j=[Y_n O_j Y_n^(-1)-O_j] minus its vacuum mean. Because O_j has the same constant action on every uniform color, B_j has exactly the centered dressed-source vector on that vacuum. Unlike merely centering the full operator, this difference has a quasilocal norm beginning at lambda; the order-zero centered operator need not vanish as an operator. For a single product vacuum, disjoint centered local terms have zero covariance. For the symmetric vacuum cat, the same follows because each local term is color invariant and thus has the same mean in every uniform color; the union of the two supports, when proper, cannot connect distinct uniform vacua. Terms whose supports cover the ring are bounded by the exponentially decaying dressing tails; for L much larger than lambda^(-2) these wrap contributions are negligible compared with the target powers. Equivalently one may first work in the infinite-volume mixture of uniform phases. Exponentially decaying dressing tails give a uniformly summable Gram kernel, with sum_r |<B_0 vac,B_r vac>|<=C lambda^2. The convolution operator bound then gives ||sum_j f_j B_j vac||^2<=C lambda^2. Applying the same argument to the order-two source remainder gives vector norm O(lambda^2), uniformly for normalized f. The outside-window contribution is thus controlled without multiplying by M. This argument uses the declared prepared vacuum and invariant readout; it is not a general clustering assertion for exact-H ground states.

For fixed finite normal-form order, each local term only moves a wall by a bounded distance. After vacuum subtraction its momentum fiber is a bounded finite-range operator on the separation coordinate, with uniformly bounded momentum derivatives. The two-wall coefficient bounds therefore also control the infinite-separation fiber. Near pi, K1=2 cos(q/2) times its nearest-separation adjacency has a cubic Taylor remainder. The explicit K2 coefficients depend on cos(q), so their variation is quadratic in q-pi. Reflection/checkerboard symmetry suppresses D3 at pi and its first momentum derivative is bounded; coefficients of order four and above are uniformly bounded. Thus with q=pi-lambda*kappa the respective corrections after dividing by lambda^2 are O(lambda^2), O(lambda^2), O(lambda^2), and O(lambda^2). Consequently the scaled operator converges uniformly on bounded kappa windows to the previously derived crossover operator, with an O(lambda^2) error. The isolated eigenprojection near kappa=0 is stable. The corresponding finite-ring approximation converges when both wall-separation cutoff and circumference grow; for a dynamical infinite-line comparison choose L much larger than lambda^(-2), as well as M.

These steps establish a lower packet signal for the finite-order normal form under the stated asymptotic and prepared-state conditions. A separate focused check confirmed the source Gram and fiber arguments after the explicit difference-source, finite-cat union and quadratic K2 refinements.

A smooth frequency window supported around 8+lambda^2(9/16), narrower than the other-mode separation in scaled units, has a rescaled Schwartz time kernel. Integrating the all-time local comparison against that kernel uses its finite second moment and preserves the O(lambda^(5/2)) error. Thus it can transfer a filtered correlator signal to the exact Hamiltonian in the explicitly dressed prepared state. The exact-H state is generally nonstationary: the transferred object is not asserted to be a positive equilibrium spectral measure or an infinite-time pole. A literal finite-duration experiment additionally needs a stated time-window truncation bound.

Method reference: the volume-independent propagation estimate uses the bounded-interaction Lieb-Robinson theorem and its exponentially decaying spatial form, Theorem 2.3 of [Nachtergaele and Sims, 2010](https://arxiv.org/abs/1004.2086). Combining that bound with the trivial commutator bound inside the cone and summing the quasilocal remainder gives the one-dimensional polynomial-time comparison used here. The normal-form algebra and packet argument above are supplied explicitly rather than inferred from that reference.
