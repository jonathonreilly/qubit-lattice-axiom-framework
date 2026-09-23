---
claim_id: relational_spiral_frames_are_rigid_on_the_lattice_and_under_the_static_reading_but_flexible_and_amplified_under_the_sweep_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Spiral records of open PR 8691 (b(x) = R_z(theta . x) b0 with Pythagorean angles (3/5, 4/5), (5/13, 12/13), (8/17, 15/17)), linearised in the stationarity relations of its sweep rule: each site's value and its three back-neighbours lie on one great circle with axis n(x), and b(x - e_i) = R_n(x)(-theta_i) b(x). In plane only the constant phase solves. Out of plane, with a the value's vertical deviation (sign reversed) and beta the axis tilt along z x b0, the relations read a(x - e_i) = c_i a(x) - s_i beta(x), and every w gives the exact solution a = prod_j (c_j - w s_j)^(-x_j), beta = w a. On L-boxes the linear solutions are exactly the phase and the span of these modes: nullity 3L - 3 for L = 3, 4, 5 (exact rational solutions with a modular rank bound). On Z^3 a mode is bounded only if |c_j - w s_j| = 1 for every j; each such circle is |w|^2 - 2 cot(theta_j) Re w = 1, so the three meet only at w = +-i, whose modes are the two global tilts; bounded linear deformations on the lattice are global. Along the sweep a consistent back-boundary perturbation propagates uniquely as its modes, which grow by 1/|c_j - w s_j| per step (5/3, 13/5, 17/8 at w = 0; 5, 13, 34 at w = 1/2); a generic perturbation violates the rule's three conditions per site. Under the static reading, where each core site completes from its back-neighbours and from its forward neighbours, the out-of-plane solutions on 4-, 5- and 6-boxes are the two global tilts and a free axis at each of the two core corners (nullity 4, exact solutions with a modular rank bound); only the tilts move core sites, so the static reading is rigid on boxes. Linear order only. No reading, rule, alphabet or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/relational_spiral_frames_linear_rigidity_on_the_lattice_and_sweep_amplification_on_boxes_2026_09_23.py
---

# Relational spiral frames: rigid on the lattice and under the static reading, flexible and amplified under the sweep

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8691 showed that under possibility
covariance one qubit can still carry the lattice frame: spiral records
are stationary under a covariant, unsoldered sweep rule, and neighbours
read bond directions from the rotation between their values. It left
rigidity open: whether every stationary record near a spiral is a spiral.
This block answers that at linear order.

## Result up front

1. **The linearisation splits in two.**
   - In plane, a phase ψ must satisfy ψ(x - e_i) = ψ(x). Only a constant
     phase does.
   - Out of plane there are two unknowns. Let a be the value's vertical
     deviation, sign reversed, and β the axis tilt along z × b0. They must
     satisfy a(x - e_i) = c_i a(x) - s_i β(x). For every number w, an
     exact solution is a = prod_j (c_j - w s_j)^(-x_j) with β = w a.

2. **On boxes the frame is flexible.** On an L-box the linear solutions
   are exactly the phase together with these modes. The dimension is
   3L - 3 for L = 3, 4, 5. It grows with the box, so it is fixed by
   boundary data.

3. **On the lattice it is rigid.** A mode stays bounded in every direction
   only if |c_j - w s_j| = 1 for all three j. Each such circle is
   |w|^2 - 2 cot(θ_j) Re w = 1. The cotangents 3/4, 5/12 and 8/15
   differ, so any two circles meet only at w = ±i. The w = ±i modes are
   the two global tilts. So on Z^3 every bounded linear deformation of a
   spiral is a global rotation, together with the phase.

4. **The sweep amplifies consistent errors and stops at generic ones.**
   Any two back-neighbours fix (a(x), β(x)), since
   s_i c_j - c_i s_j = sin(θ_i - θ_j) ≠ 0. So propagation forward is
   unique. A consistent perturbation of the back boundary propagates as
   its modes. Along the sweep these grow by 1/|c_j - w s_j| per step:
   - 5/3, 13/5 and 17/8 at w = 0;
   - 5, 13 and 34 at w = 1/2.

   Other modes decay, for example 5/9, 13/31 and 17/37 at w = 3. Only the
   global tilts stay level. A generic perturbation breaks the rule's three
   conditions per site (one out of plane, two in plane), so the rule
   records nothing there.

5. **The static reading is rigid on boxes.** Under the static reading
   each core site completes from its back-neighbours and from its forward
   neighbours. A mode then needs (s_i + c_i w)/(c_i - s_i w) to agree for
   all three i, which happens only at w = ±i. On 4-, 5- and 6-boxes the
   out-of-plane solutions are the two global tilts and a free axis at each
   of the two core corners. Those corners have no core neighbour behind
   them, or ahead of them. Only the tilts move core sites.

6. **What this means for relational frames.**
   - Every linear deformation keeps each back-neighbour relation a
     rotation by θ_i about the local axis. The bond-direction reading of
     open PR 8691 therefore survives wherever the rule has outputs.
   - On the infinite lattice, spiral records are linearly rigid, and under
     the static reading they are rigid on finite boxes too.
   - A sweep started from boundary data does not heal errors. Consistent
     errors along growing modes are amplified exponentially, and generic
     errors leave unrecorded sites.
   - Together with open PR 8691's first-formation result, this means a
     near-spiral frame registered by formation needs exact boundary data.
     The static reading holds the frame rigidly, which is where the
     assembly's {alphabet, reading} route puts it.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "rigidity of stationary spiral records is not established (open PR 8691)"
source_of_blocker_text: open_pr_8691
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record on the relational-letter branch: rigid on the lattice and under the static reading, flexible under the sweep with amplified boundary errors; nonlinear rigidity remains open"
conditional_surface_status: "possibility covariance and the unsoldered reading as in open PR 8691; the declared spiral, angles and sweep relations; linear order"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "exact linearisation with rational solutions certified by a modular rank bound, and a Fourier argument on Z^3 resting on exact algebraic identities"
```

## Premises and declared objects

- **Open PR 8691's spiral records.** b(x) = R_z(θ . x) b0, with
  (cos θ_j, sin θ_j) = (c_j, s_j) = (3/5, 4/5), (5/13, 12/13) and
  (8/17, 15/17).
- **Its sweep rule.** It reads a great circle from three back-neighbour
  values and returns the unique point that each value reaches by one of
  the three rotations. It records nothing when there is no such point. At
  a stationary record, each interior site x has an axis n(x) with
  n(x) . b(x) = 0 and b(x - e_i) = R_n(x)(-θ_i) b(x). Near a spiral the
  assignment of angles to directions is the spiral's own.
- **Boxes.** Sites have coordinates 0..L-1. Interior sites, with all
  coordinates at least 1, carry the relations; they and their
  back-neighbours are the box sites used.
- **Linear order.** Values and axes are perturbed to first order,
  keeping unit length and n . b = 0.

## Prior art and what is new

- Open PR 8691: the spirals, the rule, stationarity and the frame
  reading, the first-formation result, and rigidity left open.
- The landed possibility-covariance note: the independent internal
  action.
- Standard: the Rodrigues rotation formula, and Fourier analysis of
  constant-coefficient difference equations on Z^3.
- New here: the linearisation, its exact mode family, box flexibility
  under the sweep, lattice rigidity, sweep amplification and static
  rigidity on boxes.

## Theorem 1 — The linearisation

Write R_n(α) v = cos α v + sin α (n × v) + (1 - cos α)(n . v) n, and take
α = -θ_i. At the spiral, n = z and b = b0(x) lies in the plane; let t0 =
z × b0. Perturb b by ψ t0 - a z and n by a b0 + β t0. The radial axis
tilt equals a because n . b = 0 must be kept.

- In the plane, (n . b) vanishes to first order and n × b gains nothing
  in plane from the axis tilt. So ψ(x - e_i) = ψ(x).
- Vertically, the vertical part of n × b is -β, which gives
  a(x - e_i) = c_i a(x) - s_i β(x).

Substituting a = prod_j (c_j - w s_j)^(-x_j) and β = w a satisfies all
three relations identically. The runner checks the full linearisation
directly, with value and axis in R^3 under the unit and orthogonality
constraints. The lifted phase and modes solve it exactly, in rational
arithmetic.

## Theorem 2 — Boxes

On L-boxes with L = 3, 4, 5, the full linearisation has modular nullity
6, 9 and 12. The phase and 25 exact modes (w = k/7, |k| ≤ 12) have
modular rank 6, 9 and 12. Modular rank bounds rational rank from below,
so the rational nullity is at most these numbers. Exact solutions that
are independent modulo the prime are independent over the rationals. So
the rational nullity is exactly 3L - 3. Every linear solution on these
boxes is the phase plus a combination of modes.

## Theorem 3 — The lattice

Take a bounded solution (a, β) on Z^3. It is a tempered distribution,
and its Fourier transform is supported where the 3 × 2 symbol
[e^(-ik_i) - c_i, s_i] has a kernel (A, B).
- If A = 0, then B = 0.
- Otherwise w = B/A must satisfy e^(-ik_i) = c_i - w s_i. For real k this
  means |c_i - w s_i| = 1 for all i.

Now |c - w s|^2 = 1 is equivalent to |w|^2 - 2 (c/s) Re w - 1 = 0, since
c^2 - 1 = -s^2. Two such circles with different c/s give Re w = 0 and
|w| = 1. So the support is k = ±θ. A bounded distribution supported at
two points is a combination of the two plane waves there, which are the
modes at w = ±i. The runner checks that these are the global tilts:
- about the x axis, a = -sin(θ . x), β = -cos(θ . x);
- about the y axis, a = cos(θ . x), β = -sin(θ . x).

In plane, ψ(x - e_i) = ψ(x) forces ψ to be constant.

## Theorem 4 — The sweep

The coefficient pairs (c_i, -s_i) are pairwise independent:
s_i c_j - c_i s_j = sin(θ_i - θ_j) ≠ 0. So any two back-neighbours fix
(a(x), β(x)), and the third must agree. Together with ψ, that gives three
linear conditions per site, the linear form of the rule's conditions: a
common great circle and the angle pattern.

- **Consistent data** propagates uniquely, as its modes, with forward
  growth 1/|c_j - w s_j| per step.
- **Generic data** meets the conditions nowhere, and the rule records
  nothing.

On a 6-box the runner sweeps the w = 1/2 mode's 75 back-boundary values
forward and recovers the mode exactly. It grows by (5 · 13 · 34)^4 from
(1, 1, 1) to (5, 5, 5). Changing one boundary value by 1/1000 breaks the
third relation at the first site that reads it.

## Theorem 5 — The static reading

At a core site, the forward relations read
a(x + e_i) = c_i a(x) + s_i β_f(x), with their own axis tilt β_f. Take a
mode that meets the back relations. The forward relations then need
β_f = a (s_i + c_i w)/(c_i - s_i w) for all three i. Writing w = tan φ,
this is tan(θ_i + φ), and three distinct angles agree only at the fixed
points w = ±i.

On 4-, 5- and 6-boxes the static system has modular nullity 4. It has four
exact solutions, independent modulo the prime:
- the tilt about x, a = -sin(θ . x), with β_b = β_f = -cos(θ . x);
- the tilt about y, a = cos(θ . x), with β_b = β_f = -sin(θ . x);
- a free back-axis at the core corner (1, 1, 1), whose back-neighbours
  lie in no other relation;
- a free forward axis at the opposite core corner.

Only the tilts move core sites, so the static reading is rigid on boxes.

## No-Go Discipline Gate

The negative content is scoped to linear order at the declared spiral:
sweeps do not heal boundary errors.

- **N1 alternative routes.** The following are outside this block:
  - nonlinear stationary records;
  - rules other than open PR 8691's;
  - other angle triples;
  - other windows.
- **N2 wall independence.** Exact rational solutions, modular rank
  bounds and algebraic identities.
- **N3 hidden walls.** The Fourier step uses boundedness on the whole
  lattice; boxes have no such condition.
- **N4 residual matching.** The relational branch's residual is exact
  boundary data or a mechanism that removes growing modes.
- **N5 rhetoric audit.** "Rigid" means linear and bounded on Z^3;
  "flexible" means linear on boxes.
- **N6 partial-closure paths.** Nonlinear rigidity; decaying-mode
  selection by a boundary law.
- **N7 steelman.** For relational frames: the lattice spiral is
  linearly rigid, the static reading is rigid on boxes, and the angle
  reading survives every linear deformation. Against registration by formation: the sweep amplifies
  consistent boundary errors exponentially and stops at generic ones.
  Both are recorded.
- **N8 cross-cycle echo.** Open PR 8691 is cited; the spiral and the
  relations are its own.

## Falsifiers

- An exact rational solution of the full linearisation on a declared box
  outside the span of the phase and the modes falsifies Theorem 2.
- A bounded non-global solution on Z^3 falsifies Theorem 3.
- A static solution on a declared box that moves a core site and is not
  a tilt falsifies Theorem 5.
- A mode that fails the relations, or growth factors other than those
  stated, falsify Theorems 1 and 4.

## Boundaries and non-claims

- Linear order only. Whether non-spiral stationary records exist at
  finite amplitude is not decided.
- The rule's behaviour far from a spiral is not analysed.
- No reading, rule, alphabet or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PR 8691 and the landed possibility-covariance note are cited. The
Rodrigues formula and Fourier analysis on Z^3 are standard mathematics.
No audit grade, no new axiom, no new primitive, no new comparator and no
new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the reduced out-of-plane relations are derived by hand and checked
    against the full linearisation of open PR 8691's relations, which
    the lifted solutions satisfy exactly;
  - nullities are computed modulo a prime and matched by exact rational
    solutions;
  - the tilts and the static corner solutions are written directly and
    checked against the relations.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutant | change | outcome |
|---|---|---|
| two angles swapped in role | (8/17, 15/17) to (15/17, 8/17) | caught (2 FAIL) |
| lifted vertical deviation with the wrong sign | -a to a | caught (1 FAIL) |
| mode built with c + w s | minus to plus | caught (2 FAIL) |
| phase solution dropped | solution list emptied | caught (1 FAIL) |
| orthogonality constraint dropped | n . b row removed | caught (1 FAIL) |
| tilt about x with beta sign flipped | -cos to cos | caught (1 FAIL) |
| three modes only | 25 values of w to 3 | caught (1 FAIL) |
| circle identity with the wrong sign | minus to plus | caught (1 FAIL) |
| rank skips a column block | continue to break | caught (2 FAIL) |
| sweep ignores the third relation | test removed | caught (1 FAIL) |
| axis tilt with the wrong solve | Cramer numerator reversed | caught (1 FAIL) |
| static forward relation with the wrong sign | -s to s | caught (1 FAIL) |
| corner axis at the wrong site | (1, 1, 1) to (1, 1, 2) | caught (1 FAIL) |
| forward relations share the back axis | beta_f to beta_b | caught (1 FAIL) |

14 of 14 caught.

- **Vacuity guard:** nullities and solution ranks are printed for every
  box.
- **Budget:** 6 checks, stdout 1556 characters (ceiling 6000), about
  3 s (ceiling 900 s), exact Fractions.

## Verification

```bash
python3 scripts/relational_spiral_frames_linear_rigidity_on_the_lattice_and_sweep_amplification_on_boxes_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/relational_spiral_frames_linear_rigidity_on_the_lattice_and_sweep_amplification_on_boxes_2026_09_23.txt`.
