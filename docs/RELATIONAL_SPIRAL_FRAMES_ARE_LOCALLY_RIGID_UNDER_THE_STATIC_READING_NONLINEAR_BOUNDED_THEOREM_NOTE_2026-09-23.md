---
claim_id: relational_spiral_frames_are_locally_rigid_under_the_static_reading_nonlinear_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The static relations of open PR 8691 on 4- and 5-boxes: each core site's value b(x) and axes n_b(x), n_f(x) with unit lengths, n . b = 0, b(x - e_i) = R_nb(-theta_i) b(x) and b(x + e_i) = R_nf(theta_i) b(x), for the Pythagorean angles (3/5, 4/5), (5/13, 12/13), (8/17, 15/17). Linearised at the spiral b(x) = R_z(theta . x) b0 with all axes z, the full system has nullity exactly 5 (exact kernel vectors with a modular rank bound): the phase, the two tilts, and a turn of the back axis at one core corner and of the forward axis at the other. Exact nonlinear solutions realise all five directions: rational rotations of the whole record, and rational turns of either corner axis with that corner's three outer neighbours rotated along. The family's tangent vectors at the spiral are the kernel vectors, so by the implicit function theorem every static solution near the spiral is a rotated spiral up to the two corner axes. Local, on the declared boxes; the sweep reading is flexible (open PR 8717). No reading, rule, alphabet or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/relational_spiral_frames_locally_rigid_under_the_static_reading_nonlinear_2026_09_23.py
---

# Relational spiral frames are locally rigid under the static reading

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8691 left open whether every
stationary record near a relational spiral is a spiral. Open PR 8717
answered this at linear order:
- under the static reading, only the global tilts and two corner axes
  move;
- under the sweep, the record is flexible, and boundary errors are
  amplified.

This block lifts the static answer to the full nonlinear relations.

## Result up front

1. **The linearised static system has nullity exactly 5.** The unknowns
   are values on the used sites and back and forward axes at the core
   sites, with every unit-length and orthogonality constraint and every
   relation. On 4- and 5-boxes the kernel is spanned by five exact
   vectors:
   - the phase (rotation about z);
   - the two tilts (rotations about x and y);
   - a turn of the back axis at the core corner (1, 1, 1);
   - a turn of the forward axis at the opposite core corner.

2. **Exact nonlinear solutions realise all five.** The following are
   exact stationary records under every static relation:
   - rotations of the whole record by (3/5, 4/5) about x, y or z;
   - a turn of either corner axis by (5/13, 12/13), with that corner's
     three outer neighbours rotated along, moving exactly those three
     values.

   Their tangent vectors at the spiral are the five kernel vectors.

3. **So the static spiral is locally rigid.** By the implicit function
   theorem, the solution set near the spiral is a 5-dimensional manifold,
   and the family fills it. Every static solution close to the spiral is
   therefore a rotated spiral, up to the axis at each core corner.

4. **What this means for relational frames.** The static reading holds a
   relational frame rigidly: nothing near the spiral but a global rotation
   changes the core. The sweep does not (open PR 8717). This is where the
   assembly's {alphabet, reading} route carries relational letters.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "rigidity of stationary spiral records is not established (open PR 8691); linear only (open PR 8717)"
source_of_blocker_text: open_prs_8691_8717
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record on the relational-letter branch: the static reading is locally rigid (nonlinear) on declared boxes"
conditional_surface_status: "possibility covariance and the unsoldered reading as in open PR 8691; the declared spiral, angles and static relations; 4- and 5-boxes; local near the spiral"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "an exact nullity with a modular rank bound, exact nonlinear solution families, and the implicit function theorem"
```

## Premises and declared objects

- **Open PR 8691's spiral and angles.** b(x) = R_z(θ . x) b0 with
  (cos θ_j, sin θ_j) = (3/5, 4/5), (5/13, 12/13) and (8/17, 15/17).
- **Its static reading.** Each core site x completes from its
  back-neighbours with an axis n_b(x) and from its forward neighbours with
  an axis n_f(x). Here:
  - n_b . b = n_f . b = 0;
  - b(x - e_i) = R_nb(-θ_i) b(x);
  - b(x + e_i) = R_nf(θ_i) b(x);
  - values and axes are unit vectors.

  Near the spiral the assignment of angles to directions is the spiral's
  own.
- **Boxes.** Core sites have coordinates 1..L-2. Used sites are the core
  sites and their six neighbours.
- **The Rodrigues formula.**
  R_n(a) v = cos a v + sin a (n × v) + (1 - cos a)(n . v) n.

## Prior art and what is new

- Open PR 8691: the spiral, the rule, the static completion, rigidity
  open.
- Open PR 8717: linear rigidity under the static reading, flexibility and
  amplification under the sweep, and lattice rigidity.
- Standard: the implicit function theorem, the Rodrigues formula.
- New here: the full static nullity, the exact nonlinear families and
  their tangents, and local nonlinear rigidity.

## Theorem — Local rigidity

Write the static system as F = 0 on the space of values and axes, with
n unknowns. At the spiral p:
- rank DF(p) = n - 5;
- the five kernel vectors are exact.

The map from SO(3) × (back corner turn) × (forward corner turn) to
records is smooth and sends the identity to p. Its image lies in F = 0.
Its derivative at the identity has rank 5, and its columns are the kernel
vectors. So near p the image is a 5-dimensional submanifold M inside
F = 0.

Choose n - 5 components of F with independent gradients at p. Their zero
set N is a 5-dimensional manifold near p, and it contains F = 0, which
contains M. A 5-dimensional submanifold of a 5-dimensional manifold is
open in it. So near p, M = N = {F = 0}.

The corner turns are free because each corner's three outer neighbours
lie in that corner's relation and in no other.

## No-Go Discipline Gate

The negative content is scoped. Under the static reading on the declared
boxes, no solution near the spiral other than the stated family exists.

- **N1 alternative routes.** The following are outside this block:
  - solutions far from the spiral;
  - larger boxes, although the linear count of open PR 8717 extends to
    6-boxes;
  - other angle triples.
- **N2 wall independence.** An exact nullity, exact solutions and a
  standard theorem.
- **N3 hidden walls.** The theorem is local; the neighbourhood size is
  not computed.
- **N4 residual matching.** The relational branch's residual is the
  sweep's flexibility, and first formations (open PRs 8691, 8717).
- **N5 rhetoric audit.** "Rigid" means local, on the declared boxes, up
  to the stated family.
- **N6 partial-closure paths.** Global rigidity on boxes; the infinite
  lattice.
- **N7 steelman.** For relational frames: the static reading holds them
  rigidly. Against them under formation: sweeps are flexible and
  amplify errors, and first formations miss them. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8691 and 8717 are cited; the linear
  kernel agrees with open PR 8717's static count.

## Falsifiers

Any of the following falsifies the theorem:
- a sixth independent exact kernel vector on a declared box;
- a family member that fails a relation;
- a tangent vector that is not the stated kernel vector.

## Boundaries and non-claims

- Local near the spiral, on 4- and 5-boxes.
- No reading, rule, alphabet or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PRs 8691 and 8717 and the landed possibility-covariance note are
cited. The implicit function theorem and the Rodrigues formula are
standard mathematics. No audit grade, no new axiom, no new primitive, no
new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the kernel vectors are written as rotations and corner turns and
    checked against the linear rows;
  - the nonlinear families are checked against the exact relations;
  - the corner tangents come from a first-order Rodrigues expansion,
    independent of the linear rows.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutant | change | outcome |
|---|---|---|
| forward relations use the back axis | n_f to n_b | caught (2 FAIL) |
| forward rotation with the back sign | +s to -s | caught (2 FAIL) |
| orthogonality rows dropped | n . b rows removed | caught (2 FAIL) |
| one corner kernel vector dropped | forward corner removed | caught (1 FAIL, then a nonzero exit) |
| corner outer neighbours with the wrong sign | d s_i to -d s_i | caught (2 FAIL) |
| rotation family not a rotation | (3/5, 4/5) to (3/5, 3/5) | caught (1 FAIL) |
| corner family skips an outer neighbour | three neighbours to two | caught (1 FAIL) |
| first-order Rodrigues term altered | (1 - c) to (1 + c) plus an extra term | caught (1 FAIL) |
| rank skips a column block | continue to break | caught (2 FAIL) |

9 of 9 caught.

- **Vacuity guard:** unknowns, equations, nullities and ranks are printed
  for each box.
- **Budget:** 3 checks, stdout 1073 characters (ceiling 6000), about
  1 s (ceiling 900 s), exact Fractions.

## Verification

```bash
python3 scripts/relational_spiral_frames_locally_rigid_under_the_static_reading_nonlinear_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=3 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/relational_spiral_frames_locally_rigid_under_the_static_reading_nonlinear_2026_09_23.txt`.
