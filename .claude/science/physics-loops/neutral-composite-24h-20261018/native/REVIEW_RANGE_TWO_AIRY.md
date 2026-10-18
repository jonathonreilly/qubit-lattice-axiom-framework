# Range-two Airy and frozen-arm focused review

Disposition: PASS. No material fixes requested. Ordinary scoped review only; no formal audit or merge.

Read the canonical note, two root proofs, both runners and their principal source inputs; reused INDEPENDENT_RANGE_TWO_BESSEL, PERTURBATION and FROZEN_ARM. The Bessel boundary sign, factor-of-two normalization, c=109/96 shift, physical O(lambda^(14/3)) remainder and positive width convention agree. The contour proof explicitly separates analytic Weyl derivatives from positive resolvent-vector norms, controls both rows and columns, and uses rank-one Riesz projections with trace-norm control. Localized endpoint estimates support restoring energy dependence. The corrected-fast extension requires uniform holomorphy on the smaller depth-f disk, not an assumed pointwise estimate or a microscopic continuation.

The frozen-arm argument uses fixed-order connected support, the prescribed zero-block homological convention, and positive affine slopes with a bounded operator remainder. Its cross-channel finite-rank assertion is explicitly in the full three-momentum fiber. The resolvent gap and O(Jz lambda^4) Schur norm do not by themselves establish the possible O(Jz lambda^6) pole effect; retained-host stability is correctly retained as an obligation. No full-H transfer, actual remainder-to-pole control, original-source residue accuracy or state/detector identification is asserted.

The numerical arm is the stated specified coefficient model with analytic slow-host input. Its logarithmically growing scaled cutoff and 20 percent comparison are appropriate finite controls; scalar Schur residuals are not represented as rigorous pole errors. The Airy runner declares both local sources. The frozen runner declares its exact path source, tests six K2 examples and plaquette counts; all-length conclusions come from the structural proof rather than this finite scan. Parent reports replays PASS in 0.952004 s and 3.581454 s. This review did not duplicate those computations.

Hashes at review:
- `docs/NATIVE_RANGE_TWO_AIRY_NOTE_2026-10-18.md`: `3ccf8a1ab14e6037088fda07e8a2abaab4574a337ae7f85478702bfe890a6911`
- `scripts/native_range_two_airy.py`: `5b2140e43b55365ef08ef7f5c8a8827184051bc7b927ad01ea5757cc9a51df07`
- `scripts/native_frozen_arm_control.py`: `5e14f6c631e870d60b1f050afaa92530839d1b510924dbc503b65f09cd1caa7d`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/RANGE_TWO_AIRY_PROOF.md`: `ec4630d97f315fb0372a892376c05e838a22f3e1cc6b5c5e3d9b65d66f1b64f1`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/FROZEN_ARM_ELIMINATION_PROOF.md`: `b46eee84e483366a05cf38aed37fa5fd4047a9a1f2f6d5089046cc6bd2dd4132`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_range_two_airy.py`: `6fc58b56026e15f5abdfd00a084cc2a77a65e88aa97171309cd40b7a2bb58de9`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_second_other.py`: `fc9339f0bab5ba5c03016fdb3d710bea89f70dc88c6369c416737577de97c26a`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_host.py`: `c45065369d566859cd563e8108df1b00ca3737c5dfaf1c5ad582ea11c5ad40c2`
