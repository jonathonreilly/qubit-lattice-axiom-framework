# Review History

## Prior matching branch evidence

Commit `ff703369b0` records two clean review iterations for the same source
delta. That evidence is prior art, not a current-branch self-certification;
the current branch must still pass the applicable review lenses and checks.

## Current branch

### Iteration 1

- Code/runner: `RISK`. Connectedness, regularity, and degree do not uniquely
  identify the 2D `4x4` torus, so a rewired helper graph could survive the
  structural certificate if its low spectrum happened to agree.
- Physics claim: `OPEN`, with a closed exact finite diagnostic boundary.
- Proof obligations: `CLOSED` for the scoped finite target; operational
  preparation is strictly stronger and excluded.
- Imports/support: `DISCLOSED`; no observed, fitted, literature, or approved-
  primitive input is load-bearing.
- Nature retention: `OPEN`; cooling/control/readout, noise, and operational
  preparation-time scaling remain open.
- No-go discipline and labeling-convention reviews: not applicable.
- Repo governance and audit compatibility: `PASS` subject to fixing the
  topology certificate and rerunning final validation.

Fix: independently reconstruct the claimed periodic adjacency from `dim` and
`side`, compare it to the helper graph, use it in the `H1=-A` residual, and add
a relabeling mutation falsifier. The refreshed cache is pinned to runner SHA
`ef05b9ffc8dfbbf8a7c9dfb1c216b2839584bcfe53c5d9b44bb5764493df1995`.

### Iteration 2

- Code/runner: `PASS`; default certificate, high-gap failure path, exact-gap
  boundary, independent Fourier/pair-spectrum calculation, topology mutation,
  and cache freshness all pass.
- Physics claim boundary: `OPEN`; no operational-preparation claim is made.
- Proof obligations: `CLOSED` for the finite open-gate target.
- Imports/support: `CLEAN` for that target.
- Nature retention: `OPEN` by the explicit operational boundary.
- No-go discipline: not applicable; delocalization is not presented as an
  impossibility theorem.
- Labeling convention: not applicable.
- Repo governance: `PASS`; native vocabulary and `Type: open_gate` are present.
- Audit compatibility: `PASS`; the final pipeline run completed with zero
  strict-lint errors, re-ingested the target as `open_gate`, and placed the
  source-drift row in the independent audit queue. All generated authority
  outputs were removed afterward.

Final current-branch review-loop disposition: `pass`.

<!-- Historical review record from the matching unmerged branch follows. -->

## Iteration 1

- Code/runner: `RISK`. The analytic chain passed independent Fourier and
  adjacency checks, but custom gap-threshold exit semantics and tiny
  note/cache roundoff rows needed repair.
- Physics claim: `PASS` as an exact finite boundary inside an open gate. The
  prose needed to separate native delocalization from operational difficulty.
- Imports/support: `DISCLOSED`; fixed controls, helper constructors, tensor
  basis, and factorization convention needed finer classification.
- Nature retention: `BOUNDED-OPEN`.
- Repo governance/audit compatibility: `FIX` for source type metadata and
  closeout details.
- No-go discipline: not applicable.

All findings were fixed narrowly: the runner now fails custom thresholds
consistently, uses a tolerance at the exact analytic boundary, avoids no-go or
operational-preparability language, refreshes its cache, and the note/import
ledger make every finite convention and operational exclusion explicit.

## Iteration 2

- Code/runner: `PASS`.
- Physics claim boundary: `PASS`, exact finite boundary on `open_gate`.
- Imports/support: `CLEAN`.
- Nature retention: `BOUNDED-OPEN PASS`.
- Repo governance: `PASS`.
- Audit compatibility: `PASS`; pipeline and strict lint completed with no
  errors, and generated audit authority outputs were removed from the branch.
- No-go discipline: not applicable.

Final review-loop disposition: `pass`. Independent audit remains required.
