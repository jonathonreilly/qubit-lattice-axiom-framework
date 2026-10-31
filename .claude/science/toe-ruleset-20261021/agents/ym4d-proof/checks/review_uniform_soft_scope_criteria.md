# Scope supplement: finite-u normalization falsifiers

Recorded before the new diagnostic implementation or execution. The original
uniform-soft review, its receipt and all source inputs remain immutable. The
new covariance worker and coordinator raised the tree-phase versus exact
finite-u distinction; that concern is acknowledged as prior exposure. This
reviewer independently derived the quadratic coefficient from the original
Haar-normalized kernel before constructing this control. No covariance-worker
implementation is consumed.

The original kernel has t=kappa*u, u=1/g^2, and
`K(V,U)=exp(t Re tr(V^-1 M(U))/N)/Z_t(M(U))`,
`Z_t(M)=integral_SU(N) exp(t Re tr(W^-1 M)/N) dW`.
The candidate exact quadratic coefficient for a path variation with first-order
contour values X_tau, mean Xbar and top value B is
`t/2 [||B-Xbar||^2+(1-c_N(t)) average ||X_tau-Xbar||^2]`,
where `c_N(t) I=E_t[W]` at M=I. US1 instead is the quadratic part of the
u-stripped normalized tree phase with phi equal to the SU(N) maximum minus the
actual real trace. That distinction, not a new all-depth theorem, is tested.

Proof falsifiers:

- A finite-u spread term that survives at the identity rules out interpreting
  US1 as the full finite-u negative-log Hessian divided by u.
- The expectation must use the original normalized trace, Haar measure, and
  t=kappa*u. A scalar coefficient from a different trace convention is invalid.
- Pure gradient and harmonic data must have no contour variance correction.
- The exact phase's fourth derivative and FC18/FC20 must refer to T_n, the
  stationary u-stripped tree value, not to the full finite-u effective action.
- Any proposed correction that silently changes US1 or claims conditional
  covariance localization fails this scope-only task.

Independent diagnostic plan:

1. Construct the actual d=4,L=3 S4-prime paths for coarse direction 0 and all
   24 orderings and 81 centered block points. Use a fine Cartan SU(2) link field
   supported on the direction-0 edge from (0,1,0,0) to (1,1,0,0). Its contour
   phases are obtained by signed individual steps. At least one is zero and one
   is one, giving strictly positive spread without choosing a field post hoc.
2. For `SU(2)`, write a group element as a unit quaternion. Haar class integration
   is `(2/pi) integral_0^pi sin(theta)^2 dtheta`. Direct high-precision quadrature
   gives c_2(t) as the weighted cosine mean and gives the full normalizer for
   the actual complex path mean m(epsilon). No Bessel formula or author helper
   will be used to build the target.
3. At t=.5,2,8,32, evaluate the exact negative logdensity at top phases equal to
   the path mean and to that mean plus .3. Use epsilon=1/1000 and 1/2000 and
   Richardson elimination of the O(epsilon^2) Hessian error. Require absolute
   agreement with the derived Hessian to 1e-8; record raw values and errors.
4. At zero linear residual, reject the mutation that the finite-u Hessian is
   zero or that c_2(t)=1. Verify positive spread correction and verify the
   u-stripped tree phase has zero quadratic coefficient along this variation.
5. Check an actual lattice gradient and constant link field separately; every
   contour has the required identical endpoint/constant value, hence zero
   variance. At large t=64,256,1024, directly evaluate t(1-c_2(t)); its approach
   to 3/2 is bounded numerical corroboration of a separately derived Laplace
   asymptotic, not a proof for arbitrary t or N.

All computations are finite diagnostics. Preserve every implementation error,
failed predicate or changed criterion. The original report's no-repair wording
will be corrected explicitly in a separate supplement if the scope concern is
confirmed; its frozen bytes will not be rewritten.
