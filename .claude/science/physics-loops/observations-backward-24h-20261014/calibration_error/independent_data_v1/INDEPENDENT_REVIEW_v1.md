# Independent day169 quotient reconstruction check v1

This is an independent extraction and exact finite-data format check. Root remains the author. The independent calculation was frozen before opening any new calibration_error author source or results. Old M2/M5 summary totals and comparison scales were already exposed and are declared in PRECHECK_v1.md. No formal audit, physical calibration or independent gravity test is claimed.

## Inputs and implementation

Only the four registered files under outputs/cassini_doppler_inputs were read as measurement inputs. Their original bytes, labels and M2 primary interpretation PDFs/texts are hashed in INPUT_IDENTITY_v1.json. No reserved track or new sample was opened or downloaded. The independent program uses contiguous binary-character slices and exact Fraction arithmetic. It imports no author decoder, reconciliation, quotient or history routine.

The label supplies 160,870 tracking rows, 91,863 ODF orbit rows and bit positions. Primary tdf_unpack Table5 supplies N=(H*10^14+I*10^7+L)/10^6 cycles (its published example is checked exactly); June2000 TRK-2-18 supplies the Doppler channel interpretation of ODF item15 and the combined 46-bit reference word. All tracking record identifiers and relevant format, phase/reference and quality fields are retained in ATDF_EXTRACTED_FIELDS_v1.jsonl; original raw identities preserve every unexpanded quality/status bit as well. ODF_EXTRACTED_FIELDS_v1.jsonl retains every orbit row, including 199 type37 rows outside the Doppler comparison. No quality or residual selection is made among Doppler endpoints. Endpoint matching uses time, receiving station, band, ground mode, channel and spacecraft ID. Every duplicate is retained.

The conditional M2 receiver convention supplies Q=T(D+10^6) cycles for coherent data and Q=T[D+10^6+(880/221)F_A-(11/3)F_O] for one-way data. This convention is reused as an exposed format definition; the present task does not independently rederive physical calibration. All matched endpoint reference values agree at both ends, so retaining both reference alternatives produces no numerical ambiguity.

The computed object is [N_end-N_start-Q] in R/(2^32 Z), and its projection to R/Z. Centering an error coset is only a way to print its distance to zero. No forward count increment is chosen, and no assumed increment range, reset count, cycle-slip history or history lift is implemented or called. The raw signed difference is retained separately for every endpoint variant. Adding any integer multiple of 2^32 to an endpoint leaves the former comparison unchanged; adding an integer cycle leaves the latter unchanged. This information loss is explicit and is not repaired by a small comparison residue.

## Exact complete finite-data result

All 91,664 Doppler intervals match: 61,459 two-way, 29,556 three-way and 649 one-way. There are 91,665 endpoint-pair variants: 91,663 unique pairs and one interval with two end variants. The duplicate is ODF record 4100 with the preserved ATDF 25901/25902 alternative. There are 91,701 distinct matched raw ATDF records and 91,700 logical endpoint keys. All nominal/flagged quality variants remain in the ledger.

Both quotient distances have maximum 100849/132600000000 cycles (approximately 7.60550527903469e-7), at ODF 3916. The coherent-only maximum is 473/1000000000 cycles at ODF 2774. Every exact comparison lies within the predeclared storage-number scale 2e-6+T*1e-9 cycles, with the inherited one-way reference-storage terms added. These are stored-number comparison scales, not hardware accuracy bounds. NARROW_CONSISTENCY_v1.json also checks all 91,665 exact projections from the 2^32 quotient to the one-cycle quotient.

For item19=item24=0 with item87>0:

- 13,015 ODF intervals have nominally good/locked endpoints with at least one such positive item87.
- 9,207 unique raw endpoint records meet that predicate; they also represent9,207 distinct logical endpoint keys.
- Those records occur 18,393 times in the fully retained interval-variant endpoint ledger.

The first count is also 13,015 if phrased as an interval containing any endpoint satisfying the predicate. All endpoint IDs, logical keys and interval IDs are preserved in QUALITY_DIAGNOSTICS_v1.json. The field is diagnostically nonzero despite the nominal quality/lock values. Receiver-specific interpretation, relation to physical slips, and calibrated count-error certification remain open; this calculation supplies neither a physical-error upper bound nor a claim that these data contain 13,015 actual physical slips.

## Consecutive triples in cycle units

Static grouping uses ODF items 6–20, excluding the time, stored observable, count duration and station-delay items, exactly as declared in M5. Reference-frequency parts and the validity bit remain in the static key. Every gap, overlap or duplicate would split a chain. The result is 8 strata and 36 chains, with 28 gaps, no overlap/duplicate intervals and 91,628 adjacent pairs. One chain is a singleton, hence the complete count of equal-duration consecutive triples is 91,593 rather than 91664−2*36. All durations are one nominal second. No unequally spaced triple is silently assigned the equal-spacing formula.

For each triple retain four shared endpoint identities and compute

    -N0+3N1-3N2+N3  versus  Q0-2Q1+Q2 modulo one cycle.

The coefficients act on cycles; these are not mislabeled Hz differences. The four-endpoint Cartesian alternatives yield 91,594 comparisons. The only duplicate triple consists of ODF 4096, 4098, 4100. Maximum exact modular discrepancy is 893/500000000 cycles (1.786e-6), at ODF 37634, 37636, 37638. Every variant lies within e0+2e1+e2 for the individual predeclared storage-number scales. The entire ledger is ALL_THIRD_DIFFERENCES_v1.jsonl, with exact signed phase combination, ODF cycle combination, quotient residue, endpoint identifiers and scale. No polynomial or gravity parameter was fitted.

## Execution and scope

The raw program ran once under /usr/local/bin/python3 and exited 0 in 12.8833 seconds; stderr is empty. It decoded every stated row and performed all interval/triple comparisons using exact rational arithmetic. No failed run, changed threshold or discarded variant occurred. A later narrow ledger consistency pass checked exact quotient projection and chain-count identities without rerunning the raw program. EXECUTION_IDENTITY_v1.json binds the original program and all products; FINAL_IDENTITY_v1.json binds this report and the additional consistency record. Large reviewer ledgers are local output artifacts, not a request to publish raw data or commit them.

The result removes an unnecessary forward-history choice from these quotient comparisons only. It does not establish an unwrapped counter history, station proper-time calibration, stochastic noise model, physical accuracy, or any scalar/gravity observation test. Independent reproduction here means a separate implementation on the same exposed, dependent precursor/product pair.
