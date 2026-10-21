<!-- Original PR9818 source SHA256 18de722c2884213785d4418e59d16ea4b6d62e0ee2402062093f74c06555128e. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Independent flat-character locality check

Disposition: PASS for character-independent fixed-order local coefficients and matched finite-time neutral collision physics, subject to the uniform normal-form bounds already established. Two qualifications are essential: arbitrary character-sector vacua need not be exact GLOBAL grounds, and a generic character sector is not invariant under physical translations.

## Group and physical-plane labels

For an even R by R transverse torus at even height L=10, flat column patterns are

    f_(x,y)=a_x+b_y modulo two.

The common shift of every a and every b is redundant. The row/column flip group G therefore has size 2^(2R-1), acts freely and transitively on these computational flat patterns, and obeys product(all row flips)=product(all column flips). Its compatible one-dimensional characters satisfy the same product relation.

Physical X planes implement one family of these flips. In N0 a whole Y column is i^L Xbar Zbar=-Xbar for L=10, since Zbar=product_z Z=+1 on either aligned column. A Y plane contains R columns, so its extra sign is (-1)^R=+1. Thus the other physical plane family implements the other flat flips with no residual phase. Every physical Z plane evaluates to (-1)^(sum f)=+1 because R is even. These facts justify the proposed positive Z-plane restriction and the untwisted X/Y character identification in this geometry. They should not be assumed unchanged for odd R or odd height.

For each compatible real character chi,

    |Omega_chi> = |G|^(-1/2) sum_g chi(g)|g>

is the unique flat vector in that character sector. Orthogonality follows from the regular representation.

## Minimum flat difference and local matrix elements

A nontrivial flat difference changes at least R columns. For example if n rows and m columns are toggled, its weight is R(n+m)-2nm; minimizing over nonidentity patterns gives R. Therefore a pure column-X word changing fewer than R columns cannot represent a nontrivial element of G.

However, this support statement by itself does NOT apply to an arbitrary local operator. One must also require the physical plane invariance of the operator, as the root does for native coefficients and neutral readouts. A local Z word need not preserve characters or have the asserted diagonal property.

For a plane-invariant Pauli word with column-X support A, a matrix element between flat configurations can be nonzero only if A is their flat difference. If |A|<R this forces A empty. Its diagonal value is then constant on the flat orbit by plane invariance. Thus its compression to the flat manifold is a scalar, identical in every chi. Linear combinations give the same conclusion termwise. This is the exact finite-order reason, rather than an appeal to near-degenerate energies alone.

For defect words D_A=product_(r in A) Xbar_r, use orbit states D_A|Omega_chi>. Their Gram is zero unless A symmetric-difference B belongs to G. In particular distinct unordered two-column sets give orthonormal states when R>4; coincident endpoints should be excluded or recognized as the vacuum. The same physical local plane-invariant coefficient has identical matrix elements between A and B whenever

    |A symmetric-difference B| + |X-support of coefficient| < R.

The reason is that a nontrivial flat difference cannot then connect two different orbit representatives. The surviving diagonal-orbit terms have constant amplitudes and chi(g)^2=1. This proves the character independence of the local winding adjacency and local diagonal potentials in the two-column subspace.

The relevant bound concerns the NUMBER of flipped columns, not just a small diameter or the phrase “local word.” At each fixed normal-form order the support bound is finite and independent of R. High-order words whose support can realize a complete flat row/column are the first possible source of character dependence. Local vacuum-returned identity pieces cannot generate a hidden character phase.

## Actual sector vacua and errors

The equivariant local normal forms preserve every plane-character sector. At fixed final order M and polynomial R, eventually R exceeds every retained local support. The retained Q0 compression is then the same scalar in every sector, and each Q0 sector has rank one. Combined with the inherited global lower bound and order-lambda^4 defect gap, the exact lowest eigenvalue IN EACH CHARACTER SECTOR differs from this scalar by at most O(J R^2 lambda^M), with corresponding projector control after dividing by the gap. Hence the sector-vacuum energies agree to this accuracy uniformly over chi. No factor |G| is needed: the estimates are operator-norm/relative-form estimates, not a sum of sector errors.

This does NOT prove that all these exact sector vacua are global ground states. Winding effects beyond every fixed retained order in the polynomial limit can split their energies. Reflection positivity establishes existence of a global ground in the positive sector; it does not make every other sector globally minimizing. A finite collision prepared on another exact sector vacuum is still well defined, using that vacuum's own energy reference. Its preparation is a state choice, not a derived thermodynamic selection.

## Translation and finite collisions

A physical translation permutes row/column character patterns. Generic chi is not fixed by this action, so a fixed generic character sector has no physical momentum quantum number. It is nevertheless legitimate to prepare a relative-coordinate packet, or a uniform center superposition in the defect-coordinate basis, because the fixed-order local pair matrix is the same. That coordinate construction must not be described as an exact physical zero-momentum eigenstate in the generic sector.

The derived collision can therefore be transferred to any compatible chi by using the same matched defect-coordinate preparation and readout and the same uniform norm bounds. Local retained coefficients are identical; the remainder is uniform; no sum over exponentially many character sectors is required. The common rest energy must be referenced consistently to the chosen sector vacuum. Long wrapping/support processes remain in the controlled remainder. At finite time their possible character phases are bounded by the same norm error.

For this statement, verify that the normal forms/readouts used in the collision are plane invariant and retain the stated finite support or uniformly controlled tails. A proof that silently selects a physical momentum fibre inside an arbitrary chi sector would need to be reformulated as the coordinate-packet comparison above. The result removes the choice of X/Y character from this local neutral finite-time observable to the proved accuracy; it does not remove the Hamiltonian, height, weak-coupling, prepared-state, or measurement-identification premises.
