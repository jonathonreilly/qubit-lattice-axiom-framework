lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-01T06:34Z

# Gate: Lemma EX and Lemma EX2 (`library/sector-values.md` 3A, 3B), SU(2), d = 4

**Provenance.** anthropic/claude-opus-5-5, effort high, Mac mini worker, mapped side, statement pinned at 7c12c6981. The branch head moved to c2b81fab0 during the work, with no change to `library/sector-values.md` or `FINISH.md`. A same-model check is not independent in model and is not an audit. Verdicts steer research and grant no status.

## Verdicts

| Statement | Verdict | Basis |
|---|---|---|
| Lemma EX, W = 1 | ADVANCE | Steps stand; defects D4, D6, D7 are local. New reduction R1 removes the level from this form. No violation in reach. |
| Lemma EX, weighted | ADVANCE, on weaker evidence | Steps stand by scale count. Numerics: 40 random W per nu, two fields. |
| Lemma EX2 | CORRECT-NO-ADVANCE | No counterexample, and the abelian case holds exactly. But a step fails as written (D1), the expansion omits terms (D2), and the statement names no gauge (D3). Nothing downstream, Prop DS included, may rest on it until it is rewritten. |

**No WRONG.** Item 7 of the queue is not blocked. All of this rests on Prop AN3 and Theorem F-D, neither gated. The numerics find nothing; they do not prove a bound.

**The main gap in what was tested:** no field with a topological charge at small flux was tested. See Limits.

## New result: R1 (proved here, short)

For W = 1, V^*(V') lies in the fibre of V', so its Wilson energy is at least the one-level fibre minimum. Hence e_j(V') >= e^(1)(V') at every j, with the same f, E, I. **So the unweighted Lemma EX at all levels follows from the statement at level one.** Only the weighted form and Lemma EX2 can depend on the level. Measured: e_(top, k = 2) - e^(1) > 0 on all eight runs, 7.5e-7 to 3.2e-4 of E.

## Defects, ranked by what they break

**D1. EX2: the bound on d_{V'} delta F is false as written.** The text has d_{V'} delta F = [F, h], "at most |F| |delta F| in the gauge at x". But h is a sum of delta F along the radial path, so |h| is about r |delta F|, not |delta F|. Measured, ||d_V delta F||^2 / (f_m^2 ||delta F||^2) at m = 0, 1, 2: 2.64, 3.90, 7.37 (worst bond, f = 0.0447) and 2.63, 3.89, 7.48 (f = 0.0508). So the constant is not uniform on these runs. That is two steps of a trend, with s^-2 expected by hand. On the mix background it stays near 1: 1.09, 1.11, 1.26.
*Repair, unproved:* ||[F, h]||^2_{l^2} <= ||F||^2_{l^4} ||h||^2_{l^4} <= C s^2 f_k^2 ||h||^2_{Eps}, by the first clause of (COMP)(i) and the box Sobolev bound in a box gauge. This is at or below the C(L) f ||delta F||^2 the proof needs. Measured ||d_V delta F||^2 / (s^2 f_k^2): 15.8, 12.3, 3.9 and, on mix, 6.6, 17.3, 4.9, so bounded on these runs. The Sobolev note was not read for this gate.

**D2. EX2: the second-variation display omits terms.** D^2 of Q(F) along the chain is 2 Q[delta F] + 2 Q(F, delta^2 F), with delta^2 F = D^2 F[h, h] + DF[h^2]. The text keeps only DF[h^2]. It also drops the variation of the transports inside Delta_y F.
*Repair, unproved:* read the second term with the full delta^2 F, which is what (COMP)(i) bounds. Bound the transport terms by eps |Delta delta F|^2 + C |h|^2 |F|^2, summed with the Hoelder step of D1.

**D3. EX2: b_m is not defined.** delta_b theta changes by [phi, theta] under a t-dependent gauge, and the statement names no gauge. D1 and D2 both need one.
*Repair, unproved:* state b_m in the gauge of Prop AN3, or in a box gauge. Prop DS reads the same quantity and needs the same fix.

**D4. EX and Prop GS: "(toron term)" has no formula.** Section 3A never defines it. The only computation is Lemma O3's C(L) Phi(e^-8 N/4) per box, for g_i and not for the excess. At a flat field e = 0 exactly, so a per-box constant is not the true size there.
*Repair:* state it in Lemma EX as that per-box bound, or derive the excess form.

**D5. "Sup flux falls", f_j <= f_{j+1}/4, fails at L = 3 on zone-corner parents.** f_j/f_{j+1} = 0.2727 (wave, k = 1), 0.2644, 0.2532 (mix). Constant links give 0.112. It may lie below L_0, which is not stated. EX2 and GS need only a ratio below one, so nothing breaks.
*Repair:* state the ratio as a constant below one.

**D6. EX Step 4(iii) bounds d_{V'} F, but Step 3 uses flat d on psi_a.** The difference [A, psi] has size f r |psi|, so it adds C M f ||psi||^2, the same order. Harmless, but it is not written.

**D7. EX Step 1: the hypercubic average "leaves the sum unchanged" only if the block map is covariant.** A comb of one axis order is not. Measured spread of e over the 24 axis permutations: spread/(f E) = 1.4e-3 at f = 0.079 and 3e-5 at f = 0.013. Harmless: K is unaffected, and the error is below the term allowed.

**Not a defect, but worth knowing.** Lemma EX has content only where I >> f E. Where I is of the order of f E, which includes instantons at every radius (I/(f E) is a pure number), the error term covers it and the coercivity says nothing. So the lemma says little about a charged region. What carries the sum over levels there is the fall of f.

## Registered criteria (`checks/gate_ex/CRITERIA.md`, written before any run)

c_1 = c_e/2. C_eff := (c_1 I - e)/(f E); negative means e >= c_1 I, so the lemma holds there with no error term.

| Criterion | Outcome | Numbers and caveats |
|---|---|---|
| V1 | PASS | Covariance 8e-16. |
| V2 | PASS, one exception | Solver points below 1e-9. `x_adv2.py` accepted at g < 1e-6, looser than V2. |
| V3 | PASS | e/E 1.45466 v 1.45455; 0.80007 v 0.80000; 1.84937 v 1.84919. |
| V4 | PASS, weak | Random perturbations; three abelian fields only. |
| X1 | PASS | sup C_eff, N' = 1, three seeds agreeing to 4 digits: -0.401, -0.386, -0.379 at f = 0.08, 0.032, 0.0128. Named shapes stable within 8 percent. The rule is lax for negative C. |
| X2 | PASS at N' = 2, 3 near f = 0.1 only; **N' = 4 not run** | See below. |
| X3 | PASS | e/I at L = 5, 7, 9, fixed f L^2: 0.2406, 0.2452, 0.2468 (D3); 0.1607, 0.1636, 0.1641 (D2). |
| X4 | PASS at N' = 1, k = 2; **k = 3 not run**; ratio clause **not decided** | k = 3 needs N = 27, about 7 GB, over the 2 GB limit. N' = 2 energies were not logged, so that case rests on R1. The ratio clause is ill-posed for negative values and compares different fields. |
| X5 | PASS | sup C_W negative throughout: -1.44 to -6.53 at k = 1, f = 0.087. e(W)/I(W) stays 0.156 to 0.366, above c_1 = 0.049. Random W, not an adversarial search. |
| X6 | PASS after two script fixes | Min (g - 1)/|P-hat|^2 = 0.098765, 0.106667, 0.108844 at L = 3, 5, 7, ratio 1.0000, infimum at P -> 0 along (1,1,1,0). See below. |
| Y1 | **Vacuous** | The script's sum telescopes, so it could not fail. Real check, V = 1 only: the solver's D^2 Y_2 = 67.25805 against Fourier 67.257664. |
| Y2 | PASS | d^2 e_j / b = 0.32 to 0.70 against c_e/2 = 0.049, so err < 0 on every run. |
| Y3 | PASS | All 12 (mu, colour) at f = 0.0447: b(V)/b(1) <= 0.963 at m = 1, <= 0.994 at m = 0. Worst at k = 2: b_2(V)/b_2(1) = 0.952, b_2 = 18.1 < b_1 = 74.5. One site by symmetry, const background. |
| Y4 | **FAIL at m = 0 to 1**, artefact; PASS at m = 1 to 2 | Rise 4.4 to 4.5 against a cap of 1.5, at V = 1, an exact abelian value: my cap was miscalibrated, as (i) allows C(L). m = 1 to 2: 1.45 to 1.46. |

**X2 in full.** On in-domain points sup C_eff = -0.401, -0.390, -0.301 at N' = 1, 2, 3 (f = 0.08, 0.096, 0.138). The rule was written for positive values; the sign never changes and the steps are +0.01, +0.09. The rise comes through the denominator: I/(f E) falls 4.8, 4.4, 3.2 as flux localises, while e/I stays 0.133, 0.139, 0.143. N' = 3 had 25 steps against 40 and was still rising slowly. Lowest in-domain e/I on any field: 0.1125 (T2), above c_e = 0.0988.
Runs that do not count: the ft = 0.0128 runs at N' = 2, 3 left the domain and give no small-f data at N' >= 2. They reached f = 1.57 and f = 1.17, the second with e/I = 0.053 at L^2 f of about 10, so coercivity does weaken at large flux, outside the lemma's hypotheses. The first search, `x_adv.py` at N' = 2, is void: it stalled and its BEST is its start point. Its f = 0.08 toron start crashed.

**X6 in full.** The first run gave a registered FAIL (0.905, then -1.68, -0.50). Alias signs need P in the fundamental domain and my optimiser left it. A second fix floors |P-hat|^2, as L = 7 then gave -1.06 at P = 0 by roundoff. Both fixes followed a FAIL. The log is kept as `x_symbol_unwrapped.log`. By hand at small P: (g - 1)/|P|^2 = 2c (1 + sum p^4 + min_{a perp p} sum a^2 p^2), c = (1 - L^-2)/24. On the family p^2 = (u, u, u, w) this is 2c (4/3 + 2w/3), least at w = 0, which is the stated value. That covers one family only and is no proof over all P.

**Added after registration, report only.** `x_abelian.py`, the D1 ratio, `x_order.py`, and `run_y3.py`. `run_y3.py` was run because Y3 as registered needed an adversarial bond at f <= 0.05, which the earlier runs did not have.

**EX2 abelian, levels, exact.** D^2 Y_k = 40.96, 67.26, 72.20, 72.80, 72.87, 72.879, 72.880 at k = 1 to 7 (N' = 2). N' = 4 runs 28.73 to 46.852. Increments fall at a ratio tending to 1/9 from 0.64, so the slow early ratio is pre-asymptotic. It reproduces the solver at k = 1, 2 to 1e-4. Since D^2 Y_k = sum_j D^2 e_j >= 2 c_e sum b in the abelian case, EX2 holds there given c_e.

## Limits

- **Sectors.** Both instanton runs are void: one crashed, and one has residuals 2 and 0.3 with a parent of S = 97 against 39.5 and f = 1.5. Peak flux is 2/rho^2, so f near 0.08 needs rho near 5 and N' >= 20, out of reach at 2 GB. No charged field at small flux was tested in d = 4.
- **Reach.** k <= 2 in SU(2). N' <= 3 at one level. Only f = 0.0128 approaches a_* <= c L^-2 at L = 3.
- **Sup over fields.** -0.38 is a sup over what was searched. On a torus of N' of about 8 or more, constant abelian flux has e = I = 0, so C_eff = 0 by Lemma 3.3 (by hand, not run).
- **Second-variation repair.** D1 to D3 are repairs only; the rewritten EX2 has not been gated.

## Read and not read

Read: `FINISH.md`, `GOAL.md`, `library/sector-values.md` Sections 0 to 3B and 7, with grep lines of 8; `library/analytic-lift.md` AN1 to AN4; `library/composite-adjoint.md` to Lemma AD1; lines 25, 47, 126 and Lemma 3.1 of `parts/hard-core--mapped.md`; `checks/hard-core--mapped_excess.py`, `_lift_su2.py`, `_lift_gradient.py` in part.

Not read: `parts/hard-core--independent.md`, any gate on it, the Sussman-Alpoge repository, Theorem F-D, HS-P, HS-T, `library/lattice_sobolev_box_gauge.md`, `library/one-step-closure.md` beyond grep, `library/sector-values.md` Sections 4 to 6.

Logs and JSON are in `checks/gate_ex/`. The `.pt` fields and the `.sh` drivers were lost at a tree reset; the logs record every command and start time. The memory gate held jobs at times from 20:50Z, none was skipped. All numerics ran under the lock, now released.
