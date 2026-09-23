---
claim_id: relational_letters_in_alternating_pairs_record_the_role_pattern_under_the_static_reading_but_not_on_the_side_four_torus_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Relational letters with six angles in three pairs (alpha_j, beta_j), in the planar form of open PR 8729 (values are residues mod m), under the static reading of open PR 8691 with its global octant. One fixed nearest-neighbour rule, the pair rule: at a core site the six differences to its neighbours are signed angles with one common sense, the two neighbours on one lattice line use the two angles of one pair (complementary types), and the three lines use the three pairs. If the twelve signed angles are distinct and nonzero and two conditions hold, (D) within-pair differences distinct up to sign across pairs and (E) no within-pair difference equal to a difference between angles of the other two pairs, then every static record on a core of side at least 2 is an alternating spiral: each lattice axis carries one pair, and along it the steps alternate between the pair's two angles. The proof: link differences carry the sense, the pair and alternating types; every square of core links is straight by (D) and (E). With one core value fixed there are exactly 96 records (6 frames, 2 senses, 8 phases), checked by complete search on cores of side 2, 3 and 4 for the letters m = 16, pairs (1, 7), (2, 10), (3, 5). Each site reads from its forward differences the frame and its parity vector x mod 2 in the pair frame, up to one global phase: the role pattern, a covariant local readout that all 8 phases realise. Condition (U), that no two allowed stars share their six neighbours, holds for these letters, so every site is a function of its six neighbours. On the side-L torus a record is one alternating spiral that wraps, which for these letters needs 8 | L (searched: none for L = 2 to 7, the 96 spirals for L = 8). The landed ice torus has side 4. There, wrapping needs every pair to sum to 180 degrees, and then (U) fails: moving a site by 180 degrees swaps its sense and types and keeps its neighbours, and shifting one parity class by 180 degrees maps records to records. All 240 decoding pair sets with moduli up to 24 that wrap on the side-4 torus fail (U); for m = 20, pairs (1, 9), (2, 8), (4, 6), the side-4 records are exactly the 96 spirals, but every site admits its antipode given its neighbours. Contrasts on those side-4 letters: without complementary types there are 2592 records and the readout misses the role pattern on all but the 96 spirals; with one octant per site there are 9216 records, 96 of them spirals. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/relational_letters_in_alternating_pairs_record_the_role_pattern_under_the_static_reading_2026_09_23.py
---

# Relational letters in alternating pairs record the role pattern under the static reading, but not on the side-4 torus

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8743 proved that relational spiral
letters under the static reading are globally rigid for Sidon angles, and
that a rigid record gives every site the same view. So it carries the
lattice frame but no role pattern. The assembly (open PR 8648) therefore
supplies roles whenever the letters are relational, as under possibility
covariance. This block asks whether a relational record can carry the
role pattern.

## Result up front

1. **Letters in alternating pairs.** Take six angles in three pairs
   (alpha_j, beta_j). At a core site the pair rule asks:
   - the six differences to the neighbours are signed angles with one
     common sense;
   - the two neighbours on one lattice line use the two angles of one
     pair, one each (complementary types);
   - the three lines use the three pairs.

   It is one fixed nearest-neighbour rule. It depends only on differences,
   so it commutes with every rotation of the circle, and it uses the
   reading's octant to tell back from forward. The letters here are
   m = 16 with pairs (1, 7), (2, 10) and (3, 5): steps of 22.5 degrees,
   with pair sums of 180, 270 and 180 degrees.

2. **The records are alternating spirals.** Every static record on a core
   of side at least 2 is an alternating spiral:
   - each lattice axis carries one pair;
   - along the axis, the steps alternate between the pair's two angles.

   The proof needs the twelve signed angles to be distinct and two
   conditions:
   - **(D)** the within-pair differences are distinct up to sign across
     pairs;
   - **(E)** no within-pair difference equals a difference between angles
     of the other two pairs.

   With one core value fixed there are exactly 96 records: 6 frames, 2
   senses and 8 phases. A complete search on cores of side 2, 3 and 4 finds
   exactly these.

3. **Each site reads its role.** The forward differences at a site decode
   to a pair and a type on each line.
   - The pairs give the frame, the same at every site.
   - The types give the parity vector x mod 2 in the pair frame, up to one
     global phase: the role pattern of the superlattice. All 8 phases occur.
   - A rotation of the circle, a shift or a reflection, leaves every pair
     and type unchanged. So the readout is a covariant local readout.

   The role is not a record value here either. It is read from the
   differences to the neighbours.

4. **Each site is a function of its neighbours.** Condition (U) says that
   no two allowed stars share their six neighbours, and it holds for these
   letters. So each site value is fixed by its six neighbours, which is the
   form the static reading asks for.

5. **Tori of side divisible by 8.** On a torus every site is a core site,
   so a record is one alternating spiral that wraps. Each line must have
   even length L, with (L/2)(alpha_j + beta_j) = 0 mod m for its pair.
   - For these letters that means 8 | L.
   - The search finds no records for L = 2 to 7, and exactly the 96
     spirals for L = 8.

6. **Not on the landed ice torus.** The landed ice torus has side 4. A
   record wraps there only if every pair sums to 180 degrees, since a
   decodable pair cannot sum to 0. Then (U) fails:
   - moving the centre of an allowed star by 180 degrees swaps its sense and
     both types on every line, and keeps its six neighbours;
   - shifting one parity class of a record by 180 degrees gives another
     record.

   So on the side-4 torus a site is fixed by its neighbours only up to its
   antipode, and the static reading's nearest-neighbour form fails.
   - All 240 decodable pair sets with moduli up to 24 that wrap on the
     side-4 torus fail (U).
   - For m = 20 with pairs (1, 9), (2, 8), (4, 6), conditions (D) and (E)
     hold, and the side-4 records are exactly the 96 spirals. Every site
     still admits its antipode given its neighbours.

7. **Contrasts** on those side-4 letters:
   - **Without complementary types** there are 2592 records: in each line
     the angles may come in any order with two of each. The readout misses
     the role pattern on all but the 96 spirals.
   - **With one octant per site** (a sense per line) there are 9216
     records, of which 96 are spirals. Rigidity uses the reading's global
     octant, as it does for single-angle letters (open PR 8744).

8. **What this means for roles.** A static relational record can carry the
   role pattern after all: letters in alternating pairs record it, with
   each site a function of its neighbours.
   - On open boxes, and on tori whose side 8 divides for these letters, the
     roles decision can be replaced by the alphabet and the reading.
   - Under possibility covariance, the assembly's one unsoldered set
     {alphabet, reading, roles} would then become {alphabet, reading}, the
     same set that fixed letters need.
   - On the landed ice torus of side 4, neither kind of relational letter
     works. The single-angle letters of open PR 8743 do not wrap there,
     and pair letters fail (U). With these two kinds of relational letter,
     the static route there still needs fixed letters or soldering, with
     roles read from the fixed letters or supplied. Open PR 8752 gives
     relational letters in four-angle cycles that do work on this torus.
   - The static ice records of open PR 8679 were checked on the side-4
     torus; on the side-8 torus they are not checked here.

## Machine status and trace

- **Runner:**
  `scripts/relational_letters_in_alternating_pairs_record_the_role_pattern_under_the_static_reading_2026_09_23.py`
- **Result:** `TOTAL: PASS=18 FAIL=0`, about 47 s, stdout 2998 characters.
- **Cache:**
  `logs/runner-cache/relational_letters_in_alternating_pairs_record_the_role_pattern_under_the_static_reading_2026_09_23.txt`
- **Arithmetic:** exact residues mod m. The searches assign sites in
  breadth-first order from one fixed value. Candidates come from the star
  rule at every assigned core neighbour, and every star is checked
  whenever one of its sites is assigned.

## Premises and declared objects

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

## Prior art and what is new

- Open PR 8691: relational frames and the static reading.
- Open PR 8729: the planar form.
- Open PR 8743: single-angle letters are rigid under the static reading
  and carry no role pattern.
- Open PR 8744: rigidity needs the global octant.
- Open PRs 8676 and 8679: coordinate letters read roles as c mod 2, and
  the static ice records.
- New here:
  - the pair rule and its rigidity under (D) and (E);
  - the covariant role readout;
  - condition (U) and the nearest-neighbour form;
  - the side-4 obstruction, where pair sums are forced to 180 degrees;
  - the contrasts.

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

## What this means

Under possibility covariance the letters are relational. The assembly
(open PR 8648) then has one unsoldered minimal set for gravity,
{alphabet, reading, roles}. Its roles are supplied, because a static
relational record carried no role pattern (open PR 8743).

Letters in alternating pairs do carry one:
- each site reads its role from its six differences;
- the reading's octant tells back from forward;
- each site is a function of its neighbours.

On open boxes, and on tori whose side the pair sums allow (8 | L here),
roles can therefore be read, and that set would become
{alphabet, reading}. This is the set fixed letters need.

The landed ice torus of side 4 is the exception:
- the single-angle letters of open PR 8743 do not wrap there;
- pair letters wrap only with pair sums of 180 degrees, and then fail
  (U).

So with these letters, the static route on that torus still needs fixed
letters or soldering, as open PR 8743 found for single-angle letters.
Open PR 8752 gives relational letters in four-angle cycles that do work on
it. The static ice records of open PR 8679 were checked on the side-4
torus; the side-8 torus carries these letters but not a checked ice route.

## No-Go Discipline Gate

The negative content is the side-4 obstruction and the contrasts, scoped
to the declared rule and windows.

- **N1 alternative routes.** Other relational rules, alphabets beyond one
  circle, and readings other than the static reading are outside this
  block.
- **N2 wall independence.** The rigidity proof is additive, and complete
  searches check it. The side-4 obstruction is proved in two lines and
  checked over 240 sets.
- **N3 hidden walls.** The reading's global octant is supplied structure
  (open PR 8744). The contrast with one octant per site is flexible.
- **N4 residual matching.** On the side-4 torus the residual is the
  antipodal ambiguity. Rigidity survives it, but the nearest-neighbour
  form does not.
- **N5 rhetoric audit.** "Records the role pattern" means a covariant
  local readout equal to the parity vector up to one global phase, on
  every record of the declared letters.
- **N6 partial-closure paths.**
  - the static ice records on tori of side 8 and larger;
  - pair letters on other windows;
  - rules that distinguish antipodes by larger records.
- **N7 steelman.**
  - For roles from relational letters: pair letters record them, with
    each site a function of its neighbours.
  - Against: not on the landed torus.

  Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8648, 8669, 8676, 8679, 8691, 8729,
  8743 and 8744 are cited.

## Falsifiers

Any of the following falsifies the theorems:
- a static record on a core of side at least 2 that is not an alternating
  spiral, for decodable letters with (D) and (E);
- a site of such a record whose readout is not its parity vector plus the
  record's phase;
- a decodable pair set that wraps on the side-4 torus and satisfies (U).

## Boundaries and non-claims

- The static reading with its global octant, the declared pair rule, the
  planar form, cores of side at least 2, and tori of side 2 to 8.
- The static ice route is not re-checked on the side-8 torus.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PRs 8648, 8669, 8676, 8679, 8691, 8729, 8743 and 8744, the landed
possibility-covariance note and the landed role-pattern note are cited.
No audit grade, no new axiom, no new primitive, no new comparator and no
new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the square lemma is checked by enumeration;
  - the searches check the proof on cores and tori;
  - the side-4 obstruction is checked over all small decodable sets;
  - the readout is checked at every site of every record.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| complementary types dropped | complement test removed | caught (8 FAILs) |
| common sense dropped | sense test removed | caught (7 FAILs) |
| distinct pairs dropped | pair test removed | caught (7 FAILs) |
| one pair per line dropped | same-pair test removed | caught (7 FAILs) |
| colliding signed angles accepted | collision test removed | caught (1 FAIL) |
| square relation sign | one sign flipped | caught (1 FAIL) |
| spirals without alternation | constant types | caught (5 FAILs) |
| candidate direction ignored | direction dropped | caught (6 FAILs) |
| parity read on the lattice axis index | pair frame ignored | caught (1 FAIL) |
| uniqueness from back neighbours only | forward neighbours dropped | caught (1 FAIL) |
| shared-star shift sign | shift sign flipped | caught (1 FAIL) |
| side-4 scan reads side 8 | wrap factor 4 | caught (1 FAIL) |
| parity-class shift by 90 degrees | shift m/4 | caught (1 FAIL) |
| covariance compares senses | senses compared | caught (1 FAIL) |
| octant rule keeps no sense per line | per-line sense test removed | caught (1 FAIL) |
| core value fixed off the spiral origin | fixed value 1 | caught (1 FAIL) |
| wrap condition without the half | factor L | caught (1 FAIL) |
| free contrast reads the pair rule | pair rule | caught (1 FAIL) |
| circle test excludes angle 1 | wrong excluded value | caught (1 FAIL) |

  19 of 19 are caught.

- **Vacuity guard:** record counts, star counts, square solutions, set
  counts and role weights are printed.
- **Budget:** 18 checks, stdout 2998 characters (ceiling 6000), about
  47 s (ceiling 900 s), exact modular arithmetic. Every search has a
  record cap, and all searches share a node cap of about three times the
  true run's 823641 nodes. A search fails its check when a cap binds.

## Verification

```bash
python3 scripts/relational_letters_in_alternating_pairs_record_the_role_pattern_under_the_static_reading_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=18 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/relational_letters_in_alternating_pairs_record_the_role_pattern_under_the_static_reading_2026_09_23.txt`.
