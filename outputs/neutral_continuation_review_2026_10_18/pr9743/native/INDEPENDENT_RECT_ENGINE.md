# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Independent check: 3x3x4 physical-spin engine

Reviewed the rectangular plane reduction, affine/quadratic translation tables, orbit matvec, ground-search driver, and recorded JSON. Independent scratch controls are in `/private/tmp/neutral_rect_independent_check.py`. No dense 36-spin or 2^28 vector was allocated, and the eigensolve was not repeated.

## Plane sector and physical map

On 3x3x4, X and Y planes commute because their intersection has length four. Each X or Y plane anticommutes with a Z plane because those intersections have length three. Thus the chosen three individual X planes, three individual Y planes, and three adjacent Z-plane products commute. Of these nine generators one is redundant: the product of the X and Y plane families equals the product of all Z planes, which is already the product of two alternating Z-relative generators. The phase is positive for 36 spins. Rank is eight, leaving 28 logical bits and dimension 2^28.

The X-flip subgroup has rank five, so each computational affine representative generates a physical orbit of 32 states. I constructed these states independently by applying the original signed-generator projectors, normalized the resulting orbit, and compared physical H action to the reduced logical action for six randomly selected basis states. Maximum discrepancy was exactly zero. This tests the Y phases, affine constraints, and signed reduction together.

The special rectangular branch selects one specified plane sector. It ignores the generic `defects` parameter in that branch; it should not be presented as a scan of all rectangular sectors.

## Translation phases and group action

A site permutation maps physical bitstrings linearly. The choice of affine stabilizer representative makes its logical label action affine; reducing the signed orbit contributes a phase whose exponent is at most quadratic in the logical bits. The code extracts the affine columns from basis vectors and the phase polynomial from constant, linear and pair evaluations, which is sufficient for this Clifford/permutation action. The upper-triangular phase rows avoid double counting cross terms.

Independent physical-orbit checks for translations by the three generators and a combined shift gave exactly zero discrepancy. One hundred random logical basis/group pairs satisfied the full translation group law, including phases. Separate sparse raw-logical checks on those trials gave H T=T H exactly. Translation invariance of the chosen all-positive plane constraints ensures the action stays in this sector.

## q=0 orbit normalization and exact dimension

For a signed orbit with a positive stabilizer, the q=0 vector is the signed sum over its distinct members divided by sqrt(orbit size). A stabilizer carrying negative phase would annihilate that orbit's q=0 projection and must be excluded; the implementation performs that test. Its stored representative has identity phase +1.

For output orbit i and input orbit j, evaluating H at the output representative gives the factor sqrt(size_i/size_j), multiplied by the input member's stored sign and the Pauli phase on the input computational string. The matvec uses precisely this factor and phase convention.

Using memory-mapped saved labels, signs, representatives and sizes, five randomly selected orbit columns were reconstructed as sparse raw-logical vectors. Their projected H matrix elements agreed with the implemented formula to at most 1.78e-15.

I also computed the q=0 dimension independently by the signed Burnside formula (1/36) sum_g trace(T_g). For each translation, I solved its affine fixed-point equations and evaluated the quadratic sign sum on that affine space by exact binary Gaussian elimination. The resulting dimension is exactly 7,458,416, matching the saved orbit count. This check does not rely on scanning or trusting every stored orbit label.

The existing L=2/L=3 driver provides additional full-vector intertwiner controls on smaller representations. Its equations and normalization are consistent with the independent checks above; those separate eigensolves were not rerun here. Length-two forward-bond duplication is part of that control Hamiltonian and should not be confused with a generic large-grid bond count.

## Numerical ground-search output and scope

The recorded q=0, selected-plane-sector search found energies -49.970264103705446 and -49.089495946276855, with residuals approximately 7.17e-13 and 3.91e-9. The reported random-vector Hermiticity error is 1.04e-17. These support accurate eigenpairs within the specified finite representation; residuals alone do not certify that no lower state was missed by the iterative solver.

No other momentum or plane-sector ordering is established. The 3x3x4 geometry also breaks full cubic permutation symmetry even at equal microscopic couplings, so cubic-scalar versus nematic finite-box selection statements require care. The engine extends a finite native benchmark and does not prove a bulk scalar, a thermodynamic phase, a universal source coupling or an empirical identification.
