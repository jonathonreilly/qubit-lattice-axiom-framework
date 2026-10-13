# Radiation v2: affected-source independent confirmation

## Disposition

**R1 is closed for the exact v2 sources below.** The parent's new off-trajectory force controls compare the actual implementation with canonical proper-time Klein–Gordon accelerations. All 54 supplied states also agree with an independent canonical-N reconstruction in z=S^(1/6). The exact mutation that passed all 1,195 v1 assertions now fails all 54 new coordinate-acceleration comparisons and returns exit code 1. No material mathematical, numerical, or source-continuity issue was found in this affected change.

This is a narrow source/test correction confirmation. It does not reclassify the original two-field construction as an empirical result, a stability theorem, a unique reconstruction, or a certified no-go delivery. It does not perform a formal audit, repository gate, publication gate, or landing action. The original full review and all its failures remain unchanged.

## Read and freeze scope

Read in full: `check_radiation_closure_v2.py`, `off_trajectory_controls_v2.py`, `OFF_TRAJECTORY_FIXTURES_v2.json`, `OFF_TRAJECTORY_REVISION_v2.json`, and the actual v2 freeze/execution/stdout/stderr. The reviewer inspected every added row through independent recomputation and every added assertion through exhaustive accounting. The 27 paths in `INPUT_RECEIPT_v1.json` include all 11 current frozen inputs, five execution/evidence files and all 11 original v2 source snapshots. No new external primary-source claim was introduced; the previous primary reads remain applicable because all 118 original source, primary and reviewer identities were reverified unchanged.

| Current source/evidence | SHA-256 |
| --- | --- |
| Author v2 runner | `c86d2c5442593132b484ab8a7f03288f08b791207686fa4bde4f50b962ca3192` |
| Canonical-force helper | `18ad59a63226defd35d6e37435a69313a878f7f92a4eebe9ac0e2f75cd59fffa` |
| New fixtures | `447b8f7eb338c7d24a56010502b664b8c6cdde07c371d878a9c392ed4ca65476` |
| Revision record | `68ddcda565887d9cfd75997d4b075f3ced991feb7f872e95a1b5deda16ed4236` |
| Actual v2 results | `d502ddde0d506b8b262fc27b681ecb7a2d3c57edb566c344a1cb77c8cd5f7493` |

The first frozen v2 execution records 1,573 passes and zero failures, exit 0, elapsed 99.2534 seconds. Its stderr is empty. This review did not manufacture a fresh positive author execution to replace that history.

## Original source and result continuity

The 12 original non-main functions are identical both as complete source text and as Python ASTs. They are `check`, `close`, `exact`, `symbolic_identities`, `thermal_calibration`, `local_functions`, `potential`, `rhs`, `algebra_grid`, `old_potential_responses`, `exact_background_integrations`, and `endpoint_controls`. The only runner changes are the added helper import, invocation in main and new helper/fixture source hashes. The exact diff is preserved.

The symbolic, thermal, local-grid, old-potential, background-history and endpoint result sections are exactly equal as parsed JSON, including every numerical value, string and record. The original 1,195 assertion objects are an exact prefix of v2's assertions. The original role and environment-version records are also unchanged. New timestamps, source identities, totals and the added off-trajectory section are expected v2 changes. The extended helper is separately frozen; it imports no reviewer program and uses none of the tested runner's local-potential helpers to construct its expected forces.

## Independent transformation check

Let F=(dS/dchi)^2>0 and choose the same branch dS/dchi=-sqrt(F). With x=log S,

  dchi/dx=-r,  r=S/sqrt(F),
  Gamma=d(log r)/dx=1-S F_S/(2F).

For proper-time velocities q=udot and v=chidot, the canonical constraint gives

  H²=[2(sigma_m+sigma_r+V)+q²+v²]/3,
  Hdot=-(sigma_m+4sigma_r/3)-q²-v².

The canonical force equations give

  uddot=-3Hq-V_u-sqrt(a)sigma_m,
  chiddot=-3Hv-V_chi.

Consequently, with w=q/H and p=-v/(rH),

  w_N=uddot/H²-w Hdot/H²,
  p_N=-chiddot/(rH²)-p Hdot/H²-Gamma p².

These are exactly the transformations used by the parent's new helper. The minus sign in V_chi=-sqrt(F)V_S is essential and is present. The Jacobian/connection term in p_N is also present. Selecting proper velocities first and solving the canonical constraint does not impose p=-3. Matter/radiation multipliers are genuinely displaced, so the fixtures are not the exact-background solution in another notation.

For an independent route, the reviewer uses z=S^(1/6), R=bz^8 and

  J=dchi/dz=-2sqrt(a)z²sqrt(1+4bz²/3)/Hbar.

Repeated applications of J^(-1)d/dz produce the canonical potential derivatives and M. At 95 decimal digits, the reviewer computes canonical N accelerations first, then transforms only the output through D=zJ:

  p=6 chi_N/D,
  p_N=6 chi_NN/D-[1+z J_z/J]p²/6.

No parent helper is imported or executed for positive evidence. The independent program reads the frozen result as comparison data only. It reconstructs each fixture's state, canonical H², proper-time accelerations and both N accelerations, rather than trusting expected values already stored by the helper.

## Fixture coverage and numerical results

The 54 states are the complete 3×3×3×2 Cartesian product specified before v2 execution: three a values, three R/S values, three L/S values and two signed field/velocity/density disturbances. The helper constructs b and L once per fixture and holds them fixed when differentiating S. This matters: differentiating with a fixed instantaneous R/S ratio would describe a different potential. The implementation correctly uses R=bS^(4/3).

All fixtures have positive source densities, H² and Friedmann denominator. The minimum independently reconstructed denominator is 2.97363419990. The absolute p_N values range from 0.291911808543 to 2.69794052137, well above the declared minimum-force guard of 1e-4 and the 2e-10 absolute/relative comparison budgets. The seven controls per state check the two accelerations, two kinematics, matter exchange, trace-free radiation conservation and nonzero coordinate acceleration. The assertion name `canonical chi acceleration` refers to the coordinate p_N obtained from the canonical chi equation; its compared quantity is correctly transformed rather than an untransformed proper-time acceleration.

The independent affected-source program has **1,244 passes and zero failures**, including all 378 new stored assertion records. Largest absolute differences from the independent values:

| Compared quantity | Maximum absolute difference |
| --- | --- |
| Actual runner u_NN | 3.406e-17 |
| Actual runner p_N | 5.614e-15 |
| Parent expected u_NN | 8.952e-18 |
| Parent expected p_N | 3.984e-16 |
| H² (across its wide fixture scale) | 1.358e-13 |

These numbers support the corrected executable comparisons. Finite force fixtures do not constitute a perturbative stability proof or universal error certificate. No new observations, fitting, numerical target changes or theory parameters are introduced by this revision.

## Exact repeated mutation

Only in the review-owned copied source, replace the identical v1/v2 expression

  -(3+h)*p-Gamma*p²-V_x/(g H²)

by literal `0.`. All fixtures, helper code, assertions and tolerances remain byte-identical to the frozen v2 inputs. The complete mutated runner was actually executed with exclusive result output.

The run began at 05:04:07.578146 UTC and ended at 05:06:02.107844 UTC on 13 October 2026, taking 114.5298 seconds. It returned **exit 1: 1,519 passes and 54 failures**. The failures are exactly the 54 new `off trajectory canonical chi acceleration` comparisons. All 1,195 original assertions still pass, as expected from the original blind spot; the other 324 added checks pass. The mutant stderr is empty and the complete failed JSON/stdout are preserved. Mutant runner SHA-256: `9977565a839b6342c259a97f04b3b6ce98663321f3dfe69e3b4ed11548096216`.

This is the missing discriminator requested by R1. It rejects the literal-zero implementation through observed mismatches, not through a source-string check or a modified tolerance. The previously surviving v1 mutation remains preserved in the original review; it is not retroactively relabeled as detected.

## Failure history, recipe and exact closure

No unexpected operational or numerical failure occurred in this affected check. The mutation's 54 failures and exit 1 are expected sensitivity evidence. Earlier v1 extraction and overstrict-precision failures remain exactly unchanged and are not rerun or erased here.

Reproduction order: inspect `SOURCE_CONTINUITY_v1.json` and the exact source diff; run `independent_force_check_v1.py` in a fresh review copy with the pinned snapshot; execute the mutation copy with a fresh `--output-json` destination. The positive reviewer script exclusively creates `FORCE_RESULTS_v1.json`; the raw reviewer execution and mutation execution/logs are pinned. Reviewer source SHA-256: `3284abdd6a0addaf97733b3848ca8df5dca5e9259803d6f1e801a4345ecc4c82`.

The final affected receipt binds every checked author input, reviewer source and output, the mutation's complete local source closure, the prior immutable review receipt and all original unchanged identities. It excludes its own bytes to avoid self-reference. R1 is closed only for the listed v2 source identities; the original v1 finding remains historically valid. The original conditional scientific scope and all stated interpretation limits remain unchanged.
