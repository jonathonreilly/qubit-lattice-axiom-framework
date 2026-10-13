---
title: Curvature and scalar geometry for a locally normalized fluid history
claim_id: curvature-fluid-construction-bounded-theorem-note-2026-10-13
date: 2026-10-13
---

# Curvature and scalar geometry for a locally normalized fluid history

Status: proposed_retained

Type: bounded_theorem

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: Test finite-temperature matter, inhomogeneous perturbations and preparation of the displayed history.
conditional_surface_status: Conditional on the specified classical action, constant sector and ideal-fluid domain.
hypothetical_axiom_status: The independent fluid coupling and curvature-dependent scalar operators are supplied candidate assumptions.
admitted_observation_status: Local gravity motivates the normalization; the comparison target and diagnostic parameters are supplied, with no independent empirical test.
claim_type_reason: An explicit positive-kinetic construction admits the displayed exact family and conditional normalization identity.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Statement and physical question

A density inferred using a local Newton measurement need not be normalized
by the bare tensor coefficient in a cosmological action. This motivates
reconstructing both responses within one specified candidate.

For every \(0<a,b<1/3\), \(\nu,H_v,q>0\), and \(\zeta\geq0\), the action
below has positive scalar kinetic coefficients at every finite real field
value. In the constant sector \(C=3sH_v^2/2\), it admits the exact expanding,
flat, homogeneous ideal-dust/radiation family in Section 3, for arbitrary
real initial field amplitudes. Its stationary vacuum has the three positive
local squared masses in Section 5. Under the separately supplied local
weak-body, light-scalar exchange law, the ideal background satisfies
\[
 H_J^2=H_v^2+\frac{8\pi G_N}{3}\frac{1+b}{1+k}(\rho_m+\rho_r).
\]
Thus an admitted target fluid normalization fixes
\(b=S_{\rm target}^2(1+k)-1\). The choice \(b=k\) calibrates that target
to unity. It does not predict the target or the couplings.

These are conditional constructive statements. The classical metric
action, matter coupling, ideal fluids, auxiliary forms, flat homogeneity,
constant sector, initial amplitudes and positive vacuum scale are supplied.
The free coefficient \(2a/b\) controls motion away from the displayed orbit.
There is no claim of initial-state selection, global future convergence,
inhomogeneous stability, a quantum completion, measured thermal abundances,
or an established TOE. No repository theorem is needed to complete the
proof below. The earlier exploratory arguments are recoverable history,
not implicit physical premises.

## 1. Specified action and independent constants

Use signature \((-+++)\), \(c=1\), fields \(\phi=(u,x,y)\),
\(\alpha=\sqrt a\), \(A=e^{\alpha u}\), and \(g_J=A^2g\). Define
\[
\begin{split}
D&=1+\frac{2(1+b)}3(x^2+y^2),\\
K_b&=\operatorname{diag}\left(1,\frac{4b}{9D},\frac b{3D}\right),\\
V_0/H_v^2&=\frac32+
 \left(\frac b2-\alpha u+\frac{2a}b u^2\right)x^2
 +\frac b3y^2+\frac\nu2u^2,\\
V_1/H_v^2&=\left(\frac b2+\alpha b u+\frac{2a}b u^2\right)x^2
 +\frac b3y^2.
\end{split}
\]
The two couplings \(a,b\) are independent. All displayed parameters,
including \(a,b,H_v,\nu,\zeta\), are independent of the auxiliary variable
\(q\) in the unreduced variation. At \(b=a,\zeta=0\) these \(K_b,V_0,A\)
reduce to the earlier analytic-fluid functions. Recovering its local bulk
equations also uses \(C=0\) and a fixed \(q\) sector; auxiliary constraints
and boundary conditions remain separate in this action.

Let \(F_4=d{\cal A}_3,\widehat F_4=d\widehat{\cal A}_3\) be real
noncompact four-forms, with fixed positive auxiliary scales. Specify
\[
\begin{split}
S={}&\int\!{\rm vol}_g\,q
 \left[\frac R2-K_{b,AB}\partial\phi^A\!\cdot\!\partial\phi^B-2V_0\right]
 +\frac\zeta2\int\!{\rm vol}_J R_J\\
&+\zeta\int\!{\rm vol}_g
 \left[-K_{b,xx}(\partial x)^2-K_{b,yy}(\partial y)^2-2V_1\right]\\
&-\int\!{\rm vol}_g\,\Lambda A^4+\Gamma_m[A^2g,\psi]
 +\int\frac{\Lambda}{\mu_{\rm aux}^4}F_4
 +\int\frac{q^2}{2M_{\rm aux}^4}\widehat F_4 .
\end{split}
\]
The unreduced matter action is explicitly split as
\(\Gamma_m=-\int{\rm vol}_J\rho_{\rm vac}+\Gamma_m^{\rm dyn}\),
where \(\rho_{\rm vac}\) is constant and \(\Gamma_m^{\rm dyn}\) contains
only the dynamical matter. The constant part is included in \(C\) below.
The new \(\zeta\) transverse kinetic and potential operators are supplied
theory, reconstructed for the desired ideal history. No loop coefficient
or uniqueness/naturalness result is assumed. In particular \(b=0\) is not
an admitted kinetic metric; small-\(b\) statements mean limits through
positive values.

Vary the forms first to obtain constant \(q,\Lambda\) in a connected
sector. Write
\[
 s=\zeta/q,\quad z=sA^2,\quad F=1+z,\quad
 J=1+(1-3a)z,\quad C=(\Lambda+\rho_{\rm vac})/(2q),\quad
 W=V_0+sV_1+CA^4.
\]
After integration by parts, the Ricci coefficient is \(qF\); the kinetic
coefficients before the Einstein transformation are
\[
 Z_u=q-3a\zeta A^2,\qquad
 Z_x=(q+\zeta)K_{b,xx},\qquad Z_y=(q+\zeta)K_{b,yy}.
\]
Here \(Z_u\) by itself is not the physical Einstein kinetic coefficient.
For \(\widehat g=Fg\), the reduced action is
\[
 \int{\rm vol}_{\widehat g}\,q
 [\widehat R/2-\widehat K_{AB}\partial\phi^A\!\cdot\!\partial\phi^B
 -2\widehat V]+\Gamma_m^{\rm dyn}[B^2\widehat g,\psi],
\]
with
\[
 \widehat K_u=\frac J{F^2},\quad
 \widehat K_x=\frac{1+s}{F}\frac{4b}{9D},\quad
 \widehat K_y=\frac{1+s}{F}\frac b{3D},\quad
 \widehat V=\frac W{F^2},\quad B=\frac A{\sqrt F}.
\]
The Weyl contribution
\(3(\partial_u\log F)^2/4\), added to \(Z_u/(qF)\), gives \(J/F^2\)
exactly. Since \(D,F,J>0\) in the stated domain, all three entries are
positive. No lower bound uniform over unbounded field space is claimed.

## 2. Full equations and the meaning of a fixed sector

For Einstein proper time, let \(v^A=d\phi^A/d\widehat t\),
\(\sigma=\widehat\rho_m/(2q)\), \(r=\widehat\rho_r/(2q)\),
\(T=\widehat K_{AB}v^Av^B\), and
\(\alpha_B=\partial_u\log B=\alpha/F\). The full local ideal-fluid equations are
\[
\begin{split}
3\widehat H^2&=T+2(\widehat V+\sigma+r),&
\dot{\widehat H}&=-T-\sigma-\frac43r,\\
\dot v^A+3\widehat H v^A+\widehat\Gamma^A_{BC}v^Bv^C
 &=-\widehat K^{AB}(\widehat V_{,B}+\delta_{Bu}\alpha_B\sigma),\\
\dot\sigma&=(-3\widehat H+\alpha_Bv^u)\sigma,&
\dot r&=-4\widehat H r.
\end{split}
\]
Equivalently, \(\Pi_A=\widehat K_{AB}v^B\) obeys
\[
 \dot\Pi_A=-3\widehat H\Pi_A+
 \frac12\partial_A\widehat K_{BC}v^Bv^C-\widehat V_{,A}
 -\delta_{Au}\alpha_B\sigma .
\]
This second representation supplies an independent computational route.
The numerical \(N=\log\widehat a\) chart uses the positive root
\(\widehat H>0\) and \(3-\widehat K_{AB}\phi'^A\phi'^B>0\).
Finite integration in this chart is not a global existence theorem.

The original auxiliary variation is
\[
 {\cal L}_0=R/2-K_b(\partial\phi,\partial\phi)-2V_0,\qquad
 \widehat F_4=-M_{\rm aux}^4{\cal L}_0\,{\rm vol}_g/q,\qquad
 F_4=\mu_{\rm aux}^4 A^4{\rm vol}_g .
\]
It differentiates \(q{\cal L}_0+\zeta{\cal L}_1\) at fixed \(\zeta\),
not \(q({\cal L}_0+s{\cal L}_1)\) at fixed \(s\).
The latter derivative adds \(s{\cal L}_1\). Calibrating \(b=k\) in a
chosen sector does not authorize replacing \(b\) by a function of \(q\)
inside the unreduced action. The auxiliary boundary sector is an assumption,
not a solution of the observed vacuum-scale problem.

## 3. Exact ideal-fluid family

Supply \(C=3sH_v^2/2\) and use original-frame proper time and
\(N=\log a_g\). For arbitrary real \(x_0,y_0\), set
\[
\begin{split}
u&=0,\qquad x=x_0e^{-3N/2},\qquad y=y_0e^{-2N},\\
\rho_m&=2q(1+s)H_v^2x^2,\qquad
\rho_r=2q(1+s)H_v^2y^2,\qquad H=H_v\sqrt D .
\end{split}
\]
Since \(A=1,\dot u=0\), these are also Jordan physical densities,
clock and expansion. Write \(X=H_v^2x^2,Y=H_v^2y^2\). Direct differentiation gives
\[
\begin{split}
T_b&=b(X+4Y/3),&
W|_{u=0}&=(1+s)(3H_v^2/2+bX/2+bY/3),\\
\dot H&=-(1+b)(X+4Y/3),&
R&=12H_v^2+2(1+b)X.
\end{split}
\]
They satisfy both independent metric equations:
\[
3q(1+s)H^2=\rho_m+\rho_r+q(1+s)T_b+2qW,\qquad
-2q(1+s)\dot H=\rho_m+\frac43\rho_r+2q(1+s)T_b.
\]
The \(u\) equation is independent of these constraints. It reduces to
\[
 -2qW_u+\alpha\zeta R-\alpha\rho_m=0,\qquad
 W_u=\alpha[(sb-1)X+6sH_v^2].
\]
The constant terms cancel, and its remaining coefficient is
\(-2(sb-1)+2s(1+b)-2(1+s)=0\).

For the \(x,y\) equations, every kinetic and potential force term on this
orbit has the same overall factor \(q(1+s)\). With \(D_x=\partial_xD\),
\(D_y=\partial_yD\), their nonzero connection components are
\[
\begin{array}{lll}
\Gamma^x_{xx}=-D_x/(2D),&
\Gamma^x_{xy}=\Gamma^x_{yx}=-D_y/(2D),&
\Gamma^x_{yy}=3D_x/(8D),\\
\Gamma^y_{yy}=-D_y/(2D),&
\Gamma^y_{xy}=\Gamma^y_{yx}=-D_x/(2D),&
\Gamma^y_{xx}=2D_y/(3D).
\end{array}
\]
Their velocity contractions equal \(3x\dot H/2\) and \(2y\dot H\).
The ordinary accelerations are
\((9H^2/4-3\dot H/2)x\) and \((4H^2-2\dot H)y\).
The forces are \(9H^2x/4\) and \(2H^2y\), respectively.
Adding acceleration, connection, \(3H\) friction and force therefore
vanishes in each equation. This verifies the full field system rather
than only its energy constraint. Equivalently
\(K_{b,ij}\dot\phi^j=-[b/(1+b)]\partial_i(H_v\sqrt D)\) for \(i=x,y\).
The action's \(D\) is a field function, never an inserted evolving Hubble rate.

On this family
\[
 {\cal L}_0=3H_v^2+(1+b)X+\frac{2b}{3}Y .
\]
For a specified finite-volume boundary sector its flux ratio is the
volume average of this expression, since \(A=1\). A limiting future
ratio would require a separately specified regulator; the local theorem
does not assert finite absolute fluxes on an infinite history. A constant
shift \(\rho_{\rm vac}\mapsto\rho_{\rm vac}+\delta\),
\(\Lambda\mapsto\Lambda-\delta\) preserves \(C\) and the local equations
in the stipulated classical sector. It determines neither \(H_v\) nor a
quantum measure.

## 4. Explicit off-trajectory potential bound

The \(x^2\) coefficient in \(V_0+sV_1\) is
\[
 f_s(u)=\frac{b(1+s)}2+\alpha(sb-1)u+\frac{2a(1+s)}b u^2 .
\]
Completing the square gives
\[
\begin{split}
u_{\min}&=-\frac{b(sb-1)}{4\sqrt a(1+s)},\\
f_s(u)&=\frac{2a(1+s)}b(u-u_{\min})^2+
 \frac{b[3+(2-b)s][1+(2+b)s]}{8(1+s)}>0 .
\end{split}
\]
This is an all-real-\(u\) polynomial bound under the stated parameters.
The restoring coefficient \(2a/b\) can be large and is a new physical
choice, not inferred from the displayed history. The transformed
potential has a finite plateau along \(x=y=0,u\to+\infty\) when \(s>0\).
No earlier coercive/global-convergence proof is imported into this model.

## 5. Local stationary vacuum and physical time

At \(u=x=y=0\), \(C=3sH_v^2/2\),
\(\widehat V_{,A}=0\), and \(H_J=H_v\). The Hessian is diagonal. At a
stationary point its covariant and coordinate forms agree. Dividing by
\(\widehat K_A\) gives Einstein proper-time squared masses, then dividing
by \(B_0^2=1/(1+s)\) converts to physical time. The result is
\[
 \frac{(m_{u,J}^2,m_{x,J}^2,m_{y,J}^2)}{H_v^2}
 =\left(\frac{\nu(1+s)+12as}{1+(1-3a)s},\frac94,2\right).
\]
All entries are positive. These are local vacuum masses; fluid-background
mixing and gravitational/density perturbations are different calculations.
Positive masses alone do not certify the assumed long-range exchange in
an experiment.

## 6. Conditional local-gravity normalization

Freeze \(u=0\) during a local weak-body experiment, and supply a scalar
light on its measured length scale, universal unscreened coupling,
negligible self-gravity sensitivity and a valid locally frozen exchange
description. A canonically normalized dimensionless scalar has
\[
 \left(\frac{\partial\log B}{\partial\varphi}\right)^2
 =\frac{(\alpha/F)^2}{\widehat K_u}=\frac aJ .
\]
The stipulated tensor-plus-scalar exchange law therefore gives
\[
 k=\frac a{1+(1-3a)s},\qquad G_N=\frac{1+k}{8\pi q(1+s)}.
\]
Applying it during a fluid epoch additionally requires the local
wavenumber to exceed the relevant background mass/mixing and evolution
scales. This bridge is not a homogeneous equation or an apparatus model.
Eliminating \(q(1+s)\) in Section 3 yields the stated normalization identity.
\(S^2=(1+b)/(1+k)\) multiplies the fluid term in \(H_J^2\); the total
Hubble ratio also includes the supplied \(H_v\).

For the supplied diagnostic post-Newtonian formulas
\[
 \delta\gamma=-\frac{2k}{1+k},\quad
 \delta\beta=\frac{\beta_Dk}{2(1+k)^2},\quad
 \eta=4\delta\beta-\delta\gamma,\quad
 \beta_D=-\frac{a(1-3a)s(1+s)}{[1+(1-3a)s]^2},
\]
the parameterized zero-\(\eta\) family
\[
 s=\frac{1+k}{k(1-3k)},\qquad
 a=\frac{(1-k)(1+3k)}4,\qquad 0<k<1/3
\]
has \(\beta_D=-(1+k)\). These post-Newtonian response equations are
explicit imported diagnostic premises here, not a new nonlinear
post-Newtonian derivation. No observed Cassini/LLR likelihood is used.
On \(b=a\), \(S^2=(5-3k)/4\); on the independently calibrated \(b=k\),
\(S^2=1\). At \(k=10^{-5}\), the latter uses \(2a/b=50000.999985\).
An inverse target is admitted only if its computed \(b\) lies strictly
between zero and \(1/3\); the runner preserves all supplied target rows.

For ideal preannihilation photons, relativistic electron pairs and three
equal-temperature neutrino pairs, \(g_*=2+(7/8)(4+6)=43/4\). Expressing a
uniform fluid-rescaling as one ideal neutrino species gives
\(\Delta N_{\rm pre}=(43/7)(S^2-1)\). After the separately stipulated
instantaneous decoupling/annihilation entropy law,
\[
 c_\nu=\frac78(4/11)^{4/3},\qquad
 \Delta N_{\rm post}=(S^2-1)(c_\nu^{-1}+3).
\]
These are species-density arithmetic, not observations or one extra
neutrino population through a real transition. No nuclear reactions,
noninstantaneous neutrino transport, thermal scalar evolution or
primordial perturbations are checked by these ideal diagnostic rows.

## 7. Reproduction and scope of the numerical witness

Primary runner: `scripts/curvature_fluid_construction_2026_10_13.py`.
Its declared inputs are this note and the three JSON files under
outputs/curvature_fluid_construction_2026_10_13. It has no repository helper
runner. Synthetic fixtures supply 72 parameter tuples, 360 orbit and
operator-omission rows, 72 coefficient minima/Hessians, 12 diagnostic
families, 30 inverse targets, four full histories and 72 general finite-field
equation states. Exact symbolic residuals supplement the proof.

The original exploratory v1 values passed an independent action-based
recomputation, but three real source changes escaped its own assertions:
zero \(u\) acceleration, a missing \(u\)-metric derivative, and wrong-frame
stored masses. A separate v2 adds a symbolically differentiated
proper-time momentum oracle at nonzero field velocities and binds every
serialized physical mass to a rational parameter oracle. The original
failures and corrections remain recoverable. This canonical port preserves
the v2 physical functions; location, cache-input declarations and result
handling change for reproducibility.

Finite numerical agreement does not prove stability for arbitrary initial
states or independence from the supplied assumptions. The exact algebra
proves the constructive implication above. Selecting matter species,
preparing the ideal orbit, controlling inhomogeneous modes, deriving
couplings/vacuum scale, and testing independent measurements remain
physical obligations. Formal audit status is unset.
