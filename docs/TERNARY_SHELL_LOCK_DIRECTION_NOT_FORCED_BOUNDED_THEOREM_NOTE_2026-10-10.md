---
claim_id: ternary_shell_lock_direction_not_forced_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On a shell whose six axis directions take values in {0, 1, blank}, there are 729 shells. Under the soldered action on the six output directions, no shell has output type (1,). A stabilizer-invariant probability is unique exactly on the three constant shells 000000, 111111, and bbbbbb, and on each of those the unique law is the uniform law of mass 1/6. Every other shell has at least two invariant probabilities. Singleton output orbits occur only as an antipodal pair, as all six directions, or not at all, so no shell forces one locked direction. The uniform law and both point masses on a five-blank shell are not selected. No site and no rate are supplied. The bond factor and the 3x3 correlation are not used."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ternary_shell_lock_direction_not_forced_2026_10_10.py
---

# No ternary six-neighbor shell forces one locked direction

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/ternary_shell_lock_direction_not_forced_2026_10_10.py`](../scripts/ternary_shell_lock_direction_not_forced_2026_10_10.py)

**Carrier.** The object is one coloring of the six axis directions by
`{0, 1, blank}`. It is not a bond factor, and it is not a `3×3`
correlation. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the
six neighbor directions and the proper cubic rotations. They do not say how
a rotation moves a possibility. This note uses the soldered action only.
A blank is a color on that menu, not a deleted direction. The note does
not choose a site, and it does not define a rate.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact output-orbit census of all 729 ternary shells and the invariant probabilities on the six directions."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "No ternary shell has soldered output type (1,). The only unique invariant laws are the uniform law on 000000, 111111, and bbbbbb, and none of those laws is adopted. A menu that deletes blanks is outside this census."
conditional_surface_status: "alphabet {0, 1, blank} on the six axis directions; soldered six-direction menu; proper cubic action by permuting directions"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## What is conditional

A shell is a map from

```text
(+x, -x, +y, -y, +z, -z)
```

to `{0, 1, blank}`. There are `3^6 = 729` shells. The proper cubic group
is the 24 signed permutation matrices of determinant `1`. It acts on
shells by `(R·c)(d) = c(R^{-1} d)`.

The output action is the soldered one. The locked menu is the same six
directions, and `R` sends a direction to its image. A menu that first
deletes the blank directions is not used.

A law is a function of the shell alone. The same function may be read at
any site. That does not select the site. No clock and no rate occur.

The proper-cubic orbits of these 729 profiles are already recorded as a
count of 57, for support tables and label-equivariant menus. This note
recomputes that count as a check that the action is the same group
action. It does not restate the support-table census. The question here
is the stabilizer's action on the six output directions.

## Theorem 1 — seven output types, and no type `(1,)`

**Conclusion.** For each shell, the orbit sizes of its stabilizer on the
six directions partition 6. The shells fall into seven output types.

| output type | shells |
|---|---|
| `(6)` | 3 |
| `(4,2)` | 18 |
| `(3,3)` | 24 |
| `(4,1,1)` | 54 |
| `(2,2,2)` | 114 |
| `(2,2,1,1)` | 108 |
| `(1,1,1,1,1,1)` | 408 |

The counts sum to 729. No shell has output type `(1,)`. An output type
is a partition of 6, and `(1,)` is not such a partition. The enumeration
finds the same absence.

Enumeration and the Burnside average both give 57 shell orbits. The
Burnside sum is `1368`. For every shell, the shell-orbit size times the
stabilizer order is 24. Swapping `0` with `1` and leaving blanks fixed
preserves the output type.

## Theorem 2 — singleton output orbits are paired, total, or absent

**Conclusion.** The identity fixes all six directions. Every other proper
rotation fixes either no direction or exactly one antipodal pair. The
four rotations about `+z` are the rotations that fix `+z`, and each of
them fixes `-z`. The group is transitive on the six directions.

Therefore a direction fixed by a whole shell stabilizer is fixed together
with its antipode. The number of singleton output orbits is 0, 2, or 6.
It is 6 exactly when the stabilizer is trivial, and then every direction
is a singleton. The shell counts are 159 with no singleton, 162 with one
antipodal pair, and 408 with all six directions singleton. No shell has
exactly one singleton output orbit.

Every output orbit is monochromatic, because a stabilizer element
preserves the shell. The number of output orbits is therefore at least
the number of colors on the shell. One output orbit occurs only for a
shell that uses one color.

## Theorem 3 — the unique invariant laws are the three uniform laws

**Conclusion.** Fix a shell `c`. A probability on the six directions is
invariant under the stabilizer of `c` exactly when it is constant on the
output orbits of that stabilizer. The uniform law on one such orbit, and
zero on the others, is invariant. Distinct orbits give distinct laws.

One output orbit occurs for exactly three shells:

| shell | stabilizer | output orbit | unique law |
|---|---|---|---|
| `000000` | 24 | all six directions | uniform, mass `1/6` |
| `111111` | 24 | all six directions | uniform, mass `1/6` |
| `bbbbbb` | 24 | all six directions | uniform, mass `1/6` |

Each is a shell orbit of size 1. The stabilizer is the whole group, which
acts transitively, so every invariant probability is constant on the six
directions. The unique probability puts mass `1/6` on each direction. A
point mass is not invariant: the stabilizer moves it to all six point
masses. The support has six points. None of these shells forces one
direction. The uniform law is not selected.

Every other shell has at least two output orbits, hence at least two
invariant probabilities. In particular, no shell with one, two, three,
four, or five blanks has a unique invariant probability. There are 664
such shells. The two shells above with no blank are the constant binary
shells. The one shell with six blanks is `bbbbbb`.

The twelve shells with exactly five blanks all have output type
`(4,1,1)`. On `bbbb0b`, the recorded direction is `+z` and the other five
entries are blank. The output orbits are the equator of `z`, `{+z}`, and
`{-z}`. The point mass on `+z` and the point mass on `-z` are both
invariant, and they disagree. A point mass on `+x` is not invariant. The
single recorded direction is therefore not forced. The same two
assignments transport across all twelve shells: the image of the point
mass on the recorded direction is the point mass on the recorded
direction of the image shell, and likewise for the blank antipode. Each
image orbit has six shells. Neither law is selected.

No shell has a single output orbit of size 1. A point mass can be
invariant, but only when at least one other invariant probability exists
on the same shell. The shell does not choose a direction.

## What this does not say

- It does not adopt the uniform law, the point mass on a recorded
  direction, or the point mass on a blank antipode.
- It does not say that a supplied law is forbidden from being a point
  mass. Theorem 3 records the shells on which a point mass is invariant,
  and records that the shell does not select it.
- It does not classify a menu that deletes blank directions before the
  action. On that other menu a five-blank shell would be a one-point
  menu. That menu is not used, and it is not a selected direction.
- It does not rerun a bond factor, a cap pencil, a path correlation, a
  CHSH square, or a polynomial of a `3×3` correlation.
- It does not choose the site at which the shell is read, and it does not
  define a formation rate.
- It does not identify a shell entry or an output direction with a mass
  density.
- It does not restate the support-table census whose orbit count is 57.
  The agreement of the shell-orbit count is a check of the action, not
  a second classification of those tables.

## No-Go Discipline Gate

Scoped claim: under the soldered six-direction action, no shell with
entries in `{0, 1, blank}` forces one locked direction. Output type
`(1,)` does not occur. A unique invariant probability occurs exactly on
`000000`, `111111`, and `bbbbbb`, and that probability is the uniform
law of mass `1/6`, which is not adopted.

N1. Five attacks on that scoped claim:

1. Let the all-blank shell force a point mass because no direction is
   recorded. The stabilizer is the whole group. Transitivity gives equal
   masses, hence `1/6`, and the point mass has six images. `ATTEMPTED`.
2. Let the single recorded direction of a five-blank shell be the locked
   direction. The shell `bbbb0b` has type `(4,1,1)`. The blank antipode
   is a second singleton, and its point mass is invariant. `ATTEMPTED`.
3. Let some shell have exactly one singleton output orbit. Every
   non-identity rotation fixes at most one antipodal pair, so the
   singleton count is 0, 2, or 6. The census has no count 1.
   `ATTEMPTED`.
4. Let some partial shell have output type `(1,)`. The seven types are
   the rows of Theorem 1, and `(1,)` is not among them. `ATTEMPTED`.
5. Let a non-constant shell have one output orbit because the stabilizer
   mixes two colors. Every output orbit is monochromatic, so one orbit
   requires one color. The only one-color shells are the three constants.
   `ATTEMPTED`.

N2. Only the soldered six-direction menu is used. No second output action
is stated, and no independent-wall count is asserted.

N3. The alphabet `{0, 1, blank}`, recording of all six neighbor slots,
and the soldered action on those six directions are written as
hypotheses. No dynamics clause is used. The three approved primitives
`scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive` are not inputs.

N4. The support-table census of the 729 profiles, the mirror count of 57
proper orbits and one chiral pair, and the handed-rule base weight
`1/6` on an empty background are different carriers. Dropping them leaves
Theorems 1–3 intact: the 729 shells and their output orbits are
recomputed here. The uniform law in Theorem 3 is the unique
stabilizer-invariant probability on a constant shell. It is not that
supplied base weight, and it is not adopted.

N5. The negative sentence is about one shell and the soldered menu. The
runner resolves the 729 shells, the six directions, and the 24 rotations.
It does not resolve a second site, a block of sites, or an infinite
lattice.

N6. This note does not say that a new axiom is required. It does not
select the uniform law or either point mass. Source/action remains an
open gate. The formation rule remains downstream supplier content.

N7. Steelman, outside this menu: delete the blank directions first, and
the shell `bbbb0b` becomes a one-point menu whose only probability is the
point mass on `+z`. That is not the soldered six-direction menu. The
deletion is not executed, and the resulting point mass is not a selected
possibility. The odd cap alphabet stays stopped. The one-blank census and
the fully recorded binary census are not reopened.

N8. This note does not reopen the one-blank orbit table, the binary-shell
orbit table, the unsoldered count `1024`, the CHSH squares, the directed
correlation, the readout split, the quadratic channels, the
achiral-orbit factor, the linear factor `1 + kappa F`, the quadratic
pencil, or the shifted cap factor.

## Review record

The open question was which of the 729 ternary shells have soldered
output type `(1,)`, or a unique invariant probability on the six
directions. The finite discriminator is the census above. No shell has
type `(1,)`. The unique-invariant shells are `000000`, `111111`, and
`bbbbbb`. Each forces the uniform six-point law and does not force one
direction. The miss on a locked direction is real. The three shells are
named because they exist.

Outstanding at landing: the uniform law is not a physical rule; neither
point mass on `bbbb0b` is selected; a menu that deletes blanks is outside
the census; the site and the rate stay unsupplied; independent audit has
not reviewed this note. No helper runner is declared.

The output types, the singleton counts, and the three shell names were
fixed by a separate enumeration before the runner's expected table. The
author re-ran two load-bearing mutations on scratch copies; each printed
`FAIL=1`, and the copies were not kept.

- Demanding that a point mass be invariant on `bbbbbb` fails one check.
- Demanding that the five-blank shells have output type `(1,)` fails one
  check.

## Runner

`scripts/ternary_shell_lock_direction_not_forced_2026_10_10.py` builds
the 24 proper rotations and all 729 shells. It checks closure, the
fixed-direction bound, the Burnside count 57, orbit-stabilizer, the seven
output types and the absence of type `(1,)`, the singleton counts 159,
162, and 408, the three constant shells and their uniform law, the 664
shells with one through five blanks, the twelve five-blank shells and
the witness `bbbb0b`, the `0`/`1` swap, monochromatic output orbits, and
transport of both five-blank point masses. It reads no external
scientific input.
