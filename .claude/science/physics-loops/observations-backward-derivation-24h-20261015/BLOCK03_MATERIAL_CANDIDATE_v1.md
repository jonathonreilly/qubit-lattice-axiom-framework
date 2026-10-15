# Material stress transport and a regular-center reconstruction family

Root provisional derivation, 2026-10-15. This extends the inverse to known
material stress and tests whether regular-center smoothness selects its remaining
normalization. It is a constructed family, not an observed universe, a selected
potential or an empirical exclusion. Independent checking is still pending.

## Known stress transports, but does not specify, a boundary value

Use the same candidate gravitational action and physical metric as block 01,
writing Z(F)=omega(F)/F. A static material stress tensor is
T^mu_nu=diag(-rho,p_r,p_t,p_t). With the previously derived metric quantities
a=G^theta_theta-G^t_t and d=B(1/r-N'/N), the angular-minus-time equation is

    F a=(rho+p_t)+d F'.

On d!=0, put u=a/d, s=(rho+p_t)/d and
M(r)=exp integral_(r0)^r u(t)dt. Exact integration gives

    F(r)=M(r)[F(r0)-integral_(r0)^r s(t)/M(t)dt].       (1)

Thus a genuinely connected, measured metric-and-stress interval transports one
normalization affinely. It need not leave one independent C for each subinterval.
It still contains F(r0), and neither disconnected environmental profiles nor an
unmeasured stress can be replaced by this transport law. Supplying a chosen
F(r0) would supply the missing boundary condition. This observation is a positive
solution formula, not a universal impossibility claim about other measurements.

Let ell'=N'/N and K=Z B F'^2. Where F'!=0, the remaining inverse is

    K=F(Gr-Gt)-(rho+p_r)-B F''-(B'/2-B ell')F',
    Z=K/(B F'^2),
    V=-F Gt-rho-K/2-B F''-(B'/2+2B/r)F'.             (2)

The independent material conservation condition is

    p_r'=-(rho+p_r)ell'+2(p_t-p_r)/r.

When the material equations hold, this conservation law and the metric equations
imply the scalar equation on a nonconstant chart; the candidate below will also
be substituted into the scalar equation directly. A conserved tensor alone is
not presented as a derivation of its underlying material action or state.

## Explicit matter and regular geometry

As a controlled matter model, take irrotational dust with multiplier lambda:

    S_m=-1/2 integral sqrt(-g) lambda[(partial T)^2+1].

Variation in lambda enforces (partial T)^2=-1; variation in T gives
div(lambda grad T)=0. On this constraint its stress is
T_mu_nu=lambda partial_mu T partial_nu T. This is an explicitly chosen matter
action for the construction, not a derivation of actual matter. Set T=t and
lambda=rho0>0. In the static metric

    N=1, B=1-k r^2, k>0, 0<=r<R, k R^2<1,              (3)

both dust equations hold and T^mu_nu=diag(-rho0,0,0,0).
The density is a material-state input. The metric is smooth at the center:
B(0)=1, N is constant, and its spatial Cartesian components are regular.
No exterior matching, infinite history or stability statement is made.

Here Gt=-3k, Gr=Ga=-k, a=2k, d=B/r. Choosing the normalized homogeneous
solution M=1/B in (1) yields the following entire candidate family:

    rho0 R^2/2 < C < rho0/(2k),
    F_C(r)=(C-rho0 r^2/2)/(1-k r^2),
    Z(F)=3k/(rho0-2kF),
    V_C(F)=rho0/2+3(rho0-2kF)^2/[2(rho0-2kC)].          (4)

Every C in that nonempty interval gives positive F on the ball and
0<F<rho0/(2k). With A=2kC-rho0<0,

    F'=A r/B^2,
    K=-3k A r^2/B^2,
    Z(F_C)=-3kB/A>0,
    2omega+3=2FZ+3=3rho0/(rho0-2kF)>0.                 (5)

F is monotone on r>0. Its smooth even extension has F'(0)=0; the explicit
Z(F) and V_C(F) remain finite at F=C, so the action and field equations have
regular limits at the center. The vacuum inverse's division by F' is not used
there. Both metric curvature and scalar derivatives stay finite on every closed
ball of radius smaller than the stated R.

Equations (2) give exactly (4): in particular, A/B=2kF-rho0 and

    V=3kF-rho0-3A(1+B)/(2B^2)
     =rho0/2-3(2kF-rho0)^2/(2A).

Substitute into the scalar equation

    R4/2+Z box F+(Z_F/2) B F'^2-V_F=0, R4=6k.

All terms are explicit rational functions of r,k,rho0,C, including their
regular center limits. This is the proposed exact check, not a numerical fit.

## What this construction actually varies

The same metric (3), same positive dust density and same proper-time dust flow
occur for every C. The kinetic function Z(F) is the same. The potential's
coefficient and scalar central value vary together with C. These are different
candidate actions, not a symmetry transforming solutions of one fixed action.
Changing only the profile C at fixed V_C is an off-shell mutation to test.

Static clocks, radial null timing and the stationary zero-speed geodesics of
this metric are the same across the family. The construction supplies no
nonzero-speed circular-orbit observation. It is enough to expose a regular
local material example with alternative action reconstructions; it is not a
theorem of indistinguishability under all perturbations or other experiments.

Regularity, known dust stress, positive F, positive kinetic terms and this
static metric therefore coexist in the displayed family. Declaring one C
selected would go beyond this construction. A specified global potential,
material response, boundary matching or additional measured disturbance could
constrain it, but none has been derived here. No action-selection, initial-state
or absolute-scale import is counted as retired.

## Planned verification and next question

Directly substitute all members into the temporal, radial, angular and scalar
equations, the dust constraints and continuity equation; check the center
limits and positive-kinetic identity. Test changed C at fixed potential and
changed source density as explicit mutations. An independent reduced-action
or other independent calculation is needed before reuse.

Next: determine whether an independently measured material perturbation can
distinguish members of this family without choosing its preparation history or
source response. This positive-response calculation would be a distinct route;
the present example does not exclude it.
