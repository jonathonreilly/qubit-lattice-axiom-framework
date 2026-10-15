# Focused M9 canonical empirical source correspondence, v1

The canonical receiver preserves the independently checked raw extraction, header coverage, corrected-I/Q digests and conditional ADC-cell formula. Its shared character/interval functions and three new analytic fixtures are correct. The NCO helper implements the stated exact recorded-number polynomial join and retains both supplied time arguments. No unresolved mismatch remains in this assigned scope. This is a focused source correspondence check, not a formal audit, complete mathematical review, physical phase calibration, or final cache acceptance.

## Frozen independent evidence reused

The original independent extraction identity remains `869f984541def9f9103a5063462243a52aa337343fae70af3434c7c6a190f10b`; its report remains `1ea7a956229b4e1ab56fc2310f2054022f7be6485a047c0ba7fa5fb90454cbb9`. All 19 originally bound files were re-hashed and are unchanged. The later complete author-v2 correspondence identity remains `3beae4b1b22966fb1e7bf0c1efa9b8cef3cced4833918b8bd67746bc9b88eaea`, with report `9d0cd5eba5dacdb452874898a552037deb4c4a3c4a91a54287218b82cc13ddb6`. Neither report is relabeled as a review of later source bytes.

That earlier comparison established all 1200 selected-record corrected-I/Q digests, all 1251740 scalar header values including IEEE bit patterns, and all 17882 sixteen-byte spare blocks. Both products have 8941 headers. The fixed 600-second window has 600 records per channel and 600000 aligned sample pairs. The separately frozen 19 synthetic checks covered packing and 725 exact rational cell points. The post-exposure ADC comparison reused the independently decoded arrays and agreed within 2.78e-17 cycles. These are independent implementations on exposed development inputs, not independent empirical tests.

## Source and delta actually read

I read the complete canonical receiver, complete NCO helper, complete primary runner, complete four-input manifest, complete receiver-v2-to-canonical delta, and the note, focusing this disposition on its empirical, import, no-go-scope and review language. The mathematical helper was inspected for imports and file/process access only; its mathematics belongs to the separate focused proof review. The complete frozen source bytes and hashes are recorded in `CANONICAL_SOURCE_CORRESPONDENCE_IDENTITY_v1.json` and copied under `canonical_sources_v1`.

Relative to the already compared author receiver v2, canonical source returns its terminal result, factors the unchanged character and interval formulas into shared functions used by the actual data path, adds three fixtures, and declares the 180-second runner metadata. Packed-word extraction, exact raw/label hash checks, complete headers, the fixed window, flags, deterministic gzip, 1 kSPS lag guard and sample ordering are unchanged. The nonzero check in `character` agrees with the pre-existing actual-data check; it does not introduce an estimator or remove any admitted sample.

For theta in {0, pi/10}, X=exp(5i theta) and K=exp(19i theta) give X^19 conjugate(K)^5=1 pointwise. Their separate nonzero means have arguments pi/4 and -pi/20, hence combined argument 19pi/4+5pi/20=5pi and character -1. The interval fixture is exactly [19(-0.1)-5(0.4), 19(0.2)-5(-0.3)]=[-3.9,5.3]. This checks the negative coefficient's endpoint reversal. These are analytic checks of the newly shared data-path functions, not a repetition of the full raw run.

## NCO arithmetic, domain, and narrow concrete check

Write the stored accumulated phase as A and the cubic as p0+p1 s+p2 s^2+p3 s^3, in cycles, with s in seconds. For consecutive tagged records, the exact join at a common supplied shift sigma is

    d(sigma) = A_new - A_old + P_new(sigma) - P_old(1+sigma).

An independent expansion gives cubic coefficients

    c0 = A_new-A_old + p0_new-p0_old-p1_old-p2_old-p3_old
    c1 = p1_new-p1_old-2p2_old-3p3_old
    c2 = p2_new-p2_old-3p3_old
    c3 = p3_new-p3_old.

The canonical helper's `Fraction.from_float` evaluation is exactly this expression on the archived binary64 values. It is not a claim that physical oscillator phase is exact. The integer-second difference assertion is appropriate for these pinned same-day consecutive headers; it is not a generic cross-day or cross-configuration assembler. The two sigma values are 0 and 1/2000, not fitted values. No per-join integer or real offset is selected.

`NCO_HEADER_SPOTCHECK_v1.py` independently expands these coefficients from the first four rows of each original independent header ledger and uses Horner evaluation, without importing the author's helper or rereading packed raw data. All twelve checks (three joins, two bands, two supplied shifts) match the saved author exact fractions. In particular the first zero-shift X join is 0, while the first Ka join is -357913941/147573952589676412928 cycles. The result identity is `beae131f3ec86634b119e579c34330de688a6bdf420c9702f5750c44218199e3`. This deliberately narrow concrete check did not independently rerun all 17880 adjacent-record joins at both shifts.

The source keeps exact residual-string identity hashes, raw min/max and absolute quantiles. Its additional centered fractional diagnostic does not change those. The note's quoted all-join maxima match the existing author NCO product, which this report inspected but did not regenerate. Both arguments give tiny joins; neither selects physical phase timing. A small continuity residual does not supply complex sign, analog LO/electronics phase or carrier-estimator identification.

## Input/output closure and timing scope

The manifest's four exact raw/label identities match the frozen independent inputs. The later unexamined receiver pair is not a runner input. The default scientific path verifies the four local hashes, runs the mathematics and receiver helpers, then feeds the two newly generated complete header ledgers to the NCO helper. There is no read of an author working result, independent report, raw-header oracle or undeclared observation file in this numerical path.

The primary declares six package input paths (note, three helpers, manifest and frozen protocol), and records its own source as a seventh identity. The mathematical helper has no scientific file read. The receiver reads exactly the two raw files and two labels; the NCO helper reads exactly the two generated header ledgers. Product closure is the eight named output files plus summary.json. The external manifest and intermediate-read statement distinguish those generated reads from raw scientific inputs. Documentation/SIS and other original references support the prose but are not secretly imported by the numerical runner.

The 11 explicit development checks cover both full product counts, the fixed selection and sample count, matching keys, the independently checked complete digest-list identity, finite conditional cells, independent width-summary targets, sky-phase status, both retained shifts, all recorded join counts, and the two author all-join zero-shift identity targets. The latter targets are repeatability controls, not a second independent all-join derivation. Receiver fixture count rises from 7 to 10 after the shared-function controls. The mathematical control count is supplied by the separately reviewed helper and is not re-certified here.

The scientific primary and all three helpers now declare 180 seconds. `--fetch-inputs` is a separate acquisition path, performs no scientific inference, and allows curl up to 240 seconds per input; it is not covered by an assertion that a four-file network fetch must fit a 180-second scientific envelope. No network or download was used in this review. No execution runtime is inferred from the declaration alone.

## Empirical and import wording

The published counts and conditional ADC-width statistics agree with the original independent comparison. Every selected pair contributes; origin-reaching/extreme-code flags remain explicit, and the actual fixed window has none. The ideal unsaturated rectangular analog preimage is an additional premise, not a consequence of two's-complement unpacking or 2k+1 centering. No physical saturation history, analog noise, carrier accuracy, scalar energy or gravity residual is certified.

I read the complete independent instrument phase review, identity `1ba68da8ecf67a6790ad640ae320bd0e9a7940969166d54f7f9c3b55777f2865`. The canonical source-bounded account corresponds to it: the original 2001 specification uses start-of-millisecond phase and midpoint frequency; the day169 label uses a midpoint phase argument too; first-sample tags and designed pipeline compensation are positively specified. The unresolved sign and analog phase statements are limited to those reviewed documents. I did not repeat the other checker's PDF-page review or represent it as my own.

The note keeps operational cross-uplink relation, phase/clock/ray transfer, estimator and physical error/energy bounds, action, initial state, scales and environment open. Its pointwise ADC and separate-average witnesses do not rule out a justified coherent estimator with a narrower admissible waveform family. Earlier milestones are context, not undeclared numerical premises. All inputs remain exposed development; zero physical fits, independent empirical tests or selected timing conventions are claimed.

## Review repair chronology and cache limits

I flagged that the earlier phrase “no fitted offset or wrapping” omitted the separately computed fractional diagnostic. The author changed the note to say the retained join residuals are unwrapped, a separate fractional diagnostic is reported, and neither selects a convention. I read this affected wording at final note hash `5bd3667c7e34646e616c82498401c8c9169604ce471aeefefd3f1b1da65f6616`; it resolves the finding. I also verified the added helper timeout declarations are metadata only. A guarded attempt to write this report against the earlier source hashes stopped at its first assertion before creating any report or source snapshot, because that declared repair had arrived. This was an effective stale-source guard, not a numerical failure; no completed report was replaced.

The preliminary summary inspected here binds older receiver `e5fef4c56f4b0756dfe8cb8c7fae5834547c6c98f91d5b2bb4e97f3842489a5e` and 7 receiver fixtures. It is preserved as `canonical_sources_v1/PRELIMINARY_summary.json` and is historical, not a final cache for current receiver `4eea9fe5454b7ab8896bbada623b668da09d71d694401ecc8862b7b0651a9c00`. The NCO product used for twelve spot checks is also preserved. A final source/product/cache binding remains pending the author's frozen envelope. Mutation coverage, full theorem review, staged delivery, integrated landing and formal audit are outside this focused report. No original reviewer output, author source, index, branch, status or lock was changed.
