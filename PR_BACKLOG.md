# PR Backlog — toe-retention-source-action-20260725

## Cycle 700 — admissibility union/subset closure — BACKLOGGED, not opened

Branch: `physics-loop/admissibility-union-subset-closure-20260725` (pushed;
commits `439be29671`, `f3c3b01e7d`, `aedefb8d24`, `de5c9721ce`, plus this).
Runner 6 PASS / 0 FAIL, cold-run in an isolated worktree, receipt pin verified.

**No PR was opened.** This is the fourth block touching the
Record/Admissibility surface this campaign, so the cluster-cap evaluator was
mandatory. It was run as an independent codex `gpt-5.6-sol` xhigh seat with no
write access and returned **`VERDICT: BACKLOG`**. Its reasoning, which is
accepted:

1. The repair is largely self-referential — the rejected duplication argument
   from PR #5620 is not retained, and the salvaged kernel classification does
   not depend on it, so repairing the finding restores no live claim.
2. The core result is the elementary fact that an arbitrary local constraint
   need not be hereditary or compositional. The runner adds fixtures, not
   substantial physics.
3. U4's presentation overreached in calling the separation "exact"; it is
   sufficient, with one boundary witness, not shown necessary.
4. Most importantly, cycle 700 **qualifies cycle 698's M1**, and that caveat
   belongs inside PR #5625 where reviewers can assess the readout argument
   coherently, rather than arriving as a separate PR with its own audit
   sequencing burden.

**Actions taken on the verdict.** Point 3 was a correctness criticism and the
note is corrected: the title, the U4 heading, and the tightness paragraph now
say *sufficient* and explicitly disclaim necessity. The scope section now
distinguishes what the finite window checks from what the proof carries.

**Outstanding action, blocked on review timing.** Point 4 is the right disposal:
the M1 domain caveat should be folded into #5625. That PR was under active
review when this verdict arrived, and pushing to a branch mid-review would
invalidate the reviewer's frozen snapshot and drop the commit at landing. The
caveat is therefore queued for the next fix iteration on #5625, or as a
follow-up if #5625 lands first.

**Exact recovery command if the branch is wanted later:**

```bash
git fetch origin physics-loop/admissibility-union-subset-closure-20260725
git checkout -b c700 origin/physics-loop/admissibility-union-subset-closure-20260725
python3 scripts/physical_admissibility_union_subset_closure_cycle700_2026_07_25.py
```

The one-paragraph caveat to fold into cycle 698's M1, if this branch is never
opened:

> M1 reads the additivity clause as quantifying over every splitting of every
> collection. That presumes the parts and the joins are themselves
> configurations. Admissibility fixes only *that there is* one
> nearest-neighbour rule, not which, and for some legitimate rules a
> sub-collection of an admissible configuration is inadmissible, and a disjoint
> union of two admissible configurations is inadmissible. M1's decomposition
> use is the safe direction, but the clause's domain is rule-dependent and the
> strict reading should be stated with that condition attached.
