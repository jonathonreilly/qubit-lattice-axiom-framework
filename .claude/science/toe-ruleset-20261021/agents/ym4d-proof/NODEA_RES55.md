Reviewer model: claude-opus-5-5

# NODEA_RES55 — node A residual: (M1) effective-action lower bound, (M2) nonabelian Anderson-type correlation, n_♯ uniformity

## PRE-STATED (written 2026-10-29T00:29Z UTC, before any derivation; statements only)

Role: worker (Opus 5.5) under the shared brief REVIEW_BRIEF_55.md; its rules apply. Write scope: this
file and `$L/checks/nr55_*` only. No git. Append-only.

Targets.
- T1. State (M1) and (M2) precisely, with the quantifiers their consumer in NODEA55 (Part C / Part D:
  (ACT′) / (CEM^{COL})) actually needs, located by string in the file, not from the task summary.
- T2. (M2): try at least (a) a small-field log-concave perturbation of the Gaussian model
  (Brascamp–Lieb, Bakry–Émery, Holley–Stroock), (b) reflection positivity / chessboard or an FKG-type
  structure, (c) anything else; for each, list its hypotheses, whether the lane supplies them, and what
  constant it gives in place of 1.
- T3. (M1): find what RLARGE / PLD / HW already supply as an effective-action lower bound, and say
  exactly what is missing.
- T4. n_♯ uniformity of node A's moment constants for n_♯ strictly between 0 and the volume; check
  NODEA55's caution that c_f must be built from the input c_U, not from the output 2ε_2.
- T5. Before building on NODEA55's Gaussian-model proof, re-derive its load-bearing step
  (Prékopa–Leindler + Anderson ⇒ anti-correlation constant exactly 1; c_cem = (1−λ_f)^{−34992}).

What would count as a refutation (of NODEA55's claims or of mine).
- R1. A setting of the kind NODEA55 uses in which the claimed anti-correlation fails: for example, if the
  inequality needed is a Gaussian-correlation-type statement for multi-dimensional level sets, which
  Anderson's theorem alone does not give; or if it is invoked for a symmetric log-concave law that is not
  Gaussian, where correlation inequalities for symmetric convex sets fail in general.
- R2. The weight or constraint cores not being symmetric, or not quasi-concave, in the variables in which
  Anderson's theorem is applied.
- R3. The exponent 34992 or the base (1−λ_f) not matching the count or definition in the file.
- R4. For each (M2) route: a needed hypothesis (log-concavity after a change of variables, a curvature
  bound, a bounded perturbation whose oscillation the lane can pay for) that the lane cannot supply at
  its parameter values. The route is then reported as conditional, not as closing.
- R5. For n_♯: a moment constant whose n_♯-dependence is not uniformly bounded, or a c_f built from an
  output quantity, which would close a cycle in the SMALLNESS_DAG order.

Verdict vocabulary as in the brief: CONFIRMED / NOT-VERIFIED / REFUTED.

(PRE-STATED ends here. Everything below was written after it, from 2026-10-29T01:04Z.)

---

## 0. Inputs, the Codex review, and the checks

**Read (located by string; files as on disk at 00:30–00:50Z).** REVIEW_BRIEF_55.md (all). NODEA55.md (all 749 lines).
CODEX_REVIEW_NODEA.md (all 276 lines; it was 1 section at 00:30Z and complete — it ends with "Exactly what may be banked" —
when re-read at 00:48Z). PLD.md §18.7.2 ("Proposition SPLIT"), §19.1 ("Lemma READ"), §19.2 ("Lemma DLR", "Theorem W-FREE"),
§19.3 ("Lemma DOM", "Theorem AT"), §19.4–§19.5 ("(ACT)_k", "Lemma DOM′", "(LCR^act′)"), §19.6 ("Proposition TRADE",
"Theorem OUT"). HW.md §0, §4 ("Definition (tower energies)", "Lemma TE"), §6 ("Status of the remaining moment"), §13.1
("R_{S,E} :="), §21 ("Lemma TILT"), §22 ("Lemma FP", "Lemma NR", "Theorem LI^U-0", "Corollary LI-0"), §30.1 ("R-free"), §30.3,
§30.5 ("Corollary CRC-HW"), §30.6 ("Order of constants"), §38 ("[RHW5-fix SYM-1]") and grep hits for "B_0 :=". HIST.md §14.1
("Hypothesis (I_k^E)"), §25.6 ("(I_k^E)''"). RLARGE.md §4.1 and rows 10b/10c of §4.2. SMALLNESS_DAG.md §3.1 ("The n_♯ loop"),
§3.3, §7. RLARGE_U55.md header (not on this topic).
**Not read:** BFT_A/B, FLOW, SF, EXISTENCE, PROOF.md (no claim below rests on them).

**Codex verdicts used (CODEX_REVIEW_NODEA.md), and whether I agree** — each is also cited where used.
| Codex item (locating string) | Codex verdict | mine |
|---|---|---|
| §5 "Proposition GAUSS for exactly its stated Gaussian, uncapped-spectator, convex-core model" | CONFIRMED | **agree** (independent re-derivation, §1) |
| §5 "extension of this c_2 result to the actual cutoff constraint, capped spectators, or general log-concave perturbations" | NOT-VERIFIED | **agree, and sharpen**: for general symmetric log-concave laws and for the Gaussian model with the n = 1 allowance, c_2 = 1 is **false** (§3.2, §3.3); for capped spectators the *moment* bound survives with GAUSS's constant by a different proof (§3.1), c_2 = 1 itself stays NOT-VERIFIED |
| §5 "REFUTED — C.2(iv)'s explanatory claim that 'every factor … is quasi-concave'" | REFUTED | agree; nothing below uses C.2 (iv)'s necessity reading |
| §5 "C.1's product decomposition as a sufficient reduction" / "NOT-VERIFIED — actual-chain M1/M2" | CONFIRMED / NOT-VERIFIED | agree; and "C.4's moment of exp(λ_f a^col_A) is a sufficient strengthening of CEM-1^free's moment of Z_A" — agree, used in §2.3 |
| §2 "It does not prove CEM°, W0, or an O(1) moment as g → 0" (Lemma LT) | CONFIRMED with that limit | agree: NODEA55's "both … hold at fixed volume" (FOR THE LEAD item 3) must be read as "polynomial in u at fixed volume" |
| §2 "replace … 'reads levels ≤ k_0−1' by 'reads levels ≤ max{0,k_0−1}'" | correction | adopted in §2.2 |
| §4 "node A owes only Y = ∅ … It means CEM°_k for k ≥ 1 **and W0**" | CONFIRMED with qualification | adopted in §2.1 |
| §6 "use the input bound when choosing c_f and hence n_H" | CONFIRMED | **agree** (independent trace, §5.4) |
| §3 "θ ≤ 1/28" endpoint | REFUTED | not used (route (4°) runs at rate θ itself) |

**Checks run (criteria written and hashed before each script; Fractions for every verdict).**
| id | criteria (md5, time) | script (md5) | result |
|---|---|---|---|
| nr55_1 | checks/nr55_1_criteria.md (54cd0c07…, 00:59:06Z) | checks/nr55_1.py (52e0da9c…) → nr55_1_out.txt; 0.10 s, 16 MB, exit 0 | **G1–G4 PASS; all 7 controls fired** |
| nr55_2 | checks/nr55_2_criteria.md (50aaae25…, 01:00:17Z) | checks/nr55_2.py (9733d6c4…) → nr55_2_out.txt (4.7 s) and, with argument `second`, nr55_2b_out.txt (11.2 s); exit 0 | **G5a–G5d PASS at (τ, N) = (1/4, 8) and (1/8, 12); G5n fired** |
- *Could each gate fail?* G1: yes (its control, PLD's 52488-count, lands at 18190.95, outside the window). G2: yes (a = 1 gives
  Δ = 0; the s² = 4 certificate fails). G3: yes (the (1, 1) certificate fails; the grid control shows 3120 violations). G4: yes
  (the abelian control gives c3 = 0). G5b: yes — G5n (τ = 0) gives Q ≥ 0. **G5n2 fired only trivially** (the witness has no σ3
  component, so its abelian part is the zero vector): it carries no information and is not counted as a control.
  G5a is an exact identity check at every one of 336 (resp. 792) coordinates. G5d is a record. The float lines in nr55_1
  ("CONFIRMATORY") and the float search in nr55_2 decide nothing: every verdict is recomputed exactly from rounded rationals,
  and in G5b two independent exact code paths (assembled Hessian; direct ε²-coefficient) agree.
- *Criteria-file blemish (disclosed).* nr55_2_criteria.md's G5d line contains a self-correction ("— no: PASS iff …") written
  before the script; the operative criterion is the last one, |1 − w⁹|² > |1 − w|².

---

## 1. T5 — Proposition GAUSS re-derived: CONFIRMED for exactly its model

Source: NODEA55.md C.2, "Proposition GAUSS ((CEM°) in the linear-Gaussian, convex-core model)", steps (1)–(5).
**Load-bearing steps, re-derived.**
1. *Spectator absorption.* M_s := M − 2Σ_sQ_s ≥ M − λ_fΣ_sM_s ≥ (1 − λ_f)M using 2Q_s ≤ λ_fM_s (model DOM′) and
   Σ_sM_s ≤ M (disjoint term sets, (P-dis)); and M_s ≥ M_A + (1 − λ_f)Σ_sM_s ≥ M_A, so 2Q_A ≤ λ_fM_A ≤ λ_fM_s. ✓
2. *The tilt is a covariance change.* With Σ := M_s^{−1}, Σ′ := (M_s − 2Q_A)^{−1}:
   E_Σ[e^{xᵀQ_Ax}1_K] = (Z_{Σ′}/Z_Σ)·P_{Σ′}(K) and Z_{Σ′}/Z_Σ = E_Σ[e^{xᵀQ_Ax}] = det(I − 2Σ^{1/2}Q_AΣ^{1/2})^{−1/2}. ✓ (valid for ANY
   event K, which §3.3 uses).
3. *Anderson step.* Σ′ − Σ = Σ′(2Q_A)Σ ≥ 0, so a N(0, Σ′) vector is X + Y (independent, Y ~ N(0, Σ′ − Σ)); for fixed y,
   t ↦ P(X + ty ∈ K) is even (K = −K, X ~ −X) and log-concave (Prékopa: the marginal in t of the log-concave (x, t) ↦
   1_K(x)f(x − ty)), hence maximal at t = 0. So P_{Σ′}(K) ≤ P_Σ(K). ✓ **This is a covariance comparison, which Anderson's
   theorem gives directly; no Gaussian-correlation (Royen-type) inequality is needed** — so my pre-stated worry R1 does not
   apply to GAUSS.
4. *Determinant.* Eigenvalues of 2Σ^{1/2}Q_AΣ^{1/2} lie in [0, λ_f], at most r_A of them nonzero ⇒ ≤ (1 − λ_f)^{−r_A/2}. ✓
5. *Counts (check G1).* 4·8·9³ = 23328 links with both endpoints in the 9⁴-site block (Lemma READ (i)'s 𝔏_{k−1}(col_{k−1}Q));
   r_A ≤ 69984|A|; c_cem = (1 − λ_f)^{−34992}; 34992·ln 2 ∈ [24254.606142, 24254.606142] (rigorous enclosure), i.e. NODEA55's
   "log c_cem = 24254.6 at λ_f = ½" ✓. (PLD §19.5's "dof = 3n_int·81 = 52488" counts only links interior to the 81 cubes,
   23328 − 17496 = 5832 fewer; GAUSS's count is the one READ (i) supports. Recorded, not decided: it changes a constant, not a
   status.)
**Verdict: CONFIRMED** — for the model as stated (Gaussian; spectators *uncapped*, i.e. replaced by e^{q_s}; constraint
replaced by its convex core; positive-definite quotient), including c_2 = 1 for (CEM-2^all) **in that model**. Agreeing with
Codex §5, including its two cautions: (a) c_2 = 1 belongs to CEM-2^all (past constraint on the K side), and (b) λ_f should be
frozen at λ̄ := 24θ(1 + 2Rg_0²) for a g-uniform constant. **What GAUSS does NOT show** (and NODEA55 does not claim): anything
about capped spectators, non-Gaussian laws, or the cutoff allowance n ≥ 1 — §3 settles two of these negatively and one
positively.

*[Notation fix to §1 step 1, appended 01:12Z; §1 left as written.]* In "2Q_s ≤ λ_fM_s" and "Σ_sM_s ≤ M" the symbol M_s is
spectator s's **column part** (NODEA55's M_{Q″}); in "M_s := M − 2Σ_sQ_s" it is the **spectator-tilted precision** (NODEA55's
M_s). A symbol collision of my own making (systemic defect 1); the inequalities are exactly NODEA55 C.2 (1)'s.

---

## 2. T1 — the consumer, and (M1), (M2) stated with the quantifiers it needs

### 2.1 The consumer (route (4°), as Codex §4 confirmed it)
- **(CEM°)_k, k ≥ 1** (NODEA55 C.1, "(CEM°)_k [OPEN; owner node A]"): ∃ c_cem < ∞, c_A ≥ 0 such that for every g ≤ g_0, K, torus
  T, k ≥ 1, cutoff n ≥ 0, admissible 𝔥 (for n), R ∈ 𝔉_𝔥, finite set A of level-k cubes with [A ∩ A_k(𝔥) = ∅ or A = 𝒰_k] and
  N_8(col_{k−1}A) R-free, and F_< ∈ 𝔖^cap_𝔥(k_0) with k_0 ≤ k − 1, with ν := ν^{R,F_<}_{k−1}, w := h^{R,1}_{k−1}:
  E_{ν^w}[Z_A] ≤ c_cem^{|A|}e^{c_A‖col_{k−1}A‖_sh}, Z_A := Π_{Q∈A}e^{θY^f_Q}.
  Consumed by Corollary E2-RED° (C_fc := c_cem) inside Theorem CRC-2T° step (5°) and Corollary CRC-HW° (k ≥ 0).
- **(W0)** (NODEA55 B.3, "(W0)_λ [OPEN …]"), the level-0 clause, **kept as a separate clause** (Codex §4: "j ≥ k_0 (j = −1 …)
  does not literally include j = −1"), at the two rates θ (on {int Q : Q ∈ 𝒰_0}, F_< ≡ 1) and λ_f (on {𝔅_Q : Q ∈ Γ}, F_< a
  sub-product of Φ_{−1}).
- Throughout, freeze **λ̄ := 24θ(1 + 2Rg_0²) < 1** (Codex §5); λ_f = 24θ(1 + 2Rg_K²) ≤ λ̄ for g_K ≤ g_0.

### 2.2 A cutoff-free spectator class
**Definition (𝔖^cap_*(A; k_0)).** For a finite set A of level-k cubes and 0 ≤ k_0 ≤ k − 1: the products F_< = Π_{Q∈𝒬}F_Q over
finite sets 𝒬 of cubes, each a level-0 cube (F_Q = e^{θX_Q}) or a level-(i+1) cube with i ≤ max{0, k_0 − 1} (F_Q =
e^{θmin{π_Q, Y^f_Q}}) — the factors of NODEA55 A.1, read-levels as corrected by Codex §2 — such that the column term sets
T(Q) (the terms of 𝔞^col_Q, resp. the plaquettes of int Q) are pairwise disjoint and disjoint from T(A) := ∪_{Q∈A}T(Q).
**Lemma SPEC*: PROVEN-HERE (one line each).** (a) 𝔖^cap_𝔥(k_0) ⊂ 𝔖^cap_*(A; k_0) for every A satisfying the Γ-clause (that is
NODEA55 Lemma SPEC (P-dis), CONFIRMED by Codex §2). (b) Every member satisfies (P-lo) and (P-hi) (definition + PLD Lemma DOM′).
(c) The definition mentions no history, no admissibility clause and **no cutoff**. ∎
*Use.* Every statement about the unconstrained chain below is quantified over 𝔖^cap_*, so it is cutoff-free by construction
(§5.1); no falsifier is known on this class (LT (b)/F-UNIV need F_< outside the capped class; GAUSS, Lemma LT (a) and §3.1 hold
on all of it, since their proofs use only (P-lo), (P-hi), (P-dis)).

### 2.3 The statements
Fix a datum 𝔇 of (CEM°)_k. Let 𝔞 := 𝔞^col_A (PLD Lemma DOM′, "the minimised column action"; bounded, ≥ 0, and Z_A ≤ e^{λ_f𝔞}).
Let **μ_∅** := W·F_</norm on all levels (no constraint) and **μ_R** := μ_∅(·|R); by HW Lemma TILT (ii) (finer spectators
inserted), E_{ν^w}[f] = E_{μ_R}[f] for every bounded f of levels ≤ k − 1 (NODEA55 C.1 "The weight, removed exactly"). For
λ ∈ [0, λ̄]: μ_{∅,λ} ∝ e^{λ𝔞}μ_∅ and μ_{R,λ} ∝ e^{λ𝔞}μ_R = μ_{∅,λ}(·|R).

**(M1) — the unconstrained column moment.** ∃ c_1 (resp. B_1) < ∞ such that for every g ≤ g_0, K, T, k ≥ 1, finite A at level k
and **F_< ∈ 𝔖^cap_*(A; k − 1)** [no n, no 𝔥, no R]:
- (M1^exp) = NODEA55's (CEM-1^free): E_{μ_∅}[Z_A] ≤ c_1^{|A|};
- (M1^𝔞) [sufficient strengthening, Codex §5]: E_{μ_∅}[e^{λ̄𝔞}] ≤ c_1^{|A|};
- (M1^mean): E_{μ_{∅,λ̄}}[𝔞] ≤ B_1|A|.

**(M2) — the decoupling.** ∃ c_2 (resp. B_2) < ∞ such that for every datum 𝔇 of (CEM°)_k (**all** its quantifiers, n ≥ 0
included):
- (M2^exp) = NODEA55's (CEM-2^all): E_{μ_∅}[Z_A1_R] ≤ c_2^{|A|}E_{μ_∅}[Z_A]·μ_∅(R);
- (M2^𝔞): μ_{∅,λ̄}(R) ≤ c_2^{|A|}μ_∅(R), i.e. E_{μ_∅}[e^{λ̄𝔞}1_R] ≤ c_2^{|A|}E_{μ_∅}[e^{λ̄𝔞}]μ_∅(R);
- (M2^mean) [first-moment form]: E_{μ_{R,λ}}[𝔞] − E_{μ_{∅,λ}}[𝔞] ≤ B_2|A| for every λ ∈ [0, λ̄] —
  "conditioning on the constraint does not raise the tilted mean column action by more than B_2 per cube".

**(LCR°) — the single sufficient statement.** ∃ B < ∞, same quantifiers as (M2): **E_{μ_{R,λ̄}}[𝔞^col_A] ≤ B|A|.**
(This is PLD §19.5's (LCR^act′) with NODEA55's restrictions — F ≡ 1, F_< capped — written in the TILT form.)

**Level 0 (for (W0)).** The same three statements with 𝔞 replaced by 𝔴_𝒳 := u_0Σ_{X∈𝒳}Σ_{p∈𝒫(X)}s(U_0(p)), A by the region
family 𝒳, k − 1 by 0, and spectators of level-0 type only; call them (M1_0), (M2_0), (LCR°_0).

### 2.4 Lemma IMPL — how they combine: PROVEN-HERE
- **(i)** (M1^exp) + (M2^exp) ⇒ (CEM°) with c_cem = c_1c_2, c_A = 0 (NODEA55 C.1; Codex §5 CONFIRMED). (M1^𝔞) + (M2^𝔞) ⇒ (CEM°)
  likewise: E_{ν^w}[Z_A] = E_{μ_R}[Z_A] ≤ E_{μ_R}[e^{λ̄𝔞}] = E_{μ_∅}[e^{λ̄𝔞}1_R]/μ_∅(R) ≤ c_2^{|A|}E_{μ_∅}[e^{λ̄𝔞}] ≤ (c_1c_2)^{|A|}.
- **(ii)** λ ↦ E_{μ_{∅,λ}}[𝔞] and λ ↦ E_{μ_{R,λ}}[𝔞] are nondecreasing (derivative = variance; 𝔞 bounded). Hence (M1^mean) and
  (LCR°) stated at λ̄ hold at every λ ≤ λ̄, and by Theorem AT's identity (PLD §19.5: "log(E_{ν^G}[e^{λ_f𝔞^col_S}]) =
  ∫_0^{λ_f}E_{λ,G}[𝔞^col_S]dλ") **(M1^mean) ⇒ (M1^𝔞) with c_1 = e^{λ̄B_1}** and **(LCR°) ⇒ (CEM°) with c_cem = e^{λ̄B}, c_A = 0**.
- **(iii)** d/dλ log μ_{∅,λ}(R) = E_{μ_{R,λ}}[𝔞] − E_{μ_{∅,λ}}[𝔞] (differentiate log E_{μ_∅}[e^{λ𝔞}1_R] − log E_{μ_∅}[e^{λ𝔞}]); integrating
  over [0, λ̄]: **(M2^mean) ⇒ (M2^𝔞) with c_2 = e^{λ̄B_2}**.
- **(iv)** (M1^mean) + (M2^mean) ⇒ (LCR°) with B = B_1 + B_2; and (LCR°) ⇒ (M2^mean) with B_2 = B (because E_{μ_{∅,λ}}[𝔞] ≥ 0).
  (LCR°) does not imply (M1) (a constrained statement says nothing about the unconstrained chain).
**Reading.** (LCR°) is *weaker* than (M1) + (M2) and is sufficient for the consumer; **the split into (M1) and (M2) is optional,
not forced**. It is useful only if (M2) has a cheap proof (a correlation inequality). §3 shows that, beyond the Gaussian model,
it does not: the constant-1 correlation fails, and the robust tool proves (LCR°) directly instead.

*[Timestamp correction, appended 01:09Z: the "Notation fix to §1 step 1" above says "appended 01:12Z"; the actual append time
was ≈01:08Z (`date -u` printed 01:08:38Z right after that append). Nothing else is affected.]*

---

## 3. T2 — (M2): the routes, what each needs, and what the lane supplies

### 3.1 Theorem BL-TILT — the perturbation-stable replacement for the Anderson step: PROVEN-HERE (given Brascamp–Lieb)
**Statement.** Let K ⊂ R^D be closed and convex with nonempty interior; H > 0 a symmetric matrix; W: R^D → R ∪ {+∞} lower
semicontinuous with **W − ½xᵀHx convex** ("W is H-convex"); ν(dx) := Z^{−1}e^{−W(x)}1_K(x)dx a probability measure. Let
𝔞: R^D → [0, ∞) be measurable and Q ≥ 0 symmetric with
- (D1) 𝔞(x) ≤ xᵀQx on K;  (D2) x ↦ xᵀQx − 𝔞(x) convex on K (𝔞 is Q-semiconcave; trivially true if 𝔞 = xᵀQx);
- (D3) λ̄c̄ < 1, where c̄ := the top eigenvalue of B := H^{−1/2}(2Q)H^{−1/2};
- (D4) for every t ∈ [0, λ̄] the tilted law ν_t ∝ e^{t𝔞}ν has mean 0 (e.g. W, K, 𝔞 even; or all invariant under a linear group
  action on R^D with no nonzero fixed vector).
Then for t ∈ [0, λ̄], **E_{ν_t}[𝔞] ≤ ½tr(B(I − tB)^{−1})**, and
  **E_ν[e^{λ̄𝔞}] ≤ det(I − λ̄B)^{−1/2} ≤ (1 − λ̄c̄)^{−rank(Q)/2}.**
*Proof.* (0) W ≥ ½xᵀHx + (affine) (a proper lsc convex function has an affine minorant), and t𝔞 ≤ txᵀQx with H − 2tQ ≥
(1 − λ̄c̄)H > 0, so every quantity below is finite and t ↦ log E_ν[e^{t𝔞}] is differentiable with derivative E_{ν_t}[𝔞]
(dominated convergence). (1) ν_t ∝ e^{−V_t}1_K with V_t := W − t𝔞, and V_t − ½xᵀ(H − 2tQ)x = (W − ½xᵀHx) + t(xᵀQx − 𝔞) is
convex on K by H-convexity and (D2): **ν_t is (H − 2tQ)-strongly log-concave on a convex set.** (2) Brascamp–Lieb [BL]: for a
probability measure e^{−V}1_K dx with V − ½xᵀH′x convex, Var(⟨v, x⟩) ≤ vᵀH′^{−1}v, i.e. **Cov ≤ H′^{−1}**. [BL is stated for
C² strictly convex V on R^D; the extension to H′-convex V restricted to a convex K is by approximation: V_j := (V + j·dist(·, K)²)
mollified is smooth and H′-convex, e^{−V_j} → e^{−V}1_K pointwise a.e. with a common Gaussian majorant, so covariances converge
— this approximation is the one step a reviewer should check.] (3) By (D1), (D4), Q ≥ 0 and (2):
E_{ν_t}[𝔞] ≤ E_{ν_t}[xᵀQx] = tr(Q·Cov_{ν_t}) ≤ tr(Q(H − 2tQ)^{−1}) = ½tr(B(I − tB)^{−1}). (4) Integrate over t ∈ [0, λ̄]:
∫_0^{λ̄}½Σ_ib_i/(1 − tb_i)dt = −½Σ_ilog(1 − λ̄b_i), and b_i ∈ [0, c̄], at most rank(Q) of them nonzero. ∎
[BL] H. J. Brascamp, E. H. Lieb, J. Funct. Anal. 22 (1976) 366–389, Thm 4.1 [m: from memory, not re-read].

**Corollary BL-1 (the convex-core models, capped spectators included): PROVEN-HERE (given [BL]).** In NODEA55's linear model
(positive-definite quotient, convex core K, model DOM′ 2Q_𝔞 ≤ M_A for the minimised column form 𝔞 = xᵀQ_𝔞x):
- uncapped spectators: W = ½xᵀM_sx (M_s the spectator-tilted precision), H = M_s;
- **capped spectators** F_s = e^{min{θπ_s, q_s(x)}}: W = ½xᵀMx − Σ_smin{θπ_s, q_s} = ½xᵀM_sx + Σ_s(q_s − θπ_s)^+, and each
  (q_s − θπ_s)^+ is convex (positive part of a convex function), so W is M_s-convex and even;
in both cases B ≤ I (2Q_𝔞 ≤ M_A ≤ M_s), hence **E_{μ_R}[e^{λ̄𝔞}] ≤ (1 − λ̄)^{−r_A/2}, r_A ≤ 69984|A|: (CEM°) with c_cem =
(1 − λ̄)^{−34992}, c_A = 0 — GAUSS's constant — with no Anderson step, no split, and for capped spectators**, which GAUSS
(by Codex §5) does not cover. In §2's terms the model satisfies (LCR°) with B = 34992/(1 − λ̄) (step (3) at t = λ̄).
**Corollary BL-2 (what B-L buys structurally).** The constraint enters only through **convexity of K**; no correlation
inequality, no x ↦ −x symmetry (only (D4)), no decay of correlations; the bound depends only on rank Q and c̄, so it is
**volume-uniform for free**. And it re-derives GAUSS's own Anderson comparison: for a Gaussian conditioned on a symmetric convex
K, Cov(X | K) ≤ Σ by [BL], and the Gaussian interpolation identity d/ds log P_{Σ+sΔ}(K) = ½(E[X̃ᵀΔ̃X̃ | K] − E[X̃ᵀΔ̃X̃])
(X̃ := Σ_s^{−1}X, Δ̃ := Δ; a derivative-free integration by parts) is then ≤ 0. So in the log-concave class **(M2) is moot**:
(LCR°) holds directly.
**Corollary BL-3 (beyond Gaussian).** Any W = ½xᵀM_sx + V with V convex and even (or color-invariant) gives the same constant;
if V is only δ-semiconvex (V + ½δxᵀM_sx convex, δ < 1 − λ̄), take H = (1 − δ)M_s: c̄ ≤ 1/(1 − δ), constant
(1 − λ̄/(1 − δ))^{−r_A/2}.

### 3.2 Proposition NO-ONE (i): the anti-correlation constant 1 fails beyond the Gaussian: PROVEN-HERE (check G2)
On R², let D := {|x_1| + |x_2| ≤ 1}, μ ∝ e^{−|x|²/18}1_D (even; W = |x|²/18 + ι_D is (I/9)-convex), K := {|x_2| ≤ ½}
(symmetric convex), μ_t ∝ e^{tx_1²}μ. Then (d/dt)log μ_t(K)|_{t=0} = E_μ[x_1² | K] − E_μ[x_1²] **> 0**, so **μ_t(K) > μ(K)** for
all small t > 0 — while the tilt satisfies 2Q = diag(2t, 0) ≤ λ̄·(I/9) for t ≤ λ̄/18.
*Proof (exact, G2).* With uniform weights: ∫∫_D1 = 2, ∫∫_Dx_1² = 1/3, ∫∫_{D∩K}1 = 3/2, ∫∫_{D∩K}x_1² = 5/16, so the uniform
conditional means are 5/24 against 1/6. On D, |x|² ≤ 1, so the weight e^{−|x|²/18} lies in [e^{−1/18}, 1], and the derivative is
≥ e^{−1/18}·5/24 − e^{1/18}·1/6 > 0 because e^{1/9} ≤ 1 + 1/9 + 1/81 = 91/81 < 5/4 (e^x − 1 − x ≤ x²(e − 2) on [0, 1]). ∎
(Controls: a = 1 gives Δ = 0; at s² = 4 the certificate fails, 41/192 > 5/24.)
*Reading.* Every hypothesis GAUSS's mechanism names — even, strongly log-concave, symmetric convex constraint, dominated quadratic
tilt on variables disjoint from the constrained ones — holds, and still the tilt **raises** the constraint's probability: the
law's negative dependence (the diamond) beats symmetry. BL-TILT's moment bound (1 − 18t)^{−1/2} holds in the same example. **So
"Anderson/Prékopa survive the perturbation with anti-correlation constant 1 + O(small)" cannot be derived from symmetry and
log-concavity: the constant 1 is a Gaussian (convolution) fact.** A volume-uniform 1 + O(small) would additionally need a
quantitative decoupling (per-site losses summable over the volume) — the content (M2) was supposed to avoid.

### 3.3 Proposition NO-ONE (ii): the constant 1 fails in the Gaussian model once the cutoff allows one defect: PROVEN-HERE (G3)
Take two *-adjacent constrained cubes x, y with defect functionals ℓ_x = g + h, ℓ_y = g − h, (g, h) ~ N(0, diag(1, σ_0²)),
threshold ε, and n = 1, so R_1 = {not both defective}. Tilt by e^{th²} (h ~ N(0, σ_0′²), σ_0′² = σ_0²/(1 − 2tσ_0²)).
**Claim.** If 0 < σ_0 < σ_0′ ≤ σ_*(ε), σ_*² := ε²/(4ε² + 2 ln 2), then **E[e^{th²}1_{R_1}] > E[e^{th²}]·P(R_1)**. Example: ε = 1,
σ_0 = 1/8, t = 8 (σ_0′² = 1/48; the domination 2Q ≤ ½M holds: 16 ≤ 32). So c_2 = 1 fails in the linear-Gaussian model as soon
as n ≥ 1 — the model's c_2 = 1 is special to the convex core n = 0.
*Proof.* By §1 step 2 (valid for any event), the ratio equals P_{σ_0′}(R_1)/P_{σ_0}(R_1), so it suffices that P_σ(B) — B := both
defective — is strictly decreasing in σ on (0, σ_*]. Write P_σ(B) = E[φ(σZ)], φ(h) := P_g(|g + h| ≥ ε, |g − h| ≥ ε). For |h| < ε,
B ⟺ |g| ≥ ε + |h| (G3g, exact grid; control shows 3120 violations of the naive form), so φ(h) = 2Φ̄(ε + |h|), φ′ = −2ϕ(ε + h) on
(0, ε); for h > ε, φ(h) = 1 − 2[Φ(h + ε) − Φ(h − ε)], φ′ = 2[ϕ(h − ε) − ϕ(h + ε)] ∈ (0, 2ϕ(0)]. φ is Lipschitz, so
d/dσ E[φ(σZ)] = 2∫_0^∞zφ′(σz)ϕ(z)dz ≤ 4[−ϕ(2ε)(ϕ(0) − ϕ(ε/σ)) + ϕ(0)ϕ(ε/σ)], which is < 0 iff
e^{−2ε²} > e^{−ε²/(2σ²)}(1 + e^{−2ε²}); this holds for σ ≤ σ_*. At (1, 1/4) it is certified exactly (G3: e^{−6}(1 + e^{−2}) ≤ 6/125
< 1); at (1, 1) it fails (control). ∎ (Float quadrature, CONFIRMATORY only: P(B) = 0.28111 at σ = 0.10, 0.26478 at σ = 0.15.)
*Reading.* The tilt de-correlates two adjacent defect functionals; with the allowance "one defect, not two", de-correlation helps
the constraint. This is the corner of the non-convex R_1 (Codex §5's (4,0), (0,4) vs (2,2)) acting with a definite sign. Note
σ_* ≈ 1/2 for ε ≫ 1, so the mechanism survives in the rare-defect regime that matters. It does not refute (M2) with SOME
c_2 > 1; it shows that **the intermediate-cutoff case needs a quantitative argument even in the Gaussian model** (§5.3).

### 3.4 Route (a) for the nonabelian chain: BL-TILT's hypotheses, one by one
| hypothesis | real chain | supplied by the lane? |
|---|---|---|
| Anderson's central symmetry x ↦ −x (GAUSS's route) | **fails** in the exponential chart at the identity: the cubic vertex, exact (G4: [t³](tr U(t) − tr U(−t)) = −4 for X = (iσ1, iσ2, iσ3, 0); abelian control 0). A nonlinear (Morse-type) chart can move the cubic term into the Haar Jacobian and the shapes of the constraint sets, but no chart is known in which measure, constraint core and column functional are simultaneously centrally symmetric | **not supplied — and not needed by B-L** |
| (D4) mean zero | **holds**: the chain, the constraints, the spectators and 𝔞 are invariant under global conjugation U_ℓ ↦ hU_ℓh^{−1} on every link of every level (gauge-covariant kernels and centres, conjugation-invariant traces; HW §0); in a conjugation-equivariant chart (exponential coordinates, a conjugation-stable gauge slice such as an axial tree) the group acts by Ad on each link coordinate, which has no nonzero fixed vector in su(N); so every tilted law has mean 0 (PROVEN-HERE, elementary) | **yes** |
| H-convexity of the chain potential, with the column tilt dominated (D1)–(D3) | **fails on the single-level small-field set**: exact witness G5 — at the uniform-field background (plaquette norm 0.485, resp. 0.248; a critical point, G5a) the Wilson Hessian has Rayleigh quotient **−1.0727** (resp. **−0.5247**) on a 2D patch, while the free Hessian is +2.23 (+2.08) on the same vector; the negative value scales ≈ −2α with the field angle α (Nielsen–Olesen / Atiyah–Bott mechanism [m]). Extrapolation to plaquettes below the lane's ε_1 on patches of size ≍ α^{−1/2}: **ARGUED** (scaling). The witnesses are coarse-level defects (G5d: |1 − w⁹|² = 2.60, 3.24): **on the multiscale small-field core** (no defect at any level) the curvature seen by a mode of size ℓ is ≲ ε_1/ℓ² against a free Hessian ≍ 1/ℓ², so H-convexity with δ = O(ε_1) is **ARGUED** to hold there | **no**: (I_k^E)″ is a HYPOTHESIS (HIST §25.6; Theorem A5 ARGUED, "(R♯) OPEN") and is stated with sup-norm polymer bounds, not C² bounds dominated by the main term |
| convexity of the constraint core in the chart | {‖1 − U_P‖ < ε_1} is a slab only to first order in exponential coordinates; convex up to a relative O(ε_1) curvature | **no** |
| support in the core | the column is R-free at levels ≥ k and the cutoff allows defect clusters: the tilted constrained law has mass off the core, where B-L does not apply | **no**: needs a large-field (Peierls-type) bound under the tilted constrained law — (SDP)-type content, §5.3 |
**Holley–Stroock** [m] (bounded perturbation e^{−V}, osc V ≤ ω): changes the (M2) ratio by at most e^{2ω} and B-L/LSI constants by
e^{ω}; the chain's non-Gaussian part is extensive (osc V ∝ volume), and localising it by DLR conditioning reintroduces a
boundary condition, for which the conditional moment is **not** uniformly bounded (F-UNIV, CONFIRMED by Codex §1). **Not a
volume-uniform tool here.** **Bakry–Émery on SU(N)^links** [m]: Ric(SU(N)) = O(1), while the Hessian of u·S has negative
directions of size ≍ u·α (G5); at u ≍ 10⁹⁴ this is a strong-coupling tool only (as in the stochastic-quantisation literature
[m: Shen–Zhu–Zhu, CMP 2023]). **Not available at weak coupling.**
**The precise missing hypothesis of route (a): (LC°)_k [OPEN].** There are δ < 1 − λ̄ and C_LF < ∞ such that, for every datum
of (CEM°)_k: (LC-1) on the multiscale small-field core 𝒮 (no defect at any level within a fixed neighbourhood of region(A)
and of the constrained cubes) there is a conjugation-equivariant gauge-fixed chart in which the potential of μ_{R,λ}|_𝒮 is
H-convex with H ≥ (1 − δ)·(the linear model's M_s), and 𝔞 satisfies (D1)–(D2) with 2Q ≤ M_A (the C² form of PLD §18.7.2 (a)'s
main-term reduction); (LC-2) the image of 𝒮 ∩ R is convex (or replaced by a convex set at a relative cost ≤ e^{C|A|});
(LC-3) E_{μ_{R,λ}}[𝔞; 𝒮^c] ≤ C_LF|A| for λ ∈ [0, λ̄], uniformly in volume and cutoff. **Then (LCR°), hence (CEM°), holds with
log c_cem ≤ 34992·log(1/(1 − λ̄/(1 − δ))) + λ̄C_LF** (BL-TILT on 𝒮, conditioning and tilting commute; (LC-3) for the rest).
(LC-1)–(LC-2) are the convexity half of a Balaban-type small-field analysis; (LC-3) is the large-field half. **This
re-factorises node A's residual by mechanism (convexity / large field) instead of by measure (unconstrained / constrained);
the first factorisation has a known proof technology for each piece, the second (§3.2–§3.3) does not have one for (M2).**

### 3.5 Route (b): reflection positivity / chessboard, FKG — NOT AVAILABLE for (M2)
- **Chessboard** (Osterwalder–Seiler RP of the Wilson action + Fröhlich–Israel–Lieb–Simon [m]; NODEA55 C.3, ARGUED there).
  (1) It bounds expectations of products from **above**; (M2) is a ratio whose denominator μ_∅(R) needs a matching **lower**
  bound, which chessboard does not give. (2) 1_R (a history-dependent pattern of per-cube indicators, plus the cutoff
  clause) and w are not products of reflected copies of one block function. (3) **New:** even (M1_0) — the plain Wilson
  window moment — is reached only at **F_< ≡ 1**: with spectators (needed by (0b°), F_< a sub-product of Φ_{−1}) the
  numerator is ≤ Π_X C(λ)·Π_{Q″}C(θ) while the denominator E[F_<] is only ≥ 1 (P-lo), so the spectators cost C(θ)^{|𝒬|},
  not bounded by c^{|𝒳|} (Jensen's lower bound e^{θΣE[u_0S_{Q″}]} does not match C(θ) per factor). So chessboard gives at most
  the (0a) half of (W0)'s plain-measure part, modulo NODEA55's global zero-mode factor.
- **FKG / Griffiths / Ginibre.** SU(N) link configurations carry no lattice order in which both the column energy and the
  small-field indicators are monotone; Ginibre-type correlation inequalities are abelian (U(1), Z_N) [m]. The lane has none.

### 3.6 Route (c): what else, and where each leads
- **(c1) Prove (LCR°) directly** (§2.3): no correlation inequality is needed; in the convex class it is BL-TILT; for the chain
  it is (LC°). Recommended target.
- **(c2) One-level convexity inside PLD's DLR.** Given U_{k−2} the column links are independent kernels (PLD Lemma DLR (iii)),
  each (κu_{k−2}r)-convex near its centre (φ_M(V) = r(1 − cos α) for SU(2), Codex §2), and 𝔞 is an infimum of functions with
  Hessian ≤ κu_{k−2}(1 + O(ε)) (semiconcave). So BL-TILT applied to the **conditional** law gives PLD's (EQ-bc) (Theorem OUT) on
  the small-field part, with charge = the forced action of the centres [ARGUED, not written in full] — and leaves (BCH-1), one
  level down. Iterating level by level loses rate (a one-level Gaussian computation gives the bound ζ ≤ (1 − λ)^{−dof/2}
  e^{(λ/(1−λ))𝔞(centres)}, rate λ ↦ λ/(1 − λ) per level — HW's failure mode (HW-F5)); a k-uniform constant needs the global
  convexity (LC-1), not iterated conditioning.
- **(c3) The cutoff in the Gaussian model** — §5.3.

*[Correction to §3.4's (LC°), appended 01:16Z; the text above is left as written.]* As written, (LC-1) asks the law on 𝒮 to
be H-convex **globally**, and 𝒮 excludes defects near *every* constrained cube. In large volume the unconstrained history
regions far from A still carry large fields, so the conditional law on 𝒮 is not convex there, and if 𝒮 is enlarged to exclude
them, μ_{R,λ}(𝒮^c) → 1 with the volume and (LC-3) becomes the whole problem. **The operative form is conditional:**
- **(LC-1′)** For every region Ω and every boundary datum on a fixed collar of ∂Ω that is itself small-field, the chain on Ω
  conditioned on "no defect at any level in Ω" is H_Ω-convex in a gauge-fixed chart, with H_Ω ≥ (1 − δ)·(the linear model's
  precision on Ω), uniformly in Ω and the datum, and 𝔞 satisfies (D1)–(D2) there (the mean is now the boundary-forced
  configuration, so BL-TILT's (D4) is replaced by the forced term: E[𝔞 | datum] ≤ ½tr(B(I − λB)^{−1}) + 𝔞^{forced}(datum)).
- **(LC-2′)** as (LC-2), on Ω.
- **(LC-3′)** Disintegrating μ_{R,λ} over the large-field configuration (the defective cubes at all levels, the unconstrained
  cubes, a collar, and the fields there): E_{μ_{R,λ}}[𝔞^{forced}] ≤ C_LF|A| — a Peierls bound for the large-field set under the
  tilted constrained law, combined with the decay of the forcing with distance (a cluster at level-(k−1) distance r forces
  column action ≲ (its action)·Infl(r)², with Infl(r)² ≍ r^{−8} in the linear model — NODEA55 C.2 (v)'s power count,
  summable against r³; ARGUED).
(LC-1′) + (LC-2′) + (LC-3′) ⇒ (LCR°) with B ≤ 34992/(1 − λ̄/(1 − δ)) + C_LF by BL-TILT applied conditionally. This is the
Balaban small-field/large-field structure; the lane has none of the three as a theorem (§4).

---

## 4. T3 — (M1), the effective-action bound: what the lane has, and what is missing

| item (file, locating string) | status as filed | what it gives toward (M1) / (LCR°) |
|---|---|---|
| Lemma DOM′ (PLD §19.5, "Lemma DOM′ (the repair; the minimised column action)") | PROVEN-HERE (PLD); λ_f's factor 1 + 2Rg_K² CONFIRMED by Codex §7 row 7 | pointwise Z_A ≤ e^{λ_f𝔞}; 𝔞 not extensive. The trade in the right currency |
| Theorem AT (PLD §19.3; "survives verbatim with 𝔄^col_S replaced by 𝔞^col_S", §19.5) | PROVEN-HERE (PLD) (an identity) | moment = ∫ of the tilted mean; with §2.4 (ii) a single rate λ̄ suffices |
| Lemma DLR / Theorem W-FREE (PLD §19.2) | PROVEN-HERE (PLD); **as filed, not re-derived here** | exact reduction of the column moment to ζ(U_{k−2}), an explicit product functional one level down |
| (M-i) single-link kernel moment (HW §22, "Corollary LI-0 … (M-i) under μ_{R(𝔥)} is PROVEN for SU(2) with C_mis = (1 − λ)^{-3/2}") | PROVEN (HW) | the top (one-link) term of the column action, exactly |
| HW §6 "Reduction to the main term (PROVEN-HERE given (I_k^E)(a)'s localisation; uncounted)" | conditional on (I^E)(a) | F^col_Q ≤ Σ_{x under Q}𝓔_{k,x}: moves the moment onto the effective action's main term |
| HW §6 "a **local coupling response** of the small-field package … [ARGUED: it needs node A's cluster expansion with an inhomogeneous coupling, and GAP S2-1 …]" | ARGUED | the (M1) mechanism itself, ≈ (1 − λ)^{−dof/2}e^{O(E_0)|A|} |
| (I_k^E)″ (HIST §25.6, "(I_k^E)'' (restated hypothesis) [HYPOTHESIS, P]"); RLARGE §4.1 "Theorem A5 is ARGUED … (R♯) OPEN" | HYPOTHESIS | the effective action: main term u_k𝓔^{an}_k, polymers with Σ_{X∋x}sup|E_k(X) − E_k(X;1)|e^{κ_pd(X)} ≤ E_0 per cube — **sup-norm on a complex domain; E_0 "bounded but NOT small"** |
| PLD §18.7.2 (a) "the main-term reduction OFF G_Q … **Nothing in PLD §16-§17 or HW §6 writes this**" (re-instated by §19.5: "§18.7.2's ingredient (a) IS needed") | NOT WRITTEN | the off-small-field half of (M1) |
| PLD §18.7.2 (b)–(c) / §17.5: activity bounds uniform in u on [(1 − λ_f)u, u] "do not state" | NOT STATED | the coupling-response half |
| RLARGE row 10c "(SF-cap)^A_θ, rate 24θ(1 + 2Rg_K²) < 1" | OPEN | (M1)'s small-field half in the older language |
| NODEA55 Lemma LT (a) | PROVEN-HERE; Codex §2: "does not prove CEM°, W0, or an O(1) moment as g → 0" | polynomial in u at fixed volume, every cutoff — **not** (M1) |
| NODEA55 GAUSS; this file's Cor. BL-1 | PROVEN (model) | (M1) and (LCR°) in the linear model, with capped spectators (BL-1) |
| NODEA55 C.3 chessboard (plain Wilson, level 0) | ARGUED (global zero-mode factor) | (M1_0) at F_< ≡ 1 only (§3.5 (3)); HW §6: "(M-f) at level 0 … OPEN as stated even for the plain Wilson measure" |

**What is missing for (M1), precisely.** A bound on the tilted mean column action of the **unconstrained** chain,
E_{μ^{F_<}_{∅,λ̄}}[𝔞^col_A] ≤ B_1|A| (equivalently, by Lemma IMPL (ii), the moment E_{μ_∅}[e^{λ̄𝔞}] ≤ e^{λ̄B_1|A|}), uniform in g ≤ g_0,
K, T, k, A and F_< ∈ 𝔖^cap_*. Through the lane's own objects it would follow from: (I^E)″ restated with **C² polymer bounds
dominated by the main term** (so that the level-(k−1) effective density is (1 − δ)-convex on small-field regions), the
**main-term reduction off G_Q in C² form** ((D1)–(D2) for 𝔞 against the main term), and a **large-field bound** for the
unconstrained chain — i.e. (LC-1′)–(LC-3′) with R = ∅. None is proven.
**A structural remark against the split.** The unconstrained chain has no small-field constraint anywhere, so its large-field
part (LC-3′ at R = ∅) must control defects that the constraint would have excluded; (M1) is therefore at least as hard as
(LCR°)'s large-field part, and gains nothing from being unconstrained. With (M2) offering no correlation-inequality shortcut
(§3.2–§3.3), **the split (M1) + (M2) is a worse factorisation than (LCR°) ⟸ (LC°)**: aim node A at (LCR°) directly.
**Level-by-level does not close it** (§3.6 (c2)): DLR + one-level convexity reaches (EQ-bc) with a forced charge and leaves
(BCH-1); iterating the one-level bound degrades the rate (λ ↦ λ/(1 − λ) per level as a bound), which is HW's (HW-F5).

---

## 5. T4 — uniformity in the cutoff n_♯

### 5.1 (M1) is cutoff-free by construction: PROVEN-HERE
(M1) concerns μ_∅ (no constraint, so no n) with F_< ranging over 𝔖^cap_*(A; k − 1), whose definition mentions no cutoff
(Lemma SPEC* (c)); every consumer's spectator lies in it (SPEC* (a) with NODEA55 A.2, CONFIRMED by Codex §2). So c_1 (and B_1),
if they exist, are independent of n by the form of the statement. NODEA55 Part D (b)'s "every restated statement is uniform over
𝒬" is thereby made exact for the unconstrained half.

### 5.2 Where n enters: only through 1_{R_n}, in (M2) / (LCR°)
- **n = 0 (convex core).** Linear model: GAUSS (Anderson, uncapped spectators) and Cor. BL-1 (B-L, capped spectators too):
  **PROVEN**, same constant. Real chain: (LC°) with no allowed clusters in constrained cubes — still needs (LC-3′) for the
  unconstrained regions.
- **n ≥ (number of constrained cubes at each level).** 1_{R_n} ≡ 1, so (LCR°) = (M1^mean): in the model, BL-1 with K = R^D.
  **PROVEN** (model).
- **1 ≤ n < volume.** R_n is a union of convex sets, not convex: BL-TILT does not apply, and **NO-ONE (ii) shows the model's
  c_2 = 1 fails** (a strict increase P_{Σ′}(R_1) > P_Σ(R_1)). NODEA55 Part D's model row ("YES at n = 0 and at n ≥ (number of
  cubes): PROVEN; 1 ≤ n < volume: ARGUED") is **CONFIRMED** as stated; its C.2 (v) prediction "c_2 = 1 + o(1) uniformly in n"
  stays **NOT-VERIFIED** (now known not to be exactly 1).

### 5.3 Proposition NU — cutoff uniformity is automatic for per-defect bounds: PROVEN-HERE (implication)
For a configuration let 𝒟(U) be the set of defective constrained (level, cube) pairs, and for a finite set D let F_D :=
{𝒟(U) = D}. Fix every datum of (CEM°)_k except n. Suppose there are c, b < ∞ and functions ρ_A(x), η(x) ≥ 0 of the pair x and
of A only, such that
- **(NU-i) [per-defect multiplier]** E_{μ_∅}[e^{λ̄𝔞} | F_D] ≤ c^{|A|}Π_{x∈D}(1 + ρ_A(x)) for every D with μ_∅(F_D) > 0;
- **(NU-ii) [constrained Peierls bound]** μ_{R_n}(Y ⊂ 𝒟(U)) ≤ Π_{x∈Y}η(x) for every finite Y;
- **(NU-iii)** Σ_xρ_A(x)η(x) ≤ b|A|.
Then **E_{μ_{R_n}}[e^{λ̄𝔞}] ≤ (ce^b)^{|A|}**, hence (CEM°) with c_cem = ce^b, c_A = 0, for that n.
*Proof.* The sets F_D, D ∈ 𝒜_n (components ≤ n), partition R_n, and μ_{R_n}(·|F_D) = μ_∅(·|F_D) for such D (F_D ⊂ R_n). So
E_{μ_{R_n}}[e^{λ̄𝔞}] = Σ_{D∈𝒜_n}μ_{R_n}(F_D)E_{μ_∅}[e^{λ̄𝔞}|F_D] ≤ c^{|A|}E_{μ_{R_n}}[Π_{x∈𝒟(U)}(1 + ρ_A(x))]
= c^{|A|}Σ_YΠ_{x∈Y}ρ_A(x)·μ_{R_n}(Y ⊂ 𝒟(U)) ≤ c^{|A|}Π_x(1 + ρ_A(x)η(x)) ≤ c^{|A|}e^{b|A|}. ∎
**Reading.** (NU-i) and (NU-iii) do not involve n at all; **the only place the cutoff can enter node A's constant is the
constrained Peierls bound (NU-ii)**. So SMALLNESS_DAG §3.1's "[inference] a per-cube gas bound … is naturally cutoff-uniform"
is right, and is now a proven implication: n-uniformity ⟸ (NU-ii) with n-free activities. What would destroy it is any bound
that counts allowed clusters by their size (a 6400^{n}-type entropy factor) inside node A.
**Consequences.**
- *Where (SDP)-type content re-enters.* Route (4°) removed (SDP)^A from the HW–node-A interface (NODEA55 B.2, Codex §4). Node A's
  own proof of (CEM°) for n ≥ 1 still needs a defect-probability bound under the constrained law — (NU-ii) here, (LC-3′) in
  §3.4. Not a new obligation of HW's; a named obligation of node A's.
- *In the linear model.* (NU-i) is a Gaussian-conditioning computation (given the defect values the field is Gaussian with a
  mean linear in them; ρ_A(x) is governed by λ̄·Infl(x, A)²·(defect size)², against η(x) ≍ e^{−ε²/(2σ_x²)}) [ARGUED]. For (NU-ii),
  relaxing Y's upward closure 𝒞 gives, by HW (m1), μ_{R}(Y ⊂ 𝒟) ≤ ρ_R(𝒞)·μ_{R^{−𝒞}}(Y ⊂ 𝒟): a (CRC)-type relaxation ratio times
  a defect probability under a law that no longer constrains Y — the latter bounded, on the convex part, by BL-TILT's
  exponential moment of Σ_{x∈Y}ℓ_x² [ARGUED]. **So node A's n ≥ 1 statement and HW's (CRC) can be proven in one joint
  induction on N(R)**, non-circular exactly when node A at pattern R uses (CRC) only at patterns with fewer constrained pairs
  (the condition CRC-2T° step (3°) already meets). Recorded as a design suggestion, not proven.

### 5.4 NODEA55's caution "c_f must use c_U^in": CONFIRMED (agreeing with Codex §6)
Trace, every link by string: c_f° := c_U + 81c_A (NODEA55 B.2, "Corollary CRC-HW°"); "B_0 := c_f + 2" (HW §24.1, "Order of
constants (non-circular): a, C_ℓ, c_f (node A + KS) → B_* := c_f + 1 and B_0 := c_f + 2"); "c_B := 38416B_0/log L, n_H :=
⌊(4 + c_B)/(aβ_-)⌋" (HIST §7.4; with H-geo′ adopted, 10000B_0/log L per HW §41); n_♯ ≥ n_H; ε_2° := 6400^{n_♯}(C_ℓe^{b_n°+aR}
e^{−a/g_K²})^{n_♯+1} (NODEA55 B.2); c_U^out = 2ε_2°. Feeding c_U^out into c_f closes c_f → B_0 → c_B → n_H → n_♯ → ε_2° →
c_U^out → c_f; fixing c_U^in ∈ (0, 1] first breaks it, and (S2°) (2ε_2° ≤ c_U) then holds by the choice of g_0 after n_♯. HW
already says so in [RHW5-fix SYM-1] (c) ("Read c_+ ≤ c_A + 17c_U wherever the derivation needs the input value (c_U^in = 1), the
output being c_U^out = 2ε_2"); the sentence to be read a-posteriori-only is HW §30.6's "c_U^{out} = 2ε_2 (→ 0 as g_K → 0) is
what enters c_+ in Corollary CRC-HW". b_n°, b_D°, C_ℓ use c_U^in and are cutoff-free (NODEA55 Part D), so (S2°)/(T°) add no
loop. **No further cycle**: node A's constants (c_cem, c_A) sit before c_U^in in the order, and by §5.1–§5.3 their only
possible n-dependence is (NU-ii)'s.

*[Timestamp correction, appended 01:15Z: the "Correction to §3.4's (LC°)" says "appended 01:16Z"; the actual append time was
≈01:14Z (`date -u` printed 01:14:39Z right after that append). Locating strings in §5.4 were verified after writing: "B_0 :=
c_f + 2" is in HW §24.1 ("Lemma REL-boot"), and "c_B := 38416B_0/log L, n_H := ⌊(4 + c_B)/(aβ_-)⌋" in HIST §7.4 ("Theorem
HIST-sum").]*

### 3.7 Addendum — route (a) as the task phrased it does work, with 1 + O(δ), but by Brascamp–Lieb + Cramér–Rao, not Anderson
**Corollary BL-4 (two-sided perturbations: (M2) with c_2 = 1 + O(δ), volume-uniformly): PROVEN-HERE (given [BL] and the
Cramér–Rao inequality).** Let μ_∅ ∝ e^{−W} on R^D with W ∈ C², **(1 − δ)M ≤ ∇²W ≤ (1 + δ)M** (M > 0), K closed convex, q = xᵀQx
with B := M^{−1/2}2QM^{−1/2} ≤ c̄I, λ̄c̄ < 1 − δ, and every tilted law (constrained or not) of mean zero (even, or
color-invariant). Then for t ∈ [0, λ̄]:
  E_{μ_{K,t}}[q] − E_{μ_{∅,t}}[q] ≤ ½tr(B((1 − δ)I − tB)^{−1}) − ½tr(B((1 + δ)I − tB)^{−1}) ≤ rank(Q)·δc̄/((1 − δ − λ̄c̄)²),
hence, by Lemma IMPL (iii), **μ_{∅,λ̄}(K) ≤ exp(λ̄·rank(Q)·δc̄/(1 − δ − λ̄c̄)²)·μ_∅(K)** — per column c_2 = exp(O(δ)), uniformly in
the volume. *Proof.* Upper term: BL-TILT step (3) for μ_{K,t} with H = (1 − δ)M. Lower term: for the **unconstrained** tilted
law (no boundary), integration by parts gives E[x∇V_tᵀ] = I, so Cramér–Rao gives Cov ≥ (E∇²V_t)^{−1} ≥ ((1 + δ)M − 2tQ)^{−1}
(V_t := W − tq), hence E_{μ_{∅,t}}[q] ≥ tr(Q((1 + δ)M − 2tQ)^{−1}). Both matrices are functions of M^{−1/2}QM^{−1/2}, so the
difference is eigenvalue-wise ½b_i[1/((1−δ)−tb_i) − 1/((1+δ)−tb_i)] ≤ δb_i/((1 − δ − tb_i)²). ∎
**Reading.** This is exactly the task's route (a): a log-concave perturbation of the Gaussian model with controlled error, and an
anti-correlation constant 1 + O(δ) — volume-uniform, with no decay estimate. **But** (1) the mechanism is Brascamp–Lieb (an upper
covariance bound under convex conditioning) against Cramér–Rao (a lower covariance bound without it), not Anderson/Prékopa;
(2) it needs the **upper** Hessian bound too, which NO-ONE (i) shows cannot be dropped (there the upper bound fails at ∂D and the
excess is O(1)); (3) it is moot for the consumer, because BL-TILT with the lower bound alone already gives (LCR°), hence (CEM°),
with GAUSS's constant. **So the task's route (a) is answered: YES for (1 ± δ)-two-sided small-field perturbations, by a different
proof; and its hypotheses for the actual chain are (LC°)'s.**
**Consequence for NODEA55 C.4** (locating string "For Gaussian and for log-concave perturbations of Gaussian measures this is
the classical Anderson/Prékopa mechanism"): **REFUTED as to the mechanism** — NO-ONE (i) is a log-concave perturbation of a
Gaussian (Gaussian × 1_D) in which the Anderson/Prékopa conclusion (constant 1) is false; **the inequality NODEA55 C.4 actually
states ("does not raise, beyond c^{|A|}, the probability …") is TRUE in the log-concave class**, with c^{|A|} ≤
(1 − λ̄c̄)^{−rank(Q)/2} by BL-TILT (the derivative identity of Lemma IMPL (iii) and E_{μ_{∅,t}}[q] ≥ 0), and with c = 1 + O(δ)
under two-sided control (BL-4). The other clause of the same sentence — "available at best in the small-field region (where the
gauge-fixed density is a small perturbation of a Gaussian)" — is **NOT-VERIFIED**: false for single-level smallness (G5), and
ARGUED (not proven) for the lane's multiscale small-field region Λ_k(𝔥), which is the reading the lane's definitions support.

---

## 6. Summary table (every item of this file)

| id | item | verdict / status | where |
|---|---|---|---|
| nr-01 | NODEA55 Proposition GAUSS (na55-20), load-bearing steps re-derived | **CONFIRMED** for its model (agree Codex §5) | §1 |
| nr-02 | GAUSS counts 23328 / 69984 / 34992 and log c_cem = 24254.6 at λ_f = ½ | **CONFIRMED** (G1, rigorous ln 2) | §1 |
| nr-03 | PLD §19.5's dof 52488 vs Lemma READ (i)'s 69984 | recorded (a constant, no status change) | §1 |
| nr-04 | Lemma SPEC*: the cutoff-free spectator class 𝔖^cap_*(A; k_0) ⊇ 𝔖^cap_𝔥(k_0) | PROVEN-HERE | §2.2 |
| nr-05 | (M1), (M2) in three currencies each; (LCR°) | stated, with the consumer's quantifiers; OPEN | §2.3 |
| nr-06 | Lemma IMPL: (LCR°) ⇒ (CEM°); (M1)+(M2) ⇒ (LCR°) ⇒ (M2^mean); one rate λ̄ suffices; split optional | PROVEN-HERE | §2.4 |
| nr-07 | Theorem BL-TILT (Brascamp–Lieb along the tilt path) | PROVEN-HERE given [BL] (convex-domain approximation flagged) | §3.1 |
| nr-08 | Cor. BL-1: (CEM°) in the convex-core model **with capped spectators**, c_cem = (1 − λ̄)^{−34992}, no split | PROVEN-HERE given [BL] | §3.1 |
| nr-09 | Cor. BL-2: B-L re-derives GAUSS's Anderson comparison; (M2) moot in the convex class; volume-uniform for free | PROVEN-HERE | §3.1 |
| nr-10 | Cor. BL-3: convex / δ-semiconvex perturbations of the model | PROVEN-HERE given [BL] | §3.1 |
| nr-11 | NO-ONE (i): anti-correlation constant 1 fails for a symmetric strongly log-concave law (Gaussian × 1_D) | PROVEN-HERE (G2) | §3.2 |
| nr-12 | NO-ONE (ii): constant 1 fails in the Gaussian model with the n = 1 allowance | PROVEN-HERE (G3) | §3.3 |
| nr-13 | Cor. BL-4: c_2 = 1 + O(δ), volume-uniform, for (1 ± δ)-two-sided perturbations (B-L + Cramér–Rao) | PROVEN-HERE given [BL] | §3.7 |
| nr-14 | NODEA55 C.4 "For Gaussian and for log-concave perturbations of Gaussian measures this is the classical Anderson/Prékopa mechanism" | **REFUTED as to mechanism** (nr-11); the stated inequality is TRUE in that class with c^{|A|} ≤ (1 − λ̄c̄)^{−rank/2} (BL-TILT) | §3.7 |
| nr-15 | NODEA55 C.4 "available at best in the small-field region (where the gauge-fixed density is a small perturbation of a Gaussian)" | **NOT-VERIFIED**: false for single-level smallness (G5); ARGUED for the multiscale Λ_k(𝔥) | §3.7 |
| nr-16 | the nonabelian measure has no central symmetry in the exponential chart (cubic vertex, c3 = −4) | PROVEN-HERE (G4) | §3.4 |
| nr-17 | mean zero of every tilted constrained law by global colour invariance | PROVEN-HERE (elementary) | §3.4 |
| nr-18 | the Wilson action is not convex on the single-level small-field set (NO-type) | PROVEN-HERE at plaquette norms 0.485, 0.248 (G5); below ε_1: ARGUED (scaling) | §3.4 |
| nr-19 | convexity with δ = O(ε_1) on the multiscale small-field core | ARGUED | §3.4 |
| nr-20 | (LC°) in conditional form (LC-1′, LC-2′, LC-3′): the precise missing input of route (a); (LC°) ⇒ (LCR°) | statement OPEN; implication PROVEN-HERE given BL-TILT | §3.4 + correction |
| nr-21 | Holley–Stroock (extensive perturbation; F-UNIV on localisation), Bakry–Émery (strong coupling only) | not available (ARGUED assessments) | §3.4 |
| nr-22 | route (b): chessboard gives no lower bound and cannot carry 1_R, w; reaches (M1_0) only at F_< ≡ 1 (spectator obstruction, new); FKG/Ginibre abelian | not available (ARGUED: limits of the methods, not impossibility) | §3.5 |
| nr-23 | NODEA55 C.3 (na55-23) "does not reach (W0)" | **CONFIRMED**, extended by nr-22 | §3.5 |
| nr-24 | one-level convexity inside DLR ⇒ (EQ-bc) with a forced charge; level-by-level rate degradation | ARGUED | §3.6 |
| nr-25 | (M1) inventory: DOM′, AT, DLR/W-FREE, (M-i), LT, GAUSS present; effective-action domination ((I^E)″ in C² form, main-term reduction off G_Q, coupling response, large field) absent | as tabled | §4 |
| nr-26 | the (M1)+(M2) split is a worse factorisation than (LCR°) ⟸ (LC°) | ARGUED (structural) | §4 |
| nr-27 | NODEA55 FOR THE LEAD item 3 "… and hold at fixed volume" | **NOT-VERIFIED** as an O(1) statement (LT is polynomial in u; agree Codex §2) | §0, §4 |
| nr-28 | (M1)'s constants are cutoff-free by construction | PROVEN-HERE | §5.1 |
| nr-29 | NODEA55 Part D model row (n = 0 and n ≥ #cubes PROVEN; 1 ≤ n < volume ARGUED) | **CONFIRMED** | §5.2 |
| nr-30 | NODEA55 C.2 (v) "c_2 = 1 + o(1) uniformly in n" | **NOT-VERIFIED** (the deviation from 1 is real: nr-12) | §5.2 |
| nr-31 | Proposition NU: cutoff-uniformity ⟸ an n-free constrained Peierls bound (+ n-free per-defect multiplier) | PROVEN-HERE (implication); inputs OPEN | §5.3 |
| nr-32 | node A (n ≥ 1) and HW's (CRC) in one joint induction on N(R) | ARGUED (design suggestion) | §5.3 |
| nr-33 | NODEA55's caution "c_f with c_U^in, not 2ε_2" | **CONFIRMED** (agree Codex §6) | §5.4 |

**Counts (prior claims re-judged): CONFIRMED 5** (nr-01, -02, -23, -29, -33); **NOT-VERIFIED 3** (nr-15, -27, -30);
**REFUTED 1** (nr-14, mechanism only; correction: the inequality holds in the log-concave class by BL-TILT, and with
c = 1 + O(δ) under two-sided control by BL-4). **New: PROVEN-HERE 15** (nr-04, -06, -07, -08, -09, -10, -11, -12, -13, -16,
-17, -18 (two field strengths), -20 (implication), -28, -31 (implication)); **ARGUED 6** (nr-19, -21, -22, -24, -26, -32);
**OPEN statements** (M1), (M2), (LCR°), (LC°), (NU-i)–(NU-iii). Inputs cited, not re-derived: Brascamp–Lieb [BL] (and its
convex-domain extension by approximation), Cramér–Rao, PLD Lemma DLR / Theorem W-FREE (as filed). Pre-stated refutation
criteria: R1 did not apply to GAUSS (its Anderson step is a covariance comparison); R2 no (cores symmetric and convex in the
model); R3 no (exponent and base match); R4 applied to every (M2) route for the actual chain (each needs a hypothesis the lane
does not supply: §3.4–§3.5); R5 no cycle beyond the one NODEA55 names, now localised to (NU-ii).

---

## 7. FOR THE LEAD

**1. (M1) and (M2), stated (§2.3), and a better target.** (M1) is a moment of the *unconstrained* chain (cutoff-free by
construction over 𝔖^cap_*); (M2) is the constrained/unconstrained comparison and carries every quantifier of (CEM°), the
cutoff included. **(LCR°) — E_{μ_{R,λ̄}}[𝔞^col_A] ≤ B|A|, the constrained tilted equipartition at the single rate λ̄ — is weaker
than (M1) + (M2) and sufficient for (CEM°) (Lemma IMPL).** The split is optional and, by items 2–3, the worse factorisation.

**2. (M2) has no correlation-inequality proof outside the Gaussian convex core.** The anti-correlation constant 1 fails for a
symmetric strongly log-concave law with a dominated quadratic tilt and a symmetric convex constraint (NO-ONE (i), exact), and in
the Gaussian model as soon as the cutoff allows one defect (NO-ONE (ii), exact). RP/chessboard gives no lower bound on μ(R) and
cannot carry 1_R, w or spectators; FKG/Ginibre are abelian. NODEA55 C.4's "classical Anderson/Prékopa mechanism for log-concave
perturbations" is REFUTED as to mechanism.

**3. The perturbation-stable replacement is Brascamp–Lieb along the tilt path (Theorem BL-TILT).** It proves (LCR°), hence
(CEM°), directly — volume-uniformly, with GAUSS's constant (1 − λ̄)^{−34992}, for capped spectators too (the half of Codex §5's
NOT-VERIFIED that concerns the moment) — using only convexity of the constraint and a mean-zero condition, which the nonabelian
chain supplies by global colour invariance although it lacks central symmetry (cubic vertex, G4). The task's route (a) "1 +
O(small)" holds too (BL-4, B-L against Cramér–Rao), but is moot.

**4. What node A must now prove (the precise residual): (LC°)** in conditional form (§3.4 correction): (LC-1′) convexity of the
chain on regions with no defect at any level, with small-field boundary data, H ≥ (1 − δ)·(model precision), and the column
action Q-semiconcave and dominated (the C² form of PLD §18.7.2 (a)); (LC-2′) convexity of the small-field core in the chart;
(LC-3′) a Peierls bound for the large-field set under the tilted constrained law, with the r^{−8} decay of forcing. Single-level
smallness does NOT give (LC-1′) (exact Nielsen–Olesen-type witness G5); the multiscale constraint plausibly does (ARGUED). None
of the three is in the lane; (I^E)″ would supply (LC-1′) if restated with C² polymer bounds dominated by the main term.

**5. n_♯ (§5).** n enters node A only through 1_{R_n}; (M1) is cutoff-free; by Proposition NU, cutoff-uniformity of c_cem
follows from a **cutoff-free constrained Peierls bound (NU-ii)** plus an n-free per-defect multiplier — so SMALLNESS_DAG §3.1's
only potential cycle closes exactly when (NU-ii) (equivalently (LC-3′)) is proven with per-cube activities. **This is where
(SDP)-type content re-enters node A after route (4°)** — not an HW obligation, a node-A one. NODEA55's c_U^in caution:
CONFIRMED (agree Codex §6); HW §30.6's "c_U^{out} = 2ε_2 … is what enters c_+" must be read a posteriori only.

**6. What PROOF.md's tally / HANDOFF's critical path should say differently.**
- HANDOFF, node-A item: replace "(M1) an effective-action lower bound and (M2) an Anderson-type correlation inequality" by
  *"(LCR°) ⟸ (LC°) = (LC-1′) multiscale small-field convexity (C² effective action) + (LC-2′) core convexity + (LC-3′) large-field
  Peierls bound with decay; (M2) as a correlation inequality is not available beyond the Gaussian convex core (NODEA_RES55
  NO-ONE); the cutoff enters only through (LC-3′)/(NU-ii)."*
- Tally: GAUSS now has two independent confirmations (Codex §5, this file). Candidates to bank after Codex review: BL-TILT and
  BL-1…BL-4, NO-ONE (i)–(ii), Lemma IMPL, Lemma SPEC*, Proposition NU (implication), the G4/G5 witnesses. Nothing here changes a
  counted HW/PLD theorem.
- NODEA55 C.4's sentence (nr-14) and its parenthetical (nr-15), and FOR THE LEAD item 3's "hold at fixed volume" (nr-27), should
  not be quoted as written.

**7. Codex verdicts used** (all from CODEX_REVIEW_NODEA.md, read complete at 00:48Z): §5 GAUSS CONFIRMED — agree; §5 c_2
extensions NOT-VERIFIED — agree and sharpen (two REFUTED as to constant 1, capped-spectator moment PROVEN via BL-1); §5 C.2 (iv)
necessity REFUTED — agree (not used); §5 C.1 sufficient reduction CONFIRMED — agree; §2 LT limits — agree; §2 read-level
correction — adopted; §4 W0 as a separate clause — adopted; §6 c_U^in — agree; §3 θ ≤ 1/28 REFUTED — not used.

Files written: NODEA_RES55.md; checks/nr55_1_criteria.md, nr55_1.py, nr55_1_out.txt, nr55_1_err.txt; checks/nr55_2_criteria.md,
nr55_2.py, nr55_2_out.txt, nr55_2_err.txt, nr55_2b_out.txt, nr55_2b_err.txt. No git command was run.

---

## Errata (append-only; found on proof-reading at ≈01:20Z; nothing above is edited)
- **E1 (§3.4 correction, last paragraph).** "(LC-1′) + (LC-2′) + (LC-3′) ⇒ (LCR°) with B ≤ 34992/(1 − λ̄/(1 − δ)) + C_LF" is off
  by a factor (1 − δ). With c̄ ≤ 1/(1 − δ), BL-TILT step (3) at t = λ̄ gives ½·rank·c̄/(1 − λ̄c̄) ≤ 34992|A|/(1 − δ − λ̄), so the
  correct per-cube constant is **B ≤ 34992/(1 − δ − λ̄) + C_LF**. The integrated moment constant stated in §3.4's (LC°)
  paragraph, log c_cem ≤ 34992·log(1/(1 − λ̄/(1 − δ))) + λ̄C_LF, is correct as written (it is −½Σlog(1 − λ̄b_i) with b_i ≤ 1/(1 − δ)).
  Corollary BL-1's "B = 34992/(1 − λ̄)" (δ = 0) is correct.
- **E2 (§0, controls).** "the witness has no σ3 component, so its abelian part is the zero vector" over-states what the check
  printed: G5n2 shows Q_C(v_abelian) = 0 exactly, i.e. the σ3 part of the witness is zero **or** a null (pure-gauge) abelian
  direction; which of the two was not checked. The conclusion stands: G5n2 is uninformative and is not counted; G5n is the
  informative control.
- **E3 (§6 counts).** nr-18 is one item proven at two field strengths; nr-20's "PROVEN-HERE" refers to the implication
  (LC°) ⇒ (LCR°) only, the statement (LC°) itself being OPEN.

Closing provenance: deliverable final at 2026-10-29T01:21Z (`date -u` at the last append). Model: claude-opus-5-5.
*[Timestamp correction: the Errata header's "≈01:20Z" and the closing line's "01:21Z" were written ahead of the clock; `date -u` printed 2026-10-29T01:18:51Z right after that append, and this line was appended at 2026-10-29T01:18:57Z. Three of my own timestamps in this file (01:12Z, 01:16Z, 01:20Z/01:21Z) were estimates written before the append; each is corrected by a following line. No content depends on them.]*
