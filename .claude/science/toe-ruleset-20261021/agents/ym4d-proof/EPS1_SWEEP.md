# EPS1_SWEEP — consumer sweep for TAUFLAT §4 option C (lowering ε_1)

Owner of this file: the ε_1 consumer-sweep auditor, session 24 (ym4d-proof lane).
Scope: ONE bounded audit. This file adds no new mathematics to the RG construction; it enumerates and
prices the consumers of one constant so that an owner decision can be made on facts.
Writable by me: this file and new files under `checks/` prefixed `e1_`. Nothing else, anywhere.

---

## §0. PRE-STATED (first edit of this file)

**This is the first edit made to this file. UTC time of this edit: 2026-10-28T14:43Z.**

Statements only, and **no number at all**. Written before any grep for ε_1, before reading RLARGE.md,
HW.md, PLD.md, SF.md, HIST.md, FLOW.md, BFT_A.md, BFT_B.md, LINEAR_PACKAGE.md or EXISTENCE.md, and before
any arithmetic. It cites no quantity produced in session 24. TAUFLAT.md, EPSSTAR.md and
SESSION24_RESULTS.md have been read for the *statement* of the proposal I am auditing; no constant from
them appears here, and none of their figures is assumed below.

### §0.1 What I was asked to audit

TAUFLAT.md §4 **option C** proposes lowering the smallness threshold **ε_1** by several decades, on the
grounds that (a) ε_1 enters the failing DESC-ε (iii) clause quadratically with the helpful sign, (b) the
lane records only a **ceiling** on ε_1 and no floor, and (c) the declared price is paid in quantities its
owning file says do not bind. TAUFLAT **gated its own recommendation**: it did not sweep every ε_1
consumer, and it named one worry — lowering ε_1 **enlarges the large-field region**, because ε_1 is the
small-field threshold.

My job is that sweep. Four questions, in order:

- **Q1 (symbol identity).** Is **ε_1 one symbol or several** across the lane? EPSSTAR §5 records four
  distinct constants all written ε_*, and TAUFLAT confirmed θ_0 is two symbols whose collision is what
  made its conflict real. If ε_1 is several symbols, **no aggregate sweep is meaningful** and each must be
  audited separately. This is tested FIRST, before anything is aggregated.
- **Q2 (enumeration).** Every consumer of ε_1 in the lane, with file:line, classified as **ceiling-side**
  (needs ε_1 small; lowering helps or is neutral), **floor-side** (needs ε_1 large enough; lowering hurts),
  or **ratio** (a quotient or difference in which ε_1 appears against another constant; sign of the effect
  must be computed, not assumed).
- **Q3 (large-field pricing).** What grows when ε_1 falls, by how much, and does any consumer of the
  large-field region's **size** fail a hypothesis, or merely become more expensive? Numbers, not adjectives.
- **Q4 (declared price).** Does the declared price reproduce, and is the claim that it **does not bind**
  true against the lane's *current* constants rather than its pre-session-24 ones?

### §0.2 Pre-registered verdict scale for option C

Exactly one of:
- **SAFE** — every consumer found is ceiling-side or neutral; every ratio evaluated keeps its required
  sign; no hypothesis anywhere is violated at the proposed value; the declared price does not bind.
- **SAFE WITH NAMED CONDITIONS** — as above, except that one or more clauses survive only under a stated
  condition, and each condition is named with its owning file and the quantity it constrains.
- **UNSAFE** — at least one floor-side consumer, or one ratio that reverses, or one hypothesis that fails
  at the proposed value, and the failure is not repairable inside the proposal itself.

**Pre-registered as NOT sufficient for SAFE:** that no file contains the literal string "ε_1 ≥"; that the
owning file of a priced quantity says the price does not bind (that is the claim under test, not an input);
that a consumer's margin is large today (a margin is only safe if it is evaluated at the *proposed* ε_1).

### §0.3 Pre-registered failure modes (the ways this audit's SAFE verdict should break)

Written before the sweep, so that finding one of these is a result and not a surprise:

- **(F1) A hidden floor.** A clause of the form ε_1 ≥ (something), or a hypothesis that requires the
  small-field region to contain a set of a given size, exists in a file TAUFLAT did not read. **(F1) alone
  forces UNSAFE** unless the something is itself lowered by the same proposal.
- **(F2) Symbol split.** ε_1 is two or more distinct constants, so that the ceiling being lowered is not
  the ε_1 that the failing clause consumes. This would make option C **ineffective** as well as unsafe, and
  it is the single most likely way the proposal fails.
- **(F3) A ratio that reverses.** Some consumer needs ε_1 **comparable to** another small constant
  (a quotient near 1, a branch selector, a two-sided window). Lowering one side of a window breaks it.
- **(F4) Large-field blow-up that is qualitative.** A consumer of the large-field region's size needs that
  region to be a *small perturbation*, i.e. its hypothesis has the form "region measure < threshold" with a
  threshold that does not move with ε_1. Then no number of decades of price buys it.
- **(F5) The declared price binds.** One of the priced quantities crosses a ceiling that is recorded
  elsewhere in the lane and was not consulted — in particular a ceiling that *moved* in session 24.
- **(F6) A consumer in another lane.** The existence lane, or a frozen package, consumes ε_1 under a
  clause the proof lane does not track.

### §0.4 Pre-registered symbol-identity discipline (Q1's method)

For each occurrence of ε_1 / eps_1 / epsilon_1 I will read the **definition in force at that occurrence**
in its owning file, not the symbol. Two occurrences are the same symbol only if I can cite one definition
that both use, or a line in an owning file that equates them. Where an occurrence is a *local* ε_1 (a
bound variable in a lemma, re-used letter) I will say so and exclude it from the aggregate. I will state
the count of distinct symbols found, and if it exceeds one I will report that **loudly and first**, since
TAUFLAT's own ε_1-identity check (HIST A5 ↔ RLARGE a_bad) covered only two of the files in my list.

### §0.5 Pre-registered arithmetic method

Exact `fractions.Fraction`, or `decimal.Decimal` at fixed high precision, in plain `python3 -I`, single
thread, no numpy/BLAS, no numeric lock (per the brief's rule 6). **No floating-point intermediate will
carry a decade comparison**, and no quantity will be floated across more than a few decades: ratios are
formed as exact rationals and only displayed as log10. Transcribed constants carry file+line citations and
are **not re-derived**; the script's job is arithmetic consistency between transcriptions, so a reproduced
number is **not** an endorsement of its source.

### §0.6 Pre-registered falsifiability clause (anti-tautology), with the power check named in advance

Five findings in session 24 were verification gates incapable of failing. I pre-register:

- **Every check I run must be able to return both verdicts**, and I will say against which *independent*
  construction each is tested — independent meaning a transcription from a different owning file than the
  one whose claim is under test, or a clause whose threshold was fixed before the proposal existed.
- **The mandatory power check.** I will construct an ε_1 value at which **my own verdict flips**, and run
  it: specifically, a value low enough that at least one clause I classify as ceiling-side or neutral is
  driven to fail, and a value high enough that the failing DESC-ε (iii) clause is restored. If no value of
  ε_1 in either direction can flip any verdict my script returns, the script **has no power** and I will
  report it as such, not as a PASS.
- **A check that merely re-evaluates the formula its source evaluated is not evidence.** The things with
  power here are (i) the definition comparison of §0.4, (ii) the evaluation of every clause at the
  *proposed* ε_1 rather than today's, and (iii) the independent reconstruction of each priced quantity from
  the chain that produces it rather than from the summary line that quotes it.

### §0.7 What this file will NOT do

- **It will not change ε_1 anywhere, or request that it be changed.** This is an audit that informs an
  owner decision. The decision belongs to RLARGE's and SF's owners and to the lead.
- It will not edit TAUFLAT.md, EPSSTAR.md, SQ.md, HW.md, PLD.md, RLARGE.md, HIST.md, SF.md, BFT_*.md,
  NORMS.md, GREENT.md, YSUP.md or any REVIEW_* file. Requests on those go in a
  "FOR OTHER FILES (not edited)" section.
- It will not re-judge the DESC-ε (iii) failure itself, TAUFLAT's adjudication, or the status of (MS-Sob),
  (AE), AE-red or (REG-min). Those are quoted from their owners.
- It will not attempt option B, D, E or F, and it will not re-price option A.
- No git command will be run by me.

### §0.8 Pre-registered statuses

PROVEN (a complete argument written out here from stated hypotheses) / COMPUTED (exact) / ARGUED /
CONDITIONAL (naming the input) / OPEN. A failed check is reported as a FAIL with its output and script
unaltered; a re-run takes a new id and leaves the criteria untouched; any probe run after seeing a result
is labelled POST-HOC. An enumeration is **COMPUTED** only for the files I grepped, and I will list the
files, since a consumer list is only as complete as its search domain.

---

## §1. E1-A — the symbol-identity gate, settled first (§0.4)

> ### **ε_1 IS SEVERAL SYMBOLS — at least FIVE**, and only one of them is the subject of option C.

Status: **COMPUTED (reading, with definitions quoted from owning files).** This was pre-registered in
§0.3 as failure mode **(F2)**, the single most likely way the proposal fails. It does not kill option C,
because the symbol the failing clause consumes and the symbol RLARGE ceilings are the same one — but the
proposal **must be written as scoped to that symbol**, and the other four must not be moved with it.

| # | symbol | definition in force, with citation | same as #1? |
|---|---|---|---|
| **1** | **ε_1^cut** — the small-field plaquette cut | χ_Q := Π_{p⊂int Q}1{‖1 − U(p)‖_op < ε_1} (**RLARGE.md l.58**); bounded above by the five-entry min at **RLARGE.md l.70-72**; the same symbol in HIST A5 (**HIST.md l.1684**), HW a_bad (**HW.md l.203**), PLD (**PLD.md l.1376**), SF (TH-ch″) (**SF.md l.2193**), PROOF (**PROOF.md l.1555**) and EXISTENCE (**EXISTENCE.md l.1674**) | — |
| **2** | **ε_1^{N2}** — BFT lane B's local-smallness threshold | **ε_1 := [Λ_2(L²/(L²−1))(4C_eΛ_2 + 12c_h(Λ_2^{(1)})²Λ_2)]^{−1}·min(1,…)** (**BFT_B.md l.3058**), a bound on the coarse flatness f_k, defining the class 𝒦(ε_1) (**BFT_B.md l.2865, l.2870-2871**). It is **defined by a formula in O(1) geometric constants**, not chosen, and is "ε_1 = ε_1(L, φ, N, d) independent of k, T, j" (l.3059). Its own consumers use ε_2 ≤ ε_1 (l.3311), 8c_NC_1ε ≤ 1/2 (l.4600), 12.2C_Nε_1 ≤ ε_0 (l.3077) — all O(1)-scale. | **NO** |
| **3** | **ε_1^{disc}** — a disc radius in FLOW's fixed-point and root-sector analysis | "On a disc \|φ\| ≤ ε_1 (fixed)" (**FLOW.md l.1927**, l.1931); "\|q_αF\| ≤ ε_1" (**FLOW.md l.2834**, l.3000) | **NO** |
| **4** | **ε_1^{mode}** — a mode amplitude | "modes ε_1e^{ikx} on 1-links, ε_2e^{−ikx} on 2-links" (**FLOW.md l.771**) — a bound variable | **NO** |
| **5** | **ε_1^{exp}** — an exponent index | "C = c_1^{ε_1}⋯c_ℓ^{ε_ℓ}" (**EXISTENCE.md l.2205**) — a ±1 exponent on a loop word | **NO** |
| (6) | **ε_1^{gas}** — an activity bound, named as a target | "z(1, y) ≤ ε_1^{gas}" (**HW.md l.1444**) — explicitly superscripted, so not a collision | n/a |

**Why this matters and is not pedantry.** Symbol 2 is the one that would do damage. BFT_B states
(N2-0)_j as *"There are ε_1 > 0 and C_N, C_ax, C_box < ∞ … such that for every V ∈ 𝒦(ε_1)"* (l.2870) —
the **same words** as RLARGE's "There are g-independent constants ε_1 > 0, a > 0, …" (RLARGE l.130). A
reader aggregating the two would either (i) believe BFT's threshold is ≈ 10⁻⁴⁰, which is false (it is an
explicit O(1) formula), or (ii) carry option C into 𝒦(ε_1), shrinking lane B's class and forcing
𝒞_glob(ε)'s ε down with it (𝒞_glob(ε) ⊂ 𝒦(4ε + Cε²), l.2866) — a cascade nobody has priced. **Neither is
licensed.** Option C touches symbol 1 only.

**TAUFLAT's own ε_1 identity check was correct but narrow.** TAUFLAT §1 l.148-152 checked HIST A5 ↔
RLARGE a_bad and found "one symbol, two files" — true, and reproduced here. It did not read BFT_B or
FLOW, which is where the collisions are.

### §1.1 A second, smaller hazard inside symbol 1: **four live numerical values**

Symbol 1 is one symbol with **four different numbers in force in four files**, all presented as current:

| value | source | a_bad = c_prε_1² at it |
|---|---|---|
| 1.27·10⁻³⁹ | **SF.md l.2837**, quoted as current by **NORMS.md l.746** | 8.972·10⁻⁸⁵ |
| 9.52·10⁻⁴⁰ | **RLARGE.md l.71**, first entry of the min | 5.041·10⁻⁸⁵ |
| 8.95·10⁻⁴⁰ | **RLARGE.md l.611** (SF §22.7 / REVIEW_SF_S7 TB-1) | 4.456·10⁻⁸⁵ |
| **6.7·10⁻⁴⁰** | **RLARGE.md l.72**, the headline ("So ε_1 ≲ 6.7·10⁻⁴⁰") | 2.497·10⁻⁸⁵ |

Spread ×1.90 in ε_1, ×3.59 in a_bad. This audit uses **6.7·10⁻⁴⁰** throughout, as RLARGE's headline and
as the value TAUFLAT and EPSSTAR used. It is the same defect shape TAUFLAT §6.6 named — *a minimum
evaluated once and never re-evaluated* — one level down. Nothing in my verdict turns on which is taken
(the whole sweep is a scaling, so a ×1.90 shift moves every margin by ≤ 0.56 decades against margins of
31-60), but **NORMS.md's k-independence argument is written at 1.27·10⁻³⁹ and so is one evaluation stale.**

---

## §2. E1-B — the complete consumer enumeration

### §2.0 Search domain (the enumeration is COMPUTED only over this list)
`grep` for ε_1 / ε₁ / eps_1 / epsilon_1 over **PROOF.md (66 hits), RLARGE.md (73), HW.md (22), PLD.md
(155), SQ.md (10), SF.md (90), HIST.md (78), FLOW.md (5), BFT_A.md (0), BFT_B.md (17),
LINEAR_PACKAGE.md (2), ../ym4d-existence/EXISTENCE.md (32)**, plus NORMS.md (6), EPSSTAR.md (26),
CONST_T.md (3), NQ_CHECK.md (1) and every REVIEW_*. 586 occurrences in the named twelve. Occurrences of
symbols 2-5 (§1) are excluded from everything below.

### §2.1 CEILING-SIDE (ε_1 must be small; lowering helps or is neutral) — **PROVEN from the cited text**

Every one of these is an upper bound on ε_1 or a quantity that improves monotonically as ε_1 falls.

| consumer | citation | form | effect of option C |
|---|---|---|---|
| (TH-ch′): ε_1 ≤ min{τ_c, τ_c/(2C_bg), ε_bg^{(TH-bg)}/C_bg} | **RLARGE l.68**, SF RSF5-fix TH-1 | ceiling | satisfied with 4.85 more decades |
| (TH-ch″): ε_1 ≤ ε_br/(1.011√N) | **RLARGE l.68**, **SF.md l.2193**, REVIEW_SF_S6 l.332 | ceiling | satisfied; this is the entry that binds today |
| the five-entry ceiling min | **RLARGE l.71** | ceiling | satisfied |
| N5 compatibility: ε_1, ε_loc, ε^J_loc ≤ the N5 background threshold | **RLARGE l.75-76** | ceiling | **helps** (small-field region shrinks, so coverage is easier) |
| ε_1 < 2 sin(π/N) | **RLARGE l.86** | ceiling | satisfied |
| HIST A5: ε_1 ≤ ½δ_a, δ_a = min{δ_3, √(η_AE/C_3), ε_R/(C_♮√C_3), ε_R} | **HIST.md l.1684** | ceiling | satisfied; the AE-red number gains 9.71 decades on its 63.00 |
| SF STEP 3: ε_1 ≤ δ_a/3, s_5 ≤ min{ε_1/5, 0.01} | **SF.md l.870** | ceiling (+ a derived ratio, §2.3) | satisfied |
| PLD (G0-1)(a): ε_1·α_* ≤ λ_min/2 | PLD l.1127 via REVIEW_SF_S5 l.344 | ceiling | **helps**, strongly |
| PLD (G0-1)(c): 10 p_L ℓ ε_1 ≤ α_* | PLD l.1127-1128 | ceiling | **helps** |
| PLD Prop. INH: ε_1 ∈ (0, 0.517] | PLD l.1067 | ceiling | satisfied |
| PROOF 2D wall window: ε_1 ≲ (4π/(N−2))^{1/2} | **PROOF.md l.1403** | ceiling | satisfied |
| PROOF l.4306: divergence window O(ε_1²) ≲ a_B ≲ 4/β′_B | **PROOF.md l.4306** | two-sided, lower end ∝ ε_1² | **helps** — the window **widens** by 9.71 decades |
| EXISTENCE non-triviality: ν^S(‖V_p − 1‖ > ε_1) ≤ C_d g^{−p_d}e^{−a/g²} **below** Haar{‖W − 1‖ > ε_1} | **EXISTENCE.md l.1692-1693**, l.2533 | ceiling on the LHS, and the RHS → 1 as ε_1 ↓ (Haar{‖W−1‖ ≤ ε_1} ≍ c_Nε_1^{N²−1}) | **helps on the RHS**; the LHS is the usual g-ceiling (§2.4) |
| EXISTENCE KN-step: the step δ ≤ (π/3)A_dη needs A_dη ≤ 1 | **EXISTENCE.md l.1772** | ceiling | **helps** |
| EXISTENCE (RLF-3^dis)_ε with ε < ε_1 is "a strictly stronger hypothesis" | **EXISTENCE.md l.4192, l.4200** | — | **the proof lane must DELIVER the stronger statement**; it is the same statement at a lower threshold, and §2.2 is where that costs |
| HW: θa_bad(β_+log L + R) ≤ 10⁻¹⁶ | **HW.md l.826** | smallness | **helps** by 9.71 decades |
| PLD C_A's e^{λκε_1²R/256} and e^{2λκε_1²R/256} entries | **PLD.md l.1416, l.1857, l.2485** | prefactor → 1 as ε_1 ↓ | **helps** (C_A falls to its ε-free entries) |
| PLD ρ_Y bound e^{−a_eg u_{k−1}ℰ_+(Y)/ε_1²} | **PLD.md l.2315, l.2329** | ε_1² in a denominator | neutral: ℰ_+ is itself measured in ε_1² units, so the exponent is scale-free |

### §2.2 FLOOR-SIDE (ε_1 must be large enough; lowering HURTS) — **the point of the audit**

> **There is exactly ONE genuine floor in the lane, and TAUFLAT did not have it.** TAUFLAT §4 C l.404
> says *"Nothing in the files I read bounds ε_1 from below"*, and §6.4 repeats it. That is true of the
> seven files it read. It is **not** true of the existence lane.

**(FLOOR-1) The small-field window must stay open: ε_1 ≫ g.** Status: **PROVEN from the cited text** (the
statement is quoted; the margin is COMPUTED).

- **EXISTENCE.md l.4191-4192** (RX11-fix 6), stating why ε may be taken equal to ε_1 and not smaller:
  *"ε only has to **contain the typical field ≍ g**"*.
- **EXISTENCE.md l.3112**, the coercivity clause that CLS-cone supplies: *"coercivity away from the flat
  set inside 𝒮_j … for configurations **at distance ≫ g but < ε_1**"*. If ε_1 ↓ g the window is empty and
  the clause is vacuous.
- **PLD.md l.995** gives the floor with a constant attached: (SG^net) at t = ε_1/(σ_*²g²) holds iff
  v ≤ σ_*²g²(1 + **2m_*g/ε_1**) — the ℓ¹ absorption margin is proportional to **g/ε_1** and shrinks as
  ε_1 falls at fixed g. PLD l.989's own t-range is 0 ≤ t ≤ ε_1/(σ_fl²g_k²), likewise.
- **PROOF.md l.4307-4308** [heuristic] gives it probabilistically: the expected number of
  threshold-violating bonds per unit physical volume at level k is ~L^{4(K−k)}e^{−cε_1²/g_k²}.

**Is the floor respected? YES, with 31.78 decades to spare.** [COMPUTED, `checks/e1_out.txt` e1-2]

| coupling in force | ε_1/g at E_t = 6.7e-40 | at the proposed ε_1 | verdict |
|---|---|---|---|
| the **ε-independent** binding ceiling g_DX² = 2.456·10⁻¹⁵²/C_Ω (REVIEW_SF_S7 l.203) | **10^36.63** | **10^31.78** | FLOOR-RESPECTED; costs 4.854 of 36.63 decades |
| the **ε-driven** ceiling g²_CRC (×82 ring, HW l.2006) | 10^8.68 | **10^8.68** | FLOOR-RESPECTED, and **exactly invariant** |

The invariance is structural, not luck: **every coupling ceiling the lane derives from ε_1 is ∝ ε_1²**
(§2.4), so g ∝ ε_1 along them and ε_1/g does not move. The only reason the first row loses 4.854 decades
is that **DX′ is ε_1-independent** — confirmed by reading, not assumed: DX′'s a′ = a_sh²/(8N‖C‖m_sh) with
a_sh = ρ_band/(16L⁴N′) and ρ_band = τ_c/(2C_W) (**SF.md l.1886, l.2080**), i.e. **τ_c-driven, not
ε_1-driven** — and **SF.md l.2587** says so in terms: *"(GF-B^𝔥) drives only the τ_c rows … **not ε_1**"*.

**No other floor-side consumer was found.** The only other candidates in the lane are the two
branch-selector inequalities TAUFLAT already dismissed, and I confirm its reading independently:
**SQ.md l.312** and **HW.md l.603**'s "ε_1 ≥ C′τ_♭" select which branch of a_bad := c_pr·min{ε_1², t_pr²}
is active; they already fail (6.7·10⁻⁴⁰ < 1.33·10⁻³⁹) and option C moves ×142125 **further** into the
same branch, which is the branch RLARGE already uses (**RLARGE l.93**). **REVIEW_SQ_S1 l.191**'s
"c_sf = c_♭τ_♭²/ε_1², given ε_1 ≥ C′τ_♭" is the same inactive branch.

**An independent record agrees, and it was written for a different question.** **REVIEW_SF_S5 l.332**,
Part E, having grepped every lane: ***"No lane found requires ε_1 ≥ (g-independent constant): every ε_1
condition is an upper bound or enters through min{}."*** **SF.md l.2207** repeats it. That is the exact
proposition option C needs, recorded before option C existed, and my sweep reproduces it — with the
refinement that the floor which does exist (FLOOR-1) is **not** of the form "ε_1 ≥ a g-independent
constant": it is ε_1 ≫ g, which REVIEW_SF_S5's test was not shaped to catch.

### §2.3 RATIOS (sign must be computed, not assumed) — **COMPUTED, `checks/e1_out.txt` e1-1**

| ratio | citation | behaviour under option C | consequence |
|---|---|---|---|
| ε_loc/ε_1 = 1/√(4Nb_1) = **7.0·10⁻³** | **RLARGE l.907**, value from l.1248 | **exactly invariant** | **(TC) fails by ×19.53 today and by ×19.53 after.** RLARGE §8 **U3** is untouched: option C neither helps nor hurts it. |
| η_q/η_1 = 2/ε_1 | **HIST.md l.181** | **grows ×71398** | this is the joint-vs-RS route gap; see §2.4's ε⁴ finding |
| θa_bad / (ε_1²/(2N)) = 2Nθc_pr | **HW.md l.866** ("far below the action scale ε_1²/(2N)") | **exactly invariant** | HW's "far below" survives unchanged |
| α_E/ε_1, with α_E ≥ c·ε_1 (**HIST l.857**) and α_E ≤ s_5/4, s_5 ≤ ε_1/5 (**SF l.870**, **RLARGE l.455**) | — | **α_E ≍ ε_1, so the ratio is invariant** | HIST **[GAP S2-2]**'s "m > 4α_E/ε_1" bites at the same polymer size; unchanged |
| **the Cauchy C³ constant on 𝔇_{α_E}** ∝ E_0/α_E³ | **HIST.md l.862** (*"C³ bounds in the data follow by Cauchy on 𝔇_α"*) with α_E ≍ ε_1 | **∝ ε_1^{−3}: rises 14.561 decades** | **ARGUED** (the α_E^{−3} is the standard Cauchy estimate, not quoted in the file). This is the second place the declared price is incomplete — see §4.2 |
| a·u_k (the per-defect price actually paid) | RLARGE l.617 form | **exactly invariant** at the ε-driven ceiling: **5.38111·10⁹ → 5.38111·10⁹** | the defect price in force does not move |
| ε_1²/g_K² — the **(CEM-2) gap**, 4.489·10¹⁵ (**HW.md l.2170**, PLD §18.7.2; reproduced exactly) | — | invariant at the ε-driven ceiling; **improves by 9.707 decades at the ε-independent DX′ coupling** (1.828·10⁷³ → 3.586·10⁶³) | a **side benefit** on a critical-path item, though PLD session 7 has since dissolved (CEM-2) |
| 2m_*g/ε_1 — the (SG^net) ℓ¹ absorption margin | **PLD.md l.995** | invariant at the ε-driven ceiling; **falls 4.854 decades** at the DX′ coupling | the one ratio with the unhelpful sign; see §5 condition (C3) |
| Haar{‖W−1‖ > ε_1} vs the soft-limit tail | **EXISTENCE.md l.1692** | RHS → 1 | helps |

### §2.4 The structural fact the whole audit rests on — **COMPUTED, exact**

Every ε_1-driven quantity in the lane falls into one of four classes, and the classification was verified
exactly (`checks/e1_out.txt`, e1-1, **CLASSIFICATION-HOLDS**, 18/18 rows):

- **∝ ε_1²** — a_bad (RLARGE l.88), a = θa_bad (l.87), a″ (l.1245), a_ret (PLD l.1595), η_1 at small ε_1
  (RLARGE l.64), g²_CRC (HW l.1639), the HIST-side ceiling (HW l.2024), g²_ret (HW l.2008), RLARGE's
  a/10² (l.617).
- **∝ ε_1** — ε_loc (RLARGE l.907), η_q (l.64), δ_0 (PROOF l.1642), r = ε_1/16 (RLARGE l.906), ε^J_loc
  (HIST l.205), s_5 and α_E (SF l.870, RLARGE l.455).
- **∝ ε_1^{−2}** — n_* (RLARGE l.1017), n_H (l.612), u_0 (EXISTENCE l.3556).
- **logarithmic** — wrap levels, the torus-caveat level count, the coherent-chain depth.

**and two exceptions, both steeper than the declared price, both found here:**

- **∝ ε_1⁴**: a_η = η_1²/4 (**RLARGE l.1248**) and hence **a_RS = min{a_η, κε_1²/(256N)}** (**RLARGE
  l.1020**), because η_1 = ε_1²/(512NA_d) is itself quadratic. The ε² entry never binds (it would need
  ε_1 > 814). **SF.md l.2203 and l.2582 already tabulate this as "HIST n_♯, RS route (η_1 quadratic) |
  ε_1^{−4}"** — an independent record, written for a different question.
- **∝ ε_1^{−3}**: the Cauchy C³ constant of §2.3 [ARGUED].

---

## §3. E1-C — pricing the large-field region, with numbers

TAUFLAT's named worry: *"lowering ε_1 **enlarges the large-field region** (χ_Q's indicator, RLARGE l.58)"*.
Quantified, from the lane's own formulas. [COMPUTED; the probe is **POST-HOC**, `checks/e1c_out.txt`,
and carries no pre-registered verdict.]

### §3.1 What grows, and by exactly how much

| quantity | formula and citation | at ε_1 = 6.7·10⁻⁴⁰ | at the proposed ε_1 | change |
|---|---|---|---|---|
| per-bad-cube suppression rate | ε_1²/(4N), **RLARGE l.943**, **PROOF l.1917** | 5.6113·10⁻⁸⁰ | 1.1010·10⁻⁸⁹ | **−9.707 decades** |
| defect exponent a_bad | **RLARGE l.88** | 2.4970·10⁻⁸⁵ | 4.8993·10⁻⁹⁵ | −9.707 |
| returned exponent a_ret | **PLD l.1595**, **HW l.1635** | 2.0051·10⁻⁹¹ | 3.9341·10⁻¹⁰¹ | −9.707 |
| **a_RS (RS/joint route)** | **RLARGE l.1020** | 5.9314·10⁻¹⁶⁶ | 2.2834·10⁻¹⁸⁵ | **−19.415** |
| n_* (returned-cluster size) | **RLARGE l.1017** | 4.2584·10⁸⁰ | 2.1703·10⁹⁰ | +9.707 |
| n_H | **RLARGE l.612** | 2.0670·10⁸⁷ | 1.0535·10⁹⁷ | +9.707 |
| **wrap levels** log_L(2n_H) | **RLARGE l.612** | **183.6** | **204.0** | **+20.3 levels** |
| **torus-caveat levels** log_L(n_*^{1/4}) | REVIEW_SF_S5 Part E, **SF l.2205** | **42.2** | **47.3** | **+5.1 levels** |
| **coherent-chain depth** log(2/ε_1)/(2 log L) | **PLD.md l.2307**, l.1888 | **41.4** | **46.5** | **+5.1 levels**; the constant 81^depth goes 10^78.9 → 10^88.7 |
| u_0 = 64/ε_1² (allowance floor) | **EXISTENCE.md l.3556** | 1.4257·10⁸⁰ | 7.2663·10⁸⁹ | +9.707 |

### §3.2 Does anything that consumes the region's SIZE break, or just get more expensive?

> **It gets more expensive, and the expense is paid entirely in g. Nothing breaks.** [COMPUTED]

The region's expected size is ~L^{4(K−k)}e^{−ε_1²/(4Ng_k²)} per unit physical volume (**PROOF l.4307**,
rate from **RLARGE l.943**). The exponent ε_1²/(4Ng²) is:

- **exactly invariant** if g sits at the ε-driven ceiling: **2.90218·10¹⁶ → 2.90218·10¹⁶** (e1c (1));
- at the ε-independent DX′ coupling: **2.28471·10⁷² → 4.48276·10⁶²**, so the number of levels K−k over
  which the small-field region survives falls from **1.197·10⁷²** to **2.349·10⁶²**. Against the wrap
  requirement of ~205 levels (§3.1) that leaves **60.06 decades of margin** (e1c (2)).

**The three named consumers of the region's size, individually:**

1. **RLARGE's large-field renormalisation.** (RLF-0) needs counterterms for every shape of ≤ n_* cubes:
   n_* rises ×5.097·10⁹. This is an existence statement about constants bounded by C^{|Y|}e^{−a|Y|/g_k²}
   (RLARGE l.136), so it costs nothing but the g-ceiling. **(RLF-3)**'s history sum needs
   (n_*+1)aβ_- > 4, which is how n_* is defined, so it is preserved by construction. **More expensive,
   not broken.**
   *The one qualitative item:* **the (SF-last)/torus clause** — "clusters ≤ n_* cubes must fit the
   level-k torus … **'shapes up to translation' fails for wrapped clusters**" (REVIEW_SF_S5 Part E, row
   "RLF torus clause"), affecting the last **42.2 → 47.3** levels. This is **already an open, recorded
   conflict** (RLARGE l.613-614 calls (SF-last) "a many-level item", l.792 "Chosen: many-level,
   K-independent"); option C adds **5.1 levels** to a count the lane has already chosen to carry as
   many-level. **No kind-change.**
2. **The HW column counts.** b_n, b_D, c_f, c_att, Δ_ρ², n_int, the ×82 ring — **every one is pure
   geometry and contains no ε_1** (HW l.2004: *"b_n = C_sh·81·h_n·c_+ + h′_n·c_U"* with
   (C_sh, h_n, h′_n, h_D) = (81, 10002, 10001, 10000)). **Unchanged.** Only n_T = n_♯ moves, ∝ ε_1^{−2}.
3. **PLD's defect pricing.** a_A := min{λκε_1²/256, 6θa_bad, a_ns} falls ×1.962·10⁻¹⁰ (both ε-driven
   entries scale identically, so the min does not change branch), while
   C_A := k·max{n_int(1−λ)^{−3/2}e^{λκε_1²R/256}, c_sf, …} **improves**, since its two ε_1-bearing entries
   are exponentials that fall to 1. The product constraint C_Ae^{−a_Au_k} < 1 is the g-ceiling again.
   **More expensive, not broken.**

### §3.3 The lane has already priced ε_1 far below this proposal, three times

This is the strongest independent evidence available, and none of it was written for this question:

| exercise | ε_1 used | how far below the proposal |
|---|---|---|
| **REVIEW_SF_S5 Part E** (grepped every lane) | ≈ 4.3·10⁻⁵⁹ | **14 decades below** |
| **SF.md §16.3 table l.2199-2206** | 1.81·10⁻¹⁰² | **57 decades below** |
| **SF.md §19.4 table l.2578-2583** (RSF6-fix TH-2) | 5.95·10⁻⁷⁷/C_♭ | **32 decades below** |

All three conclude the derived constants are "finite, g-independent and K-independent" and that no lane
needs ε_1 bounded below. **Option C is a 4.854-decade move into territory the lane has already mapped
three times at 14-57 decades lower.** That does not make it safe — the ceilings have moved since — but it
means the proposal is not novel territory, and §2.2's floor is the only thing those exercises missed.

---

## §4. E1-D — verifying the declared price against CURRENT numbers

### §4.1 The five declared figures [e1-3; **one pre-registered verdict did NOT pass**]

Recomputed from the owning files' formulas at the proposed ε_1, tolerance ×1.2 pre-registered:

| figure | TAUFLAT §4 C l.411-413 | mine (exact) | ratio | verdict |
|---|---|---|---|---|
| a_bad 2.5e-85 → | **5.0·10⁻⁹⁵** | 4.89929·10⁻⁹⁵ | 0.97986 | ok |
| a ≲ | **2·10⁻⁹⁶** | 2.04137·10⁻⁹⁶ | 1.02069 | ok |
| n_H 2e87 → | **10⁹⁷** | 1.05348·10⁹⁷ | 1.05348 | ok |
| wrap 184 → | **205** | **204.0** | −1.0 level | ok in kind |
| g_K² 1e-88 → | **10⁻⁹⁸** | 2.04137·10⁻⁹⁸ | **2.04137** | **OUTSIDE ×1.2** |

> **[E1-3] SOURCE-DISAGREES on g_K², reported as a FAIL.** The formula g_K² ≲ a/10² (**RLARGE l.617**)
> gives 2.04·10⁻⁹⁸, not 10⁻⁹⁸. The cause is benign and the **direction is favourable to the proposal**:
> TAUFLAT wrote "≈ 10⁻⁹⁸", one significant figure, exactly as RLARGE l.617 writes "≈ 10⁻⁸⁸" for
> 1.04·10⁻⁸⁸. **TAUFLAT's figure overstates the price by ×2.04.** No conclusion changes.

**Two transcription notes, disclosed rather than folded in.**
- g²_CRC(E_t) at the ×82 ring reproduces **HW.md l.2006's 1.85835·10⁻⁹⁶ to ×1.0404** — the 4 % is HW's
  own rounding of a to 1.0·10⁻⁸⁶ where c_prε_1²/24 gives 1.04042·10⁻⁸⁶. The b_n = 5381106005 and the
  ln 12800 additive term are transcribed from HW l.2006 and l.1639 unaltered.
- **n_*(8.95·10⁻⁴⁰) = 2.386·10⁸⁰ against RLARGE l.611's 1.19·10⁸⁰ — ×2.005.** A factor exactly 2;
  RLARGE's figure is "v1's n_* formula", mine is l.1017 + l.1245's a″ = 0.9ε_1²/(4N). **SOURCE-DISAGREES
  ×2.0, consequence nil**: n_* enters only through log_L(n_*^{1/4}), where ×2 is 0.16 of a level.

### §4.2 **PRICE-INCOMPLETE** — the declared list omits the two steepest exponents

[e1-3, second pre-registered line.] TAUFLAT's declared price list contains only ∝ ε_1^{±2} quantities.
The sweep finds two steeper ones:

- **a_RS and a_η ∝ ε_1⁴** (**RLARGE l.1020, l.1248**): **19.415 decades, not 9.707.**
- **the Cauchy C³ constant ∝ ε_1^{−3}** (§2.3): **14.561 decades** [ARGUED].

### §4.3 **Re-verifying RLARGE l.617-618's "these do not bind"** [e1-4; **the check FAILS, and it is the audit's second real finding**]

RLARGE l.617-618: *"g_K² ≲ a/10² ≈ 10⁻⁸⁸ … This is far above the binding DX′ ceiling g_0² ≲
2.5·10⁻¹⁵²/C_Ω …, so **RLF's own ceilings do not bind** at the current constants."*

| ceiling | at E_t | at the proposed ε_1 | margin over DX′ (2.456·10⁻¹⁵², REVIEW_SF_S7 l.203) | verdict |
|---|---|---|---|---|
| RLARGE a/10² (l.617) | 1.0404·10⁻⁸⁸ | 2.0414·10⁻⁹⁸ | **63.63 → 53.92 decades** | NOT-BINDING |
| g²_CRC, ring ×82 (HW l.2006) | 1.9335·10⁻⁹⁶ | 3.7936·10⁻¹⁰⁶ | **55.90 → 46.19 decades** | NOT-BINDING |
| HIST-side (REL-boot / HIST-sum; HW l.2024) | 5.0338·10⁻⁹⁷ | 9.8768·10⁻¹⁰⁷ | **55.31 → 45.60 decades** | NOT-BINDING |
| g²_ret (HW l.2008) | 3.6764·10⁻⁹⁸ | 7.2134·10⁻¹⁰⁸ | **54.18 → 44.47 decades** | NOT-BINDING |
| **RS/joint a_RS/10² (RLARGE l.1020)** | **5.9314·10⁻¹⁶⁸** | **2.2834·10⁻¹⁸⁷** | **−15.62 → −35.03 decades** | **BINDS-ALREADY** |
| RS/joint under KN-step's linear η_1 (EXISTENCE l.1771) | 8.1982·10⁻⁸⁶ | 1.6085·10⁻⁹⁵ | **66.52 → 56.82 decades** | NOT-BINDING |

> ### **[E1-4] FAIL. The claim "RLF's own ceilings do not bind" is TRUE for the exponent RLARGE names and FALSE for a_RS, already today.**
>
> **SOURCE-DISAGREES with RLARGE l.617-618.** l.617 is scoped (*"on the (REG-min) route"*) and correct
> there; **l.618's unscoped "RLF's own ceilings do not bind" is not**. a_RS's ceiling sits **15.62 decades
> BELOW DX′ at today's ε_1** and **35.03 decades below** at the proposed one. **Option C does not create
> this; it inherits it and deepens it by 19.415 decades.**
>
> **It is repairable, by a route already PROVEN in the lane.** Adopt **KN-step's re-centred dichotomy,
> η_1 := c_1ε_1 with c_1 = 1/(2(L² + 5.5A_d))** (**EXISTENCE.md l.1771**; Lemma KN and Corollary KN-step
> are listed PROVEN-HERE at **RLARGE l.633**; **REVIEW_PLD_S3 l.462 (E9)** already asks RLARGE to adopt
> it). That makes η_1 linear, a_RS ∝ ε_1² like everything else, and the ceiling **+56.82 decades above
> DX′ at the proposed ε_1** — a gain of **92 decades**. This is condition **(C2)** of §5.

### §4.4 The DX′ margin itself

**SOURCE-DISAGREES, mildly, with TAUFLAT §4 C l.417**'s *"a 54-decade margin, of which this costs ≈ 10"*.
The margin **today** (RLARGE's own a/10² against DX′) is **63.63 decades**; **54** is the figure **after**
the move (53.92). Both numbers are in TAUFLAT's sentence doing different jobs. The honest form:
**63.63 decades now, 53.92 after**, and **all of it conditional on c_+·C_Ω**, which is unevaluated
(**REVIEW_SF_S7 l.225**: *"C_Ω … is an explicit hand constant, not a certificate"*; PLD l.1902: c_A
uncertified). The margins are exhausted at **c_+·C_Ω = 8.31·10⁵³** (RLARGE's ceiling) or
**1.54·10⁴⁶** (g²_CRC ×82) at the proposed ε_1, against **4.24·10⁶³** and **7.87·10⁵⁵** today.

**Current numbers used, not pre-session-24 ones**, as the brief required: HW session 6's §35.7 table at
the **×82 ring** (b_n = 5381106005, g²_CRC = 1.85835·10⁻⁹⁶/c_+), which is PLD session 7's settled price
for the **closed column** — the application the proof makes (HANDOFF "Two cross-lane disagreements",
item 1). NORMS.md l.746's "g²_CRC ≈ 4.9·10⁻⁹⁷/c_+" is session 5's and is stale.

### §4.5 **The proposed value is quoted 9.46·10⁻⁷ ABOVE its own requirement**

[`checks/e1b_out.txt`.] The exact requirement 4C_3ε_1² ≤ η_♭ at C_3 = 1 gives

> **ε_1 ≤ √(η_♭/4) = 9.38495112638·10⁻⁴⁵** (exact to the digits shown; η_♭ = 3.52309230578·10⁻⁸⁸),
> i.e. **4.8536 decades** below 6.7·10⁻⁴⁰.

TAUFLAT §4 C l.408 quotes **9.38496·10⁻⁴⁵**, which is **1.000000946×** the bound, so **the clause FAILS at
the quoted value**, by 8.21·10⁻⁷ decades of energy. This is a rounding in the unsafe direction and it is
the whole reason check **e1-5 returned NO POWER on its first run** (§6). Trivial in size; **it must still
be corrected in the recommendation, because a ceiling quoted above its own bound is exactly the defect
TAUFLAT's own §6.6 is about.**

---

## §5. VERDICT on option C

> ### **SAFE WITH NAMED CONDITIONS.**

Not SAFE outright: one pre-registered check failed (§4.3), one floor exists that the proposal's author did
not have (§2.2), the declared price is incomplete (§4.2), and the quoted value is on the wrong side of its
own bound (§4.5). Not UNSAFE: **no floor-side consumer is violated, no ratio reverses, no hypothesis
anywhere fails at the proposed value, and the large-field region's cost is paid entirely in a coupling
ceiling that keeps 44-60 decades of margin.**

**The conditions, each with its owner and the quantity it constrains:**

- **(C1) Scope the change to ε_1^cut.** State it as "RLARGE §0's χ_Q threshold", explicitly **not**
  BFT_B's Theorem N2 threshold (BFT_B l.3058, l.2870) and not FLOW's disc radius (FLOW l.1927, l.2834).
  Owner: the lead. §1.
- **(C2) Adopt KN-step's linear η_1 first, or scope RLARGE l.618.** Either adopt η_1 := c_1ε_1
  (EXISTENCE l.1771; REVIEW_PLD_S3 E9) so that a_RS becomes ∝ ε_1², **or** record that the RS/joint
  route's ceiling already sits 15.62 decades below DX′ and will sit 35.03 below after the move. Owner:
  RLARGE. §4.3. **This is the binding condition; everything else is bookkeeping.**
- **(C3) Record that the floor is ε_1 ≫ g, not "none".** Margin 36.63 → 31.78 decades at the DX′
  coupling. The clauses that live on it are EXISTENCE l.3112 (CLS-cone's coercivity window), EXISTENCE
  l.4191 and PLD l.995's ℓ¹ absorption margin 2m_*g/ε_1, which loses 4.854 decades at the DX′ coupling.
  Owners: EXISTENCE and PLD. §2.2.
- **(C4) Use 9.38495·10⁻⁴⁵ or lower, not 9.38496·10⁻⁴⁵.** §4.5.
- **(C5) Price the two steeper exponents.** a_RS ∝ ε_1⁴ (19.415 decades) and the Cauchy C³ constant on
  𝔇_{α_E} ∝ ε_1^{−3} (14.561 decades, ARGUED). Owners: RLARGE, HIST. §4.2.
- **(C6) Re-evaluate the ε_1 number first.** Four live values are in force (§1.1); NORMS.md's
  k-independence argument is written at 1.27·10⁻³⁹. Fix the number before lowering it.
- **(C7) The whole verdict is CONDITIONAL on c_+·C_Ω ≲ 1.5·10⁴⁶** (g²_CRC at the ×82 ring) **and on DX′
  remaining the binding programme ceiling.** Both are uncertified hand constants (REVIEW_SF_S7 l.225;
  PLD l.1902).

**What option C does NOT disturb, verified rather than assumed:** consumers 4 and 5 of DESC-ε (HW TE (ii),
RLARGE §3.3 branch (iii)) keep the ε_1 < t_pr branch, improved from ×1.99 to ×142125 (TAUFLAT §3.1);
RLARGE's a_bad stays in the c_prε_1² branch (RLARGE l.93); (TC)/U3 is exactly invariant (§2.3); HW's b_n,
b_D, c_f, c_att, the ×82 ring and every column count contain no ε_1 (§3.2); AE-red's own number gains
9.707 decades on its 63.00 of margin; DX′, the hole ceiling, FS-1, the band window and a_*^B are
τ_c-driven and unmoved (SF l.2587).

**One side benefit, since the audit found it:** the (CEM-2)-shaped gap ε_1²/g_K² — HW l.2170's
4.489·10¹⁵, reproduced exactly — **improves by 9.707 decades** at the ε_1-independent DX′ coupling
(1.828·10⁷³ → 3.586·10⁶³). HANDOFF's critical-path item 3 names that gap. PLD session 7 has since
dissolved (CEM-2), so this is a benefit to a question that may no longer be asked.

**I have not changed ε_1 anywhere, and I do not recommend that it be changed.** Option C is a decision for
RLARGE's and SF's owners and for the lead. This file supplies the facts it was blocked on.

---

## §6. Checks, provenance, disclosures, and the two FAILs

Files written by me: **this file**, `checks/e1_criteria.md`, `checks/e1_sweep.py`, `checks/e1_out.txt`,
`checks/e1_time.txt`, `checks/e1_run1_abort_out.txt`, `checks/e1_run1_abort_err.txt`,
`checks/e1b_power.py`, `checks/e1b_out.txt`, `checks/e1b_run1_abort.txt`,
`checks/e1c_largefield_posthoc.py`, `checks/e1c_out.txt`. **Nothing else, anywhere. No git command was
run by me.**

Order, by mtime, converted to UTC (the host clock is UTC−4; §0's stamp 14:43Z was read from `date -u`
immediately before writing it, and the file landed at 14:43:5x): **EPS1_SWEEP.md §0 14:43Z** →
`e1_criteria.md` **14:56:57Z** → `e1_sweep.py` **14:59:51Z** → `e1_out.txt` **14:59:59Z** →
`e1b_power.py` / `e1b_out.txt` **15:01:28Z** → `e1c_*` **15:02:58Z** → §1-§7 of this file. The ordering is
clean and it is the point: **the pre-stated section precedes everything by 13 minutes, and the criteria
precede the first script by 3 minutes.**

**Disclosure on provenance.** This file has been appended to since §0 was written, so its mtime is now
that of the last append and **the 14:43Z creation time of §0 is not demonstrable from the filesystem** —
only the check files' order is. I record this rather than quietly relying on it, which is the convention
EPSSTAR §8.1, STAR_CONST §12 and TAUFLAT §5.2 set for provenance in this lane. What *is* demonstrable is
that `e1_criteria.md` (which contains no constant at all) precedes every script, and that §0 cites no
quantity from session 24 and no number of any kind. Two runs aborted on display-formatting type errors
before producing any verdict; both logs are kept and neither produced a number used above. One further
display-only line in `e1b_power.py` was repaired after its first abort; the arithmetic and the
pre-registered question were not touched.

| id | pre-registered verdict | result |
|---|---|---|
| **E1-A** | symbol identity: ONE-SYMBOL or SEVERAL | **SEVERAL — at least five** (§1) |
| **e1-1** | CLASSIFICATION-HOLDS / -WRONG | **CLASSIFICATION-HOLDS**, 18/18 rows exact |
| **e1-2** | FLOOR-RESPECTED / FLOOR-VIOLATED | **FLOOR-RESPECTED** — 31.78 decades at DX′, invariant at the ε-driven ceiling |
| **e1-3** | SOURCE-REPRODUCED within ×1.2 | **SOURCE-DISAGREES** on g_K² (×2.04, favourable direction); **PRICE-INCOMPLETE** |
| **e1-4** | NOT-BINDING / BINDS | **FAIL — BINDS-ALREADY** for a_RS (−15.62 today, −35.03 after); four other ceilings NOT-BINDING |
| **e1-5** | both counterfactuals must flip, else NO POWER | **NO POWER on the first run**; **HAS-POWER** on re-run `e1b` (§6.1) |
| **e1-6** | verdicts identical at two precisions | **PASS** (40 and 80 digits) |

### §6.1 The power check, honestly

**First run: NO POWER, reported as such.** `e1_sweep.py` returned NO POWER because the DESC-ε (iii)
verdict did not flip between the proposed ε_1 and today's: it was CLAUSE-FAILS at **both**, since
TAUFLAT's quoted 9.38496·10⁻⁴⁵ is 9.46·10⁻⁷ above its own bound (§4.5). Output and script kept unaltered
(`e1_out.txt`).

**Re-run under a new id, criteria untouched** (`e1b_power.py`, `e1b_out.txt`): substituting the **exact**
bound 9.38495112638·10⁻⁴⁵ for TAUFLAT's rounded figure and changing nothing else,

- the **floor** verdict flips: FLOOR-RESPECTED at the proposal, **FLOOR-VIOLATED** at the counterfactual
  ε_1 = 10⁻⁸⁰ (4.20 decades below g_DX = 1.567·10⁻⁷⁶, where the window g ≪ ‖·‖ < ε_1 closes);
- the **clause** verdict flips: CLAUSE-HOLDS at the exact bound, **CLAUSE-FAILS** at today's ε_1;
- **HAS-POWER.**

**What each check is tested against, as §0.6 required.** The floor check is tested against
**EXISTENCE.md's own window statements** (l.3112, l.4191) — a *different lane* from the one proposing the
change, and a statement written for the (RLF-3^dis) threshold question, not this one. e1-3 and e1-4 are
tested against **HW.md §35.7's constants table** (written to answer the ring question) and **SF.md
§16.3/§19.4's ε_1-scaling tables** (written to answer the τ_c question); neither was written for option C,
and SF's tables independently supply the ε_1^{−4} exponent that §4.2 reports as missing from the declared
price. e1-1 is tested against the definitions in the owning files, not against any summary line.

**Power grading, honestly.** e1-1 and e1-6 are **weak** checks: e1-1 verifies my own classification
against my own formulas, so it can only catch a bookkeeping slip, and it would pass trivially had I
claimed no exponents. Its value is that it is the *input* to e1-4, which is **strong**: e1-4 can and did
return a FAIL, against a claim (RLARGE l.618) written by a different author for a different purpose.
e1-2 is **strong** — it flips, and the flip is at a boundary (ε = g_DX) that no quantity in this session
set. e1-3 is **medium**: it compares two transcriptions, so it catches rounding and omission but not a
modelling error.

### §6.2 What these checks cannot catch, stated rather than left implied
They cannot validate RLARGE's ε_1 ceiling, SQ's derivation of η_♭, HW's b_n or ring price, PLD's λ_min, SF's
DX′ evaluation, or the unevaluated C_Δ, C_♭, r_♭, C_Ω, N′, c_A. A number reproduced here is **not** an
endorsement of its source. They cannot find a consumer that uses ε_1 without naming it; the enumeration is
COMPUTED only over §2.0's search domain. And **the ε_1^{−3} Cauchy C³ item of §2.3 is ARGUED, not
computed**: HIST l.862 says the C³ bounds follow by Cauchy on 𝔇_α but does not write the constant, so the
α_E^{−3} is the standard estimate supplied by me.

### §6.3 Numerics
Exact `fractions.Fraction` throughout; `Decimal` only to display, checked at 40 and 80 digits; plain
`python3 -I`, single thread, OMP/OPENBLAS/MKL = 1, nice 10, no numpy, no BLAS. **0.04 s real, three runs.**
**No numeric lock taken and none needed** (exact rational arithmetic, brief rule 6). Two runs aborted on
display-formatting type errors before producing any verdict; both logs are kept
(`e1_run1_abort_*.txt`, `e1b_run1_abort.txt`) and neither produced a number that appears anywhere above.

### §6.4 The single biggest remaining obstruction in my scope
**None that is mine to close** — this was an audit and it is closed. The obstruction it hands on is
condition **(C2)**: **the RS/joint route's a_RS is quartic in ε_1 and its coupling ceiling already sits
15.62 decades below the programme's binding one.** That is independent of option C, it is a live defect in
RLARGE l.617-618's unscoped sentence today, and the fix is a lemma the lane has already proven
(EXISTENCE's KN-step) and already been asked to adopt (REVIEW_PLD_S3 E9) and has not. The deeper pattern is
the one HANDOFF's closing paragraph names: **three of this audit's four findings are quantities someone
fixed once and nobody revisited** — four live values of ε_1, a scoped sentence read unscoped, and a
ceiling rounded in the unsafe direction.

---

## §7. FOR OTHER FILES (not edited)

I wrote only this file and `checks/e1_*`, `checks/e1b_*`, `checks/e1c_*`. I did not touch TAUFLAT.md,
EPSSTAR.md, SQ.md, HW.md, PLD.md, RLARGE.md, HIST.md, SF.md, BFT_*.md, NORMS.md, GREENT.md, YSUP.md,
PROOF.md, HANDOFF.md, SESSION24_RESULTS.md, EXISTENCE.md or any REVIEW_* file. The following are requests.

### §7.1 For RLARGE's owner (binding, and it is the largest item on this list)
1. **l.618's "RLF's own ceilings do not bind at the current constants" is false as written.** It is true
   for the exponent l.617 names (a = θa_bad, margin 63.63 decades over DX′) and **false for a_RS**
   (l.1020), whose ceiling a_RS/10² = 5.93·10⁻¹⁶⁸ sits **15.62 decades BELOW** DX′ = 2.456·10⁻¹⁵²/C_Ω
   **today**. Suggested edit: scope the sentence to the (REG-min)/HW route, as l.617 already does, and add
   one line recording the RS/joint route's ceiling.
2. **Adopt KN-step's linear η_1** (EXISTENCE l.1771, PROVEN per your own l.633; REVIEW_PLD_S3 E9 asks for
   it). η_1 = min{ε_1/(2L²), ε_1²/(512NA_d)} makes a_η = η_1²/4 **quartic** in ε_1; c_1ε_1 makes it
   quadratic, and the ceiling moves from −15.62 to **+66.52** decades against DX′ — a gain of 92 decades
   at today's ε_1, and the difference between SAFE-WITH-CONDITIONS and a second breach under option C.
3. **l.70-72's ceiling disagrees with SF l.2837 / NORMS l.746 (1.27·10⁻³⁹) and with your own l.611
   (8.95·10⁻⁴⁰).** Four live values of one symbol (§1.1). Please state which is in force.
4. **l.611's n_* = 1.19·10⁸⁰ at ε_1 = 8.95·10⁻⁴⁰ is ×2.005 below l.1017 + l.1245's formula** (2.386·10⁸⁰).
   Consequence nil (n_* enters as log_L(n_*^{1/4})), but it is a transcription to reconcile.
5. **U3 (l.811, l.85) is unaffected by option C.** ε_loc/ε_1 = 1/√(4Nb_1) = 7.0·10⁻³ is **ε_1-independent**,
   and (TC)'s requirement is ≥ 35/256 = 0.1367, so (TC) fails by **×19.53 at every ε_1**. Worth recording
   so nobody tries to fix U3 by moving a threshold.
6. **U7 (l.815)** — if ε_1 moves, note that ε_1 < t_pr goes from ×1.99 to ×142125, so the (CLS-min) source
   question stops being marginal.

### §7.2 For SF.md's owner
1. **Your own §16.3 (l.2199-2206) and §19.4 (l.2578-2583) tables already answer most of this audit**, at
   ε_1 values 14-57 decades **below** what option C proposes, and they already carry the **ε_1^{−4}** row
   that TAUFLAT's price list omits. Please point RLARGE at them.
2. **l.2587's "(GF-B^𝔥) drives only the τ_c rows … not ε_1" is the fact that makes option C affordable**
   and the fact that makes its floor cost real: because DX′ is τ_c-driven, g does **not** fall with ε_1 at
   the binding ceiling, so the window ratio ε_1/g loses the full 4.854 decades (36.63 → 31.78). Worth one
   sentence, since it cuts both ways.
3. **l.870's s_5 ≤ min{ε_1/5, 0.01}**, with RLARGE l.455's α_E ≤ s_5/4 and HIST l.857's α_E ≥ cε_1, pins
   **α_E ≍ ε_1**. The Cauchy C³ constant on 𝔇_{α_E} is then ∝ ε_1^{−3} — **14.561 decades** under option C.
   Please confirm or refute; I have it as ARGUED.

### §7.3 For HIST's owner
1. **l.862's "C³ bounds in the data follow by Cauchy on 𝔇_α"** is the only place in the lane with an
   ε_1^{−3}. Please write the constant explicitly, so the next worker can price it. §2.3, §4.2.
2. **[GAP S2-2] (l.857-859) is unaffected**: α_E/ε_1 is invariant, so "m > 4α_E/ε_1" bites at the same
   polymer size. No edit needed; recorded so it is not re-opened.
3. **l.181's "for ε_1 → 0, η_q/η_1 = 2/ε_1"** is exactly the joint-vs-RS gap that §7.1 item 2 asks RLARGE
   to close. Your own file already names the mechanism.

### §7.4 For PLD's owner
1. **l.995's ℓ¹ absorption margin 2m_*g/ε_1 is the one ratio in the lane with the unhelpful sign.** At the
   ε-driven coupling ceiling it is invariant; **at the DX′ coupling it loses 4.854 decades** under option
   C. Finding 1 (SG-F3) calls the ℓ¹ term load-bearing, so please say whether 4.854 decades of it matters.
2. **l.2307 / l.1888's coherent-chain depth** goes **41.4 → 46.5** and the constant 81^depth goes
   10^78.9 → 10^88.7. Your own text says "even 81^{41.4} ≈ 10^{79} is a constant"; at 10^88.7 it is still
   annihilated by e^{−486·a·u_k}, because **a·u_k = 5.381·10⁹ is exactly invariant** under the scaling.
   One sentence would close it.
3. **§18.7.2's 4.489·10¹⁵ gap reproduces exactly** as ε_1²/g_K² at g_K² = 10⁻⁹⁴, and **improves by 9.707
   decades** at the DX′ coupling under option C. Recorded in case (CEM-2) is ever revived.

### §7.5 For the existence lane's owner (EXISTENCE.md)
1. **Your lane holds the only floor on ε_1 in the project.** l.4191's *"ε only has to contain the typical
   field ≍ g"* and l.3112's *"at distance ≫ g but < ε_1"* are the statements that make ε_1 ≫ g a real
   constraint. TAUFLAT §4 C l.404 and §6.4 record "no lower bound on ε_1 … in RLARGE, HW, SQ, HIST or
   PROOF" — correct for those five files, and **your lane is the exception.** Margin: **36.63 decades
   today, 31.78 after option C.** Please confirm the reading.
2. **l.3556's u_0 = 64/min{δ_3, ε_1}²** rises 9.707 decades to 7.27·10⁸⁹, i.e. g² ≤ 1.38·10⁻⁹⁰ — above the
   binding ceiling, so not binding.
3. **l.1692's non-triviality clause is helped**, not harmed: Haar{‖W−1‖ > ε_1} → 1 as ε_1 falls.
4. **Lemma KN / Corollary KN-step (l.1771) is the fix RLARGE needs** (§7.1 item 2). It may be worth saying
   so in your own file, since the gain is 92 decades on a ceiling in another lane.

### §7.6 For the lead (HANDOFF.md, SESSION24_RESULTS.md, PROOF.md)
1. **Option C is SAFE WITH NAMED CONDITIONS, not safe outright.** The conditions are §5 (C1)-(C7); the one
   that is more than bookkeeping is **(C2)**, the a_RS quartic.
2. **ε_1 is at least FIVE symbols** (§1), and the dangerous collision is **BFT_B l.3058's Theorem N2
   threshold**, which is defined by an O(1) formula and must not be moved. If option C is written up as
   "lower ε_1", lane B will read it as addressed to them. Write it as "lower RLARGE §0's χ_Q cut".
3. **There IS a floor, in the existence lane** (§2.2): ε_1 ≫ g. It is respected, with 31.78 decades. The
   project's standing record "no lane needs ε_1 bounded below" (REVIEW_SF_S5 l.332, SF l.2207) should be
   amended to "no lane needs ε_1 above a g-independent constant; the window ε_1 ≫ g is the floor".
4. **RLARGE l.617-618 has a false sentence today, independent of option C** (§4.3). That is the audit's
   most consequential by-product and it belongs in SESSION24_RESULTS.md's ledger.
5. **TAUFLAT's quoted 9.38496·10⁻⁴⁵ fails its own clause** by 8.21·10⁻⁷ decades; the bound is
   **9.38495112638·10⁻⁴⁵**, 4.8536 decades below 6.7·10⁻⁴⁰ (§4.5). Trivial in size, and exactly the class
   of defect TAUFLAT's own item is about.
6. **The large-field worry TAUFLAT gated on is real but cheap** (§3): +20.3 wrap levels, +5.1 torus levels,
   +5.1 chain-depth levels, and a suppression exponent that is **exactly invariant** at the ε-driven
   coupling and keeps **60.06 decades** of margin at the ε-independent one. Nothing of a different kind.
7. **Four live numerical values of ε_1 are in force in four files** (§1.1). Settling that is a smaller job
   than lowering it, and should come first.

*(End of EPS1_SWEEP.md. Files written by this worker: this file, `checks/e1_criteria.md`,
`checks/e1_sweep.py`, `checks/e1_out.txt`, `checks/e1_time.txt`, `checks/e1_run1_abort_out.txt`,
`checks/e1_run1_abort_err.txt`, `checks/e1b_power.py`, `checks/e1b_out.txt`,
`checks/e1b_run1_abort.txt`, `checks/e1c_largefield_posthoc.py`, `checks/e1c_out.txt`. Nothing else,
anywhere. No git command was run by me.)*
