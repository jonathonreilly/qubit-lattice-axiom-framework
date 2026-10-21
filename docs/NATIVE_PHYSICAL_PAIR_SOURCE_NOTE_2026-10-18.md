# Native physical pair coupling to a neutral bound mode

Status: conditional-support.

The original whole-column X readout, applied in a neutral two-feature combination, has a derived nonzero spectral atom in the native Q4 neutral bound mode. Its finite-volume form factor and second-order dressing follow from the existing YY virtual bonds; no interaction or independent scalar oscillator is added.

Proof (`outputs/neutral_continuation7_review_2026_10_18/proofs/pr9808/PHYSICAL_PAIR_SOURCE_PROOF.md`) gives exact source conventions, finite-grid normalization and polynomial-grid remainder conditions. [Runner](../scripts/native_physical_pair_source.py) checks normalization, overlap and physical bond counts. Independent check (`outputs/neutral_continuation7_review_2026_10_18/proofs/pr9808/INDEPENDENT_PHYSICAL_PAIR_SOURCE_CHECK.md`) checks matched-state locality.

This is an observable-specific spectral residue, not an on-shell conversion rate or universal scalar force. Hamiltonian, slab geometry, units and probe choice remain premises. No empirical tests or retained-status claim.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_physical_pair_source.py`

Complete mathematical arguments and owning-head helper sources are literal inputs. Finite controls test the declared coefficients, matrices and fixtures; analytic joint-limit conclusions use the full proofs and their supplied Hamiltonian, geometry, state, source and order-of-limits premises. One enforced aggregate cap owns child execution and preserves streamed diagnostics. Fresh result JSON is written only in the declared isolated temporary execution directory. Historical status and numerical replay narratives are provenance, not current evidence.
