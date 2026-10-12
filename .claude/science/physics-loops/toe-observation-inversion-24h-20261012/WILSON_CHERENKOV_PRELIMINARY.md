# Wilson Cherenkov subtarget — preliminary analytic work

Frozen author calculation before numerical optimization, 2026-10-12. This is the optional subtarget in TARGET.md, not a new fitted grammar. Fixed w=1, a²=1−mu, mu>0. No claim of global finite-momentum theorem yet.

For a fixed direction n, A=sum n_i^4, the small central free electron square is mu²+r²+C_e r⁴+O(mu r⁴+r⁶), C_e=(3−4A)/12; photon C_gamma=−A/12. At r→0 with mu/r² fixed, assume a collinear outgoing electron carries fraction y in(0,1) and the photon fraction 1−y. The leading energy excess is
  2 gap /[(1−y)r³] = [C_e(1+y+y²)−C_gamma(1−y)²] − (mu²/r⁴)/y.
Thus opening is controlled by the cubic
  F_A(y) = y[(1−A)+(1−2A)y+(1−A)y²]/4.
Soft limit y=1 gives F_A(1)=(3−4A)/4. At A=1, F=−y²/4 and no leading opening; this says nothing by itself about all finite momenta.

The global maximum on[0,1] switches from y=1 to a hard-photon interior y_- at
 A_c=(8−2 sqrt2)/7 = about .738796,
 with the competing interior point y=sqrt2−1. For A>A_c,
 y_- = (1−A)/[(2A−1)+sqrt(A²+2A−2)],
 while for A<A_c the maximizer is y=1. At the switch both maximize. Derivation: factor 4[F(1)−F(y)] = (1−y)[(1−A)y²+(2−3A)y+(3−4A)], then impose its interior double zero. The threshold conjecture is r_th⁴ = mu² / max F_A. For every fixed A<1 the max is positive, even when the electron quartic C_e is negative. Thus a soft-only analysis would miss a hard-emission branch. Near the axis 1−A=B→0, y_-~B/2, maxF~B²/16, r_th~2sqrt(mu/B); this expansion is nonuniform when B is comparable to mu.

Obligations before theorem use: independently check polynomial maximization and switch; verify the rescaled central problem with exact full-torus optimization and mass/direction controls; prove noncollinear/endpoint configurations cannot preempt the leading threshold at fixed A<1; derive the axis exceptional case directly; check prior art for hard/soft Cherenkov thresholds. No nature likelihood, attenuation width or charged-particle survival bound follows from this algebra alone.
