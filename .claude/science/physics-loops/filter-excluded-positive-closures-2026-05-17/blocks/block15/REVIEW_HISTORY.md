# Block 15 -- Review History

## 2026-05-17 -- Build

**Target row:** `yt_boundary_theorem` (desc=469, criticality=critical, score=16.268)

**Approach:** Identified that the parent has 5 distinct sub-claims, most of
which are interpretive. The unique narrow positive theorem available without
re-arguing interpretation is the **numerical-well-definedness** of the
backward-RGE map used to implement claim (iv). That is the strictly
weaker, fully algorithmic prerequisite that the parent assumes implicitly.

**Discovery during build:** Initial scan interval `[0.5, 1.3]` runs INTO
the Yukawa-Landau-like onset at `X ~ 1.28`, causing Phi to grow from ~1 to
~13 across `[1.27, 1.28]`. This was a real finding: it forces the maximal
well-defined scan interval to `[0.5, 1.2]`. The note and runner were revised
to use the tighter interval and to ADD a fifth check (T5) that empirically
locates the Yukawa-Landau onset and verifies that the scan boundary is the
maximal well-defined range. This also tightens the Lipschitz numerical bound
and exposes the physical band structure cleanly.

**Result:** 23/0 PASS. All five sub-theorems (T1)-(T5) verify on the chosen
scan interval. The unique-root claim is rigorously established via
strict-monotonicity + sign-change + multi-subinterval brentq agreement.

**Files added:**
- `docs/YT_BOUNDARY_BC_TRANSFER_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-17.md`
- `scripts/frontier_yt_boundary_bc_transfer_uniqueness.py`
- `logs/runner-cache/frontier_yt_boundary_bc_transfer_uniqueness.txt`
- `.claude/science/physics-loops/filter-excluded-positive-closures-2026-05-17/blocks/block15/{BLOCK_BRIEF,V1V5_NOTES,REVIEW_HISTORY}.md`

**Files NOT touched (per hard rules):**
- `docs/audit/data/audit_ledger.json` (audit data; forbidden)
- `docs/CANONICAL_HARNESS_INDEX.md` (forbidden)
- `docs/DERIVATION_ATLAS.md` (forbidden)
- `docs/DERIVATION_VALIDATION_MAP.md` (forbidden)
- `docs/YT_BOUNDARY_THEOREM.md` (parent; left unchanged)
- `scripts/frontier_yt_boundary_consistency.py` (parent runner; left unchanged)
- `main` branch (no push, no merge)

**Status:** PR branch `physics-loop/yt-boundary-theorem-block15-2026-05-17`
ready to commit + push + open PR. Honest status:
`positive_theorem (numerical narrow well-definedness)`.
