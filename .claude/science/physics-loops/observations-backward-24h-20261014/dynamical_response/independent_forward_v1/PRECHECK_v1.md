# Independent rolling radial scalar/dust equations, pre-exposure freeze

I have read only the supplied action note and fixed forward protocol. I have not read parent forward_v1.py, run_v1, WORKING_v1 or new results. The canonical field used here is chi_can, defined by dchi_can/du=sqrt(2Q K_uu); it is distinct from the bounded algebraic variable called chi in the source confinement note. The factor 2 follows from that action's kinetic term -Q K(du)^2. All following statements are conditional on the supplied radial action, linear perturbation theory, Einstein gravity plus conformal pressureless dust, and a common Newtonian-gauge Fourier mode. They do not assert an empirical readout or choose its initial scalar state.

Write M=Q, V=2Q Hv^2 U, A=sqrt(C), b=d ln A/dchi_can. Use Einstein proper background time t, Einstein scale aE, H=dot aE/aE and physical K_E=k_com/aE. Background canonical velocity is w=dot chi_can. Then

    dot u=w/sqrt(2Q K),
    dot w=-3H w-V_chi-b rho,
    dot rho=(-3H+b w)rho,
    dot ln aE=H,
    H^2=(w^2/2+V+rho)/(3Q),
    dot H=-(w^2+rho)/(2Q).

The source form rho=A times conserved Einstein-volume number density fixes the perturbation convention. Define D=delta n_E/n_E, X=delta chi_can, Z=dot X, and covariant dust velocity u_i=partial_i v. The dust energy contrast is D+bX. In Einstein Newtonian gauge, dsE^2=-(1+2phi)dt^2+aE^2(1-2phi)dx^2; the scalar and pressureless dust have zero linear anisotropic stress. The independent evolution system is

    dot phi=-H phi+(w X-rho v)/(2Q),
    dot D=K_E^2 v+3 dot phi,
    dot v=-phi-bX-b w v,
    dot X=Z,
    dot Z=-3H Z-[K_E^2+V_chichi+rho(b_chi+b^2)]X
          +4w dot phi-2(V_chi+b rho)phi-b rho D.

The first equation is the 0i constraint with delta T^0_i=rho partial_i v-w partial_i X. Number conservation gives the second equation. The dust acceleration includes the time-dependent particle mass A. For the scalar, perturbing box chi-V_chi=b rho gives 4w dot phi+2phi(dot w+3Hw)-b delta rho-b_chi rho X. Inserting the background and delta rho=rho(D+bX) gives the displayed signs and the full rho(b_chi+b^2) term. Neither scalar time derivatives nor homogeneous perturbations are dropped.

The independent 00 diagnostic is

    C00=-2Q[K_E^2 phi+3H(dot phi+Hphi)]
        -rho(D+bX)-w Z+w^2 phi-V_chi X=0.

At t=0 set phi, X, Z and v freely as the protocol specifies, then solve only this constraint for D:

    D=[(-2Q K_E^2+w^2)phi+3H rho v-w Z
       -(3Hw+V_chi+b rho)X]/rho.

No later zero-constraint reset is permitted. An extra spatial-trace diagnostic is

    ddot phi+4H dot phi+(2 dot H+3H^2)phi
      =[w Z-w^2 phi-V_chi X]/(2Q).

Its ddot phi follows by differentiating the 0i evolution, with no separate evolution enforcing it.

The physical Jordan clock/scale map must use the same perturbed slicing. Set G=H+bw, dtJ=A dt, aJ=A aE, N=ln(aJ/aJ0). Then HJ=G/A and the Jordan metric potentials are PsiJ=phi+bX and PhiJ=phi-bX. The velocity potential transforms as vJ=A v. Consequently

    KJ=K_E/A, F=Q/A^2,
    W=KJ^2 vJ/HJ=K_E^2 v/G,
    deltaJ=D-3bX,
    d/dN=(1/G)d/dt,
    deltaJ'=W+3PhiJ',
    W'+(2+HJ'/HJ)W=-KJ^2 PsiJ/HJ^2.

Here HJ'/HJ=[dot G-bw G]/G^2. These identities follow directly from the Einstein equations above; no r=q specialization is made. The observed slip ratio inside this ideal map is r=bX/phi, generally different from the geometric q=2Q b^2. Setting q to r would remove the arbitrary scalar state that this experiment intentionally retains.

An independent momentum reconstruction is already available from these equations. Let a=aJ/aJ0, H0=HJ(0), P=-2a^3 KJ^2 phi/(3H0^2 W), g=F'/F=-2bw/G, R=rhoJ0/(3H0^2 F), and r=bX/phi. The 0i equation implies

    (2/P)R-g-r(g/q)=2+2phi'/phi.

Three simultaneous modes form a linear system with rows [2/P,-1,-r] and right side 2+2phi'/phi for [R,g,g/q]. This needs a nonsingular matrix and nonzero denominators; q=g/(g/q) additionally needs g/q nonzero. The fourth mode tests the same reconstructed triple. This has been derived here before seeing the parent's identity. It is an ideal exact-input relation, not an assurance of conditioning or obtainable observational time derivatives.

For the supplied geometric candidate, F/Fc=beta(1-3q)/(beta-q). Thus y=R(1-3q)=B-(B/beta)q with B=rhoJ0/(3H0^2 Fc). Two distinct reconstructed q epochs calibrate this line and give B and beta; later epochs and the reserved mode are tests, retaining singular cases. Calibration indices and thresholds will remain fixed. A fitted beta does not derive the action or absolute density/Planck scale.

Implementation plan: use independently written analytic radial coefficient derivatives, canonical w background state, log aE, and all four perturbation modes in one system per background. Normalize independent time to HE0*t. Use an independent Radau solver at the original rtol/atol and maximum physical step (declared methodological difference from parent protocol DOP853), and preserve any tolerance or conditioning failure. No parent code is imported. Freeze source before accessing parent outputs; compare only after independent outputs are frozen.
