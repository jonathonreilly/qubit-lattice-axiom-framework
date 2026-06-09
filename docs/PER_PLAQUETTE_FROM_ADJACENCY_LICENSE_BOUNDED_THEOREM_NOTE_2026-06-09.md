# Per-Plaquette Link-License Finite Enumeration Support

**Date:** 2026-06-09
**Claim type:** bounded_theorem (finite enumeration under an explicit
unit-neighborhood link-support license)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_per_plaquette_from_adjacency_license_2026_06_09.py`](../scripts/frontier_per_plaquette_from_adjacency_license_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_per_plaquette_from_adjacency_license_2026_06_09.txt`](../logs/runner-cache/frontier_per_plaquette_from_adjacency_license_2026_06_09.txt)

---

## Role

This note records a narrow finite enumeration: under an explicit
unit-neighborhood lift of the nearest-neighbor dependency license from sites to
links, the rooted simple length-4 loops on the cubic lattice are exactly
plaquettes and pass the license, while the rooted simple length-6 loops all
fail it.

This is not a derivation of the gauge action from the axioms. The
unit-neighborhood link-support license is the bounded input being tested. The
registered `kinetic_isotropy_primitive` is used only for its stated one-tick
form context; it does not supply an action, source term, dynamics,
gauge-invariant class, selector, probability rule, normalization rule, or
empirical match.

## Definitions

- **Site dependency relation:** the nearest-neighbor relation `R` of the cubic
  `Z^3` lattice, with the reachability note's one-tick dependency wording used
  as context.
- **Strict link lift:** two links are adjacent only when they share a site.
- **Unit-neighborhood link-support license:** for every target link `l=(a,b)`
  in a candidate loop, every endpoint `p` of every loop link must obey
  `min(d(p,a), d(p,b)) <= 1`, where `d` is cubic graph distance.
- **Finite enumeration domain:** rooted simple closed loops at the origin on
  `Z^3`, with no immediate backtracking and no repeated undirected edge, at
  lengths 4 and 6.

## Result

The paired runner verifies:

- The strict link lift rejects the plaquette itself: opposite plaquette edges do
  not share a site. That lift is therefore too strict for any plaquette
  fundamental term.
- At length 4, there are 24 rooted simple closed loops in the enumeration; all
  are plaquettes and all satisfy the unit-neighborhood license.
- At length 6, there are 264 rooted simple closed loops in the enumeration;
  none satisfy the unit-neighborhood license.

Within this finite enumeration domain, the unit-neighborhood license selects
plaquette loops and rejects the first longer simple-loop class.

## Boundaries

- This does **not** prove that the fundamental gauge action is per-plaquette.
  It supplies finite support for that route under the explicit license above.
- This does **not** retire a structural premise, add a new primitive, amend an
  axiom, or classify the license as already derived from the framework
  baseline.
- This does **not** derive `theta_bare = 0`, import or land PR #3429's
  cross-plane claim, or assert that downstream quantities are theorems.
- This does **not** analyze all loop lengths. Lengths 4 and 6 are the tested
  finite domain.
- This does **not** change any audit status or effective status.

## Dependencies

- [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md) — contextual
  one-tick dependency wording for `R`.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) —
  approved primitive used only for one-tick form context.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the only status
authority.
