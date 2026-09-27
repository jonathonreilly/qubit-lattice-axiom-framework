# Figure7 extraction review

Bounded extraction-only check, 2026-09-27. The fixed40min and120min slices support a rough positive-FT separation of about2.3MHz. This review does not compare a model, infer an underlying signed splitting, or supply an experimental confidence interval. Author extraction files were unchanged.

Read the protocol, full extractor and preserved JSON/log; inspected the300dpi page rendering and vector object inventory. Actual artifact names are `parity_profiles.json/log` and `figure7-page300.png`, rather than the dispatch shorthand. The author method uses source-axis interpolation, pixel blue contrast, local peaks with prominence.05 and minimum separation.6MHz, and retains all six times and their±.267min controls. It reads no model predictions. Peak-finding distance is a detection restriction, so it cannot establish absence of closer doublets; that restriction does not force the well-separated peaks at the two reviewed slices.

## Independent method and evidence

Used source PDF coordinates directly: x=79.097+187.408*t/120, and f=2.5+(y−645.716)*17.5/92.041 MHz. The background rectangle begins at y636.057, giving a bottom near.664MHz, not0. The plot top is20MHz. Its tick calibration is therefore consistent with the author formula; treating the bottom as zero would bias extraction.

The inventory has366 rectangles plus81 curves and46 lines. Rectangles alone are not a complete heatmap: at40min an upper-branch cell intersects x141.5663 but the lower feature is not separately represented by an intersecting rectangle; at120min a lower-branch cell intersects x266.505 but the upper one is absent from that rectangle subset. Absence from the rectangle list is not absence of a plotted peak. At40min the upper rectangle has y690.134..691.8786, center11.11117MHz. At120min the lower rectangle has y677.922..679.6671, center8.78931MHz. These are direct vector anchors, independent of rendering interpolation.

The saved independent script uses those vector row boundaries to construct source-bin rows, then averages blue-minus-red color over bin interiors and a small horizontal strip at each fixed time. This differs from the author's one-column pixel maxima/1-minus-red/scipy peak search: it returns source-bin centers rather than sub-bin rendered peak positions. Two windows8..9.8 and10..12MHz were chosen from the visibly separated features, without theory information. No frequency fitting or theoretical curve was used. This is a vector-registered image cross-check, not independent raw experimental data.

| Fixed time | Author nominal peaks MHz | Author separation MHz | Independent source-bin peaks MHz | Bin-center separation MHz |
|---|---|---:|---|---:|
|40min|8.7751,11.1480|2.3729|8.7893,11.1112|2.3219|
|120min|8.8208,11.1024|2.2816|8.7893,11.1112|2.3219|

All three time-offset controls at each of these two times give the same author pixel peaks. The independent discrepancies of about.051/.040MHz are well below one source bin, but should not be presented as an experimental accuracy estimate. The independent script and complete bin values are preserved as `independent_parity_bin_check.py/json`.

## Precision and scope

Source cell height approximately1.745PDFpoints corresponds to about.332MHz. Rendered pixel spacing about.0456MHz only oversamples that presentation. Decimal differences between pixel maxima at40 and120min need not show a resolved change in physical doublet splitting: both independent selections occupy the same two source-bin rows.

As a descriptive bin-localization illustration, the selected row edges are approximately8.623..8.955 and10.945..11.277MHz. Allowing each center anywhere inside its selected row gives a separation approximately1.99..2.65MHz. This is a geometric bin range conditional on peak-row identification, not an experimental interval, a rigorous uncertainty bound, or a claim that all physical estimation error lies there. Acquisition linewidths, finite Fourier window, drift, background contrast and plotting transformation remain outside it. The defensible report is roughly2.3MHz at each reviewed time, with source binning about.33MHz.

The20/60/80/100min slices were not independently re-extracted here. No maximum-over-time claim is established. The source-note detuning sign caveat remains: positive FT separation is a lower bound on the full energy-frequency parity splitting absent sign information, and must not be divided by6 when compared in energy-frequency units.

## Correction and provenance

Updated only the reviewer-owned `PARITY_SOURCE_REVIEW.md` to correct its prior misleading “0–20MHz” and raster-only description, with an explicit correction notice. The PDF is mixed vector/other paint; the PNG is a raster rendering. No author extraction or protocol was changed.

Source PDF SHA256 remains `49fd0df0facd4579af9c29d2ac0b91cf52badadb930134053d5d63c89c084382` (published Lescanne2019, printed page014030-9).

- `PARITY_PROTOCOL.md`: `147a0aada9d837c4978a4c74d89a685f2f4e07f924371fac3d54c9589556adf2`.
- `extract_parity_profiles.py`: `0233b6825a9db8f8afd5e961075d3e86ae3a021d162305d99880e3bff34e78e1`.
- `parity_profiles.json`: `28db925589ffadf1f953d30bc640aee67f53cb56777f67e331dde03b5df1b26e`.
- `parity_profiles.log`: `762fc4229ec61770a0c0f6310261d5824df58f3cb1237e4c1ab981b317de2921`.
- `page9-vectors.json`: `6f81c42f14ac106e29438fdca1bc8bfeebe5666b79d5a74e4824232e01c0dd54`.
- `figure7-page300.png`: `f16274ae2e4a74bfd9b748e5db030718d4ca0032b3131b819e19c80ef636768d`.
- `independent_parity_bin_check.py`: `4f8246f2df3ef89143734916b866020ee7376b7c75ad1572080e72d1f6e83f9c`.
- `independent_parity_bin_check.json`: `ace391e9e2a428783938c49fd478f8ee8bdec302f57577d69b49d59d0ea82237`.
