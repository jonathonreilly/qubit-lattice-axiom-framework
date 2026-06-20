# G Bare Parent Finite-Link/Wilson Beta=6 Bridge

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Audit status:** set only by the independent audit lane. This source note
does not set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py`](../scripts/g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py)

## Purpose

The parent note `G_BARE_DERIVATION_NOTE.md` needs a non-circular supply of the
`beta = 6` surface. This sentence names the target parent but is not a
citation-graph dependency of this bridge note. The older route mixed two steps:

```text
beta = 2 N_c = 6
g_bare^2 = 2 N_c / beta = 1
```

This bridge separates them.

- [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md)
  supplies the finite-link canonical scalar slot: once the fixed canonical
  `SU(3)` generator basis is chosen, there is no independent scalar
  multiplier in the link exponent. In canonical finite-link coordinates,
  this is the `g_link^2 = 1` slot.
- [`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md)
  supplies the Wilson coefficient identity inside the supplied standard
  Wilson plaquette action:

```text
beta g_bare^2 = 2 N_c.
```

This note proves that the scalar in those two statements is the same scalar
slot on the parent surface: the scalar multiplying the same canonical
generators `T_a` in the finite-link/plaquette exponent.

## Claim

Assume:

1. A finite `SU(3)` link is expressed in canonical generator coordinates:

```text
U = exp(i A^a T_a a).
```

2. A Wilson plaquette on the same canonical basis uses the scalar slot
   `g_bare` in the exponent:

```text
U_P = exp(i a^2 g_bare F^a T_a + O(a^3)).
```

3. The finite-link rigidity theorem removes an independent scalar multiplier
   in the canonical `T_a` basis.

4. The Wilson small-`a` theorem gives `beta g_bare^2 = 2 N_c`.

Then the parent surface has

```text
g_bare^2 = 1
beta = 2 N_c.
```

For `N_c = 3`, this gives

```text
beta = 6.
```

## Proof

The finite-link theorem fixes the canonical generator basis. A scalar
insertion

```text
U = exp(i s A^a T_a a)
```

can be absorbed into the coefficient vector of the same operator, but it is
not an additional scalar-normalization freedom of the fixed `T_a` basis. The
canonical coordinate surface is therefore `s = 1`.

The Wilson small-`a` theorem's `g_bare` is exactly the scalar multiplying the
same canonical generators in the plaquette exponent. Since the parent row uses
that same finite-link `SU(3)` surface, `g_bare = s = 1` on the canonical
coordinate branch.

Substitute this into the Wilson coefficient identity:

```text
beta g_bare^2 = 2 N_c
g_bare^2 = 1
beta = 2 N_c.
```

At `N_c = 3`, exact rational arithmetic gives `beta = 6`.

## Boundary

This note does not claim:

- Wilson plaquette action-surface selection from framework axioms;
- exclusion of improved or non-Wilson gauge actions;
- a continuum running-coupling value;
- global logarithm-branch selection;
- a phenomenological fitted coupling;
- a dynamical fixed point;
- an audit verdict or any effective-status promotion.

The result is a bounded composition theorem internal to the finite-link
canonical Wilson surface.

## Falsifiers

The bridge would fail if any of the following were true:

- the Wilson theorem's `g_bare` were not the scalar multiplying the canonical
  `T_a` in the plaquette exponent;
- the parent row used a noncanonical finite-link scalar slot `s != 1`;
- the downstream use needed Wilson action-surface selection rather than the
  supplied standard Wilson surface;
- a continuum/global gauge-field interpretation were load-bearing.

The runner checks these as source-boundary guards rather than audit verdicts.

## Verification

Run:

```text
python3 scripts/g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py
```

Expected:

```text
TOTAL: PASS=37 FAIL=0
```
