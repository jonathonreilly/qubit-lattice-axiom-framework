# Native assisted coupling across fixed feature heights

Status: conditional-support. Trace: upstream_support. No empirical scalar identification.

The existing one-qubit/site Hamiltonian generates a nearest-hop vertex that reverses two whole column backgrounds. At fixed even height L its exact leading coefficient is -J lambda^(L-1)/2^(L-2) in the x direction. No interaction or coupling constant is added. For L>=6 the prepared vacuum-background channel has squared weight J² lambda^(2L-2)/2^(2L-4) in its derived four-plaquette window near JL lambda^4/16.

The proof (`outputs/neutral_continuation6_review_2026_10_18/proofs/pr9796/ALL_HEIGHT_ASSISTED_HOP_PROOF.md`) evaluates all virtual paths and separates diagonal contamination, dressing and background-channel interpretation. The [runner](../scripts/native_all_height_assisted_hop.py) checks exact finite path sums and the height-six third-order cancellation. These are model-development checks, not independent observational tests.

The connection is a prepared vertex, not a full heavy-particle scattering channel or cosmological scalar. Feature height, weak anisotropy, geometry, preparation and units remain supplied. A small coupling obtained by choosing a large height does not derive a physical hierarchy. Independent coefficient and window checks are recorded in the campaign native directory.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_all_height_assisted_hop.py`

The complete mathematical sources and owning-head helpers are portable literal inputs. The supplied Hamiltonian, geometry, state, observable and order of limits remain premises. The primary executes finite coefficient and algebra controls under one enforced aggregate cap, streams child diagnostics, and writes fresh isolated outputs. Analytic asymptotic and microscopic transfer results are supplied by the complete proofs, not numerically established by finite controls. Historical verdicts and saved numerical diagnostics confer no current authority.
