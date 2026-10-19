# Native neutral response survives increasing slab area

Status: bounded-support. At the derived four-layer coefficient ratio, the
original neutral readout has a strictly nonzero integrated response density
as transverse area grows. This closes a finite-size-only loophole without
adding an interaction, choosing a scalar coupling, or assuming clustering.
The geometry is still a supplied thin slab, not a three-dimensional scalar.

The bulk slab proof (`outputs/neutral_continuation6_review_2026_10_18/proofs/pr9790/BULK_SLAB_RESPONSE_PROOF.md`)
uses a ground-amplitude ratio bound, a variational energy inequality, and
local spectral moments. For E=sum column-edge products, it proves
Var(E)/area > 0.00928960 and positive spectral weight per area >0.00328437
in the broad coefficient-frequency interval (0,1399.518]. The original
readout's inelastic coefficient is -3E, so its weight is nine times larger.
The microscopic normalized weight is at least 4.510e-7 lambda^8 in the
ordered limit lambda->0 first, then increasing area. This is an integrated
bound; it does not locate a particle line or a positive lower frequency.

A separate feature-motion derivation (`outputs/neutral_continuation6_review_2026_10_18/proofs/pr9790/PLAQUETTE_PROPAGATION_PROOF.md`)
explains how native two-step plaquette processes move a sixteen-spin feature
and generate its momentum-dependent readout form factor. Its auxiliary
small-u expansion is checked against finite coefficient spectra; substituting
physical u=1 is not treated as a controlled truncation. The area-density
bound instead holds directly at u=1.

[Replay](../scripts/native_slab_response_density.py) includes independent-size
integer Pauli enumeration, finite dense moment identities, and the auxiliary
series convergence control. The exact third-moment norm bound is 9,003,008
per unit area; no fitted coefficient enters it. All numerical work is exposed
model development, not an observed-data fit or independent empirical test.

A joint microscopic coupling/volume limit, three-dimensional propagation,
stable isolated scalar, cosmological field, universal matter coupling and
source/detector identification remain open. This result does not derive the
native Hamiltonian or the ground-state preparation from observations.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_slab_response_density.py`

The complete mathematical sources and owning-head helpers are portable literal inputs. The supplied Hamiltonian, geometry, state, observable and order of limits remain premises. The primary executes finite coefficient and algebra controls under one enforced aggregate cap, streams child diagnostics, and writes fresh isolated outputs. Analytic asymptotic and microscopic transfer results are supplied by the complete proofs, not numerically established by finite controls. Historical verdicts and saved numerical diagnostics confer no current authority.
