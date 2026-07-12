# Review History

## Iteration 1

The code and physics reviewers found a blocking selector defect: drifted
coordinates were rounded to locate mass sites, so several rows silently used
fewer than 54 trials and averaged unequal per-seed panels. The repair replaced
that selector with stable grid-label mass sites and regenerated every affected
table row.

The governance reviewer also required explicit snapped/jitter rules, layer and
mass labels, source amplitude, cutoffs, and all-panel normalization checks.
Those disclosures and checks were added.

## Iteration 2

- Code / runner: PASS. An independent transfer-matrix implementation
  reproduced all displayed rows with 54 trials each.
- Physics claim: BOUNDED / PASS.
- Imports / support: DISCLOSED / PASS.
- Nature retention: BOUNDED / PASS; no physical Gate B claim.
- Labeling convention: PASS.
- No-go discipline: not applicable.
- Repo governance and audit compatibility: PASS.
- SHA-pinned cache: fresh, exit 0, `PASS=12 FAIL=0`.
