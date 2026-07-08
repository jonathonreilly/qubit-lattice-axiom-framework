# Inertial Closure Width-Independent Acceleration on the Two-Step Surface -- Bounded Theorem

**Date:** 2026-07-08
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** On the free `U = 1`, `d = 3` staggered two-step transfer
surface, with real species coefficient `m > 0`,
`E(p) = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu))`, and
`M_I = m sqrt(1 + m^2)` as computed by the mass-observable block01 note, this
note proves that a species-blind weak linear probe gives exact momentum drift
and a packet acceleration whose leading term is independent of packet width in
the stated small-momentum window. The note supplies only the inertial response
half of the closure. It supplies no gravitational source coefficient, no WEP
claim, and no source-side identification.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/inertial_closure_two_step_surface_2026_07_08.py`](../scripts/inertial_closure_two_step_surface_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/inertial_closure_two_step_surface_2026_07_08.txt`](../logs/runner-cache/inertial_closure_two_step_surface_2026_07_08.txt)

## Why This Note Exists

The block01 mass-observable note computes two free one-particle readouts on
the realized two-step surface: the rest gap `arcsinh(m)` and the spectral
curvature coefficient

```text
    M_I = m sqrt(1 + m^2).
```

That note deliberately stops before proving that `M_I` governs the actual
acceleration of a packet under an external probe. This note supplies that
separate dynamical statement. It also explains why the 2026-04-07
width-dependent negative is recovered in the gapless limit rather than
contradicted on its own substrate.

## Imports And Premises

- **I-DYN / I-MASS / I-TIME.** These are inherited exactly from the
  "Imports And Premises" section of
  [`MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md`](MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md).
  In particular, this note uses the free `U = 1`, `d = 3` two-step symbol
  `E(p)`, the on-site positive mass coefficient `m > 0`, and the same
  blocked-time normalization footing through that source note rather than
  restating the import chain.
- **I-EXT.** Add a weak linear probe

```text
    H = H_eff + g X_3
```

  coupled to the conserved on-site `Q`-density with a species-independent
  free coefficient `g`. Equivalently, on a finite torus this is represented in
  the momentum-shift gauge, so the canonical momentum is shifted uniformly
  along the `p_3` direction and the torus periodicity is respected.

I-EXT is the only new import in this note. It is a probe import, not a
gravitational-source import.

## Why The Probe Is Not The Gravitational Coupling

The weak-field source/readout interface note records the EP-S3a weak-field
test-particle form

```text
    U_test(phi; x) = -m phi(x).
```

That is a mass-weighted gravitational source coupling. Using it here would
assume the shared source/inertial coefficient identity before proving it, and
would therefore beg the WEP question.

The I-EXT probe is deliberately different: it is a species-blind coupling to
the conserved on-site `Q`-density with free coefficient `g`. The relation
between this probe coefficient and the gravitational source coefficient is
exactly the block04/source-side question. This note does not touch that
question.

## Statement

On the free `U = 1`, `d = 3` two-step transfer surface, let

```text
    E(p) = arcsinh(sqrt(m^2 + sin^2 p_1 + sin^2 p_2 + sin^2 p_3)),
    M_I = m sqrt(1 + m^2),
    m > 0.
```

**T1 - exact momentum law.** In the momentum-shift gauge, for any
one-particle state with mean momentum `p_bar`,

```text
    <p(t)> = p_bar - g t e_3.
```

This identity is exact. It has no error term and is torus-consistent.

**T2 - exact band-velocity / acceleration law.** For a one-particle momentum
density `rho(p)`,

```text
    d<X_3>/dt
      = int rho(p) (dE/dp_3)(p - g t e_3) d^3p,

    d^2<X_3>/dt^2
      = -g int rho(p) (d^2E/dp_3^2)(p - g t e_3) d^3p.
```

These are exact identities for any normalizable one-particle state. The
single scalar band is supplied by block01 T1, so no interband terms exist.

**T3 - windowed width-independence.** Let `rho` be centered at `p_bar = 0`
with total second moment `sigma_p^2 = sum_mu <p_mu^2>`, and let `rho` be
supported in the shifted window

```text
    W(t) = { p : |p|_inf + |g| t <= p_* },
```

where `p_* = p_*(m)` is the local curvature window certified for this
two-step surface. Define

```text
    r(t) = M_I int rho(p) (d^2E/dp_3^2)(p - g t e_3) d^3p - 1.
```

Then

```text
    d^2<X_3>/dt^2 = -(g / M_I) [1 + r(t)]
```

with

```text
    |r(t)| <= C4(m) (sigma_p^2 + g^2 t^2),

    C4(m) = (1/2) M_I sup_{|q|_inf <= p_*} || Hess E_33 (q) ||_2,
```

the supremum of the Hessian of the curvature function
`E_33 = d^2E/dp_3^2` over the window. The rest-point evaluation of the
on-axis entry is sympy-exact,

```text
    (1/2) | M_I (d^4E/dp_3^4)(0) |
      = (3 + 10 m^2 + 4 m^4) / (2 m^2 (1 + m^2))  <=  C4(m),
```

so the explicit closed form lower-bounds the window constant and fixes its
small-`m` divergence rate.

**T3' - Gaussian tail corollary.** For an isotropic Gaussian `rho` of
per-axis width `sigma` (so `sigma_p^2 = 3 sigma^2`) that is not
window-supported, truncation to `W(t)` adds to `|r(t)|` an explicitly
exponentially small tail term bounded by

```text
    eps_tail(t) <= M_I osc_BZ(E_33) * P_rho( p not in W(t) ),
```

with `osc_BZ` the global oscillation of `E_33` over the Brillouin zone and
`P_rho` the Gaussian tail mass; the paired runner prints this addend for
every window-qualifying run. Thus the leading acceleration is independent of packet width, the
window-supported residual is quadratic in the packet's momentum width and in
the probe-induced momentum shift, and the Gaussian tail correction is
exponentially small in `(p_* - |g| t)^2 / (2 sigma^2)`. This is the
generator-invariant inertial response that the 2026-04-07 attempt lacked.

**T4 - mechanism exhibit.** The curvature-ratio constant satisfies

```text
    C4(m) ~ 3 / (2 m^2)        as m -> 0,
```

so the windowed width-independence bound becomes vacuous at `m = 0`. In that
limit the acceleration becomes width-dominated. This recovers the decisive
mechanism in the 2026-04-07 matter/inertial closure note:

> "the slope is dispersion-dependent, not mass-dependent"

The old negative is thereby explained, not contradicted. It probed the
`m = 0`, or effectively gapless, regime of a different substrate.

## Proof Sketch

For T1, represent the I-EXT perturbation in momentum space. The linear
position probe is the generator of translations in `p_3`, so the
Schrodinger flow transports the wave packet along

```text
    p_3(t) = p_3(0) - g t.
```

The momentum-shift gauge implements this transport on the torus by shifting
the momentum argument rather than by using a non-periodic position potential.
Taking the first moment of the transported density gives
`<p(t)> = p_bar - g t e_3` exactly.

For T2, block01 T1 reduces the one-particle dynamics to the scalar band
`E(p) I_8`. The Heisenberg velocity in the `3` direction is therefore the
band derivative `dE/dp_3`, evaluated on the shifted momentum argument from
T1. Differentiating once more in time gives the displayed acceleration
identity. Because the band is scalar and taste-degenerate, there are no
off-diagonal band-connection or interband terms.

For T3, expand the exact curvature

```text
    E_33(q) := d^2E/dp_3^2(q)
```

around the rest point. Block01 T4 gives

```text
    E_33(0) = 1 / M_I.
```

The first momentum derivatives of `E_33` vanish at the rest point by
evenness, so for `q` in the window the second-order Taylor bound gives

```text
    | E_33(q) - E_33(0) |
      <= (1/2) sup_{W} || Hess E_33 ||_2 * |q|^2,
```

a bound that holds uniformly on `W(t)` because the supremum is taken over
the window rather than evaluated only at the rest point — this is what makes
the bound valid for every window-supported density, not just for densities
concentrated near `0`. Averaging over the shifted packet gives

```text
    int rho(p) |p - g t e_3|^2 d^3p = sigma_p^2 + g^2 t^2
```

for `p_bar = 0`, which yields the displayed residual bound. The on-axis
fourth derivative is sympy-exact,

```text
    (d^4E/dp_3^4)(0)
      = -(3 + 10 m^2 + 4 m^4) /
        (m^3 (1 + m^2)^(3/2)),
```

and its rest-point Taylor coefficient lower-bounds `C4(m)` as displayed. For
T3', split the integral over `W(t)` and its complement: the window part obeys
the T3 bound, and the complement contributes at most the global oscillation
of `M_I E_33` times the Gaussian tail mass, which is exponentially small in
`(p_* - |g| t)^2 / (2 sigma^2)`.

For T4, the expression for `C4(m)` diverges like `m^-2`. Setting `m = 0`
removes the positive gap that block01 T3 uses to make the one-particle sector
well-defined. The same acceleration formula then no longer supplies a
width-independent leading term; packet width and spreading dominate the
response, matching the mechanism recorded in the 2026-04-07 negative.

## What This Retires And What It Does Not

This retires the mechanism of the 2026-04-07 negative on the realized
two-step surface: for `m > 0`, within the stated momentum window, inertial
response is width-independent to leading order and the width-dependent
remainder is controlled by `C4(m)`.

This does not retire the 2026-04-07 note as a historical record. Its negative
remains the record of the Gaussian-packet, grown-DAG, effectively gapless
attempt that it actually tested.

This does not establish persistence as non-spreading. Free packets still
spread. The persistence supplied through block01 T3 is the gapped,
well-defined one-particle sector/projection; it is not a claim that free
wave packets keep fixed spatial width.

This does not touch the gravitational side. The source coefficient, the
shared-coupling identity, and any WEP ratio statement remain outside this
note.

## Discharge Audit

The 2026-06-17 no-go residual R2 is quoted in block01's discharge section as:

> "A separate theorem identifying an inertial rest-gap readout for physical matter."

Block01 identifies and computes the rest-gap and curvature readouts, but it
delegates the statement that `M_I` governs actual packet acceleration to a
companion inertial-closure theorem. This note supplies that companion
inertial half by T1-T3, conditional on the inherited block01 imports and the
new I-EXT probe import.

The source-side residual is untouched. In block01's language, the gamma
freedom and source-side shared-coupling question remain block04/source-side
issues. This note supplies no R3 discharge.

## Consequence

On the declared free two-step surface, the same coefficient

```text
    M_I = m sqrt(1 + m^2)
```

that block01 computes from the spectral curvature also governs the leading
packet acceleration under the species-blind I-EXT probe:

```text
    d^2<X_3>/dt^2 = -g / M_I
```

up to the explicit windowed residual
`O_m(sigma_p^2 + g^2 t^2)`. This is an inertial closure statement for the
free positive-mass surface only.

## Boundaries

- Free `U = 1`, `d = 3` two-step surface only.
- Positive mass `m > 0` only for the width-independence theorem.
- The width-independence statement's exact bound is stated for
  window-supported momentum densities; Gaussian packets carry the explicitly
  printed exponentially small tail addend of T3'.
- The T3 statement is centered at `p_bar = 0`; nonzero packet-center
  statements are not asserted here.
- The probe coefficient `g` is species-blind and external; it is not the
  gravitational source coefficient.
- No WEP claim is supplied.
- No source-side gamma identity is supplied.
- No equality between I-EXT's `g` and the gravitational source coefficient is
  supplied.
- Free packets may still spread; this note does not prove soliton-like
  persistence or fixed spatial width.
- This note sets no audit status.
- Independent audit is required.

## Dependencies

- [`MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md`](MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md)
  supplies the inherited I-DYN / I-MASS / I-TIME import surface, the scalar
  one-particle band, the positive-gap sector footing, `E(p)`, `M_I`, and the
  R2 discharge wording used here.
- [`MATTER_INERTIAL_CLOSURE_NOTE.md`](MATTER_INERTIAL_CLOSURE_NOTE.md)
  supplies the historical width-dependent negative and the dispersion-driven
  mechanism recovered in the `m -> 0` limit.
- [`EP_RECORD_STIFFNESS_WEAK_FIELD_SOURCE_READOUT_INTERFACE_NOTE_2026-06-16.md`](EP_RECORD_STIFFNESS_WEAK_FIELD_SOURCE_READOUT_INTERFACE_NOTE_2026-06-16.md)
  supplies the EP-S3a weak-field source/readout contrast showing why the
  I-EXT probe must not be treated as the gravitational coupling.
- [`FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`](FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md)
  supplies the d-dimensional two-step dispersion authority and house style
  followed by this note.

## Runner And Cache

Primary runner:
[`scripts/inertial_closure_two_step_surface_2026_07_08.py`](../scripts/inertial_closure_two_step_surface_2026_07_08.py)

Runner cache:
[`logs/runner-cache/inertial_closure_two_step_surface_2026_07_08.txt`](../logs/runner-cache/inertial_closure_two_step_surface_2026_07_08.txt)

Current local runner result:

```text
TOTAL: PASS=8 FAIL=0
```

Load-bearing residuals from the cached run: every window-qualifying run
satisfies the T3/T3' bound with margin (worst residual/bound `0.4494`, which
matches the predicted spectral-norm slack `A_iso / (3 C4_win)`); the measured
collapse coefficient matches the isotropic fourth-derivative prediction to
better than `1%` at all gated masses (`A/A_iso = 0.995, 0.990, 0.999` for
`m = 0.5, 1, 2`); the runner certifies the window `p_*(m) = min(pi/4, 0.6 m)`
and verifies numerically that the note's closed-form rest-point coefficient
is attained as the window constant; the `m = 0` control leg width-splits
(slopes `-0.078 / -0.599 / -1.184` across the historical widths), reproducing
the 2026-04-07 mechanism; the 1D open-boundary position-space evolution
agrees with the momentum-gauge prediction to `4.6e-13`.

## Changelog

- **2026-07-08.** Initial bounded-theorem note. Worker review caught a tail
  gap in the original T3 statement (a 3-sigma window with finite fourth
  moments does not control Gaussian tails); T3 was restated for
  window-supported densities with the sup-Hessian window constant and the
  T3' Gaussian tail corollary was added. Paired runner gates
  bound-compliance on window-qualifying runs; local result
  `TOTAL: PASS=8 FAIL=0`.
