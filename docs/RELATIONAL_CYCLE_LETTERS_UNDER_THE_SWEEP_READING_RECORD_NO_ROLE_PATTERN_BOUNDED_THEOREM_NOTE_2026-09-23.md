---
claim_id: relational_cycle_letters_under_the_sweep_reading_record_no_role_pattern_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The relational cycle letters of open PR 8752 (m = 211, cycles (19, 31, 132, 29), (108, 43, 194, 77), (88, 39, 126, 169)) under the sweep reading of open PR 8743, in the planar form of open PR 8729: each core site reads only its three back neighbours, and its three back differences are signed angles with one common sense from the three different cycles. On the core of side 3 a search over core values, candidates in the table's order, finds 40 sweep records within 1139801 search nodes. The first, completed on the low faces, satisfies the sweep rule at all 27 core sites. It is not one of the 768 cycle spirals (a set that contains an explicit control spiral), and its back-step phases are not the position mod 4 plus one global phase on any line, while the control spiral's are. All 40 break the static cycle rule at (2, 2, 2), whose six neighbours all lie in the core, so none extends to a static record whatever the face values; the static rule accepts the control spiral there. So under the sweep reading these letters record no role pattern; the static reading of open PR 8752, which also reads the forward neighbours, is what makes them rigid. The sweep rule is checked to accept one sense with three cycles and to reject mixed senses and a repeated cycle. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/relational_cycle_letters_under_the_sweep_reading_record_no_role_pattern_2026_09_23.py
---

# Relational cycle letters under the sweep reading record no role pattern

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8752 found that relational letters
in four-angle cycles are rigid under the static reading, and record the
role pattern on the landed ice torus. The static reading reads a site's
back and forward neighbours. This block asks what the sweep reading,
which reads only the back neighbours, leaves of that.

## Result up front

1. **The sweep reading.** Each core site reads its three back neighbours
   x − e_i. Its three back differences must be signed angles with one
   common sense, from the three different cycles: the back half of the
   cycle rule. The runner checks that this rule accepts one sense with
   three cycles and rejects mixed senses and a repeated cycle.

2. **Witnesses of flexibility.** On the core of side 3, a search over core
   values finds 40 sweep records within 1139801 search nodes. The first,
   completed on the low faces, satisfies the sweep rule at all 27 core
   sites. It is not a cycle spiral: its core values differ from all 768,
   a set that contains an explicit control spiral.

3. **No static extension.** All 40 records break the static cycle rule
   at (2, 2, 2), the core site whose six neighbours all lie in the core.
   In the first, one line changes cycle across that site. So none of
   them extends to a static record, whatever the face values. The static
   rule accepts the control spiral at the same site.

4. **No role readout.** The back-step phases of the first witness are not
   the position mod 4 plus one global phase: they take 3, 3 and 4 values
   on the three axes. The same readout gives exactly one phase per axis
   on the control spiral.

5. **What this means.** The forward neighbours carry the rigidity. With
   back neighbours only, a line may change cycle and phase from site to
   site, so a record need keep neither the frame nor the positions. Roles
   from relational letters therefore need the static reading (open
   PR 8752), and the assembly's relational route to roles rests on the
   reading decision. The same holds for single-angle letters under the
   sweep (open PR 8743).

## Machine status and trace

- **Runner:**
  `scripts/relational_cycle_letters_under_the_sweep_reading_record_no_role_pattern_2026_09_23.py`
- **Result:** `TOTAL: PASS=7 FAIL=0`, about 48 s, stdout 1132 characters.
- **Cache:**
  `logs/runner-cache/relational_cycle_letters_under_the_sweep_reading_record_no_role_pattern_2026_09_23.txt`
- **Arithmetic:** exact residues mod 211. The search assigns core sites by
  level from (1, 1, 1), which is fixed at 0, with candidates in the order
  of the angle table, and stops at 40 records or a node cap of about three
  times the true run.

## Premises and declared objects

- **Sweep reading** (open PR 8743): back neighbours only.
- **Static reading and the cycle letters** (open PR 8752).
- **Planar form** (open PR 8729).

## Prior art and what is new

- Open PR 8743: single-angle letters under the sweep admit records that
  are not spirals.
- Open PR 8752: cycle letters are rigid under the static reading.
- New here: witnesses that cycle letters under the sweep reading admit
  records that are not spirals, break the static rule, and read no role
  pattern.

## No-Go Discipline Gate

- **N1 alternative routes.** Other formation readings, and other orders
  of formation, are not searched.
- **N2 wall independence.** Explicit witnesses, checked site by site; the
  static failure is at a site whose neighbours all lie in the core.
- **N3 hidden walls.** The control spiral shows that the rules and the
  readout accept what they should.
- **N4 residual matching.** The sweep leaves each line free to change
  cycle and phase.
- **N5 rhetoric audit.** "Record no role pattern" means: records exist
  whose readout is not the parity vector plus one global phase.
- **N6 partial-closure paths.** Counting all sweep records; sweep readings
  with more letters.
- **N7 steelman.** For the sweep: it keeps local consistency. Against: its
  records need keep neither the frame nor the roles. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8648, 8729, 8743 and 8752 are cited.

## Falsifiers

- A proof that every sweep record of these letters on the side-3 core is a
  cycle spiral.
- A witness that satisfies the static rule at (2, 2, 2).

## Boundaries and non-claims

- The sweep reading, the declared letters, the core of side 3.
- The full number of sweep records is not computed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PRs 8648, 8729, 8743 and 8752 and the landed possibility-covariance
note are cited. No audit grade, no new axiom, no new primitive, no new
comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** witnesses checked site by site; controls for
  the sweep rule, the static rule, the spiral set and the readout.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| sweep rule without the common sense | sense test removed | caught (1 FAIL) |
| sweep rule without distinct cycles | cycle test removed | caught (1 FAIL) |
| spirals without the phase advance | constant phase | caught (1 FAIL) |
| static rule without the same-cycle test | cycle test removed | caught (1 FAIL) |
| faces completed with the wrong sense | sense flipped | caught (1 FAIL) |
| phase readout without the position | position dropped | caught (1 FAIL) |
| thirty-nine witnesses | record cap 39 | caught (2 FAILs) |

  7 of 7 are caught. Three earlier mutants that altered a helper without
  changing the witnesses' verdicts were caught only after the controls
  were added.

- **Vacuity guard:** record and node counts, phase counts and the control
  spiral are printed or checked.
- **Budget:** 7 checks, stdout 1132 characters (ceiling 6000), about 48 s
  (ceiling 900 s).

## Verification

```bash
python3 scripts/relational_cycle_letters_under_the_sweep_reading_record_no_role_pattern_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=7 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/relational_cycle_letters_under_the_sweep_reading_record_no_role_pattern_2026_09_23.txt`.
