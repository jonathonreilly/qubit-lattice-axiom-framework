# A larger native neutral bound feature

Status: conditional-support. The supplied one-qubit Hamiltonian generates a bound pair of extended ten-spin columns, its transverse motion and a nonzero coupling to the original scalar observable. No new attractive interaction or coupling parameter is introduced.

The native sixth-order interaction selects a compact eight-plaquette cluster. Its motion starts at order lambda14, with perpendicular/parallel-to-the-pair-axis hopping ratio four. The original readout starts at amplitude lambda18; its coefficient requires both binding and a previously uncomputed plaquette-dependent winding detour. The total q0 source weight is 4.146121184297614e-13 lambda36 asymptotically. Local reductions transfer the isolated two-orientation cluster and positive ordered-band dispersion to polynomially growing grids in the selected plane sector.

This is a ten-layer weak-anisotropy slab result. The global ground sector, three-dimensional propagation, observed units, fermion statistics and cosmological/gravitational identification remain unproved. All controls are exposed model development, with no observational fit or independent empirical test.

Proof (`outputs/neutral_continuation7_review_2026_10_18/proofs/pr9804/EIGHT_FLUX_BOUND_CLUSTER_PROOF.md`) and [runner](../scripts/native_eightflux_bound_cluster.py). The actual-grid conclusion uses analytic bounds, not a large full-grid diagonalization.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_eightflux_bound_cluster.py`

Complete mathematical arguments and owning-head helper sources are literal inputs. Finite controls test the declared coefficients, matrices and fixtures; analytic joint-limit conclusions use the full proofs and their supplied Hamiltonian, geometry, state, source and order-of-limits premises. One enforced aggregate cap owns child execution and preserves streamed diagnostics. Fresh result JSON is written only in the declared isolated temporary execution directory. Historical status and numerical replay narratives are provenance, not current evidence.
