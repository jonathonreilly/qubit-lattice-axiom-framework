# Referee report: J:derive:uniqueness-region-up:a1

**Author:** w-macbookpro90c72-jcc2b (grok-4.6).
**Referee:** w-jonathonsmac4f50-j7b64 (claude-opus-5).
**Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `706afaa5`, and its log.

**Provenance.** The criterion comes from attempt a2 (worker w-jonathonsmac4f50-j1ba5). That worker is this referee's
model family, and a2 was refereed as a partial by a grok worker. a1 re-implements the criterion and adds one grid point.
This referee's `check.py` recomputes a1's numbers with a2's functions. It is therefore a recomputation, not an independent
method. The author's re-implementation is the cross-family check of a2's machinery, and it agrees with a2 at `p = 51/10`
on all 30 pairs.

## The claim

The averaged Wasserstein criterion of a2 (ground metric `ρ = 1` orthogonal and `α = 5/4` antipodal, averaged over the 216
achievable laws) gives `3κ̄ < 1` at `p = 511/100`. So a2's uniqueness and exponential-forgetting argument applies at
`p = 5.11`. The attempt also reports:
- `3κ̄ > 1` at `p = 512/100, …, 52/10` for every tested `α`;
- a same-copy two-level diagnostic, marked as not used for uniqueness.

## Step by step

**Step 1 (a2's criterion, re-checked): holds.** U1 gives `3κ̄ = 52187574259076840991934694/52321061656792031643757593` at
`p = 51/10` over all 30 ordered pairs, the author's fraction, with feasible transport plans.

**Step 2 (the new grid point): holds.**
- At `p = 511/100` and `α = 5/4`, over all 30 ordered pairs with no symmetry used,
  `3κ̄ = 641339158597871240931289476511219280500203/641457015620770188990330181460632729109801 = 0.99981627 < 1` (U2).
- The transport plans are feasible.
- `3κ̄ = 1.00218138` at `512/100` and `1.02101204` at `52/10`, both above 1 (U3).

**Step 3 (other `α`): holds** where re-checked. At `α = 4/3` the values are `0.99827159` (`p = 51/10`) and `1.00064630`
(`p = 511/100`). At `α = 3/2` they are `0.99991740` and `1.00230637`. All match the author's (U4).

**Step 4 (same-copy joints): not re-checked.** It is marked as not used for uniqueness, and the attempt says correctly why
it does not control the mixed-copy recursion.

**Step 5 (consequences): holds.** a2's step-7 argument depends on `p` only through `3κ̄ < 1`, so it applies at `p = 5.11`.

## Classic failure modes

None found. The statement is exactly the grid point certified, and the failure at `512/100` is reported as a no-go for
this criterion only.

## Verdict

The partial result survives with no failing step in steps 1–3 and 5.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
