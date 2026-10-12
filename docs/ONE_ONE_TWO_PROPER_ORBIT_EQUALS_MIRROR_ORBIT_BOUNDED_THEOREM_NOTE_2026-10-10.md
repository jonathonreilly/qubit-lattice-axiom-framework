---
claim_id: one_one_two_proper_orbit_equals_mirror_orbit_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "The proper cubic orbit of the record value (1, 1, 2) has 24 points and equals its orbit under the 48 signed permutation matrices. One improper mirror, the swap of the two unit axes, fixes (1, 1, 2) and carries every improper image into the proper orbit. The orbit is exactly the 24 integer vectors of absolute values 1, 1, and 2. It is not a chiral pair. Orbit equality is not a selected law, a mass density, a formation site, or a rate. The orbit of (1, 2, 2) is not enumerated."
upstream_dependencies:
  - minimal_axioms
runner: scripts/one_one_two_proper_orbit_equals_mirror_orbit_2026_10_10.py
---

# The proper orbit of (1, 1, 2) already contains one improper mirror

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/one_one_two_proper_orbit_equals_mirror_orbit_2026_10_10.py`](../scripts/one_one_two_proper_orbit_equals_mirror_orbit_2026_10_10.py)

**Carrier.** The object is the integer triple `(1, 1, 2)`, acted on by
signed permutation matrices in the same way the
[order-blind factor note](ACHIRAL_ZERO_ONE_TWO_ORBIT_ORDER_BLIND_FACTOR_BOUNDED_THEOREM_NOTE_2026-10-09.md)
acted on `(0, 1, 2)`. That note proved its own orbit is not a chiral pair
and then built a bond product. This note does not import that product, the
value `kappa = 1/2`, or the path correlation `1/72`. It asks only whether
the proper orbit of `(1, 1, 2)` equals the orbit under the full
signed-permutation group.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply proper cubic
rotations about each site. They do not supply improper mirrors as
symmetries of the admissibility rule. The full signed-permutation set is
the comparison set, not an extra axiom. Reading note (2) still says the
distribution does not supply the formation site, probability, or rate. The
open-gate list still names "source/action and physical-observable
identification." This count does not close either sentence, and it does
not select a law.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact comparison of one proper orbit with the full signed-permutation orbit, by enumeration of a finite group."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "The proper orbit of (1, 1, 2) equals its mirror orbit and is not a chiral pair. Equality is not a selected law. The orbit of (1, 2, 2) stays unenumerated. Formation site, probability, and rate stay unsupplied."
conditional_surface_status: "one integer triple (1, 1, 2); action by the 48 signed permutation matrices; proper matrices are those of determinant +1"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## What is conditional

`G` is the set of `3×3` signed permutation matrices. `O` is the subset of
determinant `+1`. These are the same matrices used to compare `(0, 1, 2)`
with its mirror. They are a mathematical comparison, not a claim that an
improper mirror is a symmetry of the admissibility rule. The triple is a
record value in that comparison. It is not a chosen formation, and it is
not a mass density.

## Theorem — the two orbits are the same 24-point set

**Conclusion.** `|G| = 48` and `|O| = 24`. Let `A` be the `O`-orbit of
`(1, 1, 2)`. Then `|A| = 24`, and `A` equals the `G`-orbit. The matrix

```text
s = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
```

has determinant `-1` and fixes `(1, 1, 2)`. `A` is exactly the set of
integer vectors whose absolute values are `1`, `1`, and `2`. It is not a
chiral pair. The equality is not a selected law.

**Proof.** Every element of `G` is obtained once by placing a sign
`±1` in each row of a permutation matrix. There are `3! · 2^3 = 48`
such matrices, they are closed under multiplication, and each inverse is
the transpose. The determinant is `±1`, with `24` matrices on each side.
The determinant `+1` subset contains the identity and is closed under
multiplication and inverse, so it is a subgroup.

The stabilizer of `(1, 1, 2)` in `G` has two elements: the identity, and
`s`. The third coordinate is the only one of absolute value `2`, so every
stabilizer element fixes that axis and keeps its sign. The first two
coordinates are both `+1`, so neither sign may flip, and those two axes
may be swapped. The swap `s` is a transposition with positive signs, hence
determinant `-1`. Exactly one stabilizer element lies in `O`. Therefore
`|A| = |O| / 1 = 24`, while the `G`-orbit has size `|G| / 2 = 24`.

The same conclusion is the transport used for `(0, 1, 2)`. If an improper
`g` sends `(1, 1, 2)` to `v`, then `g s` has determinant `+1` and sends
`(1, 1, 2)` to `g · (s · (1, 1, 2)) = v`. Every improper image is already
in `A`, so the two orbits are equal. `A` is not the union of two proper
orbits.

The set of vectors with absolute values `1`, `1`, and `2` has `3 · 8 = 24`
elements: three axes for the entry of absolute value `2`, and an
independent sign on each coordinate. `G` preserves that absolute-value
pattern, and `(1, 1, 2)` lies in the set, so the `G`-orbit is contained in
it. The two sets have the same finite size, so they are equal.

Two proper images show that the repeated unit entry does not by itself
force an improper move. The even permutation

```text
[[0, 0, 1], [1, 0, 0], [0, 1, 0]]
```

lies in `O` and sends `(1, 1, 2)` to `(2, 1, 1)`. The proper matrix

```text
[[0, 1, 0], [1, 0, 0], [0, 0, -1]]
```

lies in `O` and sends `(1, 1, 2)` to `(1, 1, -2)`. The diagonal mirror
`diag(-1, 1, 1)`, which fixes `(0, 1, 2)`, sends this seed to
`(-1, 1, 2)`. That image is not the seed, and it is still in `A`. No
coordinate of a point of `A` is `0`, so `A` is not the orbit of
`(0, 1, 2)`.

No coefficient is read off the count. The integer `24` is the size of a
set of triples. It is not a mass density, a probability, or a rate.

## What this does not say

- It does not adopt the orbit equality as a physical law, a circulation,
  a flux, or a mass density.
- It does not add `s` to the symmetries supplied by the axioms. `s` is one
  comparison element, and it is improper.
- It does not say that every 24-point orbit is equal to its mirror orbit.
- It does not enumerate the orbit of `(1, 2, 2)`, a mixed alphabet, or a
  higher-rank bond space.
- It does not rerun the axis-role product, the value `kappa = 1/2`, or the
  path correlation `1/72` on the orbit of `(0, 1, 2)`.
- It does not rerun a corner-weight elimination, a shell census, a cap
  pencil, or a CHSH square.
- It does not choose a formation site, and it does not define a rate.

## No-Go Discipline Gate

Scoped claim: the proper cubic orbit of `(1, 1, 2)` has 24 points and
equals the orbit under all 48 signed permutation matrices. The improper
swap of the two unit axes fixes the seed. The orbit is not a chiral pair.
The equality is not a selected law. The orbit of `(1, 2, 2)` is not
enumerated.

N1. Five attacks on that scoped claim:

1. Let the repeated absolute value `1` cut the proper orbit to 12 points
   and leave a mirror twin. The swap `s` is improper and fixes the seed,
   so every improper image is already proper. The proper orbit has 24
   points, not 12. `ATTEMPTED`.
2. Let the mirror `diag(-1, 1, 1)` that fixes `(0, 1, 2)` be the witness
   here. It sends `(1, 1, 2)` to `(-1, 1, 2)`, which is not the seed.
   That image is still in the proper orbit. The fixing mirror is `s`.
   `ATTEMPTED`.
3. Let moving the entry `2` off its axis require an improper permutation.
   One even permutation in `O` sends `(1, 1, 2)` to `(2, 1, 1)`.
   `ATTEMPTED`.
4. Let changing the sign of the `2` require an improper matrix. One
   determinant `+1` matrix sends `(1, 1, 2)` to `(1, 1, -2)`. `ATTEMPTED`.
5. Let the equality be a selected interaction because the two orbits
   coincide. The theorem records a set equality and does not adopt it.
   `ATTEMPTED`.

N2. Only this one triple and the signed-permutation action are used. No
second output action is stated.

N3. The group `G`, the proper subset `O`, and the seed `(1, 1, 2)` are
written as the comparison already used for one other triple. No dynamics
clause is used. The three approved primitives `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive` are not
inputs.

N4. The order-blind factor on `(0, 1, 2)` is a different carrier. Dropping
its bond product, its `kappa`, and its path correlation leaves the orbit
equality intact: the 48 matrices, the mirror `s`, and the 24 vectors are
recomputed here. No count in that note is used as a mass. The corner-weight
family and the shell censuses are not inputs.

N5. The negative sentence is about one triple. The runner evaluates the
48 matrices, the stabilizer, and the absolute-value list. It does not
resolve a second orbit as an independent variable.

N6. This note does not say that a new axiom is required. It does not
select a coefficient. Source/action remains an open gate. The formation
rule remains downstream supplier content.

N7. Steelman, outside this triple: enumerate the orbit of `(1, 2, 2)`, a
mixed alphabet, or a higher-rank bond space, or call the integer `24` a
mass density. None of those is executed. The orbit of `(1, 2, 2)` stays
unenumerated. The corner-weight family stays stopped. The odd cap alphabet
stays stopped. The shell censuses are not reopened.

N8. This note does not reopen the `(0, 1, 2)` factor, the linear factor
`1 + kappa F`, the quadratic pencil, the shifted cap factor, the
729-shell census, the one-blank census, the binary-shell census, the
square-circulation census, the alternating sum, the four-weight
elimination, or the shared symbol pair.

## Review record

The open question was whether the proper orbit of `(1, 1, 2)` equals its
mirror orbit under the comparison already used for `(0, 1, 2)`. It does.
Both orbits have 24 points. The witness is the improper swap of the two
unit axes. The equality is not a selected law. The miss on `origin/main`
is real: no note there states this comparison. The orbit of `(1, 2, 2)`
was not part of the count.

Outstanding at landing: `(1, 2, 2)` stays unenumerated and is not the next
alphabet; the site and the rate stay unsupplied; independent audit has not
reviewed this note. No helper runner is declared.

The group orders, the mirror `s`, and the size `24` were fixed by the
enumeration above before the runner's expected comparisons. The author
re-ran two load-bearing mutations on scratch copies; each printed
`FAIL=1`, and the copies were not kept.

- Demanding that the proper orbit have 48 points fails one check.
- Demanding that the fixing swap have determinant `+1` fails one check.

## Runner

`scripts/one_one_two_proper_orbit_equals_mirror_orbit_2026_10_10.py`
builds the 48 signed permutation matrices and the 24 of determinant `+1`.
It checks that both sets are groups, that the proper orbit of `(1, 1, 2)`
has 24 points and equals the full orbit, that one improper mirror fixes
the seed and transports every improper image, that the orbit is the
absolute-value pattern `1, 1, 2`, that one proper cycle moves the `2` and
one proper matrix flips its sign, and that the stabilizer has order `2`
with only the identity proper. It emits no coefficient. It reads no
external scientific input. The cached result is `TOTAL: PASS=6 FAIL=0`.
