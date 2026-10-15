# Independent full rolling scalar–dust equations and momentum inverse

This derivation is frozen before reading root's new M14 working note or code. Root remains scientific author. The starting action is exactly the supplied task premise; the prior M12 candidate action is a separately identified conditional source for the transverse-decoupling paragraph. No observation, prior finite-mode sign claim, external literature search, formal audit or new state-selection principle is used.

## 1. Definitions and action variation

Use natural units, signature (-+++), Q>0 constant, A(chi)>0 smooth and V(chi) smooth:

    S=int sqrt(-g)[Q R/2-(partial chi)^2/2-V(chi)]
      +S_m[A(chi)^2 g,psi].

Einstein cosmic time is t; dots below mean d/dt. Set b=d ln A/dchi and b_chi=db/dchi. Einstein dust rest-energy density is rho=m A N, with conserved rest-frame number density N. Background variables obey

    pi=chidot,
    3Q H^2=rho+pi^2/2+V,
    Hdot=-(rho+pi^2)/(2Q),
    pidot=-3Hpi-V_chi-b rho,
    rhodot=(-3H+b pi)rho.                                   (B)

The matter variation is delta S_m=sqrt(-g)b T delta chi with T=-rho. Thus box chi-V_chi=-b T=b rho. Dust energy exchange is nabla_mu T_m^{mu nu}=b T nabla^nu chi. Conserved number and variable mass yield the same background rhodot. The force law is

    u^mu nabla_mu u_nu = -b(delta_nu^mu+u_nu u^mu)partial_mu chi.

These signs fix all later conventions. The background Friedmann residual has zero time derivative under (B); it must be imposed initially.

Let chi=chibar+sigma, and define n=delta N/Nbar as the perturbation of the Einstein rest-frame NUMBER density. Then

    delta rho=rho(n+b sigma),
    delta p_chi=pi sigmadot-pi^2 Psi-V_chi sigma,
    delta rho_chi=pi sigmadot-pi^2 Psi+V_chi sigma.

The coordinate-volume number contrast is instead n_c=n-3Phi. It has a simpler continuity equation, but is not the n used here. An author using n_c must also change the density-source formula; notation differences alone are not sign defects.

For a nonzero comoving Fourier wave number k, K^2=k^2/a^2>0 and laplacian=-k^2. The metric and covariant velocity convention are

    ds_E^2=-(1+2Psi)dt^2+a^2(1-2Phi)dx^2,
    u_i=partial_i v,
    u^0=1-Psi, u^i=a^-2 partial_i v.

In particular v is a COVARIANT velocity potential, not a physical-velocity divergence. Its Euler equation has no H term by itself.

## 2. Complete linear equations, with metric slots explicit

Canonical scalar plus pressureless dust has no linear anisotropic stress about a homogeneous background. For k!=0 this gives Phi=Psi. Before imposing that equality, the relevant metric slots are:

    00:  -2Q[K^2 Phi+3H(Phidot+H Psi)]
          =rho(n+b sigma)+pi sigmadot-pi^2 Psi+V_chi sigma; (E00)

    0i:  2Q(Phidot+H Psi)=pi sigma-rho v;                 (E0i)

    number: ndot=K^2 v+3Phidot;                         (N)

    Euler: vdot+b pi v=-Psi-b sigma;                    (V)

    KG: sigmaddot+3H sigmadot
        +[K^2+V_chichi+rho(b_chi+b^2)]sigma
        =pi(Psidot+3Phidot)-2(V_chi+b rho)Psi-b rho n.    (KG)

No quasistatic, small-mass, adiabatic-state or neglected-homogeneous-mode approximation has entered these equations. The b^2 rho term comes from using NUMBER contrast n: delta rho/rho=n+b sigma. With an Einstein energy-density contrast instead, this term is moved into the source; it cannot simply be omitted.

The number equation follows from sqrt(-g)N u^0=a^3 Nbar(1+n-3Phi), so the lapse Psi cancels from that product. The covariant Euler equation follows from u^mu nabla_mu u_i=partial_i(vdot+Psi) and force_i=-b partial_i(sigma+pi v). This verifies that spatial Phi enters continuity and time Psi enters force.

For KG, direct expansion of the d'Alembertian gives

    delta(box chi)=-sigmaddot-3H sigmadot-K^2 sigma
       +2Psi(pidot+3Hpi)+pi(Psidot+3Phidot).

Perturbing box chi-V_chi=b rho and then using (B) yields (KG). In particular the lapse term includes -2 b rho Psi as well as -2 V_chi Psi. Einstein-frame dust has delta T=-delta rho, without an additional lapse factor in that trace; the displayed lapse term arises from the wave operator and the background equation.

Setting Phi=Psi=phi, the spatial trace equation is

    phiddot+4H phidot+(2Hdot+3H^2)phi
       =(pi sigmadot-pi^2 phi-V_chi sigma)/(2Q).           (Eij)

All metric-slot statements above follow the metric actually written here. No claim about a differently named prior note is made without inspecting that note's explicit metric convention.

## 3. Evolution, constraints and both scalar initial data

Let p=sigmadot. Use (E0i) as the metric evolution equation

    phidot=(pi sigma-rho v)/(2Q)-Hphi.

Together with (N), (V), sigmadot=p and (KG), this is a five-component first-order system for (phi,sigma,p,n,v). The undivided initial 00 constraint, after using (E0i), is

    C=(2QK^2-pi^2)phi+pi p
       +(3Hpi+V_chi+b rho)sigma+rho n-3Hrho v=0.         (C)

Direct differentiation using the background and the five evolution equations gives

    Cdot=-3H C,                                         (CP)

and the left side minus the right side of (Eij) is identically zero. An independent symbolic calculation is preserved in CONSTRAINT_DERIVATION_SCRATCH_v1.json; the formal control script will reproduce it. Thus initial C=0 propagates, without solving a quasistatic algebraic scalar equation or discarding a scalar homogeneous solution.

Both sigma(t0) and p(t0) are free perturbation data subject to the combined gravitational/matter constraints, not a chosen particular response. With rho>0 one can choose sigma,p,phi,v and solve (C) for n; this exhibits the two scalar and two dust phase-space freedoms. Alternatively solving for phi divides by 2QK^2-pi^2, which may vanish and is not generally safe. The undivided constraint or solving for n avoids pretending that this coefficient is always positive. Initial states of different modes may differ, but cannot violate the Einstein constraints.

## 4. Exact linear conformal map

Use Jordan cosmic background time tau and scale factor a_J:

    d tau=A dt, a_J=A a,
    H_J=(H+b pi)/A, F=Q/A^2,
    Psi_J=Psi+b sigma, Phi_J=Phi-b sigma,
    v_J=A v,
    delta_J=n-3b sigma, rho_J=rho/A^4.                   (J)

Here Jordan dust has fixed particle mass, so its number and energy-density contrasts agree. Einstein energy contrast n+b sigma=delta_J+4b sigma. The sum Phi_J+Psi_J=Phi+Psi=2phi is invariant. The coordinate-volume number contrast n-3Phi=delta_J-3Phi_J is also invariant.

The Jordan equations directly follow:

    d delta_J/dtau=K_J^2 v_J+3 dPhi_J/dtau,
    d v_J/dtau=-Psi_J,
    K_J=K/A, rho_J,tau=-3H_J rho_J.                     (JD)

Indeed d(A v)/dtau=vdot+b pi v, giving the correct time-potential force. No perturbative time-coordinate shift beyond the background relation d tau=A dt is made here. Nonzero Fourier modes fix the irrelevant spatially constant velocity-potential ambiguity.

## 5. Exact three-mode momentum inverse

This inverse is a consequence of the complete linear system, rather than of a quasistatic field closure. It still presupposes calibrated physical fields and a supplied scalar-plus-dust action class.

For each simultaneous Jordan mode j, ideal Weyl lensing gives

    phi_j=(Phi_J,j+Psi_J,j)/2.

Calibrated dust velocities and their physical-time derivative give Psi_J,j=-d v_J,j/dtau. Define the scalar conformal perturbation readout

    h_j=Psi_J,j-phi_j=b sigma_j,
    y_j=d phi_j/dtau+H_J phi_j.

Let

    lambda=d ln A/dtau=b pi/A,
    q=2Q b^2,
    Gamma=rho_J/(2F)>0.                                 (I0)

For b!=0, the Einstein momentum equation transforms exactly to

    y_j=lambda phi_j+(lambda/q)h_j-Gamma v_J,j.          (I1)

Proof: divide (E0i) by 2QA, use H=A(H_J-lambda), pi=A chi_tau, sigma=h/b, v=v_J/A, rho=A^4 rho_J and chi_tau=lambda/b. The matter term becomes rho_J v_J/(2F). No scalar initial amplitude was set in making this substitution: h_j contains the actual scalar perturbation, including any free wave.

At an epoch form the matrix with rows [phi_j,h_j,-v_J,j] and right side y_j. Three real modes (or enough independent real components of calibrated complex modes) with rank three determine

    (lambda, S, Gamma), S=lambda/q.

If lambda!=0 and S!=0, then q=lambda/S. Impose q>0, Gamma>0 and any additional candidate-specific domain; the generic canonical action does not itself impose q<1/3. Extra modes test the common coefficients. A common unknown CONSTANT amplitude for each mode rescales that row and its right side and does not change the inverse. Unknown relative channel gains or time-varying amplitudes generally do not cancel. Lensing projection and velocity bias are not removed by matrix algebra.

The alternative observable matrix [phi_j,Psi_J,j,-v_J,j] has coefficients [lambda-S,S,Gamma], so lambda is the sum of its first two fitted coefficients. Confusing that parameterization with [phi,h,-v] would change the inferred q. The sign of the velocity column is fixed by the stated covariant velocity convention.

Rank three is only a conditional identifiability gate. When b=0, h=0 and q=0; the division by b in (I1) is unavailable and scalar momentum can remain nonzero if chi_tau!=0. At a genuine turning point pi=0 with b!=0, lambda=S=0, so the momentum relation reduces to y_j=-Gamma v_J,j and instantaneous q is not recovered even if the readout matrix has rank three. Nearby smooth dynamics might constrain a limit, but that is extra information. Nearly singular mode matrices or small lambda make finite-error inference ill-conditioned. Correlated/growing modes can have rank loss; neither three labels nor three measurements guarantees rank three.

Constraint compatibility does not rule out rank-three data in principle. At one background epoch choose independent small triples (phi,h,v_J), let sigma=h/b and choose p freely; equation (C) then fixes n for each mode. The smooth full evolution supplies local solutions. This is a mathematical existence fixture, not evidence that actual surveyed modes realize a well-conditioned matrix.

## 6. What is identified about F, and remaining tests

The reconstructed coefficients must obey

    F_tau/F=-2lambda,
    Gamma_tau/Gamma=2lambda-3H_J,                         (I2)

because physical dust is conserved. Thus F(tau)/F(tau0)=exp[-2 integral lambda dtau], and with rho_J=rho_J0 a_J^-3,

    F/rho_J0=a_J^-3/(2Gamma).                            (I3)

These give the same relative history only when the second relation in (I2) holds. Absolute F remains degenerate with the unknown rho_J0: simultaneous positive rescaling of F,Q,rho_J0 and corresponding supplied action scales is not fixed by these readouts. A numerical value of measured Newton G is not silently inserted.

For b!=0 and q>0 the background kinetic equation adds a potential-independent consistency test:

    H_J,tau-lambda_tau+lambda H_J+Gamma
       +lambda^2(1/q-1)=0.                              (I4)

It follows by transforming Hdot=-(rho+pi^2)/(2Q). The background Friedmann equation similarly fixes the relative Jordan potential along a supplied valid trajectory:

    V_J/F=3(H_J-lambda)^2-2Gamma-lambda^2/q,
    V_J=V/A^4.                                          (I5)

These expressions do not establish full model membership by themselves. The scalar KG equations, 00 constraint, number evolution, background consistency and any chosen action's off-trajectory structure remain tests. Momentum inversion reconstructs necessary common coefficients; it is not a substitute for all the field equations or a selected scalar initial state. Inferring q and F ratios can challenge the revised candidate chart, but does not prove that chart was uniquely derived from nature.

## 7. Radial transverse decoupling in the supplied candidate

This paragraph imports the M12 action, exact source SHA256 dde833e8bcb69f4ab5e03eb911aa534dbf23647d5fb03cd1be469bac2e977122, previously fully reviewed and refrozen here. Its Einstein action is Q[R/2-K_AB partial phi^A partial phi^B-2Hv^2 U], with A=A(u), diagonal K, K_uu independent of x,y and U=U_rad(u)+(k/2)x^2 exp[-(1-k)u/alpha]+(k/3)y^2 exp[-(1+k)u/alpha]. K_xx,K_yy are positive and even in x,y.

The background truncation x=y=xdot=ydot=0 is invariant: A_x=A_y=0, U_x=U_y=0, and partial_x K_uu=partial_y K_uu=0 there. About this radial background, mixed radial/transverse potential derivatives vanish; the transverse perturbations have no first-order matter coupling and no first-order stress-energy source. Their homogeneous linear equations are

    delta x_ddot+(3H+dot K_xx/K_xx)delta x_dot
       +(K^2+Hv^2 U_xx/K_xx)delta x=0,

and similarly for y, evaluated at x=y=0. They may have arbitrary linear initial values without sourcing the radial/metric block at first order. This is decoupling, not a claim that their physical amplitudes vanish or that nonlinear corrections are absent. Canonical rescaling of their time-dependent kinetic factors introduces additional pump terms, so positivity of U_xx alone is not a complete stability theorem.

The radial canonical chart satisfies dchi/du=sqrt(2Q K_uu). Therefore b=(d ln A/du)/sqrt(2Q K_uu) and q=2Qb^2=|d ln A|_K^2, matching the earlier geometric convention. A nonradial background, a cross kinetic term, transverse dependence of A or loss of the stated symmetry requires the full coupled perturbation system; this one-field block does not silently cover it.

## 8. Scope and planned controls

The supplied action, minimal Jordan dust, flat homogeneous background, linear perturbation regime, smooth coefficients, common physical clocks/modes and calibrated readout map remain imports. No raw data, measured density, initial scalar wave, error budget or absolute gravitational normalization was chosen. Both scalar initial perturbations are retained. Exact derivation is distinguished from finite-data admission and numerical integration.

The independent controls will check the wave-operator metric slots, constraint propagation and trace consistency, conformal conservation, the momentum conversion and rank/turning-point cases. Deliberately omitted terms will be kept as failed closures. No new root working note/code has been opened at this checkpoint, and no prior finite-mode sign defect is alleged.
