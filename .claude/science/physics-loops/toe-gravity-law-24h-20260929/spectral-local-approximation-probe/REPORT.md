# Local centered Hamiltonian continuation

Author proof candidate, 2026-09-30. The parent analytic evolution proof is
now independently checked at REPORT SHA93e302c06d9e6a6c85f3c538f2d765ec1dcb5734065f740b310e9144f6abd6b8;
the focused check is independent-spectral-evolution-check/REPORT.md,
SHA11a2350888aea0c661b1ccf5f0196898ab9aa7012f0955b4e991bd257f3ba65f.
This extension has not yet had a focused independent check. It belongs to
the same nonlinear approximation unit, not a new theorem family or PR.

## Exact changed law and local support

Keep the parent's six full canonical metric pairs on the odd n=2J+1 torus,
physical period2pi, density momenta p=n^3 P, symmetric pi offdiagonal p/2,
positive kinetic/curvature couplings a,K, and literal Christoffel definition
of C. Write the physical mesh spacing as epsilon=2pi/n to avoid confusing
it with kinetic coupling a. Replace every spatial derivative by

 D_epsilon,j f(x)=[f(x+epsilon e_j)-f(x-epsilon e_j)]/(2epsilon).

The actual finite Hamiltonian is H_epsilon=C_epsilon[1], with unit lapse and
zero shift, ordinary grid products and every canonical mode retained. Its
Fourier symbol is i sin(epsilon k_j)/epsilon. This changes block112's seed,
collocation and timings. No old exact finite closure result transfers.

The literal C density has coordinate support in the graph ball of radius2:
the outer D acts on a Christoffel expression using an inner Dg. Nevertheless
the GLOBAL unit-lapse H has the exact summation-by-parts representation
mean[T+V(g,Dg,D B(g))] from the parent. Each local term of that representation
touches only the center and its six nearest neighbors, so its support has
radius1 and diameter2. The actual g,p equations consequently have radius at
most2. The momentum density pi:q_k-2D_j(g_ik pi^ij) has radius1. These are
stencil distances; inverse and square-root matrices act pointwise and add no
spatial support. A nonuniform lapse need not share the unit-lapse density
rewrite, and its exact algebra is not asserted.

The redundant q=Dg,r=D B augmentation and adjoint variation hold verbatim
because this D is real, skew-adjoint and time independent. In particular,
B_g multiplies D V_r AFTER differentiation; no spatial chain rule is used.
Both consistency identities q-Dg and r-D B remain exactly zero from
consistent initial data. Augmentation changes no physical carrier.

## Uniform analytic existence

Use precisely the parent's Wiener norms, fixed radius sigma0, real initial
g0=I+h0 with |h0|_(2sigma0)<=1/8, and finite |p0|_(2sigma0). The circular
algebra and N seminorm estimates do not depend on the derivative symbol.
For all representative modes, |sin(epsilon k_j)/epsilon|<=|k_j|. Thus every
derivative-loss, initial derivative, bootstrap and scale-Lipschitz bound
of parent sections3-5 remains valid with the SAME finite constants C0,C1,
C_h,C,M0,M and common positive times T0,T. In particular no lower bound
on this symbol, absence of doubler modes, or coercivity is used.

The compactness proof still passes to the continuum augmented ADM equation:
on each fixed Fourier mode the multiplier converges to ik_j; uniform analytic
tails and one radius reserve control the complement. Local product aliases
obey the unchanged circular Wiener bound. Continuum uniqueness is the same
ordered Volterra argument. Alternatively, once the parent constructs that
continuum solution, the following direct consistency estimate and its
Volterra stability prove convergence without a second existence construction.

## Full sampling commutator, including aliases

Let I_J be actual sampling. For every original mode k in Z^3, including
those outside the representative cube, the centered difference multiplier
on its sampled value is i sin(epsilon k_j)/epsilon, since epsilon n=2pi.
There is consequently no separate alias error to insert into this derivative
commutator: periodicity already includes all aliased modes. For all real z,
|sin z-z|<=|z|^3/6 by Taylor's integral remainder. Thus for delta=rho-rho'>0,

 sum_j |(D_epsilon,j I_J-I_J partial_j)f|_rho'
     <= epsilon^2 L(delta) |f|_rho,
 L(delta)=(1/6)[3/(e delta)]^3.                         (1)

Indeed |wrap(k)|_1<=|k|_1, sum_j |k_j|^3<=|k|_1^3 and
sup_(u>=0) u^3 exp(-delta u)=[3/(e delta)]^3. This proof covers the
zero mode, near-Nyquist modes and arbitrary analytic Fourier tails, without
projecting a bracket or removing high canonical variables. The prospective
extra exponential alias allowance in CONTRACT is unnecessary for this
particular periodic symbol. Interpolant-to-continuum comparison still has
the usual separate Fourier sampling tail; (1) concerns samples themselves.

Use rho2=3sigma0/4,rho1=sigma0/2,rho0=sigma0/4 and delta=sigma0/4.
For the parent's finite decomposition F=F0+sum_l P_l D_j Q_l set

 K_R^loc=L(delta) sum_l m_P_l m_Q_l,
 K_0^loc=L(delta)(|h0|_rho2+|B(g0)-I|_rho2).

Algebraic local maps commute with sampling exactly. Equation(1) gives source
norm <=epsilon^2 K_R^loc and initial augmented mismatch <=epsilon^2 K_0^loc.
The metric and momentum initial samples agree exactly. Applying the same
Volterra bound on t<=T gives

 |U_epsilon(t)-I_J U(t)|_rho0
          <=2(K_0^loc+T K_R^loc) epsilon^2.              (2)

Actual finite solutions, not projected continuum equations, appear here.
The sampled continuum q/r may be off the finite consistency manifold; the
augmented vector field is defined on the full common convex analytic ball.

The true scalar and three momentum densities have at most one D acting on
a local analytic map of U. Their uniform scale-Lipschitz estimate between
rho0 and sigma0/8, combined with (1) applied using a positive continuum
radius reserve, bounds their differences from sampled continuum densities
by C_constraint^loc epsilon^2, uniformly on[0,T]. The constant comes from the
same finite majorant procedure. If the continuum initial constraints vanish,
the parent's exact continuum propagation keeps them zero; the actual finite
densities are therefore O(epsilon^2). They need not vanish initially or later.

## Interpretation and planned diagnostic

This supplies a candidate finite-range, actual-Hamiltonian approximate escape
under analytic preparation and mesh refinement. It is compatible with the
proved obstruction to exact local mixed closure, whose conclusion has not
been weakened. The law still supplies continuous canonical tensors, a chosen
Hamiltonian, external lapse/time and an analytic continuum comparison. The
centered ultraviolet branch remains; no generic smooth-data stability, unique
low-energy graviton content, common original-matter action, record clock,
native M2 realization or axiom inconsistency follows.

The planned diagnostic adapts the parent's actual diagonal restriction by
changing ONLY the derivative matrix and refinement grids. It will rerun the
original-H versus exact-adjoint gradient control, then the same pulled-back
Kasner data. It is author reuse, not an independent implementation. Record
true C and nontrivial J_x densities, initial finite sampling defects and
energy drift. The transverse J_y,J_z vanish identically by this symmetry.
The duration0.01 is a chosen diagnostic interval, not certified by the very
conservative analytic time. Expected second-order refinement is a control,
not the proof of(2). Price30 CPU seconds/150MB, BLAS1, no worker persistence.
