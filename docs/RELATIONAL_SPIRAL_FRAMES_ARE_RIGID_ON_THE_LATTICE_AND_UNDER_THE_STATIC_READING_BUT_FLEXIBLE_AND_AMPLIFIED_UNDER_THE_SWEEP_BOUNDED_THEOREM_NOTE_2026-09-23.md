---
claim_id: relational_spiral_frames_are_rigid_on_the_lattice_and_under_the_static_reading_but_flexible_and_amplified_under_the_sweep_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "For the declared Pythagorean angles the full sweep linearization has nullity 6, 9, 12 on L=3,4,5 boxes. Exact rational kernel vectors and modular rank bounds agree. On the whole lattice, bounded solutions are the phase and the two global tilts, by the Fourier-symbol argument below. This is a linear theorem.  Nonsingular exponential modes can grow, decay or remain neutral. The runner reconstructs the w=1/2 mode on a 6-box from its 75 used back-boundary values; one 1/1000 perturbation causes a consistency failure at the first affected site. For the static linearized system, L=4,5,6 have out-of-plane nullity four: two tilts and two corner-axis freedoms; including the phase gives five. Only the global rotations change core values. Finite-box rank claims apply only to the listed sizes and angles. Exponential formulas exclude w=c_j/s_j. Consistency rejection occurs where a local constraint fails; it is not a theorem that arbitrary perturbed data fail everywhere. The whole-lattice result requires boundedness and linearization; nonlinear/local rigidity is a separate result. No dynamics, physical instability or exhaustive boundary-data requirement follows."
upstream_dependencies:
  - minimal_axioms
  - relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_bounded_theorem_note_2026-09-22
runner: scripts/relational_spiral_frames_linear_rigidity_on_the_lattice_and_sweep_amplification_on_boxes_2026_09_23.py
---

# Linear spiral rigidity: lattice theorem and finite-box comparisons

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

For the declared Pythagorean angles the full sweep linearization has nullity 6, 9, 12 on L=3,4,5 boxes. Exact rational kernel vectors and modular rank bounds agree. On the whole lattice, bounded solutions are the phase and the two global tilts, by the Fourier-symbol argument below. This is a linear theorem.

Nonsingular exponential modes can grow, decay or remain neutral. The runner reconstructs the w=1/2 mode on a 6-box from its 75 used back-boundary values; one 1/1000 perturbation causes a consistency failure at the first affected site. For the static linearized system, L=4,5,6 have out-of-plane nullity four: two tilts and two corner-axis freedoms; including the phase gives five. Only the global rotations change core values.

## Boundaries and non-claims

Finite-box rank claims apply only to the listed sizes and angles. Exponential formulas exclude w=c_j/s_j. Consistency rejection occurs where a local constraint fails; it is not a theorem that arbitrary perturbed data fail everywhere. The whole-lattice result requires boundedness and linearization; nonlinear/local rigidity is a separate result. No dynamics, physical instability or exhaustive boundary-data requirement follows.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Conditional mathematics of the declared relational record model"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the declared scope; test extensions separately"
conditional_surface_status: "The stated domain, rule, boundaries and finite checks only"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Conditional proof and exact finite witnesses; no retained grade asserted"
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



## Theorem 1 — The linearisation

Write R_n(α) v = cos α v + sin α (n × v) + (1 - cos α)(n . v) n, and take
α = -θ_i. At the spiral, n = z and b = b0(x) lies in the plane; let t0 =
z × b0. Perturb b by ψ t0 - a z and n by a b0 + β t0. The radial axis
tilt equals a because n . b = 0 must be kept.

- In the plane, (n . b) vanishes to first order and n × b gains nothing
  in plane from the axis tilt. So ψ(x - e_i) = ψ(x).
- Vertically, the vertical part of n × b is -β, which gives
  a(x - e_i) = c_i a(x) - s_i β(x).

For w different from each c_j/s_j, substituting a = prod_j (c_j - w s_j)^(-x_j) and β = w a satisfies all
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
|w| = 1. So the support is k = ±θ. A distribution supported at two points is a finite sum of derivatives
of point masses. Its inverse Fourier coefficients are exponential
polynomials; boundedness of the original sequence excludes every
nonconstant polynomial factor. The remaining plane waves are the modes
at w = ±i. The runner checks that these are the global tilts:
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
- **Inconsistent data** is rejected at any site where the third
  relation disagrees with the first two.

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

Only the tilts move core sites, so core values are linearly rigid on the three tested box sizes.


## No-Go Discipline Gate and falsifiers

**N1 alternative routes / N3 hidden walls.** The negative claims use only the premises and domain above. Alternative
rules, boundary conditions, larger units, hidden shared data, physical
encodings and unstated parameter measures remain outside the result.
**N2 wall independence / N5 resolution.** The declared controls test which supplied conditions matter; a finite
search is exhaustive only where it completes below both record and work
caps. Witness prefixes and subsamples are labelled as such.

**N4 residuals / N6 partial closure.** Extending the explicit boundaries is
separate work; the result does not classify all possible repairs or routes.

**N7 strongest alternatives / N8 cross-result scope.** The positive controls
and companion results above remain available within their own hypotheses.
They do not inherit an exclusion from this note.

A counterexample meeting a theorem's stated hypotheses, a changed exact
count in an exhaustive search, or a failed declared control falsifies the
corresponding result. No other claim is graded, unlocked or audited here.

## Dependencies and provenance

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion result from PR #8691](RELATIONAL_FRAMES_IN_ONE_QUBIT_SPIRAL_RECORDS_UNDER_POSSIBILITY_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-09-22.md)

The original author narrative and review history are recoverable from
the originating PR. Historical author mutation reports are not a substitute
for the current landing review. No new axiom or retained audit grade is adopted.

## Verification

```bash
python3 scripts/relational_spiral_frames_linear_rigidity_on_the_lattice_and_sweep_amplification_on_boxes_2026_09_23.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/relational_spiral_frames_linear_rigidity_on_the_lattice_and_sweep_amplification_on_boxes_2026_09_23.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
