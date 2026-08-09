# Historic intake: Corrected Propagator: From Amplitude Repulsion to Gravitational Attraction

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: march_2026_event_network_era
Era: march_event_network — propagator exp(ikS)/L^p with spent-delay action and Laplacian-relaxation delay field on grids and generated causal DAGs

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The standard propagator exp(ikS)/delay^p suppresses amplitude near mass independently of phase (k=0 shift -14.02), producing repulsion; replacing the attenuation with geometry-only 1/L^p makes gravity a pure phase effect (k=0 shift exactly +0.00, k=2 shift +13.66) via a phase valley where spent-delay action decreases near mass (Delta-S ~ -L*sqrt(2f), e.g. S = 1.000, 0.868, 0.642, 0.382 at f = 0, 0.01, 0.10, 0.50), giving attraction on 11/12 generated-DAG seeds while preserving interference (12/12, V=0.995) and the Born rule (I3/P = 6.48e-16), with shift scaling as k^2 (CV=0.10).

Original verdict: Overall confidence HIGH for the corrected propagator as an improvement over standard, MODERATE for the attraction mechanism's universality, LOW for distance scaling and decoherence.
Scope: 30 experiments over 20 scripts; rectangular grids 40x31 to 80x71 and generated DAGs of 12-15 layers x 20-25 nodes (connect_radius=3.0, y_range=10.0); k from 0.01 to 20.0, attenuation power 0-3.0, 5-20 seeds per test, k-averaged over k in {3,...,8}; 9 action formulas and 6 attenuation modes searched.
Escape conditions (negative claims): Five null results carry their conditions: 2D lensing is RETRACTED because the outgoing angle oscillates and reverses sign at large impact parameter; the universal force law holds on rectangular grids (R^2=0.91 for shift = C*k^2*Q3) but fails on random DAGs (R^2=0.20 for Q3, 0.04 for Delta-Q3) because topology dominates the coupling — only the k^2 scaling is universal, not the constant C; decoherence is weak (5/12, opaque mass 3/12 as paths route around blocked nodes) and is argued to need a mechanism beyond the propagator, namely topology change; mixed attenuation 1/(L(1+alpha*f))^p with small alpha does not restore distance falloff; and compact density y_range=3 kills attraction only because the field gradient saturates at 0.01 versus 0.46 at y_range=10. The (1+field)^p boost attracts 10/10 but is rejected as unstable (amplitude blow-up 7e9, inverted distance scaling, Born rule I3/P=0.46).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The era's flagship terminal result: standard-propagator repulsion diagnosed; gravity re-founded as pure phase (k=0 shift exactly 0; phase valley Delta-S ~ -L*sqrt(2f); k^2 scaling CV=0.10; 11/12 DAG attraction) while preserving interference (V=0.995) and I3 ~ 1e-16; carries the 2D-lensing retraction and five conditioned null results; 26 runners + 18 logs named.

## Provenance (pinned)

- Original path: `.claude/science/write-ups/corrected-propagator-2026-03-31.md`
- Source commit: `9a89b4a21f6677e5bf8378b4907e2d90f4e351d5`
- git blob: `7b9cfa4e1181410a6879e7d3645d0a958eb9010b`
- sha256: `c5b19e988a1d03fdcdb4004b3ac21169a7d176fabca178cfa8bb74fb2cc1af25`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/march/3163_corrected-propagator-2026-03-31.md](../../archive_unlanded/historic_intake_originals/march/3163_corrected-propagator-2026-03-31.md)
- Lines: 192; runners named: historic runner (unpinned, not in this packet): `scripts/amplitude_packet_action_sweep​.py`; historic runner (unpinned, not in this packet): `scripts/amplitude_spent_fraction_deep​.py`; historic runner (unpinned, not in this packet): `scripts/spent_fraction_generated_dag​.py`; historic runner (unpinned, not in this packet): `scripts/amplitude_attenuation_attraction​.py`; historic runner (unpinned, not in this packet): `scripts/attraction_sanity_checks​.py`; historic runner (unpinned, not in this packet): `scripts/geometry_attenuation_definitive​.py`; historic runner (unpinned, not in this packet): `scripts/attraction_k_resonance​.py`; historic runner (unpinned, not in this packet): `scripts/corrected_unified_mechanism​.py`; historic runner (unpinned, not in this packet): `scripts/growth_rule_attraction_selection​.py`; historic runner (unpinned, not in this packet): `scripts/attenuation_first_principles​.py`; historic runner (unpinned, not in this packet): `scripts/corrected_opaque_decoherence​.py`; historic runner (unpinned, not in this packet): `scripts/corrected_distance_and_lorentz​.py`; historic runner (unpinned, not in this packet): `scripts/distance_scaling_large_grid​.py`; historic runner (unpinned, not in this packet): `scripts/compact_density_diagnosis​.py`; historic runner (unpinned, not in this packet): `scripts/attraction_corridor_map​.py`; historic runner (unpinned, not in this packet): `scripts/weak_coupling_distance​.py`; historic runner (unpinned, not in this packet): `scripts/corrected_propagator_regression_v2​.py`; historic runner (unpinned, not in this packet): `scripts/ray_slope_lensing_test​.py`; historic runner (unpinned, not in this packet): `scripts/growing_graph_attraction_emergence​.py`; historic runner (unpinned, not in this packet): `scripts/perturbative_attraction_derivation​.py`; historic runner (unpinned, not in this packet): `scripts/gravitational_force_law​.py`; historic runner (unpinned, not in this packet): `scripts/force_law_on_dags​.py`; historic runner (unpinned, not in this packet): `scripts/force_law_delta_q3​.py`; historic runner (unpinned, not in this packet): `generative_causal_dag_interference​.py`; historic runner (unpinned, not in this packet): `generated_dag_gravity_induced_phase​.py`; historic runner (unpinned, not in this packet): `toy_event_physics​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Validation table records record suppression as MARGINAL (Delta-V = 0.002, 6/7 regression pass), decoherence WEAK, distance scaling UNCLEAR, universal force law FAIL; known fragilities include attraction failing at k ~ 3.5-4.7 on the lattice (called a lattice resonance absent on DAGs).
- Supersession (as known at extraction): Supersedes the standard propagator used in all 2026-03-30 gravity work (which it diagnoses as producing repulsion) and retracts the 2D gravitational lensing claim; growth results place interference emergence at 6 layers and gravity at 8.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
