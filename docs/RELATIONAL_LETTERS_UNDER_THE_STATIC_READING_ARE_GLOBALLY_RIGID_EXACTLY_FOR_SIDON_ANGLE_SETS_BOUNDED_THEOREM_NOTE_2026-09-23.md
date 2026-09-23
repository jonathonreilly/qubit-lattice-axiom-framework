---
claim_id: relational_letters_under_the_static_reading_are_globally_rigid_exactly_for_sidon_angle_sets_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "With a fixed octant, Sidon angles and six distinct nonzero signed angles, the proof below makes core values a spiral on every cubic core of side at least two. For both (1,2,4) mod 7 and (1,2,5) mod 12, complete searches on core sides 2,3,4 give 12 normalized core spirals. The identification of Sidon with conditions (a),(c) is checked over all 494 triples for moduli 5 through 12 (252 Sidon). Full side-4 box searches reproduce the core counts.  Two non-Sidon additive-support contrasts have 48,384,3072 core records on those sizes, including only 12 spirals. These examples do not prove Sidon necessary for rigidity in every model, and do not enforce rejection of ambiguous inputs by the original unique-completion algorithm. Sweep-only counts on side-two cores are 336 and 24. On tori the seven-value case needs 7|L, and the twelve-value case needs 12|L; the listed direct finite searches agree. Permitting a sitewise octant gives 15024 side-two core records, including 48 spirals.  Complete spiral extensions have identical relative neighbourhood views and cannot yield a nonconstant rotation-invariant scalar role readout. This also applies to torus/infinite spirals and to sites whose entire neighbourhood lies inside a rigid core. It does not say every boundary neighbourhood of every finite static extension is identical. The theorem is sufficiency, not an if-and-only-if classification. Core-value rigidity leaves possible outer-neighbour freedoms. The supplied fixed octant transforms with the background; holding it fixed is not a rotation-covariant lattice law. Contrast counts refer to additive support, which can admit ambiguous stars. The torus proof and direct searches have the stated sizes; no ice measure or gravitational conclusion is imported."
upstream_dependencies:
  - minimal_axioms
  - relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_bounded_theorem_note_2026-09-22
  - relational_spiral_letters_with_finitely_many_values_seven_suffice_and_are_the_fewest_bounded_theorem_note_2026-09-23
runner: scripts/relational_letters_static_reading_globally_rigid_exactly_for_sidon_angle_sets_2026_09_23.py
---

# Sidon sufficiency for global rigidity of spiral core values

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

With a fixed octant, Sidon angles and six distinct nonzero signed angles, the proof below makes core values a spiral on every cubic core of side at least two. For both (1,2,4) mod 7 and (1,2,5) mod 12, complete searches on core sides 2,3,4 give 12 normalized core spirals. The identification of Sidon with conditions (a),(c) is checked over all 494 triples for moduli 5 through 12 (252 Sidon). Full side-4 box searches reproduce the core counts.

Two non-Sidon additive-support contrasts have 48,384,3072 core records on those sizes, including only 12 spirals. These examples do not prove Sidon necessary for rigidity in every model, and do not enforce rejection of ambiguous inputs by the original unique-completion algorithm. Sweep-only counts on side-two cores are 336 and 24. On tori the seven-value case needs 7|L, and the twelve-value case needs 12|L; the listed direct finite searches agree. Permitting a sitewise octant gives 15024 side-two core records, including 48 spirals.

Complete spiral extensions have identical relative neighbourhood views and cannot yield a nonconstant rotation-invariant scalar role readout. This also applies to torus/infinite spirals and to sites whose entire neighbourhood lies inside a rigid core. It does not say every boundary neighbourhood of every finite static extension is identical.

## Boundaries and non-claims

The theorem is sufficiency, not an if-and-only-if classification. Core-value rigidity leaves possible outer-neighbour freedoms. The supplied fixed octant transforms with the background; holding it fixed is not a rotation-covariant lattice law. Contrast counts refer to additive support, which can admit ambiguous stars. The torus proof and direct searches have the stated sizes; no ice measure or gravitational conclusion is imported.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Conditional mathematics of the declared relational record model"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the declared scope; test extensions separately"
conditional_surface_status: "The stated domain, rule, boundaries and finite checks only"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Conditional proof and exact finite witnesses; no retained grade asserted"
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



## Theorem 3 — Sidon identity and additive-support contrasts

- Sidon means all six sums θ_i + θ_j (i ≤ j) are distinct. For three
  distinct angles this is exactly (a), 2θ_i ≠ 2θ_j, together with (c),
  2θ_k ≠ θ_i + θ_j. The runner checks this over all 494 triples with
  m = 5 to 12.
- For the two declared non-Sidon contrasts, squares that are neither straight nor folded exist
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


## Corollary — Complete spiral neighbourhoods

For a complete spiral, translating by y rotates every value in a local
neighbourhood by the same angle theta·y. A rotation-invariant scalar
readout must therefore be constant across these neighbourhoods. The parity
vector is not constant. For the seven-value spiral even the absolute value
repeats at x and x+(1,1,1), since the signed sum is ±7 modulo 7, while all
three parity bits change. This argument concerns complete spirals or
neighbourhoods fully contained in the rigid core, not arbitrary outer faces.

## No-Go Discipline Gate and falsifiers

**N1 alternative routes / N3 hidden walls.** The negative claims use only the premises and domain above. Alternative
rules, boundary conditions, larger units, hidden shared data, physical
encodings and unstated parameter measures remain outside the result.
**N2 wall independence / N5 resolution.** The declared controls test which supplied conditions matter; a finite
search is exhaustive only where it completes below both record and work
caps. Witness prefixes and subsamples are labelled as such.

**N4 residuals / N6 partial closure.** Extending the explicit boundaries is
separate work; the result does not classify all possible repairs or routes.

**N7 strongest alternatives / N8 cross-result scope.** The positive controls
and companion results above remain available within their own hypotheses.
They do not inherit an exclusion from this note.

A counterexample meeting a theorem's stated hypotheses, a changed exact
count in an exhaustive search, or a failed declared control falsifies the
corresponding result. No other claim is graded, unlocked or audited here.

## Dependencies and provenance

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion result from PR #8691](RELATIONAL_FRAMES_IN_ONE_QUBIT_SPIRAL_RECORDS_UNDER_POSSIBILITY_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-09-22.md)
- [Companion result from PR #8729](RELATIONAL_SPIRAL_LETTERS_WITH_FINITELY_MANY_VALUES_SEVEN_SUFFICE_AND_ARE_THE_FEWEST_BOUNDED_THEOREM_NOTE_2026-09-23.md)

The original author narrative and review history are recoverable from
the originating PR. Historical author mutation reports are not a substitute
for the current landing review. No new axiom or retained audit grade is adopted.

## Verification

```bash
python3 scripts/relational_letters_static_reading_globally_rigid_exactly_for_sidon_angle_sets_2026_09_23.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/relational_letters_static_reading_globally_rigid_exactly_for_sidon_angle_sets_2026_09_23.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
