**Final canonical source confirmation — Cassini count and station-time block**

The final canonical sources preserve the checked reconstruction and mathematical scope. The added item-87 metadata agrees with the raw ATDF bytes at every used endpoint occurrence, and stripping only that added field reproduces the complete previously checked row ledger byte for byte. The packaged runner also reproduces the author's output bytes in an isolated run using the pinned development inputs. The identified slip-metadata omission and receiver-reference wording issue are resolved within this scope.

This is a focused source/math confirmation, not a formal audit, landing review, retained-status decision or empirical gravity conclusion. It extends the unchanged `REVIEW_ATDF_RECONCILIATION_v2.md` (SHA-256 `ca8c5812fae86c035ea3490bf7348e35488670dd3d7cab3a8fba9fbf00e6d1e8`) and the earlier ramp and finite-count reports in this directory. Those reports, their failures and their original identities remain intact.

The complete final constituent bound here is:

| Canonical file | SHA-256 |
| --- | --- |
| `docs/CASSINI_DOPPLER_COUNT_STATION_TIME_BOUNDED_THEOREM_NOTE_2026-10-14.md` | `7665d29d78d2ce302c445bb3f8878e50cb75d89d20bbd14cdb0c4f8d673a0bde` |
| `scripts/cassini_doppler_count_bridge_check.py` | `a82b64943f216202aa1cb5db899a36c92a96d75136f728d19e3a6d78a71d279b` |
| `scripts/cassini_doppler_development_inputs.json` | `7e383c50247c91d0086e8c308e11613bb386b0f93cf282e2e4128f5a320b0392` |
| `scripts/cassini_odf_decode.py` | `2dfc9339ca5a962ade99df5a3270e95cff3e97501ce32f198ce51681fcb2d9c8` |
| `scripts/cassini_atdf_decode.py` | `2ac6212a6ef7da1a95baa8f0b0a9fad99b74bed4de0a7e819d7d6b930b53196c` |
| `scripts/cassini_ramp_phase.py` | `f6f20d30a557e03359ca1b28fc466805700122ca280819338da733eee80ca296` |
| `scripts/cassini_finite_count_endpoint_check.py` | `8d6c1ef43ff738cc85c8fcb0406a30d19afd1ef0be4c5c7c8b32786d28840003` |
| `scripts/cassini_atdf_odf_reconcile.py` | `adbeaf5c78b9eedf0b3d94b1d27efca84fc2ad03002686a8114c912e1f8cd225` |
| Campaign `RAW_DATA_PROTOCOL_v1.json` | `1360e8812eb5500d654c30be2320eb852102d182b16957fad270265a11673c5a` |
| Campaign `RAW_DATA_PROTOCOL_v2_ATDF.json` | `cfc407bb7ad15ff94166a78ff6520ab6ce1c1cf1477f2184489b9171610c3030` |

I read the canonical note, wrapper, source manifest and both exposure protocols in full. The final note's last change qualifies F_A as the stored reference with the S-band normalization used by this conversion; the level flag alone is explicitly not a physical-frequency calibration. Other edits in that final change are prose spacing. All displayed mathematical formulas are unchanged from the earlier complete note read, which now explicitly requires a unique, temporally ordered retarded map.

The helper-source mapping was checked by exact whole-file transformations. ODF decoding is byte-identical to the earlier checked decoder. ATDF decoding changes only its docstring and displayed phase-example scale from the preserved erroneous label scale to the primary-guide correction. The ramp and endpoint helpers change only module/file names. The canonical reconciler changes only import names relative to the final working reconciler, SHA-256 `fde68aa68a82a5afdad8b2d633a820d80b787b7d81439224903d8ffa05ee4afb`. That final working source differs from the independently checked frozen source only by requesting item 87, appending it to retained mode/quality metadata and clarifying its scope text. There is no additional arithmetic, data-selection or residual-filter change.

For the metadata check I independently read item 87 from its label-defined position, zero-based bit 1466 with width 10. All 183,329 used endpoint occurrences match their final ledger values. The final ledger hash is `6973b8b57b7ecb9fc4f3ea87efbfa1e15dfe4e12349f3ad6aadd054790597f77`. Removing only that added value from each endpoint's metadata yields SHA-256 `0aa1da97c9cb0bcba4ce3bce3c203d3759843d7bca78890007d0f50ef0e40f19`, exactly the earlier independently verified ledger. All 91,664 rows, endpoint candidate IDs, count increments, residuals, countermodels and comparison scales are therefore unchanged. The arithmetic group summaries and outcomes also match the earlier source.

The nonzero diagnostic appears in 18,393 endpoint occurrences, covering 9,207 distinct ATDF endpoint records and 13,015 intervals with at least one nonzero endpoint diagnostic. These are different counting units and are not independent slip events or a classification of unusable observations. The final note correctly leaves the receiver-specific interpretation and physical phase-history correction unresolved. The duplicate candidate at ODF record 4100 still preserves both variants and their differing no-process/sample-type fields.

I executed the unmodified canonical wrapper in `atdf_canonical_final_v1/` with a populated, hash-verified input cache linked only to the authorized June 18 raw pair and labels. All writes stayed in that isolated directory. It exited 0 with 11 aggregate checks satisfied, 526 endpoint controls, 16 ramp controls and 10 count controls. Every output JSON is byte-identical to the author's canonical output, as is the full row ledger. The summary hash is `10284751421344010b1f2e080f6f5c8289b15eefbeb8c67a0fda2b8fecbf01c5`; the canonical reconciliation summary hash is `52300ef640fc9b3d643c8fce268c2b40318c1c1c6726e4c2de1c7d9734f8dbab`.

The final note changed after the isolated execution, but the wrapper and executable sources did not. I checked the final note's changes and exact hash separately; the wrapper does not execute the note. This is not a claim that a cache envelope binding the final note has already been regenerated. The cold-cache HTTPS download path was read but not independently exercised here. The populated-cache path verifies lengths/hashes, and the manifest contains only the authorized raw pair and labels. The separately listed primary-document hashes and registered exposure roles are consistent with the checked sources.

I inspected the author's mutation receipts and confirmed their original source hashes against the final executable files. `DOPPLER_MUTATIONS_v1.json` preserves 18 assertion rejections and one range-guard rejection. In v2, the altered bit field remains within range and is rejected by a value assertion; all 19 recorded variants then produce assertion failures. V2 receipt SHA-256 is `237ea385531891a0efb293278478b41bf17b15bd9de2501984e50e52c01ad012`. I did not rerun that author suite or treat its receipt as an additional independent experiment. The separate independent countermodels and raw-row reconstruction remain the direct evidence for my check.

The final note keeps the essential distinctions: known instrument definitions versus derived phase identities; a proved unique modulo representative inside a supplied history interval versus a derived physical history bound; dependent precursor/product agreement versus independent validation; and stored-number comparison scales versus instrumental uncertainty. The endpoint inequality requires Lipschitz coverage, and the explicit jump counterexample prevents silently extending it across discontinuities. No action, potential, initial state, scalar scale or calibrated gravity parameter follows from this block.

Reproduction/identity additions:

| File | SHA-256 |
| --- | --- |
| `check_atdf_final_metadata_v1.py` | `1b3e8ce18a8464b65fe256b9fd474bb1adf35b17a3240eb44afb57c93a7a37e1` |
| `ATDF_FINAL_METADATA_RESULTS_v1.json` | `7961898d59db4f3ef7482772f1c09e7c1d69341eef8b26942c5d4c9934cc80a7` |
| `check_atdf_canonical_binding_v1.py` | `46fb4828ec091e7962ce2fe48448f65e79c5a90733c2e2c5ff9c872501069ebb` |
| `ATDF_CANONICAL_BINDING_v1.json` | `00819d708d5fd8922aef17b843f5d9b9e6348c1f8d417dda52eb061529564f57` |

All earlier limitations and preserved failed routes remain applicable. No further material issue was found within this scoped source confirmation. No canonical source, prior report, ownership state, branch, commit, reserved product or science status was changed by the independent checker.
