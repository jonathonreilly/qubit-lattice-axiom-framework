# A slow large feature without another interaction

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

At beta0, the C/e mixed channel vanishes. The finite-temperature calculation in THERMAL_BRIDGE_DERIVATION.md supplies a nonzero conserved-energy projection of the uniform composite, with coefficient−2beta+O(beta³) and certified variance fraction4beta²K²+O(beta⁴). Extending this simultaneously to finite-beta, infinite-width packets requires uniform control of connected correlations and dynamics. Do not silently transfer the exact tracial residual estimate to that different inner product. The candidate state, finite-q mode, normalization and matter/source identifications remain separate questions.

A physically prepared density perturbation proportional to E_f can be defined in a finite system at sufficiently small amplitude to preserve positivity. That construction would be a supplied preparation, not a derivation of a stable fermion or of the background history. The observed clock/ruler and universal-matter comparator has still not been matched.
