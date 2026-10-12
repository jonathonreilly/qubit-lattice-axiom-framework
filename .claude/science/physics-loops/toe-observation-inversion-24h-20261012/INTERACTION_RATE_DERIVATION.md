# Local gauge vertex and a provisional decay-rate limit

Author derivation, 2026-10-12. Supplied Hamiltonian completion; focused independent derivation supports the vertex, trace and coefficient, with normalization and physical limitations made explicit below. Natural units in this note. This does not derive QED or a source/detector from framework axioms.

For dimensionless lattice spacing1 and continuous Hamiltonian time, supply four-component canonical fermions and link-centered noncompact photon coordinates. Minimal link coupling gives

 H_f=sum_x mu psi_x^dagger beta psi_x + (1/(2i))sum_(x,i)[psi_x^dagger alpha_i exp(i e A_(x,i)) psi_(x+i)-h.c.].

At A=0, h(p)=sum alpha_i sin p_i+mu beta. Fill the negative band; particles/holes are excitations relative to this supplied vacuum. Supply the canonical photon Hamiltonian H_gamma=(1/2)sum_(k,lambda)[Pi^2+omega(k)^2 A^2], with [A,Pi]=i, omega(k)=||hat k||, hat k_i=2sin(k_i/2), and unit real polarizations transverse to hat k. The link field's single-photon Fourier coefficient is 1/sqrt(2omega V). Frequency alone would not fix this normalization. The external e couples to this canonically normalized field. Link midpoint Fourier convention gives the one-photon vertex

 V_lambda(p,k)=sum_i epsilon_(lambda,i)(k) alpha_i cos(p_i-k_i/2).

The coupling e is external calibration and is factored out of V. The exact Ward difference is

 sum_i hat k_i alpha_i cos(p_i-k_i/2)=h(p)-h(p-k).

For q=k-p, s_p=sin p and s_q=sin q, define a_i=epsilon_(lambda,i) cos(p_i-k_i/2). Rank-two Dirac projectors P_+(p)=(I+h(p)/e_p)/2 and P_-(p-k)=(I-h(p-k)/e_q)/2 give the spin-summed squared vertex

 S_lambda=tr(P_+(p)V_lambda P_-(p-k)V_lambda)
 =|a|^2[1+(mu^2-s_p.s_q)/(e_p e_q)]+2(s_p.a)(s_q.a)/(e_p e_q).

For one incident polarization (or its unpolarized average), the leading golden-rule width per dimensionless time is

 Gamma_lambda=(e^2/(8 pi^2 omega)) integral_BZ d^3p S_lambda delta(omega-e_p-e_q).

No external spin average is applied to final states. The unpolarized photon averages, rather than sums, the two photon polarizations. For each independent pi shift of p, the matching components of s_p, s_q and a change sign, leaving the energy delta and spin trace invariant. Thus the complete torus integral is exactly eight times the integral over a pi-period fundamental cell. At small momentum these are eight charged Dirac species, not one observed electron. The central partial width can witness an allowed channel in this completion; discarding the other species does not provide their physical identification or removal.

Provisional scaling limit: k=r n, mu=r^2 sqrt(A4)/(8 sqrt chi), chi>1 fixed, A4=sum n_i^4. Set p=x k+l with l transverse to n of order r^2, u=x(1-x). The central-cone energy shell has, to leading order,

 |l|^2=mu^2[16 chi u(1-4u)-1].

Allowed x obey16chi u(1-4u)>1. The leading unpolarized spin sum is

 S_avg=[mu^2+|l|^2(1-2u)]/(2u^2 r^2).

Integrating the transverse delta then gives the central-cone partial width

 Gamma=alpha mu^2/(2r) I(chi)+o(mu^2/r),
 I(chi)=integral_allowed dx [2+16chi(1-2u)(1-4u)], alpha=e^2/(4pi).

In physical units Gamma_energy=alpha m^2/(2E) I(chi) to leading order; rate in inverse seconds is Gamma_energy/hbar. As chi decreases to1 after this fixed-chi scaling limit, I(chi)~4sqrt2 sqrt(chi-1). Neither error nor near-threshold uniformity is established here yet. The microscopic mass, Hamiltonian vacuum, coupling and detector identifications remain supplied. This rate cannot be extrapolated to arbitrary chi growing with1/mu or to the exact threshold without separate bounds.

The independent check verifies direct4x4 projectors, eigenspinor amplitudes, finite-difference hopping, Ward difference, all eight shifts, coarea normalization and exact axial quadrature. Its independent J(chi) equals I(chi)/(16chi), with J=[t^3/6+t^5/10+t/(8chi)] from t_- to t_+, t_+/-^2=(1+/-sqrt(1-1/chi))/2. Author quadrature provides further finite controls, not error certificates for an astronomical parameter point.

Exact local spin positivity follows by reflecting s_q across the plane perpendicular to a: t'=s_q-2(a_hat.s_q)a_hat. Cauchy for (mu,s_p),(mu,t') gives S_lambda>=2mu^2|a|^2/(e_p e_q)>0 for real a!=0 and mu>0. The central fixed-chi shell has cos weights bounded away from zero and a nonzero coarea measure for sufficiently small r.

The rate is a leading e^2 coefficient using the stated free or explicitly matched dispersions. Symmetries of this supplied spatial lattice do not by themselves set the renormalized relative photon/electron speed. An allowed O(e^2 r) correction can exceed the O(r^3) free kinematic excess, and even matched leading speeds leave O(e^2 r^3) corrections to check. No coefficient of that self-energy has been computed here. The limits of weak coupling, small momentum and approach to threshold have not been interchanged as an interacting theorem. Atmospheric shower response, source/propagation, running coupling and species identification remain separate. A kinematic opening or tree width alone does not justify importing a published95% LIV limit.
