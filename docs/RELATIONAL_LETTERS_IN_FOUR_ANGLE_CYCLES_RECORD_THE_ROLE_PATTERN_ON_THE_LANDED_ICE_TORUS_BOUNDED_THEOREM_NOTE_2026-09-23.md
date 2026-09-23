---
claim_id: relational_letters_in_four_angle_cycles_record_the_role_pattern_on_the_landed_ice_torus_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Relational letters in which each lattice line cycles through four angles (c_0, c_1, c_2, c_3) with sum 0 mod m, in the planar form of open PR 8729, under the static reading of open PR 8691 with its global octant. One fixed nearest-neighbour rule, the cycle rule: at a core site the six differences to its neighbours are signed angles with one common sense, on each lattice line the back and forward differences are consecutive angles c_k, c_{k+1} of one cycle, and the three lines use the three cycles. If the twenty-four signed angles are distinct and nonzero and every solution of the square relation is straight (a finite condition), every static record on a core of side at least 2 is a cycle spiral: each axis carries one cycle, and the phase of the forward step along axis i is phi_i + x_i mod 4. With one value fixed there are 768 records (6 frames, 2 senses, 4^3 phases). For m = 211 and cycles (19, 31, 132, 29), (108, 43, 194, 77), (88, 39, 126, 169): every square solution is straight (96 straight, 0 bent); no two allowed stars share their six neighbours, so every site is a function of its neighbours (positive control: a decodable cycle set mod 37 with 24 shared stars); complete searches on cores of side 2, 3 and 4 find exactly the 768 cycle spirals; tori of side 2 to 8 have static records exactly when 4 divides L, and then exactly the 768 spirals, which includes the landed ice torus of side 4. On that torus each site reads the frame and its phase x mod 4 on every line, up to one global phase, hence its parity vector (the role pattern) up to one global phase; the readout commutes with rotations of the circle, and the rule admits exactly one value at every site given its neighbours. Since m is odd, no residue is 180 degrees, so the antipodal ambiguity that pair letters meet on this torus (open PR 8750) does not arise. Contrasts: a cycle set mod 37 with that property but with bent squares has 1344 core records, 576 of them not spirals; with one octant per site the side-4 torus has 24576 records, 768 of them spirals with every axis forward; open PR 8854 shows that all 24576 are these spirals with axes reversed or with a raw sense per axis, so under that rotation-covariant rule the letters record their octant on this torus. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/relational_letters_in_four_angle_cycles_record_the_role_pattern_on_the_landed_ice_torus_2026_09_23.py
---

# Relational letters in four-angle cycles record the role pattern on the landed ice torus

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8750 found that relational letters
in alternating pairs record the role pattern under the static reading,
with each site a function of its neighbours, but not on the landed ice
torus of side 4. There the pairs must sum to 180 degrees, and a site is
fixed by its neighbours only up to its antipode. This block asks for
relational letters that work on that torus.

## Result up front

1. **Four-angle cycles.** Each lattice line cycles through four angles
   (c_0, c_1, c_2, c_3) whose sum is 0 mod m. At a core site the cycle
   rule asks:
   - the six differences to the neighbours are signed angles with one
     common sense;
   - on each lattice line, the back and forward differences are
     consecutive angles c_k, c_{k+1} of one cycle;
   - the three lines use the three cycles.

   It is one fixed nearest-neighbour rule. It depends only on
   differences, and it uses the reading's global octant (open PR 8744) to
   tell back from forward. The letters here are m = 211 with cycles
   (19, 31, 132, 29), (108, 43, 194, 77) and (88, 39, 126, 169).

2. **The records are cycle spirals.** Two conditions suffice: the
   twenty-four signed angles decode each difference, and every solution of
   the square relation is straight. Then every static record on a core of
   side at least 2 is a cycle spiral:
   - each axis carries one cycle;
   - along axis i the forward step at x is c_{phi_i + x_i mod 4}.

   With one value fixed there are 768 records: 6 frames, 2 senses and 4^3
   phases. For the declared letters the square relation has 96 straight
   solutions and no bent ones. Complete searches on cores of side 2, 3
   and 4 find exactly the 768 spirals.

3. **They live on the landed ice torus.** A spiral wraps on the side-L
   torus when 4 divides L, since each cycle sums to 0. The search finds no
   records for L = 2, 3, 5, 6, 7, and exactly the 768 spirals for L = 4 and
   8. The side-4 torus is the landed ice torus: 2 × 2 × 2 cells, or
   4 × 4 × 4 sites once links, plaquettes and cube sites are counted.

4. **Each site reads its role there.** On the side-4 torus each site
   decodes its forward differences:
   - a frame (which line carries which cycle) and a sense, the same at every
     site;
   - on every line a phase, x mod 4 plus one global phase;
   - so its parity vector x mod 2, up to one global phase: the role
     pattern. All 64 cycle phases and all 8 parity phases occur.

   The readout commutes with rotations of the circle.

5. **Each site is a function of its neighbours.** No two allowed stars
   share their six neighbours: moving a site with its neighbours fixed
   never gives another allowed star. This condition, (U), holds for the
   declared letters. The rule admits exactly one value at every site of
   the side-4 records. Since m is odd, no residue is 180 degrees, so the
   antipodal ambiguity of open PR 8750 does not arise. A decodable cycle
   set mod 37 that fails (U), with 24 shared stars, is the test's positive
   control.

6. **Contrasts.**
   - A cycle set mod 37 with (U) but with bent squares has 1344 records on
     the core of side 2, 576 of them not spirals. So straight squares
     carry the rigidity.
   - With one octant per site (a sense per line, phase steps of +1 or −1)
     the side-4 torus has 24576 records, 768 of them spirals with every
     axis forward. Open PR 8854 shows that all 24576 are the same spirals
     with axes reversed or with a raw sense per axis. That rule is the
     rotation-covariant one the Admissibility text asks for, and under it
     the letters record their own octant on this torus; no octant need be
     supplied.

7. **What this means.** Cycle letters give each site, relationally, what a
   coordinate label of open PRs 8676 and 8679 gives on the landed torus:
   - the lattice frame;
   - its position mod 4 on every line.

   Both hold up to one global rotation of the circle and one global
   translation. So under possibility covariance, the static route with
   relational letters reads roles on the landed ice torus too:
   - open PR 8750's side-4 exception is removed;
   - the unsoldered gravity set of the assembly's relational control is
     {alphabet, reading} on open boxes and on tori whose side 4 divides,
     which include the landed ice torus. Tori of side 2, 3, 5, 6 and 7
     carry neither pair nor cycle records.

   The static ice records of open PR 8679 are checked on this torus. The
   combined record, letters and ice records together, is not re-searched
   here; it follows by composition: the letters are functions of their
   neighbours, and the frame and roles are read from them.

## Machine status and trace

- **Runner:**
  `scripts/relational_letters_in_four_angle_cycles_record_the_role_pattern_on_the_landed_ice_torus_2026_09_23.py`
- **Result:** `TOTAL: PASS=13 FAIL=0`, about 170 s, stdout 2196 characters.
- **Cache:**
  `logs/runner-cache/relational_letters_in_four_angle_cycles_record_the_role_pattern_on_the_landed_ice_torus_2026_09_23.txt`
- **Arithmetic:** exact residues mod m. The searches assign core sites
  first, in breadth-first order from one fixed value, then the faces.
  Candidates come from the star rule at every assigned core neighbour.

## Premises and declared objects

- **Static reading** (open PR 8691) with its global octant (open PR 8744).
- **Planar form** (open PR 8729): values on one great circle as residues
  mod m. The one-great-circle step of open PR 8743 uses separations that
  are neither 0 nor 180 degrees. Here m is odd, so no residue is 180
  degrees, and decoding makes every link difference nonzero. This note
  does not restate that step for the cycle rule.
- **Role pattern:** the parity vector x mod 2, up to its 8 global phases
  (landed role-pattern note; open PR 8669).
- **Landed ice torus:** side 4 in fine form (open PRs 8679, 8727).

## Prior art and what is new

- Open PR 8750: pair letters record the role pattern, but not on the
  side-4 torus.
- Open PR 8743: single-angle letters carry no role pattern.
- Open PRs 8676 and 8679: coordinate labels in Z_4^3, roles as c mod 2.
- New here:
  - the cycle rule and its rigidity from straight squares;
  - letters that live on the landed ice torus, with each site a function
    of its neighbours;
  - the role readout there;
  - the contrast with bent squares.

## Theorem 1 — Cycle spirals

Assume decoding and straight squares, and a core of side at least 2.

- **Links.** On a core link from y to y + e_i, F_i(y) = B_i(y + e_i)
  decodes to one sense, one cycle and one phase k. The rule at y + e_i
  makes its forward phase k + 1. So along every line of core links the
  cycle is constant and the phases advance by one per step. The core is
  connected, so the sense is constant.
- **Squares.** In a core square y, y + e_i, y + e_j, y + e_i + e_j, write
  a = F_i(y), c = F_j(y), b = F_j(y + e_i) and e = F_i(y + e_j). By the
  links step:
  - b carries a cycle X ≠ A, where A is the cycle of line i;
  - e carries a cycle Y ≠ B, where B is the cycle of line j;
  - X ≠ Y at the far corner.

  So a + b = c + e is one of the finitely many square relations. By
  assumption each of them is straight: X = B, Y = A, b = c and e = a.
- **Constancy.** Straight squares carry each line's cycle and phase
  across the transverse directions. Every core link lies in a core square.
  So axis i carries one cycle, and the forward phase at x is
  phi_i + x_i mod 4.

The record is a cycle spiral. Conversely every cycle spiral satisfies the
rule. With one value fixed there are 6 × 2 × 64 = 768.

## Theorem 2 — Tori and roles

On the side-L torus every site is a core site, so for L ≥ 3 a record is
one cycle spiral that wraps. Going once around axis i adds L/4 full
cycles when 4 divides L, which sum to 0 mod m. Otherwise the phase does
not return, since the phase advances by one per step. So records exist
exactly when 4 divides L. The search confirms this for L = 2 to 8 and
finds the 768 spirals for L = 4 and 8.

On the side-4 torus the forward differences at x decode to the frame, the
sense and the phases phi_i + x_i mod 4. Reduced mod 2, the phases give
x mod 2 plus the global phase phi mod 2: the parity vector up to one of
its 8 global phases. The runner reads this at all 64 sites of all 768
records:
- one frame per record;
- one phase per record;
- all 64 cycle phases and all 8 parity phases occur.

## Theorem 3 — The nearest-neighbour form

(U) says that no d ≠ 0 turns an allowed star into another allowed star
with the same six neighbours. For the declared letters the runner tests
all 768 stars and all 210 shifts, and finds none. The positive control is
the cycle set mod 37 ((34, 13, 35, 29), (11, 4, 23, 36), (20, 15, 18, 21)),
which decodes but has 24 such stars. On 48 of the side-4 records, the
rule admits exactly one value at every site given its neighbours.

## No-Go Discipline Gate

- **N1 alternative routes.** Pair letters (open PR 8750) and single-angle
  letters (open PR 8743) are the neighbouring schemes; other cycle lengths
  are not searched.
- **N2 wall independence.** The proof rests on a finite condition, checked
  by enumeration. The searches check the proof on cores of side 2 to 4
  and on tori of side 2 to 8.
- **N3 hidden walls.** The fixed-octant rule uses a supplied octant. With
  one octant per site the side-4 torus has 24576 records, the oriented
  spirals of open PR 8854, so on this torus the letters record the octant
  themselves.
- **N4 residual matching.** Rigidity fails with bent squares; the contrast
  exhibits it.
- **N5 rhetoric audit.** "Record the role pattern" means a covariant local
  readout equal to the parity vector up to one global phase, on every
  record.
- **N6 partial-closure paths.**
  - the combined record with the static ice records, searched directly;
  - cores of side 5 and more, searched directly;
  - the smallest modulus with these properties.
- **N7 steelman.** For: the letters work on the landed torus. Against:
  they need an alphabet of 211 values and the reading's octant. Both are
  recorded.
- **N8 cross-cycle echo.** Open PRs 8648, 8669, 8676, 8679, 8691, 8727,
  8729, 8743, 8744 and 8750 are cited.

## Falsifiers

Any of the following falsifies the theorems:
- a static record on a core of side at least 2 that is not a cycle
  spiral, for decodable letters with straight squares;
- a side-4 record whose readout at some site is not its parity vector plus
  the record's phase;
- two allowed stars of the declared letters that share their six
  neighbours.

## Boundaries and non-claims

- The static reading with its global octant, the declared cycle rule, the
  planar form, cores of side at least 2, and tori of side 2 to 8.
- The combined record with ice records is not re-searched.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PRs 8648, 8669, 8676, 8679, 8691, 8727, 8729, 8743, 8744 and 8750,
the landed possibility-covariance note and the landed role-pattern note
are cited. No audit grade, no new axiom, no new primitive, no new
comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the square condition is enumerated;
  - the searches check the proof;
  - (U) has a positive control;
  - the readout is checked at every site of every side-4 record.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| phase step not enforced | phase test removed | caught (6 FAILs) |
| common sense dropped | sense test removed | caught (5 FAILs) |
| distinct cycles dropped | cycle test removed | caught (6 FAILs) |
| one cycle per line dropped | same-cycle test removed | caught (4 FAILs) |
| one angle moved by one | cycle sum broken | caught (5 FAILs) |
| square relation sign | one sign flipped | caught (1 FAIL) |
| spirals without the phase advance | constant phase | caught (3 FAILs) |
| candidate direction ignored | direction dropped | caught (5 FAILs) |
| phase read without the position | position dropped | caught (1 FAIL) |
| uniqueness from back neighbours only | forward neighbours dropped | caught (1 FAIL) |
| shared-star shift sign | shift sign flipped | caught (1 FAIL) |
| tori expected for even sides | 4 | L read as 2 | L | caught (1 FAIL) |
| frame read from phases | phases for cycles | caught (1 FAIL) |
| covariance compares senses | senses compared | caught (1 FAIL) |
| core value fixed off the spiral origin | fixed value 1 | caught (1 FAIL) |
| search order with faces first | faces first | caught (6 FAILs) |
| spirals without the sense | sense dropped | caught (3 FAILs) |
| octant rule keeps no sense per line | per-line sense test removed | caught (1 FAIL) |

  18 of 18 are caught.

- **Vacuity guard:** record counts, star counts, square solutions and
  phase counts are printed.
- **Budget:** 13 checks, stdout 2196 characters (ceiling 6000), about
  170 s (ceiling 900 s), exact modular arithmetic. Every search has a
  record cap. All searches share a node cap of about three times the true
  run's 2351540 nodes, and a search fails its check when a cap binds.

## Verification

```bash
python3 scripts/relational_letters_in_four_angle_cycles_record_the_role_pattern_on_the_landed_ice_torus_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=13 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/relational_letters_in_four_angle_cycles_record_the_role_pattern_on_the_landed_ice_torus_2026_09_23.txt`.
