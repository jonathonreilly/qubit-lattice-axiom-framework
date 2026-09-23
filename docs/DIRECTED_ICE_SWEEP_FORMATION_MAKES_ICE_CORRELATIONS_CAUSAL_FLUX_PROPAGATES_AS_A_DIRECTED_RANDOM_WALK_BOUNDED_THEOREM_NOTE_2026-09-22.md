---
claim_id: directed_ice_sweep_formation_makes_ice_correlations_causal_flux_propagates_as_a_directed_random_walk_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading, sweep order, the soldered uniform-consistent vertex rule of open PR 8667 written in arrows (each vertex, after its three back-links, takes forward arrows uniformly among those keeping the ice rule). Exact: conditional mean B/3 per forward arrow and conditional covariance (3/2)(1 - B^2/9) times the sum-zero projector; the mean response to one back-link is the multinomial random walk with steps e_1, e_2, e_3 (layer mass 1, transverse variance 2n/9, diagonal peak (3m)!/(m!^3 27^m), m R_m rising below 1; 3^(-n) along a lattice axis and ratio (2n+1)(2n+2)/(9(n+1)^2) along a face diagonal); the symbol D(k) = 1 - (1/3) sum e^(-i k_j) vanishes only at k = 0 and expands as (i/3) sum k_j + (1/6) sum k_j^2 + ...; on a 4x4x4 box with independent uniform inflow, every back sum has variance 3, same-layer arrows are uncorrelated, and the covariance of any two arrows is R/3 when one lies in the other's forward cone and 0 otherwise. The uniform ice measure on the landed 2x2x2 torus has an arrow covariance invariant under all 48 cubic symmetries. No rule, order law or physical identification is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
runner: scripts/directed_ice_sweep_formation_flux_propagates_as_a_directed_random_walk_2026_09_22.py
---

# Directed ice: formation along a sweep makes the ice correlations causal, and flux propagates as a directed random walk

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Formation reaches the ice support in a
sweep with no unrecorded site (open PRs 8667, 8670), with a frame source
(open PRs 8676, 8679). But with local records it cannot reach the uniform
ice measure behind the landed Coulomb correlations (open PR 8686). This
block asks what the sweep-formed ice measure looks like at long
distances.

## Result up front

1. **The ice rule makes the sweep rule linear in the mean.** In arrow form
   (sigma = +1 along +e_i) the ice rule says that at every vertex the
   forward arrows sum to the backward arrows. Suppose a vertex, formed
   after its three back-links, picks its forward arrows uniformly among
   those that keep the rule.
   - Each forward arrow then has conditional mean B/3, where B is the
     back sum.
   - The conditional covariance is (3/2)(1 - B^2/9) times the projector
     onto sum-zero patterns.
   - So fluctuations never change the flux a vertex passes on.

2. **A flux fluctuation walks forward.** The mean response to a unit
   change of one back-link obeys R(x) = (1/3) times the sum over x's
   back-neighbours, so it is exactly the multinomial random walk with
   steps e_1, e_2, e_3.
   - Each diagonal layer carries total response 1, so flux is conserved.
   - The transverse variance is 2n/9 after n steps.
   - The peak on the diagonal is (3m)!/(m!^3 27^m), and m times it rises
     but stays below 1, so it decays like 1/m.
   - Along a lattice axis the response is exactly 3^(-n), and along a face
     diagonal it falls geometrically (ratio tending to 4/9). Only the body
     diagonal carries a power law, so even a mixture over sweep directions
     keeps correlations concentrated on the body diagonals.
   - The Fourier symbol D(k) = 1 - (1/3) sum e^(-i k_j) vanishes only at
     k = 0. Near there it is (i/3)(k_1 + k_2 + k_3) + (1/6) |k|^2 + ...:
     first order along the sweep diagonal, second order across it. That
     is directed diffusion.

3. **The sweep-formed ice measure is causal.** On a 4x4x4 box with
   independent uniform inflow arrows, the second moments close exactly.
   - Every back sum has variance 3, so arrows in the same diagonal layer
     are uncorrelated.
   - The covariance of any two arrows is R/3 when one lies in the other's
     forward cone, and 0 otherwise. Arrows outside each other's cones are
     uncorrelated.

4. **The uniform measure has no direction.** The uniform ice measure on
   the landed 2x2x2 torus (9600 states) has an arrow covariance invariant
   under all 48 cubic symmetries, including those that reverse the sweep
   diagonal. The sweep-formed measure's correlations live in forward
   cones of one diagonal and have no such symmetry.

5. **What this means for the photon lane.** A sweep forms the ice support
   and keeps the Gauss law exactly. But the resulting phase is directed:
   - flux fluctuations are carried along the sweep's diagonal as a random
     walk;
   - correlations vanish outside forward cones.

   That is not the isotropic Coulomb phase of the landed notes. The formed
   photon route therefore reaches a different long-distance phase unless
   the uniform measure is restored, by a coordinator (open PR 8686) or by
   conditioning. A covariant mixture over sweep frames averages the
   direction but not the causal structure of each realisation.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "formation with local records reaches the ice support but not the uniform ice measure (open PR 8686); determine the long-distance character of the sweep-formed ice measure"
source_of_blocker_text: open_prs_8667_8686
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record in the assembly that the formed photon route yields directed ice unless coordinated; test other covariant rules (straight-continuation preferences) and the covariant sweep mixture"
conditional_surface_status: "formation reading; sweep order; the soldered uniform-consistent vertex rule; independent uniform inflow on the box; the landed uniform measure for comparison"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "items 1-4 are exact enumerations and exact rational recursions on declared windows; the symbol statements are exact series coefficients plus a one-line zero-set argument"
```

## Premises and declared objects

- **Arrows and the ice rule.** Coarse vertices of Z^3 carry arrows on
  links, with sigma = +1 along +e_i. The ice rule in arrow form is 3 in
  and 3 out at every vertex, which is the landed occupation form read
  through the even/odd coarse sublattice.
- **The sweep.** Each vertex forms after its three back-links (open
  PR 8670).
- **The vertex rule.** The soldered uniform-consistent vertex rule of open
  PR 8667, written in arrows.
- **The box.** Coarse vertices [0,4)^3 with independent uniform arrows
  entering through the three low faces.
- **The comparison.** The uniform ice measure on the landed 2x2x2 torus.

## Prior art and what is new

- The landed spin-half cubic-ice note gives the uniform RK measure and its
  Coulomb correlations, and the 9600 states used here.
- Open PR 8667 treats sweeps and their bias on the plaquette window; open
  PR 8686 treats the loop obstruction and coordinators.
- New here: the long-distance character of sweep-formed ice. Its
  covariance is causal and given exactly by a directed random walk.
- The multinomial walk, its local limit, and lattice Fourier series are
  standard mathematics.

## Theorem 1 — The rule in arrow form

For each of the 8 back patterns, the forward patterns keeping the ice
rule (C(3, k) of them, k = (3 + B)/2 up-arrows) give mean B/3 and
covariance (3/2)(1 - B^2/9)(I - J/3), checked by enumeration.

## Theorem 2 — The response walk and its symbol

Conditional means propagate linearly. A unit change on one back-link of
vertex v changes each forward arrow at v by 1/3, and the change of any
later vertex's back sum is R(x) = (1/3) sum_j R(x - e_j), with R(v) = 1.
Its solution is the multinomial probability of reaching x with steps
e_1, e_2, e_3 each taken with probability 1/3. This is checked up to 14
steps, together with:
- total layer mass 1;
- transverse variance 2n/9;
- the diagonal ratio identity, for m up to 20;
- R(n,0,0) = 3^(-n) and the face-diagonal ratio identity, for n up to 20.

For the symbol, Re D(k) = 1 - (1/3) sum cos k_j is zero only when every
cos k_j = 1, that is at k = 0. On the quarter-period grid the only zero
is k = 0. The series coefficients are exact.

## Theorem 3 — Causality of the formed measure

Second moments close exactly: conditional means are linear, and
conditional covariances are quadratic in the back arrows.

By induction over diagonal layers, arrows in one layer are pairwise
uncorrelated:
- each vertex's back sum has variance 3;
- the forward arrows at a vertex are then uncorrelated;
- two vertices of one layer share only uncorrelated inputs.

Every covariance therefore comes from the response walk. An arrow and a
forward arrow of a vertex in its head's forward cone have covariance
R/3; any other pair has covariance 0.

All of this is checked on the 4x4x4 box, for all 192 x 192 pairs of
forward arrows and for two inflow arrows against every forward arrow. The box has 240 arrows with
exact rational second moments.

## Theorem 4 — The uniform measure's symmetry

The arrow covariance of the uniform measure on the 2x2x2 torus, over
9600 states, satisfies C(g l, g m) s_l s_m = C(l, m) for all 48 signed
permutations g. Here s is the sign by which g maps each link's axis. The
check is exact.

## No-Go Discipline Gate

The negative content is scoped: the sweep-formed ice measure of the
declared rule is causal and directed, so it is not the uniform measure's
isotropic phase.

- **N1 alternative routes.** The following are not computed:
  - other covariant vertex rules, such as preferences for straight
    continuation (their mean response still lives in the forward cone;
    their covariance is not computed);
  - non-sweep orders;
  - coordinated formation (open PR 8686).
- **N2 wall independence.** Exact recursions and enumeration; no
  dynamics beyond the formation law.
- **N3 hidden walls.** The inflow is declared independent and uniform. A
  correlated inflow adds its own correlations, propagated by the same
  walk.
- **N4 residual matching.** The residual for the formed photon route is a
  uniform-measure restorer (coordinator or conditioning), or acceptance
  of a directed phase.
- **N5 rhetoric audit.** "Causal" means the covariance support described
  in Theorem 3. No claim about physical light cones or propagation speed
  is made.
- **N6 partial-closure paths.** Other rules; the covariant sweep
  mixture; correlation shapes on larger boxes.
- **N7 steelman.** For formation: the Gauss law is exact and flux is
  conserved and transported. Against identifying the result with the
  landed photon phase: its correlations are causal and directed, not
  isotropic. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8667, 8670 and 8686 and the landed
  notes are cited; the 9600 states are reproduced.

## Falsifiers

- A back pattern whose forward moments differ from Theorem 1.
- A response value off the multinomial walk.
- A pair of arrows on the box whose covariance departs from R/3 inside a
  cone, or from 0 outside every cone.
- A cubic symmetry under which the uniform measure's arrow covariance
  changes.

## Boundaries and non-claims

No rule, order law or physical identification is adopted. The box is
finite, the inflow is declared, and the stationary infinite-lattice law
is described through the same recursion only. Nothing here addresses
the static route or coordinated formation. Nothing here grades, unlocks
or audits any other claim.

## Imports

The landed notes and open PRs are cited. The multinomial walk and
Fourier series are standard mathematics. No audit grade, no new axiom,
no new primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the response recursion is compared with the closed multinomial
    formula;
  - the box covariance comes from the second-moment recursion, not from
    the kernel, and is then compared with the kernel pair by pair;
  - the uniform measure's symmetry is checked on all 9600 states.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| forward patterns not held to the ice rule | = B to >= B | caught (2 FAILs) |
| response averages over two parents | 1/3 to 1/2 | caught (2 FAILs) |
| multinomial exponent off by one | 3^n to 3^(n+1) | caught (4 FAILs) |
| transverse spread centred wrongly | n/3 to n/2 | caught (1 FAIL) |
| symbol built from e^(+ik) | sign of i | caught (1 FAIL) |
| quarter-period values wrong | one value changed | caught (1 FAIL) |
| box recursion averages with 1/2 | 1/3 to 1/2 | caught (3 FAILs) |
| forward covariance shifted | (VB - 3)/6 to (VB - 2)/6 | caught (2 FAILs) |
| inflow variance halved | 1 to 1/2 | caught (3 FAILs) |
| cone condition drops one axis | axis test removed | caught (1 FAIL) |
| arrows ignore the sublattice | arrow convention | caught (1 FAIL) |
| reflections do not flip arrows | axis sign dropped | caught (1 FAIL) |
| forward covariance constant | (VB - 3)/6 to (VB - 3)/5 | missed; diagnosed non-defect (every back sum has variance 3, so the constant multiplies zero) |

  Twelve of twelve defect mutants are caught; the thirteenth multiplies
  a quantity that Theorem 3 shows is always zero.

- **Vacuity guard:** 240 box arrows, 192 x 192 covariance comparisons,
  9600 torus states and 48 symmetries are reported or iterated in full.
- **Budget:** 12 checks, stdout 2194 characters (ceiling 6000), under a
  second (ceiling 900 s), exact Fractions.

## Verification

```bash
python3 scripts/directed_ice_sweep_formation_flux_propagates_as_a_directed_random_walk_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=12 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/directed_ice_sweep_formation_flux_propagates_as_a_directed_random_walk_2026_09_22.txt`.
