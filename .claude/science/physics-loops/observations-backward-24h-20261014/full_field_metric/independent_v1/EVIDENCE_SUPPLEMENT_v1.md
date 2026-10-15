# M20 narrow saved-evidence confirmation

This supplement binds the reviewed canonical sources to the saved execution, cache, paired products and eight mutation runs. It preserves the original independent proof, canonical source review and all earlier versions. No author scientific calculation, ODE, aggregate or mutation was rerun. This is not a formal audit or an empirical validation.

I read the complete `GUARDED_EXECUTION_v1.json`, `MUTATIONS_v1.json`, `HANDOFF.md`, initial `EXECUTION_v1.json`, current cache and both output JSON files. I read all eight raw stdout/stderr streams and wrappers. Every complete mutant source was compared byte-for-byte with the reviewed helper after exactly its one declared replacement; this checks the entire source, not only a matching token or truncated diff. All source, receipt, product and raw mutation file hashes are retained in `EVIDENCE_BINDING_RESULTS_v1.json`.

## Source and execution binding

The four canonical source/protocol files remain identical to the complete-source review. The primary and ordered five-input fingerprint were independently recomputed, including the two inherited premise notes. They match the before/after receipt, cache header and output identities. The recorded before and after dictionaries agree in both content and complete filesystem-stat tokens. This is verification of the recorded guard evidence; I did not independently observe or rerun its historical process.

- Primary: `f859afe954b42f75a7a97ef3e51af4ef1761992fbaba0bf5310d518b70078180`.
- Helper: `63ac20cfe19f3e0e681ace4714434f58fef50c82fe5ad95a282d0a9e79268a21`.
- Note: `493130222fb63c5fef6d21f14ab254288b0fe81b1d0e5e767cf28d98e77d516a`.
- Protocol: `5254a684a8cba9a3ec0787723a9be4663f2e6b04dccfdf70d9e296c4a055d3d4`.
- Input fingerprint: `996e3febacdc7b856e3afb89ef3e08ba1a304e76613897884ca72062800370e6`.
- Cache: `02138252abadb3a66d10f532ed829231aeb51a061e6cc4f384701a8f27642995`.

The guarded receipt records start `2026-10-15T21:16:34.175712+00:00` and completion `2026-10-15T21:16:34.700896+00:00`. Its elapsed execution is `0.5140860080718994` seconds within 120 seconds, with status ok, exit zero, empty stderr and fresh cache. The cache rounds elapsed time to 0.51 seconds as expected. Its stdout exactly matches the receipt up to terminal-newline normalization; the embedded summary equals the paired summary, whose shared fields equal the detailed results.

There are 31 uniquely named passing controls and zero failures: two twelve-control local solution-jet cases plus seven domain refusals. The cases exactly match the protocol. Each saved six-equation residual is below the fixed `1e-35` threshold, and both saved reconstructed envelopes are strictly interior with positive T and Delta. The source-generated case values are saved evidence of the author execution, not an independently repeated ODE result.

The initial `EXECUTION_v1.json` is retained. Its stdout/stderr/source hashes also match these unchanged scientific outputs, but `HANDOFF.md` explicitly discloses that its `started_at` was captured after the run and represents completion. I do not use that field as a measured start. The later guarded receipt supplies separately labeled start and completion evidence; the earlier mistake is neither erased nor treated as a scientific timing result.

## Actual mutant failure evidence

All eight mutated candidates match their declared source SHA-256 and differ from the reviewed helper by exactly the recorded replacement. The wrappers call the candidate controls with the same declared protocol path. Every raw stderr is empty and every wrapper exits zero, while its JSON explicitly records false controls. Thus the rejection is established by saved failed mathematical controls, not an import/setup exception or merely a nonzero process exit. For each variant, passed plus failed equals 31; numeric failed errors exceed the unchanged tolerance.

| Deliberate source error | False controls in raw output |
|---|---:|
| missing B in transverse kinetic | 7 |
| wrong transverse source sign | 6 |
| half radial scalar operator | 6 |
| reversed y share | 2 |
| wrong y potential power | 2 |
| wrong angular null chart | 12 |
| omit base potential derivative | 6 |
| wrong Einstein conformal kinetic | 16 |

The missing-B mutation fails reconstructed transverse energy and squares; reversed y share and wrong y power fail the y-square checks; the wrong conformal kinetic coefficient additionally fails original Jordan metric/scalar equations. All eight have actual false controls. There is no reported exception-only detection or survivor. This establishes sensitivity to these eight specific altered formulas only, not exhaustive defect detection.

## Disposition

No source/cache/product/mutation discrepancy remains in this scoped confirmation. The author aggregate is 31/0; it is distinct from the unchanged 34 independent pre-exposure exact controls and 50 post-exposure correspondence checks. No new physical assumption has been retired by this evidence binding. Graph/PR delivery, current-main integration and formal audit remain outside the scope.

Reproduce only these mechanical comparisons with `evidence_binding_v1.py`; it reads existing artifacts and writes its own receipt, without executing the author science. Frozen evidence copies and all detailed identities are in this reviewer directory.
