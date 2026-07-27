# Review History — poisson-self-bound-source (cycle 713)

## Local review pass (2026-07-27)

Codex `gpt-5.6-sol` xhigh review seats produced no usable verdict across three
attempts in the preceding cycles of this campaign; the active tool policy
forbids spawning a separate review agent. Per the skill's own conditional —
"otherwise the loop agent applies the same evaluator brief locally" — the pass
below was run locally against the deliverable note and the runner output.

### Findings raised and resolved

| # | Finding | Resolution |
|---|---|---|
| L1 | The first draft scored self-binding on the **extent alone**. That is the criterion the landed `FROZEN_STARS_RIGOROUS_NOTE.md` uses, and under it biharmonic passes — the g=10 biharmonic extent is flat at 2.70-2.91 across every box. | Added the well-depth condition as the load-bearing half, and made row R5 state explicitly that a width-only criterion calls the biharmonic state self-bound. |
| L2 | The depth divergence could have been an artifact of the Dirichlet wall, or of the nonlinear fixed point. | Added rows R6 and R7: prescribed source with no self-consistency, on Dirichlet and on a boundary-free torus out to `N = 96`. The growth survives both. |
| L3 | The far-field row originally fitted a decay exponent on the self-consistent field. On Dirichlet that fit is wall-biased — `beta` read `2.286` at `N=24` and only fell to `1.362` by `N=48`, still short of 1. Fitting a power law and calling the residual a finite-size effect would have repeated the parent note's own error. | Replaced with the matched point-source kernel ratio (row R10). Both sides carry the same wall and the same image, so no correction is applied and no exponent is fitted — and it is the comparison the parent ledger row asks for by name. |
| L4 | The torus version of the **self-consistent** solve converged to the uniform state: a constant `rho` is exactly the zero mode, so the removed-zero-mode field solve returns `phi = 0` and `V = 0` is an exact fixed point. Reported `rms = N/2` and `depth = 0`. | Route abandoned rather than patched with a symmetry-breaking seed, whose choice would have been an unstated condition. The torus is used only where it needs no seed — the prescribed-source kernel row R7. Recorded here rather than dropped silently. |
| L5 | `local` was initially scored alongside the others. Its converged branch jumps from `rms = 0.0245` to `5.9968` between `N = 20` and `N = 24` at `g = 100`, from the same zero start. | Demoted to row R8 as a bistability finding. `local` is excluded from the comparison rather than scored in it. |
| L6 | The `g = 100` biharmonic runs do not converge at `N >= 20` (`change` above tolerance at the 300-iteration cap). Scoring a divergence claim on non-converged iterates would be unsound. | The scored row R5 uses `g = 10`, where every box converges. The `g = 100` behaviour is mentioned in the gates document's N1 route table as a second, weaker witness. |
| L7 | Row R11's predicted deviation ratio was written as `(rms/5)^2 / (rms/9)^2`, in which `rms` cancels — it is `(9/5)^2` however the source is sized, so the row read as a test of the measured extent when it is not. | Rewritten; see L8, which replaced the row entirely. |
| L8 | With the algebra fixed, R11 still failed on its substance: the measured falloff across the window was `1.49` against the `3.24` a quadrupole correction predicts, so "the residual is the finite size of the source" was **not** supported by its own number. Rather than widen the tolerance band until it passed, the cause was tested directly. The interior width `M` is even for even `N`, which puts the box centre — and so a centred state's centroid — exactly **between** sites in all three axes, leaving the comparison point source offset by `sqrt(3)/2 = 0.8660`. | Confirmed decisively. At odd `M` the centroid falls on a site and the median ratio moves `1.01389 -> 1.00013` (`N = 24` vs `25`) and `1.01228 -> 1.00008` (`N = 32` vs `33`), with the scatter falling from `1.3e-01` to `1.1e-03`. The entire residual was the placement of the comparison point, not physics. R10 was re-scored on odd widths, where it is two orders of magnitude tighter, and R11 became the controlled parity contrast that establishes the attribution. |

### Disposition

`pass`, with the demotion required by the no-go discipline gate's N7 steelman
applied: the biharmonic result is recorded as a bounded theorem under a named
isolation condition, not as an unconditional no-go. See
`docs/CYCLE713_VALUE_NO_GO_AND_CLUSTER_CAP_GATES_2026-07-27.md` Part 2.

### Inference audit (step 11)

`scripts/inference_audit_lint.py` from the unmerged branch
`methodology/inference-audit-20260726` (PR #5652), run against both the runner
and the note. Result recorded in `HANDOFF.md`.
