---
claim_id: relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Qubit possibilities as rational Bloch-sphere points; possibility covariance read as the independent internal rotation action of the landed possibility-covariance note, together with the unsoldered lattice reading. Fixed coordinate letters are then unavailable, but relational ones exist: spiral records b(x) = R_n(t . x) b0 with three Pythagorean angles are stationary records of a covariant unsoldered rule in a sweep (unique outputs on a 4-box, for a spiral and a rotated spiral); the rule is symmetric in its inputs and commutes with rotations of the sphere; every core site reads each neighbour's bond direction from the rotation between their values; under the static reading each core site is the unique covariant completion of its back or forward neighbours. At a first formation a lone child's law is symmetric about its parent's value, its only atoms are the poles, and two stationary spirals agree at a parent and differ at its child, so after the first lone child each lone child reaches its spiral value with probability 0. Rigidity (every stationary record a spiral) is not established. No reading, rule, alphabet or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_2026_09_22.py
---

# Relational frames in one qubit: spiral records under possibility covariance

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Coordinate letters (open PR 8676) are one
of the two frame sources behind every route to gravity (open PR 8648,
fourth edition). The Qubit axiom says "No possibility is privileged.
Possibilities are distinguished by the supplied algebraic structure
alone." Read as possibility covariance, a rule must commute with every
rotation of the Bloch sphere, so it cannot give 320 fixed points a
special status. This block asks whether the frame can still live in one
qubit's own possibilities.

## Result up front

1. **Fixed letters go; relational letters stay.** Under possibility
   covariance, 320 fixed points cannot serve as letters. Spiral records
   can: b(x) = R_n(t . x) b0, built from three rotations about one axis
   by Pythagorean angles with (cos, sin) = (3/5, 4/5), (5/13, 12/13) and
   (8/17, 15/17). The six signed angles are distinct, and the positive
   ones obey the plaquette lemma.

2. **Spirals are stationary in a sweep.** The spiral rule works as
   follows:
   1. It reads a great circle and its two orientations from three
      back-neighbour values.
   2. It returns the unique point that each value reaches by one of the
      three rotations.
   3. It records nothing if there is no such point.

   The rule is symmetric in its inputs, so it is unsoldered, and it
   commutes with every rotation of the sphere. On a 4x4x4 box, every site
   with three back-neighbours equals the rule's unique output, both for a
   spiral and for a spiral rotated by a rational rotation about another
   axis.

3. **The record carries the frame.** At every core site, the rotation
   taking its value to each neighbour's value is one of the six signed
   angles, and that angle names the bond direction. From there the
   emulation of soldered rules, which reads only bond directions, goes
   through as in open PRs 8676 and 8679. The ice-support readout and the
   role letters of those pull requests use absolute coordinate labels,
   which a spiral record does not carry: every core site of a static
   spiral sees the same differences to its neighbours (open PR 8743).
   Under the static reading each
   core site is the unique covariant completion of its three back
   neighbours, and also of its three forward neighbours (with the
   orientation reversed).

4. **First formations miss it.** A lone child sees only its parent, so
   its law must be symmetric about the parent's value. Such a law has
   atoms only at the parent's two poles, and spiral values are never
   there. Two stationary spirals that agree at a parent can differ at its
   child (checked exactly). So after the first lone child, whose azimuth
   is only a global rotation, each lone child reaches its required spiral
   value with probability 0. Registration at a first formation fails
   almost surely; sweeps have no lone children.

5. **What moves in the decision structure.** Under possibility
   covariance, the alphabet routes to gravity survive inside the qubit's
   own possibility domain, and exactly where the assembly already puts
   them: the sweep ({alphabet, order law}) and the static reading
   ({alphabet, reading}). With relational letters alone, roles are then
   supplied, since a relational record carries no role pattern (open PR
   8743). The first-formation prices of open PR 8676 need
   fixed letters: 2/9 in corner growth, certainty in a designed order.
   Under possibility covariance both drop to zero, since both orders grow
   by lone children. Two things are not established here: whether every
   stationary sweep record is a spiral, and whether finitely many
   possibilities suffice (these spirals take infinitely many values).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "coordinate letters (open PR 8676) use fixed possibilities; under possibility covariance ('no possibility is privileged' read as rotation covariance of the rule) determine whether one qubit's possibilities can carry the lattice frame"
source_of_blocker_text: minimal_axioms_qubit_sentence_and_open_pr_8676
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record the reading split on the alphabet decision (fixed letters without possibility covariance; relational spirals with it, sweep or static only); test rigidity of stationary spiral records"
conditional_surface_status: "possibility covariance as the supplied independent internal rotation action; unsoldered lattice reading; declared spiral rule and angles; declared box"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "exact rational geometry on declared records and windows, plus a short symmetry argument for lone children"
```

## Premises and declared objects

The Qubit axiom's sentences quoted above. The landed possibility-covariance
note supplies, without adopting it, the independent internal action: rotations of
the Bloch sphere acting on all values at once. This block reads "No
possibility is privileged" as covariance of the rule under that action,
R(h.config) = h_* R(config), together with the unsoldered lattice reading.

Declared objects:
- rational Bloch-sphere points;
- the three Pythagorean angles and the spiral records built from them;
- the spiral rule;
- the sweep and the static reading;
- first formations with lone children.

## Prior art and what is new

- The landed possibility-covariance note counts invariants and covariants
  under the independent internal action. It notes that recorded content
  can supply a lattice-to-internal map covariantly where a certain matrix
  is invertible, but it does not construct a formation law. New here: a
  covariant formation rule whose stationary records carry that map.
- Open PR 8676 builds registered frames with fixed coordinate letters.
  New here: relational letters under possibility covariance, and the
  loss of the first-formation price.
- Pythagorean rotations and the Rodrigues formula are standard
  mathematics.

## Theorem 1 — Spiral records are stationary and carry the frame

The rule's great circle is the unit normal of w_0 x w_1. It is rational
here because the angle differences have rational sines. The rule checks
all six assignments and both orientations, and exactly one candidate
survives. That uniqueness uses the distinctness of the six signed angles
and the plaquette lemma, checked over 81 cases.

On the box, every site with three back-neighbours equals the rule's
output. This holds for the spiral and for the rotated spiral, which
checks that the rule commutes with rotations of the sphere. The output
does not change when the inputs are permuted.

Every core site reads each of its six neighbours' bond directions as the
unique signed angle between their values.

## Theorem 2 — First formations

Let a lone child's only formed neighbour have value p. Possibility
covariance makes the child's law invariant under rotations about p, so
its atoms lie in {p, -p}. The rotation of the whole spiral by a
Pythagorean angle about p is again a stationary spiral: it agrees at the
parent and differs at the child (checked). The required child values are
never at the poles (checked). So once the global rotation is used up by
the first lone child, each further lone child reaches its required value
with probability 0.

## No-Go Discipline Gate

The negative content is scoped. Under possibility covariance with one
qubit per site, spiral registration at a first formation fails almost
surely.

- **N1 alternative routes.** Two things are not classified: relational
  schemes other than spirals, and formation units of several qubits,
  which offer more room.
- **N2 wall independence.** Exact rational geometry and a symmetry
  argument; no dynamics.
- **N3 hidden walls.** Possibility covariance is a declared reading. The
  landed note does not adopt it, and without it fixed letters work as in
  open PR 8676.
- **N4 residual matching.** The alphabet decision now carries a reading
  split: fixed letters without possibility covariance, relational spirals
  with it.
- **N5 rhetoric audit.** "Fails" refers only to spiral registration at
  first formations under possibility covariance.
- **N6 partial-closure paths.** Rigidity of stationary spiral records;
  multi-qubit units.
- **N7 steelman.** Against relational letters: rigidity is not shown, and
  first formations are closed to them. For them: they need no privileged
  possibility, and they work exactly where the gravity routes already
  sit.
- **N8 cross-cycle echo.** Open PRs 8670, 8676, 8679 and 8648 and the
  landed note are cited.

## Falsifiers

- A box site on a spiral whose value is not the rule's unique output.
- A pair of angles violating the lemma.
- A core site whose neighbour rotation is not the labelled signed angle.
- A covariant lone-child law with an atom at a spiral value.

## Boundaries and non-claims

No reading, rule, alphabet or order law is adopted. Possibility
covariance is taken as a declared reading of the Qubit sentence.
Rigidity is not established. Nothing here grades, unlocks or audits any
other claim.

## Imports

The Qubit and Admissibility text and the landed note are cited.
Pythagorean rotations and the Rodrigues formula are standard. No audit
grade, no new axiom, no new primitive, no new comparator and no new
framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the spiral is built by complex multiplication, and the rule works by
    Rodrigues rotations;
  - rotated spirals test covariance through an independent axis;
  - the twin spiral is built about the parent's own value.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| second angle not a unit rotation | 12/13 to 11/13 | caught (3 FAILs) |
| two equal angles | third angle set to the first | caught (3 FAILs) |
| rule tries one orientation only | orientations cut | caught (4 FAILs) |
| rule tries one assignment only | assignments cut | caught (1 FAIL) |
| Rodrigues drops the axial term | term removed | caught (5 FAILs) |
| spiral steps backwards along z | sign flipped | caught (5 FAILs) |
| frame read without the sine sign | sign dropped | caught (1 FAIL) |
| twin rotation about another axis | parent axis to z | caught (1 FAIL) |
| global rotation not a rotation | axis not unit | caught (4 FAILs) |
| rule skips the great-circle test | guard removed | missed; diagnosed non-defect (a rotation about n keeps a point's height, so the consistency test already rejects off-circle inputs) |

  Nine of nine defect mutants are caught; the tenth removes a redundant
  guard.

- **Vacuity guard:** every stationarity and readout check runs over all
  sites of the declared box or core.
- **Budget:** 7 checks, stdout 1402 characters (ceiling 6000), under a
  second (ceiling 900 s), exact Fractions.

## Verification

```bash
python3 scripts/relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=7 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_2026_09_22.txt`.
