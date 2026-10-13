---
title: Analytic scalar geometry for a supplied dust and radiation history
claim_id: analytic-fluid-cosmology-construction-bounded-theorem-note-2026-10-13
date: 2026-10-13
---

# Analytic scalar geometry for a supplied dust and radiation history

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
next_trace_action: Test the supplied action against matter, perturbation and quantum observables with preparation and readout specified.
conditional_surface_status: The result is conditional on the displayed classical action and homogeneous ideal-fluid domain.
hypothetical_axiom_status: New candidate physical assumptions are explicit and are not adopted framework primitives.
admitted_observation_status: One previously exposed numerical benchmark supplies initial amplitudes; there is no independent observation test.
claim_type_reason: An explicit construction and proof hold on a specified model and domain.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target and imports

For every fixed \(a,\nu,H_v>0\), the three-field model below has analytic
positive scalar geometry, admits the displayed exact family with arbitrary
supplied dust/radiation amplitudes, and every finite-energy flat homogeneous
Einstein-expanding state with nonnegative fluid densities has a global future
proper-time solution converging to its unique vacuum, with

\[
 (u,x,y,\dot u,\dot x,\dot y,\sigma,r)\longrightarrow0,\qquad
 H\longrightarrow H_v,\quad A\longrightarrow1,\quad H_J\longrightarrow H_v.
\]

This is the precise implication proved here. The action, universal conformal
matter coupling, classical Einstein gravity, flat homogeneity, ideal fluids
and positive parameters are supplied candidate assumptions. In particular,
\(H_v\) is a supplied scale. Their physical identification remains a research
question. The proof uses smooth finite-dimensional ODE continuation and the
invariant-set argument given below. It has no load-bearing repository theorem
dependency and proposes no change to the premise registry.

The numerical example uses \(H_0=1,m=0.3,
\Omega=5.046740289227271\times10^{-5}\). These are supplied dimensionless
inputs. The radiation number came from an already exposed photons-only
calibration in the exploratory campaign; this note neither recalibrates it
nor asserts a temperature likelihood. The theorem accepts arbitrary real
amplitudes, including zero, independently of that example. Measured gravity,
particle content, neutrino abundance, entropy, primordial initial states and
the observed small vacuum scale are not outputs of this construction.

## Specified action and equations

Use signature \((-+++)\), \(G_*>0\), and the Einstein-frame action

\[
 S={1\over16\pi G_*}\int\sqrt{-g}\,
 [R-2K_{AB}(\phi)\partial\phi^A\!\cdot\!\partial\phi^B-4V(\phi)]
 +S_m[A(\phi)^2g],\qquad\phi=(u,x,y).
\]

The matter metric is \(g_J=A^2g\). Define

\[
 \begin{split}
 A&=e^{\sqrt a\,u},\qquad D=1+{2(1+a)\over3}(x^2+y^2),\\
 K&=\operatorname{diag}\left(1,{4a\over9D},{a\over3D}\right),\\
 V&=H_v^2\left[{3\over2}+f(u)x^2+{a\over3}y^2+{\nu\over2}u^2\right],\\
 f(u)&={a\over2}-\sqrt a\,u+2u^2
      =2\left(u-{\sqrt a\over4}\right)^2+{3a\over8}.
 \end{split}
\]

These functions are real analytic at every finite real field value and \(K\)
is positive definite there. Its two nontrivial components describe a curved
field metric. No uniform lower eigenvalue over unbounded field space is used.
The third field, curved metric and freely chosen restoring coefficient are
explicit new ingredients.

Let \(t\) be Einstein proper time, \(b(t)>0\) its scale factor,
\(H=\dot b/b>0\), \(v^A=\dot\phi^A\), and
\(\sigma=4\pi G_*\rho_m,r=4\pi G_*\rho_r\). These are Einstein-frame
mass-equivalent densities. With \(T=K_{AB}v^Av^B\), the full homogeneous
system is

\[
 \begin{split}
 3H^2&=2(\sigma+r+V)+T,\\
 D_tv^A+3Hv^A+K^{AB}(V_B+\alpha_B\sigma)&=0,
       \qquad\alpha=(\sqrt a,0,0),\\
 \dot\sigma&=(-3H+\sqrt a\,\dot u)\sigma,\qquad\dot r=-4Hr,\\
 \dot H&=-T-\sigma-{4r\over3}.
 \end{split}
\]

The positive constraint root defines \(H\) on the autonomous state space.
Nonnegative \(\sigma,r\) and their zero-density boundaries are invariant.
Radiation's zero trace gives no direct \(u\) source. Both the scalar dust
force and the dust mass exchange are included.

## Exact supplied-fluid family

For \(N=\log b\) and arbitrary real \(x_0,y_0\), define

\[
 u=0,\quad x=x_0e^{-3N/2},\quad y=y_0e^{-2N},\quad
 \sigma=H_v^2x^2,\quad r=H_v^2y^2,\quad H=H_v\sqrt D.
\]

Here \(A=1\), so the two clocks and scale factors agree. Conservation holds,
and direct substitution gives

\[
 T=a(\sigma+4r/3),\quad V={3H_v^2\over2}+{a\sigma\over2}+{ar\over3},
 \qquad\dot H=-(1+a)(\sigma+4r/3).
\]

These establish Friedmann and Raychaudhuri. The \(u\) equation holds because
\(V_u=-\sqrt a\,\sigma\) cancels its dust source and all \(u\) connections
vanish. To check the other two scalar equations individually, write
\(\bar H=H_v\sqrt D,\eta=a/(1+a)\). Lower the proposed velocity with \(K\):

\[
 v_i=-\eta\partial_i\bar H,\qquad
 D_tv_i=-\eta\operatorname{Hess}(\bar H)_{ij}v^j,\qquad i=x,y.
\]

For \(P=T/2\) evaluated on this velocity field, metric compatibility and
Hessian symmetry give
\(\partial_iP=-\eta\operatorname{Hess}(\bar H)_{ij}v^j=D_tv_i\).
On \(u=0\), \(P+V=3\bar H^2/2-H_v^2(x^2+y^2)\). Thus

\[
 D_tv_i+3\bar Hv_i+\partial_iV
 =3(1-\eta)\bar H\partial_i\bar H-\partial_i[H_v^2(x^2+y^2)]=0.
\]

This verifies every scalar equation as well as the total energy relation.
Off this orbit the metric remains the declared function \(D(x,y)\); it is
never defined using the actual Hubble rate.

For supplied \(H_0>0,m,\Omega\geq0,m+\Omega<1\), choosing

\[
 H_v^2=H_0^2(1-m-\Omega),\quad
 x_0^2={3m\over2(1+a)(1-m-\Omega)},\quad
 y_0^2={3\Omega\over2(1+a)(1-m-\Omega)}
\]

gives \(H^2/H_0^2=me^{-3N}+\Omega e^{-4N}+1-m-\Omega\).
These amplitudes are initial data set by the supplied inputs. Either sign
is allowed, including zero, and \(\nu\) is free on the exact orbit.

## Global homogeneous future existence and convergence

For an arbitrary state in the stated domain, define
\(E=T/2+V+\sigma+r=3H^2/2\). The scalar equation gives
\(\dot T/2=-3HT-v^AV_A-\sqrt a\,\sigma\dot u\). Its last term cancels
the dust mass change, so

\[
 \dot E=-3H(T+\sigma+4r/3)\leq0.
\]

The potential obeys

\[
 V\geq {3H_v^2\over2}+{3aH_v^2\over8}x^2
               +{aH_v^2\over3}y^2+{\nu H_v^2\over2}u^2.
\]

For every finite initial energy this bounds all fields on a compact set.
The continuous positive metric has a positive minimum eigenvalue on that
set. Hence \(T\leq2E\) bounds all velocities, and the nonnegative densities
are bounded too. The smooth positive-root vector field has
\(H_v\leq H\leq\sqrt{2E(0)/3}\) and is regular on this invariant compact
sublevel, including either zero-density boundary. ODE continuation supplies
a solution for every future finite \(t\). This proof uses the densities
themselves, without a logarithmic coordinate singularity at zero.

The invariant-set step is explicit. A bounded future orbit has a nonempty
compact omega-limit set. Monotone continuous \(E\) has a limit and is
constant along its invariant omega-limit trajectories. Therefore \(\dot E=0\)
there. All summands are nonnegative and \(H>0\), giving
\(v=0,\sigma=r=0\). Invariance of \(v=0\) also requires \(\nabla V=0\).
The equations \(V_x=2H_v^2f(u)x,V_y=2aH_v^2y/3\) give \(x=y=0\);
then \(V_u=\nu H_v^2u=0\) gives \(u=0\). The omega-limit set is the
single vacuum, and precompactness gives convergence of the whole orbit.
This proves the target's global homogeneous conclusion.

Physical proper time obeys \(dt_J=A\,dt\), with
\(H_J=A^{-1}(H+\sqrt a\,\dot u)\). Bounded \(u\) bounds \(A\) above and
away from zero, so \(t_J\to\infty\). The already proved limits give
\(A\to1,H_J\to H_v\). This concerns homogeneous proper time, without
asserting a result about general inhomogeneous geodesics.

## Free scalar modes and a frame witness

At the vacuum the canonical squared masses are \(H_v^2(\nu,9/4,2)\).
In the free scalar sector, with fluid perturbations set to zero,

\[
\begin{array}{ll}
u,\ \nu\ne9/4:&C_1e^{[-3+\sqrt{9-4\nu}]H_vt/2}
                    +C_2e^{[-3-\sqrt{9-4\nu}]H_vt/2},\\
u,\ \nu=9/4:&(C_1+C_2t)e^{-3H_vt/2},\\
x:&(C_1+C_2t)e^{-3H_vt/2},\\
y:&C_3e^{-H_vt}+C_4e^{-2H_vt}.
\end{array}
\]

For \(\nu>9/4\), use the equivalent real sine/cosine pair. The critical
polynomial factor is retained. The exact \(y\) trajectory uses the
\(e^{-2H_vt}\) solution; both independent solutions are displayed.

The admissible state \(a=\nu=H_v=1\), all fields and fluids zero, and
velocity \((\dot u,\dot x,\dot y)=(-3,0,0)\) has \(T=9,V=3/2,H=2\)
and \(H_J=-1\). It is a finite-energy state in the theorem's
Einstein-expanding domain. The convergence proof includes its future
evolution without requiring intermediate physical-frame expansion.

## Proof obligations and scope

The proof chain is positive analytic geometry and coercivity; all exact
background equations; full off-orbit energy cancellation; compact invariant
sublevels and continuation; the unique invariant zero-dissipation state;
and physical-clock convergence. Each step is proved above. Finite numerical
checks support the implementation, not the infinite-time proof itself.

The strict inequalities \(a,\nu,H_v>0\) are hypotheses; no uniform theorem
at their zero limits is supplied. All finite real field values and velocities
and both zero-fluid boundaries are included. The exact-amplitude family and
future convergence are separate positive conclusions. A probability law for
initial amplitudes, attraction to a particular finite history, inhomogeneous
evolution and quantum corrections have no proof in this note. The strongest
next physical obligation is to supply and test the matter and initial-state
identification of the action. No impossibility theorem for those extensions
is asserted.

## Relation to existing source

The supplied dust/radiation/constant-vacuum expansion curve and its late-time
de Sitter limit already appear in current-main
`COSMOLOGY_FRW_KINEMATIC_REDUCTION_THEOREM_NOTE_2026-04-24.md`, notably
section 5. This note does not claim discovery of that curve or its endpoint.
Its proposed contribution is the specified curved three-field action and
the proof for all finite-energy homogeneous Einstein-expanding initial
states of that nonlinear model, including states off the exact trajectory.
The earlier note is contextual comparison, not a premise of the proof, and
its historical status language is not adopted here. No literature-wide
novelty claim is made.

## Computation and reproduction

Primary runner: `scripts/analytic_fluid_cosmology_2026_10_13.py`.
Its numerical input is
`outputs/analytic_fluid_cosmology_2026_10_13/fixtures.json`.
The note and import/scope record are declared package integrity inputs.
No other repository scientific result is read at runtime.

The runner preserves the exploratory equations and fixtures. It computes
the connection and background equations symbolically, compares full
off-orbit forces and conservation with a separately implemented momentum
form, differentiates the actual metric and potential, checks free modes
against matrix exponentials, integrates the tracking equations at two
refinements, and compares disturbed histories in e-fold and proper-time
coordinates. A separate numerical review uses canonical-momentum Radau
evolution and independent derivatives and modes. These are internal checks
with shared model premises, not independent measurements.

Canonical execution, mutation results and final source review are recorded
in the branch-local review history. The paired cache is generated through
`scripts/runner_cache.py:execute_and_write_cache`. Run the primary directly
for concise results, or use `--output-json` to retain full rows. Every
scientific conclusion keeps the conditional scope above.

## Review record and preserved exploratory scope

This self-contained constructive unit comes from exploratory
`direct_analytic_fluid_completion`. The original v1 omitted the critical
\(\nu=9/4\) mode and did not make the frame qualification sufficiently
explicit. Both were corrected before the first parent execution. Original
sources, failed reviewer checks and corrections remain in the complete
recovery archive in the branch-local pack. The free-mode basis and frame
witness above keep the relevant mathematics in active source.

The exploratory unit also asserted a broader negative history-selection
conclusion. That assertion is explicitly deferred, with its evidence and
pending five-family publication requirement preserved in the recovery
record. It is not part of this target or a theorem imported through the
archive. The older combined cosmology packet remains separately pending.
This unit neither clears that obligation nor changes its evidence.
Formal audit status remains unset. Independent source review and mechanical
validation are separate records; no merge is proposed by this author run.
