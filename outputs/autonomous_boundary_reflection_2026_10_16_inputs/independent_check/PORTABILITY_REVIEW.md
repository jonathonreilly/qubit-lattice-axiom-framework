# Bounded portability review

2026-10-16. Static, source-exposed delta check only; neither candidate module
was imported or executed. The previously selected model/reasoning setting
was preserved. No new mathematical derivation or independent discovery is
claimed.

**No mathematical-path alteration, historical-evidence mismatch, or blocking
canonical assertion/scope issue was found.** The intended adaptations match
the actual changes. Execution of the canonical entry point remains pending
this review.

## Exact sources

Canonical files are under
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/scripts/`.
I read both complete files, compared de-indented function bodies against the
original checker bodies, inspected their imports and scopes, and compared the
primary against its archived author diagnostic.

| File | Bytes | SHA256 |
|---|---:|---|
| `autonomous_boundary_reflection_check_2026_10_16.py` | 20250 | `adb3a01d477d244e9d271a37b982d0bb0eb61d0daed701eaabfc6046befb6c94` |
| `autonomous_boundary_reflection_2026_10_16.py` | 8595 | `facd29fd1932b1099a8731baf468affb7ee629f88b430bf64e0134345bc852eb` |
| Original `check.py` | 13230 | `ac306fbb5c40944f605bc11c3b032f5012e42e3c083b76c80b0367099b330117` |
| Original `check_addendum.py` | 5758 | `4d89eb4a831b40b3d468c93d34e9f63366c6b5e41cf718d6d34cd4262b9a6cf1` |

## Delta and provenance

After removing the new function indentation, the reflection body differs
only in wall-envelope metadata, the three added assertions at helper lines
276–278, and replacing its original-directory JSON write with `return RESULTS`.
The readiness body differs only in the resource-envelope metadata and
replacing its original-directory write with `return results`. Moving imports
to the module prefix, removing the standalone ROOT paths and per-script
resource-limit calls, and wrapping local variables do not change the
calculation paths. The primary imposes the shared 120 CPU-second limit.

The primary directly invokes both functions, once each, at lines 164–165
and retains their returned reports. Its separate sparse-joint calculation
body is unchanged from the preserved author diagnostic. The other primary
changes are thread configuration, imports, declared inputs/timeout, portable
output paths and combined reporting. It does not substitute archived outputs
for either calculation.

All 15 files in the packaged `independent_check/` directory are byte-identical
to their originals, including scripts, complete outputs, receipts and review.
All 27 entries of `ARTIFACT_MANIFEST.json` match their actual byte counts and
SHA256 values. Packaged V1, V2, the V2 change note and readiness addendum also
match this reviewer's frozen copies. Original absolute paths in historical
receipts remain historical provenance, as the manifest explicitly states.

New helper `completion.script_sha256` fields correctly identify the combined
portable helper, so both functions will report the same new helper hash.
They must not be described as the old individual checker hashes; the original
execution receipts preserve those identities unchanged. The primary's input
hashes separately include the current helper and frozen V2/addendum.

## Assertion scope and remaining verification limit

The three new gates enforce already observed finite-fixture discriminators:
nominal J=1, w=4/3, sigma=0.15, T=80, 768 clock sites and the three listed
late-time samples. The original results are about 0.07275–0.07298 for the
correct full-joint error, about 1.6 without the global phase and at least
1.232 without old aging. Thus `<0.12` and `>1` have substantial margins.
These are regression thresholds selected with the historical results known;
they do not certify every admitted fault, arbitrary time, infinite volume or
the sufficient epsilon schedule. The source and combined status retain those
limits and the source-exposed qualification.

The CPU cap is actually installed by the primary. `AUDIT_TIMEOUT_SEC=120`
and the helper's “primary runner envelope” text declare the intended external
wall envelope; this static review did not exercise its external enforcement,
dependency availability, elapsed time or the new assertions. Existing
historical execution success is not a canonical execution receipt. No change
is requested before that execution on the inspected source hashes.

Only this PORTABILITY_REVIEW.md was written. The canonical worktree,
original scripts, original reviews and execution evidence were not edited.
