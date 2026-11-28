First failing step: none

# RO1 gate (pass 3): `library/ro1.md`

Referee: Claude Opus 5.5, fresh session, 2026-11-05. One line-by-line reading of `library/ro1.md` (693 lines). I also read `ym4-assembly.md` §5 RO1, `cl1.md` Lemmas 5 and 8 and Theorem 9, `sr1.md` Theorem 1, `ph1.md` whole, and the defect lists of `gates/o4-check-1.md` and `gates/o4-check-2.md`. SA = `scratchpad/sa/ym4.tex`; Y3 = `scratchpad/sa/YM3_I.tex`. No computation was used.

## Findings

1. **Line 80 (H-P).** Attribution. H-P says PH1 gives each component "the H-C and H-S interfaces". PH1 gives H-S (its Lemma 10). PH1 Theorem 1(3) does not list the coordinate-picture Hilbert spaces, the tangential unitaries or the cube cone. Those come from CL1 Theorem 9(3)–(4), applied with integrating states equal to the component's realizing pure states ρ_j. CL1 allows any ρ_j ∈ 𝒢 (Theorem 9 preamble), and its Lemmas 5 and 8 use only the moment limit, the bounds and the mirrors. PH1 Lemma 8 supplies all of these for the component. This is the reading of `o4-check-2.md` §4, defect 1 ("cone-o6 ... apply to σ_ξ"). Not fatal. Repair: in H-P write "H-C for a component is CL1 Theorem 9(3)–(4) applied to its realizing pair (ρ_j, ν_j)", or add the sentence to PH1 clause 3 (see `ph1-gate.md` finding 2).

2. **Lines 217–228 (Lemma 3 statement).** Wording. (3.2) defines Φ = [τ_{−(η/4)e_4}F] and Ψ = [τ_{−(η/4)e_4}G]. These are positive-time classes only if every entry of F and G lies strictly above η/4. The proof uses this through Lemma 2 and (3.4), but the statement omits it. WR1 H4 states it. Not fatal. Repair: add "for F, G with all entries strictly above η/4".

3. **Lines 668 and 684 (exponent remark).** Observation, not a defect. The text says SA's UI10 exponent η^{−4} "must not be substituted into the exponent-five argument". That is right for the displayed constants: ℘ = 9 would give the band 4|m| ≤ 9n. But no step of Lemmas 4–8 needs ℘ = 5. Theorem 6 kills every |m| ≥ 2 by t⁸Γ(t) → 0, whatever the band, because e^{4|m||s|} ≥ e^{8|s|}. The cosh argument handles |m| = 1. Lemma 7 needs only a linear bound a_k ≤ ℘k/2: the increments are then bounded integers, and the divisibility step is unchanged. So p_I = 0 sharpens constants but is not load-bearing for O(4). No repair needed.

## Steps checked (each holds as written)

**Insertion-support bookkeeping (Lemma 2).**
- l = L^{−i} with η/(5L) < l ≤ η/5. The grid L^{−i−2}ℤ⁴ has spacing l/L², so |y − y_*|_∞ ≤ l/(2L²).
- Support radius about y_*: c_Iη + l/(2L²) < l/8 + l/18 = 13l/72 < l/4. This uses η < 5Ll, c_I = 1/(40L) and L ≥ 3.
- |y_{*,4}| + l/2 ≤ η/8 + η/90 + η/10 = 17η/72 < η/4.
- B = τ_{2ce_4}F and A = τ_{−le_4}G. θ_cB = θF and τ_{le_4}A = G, so (2.7) is σ(θF̄·X(h)·G). B lies above c because c > −η/4. A lies above c because c + l = y_{*,4} + l/2 < η/4.
- ‖B‖²_c = ‖e^{−(c+η/4)H}Φ‖² and ‖A‖²_c = ‖e^{−(η/4−c−l)H}Ψ‖². Both times are positive. Contraction then gives (2.1) with C_I = 2Q_0/r_src, p_I = 0.
- These match Y3 IV-56-17: c_I = 1/(40L), p_I = 0 (Y3 L79374–79380).
- Rooted count (2.4): 16 corners · 8^{2m} walks · 2^{16(m+1)} cube subsets, so κ_D = 22 log 2. Per-scale costs and the sum (2.6) checked, including (1+L^j)⁴ ≤ 16L^{4j} and e^{γ′L^j} ≥ (γ′L^j)⁶/6!.
- Small mesh: l/a ∈ {1} ∪ [L, ∞) with L ≥ 3. The bound ‖𝒪_a(h)‖_∞ ≤ 12·64⁴‖h‖_∞ holds for 3 ≤ l/a < 64.
- Cauchy at radius r_src/‖h‖_♯. The same torus-subsequence normalizer E_h serves ρ and ν, so E_h′(0) cancels.
- Lemma 1 oscillation count: 6n³ − 2n² per orientation, times 2β, times 6, is at most 72βn³.

**Plate-exponent bookkeeping (Lemma 3).**
- (3.4) is Lemma 2 with the insertion at time η/4, translated once. Its outside fields lie above η/4.
- M_{h,η} uses B_{h,η/2}, which needs supp h ⊂ B(0, c_Iη/2). Both n_r and s_r are supported in B(0, εη) with ε ≤ c_I/8.
- I checked ⟨Φ, M_{h,η}(x)Ψ⟩ = σ(θF̄·(τ_xh)·G) step by step for real |x_4| < η/8. Every semigroup time stays positive.
- The cube cone gives contraction of T(z) on Re z_4 ≥ Σ|Im z_j|.
- Δ³(|x|² log|x|) = Δ(8 log|x| + 6) = 16|x|^{−2}. Flux −4π²f(0) gives Δ³G_0 = δ_0.
- Norms: ‖n_r‖_♯ ≤ Cr and ‖s_r‖_♯ ≤ Cr^{−5}.
- A polydisc of radius η/128 moves |Re z_4| + Σ|Im z_j| by at most η/32. So it stays in the margin-η/8 tube.
- Cauchy cost 6!(128/η)⁶·4³. With r = εη: ‖V_η‖ ≤ C(εη^{−5} + ε^{−5}η^{−5}) = C_PD η^{−5}.
- Integration by parts carries no sign and no boundary term. (3.3) at η = 4a gives Ca^{−5}.
- So ℘ = p_I + 5 = 5, matching the assembly's "℘ = p + 5 = 5" and SA L28789 "℘ = p + 5".

**Lemma 4.**
- T(v) multiplier, contraction and the Taylor bound r^{−j−k}.
- Padding independence: (b−a) + (v−2b) + (b−a) = v − 2a.
- (4.5) with a = δ/4, so 2a < min r(v_i).
- Gluing over convex overlaps that contain their real parts.
- Band: δ ≥ r_0 cos(3π/8)e^{−|Im z|} gives |a_Y| ≤ Ae^{5n|Im z|}, so c_m = 0 for 4|m| > 5n.
- Interpolation projectors p_m(𝓛) and the boost formula (4.8).
- Gram identity (4.7) and boost positivity; top kernel, (4.10) and the cut inequality (4.2).

**Lemma 5.**
- The measure μ is independent of a, and vacuum subtraction holds.
- Shapes: ∫a_0 = 5/8, ‖a_0′‖ ≤ 12, ∫b_0 = 1, ‖b_0′‖ ≤ 3/2, b_0(s) + b_0(1−s) = 1, ∫ρ_0 = 5/2.
- Half-widths 3h/8, h/4, 3h/2, 3h/2; squared sum 301h²/64 < d² with d = 5h/2.
- Reflection distance 17h/4 ∈ [d, 6d].
- ∫f ≥ 125Ah⁴/128 = (1/120)(3A)d⁴; Lip ≤ 70A/h ≤ 4800A/h.
- (5.4) uses 2N terms, each of size 3Au^{1/2}.
- Low-energy transforms: time ≥ (h/2)e^{−3}, space ≥ h/8 because |xq| ≤ 1/4.
- C_φ = 256e⁶[150R²A]², using N ≤ 25R²h^{−2}.
- Tonelli, and t⁸Γ(t) ≤ t⁹Q_εm(Q_ε) + 8!ε.

**Theorem 6.**
- g_r(is) = ∫e^{−r(E cosh s + q sinh s)}dμ ≤ Γ(re^{−|s|}) = o(e^{8|s|}).
- The three-term identity holds for 1 and e^{±4iz} with C = cosh 4.
- Pushforward: −tE_s + ixq_s gives R_{is}(t,x), so the transform of μ_s is G at R_{is}(t,x).
- (6.4) ⇒ ν ≪ μ (diagonal cone); c_0 ± 2c_1 cosh 4s ≥ 0, so c_1 = 0.
- Polarization handles mixed labels.

**Lemma 7.**
- Rotation by π/k gives k | 2M(2k).
- Zero-set propagation through (4.10) and connectedness of the configuration space; arc reduction with odd index sums.
- Convexity 2a_k ≤ a_{k−1} + a_{k+1} from (4.2) with (k−1, k+1). Bounded integer increments; D = 0 by divisibility; empty-tuple cut.

**Lemma 8.**
- (8.1)–(8.2): the cube-cone multiplier bound.
- Time-tie induction on q ≤ n(n−1). The common cut separates the same groups in both frames.
- Identity theorem along I; finite angle steps.
- Cutoffs near the diagonals cost ε^{−r} and flatness gives ε^N, so the cut-off tests converge to the original in Schwartz seminorms.

**Theorem 9.**
- Coordinate-plane rotations generate SO(4), and W_4 supplies the other component of O(4).
- Self-centering: (ρ_j, ρ_j) realizes the self-centred hierarchy by the finite subset expansion. The triangular map is unitary between the forms and preserves the cone. The mean is restored by the same expansion.

**Componentwise scope.**
- H-T is applied to the component's own connected two-point function. TP1(4) is assumed for every approximating periodic state, so it passes to the realizing ρ_j: cov_{ρ_j} → S_2^T[σ_ξ].
- Lemma 2's constant is uniform over the states.
- Theorem 9 runs Lemmas 1–8 for each realized component and never infers covariance from the mixture (lines 649, 680, 688).
- This matches SA L31799–31831: "the angular chain proves covariance for each realized component".

**Against the assembly entry.** Theorem 9 clauses 1–5 match `ym4-assembly.md` RO1(a) (1)–(5), with p = 0. The imports match (b).

**SA/Y3 readings confirmed.**
- SA L28490–28518: UI10 has Cη^{−4}.
- SA L28787–28789, L28836: ℘ = p + 5.
- SA L28569–28571: "The preceding insertion theorem supplies p = 4".
- SA L31799–31856: per-component scope, TU10 "uniformly in the approximating states", ϑ_* = 1/12000.
- Y3 L79104 is IV-55-9 and Y3 L79374 is IV-56-17 (c_I = 1/(40L), p_I = 0). This confirms the locator correction at line 691.

## Verdict

RO1 is a correct conditional implication. Rooted D1, LG1, CL1(2)–(4) and state-uniform TU10 give full scalar O(4) covariance on separated compact C¹ tuples and on the diagonal-flat extension, for each realized component. The insertion support and the plate exponent are correctly kept. The three findings are an attribution, a missing hypothesis in one statement, and a remark. None breaks a statement.

Checked line by line by Claude (fresh session).
