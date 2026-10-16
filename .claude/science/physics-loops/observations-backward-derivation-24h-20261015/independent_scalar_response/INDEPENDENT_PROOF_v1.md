# Independent action-first scalar/metric response proof, v1

Exposure before this proof: only SCALAR_RESPONSE_NEUTRAL_CONTRACT_v1.json from the new response block. No root SCALAR_RESPONSE or MATTER_CLOCK argument, code or result has been opened. This is conditional mathematical support, not empirical validation or formal audit.

Normalization is explicit: use S=int sqrt(-g)[M^2 R/2 - (partial phi)^2/2 - V(phi)] - sum m int A(phi) ds_E, M>0, A>0, signature(-+++). If M in a later source denotes the coefficient M^2 rather than its square root, replace M^2 consistently; the neutral prose did not write the gravitational action coefficient explicitly. All derivatives below use Einstein cosmic time unless marked tau. rho is the bare proper rest/number density in the Einstein metric; r=A rho. alpha=A_phi/A; v=dot(phi); F=V_phi+rho A_phi; mu=V_phiphi+rho A_phiphi at fixed rho.

The action gives M^2 G_ab=T_phi,ab+T_dust,ab and Box phi=V_phi+rho A_phi. The homogeneous equations are 3M^2 H^2=r+v^2/2+V, -2M^2 dot(H)=r+v^2, dot(rho)=-3H rho, dot(v)+3Hv+F=0. Hence an exactly static flat Minkowski background with positive dust is inadmissible: dot(H)<0 even if V is adjusted to cancel the Friedmann density at one instant. No minimum or static background is imposed.

Let chi=delta(phi), P=Psi_E and Q=Phi_E. Varying Box phi directly through sqrt(-g)=a^3(1+P-3Q), g^00=-(1-2P) gives

  delta(Box phi)=-ddot(chi)-3H dot(chi)-K^2 chi
                 +v(dot(P)+3dot(Q))+2P(dot(v)+3Hv).

The perturbed source is mu chi + A_phi delta(rho). Substitution of the background scalar equation gives

  ddot(chi)+3H dot(chi)+(K^2+mu)chi
    =-A_phi delta(rho)+v(dot(P)+3dot(Q))-2F P.                 [S]

Both canonical scalar and dust have no linear anisotropic stress for a homogeneous scalar background. The scalar traceless spatial Einstein equation gives P=Q for each nonzero Fourier mode; the zero mode is excluded by the contract. Hence the metric-driving derivative in [S] is 4v dot(P).

The Hamiltonian constraint can be obtained independently from ADM. The spatial curvature perturbation is -4K^2 Q. With lapse1+P and zero shift, K^i_j=-[H-dot(Q)-HP]delta^i_j at first order. Thus delta(R3+Ktrace^2-KijKij)=-4K^2 Q-12H(dot(Q)+HP). The normal energy perturbation is

  delta(E)=A delta(rho)+v dot(chi)-v^2 P+F chi,

where F chi includes the indispensable dust mass perturbation rho A_phi chi. Therefore

  -2M^2[K^2 P+3H(dot(P)+HP)]
       =A delta(rho)+v dot(chi)-v^2 P+F chi.                 [H]

Velocity energy of nonrelativistic dust begins at second order, but the first-order dust velocity still enters the momentum constraint and evolution. No such constraint is silently replaced by a Poisson-only equation.

Eliminating delta(rho) exactly between [S] and [H] yields

  ddot(chi)+(3H-alpha v)dot(chi)+(K^2+mu-alpha F)chi
    =(6M^2 alpha H+4v)dot(P)
      +[2M^2 alpha K^2+6M^2 alpha H^2-alpha v^2-2F]P.       [E]

No time derivative or metric-source term was discarded. On the background Friedmann constraint, the P coefficient can equivalently be written

  2M^2 alpha K^2+2alpha V-2V_phi.

This is a simplification using an equation, not an omitted background correction. The eliminated curvature is

  mu-alpha F = V_phiphi-alpha V_phi+r alpha_phi,

and is not generally the fixed-bare-density curvature mu. Their difference vanishes at F=0 (or alpha=0), but that is an extra event/trajectory condition, not a conclusion from slip.

The source convention matters: for a coordinate-number contrast, delta(rho)=rho(delta_n+3P), because the proper spatial volume is a^3(1-3P). Substituting this in BOTH scalar and Hamiltonian equations gives [E] unchanged. Mixing proper-number and coordinate-number sources would introduce spurious mass/metric terms.

Conformal potentials: at fixed coordinates g_J=Abar^2(1+2alpha chi)g_E, a_J=Abar a_E and d tau=Abar dt. Consequently

  Psi_J=P+alpha chi, Phi_J=P-alpha chi,
  slip s=(Psi_J-Phi_J)/(Psi_J+Phi_J)=alpha chi/P.           [C]

The ratio requires P!=0; division by alpha additionally requires alpha!=0. An alpha=0 event has zero conformal slip regardless of mu or a nonzero chi. These potentials use the background matter-clock coordinate tau; an actual perturbed clock also carries lapse1+Psi_J. A slip measurement alone neither provides chi's initial data nor the time derivatives and amplitude P needed in [E]. An equivalent exact slip equation is [E] acting on chi=sP/alpha, retaining derivatives of s, P and alpha; replacing this by a static algebraic formula is an additional approximation.

For the matter-clock expression let sigma=v/Abar, h=H/Abar=H_J-alpha sigma and K_J=K/Abar. Since dot(chi)=Abar chi_tau and ddot(chi)=Abar^2 chi_tautau+dot(Abar)chi_tau, [E] becomes exactly

  chi_tautau+3h chi_tau+[K_J^2+(mu-alpha F)/Abar^2]chi
    =(6M^2 alpha h+4sigma)P_tau
      +[2M^2 alpha K_J^2+6M^2 alpha h^2-alpha sigma^2-2F/Abar^2]P. [J]

The -alpha v damping term cancels the time-conversion acceleration term; it must not be counted twice. In Jordan H_J notation the remaining damping is3(H_J-alpha sigma), not generally3H_J. This is still the Einstein canonical perturbation chi, without a further field redefinition.

A static Yukawa-like expression s approximately equals 2M^2 alpha^2 K^2/(K^2+mu-alpha F) only after suppressing chi acceleration, chi damping, metric derivative driving, and the full background P correction relative to the retained terms; a particular-response/initial-history prescription is also needed for that approximation. Freezing only time derivatives leaves numerator2M^2 alpha^2 K^2+6M^2 alpha^2 H^2-alpha^2 v^2-2alpha F, not just its K^2 term. In the matter clock the candidate denominator scale is(mu-alpha F)/Abar^2, not mu automatically. No positivity of mu or of mu-alpha F, minimum, static dust Minkowski background, measured density supplier or empirical validity is assumed.

Executable controls are designed independently: derive delta(Box phi) from determinant/inverse metric, derive the ADM energy/curvature pieces, exact symbolic density elimination and time conversion, and integrate the original action-derived background plus scalar, dust number, dust Euler and momentum equations on a finite expanding positive-dust fixture. Use dust velocity potential U with a^2 dot(x)=grad U: dot(delta)=3dot(P)+K^2 U; dot(U)=-P-alpha chi-alpha v U; dot(P)=(v chi-rU)/(2M^2)-HP. Initial delta is fixed by [H], not by a chosen quasistatic source. The original scalar equation [S] evolves chi; [H] and [E] are checked as independent residuals along the numerical solution. This is a numerical equation check, not physical observation or a high-precision trajectory.
