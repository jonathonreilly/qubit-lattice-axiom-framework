# Direct check of the inherited polarization-data comparison

I personally recomputed the fixed public-data comparison on October 12, 2026,
without refitting or changing the inherited split. This is post-exposure
verification of an existing development comparison. It is not new independent
test data. The original freeze remains unchanged at SHA-256
`0e4dc14ae089be908dcfcdc26c07dffa7c3bea57c50cc13b32b7d3a6ef2cf46e`.

The primary source is [Song et al.](https://www.nature.com/articles/s41467-025-66258-x),
with the [versioned data release](https://doi.org/10.6084/m9.figshare.30499499.v1).
The original source workbook hash is
`dcb11e46c0e61d09a22d2ef6c6778e3afb0fc1b1f5bbe218581597c133950e15`.
The publication's coordinate, coincidence and apparatus interpretation remains
as qualified in RESULTS.md; no new source-map certainty is asserted here.

Using a named-sheet openpyxl read independent of the inherited direct XML
extractor, I matched all 36 calibration/test observation records to Figure4d:
108 coordinate/count/error cells. The result field `source_cells_verified=36`
counts source-cell ranges (one three-cell range per record). A separate
arcsin/tanh implementation reproduces every frozen count mean within
3.7e-12 counts. No original prediction helper was imported.

| Fixed model | Calibration weighted square | Test weighted square | Test with supplied local prediction covariance |
| --- | ---: | ---: | ---: |
| Boundary alternative | 207.563040 | 1447.844250 | 357.181927 |
| Quantum cosine | 230.710642 | 420.641269 | 303.737613 |
| Triangular baseline | 5480.587186 | 14117.420390 | 3502.282485 |

The frozen cosine comparison has the lower development-test score. These
scores remain descriptive: the covariance calculation is checked as matrix
arithmetic using its frozen inputs, not validated as statistical coverage.
No new fit, physical preference significance, or fundamental-law rejection
is inferred.

For any two equivalent-setting records y1,y2 with stated positive errors,
completing the square gives

    min_m [(y1-m)^2/s1^2 + (y2-m)^2/s2^2]
        = (y1-y2)^2/(s1^2+s2^2).

Summing this exact rational quantity for the eight calibration pairs gives
202.55428203986662. Thus any stationary angular mean under the inherited
coordinate map incurs that much weighted mismatch before its shape is chosen.
This check narrows the interpretation: the poor listed-error fit cannot be
ascribed solely to the proposed fundamental correlation law. Drift, response,
coordinate interpretation and count processing remain unresolved possibilities.

The initial system-Python route lacked openpyxl and failed before data or
calculation. Its source and import error are preserved. The identical source
then ran successfully with the supplied workspace Python runtime; no packages,
model settings or scientific inputs were changed. Reproduce with that runtime
and direct_song_readout_check.py only in a fresh output directory or preserved
copy, because the script intentionally refuses to overwrite the existing
execution receipt/results. Runtime provenance and source checks are saved in
direct_song_recheck_evidence/. This is parent verification of inherited results,
not a claim to have independently authored or calibrated the original fit.
