# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Independent X-basis subsystem-charge representation check

The affine constraints, even-torus complement quotient, boundary-seed source matrix element and paired readout formula check. Independent full-logical-space controls were performed for vacuum, single and vertical-dipole charge patterns on3x3,3x4 and4x4. These small periods are representation controls only, not native coefficient tests.

Control script: /private/tmp/neutral-four-column-charges-independent.py
Output: /private/tmp/neutral-four-column-charges-independent.json

## Affine spin coordinates

In the X eigenbasis write x_xy in{0,1}. Row and column products impose XOR constraints r_x and c_y, with the required consistency XOR_x r_x=XOR_y c_y. Taking the (nx-1)(ny-1) interior bits as free gives

x_(x,last)=r_x XOR XOR_(y<last)x_xy,
x_(last,y)=c_y XOR XOR_(x<last)x_xy,
x_(last,last)=r_last XOR XOR_(y<last)c_y XOR XOR_allfree x_xy.

These are precisely setup's masks/constants. The unconsolidated sector dimension is2^((nx-1)(ny-1)). XX bonds are diagonal products of these affine X spins, with minus sign and coefficient t/K=8/9. Each physical plaquette Z product flips its four X bits and preserves every row/column charge. Restricting that flip to the free bits gives the code's plaquette mask. All physical plaquettes are retained even if reduced masks coincide, so their multiplicities are correct.

## Both-even complement quotient

When both transverse lengths are even, flipping every X spin preserves all row and column charges. It is the action of the global physical Z product, an additional commuting symmetry. Its plus-sector orbit basis is

(|free q>+|free q XOR allones>)/sqrt(2).

The code fixes the highest free bit to zero and, when a plaquette mask would flip it, XORs the mask with allones. There is no extra sign in the plus sector. The diagonal XX energy is invariant under this complement, so evaluating it on the chosen representative is correct. The dimension is reduced by another factor two. If either length is odd, complement changes at least one charge and must not be quotiented within a fixed charge sector; the code correctly omits it.

This is a selected plus global-Z sector, not automatic inclusion of both global-Z signs or a proof of the global ground sector.

## Explicit full-space controls

I enumerated full physical X-spin configurations, imposed the physical charge constraints directly, and built the normalized sparse isometry W into each selected sector. I then constructed H_full W directly from physical XX diagonals and physical plaquette Z flips, independently of the code's affine masks.

For all three tested charge patterns:

-3x3: full space512, selected charge dimension16, quotient16;
-3x4: full space4096, selected charge dimension64, quotient64;
-4x4: full space65536, selected charge dimension512, complement-plus quotient256.

The maximum element of H_full W-W H_code was zero in every case. W†W error was zero for the first two shapes and2.22e-16 for4x4. Every4x4 isometry had exactly zero global-complement-plus error. Thus the tests cover the full reduced matrices, not just a few eigenvalues.

## Meaning of gs0 dot gscharge

A product of physical Z at the specified seed sites flips those X bits. Because every chosen site is on the final row or final column, it changes only affine boundary coordinates and the charges, leaving all free interior bits unchanged. In the both-even case the same operation commutes with global Z and preserves the complement pairing and its plus sign. Consequently

W_charge† Z_seed W_vac=I

in these matched coordinate bases. I checked this identity exactly for all tested patterns and shapes. It justifies |gs0† gscharge|² as the transition weight of THIS specified seed operator between the two selected ground vectors.

It is not the physical overlap of the states themselves: different charge sectors are orthogonal. If a seed includes interior sites, a nontrivial free-bit XOR must be inserted; the plain dot product would then be wrong. Degenerate ground subspaces also require a projector/summed-overlap treatment if a basis-independent weight is intended.

## Paired native readout identity

Taking the supplied L4 coefficient/source relation as input, the physical leading excitation energy is

Delta E_phys/Jz=lambda4*(9/64)*gap_code.

The paired readout identity gives

Delta C/lambda4=3*(9/64)*gap_code+(3/128)*Delta<P>.

Dividing gives3+Delta<P>/(6 gap_code), exactly the implemented expression. The code also extracts <P> correctly from H=t diag-sum P: <P>=t<diag>-E. The ratio is undefined at zero gap; the code avoids the exact zero denominator but a near-zero numerical gap would still require uncertainty handling.

This algebra is consistent with the L4 source coefficients: the plaquette term differs from3H/Jz by+(3/128)lambda4 sum P, while the pair-flip derivative supplies the3H/Jz part. I did not independently replay the newly supplied full16-physical-site native coefficient test in this focused representation check.

These values are sector-dependent diagonal responses of a specified native readout, not gravitational charge, equivalence-principle measurements, particle statistics or a physical matter identification. Selected-sector Ritz residuals alone do not certify all charge sectors or thermodynamic behavior.
