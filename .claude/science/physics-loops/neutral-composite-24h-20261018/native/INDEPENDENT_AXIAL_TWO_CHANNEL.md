# Focused check: axial distance-two interval channel

Checked the two supplied path-enumeration scripts and completed boundary JSON. The following derives their long-interval entries and the projected fast-channel vertex. It does not prove a closed slow channel or a native resonance.

## All ell>=3: diagonal and endpoint motion

For any non-neighboring column pair with the same interval, four distinct endpoint-adjacent layers each have eight incident transverse edges of cost four rather than the vacuum cost eight. Each contributes -1/8 after subtraction, giving diagonal -4. Everywhere else the diagonal contribution equals vacuum. This uses a uniform aligned reference.

As in the preceding E8 classification, a two-bond path changes at most four spins. For ell>=3 a different final column pair is impossible. Non-neighboring columns also cannot change two layers with only two bonds. The only possible off-diagonal final interval changes a single layer at one endpoint. This requires the columns to be joined by a transverse path of length two.

Each of the two orderings along that path has intermediate cost four. For an axial X-X path the matrix-element product is +1, giving -1/2 in total. For an axial Y-Y path the middle spin changes sign between the two actions: the product is -1, giving +1/2. This holds for both extension and contraction. For a mixed X-Y path, the two reverse orderings have opposite products and the same denominator; they cancel exactly for each intermediate column. Thus diagonal separation (1,1) has no such hop, whereas (2,0) and (0,2) have opposite signed hops. Separations with Manhattan distance greater than two have no off-diagonal entry at this order.

In the physical-square scalar basis

A_ell=(|axial X separation 2,ell>+(-1)^ell |axial Y separation 2,ell>)/sqrt(2),

the sign alternation converts both orientations to the same hopping. At total longitudinal momentum zero the two endpoints add, giving A_ell -> A_(ell+/-1) coefficient -1. The bulk slow-arm symbol is -4-2 cos p, bottom -6, in units Jperp^2/Jz. If independently established tension is Jz lambda^4 ell/8, balancing this arm's kinetic term with that tension gives size 2 lambda^(-2/3). That balance alone does not establish a resonance or its boundary condition.

## Why ell=2 is different

At length two, two operations can move one whole occupied column to its transverse neighbor, one operation on each layer. The two orderings each have cost four and product +1, for both X-X and Y-Y, hence every such physical column hop has coefficient -1/2. At total transverse momentum zero this is relative hopping -1 between noncoincident separations. Attempts to merge the columns leave the E8 sector and are excluded.

The completed JSON explicitly contains these additional outputs from axial separation two: axial separation three and mixed separations (2,+/-1), besides nearest separation one. They are legitimate ell=2 states. Therefore the axial arm is not closed. The same ell=2 transverse motion exists for diagonal pairs and lets additional frozen channels reach the nearest-pair fast arm.

## Exact projected fast-channel vertex

Let d=(|ex>+|-ex>-|ey>-|-ey>)/2 and d2=(|2ex>+|-2ex>-|2ey>-|-2ey>)/2 in the ell=1 relative-coordinate host. Let E2 be the normalized nearest-pair ell=2 scalar state. Let P_fast project to the first-order source-connected host plus nearest-pair string component.

Contraction from A2 to ell=1 contributes -d2: two endpoint contractions have -1/2 for X and +1/2 for Y. The ell=2 transverse column hops contribute -E2. Consequently

P_fast K2 A2 = -d2-E2 = (K1 d)/2.

The second equality follows directly from relative host hopping -2: K1 d=-2d2-2E2, with mixed-diagonal and origin contributions cancelling. Normalization agrees with the even relative-coordinate embedding; there is no extra sqrt(2).

This is a projected identity. K2 A2 has further components orthogonal to P_fast. In particular it is incorrect to replace the full boundary action by (K1 d)/2 without retaining those components.

## What radiation suppression follows, conditionally

For the isolated fast K1 block, its spectral theorem gives the vertex spectral measure

< K1 d/2 | delta(E-K1) | K1 d/2 > = E^2 <d|delta(E-K1)|d>/4.

Thus the imaginary fast-channel self-energy from this vertex is suppressed by E^2 relative to the full fast-block d spectral measure. The relevant Green function is that of the complete fast block, not simply the bare two-dimensional host. With <d|K1|d>=0, the resolvent identity is

< K1 d/2 | (z-K1)^-1 | K1 d/2 > = [z^2 G_fast,d(z)-z]/4.

This includes a real analytic term; vanishing dissipative density at zero does not imply the entire self-energy vanishes at nearby energies. Singular densities, higher-order changes in the fast operator/vertex, and mixing with the other ell=2 slow channels must be handled before asserting any power law for native radiation. A slow eigenvector generally need not remain the single A2 boundary vector, so its total fast vertex need not retain this derivative form.

## Support and scope

The longitudinal margin of three contains the endpoint processes and their nearest longitudinal neighbors. The listed transverse boxes contain all two-step neighborhoods of the evaluated pairs; remote repeated-edge shifts cancel with the vacuum term. The independent argument establishes all ell>=3 rows for the specified separations, not all remaining boundary rows or all transverse asymptotic sectors. Plane parity and the uniform reference remain assumptions of the excitation construction; no equilibrium state selection or scalar-field identification follows.

## Updated slow-host interpretation

Root's correction is essential: after removing the first-order fast component, the ell=2 slow sector still contains all relative separations except the origin and nearest neighbors. Its second-order relative hopping -1 and diagonal -4 have essential continuum [-8,0]; removal of finitely many relative sites does not remove that continuum. The axial-arm bottom -6 lies inside it. Therefore the projected fast-channel derivative identity cannot determine the total width, and supplies no lambda^7 total-width claim.

If the completed slow model supplies a regular complex endpoint scattering length at this energy, its natural kinetic unit is Jz lambda^2 and dimensionless tension is f_s=lambda^2/8. Its Airy length is f_s^(-1/3)=2 lambda^(-2/3), spacing is order Jz lambda^(10/3), and a finite imaginary scattering length would produce full width of order Jz lambda^4. This is conditional scaling, not a checked coefficient or proof of the complete native slow model. The other slow channels, projected boundary, and original readout remain to be derived.
