# Fractional-Instanton Action Core From Topological Infrastructure

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/fractional_instanton_action_core_split_2026_06_18.py`](../scripts/fractional_instanton_action_core_split_2026_06_18.py)
**Cached runner output:**
[`logs/runner-cache/fractional_instanton_action_core_split_2026_06_18.txt`](../logs/runner-cache/fractional_instanton_action_core_split_2026_06_18.txt)

## Claim

The fractional-instanton action core used by the external dilute-gas parent
has a bounded support split from the retained-bounded topological-instanton
infrastructure.

Given the fixed-convention bounded authorities
[`TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.md`](TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.md),
for the twisted-sector topological arithmetic and
[`INSTANTON_4D_ACTION_8PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`](INSTANTON_4D_ACTION_8PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md)
for the fixed Euclidean action normalization, the topological sector arithmetic supplies

```text
Q = k/N
```

on the twisted `T^4` surface, and the bounded action normalization supplies

```text
S_E >= (8*pi^2/g^2) |Q|.
```

Therefore the self-dual/anti-self-dual saturated action coefficient in a
fractional sector is

```text
S_frac(k,N) = (8*pi^2/g^2) |k/N|.
```

This is the action-core algebra only. It does not derive a dilute-gas
determinant, measure, coupling-scale prescription, convergence theorem,
condensate criterion, framework substrate identification, or hierarchy
observable.

## Finite Arithmetic Core

The core is just substitution into the retained-bounded topological authority:

```text
Q = k/N
S_frac = (8*pi^2/g^2) |Q|
       = (8*pi^2/g^2) |k/N|.
```

The useful checks are:

```text
N=1, k=1: S_frac = 8*pi^2/g^2      (integer BPST normalization)
N=2, k=1: S_frac = 4*pi^2/g^2      (half-action scale)
N=3, k=1: S_frac = (8/3)*pi^2/g^2
N=4, k=1: S_frac = 2*pi^2/g^2
```

At the external convention `g^2=1`, this reproduces the parent table's raw
Boltzmann factors:

```text
N=2: exp(-4*pi^2)       ~= 7.16e-18
N=3: exp(-(8/3)*pi^2)   ~= 3.7e-12
N=4: exp(-2*pi^2)       ~= 2.7e-9
```

Those factors are arithmetic outputs of the fixed external normalization. They
are not framework predictions and do not by themselves establish a condensate,
scale ratio, or hierarchy mechanism.

## What This Splits From The Parent

The parent open-gate note
`FRACTIONAL_INSTANTON_DILUTE_GAS_CONDENSATE_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`
mixes two kinds of content:

- the fractional charge/action algebra above; and
- the external dilute-gas/condensate modeling target.

This note isolates the first item. The second item remains open external
model-regime material: the one-loop determinant, phase-space measure,
running-coupling scale, density of states, finite-volume/temperature regime,
and dilute-gas convergence still require separate authority before any
framework claim can consume them.

## What This Does Not Close

- No Yang-Mills topology is derived from `Cl(3,0)` on `Z^3`.
- No twisted `T^4` sector is identified with the framework substrate.
- No framework observable is identified with a fractional-instanton sector.
- This note does not identify the framework substrate with a 4D SU(N)
  twisted-torus gauge background.
- This note does not derive a dilute-gas determinant, measure, coupling scale,
  convergence criterion, or condensate formation theorem.
- This note does not close alpha_LM^16, `v/M_Pl`, any `alpha^N` hierarchy, or
  any physical scale ratio.
- This note does not derive a hierarchy scale ratio or numerical prediction.
- No new axiom, fitted value, or observed target value is used.

## Runner Certificate

The paired runner checks:

- upstream `topological_instanton_textbook_infrastructure_import` and
  `instanton_4d_action_8pi2_over_g2_external_narrow` are retained-bounded in
  the live ledger;
- `S_frac = (8*pi^2/g^2)|k/N|` as exact rational arithmetic in the coefficient
  of `pi^2/g^2`;
- integer and half-charge limits;
- the parent table's canonical `g^2=1` numerical factors;
- the parent cites this action-core split while preserving the dilute-gas and
  condensate blockers;
- no status promotion, hierarchy closure, or substrate closure is introduced.

Expected result: `SCORECARD PASS=9 FAIL=0`.
