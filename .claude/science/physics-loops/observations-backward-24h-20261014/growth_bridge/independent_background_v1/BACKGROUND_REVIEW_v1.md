# Focused growth/background compatibility check

Root remains author. I independently derived the equations and froze the exact fixture calculation before reading `growth_bridge/WORKING_v2.md`. I wrote only this assigned directory, used no raw observations or new integrations, and did not run a formal audit. The checked author source is SHA256 `0aad424f1fd7fe582c7005edab096e7e0a3787ef8ef84ca2ccd813d3490a6397`, copied verbatim as `AUTHOR_WORKING_v2.md` after the independent freeze.

The complete pre-exposure derivation is `PRECHECK_v1.md`. Its source and commitments were frozen in `PRECOMPUTE_FREEZE_v1.json` (`a7e68dd3d324a3d5d6fc709d31ba9cd11683bf0751785e592047d97a1b938c5a`). The independent calculation and conclusions were frozen in `RESULT_FREEZE_v1.json` (`a054fd3089cbe4fe4743095b0611f880c2fb313b53db42ef3a3690ade7ca95b2`). This report is the subsequent source comparison, not a relabeling of author equations as an independent derivation.

## Independent result and correspondence to equations (5)–(10)

Use prime=d/dN, flat conserved dust, F=Fc Z, rho=3H0² Fc B exp(-3N), Y=H²/H0², and the single-radial-field identification omega=(1-3q)/(2q). Define

    A=Z+Z'/2,
    M=Z''-Z'+omega Z'^2/Z,
    C=3Z+(5/2)Z'+Z''/2.

Direct substitution into the checked M12 metric identities gives

    A Y'+M Y+3B exp(-3N)=0,
    V/(Fc H0²)=C Y+(A/2)Y'-(3B/2)exp(-3N).

These match v2 equations (5), (6) and (9), including the clock conversion, signs and kinetic factor. The factor multiplying Fddot is essential: Fddot=Fc H0²[Y Z''+Y' Z'/2]. Moving transverse fields would add kinetic stress; geometric q cannot simply stand in for the one-field background reconstruction in that case.

From the supplied definitions of P and r, Psi=(1+r)(Phi+Psi)/2. On W!=0, physical dust Euler gives

    Y'+2L Y=S,
    L=2+W'/W,
    S=3 exp(-3N)(1+r)P.

This matches v2 equation (7). Defining T=2LA-M, the combined necessary condition is

    T Y=3 exp(-3N)[B+A(1+r)P].

This is v2 equation (8) with L1=2A, L0=M and its D=L. When T!=0 it determines a necessary algebraic Y. That function must still obey its own derivative equation; inserting an arbitrary derivative supplied by Euler without differentiating the determined Y would be invalid. If T=0, both consistency and rank must be checked before division. Positive Y is required. The v2 text explicitly retains these gates.

The potential relation (10) also matches the independent conformal normalization: V=2Q Hv² U/A_conformal^4, F=Q/A_conformal², Q/Fc=4beta/(1+k), hence V/(Fc H0² Z²)=[2(Hv/H0)²/(Q/Fc)](B0+nu B1). Its shape and scale are still candidate premises/calibrations. A potential fit cannot repair a failure of the necessary kinetic-plus-Euler equations. The note correctly preserves nonzero-F', complete matter, perturbation closure and absolute-normalization limitations.

## Exact two-candidate fixture

The pre-exposure fixture uses q=9/50-N/25, W=1, beta1=29/100, B1=1/5, P=B1(N+2)/Z_beta1 and beta2=13/50, B2=26/145, where

    Z_beta=beta(1-3q)/(beta-q).

The resulting exact shared P is

    P=10(N+2)(4N+11)/[29(6N+23)].

The reduced continuity density functions are

    P Z_beta1/B1=N+2,
    P Z_beta2/B2=N+11/4.

Both derivatives equal W=1 identically. Thus the shared reduced observations retain an integration-constant ambiguity. This statement concerns leading continuity; it does not establish exact relativistic continuity delta'=W+3Phi'. The v2 note itself preserves that distinction.

For the full background/Euler test, the independent precheck explicitly chooses the light radial slip specialization **r=q**. This is an additional specified part of the fixture, not an implication of the metric identities. Write Y_alg=exp(-3N)U. Since W=1,

    U=3[B+A(1+q)P]/(4A-M),
    R=exp(3N)[Y_alg'+4Y_alg-3exp(-3N)(1+q)P]
     =U'+U-3(1+q)P.

The independently written SymPy calculation uses rational numbers throughout. At N=0:

| Branch | T=4A-M | Forced Y_alg | Euler consistency residual R |
| --- | --- | --- | --- |
| beta=29/100 | 1308712/299475 | 13384899/30100376 | -43561803701691/78106261667360 |
| beta=13/50 | 63947/14400 | 7664652/16404865 | -1083926166138/1855997211505 |

The residuals are approximately -0.5577248581 and -0.5840128204, respectively. Both forced Y values are positive and both denominators nonzero. The point lies in the common admissible chart: q=.18, beta1=.29, beta2=.26, Z1=667/550>1 and Z2=299/200>1. Smoothness then gives a local domain around the point. No singular division or unphysical negative H² creates the rejection.

Therefore neither of these specified branches can satisfy the full radial kinetic equation and Euler equation on an interval containing N=0 **under r=q**. No expansion curve was imposed: each Y was forced by eliminating Y' from the two equations. The discarded derivative consistency is precisely what defeats both leading-continuity constructions. This is a local exact necessary-condition failure, not a rejection of every parameter choice or a proof of empirical exclusion. The rational q profile is not asserted admissible for all N.

## Scope boundary retained

The author v2 fixture supplies q,P,W but does not itself specify r in that paragraph. I notified root of this distinction. If r is unspecified or comes from a finite-range map differing from q, the numerical fractions above are not an unconditional statement about that alternative. The general Euler elimination is valid with arbitrary supplied r; a full fixture must supply its slip/range branch. Without it the Euler source is underdetermined. Nor do surviving reduced continuity assignments prove exact perturbation, background-potential or full action membership.

I read the complete WORKING_v2 context but checked the requested background equations and this fixture. I did not independently audit the earlier quadratic/Mobius classification, the four-row lift, survey estimators, observational sources, tensor reconstruction or any new parent executable. The independent exact file also retains a formal potential readout for its algebraically reconstructed Y; since Y fails full compatibility, that expression is not labeled a solution's physical potential. No failed branch was repaired by choosing a selector, an expansion history or a different tolerance.

The complete report/source/result identity is in `BACKGROUND_IDENTITY_v1.json`. The exact residuals and denominators are preserved in `INDEPENDENT_RESULTS_v1.json`; no numerical fitting or ODE campaign was performed.
