---
claim_id: formed_flux_as_a_persistent_walk_straight_continuation_gives_ballistic_then_diffusive_transport_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading, sweep order, arrows with the ice rule in arrow form. The rule R_p (forward arrows equal the back arrows with probability p, otherwise uniform among ice-consistent forward arrows) keeps the ice rule exactly, has forward mean p b_i + (1 - p) B/3, and is covariant under the six octant-preserving axis permutations; pairing axes makes it soldered. A flux fluctuation's direction follows the kernel K = p I + (1 - p) J/3 (eigenvalues 1, p, p), so the mean flux kernel is a persistent random walk on the forward lattice: each layer carries flux 1; at p = 1 the flux runs straight along its axis; at p = 0 it is the multinomial walk of open PR 8687 at all 2925 sites checked. Its spread along the source axis equals the Markov occupation variance (layers 1-15) and grows at rate (2/9)(1+p)/(1-p) (2/3 at p = 1/2), approached geometrically. On a 4x4x4 box with independent inflow (p = 1/2, 3/4) back sums have variance 3, same-layer arrows are uncorrelated, and the covariance with an inflow arrow is the persistent-walk kernel, so the covariance stays causal. No rule, order law or physical identification is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
runner: scripts/formed_flux_persistent_walk_straight_continuation_ballistic_then_diffusive_2026_09_22.py
---

# Formed flux as a persistent walk: straight continuation gives ballistic, then diffusive, transport

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Sweep-formed ice is directed: a flux
fluctuation walks forward as a multinomial random walk (open PR 8687).
The equal-time Coulomb law needs a positive static rule, and dynamics
still needs the landed Hamiltonian (open PR 8698). This block asks what
transport formation itself can give a flux fluctuation: diffusion only,
or something closer to a propagating wave.

## Result up front

1. **A straight-continuation rule keeps the ice rule.** Take the rule
   R_p: with probability p the forward arrows copy the back arrows on the
   same axes; otherwise the rule picks uniformly among the ice-consistent
   forward arrows.
   - It keeps the ice rule exactly.
   - Each forward arrow has mean p b_i + (1 - p) B/3.
   - It is covariant under the six axis permutations that preserve the
     sweep's octant.
   - Pairing each back-link with the forward link on its axis needs a
     frame source: soldering, or coordinate letters as in open PR 8676.

2. **The flux direction has memory.** A unit of flux keeps its axis with
   probability (1 + 2p)/3 and turns to each other axis with probability
   (1 - p)/3. The direction kernel is K = p I + (1 - p) J/3, with
   eigenvalues 1, p, p. The memory of the direction relaxes by a factor
   p per layer.

3. **The mean flux kernel is a persistent random walk.**
   - Each diagonal layer carries flux 1.
   - At p = 1 the flux runs straight along its axis and never spreads.
   - At p = 0 the kernel is the multinomial walk of open PR 8687,
     checked at all 2925 sites up to 24 layers.

4. **Ballistic, then diffusive.** The spread along the source axis
   equals the variance of the direction chain's occupation count
   (checked exactly for layers 1-15).
   - It grows at rate (2/9)(1 + p)/(1 - p), which is 2/3 at p = 1/2,
     three times the p = 0 rate. The approach is geometric in p.
   - At p = 1 the spread is 0 in every layer; at p = 0 it is 2n/9.
   - So flux moves ballistically along a lattice axis for about
     1/(1 - p) layers and diffuses beyond, with a coefficient enhanced by
     (1 + p)/(1 - p).

5. **The covariance stays causal.** On a 4x4x4 box with independent
   uniform inflow, the second moments close exactly for p = 1/2 and
   p = 3/4. Every back sum has variance 3, same-layer arrows are
   uncorrelated, and the covariance with an inflow arrow is the
   persistent-walk kernel. So the causal structure of open PR 8687
   holds across the family: arrows correlate only inside forward cones.

6. **What this means for the photon lane.** A persistent random walk is
   the discrete form of telegraph propagation: finite speed with damping,
   a standard continuum limit. So formation can move flux like a wave
   over a finite memory length. That motion runs along the three lattice
   axes of the sweep's octant, and it is damped unless p = 1, where the
   rule is deterministic and nothing spreads. Undamped isotropic wave
   propagation is not produced by these rules. The dynamics of the landed
   photon phase stays with the supplied Hamiltonian (open PR 8698).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "formed ice transports flux diffusively (open PR 8687) and photon dynamics rests on the supplied Hamiltonian (open PR 8698); determine what transport covariant formation rules with memory give"
source_of_blocker_text: open_prs_8687_8698
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record that formed flux transport is ballistic-then-diffusive along the octant's axes; compute covariances under R_p and the covariant mixture over sweep frames"
conditional_surface_status: "formation reading; sweep order; the declared rule family R_p with a frame source; mean-response kernels and box covariances"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "exact enumeration of the rule, exact eigenvectors of the direction kernel, and exact rational recursions of the flux kernel and its spread"
```

## Premises and declared objects

- **Arrows and the ice rule** on coarse links, in arrow form, as in open
  PR 8687.
- **The sweep.**
- **The rule family R_p,** with a frame source to pair axes.
- **The direction kernel K,** and the flux kernel G(y, j): the expected
  flux arriving at y along axis j from a unit arriving at the origin
  along axis 0.

## Prior art and what is new

- Open PR 8687 gives the p = 0 case: the multinomial walk, and causal
  covariance.
- Standard mathematics: persistent (correlated) random walks, the
  variance of Markov occupation counts, and the telegraph equation as
  their continuum limit.
- New here: covariant ice formation with a straight-continuation
  preference realises the persistent walk exactly. Its ballistic and
  diffusive regimes are computed exactly.

## Theorem 1 — The rule and its kernel

Enumeration of the 8 back patterns, for p = 0, 1/3, 1/2 and 1, confirms:
- the ice rule;
- the forward mean;
- covariance under the six axis permutations.

K sends the uniform vector to itself, and sum-zero vectors to p times
themselves.

## Theorem 2 — The persistent walk

G(y, j) = sum_i G(y - e_j, i) K_ij, starting from G(0, 0) = 1. The
following are checked exactly up to 24 layers:
- layer flux 1;
- at p = 1, support on the source axis only;
- at p = 0, the multinomial walk at every site.

The spread along the source axis equals sum_t a_t(1 - a_t) plus twice
sum_(s<t) a_s(1/3 + (2/3)p^(t-s) - a_t), where a_t = 1/3 + (2/3)p^t.
This is the occupation variance of the direction chain started on the
source axis, and the agreement is checked for layers 1-15 at p = 1/2.
Consecutive differences approach (2/9)(1 + p)/(1 - p) within
4(s + 2)p^(s+1).

## Theorem 3 — Causal covariance

For R_p, the conditional mean of a forward arrow is linear in the back
arrows, and E[f_i f_k | b] = p b_i b_k + (1 - p)(B^2 - 3)/6 is quadratic.
So the second moments close. Suppose the back arrows of a vertex are
uncorrelated with variance 1. Then the forward arrows are uncorrelated
too, since the linear and fluctuating parts cancel exactly. By induction
over layers every back sum has variance 3, and every covariance is carried
by the mean kernel. Checked exactly on a 4x4x4 box for p = 1/2 and 3/4.

## No-Go Discipline Gate

The negative content is scoped: within R_p, flux transport is ballistic
only at p = 1, where it is deterministic, and diffusive at long range
otherwise.

- **N1 alternative routes.** Other covariant rules with longer memory,
  static readings, and the covariant sweep mixture are not computed.
- **N2 wall independence.** Exact recursions; no dynamics beyond
  formation.
- **N3 hidden walls.** The inflow is declared independent and uniform;
  covariances are computed on a 4x4x4 box for two values of p.
- **N4 residual matching.** For wave-like photon dynamics the residual is
  a supplied Hamiltonian, or rules with undamped memory, which at p = 1
  are deterministic.
- **N5 rhetoric audit.** "Wave-like" means finite-speed transport over
  the memory length. No claim of relativistic or isotropic propagation
  is made.
- **N6 partial-closure paths.** Covariances under R_p; longer-memory
  rules; the covariant mixture.
- **N7 steelman.** For formation as photon dynamics: it gives finite
  speed and conserved flux. Against it: damping and axis anisotropy.
  Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8687 and 8698 and the landed note
  are cited.

## Falsifiers

- A back pattern whose forward law breaks the ice rule or the stated
  mean.
- A layer with flux other than 1.
- A p = 0 site off the multinomial walk.
- A spread differing from the Markov formula.

## Boundaries and non-claims

No rule, order law or physical identification is adopted. Only mean
flux kernels are computed. Nothing here grades, unlocks or audits any
other claim.

## Imports

The landed note and open PRs are cited. Persistent walks and the
telegraph limit are standard mathematics. No audit grade, no new axiom,
no new primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the flux kernel comes from the lattice recursion;
  - the spread comes from the Markov-chain formula, and the two are
    compared exactly;
  - the p = 0 case is compared with the closed multinomial formula.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| straight branch shifts axes | back pattern rotated | caught (2 FAILs) |
| kernel turn weight 1/2 | (1-p)/3 to (1-p)/2 | caught (4 FAILs) |
| flux arrives from the wrong neighbour | predecessor axis shifted | caught (2 FAILs) |
| Markov variance sign | 1 - a to 1 + a | caught (1 FAIL) |
| diffusion rate squared denominator | (1-p) to (1-p)^2 | caught (1 FAIL) |
| spread measured about n/3 | true mean replaced | caught (2 FAILs) |
| straight branch half weight | p to p/2 | caught (1 FAIL) |
| box recursion turn weight 1/2 | K on the box | caught (1 FAIL) |
| box inflow variance halved | 1 to 1/2 | caught (1 FAIL) |

  Nine of nine defect mutants are caught.
- **Vacuity guard:** 2925 sites; 24 layers; 15 exact variance
  comparisons.
- **Budget:** 7 checks, stdout 1210 characters (ceiling 6000), under a
  second (ceiling 900 s), exact Fractions.

## Verification

```bash
python3 scripts/formed_flux_persistent_walk_straight_continuation_ballistic_then_diffusive_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=7 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/formed_flux_persistent_walk_straight_continuation_ballistic_then_diffusive_2026_09_22.txt`.
