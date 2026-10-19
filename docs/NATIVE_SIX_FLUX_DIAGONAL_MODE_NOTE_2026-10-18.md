# Native staggered neutral mode from diagonal column pairs

Status: conditional-support.

The same one-qubit Hamiltonian supports a neutral two-column feature in its six-defect sector. Native virtual paths select an antisymmetric internal orientation and a band minimum at transverse momentum (pi,pi). The twelfth-order plaquette-dependent winding detour is essential for the sign of its motion; no interaction is added.

Proof (`outputs/neutral_continuation7_review_2026_10_18/proofs/pr9809/SIX_FLUX_DIAGONAL_MODE_PROOF.md`) gives actual finite-volume transfer and a symmetrized microscopic X/Y-column readout that is exactly scalar under the transverse little point group. Its leading pole weight is 1-5lambda²/2. The [runner](../scripts/native_sixflux_diagonal_mode.py) checks exact path sums, finite-pattern classification, physical readout symmetries and normalization.

This is a staggered slab mode, not a uniform cosmological scalar, three-dimensional Lorentz scalar, or universal force. Native action, geometry, scale and measurement protocol remain premises. Independent checks are ordinary scoped reviews, not formal audit verdicts. All controls are exposed model development, not empirical tests.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_sixflux_diagonal_mode.py`

Complete mathematical arguments and owning-head helper sources are literal inputs. Finite controls test the declared coefficients, matrices and fixtures; analytic joint-limit conclusions use the full proofs and their supplied Hamiltonian, geometry, state, source and order-of-limits premises. One enforced aggregate cap owns child execution and preserves streamed diagnostics. Fresh result JSON is written only in the declared isolated temporary execution directory. Historical status and numerical replay narratives are provenance, not current evidence.
