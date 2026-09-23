---
claim_id: strong_cycle_letters_record_frame_and_roles_under_the_rotation_covariant_rule_on_every_window_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The rotation-covariant static cycle rule (open PR 8854; each site reads each lattice line in either orientation: per line one raw sense and one cycle, phases one step apart either way; three lines, three cycles) makes the phase walk along each line step by +-1 at every site. Cycle letters are strong when they decode, each cycle sums to 0, and every square of links is straight for every sign pattern (the mixed-sign square condition). Then every covariant record on a core of side at least 2 is a folded cycle spiral: each axis carries one cycle, one raw sense and one +-1 phase walk shared by all parallel lines. Each site therefore reads the frame and its parity vector (the phase parity alternates at every step): the role pattern, on every window. The orientation is recorded exactly where the walks cannot turn. For m = 100003 and cycles (17612, 74607, 8272, 99515), (33433, 15456, 64938, 86179), (99741, 58916, 61899, 79453): the square condition holds for all sign patterns, and (U) holds under the covariant rule (24576 stars, one per neighbour class). The covariant records on the core of side 3 are exactly the 24576 folded spirals, and every one reads a global frame and parity vector. On the side-4 torus every closed zero-sum phase walk is monotone, so the records there are oriented spirals and carry their octant. On the side-8 torus folded closed walks exist (64 per cycle), and a folded spiral satisfies the rule at all 512 sites with a varying orientation readout and global frame and parity readouts. Controls: the letters of open PR 8752 (m = 211) have 240 bent mixed-sign squares, and on the side-3 core 9216 of their 33792 covariant records have a non-global parity readout; a set mod 37 has (U) collisions. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/strong_cycle_letters_record_frame_and_roles_under_the_rotation_covariant_rule_on_every_window_2026_09_23.py
---

# Strong cycle letters record the frame and the roles under the rotation-covariant rule, on every window

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. The octant block (open PR
8854) showed that the cycle letters of open PR 8752, under the
rotation-covariant rule that the Admissibility text asks for, record their
octant on the landed ice torus. This block asks what that rule records on
other windows, and what the letters need for it.

## Result up front

1. **Phase walks.** Under the rotation-covariant rule each site reads
   each lattice line in either orientation. Along a line, the raw sense and
   the cycle are constant, and the phase steps by +1 or −1 at every site: a
   walk that may turn.

2. **Strong letters.** Cycle letters are strong when:
   - they decode;
   - each cycle sums to 0;
   - every square of links is straight for every sign pattern (the
     mixed-sign square condition).

   The letters here are m = 100003 with cycles (17612, 74607, 8272, 99515),
   (33433, 15456, 64938, 86179) and (99741, 58916, 61899, 79453). They are
   strong, and (U) holds under the covariant rule.

3. **Every record is a folded spiral.** For strong letters, every covariant
   record on a core of side at least 2 is a folded cycle spiral:
   - each axis carries one cycle and one raw sense;
   - each axis has one phase walk with steps of ±1, shared by all parallel
     lines.

   On the core of side 3 the covariant records are exactly the 24576
   folded spirals (6 frames × 16³).

4. **Frame and roles on every window.** Each site reads the frame and its
   parity vector. The phase parity alternates at every step, whichever
   way the walk goes, so the parity vector is x mod 2 up to one global
   phase: the role pattern. Every record on the side-3 core reads both
   globally.

5. **The orientation only where walks cannot turn.**
   - On the side-4 torus, the landed ice torus, every closed zero-sum
     phase walk is monotone. The records are oriented spirals and carry
     their octant, as the octant block found for the letters of open
     PR 8752.
   - On the side-8 torus folded closed zero-sum walks exist, 64 per cycle.
     A folded spiral satisfies the rule at all 512 sites. Its orientation
     readout varies along an axis, while its frame and parity readouts are
     global.

   So the orientation is a record only on windows that forbid turning;
   the roles are a record everywhere.

6. **The square condition carries the roles.** The letters of open
   PR 8752 (m = 211) have 240 bent mixed-sign squares. On the side-3 core,
   9216 of their 33792 covariant records have a parity readout that is not
   global. A set mod 37 has (U) collisions under the covariant rule.

7. **What this means.** With strong cycle letters, the rotation-covariant
   static rule that the Admissibility text asks for records the frame and
   the role pattern on every window, with each site a function of its
   neighbours. No octant is supplied and no role is supplied. Under
   possibility covariance, the static route's relational letters then need
   only the alphabet and the reading. The orientation is a record on the
   landed torus and is absent where walks may turn, and the role readout
   does not use it.

## Machine status and trace

- **Runner:**
  `scripts/strong_cycle_letters_record_frame_and_roles_under_the_rotation_covariant_rule_on_every_window_2026_09_23.py`
- **Result:** `TOTAL: PASS=10 FAIL=0`, about 149 s, stdout 1401 characters.
- **Cache:**
  `logs/runner-cache/strong_cycle_letters_record_frame_and_roles_under_the_rotation_covariant_rule_on_every_window_2026_09_23.txt`
- **Arithmetic:** exact residues mod m. The core search omits faces: a
  boundary line can always be completed by a face step of its own sense
  and cycle, one phase away.

## Premises and declared objects

- **Admissibility** (minimal axioms): one fixed nearest-neighbour rule,
  covariant under lattice translations and proper cubic rotations.
- **The covariant rule** (octant block, open PR 8854).
- **Planar form** (open PR 8729); cycle letters (open PR 8752).
- **Role pattern:** the parity vector x mod 2 up to its 8 global phases.

## Prior art and what is new

- Open PR 8752: cycle letters under the fixed-octant rule.
- Octant block (open PR 8854): under the covariant rule, the letters of
  open PR 8752 record their octant on the landed torus.
- New here:
  - phase walks and folded spirals;
  - the mixed-sign square condition and letters that satisfy it;
  - roles on every window;
  - the orientation exactly where walks cannot turn;
  - the m = 211 contrast.

## Theorem — Folded spirals

Let the letters be strong, and take a core of side at least 2.

- **Links.** On a core link from y to y + e_i the difference is F_i(y) and
  also B_i(y + e_i), and it decodes to one raw sense, one cycle and one
  phase. So along a line of core links the raw sense and the cycle are
  constant, and at each site the phase steps by ±1.
- **Squares.** In a core square, write a = F_i(y) and c = F_j(y), and
  b = F_j(y + e_i) and e = F_i(y + e_j). The line through y + e_i along i
  carries the cycle of a, so b carries another cycle; likewise e. At the
  far corner b and e carry different cycles. The relation a + b = c + e,
  with any raw senses, then has only straight solutions: b = c and e = a,
  with the same cycle, phase and raw sense.
- **Folded spirals.** Parallel lines therefore agree step by step. Each
  axis carries one cycle, one raw sense and one phase walk, and every such
  choice satisfies the rule.

**Readouts.** The forward step along axis i at x has phase w_i(x_i), and
w_i(x_i) ≡ w_i(1) + x_i − 1 (mod 2). The parity vector is x mod 2 plus one
global phase. The frame is the cycle carried by each axis.

**Windows.** On the side-L torus each walk must close, and its steps must
sum to 0 mod m. For the declared letters and L = 4, only monotone walks
do; for L = 8, folded walks do as well.

## No-Go Discipline Gate

- **N1 alternative routes.** Other alphabets and rules are outside this
  block.
- **N2 wall independence.** The proof rests on a finite condition, checked
  by enumeration over all sign patterns. The side-3 search is compared with
  an independent generator.
- **N3 hidden walls.** Faces are omitted from the core search; the
  completion argument is stated.
- **N4 residual matching.** Where walks may turn, the orientation is not a
  record.
- **N5 rhetoric audit.** "On every window" means every core of side at
  least 2 and every torus on which the letters wrap.
- **N6 partial-closure paths.**
  - smaller strong moduli;
  - the combined letter-and-ice record;
  - the formation reading with these letters.
- **N7 steelman.** For a supplied orientation: walks may turn. Against:
  the roles and the frame do not need it. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8648, 8729, 8752 and 8854 are cited.

## Falsifiers

- A covariant record of strong letters on a core that is not a folded
  spiral.
- A record of strong letters whose parity readout is not global.
- A closed zero-sum walk of length 4 that turns, for the declared letters.

## Boundaries and non-claims

- The covariant rule, the declared letters, cores of side at least 2, and
  tori of side 4 and 8.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, open PRs 8648, 8729, 8752 and 8854, the landed
possibility-covariance note and the landed role-pattern note are cited. No
audit grade, no new axiom, no new primitive, no new comparator and no new
framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the square condition is enumerated over all
  sign patterns; the core search is checked against an independent
  generator; (U) is tested with a positive control; the m = 211 contrast.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| covariant rule without the per-line sense test | sense test removed | caught (3 FAILs) |
| covariant rule with forward steps only | backward steps refused | caught (3 FAILs) |
| distinct cycles dropped | cycle test removed | caught (4 FAILs) |
| bent test ignores the senses | sense clause removed | equivalent (see below) |
| U classes keyed without the forward part | key shortened | caught (1 FAIL) |
| folded generator without turns | turns removed | caught (1 FAIL) |
| parity read without the position | position dropped | caught (2 FAILs) |
| closure without the zero-sum test | sum test removed | caught (1 FAIL) |
| folded witness made monotone | witness unfolded | caught (1 FAIL) |
| frame read from phases | phases for cycles | caught (1 FAIL) |
| side-4 closure read at length 6 | wrong length | caught (1 FAIL) |

  10 of 10 defect mutants are caught. The sense clause is equivalent for decodable letters: a square whose opposite sides match in cycle and phase but not in sense would need twice one angle to equal plus or minus another angle, which decoding excludes.

- **Vacuity guard:** record, star, class and walk counts are printed.
- **Budget:** 10 checks, stdout 1401 characters (ceiling 6000), about
  149 s (ceiling 900 s). All searches share a node cap of about three
  times the true run's 1269866 nodes.

## Verification

```bash
python3 scripts/strong_cycle_letters_record_frame_and_roles_under_the_rotation_covariant_rule_on_every_window_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=10 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/strong_cycle_letters_record_frame_and_roles_under_the_rotation_covariant_rule_on_every_window_2026_09_23.txt`.
