# A light mobile constituent from a whole column

Status: conditional-support. Flipping one ten-qubit column changes all horizontal plane charges and produces an isolated light band in the same native Hamiltonian as the neutral bound modes. Its rest energy starts at J(L/16)lambda4 and its transverse quadratic dispersion at Jgamma lambda10|q|². No hopping interaction is supplied.

The original normalized whole-column X readout has pole weight 1-(5/4)lambda²+O(lambda4), with the lost weight accounted for by virtual wall dressing. Local coefficient and Gram bounds transfer this statement to polynomially growing grids. The neutral ZZ readout cannot create this charged mode; the two observables must not be conflated.

“Charge” here is an exact plane-symmetry label, not electric charge. These column operators commute at separate sites and do not establish fermions. The adjacent and separation-two neutral features are native bound configurations of the same column variables, but their scattering or scalar–matter vertex requires a further calculation.

Proof (`outputs/neutral_continuation7_review_2026_10_18/proofs/pr9807/CHARGED_COLUMN_POLE_PROOF.md`), [runner](../scripts/native_charged_column_pole.py). Hamiltonian, geometry, units and observational identification remain premises.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_charged_column_pole.py`

Complete mathematical arguments and owning-head helper sources are literal inputs. Finite controls test the declared coefficients, matrices and fixtures; analytic joint-limit conclusions use the full proofs and their supplied Hamiltonian, geometry, state, source and order-of-limits premises. One enforced aggregate cap owns child execution and preserves streamed diagnostics. Fresh result JSON is written only in the declared isolated temporary execution directory. Historical status and numerical replay narratives are provenance, not current evidence.
