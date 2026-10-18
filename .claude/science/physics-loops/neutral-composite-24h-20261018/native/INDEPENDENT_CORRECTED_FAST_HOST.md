# Corrected fast-host Green functions near the moving van Hove energy

Scope: the specified coefficient-model dispersion and its rank-one contact, at total momentum zero. This is not a full-native resonance result. The named `/private/tmp/neutral_outgoing_host.py` was absent when checked; the analytic result below does not depend on that script.

Write s=cos x+cos y, d=cos x-cos y, d2=cos(2x)-cos(2y)=2ds, and

epsilon_lambda=-4s-lambda*d^2.

All averages below are normalized torus averages. Let G=<d^2/(z-epsilon_lambda)>, G4=<d^4/(z-epsilon_lambda)>, G6=<d^6/(z-epsilon_lambda)>, continued from the retarded upper-half-plane function onto the outgoing branch near the target. Both d and d2 have norm one. The hard origin is irrelevant within their square-odd, reflection-even symmetry sector, which remains invariant under this dispersion.

## Moving saddle and uniform logarithm

For |lambda|<lambda0<1, the only critical momenta are the usual four square-lattice critical points. At (0,pi), with local coordinates u,v,

epsilon_lambda=-4lambda+2(1+lambda)u^2-2(1-lambda)v^2+O((u^2+v^2)^2).

The second saddle is related by axis interchange. Both have d^2=4. An analytic Morse change of coordinates, uniform for this compact lambda range, reduces each saddle to a difference of squares. In the normalized two-dimensional integral, the two saddles together give weighted density

rho_d(-4lambda+w) = [1/(pi^2 sqrt(1-lambda^2))] log(1/|w|)+O(1).

One way to track the coefficient is that each saddle contributes weight 4 divided by (2pi)^2 times the inverse square root of the quadratic coefficients, 1/[2 sqrt(1-lambda^2)], to the coefficient of log(1/|w|). Summing the two gives the expression above. The retarded imaginary part is -pi*rho_d.

Locally on the outgoing branch a compatible singular term is

G(z) = -i/[pi sqrt(1-lambda^2)] log[Lambda/(-i w)] + O(1),
w=z+4lambda,

where changing the positive cutoff Lambda changes only the bounded remainder. The logarithm is continued from Im w>0; near negative real w its outgoing continuation is analytic across that real segment. This expression is not the ordinary lower-half-plane physical-sheet integral.

For z=-6lambda+O(lambda^(7/3))-i O(lambda^3), on disks/strips with fixed constants and lambda>0, w=-2lambda+o(lambda) stays uniformly away from the saddle by a constant times lambda. Therefore

G(z)=-i/[pi sqrt(1-lambda^2)] log(1/lambda)+O(1)

uniformly, including imaginary parts much smaller than the saddle detuning. The leading imaginary sign is negative. The O(1) bound follows from the local analytic saddle expansion plus the nonsingular remainder of the energy surface, not from an absolute-value bound on the original real-momentum integral.

The weights d^4-4d^2 and d^6-16d^2 vanish quadratically at both saddles. Their local saddle integrals have no leading divergent logarithm and remain bounded on the same continued domains. Hence G4=4G+O(1), G6=16G+O(1), uniformly. This supplies the moments needed below; no numerical fit is involved.

## Mixed moments: the first one does not vanish

Using 4s=(z-epsilon_lambda)-z-lambda*d^2 and <d^2>=1 gives the exact identity

G12=<d*d2/(z-epsilon_lambda)>
   =1/2-(z/2)G-(lambda/2)G4
   =1/2-(w/2)G+O(lambda).

Thus G12=1/2+O(lambda log(1/lambda)). It is bounded but tends to 1/2, not zero. Its imaginary part tends to zero; confusing that with the full mixed Green function would miss the finite real term.

Since <d^4>=9/4 and <d^2 s>=0, a second exact identity is

G22=<d2^2/(z-epsilon_lambda)>
   =-z/4-9lambda/16
     +(z^2 G+2zlambda G4+lambda^2 G6)/4.

At the stated target this yields

G22=15lambda/16+O(lambda^2 log(1/lambda)).

In particular G22 does vanish, at order lambda. The target displacement O(lambda^(7/3)) is smaller than the displayed error. These identities also make explicit which finite real terms accompany the suppressed on-shell density.

## Rank-one contact

For the added coefficient-model contact +lambda |d><d|, Woodbury resummation gives

Gdd_contact=G/(1-lambda G),
G12_contact=G12/(1-lambda G),
G22_contact=G22+lambda G12^2/(1-lambda G).

Here lambda G=O(lambda log(1/lambda)) tends uniformly to zero, so the denominator has no zero in the prescribed domain for sufficiently small lambda. Consequently

Gdd_contact=-i/[pi sqrt(1-lambda^2)] log(1/lambda)+O(1),
G12_contact=1/2+O(lambda log(1/lambda)),
G22_contact=19lambda/16+O(lambda^2 log(1/lambda)).

The contact changes the leading real coefficient of G22 by +lambda/4. It does not change the leading divergent logarithm or the limiting mixed constant. All bounds are analytic on the local outgoing domains, allowing Cauchy derivative estimates on smaller disks if needed for the coupled Schur complement.

## Limitations

These statements require the stated moving target, positive small lambda, the chosen outgoing branch, and the exact dispersion/contact being analyzed. They do not hold uniformly across the shifted saddle itself, at other band edges, or as arbitrary pointwise real-axis claims for the confined full model. They establish the needed host moments; arm corrections, full dressed vertices, source normalization, omitted higher coefficients, and native control remain distinct steps.
