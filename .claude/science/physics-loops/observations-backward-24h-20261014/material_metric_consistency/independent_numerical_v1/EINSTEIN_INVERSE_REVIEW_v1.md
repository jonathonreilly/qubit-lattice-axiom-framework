# M19 independent Einstein-frame numerical check

The separate Einstein-areal generator supports the nonlinear physical-metric inverse on one nonconstant, positive-candidate local fixture. It recovers the supplied parameters and scalar profile, and the potential inferred at two radii agrees at twelve later saved radii. No author solver, author numerical output or aggregate was executed. This is a focused numerical equation/coordinate consistency check within the supplied action, not observational validation or a formal audit.

## Reading and freeze chronology

The complete author note was read at the first tool time, 2026-10-15T20:06:58Z, and preserved as `EXPOSED_NOTE_v1.md`, SHA256 `97c981752e50c9be3ec9c4686d0d63704a615948567dc793531cc465b3325c70`. Its inverse formulas and reported fixture parameters were already exposed. Therefore the independent contribution is the different generator, coordinate transformation, numerical implementation and assembly; it is not a blind discovery of the inverse theorem. The action and inverse inputs are conditional premises.

The independent equations were frozen at 20:09:27.628231Z in `PRECHECK_v1.md` (SHA256 `d52db2d909102db3d9961750762d06886a84e7be8922f70b5bb3daa140e05c1e`). Implementation was frozen at 20:11:52.994874Z. Both trajectories, all 21 saved rows per trajectory and conclusions were frozen at 20:12:54.234014Z in `INDEPENDENT_RESULTS_FREEZE_v1.json` (SHA256 `17322b881f2368f615d760dc5036ffbda7ebce233ee69b83ffb0ec4dfbbc80f2`), before reading the parent helper or outputs.

Only afterward, within 20:15:06Z–20:15:35.043735Z, the complete text of `scripts/scalar_vacuum_metric_inverse.py` was exposed. Its frozen copy is `EXPOSED_AUTHOR_HELPER_v1.py`, SHA256 `1fc303d42d24f4700b16080db58bfce0a214f9de970033470e05da2469cd08f7`. The `first_helper_read_utc` field in `AUTHOR_EXPOSURE_v1.json` denotes the preceding clock marker, not a separately measured exact tool-start instant. No author result arrays were read. The source comparison below is limited to the alternative generator/metric inverse correspondence; it does not constitute a full helper review or verification of its other tests. Later author note changes are outside this report's frozen note exposure.

## Independent generator and physical coordinate map

Set the unidentifiable common classical normalization f0=1, write X=s+z² and P=V/f0, and use g_E=X g_J. The Einstein action is

    integral sqrt(-g_E) [R_E/2 - K(z)(d z)²/2 - U(z)],
    K=2/(lambda X)+6z²/X²,  U=P/X².

With Einstein areal radius R, metric

    ds_E²=-exp(2 alpha)dt²+dR²/C+R²dOmega²,

and p=dz/dR, the independently derived equations are

    C_R=(1-C)/R - R(C K p²/2+U),
    alpha_R=(1-C)/(2 C R)+R K p²/4-R U/(2 C),
    p_R=U_z/(C K)-(alpha_R+C_R/(2 C)+2/R)p-K_z p²/(2K),
    z_R=p.

The first two follow from Einstein Gt and Gr, and the third from the noncanonical scalar Euler equation. The implementation uses

    K_z=-4z/(lambda X²)+12z/X²-24z³/X³,
    P_z=Hv²[12z³+(nu/a)z³(4 log²z+2 log z)],
    U_z=P_z/X²-4zP/X³.

The physical areal coordinate and metric are

    r=R/sqrt(X), eta=1-Rzp/X, J=dr/dR=eta/sqrt(X),
    B=C eta², ell=alpha-(log X)/2.

The conditions C>0, z>0 and eta>0 give the local regular branch. Physical derivatives use D_r=J⁻¹D_R with

    D_R=partial_R+p partial_z+p_R partial_p+C_R partial_C.

This supplies the seven input values (r,B,B',B'',ell',ell'',ell''') to the inverse. Neither the source scalar nor source parameters are arguments of the inverse assembly. The scalar and parameters are available only on the generator/truth side and for comparison. Integration of u dr uses the physical Jacobian J after changing integration variable to Einstein R.

The initial parameters k=.1, Hv=.03 and nu=1.2 had appeared in the author note; the initial state and radial span were selected independently: z0=1.35, p0=.08, C0=.95, r0=1, alpha0=log(s+z0²)/2, R0=sqrt(s+z0²), R_end=R0+1.5. In particular p is an Einstein-radius derivative, not the author's physical-radius initial velocity. The physical scalar increases from approximately1.35 to1.43782656. No initial scalar boundary information is supplied to the inverse.

## Metric-only reconstruction and source correspondence

The independent code assembles Gt,Gr,Ga and D=B(1/r-ell'), then

    u=(Ga-Gt)/D,
    H=Gr-Gt-B(u'+u²)-(B'/2-B ell')u,
    j=B u²/(2H),
    W=-Gt-H/2-B(u'+u²)-(B'/2+2B/r)u.

Its quotient derivative u' is manually assembled from the seven metric inputs; it is not imported from the author symbolic code. Calibration at saved radii0 and8 uses I=integral(u dr), E=exp(-I), lambda=(j8-E j0)/(1-E), then k=(1-2/sqrt(1+3lambda))/3 and Y=sj/(lambda-j). The potential P=(s+Y)W is fit to Hv² A(Y)+(Hv²nu) C(Y), where A=3(s+Y²), C=Y² log²Y/(4a), at the same two radii. Later saved radii9–20 are checked without refitting. These are twelve subsequent synthetic checks, not independent empirical data or statistical holdouts.

Post-freeze reading confirms that the author's `geometry_functions` and `invert_metric` use the same metric-only formulas and positive-candidate algebra. The author uses a direct Jordan ODE, 601 physical-radius samples and cumulative Simpson integration; this implementation uses the independent Einstein ODE, transformed physical radii and Gauss–Legendre quadrature. It did not run the author's code to obtain agreement, nor attempt to reproduce the author's different fixture arrays.

## Numerical computation and results

The independent source is `einstein_generator_v1.py`, SHA256 `88c50bf23033ac444e63a10c2cc875c49f9fd2f49ab4a7465702b8dc6d1c6b53`. It integrates the Einstein system in IEEE double precision with SciPy DOP853. The primary trajectory has rtol2e-12, atol1e-14, max_step.075; the refinement has rtol5e-14, atol1e-15, max_step.025. They require317 and917 function evaluations respectively. Both completed. The guarded subprocess cap was120seconds; actual wall time was1.012seconds, with empty stderr.

At each approximate saved state, derivatives of the independent analytic vector field are assembled at50decimal digits using mpmath differentiation. This is not a high-precision trajectory, not a reconstruction from rounded measured metric inputs, and not a certified error enclosure. Algebraic derivative assembly is deliberately distinguished from trajectory accuracy.

The primary physical interval is approximately [1,1.34880904552]. Across its21 saved points, minima are C=.95, B=.901631, eta=.974210, |D|=.685554, |u|=.0300067, H=.00149755, j=.248146 and lambda-j=2.11015. These are sampled margins, not interval-certified domain bounds. The recovered potential coefficients are positive.

| Quantity | Primary result | Refined result |
|---|---:|---:|
| recovered k | .0999999999999998586 | .0999999999999998676 |
| absolute k error | 1.41424e-16 | 1.32354e-16 |
| recovered Hv² | .000899999999999999670 | .000899999999999999691 |
| absolute nu error | 2.01908e-14 | 1.88959e-14 |
| max absolute reconstructed Y error | 4.63650e-15 | 4.33915e-15 |
| max later absolute potential residual | 7.26693e-19 | 6.80088e-19 |
| max later relative potential residual | 1.29653e-17 | 1.21338e-17 |

Quadrature refinement24→48 and48→96 changes I by9.61e-19 and−3.70e-19, respectively. The maximum difference of saved Einstein states between trajectories is6.67e-16. Such agreement is a finite numerical stability diagnostic, not a rigorous global integration error bound.

The two-point denominator is1-E≈.00649481 (reciprocal≈153.969), and the potential matrix has determinant≈20.3511 and2-norm condition number≈327.983. The problem remains sensitive to readout/integral errors; this synthetic calculation supplies no observational error budget.

## Original equations and what the residuals mean

The original Jordan tt, rr, angular and scalar equations were separately evaluated after the conformal/radial transformation, using the true mapped scalar derivatives z'=p/J and z''=(p_R J-p D_RJ)/J³. Their largest primary residual is approximately2.94e-50. This tiny number measures50-digit local algebraic compatibility of the distinct Einstein equations and physical-coordinate map at approximate states. It does not measure50-digit trajectory correctness. The angular Jordan equation is included, rather than checking only equations used to evolve C and alpha.

A second residual calculation substitutes the recovered parameters/profile and the compatible identities z'=uX/(2z), z''=X(u'+u²)/(2z)-X²u²/(4z³). The primary maximum absolute residuals are7.27e-19 in each metric equation and1.269e-16 in the scalar equation; refinement gives6.81e-19 and1.188e-16. This second check uses the derivative compatibility identities; it is not a separate finite-difference differentiation of reconstructed Y. Profile agreement over all saved radii and the distinct true-scalar original-equation check are retained separately, so that these residuals are not misrepresented as an independent high-order observation reconstruction.

## Failures, limits and disposition

An initial report-writing command failed to parse because three derivative prime characters ended a triple-single-quoted Python prose string. No command body executed and no scientific data were changed. `PRECHECK_SETUP_FAILURE_v1.json` retains that setup failure. The computation itself had no recorded solver failure or sampled-domain exit; no thresholds or fixture epochs were adjusted after the result.

This verifies one regular, nonconstant, positive-candidate local solution family numerically through an alternative frame/generator. It does not establish interval-wide regularity, global completion, material boundaries, physical stability, uniqueness across excluded branches, an observed metric/derivative supplier, an independently selected vacuum or action, an absolute F normalization, a physical radial scale, initial history, or empirical agreement. The same known action supplies both the generator and the inverse hypothesis. Roundoff-small residuals cannot retire those premises.

The report is bound to the original exposed note and post-freeze helper snapshot, not to later author edits or a future canonical aggregate/cache. Root retains scientific authorship. No author aggregate, raw observation extraction, Git operation or formal audit was run in this check. All work products were written only in the assigned independent numerical directory.
