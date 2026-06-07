# Mass/Yukawa Holomorphic Determinant Selector No-Go Note

**Date:** 2026-06-07
**Claim type:** no_go
**actual_current_surface_status:** no-go
**trace_class:** negative_route_pruning
**reachability_to_target:** prunes
**Status authority:** source-note proposal only. Independent review and audit
are required before this branch-local result can be used as an effective
repo-wide status.
**Primary runner:** [`scripts/frontier_mass_yukawa_holomorphic_determinant_selector_no_go_2026_06_07.py`](../scripts/frontier_mass_yukawa_holomorphic_determinant_selector_no_go_2026_06_07.py)
**Cached log:** [`logs/runner-cache/frontier_mass_yukawa_holomorphic_determinant_selector_no_go_2026_06_07.txt`](../logs/runner-cache/frontier_mass_yukawa_holomorphic_determinant_selector_no_go_2026_06_07.txt)

## Question

After the native Berry route failed, the live route became:

```text
mass/Yukawa fluctuation determinant
  -> holomorphic or Pfaffian doublet count
  -> det_C rather than det_R
  -> r=1/2.
```

This note tests what the current finite doublet actually supplies.  The answer
is a fork, not a selector.

## Finite Statement

On the two-real-dimensional faithful doublet, let

```text
J = [[0,-1],[1,0]]
L(u,v) = [[u,-v],[v,u]]
z = u + i v.
```

Then `J^2=-I`, `LJ=JL`, and

```text
det_R(L) = u^2 + v^2 = det_C(L) conjugate(det_C(L)).
```

Thus the current carrier supports both determinant functors:

```text
det_C: one holomorphic doublet slot
det_R: two real doublet slots.
```

They are both multiplicative and compatible with the same `J`-linear carrier.
Choosing one is a polarization/action-family choice, not a consequence of the
mass operator alone.

## Consequence For The Koide Dial

With the usual finite energy bookkeeping

```text
E_singlet = 3 a^2
E_doublet = 6 |b|^2,
```

the two counts give:

```text
real/vector count       (1,2) -> r=1
holomorphic/chiral count (1,1) -> r=1/2.
```

The runner verifies that changing Gaussian versus Berezin statistics does not
decide this fork:

| action family | polarization | doublet count | result |
|---|---:|---:|---:|
| real Gaussian | real | 2 | `r=1` |
| Majorana Berezin | real | 2 | `r=1` |
| holomorphic Gaussian | holomorphic | 1 | `r=1/2` |
| holomorphic Berezin | holomorphic | 1 | `r=1/2` |

Statistics is not the selector.  Polarization is.

## Pfaffian Boundary

A Pfaffian can produce the square root:

```text
Pf(mJ)^2 = det(mJ) = m^2.
```

But using `Pf(mJ)` requires choosing the antisymmetric bilinear `mJ` as the
fermionic action.  The current finite carrier also admits the real metric form
`mI`, whose determinant is `m^2`.  The Pfaffian is therefore not a free output
of the mass/Yukawa operator; it is selected by the action family.

## Route-Pruning Result

The current surface does not derive:

```text
the generation mass/Yukawa fluctuation determinant is holomorphic/Pfaffian.
```

It derives the exact square relation and the two possible counts.  The missing
selector is the physical action/polarization theorem that says the charged
lepton generation fluctuation is the holomorphic/Pfaffian one rather than the
real/vector one.

## What This Prunes

This prunes only the route:

```text
the current finite mass/Yukawa determinant functor itself selects det_C.
```

It does not prove:

- that a later staggered-Dirac mass/Yukawa realization cannot derive a
  holomorphic/Pfaffian action;
- that a rooted spin-generation-entangling carrier cannot change the field
  module;
- that `r=1/2` is impossible;
- that the existing open-gate FS/chiral-vs-vector count is wrong.

It says the current determinant algebra exposes the fork exactly and leaves the
physical action-family selector open.

## Runner Certificate

The cached run reports:

```text
SCORECARD: PASS=21 FAIL=0
```

## Audit Boundary

This branch does not edit `docs/audit/**`, set an audit verdict, update an
audit queue, or mark a row as retained.  It supplies a reviewable route-pruning
packet for independent review.
