# Independent unequal-shell projection and compatibility

This proof was frozen before opening any new root unequal-window derivation or implementation. Root remains scientific author. The only problem inputs are the supplied leg-one field law and homogeneous/isotropic scalar-flow geometry; the previously reviewed M15 note is context, not evidence for the new algebra. No observations, physical calibration, covariance state or boundary value is selected. The exact controls below are synthetic mathematical fixtures, not an empirical test or formal audit.

## Geometry and time slots

Write x=chi(N1)>0, z=chi(N2)>0, mu=n1 dot n2, r=|z n2-x n1|, and d_i=a_i H_i. Use an open noncollinear triangle chart

    |x-z| < r < x+z,   mu=(x^2+z^2-r^2)/(2xz).

Both time arguments are independent. Let K_AB(N1,N2,r) be connected unequal-time covariances of smooth homogeneous/isotropic scalar fields; assume the needed derivatives exist and commute with expectation. The identities also hold for uncentered moments when these operations are justified. The velocity observable is supplied as u_i=n_i dot grad V_i/d_i, with the gradient a spatial derivative at fixed time, not a derivative along the light cone. Assume d_i is known and nonzero.

For e=(x2-x1)/r define

    b1=(x-z mu)/r=(r^2+x^2-z^2)/(2xr),
    b2=(z-x mu)/r=(r^2+z^2-x^2)/(2zr).

Thus n1 dot e=-b1 and n2 dot e=b2. Spatial differentiation gives

    C_S1u2 = b2 K_SV,r / d2,
    C_u1S2 = b1 K_VS,r / d1,
    d1 d2 C_u1u2 = p K_VV,rr + ell K_VV,r,
    p=b1 b2=[r^4-(x^2-z^2)^2]/(4xz r^2),
    ell=-(mu+p)/r=-xz(1-mu^2)/r^3.

The last sign follows directly from grad_1 grad_2 K=-Hess_r K. In particular its coefficient of K_rr is positive b1 b2, which itself need not be positive on unequal shells. The controls independently differentiate a Gaussian covariance in six Cartesian coordinates and agree with this expression.

A light-cone angular covariance is Ktilde(N1,N2,mu)=K(N1,N2,r(N1,N2,mu)). The fixed-spatial-position time derivative of the homogeneous/isotropic covariance is the partial derivative at fixed r. At leg one,

    partial_1|r = partial_1|mu + x' (x-z mu)/(xz) partial_mu.

This follows from r_1|mu=x' b1 and r_mu=-xz/r. For a flat FLRW past light cone x'=-1/d1. The correction is a one-leg derivative; it is not the simultaneous equal-shell time derivative. Derivatives of d1 and of the projection factors must also be retained when differentiating normalized measured correlations.

## A local compatibility pair without a potential boundary

To avoid the problem's two uses of a, denote its field-law coefficients by alpha(N1), gamma(N1):

    S_1,N - y(N1) V_1,N = alpha(N1) S1 + gamma(N1) V1.

Multiply by V2, average, then differentiate in r. Put

    F=K_VV,r,
    h=K_SV,r=d2 C_S1u2/b2,       [requires b2 != 0 on this chart]
    H=(partial_1-alpha)h,
    U=d1 d2 C_u1u2,
    E=p partial_r+ell,
    L=y partial_1+gamma.

The supplied field law and projection imply the two equations

    E F=U,             L F=H.                                  (1)

Coefficients y,gamma depend only on time, so they commute with E. Geometry does not commute with the time derivative:

    L U-E H = y E_1 F,
    E_1=p_1 partial_r+ell_1.                                    (2)

All subscript-1 coefficient derivatives in this proof hold r,N2 fixed. Let

    J=L U-E H,
    Delta=y(p ell_1-p_1 ell),
    G=p J-y p_1 U.

Eliminating F_r between E F=U and (2) gives the exact algebraic identity

    G=Delta F.                                                 (3)

Hence on an open chart where Delta != 0 the data-derived expression F*=G/Delta must satisfy both E F*=U and L F*=H. Equivalently, the two denominator-cleared necessary compatibility residuals are

    p Delta G_r + (ell Delta-p Delta_r)G - Delta^2 U = 0,        (4a)
    y Delta G_1 + (gamma Delta-y Delta_1)G - Delta^2 H = 0.      (4b)

Neither expression contains an undetermined covariance derivative or an integration boundary value. Identities (3)-(4) follow without division by p, so p=0 by itself is not a failure of this reconstruction. The cleared identities remain necessary even where Delta=0, although there they can lose information.

On a regular chart these two tests are sufficient only for existence of the auxiliary derivative F satisfying the reduced pair (1): set F=G/Delta and substitute. They are not sufficient for a globally positive covariance, a full stochastic field solution, both field-law time legs, an observational reconstruction or a selected cosmic state. Integrating F to K_VV still leaves time-dependent constants, and global covariance positivity is a separate obligation. The present result is a necessary implication for supplied candidate coefficients and ideal correlations, not their identification from finite data.

An additional simple necessary relation is available if C_S1S2 and the reverse cross correlation C_u1S2 are supplied: set g=K_SS,r and h21=d1 C_u1S2/b1 on b1 !=0, then (partial_1-alpha)g=L h21. This separate relation does not replace the VV compatibility pair or reconstruct missing shear modes.

## Geometric and coefficient degeneracies

A direct differentiation gives

    p ell_x-p_x ell = [2z mu-x(1+mu^2)]/r^3,
    Delta = y x' [2z mu-x(1+mu^2)]/r^3.                         (5)

For x>=z the bracket is strictly negative in -1<mu<1. For x<z it vanishes at the interior angular value

    mu*=(z-sqrt(z^2-x^2))/x.

Thus a real interior rank-loss surface exists, not just coincident or collinear limits. Exact example: x=3,z=5,mu=1/3,r=2 sqrt(6), with b2 nonzero. At x=z the partial-leg determinant tends to -r/(4x^3), not zero. This does not identify a one-leg derivative from an equal-time diagonal alone.

The cross-projection gate b2!=0 is independent: x=5,z=3,mu=3/5,r=4 has b2=0 but a nonzero commutator determinant. Conversely x=3,z=5,mu=3/5,r=4 has p=0 while p ell_x-p_x ell=3/100. The construction correctly avoids dividing by p. The triangle endpoints, observer radii zero and coincident r=0 lie outside this coordinate chart. Nearby small |b2| or |Delta| causes instability; no precision or finite-noise assertion follows from a nonzero denominator.

If y vanishes identically on an interval but gamma!=0, (1) instead supplies F=H/gamma and the separate test E(H/gamma)=U. If both y and gamma vanish, H=0 is necessary and the field law supplies no F through that equation. If x'=0, the geometry commutes with the time leg and L U-E H=0 remains necessary, without this algebraic recovery. Isolated zeros or a geometric rank-loss surface require an affected chart/continuation analysis; the result does not declare them a universal information-loss theorem. Other observations or higher derivatives may supply different tests.

## Missing shear ell=0,1 are not automatically cancelled

The derivation above assumes the actual scalar-potential cross correlation. If the S leg is supplied only by full-sky shear inversion, its absent ell=0,1 can change C_S1u2 by A(N1,N2)+B(N1,N2)mu. Under the cross normalization this becomes

    delta h = d2[-(B/x)r + (2z A+2z^2 B/x) r/(r^2+z^2-x^2)].   (6)

Unequal shells therefore produce a rational nuisance span. Its time derivatives also differentiate z^2-x^2 and generate higher denominator powers. It cannot be silently discarded or treated as an unchanged polynomial equal-shell nuisance. One must either supply these angular modes or prove a further quotient/annihilator construction for the whole time-dependent projected relation. Equations (4) as written are not such a quotient.

An exact counterexample makes this limitation concrete. Use x=2-N1,z=3,d1=d2=1,y=N1+2,alpha=0,gamma=1. A valid synthetic homogeneous/isotropic family has V(N,x)=(1+N^2)X(x), covariance of X equal to exp(-r^2/5), and S=yV; leg two is N2=-1. This satisfies the supplied field law. Add a unit angular monopole to its C_S1u2 representative, leaving U unchanged. At N1=0,r=2 the reconstructed derivative's radial residual E F*-U changes by exactly 37/9801, and its time residual L F*-H changes by exactly 14336/29403. Thus an arbitrary permitted shear representative can falsely fail the unreduced compatibility relation. This is a deterministic nuisance counterexample, not an observed calibration result or a no-go for all projected information.

## Independent controls and scope

`independent_controls_v1.py` has 27 passing exact controls and no failures. They check the Cartesian Hessian sign, radial coefficients, determinant and three different degeneracies, fixed-r time conversion, the noncommuting time/projection operator, a positive-definite synthetic Gaussian covariance family, both cleared compatibility identities, the monopole counterexample and the y=0 algebraic branch. Deliberately discarded shortcuts fail explicitly: the opposite mixed-derivative sign, ignoring the geometry commutator, replacing fixed-r by fixed-angle time differentiation, or ignoring the shear monopole. No author code was inspected or executed.

The source and results are frozen with SHA256 identities. The Gaussian fixture is an existence/control example only; it does not supply actual preparation. All physical premises remain supplied: field law, scalar flow, smooth unequal-time signal covariance, flat calibrated distance/time geometry, peculiar-velocity interpretation, angular-mode treatment and measurement/error operators. No actual finite window or noise envelope is derived here. No uniqueness, fundamental-action selection, full-history converse, empirical validation or formal review verdict is claimed.
