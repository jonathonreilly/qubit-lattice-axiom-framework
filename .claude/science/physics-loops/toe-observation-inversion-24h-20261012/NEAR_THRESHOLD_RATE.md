# Exact fixed-momentum threshold onset: author derivation

Author derivation with focused-check corrections, 2026-10-12. This is the golden-rule coefficient of the explicitly supplied Hamiltonian, not a uniform theorem about its interacting spectrum. Let fixed k be nonzero with every |k_i|<pi/2. Keep canonical photon Hamiltonian H_gamma=(1/2)sum(Pi^2+omega^2 A^2), two unit real transverse polarizations, and a real gauge coupling e with alpha=e^2/(4pi). Strictly positive rate requires e!=0; the formula gives zero at e=0.

Use the threshold definitions c_i=cos k_i, b_i=sin k_i, S=sum sin^2(k_i/2), G=4S, and the unique u in(0,1) satisfying sum b_i^2/sqrt(c_i^2+u b_i^2)=G. Let D_i=sqrt(c_i^2+u b_i^2), q_i=(1/2)atan(sqrt(u)tan k_i), p_*=k/2+q, and R=R_max(k)>0. Put mu_*^2=R, delta=R-mu^2>0, and send delta to zero at this fixed k.

For the mass-independent function R(q)=C(q)^2/G-T(q), with C=sum b_i sin q_i cos q_i and T=sum c_i sin^2 q_i, the negative Hessian at q_* is

 K=2 diag(D_i)-(2/G)vv^T,  v_i=b_i c_i/D_i.

The stationary equation gives

 G-sum v_i^2/D_i=u sum b_i^4/D_i^3>0.

Consequently K is positive definite, including directions with zero components, and

 det K=8 (product D_i) (u/G) sum b_i^4/D_i^3.

There are exactly two minima in a momentum cell of side pi (the exchanged daughters), and sixteen on the full 2pi torus (the eight independent pi shifts). This multiplicity follows from the exact coordinate maximization and the strict maximum in u; it is not an assumed flavor count.

At threshold e_+=(sqrt S)(1+sqrt u), e_-=(sqrt S)(1-sqrt u), so e_+e_-=S(1-u). For f=omega-e(p)-e(k-p), the mass derivative coefficient is

 A=omega/(2e_+e_-)=1/[sqrt S(1-u)].

The exact product identity

 [ (e_++e_-)^2-G ][ (e_+-e_-)^2-G ] =4G[R(q)-mu^2]

and its nonzero second factor show near each minimum

 f=A[delta-(1/2)y^T K y]+higher-order terms,

where y is displacement from the threshold momentum. In particular the pair-energy Hessian at threshold is A K. Compactness gives a strictly positive gap away from the finite minimum set; thus only these neighborhoods contribute for sufficiently small delta. The parametric Morse lemma or a local change to quadratic coordinates yields

 integral_neighborhood d^3p S_lambda(p) delta_D(f)
 =4pi S_lambda(p_*) sqrt(2delta)/(A sqrt(det K))+o(sqrt delta).

The spin sum is positive for every real nonzero vertex vector a. If t'=s_q-2(a_hat.s_q)a_hat, Cauchy applied to (mu,s_p),(mu,t') gives

 S_lambda=|a|^2[e_p e_q+mu^2-s_p.t']/(e_p e_q)
 >=2mu^2|a|^2/(e_p e_q)>0.

At q_* every |q_i|<pi/4, so cos q_i is nonzero and a_i=epsilon_i cos q_i cannot vanish for a unit polarization. Exchange and pi shifts leave S_lambda and K invariant. Let S_0 be either this single-polarization value or its average over the two incident polarizations, evaluated at mu=mu_*.

For the two central minima, the width therefore has the exact leading onset

 Gamma_central=2 alpha (1-u) S_0 sqrt(2delta)/sqrt(det K)+o(sqrt delta).

The complete naive torus width is eight times the central-cell width, exactly at tree level. Here the central cell includes the two exchanged minima, not one. The rate has dimensions of inverse lattice time; physical width is Lambda times it. This local result proves a nonzero coefficient for an open neighborhood above threshold. It does not set a uniform astronomical attenuation margin, resum self-energies, remove doublers, or provide a detector response.

Consistency check only: as k=r n tends to zero, K has det K=4r^2 A4+O(r^4), u=1/2+O(r^2), S_0=r^2 A4/2+O(r^4). Define chi_exact=R(k)/mu^2; then delta=mu^2(chi_exact-1) exactly. The earlier leading-order chi=A4 r^4/(64mu^2) instead satisfies delta/mu^2=chi-1+O(r^2 chi). Thus replacing chi_exact by chi arbitrarily close to the finite-r threshold is incorrect. The corresponding coefficient 2sqrt2 alpha mu^2/r sqrt(chi-1) is only a formal overlap comparison when r^2 is much smaller than chi-1, which is itself small. No uniform interchange or quantitative remainder is asserted. This qualification is a correction prompted by the independent check.
