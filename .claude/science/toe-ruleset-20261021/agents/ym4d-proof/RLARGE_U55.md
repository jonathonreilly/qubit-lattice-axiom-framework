Reviewer model: claude-opus-5-5

# RLARGE_U55 — closing RLARGE's three open items (U1, U3/(TC), FI-1) on the live large-field route

## PRE-STATED (written 2026-10-29T00:09:28Z UTC, before any derivation; statements only)

Worker: Opus 5.5 (claude-opus-5-5). Writes only this file and `checks/ru55_*`. No git.

Targets:
- **T1 (U1).** Determine, or bound from their definitions, the two quantities a_ret and a_A that
  RLARGE's live route ("RLF-step v3") uses in condition (RLF-δ) and in the quoted live margin
  ("+63.6 decades", which assumes θ → 1/24 and a_A ≥ θ·a_bad). Then settle RLARGE's sentence
  "RLF's own ceilings do not bind" (cited near RLARGE l.618; to be located by string) for (RLF-δ):
  CONFIRMED, NOT-VERIFIED or REFUTED.
- **T2 (U3).** SMALLNESS_DAG's check dag55_3 reports that RLARGE's (TC) fails with RLARGE's own
  ε_loc by factors 19.32 / 15.45 / 22.99 / 18.38 (N = 2, 3; κ = 1, 1/4). Prove or refute the argued
  repair (quietness threshold taken that factor below η_q, shrinking a_cb's third entry by the
  factor squared); recompute every quantity the repair changes; check the repaired order against
  SMALLNESS_DAG's topological order for cycles and for K- or T-growth.
- **T3 (FI-1).** Decide whether the fixed point of the coupling-sequence condition that RLARGE's
  Option A removes from the constants ("integration choice", U4) is guaranteed to exist with the
  constants in force, i.e. whether it can be stated as a theorem; align with FLOW55.md if it exists.

What would count as a refutation (of the claim under test, not of my own work):
- T1: a_ret or a_A shown to be unbounded / undefined by any source, or a bound under which (RLF-δ)
  fails at the frozen constants → l.618 REFUTED for (RLF-δ); a quoted margin evaluated at a
  different value of θ, a_A or a_ret than the one in force → that margin REFUTED (re-stated).
- T2: the shrunken threshold failing to restore (TC); the a_cb entry not scaling as the factor
  squared; any new edge in the dependency graph that closes a cycle, or makes a constant that must
  be K- or T-uniform depend on K or T → the repair REFUTED.
- T3: a coupling-sequence condition whose fixed point need not exist (e.g. a map not into its domain,
  a contraction constant not < 1 with the constants in force, or a hidden dependence of the domain
  on the fixed point itself) → "fixed point is a theorem" REFUTED; if the existence needs an input
  no file supplies → NOT-VERIFIED with that input named.

Discipline: every symbol compared is pinned by file + locating string (systemic defect 1); every
inequality is checked at the value of the constant it is evaluated at (defect 2); every numeric gate
gets pre-registered criteria in `checks/ru55_*_criteria.md` before its script, exact rationals only,
and each gate is built so that a wrong answer would fail it (defect 3).

---

## 0. What I read, and how this file is organised (written 2026-10-29T00:31Z, before any check of mine existed)

**Read in full:** REVIEW_BRIEF_55.md; REVIEW55_ARS.md (577 l.); SMALLNESS_DAG.md §0-§11, the errata and Appendix C (Appendices A-B
by grep); checks/dag55_3_criteria.md, dag55_3_tc.py, dag55_3_out.txt; checks/dag55_2_criteria.md and dag55_2_dag.py (the checker).
**Read by string-located range:** RLARGE.md l.1-845 (all live v3 text and the Appendix-A reading notes) and l.902-1010 (frozen
Proposition CL, Lemma RS); HW.md l.160-240 (Lemma TE, W-bad, W-cb, DJ) and grep hits for a_A; HIST.md l.130-260 (PM, KQ, RS-lin,
CL^J) and l.292-380 (Lemma 7.2-0^J, the non-quiet remarks); PLD.md l.470-500 ((SC)_k, Proposition W1R), l.1291-1345 (§16.0),
l.1403-1482 (§16.5-§16.6), l.1506-1600 (§16.8-§16.10), l.2438-2562 (§18.7.0-§18.7.1), l.3455-3560 (§19.8, §19.10);
FLOW.md l.40-80, l.146-235 (Def F-g, layer-1 hypotheses), l.418-500 (F-flow, F-tune, F-ind), l.1296-1330 (F-mono);
REVIEW_RLARGE_V3.md l.1-30, l.200-300 (§3.3 FI-1, §3.4 K12, Part 4); REVIEW55_HWPLD.md header and F6, r55h-37/38;
checks/p4_criteria.md and p4_out.txt (section E). PROOF.md only l.18 and l.88 (by grep).
**Not read:** EXISTENCE.md, BFT_A/B, SQ, SF (except the C_Ω definition line, SF l.2073, by grep). FLOW55.md does not exist at
00:31Z (checked by `ls`); re-checked before finishing (§3.5).
**Line numbers.** RLARGE.md is unmodified since 08:03 local, so the RLARGE line numbers the task quotes (l.192-201, l.618) are
current: the (RLF-δ) block is l.192-202, "Coupling ceilings from this file" is l.615-620 and the sentence "RLF's own ceilings
do not bind" is on l.618. W-cb's a_cb is RLARGE l.442-443 and HW l.214-227.

**Organisation.** §1-§3 are the hand derivations for U1, U3 and FI-1, written before any check of mine existed; they carry the
exact statements the DAG check cites. §4 is the check record (criteria written before each script). §5 gives the verdicts,
with the numbers from §4. §6-§8 are the review files used, the summary table, and the note to the lead.

---

## 1. U1 — a_ret and a_A (derivation)

### 1.1 What a_ret is, by definition chain (not by guess)
- RLARGE §1.2 (RLF-0), l.192-196: |c̄_0^{sea}| + |δβ_k| ≤ Cg_k^{-p}e^{-a_ret/g_k²} with "p a fixed power; PLD Proposition W1R gives
  p = 6 + p(SC)", and "a_ret denotes the exponent of the returned-cluster bounds of (W1-ret′^J)_k (a)-(b) … no source states its
  value".
- PLD Proposition W1R (l.487-491): (W1-ret′)_k (a)-(b) ⇐ (SC)_k + (SF-irr)_{k+1}, with c̄_0^{sea} := Σ_{X∋0}𝓗^{sea}_X(1)/|X|,
  δβ_k^{sea} := 2N(1/6)Σ_{X∋0}tr t^{𝓗_X}/|X|, and |c̄_0^{sea}| + |δβ_k^{sea}| ≤ C′g_k^{-6-p}e^{-a/g_k²}; the "a" is (SC2)'s exponent
  (PLD l.485: "(SC2) Σ_{X∋x}sup_{chart}|∂^q𝓗^{sea}_X|e^{κ_dd(X)} ≤ Cg_k^{-p}(Λ/g_k²)^qe^{-a/g_k²} for q ≤ 3").
  So **a_ret ≡ (SC2)'s exponent a** (the same object; REVIEW_RLARGE_V3 §3.4 reached the same identification).
- **Domain.** (SC2) is a sup over the chart, and both counterterms are read at V = 1 (the "(1)" in c̄_0^{sea}'s definition;
  δβ_k^{sea} is the GT-lat′ quadratic coefficient at V = 1), which lies in every chart {ε_2(V) ≤ r}. Hence **Proposition CC**
  (PLD §16.8: no uniform a_ret on the full cut-good domain; frozen part PROVEN, sea part ARGUED) **does not reach (RLF-0) or
  (RLF-δ)**; it reaches only (RLF-2)'s remainders off the chart ((SF-irr^off), PLD §16.9), which is not U1.
- **The only candidate value in the lane** is PLD §16.8 (l.1550): **a_ret^{PLD} := min{κε_1²/(2048N), 49η_q²/(1024σ_fl²),
  κε_loc²/(64N)}**, the per-cube prices of the three returned families on the chart ((α) quiet collar-good bad cluster, CL^J (c);
  (β) non-quiet sea cube, PLD-desc at τ = η_q with HS-net; (γ) collar-mismatch cube, Lemma KN at t = ε_loc/4), "conditional on
  (SC)_k; (SC)_k's cluster expansion may lose a fixed factor". Reading: a cluster expansion whose per-cube activities are
  ≤ (C e^{-a_ret^{PLD}u})^{|X|} yields (SC2) with any exponent a′ < a_ret^{PLD} (at a larger C and a smaller coupling ceiling).
  So, conditional on (SC)_k being proven that way, **a_ret may be taken as any fixed number in (0, a_ret^{PLD})**; a_ret^{PLD} is
  a supremum, not a value.
- **Inputs this choice puts on the (RLF-0)/(RLF-δ) path** (all upstream of g_0): (SC)_k [HYPOTHESIS]; the (β) entry's
  PLD-desc ⇐ (SG^{fl})_k at τ = η_q on the chart (so RLARGE row 7's "not consumed by the HW route" stops being true for
  (RLF-0)/(RLF-δ) once a_ret := a_ret^{PLD}); (BG)_k's curvature clause at near-trivial V (PLD §16.9, "restricted form";
  REVIEW_RLARGE_V3 §3.4 predicted this return); σ_fl at level k (N5 level-uniformity ⇐ BFT; SMALLNESS_DAG §4.3's weak seed).
  σ_fl² = 16(1 + O(α_*))/λ_min is "the Gaussian part only" (PLD l.1552-1553): the O(α_*) correction is not bounded in any source
  I read. λ_min ≥ 3.17·10⁻³ is the adopted class value ([SF7-edit]; SMALLNESS_DAG §9 on REVIEW55_LEAD H7).
- **Which entry binds, and a_ret^{PLD}/a_bad:** computed exactly in check ru55_3 (§4.3).

### 1.2 (RLF-δ)'s γ_0 exists for every a_ret > 0 — elementary
Put P := 12 + p(SC) (so Cg^{-p}e^{-a_ret/g²} ≤ g⁶ with p = 6 + p(SC) reads Cg^{-P}e^{-a_ret/g²} ≤ 1) and t := 1/g². The condition is
φ(t) := a_ret·t − (P/2)·ln t − ln C ≥ 0. φ is convex, φ′(t) = a_ret − P/(2t) > 0 for t > P/(2a_ret), and φ → +∞. Since
ln t < √t for every t > 0 (the maximum of ln t − √t is ln 4 − 2 < 0, at t = 4), φ(t) ≥ a_ret·t − (P/2)√t − ln⁺C, which is ≥ 0 for
**√t ≥ s_0 := [P/2 + (P²/4 + 4a_ret·ln⁺C)^{1/2}]/(2a_ret)**; s_0² ≥ P/(2a_ret), so φ ≥ 0 on all of [s_0², ∞). Hence
**γ_0 := 1/s_0 > 0 works for every g ∈ (0, γ_0]**, and γ_0 depends on (a_ret, C, p) only: it is g-independent, and K-, T-independent
exactly when a_ret, C, p are. This is all that "existence of (RLF-δ)'s γ_0" needs; the value of a_ret matters only for the
magnitude of γ_0 (SMALLNESS_DAG §8.3).

### 1.3 RLARGE l.618 for (RLF-δ): what the sentence asserts, exactly
l.615-618 says HIST-sum's, REL-seq's and (RLF-δ)'s smallness conditions "all have the form e^{-a/g²} ≪ (polynomial and C_ℓ
factors)^{-1}" and that their ceilings lie "far above the binding DX′ ceiling g_0² ≲ 2.5·10⁻¹⁵²/C_Ω". For (RLF-δ) the exponent is
a_ret, not a (REVIEW55_ARS F03). By §1.2's monotonicity, "(RLF-δ) does not bind at DX′" is **equivalent** to φ(t_DX) ≥ 0 at
t_DX := C_Ω/(2.5·10⁻¹⁵²) (given t_DX ≥ P/(2a_ret), true at every value below), i.e.
  **(L618-δ):  ln C + ((12 + p(SC))/2)·ln(C_Ω/(2.5·10⁻¹⁵²)) ≤ a_ret·C_Ω/(2.5·10⁻¹⁵²).**
C and p(SC) are (SC)_k's constants, which no source states. So l.618 for (RLF-δ) is a statement about (SC)_k's constants. Its
budget at a_ret = a_ret^{PLD} is computed in ru55_3; C_Ω := C + 3(N² − 1)/2 (SF l.2073) enters with a positive power on the right
and only logarithmically on the left, so the worst case is the smallest admissible C_Ω.

### 1.4 What a_A is, and the four routes that give it a formula
- **Definition.** a_A is the exponent of (SDP)^A (RLARGE l.408-410; HW l.937: "μ(S ⊂ D_k) ≤ (C_Ae^{-a_Au_k})^{|S|}·exp(c_A·shadow
  sums), a_A ≥ θa_bad"), with the rule "If a_A < θa_bad, θ is lowered to a_A/a_bad and nothing else changes" (HW l.941). (SDP)^A is
  OPEN [P, node A]. So a_A has no value until (SDP)^A is proven; what exists are four conditional routes in PLD, each with an
  explicit formula (bad-only defects, SU(2), ε_1 ≤ min{1/(4A_d), t_pr}, λ ∈ (0, 1) free):
  - **(i) PLD §16.5, NA-PRICE (i)** (l.1416): a_A = min{λκε_1²/256, 6θa_bad, a_ns}; "a_ns ≥ θa_bad by hypothesis" of (J-NS^dir):
    "This puts the whole K12 content into the hypothesis a_ns ≥ θa_bad of (J-NS^dir); it is not an output."
  - **(ii) PLD §17.4, NA-PRICE^E (i)** (l.1856, l.1908-1913): a_A = min{λκε_1²/256, 6θa_bad, a_cd}; a_A ≥ θa_bad ⟺ a_cd ≥ θa_bad;
    fallback θ ≈ a_ret/a_bad if the centre-defect price is only threshold-type.
  - **(iii) PLD §18.7, NA-PRICE^{E+} (i)** (l.2485): **a_A = min{λκε_1²/256, 6θa_bad}**, "a_A ≥ θa_bad unconditionally"; conditional
    on (CLS-min) + (CEM^{COL})_k. REVIEW55_HWPLD (Opus 5.5): the implication is CONFIRMED (r55h-38) but **(CEM^{COL}) is FALSE as
    quantified** (F_< universally quantified; r55h-18, F6), so the implication is vacuous until F_< is restricted.
  - **(iv) PLD §19.8, route (ρ2)** [ARGUED in file; REVIEW55_HWPLD r55h-37: NOT-VERIFIED]: the same formula with θ ≤ 1/(24·5^d)
    = 1/15000 (PLD l.3482).
- **Re-derivation of (iii)'s "a_A ≥ θa_bad".** 6θa_bad ≥ θa_bad is trivial. At ε_1 < t_pr, a_bad = c_prε_1², so
  λκε_1²/256 ≥ θa_bad ⟺ **κ ≥ 256θc_pr/λ**; at θ ↑ 1/24, λ = ½ this is κ ≥ 64c_pr/3 = 1/84270 (exact, c_pr = 1/1797760; ru55_3),
  so it holds at both of PROOF's example values κ ∈ {1, ¼}. At θ = 1/24, κ = 1, λ = ½: a_A/a_bad = min{1/(512c_pr), ¼} = ¼.
- **So, U1's second question ("whether a_A ≥ θa_bad"):** on every route the only way a_A < θa_bad can happen is through a
  **θ-free** entry (λκε_1²/256, a_ns or a_cd) falling below θa_bad; the θ-dependent entry 6θa_bad never does. Whether it happens
  is route-dependent and is not established: (i) assumes it; (ii) leaves it as the open inequality a_cd ≥ θa_bad; (iii)/(iv)
  give it for κ ≥ 256θc_pr/λ from a hypothesis that is false as quantified (iii) or an ARGUED route (iv).

### 1.5 θ ↔ a_A: a literal 2-cycle, and why it is not a real one
Route (iii)'s formula makes a_A depend on θ (the 6θa_bad entry), while HW's rule makes θ depend on a_A. Encoded literally this
is a 2-cycle θ → a_A → θ in the constants graph (to be exhibited by ru55_2, variant V3). It is broken by the following order,
which is what the formulas actually say: since 6θa_bad > θa_bad for every θ > 0, the lowering rule never reads the 6θa_bad
entry. Put **a_A° := the θ-free entries of the route's a_A (min{λκε_1²/256, a_ns or a_cd where present})**; then
**θ := min{θ_cap, a_A°/a_bad}** (θ_cap the CAP-1 choice), then a_A := min{a_A°, 6θa_bad} ≥ θa_bad, then a = θa_bad.
Order: (κ, λ, ε_1, c_pr, the route's θ-free entries) → θ → a_A → a. The θ-dependence of c_sf / c_cem (rate 24θ) and through it
of C_A and C_fc runs forward from θ and closes nothing. (ru55_2, variant V4.)

### 1.6 The "+63.6 decades" figure
It is log10((a/10²)/DX′) at a = a_bad/24, DX′ = 2.5·10⁻¹⁵² (REVIEW55_ARS F04: +63.619267), i.e. route (iii)'s θ ↑ 1/24, with
a_A ≥ θa_bad, C_Ω = 1, and l.617's form "g_K² ≲ a/10²". Three of its assumptions are not the live state: (a) θ is
route-dependent (§1.4: 1/24, 1/15000, or a_ret/a_bad on (ii)'s fallback); (b) l.617's "a/10²" drops HIST-sum's factor
e^{38417B_0} (REVIEW_RLARGE_V3 Part 4 and fix N3-3: with HW's B_0 := B_1 + c + 1 ≥ 1 the ceiling is a/(ln 12800 + ln C_ℓ + aR +
38417B_0) ≈ 2.70·10⁻⁹¹ at B_0 = 1, not ≈ 10⁻⁸⁸); (c) RLF's lowest own ceiling is (RLF-δ)'s (§1.3), not HIST-sum's. The
re-evaluated margins are in ru55_3. PROOF.md l.18 ([S26-REVIEW]) already calls +63.619 "an upper benchmark … not a margin".

---

## 2. U3 — the (TC) window (derivation)

### 2.1 (TC) as written is infeasible, and no ε_loc repairs it
On the live branch (ε_1 ≤ 256Nδ_0, Nb_1 ≥ 4) RLARGE's ε_loc (frozen CL: ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}}) is
ε_1/(2√(Nb_1)) and RS-lin's η_q is ε_1/(256NA_d), so (TC) ε_loc/2 ≥ (16N + 3)A_dη_q reads R ≤ 1 with
  **R² := ((16N + 3)A_dη_q/(ε_loc/2))² = (16N + 3)²·b_1/(4096N)**   (b_1 = n_P + 12κ(1 + A_d)² = 1296 + 1200κ at d = 4, L = 3),
a rational number, so the verdict needs no square root (ru55_1). U3's proposed fix "adopt ε_loc ≥ (16N + 3)ε_1/(128N)"
contradicts CL (c)'s requirement b_1(ε°)² ≤ ε_1²/(4N) for every ε° ≤ ε_loc exactly when R > 1. And CL (c) cannot be relaxed by
more than √2: its numerator gives the exponent |Y|ε_1²/(2N), so even giving the whole of it away allows only ε_loc <
ε_1/√(2Nb_1), and R/√2 > 1 at every grid point (ru55_1 G2). **So U3 is settled negatively on the ε_loc side**; the repair must
act on the quiet side of W-cb's case split.

### 2.2 Lemma W-cb♯ (the repair). Statement and proof
**Lemma W-cb♯ (CONDITIONAL ⇐ (CLS-min); no (TC)).** Setting, notation and reading of σ_Q exactly as HW Lemma W-cb (HW l.214-227):
Q a level-(k+1) cube, X^cb_Q := κu_kΦ_{C(Q)}(U, V) + u_kΣ_pℰ_p(U) (p over the level-k plaquettes in the column of N_1(Q)), collar
threshold t := ε_loc/2 (any t > 0 works). Put
  **η* := min{η_q, ε_loc/(2(16N + 3)A_d)}**   (in general η*(t) := min{η_q, t/((16N + 3)A_d)}).
Then on {Q collar-bad or non-quiet}: X^cb_Q ≥ a_cb♯·u_k with
  **a_cb♯ := min{c_pr·min{ε_loc²/4, t_pr²}, κε_loc²/(64N), c_pr·min{η*², t_pr²}}**,
and X^cb_Q ≤ κu_kΦ_{C(Q)} + 24u_kF^col_{N_1(Q)} (unchanged). If (TC) holds then η* = η_q and a_cb♯ = HW's a_cb.
*Proof.* Non-quiet and (α): verbatim HW (TE (ii) at level k, or (B) at k = 0, gives ℰ_p ≥ c_pr·min{η_q², t_pr²} resp.
c_pr·min{ε_loc²/4, t_pr²}; both are ≥ a_cb♯ since η* ≤ η_q). (β): some c ∈ C(Q) has ||V_c − S_c(U)|| > t. Let η_c be the largest
||1 − U_p|| over the level-k plaquettes of c's two endpoint blocks (the plaquettes RS (R1) uses for c).
 (β1) η_c ≥ η*: that plaquette lies in the column of N_1(Q) (HW's reading "C(Q) and the endpoint blocks of its links inside
 N_1(Q)" — the same inclusion HW's own proof uses in "If a block is not quiet, the non-quiet case applies"), so TE (ii) at level k
 (k = 0: (B)) gives X^cb_Q ≥ u_kℰ_p ≥ u_kc_pr·min{η*², t_pr²} ≥ a_cb♯u_k.
 (β2) η_c < η*: RS (R1) gives δ := ||M̄_c − S_c|| ≤ A_dη_c < A_dη* ≤ A_dη_q ≤ δ_0 (η_q ≤ δ_0/A_d by its definition), so Lemma PM
 gives ||W_0 − S_c|| ≤ 3δ and ||M̄_c − W_0|| ≤ 4δ. With δ < A_dη* ≤ t/(16N + 3): x := ||V_c − W_0|| > t − 3δ > 16Nt/(16N + 3) ≥
 max{16Nδ, t/2} (the last because 32N ≥ 16N + 3). Lemma KQ (lower), with ||M̄_c||_op ≤ 1: φ_c ≥ x²/(2N) − 4δx ≥ x²/(2N) − x²/(4N)
 = x²/(4N) ≥ t²/(16N) = ε_loc²/(64N); so X^cb_Q ≥ κu_kφ_c ≥ u_kκε_loc²/(64N) ≥ a_cb♯u_k.
 Upper bound: TE (iii), unchanged. ∎
*What it uses that HW's proof does not:* nothing. It uses the same lemmas (TE, RS (R1), PM, KQ) and the same geometric inclusion,
and replaces the hypothesis (TC) by a case split at η* inside the quiet case. Theorem HW's collar extension (HW l.313-315) then
runs verbatim with a_D♯ := min{a_bad, a_cb♯} and without "(TC) added".

### 2.3 What W-cb♯ changes, and what it leaves alone
- **Changed:** W-cb's output exponent: a_cb → a_cb♯, the third entry c_pr·min{η_q², t_pr²} → c_pr·min{η*², t_pr²} = (third entry)/R²
  when η_q ≤ t_pr (true at every live ε_1, since ε_1 < t_pr); a_D := min{a_bad, a_cb} → a_D♯; the collar family's price
  e^{-θ_cb a_D♯(u_j − R)} with θ_cb < 1/(96·82); and, if the collar family is included in the history (SMALLNESS_DAG edge
  "a_D → a"), every consumer of a downstream (n_H, n_♯, W, ε_♯, C_H, the g_0 ceilings) — magnitudes only. Which a_cb♯ entry binds,
  and a_cb♯/a_bad, are computed in ru55_1 G4.
- **Unchanged:** ε_1, η_q, ε_loc, Proposition CL, CL^J, RS-lin, Lemma 7.2-0^J (ε^J_♮), the definition of "non-quiet"
  (RLARGE l.297 still at η_q), the collar rule σ_Q, a_bad, a_A, a_ret, θ for bad defects.
- **Removed:** (TC) as a hypothesis everywhere it appears (RLARGE l.82-86, §1.1 [v3-cb], §2.3 table, §3.6, §4.2 rows 10f and 20,
  §7, K15, U3; HW W-cb, Theorem HW's collar extension, §19 Scope).

### 2.4 SMALLNESS_DAG's form of the repair (lower the quietness threshold to η′ ≤ η_q/R) — valid, but it touches more
Lowering the quietness threshold itself to η′ := η_q/R (SMALLNESS_DAG §8.1) makes (TC) hold with equality and gives the same
a_cb. But "quiet" is a shared definition, so the change also reaches: (a) RLARGE l.297 (more cubes non-quiet, hence collar-bad);
(b) CL^J (c)'s hypothesis "every Q ∈ Y is quiet" — harmless (η′-quiet ⇒ η_q-quiet, RS-lin's hypotheses only strengthen);
(c) Lemma 7.2-0^J's ε^J_♮ ≤ min{η′/2, ε^J_loc/C_♭} — whether the first entry becomes binding is checked in ru55_1 G6;
(d) **a_ret^{PLD}'s binding (β) entry** (non-quiet sea cubes priced at the quietness threshold: a_fl(η′/2) = a_fl(η_q/2)/R²), and
through the K12 fallback θ ≤ a_ret/a_bad on route (ii), θ and a. W-cb♯ gets the same a_cb with none of (a)-(d). ru55_2 compares
the two encodings (variants V1, V2).
**Joint collar (K2, open).** If the still-unstated σ^J_Q uses ε^J_loc/2 (ε^J_loc := ε_1/(157(1 + A_d)√N)) as its coarse-link
threshold, the factor is R^J := (16N + 3)A_dη_q/(ε^J_loc/2) instead of R (ru55_1 G7); W-cb♯ covers any t.

---

## 3. FI-1 — the coupling fixed point (derivation)

### 3.1 The structure: one scalar equation per level, solved forward
- In W the kernel couplings are parameters (RLARGE §0: "The kernel couplings u_i are parameters of W"); K_i carries κu_i.
  Because ∫K_j dU_{j+1} = 1, the U_{k+1}-marginal of W involves only K_0, …, K_k. But stage k's R-operation reads one more kernel:
  CL^J's w^J_B contains the factors k^{(k+1)}_{c′}(U_{k+2}(c′); M̄_{c′}(U_{k+1})), c′ ∈ C(B) (HIST §4), with U_{k+2} as frozen data;
  no later kernel is read. So stage k's effective output (FLOW Def F-g) is a function
  **u_{k+1}^{eff} = Φ_k(x) := u_k − b_k − ρ_k(x),  x := u_{k+1}^{ker}**,
  of the (A5-consistent) past u_0, …, u_k and of the single next kernel parameter x; b_k is the one-loop number of step k (it
  involves K_k and the level-k action only, not x), and ρ_k = −β[ΣE^{≥2}_k] + δβ_k (FLOW Prop. F-rem, corrected sign).
- A5 ("the chain's own sequence": kernel = effective) is therefore **x = Φ_k(x) at each level, given the past** — a forward,
  per-level scalar fixed point (REVIEW_RLARGE_V3 §3.3's reading; "not a global fixed point on [0, K]").

### 3.2 Theorem FI-1 (per-level existence). Statement and proof
**Hypotheses.** FLOW's (UNIV-1L) (|B_n − β_0'n log L| ≤ R_0, B_n := Σ_{k<n}b_k, R := 2R_0) and its order of constants (β_-, R, then
C_ρ, then γ). Put **X_k := [u_k − (3/2)β_0'log L − R, u_k + R]** (the one-step window) and **x_lo := max{2R, 2/min{1, κ}}**
(Option A's g_{k+1}² ≤ 1/(2R) and CL^J's restated Setting g_{k+1} ≤ min{1, √κ}/√2). Assume
- **(A-unif)** [Option A's own content, with its quantifier written out]: for every k, every A5-consistent past with
  g_0, …, g_k ≤ γ and every kernel parameter x ∈ X_k, stage k is defined and obeys F-rem's bound |ρ_k(x)| ≤ C_ρg_k² with
  x-independent C_ρ (the stage constants bounded via 1/g_{k+1}² ≤ 1/g_k² + R and the lower end of the bracket);
- **(A-cont)** x ↦ ρ_k(x) is continuous on X_k;
- **γ:** C_ργ² ≤ ½β_0'log L (FLOW) and **γ^{-2} ≥ max{2R, 2/min{1, κ}} + R + (3/2)β_0'log L** (new; it only keeps X_k inside
  Option A's bracket).
**Claim.** For every k and every A5-consistent past with g_0, …, g_k ≤ γ, the equation x = Φ_k(x) has a solution x* ∈ X_k, and the
extended sequence obeys (F_R) on [0, k + 1] (Theorem F-flow).
*Proof.* (UNIV-1L) at n = k and k + 1 gives |b_k − β_0'log L| ≤ 2R_0 = R. With |ρ_k(x)| ≤ C_ρg_k² ≤ C_ργ² ≤ ½β_0'log L:
b_k + ρ_k(x) ∈ [½β_0'log L − R, (3/2)β_0'log L + R] for every x ∈ X_k, so Φ_k(X_k) ⊂ [u_k − (3/2)β_0'log L − R, u_k + R − ½β_0'log L]
⊂ X_k. Also X_k ⊂ [x_lo, u_k + R] because u_k ≥ γ^{-2} and the γ condition, so (A-unif) is used only inside Option A's bracket.
f(x) := Φ_k(x) − x is continuous on X_k, f(left end) ≥ 0 and f(u_k + R) ≤ −½β_0'log L < 0; the intermediate value theorem gives
x*. At x*, u_k − u_{k+1} = b_k + ρ_k(x*) with |ρ_k(x*)| ≤ C_ρg_k², which is all Theorem F-flow uses. ∎
**Corollary (sequence).** By induction on k (choosing one solution per level), every bare coupling whose sequence stays in
(0, γ] has an A5 sequence; constants never depend on the choice (by (A-unif) they are fixed before any x).

### 3.3 Uniqueness, and what F-tune needs
FLOW's F-tune uses (SF-cont): g_0 ↦ u_{k+1}(g_0) continuous — which presupposes that the sequence is a function of g_0. With
several solutions per level, a selection (e.g. the smallest) is only lower semicontinuous in the past and can jump, so (SF-cont)
for the A5 sequence is not automatic (ru55_4 builds an explicit continuous family where the smallest fixed point jumps).
- **(A-Lip)** |ρ_k(x) − ρ_k(x′)| ≤ q|x − x′| on X_k with q < 1, and ρ_k jointly continuous in (past, x). Then Φ_k maps X_k into
  itself and is a q-contraction, so x* is unique and depends continuously on the past (|x*(p) − x*(p′)| ≤ (1 − q)^{-1}·
  sup_x|ρ_k(p, x) − ρ_k(p′, x)|); by induction u_K(g_0) is continuous on the admissible set and **F-tune's proof applies verbatim
  to the A5 sequence**.
- **(A-an) ⇒ (A-Lip):** if for every real x_0 ∈ X_k, ρ_k extends holomorphically in x to the disc |x − x_0| < r with |ρ_k| ≤ C_ρg_k²
  there and r ≥ 2C_ρg_k², Cauchy's estimate gives |∂_xρ_k| ≤ ½ on X_k, i.e. q = ½. (The radius asked for is tiny: relative to
  x_0 ≳ γ^{-2} it is ≲ 2C_ργ⁴.) Every place where x enters explicitly is a normalised kernel factor e^{-κxφ}/∫e^{-κxφ} with
  x-independent indicators, entire in x and with a non-vanishing normaliser for |Im x| < π/(4κ) (φ ∈ [0, 2]) [inference: that
  node A's full stage-k output inherits this is not written anywhere].
- Without (A-Lip), F-tune can still be recovered from (A-cont) by a continuation argument (Tietze-extend each Φ_k off the A5 set,
  apply Browder's theorem on the connected fixed-point set of a one-parameter family of self-maps of a box) — **ARGUED here, not
  written out.**

### 3.4 Acyclicity and uniformity
- No constant reads the fixed point: by (A-unif) all stage constants are fixed on X_k before x is chosen, and C_ρ, R, β_±, γ are
  fixed in F-ind's order. The new γ condition reads only R, κ, β_0', L — all fixed before γ — so it adds the edges R → γ, κ → γ,
  L → γ to SMALLNESS_DAG's graph (ru55_2, variant V5); expected: no cycle. The fixed point itself lives in the coupling layer
  (SMALLNESS_DAG's kernel_seq / eff_seq), after g.
- K and T enter nowhere: Φ_k is a level-k object; R, β_0', C_ρ, γ are K-, T-independent (FLOW). The torus enters only through
  δβ_k ⊂ ρ_k, whose torus-independence above the wrap levels is U5 — a property of ρ_k, not of the fixed-point argument.

---

## 4. Check record (criteria always written before the script; exact rational arithmetic; every run exit 0, empty stderr)

| id | criteria (UTC) | script → output | what it decides | result |
|---|---|---|---|---|
| ru55_1 | ru55_1_criteria.md (00:34Z; its header says 00:36Z — wrong, corrected in the file by an appended line) | ru55_1_tc.py → ru55_1_out.txt | U3: (TC) as written, U3's own fix vs CL (c), W-cb♯'s inequality chain, a_cb♯'s entries, a_D♯, ε^J_♮ under the quietness form, joint factor | all gates PASS; controls C1-C3 fire |
| ru55_2 | ru55_2_criteria.md (00:36:01Z) | ru55_2_variants.py + ru55_2_dag.py → ru55_2_out.txt | DAG variants V0-V6 with SMALLNESS_DAG's own checker functions (read-only import) | all pre-registered verdicts PASS; checker controls C1-C7 fire on V6; driver controls C-A, C-B, C-C fire |
| ru55_2b | ru55_2b_criteria.md (after reading CODEX_REVIEW_DAG) | ru55_2b_dag.py → ru55_2b_out.txt | Codex's omitted edge n_♯ → (SC)_k: is a_ret in the cutoff loop on every route? | Codex's 14-node SCC reproduced; claim TRUE; control fires |
| ru55_3 | ru55_3_criteria.md (00:38:05Z) | ru55_3_u1.py → ru55_3_out.txt | U1: a_ret^{PLD}'s binding entry and ratio, the (L618-δ) budget, (RLF-δ) ceilings, the "+63.6" family, route (iii)'s κ threshold | all gates PASS; K1-K3 fire; **K4 reported False — a defective criterion** (below) |
| ru55_3b | ru55_3b_criteria.md (written after ru55_3 ran, before its script) | ru55_3b_lncheck.py → ru55_3b_out.txt | replaces ru55_3's K4: certifies the rigorous log enclosures | L1-L3 PASS, L4 fails as designed: enclosures CERTIFIED |
| ru55_4 | ru55_4_criteria.md | ru55_4_fi1.py → ru55_4_out.txt | FI-1: window invariance at its extremes; tightness of the γ condition; (A-Lip) load-bearing | all PASS; F2-C fires |

**Disclosures.** (1) ru55_3's control K4 asked the ln 10 enclosure (width 4·10⁻⁴⁵) to contain 2.302585092994045684, which is
an 18-digit *truncation* lying 1.8·10⁻²⁰ below ln 10 = 2.302585092994045684017991…; a correct enclosure cannot contain it.
The 20-digit display "2.30258509299404590109" in ru55_3_out.txt is a float-conversion artifact (the nearest double). Neither
criteria nor script was edited; ru55_3b (new id, criteria first) certifies the enclosures with a correct window and an
independent route (3 ln 2 + ln(5/4)). Every ru55_3 verdict therefore stands. (2) ru55_4 F4's steep family has |ρ| ≤ ε + 10⁻⁶ at
s = a + 10⁻⁶ (the criteria file says ≤ ε); immaterial (the jump, 4.0·10⁻³, exceeds ε = 3·10⁻³; shrinking a by 10⁻⁶/3 restores
|ρ| ≤ ε with the same jump to 10⁻⁶) — not re-run. (3) ru55_2b was designed after reading CODEX_REVIEW_DAG §3.1; its criteria
state that. (4) No float enters any verdict; every decade figure below is a rigorous rational enclosure (ru55_3 + ru55_3b).
(5) The DAG variants test the encoded graph only; an edge nobody encoded is invisible to them (CODEX_REVIEW_DAG §4 makes the
same point about the checker, and I agree).

**Can each gate fail?** ru55_1 G1 can output HOLDS (C1 does, at ε_loc := ε_1/4); G3 can fail (C2 does, at twice the δ
supremum); G4's equality test separates R from R² (C3). ru55_2: the literal route-(iii) graph V3 does produce a B-strict
cycle (C-A), an injected back-edge through η* is seen (C-B), and a K tag on η* reaches g_0 (C-C). ru55_3: P = 10⁶² violates
(L618-δ) (K1); B_0 moves the margin by 2.57 decades (K2); λ = 10⁻⁶ flips a_A's binding entry (K3). ru55_4: γ^{-2} one unit
below the condition breaks the lower end (F2-C).

---

## 5. Findings (verdict per claim; file + locating string; derivation or reason)

### U1 — a_ret, a_A, and RLARGE l.618 for (RLF-δ)

**ru55-U1a — "a_ret … no source states its value" (RLARGE l.195-196): CONFIRMED as of RLARGE v3's input freeze (09:37 UTC); now
STALE.** PLD §16.8 (session 4, written from 10:16 UTC, after the freeze) states a conditional candidate. Not a counted item.

**ru55-U1b — a_ret is (SC2)'s exponent, and Proposition CC does not reach (RLF-0)/(RLF-δ): CONFIRMED** (§1.1; W1R reads both
counterterms at V = 1 and (SC2) is a sup over the chart). REVIEW_RLARGE_V3 §3.4's identification: agree. New: Proposition CC
is not an obstruction for (RLF-δ).

**ru55-U1c — PLD §16.8's a_ret^{PLD} := min{κε_1²/(2048N), 49η_q²/(1024σ_fl²), κε_loc²/(64N)}: arithmetic CONFIRMED; status
CONDITIONAL.** ru55_3 U1-1: the (β) entry 49η_q²/(1024σ_fl²) binds at all 24 grid points (N ∈ {2, 3}, κ ∈ {1, ¼}, λ_min ∈
{3.17·10⁻³, 4.23·10⁻³, 6.6·10⁻¹⁰}) by ≥ 5 orders; a_ret^{PLD}/a_bad = 43632197/54358179840000 = 8.0268·10⁻⁷ (N = 2) and
3.5675·10⁻⁷ (N = 3) at λ_min = 3.17·10⁻³ (κ-independent, since the binding entry is); 1.0711·10⁻⁶ / 4.7604·10⁻⁷ at 4.23·10⁻³;
the L0-1 sensitivity factor is exactly 158500000/33 = 4.8030·10⁶. PLD p4 E2's printed values reproduce (U1-2). Status: a
supremum for (SC2)'s exponent, CONDITIONAL on (SC)_k [HYPOTHESIS], on (SG^{fl})_k at τ = η_q on the chart (via PLD-desc), on
(BG)_k's curvature clause at near-trivial V, and on a level-k bound for σ_fl (N5 level-uniformity ⇐ BFT); σ_fl's O(α_*)
correction is unbounded in every source I read. **Consequence for RLARGE §4.2:** row 7 ("(SG^{fl})_k … not consumed by the HW
route") and row 8 ((BG)_k "load-bearing only for (SG^{fl})/PLD-desc") are not true for (RLF-0)/(RLF-δ) once a_ret := a_ret^{PLD}
— both re-enter through row 2 (PLD §16.9 says so; REVIEW_RLARGE_V3 §3.4 predicted it).

**ru55-U1d — (RLF-δ)'s γ_0 exists for every a_ret > 0: CONFIRMED (PROVEN here, §1.2, with erratum E1).** γ_0 = 1/s_0 explicit
in (a_ret, C, p); g-independent; K-, T-independent exactly when (a_ret, C, p) are. CODEX_REVIEW_DAG edge 114 ("any fixed
positive a_ret gives a sufficiently small ceiling"): agree.

**ru55-U1e — RLARGE l.618 "RLF's own ceilings do not bind", for (RLF-δ): NOT-VERIFIED, reduced to one explicit inequality.**
By §1.3 the sentence is equivalent to (L618-δ): ln C + ((12 + p(SC))/2)·ln(C_Ω/(2.5·10⁻¹⁵²)) ≤ a_ret·C_Ω/(2.5·10⁻¹⁵²), with C, p(SC)
the constants of (SC)_k, which no source states (that is the missing input). ru55_3 U1-3 (rigorous): at a_ret ↑ a_ret^{PLD},
ε_1 = 6.7·10⁻⁴⁰, N = 2, λ_min = 3.17·10⁻³, C_Ω = 1, the budget is 8.0172·10⁶⁰ and ln t_DX = 349.0766, so (L618-δ) holds for
every p(SC) ≤ 4.59·10⁵⁸ (ln C = 0), every ln C ≤ 8.0·10⁶⁰ (p(SC) = 0), and jointly at (12 + p(SC), ln C) = (10⁵⁸, 10⁶⁰); at N = 3
the budget is 3.5632·10⁶⁰; under the L0-1 sensitivity value 1.6692·10⁵⁴ (still holds at (10⁵¹, 10⁵³)); a larger C_Ω only helps.
(RLF-δ)'s ceiling itself (U1-4): g² = 1.029·10⁻⁹⁴ … 7.561·10⁻⁹⁵ at PLD's sample constants (p(SC), ln C) ∈ {6, 12} × {0, 50}
(+57.48 to +57.61 decades over DX′ at C_Ω = 1; PLD p4 E3 reproduced) and 1.12·10⁻⁹⁶ (+55.65) at an ILLUSTRATIVE (702, 10⁵). So the
sentence is true unless (SC)_k's constants are astronomically large (≳ 10⁵⁸), which nothing in the lane suggests but nothing
states; and per SMALLNESS_DAG §8.3 the comparison decides nothing about truth. Two corrections to l.615-617 that do hold:
(i) for (RLF-δ) the exponent is a_ret, not a, and the condition carries a log factor (Cg^{-(12+p(SC))}e^{-a_ret/g²} ≤ 1), so its
ceiling is a_ret/(ln C + ((12 + p(SC))/2)ln(1/g²)), not a/10² — REFUTED as written (REVIEW55_ARS F03 found the exponent; agree);
(ii) **(RLF-δ)'s ceiling is the lowest of RLF's own ceilings** (≈ 10⁻⁹⁴ against HIST-sum's 2.70·10⁻⁹¹), so l.617's
"g_K² ≲ a/10² ≈ 10⁻⁸⁸" names neither the binding RLF condition nor its value — REFUTED as written. Collision note: C here is
(SC)_k's prefactor; SF's C inside C_Ω := C + 3(N² − 1)/2 (SF l.2073) is a different object (the TILT determinant constant).

**ru55-U1f — "+63.619 decades" (ARS_BIND A7; PROOF [S25-fix 4]; SESSION25_RESULTS l.578 "THE LIVE EXPONENT … CLEARS DX′ BY
+63.619 DECADES"): arithmetic CONFIRMED at its inputs; as the live margin REFUTED.** ru55_3 U1-5 reproduces +63.619267 exactly
for (θ = 1/24, l.617's D = 100, DX′ = 2.5·10⁻¹⁵², C_Ω = 1). Its inputs are not the live state: with HW's B_0 := B_1 + c + 1 ≥ 1
(HW l.671), HIST-sum's ceiling is a/(ln 12800 + 324 ln(4/3) + 38417B_0) = 2.700997·10⁻⁹¹ at θ = 1/24, B_0 = 1 (REVIEW_RLARGE_V3 N3-3's
2.70·10⁻⁹¹ reproduced), margin **+61.034**; with route (iv)'s θ = 1/15000: **+58.238**; with route (ii)'s fallback θ = a_ret/a_bad:
**+56.318**; and the binding RLF ceiling is (RLF-δ)'s (+57.5 to +57.6 at PLD's sample constants, U1-4). All positive (sign gate
PASS); ln C_fc and aR are omitted here as REVIEW_RLARGE_V3 does, and each would lower these figures further. PROOF.md l.18
([S26-REVIEW]) already calls +63.619 "an upper benchmark (θ at its supremum, a_A dropped, C_Ω = 1), not a margin": agree, and
add **"B_0 dropped (l.617's a/10²)"** to its list of dropped inputs.

**ru55-U1g — a_A: definition and the four PLD routes (§1.4): CONFIRMED by reading.** **Route (iii)'s "a_A ≥ θa_bad
unconditionally" (PLD l.2486): CONFIRMED as arithmetic** — κ ≥ 256θc_pr/λ, = 1/84270 exactly at θ = 1/24, λ = ½; a_A/a_bad = ¼ at
κ = 1 with 6θa_bad binding (ru55_3 U1-6) — **but conditional on (CEM^{COL})**, which REVIEW55_HWPLD F6 finds false as
quantified (I did not re-derive F6; I rely on it as an Opus 5.5 review and flag it as such). **U1's question "whether
a_A ≥ θa_bad": NOT-VERIFIED** — assumed on route (i), the open inequality a_cd ≥ θa_bad on route (ii), derived from a hypothesis
false as quantified on (iii) and from an ARGUED route on (iv). On every route the only possible failure is a θ-free entry
falling below θa_bad, and then θ := that entry/a_bad is explicit — so whatever the answer, it costs a magnitude (n_H), never
an existence or an order.

**ru55-U1h — θ ↔ a_A: the literal encoding of route (iii) has a 2-cycle; §1.5's order removes it: CONFIRMED for the encoded
graph.** ru55_2 V3: B-strict SCC [a_A, theta] (C-A fires); V4 (a_A° θ-free → θ → a_A): 0 B-strict SCCs, order a_A° (112) < θ (134) <
a_A (143) < a (144). Side effect: in V4 θ leaves the cutoff (n_♯) SCC (12 → 11 nodes), i.e. on route (iii)/(iv) θ no longer rests
on node A's unstated n_♯-uniformity. **SMALLNESS_DAG §3.3's "a_A does not depend on θ": REFUTED** for PLD's routes (each a_A
formula contains 6θa_bad); harmless once ordered. CODEX_REVIEW_DAG edge 41 ("conditional on a_A having been obtained
independently of this θ"): agree — the condition fails literally on route (iii), and §1.5 is the repair.

**ru55-U1i — Where a_ret sits relative to the cutoff loop: CONFIRMED (ru55_2b).** With CODEX_REVIEW_DAG's omitted edge
n_♯ → (SC)_k (PLD l.378, "𝒢_x := Σ_{N≤n_♯}…"), the cutoff SCC is 14 nodes and contains (SC)_k and a_ret (Codex reproduced, also on
top of my V6); removing route (ii)'s K12 fallback edge a_ret → θ (route (iii)/(iv), where K12 is settled without a_ret, PLD
l.2548-2549) shrinks it to 12, with a_ret and θ outside. So: (SC)_k's cutoff-indexed constants must be n_♯-uniform for (SDP)^A
on every route (Codex's point, agree), but **a_ret needs n_♯-uniformity only on route (ii)'s fallback**; on (iii)/(iv) the order
"n_♯, then (SC)_k at that cutoff, then a_ret(n_♯) > 0, then γ_0, then g_0" is acyclic.

### U3 — the (TC) window

**ru55-U3a — "(TC) fails with RLARGE's own ε_loc by ×19.32 / ×15.45 / ×22.99 / ×18.38" (SMALLNESS_DAG §8.1, dag55_3): CONFIRMED.**
ru55_1 G1, exact: R² = 47775/128, 488775/2048, 33813/64, 345933/1024 (R ∈ [19.319476, 19.319477], [15.448613, 15.448614],
[22.985389, 22.985390], [18.380021, 18.380022]), each equal to the closed form (16N + 3)²b_1/(4096N). CODEX_REVIEW_DAG §6 has the
same four exact squares: agree. Notation: in §2 and here R is the (TC) ratio (SMALLNESS_DAG's R; Codex's R_TC); it is not FLOW's
flow slack R = 2R_0 used in §1 and §3 — I recommend the name R_TC.

**ru55-U3b — RLARGE U3's own fix "adopt ε_loc ≥ (16N + 3)ε_1/(128N) if compatible with CL (c)": REFUTED (incompatible).** ru55_1
G2: incompatible with CL (c) at all four points; also with CL's proof given all of its numerator (√2-relaxed, G2a) and with the
plaquette term alone (b_1 → n_P = 1296, i.e. κ → 0, G2b). Within CL's proof no ε_loc works. RLARGE §0's [hand] sufficient
condition itself (ε_loc ≥ (16N + 3)ε_1/(128N) ⇒ (TC)) is correct algebra (REVIEW_RLARGE_V3 Part 4: agree) but vacuous for CL's ε_loc.

**ru55-U3c — Lemma W-cb♯ (§2.2): CONFIRMED (PROVEN here).** (TC) is removed as a hypothesis; the proof uses only HW's own lemmas
(TE, RS (R1), PM, KQ) and the same inclusion HW's proof uses. ru55_1 G3 checks the inequality chain exactly at the δ supremum
(N = 2, 3), and C2 shows it fails at twice that. Precision note: η_c is the maximum over the level-k plaquettes with all vertices
in B(X) ∪ B(X + e_μ) (straddling plaquettes included — the set RS (R1)'s rectangles use); under HW's reading these lie in the
column of N_1(Q). Valid for every ε_1 (η* := min{η_q, …} carries η_q's δ_0 cap), so CODEX_REVIEW_DAG §6's domain restriction
ε_1 ≤ 2/5 concerns the size of R, not W-cb♯.

**ru55-U3d — What the repair changes: CONFIRMED (exact).** ru55_1 G4-G5: a_cb♯'s third entry binds at all four points; a_cb♯/a_bad
= 1/(16Nb_1(16N + 3)²A_d²) = 1/7925299200 (N = 2, κ = 1), 1/5067619200 (2, ¼), 1/25241269248 (3, 1), 1/16139850048 (3, ¼), i.e.
1.2618·10⁻¹⁰, 1.9733·10⁻¹⁰, 3.9618·10⁻¹¹, 6.1958·10⁻¹¹; the old third entry divided by the new one equals R² exactly; a_D♯ = a_cb♯.
Downstream (SMALLNESS_DAG edge a_D → a, when the collar family is in the history): a, n_H, n_♯, W, ε_♯, C_H and the g_0
ceilings move by magnitudes only. Nothing upstream moves.

**ru55-U3e — SMALLNESS_DAG §8.1's form of the repair (quietness threshold η ≤ η_q/R; third entry ÷ R²): CONFIRMED, and its "Not
checked: whether CL^J's other uses of η_q tolerate the change" is now checked.** CL^J (c): tolerates (η′-quiet ⇒ η_q-quiet).
Lemma 7.2-0^J: ε^J_♮'s min{η′/2, ε^J_loc/C_♭} is still decided by ε^J_loc/C_♭ at all four points ((η′/2)²/(ε^J_loc/C_♭)² = 6.16,
9.63, 2.90, 4.54; ru55_1 G6) — unchanged. **But a_ret^{PLD}'s binding (β) entry prices non-quiet sea cubes at the quietness
threshold, so it falls by R² too**, and with it route (ii)'s fallback θ: ru55_2 V2 shows the quietness form reaches a_ret,
γ_0, γ, β_+ and g_1 (42 descendants), W-cb♯ does not (37; strict subset). CODEX_REVIEW_DAG §6 ("compatibility with the other
consumers remains NOT-VERIFIED"): agree at its time; settled here — W-cb♯ touches no other consumer.

**ru55-U3f — The repair creates no cycle and no K- or T-growth: CONFIRMED for the encoded graph** (ru55_2 V1: 0 B-strict SCCs;
B-all family identical to V0's; live growth seeds unchanged [C_fun, V_LF]; η* not growth-tainted; its weak taint is ε_1's,
witness ε_N5,unif → ε_loc → η*; order η_q (114), ε_loc (113) < η* (116) < a_cb (124) < a_D (125) < a (139) < g_0 (162)). The (TC)
edge η_q → ε_loc was the one ε_1-free *window* in the hierarchy (SMALLNESS_DAG §8.3; CODEX_REVIEW_DAG §7 item 1); W-cb♯ deletes
it, so that counterexample to "every live constraint is a one-sided bound on a later choice" disappears. Codex's other two
((K), the complex width) are outside this file.

**ru55-U3g — Joint collar (K2), informational: CONFIRMED arithmetic.** If σ^J_Q's coarse-link clause uses ε^J_loc/2, the (TC)-type
factor is R_J² = 754875625/8192 (R_J = 303.56, N = 2) and 534267075/4096 (361.16, N = 3), κ-independent; W-cb♯ covers it, at the
price a_cb♯ ∝ 1/R_J².

### FI-1 — the coupling fixed point

**ru55-F1 — FI-1 is a per-level, forward, scalar fixed point (REVIEW_RLARGE_V3 §3.3): CONFIRMED** (§3.1: the U_{k+1}-marginal of W
involves K_0..K_k only; stage k reads K_{k+1} through CL^J's C(B) factors and no later kernel).

**ru55-F2 — Theorem FI-1 (§3.2): CONFIRMED (PROVEN here), conditional on (A-unif) and (A-cont).** The one-step window X_k is mapped
into itself with no hypothesis beyond FLOW's (UNIV-1L) and C_ργ² ≤ ½β_0'log L (ru55_4 F1); the new γ condition only keeps X_k
inside Option A's bracket and is tight (F2; F2-C). (A-unif) is Option A's own content with its kernel-parameter quantifier
written out, restricted to the one-step window (much weaker than uniformity over the whole bracket [x_lo, u_k + R]). The γ
condition is implied at the constants in force unless R ≳ 10⁹³, since γ² ≤ γ_0² ≲ 10⁻⁹⁴ (U1-4).

**ru55-F3 — Uniqueness and tuning: CONFIRMED (PROVEN here) given (A-Lip), and (A-Lip) is load-bearing for the contraction route.**
With (A-Lip) and joint continuity, (SF-cont) holds for the A5 sequence and F-tune applies verbatim (§3.3, with erratum E2);
(A-an) ⇒ (A-Lip) by Cauchy at radius 2C_ρg_k². ru55_4 F4: a continuous family with |ρ| ≤ ε and slope 2 makes the smallest fixed
point jump by 4.0·10⁻³ > ε = 3·10⁻³, while the slope-½ family moves by ≤ 2|Δs|. The Browder-continuation alternative (from
(A-cont) alone) is ARGUED only.

**ru55-F4 — RLARGE §4.4 "Neither option is a theorem here" / U4 / K11: SUPERSEDED.** Option A is now an existence theorem
conditional on (A-unif) + (A-cont), and a tuning theorem given (A-Lip). REVIEW_RLARGE_V3 §3.3's FI-1A (continuity + invariance)
is the right condition — its invariance half is PROVEN here — and its "A and B are the same proof once FI-1A is stated": agree
(B's "check that the bracket at (k, k + 1) is an output of the step at k" is exactly F1/F2). CODEX_REVIEW_DAG §3.3 ("NOT-VERIFIED
as discharged … F-tune's scalar continuity argument cannot simply be relabelled a proof of the missing sequence-level
agreement"): agree — Theorem FI-1 is a different argument (IVT in the next kernel parameter, per level), and it discharges
the agreement modulo (A-cont), not modulo F-tune.

**ru55-F5 — FI-1 is not a constants cycle, and its γ condition adds none: CONFIRMED** (SMALLNESS_DAG §3.2: agree; ru55_2 V5: R, κ,
L → γ add no SCC; γ (117) precedes g_1 (119) and g_0 (161)). K and T enter nowhere; the torus enters only through δβ_k ⊂ ρ_k (U5).

**ru55-F6 — Alignment with FLOW55.md (Opus 5.5, in progress; read at 00:44Z: PRE-STATED 00:28:57Z, findings from 00:43Z).** No
duplication: FLOW55 derives the per-step recursion and b_k; I use only its one-step form u_{k+1} = u_k − b_k − ρ_k with
|ρ_k| ≤ C_ρg_k² (its §1 summary) and the x-independence of b_k (its §5: b_k = 𝔅(J_k), a function of the tree jets of 𝒯_k, i.e.
of κ and the past). One request to FLOW55/FLOW: carry the next-kernel-parameter quantifier ("for every x = u^{ker}_{k+1} ∈ X_k")
in F-rem and (SF-g)_k, or else state them along the A5 sequence, which presupposes Theorem FI-1. **Symbol collision:** FLOW55
§0 item 5 and §1 use "(TC)" for "k-uniform weighted bounds and geometric convergence of [the tree jets] J_k" — not RLARGE/HW's
(TC) (ε_loc/2 ≥ (16N + 3)A_dη_q). Since W-cb♯ retires the latter, the name can pass to FLOW55's object, but only with a note.

**Route-numbering collision (read before quoting any route).** My routes (i)-(iv) are PLD §16.5, §17.4, §18.7 and §19.8 (ρ2).
PLD itself (l.2898-2908) calls §17.4 "route (i)" and §18.7 "route (ii)", and HANDOFF's "Route (ii) defuses it" (the λ_min item)
means PLD §18.7 = my (iii).

---

## 6. Review and Codex files used, and whether I agree

- **CODEX_REVIEW_DAG.md** (Codex gpt-6-astra/max per the brief; banner not inspected; read in full as on disk at 00:41Z, 37 642
  bytes, "Review completed: 2026-10-29 00:13:04 UTC" — it looks finished; at 00:09Z it was 2 375 bytes, i.e. it was still being
  written when this task began). **§6 (TC) exact derivation: agree** (identical exact squares). **§6 "reducing quietness …
  compatibility with the other consumers remains NOT-VERIFIED": agree at its time, settled here** (ru55-U3e; and W-cb♯ needs no
  change of the quietness threshold). **§3.1 omitted edge n_♯ → (SC)_k: agree**, reproduced (ru55_2b), and sharpened: a_ret is in
  the cutoff loop only through the K12 fallback (ru55-U1i). **§3.3 FI-1 "NOT-VERIFIED as discharged": agree at its time**; Theorem
  FI-1 discharges existence modulo (A-unif) + (A-cont) by a different argument than F-tune (ru55-F4). **Edge 41's condition** (a_A
  independent of θ): agree, and it fails literally on route (iii) (ru55-U1h). **Edges 43, 110, 114: agree.** **§7 "unconditional
  retirement of the decade ledgers REFUTED", item 1 (TC):** agree for (TC) as written; W-cb♯ removes that window (ru55-U3f).
  Items 2-3 ((K), complex width): not examined here. **§4 checker audit** (controls cannot find semantic errors; omitted edges are
  invisible): agree, and it applies to my ru55_2/2b variants too.
- **REVIEW55_ARS.md** (Opus 5.5): F03 ((RLF-δ) uses a_ret, l.618 NOT-VERIFIED for it) — agree, and reduced here to (L618-δ); F04
  (+63.619 reproduced; qualifications θ, U1, (AE)) — agree, and I add B_0 (ru55-U1f); F05 K9 (a_ret is the one door for an
  a_RS-type quartic) — agree: a_ret^{PLD}'s binding entry is a fluctuation price ∝ η_q²/σ_fl², not an a_RS quartic.
- **SMALLNESS_DAG.md** (Opus 5.5): §8.1 / dag55_3 — CONFIRMED (ru55-U3a, U3e); §3.2 FI-1 not a constants cycle — CONFIRMED (ru55-F5);
  §3.3 "a_A does not depend on θ" — REFUTED for PLD's routes (ru55-U1h); §8.3's principle — agree for one-sided bounds, and W-cb♯
  removes the exception it names.
- **REVIEW_RLARGE_V3.md** (independent agent, 09:47-10:05 UTC): §3.3 FI-1A — agree (ru55-F4); §3.4 K12 owner/identification — agree
  (ru55-U1b); Part 4 / N3-3 (e^{38417B_0} dropped; 2.70·10⁻⁹¹) — agree, reproduced (ru55-U1f).
- **REVIEW55_HWPLD.md** (Opus 5.5): F6 ((CEM^{COL}) false as quantified) and r55h-37/38 — used, not re-derived (ru55-U1g says so).
- **FLOW55.md** (Opus 5.5, in progress): aligned, no duplication; a symbol collision flagged (ru55-F6).

---

## 7. Summary table — every claim examined, with its verdict

| # | claim | where (file, locating string) | verdict | finding |
|---|---|---|---|---|
| 1 | a_ret's value stated by no source | RLARGE l.195-196 "no source states its value" | CONFIRMED as of v3's freeze; STALE (PLD §16.8) | U1a |
| 2 | a_ret ≡ (SC2)'s exponent; W1R chain | PLD l.485, l.487-491; REVIEW_RLARGE_V3 §3.4 | CONFIRMED | U1b |
| 3 | Proposition CC does not reach (RLF-0)/(RLF-δ) | PLD §16.8 "Proposition CC"; W1R "𝓗^{sea}_X(1)" | CONFIRMED (new) | U1b |
| 4 | a_ret^{PLD} formula; (β) binds; a_ret/a_bad = 8.03·10⁻⁷ (N=2), 3.57·10⁻⁷ (N=3) | PLD l.1550-1555; p4 E2 | CONFIRMED (arithmetic); status CONDITIONAL (supremum) | U1c |
| 5 | (SG^{fl})_k, (BG)_k off the (RLF-0)/(RLF-δ) path | RLARGE §4.2 rows 7, 8 | REFUTED once a_ret := a_ret^{PLD} (they re-enter via row 2) | U1c |
| 6 | (RLF-δ)'s γ_0 exists for any a_ret > 0 | RLARGE l.201 "The γ_0 needed" | CONFIRMED (proven here) | U1d |
| 7 | l.618 "RLF's own ceilings do not bind" — (RLF-δ) | RLARGE l.615-618 | NOT-VERIFIED; ⟺ (L618-δ), true unless (SC)_k's constants ≳ 10⁵⁸ | U1e |
| 8 | (RLF-δ)'s condition "has the form e^{-a/g²}", ceiling "a/10²" | RLARGE l.615-617 | REFUTED (exponent a_ret, log factor; lowest RLF ceiling) | U1e |
| 9 | "g_K² ≲ a/10² ≈ 10⁻⁸⁸" for HIST-sum/REL-seq | RLARGE l.616-617 | REFUTED (drops e^{38417B_0}: 2.70·10⁻⁹¹ at B_0 = 1) | U1e, U1f |
| 10 | "+63.619 decades" at its inputs | ARS_BIND A7; PROOF l.88 | CONFIRMED (arithmetic) | U1f |
| 11 | "+63.619" is the live margin | SESSION25_RESULTS l.578 "CLEARS DX′ BY +63.619" | REFUTED (+61.03 / +58.24 / +56.32 by route; RLF's binding (RLF-δ) ≈ +57.5) | U1f |
| 12 | a_A's definition and four routes | HW l.937-941; PLD l.1416, 1856, 2485, 3482 | CONFIRMED (reading) | U1g |
| 13 | route (iii): a_A ≥ θa_bad iff κ ≥ 256θc_pr/λ (1/84270); a_A = a_bad/4 | PLD l.2485-2487; p6 C1-C2 | CONFIRMED (exact); hypothesis false as quantified | U1g |
| 14 | a_A ≥ θa_bad (U1's question) | RLARGE l.809 (U1) | NOT-VERIFIED (route-dependent) | U1g |
| 15 | θ ↔ a_A literal 2-cycle on route (iii); resolved by §1.5's order | RLARGE_U55 §1.5; ru55_2 V3/V4 | CONFIRMED (encoded graph) | U1h |
| 16 | "a_A does not depend on θ" | SMALLNESS_DAG §3.3 | REFUTED for PLD's routes (harmless once ordered) | U1h |
| 17 | a_ret in the cutoff loop only via the K12 fallback | ru55_2b; CODEX_REVIEW_DAG §3.1 | CONFIRMED | U1i |
| 18 | (TC) fails with RLARGE's ε_loc (×19.32/15.45/22.99/18.38) | SMALLNESS_DAG §8.1; dag55_3 | CONFIRMED (exact R²) | U3a |
| 19 | U3's fix ε_loc ≥ (16N+3)ε_1/(128N) compatible with CL (c) | RLARGE l.811 (U3) | REFUTED (incompatible, even relaxed CL, even κ → 0) | U3b |
| 20 | [hand] sufficient condition for (TC) | RLARGE l.84-86 | CONFIRMED (algebra), vacuous for CL's ε_loc | U3b |
| 21 | Lemma W-cb♯ ((TC) removed) | RLARGE_U55 §2.2 | CONFIRMED (proven here) | U3c |
| 22 | a_cb♯ binding entry; a_cb♯/a_bad = 1.26·10⁻¹⁰, 1.97·10⁻¹⁰, 3.96·10⁻¹¹, 6.20·10⁻¹¹; shrink exactly R² | ru55_1 G4-G5 | CONFIRMED (exact) | U3d |
| 23 | quietness-threshold repair; third entry ÷ R² | SMALLNESS_DAG §8.1 "Repair (mine, ARGUED)" | CONFIRMED; its consumer check done: ε^J_♮ unchanged, a_ret's (β) entry ÷ R² | U3e |
| 24 | repair creates no cycle, no K/T growth | ru55_2 V1 | CONFIRMED (encoded graph) | U3f |
| 25 | (TC) is a two-sided feasibility window | CODEX_REVIEW_DAG §7 item 1; PROOF.md l.15 | CONFIRMED as written; REMOVED by W-cb♯ | U3f |
| 26 | joint-collar factor R_J = 303.56 / 361.16 | ru55_1 G7 | CONFIRMED (arithmetic; σ^J_Q unstated) | U3g |
| 27 | FI-1 is per-level and forward | REVIEW_RLARGE_V3 §3.3 | CONFIRMED | F1 |
| 28 | Theorem FI-1 (existence) | RLARGE_U55 §3.2 | CONFIRMED (proven here; ⇐ (A-unif) + (A-cont)) | F2 |
| 29 | uniqueness/tuning ⇐ (A-Lip); (A-Lip) load-bearing | RLARGE_U55 §3.3; ru55_4 F4 | CONFIRMED (proven here) | F3 |
| 30 | "Neither option is a theorem here" (U4, K11) | RLARGE l.568 | SUPERSEDED (conditional theorem) | F4 |
| 31 | FI-1 "a fixed point, not a constants cycle"; γ condition acyclic | SMALLNESS_DAG §3.2; ru55_2 V5 | CONFIRMED | F5 |
| — | Browder-continuation route to F-tune without (A-Lip) | RLARGE_U55 §3.3 | ARGUED only (not counted) | F3 |

**Counts (rows 1-31): CONFIRMED 23 (incl. one STALE, row 1) · NOT-VERIFIED 2 (rows 7, 14) · REFUTED 6 (rows 5, 8, 9, 11, 16, 19)
· SUPERSEDED 1 (row 30, a status line overtaken by row 28; not a refutation).**

---

## 8. To the lead

**What changes, in one line each.**
- **U3 is closed.** (TC) is infeasible with CL's ε_loc (exact), and no ε_loc can fix it within CL's proof; **Lemma W-cb♯ removes
  (TC) as a hypothesis** by splitting W-cb's quiet case at η* := min{η_q, ε_loc/(2(16N + 3)A_d)}. Cost: a_cb♯ = a_cb/R² exactly
  (×373.24 at N = 2, κ = 1), a magnitude downstream of a_D. Nothing upstream moves, and no other consumer of η_q is touched.
  Prefer W-cb♯ to lowering the quietness threshold: the latter also lowers a_ret^{PLD} by R² (and route (ii)'s fallback θ).
  Row 20 and U3 can be struck, and row 10f and K15 read "W-cb♯ ⇐ (CLS-min)" with a_cb♯.
- **U1 is reduced, not closed.** a_ret is (SC2)'s exponent; its only candidate is PLD §16.8's chart formula (a supremum,
  CONDITIONAL on (SC)_k, (SG^{fl})_k at η_q on the chart, restricted (BG)_k and a level-k σ_fl). Existence of (RLF-δ)'s γ_0 needs
  only a_ret > 0. **l.618 for (RLF-δ) ⟺ (L618-δ)**, a single inequality on (SC)_k's unstated (C, p), true unless they are ≳ 10⁵⁸.
  a_A ≥ θa_bad is route-dependent and not established; it can only ever cost a magnitude.
- **FI-1 is a theorem, conditionally.** Per level, the fixed point exists by the intermediate value theorem in the next kernel
  parameter, given (A-unif) (Option A's own content, on the one-step window only) and (A-cont). The window's invariance is proven
  from FLOW's constants, plus one harmless extra upper bound on γ. Uniqueness, and hence F-tune for the A5 sequence, needs
  (A-Lip), and the counterexample shows (A-Lip) is load-bearing. U4/K11 should read "Option A with (A-unif), (A-cont), (A-Lip)
  [node A regularity in the kernel parameter]".

**Findings that change what PROOF.md / HANDOFF should say** (owner's call; I edited neither):
1. PROOF.md l.15 ("(TC) … two-sided feasibility windows"): with W-cb♯, (TC) is no longer a window. Two remain: (K) and the complex
   width.
2. PROOF.md l.16 ("RLARGE l.618 … NOT-VERIFIED for (RLF-δ), whose a_ret is unfixed (RLARGE U1)") should read: NOT-VERIFIED,
   reduced to (L618-δ) on (SC)_k's constants, with a 10⁵⁸ envelope at a_ret^{PLD}. RLF's lowest own ceiling is (RLF-δ)'s
   (≈ 10⁻⁹⁴), not HIST-sum's.
3. PROOF.md l.18's list of what "+63.619" drops should add **B_0** (l.617's a/10²). The figures by route are +61.03 (θ ↑ 1/24),
   +58.24 (θ = 1/15000) and +56.32 (fallback), all at B_0 = 1. SESSION25_RESULTS l.578's headline is wrong as a live margin.
4. HANDOFF's "one PROOF-owned constant conflict" (λ_min 3.17·10⁻³ vs 6.6·10⁻¹⁰): on routes (iii)/(iv) it moves only γ_0, and
   (L618-δ) holds under both values (budget 1.67·10⁵⁴ under L0-1). It matters only through route (ii)'s K12 fallback (θ ∝ a_ret).
5. RLARGE §4.2 rows 7 and 8 are stale once a_ret := a_ret^{PLD}: (SG^{fl})_k and the restricted (BG)_k re-enter through row 2.
6. SMALLNESS_DAG: §3.3's "a_A does not depend on θ" should be replaced by §1.5's order (θ before a_A, from a_A°'s θ-free entries).
   Its §8.1 repair is CONFIRMED and superseded by W-cb♯. Under §1.5's order, θ and a_ret leave the cutoff SCC on routes (iii)/(iv)
   (ru55_2/2b).
7. **No tally change.** W-cb♯ is uncounted, like W-cb. Theorem FI-1 is conditional on node-A regularity and is not a PROOF.md
   item. None of this touches the 72 / 2 / 7 / 24 + 1 tally.

**Symbol collisions found in this work:** R (the (TC) ratio vs FLOW's slack 2R_0; use R_TC); "(TC)" (RLARGE/HW's threshold
compatibility vs FLOW55's tree-jet convergence); C (the (SC)_k prefactor vs SF's TILT constant inside C_Ω); route numbers (mine
vs PLD's); t (§1.2's 1/g² vs §2.2's collar threshold, local to this file).

**Codex agreement:** with CODEX_REVIEW_DAG on every item I used. I extend its §3.1, settle its §6 NOT-VERIFIED, discharge part of
its §3.3, and remove its §7 item 1 (see §6).

---

## Errata to this file (append-only; found on proof-reading at 2026-10-29T00:47Z; nothing above is edited)
- **E1 (§1.2).** "s_0² ≥ P/(2a_ret), so φ ≥ 0 on all of [s_0², ∞)" — the stated inequality holds only when P/(2a_ret) ≥ 1, which is
  true at every value used here (P/(2a_ret) ≥ 6/(2·10⁻⁹⁰)), and the conclusion does not need it. The correct one-line reason:
  ψ(s) := a_ret s² − (P/2)s − ln⁺C ≥ 0 for every s ≥ s_0 (s_0 is ψ's larger root), and φ(t) ≥ ψ(√t). So φ ≥ 0 on [s_0², ∞).
- **E2 (§3.3).** "|x*(p) − x*(p′)| ≤ (1 − q)^{-1}·sup_x|ρ_k(p, x) − ρ_k(p′, x)|" omits Φ_k's explicit dependence on u_k. Read
  "≤ (1 − q)^{-1}(|u_k − u′_k| + sup_x|ρ_k(p, x) − ρ_k(p′, x)|)". The continuity conclusion is unchanged (x*(p′) ∈ X_k(p) for p′
  near p, since Φ_k maps X_k strictly inside at its upper end and the γ condition can be taken strict).
- **E3 (§0).** "Not read: … SF (except the C_Ω definition line …)" — HANDOFF.md l.172-184 and PROOF.md l.12-18 were also read, by
  grep and sed, after §0 was written (for §8).

## Closing provenance (2026-10-29T00:48Z UTC)
Model: claude-opus-5-5 (line 1). Files written: this file; checks/ru55_1_{criteria.md, tc.py, out.txt, err.txt};
ru55_2_{criteria.md, variants.py, dag.py, out.txt, err.txt}; ru55_2b_{criteria.md, dag.py, out.txt, err.txt};
ru55_3_{criteria.md, u1.py, out.txt, err.txt}; ru55_3b_{criteria.md, lncheck.py, out.txt, err.txt};
ru55_4_{criteria.md, fi1.py, out.txt, err.txt}. Every err.txt is empty. No git command was run, and no other lane file was edited.
The DAG checks import checks/dag55_2_dag.py and checks/dag55_2_graph.py read-only (python3 -I -B: no bytecode written).

## Errata, second pass (append-only; proof-reading at 2026-10-29T00:48Z; nothing above is edited)
- **E4 (§0).** "re-checked before finishing (§3.5)": there is no §3.5; the FLOW55 re-check is ru55-F6 in §5. Re-checked again at
  00:48Z: FLOW55.md is 33 490 bytes (mtime 00:46Z) and still contains no statement about FI-1, A5 or the kernel parameter (grep for
  "FI-1", "A5", "fixed point", "kernel coupling", "Option A": no hits beyond its consumer table's quotation of FLOW §4), so
  ru55-F6 stands.
- **E5 (§1.1).** "computed exactly in check ru55_3 (§4.3)": there is no §4.3; read "the ru55_3 row of §4 and ru55-U1c in §5".
- **E6 (§1.4).** "(SDP)^A (RLARGE l.408-410 …)": the statement is at **RLARGE l.397-398** (string "μ(S ⊂ D_k) ≤ (C_Ae^{-a_Au_k})^{|S|}·
  exp(c_A·shadow sums), a_A ≥ θa_bad").
- **E7 (§2.3).** In one bullet R names two objects: in "e^{-θ_cb a_D♯(u_j − R)}" it is FLOW's slack 2R_0 (HW's notation); in
  "(third entry)/R²" it is the (TC) ratio R_TC. The same split applies to §2.4 ("η′ := η_q/R" is R_TC).
- **E8 (closing provenance).** The header "(2026-10-29T00:48Z UTC)" was written ahead of the clock: `date -u` immediately after the
  write printed 00:47:14Z.
- **E9 (§7 counts).** The table has **CONFIRMED 22** (rows 1, 2, 3, 4, 6, 10, 12, 13, 15, 17, 18, 20-29 except none, i.e. 20, 21, 22,
  23, 24, 25, 26, 27, 28, 29, and 31), not 23. Corrected counts for rows 1-31: **CONFIRMED 22 · NOT-VERIFIED 2 (rows 7, 14) ·
  REFUTED 6 (rows 5, 8, 9, 11, 16, 19) · SUPERSEDED 1 (row 30)** = 31.
