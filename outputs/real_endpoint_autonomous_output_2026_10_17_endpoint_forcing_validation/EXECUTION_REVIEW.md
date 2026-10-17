# Endpoint-forcing execution receipt review

The observed bounded execution supports the stated arithmetic corroboration: the canonical run exited 0 with 547 arithmetic rows, comprising exactly 490 inherited rows and 57 new EF rows. All eight mutations passed declared-input integrity, then exited 1 at the intended first scalar failure. I found no discrepancy between the receipt streams, mutation source changes, source pins, summary, or the final publication paragraph. This is an execution-evidence check continuing the same reviewer's analytical and integration work, not another independent derivation or retained audit.

## Sources and method

N=`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`; W is its sibling `correlation_worktree`; R=N/endpoint_forcing_validation.

I read `R/run_validation.py` completely, the canonical wrapper, relevant `runner_cache.py` execution/cache functions, all nine PRELAUNCH/RESULT receipts, the complete parsed canonical result, all 57 EF row records, and all eight actual failure records with surrounding integrity status. Deterministic receipt parsing compared counts/names and verified hashes; it did not import or run any scientific program. I also diffed every stored mutated runner against the pinned canonical runner. No scientific rerun, solver, W/Git edit, model change or prompt edit was performed. Only this report was written.

| Evidence/source | SHA256 |
|---|---|
| Canonical scientific runner | `d93be99a2a49abed5c3a8edc6740af7c50fa6d8ba6a7f9d156cb73319d4e78cb` |
| runner_cache.py | `1f534bb856d68140359e7204b08577c204195ff6077e7d7f6c4974e92f0afaf2` |
| Declared ARTIFACT_MANIFEST.json | `d9ef08360edf5a5c4f1eddff7f400f05dedda4cee711553d276cb5b60d8bdf72` |
| Prior integration review | `0b2b08a11f8d8fe5720b3be92360a405dddda36ff3ba3274bc0f8952e4a0f1e2` |
| R/run_validation.py | `1513a0a620174a20a5897e611fd9a1671237ed827460d2e37c8b2b84030a428d` |
| R/CANONICAL_RESULT.json | `ecf74173014da676eac3a3fa408f9f4d09f6fba1f46ecfd74a1481deaef4471e` |
| R/MUTATION_SUMMARY.json | `e50833219ad3f2d8f3627aa3d2c0c979785ef09242705db0092ab891ccf226a4` |
| R/canonical/PRELAUNCH.json | `2d1edc049eab56c3a12fb5d397e7f06e101e34996010a7d2d0549ae0556fbb8b` |

The canonical prelaunch contains 112 source/interpreter records; each mutation prelaunch contains 108. Every recorded byte count/hash and every RESULT output hash matched the currently present corresponding file when checked. These comparisons include the canonical runner, helper, wrapper, launch script, integration report, declared inputs and interpreter, and all eight mutated runners with their copied declared inputs. The runner and manifest identities are the ones reviewed before execution. The executable is Python 3.13.5 at the recorded Homebrew path.

The launch code rejects a runner different from the reviewed SHA, writes/fsyncs PRELAUNCH before each launch, and refuses an existing launch receipt. Its canonical path calls `execute_and_write_cache`, which calls the scientific runner once and checks pre/post execution identities before writing the cache; it is not a cache-read shortcut. Eight scratch-source mutations follow. This supports the single-launch description in this packet; it is not a claim about all historical invocations elsewhere.

## Actual canonical result

The inner canonical result reports status `ok`, exit 0, elapsed 0.08256006240844727 seconds and inner wall allowance 30 seconds. Its outer wrapper receipt reports exit 0 and 0.3605699590407312 seconds. The complete runner stream is 144635 UTF-8 bytes. Its serialized `checks` array has 547 distinct names; the 547 `PASS arithmetic:` lines match those names in exactly the same order, without missing or duplicate rows. Exactly 57 start with `EF `, leaving 490 inherited rows. Integrity success and the final scoped `TOTAL PASS` line are separate from that arithmetic count.

I inspected every new EF record, including its exact rational lhs/relation/rhs. Representative load-bearing observations are:

- Endpoint deletion forcing is 57047/5000<12, with the 44-power closed-source row present before it.
- Actual endpoint-shift domain, Woodbury denominator/multiplier, separate P/Y bounds and additive X correction all appear. They do not replace X with Y in the background term.
- Disk oscillation is 36000001/124000000<.291; the energy-loss row is 4960000000000/999998000001<4.961. The complementary and full inverse rows, separate cutoff margin and update norm are present.
- The complete bottom and side source rows retain X+update*Y. Localized exponent is exactly 60; its bottom and both sides are charged. The side envelope is exactly 341/12500000000=2.728e-8, and the localized total is 10344323/378787500000000<2.733e-8.
- Scalar phase uses 7499999999999887=vT-113. Separate outgoing/incoming heights, shifted scalar cutoff, exponential lower witness, both tails and their squared normalization costs appear.
- Complete nominal/fixed-nominal infinite and finite sums include unchanged static cost and fixed-spectrum profile comparison. M is 15000000000000000000. The finite exponent comparison is 12960000000000000009<15000000000000000023 and its prefactor is 19683/20971520<.001. Ratios remain 100/3 and 40000/3.

The separate new summary fields state T=3e17, M=1.5e19 and the claimed nominal/fixed-nominal ceilings; historical onset fields remain unchanged. The stream labels its limited scalar scope and reports no large matching matrices or dynamics. Re-executing the 490 inherited arithmetic checks is not 490 new scientific findings.

The cache helper merges the scientific subprocess's stderr into its stdout stream. Its returned empty `stderr` field therefore must not be described as an independently observed empty scientific stderr stream. The outer wrapper stderr file is genuinely zero bytes; no error/traceback appeared in the captured merged scientific stream. Each mutation captures stdout and stderr separately, with zero-byte stderr observed.

## All eight actual first failures

Each mutation used `python -O`, returned exit 1, had exactly one `TOTAL FAIL:` line and a preceding `PASS integrity:` line. The underlying check helpers raise rather than relying on removable Python assertions. The actual first failure names agree with the launch script and mutation summary:

| Mutation | Stored source change | Actual first failure |
|---|---|---|
| closed_powers | ef_closed exponent 44→20 | `EF endpoint closed amplitude 44 powers` |
| projected_forcing | projected .2→69 | `EF deleted-source forcing bound` |
| whole_core_forcing | bottom emitter-update Y→X | `EF complete bottom column with endpoint forcing` |
| excess_strip | h=8e-15→8e-14 | `EF background disk oscillation` |
| endpoint_shift | shift envelope 1e-20→1e-8 | `EF background multiplier` |
| short_time | T=3e17→3e15 | `EF complete bottom exponent` |
| side_budget | localized side coefficient 44→88 | `EF both localized cutoff side ceiling` |
| finite_length | M/T=50→40, with matching size identity 1.5e19→1.2e19 | `EF finite transfer exponent margin` |

The actual failed comparisons, in that order, are:

1. `108198406747431/2621440000000000000000000 < 1/1000000000000000000000000`.
2. `2903899/1000 < 12`.
3. `49894000000863247011396/2849 < 2200000000000`.
4. `36000001/11500000 < 291/1000`.
5. `25000000/24999991 < 1000000000000000001/1000000000000000000`.
6. `3/5 = 60`.
7. `341/6250000000 = 341/12500000000`.
8. `12960000000000000009 < 12000000000000000023`.

Stored source diffs confirm these are the only changes, except for the explicitly documented finite-length companion identity update. That companion permits the test to reach the physical transfer-margin check rather than stopping at a bookkeeping equality. The other seven mutations change one expression each. The observed first failures must not be relabeled as later resonance, cutoff or final-error failures that execution never reached. In particular, excess strip stops at disk oscillation and the shift-envelope mutation at the multiplier. These are valid discriminators for the named scalar-envelope families; they do not prove the matrix identities.

All mutation wall times were below .253 seconds. Their full streams and RESULT output hashes remain in the corresponding `mutation_*` directories.

## Caps and evidence boundary

The launcher applies RLIMIT_CPU=10 seconds and RLIMIT_FSIZE=16777216 bytes. Canonical outer/inner wall limits are 45/30 seconds; mutation wall limits are 10 seconds. No memory cap was applied. CPU limits are per process, not a demonstrated aggregate tree CPU budget. No timeout or cap termination occurred in these receipts.

These eight tests are new mathematical mutations, not new integrity-rejection tests. The current run exercised successful declared-input integrity; historical malformed-input/inert-import tests were not rerun here. No full combined-main pipeline or retained audit ran. Scalar success does not certify source normalization, noncommuting kernel order, background identity, local synthesis, complete contour proof, full-device dynamics or native suppliers; those remain the separately exposed analytical/premise obligations. N6 remains outside the canonical positive refinement.

## Final publication delta

I read the final source/verification paragraph of W/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md and its changed introductory wording. Its final observed SHA256 is `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`.

Reversing only the execution paragraph to its frozen draft text and `This appendix` to `This draft` reproduces the previously reviewed whole-note hash `2ec466a624705dbd707c0c855df2d1dd93068df11e6f28b633eb8e4d3462a7cb`. Thus the new note delta is exactly the reported wording/status update, with no unreviewed mathematical changes. Its count, exit-status, mutation and scope statements agree with the observed evidence and avoid an empty-scientific-stderr claim.

All 41 files present in W/outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation matched their N receipt counterparts byte-for-byte, including the renamed launch script and copied integration review. The evidence copy is outside declared scientific inputs; frozen draft artifacts remain historical source material. This copy review verifies the files actually present, not unclaimed additional source snapshots.

The execution paragraph is supported as written. This report completes the requested selective execution check, without granting retained status, merging, or extending the physical or perturbation domain. No editable prompt file changed.
