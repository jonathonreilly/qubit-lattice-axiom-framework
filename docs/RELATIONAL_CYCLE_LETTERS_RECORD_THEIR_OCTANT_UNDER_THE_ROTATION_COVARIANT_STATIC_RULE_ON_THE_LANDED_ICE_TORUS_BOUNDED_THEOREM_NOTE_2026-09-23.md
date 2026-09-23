---
claim_id: relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_on_the_landed_ice_torus_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The Admissibility text asks for one fixed nearest-neighbour rule covariant under lattice translations and proper cubic rotations. The static cycle rule of open PR 8752 fixes back neighbours x - e_i and forward neighbours x + e_i, a supplied octant, and its 768 stars are not closed under a quarter turn. Its rotation-covariant form lets each site read each lattice line in either orientation: on each line the two differences have one raw sense and one cycle, with phases one step apart in either direction, and the three lines use the three cycles; its 24576 stars are closed under all 48 signed axis permutations. For the letters of open PR 8752 (m = 211, cycles (19, 31, 132, 29), (108, 43, 194, 77), (88, 39, 126, 169)), a complete search on the landed ice torus of side 4 finds exactly the 24576 oriented cycle spirals (6 frames, 8 raw senses, 8 orientations, 64 phases). In every record each site reads the same frame, the same orientation of each axis and its parity vector up to one global phase, and all 8 octants occur: the records carry their own octant and the role pattern. No two covariant stars share their six neighbours (a decodable control set mod 37 has 864 such pairs), and on sampled records the rule admits one value per site. The fixed-octant rule's 768 records are the covariant records with every axis forward and one common sense. On the side-2 box the covariant rule leaves each boundary step free and has more than 100000 records. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_2026_09_23.py
---

# Relational cycle letters record their octant under the rotation-covariant static rule, on the landed ice torus

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign after the TOE derivation campaign
by underdetermination witnesses. Open PRs 8743, 8744 and 8752 used a
static reading whose octant is supplied: back neighbours x − e_i, forward
neighbours x + e_i. The Admissibility text asks for a rule covariant under
proper cubic rotations. This block asks whether relational letters can do
without the supplied octant.

## Result up front

1. **The covariant rule.** The Admissibility text reads: "There is one
   fixed nearest-neighbor admissibility rule, covariant under lattice
   translations and proper cubic rotations." A static rule with a fixed
   back and forward octant is not rotation covariant: the 768 stars of
   the cycle rule of open PR 8752 are not closed under a quarter turn. Its
   covariant form lets each site read each lattice line in either
   orientation. On each line the two differences have one raw sense and
   one cycle, with phases one step apart in either direction; the three
   lines use the three cycles. Its 24576 stars are closed under all 48
   signed axis permutations.

2. **On the landed ice torus the records are oriented spirals.** For the
   letters of open PR 8752, a complete search on the torus of side 4
   finds exactly the 24576 oriented cycle spirals: each axis carries one
   cycle, one raw sense, one orientation and one phase (6 × 8 × 8 × 64).

3. **The records carry their octant and their roles.** In every record,
   every site reads:
   - the same frame (which line carries which cycle);
   - the same orientation of each axis, the direction in which its phase
     advances;
   - its parity vector x mod 2 up to one global phase: the role pattern.

   All 8 octants occur. The octant is a record value of the whole
   configuration, not something the reading supplies.

4. **Each site is a function of its neighbours.** No two covariant stars
   share their six neighbours; a decodable control set mod 37 has 864
   such pairs. On sampled records the covariant rule admits exactly one
   value at every site.

5. **Relation to the supplied octant.** The 768 records of the
   fixed-octant rule (open PR 8752) are exactly the covariant records with
   every axis forward and one common sense. Open PR 8752's contrast, with
   one octant per site and 24576 records of which 768 are spirals, is
   therefore not flexibility. Its other records are the same spirals with
   axes reversed or with a raw sense per axis. That contrast's reading,
   that the rigidity uses the reading's global octant, is corrected here
   for cycle letters.

6. **Where the lines close.** On an open box the covariant rule leaves
   each boundary step free to go either way. The side-2 box has more than
   100000 records. The orientation is recorded where the lines close, as
   on the torus.

7. **What this means.** On the landed ice torus the relational static
   route needs no supplied octant. The rule can be rotation covariant, as
   the Admissibility text asks, and the letters record the orientation,
   the frame and the roles. The direction that the static reading seemed
   to supply is recorded by the configuration. Cycles tell the two ends of
   a line apart because their phase advances. Single-angle letters (open
   PR 8744) cannot do this: a line of one angle read backwards is again a
   line of one angle, with the opposite sense.

## Machine status and trace

- **Runner:**
  `scripts/relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_2026_09_23.py`
- **Result:** `TOTAL: PASS=9 FAIL=0`, about 157 s, stdout 1479 characters,
  peak about 270 MB.
- **Cache:**
  `logs/runner-cache/relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_2026_09_23.txt`
- **Arithmetic:** exact residues mod m. The searches assign sites in
  breadth-first order from one fixed value, core sites before faces, with
  candidates from the star rule at every assigned core neighbour.

## Premises and declared objects

- **Admissibility** (minimal axioms): one fixed nearest-neighbour rule,
  covariant under lattice translations and proper cubic rotations.
- **Static reading** (open PR 8691), with the covariant rule in place of a
  supplied octant.
- **Planar form** (open PR 8729); the letters of open PR 8752.
- **Role pattern:** the parity vector x mod 2 up to its 8 global phases
  (landed role-pattern note).

## Prior art and what is new

- Open PR 8744: single-angle letters need a global octant.
- Open PR 8752: cycle letters under the fixed-octant rule, and its
  per-site octant contrast.
- New here:
  - the covariant rule and its closure under the cubic group;
  - the records on the landed torus under that rule are the oriented
    spirals;
  - the recorded octant;
  - the correction of open PR 8752's reading of its contrast.

## Theorem — Oriented spirals on the landed torus

For the declared letters, the static records of the covariant rule on the
torus of side 4 are exactly the oriented cycle spirals. The theorem is
established by complete search, cross-checked by generating the 24576
oriented spirals independently. On each line the phase walk may step up or
down at every site; a spiral walks one way at a constant rate. The search
shows that on this torus no walk turns and no line's sense or cycle
changes across parallel lines. Every record reads as in item 3.

## No-Go Discipline Gate

- **N1 alternative routes.** Other letters and other windows are outside
  this block. Open boxes are flexible at their boundaries.
- **N2 wall independence.** Complete search, an independent generator,
  and a closure check on the rule.
- **N3 hidden walls.** The covariant rule is checked against all 48 signed
  axis permutations, the fixed-octant rule against a quarter turn.
- **N4 residual matching.** On open boxes the residual is boundary freedom.
- **N5 rhetoric audit.** "Record their octant" means every record reads
  one orientation per axis at every site.
- **N6 partial-closure paths.**
  - tori of side 8 and more under the covariant rule;
  - cores with fixed faces;
  - pair letters under the covariant rule.
- **N7 steelman.** For a supplied octant: open boxes do not fix it.
  Against: the landed torus fixes it by closure. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8648, 8691, 8729, 8743, 8744 and 8752
  are cited.

## Falsifiers

- A static record of the covariant rule on the side-4 torus that is not an
  oriented cycle spiral.
- A site of such a record whose orientation or parity readout differs from
  the rest of the record.
- Two covariant stars of the declared letters that share their six
  neighbours.

## Boundaries and non-claims

- The declared letters, the covariant rule, the torus of side 4, and the
  side-2 box as a contrast.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, open PRs 8648, 8691, 8729, 8743, 8744 and 8752, the
landed possibility-covariance note and the landed role-pattern note are
cited. No audit grade, no new axiom, no new primitive, no new comparator
and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** complete search against an independent
  generator; the closure check; (U) with a positive control; readouts at
  every site of every record.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| covariant rule without the per-line sense test | sense test removed | caught (3 FAILs) |
| covariant rule with forward steps only | backward steps refused | caught (3 FAILs) |
| distinct cycles dropped | cycle test removed | caught (7 FAILs) |
| covariant stars with one common sense | per-line senses removed | caught (2 FAILs) |
| action without the reversal | reversal dropped | caught (1 FAIL) |
| oriented spirals without the orientation | orientation ignored | caught (2 FAILs) |
| orientation read as always forward | readout fixed | caught (1 FAIL) |
| parity read without the position | position dropped | caught (1 FAIL) |
| shared-star shift sign | shift sign flipped | caught (1 FAIL) |
| fixed-like records of any sense | sense test dropped | caught (1 FAIL) |
| box read with the fixed rule | fixed rule on the box | caught (1 FAIL) |
| candidate direction ignored | direction dropped | caught (4 FAILs) |
| frame read from phases | phases for cycles | caught (1 FAIL) |
| quarter turn replaced by the identity | identity turn | caught (1 FAIL) |

  14 of 14 are caught.

- **Vacuity guard:** record, star and octant counts and the control count
  are printed.
- **Budget:** 9 checks, stdout 1479 characters (ceiling 6000), about
  157 s (ceiling 900 s). Every search has a record cap, and all share a
  node cap of about three times the true run's 1883006 nodes.

## Verification

```bash
python3 scripts/relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=9 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_2026_09_23.txt`.
