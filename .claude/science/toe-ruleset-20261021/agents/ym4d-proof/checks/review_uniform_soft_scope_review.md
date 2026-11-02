# Affected scope review: tree phase and finite-u normalization

**Claim type:** meta. **Finding: scope correction required.** The unqualified sentence following US1 can incorrectly identify its quadratic energy with the exact finite-u normalized negative-log density. That identification is false. US1 is the quadratic part of the u-stripped normalized tree phase. The uniform FC19 bound and neutral FC20 proof for that displayed energy remain mathematically unchanged.

This supplement corrects the corresponding unqualified language and the no-author-repair statement in the [original independent report](../REVIEW_UNIFORM_SOFT_MINIMIZER_ASTRA.md). That report and its [original receipt](review_uniform_soft_receipt.json) remain immutable. Their SHA-256 values are respectively `78d40a5480aafe94c30ee5c0b827d30b84ec629dfccaa91b44c98cfe08ecf3d9` and `33b98352bcdae4c40f9db02cefbbdfd225063395da0c7c589ee47626e0ed10a3`. The new covariance worker raised the distinction; this reviewer independently reconstructed the finite-u coefficient below. No claim of independent discovery is made.

## Exact original convention

[LINEAR_PACKAGE §1.3](../LINEAR_PACKAGE.md) explicitly calls its energy the quadratic part of the tree-level exponent. The original Decision-4 kernel in [the frozen proof](../PROOF_session16_snapshot.md), lines 1498–1526, uses u=1/g^2, t=kappa*u, normalized trace q(A)=Re tr(A)/N and Haar measure of total mass one:

`K_t(V,M)=exp(t q(V^-1 M))/Z_t(M)`,
`Z_t(M)=integral_SU(N) exp(t q(W^-1 M)) dW`.

The common exp(-t) factors have canceled here; no convention has changed. Let `m(M)=max_W q(W^-1 M)` and `phi_M(V)=m(M)-q(V^-1 M)`. Exactly,

`-log K_t(V,M)=t phi_M(V)+log J_t(M)`,
`J_t(M)=integral_SU(N) exp(-t phi_M(W)) dW`.

The second term depends on M. Canceling an explicit shrinkage term in the first rewriting does not remove that dependence. The corrected [FLOW §3.1](../FLOW.md), lines 114–144, separates the normalized phase phi from the Haar integral, including the SU(N) polar determinant correction. [Recovery §3.1](../RECOVERY_UIR_ASTRA.md) identifies the same normalized tree phase and its coordinate scaling. The complete homogeneous fourth-order value in [FC18](../RESIDUAL_FULL_COLOUR_ASTRA.md) is explicitly a tree value. Its T_n refers to this stationary phase, not the complete finite-u effective action.

## Independent derivation of the surviving term

Use the Lie norm `||X||^2=-Re tr(X^2)/N`. Let the actual contour transporters be T_tau(epsilon), with T_tau(0)=I and T_tau'(0)=X_tau, and let `Xbar=average X_tau=Q_root a`, `sigma^2=average ||X_tau-Xbar||^2`, `r=B-Xbar`, `V(epsilon)=exp(epsilon B)`. The real trace of each unitary contour has its second derivative fixed by X_tau, irrespective of the traceless anti-Hermitian second-order commutator terms. Therefore

`q(V(epsilon)^-1 M(epsilon))=1-epsilon^2 (||r||^2+sigma^2)/2+O(epsilon^3)`.

At M=I, put `dmu_t(W)=Z_t(I)^-1 exp(t q(W))dW`. Conjugation invariance makes `E_t[W]=c_N(t) I`, and inversion invariance makes c_N(t) real and gives the same expectation for W^-1. Hence

`D log Z_t(I)[H]=(t c_N(t)/N) Re tr H`,
`c_N(t)=E_t[q(W)]=d log Z_t(I)/dt`.

Multiply M(epsilon) on the left by exp(-epsilon Xbar), which leaves Z_t unchanged by Haar invariance. The resulting curve has zero first derivative, while its second derivative has real trace `-N sigma^2`. Thus

`[epsilon^2] log Z_t(M(epsilon))=-t c_N(t) sigma^2/2`,

and the exact finite-u quadratic coefficient of the negative log kernel, after subtracting its identity value, is

`[epsilon^2](-log K_t)=t/2 [||r||^2+(1-c_N(t)) sigma^2]`.  (SCOPE1)

This holds for arbitrary first-order colours, not just the SU(2) control below. Haar integration of a nontrivial irreducible fundamental representation gives c_N(0)=0. Also `c_N'(t)=Var_t(q(W))>0`, and q(W)<1 away from I while the finite-t density has full support. Consequently `0<c_N(t)<1` for every finite t>0. The spread term in SCOPE1 is strictly positive whenever sigma^2>0.

By contrast, the normalized maximum m(M(epsilon)) has quadratic decrease sigma^2/2. Thus `[epsilon^2]phi=||r||^2/2`; the phase has exactly the residual-only quadratic term used in US1. Pure gradients and harmonic constant links have equal contour phases and sigma^2=0, so this correction does not contradict their gauge or harmonic null modes.

For fixed N and t tending to infinity, the unique maximum q=1 occurs at I. In Lie coordinates q(exp X)=1-||X||^2/2+O(||X||^4). Rescaling X=Y/sqrt(t), with the smooth Haar density and exponentially small contribution away from I, gives `t(1-c_N(t)) -> (N^2-1)/2`. Therefore the extra Hessian in the unstripped negative logdensity is of order one, while its contribution after division by u is of order 1/u. This local Laplace argument is not a depth-uniform control of any finite-u effective action.

## Exact target retained and wording repair

Define the normalized tree phase as

`F_tree=sum_p s(U_p)+sum_(j,c) kappa_j phi_(M_c(U_j))(U_(j+1),c)`.

Its quadratic part is US1 and its stationary value is the T_n consumed by FC18–FC20. The original analytic strip, stationary transport, Stokes and row/column estimates concern that quadratic energy. Its neutral fourth-order stationary coefficient is still FC18. They establish neither the corresponding minimizer of the full finite-u logdensity nor uniform localization of its conditional fluctuation covariance.

The [minimal replacement text](review_uniform_soft_scope_replacement.md) changes the opening scope, the introduction to US1 and the ambiguous paragraph after it. It does not alter any displayed US1–US17 formula. The original frozen consumer already calls FC18 a tree value, so no change to its formula or historical review is requested. The source owner will make the edit and provide exact changed bytes for affected re-review; no source correction has been made by this reviewer.

## Independent actual-kernel control

The [new criteria](review_uniform_soft_scope_criteria.md) preceded the [standalone implementation](review_uniform_soft_scope_01.py). For one coarse direction it constructs all 24*81=1,944 actual d=4,L=3 S4′ contours and a predeclared Cartan SU(2) link field supported on the edge from (0,1,0,0) to (1,1,0,0). Exactly 84 paths have phase one and 1,860 have phase zero. Thus the mean is 7/162 and the exact variance is 1085/26244>0.

For SU(2), the unit-quaternion Haar class measure is `(2/pi) sin(theta)^2 dtheta`. Direct 80-digit quadrature evaluates both c_2(t) and the exact normalizer of the actual complex path mean. No Bessel formula, predecessor helper or covariance-author code is used. Direct density differences at two predeclared epsilon values and Richardson extrapolation recover SCOPE1 at t=.5,2,8,32, for zero residual and residual .3. At zero residual, the tree Hessian is zero while the finite-u Hessians are approximately .018114, .046872, .059782 and .061514. The largest observed Hessian discrepancy from SCOPE1 is below 3.2e-16. This is a concrete counterexample to the broader finite-u reading of US1.

The [complete output](review_uniform_soft_scope_01_out.json) records 29/29 predicates, including actual gradient/constant-path controls, rejection of the finite-u-equals-tree mutation and bounded corroboration of `t(1-c_2(t))->3/2`. The [stderr stream](review_uniform_soft_scope_01_err.txt) is empty. The program executed once with exit zero; no failed predicate, implementation error or threshold change occurred. Repeated sample predicates are not independent theorems. Numerical quadrature is not an interval proof; the exact coefficient and strict positivity follow from the derivation above.

## Revised review disposition

The source requires the stated scope correction. The original mathematical confirmation survives for the explicitly displayed tree energy and neutral stationary T_n quartic. Its unqualified finite-u interpretation and the original report's no-repair wording are withdrawn. No broad rerun of the original linear controls is needed if the edit changes only this scope, but source confirmation must bind the actual repaired bytes after they arrive.

The full Yang–Mills existence and physical continuum mass-gap theorems remain OPEN. No conditional Gaussian localization, finite-part increment, nonlinear RG or audit verdict is supplied here. Original report, receipt, source and previous checks were left untouched; this supplement has its own [receipt](review_uniform_soft_scope_receipt.json). A packaging-only link scan initially misread inline mathematical code as a Markdown link; excluding code spans corrected the scanner. The [packaging event](review_uniform_soft_scope_packaging_attempt01.json) preserves that failure separately from the successful mathematical diagnostic.
