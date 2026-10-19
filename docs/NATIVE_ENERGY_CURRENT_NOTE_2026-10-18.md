# Energy transport coupling fixed by the native Hamiltonian

Status: bounded-support.

The native bond commutators produce an exact local energy current. Continuity then fixes the collective pole's longitudinal current coupling from its already derived energy-density form factor, with no new interaction or transport coefficient. The isolated pole's static energy-density susceptibility scales as lambda16 q4 for L10.

This is a conservation-law consistency result. It does not derive a momentum density, gravitational stress tensor, universal force or a Newtonian potential. The pole contribution is not the whole susceptibility. No measured data enter the controls.

Proof (`outputs/neutral_continuation7_review_2026_10_18/proofs/pr9814/NATIVE_ENERGY_CURRENT_PROOF.md`); [runner](../scripts/native_energy_current.py). Eight-qubit native commutator and spectral-continuity controls supplement the analytic actual-pole relation.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_energy_current.py`

Complete mathematical arguments and owning-head helper sources are literal inputs. Finite controls test the declared coefficients, matrices and fixtures; analytic joint-limit conclusions use the full proofs and their supplied Hamiltonian, geometry, state, source and order-of-limits premises. One enforced aggregate cap owns child execution and preserves streamed diagnostics. Fresh result JSON is written only in the declared isolated temporary execution directory. Historical status and numerical replay narratives are provenance, not current evidence.
