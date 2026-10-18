# Native mobility, readout and momentum selection of the large neutral feature

Status: bounded-support. This block concerns the complete compact four-wall K1 graph derived from the supplied one-qubit Hamiltonian. Physical first-order energies and curvatures carry J lambda. It is not a full-H dispersion theorem. All numerical controls are exposed model development.

## Exact mobility/readout identity

Use a=cos(Qx/2), b=cos(Qy/2), c=cos(Qz/2). The punctured host has hoppings -2a,-2b; its two rays have hopping magnitude2c. For a bound energy E below the ray band, eliminate each ray with

 sigma(E,c)=(E+sqrt(E²-16c²))/2.

Let u denote the two root amplitudes of the FULL normalized bound vector, including host and rays. Differentiating the reduced eigenvalue equation gives

 E_c = sigma_c |u|² = -8c |u|²/sqrt(E²-16c²).

There is no further normalization denominator: the factor from differentiating sigma with respect to E is exactly the ray norm already included in this normalized state. This also follows by summing the ray hopping Hellmann-Feynman form.

At Qx=Qz=0, the exact coefficient curvature is

 E_zz=-E_c/4=2|u|²/sqrt(E²-16)>0.

The leading dressed original-source coefficient is lambda(-1,b), so its coefficient-model weight W=lambda²|(-1,b).u|². Wherever this overlap is nonzero, with v_E=u/|u|,

 E_zz / (W/lambda²) = 2/[sqrt(E²-16) |(-1,b).v_E|²].             (1)

Equation(1) relates native longitudinal mobility and the original readout coefficient. It is not an identity for the higher-order full-H source, nor a universal matter coupling. No new interaction is added.

At the derived threshold bc, use the previously established constants c_log=1/(8pi sqrt(bc)), D=(Dx,Dy), sigma_c=sigma(Eh,1), v the unit critical root vector. With delta=Eh-E and L=log(1/delta),

 E_zz ~ A delta L²,
 A=c_log/[sqrt(Eh²-16) sigma_c²(D.v)²] approximately0.217063831866,
 A/W0=2/[sqrt(Eh²-16)|(-1,bc).v|²] approximately8.43131882660.

Thus large transverse extent is accompanied by diminishing longitudinal mobility and diminishing local readout weight. The ratio is derived; neither quantity remains finite in this limit.

## Positive Hessian, without a stationary rest point

To justify derivatives, use the exact parameter-dependent Green integrals, not only the leading binding asymptotic. In a fixed neighborhood of (a,b,c)=(1,bc,1), the host minimum is nondegenerate and stays strictly below the ray edge. Split off that minimum and use parameter-smooth Morse coordinates. The local integrals have logarithmic expansions with smooth parameter coefficients; the complement is analytic. Fixed parameter derivatives preserve this structure. The finite cavity Schur operations do also.

Writing t=1/log(1/delta), the simple critical equation extends smoothly to t=0 as

 F(theta,t)=mu_edge(theta)-1-K(theta)t+O(t²), K>0.

Terms containing delta are exponentially flat in t. The implicit-function theorem gives smooth t(theta), with a simple zero on the critical surface. Consequently delta=exp[-1/t(theta)] has every fixed parameter derivative bounded by delta times a finite inverse power of t; these derivatives vanish on approach from the bound side. This supplies the derivative control missing from a bare undifferentiated asymptotic.

Since E=-4(a+b)-delta, at Qx=Qz=0 on the positive-Qy branch,

 E_xx ->1, E_yy ->bc, E_zz~A delta log²(1/delta)>0,
 E_y ->2sqrt(1-bc²) approximately1.94410822483.

All mixed second derivatives vanish there by evenness in Qx and Qz. The Hessian is therefore positive definite sufficiently near threshold. This differs from the negative y curvature at the compact Qy=pi anchor. The nonzero first derivative is essential: these points are moving, not local energy minima or stationary rest states. Their increasingly unequal curvatures do not supply an isotropic relativistic light cone.

For numerical corroboration, finite differences of the exact cavity root give y curvature approximately -5.91266 at b=.1, -.751454 at .15, .166336 at .18 and .199996 at .2. At .2 the z curvature is only4.58245e-9. These checks support the analytic limit; they do not certify an inflection point or replace the parameter-smooth proof. A separate L=100 finite-graph control compares the exact normalized-root identity with finite differences in ray hopping at b=.1, with discrepancy below1e-6.

## Global coefficient energy and the surviving selection assumption

In a fundamental momentum zone a,b,c lie in[0,1]. Gauge the y-ray hopping to be negative along its ray. All edge magnitudes are then monotone in a,b,c, and for any vector psi,

 <psi,K1(a,b,c)psi> >= <|psi|,K1(1,1,1)|psi|> >= -8||psi||².

The last bound follows either from the checked all-one Birman criterion (largest edge eigenvalue2-sqrt3<1, no bound below-8) or directly from the maximum absolute row sum8: ordinary host vertices have four magnitude2 neighbors, orientation roots have three such host neighbors plus one ray neighbor, and ray vertices have at most two. Frozen nonadjacent long intervals contribute zero. Widely separated host packets at Q=0 approach-8, so this is the sharp global infimum in the complete compact N4 coefficient graph.

The large bound branch instead tends to-4(1+bc), approximately-4.93903. It does not minimize this coefficient energy over momentum. Its existence and calculable overlap therefore do not derive its population or momentum selection by energy minimization. This is a conditional N4 limitation, not a full-H or cosmological no-go.

## Assumptions and reach

The supplied Hamiltonian, weak anisotropic ground regime, chosen near-threshold momentum, lattice units and physical interpretation of the Fourier bond diagnostic survive. The previously proved full-H positive-window theorem remains distinct from the coefficient dispersion studied here; no exact microscopic band velocity or lifetime is inferred. The feature is primarily two coherent, widely separated flips, with excitation energy near8J. No fermion, universal scalar coupling, cosmological initial state or empirical test is supplied by this mobility identity.
