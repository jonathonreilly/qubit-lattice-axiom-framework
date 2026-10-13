# DDO 125 public moment-map diagnostic

Frozen before opening the FITS arrays, 2026-10-12. Direct parent authorship.
Status: conditional-support; observation-driven model development.

The earlier finite response matrix requires an additional pressure term of
1113.2873278904708 (km/s)^2 at UGC07577 R=0.94 kpc if only this source's
pressure correction changes. That is necessary within the frozen matrix,
not sufficient, not a measurement, and not an interval requirement.

The Lelli figure and its shallow density chord, the published Stil/Israel
global dispersions, and the Ott survey methods have already been exposed.
The FITS arrays have not been opened. This source was selected because the
finite model failed: these are development diagnostics, not a blind holdout.
No response function, mass model, inclination or distance will be refitted.

## Inputs and frozen extraction

Use the official VLA-ANGST DDO125 natural and robust column-density, moment-1
and moment-2 products. Retain original compressed bytes and headers with
hashes. The archive's moment 2 is a line width in km/s, not its square.
Read metadata and verify dimensions, WCS, beam, units, blank masks and
coordinate agreement before computing profiles. Abort the affected
comparison if those checks fail; preserve the failure. Cubes are not needed
for this first diagnostic and are not to be silently substituted for the
mask/rescaled/primary-beam-corrected moment products.

Use the original source distance 2.59 Mpc and R0=0.94 kpc. Use two explicit
J2000 centers from Ott2012: catalog 12:27:41.8 +43:29:38, and observing
pointing 12:27:40.9 +43:29:44. Neither is asserted to be the dynamical center.
Inclinations are 60,63,66 degrees (original 63 +/-3); position angles east
of north are 118,120,135,150 degrees. The 135 degree kinematic and 118
degree HI-isophote angles come from Stil/Israel2002; the other two bracket
the former. Treat these as finite sensitivity choices, not probabilities.
No best geometry will be selected after seeing the arrays.

Construct elliptical sky radii using exact WCS sky positions, local tangent
east/north offsets and a thin-disk projection. At R0 plus/minus half widths
0.18,0.36,0.54 kpc, take annuli of full radial thickness 0.09 kpc. Also
tabulate the central annulus. Keep these below-beam samples explicitly
correlated and resolution-limited; no intrinsic derivative is inferred.

In each annulus report total pixels, valid nonnegative column-density
coverage, area mean column density and valid moment-2 coverage. Use the
common positive-column/finite-nonnegative-line-width mask for paired
pressure diagnostics. Report its mean column and column-weighted mean
line-width square. Pixel counts are not independent sample counts.
All omitted/negative/blank values and coverage are counted. No interpolation
over blanks, noise clipping, spatial smoothing, sigma floor or data-driven
trimming is permitted. Natural and robust products stay separate; different
beams are a diagnostic comparison, not repeated independent measurements.

## Observable and conditional physics

For two endpoint annuli define S=mean(N_HI) and Q=mean(N_HI * m2^2) on
the same valid paired mask. Let Delta=ln(Rhi/Rlo). Report

    C_S = -ln(S_hi/S_lo)/Delta,
    C_Q = -ln(Q_hi/Q_lo)/Delta,
    W2 = Q/S,
    p_proxy = -(Q_hi-Q_lo)/(Delta * (S_hi+S_lo)/2).

These are finite differences of masked, beam-convolved published products.
p_proxy has (km/s)^2 units; it is not a measured pointwise pressure term.
Under additional steady axisymmetric circular isotropic-gas assumptions,
fixed vertical shape and constant height, the intrinsic continuum equation
is p=-sigma_R^2*d ln(Sigma*sigma_R^2)/d ln R. With height variation it
acquires +sigma_R^2*d ln h/d ln R. Converting the line-width products to
that intrinsic equation requires a three-dimensional/source/beam/mask model.
This block supplies none. Global 6.2 and 7.3 +/-1.5 km/s values are context;
the latter scatter is across the galaxy, not a local measurement error.

Numerical checks: unit/shape/WCS consistency; natural moment0/column-density
conversion if available; constant and power-law synthetic profiles for
finite-difference signs; WCS pixel/sky round trips; beam projection and
Gaussian covariance algebra checked independently. Report all geometry rows,
not selected outcomes. Make no significance, likelihood, deconvolution,
holdout-success or galaxy-exclusion claim.

Next useful question: what intrinsic gas/source reconstruction would be
required to convert these measured products into a pressure bound compatible
with the original rotation data? Preserve the result even if the answer
requires a local pivot.
