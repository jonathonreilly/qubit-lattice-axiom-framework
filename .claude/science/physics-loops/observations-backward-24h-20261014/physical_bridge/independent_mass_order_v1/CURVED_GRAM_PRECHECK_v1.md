# Independent curved-weight / massless-propagation Gram precheck v1

Frozen after the independent 63-control curved-count construction run and before reading CURVED_COUNT_COMPOSITION_v1.md or curved_count_controls_v1.py. No curved author implementation is exposed. This supplements, and does not alter, CURVED_COUNT_PRECHECK_v1.md.

The newly requested check is the exact energy dual norm of the curved-derived weights propagated using a free massless comparison field chi on Minkowski coordinates. It does not identify this operator with the actual curved Klein-Gordon evolution. The separate curvature reviewer owns that comparison.

Keep L=3/5, t_i=7/5+i, gamma=(-1,3,-3,1), d(t)=1-Ht. For z=n.e1 and common null time s=t-n.x, the clock-minus-directional-force-derivative density is a sum of 12 steps. Its coefficients and knots are independently derived as

  emission: A_ei(s,z)=gamma_i[d(t_i-2L)+z d(s)], K_ei=t_i-2L;
  reception: A_ri(s,z)=gamma_i[-d(t_i)+z d(s)], K_ri=t_i;
  bounce: A_bi(s,z)=-2z gamma_i d(s+zL), K_bi=t_i-L-zL.

Thus H_z(s)=sum_j A_j(s,z)1_{s<K_j(z)}. The bounce d(s+zL) factor comes from evaluating the body force derivative at body coordinate time t=s+zL. Replacing it by d(s) discards an H z L term. Every knot is positive on -1<=z<=1. The coefficient sum vanishes identically, so integration from s=0 through the maximum knot equals the whole real-line integral.

For norm N=int(p^2+|grad chi|^2), the real-field Gram is

  pi G(H)=(1/4)int_{-1}^1 dz int_R ds H_z(s)^2.

Because each A is linear in H and the ordering knots do not depend on H, G is exactly quadratic in H. Its constant coefficient must be 329/(54 pi), already independently checked. For the actual curved interpretation restrict 0<=H<1/t_max=5/22. No numerical value of H is inferred.

Independent protocol: integrate the pairwise polynomial products A_j A_l from 0 to min(K_j,K_l). Split z only at exact rational knot crossings. Integrate each resulting polynomial in z using exact rational arithmetic and retain every coefficient of pi G(H). As a separate representation, sort the 12 knots at Gauss direction nodes and integrate the squared summed affine-in-s density over each adjacent interval; two temporal Gauss nodes are exact for that quadratic, and nine direction nodes per ordering cell exceed the polynomial degree required. Check the symbolic polynomial at H=0,1/25,1/10 against those sorted-interval controls, and check positivity/Cauchy consistency of the resulting 2x2 Gram in (1,H). No author scientific suite reruns.
