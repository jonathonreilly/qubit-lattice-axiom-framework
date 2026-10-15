# M11 canonical source and data correspondence, frozen v1

This is a focused computational/source review by `/root/inertial_response_check`. Root remains the scientific author. It is not a formal audit, an integrated-main validation, or approval to infer a physical receiver covariance. I read the complete frozen primary runner, three helpers, input manifest, both protocol files and the complete canonical note. I replayed only comparisons of already frozen rows and source/product identities. I did not rerun raw decoding, spectral estimation, continuous-frequency exclusion, synthetic sampling, or the scientific aggregate.

The v1 implementation preserves the independently reconstructed data and the author's working calculations. All 1,200 canonical rows are byte-identical to the original working ledger. All discrete decisions agree with the independent implementation. **Six original tolerance failures across five Ka records remain failures.** The successful 51-control author envelope does not remove them.

During this review root identified an interpretive issue in v1: the permitted direction-dependent radius does not imply zero-mean error. The frozen v1 note and primary still use “mean” in places where “specified signal/location center” is justified. This report preserves those bytes as historical and leaves that wording issue open; a later source-bound supplement must check the correction. No live edited source is silently substituted into this report.

## Frozen scope and closure

`CANONICAL_INPUTS_v1.json` froze 14 files before the full canonical inspection: primary, seven declared inputs, cache, four output products and execution receipt. Its SHA256 is `4edcd1ccf0aabdad7ebc12abd5f4bb006779a85880fadd81f16b316819e75d59`. The mirrored copies in `canonical_inputs_v1/` reproduce every declared byte count and hash. `canonical_binding_v1.py` independently checks those identities, the ordered runner input fingerprint, output links, raw input hashes, import closure, and the original comparison equality. Its results are in `CANONICAL_BINDING_RESULTS_v1.json`.

Key v1 identities:

| Item | SHA256 |
| --- | --- |
| Primary | `256f62863ff7c7f5e5aaf141bf44c03426f5711d6d45b16de8a8e58bfd29fdfd` |
| Complete canonical note | `6e321840bf78a2687fb516aca2e46da293c72c9499dd5175bf5434da017fcb10` |
| Geometry helper | `c9b1e47cbaeaa8faf31543541e983c19f23a4e4d1fdfebae88e1e0590843e7aa` |
| Development helper | `b2de0a9f609f852acfceb5b8adfafcc958f3c68674f6acc8dd84ea5b54575905` |
| Sampling helper | `5cf7f2a6ef97f007b77edb1a1d055541c8546ce8a92a7ba7133049456aa4304c` |
| Input manifest | `e97df7132ac49fc31b2de89f7419afd82762f430fd4996de09bd1760cb1c127a` |
| Original/final v1 row ledger | `47c52a45a6b5015522c80749f15e644328e2817b01cf17614628b679b99a8105` |
| v1 primary summary | `06847880a4e1ec1610c1b9f6a281a64b081c86a6da79032556ecde2a1eaebf80` |
| v1 cache | `afba605d5723db6d690229cace2b18b11a9153e92b503001eb7e8626132ff8d2` |

The primary's seven `AUDIT_INPUT_PATHS` match the snapshot manifest and summary, in order. Rebuilding the fingerprint yields `720da3f7b4e37876fbc16445a18649c2ae2107afe82e8b4b4397214e78b68f16`, equal to the v1 cache header. The receipt records exit 0, empty stderr, 17.86530041694641 seconds, declared timeout 180, and a fresh cache. Its stdout equals the cached stdout; the final JSON equals `SUMMARY_v1.json`. The 51 author checks comprise 26 geometry, 9 sampling, 6 receiver and 10 development checks, with zero failed checks. These are author-run checks inspected here, not 51 new reviewer executions and not the separate mathematical reviewer's controls.

`SUMMARY_v1.json` binds all seven inputs, the primary and three subordinate products. The development `SOURCE_FREEZE_v1.json` binds its five source dependencies and four registered raw/label identities. I rehashed those four existing raw/label files without decoding them; all hashes match. The new manifest is self-contained. Its historical protocol references are provenance text, not undeclared imports or reads of old helper source.

The source imports only the three new local helpers plus standard-library, NumPy and SciPy facilities. No earlier unpublished RSR or carrier helper is imported. The optional network acquisition branch is explicit, host-restricted and hash-checked; I did not invoke it. The default scientific path reads the registered local files. It writes the four declared products. The sampling helper has a separate standalone output branch; when called by the primary, its controls are embedded in the primary summary instead.

## Decoder, estimator and diagnostics

The canonical development helper independently contains its label-schema parser, header reader and signed IQ extraction. It reads 32-bit big-endian words as high signed-16 Q and low signed-16 I, and uses `z=(2I+1)+i(2Q+1)`. It checks the pinned product and label hashes first. The fixed first 600 one-second records of each product cover UTC seconds 48900 through 49499 at 1,000 samples/second. The earlier blind extraction used a distinct `struct` path and froze full raw/header and corrected-IQ evidence; all 1,200 corrected-IQ hashes still agree.

Each frequency estimate uses only samples 0:500. The canonical estimator takes the largest bin of a 16,000-point FFT and refines that bin's ±0.0625 Hz neighborhood, then wraps modulo 1,000 Hz. This is the specified local estimator, not a guarantee of a globally best carrier. The validation projection, diagnostics and exclusion calculation use only samples 500:1000 and centered times. The source's sample-split fixture changes the latter half while preserving the training half and verifies identical estimated frequency. It is a source/implementation check, not evidence of statistical independence between halves.

For validation residual r and E=sum|r|², the published complex lag diagnostic is sum r[n+k]conj(r[n])/E. The pseudo-covariance is sum r[n]²/E. These are descriptive normalized residual statistics, not an unbiased or physical covariance estimate. My original ledger additionally retains alternative normalizations. The low and high non-DC DFT bands have complex ranks 248 and 251; the published low/high quantity is energy per rank. No fitted noise scale or alternate covariance is inserted.

All selected records remain represented. The canonical ledger retains its declared error/extreme fields and aggregate header setting histograms; it does not publish every field in the 71-field independent header ledger. The full raw inputs, the latter ledger and previous correspondence evidence preserve the broader header context. This review does not relabel the canonical rows as full-header dumps. Both products were already exposed development material.

## All-row correspondence and preserved failures

`canonical_row_comparison_v1.py` compares all canonical rows to the frozen independent rows. It executes no author source. Its result and per-row difference ledger equal the original author-working comparison exactly. Canonical and working row files are byte-identical. Their development summaries differ only in source-freeze hash and elapsed seconds.

Maximum training-frequency difference is 1.017407953440852e-7 Hz. The maximum residual-energy difference divided by validation energy is 3.510359570673759e-8; normalized lag-component and pseudo-covariance differences are 3.5435531231531314e-8 and 5.093932947675128e-8. The maximum relative per-rank color-ratio difference is 7.647114586006865e-8. All 2,400 allocation-level enclosure and exclusion classifications and all partition cell counts agree.

The retained failures against the original 5e-7 comparison limits are:

| Ka record index | Metric | Difference |
| --- | --- | ---: |
| 324 | Family arc half-width, relative | 1.4390139634334886e-6 |
| 512 | Pointwise arc half-width, relative | 7.690169679941405e-7 |
| 566 | Pointwise arc half-width, relative | 1.8628129174746988e-6 |
| 586 | Family arc half-width, relative | 7.944498205958439e-7 |
| 595 | Family arc half-width, relative | 3.3101848395666877e-6 |
| 595 | Family normalized lower score | 0.0006102597741957094 |

The already frozen targeted diagnosis shows that evaluating both independent paths at the same reported frequency reduces the arc discrepancy to 1.7763568394002505e-14 and score discrepancy to 3.2810698602503408e-12. Tiny optimizer differences propagate through the small margin and arcsine map; the original endpoint/score failures remain recorded, not replaced by the common-frequency experiment. Neither tolerance nor row was changed. Ka595 remains non-excluded in both paths. See the original `ARC_CONDITIONING_RESULTS_v1.json` and `AUTHOR_CORRESPONDENCE_REVIEW_v1.md` for the full calculation.

Pointwise allocation gives numerical exclusions X=489/600 and Ka=592/600; family allocation gives X=168/600 and Ka=578/600. No arc was obtained for 0/8 X/Ka records pointwise and 0/21 family. These outcomes are retained, not clipped. The family calculation uses alpha=.01/1200, split alpha/2 for carrier and alpha/4 for each color tail. These are fixed-procedure conditional-model statements, not an independent empirical validation or interval-certified exclusion.

## Mathematical and interpretive source scope

All ten geometry production functions are AST-identical to the frozen working geometry; only its `controls` function changed, adding four boundary/outer-arc checks. I read those additions rather than rerunning the suite. The code implements the previously checked real-arithmetic construction: complex-rank ratios, conservative ADC ball, strict Dirichlet outer arc, two tail scores, and midpoint Lipschitz margins. The numerical path expressly lacks outward-rounded intervals. It is therefore not a certified enclosure of floating-point roundoff.

The complete note states the supplied conditional uniform-direction law, positive radial factor, single-tone signal, uniform cadence, ideal unsaturated ADC cells and training conditioning. Those premises are not derived from gain settings or residual spectra. It separates arbitrary radius cancellation from physical noise calibration, covariance-isotropy from a spherical direction law, and a training-only estimator from validation-selected frequency. The sampling source tests synthetic witnesses for these distinctions; its tail frequencies and exact Dirichlet comparison are not new observational evidence. The displayed FIR example establishes that filtering can correlate samples; it does not identify the actual receiver filter or repair conditional independence.

The open v1 wording issue is real but does not alter the radial-cancellation identities. For U uniform on the complex unit sphere in C^N and R=1+kappa Re(U_1), 0<kappa<1, R is positive, E[U]=0, and E[R U]=kappa e_1/(2N), since E[Re(U_1) U_j]=delta_(1j)/(2N). Thus `c*u_f` is a supplied signal/location center, not necessarily E[y]. A physical mean or covariance might not even exist for a general allowed radius. Root announced a correction after this snapshot; this report does not pre-approve its final wording or cache.

I checked the note's empirical numbers and scope against the frozen data and inspected source. I did not perform a fresh primary-document review, a full general statistical-theorem audit, or an integrated landing check. No new fit, calibrated physical noise bound, sky phase, scalar inference, initial-state selection or independent gravity test follows from this computational correspondence.

## Preserved provenance

Original pre-exposure source, independent rows, headers, initial report and identity remain unchanged. The source correspondence report `32f948ecdd8e0892265b3bb649400d895b6ee087ddd1e93650b54950bdda23cb` and its identity `4c94407f77ee85b5c486e0a18a360331cee642ff2cfffbd49c791c9639923b78` retain their original scope. The original comparison result `d195487cc9c2e621f930e45a08d5f04dba6377682ec43278b65c7baa086e5d65` and conditioning result `b17abe6a0ee7115a5b2d5ccf5fb3fcf2a829aa30db0ecd984fee5a8e6f86cf72` are not relabeled as canonical or recomputed science. The accompanying `CANONICAL_IDENTITY_v1.json` binds this report, the v1 snapshots and new comparison-only evidence. Subsequent live source changes are listed separately in the binding result and remain outside this v1 review.
