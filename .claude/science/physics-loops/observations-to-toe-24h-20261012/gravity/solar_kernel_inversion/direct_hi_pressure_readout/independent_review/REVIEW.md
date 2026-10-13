# Independent check of the DDO 125 HI figure pressure diagnostic

Completed 2026-10-12, within the original campaign deadline. The parent authored
the scientific source; this is a focused independent source and arithmetic
check, not a formal audit, a new data fit, or a landing decision.

**Disposition: supported within the stated diagnostic scope. No materially
required source correction.** The red source identity, axis calibration,
distance conversion, chord calculation and conditional density-ratio bound
check out. The figure does not supply a measured pressure correction or an
unconditional exclusion. The note preserves that distinction.

## Source read and identities

I read the complete protocol, result note, extraction runner and result JSON;
then read the added source/download/distance receipts. I also read the small
plot runner, inspected its rendered output, read the prior pressure receipt
and source-distance metadata, and read the optional matter/radiation parent
disposition. All scientific source bytes stayed unchanged during this check.

| Source in the parent block | SHA-256 |
|---|---|
| `PROTOCOL.md` | `4baa6e5692d522e6b8e28dc2a5cd1cbe67850d3ae4ff3aa4e340484022dca267` |
| `DIRECT_PROFILE_RESULT.md` | `cbe210a50dd7a6ebfeb24c7ffc221e44b7665c3d14548180286fa8b9f66ae827` |
| `trace_profile.py` | `1ec3784382821825af20702cb416f14f9293f1dcb3a7f96a4bfa1c2057a8c7e4` |
| `evidence_v1/RESULTS.json` | `d2856f49d7b33bce96f87754c372824e11933e5d92917d37841ffc426ebb789a` |

The pinned PDF is Lelli, Verheijen, Fraternali and Sancisi (2012), *Dynamics of
starbursting dwarf galaxies. II. UGC 4483*, A&A 544, A145,
DOI `10.1051/0004-6361/201219457`. Its SHA-256 is
`3e32e882d9ad1b504c22fffbbca3b57bc83615c47b6629e8a356927b3e07e9b7`.
The supplied Figure 9 page render has SHA-256
`3639b226bfd6f2069ef2ffde3d63b358c94e1da8c701d610de2502cae33653da`.
These hashes were checked against the actual local bytes.

Figure 9 is on PDF page 9, zero-index 8, printed page 8 of 11. I visually
inspected that full page. Its caption identifies the red curve as DDO 125
(UGC 7577), the blue as UGC 4483, and the top panel as HI surface density.
The lower panels are optical brightness and rotation speed, respectively.
The dashed red top curve, rather than either lower curve or the red legend
stroke, is the selected object.

I read the continuation of Section 4 on PDF page 10 and visually inspected
the independently rendered full page saved as `source_page_10.png`. That
section gives the DDO 125 distance as 2.6 Mpc and the HI resolution as about
180 pc, and attributes the DDO 125 comparison to Swaters et al. (2009).
The paper's earlier 6–8 km/s discussion concerns UGC 4483. It cannot be
imported as a measured local DDO 125 dispersion. The note says this correctly.

The campaign's prior source receipt identifies UGC07577 with distance
2.59 Mpc, distance error 0.13 Mpc and source references `Sw09,Sw02`.
Its SHA-256 is
`c4d8134d3485d49ad3070dff55b422428d20a604e28d41619df59bfcf142095c`.
The compact distance pin matches that receipt's complete metadata exactly.
It remains a supplied nominal distance; no uncertainty propagation is claimed.

## Independent extraction and arithmetic

`independent_check.py` does not import or execute the author's extraction or
plot runner. It parses the original PDF content stream with `pypdf`, selects
the red stroked subpath by color, panel geometry and connected vertex count,
and extracts tick segments plus their actual text labels. It uses rational
least squares and rational interpolation, followed by 70-digit `mpmath`
logarithms. The author result is loaded only after the independent observable
calculation, for comparison.

The page has no `cm` transform or form `Do` operations. The selected source
uses a three-component ICC color space; its red identity is also directly
visible. The curve has 31 increasing-radius vertices and 30 connecting
segments. The disconnected two-vertex legend is excluded. The dashes are
display styling, not missing interpolation nodes.

The five labelled radius ticks are 0, 0.4, 0.8, 1.2 and 1.6 kpc. Their raw PDF
x coordinates are 357.536, 395.086, 432.568, 470.119 and 507.669 points. The
top-panel tick positions agree with the labelled bottom-panel shared axis.
The density labels are 0, 5 and 10 solar masses per square parsec, at raw
bottom-origin y coordinates 669.539, 709.428 and 749.248 points. Thus density
increases upward; the author's top-origin negative y calibration has the
correct sign. No logarithmic source axis was assumed.

Independent rational calibration of the original PDF decimal coordinates
gives maximum tick residuals of 0.0002941654 kpc and 0.0028854953 in the density
units. These are diagram calibration residuals, not observational errors.
The maximum raw-coordinate difference from the author result is only
0.000028809 PDF points, consistent with MuPDF's binary32 coordinate conversion.

Matching the same angular location gives, exactly at the declared nominal
inputs,

    R0 = 0.94 * 2.6 / 2.59 = 1222/1295 kpc
       = 0.9436293436293436... kpc.

Multiplying radius by the distance ratio in this direction is correct. This
is a coordinate comparison with the existing source point; it does not update
the finite matrix or claim a revised source fit. A constant radial distance
rescaling also leaves a logarithmic derivative invariant.

The prior pressure receipt has SHA-256
`03106e69c99aaeb9152bd0eebe7a4a0fde6c63d8a12c0e9af4b0566fa07eb06e`.
I reused its already checked conditional D requirement, without rerunning the
finite-source solve. Its stored exact rational value is approximately
1113.28732789047073475 (km/s)^2. It refers to one UGC07577 point at campaign
radius 0.94 kpc, with the other sources, rectangles, matrix and normalization
fixed as stated in the parent work. It is necessary, not sufficient.

Using that exact rational requirement and the independent curve gives:

| Centered width, kpc | Raw-decimal PDF chord, (km/s)^2 | Author chord | Displayed precision |
|---|---:|---:|---:|
| 0.09 | 72.5767940328 | 72.5766894394 | 72.58 |
| 0.18 | 52.9328202685 | 52.9331245780 | 52.93 |
| 0.36 | 25.4607070122 | 25.4606937408 | 25.46 |

The largest difference is 0.00030431 (km/s)^2. A separate independent
binary32-coordinate conversion, followed by the same rational calibration,
matches all three author values within 1.21e-13 (km/s)^2. This explains the
small parser difference without changing the physical interpretation or the
reported rounding. Extra arithmetic digits describe file reproduction only.

For the 0.18 kpc interval the independent raw-decimal trace ratio is
0.8536380551; the author's binary32 route gives 0.8536372785. Both round to
0.85364. The conditional sustained-pressure ratio bound is
0.035854557009902804. The required minus-log density slope is
17.395114498288605, and the local density scale is 0.05424680267107 kpc.
That 54 pc scale is below the approximately 180 pc nominal resolution.

An independent scalar pixel-to-segment calculation selects the same 820 red
pixels from the supplied render and finds a maximum distance of 0.5697567 PDF
points from the raw-decimal polyline. This agrees with the author's 0.5697506
after coordinate rounding. It verifies the selected display geometry, not
the HI observation, beam model, covariance, or intrinsic density gradient.

All five independent check families pass. Constant-density and power-law
profiles separately verify the sign, zero case and normalization of the chord
formula. Raw stdout and the empty stderr are preserved. There were no failed
independent checks or corrected scientific failures.

## Pressure equation and inference boundary

For the stated steady circular, axisymmetric, isotropic gas, with no mean
radial flow, the radial Euler balance gives

    v_phi^2/R = dPhi/dR + (1/rho) dP/dR,
    p = v_c^2 - v_phi^2 = -R/rho * dP/dR.

With P = rho sigma^2 and the supplied fixed vertical-shape relation
rho proportional to Sigma/h, this becomes

    p = -sigma^2 [d ln Sigma/d ln R
                 + d ln sigma^2/d ln R - d ln h/d ln R].

The signs and normalization in the note are correct. A changing vertical
shape or an unmodelled radial conversion between the plotted tracer and the
pressure-carrying density would require another term or premise. No such
conversion is measured here. The updated note expressly includes steady
circular motion and no mean radial flow.

If sigma = 8 km/s and h are constant over an interval, integration gives

    integral p d ln R = -64 ln(Sigma_hi/Sigma_lo).

Dividing by ln(R_hi/R_lo) yields the declared chord. It is the logarithmic
radius average of the correction for an underlying profile satisfying these
premises; it is not the correction at its center. Applying this operation to
a displayed line retains only a figure diagnostic. In particular, a nominal
one-resolution-element width does not establish independent endpoints or a
deconvolved gradient.

Only the additional premise that p is at least the required value throughout
the interval permits

    Sigma_hi/Sigma_lo <= exp[-(p_required/64) ln(R_hi/R_lo)].

The inequality is in the correct direction. A point requirement has no such
integral lower bound: it supplies no minimum width for a possible high-gradient
feature. The note and generated figure explicitly state that the certificate
does not impose interval persistence. They therefore do not silently turn the
point bound into an interval exclusion.

The displayed shallow profile cannot realize the sustained correction within
the supplied constant-dispersion/height model. That conditional statement is
supported. An unresolved feature, unknown dispersion or height gradients,
noncircular motions, geometry and beam/readout effects remain outside this
calculation. There is no measured local dispersion, error model, likelihood,
raw or deconvolved HI profile, or new independent holdout in this block. A
different readout of related Swaters source material is not an independent
statistical test. These limitations are stated in the parent source.

The positive tabulated quantity is minus the logarithmic density chord slope.
The current equations fix this sign unambiguously. Calling the table column
“minus-log density chord slope” would be an optional clarity improvement,
not a materially required correction.

## Provenance and operational scope

The source/download receipts preserve a reported Python certificate-verification
failure followed by successful system curl with normal TLS verification. I
verified their saved identities and the resulting PDF bytes; I did not replay
the network requests or independently reconstruct the earlier TLS environment.
The reported route failure has not been used as evidence against the science.

The JSON, protocol, author runner and previous input receipts have matching
embedded hashes. A possible escape-rendering ambiguity in the displayed
`f.write` line was inspected by parsing the source AST: it writes one actual
newline character. The saved result is valid JSON. This was not a runner
failure or evidence mismatch.

The additional plot reads the frozen result without fitting. Its dashed
comparison curve integrates the extra sustained-pressure premise from the
inner displayed density. The plot labels the dispersion as illustrative,
shows the nominal interval, states that no raw cube/error model is supplied,
and explicitly disclaims any inference of persistence from the point
certificate. The rendered plot is legible and consistent with the note.

I read the optional `direct_vector_matter_radiation/CHECKED_OUTCOME.md`, SHA-256
`c5c29efb132c07c210a3de0855ac35113a1199578924af84ea4f26326c5dda4c`.
It preserves the earlier review's distinction between parent results and
reviewer supplements, prescribed source controls and coupled dynamics, the
q=5 vertical instability, and calibration versus observational success.
No matter/radiation rerun or expanded verdict was performed here.

All review writes are under this new `independent_review` directory. No author
source, Git state, model setting, process, campaign deadline or external
application was changed. No AI worker, fit, formal audit, PR or landing action
was run. This is source readiness for the explicitly bounded diagnostic;
repository packaging, combined validation and landing are separate decisions.

`REVIEW_RECEIPT.json` supplies exact original/snapshot paths, hashes, check
artifacts, findings and dispositions. It is the machine-readable source closure
for this review. The original pinned source remains available in
`source_snapshot` together with the recorded first download failure.
