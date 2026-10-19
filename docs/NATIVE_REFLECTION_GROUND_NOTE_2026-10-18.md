# The neutral-mode sector contains a global ground state

Status: exact-support for the supplied even periodic one-qubit Hamiltonian. Two reflection-positive cuts prove that at least one global ground state has positive character under every exact plane symmetry, for any finite even transverse size and positive coupling. No weak-coupling or exponentially small tunneling estimate is needed for this existence result.

The previously derived neutral pole can therefore be referenced to an actual global ground state, rather than a possibly higher-energy selected sector. Its original scalar source preserves the plane characters, so degeneracies in other sectors do not spoil that spectral calculation. Uniqueness and physical preparation are not established.

The method uses the established coefficient-matrix trace inequality of [Lieb and Schupp](https://arxiv.org/abs/math-ph/9910037); the compass-specific two-cut sign and character argument is derived here. We do not import their singlet conclusion. Small exact-grid controls check signs and sector projectors; the all-size claim is analytic.

Proof (`outputs/neutral_continuation7_review_2026_10_18/proofs/pr9806/REFLECTION_GROUND_SECTOR_PROOF.md`), [runner](../scripts/native_reflection_ground_sector.py). The Hamiltonian, slab geometry, physical scales and cosmological identification remain un-derived.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_reflection_ground_sector.py`

Complete mathematical arguments and owning-head helper sources are literal inputs. Finite controls test the declared coefficients, matrices and fixtures; analytic joint-limit conclusions use the full proofs and their supplied Hamiltonian, geometry, state, source and order-of-limits premises. One enforced aggregate cap owns child execution and preserves streamed diagnostics. Fresh result JSON is written only in the declared isolated temporary execution directory. Historical status and numerical replay narratives are provenance, not current evidence.
