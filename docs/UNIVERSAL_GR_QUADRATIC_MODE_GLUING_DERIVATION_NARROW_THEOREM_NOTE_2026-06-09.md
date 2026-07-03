# Universal GR Quadratic Mode Gluing Derivation

**Date:** 2026-06-09
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_universal_gr_quadratic_mode_gluing_derivation_2026_06_09.py`](../scripts/frontier_universal_gr_quadratic_mode_gluing_derivation_2026_06_09.py)
**Runner cache:**
[`logs/runner-cache/frontier_universal_gr_quadratic_mode_gluing_derivation_2026_06_09.txt`](../logs/runner-cache/frontier_universal_gr_quadratic_mode_gluing_derivation_2026_06_09.txt)

## Statement

This note derives the finite quadratic-mode gluing law used by the
universal-GR sign diagnostics. For a diagonal bounded channel with quadratic
Lagrangian

```text
L = (1/2) G qdot^2 - (1/2) V q^2,
```

the Euler-Lagrange equation is

```text
G qddot + V q = 0.
```

On a normal mode `q(t) = exp(i omega t)`, this gives

```text
omega^2 = V / G,     G != 0.
```

This is the gluing law used when a finite channel has already been reduced to
a kinetic coefficient `G` and a curvature/potential coefficient `V`.

## What This Repairs

The degenerate-supermetric sign diagnostic previously treated `omega^2 = V/G`
as a supplied comparator-gluing convention. This note makes that specific
gluing step a framework-local finite quadratic derivation. The diagnostic can
now import the function checked here instead of treating the gluing law itself
as an unproved premise.

## What Remains Open

This derivation does not derive the Regge/Lichnerowicz comparator signs. It
does not identify the full Einstein-Hilbert action, a continuum coefficient,
or `G_Newton`. It also does not derive a framework-native finite-`k` stress
response. Those remain separate GR-lane obligations.

The theorem is therefore narrow:

```text
Given a finite diagonal quadratic channel with coefficients (G,V),
the normal-mode frequency is omega^2 = V/G.
```

It is not a theorem that a particular framework object has already supplied the
GR values of `G` or `V`.

## Runner-Checked Content

The runner verifies:

- symbolic Euler-Lagrange reduction to `V - G omega^2`;
- exact rational examples of `omega^2 = V/G`;
- the degenerate sign-product consequence when `G_trace = G_TT`;
- the lambda-one GR control sign pattern inside the same quadratic-mode law;
- explicit source-note guardrails excluding the comparator signs and full GR
  action.

No observed value, fitted selector, new axiom, Tier-A admission, registered
scale, or physical Newton constant is used. Equivalently: this packet uses
no new axiom and no Tier-A admission.

## Relation to the Degenerate Supermetric Sign Row

For the row
`UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md`,
this note removes one supplied item: the finite quadratic gluing law. The row
still remains conditional on the supplied opposite-signed comparator pair

```text
V_trace = -k^2/2,
V_TT    = +k^2/2.
```

So the row is not promoted here. The change is smaller but real: the sign no-go
now depends on a derived finite gluing law plus a supplied comparator-sign
packet, rather than on two supplied premises.

## Command

```bash
PYTHONPATH=scripts python3 scripts/frontier_universal_gr_quadratic_mode_gluing_derivation_2026_06_09.py
```

Expected: `TOTAL: PASS=7 FAIL=0`.
