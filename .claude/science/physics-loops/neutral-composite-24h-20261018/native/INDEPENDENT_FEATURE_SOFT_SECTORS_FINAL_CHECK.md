# Focused final check: native feature soft sectors

Reviewed `native/FEATURE_SOFT_SECTORS_PROOF.md`, `docs/NATIVE_FEATURE_SOFT_SECTORS_NOTE_2026-10-18.md`, `scripts/native_feature_soft_sectors.py`, the orbit control, and the relevant statements of `NATIVE_DRESSED_PATCH_PROOF.md` in the scalar-environment worktree. This is an independent mathematical/source check, not a formal audit or a new spectrum calculation.

## Correction made during review

The initial section 2 exchanged the plane normals. For H=-J(ZZ_z+lambda XX_x+lambda YY_y), the exact symmetries are X on x-normal planes and Y on y-normal planes. X on a y-normal plane would anticommute with crossing Y bonds. Root corrected this label error; I verified the corrected lines. No orbit count or energy coefficient changes.

## Mathematical conclusion

The corrected proof supports the stated count, conditional on its cited dressed-patch theorem and uniform normal-form bounds. The orbit compression argument is sufficient for minmax without asserting invariance of the trial space. The exact odd physical-Z restriction excludes N=0, and the cited wall-relative estimate excludes N>=4 near the heavy energy. Half-column N=2 states are even and are likewise excluded. Thus the minmax eigenvalues are actual odd heavy levels, rather than vacuum levels accidentally counted by unrestricted minmax.

The pure outside vector is chosen once from a convex decomposition; symmetry generates the remaining trials without any repeated optimization. The subgroup has a free orthogonal orbit of size 2^(2m-1). Character Fourier sums are therefore nonzero and provide a variational vector in every selected character. Distinct characters need not have distinct energies. Both the proof and public note correctly count eigenvalues with multiplicity and avoid claiming a tower of visible frequencies.

The physical flip bound 4m-2>8 holds for m>=3 and applies to the retained order-four winding terms too. A global remainder in operator norm bounds the whole trial span without multiplying by its dimension. The asymptotic regime m~lambda^(-3/4) is safely above this finite threshold and fits inside R~lambda^(-1).

The original C_Q commutes with these planes for every allowed Fourier momentum: each longitudinal distance-two pair intersects an x- or y-normal plane twice or not at all. The phase multiplying the pair does not change commutation. Equivariant dressing preserves the selection rule. Therefore matrix elements between distinct selected characters vanish exactly; this statement needs no quantitative source-residue estimate. No result here supplies a neutral-accessible mode within a fixed character.

## Replay and dependency scope

I replayed `neutral_patch_orbit_control.py` directly, avoiding generated repository outputs. It passed m=2,...,6, with orbit sizes 8,32,128,512,2048 and minimum column differences m. The m=2 row has physical difference 6<=8 and is only an orbit count, not an order-four separation certificate; the proof correctly requires large m. The control labels its finite algebraic scope honestly.

The runner executes this finite control and records bounded-support scope. It does not numerically prove the asymptotic patch energy, SW remainder or wall-relative separation. Those remain analytic dependencies on `NATIVE_DRESSED_PATCH_PROOF.md` and its referenced local-normal-form results. The declared inputs include the soft-sector proof, dressed-patch proof, probe-loop proof and control; they are not a standalone manifest of every transitive normal-form dependency. Do not describe this runner alone as a full independent replay of those earlier theorems. The present public note does not make that claim.

With the plane-normal correction, no further blocking issue was found in this focused review. The result remains a supplied-Hamiltonian, fixed-height weak-coupling statement, not empirical particle identification, a scalar pole or a statistical-species derivation.
