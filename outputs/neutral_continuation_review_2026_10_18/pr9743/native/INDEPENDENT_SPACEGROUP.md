# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Independent space-group representation check

Checked 2026-10-18. Scope: the existing 36-spin periodic 3x3x4 native compass Hamiltonian, its selected plane sector, and its translation/D4xy/z-reflection invariant subspace. No full-Hilbert dense arrays or eigensolver replay were used.

## Exact symmetry and dimension

The 576 coordinate maps are translations (36) times D4xy (8) times z reflection (2). Coordinate reflections alone preserve undirected compass bonds. An xy coordinate swap combined with global S=diag(1,i) sends X to Y, Y to -X and Z to Z; the minus signs cancel on each bond. This is a symmetry when Jx=Jy. It is not the full cubic point group on this rectangular geometry.

On this selected sector global Z is +1. Thus computational support has even down-spin count, the S phase is the real sign (-1)^(Ndown/2), and S squared acts as identity on the sector. On the full physical Hilbert space S squared is global Z instead: one must not omit that qualification. X and Y planes have 12 sites, so the extra sign from rotating Y planes is +; the selected plane characters are preserved. Z-relative characters are merely permuted.

Independent script `/private/tmp/neutral_spacegroup_independent_check.py` constructed the physical coordinate maps separately, expanded selected logical states into their 32-term physical stabilizer orbits, and compared the physical permutation/spin phase against the parent affine/quadratic logical maps. Maximum error was exactly zero. One hundred random signed group-composition and Hamiltonian-commutation controls passed exactly.

An independent GF(2) fixed-point solve and quadratic Gauss-sum evaluation of each signed transformation trace gives

    dim invariant = (1/576) sum_g Tr U_g = 475194.

This matches the saved orbit enumeration exactly. The character trace includes signs; an unsigned permutation-orbit count would be insufficient. Data: `/private/tmp/neutral_spacegroup_independent_check.json`.

## Normalization and numerical scope

Signed-orbit sums normalized by sqrt(orbit size) give the stated representative matrix-element factor sqrt(output size/input size), with the sign of the input orbit representative transport. Invariant vectors in the translation-only representation embed into the larger-group orbit sums with sqrt(old orbit size/new orbit size). Parent's saved projection error is 1.9155e-14, consistent with this formula and ground membership in the smaller invariant space.

Saved low.json has dimension 475194 and ground energy -49.970264103705546 with residual 1.51e-13. The first 19 residuals are approximately 1e-13; the twentieth is 9.08e-12. These support approximate eigenpairs of this selected symmetry block, not a certified global ground, completeness of all sectors, or a thermodynamic particle. Original Cz is invariant under this group, so its action on an invariant initial state stays in the block. At z length four Cz is not the length-three identity -Hz.

## Corrected Q projection

The reported failure from composing individually spatially projected Hx and Hy is real and important: P A P B P is generally not P A B P when A or B leaves the retained irrep. Hx and Hy individually do so under xy swap. Their invariant linear combinations can be projected linearly, but their nested products must first be formed before the space-group projection.

The corrected response script forms sum_a [Ha,[H,Ha]] in the full selected-plane logical Pauli algebra, then applies orbit_op once. Every Ha preserves the plane sector, so performing the algebra after the plane reduction is exact. This fixes the issue without requiring a full physical-Hilbert calculation.

Independent `/private/tmp/neutral_sg_Q_independent.py` compared these raw logical nested commutators with the separately derived local formula 4 sum_(b,f,a!=b) Af K_af^2. Both produce 1404 nonzero combined Pauli terms and maximum coefficient discrepancy exactly zero. Thus the corrected Q algebra is independently validated. I did not rerun the large-vector Q response contraction. The corrected saved response has mean 2920.7719554525393, consistent with the parent's raw-q0 mean rather than the rejected approximately 3247 value. Preserve response_before_Q_projection_fix.json as a failed implementation record; none of its Q results should be used. Native H, its ground, and low eigenpairs are unaffected by this operator-construction error.

No new interaction, empirical source identification, isotropic bulk spectrum, or continuum scalar conclusion follows from this representation check.
