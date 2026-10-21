# Native energy-density coupling to the neutral mode

Status: conditional-support.

The lattice's bond-center energy density has a derived nonzero transition to the native Q4 neutral pole at nonzero momentum. Matching direct virtual paths and ground-state mixing gives amplitude proportional to lambda10 q² and weight proportional to lambda20 q4. At zero momentum it is exactly dark because the source is total energy.

Proof (`outputs/neutral_continuation7_review_2026_10_18/proofs/pr9811/NATIVE_ENERGY_SOURCE_PROOF.md`) fixes the density convention, coefficients, source connection and actual-grid remainder. [Runner](../scripts/native_energy_source_pole.py) checks the physical marked paths and coefficient algebra.

No added interaction or independent scalar field is used. This is not a gravitational or universal scalar coupling: energy-density improvements, detector implementation, physical units and the native slab geometry remain explicit limitations. All controls are model development, not empirical tests.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_energy_source_pole.py`

Complete mathematical arguments and owning-head helper sources are literal inputs. Finite controls test the declared coefficients, matrices and fixtures; analytic joint-limit conclusions use the full proofs and their supplied Hamiltonian, geometry, state, source and order-of-limits premises. One enforced aggregate cap owns child execution and preserves streamed diagnostics. Fresh result JSON is written only in the declared isolated temporary execution directory. Historical status and numerical replay narratives are provenance, not current evidence.
