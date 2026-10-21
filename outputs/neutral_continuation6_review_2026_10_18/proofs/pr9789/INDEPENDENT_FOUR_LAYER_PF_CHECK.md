<!-- Original PR9789 source SHA256 65aeb1519fcebc685329fc40d407167097e44c382191eee09ce442207dd6aca2. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Four-layer coefficient model: global-ground PF check

Disposition: PASS. The all-row/column-X-positive block is a justified global-ground benchmark, not an arbitrary selected sector. The argument can be sharpened to exact coefficient-ground multiplicities: one for even R, two for odd R (R>=2). Read /tmp/neutral_four_layer_root.md. No canonical/shared edits.

## Z-basis connectivity and symmetries

On the connected open R x R transverse grid, the binary vectors corresponding to nearest-neighbor pair flips span the full even-weight subspace: along a path, summing its edge vectors flips only its endpoints. Hence the -5XX off-diagonal moves connect every Z configuration of a fixed global parity Z_all=product_i Z_i. The diagonal plaquette term does not alter irreducibility. Perron-Frobenius, after a scalar shift, gives a unique strictly positive lowest vector in each parity sector. These conclusions hold despite arbitrary diagonal entries.

Each complete row-X or column-X product commutes with K and is a nonnegative permutation in this Z basis. For even R it preserves global Z parity. Acting on its strictly positive unique sector ground must therefore give eigenvalue +1, not -1. Both parity-sector ground vectors lie in the all-positive row/column block, and whichever has lower energy is a global ground there.

For odd R, every single row-X and column-X exchanges the two global Z parity sectors. It maps the normalized positive sector ground to the normalized positive ground of the other sector with no minus sign. This proves their energies are equal. Products of two such generators preserve parity and act positively. The sums and differences of the positive parity-sector grounds consequently have, respectively, all row/column eigenvalues +1 and all -1. No other combination of row/column characters occurs in the global ground space, since each global parity sector has only one ground vector. Thus the global coefficient ground multiplicity is exactly two for odd R.

Global Z commutes with K and O and maps the all-positive and all-negative ground vectors into one another. Their O spectral responses agree. Moreover O preserves all row/column characters, so cross terms between these two sectors vanish in O correlation/spectral expressions. The same response therefore holds for arbitrary coherent superpositions or mixtures in this ground doublet, not merely for the two chosen basis vectors.

## X-basis block and strengthened even-R conclusion

In the X basis, the all-positive constraints are even bit parity in each row and column. There are 2R constraints with one dependency, so the solution dimension is 2^(R^2-2R+1)=2^((R-1)^2). Choosing the upper-left (R-1)x(R-1) bits freely and filling the last row/column gives exactly the stated four-corner generators. The numerical dimensions 2,16,512,65536,33554432 for R=2,...,6 are correct.

The elementary plaquette-flip vectors themselves span this constrained binary space: summing plaquettes in a rectangle generates its four-corner pattern, including each free-bit generator. Thus the -4 plaquette off-diagonal moves make K irreducible within the all-positive X block. Perron-Frobenius gives a UNIQUE ground vector in that block.

For even R, the two global-Z parity ground vectors already lie in this block. They cannot have equal energy, since that would contradict its unique lowest eigenvector. Therefore the full K has a unique global ground for even R. More specifically, Z_all acts as the all-bit-complement permutation within the constrained X block when R is even. It is nonnegative and commutes with K, so the positive block ground has Z_all=+1. The odd global-parity sector is strictly higher. For odd R the complement maps the all-positive block to the all-negative block instead, consistently with the exact doublet above.

These are finite-dimensional strict-gap statements: after accounting for the stated one- or two-dimensional ground space, the next coefficient eigenvalue is strictly higher. PF supplies positivity of that gap at each fixed R, not a useful numerical lower bound or a uniform gap as R grows.

## Native-transfer qualification

The given order-four coefficients are consistent with the previously checked periodic L=4 winding coefficient gamma_4=5Jz lambda^4/128 and A_4=36/5: the source winding coefficient is -18lambda^4/(128sqrt(V)); the diagonal source coefficient is -12lambda^4 sum P/(128sqrt(V)). Thus O=3K-3sum XX is algebraically consistent. The completeness of the native order-four graph classification remains its separate supplied premise.

At fixed R, if that classification and the exact wallfree block reduction hold, its coefficient ground gap and the O(Jz) wall gap justify perturbative convergence of actual ground vectors into this global coefficient ground space as lambda tends to zero. The leading source response must still be transferred with the appropriate operator/error estimates. No uniform R-growth transfer follows from PF alone. For odd R, preserving the exact physical symmetry representation is necessary when invoking protected degeneracy beyond leading order; the coefficient PF proof itself does not replace that check.

The result establishes a valid global-ground coefficient benchmark for the original native slab. It does not by itself identify a collective particle, scalar mode, observed coupling, or large-R phase.
