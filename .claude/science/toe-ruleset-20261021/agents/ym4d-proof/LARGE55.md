Reviewer model: claude-opus-5-5

# LARGE55 — the large-field part of UV stability: simplify, then close what is left

UTC start: 2026-10-29 03:38 (from `date -u` at session start).
Role: Opus 5.5 WORKER (not a reviewer of a batch); the shared rules of REVIEW_BRIEF_55 apply.
Writes: this file and `checks/lg55_*` only. Append-only after this header.

## PRE-STATED (written before any derivation)

Targets.
- T1 (first principles). State, with full quantifiers, the minimal large-field statement(s) the full
  theorem needs: (a) for UV stability L6-soft, e^{-E_-|T|} <= Z_K/Z_K^{ref} <= e^{E_+|T|} uniformly in K;
  (b) for the per-step conditional bounds at a FIXED coarse field U_K (SRC / conditional decay /
  universality N3, which must hold at LARGE coarse fields).
- T2 (mechanism). Price the lane's v3 large-field architecture (RLARGE.md v3 §7 DAG with feeders HW, PLD,
  HIST, SQ, SF) against an action-based Balaban-type large/small-field split (Dimock's expositions as the
  map), counting OPEN/ARGUED/HYPOTHESIS items each needs. Recommend one, with reasons. Say exactly which
  step of the large-field argument uses Balaban's hard constraint and what replaces it in the soft S4'
  scheme.
- T3 (prove). Prove as much of the chosen route as possible, uniformly in k and T, from banked inputs
  (PROOF.md [S26-BANKED] or a REVIEW55_*/CODEX_REVIEW_* confirmation) and what is proved here. Name
  every remaining input precisely.

What would count as a refutation (of my own deliverable's claims, stated in advance).
- R1: an explicit configuration / regime in which the proposed minimal statement holds but the needed
  consequence (L6-soft or the conditional per-step bound at large U_K) fails — i.e. the statement does not
  suffice.
- R2: a step in the action-based large-field argument whose only known proof uses Balaban's hard
  constraint (support of the RG kernel restricted to small fields) with no soft replacement — then the
  simplification fails at that step and I must say so.
- R3: a counterexample to a claimed lower bound on the Wilson action of a non-small block (e.g. a
  configuration with a non-small block field whose action is below c p(g)^2/g^2), or to a claimed
  entropy count (polymer/region counting exceeding the suppression uniformly in k, T).
- R4: any numeric gate I pre-register that fails, or that I find cannot fail (then it is void, not PASS).
- R5: a banked input I lean on that turns out not to be banked (not in [S26-BANKED] and not confirmed in a
  REVIEW55_*/CODEX_REVIEW_* file) — then every conclusion depending on it is downgraded to conditional.

Verdict vocabulary: PROVEN-HERE (I derived the load-bearing step in this file), CONFIRMED (re-derived a
banked/earlier claim), NOT-VERIFIED, REFUTED, OPEN (a named remaining input).

---

## §0. Read record, provenance of every input, Codex/Opus-5.5 verdicts used (written 2026-10-29 ≈04:20Z)

Read (targeted, by string/section; nothing read whole): REVIEW_BRIEF_55; HANDOFF; PROOF.md banner + [S26-BANKED]
(l.1-36), S4′/Decision 4/Lemma D4-norm (strings `S4' [S3] Order-averaged`, `Decision 4: the RG kernel`,
`Lemma D4-norm (the normalised kernel)`), Proposition LF-count (string `[S6] Proposition LF-count`); RLARGE.md §0, §1,
§2-§3 (for FV and the defect notions), §4.2-§4.4, §5, §6, §7, §8; REVIEW55_HWPLD (summary, F6, FOR THE LEAD);
REVIEW55_CONST (headline, §6); CODEX_REVIEW_RLU (summary, bankable scope); SRCAN55 §4; SRCCD55 §6 (M1)-(M7); UNIV55 §2.4,
§3.1-§3.2; PLAN_S26 §2, §11-§12; BALABAN_EXTRACT §5 M8-M9, §6.1-§6.2, §9; HW.md §5.2 (Lemma KS, KS-chain, (KS-N));
CODEX_REVIEW_BALX F1-F3 (coordinator's pointer); HINT2_55 §R2.1, §R2.4 (coordinator's pointer); LCONV55 §G, FOR THE LEAD
(coordinator's pointer). Corpus (scratch, data only): Dimock 1108.1335 (abstract, §1), 1212.5562 (§1, p.1-4; Remark 3 after
eq. (222)), 2204.07201 (§2-§5 in full; it is 815 lines).

**Provenance rules I apply.** A session-24/25 item is used as an input only if [S26-BANKED] or a REVIEW55_*/CODEX_REVIEW_* file
confirms it; older items (sessions ≤ 23: Decision 4, D4-norm, LF-count, GT-lat, R4D-iso, HIST-sum's arithmetic, LINEAR_PACKAGE
Thm 2.1) are cited as lane statements and **re-derived here wherever they are load-bearing** (D4-norm (2) is re-derived inside
Lemma TL/MIS below; LF-count is superseded by Theorem DENSE below, which is proved from scratch).

**Symbols pinned for this file (systemic defect 1).** d = 4; G = SU(N), N ≥ 2; D := N² − 1 = dim G. Level j field U_j on
Λ_j; u_j := 1/g_j² (lane normalisation u = β_Wilson = 2N/g_std², RLARGE §0 `Action normalisation`); s(U) := 1 − N⁻¹Re tr U.
**t_j := κu_j** (the stage-j kernel stiffness; κ is the lane's kernel constant of Decision 4). Kernel of stage j:
K_j(V, U) = Π_c k_c, k_c(V_c; M) := e^{−t_jφ_M(V_c)}/𝒩_{t_j}(M), φ_M(V) := 1 − N⁻¹Re tr(V⁻¹M) ∈ [0, 2], M = M̄_c(U) the S4′
mean of contour transporters, ‖M‖_op ≤ 1 (PROOF `Decision 4`). ρ_0 := e^{−S_0}, ρ_{j+1}(V) := ∫ρ_j(U)K_j(V, U)dU (the
**effective density** of level j+1; = Z_K × the level-(j+1) marginal); Z_K = ∫ρ_j dU_j for every j. |T| := number of level-K
sites, so |E_K| = 4|T| level-K links. β_± are the (F_R) slopes (RLARGE §0 `(F_R)_{[0,k]}`), β_0^std = 11N²/(12π²) per log L in
this normalisation. **ε** in this file always denotes a link-unit cut (a bound on ‖1 − U_p‖_op); **a** a per-cube price exponent
(price e^{−a u}); I do not use the lane's ε_1, a_bad, θ, n_♯ values except where quoted with their file.
c_N := inf_{0<r≤1} Haar(B_op(1, r))/r^D > 0 (positive: a positive continuous function of r on (0, 1] with a positive limit
at 0, B_op(1, r) containing a geodesic ball of radius ≍ r).

**Codex / Opus-5.5 verdicts used (agreement stated, per the brief):**
- CODEX_REVIEW_BALX **F2** (coupling-dependent integration cuts coexist with fixed admissibility radii in the expositions; the
  fixed-threshold account is refuted as general) — **AGREE**; §2.3 below derives what F2 implies for d = 4 large fields.
  **F3** (the extract's own alternative cut has a summable n^{−3/2} tail) — **AGREE as algebra**; I add (§2.3) that F3 concerns a
  compounding product Π(1 + Dh_k), not the large-field count, which diverges for every cut (Theorem DENSE, Prop. NOFREEZE).
- REVIEW55_HWPLD (Opus 5.5) r55h-18 / r55h-26 / r55h-25 (the universally quantified F_< makes (E2^𝔉′), (CEM^{COL}), (ACT′),
  (LCR^act′), (BCH-1) false as quantified; (CEM-2) not dissolved; PLD §18.5 (b′) false) — **AGREE** (not re-derived; used only
  as evidence of the cost of the conditioned-moment layer, which the recommended architecture does not consume).
- CODEX_REVIEW_RLU "Exactly what may be banked" 1-5 (W-cb♯ and FI-1 conditional) — **AGREE** with its scoping; W-cb♯ is not
  consumed by the recommended architecture; FI-1 is route-independent and is kept.
- [S26-BANKED] `Source-inserted RG (SRC) — Proposition B and Lemma V CONFIRMED` (the soft chain is Markov with exact source
  recursion) — used in §1.3.
- HINT2_55 and LCONV55 are Opus 5.5 files whose Codex reviews are still running (coordinator); I use them as stated inputs to the
  design and give my own verdict on the specific claims I touch (§5.5, §5.6), not as banked results.

---

## §1. T1 — What the full theorem needs from large fields, and the minimal statements

### 1.1 Who consumes large-field control, and in what form
| consumer | what it needs | form |
|---|---|---|
| L6-soft (UV stability; EXISTENCE's ratios Z(𝔥)/Z_K; chessboard constants) | e^{−E_−\|T\|} ≤ Z_K/Z_K^{ref} ≤ e^{E_+\|T\|}, uniformly in K | partition-function level, integrated over every field |
| H_reg via sources (SRC (M1), Prop. E) | the same for Z_K(J), J a complex local source in a polydisc, with the vacuum part J-independent | partition-function level, complex weights |
| SRC conditional decay / UNIV (N1)-(N4) / SRC (M2) | per-step bounds **conditional on a coarse field**, at every coarse field (sup over V, UNIV55 §2.1 `(sup_V)`) | sup over configurations, **difference form** (two theories, or with vs without a source) |
| H_int, bare-flowed witness (HINT2_55 (TS-up)) | flowed energy density ≤ C g_k^{2(1−ϑ)} at every short flow time | a sharp action-gap bound on flow-surviving concentrations (§5.5) |

### 1.2 Lemma TL (the top level is free). PROVEN-HERE (elementary)
**Statement.** For every stage j with t_j ≥ 1, every K, T and every level-(j+1) configuration V (no smallness):
  **e^{−2t_j|E_{j+1}|}·Z_K ≤ ρ_{j+1}(V) ≤ (e·c_N⁻¹·t_j^D)^{|E_{j+1}|}·Z_K.**
*Proof.* (i) Lower: φ ≤ 2 gives numerator ≥ e^{−2t_j}; 𝒩_t(M) = ∫e^{−tφ_M} ≤ 1; so k_c ≥ e^{−2t_j}. (ii) Upper (this is PROOF's
D4-norm (2), re-derived): let V_0 maximise Re tr(V⁻¹M) over SU(N), φ_min := φ_M(V_0). For V ∈ B_op(V_0, 1/t):
φ_M(V) − φ_min = N⁻¹Re tr((V_0⁻¹ − V⁻¹)M) ≤ ‖V_0⁻¹ − V⁻¹‖_op‖M‖_op ≤ ‖V − V_0‖_op ≤ 1/t (using |N⁻¹tr(XM)| ≤ ‖X‖_op‖M‖_op and
unitary invariance). Hence 𝒩_t(M) ≥ e^{−tφ_min}e^{−1}Haar(B_op(1, 1/t)) ≥ e^{−tφ_min}e^{−1}c_N t^{−D} (t ≥ 1), and
k_c(V) = e^{−t(φ_M(V) − φ_min)}e^{−tφ_min}/𝒩_t(M) ≤ e·c_N⁻¹t^D. (iii) Both bounds hold pointwise for K_j(V, U) = Π_ck_c; integrate
against ρ_j ≥ 0 and use ∫ρ_j = Z_K. ∎
**Corollary TL-1 (sup-form ⟺ integrated form at the top).** For any c-number 𝒱:
|log Z_K − 𝒱| ≤ sup_{U_K}|log ρ_K(U_K) − 𝒱| ≤ |log Z_K − 𝒱| + 4|T|·max{2t_{K−1}, log(e c_N⁻¹t_{K−1}^D)}.
(Left: Haar is a probability measure. Right: Lemma TL at j = K − 1.) Under (F_R), u_{K−1} ≤ u_K + β_+log L + R, so the extra term
is E|T| with E depending on (N, κ, g_K, L, R) only. **So UV stability "at every coarse field" is the same statement as UV
stability**; a large coarse field is not a separate obstruction for any partition-function-level consumer.
**Corollary TL-2 (coarse law ≍ Haar).** ν_K := ρ_K/Z_K obeys e^{−8t_{K−1}|T|} ≤ dν_K/dHaar ≤ (e c_N⁻¹t_{K−1}^D)^{4|T|}: every set of
coarse configurations — in particular every large-coarse-field set — has probability within K-independent factors per unit
volume of its Haar measure. (This is UNIV55 §2.1's lower bound, `Well-posedness of sup_V`, plus the matching upper bound.)
*What TL does not give.* For j < K − O(1), |E_{j+1}| = 4L^{4(K−1−j)}|T| and the bounds are useless: all the content of UV stability
is at fine levels. That is where §2's obstruction lives.

### 1.3 Lemma PP (positivity propagation through common kernels). PROVEN-HERE (elementary)
**Statement.** Let P(V|U) ≥ 0 be measurable (for instance Π_{i=m}^{n−1}K_i, the common stages m..n−1 of two chains), ρ² ≥ 0,
ρ¹ complex-valued, c ∈ ℂ, δ ≥ 0, and suppose all integrals below converge absolutely.
(a) If |ρ¹(U) − e^cρ²(U)| ≤ δ|e^c|ρ²(U) for every U, then |ρ'¹(V) − e^cρ'²(V)| ≤ δ|e^c|ρ'²(V) for every V, where
    ρ'^a(V) := ∫ρ^a(U)P(V|U)dU.
(b) If ρ¹ ≥ 0 and e^{c−δ}ρ² ≤ ρ¹ ≤ e^{c+δ}ρ² (c real) for every U, the same holds for ρ'¹, ρ'² for every V.
*Proof.* (a) |ρ'¹ − e^cρ'²| ≤ ∫|ρ¹ − e^cρ²|P ≤ δ|e^c|∫ρ²P. (b) Integrate the two inequalities against P ≥ 0. ∎
**Corollary PP-1 (UNIV55 (N3) is not a separate input).** If two theories share the kernels from level m on and
sup_U|log ρ¹_m(U) − log ρ^R_m(U) − c| ≤ δ over ALL level-m configurations, then the same bound holds at every coarser level, in
particular at ℓ_0 and every coarse V. So Proposition T's (U-dens) at ℓ_0 costs nothing beyond the sup-form comparison at any finer
common level: **no background-field theory at non-small backgrounds for the last j_0 levels (UNIV55 (N3)'s first alternative) is
needed.** What IS needed is the comparison in sup form over all configurations at the level where it is proven — i.e. the
large-field form of (N1) (UNIV55's second alternative). The requirement is the same at every level; the top levels are not
special.
**Corollary PP-2 (SRCCD55 (M2) likewise).** With the exact source recursion of the banked Proposition B, if the source-perturbed
effective density obeys |ρ_m(U; z) − e^{c(z)}ρ_m(U; 0)| ≤ δ|e^{c(z)}|ρ_m(U; 0) for all level-m U with δ < 1, then at every coarser
level and every coarse V the conditional generating function ρ(V; z)/ρ(V; 0) lies in the closed disc of radius δ|e^{c(z)}| about
e^{c(z)}: non-vanishing and bounded at every coarse field. (M2) reduces to the per-level difference-form bound at any finer level.

### 1.4 The minimal large-field statements (with quantifiers)
Notation: N_j := number of level-(j+1) blocks; Z_K^{sf}[δβ] := the partition function of the chain with every level's small-field
indicators imposed and the couplings u_j replaced by u_j − δβ_j; e_j^{sf} := its level-local vacuum density (node A's output).
**(LF-UV) [for (a): UV stability and all partition-function consumers].** There are, for every level j, a field-independent number
e_j and a coupling shift δβ_j, each a function of the level-j coupling data (g_j, g_{j+1}; L, N, κ) only, with |δβ_j| ≤ g_j⁶
and Σ_j|δβ_j| < ∞ uniformly in K, and E_± < ∞, such that for all K and all T ≥ T_0:
  e^{−E_−|T|} ≤ Z_K·exp(−Σ_{j<K}N_j(e_j − e_j^{sf}))/Z_K^{sf}[δβ] ≤ e^{E_+|T|},
and the same with S_0 replaced by S_0 − J·O for complex local sources J in a fixed polydisc, with e_j, δβ_j unchanged and E_±
depending on ‖J‖ and |supp J| only.
*Remarks.* (i) The level-locality of e_j and δβ_j is what makes the statement non-tautological. (ii) By Theorem DENSE (§2.1)
e_j ≠ e_j^{sf} is forced: the large-field part of the free energy diverges with K, so it must be a level-local c-number (plus a
coupling shift). (iii) This is RLF's (RLF-0)+(RLF-1)+(RLF-4) content, stated without the route-specific (RLF-3′).
**(LF-diff) [for (b): conditional per-step bounds at a fixed coarse field].** For every level m, every pair of theories sharing
kernels from some level s ≤ m on (UNIV: grid 1 / grid R; SRC: source z / no source), and EVERY level-m configuration U (no
smallness), the large-field parts of the two per-level representations (returned activities and history factors, §6.1) differ
by at most δ_m per level-m block, with (δ_m) obeying UNIV55's (N1) recursion (contraction of the irrelevant part, bounded growth
of the marginal part, constants uniform in m and in the configuration).
*Sufficiency.* (LF-UV) + node A + the flow ⇒ L6-soft and H_reg's partition-function bounds (by definition of the reference).
(LF-diff) + node A's difference form ⇒ UNIV55 Theorem U's per-level inputs (N1) at every configuration, hence (U-dens) at ℓ_0 by
PP-1 with no further large-coarse-field analysis; and SRC's (M2) by PP-2. TL removes every partition-level statement "at large
coarse fields". **Neither statement gives (TS-up)** (§5.5).
*Minimality.* Each clause is necessary for its consumer: the c-number by DENSE; level-locality to avoid tautology; the source
clause because H_reg is a source statement; the sup-over-configurations clause because Proposition T needs sup_V and, by TL-2,
large coarse fields carry probability bounded below. Nothing weaker than "difference form at every configuration of some level"
serves Proposition T (it needs sup_V; by PP-1 that is equivalent to sup over configurations of any finer common level).

---

## §2. T2(a) — In d = 4 large-field contributions must be renormalised: a counterexample to the d = 3 mechanism

The brief's candidate mechanism — "on a block where the field is not small the action is ≥ (cost), and the large-field region's
contribution is paid by that suppression against combinatorial entropy, with no small-field expansion inside it" — is exactly
the d = 3 mechanism of Dimock 2204.07201 §3 (its (17)-(19): ζ_0(□)e^{−‖dA_0‖²_□/4} ≤ e^{−p(e_0)²/4}, Σ_Ω ≤ exp(e^{−p²/4}|T|_M) ≈ 1
"since e^{−p²/4} beats |T|_M"; the large-field contributions "do not require renormalization"). The following theorem shows
that in d = 4 this fails **for the true measure, not just for the bound**, for every cut, fixed or coupling-scaled.

### 2.1 Theorem DENSE (bare large fields are dense; the all-small-field part is superexponentially negligible). PROVEN-HERE
**Setting.** Bare torus Λ_0 of side T·L^K, |Λ_0| = T⁴L^{4K}; Wilson measure μ_K ∝ e^{−u_0Σ_ps(U_p)}Π_bdU_b. This is the U_0-marginal
of the soft chain (integrate the normalised kernels top-down), so every U_0-event has the same probability under W/Z_K.
**Statement.** Let 0 < ε ≤ ε_max with ε + ε³ ≤ 1 (ε_max ≈ 0.6823), A_N(ε) := (24/N)(1 + ε²)² + 6ε, D = N² − 1, and
π_0 := c_Nε^{3D}e^{−u_0ε²A_N(ε)}. Then:
(i) for every bare plaquette p_0, a link b ∈ p_0, and every configuration of all other bare links,
    μ_K(‖1 − U_{p_0}‖_op ≥ ε | U_{b′}, b′ ≠ b) ≥ π_0;
(ii) μ_K(no bare plaquette has ‖1 − U_p‖_op ≥ ε) ≤ exp(−π_0|Λ_0|/9);
(iii) more generally, for every n ≥ 1, the expected number of n-clusters of ε-bad plaquettes (n link-disjoint plaquettes stacked
    in direction 3, a *-connected set) is ≥ (|Λ_0|/(9n))·π_0^n;
(iv) if the bare coupling obeys u_0 ≤ u_* + β_*K log L (e.g. (F_R)'s upper bracket between levels 0 and K: u_* = u_K + R,
    β_* = β_+), then for every fixed ε with ε²A_N(ε)β_* < 4,
    log(Z_K/Z_K^{sf}) ≥ (c_Nε^{3D}/9)·T⁴e^{−ε²A_N(ε)u_*}·L^{(4 − ε²A_N(ε)β_*)K} → ∞ (exponentially in K),
    where Z_K^{sf} is ANY quantity ∫W·Π_{bare p}1{‖1 − U_p‖ < ε}·F with 0 ≤ F ≤ 1 (any small-field indicators at any coarser
    levels, any history restriction) — in particular the all-small-field contribution of any large/small split whose bare cut is ε;
(v) the same divergence holds for every coupling-dependent cut ε = g_0p(g_0), p(g) = (log 1/g)^p, p > 0 (for K large), and then
    (iii) gives, for every FIXED n, an expected number of cut-failing n-clusters → ∞.
*Proof.* (1) *Conditional law of one link.* For each plaquette q ∋ b, by cyclicity of the trace (and Re tr X = Re tr X* for a
backward traversal), s(U_q) = 1 − N⁻¹Re tr(U_bB_q) with B_q ∈ SU(N) built from the other three links. So the conditional density
of U_b is ∝ exp(u_0f(U_b)), f(U) := N⁻¹Re tr(UA), A := Σ_{q∋b}B_q, ‖A‖_op ≤ 2(d − 1) = 6. For q = p_0, U_{p_0} is conjugate to
U_bB_0 (or to its inverse), so ‖1 − U_{p_0}‖_op = ‖1 − U_bB_0‖_op = ‖B_0⁻¹ − U_b‖_op: p_0 is ε-bad iff U_b ∉ B_op(B_0⁻¹, ε).
(2) Let U* maximise f on SU(N), ψ := f(U*) − f ≥ 0. The conditional law is e^{−u_0ψ}dU/∫e^{−u_0ψ}dU and ∫e^{−u_0ψ} ≤ 1, so
P(S | rest) ≥ ∫_Se^{−u_0ψ}dU for every Borel S.
(3) *First-order condition.* For Y ∈ su(N), t ↦ f(e^{tY}U*) is maximal at 0: Re tr(YP) = 0, P := U*A. Write P = H + K, H
Hermitian, K anti-Hermitian. For Y anti-Hermitian Re tr(YH) = 0 identically and tr(YK) is real, so tr(YK) = 0 for all Y ∈ su(N),
whence K = iλ·1, λ ∈ ℝ.
(4) *A cheap displacement.* For an orthonormal pair e_1, e_2 and θ ∈ [0, π] put Y_θ := iθ(e_1e_1* − e_2e_2*) ∈ su(N),
W_θ := e^{Y_θ}U*. Then ‖W_θ − U*‖_op = |e^{iθ} − 1| = 2sin(θ/2), and with h_i := ⟨e_i, He_i⟩ ∈ ℝ,
Re tr((1 − e^{Y_θ})P) = Re[(1 − e^{iθ})(h_1 + iλ) + (1 − e^{−iθ})(h_2 + iλ)] = (1 − cos θ)(h_1 + h_2) (the λ-terms ±λ sin θ
cancel). Since ψ(e^{Y}U*) = N⁻¹Re tr((1 − e^{Y})P), ψ(W_θ) ≤ (2/N)(1 − cos θ)‖H‖_op ≤ (2/N)(1 − cos θ)‖A‖_op ≤ (24/N)sin²(θ/2).
(5) *Lipschitz.* |ψ(U) − ψ(U′)| = N⁻¹|Re tr((U′ − U)A)| ≤ N⁻¹‖U′ − U‖_op‖A‖_{S_1} ≤ ‖A‖_op‖U′ − U‖_op ≤ 6‖U′ − U‖_op.
(6) Put δ := ‖U* − B_0⁻¹‖_op, r := ε³. If δ ≥ ε + r take W := U*; else take θ with sin(θ/2) = ε + r (≤ 1) and W := W_θ, so
‖W − B_0⁻¹‖_op ≥ 2(ε + r) − δ > ε + r. In both cases B_op(W, r) lies in the bad set {‖U − B_0⁻¹‖ ≥ ε}, and on it
ψ ≤ (24/N)(ε + r)² + 6r = ε²A_N(ε). Hence P(bad | rest) ≥ Haar(B_op(1, r))e^{−u_0ε²A_N(ε)} ≥ c_Nε^{3D}e^{−u_0ε²A_N(ε)} = π_0. (i) ∎
(7) *Link-disjoint test family.* 𝒳 := {x : x_1, x_2 even, x_1, x_2 ≤ side − 2}; p_x := the (1,2)-plaquette at x, b_x := (x, e_1).
The plaquettes p_x, x ∈ 𝒳, are pairwise link-disjoint (their 1- and 2-coordinates lie in disjoint pairs {x_i, x_i + 1}), and
|𝒳| ≥ |Λ_0|/9 (⌊s/2⌋ ≥ s/3 for s ≥ 2). For an ordering x_1, …, x_n, Π_{i<n}1{p_{x_i} good} does not read b_{x_n}, so
P(∩_{i≤n}{p_{x_i} good}) = E[Π_{i<n}1{…}·P(p_{x_n} good | all links but b_{x_n})] ≤ (1 − π_0)P(∩_{i<n}…); induct:
≤ (1 − π_0)^{|𝒳|} ≤ e^{−π_0|Λ_0|/9}. (ii) ∎ For (iii) stack p_x, p_{x+e_3}, …, p_{x+(n−1)e_3} (link-disjoint, *-connected) and run
the same conditioning with the lower bound: P(all n bad) ≥ π_0^n; take ⌊|𝒳|/n⌋ disjoint stacks.
(8) (iv): Z_K^{sf} ≤ ∫W·Π_p1{good} = Z_K·μ_K(no bad bare plaquette) ≤ Z_K e^{−π_0|Λ_0|/9}, and π_0|Λ_0| ≥ c_Nε^{3D}T⁴
e^{−ε²A_N(ε)u_*}L^{(4 − ε²A_N(ε)β_*)K}. (v): with ε = g_0p(g_0), u_0ε² = p(g_0)², g_0² ≥ (u_* + β_*K log L)⁻¹, so
π_0 ≥ c_N(u_* + β_*K log L)^{−3D/2}exp(−A_N(ε)(½log(u_* + β_*K log L))^{2p}): quasi-polynomially small in K against |Λ_0| = T⁴L^{4K};
the same for π_0^n at fixed n. ∎
**Numbers (check lg55_1, exact rational arithmetic, criteria pre-registered).** The density condition ε²A_N(ε)β_0^std < 4 holds
for all ε up to ≈ 0.62 (N = 2), ≈ 0.53 (N = 3), and every cut the lane uses (ε_1 ≲ 10⁻³⁹, RLARGE §0) satisfies it with room;
the exact grid values are in §7.
**What it refutes, exactly.**
- **Claim B ("d = 3 mechanism suffices in d = 4"):** *there are a bare cut ε ≤ ε_dense(N) and E < ∞ with Z_K ≤ e^{E|T|}Z_K^{sf}
  uniformly in K* — **REFUTED** by (iv) (and by (v) for coupling-scaled cuts). Any argument that writes Z_K = Σ_ΩZ_K(Ω) with
  Z_K(Ω) ≤ (small-field part)·Π_{□∈Ω^c}w_□ and bounds Σ_ΩΠw ≤ e^{E|T|} proves Claim B; so that argument is impossible.
- The brief's mechanism as a **complete** mechanism: REFUTED for d = 4 (CONFIRMED for d = 3, where Dimock's (19) holds).
- PROOF.md's Proposition LF-count (`[S6] Proposition LF-count`) proved divergence of the unrenormalised **bound**; DENSE proves
  divergence of the **quantity** log(Z_K/Z_K^{sf}), uniformly over all coarser-level choices, with an explicit threshold, and for
  coupling-scaled cuts. LF-count's conclusion ("their contribution to log Z must itself be renormalised") is now a theorem.
- Consistent with RLARGE v3's design: v3 never claims Z ≈ Z^{sf}; its returned defects exist for exactly this reason.

### 2.2 Proposition NOFREEZE (coupling-scaled cut failures cannot be left unreturned). PROVEN-HERE (arithmetic + DENSE (v))
**Statement.** Let a scheme classify, at level j, *-components of cut-failing cubes with a coupling-scaled cut ε_j = g_jp(g_j),
p(g) = (log 1/g)^p, and leave components of size ≤ n unreturned (frozen / history), with per-cube weights w_j that are valid
upper bounds for the true weights, so that w_j ≥ c·exp(−A·p(g_j)²) (DENSE (i) at the bare level; the same lower-bound mechanism at
level j). Then for every fixed n and every per-level shadow cost B ≥ 0 (including B = 0), under (F_R)'s upper bracket,
L^{4(K−j)}w_j^{n}e^{B(K−j)} ≥ c^n·exp(4(K−j)log L − nA(½log(u_K + R + β_+(K−j)log L))^{2p}) → ∞ as K − j → ∞,
so the RLF/HIST-type history sum Σ_jL^{4(K−j)}w_j^{n+1}e^{B(K−j)} diverges as K → ∞ for every n. At the bare level this is not an
artefact of the bound: DENSE (v)+(iii) gives an expected number of such n-clusters → ∞.
*Proof.* (log x)^{2p} = o(x); substitute u_j ≤ u_K + β_+(K−j)log L + R. ∎
**Consequence (with F2).** Balaban/Dimock's coupling-scaled integration cut (CODEX_REVIEW_BALX F2's table) is compatible with d = 4
only if **every** cut failure is returned in-step (renormalised), never frozen; an unreturned / history category needs a **fixed**
threshold ε_cl, for which the price exponent is linear in u (e^{−a u_j}, a ∝ ε_cl²) and components of size > 4/(aβ_−) are rare
(DENSE (iii) with π_0^n, n > 4/(ε²A_Nβ)). With a fixed threshold the bare n-cluster count tends to 0 exactly when nε²A_Nβ_* > 4
(up to the gap between A_N and the true cheapest cost) — the RLF n_♯ structure is forced, not chosen.

### 2.3 The threshold choice, with CODEX_REVIEW_BALX F2/F3
- **Two domains, two roles (agreeing with F2).** A FIXED link radius ε_0 is an admissibility/chart domain (BCH, background-field
  theory, analyticity converge). A coupling-scaled canonical cut |Z_can| ≤ p(g) (link size g p(g) → 0) is the domain on which the
  fluctuation interaction is **absolutely** small: the BCH cubic vertex of the bare action in canonical link variables is
  (g/(2N))⟨ΣZ, Σ[Z, Z]⟩ = O(g|Z|³), which on |Z| ≤ p(g) is O(gp³) → 0, while on a fixed link cut |gZ| ≤ ε it reaches ε³/g² → ∞.
  (On the fixed cut it is still **relatively** small, ≤ Cε|Z|², so a fixed-cut fluctuation expansion is possible but must use
  relative/regulator norms; this is a node-A design choice, not a large-field one.) [Remark; elementary; not load-bearing.]
- **What d = 4 adds (DENSE, NOFREEZE).** Failures of either cut are dense at fine levels. Coupling-scaled failures must all be
  returned; fixed-threshold failures may be frozen only in components of size > 4/(aβ_−).
- **F3.** Its summable tail Σ_n h_{K−n} < ∞ concerns compounding products Π(1 + Dh_k) of constants, not the large-field count
  Σ_jN_jw_j, which diverges for every cut (DENSE). AGREE with F3's algebra; it does not bear on large-field summability.
- **Recommendation for the large-field architecture:** one FIXED classification threshold ε_cl ≤ ε_0 (inside node A's chart) for
  large fields and histories; node A chooses its fluctuation cut (coupling-scaled with all failures returned as perturbative
  polymers — Balaban/Dimock — or fixed with regulator norms). The large-field layer below is the same in both cases.

---

## §3. T2(b) — Which steps of the large-field argument use the hard constraint, and what replaces each in the S4′ soft scheme

Map: Dimock 2204.07201 §3-§5 (QED3; the gauge field averaged with the hard δ(A_{k+1} − QA_k), §5 eq. (52)) and 1212.5562 §1
(scalar; the averaging is itself soft, a Gaussian e^{−aL²‖Φ_1 − QΦ_0‖²/2}, eq. (5)). The S4′ averaging operator itself is not
the issue (PROOF `Lemma B-avg`: Balaban's (0.4) and S4′ differ only in contour pairing); the issue is δ versus the normalised kernel.

| step of the large-field argument | where the hard constraint is used | soft replacement | status of the replacement |
|---|---|---|---|
| (h1) price of a large **fluctuation** | the exact split ‖dA_k‖² = ‖dÃ_{k+1}‖² + ‖dZ_k‖² (2204.07201 eq. (56)): Ã_{k+1} is the constrained minimiser and Z_k ∈ ker Q, so the cross term vanishes; then ζ·e^{−‖dZ‖²/2} ≤ e^{−cp²} | expand the **total** soft action S + Σκu φ at its critical point at fixed coarse field: the linear term vanishes at a critical point, so the split is exact at quadratic order, with the soft Hessian in place of the constrained one | identity elementary; needs the soft background (BFT-0/1) at the coarse field |
| (h2) non-degenerate fluctuation measure | QZ = 0 + axial ⇒ ‖dZ‖² ≥ c‖Z‖² (2204.07201 after eq. (23)) | soft Poincaré: the κ-penalty pins block-average (slow) directions; within-block directions by the Wilson Hessian's Poincaré gap (LINEAR_PACKAGE Thm 2.1, `Δ + aQ_str^†Q_str ≥ min(1/5, a/2)`, at the trivial background) | trivial background: lane statement (pre-S24); at a chart background: one-step conditional positivity (LCONV55 §G2, ARGUED) |
| (h3) "fine small ⇒ coarse admissible" | U_{k+1} = Q(U_k) is a deterministic function; L1d(i)/L1e(b) give coarse regularity from fine regularity | U_{k+1} = (soft) M̄(U_k) + kernel fluctuation: a **new large-field type, the mismatch**, priced by the kernel itself (Lemma MIS below, uniform in the past, all SU(N)) | PROVEN here (MIS) |
| (h4) large-field regions are **frozen** | the RG is localised to the small-field region Ω_k (Dimock 1212.5562 eq. (14): averaging only on Ω_1; 2204.07201: Ω_{k+1} ⊂ Ω_k); no coarse variables exist over Ω_k^c | the fixed chain has coarse variables everywhere, but over the forward cone of a frozen region they integrate out **exactly** (Lemma COL below): for partition functions the fixed chain and Dimock's localised chain coincide | PROVEN here (COL) |
| (h5) price of a large **coarse field** (new region at level k+1) | from the effective density of level k+1: the main term (background action) on admissible fields (2204.07201 §3 (17)-(18), at general k the current effective action) | the same: ρ_{k+1}(V) ≤ (main term at V)·(polymers) on node A's chart, and a **main-term coercivity** clause (BFT-coer, §6.2) gives the price. Proposition FV (RLARGE §3.1) forbids pricing by the *conditional law* given V — in the hard scheme too, since that law is normalised as well (its normaliser IS ρ_{k+1}(V)); FV is not soft-specific | OPEN (BFT-coer), s-scale, inside node A's chart |
| (h6) final integration of frozen fields | crude bounds using stability of the action on the frozen variables (Dimock III) | the same; on SU(N) every variable is compact, so the crude bound is Haar volume ≤ 1 against a Gaussian normaliser: a one-time cost e^{(D/2)log(Ct_j)} per frozen link (§6.1) | elementary |

**The one soft-specific phenomenon.** Over a large-field fine region M̄_c can be short (‖M̄_c‖ ≪ 1, e.g. Haar-random fine links) and
then k_c(·; M̄_c) is nearly uniform: the coarse field above a large fine field is *undetermined*, and S4′ block centres feed every
contour of a coarse link (the first link of each contour starts at c_X), so such a coarse field can stay undetermined for several
levels. In the hard scheme this never arises because those coarse variables are never created. Lemma COL removes it for every
partition-function statement; for statements at a fixed top field, only the top level's column kernels survive, bounded by TL.

### 3.1 Lemma MIS (thresholded mismatch suppression, every SU(N), uniform in the past). PROVEN-HERE (elementary)
Write ψ_c := φ_{M̄_c(U_j)}(U_{j+1,c}) − φ_min(M̄_c(U_j)) ≥ 0 (the kernel's own exponent, centred).
**Statement.** For every stage j with t_j ≥ 1, every past (U_0, …, U_j), every set C of level-(j+1) links and every δ > 0:
  P(ψ_c ≥ δ for all c ∈ C | U_0, …, U_j) ≤ (e c_N⁻¹t_j^D e^{−t_jδ})^{|C|};
and for sets C_j at several stages j ∈ J, under the plain chain law W/Z_K,
  P(∩_{j∈J}{ψ_c ≥ δ_j ∀c ∈ C_j}) ≤ Π_{j∈J}(e c_N⁻¹t_j^De^{−t_jδ_j})^{|C_j|}.
*Proof.* Given U_j, the links of U_{j+1} are independent with densities k_c (Lemma TD; Markov in the level index, as banked in
Proposition B). From Lemma TL's proof, k_c(V) ≤ e c_N⁻¹t^De^{−tψ_c(V)}, so ∫_{ψ_c≥δ}k_c ≤ e c_N⁻¹t^De^{−tδ}; take the product over
c ∈ C. For several stages, condition on U_0, …, U_{j_max} for the event at the last stage (an event in (U_{j_max}, U_{j_max+1})),
bound it by its sup over the past, and induct downward. ∎
*Use.* For a threshold δ ≥ (2D log t_j + s)/t_j the prefactor is absorbed: ≤ e c_N⁻¹e^{−s}. So a **thresholded** route needs no
sharp softening; v3's moment form (M-i) needs Lemma KS (c)'s exact (1 − λ)^{−3/2} (SU(2)) and therefore (KS-N) for N ≥ 3 (RLARGE
row 10e, HYPOTHESIS). **(KS-N) is not an input of a thresholded architecture** (its truth stays NOT-VERIFIED here).

### 3.2 Lemma COL (frozen forward cones integrate out). PROVEN-HERE (elementary)
**Statement.** Let m < K and 𝒞 = (𝒞_{m+1}, …, 𝒞_K), 𝒞_i ⊂ E_i, be **forward closed**: every level-(i+1) link whose S4′ mean M̄
reads a link of 𝒞_i lies in 𝒞_{i+1} (m < i < K). Let F ≥ 0 be any function of the chain variables that reads no variable U_{i,c},
c ∈ 𝒞_i, i > m. Then, for every value of the other variables,
  ∫ F·Π_{i=m}^{K−1}Π_{c∈𝒞_{i+1}}k_c(U_{i+1,c}; M̄_c(U_i)) Π_{i>m}Π_{c∈𝒞_i}dU_{i,c} = F.
*Proof.* The level-K column variables occur only as outputs of their own kernels (nothing reads level K), so each integrates to 1.
After that, the level-(K−1) column variables occur only as outputs of their own kernels: by forward closedness no non-column kernel
reads them, and the level-K column kernels that did are gone. Induct downward to level m + 1. ∎
*Remarks.* (1) The forward cone of a level-m region (all links whose M̄ reads it, recursively) is forward closed. Since S4′ contours
of c = (X, X + e_μ) stay in B(X) ∪ B(X + e_μ), its cross-section shrinks by ~L⁴ per level to O(2^d) coarse sites and then stays
bounded; it reaches level K. (2) Any history decomposition whose indicators read only small-field (non-cone) variables — Balaban's,
where the level-i indicators read the level-i small-field variables only — is compatible with COL. (3) Consequently, for a frozen
region the fixed soft chain costs nothing over Dimock's localised RG; the per-level "shadow" cost of RLARGE (RLF-3′)'s
exp(B_0Σ|sh_k|) is not intrinsic to the fixed chain (see §6.1 for the normalisation argument and its status).

---

## §4. Lemma KA — analyticity of large-field and returned activities in the coarse field (settles the (RLF-5) width; S4-5)

### 4.1 Lemma KA (the soft kernel on the polar tube). PROVEN-HERE (elementary)
For ‖M‖_op ≤ 1 and t > 0 let n_t(V; M) := exp(−t[1 − (2N)⁻¹(tr(V⁻¹M) + tr(M*V))]), V ∈ SL(N, ℂ). It is holomorphic (V⁻¹ = adj V
for det V = 1, so it is entire in the matrix entries), and on SU(N) it equals e^{−tφ_M(V)} (for unitary V, tr(M*V) is the
conjugate of tr(V⁻¹M)). Every V ∈ SL(N, ℂ) is uniquely V = We^X with W ∈ SU(N), X Hermitian traceless (polar decomposition).
**Statement.** |n_t(We^X; M)| ≤ e^{t(cosh‖X‖_op − 1)}·n_t(W; M), uniformly in M (long or short) and W. Hence the holomorphic
kernel k_c^ℂ(V; M) := n_t(V; M)/𝒩_t(M) obeys |k_c^ℂ(We^X; M)| ≤ e^{t(cosh‖X‖ − 1)}k_c(W; M).
*Proof.* With A := W⁻¹M (‖A‖_op ≤ 1): tr(M*We^X) = tr(e^XA*) and Re tr(e^XA*) = Re tr((e^XA*)*) = Re tr(Ae^X) = Re tr(e^XA).
So the real part of the bracket is Re tr(e^{−X}A) + Re tr(e^XA) = 2Re tr(cosh(X)A), and
|n_t(We^X)|/n_t(W) = exp(tN⁻¹Re tr((cosh X − 1)A)). The matrix B := cosh X − 1 is Hermitian, B ≥ 0, ‖B‖_op = cosh‖X‖_op − 1,
so |tr(BA)| ≤ (tr B)‖A‖_op ≤ N‖B‖_op. ∎

### 4.2 Corollaries
**KA-1 (every kernel superposition, at every fine field).** If R(V) := ∫F(U)Π_{c∈C}k_c(V_c; M̄_c(U))dU with F ∈ L¹ (complex or
≥ 0) and V = (V_c)_{c∈C}, then R is holomorphic on the polar tube 𝒯_r := {(W_ce^{X_c})_c : ‖X_c‖_op ≤ r} and
  |R(We^X)| ≤ e^{t(cosh r − 1)|C|}∫|F|Π_ck_c(W_c; M̄_c(U))dU   (= e^{t(cosh r−1)|C|}R(W) if F ≥ 0),
uniformly in F, in the fine field (no smallness of M̄: undetermined columns included) and in W. (Holomorphy by dominated convergence:
|k_c^ℂ| ≤ e^{t(cosh r−1)}e c_N⁻¹t^D on 𝒯_r by KA and TL.) At **r = ρg/√κ** (link units; canonical width ρ/√κ) the growth is
≤ e^{(ρ²/2)cosh r} per link: **g-independent**. This proves for every activity of this form what PLD §9.4 ARGUED for one frozen
activity (width O(g/√κ)).
**KA-2 (g-independent link widths are paid by the activity's own price).** If, in addition, R(W) ≤ e^{−a u·n}·(reference) for a
cluster of n bad cubes and R depends on ≤ c_ℓ·n coarse links through kernels, then on the polar tube of fixed link width α:
  |R| ≤ e^{−(a − c_ℓκ(cosh α − 1))u·n}·(reference),
exponentially small iff α < arccosh(1 + a/(c_ℓκ)) ≈ √(2a/(c_ℓκ)). Hence:
- **Fixed-threshold activities (a fixed):** holomorphy on 𝔇 with a g-INDEPENDENT link width α_E < √(2a/(c_ℓκ)) holds, with the
  price reduced by c_ℓκ(cosh α_E − 1). RLARGE §1.2 (RLF-5) S4-5's "(RLF-5)'s width and (I_k^E)″ (b″) … cannot hold for the same
  polymers" is therefore **REFUTED as an unconditional statement** for such activities. What remains is a **two-sided window**
  (in the sense of PLAN_S26 §12): α_E must be ≤ √(2a/(c_ℓκ)) and ≥ what node A's Cauchy estimates need. At v3's own constants
  (a = θa_bad ≲ 10⁻⁸⁶, RLARGE §0) the upper end is ≲ 10⁻⁴³/√(c_ℓκ): the window's non-emptiness is a node-A question (OPEN).
- **Coupling-scaled activities (price e^{−cp(g)²}, sub-linear in u):** a fixed link width is not affordable (e^{κu(cosh α − 1)}
  beats e^{−cp(g)²} as g → 0): the domain must shrink like link width ≲ g·p(g)/√κ, i.e. **canonical** width ≍ p(g)/√κ — the
  Balaban/Dimock convention of canonical domains growing as the coupling falls (2204.07201; 1512.04373 (286)-(287) per F2's table).
  S4-5 is then settled by option (2) (two classes) or by stating node A's norm in canonical units.
**KA-3 (the coarse envelope exists at every coarse field).** ρ_K(V) = ∫ρ_{K−1}(U)Π_ck_c(V_c; M̄_c(U))dU with ρ_{K−1} ≥ 0, so ρ_K is
holomorphic on 𝒯_r in the coarse variable with |ρ_K(We^X)| ≤ e^{t_{K−1}(cosh r − 1)·4|T|}ρ_K(W) at EVERY coarse field W (large or
small); the same holds per link for every returned polymer. *Scope:* this is analyticity in the **coarse** variable. SRCAN55's
𝒰_ℂ (its §1 table: "sup of a mixed second derivative of the conditional generating function over the complex polydisc") is in the
**source** variables; KA-3 does not bound it. For the source variables, PP-2 (§1.3) is the relevant reduction.

---

## §5. T2(c) — v3 versus an action-priced Balaban-type split: pricing and recommendation

### 5.1 What any d = 4 route must contain (from §2-§4), and what is route-specific
- **Forced in every route:** (i) an in-step **R-operation**: returned large-field clusters renormalised into level-local
  c-numbers, coupling shifts and irrelevant remainders (DENSE: without it Z_K/Z_K^{sf} → ∞); (ii) a **history** of unreturned
  regions, with a FIXED classification threshold and a size cutoff (NOFREEZE; DENSE (iii)); (iii) node A's per-step small-field
  step on regions with holes; (iv) the flow; (v) the final level and assembly.
- **Route-specific:** how an unreturned region is **priced** and how the history is **summed**.
  - v3: in ONE integrand Z(𝔥) = ∫W·1_𝔥 relative to Z(∅), by forward joint moments under conditioned laws μ_{R(𝔥)}, ℛ_𝔥^↑
    (HW Lemma CH, HW^cap, REL-seq), with the coherent-background window (CLS-min) ⇐ (REG-min) (free-boundary, cone-local, at
    non-small coarse fields), the future tilt (LI^F), the in-step price as a probability (SDP)^A, the fine moment (SF-cap)^A,
    (NA-∅), (KS-N), the collar windows W-cb, a per-level shadow cost B_0 = c_LI + c_f + 164ε_♯.
  - Balaban-type (Dimock 2204.07201 §3-§5, 1212.5562 §1, transplanted): **inductively**, level by level, on the effective density:
    a new level-(k+1) large field is priced at stage k+1 by the **main term** of ρ_{k+1} on node A's chart (pointwise, no
    conditioned law — exactly what Proposition FV says carries the suppression: "the suppression of bad V lives in V's own law",
    RLARGE §3.1 item 2), or by the kernel (MIS) for a mismatch; frozen regions' forward cones integrate out (COL); small regions are
    returned in-step; the history is summed by HIST-sum's arithmetic.

### 5.2 Pricing, row by row (RLARGE §4.2 rows; statuses as there unless a REVIEW55/CODEX file changed them)
Legend: **S** shared by any route; **R** R-operation core (forced, DENSE); **V3** v3-specific (not consumed by the recommended
route); **→** replaced by a new item of §6.
| rows (RLARGE §4.2) | class | in the recommended route |
|---|---|---|
| 1, 1a (F_R) ⇐ F-flow ⇐ UNIV-1L; layer-1 inputs | S | unchanged (FLOW55: reduced to (UIR^♮), banked conditionally) |
| 2 (RLF-δ)_k; 2b FI-1 bracket | S | unchanged (FI-1 banked conditionally, CODEX_REVIEW_RLU 2) |
| 3, 3a, 3b, 3c node A (SF^J)_k, N5 uniformity, stage 0, constants | S | unchanged in scope; **form per step** (§5.4): one-step positivity + cluster expansion, on regions with holes |
| 4 (I_k^E)″ [HYPOTHESIS, P]; 4a CL^J restatement | S→ | replaced by the representation (R_m) of §6.1 (same role, P; statement s) |
| 5, 5a, 5b, 6, 14, 15 (W1-ret′^J), (SC), (SF-irr), (H-Mayer^J), I-σ, I-tay^J | R | unchanged (the in-step returned price is their pointwise output, not a probability) |
| 7 (SG^fl)_k | V3 | not consumed (already off the HW route) |
| 8 (BG)_k = BFT-3; 21 assembly; 22 BFT-5; 23 BFT-0..4 | S | unchanged |
| **9 (CLS-min) ⇐ (REG-min) [OPEN, P, "close to circular"]** | V3 | **→ (BFT-coer)** (§6.2): main-term coercivity on node A's chart, a small-field BFT clause; the free-boundary minimum at non-small coarse fields is never needed, because every large-field condition is evaluated on chart fields (§3 (h3), (h5)) |
| **9p (AE) ⇐ (MS-Sob) [P]** | V3 | dropped |
| **10 (H-w′)** (HW^cap + REL-seq on ℛ_𝔥^↑) | V3 | **→** the inductive per-history bound of §6.3 (pointwise; MIS, COL, BFT-coer, node-A locality) |
| 10a (LI^F) [OPEN, s-P] | V3 | dropped (no conditioned law; frozen cones integrate out exactly, COL) |
| **10b (SDP)^A as a probability under ℛ_𝔥^↑ [OPEN, P]** | V3 | dropped (the in-step price is row 5's pointwise bound) |
| 10c (SF-cap)^A; 10d (NA-∅) | V3 | dropped; (NA-∅)'s role → node A's hole-insertion locality clause + assembly |
| 10e (KS-N) [HYPOTHESIS] | V3 | dropped (thresholded mismatch: Lemma MIS, PROVEN for every SU(N)) |
| 10f collar-bad windows, W-cb, (TC), (M-i) on collar links | V3 | dropped (collar conditions are part of the return criterion; W-cb♯ not consumed) |
| 11 (SF-last) + wrap levels | S | unchanged |
| 12 H-4; 17 (SC)/(SF-irr)/(W1-ret′) as inputs of (SDP)^A; 18 non-circularity of (SDP)^A; 19 history-independent rule; 20 (TC) | V3 | dropped (Balaban's indicators read only current small-field variables: COL remark (2)) |
| 13 E10 | S | becomes node A's "regions with holes" (no separate item) |
| 16 (RLF-5) width / S4-5 | R | **settled in substance by Lemma KA** (§4.2): a two-sided window for fixed-threshold activities, canonical units for coupling-scaled ones |
| — the HW/PLD interface ((E2^𝔉′), (CEM^{COL}), (ACT′), (LCR^act′), (BCH-1); refuted as quantified, REVIEW55_HWPLD r55h-18/-26) | V3 | not consumed |
**Count.** Of RLARGE's ~38 open/hypothesis rows, **15 are V3-specific and are dropped**, including **three P-scale walls**
((CLS-min) ⇐ (REG-min); (AE) ⇐ (MS-Sob); (SDP)^A) and the false-as-quantified interface layer. Added: **(BFT-coer)** (s, inside
node A's existing BFT domain), the **(R_m)** statement (replacing row 4), a **shadow-normalisation / tower** item (s, ARGUED here),
and four lemmas **PROVEN here** (MIS, COL, KA, TL; with DENSE, NOFREEZE, PP). The R-operation core (rows 5-6, 14-15) and every
shared node-A / flow / BFT row are unchanged: **the simplification is in the pricing layer, not in the R-operation.**

### 5.3 Recommendation: the action-priced Balaban-type split (§6), with v3's returned-cluster layer kept
Reasons. (1) **FV-compatible by construction:** prices come from the effective density's main term, never from a conditional law
given the coarse field. (2) It **removes the three v3-specific P-scale walls**, one of them "close to circular" (REVIEW_SQ_S2 via
RLARGE row 9), and the conditioned-law layer that REVIEW55_HWPLD found false as quantified. (3) Its only new nonlinear input,
(BFT-coer), lies **inside** node A's chart, where BFT is being proved anyway (BFT-3 banked on the global potential-small domain,
[S26-BANKED] BFT34_55). (4) Mismatch pricing is **unconditional for every SU(N)** (MIS), so (KS-N) disappears. (5) Frozen regions
cost nothing per level (COL), so the per-level shadow constant B_0 and (LI^F) disappear (normalisation argued in §6.3).
(6) Everything route-independent that v3 built is kept: the returned-cluster R-operation, (RLF-δ), FI-1, HIST-sum's arithmetic.
**Risks (stated, not hidden).** (a) The inductive representation must normalise each frozen region at its creation level (§6.3;
ARGUED, not proven); (b) node A must work on regions with holes ("coupling between large and small field regions, which is
abundant", Dimock 2204.07201 §5) — the same burden v3 carries in (SF^J)_k on Λ_k(𝔥); (c) (BFT-coer) must hold uniformly on the
chart; (d) towers (returned regions whose coarse field leaves the chart) must be short — supported at the linearised level by
lg55_2 (§7), not proven nonlinearly; (e) the R-operation core is unchanged in difficulty (P).

### 5.4 How the small-field region is handled per step (answering LCONV55 via the coordinator)
- **Per step, at the background — Balaban's one-step positivity, not global convexity.** At stage k the fluctuation of U_k about the
  soft background bg(U_{k+1}) is integrated with the soft Hessian at bg: the κ-penalty pins the block-average (slow) directions,
  where LCONV55's stripe deficit lives (its §G2: deficit ≈ u_0cβ² against ≈ κu_0), and the Wilson Hessian's within-block Poincaré gap
  controls the fast directions provided the background curvature is ≪ L⁻² in link units (chart smallness). The non-quadratic terms
  are handled by a cluster expansion on the fluctuation cut (coupling-scaled with all failures returned, or fixed with regulator
  norms: §2.3), with an inhomogeneous coupling where sources or tilts require it.
- **LCONV55's "windows do not overlap"** (§G1: convexity needs u t² ≲ 1, a Peierls bound needs u t² ≫ 1) concerns **global**
  convexity of the chain. For **one-step conditional positivity** the conditions are fixed-size: cβ² < κ (kernel beats the stripe
  deficit) and β ≪ L⁻² (Poincaré beats the background curvature), with β the link-size of the background/fluctuation. Both hold on
  a fixed chart β ≤ ε_0, while the Peierls side needs u_kε_cl² ≫ 1 (or u_k(gp(g))² = p(g)² ≫ 1): **compatible** for g ≪ ε_cl ≤ ε_0.
  [ARGUED; the two positivity conditions are LCONV55 §G2's (ARGUED there) plus the elementary Poincaré comparison.]
- **What is not needed.** LCONV55 §G3's (LCR°)/(CEM°)/(SDP)^A-in-tilted-form are obligations of the **HW moment route** (their
  consumers are Corollary E2-RED°, CRC-2T°, CRC-HW°). The recommended route consumes none of them: the small-field bulk bound is
  the per-step cluster expansion itself, assembled level by level.

### 5.5 (TS-up) for the bare gradient-flowed witness (answering HINT2_55 via the coordinator)
- **Verdict on HINT2_55 §R2.4 (ii)** ("(TS-up) for the bare 4D density needs (SRC) plus a sharp large-field estimate; Balaban-type
  e^{−cp(g)²} factors do not suffice via the union bound"): **CONFIRMED** for the union-bound part, and extended: a FIXED cut does
  not rescue it either. With per-block price e^{−a u_j} and aβ < 4 (every cut inside the chart; DENSE's threshold is far above any
  chart radius), Σ_{k/2≲j<k}L^{4(k−j)}e^{−a u_j} ≥ e^{−a u_k}Σ_{r≤k/2}L^{(4 − aβ_+)r} → ∞. No cut-based large-field scheme — v3 or
  the recommended one — delivers (TS-up) by counting.
- **What the recommended mechanism CAN deliver:** the per-level, single-level statement "P(a given level-k block is cut-failing)
  ≤ Ce^{−cost_k}", with cost_k = a u_k (fixed threshold) or c p(g_k)² (coupling-scaled), which is ≪ g_k² in both cases. That is
  exactly what HINT2_55's **Branch D** (deterministic level-local block observable, §R3.3) needs; so H_int is not left open by the
  large-field scheme on that branch (given the scheme's own open items).
- **What it cannot deliver without a new input:** (LF-inst), an action-gap bound for **flow-surviving** concentrations,
  P_j ≤ Ce^{−c_LFu_j} with c_LFβ_− > 4. In the recommended architecture its natural home is the in-step return at level j (a
  conditional bound on a returned tower given chart surroundings), but it needs a lattice **energy-quantisation** statement —
  configurations whose flowed energy at flow time ≍ L^{2k} concentrates at scale L^j must carry action ≥ (8π² − δ)/g_std² near the
  concentration, with the lattice flow's shrinking accounted for — plus the moduli entropy. That is a new P-scale input outside UV
  stability, in every route. **Recommendation:** use Branch D for H_int; treat (LF-inst) as a separate optional item.

---

## §6. T3 — The recommended route, step by step: what is proven, what is argued, what remains

Parameters, fixed in this order (no cycle): (N, L, κ) → node A's chart radius ε_0 → classification threshold ε_cl ≤ ε_0 and
c_co (BFT-coer) → a := c_co·ε_cl² → n_♯ ≥ ⌊4/(aβ_−)⌋ (c_B = 0, §6.3 step 5) → g_0. Node A's fluctuation cut is node A's choice
(§2.3). Histories 𝔥 = (𝒰_0, …, 𝒰_{K−1}): 𝒰_j = the frozen components created at level j (each a *-connected set of > n_♯
cut-failing level-j blocks, or a component whose return failed), with their forward cones (Lemma COL). Λ_m(𝔥) := the level-m
sites outside the cones' level-m cross-sections and their collars.

### 6.1 The target representation (R_m) (replaces (I_k^E)″; OPEN, P; statement s)
There are constants (ε_0, ε_cl, n_♯, a, C, κ_d), independent of K, T, m and the history, such that for every K, T, every m ≤ K
and every level-m configuration U: ρ_m(U) = Σ_𝔥ρ_{m,𝔥}(U) with ρ_{m,𝔥} ≥ 0 and
(a) on Λ_m(𝔥) ρ_{m,𝔥} is node A's small-field formula: main term u_m𝓔_m (coupling shifted by δβ) plus polymers E_m(X), X ⊂ Λ_m(𝔥),
    INCLUDING every returned activity, with polymer bounds ≤ e^{−κ_dd(X)}·(small) uniform in (m, K, T, 𝔥), holomorphic in the
    coarse field on the canonical domain of width ≥ c/√κ (Lemma KA-1 supplies this for returned activities);
(b) each frozen component 𝒟 created at level j contributes a factor ≤ (Ce^{−a u_j})^{|𝒟|} relative to the small-field formula it
    replaces at level j, and **no factor at any level > j** (its cone integrates out, COL; normalisation in step 5 below);
(c) the c-number is Σ_{j<m}N_j(𝔥)e_j with level-local e_j (N_j(𝔥) the level-(j+1) blocks outside the creation-level supports).
Then (LF-UV) ⇐ (R_K) + HIST-sum + final level, and (LF-diff) ⇐ the difference form of (a)-(c).

### 6.2 (BFT-coer) — the only new nonlinear input (OPEN, s; inside node A's BFT domain)
For every level j, region Λ and level-(j+1) configuration V in the chart on Λ's collar (‖1 − V_P‖_op ≤ ε_0), the main term of
ρ_{j+1}'s small-field formula is a sum of nonnegative local densities (up to exponentially decaying, chart-uniform tails) with
  𝓔_{j+1}(V; Λ) ≥ c_co·Σ_{P⊂Λ}‖1 − V_P‖²_op.
At the trivial background this is the coercivity of the linearised background action (the minimal soft action compatible with
the coarse data dominates the coarse Wilson quadratic form: a linear statement); on the chart it is a perturbation of it. It is
(CLS-min) **restricted to chart fields with cut-small finer fields**, which is all the recommended route needs; v3 needs (CLS-min)
at every chain configuration because its moments see every configuration.
**Lemma PRICE (implication; PROVEN-HERE, one line).** Given (BFT-coer) and the polymer bounds of (R_{j+1})(a), for every set S of
level-(j+1) blocks each containing a plaquette with ‖1 − V_P‖ ≥ ε_cl: ρ_{j+1,𝔥}(V)·Π_{B∈S}ζ_B(V) ≤ e^{−a u_{j+1}|S|}·e^{c|S|}·
(the same term with the main term removed on S), a = c_co ε_cl², c the polymer norm per block. *Proof:* split 𝓔 = 𝓔_S + 𝓔_{S^c}
by locality and use 𝓔_S ≥ c_coε_cl²|S|; bound the polymers touching S by their norm. ∎

### 6.3 The inductive step k → k+1, with the status of each sub-step
1. **Small-field step on Λ_k(𝔥)** (node A, per step: one-step positivity at the background + cluster expansion; §5.4). OPEN (I1).
2. **New large fields at level k+1.** Chart fields: priced by Lemma PRICE ⇐ (BFT-coer) [OPEN (I2)]. Mismatches: Lemma MIS
   [PROVEN]. Inside Λ_k(𝔥) with cut-small fine fields the S4′ mean is in the chart (PROOF `L1d(i)`/`L1e(b)` for S4′ iterates,
   "|V(∂p′) − 1| ≤ (1 + 4C_δ)F", pre-S24, cited not re-derived), so a non-chart U_{k+1} there is a mismatch — priced by MIS.
3. **Returns.** Components with ≤ n_♯ blocks whose surroundings and coarse field above are in the chart are integrated in-step;
   the activity is a kernel superposition, holomorphic on 𝒯_{ρg/√κ} with growth ≤ e^{ρ²/2} per link (KA-1) [PROVEN], bounded by
   its creation price [PRICE/MIS]; renormalised after the sea average (rows 5-6, 14-15) [OPEN (I3), P].
   **Towers** (the coarse field above leaves the chart): at the linearised level lg55_2 shows a unit single-link perturbation
   reaches any coarse plaquette with weight ≤ (L−1)/L^d exactly (2/81 at d = 4, L = 3; 4/625 at L = 5), the block-centre hub acts
   on the coarse field as a pure coarse gauge transformation (ω = −1/(2d)) plus a non-gauge remainder ≤ 5/216 (d = 4, L = 3), and
   two levels at a deep centre shrink the plaquette response by 5/162 (L = 3) / 13/1875 (L = 5). [ARGUED + exact linear
   evidence; the nonlinear tower bound is OPEN (I4), s.]
4. **Freezing.** Components with > n_♯ blocks (or failed returns) are frozen at their creation level j; their forward cones
   integrate out exactly (COL) [PROVEN]; on SU(N) the frozen links are integrated with Haar ≤ 1 against a Gaussian normaliser:
   a one-time factor ≤ (e c_N⁻¹t_j^D)^{|links|} (TL's bound), absorbed by the price since a u_j ≫ D log t_j [elementary].
5. **Normalisation (the crux of "no per-level shadow cost").** Above level j the frozen history and the reference differ only on
   the cone: the history has normalised kernels (= 1, COL); the reference Z(∅) = ∫W·1_∅ has the same kernels, restricted by the
   small-field indicators of the cone region, whose conditional probability is ≥ 1 − O(Σ_{i>j}e^{−a u_i})·|cross-section| (the
   cross-section is O(2^d) blocks, COL remark (1)). Exact in the Gaussian model (the frozen variable carries its creation-level
   normalisation; no K-dependent factor). [ARGUED; the nonlinear statement within (R_m) is OPEN (I5), s.] **Fallback** if a
   per-level cost B(u_i) = O(log u_i) survives the bookkeeping: a level-dependent cutoff n_♯(j) ≍ (4 + δ + 38416B(u_j)/log L)/(aβ_−)
   keeps HIST-sum summable with level-local constants (wrap levels stay K-independent because u_j ≍ u_K near the top) [ARGUED;
   HIST §7.4's arithmetic must be re-derived with level-dependent parameters].
6. **History sum.** HIST-sum's arithmetic (RLARGE §5.2) with c_B = 0: n_H = ⌊4/(aβ_−)⌋. [ARGUED (it is HIST-sum with one
   constant set to 0); HIST-sum itself is a pre-S24 CONFIRMED-conditional arithmetic lemma.]
7. **Final level.** (SF-last) at level K; any coarse field is admissible as an argument (TL) [S].

### 6.4 Remaining inputs, named exactly (scale; class)
| id | input | scale | class |
|---|---|---|---|
| I1 | node A per-step small-field package on regions with holes, incl. one-step positivity at chart backgrounds | P×3-4 | shared |
| I2 | (BFT-coer) (§6.2) | s | new, inside BFT |
| I3 | R-operation core for returned components and towers: (W1-ret′^J), (SC), (SF-irr), (H-Mayer^J), I-σ, I-tay^J | P | forced (DENSE) |
| I4 | nonlinear tower (dilution) bound for S4′ (linear evidence: lg55_2) | s | new |
| I5 | frozen-region normalisation (c_B = 0) or the level-dependent cutoff fallback | s | new |
| I6 | (R_m) as an induction (statement s; proof = I1-I5) | P | replaces RLARGE row 4 |
| I7 | (F_R) (FLOW55: ⇐ (UIR^♮)), FI-1 (banked conditionally), (RLF-δ) | P / s | shared |
| I8 | BFT-0..5 | P | shared |
| I9 | final level, wrap levels, assembly | s-P | shared |
| I10 | (LF-diff): the difference form of I1-I6 at every configuration of some level (UNIV (N1)-(N3), SRC (M1)-(M2)) | P | required in every route; not in RLARGE's DAG |
| I11 | (LF-inst) for (TS-up) on the bare-flowed witness | P | outside UV stability; avoidable (Branch D) |
| — | node-A norm decision for (RLF-5): KA-2 window α_E < √(2a/(c_ℓκ)) (fixed threshold) or canonical units | decision | — |
**Proven here (uniform in K and T, from elementary inputs only):** Lemma TL (+ TL-1, TL-2), Lemma PP (+ PP-1, PP-2), Theorem DENSE
(i)-(v), Proposition NOFREEZE, Lemma MIS, Lemma COL, Lemma KA (+ KA-1, KA-2, KA-3), Lemma PRICE (as an implication from I2);
exact checks lg55_1 and lg55_2 (§7).

---

## §7. Check record (criteria written and hashed before each script; exact rational arithmetic; exit 0, empty stderr)

**lg55_1** — Theorem DENSE's density condition ε²A_N(ε)β < 4 on the grid ε = k/1000.
Files: `checks/lg55_1_criteria.md` (sha256 705ecbd6…, written 04:37:12Z before the script), `checks/lg55_1_dense.py`
(23587fce…), `checks/lg55_1_out.txt` (ea102a9d…; a rerun is byte-identical, `lg55_1_out_run2.txt`), `checks/lg55_1_err.txt` (empty).
(The first run's stderr held /usr/bin/time's own report; it was renamed `lg55_1_time_err.txt` and the script rerun with a clean
stderr. Disclosed; the outputs are identical.)
Results (β_up from π > 333/106; β_lo from π < 355/113; "threshold" = the largest grid ε with the condition holding at every
smaller grid point under β_up, and the first failing grid point under β_lo):
| N | 2 | 3 | 4 | 5 | 6 | 8 | 10 |
|---|---|---|---|---|---|---|---|
| ε threshold (β_up) | 0.629 | 0.538 | 0.475 | 0.429 | 0.394 | 0.341 | 0.303 |
| first failure (β_lo) | 0.630 | 0.539 | 0.476 | 0.430 | 0.395 | 0.342 | 0.304 |
| threshold with 1.1·β_up | 0.610 | 0.520 | 0.459 | 0.415 | 0.380 | 0.328 | 0.292 |
Gates: P1 (N = 2 in [0.600, 0.640]) PASS; P2 (N = 3 in [0.500, 0.560]) PASS; P3 monotonicity PASS; P4 non-increasing in N PASS;
controls C1 (fails at ε = 0.682, N = 2) PASS, C2 PASS. Report: the lane's ε_1 = 6.7·10⁻⁴⁰ satisfies the condition for every N.
*Could it have failed?* Yes: P1/P2 were hand predictions with 4-6-point windows; C1 shows the condition does fail inside the grid.

**lg55_2** — exact linearised structure of the S4′ mean (dilution, the block-centre hub, two levels at a deep centre).
Files: `checks/lg55_2_criteria.md` (cd5ed1de…, written 04:38:21Z before the script), `checks/lg55_2_s4p.py` (09f33672…),
`checks/lg55_2_out.txt` (f33cb7eb…; rerun identical), `checks/lg55_2_err.txt` (empty); 2.9 s.
| (d, L) | max \|w^c_b\| | R1 (any link in B(0)) | R1c (links at c_0) | R1(b_0) | R2 (two levels, deep centre) | ω (gauge part) | non-gauge remainder |
|---|---|---|---|---|---|---|---|
| (2,3) | 4/9 | 2/9 | 2/9 | 2/9 | 5/81 | −1/4 | 7/36 |
| (2,5) | 9/25 | 4/25 | 3/25 | 3/25 | 13/625 | −1/4 | 11/100 |
| (3,3) | 19/81 | 2/27 | 2/27 | 2/27 | 5/729 | −1/6 | 11/162 |
| (3,5) | 71/375 | 4/125 | 3/125 | 3/125 | 13/15625 | −1/6 | 17/750 |
| (4,3) | 4/27 | 2/81 | 2/81 | 2/81 | 5/6561 | −1/8 | 5/216 |
| (4,5) | 81/625 | 4/625 | 3/625 | 3/625 | 13/390625 | −1/8 | 23/5000 |
Gates: G0 (contours of (X, μ) stay in B(X) ∪ B(X + e_μ)) PASS; G1 (gauge perturbations give zero coarse curvature exactly; a
non-gauge one does not) PASS; G2 (first-link fraction (L^d − 1)/(2dL^d) for every signed direction, empty first segment 1/L^d)
PASS; H3 (max |w| < 1/2) PASS; H4 (R1 ≤ 1/4 at d = 4 for L = 3, 5, decreasing in L) PASS; H5 (R2 ≤ R1(b_0)/2 at d = 4) PASS.
*Observations (in all six computed cases; not claimed beyond them):* R1 = (L − 1)/L^d; R1c = (m + 1)/L^d; the centre perturbation's
coarse-link response is the pure gauge pattern with ω = −1/(2d) plus a non-gauge remainder that shrinks with L; two levels at a
deep centre multiply the plaquette response by 5/162 (L = 3) and 13/1875 (L = 5).
*Could it have failed?* G1's non-gauge control shows the curvature functional is not identically zero; H4/H5 were genuine
hypotheses (a hub that transmits curvature at full strength would have violated H5 by a factor ≈ 16).
*Scope.* Linearised (small perturbations) only. It supports the tower item I4; it does not prove the nonlinear tower bound.

---

## §8. Errata from a full re-read of §0-§7 (append-only; each item overrides the text it names)
- **E1 (§3, paragraph "The one soft-specific phenomenon").** Overstated. Correct statement: k_c(·; M̄_c) is nearly uniform only
  when t_j‖M̄_c‖_op ≲ 1; an average of many contour transporters, even independently random ones, has ‖M̄‖ ≫ 1/t_j at small g, so
  the kernel stays concentrated (width ≍ (t_j‖M̄_c‖)^{−1/2}) around the polar part of M̄_c — the coarse field above a large fine
  field is random in its polar part, not "undetermined". At a block centre the hub transmits a centre perturbation to the coarse
  links as a coarse **gauge** transformation to leading order (lg55_2: ω = −1/(2d) exactly in the linearisation, non-gauge
  remainder ≤ 5/216 at d = 4, L = 3), so coarse curvature is not fed by the hub; "can stay undetermined for several levels" is
  not supported (linearised decay (L − 1)/L^d per level; 5/162 over two levels at a deep centre). The paragraph's conclusions
  (COL for partition functions; TL at the top level for fixed-U_K statements) are unaffected.
- **E2 (§2.1 (iii)).** The stack count is ≥ |Λ_0|/(18n) (for bare side ≥ n), not |Λ_0|/(9n). Immaterial.
- **E3 (§2.1 (ii), (iv)).** If the small-field indicator covers cube-interior plaquettes only (RLARGE §0 `Indicators`), restrict
  𝒳 to plaquettes interior to level-1 cubes: 2m consecutive integers contain exactly m even ones, so the density is still
  ≥ (m/L)² ≥ 1/9 for L ≥ 3 (bare side a multiple of L), and the plaquettes stay link-disjoint. Statement unchanged. For (iii)
  read "n *-adjacent cubes, each containing one interior test plaquette" (the cluster notion of RLARGE §2.3 is on cubes).
- **E4 (§2.1 "Numbers").** The computed thresholds are 0.629 (N = 2) and 0.538 (N = 3) (§7), inside the hand estimates' windows;
  "≈ 0.62", "≈ 0.53" read 0.629, 0.538.
- **E5 (§5.2 "Count").** "~38 open/hypothesis rows" reads "the 38 rows of RLARGE §4.2's hypothesis list" (some are conditional
  implications, e.g. row 10).
- **E6 (§5.5 first bullet).** The displayed lower bound carries a factor e^{−aR} from (F_R)'s bracket:
  Σ ≥ e^{−a(u_k + R)}Σ_{r≤k/2}L^{(4 − aβ_+)r}. Conclusion unchanged.
- **E7 (§6.3 step 3).** "(L − 1)/L^d exactly" is the observed value in the six computed (d, L) cases, not a proven formula.

---

## §9. Verdicts on inherited claims touched by this file (file + locating string; reason)
- **IV1 — the brief's candidate mechanism** ("the large-field region's contribution is paid by that suppression against
  combinatorial entropy, with no small-field expansion inside it") **as a complete d = 4 mechanism: REFUTED** (Theorem DENSE
  (iv)-(v): log(Z_K/Z_K^{sf}) → ∞ for every bare cut ε ≤ 0.629 (N = 2), 0.538 (N = 3), … and every coupling-scaled cut). As the
  d = 3 mechanism: CONFIRMED (Dimock 2204.07201 §3, eqs. (17)-(19)). Its spirit — price a large field by the action at its own
  level, never by a conditional law — is kept (§5.3) for the unreturned part only.
- **IV2 — Dimock 2204.07201 §3's statement that large-field contributions need no renormalisation, read in d = 4: REFUTED**
  (same reason); in its own d = 3 setting: CONFIRMED.
- **IV3 — PROOF.md `[S6] Proposition LF-count`: CONFIRMED in substance and strengthened.** LF-count concerns the bound; DENSE
  proves the divergence of the quantity, uniformly over coarser-level choices, with explicit thresholds and for coupling-scaled
  cuts. (Its thresholds ε_1 ≲ 1.16 (SU(2)), 0.77 (SU(3)) use a different cost functional, ½‖Δ‖ε², and are not comparable with
  A_N's; no verdict on them.)
- **IV4 — BALABAN_EXTRACT §5 M9 / RLARGE §1.0 ("in d = 4 the large-field regions need the R operation"): CONFIRMED** (DENSE).
- **IV5 — CODEX_REVIEW_BALX F2: AGREE**; NOFREEZE adds the d = 4 rule (a coupling-scaled cut can only be an integration cut with all
  failures returned; histories need a fixed threshold). **F3: AGREE** as algebra; it does not bear on large-field summability.
- **IV6 — RLARGE §1.2 (RLF-5), S4-5: "(RLF-5)'s width and (I_k^E)″ (b″) … cannot hold for the same polymers": REFUTED as an
  unconditional statement** for fixed-threshold activities (Lemma KA-2: holomorphy at a g-independent link width α_E holds when
  α_E < arccosh(1 + a/(c_ℓκ)), at a reduced price); it is correct for coupling-scaled activities, where canonical units are
  forced. **Correction:** S4-5 is a two-sided window (α_E between node A's Cauchy needs and √(2a/(c_ℓκ))), not a conflict.
- **IV7 — PLD §9.4 as quoted in RLARGE §1.2 (RLF-5) ("ARGUES width O(g/√κ) for one frozen activity"): CONFIRMED and generalised**
  (KA-1, PROVEN for every kernel superposition at every fine field). I did not read PLD §9.4 itself; the verdict is on the quote.
- **IV8 — RLARGE §4.2 row 10e, (KS-N) as an input of the large-field route: REFUTED as a necessary input** (Lemma MIS prices
  thresholded mismatches for every SU(N)); the truth of (KS-N) itself: NOT-VERIFIED.
- **IV9 — UNIV55 §2.4(B) "the set … has ν^G-probability bounded below": CONFIRMED** (Lemma TL-2, with the matching upper bound).
- **IV10 — UNIV55 §3.1 (N3), first alternative ("BFT extended to backgrounds of bounded but not small curvature") as needed:
  REFUTED as necessary** (PP-1: a sup-form comparison passes through common kernels without loss); (N3) as an instance of the
  large-field form of (N1) (UNIV55's second alternative): CONFIRMED.
- **IV11 — SRCCD55 §6 "(M2) SRC-κ-LF at large coarse fields" as a separate requirement: REFUTED as separate** (PP-2: it reduces to
  the per-level difference-form bound at any finer level, i.e. I10). The underlying requirement (I10): CONFIRMED.
- **IV12 — SRCAN55 §4 (N-1) "The complex envelope 𝒰_ℂ(U_K) is not even defined at large coarse fields": NOT-VERIFIED here.**
  𝒰_ℂ is in the source variables; KA-3 concerns the coarse variable. PP-2 reduces its large-coarse-field part to I10.
- **IV13 — HINT2_55 §R2.4 (ii) (union bound fails; (TS-up) needs (SRC) + (LF-inst)): CONFIRMED for the union-bound failure**, and
  extended to fixed cuts (§5.5); **the necessity of (LF-inst) specifically: NOT-VERIFIED** (HINT2_55 itself labels it ARGUED).
- **IV14 — LCONV55 §G1 "the convexity window and the Peierls window are disjoint": CONFIRMED for global convexity** (its convexity
  side not re-derived; accepted as stated, Codex review pending); **not applicable to one-step conditional positivity** (§5.4).
- **IV15 — LCONV55 §G3 "(LCR°) ⟸ [one-step conditional positivity] + [inhomogeneous cluster expansion] + [(LC-3′)^tilt]" as an
  obligation of node A: REFUTED as an obligation of the recommended architecture** (its consumers are HW-route items, not
  consumed); as a statement about the HW route: not judged.
- **IV16 — RLARGE §3.1 Proposition FV and its Lesson item 2: CONFIRMED** (as a conditional statement; its logical point — a
  normalised conditional law cannot carry the price — holds in the hard scheme too) and identified with Balaban's ordering:
  price level-(k+1) large fields at stage k + 1 by ρ_{k+1}'s main term.
- **IV17 — RLARGE §1.2 (RLF-3′)'s factor exp(B_0Σ_{(j,𝒟)}Σ_{k≥j}|sh_k(𝒟)|) as intrinsic to the fixed soft chain: REFUTED as
  intrinsic** (Lemma COL: forward cones integrate out exactly); whether a representation keeps a per-level cost is a
  normalisation question (§6.3 step 5, ARGUED).
- **IV18 — CODEX_REVIEW_RLU "Exactly what may be banked" 1-5: AGREE** (W-cb♯ not consumed here; FI-1 kept).
- **IV19 — REVIEW55_HWPLD r55h-18, r55h-25, r55h-26: AGREE** (used as evidence only; not re-derived).

## §10. Summary table — every claim made or judged in this file
| id | claim (place) | verdict / status |
|---|---|---|
| lg-1 | Lemma TL: e^{−2t_j\|E_{j+1}\|}Z_K ≤ ρ_{j+1} ≤ (e c_N⁻¹t_j^D)^{\|E_{j+1}\|}Z_K at every configuration (§1.2) | PROVEN-HERE |
| lg-2 | TL-1 (sup-form ⟺ integrated L6-soft at the top), TL-2 (coarse law ≍ Haar per volume) (§1.2) | PROVEN-HERE |
| lg-3 | Lemma PP (positivity/difference propagation) (§1.3) | PROVEN-HERE |
| lg-4 | PP-1 ((N3) not separate), PP-2 ((M2) not separate) (§1.3) | PROVEN-HERE (implications) |
| lg-5 | (LF-UV), (LF-diff) are the minimal statements; sufficiency and clause-wise minimality (§1.4) | ARGUED (sufficiency as implications given node A, flow) |
| lg-6 | Theorem DENSE (i)-(v) (§2.1; constants per E2, E3) | PROVEN-HERE |
| lg-7 | DENSE thresholds 0.629 / 0.538 / 0.475 / … (§7) | PROVEN-HERE (exact, lg55_1 PASS) |
| lg-8 | Proposition NOFREEZE (§2.2) | PROVEN-HERE (arithmetic; bare-level reading unconditional; level-j reading assumes the analogous lower bound) |
| lg-9 | fixed link cut: cubic vertex not absolutely small, relatively small (§2.3) | PROVEN-HERE (elementary; not load-bearing) |
| lg-10 | hard-constraint usage (h1)-(h6) and soft replacements (§3 table) | ARGUED (reading of the corpus + elementary facts) |
| lg-11 | Lemma MIS (§3.1) | PROVEN-HERE |
| lg-12 | Lemma COL (§3.2) | PROVEN-HERE |
| lg-13 | Lemma KA (§4.1) | PROVEN-HERE |
| lg-14 | KA-1, KA-2, KA-3 (§4.2) | PROVEN-HERE (KA-2 as an implication from the activity's price and dependence count) |
| lg-15 | Pricing: 15 of RLARGE's 38 rows are v3-specific and dropped, incl. three P-scale walls (§5.2) | ARGUED (classification) |
| lg-16 | Recommendation: action-priced Balaban-type split with v3's returned-cluster layer (§5.3) | ARGUED (recommendation, risks listed) |
| lg-17 | One-step positivity and Peierls windows are compatible (§5.4) | ARGUED |
| lg-18 | No cut-based scheme gives (TS-up) by counting (§5.5) | PROVEN-HERE (arithmetic) |
| lg-19 | The recommended scheme supports HINT2's Branch D (§5.5) | ARGUED |
| lg-20 | (R_m) target (§6.1); (BFT-coer) (§6.2) | statements; OPEN |
| lg-21 | Lemma PRICE (§6.2) | PROVEN-HERE (implication from (BFT-coer)) |
| lg-22 | Linearised S4′ dilution, hub = coarse gauge transformation, two-level deep-centre decay (§6.3 step 3, §7) | PROVEN-HERE for the six computed (d, L) (exact, lg55_2 PASS); nonlinear OPEN |
| lg-23 | No per-level shadow cost (c_B = 0) (§6.3 step 5) | ARGUED |
| lg-24 | Level-dependent cutoff fallback keeps HIST-sum summable with level-local constants (§6.3 step 5) | ARGUED |
| IV1-IV19 | inherited claims (§9) | CONFIRMED: IV3, IV4, IV7, IV9, IV13 (union bound), IV14 (global), IV16 and the confirmed halves of IV1, IV2, IV10, IV11; REFUTED: IV1 (d = 4), IV2 (d = 4), IV6, IV8 (as needed), IV10 (first alternative as needed), IV11 (as separate), IV15 (as an obligation here), IV17 (as intrinsic); NOT-VERIFIED: IV8 ((KS-N) truth), IV12, IV13 ((LF-inst) necessity); AGREE with Codex: IV5, IV18; with Opus 5.5: IV19 |

## §11. For the lead
1. **First principles.** The full theorem needs from large fields exactly two statements (§1.4): (LF-UV) — the large-field part of
   the free energy is a level-local c-number plus a coupling shift plus O(|T|), also with complex local sources — and (LF-diff) —
   its difference form at every configuration of some level. Nothing is needed "at large coarse fields" beyond these: Lemma TL makes
   every top-level partition statement free, Lemma PP carries every sup-form comparison through the top levels at no cost, so
   UNIV55's (N3) and SRCCD55's (M2) are not separate inputs. Neither statement gives (TS-up).
2. **The brief's simpler mechanism is refuted for d = 4** (Theorem DENSE): bare large fields are dense for every cut up to 0.629
   (SU(2)), 0.538 (SU(3)), and for every coupling-scaled cut; Z_K/Z_K^{sf} → ∞. An in-step R-operation is forced in every route,
   and (NOFREEZE) histories need a FIXED threshold; a coupling-scaled cut (CODEX F2) can serve only as an integration cut whose
   failures are all returned.
3. **Recommendation (§5.3): keep v3's returned-cluster R-operation and HIST-sum arithmetic; replace its pricing layer** (HW/PLD/SQ
   moments under conditioned laws) by Balaban's inductive pricing at each level by the effective density's main term. This drops
   15 of RLARGE §4.2's 38 rows, including three P-scale walls ((CLS-min) ⇐ (REG-min), "close to circular"; (AE) ⇐ (MS-Sob); (SDP)^A)
   and the interface REVIEW55_HWPLD found false as quantified, and adds one small-field clause (BFT-coer) inside node A's chart.
   The hard constraint enters the large-field argument at (h1)-(h5) (§3); each has a soft replacement, two of them proven here
   (MIS for mismatches, COL for frozen columns).
4. **Proven here, uniform in K and T:** TL, PP, DENSE, NOFREEZE, MIS, COL, KA (with KA-1..3), PRICE; exact checks lg55_1, lg55_2
   (both PASS, criteria pre-registered). **Remaining inputs, named:** I1-I11 (§6.4). The new ones are I2 (BFT-coer), I4 (nonlinear
   tower bound; linear evidence lg55_2), I5 (frozen-region normalisation, or a level-dependent cutoff); I10 ((LF-diff)) is required by
   UNIV/SRC in every route and is missing from RLARGE's DAG; I11 ((LF-inst)) only for the bare-flowed witness — use HINT2's Branch D.
5. **What should change in PROOF.md / HANDOFF (for the lead to decide; nothing is edited here).** No tally change. HANDOFF's row
   "BFT off 𝒞_glob (large fields)" should read: *"R-operation forced (LARGE55 DENSE); recommended pricing = Balaban-type inductive
   (LARGE55 §5-§6), not RLARGE v3's HW moments; open: I1-I6, I10 (LARGE55 §6.4)"*. RLARGE §7's critical path should drop rows 7, 9,
   9p, 10, 10a-10f, 12, 17-20 if the recommendation is adopted. S4-5 (RLARGE U2) is a two-sided window, not a conflict (KA-2).
   (KS-N) leaves the critical path (MIS). Node A's residual should be the per-step package (LCONV55 §G2 + cluster expansion); its
   §G3 tilted-moment obligations exist only on the HW route.
6. **Codex verdicts used:** CODEX_REVIEW_BALX F2, F3 — agree; CODEX_REVIEW_RLU 1-5 — agree. Opus 5.5 verdicts used: REVIEW55_HWPLD
   r55h-18/-25/-26 — agree. No disagreement with any Codex verdict.


## §12. Errata, second pass (append-only; found on a full re-read at ≈04:50Z; each item overrides the text it names)
- **E8 (§0, last bullet).** "(§5.5, §5.6)" reads "(§5.4 for LCONV55, §5.5 for HINT2_55)".
- **E9 (§1.4 "Minimality", last sentence).** "by PP-1 that is equivalent to sup over configurations of any finer common level" is
  wrong: PP-1 gives one direction only (a finer-level sup-form comparison IMPLIES the ℓ_0 one). Correct: the weakest statement
  Proposition T itself needs is the global sup_V comparison at ℓ_0 ((U-dens)); (LF-diff) is the natural RG-level **sufficient**
  form, and PP-1 shows that nothing specific to the last levels is needed beyond it. (LF-diff) is not claimed minimal.
- **E10 (§2.1 "What it refutes", Claim B bullet).** The reduction "any argument … proves Claim B" needs the small-field part of
  each history Ω to be bounded by e^{E′|Ω^c|}·Z_K^{sf} (as it is in Dimock's scheme, where it is a small-field partition function
  on Ω). With that qualification the reduction holds; DENSE (iv) refutes Claim B itself without qualification.
- **E11 (§2.2 "Consequence", last two sentences).** "With a fixed threshold the bare n-cluster count tends to 0 exactly when
  nε²A_Nβ_* > 4 … the RLF n_♯ structure is forced, not chosen" overstates. DENSE gives only a LOWER bound: the count DIVERGES
  whenever nε²A_N(ε)β_* < 4. That large components are rare needs an UPPER bound P ≤ (Ce^{−a u})^n with naβ_− > 4 — the history's
  price, which is OPEN at levels ≥ 1 (I2, I6). What is forced is that **small** components cannot be unreturned; a finite n_♯ that
  works exists only once the upper bound is proven.
- **E12 (§5.1 (ii)).** "a history of unreturned regions … forced in every route" overstates: returning every component (towers,
  no frozen category) is possible in principle. Correct: *if* unreturned regions are used, they need a FIXED threshold and a size
  cutoff (NOFREEZE, DENSE (iii)); small components must always be returned (DENSE).
- **E13 (§6 parameter order; §6.1 (b); §6.3 steps 5-6; §10 lg-23).** "No per-level shadow cost (c_B = 0)" is too strong. The cone's
  lateral boundary cuts small-field polymers at every level it crosses, giving a per-level factor e^{O(η)·|∂(cross-section)|}, η
  node A's polymer norm per block: a **constant** (and small) per-level cost, not zero. What the normalisation argument removes is
  any K- or u-dependent per-level cost and any conditioned-law constant (c_LI, REL-seq's 164ε_♯). HIST-sum absorbs a constant:
  n_♯ ≥ n_H = ⌊(4 + c_B)/(aβ_−)⌋ with c_B := 38416·O(η)·|∂|/log L. Read "c_B = 0" as "c_B = O(η), a constant"; (R_m)(b)'s "no
  factor at any level > j" as "no K-dependent factor; a constant per-level boundary factor". Status unchanged: ARGUED (I5).
- **E14 (§6.3 step 5).** The phrase "whose conditional probability is ≥ 1 − O(Σ_{i>j}e^{−a u_i})·|cross-section|" is itself a
  large-field bound for the reference's cone region; inside the induction it must come from the same pointwise pricing
  (PRICE/MIS) applied to the reference's representation, not from a conditioned law. As written it is part of the ARGUED
  normalisation, not an independent input.
- **E15 (§6.3 step 2; §6 parameter order).** L1e(b) bounds the coarse curvature by (1 + 4C_δ)F with F the fine curvature **in
  coarse units** (F = L²×fine plaquette size). So "the S4′ mean is in the chart" needs (1 + 4C_δ)L²ε_cl ≤ ε_0: the parameter order
  must read ε_cl ≤ ε_0/((1 + 4C_δ)L²), not ε_cl ≤ ε_0.
- **E16 (§6.1 (c), §1.4 (LF-UV)).** Returned towers make a level's c-number depend on the couplings of the few levels below the
  return level (with weights decaying in the tower height, I4). Read "level-local" as "quasi-local in scale: a function of
  (g_i)_{i ≤ j} with dependence on g_{j−h} weighted by the tower-height decay". Tautology is still excluded (no dependence on K or T).
- **E17 (§9 IV10, IV11).** UNIV55 (N3) offers two alternatives and does not claim the first is necessary; my "REFUTED as necessary"
  refutes a claim not made. Correct verdicts: **IV10 — "(N3) is a requirement specific to the last j_0 levels below ℓ_0": REFUTED**
  (PP-1 crosses those levels with no loss in the global sup-form δ_d); **the requirement it encodes — the large-field form of (N1)
  at every configuration, which UNIV55's (N1) already states ("INCLUDING large-field regions"): CONFIRMED.** IV11 (SRCCD55 (M2))
  likewise: "specific to the last levels" REFUTED (PP-2); the underlying per-level difference-form requirement (I10) CONFIRMED.
- **E18 (§3 table (h6); §3.2 remark (3)).** The pointers "§6.1" read "§6.3 step 4" and "§6.3 step 5" respectively.
- **E19 (§4.2 KA-2).** At a = 10⁻⁸⁶ the upper end √(2a/(c_ℓκ)) is ≈ 1.4·10⁻⁴³/√(c_ℓκ) (the text's "≲ 10⁻⁴³/√(c_ℓκ)" is the order).
- **E20 (§5.5 first bullet).** "aβ < 4 (every cut inside the chart …)": the precise reason is that a VALID per-block price exponent
  a cannot exceed the true cheapest cost, which is ≤ ε²A_N(ε) by DENSE (i) at the bare level (and by the analogous construction
  at level j, not proven here), and ε²A_N(ε)β_+ < 4 below DENSE's threshold.
**Counts after E17 (replacing §10's last row).** Inherited claims judged: **CONFIRMED 11** (IV1 for d = 3, IV2 for d = 3, IV3, IV4,
IV7, IV9, IV10's encoded requirement, IV11's encoded requirement, IV13's union-bound part, IV14 for global convexity, IV16);
**REFUTED 8** (IV1 for d = 4, IV2 for d = 4, IV6, IV8 as a necessary input, IV10 as last-level-specific, IV11 as last-level-specific,
IV15 as an obligation of the recommended architecture, IV17 as intrinsic); **NOT-VERIFIED 3** (IV8's (KS-N) truth, IV12, IV13's
(LF-inst) necessity); agreements with reviews: IV5, IV18 (Codex), IV19 (Opus 5.5). Own claims: PROVEN-HERE 15 (lg-1, 2, 3, 4, 6,
7, 8, 9, 11, 12, 13, 14, 18, 21, 22), ARGUED 8 (lg-5, 10, 15, 16, 17, 19, 23, 24), OPEN statements 1 (lg-20).

## Closing provenance
Deliverable final at the `date -u` below. Model: claude-opus-5-5. Files written by this worker: `LARGE55.md`;
`checks/lg55_1_criteria.md`, `checks/lg55_1_dense.py`, `checks/lg55_1_out.txt`, `checks/lg55_1_out_run2.txt`,
`checks/lg55_1_err.txt`, `checks/lg55_1_time_err.txt`; `checks/lg55_2_criteria.md`, `checks/lg55_2_s4p.py`, `checks/lg55_2_out.txt`,
`checks/lg55_2_out_run2.txt`, `checks/lg55_2_err.txt`, `checks/lg55_2_err_run2.txt`, `checks/lg55_2_time.txt`. No git command was run.
The Balaban-method corpus was read as data only; nothing from it is copied into the repository beyond short attributed phrases.
Thu Oct 29 04:46:59 UTC 2026
