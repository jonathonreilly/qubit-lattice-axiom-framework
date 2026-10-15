# Independent RSR extraction and conditional angle-cell check v1

The independent reader successfully decoded all 8,941 headers in each pinned RSR file and all samples in the frozen UTC window. The selected window contains 600 records and 600,000 complex samples per channel, yielding 600,000 exactly matched X/Ka sample pairs. No record was quality-clipped. The 1,200 per-record corrected-I/Q hashes are frozen in the two WINDOW_RECORDS ledgers before author implementation or numeric-result comparison.

## Independence and exact input scope

I read the two assigned product labels, including all 72 column definitions and their complete mutual difference, and the 2k+1 packing/centering section 1.5.2.1 of the already present casrssis.txt. I read the author's explicit preaccess protocol and raw-source manifest. No root RSR implementation, draft, output, per-record digest or ADC-cell summary was opened before this result freeze. The source and protocol were frozen before the first raw read. Root then announced the protocol/label-level total and window counts; that exposure is recorded in EXECUTION_v1.json. It did not supply sample values, digests or change the prewritten reader.

| Input | Bytes | SHA-256 |
| --- | ---: | --- |
| c32easc2002_169_1335x54x25d.1a1 | 38088660 | 28af13233a64f7629b794cc8beaad0db2500fb09cc421cda3e82544144235a92 |
| c32easc2002_169_1335x54k25d.1b1 | 38088660 | 9544e294be8867cb013b3d96891a413f5dddc3d5e0236e8a2b9331fe7d45a19e |
| rsr_c32easc2002_169_1335x54x25d.lbl | 61946 | 36ab671cbb83c7d04060c2a19058800a4fc50f780aa8fa6e9f77ed3089046382 |
| rsr_c32easc2002_169_1335x54k25d.lbl | 61946 | 2349b0473986f5247650fc88a5bbaf7e859786e22253b38f4a8719af3dd0c697 |
| casrssis.txt | 309479 | daa759b2338fc4ca53d7474d7c17f83a1068470c0c5a00bcc17cf2d17e5ad84b |

The two raw files were read completely for hash/length/framing. Every 260-byte header was decoded and retained, together with its exact raw hex and complete record hash. Only payload samples in year 2002, day 169, 48900 <= t < 49500 were interpreted. The original protocol makes both entire products exposed development. None of the reserved raw files was accessed. This is an independent implementation on exposed inputs, not an independent empirical test.

The implementation uses Python standard-library struct and integer bit masks and does not import root code. Q is the upper halfword; I is the lower halfword; packed samples advance from least to most significant bits. Two's-complement conversion precedes 2k+1 correction. The output order is corrected I then Q, each a big-endian signed 32-bit integer. The primary labels define 4,260-byte records with 4,000 payload bytes. The selected actual headers specify 16-bit components and rate 1 kilosample/second, so each selected record contains 1,000 complex samples. All allowed packing resolutions were independently exercised on synthetic fixtures.

## Full header and selected-sample findings

Each file has consecutive record sequence values 0 through 8,940 and exact one-second header times 48,900 through 57,840 UTC seconds on day 169. There are no duplicate time/grid keys, unmatched header-grid keys, sequence gaps, nonfinite decoded header fields, documented framing-constant mismatches or sample-grid configuration/duration anomalies in the checks implemented. Every raw header is still retained; absence of these particular anomalies is not a general receiver-health certificate.

Both products identify spacecraft 82, SPC 10, downlink DSS 25, three-way tracking with uplink DSS 54 and X uplink. RSR IDs are 1 for X downlink and 2 for K downlink, both subchannel 1. Resolution and rate are constant at 16 bits and 1 kilosample/second. Hardware error counts and predicts override flags are zero in all records; predicts time shifts, frequency overrides/rates/offsets and subchannel offsets are also zero. The distinct front-end gains, attenuation, ADC RMS/peak values, model fields and all other header fields remain in the complete ledgers and inventories. These status values do not prove zero receiver error or phase stability.

The UTC window selects records 0 through 599 and sample indices 0 through 999 from each record. There are no unmatched window records, duplicate alternatives or extreme signed output codes in this window. No selected ideal cell touches the origin. Absence of extreme codes does not establish an unsaturated physical history or validate the supplied quantizer transfer law.

| Result | X channel | Ka channel |
| --- | ---: | ---: |
| Selected complex samples | 600000 | 600000 |
| Corrected I range | -51919 to 53331 | -42017 to 40169 |
| Corrected Q range | -52393 to 57883 | -41487 to 40991 |
| Minimum squared code-center amplitude | 3970 | 775042 |
| Maximum squared code-center amplitude | 3915037178 | 1877186042 |

Exact integer component sums, squares and cross-products are preserved in RESULTS_v1.json. The nominal sample-time grid is the SFDU tag plus j/header_rate. This is a recorded-grid interpretation, not a derivation of an absolute receiver clock, a half-millisecond model-evaluation convention or the sky-phase sign. No NCO or LO phase was restored or convention fitted here.

## Exact conditional cell mathematics

PRECHECK_v1.md supplies the frozen proof. Under the additional unsaturated ideal midrise rectangle premise, a corrected center (a,b) has a cell [a-1,a+1] by [b-1,b+1]. For nonzero (x,y) in the cell, the relative angle is atan2(a*y-b*x,a*x+b*y). Because a and b are nonzero odd integers, the denominator is strictly positive away from the origin. Its exact extreme slopes are the nonzero corner values (a*y-b*x)/(a*x+b*y); the monotonic atan maps them to the exact closed angle enclosure. This is a consequence of a linear-fractional function on a rectangle, not a stochastic noise model.

The origin requires explicit handling. For centers (plus or minus 1, plus or minus 1), the closed rectangle touches zero and analog phase there is undefined. Ignoring that zero point, the other corners yield the correct angle limits; for (1,1), they are [-pi/4,pi/4] relative to the code center. The enclosure must therefore state its nonzero-voltage domain, and atan2(0,0) must not be treated as a physical angle. The actual selected samples do not encounter this corner case, but the general theorem does.

The exact independent oracles include (3,1), whose errors range from -atan(1/3) to atan(1/2), and (101,101), whose errors range from -atan(1/101) to atan(1/101). The 19/-5 character maps two error intervals to [19*lX-5*hK,19*hX-5*lK], with total width 19*wX+5*wK. Projection of an interval of width at least 2*pi fills the circle. The two (101,101) cells give errors plus or minus 24*atan(1/101); two (1,1) cells give [-6*pi,6*pi] before circular projection. A disk enclosure may be conservative, but it is not identical to the rectangle's exact angular range.

Nineteen synthetic controls pass, including all five supported packing resolutions and exact rational checks at 725 nonzero interior/edge fixture points. These checks are separate from the raw file comparison. They neither establish the actual analog transfer law nor supply carrier/thermal, electronics, propagation or gravitational errors.

On the actual selected code centers, the conditional 19/-5 character-cell width has median 0.0005482142770177202 cycles and maximum 0.1341142987521808 cycles. The maximum absolute endpoint-error enclosure has median 0.00027411576072477637 and maximum 0.06729341111793699 cycles. These are floating descriptive evaluations of the supplied ideal cell image; no physical uncertainty interpretation is assigned. All 600,000 pairs contribute, with no clipping, fitted phase, threshold selection or discarded flagged sample. Raw baseband character values are retained only as a circular arithmetic diagnostic and have not been promoted to sky/carrier phase or a scalar residual.

## Frozen execution evidence

The independent raw execution ran once, exited 0 in 4.504255624953657 seconds and produced empty stderr. There was no failed attempt, threshold adjustment or post-access source repair. The complete evidence identities are in FINAL_IDENTITY_v1.json.

| Artifact | SHA-256 |
| --- | --- |
| independent_rsr_reader_v1.py | ee3b0475758f3033dd54c989986419d3a73adf76ad329f1c3d2068e3d52e43b5 |
| PREACCESS_FREEZE_v1.json | 0a296403a2c4f0af01e787346c360d6c2b2d1d34a140f815a5ddfa920bbf290b |
| RESULTS_v1.json | e1a725bdd4ff2987ae1dbaaf6bf8e71e6f0dbe08225c270cb25afb45a96359ef |
| X complete corrected window I/Q array | 2094952c4df7757c397810a01dfd67d83e643fb8be8aff60e219fd3e1a5bce86 |
| Ka complete corrected window I/Q array | e3f08dce9f664f54e80e38d44f03cbb4b34e448c56164212fc801b653794074a |
| X per-record sample/digest ledger | 9f6bcf04a723db1b4805e3ee6b1107db3a59338dd7a273bdba86d50a1e9a0fda |
| Ka per-record sample/digest ledger | fd7cd45765619adfcb6374bc2cc76993e638892f2ef7a04f2752dc17da5a2f58 |

Only the assigned independent_rsr_v1 directory was written. No root scientific source, campaign state, lock, Git index, branch, PR, model setting or external service was changed. Author-source and exact per-record correspondence are the next separate, post-freeze check; this report does not claim that comparison is already complete.
