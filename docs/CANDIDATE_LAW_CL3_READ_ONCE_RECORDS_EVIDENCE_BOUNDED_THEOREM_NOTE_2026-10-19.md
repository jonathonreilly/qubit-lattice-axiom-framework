---
claim_id: candidate_law_cl3_read_once_records_evidence_bounded_theorem_note_2026-10-19
claim_type: bounded_theorem
claim_scope: "Finite supplied lattice diagnostics: per-tick position records under a learning update in a 1D two-component walk, and which-slit sorting of readable no-revisit burn trails in a 2D double slit with Bell-type jump rates; no derivation of the read-once clause, physical record dynamics or empirical identification."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/candidate_law_cl3_read_once_records_evidence_2026_10_19.py
---

# Read-once records: two supplied finite-model diagnostics

Claim type: bounded_theorem.
Primary runner: `scripts/candidate_law_cl3_read_once_records_evidence_2026_10_19.py`.

The [proposal register](CANDIDATE_LAWS.md) is provenance context with zero premise weight. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose the walks, jump rates, record rules or readouts below. The note reports what happens in those explicitly supplied models. It motivates the read-once clause; it does not derive it, and neither model is offered as physical dynamics.

## Question

Burn fronts of the register's relay definition form a record at a site each step. Two readings of such records were compared. In the first, the records are readable and the odds condition on them. In the second, each record's single read is taken by the next site of its relay, so no other reader exists. The diagnostics ask what goes wrong in the first reading.

## Part A: a position record every tick

The supplied walk has two components per site on a ring of 3000 sites. Each tick a coin of angle 0.05 mixes them, the first shifts one site right and the second one site left. The initial packet is the positive-frequency branch around momentum 0.06, with group speed cos(th) sin(k)/sin(omega) = 0.7678 for cos(omega) = cos(th) cos(k).

Without records the mean position advances at the group speed (A1). In the recorded model a site is drawn every tick from the current odds, and the odds are conditioned on it: both components are kept at that site and zeroed elsewhere, then renormalised. Averaged over 200 seeded runs, the mean speed falls over the run to a late value consistent with zero within three standard errors (A2). The recorded body also spreads more than twice as wide as the unrecorded packet (A3).

The record's lifetime does not enter this update. If the conditioned odds persist after the record ends, the evolution is that of A2. If the unconditioned odds are restored, the evolution is that of A1, and the record has no later effect at all. A one-tick record lifetime therefore does not separate these cases in this model.

## Part B: readable burn trails in a double slit

The supplied wave is nearest-neighbour hopping on a 130 by 161 lattice, integrated by fourth-order Runge–Kutta with step 0.04. A wall at x = 40 has two five-site slits centred at y = ±9, and the screen is at x = 105. Fronts are drawn from the initial odds and jump to neighbour i from site j at rate max(0, 2 Im(conj psi_i H_ij psi_j)) / |psi_j|^2, Bell's lattice rule. They may not enter a site they have already burnt, and the burnt sites do not feed back on the wave.

The one-slit runs give no fringes in their own half of the screen (B1). With both slits, the wave flux and the front arrivals both show fringes (B2). Each front's trail records which slit it passed. Sorting arrivals by that slit gives which-slit predictability D and a fringe contrast V within each slit group, measured in that group's half of the screen. Both are large, and D^2 + V^2 exceeds 1 (B3). The runner prints all values.

For quantum which-path markers the Englert duality relation is D^2 + V^2 <= 1. In this supplied model readable trails exceed that bound. If, in addition, the odds condition on the trail positions, Part A applies. A reading in which nobody but the relay's next site reads the trail removes the sorted ensemble from the model. The model does not establish that this is the only such reading.

## Scope

All geometries, seeds, packet parameters, bin widths and contrast windows are fixed in the runner. Front arrival statistics come from a finite sample at a finite step, not an exact equivariance proof. The diagnostics say nothing about which records relay, about rates or about the next-site choice, which the clause leaves open. Physical record dynamics, a derivation of the clause, the Englert bound beyond this model, and empirical identification are deferred.
