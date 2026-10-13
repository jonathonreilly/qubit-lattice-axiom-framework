---
title: A conditional weak-scalar expansion and fast curvature coefficient
claim_id: weak-scalar-limit-bounded-theorem-note-2026-10-13
date: 2026-10-13
---

# A conditional weak-scalar expansion and fast curvature coefficient

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
next_trace_action: Establish bounds for finite-coupling solutions and test the physical identification.
conditional_surface_status: Conditional on the specified classical action, positive fluid density and bounded scaled states.
hypothetical_axiom_status: The scalar metric, potential, universal matter coupling and normalization are supplied candidate theory.
admitted_observation_status: Observed expansion and local gravity motivate the question; this theorem contains no fitted data or empirical acceptance.
claim_type_reason: Uniform coefficient expansions on fixed compact sets and their conditional instantaneous consequences.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Statement and scope

Can an additional scalar sector have a small effect on expansion while its
internal dynamics remain rapid? The specified classical candidate below
provides an explicit conditional calculation. It is motivated by reconstructed
cosmic histories; neither those numerical histories nor any repository theorem
is a premise here. For fixed positive constants \(H_v,Q_0,\rho_{\rm unit},\nu\),
take \(0<k<1/3\) tending to zero. On every fixed compact set of
\((v,w,x,y,p_x,p_y,\rho_J,P_J)\), with \(\rho_J\geq0\), put
\(u=k^2v,p_u=kw\). Dimensionless \(\rho_J,P_J\) are measured in the
supplied unit \(\rho_{\rm unit}\). The expansions in Sections 2–3 are
uniform on that set. They are statements about coefficients and instantaneous
states, not existence or convergence of a family of solutions.

The corresponding expansion of the physical Hubble constraint is
\[
 \frac{H_J^2}{H_v^2H_{\rm GR}^2}=1+kC_1+O(k^2),\qquad
 C_1=\frac{2(\bar V-\sigma_0)}{3H_{\rm GR}^2}
      +\frac{\bar T}{3},\qquad H_{\rm GR}^2=1+\frac{2\sigma_0}{3},
\]
where \(\sigma_0=R_0\rho_J\), \(R_0=\rho_{\rm unit}/(2Q_0H_v^2)\),
\(\bar V=x^2/2+y^2/3\),
\(\bar T=4p_x^2/(9D_0)+p_y^2/(3D_0)\), and
\(D_0=1+2(x^2+y^2)/3\). At an ideal matched instantaneous state
\(\sigma_0=x^2+y^2,p_x=-3x/2,p_y=-2y\), \(C_1=0\).
This cancellation is not imposed on general thermal states.

No quantum limit, uniform history error, initial-state selection, stability
of the complete coupled perturbation spectrum, empirical validation or TOE
is established. In particular no failed stiff integration is replaced by
the coefficient limit. Positive classical kinetic coefficients vanish as
\(k\to0\); the endpoint is not an admitted nondegenerate scalar action.

## 1. Complete supplied action and physical readout

Use signature \((-+++)\), \(c=1\), \(\phi=(u,x,y)\),
\(a=(1-k)(1+3k)/4\), \(\alpha=\sqrt a\),
\(s=(1+k)/[k(1-3k)]\), \(E=e^{2\alpha u}\),
\(F=1+sE\), \(J=1+(1-3a)sE\), and
\(D=1+2(1+k)(x^2+y^2)/3\). Specify
\[
 K=\mathop{\rm diag}\left(\frac J{F^2},
 \frac{1+s}{F}\frac{4k}{9D},\frac{1+s}{F}\frac{k}{3D}\right),
 \quad C_B=\frac{(1+s)E}{F},\quad \alpha_B=\frac\alpha F.
\]
Set
\[
\begin{split}
 V_0&=\frac32+(k/2-\alpha u+2au^2/k)x^2+ky^2/3+\nu u^2/2,\\
 V_1&=(k/2+\alpha ku+2au^2/k)x^2+ky^2/3,\\
 U&=\frac{(1+s)[V_0+sV_1+3sE^2/2]}{F^2}.
\end{split}
\]
The complete local candidate is
\[
 S=Q(k)\int\!\sqrt{-\widehat g}\,
 [\widehat R/2-K_{AB}\partial\phi^A\cdot\partial\phi^B-2H_v^2U]
 +S_m[C_B\widehat g,\psi],\qquad Q(k)=Q_0(1+k).
\]
The constant vacuum contribution is the explicit potential constant; the
fluid stress tensor contains dynamical matter. The functions and normalization
are assumptions. No ultraviolet or auxiliary-boundary derivation is needed
or claimed for this local action. All three entries of \(K\) are positive
for finite fields in this parameter range because \(a<1/3\) and \(F,J,D>0\).

On a flat homogeneous expanding background write \(N=\log\widehat a\),
\(p_A=d\phi_A/dN\), \(T=K_{AB}p_Ap_B\), and
\(R=R_0/(1+k)\). In the region \(T<3\), the constraint and readout are
\[
 \frac{\widehat H^2}{H_v^2}=\frac{2[U+C_B^2R\rho_J]}{3-T},\quad
 N_J'=1+\alpha_Bp_u,\quad
 \frac{H_J^2}{H_v^2}=\frac{\widehat H^2}{H_v^2}\frac{(N_J')^2}{C_B}.
\]
They follow from the action and \(g_J=C_B\widehat g\).
On a bounded scaled-state set, \(T=O(k)\), so \(T<3\) for sufficiently
small positive \(k\); \(N_J'>0\) then also follows. For the separately
supplied massless local weak-body exchange approximation, define
\(G_N/G_{\rm ref}=C_B(1+\alpha_B^2/K_u)/(1+k)\),
\(G_{\rm ref}=1/(8\pi Q_0)\). This approximation does not establish
environmental matching or scalar range for an actual apparatus.

## 2. Weighted coefficient expansion and proof

The following exact rewrite makes the limit regular. Put
\(d=k(1-3k)\), \(f=d+(1+k)E\); then \(d+1+k=4a\),
\[
 K_u=\frac{d[d+(1-3a)(1+k)E]}{f^2},\quad
 K_x=\frac{16ak}{9fD},\quad K_y=\frac{4ak}{3fD},\quad
 \alpha_B=\frac{\alpha d}{f},\quad C_B=\frac{4aE}{f},
\]
and \(U=4aS/f^2\), where
\[
 S=\frac32[d+(1+k)E^2]+2akx^2+4\alpha k^2ux^2
   +8a^2u^2x^2/k+\frac{4ak}{3}y^2+\frac{\nu d}{2}u^2.
\]
For \(u=k^2v\), \(E=1+k^2v+O(k^3)\),
\(f=4a+(1+k)(E-1)\), with denominators bounded away from zero
uniformly on each fixed compact set for small enough \(k\). Direct
substitution and differentiation give
\[
\begin{gathered}
 K_u/k=1/4+O(k),\quad K_x/k=4/(9D_0)+O(k),\quad
 K_y/k=1/(3D_0)+O(k),\\
 U=3/2+k\bar V+O(k^3),\quad
 \alpha_B/k=1/2+O(k),\quad C_B=1+O(k^3),\\
 U_u/k=vx^2-x^2-2y^2/3+O(k),\qquad kU_{uu}=x^2+O(k).
\end{gathered}
\]
For clarity, \(U(0,x,y)=3/2+k\bar V\) is exact. The derivative
\(U_u=O(k)\) throughout \(u=k^2v\), so its integral from zero is
\(O(k^3)\). The term \(8a^2u^2x^2/k\) in \(S\) supplies the
leading \(vx^2\) derivative and \(x^2/k\) curvature. Taking derivatives
before setting \(u=0\) is essential. These regular expansions prove the
stated uniformity; they are not uniform on unbounded field sets or on time
intervals that grow with \(1/k\).

## 3. Physical constraint and its first correction

The kinetic expression is \(T=k\bar T+O(k^2)\); its \(u\) contribution
is \(O(k^3)\). The non-vacuum scalar energy is consequently \(O(k)\),
while \(U\) retains \(3/2\). Also
\(C_B^2R\rho_J=\sigma_0(1-k)+O(k^2)\),
\(N_J'=1+O(k^2)\). Expanding the constraint yields
\[
 \frac{H_J^2}{H_v^2}
 =H_{\rm GR}^2+k\left[\frac{2(\bar V-\sigma_0)}3
                  +\frac{H_{\rm GR}^2\bar T}{3}\right]+O(k^2),
\]
which proves \(C_1\). For the matched ideal state,
\(H_{\rm GR}^2=D_0\),
\(\bar T=(x^2+4y^2/3)/D_0\), and
\(2(\bar V-\sigma_0)=-x^2-4y^2/3\); cancellation follows exactly.
The conditional local readout also gives \(G_N/G_{\rm ref}\to1\).
None of these statements assumes a completed finite-\(k\) trajectory.

## 4. Transverse equations and the fast coefficient

If a sufficiently regular transverse solution limit exists with the bounded
scaled states above, and \(\rho_J,P_J\) converge uniformly on the fixed
interval to the limiting matter coefficients used below, its equations in
\(N_J\) use
\(\bar g=\operatorname{diag}(4/(9D_0),1/(3D_0))\):
\[
 \phi_i'=p_i,\quad p_i'=-(3+h_{\rm GR})p_i
       -[C_i+\bar V_{,i}/H_{\rm GR}^2]/\bar g_i,\quad
 h_{\rm GR}=-R_0(\rho_J+P_J)/H_{\rm GR}^2,
\]
where
\(C_i=p_i\sum_j\partial_j\bar g_i\,p_j
-\tfrac12\sum_j\partial_i\bar g_j\,p_j^2\).
In particular
\[
 \frac{C_x}{\bar g_x}=\frac{-2xp_x^2-4yp_xp_y+3xp_y^2/2}{3D_0},\quad
 \frac{C_y}{\bar g_y}=\frac{-4xp_xp_y-2yp_y^2+8yp_x^2/3}{3D_0}.
\]
This follows by dividing the transverse field equations by \(k\);
the terms proportional to \(p_u\) vanish. The limiting metric is curved.
At \(x\ne0\), the positive potential-curvature contribution obeys
\[
 \frac{U_{uu}}{K_u(\widehat H^2/H_v^2)}
 \sim\frac{4x^2}{k^2H_{\rm GR}^2}.
\]
It is not a full coupled eigenvalue. The kinematic family
\(u=k^2\sin(N/k)\) has \(p_u=k\cos(N/k)\) but
\(p_u'=-\sin(N/k)\). Thus the admitted amplitude scaling permits
\(K_up_u'=O(k)\), the force order. This example concerns the scaling
assumption alone; it is not asserted to solve the cosmological equations.
At \(x=0\) the displayed leading curvature vanishes.

## Reproduction and limits of evidence

Primary runner: `scripts/weak_scalar_limit_2026_10_13.py`.

Run `python3 scripts/weak_scalar_limit_2026_10_13.py`. It checks exact
algebra, compact/original action agreement at frozen numerical points,
the leading physical correction, curved connections and their omission
controls. Numerical controls support the proof; they are not physical
experiments or a convergence theorem. `outputs/weak_scalar_limit_2026_10_13/imports.json`
records all assumptions and the absence of measured inputs. All runtime
inputs are declared by the runner. No ODE, observational covariance or
likelihood is used by this canonical unit. Exploratory thermal histories,
distance comparisons and failed solver routes remain separately archived.
