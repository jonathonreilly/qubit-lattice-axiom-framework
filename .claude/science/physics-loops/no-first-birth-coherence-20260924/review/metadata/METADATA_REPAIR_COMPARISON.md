# Metadata repair and fresh-cache comparison

No material discrepancy was found. Both note changes are confined to the
visible Type/Status metadata, both runners are unchanged, and both complete
fresh execution records correspond exactly to the updated source-bound
caches and output files. Scientific values are unchanged apart from measured
execution times.

This is the requested mechanical follow-up against the two prior publication
comparisons. It is not a new blind scientific review, primary reproduction,
audit verdict or retained-status decision.

## Exact metadata delta

The no-first-birth comparison base and observed HEAD were
`918fbe18619667017c56c29677f9f02363368d89`. The mixed-preparation comparison
base and observed HEAD were `cfac353eedae504627196bf9e48009f1b4177f94`.
Their committed note, runner, result and cache identities match the prior
scientific comparison anchors.

For each note, the complete new bytes equal the committed bytes after one
exact replacement of the opening status line. The replacement adds
`**Type:** bounded_theorem` and `**Status:** proposed_retained`, then restores
the former conditional statement as an ordinary paragraph beginning with
capitalized “Conditional.” The existing YAML `claim_type: bounded_theorem`
agrees. The explicit “not a retained audit verdict” wording and every other
conditional/model caveat remain unchanged. No mathematical statement, proof,
coefficient, assumption, evidence description or limitation changed.

The complete diffs are retained as `SEVENTH_METADATA_ONLY_DIFF.txt` and
`EIGHTH_METADATA_ONLY_DIFF.txt`. The visible proposed status does not turn
the unchanged conditional result into an applied retained audit verdict.

## Declared inputs and completed executions

Both runners are byte-identical to their committed versions. The ordered
declared-input sets are unchanged: five notes for no-first-birth and six for
mixed preparation. In each set only the corresponding opening metadata
changed; every other input is byte-identical to its committed version. The
actual length-prefixed fingerprints recompute as follows:

| Publication | Fresh declared-input SHA256 | Recorded primary seconds |
| --- | --- | --- |
| No first birth | `f3deeef2f0cd8e59b466fc3915e959f7397dba42bcdde390446538b8f7e7b219` | 75.59323716163635 |
| Mixed preparation | `d095f445456eb9e704659751bed5fd5ecc64c4803c89a874dca2403d4c25662d` | 0.41100001335144043 |

The fingerprints match the new headers and differ from the old fingerprints.
All four file hashes in each metadata freeze match the actual publication
files. Both execution records report status ok and exit 0. Reconstructing the
entire canonical cache from each full execution record, actual runner hash
and recomputed input fingerprint reproduces all 20,893 and 64,168 bytes,
respectively. This checks the bodies as well as the headers; it does not
restamp or otherwise modify either cache.

The no-first-birth stream contains exactly three progress JSON objects,
the final result object and `TOTAL: PASS=3 FAIL=0`. Each progress object
equals its corresponding final-result row. The mixed-preparation stream
contains exactly its final result object and `TOTAL: PASS=2 FAIL=0`.
In both cases the final JSON text plus newline is byte-identical to the
published result. Both complete streams fit below the cache clipping limit.
The API merges process stderr into stdout; the separate stderr fields are
empty, and the merged streams contain no diagnostic text outside those
objects and summary lines.

A complete recursive comparison with the committed results finds only four
timing differences for no-first-birth (three rows and overall runtime) and
one overall timing difference for mixed preparation. All remaining values,
including the runner source hash, are exactly equal. The changed measured
timings and complete fresh API records are preserved; no prospective runtime
success is assumed. The initial long display of the execution files was
truncated by the tool; the subsequent full-file JSON parsing, recursive
comparison and exact cache reconstruction cover every byte and value.

## Evidence and limits

The exact external evidence identities are:

| External file | SHA256 |
| --- | --- |
| `SEVENTH_METADATA_REPAIR_FROZEN.json` | `aeb0fca4191f52c26eafdd78183e0dd8c88448ebbd869996688ec7bbb9c8507e` |
| `SEVENTH_METADATA_CACHE_EXECUTION.json` | `da1ded3660f687f0b65ee818deed9766d33e06fcfb4e8448dadf540048304aa9` |
| `EIGHTH_METADATA_REPAIR_FROZEN.json` | `d4ba3cdfd0059567ae90529e1e27ac1d4d3c8d9f783f1cd6597d77584433abb5` |
| `EIGHTH_METADATA_CACHE_EXECUTION.json` | `2d84b7daf2ced88e2df6a06fc5e26715715937540e10562227000b0c1c4df5bc` |

`METADATA_REPAIR_SOURCE_PINS.json` records all absolute source/evidence paths,
current hashes and committed baseline hashes. `METADATA_REPAIR_EVIDENCE.json`
records both fingerprints, full-output correspondence and the exact five
runtime differences. The bookkeeping script and full stdout/stderr logs are
included in the separate seal. Its final execution exits 0; it never imports
or executes either physics runner.

The continuous-coherence publication seal
`5d2676e7ead04a5e67d709d2ef2d6a9dbcbfb83468fac6acb6bb5c9083d1a318`
and all 19 members are unchanged. The mixed-preparation publication seal
`1cd9b2465460ea2be9a8e488895eac9c9e09125b8669ec0df6b563cc94985147`
and all five members are unchanged. These reports serve only as comparison
anchors; their scientific checks are not relabeled as new work here.

No primary was rerun by this checker. No frontier argument, unrelated active
packet or rebuilding citation manifest was reviewed. All new files are
confined to `publication-metadata-independent`; previous seals, publication
sources and audit state were not edited. No repair is requested within this
metadata and evidence-correspondence scope.
