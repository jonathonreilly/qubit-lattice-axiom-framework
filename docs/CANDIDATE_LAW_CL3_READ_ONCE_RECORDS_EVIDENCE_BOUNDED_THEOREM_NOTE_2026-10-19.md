---
claim_id: candidate_law_cl3_read_once_records_evidence_bounded_theorem_note_2026-10-19
claim_type: bounded_theorem
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
conditional_surface_status: "Finite numerical diagnostics under supplied algorithms"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Scope-pinned numerical support, not a general physical law"
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_scope: "Finite supplied numerical diagnostics: per-tick position projection in a 1D two-component walk and slit-labelled histogram correlations of non-revisiting trajectories in a 2D double slit. No read-once derivation or operational complementarity test is implemented."
upstream_dependencies:
  - minimal_axioms
runner: scripts/candidate_law_cl3_read_once_records_evidence_2026_10_19.py
---

# Position-conditioned walk and labelled-trail histogram diagnostics

Claim type: bounded_theorem.
Primary runner: `scripts/candidate_law_cl3_read_once_records_evidence_2026_10_19.py`.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose the walks,
jump rates, projection rules or readouts below. These are two separately supplied
algorithms, reported as finite numerical support. No physical record mechanism
or external reader is implemented.

## Question

How do repeated sampled position projections affect one supplied walk, and what
screen correlations occur for a separately supplied non-revisiting trajectory
algorithm? The first algorithm projects onto a sampled position each tick. The
second logs trajectories without feeding those logs into the wave. Neither
algorithm implements or derives an access restriction on permanent records.

## Part A: a position record every tick

The supplied walk has two components per site on a ring of 3000 sites. Each tick a coin of angle 0.05 mixes them, the first shifts one site right and the second one site left. The initial packet is the positive-frequency branch around momentum 0.06, with group speed cos(th) sin(k)/sin(omega) = 0.7678 for cos(omega) = cos(th) cos(k).

Without records the mean position advances at the group speed (free-walk diagnostic). In the recorded model a site is drawn every tick from the current odds, and the odds are conditioned on it: both components are kept at that site and zeroed elsewhere, then renormalised. Averaged over 200 seeded runs, the mean speed falls over the run to a late value consistent with zero within three standard errors (position-projection diagnostic). The recorded body also spreads more than twice as wide as the unrecorded packet (width diagnostic).

The record's lifetime does not enter this update. If the conditioned odds persist after the record ends, the evolution is the position-projected walk. If the unconditioned odds are restored, the evolution is the free walk, and the record has no later effect at all. A one-tick record lifetime therefore does not separate these cases in this model.

## Part B: readable burn trails in a double slit

The supplied wave is nearest-neighbour hopping on a 130 by 161 lattice, integrated by fourth-order Runge–Kutta with step 0.04. A wall at x = 40 has two five-site slits centred at y = ±9, and the screen is at x = 105. Fronts are drawn from the initial odds and jump to neighbour i from site j at rate max(0, 2 Im(conj psi_i H_ij psi_j)) / |psi_j|^2, Bell's lattice rule. They may not enter a site they have already burnt, and the burnt sites do not feed back on the wave.

The one-slit runs have sampled max/min contrast below 0.3 in their own
screen half. With both slits, the sampled wave-flux and arrival histograms have
contrast above 0.9 in the declared central window. These are histogram contrasts;
max/min contrast alone does not identify interference oscillations.

For arrivals labelled by their visited slit, define

    D_screen = |P(y > 0 | upper slit) - P(y > 0 | lower slit)|.

Let C_upper and C_lower be (maximum - minimum)/(maximum + minimum)
in the respective labelled group's upper or lower histogram window, with
C_mean = (C_upper + C_lower)/2. The runner reports all values and the proxy
statistic D_screen^2 + C_mean^2. It does not identify these quantities with an
operational path-detector distinguishability and phase-scanned visibility on
a matched ensemble, so no Englert-bound comparison is established.

A concrete interpretation control uses two disjoint, slit-labelled half-screen
profiles with monotonically decreasing bin heights 10,9,...,1. It gives
D_screen = 1 and C_mean = 9/11, hence proxy statistic 202/121, with no oscillatory
fringes. The reported proxy statistic therefore carries no read-once inference.

## Scope

All geometries, seeds, packet parameters, bin widths and contrast windows are
fixed in the runner. The jump implementation caps each finite-step jump
probability at one and forbids revisits; these modify the continuous-time
Bell-rate construction. Arrival statistics are finite samples at finite step,
not an exact equivariance proof. Physical record dynamics, a reader model,
read-once access rules and empirical identification remain outside this result.

## Review record

The original complementarity and read-once interpretation is withdrawn. The
current candidate-law register is unchanged and supplies no premise to these
diagnostics. The position-speed test now checks the stated three-standard-error
condition separately from slowdown. The histogram outputs are labelled proxies,
and the monotone-profile control makes their interpretation limitation explicit.
