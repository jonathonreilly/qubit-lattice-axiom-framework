# SU(2) Weak u_0 One-Plaquette Wilson Bracket Bounded Support

**Date:** 2026-06-18
**Claim type:** bounded_theorem (finite one-plaquette Wilson/Haar support)
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/su2_weak_u0_one_plaquette_wilson_bracket_2026_06_18.py`](../scripts/su2_weak_u0_one_plaquette_wilson_bracket_2026_06_18.py)
**Cached runner output:**
[`logs/runner-cache/su2_weak_u0_one_plaquette_wilson_bracket_2026_06_18.txt`](../logs/runner-cache/su2_weak_u0_one_plaquette_wilson_bracket_2026_06_18.txt)

## Claim Scope

This note supplies a framework-native finite one-plaquette support point for
the `u_0(SU(2))` interval consumed by
[`G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md`](G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md).
It uses the retained native `SU(2)` gauge surface and the existing
retained_bounded weak one-hop Wilson anchor `beta_W = 16`.

The durable statement is narrow:

```text
<P>_1plaq(beta) = I_2(beta) / I_1(beta),
u_0,1plaq(beta) = <P>_1plaq(beta)^(1/4),
u_0,1plaq(16) = 0.976111254449673... in [0.9761, 0.9762] subset [0.96, 0.98].
```

This retires the purely literature-only character of the `g_2(v)` row's
interval on the finite one-plaquette Wilson/Haar surface. It does not prove the
full four-dimensional nonperturbative SU(2) lattice plaquette, does not replace
a Monte Carlo vacuum calculation, does not consume an observed electroweak
`g_2`, and does not add a new axiom.

## Derivation

Parametrize a conjugacy class in `SU(2)` by

```text
U(theta) = cos(theta) 1 + i sin(theta) n . sigma,
0 <= theta <= pi,
(1/2) Tr U = cos(theta).
```

The normalized Haar class measure is

```text
dmu(theta) = (2/pi) sin(theta)^2 dtheta.
```

For the one-plaquette Wilson weight
`exp(beta (1/2) Tr U) = exp(beta cos(theta))`, the finite partition factor is

```text
Z(beta) = (2/pi) int_0^pi exp(beta cos(theta)) sin(theta)^2 dtheta
        = I_0(beta) - I_2(beta)
        = 2 I_1(beta) / beta,
```

where `I_n` is the modified Bessel function. Differentiating the finite
integral with respect to `beta` gives

```text
<P>_1plaq(beta) = d log Z(beta) / d beta
                = I_2(beta) / I_1(beta).
```

The last equality follows from the Bessel derivative and recurrence identities:

```text
d/d beta [I_0(beta) - I_2(beta)] = (I_1(beta) - I_3(beta)) / 2,
I_1(beta) - I_3(beta) = 4 I_2(beta) / beta,
I_0(beta) - I_2(beta) = 2 I_1(beta) / beta.
```

Substituting the existing weak one-hop Wilson anchor `beta_W = 16` gives

```text
<P>_1plaq(16) = 0.90781484588075051761...
u_0,1plaq(16) = <P>_1plaq(16)^(1/4)
              = 0.97611125444967325561...
```

Therefore

```text
u_0,1plaq(16) in [0.9761, 0.9762] subset [0.96, 0.98].
```

## Relation to the g_2(v) Bounded Interval Row

The `g_2(v)` interval row previously had one remaining explicit source blocker:
the interval

```text
u_0(SU(2)) in [0.96, 0.98]
```

was treated as a literature import. This note gives an internal finite
Wilson/Haar one-plaquette computation at the same `beta_W = 16` surface, so the
interval can be re-audited as supported by a framework-native one-plaquette
calculation rather than by Trottier/Munster as load-bearing authority.

The literature references remain useful as parallel context and comparison.
They are not needed for the finite one-plaquette bracket proved here.

## What This Does Not Establish

- No full four-dimensional nonperturbative SU(2) lattice vacuum plaquette.
- No proof that the one-plaquette bracket equals the infinite-volume Wilson
  action expectation value.
- No Monte Carlo import or replacement of a controlled nonperturbative
  simulation.
- No observed electroweak `g_2` import, fit, selector, or prediction.
- No new axiom, primitive, gauge group, Wilson convention, or probability
  postulate.
- No audit verdict or effective-status change.

## Dependencies

- [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md) supplies the
  retained native `Cl(3,0)^+ -> Spin(3) = SU(2)` gauge surface.
- [`SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28.md`](SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28.md)
  supplies the retained_bounded weak one-hop Wilson value `beta_W = 16`.
- The Bessel identities are proved directly by the runner from the positive
  defining series and recurrence checks; standard lattice-gauge texts may be
  cited in parallel but are not load-bearing for this finite computation.
