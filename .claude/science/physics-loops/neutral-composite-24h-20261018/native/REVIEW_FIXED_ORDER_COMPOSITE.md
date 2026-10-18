# Complete fixed-order compact-sector pole review

Disposition: component review PASS; final synthesis check pending the separately requested focused report. No material fix identified by this review so far. Ordinary review only, no audit verdict.

Read the canonical synthesis, root proof, runner, INDEPENDENT_FIXED_ORDER_FAST/SLOW and INDEPENDENT_K4_GAUGE. Gauge transfer compares the same full E8 spectral block, not the selected slow subspace; first-order QQ differences and second-order PP cancellation are explicit. The resulting [G3,K1] vanishes only with both external K1-null conditions. Vacuum subtraction and proper nonwrapping local limits are retained. No general observable or arbitrary-gauge identification is inferred.

The fast argument uses fixed Fourier support and derivative bounds, the actual B1 scalar channel, saddle detuning comparable to lambda, and an outgoing-sheet logarithm. It does not replace continuation by a norm-only resolvent perturbation. The ordinary confined-arm Green function is on its correct lower physical sheet. Finite contacts are restored with the small lambda-log parameter. Slow strict dissipation uses a conjugated spectral-density form, with a nonconstant axial source on regular Fermi arcs, rather than an assumed imaginary coefficient.

Endpoint stability uses the O(f) fixed-endpoint Riesz residue, subtracts its pole to obtain a bounded holomorphic regular matrix, and applies a finite-dimensional determinant and Cauchy estimates. This is materially stronger than multiplying a global perturbation norm by an assumed endpoint weight. The resulting physical O(lambda^5 log) shift is below the O(lambda^(14/3)) retained remainder. Higher affine slopes remain unbounded potentials in the arm, not finite contacts; their scaling is accounted for separately.

The theorem is explicitly fixed order and full momentum fiber, in the supplied compact four-wall sector and ordered reference. No uniform-in-order limit, actual microscopic remainder-to-pole transfer, original-source residue accuracy, selected state or empirical identification is claimed. Finite runner controls are properly supplementary: physical eight-site K1-nullspace K4 comparison and a leading punctured-host spectral identity. Both local source imports are declared. Parent reports source-bound replay PASS in 0.716054 s; not independently repeated here.

Hashes at review:
- `docs/NATIVE_FIXED_ORDER_COMPOSITE_NOTE_2026-10-18.md`: `d88f96cbd87cfd6754eca0f1ee32b2b223103f1bb01d3608437ef172c864811e`
- `scripts/native_fixed_order_composite.py`: `6968e1103b7d13e1896ceeb7991f56612c7eb9631dbc2376906c00e52aad8cc1`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/FIXED_ORDER_COMPOSITE_POLE_PROOF.md`: `9751b654d1fc3788f68739ac9bf00e7b4e11cb9b8c49616a52d94ed832e446d1`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_K4_GAUGE.md`: `5af9faa72b3119beb29ffda33c56073d610d745461c3a3a8f50e96dfcb2c6ac2`

Final synthesis confirmation: PASS. Read INDEPENDENT_FIXED_ORDER_SYNTHESIS and the amended section 4. The large Airy contour now explicitly applies to the baseline slow problem before fast restoration; fast self-energy is used only on its established lower depth-f disk chosen from the baseline pole. This resolves the contour ambiguity without importing continuation across the real axis. Higher slope is retained in f_lambda, endpoint matrices/residues stay localized, and the determinant/Cauchy argument yields the stated O(Jz lambda^5 log) shift. Combined with the separately reviewed graph and gauge inputs, no material synthesis finding remains. The full microscopic pole and original-source accuracy exclusions remain unchanged.
- Updated `.claude/science/physics-loops/neutral-composite-24h-20261018/native/FIXED_ORDER_COMPOSITE_POLE_PROOF.md` SHA256: `3e8e44850317d8fcc1bb461609775ac474cade06ed2ea2898e24d94bd6a37f38`
- Updated `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_FIXED_ORDER_SYNTHESIS.md` SHA256: `3ea2327474dd8afc672842cf1badf5eb584abd34f61f04175c622de873461a71`
