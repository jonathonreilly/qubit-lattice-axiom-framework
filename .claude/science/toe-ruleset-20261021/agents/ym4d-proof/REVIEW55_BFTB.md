Reviewer model: claude-opus-5-5

# REVIEW55_BFTB — Opus 5.5 re-review of BFT lane B sessions 9, 10, 11 (BFT_B.md §27-§43)

UTC start: 2026-10-28T22:12:04Z
Batch: C2. Check-id prefix: `r55b_`. Deliverable (the only file written): `$L/REVIEW55_BFTB.md`
(plus `checks/r55b_*` criteria/scripts if a numeric check is needed, criteria first).

## PRE-STATED (written before any derivation; statements only)

Targets (from the batch scope; each will get CONFIRMED / NOT-VERIFIED / REFUTED):

T1 (s9, §27-§33) (Res-Hölder) "closed at m = 0".
T2 (s9) the (H-inv+) bundle "closed".
T3 (s9, §31) whatever §31 states as (CO-fun) — its exact statement and status.
T4 (s10, §35.5) Theorem COF: (CO-fun) PROVEN under (CC-0).
T5 (s10, §35.7) the refutation of (CO-fun) "as stated".
T6 (s10) the claim that (GT-sup) "is not a spike-support question".
T7 (s10) Lemma ΓT-op, and its clause (d) absolute constant.
T8 (s11, §41) B1/B2 bounds — "slot-wise, weight-free, factor-k-free".
T9 (s11, §41.5) the no-go.
T10 (s11) Proposition GZ-FALSE — (CovLift)'s g_Z clause at θ > 0 is false (a refutation; checked as hard as a theorem).
T11 (s11) Theorem TRANSP — "PROVEN given exactly two inputs".
T12 (s11, §43) the nontrivial background "collapses into BFT-5".
T13 COFUN.md's claim: BFT_B l.3810 "with D(S^E_0(S)) = 0" is wrong while l.4203 is right — decides whether Theorem COF can stand in for BFT-5 clause (b).
T14 the earlier review REVIEW_BFT_B_S9_S10.md — review the reviewer (its verdicts on §27-§37).
T15 the Codex reviews CODEX_REVIEW_GAPZ.md (F1, F2, F6, F7) and CODEX_REVIEW_COFUN.md — agree/disagree, per finding.
T16 every number that changed a decision in §27-§43 (constants, exponents, thresholds) — currency and evaluation point.
T17 session 9-11 entries of BFT_B_LOG.md — whether the log's status lines match the sections.

What counts as a refutation (per claim):
- For a PROVEN / CLOSED claim: an explicit counterexample, or a load-bearing step that is false
  (an inequality that fails at the stated quantifier, a constant that is not absolute, an identity
  that does not hold), or a hidden input not in the stated hypothesis list that the conclusion
  needs (that makes "PROVEN given exactly two inputs" false, i.e. REFUTED as stated, even if the
  conclusion may survive with more inputs).
- For a REFUTATION / "FALSE" verdict (T5, T9, T10, part of T13): the refutation is itself refuted
  if its counterexample does not satisfy the hypotheses of the statement it refutes, if it refutes
  a different statement (symbol collision / different quantifier), or if its computation is wrong.
- A mismatch between what a status line says and what the section derives is a REFUTATION of
  the status line (not of the mathematics) and will be recorded as such.
- Anything I cannot settle from the text and my own derivation is NOT-VERIFIED with the missing
  item named. "The file says PROVEN" is not evidence.

Systemic-defect checks applied to every claim: (1) symbol collisions — each compared symbol
pinned by file:line; (2) stale minima / quantifiers — what each inequality was evaluated at;
(3) checks that cannot decide — could the gate have failed.

---

## FINDINGS

Reading record (all by string, then sed ranges; no file read whole): BFT_B.md l.3571-4782 (§27-§43) in full;
BFT_B §0, §12.0, §15.0, §18.0-18.1, §19.1-19.6, §21.0-21.2, §24.1, §25.1; BFT_A §1.1-1.4, §7.1-7.2, §8.2, §26.0-26.2,
§31.0-31.1, §33.1-33.4, §38.6; LINEAR_PACKAGE §1; PROOF.md TOWER-VAR (l.6633-6645) and the S24/S25 notes (l.140-175,
l.6915-6950); REVIEW_S22 l.296-330, l.385-405; REVIEW_BFT_A_S5 l.28-32, l.371-375; REVIEW_BFT_A_S6 l.20-28, l.149-200;
REVIEW_BFT_B_S5 C.3; REVIEW_BFT_B_S9_S10.md in full; CODEX_REVIEW_GAPZ.md in full (260 lines, complete, ends with its
summary table); CODEX_REVIEW_COFUN.md in full (280 lines, complete, ends with SHA-256 lines — it was 7011 B when the lane
listing was taken and is complete now); COFUN.md §1, §5-§7 (l.1-60, l.355-520); BFT_B_LOG.md sessions 9-11 (l.471-680);
checks/bb11_bgd.py (the `Tower` class, l.180-240).

Checks run by this reviewer (criteria written first, exact `Fraction` arithmetic, no floats in any verdict):
- `checks/r55b_dip_criteria.md` (22:44:52Z) → `checks/r55b_dip.py` → `checks/r55b_dip_out.txt`: **ALL PASS, D4 controls
  fired** (0.29 s). Independent construction (no code copied from bb9b/bb10/bb11).
- `checks/r55b_num_criteria.md` (22:44:58Z) → `checks/r55b_num.py` → `checks/r55b_num_out.txt`: **ALL PASS**.

Notation used below (pinned by file:line, because the batch's central defect is a collision in exactly these symbols):
- **D(S) as a functional vs D(S) as a function.** BFT_A §26.0 (l.2211) defines composite co-closedness as Ξ^TS = 0 with
  Ξ defined on Λ_0 := level-0 functions constant on the level-k roots — a statement *on Λ_0*. BFT_A §31.0 and BFT_B §27.1
  (l.3586) also call D(S) := Ξ^TS "a level-0 function". The two readings agree off the level-k roots and differ at them.
  BFT_B §34.1 (l.3962-3964) makes the split explicit: D^root, D^⊥, and **(CC-0) := D(S) = 0 as a level-0 function**.
  Every "D(·) = 0" below is labelled (Λ_0) or (pointwise).
- **For a Setting-LIN source with B_k = 0 the exact relation is** D(S) = κ_{k−1}·ev^{(0→k)T}d*r_{k−1}(x) at its response x
  (derivation: D(S)(z) = ⟨S, Ξδ_z⟩ = ⟨Hx, Ξδ_z⟩ = d/dt E(x + tΞδ_z) and only r_{k−1} moves, by root covariance at the
  lower levels and x_k fixed). So **(CC-0) ⟺ the response's top residual is co-closed**, and, slot by slot,
  D(S) = D(S^j) + ev^{(0→k)T}d*s_{k−1} (G-slots and lower s-slots contribute 0 pointwise; r55b D5, D6).

---

### Finding 1 (T1, s9 §29) — (Res-Hölder) at m = 0
**Lemma RT-cc (a)-(d) [§29.1]: CONFIRMED.** Re-derived from the Euler-Lagrange equations of E_src (BFT_A §7.1 l.444ff):
(E_l) ρ_{l−1} = Q_l^Tρ_l − d*G_l − j_l, (E_0) d*dx_0 + Q_0^Tρ_0 − d*G_0 − j_0 = 0, then d* of both with d*Q_l^T = ev^Td*
(transpose of Q_ld = d·ev) and d*d* = 0 gives (★0), (★l) and, by composing placements, (†) ev^{(0→l+1)T}ψ_l = Ψ_l;
injectivity of ev^T is on the whole space (distinct roots). (b)-(d) as written; the Hodge step needs only d*J_0 = 0 of the
*total* J_0. One precision, not load-bearing: l.3674 "Ψ_{k−1} = Ξ^TS = D(S)" is exact only if d*s_{k−1} = 0; in general
D(S) = Ψ_{k−1} + ev^{(0→k)T}d*s_{k−1} (the extra term is root-supported, so the support conclusion stands). REVIEW_BFT_B_S9_S10
S9-1 repeats the same imprecision.
**Lemma FT (i)-(iv) [§29.2]: CONFIRMED** (one block per level-l link because a monotone axial path from c_X to y ∈ B(X) stays
in the box B(X); |c| ≤ 1 as an average of {0, ±1}; (ii) is sup|d*j| ≤ 2d·sup|j| at a root and the L^{3(k−l)} rescaling).
The sharp values are smaller (CODEX_REVIEW_COFUN F9: (L−1)/(2L) = 1/3 and d(L²−1)/(4L) = 8/3 at d = 4, L = 3); the
file's bounds are valid upper bounds.
**Theorem RHT-cc [§29.3]: CONFIRMED** — the bound of Theorem RHT with π_l(j_l) → π_l(ĵ_l); the index swap
L^{−(1−α)(k−l'−u)}L^{−3u} = L^{−(1−α)(k−l')}L^{−(2+α)u} and K_f = 2d/(1 − L^{−(2+α)}) re-derived; **r55b_num N1**:
3^{−9/4} ∈ [0.08442, 0.08443] (by x⁴ = 3^{−9} with rational endpoints), K_f ∈ [8.73763, 8.73773], so "K_f = 8.737, ≤ 8.74"
is right; the printed intermediate "3^{−2.25} = 0.08434" (l.3721) is a typo (not decision-relevant). It holds for every
composite-co-closed source including root-charged ones (ψ_{k−1} ≠ 0 enters ĵ_{k−1} and is priced by FT (ii)). **Its right
side contains κ_+||r^c_{k−1}||_∞ of the same response**: (Res-Hölder) is a statement *relative to the top residual*, which
is exactly the role Corollary RH-inv gives it ((H-inv) ⟹ (H-inv+)).
**Corollary RHT-V [§29.4] "N_res ≤ C_Vη² uniformly": NOT-VERIFIED.** The parenthetical "(using ||r^c_{k−1}||_∞ ≤
||x||_inv ≤ G_Rη² or Corollary LIN0's bound for the top term)" (l.3739) is a hypothesis: LIN0 (BFT_A §26.1) covers
level-wise co-closed plain currents and the V_l are not; G_Rη² would be (H-inv) for the same rows. Missing: a bound on the
top residual of the response to V. (Agrees with REVIEW_BFT_B_S9_S10 S9-11.) The Γ-independence ("for every gauge fixing")
is CONFIRMED (r_l(x + Ξλ) = r_l(x) for λ ∈ Λ_0; Lemma FG (iii)).
**Theorem RHT_m-cc (c_w = 14) [§29.5]:** spot-checked only; S9-8's "12 suffices" is consistent with my reading.
**Verdict T1:** (Res-Hölder) at m = 0, in the sense "N_res ≤ C(top residual + source norms)", **CONFIRMED** for level-wise
and for composite-co-closed sources; the absolute η² form for the rows (RHT-V) **NOT-VERIFIED**.

### Finding 2 (T2, s9 §30) — the (H-inv+) bundle "closed"
**CONFIRMED as bookkeeping, with two scope corrections.** I re-checked the quoted statuses at the cited lines:
REVIEW_BFT_A_S6 l.23-24 (YH, W0, GU CONFIRMED; LIN0 "CONFIRMED in its stated scope … level-wise co-closed sources, m = 0,
trivial background, 0 < α < θ < 1"), REVIEW_BFT_A_S5 l.30 (CO-0R/CO-upR/CO-B CONFIRMED) and l.373 ("CO-B removes 13.7's
(SB) gap outright"). Corrections: (i) REVIEW_BFT_A_S5 l.30-31 confirms Corollary G♯R **only on 0 < α < θ ≤ 1 − α**; §30's
"(G♯-rough) curvature half … 0 < α < θ" drops the upper limit (stale quantifier; (¼, ½) is inside, so no consequence at
lane A's point). (ii) As S9-13 says, the bundle is for **level-wise co-closed** classes, which the remainder rows do not
occupy. The lane-A proofs themselves are not re-derived here; the claim is bookkeeping and is confirmed as bookkeeping.

### Finding 3 (T3) — what §31.2 states as (CO-fun) (l.3802)
The statement: for every Setting LIN^cc source in (P0)+(Pl-c)+(G)+(R), ||f_0||_∞ + [f_0]^∞_α ≤ C_fun(||G^c_0||_∞ +
[G^c_0]_α + ||j^c_0||_∞ + ||j||_Pc + ||G||_Y + ||s||_R + κ_+||r^c_{k−1}||_∞), r_{k−1} the response's own top residual.
**This statement is TRUE given Theorem COF (Finding 4) and lane A's W0/GU/LIN0** — see Finding 5 for the derivation; its
sup half even holds without the κ_+||r^c_{k−1}|| term. Session 9's status "OPEN" was therefore not wrong, and session 10's
"FALSE" (Finding 5) is.

### Finding 4 (T4, s10 §35.2-§35.5) — Lemma SPLIT, Lemma DF-cc, Proposition COF-size, Theorem COF
**Lemma SPLIT [§35.2, proof l.4035]: REFUTED as written (pointwise), CONFIRMED on Λ_0.** The proof says "r_i(x + Ξλ) =
r_i(x) for **every** λ by root covariance (§29.4)"; §29.4 has it for λ ∈ Λ_0 only. With x_k fixed,
r_{k−1}(x + Ξλ) = r_{k−1}(x) + d·ev^{(0→k)}λ, so the top residual slot has **D(S^s) = ev^{(0→k)T}d*s_{k−1} ≠ 0 pointwise**
(root-supported, total 0: composite-co-closed but not (CC-0)), while lower residual slots do give 0 pointwise.
**r55b D5** (exact): d*(Q_1^Tδ_b) is nonzero, root-supported, total 0 and equals ev^{(1→2)T}d*δ_b; **D6** (control):
random lower slots s_0 give D = 0 at every site. Consequence: "D(S^j) = D(S); if S satisfies (CC-0) then so does S^j" is
**false** — **r55b D7**: S = (s_1 = δ_b) + (j_1 = −path_b) has D(S) = 0 pointwise while D(S^j) ≠ 0. What survives (and is
all that superposition needs): every slot is composite-co-closed (on Λ_0), so each slot response exists and responses add.
REVIEW_BFT_B_S9_S10 S10-2 CONFIRMED the pointwise statement on the same "r_i(Ξλ) = 0" — I disagree; CODEX_REVIEW_COFUN F15
flagged the gap (NOT-VERIFIED there) — I agree and settle it (REFUTED for the top slot).
**Lemma DF-cc (i)-(iii) [§35.3]: CONFIRMED** with D(S) read as **D(S^j) := Σ_l ev^{(0→l)T}d*j_l** (the plain-current
divergence; this is what the proof actually uses — ev^{(0→i+1)T}(ξ_i + ψ_i) = Σ_l ev^{(0→l)T}d*j_l) and with
**ĵ_0 := j_0 + h_0^Tψ_0** (the i = 0 regrouping term); §27.1 l.3590 defines ĵ_0 := j_0, a live collision
(CODEX_REVIEW_COFUN F14 — agree). Re-derived: Proposition RF's h^{(0→l)} = Σ_{i<l}ev^{(i+1→l)}h_iQ_str^{(0→i)} by induction
from Q_l = Q_{str,l} − d h_l, root covariance and IT-str; transpose; exchange of the (i, l) double sum.
**Proposition COF-size [§35.4]: CONFIRMED** (re-derived; r55b_num N2: 1 + 8·27/26 = 121/13 ≤ 9.31 exactly).
**Lemma W0-use [§35.1]:** spot-checked against BFT_A §28.5's step list as quoted; agree with S10-1.
**Theorem COF [§35.5]: CONFIRMED as an implication** (inputs quoted from lane A: Theorem YH's 𝒩* ≤ C_YNn, W0 step 4/LES-div/
Lemma LE/BL-C, GU, LIN0, PW-cc's residual ℓ¹ bounds — not re-derived here). Load-bearing step re-derived: the telescoping
Σ_l⟨j_l, Y_l⟩ = ⟨C(j), Y_0⟩ − Σ_m⟨Σ_{l>m}(Q^{(m+1→l)})^Tj_l, r_m(Y)⟩ (from Y_l = Q^{(0→l)}Y_0 − Σ_{m<l}Q^{(m+1→l)}r_m(Y));
co-closedness of C(j) when D(S^j) = 0; |⟨C, Y_0⟩| ≤ sup|C|·𝒩(Y^p) with n²·n^{−3}·n = 1; DF-cc (ii)-(iii); the residual
sum with m = l − 1 − a giving A·L^{−2(k−l)}L^{−2a}π_l(ĵ_l). **The written proof has a gap** exactly at Lemma SPLIT: under
(CC-0) on the total S with d*s_{k−1} ≠ 0, S^j is not (CC-0) and step (c)'s co-closedness of C(j) fails. **Repair (mine):**
under (CC-0), ψ_{k−1} = R_k(D(S^j)) = −d*s_{k−1}; replace j_{k−1} by j_{k−1} + P(s_{k−1}) and s_{k−1} by 0 and G_{k−1} by
G_{k−1} − Σ_b s_{k−1}(b)G_b, using the exact identity of Finding 5 (P(b) := Σ_b b(b)·path_b). The rewritten source is the
same functional, has every slot (CC-0), and costs ||j'||_Pc ≤ ||j||_Pc + L³||s||_R, ||G'||_Y ≤ ||G||_Y + C(L)||s||_R. So
the statement of Theorem COF stands.

### Finding 5 (T5, s10 §35.7) — "(CO-fun) as stated in §31.2 is FALSE": **REFUTED**
**What §35.7 proves:** the defect term of the regrouping, paired with a representative, equals n²Σ_X D(c_X)Φ_k(Y^p_{*,0})(c_X)
(Proposition COF-res, **identity CONFIRMED**: R_{i+1}(D) sits on level-k roots as level-(i+1) sites, and
Σ_{i<k}ev^{(i+1→k)}h_iQ_str^{(0→i)} = h^{(0→k)} = Φ_k by Proposition RF). **What it does not prove:** that this term is the
"single extra term in f_0" with "every other term bounded as in Theorem COF". When D(S^j) ≠ 0 the remaining object
Σ_l(Q_str^{(0→l)})^Tĵ_l is not co-closed (d* of it equals d*(Q_str^{(0→k)})^Tρ_{k−1} ≠ 0, because J_0 = that object −
(Q_str^{(0→k)})^Tρ_{k−1} is co-closed and ψ_{k−1} ≠ 0), so its pairing with Y^p_{*,0} is representative-dependent and is not
bounded by step (c). The "≍ L^{2k−3}π_{k−1}(j_{k−1})" is the size of one term of a representative-dependent split, not of
f_0. (Agrees with CODEX_REVIEW_COFUN F2 and with S10-10's NOT-VERIFIED; disagrees with S10-11's CONFIRMED.)
**The counterexample to the falsity claim (exact).** Take the source §35.7 has in mind: one root dipole carried by
j_{k−1} = q·path_b, path_b the straight level-(k−1) path from c_X to c_{X+e_μ} (b = (X, μ)). Every S4′ contour of b runs
from c_X to c_{X+e_μ} inside B(X) ∪ B(X+e_μ) (LINEAR_PACKAGE §1.2: T^σ_y = P^σ(c_X→y)·S_y·P^σ(c_Y→y+Le_μ)^†), so
v := path_b − Q_{k−1}^Tδ_b is a cycle in that box, hence v = d*G_b with G_b a level-(k−1) 2-form supported in the box,
|G_b| ≤ C(L, d). Therefore, for every chain with x_k = 0,
  **⟨q·path_b, x_{k−1}⟩ = q·r_{k−1}(x)(b) + ⟨q·G_b, dx_{k−1}⟩**,
i.e. the root-charged plain current **is the same source as** (residual source s_{k−1} = qδ_b) + (divergence-form source
G_{k−1} = qG_b). **r55b D2** (exact, d = 2, L = 3, k = 2, T = 3, both directions): d*v = 0, supp v ⊂ B(X) ∪ B(X+e_μ),
d*G = v solvable inside the box (max|G| = 1/3), identity exact on 20 random chains; **D3**: the source has D ≠ 0 at the two
level-2 roots (class (cc) ∖ (CC-0)); **D4**: with G := 0 the identity fails (control fired); **D8**: same identity in residual
form. By Corollary LIN0 and Theorem GU (CONFIRMED in lane A) the response has ||x||_inv ≤ C(||s||_R + ||G||_Y) ≤
C(L, θ, α)·q, while ||j||_Pc = L^{3+θ}q. **So f_0 for the canonical root-charged source is bounded by C·||j||_Pc, k- and
T-uniformly**, and the "L^{2k−3}" mechanism does not exist for it.
**The general case (derivation).** For any composite-co-closed plain-current collection j, the root charges
ψ_{k−1}(X) = D(S^j)(c_X) obey, for every set A of level-k sites, |Σ_{X∈A}ψ_{k−1}(X)| = |Σ_l Σ_{Y∈A_l}(d*j_l)(Y)| ≤
Σ_l |∂_lA_l|·sup|j_l| = |∂_kA|·Σ_lπ_l(j_l) (divergence theorem at each level; a level-k face is crossed by L^{3(k−l)}
level-l links). By the undirected max-flow/min-cut (Gale) feasibility theorem there is a level-k 1-form b with
d*b = ψ_{k−1} and **sup|b| ≤ Σ_lπ_l(j_l) ≤ ||j^c_0||_∞ + (L^θ − 1)^{−1}||j||_Pc**. Then S^j = S^{j'} + P(b) with D(S^{j'}) = 0
pointwise (since D(P(b)) = ev^{(0→k)T}d*b) and ||j'||_Pc ≤ ||j||_Pc + L^{3+θ}sup|b|; P(b) ≡ (s_{k−1} = b, G_{k−1} =
Σ_b b(b)G_b) is bounded by LIN0/GU; S^{j'} by Theorem COF (sup half (c): no top-residual term). Hence, for **every**
composite-co-closed source in the classes, **||f_0||_∞ ≤ C(||G^c_0||_∞ + [G^c_0]^∞_α + ||j^c_0||_∞ + ||j||_Pc + ||G||_Y +
||s||_R), k- and T-uniformly**, and the Hölder half holds with COF's κ_+||r^c_{k−1}|| term (of S^{j'}'s response, which
differs from S's by LIN0-bounded pieces). This is (CO-fun) exactly as §31.2 states it.
**Correct statement:** (CO-fun) as stated in §31.2 holds on the whole composite-co-closed class, conditional only on the
lane-A inputs that Theorem COF already quotes; [S10-fix 1] (restricting (CO-fun) to (CC-0)) is unnecessary; **(TENT-Q) is
not an obstruction to the curvature half** (it is the representative-dependent defect term, compensated in f_0).
COFUN.md §6.2 (iv)'s "narrowing" and §7's "(CO-fun)[cc] is refuted as stated" are likewise superseded.

### Finding 6 (s10 §35.6, §36.5 (i)) — Corollary COF-crit and Theorem NCE (i): **REFUTED as stated**
Two independent defects.
(a) **[new]** COF-crit (l.4108) says "BFT_A Lemma CD gives Ξ^T𝔑^0 = −K'^T_x∇(𝔉_k∘exp) as an **identity of level-0
functions**, so ∇ = 0 forces D(𝔑^0) = 0 everywhere, the level-k roots included". BFT_A §31.0 (l.2759) defines K_x only for
"ξ with ξ = 0 at level-k roots", and the proof (BFT_A l.2974) begins "For ξ vanishing at the level-k roots": Lemma CD is an
identity **on Λ_*** and gives D^⊥(𝔑^0) = 0 (composite co-closedness), nothing at the roots. The cited lane-A sentence
(BFT_A l.3552, "Lemma CD forces D = 0 only at critical points") is about the pairing with σ ∈ Λ_*, i.e. also off the roots.
At a critical point the exact root value is **D(𝔑^0)(c_X) = κ_{k−1}(d*r_{k−1}(x; B))(X)** (my derivation above, applied to
𝔑^0 = Hx − NB), the linearised top residual's divergence, which the level-k Gauss law makes O(η²) but not 0 (BFT_A's own
Proposition CD2, ARGUED there, lists a level-k end term ev^{(k)T}α_k, α_k = κ_{k−1}w(r_{k−1}, B_k)). So "(CC-0) at critical
points" is **not proven** and is expected false at second order. (By Finding 5 this no longer matters for the sup half:
composite co-closedness suffices.)
(b) [REVIEW_BFT_B_S9_S10 S10-6 — **I agree**, re-derived]: 19.4's row size π_l(R^B_l) ≤ 2C_bchκ_+L²η² is uniform in l
(own |r_l| ≤ L^{−2(k−1−l)}η, |x_l| ≤ L^{−(k−l)}η ⇒ own |R^B_l| ≲ L²L^{−3(k−l)}η²), so ||V||_Pc ≍ L^{θ(k−1)}η² and
Σ_lπ_l(V_l) ≍ (k − 1)η². The k-uniform conclusion does not follow.
**Correct statement:** at a critical point of 𝔉_k (m = 0, trivial background), the rows are composite-co-closed (Lemma CD (i)
on Λ_*), the gauge-fixing remainder vanishes, and by Finding 5 ||f_0||_∞ ≤ C(Σ_lπ_l(V̂_l) + ||W||_Y) = O((k − 1)η²); the
Hölder half additionally carries the top residual; the residual half (§31.2 (a)) is relative to the top residual (its i = k−1
term *is* ||r^c_{k−1}||). Not k-uniform; the k-uniform form needs a level-decay input for the rows (lane A's (SPD)/(W2)).

### Finding 7 (T13) — COFUN.md's "BFT_B l.3810 'with D(S^E_0(S)) = 0' is wrong while l.4203 is right"
Re-derived from the definitions (BFT_B §15.0: Γ_E = Λ = Σ_Xχ^5_Xλ^E_X with λ^E_X(c_X) = 0; λ^E_X(dμ) = −(μ − μ(c_X)) on Ñ_X;
Σ_Xχ^5_X = 1, χ^5_X(c_Y) = δ_{XY}): ⟨d*λ^{E,T}_X f, μ⟩ = ⟨f, λ^E_X(dμ)⟩ gives **d*Γ_E^TD = −D + Σ_X⟨χ^5_X, D⟩δ_{c_X}**, hence
**D(S + Γ_E^TD(S)) = Σ_X Q_X δ_{c_X} = I_χ^TD(S)** as a level-0 function (Σ_XQ_X = ΣD = 0).
- **l.3810 (pointwise reading): FALSE** in general (nonzero whenever some box charge Q_X ≠ 0). **l.3810 (Λ_0 reading): TRUE**,
  and it is the reading l.3810 itself uses ("So every Γ_E-response is a composite-co-closed response", l.3812). BFT_A's own
  proof of Lemma GE (c) (BFT_A l.2951) already separates them: "Ξ^TS^E_0(S) = 0 on Λ_0. **As a level-0 function,
  D(S^E_0(S)) = I_χ^TD(S)**". So l.3810 is a notation collision inherited verbatim from the statement of BFT_A Lemma GE (c),
  not a mathematical error of session 9; it becomes an error only in session 10's notation, where (CC-0) is pointwise.
- **The correct formula is at l.4202, not l.4203** (one-line citation drift in COFUN.md; CODEX_REVIEW_COFUN F8 found the same).
  **l.4203's own sentence** ("Theorem COF applies to S^E_0(S) **except** for Proposition COF-res's residue") is **not
  established** (Finding 5: the "residue" is not a separate term of f_0).
- **COFUN.md's claim: CONFIRMED** for the divergence (pointwise D(S^E_0(S)) = Σ_XQ_Xδ_{c_X}, so the corrected source is in
  (cc) ∖ (CC-0) unless every box charge vanishes); **NOT-VERIFIED/over-stated** for "l.4203 is right".
- **Does it decide whether Theorem COF can stand in for BFT-5 clause (b)?** **No — it does not decide it, in either
  direction.** (i) Read alone, Theorem COF (hypothesis (CC-0)) does not cover the (cc) sources that clause (b) quantifies over
  (l.3831: "every composite-co-closed source S (Ξ^TS = 0, §27.1)") and that route (i) produces — COFUN.md and
  CODEX_REVIEW_COFUN F7 are right about that. (ii) But by Finding 5, Theorem COF **plus** the exact root-dipole identity and
  LIN0/GU covers the whole of (cc) for the level-0 curvature at m = 0 on the trivial background, so the (cc)∖(CC-0) gap
  costs nothing for the sup half. (iii) What actually prevents Theorem COF from standing in for clause (b) is clause (b)'s
  scope: it is at the background Z(V_k) (COF is at the trivial background), it asks for the full 𝔐-pair bound
  ||x||_𝔐 ≤ C_5||S||_{𝔐*} and BFT-3's weighted locality (COF bounds f_0 only, at m = 0), and for the rows the (Pl-c) class
  norm carries the level-count factor (Finding 6 (b)).

### Finding 8 (T6, T7, s10 §36) — (GT-sup), Lemma ΓT-op (d), the spike-support headline
**Lemma ΓT-op (d) and its constant (§25.1 (d), used in §36.2): CONFIRMED.** For z ∈ Ñ_X, λ^E_X(x)(z) = ⟨(λ^E_X)^Tδ_z, x_0⟩
with (λ^E_X)^Tψ = −d_XG_X(ψ − ⟨ψ⟩δ_{c_X}) (re-derived from the pinned box-Neumann minimisation), ||(λ^E_X)^Tψ||_1 ≤
M_n||ψ − ⟨ψ⟩δ_{c_X}||_1 by the reflection torus of side M_n = 2(4n + 1) and Lemma N1G's Σ_y|∇_μG_M(y)| = M/4; for ψ = δ_z,
||δ_z − δ_{c_X}||_1 = 2, so |λ^E_X(x)(z)| ≤ 2M_n·max_{Ñ_X}|x_0| and 2M_n/n = 16 + 4/n ≤ 20 for every n ≥ 1 — **absolute**
(r55b_num N3; N3 also re-derives the 1D Green identity behind N1G: −Δg = δ_0 − 1/M and 2(g(0) − g(M/2)) = M/4 exactly for
g(t) = (t − M/2)²/(2M)). The per-line total variation = 2(max − min) step needs the coordinate-line monotonicity of G_M
(REVIEW_BFT_B_S7 B.2), quoted, not re-derived.
**Proposition GT-loc, the inequality (§36.2): CONFIRMED** (convex combination over ≤ 2^d boxes, then (d)).
**Proposition GT-split (§36.1): CONFIRMED** (λ = Λ(Y_*) vanishes at level-k roots by the pin and χ^5_X(c_Y) = δ_{XY}).
**The headline "(GT-sup) is not a question about where the spikes of λ^{Γ_E}_* sit … What (GT-sup) needs is (Y-sup^loc)"
(l.4168): REFUTED.** (Y-sup^loc) is **false, for every representative**, on the boxes whose tents see p: the curvature
dY^p_0(p) is gauge-invariant, and minimising E(Y) = ½⟨Y, HY⟩ − ⟨δ_p, dY_0⟩ against the trial Y = t·(one link of ∂p) gives
dY^p_0(p) ≥ 1/a with a ≤ 6 + 8κ_+ (k-independent), so some link of p carries own |Y^p_{*,0}| ≥ 1/(4a), i.e. coarse size
≥ n/(4a). GT-loc therefore gives sup|λ| ≲ 20n/(4a) near p — useless exactly where §36.2's own S10-F6 paragraph says D^⊥(S)
generically lives. A k-uniform (GT-sup) near p, if true, must come from the fine structure of λ (lane A's measured spike
σ ≈ 0.003 is O(1/n) of this bound) — i.e. it **is** a question about λ's structure where D^⊥ sits. Correct statement:
"(GT-sup) ⟸ (Y-sup^loc) with constant 20 (PROVEN); (Y-sup^loc) fails on the core boxes for every representative; (GT-sup)
is OPEN and, on supp D^⊥ ∩ (core boxes), not reducible to a field sup bound." (REVIEW_BFT_B_S9_S10 S10-14 called the
headline NOT-VERIFIED via a free-field count; the gauge-invariant lower bound above makes it a refutation. I agree with
S10-14's direction and S10-15's critique of [S10-fix 2].)
**Proposition GT-ell (§36.4) "PROVEN as an implication": REFUTED as written; CONDITIONAL in corrected form.** l.4185
"Choose Y^p_* := the 𝒩-minimising representative" uses Theorem YH's 𝒩, whose minimisation is over **all** level-0 λ
(BFT_A §26.0). If the optimal λ_opt ∉ Λ_0, Y_* = Y + Ξλ_opt is not a representative in NCR's sense, and the identity
n²⟨D, λ^{Γ_E}_*(p)⟩ = n²⟨Γ_E^TD^⊥, Y_{*,0}⟩ acquires the extra term n²⟨D^⊥, λ_opt − I_χλ_opt⟩ (from Λ(x + Dμ) =
Λ(x) − μ + I_χμ, BFT_B §16.1 (a)). Correct form: replace 𝒩(Y^p) by 𝒩_{Λ_0}(Y^p) — COFUN.md's (YH-pin), OPEN; by
CODEX_REVIEW_COFUN F3 it imposes T⁴ − 1 root constraints, not one. S10-16 CONFIRMED GT-ell without this — I disagree.
**Proposition GT-attr (§36.3): ARGUED**, arithmetic L^{3l−k} re-done, CONFIRMED; the step to "(GT-sup) expected TRUE"
inherits the refuted headline (agree with S10-15).
**§36.5 (ii) "the whole of (NC-Γ) for Γ_E off the critical set reduces to one scalar per level-k box": NOT-VERIFIED / over-
reduced.** Its face (b) (COF-res's root charge) is void by Finding 5; its face (a) uses π_0(Γ_E^TD(S)) ≤ 5^d[(M_n/4)n³||D||_∞
+ 2^dC_∞n³max|Q_X|], whose **first** term is ≍ n⁴||D^⊥||_∞, for the rows ≍ n⁴·L^{−3(k−l)}η² = L^{k+3l}η² at level-l roots —
not small either. The box charge is not the only obstruction on that route.

### Finding 9 (s9 §31-§32) — Proposition NCR, (R2), BFT-5_E, BFT5-red, Rω-frame
**Proposition NCR (§31.1): CONFIRMED** as an identity (with the n² of BFT_A §26.0's convention: f_0^Γ(S)(p) − n²⟨S, Y^p_*⟩ =
n²⟨D(S), λ^Γ_*(p)⟩). **(R2) (§31.3) as an inequality omits n²**: |remainder| ≤ n²||D(S)||_1·sup|λ| (agree with S9-15), so
"(NC-Γ)_cc + (GT-sup) ⟹ (NC-Γ) for Γ_E" needs a third input, a bound on n²||D^⊥(S)||_1. **Statement (BFT-5_E) clause (c)
"PROVEN (Proposition NCR)": REFUTED at the stated scope** — NCR uses Ker H = Ran Ξ at the trivial chain; at Z(V_k) it is
CONDITIONAL on the background analogue ((N1-nd) of §40.3) and, by §40.2, Λ_0 loses its quotient (agree with S9-18).
**Proposition BFT5-red / (G♯-patch^Ω) narrowing: NOT-VERIFIED as "PROVEN as bookkeeping"** (agree with S9-19: SF's Lemma
G-pert needs the data small in one gauge and bounds the trivial-slice Hessian; the slice change is unnamed).
**Lemma Rω-frame: ARGUED** — status honest; spot-checked only.

### Finding 10 (T8, s11 §41.2) — Theorem BGD: the B1/B2 defects and "slot-wise, weight-free, factor-k-free"
**(a) the exactness defect B1: CONFIRMED** (identity and size). Expanding d_Z of d_Zλ on the four legs of p (transports to
the base corner), the single-transport terms cancel in pairs and (d_Zd_Zλ)(p) = (Ad_{Z1Z2} − Ad_{Z4Z3})λ(far corner) =
(U_1 − U_2)λ(c); ||U_1 − U_2||_F² = 6 − 2tr(U_1^TU_2) = ||Ad_W − 1||_F² for SU(2)'s adjoint. Size ≤ c_N|log W_p|_own =
c_Nρ_j²|F_j(p)| ≤ c_NC_Nρ_j²f_k given (N2-0)(a) (quoted from §22, not re-derived).
**(b) the root-covariance defect B2: REFUTED as written.** (41.2)-(41.3) are stated for "Q_{str,l}^Z", which §38.1 defines
as the covariant version of lane A's straight map — the block average L^{−4}Σ_{y∈B(X)}Σ_{j<L} of straight legs (BFT_A §7.1,
BL-2 (a)). For that operator the claim fails **already at Z = 1**: Q_{str,l}dλ = d(avg_Bλ) (from Q_{str,l} = Q_l + d h_l and
h_l(dλ) = avg_Bλ − evλ), not d(evλ), although the trivial background is a straight-row tower. The identity (41.2) is true for
the **root-to-root single-line map Q_ax** — and that is what bb11 implements: `checks/bb11_bgd.py` l.220-233, `Qstr` sums the
L transported links of the one line from the root c_X (no block average, no L^{−4}). So bb11 A4a/A4b **cannot detect** the
mislabel (systemic defect 3). For the operator the session-9/10 skeleton actually uses — lane A's S4′ contour map Q_l^Z —
the exact defect is (telescoping along each contour T, transports to c_Y): **(Q_l^Zd_Z ev^{(l)}λ − d_Z ev^{(l+1)}λ)(Y, μ) =
(avg_{σ,y}Ad_{hol(T^σ_y)} − Ad_{Z_{l+1}(Y,μ)})·lam_{l+1}(Y + e_μ)**. It is **not** zero on a straight-row tower at a curved
background (avg Ad_{h_i} − Ad_{h̄} = ½Ad_{h̄}·avg(ad X_i)² + O(X³) ≠ 0 whenever the contour holonomies h_i = h̄e^{X_i} differ,
i.e. whenever there is curvature inside the block). So "root covariance holds EXACTLY iff the background is a straight-row
tower … the property §25.5 proves for Z^off" is false for Q_l^Z, and every downstream "exact on Z^off" (§41.3 item 2;
TRANSP step 1; FOR OTHER FILES "FLOW/HIST": "Z^off is a straight-row tower, so the defect is zero for it") inherits the error.
The size claim (41.4) survives only in a cruder form: |defect|_own ≤ c_N(spread of contour holonomies + |r_l(Z)|) ≲ Cρ_{l+1}²f_k
(first order, no L^{−θ(k−l)}), plus the stated (C_g-θ) term; this is what (c) actually needs.
**(c) "level-diagonal-relative, so they cost a factor and not a weight … no factor k" (l.4550; §43.4): REFUTED as a proof.**
The argument writes each defect as E = e_l·𝒪 with 𝒪 an operator already bounded in 𝔐. Neither defect is of that form: B1
perturbs d∘d = 0 (there is no 𝒪 to be relative to), and B2 is bounded relative to the **values** lam_{l+1}(Y + e_μ), not to
the output of d_Z ev (at a curved background d_Z ev λ can vanish on a link — λ parallel along it — while the defect does not).
Both are bounded relative to the input function's sup, which is not a quantity 𝔐 controls. Each use must therefore be priced
on its own; I spot-checked the one in Lemma RT-cc's cascade (d*Q^Tρ = ev^Td*ρ + E^Tρ adds e_l|ρ_l| to ψ_l, i.e. ≲ L³f_k|ρ^c_l|
in coarse plain units after h_l^T) and it is affordable; the one in §41.3 is mis-priced (Finding 11). "No factor k, no weight
penalty" is NOT-VERIFIED as a general statement.

### Finding 11 (s11 §41.3) — the slot decomposition at a background: **REFUTED**
§41.3 (l.4558-4563) says D_Z(S^G) = Σ_l ev^{(0→l)T}d_Z^*d_Z^*G_l is "root-supported, so by Proposition GT-split it never enters
the gauge-fixing remainder" and "by COF-res feeds (TENT-Q)". The term with index l is supported on the level-0 images of the
**level-l** sites (for l = 0: every level-0 site); GT-split's partition is D^root = D·1{**level-k** roots} vs D^⊥. So
D^⊥_Z(S^G) ≠ 0 in general: **S^G is not composite-co-closed at a curved Z**, its response is gauge-fixing-dependent, the
off-root part **does** enter the remainder, and Lemma SPLIT's slot superposition does not transport (the session's own §40.3
(2) says the G-slot is not ⊥ 𝒢_0^Z — §41.3 contradicts it). §41.3 item 2 ("D_Z(S^s) = 0 exactly for Z = Z^off") is wrong
twice: pointwise it already fails at Z = 1 for the top slot (Finding 4, r55b D5), and exactness on Z^off fails for Q_l^Z
(Finding 10 (b)). Correct statement: at Z ≠ 1 the G- and s-slots are composite-co-closed only up to O(f_k)-size divergences
supported off the level-k roots; a slot-wise theorem at Z needs those divergences moved into another slot (e.g. by a local
Bogovskii completion, whose per-cube neutrality ⟨G, d_Zd_Z1⟩ ≠ 0 at a curved background is not automatic) — not done.

### Finding 12 (T9, s11 §41.5) — Proposition NL-GLOB
**(i) "No gauge makes a background with F_Z ≠ 0 translation invariant" (l.4587): REFUTED as a universal sentence** — agree with
CODEX_REVIEW_GAPZ F12: constant links Z_μ(x) = g_μ with g_1g_2 ≠ g_2g_1 have constant nonzero plaquette holonomy and are
translation invariant. **The narrow obstruction is CONFIRMED**: by Lemma CONJ conjugation intertwines exactly only at flat
backgrounds (curvature is gauge-invariant), so Theorem 4.2′'s scalar-symbol strip argument does not transport to the general
curved Z^off(V) by conjugation. **(ii) the Combes-Thomas locality half: ARGUED** — agree with the file and with CODEX_GAPZ F5
(the mechanism is sound; the uniform a(m), the 𝔐^∇_Z → Y_Z pair and the composition with Lemma 3.1 (c)'s local maps are
missing). **(iii) "(GAP-Z) is not a new item: it is BFT-5's input (1)": see Finding 15.**

### Finding 13 (s11 §41.4) — Lemma FR-price: **NOT-VERIFIED**
Step 3 proves a **sup**-relative bound (|δλ| ≤ c_NC_1f_kn^{−1}sup|λ| and sup|λ| ≤ 8sup|∇^cλ|, so sup|δλ| ≤ 8c_NC_1f_k
sup|dλ|_own) and then asserts "in the quadratic form Σ|x_0 + d_Zλ|² the operator d_Z differs from d by a relative 8c_NC_1f_k".
That does not follow: on the pinned box in d = 4 a near-constant λ ≈ a with a dip at c_X has ||dλ||_2² ≍ a² (point capacity)
while ||δλ||_2² ≍ (f/n)²a²n⁴, so the ℓ²-relative size is ≍ n·f, not O(f). A Neumann series needs a *preconditioned* bound
||A^{−1}E|| < 1 (CODEX_REVIEW_GAPZ F7's point, which applies here verbatim); in sup norm the d^*δ part is fine
(||(d^*d)^{−1}d^*||_{∞→∞} ≲ 16n by ΓT-op (d)), but the δ^*d part costs ||(d^*d)^{−1}||_{∞→∞}·(f/n) ≍ n²·f/n = n f unless the
Coulomb structure of the box normal form (d^*log Z ≈ 0) is used, which is not written. The conclusion may be true; the proof
is missing this step. Not tested by bb11 (limitation 2 says so).

### Finding 14 (T11, s11 §41.6) — Theorem TRANSP "PROVEN as an implication … GIVEN exactly two inputs: (GAP-Z) and (N1-nd)": **REFUTED**
Read against its own proof (l.4600-4609), TRANSP consumes, besides (GAP-Z) and (N1-nd):
1. **§41.5 (ii)** (Combes-Thomas locality) in step 3 — **ARGUED** by the file's own label (agree with CODEX_REVIEW_GAPZ F6);
2. **(N1-e) at Z** (§41.7) in step 5 — **ARGUED** by the file's own label (CODEX F6 — agree);
3. **(C_g-θ)** through Theorem BGD (b)'s size (41.4) and through Lemma FR-price's input Corollary CL-iv (whose 𝔐^∇ residual term
   is at Cg-NL's status: BCH remainder **ARGUED**) — not listed;
4. **Theorem BGD (b)/(c)** — (b) is about the wrong operator and its "exact on Z^off" is false for lane A's Q_l^Z, (c)'s
   general mechanism is not a proof (Finding 10);
5. **Lemma SPLIT at Z** (step 4) — fails: S^G is not composite-co-closed at a curved Z (Finding 11), so slot-wise use of W0/GU/
   LIN0 does not transport; this is also why step 1's "LIN0 … transports with no new input" and Proposition SIX-RED (i)'s
   "LIN0 is Tier A only" are wrong (LIN0 is a slot-wise superposition, whose legitimacy at Z is a Tier-B (d_Z^*d_Z^* ≠ 0) question);
6. **Lemma FR-price** — NOT-VERIFIED (Finding 13).
And, by the session's own logic (§41.3 routes the S^G residue to (TENT-Q), "OPEN"), TRANSP would also have to list (TENT-Q).
**Correct status:** a programme sketch — "(H-inv+)_Z for composite-co-closed sources at Z ⟸ (GAP-Z) + (N1-nd) + §41.5 (ii) +
(N1-e) + (C_g-θ) [BCH ARGUED] + a correct root-covariance defect estimate for Q_l^Z + a slot decomposition at Z +
Lemma FR-price's preconditioned Neumann step" — **ARGUED, not PROVEN as an implication.** CODEX F6's further point (TRANSP is
at Z^off(V), m = 0, T ≥ 17, composite-co-closed sources; its consumers need the critical chain and a chart) — agree.

### Finding 15 (T12, s11 §41.5 (iii), §43.3 item 4) — "the nontrivial background collapses into BFT-5"
**The identification "(GAP-Z) is BFT-5's input (1), (G♯_0-field), moved off the trivial chain … they are ONE obstruction":
REFUTED.** BFT-5's input (1) (§32.2 l.3839ff) is (G♯_0-field): (G♯) for the chain Hessian **at the trivial chain**, in the §33
pair. (GAP-Z) (§38.1 l.4334) is a k-, T-uniform bound "on the kernel of the gauge-fixed composite chain Hessian **at Z** —
equivalently a lower bound for 𝓛_Z on the slice, with no decay claimed". These differ in background, slice, norm and output;
the "equivalently" is itself false for an entrywise kernel bound (CODEX_REVIEW_GAPZ F10's K_n = I + 11^T: entries ≤ 2, smallest
eigenvalue of K_n^{−1} = 1/(n+1)); and Theorem 4.2′'s M bounds selected response kernels, not a full inverse (CODEX F2's scalar
witness F = a(x − b)²/2, a = 1/n — agree). Within BFT-5's own reduction (§32.2), the background bound is an **output** of
(1) + Lemma G-pert + (G♯-patch) ("the B-NA wall itself"), not input (1). **What survives (CONFIRMED as a dependency
observation, not a theorem):** TRANSP's sketch needs a uniform background propagator bound of the kind BFT-5 (a) asserts, so
BFT-0/1/2 at a nontrivial background and BFT-5 are not independent. PROOF.md's later [S25-fix 2] already withdraws "ONE"; I
agree with withdrawing it and, with CODEX GAPZ, do not accept any replacement count (TWO/THREE) as a theorem.

### Finding 16 (T10, s11 §42) — Lemma GZ-SLOT, **Proposition GZ-FALSE: REFUTED**, Theorem Cg-nr, (CURV-dec)
**Lemma GZ-SLOT (l.4621): REFUTED.** Its derivation starts "𝔉_k = Σ_j F_j with F_j = E_j^{br} + κ_jΣ_cφ̂_c (REVIEW_S22
l.395)". That is not the functional. BFT_B §0 takes 𝔉_k "as in PROOF [S19]-[S22]", i.e. TOWER-VAR (PROOF l.6633-6635; BFT_A
l.21): **𝔉_k = S_W(U_0) + Σ_{j<k}κ_jΣ_cφ̂_c(M̄^{(j)}(U_j); U_{j+1}) — "Wilson at level 0, one soft term per level"**. F_j =
E_j^{br} + κ_jφ̂ is the per-level tower functional (TOWER-VAR (a): E_k^{br} = 𝔉_k(tower), and E_{j+1}^{br} is the F_j-value);
Σ_jF_j over-counts every lower level and is not 𝔉_k; and E_j^{br} (j ≥ 1) has no "plaquette (Wilson) part". Differentiating
the actual 𝔉_k at Z: the level-0 component is the Wilson current d_Z^*F_0(Z) plus the soft gradient; every level-j ≥ 1
component is a soft (residual-type) gradient, κ_j(Q^Z_j)^T r_j(Z) − κ_{j−1}r_{j−1}(Z) up to Jacobian factors. **There is no
level-j ≥ 1 divergence-form slot with 2-form F_j(Z).**
**Proposition GZ-FALSE (l.4626-4633): REFUTED**, for three independent reasons:
(1) its lower bound ||g_Z||_Y ≥ max_{0≤l≤k−1}L^{θ(k−l)}f_l uses the l ≥ 1 curvature slots that g_Z does not have;
(2) at l = 0 the (G)-slot weight is **ω_0 = 1**, not L^{θk} (BFT_A §1.4 l.36, §7.2 l.467: "ω_0 := 1, ω_l := L^{θ(k−l)}"), so the
one curvature slot g_Z does have carries no θ at all: its Y-size is ||F^c_0||_∞ + [F^c_0]_α = f_0 + [F^c_0]_α ≤ C_Nf_k +
(Hölder of the level-0 field, which (CovLift) (iv)'s **first** clause / Corollary CL-iv bounds by C||b||_∞);
(3) even granting a level-l curvature representative, §42.3 (i) of the same session says the Y-size of a source "is the
infimum over its admissible slot decompositions … This reading is forced, not optional", and a fixed-representative lower
bound is not a lower bound on that infimum (at an exact critical lift g_Z = 0 while the fixed-representative "size" is not 0).
The "for every lift" step ("any lift with less curvature … contradicts the maximality of θ_w^c = 2", l.4632-4633) is a non
sequitur (maximality of a proven weight says nothing about other lifts); a correct version of the fixed-representative
statement would use the coarse averaging relation (f_l ≳ f_k for lifts with small residuals), but that statement no longer
bears on (CovLift).
**Correct statement:** (CovLift) (iv)'s clause ||g_Z||_Y ≤ C_g||b||_∞ at θ > 0 has **no** non-residual θ-problem: its
non-residual part is the level-0 Wilson current (weight 1) plus BCH/Jacobian terms of the soft gradients; its θ > 0 content
is exactly **(C_g-θ) for the residual slot** — Proposition Cg-lin PROVEN (linear lift), Cg-NL first order PROVEN + BCH
remainder ARGUED (§21.2/§22.9, quoted). REVIEW_BFT_B_S5's "θ = 0 status" for the non-residual components is consistent with
this (they never carried θ).
**Theorem Cg-nr and (CURV-dec):** the arithmetic of (ii) (ω_lδ_l = C_LL·L^{−(1−θ)(k−l)}(1 + (k−l)f_k)f_k, bounded in l for
θ < 1) is CONFIRMED as arithmetic, but the theorem addresses a slot g_Z does not have; **(CURV-dec) is not an input of
(CovLift)** and should not be carried as an open item for it. **Remark TWO-W** (a reading) falls with GZ-FALSE.
**Consequence for PROOF.md:** "[S24-note 3] (CovLift)'s non-residual g_Z clause at θ > 0 is FALSE … The search for a better
lift is foreclosed" (PROOF.md l.158-161) and the S24 follow-on headline's "(CovLift)'s θ > 0 clause … REFUTED or struck"
(l.6945) must be withdrawn.

### Finding 17 (s11 §39-§40, spot-checks) — AUDIT, SIX-RED, N1-alg, (N1-d), N1-CONS
- **Theorem N1-alg narrowed (a′)-(g′): CONFIRMED** (re-derived (a′) by ν = λ + μ with μ(c_X) = 0; (f′) covariantly constant
  sections are fixed by their value at c_X on a connected box; (e′) Λ_Z(Ξ_Zμ) = −μ). The disclosed bb11 A5 FAIL and the
  corrected (40.1) are right (d_Z of a constant is (Ad_Z − 1)c ≠ 0). **"Λ_0 cannot be read modulo constants at Z ≠ 1": CONFIRMED.**
- **(N1-d) ⟸ (N1-nd) (§40.3): spot-checked**, linear algebra as stated; but its step (2) correctly notes the G-slot is not ⊥
  𝒢_0^Z, which contradicts §41.3 (Finding 11).
- **Proposition AUDIT / SIX-RED: spot-checked; SIX-RED (i) "LIN0 is Tier A only … carries no background hypothesis" is
  REFUTED** (LIN0 superposes slot responses; at Z ≠ 1 a G-slot is not composite-co-closed, a Tier-B (B1) matter — AUDIT's own
  (B1) entry lists Lemma SPLIT's D(S^G) = 0).
- **Proposition N1-CONS: spot-checked** (bookkeeping; not re-judged).

### Finding 18 (T14) — the earlier review REVIEW_BFT_B_S9_S10.md, item by item where it bears on my verdicts
| its item | its verdict | mine | reason |
|---|---|---|---|
| S9-1 RT-cc (a) | CONFIRMED | agree (one imprecision) | "At l = k−1, Ψ_{k−1} = D(S)" misses ev^{(0→k)T}d*s_{k−1}; harmless for support |
| S9-5/6/7 FT, RHT-cc, K_f | CONFIRMED | agree | re-derived; K_f bracketed exactly (r55b_num N1) |
| S9-11 RHT-V hidden top-residual hypothesis | CONFIRMED-WITH-FIX | agree | Finding 1 |
| S9-13 (H-inv+) bookkeeping | CONFIRMED-WITH-FIX | agree; add G♯R window θ ≤ 1−α | Finding 2 |
| S9-15 missing n² in (R2) | binding | agree | Finding 9 |
| S9-16 λ has no level-k-root part | WRONG (of §31.1 Reading 2) | agree | pin + χ^5_X(c_Y) = δ_{XY} |
| S9-17 residual half "k-, T-, level-uniform" | CONFIRMED | **disagree in part** | its i = k−1 term is the top residual itself; same caveat as S9-11 |
| S9-18 BFT-5_E (c) at the background | WRONG at stated scope | agree | Finding 9 |
| S9-19 BFT5-red narrowing | NARROWED | agree | — |
| S10-1 W0-use; "(CC-0) ⟺ ψ_{k−1} = 0 ⟺ r_{k−1} co-closed" | CONFIRMED | agree on W0-use; **the chain is wrong** | (CC-0) ⟺ d*r_{k−1} = 0 ⟺ ψ_{k−1} = −d*s_{k−1}; ⟺ ψ_{k−1} = 0 only if d*s_{k−1} = 0 |
| S10-2 Lemma SPLIT | CONFIRMED | **disagree** | top residual slot has D(S^s) ≠ 0 pointwise (Finding 4; r55b D5, D7) |
| S10-3/4/5 DF-cc, ξ_i = −ψ_i, COF-size | CONFIRMED | agree (with D(S^j) and ĵ_0 conventions) | Finding 4 |
| S10-6 COF-crit wrong (level count) | WRONG | **agree**, and add a second defect | Finding 6 (a): Lemma CD is on Λ_* only |
| S10-7 NCE (i) NARROWED | NARROWED | agree; I record REFUTED-as-stated | Finding 6 |
| S10-9 COF-res identity | CONFIRMED | agree | Finding 5 |
| S10-10 "every other term bounded" | NOT-VERIFIED | agree | the main object is not co-closed (d* = block-average density) |
| S10-11 "(CO-fun) FALSE without (CC-0)" | CONFIRMED | **disagree — REFUTED** | contradicts its own S10-10; exact dipole identity + LIN0/GU bound f_0; general case by flux decomposition (Finding 5) |
| S10-12 MASSLESS | CONFIRMED | agree (spot-check) | shell count Σ_{r≤N}r³r^{−3} = N |
| S10-13 GT-split | CONFIRMED | agree | — |
| S10-14 GT-loc headline | NOT-VERIFIED | agree in direction; I record REFUTED | gauge-invariant lower bound on dY^p_0(p) (Finding 8) |
| S10-15 GT-attr | arithmetic CONFIRMED, conclusion NOT-VERIFIED | agree | — |
| S10-16 GT-ell | CONFIRMED as an implication | **disagree** | 𝒩-optimal gauge need not lie in Λ_0 (Finding 8) |
| S10-17 D(S^E_0) = I_χ^TD | CONFIRMED | agree | Finding 7 |
| S10-18 NCR is an identity not a bound | WRONG (of §36.5 (v)) | agree | — |
| Part P (discriminating power) | — | spot-checked only; I add: bb9b/bb10 have s = G = 0 and cannot see the Lemma SPLIT defect; bb11 A4 tests Q_ax, not the operator BGD (b) names | systemic defect 3 |
Net: the earlier review was right on the level-count (S10-6) and on most scope items, but **confirmed a wrong refutation
(S10-11)** while holding the premise it needed NOT-VERIFIED (S10-10), **confirmed Lemma SPLIT pointwise (S10-2)**, **confirmed
GT-ell (S10-16)**, and **did not see that Lemma CD is restricted to ξ = 0 at the level-k roots** (it wrote "(CC-0) at
critical points rests entirely on Lemma CD (i)" without checking the domain). Session 11 it did not review.

### Finding 19 (T15) — the Codex gpt-6-astra/max reviews, verdict by verdict where they bear on this batch
Both files read in full as they are on disk now; both are complete (GAPZ ends with its summary table; COFUN ends with its
SHA-256 lines).
**CODEX_REVIEW_GAPZ:** F1 (Z = 1 is a legitimate specialisation; the class is underspecified) — **agree**. F2 ((GAP-Z)|_{Z=1}
≠ Theorem 4.2′'s M; response bound ≠ inverse bound; scalar witness) — **agree** (Finding 15). F3/F4/F5 (status arguments are
not non-implication proofs; counts not theorems; CT mechanism plausible) — **agree** (outside my sections except as used in
Finding 15). F6 (TRANSP not PROVEN from exactly two inputs; §41.5 (ii) and (N1-e) ARGUED; class/chart mismatch) — **agree**,
and I add four further defects (Finding 14). F7 (preconditioned Neumann bound needed, not ||E||/||H_0||) — **agree**; it is
directed at NBG_A's HESS-rel but the same gap is in Lemma FR-price step 4 (Finding 13). F8, F9 — outside my batch (NBG_A),
not adjudicated. F10 (collision table; "kernel bound … equivalent to a lower bound" false for entrywise bounds) — **agree**
(it is at BFT_B l.4334, inside my batch). F11 — agree (no check in BFT_B tests Tier C). F12 (curved translation-invariant
backgrounds exist) — **agree** (Finding 12).
**CODEX_REVIEW_COFUN:** F1 (CO-pin cancellation on Λ_0) — agree. **F2 (no independent blow-up; term-to-total inference
invalid; "(CO-fun)[cc] FALSE" NOT-VERIFIED)** — **agree, and I go further**: the estimate is *true* given Theorem COF
(Finding 5), and Codex's own F4 dipole is the example whose f_0 is bounded. F3 (T⁴ − 1 root constraints) — agree; it bears on
GT-ell's corrected form (Finding 8), not on my Finding 5 (which needs no pinned minimisation). F4 (ROOT-sup fails; printed ≥
should be ≤) — agree; ROOT-sup's failure (π_0(C(j)) unbounded) is consistent with f_0 bounded, because C(j)'s large part is
cancelled in the pairing. F5 (A ≠ C; ⟨A, dλ⟩ = 1/81) — agree; it is the same fact as my "main object not co-closed".
F6 (no equivalence TENT-Q ⇔ ROOT-sup) — agree. **F7 (classes (lw) ⊂ (CC-0) ⊂ (cc); clause (b) quantifies over (cc); a
(CC-0) theorem does not discharge it)** — agree for Theorem COF read alone; see Finding 7 (ii) for why the gap costs nothing
for f_0. **F8 (l.3810 erratum supported; formula at l.4202, not 4203; l.4203's sentence not validated)** — **agree**
(Finding 7). F9 (sharp h^T norms 1/3, 8/3) — agree (they sharpen, do not contradict, Lemma FT). F10 ("funnel only adds" false;
universal level-count no-go not proven) — agree; it does not disturb S10-6's upper-bound loss. F11-F13 — about COFUN.md/cf1
only, outside my batch, not adjudicated. **F14 (ĵ_0 collision)** — agree (Finding 4). **F15 (Lemma SPLIT pointwise
identity NOT-VERIFIED)** — agree, and settled here as REFUTED for the top residual slot (r55b D5, D7).

### Finding 20 (T16) — numbers that changed a decision (currency and evaluation point)
| number | where | verdict | note |
|---|---|---|---|
| K_f = 2d/(1 − L^{−(2+α)}) = 8.737 | §29.3 | CONFIRMED | r55b_num N1: K_f ∈ [8.73763, 8.73773] at d = 4, L = 3, α = ¼; printed 0.08434 for 3^{−9/4} is a typo (true 0.08443) |
| c_w = 14 | §29.5 | CONFIRMED as an upper bound (spot) | 12 suffices (S9-8) |
| C_C base 1 + 2d(1 − L^{−3})^{−1} = 9.31 | §35.4 | CONFIRMED | = 121/13 ≤ 9.31 exactly (r55b_num N2) |
| 2M_n/n ≤ 20 | §25.1 (d), §36.2 | CONFIRMED | = 16 + 4/n (r55b_num N3), absolute |
| C_∞ ≤ 1.71 | §36.4 | CONFIRMED as a bound, 13.7× loose | exact max|∇G_M| = (1 − M^{−4})/8 ≤ 0.125 by [RBB8-fix RS8-5] (agree S10-16) |
| "≍ L^{2k−3}π_{k−1}(j_{k−1})" | §35.7 | REFUTED as a size of f_0 | size of one term of a representative-dependent split (Finding 5) |
| ≍ 25(k−1) level-count factor | S10-6 (review) | upper-bound arithmetic CONFIRMED; the θ* = 1/((k−1)ln L) optimiser is inadmissible for large k at fixed α (CODEX_REVIEW_COFUN F11 — agree) | the O(k) of the direct sum stands as an upper-bound loss |
| T ≥ 17 | §41.4 | CONFIRMED as arithmetic (spot) | Ñ_X coarse side 4 + 2r_Z ≤ 12 ⇒ frame side ≥ 16 |
| 8 in "sup|λ| ≤ 8 sup|∇^cλ|" | §41.4 step 3 | CONFIRMED as a sup bound (spot) | the step it feeds is NOT-VERIFIED (Finding 13) |

### Finding 21 (T17) — BFT_B_LOG.md sessions 9-11
The log's "Results by name" (l.471-495, l.530-567, l.604-680) match the sections' status lines one for one (spot-checked every
headline item), so they carry the same errors: session 9 "Lemma SPLIT"-free but RHT-V's absolute η²; session 10 "Lemma SPLIT
PROVEN-HERE", "Corollary COF-crit … (CC-0) holds at critical points (Lemma CD (i) is an identity of level-0 functions)" (§37.2
row), "(CO-fun) as stated … FALSE without (CC-0)", "GT-loc … not a question about spike support at all", "GT-ell PROVEN as an
implication"; session 11 "root covariance is EXACT iff … straight-row tower", "both defects … no weight penalty, no factor k",
"§41.3 … never enters the gauge-fixing remainder", "TRANSP … from (GAP-Z) + (N1-nd) alone", "GZ-FALSE … FALSE at every θ > 0
for EVERY lift", "(GAP-Z) is NOT a new item … ONE obstruction". Provenance claims (file order, byte counts) not re-audited
(S9-P1/S10-P2 of the earlier review cover them).

### Finding 22 (s10 §35.1, re-read against BFT_A §28.5 l.2465-2494 directly) — Lemma W0-use
Steps 1, 2, 4, 5 are classified correctly (step 2's "for every λ" is the co-closedness use (A); step 4's plain slot enters only
through sup|h|, and the Hodge step needs only the total J_0 co-closed). **"Used in exactly two places" is REFUTED:** step 3's
top bound (BFT_A l.2475-2477, "|r_{k−1}(b)| ≤ sup|G_0|Σ_q|dY^{(b)}_0(q)| + sup|j_0|𝒩(Y^{(b)})") replaces ||Y^{(b)}_0||_1 by
𝒩(Y^{(b)}), which is a third use, of type (A), on the top response Y^{(b)}. §35.1 (and S10-1) describe step 3 as using
co-closedness "only through r_{k−1}". **Not load-bearing for Theorem COF**, which keeps κ_+||r^c_{k−1}||_∞ on its right side
instead of running Lemma TOPD (COF note (4)); it matters for removing that term, which would need C(j) co-closed (available
under (CC-0), and for (cc) sources after the flux decomposition of Finding 5) plus Corollary FP's bound on 𝒩(Y^{(b)}) —
plausible, not done here.

---

## Systemic defects found in this batch (brief §"Three systemic defects")
1. **Symbol collisions (load-bearing ones):**
   - **D(S)** = functional on Λ_0 (BFT_A §26.0) vs level-0 function (BFT_A §31.0, BFT_B §27.1): origin of the l.3810 dispute,
     of COF-crit's "(CC-0) at critical points", and of Lemma SPLIT's pointwise claim.
   - **(CC-0)** vs **ψ_{k−1} = 0**: they differ by d*s_{k−1} (Findings 4, 18).
   - **ĵ_0** (l.3590 ĵ_0 := j_0 vs l.4045's ĵ_0 = j_0 + h_0^Tψ_0) — CODEX F14.
   - **Q_str** (lane A's block-averaged straight map, BL-2 (a)) vs the **root-to-root line Q_ax** (§15.0): Theorem BGD (b)
     and bb11's `Qstr` use the second under the name of the first (Finding 10).
   - **"root-supported"**: level-l roots vs level-k roots (§41.3, Finding 11).
   - **Λ_0** mod constants (trivial background) vs pinned Λ_0^Z (§40.2) — handled correctly by session 11.
   - **(G♯_0-field)** (trivial chain, §33 pair) vs **(GAP-Z)** (background, slice coercivity/kernel) vs Theorem 4.2′'s **M**
     (response kernels) — CODEX GAPZ F2/F10; Finding 15.
   - **ω_0 = 1** vs ω_l = L^{θ(k−l)}: GZ-FALSE applies the l ≥ 1 weight at l = 0 (Finding 16).
   - **𝔉_k** (TOWER-VAR, Wilson at level 0 only) vs "Σ_jF_j" (Finding 16).
   - **(NEUT-box)**: §34.1 and §36.4 forms differ by n⁴ (S10-16 — agree).
2. **Stale quantifiers:** §30's G♯R window drops θ ≤ 1 − α (Finding 2); COF-crit applies a per-level row size where the
   theorem needs the weighted class norm (S10-6); GT-ell uses YH's unrestricted 𝒩 where a Λ_0-restricted one is needed
   (Finding 8); S10-6's θ* optimiser leaves the admissible θ > α range at large k (CODEX COFUN F11).
3. **Checks that cannot decide:** bb9b/bb10/bb10c run with s = G = 0, so the top-residual-slot defect of Lemma SPLIT is
   invisible to them (r55b D5-D7 see it); bb11 A4a/A4b test the root-to-root line map, so they cannot detect Theorem BGD (b)'s
   operator mislabel; nothing in bb11 tests §41.2 (c), §41.3 or §41.4 (the file says so). My own r55b gates: D2 could fail
   (a non-root-to-root contour leaves d*v ≠ 0 and no G in the box), D4 is a control that fired, D6 is the control for D5.
4. **Status arguments presented as proofs:** "(GAP-Z) is BFT-5's input (1)" (an identification by name); "§35.7: (CO-fun) is
   FALSE" (one term of a representative-dependent split read as the whole); "GZ-FALSE … for every lift" (maximality of a
   proven weight read as a property of all lifts).

---

## SUMMARY TABLE (every claim in the batch; verdicts CONFIRMED / NOT-VERIFIED / REFUTED; "spot" = spot-checked only, not counted)
| # | claim (file, locating string) | file status | verdict | finding |
|---|---|---|---|---|
| 1 | Lemma RT-cc (a)-(d), §29.1 | PROVEN-HERE | **CONFIRMED** (l.3674's "Ψ_{k−1} = D(S)" imprecise, harmless) | 1 |
| 2 | Lemma FT (i)-(iv), §29.2 | PROVEN-HERE | **CONFIRMED** | 1 |
| 3 | Theorem RHT-cc, K_f = 8.737, §29.3 | PROVEN-HERE | **CONFIRMED** (relative to top residual; r55b_num N1) | 1, 20 |
| 4 | Corollary RHT-V "N_res ≤ C_Vη²", §29.4 | PROVEN as implication | **NOT-VERIFIED** (top-residual bound for V missing) | 1 |
| 5 | Theorem RHT_m-cc, c_w = 14, §29.5 | PROVEN-HERE | spot (upper bound fine) | 1 |
| 6 | T1: (Res-Hölder) closed at m = 0 | — | **CONFIRMED** in relative form; absolute row form NOT-VERIFIED (= #4) | 1 |
| 7 | T2: Proposition CO-use / (H-inv+) bundle closed, §30 | PROVEN-HERE (bookkeeping) | **CONFIRMED** as bookkeeping (+ G♯R window, class caveat) | 2 |
| 8 | T3: (CO-fun) as stated in §31.2 (l.3802) holds | stated, OPEN | **CONFIRMED** true given Theorem COF + W0/GU/LIN0 (my derivation) | 3, 5 |
| 9 | Proposition NCR, §31.1 | PROVEN-HERE | **CONFIRMED** (with n²) | 9 |
| 10 | (R2) bound / "(NC-Γ)_cc + (GT-sup) ⟹ (NC-Γ)", §31.3 | stated implication | **REFUTED** (needs n²‖D^⊥‖_1 as a third input) | 9 |
| 11 | §31.2 (a) residual half "PROVEN unconditionally" | PROVEN | **NOT-VERIFIED** (its i = k−1 term is the top residual) | 1, 18 |
| 12 | BFT-5_E clause (c) "PROVEN (NCR)", §32.1-32.2 | PROVEN | **REFUTED** at stated scope → CONDITIONAL on (N1-nd)-type input | 9 |
| 13 | Proposition BFT5-red as bookkeeping, §32.2 | PROVEN as bookkeeping | **NOT-VERIFIED** | 9 |
| 14 | Lemma Rω-frame, §32.3 | ARGUED | spot (status honest) | 9 |
| 15 | Lemma W0-use "exactly two places", §35.1 | PROVEN-HERE | **REFUTED** (third use at step 3's TOPD; harmless for COF) | 22 |
| 16 | Lemma SPLIT (pointwise D(S^s) = 0; (CC-0) passes to S^j), §35.2 | PROVEN-HERE | **REFUTED** (top slot; r55b D5, D7); slot-wise composite co-closedness CONFIRMED | 4 |
| 17 | Lemma DF-cc (i)-(iii), §35.3 | PROVEN-HERE | **CONFIRMED** (with D(S^j), ĵ_0 conventions) | 4 |
| 18 | Proposition COF-size, §35.4 | PROVEN-HERE | **CONFIRMED** (121/13) | 4, 20 |
| 19 | T4: Theorem COF, §35.5 | PROVEN as implication | **CONFIRMED** (proof gap at #16 repaired) | 4 |
| 20 | Corollary COF-crit, §35.6 | PROVEN as implication | **REFUTED** ((CC-0) not given by Lemma CD; level count) | 6 |
| 21 | Proposition COF-res, identity, §35.7 | PROVEN-HERE | **CONFIRMED** (as an identity for the defect term) | 5 |
| 22 | T5: "(CO-fun) as stated is FALSE"; "single extra term", §35.7 | PROVEN-HERE | **REFUTED** (r55b D2-D4; LIN0/GU; flux decomposition) | 5 |
| 23 | Remark MASSLESS, §35.8 | PROVEN-HERE | spot (agree S10-12) | 18 |
| 24 | Proposition GT-split, §36.1 | PROVEN-HERE | **CONFIRMED** | 8 |
| 25 | T7: Lemma ΓT-op (d) and the absolute constant 20 | PROVEN-HERE | **CONFIRMED** (r55b_num N3) | 8 |
| 26 | Proposition GT-loc, the inequality, §36.2 | PROVEN-HERE given ΓT-op (d) | **CONFIRMED** | 8 |
| 27 | T6: "(GT-sup) is not a spike-support question; needs (Y-sup^loc)", l.4168 | headline | **REFUTED** ((Y-sup^loc) false on core boxes, every representative) | 8 |
| 28 | Proposition GT-attr, §36.3 | ARGUED | arithmetic **CONFIRMED**; "(GT-sup) expected TRUE" **NOT-VERIFIED** | 8 |
| 29 | Proposition GT-ell, §36.4 | PROVEN as implication | **REFUTED** as written (𝒩-optimal gauge ∉ Λ_0) → CONDITIONAL on (YH-pin) | 8 |
| 30 | Theorem NCE (i), §36.5 (k-, T-uniform at critical points) | PROVEN as implication | **REFUTED** as stated (corrected form in Finding 6) | 6 |
| 31 | Theorem NCE (ii) "one scalar per level-k box", §36.5 | reduction | **NOT-VERIFIED** (face (b) void; face (a) has a bulk n⁴‖D^⊥‖ term) | 8 |
| 32 | T13: COFUN.md "l.3810 wrong, l.4203 right" | — | **CONFIRMED** for the divergence (pointwise; correct formula at l.4202); l.4203's sentence NOT-VERIFIED | 7 |
| 33 | Theorem N1-alg narrowed (a′)-(g′); Λ_0 not mod constants, §40.2 | PROVEN-HERE | **CONFIRMED** | 17 |
| 34 | (N1-d) ⟸ (N1-nd), §40.3; N1-CONS, §40.4 | PROVEN as implication / bookkeeping | spot | 17 |
| 35 | Proposition AUDIT / SIX-RED (i) "LIN0 Tier A only", §39 | PROVEN-HERE | AUDIT spot; **SIX-RED (i) REFUTED** | 17 |
| 36 | Lemma CONJ (i)-(iii), §41.1 | PROVEN-HERE | **CONFIRMED** (pointwise M_G intertwining re-derived) | 12 |
| 37 | T8: Theorem BGD (a) (B1), §41.2 | PROVEN-HERE | **CONFIRMED** (given (N2-0)(a)) | 10 |
| 38 | T8: Theorem BGD (b) (B2), (41.2)-(41.3), "EXACT iff straight-row tower" | PROVEN-HERE (identity) | **REFUTED** (Q_str mislabel; false for lane A's Q_l^Z) | 10 |
| 39 | T8: Theorem BGD (c) "slot-wise, weight-free, factor-k-free"; §43.4 | PROVEN-HERE | **REFUTED** as a proof (defects are value-relative) | 10 |
| 40 | §41.3 slot decomposition at Z | PROVEN-HERE | **REFUTED** (S^G not composite-co-closed at Z) | 11 |
| 41 | Lemma FR-price, §41.4 | PROVEN as implication | **NOT-VERIFIED** (sup vs quadratic form; preconditioning) | 13 |
| 42 | T9: NL-GLOB (i) "no gauge makes a curved background translation invariant" | PROVEN-HERE | **REFUTED** as worded (CODEX F12); narrow obstruction CONFIRMED | 12 |
| 43 | NL-GLOB (ii) Combes-Thomas locality | ARGUED | **NOT-VERIFIED** (agree: ARGUED) | 12 |
| 44 | T11: Theorem TRANSP "PROVEN … given exactly (GAP-Z) and (N1-nd)", §41.6 | PROVEN as implication | **REFUTED** | 14 |
| 45 | (N1-e) at Z, §41.7 | ARGUED | **NOT-VERIFIED** (agree: ARGUED) | 14 |
| 46 | T12: "(GAP-Z) is BFT-5's input (1); ONE obstruction", §41.5 (iii), §43.3 | — | **REFUTED** (identification); dependency observation CONFIRMED (not counted) | 15 |
| 47 | Lemma GZ-SLOT, §42.1 | PROVEN-HERE | **REFUTED** (𝔉_k ≠ Σ_jF_j; no level-j ≥ 1 curvature slot) | 16 |
| 48 | T10: Proposition GZ-FALSE, §42.2 | PROVEN-HERE | **REFUTED** (wrong slots; ω_0 = 1; infimum reading; every-lift non sequitur) | 16 |
| 49 | Theorem Cg-nr (ii) arithmetic, §42.3 | PROVEN | **CONFIRMED** as arithmetic; (CURV-dec) not an input of (CovLift) (part of #48) | 16 |
| 50 | Remark TWO-W, §42.4 | reading | spot (falls with #48) | 16 |
| 51 | Numbers: C_∞ ≤ 1.71 (§36.4), T ≥ 17, "8" (§41.4) | — | spot (valid bounds) | 20 |

Counts (rows 1-51, spot rows excluded): **CONFIRMED 21, NOT-VERIFIED 10, REFUTED 20.**
(CONFIRMED: 1, 2, 3, 6, 7, 8, 9, 17, 18, 19, 21, 24, 25, 26, 32, 33, 36, 37, 49 and the GT-attr arithmetic in 28 and the
narrow NL-GLOB obstruction in 42, counted once each = 21. NOT-VERIFIED: 4, 11, 13, 28 (conclusion), 31, 41, 43, 45, and the
l.4203 sentence in 32 and RHT-V's use in 6 counted with 4 — i.e. 4, 11, 13, 28, 31, 41, 43, 45, 32b, 6b = 10. REFUTED: 10, 12,
15, 16, 20, 22, 27, 29, 30, 35, 38, 39, 40, 42 (universal sentence), 44, 46, 47, 48, and the two of COF-crit's defects counted
once (20) — i.e. 10, 12, 15, 16, 20, 22, 27, 29, 30, 35, 38, 39, 40, 42a, 44, 46, 47, 48 = 18, plus #22's second clause
("single extra term") and #46's "ONE obstruction" counted separately = 20.)

UTC end of findings: see the closing timestamp line below.

## Counts — corrected and final (this supersedes the "Counts" paragraph directly under the summary table, which mis-added)
Counted verdicts (spot rows 5, 14, 23, 34, 50, 51 and AUDIT's spot part of 35 excluded; rows 28, 32, 42 carry two verdicts):
- **CONFIRMED 21:** rows 1, 2, 3, 6, 7, 8, 9, 17, 18, 19, 21, 24, 25, 26, 28 (arithmetic), 32 (divergence), 33, 36, 37,
  42 (narrow obstruction), 49.
- **NOT-VERIFIED 9:** rows 4, 11, 13, 28 (conclusion), 31, 32 (l.4203 sentence), 41, 43, 45.
- **REFUTED 18:** rows 10, 12, 15, 16, 20, 22, 27, 29, 30, 35, 38, 39, 40, 42 (universal sentence), 44, 46, 47, 48.

## REFUTED items, each with its correction (one line each; derivations in the findings)
1. (R2)/"(NC-Γ)_cc + (GT-sup) ⟹ (NC-Γ)" — |remainder| ≤ n²‖D(S)‖_1·sup|λ|; a bound on n²‖D^⊥(S)‖_1 is a third input.
2. BFT-5_E clause (c) "PROVEN" — CONDITIONAL on Ker H_Z = Ran Ξ_Z ((N1-nd)) at the background.
3. Lemma W0-use "exactly two uses" — three: step 3's TOPD bound uses 𝒩(Y^{(b)}) (type (A)); harmless for Theorem COF.
4. Lemma SPLIT pointwise — D(S^s) = ev^{(0→k)T}d*s_{k−1} (root-supported, total 0), and (CC-0) of S does not pass to S^j;
   every slot is composite-co-closed on Λ_0, which is what superposition needs.
5. Corollary COF-crit — Lemma CD holds on Λ_* only, D(𝔑^0)(c_X) = κ_{k−1}(d*r_{k−1}(x;B))(X) at a critical point; and the rows'
   class norm is ≍ L^{θ(k−1)}η²: at critical points ‖f_0‖_∞ = O((k−1)η²) by Finding 5, not k-uniform.
6. §35.7 "(CO-fun) as stated is FALSE" / "single extra term" — (CO-fun) as stated holds on every composite-co-closed source
   given Theorem COF (sup half without the top-residual term), via q·path_b ≡ (s_{k−1} = qδ_b, G_{k−1} = qG_b) and a max-flow
   flux b with sup|b| ≤ Σ_lπ_l(j_l). [S10-fix 1] is unnecessary; (TENT-Q) is not a curvature-half obstruction.
7. "(GT-sup) is not a spike-support question; it needs (Y-sup^loc)" — (Y-sup^loc) is false on the core boxes for every
   representative (dY^p_0(p) ≥ 1/(6 + 8κ_+)); GT-loc only settles (GT-sup) where supp D^⊥ avoids the core.
8. Proposition GT-ell "PROVEN as an implication [of YH]" — CONDITIONAL on 𝒩_{Λ_0}(Y^p) ≤ Cn (YH-pin); with YH's unrestricted
   𝒩 the identity misses n²⟨D^⊥, λ_opt − I_χλ_opt⟩.
9. Theorem NCE (i) k-, T-uniform — see 5; Γ-independence at critical points CONFIRMED.
10. SIX-RED (i) "LIN0 is Tier A only" — LIN0's slot superposition is a Tier-B matter at Z ≠ 1 (d_Z^*d_Z^* ≠ 0).
11. BGD (b) — (41.2)-(41.3) hold for the root-to-root line map Q_ax (what bb11 tests); for lane A's Q_l^Z the defect is
    (avg_{σ,y}Ad_{hol(T^σ_y)} − Ad_{Z_{l+1}})·lam_{l+1}(Y+e_μ), not zero on straight-row towers; size only ≲ Cρ_{l+1}²f_k.
12. BGD (c) "no weight, no factor k" — the defects are bounded relative to input values, not to the operators they perturb;
    each use must be priced (RT-cc's cascade: affordable; §41.3: mis-priced).
13. §41.3 — D_Z(S^G) lives on level-l roots (all sites at l = 0), so S^G is not composite-co-closed at a curved Z and its
    off-root part does enter the gauge-fixing remainder; Lemma SPLIT does not transport.
14. NL-GLOB (i)'s universal sentence — curved translation-invariant backgrounds exist (constant noncommuting links).
15. Theorem TRANSP — also consumes §41.5 (ii) [ARGUED], (N1-e) [ARGUED], (C_g-θ) [BCH ARGUED], a correct Q_l^Z defect, a slot
    decomposition at Z and FR-price [NOT-VERIFIED]: ARGUED, not PROVEN as an implication.
16. "(GAP-Z) is BFT-5's input (1); ONE obstruction" — input (1) is the trivial-chain (G♯_0-field); (GAP-Z) is a background
    statement that BFT-5's own reduction derives from (1) + G-pert + (G♯-patch); only a dependency, not an identity.
17. Lemma GZ-SLOT — 𝔉_k (TOWER-VAR) has its Wilson term at level 0 only; levels j ≥ 1 of g_Z are residual-type; no level-j
    curvature slot.
18. Proposition GZ-FALSE — the only curvature slot of g_Z is at level 0 with ω_0 = 1; the θ > 0 content of (CovLift) (iv)'s
    g_Z clause is (C_g-θ) for the residual slot (Cg-lin PROVEN; Cg-NL first order PROVEN, BCH ARGUED); (CURV-dec) is not an
    input of (CovLift).

## What this changes in PROOF.md and HANDOFF.md (the lead edits; I edit neither)
- **PROOF.md l.158-161 [S24-note 3] "(CovLift)'s non-residual g_Z clause at θ > 0 is FALSE … the search for a better lift is
  foreclosed": withdraw** (REFUTED items 17-18). Also l.6945's "(CovLift)'s θ > 0 clause … REFUTED or struck": withdraw for
  (CovLift); and **drop (CURV-dec)** from the session-scale list at l.156-157.
- **PROOF.md S24 follow-on headline (l.6942-6943) "(CO-fun) under (CC-0) … PROVEN":** upgrade to "(CO-fun) as stated in
  BFT_B §31.2 holds on every composite-co-closed source given Theorem COF and lane A's W0/GU/LIN0 (REVIEW55_BFTB F5); its sup
  half needs no top-residual term". **[S24-note] "(CO-fun)'s residue is the same functional as the (GE-T) refutation"
  (l.166-167):** keep the identity (COF-res = TE tent coefficient), drop the implication that (CO-fun) fails.
- **PROOF.md l.6919-6923 item 4:** "Theorem NCE gives (NC-Γ) for Γ_E at every critical point … uniformly in k and T" → at
  critical points: Γ-independent, residual half relative to the top residual, curvature sup half O((k−1)η²) (not k-uniform);
  "off the critical set the whole obstruction is one scalar per level-k box" → over-reduced (the (P0)-slot bound of Γ_E^TD(S)
  also has a bulk term n⁴‖D^⊥‖_∞, ≍ L^{k+3l}η² for the rows; the root-charge face is void). "(Res-Hölder) closed at m = 0"
  stays, in the relative form (RHT-V's absolute η² is NOT-VERIFIED).
- **PROOF.md l.140-161 (S25 notes on GAP-Z):** TRANSP must not be cited as "PROVEN given (GAP-Z) + (N1-nd)"; new background
  defects to carry: the slot decomposition at Z (S^G not composite-co-closed) and root covariance of lane A's Q_l^Z (not exact
  on straight-row towers).
- **The main-path tally (72 / 2 / 7 / 24 + 1) does not change:** none of these items was counted in it.
- **HANDOFF item 2 ("(N1) + (CovLift)'s non-residual g_Z at θ > 0"):** replace the g_Z clause by "(C_g-θ)'s BCH remainder
  (ARGUED)" and add the two background defects above; TRANSP is a sketch, not a reduction.
- **HANDOFF item 5:** keep "the level-count factor k first" (I agree with S10-6). **Remove (TENT-Q) from the list it is
  upstream of** (not an obstruction to the curvature half); (Y-sup^loc) is not merely NOT-VERIFIED — it is false on the core
  boxes for every representative, so (GT-sup) near p **is** a question about λ's fine structure (the "may be … after all"
  sentence can be made definite). The "one scalar per level-k box" sentence is over-reduced (bulk term).
- **HANDOFF "do not" item 3** ("pricing (CO-fun) and the (GE-T) refutation as two items"): reword — they are one functional
  identity, but (CO-fun) is not refuted by it.

UTC end: 2026-10-28T23:01Z (approx.; the file's mtime is authoritative).

Correction (appended 2026-10-28T22:59:20Z): the "UTC end" line above was written as an estimate; the actual `date -u` at that append was 2026-10-28T22:58:42Z. Final append of this file: 2026-10-28T22:59:20Z. Files written by this reviewer: REVIEW55_BFTB.md, checks/r55b_dip_criteria.md, checks/r55b_num_criteria.md, checks/r55b_dip.py, checks/r55b_dip_out.txt, checks/r55b_dip_err.txt, checks/r55b_num.py, checks/r55b_num_out.txt, checks/r55b_num_err.txt. No git command was run.
