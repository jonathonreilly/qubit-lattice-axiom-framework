# Independent potential reconstruction precheck

No parent postprocess or potential result has been opened. Inputs are only this checker's already frozen fourteen epochs, reconstructed R,g,q,beta, the physical E=HJ/H0 trajectory readout, and the supplied radial action/chart. No ODE rerun or parameter truth enters the inverse.

For the radial Jordan action, omega=(1/q-3)/2 and g=F'/F. Its 00 equation is

    3FH^2=rho+omega Fdot^2/(2F)+VJ-3H Fdot.

Since rho/(FH0^2)=3R a^-3, directly

    vbar=VJ/(F H0^2)=E^2[3+3g-(1/q-3)g^2/4]-3R a^-3.

This avoids differentiating reconstructed g; it uses the full supplied radial background equation rather than a quasistatic response. It is only a necessary background potential readout until the candidate action is separately checked.

Invert the fixed candidate chart from the already independently calibrated beta. For 1/4<beta<1/3, set k=(1-sqrt(4-12beta))/3, alpha=sqrt(beta), s=(1+k)/(k(1-3k)). If 0<q<beta,

    X=exp(2alpha u)=(beta/q-1)/[(1-3beta)s],
    u=ln(X)/(2alpha), T=1+sX,
    A^2=(1+s)X/T,
    U0=3/2+3s(X-1)^2/(2T^2),
    U1=(1+s)u^2/(2T^2).

The potential transformation is VJ=VE/A^4=2Q Hv^2(U0+nu U1)/A^4, whereas F=Q/A^2. Hence

    d=(A^2/2)vbar=lambda U0+mu U1,
    lambda=(Hv/H0)^2, mu=lambda nu.

Solve the two exact-declared calibration rows (indices0,2) for lambda,mu and form nu=mu/lambda. Evaluate the fixed indices3,4,5,6 with the same pair. Use ordinary double arithmetic on the frozen reconstructed inputs. Record matrix determinant, unscaled and column-normalized 2-norm condition numbers, geometric-field reconstruction differences, coefficient errors relative to truth only after fitting, and absolute/term-normalized later residuals. These are diagnostics; no new numerical pass threshold is chosen and no declared threshold is changed.

A small U1 and nearly collinear rows can make nu poorly conditioned even when potential residuals are tiny. Floating roundoff and upstream reconstructed beta/q errors must remain visible. Extra observed precision, actual physical scalar-potential selection, absolute Q or rho0, and empirical confirmation do not follow. The candidate A(u) normalization and potential basis are supplied premises.
