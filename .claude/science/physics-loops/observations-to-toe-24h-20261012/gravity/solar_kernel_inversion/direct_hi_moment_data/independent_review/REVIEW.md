# Independent check of the DDO125 public HI moment diagnostic

2026-10-12. Focused source, geometry, arithmetic and inference review within
the existing campaign deadline. The parent remains the research author.

**Disposition: the frozen source is ready within its stated descriptive,
conditional-support scope. No materially required source correction.** All
144 chords and 336 annuli reproduce independently, with identical pixel and
mask counts. The largest pressure-proxy discrepancy is
7.105427357601002e-14 (km/s)^2. The essential m/s-to-km/s conversion was already
implemented correctly and documented before profiles. This result does not
identify the map statistic with intrinsic radial pressure or exclude a galaxy
or gravity theory.

This is not a formal audit, retained-grade promotion, combined repository
validation, or landing decision. There were no source edits, fits, AI workers,
Git operations, process changes or deadline changes.

## Exact reviewed source

I read the complete `PROTOCOL.md`, `SOURCE_LEDGER.md`, `METADATA_RESOLUTION.md`,
`DIRECT_MOMENT_RESULT.md`, `read_moment_profiles.py`, the input/download pins,
and the two claim/trace metadata notes. The complete result JSON was parsed
and compared against an independent reconstruction, including every geometry,
annulus, chord and repeated endpoint record. I inspected every chord's scalar
values. No author runner was imported or executed.

| File | SHA-256 |
|---|---|
| `PROTOCOL.md` | `23b6712015ee9d9a9260383840621cc8222376e44ff0c7b4870cc1d7f91804bf` |
| `SOURCE_LEDGER.md` | `74322ec9fb428bc859101d83697a538281b956e66ae3b1eb4ee84aa5fe4cb11e` |
| `METADATA_RESOLUTION.md` | `f300e7dc923d6a5cfdb69324fa6c6a6775f30f19bb333d36261809e20fc8229a` |
| `DIRECT_MOMENT_RESULT.md` | `e53f4557f2c4e5d2969a1df02c831f56e3e4b9ef66287642aedd26f24661ee6f` |
| `read_moment_profiles.py` | `f7e3b340bdfa188a93f25aec4591e9d5780242a09bf033f82c8fed5b23fcc9c8` |
| `evidence_v1/RESULTS.json` | `8cdd35a488b24c020854b7431858ff1e93f38fb310574431edf9327ae81591be` |

`REVIEW_RECEIPT.json` pins these and all supporting bytes. `source_snapshot`
preserves the source notes, original evidence, all eight compressed FITS
inputs, official downloaded HTML and retrieval receipts. The earlier source
and pressure receipts are separately pinned as reused premises, not rerun
science. Their identities remain respectively
`c4d8134d3485d49ad3070dff55b422428d20a604e28d41619df59bfcf142095c`
and `03106e69c99aaeb9152bd0eebe7a4a0fde6c63d8a12c0e9af4b0566fa07eb06e`.

## Source identity, units and reduction history

The saved official NRAO product page has a DDO125 row containing the exact
eight natural/robust Mom0CD, Mom0, Mom1 and Mom2 links. I parsed that actual
row independently and matched every downloaded name, original URL, HTTPS
retrieval URL, byte count and hash. No merely similar object or alternate
data product was substituted. All FITS headers identify `DDO125`.

The official page labels moments 1 and 2 in km/s, whereas every downloaded
moment-1/2 header says `METR/SEC`. Moment 0 is `JY/B*M/S`; Mom0CD is `CM^-2`.
The source uses the header units: it divides moments 0, 1 and 2 by 1,000 and
leaves column density unchanged. That is correct. The frozen protocol's
earlier web-unit statement is not silently rewritten; the metadata-resolution
note records the discrepancy and correction explicitly.

Ott et al.'s displayed second-moment equation includes the square root of the
intensity-weighted velocity variance. Thus the map is an RMS line width, not
a variance or spectral FWHM. Squaring after the m/s-to-km/s conversion is
correct; an additional Gaussian FWHM conversion would be wrong. Omitting the
division would multiply the variance/proxy by 10^6; multiplying by 1,000
instead of dividing would multiply it by 10^12 relative to the correct result.

The source paper's processing description confirms that the moment maps use
masked, flux-rescaled, primary-beam-corrected cubes. The publicly supplied
standard cubes have different corrections/masks. The archive masks include
manual decisions and suppress low-surface-brightness emission; robust maps
receive further column-density treatment. The parent does not claim to
reproduce them by a naive sum of the public cubes.

Ott's catalog row gives the J2000 center 12:27:41.8, +43:29:38 and alias
UGC7577. The observing rows give 12:27:40.9, +43:29:44. Both match the declared
grid. Ott's listed distance is 2.58 Mpc; using the explicitly supplied campaign
distance 2.59 Mpc is deliberate, not a claim that the source lists 2.59. The
earlier source receipt verifies 2.59 Mpc and i=63 degrees with listed error
3 degrees. Neither trial center is proven to be the dynamical center.

Stil and Israel's table row labelled D125 contains the quoted kinematic and
HI-isophote angles 135 and 118 degrees. Their global dispersion table contains
6.2 and 7.3 +/-1.5 km/s; the explanatory text identifies the scatter as spatial
scatter and describes Gaussian fitting and corrections. These are not local
moment-2 error bars. The grid uses supplied east-of-north trial angles, not
posterior samples or a recovered fit. In a future measured-geometry fit the
coordinate epoch/position-angle frame must also be specified; Stil's tabulated
center coordinates are B1950 and have not been substituted for the Ott centers.

The preserved protocol/download chronology is consistent with the recorded
freeze preceding downloaded-array access. That chronology is a saved provenance
claim, not an independent reconstruction of every earlier session action.
Selection followed the prior model discrepancy, so development-only status
is appropriate regardless. No blind-test credit follows.

## Independent geometric reconstruction

All eight maps have 1024 by 1024 spatial cells, two singleton extra axes,
floating `BITPIX=-32`, and matching spatial WCS cards. They use RA/DEC SIN,
zero rotation, no CD/PC matrices or slant-PV terms, reference pixel
(512,513) in FITS one-based coordinates, and reference sky position
(186.920416667,43.4955555556) degrees. The angular step is approximately
1.5 arcseconds, with decreasing RA along increasing image x. Epoch/equinox
is 2000 in the respective old/new header forms.

I reconstructed this map directly, without an `astropy.wcs` call. For the
reference radial, east and north unit vectors n0,e0,t0 and intermediate SIN
coordinates xi,eta in radians, the celestial unit vector is

    u = xi e0 + eta t0 + sqrt(1-xi^2-eta^2) n0.

For each trial center's basis n,e,t the gnomonic lengths are

    E = D (u dot e)/(u dot n),   N = D (u dot t)/(u dot n).

The thin-disk radius is the norm of the major-axis component and the
minor-axis component divided by cos(i). This derives the projection directly
from the header and trial geometry. The direct inverse projection closes to
3.49e-11 pixels over the whole map, and unit-vector normalization to 5.56e-16.
These are floating implementation checks, not interval certificates.

The independent cell selections reproduce all parent annular counts exactly.
The minimum cell-to-annular-boundary margin in this calculation is
2.7312340e-8 kpc. There is no observed boundary-cell disagreement.

The map statistic is an equal-cell mean on the SIN image grid. It is not an
exact solid-angle or disk-area integral. Across selected cells the solid-angle
Jacobian differs from its reference value by at most 1.46e-7; the disk-area
Jacobian, apart from its common constant, ranges from 1.0000000188 to
1.0000004953. These very small geometric variations do not change the stated
finite pixel-mean operation. A forward physical integral should nevertheless
specify its area convention.

## Masks, arithmetic and all-row comparison

Natural maps have 34,766 finite pixels each. Robust Mom0CD has 32,267 and
moments 1/2 have 31,844. Robust Mom0 has 34,693 finite pixels including
484 negatives. Natural Mom2 has 24 exact zeros; robust Mom2 has 1,090. There
are no infinities. The obsolete robust `BLANK=-1` keyword is invalid for these
floating arrays; actual missing data are IEEE NaNs. The ordinary Astropy
warning is retained rather than reinterpreted as a mask instruction.

The independent check applies the stated distinction between finite
nonnegative column-density coverage and the strictly positive-column,
finite-nonnegative-line-width paired mask. It retains zero widths, performs
no blank interpolation or extra clipping, and uses the same paired cells
for S and Q. Direct compensated `math.fsum` cell sums provide an independent
arithmetic route. All coverage, missing, negative and zero counts match.

Natural annuli have full paired coverage. Every affected robust annulus has
one missing moment-2 cell and no missing column-density cell. The smallest
paired coverage is 551/552 = 0.9981884057971014. Those missing cells are
excluded, not set to zero. Pixel counts and geometry cases are not independent
sample counts, and natural/robust products share observational provenance.

Every one of the 48 geometry cases, 336 annuli and 144 chords was compared,
including all duplicate low/high endpoint records. The comparison covers
12,011 numeric leaves, as well as record identities and schema keys. No
numerical discrepancy exceeds ordinary arithmetic rounding:

| Compared quantity | Maximum discrepancy |
|---|---:|
| Pixel/mask counts, coverage, S and density chord | exactly zero |
| Q | relative 4.17e-16 |
| Column-weighted RMS width | 1.78e-15 km/s |
| Minus-log Q chord | 1.45e-15 |
| Pressure-shaped proxy | 7.11e-14 (km/s)^2 |
| Disk beam covariance | 6.94e-18 kpc^2 |
| Disk principal FWHM | 1.12e-16 kpc |

The very large absolute units of Q make its absolute floating difference
look large; the relevant discrepancy is relative to its roughly 10^22 scale.
These numerical tolerances are not data uncertainties.

| Endpoint spacing, kpc | Natural p_proxy, (km/s)^2 | Robust p_proxy, (km/s)^2 |
|---|---:|---:|
| 0.18 | 19.9829799954 to 82.0100184609 | 12.6619453652 to 104.1917928563 |
| 0.36 | 24.9537197359 to 71.1763041191 | 20.0802064028 to 78.3889844717 |
| 0.54 | 26.4196769092 to 62.9281438810 | 23.3103955041 to 65.0497337113 |

The central column-weighted RMS ranges are 6.777529142–7.049336546 km/s
(natural) and 6.698353342–7.141687395 km/s (robust), matching the note.

Natural column/Mom0 conversion is 9.005379171594862e21 per Jy/beam km/s,
with maximum relative nonconstancy 1.79398e-7. Robust is
3.2628506042861326e22 with nonconstancy 1.64754e-7. Both reproduce exactly.
The reported agreement with the author's rounded atomic/beam normalization
is 0.02821% and 0.02191%, correctly below 0.03%. An independent calculation
using the SI Rayleigh-Jeans conversion and Gaussian beam solid angle gives
agreement of 0.01836% and 0.01206%, while still supplying the conventional
rounded HI column coefficient. These are unit/file consistency checks;
Mom0CD and Mom0 are derived from the same data, not independent measurements.

## Gaussian beam and synthetic controls

No standard BMAJ/BMIN/BPA cards are present. Each map has one consistent
CLEAN-history beam for its weighting: 11.53764 by 10.63008 arcseconds at
-68.22 degrees for natural, and 6.25644 by 5.41008 at -80.10 degrees for
robust. These agree with Ott's rounded table values.

For beam major/minor FWHM a,b, relative angle delta, and q=cos(i), I independently
formed the squared-FWHM matrix in the disk coordinates:

    F11 = a^2 cos^2(delta) + b^2 sin^2(delta)
    F22 = [a^2 sin^2(delta) + b^2 cos^2(delta)]/q^2
    F12 = (a^2-b^2) sin(delta)cos(delta)/q.

Its determinant is a^2 b^2/q^2. The eigenvalues follow from the scalar
trace/discriminant quadratic, rather than the author's matrix eigensolver.
Multiplication by the angular-distance scale and division by 8 ln(2) for
covariance reproduces every beam. Face-on and circular-beam controls check
rotation invariance and the sec(i) minor-axis stretching.

The largest disk-plane FWHM ranges are 0.267253042–0.339389100 kpc (natural)
and 0.138292973–0.183191554 kpc (robust). This is a local linear Gaussian-beam
description, not an exact global convolution/deconvolution operator. The
0.09 kpc annuli are below those scales. No independence or intrinsic radial
resolution follows from the 1.5 arcsecond cell size.

For synthetic S=R^(-a), Q=49 R^(-a-b), set r=sqrt(Rlo Rhi) and
h=ln(Rhi/Rlo)/2. Independently,

    p_proxy = 49 r^(-b) sinh[(a+b)h] / [h cosh(ah)].

This closed expression reproduces all five frozen constant/power-law cases,
including slope signs and the zero case. A separate 8,000 m/s control gives
64 (km/s)^2 after conversion. No synthetic pass is treated as a test of the
galaxy's physical state.

## Physical interpretation and remaining imports

For intrinsic steady circular axisymmetric isotropic gas with the supplied
vertical-shape/tracer relation and constant height,

    Sigma p = -d(Sigma sigma_R^2)/d ln R.

Integrating gives precisely the endpoint identity in the note. A variable
height adds +sigma_R^2 d ln h/d ln R. The signs are correct. The reported
proxy replaces intrinsic endpoint products by masked annular projected
moments and replaces the integral weight by an endpoint mean. Those are
additional approximations, not an identity that converts the map into p(R0).

The missing physical imports remain substantial: intrinsic three-dimensional
gas structure and radial dispersion, optical-depth/tracer-to-mass conversion
(the published column map already supplies the usual HI emission calibration),
height and its gradient, geometry and noncircular flow, anisotropy, the
instrumental spectral/spatial response, and the actual mask/noise/reduction
map. Moment 2 also contains unresolved projected velocity gradients and
multiple components. Beam smearing need not permit a simple one-sided
pressure bound; the mask/noise and varying source fields prevent that inference.

The prior finite-matrix number 1113.2873 (km/s)^2 remains a necessary
pointwise requirement under its original fixed-source assumptions. It is not
a required integral or annular proxy. All tabulated proxies are much smaller,
but neither that comparison nor the apparent profile smoothness excludes an
unresolved intrinsic feature. The note correctly states these limitations and
does not claim a likelihood, significance, blind holdout, deconvolution,
intrinsic sigma_R measurement or galaxy/theory exclusion.

The trace/claim metadata retains conditional support, identifies the missing
physical observation map and forbids proposal/retained promotion. Its target
category does not make the present data diagnostic a new physical theorem.
No material assumption was silently converted into an adopted framework axiom.

## Preserved failures and reproduction

The first independent run stopped before profile calculations because I
compared the saved newline-separated FITS header string with Astropy's default
unseparated serialization. This was a reviewer formatting error, not a FITS
or author-source mismatch. The exact failed source is
`independent_check_v1_failed.py`; stdout/stderr are `CHECK_v1.*.txt`.
`HEADER_COMPARISON_FAILURE_v1.txt` preserves the initial comparison evidence.
The subsequent wrong-separator debugging parse produced spurious card warnings;
`HEADER_STRING_DIAGNOSIS.json` explicitly preserves a reproduction of those
warnings and the diagnosis. They are distinct from the real, expected BLANK
warning in the downloaded floating FITS headers.

Using the proper separator matches every complete original header string
exactly. The corrected source is `independent_check.py` with SHA-256
`7793f59e8fed006ed4b5d6b65d8b6267913fd716de7c6c8a2f8f303043d85d01`.
Its successful output is `CHECK_RESULTS_v2.json`, SHA-256
`147303eaee53f2b822b13c2a8da4375fae42d6b2ecc4fa22409fa6b687b97d4e`;
the raw second stdout and empty stderr remain preserved. The original author
source, freeze, download receipts and results were never edited. The earlier
reported missing-bs4 route failure also remains pinned; it did not invalidate
the data or require installation for this check.

Reproduction uses the supplied isolated interpreter and the review's own
snapshot inputs. The successful checker deliberately writes its output
exclusively; use a disposable copy of this review directory to run it again
without replacing immutable evidence. No original author runner needs to run.
All review writes are confined to this new `independent_review` directory.
