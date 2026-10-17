# Positive precision arithmetic draft — unexecuted

`ARITHMETIC_BLOCK.py.txt` is intended immediately after the current LC block, before `check_arithmetic` returns. It uses existing Fraction alias F, explicit-raising lt helper, J/E0 and lc_* variables. New names are pr_*. Historical values are not overwritten. No imports, execution, compile, numerical integration or mutation tests were performed. There is no observed PASS count. Root owns integration, bounded prelaunch/resource plan, source refresh and execution. This is drafting by the positive-contract reviewer after review, not another independent check.

## Exact source identities

Sources under /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934:

- endpoint_precision_publication/SECTION.md: fde5d563e86cf660e16f71fe1f0bf8f3aebd7f2201ffb42b4708e469e5f52d77.
- endpoint_static_precision/PROPOSAL.md: 233364359dc3e79b54debf331eb75e6454f093cdbec36c36e1ba4fe17acc1381.
- endpoint_static_precision_check/REVIEW.md: 40f7649071bc0eeb192a7832c64510c4185d39d31b6c27e9064a77fd5fa6a5f5.

W=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree:

- scripts/real_endpoint_autonomous_output_2026_10_17.py: 93cc122aa253fc2a6fc26748826561bdf61343227e36a9f1df02f4f248e5b991.
- docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md: bc75051b87d62e65ea7953f11c2fcd320f1a9ab853c7a346f32e9314859cb1a5.

The positive proposal/review and publication section were fully read or authored immediately before drafting; the current LC implementation was reread fully. No negative reference illustration or fixed-spectrum construction is represented by these checks. Source hashes identify drafting inputs, not an executed integrated runner.

## Checks and external premises

| New row group | Arithmetic actually corroborated | Analytical premise remaining outside execution |
|---|---|---|
| positive coupling, occupations, absolute detuning | Extremal positive coefficients for r in [.99999,1], signed detuning envelope | Exact correlated installation preserves endpoint2J and c_new. Independent coefficient errors are excluded; no endpoint sampling proves a continuum contract |
| ratio, fixed phase profile | eta and its positive denominator, epsilon and twice-epsilon | Exact COMPLEX ratio rD0/Da; pointwise sine floor; positive normalization costs exactly abs(1-norm(g)); no phase optimization |
| shifted interval/mass | d-|Delta|, mass smallness and denominators, worst-case log argument, actual/reference residuals | Shifted centered interval is contained in original band; exact finite-interval density lemma, full global normalized measure and local synthesis. No exterior spectrum is discarded |
| relative detuning/moment | Delta/alpha_a, changed3.500026 coefficient, restricted band moment and delta | x is relative to nominal E0; actual denominator includes detuning; measure is dk with existing Fourier normalization; full complex ratio still holds |
| real/disk/strip complementary, resonant margin | All changed denominators and full Schur rank correction | Seven complementary directions remain; background disks unchanged; operator Cauchy and exact complex self-energy, not real derivative extrapolation |
| source, complete C, localized | Endpoint worst envelopes, C_b/C_s, bottom and both-side sums | Actual source-specific Schur solve, algebraic open-wave subtraction, vector holomorphy/closed tails, overlap factors and both cutoff sides |
| scalar cutoff/height/tails | Detuning subtraction in cutoff, smallest outgoing height, phase113, fourth-power exponential tails | Dbar's exp(-y) sign and scalar outgoing pole-free strip; geometric lattice sum; scalar strips are distinct from C strip |
| complete actual/fixed nominal | All static/dynamic contributions, positive normalization twice where prescribed, nominal tail, perturbed radius and finite sum | Fixed nominal target, full outputs and arbitrary references; preparation versus outgoing aggregation; finite distance/window and transfer proof reused from LC |

Uniform interval coverage relies on the reviewed monotone envelopes, not numerical sampling. kappa_hi bounds positive numerators and kappa_lo bounds inverse powers; mixed endpoints deliberately overestimate. The logarithm uses d rather than d_a in its numerator, kappa_hi there and kappa_lo in its denominator. Its H bound uses pi<10/3, while mass estimates use pi>3. These elementary bounds and e>8/3, exp(100)>10^30, exp(-a)<=24/a^4 are analytical inputs already explained in the source/LC map.

The code keeps actual residual mass and reference mass separate, and uses the existing LC nominal target-tail ceiling in the final fixed-target sum. The new radius check is the only changed premise of the reused finite-transfer substitution. Same T=4e21, M=2e23 and finite [T,2T] interval are inherited. No seed-epsilon test is added: unitary invariance of an isometry-norm error is a proof fact, not useful scalar PASS content.

All decimals use F strings; every division involving non-integer arithmetic has a Fraction operand. There are no float scientific literals or bare asserts. Explicit positive denominator checks precede corresponding inverses. Rows evaluate extremal expressions, rather than merely repeating the advertised final ceilings as inequalities between constants. Nevertheless scalar inequalities cannot validate their symbolic derivations.

## Suggested decisive mutations, not executed

Each should be a single isolated change to an integrated candidate with exact source diff, stdout/stderr and intended failure recorded. Rejection earlier than the suggested row must be interpreted, not relabeled.

1. Enlarge pr_rel from1e-5 to1e-3: ratio perturbation ceiling or finite complex ratio error should reject the enlarged contract. This tests perturbation range sensitivity, not arbitrary correlated-control errors.
2. Enlarge pr_det to1e-3: absolute detuning or ratio perturbation rows should fail. Removing detuning from a denominator makes an upper bound spuriously smaller and is NOT reliably detected by these rows; source review remains essential.
3. Change pr_da to lc_d/2: shifted interval lower margin fails. Separately raise the mass regularity coefficient10^6 to10^8: shifted actual missing mass should fail. These test lost interval budget and unjustified regularity.
4. Increase the nominal lower-coupling loss by setting pr_klo=pr_rlo*lc_kap/100 in the candidate: relative detuning/moment or logarithm rows should fail. This catches unsupported extension toward zero coupling, not a proof of an optimal lower range.
5. Replace the disk complementary gap .18 by .16 in that expression: disk complementary inverse should fail (<6 is then false), after positivity still holds. This specifically probes the complementary gap margin without allowing a negative inverse to masquerade as small.
6. Inflate lc_h to1e-17 in an isolated integrated copy: a preceding LC bridge/Neumann check or PR resonant/strip checks should reject it. Record the actual first failure; this is a shared prerequisite mutation.
7. Increase the localized two-side coefficient44 to88 in pr_side: complete localized error should fail. Deleting an edge or an overlap factor only reduces an upper bound and is NOT automatically caught by this block; the reviewed contour identity is the safeguard.
8. Reduce pr_holo by a factor10: scalar outgoing height lower should fail. A change to the outgoing sign or elimination of phase113 requires analytical/source review; neither is certified by passing tail arithmetic.
9. Increase pr_profile by a factor10 after its definition: fixed phase normalized profile should fail (or final fixed-target sum if applied later). Conversely dropping its factor2 can spuriously pass; positive normalization is independently proved, and execution cannot replace that proof.

These are nine mutation families, not observed detections. Existing nominal LC tests retain responsibility for shared T/M, radius-transfer constants and normalized target premises. Integration must refresh source/input pins and preserve all existing checks. No W/Git/checkpoint/prompt edit or scientific run occurred during drafting; no model/effort change. Numerical corroboration, if subsequently executed, will not establish a broader coefficient-error contract or an independent physics proof.

Final concurrent-source observation: after drafting, a fresh hash of W/scripts/real_endpoint_autonomous_output_2026_10_17.py returned e932a64925f20f63532f531a6adb5476065ef795d165f649a7dcc3f2cfa6ad8b, rather than the requested baseline93cc122... . The root was notified. This package targets the LC definitions read above; no claim is made to have reviewed the concurrent runner revision or its execution. Integration must resolve that changed source explicitly.
