# Public HI products narrow the pressure-readout question

Status: conditional-support. Direct parent calculation, 2026-10-12.
This is exposed model development, not a blind test or a galaxy exclusion.

Eight official VLA-ANGST DDO125 products were downloaded and pinned before
calculation. The parent personally checked headers and wrote the extraction.
The predeclared grid has two centers, three inclinations, four position
angles, two imaging weights and three radial endpoint spacings:144 chords.
No best orientation, trimming threshold, source mass or theory parameter was
fitted. The observing and reduction source is Ott et al. (2012), AJ144,123;
the exact URLs and assumptions are in SOURCE_LEDGER.md.

## What is actually measured here

Moment2 in the files is a line width in m/s. Dividing by1000 before squaring
is required; the archive web page's km/s descriptions are not file units.
Column density is cm^-2. The stored natural beam is11.53764x10.63008arcsec,
the robust beam6.25644x5.41008arcsec. Pixel size is1.5arcsec.
At the supplied2.59Mpc distance the largest disk-plane beam FWHM ranges
.267-.339kpc for natural and .138-.183kpc for robust across the fixed
geometry grid. Thus the.09kpc annuli, especially their shorter chords,
must not be treated as independent, deconvolved radial measurements.

For each endpoint annulus, S is mean column density and Q is mean column
density times line-width squared on the same finite paired mask. Let
Delta=ln(Rhi/Rlo). The reported pressure-shaped diagnostic is

    p_proxy = -(Qhi-Qlo)/(Delta*(Shi+Slo)/2).

It is a finite difference of masked, convolved projected products. It is
not the intrinsic pressure term p(R0). The central column-weighted rms
line width ranges6.778-7.049km/s in the natural products and6.698-7.142km/s
in robust products. These ranges reflect specified geometries, not error
bars or independent repeated observations. They are not sigma_R estimates.

| Endpoint spacing, kpc | Natural p_proxy range, (km/s)^2 | Robust range, (km/s)^2 |
|---|---:|---:|
| .18 | 19.98 to82.01 | 12.66 to104.19 |
| .36 | 24.95 to71.18 | 20.08 to78.39 |
| .54 | 26.42 to62.93 | 23.31 to65.05 |

Every natural endpoint annulus has full paired coverage. The minimum robust
coverage is.998188; the affected missing pixels are counted without filling.
All144 rows, their endpoints, means, minus-log chords, coverage and beams
are in evidence_v1/RESULTS.json. The file also reports all48 geometry cases,
336 annuli and whole-map blank/negative/zero counts. No pixelwise standard
error or observational significance is asserted.

## What the equation permits

For intrinsic steady circular axisymmetric isotropic gas, with fixed
vertical shape and constant height,

    p = -R/Sigma * d(Sigma*sigma_R^2)/dR
      = -sigma_R^2 * d ln(Sigma*sigma_R^2)/d ln R.

Equivalently, the exact intrinsic interval identity is

    integral_[ln Rlo,ln Rhi] Sigma(R)*p(R) d ln R
      = (Sigma*sigma_R^2)(Rlo) - (Sigma*sigma_R^2)(Rhi).

This explains the numerator of the diagnostic. Replacing intrinsic endpoint
values by annular, beam-convolved maps and the integral weight by an endpoint
mean is an additional approximation, not an identity for the galaxy. If
height varies, the equation also contains sigma_R^2*d ln h/d ln R; mean
radial flows, anisotropy, changing vertical shape or a different tracer
conversion require more terms. Line width includes unresolved projected
rotation, expanding structures, thermal/random motions and instrumental
effects. The data pipeline's masks and noise matter as well.

The previous finite response certificate requires1113.2873(km/s)^2 at
R=.94kpc under its fixed matrix/source assumptions if only this pressure
readout changes. None of the tabulated smooth apparent-product chords
approaches that scale. But a point requirement imposes no interval lower
bound, and these statistics are not intrinsic p. Therefore this result
does not rule out an unresolved feature, a height or velocity-anisotropy
gradient, a different source reconstruction, noncircular motion or a
different gravity theory. It supplies actual data that a proposed pressure
rescue now has to model, rather than an adjustable unmeasured sigma.

## Reproduction and verification

Run read_moment_profiles.py with --data-dir pointing to the eight downloaded
files and --out to a new JSON path. The output is exclusive; original runs
are not overwritten. DOWNLOADS.json pins each public URL and byte hash.
PROTOCOL_FREEZE.json records the protocol before FITS access; the preserved
METADATA_RESOLUTION.md records the m/s correction and mask differences.

Six numerical/metadata families pass: hashes/units/shapes, common WCS and
round trip, consistent beam history, column-density/moment0 conversion,
synthetic constant/power-law/units controls and complete geometry accounting.
The WCS round-trip error is4.55e-11 pixels or less. The column/moment0
conversion is constant within1.80e-7 relative and agrees with the rounded
atomic/beam conversion within.03 percent. These are file/implementation
checks, not validation of the intrinsic pressure interpretation.

The frozen calculation carries no fitted response function, accepted
cosmology, new likelihood, retained-grade proposal or TOE. Next work must
either build an explicit three-dimensional beam/source readout for these
data or pivot to a theory bridge that predicts an additional observable.
