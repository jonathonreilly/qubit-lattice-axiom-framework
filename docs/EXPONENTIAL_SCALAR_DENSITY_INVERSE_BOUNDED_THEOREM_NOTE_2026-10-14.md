# Reconstructing local scalar action functions from density response

Status: conditional support; ideal-input inverse, not an action inferred from measured data.
Claim type: bounded_theorem. Scientific author: /root.
Primary runner: `scripts/exponential_scalar_density_inverse_check.py`.

A stationary density family gives a scale-eliminated consistency relation between
tensor gravity, coupled scalar ranges and environmental susceptibility. Under a
single-field action class, ideal density and coupling functions then reconstruct
the Jordan kinetic coefficient and potential on the sampled interval, leaving
one vacuum-energy constant. This is a constructive conditional inverse; neither
the input functions nor the selected physical state have been measured here.

The [complete supplied action](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md),
[weak force normalization](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md),
and [prescribed-density environment map](EXPONENTIAL_SCALAR_ENVIRONMENT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-10-14.md)
remain explicit dependencies. A stable scalar Hessian at fixed particles is not
a theorem of fluid, metric or apparatus stability. The probe's source constraint
changes its linear response; no constant constraint is silently selected here.
All computational examples are exposed synthetic development data. There is no
measured likelihood, independent empirical validation or complete action/state/
scale selection. The full two hand derivations follow without equation changes.

## 1. General stationary susceptibility and scale elimination

Personally derived by /root. Conditional local theorem, not a measured fit. This extends the prescribed-particle density analysis without changing its final v3 source or any sealed evidence. The complete candidate action remains supplied. Natural units c=1 until section 5; Q is held fixed across the stationary family.

### 1. Precisely varied source and field data

Use local normal field coordinates chi^i at one stationary point for the supplied kinetic action -Q K_AB partial phi^A partial phi^B. Thus the canonical kinetic coefficient is -Q, not -Q/2. Write Y=Hv^2 U, A=sqrt(C)>0, beta_i=partial_i ln A and rho_*=m_J n_E, with particle number per local Einstein proper three-volume. The Einstein metric is fixed for the scalar variation. The physical rest density is rho_J=rho_*/A^3 and rho_E=A rho_*=A^4 rho_J. The scalar stationarity equation is

    F_i=Y_i+rho_* A_i/(2Q)=0.                         (1)

The fixed-particle Einstein squared mass matrix is the covariant Hessian

    M_E^2 = Hess(Y)+rho_* Hess(A)/(2Q).                (2)

These formulas come directly from the particle action -m_J integral A ds_E. Assume a differentiable local stationary family parametrized by positive rho_J, and a positive-definite M_E^2 at the point under consideration. This is scalar stability for the prescribed particles, not a fluid/gravity stability theorem. The implicit function theorem supplies a locally differentiable branch under the positive-definite condition below; it does not prepare or dynamically populate it.

At fixed physical density, rho_* changes as A^3. Defining c_rho=rho_E/(2Q)>0, differentiation of (1) along the stationary family gives

    [M_E^2+3 c_rho beta beta^T] dchi
       = -c_rho beta d ln rho_J.                     (3)

The additional rank-one term is a physical-volume effect. It is not part of the fixed-particle mass (2). Both matrices in (3) are positive definite under the premise above. Local field-coordinate connections cause no extra term in the derivative of the zero covector F; the invariant statement is obtained by using a K-orthonormal frame.

### 2. Exact susceptibility identity

Set zeta=c_rho beta^T (M_E^2)^(-1) beta >=0. The rank-one inverse identity yields

    d ln A / d ln rho_J = -zeta/(1+3 zeta),
    B := -d ln G_bare / d ln rho_J = 2 zeta/(1+3 zeta),
    zeta = B/(2-3B).                                 (4)

Here G_bare=A^2/(8 pi Q) and the same Q is used across the family. Therefore 0<=B<2/3 for finite positive masses; B=0 iff beta=0. The equality B=2/3 is a singular/limiting case, not attained under the finite positive-definite premise. The logarithmic A slope lies in (-1/3,0] on this stable family. An earlier negative-u stationary-map bound (-1/2,0) included unstable stationary points, so these results do not conflict.

At a frozen background M_J^2=M_E^2/A^2. Let m_i,J^2>0 be its eigenvalues in a K-orthonormal frame and q_i=(e_i dot beta)^2. Then

    zeta = 4 pi G_bare rho_J sum_i q_i/m_i,J^2,
    sum_i q_i = q = |beta|^2.                        (5)

No Hv or Q remains separately in this relation. They have been replaced by the local measurable tensor-force normalization and local density, conditional on reconstructing that normalization. This eliminates them from this one consistency relation; it does not derive their fundamental values.

For one coupled mass, or the coupling-weighted harmonic mass

    m_eff^2 = q / sum_i(q_i/m_i,J^2),  q>0,

we obtain

    m_eff^2/(4 pi G_bare rho_J)=q(2/B-3).             (6)

The effective mass is between the smallest and largest coupled masses. This identity constrains a weighted response and cannot determine all masses separately. In the revised candidate at x=y=0, the density source and coupling are radial and the mass matrix is diagonal, so m_eff=m_u,J. Substituting the earlier S_env=-A d_J'/d_J and B=2/S_env recovers

    m_u,J^2/(4 pi G_bare rho_J)=q(S_env-3).           (7)

Positive radial mass is equivalent to S_env>3 for that one coupled direction; the candidate's two transverse masses are separately positive. For a generic multi-field theory, satisfying (4) or 0<B<2/3 is only necessary for the full positive-mass premise, not sufficient. An uncoupled or weakly coupled negative eigenvalue can be hidden from this scalar contraction. For example M_E^2=diag(1,-4), c_rho=1 and beta=(1/5,1/10) give zeta=3/80>0 and the same apparently stable interval for B despite one unstable field. This counterexample lies outside the theorem's positive-definite hypothesis and defeats its converse, not the theorem.

### 3. What has and has not been selected

Equations (3)-(6) hold for any smooth potential and conformal coupling satisfying the explicit local premises. Agreement would test that prescribed-source stationary description, not distinguish this candidate's supplied potential from every alternative. Candidate-specific content still resides in q(A), d_J(A), the mass spectrum and higher responses. A state, equilibration mechanism, finite-body solution, metric backreaction, source pressure, quantum state and action-selection mechanism have not been supplied by this differentiation.

The derivative is between stationary configurations of different densities. It is not the time derivative during an evolving density change; adiabatic tracking requires its own separation of timescales and preparation. Nor is (4) a direct observation of A in universally coupled matter units.

### 4. A laboratory readout still needs its geometry

An actual positive calibrated response has G_cal=gamma(rho_J) G_bare. Thus

    B=-d ln G_cal/d ln rho_J + d ln gamma/d ln rho_J. (8)

For positive Newton-force kernels the earlier finite-body theorem gives 1<=gamma<=1+q in the frozen stable weak regime. That range alone does not bound its derivative. The mathematical envelope example gamma=1+(q/2)[1+sin(omega ln(rho_J/rho_ref))], for fixed q>0, remains in the interval while its logarithmic derivative at rho_ref grows without bound with omega. This is a counterexample to inferring a derivative bound from an amplitude bound; it is not a claimed apparatus solution.

A prospective observational use therefore requires enough spatial-range and source-geometry information to reconstruct G_bare and the coupled q_i,m_i. An ideal point-source sum of Yukawa responses provides such model observables in principle; finite size, readout conditioning and environmental backreaction remain separate. No unpublished experimental precision or independent dataset is assumed here. Density scans used to construct the derivative would be calibration/development data; a separate configuration would need to be reserved before a prediction could be called an independent test.

### 5. SI convention and checks planned before execution

If rho_m is physical mass density in kg/m^3 and mu_i is the inverse range in m^-1, (5) is

    zeta=(4 pi G_bare,SI rho_m/c_light^2) sum_i q_i/mu_i^2.

The single-mode identity is

    c_light^2 mu_J^2/(4 pi G_bare,SI rho_m)=q(2/B-3). (9)

For energy density use rho_energy/c_light^2 in place of rho_m. A missing c_light^2 would mix inverse-length squared and inverse-time squared. Neither SI G nor rho_m is assigned an empirical value in this block.

The executable controls will reconstruct (3) by differentiating an independently built source at a stationary point, verify a rational two-field rank-one inverse and a non-diagonal positive matrix, test the hidden unstable-direction counterexample and amplitude-versus-slope counterexample, and compare with the candidate's saved direct roots without solving or fitting them again. Actual altered implementations will remove the volume term, change the kinetic factor and omit the conformal mass conversion. These are model-development controls, not observed measurements. Full execution and failure records will be retained separately from this hand source.

## 2. Single-field action inverse and source-control distinction

Personally derived by /root. This is an inverse theorem for ideal input functions, not a reconstruction from already measured data. It keeps the action-class and source-control premises visible. No state selector, raw-data fit or fundamental scale value is introduced.

### 1. Scope of the inverse

Restrict the supplied candidate to x=y=0. This is a consistent classical truncation for its matter coupling: K_uu and A depend only on u, partial_x K_uu=partial_y K_uu=0, and U_x=U_y=b_x=b_y=0 there. It does not select that sector dynamically or identify arbitrary transverse action functions. More generally consider a single coupled dimensionless scalar chi with Einstein action

 S=integral sqrt(-g_E)[Q R_E/2-Q(partial chi)^2-V_E(chi)]+S_m[A(chi)^2 g_E,psi].

Let Q>0 be fixed, A>0 and q=(d ln A/d chi)^2>0 on a connected branch. Work in natural units. The ideal reconstruction inputs are the tensor-force coefficient G=G_bare=A^2/(8 pi Q), the coupling q as a function of G, and the stationary physical nonrelativistic rest density rho_J as a function of G, all in common physical units. These would require controlled readout geometry, environment and source response. No such complete measured functions have been obtained here. G_cal alone is not automatically G.

### 2. The conformal action transformation is derived, not chosen

Put F=Q/A^2=1/(8 pi G), lambda=ln A, and V_J=V_E/A^4. For g_E=A^-2 g_J, the Ricci contribution is

 sqrt(-g_E) Q R_E/2
 =sqrt(-g_J)[F R_J/2+3F box_J lambda-3F(partial lambda)^2].

After a boundary integration, 3F box lambda gives -3 partial F partial lambda=+6F(partial lambda)^2. The original scalar kinetic term becomes -F(partial chi)^2=-F(partial lambda)^2/q. Since partial lambda=-partial F/(2F), the action is

 S=integral sqrt(-g_J)[ F R_J/2 - omega(F)(partial F)^2/(2F)-V_J(F)]
     +S_m[g_J,psi],
 omega(F)=(1/q(F)-3)/2.                                  (1)

This field redefinition requires q>0 to use F as a coordinate. A zero coupling point must be treated in a different chart. For the candidate q<1/3, omega>0; the invariant kinetic positivity condition is 2omega+3=1/q>0. Positivity is not inferred merely from an arbitrary Jordan kinetic coefficient. Boundary terms and admissible variations must be handled consistently. No additional free omega function has been postulated: under these class premises it is reconstructed from the supplied ideal response function q(F).

The corresponding Einstein coordinate is determined up to orientation and an additive constant:

 dchi = +/- d ln F/(2 sqrt(q(F))).                       (2)

An absolute Q and a globally chosen Einstein normalization are not obtained by this reparametrization.

### 3. The density family reconstructs a potential, with one surviving constant

Vary the particle action at fixed Einstein proper particle density rho_*=m_J n_E and fixed Einstein metric. Its energy density is rho_* A. The stationary equation is

 dV_E/dchi + rho_* dA/dchi=0.

Because rho_*=rho_J A^3 and A_chi is nonzero, on the stationary family

 dV_E/dA=-rho_J(A) A^3.                                 (3)

Changing to F and V_J gives the exact first-order reconstruction equation

 2F V_J'(F)-4V_J(F)=rho_J(F),
 V_J(F)=F^2[C+integral_(F_ref)^F rho_J(f)/(2 f^3) df].     (4)

Equivalently,

 V_J(G)=[G_ref^2 V_J(G_ref)
             -(1/2)integral_(G_ref)^G rho_J(g) g dg]/G^2. (5)

Thus q(F) and rho_J(F), if they were determined on an interval, reconstruct the single-field Jordan action functions there up to one potential constant C. The homogeneous ambiguity V_J->V_J+C_add F^2 is exactly a constant Einstein potential shift V_E->V_E+C_add Q^2. It leaves the stationary density equation and its scalar derivative unchanged. It changes the gravitational stress and curvature, so it is not an equivalence of complete background solutions. No off-interval extension, transverse field metric/potential or unique three-field action follows.

A reference curvature can remove this remaining constant only with additional justified data. If the scalar is constant in a region and its derivative stress vanishes, the Jordan metric trace for dust is F R_J=rho_J+4V_J. Then one measured R_J and rho_J there supplies V_J=(F R_J-rho_J)/4. A generic rolling or spatially varying region has derivative terms; using that formula there would import a false premise. The present expansion rate alone is not such a curvature measurement.

### 4. The probe's density constraint changes the mass coefficient

Let M_0,E^2 be the scalar Hessian at fixed rho_* divided by the actual kinetic coefficient 2Q. In the notation of the preceding susceptibility theorem it is Hess(V_E/(2Q))+rho_* Hess(A)/(2Q). If an imposed local perturbation instead has

 delta ln rho_* = p delta ln A,

then differentiating the scalar source gives

 M_p,E^2=M_0,E^2+p c_rho beta beta^T, c_rho=rho_E/(2Q).

For several fields this formula is written in a K-orthonormal field frame, with beta_a=e_a^A partial_A ln A and M^2 the corresponding mass matrix. In general field coordinates the covariant Hessian shift is p c_rho beta_A beta_B, while the mass endomorphism shift is p c_rho K^{AC} beta_C beta_B. With that basis convention, the expression holds when the scalar proportional-response law is stipulated. It is a local source prescription; actual material dynamics could be frequency dependent, nonlocal or tensorial and must be derived separately. It does not establish a pressure-supported or self-gravitating source.

For the single coupled mode and a frozen frame,

 m_p,J^2=m_0,J^2+p q rho_J/(2F).

On a positive-density portion with rho_J'(F)!=0, the local inverse and logarithmic derivative are defined, giving B=-d ln G/d ln rho_J=rho_J/(F rho_J'). The mass formulas below do not require division by rho_J or rho_J'; they remain algebraic identities at zero or turning densities wherever the underlying stationary family is smooth. The reconstruction yields

 m_0,J^2=q[rho_J' -3rho_J/(2F)],
 m_p,J^2=q[rho_J' +(p-3)rho_J/(2F)],
 m_3,J^2=q rho_J'.                                      (6)

Here p=0 fixes Einstein particle density, while p=3 fixes the physical density in the source algebra at fixed Einstein metric. They are different source-response prescriptions, not different predictions for the same fully specified experiment. For example keeping physical density fixed can require particle/geometry control; a reservoir or its support stress has not been constructed. A physical Jordan-frame scalar equation after eliminating the metric trace has the corresponding fixed-source coefficient q(2F V_J''-2V_J')=q rho_J' about a constant stationary background. That algebraic agreement does not show that a particular apparatus holds the required source fixed or that its full coupled spectrum is this coefficient.

The earlier stable fixed-particle susceptibility bound is B<2/3. It must not be inferred from positivity of m_3 alone. The function rho_J(F)=rho_ref(F/F_ref)^n, n>0, supplies a counterexample family: B=1/n, m_0^2=q rho_J(n-3/2)/F and m_3^2=q rho_J n/F. Thus 0<n<3/2 has a positive fixed-physical-density coefficient but a negative fixed-particle mass. This does not violate frame equivalence: changing the held-fixed matter data changes the perturbation problem.

### 5. Constructive exact inverse examples and what can be tested

For that power-law family, n!=2 gives

 V_J=C F^2+rho_ref F^n/[2(n-2)F_ref^n].

At n=2 the exact solution is

 V_J=F^2[C+rho_ref ln(F/F_ref)/(2F_ref^2)].

Both satisfy (4). C can be chosen so that V_J>0 on a chosen compact interval, but choosing C in a synthetic control is not a derived vacuum energy. The examples with n=1 and n=3 will explicitly distinguish the two mass prescriptions. A nonconstant positive q(F) will test the kinetic transformation without freezing omega by assumption. Added C F^2 will demonstrate the density/response degeneracy while changing the metric trace.

The candidate's original density map is a conditional specialization of this inverse. It will be checked by differentiating its transformed original potential, not fitted to new data. A density curve alone supplies neither q nor the potential offset; a single density point supplies only one equation, not an entire function. Multiple reconstructed action functions agreeing with these ideal inputs remain unconstrained off the sampled interval and in unprobed field directions. Preparing equilibrium and acquiring an independent validation configuration are unresolved empirical tasks.

### 6. External convention cross-check

The Jordan action, trace-eliminated scalar equation and constant-omega mass convention were checked against Quiros et al., arXiv:1506.05420v2, pp.2-3, Eqs.(1)-(3),(8). Its action is twice ours under F=phi and V=V_J, so the field equations agree. Only this normalization check is used; its environmental phenomenology and broad frame claims are not adopted. The variable-omega term is derived separately by variation here. The earlier Khoury/Weltman particle-density convention remains a separate source.

This source was accessed during model development before the new controls. It is not an independent empirical test. Original PDFs and exact local commands are retained. The calculations and inverse conclusions above are personally derived from the declared action and density definitions.

## Reproducible scope and evidence

The runner makes the earlier96 density controls fresh, then applies53 general
susceptibility,63 inverse-action and28 basis/domain controls, preserving their
complete rows and substantive outputs. Candidate roots are recomputed in memory
rather than loaded from a campaign scratch file. These totals distinguish reused
science from the new inverse statements; they are not240 measured experiments.

The inverseB formula requires positive density and a nonzero density derivative.
Undivided mass identities still hold at smooth turning or zero-density points.
The multifield mass formula uses a K-orthonormal frame; a general-coordinate
endomorphism requires K inverse. Original source v1 and the v2 clarification,
affected-only controls, all actually damaged implementations and independent
source/correspondence reports are preserved. No old failure or source version
is replaced by the canonical result.

The external convention reference is [Quiros et al., arXiv:1506.05420v2](https://arxiv.org/pdf/1506.05420v2),
pp.2–3. Only its action/equation normalization was used. Its phenomenology and
broad frame conclusions are not adopted. This was an exposed development source.
