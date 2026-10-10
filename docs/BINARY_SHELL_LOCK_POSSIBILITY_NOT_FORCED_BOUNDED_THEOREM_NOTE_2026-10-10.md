---
claim_id: binary_shell_lock_possibility_not_forced_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On a fully recorded binary coloring of the six axis directions, the 24 proper cubic rotations have 10 shell orbits. Under the soldered action on the six output directions, a conditional probability is covariant exactly when it is constant on the stabilizer's output orbits. The two constant shells force the uniform law of mass 1/6, whose support has six points. Every other shell has at least two output orbits, no shell has output type (1,), and singleton output orbits occur only in pairs, so no shell forces one locked direction. Under the unsoldered action on a two-label menu, there are 1024 covariant deterministic laws and 511 varying laws lock each label at each shell. No site and no rate are supplied. The bond factor and the 3x3 correlation are not used."
upstream_dependencies:
  - minimal_axioms
runner: scripts/binary_shell_lock_possibility_not_forced_2026_10_10.py
---

# A binary six-neighbor shell does not force one locked possibility

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/binary_shell_lock_possibility_not_forced_2026_10_10.py`](../scripts/binary_shell_lock_possibility_not_forced_2026_10_10.py)

**Carrier.** The object is one fully recorded coloring of the six axis
directions by `{0,1}`. It is not a bond factor on the orbit of `(0, 1, 2)`,
and it is not a `3×3` correlation. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
supply the six neighbor directions and the proper cubic rotations. They do
not say how a rotation moves a possibility. This note compares two supplied
actions and adopts neither. It does not choose a site, and it does not
define a rate.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact orbit census of the 64 binary shells and the stabilizer orbits of the six directions, plus the unsoldered count 1024."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "No binary shell forces one locked possibility under either supplied action. The constant shells force only the uniform six-point law, and only under the soldered action. Do not adopt that law. Do not return to the odd cap alphabet."
conditional_surface_status: "fully recorded {0,1} shells; soldered six-direction menu or unsoldered two-label menu; proper cubic action by permuting directions"
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

to `{0,1}`. All six neighbors are recorded. A blank neighbor is outside
this census. The proper cubic group is the 24 signed permutation matrices
of determinant `1`. It acts on shells by `(R·c)(d) = c(R^{-1} d)`.

Two output actions are supplied separately.

- **Soldered.** The locked menu is the same six directions, and `R` sends
  a direction to its image.
- **Unsoldered.** The locked menu is `{0,1}`, and `R` does not move the
  label.

A law is a function of the shell alone. The same function may be read at
any site. That does not select the site. No clock and no rate occur.

## Theorem 1 — ten shell orbits

**Conclusion.** The action on the 64 shells has 10 orbits. Their sizes are

```text
1, 1, 3, 3, 6, 6, 8, 12, 12, 12.
```

Enumeration and the Burnside average agree. For a rotation `g` with `c(g)`
cycles on the six directions, `2^{c(g)}` shells are fixed, and

```text
(1/24) * sum_g 2^{c(g)} = 10.
```

For every shell, the orbit size times the stabilizer order is `24`.

## Theorem 2 — output orbits of the ten representatives

**Conclusion.** Write a shell as the six bits in the direction order above.
One representative of each orbit has the following stabilizer order and
output orbits under the soldered action.

| shell | orbit | stabilizer | output orbits |
|---|---|---|---|
| `000000` | 1 | 24 | all six directions |
| `000001` | 6 | 4 | equator of `z`; `{+z}`; `{-z}` |
| `000011` | 3 | 8 | equator of `z`; `{+z,-z}` |
| `000101` | 12 | 2 | `{+x,-x}`; `{+y,+z}`; `{-y,-z}` |
| `000111` | 12 | 2 | `{+x,-x}`; `{+y}`; `{-y}`; `{+z,-z}` |
| `010101` | 8 | 3 | `{+x,+y,+z}`; `{-x,-y,-z}` |
| `001111` | 3 | 8 | `{+x,-x}`; the other four |
| `010111` | 12 | 2 | `{+x,+y}`; `{-x,-y}`; `{+z,-z}` |
| `011111` | 6 | 4 | `{+x}`; `{-x}`; the other four |
| `111111` | 1 | 24 | all six directions |

The six distinct output types are `(6)`, `(4,1,1)`, `(4,2)`, `(2,2,2)`,
`(2,2,1,1)`, and `(3,3)`. No shell, representative or not, has type `(1)`.
A shell that has a singleton output orbit has at least two of them.
Complementing every bit preserves the output orbits, because a permutation
of slots commutes with that complement.

## Theorem 3 — the soldered menu forces a distribution only for the constant shells

**Conclusion.** Fix a shell `c`. A probability on the six directions is
invariant under the stabilizer of `c` exactly when it is constant on the
output orbits of that stabilizer. The uniform law on one such orbit, and
zero on the others, is invariant. Distinct orbits give distinct laws.

The two constant shells have one output orbit, of size 6. Their only
invariant probability is the uniform law, mass `1/6` on each direction.
A point mass is not invariant: the stabilizer is the whole group, which
acts transitively. The support has six points. The shell forces that
distribution and does not force one direction.

Every non-constant shell has at least two output orbits, so at least two
invariant probabilities. In particular the shell `000001`, one occupied
pole at `-z`, has singleton orbits `{+z}` and `{-z}`. Both point masses
are invariant, and a point mass on `+x` is not. The shell `010101` has
two orbits of size 3 and no invariant point mass. The shell `000011` splits
into a pair and an equator and has no invariant point mass.

No shell has a single output orbit of size 1. Therefore no binary shell
forces one locked direction. A point mass can be invariant, when a
singleton orbit exists, but a second invariant point mass exists on the
same shell. The shell does not choose between them.

Transport is well defined. If a probability is constant on the output
orbits of `c`, its rotate by `R` depends only on the image shell `R·c`,
and that rotate is invariant under the stabilizer of the image. This holds
for the uniform-on-one-orbit law of every output orbit of every
representative. The point mass on `+x` at the zero shell is the control
that fails: distinct stabilizer elements move it to distinct masses.

## Theorem 4 — the unsoldered menu forces neither label

**Conclusion.** If the output label is not moved, a function
`f` from shells to `{0,1}` is covariant exactly when it is constant on
shell orbits. There are `2^{10} = 1024` such functions. The two constant
functions do not vary with the shell. The other `1022` do.

Fix a shell. Setting the value on its orbit and assigning the remaining
nine orbits freely gives `2^9 = 512` covariant functions that lock a
chosen label there. One of those 512 assigns that label to every orbit.
Hence `511` varying covariant functions lock each label at that shell.
The indicators used below are two of them. On a shell other than the two
constants, they are the indicator of its own orbit and the indicator of
the all-zero orbit. On the all-zero shell they are the indicator of that
orbit and the indicator of the all-one orbit, and conversely on the
all-one shell.

The coordinate function `c |-> c(+x)` is not covariant. The quarter turn
about `z` lies in the group and sends the shell with only `+x` occupied
to the shell with only `+y` occupied. Those shells are in one orbit, and
the function takes both values there.

So unsoldered covariance plus variation still does not force the locked
label. Both labels remain available at every shell.

## What this does not say

- It does not adopt the uniform law, either point mass, or either label.
- It does not say that a supplied law is forbidden from being a point mass.
  Theorem 3 records the shells on which a point mass is invariant, and
  records that the shell does not select it.
- It does not classify a menu other than the six directions or the
  unsoldered pair `{0,1}`. A blank slot, a partial shell, and a recorded
  Bloch vector are different carriers.
- It does not rerun a bond factor, a cap pencil, a path correlation, a
  CHSH square, or a polynomial of a `3×3` correlation.
- It does not choose the site at which the shell is read, and it does not
  define a formation rate.
- It does not identify a shell bit or an output direction with a mass
  density.

## No-Go Discipline Gate

Scoped claim: under either supplied action, no fully recorded binary shell
forces one locked possibility. Under the soldered action the two constant
shells force the uniform six-point law and nothing smaller. Under the
unsoldered action both labels survive at every shell.

N1. Five attacks on that scoped claim:

1. Let the constant shell force a point mass because every direction is
   equivalent. Transitivity gives equal masses, hence `1/6`, and the
   runner rejects the point mass. `ATTEMPTED`.
2. Let the single occupied pole force its own direction. The shell
   `000001` has two singleton orbits, `{+z}` and `{-z}`, and both point
   masses are invariant. `ATTEMPTED`.
3. Let the three negative directions force one triple to a point. The
   shell `010101` has two orbits of size 3, and no point mass is
   invariant. `ATTEMPTED`.
4. Let unsoldered covariance identify the two labels. The quarter turn
   about `z` preserves every orbit indicator and moves the `+x` bit,
   which is the non-covariant control. `ATTEMPTED`.
5. Let some size-1 shell orbit other than the constants have output type
   `(1)`. The only size-1 shell orbits are the two constants, and their
   output orbit has size 6. No shell has type `(1)`. `ATTEMPTED`.

N2. The soldered menu and the unsoldered menu are alternative supplied
actions, not two walls of one claim. Theorems 3 and 4 are stated
separately. No independent-wall count is asserted.

N3. Full recording, the binary alphabet, and the action on outputs are
written as hypotheses. No dynamics clause is used. The three approved
primitives `scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive` are not inputs.

N4. The covariant pair of finite-support laws on a parity bit, the
broadcast bounds for an independent product, and the antipodal fair-coin
statement for recorded Bloch vectors are different carriers. Dropping
them leaves Theorems 1–4 intact: the 64 shells and their output orbits
are recomputed here.

N5. The negative sentence is about one shell and one output menu. The
runner resolves shells, directions, and the two actions. It does not
resolve a second site, a block of sites, or an infinite lattice.

N6. This note does not say that a new axiom is required. It does not
select either action. Source/action remains an open gate. The formation
rule remains downstream supplier content.

N7. Steelman, outside these two menus: a stabilizer that flips the two
points of an antipodal menu can force those two weights to agree, and a
blank neighbor can change the shell. Neither menu is the one used here.
A supplied law may still put mass 1 on a singleton orbit; the shell does
not choose which singleton. That escape is not a selected possibility,
and it is not queued. The odd cap alphabet stays stopped.

N8. This note does not reopen the CHSH squares, the directed correlation,
the readout split, the quadratic channels, the achiral-orbit factor, the
linear factor `1 + kappa F`, the quadratic pencil, or the shifted cap
factor.

## Review record

The open question was what a nearest-neighbor condition can force about
which possibility a forming record locks, with the site and the rate left
unsupplied. The finite discriminator is the census above. The miss is
real: no shell in this census forces one possibility. The uniform law on
a constant shell is a forced distribution under one supplied action, not
a forced possibility, and it is not adopted.

Outstanding at landing: neither action is selected; the uniform law is
not a physical rule; blanks and partial shells are outside the census;
the site and the rate stay unsupplied; independent audit has not reviewed
this note. No helper runner is declared.

The orbit sizes and the output-orbit table were written before the
matching runner lines. The author re-ran two load-bearing mutations on
scratch copies; each exited with `FAIL=1`, and the copies were not kept.

- Demanding that a point mass be invariant on the zero shell fails one check.
- Demanding that the `+x` bit agree with its quarter-turn image fails one check.

## Runner

`scripts/binary_shell_lock_possibility_not_forced_2026_10_10.py` builds the
24 proper rotations, the 64 shells, and the stabilizer of each shell. It
checks closure, the Burnside count, the ten-row table, orbit-stabilizer,
the six output types, the absence of type `(1)`, paired singletons,
complements, the uniform law, the two pole masses, the two triple orbits,
the pair-and-equator split, transport of every uniform-on-one-orbit law,
the ill-defined point mass, the unsoldered indicator pair, the count
`511`, and the quarter-turn control. It reads no external scientific input.
