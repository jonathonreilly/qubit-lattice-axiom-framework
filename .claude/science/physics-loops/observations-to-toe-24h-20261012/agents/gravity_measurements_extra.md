# Independent scalar-continuum construction and vacuum coherence

Date: 2026-10-12. Main/source pin: `7f9fac6cb89c6c7b86cde4f5716870d0dfc4b9de`.
Status: **conditional-support**. This is an independent mathematical
construction/check requested by the coordinator, not an empirical inference,
novelty claim, or adopted physical premise. The coordinator's upcoming
equations were not read before this derivation.

```yaml
actual_current_surface_status: conditional-support
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
proposal_allowed: false
proposal_allowed_reason: free scalar bath, source coupling, vacuum preparation, and source histories are supplied candidate premises
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 1. Exact model, conventions, and static normalization

Work in `hbar=c=1`, in 3+1 Minkowski dimensions. Let `s, ell > 0` and

`nu(dmu) = ell^s mu^(s-1) exp(-ell mu) dmu / Gamma(s)`, `mu > 0`.

This is a unit-total-mass measure on inverse Compton lengths, with no atom
at zero. It is not the density with respect to `d(mu^2)`; changing the mass
variable without its Jacobian changes the answers.

One realization uses independent canonically normalized real fields
`phi_mu`, with mass-delta-normalized commutators, and
`Phi = integral sqrt(dnu/dmu) phi_mu dmu`. Consequently

`W(x) = <Phi(x)Phi(0)> = integral W_mu(x) nu(dmu)`.

The direct integral is a positive generalized free field. Its equal-time
canonical commutator is normalized by `integral nu=1`; no finite-order
single-field equation is assumed. Couple a real classical source through
`L_int=J Phi`, so each canonical component has
`(partial_t^2 - Laplacian + mu^2) phi_mu = sqrt(dnu/dmu) J`.

Eliminating a static field gives interaction energy
`-1/2 integral J G_static J`. The cross-term of point sources `g_A,g_B`
at separation `r>0` is therefore exactly

`V_AB(r) = -g_A g_B/(4 pi r) integral exp(-mu r) nu(dmu)`

`         = -g_A g_B/(4 pi r) [ell/(ell+r)]^s`.

The first expression fixes all subsequent coupling and two-point-function
normalizations. At small r the potential has the canonical `1/r` leading
term; at large r it decays as `r^(-1-s)`. This continuum is not a massless
pole disguised as a density.

## 2. Retarded and Wightman kernels

Let `r=|x|`, `omega_mu,k=sqrt(k^2+mu^2)`. Our retarded convention is
`G_R(x)=i theta(t) <[Phi(x),Phi(0)]>`; it solves the positive-source wave
equation above. In spatial Fourier variables,

`G_R(t,k) = theta(t) integral sin(omega_mu,k t)/omega_mu,k nu(dmu)`.

For `r>0`, the position-space distribution is

`G_R(t,r) = delta(t-r)/(4 pi r)`

` - theta(t-r)/(4 pi tau) integral mu J_1(mu tau) nu(dmu)`,

where `tau=sqrt(t^2-r^2)` in the interior of the future cone. The unit
light-cone front follows from `integral nu=1`. The interior term has the
closed form

`-theta(t-r) s(s+1)/(8 pi ell^2)`

`  * 2F1((s+2)/2, (s+3)/2; 2; -tau^2/ell^2)`.

This follows by integrating the power series of `J_1`, initially in its
convergence domain and then continuing the Laplace integral. For `s=1`,
the tail simplifies to `-theta(t-r) ell/[4 pi(ell^2+tau^2)^(3/2)]`.
Integrating that expression over t reproduces
`ell/[4 pi r(ell+r)]`, an independent static normalization check.

The Wightman distribution is

`W(t,x) = integral nu(dmu) integral d^3k/(2 pi)^3`

`           * exp(-i omega_mu,k t + i k.x)/(2 omega_mu,k)`.

Equivalently, put `zeta=sqrt(r^2-(t-i0)^2)` on the positive-real branch
for spacelike separation:

`W(t,r) = ell^s/[4 pi^2 Gamma(s) zeta]`

`           * integral_0^infinity mu^s exp(-ell mu) K_1(mu zeta) dmu`.

For `Re(zeta)>0` it also equals the convergent integral

`W = s ell^s/(4 pi^2 zeta)`

`      * integral_0^infinity cosh(u)/[ell+zeta cosh(u)]^(s+1) du`,

with the timelike result defined by the stated boundary value. For example,
`s=1, t=0, r=ell` gives `W=1/(6 pi^2 ell^2)`.
The retarded support is causal before spatial smearing. A Gaussian has
noncompact spatial support, so smeared observables do not have a sharp
point-to-point support boundary.

## 3. Gaussian source and exact decoherence exponent

Fix `a>0` and define the normalized profile

`f_a(x) = (2 pi a^2)^(-3/2) exp[-|x|^2/(2a^2)]`,

so `f_tilde_a(k)=exp(-a^2 k^2/2)`. Its squared transform is
`exp(-a^2 k^2)`. The width convention is explicit to avoid a factor-two
ambiguity. Two alternative fixed source positions have separation `d>=0`:

`J_L/R(t,x) = g 1_[0,T](t) f_a(x-x_L/R)`.

The same field gives the static interaction of Gaussian sources by replacing
the point Green function with
`integral nu(dmu) integral d^3k/(2 pi)^3 exp(i k.r)`
`* exp[-(a_A^2+a_B^2)k^2/2]/(k^2+mu^2)`.
Thus the displayed point potential fixes coupling normalization, while an
actual finite-width static prediction must use the corresponding smearing.

The bath starts in the free vacuum, uncorrelated with the two-position
source state. The positions and switch are externally supplied; recoil and
backreaction are omitted. Linear forcing creates conditional coherent
states. Their overlap has magnitude

`|rho_LR(T)/rho_LR(0)| = exp[-Gamma(T,d)]`,

where `Gamma = (1/2)||alpha_L-alpha_R||^2`, not the full squared norm.
Using `|integral_0^T exp(i omega t)dt|^2 = 2(1-cos omega T)/omega^2` and
the angular average `cos(k.d) -> sinc(kd)` gives exactly

`Gamma(T,d) = g^2/(2 pi^2) integral nu(dmu) integral_0^infinity dk`

`  * k^2 exp(-a^2 k^2)/omega_mu,k^3`

`  * [1-sinc(kd)] [1-cos(omega_mu,k T)]`.

Here `sinc(x)=sin(x)/x` with `sinc(0)=1`. Common coherent-state phases can
be retained separately; they do not affect this visibility. With identical
profiles and translation-invariant vacuum, branch self-energies are equal.
The checks `Gamma(0,d)=Gamma(T,0)=0` follow exactly, and the integrand
proves `Gamma>=0` for every T.

## 4. Local and spatial-difference frequency spectra

Define the two-sided Fourier transform of the vacuum Wightman function,
with positive frequencies populated:

`S_a(omega,d) = integral dt exp(i omega t)`

`                * <Phi_a(t,x) Phi_a(0,x')>`, `d=|x-x'|`.

For `omega>0`, set `k=sqrt(omega^2-mu^2)` and obtain

`S_a(omega,d) = 1/(2 pi) integral_0^omega k exp(-a^2 k^2) sinc(kd) nu(dmu)`.

It vanishes for `omega<0`. The local spectrum is `S_loc=S_a(omega,0)`.
For the difference operator `DeltaPhi_a=Phi_a(x_L)-Phi_a(x_R)`,

`S_diff(omega) = 2[S_loc-S_a(omega,d)]`

`             = 1/pi integral_0^omega k exp(-a^2 k^2) [1-sinc(kd)] nu(dmu)`.

This is a Wightman spectrum. The symmetrized noise spectrum is one-half
of it at positive frequency and is even in omega; the retarded spectrum is
another object. Calling all three the same spectral density loses factors.
In the present convention the equivalent visibility formula is

`Gamma(T,d) = g^2/(2 pi) integral_0^infinity`

`               S_diff(omega) [1-cos(omega T)]/omega^2 d omega`.

Set

`A_s = ell^s B(s/2,3/2)/[4 pi Gamma(s)]`

`    = ell^s/[2^(s+2) Gamma((s+1)/2) Gamma((s+3)/2)]`.

As `omega -> 0+`, for fixed finite a, ell and d,

`S_loc(omega) = A_s omega^(s+1) [1+O(omega)]`,

`S_diff(omega) = A_s d^2/(s+3) omega^(s+3) [1+O(omega)]`.

The second result uses `1-sinc(kd)=(kd)^2/6+O(k^4d^4)` and a beta
integral. The spatial difference contributes two further powers of
frequency. The leading coefficients are independent of the Gaussian width;
the width enters at higher orders and controls ultraviolet convergence.

## 5. Long times and an explicit finite bound valid for every T

The nonnegative function `S_diff(omega)/omega^2` is integrable: its infrared
behavior is `omega^(s+1)`, and spatial Gaussian suppression together with
the exponential mass density controls the ultraviolet. Hence

`Gamma(T,d) -> Gamma_infinity(d)` as `T -> infinity`,

`Gamma_infinity = g^2/(2 pi) integral_0^infinity S_diff(omega)/omega^2 d omega`.

Riemann-Lebesgue supplies this limit. It is a finite plateau, not a constant
Markovian decay rate. The finite-time exponent need not increase monotonically:
its cosine transform can approach the plateau from either side.

For `d>0`, a useful explicit asymptotic coefficient is

`Gamma_infinity-Gamma(T,d)`

` = [g^2 A_s d^2 Gamma(s+2) cos(pi(s+2)/2)]/[2 pi(s+3)]`

`     * T^(-s-2) + o(T^(-s-2))`.

When s is a positive odd integer this coefficient vanishes. The next
small-frequency coefficient of `S_diff` is

`B_s = -ell^(s+1) d^2 B((s+1)/2,5/2)/[12 pi Gamma(s)]`,

so the next possible term is
`g^2 B_s Gamma(s+3) cos(pi(s+3)/2)/(2 pi) * T^(-s-3)`.
For example, at `s=1`,

`Gamma_infinity-Gamma(T,d) ~ -g^2 ell^2 d^2/(10 pi^2 T^4)`.

These asymptotics use the smooth, exponentially controlled ultraviolet
behavior of this specific measure and positive Gaussian width; they are
not conclusions from the infrared power alone for an arbitrary bath.

A uniform bound follows without asymptotics. Since `1-cos<=2`,
`omega_mu,k>=k`, `integral nu=1`, and `0<=1-sinc(kd)<=(kd)^2/6`,

`0 <= Gamma(T,d) <= 2 Gamma_infinity(d)`

`                   <= g^2 d^2/(12 pi^2 a^2)` for every `T>=0`.

Thus visibility is at least `exp[-g^2 d^2/(12 pi^2 a^2)]` uniformly in T.
The bound is loose at large d/a but finite. A sharper still measure-independent
bound is `Gamma(T,d)<=g^2 J(d/a)/pi^2`, where

`J(d/a)=integral_0^infinity exp(-a^2 k^2)[1-sinc(kd)] dk/k`.

Writing `q=d/(2a)` and D for Dawson's integral,
`J=2 integral_0^q D(u)du - 1 + D(q)/q`, with its continuous zero limit.
As d/a becomes small, `J=d^2/(12a^2)+O(d^4/a^4)`.

An additional positive quadrature for the plateau is

`Gamma_infinity = g^2/(4 pi^2) integral_0^infinity du`

` * u^(1/2)/(a^2+u)^(3/2) [1-exp(-d^2/(4(a^2+u)))] M_nu(u)`,

where `M_nu(u)=integral exp(-u mu^2)nu(dmu)`. This follows from a Laplace
representation of `omega^-3` and an elementary Gaussian momentum integral.
It is suitable for stable numerical evaluation without an oscillatory T.

## 6. Physical and verification boundary

The all-T bound assumes a nonzero spatial width a. Taking a to zero with a
hard time switch and d>0 restores a logarithmic ultraviolet divergence;
that limit is not licensed by the formula for a>0. The source's factorized
vacuum preparation and switching protocol also matter. Starting with dressed
sources, including their motion, or repeatedly preparing the bath changes
the problem. A finite vacuum-overlap plateau is not a claimed universal
absence of decoherence, nor evidence that this scalar construction describes
observed gravity. The construction fixes static and noise normalizations
together rather than choosing them independently.

## 7. Executed numerical checks

Runtime evidence is in
`/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/gravity_measurements/`:
`scalar_continuum_check.py` and `scalar_continuum_check_results.json`.
The script ran with SciPy 1.17.0, one CPU thread, after checking stop markers
and the campaign deadline. It imports no parent science functions or results.

The check evaluates the static Laplace integral and retarded Bessel integral
at `s=0.4,1,2.7`, compares the Wightman special value above, and verifies
the small-frequency coefficients at `omega=0.001`. Relative static/kernel
differences are below `3e-12`; the low-frequency ratios are within `0.001`
of their asymptotic limits.

For the independent numerical choice
`s=1, ell=1.3, a=0.7, d=1.2, g=0.8`, oscillator-mode and frequency-spectrum
integration give, respectively,

| T | Oscillator integral | Frequency integral |
|---:|---:|---:|
| 2 | 0.005988046688421602 | 0.005988046688420314 |
| 5 | 0.004294469267764870 | 0.004294469267763148 |

The frequency integral gives plateau `0.004257864126393025`; the positive
Schwinger-parameter integral gives `0.004257864126393124`. The uniform
polynomial bound is `0.015880544701492944`. The observed overshoot at T=2
is compatible with the nonmonotone exact formula. At T=10,20,40, the ratio
of the computed approach-to-plateau term to the stated s=1 leading asymptotic
is `1.07037, 1.01640, 1.00403`. These checks support normalization and
quadrature; the all-T bound is established by the displayed inequalities,
not by sampling those times.

Reproduction command actually run:

```sh
python3 /Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/gravity_measurements/scalar_continuum_check.py
```
