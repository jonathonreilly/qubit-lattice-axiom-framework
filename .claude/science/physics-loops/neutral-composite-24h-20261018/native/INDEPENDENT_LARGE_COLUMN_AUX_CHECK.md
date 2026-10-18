# Auxiliary large-column occupation provenance check

Disposition: PASS as explicitly frozen, auxiliary numerical evidence. No formal audit or heavy eigenstate replay; no source edits.

The local transverse operator includes exactly the existing x/y bonds of each rung. In its positive physical parity sector its eigenvalues are -2sqrt(2),0,+2sqrt(2), so P_low=(h²-2sqrt(2)h)/16 and P_high=(h²+2sqrt(2)h)/16 are correct spectral projectors; P_mid=I-P_low-P_high. These project onto internal energy eigenspaces, with the protected coordinate retained. They are not particle-number operators. The extra exact plane-sector compression preserves h and uses the checked signed-orbit normalization; its physical Y plane has sixteen Y factors and coefficient i^16=+1, as implemented.

All stored probabilities lie in[0,1] and sum to one within1.2e-16. The energy identity <h>=2sqrt(2)(p_high-p_low) agrees within7.2e-15. The ground-projector covariance is correctly formed as <P_i g,P_j g>-<P_i><P_j> for real Hermitian commuting rung projectors. Its diagonals match p(1-p) within1.2e-13 and its minimum eigenvalue is positive(.18995). The reported approximately2.06e-13 residual supports a numerical selected-sector eigenstate; it is not a global-ground certificate or exact arithmetic eigenvector. No full-state or expectation recalculation was claimed by this review.

The local frozen NPZ exists, and its SHA256 exactly matches the committed JSON declaration be3065e52bcd86cca06d3ddfde11111a8a9e68316a3d03db40be1187e4f75823. The separate eigenpair JSON identifies geometry2x2x8, selected CSS sector, numerical energies and residuals. The canonical large-column note and occupation JSON explicitly say the disposable binary is not committed, the self-contained runner does not regenerate this diagnostic, and the exact proofs do not use it. This is honest provenance for a frozen auxiliary result, not a claim of checkout-only reproducibility. A rerun of the script requires the matching local NPZ; absence elsewhere is an expected limitation rather than a hidden runner dependency.

Substantial central internal excited-space probability supports the narrow conclusion that the selected equal-coupling state is not nearly confined to the low internal rung state. It does not infer real-particle abundance, a scalar pole, a bulk state, or failure of every possible effective description. The script's adjective 'exact' should be understood as the exact finite-H model/projector definition, subject to the explicitly supplied numerical eigenpair residual.

Hashes:

- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_internal_occupation.py`: `f687fd8e24bc4a1f7c221c068c7727ceb2df26a0e4dcb66bc77135eb67167bb3`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_internal_occupation.json`: `2d609402878fe5a327b6158e3eed9e0eefb4e735eecb2666cf2893551473c16e`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/stationary_2x2x8_plus.json`: `056ec68a0ece08943d0dd1ed4daa549634a3288bdae75c6c957f9e89697c759c`
- `/private/tmp/scalar-environment-20261017/docs/NATIVE_LARGE_COLUMN_DYNAMICS_NOTE_2026-10-18.md`: `58f87669d9e58a6f632bc6d1cb1d3e2ab43a9ef44a676f36c59fd180ab6f24ea`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/EXACT_INTERNAL_FACTOR.md`: `bebe07c21ada85c2d5f153517763a8a6b998eb7ff45933602c4b1f029f01c6f1`
