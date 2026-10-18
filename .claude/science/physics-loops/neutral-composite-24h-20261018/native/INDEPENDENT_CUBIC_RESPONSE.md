# Independent check: periodic 27-spin cube response

Reviewed the model, signed-sector extension, response reconstruction, and recorded outputs. Independently checked physical-to-logical action by explicit normalized stabilizer orbits; no large eigensolve was repeated.

## Pauli convention and representation control

The representation is p X^x Z^z, acting on a computational bitstring s with phase p*(-1)^(s dot z). Multiplication accordingly contributes (-1)^(z dot y). Since Y=i XZ, the native -YY bond is +XXZZ, while four Y factors in a plaquette have phase +1. The two-Y-plane product has 18 Y factors and phase -1 before inserting the desired character. These conventions agree with the source.

The reducer applies the stabilizer phase on the pre-flip computational string and then flips the X mask, which is the correct signed-orbit reduction. The affine pure-Z constraints incorporate negative characters. The output-side implementation of the reduced operator evaluates its phase on input i=j xor x, also correctly.

Independent control `/private/tmp/neutral_cube_map_independent.py` constructs each physical orbit directly by projecting the four commuting X-containing original generators onto the affine representative. Each orbit contains 16 computational states and is normalized. For each of the four character representatives, eight randomly selected logical basis vectors were tested separately for H and S. Both intertwining identities Hphysical W=W Hlogical and Sphysical W=W Slogical had maximum discrepancy exactly zero. This tests the updated negative-sector signs as well as the all-positive block.

## What the two sources measure

S is the sum of four-spin plaquettes normal to each axis, with the Pauli component along that normal. Under a simultaneous cubic spatial/spin rotation, plaquette orientations permute and the four spin signs multiply to +1. Thus S is a cubic scalar of this finite Hamiltonian. It is not the original distance-two readout C, and no cosmological or electromagnetic identification follows.

The second source is B=Hz-(Hx+Hy)/2. It is an axis-selecting component of the cubic nematic representation, not a cubic scalar. Comparing its response with S is useful precisely because they are distinct symmetry probes.

On a periodic length-three longitudinal cycle, the sites z-1 and z+1 are nearest neighbors. Summing the original Cz over centers counts each Z bond once, so Cz=-Hz for Jz=1. Since B=(3/2)Hz-H/2,

Cz=-(2/3)B-(1/3)H.

For an exact energy eigenstate, the connected H source annihilates that state. Therefore the connected Cz source is exactly -(2/3) times the B source, with spectral weights 4/9 times the B weights. Summing the analogous C over all three axes gives -H and no finite-frequency response. These are finite L=3 aliases and cannot be imported as identities on a larger grid.

## Response reconstruction and numerical evidence

The response vector is centered as (O-<O>)g, with squared norm equal to its variance. The Lanczos tridiagonal represents H-E0 on the generated source Krylov space; its initial-component weights sum to that variance in exact orthonormal arithmetic. The code replays the basis, constructs selected Ritz vectors, renormalizes them, and directly evaluates their Rayleigh energies, full-H residuals and squared source overlaps. The two-pass check substantially improves upon treating all quadrature nodes as eigenmodes.

The recorded ground residual is 2.55e-11. For S, two selected lines have small direct residuals: gaps approximately 3.763565916 and 6.797207495, with weights 58.33658731 and 13.79813421. Three other selected S nodes fail the stated 1e-8 residual threshold and are correctly marked unaccepted. For B, four selected lines pass, at gaps approximately 1.423237955, 5.119443487, 5.315798341 and 6.932304652; the node near 10.384677407 fails. These weights are for the unnormalized summed sources.

There is no full Lanczos reorthogonalization. Loss of orthogonality may create ghost quadrature nodes; direct residuals identify good approximate eigenvectors but do not by themselves certify distinct spectral multiplicities or precise weights without isolation controls. The accepted listed gaps are distinct. Only the largest selected quadrature weights were reconstructed, so this does not certify absence of other low-energy or low-weight lines. A small residual bounds distance to some exact eigenvalue, not the global spectral ordering or a complete response measure.

## Sector scan and claim boundary

The updated defect characters correctly select one representative in each of the four isotropic classes. The recorded candidate lowest energies are approximately -38.1916498924, -37.7277035789, -37.0941927629 and -36.3938001135 for k=0,1,2,3. Their small residuals support the computed eigenpairs; the four-class symmetry reduction is exact. Ordinary `eigsh(which='SA')` plus residuals nevertheless is not a rigorous lower-bound certificate excluding a missed lower eigenvalue. Appropriate wording is that the four representative lowest-eigenvalue searches found the k=0 candidate lowest, rather than claiming a formal ground-state proof solely from residuals.

All conclusions concern this finite periodic 27-physical-spin Hamiltonian. The protected plane doublet, character sectors, finite-size aliases and reconstructed source lines do not establish a thermodynamic phase, propagating bulk scalar, force law, or empirical correspondence.
