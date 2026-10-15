# Independent physical-metric static scalar comparison

This derivation uses only the inherited complete supplied action. No new author working note or program has been read. It gives two necessary upper bounds on the radial variable in a regular finite static domain. The transverse fields remain present. Neither bound identifies the action's Q with a measured Newton constant, proves existence for an arbitrary prescribed metric, selects a static state or supplies its boundary data.

## Inputs and exposure

The complete local-response and future-confinement notes were read. The earlier finite-body note supplies context for the distinction between a held flat scalar model and a full physical-metric solution; its zero-transverse reduction and vacuum matching are not imported here. Exact inherited source copies and hashes are in INHERITED_EXPOSURE_v1.json.

The parent task supplied the variable z=exp(-sqrt(a)u), a finite boundary upper bound zB>=1, and asked whether physical curvature permits a necessary comparison. After I reported the action cancellation and maximum bound, the parent said its independent working route used a curvature-functional comparison, without sending a formula or source. That route-category exposure is disclosed. The formulas below were obtained from my own variation and positive-part/Green argument; no parent working derivation or code was opened. This is a focused independent derivation, not a formal audit or a new scientific-author role.

Fix 0<k<1/3, nu>0, Q=Q0(1+k)>0 and Hv>0. Write

    a=(1-k)(1+3k)/4, alpha=sqrt(a),
    s=(1+k)/(k(1-3k)), B=1+s,
    kappa=(1-3a)/a.

Then 1/4<a<1/3, 1/3-a=(1-3k)^2/12, and kappa>0. The action has no half-factor before its Einstein-frame K kinetic term:

    S=Q integral sqrt(-ghat)[Rhat/2-K_AB dphi^A.dphi^B-2Hv^2 U]
       +Sm[C ghat,psi].

All parameters, the matter action and its universal physical metric are supplied candidate definitions. Natural units and signature (-+++) are retained.

## Complete physical Jordan action

Set g=C ghat and z=exp(-alpha u)>0. Then

    C=B/(z^2+s), u=-ln(z)/alpha,
    D=1+2(1+k)(x^2+y^2)/3,
    px=(1-k)/a, py=(1+k)/a.

Under this conformal transformation,

    sqrt(-ghat) Rhat = sqrt(-g) C^-1
       [R+3 Box ln C-(3/2)(d ln C)^2].

Integrating the Box term by parts contributes a net positive `(3Q/(4C))(d ln C)^2` to the physical-frame kinetic density, up to the displayed conformal boundary divergence. This is a bulk-equation calculation with compactly supported variations or corresponding boundary terms. Thus the scalar kinetic matrix is `Q C^-1[K_AB-(3/4)(ln C)_,A(ln C)_,B]`.

Its radial coefficient after replacing u by z is exactly constant. Indeed `(ln C)_,u=2alpha/F`, `K_uu=J/F^2`, and `J-3a=(1-3a)F`, so

    C^-1 [K_uu-(3/4)(ln C)_,u^2] (du/dz)^2 = kappa/B.

The full transformed action is

    S=(Q/B) integral sqrt(-g) [
         (z^2+s)R/2 - kappa (dz)^2 - z^2 Tperp - 2Hv^2 V]
       +Sm[g,psi],

    Tperp=B[4k (dx)^2/(9D)+k (dy)^2/(3D)],

    V=(3/2)(z^4+s)+(nu/(2a))z^4 ln(z)^2
       +k x^2 z^px (z^2+s)^2/(2B)
       +k y^2 z^py (z^2+s)^2/(3B).

The apparent constant radial kinetic term is a consequence of the complete action, including its conformal Einstein term. The transverse kinetic coefficients depend on x,y through D and are not discarded. At fixed g, Sm has no explicit z variation under the supplied universal-coupling definition. Matter nevertheless affects the metric equations; this calculation does not remove that dependence from a full solution.

## Static radial field equation and signs

Varying z independently at fixed g,x,y gives exactly

    kappa Box_g z = z(Tperp-R/2)+Hv^2 V_z.             (1)

The factor Q/B cancels from this equation. A separate weighted one-dimensional Euler-Lagrange calculation fixes both the curvature sign and the factors of two.

For a static physical metric and static scalar fields,

    ds_J^2=-N(x)^2 dt^2+h_ij(x)dx^i dx^j, N>0,
    L z = [N sqrt(h)]^-1 partial_i[N sqrt(h) h^ij partial_j z]
        =Delta_h z+grad_h ln N . grad_h z,

and Box_g z=Lz. In particular R is the four-dimensional physical Ricci scalar, not merely the spatial scalar: `R=R[h]-2 N^-1 Delta_h N`. The latter follows from `R_tt=N Delta_h N` and `R_ij=R_ij[h]-N^-1 Hess_h(N)_ij`. A lapse or coordinate conversion cannot be dropped when using an observed metric.

Staticity makes Tperp>=0 without setting x or y to zero, requiring them to be constant, or solving their equations first. Also

    V_z=6z^3+(nu/a)z^3 ln(z)[2ln(z)+1]
         +k x^2/(2B) z^(px-1)(z^2+s)[(px+4)z^2+px s]
         +k y^2/(3B) z^(py-1)(z^2+s)[(py+4)z^2+py s].

For z>=1 every displayed contribution is nonnegative and V_z>=6z^3. This uses no upper bound on nu. It is deliberately not a claim about all z>0.

Assume henceforth a bounded regular domain Omega, a positive smooth lapse bounded away from zero, a smooth positive spatial metric uniformly elliptic on its closure, and a regular finite-field static solution. Assume the boundary trace satisfies 0<z<=zB for a supplied constant zB>=1. Smooth strong solutions suffice; the positive-part argument below extends to an appropriate weak formulation. Horizons, singular interfaces, noncompact ends and degenerate ellipticity require separate boundary/regularity proofs. An unbounded domain needs an exhaustion or suitable limiting boundary/maximum-principle hypotheses, not just this finite-domain statement.

## A potential-scale maximum bound

Let Rmax=sup_Omega R. If z attains an interior maximum above zB, then Lz<=0 there, so (1) implies

    R >= 2Hv^2 V_z/z >= 12Hv^2 z^2.

Consequently every admitted solution obeys

    z <= Zpot := max[zB, sqrt(max(Rmax,0)/(12Hv^2))].  (2)

This is a necessary ceiling, even with nonzero transverse fields. It uses the supplied potential scale Hv and a bound on the physical metric curvature. Neither is claimed already measured or derived. If Rmax<=12Hv^2, the boundary upper bound alone controls the interior maximum.

One may keep the positive regulator term. Define for t>=1

    Fcurv(t)=12Hv^2 t^2+(2nu Hv^2/a)t^2 ln(t)[2ln(t)+1].

It is strictly increasing since

    Fcurv'(t)=24Hv^2 t+(2nu Hv^2/a)t[4ln(t)^2+6ln(t)+1]>0.

Set zeta=1 if Rmax<=12Hv^2; otherwise let zeta be the unique root `Fcurv(zeta)=Rmax`. Then `z<=max(zB,zeta)` sharpens (2). No chosen homogeneous density minimum enters the proof. The bound does not show the existence of a full solution that attains it.

## A curvature-functional finite-domain bound

There is a useful complementary bound that does not use the numerical magnitude of Hv. Define

    qR=R_+/(2kappa), R_+=max(R,0),
    G_D=(-L_D)^-1, with zero Dirichlet boundary,
    T f=G_D(qR f), eta=||G_D(qR)||_infinity.

The weighted Dirichlet operator is positive on the declared regular domain. Its measure is `N sqrt(h) d^3x`. Positivity gives `||T||_{infinity->infinity}=eta`.

Let w=(z-zB)_+. On its positive set z>=1, so (1), Tperp>=0 and V_z>=0 imply `-Lz<=qR z`. The convex positive-part inequality gives distributionally

    -Lw <= qR(zB+w), w|boundary=0.

Dirichlet comparison therefore yields

    w <= zB T1+T w.

If eta<1, taking suprema closes this inequality:

    ||w||infinity <= zB eta/(1-eta),
    z <= Zgreen := zB/(1-eta).                       (3)

A pointwise version is `z<=zB sum_{n>=0} T^n 1`. The finite boundary data, physical static geometry and k remain suppliers. Condition eta<1 is sufficient for this particular quantitative closure; eta>=1 is not evidence against a solution, against screening, or against the action. Equations (2) and (3) can be combined by taking the smaller admitted ceiling. In contrast to a prescribed particle-mass Newton potential, qR is computed from the actual physical metric curvature, and no Q-to-measured-G substitution appears.

For an explicit geometric control, take an ultrastatic physical metric with spatial three-sphere radius Lc and a geodesic ball `0<=theta<=thetaB<pi`. Then R=6/Lc^2 and the Dirichlet torsion function is

    G_D(1)=(Lc^2/2)[theta cot(theta)-thetaB cot(thetaB)].

Direct radial differentiation gives `-L G_D(1)=1`, and its maximum is at theta=0. Thus

    eta=3[1-thetaB cot(thetaB)]/(2kappa)
         ~ thetaB^2/(2kappa) for a small ball.

At k=1/6 and thetaB=pi/12, eta is about0.1721354. For zB=6/5 the Green ceiling is about1.4495124. If the separately supplied Hv*Lc=1/100, the cruder potential ceiling is about70.710678. These are operator/bound illustrations for an explicit geometry, not manufactured solutions of all the candidate's matter and metric equations or observational estimates.

## Consequences, failed shortcuts and remaining suppliers

An upper bound z<=Z implies `u>=-ln(Z)/sqrt(a)` and `C>=B/(s+Z^2)`. It does not give a positive lower bound on z, an upper bound on u, or a scalar-force/gradient bound. The model's local coupling norm is `g=a z^2/[z^2+(1-3a)s]`, increasing in z and equal to k at z=1; converting it to an actual local experiment still needs the finite-response and measurement premises. No Newton coefficient is inferred here.

Several tempting shortcuts are invalid and retained as explicit controls:

- Inserting a half-factor in front of the original K changes the transformed kinetic coefficient and the comparison constants. The inherited normalization is load-bearing.
- V_z is not positive over every z>0 for every allowed nu. With x=y=0, nu=64a and ln(z)=-1/4, `V_z/z^3=-2`. The positive-part proof is valid because zB>=1 restricts the tested excess to z>=1.
- A time-dependent transverse field can have negative Lorentzian `(dx)^2` or `(dy)^2`. Staticity, or an explicit replacement nonnegative-contraction condition, cannot be omitted.
- The first Green iterate is not a general upper bound. In the abstract comparison problem `-f''=q f` on [-L,L] with boundary zB and qL^2=1, the central value is zB sec(1)>1.5zB, whereas eta=qL^2/2=1/2. The full bound gives2zB. This is a comparison-operator witness, not a full candidate solution. The strict inequalities follow already from `1/2<cos(1)<13/24<2/3`.

The 42 independent controls all pass. They check exact transformation coefficients, potential cancellation and derivatives, a separate weighted Euler-Lagrange variation, sign/domain and normalization witnesses, the spherical torsion formula, and the abstract comparison fixture. Their modest floating-point evaluations are illustrations; the comparison theorem rests on the displayed analytic proof. No author source or aggregate was executed, no observation or empirical holdout was opened, and there was no failed execution to hide. Rejected mathematical shortcuts remain in the report and control output.

The action, parameters, static realized state, finite boundary bound, physical metric/calibration and regular domain are still assumptions. Matter and metric equations must also hold for a full solution, but were not replaced by a convenient density trace in deriving the necessary scalar bound. These results constrain an admitted environment rather than select one. They do not prove existence, uniqueness, dynamical attraction, compact-object stability, an environmental force suppression, an observational exclusion or a TOE.
