# Galaxy response comparison: frozen development protocol

Source pin: `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`. This is provisional research, not an adopted physical law, audit verdict, raw-data likelihood, or blind confirmation. Runtime receipts supply UTC and hashes. No target fit has been run at this freeze.

## Target, exposure and data boundary

Compare a positive universal linear finite-range force with an explicit nonlinear acceleration response on processed SPARC rotation curves. The official project index, master paper, and table schemas have been read. Published SPARC/RAR results are already known. The paper's UGCA442 example and automatic web previews of CamB, D512-2, D564-8, D631-7 and DDO064 rows were exposed during schema retrieval; those six names are training-only. No fitted residuals or selected best models have been inspected. All remaining holdout galaxies are a model-development holdout, not blind new data.

Primary files are the official `SPARC_Lelli2016c.mrt` and `Rotmod_LTG.zip`; preserve whole-file hashes and exact original-rotation-source codes. Obtain the official master paper and profile archives for provenance/availability. The supplied baryonic curves already assume Newtonian disk/bulge geometry and photometric/gas reductions. They are not raw velocities, image pixels, independent acceleration measurements, or a likelihood with known covariance. H I density profiles are not columns of the standard mass-model table. Their absence must not be concealed by multiplying Newtonian disk speeds by a spherical Yukawa factor.

## Selection and split, before target fitting

Main finite-source comparison: Q=1 or 2, inclination at least 30 degrees, all supplied bulge components zero, at least six positive-radius rows, and at least five rows at R >= 0.5 Rd. Keep all such outer rows provided the declared positive source reconstruction passes its baryonic-only checks below. Report every rejection and reason. Nonpositive/invalid observed speeds invalidate a galaxy for log scoring; report them, do not tune a threshold to residuals. No morphology/velocity/acceleration/residual cut beyond these rules.

Split eligible galaxy names by SHA256 of UTF-8 `galaxy-response-20261012:` plus the exact SPARC name: integer from first eight hex digits modulo 5 equals zero is test, otherwise train; the six exposed names above are train. The split is at galaxy level. All photometric and baryonic predictors may be used to compute a test galaxy's predictions; its observed rotation velocities may not set global parameters. Freeze source reconstruction, fit code and split receipt before evaluating test scores.

## Models and normalization

All use one universal stellar mass-to-light ratio U in [0.1,1.0] solar units, fitted only on training galaxies; a second table repeats U fixed at 0.5. No per-galaxy fitted gravity parameters, distances, inclinations, or U. Gas includes the published 1.33 helium factor exactly once. Positive/negative component speeds encode inward/outward accelerations as V|V|, not V².

N: Newtonian baryons, V² = Vgas|Vgas| + U Vdisk|Vdisk|.

L: potential between point masses

`-G_N m_A m_B / d * [1 - sum_j w_j + sum_j w_j exp(-d/lambda_j)]`,

with w_j >= 0, sum w_j <= 1, and fixed lambda_j = [0.3,1,3,10,30,100] kpc. This is a finite positive massless-plus-massive spectral response normalized to the short-distance Newton constant, with six global spectral weights and common U. It includes N. It is a declared finite response family; a failure does not exclude arbitrary modified gravity or arbitrary positive measures outside the grid. Also report the value attained with all massive weights zero. A comparison that normalizes the same positive force to its asymptotic rather than locally measured G would be a different model and must not be silently substituted.

NL: `g_pred = g_bar / [1-exp(-sqrt(g_bar/a0))]`, with g_bar from the same baryonic disk source and a0 a single global acceleration in [1e-12,1e-8] m/s². Use stable expm1. This known RAR-style response is a supplied physical rule, not derived from the scalar continuum or claimed novel. It is defined here as a circular-orbit acceleration law. The algebraic relation is not generally the disk solution of AQUAL or QUMOND; a covariant action, nonspherical field solution, lensing response, external-field behavior and cosmology remain separate obligations. Global parameter counts are N:1, L:7, NL:2; fixed-U versions remove one each.

## Positive source reconstruction, independent of observed rotation speeds

Use the published signed Newtonian gas and unit-U disk curves as calibration inputs, with total gas mass 1.33 MHI and unit-U stellar mass L3.6. Construct axisymmetric nonnegative radial densities from a fixed basis of circular rings convolved with normalized 2D Gaussians. Each basis has unit total mass, radius A_j and width sigma, Fourier-Bessel transform exp(-sigma² k²/2) J0(k A_j)/(2pi). Set A_j uniformly on [0,1.5 Rmax], 64 terms and sigma=Rmax/32. Gas is a thin plane; stars use the paper's exponential vertical profile with h=0.196 Rd^0.633 kpc. These are explicit reconstruction assumptions; the ring weights are baryonic calibration parameters, not new gravitational or Vobs-fitted knobs.

For each component, determine nonnegative masses by least squares against its signed Newtonian V², with a total-mass constraint of five percent. Use normalized residuals relative to max(max|Vcomp²|,1 (km/s)²), not errors invented for the published components. Prefer a deterministic convex constrained solve. Report the fit residuals and all active assumptions. Accept a component only if its RMS signed-V² discrepancy is at most 2% of that scale, its maximum at most 5%, and its total mass agrees within 5%. A zero component has zero density. Source-density ambiguity remains even if these checks pass. Profile brightness is a diagnostic, not an undeclared extra fit after seeing rotation residuals.

Compute the Yukawa force of these actual disk densities using the derived axisymmetric Green function. With q=sqrt(k²+lambda^-2), radial acceleration contribution is

`G M_j integral_0^infinity dk [k²/q] J1(kR) J0(kA_j) exp(-sigma²k²/2) / (1+q h)`.

Multiply by R for V². At lambda=infinity this is the Newtonian disk force; h=0 for gas. The normalization must be independently checked against a real-space softened-free Newtonian Gaussian disk control and a point-mass far field. No spherical substitution is allowed. Use finite-source forward curves for all three primary models so baryonic reconstruction error is shared. Separately report the N/NL comparison using the original published Newtonian components, which needs no inverse density reconstruction.

Numerical quadrature: k <= 8/sigma, at least 1024 Gauss-Legendre nodes initially; double nodes for convergence. Freeze any necessary numerical repair before opening test scores. Reconstruct also with 96 rings and sigma=Rmax/48 as a declared source-resolution sensitivity; report changes rather than choose whichever gives the preferred fit. If a substantial sample cannot pass the reconstruction contract, the finite-source comparison is inconclusive and the original-component N/NL diagnostic remains valid in its narrower processed-data scope. Do not relax thresholds after inspecting target residuals.

## Objective and reporting

Minimize mean over training galaxies of their mean squared log10(Vpred/Vobs), so each galaxy has equal aggregate weight. No independent-Gaussian likelihood, information criterion, significance, posterior, or sigma exclusion is inferred. A model predicting nonpositive total radial acceleration on selected rows is invalid there. Report train and test galaxy-equal RMS log velocity, median signed log residual, per-galaxy scores, row counts, parameters and boundary solutions. Report also original e_Vobs normalized residuals only as descriptive quantities with unknown correlations.

Use deterministic constrained optimization, documented starting points, and convergence diagnostics; for L check the best solution against N and vertex controls. Fit parameters only on train, then evaluate test once per declared model and sensitivity. Preserve failed fits and numerical errors. No rank ordering by test score is used to change models within this block.

Nuisance accounting: central D and i are fixed in the primary score. For a common change d=D/D0, radii scale by d, component V² by d at fixed angular profile and U, total masses by d², and a Yukawa scale enters through lambda/d in the fiducial physical profile. Published deprojected Vobs and its random error scale by sin(i0)/sin(i). Inclination also affects the source reconstruction/deprojection; the simple speed rescaling alone is not a complete re-reduction. Report these exact roles and the missing covariance. A declared sensitivity at D +/- one quoted error and i +/- one quoted error, independently per galaxy and clipped to positive D and 1..90 degrees, may give an optimistic prediction envelope with the frozen global parameters; label it an envelope, not a refit, marginalized likelihood, or confidence region. Do not hide these per-galaxy nuisance freedoms in the universal-parameter count.

## Cross-scale interpretation and falsifier

State the Solar-system normalization and the additional metric/polarization assumptions needed to use Cassini on L. For galactic lambda, mu times AU is tiny, so a specified linear metric response reduces to the PPN response class there; universal scalar/massive-spin-2 weights cannot be assigned an arbitrary optical gamma. Do not import the earlier single-pole benchmark as a new Cassini refit. NL approaches Newtonian behavior at high acceleration; compute that limit, but do not claim an ephemeris or light-deflection test without its metric and field equations.

The constructive falsifier is explicit: the same global law, G normalization and train-fitted constants must predict held-out galaxy curves from measured baryonic inputs without adjusting galaxy-specific gravity strengths. Report failure or inadequate source reconstruction honestly. Success on this processed sample is only a conditional cross-scale candidate, not unification or proof of the mechanism.
