# Source-exposed delta check

Date: 2026-11-09. Scope: only the two corrections identified in the frozen `SOURCE_CHECK.md`, plus exact patch recovery and unchanged-file verification. This is a research check, not an audit or formal landing review. No full repeat review or numerical work was performed.

## Source identities

All source paths below are relative to `/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/carrier_interface/`.

| File | Verified SHA256 |
|---|---|
| Final `RESULT.md` | `f980d1e29c0b6c4d5fe64becd7fa3a7abcf0f7e5ed7fafb517f439fc63eb0ff3` |
| Unchanged `ASSUMPTIONS.md` | `9e06e542c393f386680c3f28d3929265c83aa74d1ee1507cea176b93ec173bc5` |
| Archived `outputs/result_before_source_fixes.md` | `ad12e660846dc8d1ccfa679f9842a7a37a8af1935293dd81cbafa6ac8a65901e` |
| `outputs/source_fixes.patch` | `33aa97692bce9e76e4af767848cceaf41a848a27bbc2f45343f029b5ee14fcbb` |

The patch was read completely. The changed passages and their immediate context were read from final `RESULT.md` lines 174–194 and 281–295. Earlier complete review is reused only for the byte-identical remainder.

## Both findings are resolved

**F1, POVM trace bound:** The final line is `K<=sum_(a=0)^(K-1) tr(E_a)<=d`. The `K` selected POVM effects sum to at most the identity even when additional outcome labels remain. Each selected effect has trace at least one by the unchanged positive-density argument, so the corrected inequality proves `d>=K`. It covers the previously recorded unused-outcome counterexample. The conditional conclusion and comparison assumptions are unchanged.

**F2, target-relative pattern equality:** The definition now explicitly requires equality to the complete target-specific pattern and forbids only records beyond that pattern. The fine pattern is exactly the six detector seeds; the coarse pattern is exactly those seeds plus the prescribed fine record. Thus the coarse predecessor is permitted at `R1`, while the extra coarse record at the occupied fine center in `R2` still selects fallback. Occupancy remains a separate formation-rate mask. This removes the conflicting stage-independent reading without adding a premise or changing the intended two-birth law.

## Exact recovery evidence

Deterministic standard-library text/hash operations established that the supplied patch equals the complete canonical zero-context unified diff between the archived and final byte strings. It contains exactly two hunks; there are no other `RESULT.md` changes.

In an automatically removed temporary directory, a copy of the archived source was named `RESULT.md`. All four commands completed successfully:

```text
git apply --unidiff-zero --check <absolute source_fixes.patch path>
git apply --unidiff-zero <absolute source_fixes.patch path>
git apply --unidiff-zero --reverse --check <absolute source_fixes.patch path>
git apply --unidiff-zero --reverse <absolute source_fixes.patch path>
```

After forward application, an exact byte comparison matched final `RESULT.md`, with SHA256 `f980d1e29c0b6c4d5fe64becd7fa3a7abcf0f7e5ed7fafb517f439fc63eb0ff3`. After reversal, an exact byte comparison recovered the archived reviewed source, with SHA256 `ad12e660846dc8d1ccfa679f9842a7a37a8af1935293dd81cbafa6ac8a65901e`. Only the disposable copy was patched; the source files were not modified by this check.

The original checker artifacts were rehashed and remain unchanged:

- `INDEPENDENT.md`: `9ae83aa0dcc5b9fd4cf926526f2201ce0b72a56c1533eb0e341f3122ae8fb7a5`.
- `CHECKPOINT.md`: `e1af91795b530263420b4483a43875f6d25d0dbac80359cb3efaa61d3752f54f`.
- `SOURCE_CHECK.md`: `b52b979ded08be19d471773c97d1fdffa7fa1cc2d902220693e8d9e49030153b`.

Result: both bounded findings are closed at the final source hash. The original complete source check, together with this exact two-hunk delta check, covers the corrected source. This is a source-exposed verification with the same independence and execution limits already recorded; it grants no audit status. `DELTA_CHECK.md` is the only new durable artifact from this task.
