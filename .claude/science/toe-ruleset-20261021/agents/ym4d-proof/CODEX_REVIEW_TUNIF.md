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

### F2 — The original tu1-D criterion is satisfiable; the stated excuse is false

**Verdict: REFUTED** for “unsatisfiable by the truth / cannot PASS”; **CONFIRMED** for the recorded seed-777 FAIL and the repaired finite-sample inequality. Attachments: `TUNIF.md:541–551,649–651`; `checks/tu1_criteria.md:37–42`; `checks/tu1b_criteria.md:8–18`; `checks/tu1_twisted.py:264–284`; `checks/tu1b_pole.py:12–24`.

Four sample values `10^-1,...,10^-4` span three decades. A pure pole `A/ε`, A>0, grows by **exactly 1000**, satisfying the original **≥1000**, not violating it. For `A/ε+B`, with positive endpoint values, the ratio is `(10000A+B)/(10A+B)`: below 1000 if B>0, equal if B=0, above if B<0. The existence of a pole alone cannot decide which case holds.

An exact input of the actual construction makes this decisive, not merely a toy scalar objection. Set ℓ=3,d=4, `a_1(u)=1_{u_1=2}`, all other components zero, and `F=D∧a`. Use the script's transverse twists `(z_2,z_3,z_4)=(5/4,3/7,7/5)` and `z_1=1+ε`. Then `F_1beta=−ν_beta·1_{u_1=2}·1_{u_beta=2}`, Ω_beta=`−ν_beta·1_{u_beta=2}`, μ=−1. The corrected solution has `b_1=1/3`, `b_beta=(u_1/3)ν_beta·1_{u_beta=2}` and **max|b|=8/21**, independent of ε. Omitting b_1 gives **max|b|=4/(7ε)**. Thus the four uncorrected maxima are **40/7, 400/7, 4000/7, 40000/7**; growth **1000**, corrected variation **1**, and the original gate **passes**. Exact Python evaluation with the existing functions reproduced these values and zero corrected residuals. No floats or file writes were used by that check.

For the actual seed 777, exact recomputation gives corrected max **158/15** at all six values. The uncorrected maxima are `(1200,11433,113763,1137063,11370063,113700063)/7`, equivalently **1137/(70ε)+9**. Original growth is **379021/400 = 947.5525**, so the recorded 947.6 and FAIL are correct rounded reports. The repair's successive ratios are `3811/400`, `37921/3811`, `379021/37921`, `3790021/379021`, `37900021/3790021`; they satisfy its rational thresholds 9 and 99/10. The mathematical phenomenon is intact, but the correct explanation is **an over-demanding threshold for this pole plus its positive regular part**, not a gate unsatisfiable by a true pole.

The replacement gate also does not characterize a simple pole: the implementation only checks lower bounds on ratios. A double pole has successive ratios **100**, which satisfy every uncorrected-side inequality at `tu1b_pole.py:23`. “Must approach 10” in the criteria is not implemented as convergence, monotonicity toward 10, or even an upper bound. The observed sequence is consistent with a simple pole (and the exact formula above establishes one for these samples); the gate itself cannot exclude higher-order poles. Claim status of the gate's asserted diagnostic sufficiency: **GAP**.

### F3 — The m=0 consumer is real; the m>0 argument does not follow from a sup bound alone

**Verdict: CONFIRMED** for the need to control unrestricted configuration legs for the named N_0 consumer; **REFUTED** for the general “sup bound alone” inference; **NOT-VERIFIED** for a replacement proof for this particular chain at every m>0. Attachments: `TUNIF.md:158–187,196–211,588–590`; `NORMS.md:331–332,422–431`; `PROOF.md:5885–5887,5918–5922,6058–6059`.

For a scalar row M, `Σ_y|M_xy|=sup_{|Y|∞≤1}|Σ_y M_xy Y_y|`, by choosing each Y_y to align the sign. A decay constraint `|Y_y|≤e^{−m d(y,x)}` excludes that global sign pattern. For example `M_xy=1` has unweighted row mass T^d but decay-restricted row action bounded by `Σ_{Z^d}e^{−m|y|_1}`. Thus a bound only for the stated m>0 test class cannot furnish the BR1 N_0 bound. BR1 explicitly uses N_0 at the cited current lines. NAH1's later weighted estimates still import N_0 bounds for local Hessian factors; the positive operator weight there is not permission to replace those factors with a decay-restricted trilinear test norm. In block/color spaces the scalar sign identity needs the corresponding finite-dimensional norm comparison; exact equality of block-norm row sums is not automatic.

However, the factors `e^{−m d(p,x)}` in TUNIF's vertex sum concern the **responses at the vertex p**, whereas the decay restriction is imposed on the **coarse input**. An unweighted `∞→∞` bound does not transport that decay. Counterexample: on a T^d-site torus let `(RY)(p)=Y(x)` for every p. Then `||R||∞→∞=1`, uniformly in T, while the unit decay-admissible input Y=δ_x has RY identically 1. The local cubic `V(X,Y,W)=Σ_p(RX)(p)(RY)(p)(RW)(p)` equals T^d on three such inputs. The claimed leftover decaying factor cannot be inferred from sup bounds. This refutes that inference, not the Yang–Mills chain theorem by itself. A weighted response estimate, or another use of locality/cancellation, is required; NORMS's second N-loc estimate at 423 is exactly an extra weighted input-to-output property.

The m>0 theorem would be a meaningful weaker/easier theorem if its weighted transport hypotheses were proved, not a vacuous statement. The target's main T-UNIF statement is explicitly at m=0, so no hidden m>0 substitution was found in that statement. Full identification with the original N^F-2 definition remains outside the permitted NORMS sections.

### F4 — Mean subtraction loses a factor; harmonic mass uses an upper bound as equality

**Verdict: REFUTED** for the displayed mean-subtraction arithmetic and the equality for one-link harmonic mass; **CONFIRMED** for volume cancellation in the harmonic-mode budget, conditional on the stated harmonic response. Attachments: `TUNIF.md:365,378–392,578–579`.

Write n=k−j. A single unit coarse link in orientation v has mean vector `c_k=T^{−d}e_v`; if its harmonic response is `c_j=L^{−n}c_k`, summing over the **one occupied orientation** gives exactly `T^dL^{dn} L^{−n}T^{−d}=L^{(d−1)n}`. Summing the maximum component over all d orientations yields the conservative upper bound **d L^{(d−1)n}**, not equality for this δ_x. This harmless factor-d overcount leaves the T-free conclusion intact. The harmonic response formula itself relies on Q preserving the mean sector and on orthogonality in the chain form, not just on `Q(const c)=Lc`; its full chain derivation is not supplied by the allowed sections.

The subtraction of the constructed primitive's mean has a different missing factor. Line 392 assumes `|mean b|≤𝔠_0L^{−k}c_{η′}T^{−d}`. Multiplying by the number `dT^dL^{dk}` of level-0 links gives **d𝔠_0c_{η′}L^{(d−1)k}**, not the stated **dc_{η′}L^{(d−1)k}**. The lost factor is **𝔠_0**; at transported levels the direct Q estimate also brings its 𝔮_0 when applicable. Using only the stated envelope and harmonic bound, a safe level-0 estimate for `b−mean b+c_0` is **d(2𝔠_0c_{η′}+1)L^{(d−1)k}**. This is a sufficient triangle bound, not a lower bound or a claim of optimality. The file gives no inequality allowing the omitted 𝔠_0 to be replaced by 1, and M in 𝔠_0 is a free imported bound. Its displayed all-level 𝔠_L therefore is not established by this arithmetic.

Symbol check: `TUNIF.md:365` and `578` both define **𝔠_0=4(d−1)(1+κ)M**. There is no factor-two discrepancy between them. The error above is the omission of the entire 𝔠_0 in the mass calculation.

