# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Focused check: projected second-order slow host and axial arms

The proposed Green function and conditional width coefficient check independently. The native statement supported here is a coefficient projection; the fast first-order continuum prevents an automatic autonomous slow-model reduction.

## Projected coefficient graph

For ell=2 and a non-nearest column pair, the diagonal K2 entry is -4. Moving one entire occupied column to a nearest transverse neighbor requires one bond action on each of two layers. Both orderings have intermediate cost four and product +1 (XX or YY), giving -1/2 per physical column hop. At total transverse momentum zero these give relative hopping -1. The origin is forbidden, and nearest relative separations belong to the fast K1 block, so projection to slow states removes precisely the origin and its four nearest neighbors.

For ell>=3, the preceding local classification gives only axial separation-two endpoint moves, -1/2 for X and +1/2 for Y; all non-axial pairs are stationary at K2. In the scalar basis with the Y orientation multiplied by (-1)^ell, the two longitudinal endpoints add to hopping -1. At ell=2 this attaches the normalized axial-shell state A=(|2ex>+|-2ex>+|2ey>+|-2ey>)/2 to the first long-interval scalar state with amplitude -1. Other scalar angular channels remain part of the slow host, not additional independently attachable arms in this scalar sector. Frozen long intervals remain a separate decoupled summand at this coefficient order.

Thus, within the specified parity/reference/symmetry sector, the stated active graph is the Pslow K2 Pslow graph. Projection discards nonzero K2 connections back to the fast block. It is not exact invariance under the native Hamiltonian.

The punctured two-dimensional host has diagonal -4 and hopping -1, hence essential spectrum [-8,0]; finite deletion of sites preserves that essential interval. Each unconfined long arm has spectrum [-6,-2]. Its bottom -6 lies inside the host continuum.

## Independent Green-function check

Remove the diagonal -4, so e=-6 corresponds to E=-2 for the hopping-only square lattice. Its Fourier denominator is E+2 cos x+2 cos y+i0. The five-site Schur deletion used in the root script is the standard exact resolvent of the lattice with those sites deleted (provided the finite Green block is invertible at the boundary value). The source A is normalized: its Fourier transform is cos(2x)+cos(2y), with squared torus average one.

I independently reduced the deletion to the square-invariant hole subspace spanned by the origin and normalized nearest shell N. Since H|0>=-2|N>, writing g00=<0|R|0>, g0A=<0|R|A>, gAA=<A|R|A> gives the scalar formula

Gpunct,AA = gAA - E*g0A^2/(E*g00-1).

Other hole symmetry sectors cannot couple to A. Independently evaluating these three torus integrals, analytically integrating y first, gives at E=-2:

* g00=-0.2682955017870335-0.3432201251543870 i;
* g0A=0.2047510918139752+0.1690839245716910 i;
* gAA=-0.4266162429649595-0.1261953524110140 i;
* Gpunct,AA=-0.3060521439059136-0.2464356212672203 i.

Direct finite-torus broadened integrations also approach this result as broadening decreases. The retarded square-root prescription in the supplied one-dimensional integration has the correct sign at this energy. Its current split formula is specialized to the selected energy/range, not a general-purpose all-energy lattice resolvent.

## Boundary and conditional Airy width

The endpoint coupling is -1, so Sigma=Gpunct,AA. With arm hopping -1 the ghost equation is psi0=-Sigma psi1, giving a=Sigma/(1+Sigma). Numerically

a=-0.2796521330915376-0.4544316487975155 i.

For dimensionless tension f=lambda^2/8 and kinetic unit Jz lambda^2, the Airy length is f^(-1/3)=2 lambda^(-2/3), spacing is order Jz lambda^(10/3), and the full-width convention gives

Gamma=-2 Jz lambda^2 f Im a
     =0.1136079121993789 Jz lambda^4 + o(lambda^4)

for this conditional lossy-endpoint model. If the arm coordinate is n=ell-2>=1, the real order-f endpoint term is f(2+a), not the f(1+a) of the earlier arm starting at ell=2. This offset does not change the leading width. An energy-dependent outgoing continuation is needed for an actual model resonance; freezing the boundary resolvent supplies its leading asymptotic coefficient.

## Why this is not yet a native width

The fast K1 block is gapless at the slow energy scale. One cannot justify removing it with a gapped Schrieffer-Wolff denominator, and Pslow K2 Pslow being an exact coefficient projection does not establish autonomous slow dynamics. Its couplings to the full slow boundary wavefunction need to be retained or controlled. The derivative identity previously derived for the single axial endpoint vector does not automatically hold for all host components.

Higher native coefficients can alter real dispersion or introduce radiation before the desired order of precision; nominally higher coefficients may exceed the Airy spacing or width. Their constant parts cannot simply be presumed removable without checking their state dependence. The supplied tension and a uniform expansion for interval size lambda^(-2/3) must also be established. Hence the computed 0.1136079122 is a checked coefficient of the projected host-plus-arm model, not a native resonance, pole, or lifetime claim.
