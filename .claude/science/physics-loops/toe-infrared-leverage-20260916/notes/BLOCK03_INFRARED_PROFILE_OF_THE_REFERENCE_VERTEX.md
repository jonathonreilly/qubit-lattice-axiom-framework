# Infrared profile of the reference current vertex

**Author mathematical proposal, no independent review or audit.** This computes the infinite-cubic reference form factor identified in [BLOCK02](BLOCK02_ORTHOGONAL_TRANSVERSE_SECTOR_AND_CURRENT_VERTEX.md). It does not compute the interacting spectral density, a beta function, an infraparticle, or the actual ground state.

## 1. Exact reference symbol

For the unit-weight infinite cubic Maxwell reference, on k in [-pi,pi]^3, put

    d_i(k)=exp(i k_i)-1, omega(k)=sqrt(sum_i |d_i(k)|^2),
    P(k)=I-d(k)d(k)*/omega(k)^2,
    A(k)=omega(k)P(k).

The single zero Fourier point can be assigned arbitrarily for L2 statements. The transverse mode profile of an oriented link at the origin is

    v_i(k)=omega(k)^(-1/2)P(k)e_i.                    (1)

This is the bulk counterpart of K^(1/2)P e in BLOCK02. Inner products use dk/(2pi)^3. The diagonal projector is

    ||P(k)e_i||^2=1-|d_i(k)|^2/omega(k)^2.

Its angular average near zero is 2/3, not one. This is a transverse two-polarization reference calculation.

## 2. Exact low-frequency integral and bounds

For 0<lambda<=1 use q_i=2sin(k_i/2). This is one-to-one on the Brillouin cube; omega=|q| and

    dk=J(q)dq, J(q)=product_i(1-q_i^2/4)^(-1/2).

The ball |q|<=lambda lies inside its image. Therefore

    ||1_(A<=lambda) v_i||^2
      =(2pi)^(-3) integral_0^lambda r dr
          integral_(S^2)(1-n_i^2)J(rn)dn.            (2)

The spectral projection in (2) is within the transverse space. It does not include the longitudinal zero eigenspace, on which v_i is zero.

For 0<=r<=1,

    1<=J(rn)<=(1-r^2/4)^(-3/2)<=1+r^2.

The last inequality follows by differentiating in r^2: the derivative is at most (3/8)(3/4)^(-5/2)<1. Since integral_(S^2)(1-n_i^2)dn=8pi/3, equation(2) gives the explicit bound

    lambda^2/(6pi^2)
      <=||1_(A<=lambda) v_i||^2
      <=lambda^2/(6pi^2)+lambda^4/(12pi^2).           (3)

Expanding the same smooth Jacobian uniformly gives

    J(rn)=1+r^2/8+O(r^4),
    ||1_(A<=lambda) v_i||^2
      =lambda^2/(6pi^2)+lambda^4/(96pi^2)+O(lambda^6).

The coefficients follow from the analytic integral, not a fit to the finite lattice sums.

## 3. Energy-weighted norms distinguish two obligations

For 0<sigma<lambda<=1 and p>=0, the same exact integral has radial factor r^(1-2p):

    ||1_(sigma<A<=lambda) A^(-p)v_i||^2
      =(2pi)^(-3) integral_sigma^lambda r^(1-2p)dr
          integral_(S^2)(1-n_i^2)J(rn)dn.            (4)

At p=1/2 the integral is finite down to sigma=0. Thus v_i is in the domain of A^(-1/2). At p=1,

    0 <= ||1_(sigma<A<=lambda) A^(-1)v_i||^2
           -(1/(3pi^2))log(lambda/sigma)
      <=(lambda^2-sigma^2)/(6pi^2).                  (5)

Consequently v_i is not in the domain of A^(-1). The coefficient 1/(3pi^2) is exact. Contributions away from k=0 are finite and cannot remove this positive logarithmic divergence.

The per-link leading vertex in BLOCK02 is (g/sqrt(2))eta v_i. At any fixed nonzero g and eta>0, its inverse-energy norm has coefficient g^2 eta^2/(6pi^2) multiplying log(1/sigma). Its energy-form norm remains finite. Multiplication by a matter-current matrix element that vanishes at low momentum could change this conclusion; no such matrix element has been supplied here.

## 4. Matching a local free-box form factor to the bulk reference

Center successively larger free cubes around a fixed link and embed their edge spaces in the infinite lattice. Their positive matrices C*C converge on finitely supported vectors, and are uniformly bounded by12. Continuous functional calculus therefore converges strongly. The function defining v_i is x^(-1/4) on x>0 and zero at x=0, so its singular endpoint needs an additional bound.

The tensor eigenfunction estimate used in BLOCK01 supplies that bound. For a fixed link, the spectral mass of K=(C*C)^(-1/2) on 0<sqrt(x)<=lambda is bounded above by the corresponding mass of H1^(-1/2) on that interval. The two operators commute with the Hodge decomposition and agree on S; the extra gradient contribution is nonnegative. Every tensor eigenfunction has squared value <=8/(L+1)^3 and sqrt(lambda_n)>=2|n|/(L+1). A shell sum up to |n|_infinity<=(L+1)lambda/2 bounds the mass by C lambda^2 uniformly in L; if this radius is below one the sum is empty. Indeed the bound is at most14 M(M+1)/(L+1)^2 with M=floor((L+1)lambda/2), which is <=7lambda^2 when M>=1.

A continuous cutoff removing 0<sqrt(x)<delta hence changes the local form factor in squared norm by at most C delta^2 uniformly. First let the box grow with delta fixed, then let delta decrease to zero. This proves convergence of the local finite-box profile to (1), and convergence of K_ee to its finite bulk value. In particular eta_e=exp(-g^2 K_ee/4) converges to a strictly positive constant at fixed g.

This statement concerns the chosen reference modes. It does not identify the actual interacting finite-volume vacuum or transport a gap theorem between boundary conventions.

## 5. What the calculation changes

The local current vertex is finite, but applying a bare free-photon energy inverse to it produces a logarithmic norm divergence. A uniform all-state perturbative elimination cannot be justified merely by the local vertex norm. Energy-form estimates, a coupled fermion/photon denominator, current cancellations, coherent dressing, or a multiscale construction are materially different remaining routes.

No route to the actual phase is ruled out here. In particular, the calculation does not prove that interactions stay strong at macroscopic scales or that the axioms need to change. It identifies the particular inverse estimate that fails and the current information that a successful replacement must supply. The physical-wall count is zero.

## 6. Checks and scope controls

The runner uses two distinct calculations: direct Cartesian sums of the lattice dispersion on periodic grids N=16,32,64,128,256, and spherical quadrature after the exact low-frequency coordinate change. The successive logarithmic slopes approach the analytically derived 1/(3pi^2). The low-frequency quadrature resolves the quadratic and quartic terms. These are numerical challenges of the formulas; the integrability and divergence conclusions follow from equations(3)-(5).

Finite grids exclude their exact zero mode, as required by the transverse reference convention. They are not samples of the compact interacting ground state. A divergence in this positive reference norm cannot be cancelled by a sign choice; a physical matrix element with an additional soft factor is a different object and remains open. The earlier campaign's bounded-time weak-coupling propagation theorem did not apply an inverse photon energy, so this calculation does not contradict it.
