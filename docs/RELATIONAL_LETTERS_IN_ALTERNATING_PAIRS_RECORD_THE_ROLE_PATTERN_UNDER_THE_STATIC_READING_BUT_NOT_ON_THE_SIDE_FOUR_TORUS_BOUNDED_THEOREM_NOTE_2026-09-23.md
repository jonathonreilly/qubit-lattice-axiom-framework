---
claim_id: relational_letters_in_alternating_pairs_record_the_role_pattern_under_the_static_reading_but_not_on_the_side_four_torus_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "For the declared planar fixed-octant pair rule, decoding and conditions (D),(E) force alternating spiral core values. For m=16 pairs (1,7),(2,10),(3,5), all 24 allowed squares are straight, (U) holds on all 96 stars, and core sides 2,3,4 each have exactly 96 records with unique face completions. The compatible torus sizes satisfy 8|L; direct searches cover L=2 through 8.  All 96 side-eight records have a common pair frame and parity readout up to one of eight global phases; per-record role weights are 64,192,192,64. Exhaustive site conditionals are singletons. A mod-13 control has 24 shared stars. Any decodable pair set wrapping on side four must have all pair sums equal to a half turn, which violates (U); all 240 tested sets through modulus 24 agree. The m=20 contrast has 96 records with exactly two antipodal centre values, and the parity-class shift preserves records. Without complementary types it has 2592 records, 2496 missing the canonical role readout; with sitewise senses it has 9216, including the original 96 spirals. The supplied global octant selects forward directions. The model is planar residue arithmetic; extending it to arbitrary sphere inputs or coupling it to an ice measure requires separate arguments. The role readout is parity up to a global phase, not an absolute site label. No gravity parameter set or physical assembly requirement is established."
upstream_dependencies:
  - minimal_axioms
  - relational_spiral_letters_with_finitely_many_values_seven_suffice_and_are_the_fewest_bounded_theorem_note_2026-09-23
  - relational_letters_under_the_static_reading_are_globally_rigid_exactly_for_sidon_angle_sets_bounded_theorem_note_2026-09-23
runner: scripts/relational_letters_in_alternating_pairs_record_the_role_pattern_under_the_static_reading_2026_09_23.py
---

# Alternating pair records and the side-four antipodal obstruction

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

For the declared planar fixed-octant pair rule, decoding and conditions (D),(E) force alternating spiral core values. For m=16 pairs (1,7),(2,10),(3,5), all 24 allowed squares are straight, (U) holds on all 96 stars, and core sides 2,3,4 each have exactly 96 records with unique face completions. The compatible torus sizes satisfy 8|L; direct searches cover L=2 through 8.

All 96 side-eight records have a common pair frame and parity readout up to one of eight global phases; per-record role weights are 64,192,192,64. Exhaustive site conditionals are singletons. A mod-13 control has 24 shared stars. Any decodable pair set wrapping on side four must have all pair sums equal to a half turn, which violates (U); all 240 tested sets through modulus 24 agree. The m=20 contrast has 96 records with exactly two antipodal centre values, and the parity-class shift preserves records. Without complementary types it has 2592 records, 2496 missing the canonical role readout; with sitewise senses it has 9216, including the original 96 spirals.

## Boundaries and non-claims

The supplied global octant selects forward directions. The model is planar residue arithmetic; extending it to arbitrary sphere inputs or coupling it to an ice measure requires separate arguments. The role readout is parity up to a global phase, not an absolute site label. No gravity parameter set or physical assembly requirement is established.

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

Write B_i=a(x)-a(x-e_i), F_i=a(x+e_i)-a(x). The pair rule requires
all six differences to have one common decoded sense, the B/F pair on
axis i to use complementary types of one pair, and three distinct pairs
across the axes. (D) says within-pair differences are distinct up to sign
across pairs. (E) excludes a within-pair difference equalling any
signed difference between angles in the other two pairs. (U) excludes a
nonzero centre shift preserving the same six neighbour values.

- **Static reading** (open PR 8691): each core site, one with all six
  neighbours in the window, satisfies the rule with its three back
  neighbours x − e_i and its three forward neighbours x + e_i. The octant
  is fixed by the reading; a contrast lets each site choose its own.
- **Planar form** (open PR 8729): values on one great circle, written as
  residues mod m. The one-great-circle step of open PR 8743 uses only two
  facts: values across a link are distinct and not antipodal, and two
  forward rotations from different pairs never differ by 0 or 180
  degrees. The runner checks both for the declared letters. This note does
  not restate that step for the pair rule.
- **Decoding:** the twelve signed angles ±alpha_j, ±beta_j are distinct
  and nonzero, so each difference has a sense, a pair and a type.
- **Letters:** m = 16, pairs (1, 7), (2, 10), (3, 5). The side-4 contrast
  uses m = 20, pairs (1, 9), (2, 8), (4, 6).
- **Role pattern:** the parity vector x mod 2, up to its 8 global phases
  (the landed role-pattern note; open PR 8669).



## Theorem 1 — Alternating spirals

Assume decoding, (D) and (E), and a core of side at least 2.

**Links.** On a core link from y to y + e_i, the difference F_i(y) is also
B_i(y + e_i). Decoding it gives one sense, one pair and one type. So y and
y + e_i share the sense and the pair of line i, and the type of F_i(y) is
the back type at y + e_i. The rule then makes the forward type at y + e_i
the other one. Along every line of core links, the pair is constant and
the forward types alternate. The core is connected, so the sense is
constant.

**Squares.** Take a square y, y + e_i, y + e_j, y + e_i + e_j in the core.
Let A and B be the pairs of lines i and j at y, and C the third pair.
Write:
- a = F_i(y) and c = F_j(y);
- b = F_j(y + e_i), with pair X, where X ≠ A since line i at y + e_i
  carries A;
- e = F_i(y + e_j), with pair Y, where Y ≠ B since line j at y + e_j
  carries B.

At the far corner, b and e are back differences on lines j and i, so
X ≠ Y. With the common sense removed, a + b = c + e. Write g_P(t) for the
angle of pair P with type t, and p, q, r, u for the types of a, b, c, e.
The cases are:
- **X = B, Y = A.** Then g_A(p) − g_A(u) = g_B(r) − g_B(q).
  - If p ≠ u, the left side is ± the within-pair difference of A, which
    is not 0. The right side is 0, or ± that of B, which (D) excludes.
  - So p = u, hence q = r: the square is **straight**.
- **X = C, Y = A.** Then g_A(p) − g_A(u) = g_B(r) − g_C(q).
  - If p = u, the right side is zero, which is impossible for different
    pairs.
  - If p ≠ u, a within-pair difference of A equals a difference between
    B and C, which (E) excludes.
- **X = B, Y = C.** This case is symmetric: a within-pair difference of B
  would equal a difference between A and C, which (E) excludes.

So every core square is straight: b = c and e = a, with the same pairs
and types.

**Constancy.** Straight squares carry each line's pair and type unchanged
across the transverse directions, and every core link lies in a core
square. So:
- each lattice axis i carries one pair on the whole core;
- the type of F_i(x) is phi_i + x_i mod 2.

The record is an alternating spiral. Conversely every alternating spiral
satisfies the rule. With one core value fixed there are 6 frames, 2 senses
and 8 phases: 96 records.

The runner enumerates every square configuration for the letters: 24
solutions, all straight. A complete search on cores of side 2, 3 and 4
finds exactly the 96 spirals, each with one completion on the faces.



## Theorem 2 — Roles and the nearest-neighbour form

**Readout.** At a core site, decode the three forward differences. Line i
gives its pair sigma(i) and the type phi_i + x_i mod 2. Indexed by pairs,
the types form rho(x): the parity vector x mod 2 in the pair frame, plus
one global phase phi.
- A shift of all values leaves the differences unchanged.
- A reflection negates them, which flips the sense only.
- So rho is unchanged by every rotation of the circle.

The runner reads rho at all 512 sites of every side-8 record:
- one frame per record;
- one phase per record, and all 8 phases occur;
- role weights (the number of odd entries) 64, 192, 192 and 64 per record,
  that is the vertex, link, plaquette and cube classes of the superlattice.

**(U).** Take an allowed star and move its centre by d ≠ 0 with the six
neighbours fixed. (U) asks that the new star is never allowed. For the
declared letters the runner tests all 96 stars and all 15 shifts, and
finds none. So every site is a function of its six neighbours. On every
side-8 record the rule admits exactly one value at every site. The test's
positive control is a decodable set that fails (U): m = 13 with pairs
(1, 2), (3, 4), (7, 8) has 24 such stars.



## Theorem 3 — Tori, and the side-4 obstruction

On the side-L torus every site is a core site. By Theorem 1 (L ≥ 3) a
record is one alternating spiral, and it must wrap. Each line has even
length L, and (L/2)(alpha_j + beta_j) = 0 mod m for its pair. Every pair
is carried by some axis, so this holds for all three pairs.
- For the declared letters the pair sums are 8, 12 and 8 (mod 16), so
  8 | L.
- The search finds no records for L = 2 to 7, and exactly the 96 spirals
  for L = 8.

**Side 4.** Wrapping on the side-4 torus needs 2(alpha_j + beta_j) = 0
mod m. A decodable pair cannot sum to 0, so m is even and every pair sums
to m/2 (180 degrees). Now move the centre of an allowed star by m/2:
- B_i + m/2 = s g(t_i) + m/2 = −s g(1 − t_i), since g(t) + g(1 − t) = m/2
  and −m/2 = m/2 mod m;
- likewise F_i − m/2 = −s g(t_i).

The moved star has the opposite sense, the same pairs and swapped types,
so it is allowed. Two allowed stars share their six neighbours, and (U)
fails. Globally, adding m/2 on the odd parity class moves every link
difference by m/2. So it maps each record to another record with the same
values on the even class.

The runner checks:
- all 240 decodable pair sets with m up to 24 that wrap on the side-4
  torus: all fail (U);
- for m = 20, pairs (1, 9), (2, 8), (4, 6): (D) and (E) hold, and the
  side-4 records are exactly the 96 spirals;
- in those records every site admits exactly its value and its antipode
  given its neighbours;
- the parity-class shift maps records to records.



## Contrasts

The contrasts use the side-4 letters:
- **Without complementary types:**
  - 2592 torus records, from 12 frames and senses times 6^3 orders of two
    and two angles per line;
  - the readout misses the role pattern on all but the 96 spirals.
- **With one octant per site** (a sense per line): 9216 records, of which
  96 are spirals. Rigidity uses the reading's global octant.


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
- [Companion result from PR #8729](RELATIONAL_SPIRAL_LETTERS_WITH_FINITELY_MANY_VALUES_SEVEN_SUFFICE_AND_ARE_THE_FEWEST_BOUNDED_THEOREM_NOTE_2026-09-23.md)
- [Companion result from PR #8743](RELATIONAL_LETTERS_UNDER_THE_STATIC_READING_ARE_GLOBALLY_RIGID_EXACTLY_FOR_SIDON_ANGLE_SETS_BOUNDED_THEOREM_NOTE_2026-09-23.md)

The original author narrative and review history are recoverable from
the originating PR. Historical author mutation reports are not a substitute
for the current landing review. No new axiom or retained audit grade is adopted.

## Verification

```bash
python3 scripts/relational_letters_in_alternating_pairs_record_the_role_pattern_under_the_static_reading_2026_09_23.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/relational_letters_in_alternating_pairs_record_the_role_pattern_under_the_static_reading_2026_09_23.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
