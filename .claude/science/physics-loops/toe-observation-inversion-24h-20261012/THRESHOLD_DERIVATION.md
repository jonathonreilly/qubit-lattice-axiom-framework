# Provisional exact pair-threshold derivation

Author calculation, 2026-10-12. Independent check pending. Supplied models in GOAL.md; no empirical conclusion yet.

Set G(k)=4 sum_i sin^2(k_i/2)>0, c_i=cos k_i, b_i=sin k_i. Restrict |k_i|<pi/2, k!=0, mu>0. The electron symbol is e(p)=sqrt(mu^2+sum_i sin^2 p_i). Momentum addition is modulo 2pi. All pair momenta are included, not just central-cone or collinear pairs.

Put p=k/2+q, the other momentum k/2-q. Define S=G/4, T=sum c_i sin^2 q_i, C=sum b_i sin q_i cos q_i, X=mu^2+S+T. Then

 (e(p)+e(k-p))^2=2X+2 sqrt(X^2-C^2).

The pair lies below the photon energy sqrt(G) precisely when X<2S and C^2>4S(mu^2+T). Hence any below-photon pair requires mu^2<R(q)=C^2/G-T.

Use C^2/G=max_t (2t C-G t^2). Taking the maximum over all q is legitimate on the compact torus; the t dependence is coercive after maximization. Each component has

 max_q [2t b sin q cos q-c sin^2 q] = (sqrt(c^2+4t^2 b^2)-c)/2.

Writing u=4t^2>=0, the full maximum is

 R_max(k)=max_(u>=0) F_k(u),
 F_k(u)=1/2 sum_i [sqrt(c_i^2+u b_i^2)-c_i]-G u/4.

F is strictly concave for k!=0 and c_i>0. Four times its derivative at0 is sum (1-c_i)^2/c_i>0; at1 it is -sum (1-c_i)^2<0. Therefore there is a unique u_* in(0,1) satisfying

 sum_i b_i^2/sqrt(c_i^2+u_* b_i^2)=G.

A maximizing pair is

 q_i=1/2 arctan(sqrt(u_*) tan k_i) modulo pi,
 p_i=k_i/2+q_i,

or its exchange. At this optimizer C=G sqrt(u_*)/2, so for mu^2=R_max, mu^2+T=C^2/G=G u_*/4=S u_*<S. Thus the extra squaring condition X<2S is satisfied at equality and remains so if mu decreases. This proves the exact kinematic criterion:

 min_p [e(p)+e(k-p)] < sqrt(G) iff mu^2<R_max(k).

Equality gives the threshold; larger mu forbids this channel for all torus momenta. All pi-shifted electron corners are included by the maximization. At threshold the two shares are generally noncollinear in3D, although their leading small-k directions coincide. This is a kinematic theorem, not a decay-rate theorem.

As k=r n with |n|=1, r->0:

 u_*=1/2+O(r^2),
 R_max=r^4 (sum n_i^4)/64+O(r^6),
 p/k at leading order = (1 +/-1/sqrt2)/2.

The threshold r~sqrt(8mu)/(sum n_i^4)^(1/4). Exact directional correction and uniform bounds remain to be written. Symmetric q=0 always gives pair energy2 sqrt(mu^2+G/4)>sqrt G; it would miss every positive-mu channel.

For one nonzero component k, c=cos k:

 u_*=(1+3c)/(4(1+c)),
 R_max=(1-c)^2/[8(1+c)] = sin^4(k/2)/[4cos^2(k/2)].

Restoring physical photon energy E=Lambda sqrt G and mass m=m_e c^2, the axis equality is

 Lambda^2=E^2/4+E^4/(64m^2).

Thus a cutoff bound from survival needs a finite rate and detector bridge first; the expression is not yet a95% confidence limit.

Common-Laplacian comparator: e_L(p)=sqrt(mu^2+G(p)). Since2|sin((p_i+q_i)/2)| <=2|sin(p_i/2)|+2|sin(q_i/2)| componentwise, norm subadditivity gives sqrt G(p+q)<=sqrt G(p)+sqrt G(q). For mu>0 each e_L exceeds its massless norm, hence the photon cannot decay into this pair anywhere on the torus. This elementary comparator proof should be checked for modular momentum and sign conventions. It shares the photon timing law with the sine-Dirac candidate, so timing alone cannot select the electron completion.
