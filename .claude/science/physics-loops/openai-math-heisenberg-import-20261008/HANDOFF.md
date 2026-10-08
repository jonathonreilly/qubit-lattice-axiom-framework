# Handoff

For the supplied Pauli Hamiltonian with J<0 on Z3, the checked local-algebra and KMS scaling bridge transports the accepted existence theorem to a translation-invariant low-temperature equilibrium with Pauli magnetization at least 1/4. Exact one-flip dispersion gives D=-2J and the quartic lattice coefficient.

Status: conditional-support / bounded_theorem. Base `ed04ee2736b5bddb4e9064966505e3c3dfe003de`, external `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, planning instructions `eb1f1ca8338848cf2046582e13aef372d8540937`. Source note: `docs/SUPPLIED_FERROMAGNET_ORDER_AND_LOW_TEMPERATURE_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-10-08.md`. Runner: `scripts/supplied_ferromagnet_order_and_low_temperature_normalization_2026_10_08.py`. Complete cache: `logs/runner-cache/supplied_ferromagnet_order_and_low_temperature_normalization_2026_10_08.txt`.

Accepted Lean support: OAI.Heisenberg.spontaneous_magnetization at d=3 and ell=1. The later Bloch/lattice-correction asymptotic remains explicitly paper-premised; the imported ordered-state theorem does not formalize it. Our basis/coupling/KMS bridge is new local proof work.

No sign selection for J, numeric critical temperature, unique equilibrium, finite-volume spontaneous magnetization, thermalization, physical readout or local proof of the many-body asymptotic remainder is claimed.

Read the complete source and source-bound selective review, then perform the shared integrated-current-main landing checks if proposing a later merge. This author run opens a review PR, does not merge and does not apply an audit verdict. Formal retained status belongs to the independent audit path. Lean targets for our new proofs are enumerated in the note; a second external formal verification is not required for accepted matching imports.

The conformance spec's older proposed_retained/proposed_promoted wording differs from its cited current CLAIM_STATUS enum; conditional-support follows that current authority. No status is inferred from a proposed PR. The broader portfolio and other leads are tracked in the original openai-math-leads-20261007 packet/PR9466.
