# Gate: IN1 distil (`library/in1.md`), pass 3

First failing step: none.

Scope. One line-by-line reading of `library/in1.md` (668 lines) at clone HEAD `2c30ac7a0`. I checked it against `library/c4-order.md`, `library/um-envelope.md`, `library/pr-lay-draft.md` (§0, §8, §10), the other cited notes (`b-value.md` Theorem V, `prefactor-loc.md` Theorem S/Corollary T, `b4-induction.md`, `layered-a3.md`, `c1-repr.md`, `geo5c-count.md`), and the gates `carrier-check.md`, `b4-ind-check.md`, `geo5c-gate.md`, `sa-2.8-terms-gate.md`. `p82.md` is not cited by in1, and in1 uses no import from it. I read the SA and YM3 lines listed in Section 3. Research text. Not an audit. Grants no status. No computation was used as a proof step.

## 1. Findings

All findings can be repaired. None is fatal.

**F1. Line 5. Source record is missing.** The link `../checks/in1-distill/source-checks.md` points to no file at this checkout (`git ls-tree -r HEAD` has no such path). The locator corrections at line 658 cite that record. I checked those locators directly, and they read as stated:
- YM3 63108–63112 gives r≥2, 𝔭₀≥6r+1, q≥41𝔭₀+1.
- YM3 63239–63248 gives B_nm ε_dc ≤ γ₀/2 and (LM)³ε_dc ≤ 1.
- YM3 63448–63458 gives γ₂=(LM)⁻³.
- SA FG11 is at 14084, and the proof ends at 14088–14089.

Repair: add the record, or remove the link.

**F2. Line 79, (7). X̃ is not defined.** The supremum is over 𝒟_i(X̃). The text never defines X̃. Repair: define it (the creation-domain hull of X), or write X.

**F3. Lines 127 and 400. "List size" is not defined.** H-SF says "provided its list size is at most N_*". Lemma 5 then bounds Σ_j f_{n+1−j}‖E^{(j)}‖ + Σ_j w_{n,j}‖R^{(j)}‖. This sum agrees with SA R18 (5993–6010):
- set ν=n+1−j;
- then (k+2−j)^{3/2}L^{−α_H(k−j)} ≤ C_age ν^{3/2}L^{−α_Hν};
- the w term is ϱ_j² ≤ C(k+2−j), with the maximum over all three radii. All α_ι have the same θ-dependence, so one ratio suffices, as (13) says.

Repair: define the list size as this sum.

**F4. Line 155 (H-G) and line 501 (Lemma 8). The definition of "light" goes in one direction only.** The text says "a light node has o(u) ≤ C_g". Line 501 bounds Σ r̂|C(u)| by 2C_g O + C_g(C_g+1)Q. That step needs 1+o(u) ≤ 2o(u) at every non-light node, that is, o(u) ≥ 1. The one-way statement does not give this. SA 17744 defines a light component as "one with at most C" occupied cells, which goes both ways. Repair: define a light node as a node with o(u) ≤ C_g. Then every non-light node has o(u) > C_g ≥ 1, and (31) follows with the stated C_cnt. I checked the arithmetic: (5C_g+1)C_g·2 + 4C_g²s₀.

**F5. Lines 312–316 (Lemma 2, bound on C−C_*). One factor is left out of the display.** At a varied entry, the η term also carries the parameter weight. The floor and a ≤ ‖A‖ ≤ HV(μ₀) give

  Σ_y η e^{−μ₀d}(1 + e^{16κ̄+μ₀d/4}·1_{d≥M}) ≤ (9/8) η V(μ₀/2).

The display leaves out the factor 9/8. H_0 absorbs it. Line 325 handles the Γ term the same way ("the assumed floor absorbs the parameter weights"). Repair: add the factor, or reuse the remark at line 325.

**F6. Lines 227–234 (constant order). c_lin has no row.** Lemma 6 (lines 452–457) fixes c_G from c_lin²/16 and from the certificate multiples (A₁/A₀)². c_G is in row 7. The table names neither c_lin nor H-C's certificate constants (κ_pos and the collar/rim fractions). Row 8 says "all remaining … constants precede X₀". Read that way, c_G would come before a constant it depends on. Repair: put c_lin and the certificate constants in row 7, before c_G. (A₁ and A₀ are in row 6, which is correct.)

**F7. Lines 233, 417 and 548. The boundary volume cost is not in the floor on c₁.** Lemma 5 says the interior volume cost of the boundary maximum 𝖡 "is included later in c₁". Row 7 and the proof of Theorem 10 set c₁ ≥ c + C_env + C_int + c_ent. That floor has no volume term. Repair: add the volume cost (C_vol of c4-order row 17) to the floor, or say that C_env contains it. c₁ is chosen before X₀, so the order does not change.

**F8. Lines 227–230. Some floors from c4-order are not listed.** Row 2 leaves out L² ≥ 6√2 λ_a (c4-order row 3). Row 4 leaves out κ/4 > κ_D and the history-entropy floor on κ (c4-order row 8). Each one is a floor on an upward choice, applied where in1 already makes that choice. So the order stays valid. Lemma 3 already takes κ large. Repair: list these floors.

**F9. Line 108. The Outstanding note does not cite all the relevant work.** It names SA 14141–14205 and the PR1 inputs. It does not mention `carrier-adopt.md` §6 or `inv-root.md`. `gates/carrier-check.md` §6 (Codex) marks those as ADVANCE: they supply um-envelope (6) for the specified inv-root series, with constants fixed before M and κ̄ (see also `gates/b4-ind-check.md:41`, b_d=32). So the open item may be smaller than line 108 says. It may only be the identification of that adopted series with the actual UM carriers, together with its heredity. The heredity example at lines 329–334 is correct (R_{22}=1+⅜(t²+u²)+…). It applies to the geodesic-weighted entries of the global root R(A) in (20). It does not automatically apply to a walk-tagged series. The text already says this ("refutes inferring carrier heredity from this construction"). This finding is not an error in any proof. Repair: cite those notes.

**F10. Line 574. One smallness condition is implicit.** The Haar-ball bound c_H s³ uses s ≤ 1, that is, X₀ ≥ c_ball². Repair: add this condition to the X₀ list in row 9.

**F11. Notation is overloaded.** These letters each carry several meanings: P (the UM count in (22), P_j, the pair in A(P)); a (gap, a_p, a_j, radii); A (A_{K₀}, the action, the matrix, 𝒜_j); d (rate in (9), distance); D (degree, D₀, D(x,y)); W (W₀, kernel, W(𝒮)); R (remainder, R_j, R(B)); t (tube, level, path length, radius parameter). This affects clarity only. No step is ambiguous in context.

## 2. Check of each statement

- **Definitions (1)–(8).** f_U²=2a_p holds, since ‖e^{iφ}−1‖²=2(1−cos φ). The tents sum to one. (5) agrees with SA R16 (5940–5955). The volume in (6) dominates SA R25's v up to the C_v of H-G, because (1+log x_n)(MR_n)⁴|C|_n majorizes log θ · sites.
- **Lemma 1. Holds.**
  - Conjugation cost: μH'/(e(μ'−μ)) ≤ a/2 at μ₁, using μ'−μ₁ ≥ μ'/2.
  - The resolvent bound follows from accretivity. The entry bound follows from norm ≥ entry.
  - The root integral is √(2/a). The scalar identity (1/π)∫ζ^{−1/2}(ζ+b)^{−1}dζ = b^{−1/2} holds.
  - Difference bound: the constant ½(2/a)^{3/2} is the derivative of b^{−1/2}. V(μ₁/2)² is a valid overcount (one V suffices). This needs n_c ≥ 1 and the triangle inequality for d.
- **Lemma 2. Holds,** apart from F5.
  - A segment of ℓ sites meets at most 2⁴ cubes. The segment count is ⌈(d+1)/ℓ⌉ ≤ 1+d/ℓ. M ≥ 128κ̄/μ₂ gives 16κ̄/(LM) ≤ μ₂/4.
  - Compression perturbation: at most a/4. Gap 3a/4.
  - K₀ and H₁ hold as displayed.
  - The second Γ term gives e^{32κ̄−7μ₂t/4} ≤ e^{32κ̄−μ₂M/4}e^{−3μ₂t/2} for t ≥ M.
  - Schur identity at s=1: C + CA₀₁(A⁻¹)₁₁A₁₀C = (A⁻¹)₀₀ by block inversion, with RRᵀ=A⁻¹.
  - Wall factorization: correct.
- **Lemma 3. Holds.**
  - UM15 as printed at SA 14513–14528 is C₀ = C_pW₀L⁴ + A_Kc_m(LM)⁴(ε+C_pW₀M⁻⁴+γ/2). This expands to in1's form, with D₀=Ac_mL⁴.
  - With (22) and (23), each of the three terms is ≤ 1/3.
  - UM14 (SA 14518): PW₀M⁻⁴ + γ_tilt/2 ≤ ρ₀/2 + ρ₀/2.
  - The window in (24) is nonempty, because L > 2C_h^WF C_h^UM c_ℓ(1+4β_s) suffices and row 2 asks for 4×.
  - Failed-bond floor: p_⋆=n_bp ≤ e^{−Θ}/4. Together with e^ΘA_a a ≤ 1/4, this gives UM22–UM23's τ ≤ 1/2 (SA 14622–14638).
  - W₀ here is ≤ um-envelope's ρ₀M⁴/(2P). It is M-free, so it may come first.
- **Lemma 4. Holds.**
  - Telescoping with |a_j−a_i| ≤ 2c₂ gives λ_♯=c₀−ς and B_♯=c₀+2c₂+ς.
  - These differ from SA RF22 (c₀/2−ς̄, C_β+ς̄), but they are derived directly from (10)–(11) and are correct.
  - Defining ς as sup_{x≥X₀}u is safer than C′γ^{κ₀−8}, since the f-part of RF20 (SA 20687–20690) is of order γ(log γ⁻²)^{𝔭₀}.
  - λ_♯ ≥ 3c₀/4 ≥ λ̲ and B_♯ < B̄=c₀+2c₂+3.
- **Lemma 5. Holds** (see F3).
  - θ_j/θ_n ≤ 1+B̄m/X₀, the log ratio is ≤ 2, and θ_j ≥ ½(X₀+λ̲m).
  - The series is summable because κ₀ > 4.
  - Circularity E₀ → N_* → s_kN_* is cut by X₀ (C_E is free of E₀ and N_*).
- **Lemma 6. Holds.**
  - Row sum L², column sum L⁻², ‖W‖_{2→2} ≤ 1, ‖W^h‖_{1→2} ≤ L^{−2h}. These are the 4D analogue of YM3 6800–6803, where the column sum is L⁻¹ in 3D.
  - The count of 24 cones is right: 6 planes × 4.
  - Cone recursion: q_ρ = min{⌊s_ρ/L⌋, R_ρ−2} covers both corners when R_ρ ≥ 2, that is, when l < t−1.
  - Bootstrap: 24·(9/8)·4 = 108. e_L ≤ ϖ_L²/4 keeps the curvature ≤ ϖ_L.
  - Witness: x_{t−1} ≥ θ_t/2 for X₀ ≥ 3c₅, which gives c_lin²P_t²/16.
  - The other certificates scale as (A₁/A₀)²P², which agrees with SA 18287–18327.
- **Lemma 7. Holds.**
  - C_z = (2/π)(√π/4)(π²/2)^{3/2} and c_z = 8e^{−1/2}/(3π³) are correct.
  - The ball contains {φ < θ^{−1/2}}, since 2 sin(φ/2) ≤ φ.
  - (30) follows by triangular injective change of variables and Tonelli.
- **Lemma 8. Holds** (see F4).
  - Contraction: monotone r̂, with each creation counted ≤ s₀ times.
  - Stretch assignment: injective. A merger is the first entry through a non-first predecessor on the unique upward path. Each cell is used ≤ 2 times and each mark ≤ 1 time.
  - 1+log x_n ≤ 4R_n for X₀ ≥ max(e, 2c₅).
  - T_t r̂_t ≲ (log θ)^{6r} < P_t/2 because 𝔭₀ > 6r.
  - Leaf: P_t ≥ (1−ε_rar/2)P_i.
  - Cut leaves: c_G ≤ c_w/(2N_cut).
  - SA's ledger (17741–17762) gives a mark the gain p_t=P_t. in1 uses P_t/2, which is weaker and adequate.
- **Lemma 9. Holds.** D^{2(N−1)} rooted sets, and V° ≥ N. This agrees with SA 18712.
- **Theorem 10. Holds as stated, conditional on H-LF, H-G, H-C and H-E.**
  - The induction on finite operation ancestry is well founded.
  - Borel majorants with summable allowances, Tonelli at fixed inner variables, then e^{C_int V°}.
  - The inner sums with w⁻¹ give exactly 𝔐_c ≤ 1.
  - Then (32) with the root cells |C(root)|=|X|_i, then (33).
  - The drop-out and fixed-exterior cases use the same steps under H-E.
- **Theorem 11. Holds as stated, conditional.**
  - The class clauses are returned by Lemma 5 (E), H-SF (R, 𝖡, domains, structure), Theorem 10 (mass) and H-O ((18)). Each is used where needed.
  - (35): 4N links, Haar mass (c_Hs³)^{4N}, s=c_ball x^{−1/2}. This gives 6 log x and agrees with SA 19792–19804 (see F10).
- **Theorem 12. Holds as stated, conditional.**
  - Existence: x_{k+1} > h ≥ X₀ via b_{k+1} ≤ B_♯ (Lemma 4 applied before the class step).
  - The θ=x tube has zero deviation.
  - Termination comes from the lower drift.
  - Both K bounds check.
  - The uniform Cesàro bound comes from the β-free sequence u_*(max{X₀, h+λ_♯m−c₅}). This gives β/(K log L) → c₀/log L = 11/(3π²).
  - Torus: ℓL^{K−j} ≥ 2L¹¹MR_j, using x_j ≤ h+B_♯(1+n) and R_j ≤ L(log x_j)^r.

## 3. Order of constants and the c4-order cycle

**The cycle κ̄ → M → C₀^UM → Θ → κ̄ (c4-order lines 72–75, 90–91) is broken, conditionally on H-M.**
- Θ in (24) uses the fixed envelope C̄₀^UM=1. Its "3" is 1+2, which is UM18 (SA 14576–14578) with C₀=1. So Θ depends on κ and on row-2 constants only.
- K₀, A_{K₀}, ε₀, ρ₀, P and c_m are fixed in row 4, before κ. W₀ is M-free.
- ε_* and γ_tilt depend on M and are fixed in row 6.
- (23)'s first inequality is a floor on M after κ̄. It uses H₀, b and d, which H-M fixes before κ̄ and M.
- Its second inequality is a ceiling on the radii and tube after M.
- Hence C₀^UM ≤ 1 with no dependence back onto Θ.

H-M with constants fixed before κ̄ and M is exactly the input that c4-order row 8 flags and that um-envelope §5 assumes. in1 marks it Outstanding at line 108, which is correct (see F9).

**The other two cycles are also broken.**
- The flow cycle γ → (λ_♯, B_♯) → γ is cut. The weak triple is fixed in row 2. Every X₀ condition (Lemmas 5, 6, 8) uses λ̲, c₅ and B̄ only. ς, λ_♯ and B_♯ are computed after X₀ and are read only by Theorem 12's stopping rule and torus choice.
- The 2.8 cycle is cut: d₀ comes after L, r and B̄ (row 8).

**Every other dependence is ordered,** with three exceptions noted above: F6 (c_lin before c_G), F7 (volume cost in c₁) and F8 (floors not listed). In detail:
- E₀=E_N+1 → N_* comes after C_E and f_ν.
- c_G comes after A₁/A₀.
- c₁ comes after c, C_env, C_int and c_ent.
- X₀ comes after all of these.

Remark, not a finding. Row 1 drops c4-order's q−𝔭₀ > Cr (SA 19491, which serves "N_k s_k → 0"). It is implied:
- Enlarge C to ≥ 2. Then q > C𝔭₀ and 𝔭₀ > 3Cr give q−𝔭₀ > 𝔭₀ > Cr.
- With in1's N_k=R_k ≤ L(log θ)^r, the inequality q > 𝔭₀+2r alone gives N_ks_k → 0.

## 4. Imports and source readings

**Imports.** Each import is used only within the scope stated in its source note:
- H-M agrees with um-envelope (7) and §5. It is more general because it uses H_p(M) and C_τ|τ−1|. PR-lay supplies hypotheses (a)–(d) on 𝖠, including the global gap on every compression and the M-free H₁. These match Lemma 2's hypotheses, not the inverse-root identification. in1 says so.
- H-OL: b-value Theorem V gives c₀=(11/3π²)log L and |b[Ψ_k]−kc₀| ≤ c₂. Identification stays an import.
- H-SF agrees with SA RF20 (20683–20700) in both parts of the error. (12) is used only as stated.
- H-SUM agrees with SA OSF16 and the floor (19773–19804).
- H-O agrees with SA R25 (6291–6310).
- H-C cites SA 18287–18301 (A+GF ≥ cδ²) and 18303–18327 (Schur coercivity). YM3 Lemma I-10-97 (YM3 6862–6885) is three-dimensional ("L in the third direction"), as in1 says.
- H-G: SA 17719–17762 (count, ledger) and 18416–18715 (volume, entropy) read as cited.
- H-LF agrees in scope with c1-repr §§2–3.

**SA readings confirmed:**
- 5663–5755 (R4–R6: gauges, potentials, towers, strictness);
- 13904–14089 (FG1–FG11; FG6 has cost e^{A_K(ε+ρ)m}, independent of m and n);
- 14141–14205 (decoupled series r(s) ≠ 𝖠(s)^{−1/2}; the mutilated form need not have a gap);
- 14376–14399 (UM4–UM6);
- 19470–19493 (frame cut; exponent roles).

## 5. Verdict

Theorems 10, 11 and 12 hold as stated, conditional on H-M, H-OL, H-SF, H-LF, H-G, H-C, H-E, H-O and H-SUM, and on the order of constants. Lemmas 1–9 are correct hand proofs. The c4-order budget cycle is broken, conditionally on H-M, with constants fixed before κ̄ and M. That condition is exactly the input c4-order flagged. The eleven findings are definitions, a missing record, unlisted floors or constants, one omitted absorbed factor, and a citation. Each one has a direct repair. None changes a statement.

Checked line by line by Claude (fresh session).
