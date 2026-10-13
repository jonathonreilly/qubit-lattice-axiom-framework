# Independent radiation-closure derivation

This checks the supplied action and ideal-fluid assumptions. It does not
derive radiation thermodynamics or select an initial entropy. The letter R
below denotes 4 pi G_star rho_r, not the metric Ricci scalar or scale factor.
S, R and L have units of inverse time squared; a is dimensionless.

## 1. Unchanged potential and positive conserved radiation

At u=0 the u equation requires the dust density to equal the function S(chi).
Therefore dot S=-3HS and dot R=-4HR, so R=b S^(4/3) with b>0. The original
potential gives S_chi=-3 Hbar sqrt(S/a), hence

    dot chi^2 = a S H^2/Hbar^2,
    Hbar^2 = 2[(1+a)S+L]/3.

The full Einstein Friedmann equation is

    3H^2 = 2(S+R+L)+aS+aS H^2/Hbar^2.

Solving algebraically, rather than assuming the old Hubble law, gives

    F=H^2=Hbar^2[1+2R/B],  B=(2+a)S+2L.

Differentiating this F along the conserved densities gives
dot H=-(3S/2)F_S-2R F_R, with partial derivatives treating S and R as separate
arguments. Direct subtraction of the Raychaudhuri value
-S-4R/3-aS F/Hbar^2 gives

    2aRS[(2+a)S-L]/(3B^2).

This is nonzero except at S=L/(2+a), under a,R,S,L>0. An expanding solution
cannot remain at that isolated S because dot S=-3HS and H^2=F>0. It follows
that the particular exact u=0 branch of this unchanged potential cannot obey
both equations on a positive-density time interval. Eta does not enter this
branch condition. The result excludes neither approximate trajectories nor
drifting u, other potentials or other supplied premises. In particular the
residual tends to zero with the densities and is not an observational lower
bound on a discrepancy.

## 2. New background equations

For the new construction define

    R=bS^(4/3), W=S+4R/3, C=(1+a)(S+R)+L,
    Hbar^2=2C/3, dot chi^2=aW,
    U=L+aS/2+aR/3.

Friedmann holds because 2(S+R+U)+aW=2C. Density conservation gives
dot H=-(1+a)W, which is exactly -W-dot chi^2. The transverse force cancels:
V_u+sqrt(a)S=-sqrt(a)S+sqrt(a)S=0. The longitudinal terms are

    ddot chi * dot chi/Hbar = -a(3S+16R/3)/2,
    U_chi * dot chi/Hbar = -a(3S/2+4R/3).

Adding these to 3 dot chi^2 gives zero. The chi equation, both conservation
equations, Friedmann and Raychaudhuri therefore agree. No equation uses the
choice of M away from u=0 to force this background identity.

The coordinate satisfies dS/dchi<0 for every S>0. Its inverse is smooth on
that open interval. The model's parameter b is chosen with the radiation
normalization and is part of the newly constructed potential; matching that
exposed background is not an independent prediction of the original model.

## 3. Bare Hessian and the lower bound

Let J=(dS/dchi)^2=6CS^2/(aW). Total S differentiation includes
dR/dS=4R/(3S). The chain rule gives

    U_chichi = J U_SS + (J_S/2)U_S.

Independent simplification gives the explicitly positive expression

    U_chichi = [L(128R^2+192RS+81S^2)
              +(1+a)(256R^3+656R^2S+561RS^2+162S^3)]
              /[6(4R+3S)^2].

Thus U_chichi>0 for the stated positive domain. Equivalently U_S>0,
U_SS>0 and J_S>0, as asserted in the note. The derivative itself is

    J_S = 6S[8LR+9LS+(1+a)(24R^2+41RS+18S^2)]
          /[a(4R+3S)^2] > 0.

U_SS=0 in the optional b=0 limiting control, but the other term still makes
U_chichi positive. The main theorem assumes b,L>0; a zero-L grid control
does not acquire the positive-L future-vacuum expansion by continuity of
notation alone.

With M=aJ/U_chichi+aS^2/U, the on-trajectory Hessian is

    [[M, -sqrt(a)S_chi],[-sqrt(a)S_chi,U_chichi]].

Both diagonal entries are positive and its determinant is
aS^2 U_chichi/U>0. This is a positive **bare** potential Hessian at u=0, not
a claim of positive Hessian throughout the entire two-dimensional field space
or of stable coupled matter/metric evolution.

For all real u at each S>0,

    V = M/2 [u-sqrt(a)S/M]^2 + U-aS^2/(2M).

Since M>aS^2/U, the last term is greater than U/2. The stated weaker bound
V>=U/2>0 is consequently valid globally in u. This is an algebraic bound;
no numerical optimization or selected interval of u is needed for its proof.

## 4. Full field-coordinate equations

Dimensionally, x means ln(S/S_ref) with a fixed positive reference density;
the same convention applies to lm and lr. Writing ln S is shorthand after
choosing units. The choice only shifts the coordinate origin. The field
metric is the fixed function

    g(x)=aW/(9 Hbar(S)^2),  dchi/dx=-sqrt(g),
    Gamma=g_x/(2g).

Hbar here belongs to the constructed coordinate function; it is not replaced
by the actual off-trajectory Hubble value when evolving perturbed states.

The canonical proper-time equation for chi transforms to

    ddot x+3H dot x+Gamma dot x^2+V_x/g=0.

For Einstein N=ln(scale factor), w=du/dN and p=dx/dN, this gives

    p'=-(3+h)p-Gamma p^2-V_x/(gH^2).

The u equation gives the corresponding source
-(V_u+sqrt(a)sigma_m)/H^2. Radiation has no direct scalar force because its
stress trace vanishes. Friedmann and Raychaudhuri yield exactly

    H^2=2(sigma_m+sigma_r+V)/(3-w^2-gp^2),
    h=-(sigma_m+4sigma_r/3)/H^2-w^2-gp^2.

Einstein rest-mass conservation gives lm'=-3+sqrt(a)w; radiation gives
lr'=-4. These equations hold off the specified trajectory on the positive-H,
positive-density chart with positive denominator.

On the target, p=-3, u=w=0 and the denominator is positive because

    Hbar^2(3-9g)
      =(2+a)S+(2+2a/3)R+2L > 0.

The x acceleration reduces identically to zero there. The independent symbolic
check verifies this separately from the canonical background equations. The
metric g is positive on S>0 but tends to zero at the future endpoint x=-infinity;
this is coordinate degeneration, not an added physical degree of freedom.

## 5. Early limiting slopes and the correction

The normalized speed obeys the exact relation

    (chi'/sqrt(a))^2 = W/Hbar^2.

For R/S large and L negligible this tends to 2/(1+a), as stated. In the
dust-dominated limit R/S and L/S both tend to zero, it instead tends to
3/[2(1+a)]. The original handwritten square-root expression omitted this
factor of two. V2 corrects exactly that phrase and leaves every other equation
unchanged. The original failed assertion remains in the first test result.

Because U scales as R proportional to scale_factor^-4 in the first limit and
as S proportional to scale_factor^-3 in the second, the respective positive
exponential steepness magnitudes are

    kappa_rad=sqrt[8(1+a)/a],
    kappa_dust=sqrt[6(1+a)/a].

The actual logarithmic derivative with increasing chi is negative. Both
steepness values in v1 were already correct. For an arbitrary fixed positive
b,L pair, a clean intermediate dust epoch is not guaranteed; the dust result
is the stated conditional dominance limit. As S tends to infinity at fixed
b>0, the actual asymptotic past is radiation dominated.

## 6. Future fractional powers and full-potential regularity

Let H_vac^2=2L/3, beta=3H_vac/(2sqrt(a)), q=beta(chi_c-chi)>0. Then

    dq/dS = (1/2)S^-1/2 sqrt(1+4bS^(1/3)/3)
            /sqrt[1+(1+a)(S+bS^(4/3))/L].

The integral converges at S=0, so chi_c is finite. Put y=S^(1/6). Its ordinary
Taylor expansion integrates to

    q=y^3+(2b/5)y^5-(2b^2/21)y^7+O(y^9).

Series inversion, not fitting to numerical values, yields

    S=q^2-(4b/5)q^(8/3)+(464b^2/525)q^(10/3)+O(q^4),
    U=L+(a/2)q^2-(ab/15)q^(8/3)
        +(136ab^2/1575)q^(10/3)+O(q^4).

Thus both displayed handwritten fractional coefficients are correct. To check
the whole potential, beta cancels from a(S_chi)^2/U_chichi, giving

    M=4q^2-(992b/135)q^(8/3)+O(q^(10/3)).

Consequently

    V=L+A2(u)q^2+A8(u)q^(8/3)+O(q^(10/3)),
    A2=a/2-sqrt(a)u+2u^2,
    A8=-(496b/135)(u-27sqrt(a)/248)^2-43ab/1860.

A8 is strictly negative for all finite real u when a,b>0. The value, gradient
and Hessian have finite one-sided limits, locally uniformly in finite u.
Third chi derivatives diverge; already at u=0,

    U_chichi_chi ~ (16ab/81) beta^3 q^-1/3.

This proves one-sided C2 but not C3 behavior for the full potential. A C2
continuation across the finite endpoint can be supplied mathematically, but
the defined S>0 branch does not select one or establish global evolution
through it. There is no analytic endpoint extension for this same b>0
one-sided function. The conclusion is distinct from a claim that the open
S>0 potential is nonsmooth; it is smooth at every interior point.

## 7. Independent numerical control

`check_radiation_endpoints_v1.py` uses 90-digit quadrature of the exact y
integral, with no truncated series substituted into the integrand. It evaluates
18 combinations of three couplings, three b values and two positive L values,
at S=10^-9,10^-18,10^-30: 54 coordinate rows. It separately differentiates U
and J numerically at high precision to obtain U_chichi and M.

The ratios (S-q^2)/q^(8/3), [U-L-aq^2/2]/q^(8/3), and
(M-4q^2)/q^(8/3) converge to the derived coefficients. The worst final relative
errors are respectively 1.1048e-9, 1.2953e-9 and 1.5612e-9, below the
pre-execution 2e-7 numerical comparison tolerance. The code also checks
positive determinant and representative complete-square bounds; the proof
above, not those finite samples, establishes the all-u statement.

No empirical array, photon calculation or parent numerical helper is used.
These checks do not assert that the future parent implementation reproduces
the derivation; that implementation is outside this source freeze.
