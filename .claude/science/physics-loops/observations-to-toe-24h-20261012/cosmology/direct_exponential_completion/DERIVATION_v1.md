# Positive exponential completion of the observed-history candidate

Parent /root authors this alternative. It is a new potential, not a more
accurate evaluation of the original potential. Original stiff failures remain
failures. Observations and original candidate results are already exposed;
this is model development. The thermal gas, masses, physical normalization,
kinetic metric and universal matter coupling are held fixed.

Use the original three-field Einstein kinetic metric K and coupling C_B,
with a=(1-k)(1+3k)/4, b=k, s=(1+k)/(k(1-3k)), alpha=sqrt(a),
E=exp(2 alpha u), F=1+sE and D=1+2(1+b)(x²+y²)/3:

    K=diag(J/F²,(1+s)4b/(9FD),(1+s)b/(3FD)),
    J=1+(1-3a)sE, C_B=(1+s)E/F, alpha_B=alpha/F.

The normalized local action is Q(k) integral sqrt(-g_hat)
[R_hat/2-K_AB partial(phi_A)partial(phi_B)-2 H_v² U_exp]
+ S_m[C_B g_hat,psi], with Q(k)=Q0(1+k). The matter stress contains the
dynamical gas/dust, while the constant vacuum contribution is in U_exp.
The action, gas history, Q0,H_v and initial state are supplied assumptions.

Define fixed positive exponents in each model:

    lambda_x=2 alpha(1+s b)/(b(1+s)), lambda_y=4 alpha s/(1+s),
    U_exp=3/2+3s(E-1)²/(2F²)
           +(b/2)x² exp(-lambda_x u)+(b/3)y² exp(-lambda_y u)
           +nu(1+s)u²/(2F²), nu>0.

All added terms are nonnegative, so U_exp>=3/2 at all finite real fields.
The kinetic coefficients remain positive for0<k<1/3. This is a classical
finite-field statement; no uniform lower kinetic bound or quantum result.

At u=0, the potential and its full first gradient agree exactly with the
original curvature-fluid potential:

    U_exp=3/2+b x²/2+b y²/3,
    U_x=b x, U_y=2b y/3,
    U_u=-alpha(1+s b)x²/(1+s)-4alpha s b y²/(3(1+s)).

Thus the same ideal u=0, p_u=0, x∝a_J^(-3/2),y∝a_J^(-2) solution remains
a solution of the complete homogeneous equations under its original ideal
fluid matching. This follows from equality of the kinetic metric, potential
and first derivatives on that orbit, not from copying an old trajectory for
a different action. The new second derivatives differ away from the vacuum;
full perturbations and actual thermal histories must be recomputed.

## A different weak limit

For k→0 with fixed bounded u,x,y and velocities (no u=k²v restriction), put
t=exp(-u), D0=1+2(x²+y²)/3. Then

    K/k -> t diag(1/4,4/(9D0),1/(3D0)), alpha_B/k -> t/2,
    C_B=1+k(1-t)+O(k²),
    (U_exp-3/2)/k -> W
       =3(1-t)²/2+t²(x²/2+y²/3+nu u²/2).

These limits are uniform on fixed compact field/velocity sets. The
denominators after multiplying by k are positive and smooth at k=0.
Consequently U_exp,uu/K_u has a finite fixed-state limit W_uu/(t/4).
This removes the original x²/k² potential-curvature contribution in this
new candidate. It does not prove stability or bound the full evolving modes.
The new scaling allows finite u and p_u; the old narrow weak-limit theorem
is not used as its trajectory approximation.

Let sigma0=R0 rho_J and H_GR²=1+2sigma0/3. The instantaneous physical
constraint has the expansion H_J²/(H_v² H_GR²)=1+k C_exp+O(k²), where

    Tbar=t[p_u²/4+(4p_x²/9+p_y²/3)/D0],
    C_exp=2[W+sigma0(1-2t)]/(3H_GR²)+Tbar/3+t p_u-1+t.

This follows by expanding sigma=C_B² sigma0/(1+k), the Friedmann
denominator3-Kp² and the readout factor(1+alpha_B p_u)²/C_B. At ideal
u=p_u=0 and matched fluid/scalar state it reduces to the prior vanishing
first correction. The conditional weak-body G_N ratio tends to1, with its
first correction cancelling: C_B(1+alpha_B²/K_u)/(1+k)=1+O(k²).
No assertion of solution convergence is made from these coefficient limits.

## Frozen numerical block

Compute the full changed action and new gradients, not the old force. Use
the same entropy clock, collisionless neutrino distribution, fixed masses,
T0,H0 and dust calibration as direct_thermal_matter_bridge. Integrate three
split models k=.01,1e-5,1e-6, each baseline128-node gas and refined256-node
gas; initial [u,X,Y,p_u,vx,vy]=[0,1,1,0,-1.5,-2]. No parameter or initial
state is fitted. Baseline DOP853 rtol1e-9,atol1e-11,max L step.025;
refinement1e-10,1e-12,.0125;241fixed temperature sites; per-case wall cap120s.
Require complete positive-chart evolution and compare scaled states within
3e-6 between these two runs. This internal refinement bound is not empirical
acceptance. Preserve all incomplete/failed runs and error values.

Before histories, compare analytic derivatives and full lowered-momentum
accelerations to independently differentiated80digit action evaluations at
three temperatures and three off-orbit states, with3e-9 scaled RHS bound.
Test exact ideal-orbit first-jet agreement and small-k coefficient limits.
Independent full-path reproduction is requested using a different solver
and momentum/gas implementation. No galaxy, quantum or TOE closure follows.
