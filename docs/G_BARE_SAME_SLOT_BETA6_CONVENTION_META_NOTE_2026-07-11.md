# G Bare Same-Slot and Beta=6 Convention

**Date:** 2026-07-11
**Type:** meta
**Status authority:** convention record only; this note is not a theorem and
does not set, predict, or apply an audit verdict.

## Convention

The parent `g_bare` surface uses the following explicit naming and
normalization convention:

```text
(SD)  A^a := C^a, equivalently g_bare := s.
```

Here `C^a` is the canonical finite-link coordinate, `A^a` is the field
coordinate used in the supplied standard Wilson plaquette convention, and
the canonical finite-link slot is `s = 1`. This is a same-slot definition,
not a construction-level consequence of the link or plaquette data.

On the separately proved algebraic family
`gamma*(beta)^2 = 2 N_c / beta`, choosing `(SD)` sets `gamma* = s = 1`.
The Wilson coordinate then reads

```text
beta = 2 N_c,
g_bare = 1.
```

With the supplied group label `N_c = 3`, the same convention is displayed as

```text
beta = 6.
```

These equalities are definition-level bookkeeping after `(SD)` is chosen.
They are not theorem outputs and must not be cited as a framework derivation
of `g_bare = 1`, `beta = 6`, the Wilson action surface, or the same-slot
identification.

## Algebraic context

The bounded algebraic facts that expose where this convention acts live in
[`G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md`](G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md):

- the exact split redundancy
  `gamma F[C/gamma; gamma] = F[C; 1]`;
- the matched-scalar family `gamma*(beta)^2 = 2 N_c / beta`; and
- the pin equivalence `gamma*(beta) = s` if and only if
  `beta = 2 N_c`.

That theorem note does not choose `(SD)`. This meta note records the choice
separately so labeling and normalization bookkeeping cannot be mistaken for
bounded theorem content.

## Boundary

- No new axiom, primitive, dynamics, fitted value, or observed value is
  introduced.
- No claim is made that the framework selects the Wilson plaquette action.
- A derivation of the same-slot identification from an operator or
  Hamiltonian surface remains open.
- Independent audit remains the sole authority for theorem-row status.
