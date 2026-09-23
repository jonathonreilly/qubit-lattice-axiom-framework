---
claim_id: relational_spiral_letters_with_finitely_many_values_seven_suffice_and_are_the_fewest_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The rule of open PR 8691 under possibility covariance (great circle from two back-neighbour values, all six angle assignments and both orientations, unique surviving point) with spiral records b(x) = R_z(theta . x) b0. The output is unique when (a) the angles are distinct modulo 180 degrees, (b) no 3-cycle shifts every angle by the same amount, and (c) no angle is the mean of the other two modulo 180 degrees. The angles (30, 60, 150) degrees meet all three; their spiral takes 12 values in Q(sqrt 3); on the 4-box every site with three back-neighbours is the rule's unique output (exact), the rule commutes with a quarter turn of the sphere, and each core site reads its six bond directions from the six distinct signed angles. The angles (30, 90, 150) break (c), and the rule then has a second output. A spiral with m values needs six distinct nonzero signed angles among the multiples of 360/m, so m >= 7; up to m = 12 a valid triple exists exactly for m = 7, 9, 10, 11, 12. For spiral inputs every value lies on one great circle and the rule's normal is the axis, so each fit is a congruence of angle multiples modulo m; this planar reduction reproduces the exact Q(sqrt 3) rule at all 27 sites of the twelve-value box, and with it the angles (1, 2, 4) x 360/7 give a seven-value spiral that is the rule's unique output at all 64 sites of a 5-box, with the frame reading: seven values suffice and no spiral does with fewer. First formations are unaffected (open PR 8691). No reading, rule, alphabet or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/relational_spiral_letters_with_finitely_many_values_seven_suffice_2026_09_23.py
---

# Relational spiral letters with finitely many values: seven suffice, and no spiral does with fewer

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8691 built relational letters under
possibility covariance: spiral records whose neighbours differ by
rotations through three Pythagorean angles. Those spirals take infinitely
many values, and the PR left open whether finitely many possibilities
suffice. This block answers yes: seven suffice, and no spiral does with
fewer.

## Result up front

1. **When the rule's output is unique.** The rule reads a great circle
   from its back-neighbours' values. It tries all six assignments of the
   three angles and both orientations, and keeps the points that fit. For
   a spiral, a second fit appears exactly when one of three coincidences
   occurs:
   - two angles agree modulo 180 degrees;
   - a 3-cycle shifts every angle by the same amount;
   - one angle is the mean of the other two modulo 180 degrees.

   Otherwise the output is unique.

2. **Twelve values suffice.** The angles (30, 60, 150) degrees avoid all
   three. Their spiral lives in Q(√3) and takes the twelve multiples of 30
   degrees on one great circle. The runner checks the following exactly:
   - on the 4-box every site with three back-neighbours is the rule's
     unique output;
   - the rule commutes with a quarter turn of the sphere;
   - each core site reads its six bond directions from the six distinct
     signed angles.

3. **The conditions matter.** The angles (30, 90, 150) have
   30 + 150 = 2 × 90, and the rule then has a second output.

4. **Seven suffice, and fewer cannot.** A spiral with m values needs six
   distinct nonzero signed angles among the multiples of 360/m, so
   m ≥ 7. Up to 12, valid triples exist exactly for m = 7, 9, 10, 11 and
   12.

   For spiral inputs every value lies on one great circle, and the rule's
   normal is the axis. So each fit is a congruence of angle multiples
   modulo m. This planar reduction reproduces the exact Q(√3) rule at all
   27 sites of the twelve-value box. With it, the angles (1, 2, 4) × 360/7
   give a seven-value spiral that is the rule's unique output at all 64
   sites of a 5-box, with the frame reading.

5. **What this means for relational frames.** Under possibility
   covariance one qubit can carry the lattice frame with a finite
   relational alphabet. The twelve points are defined only relative to
   one value and one axis, so no possibility is privileged. First
   formations still miss it (open PR 8691). Frames held by the static
   reading are locally rigid (open PR 8724), and so are those on the
   lattice (open PR 8717).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "whether finitely many possibilities suffice for relational letters (open PR 8691)"
source_of_blocker_text: open_pr_8691
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record on the relational-letter branch: a seven-value relational alphabet works, and no spiral works with fewer"
conditional_surface_status: "possibility covariance and the unsoldered reading as in open PR 8691; the declared rule, angles and box"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "exact computation in Q(sqrt 3), a short uniqueness argument over assignments and orientations, and a counting bound"
```

## Premises and declared objects

- **Open PR 8691's rule.** From back-neighbour values w_0, w_1, w_2 it
  reads the great circle with normal w_0 × w_1, normalised. It then tries
  every assignment σ of the angles and both orientations o. A point b is
  kept when w_i = R_{o n}(-θ_σ(i)) b for all i. The rule outputs the
  unique kept point, and records nothing otherwise.
- **Spiral records.** b(x) = R_z(θ . x) b0 with b0 = (1, 0, 0).
- **Exact arithmetic in Q(√3).** Pairs a + b√3 of Fractions. The cosines
  and sines of multiples of 30 degrees lie in this field, and so does
  every normal the rule needs here.

## Prior art and what is new

- Open PR 8691: the rule, Pythagorean spirals, the frame reading, first
  formations, and the question of finitely many values.
- Open PRs 8717 and 8724: rigidity of spiral frames.
- New here:
  - the uniqueness conditions;
  - a twelve-value spiral verified exactly in Q(√3);
  - the planar reduction and a seven-value spiral;
  - the counting bound m ≥ 7.

## Theorem 1 — Uniqueness

For a spiral, the three back-neighbours are rotations of b by -θ_i about
one axis. Another fit with assignment σ and the same orientation needs
θ_σ(i) - θ_i to be one constant. For a transposition this forces two
equal angles. For a 3-cycle it forces equal shifts: condition (b).

With the orientation reversed, the fit needs θ_i + θ_σ(i) to be one
constant:
- for the identity, two angles agree modulo 180 degrees (a);
- for a transposition, one angle is the mean of the other two (c);
- for a 3-cycle, two angles are equal.

The runner checks uniqueness directly at every site of the 4-box.

## Theorem 2 — Finite alphabets

A spiral whose angles are multiples of 360/m takes at most m values. The
frame reading needs six distinct signed angles. These are nonzero
residues modulo m closed under negation, so m - 1 ≥ 6. The runner lists
the m up to 12 with a valid triple.

## Theorem 3 — The planar reduction

For spiral inputs, w_0 and w_1 are distinct and not antipodal, by
condition (a). So the normal w_0 × w_1 is ±z, and every rotation the
rule tries is a rotation of the equator by a multiple of 360/m. A
candidate b = R(s θ_σ(0)) w_0 fits exactly when
angle(w_i) ≡ angle(b) - s θ_σ(i) (mod m) for all i, with s = ±1. The
runner checks that this reduction gives the same unique output as the
exact Q(√3) rule at all 27 sites of the twelve-value box. It then
applies the reduction to (1, 2, 4) × 360/7 on a 5-box: one output at
each of the 64 sites, seven values, and six distinct signed angles.

## No-Go Discipline Gate

The negative content is scoped: spiral records, the rule of open
PR 8691, and the declared conditions.

- **N1 alternative routes.** The following are outside this block:
  - non-spiral finite records;
  - other rules;
  - larger boxes.
- **N2 wall independence.** Exact field arithmetic and a counting
  argument.
- **N3 hidden walls.** The uniqueness conditions are for spiral inputs.
- **N4 residual matching.** The relational branch's residual is first
  formations (open PR 8691).
- **N5 rhetoric audit.** "Suffice" means checked on the declared boxes:
  twelve values in exact field arithmetic, seven by the planar reduction.
- **N6 partial-closure paths.** Non-spiral finite alphabets.
- **N7 steelman.** For finite relational letters: seven and twelve work,
  with rigidity from open PRs 8717 and 8724. Against them: first
  formations still miss them. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8691, 8717 and 8724 are cited.

## Falsifiers

Any of the following falsifies the theorems:
- a second rule output on the twelve-value spiral at a box site;
- a valid triple for m ≤ 6;
- a unique output for (30, 90, 150).

## Boundaries and non-claims

- Spiral records, the declared rule, and the 4-box.
- The seven-value case rests on the planar reduction, which is checked
  against the exact rule at twelve values.
- No reading, rule, alphabet or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PRs 8691, 8717 and 8724 and the landed possibility-covariance note
are cited. Field arithmetic in Q(√3) and the Rodrigues formula are
standard. No audit grade, no new axiom, no new primitive, no new
comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the uniqueness conditions are derived by hand and checked by brute
    force over assignments and orientations at every box site;
  - the contrast triple shows the conditions are needed.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutant | change | outcome |
|---|---|---|
| field product drops the 3 | 3 b d to b d | caught (4 FAIL) |
| one orientation only | both orientations to one | caught (4 FAIL) |
| identity assignment only | six assignments to one | caught (1 FAIL) |
| good angles replaced by the bad triple | (30, 60, 150) to (30, 90, 150) | caught (4 FAIL) |
| third condition dropped | mean test removed | caught (1 FAIL) |
| sine of 30 degrees wrong | 1/2 to sqrt(3)/2 | caught (4 FAIL) |
| quarter turn not a rotation | a reflection instead | caught (1 FAIL) |
| signed-angle distinctness dropped | test removed | caught (1 FAIL) |
| seven-value angles break the mean condition | (1, 2, 4) to (1, 2, 3) | caught (1 FAIL) |
| planar fit with the wrong sign | minus to plus | caught (1 FAIL) |
| twelve-value comparison always agrees | comparison returns true | caught (1 FAIL) |

11 of 11 caught. Three first misses were repaired:
- the covariance check now verifies that the map is a proper rotation
  (the rule is also covariant under reflections, since it tries both
  orientations);
- the counting check now tests that a triple containing an angle and
  its negative is rejected;
- the planar-reduction comparison now has a negative control.

A mutant letting zero angles into the count was dropped as equivalent,
since the signed-angle test already excludes them.

- **Vacuity guard:** site counts, value counts and the list of valid m
  are printed.
- **Budget:** 6 checks, stdout 1613 characters (ceiling 6000), under a
  second (ceiling 900 s), exact arithmetic in Q(√3).

## Verification

```bash
python3 scripts/relational_spiral_letters_with_finitely_many_values_seven_suffice_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/relational_spiral_letters_with_finitely_many_values_seven_suffice_2026_09_23.txt`.
