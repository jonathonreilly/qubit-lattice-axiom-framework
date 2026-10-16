# Scalar coefficient constraints from ideal shear and radial velocities

**Date:** 2026-10-15
**Status:** conditional-support
**Claim type:** bounded_theorem
**Primary runner:** [scalar_projected_covariance_check.py](../scripts/scalar_projected_covariance_check.py)

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: revised_scalar_action_potential_scale
target_blocker_text: Derive or eliminate the remaining scalar action, state, scale and measurement assumptions
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: Necessary coefficient constraints from ideal continuum shell correlations under the stated linear field law and measurement geometry
hypothetical_axiom_status: none proposed
admitted_observation_status: Primary-source measurement context only; no measured correlation history or independent empirical test
claim_type_reason: A projection and elimination theorem with explicit geometry, statistics, smoothness and field-law premises
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: Establish which finite source and velocity windows can supply a weak constraint, or expose their missing functional without choosing a prior history
```

**Exact target.** Under the hypotheses below, derive a necessary scalar
coefficient constraint using equal-radius shear/velocity correlations, without
reconstructing a velocity potential, choosing its radial boundary value,
setting missing angular modes to zero, or specifying a common transfer or
initial covariance. The theorem is an implication, not a converse or an
observational detection. Its five-row inverse additionally requires rank and
physical-chart admission. No action, potential, scale or ensemble is selected.

Root personally derived the ordered elimination and implemented the controls.
The standard Born inversion, velocity Hessian and integration-by-parts facts
are not claimed as discoveries. The combined construction has focused
independent checks; no global literature-priority claim or formal audit is made.

## 1. Observations and exact hypotheses

Use c=1 and physical Jordan coordinates, with
`ds²=a²[-(1+2Psi)deta²+(1-2Phi)dx.dx]`. Set `S=Phi+Psi`, `N=ln a`,
`H=dln a/dtJ`, `h=H_N/H`, and `V=H vJ`, where the scalar peculiar velocity is
`v_phys=grad_x vJ/a`. A measured radial velocity would be
`u=n.grad_x V/(aH)`, a spatial derivative at fixed emission time.

The geometry assumes a calibrated, spatially flat expanding background,
`chi_N=-1/(aH)`, first-order scalar perturbations, Born lensing, full-sky
angular correlations and continuum source distances. Require sufficiently
smooth, real, homogeneous and isotropic signal covariances; derivatives and
expectations must commute. Work on an open domain `0<r<2chi(N)`, with chi>0.
Noise, selection, intrinsic alignment, calibration and relativistic corrections
must already be accounted for. These are supplied premises, not derived data.
No Gaussianity, growing-mode or common stochastic transfer is assumed.

For the sum potential the Born convention is

    psi(s,n)=integral_0^s [(s-chi)/(s chi)] S_LC(chi,n) dchi,
    gamma_E,lm=0.5 sqrt[(l-1)l(l+1)(l+2)] psi_lm,  l>=2,
    S_LC(s,n)=partial_s[s² partial_s psi(s,n)].             (1)

The last line follows by differentiating the integral twice; regular angular
modes justify the observer endpoint. It returns S, not S/2. The radial
operator also kills foreground integration terms A(n)+B(n)/s on an interior
continuum interval. Applied to a covariance, (1) differentiates each shear
source argument before restricting to equal distance. Shear does not supply
l=0,1. A finite mask introduces additional nulls not treated by this theorem.

[Taylor v1, Eqs. 3–18](https://arxiv.org/pdf/astro-ph/0111605v1)
provides the corresponding flat-Born inverse in its single-potential
convention. [Heavens v2, Secs. 2.3–2.5](https://arxiv.org/pdf/astro-ph/0304151v2)
explicitly includes source-distance mixing, masks and shape noise. Those
papers do not supply this theory's observed continuum correlations. Their
Poisson/growth forecasts are not imported here.

For sources at chi n1 and chi n2, put mu=n1.n2 and
`r=chi sqrt[2(1-mu)]`. After mapping shell data to (N,r),

    partial_N|r = partial_N|mu
                    +2(1-mu)(chi_N/chi) partial_mu.       (2)

This follows by differentiating r at fixed angle; the angular term cancels
that change. Fixed-angle, fixed-multipole and fixed-comoving-separation
derivatives are different operations. Equation (2) concerns ensemble
correlations, not repeated measurements of an individual object.

## 2. Potential elimination and missing angular modes

Let C_AB(N,r) denote equal-time spatial covariances. Differentiating the
isotropic scalar correlation with respect to the two Cartesian positions gives

    C_Su = r C_SV,r/(2aHchi),
    a²H² C_uu = alpha C_VV,rr -(1-alpha)C_VV,r/r,
    alpha=r²/(4chi²).                                    (3)

The opposite signs of the two separation derivatives and
`n1.rhat=-n2.rhat` give the velocity auto-correlation sign. Radial velocity
is not dV_LC/dchi. The radial pair geometry agrees with
[Wang et al. v1, Secs. 3–5](https://arxiv.org/pdf/1808.07543v1).
At a single radius and separation their two arbitrary-vector-covariance
statistics have rank one. We instead use the scalar-flow differential relation;
we do not claim to measure both arbitrary vector components separately.

Define operators, acting on everything to their right, by

    D=partial_r/r, K=r partial_r,
    E=alpha(K+2)-1, P=(K+2)K(K-2)(K-4), Qop=P E² D,
    d=2aHchi C_Su/r²=D C_SV, U=a²H² C_uu=E D C_VV,
    g=-2chi_N/chi=2/(aHchi), E_N=g(E+1).                  (4)

In particular E and P do not commute. Differentiating U and applying E gives

    E U_N-g(E+1)U=E²D(C_VV,N).                            (5)

Thus no integration constant is needed to form the following six inputs:

    A=Qop C_SS,           A1=Qop(C_SS,N),
    B=P E² d,            B1=P E²(d_N),
    C=P E U,             C1=P[E U_N-g(E+1)U].             (6)

A1, B1 and C1 are not ordinary derivatives of A, B and C. They all apply the
same spatial operator Qop to the underlying three scalar covariances or their
total equal-time derivatives. The nonzero kernel
`f=r^-2 exp(-2chi²/r²)` satisfies E f=0: a direct inversion of E would require
additional domain information. This is an operator-kernel example, not a claim
that f itself is a globally positive covariance spectrum.

An omitted l=0,1 contribution to a full-sky angular correlation has form
`a(N)+b(N)r²`. Consequently the ambiguities in C_SS, d and U are respectively
`a+b r²`, `a/r²+b`, and `a+b r²`. Applying (6) sends them to linear combinations
of r^-2, 1, r² and r⁴ before P; P kills each. For example
`E²(1)=8alpha²-4alpha+1` and `E²(r^-2)=r^-2`. Time derivatives preserve this
finite nuisance span when the changing E is treated as in (5). All six inputs
are therefore unchanged by those omitted modes. This does not restore the
modes, extend to an arbitrary mask, or guarantee nonzero rank. The processed
A,B,C need not form a positive semidefinite covariance matrix.

## 3. Conditional field law and coefficient identification

The dynamical premise is the following common, spatially uniform coefficient
law for each realization, with an otherwise arbitrary field T:

    S_N=-(1+x/2)S-yT/2-mV,
    V_N=hV-(S+T)/2.                                      (7)

Elimination gives `S_N-y V_N=a0 S+c0 V`, where
`a0=(y-x-2)/2`, `c0=-h y-m`. This states the exact premise of the theorem;
it is not derived from shear. For a supplied canonical scalar with universal
conformal dust, `F=Q/Aconf²`, `q=2Q(dln Aconf/dvarphi)²`,
`x=F_N/F`, `y=x/q`, `m=JR`, `J=3exp(-3N)/(H/H0)²`.
The full action/equation derivation and meanings of R,T are in the
[preceding dynamical note](SCALAR_DYNAMICAL_MOMENTUM_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-15.md).
Nothing here assumes that a fitted coefficient history obeys all those field equations.

Multiply (7) at one point by S-yV at the other and use exchange symmetry of
real isotropic scalar covariances. The separate cross-time-leg derivatives
cancel, giving

    (C_SS,N-2y C_SV,N+y² C_VV,N)/2
       =a0 C_SS+(c0-a0y)C_SV-c0y C_VV.                  (8)

Apply Qop; its coefficients are spatial and the dynamical coefficients depend
only on N. At each radius the observable necessary constraint is

    [A/2, -A/2-B1+(h-1)B, C1/2+B/2-hC, B, -C]
      .[x,y,y²,m-xy/2,my] = -A1/2-A.                    (9)

This proves the target implication, including (5) and angular-null immunity.
Five linearly independent rows are sufficient to solve the lifted five-vector.
A proposed scalar interpretation must satisfy z3=y²,
`z5=(z4+xy/2)y`, `m=z4+xy/2`, and the required domain gates
`R=m/J>0`, `y!=0`, `q=x/y>0`. These conditions are not a full-history converse.
The necessary relation (9) itself uses no division by y; reconstruction of q
fails at y=0. Neither rank nor numerical stability is automatic.

A manufactured five-shell homogeneous/isotropic ensemble gives a rank witness.
Its spectrum consists of five j0(kr) shells with positive definite 3x3
(S,V,T) covariance matrices, realizable by bounded amplitudes with uniform
phase and direction. The event is x=3/50, y=2/5, m=28/15, h=-2/7, chi=3;
k=(.4,.8,1.2,1.6,2), r=(.5,1,1.5,2,2.5), with r=3 reserved.
The independent proof expands j0 through degree 72, bounds the remaining
series and obtains `||Mrounded^-1||inf ||M-Mrounded||inf <6.24e-23<1`.
This proves rank for that exact synthetic matrix; it does not prove observed
rank. Its induced infinity condition number is about 6.32e9. High-precision
recovery in this fixture is not useful measured precision.

## 4. Weak constraints and error pricing

Let w(N,r) be smooth with compact support strictly inside the domain, and use
measure dN dr. Integration by parts gives

    K*=-K-1, P*=(K-1)(K+1)(K+3)(K+5),
    D*w=-partial_r(w/r), E*w=-alpha r partial_r w-(alpha+1)w.

Set `L*w=(E*)² P*w`, `Q*w=D*L*w`. After radial then time integration by parts,
(8) implies `integral(K_SS C_SS+K_Su C_Su+K_uu C_uu)dNdr=0`, with

    K_SS=-0.5 partial_N(Q*w)-a0 Q*w,
    K_Su=(2aHchi/r²)[partial_N(y L*w)-(c0-a0y)L*w],
    K_uu=a²H²{-partial_N[(y²/2)E*P*w]
                -(y²g/2)(E*+1)P*w+c0y E*P*w}.            (10)

The derivatives now act on the supplied geometry, proposed coefficient
histories and test weight. Coefficients cannot be replaced by their central
redshift values without an additional approximation/error bound. The result
is still necessary only. It does not require a potential boundary condition.

A finite-regularity alternative is a FIXED interior rectangle with w through
radial derivative six zero at radial boundaries and all needed radial jets
zero at time endpoints. With moving radial limits an additional time flux
survives unless imposed zero or explicitly retained. Its boundary density is
`0.5 Q*w C_SS-y L*w d+0.5 y² E*P*w U`, multiplied by minus the upper boundary
speed and plus the lower speed. Vanishing through derivative seven is one
sufficient stronger choice. The primary compact-support statement avoids it.

Separately justified envelopes `|delta C_i|<=epsilon_i` give the rigorous
residual error bound `sum_i integral |K_i|epsilon_i dNdr` by the triangle
inequality. The bound holds for fixed kernels. Uncertain geometry, coefficient calibration or other kernel inputs require their additional kernel-error and cross terms. No epsilon, cosmic variance or noise independence is supplied.
Large derivative kernels can still amplify errors severely. Moreover C_SS
and C_Su still require (1) on each relevant source leg. For finite source bins,
the desired functional must be represented by their calibrated window span
on an explicitly admitted signal space. An equal-epoch diagonal of a
continuous two-source covariance is not supplied by interpolation alone.

## 5. Verification, failures and remaining imports

The paired primary performs exact operator/Cartesian/lensing checks, a
high-precision synthetic inverse, a separate exact two-dimensional weak-form
fixture and full supplied scalar/dust evolution on two synthetic backgrounds.
Five comoving shells, three independent initial vectors per shell and five
epochs yield sixty projected rows. Initial scalar momentum is free; only the
initial 00 constraint sets the density. The evolving distance obeys
`chi_dot_E=-1/aE` to a declared observer endpoint. The forward projection uses
algebraic representations of the same operator; it is not a second independent
numerical projection implementation. The supplied candidate equations and
potential are test inputs, not inferred theory or calibration.

The rolling rows have scaled identity residuals below 2.2e-14, while the
row-scaled matrices reach condition numbers about 7.9e12 and coefficient errors
about 2.1e-4. These diagnostics establish neither uniform time-domain rank nor
survey usability. No assertion suppresses this inverse degradation. The
unmeasured signal histories, instrument response, velocity zero point, H/chi
calibration, homogeneity/isotropy and signal/noise separation remain imports.

Focused independent evidence is recorded in the campaign pack: a blind
23-control compatibility derivation, 13 subsequent operator/rank comparisons,
a separate 25-control weak calculation, and a 43-control primary-source
projection derivation. Counts are distinct internal checks, not independent
empirical experiments. The weak reviewer read the proposed equations before
rederiving them; the geometry and primary-source derivations froze before
reading the working construction. The complete reports state their limits.

Preserved failures include the initial literal SymPy Subs comparison failure
(17 pass, 1 fail; the general chain-rule coefficient cancels), a wrongly labeled
entrywise matrix norm repaired to an induced norm, a real moving-boundary
qualification repaired without changing (10), NumPy bool JSON serialization,
and ordinary-polynomial integration failures on valid Laurent terms in the
root and independent weak checkers. No physical case, threshold or failed
scientific result was removed to obtain a pass.

This retires the need to prescribe a velocity-potential integration value or
l=0,1 covariance for this necessary test. It does not retire a field action,
initial cosmological state, potential, absolute scale, environment or actual
measurement/noise supplier. The next discriminator is whether actual finite
windows determine a useful member of (10), with calibrated error control.
The scope checklist (`.claude/science/physics-loops/observations-backward-24h-20261014/projected_covariance/NO_GO_DISCIPLINE_CHECKLIST.md`)
and campaign handoff preserve alternatives; no universal no-go is asserted.
