---
claim_id: one_blank_shell_lock_possibility_not_forced_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On a shell with exactly one blank axis direction and the other five entries in {0,1}, the 24 proper cubic rotations have 12 shell orbits. Under the soldered action on the six output directions, the blank direction and its antipode are singleton output orbits on every shell. No shell has a unique invariant probability, and no shell has output type (1,), so none forces one locked direction. A point mass on the blank and a point mass on the antipode are both invariant, so it is false that every covariant conditional has support larger than one point. Neither point mass is selected. No site and no rate are supplied. The bond factor and the 3x3 correlation are not used."
upstream_dependencies:
  - minimal_axioms
runner: scripts/one_blank_shell_lock_possibility_not_forced_2026_10_10.py
---

# One blank six-neighbor shell does not force one locked direction

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/one_blank_shell_lock_possibility_not_forced_2026_10_10.py`](../scripts/one_blank_shell_lock_possibility_not_forced_2026_10_10.py)

**Carrier.** The object is one coloring of the six axis directions in which
exactly one direction is blank and the other five take values in `{0,1}`.
It is not a bond factor, and it is not a `3×3` correlation. The fully
recorded `{0,1}` census is a different carrier, and its uniform law is not
used. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the six
neighbor directions and the proper cubic rotations. They do not say how a
rotation moves a possibility. This note uses the soldered action only. It
does not choose a site, and it does not define a rate.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact orbit census of the 192 one-blank shells and the stabilizer orbits of the six directions."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "No one-blank shell forces one locked direction under the soldered action. The blank and its antipode are both available point masses, and neither is adopted. Shells with two or more blanks stay outside this census."
conditional_surface_status: "exactly one blank direction; the other five entries in {0,1}; soldered six-direction menu; proper cubic action by permuting directions"
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

to `{0,1, blank}` with exactly one blank. A shell with no blank, and a
shell with two or more blanks, is outside this census. The proper cubic
group is the 24 signed permutation matrices of determinant `1`. It acts
on shells by `(R·c)(d) = c(R^{-1} d)`. The blank is a color, not a deleted
direction.

The output action is the soldered one. The locked menu is the same six
directions, and `R` sends a direction to its image. The unsoldered
two-label menu is not used.

A law is a function of the shell alone. The same function may be read at
any site. That does not select the site. No clock and no rate occur.

## Theorem 1 — twelve shell orbits

**Conclusion.** There are 192 such shells, and the action has 12 orbits.
Their sizes are

```text
6, 6, 6, 6, 12, 12, 24, 24, 24, 24, 24, 24.
```

Enumeration and the Burnside average agree. A rotation with `f` fixed
directions and `c` cycles fixes `f * 2^{c-1}` shells of this kind when
`f > 0`, and it fixes none when `f = 0`: the blank must occupy a cycle of
length 1, and every other cycle is colored `0` or `1`. The sum over the
group is `288`, and

```text
288 / 24 = 12.
```

The sum of the stabilizer orders over the 192 shells is also `288`. For
every shell, the orbit size times the stabilizer order is `24`.

## Theorem 2 — the blank and its antipode are singleton output orbits

**Conclusion.** Exactly four proper rotations fix a given direction, and
each of those four fixes the antipode. For `+z` they are the identity, the
quarter turn about `z`, the half turn about `z`, and the three-quarter
turn about `z`. The group acts transitively on the six directions.

Let `d` be the unique blank direction of a shell `c`. If `R·c = c`, then
`R` fixes `d`. Every proper rotation that fixes `d` also fixes `-d`.
Therefore every stabilizer element fixes `-d`, and both `{d}` and `{-d}`
are output orbits. The color on `-d` does not decide membership in the
stabilizer, because every candidate already fixes `-d`.

The stabilizer is determined by the four equatorial colors. Write the two
opposite equatorial pairs.

- If all four equatorial colors agree, the stabilizer has order 4 and the
  output type is `(4,1,1)`. There are 24 such shells.
- If each opposite pair is monochrome and the two pairs differ, the
  stabilizer has order 2 and the output type is `(2,2,1,1)`. There are 24
  such shells.
- Otherwise the stabilizer is trivial and the output type is
  `(1,1,1,1,1,1)`. There are 144 such shells.

These three types partition the 192 shells. No shell has type `(1,)`. A
singleton count of 1 does not occur. The number of output orbits is 3, 4,
or 6.

One representative of each orbit, written in the direction order above
with `b` for the blank, is the following.

| shell | orbit | stabilizer | output orbits |
|---|---|---|---|
| `00000b` | 6 | 4 | equator of `z`; `{+z}`; `{-z}` |
| `00001b` | 6 | 4 | equator of `z`; `{+z}`; `{-z}` |
| `00010b` | 24 | 1 | six singletons |
| `00011b` | 24 | 1 | six singletons |
| `000b11` | 12 | 2 | `{+x,-x}`; `{+y}`; `{+z,-z}`; `{-y}` |
| `00111b` | 12 | 2 | `{+x,-x}`; `{+y,-y}`; `{+z}`; `{-z}` |
| `01010b` | 24 | 1 | six singletons |
| `01011b` | 24 | 1 | six singletons |
| `010b11` | 24 | 1 | six singletons |
| `01111b` | 24 | 1 | six singletons |
| `0b1111` | 6 | 4 | `{+x}`; equator of `x`; `{-x}` |
| `11111b` | 6 | 4 | equator of `z`; `{+z}`; `{-z}` |

Swapping `0` with `1` and leaving the blank fixed preserves the output
orbits. A permutation of slots commutes with that swap.

## Theorem 3 — neither pole is a forced direction

**Conclusion.** Fix a shell `c`. A probability on the six directions is
invariant under the stabilizer of `c` exactly when it is constant on the
output orbits of that stabilizer. The uniform law on one such orbit, and
zero on the others, is invariant. Distinct orbits give distinct laws.

Every shell in this census has at least three output orbits, so at least
three invariant laws. In particular the point mass on the blank direction
and the point mass on its antipode are both invariant, and they are
distinct. Each has support size 1. The shell therefore does not force one
locked direction: the invariant probability is not unique, and it is not
a single point mass.

The same two assignments transport. Sending the point mass on the blank
of `c` by `R` yields the point mass on the blank of `R·c`, and likewise
for the antipode. Each assignment is one covariant law on all 192 shells.
The two laws disagree on every shell. Neither law is selected.

It is false that every covariant conditional has support larger than one
point. The two point masses are covariant conditionals of support size 1.
Shells whose stabilizer is nontrivial also have an invariant law of
support 2 or 4. On a trivial stabilizer every probability is invariant,
including laws of support 6. The uniform law of mass `1/6` is invariant
on every shell, because it is constant on every orbit, and it is not the
only invariant law.

Three witnesses:

- The shell `00000b` has type `(4,1,1)`. Both pole point masses are
  invariant. A point mass on `+x` is not. The equatorial orbit has size 4.
- The shell `00111b` has type `(2,2,1,1)`. Both pole point masses are
  invariant. A point mass on `+x` is not. Each equatorial orbit has size 2.
- The shell `00010b` has trivial stabilizer. All six point masses are
  invariant, and they are six different laws.

No shell has a single output orbit of size 1. A point mass can be
invariant, and on this census at least two are, but the shell does not
choose among them.

The point mass on `+x` at `00000b` is the control that fails to transport
inside the stabilizer: distinct stabilizer elements move it to distinct
masses.

## What this does not say

- It does not adopt the point mass on the blank, the point mass on the
  antipode, or the uniform law.
- It does not say that a supplied law is forbidden from being a point
  mass. Theorem 3 records that both pole point masses are invariant, and
  that the shell does not select one.
- It does not classify a shell with two or more blanks, a fully recorded
  binary shell, or a menu other than the six directions. The unsoldered
  two-label count is not redone.
- It does not rerun a bond factor, a cap pencil, a path correlation, a
  CHSH square, or a polynomial of a `3×3` correlation.
- It does not choose the site at which the shell is read, and it does not
  define a formation rate.
- It does not identify a shell entry or an output direction with a mass
  density.

## No-Go Discipline Gate

Scoped claim: under the soldered six-direction action, no shell with
exactly one blank forces one locked direction. The blank and its antipode
are always both singleton output orbits, so both point masses are
invariant and neither is the unique invariant law. Support size 1 occurs,
and it is not selected.

N1. Five attacks on that scoped claim:

1. Let the blank be the unique distinguished slot, and let the shell force
   the point mass there. The antipode is a second singleton, and its point
   mass is invariant. `ATTEMPTED`.
2. Let the recorded antipode be the unique locked direction. The blank is
   a singleton as well, and its point mass is invariant. `ATTEMPTED`.
3. Let a constant equator force the blank by transitivity on the other
   four directions. The shell `00000b` has type `(4,1,1)`. Both pole point
   masses are invariant, and a point mass on `+x` is not. `ATTEMPTED`.
4. Let a trivial stabilizer select `+x` because every direction is a
   singleton. The shell `00010b` admits all six point masses. `ATTEMPTED`.
5. Let some shell have output type `(1,)`. The only types are `(4,1,1)`,
   `(2,2,1,1)`, and `(1,1,1,1,1,1)`. `ATTEMPTED`.

N2. Only the soldered menu is used. No second output action is stated, and
no independent-wall count is asserted.

N3. Exact one-blank recording, the alphabet `{0,1, blank}`, and the
soldered action on the six directions are written as hypotheses. No
dynamics clause is used. The three approved primitives
`scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive` are not inputs.

N4. The fully recorded binary census, the channel probe in which a blank
slot contributes `I/2`, the priority rule that orients an edge toward a
blank neighbor, and the algebra-action count of initially blank neighbors
are different carriers. Dropping them leaves Theorems 1–3 intact: the 192
shells and their output orbits are recomputed here.

N5. The negative sentence is about one shell and the soldered menu. The
runner resolves the 192 shells, the six directions, and the 24 rotations.
It does not resolve a second site, a block of sites, or an infinite lattice.

N6. This note does not say that a new axiom is required. It does not
select either point mass. Source/action remains an open gate. The formation
rule remains downstream supplier content.

N7. Steelman, outside this census: two or more blank directions can put
the antipode in the blank set, and the pair of singletons used here need
not survive. That census is not executed. A supplied law may still put
mass 1 on the blank direction of a one-blank shell; the shell also allows
mass 1 on the antipode. That escape is not a selected possibility, and it
is not queued. The odd cap alphabet stays stopped. The uniform law on a
fully recorded constant shell is not reopened.

N8. This note does not reopen the binary-shell orbit table, the unsoldered
count `1024`, the CHSH squares, the directed correlation, the readout
split, the quadratic channels, the achiral-orbit factor, the linear factor
`1 + kappa F`, the quadratic pencil, or the shifted cap factor.

## Review record

The open question was whether allowing one axis direction to be blank, and
not only `0` or `1`, makes a soldered conditional lock one direction. The
finite discriminator is the census above. The miss is real on both arms.
No shell in this census forces one direction. It is also false that every
covariant conditional has support larger than one point: the blank and
its antipode each carry an invariant point mass, and the shell does not
choose between them.

Outstanding at landing: neither point mass is selected; the uniform law is
not a physical rule; two or more blanks are outside the census; the site
and the rate stay unsupplied; independent audit has not reviewed this
note. No helper runner is declared.

The orbit sizes and the output-orbit table were written before the
matching runner lines. The author re-ran two load-bearing mutations on
scratch copies; each exited with `FAIL=1`, and the copies were not kept.

- Demanding that the antipode point mass fail to be invariant on
  `00000b` fails one check.
- Demanding that the `+x` point mass be invariant on `00000b` fails one
  check.

## Runner

`scripts/one_blank_shell_lock_possibility_not_forced_2026_10_10.py` builds
the 24 proper rotations, the 192 shells, and the stabilizer of each shell.
It checks closure, the four rotations about `+z`, the Burnside count, the
twelve-row table, orbit-stabilizer, the blank and antipode singletons, the
three output types and the counts 24, 24, and 144, the three witnesses,
transport of both point-mass laws, transport of every uniform-on-one-orbit
law of every representative, the ill-defined equatorial point mass, and
the `0`/`1` swap. It reads no external scientific input.
