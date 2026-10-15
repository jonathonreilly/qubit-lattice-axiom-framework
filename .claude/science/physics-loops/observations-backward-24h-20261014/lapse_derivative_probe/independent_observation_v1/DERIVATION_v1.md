# Independent spatial-curvature and lapse input derivation

This derivation precedes exposure to root's extension. It checks the measurement premises, not an unread candidate theorem. Natural units `c=1` are used; every derivative below is with respect to independently calibrated physical areal radius unless stated otherwise.

## 1. Metric, clocks and radial range

Use the physical, static, spherically symmetric metric on a radial domain

```text
ds_J^2 = -N(r)^2 dt^2 + dr^2/B(r) + r^2 dOmega^2,
N>0, B>0, f(r)=N(r)/N(r0).
```

`r` is fixed by the area `4 pi r^2`, not by a radar-distance definition. Standard clocks and reflecting endpoints are stationary in this chart. A photon has conserved Killing energy, so an outward link from `r0` to `r` has received/emitted frequency ratio `1/f(r)`. Vacuum radial propagation, a fixed emitter, an instantaneous reflection and an outward endpoint `r>r0` give

```text
tau(r) = 2 integral_[r0,r] ds/[f(s) sqrt(B(s))],
g(r) = tau'(r) = 2/[f(r) sqrt(B(r))] > 0,
B(r) = 4/[f(r)^2 g(r)^2].                            (A)
```

The coordinate normalization of `N` cancels. Proper-time calibration, stable clock comparison and consistent time/length units do not thereby disappear. A moving reflector, a material signal path, a delay at turnaround, a nonradial path or a nonzero metric shift is a different measurement model. The stationary-clock result alone does not justify replacing static radial propagation by a general stationary experiment.

## 2. Intrinsic three-curvature and the derivative trade

For the spatial metric `h=dr^2/B+r^2 dOmega^2`, introduce proper radial distance `rho`, so `dr/d rho=sqrt(B)` and `d^2r/d rho^2=B'/2`. The warped-sphere scalar curvature is

```text
R3 = -4 r_(rho rho)/r + 2[1-r_rho^2]/r^2
   = 2(1-B)/r^2 - 2B'/r.                            (B)
```

Define `L=f'/f`, `T=g'/g`, and `K=L+T`. Differentiating (A) gives `B'/B=-2K`, hence

```text
R3 = 2(1-B)/r^2 + (4B/r)(f'/f+g'/g).                (C)
|grad_h ln N| = sqrt(B)|f'/f| = 2|f'|/(f^2 g).       (D)
```

The signed radial proper derivative is `sqrt(B) f'/f`. It also equals the signed proper acceleration of the static clock congruence; it is not the acceleration of freely falling test bodies. Its physical interpretation presupposes that congruence and the matter metric.

Thus a pointwise `R3` supplier derived by this map uses `f,g,f',g'`. There is no explicit `f''`, but `g'=tau''` remains. This is a reduction in one derivative channel, not a derivative-free measurement route. `R3` is intrinsic to the specified orthogonal static slices; it is not the four-dimensional Ricci scalar, and an unspecified alternative slicing need not give the same three-curvature.

The four-curvature obeys

```text
R4 = R3 - 2 Delta_h N/N,
Delta_h N/N = B f''/f + (2B/r+B'/2)f'/f
            = Delta_h ln N + |grad_h ln N|^2.         (E)
```

Consequently bounded `R3`, `f` and `f'` alone do not bound `R4` pointwise. An environmental theorem using the weaker inputs must justify its actual transformed equation or weak comparison; it cannot simply rename the old curvature in M17.

There is a legitimate integration-by-parts mechanism to test. For a smooth specified weight `w` and outward spatial normal `n`,

```text
integral w R4 dV_h
 = integral [w R3 + 2 grad w . grad ln N
                    - 2w |grad ln N|^2] dV_h
   - 2 integral_boundary w partial_n ln N dA_h,      (F)

integral w N R4 dV_h
 = integral [w N R3 + 2 grad w . grad N] dV_h
   - 2 integral_boundary w partial_n N dA_h.         (G)
```

If `w` vanishes on every boundary component, the displayed boundary terms vanish. Otherwise their traces/signs must be supplied or bounded. A solution-dependent weight is not an observed kernel without further work. These identities are possible first-derivative suppliers for a proved weak argument, not proof of an unread new environmental bound.

For reference, the radial M17 operator itself has the exact measurement form

```text
L_J psi = 4/(f^2 g r^2) d/dr[(r^2/g) psi']
        = B[psi''+(2/r-g'/g)psi'].                   (H)
```

It follows from `N r^2 sqrt(B)/N(r0)=2r^2/g` and `N r^2/[N(r0)sqrt(B)]=f^2 g r^2/2`. Keeping a divergence form may change which derivative errors are needed for a particular weak certificate; it does not validate a pointwise curvature estimate from unqualified samples.

## 3. Sufficient enclosures away from the center

Suppose one has certified simultaneous enclosures over the whole intended annulus, with `r>=r_min>0`,

```text
0<f_- <= f <= f_+,   0<g_- <= g <= g_+,
f' in I_p,          g' in I_q.
```

They may vary with radius. Define interval operations with outward rounding, rather than substituting independently favorable central values:

```text
I_B = [4/(f_+^2 g_+^2), 4/(f_-^2 g_-^2)],
I_L = I_p/[f_-,f_+],
I_K = I_L + I_q/[g_-,g_+],
I_R3 = 2(1-I_B)/r^2 + (4/r) I_B I_K.                (I)
```

Dependencies between these intervals may make the enclosure loose but do not invalidate a conservative enclosure. If radius itself ranges over a positive interval, use that same joint calibrated radius in the original expressions or a conservative interval extension; its relationship to the sampled profiles and their derivatives must also be covered.

For an absolute gradient envelope,

```text
|grad_h ln N| <= 2 max(|I_p|)/(f_-^2 g_-).            (J)
```

Uniform positive lower bounds give the ellipticity and lapse-ratio prerequisites used by many static comparisons. For a whole-domain lapse ratio, `Nmax/Nmin=fmax/fmin`; a common time-coordinate normalization cancels. These are input enclosures, not measured values produced by the formulas.

An explicit error version makes the required information visible. Let both true and nominal `f,g` exceed positive `m_f,m_g`; suppose their errors are at most `epsilon_f,epsilon_g`, and the slope errors at most `epsilon_p,epsilon_q`. With finite nominal slope bounds,

```text
delta_L <= epsilon_p/m_f + |p_hat|max epsilon_f/m_f^2,
delta_K <= delta_L + epsilon_q/m_g
                       + |q_hat|max epsilon_g/m_g^2,
delta_B <= 8 epsilon_f/(m_f^3 m_g^2)
                       + 8 epsilon_g/(m_f^2 m_g^3),
delta_R3 <= 2 delta_B/r_min^2
            + (4/r_min)[B_max delta_K+|K_hat|max delta_B].  (K)
```

The last line treats radius as exactly calibrated. Additional radius/coordinate errors need their own enclosure. It is conservative, not a claim of optimal statistical uncertainty. No observational covariance is assumed independent merely because interval arithmetic permits independent extreme endpoints.

There is also a useful integrated consistency condition. Equation (B) is

```text
[r(1-B)]' = r^2 R3/2.
```

On a regular ball this fixes `B(r)=1-[integral_0^r s^2 R3(s) ds]/(2r)`; on an annulus it additionally requires the value of `a[1-B(a)]` at its inner radius `a`. A supplied `R3` profile and a measured `B` cannot be freely inconsistent. More positively, for a specified differentiable areal-radius weight `w`,

```text
integral_a^b w r^2 R3 dr
 = 2[w r(1-B)]_a^b - 2 integral_a^b w' r(1-B) dr.    (O)
```

This signed weighted functional needs only a certified `B` enclosure and its boundary values, not a pointwise `B'` or `g'` measurement. A uniform metric error `delta_B` gives absolute functional error bounded by `2 delta_B[|w(a)|a+|w(b)|b+integral_a^b |w'|r dr]`. Fixed calibrated weights and radius are assumed here. These are signed areal-radius functionals, not automatically spatial-volume statistics or bounds on the positive part `(R3)_+`. Positive and negative curvature can cancel, so they cannot simply replace the latter in a comparison theorem. This distinction leaves a genuine weaker-measurement route open when the proved certificate has exactly the matching functional form.

## 4. Radius calibration is a derivative input

If samples are labelled by an instrument coordinate `xi`, and the independently calibrated relation is `r=r(xi)` with `r_xi>0`, write the observed lapse ratio as `F(xi)`. Then

```text
f' = F_xi/r_xi,
g = tau_xi/r_xi,
g' = tau_xixi/r_xi^2 - tau_xi r_xixi/r_xi^3,
B = 4 r_xi^2/(F^2 tau_xi^2),
K = F_xi/(F r_xi) + tau_xixi/(tau_xi r_xi)
                         - r_xixi/r_xi^2.           (L)
```

A bound on the radius values alone does not supply the derivative calibration appearing in this expression. Monotonicity and positive lower bounds also matter. Directly taking slopes with respect to a radar distance, proper radial length, redshift label or coordinate radius and calling them areal-radius slopes changes the formula. When applicable, the proper lapse-gradient magnitude simplifies to `2|F_xi|/(F^2 tau_xi)`; this cancellation does not eliminate areal-radius requirements from the three-curvature or domain geometry.

## 5. Finite samples and unresolved interpolation

Data values with error bars are not uniform derivative enclosures. A sufficient additional route is a declared regularity class, calibrated smoothing/window response and a validated interpolation error bound. For example, if samples of `f` at `r,r+h` have absolute errors at most `epsilon`, and an independently justified `|f''|<=M` holds between them, the forward difference estimates `f'(r)` with error at most

```text
2 epsilon/h + M h/2.                                (M)
```

Likewise, with `|tau'''|<=M3`, the centered second difference for `tau''(r)` has error at most

```text
4 epsilon_tau/h^2 + M3 h/3.                         (N)
```

The latter follows from the normalized triangular-kernel average of `tau''` on `[r-h,r+h]`. It demonstrates a sufficient supplier, not a necessary unique estimator. Directly calibrated slope measurements or a different validated functional could replace these premises. A chosen spline, Gaussian-process kernel, band limit or fit family is an additional modelling assumption until justified; a small residual at observed nodes is not its derivative certificate. A theorem containing only first lapse derivatives can still require stronger regularity to *estimate* those derivatives from noisy finite values.

A concrete kinematic counterexample fixes `f=1` and nominal `tau=2r`. Choose a smooth bump `b(r/L)` supported strictly inside an unobserved gap of an annulus and set

```text
tau_epsilon(r)=2r+epsilon^3 L b(r/L) sin[r/(epsilon^2 L)].
```

For sufficiently small positive epsilon, `g=tau_epsilon'>0`, `g` converges uniformly to 2, and `tau_epsilon` converges uniformly to `2r`. Every sampled value outside the bump, including sampled slopes, is exactly unchanged. But

```text
tau_epsilon'' = [epsilon^3 b'' sin + 2epsilon b' cos
                                  - b sin/epsilon]/L
```

is unbounded along a sequence of epsilon values wherever the bump is nonzero. Equation (C) gives correspondingly unbounded positive and negative spatial-curvature excursions while (A) defines a smooth positive static metric. Smooth compact support preserves an untouched regular center and exterior if included. This disproves a general inference from these finite samples or C0 errors to a pointwise curvature bound. It is not asserted to satisfy the full candidate Einstein/matter equations and does not prohibit a separately proved weak or averaged certificate.

There is a separate check on (E): fix `B=1` and use `f_epsilon=1+epsilon^3 b(r/L)sin[r/(epsilon^2L)]`, with `g=2/f_epsilon`. Then `R3=0`, `f_epsilon` tends uniformly to 1, and `f_epsilon'` tends uniformly to zero, while `R4=-2(f''+2f'/r)/f` has unbounded excursions. Thus even accurately small first-lapse gradients do not themselves supply a pointwise four-curvature bound.

## 6. Center and boundary coverage

On a regular spherical center, `B(0)=1`, `B'(0)=0` and a smooth radial lapse has `f'(0)=0`. For a center emitter, `f(0)=1`, `g(0)=2` and `g'(0)=0`. If

```text
B=1+b2 r^2+O(r^4),
```

then `R3(0)=-6b2=-3B''(0)`. Writing `f=1+f2 r^2+O(r^4)` and `g=2+g2 r^2+O(r^4)` yields `b2=-(2f2+g2)`, hence `R3(0)=12f2+6g2`.

The apparently singular terms in (B),(C) therefore require a certified regular limit. A constant absolute error in `B`, or an unconstrained first-derivative error, is not a uniform central curvature error bound. One needs control of `(1-B)/r^2` and `B'/r`, an equivalent regular-center expansion with bounded coefficients/remainder, or a separately supplied whole-ball curvature enclosure. This need not be a separate bound on `f''` if the relevant combined metric quantity is certified, but regularity by itself does not give its numerical coefficient. Restricting to an annulus avoids the center limit and adds an inner boundary; it cannot erase that boundary's field/metric information.

An outer set of clock links cannot be silently extrapolated through an opaque source or an unsampled interior. A supplied whole-domain `R3` enclosure, lapse/gradient envelope and all boundary traces can be adequate hypotheses; external measurements alone have not supplied them. Spherical symmetry, exact staticity, the physical matter metric and static scalar fields are separate conditions. Static metric data do not show the scalar fields to be static, and a mass/lensing fit using a GR density law is not a theory-independent three-curvature measurement.

## 7. Hand checks and disposition

The proper-radius derivation gives `R3=0` for flat space and for the static Schwarzschild slice `B=1-2M/r`. For de Sitter `B=1-H^2r^2`, it gives `R3=6H^2`, while `N=sqrt(B)` has `Delta_h N/N=-3H^2` and therefore `R4=12H^2`. The anti-de Sitter signs reverse. Constant lapse makes the two curvatures equal. These are hand checks, not an executed numeric test count.

The weaker geometric inputs are meaningful, but they remain calibrated functional inputs. This derivation neither proves nor rejects root's unread extension. It identifies which derivative, coordinate, boundary and error assumptions must be displayed, and leaves open whether a new transformed/weak comparison can use them without demanding a pointwise `R4` enclosure.
