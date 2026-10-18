# Independent longitudinal center-of-mass dispersion check

Read the actual ell=4, rx=2, ry=0 row of `native/neutral_bulk_second_other.json`. Its vacuum-subtracted diagonal is -4. The only off-diagonal targets are common intervals [-1,3], [1,3], [0,2], and [0,4], each with coefficient -1/2. Thus these are four distinct moves of one endpoint; they are not a previously assumed center-of-mass kinetic term.

The local coefficient also follows directly: growth or shrinkage of an endpoint at axial column separation two uses the two transverse bonds along the intervening column. Both possible orders give an intermediate configuration costing 4Jz above the initial E8 configuration. The two XX products have positive product, hence each resolvent contribution is -1/4 in units Jz lambda^2 and the sum is -1/2. Shrinkage has the same local energy cost. YY along the other transverse direction gives the corresponding gauge-related sign; the previously specified (-1)^ell orientation gauge converts its length-link hopping to the same negative convention. This reasoning applies to separated endpoints; short-interval boundary rows require their own calculation.

## Fourier reduction

Label a common interval by integer endpoints l,r and ell=r-l+1, with center c=(l+r)/2. In a normalized longitudinal translation fiber use |p,ell> proportional to sum_l exp[i p(l+(ell-1)/2)] |l,l+ell-1>. At fixed ell this is an ordinary normalized translation orbit, with no additional two-endpoint normalization factor.

Growth at the left shifts c by -1/2, and growth at the right shifts c by +1/2. Their two amplitudes therefore add to

-(1/2)(exp(ip/2)+exp(-ip/2))=-cos(p/2).

The same sum holds for shrinkage. Choice of Fourier sign conjugates the separate phases but leaves this real result unchanged. The bulk length-chain symbol is consequently

E(p,k)/Jz = 8 + lambda^2[-4-2 cos(p/2) cos k]

at this order, before the string tension. In particular, for p near zero the bottom is 8-6lambda^2+(lambda^2/4)p^2+O(lambda^2 p^4). This is a genuine derived longitudinal momentum dependence of the coefficient model. The half-integer center gauge means p shifted by 2pi can also shift the relative-length gauge; the local near-zero dispersion is unaffected.

## Conditional confined-arm scaling

Let c_p=cos(p/2)>0 bounded away from zero and retain the previously derived physical tension Jz lambda^4 ell/8. In slow energy units Jz lambda^2 the slope is f=lambda^2/8 and the continuum kinetic coefficient near the length-band minimum is c_p. The Airy spacing is alpha_1 c_p^(1/3) f^(2/3). Therefore the proposed candidate real energy is

E_real/Jz = 8-(4+2c_p)lambda^2 + (alpha_1/4)c_p^(1/3)lambda^(10/3) + O(lambda^4).

The factor 1/4 is exactly (1/8)^(2/3). Boundary offsets and scattering lengths enter at order lambda^4 under the regular outgoing boundary assumptions used in the earlier model. This is conditional on the momentum-dependent bath/self-energy satisfying those assumptions; the endpoint calculation alone does not prove a pole or its width. It is nonuniform near p=pi, where c_p vanishes and a different scaling is necessary. The leading bare energy is 8Jz, not a dimensionless 8 added to dimensional corrections.

## Transverse scope

A fixed-order term with n transverse flips cannot change the unordered column pair of an interval with ell>n: the physical spin symmetric difference requires at least 2ell flips. Thus a long-arm bulk coefficient has no transverse center-of-mass hopping at that fixed order. Finite-length endpoint/bath channels can still generate transverse momentum dependence in boundary self-energies. Absence of bulk transverse hopping at this order does not prove exact transverse immobility, nor an isotropic relativistic dispersion. The calculation identifies a longitudinal route for the specified composite arm while leaving complete momentum-dependent resonance control to the next block.

## Addendum: slow host, contact vertex, and fast bulk geometry

Checked `/private/tmp/neutral_com_pole_root.md`, the source of `neutral_bulk_second_other.py`, and `neutral_bulk_second_boundary.json`. The latter includes ell=2 axial-x, axial-y and diagonal separations, plus ell=3 axial-y. Its explicit ell=3 axial-y contractions to [1,2] and [0,1] each have raw coefficient +1/2, while the ell=4 axial-x contractions in the first JSON each have -1/2. The established orientation gauge (-1)^ell for the y arm changes the former to -1/2 and leaves its ell=2 host endpoint positive. Thus the same normalized scalar combination joins the two orientations at ell=2.

1. **Slow ell=2 host.** Every listed single-column transverse hop keeps its interval [0,1] unchanged and has coefficient -1/2. Combining the two possible column moves at zero transverse center momentum gives relative-lattice hopping -1. Since the longitudinal center does not change, there is no p-dependent phase. The excluded origin and nearest-shell sites likewise represent the same geometry at all longitudinal p. This confirms the leading punctured slow-host bulk operator is unchanged. Fast-sector contacts are separate; removing nearest-shell sites is a projection, not an assertion those physical channels do not exist.

2. **Slow arm to host.** For ell=3 the contractions [0,2] to [1,2] and [0,1] shift the center from 1 to 3/2 and 1/2. Their Fourier phases again sum to 2gamma, gamma=cos(p/2), giving -gamma between each normalized orientation arm and its host endpoint. In the normalized scalar combination A=(|2ex>+|-2ex>+|2ey>+|-2ey>)/2, the arm-to-host vector is exactly -gamma A in the stated gauge. Orthogonal orientation normalization adds no factor of two. The associated leading scalar self-energy is consequently gamma^2 G_AA^hole(E). This check concerns the leading K2 contact, not all higher short-interval corrections.

3. **Fast long arm.** A first-order XX operation at either endpoint of an adjacent-column interval has amplitude -1, so the two center phases give -2gamma per length link. YY is brought into the same sign by its existing orientation gauge. Hence the leading fast-arm operator is -2gamma T if T has unit off-diagonal entries.

4. **Fast far-separated ell=1 host.** Its first-order transverse single-spin hops keep the common z layer fixed. The two-step independent-magnon processes producing the bulk symbol -(cos kx-cos ky)^2 likewise keep that layer fixed. A simultaneous change of the two distant spins' z layer would require two transverse edges directly joining the distant sites, which do not exist. Consequently the bulk symbol remains -4(cos kx+cos ky)-lambda(cos kx-cos ky)^2, independent of longitudinal p. Near-neighbor contact processes can change the layer, as is visible in the ell=1 adjacent rows of the actual JSON; these must remain p-dependent finite contacts. This distinction is essential.

Thus the stated leading coefficient geometry is sound. It supports carrying the existing analysis into a small p neighborhood, but does not itself prove uniform outgoing Green-function continuation, residue control, or persistence of the complete pole. Those analytic claims remain the separate domain check.
