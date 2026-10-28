# Independent hostile review of TUNIF.md

## PRE-STATED

UTC registration: 2026-10-28 21:50:28 UTC. Written before reading the target or deriving any result.

Scope: TUNIF §U0–§U9; permitted tu1/tu1b check records; NLOC §L5/§L7; NORMS §N4/§N7. At most two additional source files will be used, and identified. No git commands, no edits outside this deliverable, no numerical computation except exact arithmetic in plain Python. Source locations will be obtained by string search, with observed line numbers recorded.

Pre-stated targets and refutation criteria:

1. TU-0/TU-1/TU-2/TU-3: reconstruct the twisted difference algebra and boundary conditions. Refutation: a closed admissible analytic 2-form without the asserted primitive; a residual term in the spread correction; a norm loss larger than the advertised bound; or cancellation by a zero divisor in the actual coefficient space. Distinguish analytic families from individual momentum fibers, particularly resonant fibers.
2. Quantifier Q3: reconstruct what m=0 and m>0 norms imply and identify the consumer's actual norm. Refutation: a quantifier mismatch, an invalid implication from a supremum bound, or an asserted necessity unsupported by the consumer.
3. N-loc-b to N-loc-b': count the constant mode's mass in the specified measure and scaling, and trace the repair into the permitted consumer text. Refutation: incorrect mass or scale, or a consumer needing an unrepaired hypothesis.
4. Checks: rebuild what A/B/C/D/E and the replacement D can decide. Refutation: a falsely excused failure, vacuous/tautological gate, or a control that cannot distinguish the claimed defect. A printed PASS is not verification.
5. Scope: trace d=4, trivial background, abelian/linearised hypotheses through the claimed N1-15 transfer. Refutation: use outside those hypotheses without a separate argument.
6. Across all targets: identify symbol meanings by source location, inspect changing constants and quantifiers, and verify any load-bearing numerical or line citation against the allowed sources.

Review verdicts: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. Findings are appended as the review proceeds; provisional statements will be explicitly revised if later evidence changes them.

## Findings (incremental)

### F1 — TU-0/TU-1/TU-2/TU-3 survive the isolated-fiber attack

**Verdict: CONFIRMED for the analytic-family statements; claim status: PROVEN.** Attachments: `TUNIF.md:259–275` (twisted difference and TU-0), `283–290` (TU-1), `296–308` (TU-2), `317–339` (TU-3). This does not yet validate TU-4/TU-5/TU-6's consumer bridge.

Independent reconstruction: along a line write `a=σg/(z−1)`. The function `a+Σ_{i<u}g(i)` has difference `g(u)` at interior sites, while its seam difference is `(z−1)a−Σ_{i<ℓ−1}g(i)=g(ℓ−1)`. The homogeneous equation forces a line-constant value with `(z−1)a=0`. Operators in distinct coordinates commute, including the seam factors.

For the division estimate, put `w=a+ib`, `|a|≤π/2`, `|b|≤η′`. Rotating the integral by `e^{−ia/2}` gives real part at least `e^{−η′}∫_0^1 cos(a(t−1/2))dt ≥ (2/π)e^{−η′}`. Thus `|e^{iw}−1|≥(2/π)e^{−η′}|w|`; Cauchy's estimate bounds `|g(w)|≤|w|G/(η−η′)`. For `π/2≤|a|≤π`, `Re e^{iw}≤0` gives denominator at least 1. Periodicity and vanishing on the entire hyperplane `p_mu=0` remove every zero. This reconstructs the advertised κ bound.

Apply the first line sum to closedness at `p_1=0`: `D_beta Ω_gamma=D_gamma Ω_beta`. Apply the second at `p_2=0`: `D_gamma Φ=0`. Each remaining transverse cell line makes Φ constant in its cell coordinate and gives `(e^{ip_gamma}−1)Φ=0`. Here Φ is still analytic in the remaining variables, including a free `p_gamma` for some `gamma≥3`. On the open set `e^{ip_gamma}≠1`, Φ=0, hence by continuation Φ=0 everywhere. The finite cell index makes this a componentwise argument in a free module of analytic functions. Evaluation at `p_gamma=0` first would invalidate cancellation, but that is not the stated proof. At all-resonant momentum a constant nonzero plaquette is a closed non-exact fiber field; it is not the restriction of a closed analytic family of the required kind. Thus it is not a counterexample to TU-2 or TU-3.

For the spread correction, the line solve gives `D_beta μ=Ω_beta` first away from `z_2=1`, then everywhere analytically. Set `b_1=−μ/ℓ`, extending it independently of `u_1` and `p_1`. This is an admissible cell 1-form; a twisted difference is an operator, not an extra condition requiring the coordinate values themselves to be quasi-periodic. Its transverse derivative is exactly `−Ω_beta/ℓ`, bounded by G on the original strip. Consequently `G_beta=F_1beta−Ω_beta/ℓ` is bounded by 2G on the original strip, even though μ's bound was obtained only on the smaller strip. Its line sum vanishes at `p_1=0`; one more division therefore uses the original η, not a second strip loss. The remaining curl error is annihilated by D_1 and vanishes by analytic continuation. The estimates are `|μ|≤(1+κ)ℓ²G`, `|b_1|≤(1+κ)ℓG`, and `|b_beta|≤2(1+κ)ℓG`. No extra power of ℓ is hidden in this argument.

**Boundary of this confirmation:** admissibility as a cell 1-form is not admissibility as a nested chain reparametrisation fixing all level-k roots. The latter is a separate obligation in TU-6 and is reviewed below.

