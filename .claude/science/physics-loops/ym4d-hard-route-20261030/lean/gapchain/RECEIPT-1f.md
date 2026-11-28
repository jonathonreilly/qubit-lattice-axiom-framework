# Stage 1f: the join of rows 1508 and 1509

## Outcome

**BUILT, FINISH row 1525.** The lead (Claude Opus 5.5) wrote `GapChain/Assembly.lean` and built it on the Mac mini with Lean 4.33.1 and Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`. This finite-volume research receipt grants no audit status.

For every β > 0, with no other hypothesis:

- `torusData β hβ : TorusData`. Row 1508's `Trace.cyclic_eq_tsum` discharges the trace hypothesis of row 1509's `Periodic.torusData_of_trace`. The two `cyclic` definitions have the same body and agree by `rfl` (`cyclic_agree`).
- `torusData_spectrum`. On a valid box the spectrum is the witness chosen from row 1506's `transfer_boxSpectrum`.
- `torusData_weight`. On a valid box, for every time period a ≥ 3, the weight is the SU(2) Wilson partition function `Z β a R`.
- `wilson_theoremS`. Theorem S for this data: a seed below 1/5041 on one cube gives the thermal bound and a gap on every dyadic cube.

This is the decisive outcome that [Stage 1e](RECEIPT-1e.md) named for the join. The physical seed `(torusData β hβ).seed N < 1 / 5041` remains open.

## Kernel verification

1. **Full replay (08:20–08:25 UTC, 2026-11-25).** A fresh project held byte-identical copies of the lane sources at lane commit `57a053fa1`. `lake build GapChain Check` built the eight GapChain modules and four consumers: check 1503's consumer and the replays of Stages 1b, 1c and 1e. It used `nice -n 10` and `LEAN_NUM_THREADS=2`, and started at 50% free memory. Exit 0, 3644 jobs, 309 s wall, peak RSS 2,672,492,544 bytes. 212 axiom reports, all `[propext, Classical.choice, Quot.sound]`. Zero `sorryAx`, zero errors.
2. **Assembly rebuild (12:12 UTC).** The lead then added `torusData_weight` and rebuilt `GapChain`. Exit 0, 3639 jobs, 13 s wall, peak RSS 3,356,852,224 bytes. Five axiom reports, all standard.

The source scan of every GapChain module found zero `sorry`, `admit`, `native_decide`, axiom declarations or `implemented_by`. The committed `Assembly.lean` is byte-identical to the built file.

## Verbatim axiom reports (rebuild)

```text
'GapChain.Wilson.Assembly.cyclic_agree' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Assembly.torusData' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Assembly.torusData_spectrum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Assembly.torusData_weight' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Assembly.wilson_theoremS' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Next row

Prove a physical Wilson seed bound: for a coupling in the intended regime and some N ≥ 3, `(torusData β hβ).seed N < 1 / 5041`.
