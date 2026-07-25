# PR Backlog — toe-retention-source-action-20260725

## Cycle 701 — normalization residual map — BACKLOGGED TWICE, target stopped

Branch: `physics-loop/normalization-axis-map-20260725` (pushed). Runner
7 PASS / 0 FAIL, cold-run isolated, pin verified. **No PR opened, and no third
revision attempted.**

The cluster-cap evaluator ran twice, as an independent codex `gpt-5.6-sol`
xhigh seat with no write access, and returned `BACKLOG` both times. Both
verdicts found real errors, not stylistic objections.

### Round 1 — the independence claim

Draft 1 claimed the residuals are provably independent because their
transcribed defining equations use disjoint symbols. Correctly rejected as
**true by construction**: separately transcribed equations trivially use
different symbols, which cannot rule out a semantic identification. The product
check also omitted `kappa_EW` entirely while the note presented it as a fourth
parameter, so it could not support its own conclusion. Withdrawn.

### Round 2 — the corpus claim, and a factual error

Draft 2 replaced the theorem with a commit-pinned negative corpus search: "no
landed note links these". That is **false for one pair**, and the evaluator
caught it. `C2_WEIGHTING_NORMAL_FORM_ONE_PARAMETER_UNIQUENESS_BOUNDED_NOTE_2026-07-02.md`
records, verbatim:

> "Conditional correspondence only: if the `kappa_EW` wall is restricted to this
> two-cell rational content-determined C2 class, then the missing
> 'weighting/readout-bridge rule' is exactly the missing choice of the single
> parameter `w` or a rule that fixes it."

That is a landed conditional link between `kappa_EW` and `w`. Draft 2 would
have erased it. The search was also inadequate as evidence: two of its three
commands were displayed with literal ellipses rather than reproducibly, and
three searches cannot support an all-pairs conclusion over five parameters.

**The two-`w` conflation also survived into draft 2.** The note distinguished
`w_readout` from `w_formation` in prose and then wrote "Both satisfy
`kappa = 2w/(1-w)`". The C2 source supplies only the readout normal form
`I_w = x_A + w·x_B`; the `kappa` bijection belongs to the **formation** weight
under the Koide note's named conditional identifications. The runner repeated
the error in its A1 label and by naming the C2 expression `koide_form`.
Distinct symbols do not repair an incorrect semantic attribution.

### Disposition

Target stopped. Two rounds, two sets of real errors, and a falsified headline
is sufficient evidence that this cross-lane mapping needs slower per-source
reading than this session gave it. Per the skill's value-gate exhaustion
condition, a thin or wrong artifact is worse than none.

**What is worth keeping is recorded in the handoff, not here as a claim:** the
corrected relationships between the residuals, including the C2 conditional
correspondence that draft 2 got wrong.

### Recovery

```bash
git fetch origin physics-loop/normalization-axis-map-20260725
git checkout -b c701 origin/physics-loop/normalization-axis-map-20260725
```

Anyone resuming should start from the corrected picture in the handoff, fix the
`w_readout` / `w_formation` attribution at the source level first, and treat
the C2 conditional correspondence as a link to report rather than a gap.

## Cycle 700 — admissibility union/subset closure — BACKLOGGED

Branch: `physics-loop/admissibility-union-subset-closure-20260725` (pushed).
Runner 6 PASS / 0 FAIL, cold-run isolated, pin verified. No PR opened.

Evaluator verdict `BACKLOG`: the repair is self-referential because the
rejected duplication argument from #5620 is not retained and the salvaged
kernel classification does not depend on it; the core result is the elementary
fact that an arbitrary local constraint need not be hereditary or
compositional; and the useful part — a domain caveat on cycle 698's M1 —
belonged inside #5625 rather than in a separate PR.

Its correctness criticism was applied: the separation condition is
**sufficient**, not exact, and the note no longer implies necessity.

#5625 has since landed, so the M1 caveat is now a follow-up against landed
work rather than a fix-iteration item. The paragraph to fold in:

> M1 reads the additivity clause as quantifying over every splitting of every
> collection. That presumes the parts and the joins are themselves
> configurations. Admissibility fixes only *that there is* one
> nearest-neighbour rule, not which, and for some legitimate rules a
> sub-collection of an admissible configuration is inadmissible, and a disjoint
> union of two admissible configurations is inadmissible. M1's decomposition
> use is the safe direction, but the clause's domain is rule-dependent.
