# A native six-layer neutral pole with a derived readout

Status: conditional-support. The supplied one-qubit Hamiltonian produces an isolated collective mode without an added interaction or chosen scalar coupling, within a specified six-layer symmetry sector and weak-coupling limit.

The sixth-order calculation keeps both native column hopping and the interaction between neighboring plaquette defects. Their derived ratio makes the four-defect problem a four-arm graph with one repulsively bound state above its continuum. The state carries about 7.03 percent of the relevant leading source weight. It is planar and its dispersion bends downward near zero momentum, so this branch does not establish a positive-gradient relativistic scalar.

The actual microscopic result holds along even transverse size R comparable to log(1/lambda), using the lowest vacuum in the specified positive plane-symmetry sector. Its excitation energy is J[3lambda^4/8+0.16793911416lambda^6+o(lambda^6)]. The original normalized bond readout has pole weight 1.86442186268e-5lambda^12[1+o(1)]. A native prepared heavy-hop vertex also couples to the mode, with the expected finite-volume normalization; it is not a relaxed-heavy scattering result.

The proof (`outputs/neutral_continuation6_review_2026_10_18/proofs/pr9798/SIX_LAYER_NEUTRAL_POLE_PROOF.md`) includes native coefficients, complete four-defect comparison, normalization and separate source/energy error bounds. The [runner](../scripts/native_six_layer_neutral_pole.py) checks exact virtual paths, independent sixth-order recursion, finite torus graphs and the star residue. Independent focused reports are in the campaign native directory.

Global-ground selection, three-dimensional propagation, physical scales, cosmological interpretation and observational tests remain open. All calculations are exposed model development. The Hamiltonian and geometry have not been derived from observations.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_six_layer_neutral_pole.py`

The complete mathematical sources and owning-head helpers are portable literal inputs. The supplied Hamiltonian, geometry, state, observable and order of limits remain premises. The primary executes finite coefficient and algebra controls under one enforced aggregate cap, streams child diagnostics, and writes fresh isolated outputs. Analytic asymptotic and microscopic transfer results are supplied by the complete proofs, not numerically established by finite controls. Historical verdicts and saved numerical diagnostics confer no current authority.
