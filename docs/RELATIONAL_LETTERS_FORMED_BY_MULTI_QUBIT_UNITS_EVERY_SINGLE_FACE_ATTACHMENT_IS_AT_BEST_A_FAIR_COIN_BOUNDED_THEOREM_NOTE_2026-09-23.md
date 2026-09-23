---
claim_id: relational_letters_formed_by_multi_qubit_units_every_single_face_attachment_is_at_best_a_fair_coin_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Relational spiral letters (open PRs 8691, 8729) formed by 2 x 2 x 2 joint units under possibility covariance and proper lattice covariance, in the planar form of spiral records (angles modulo 12 in units of 30 degrees, angles (30, 60, 150) degrees), with each unit's law depending only on its formed neighbours, as a lone child's does in open PR 8691. A unit extending the formed region through one face sees (A0, A0 + alpha, A0 + beta, A0 + alpha + beta) and adds one step t per layer. Reversing the circle (a sphere rotation) sends the view to (-A0, -alpha, -beta) and negates the correct step; the half turn about the growth axis sends it to (A0 + alpha + beta, -alpha, -beta) and keeps it; the two views differ by a circle rotation, checked for all 24 proper orientations, both circle orientations and all three axes. So a covariant rule gives the steps t and -t equal probability at every single-face view: no deterministic covariant rule continues, and each single-face attachment is right with probability at most 1/2. Any growth reaching n units along each axis makes at least 3(n - 1) single-face attachments (exactly 3(n - 1) in corner growth), so registration has probability at most 2^(-3(n - 1)); the covariant fair coin over the sign of the missing angle attains it (exactly 1/64 on a 3 x 3 x 3 grid of units). Copying an in-face sign keeps the reversal and breaks the half turn; treating the face as the back side does the opposite; they register the frame in 12 and 6 of the 48 first-unit patterns. A unit that also reads two layers back, outside local formation, registers the frame in all 48. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/relational_letters_multi_qubit_units_single_face_attachment_is_a_fair_coin_2026_09_23.py
---

# Relational letters formed by multi-qubit units: every single-face attachment is at best a fair coin

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8691 showed that under possibility
covariance a lone child, which sees only its parent, misses its spiral
value almost surely, so relational frames fail at a first formation. It
asked whether formation units of several qubits offer more room. This
block answers for 2 x 2 x 2 units whose law, like a lone child's, depends
only on their formed neighbours: not enough.

## Result up front

1. **A single face cannot tell which way the frame runs.** A unit that
   extends the formed region through one face has only that face's four
   values as formed neighbours. In the planar form of a spiral (open PR
   8729), its continuation adds one step t per layer. Two symmetries act
   on the view:
   - Reversing the great circle is a rotation of the sphere. It negates
     the view and must negate the step.
   - The half turn of the lattice about the growth axis permutes the face.
     It must keep the step, since the continuation along the axis is
     unchanged.

   The two resulting views differ only by a rotation of the circle, which
   leaves the step alone. The runner checks this for all 24 proper
   orientations, both circle orientations and all three axes.

2. **So a covariant rule is at best a fair coin.** At every single-face
   view, a covariant rule gives the steps t and -t equal probability. No
   deterministic covariant rule can continue, and a randomised one is
   right with probability at most 1/2 at each single-face attachment.

3. **Growth needs many single-face attachments.** Every unit that pushes
   the formed region to a new extent along an axis touches it through one
   face. So reaching n units along each axis takes at least 3(n - 1)
   single-face attachments; corner growth takes exactly that many.
   Registration has probability at most 2^(-3(n - 1)), which tends to 0.
   The covariant fair coin, which draws the sign of the missing angle,
   attains the bound: exactly one of its 64 sign draws registers a
   3 x 3 x 3 grid of units, for each of the 48 first-unit patterns.

4. **Each covariance matters.** Two deterministic rules each keep one
   covariance and break the other:
   - copying an in-face sign commutes with the reversal but not with the
     half turn;
   - treating the face as the back side commutes with the half turn but
     not with the reversal.

   Each is right on 72 of the 144 single-face views. They register the
   frame in 12 and 6 of the 48 first-unit patterns.

5. **The nearest-neighbour premise matters too.** A unit that also reads
   the site two layers back sees the step along the growth axis. The step
   it reads is the pattern's own step, so this reader keeps both
   covariances, and it registers the frame in all 48 patterns. That read
   reaches outside the unit's formed neighbours, so it is outside local
   formation (the criterion of open PRs 8715 and 8720).

6. **What this means for relational frames.** Under possibility covariance
   and local formation, first formations fail for single sites (open PR
   8691) and, on large windows, for 2 x 2 x 2 units. Relational frames are
   carried by either of two routes:
   - sweeps without a first formation, with exact boundary data (open
     PR 8717);
   - the static reading, where they are rigid (open PRs 8717, 8724), with
     seven letters enough (open PR 8729).

   Formation that also reads two layers back continues them from a first
   unit (checked).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "whether formation units of several qubits rescue relational frames at a first formation (open PR 8691)"
source_of_blocker_text: open_pr_8691
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record on the relational-letter branch: under local formation, bounded units do not rescue first formations; sweeps without a first formation, the static reading and two-layer formation reads remain"
conditional_surface_status: "possibility covariance and proper lattice covariance; relational spiral letters in planar form; 2 x 2 x 2 units attaching through faces, each unit's law depending only on its formed neighbours"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "an exact symmetry argument checked over all orientations, a counting bound on attachments, and exact growth runs"
```

## Premises and declared objects

- **Relational spiral letters.** Values on one great circle with neighbour
  steps from the angles (30, 60, 150) degrees. The planar form uses angles
  modulo 12 in units of 30 degrees; for spiral inputs every fit is a
  congruence (open PR 8729).
- **Covariance.** The rule commutes with rotations of the sphere,
  including the reversal of a great circle. It also commutes with proper
  rotations of the lattice, including the half turn about a growth axis.
- **Units.** Blocks of 2 x 2 x 2 sites, formed jointly. The first unit
  carries the spiral pattern under one of the 24 proper lattice
  orientations and either circle orientation. Later units attach through
  faces.
- **Locality.** A unit's law depends only on its formed neighbours, the
  formed sites adjacent to its sites. This is the unit form of the local
  formation criterion (open PRs 8715, 8720) and matches the lone child of
  open PR 8691.
- **Growth.** Corner growth over an n x n x n grid of units. A unit with
  two or three formed faces reads the step along each growth axis from
  another formed face. A unit with one formed face takes its step from
  the rule under test.

## Prior art and what is new

- Open PR 8691: lone children miss spiral values, and the question of
  multi-qubit units.
- Open PRs 8717, 8724 and 8729: rigidity and finite relational letters.
- Open PRs 8715 and 8720: the local formation criterion and joint cell
  units for the ice measure.
- New here:
  - the reversal–half-turn equivalence of single-face views;
  - the fair-coin bound and its attainment;
  - the attachment count;
  - the controls: which covariance each deterministic rule breaks, and
    the two-layer read.

## Theorem 1 — The fair-coin bound

For a face view F and a step s, let U_s(F) be the continuation that adds
s per layer. Let P_F be the rule's law given the view F. Let h be the
half turn about the growth axis. Let ρ be the reversal of the circle
followed by a rotation of the circle by c = 2A0 + α + β.

- The half turn maps F to hF and U_s(F) to U_s(hF). So
  P_hF(U_s(hF)) = P_F(U_s(F)).
- The rotation ρ also maps F to hF, but it maps U_s(F) to U_-s(hF). So
  P_hF(U_-s(hF)) = P_F(U_s(F)).

So at the view hF the continuations with steps s and -s are equally
likely. Every view is hF for some pattern, and the half-turned pattern
keeps the step. The correct step t is ±θ with θ in {1, 2, 5}, which is
never its own negative modulo 12. So the correct continuation has
probability at most 1/2, and a deterministic law would need t = -t.

## Theorem 2 — Attachments

Take a unit that extends the formed region's span along an axis: it
reaches a new maximum or a new minimum there. Every formed unit lies
strictly on one side of it along that axis. So it can touch the formed
region only through the face on that side. Reaching n units along each
axis therefore takes at least n - 1 such attachments per axis. Each is
right with probability at most 1/2 given that everything before it is
right. By the chain rule, registration has probability at most
2^(-3(n - 1)).

## No-Go Discipline Gate

The negative content is scoped: possibility covariance, local formation,
relational spiral letters, 2 x 2 x 2 units attaching through faces.

- **N1 alternative routes.** The following are outside this block:
  - formation reads beyond the formed neighbours, which continue the
    frame (checked);
  - units whose attaching faces lack the half-turn symmetry;
  - growing unit sizes;
  - fixed letters without possibility covariance (open PR 8676).
- **N2 wall independence.** Exact symmetry checks, a counting argument,
  and growth runs with each premise dropped in turn.
- **N3 hidden walls.** Both covariances and the locality premise are
  declared. Each is shown to matter by a control that drops it.
- **N4 residual matching.** The relational branch's residual under local
  formation is sweeps without a first formation.
- **N5 rhetoric audit.** "At best a fair coin" refers to single-face
  attachments of the declared units under the declared premises.
- **N6 partial-closure paths.** Two-layer formation reads; units with
  asymmetric faces; attachments through several faces from the start.
- **N7 steelman.** For units:
  - a rule that breaks one covariance registers from 1/4 or 1/8 of the
    first-unit patterns;
  - a two-layer read registers from all of them.

  Against units: covariant local rules cannot, on large windows. All of
  these are recorded.
- **N8 cross-cycle echo.** Open PRs 8676, 8691, 8715, 8717, 8720, 8724 and
  8729 are cited.

## Falsifiers

Any of the following falsifies the theorems or their controls:
- a covariant local rule whose law is not symmetric in the step at some
  single-face view;
- corner growth of n units with fewer than 3(n - 1) single-face
  attachments;
- a fair-coin registration count other than one of 64 draws;
- control counts other than 12, 6 and 48.

## Boundaries and non-claims

- The declared units, growth, angles and premises.
- The two-layer read is recorded as a control, not proposed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PRs 8676, 8691, 8715, 8717, 8720, 8724 and 8729 and the landed
possibility-covariance note are cited. No audit grade, no new axiom, no
new primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the half-turned views are read off the rotated pattern directly, not
    from the formula;
  - the attachment count is checked against the closed form and against
    the calls a growth run makes;
  - the covariance of each control is checked on the reversed and
    half-turned views directly;
  - the growth runs use exact modular arithmetic.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| half turn misses one coordinate | face (1 - u, 1 - v) to (1 - u, v) | caught (2 FAILs) |
| reversal keeps the values | -v to v | caught (3 FAILs) |
| a step that is its own negative | angles (1, 2, 5) to (1, 2, 6) | caught (5 FAILs) |
| improper orientations included | parity filter removed | caught (5 FAILs) |
| attachment count includes corner units | one positive coordinate to at most two | caught (2 FAILs) |
| copy rule negates the sign it copies | s to -s | caught (1 FAIL) |
| continuation ignores the layer | (layer + 1) t to t | caught (3 FAILs) |
| multi-face step read with the wrong sign | forward difference reversed | caught (3 FAILs) |
| two-layer reader reads an in-face step | growth axis to an in-face axis | caught (1 FAIL) |
| fair coin ignores its draws | sign draw removed | caught (1 FAIL) |
| views drop one growth axis | three axes to two | caught (2 FAILs) |
| back rule copies the second in-face sign | + to the in-face sign | caught (2 FAILs) |
| signed angles read with one sign only | signs (1, -1) to (1) | caught (4 FAILs) |

  All 13 are caught. One further mutant is equivalent: copying the
  other in-face sign. Either copy is right exactly when the pattern's
  three axis signs agree, so both give the same 12 patterns, and both
  keep the reversal and break the half turn.

- **Vacuity guard:** view counts, attachment counts, draw counts and win
  counts are printed.
- **Budget:** 7 checks, stdout 2314 characters (ceiling 6000), about a
  second (ceiling 900 s), exact modular arithmetic. The fair-coin check
  runs only when the growth's attachment count matches the closed form.

## Verification

```bash
python3 scripts/relational_letters_multi_qubit_units_single_face_attachment_is_a_fair_coin_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=7 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/relational_letters_multi_qubit_units_single_face_attachment_is_a_fair_coin_2026_09_23.txt`.
