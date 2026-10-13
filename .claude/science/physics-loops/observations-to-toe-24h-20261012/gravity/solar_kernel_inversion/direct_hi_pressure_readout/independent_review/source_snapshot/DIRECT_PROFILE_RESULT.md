# The published HI profile does not supply the large pressure correction

Direct parent calculation, October 12, 2026. A diagnostic of an exposed
published curve, under explicit source assumptions; no likelihood or
unconditional exclusion.

## Source and numerical extraction

Figure9 of Lelli et al.2012, A&A544,A145,
[DOI10.1051/0004-6361/201219457](https://doi.org/10.1051/0004-6361/201219457),
plots the HI surface-density profile of DDO125/UGC7577 as a red dashed line.
The [version-of-record PDF](https://pure.rug.nl/ws/portalfiles/portal/75866939/aa19457_12.pdf)
was read, rendered and visually inspected. Section4 uses a2.6Mpc distance
and gives about180pc spatial resolution for this galaxy. The curve derives
from Swaters et al.2009; it is a different readout of related source material,
not a statistically independent new observation. No raw HI cube, local
dispersion or covariance was recovered here.

The runner extracts the exact red vector polyline in PDF page9, excludes
the disconnected legend segment, and calibrates against all five labelled
radius ticks and three density ticks. There are31 curve vertices.
Its values are figure-tracing precision, not measurement precision.
An independent render route checks820 red pixels against the polyline;
the largest distance is.570 PDF points. Axis rounding residuals are recorded.
The full source PDF/hash and the temporary render remain in the runtime
pressure directory; results preserve every selected vector segment and tick.

The old finite-certificate radius is.94kpc at2.59Mpc. Matching its angular
location on this figure gives R0=.9436293436kpc. This small distance
conversion is explicit. The prior lower-bound certificate and all model
matrices are unchanged.

## What pressure would require

For a steady axisymmetric isotropic gas in circular motion, with no mean
radial flow and pressure P=rho sigma², radial force balance gives

    p = v_c²-v_phi² = -R/rho dP/dR
      = -sigma² [d ln Sigma/d ln R + d ln sigma²/d ln R - d ln h/d ln R],

if rho is proportional to surface density Sigma divided by scale height h.
The last relation requires a specified vertical shape; changes in that
shape add another source term. It is not a consequence of rotation data.

If sigma and h are constant, the logarithmic chord defines

    p_chord = -sigma² ln(Sigma_hi/Sigma_lo)/ln(R_hi/R_lo).

For a smooth underlying profile satisfying these premises it is the
log-radius average of p over the interval. Applying it to a plotted
piecewise-linear curve gives only a resolved-profile diagnostic.

With the previously declared illustrative sigma=8km/s, the frozen
centered intervals give:

| Figure radius width kpc | Log-density chord slope | p_chord (km/s)² | Scope |
|---|---:|---:|---|
| .09 | 1.1340 | 72.58 | Below nominal spatial resolution |
| .18 | .8271 | 52.93 | Approximately one resolution element |
| .36 | .3978 | 25.46 | Two nominal resolution elements |

The finite D certificate requires p(.94kpc)>=1113.2873278904708(km/s)²
if only UGC07577 pressure shifts change and the remaining source matrix,
rectangles and coefficient cap stay fixed. This condition is necessary,
not sufficient. Under constant sigma8 and h, the corresponding point
log-density slope would be17.3951, with local density scale about54pc
at the figure's adopted distance. That scale lies below the reported
resolution; the curve cannot measure such a point derivative reliably.

An additional, stronger premise makes a resolved comparison possible:
suppose p>=1113.2873 persists throughout the .18kpc interval, with sigma8
and h constant. Integrating the pressure equation then requires

    Sigma_hi/Sigma_lo <= (R_hi/R_lo)^(-1113.2873/64) = .03585.

The displayed curve instead gives.85364. Thus the displayed resolved
profile with those supplied conditions does not realize a sustained
pressure correction of that size. The finite pointwise certificate itself
does not impose persistence throughout this interval. The comparison
cannot reject an unresolved narrow feature by silently adding that premise.

## Decision and next measurement

The figure provides no measured rescue of the failed finite response
family under the simple constant-dispersion/height picture. It also does
not by itself rule out the physical galaxy: dispersion gradients, flaring,
beam convolution, noncircular motions, inclination, vertical structure and
the actual velocity extraction remain unmodelled. In particular, the
6–8km/s dispersion discussed elsewhere in the source paper is for UGC4483,
not a local DDO125 measurement.

The next useful observation is a source-specific HI dispersion/column-density
cube or tabulation with beam, geometry and reduction metadata. A forward
beam/readout model can then test whether the correction is admissible.
Refitting response coefficients or replacing the pressure tracer with the
previous gravitational source inversion would not perform that test.

The initial Python download failed because its local certificate bundle
could not verify the issuer. System curl with normal TLS verification
succeeded; both attempts are recorded. This was a local route failure,
not a missing-science conclusion. No source fit or formal audit was run.
