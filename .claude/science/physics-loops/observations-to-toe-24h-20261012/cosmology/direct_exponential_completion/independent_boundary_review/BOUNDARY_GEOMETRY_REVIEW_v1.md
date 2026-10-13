# Focused independent boundary-geometry review

The frozen note's mathematical claims are correct. No source correction is requested. The result concerns the normalized limiting field metric and potential; it does not establish cosmological escape, failure of a supplied trajectory, a finite-k global statement, or a quantum cutoff.

## Exact scope and provenance

I read the complete boundary derivation, runner, freeze, all 11 result rows, execution record, regular-limit derivation, and original exponential-action derivation. Seven exact files are preserved in `source_snapshot/`. The review freeze precedes the independent calculation. All seven originals and snapshots still match their frozen hashes; all four entries of the parent's execution freeze match these bytes. The parent freeze precedes its execution, which finished before this review freeze.

The boundary note is SHA-256 `902e0c54f7fefba200c0eb04e122866dd4f502495338317528039ab191e75f27`; the parent runner is `2390776877a9e164e9eb90d152ce08bb376a030637d67f1b7897f98c96dfd3ee`. The regular-limit source is `fb5447dbd13fb5015a8f6b06f2ecb92a6e543028176df24e566defa8ef0a2afa`, and the original action note is `caf44625b1afd2be042f791800635d2e3707a8a997aab313cc7bcb2bb5623e27`.

No parent runner was imported or executed. No histories were integrated, fitted, altered, or rescored. The prior observational and trace reviews remain untouched. This is a focused mathematical check, not a formal audit or a claim-status promotion.

## Independent derivation

All coordinates, this metric's length, and W are normalized field quantities. They are not spacetime distances, an energy in SI units, or a measured ultraviolet scale.

With r=exp(-u/2), dr=-(r/2)du, the radial term exp(-u)du²/4 is exactly dr². The remaining metric is r² times h, where h=diag(4/(9D),1/(3D)) and D=1+2(x²+y²)/3. The metric stays positive for every finite u,x,y. Positivity by itself supplies no lower bound uniform as u tends to infinity.

For the two-dimensional curvature, use X=2x/3 and Y=y/sqrt(3). Then h=(dX²+dY²)/D with D=1+3X²/2+2Y². Writing its conformal factor as sigma=-log(D)/2 gives K_h=-D(sigma_XX+sigma_YY), hence

    K_h(x,y) = [7+(2/3)(x²-y²)]/(2D),
    K_h(0,0) = 7/2.

I did not assume the cone scalar-curvature formula for the three-dimensional calculation. The independent script differentiates the original diagonal u-coordinate metric, forms its first-kind connection, raises the first index, and contracts the three sectional Riemann components. It obtains

    K_ux = K_uy = 0,
    K_xy = exp(u)(K_h-1),
    R[g] = exp(u)(15-2x²-6y²)/(3+2x²+2y²).

Consequently R[g](u,0,0)=5 exp(u)=5/r². All x,y derivatives are taken before substituting the transverse origin. This agrees with the parent's direct Ricci calculation through a different contraction and coordinate representation.

The radial length from u=0 to U is 1-exp(-U/2), tending to one. More strongly, x=y=0 and u(lambda)=-2log(1-lambda), 0<=lambda<1, solve every affine geodesic equation and have unit speed. The geodesic has no continuation within the stated r>0 manifold at lambda=1. Equivalently, r_n=1/n at fixed transverse coordinates is Cauchy: the radial path attains distance |r_n-r_m|, and every path has length at least the absolute radial displacement. Its missing endpoint shows metric incompleteness. The divergent scalar curvature along this approach rules out a smooth nondegenerate Riemannian extension that adds that endpoint. A fixed positive overall metric factor rescales distances and curvature but does not remove these features.

Substitution in the full W gives exactly

    W = 3(1-r²)²/2 + r⁴[x²/2+y²/3+2 nu(log r)²].

Since r⁴(log r)² tends to zero, W tends to 3/2 for every fixed finite x,y and positive fixed nu. Bounded transverse coordinates also cause no divergent barrier in this expression. The conclusion is not uniform over arbitrary diverging transverse fields, and it does not rule out a separate trapping or energy argument for specified initial data.

## Checks and sensitivity

`independent_boundary_check_v1.py` contains the full independent recipe. Its single execution completed in about 0.24 seconds: 22 exact mathematical/diagnostic checks and complete consumption of the 11 parent residual rows, 33 pass and zero fail. The 11 producer residual checks are bookkeeping corroboration; the independent metric, connection, curvature, geodesic, and potential calculations supply the mathematical evidence. Parent execution reports 11 pass, zero fail, exit zero, empty stderr, and approximately 0.515 seconds; its full output is preserved.

Two explicitly damaged-metric probes test decisive formulas. Freezing D=1 before differentiating changes the origin scalar from 5 exp(u) to -2 exp(u), an exact residual of -7 exp(u). Omitting the radial 1/4 changes it to 13 exp(u)/2, with residual 3 exp(u)/2, and doubles the radial length to two. Both probes are rejected by the undamaged target identities. These are independent symbolic input mutations, not claims of end-to-end mutation coverage of the parent's runner. Their nonzero residuals and exact modified metrics are preserved in the script and result.

There was no failed scientific assertion. The initial file-inventory command used an unavailable `python` alias and exited 127; using `python3` recovered immediately. That actual tool failure is retained in `TOOL_FAILURES_v1.json` rather than suppressed.

## Scope disposition

The geometry supplies a counterexample to deriving completeness merely from pointwise kinetic positivity, and the explicit potential supplies no divergent barrier along this particular finite-distance approach. Neither observation determines the dynamical fate of a cosmological solution. The source correctly retains the compact, bounded limiting-solution premise of its finite-interval comparison argument. Its previously computed finite histories are not promoted here to an all-time existence theorem; their output was not rerun. The boundary result does not invalidate the conditional theorem, does not imply the singular normalized limit describes the full finite-k theory at arbitrarily large u, and does not introduce a physical cutoff.

The source, exact identities, all result rows, and these limitations agree. The complete source disposition and final evidence hashes are in `SOURCE_DISPOSITIONS_v1.json` and `FINAL_RECEIPT_v1.json`.
