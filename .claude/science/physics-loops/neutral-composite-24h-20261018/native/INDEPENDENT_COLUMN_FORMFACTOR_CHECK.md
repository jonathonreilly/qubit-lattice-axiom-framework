# Whole-column original-readout form factor: independent check

Disposition: PASS with the midpoint Fourier convention stated explicitly. Inspected and replayed /tmp/neutral_square_local_source.py; all 16 reference patterns and four separately marked vertices pass exactly with rational arithmetic. No shared/canonical edits.

Define C_Q with its phase at the longitudinal bond midpoint: V^-1/2 sum_r exp[-iQ.(r+ez)] Z_r Z_(r+2ez). A flipped spin at vertex r changes the two diagnostic bonds whose midpoints are r-ez and r+ez. Its source difference is therefore

 -2[exp(-iQ.(r-ez))+exp(-iQ.(r+ez))]/sqrt(V)
 =-4cos(Qz)exp(-iQ.r)/sqrt(V).

This matches root's formula. If instead r in the source definition denotes the lower endpoint, a global exp(+iQz) phase is needed; the two conventions should not be mixed.

The marked-path script differentiates each intermediate denominator using that vertex's indicator divided by the intermediate flip count. It includes all 24 square-edge permutations, actual XX/YY signs for each reference pattern, and the three denominators. Each vertex contributes -3P/512 at unit normalization. Summing four vertices recovers the previously checked uniform coefficient -3P/128. Thus the orientation-dependent Fourier coefficient is

 -3lambda^4 cos(Qz)/(512sqrt(V))
   sum_(p,z) P_p sum_(vertices r of p) exp(-iQ.r).

For a unit transverse square centered at c_p,

 sum_vertices exp(-iQ.r)=4exp(-iQ.c_p)cos(Qx/2)cos(Qy/2).

Hence the stated centered-plaquette form follows with coefficient -3lambda^4/(128sqrt(V)). The factors cos(Qz), cos(Qx/2), cos(Qy/2) have distinct geometric origins and no extra factor two is missing.

A separated nonwrapping whole-column rectangle changes P from +1 to -1 at four transverse plaquette centers on every longitudinal slice. Therefore the order-four contrast is

 3lambda^4/(64sqrt(V)) cos(Qz)cos(Qx/2)cos(Qy/2)
  [sum_z exp(-iQz z)] [sum_(four corners c) exp(-iQ_perp.c)].

For allowed periodic momenta, the z sum is L if Qz=0 modulo 2pi and zero otherwise. At Qz=0 this is exactly the expression supplied by root. At Q=0 the four-corner sum is 4, reducing to 3Llambda^4/(16sqrt(V)), as required by the uniform-source calculation.

Here “corners” means the centers of the four BAD PLAQUETTES bordering the flipped rectangle, not the coordinates of the outermost flipped sites. Fixing that convention avoids a spurious half-lattice phase. Allowed Fourier momenta and consistent midpoint representatives also handle periodic seams.

The fixed-order higher-source terms obey the same local diagonal corner-support argument, giving an ABSOLUTE error O_n(lambda^5 L/sqrt(V)), uniformly in allowed real Q because all Fourier weights have modulus one. There is no relative approximation at zeros of the cosine factors or the four-corner interference sum. For Qz!=0, the diagonal expectation in a longitudinally invariant whole-column trial vanishes exactly, not merely at leading order, provided the dressing is translation-equivariant. This is consistent with the earlier exact longitudinal low-energy selection rule.

This is the static spatial form factor of the original diagnostic on the dressed rectangle relative to the ground reference (with the previously quantified actual-ground replacement error when applicable). It is not a transition matrix element, dynamic production amplitude, or universal coupling.
