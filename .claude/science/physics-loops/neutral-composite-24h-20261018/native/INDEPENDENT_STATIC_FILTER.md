# Gaussian static-response locality check

Checked 2026-10-18 against the second half of `/private/tmp/neutral_static_response_root.md`. The neutral restricted gap and one-state-per-character band statement are treated as inputs to this check. No generic thermodynamic clustering theorem is invoked.

## Fourier convention and sign

With f_sigma(E)=(1-exp(-E^2/(2sigma^2)))/E, define

    k_sigma(t)=-(i/2) sign(t) erfc(sigma|t|/sqrt(2)).

Pairing positive and negative t gives integral k(t) exp(iEt)dt=integral_0^infinity erfc(sigma t/sqrt(2)) sin(Et)dt. Integration by parts yields exactly f_sigma(E). There is no missing 2pi under the stated transform convention.

For a stationary ground vector g, spectral decomposition gives

    <[A,tau_t B]>
      =sum_n [A_gn B_ng exp(i Delta_n t)
               -B_gn A_ng exp(-i Delta_n t)].

Since f_sigma is real and odd, its filtered integral is 2Re sum A_gn B_ng f_sigma(Delta_n). Thus chi_sigma=integral k(t)<[A,tau_t B]>dt has the stated static sign. Equivalently the usual perturbation -hB convention gives static response from i theta(t)<[tau_t A,B]>. The whole-time filter already includes its imaginary factor; do not insert an additional i.

## Spectral approximation error

Assume all inelastic neutral matrix elements from g have Delta_n>=Delta>0. Diagonal elastic terms cancel in the commutator. Then Cauchy-Schwarz on the spectral sums gives

    |chi_AB-chi_sigma|
      <= (2||A||||B||/Delta)
           exp[-Delta^2/(2sigma^2)].

This holds for distinct A,B and does not require positive cross spectral weights. A restricted gap in the channels reached by A and B suffices. No full global gap between different plane characters is needed.

## Direct LR split

Let r be the support distance, and use a uniform finite-range LR estimate

    ||[A,tau_t B]|| <= C_XY ||A||||B||
                          exp[-mu(r-v|t|)],

together with the trivial bound2||A||||B||. C_XY depends on the fixed local supports and lattice geometry; it is not a universal constant for arbitrarily large supports.

For |t|<=r/(2v), the LR exponential is at most exp(-mu r/2). The full kernel L1 norm is sqrt(2)/(sigma sqrt(pi)), giving a short-time bound C_XY ||A||||B|| sigma^-1 exp(-mu r/2).

For |t|>r/(2v), Gaussian/erfc tail bounds give

    integral_tail |k(t)|dt
      <= C sigma^-1 exp[-sigma^2 r^2/(8v^2)].

This estimate can be used with the trivial commutator norm, and introduces no time-dependent volume factor. Choosing sigma^2=2Delta v/r balances that exponent with the spectral error exponent. Consequently, for positive r,

    |chi_AB| <= C_XY ||A||||B||
       [Delta^-1 + sqrt(r/(Delta v))]
       exp[-kappa r],

    kappa=min(mu/2, Delta/(4v)).

For small r the uniform bound2||A||||B||/Delta can be used instead. The absolute value is required; a cross susceptibility need not be positive. The square-root prefactor may be absorbed into a slightly weaker exponential if desired.

## Finite boxes and state averages

Finite-range microscopic H admits the LR estimate uniformly in the periodic volume, with torus distance and bounded local supports. The assumed neutral gap is uniform in the specified growing-box family. Thus the above proof works directly in those finite boxes; it does not take an uncontrolled infinite-volume limit. For the native short-range Hamiltonian, a uniform v=O(Jz a) and Delta>=c Jz give an inverse-decay scale bounded by a constant times a, independent of lambda. This is an upper bound on the response range, not a claim that a fitted correlation length equals that constant.

Every neutral operator preserves the plane character. Under the one-band-state-per-character input, there are no inelastic low-band matrix elements within a character, and no offdiagonal matrix elements between different characters. A mixture or coherent superposition of exact ground characters therefore has a retarded susceptibility equal to a convex sum of the character responses; the same bound follows. Character-dependent diagonal expectations can produce elastic mixture covariance, but that is absent from the commutator. An isothermal static derivative allowing state populations to change is a different quantity and is not bounded by this argument merely because the retarded response is.

For sums of separated fixed-support sources, apply the local bound pairwise and sum |a_i||b_j| with the corresponding support distances. If every pair is separated by R, this gives the stated coefficient-mass prefactor times a polynomial/exponential bound in R. Increasing source size can increase that prefactor; the conclusion concerns separation beyond the feature supports, not their internal size. It supplies no universal assertion about extended sources with weights or diameters growing arbitrarily with separation.

Conclusion: the Fourier signs, error, LR split and balanced exponential are correct. Conditional on the separately proved neutral restricted gap, this is an actual static RETARDED-response locality bound in the weak-coupling finite-box family, not a bound on elastic covariance, charged channels, other states, or arbitrary thermodynamic/isotropic regimes.
