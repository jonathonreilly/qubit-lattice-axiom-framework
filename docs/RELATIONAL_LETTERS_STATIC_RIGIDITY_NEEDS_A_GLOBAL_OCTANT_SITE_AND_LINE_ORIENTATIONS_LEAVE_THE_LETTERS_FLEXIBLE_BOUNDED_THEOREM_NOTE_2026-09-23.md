---
claim_id: relational_letters_static_rigidity_needs_a_global_octant_site_and_line_orientations_leave_the_letters_flexible_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The seven relational letters (1, 2, 4) x 360/7 under static readings that differ in how the octant is supplied, on the core of side 2 of the side-4 box with one core value fixed. At a core site with octant sigma the back neighbours are x - sigma_i e_i and the forward neighbours x + sigma_i e_i, and the back differences and the forward differences must each be a common-sign permutation of the angles (open PR 8743). A global octant (every lattice line along an axis oriented alike) gives exactly the 12 spirals aligned with it, for each of the 8 octants; the 4 opposite pairs give 48 distinct records. One orientation per lattice line (all 4096 fields of the 12 lines through the core) gives 11136 records, of which 48 are spirals; 1300 fields admit records, and a field that is not a global octant admits 108. One octant per site gives 15024 records (open PR 8743). The three readings are nested: global-octant records are line-field records, and line-field records are per-site records. So static rigidity needs one orientation per axis for the whole core, and orientations attached to sites or to lines leave the letters flexible. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/relational_letters_static_rigidity_needs_a_global_octant_line_orientations_are_flexible_2026_09_23.py
---

# Relational letters: static rigidity needs a global octant; site and line orientations leave the letters flexible

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8743 proved that under the static
reading of open PR 8691 every static record of the seven relational
letters is a spiral. It found that the rigidity uses the reading's fixed
octant: when each core site may choose its own octant, the core of side 2
has 15024 records. This block asks how much orientation the reading has to
supply.

## Result up front

1. **A global octant is enough.** Orient every lattice line along an axis
   alike. Each of the 8 octants then gives exactly the 12 spirals aligned
   with it. The 4 opposite pairs give 48 distinct records, all spirals.

2. **Orienting each lattice line is not enough.** Give each of the 12
   lines through the core its own orientation, so each core site takes
   its octant from its three lines. Over all 4096 such fields:
   - there are 11136 records, of which 48 are spirals;
   - 1300 fields admit records;
   - one field that is not a global octant admits 108.

3. **Orienting each site is not enough either.** One octant per site gives
   15024 records (open PR 8743).

4. **The readings are nested.** Every global-octant record is a line-field
   record, and every line-field record is a per-site record. Supplying
   orientation to sites or to lines therefore leaves the letters flexible.
   Rigidity needs one orientation per axis for the whole core.

5. **What this means for the frame.** Under the static reading, the
   relational letters fix the frame only once the reading supplies a
   global octant: an orientation for each axis, a body diagonal. That is
   supplied structure, like a time direction. In the decision structure it
   belongs to the reading, and it enters gravity's unsoldered set under
   possibility covariance, {alphabet, reading, roles} (open PR 8648, tenth
   edition).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "how much orientation the static reading must supply for relational letters to be rigid (open PR 8743)"
source_of_blocker_text: open_pr_8743
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record on the relational branch: the static reading supplies a global octant; site and line orientations leave the letters flexible"
conditional_surface_status: "seven relational letters; static readings with a supplied global octant, per-line or per-site orientations; core of side 2"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "complete searches over declared orientation fields on a declared core"
```

## Premises and declared objects

- **Letters and completions.** The seven letters in the planar form, as in
  open PR 8743. At a core site with octant σ, the back neighbours are
  x − σ_i e_i and the forward neighbours x + σ_i e_i. The back
  differences and the forward differences must each be a common-sign
  permutation of the angles.
- **Readings.** Three ways of supplying σ:
  - a global octant;
  - a line-orientation field, with one sign for each of the 12 lines
    through the core;
  - an octant chosen freely at each site.
- **Search.** Core of side 2 on the side-4 box, one core value fixed,
  values outside the core free.

## Prior art and what is new

- Open PR 8743: global rigidity with the fixed octant, and the per-site
  contrast.
- New here:
  - the per-line fields, and their counts;
  - the nesting of the three readings;
  - the conclusion that rigidity needs a global octant.

## Theorem — Orientation supply

Two facts come from the search:
- for each global octant, the records are exactly the aligned spirals;
- over all line fields, 11136 records occur, only 48 of them spirals.

Nesting follows from the definitions, and the runner also checks it:
- a line field assigns each site the octant of its lines, so its records
  satisfy the per-site reading;
- a global octant is a line field.

## No-Go Discipline Gate

The negative content is that site and line orientations do not restore
rigidity. It is scoped to the declared core and letters.

- **N1 alternative routes.** The following are outside this block:
  - larger cores;
  - other supplied structures, such as orientations of planes;
  - readings that reach beyond nearest neighbours.
- **N2 wall independence.** Complete searches with record, step and work
  caps.
- **N3 hidden walls.** Each reading's orientation supply is declared.
- **N4 residual matching.** The residual is a global octant, supplied
  with the reading.
- **N5 rhetoric audit.** "Not enough" refers to the declared core and
  readings.
- **N6 partial-closure paths.** Plane orientations; octants registered at
  next-nearest range.
- **N7 steelman.** For local supply: a global octant is itself a line
  field, the constant one. Against: most line fields are flexible. Both
  are recorded.
- **N8 cross-cycle echo.** Open PRs 8648, 8691 and 8743 are cited.

## Falsifiers

Any of the following falsifies the theorem:
- a global octant with records other than the 12 aligned spirals;
- a line-field count other than 11136, or other than 48 spirals;
- a line-field record that is not a per-site record.

## Boundaries and non-claims

- The declared core, letters and readings.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PRs 8648, 8691 and 8743 and the landed possibility-covariance note are
cited. No audit grade, no new axiom, no new primitive, no new comparator and
no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the per-site count is reproduced from open PR 8743;
  - alignment is checked against the octant's sign pattern;
  - nesting is checked record by record.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| site octant read from the wrong lines | axis index shifted | caught (1 FAIL) |
| line-field search with back completions only | forward side dropped | caught (3 FAILs) |
| alignment ignores the sense | one sense only | caught (1 FAIL) |
| only global fields searched | 4096 fields to 8 | caught (1 FAIL) |
| spiral test drops an axis | three axes to two | caught (2 FAILs) |
| per-site search with one octant | eight octants to one | caught (1 FAIL) |
| angles that are not Sidon | (1, 2, 4) to (1, 2, 3) | caught (3 FAILs) |

  All 7 are caught; each mutant runs in parallel with two others.

- **Vacuity guard:** counts of fields, records and spirals are printed.
- **Budget:** 3 checks, stdout 829 characters (ceiling 6000), about 176 s
  (ceiling 900 s). The searches stop at record, step and work caps set
  about three times what the true run uses.

## Verification

```bash
python3 scripts/relational_letters_static_rigidity_needs_a_global_octant_line_orientations_are_flexible_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=3 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/relational_letters_static_rigidity_needs_a_global_octant_line_orientations_are_flexible_2026_09_23.txt`.
