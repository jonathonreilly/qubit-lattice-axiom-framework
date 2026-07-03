# D3 Upper-Bound Native Stable-Orbit Scope Gate

**Date:** 2026-06-06
**Type:** bounded_theorem
**Status:** exact-support branch-local native-stable-edge gate; not an audit
verdict and not a repo-wide dimension-selection promotion.
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
   legacy-named upper-bound wrapper. On the current surface it routes the
   decisive upper edge through the native stable-circular-orbit support note,
   with textbook Bertrand sources cited only in parallel for the stronger
   closed-orbit theorem.
3. The decisive uniqueness step, on the current packet, is the intersection of
   the finite lower-bound support `{3,4,5}` with the native stable-orbit upper
   edge `d <= 3`, giving `{3}`.
4. The weaker Coulomb Green-kernel scaling companion excludes `d >= 5` on
   its admitted quadratic form and leaves `d = 4` marginal; composed with the
   same lower-bound support, it gives `{3,4}`. Coulomb scaling is therefore
   companion support here, not the unique-dimension selector.

The gate prevents two overreads: "the Coulomb companion alone selects `d = 3`
from the current lower-bound packet" and "the framework has derived the full
Bertrand closed-orbit theorem, hydrogen spectrum, or full atomic-stability
theorem." Neither follows from the current surfaces.

## Existing Surfaces

**Load-bearing one-hop authorities for re-audit:** the finite lower-bound
packet is [`DIMENSION_SELECTION_NOTE.md`](DIMENSION_SELECTION_NOTE.md); the
native stable-orbit upper edge is
[`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md);
the weaker Coulomb Green-kernel scaling companion is
[`COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md).
Legacy wrapper filenames below are context for the route history, not
additional load-bearing authorities for this gate.

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

### Upper-bound wrapper

`DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md` keeps its
legacy filename but now records a native stable-orbit source edge plus a
bounded Coulomb Green-kernel scaling companion:

| Route | Wrapper scope | Current composition with `{3,4,5}` |
|---|---|---|
| Native stable-circular-orbit edge | Green-kernel/effective-potential sign gives stable circular gravitational orbits only through `d <= 3` on the checked packet | `{3}` |
| Coulomb Green-kernel scaling companion | The admitted Green-kernel quadratic form is unbounded below for `d >= 5`, leaves `d = 4` marginal under scaling, and does not prove a hydrogenic spectrum | `{3,4}` for the weaker scaling companion |

The wrapper explicitly does not prove the full Bertrand closed-orbit theorem,
does not prove the full atomic-stability theorem or hydrogenic spectrum, and
does not give a framework-level derivation of `d = 3` from `Cl(3)` on `Z^3`
alone.

### Bounded support notes

`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md` gives bounded
support for the elementary Green-kernel/effective-potential part of the
stable-orbit route. The current finite-set composition consumes that native
stable-circular-orbit edge, not the full Bertrand theorem.

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

So the current unique-`d = 3` composition depends on the native stable-orbit
upper edge. Atomic stability supplies compatible companion support, but the
weaker `d <= 4` statement cannot by itself select `d = 3` from the present
lower-bound runner packet.

## What This Unlocks

- A reviewable one-hop gate for later D3 status work: reviewers can ask
  whether the native stable-circular-orbit support edge is sufficient for the
  current finite packet or demand a stronger closed-orbit theorem.
- A clean separation between the lower-bound runner packet and the upper-bound
  native stable-orbit edge plus bounded Coulomb Green-kernel scaling
  companion.
- A guard against using the Coulomb scaling lane as a silent uniqueness
  selector when only the weaker `d >= 5` exclusion / `d = 4` marginality
  statement is in scope.
- A narrow target for future work: either audit the native stable-orbit edge as
  sufficient for this finite packet, or build stronger native closed-orbit and
  atomic-stability theorems.

## Non-Claims

This note does not claim:

- a framework-internal derivation of the full Bertrand closed-orbit theorem;
- a framework-internal derivation of atomic stability or a hydrogenic
  spectrum;
- a full dimension-selection theorem from the current Lattice/Quantum/Record
  baseline;
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
SUMMARY: PASS=34 FAIL=0
```
