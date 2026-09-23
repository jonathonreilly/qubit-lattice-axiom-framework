---
claim_id: relational_letters_under_the_static_reading_are_globally_rigid_exactly_for_sidon_angle_sets_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Relational spiral letters under the static reading of open PR 8691: each core site is a covariant completion of its three back neighbours x - e_i and of its three forward neighbours x + e_i, a fixed pair of opposite octants. A completion reads a great circle from its inputs and returns a point on it, and completions across a core link share two distinct, non-antipodal values, so all core values lie on one great circle, where each completion is additive (the planar form of open PR 8729): at each core site the back differences and the forward differences are each a common-sign permutation of the angles. If the three angles form a Sidon set (the six sums theta_i + theta_j, i <= j, distinct) and the six signed angles are distinct, every static record is a spiral on its core, for every core of side at least 2: each elementary square is straight or folded, signs depend only on the level x_1 + x_2 + x_3, folds are excluded by induction on the level, and straight squares make each difference constant along its axis. Over every triple of distinct angle multiples modulo m = 5 to 12 the Sidon property is exactly conditions (a) and (c) of open PR 8729. Checked by complete search on cores of side 2, 3 and 4 for the seven letters (1, 2, 4) x 360/7 and for 30, 60, 150 degrees: exactly the 12 spirals with one core value fixed, each the unique completion at every core site, so the static records are exactly the spirals up to a global rotation. Two angle sets that break (c), (1, 3, 5) mod 12 and (1, 2, 3) mod 7, have 48, 384 and 3072 core records; with back neighbours only (the sweep reading) the Sidon sets also admit records that are not spirals. On a cubic torus every site is a core site, so a static record is one spiral that must wrap consistently: the seven letters have static records on the side-L torus exactly when 7 divides L (searched: none for L = 2 to 6, the 12 spirals for L = 7), the letters 30, 60, 150 degrees need 12 to divide L, and neither set has one on the tori of side 2 and 4 that carry the landed ice measure. Every core site of a static record sees the same differences to its neighbours, so a static relational record carries the frame but no role pattern: no covariant local readout distinguishes sites, and even with the global rotation fixed the seven letters give x and x + (1, 1, 1) the same value. The rigidity uses the reading's fixed octant, which supplies the orientation of each axis while the record supplies the angle assignment and sense: if each core site may use its own octant, the seven letters have 15024 records on the core of side 2, 48 of them spirals. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/relational_letters_static_reading_globally_rigid_exactly_for_sidon_angle_sets_2026_09_23.py
---

# Relational letters under the static reading are globally rigid, exactly for Sidon angle sets

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8691 left open whether every
stationary record of its relational frames is a spiral. Open PRs 8717 and
8724 showed that spirals are linearly rigid, and locally rigid in the full
nonlinear relations, under the static reading. This block proves global
rigidity under the static reading.

## Result up front

1. **Every static record is a spiral.** This holds for the seven letters
   (1, 2, 4) × 360/7 and for the letters 30°, 60°, 150°. Under the static
   reading, each core site is a covariant completion of its three back
   neighbours and of its three forward neighbours. Any record with that
   property is a spiral on its core, for every core of side at least 2,
   up to a global rotation of the sphere.

2. **The reason is additive.** Completions read a great circle from their
   inputs. Completions across a core link share two distinct,
   non-antipodal values, so all core values lie on one great circle. On
   that circle every completion is additive: at each core site, the back
   differences are a common-sign permutation of the angles, and so are
   the forward differences. The proof then runs in three steps:
   - If the angles form a **Sidon set** (the six sums θ_i + θ_j, i ≤ j,
     are distinct), every elementary square of links is either straight
     (opposite differences equal) or folded (opposite differences
     negated).
   - A fold at any level would give one site two equal forward
     differences, or one link two different values.
   - So every square is straight, and every difference is constant along
     its axis: the record is a spiral.

3. **Sidon is exactly the rule's own conditions.** Over every triple of
   distinct angle multiples modulo m = 5 to 12, the Sidon property holds
   exactly when conditions (a) and (c) of open PR 8729 hold: angles
   distinct mod 180°, and no angle the mean of the other two. The seven
   letters are the Fano difference set {1, 2, 4} mod 7.

4. **The search agrees.** A complete search covers every core of side
   2, 3 and 4. With one core value fixed, both Sidon sets have exactly 12
   static records, the spirals (six angle assignments times two senses).
   Each is the unique completion at every core site.

5. **Without Sidon, or without the forward completions, rigidity fails.**
   - (1, 3, 5) mod 12 and (1, 2, 3) mod 7 break (c). They have 48, 384
     and 3072 core records on cores of side 2, 3 and 4.
   - With back neighbours only (the sweep reading), the Sidon sets also
     admit records that are not spirals: 336 and 24 on the core of side
     2. This matches open PR 8717, which found the sweep flexible.

6. **On a torus the frame must wrap consistently.** On a cubic torus every site is a
   core site, so a static record is one spiral, and that spiral must
   wrap consistently around the torus.
   - The seven letters have static records on the side-L torus exactly
     when 7 divides L. The search finds none for L = 2 to 6, and exactly
     the 12 spirals for L = 7.
   - The letters 30°, 60°, 150° need 12 to divide L.
   - Neither set has a static record on the tori of side 2 or 4. Those
     tori carry the landed ice measure: 2 × 2 × 2 cells, or 4 × 4 × 4
     sites once links, plaquettes and cube sites are counted (open
     PR 8727).

7. **The record carries the frame and nothing positional.** Because a
   static record is one spiral, every core site sees the same differences
   to its six neighbours: one view, up to rotation. So no covariant local
   readout can tell sites apart, while the role pattern (the superlattice
   parity vector) takes 8 values.
   - Even with the global rotation fixed, values do not fix roles: for
     the seven letters, x and x + (1, 1, 1) always carry the same value,
     since 1 + 2 + 4 = 7.
   - Relational letters therefore supply the lattice frame, and the
     emulation of soldered rules that reads only directions.
   - They do not supply the role letters or the label readouts of open
     PRs 8676 and 8679, which use absolute coordinate labels. This
     narrows a sentence of open PR 8691.

8. **The rigidity uses the reading's octant.** The static reading of
   open PR 8691 takes back neighbours x − e_i and forward neighbours
   x + e_i: a fixed pair of opposite octants, which supplies the
   orientation of each axis. The record supplies the rest, the angle
   assignment and the sense.
   - If each core site may use its own octant, rigidity fails. The seven
     letters then have 15024 records on the core of side 2, of which 48
     are spirals (six assignments, eight sign patterns).
   - So the per-site-octant reading keeps the letters flexible, even
     though it is covariant under the lattice and local. Other covariant
     local readings are not searched here.

9. **What this means for the frame.** Under the static reading with its
   octant and these letters, the record fixes the rest of the lattice
   frame everywhere on the core, not just near a spiral. The frame
   source of the {alphabet, reading} set of downstream gravity (open
   PR 8648) is then exact for relational letters, given the octant, on
   open boxes and on tori whose side the letters divide.
   - Roles still come from fixed letters or are supplied. With relational
     letters alone, as under possibility covariance, that set needs the
     roles decision as well.
   - On the landed ice torus, the static route needs fixed letters or
     soldering.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "rigidity: whether every stationary record of the relational frames is a spiral (open PR 8691)"
source_of_blocker_text: open_pr_8691
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record in the assembly: under the static reading with its fixed octant, relational letters with Sidon angles are globally rigid and carry no role pattern; the sweep and the per-site-octant reading stay flexible"
conditional_surface_status: "static reading of open PR 8691 with its fixed octant; relational spiral letters with Sidon angles and six distinct signed angles; cores of side at least 2"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "a short additive proof, an identification checked over all small angle sets, and complete searches on declared cores"
```

## Premises and declared objects

- **Static reading** (open PR 8691). Each core site, one with all six
  neighbours in the box, is a covariant completion of its three back
  neighbours x − e_i. It is also a completion of its three forward
  neighbours x + e_i, with the orientation reversed. The back and forward
  octants are fixed by the reading; a contrast lets each site choose its
  own.
- **Completion.** The rule reads a great circle and its orientations from
  its three inputs. It returns the point that each input reaches by one of
  the three rotations, each angle used once and in one common sense.
- **Planar form** (open PR 8729). On one great circle, values are angles.
  A completion b of inputs w_i satisfies b − w_i = s θ_σ(i) for a
  permutation σ and a common sign s.
- **Angles.** The seven letters (1, 2, 4) × 360/7; 30°, 60°, 150°; and two
  contrast sets that break condition (c).
- **Search.** The core-only search fixes one core value (a global
  rotation) and leaves the values outside the core free. A full search
  on the side-4 box, face values included, is its cross-check.

## Prior art and what is new

- Open PR 8691: relational frames, the static reading, and rigidity as an
  open question.
- Open PR 8717: linear rigidity, and flexibility under the sweep.
- Open PR 8724: local rigidity in the full nonlinear relations.
- Open PR 8729: the planar reduction, conditions (a) to (c), seven letters.
- New here:
  - global rigidity under the static reading;
  - its exact condition, the Sidon property, which equals (a) and (c);
  - the contrast sets and the sweep contrast.

## Theorem 1 — One great circle

At a core site x, the back completion puts x and its back neighbours on
one great circle C_x^b, and the forward completion puts x and its forward
neighbours on C_x^f.

For a core link from y to y + e_i:
- C_y^f and C_{y+e_i}^b both contain the values at y and at y + e_i;
- these differ by one of the angles, so they are distinct and not
  antipodal;
- hence C_y^f = C_{y+e_i}^b.

Now take x with a core predecessor x − e_i and a core successor x + e_j,
j ≠ i:
- C_{x−e_i}^f contains x and x − e_i + e_j;
- C_{x+e_j}^b contains x and x + e_j − e_i;
- these are the same two points, which differ by a difference of two
  forward rotations with a common sense, so they are neither equal nor
  antipodal for the declared angles;
- so C_x^b = C_x^f.

On a core of side at least 2 these links connect everything. So every
core value lies on one great circle, and the planar form holds on the
core.

## Theorem 2 — Global rigidity for Sidon angles

Let the angles be Sidon, and let the six signed angles be distinct. Each
difference along a core link then has a well-defined sign and angle.

**Squares.** Take a square with corners y, y + e_i, y + e_j,
y + e_i + e_j in the core. Its differences are:
- a = d_i(y) and c = d_j(y), which are forward at y: same sign,
  different angles;
- b = d_j(y + e_i) and e = d_i(y + e_j), which are back at the far
  corner: same sign, different angles.

They satisfy a + b = c + e. There are two cases:
- If all four have the same sign, Sidon (applied to the angles, or to
  their negatives) gives {a, b} = {c, e}. Since a ≠ c, this means a = e
  and b = c: the square is **straight**.
- If b and e have the opposite sign to a and c, write b = −b′ and
  e = −e′, with b′ and e′ of the sign of a and c. Then a + e′ = c + b′,
  and Sidon with a ≠ c gives a = b′ and e′ = c. So b = −a and e = −c:
  the square is **folded**.

**Signs.** The far corner's back differences b and e have the forward
sign of y + e_i and of y + e_j. So the forward sign agrees across every
square's diagonal and depends only on the level t = x_1 + x_2 + x_3. A
square is folded exactly where the sign changes between levels t and
t + 1.

**No folds** (induction on the level):
- *Lowest level.* At the lowest core site, two squares share the shift
  axis i. Folds in both would give d_j(y + e_i) = −d_i(y) = d_k(y + e_i):
  two equal forward differences at one site, which is impossible.
- *Higher levels.* Let v be a core site at level t − 1 with v + (1, 1, 1)
  in the core, and set w = v + e_q and w' = v + e_s. Suppose the
  transition to level t + 1 were folded. The square (s, p) at w and the
  square (q, p) at w' share the far difference d_p(w + e_s). The folds
  would give d_p(w + e_s) = −d_s(w) = −d_q(w'). The square (s, q) at v is
  straight by induction, so d_s(w) = d_s(v) ≠ d_q(v) = d_q(w'). This is
  a contradiction.

  Such a v exists at every level t − 1 from 3 to 3(c − 1). So the
  induction covers every transition from 3 to 3c − 2, and the forward
  sign is constant.

**Constancy.** Every square is now straight, so d_i(y + e_j) = d_i(y)
whenever the square lies in the core. Along the axis itself, compare the
forward triples at y and y + e_i, each moved transversally to the bottom
of the core. Their j and k entries agree, so their i entries agree. Each
d_i is therefore constant, and the record is a spiral on the core.

## Theorem 3 — Exactness and contrasts

- Sidon means all six sums θ_i + θ_j (i ≤ j) are distinct. For three
  distinct angles this is exactly (a), 2θ_i ≠ 2θ_j, together with (c),
  2θ_k ≠ θ_i + θ_j. The runner checks this over all 494 triples with
  m = 5 to 12.
- Without Sidon, squares that are neither straight nor folded exist
  (16 each for both contrast sets). Those sets have 48, 384 and 3072 core
  records on cores of side 2, 3 and 4.

## Theorem 4 — Tori

On the cubic torus of side L every site is a core site.

For L ≥ 4:
- every 4 × 4 × 4 window embeds in the torus;
- by Theorem 2, the record is a spiral on each window's core;
- overlapping cores share their differences, so there is one spiral with
  constant differences d_i on the whole torus;
- going once around the torus gives L d_i ≡ 0 (mod m).

For the seven letters every d_i is invertible modulo 7, so 7 divides L.
For 30°, 60°, 150°, the axis that carries 30° needs 12 to divide L.

The runner searches the torus directly:
- seven letters, L = 2 to 7: no records except for L = 7, where there
  are exactly the 12 spirals with one value fixed;
- 30°, 60°, 150°, L = 2 to 4: no records.

## Corollary 5 — The frame without positions

A static record on a core is a spiral, so the differences from a core
site to its six neighbours are (±d_1, ±d_2, ±d_3) at every core site. The
runner checks one view per spiral at all 64 core sites of the side-6 box,
for all 12 spirals of both Sidon sets.

- A readout that commutes with rotations of the sphere depends only on
  that view up to rotation, so it is the same at every core site.
- The role pattern of the superlattice (the parity vector x mod 2, up to
  its 8 global phases; landed role-pattern note, open PR 8669) takes all
  8 values on the core.
- So the role pattern is not a covariant local readout of a static
  relational record.
- With the global rotation fixed, sites of different parity still share
  values. For the seven letters, (1, 1, 1) lies in the kernel of every
  spiral, since 1 + 2 + 4 ≡ 0 mod 7. For 30°, 60°, 150°, a kernel vector
  with an odd entry exists.

Coordinate letters differ: they are absolute labels c ∈ Z_4^3, and c mod
2 is the parity vector (open PR 8676).

## No-Go Discipline Gate

The negative content is the contrasts: sets that break (c), and the sweep
reading. Both are scoped to the declared cores.

- **N1 alternative routes.** Records beyond the core, and angle sets
  whose six signed angles coincide, are outside this block.
- **N2 wall independence.** Additive proof; complete searches; a
  cross-check that includes face values.
- **N3 hidden walls.** The static reading is a declared reading, and its
  fixed octant is supplied structure: it gives each axis an orientation.
  The contrast with a per-site octant is checked (15024 records, 48
  spirals).
- **N4 residual matching.** Under the sweep reading the residual is
  flexibility (open PR 8717).
- **N5 rhetoric audit.** "Globally rigid" means on the whole core of any
  box with core side at least 2.
- **N6 partial-closure paths.** Other angle sets satisfying (a) and (c);
  larger alphabets; readings between the fixed and the per-site octant,
  for example one orientation for each lattice line.
- **N7 steelman.** For flexibility: the sweep reading and non-Sidon sets
  are flexible. Against: the static reading with the declared letters is
  rigid. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8648, 8691, 8717, 8724 and 8729 are
  cited.

## Falsifiers

Any of the following falsifies the theorems:
- a static record on a core of side at least 2 that is not a spiral, for
  Sidon angles with six distinct signed angles;
- a triple for which the Sidon property and (a) with (c) disagree;
- a square that is neither straight nor folded for a Sidon set.

## Boundaries and non-claims

- The static reading, the declared completions, cores of side at least 2.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PRs 8648, 8691, 8717, 8724 and 8729 and the landed
possibility-covariance note are cited. No audit grade, no new axiom, no
new primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the core-only search is cross-checked by a full search that includes
    face values;
  - the identification is checked over all small triples;
  - the proof's plaquette lemma is checked by enumeration;
  - uniqueness is checked with the completion rule of open PR 8729.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| Sidon test without repeated sums | sums over i < j only | caught (1 FAIL) |
| condition (c) dropped | condition (c) returns true | caught (1 FAIL) |
| completions with independent signs | signs chosen per axis | caught (8 FAILs) |
| static search without forward completions | forward completions dropped | caught (3 FAILs) |
| spiral test ignores one axis | one axis ignored | caught (4 FAILs) |
| folded squares classed as straight | folded classed as straight | caught (1 FAIL) |
| completions in one sense only | one rotation sense | caught (1 FAIL) |
| full search reads one incoming triple | one incoming triple | caught (1 FAIL) |
| identification over one modulus | m = 5 only | caught (1 FAIL) |
| no value fixed in any search | no value fixed | caught (4 FAILs) |
| sweep contrast with forward completions | forward completions added | caught (1 FAIL) |
| torus without wrap-around | modulus dropped | caught (2 FAILs) |
| torus search with back completions only | forward completions dropped | caught (2 FAILs) |
| views taken as absolute values | absolute values | caught (1 FAIL) |
| core restricted to odd coordinates | odd coordinates only | caught (1 FAIL) |
| kernel search over the zero vector only | zero vector only | caught (1 FAIL) |
| octant contrast with one octant | one octant | caught (1 FAIL) |
| octant contrast with back completions only | back completions only | caught (1 FAIL) |

  18 of 18 are caught.

- **Vacuity guard:** record counts, spiral counts, square classes and
  triple counts are printed.
- **Budget:** 9 checks, stdout 3049 characters (ceiling 6000), about
  47 s (ceiling 900 s), exact modular arithmetic. Every search has a
  record cap and a step cap, and all searches share a cap on comparisons
  with a triple. Each cap is about three times what the true run uses,
  and a search fails its check when any cap binds.

## Verification

```bash
python3 scripts/relational_letters_static_reading_globally_rigid_exactly_for_sidon_angle_sets_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=9 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/relational_letters_static_reading_globally_rigid_exactly_for_sidon_angle_sets_2026_09_23.txt`.
