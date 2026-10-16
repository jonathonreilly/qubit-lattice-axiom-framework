**Focused independent reconstruction of the exposed June 18 ATDF/ODF counts**

The corrected count scale and the stated conditional forward modulo lift reproduce all 91,664 ODF Doppler rows from independently decoded ATDF endpoints. Every row's endpoint IDs, exact rational increment, residual, comparison scale, negative-control value and group summary agrees with the frozen author's v2 output. This checks stored-data reconstruction, not a physical trajectory, radio calibration, scalar constraint, independent empirical validation or formal audit.

One material metadata omission was found: the original v2 per-row metadata did not include ATDF item 87, “Total Slipped Cycles during Doppler Count.” It is nonzero in 18,393 of the 183,329 used endpoint occurrences. The author was notified and is adding it to the final packaging. Numerical agreement still holds; it must not be promoted to a slip-free phase-history premise. This report binds the frozen source before that metadata addition. A subsequent source confirmation must identify the final changed bytes.

The checked source is `atdf_odf_reconcile_v2.py`, SHA-256 `207985615620bab369ac5cb424753c3e218847067a07b150958f3bdbc0a34f58`. Its complete extraction dependencies are:

| Source | SHA-256 |
| --- | --- |
| `pds_atdf_inventory_v1.py` | `302190b07cc4279ed5e6d62744a5ee938508b91f9353eb0912f339535a74d381` |
| `pds_odf_inventory_v1.py` | `2dfc9339ca5a962ade99df5a3270e95cff3e97501ce32f198ce51681fcb2d9c8` |
| `atdf_odf_reconcile_results_v2.json` | `b097b7c91a9e92cf68f807652028ff542df444943c6a12ee8373b06e83ff00d8` |
| Runtime `ATDF_ODF_ALL_ROWS_v2.jsonl` | `0aa1da97c9cb0bcba4ce3bce3c203d3759843d7bca78890007d0f50ef0e40f19` |

The source and summary snapshots are preserved in `atdf_frozen_v2/`. I read the complete reconstruction source and its extraction helper. The independent calculation imports none of the author's extraction or conversion helpers. It uses the earlier independent PDS object-tree parser, derives locations from the labels, slices explicit MSB bit strings spanning the required bytes, and interprets signed fields by two's complement. The relevant 28 field positions/signedness agree with the published inventory schema, and 113 synthetic field-boundary cases exercise extraction. This is not a general validation of all PDS syntax or other ATDF versions.

Only the registered raw pair and their labels were opened:

| Input | SHA-256 |
| --- | --- |
| `c32easc2002_169_0000xmmmv0.tdf` | `215c2de473fd00b278267ab3ff0431ab4d00e9c3baaa17e949105b964644f4f3` |
| `c32easc2002_169_0000xmmmv0.odf` | `39a658fd74044783b598c947f54dc97dee755c8499a58d7f371831e3f2792e5f` |
| June 18 TDF label | `5c62b58cd56585b8ab2b518ca915e3ec7b8ccdc887de36b07ebabd09d496b5d6` |
| June 18 ODF label | `37beef944cfbab3711ba49b415535e2ca29113c3cd892ffe3f25160b1badf04e` |

The TDF has 160,870 declared tracking records, all format 8, with 159,528 Doppler-type samples indexed. All selected samples in this file are type 1 or 2; mixed/downlink-phase sample types accepted by the code's wider index predicate are not exercised. Calendar reconstruction uses date ordinals plus hours/minutes/seconds, separately from the author's datetime/timedelta implementation. All actual calendar values are valid and the unused fractional-time item 9 is zero. The dates span days 169–170 of 2002. This is nominal calendar matching, not a derivation of station-time, UTC or relativistic clock transformations.

All ODF Doppler compression intervals are exactly one second with a 500-millisecond midpoint component. The independent pairing uses each interval's two integer-second endpoints plus receiving station, downlink band, collection mode and channel. It agrees with every stored candidate-record list. Every Doppler row is represented once, in file order, with no extra ledger row. No residual-based selection or quality-group deletion was used. The 199 range records are outside this Doppler-specific result.

The primary [PDS ATDF unpacking guide](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_TRK-2-25/tdf_unpack.pdf), Table 5 and Appendix B(3), gives the corrected decimal-limb expression. In integer microcycles,

    C = H*10^14 + I*10^7 + L.

The independent implementation concatenates the decimal limbs, with seven digits in each lower limb, rather than using the author's sum of scaled words. Actual lower limbs satisfy the required decimal ranges. The published example (16, 4398198, 1475000) becomes 1,643,981,981.475 cycles, and both high-part and intermediate-part carry boundaries are checked exactly. The original label's H*10^12 microcycle expression is incompatible with that example and the 999 affected intervals. The guide PDF hash is `2a826779dfa96bfe39658711e936eb156e324ce2c1c41cd526c4b93588bcc33a`. The earlier inventory's displayed literal-label phase examples are historical failed-route evidence; v2 imports only its decoding/time helpers and does not reuse those phase values.

ATDF reference frequency is assembled independently in Hertz as H*1000+L/10^6. ODF reference frequency uses the contiguous 46-bit integer, expressed in millihertz, independently assembled as high*16777216+low. The Table 5 reference example also agrees. Each matched interval has equal reference values at its two endpoints. For coherent rows the ATDF and ODF reference values coincide; for one-way rows their differing roles remain explicit. With the fixed candidate convention, the reconstructed value is

    DeltaC/T - 10^6                                      (types 12,13)
    DeltaC/T - 10^6 - (880/221)*ATDF_ref
                       + (11/3)*ODF_spacecraft_ref       (type 11).

The sign/bias/reference arithmetic is consistent with the specified fixed-mode reconstruction and the cited historical definitions. This does not prove every hardware meaning of a frequency-level or uplink-band tag. In particular, no actual transmitted sky-frequency/ramp model is established by agreement between processed and precursor data.

For M=2^32 cycles, endpoint counters identify an increment only modulo M. The independent calculation takes the least nonnegative residue of the difference in integer microcycles. This equals the author's branch formula under its explicit domain: 0 <= true increment < M with no counter reinitialization. There are 21 lower-endpoint transitions requiring one modular wrap under that assumption. For both wrap and nonwrap examples, I constructed alternative histories with increments delta+n*M for n=1,2,7 that produce the same endpoints. Equal endpoints also admit either zero increment or one/more complete turns without a bound. The history bound and absence of reset are therefore surviving assumptions, not deductions from the endpoint observations or from this arithmetic agreement. [Morabito and Asmar's primary account](https://tda.jpl.nasa.gov/progress_report/42-120/120B.pdf) explicitly documents the 2^32-cycle correction, but does not eliminate that logical ambiguity for arbitrary endpoint histories. Its PDF hash is `73d5f703f31903206df81906c9f953f6933d93f6bb5ec54bc1a14d0c5f738ddc`.

All seven groups agree exactly with the published rational summaries:

| ODF type / receive / transmit | Rows | Largest absolute residual, Hz |
| --- | ---: | ---: |
| 11 / 54 / 0 | 649 | 0.000000760550527903469 |
| 12 / 25 / 25 | 36,007 | 0.000000473 |
| 12 / 45 / 45 | 6,094 | 0.000000473 |
| 12 / 54 / 54 | 19,358 | 0.000000469 |
| 13 / 25 / 54 | 9,910 | 0.000000473 |
| 13 / 45 / 25 | 10,160 | 0.000000462 |
| 13 / 54 / 45 | 9,486 | 0.000000469 |

The overall maximum is exactly 100849/132600000000 Hz at ODF record 3916. Every row lies within the stated storage-quantum comparison scale. That scale is not an uncertainty distribution, certified legacy-software error bound or instrument-accuracy claim. All indexed count values in this particular file are multiples of 1000 microcycles; theoretical field capacity and actual displayed numerical granularity should not be mistaken for physical accuracy.

One endpoint has two conversion-equivalent candidates. ODF record 4100 pairs ATDF record 25899 with records 25901 and 25902. The two ending candidates have identical count/reference conversion values but different sample-type/no-process metadata; one has the frozen-counter flag 2. Both are retained. This identifies the stored numerical conversion value, not which candidate is physically valid. The duplicate's slipped-cycle fields are zero, but other endpoints have nonzero fields.

The used endpoint-occurrence distribution of item 87 is: 0:164936; 1:6939; 2:8567; 3:1979; 4:558; 5:178; 6:69; 7:2; 8:7; 10:94. Adjacent intervals reuse endpoints, so these are occurrence counts, not counts of independent slips, unique records or unusable observations. Existing Doppler-validity/no-process fields and these slip indicators must remain distinct. The original v2 retained the former selected metadata and omitted item 87 from its row ledger; its raw data and inventory still preserve the information.

All five published negative-control families were independently recomputed for every row. The wrong literal count scale fails 999 intervals; omitted wrap correction fails 21; wrong 1000-Hz bias and reversed count sign each fail all 91,664; omitting the one-way reference difference fails all 649 one-way intervals. Additional independent countermodels show that the wrong high-part scale still fails 999 intervals even when modulo lifting is retained, the wrong microcycle factor and opposite bias sign each fail all rows, and incorrect reference units, receiver conversion factor or substitution of spacecraft reference for receiver reference each fail all 649 one-way rows. These are deliberate alternative forward formulas, not a claim that a complete source-code mutation suite was run.

The original failed v1 is preserved and verified: 999 mismatches and one ambiguous endpoint, with source hash `5c0f4d0013e87d7dd56453ed479253e79b91dbe6e08ddfda0c54de0d0ae48a04`, summary hash `d67bd7238f9f37ade9e0e05d98b528fef5b789b79269b49a1f44ac0aeb7f4293`, and full ledger hash `a2f283b4685762c30414c84819fa276e28a0a7f896d5fd51d54a10469fd9573c`. No v1 evidence was edited to erase that failed route.

Independent evidence:

| File | SHA-256 | Scope |
| --- | --- | --- |
| `check_atdf_independent_v3.py` | `2ba243c647e58431118a9945c62c3da2e3d60fe14a690cce5bf108ccf14d7522` | Independent label decoding, exact reconstruction and countermodels |
| `ATDF_INDEPENDENT_RESULTS_v3.json` | `0bc4d8b7afbca3603b0ab85f0cce13d9fab2177480b5bac8ea02d2013c19712b` | 2,177,671 successful check events; no failed numerical comparison |
| `ATDF_INDEPENDENT_v2_METADATA_CORRECTION.json` | `4ea51086f5cda051c41551ed7010b1470948261b4d78ad30a4bf372986243b68` | Preserved correction of an initially mistaken independent-report limitation |

The independent checker initially used an incorrect ODF table name and stopped before decoding; its source/stderr are preserved as `ATDF_INITIAL_CHECKER_ROUTE_FAILURE_v2.*`. A later result correctly extracted the nonzero slip distribution but included a premature, false boilerplate sentence asserting zero slips. That result and source remain preserved; the correction receipt records the contradiction, and v3 fixes the sentence without changing the extraction/arithmetic result. Neither local checker failure is a scientific failure of the author's reconstruction.

The event count consists of correlated field/row comparisons, not independent experiments. Source-copy confirmation, added slip metadata and final packaging remain to be bound separately. No primary file, existing report, ownership state, branch, commit, reserved raw product or author source was modified by this check.
