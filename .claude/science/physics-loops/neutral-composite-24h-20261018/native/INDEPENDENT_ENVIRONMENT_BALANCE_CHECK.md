# Native environment-cost balance: independent check

PASS. The stronger edge-marginal argument closes the lower bound at order Jlambda^(5/2), under the inherited uniform local reduction and actual odd two-wall spectral-cluster hypotheses. It is not circular and does not require a preassigned environment profile, clustering, or a neutral internal gap.

## Cut-energy and conditional estimates

For an m by m square of column sites (m>=3, no wrap), the internal counts are (m-1)^2 plaquettes and 2m(m-1) edges. Every internal edge has an internal plaquette meeting exactly one endpoint, including edges on the patch boundary. The logical-X-polarized trial gives e_S<=-10m(m-1). There are 4m crossing edges and 4m plaquettes intersecting but not contained in the patch, so ||B||<=36m.

For every background density matrix, the outside term is at least e_out. Combining this with e<=e_S+e_out+||B|| gives

    <K>-e >= <K_S>-e_S-72m.

This remains valid after conditioning on particle position and translating the cut to that position: the global ground energy and cut constants are translation invariant. No background factorization is used in the lower bound; only the trial used to bound e factorizes.

For an anticommuting involution pair E,P and b=< (I-P)/2 >, |<E>|<=2sqrt(b(1-b))<=2sqrt(b). Apply this to each conditional normalized background state, then Jensen over particle position. The displaced-flux bound S_d<=(16+2|d|_1^2)delta gives the uniform internal-edge bound

    average_i |<E_e>_i| <=2sqrt((16+8m^2)delta).

Dropping plaquette expectations to their lower energy bound -4 per plaquette is valid regardless of their fluctuations. The resulting bound is exactly

    <K>-e >=6m^2-74m-4
             -20m(m-1)sqrt((16+8m^2)delta).

There is no hidden area factor in the individual edge bound beyond the explicit edge count, and the conditional expectations are compatible with the background-valued singleton amplitudes.

## Choice of scale and constants

For m>=3, sqrt(16+8m^2)<=sqrt(10)m. With a=1/(20sqrt(10)) and m=min(floor(a/sqrt(delta)),floor(R/4)), one has m sqrt(delta)<=a. The negative square-root term is at most m(m-1). The weaker stated result 5m^2-74m-4 is therefore valid; it is at least 2m^2 for m>=32.

The prior upper estimate delta=O(lambda^(3/2)) and R comparable to lambda^-1 ensure m tends to infinity. For the unsaturated choice, floor(a/sqrt(delta))>=a/(2sqrt(delta)) eventually, so

    <K>-e >=2m^2 >=a^2/(2delta)=1/(8000delta).

For the saturated choice, m=floor(R/4)>=R/8 for sufficiently large R, giving <K>-e>=R^2/32. The delta=0 case is naturally included in this saturated branch and is excluded by the same argument below.

## Actual energy transfer and absence of circularity

Use normalized singleton states obtained from actual odd two-wall cluster states. Odd parity excludes the half-column block exactly. The inherited reduction gives

    D/J >=lambda(1-lambda)delta
           +lambda^4(<K>-e)/128-C lambda^3,

where D=Eheavy-Eg-4J+4Jlambda. The shared vacuum scalar cancels. The global order-five remainder is O(Jlambda^5 R^2)=O(Jlambda^3); the uniform defect remainder and actual-cluster projection error have the same or smaller order. No growing-m local-observable approximation is introduced by this energy comparison. The true vacuum energy differs from the normal-form vacuum minimum by at most that global remainder.

The prior variational upper D<=C Jlambda^(5/2) is independent of the new lower estimate. Positivity of the background excess and the kinetic form first give delta=O(lambda^(3/2)), allowing the scale choice above. If saturated, the environmental lower cost is at least cJlambda^4 R^2=c'Jlambda^2, contradicting that upper estimate for sufficiently small lambda. Thus the unsaturated inequality applies:

    D/J >=lambda(1-lambda)delta
             +lambda^4/(1024000delta)-C lambda^3.

AM–GM gives

    D/J >=2sqrt(1-lambda)lambda^(5/2)/sqrt(1024000)
             -C lambda^3.

The lambda^3 error is smaller than lambda^(5/2), so the positive lower coefficient survives. This proves the stated two-sided Theta(Jlambda^(5/2)) correction for the actual odd-heavy minimum. The argument also applies to actual odd cluster states within O(Jlambda^(5/2)) of that minimum, with constants depending on the allowed excess.

Bounding each positive term by the established upper yields both delta<=C lambda^(3/2) and delta>=c lambda^(3/2). The environmental excess has upper O(Jlambda^(5/2)) from the kinetic lower bound and lower Omega(Jlambda^(5/2)) from the cut estimate and delta upper bound. Thus it too is Theta(Jlambda^(5/2)).

## Scope

This result identifies a kinetic/transport length delta^(-1/2)=Theta(lambda^(-3/4)); it does not identify it with a sharp flat-domain radius, a center-of-mass localization length, or an actual minimizer shape. The earlier joint-flat probability guarantee remains q<3/8. The separate upper bound on any almost-surely flat patch is consistent with q<=3/4 and does not supply a matching profile theorem.

All statements concern the specified finite-height family R comparable to lambda^-1, the fixed canonical dressed coordinates, actual isolated odd two-wall states, and asymptotic constants from the finite-order local construction. They do not imply an undressed measurement statement, a fixed-lambda thermodynamic pole, an emission rate, a universal coupling, or an empirically determined scale. No material correction is required in the proposed derivation.
