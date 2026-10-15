# M11 final v2 affected-source confirmation

This is a narrow supplement to the complete frozen-v1 `CANONICAL_REVIEW_v1.md` (SHA256 `bf5b72f13a3b2bd9e6c8114247b03d6312aeab6c60e6f64bdfebca7047511a79`) and identity `abb13a5a088980cfe57caf3a4f8a85be323c909038e9cee8b21f5c5a5dd3518a`. Those files and all earlier reports remain unchanged. The v1 cache remains a historical receipt; it is not relabeled as current. Root remains author. This is source/product correspondence, not formal audit or integrated landing approval.

I froze 19 final source/cache/output/receipt/copy files in `CANONICAL_INPUTS_v2.json` (SHA256 `eceaa6f246429b8ea2a79ea2d58426d170acbcc66fed7bd7a485fdd1d0e2afc4`), read the complete two-file source delta and checked it with `canonical_delta_binding_v2.py`. The primary changes one output interpretation string from “mean” to “signal.” The note adds the nonzero-mean witness and changes the corresponding interpretation labels. The three helpers, manifest and both protocol files are byte-identical to v1. No geometry, estimator, decoder, sample split, threshold, diagnostic or raw extraction algorithm changed.

The wording correction is mathematically appropriate. For U uniform on the complex unit sphere in C^N, E[U]=0 and E[Re(U_1)U_j]=delta_(1j)/(2N). Choosing R=1+kappa Re(U_1), 0<kappa<1, leaves the direction uniform and R strictly positive but gives E[R U]=kappa e_1/(2N). Hence the tone is a specified signal/location center, not necessarily the statistical mean. General radial laws may lack moments. The amended note now says this explicitly; it does not add a zero-mean premise. The radial-cancellation argument and its limits are unchanged. The open wording issue recorded in my historical v1 review is resolved in these v2 bytes.

Final checked identities:

| Item | SHA256 |
| --- | --- |
| Note | `571c6b8f108de2c4100653f0fd2509bf33745bb02b5bdee1d2c2b2530c7d71b3` |
| Primary | `57f4325cc686482d33dd41e24649d0a1d083f3fd832ef4bf61db1a583f998741` |
| Current cache | `c1211fc7597362593ffcb7179ecdf2f2b86bd8f3380c1e3fa5d251c879b6f362` |
| Current primary summary | `c677c53abe74dcd266af92cf3812dae6a29d1ed18501fe08d316e7db91e6b56b` |
| Unchanged row ledger | `47c52a45a6b5015522c80749f15e644328e2817b01cf17614628b679b99a8105` |
| Unchanged development source freeze | `e7e30d9e3914af0ec77bcc609285bc5f11a19ff7dd821e33d7ba3ee58c548487` |

Rebuilding the seven-input fingerprint gives `c9cf9938417ba5d0033bb94ea01fef22917e2505b86b64e1ecbf40616914f08a`, equal to the new cache header. The source-bound execution receipt records status ok, exit 0, empty stderr, 17.557219743728638 seconds of 180, and fresh cache. Cached stdout equals receipt stdout and contains the exact final summary. The author control lists and all empirical statistics equal v1: 51 passed and zero failed. These are inspected author execution receipts, not reviewer reruns.

All four `CANONICAL_v2_*` pack copies exactly reproduce their final output files; `EXECUTION_RESULT_v2.json` exactly reproduces the runtime receipt. The development summary differs from v1 only in elapsed seconds. The primary summary changes only primary hash, note hash in its source map, the interpretation string and the development-summary product hash. Every frozen path still matched live bytes when this binding check completed.

All 1,200 rows and the development source freeze are byte-identical to v1. Therefore the complete earlier all-row comparison remains applicable without another extraction or numerical pass. All six original tolerance failures across five Ka records remain recorded, including the maximum relative arc-width discrepancy 3.3101848395666877e-6 and normalized lower-score discrepancy 0.0006102597741957094. The original fixed-frequency diagnosis remains a separate diagnostic and does not replace those failures. All 2,400 discrete allocation-level outcomes still agree. No tolerance changed, no observation became an independent test, and no floating-point exclusion became an interval-certified physical-noise result.

`CANONICAL_DELTA_BINDING_RESULTS_v2.json` contains the exact check results and retained failures; `CANONICAL_SOURCE_DELTA_v2.patch` preserves the source delta. The accompanying `CANONICAL_AFFECTED_IDENTITY_v2.json` binds them and this report. I performed no new scientific aggregate, raw decoding, optimizer, sampling or geometry run for this supplement.
