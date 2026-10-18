# Independent native/effective anisotropy comparison check

Reviewed `native/neutral_tube_anisotropy.py/json`, `neutral_open_xy_comparison.py/json`, and `neutral_anisotropy_comparison.py/json`, plus the stored linked-fourth-order coefficient conventions. No expensive native scan was replayed. Existing warm-start diagnostics were found and left unchanged.

## Matching plane sectors

The native calculation fixes positive rung Z parities, the original X-plane pair, and individual X/Y plane signs +1. For each tested even L=4,6,8, a Y plane contains 2L physical Ys and its computational coefficient is i^(2L)=+1, so the code's sign is correct. The two additional individual generators commute with the pre-existing constraints and are independent.

In the low rung doublet the physical generators are P_x=−tau1 and P_y=−tau2 for the specified tau convention. I independently checked these compressions using the full eight-state rung matrices, obtaining overlaps −1 to numerical precision. Because L is even, global physical products correspond to global collective X and Y with no residual minus sign.

The effective W pairs bit strings with their complements with PLUS amplitudes, fixing global X=+1. It also selects bit parity n mod2=(L/2) mod2. Since product_j Y_j=i^L(product_j X_j)(product_j Z_j), this parity choice makes global Y=+1 as well. Thus its sector is the intended native low-band sector, rather than a half-filling-only or arbitrary parity restriction. Independent bit checks give dimensions 4,16,64 for L=4,6,8. The basis permits all compatible magnetizations, not only exactly half filling.

## Fourth-order energy normalization

At J_perp=1, lambda=J_z/J_perp and t=lambda²/sqrt(2). The stored physical fourth-order coefficient has an overall 1/sqrt(2) multiplying the bond/triple bracket used as V4. Dividing H_eff by t gives

H_eff/t = constant + [−(1/2)sum(XX+YY)] + lambda² V4 + O(lambda^4).

Therefore the effective code's H+lambda² V4 has the correct normalization; it should NOT include another 1/sqrt(2). The written bond coefficients (−I/32+XY/16−5ZZ/32) and overlapping-triple coefficients (−I/8−(XY_left+XY_right)/16−3XY_next/16) match that stored bracket. Constant terms drop out of gaps but have been counted consistently.

Accordingly the comparison's `error_over_lambda4` is the appropriate expected scaling diagnostic for gaps already divided by t. An O(lambda^4) error in gaps/t corresponds to O(lambda^6) absolute energy error. This check verifies normalization and consistency with the stored fourth-order derivation, not a fresh derivation or uniform linked-cluster theorem for that coefficient.

## Original readout and weight scaling

The native probe is the sum of all existing longitudinal distance-two column composites, divided by sqrt(L−2), then centered in the actual native state. Each column sums four physical ZZ pairs; no transverse factor of 1/4 is included.

The effective probe uses the stated second-order readout

O2=(3/8)/sqrt(L−2) sum_(j=0..L−3) [XY_(j,j+1)+XY_(j+1,j+2)+XY_(j,j+2)].

The omitted elastic constant does not affect the connected transition weights. For low-band transitions the physical source amplitude is lambda² times this O2 matrix element plus higher corrections; its weight is consequently lambda^4 times the leading squared amplitude. The comparison correctly divides the native SELECTED LOW-MODE weight by lambda^4 before comparison with O2 weights.

This scaling does not apply to the entire native source norm or high-energy transitions: the original C can connect the unperturbed low band to high rung states at lower order. No claim that all native spectral weight disappears as lambda^4 is justified. Using fourth-order eigenvectors while retaining only O2 also leaves a missing next-order observable dressing; differences in normalized low-mode weights can be O(lambda²), even when the gap approximation is more accurate.

## What the weak-ratio data support

For lambda=0.1, the largest supplied gap/t discrepancies are 4.6513e−5 (L4), 9.0913e−5 (L6), and 1.0288e−4 (L8). Dividing by lambda^4 gives approximately .4651,.9091,1.0288, close to the corresponding weak-ratio trends at lambda=.2. This supports the expected finite-size perturbative scaling, without proving a uniform-in-L error bound or thermodynamic convergence.

For the index-2 readout comparison, the normalized weight differences at lambda=.2 and .1 are respectively:

- L4: .0545038 and .0136686;
- L6: .0337066 and .00799285;
- L8: .0174203 and .00404091.

Their division by lambda² is approximately stable toward the weak endpoint, consistent with omitted higher observable/state corrections. This is development-model validation, not an independent empirical test, and not exact agreement at finite lambda.

## Level ordering and numerical completeness

At stronger coupling, sorted index two can correspond to different states in the native and truncated models. In particular a nearly dark native index-2 state at lambda=1 cannot be interpreted as the same mode as a bright effective index-2 state without additional symmetry/overlap matching. Comparing sorted low energies can still diagnose truncation mismatch, but comparing individual weights requires branch identification and treatment of degeneracies. An index label is not a physical mode identifier.

The amended native code adds a normalized deterministic random component of size .1 to the warm vector before each solve. This addresses the concrete failure where a pure warm ground vector trapped the Krylov space in an additional exact symmetry block. Small residuals alone would not expose that incompleteness. The original code/results remain in `native/diagnostics/anisotropy_warmstart_before_fix.py` and `.json`; they should remain recorded as failed numerical discovery controls, not as evidence for absent states. I did not alter them.

The repaired run's random-component start and residual checks are materially better evidence, but four found Ritz eigenpairs are not a certified complete low spectrum. The comparison script correctly labels the results finite and selected-sector. No global ground-sector survey, equal-coupling validity of the truncation, bulk critical phase, physical matter identity, or cosmological coupling follows.
