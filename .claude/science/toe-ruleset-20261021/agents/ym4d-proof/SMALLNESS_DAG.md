Reviewer model: claude-opus-5-5

# SMALLNESS_DAG — the live route's constants and thresholds as one dependency graph (Step 5, target T56-5, RTARGET §55)

UTC at first write: 2026-10-28T23:02:25Z
Worker: Opus 5.5, effort max. Writes only this file and `checks/dag55_*`. No git. Append-only from here on.

## PRE-STATED (statements only; written before any node is placed, any edge drawn, or any script exists)

Read before writing this section: the step-5 brief, REVIEW_BRIEF_55.md, RTARGET.md §55 and its correction,
PLAN_S26.md, HANDOFF.md, REVIEW55_ARS.md (complete), REVIEW55_CONST.md (as on disk at 23:02Z — its mtime is
23:02:19Z, so it is still being written; to be re-read before finishing). Nothing else has been opened yet.

### Targets (RTARGET §55 T56-5, sharpened by the lead's two updates)

D1. **Node census.** Every constant and threshold on the LIVE route, each as a node with its defining
    file + locating string: (a) RLARGE's RLF-step v3 live constant list (C_ℓ, B_0, E_0, a, n_♯) and RLARGE §0's
    thresholds; (b) PROOF.md's N5/BR1 constants (𝔠_∞, C_♭, C_θ, ε_br, ε_*); (c) the BFT clause constants
    (REVIEW_S22.md, the block the brief places at l.385-435 — located by string, drift reported); (d) the SF, HW
    and PLD constants that feed (a)-(c); (e) the existence lane's consumers of (a)-(d). Structural inputs
    (N, L, d, κ_±, κ, β_±, …) are source nodes. g_0 (and the coupling schedule g_k) is the sink.
D2. **Edge census.** Every constraint "A ≤ f(B, …)" (or "A is defined from B, …", or "B must be small given A")
    as a directed edge B → A ("A's value or admissibility needs B fixed first"), each with its file + locating
    string. An edge whose source text I cannot locate is not drawn.
D3. **Symbol discipline (DAG-F3).** A node is placed only if its symbol resolves, by definition site, to one
    object. Each collision the brief names (≥6 ε_1, 4 ε_*, 4 θ_0, ≥13 C_1, ≥11 c_1, ≥5 κ; c_RS, n_♯, q, θ, α, M,
    Q_str, C_♭) is either resolved by a site-tagged node name (e.g. `eps1_chiQ@RLARGE`) or listed as DAG-F3
    unplaced. Never guessed.
D4. **Live-route discipline.** No edge is built from a claim that REVIEW55_ARS / REVIEW55_CONST / REVIEW55_NORMS /
    REVIEW55_TUNIF / REVIEW55_LEAD refuted, and no node is treated as live if a re-review shows it has no live
    consumer (e.g. a_RS, η_1 = η_RS per REVIEW55_ARS F01). Such items are listed separately as off-route.
D5. **Checker (criteria file first).** `checks/dag55_1_criteria.md` written before `checks/dag55_1_dag.py`. Plain
    python, no third-party imports, no floats in any verdict. It must report (i) every directed cycle (DAG-F1),
    with each node and each edge's file:string on it; (ii) every node whose defining text makes it grow with K
    (number of RG steps) or with T (the coarse side) (DAG-F2), and every node downstream of such a node whose
    own definition does not absorb the growth; (iii) a topological order of the acyclic part. **Designed-FAIL
    control:** the same checker, run on the same graph with one injected back-edge that closes a known cycle,
    must report that cycle (and a control injecting a K-growing source must report DAG-F2). A checker whose
    control does not fire is reported as unable to decide.
D6. **Volume (owner's update 2).** Every node is tagged with its volume behaviour: uniform in K and T; uniform at
    fixed T only (grows, or is unstated, as T → ∞); K-dependent; or unstated. The R^4 target makes "uniform at
    fixed volume only" a defect to report, not an acceptable state.

### What would count as each outcome (fixed now)

- **DAG-F1 (cycle):** a directed cycle among placed nodes, every edge on it carrying a located source string. A
  cycle that exists only through an edge I could not locate, or through an off-route item, is reported as such
  and not counted. A cycle that is broken by an explicit "fix X first, then Y" quantifier in the source text is
  not a cycle; the order-setting text is cited.
- **DAG-F2 (growth):** the node's own definition (or a cited bound on it) contains K, k, T, R, L^{k}, log T, T^d,
  a level count, or a volume, without a stated uniform bound. "Uniform" is accepted only with a located
  statement; "unstated" is reported as its own class, not as uniform.
- **DAG-F3 (unplaceable):** the symbol at the consuming site has two or more candidate definition sites and the
  consuming text does not decide between them.
- **A refutation of the DAG itself:** an edge I draw whose source text, re-read, does not say what I attribute to
  it; or a node I mark live that a re-review marks unconsumed. I re-read each edge's string once before the
  checker runs; anything that fails that re-read is removed and listed.
- **The topological order** is reported only for the acyclic graph actually built; it is the proof's quantifier
  order **only for the nodes placed**, and the report says how many candidate nodes were left unplaced.

### What this file will not do

Re-price decades; re-derive estimates; pick between rival constants; bank any status. It records what the
text says depends on what, where, and whether the graph closes.

---

## 0. What was read, what was built, and how it was checked (appended 2026-10-28T23:46Z UTC, after the checks ran)

**Read in full:** the step-5 brief, REVIEW_BRIEF_55.md, RTARGET §55 (+ correction), PLAN_S26.md, HANDOFF.md, REVIEW55_ARS.md,
REVIEW55_NORMS.md, REVIEW55_TUNIF.md, REVIEW55_LEAD.md, REVIEW55_CONST.md (re-read complete at 23:44Z: it now ends with its
summary table), REVIEW55_HWPLD.md (findings F1-F22), RLARGE.md l.1-845 (the whole live v3 text and the v3 reading notes of
Appendix A), REVIEW_S22.md l.370-436 (the BFT statement; the brief's "l.385-435" has drifted by about −2), CODEX_REVIEW_TUNIF2.md
(complete, "Review completed: 2026-10-28 23:09:35 UTC"). **Read by string-located range:** PROOF.md (N5-sf0 l.5614-5700, RW-ℓ²
and 𝔠_∞ l.5765-5880, N5-an♭ + BR1 l.5880-5970, CURV1 l.6258-6300, the C_♭ recursion and NAH-unif l.6336-6380, the [S23]
cross-lane map l.6810-6880); HW.md §13.2, §18.1-§19, §30.5-§30.6, Lemma W-cb; SF.md (DX′ l.2040-2100, (TH-ch′)/(TH-ch″) and
the O0 order l.2176-2230, the radius chain l.1990-2010, τ^A/τ^♯ l.2505-2545); SQ.md (SUP-price l.180-230, DESC-ε l.310-350,
RES-dec/STOKES-it l.1097-1160, EPS-T l.1455-1500, EPS-0b-avg/EPS-0 l.1600-1645); FLOW.md l.55-80, l.418-475; HIST.md (PM/RS-lin
l.137-172, CL^J l.205, (I_k^E) l.840-875); PLD.md §16.8; EPSSTAR.md §3.2, §6.1-§6.2 and l.505-530; CONST_T.md l.181; BFT_B.md
§32.1 and §43.3; REVIEW_BFT_B_S9_S10.md S10-6/S10-7; REVIEW55_BFTB.md (Finding 6, 7 and its closing); KFACTOR_O55.md §1-§3, §6,
§10 (Step 4's worker file, read at 23:44Z; see §4); BALABAN_EXTRACT.md §3 (skimmed, for the threshold convention);
EXISTENCE.md §20.2 and §21.3; SYMBOLS.md §4.1, §5.1, §6.1. Everything else by grep.

**What the DAG is.** A node is a constant, a threshold, or a statement that carries constants (e.g. (SDP)^A's C_A, a_A, c_A;
BFT's ε_0, r_ℂ, m_0, C_0), each with a defining file and a locating string. An edge src → dst means *src must be fixed
before dst* — dst is defined from src (`def`), constrained by an inequality in src (`le`), ordered after src by explicit source
text (`order`), needs src as a hypothesis (`req`), depends on src only through a law family indexed by src whose uniformity is
not stated (`implicit`), or is tied to src by a fixed-point condition on a sequence (`fixedpoint`). Growth tags follow
`checks/dag55_1_criteria.md`. The graph is `checks/dag55_2_graph.py` (189 nodes, 362 edges); the checker is
`checks/dag55_2_dag.py`; the output is `checks/dag55_2_out.txt`.

**Check record (criteria always before script; all three runs exit 0, empty stderr).**
- `checks/dag55_1_criteria.md` (23:10:58Z) + Addendum A (23:16:05Z: S2 string audit, C7) → graph `dag55_1_graph.py` → checker
  `dag55_1_dag.py` → run 23:39:08Z → `dag55_1_out.txt`. All seven controls fired as designed.
- `checks/dag55_2_criteria.md` (23:41:46Z) lists seven graph omissions I found on re-reading dag55_1's output (no code defect);
  `dag55_2_graph.py` = dag55_1's graph + those additions; `dag55_2_dag.py` = byte copy of dag55_1_dag.py except the graph path
  (diff shown in the session: two lines). Run 23:42:10Z → `dag55_2_out.txt`. **The binding results are dag55_2's.** The
  pre-registered expectation (B-strict unchanged, one more weak seed) held.
- `checks/dag55_3_criteria.md` (23:44:05Z, POST-HOC: designed while building the DAG, not after any dag55 output) →
  `dag55_3_tc.py` → `dag55_3_out.txt`: the (TC) feasibility question RLARGE calls U3 (§8.1 below).
- **Disclosure 1 (drafting helper).** I drafted the graph in my scratchpad and used a scratch helper that greps every locating
  string before writing the data file; so S2's PASS on the real graph is a transcription guard, not evidence of care. The
  evidence that the strings say what the edges claim is the manual re-read below. S2's discriminating power is shown by C7.
- **Disclosure 2 (dag55_1_graph regenerated once before its first run).** At 23:37Z I deleted and regenerated
  `dag55_1_graph.py` (adding the six DAG-F3 nodes) before the checker existed; no run had used the first version.
- **Manual re-read (pre-stated in D5).** Before dag55_1 ran I printed all 353 draft edges with their strings and re-read each
  against its source. Removed as not supported on the live route: three edges from CURV1's constants (C_θ, ε_θ) into the
  level-uniform N5 threshold and one BFT-4 → C_θ edge — REVIEW_S22 Part 5 says that with BFT "NAH-unif′, HG-ind's uniform
  form and (H-K) all become unnecessary", so CURV1's constants feed only the per-level route (they were re-pointed to that
  route's ε_unif and their nodes marked `off`). Re-stringed five edges whose first string was weaker than the source allows.

**Model provenance.** The worker is claude-opus-5-5 (line 1). The review files used as the guide (REVIEW55_*) are Opus 5.5
files; CODEX_REVIEW_TUNIF2 is a Codex gpt-6-astra/max file (banner not inspected by me). KFACTOR_O55 is an Opus 5.5 worker
file not yet cross-family checked (its own §10 asks for a Codex review of its Lemma TR).

---

## 1. HEADLINE

1. **DAG-F1 — the written hierarchy is acyclic.** On every `def`/`le`/`order`/`req` edge (358 of 362) the checker finds no
   strongly connected component (B-strict: NOT FOUND). Two cycles exist only when the 4 remaining edges are added (B-all):
   **(a) the n_♯ loop** — the cutoff n_♯ indexes the law family on which node A's (SDP)^A / (PRICE^ℛ) must hold, while n_♯ is
   computed from those laws' constants; HW's explicit order puts the constants first, which is consistent **only if node A
   proves them uniform in the cutoff n_♯ — a quantifier no source states** (§3.1). **(b) FI-1** — the kernel couplings fix the
   stage constants, which fix δβ_k, which fixes the effective couplings, which equal the kernel couplings (A5): a fixed-point
   problem for the coupling sequence, not a smallness cycle; RLARGE's Option A bounds the stage constants by the a-priori
   bracket (R alone), which removes it from the constants hierarchy, but Option A is "an integration choice", U4 (§3.2).
   Four further loops in the text are broken by explicit order statements, each cited (§3.3).
2. **DAG-F2 — one live K-growth reaches g_0; nothing on the live route grows with T.** The single live seed with a real
   level-count factor is **C_fun**, the curvature-half constant of (CO-fun)/(NC-Γ) at critical points (Corollary COF-crit:
   "PROVEN as an implication with a constant that grows like k", REVIEW_BFT_B_S9_S10 S10-6; "Not k-uniform", REVIEW55_BFTB
   Finding 6). Its witness path to the sink is **C_fun → BFT-5 (b) → (a5-G♯) → Theorem A5 → (I_k^E)″ → (SDP)^A's C_A → g_0**;
   it also reaches FLOW's γ and g_1 (through C_ρ) and the existence lane's g_3, g_c. **Step 4 (KFACTOR_O55, Opus 5.5, not yet
   cross-checked) reports that this factor is absent at critical points (its Lemma TR) and a norm artifact in the contraction
   (ARGUED)**; if Lemma TR survives review, the live route has **no** K- or T-growth seed left except the vacuum c-number
   𝒱_K^{LF}, which grows with K and |T| by design and is subtracted inside (NA-∅) (an absorbing edge; the checker confirms it
   taints nothing) (§4).
3. **Uniformity not established (live; the honest residue for R^4):** six nodes whose own sources say their K- or T-uniformity
   is open — the level-uniform N5 threshold (needs BFT), σ_fl at level k ≥ 1 (needs BFT), R_0 (Theorem UNIV's "k-uniform vector
   step gap OPEN"), CE-exp^k ((L-loc)_k "beyond BFT as stated"), (MOM_4)'s C_4 ("volume- and K-uniform", not stated by layer 1),
   and the counterterms δβ_k, c̄_0^{sea} (U5: torus-independence above the wrap levels unproven). Each taints g_0 (§4.3, §5).
4. **Volume (owner's update 2).** No live node's stated definition grows with T. The only fixed-volume-only constants found are
   off the live route and superseded: Corollary NL-4's ∝ T^{d+2} and GREENT's O(log T) for Theorem N1-15 — now replaced by
   TUNIF's T-uniform TU-6, CONFIRMED by REVIEW55_TUNIF and cross-family by CODEX_REVIEW_TUNIF2 — and N1-15's constant has no live
   consumer anyway (§5).
5. **DAG-F3:** six symbols left unplaced (θ_w as REVIEW_S22 writes it, m vs m_0, the η that C_fun multiplies, LINEAR_PACKAGE's
   M, Q_str, FLOW's ε_1); about thirty collisions resolved by definition site (§6).
6. **Quantifier order** (topological order of the live written hierarchy, §7): structural data → level-0 N5 chain, SF stage-0
   chain, SQ chain, BFT target constants, flow constants β_-, R → **ε_1** → its multiples (η_q, ε_loc, ε^J_loc), a_ret, (I_k^E)″,
   C_ρ, γ_0, γ, g_1, t_pr, (CLS-min), a_bad → node A's C_A, a_A, c_A → c_U := 1, c_+, c_f, B_0 → θ → a → C_fc, C_ℓ → n_H → n_♯ →
   W, C_H, ε_♯ → **g_0** → R(g) → K_0, T_1(R(g)).
7. **Side finding (exact, dag55_3): RLARGE's (TC) fails with RLARGE's own ε_loc** — by ×19.32 (N = 2, κ = 1), ×15.45 (N = 2,
   κ = ¼), ×22.99 (N = 3, κ = 1), ×18.38 (N = 3, κ = ¼). It is ε_1-free (both sides ∝ ε_1), so it is neither a cycle nor a
   growth, but as written the collar-bad family has no admissible (ε_loc, η_q) pair. Repair (mine, ARGUED): take the quietness
   threshold below η_q by that factor (§8.1). This settles RLARGE's U3 negatively as written.
8. **Dead ends confirmed by the graph:** a_RS, η_1 (REVIEW55_ARS F01), both c_RS, CURV1's C_θ/ε_θ (on the BFT route), and
   Theorem N1-15's constant have no edge into any live node. **The decade ledgers can be retired** in the sense PLAN_S26 §2d
   asks: every live constraint is an upper bound on a later choice, so magnitudes decide nothing; what decides is §3.1, §4 and
   §4.3.

---

## 2. The node census in one paragraph (full table: Appendix A, generated from `checks/dag55_2_graph.py`)

189 nodes: **164 live**, 16 off-route (CURV1's ℓ_θ/A_in/C_θ/ε_θ, the per-level route's C_♭^{(i)}, C_θ^{(i)}, ε_unif, K̄, a_RS,
η_1, c_RS = 81, N1-15, 𝔮₀, τ^♯, LOOP-const's column induction, PLD's x(S) allowance), 3 superseded (v1's a_♯/n_♯ formula, NL-4,
GREENT's 𝒮_T), 6 unplaced (DAG-F3). Groups on the live route, each node with its defining string in Appendix A:
**structural** (N, L, d, A_d, p_L, n_1, n_int, κ_±, κ, κ_0; the choices q, m and the decoupled BFT exponents θ_w^c, θ_w^r, θ_A,
θ, α); **FLOW** (β_0′, R_0, R, β_-, β_+, C_ρ, γ_0, γ, g_1); **PROOF N5/BR1** (r_*, S_*, C_Δ, the level-0 gap, m, α_*, γ′, S′_m,
R_*, T_0, ε_*, 𝔠_∞, r_♭, S_♭, C_♭, K_FP, ε_br, the class gap λ_min ≥ 3.1727·10⁻³, the level-uniform N5 threshold); **BFT**
(ε_0, r_ℂ, m_0, C_0, T_0, BFT-0/1/2, BFT-3, BFT-4, BFT-5 = (BFT-5_E) with ε_5, C_5; C_fun); **SF stage 0** (G_∞, the radius
chain, τ_c = τ^A, a_p/a_c, ε_bg^{(TH-bg)}, C_bg, ρ_band, N′, a_sh/R_sh/|Ω_B|, C_Ω, DX′'s a′, the four stage-0 ceilings and O0's
g_*); **SQ/EPSSTAR/CONST_T** (q, ε_*^{EPS-T}, m, A_cγ_c, F, C_T, C_0^{LOC-T}, θ_ε, θ_G, θ_0^{SQ4}, A_0, q^{RES}, C_r, B_0^{SQ}, C_D,
τ-sizes, τ_R, C_err, θ_0^{SUP}, θ_♯, τ_♭, η_♭, C_3, c_♭ = 1/640, C′ = 53, c_pr, t_pr); **RLARGE/HW/HIST/PLD** (ε_1, b_1, ε_loc,
δ_0, η_q, ε^J_loc, a_bad, a_cb, a_D, θ_cb, a_ret, σ_fl, C/p of (RLF-0), κ_d, κ_0^{CE} ≈ 151.3, a_A, C_A, c_A, θ, a, c_sf, C_fc, λ_*,
C_ℓ, C_ℓ′, c_U, c_+, c_f, c_LI, B_0, c_B, n_H, n^J_*, b_n, b_D, c_att, n_♯, W, ε_♯, C_H, g²_CRC, a′, 𝒱_K^{LF}, E_0, the hypothesis
nodes (I_k^E)″, Theorem A5, (a5-G♯), (SC)_k, (CLS-min), (REG-min), (LI^F), (MS-Sob), (NA-∅), (SF-last), (E2^𝔉′)); **the coupling
sequence** (kernel couplings, stage constants, δβ_k, effective couplings); **EXISTENCE** ((F, h, n, ε = ε_1, w), C_4, CE-exp^k,
the (CE-cond^ms) constants, (K), g_3, g_c, R(g), K_0/T_1); **the sink g_0** (RLF v3's "g_K ≤ g_0").

---

## 3. DAG-F1 in detail

### 3.1 The n_♯ loop (B-all SCC of 12 nodes: B_0, a, a_A, b_D, c_A, c_B, c_U, c_f, c_+, n_H, n_♯, θ) — CONDITIONAL cycle
The explicit cycle the checker prints (dag55_2_out.txt, "== B-all"):
- B_0 → c_B [def] RLARGE.md "38416B_0/log L"; c_B → n_H [def] "n_H := ⌊(4 + c_B)/(aβ_-)⌋"; n_H → n_♯ [le] "n_♯ ≥ max{n^J_*, n_H}";
- **n_♯ → c_A [implicit]** HW.md "R_{S,E} := ∩_j{every *-component of (D_j ∪ E^{(j)}) ∩ S^{(j)} has ≤ n_♯ cubes}" + "C_A, c_A
  independent of g, K, T, k and the law";
- c_A → B_0 [def] HW.md "a, C_ℓ, c (from the moments and (LI)) → B_0 := B_1 + c + 1" + "already gives (PRICE^ℛ) at one level with
  a = a_A,".
The same SCC also closes through a_A → a → n_H, a_A → θ → a, and c_+ → b_D → n_♯ ((T): "n_♯ ≥ max{n_H(a, B_0),
b_D/(aβ_-log L)}").
**Reading.** (SDP)^A must hold "for every μ ∈ ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}}" (HW §18.1); those laws are the chain conditioned on "no
unreturned defect", and "unreturned" means "n(𝒟) > n_♯" (RLARGE §2.3). So the hypothesis is indexed by n_♯. HW §13.2 and §30.6
fix the order "a, C_ℓ, c … → B_0 → n_H → n_♯ ≥ n_H → g_0(n_♯)" and "node A's C_fc, C_A, a_A, c_A → c_U := 1 → … → n_♯", i.e.
they **assume** node A's constants independent of n_♯. HW §18.1 lists the quantities they must be independent of as
"g, K, T, k and the law" — n_♯ is not named, and "the law" ranges over a family defined after n_♯. **Status: no cycle in the
written order; a cycle in the dependency structure unless (SDP)^A, (PRICE^ℛ), (M-f^A) and (LI^F) are proven with constants
uniform in the cutoff.** Why it matters: n_♯ ≳ 2·10⁸⁷ (RLARGE §5.4 [hand]), so any n_♯-dependence of the type 6400^{n_♯}
in a node-A constant would be fatal; a per-cube gas bound (activity C^{|Y|}e^{-a|Y|/g²} summed over all cluster sizes) is
naturally cutoff-uniform, so I expect the requirement to be dischargeable [inference], but it is a fourth quantifier node A
must state. **This is the one place where the hierarchy's acyclicity rests on an unstated uniformity.**

### 3.2 The FI-1 loop (B-all SCC: kernel couplings, stage constants, δβ_k, effective couplings) — a fixed point, not a constants cycle
- kernel couplings → stage constants [def] RLARGE "stage-k constants also use the kernel coupling g_{k+1} of K_{k+1} through CL^J";
- stage constants → δβ_k [def] "Derived at level k from data on levels [0, k] only" + "itself an output of stage k (through δβ_k)";
- δβ_k → effective couplings [def] "But F-flow at n = k + 1 consumes (RLF-δ)_j for j ≤ k (u_{k+1} contains δβ_k)";
- **effective → kernel couplings [fixedpoint]** "The fixed point is consistent only if the kernel coupling sequence is fixed first".
RLARGE §4.4 Option A ("Stage k's constants are functions of the parameters (g_k, g_{k+1}) of W and are bounded using only the
a-priori bracket 1/g_{k+1}² ≤ 1/g_k² + R and g_{k+1}² ≤ 1/(2R)") makes the constants depend on R only: in the graph the edge
kernel couplings → stage constants is marked absorbing on that string, and R → stage constants is an `le` edge. The remaining
loop is the statement A5 ("the chain's own sequence" = the kernel sequence), a fixed-point condition on the couplings that
FLOW's F-tune solves by continuity given the per-level inputs. **Not a DAG-F1 for constants; recorded because RLARGE itself
says "Neither option is a theorem here" (U4).**

### 3.3 Loops the source breaks by an explicit order statement (not counted as cycles; pre-stated rule)
1. **B_0 ↔ ε_♯.** RLARGE's "B_0 = c_LI + c_f + 164ε_♯" with ε_♯ := 6400^{n_♯}(…)^{n_♯+1} and n_♯ ≥ n_H(B_0) would close
   B_0 → n_H → n_♯ → ε_♯ → B_0. HW §13.2 breaks it: "→ B_0 := B_1 + c + 1 (B = 164ε_♯ ≤ 1 once g_K is small) → n_H → n_♯ ≥ n_H →
   g_0(n_♯) with ε_♯ ≤ min{½, 1/164}". Encoded as c_f, c_LI, c_A → B_0 and ε_♯ → g_0; no ε_♯ → B_0 edge.
2. **θ, C_ℓ ↔ g_K.** CAP-1 "max{6θ, 24θ}(1 + 2Rg_K²) < 1" and "λ_* = 6θ(1 + 2Rg_K²)" contain g_K. Broken by Theorem HW^cap's
   hypothesis "(H-w′) ⇐ (F_R) [g_K² ≤ 1/(2R)]" and RLARGE §5.4's "log C_ℓ ≈ (3n_int/2)·log(1/(1 - λ_*)) ≤ 324·log(4/3) ≈ 93
   at λ_* ≤ ¼". Encoded as θ, R → λ_* and θ, R → g_0; no g_0 → λ_* edge.
3. **c_U ↔ g_K.** "c_U := 2ε_2 ≤ 1" with ε_2 → 0 as g_K → 0 and b_n ∝ c_+ = c_A + c_U. HW §30.6: "c_U := 1 (any value in
   (0, 1]) → b_n, b_D, c_att, C_ℓ → …" fixes the input value first.
4. **FLOW's γ and β_±.** "β_± := β_0′ ± C_ργ²/log L" uses γ, and γ uses C_ρ = C_ρ(β_-, R). FLOW Lemma F-ind: "Fix FIRST
   β_- := β_0'/2 and R := 2R_0 …; then the layer-1 constants C_ρ = C_ρ(β_0'/2, 2R_0) are fixed; then γ := min{γ_0, …}".
5. **Stage-0 thresholds.** SF O0: "choose ζ (s5 F2), then s_0 = ζ/X_∞ and τ_c = s_0/(√NC_0), then ε_1 ≤ τ_c and RLARGE's stage-0
   thresholds ≤ τ_c (TH-ch), then ε_bg from BR1 (iii)".
6. **Existence lane.** "(F, h, n, ε, w) first; then the constants of (CE-cond^ms), (MOM_4), (LF-loc)^ε; (K) is checked once …;
   then g ≤ min{g_c, g_3} …; then R(g); then K_0, T_1(R). n does not depend on g."
**Things I looked for and did not find a cycle in:** ε_1 vs the SQ chain (η_♭, t_pr, C_D, C_T and ε_*^{EPS-T} depend only on
q, m, N, L, κ_±, C′, c_♭ — EPS-T: "ε_* = ε_*(N, q) > 0 and C_T = C_T(N, q)"); ε_1 vs the N5 chain (ε_*, 𝔠_∞, C_♭, ε_br depend on
(N, L, κ_±) and analyticity constants only); θ vs a_A ("If a_A < θa_bad, θ is lowered to a_A/a_bad and nothing else changes":
a_A does not depend on θ); BFT's ε_0 vs ε_1 (BFT's constants are "depending only on (N, L, κ_±)"); (TC)'s ε_loc vs η_q (both
∝ ε_1: an inequality between two fixed multiples, §8.1, not a loop).

---

## 4. DAG-F2 in detail

### 4.1 The one live K-growth that reaches the sink: C_fun (COF-crit's level count)
- **Seed evidence:** REVIEW_BFT_B_S9_S10 "9.31·e·(k−1) ≈ 25(k−1)" and "PROVEN as an implication with a constant that grows like k";
  REVIEW55_BFTB Finding 6: "Not k-uniform; the k-uniform form needs a level-decay input for the rows (lane A's (SPD)/(W2))."
- **Edges that carry it (each with its string, Appendix B):** L, κ_± → C_fun ("§35.6 substitutes the **per-level** row bound
  π_l(V_l) ≤ 2C_NCC_bchκ_+L²η²"); C_fun → BFT-5 [req] BFT_B §32.1 "it is CONDITIONAL on (CO-fun) for the curvature half";
  BFT-5 → (a5-G♯) [req] REVIEW_S22 "SF: BFT-1 (θ_w > 0), 2 (complex ball for (R♯)) and 5, giving (a5-G♯), (a5-U) and (MIN-reg).";
  (a5-G♯) → A5 → (I_k^E)″ [req] RLARGE row 4 "Theorem A5 [ARGUED] ⇐ (a5-G♯) + (R♯) … + (MS-Sob)"; (I_k^E)″ → C_A [req] RLARGE §7
  "(SDP)^A ⇐ (I_{k-1}^E)''(d'') + (CLS-min) + …"; C_A → g_0 [le] HW (S1) "holds once a_A/g_K² ≥ a/g_K² exceeds log(2Δ_ρ²C_A) +
  a_AR + c_+c_att". The checker's shortest witness (dag55_2_out.txt, "SINK g0: TAINTED via"): **C_fun → BFT5 → a5G → A5 → IkE
  → C_A → g0**. 43 live nodes are tainted, including FLOW's γ and g_1 (via (I_k^E)″ → C_ρ: FLOW "where C_ρ is explicit in the
  polymer norms of the step output") and the existence lane's g_3, g_c, C_4.
- **What it means.** If BFT-5 (b) is reached by the lane-B route as the reviewed record states it, the BFT-5 constant grows
  linearly in k, every node-A constant built on (I_k^E)″ inherits it, and the ceiling g_0 would have to shrink with K: a genuine
  DAG-F2 at the sink.
- **Step 4's report (KFACTOR_O55, not yet cross-checked; I read §1-§3, §6, §10).** "The ≈ 25(k−1) is real in the source's bounds
  and absent from the object": at critical points the rows decay like L^{-(k-1-l)} (its Lemma TR, "PROVEN here, as an implication
  of reviewed source lemmas"), so the curvature sup half is k- and T-uniform; in the contraction the factor is "a norm artifact,
  removed by the transport-weighted pair θ_w^r = 3" (ARGUED). Its classification: "KF-F2 in form, not a genuine non-uniformity".
  It also corrects the figure: the sharper route's pre-repair constant is (121/13)(k − 1) ≈ 9.31(k − 1), and the "≈ 25(k−1)"
  optimum θ* = 1/((k−1)ln L) lies below α = ¼ for k ≥ 5. **I did not re-derive Lemma TR.** Consequence for the DAG, stated as a
  conditional: if Lemma TR passes its cross-family review, the C_fun seed is removed and **the live route has no K- or T-growth
  seed left** except 𝒱_K^{LF} (4.2). One interaction to watch [inference]: KFACTOR_O55 §5's contraction repair uses θ_w^r = 3,
  while (C2) caps θ_w^r ≤ 2 + θ < 3 when residual-type sources sit in the source slot (REVIEW55_TUNIF W4/W5; my edge
  θ → θ_w^r); its §5(c) introduces a separate (G♯) weight 1 < θ_G ≤ 2 − α, which would lift that cap — a further decoupling of the
  exponents that the BFT statement would have to carry.
- **Multiplier (DAG-F3, U_eta_COF).** Whether the η in "(k − 1)η²" is BFT's fixed curvature size (≤ ε_0: KF-F2) or a g_k-scale
  quantity (KF-F3) is not decidable from the strings I read; KFACTOR_O55 §2 argues "A fixed-size quantity … η ≤ C_0||B_k||_D ≤ C_0ε_0".

### 4.2 The by-design growth: 𝒱_K^{LF}
Seed evidence: RLARGE "the only K-divergent quantity (HIST (P3))"; HW "𝒱_K^{LF}/|T| is not O(e^{-a'/g_K²})". Its only outgoing
edge enters (NA-∅) and is absorbing on the string "|log Z(∅) - 𝒱_K^{LF} - log Z_K^{sf}| ≤ C|T|e^{-a′/g_K²} uniformly in K": the
divergence is subtracted, not bounded. The checker shows it taints nothing (NA_empty is not in the tainted list).

### 4.3 Uniformity not established (weak seeds on the live route) — each one taints g_0
| seed | evidence (file: string) | first witness to g_0 |
|---|---|---|
| level-uniform N5 threshold | RLARGE.md: "constants are not covered by CI-bg; the level-uniform form is GAP along the per-level route" | → ε_1 → a_bad → … → g_0 |
| σ_fl (level k ≥ 1) | PLD.md: "Levels k ≥ 1 need σ_fl at level k (N5 level-uniformity, BFT)." | → a_ret → θ, γ_0 → … → g_0 |
| R_0 (UNIV-1L) | RLARGE.md: "k-uniform vector step gap OPEN [s]" | → R → g_0 (the printed witness) |
| CE-exp^k | EXISTENCE.md: "(L-loc)_k OPEN, inside the B-NA wall … BFT-3 states orders ≤ 4 only …" | → (CE-cond^ms) → g_3 → g_0 |
| C_4 of (MOM_4) | EXISTENCE.md: "E‖1 − U_k(p)‖⁴ ≤ C_4g_k⁴, volume- and K-uniform (⇐ Theorem CB + a prefactor-free (RLF-3^dis) at" | → (K) → g_3 → g_0 |
| δβ_k, c̄_0^{sea} | RLARGE.md: "no source proves that the sea average is torus-independent above the wrap levels (U5)" | → effective couplings → (absorbed at the stage constants by Option A); → 𝒱_K^{LF} |
These are not growth; they are places where a source states that the needed uniformity is not yet proven. All of them sit
behind BFT, node A or the flow's universality theorem.

### 4.4 Off-route growth (recorded so the record is complete; none has an edge into a live node)
C_♭^{(i)} ("absolute-value recursion compounds by Z_colZ_row² ≈ 1.3·10³ per level", CURV-F2); C_θ^{(i)} ("grows geometrically",
CURV-F2′); ε_unif ("ε_unif = O(1/k)", CURV-F2″); LOOP-const's column induction ("×81 per level"); PLD's x(S) allowance
(REVIEW55_HWPLD F9: "compounds geometrically"); NL-4 (∝ T^{d+2}, fixed coarse side); GREENT's 𝒮_T (O(log T)); K̄ of (H-K)
(measured values "grow with T"). The checker confirms no off/superseded node has a live successor.

### 4.5 A level-count factor the source absorbs by the running (for Step 4's taxonomy)
REL-seq's step price contains "e^{c(38417(n_♯+1) + 38416(K-1-j))}" and HW §13.2 says "The depth term e^{38416c(K-1-j)} of the
shadow allowance is beaten by the running exactly by HIST-sum's arithmetic (S2-F2)", with RLARGE §5.2: "The logarithmic flow
is load-bearing (β_- = 0 diverges for every n; HIST §7.4)". This is the live route's one asymptotic-freedom absorption; it is
internal to the definition of ε_♯ and n_H, so it is not a node, and it is the reason β_- appears in n_H.

---

## 5. Volume (the owner's update 2: what is uniform only at fixed volume)

**(a) Fixed-volume-only constants found — all off the live route and superseded.**
- **Theorem N1-15 via NLOC Corollary NL-4**: "with a constant that grows like T^{d+2}" (NLOC). The T there is the level-k coarse
  side; on a fixed physical torus T_k = T·L^{K−1−k} (RLARGE §0) is unbounded in K, so "uniform at fixed T" would also have been a
  K-growth (`Tk`). **Superseded** by TUNIF TU-6, which is uniform in k and T at its scope — REVIEW55_TUNIF U6 "CONFIRMED (conditional
  on (N-Q))" and CODEX_REVIEW_TUNIF2 "(T-UNIF), with the stated repairs, is CONFIRMED as a conditional theorem" (cross-family;
  both conditional on (N-Q) = NQ-1, which REVIEW55_NORMS E1 CONFIRMED). NLOC's Theorem NL-3′ remains REFUTED as proven
  (REVIEW55_TUNIF N7; CODEX_REVIEW_TUNIF2 §6 "the inequality itself is **REFUTED**"). And N1-15's constant has **no live
  consumer** (NQ_DEF §D5.4, CONFIRMED by REVIEW55_NORMS F8): (H-C)'s C_♭ is a different, class-wide object ((N-bg) OPEN).
- **GREENT's 𝒮_T**: "unconditional at **fixed** T and **not** uniform in T" (O(log T)); superseded by TU-4/TU-5.
- **(H-K)'s K̄** (per-level route, off): "The exact-input LP values grow with T (row 252: 0.062 at T = 4, 0.090 at T = 6;" —
  bounded toward the smooth value ≈ 1/9, measured, not certified.

**(b) Live nodes whose T-uniformity is required but not established** (§4.3): δβ_k and c̄_0^{sea} (U5 / K9: "infinite-volume
numbers" asserted; torus-independence above the wrap levels unproven; this decides one coupling shift vs two on anisotropic
tori); C_4 of (MOM_4) (existence: "volume- and K-uniform", "Not stated by layer 1"); and everything resting on BFT (BFT's T-uniformity
"every torus whose level-k side is ≥ T_0" is part of the OPEN target) or on node A's hypotheses, which assert T-independence
((SDP)^A: "C_A, c_A independent of g, K, T, k and the law"; (I_k^E)″: "all constants … independent of g, k, K, T and 𝔥"; c_sf of
(SF-cap)^A: uniform "under conditioning", K/T unstated).

**(c) Volume LOWER bounds only (harmless for R^4; listed because each is a quantifier the R^4 limit must respect):**
N5-sf0's T_0 := 4R_* + 6 (= 1.2932·10⁷ on the session-23 class) — N5-sf0 holds "uniformly in k … and T ≥ T_0"; BR1 "Let T ≥ T_0";
CURV1 "T ≥ ℓ_θ + 1" (off); BFT's T_0; DX′'s R_sh-neighbourhood (|Ω_B| ≤ 4(2R_sh + L)⁴ with R_sh ≈ 1.6·10¹² fine spacings — the
stage-0 torus must exceed it); the existence lane's "every hypercubic torus of side T ≥ T_1(R)" with R(g) ≍ log(1/g), so T_1
grows as g → 0 (the diagonal limit must keep T ≥ T_1(R(g))).

**(d) Stated T-uniform on the live route (each conditional on its own hypotheses):** the level-0 gap ("λ_min(Õ_0) ≥ 4.229507·10⁻³
… on every torus, compressions included"), 𝔠_∞^♯ and λ_min ≥ 3.1727·10⁻³ ("on tori T ≥ T_0"), ε_*, ε_br; SF's radius chain and
τ_c ("g-independent and volume-independent"); FLOW's γ, g_1, β_±, R ("do not depend on K or on the torus", resting on (SF-∞)'s
infinite-volume β and on Theorem UNIV, whose k-uniform vector step is OPEN); HW/HIST-sum ("uniformly in K and T", conditional);
RLF v3's constants ("independent of g, K, T and the history", OPEN target).

**(e) Extensive by design (correct for R^4):** 𝒱_K^{LF} and HIST-sum's C_H|T|e^{-(n_♯+1)a/g_K²}: per-unit-volume bounds with
T-independent constants.

**Net for R^4.** The written hierarchy contains no constant that grows with the volume. What R^4 needs beyond the torus is
exactly (b): BFT and node A proven with the T-uniformity they assert, U5, and (MOM_4). Nothing in the graph forces a volume
cutoff into g_0.

---

## 6. DAG-F3 — symbols

### 6.1 Unplaced (no edges; listed as nodes with live = unplaced)
| symbol | candidates | why not placed |
|---|---|---|
| θ_w as REVIEW_S22 writes it ("level-j curvature and soft-fluctuation components are weighted by L^{θ_w(k-j)}") | θ_w^c, θ_w^r, the source weight θ, θ_A | one glyph doing ≥ 3 jobs; the decoupling is CONFIRMED faithful (REVIEW55_TUNIF W2), so the DAG places the decoupled exponents and leaves the single θ_w unplaced |
| m (𝔐's weight "e^{±m d}") vs m_0 (BFT-3, BFT-4) | one constant or three | THETAW J5 / REVIEW55_TUNIF W13: "flagged, not decided" |
| η in C_fun's O((k − 1)η²) | BFT's fixed curvature size (KF-F2) or a g_k-scale size (KF-F3) | decides Step 4's classification; KFACTOR_O55 §2 argues fixed-size |
| M (LINEAR_PACKAGE 4.2′: "bounded there by M = M(L, κ_±)") | also M̄_c, Lemma PM's matrix M, Theorem CE's M-units | its consumers ((GAP-Z), TU-4, lane A's W0/GU/LIN0) are inside BFT's proof route, not modelled |
| Q_str | NORMS's 81-entry operator vs LINEAR_PACKAGE's 135-entry operator (REVIEW55_NORMS F4) | consumed only off-route (N1-15) |
| ε_1 at FLOW l.1927 ("On a disc |φ| ≤ ε_1 (fixed)") and l.2834 | one or two objects (REVIEW55_CONST K9: count ≥ 5, possibly 6) | neither is RLARGE's χ_Q cut; FLOW's uses not traced |

### 6.2 Collisions resolved by definition site (each placed as a separate node, or noted as off-route)
- **ε_1** (≥ 6, SYMBOLS §5.1): RLARGE's χ_Q cut placed (node eps1); BFT_B's ε_1^{N2} (O(1) formula), FLOW's two, EXISTENCE's
  exponent index, HW's ε_1^{gas}: not on the live constants route.
- **ε_*** (4, EPSSTAR §6.1): N5-sf0's (eps_star_N5) and EPS-T's (eps_star_EPST) placed; BG-b's (ε_1²/(4NB))^{1/2} and BFT_B's local
  max_tε_f not on route.
- **θ_0** (4, SYMBOLS §4.1): θ_0^{SUP} = 1/(2C_err) and θ_0^{SQ4} = min{θ_G, θ_ε} placed (both enter τ_♭); PLD's tilt θ_0 and
  PROOF's θ^{(0)}_loc (a CURV-F2″ bound variable) not on route.
- **C_1** (≥ 13, SYMBOLS §6.1): SUP-price's C_1 = 160 enters as c_♭ = 1/(4C_1) = 1/640; CONST_T's (★) prefactor is inside C_T's Ĉ;
  Theorem CE's C_1 = 2κ_0B is behind κ_0^{CE}; the rest not on route.
- **c_1** (≥ 11): N5-coer's c_1 appears only inside γ_0's formula, superseded by CI-0's certified gap; KN's c_1 = 1/117 off route.
- **κ** (≥ 5): RLARGE's kernel κ; κ_±; κ_0 (level-0 soft coupling, evaluated at 1); **κ_0 ≈ 151.3 (Theorem CE's decay constant —
  the same glyph)**; κ_d; κ_p; κ_s; κ(η,η′) — all placed by site or not on route.
- **c_RS** (625 frozen v1 / 81 RS-joint): both off route (REVIEW55_ARS F01, F12).
- **n_♯**: v3's cutoff (placed); v1's ⌊4/(a_♯β_-)⌋ ("superseded", RLARGE l.832); SF's "HIST n_♯" table rows (off).
- **q**: EPS-T's Moser exponent (q_M) and RES-dec's decay ratio "q := L⁻³ + C_qτ" (q_RES) placed separately.
- **θ**: CAP-1's θ; BFT's source weight θ; CURV1's θ; NAH-unif's "θ := (1 - K̄)/2"; SQ's curvature size θ — placed by site.
- **α**: BFT's α; N5's α_*; HIST's α_E; CURV1's α := 3ℓ_θε_V (bound variable); REVIEW55_CONST's allocation α — placed by site.
- **C_♭**: PROOF's C_♭ := 4S_♭n_1/r_♭ (placed); (H-C)'s class-wide C_♭^{(i)} (off, per-level); HIST Lemma 7.2-0^J's "C_♭ := L² + 1 +
  (12 + 3L)A_d" (not on the constants route); c_♭ = 1/640 (lower case, placed); NORMS's N1-15 bounds none of the consumed ones.
- **B_0**: RLARGE's history constant and SQ's STOKES-it "B_0 := 4.1C_r/(1 - qL²)" — separate nodes; HIST's representation-side
  B_0 (≥ E_0, inside (I_k^E)″'s list) is a third object.
- **C_0**: BFT's C_0; SQ's LOC-T C_0; SF's MSG_0 constant inside τ_c := s_0/(√NC_0).
- **a**: RLARGE's a = min{θa_bad, a_A}; N5-sf0's a := m − m_1; CONST_T's Moser a = q/(q−4).
- **a′**: RLARGE's (RLF-4) exponent; SF DX′'s a′ = a_sh²/(8N||C||m_sh).
- **g_0** (REVIEW55_HWPLD F1): the stage-0 coupling (u_0 = 1/g_0², SF's ceilings); RLF v3's threshold on g_K (the sink); FLOW's bare
  coupling g_0(ε, g). The stage-0 ceilings reach the sink through (F-3)'s upper bracket at K = 1 (REVIEW55_HWPLD F1's argument).
- **g_1**: FLOW's ceiling (γ^{-2} + R)^{-1/2} on the final coupling vs the level-1 coupling.
- **γ_0**: FLOW/(RLF-δ)'s coupling domain vs N5-sf0's gap γ_0 := c_1min(1/2, κ_-/2)/L².
- **r_***: N5-an's analyticity radius vs SF's radius-chain r_* = 5.16·10⁻³¹. **n_1**: PROOF's 4(3L)⁴ vs SF's DX-rel hole count.
- **C_ℓ**: HW [RHW5-fix SYM-1] "Two values, one symbol" — unprimed (ε_2, (S2)) and primed (REL-boot's r) placed separately.
- **c_f**: three HW definitions; §35.7's C_sh·81·c_+ placed. **c_U**: HW's (CRC) constant vs PLD's (LI^U) ratio.
- **C_θ**: CURV1's second-order constant vs FLOW's heat-trace constant "|θ_α(t)| ≤ C_θq_α²".

---

## 7. The quantifier order (= the topological order of the live written hierarchy)

From `checks/dag55_2_out.txt`, "== D. order (live subgraph, B-strict edges)": 164 positions, validity re-check PASS (every
edge goes forward). Ties are broken by (tier, id), so the order within a stage is not forced; the order between stages is.
**Stage 0 — data and free choices:** N, L, d, A_d, p_L, n_1, n_int, κ_±, κ, κ_0; q, m; θ_w^c = 2, θ_A = 1, θ ∈ (0,1), α ∈ (0, θ),
θ_w^r ∈ (2, 2 + θ).
**Stage 1 — analytic constants that need no threshold:** the SQ/EPSSTAR chain (A_cγ_c, F, C_T, A_0, …); G_∞; K_FP; FLOW's R_0, R,
β_0′, β_-; the N5-sf0 chain (gap → m → C_Δ, α_* → S′_m, γ′ → R_* → T_0 → ε_* → 𝔠_∞ → C_bg; r_♭ → C_♭ → ε_br); the class gap;
BFT's target constants (ε_0, r_ℂ, m_0, C_0, T_0) and C_fun → BFT-0/1/2, BFT-3, BFT-4, BFT-5 → (a5-G♯) → A5 → σ_fl → the
level-uniform N5 threshold.
**Stage 2 — stage-0 SF thresholds and the SQ thresholds:** τ_c → a_p/a_c, ρ_band → a_sh → a′_{DX} → ε_bg; DX′, hole, band, FS-1 →
O0's g_*; τ-sizes → q^{RES} → B_0^{SQ} → C_D → C_err → θ_0^{SUP}; θ_G, θ_ε → θ_0^{SQ4} → τ_R → (REG-min); θ_♯ → τ_♭ → η_♭.
**Stage 3 — ε_1**, below every one of: τ_c, τ_c/(2C_bg), ε_bg^{(TH-bg)}/C_bg ((TH-ch′)); ε_br/(1.011√N) ((TH-ch″)); the N5 threshold
at every level (needs BFT); 2sin(π/N); √(η_♭/(4C_3)) (DESC-ε (iii), if that route is used).
**Stage 4 — ε_1's dependents:** existence's (F, h, n, ε, w); (I_k^E)″ (α_E ≥ cε_1); C_ρ; ε^J_loc, η_q, ε_loc; a_ret; γ_0 → γ → β_+, g_1;
t_pr → (CLS-min) → a_bad → a_cb → a_D.
**Stage 5 — node A's constants and HW's:** c_A → c_U := 1 → c_+ → b_D, b_n, c_f → B_0 → c_B; the stage constants → C_A, a_A → θ
→ a → c_sf → C_fc → λ_* → C_ℓ → C_ℓ′; (RLF-3^dis) → C_4 → (K); g²_CRC; g_3, g_c.
**Stage 6 — the cutoff:** n_H → n_♯ → C_H, W → (SF-last); δβ_k → 𝒱_K^{LF} → (NA-∅) → a′; ε_♯.
**Stage 7 — g_0**, below every one of: FLOW's g_1; O0's g_* through (F-3) at K = 1; (2R)^{-1/2}; CAP-1's ceiling given θ; HIST-sum's
"6400C_ℓe^{aR}e^{38417B_0}e^{-a/g_K²} ≤ ½"; "ε_♯ ≤ min{½, 1/164}"; g²_CRC ((S2)); (S1); REL-boot's r ≤ ½ (with C_ℓ′); (P5)'s
"g_K² < a/(8(3κ_0 + 3)) and C_ℓe^{-a/(4g_K²)} ≤ c(κ_0)" and Theorem CE's κ_d condition; CL^J's "g_k, g_{k+1} ≤ min{1, √κ}/√2";
the existence lane's min{g_c, g_3}.
**Stage 8 — after g:** R(g) → K_0, T_1(R(g)).
This is PLAN_S26 §2d's "(N, L, κ_±) → analytic/geometric constants → thresholds (ε_1, ε_0, r_ℂ, …) → g_0", with two refinements
the graph forces: BFT's ε_0, r_ℂ come **before** ε_1 (ε_1 must sit inside the N5/BFT domain), and node A's constants come
**after** ε_1 (they are statements on the ε_1-domain) but before n_♯ (§3.1's unstated uniformity).

---

## 8. Side findings (each labelled with its support)

### 8.1 (TC) fails with RLARGE's own ε_loc — U3 settled negatively as written (EXACT, check dag55_3)
HW Lemma W-cb's hypothesis is "(TC) ε_loc/2 ≥ (16N + 3)A_dη_q" and HW leaves "whether RLARGE's ε_loc obeys (TC)" to "the owner
of the thresholds"; RLARGE §0 gives the [hand] sufficient condition ε_loc ≥ (16N + 3)ε_1/(128N) and calls compatibility
"not checked: unresolved item U3". RLARGE's ε_loc is frozen Proposition CL's "ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}}" with
"b_1 := n_P + 12κ(1 + A_d(L))²", and η_q is RS-lin's "η_q := min{ ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d }". On the live branch both
are fixed multiples of ε_1, so R := (16N + 3)A_dη_q/(ε_loc/2) = (16N + 3)√(Nb_1)/(64N) is a pure number. dag55_3 (criteria first;
integer square-root enclosures, Fractions; branch gates B1, B2 PASS at every point; control C1 reproduces R = 1 exactly at
RLARGE's hand value; control C2 gives R = 35/64, 17/32 ≤ 1 at ε_loc := ε_1/4, so the verdict logic can output HOLDS):
| N | κ | b_1 | R (enclosure, display) | (TC) |
|---|---|---|---|---|
| 2 | 1 | 2496 | [19.3195…, 19.3195…] | **FAILS** |
| 2 | 1/4 | 1596 | 15.4486… | **FAILS** |
| 3 | 1 | 2496 | 22.9854… | **FAILS** |
| 3 | 1/4 | 1596 | 18.3800… | **FAILS** |
**Reading.** Not a cycle and not a growth: an ε_1-free incompatibility between two thresholds that the text defines as
multiples of ε_1. As written, the collar-bad / non-quiet family (RLARGE row 10f) has no admissible pair. **Repair (mine,
ARGUED):** W-cb's proof uses η_q only as the quietness threshold ("If both endpoint blocks of c are quiet (< η_q), δ :=
||M̄_c − S_c|| ≤ A_dη_q ≤ δ_0"); with a quietness threshold η ≤ η_q/R the same algebra gives (TC), and RS-lin's hypotheses only
strengthen. Costs: more cubes are non-quiet (collar-bad), and the third entry of a_cb, c_pr·min{η², t_pr²}, drops by R² (≈ 373
at N = 2, κ = 1) — a constant, priced once, upstream of a_D and θa_D. Not checked: whether CL^J's other uses of η_q tolerate the
change. **This is the one infeasible window I found; it belongs on RLARGE's U3 line, not on a decade ledger.**

### 8.2 (MOM_4)'s demanded input is outside RLF v3's architecture [inference, mine; not encoded]
EXISTENCE asks for "(RLF-3^dis) at g-scaled thresholds with a prefactor-free tail (C_de^{-a_dt²/g²})^{N}", t ∈ [g_{j'}, ε]. In
RLF v3 the per-defect exponent is a = θc_pr·min{ε², t_pr²} at the cut ε, the cutoff is n_♯ ≥ n_H := ⌊(4 + c_B)/(aβ_-)⌋, and g_0 is
fixed after n_♯ (HW §13.2). Re-running RLF v3 at a cut t ≍ g would give a ∝ g², n_♯ ∝ g^{-2} and an ε_♯ that is not small
(a/g² = θc_pr ≪ 1): a g ↔ n_♯ loop. So (MOM_4) needs a different mechanism (Balaban-type fixed thresholds with separate
fluctuation bounds, or a moment bound proved directly), not a reparametrisation of RLF. BALABAN_EXTRACT §3/§M7 (Step 1)
reports that Balaban's own thresholds are fixed ("ε_0 is a **fixed** small constant, not tied to g_k"), consistent with the DAG's
fixed-threshold shape. This is an observation about a hypothesis (HYPOTHESIS-NEW in EXISTENCE), not a DAG-F1.

### 8.3 What the graph says about the decade ledgers
Every live inequality into ε_1, n_♯ and g_0 is a one-sided bound on a later choice (ε_1 above, n_♯ below, g_0 above, T below).
Lowering ε_1 (option C), raising n_♯ or lowering g_0 never feeds back into an earlier node: the B-strict order shows ε_1 at
position 107 of 164 with nothing upstream of it depending on it. So the decade counts — DX′'s 2.5·10⁻¹⁵²/C_Ω, the "+63.6"
margins, a_RS's "−15.6", the q-lever's 24 decades, TAUFLAT's 9.7 decades — are statements about how small g_0 ends up, which
PLAN_S26 §2d rightly calls irrelevant to truth. The one exception is (TC) (§8.1), an ε_1-free window. The graph supports
retiring the ledgers in favour of: §3.1's n_♯-uniformity requirement, §4's growth list, §4.3's uniformity list and §8.1.

### 8.4 Live constants with no live consumer (dead ends), confirmed by the graph
a_RS and η_1 (REVIEW55_ARS F01 — the graph has no edge from them into a live node); c_RS in both readings; CURV1's C_θ, ε_θ, ℓ_θ
(consumed only by the per-level route and SF's level-j reading of it); Theorem N1-15's 𝔚 + 13.5𝔖 (NQ_DEF §D5.4); 𝔮₀ (only
inside N1-15's prefactor). Live outputs with no successor (correctly): C_H, a′, β_+, 𝒱_K^{LF} (through an absorbing edge), and
the volume lower bounds T_0, K_0, T_1.

---

## 9. Reviews and Codex files used, and whether I agree
- **REVIEW55_ARS** (F01 a_RS unconsumed; F03 (RLF-δ) uses a_ret; F05 K9 a_ret is the only door for an a_RS-type quartic;
  F26 RS-lin live): **agree**; the graph reproduces F01 structurally (§8.4) and carries a_ret as U1-open with PLD's candidate
  formula flagged as not adopted by RLARGE.
- **REVIEW55_CONST** (K26: F = 175.8 inadmissible; K1/K2 constants valid for q ≥ 8; K7 TAUFLAT confirmed; the q-lever is
  allocation-independent): **agree**; none of it changes the DAG's structure (C_T ← F, A_cγ_c, q is unchanged; only magnitudes
  move). Read complete at 23:44Z.
- **REVIEW55_NORMS** (E1 NQ-1 CONFIRMED; F6 N1-15's T-uniformity rests on TUNIF; F8 no N1-15 factor reaches a threshold; C2 Z_col
  vs 𝔎_col): **agree**; used for N1-15's off-route status.
- **REVIEW55_TUNIF** (U6 (T-UNIF) CONFIRMED with repairs; N7 NL-3′ refuted; W2 decoupling faithful; W3 witness; W9 (W2) off
  lane A's path): **agree**, and CODEX_REVIEW_TUNIF2 (complete, 23:09:35Z) independently CONFIRMS (T-UNIF) and the N7 objection —
  **agree with Codex** on its decision table, including its NOT-VERIFIED on whether NL-3′'s existential conclusion is false.
- **REVIEW55_LEAD** (H7: λ_min conflict settled by [SF7-edit]; F3: the ×3.59·10⁵⁶ slack is "at c_+ = 1, C_Ω = 1"; H11: +63.619 is
  a conditional benchmark): **agree**; the graph uses the certified class value 3.1727·10⁻³ and carries C_Ω, c_+ symbolically.
- **REVIEW55_HWPLD** (F1 the g_0 collision and why the comparison is valid; F4 the ring is free, c_+ = c_A + c_U; F6 universal F_<
  false; F9 x(S) allowance compounds): **agree**; F1 supplies the edge from the stage-0 ceilings to the sink, F6 is the status of
  node (E2^𝔉′), F9 is the off-route node PLD_xS.
- **REVIEW55_BFTB** (Finding 6: COF-crit and NCE (i) REFUTED as stated; O((k−1)η²) at critical points): **agree** as the reviewed
  record, which is what the C_fun seed encodes; KFACTOR_O55 (Step 4) disputes the conclusion at critical points — not yet
  cross-checked, so the seed stays, flagged (§4.1).
- **KFACTOR_O55** (Step 4 worker file, Opus 5.5, uncross-checked): used only to state the conditional in §4.1; I did not
  re-derive Lemma TR.

---

## 10. Summary table — every finding of this file, with its support

| # | finding | support | status |
|---|---|---|---|
| 1 | Written hierarchy (358 def/le/order/req edges) is acyclic | dag55_2 B-strict: 0 SCCs; C1, C5 controls fire | PROVEN for the encoded graph (check) |
| 2 | n_♯ loop through (SDP)^A's n_♯-indexed laws; acyclicity needs n_♯-uniform node-A constants (unstated) | dag55_2 B-all SCC of 12; HW §13.1, §13.2, §18.1 strings | DAG-F1 CONDITIONAL (structural reading mine) |
| 3 | FI-1 fixed point (coupling sequence), removed from the constants by Option A (U4) | dag55_2 B-all SCC of 4; RLARGE §4.4 strings | fixed point, not a constants cycle |
| 4 | Six loops broken by explicit order statements | strings in §3.3 | read in situ |
| 5 | One live K-growth (C_fun) reaches g_0 via BFT-5 (b) → (a5-G♯) → A5 → (I_k^E)″ → C_A | dag55_2 witness; S10-6, REVIEW55_BFTB F6 | DAG-F2 FOUND on the reviewed record; Step 4 claims removal (uncross-checked) |
| 6 | 𝒱_K^{LF}'s K and |T| growth is absorbed by (NA-∅) | dag55_2 (NA_empty untainted); C6 absorb control | PROVEN for the encoded graph |
| 7 | Six weak seeds (uniformity not established) on the live route, each tainting g_0 | dag55_2 weak propagation | as stated by the sources |
| 8 | No live node's stated definition grows with T; fixed-volume constants (NL-4, 𝒮_T, K̄) are off-route/superseded | dag55_2 seeds; TUNIF/CODEX_REVIEW_TUNIF2 | as recorded |
| 9 | Six DAG-F3 unplaced symbols; ~30 collisions resolved by site | §6 | reading |
| 10 | Quantifier order (164 positions) | dag55_2 order, validity PASS | PROVEN for the encoded graph |
| 11 | (TC) fails with RLARGE's ε_loc by ×15.4-23.0 | dag55_3 (exact; controls fire) | PROVEN (arithmetic); repair ARGUED |
| 12 | (MOM_4)'s g-scaled demand is outside RLF v3's architecture | RLARGE/HW formulas | ARGUED (inference) |
| 13 | Dead ends: a_RS, η_1, c_RS, C_θ/ε_θ, N1-15's constant | dag55_2 graph (no live successors) | PROVEN for the encoded graph |
What "PROVEN for the encoded graph" does not cover: an edge I failed to encode, or an edge whose string does not mean what I
read it to mean (the re-read is manual; §0). The DAG-F3 list is the explicit boundary of what was encoded.

---

## 11. To the lead

**Counts (findings of this file):** 13 rows; PROVEN-by-check 6 (rows 1, 6, 10, 11 arithmetic, 13, and the control battery),
DAG-F1 CONDITIONAL 1, DAG-F2 FOUND 1 (conditional on Step 4's review), readings/inferences the rest. No claim of another file is
REFUTED here except as noted: **RLARGE's (TC) (via its own ε_loc) is infeasible as written (U3)**; and I record that PLAN_S26 §2e /
RTARGET T56-4's premise of "a level-dependent small-field threshold (as Balaban uses)" is not how the DAG (or, per BALABAN_EXTRACT,
Balaban) is built — thresholds are fixed.

**What should change in PROOF.md / HANDOFF (owner's call):**
1. The decade ledgers can be retired: no live edge runs from a magnitude back to an earlier choice (§8.3).
2. Add to node A's statements of (SDP)^A, (PRICE^ℛ), (M-f^A), (LI^F) the quantifier "constants independent of the cutoff n_♯"
   — the one unstated uniformity on which acyclicity rests (§3.1).
3. Record U3 as settled negatively: (TC) fails by ×15-23 with CL's ε_loc; adopt a quietness threshold η ≤ η_q/R (§8.1).
4. The only live level-count growth in the written hierarchy is C_fun (COF-crit); HANDOFF's critical-path item 5 should name
   its exact path to g_0 (§4.1) and point to KFACTOR_O55's Lemma TR as the pending repair (Codex review first).
5. For R^4: the live route has no fixed-volume-only constant; the open T-uniformity items are U5 (counterterms), (MOM_4), BFT's
   own T-uniformity and node A's asserted T-uniformity (§5 (b)). N1-15 via NL-4/GREENT should not be cited for anything (off-route,
   superseded, no live consumer).
6. The FI-1 choice (U4) and U1 (a_ret, a_A) remain the two RLARGE decisions the DAG cannot make; neither creates a constants cycle
   under Option A.

**The graph is reusable:** to test a proposed change, edit a copy of `checks/dag55_2_graph.py` under a new id and re-run the
checker; a new cycle or a new seed reaching g_0 is printed with every edge's file and string.

---

## Appendix A — every node (generated from `checks/dag55_2_graph.py`; strings verbatim)

Columns: id · live · tier · symbol · defining file: "locating string" (+ second string) · status · growth tags · volume (as stated) · note.

- **A_d** · live · t0 · A_d(L) := (d − 1)L(L − 1)/2 · RLARGE.md: "A_d(L) := (d - 1)L(L - 1)/2 (Lemma RS)" · DEF · vol: n/a
- **L** · live · t0 · L (block factor) · RLARGE.md: "L ≥ 3 odd; G = SU(N), N ≥ 2" · DATA · vol: n/a
- **N** · live · t0 · N (G = SU(N)) · RLARGE.md: "L ≥ 3 odd; G = SU(N), N ≥ 2" · DATA · vol: n/a
- **alpha_BFT** · live · t0 · α (lane-A Hölder exponent, 0 < α < θ) · REVIEW55_TUNIF.md: "(θ_w^c, θ_A, θ_w^r, θ, α) = (2, 1, 5/2, 1/2, 1/4)" · DEF · vol: n/a
- **d** · live · t0 · d = 4 · RLARGE.md: "d = 4; L ≥ 3 odd" · DATA · vol: n/a
- **kappa0** · live · t0 · κ_0 (level-0 soft coupling; evaluated numbers at κ_0 = 1) · PROOF.md: "At **κ_0 = 1**, L = 3, d = 4, every N" · DATA · vol: n/a · note: NOT the CE constant κ_0 ≈ 151.3 (node kappa0_CE)
- **kappa_RL** · live · t0 · κ (RLARGE kernel stiffness) · RLARGE.md: "e^{-κu_iφ_M(V)}" · DATA · vol: n/a · note: collides with κ_j, κ_0 (two objects), κ_d, κ_p, κ_s, κ(η,η′): placed by site
- **kappa_pm** · live · t0 · κ_± (soft-coupling window, κ_j ∈ [κ_-, κ_+]) · REVIEW_S22.md: "soft couplings κ_j ∈ [κ_-, κ_+]" · DATA · vol: n/a
- **m_ES1** · live · t0 · m (Stage-1 absorption margin, (ABS-ε)) · EPSSTAR.md: "(ABS-ε) is the definition of an admissible ε_*" · choice · vol: n/a
- **n_1** · live · t0 · n_1 = 4(3L)⁴ (PROOF N5-an♭) · PROOF.md: "with n_1 = 4(3L)⁴" · DEF · vol: n/a · note: collides with SF's n_1 = 497664 plaquettes per DX-rel hole: placed by site
- **n_int** · live · t0 · n_int = dL^{d-1}(L − 1) · RLARGE.md: "n_int = dL^{d-1}(L - 1)" · DEF · vol: n/a
- **p_L** · live · t0 · p_L (S4′ contour length, 5L − 4 = 11) · RLARGE.md: "p_L := 5L - 4" · DEF · vol: n/a
- **q_M** · live · t0 · q (EPS-T's Moser exponent, q > 4; SQ fixes 8, EPSSTAR uses 12, free) · SQ.md: "Fix q := 8." · choice · vol: n/a · note: q also names RES-dec's decay ratio q := L⁻³ + C_qτ (node q_RES) and other objects (SYMBOLS): placed by site; REVIEW55_CONST K1/K2: constants valid for q ≥ 8
- **theta_A** · live · t0 · θ_A = 1 (potential weight; hard cap) · REVIEW55_TUNIF.md: "(θ_w^c, θ_A, θ_w^r, θ, α) = (2, 1, 5/2, 1/2, 1/4)" · DEF · vol: n/a
- **theta_src** · live · t0 · θ ∈ (0, 1) (source weight ω_l = L^{θ(k−l)}) · REVIEW55_TUNIF.md: "(θ_w^c, θ_A, θ_w^r, θ, α) = (2, 1, 5/2, 1/2, 1/4)" · DEF · vol: n/a · note: needs θ < 1 for C_P = L/(e(1−θ)ln L) (lane A) and θ > 0 for Ω ≤ 1 + 1/(L^θ − 1)
- **theta_wc** · live · t0 · θ_w^c = 2 (curvature weight; pinned) · REVIEW55_TUNIF.md: "(θ_w^c, θ_A, θ_w^r, θ, α) = (2, 1, 5/2, 1/2, 1/4)" + NORMS.md: "A < 1 holds on {θ_w^r > 2} ∩ {θ_w^c ≥ 2}" · DEF (decoupling CONFIRMED faithful, REVIEW55_TUNIF W2) · vol: n/a
- **theta_wr** · live · t0 · θ_w^r > 2 (residual weight; 3 delivered on data) · REVIEW55_TUNIF.md: "(θ_w^c, θ_A, θ_w^r, θ, α) = (2, 1, 5/2, 1/2, 1/4)" · DEF · vol: n/a
- **A0_SQ** · live · t1 · A_0 := c_NC_T′(2.47N√κ_+ + 32^{1/8}C_0) (EPS-0 decay constant) · SQ.md: "A_0 := c_NC_T'(2.47N√κ_+ + 32^{1/8}C_0)" · DEF · vol: depth-uniform
- **A5** · live · t1 · Theorem A5 (main term of (I_k^E)″) ⇐ (a5-G♯) + (R♯) + (a5-U) + (a3-q) + (MS-Sob) · RLARGE.md: "Theorem A5 [ARGUED] ⇐ (a5-G♯) + (R♯) [A/PROOF-N2, OPEN] + (a5-U) [HIST, OPEN] + (a3-q) [HIST, OPEN] + (MS-Sob)" · ARGUED · vol: unstated
- **A_cg** · live · t1 · A_cγ_c ≤ (1 + √6)·C_{S1}(q, m)/m (Theorem ES-1) · EPSSTAR.md: "A_cγ_c ≤ (1 + √6)·C_{S1}(q, m)/m, a bound containing NO c_K, c_RB, C_K′, C_B, c_N or ε_*." · PROVEN (CONFIRMED REVIEW55_CONST K4) · vol: controls V_c on B_{3R/4−3}
- **B0_SQ** · live · t1 · B_0 := 4.1C_r/(1 − qL²) (STOKES-it; NOT RLARGE's B_0) · SQ.md: "Put B_0 := 4.1C_r/(1 - qL²), G := 2(1.011A_0 + B_0)" · DEF · vol: n/a
- **BFT012** · live · t1 · BFT-0/1/2 (composite critical point, scale-weighted regularity, analyticity) · REVIEW_S22.md: "**BFT-0 (existence, uniqueness, identification).**" · OPEN · vol: target uniform in k and T ≥ T_0
- **BFT3** · live · t1 · BFT-3 (locality, orders n ≤ 4, rate m_0) · REVIEW_S22.md: "**BFT-3 (locality).** For n ≤ 4" · OPEN (k = 1 PROVEN) · vol: target uniform in k and T ≥ T_0
- **BFT4** · live · t1 · BFT-4 (branch-action class, ||R_k||_𝒜 ≤ C_0) · REVIEW_S22.md: "**BFT-4 (branch-action class).**" · OPEN (k = 1 PROVEN) · vol: target uniform in k and T ≥ T_0
- **BFT5** · live · t1 · BFT-5 = lane B's (BFT-5_E): ε_5, C_5 'not on k or T (T ≥ 5)' · BFT_B.md: "There are ε_5 > 0 and C_5 < ∞, depending only on (N, L, κ_±) and not on k or T (T ≥ 5)" · OPEN, inputs named · vol: target uniform in k and T; clause (b) CONDITIONAL on (CO-fun)
- **B_0** · live · t1 · B_0 := B_1 + c + 1 (history/shadow constant; RLARGE: c_LI + c_f + 164ε_♯) · HW.md: "a, C_ℓ, c (from the moments and (LI)) → B_0 := B_1 + c + 1" + RLARGE.md: "B_0 = c_LI + c_f + 164ε_♯" · DEF · vol: 'the same at every level' · note: B_0 also names SQ's STOKES-it constant 4.1C_r/(1 − qL²) (node B0_SQ): placed by site
- **C0_BFT** · live · t1 · C_0 (BFT constant: tower size, regularity, locality, ||R_k||_𝒜) · REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0" · OPEN (target) · vol: as ε_0 · note: C_0 also names SQ's LOC-T constant and SF's MSG_0 constant: placed by site
- **C0_SQ** · live · t1 · C_0 (LOC-T's local residual-transport constant) · SQ.md: "16·32^{1/8}C_0θ ≤ ε_*" · PROVEN-HERE (LOC-T) · vol: n/a · note: C_0 also names BFT's C_0 and SF's MSG_0 constant in τ_c := s_0/(√NC_0): placed by site
- **C3** · live · t1 · C_3 (consumers' constant in E ≤ 4C_3ε_1²) · EPSSTAR.md: "The DESC-ε substitution needs η_♭ ≥ 4C_3ε_1²" · DEF (consumer side) · vol: n/a
- **C4** · live · t1 · C_4 of (MOM_4): E||1 − U_k(p)||⁴ ≤ C_4g_k⁴ (volume- and K-uniform required) · ../ym4d-existence/EXISTENCE.md: "There is C_4 < ∞ with" · HYPOTHESIS-NEW (not stated by layer 1) · growth: unstated-T (../ym4d-existence/EXISTENCE.md: "E||1 - U_k(p)||⁴ ≤ C_4g_k⁴, volume- and K-uniform (⇐ Theorem CB + a prefactor-free (RLF-3^dis) at"); unstated-K (../ym4d-existence/EXISTENCE.md: "E||1 - U_k(p)||⁴ ≤ C_4g_k⁴, volume- and K-uniform (⇐ Theorem CB + a prefactor-free (RLF-3^dis) at") · vol: REQUIRED volume- and K-uniform; no source proves it
- **CEcond** · live · t1 · constants of (CE-cond^ms) (a_±, β_a, β_b, M, m_e, C_e, …) · ../ym4d-existence/EXISTENCE.md: "(F, h, n, ε, w) first; then the constants of (CE-cond^ms), (MOM_4)," · HYPOTHESIS-NEW · vol: unstated
- **CEexp** · live · t1 · Corollary CE-exp^k level-uniform (⇐ N5-unif, (L-loc)_k, (FP-loc)_k, (N5-reg)_k) · ../ym4d-existence/EXISTENCE.md: "CE-exp^k CONDITIONAL; (N5-unif) CONDITIONAL ⇐ (H-K) + (H-C⁺) + (H-ℂ) (or ⇐ BFT-0,1,2,4 without (H-K))" · CONDITIONAL; inputs OPEN · growth: unstated-K (../ym4d-existence/EXISTENCE.md: "**(L-loc)_k OPEN, inside the B-NA wall** (needs all-order mixed-derivative decay: BFT-3 states orders ≤ 4 only, so (L-loc)_k is beyond BFT as stated [inference])") · vol: 'level-uniform' required; (L-loc)_k needs all-order decay beyond BFT-3
- **CLSmin** · live · t1 · (CLS-min)_{c_pr,t_pr} (coherent-background window lower bound) · RLARGE.md: "This is where the coherent background is priced: (CLS-min)_{c_pr,t_pr}" · CONDITIONAL ⇐ (REG-min) (DESC (b)) · vol: depth-uniform (SQ)
- **C_A** · live · t1 · C_A (prefactor of (SDP)^A) · HW.md: "C_A, c_A independent of g, K, T, k and the law" · OPEN (SDP)^A · vol: required independent of K, T, k and the law; n_♯-uniformity not listed
- **C_D** · live · t1 · C_D := max{G, C_r}, G = 2(1.011A_0 + B_0) (decay-class constant) · SQ.md: "C_D := max{G, C_r}, G = 2(1.011A_0 + B_0) (STOKES-it)" · DEF · vol: depth-uniform
- **C_Delta** · live · t1 · C_Δ = 2S_*n_1/r_* · PROOF.md: "so ε_* is explicit only up to C_Δ = 2S_*n_1/r_*" · DEF (not evaluated: (C_Δ-eval) OPEN) · vol: n/a (local)
- **C_H** · live · t1 · C_H := 2·6400^{n_♯}(C_ℓe^{aR}e^{38417B_0})^{n_♯+1}/(1 − L^{-γ_H}) · RLARGE.md: "C_H := 2·6400^{n_♯}(C_ℓe^{aR}e^{38417B_0})^{n_♯+1}/(1 - L^{-γ_H})" · DEF · vol: K-, T-independent constant (multiplies |T|: extensive bound)
- **C_Omega** · live · t1 · C_Ω := C + 3(N² − 1)/2 (TILT determinant + SLc source) · SF.md: "C_Ω := C + 3(N² - 1)/2 and a′ = a_sh²/(8N||C||m_sh)" · explicit (symbolic) · vol: n/a
- **C_T** · live · t1 · C_T(N, q) (EPS-T constant) · SQ.md: "ε_* = ε_*(N, q) > 0 and C_T = C_T(N, q)" + CONST_T.md: "C_T = √6 · F · B(4a) · Ĉ" · PROVEN-HERE (value uncomputed; numbers REFUTED as constructed, K26) · vol: 'on a 4D lattice torus (or on Z⁴)'
- **C_bg** · live · t1 · C_bg := 1.011√N·max{1 + 48𝔠_∞, 36p_L𝔠_∞} · SF.md: "C_bg := 1.011√N·max{1 + 48𝔠_∞, 36p_L𝔠_∞}" · DEF (read off BR1 (iii)) · vol: as 𝔠_∞
- **C_ell** · live · t1 · C_ℓ = (1 − λ_*)^{-3n_int/2}C_fc (unprimed; ε_2 and (S2)) · RLARGE.md: "C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc" · DEF · vol: 'the same at every level' (RLARGE l.545) · note: C_ℓ is two values (HW [RHW5-fix SYM-1]): unprimed here; primed C_ℓ′ (node C_ellp) for REL-boot's r and B_0
- **C_ellp** · live · t1 · C_ℓ′ (primed: C_fc′ = 2C_fc e^{c_f}; REL-boot's r and B_0) · HW.md: "§32 l.1690's PRIMED C_ℓ (with C_fc′ = 2C_fc e^{c_f}) is the one REL-boot's r and B_0 need" · DEF · vol: as C_ℓ
- **C_err** · live · t1 · C_err := C_p(K² + K_top²) + 4C_e[…] (SUP-price; K ≈ 78C_D) · SQ.md: "C_err := C_p(K² + K_top²) + 4C_e[K²/(L(L - 1)) + 1.011KC_DL/(L² - 1)]" · DEF · vol: n/a
- **C_fc** · live · t1 · C_fc = c_sf + 81C_Ae^{θa_bad R} · RLARGE.md: "C_fc = c_sf + 81C_Ae^{θa_bad R}, the same constant at every level" · DEF · vol: 'the same constant at every level'
- **C_flat_PR** · live · t1 · C_♭ := 4S_♭n_1/r_♭ (N_0-Lipschitz constant of Hess f; level 0/1) · PROOF.md: "C_♭ := 4S_♭n_1/r_♭" · DEF (not evaluated: (C_♭-eval) OPEN) · vol: n/a (local) · note: C_♭ names ≥ 2 objects: this level-0/1 Lipschitz constant and (H-C)'s class-wide C_♭^{(i)} (node C_flat_i); NORMS's N1-15 bounds neither
- **C_fun** · live · t1 · C_fun: (CO-fun)/(NC-Γ) curvature-half constant at critical points (Theorem COF route) · REVIEW_BFT_B_S9_S10.md: "PROVEN as an implication with a constant that grows like k" · PROVEN as implication with a k-growing constant · growth: K (REVIEW_BFT_B_S9_S10.md: "9.31·e·(k−1) ≈ 25(k−1)"); K (REVIEW55_BFTB.md: "Not k-uniform; the k-uniform form needs a level-decay input for the rows (lane A's (SPD)/(W2)).") · vol: T-uniform; NOT k-uniform · note: KF question (Step 4): multiplies η² of fixed size (BFT_B's row size π_l(V_l) ≤ 2C_NCC_bchκ_+L²η², 'uniform in l')
- **C_p_RLF0** · live · t1 · C, p of (RLF-0): |c̄_0| + |δβ_k| ≤ Cg_k^{-p}e^{-a_ret/g_k²} · RLARGE.md: "PLD Proposition W1R gives p = 6 + p(SC)" · CONDITIONAL ⇐ (SC)_k + (SF-irr)_{k+1} · vol: unstated
- **C_prime** · live · t1 · C′ = 53 (DESC's constant) · RLARGE.md: "(c_♭ = 1/640, C′ = 53 at N = 2, L = 3)" · DEF · vol: n/a
- **C_r_SQ** · live · t1 · C_r := 1.9Nκ̂^{3/2} (RES-dec) · SQ.md: "x_c ≤ C_rθq^{k-1-l}, C_r := 1.9Nκ̂^{3/2}" · PROVEN-HERE (RES-dec) · vol: uniformly in k
- **C_rho** · live · t1 · C_ρ = C_ρ(β_0′/2, 2R_0) (layer-1 remainder constant) · FLOW.md: "then the layer-1 constants C_ρ = C_ρ(β_0'/2, 2R_0) are fixed" · CONDITIONAL ⇐ (SF-g) · vol: unstated (a node-A output)
- **E2F** · live · t1 · (E2^𝔉′)/(CEM^{COL}) (node A input of HW's CRC route; delivers c_A = 0 for E+) · HW.md: "bounded measurable F_< ≥ 0 that is a function of U_0, …, U_{k_0−1} (**universally quantified**" · FALSE as quantified (universal F_<; REVIEW55_HWPLD F6); restated form OPEN · vol: 'independent of g ≤ g_0, k, K, T' asserted
- **EX_first** · live · t1 · (F, h, n, ε, w) (existence lane's first choices; ε = ε_1) · ../ym4d-existence/EXISTENCE.md: "(F, h, n, ε, w) first; then the constants of (CE-cond^ms), (MOM_4)," + ../ym4d-existence/EXISTENCE.md: "(LF-loc) (⇐ Theorem CB + (RLF-3^dis) at ε = ε_1" · choice · vol: n does not depend on g
- **E_0** · live · t1 · E_0 (per-cube polymer bound of (I_k^E)″ (b); bounded, not small) · HIST.md: "E_0 is bounded but NOT small" · HYPOTHESIS (part of (I_k^E)″) · vol: asserted independent of g, k, K, T (hypothesis)
- **F_sched** · live · t1 · F (Moser radius-schedule factor; printed 175.8 is INADMISSIBLE, REVIEW55_CONST K26) · CONST_T.md: "C_T = √6 · F · B(4a) · Ĉ" · DEF (value REFUTED; structure CONFIRMED as upper bound for q ≥ 8) · vol: sup over the ball radius R is finite (asymptote 16/α²)
- **G_inf** · live · t1 · G_∞ := G^A (block-inverse bound of GF-dec (e), every background) · SF.md: "**G_∞(U) ≤ G^A := L^d/√(2d) + Γ_1(1 + c_R)**" · PROVEN/COMPUTED (SF §19) · vol: 'every background, frozen holes too'
- **IkE** · live · t1 · (I_k^E)″ representation: E_0, κ_p, α_E (g, k, K, T-independent by hypothesis) · HIST.md: "E_0 is bounded but NOT small" + HIST.md: "all constants (E_0, κ_p, α_E, C_ℓ, B_0) independent of g, k, K, T and 𝔥" · HYPOTHESIS [P] · vol: hypothesis: 'all constants (E_0, κ_p, α_E, C_ℓ, B_0) independent of g, k, K, T and 𝔥' · note: the hypothesis ASSERTS K/T-uniformity; its C_ℓ, B_0 are representation-side (v2) objects, NOT HW's (DAG-F3 resolved by site)
- **K_FP** · live · t1 · K_FP := max{(2/c_D)(1 + √c_D/(4√d)), (1 + 4√d/√c_D)/s_M} · PROOF.md: "K_FP := max{(2/c_D)(1 + √c_D/(4√d)), (1 + 4√d/√c_D)/s_M}" · PROVEN-HERE (Lemma FPq) · vol: n/a
- **Kcompat** · live · t1 · compatibility (K): 48β_b²W²C_4ρ ≤ A_*, 16β_aWC_4^{1/2}ρ ≤ A_* · ../ym4d-existence/EXISTENCE.md: "48β_b²W²C_4ρ ≤ A_*" · condition · vol: g-independent apart from ρ
- **LIF** · live · t1 · (LI^F) capped future-insensitivity (HW) · RLARGE.md: "**(LI^F)** (capped spectator weights only, LI-1; over ℛ_𝔥^↑ and R(𝔥))" · OPEN [HW] · vol: unstated
- **MSSob** · live · t1 · (MS-Sob) (multi-scale Sobolev; input of A5 and of AE-red) · RLARGE.md: "(MS-Sob) ⇐[ARGUED] MSG-loc-dev + MS-HLS + (SQ-dev) [OPEN]" · OPEN (back on the critical path, TAUFLAT) · vol: unstated
- **NA_empty** · live · t1 · (NA-∅) exponent and constant (node A; NA-1 form) · RLARGE.md: "**(NA-∅)** (NA-1 form, with 𝒱_K^{LF})" · OPEN [node A] · vol: 'uniformly in K' required
- **N_prime** · live · t1 · N′ := N_r·N_μ(|Õ^{1/2}|) (finite, not evaluated) · SF.md: "Write N′ := N_r·N_μ(|Õ^{1/2}|) (finite, not evaluated)" · existence only · vol: unstated (a weighted norm of Õ^{1/2})
- **R** · live · t1 · R := 2R_0 (flow slack) · FLOW.md: "Fix FIRST β_- := β_0'/2 and R := 2R_0" + FLOW.md: "γ, g_1, β_±, R do not depend on K or on the torus." · DEF · vol: stated: does not depend on K or on the torus
- **R0** · live · t1 · R_0 (UNIV-1L deviation) · FLOW.md: "|B_n - B_j - β_0'(n - j)log L| ≤ 2R_0 (UNIV-1L twice)" · CONDITIONAL ⇐ (UNIV-1L) · growth: unstated-K (RLARGE.md: "k-uniform vector step gap OPEN [s]") · vol: stated K- and torus-free (F-tune), but Theorem UNIV's k-uniform vector step is OPEN
- **REGmin** · live · t1 · (REG-min) (cone-local free-boundary minimisers in Σ_dec) · SQ.md: "**(REG-min)** holds, by Theorem RED-0 (§13.5) with τ_R := min{τ_0, τ_*, τ_S, θ_S/C', θ_0/C'}" · PROVEN as implication (SQ §15.3; given EPS-0's inputs) · vol: depth-uniform; 'any T with level-k side ≥ 3'
- **RLF3dis** · live · t1 · (RLF-3^dis) constants a_d, p_d, C_d (existence lane's reading of (RLF-3′)) · ../ym4d-existence/EXISTENCE.md: "g^{-p_d}e^{-a_d/(2g_{j'}²)}" + ../ym4d-existence/EXISTENCE.md: "Theorem CB + a **prefactor-free** (RLF-3^dis) at g-scaled thresholds (§20.2)" · ARGUED as a literal instance of (RLF-3′) (RLARGE K8 [inference]; U11 unconfirmed) · vol: 'prefactor-free' and g-scaled thresholds demanded by (MOM_4); not stated by layer 1
- **R_star_N5** · live · t1 · R_* := least R with ε_R ≤ ½ (walk-expansion box size) · PROOF.md: "R_* := the least R with ε_R ≤ ½" · DEF · vol: n/a
- **SC_k** · live · t1 · (SC)_k fixed-V sea expansion (HYPOTHESIS) and (W1-ret′^J)_k · RLARGE.md: "**(SC)_k** fixed-V sea expansion with the collar-bad family" · HYPOTHESIS · vol: unstated
- **SF_last** · live · t1 · (SF-last) level-K integrand: a many-level item (≈ 46-184 wrap levels) · RLARGE.md: "**now a many-level item** (wrap levels, §5.4)" · HYPOTHESIS · vol: wrap levels K-independent (K16)
- **S_prime** · live · t1 · S′_m := N_m(|Õ_0|) + e^{mr_1}C_Δα_* · PROOF.md: "S'_m := N_m(|Õ_0|) + e^{mr_1}C_Δα_*" · DEF · vol: n/a
- **T0_BFT** · live · t1 · T_0 (BFT; minimal level-k torus side — a LOWER bound) · REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0" · OPEN (target) · vol: lower bound on T only
- **T0_N5** · live · t1 · T_0 := 4R_* + 6 (minimal torus side; a LOWER bound on T) · PROOF.md: "T_0 := 4R_* + 6" + PROOF.md: "uniformly in k (level 0 is k-independent apart from κ_0) and T ≥ T_0" · DEF · vol: lower bound on T only; N5-sf0 holds 'uniformly in k … and T ≥ T_0'
- **a** · live · t1 · a := min{θa_bad, a_A} (the live unreturned-defect exponent) · RLARGE.md: "a := min{θa_bad, a_A}" · DEF · vol: as its inputs; U1 open (a_A unfixed)
- **a5G** · live · t1 · (a5-G♯), (a5-U), (MIN-reg) (SF's background clauses) · REVIEW_S22.md: "SF: BFT-1 (θ_w > 0), 2 (complex ball for (R♯)) and 5, giving (a5-G♯), (a5-U) and (MIN-reg)." · OPEN (⇐ BFT-0, 1, 2, 5) · vol: as BFT
- **a_A** · live · t1 · a_A (exponent of (SDP)^A) · HW.md: "C_A, c_A independent of g, K, T, k and the law" · OPEN (SDP)^A [P, node A] · vol: required independent of K, T, k and the law (HW §18.1); n_♯-uniformity not listed
- **a_D** · live · t1 · a_D := min{a_bad, a_cb} (collar-bad family's window exponent) · RLARGE.md: "a_D := min{a_bad, a_cb}, with θ ∈ (0, 1/(96·82))" · CONDITIONAL (row 10f) · vol: as inputs
- **a_bad** · live · t1 · a_bad := c_pr·min{ε_1², t_pr²} (HW Lemma W-bad) · RLARGE.md: "a_bad := c_pr·min{ε_1², t_pr²}" · CONDITIONAL ⇐ (CLS-min) (level 0 PROVEN) · vol: as ε_1, c_pr, t_pr
- **a_cb** · live · t1 · a_cb (collar-bad window exponent, Lemma W-cb) · RLARGE.md: "κε_loc²/(64N), c_pr·min{η_q², t_pr²}}" · CONDITIONAL ⇐ (CLS-min) + (TC) [uncounted] · vol: as inputs
- **a_p_ac** · live · t1 · a_p = τ_c²/(2N), a_c ≈ κ_sτ_c²/(4N) (DX-rel prices) · SF.md: "a_p = τ_c²/(2N) = 3.14·10⁻¹¹⁸" · DEF · vol: as τ_c
- **a_prime** · live · t1 · a′ ((RLF-4) exponent: a′ < a, a′ ≤ the (NA-∅) exponent) · RLARGE.md: "(any a′ < a, and a′ ≤ the (NA-∅) exponent)" · DEF · vol: n/a
- **a_ret** · live · t1 · a_ret (returned-cluster exponent; U1) · RLARGE.md: "no source states its value" + PLD.md: "a_ret := min{κε_1²/(2048N), 49η_q²/(1024σ_fl²), κε_loc²/(64N)}" · OPEN (U1); candidate PLD §16.8, conditional on (SC)_k · vol: per cube, on the chart; 'Levels k ≥ 1 need σ_fl at level k (N5 level-uniformity, BFT)'
- **a_sh** · live · t1 · a_sh = ρ_band/(16L⁴N′), R_sh = μ^{-1}ln(r_sol/a_sh), |Ω_B| ≤ 4(2R_sh + L)⁴ · SF.md: "a_sh = ρ_band/(16L⁴N′) = 1.759·10⁻⁶⁴/N′" + SF.md: "|Ω_B| ≤ 4(2R_sh + L)⁴" · DEF · vol: a fixed R_sh-neighbourhood: g- and T-independent (needs a torus larger than it)
- **alpha_star** · live · t1 · α_* := min{r_*, (γ_0/2 − 𝔇_0(m))/(C_Δe^{mr_1})} · PROOF.md: "α_* := min{r_*, (γ_0/2 - 𝔇_0(m))/(C_Δe^{mr_1})}" · DEF · vol: n/a
- **aprime_DX** · live · t1 · a′ = a_sh²/(8N||C||m_sh) (DX′ per-block exponent; NOT RLARGE's a′) · SF.md: "C_Ω := C + 3(N² - 1)/2 and a′ = a_sh²/(8N||C||m_sh)" · DEF · vol: n/a
- **b_1** · live · t1 · b_1 := n_P + 12κ(1 + A_d(L))² (Proposition CL) · RLARGE.md: "b_1 := n_P + 12κ(1 + A_d(L))²" · DEF (frozen v1, PROVEN-HERE) · vol: n/a
- **b_D** · live · t1 · b_D (CRC depth constant) · HW.md: "b_D = h_D·(C_sh·81·c_+ + c_U)" · DEF · vol: n/a
- **b_n** · live · t1 · b_n (CRC activity constant, ∝ c_+; geometry × allowance) · HW.md: "b_n = C_sh·81·h_n·c_+ + h′_n·c_U" · DEF · vol: n/a
- **beta0p** · live · t1 · β_0′ (one-loop slope of the soft kernel) · FLOW.md: "with β_0' COMPUTED for the soft kernel" · COMPUTED (target) · vol: infinite-volume β (Def F-g, (SF-∞))
- **beta_m** · live · t1 · β_- := β_0′/2 · FLOW.md: "Fix FIRST β_- := β_0'/2 and R := 2R_0" · DEF · vol: stated K/T-free
- **beta_p** · live · t1 · β_+ := β_0′ + C_ργ²/log L · FLOW.md: "β_± := β_0' ± C_ργ²/log L (so β_0'/2 ≤ β_- ≤ β_0' ≤ β_+ ≤ 3β_0'/2)" · DEF · vol: stated K/T-free
- **c_A** · live · t1 · c_A (shadow allowance of (SDP)^A) · HW.md: "C_A, c_A independent of g, K, T, k and the law" · OPEN (SDP)^A · vol: required independent of K, T, k and the law; n_♯-uniformity not listed
- **c_B** · live · t1 · c_B := 38416B_0/log L · RLARGE.md: "38416B_0/log L" · DEF · vol: n/a
- **c_LI** · live · t1 · c_LI ((LI) allowance) · HW.md: "allowance c_LI plus the moments' own." · OPEN ((LI^F), HW) · vol: unstated
- **c_U** · live · t1 · c_U (HW's (CRC) constant; input value 1, output 2ε_2) · HW.md: "c_+ = c_A + c_U (c_U := 2ε_2 ≤ 1)" · DEF (order: c_U := 1 first) · vol: n/a · note: HW's c_U ≠ PLD's c_U (HW [RHW5-fix SYM-1] (c)): placed by site
- **c_att** · live · t1 · c_att(ρ) (attachment constant; 320001 at ρ = 8 after SH-att′) · HW.md: "c_att(ρ) := 1 + 2401·64·ρ = 1 + 153664ρ" · DEF (superseded value) · vol: n/a
- **c_f** · live · t1 · c_f (shadow allowance of (M-f^cap); C_sh·81·c_+) · HW.md: "c_f := 531441·c_+" + HW.md: "b_D = h_D·(C_sh·81·c_+ + c_U)" · DEF · vol: as c_+ · note: c_f has ≥ 3 definitions in HW (SL-1's 81(c_A + c_sf′); §32's 531441c_+; §35.7's C_sh·81·c_+): the live one is §35.7's (string2)
- **c_flat** · live · t1 · c_♭ = 1/640 (= 1/(4C_1), C_1 = 160 of SUP-price) · RLARGE.md: "(c_♭ = 1/640, C′ = 53 at N = 2, L = 3)" · DEF · vol: n/a · note: lower-case c_♭; NOT PROOF's C_♭ (node C_flat_PR)
- **c_inf** · live · t1 · 𝔠_∞ (bound for N_0(|C(U, V)|); in force 𝔠_∞^♯ = 315.19) · PROOF.md: "𝔠_∞ := min{8coth⁴(a/2), 81((N² - 1)n_Ω)^{1/2}}/(γ'(1 - ε_R)) + ν_w + C_Δα_*" + PROOF.md: "N_0(|C(U, V)|) ≤ 𝔠_∞^♯ := k′_0 + δ + k_0(e_0 + δk_0)/(1 - e_0 - δk_0)" · PROVEN-HERE / COMPUTED (CI-bg) · vol: 'on tori T ≥ T_0' (CI-bg); level 0 only — 'the level-1 𝔠_∞^{(1)} is not covered'
- **c_plus** · live · t1 · c_+ = c_A + c_U · HW.md: "c_+ = c_A + c_U (c_U := 2ε_2 ≤ 1)" · DEF · vol: as c_A · note: REVIEW55_HWPLD F4: the ring is free, c_+ = c_A + c_U (not c_A + 17c_U)
- **c_pr** · live · t1 · c_pr = c_♭/C′² · RLARGE.md: "via (REG-min) (primary), c_pr = c_♭/C′², t_pr = C′τ_♭" · DEF · vol: depth-uniform (SQ)
- **c_sf** · live · t1 · c_sf ((SF-cap)^A at rate 24θ(1 + 2Rg_K²)) · RLARGE.md: "c_sf at rate 24θ(1 + 2Rg_K²) < 1 on defect-free columns" · OPEN (SF-cap)^A [node A] · vol: required 'uniformly under conditioning'; K/T unstated · note: PLD §16.7's per-cube formula c_sf := e^{2c_U(81 + Δ_sh)}c_lcr is NOT valid (REVIEW55_HWPLD F9); no edge is built from it
- **delta_0** · live · t1 · δ_0 := min{1/(640N), 2/N³} (Lemma PM) · HIST.md: "min{1/(640N), 2/N³}" · DEF · vol: n/a
- **gamma_prime** · live · t1 · γ′ := γ_0 − C_Δα_* · PROOF.md: "γ' := γ_0 - C_Δα_* (≥ γ_0/2)" · DEF · vol: n/a
- **gap0** · live · t1 · level-0 gap input γ_0 (in force: λ_min(Õ_0) ≥ 4.229507·10⁻³, CI-0, κ_0 = 1) · PROOF.md: "N5-sf0 is re-evaluated with λ_min(Õ_0) ≥ 4.229507·10⁻³ in place of γ_0" + PROOF.md: "γ_0 := c_1min(1/2, κ_-/2)/L²" · COMPUTED (computer-assisted, certified; REVIEW_SF_S7) · vol: 'on every torus, compressions included' · note: γ_0 names: this gap, FLOW's γ_0 (node gamma0), and (here) the formula c_1min(1/2, κ_-/2)/L² whose c_1 is one of ≥ 11 c_1's
- **kappa0_CE** · live · t1 · κ_0 ≈ 151.3 (Theorem CE's decay constant) · HW.md: "CE-col constants κ_0 ≈ 151.3, κ̃_0 ≈ 217.05" · PROVEN (SF/PROOF CE) · vol: n/a · note: NOT the level-0 soft coupling κ_0 (node kappa0)
- **kappa_d** · live · t1 · κ_d (tail rate of the returned remainders; Theorem CE needs κ > 3κ_0 + 3 ≈ 457) · RLARGE.md: "κ > 3κ_0 + 3 (≈ 457 in M-units)" · OPEN (RLF-2) · vol: K-, T-independent (RLF v3 statement)
- **lam_bg** · live · t1 · λ_min ≥ 3.1727·10⁻³ (gap at real backgrounds of the session-23 class) · PROOF.md: "λ_min ≥ 3.1727·10⁻³, ε_* = 2.476·10⁻¹³/C_Δ" · COMPUTED (CI-bg, κ_0 = 1; CS-1) · vol: on tori T ≥ T_0 (CI-bg)
- **lambda_star** · live · t1 · λ_* = 6θ(1 + 2Rg_K²) · RLARGE.md: "λ_* = 6θ(1 + 2Rg_K²)" + RLARGE.md: "log C_ℓ ≈ (3n_int/2)·log(1/(1 - λ_*)) ≤ 324·log(4/3) ≈ 93 at λ_* ≤ ¼" · DEF · vol: bounded by 12θ under g_K² ≤ 1/(2R)
- **m0_BFT** · live · t1 · m_0 (BFT locality rate; THETAW J5: one symbol, three jobs) · REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0" · OPEN (target) · vol: as ε_0 · note: DAG-F3 (unresolved): the norm weight 'm' of 𝔐, BFT-3's rate and BFT-4's polymer weight are all written m/m_0 (THETAW J5; REVIEW55_TUNIF W13 'flagged, not decided')
- **m_N5** · live · t1 · m ∈ (0, m_cov^{(0)}), m_1 ∈ (0, m), a_N5 := m − m_1 (N5-sf0 decay rates) · PROOF.md: "Fix m ∈ (0, m_cov^{(0)}) and m_1 ∈ (0, m), a := m - m_1" · choice · vol: n/a · note: this 'a' is NOT RLARGE's a = min{θa_bad, a_A}: placed by site
- **q_RES** · live · t1 · q := L⁻³ + C_qτ (RES-dec residual decay ratio; NOT the Moser q) · SQ.md: "q := L⁻³ + C_qτ ≤ (L⁻² + L⁻³)/2" · DEF · vol: n/a
- **r_flat** · live · t1 · r_♭, S_♭ (Lemma N5-an♭; exist, not computed) · PROOF.md: "There are r_♭ ∈ (0, 1/(20p_L)] and S_♭ < ∞, depending only on (N, L, κ_±)" · PROVEN-HERE (existence) · vol: n/a (local)
- **rho_band** · live · t1 · ρ_band = τ_c/(2C_W) · SF.md: "ρ_band = τ_c/(2C_W) = 2.280·10⁻⁶¹ (C_W = 95.145)" · DEF · vol: as τ_c
- **rstar** · live · t1 · r_*, S_* (Lemma N5-an analyticity constants; exist, not computed) · PROOF.md: "depend on the analyticity constants r_*, S_* of" · PROVEN-HERE (existence) · vol: n/a (local) · note: r_* also names SF's radius-chain r_* = 5.16·10⁻³¹ and v1's R_*: placed by site
- **sf_chain** · live · t1 · SF radius chain (ζ, s_0, r_*^{SF}, r_sol) ∝ G_∞^{-2} · SF.md: "Scaling: ζ ≈ 1/(4032c′_gX_∞G_∞²), so every threshold of the chain is ∝ G_∞^{-2}" · PROVEN (SF s5 F2, arithmetic) · vol: g-independent and volume-independent · note: r_* here collides with N5-an's r_* (node rstar): placed by site
- **sigma_fl** · live · t1 · σ_fl² = 16(1 + O(α_*))/λ_min (fluctuation variance) · PLD.md: "σ_fl² = 16(1 + O(α_*))/λ_min" + PLD.md: "Levels k ≥ 1 need σ_fl at level k (N5 level-uniformity, BFT)." · DEF (Gaussian part only) · growth: unstated-K (PLD.md: "Levels k ≥ 1 need σ_fl at level k (N5 level-uniformity, BFT).") · vol: level 0 certified; level k ≥ 1 needs BFT
- **stage_consts** · live · t1 · stage-k constants (CL^J's C_J, Λ^J_1, …) using g_k, g_{k+1} · RLARGE.md: "stage-k constants also use the kernel coupling g_{k+1} of K_{k+1} through CL^J" · OPEN (row 2b, U4) · vol: unstated
- **theta** · live · t1 · θ (HW CAP-1 weight; θ ∈ (0, 1)) · RLARGE.md: "max{6θ, 24θ}(1 + 2Rg_K²) < 1" · choice · vol: g/K/T-independent constant · note: θ names ≥ 5 objects (CAP-1, BFT source weight, CURV1's θ, NAH-unif's (1−K̄)/2, SQ's curvature size θ): placed by site
- **theta_cb** · live · t1 · θ ∈ (0, 1/(96·82)) for the collar-bad family (W-cb) · RLARGE.md: "a_D := min{a_bad, a_cb}, with θ ∈ (0, 1/(96·82))" · constraint (row 10f) · vol: n/a
- **W** · live · t2 · W := 2n_♯ + 5 (wrap-level width) · RLARGE.md: "W := 2n_♯ + 5" · DEF · vol: K-independent; ≈ 184 wrap levels (§5.4 [hand])
- **eps0_BFT** · live · t2 · ε_0 (BFT small-field threshold for the level-k curvature) · REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0" + REVIEW_S22.md: "**depending only on (N, L, κ_±)**" · OPEN (target) · vol: claimed for every k ≥ 1 and every torus with level-k side ≥ T_0 (OPEN)
- **eps1** · live · t2 · ε_1 (the χ_Q cut, RLARGE l.58) · RLARGE.md: "χ_Q := Π_{p⊂int Q}1{||1 - U(p)||_op < ε_1}" · threshold (choice) · vol: g-, K-, T-independent (a fixed threshold) · note: ≥ 6 objects named ε_1 (SYMBOLS / EPS1_SWEEP §1); this is the χ_Q cut
- **eps_J_loc** · live · t2 · ε^J_loc := ε_1/(157(1 + A_d)√N) (CL^J's joint collar threshold) · HIST.md: "ε^J_loc := ε_1/(157(1 + A_d)√N)" · DEF (CL^J PROVEN-HERE) · vol: as ε_1
- **eps_N5_unif** · live · t2 · level-uniform N5 background threshold (all levels; matching units) · PROOF.md: "level-uniformity, BFT-0, 1 (θ_w = 0), 2 and 4" + RLARGE.md: "So K-independent thresholds, hence K-independent exponents and n_♯, exist only under BFT-0, 1" · OPEN (needs BFT-0, 1, 2, 4) · growth: unstated-K (RLARGE.md: "constants are not covered by CI-bg; the level-uniform form is GAP along the per-level route") · vol: K-uniform only under BFT; per-level route GAP (CURV-F2′, CURV-F2″)
- **eps_bg** · live · t2 · ε_bg^{(TH-bg)} (largest ε_bg allowed by the corrected (TH-bg)) · SF.md: "where ε_bg^{(TH-bg)} is the largest ε_bg allowed by the corrected (TH-bg) ε_bg²(n_1/2 + 1.03κ_sn_K) ≤ ½min{a_p, a_c}" · DEF · vol: as τ_c
- **eps_br** · live · t2 · ε_br := min{ε_*/(1 + 36p_L𝔠_∞), 1/(24𝔠_∞²C_♭), r_♭/(24𝔠_∞), r_♭/(18(3L − 1)), 1/(1728𝔠_∞K_FP)} · PROOF.md: "ε_br := min{ ε_*/(1 + 36p_L𝔠_∞), 1/(24𝔠_∞²C_♭), r_♭/(24𝔠_∞), r_♭/(18(3L - 1)), 1/(1728𝔠_∞K_FP) }" · PROVEN-HERE (Lemma BR1) · vol: 'Let T ≥ T_0' (lower bound only)
- **eps_loc** · live · t2 · ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}} (Proposition CL) · RLARGE.md: "ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}}" · DEF (frozen v1) · vol: as ε_1
- **eps_star_EPST** · live · t2 · ε_*^{EPS-T}(N, q) (ε-regularity threshold; fixed by (ABS-ε) at margin m) · SQ.md: "ε_* = ε_*(N, q) > 0 and C_T = C_T(N, q)" + EPSSTAR.md: "(ABS-ε) is the definition of an admissible ε_*" · PROVEN-HERE (EPS-T; constants uncomputed) · vol: 'on a 4D lattice torus (or on Z⁴)'; scale-invariant in R
- **eps_star_N5** · live · t2 · ε_* := α_*/(10p_L(4R_* + 5)L) (N5-sf0 threshold; 2.476·10⁻¹³/C_Δ) · PROOF.md: "ε_* := α_*/(10p_L(4R_* + 5)L)" · PROVEN-HERE (N5-sf0, CONFIRMED-WITH-FIX) · vol: uniform in T ≥ T_0 (stated) · note: ε_* names 4 objects (EPSSTAR §6.1): N5-sf0's (this), EPS-T's (node eps_star_EPST), BG-b's (ε_1²/(4NB))^{1/2}, BFT_B's local max_tε_f
- **eta_flat** · live · t2 · η_♭ := c_♭τ_♭²/C′² (DESC-ε's energy threshold) · SQ.md: "η_♭ := c_♭τ_♭²/C'²" · DEF · vol: depth-uniform
- **eta_q** · live · t2 · η_q := min{ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d} (RS-lin) · HIST.md: "η_q := min{ ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d }" · DEF; RS-lin PROVEN-HERE (CONFIRMED REVIEW55_ARS F26) · vol: as ε_1
- **g1_FLOW** · live · t2 · g_1 := (γ^{-2} + R)^{-1/2} (FLOW's ceiling on the FINAL coupling; NOT the level-1 coupling) · FLOW.md: "g_1 := (γ^{-2} + R)^{-1/2}: for every K ≥ 1 and g ∈ (0, g_1]" · DEF · vol: stated K/T-free
- **g2_CRC** · live · t2 · g²_CRC := a/(b_n + aR + log(12800C_ℓ)) ((S2) ceiling) · HW.md: "g_K² < g²_CRC := a/(b_n + aR + log(12800C_ℓ))" · DEF · vol: g-independent ceiling
- **g_3** · live · t2 · g_3 (explicit threshold for (C3)) · ../ym4d-existence/EXISTENCE.md: "(true for g ≤ g_3, an explicit threshold" · DEF · vol: g-independent
- **g_DX** · live · t2 · DX′ ceiling g_0² ≲ 2.5·10⁻¹⁵²/C_Ω (stage-0 coupling) · SF.md: "g_0² ≲ 2.5·10⁻¹⁵²/C_Ω (was 7.3·10⁻¹⁸⁰ at τ^A)" + SF.md: "g_0² ≤ g_{DX′}² ≈ 1.49·10⁻²³⁷/(C_ΩN′²f⁸)" · DEF (arithmetic) · vol: g-independent; per deep block
- **g_FS1** · live · t2 · truncation invisibility g_0² ≤ 1.8·10⁻¹¹³ · SF.md: "g_0² ≤ 1.8·10⁻¹¹³ (g_0 ≤ 4.3·10⁻⁵⁷)" · DEF · vol: g-independent
- **g_band** · live · t2 · band window g_0 ≤ ρ_band/(4√Np_0·max{N_r, 2N_μ(|𝒞|)}) · SF.md: "g_0 ≤ ρ_band/(4√Np_0·max{N_r, 2N_μ(|𝒞|)})" · DEF · vol: g-independent
- **g_c** · live · t2 · g_c (NG-red's coupling threshold) · ../ym4d-existence/EXISTENCE.md: "Given g ≤ g_c, choose I = I(g)" · DEF · vol: unstated
- **g_hole** · live · t2 · DX-rel hole ceiling g_0² ≲ (min{a_p, a_c}/a_p)·1.6·10⁻¹²⁶ · SF.md: "g_0² ≲ 1.6·10⁻¹²⁶" · DEF (arithmetic) · vol: g-independent
- **g_star_SF** · live · t2 · O0's g_* := min of the stage-0 ceilings (a ceiling on the STAGE-0 coupling) · SF.md: "all enter O0's **g_*** (min of all)" · DEF · vol: g-, T-independent · note: g_0 here = stage-0 coupling (u_0 = 1/g_0²); REVIEW55_HWPLD F1: comparable with RLF's g_0 via (F-3) at K = 1
- **gamma** · live · t2 · γ := min{γ_0, (β_0′ log L/(2C_ρ))^{1/2}} · FLOW.md: "then γ := min{γ_0, (β_0'log L/(2C_ρ))^{1/2}}" · DEF · vol: stated K/T-free
- **gamma0** · live · t2 · γ_0 (domain of (SF-g)/(RLF-δ)) · FLOW.md: "whenever g_0, …, g_k ∈ (0, γ_0]" + RLARGE.md: "The γ_0 needed for Cg^{-p}e^{-a_ret/g²} ≤ g⁶" · OPEN (node A, (RLF-δ)) · vol: g-independent (RLARGE l.198); K/T: as its inputs
- **n_H** · live · t2 · n_H := ⌊(4 + c_B)/(aβ_-)⌋ · RLARGE.md: "n_H := ⌊(4 + c_B)/(aβ_-)⌋" · DEF · vol: K-, g-independent (RLARGE §5.4 'Every row is K-independent')
- **n_J_star** · live · t2 · n^J_* (frozen cutoff of R1^J) · RLARGE.md: "n_♯ ≥ max{n^J_*, n_H}" · DEF (frozen lemmas) · vol: n/a
- **n_sharp** · live · t2 · n_♯ (returned/unreturned cutoff) · RLARGE.md: "n_♯ ≥ max{n^J_*, n_H}" + HW.md: "n_♯ ≥ max{n_H(a, B_0), b_D/(aβ_-log L)}" · choice · vol: K-independent · note: n_♯ names 3 objects: v1's ⌊4/(a_♯β_-)⌋ (superseded, l.832), this cutoff, and SF's 'HIST n_♯' table rows
- **rC_BFT** · live · t2 · r_ℂ ∈ (0, 1] (BFT complex radius, |z|_∞ ≤ r_ℂε) · REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0" · OPEN (target) · vol: as ε_0
- **t_pr** · live · t2 · t_pr = C′τ_♭ · RLARGE.md: "via (REG-min) (primary), c_pr = c_♭/C′², t_pr = C′τ_♭" · DEF · vol: depth-uniform (SQ)
- **tau_R** · live · t2 · τ_R := min{τ_0, τ_*, τ_S, θ_S/C′, θ_0/C′} · SQ.md: "**(REG-min)** holds, by Theorem RED-0 (§13.5) with τ_R := min{τ_0, τ_*, τ_S, θ_S/C', θ_0/C'}" · DEF · vol: n/a
- **tau_c** · live · t2 · τ_c = τ^A = 3.60·10⁻³¹ (PROVEN admissible stage-0 threshold) · SF.md: "the PROVEN admissible stage-0 threshold is τ_c = τ^A = 3.60·10⁻³¹" + SF.md: "g-independent and volume-independent" · PROVEN (SF) · vol: 'g-independent and volume-independent' (SF s5 F2 chain)
- **tau_flat** · live · t2 · τ_♭ := min{τ_F, τ_R, θ_0/C′, ε_M/(C_DC′), θ_♯/C′, 1/(73.6Nc′²A′²)} · SQ.md: "Write τ_♭ := min{τ_F, τ_R, θ_0/C'," · DEF · vol: depth-uniform
- **tau_sizes** · live · t2 · τ_0, τ_*, τ_S, θ_S (RES-dec / FORCE / STOKES-NA admissible sizes) · SQ.md: "τ_R := min{τ_0, τ_*, τ_S, θ_S/C'} (τ_S: the size at which STOKES-NA's smallness" · DEF · vol: n/a
- **theta0_SQ4** · live · t2 · θ_0^{SQ4} := min{θ_G, θ_ε} (EPS-0's threshold) · SQ.md: "θ_0 := min{θ_G, θ_ε}" · DEF · vol: depth-uniform · note: θ_0 names 4 objects (SYMBOLS): this, SUP-price's 1/(2C_err) (node theta0_SUP), and two others: placed by site
- **theta0_SUP** · live · t2 · θ_0^{SUP} := 1/(2C_err) (SUP-price's range) · SQ.md: "θ ≤ θ_0 := 1/(2C_err)" · DEF · vol: n/a
- **theta_G** · live · t2 · θ_G (largest θ with qβ ≤ ½ and LEV-E's conditions; ≈ 1.168·10⁻¹²/q) · SQ.md: "θ_G := the largest θ with qβ ≤ ½ and LEV-E's conditions" · DEF · vol: 'depth-independent'
- **theta_eps** · live · t2 · θ_ε (largest θ with 4·2.47N√κ_+θ ≤ ε_* and 16·32^{1/8}C_0θ ≤ ε_*) · SQ.md: "θ_ε the largest θ with 4·2.47N√κ_+θ ≤ ε_* and 16·32^{1/8}C_0θ ≤ ε_*" · DEF · vol: n/a
- **theta_sharp_SQ** · live · t2 · θ_♯(N, L, κ_-, C_D) (SUP-price's admissible θ) · SQ.md: "θ_♯(N, L, κ_-, C_D) := the largest θ satisfying all of" · DEF · vol: n/a
- **K0_T1** · live · t3 · K_0, T_1(R) (minimal depth and torus side — LOWER bounds) · ../ym4d-existence/EXISTENCE.md: "then R(g); then K_0, T_1(R). n does not depend on g." + ../ym4d-existence/EXISTENCE.md: "every hypercubic torus of side T ≥ T_1(R)" · DEF · vol: lower bounds only: 'every hypercubic torus of side T ≥ T_1(R)'
- **R_g** · live · t3 · R(g) := ⌈m_e^{-1}log(32C_e/a_-)⌉ (grows like log(1/g)) · ../ym4d-existence/EXISTENCE.md: "R = R(g) := ⌈m_e^{-1}log(32C_e/a_-)⌉" · DEF · vol: n/a
- **V_LF** · live · t3 · 𝒱_K^{LF} := Σ_{k<K: T_{k+1}≥W}N_{k+1}c̄_0^{sea}(g_k) (the vacuum c-number) · RLARGE.md: "the only K-divergent quantity (HIST (P3))" · DEF (by design K- and volume-divergent; extracted, not bounded) · growth: K (RLARGE.md: "the only K-divergent quantity (HIST (P3))"); T (HW.md: "𝒱_K^{LF}/|T| is not O(e^{-a'/g_K²})") · vol: extensive in |T| and divergent in K BY DESIGN
- **dbeta** · live · t3 · δβ_k (one coupling shift per level) and c̄_0^{sea} · RLARGE.md: "field-independent infinite-volume numbers" · OPEN (RLF-0) · growth: unstated-T (RLARGE.md: "no source proves that the sea average is torus-independent above the wrap levels (U5)") · vol: UNSTATED: 'infinite-volume numbers' asserted, torus-independence above the wrap levels unproven (K9/U5)
- **eff_seq** · live · t3 · the chain's own effective coupling sequence (g_k) · RLARGE.md: "But F-flow at n = k + 1 consumes (RLF-δ)_j for j ≤ k (u_{k+1} contains δβ_k)" · OPEN (node A5) · vol: infinite-volume β by definition (FLOW Def F-g)
- **eps_sharp** · live · t3 · ε_♯ := 6400^{n_♯}(C_ℓe^{38417c + aR}e^{-a/g_K²})^{n_♯+1}e^{38416c} · HW.md: "ε_♯ := 6400^{n_♯}(C_ℓe^{38417c + aR}e^{-a/g_K²})^{n_♯+1}e^{38416c}" · DEF · vol: → 0 as g_K → 0 at fixed n_♯
- **kernel_seq** · live · t3 · the kernel couplings (u_i) of W (parameters of the chain) · RLARGE.md: "**The kernel couplings u_i are parameters of W**" · DEF · vol: n/a
- **g0** · live · t4 · g_0 = Theorem RLF v3's ceiling on the coarsest coupling (g_K ≤ g_0) — THE SINK · RLARGE.md: "own effective coupling sequence (g_k) with g_K ≤ g_0 obeying (F_R) (§0)" + RLARGE.md: "independent of g, K, T and the history" · target (OPEN) · vol: claimed independent of g, K, T (RLF v3 statement) · note: g_0 names three objects (REVIEW55_HWPLD F1): the stage-0 coupling (SF/FLOW), this threshold on g_K, and FLOW's bare coupling g_0(ε, g)
- **A_inout** · off · t1 · A_in, A_out, c_K (LOC's constants used by CURV1) · PROOF.md: "D_L(θ) := the least D with 24A_out n(D_g)e^{-m_1D/2} ≤ θ/2" · PROVEN-HERE (LOC) / not covered by CI-bg · vol: n/a
- **C_flat_i** · off · t1 · C_♭^{(i)} ((H-C)'s class-wide Lipschitz constant of Hess E_i^br, per level) · PROOF.md: "C_♭^{(i+1)} ≤ Z_colZ_row²·C_♭^{(i)} + (1 + Z_col)(1 + Z_row)²·C_soft" · per-level route; (H-C) not discharged · growth: K (PROOF.md: "absolute-value recursion compounds by Z_colZ_row² ≈ 1.3·10³ per level") · vol: per level
- **C_theta** · off · t1 · C_θ (CURV1 second-order constant, level 0) · PROOF.md: "C_θ := 288𝔠_∞³C_♭ + 792𝔠_∞ℓ_θ + 24𝔠_∞c_π + 288A_incoth⁴(m_1/2)ℓ_θ + 53(48𝔠_∞ + 1)² + 1296𝔠_∞ℓ_θ" · PROVEN-HERE (Lemma CURV1) · vol: level 0/1; level-uniform form ⇐ BFT-4 (REVIEW_S22) · note: no consumer on the BFT route RLARGE v3 adopts; consumed by the per-level route (NAH-unif) and SF l.68-69 at level j; FLOW's C_θ (heat-trace) is a different object
- **C_theta_i** · off · t1 · C_θ^{(i)} (per-level CURV1 constants) · PROOF.md: "C_θ^{(i)} ≥ Π_{j≤i}(4κ_{j-1}𝔠_∞^{(j)}) grows geometrically" · per-level route (CURV-F2′) · growth: K (PROOF.md: "C_θ^{(i)} ≥ Π_{j≤i}(4κ_{j-1}𝔠_∞^{(j)}) grows geometrically") · vol: per level
- **K_bar** · off · t1 · K̄ := sup_i K_p^{(i)}(Z_i) < 1 ((H-K), measured ≈ 0.11-0.13, uncertified) · PROOF.md: "(K_p^♯ < 1 uniformly, measured, not certified)" · measured, not certified · growth: unstated-T (PROOF.md: "The exact-input LP values grow with T (row 252: 0.062 at T = 4, 0.090 at T = 6;") · vol: grows with T toward the smooth value ≈ 1/9 (measured)
- **N1_15** · off · t1 · Theorem N1-15 constant 𝔚 + 13.5·𝔖 (N3 of D³E_k^br(1), trivial background) · NORMS.md: "N3(D³E_k^br(1)) ≤ 𝔚 + 13.5·𝔖, uniformly in k." · PROVEN given (N-Q), (N-loc); T-uniform per TUNIF TU-6 (REVIEW55_TUNIF CONFIRMED, conditional on NQ-1) · vol: k-uniform; T-uniform via TU-6 (CONFIRMED w/ repairs); NL-4 route ∝ T^{d+2}; no live consumer (NQ_DEF §D5.4, REVIEW55_NORMS F8)
- **PLD_xS** · off · t1 · PLD's allowance through x(S) (§18.5 (b′) 'depth-free Δ_sh' REFUTED; ≥ 256/81 per level) · REVIEW55_HWPLD.md: "compounds geometrically; §18.11's UPGRADE is a downgrade" · REFUTED as depth-free (REVIEW55_HWPLD F9) · growth: K (REVIEW55_HWPLD.md: "compounds geometrically; §18.11's UPGRADE is a downgrade") · vol: per level
- **SDP_column** · off · t1 · (SDP) by column induction inside ∫W·1_𝔥 (LOOP-const; ×81 per level) — a route NOT taken · RLARGE.md: "the bound) shows it is not obtainable by column induction inside ∫W·1_𝔥 (LF-count at n = 1, ×81 per level)." · PROVEN-HERE as arithmetic about the bound (LOOP-const) · growth: K (RLARGE.md: "the bound) shows it is not obtainable by column induction inside ∫W·1_𝔥 (LF-count at n = 1, ×81 per level).") · vol: per level
- **a_RS** · off · t1 · a_RS := min{a_η, κε_1²/(256N)} (frozen v1) · RLARGE.md: "a_RS := min{a_η, κε_1²/(256N)}" · frozen v1; no live consumer (REVIEW55_ARS F01; [S25-fix 4]) · vol: n/a
- **c_RS_joint** · off · t1 · c_RS = 81 ⇐ (PLD-q)_k (RS-joint; the other c_RS) · RLARGE.md: "RS-joint's c_RS = 81 ⇐ (PLD-q)_k" · CONDITIONAL; not consumed · vol: n/a
- **ell_theta** · off · t1 · ℓ_θ, D_g(θ), D_L(θ) (CURV1 localisation lengths) · PROOF.md: "ℓ_θ := 2⌈(D_g + D_L + r_1 + 3L + 4)/L⌉ + 3 (coarse units)" · DEF · vol: 'T ≥ ℓ_θ + 1' (lower bound)
- **q0_NQ** · off · t1 · 𝔮₀ = 1 + d(L+1)/(2L) = 11/3 (Theorem NQ-1) · REVIEW55_NORMS.md: "Theorem NQ-1: ‖Q^{(m)}‖_{∞→∞} ≤ L^m + (d(L²−1)/(2L))(L^m−1)/(L−1) ≤ 𝔮₀L^m, 𝔮₀ = 1 + d(L+1)/(2L) = 11/3" · PROVEN (CONFIRMED REVIEW55_NORMS E1) · vol: uniform in j, k, T (any m consecutive levels)
- **eps_theta** · off · t2 · ε_θ := min{ε_br, α_*/(12ℓ_θ), r_♭/(18ℓ_θ), 1/(60ℓ_θ), 1/(80(48𝔠_∞ + 1))} · PROOF.md: "ε_θ := min{ε_br, α_*/(12ℓ_θ), r_♭/(18ℓ_θ), 1/(60ℓ_θ), 1/(80(48𝔠_∞ + 1))}" · PROVEN-HERE (Lemma CURV1) · vol: 'T ≥ ℓ_θ + 1' (lower bound)
- **eps_unif** · off · t2 · ε_unif (NAH-unif's depth-independent threshold) · PROOF.md: "ε_unif := inf_i min{η_*, ε_H^{(i)}," · GAP as stated (S21-5); per-level route · growth: K (PROOF.md: "ε_unif = O(1/k)") · vol: per level
- **eta_1** · off · t2 · η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d(L))} (Lemma RS (R3)'s quadratic threshold) · RLARGE.md: "η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d(L))}" · DEF; no live consumer (REVIEW55_ARS F01) · vol: n/a
- **tau_sharp** · off · t2 · τ^♯ = 1.10·10⁻¹⁴ (stage-0 threshold ⇐ (GF-B^𝔥)) · SF.md: "1.10·10⁻¹⁴ ⇐ (GF-B^𝔥)" · CONDITIONAL ⇐ (GF-B^𝔥) [OPEN] · vol: as τ_c · note: the ε_1 lever (moves ε_1 ≈ 16 orders); not in force
- **NL4** · superseded · t1 · Corollary NL-4 constant (N1-15 at fixed coarse side T, ∝ T^{d+2}) · NLOC.md: "with a constant that grows like T^{d+2}" · PROVEN (given J1-J4); superseded by TU-6 · growth: Tk (NLOC.md: "with a constant that grows like T^{d+2}") · vol: fixed coarse side only · note: T here is the level-k coarse side: on a fixed physical torus T_k = T·L^{K-1-k} is unbounded in K (PLAN_S26 §6)
- **S_T** · superseded · t1 · GREENT's cell sum 𝒮_T (= 2.514·10⁸ at T = T_0; O(log T)) · GREENT.md: "Corollary NL-4's T^d replaced by a cell sum of size O(log T), with the constant exhibited." · COMPUTED upper sum (REVIEW55_LEAD r55l-F9: not a proof); superseded by TU-4/TU-5 · growth: T (GREENT.md: "unconditional at **fixed** T and **not** uniform in T") · vol: grows like log T
- **a_sharp_v1** · superseded · t1 · a_♯ / c_RS = 5⁴ / n_♯ := ⌊4/(a_♯β_-)⌋ (v1-v2 pricing) · RLARGE.md: "a_♯, c_RS = 5⁴ and n_♯ := ⌊4/(a_♯β_-)⌋ are superseded" · superseded by §3.5, §5.2 · vol: n/a
- **U_M_pkg** · unplaced · t1 · M = M(L, κ_±) (LINEAR_PACKAGE Theorem 4.2′'s package constant) · LINEAR_PACKAGE.md: "bounded there by M = M(L, κ_±)" · DAG-F3 · vol: 'uniformly in k ≥ 1, T' · note: M also names other objects (M̄_c, Lemma PM's matrix M, Theorem CE's M-units); its consumers ((GAP-Z), TU-4, lane A's W0/GU/LIN0) are inside BFT's proof route, not modelled here
- **U_Qstr** · unplaced · t1 · Q_str (two operators: NORMS 81 entries vs LINEAR_PACKAGE 135) · REVIEW55_NORMS.md: "NQ_DEF: Q_str is two operators (81 vs 135 entries; slice identity off by 108)" · DAG-F3 · vol: n/a · note: consumed only inside NORMS/N1-15 (off-route)
- **U_eps1_FLOW** · unplaced · t1 · ε_1 at FLOW l.1927 (disc radius) and l.2834 (|q_αF| ≤ ε_1) · FLOW.md: "On a disc |φ| ≤ ε_1 (fixed)" · DAG-F3 · vol: n/a · note: one or two objects: REVIEW55_CONST K9 left the count ≥ 5, possibly 6, NOT-VERIFIED; neither is RLARGE's χ_Q cut
- **U_eta_COF** · unplaced · t1 · η in C_fun's O((k−1)η²) (BFT_B's row size) · REVIEW55_BFTB.md: "row size π_l(R^B_l) ≤ 2C_bchκ_+L²η² is uniform in l" · DAG-F3 · vol: n/a · note: whether η is BFT's fixed curvature size ε (≤ ε_0, fixed: KF-F2) or a g_k-scale quantity (KF-F3) is Step 4's question; not decidable from the strings I read
- **U_m_norm** · unplaced · t1 · m (𝔐's exponential weight, written bare) vs m_0 (BFT-3/BFT-4) · REVIEW_S22.md: "exponential weights e^{±m d} are in level-k ancestor distance" · DAG-F3 · vol: n/a · note: THETAW J5 / REVIEW55_TUNIF W13: 'flagged, not decided' whether one constant or three
- **U_theta_w** · unplaced · t1 · θ_w as written in REVIEW_S22's BFT (one weight for ≥ 3 jobs) · REVIEW_S22.md: "level-j curvature and soft-fluctuation components are weighted by L^{θ_w(k-j)}" · DAG-F3 · vol: n/a · note: candidates: θ_w^c, θ_w^r, θ (source weight ω_l), θ_A — the decoupling is CONFIRMED faithful (REVIEW55_TUNIF W2), so the placed nodes are the decoupled ones; the single θ_w is not placed

## Appendix B — every edge (src → dst [kind] file: "string"; generated from `checks/dag55_2_graph.py`)

Direction: src must be fixed before dst. Kinds: def / le / order / req / implicit / fixedpoint; (absorbs) marks an edge along which a growth does not propagate, with its absorbing string.

0. beta0p → beta_m [def] FLOW.md: "Fix FIRST β_- := β_0'/2 and R := 2R_0"
1. R0 → R [def] FLOW.md: "Fix FIRST β_- := β_0'/2 and R := 2R_0"
2. beta_m → C_rho [order] FLOW.md: "then the layer-1 constants C_ρ = C_ρ(β_0'/2, 2R_0) are fixed"
3. R → C_rho [order] FLOW.md: "then the layer-1 constants C_ρ = C_ρ(β_0'/2, 2R_0) are fixed"
4. C_rho → gamma [def] FLOW.md: "then γ := min{γ_0, (β_0'log L/(2C_ρ))^{1/2}}"
5. gamma0 → gamma [def] FLOW.md: "then γ := min{γ_0, (β_0'log L/(2C_ρ))^{1/2}}"
6. beta0p → gamma [def] FLOW.md: "then γ := min{γ_0, (β_0'log L/(2C_ρ))^{1/2}}"
7. gamma → beta_p [def] FLOW.md: "β_± := β_0' ± C_ργ²/log L (so β_0'/2 ≤ β_- ≤ β_0' ≤ β_+ ≤ 3β_0'/2)"
8. C_rho → beta_p [def] FLOW.md: "β_± := β_0' ± C_ργ²/log L (so β_0'/2 ≤ β_- ≤ β_0' ≤ β_+ ≤ 3β_0'/2)"
9. gamma → g1_FLOW [def] FLOW.md: "g_1 := (γ^{-2} + R)^{-1/2}: for every K ≥ 1 and g ∈ (0, g_1]"
10. R → g1_FLOW [def] FLOW.md: "g_1 := (γ^{-2} + R)^{-1/2}: for every K ≥ 1 and g ∈ (0, g_1]"
11. kernel_seq → stage_consts [def] RLARGE.md: "stage-k constants also use the kernel coupling g_{k+1} of K_{k+1} through CL^J" (absorbs: RLARGE.md: "bounded using only the a-priori bracket 1/g_{k+1}² ≤ 1/g_k² + R and g_{k+1}² ≤ 1/(2R)") — Option A (U4): an integration choice, not a theorem; it bounds the stage constants by the bracket (R) alone
12. stage_consts → dbeta [def] RLARGE.md: "Derived at level k from data on levels [0, k] only" + RLARGE.md: "itself an output of stage k (through δβ_k)"
13. dbeta → eff_seq [def] RLARGE.md: "But F-flow at n = k + 1 consumes (RLF-δ)_j for j ≤ k (u_{k+1} contains δβ_k)"
14. eff_seq → kernel_seq [fixedpoint] RLARGE.md: "The fixed point is consistent only if the kernel coupling sequence is fixed first" — FI-1 / U4: Option A fixes the kernel sequence first and bounds stage constants by the a-priori bracket; Option B; 'Neither option is a theorem here.'
15. R → stage_consts [le] RLARGE.md: "bounded using only the a-priori bracket 1/g_{k+1}² ≤ 1/g_k² + R and g_{k+1}² ≤ 1/(2R)" — Option A's a-priori bracket: the constants' g_{k+1}-dependence is bounded by R alone
16. G_inf → sf_chain [def] SF.md: "Scaling: ζ ≈ 1/(4032c′_gX_∞G_∞²), so every threshold of the chain is ∝ G_∞^{-2}"
17. sf_chain → tau_c [def] SF.md: "τ_c := s_0/(√NC_0) = 4.34·10⁻⁵⁹" + SF.md: "choose ζ (s5 F2), then s_0 = ζ/X_∞ and τ_c = s_0/(√NC_0), then ε_1 ≤ τ_c and RLARGE's stage-0 thresholds ≤ τ_c (TH-ch)"
18. tau_c → a_p_ac [def] SF.md: "a_p = τ_c²/(2N) = 3.14·10⁻¹¹⁸"
19. a_p_ac → eps_bg [def] SF.md: "where ε_bg^{(TH-bg)} is the largest ε_bg allowed by the corrected (TH-bg) ε_bg²(n_1/2 + 1.03κ_sn_K) ≤ ½min{a_p, a_c}"
20. tau_c → eps1 [le] SF.md: "(TH-ch′) ε_1 ≤ min{τ_c, τ_c/(2C_bg), ε_bg^{(TH-bg)}/C_bg}"
21. C_bg → eps1 [le] SF.md: "(TH-ch′) ε_1 ≤ min{τ_c, τ_c/(2C_bg), ε_bg^{(TH-bg)}/C_bg}"
22. eps_bg → eps1 [le] SF.md: "(TH-ch′) ε_1 ≤ min{τ_c, τ_c/(2C_bg), ε_bg^{(TH-bg)}/C_bg}"
23. tau_c → eps_loc [le] SF.md: "with every RLARGE stage-0 small-field threshold (incl. ε_*) ≤ τ_c"
24. eps1 → eps_loc [def] RLARGE.md: "ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}}"
25. b_1 → eps_loc [def] RLARGE.md: "ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}}"
26. kappa_RL → b_1 [def] RLARGE.md: "b_1 := n_P + 12κ(1 + A_d(L))²"
27. A_d → b_1 [def] RLARGE.md: "b_1 := n_P + 12κ(1 + A_d(L))²"
28. eps1 → eta_q [def] HIST.md: "η_q := min{ ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d }"
29. delta_0 → eta_q [def] HIST.md: "η_q := min{ ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d }"
30. A_d → eta_q [def] HIST.md: "η_q := min{ ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d }"
31. eta_q → eps_loc [le] RLARGE.md: "ε_loc/2 ≥ (16N + 3)A_dη_q" — (TC) for the collar extension; compatibility with CL's own ε_loc unchecked (U3)
32. eps1 → a_bad [def] RLARGE.md: "a_bad := c_pr·min{ε_1², t_pr²}"
33. c_pr → a_bad [def] RLARGE.md: "a_bad := c_pr·min{ε_1², t_pr²}"
34. t_pr → a_bad [def] RLARGE.md: "a_bad := c_pr·min{ε_1², t_pr²}"
35. c_flat → c_pr [def] RLARGE.md: "via (REG-min) (primary), c_pr = c_♭/C′², t_pr = C′τ_♭"
36. C_prime → c_pr [def] RLARGE.md: "via (REG-min) (primary), c_pr = c_♭/C′², t_pr = C′τ_♭"
37. C_prime → t_pr [def] RLARGE.md: "via (REG-min) (primary), c_pr = c_♭/C′², t_pr = C′τ_♭"
38. a_bad → a [def] RLARGE.md: "a := min{θa_bad, a_A}"
39. theta → a [def] RLARGE.md: "a := min{θa_bad, a_A}"
40. a_A → a [def] RLARGE.md: "a := min{θa_bad, a_A}"
41. a_A → theta [le] RLARGE.md: "If a_A < θa_bad, θ is lowered to a_A/a_bad and nothing else changes"
42. a_bad → theta [le] RLARGE.md: "If a_A < θa_bad, θ is lowered to a_A/a_bad and nothing else changes"
43. a_ret → theta [le] PLD.md: "Without (EG), θ ≤ a_ret/a_bad ≈ 8·10⁻⁷" — PLD [RPLD4-fix K-1]: K12 reduced to (EG); not adopted in RLARGE (U1)
44. theta_cb → theta [le] RLARGE.md: "a_D := min{a_bad, a_cb}, with θ ∈ (0, 1/(96·82))" — collar-bad family only (row 10f)
45. theta → g0 [le] RLARGE.md: "max{6θ, 24θ}(1 + 2Rg_K²) < 1" — CAP-1 read as a ceiling on g_K once θ is fixed
46. R → g0 [le] RLARGE.md: "(H-w′) ⇐ (F_R) [g_K² ≤ 1/(2R)]"
47. theta → c_sf [def] RLARGE.md: "c_sf at rate 24θ(1 + 2Rg_K²) < 1 on defect-free columns"
48. c_sf → C_fc [def] RLARGE.md: "C_fc = c_sf + 81C_Ae^{θa_bad R}, the same constant at every level"
49. C_A → C_fc [def] RLARGE.md: "C_fc = c_sf + 81C_Ae^{θa_bad R}, the same constant at every level"
50. theta → C_fc [def] RLARGE.md: "C_fc = c_sf + 81C_Ae^{θa_bad R}, the same constant at every level"
51. a_bad → C_fc [def] RLARGE.md: "C_fc = c_sf + 81C_Ae^{θa_bad R}, the same constant at every level"
52. R → C_fc [def] RLARGE.md: "C_fc = c_sf + 81C_Ae^{θa_bad R}, the same constant at every level"
53. theta → lambda_star [def] RLARGE.md: "λ_* = 6θ(1 + 2Rg_K²)"
54. R → lambda_star [def] RLARGE.md: "λ_* = 6θ(1 + 2Rg_K²)" — g_K enters only through the a-priori g_K² ≤ 1/(2R)
55. lambda_star → C_ell [def] RLARGE.md: "C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc"
56. n_int → C_ell [def] RLARGE.md: "C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc"
57. C_fc → C_ell [def] RLARGE.md: "C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc"
58. C_ell → C_ellp [def] HW.md: "§32 l.1690's PRIMED C_ℓ (with C_fc′ = 2C_fc e^{c_f}) is the one REL-boot's r and B_0 need"
59. c_f → C_ellp [def] HW.md: "§32 l.1690's PRIMED C_ℓ (with C_fc′ = 2C_fc e^{c_f}) is the one REL-boot's r and B_0 need"
60. c_A → c_plus [def] HW.md: "c_+ = c_A + c_U (c_U := 2ε_2 ≤ 1)"
61. c_U → c_plus [def] HW.md: "c_+ = c_A + c_U (c_U := 2ε_2 ≤ 1)"
62. c_A → c_U [order] HW.md: "node A's C_fc, C_A, a_A, c_A → c_U := 1 (any value in (0, 1]) → b_n, b_D, c_att, C_ℓ →" — c_U is FIXED at its input value 1 (output 2ε_2 ≤ 1 fed back only as a consistency check): the order statement breaks the c_U ↔ g_K loop
63. c_plus → c_f [def] HW.md: "c_f := 531441·c_+"
64. c_plus → b_n [def] HW.md: "b_n = C_sh·81·h_n·c_+ + h′_n·c_U"
65. c_U → b_n [def] HW.md: "b_n = C_sh·81·h_n·c_+ + h′_n·c_U"
66. c_plus → b_D [def] HW.md: "b_D = h_D·(C_sh·81·c_+ + c_U)"
67. c_LI → B_0 [def] HW.md: "a, C_ℓ, c (from the moments and (LI)) → B_0 := B_1 + c + 1"
68. c_f → B_0 [def] RLARGE.md: "B_0 = c_LI + c_f + 164ε_♯" — the 164ε_♯ term is replaced by its bound 1 (HW order); ε_♯ ≤ 1/164 is imposed later on g_K
69. B_0 → c_B [def] RLARGE.md: "38416B_0/log L"
70. c_B → n_H [def] RLARGE.md: "n_H := ⌊(4 + c_B)/(aβ_-)⌋"
71. a → n_H [def] RLARGE.md: "n_H := ⌊(4 + c_B)/(aβ_-)⌋"
72. beta_m → n_H [def] RLARGE.md: "n_H := ⌊(4 + c_B)/(aβ_-)⌋"
73. n_H → n_sharp [le] RLARGE.md: "n_♯ ≥ max{n^J_*, n_H}"
74. n_J_star → n_sharp [le] RLARGE.md: "n_♯ ≥ max{n^J_*, n_H}"
75. b_D → n_sharp [le] HW.md: "n_♯ ≥ max{n_H(a, B_0), b_D/(aβ_-log L)}"
76. a → n_sharp [le] HW.md: "n_♯ ≥ max{n_H(a, B_0), b_D/(aβ_-log L)}"
77. beta_m → n_sharp [le] HW.md: "n_♯ ≥ max{n_H(a, B_0), b_D/(aβ_-log L)}"
78. n_sharp → W [def] RLARGE.md: "W := 2n_♯ + 5"
79. W → SF_last [req] RLARGE.md: "**now a many-level item** (wrap levels, §5.4)"
80. n_sharp → eps_sharp [def] HW.md: "ε_♯ := 6400^{n_♯}(C_ℓe^{38417c + aR}e^{-a/g_K²})^{n_♯+1}e^{38416c}"
81. C_ell → eps_sharp [def] HW.md: "ε_♯ := 6400^{n_♯}(C_ℓe^{38417c + aR}e^{-a/g_K²})^{n_♯+1}e^{38416c}"
82. a → eps_sharp [def] HW.md: "ε_♯ := 6400^{n_♯}(C_ℓe^{38417c + aR}e^{-a/g_K²})^{n_♯+1}e^{38416c}"
83. R → eps_sharp [def] HW.md: "ε_♯ := 6400^{n_♯}(C_ℓe^{38417c + aR}e^{-a/g_K²})^{n_♯+1}e^{38416c}"
84. eps_sharp → g0 [le] HW.md: "→ n_H → n_♯ ≥ n_H → g_0(n_♯) with ε_♯ ≤ min{½, 1/164}"
85. n_sharp → C_H [def] RLARGE.md: "C_H := 2·6400^{n_♯}(C_ℓe^{aR}e^{38417B_0})^{n_♯+1}/(1 - L^{-γ_H})"
86. C_ell → C_H [def] RLARGE.md: "C_H := 2·6400^{n_♯}(C_ℓe^{aR}e^{38417B_0})^{n_♯+1}/(1 - L^{-γ_H})"
87. B_0 → C_H [def] RLARGE.md: "C_H := 2·6400^{n_♯}(C_ℓe^{aR}e^{38417B_0})^{n_♯+1}/(1 - L^{-γ_H})"
88. C_ell → g0 [le] RLARGE.md: "6400C_ℓe^{aR}e^{38417B_0}e^{-a/g_K²} ≤ ½" — HIST-sum's smallness condition
89. B_0 → g0 [le] RLARGE.md: "6400C_ℓe^{aR}e^{38417B_0}e^{-a/g_K²} ≤ ½"
90. a → g0 [le] RLARGE.md: "6400C_ℓe^{aR}e^{38417B_0}e^{-a/g_K²} ≤ ½"
91. C_ellp → g0 [le] HW.md: "n_♯ ≥ max{n_H(a, B_0), b_D/(aβ_-log L)} → g_0 with g_K² < g²_CRC, (S1), (S2), and REL-boot's r ≤ ½, 164ε′ ≤ 1" — REL-boot's r ≤ ½ uses the primed C_ℓ′
92. a → g2_CRC [def] HW.md: "g_K² < g²_CRC := a/(b_n + aR + log(12800C_ℓ))"
93. b_n → g2_CRC [def] HW.md: "g_K² < g²_CRC := a/(b_n + aR + log(12800C_ℓ))"
94. C_ell → g2_CRC [def] HW.md: "g_K² < g²_CRC := a/(b_n + aR + log(12800C_ℓ))"
95. R → g2_CRC [def] HW.md: "g_K² < g²_CRC := a/(b_n + aR + log(12800C_ℓ))"
96. g2_CRC → g0 [le] HW.md: "n_♯ ≥ max{n_H(a, B_0), b_D/(aβ_-log L)} → g_0 with g_K² < g²_CRC, (S1), (S2), and REL-boot's r ≤ ½, 164ε′ ≤ 1"
97. n_sharp → g0 [order] HW.md: "n_♯ ≥ max{n_H(a, B_0), b_D/(aβ_-log L)} → g_0 with g_K² < g²_CRC, (S1), (S2), and REL-boot's r ≤ ½, 164ε′ ≤ 1"
98. a_A → g0 [le] HW.md: "holds once a_A/g_K² ≥ a/g_K² exceeds log(2Δ_ρ²C_A) + a_AR + c_+c_att" — (S1)
99. C_A → g0 [le] HW.md: "holds once a_A/g_K² ≥ a/g_K² exceeds log(2Δ_ρ²C_A) + a_AR + c_+c_att" — (S1)
100. c_plus → g0 [le] HW.md: "holds once a_A/g_K² ≥ a/g_K² exceeds log(2Δ_ρ²C_A) + a_AR + c_+c_att" — (S1)
101. c_att → g0 [le] HW.md: "holds once a_A/g_K² ≥ a/g_K² exceeds log(2Δ_ρ²C_A) + a_AR + c_+c_att" — (S1)
102. a → g0 [le] RLARGE.md: "g_K² < a/(8(3κ_0 + 3)) and C_ℓe^{-a/(4g_K²)} ≤ c(κ_0)" — (P5): composition with Theorem CE
103. kappa0_CE → g0 [le] RLARGE.md: "g_K² < a/(8(3κ_0 + 3)) and C_ℓe^{-a/(4g_K²)} ≤ c(κ_0)"
104. C_ell → g0 [le] RLARGE.md: "g_K² < a/(8(3κ_0 + 3)) and C_ℓe^{-a/(4g_K²)} ≤ c(κ_0)"
105. SF_last → g0 [req] RLARGE.md: "applying CE needs"
106. eps_loc → a_cb [def] RLARGE.md: "κε_loc²/(64N), c_pr·min{η_q², t_pr²}}"
107. eta_q → a_cb [def] RLARGE.md: "κε_loc²/(64N), c_pr·min{η_q², t_pr²}}"
108. c_pr → a_cb [def] RLARGE.md: "κε_loc²/(64N), c_pr·min{η_q², t_pr²}}"
109. t_pr → a_cb [def] RLARGE.md: "κε_loc²/(64N), c_pr·min{η_q², t_pr²}}"
110. eps1 → a_ret [def] PLD.md: "a_ret := min{κε_1²/(2048N), 49η_q²/(1024σ_fl²), κε_loc²/(64N)}" — candidate formula, conditional on (SC)_k; U1 open
111. eta_q → a_ret [def] PLD.md: "a_ret := min{κε_1²/(2048N), 49η_q²/(1024σ_fl²), κε_loc²/(64N)}"
112. eps_loc → a_ret [def] PLD.md: "a_ret := min{κε_1²/(2048N), 49η_q²/(1024σ_fl²), κε_loc²/(64N)}"
113. sigma_fl → a_ret [def] PLD.md: "a_ret := min{κε_1²/(2048N), 49η_q²/(1024σ_fl²), κε_loc²/(64N)}"
114. a_ret → gamma0 [le] RLARGE.md: "The γ_0 needed for Cg^{-p}e^{-a_ret/g²} ≤ g⁶"
115. C_p_RLF0 → gamma0 [le] RLARGE.md: "The γ_0 needed for Cg^{-p}e^{-a_ret/g²} ≤ g⁶"
116. a → a_prime [le] RLARGE.md: "(any a′ < a, and a′ ≤ the (NA-∅) exponent)"
117. NA_empty → a_prime [le] RLARGE.md: "(any a′ < a, and a′ ≤ the (NA-∅) exponent)"
118. n_sharp → a_A [implicit] HW.md: "R_{S,E} := ∩_j{every *-component of (D_j ∪ E^{(j)}) ∩ S^{(j)} has ≤ n_♯ cubes}" + HW.md: "C_A, c_A independent of g, K, T, k and the law" — (SDP)^A must hold for every μ ∈ ℛ_𝔥^↑ ∪ {μ_R(𝔥)}; these laws are defined with n_♯; HW §13.2's order puts (a, C_ℓ, c) BEFORE n_♯; n_♯-uniformity is not stated
119. n_sharp → C_A [implicit] HW.md: "R_{S,E} := ∩_j{every *-component of (D_j ∪ E^{(j)}) ∩ S^{(j)} has ≤ n_♯ cubes}" + HW.md: "C_A, c_A independent of g, K, T, k and the law" — (SDP)^A must hold for every μ ∈ ℛ_𝔥^↑ ∪ {μ_R(𝔥)}; these laws are defined with n_♯; HW §13.2's order puts (a, C_ℓ, c) BEFORE n_♯; n_♯-uniformity is not stated
120. n_sharp → c_A [implicit] HW.md: "R_{S,E} := ∩_j{every *-component of (D_j ∪ E^{(j)}) ∩ S^{(j)} has ≤ n_♯ cubes}" + HW.md: "C_A, c_A independent of g, K, T, k and the law" — (SDP)^A must hold for every μ ∈ ℛ_𝔥^↑ ∪ {μ_R(𝔥)}; these laws are defined with n_♯; HW §13.2's order puts (a, C_ℓ, c) BEFORE n_♯; n_♯-uniformity is not stated
121. rstar → C_Delta [def] PROOF.md: "so ε_* is explicit only up to C_Δ = 2S_*n_1/r_*"
122. n_1 → C_Delta [def] PROOF.md: "so ε_* is explicit only up to C_Δ = 2S_*n_1/r_*"
123. kappa0 → gap0 [def] PROOF.md: "Off κ_0 = 1 use (1 - e_0 - |κ_0 - 1|qk_0)/k_0 in"
124. gap0 → m_N5 [le] PROOF.md: "m_cov^{(0)} the largest m with 𝔇_0(m) ≤ γ_0/2"
125. rstar → alpha_star [def] PROOF.md: "α_* := min{r_*, (γ_0/2 - 𝔇_0(m))/(C_Δe^{mr_1})}"
126. gap0 → alpha_star [def] PROOF.md: "α_* := min{r_*, (γ_0/2 - 𝔇_0(m))/(C_Δe^{mr_1})}"
127. m_N5 → alpha_star [def] PROOF.md: "α_* := min{r_*, (γ_0/2 - 𝔇_0(m))/(C_Δe^{mr_1})}"
128. C_Delta → alpha_star [def] PROOF.md: "α_* := min{r_*, (γ_0/2 - 𝔇_0(m))/(C_Δe^{mr_1})}"
129. gap0 → gamma_prime [def] PROOF.md: "γ' := γ_0 - C_Δα_* (≥ γ_0/2)"
130. alpha_star → gamma_prime [def] PROOF.md: "γ' := γ_0 - C_Δα_* (≥ γ_0/2)"
131. C_Delta → gamma_prime [def] PROOF.md: "γ' := γ_0 - C_Δα_* (≥ γ_0/2)"
132. alpha_star → S_prime [def] PROOF.md: "S'_m := N_m(|Õ_0|) + e^{mr_1}C_Δα_*"
133. m_N5 → S_prime [def] PROOF.md: "S'_m := N_m(|Õ_0|) + e^{mr_1}C_Δα_*"
134. S_prime → R_star_N5 [def] PROOF.md: "ε_R := (8S'_m/γ')coth⁴(a/4)e^{-aRL/2}"
135. gamma_prime → R_star_N5 [def] PROOF.md: "ε_R := (8S'_m/γ')coth⁴(a/4)e^{-aRL/2}"
136. m_N5 → R_star_N5 [def] PROOF.md: "ε_R := (8S'_m/γ')coth⁴(a/4)e^{-aRL/2}"
137. R_star_N5 → T0_N5 [def] PROOF.md: "T_0 := 4R_* + 6"
138. alpha_star → eps_star_N5 [def] PROOF.md: "ε_* := α_*/(10p_L(4R_* + 5)L)"
139. R_star_N5 → eps_star_N5 [def] PROOF.md: "ε_* := α_*/(10p_L(4R_* + 5)L)"
140. p_L → eps_star_N5 [def] PROOF.md: "ε_* := α_*/(10p_L(4R_* + 5)L)"
141. gamma_prime → c_inf [def] PROOF.md: "𝔠_∞ := min{8coth⁴(a/2), 81((N² - 1)n_Ω)^{1/2}}/(γ'(1 - ε_R)) + ν_w + C_Δα_*"
142. R_star_N5 → c_inf [def] PROOF.md: "𝔠_∞ := min{8coth⁴(a/2), 81((N² - 1)n_Ω)^{1/2}}/(γ'(1 - ε_R)) + ν_w + C_Δα_*"
143. alpha_star → c_inf [def] PROOF.md: "𝔠_∞ := min{8coth⁴(a/2), 81((N² - 1)n_Ω)^{1/2}}/(γ'(1 - ε_R)) + ν_w + C_Δα_*"
144. rstar → r_flat [le] PROOF.md: "We may and do take r_♭ ≤ r_*, and C_Δ ≤ C_♭."
145. r_flat → C_flat_PR [def] PROOF.md: "C_♭ := 4S_♭n_1/r_♭"
146. n_1 → C_flat_PR [def] PROOF.md: "C_♭ := 4S_♭n_1/r_♭"
147. eps_star_N5 → eps_br [def] PROOF.md: "ε_br := min{ ε_*/(1 + 36p_L𝔠_∞), 1/(24𝔠_∞²C_♭), r_♭/(24𝔠_∞), r_♭/(18(3L - 1)), 1/(1728𝔠_∞K_FP) }"
148. c_inf → eps_br [def] PROOF.md: "ε_br := min{ ε_*/(1 + 36p_L𝔠_∞), 1/(24𝔠_∞²C_♭), r_♭/(24𝔠_∞), r_♭/(18(3L - 1)), 1/(1728𝔠_∞K_FP) }"
149. C_flat_PR → eps_br [def] PROOF.md: "ε_br := min{ ε_*/(1 + 36p_L𝔠_∞), 1/(24𝔠_∞²C_♭), r_♭/(24𝔠_∞), r_♭/(18(3L - 1)), 1/(1728𝔠_∞K_FP) }"
150. r_flat → eps_br [def] PROOF.md: "ε_br := min{ ε_*/(1 + 36p_L𝔠_∞), 1/(24𝔠_∞²C_♭), r_♭/(24𝔠_∞), r_♭/(18(3L - 1)), 1/(1728𝔠_∞K_FP) }"
151. K_FP → eps_br [def] PROOF.md: "ε_br := min{ ε_*/(1 + 36p_L𝔠_∞), 1/(24𝔠_∞²C_♭), r_♭/(24𝔠_∞), r_♭/(18(3L - 1)), 1/(1728𝔠_∞K_FP) }"
152. p_L → eps_br [def] PROOF.md: "ε_br := min{ ε_*/(1 + 36p_L𝔠_∞), 1/(24𝔠_∞²C_♭), r_♭/(24𝔠_∞), r_♭/(18(3L - 1)), 1/(1728𝔠_∞K_FP) }"
153. c_inf → C_bg [def] SF.md: "C_bg := 1.011√N·max{1 + 48𝔠_∞, 36p_L𝔠_∞}"
154. p_L → C_bg [def] SF.md: "C_bg := 1.011√N·max{1 + 48𝔠_∞, 36p_L𝔠_∞}"
155. eps_br → eps1 [le] SF.md: "(TH-ch″) := (TH-ch′) ∧ ε_1 ≤ ε_br/(1.011√N)"
156. eps_star_N5 → eps1 [le] RLARGE.md: "ε_1, ε_loc, ε^J_loc ≤ the N5 background threshold (matching units)" — level 0: ε_* = 2.476·10⁻¹³/C_Δ
157. eps_N5_unif → eps1 [le] RLARGE.md: "ε_1, ε_loc, ε^J_loc ≤ the N5 background threshold (matching units)"
158. eps_N5_unif → eps_loc [le] RLARGE.md: "ε_1, ε_loc, ε^J_loc ≤ the N5 background threshold (matching units)"
159. eps_star_N5 → eps_N5_unif [le] RLARGE.md: "Level 0: **ε_* = 2.476·10⁻¹³/C_Δ** on the session-23"
160. c_inf → C_theta [def] PROOF.md: "C_θ := 288𝔠_∞³C_♭ + 792𝔠_∞ℓ_θ + 24𝔠_∞c_π + 288A_incoth⁴(m_1/2)ℓ_θ + 53(48𝔠_∞ + 1)² + 1296𝔠_∞ℓ_θ"
161. C_flat_PR → C_theta [def] PROOF.md: "C_θ := 288𝔠_∞³C_♭ + 792𝔠_∞ℓ_θ + 24𝔠_∞c_π + 288A_incoth⁴(m_1/2)ℓ_θ + 53(48𝔠_∞ + 1)² + 1296𝔠_∞ℓ_θ"
162. ell_theta → C_theta [def] PROOF.md: "C_θ := 288𝔠_∞³C_♭ + 792𝔠_∞ℓ_θ + 24𝔠_∞c_π + 288A_incoth⁴(m_1/2)ℓ_θ + 53(48𝔠_∞ + 1)² + 1296𝔠_∞ℓ_θ"
163. A_inout → C_theta [def] PROOF.md: "C_θ := 288𝔠_∞³C_♭ + 792𝔠_∞ℓ_θ + 24𝔠_∞c_π + 288A_incoth⁴(m_1/2)ℓ_θ + 53(48𝔠_∞ + 1)² + 1296𝔠_∞ℓ_θ"
164. m_N5 → C_theta [def] PROOF.md: "C_θ := 288𝔠_∞³C_♭ + 792𝔠_∞ℓ_θ + 24𝔠_∞c_π + 288A_incoth⁴(m_1/2)ℓ_θ + 53(48𝔠_∞ + 1)² + 1296𝔠_∞ℓ_θ"
165. A_inout → ell_theta [def] PROOF.md: "D_L(θ) := the least D with 24A_out n(D_g)e^{-m_1D/2} ≤ θ/2"
166. m_N5 → ell_theta [def] PROOF.md: "D_L(θ) := the least D with 24A_out n(D_g)e^{-m_1D/2} ≤ θ/2"
167. eps_br → eps_theta [def] PROOF.md: "ε_θ := min{ε_br, α_*/(12ℓ_θ), r_♭/(18ℓ_θ), 1/(60ℓ_θ), 1/(80(48𝔠_∞ + 1))}"
168. alpha_star → eps_theta [def] PROOF.md: "ε_θ := min{ε_br, α_*/(12ℓ_θ), r_♭/(18ℓ_θ), 1/(60ℓ_θ), 1/(80(48𝔠_∞ + 1))}"
169. ell_theta → eps_theta [def] PROOF.md: "ε_θ := min{ε_br, α_*/(12ℓ_θ), r_♭/(18ℓ_θ), 1/(60ℓ_θ), 1/(80(48𝔠_∞ + 1))}"
170. c_inf → eps_theta [def] PROOF.md: "ε_θ := min{ε_br, α_*/(12ℓ_θ), r_♭/(18ℓ_θ), 1/(60ℓ_θ), 1/(80(48𝔠_∞ + 1))}"
171. eps_theta → eps_unif [def] PROOF.md: "Put θ := (1 - K̄)/2, η_* := inf_i min{ε_θ^{(i)}, θ/C_θ^{(i)}, θ/C_θ^{ρ,(i)}, 1/(636p_L𝔠_∞^{(i)}), ε_br^{(i)}}" — per-level route (NAH-unif, GAP as stated); on the BFT route CURV1's constants are not consumed (REVIEW_S22: 'NAH-unif′, HG-ind's uniform form and (H-K) all become unnecessary')
172. C_theta → eps_unif [def] PROOF.md: "Put θ := (1 - K̄)/2, η_* := inf_i min{ε_θ^{(i)}, θ/C_θ^{(i)}, θ/C_θ^{ρ,(i)}, 1/(636p_L𝔠_∞^{(i)}), ε_br^{(i)}}"
173. N → eps0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
174. N → rC_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
175. N → m0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
176. N → C0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
177. N → T0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
178. L → eps0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
179. L → rC_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
180. L → m0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
181. L → C0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
182. L → T0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
183. kappa_pm → eps0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
184. kappa_pm → rC_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
185. kappa_pm → m0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
186. kappa_pm → C0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
187. kappa_pm → T0_BFT [def] REVIEW_S22.md: "**depending only on (N, L, κ_±)**"
188. theta_wc → BFT012 [def] REVIEW_S22.md: "level-j curvature and soft-fluctuation components are weighted by L^{θ_w(k-j)}" — REVIEW_S22 writes one θ_w; the decoupled exponents (THETAW, CONFIRMED faithful by REVIEW55_TUNIF W2) are what the statement needs
189. theta_wr → BFT012 [def] REVIEW_S22.md: "level-j curvature and soft-fluctuation components are weighted by L^{θ_w(k-j)}" — REVIEW_S22 writes one θ_w; the decoupled exponents (THETAW, CONFIRMED faithful by REVIEW55_TUNIF W2) are what the statement needs
190. theta_A → BFT012 [def] REVIEW_S22.md: "level-j curvature and soft-fluctuation components are weighted by L^{θ_w(k-j)}" — REVIEW_S22 writes one θ_w; the decoupled exponents (THETAW, CONFIRMED faithful by REVIEW55_TUNIF W2) are what the statement needs
191. theta_src → BFT012 [def] REVIEW_S22.md: "level-j curvature and soft-fluctuation components are weighted by L^{θ_w(k-j)}" — REVIEW_S22 writes one θ_w; the decoupled exponents (THETAW, CONFIRMED faithful by REVIEW55_TUNIF W2) are what the statement needs
192. alpha_BFT → BFT012 [def] REVIEW_S22.md: "level-j curvature and soft-fluctuation components are weighted by L^{θ_w(k-j)}" — REVIEW_S22 writes one θ_w; the decoupled exponents (THETAW, CONFIRMED faithful by REVIEW55_TUNIF W2) are what the statement needs
193. theta_src → alpha_BFT [le] REVIEW55_TUNIF.md: "0 < α < θ < 1; even θ ≤ 1 − α"
194. eps0_BFT → BFT012 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
195. rC_BFT → BFT012 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
196. m0_BFT → BFT012 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
197. C0_BFT → BFT012 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
198. T0_BFT → BFT012 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
199. eps0_BFT → BFT3 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
200. rC_BFT → BFT3 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
201. m0_BFT → BFT3 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
202. C0_BFT → BFT3 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
203. T0_BFT → BFT3 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
204. eps0_BFT → BFT4 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
205. rC_BFT → BFT4 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
206. m0_BFT → BFT4 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
207. C0_BFT → BFT4 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
208. T0_BFT → BFT4 [def] REVIEW_S22.md: "there exist ε_0 > 0, r_ℂ ∈ (0, 1], θ_w ∈ (0, 2], m_0 > 0, C_0 < ∞ and T_0"
209. eps0_BFT → eps_N5_unif [le] REVIEW_S22.md: "max_P|log V^r_{k,P}| ≤ ε ≤ ε_0 and" — the level-uniform N5 threshold must sit inside BFT's domain (matching units)
210. N → BFT5 [def] BFT_B.md: "There are ε_5 > 0 and C_5 < ∞, depending only on (N, L, κ_±) and not on k or T (T ≥ 5)"
211. L → BFT5 [def] BFT_B.md: "There are ε_5 > 0 and C_5 < ∞, depending only on (N, L, κ_±) and not on k or T (T ≥ 5)"
212. kappa_pm → BFT5 [def] BFT_B.md: "There are ε_5 > 0 and C_5 < ∞, depending only on (N, L, κ_±) and not on k or T (T ≥ 5)"
213. BFT012 → BFT5 [req] REVIEW_S22.md: "This follows from BFT-1/2 plus (G♯_0-field) + (R♯_ω) by SF's Lemma G-pert on X_c-small patches"
214. C_fun → BFT5 [req] BFT_B.md: "it is CONDITIONAL on (CO-fun) for the curvature half" — the lane-B route to BFT-5 (b): its curvature-half constant is C_fun
215. BFT012 → eps_N5_unif [req] REVIEW_S22.md: "PROOF/N5: BFT-0, 1 (θ_w = 0 suffices), 2 and 4."
216. BFT4 → eps_N5_unif [req] REVIEW_S22.md: "PROOF/N5: BFT-0, 1 (θ_w = 0 suffices), 2 and 4."
217. BFT012 → sigma_fl [req] PLD.md: "Levels k ≥ 1 need σ_fl at level k (N5 level-uniformity, BFT)."
218. eps1 → IkE [def] HIST.md: "α_E ≥ c·ε_1 (a g-INDEPENDENT radius: the whole ε_1-domain)"
219. A5 → IkE [req] RLARGE.md: "Theorem A5 [ARGUED] ⇐ (a5-G♯) + (R♯) [A/PROOF-N2, OPEN] + (a5-U) [HIST, OPEN] + (a3-q) [HIST, OPEN] + (MS-Sob)"
220. a5G → A5 [req] RLARGE.md: "Theorem A5 [ARGUED] ⇐ (a5-G♯) + (R♯) [A/PROOF-N2, OPEN] + (a5-U) [HIST, OPEN] + (a3-q) [HIST, OPEN] + (MS-Sob)"
221. BFT5 → a5G [req] REVIEW_S22.md: "SF: BFT-1 (θ_w > 0), 2 (complex ball for (R♯)) and 5, giving (a5-G♯), (a5-U) and (MIN-reg)."
222. BFT012 → a5G [req] REVIEW_S22.md: "SF: BFT-1 (θ_w > 0), 2 (complex ball for (R♯)) and 5, giving (a5-G♯), (a5-U) and (MIN-reg)."
223. IkE → a_A [req] RLARGE.md: "(SDP)^A ⇐ (I_{k-1}^E)''(d'') + (CLS-min) + (W1-ret'^J)_{k-1}(c) + (SC)_{k-1} [A/PLD, s-P] + I-tay^J [R/HIST, s]"
224. CLSmin → a_A [req] RLARGE.md: "(SDP)^A ⇐ (I_{k-1}^E)''(d'') + (CLS-min) + (W1-ret'^J)_{k-1}(c) + (SC)_{k-1} [A/PLD, s-P] + I-tay^J [R/HIST, s]"
225. SC_k → a_A [req] RLARGE.md: "(SDP)^A ⇐ (I_{k-1}^E)''(d'') + (CLS-min) + (W1-ret'^J)_{k-1}(c) + (SC)_{k-1} [A/PLD, s-P] + I-tay^J [R/HIST, s]"
226. IkE → C_A [req] RLARGE.md: "(SDP)^A ⇐ (I_{k-1}^E)''(d'') + (CLS-min) + (W1-ret'^J)_{k-1}(c) + (SC)_{k-1} [A/PLD, s-P] + I-tay^J [R/HIST, s]"
227. CLSmin → C_A [req] RLARGE.md: "(SDP)^A ⇐ (I_{k-1}^E)''(d'') + (CLS-min) + (W1-ret'^J)_{k-1}(c) + (SC)_{k-1} [A/PLD, s-P] + I-tay^J [R/HIST, s]"
228. SC_k → C_A [req] RLARGE.md: "(SDP)^A ⇐ (I_{k-1}^E)''(d'') + (CLS-min) + (W1-ret'^J)_{k-1}(c) + (SC)_{k-1} [A/PLD, s-P] + I-tay^J [R/HIST, s]"
229. IkE → c_A [req] RLARGE.md: "(SDP)^A ⇐ (I_{k-1}^E)''(d'') + (CLS-min) + (W1-ret'^J)_{k-1}(c) + (SC)_{k-1} [A/PLD, s-P] + I-tay^J [R/HIST, s]"
230. CLSmin → c_A [req] RLARGE.md: "(SDP)^A ⇐ (I_{k-1}^E)''(d'') + (CLS-min) + (W1-ret'^J)_{k-1}(c) + (SC)_{k-1} [A/PLD, s-P] + I-tay^J [R/HIST, s]"
231. SC_k → c_A [req] RLARGE.md: "(SDP)^A ⇐ (I_{k-1}^E)''(d'') + (CLS-min) + (W1-ret'^J)_{k-1}(c) + (SC)_{k-1} [A/PLD, s-P] + I-tay^J [R/HIST, s]"
232. IkE → c_sf [req] RLARGE.md: "source: F^col_Q ≤ Σ_{x under Q}𝓔_{k,x} plus node A's"
233. IkE → C_rho [req] FLOW.md: "where C_ρ is explicit in the polymer norms of the step output"
234. SC_k → C_p_RLF0 [req] RLARGE.md: "W1R: (a)-(b) CONDITIONAL ⇐ (SC)_k + (SF-irr)_{k+1} (one-field form)"
235. SC_k → a_ret [req] PLD.md: "a_ret below is "the per-cube price entering (SC)_k's expansion, conditional on (SC)_k""
236. c_pr → CLSmin [def] RLARGE.md: "This is where the coherent background is priced: (CLS-min)_{c_pr,t_pr}"
237. t_pr → CLSmin [def] RLARGE.md: "This is where the coherent background is priced: (CLS-min)_{c_pr,t_pr}"
238. REGmin → CLSmin [req] RLARGE.md: "primary source **(CLS-min) ⇐ (REG-min)**"
239. CLSmin → a_bad [req] RLARGE.md: "[HW-1] Lemma TE (ii) + W-bad ⇐ (CLS-min)"
240. LIF → c_LI [def] HW.md: "allowance c_LI plus the moments' own."
241. q_M → C_T [def] SQ.md: "ε_* = ε_*(N, q) > 0 and C_T = C_T(N, q)"
242. N → C_T [def] SQ.md: "ε_* = ε_*(N, q) > 0 and C_T = C_T(N, q)"
243. q_M → eps_star_EPST [def] SQ.md: "ε_* = ε_*(N, q) > 0 and C_T = C_T(N, q)"
244. m_ES1 → eps_star_EPST [le] EPSSTAR.md: "(ABS-ε) is the definition of an admissible ε_*"
245. m_ES1 → A_cg [def] EPSSTAR.md: "A_cγ_c ≤ (1 + √6)·C_{S1}(q, m)/m, a bound containing NO c_K, c_RB, C_K′, C_B, c_N or ε_*."
246. q_M → A_cg [def] EPSSTAR.md: "A_cγ_c ≤ (1 + √6)·C_{S1}(q, m)/m, a bound containing NO c_K, c_RB, C_K′, C_B, c_N or ε_*."
247. A_cg → C_T [def] CONST_T.md: "C_T = √6 · F · B(4a) · Ĉ"
248. F_sched → C_T [def] CONST_T.md: "C_T = √6 · F · B(4a) · Ĉ"
249. eps_star_EPST → theta_eps [def] SQ.md: "θ_ε the largest θ with 4·2.47N√κ_+θ ≤ ε_* and 16·32^{1/8}C_0θ ≤ ε_*"
250. C0_SQ → theta_eps [def] SQ.md: "θ_ε the largest θ with 4·2.47N√κ_+θ ≤ ε_* and 16·32^{1/8}C_0θ ≤ ε_*"
251. kappa_pm → theta_eps [def] SQ.md: "θ_ε the largest θ with 4·2.47N√κ_+θ ≤ ε_* and 16·32^{1/8}C_0θ ≤ ε_*"
252. q_M → theta_G [def] SQ.md: "θ_G := the largest θ with qβ ≤ ½ and LEV-E's conditions"
253. theta_G → theta0_SQ4 [def] SQ.md: "θ_0 := min{θ_G, θ_ε}"
254. theta_eps → theta0_SQ4 [def] SQ.md: "θ_0 := min{θ_G, θ_ε}"
255. C_T → A0_SQ [def] SQ.md: "A_0 := c_NC_T'(2.47N√κ_+ + 32^{1/8}C_0)"
256. C0_SQ → A0_SQ [def] SQ.md: "A_0 := c_NC_T'(2.47N√κ_+ + 32^{1/8}C_0)"
257. kappa_pm → A0_SQ [def] SQ.md: "A_0 := c_NC_T'(2.47N√κ_+ + 32^{1/8}C_0)"
258. q_RES → B0_SQ [def] SQ.md: "Put B_0 := 4.1C_r/(1 - qL²), G := 2(1.011A_0 + B_0)"
259. C_r_SQ → B0_SQ [def] SQ.md: "Put B_0 := 4.1C_r/(1 - qL²), G := 2(1.011A_0 + B_0)"
260. A0_SQ → C_D [def] SQ.md: "C_D := max{G, C_r}, G = 2(1.011A_0 + B_0) (STOKES-it)"
261. B0_SQ → C_D [def] SQ.md: "C_D := max{G, C_r}, G = 2(1.011A_0 + B_0) (STOKES-it)"
262. C_r_SQ → C_D [def] SQ.md: "C_D := max{G, C_r}, G = 2(1.011A_0 + B_0) (STOKES-it)"
263. tau_sizes → tau_R [def] SQ.md: "**(REG-min)** holds, by Theorem RED-0 (§13.5) with τ_R := min{τ_0, τ_*, τ_S, θ_S/C', θ_0/C'}"
264. theta0_SQ4 → tau_R [def] SQ.md: "**(REG-min)** holds, by Theorem RED-0 (§13.5) with τ_R := min{τ_0, τ_*, τ_S, θ_S/C', θ_0/C'}"
265. C_prime → tau_R [def] SQ.md: "**(REG-min)** holds, by Theorem RED-0 (§13.5) with τ_R := min{τ_0, τ_*, τ_S, θ_S/C', θ_0/C'}"
266. C_D → C_err [def] SQ.md: "C_err := C_p(K² + K_top²) + 4C_e[K²/(L(L - 1)) + 1.011KC_DL/(L² - 1)]"
267. C_err → theta0_SUP [def] SQ.md: "θ ≤ θ_0 := 1/(2C_err)"
268. C_D → theta_sharp_SQ [def] SQ.md: "θ_♯(N, L, κ_-, C_D) := the largest θ satisfying all of"
269. tau_R → tau_flat [def] SQ.md: "Write τ_♭ := min{τ_F, τ_R, θ_0/C',"
270. theta0_SUP → tau_flat [def] SQ.md: "Write τ_♭ := min{τ_F, τ_R, θ_0/C',"
271. theta_sharp_SQ → tau_flat [def] SQ.md: "Write τ_♭ := min{τ_F, τ_R, θ_0/C',"
272. C_D → tau_flat [def] SQ.md: "Write τ_♭ := min{τ_F, τ_R, θ_0/C',"
273. C_prime → tau_flat [def] SQ.md: "Write τ_♭ := min{τ_F, τ_R, θ_0/C',"
274. tau_flat → eta_flat [def] SQ.md: "η_♭ := c_♭τ_♭²/C'²"
275. c_flat → eta_flat [def] SQ.md: "η_♭ := c_♭τ_♭²/C'²"
276. C_prime → eta_flat [def] SQ.md: "η_♭ := c_♭τ_♭²/C'²"
277. tau_flat → t_pr [def] RLARGE.md: "via (REG-min) (primary), c_pr = c_♭/C′², t_pr = C′τ_♭"
278. eta_flat → eps1 [le] EPSSTAR.md: "The DESC-ε substitution needs η_♭ ≥ 4C_3ε_1²" — DESC-ε (iii) consumers (HIST A5 (A), (I_k^E)′ (a4), SF); fails at the in-force ε_1 by 4.85 decades in ε_1 (TAUFLAT; REVIEW55_CONST K7) — option C lowers ε_1, or (MS-Sob)
279. C3 → eps1 [le] EPSSTAR.md: "The DESC-ε substitution needs η_♭ ≥ 4C_3ε_1²"
280. C_D → REGmin [def] SQ.md: "C_D := max{G, C_r}, G = 2(1.011A_0 + B_0) (STOKES-it)"
281. tau_R → REGmin [def] SQ.md: "**(REG-min)** holds, by Theorem RED-0 (§13.5) with τ_R := min{τ_0, τ_*, τ_S, θ_S/C', θ_0/C'}"
282. tau_c → rho_band [def] SF.md: "ρ_band = τ_c/(2C_W) = 2.280·10⁻⁶¹ (C_W = 95.145)"
283. rho_band → a_sh [def] SF.md: "a_sh = ρ_band/(16L⁴N′) = 1.759·10⁻⁶⁴/N′"
284. N_prime → a_sh [def] SF.md: "a_sh = ρ_band/(16L⁴N′) = 1.759·10⁻⁶⁴/N′"
285. sf_chain → a_sh [def] SF.md: "R_sh = μ^{-1}ln(r_sol/a_sh)"
286. a_sh → aprime_DX [def] SF.md: "C_Ω := C + 3(N² - 1)/2 and a′ = a_sh²/(8N||C||m_sh)"
287. lam_bg → aprime_DX [def] SF.md: "With ||C|| ≤ 1/λ_min certified and the CHEB-f rate, DX′-1's ceiling is recomputed" — the certified class value 3.17·10⁻³ replaces 6.6·10⁻¹⁰ ([SF7-edit]; REVIEW55_LEAD r55l-H7)
288. aprime_DX → g_DX [def] SF.md: "summing over patterns needs a′/g_0² ≥ C_Ω|Ω_B| + 1"
289. C_Omega → g_DX [def] SF.md: "summing over patterns needs a′/g_0² ≥ C_Ω|Ω_B| + 1"
290. a_sh → g_DX [def] SF.md: "summing over patterns needs a′/g_0² ≥ C_Ω|Ω_B| + 1"
291. a_p_ac → g_hole [def] SF.md: "read **g_0² ≲ (min{a_p, a_c}/a_p)·1.6·10⁻¹²⁶**"
292. rho_band → g_band [def] SF.md: "g_0 ≤ ρ_band/(4√Np_0·max{N_r, 2N_μ(|𝒞|)})"
293. N_prime → g_band [def] SF.md: "g_0 ≤ ρ_band/(4√Np_0·max{N_r, 2N_μ(|𝒞|)})"
294. sf_chain → g_FS1 [def] SF.md: "i.e. g_0² ≤ 1.8·10⁻¹¹³ (g_0 ≤ 4.3·10⁻⁵⁷) at session-5's ζ"
295. g_DX → g_star_SF [def] SF.md: "all enter O0's **g_*** (min of all)"
296. g_hole → g_star_SF [def] SF.md: "all enter O0's **g_*** (min of all)"
297. g_band → g_star_SF [def] SF.md: "all enter O0's **g_*** (min of all)"
298. g_FS1 → g_star_SF [def] SF.md: "all enter O0's **g_*** (min of all)"
299. g_star_SF → g0 [le] REVIEW55_HWPLD.md: "the threshold must work for every K, in particular K = 1, where the" + RLARGE.md: "g_0² ≲ 2.5·10⁻¹⁵²/C_Ω (REVIEW_SF_S7 C-1), so RLF's own ceilings do not bind at the current constants." — symbol collision on g_0 (REVIEW55_HWPLD F1): the stage-0 ceiling bounds g_K's threshold through (F-3)'s upper bracket at K = 1
300. R → g0 [le] REVIEW55_HWPLD.md: "the threshold must work for every K, in particular K = 1, where the" — the (F-3) shift β_+log L + R
301. eps1 → EX_first [def] ../ym4d-existence/EXISTENCE.md: "(LF-loc) (⇐ Theorem CB + (RLF-3^dis) at ε = ε_1"
302. EX_first → C4 [order] ../ym4d-existence/EXISTENCE.md: "(F, h, n, ε, w) first; then the constants of (CE-cond^ms), (MOM_4),"
303. EX_first → CEcond [order] ../ym4d-existence/EXISTENCE.md: "(F, h, n, ε, w) first; then the constants of (CE-cond^ms), (MOM_4),"
304. eps_N5_unif → CEexp [req] ../ym4d-existence/EXISTENCE.md: "CE-exp^k CONDITIONAL; (N5-unif) CONDITIONAL ⇐ (H-K) + (H-C⁺) + (H-ℂ) (or ⇐ BFT-0,1,2,4 without (H-K))"
305. BFT3 → CEexp [req] ../ym4d-existence/EXISTENCE.md: "**(L-loc)_k OPEN, inside the B-NA wall** (needs all-order mixed-derivative decay: BFT-3 states orders ≤ 4 only, so (L-loc)_k is beyond BFT as stated [inference])"
306. CEexp → CEcond [req] ../ym4d-existence/EXISTENCE.md: "| (M2) level-uniform stage-j expansion | **Corollary CE-exp^k** at k = j → ∞"
307. C4 → Kcompat [def] ../ym4d-existence/EXISTENCE.md: "48β_b²W²C_4ρ ≤ A_*"
308. CEcond → Kcompat [def] ../ym4d-existence/EXISTENCE.md: "48β_b²W²C_4ρ ≤ A_*"
309. CEcond → g_3 [def] ../ym4d-existence/EXISTENCE.md: "(true for g ≤ g_3, an explicit threshold"
310. Kcompat → g_3 [order] ../ym4d-existence/EXISTENCE.md: "(K) is checked once (it involves g only through ρ ≤ 2 for g small); then g ≤ min{g_c, g_3}"
311. Kcompat → g_c [order] ../ym4d-existence/EXISTENCE.md: "(K) is checked once (it involves g only through ρ ≤ 2 for g small); then g ≤ min{g_c, g_3}"
312. g_3 → g0 [le] ../ym4d-existence/EXISTENCE.md: "then g ≤ min{g_c, g_3} with ρ ≤ (the value" — the existence lane's g is the coupling at the observation level; with (F_R) its ceiling is a ceiling on g_K
313. g_c → g0 [le] ../ym4d-existence/EXISTENCE.md: "then g ≤ min{g_c, g_3} with ρ ≤ (the value"
314. g0 → R_g [order] ../ym4d-existence/EXISTENCE.md: "then R(g); then K_0, T_1(R). n does not depend on g."
315. R_g → K0_T1 [order] ../ym4d-existence/EXISTENCE.md: "then R(g); then K_0, T_1(R). n does not depend on g."
316. eps1 → eta_1 [def] RLARGE.md: "η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d(L))}"
317. eps1 → a_RS [def] RLARGE.md: "a_RS := min{a_η, κε_1²/(256N)}"
318. eta_1 → a_RS [def] RLARGE.md: "a_RS := min{a_η, κε_1²/(256N)}" — a_η taken at its bare-level value η_1²/(2N) (l.1026)
319. q0_NQ → N1_15 [def] REVIEW55_NORMS.md: "𝔮₀ enters only prefactors; A_soft is 𝔮₀-free; j-uniformity is what is load-bearing"
320. NL4 → N1_15 [def] REVIEW55_TUNIF.md: "(N-loc) bypassed at fixed T (price T^{d+2}); open half = T-uniformity" — superseded route
321. S_T → N1_15 [def] GREENT.md: "Corollary NL-4's T^d replaced by a cell sum of size O(log T), with the constant exhibited." — superseded route
322. C_flat_PR → C_flat_i [def] PROOF.md: "C_♭^{(i+1)} ≤ Z_colZ_row²·C_♭^{(i)} + (1 + Z_col)(1 + Z_row)²·C_soft"
323. C_flat_i → C_theta_i [def] PROOF.md: "C_θ^{(i)} ≥ Π_{j≤i}(4κ_{j-1}𝔠_∞^{(j)}) grows geometrically"
324. C_theta → C_theta_i [def] PROOF.md: "C_θ^{(i)} ≥ Π_{j≤i}(4κ_{j-1}𝔠_∞^{(j)}) grows geometrically"
325. C_theta_i → eps_unif [def] PROOF.md: "ε_unif := inf_i min{η_*, ε_H^{(i)},"
326. K_bar → eps_unif [def] PROOF.md: "Put θ := (1 - K̄)/2"
327. E_0 → IkE [def] HIST.md: "all constants (E_0, κ_p, α_E, C_ℓ, B_0) independent of g, k, K, T and 𝔥"
328. eps1 → eps_J_loc [def] HIST.md: "ε^J_loc := ε_1/(157(1 + A_d)√N)"
329. A_d → eps_J_loc [def] HIST.md: "ε^J_loc := ε_1/(157(1 + A_d)√N)"
330. eps_N5_unif → eps_J_loc [le] RLARGE.md: "ε_1, ε_loc, ε^J_loc ≤ the N5 background threshold (matching units)"
331. eps1 → stage_consts [def] HIST.md: "a_J := κε_1²/(2048N),  p_J := (N² - 1)(n_ℓ + 18),  ε^J_loc := ε_1/(157(1 + A_d)√N),  Λ^J_1 := 8κ(2 + C_𝒩),"
332. stage_consts → C_A [req] RLARGE.md: "R1^J's gas convergence …; the"
333. stage_consts → a_A [req] RLARGE.md: "R1^J's gas convergence …; the"
334. kappa0_CE → kappa_d [le] RLARGE.md: "κ > 3κ_0 + 3 (≈ 457 in M-units)"
335. kappa_d → g0 [le] RLARGE.md: "H_0 ≤ c_0(κ), for g_K small enough (to be made" — Theorem CE's amplitude condition at level K
336. a → RLF3dis [def] RLARGE.md: "The exponent EXISTENCE should read is a (not a_♯)"
337. C_ell → RLF3dis [def] RLARGE.md: "since Z(𝔥) decomposes Z_K (Lemma HR) and (RLF-3′) is relative to Z(∅) ≤ Z_K, ratios"
338. RLF3dis → g_3 [def] ../ym4d-existence/EXISTENCE.md: "g^{-p_d}e^{-a_d/(2g_{j'}²)}"
339. RLF3dis → C4 [req] ../ym4d-existence/EXISTENCE.md: "Theorem CB + a **prefactor-free** (RLF-3^dis) at g-scaled thresholds (§20.2)"
340. E2F → c_f [req] HW.md: "Corollary CRC-HW ((M-f^cap) on the (E2) route): CONDITIONAL" — CRC-2T′'s hypothesis (E2^𝔉′) is false as quantified until F_< is restricted (F6): the implication producing c_f is then vacuous, not wrong
341. E2F → C_ellp [req] HW.md: "§32 l.1690's PRIMED C_ℓ (with C_fc′ = 2C_fc e^{c_f}) is the one REL-boot's r and B_0 need"
342. N → eps1 [le] RLARGE.md: "ε_1 < 2sin(π/N) (implied)"
343. a_bad → a_D [def] RLARGE.md: "a_D := min{a_bad, a_cb}, with θ ∈ (0, 1/(96·82))"
344. a_cb → a_D [def] RLARGE.md: "a_D := min{a_bad, a_cb}, with θ ∈ (0, 1/(96·82))"
345. a_D → a [le] RLARGE.md: "Theorem HW's proof with these windows gives the price e^{-θa_D(u_j - R)}" — with the collar-bad family (row 10f) the unreturned exponent is θa_D ≤ θa_bad
346. kappa_RL → g0 [le] RLARGE.md: "g_k, g_{k+1} ≤ min{1, √κ}/√2" — CL^J's Setting (owed by HIST, row 4a)
347. g1_FLOW → g0 [le] FLOW.md: "g_1 := (γ^{-2} + R)^{-1/2}: for every K ≥ 1 and g ∈ (0, g_1]" — the final coupling g = g_K must be ≤ FLOW's g_1
348. dbeta → V_LF [def] RLARGE.md: "𝒱_K^{LF} := Σ_{k<K: T_{k+1}≥W}N_{k+1}c̄_0^{sea}(g_k)"
349. W → V_LF [def] RLARGE.md: "𝒱_K^{LF} := Σ_{k<K: T_{k+1}≥W}N_{k+1}c̄_0^{sea}(g_k)"
350. V_LF → NA_empty [req] RLARGE.md: "|log Z(∅) - 𝒱_K^{LF} - log Z_K^{sf}| ≤ C|T|e^{-a′/g_K²} uniformly in K" (absorbs: RLARGE.md: "|log Z(∅) - 𝒱_K^{LF} - log Z_K^{sf}| ≤ C|T|e^{-a′/g_K²} uniformly in K") — (NA-∅) SUBTRACTS 𝒱_K^{LF}: its divergence is extracted, so it does not propagate into the (RLF-4) constants
351. MSSob → A5 [req] RLARGE.md: "Theorem A5 [ARGUED] ⇐ (a5-G♯) + (R♯) [A/PROOF-N2, OPEN] + (a5-U) [HIST, OPEN] + (a3-q) [HIST, OPEN] + (MS-Sob)"
352. theta_src → theta_wr [le] REVIEW55_TUNIF.md: "((C2) θ_w^r ≤ 2 + θ, (C3) α < θ, the" — strict θ_w^r < 2 + θ: at the endpoint the Σ-aggregated estimate loses a factor k (CODEX_REVIEW_THETAW F10; REVIEW55_TUNIF W4)
353. L → C_fun [def] REVIEW_BFT_B_S9_S10.md: "§35.6 substitutes the **per-level** row bound π_l(V_l) ≤ 2C_NCC_bchκ_+L²η²"
354. kappa_pm → C_fun [def] REVIEW_BFT_B_S9_S10.md: "§35.6 substitutes the **per-level** row bound π_l(V_l) ≤ 2C_NCC_bchκ_+L²η²"
355. tau_sizes → q_RES [def] SQ.md: "q := L⁻³ + C_qτ ≤ (L⁻² + L⁻³)/2"
356. alpha_star → lam_bg [def] PROOF.md: "CS-1 (binding): this enlarges 𝔑(α_*) to C_Δα_* = 1.0568·10⁻³, and on the enlarged"
357. C_Delta → lam_bg [def] PROOF.md: "CS-1 (binding): this enlarges 𝔑(α_*) to C_Δα_* = 1.0568·10⁻³, and on the enlarged"
358. C_Delta → c_inf [def] PROOF.md: "𝔠_∞ := min{8coth⁴(a/2), 81((N² - 1)n_Ω)^{1/2}}/(γ'(1 - ε_R)) + ν_w + C_Δα_*"
359. L → K_FP [def] PROOF.md: "K_FP := max{(2/c_D)(1 + √c_D/(4√d)), (1 + 4√d/√c_D)/s_M}"
360. d → K_FP [def] PROOF.md: "K_FP := max{(2/c_D)(1 + √c_D/(4√d)), (1 + 4√d/√c_D)/s_M}"
361. c_A → B_0 [def] HW.md: "a, C_ℓ, c (from the moments and (LI)) → B_0 := B_1 + c + 1" + HW.md: "already gives (PRICE^ℛ) at one level with a = a_A,"

## Appendix C — the live quantifier order (B-strict edges), verbatim from `checks/dag55_2_out.txt` (positions 0-163)

0:A_d 1:L 2:N 3:d 4:kappa0 5:kappa_RL 6:kappa_pm 7:m_ES1 8:n_1 9:n_int 10:p_L 11:q_M 12:theta_A 13:theta_src 14:alpha_BFT 15:theta_wc 16:theta_wr 17:A_cg 18:C0_BFT 19:C0_SQ 20:C3 21:C_Omega 22:C_fun 23:C_prime 24:C_r_SQ 25:E2F 26:E_0 27:F_sched 28:C_T 29:A0_SQ 30:G_inf 31:K_FP 32:LIF 33:MSSob 34:N_prime 35:R0 36:R 37:SC_k 38:C_p_RLF0 39:T0_BFT 40:b_1 41:beta0p 42:beta_m 43:c_LI 44:c_att 45:c_flat 46:c_pr 47:delta_0 48:gap0 49:kappa0_CE 50:kappa_d 51:m0_BFT 52:m_N5 53:rstar 54:C_Delta 55:alpha_star 56:S_prime 57:gamma_prime 58:R_star_N5 59:T0_N5 60:c_inf 61:C_bg 62:lam_bg 63:r_flat 64:C_flat_PR 65:sf_chain 66:theta_cb 67:eps0_BFT 68:eps_star_EPST 69:eps_star_N5 70:eps_br 71:g_FS1 72:n_J_star 73:rC_BFT 74:BFT012 75:BFT3 76:BFT4 77:BFT5 78:a5G 79:A5 80:sigma_fl 81:eps_N5_unif 82:CEexp 83:tau_c 84:a_p_ac 85:rho_band 86:a_sh 87:aprime_DX 88:eps_bg 89:g_DX 90:g_band 91:g_hole 92:g_star_SF 93:tau_sizes 94:q_RES 95:B0_SQ 96:C_D 97:C_err 98:theta0_SUP 99:theta_G 100:theta_eps 101:theta0_SQ4 102:tau_R 103:REGmin 104:theta_sharp_SQ 105:tau_flat 106:eta_flat 107:eps1 108:EX_first 109:CEcond 110:IkE 111:C_rho 112:eps_J_loc 113:eta_q 114:eps_loc 115:a_ret 116:gamma0 117:gamma 118:beta_p 119:g1_FLOW 120:t_pr 121:CLSmin 122:a_bad 123:a_cb 124:a_D 125:c_A 126:c_U 127:c_plus 128:b_D 129:b_n 130:c_f 131:B_0 132:c_B 133:kernel_seq 134:stage_consts 135:C_A 136:a_A 137:theta 138:a 139:c_sf 140:C_fc 141:lambda_star 142:C_ell 143:C_ellp 144:RLF3dis 145:C4 146:Kcompat 147:g2_CRC 148:g_3 149:g_c 150:n_H 151:n_sharp 152:C_H 153:W 154:SF_last 155:dbeta 156:V_LF 157:NA_empty 158:a_prime 159:eff_seq 160:eps_sharp 161:g0 162:R_g 163:K0_T1 

---

## Errata to this file (append-only; found on proof-reading at 2026-10-28T23:51Z UTC; nothing above is edited)
1. **§1 item 3 and §4.3's lead sentence "each one taints g_0" are wrong for one of the six:** δβ_k / c̄_0^{sea} (U5) does NOT reach
   g_0 in the encoded graph — its taint stops at the two absorbing edges (Option A's bracket into the stage constants; (NA-∅)'s
   subtraction of 𝒱_K^{LF}) (dag55_2_out.txt: eff_seq and kernel_seq tainted "dbeta -> eff_seq -> kernel_seq", stage_consts tainted
   only "R0 -> R -> stage_consts"). **Five of the six weak seeds taint g_0.** U5's content is therefore a scope question (one
   coupling shift vs two on anisotropic tori, K9), not a uniformity of a constant that g_0 consumes — provided Option A is adopted.
2. **§4.1 "43 live nodes are tainted"**: the checker's count includes the two seeds (C_fun, 𝒱_K^{LF}); 41 non-seed live nodes.
3. **§4.3 table, two quotations are not verbatim:** the C_4 row's exact string is "E||1 - U_k(p)||⁴ ≤ C_4g_k⁴, volume- and K-uniform
   (⇐ Theorem CB + a prefactor-free (RLF-3^dis) at" (ASCII bars and hyphen; the table printed typographic ones); the CE-exp row
   abbreviates with "…" the string "**(L-loc)_k OPEN, inside the B-NA wall** (needs all-order mixed-derivative decay: BFT-3 states
   orders ≤ 4 only, so (L-loc)_k is beyond BFT as stated [inference])". The graph file carries both verbatim (S2 PASS).
4. **§7 Stage 1 is mis-punctuated in two places:** read "BFT's target constants (ε_0, r_ℂ, m_0, C_0, T_0) → BFT-0/1/2, BFT-3,
   BFT-4; C_fun → BFT-5; BFT-0/1/2 and BFT-5 → (a5-G♯) → A5; BFT-0/1/2 → σ_fl; BFT-0/1/2, BFT-4, ε_0, ε_* → the level-uniform N5
   threshold" — there is **no** edge σ_fl → N5 threshold and **no** edge C_fun → BFT-0/1/2. **§7 Stage 4:** read "t_pr → (CLS-min)
   → a_bad; a_cb from ε_loc, η_q, c_pr, t_pr; a_bad, a_cb → a_D" — there is no edge a_bad → a_cb.
5. **§0 "Re-stringed five edges"**: precisely, before dag55_1 ran I changed the string of four edges (CLSmin → a_bad, lam_bg →
   aprime_DX, C_ell → RLF3dis, E2F → c_f), added a second string to one (stage_consts → dbeta), and replaced four multi-line
   strings by single-line ones (edges IkE → c_sf and RLF3dis → C4, node RLF3dis's string2, eps_N5_unif's growth string).
6. **§11 counts are muddled; corrected:** of §10's 13 rows — PROVEN for the encoded graph or by exact arithmetic: rows 1, 6, 10, 11,
   13 (5); DAG-F1 CONDITIONAL: row 2 (1); fixed point, not a constants cycle: row 3 (1); DAG-F2 FOUND on the reviewed record,
   conditional on Step 4's pending review: row 5 (1); read in situ / as stated by the sources: rows 4, 7, 8, 9 (4); ARGUED
   (inference): row 12 (1).
7. **§10 row 7** inherits erratum 1: five of the six weak seeds taint g_0.

## Closing provenance (2026-10-28T23:51Z UTC)
Files written by this worker: SMALLNESS_DAG.md; checks/dag55_1_criteria.md, dag55_1_graph.py, dag55_1_dag.py, dag55_1_out.txt,
dag55_1_err.txt (empty); checks/dag55_2_criteria.md, dag55_2_graph.py, dag55_2_dag.py, dag55_2_out.txt, dag55_2_err.txt (empty);
checks/dag55_3_criteria.md, dag55_3_tc.py, dag55_3_out.txt, dag55_3_err.txt (empty). Scratch drafts (not in the lane): the graph
draft and the string-lookup helper in my scratchpad. No git command was run. No other lane file was edited.
8. **§5 (c) quotes a stale R_sh.** "R_sh ≈ 1.6·10¹² fine spacings" is SF's session-5 figure; at the class in force SF §22.7 row (iii)
   gives "R_sh = 1.57·10⁵, m_sh = 1.2·10²⁰, |Ω_B| = 3.9·10²²" with "CHEB-f's μ and its explicit N_μ(|Õ^{1/2}|)". The point stands
   (a fixed, T-independent neighbourhood; the stage-0 torus must exceed it), with the current size. The same row makes node
   N_prime's status "finite, not evaluated" stale (N_μ(|Õ^{1/2}|) is explicit there); no edge changes.
9. **Quotations in §1-§11** sometimes print formulas with typographic minus signs or bars; the verbatim strings are the ones in
   `checks/dag55_2_graph.py` (and Appendices A-B, generated from it), which S2 audits.
