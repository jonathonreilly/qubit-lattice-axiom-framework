# Handoff

The supplied D3Q27 network has exactly five additive invariants, a unique positive constrained Gibbs equilibrium and convergence from every positive initial state. Its finite occupation chain has exact drift/noise and factorial detailed balance; a complete Doob–Gronwall argument bounds its fixed-time mean-square ODE approximation error uniformly in particle number.

Status: conditional-support / bounded_theorem. Base `ed04ee2736b5bddb4e9064966505e3c3dfe003de`, external `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, planning instructions `eb1f1ca8338848cf2046582e13aef372d8540937`. Source note: `docs/SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md`. Runner: `scripts/supplied_finite_velocity_collisions_and_gibbs_equilibration_2026_10_08.py`. Complete cache: `logs/runner-cache/supplied_finite_velocity_collisions_and_gibbs_equilibration_2026_10_08.txt`.

Accepted Lean support: OAI.Problem326.global_bounded_persistent_solution for fixed positive rates and each positive initial state. The stronger classwise absorbing-set companion is not required or imported. The invariant, entropy, finite-chain and LLN bridge arguments are supplied here.

No velocity refinement, continuum kinetic/fluid limit, long-time rate, exchange of particle/time limits, arbitrary-particle component classification, native dynamics, physical clock or empirical prediction is claimed.

Read the complete source and source-bound selective review, then perform the shared integrated-current-main landing checks if proposing a later merge. This author run opens a review PR, does not merge and does not apply an audit verdict. Formal retained status belongs to the independent audit path. Lean targets for our new proofs are enumerated in the note; a second external formal verification is not required for accepted matching imports.

The conformance spec's older proposed_retained/proposed_promoted wording differs from its cited current CLAIM_STATUS enum; conditional-support follows that current authority. No status is inferred from a proposed PR. The broader portfolio and other leads are tracked in the original openai-math-leads-20261007 packet/PR9466.
