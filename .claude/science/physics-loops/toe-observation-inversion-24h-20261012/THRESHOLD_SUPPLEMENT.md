# Uniform errors and fixed-energy angular extrema

Author supplement, 2026-10-12; focused independent check supports the mathematics. The physical-domain qualifications below incorporate that check. This is conditional mathematics of the frozen symbols, not an empirical exclusion.

The independent check found the alternate exact variational functional

 R(k)=max_(0<=z<=1) [ z S - (1/2)sum_i(1-sqrt(1-z sin^2 k_i)) ],
 S=sum_i sin^2(k_i/2), z=1-u.

It agrees identically with the author functional after u=1-z. For stable evaluation let c_i=cos k_i>0 and r_i=sqrt(1-z sin^2 k_i). Rationalization gives

 R_z=z(1-z) sum_i [(1-c_i)sin^2 k_i / (2(r_i+c_i)(1+r_i))].

Since c_i<=r_i<=1,

 sum_i(1-c_i)^2/16 <= R(k) <= sum_i (1-c_i)^2/(16c_i).

If max|k_i|<=epsilon<pi/2 and Q4=sum_i k_i^4, Taylor inequalities yield the explicit uniform remainder bracket

 Q4/64 (1-epsilon^2/12)^2 <= R(k) <= Q4/(64cos epsilon).

Thus the relative small-momentum error is controlled uniformly in direction, including axes and zero components. No numerical search supplies these quantifiers.

For fixed photon energy S in(0,1/2), set v_i=sin^2(k_i/2), sum v_i=S. The scalar f_z(v)=1-sqrt(1-4zv(1-v)) satisfies

 f_z''(v)=4z(z-1)/(1-4zv(1-v))^(3/2)<=0.

Therefore each R_z is Schur-convex in the three nonnegative v_i. Maximizing over z preserves the ordering: equal v_i minimize R and concentration in one component maximizes it. Both configurations remain inside the supplied |k_i|<pi/2 domain because S<1/2. For d equal nonzero components,

 R_d(S)=S^2/[4(d-S)], d=1,2,3.

Consequently

 S^2/[4(3-S)] <=R(k)<=S^2/[4(1-S)].

With physical photon energy E=2Lambda sqrt S and m=m_e c^2, the equality for d equal components is

 Lambda_d(E)^2=E^2/(4d)+E^4/(64d m^2).

For a photon of energy E, within the common angular domain S<1/2 (equivalently Lambda>E/sqrt2), Lambda>=Lambda_1(E)/sqrt3 is necessary for kinematic stability in at least one orientation, while Lambda>=Lambda_1(E) suffices in all orientations. At the equality Lambda_d this common-domain qualification requires E>4sqrt(2d-1)m. For a single d-equal configuration, its less restrictive individual central-cube condition is E>4m. Equality is the zero-phase-space threshold. Decay-rate, finite-distance and detector requirements remain separate.

Notation clarification: the inferred effective step length ell=hbar c/Lambda is a parameter of this supplied completion. It is not an extra or refitted framework scale_reference_primitive. Identifying ell with the framework reference ruler is another explicitly conditional specialization; the approved ruler itself remains unchanged.
