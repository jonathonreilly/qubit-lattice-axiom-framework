# Post-exposure author replay and actual source substitutions

This diagnostic plan is written after inspecting the author scientific code
and raw results, and after freezing the independent evidence receipt. It is
not a second prospective test of the theorem. All source and author evidence
will remain unchanged. Reviewer copies redirect only the result-file basename.

Replay the frozen author program once. Require all 35 check rows and all
scientific detail values to equal the original saved result; ignore runtime,
program basename and timing metadata. Preserve any disagreement.

Then run these actual one-at-a-time substitutions of executable expressions:

| Copy | Substitution | Expected diagnostic |
| --- | --- | --- |
| dual_sign | quaternion vector difference becomes sum | Haar/translated-cycle checks fail |
| unconstrained_saddle | remove P0 from saddle update | determinant-one / constructed SU saddle check fails |
| missing_haar | replace Vandermonde/6 by 1 | SU3 remainder checks fail |
| double_hessian | divide full-colour Hessian by 3 instead of 6 | eight-colour Hessian check fails |
| wrong_divisor | multiply actual returned means by 4 | fixed matrix-domain check fails |
| inverse_of_mean | replace mean(path inverse) by inverse(mean path) | inverse-mean distinction check fails |
| double_cubic | divide standalone cubic by 9 instead of 18 | likely survivor: parity and nonzeroness do not test its magnitude |

A surviving mutation remains a recorded coverage limit. In particular the
last anticipated blind spot is covered independently by the written cubic
expansion and the pre-exposure SU3 scalar-constraint derivative diagnostic;
it will not be reported as detected by the author checker. The independent
script's zero-lambda and wrong-dimension controls were algebraic wrong-model
witnesses, not byte-mutated author executions. The present copies provide
the executable-substitution evidence. No tolerance or acceptance comparison
will be changed after these runs.

Every numerical child uses the unchanged review launcher: memory>=50%,
load<20, active lock, threads1, nice10, 60-second wall and 55-second CPU cap,
RSS watchdog at1,900,000KiB below2GiB. Run sequentially. Preserve every gate,
raw output, failure, survivor and result; do not overwrite author outputs.
