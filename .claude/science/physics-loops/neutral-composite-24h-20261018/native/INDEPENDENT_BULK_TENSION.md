# Focused infinite-column string-tension check

Disposition: PASS for the local fourth-order bulk energy-density difference in the supplied strong-Jz model. This does not establish closure of the two-column string channel or an exact native pole.

Assume infinite longitudinal columns, ferromagnetic Jz>0, native transverse -Jperp XX and -Jperp YY on a simple square array, and the all-aligned reference. Reverse two whole column segments over the same finite interval of ell longitudinal sites. The four longitudinal domain walls cost8Jz before transverse perturbation. The argument below concerns long intervals with distinct endpoint neighborhoods; it does not introduce open-column ends.

## Excited-band locality

Take P to include the complete unperturbed energy-8Jz manifold, rather than assuming only the chosen string configurations. A virtual operation supported a bounded distance away from both endpoints sees a locally aligned longitudinal background. Its intermediate energy increase relative to the excited reference is exactly the same local wall-creation cost as in the vacuum: each isolated flipped spin costs4Jz. The preexisting four faraway walls cancel from E_reference-E_intermediate. Thus the local connected bulk loops have the same denominators as the vacuum calculation, with the original transverse sign factors evaluated on the reversed interior columns.

At second order, an interior return repeats one physical transverse bond. Its signed product and denominator are independent of the local aligned spin signs, so it is a scalar energy density common to string and vacuum. The first-order bulk return is absent. A three-step return is impossible on the infinite nearest-neighbor square graph, and no finite local sequence can reverse an entire infinite column. Consequently no lower-order diagonal term contributes a length-dependent string energy difference. Endpoint motion can occur already at first order, but it is not an interior energy density.

At fourth order, nonconstant connected interior returns are the previously checked same-slice elementary plaquettes. Repeated-edge terms are spin-independent. Disconnected remote loops cancel in the canonical linked energy difference, including folded terms; they must not be added as powers of an extensive second-order shift. Using the full degenerate manifold can add endpoint mixing/kinetic terms, but it does not change the strictly interior four-edge coefficient. Equivalently, inside each local motif the excited-band denominator equals the vacuum denominator exactly. This establishes the coefficient of the extensive diagonal term, not an eigenvalue of an isolated string state.

At fixed perturbative order, linked motifs touching an endpoint occupy only a bounded number of sites. They therefore contribute endpoint corrections independent of ell once the two endpoint neighborhoods are disjoint. This is a finite-order statement, not a nonperturbative uniform bound on a resonant excited-state self-energy.

## Coefficient and sign

The bulk effective plaquette energy is -k4 P with k4=Jperp^4/(128Jz^3). Each reversed plaquette changes its energy by+2k4. Two adjacent reversed columns share two plaquettes: the changed count is4+4-2*2=4 per interior slice. Therefore

    Delta E_bulk(ell)=8k4*ell=Jperp^4*ell/(16Jz^3).

The positive sign is confining in this diagonal effective potential. Two columns sharing no plaquette change8 plaquettes, giving16k4*ell=Jperp^4*ell/(8Jz^3). The phrase well-separated must mean no shared plaquette: diagonally neighboring columns share one and instead give12k4*ell=3Jperp^4*ell/(32Jz^3).

I independently recomputed the signed24-path Fraction plaquette sum and summed its energy change for all relevant transverse plaquettes of these three geometries. It gives respectively1/16,1/8,3/32 in units Jperp^4/Jz^3. The YY instantaneous-spin phases are retained; they do not cancel the tension. Results are saved in neutral-bulk-string-tension-independent.json. In anisotropic transverse couplings, replace Jperp^4 by Jx²Jy² at this order.

## Limits on the proposed scale inference

The local argument permits the stated linear potential coefficient in an effective string-coordinate analysis. It does not show that all other four-wall configurations decouple, that a separated-column configuration remains stationary transversely, or that endpoint conversion cannot mix channels. Higher-order bulk terms can renormalize the tension, and finite-order linked locality does not provide a uniform bound in ell or lambda.

Conditionally, a nonzero quadratic kinetic curvature of order Jz*lambda and slope of order Jz*lambda^4 give the usual balance length (lambda/lambda^4)^(1/3) proportional to lambda^-1 and energy spacing of order Jz*lambda^3. This scaling requires the asserted kinetic channel and its band-edge approximation; it can fail at momenta where curvature/hopping vanishes or when channel coupling changes the effective problem. No Airy spectrum, native bound/resonance pole, physical scalar, or observed large-feature scale is certified by this tension check alone.

No repository edits or formal audit were performed.

## SHA-256 identity

- `/private/tmp/neutral-bulk-string-tension-independent.json`: `8f11d719654ccc62517ec45de55ad5d30a60e1124e4c34009d062cd4579e0018`
