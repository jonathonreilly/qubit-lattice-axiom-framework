# Independent full radial dynamical-response check

The independently derived equations and implementation agree with the author's complete working radial scalar/dust system and all 56 saved mode rows. This is conditional source and numerical validation on fixed synthetic cases. It is not authorship of the parent result, a formal audit, a full three-field perturbation proof, observational validation or initial-state selection. I wrote only this assigned independent directory.

## Independence and immutable inputs

Before opening any parent M14 working note, code or result, I read the complete supplied action note (SHA256 `39a0dd9e107edba23adbfe8cf070f8f279190c40c651dc905af9d59911cad000`) and fixed forward protocol (`22084105058cd2d2b94edb0d7c272198cac9ef196477966bf8fd01e32355d656`). I froze `PRECHECK_v1.md` at `d641141de8388e88e973972c9b9075f74e71bd717a623898c96850684f05bc0a`; its identity record is `12ed7feb5da12958ed1b5b08cf4ad7a1aae994a7471d33ad490b478f94ff806c`.

The numerical implementation was also written and frozen before parent code/results exposure. `independent_dynamical_v1.py` has SHA256 `c453fb56f2777cc8ab3ca0d3b74dcf08c33c9d8326d189a273714e380de10b4d`. Its independent output `INDEPENDENT_DYNAMICAL_RESULTS_v1.json` is `9c43264dff6a2009ff93d90e297d1fc4fbacda865d8687c8cf75225f4f99c462`, bound before parent exposure by `RESULT_FREEZE_v1.json`, SHA256 `3895a754ba35705e8d5142c301234a9c7439c506b147c5dbc07a610e74020966`. The original implementation, stdout, empty stderr and all generated rows remain unchanged. There was no failed scientific comparison to suppress or threshold modification in this block.

Only afterward did I read and snapshot the complete `WORKING_v1.md` (`637fdbfbead8d4566bf0e99e046a26cae28123b73f88f60d4e768ee5584cdff1`), complete `forward_v1.py` (`3fe111849dadcdea804f6a70963920910cecb43f35016e52428ca86c67f03ba7`), full result and per-background products. The parent's combined result is `a2178c1ccdd526b99bb9f16bda7b5753b8e7d111a6cd659c4b9c398f689810e9`. Its three recorded source-input hashes match the copied original files. `AUTHOR_EXPOSURE_FREEZE_v1.json` records this chronology; no parent module was imported or aggregate rerun.

## Action-derived equations and signs

The supplied radial action has kinetic term -Q K(du)^2, so the canonical field satisfies chi_u=sqrt(2QK), V=2Q Hv^2 U, and b=d ln A/dchi. This canonical chi is not the bounded algebraic chi used in the confinement note. With w=dot chi, Einstein energy density rho and Einstein H, I independently obtained dot w=-3Hw-V_chi-b rho, dot rho=(-3H+bw)rho and dot H=-(w^2+rho)/(2Q).

For Einstein Newtonian potential phi, number contrast D, covariant velocity u_i=partial_i v, scalar perturbation X and Z=dot X, the frozen derivation gives

    dot phi=-Hphi+(wX-rho v)/(2Q),
    dot D=K_E^2 v+3 dot phi,
    dot v=-phi-bX-bw v,
    dot X=Z,
    dot Z=-3HZ-[K_E^2+V_chichi+rho(b_chi+b^2)]X
          +4w dot phi-2(V_chi+b rho)phi-b rho D.

The rho*b^2 term comes from delta rho=rho(D+bX), not a chosen effective mass. The -2b*rho*phi term follows from the lapse perturbation of the background scalar equation. Both signs and the factor 2 agree with the author's expanded form. The 00 equation fixes only the initial D, with phi,X,Z,v independently assigned by the protocol. Neither implementation repeatedly projects the constraint or sets a homogeneous scalar response to zero.

My 00 residual is the negative of the author's eliminated-0i constraint expression. This is just a residual sign convention. I independently compute a spatial Einstein trace residual by differentiating phi_dot through the equations, in addition to dust continuity and Euler. The author has a separate exact symbolic propagation check, Cdot=-3HC; I inspected its expression and source without representing it as a fresh blind symbolic proof by this checker.

The physical map is A>0, G=H+bw>0, HJ=G/A, F=Q/A^2, PsiJ=phi+bX, PhiJ=phi-bX, deltaJ=D-3bX and vJ=A v. Therefore W=K_E^2 v/G. Both exact linear Jordan dust equations follow from this dictionary. The two implementations agree in these slots; no Phi/Psi label exchange or Einstein/Jordan time derivative conflation is present. The source includes scalar time derivatives, rolling coefficients, conformal matter perturbations and the freely supplied X,Z states. There is no r=q or quasistatic response substitution.

## Separate implementation and solver

I implemented radial derivatives directly in real arithmetic from the action's rational/exponential functions, rather than importing the parent's SymPy-lambdified coefficient function. I evolve canonical w and log(aE), whereas the parent evolves u_dot and aE. All four mode systems share one background in each of the two independent integrations. I use normalized time tau=HE0*t and Radau, independently of the parent's DOP853. This method difference was declared before exposure. The original rtol=2e-12, atol=2e-15, maximum physical step, cases, seven sampled fractions, calibration indices and reserved indices are unchanged. Each independent Radau integration used 7009 function evaluations; the entire independent computation recorded approximately 0.757 seconds. No high-precision trajectory or rigorous integration enclosure is claimed.

The scale conventions differ by a harmless spatial coordinate normalization: I start aE=1 and use normalized aJ=A*aE/A0; the author starts aE=1/A0 and uses aJ=A*aE. Accordingly author k_com=independent k_com/A0. The physical K_E and K_J, Jordan H0 and scalar covariant velocity potential are the same. This normalization is applied explicitly in correspondence; untransformed comoving mode numbers are not falsely compared as physical differences.

All 16 independent equation/numerical controls passed. The largest scaled 00 residual over the seven saved epochs per background was 2.486e-15. The largest trace, Jordan continuity and Jordan Euler residuals were respectively 2.150e-16, 1.061e-16 and 1.994e-16. The parent separately sampled its 00 residual at 301 times per background and reports maxima 5.453e-15 and 4.307e-15. I did not independently rerun that 301-time scan; seven saved epochs per background is the independent numerical constraint scope. Neither scan is a proof between sample points.

## Momentum reconstruction and candidate recovery

Before reading the parent's formula I derived the row equation

    [2/P,-1,-r] [R,g,g/q]^T = 2+2phi'/phi,

with g=F'/F, R=rhoJ0/(3H0^2 F) and r=bX/phi. Multiplication by P/2 gives exactly the author's rows [1,-P/2,-Pr/2] and right side M=P(1+phi'/phi). This also agrees with M=P'+P P3 because P is proportional to aJ*phi/W. The independent inverse uses metric slip r; the author's uses the Euler readout. Their equivalence is checked separately: my largest |r_metric-r_Euler| is 9.160e-16. This is an ideal analytic derivative map; neither implementation estimates actual observational derivatives or their covariance.

The independent maximum absolute error in the reconstructed R,g,g/q,q vector is 4.808e-14. A fourth mode tests the same inferred triple without refitting. The supplied candidate chart implies R(1-3q)=B-(B/beta)q, with B=1/kappa. My two-epoch line solution is algebraically equivalent to the parent's 2x2 inverse for 1/beta and kappa, but was implemented separately. At fixed calibration epochs 0 and 2 I recover:

| Case | Independent beta | Independent kappa=1/B | Maximum absolute difference from author's pair |
| --- | --- | --- | --- |
| positive_roll | 0.28520000000592355 | 4.559702332250644 | 5.598e-11 |
| negative_roll | 0.3219249999989281 | 3.24712748603492 | 4.386e-11 |

The largest independent beta error against supplied truth is 5.924e-12, and the largest kappa error is 3.250e-11. Both are below the unchanged 2e-7 protocol threshold. The largest independent absolute candidate residual at the fixed later epochs is 4.302e-13, below 1e-9. All original parent result controls also report success: 22 total, comprised of four symbolic checks and nine per background. Those are inspected parent controls, distinct from my 16 independent controls and 17 post-exposure comparison checks.

The complete comparison covers all 14 saved background epochs and 56 mode rows. Maximum absolute differences include 8.743e-15 in u_dot, 7.869e-14 in inferred q, 2.432e-14 in P, 3.710e-13 in P3, 2.849e-13 in r, and 6.446e-18 in Xdot. The complete field map, maxima and locations are retained in `AUTHOR_CORRESPONDENCE_RESULTS_v1.json`. No numerical equation or saved-row discrepancy was found.

## Conditioning and actual domain limits

Three-mode rank and nonzero g/q are conditions, not consequences of the action. Matrix condition numbers differ under the deliberate row rescaling: the independent maximum is about 213.0; the author's is about 213.1. Both are finite at saved epochs, but these are not error bounds. The calibration q separations are only -4.043e-5 and +3.502e-4. The stronger amplification in beta/kappa compared with individual q discrepancies is therefore expected. No observed precision follows from the small synthetic residuals.

Both numerical histories show a sign change in g/q between sampled fractions .10 and .25. For any continuous exact history with those signs, an intermediate zero occurs; there g=y=0 and the pointwise q=g/y inverse is undefined. This is not a failure at the seven saved epochs, whose smallest |g/q| is .0027706. It does prevent relabelling this finite check as uniform identification across the entire interval. `TURNING_DOMAIN_v1.json` preserves the sampled signs, without a new root search or rigorous root enclosure. This does not prove that extra smooth whole-history information could never bridge a turning point.

The author's reserved_mode and candidate_later checks use absolute dimensionless residuals, although the frozen protocol key is named reserved_scaled_max. My initial independent summary uses explicit term-normalized residuals; the post-exposure correspondence separately checks the same absolute candidate residual and records the normalization distinction. There is no failing current case or changed threshold. The working author experiment is specialized to the protocol's Q=Hv=1 and first-three/fourth-mode split; this review does not confer generic configuration or arbitrary-unit support.

The largest metric-slip departure from geometric q is about .1828 and .3265 in the two cases, demonstrating that the successful synthetic inverse does not rely on an accidental r=q data identity. However the radial action, background, exact clock/mode calibration, conformal matter identification and ideal observation map are all supplied. A radial-sector implementation is not by itself a complete transverse-mode decoupling proof. Actual bandpowers, source populations, survey windows, bias, covariance, nonlinearities and data calibration were not tested. All observations remain outside this synthetic numerical comparison; no empirical holdout or theory acceptance is claimed.

This report covers the frozen working source and products named above. A later canonical consolidation or changed source/cache needs its own affected confirmation. No Git, source publication, runtime ownership, status or formal audit action was performed.
