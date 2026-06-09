# D3 Upper-Bound Native Support Scope Gate

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Status:** exact-support branch-local native-support scope gate; not an
audit verdict and not a repo-wide dimension-selection promotion.
**Primary runner:**
[`scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py`](../scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py)
**Runner output:**
[`logs/runner-cache/frontier_d3_upper_bound_import_scope_gate_2026_06_06.txt`](../logs/runner-cache/frontier_d3_upper_bound_import_scope_gate_2026_06_06.txt)

## Purpose

This note records the narrow composition rule for the current dimension
selection packet:

1. `DIMENSION_SELECTION_NOTE.md` is a finite-runner lower-bound surface. Its
   binding result is that the runner criteria fail for `d <= 2` and pass for
   the checked dimensions `d = 3,4,5`.
2. `DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md` is a
   legacy-named bounded support wrapper. Its current load-bearing
   upper-bound edge is the native stable-circular-orbit calculation, while
   the bounded Coulomb scaling calculation supplies compatible companion
   support.
3. The decisive uniqueness step, on the current packet, is the intersection of
   the finite lower-bound support `{3,4,5}` with the native stable-circular-
   orbit upper edge `d <= 3`, giving `{3}`.
4. The weaker atomic-stability upper bound `d <= 4`, composed with the same
   lower-bound support, gives `{3,4}`. Atomic stability is therefore companion
   support here, not the unique-dimension selector unless the stronger
   `d = 3` spectral statement is separately admitted and scoped.

The gate prevents two overreads: "atomic stability alone selects `d = 3` from
the current lower-bound packet" and "the framework has internally derived a
full dimension-selection theorem." Neither follows from the current surfaces.

## Existing Surfaces

### Lower-bound surface

`DIMENSION_SELECTION_NOTE.md` says the current bounded row is lower-bound
support only. It records:

```text
d <= 2  -> fails the runner's attractive-gravity / beta~1 lower-bound criteria
d >= 3  -> passes those runner criteria for d = 3, 4, 5
```

It also says the upper-bound wrapper is separate and not load-bearing for the
bounded lower-bound claim. Any future attempt to derive `d <= 3` inside the
framework must be reviewed separately.

### Upper-bound support wrapper

`DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md` keeps its
legacy filename, but its current load-bearing role is to record two bounded
support edges:

| Support edge | Wrapper scope | Current composition with `{3,4,5}` |
|---|---|---|
| Native stable-circular-orbit upper edge | The Green-kernel/effective-potential calculation gives stable circular orbits only at integer `d = 3`; `d = 4` is marginal and `d >= 5` is unstable | `{3}` |
| Bounded Coulomb scaling companion edge | The Green-kernel quadratic-form scaling excludes `d >= 5`, leaves `d = 4` marginal, and does not prove the physical `d = 3` hydrogen spectrum | `{3,4}` for the weaker scaling/stability bound; `{3}` only if a stronger spectral statement is separately used |

The wrapper explicitly does not claim the full Bertrand closed-orbit theorem,
does not re-derive full atomic stability or a physical electromagnetic sector,
and does not give a framework-level derivation of `d = 3` from `Cl(3)` on
`Z^3` alone.

### Bounded support notes

`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md` gives bounded
support for the elementary Green-kernel/effective-potential part of the
stable-orbit route. This retires the decisive stable-circular-orbit edge for
the current finite-set composition, while the full Bertrand closed-orbit
theorem remains standard context and is not consumed by the gate.

`COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md` gives bounded
support for a Green-kernel scaling lemma under admitted continuum premises. It
does not establish a framework-native electromagnetic sector, a physical
coupling, or the full hydrogenic spectrum.

## Composition Certificate

Let the current lower-bound packet expose only the checked finite set

```text
L_runner = {3,4,5}.
```

Then:

```text
L_runner intersect {d : d <= 3} = {3}
L_runner intersect {d : d <= 4} = {3,4}
```

So the current unique-`d = 3` composition depends on the native
stable-circular-orbit upper-bound edge. Atomic stability supplies compatible
companion support, but the weaker `d <= 4` statement cannot by itself select
`d = 3` from the present lower-bound runner packet.

## What This Unlocks

- A reviewable one-hop gate for later D3 status work: reviewers can ask
  whether the native stable-circular-orbit edge is sufficient for the current
  finite-set composition, while keeping the full Bertrand theorem as
  non-load-bearing context.
- A clean separation between the lower-bound runner packet and the upper-bound
  support edges.
- A guard against using the atomic-stability lane as a silent uniqueness
  selector when only the weaker `d <= 4` stability statement is in scope.
- A narrow target for future work: derive the full closed-orbit theorem or the
  stronger hydrogenic `d = 3` spectral statement only if a later lane actually
  needs those stronger claims.

## Non-Claims

This note does not claim:

- a framework-internal derivation of the full Bertrand closed-orbit theorem;
- a framework-internal derivation of full atomic stability or the hydrogenic
  spectrum;
- a full dimension-selection theorem from `A_min`;
- a derivation of a `Z^d` substrate from the current `Z^3` substrate;
- a repo-wide audit verdict;
- a change to any active review queue, audit ledger, lane registry, status
  board, or publication matrix.

## Verification

Run:

```bash
python3 scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py
```

Expected summary:

```text
SUMMARY: PASS=35 FAIL=0
```
