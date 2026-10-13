# Auxiliary vacuum-shift completion of the analytic candidate

Parent derivation before execution, 2026-10-13. This is a new campaign
candidate, motivated by the measured-matter vacuum calculation. It imports
the idea of auxiliary four-form constraints from the cited sequestering
literature, but changes the action and makes its own narrower claims. No
claim of historical novelty, measured four-form physics or a derived
cosmological constant is made.

## Minimal premises and explicit new assumptions

Keep the analytic three-field functions K,V,A and positive a,nu,H_v of
direct_analytic_fluid_completion. In natural units define
L0=R/2-K_AB partial(phi^A).partial(phi^B)-2V.
The matter effective action is Jordan-covariant and its constant vacuum
piece is -rho integral A^4 vol_g. It has no internal graviton or cosmological
scalar loops in the present treatment. Induced curvature and higher
derivative operators are excluded from the displayed classical model.

NEW assumptions: add real fields q(x)>0 and Lambda(x), and two real,
noncompact auxiliary three-form gauge potentials B3 and Bhat3 with
F=dB3,Fhat=dBhat3. No compact flux quantization is imposed. Fix the flux
sector/boundary data rather than independently fixing Lambda at the boundary.
Introduce positive auxiliary reference scales mu_aux,M_aux. On a finite
oriented FLRW slab, use well-posed gravitational boundary terms and variations
that give the stated bulk equations; the three-form pullbacks are fixed on
the boundary. Infinite-time flux statements below are regulated limits of
finite slabs and are additional boundary assumptions, not initial-value
selection theorems.

The Planck coefficient q and H_v remain empirically supplied parameters on
the desired branch. The task is constant-vacuum-shift insensitivity and a
compatible solution, not their derivation. No observed target is hidden in a
claimed first-principles value. General quantum-gravity stability, a measure
over flux sectors and a primordial probability law remain open.

## Action and local auxiliary constraints

Consider

  S=integral vol_g [q L0-Lambda A^4]+Gamma_m[A^2g]
    +integral (Lambda/mu_aux^4) F
    +integral [q^2/(2M_aux^4)] Fhat.

Here q has mass dimension two, Lambda and rho dimension four. F,Fhat are
metric independent before variation. The Lambda coupling is deliberately
linear; the q coupling is quadratic. This is a specified choice, not an
automatic specialization of every conclusion in the sequestering literature.

Varying the three-forms and using q>0 on a connected component gives

  dLambda=0, dq=0.

Varying Lambda and q gives the local four-form equations

  F=mu_aux^4 A^4 vol_g,
  Fhat=-(M_aux^4/q) L0 vol_g.

The forms carry no new local propagating mode through these equations;
q,Lambda are constant on shell. This statement does not analyze a
quantization over topological sectors. On a homogeneous slab these forms
have explicit potentials B3=b(t)d^3x, bdot=mu_aux^4 A^4 scale^3, and
Bhat3=bhat(t)d^3x, bhatdot=-(M_aux^4/q)L0 scale^3. Thus local integrability
is explicit. The boundary fluxes are the endpoint differences of these
potentials.

After separating the constant rho from the matter stress tensor, all local
metric/scalar equations depend on it only through

  Lambda_tilde=Lambda+rho,
  V_eff=V+[Lambda_tilde/(2q)]A^4.

They are the original analytic equations with that effective potential and
q=M_E^2. Let T_ex be the Einstein-frame trace excluding the constant
vacuum, and Q=K_AB partial(phi^A).partial(phi^B). The on-shell metric trace
and the q constraint imply

  q R=2q Q+8q V-T_ex+4Lambda_tilde A^4,
  q L0=2q V-T_ex/2+2Lambda_tilde A^4.

Off shell, metric variation of qR/2 also gives the usual derivatives of q;
they vanish only after the four-form equations enforce dq=0. Omitting them
before variation would not be a valid derivation of the unconstrained action.

## Exact constant-shift covariance, with its boundary condition

For any constant delta, change rho to rho+delta and Lambda to Lambda-delta.
All local metric/scalar/auxiliary equations and q,F,Fhat remain unchanged.
At the action level the only change is

  delta S=-(delta/mu_aux^4) integral F.

In a fixed flux sector this is field independent. Hence there is a
one-to-one map between the classical solution sets, with the same physical
metric, scalar fields, non-vacuum matter and fixed form fluxes. No scalar
force survives from the cancelled A^4 operator: the cancellation holds for
arbitrary u, not merely at the old origin.

This is a conditional solution-map theorem. It does not show that an
ordinary local scalar dynamically settles on an unmeasured constant.
Lambda must be allowed to vary as the auxiliary integration constant;
holding its numerical value fixed would remove the map. A path-integral
extension would also require the compatible translation-invariant Lambda
measure and the fixed sector. Summing different flux sectors can change
relative phases; such a sum is not asserted to be invariant.

A spacetime-dependent vacuum-like source delta(x) cannot in general be
absorbed by constant Lambda. Phase-transition stress, thermal energy,
gradients and localized Casimir stresses remain separate gravitational
sources. This calculation concerns only the constant zero-derivative
matter coefficient identified in the preceding block.

## Finite-volume trace and flux relation

Let c_F=integral F and c_hat=integral Fhat on a finite slab, with c_F nonzero.
Define the dimensional ratio

  B_flux=-(q mu_aux^4/M_aux^4)(c_hat/c_F)
        =integral L0 vol_g / integral A^4 vol_g.

Define barV=integral V vol_g/integral A^4 vol_g and
barT=integral T_ex vol_g/integral A^4 vol_g. Integrating the trace identity
gives exactly

  Lambda_tilde=q B_flux/2-q barV+barT/4.

There is no separate rho on the right. The geometric averages still depend
on the solution, and their boundary specification is part of the theory.
This relation by itself is not a prediction of a small observed curvature.
It should not be confused with freely choosing a bare counterterm while
leaving its physical boundary conditions unspecified.

## A compatible complete supplied-fluid history

Take any original analytic tracking solution, q at its supplied value, and
Lambda=-rho. Then V_eff=V and every original matter/scalar/metric equation
is unchanged. The explicit form potentials above solve the auxiliary
equations. Its finite-slab fluxes depend on that history but do not change
when rho is shifted and Lambda compensates it. This is a constructive
existence result for each rho, with unchanged matter/radiation amplitudes.

On the tracking branch, A=1 and

  sigma=H_v^2 x^2, r=H_v^2 y^2,
  H^2=H_v^2+(2/3)(1+a)(sigma+r),
  Hdot=-(1+a)(sigma+4r/3),
  L0=3H_v^2+(1+a)sigma+(2a/3)r,
  T_ex=-2q sigma.

The final L0 formula follows both from R=6(Hdot+2H^2), Q=-T_scalar and
the integrated trace. It is generally larger than 3H_v^2 at finite
nonzero densities. Consequently setting B_flux=3H_v^2 on an arbitrary
finite slab would not admit that exact positive-fluid history. The
finite-slab ratio must be the actual integral, or one must explicitly
take the future limit described next. We will test this distinction
numerically rather than replacing the finite integral by its endpoint.

For finite comoving volume and a fixed finite initial time, the
future-expanding tracking solution has

  lim(T->infinity) B_flux(T)=3H_v^2.

The numerator's deviation from 3H_v^2 times volume contains a dust
contribution that grows at most linearly in late proper time and a
radiation contribution with finite late integral; the denominator grows
exponentially. Equivalently L0->3H_v^2,A->1 with diverging positive
volume gives the weighted-average limit. Both raw form fluxes diverge;
their ratio is the stated well-defined FLRW-regulated limit. This
argument does not define averages over arbitrary inhomogeneous infinite
spacetimes.

The same limiting ratio holds for every original finite-energy
homogeneous solution on its zero-residual branch, using the already
checked convergence theorem and the on-shell curvature identity.
Thus this boundary condition remains compatible with the original
family of initial data; no observed abundance is inferred from it.

## Constant vacua selected by the specified asymptotic ratio

Impose the EXTRA future flux boundary condition B_flux=3H_v^2. Analyze
only constant-field, zero-fluid, expanding de Sitter solutions of the
displayed action, at fixed q,a,nu,H_v. Potential positivity gives x=y=0
at any stationary point. Write t=sqrt(a)u and ell=nu/a. Eliminating
Lambda_tilde with the scalar stationary equation gives

  [3+ell(t^2-t)] exp(-4t)=3,
  m_u^2/H_v^2=nu(1-4t).

The point t=0 has Lambda_tilde=0 and positive scalar masses
(nu,9/4,2)H_v^2. It is the unique solution of this constant-vacuum
constraint with a positive canonical scalar Hessian:
for t<0 the left side is greater than3; for 0<t<=1 it is less than3;
any other root must have t>1 and hence m_u^2<0. This is a statement
about the local scalar Hessian. Global boundary constraints can
restrict perturbations, so we do not turn it into a proof about
stability of every boundary-value solution or convergence of all
solutions of the extended theory.

For a neighboring ratio B_flux/H_v^2=3+epsilon, the regular branch
through u=0 obeys, at first order,

  t=-a epsilon/(nu+12a)+O(epsilon^2),
  C/H_v^2=nu epsilon/[4(nu+12a)]+O(epsilon^2),
  H_J/H_v=1+epsilon/12+O(epsilon^2),
  G_T,J/G_T,J(0)=1-2a epsilon/(nu+12a)+O(epsilon^2),

where C=Lambda_tilde/(2q). The H_J response must include the physical
conformal clock. H_v and the flux ratio still encode the chosen
curvature scale. These relations are conditional predictions for changing
that boundary input, not fits or new measurements.

## Primary context and limits

Kaloper, Padilla, Stefanyszyn and Zahariade,
arXiv:1505.01492v2, equations7-10 and subsequent discussion, motivate
the use of two metric-independent four-forms and warn that infinite-volume
ratios require care. Their standard model uses different gravitational
terms and generally nonlinear auxiliary functions. Our deliberately linear
Lambda coupling, scalar-dependent Jordan volume and q-scaled entire
gravitational/scalar L0 require the derivation above; the paper's
radiative-stability conclusion is not imported wholesale. The earlier
global sequestering formulation's finite-volume restriction is also not
assumed away by calling an infinite integral finite.

The claimed result is conditional cancellation of a constant matter-vacuum
shift and compatibility of the reconstructed history under explicit
auxiliary and boundary premises. The observed small H_v, measured q, scalar
loop corrections, induced derivative operators, flux-sector origin,
topology/quantization, changing vacuum phases and general Cauchy evolution
remain separate questions. All known-matter inputs remain exposed.
