# Independent equal-time covariance lift

Frozen before reading any new root covariance derivation. This check uses only the previously frozen momentum and Euler equations in WORKING_v1 and STATISTICAL_INPUT_v1. It supplies an independent algebra/rank check, not a new observational result or certification of the full perturbation system.

**Outcome:** yes, adding the equal-time Weyl auto-power and its total first derivative permits an exact finite reconstruction without a common-transfer assumption. Five suitably independent mode/shell rows are sufficient through a linear lift with two nonlinear compatibility checks. The required rank is attainable with unrestricted scalar initial states; it is not guaranteed for an observed ensemble. Five is a sufficient construction, not a minimality claim.

## 1. Eliminate the slip field before taking moments

Use physical N=ln a_J, h=H_J′/H_J, E=H_J/H0, K=k_com/a_J and

    V=H_J v_J,  lambda=K^2/H_J^2,  W=lambda V,
    J=3 exp(-3N)/E^2,  T=Psi-Phi,  S=Psi+Phi.

All derivatives hold the comoving Fourier label fixed. The Fourier amplitudes may be complex. The common-background coefficients x=F′/F, y=x/q and R are real. The frozen equations imply

    S′=-(1+x/2)S-(y/2)T-J R V,                         (1)
    V′=h V-(S+T)/2.                                    (2)

For (2), lambda′/lambda=-2(1+h). Substituting W=lambda V in W′+(2+h)W=-lambda Psi gives V′-hV=-Psi. No small-scale or quasistatic approximation is involved.

Define temporary common coefficients

    alpha=1+(x-y)/2,  gamma=J R+h y.

Eliminating T from (1)–(2) gives the field identity

    S′-y V′=-alpha S-gamma V.                           (3)

The scalar homogeneous state is still present through V′; it has not been fixed or discarded.

## 2. Total covariance derivatives remove the unknown leg

Let C_AB=Re E[A B*] with a fixed ensemble, and suppose the stated N derivative commutes with this expectation. In this subsection abbreviate

    A=C_SS,  B=C_SV,  C=C_VV,
    U=C_S(V′),  Z=C_V(V′).

Here A denotes a covariance, not the conformal factor. Real cross covariance is symmetric, so the product rule and (3) give

    A′=2y U-2alpha A-2gamma B,
    B′=U+y Z-alpha B-gamma C,
    C′=2Z.                                             (4)

The two nuisance time-leg moments U,Z can be eliminated without dividing by y:

    A′/2-y B′+y^2 C′/2
      +alpha A+(gamma-alpha y)B-gamma y C=0.            (5)

In particular, the extra A′ is genuinely new information. It does not follow from the diagonal C_SV and C_VV data used in the earlier admission check. Equation (5) removes the need to supply C_(S′)V separately for this inverse, while replacing it with the Weyl auto-power/derivative and additional rank obligations.

## 3. Five-row lift and physical reconstruction

At one common epoch define measured rows

    L_i=[A_i, -B_i′, C_i′/2, B_i, -C_i],
    d_i=-A_i′/2.

The five lifted unknowns are

    z=(alpha, y, y^2, gamma-alpha y, gamma y),  L z=d.   (6)

If five rows make L invertible, solve z=L^-1 d, then require the exact compatibility identities

    z_3=z_2^2,
    z_5=z_2 (z_4+z_1 z_2).                             (7)

These are substantive checks: an arbitrary five-dimensional linear solution is not automatically a three-parameter physical solution. With one-based indices,

    y=z_2,
    alpha=z_1,
    gamma=z_4+z_1 z_2,
    x=2alpha-2+y,
    R=(gamma-h y)/J.                                   (8)

Thus any solution of the physical equations is unique on this full-rank chart. Conversely, (7) makes the solved lift a solution of the eliminated covariance equations. It does not establish the rest of the background/scalar dynamics or candidate action membership. Require J>0, R>0 and, on a rolling coupling chart, y!=0 and q=x/y>0. The candidate’s additional q/beta/F/potential conditions remain separate.

A sixth or later row is a reserved no-refit covariance identity. A whole-history inference must additionally test R′/R=-x and the background equations already stated by the author. If y=0, the field equations may still determine x=0 and R, but q is not fixed by x/y. Rank failure or poor conditioning is an unclosed inference problem, not model exclusion.

## 4. Full rank is attainable with free scalar states

A useful witness uses the three real initial variables (S,V,V′). At a fixed physical background choose five independent mode preparations with covariance

    Sigma_i = epsilon^2 [t_i t_i^T + delta I_3],
    t_i=(r_i,1,w_i),  delta>0,  epsilon>0,
    (r_i,w_i)=(-1,0),(-2,0),(-3,0),(-1,1),(-2,1).

Every Sigma_i is positive definite. It can be realized using bounded, independent, zero-mean unit-variance random signs, so Gaussianity or unbounded fluctuations are unnecessary. Scale epsilon down to keep every realization perturbatively small. The total first derivatives are those of (3), not chosen independently of the equations.

For epsilon=1,

    A_i=r_i^2+delta, B_i=r_i, C_i=1+delta,
    U_i=r_i w_i, Z_i=w_i,
    B_i′=(r_i+y)w_i-alpha r_i-gamma(1+delta), C_i′=2w_i.

The determinant of the resulting L, in the displayed row order, is exactly

    det L = 2(1+delta).

Restoring the amplitude gives det L=2(1+delta)epsilon^10, which remains nonzero for epsilon>0. This is independent of the actual finite alpha,gamma,y. Also C_VV>0 and C_SV<0 in this construction, so the normalized positive-P chart can be used if desired; the lift itself does not need that division.

These initial covariances are attainable inside the supplied perturbation initial-value model. With b!=0, equation (2) gives T=2hV-S-2V′ and X=T/(2b); S gives phi=S/2 and V gives the finite dust velocity. The frozen 00 constraint solves the particle-number contrast n for every choice of these states and every finite independent Z_scalar=delta chi_dot, because rho>0. Thus arbitrary scalar velocity data need not be selected to obtain the witness. This is a local constraint-compatible preparation argument; no observationally realized rank, long-time linearity or synthetic ODE history is asserted.

## 5. What this closes, and what it does not

The missing separate time-leg derivative can be removed from the ideal common-coefficient inverse when all three same-time powers and their total derivatives are supplied with sufficient independent rows. No deterministic common transfer has been assumed. The earlier two-variable rotation illustration remains an information counterexample for covariance data without the common dynamical/row-rank conditions; it is not a counterexample to (5)–(8).

The new data burden is substantial and explicit: calibrated physical C_SS, C_SV, C_VV and their first N derivatives at a common time/fixed comoving modes, common h,J, and a demonstrably well-conditioned five-row matrix. Angular lensing auto-power is not already the required unprojected C_SS history. Redshift/scale windows, noise and derivative uncertainty still require a forward measurement model. No additional literature search, survey fit or empirical validation was performed here.

`COVARIANCE_CONTROL_v1.py` is an independent exact SymPy check. It checks both the eliminated-field route and a separate moment derivation from the original S,T,V equations; verifies the positive-definite witness, determinant and full lift recovery; and includes explicitly labelled wrong-sign/factor and incompatible-lift controls. Its saved result is 39 matched checks and zero failures. This is a narrow algebraic control count, not independent empirical evidence or a formal proof certificate. No author helper or ODE was used.
