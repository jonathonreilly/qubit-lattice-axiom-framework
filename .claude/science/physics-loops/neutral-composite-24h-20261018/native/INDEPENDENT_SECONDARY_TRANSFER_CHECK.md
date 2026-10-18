# Independent secondary molecule transfer/source check

Reviewed `native/SECONDARY_NEUTRAL_MOLECULE_PROOF.md`. Disposition: PASS for the stated energy transfer power counting and the zero-momentum source coefficient; DEMOTE an unqualified uniform shrinking-momentum residue claim until the additional orientation error below is included. Native motion is treated as the separately checked input.

## Growing torus and quotient

A syndrome with eight plaquettes and even row/column parity uses at most four distinct occupied rows and four distinct occupied columns. On sufficiently large transverse periods one can choose empty cuts in gaps, with an empty margin so that the cut does not delete a genuine nearest-neighbor syndrome adjacency. This converts the local syndrome incidence/perimeter classification into the planar one without imposing a bound on the empty gaps. On a large torus it is preferable to say “cuts through sufficiently long empty gaps,” not merely any empty coordinate.

The inverse column configuration is determined only modulo full row/column flips. These are precisely the flat ambiguities being quotiented in the positive plane sector. Do not count the different inverses as different localized shapes. Very long rods are legitimate representatives until this quotient is imposed; a finite coordinate enumeration alone would miss them. Given the independent exhaustive classification, the order-eight diagonal separation from the axial-three family is uniform: the gap to the next listed shape is Jv lambda^8/2. This argument is a syndrome-space reduction and does not require the inverse rod itself to have bounded column support. The inherited local Q-relative estimate is essential for controlling long representatives.

## Avoided crossing and microscopic energy accuracy

The orientation diagonal difference is O(J lambda^12 (qx^2-qy^2)), while the nonzero offdiagonal splitting scale is J lambda^20. For |q|<<lambda^4 its second-order effect is O(J lambda^4 |q|^4), agreeing with the note. Its leading lower-branch curvature is therefore isotropic with the quoted (5/2) J gamma^2/v lambda^12 coefficient; the other local correction is O(J lambda^14 q^2).

For allowed q=2pi n/R with fixed n and R~lambda^(-p), p>4, the dispersion increment is of order J lambda^(12+2p). A FINAL remainder epsilon=O(J R^2 lambda^M), meaning after every reduction and its denominator losses, is relatively negligible if

    M > 12+4p.

The projector comparison must be made in the exact momentum and symmetry fibre. Neighboring momenta can have much smaller separations, so a gap assertion for the unrestricted full spectrum would be wrong. Within the relevant fibre the orientation companion supplies a gap of order J lambda^20 and the other retained families are farther away.

With source norm O(R), the conservative projector-induced amplitude error is O(R^3 lambda^(M-20)). Requiring this to be o(lambda^4) gives the stated condition M>24+3p. The illustrative p=5,M=70 satisfies both inequalities. These conclusions depend on the already established uniform local reductions and global-ground identification; reflection positivity supplies existence of a positive-plane global ground, not uniqueness by itself. The ground/fibre identification must continue to use the established low-Q control in that sector.

## Explicit source normalization and UV coefficient

To avoid ambiguity about “symmetrized,” an explicit consistent convention is

    B_(r,a) = (D^X_r D^X_(r+3e_a) + D^Y_r D^Y_(r+3e_a))/2,
    O_q = (1/(sqrt(2) R)) sum_(r,a=x,y)
              exp(-iq.(r+3e_a/2)) B_(r,a).

Here D^X and D^Y are the original length-L physical column Pauli products. The factor 1/2 in the X/Y average is necessary. For L=10 their pair products have the same N0 projection. The two distinct shape orientations then give unit total leading creation norm and the equal-orientation vector.

A pair at separation three reverses 4L YY virtual-bond signs for the X-column product, or 4L XX signs for the Y product. With first-wall amplitude lambda/8, the canonical second-order source amplitude is

    1 - 2*(4L)*(lambda/8)^2
      = 1 - L lambda^2/8.

Squaring gives 1-L lambda^2/4+O(lambda^4). Taking the X/Y average does not double this correction: it is the linear average of equal matched amplitudes. Shape mixing starts at amplitude lambda^2 and is orthogonal to the original bare endpoint shape, hence changes its weight first at order lambda^4. Checkerboard lambda parity removes odd scalar corrections in the matched convention.

## Required nonzero-momentum qualification

The UV calculation just above does not remove the orientation rotation at nonzero q. For a fixed equal-orientation source the lower-branch eigenvector differs from the symmetric vector by angle

    theta = O((qx^2-qy^2)/lambda^8).

Its source weight therefore has an additional relative error

    O((qx^2-qy^2)^2/lambda^16),

conservatively O(|q|^4/lambda^16). Consequently a uniform statement is

    weight = 1-L lambda^2/4
             + O(lambda^4 + |q|^4/lambda^16)
             + microscopic remainder,

with the usual small-q and local-source regularity assumptions. At q=0 this reduces to the note's formula. At a generic fixed momentum index on R~lambda^(-p), the added term scales as lambda^(4p-16). For 4<p<5 it need not be O(lambda^4); for p near four it can even dominate the displayed lambda^2 correction. The q=0 claim, p>=5 generic sequence, or symmetry-line qx=plus/minus qy can retain the simpler residue expression. This affects the claimed accuracy of the weight, not existence of the mode or the leading energy curvature.

## Ground expectation and neutrality

This two-column source is plane-neutral, so it is NOT orthogonal to the ground by a charge-sector selection rule. At q=0 subtract its one-point expectation when invoking connected Gram bounds or interpreting total inelastic weight. At nonzero allowed q the expectation vanishes in a translation eigenstate, but the state/fibre convention must be explicit. Alternatively define the result directly by a spectral projector onto the positive-energy molecular window; that projector removes the ground component automatically and leaves the pole matrix element unchanged.

Even a very small per-site expectation can become extensive under the O(R) collective normalization, so centering cannot be omitted merely on the basis of a fixed-order local estimate when arbitrary polynomial boxes are allowed. The centered operator still has norm O(R), leaving the source-tail power counting intact.

The corrected statement derives a transverse square-symmetric native excitation and a specified microscopic spin-string readout. It supplies no laboratory detector identity, universal charge, three-dimensional Lorentz metric, or emission rate.

## Resolution after root revision

Re-read the revised physical-source section. It now gives the explicit center phases and X/Y average, subtracts the exact q=0 expectation, states the simple residue at q=0, and separately retains O(|q|^4/lambda^16) for generic momentum, with p>=5 as the sufficient first-grid restriction. These changes resolve the requested demotion. Final disposition: PASS within the stated inherited normal-form and fibre-gap scope; no remaining identified transfer/source issue in this review.
