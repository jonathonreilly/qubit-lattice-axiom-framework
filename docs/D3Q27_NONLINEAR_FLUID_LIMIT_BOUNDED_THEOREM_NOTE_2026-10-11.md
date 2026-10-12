---
claim_id: d3q27_nonlinear_fluid_limit_bounded_theorem_note_2026-10-11
claim_type: bounded_theorem
claim_scope: "For the supplied tuned D3Q27 collision and continuum-streaming model, prepared fluctuations of amplitude delta converge with explicit O(delta) Sobolev error to the specified nonlinear incompressible momentum and scalar equations on any supplied smooth lifetime. All five moment constraints, positive populations, and continuation of the kinetic solution are controlled."
upstream_dependencies:
  - d3q27_dissipative_hydrodynamic_approximation_bounded_theorem_note_2026-10-09
runner: scripts/d3q27_nonlinear_fluid_limit_2026_10_11.py
---

# A quantitative nonlinear fluid limit for the supplied D3Q27 model

**Date:** 2026-10-11

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. Independent retained-status audit has not occurred.

**Source baseline:** current main `a13caa4885f547c8d206265b031ba7649e539fd9`;
provisional transport parent `73a76d2141d30d75c6aebfb2f2f9baa6e0a025bf`.

**Runner:** [exact finite controls](../scripts/d3q27_nonlinear_fluid_limit_2026_10_11.py).

**Evidence cache:** `logs/runner-cache/d3q27_nonlinear_fluid_limit_2026_10_11.txt`.

This note proves an O(delta) comparison with nonlinear incompressible momentum
flow and an advected diffusive scalar, using fluctuation amplitude delta.
The previous linear-fluid result used a smaller amplitude. The proof below
retains quadratic convection and controls the singular kinetic scaling by
pairing nonlinear collision errors with the dissipative microscopic subspace.
It does not assume that the scalar has the same material-advection speed as
the momentum field: the finite model gives the coefficient 2/5.

The [hydrodynamic parent](D3Q27_DISSIPATIVE_HYDRODYNAMIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-10-09.md)
provides the finite collision kernel, projection, constitutive inverse and
quadratic moments. Its SHA-256 is
`038e1ed6942d79720aa1dd7360d90f9fa1067016940ceb3554efeb99c21ed0c1`.
It is a branch dependency, absent from the stated current-main baseline, and
has selective independent checks rather than an applied retained-status audit.
In particular, 2/5 and the quadratic stress formula are inherited identities;
the new argument is the complete corrector construction and uniform nonlinear
kinetic convergence. No physical carrier, collision rate or clock is selected.

## 1. Model and bilinear algebra

Use V={-1,0,1}^3, e=|v|^2, M_v=(2/3)^(3-e)(1/6)^e, and all 288
reversible four-distinct-velocity collisions ij <-> kl preserving v and e.
Let nu_r=e_k+e_l-e_i-e_j, W=diag(M), q_r=kappa_r M_i M_j,
B=W^-1 sum_r q_r nu_r nu_r^T. All rates are fixed and positive. Detailed balance gives M_i M_j=M_k M_l.
The parent proves rank 22 of the stoichiometric matrix, so the following five
invariants are the whole kernel. Let P be
the M-orthogonal projection onto K=span{1,v_x,v_y,v_z,e}, Q=I-P,
R=(B+P)^-1-P, and lambda>0 the least positive eigenvalue of B.

Define the real symmetric bilinear map

    Gamma(g,h) = W^-1 sum_r (q_r/2) nu_r
        (g_i h_j+g_j h_i-g_k h_l-g_l h_k).

Then for every pair of fields P Gamma(g,h)=0. For U in K,

    Gamma(U,U)=B(U^2/2).

The latter follows reaction by reaction from U_i+U_j=U_k+U_l, so
(U_k^2+U_l^2-U_i^2-U_j^2)/2=U_i U_j-U_k U_l. These identities hold
pointwise for spatially varying coefficients. No factorization of random
variables is involved.

The actual nonlinear kinetic equation for f=M(1+delta g) is exactly

    g_t + T g/delta + B g/delta^2 = Gamma(g,g)/delta,
    T=diag(v) dot grad_x,

on the normalized torus (R/2pi Z)^3. In population variables this is
f_t+delta^-1 T f=delta^-2 Q(f), with
Q(f)=sum_r kappa_r nu_r(f_i f_j-f_k f_l). This uses fluctuation amplitude delta,
unlike the earlier delta^3 limit. The collision law, streaming and clock
are supplied mathematical premises.

## 2. Explicit Sobolev constants

For integer s>=3 use the weighted Fourier norm
||g||_s^2=sum_k (1+|k|^2)^s sum_v M_v |g_hat_v(k)|^2.
Write m=min_v M_v=1/216 and S=sum_r q_r. The shell count
(2n+1)^3-(2n-1)^3=24n^2+2 gives

    sum_{k in Z^3}(1+|k|^2)^(-s)
       <= 1+26[1+1/(2s-3)] < 36.

Thus ||g_v||_infty <= E ||g||_s with E=6/sqrt(m).
Weighted Fourier convolution gives, for any scalar fields,

    ||ab||_{H^s} <= C_s ||a||_{H^s} ||b||_{H^s},
    C_s=6*2^s.

Indeed <k>^s <= 2^(s-1)(<l>^s+<k-l>^s), followed by Young's
convolution inequality and the preceding Fourier l1 bound, proves the claim.
This proof first applies to finite Fourier sums and then to their limits.

A deliberately conservative explicit bilinear bound is

    ||Gamma(g,h)||_s <= G_s ||g||_s ||h||_s,
    G_s=4 C_s S/m^(3/2).

For one reaction ||W^-1 nu||_M<=2/sqrt(m), and each scalar component
has H^s norm <=||g||_s/sqrt(m). Applying the scalar product bound to the
four products with the factor 1/2 proves the displayed constant by summation.
P, Q and B commute with Fourier differentiation and Sobolev weights.
Conservation therefore also gives exact H^s orthogonality
<e,Gamma(g,h)>_s=<Qe,Gamma(g,h)>_s.

## 3. Full correctors and fluid equations

Now use the parent's supplied isotropic rate
alpha=(-4579+3 sqrt(7614177))/1072 on its nine axial exchanges and unit
rates on the other reactions. The nine exchanges are
{s e_c-e_a,s e_c+e_a}<->{s e_c-e_b,s e_c+e_b}, where c is one coordinate,
a,b are the other two, s is -1,0,1, and e_a denotes a spatial unit vector.
The positive root satisfies 536 alpha^2+4579 alpha-22183=0 and alpha>1. Set nu=67/361 and D=4/49. Let real smooth
periodic fields rho,j,pi be given on [0,L], satisfying

    div j=0,
    j_t + (j dot grad)j + grad pi = nu Delta j,
    rho_t + (2/5) j dot grad rho = D Delta rho.

A sufficient regularity hypothesis, for the integer s>=3 chosen in Section 2,
is rho,j in C([0,L];H^(s+4)) intersect C^1([0,L];H^(s+2)) intersect
C^2([0,L];H^s). Pressure solves
-Delta pi=sum_ab partial_a partial_b(j_a j_b), with its mean fixed below.
The Fourier multiplier defining its mean-zero part is bounded in every
Sobolev space, so it has the regularity of j tensor j and the corresponding
time derivatives. A finite interval with these properties is supplied;
global 3D regularity is not asserted.
Take pi to have zero spatial mean, define A=(5-3e)/2 and

    U=rho A+3j dot v.
    H(r,J,E)=r A+3J dot v+(3/2)E(e-1).

H has moments (r,J,E), meaning sum_v M_v H=r,
sum_v M_v v H=J and sum_v M_v e H=E. In particular U has moments
(rho,j,0). The moments of TU are (div j,0,(5/3)div j), so PTU=0. The periodic mean of rho_t is zero because
div j=0. Define the local vector F1=(2/5)rho j-D grad rho, and set

    J1=F1-mean(F1),
    E1=3pi+|j|^2-mean(|j|^2),
    w=Q(U^2/2)-RTU+H(0,J1,E1),
    z=R[2 Gamma(U,w)-U_t-Tw].

The spatially constant subtraction in E1 fixes its mean and has no effect
on the corrector solvability. In particular w has zero spatially integrated
mass, momentum and energy, and z has zero moments pointwise.

All five components of P(U_t+Tw)=0 must be checked, not only its Leray
projection. The parent supplies the following complete moments of the
microscopic portion of w, with
D(j)=(grad j+grad j^T)/2-(div j)I/3:

    mass flux = 0,
    stress = j tensor j - (|j|^2/3)I - 2nu D(j),
    energy flux = -(2/3)rho j + (20/147)grad rho.

The first two come from the exact quadratic equilibrium stress and the
isotropic constitutive map. The energy flux follows because e v-(5/3)v
is microscopic, its quadratic moment is -(2/3)rho j, and the linear heat
flux is +(20/147)grad rho at E=0.

Adding H(0,J1,E1), the projected order-zero conditions are exactly

    rho_t+div J1=0,
    j_t+div[j tensor j-(|j|^2/3)I-2nu D(j)]+grad E1/3=0,
    (5/3)div J1+div[-(2/3)rho j+(20/147)grad rho]=0.

The first follows from div J1=(2/5)j dot grad rho-D Delta rho=-rho_t.
The second is the supplied momentum
equation, including the pressure correction and div j=0. The third is
-(5/3)[rho_t+(2/5)j dot grad rho-D Delta rho]=0. Hence

    BU=0,
    TU+Bw-Gamma(U,U)=0,
    U_t+Tw+Bz-2Gamma(U,w)=0.

The last equality uses both full projected compatibility and BR=Q.
Let G_delta=U+delta w+delta^2 z. Its full nonlinear residual is exactly

    Res_delta = delta R1 + delta^2 R2 + delta^3 R3,
    R1=w_t+Tz-2Gamma(U,z)-Gamma(w,w),
    R2=z_t-2Gamma(w,z),
    R3=-Gamma(z,z).

No asymptotic term has been discarded. The displayed regularity gives w in C H^(s+3), w_t in C H^(s+1),
z in C H^(s+2), and z_t in C H^s. For the last assertion, differentiate
z to obtain R[2 Gamma(U_t,w)+2 Gamma(U,w_t)-U_tt-Tw_t].
Thus all residual terms belong continuously to H^s. Denote

    K0=sup_{[0,L]}(||U||_s+||w||_s+||z||_s),
    S0=sup_{[0,L]}(||R1||_s+||R2||_s+||R3||_s).

For 0<delta<=1, ||G_delta||_s<=K0 and ||Res_delta||_s<=delta S0.

## 4. Uniform stability and existence

Suppose a real initial family satisfies
||g_delta(0)-G_delta(0)||_s<=I0 delta with I0 independent of delta.
The simple preparation g_delta(0)=U(0) is allowed with
I0=||w(0)||_s+||z(0)||_s. Put

    a0=G_s^2(2K0+1)^2/(2lambda),
    C0=exp(a0 L)(I0+L S0).

Assume 0<delta<=1, delta C0<=1/2, and
delta E(K0+1)<=1/2. Then the nonlinear kinetic initial-value problem
has a unique solution in C([0,L],H_M^s) intersect C^1([0,L],H_M^(s-1)),
and

    sup_{t<=L} ||g_delta(t)-G_delta(t)||_s <= C0 delta,
    sup_{t<=L} ||g_delta(t)-U(t)||_s
       <= delta[C0+sup||w||_s+sup||z||_s].

Moreover f_delta,v=M_v(1+delta g_delta,v)>=M_v/2 throughout the interval.

Proof. The Fourier generator -i diag(v dot k)/delta-B/delta^2 is
dissipative in every H_M^s. Its exponential defines a contractive C0
semigroup. Gamma is locally Lipschitz in H_M^s by the proved product
estimate, so the usual Picard contraction on the integral equation gives
a unique local mild solution and continuation while its H^s norm remains
bounded. This can also be established directly by successive approximation
on a ball, using T<=c delta/[G_s(1+||g(0)||_s)] for the initial interval;
there is no assertion that this local construction alone is uniform in delta.

Set e=g_delta-G_delta and y=||e||_s^2. For the local solution, with the energy justification below,

    (1/2)y' + (lambda/delta^2)||Qe||_s^2
      <= (G_s/delta)||Qe||_s(2||G_delta||_s+||e||_s)||e||_s
         + ||e||_s ||Res_delta||_s.

Streaming is skew-adjoint. Every collision error is microscopic because
P Gamma=0. While ||e||_s<=1, Young's inequality absorbs half the
microscopic dissipation and leaves

    (1/2)y' + (lambda/(2delta^2))||Qe||_s^2
       <= a0 y + delta S0 sqrt(y).

There is no 1/delta in a0. Applying the scalar inequality to
sqrt(y+eta^2) and then sending eta to zero gives

    ||e(t)||_s <= exp(a0 t)(||e(0)||_s+delta S0 t)
               <= C0 delta <= 1/2.

Continuity prevents exit from the bootstrap ball. The H^s norm stays
bounded by K0+1, so successive local continuations reach L. The energy calculation is justified directly by applying a finite Fourier
projection to the mild error equation. Each retained Fourier mode is C^1
in time; the streaming term cancels in the finite energy identity. The
projections of e and its H^s-continuous forcing converge uniformly on
every compact local time interval, so the integrated energy identity passes
to the limit. No extra spatial derivative is needed for this step.
At a putative finite maximal time, the bounded H^s nonlinearity is Bochner
integrable. The mild formula therefore has an H^s endpoint limit, to which
the same local Picard argument applies. This establishes continuation, not
just a formal bootstrap. Finally T:H^s->H^(s-1) and the equation give
the stated C^1 H^(s-1) regularity. The Fourier embedding and smallness condition give positivity.
Uniqueness follows from the same local Lipschitz integral equation.

Important limit: this theorem compares with an explicitly supplied smooth
solution of the displayed nonlinear system. It does not assert global
existence, unsuppressed acoustic convergence, physical entropy identification,
or a finite-particle/mesh limit. Those are separate obligations.

## 5. Prior art, evidence and open interfaces

Current-main searches for incompressible/Navier-Stokes/nonlinear fluid found
the lane map but no matching supplied-model nonlinear convergence theorem.
The search record and exact read coverage are retained in the campaign pack.
This is a repository-local comparison, not a claim of novelty of the general
mathematical method. Bellouquid's 2002 paper
[The Incompressible Navier-Stokes for the Nonlinear Discrete Velocity Models](https://arxiv.org/abs/nlin/0306036)
provides established context for discrete-velocity fluid limits. Its Euclidean
domain and preparation hypotheses are not imported as a certificate for this
quantitative periodic theorem. Sections 1–4 supply the argument used here.

| Proof obligation | Evidence and limitation |
|---|---|
| Collision kernel and positive microscopic gap | Linked finite proof and fresh exact finite reconstruction |
| Quadratic equilibrium identity and complete moments | Reactionwise proof and exact polynomial checks |
| Tuned constitutive inverse | Linked proof and full 27-component exact-number-field Poisson checks |
| Full pressure, mass and energy compatibility | Section 3; no Leray-only solvability shortcut |
| Residual powers and multiplicities | Exact expansion and direct nonconstant Fourier/time-jet controls |
| Product, dissipation and stability bounds | Analytic proofs in Sections 2 and 4; finite sampling is not their proof |
| Kinetic existence, continuation and positivity | Section 4, for the displayed initial preparation and small delta |
| Smooth macroscopic lifetime | Explicit input; global 3D existence remains outside the theorem |
| Particle, spatial-grid and quantum composition at this amplitude | Separate downstream obligations |
| Native carrier, dynamics, clock and physical identification | Open physical interfaces, not new axioms |

The primary runner's finite controls must be read with their actual coverage:
the tuned rate is checked through the eight complete Poisson sources; the
nonconstant advected-shear/thermal residual uses rational unit axial rate,
for which that particular off-diagonal-strain solution has the same coefficients.
That finite example does not test an arbitrary nonlinear solution. The analytic
proof gives the theorem for the tuned rate and the declared smooth solutions.
Deliberate failures exercise omitted pressure correction, the wrong thermal
advection coefficient, and a missing quadratic residual term. The source-bound
independent review in the campaign pack records which arguments and final
bytes were checked; no independent audit or Lean execution is inferred.

Useful scoped Lean targets are the five-invariant reaction identities, weighted
projection/inverse identities, complete moment contractions, exact residual,
and the abstract microscopic energy estimate with its semigroup hypotheses.
Formalization can strengthen the mathematical audit. It is not evidence for a
physical identification, and is not a prerequisite to investigating new proofs.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Compose microscopic spatial dynamics with controlled nonlinear macroscopic transport."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Control finite-particle and spatial-grid errors at amplitude delta, then test native dynamics and readout."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Quantitative conditional nonlinear fluid limit with full correctors and a uniform Sobolev stability bound."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
