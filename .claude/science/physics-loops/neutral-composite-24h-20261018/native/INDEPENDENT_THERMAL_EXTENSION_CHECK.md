# Native thermal bridge: order-six closure test and energy projection

## Independent order-six check

Extended the independent binary-symplectic local algorithm through D^6 C0. It generates1,007,304 distinct Pauli words at order6 and independently matches all93 nonzero order6 thermal-overlap displacements in the root JSON, plus every lower-order entry. Script/result:
- `/private/tmp/native-thermal-bridge-check/extension_check.py`
- `/private/tmp/native-thermal-bridge-check/extension_result.json`

The local-coordinate representation has no periodic boundary. Products were evaluated with integer coefficients. An initial exhaustive thermal scan was stopped for avoidable memory/time cost and preserved as `extension_v1_expensive_scan.py`; the successful version skips Pauli weights other than2 or4, since multiplying a two-site bond cannot turn any other even weight into a two-site H bond. This changes no nonzero trace contribution. Both owned processes have finished; no mathematical failure was inferred from the expensive scan.

For the root's stored twice-F coefficients Q_n(r), the coefficient of q_a² in F_n(q) is exactly

    −(1/4) sum_r Q_n(r) r_a².

For each of the three axes the independent results are

    F2(q)=−16 K^4 |q|²+O(q^4),
    F4(q)=+128 K^6 |q|²+O(q^4),
    F6(q)=+17664 K^8 |q|²+O(q^4).

Uniform sums vanish for all positive derivative orders as required by energy conservation; odd orders vanish.

## What single-oscillator closure fails

Suppose the **entire leading-gradient beta² response coefficient** were one regular undamped oscillator,

    chi(q,t)/beta² = A(q) sin[Omega(q)t]/Omega(q),
    A(q)=−16K^4 |q|²+O(q^4),
    Omega(q)²=Omega0²+O(q²).

Matching t and t³ terms fixes Omega0²=8K². It then predicts

    F6(q)=−1024 K^8 |q|²+O(q^4),

contrary to the checked +17664. Equivalently, the leading-gradient closure residual F6+8K²F4 equals18688 K^8 |q|². Momentum corrections to Omega² or amplitude at orderq² cannot repair this leading-q² mismatch.

This rejects that specific whole-channel single-frequency closure. It does not exclude a pole accompanied by other spectral weight, damping, multiple modes, an emergent low-frequency pole outside the short-time truncation, or a different state. The mixed response has signed channel weights and should not be treated as a positive single-mode structure measure. No oscillator frequency has been physically inferred merely because two coefficients temporarily fit it.

## Thermal projection onto conserved total energy

Let C=sum_x C_x, delta C=C−<C>, delta H=H−<H>, and use the stationary positive thermal operator inner product <A^dagger B>_beta. Because H commutes with the density matrix, Cov(C,H)=<delta C delta H> is real and the orthogonal projection coefficient is

    a_beta=Cov(C,H)/Var(H).

For a nonaliasing periodic cubic volume N, the elementary infinite-temperature traces are

    tr(H²)=3NK²,
    tr(C²)=3N,
    tr(CH)=0,
    tr(CH²)=6NK².

The last identity counts the two ordered nearest-bond paths for each of the3N distance-two C terms. On compatible even tori the spectral-reflection automorphism makes <C> even in beta and <H> odd. Consequently

    <C>/N=3 beta² K²+O(beta^4),
    <H>/N=−3 beta K²+O(beta³),
    Cov(C,H)=−partial_beta<C>=−6N beta K²+O(beta³),
    Var(H)=−partial_beta<H>=3NK²+O(beta²),
    a_beta=−2 beta+O(beta³).

The coefficient has inverse-energy units and multiplies delta H, not a dimensionless energy observable. More explicitly the higher term scales as beta³ K² when K is the only Hamiltonian energy scale.

The fraction of centered C's thermal norm carried by this one conserved projection is

    f_H = Cov(C,H)²/[Var(C) Var(H)]
        =4 beta² K²+O(beta^4 K^4),

since Var(C)/N=3+O(beta²K²). This is nonnegative and small only in the stated high-temperature regime.

Finite-volume qualifications matter: choose nonaliasing even periodic tori, e.g L>=6, or state the thermodynamic bulk coefficients. L3 and L4 have the previously identified bond aliases, and odd periodic tori lack the exact reflection automorphism. The formula is not a claim for every small finite cluster. Open boxes require their actual bond/boundary counts.

## Spectral and hydrodynamic meaning

Delta H is exactly conserved. Its projection therefore provides a zero-frequency component of the global centered-C structure measure. The fraction f_H is the weight of **this projection**, hence a lower bound on the total elastic fraction, not necessarily the entire elastic weight. Other conserved functions/operators and finite-size diagonal components can contribute. For example a projection onto functions of H is not exhausted by H alone.

This does not contradict the exact zero isolated retarded response to a uniform energy probe: a static conserved projection and a thermal equilibrium derivative are different from dynamical commutator response.

Extending the global projection to finite q requires independent dynamics and a suitable local-equilibrium/continuity analysis. Conservation alone does not select diffusion, ballistic transport, a relaxation time or a scalar-particle pole. A projected overlap with conserved energy is evidence for thermal energy content of this observable, not evidence for a distinct autonomous scalar or universal cosmological coupling.

## Constructive energy wavepacket follow-up

Also independently recomputed every entry of `native/compass_energy_modes.json` with the binary-Pauli implementation. `/private/tmp/native-thermal-bridge-check/energy_check.py` and `energy_result.json` match the7,13,57 kernel entries at derivative orders0,1,2 respectively.

For the physical e rather than E=2e/K, the checked per-cell Fourier norm kernels are

    N0(q)=K²[3/2+(1/2)sum_a cos(q_a)],
    N1(q)=K^4[24−8sum_(a<b)cos(q_a)cos(q_b)],
    N2(q)=192K^6 |q|²+O(q^4).

Consequently, near q0 with N0>0,

    ||D e_q||²/||e_q||²=(8/3)K² |q|²+O(q^4),
    ||D²e_q||²/||e_q||²=64K^4 |q|²+O(q^4).

The RMS frequency being linear in |q| is not an identified sound dispersion. The fourth moment is orderq² rather than the orderq4 that a pure finite-speed acoustic pole exhausting the measure would give. A low-frequency pole plus small higher-frequency weight remains possible. At q=(pi,pi,pi), N0 itself vanishes: that Fourier combination of this symmetrically assigned energy density is the zero operator, so normalized ratios are undefined there.

For f_x=exp(−|x|²/(2R²)) and e_f=sum_x f_x e_x, Poisson/Fourier concentration near zero gives |f_hat(q)|² proportional asymptotically to exp(−R²|q|²). Its mean |q|² is3/(2R²). Thus

    ||D e_f||²/||e_f||² ~4K²/R².

For each finite R this summable wavepacket is in the relevant generator domain. Unitary tracial evolution and the fundamental theorem of calculus give the exact bound

    ||e_f(t)−e_f||/||e_f|| <= |t| ||D e_f||/||e_f||.

Hence the large-R residual asymptotic supplies a controlled slow, spatially broad operator feature in this supplied Hamiltonian. The exact inequality uses the actual residual; replacing it by2|K|/R is asymptotic unless finite-R errors are enclosed. It guarantees limited change on times small compared with R/|K|; it does not establish propagation at that speed, diffusion, or a particle pole.

These are constructive HS-state results. Combining them with the finite-beta C–energy coupling requires controlling the thermal and large-R/volume limits together; that uniform state-limit argument is not supplied by the present coefficients.
