# EPSSTAR: pinning ε_* — turning A_c·γ_c from a condition into a number

Worker: the (EPS-STAR) agent of session 24. I own this file and `checks/es1_*` only. I have written nothing else
anywhere, and I will not. No git command has been run by me.

---

## 1. PRE-STATED (first edit of this file, 2026-10-28 14:00:05 UTC)

**This section is the very first edit to this file. It contains STATEMENTS ONLY. It contains no derivation of my
own and no number computed by me.** The only numbers quoted below are (a) thresholds and values handed to me in
my brief, (b) numbers landed in **CONST_T.md** and **STAR_CONST.md** before this file existed (both are
session-24 files, landed earlier today; I follow STAR_CONST §1.1's own precedent of quoting the numbers its brief
handed it and naming them as inherited), and (c) numbers written in **SQ.md §15.0-§15.1** and **REVIEW_SQ_S4**,
both of which pre-date session 24. Everything below §1 was written after this section was on disk.

### 1.1 The task, as I received it

CONST_T.md §6.1 proves, given (★):

  **C_T = √6 · F · B(4a) · [ ½(A_sγ_s)^a + ½(A_cγ_c)² + 288·C_1·Q ],  a = q/(q−4),**

and STAR_CONST.md has now supplied the (★) constants: C_1 = 5.70·10³, C_V^source = 7.23·10⁻²,
C_1·C_V^source = 411.92 ≤ 412 (floor 319.20), with q_min = 11 (conservative β-power) or 10. **The last symbol is
A_c·γ_c**, which lives in **step (5)** of SQ.md §15.1 — Stage 1, l.1489-1494 — outside steps (2)-(4), which is
why STAR_CONST could not reach it. STAR_CONST §8.3 therefore states a *condition*, not a value:

  **A_c·γ_c ≤ 3.4·10³**   (3.35·10³ at q = 12, 4.4·10³ at q = 16, 4.5·10³ for q ≳ 30, all under P-max)

and records that CONST_T's SUPPLIED reference value **A_cγ_c = 236.9·C_1 = 4.7·10³ at C_1 = 20 just fails it**, so
that ε_* must fall by a factor of 2-10 below CONST_T's SUPPLIED 10⁻⁴. REVIEW_SQ_S4 S4-16 records ≈ 30 decades of
headroom in ε_*, so STAR_CONST calls this free, while stating it as a condition.

**My job: establish A_c·γ_c ≤ 3.4·10³ rigorously by an admissible choice of ε_*, and check that lowering ε_*
breaks nothing downstream.**

### 1.2 What I will do

E1. **Expand step (5) (l.1489-1494)** and write A_c and γ_c explicitly as functions of ε_* and of whatever else
    they depend on (the Stage-1 ℓ⁴←ℓ² constant, the neighbourhood multiplicities, the three (★) coefficients).
    Label every constant FORCED or CHOICE.
E2. **Write out the Stage-1 absorption inequality** that *defines* ε_* (l.1491's "absorbed for ε ≤ ε_*"), since
    that inequality, not an arbitrary choice, is what an admissible ε_* has to satisfy.
E3. **Find the ε_* that gives A_cγ_c ≤ 3.4·10³, with margin**, and report the factor by which ε_* must drop
    below CONST_T's 10⁻⁴. Also report the ε_* that gives A_cγ_c ≤ 1, the reading STAR_CONST §6.3 assumed when it
    quoted C_T ≤ 5.3·10¹² at q = 12.
E4. **Audit every load-bearing use of ε_* in the lane for its DIRECTION.** Lowering a threshold weakens a
    hypothesis and therefore usually helps; it hurts wherever a statement needs ε_* large enough to *cover*
    something it is applied to, and wherever a ratio such as ε_1/ε_* or t_pr/ε_1 appears. I will search the lane
    files for every load-bearing use and check each direction separately. The values my brief names as relevant
    comparators are **θ_0 ≤ 1.46·10⁻¹³, τ_R ≤ 2.75·10⁻¹⁵, η_♭ ≈ 4.2·10⁻³⁶, t_pr ≈ 1.5·10⁻¹³, and PROOF's
    ε_* = 2.476·10⁻¹³/C_Δ (PROOF [SF7-edit])**. **If any consumer needs ε_* ABOVE my new value I will say so
    plainly: that would mean the ≈ 30 decades of headroom are not all usable, which is a real finding and I
    report it as one whatever it does to my own verdict.**
E5. **Carry STAR_CONST's β-power correction.** Its §6.4/§11.2 find a_c = 2 with a β⁴ coefficient on the V_c
    branch, so the telescope needs **B(4·max{a,2}) = B(8) = 1931.5 for every q ≥ 8**, not B(4a). I use that
    (P-max), not CONST_T §6.1's B(4a) (P-ct), and I report both.
E6. **Verify that the curvature coefficients staying SUPPLIED remains harmless.** STAR_CONST §8.4 item 1 records
    that C_B (BIA) and C_K′ (WB) are not pinnable from what SQ.md writes (C_K′ ≤ 1.92·10⁴ from counts the file
    calls crude; nothing at all for C_B), and §6.3 argues this is harmless for C_T. The curvature coefficients
    multiply a potential whose norm scales with ε_*, so this claim is exactly a claim about my quantity and I
    must check it rather than inherit it.
E7. **Report C_T at q = 12 and at neighbouring q** with my ε_*, as a number with a status label, and say plainly
    whether it is PROVEN or still CONDITIONAL and on what.

### 1.3 PRE-REGISTERED verdict table

Registered now, before any derivation and before any script. Every threshold in it is my brief's, STAR_CONST's or
REVIEW_SQ_S4's; none is mine.

| verdict | condition |
|---|---|
| **PASS** | an explicit ε_* > 0 is exhibited, admissible for step (5) (i.e. it satisfies the Stage-1 absorption inequality of E2), for which **A_cγ_c ≤ 3.4·10³** is PROVEN from step (5) as expanded; **AND** the E4 audit finds no load-bearing consumer requiring ε_* above that value; **AND** C_T at q = 12 under P-max is then a number **≤ 10¹³**. |
| **PASS-UNIFORM** | PASS, and in addition the ε_* that does it is expressible so that **C_T's number does not depend on C_B, C_K′ or c_N at all** — these move only ε_*. This is the strongest available outcome and is what would make CONST_T §6.1 a PROVEN number in the sense EPS-T needs (ε_* is existentially quantified in EPS-T, C_T is the thing that must be a number). |
| **PASS-CONDITIONAL** | A_cγ_c ≤ 3.4·10³ is reached, but only at an ε_* whose *value* cannot be written down because it depends on a SUPPLIED constant with no bound in SQ.md (C_B). C_T is then a number but ε_* is not; I must say which. |
| **FAIL-CONSUMER** | some load-bearing consumer needs **ε_* ≥ X** with X above the ε_* that A_cγ_c ≤ 3.4·10³ requires. Reported with the consumer named, the clash quantified in decades, and NOT rounded into a PASS. This is the outcome my brief singles out as "a real finding". |
| **FAIL-ARITH** | A_cγ_c ≤ 3.4·10³ is unreachable at every admissible ε_*: either the dependence on ε_* is not monotone, or Stage 1's own constant degrades as ε_* falls (a circularity), or the ε_*-free part of A_cγ_c already exceeds 3.4·10³. |
| **OPEN-STEP** | step (5) cannot be pinned without an estimate SQ.md does not contain. I must then name the step, name the missing estimate, and give the best rigorous bound available. This is a deliverable, not a failure to report. |

### 1.4 Things I state in advance that I will NOT do

- I will **not** edit SQ.md, CONST_T.md, STAR_CONST.md, NORMS.md, SQ_LOG.md, any REVIEW_* file, or any file other
  than this one and `checks/es1_*`. Several of those are under concurrent review. Requests for their owners go in
  a final "FOR OTHER FILES (not edited)" section.
- I will **not** change CONST_T.md §6.1's formula, its F ≤ 175.8, its B(m), its a = q/(q−4), its definition
  A := 36·C_1·|N|^{1/σ'} or γ := R^{2−4/σ}||V||_{ℓ^σ}, or its downstream chain (C_T′, A_0, G, C_D, C_err). I
  substitute into them. The one correction I apply on top is STAR_CONST's B(4·max{a,2}), as my brief directs.
- I will **not** re-derive (★). I take STAR_CONST's (★*) as given, with its three coefficients
  (c_s, c_K, c_RB) and prefactor c_g, and **I assume its two restatements of SQ.md §15.1** — V carrying three
  coefficients rather than one, and the source term's neighbourhoods being 3 plaquettes and 3 links rather than
  N_3 = 14406 or N_1 = 486 — exactly as my brief instructs, citing STAR_CONST §8.2 items 1-2 and its Lemmas
  A1-A3. **Everything I conclude is conditional on those two restatements** and I say so in my scope.
- I will **not** re-derive BIA (C_B), WB (C_K′), SOB (C_S = 3) or §15.0's R_1 bound, and I will not claim to have
  pinned C_B or C_K′. I will say exactly which numerical content of each I need and what happens if it is large.
- I will **not** re-optimise q, F or the radius schedule. q is CONST_T's lever and STAR_CONST has priced it.
- I will **not** declare ε_* "free" on the strength of REVIEW_SQ_S4 S4-16's "≈ 30 decades" without checking the
  individual consumers myself. That phrase is about one side of one inequality and my brief asks me to test it.

### 1.5 Pre-registered structural expectations (so that agreement is evidence and disagreement is reportable)

Written before any derivation or search. These are expectations, not claims.

- **Y1.** A_cγ_c will be **linear in ε_* to leading order**, with a subleading ε_*² piece from the (M_1u)² term,
  because γ_c is a norm of a potential bounded by the curvature and A_c is ε_*-free. If so, the factor by which
  ε_* must drop equals the factor by which A_cγ_c overshoots, and no optimisation is involved.
- **Y2.** Stage 1's constant will be **bounded uniformly for every ε_* below the absorption threshold**, so that
  lowering ε_* cannot raise it and there is no circularity. If this fails the verdict is FAIL-ARITH.
- **Y3.** The binding direction in the audit will be the **hypothesis-verification** direction: EPS-T is applied
  under ||𝒫||_{ℓ²(B_R)} ≤ ε_*, so every consumer that *verifies* that hypothesis needs ε_* to be at least as
  large as the curvature bound it actually has. I therefore expect the binding lower bound on ε_* to be the
  **largest** curvature bound any consumer can supply, and I expect it to be nearer 10⁻¹³ than 10⁻³⁶, i.e. I
  expect the usable headroom to be **about 8-10 decades, not 30**. If that is right, A_cγ_c ≤ 3.4·10³ is free and
  A_cγ_c ≤ 1 may not be.
- **Y4.** CONST_T's SUPPLIED A_cγ_c = 236.9·C_1 was evaluated at CONST_T's SUPPLIED C_1 = 20. STAR_CONST has
  since computed C_1 = 5.70·10³. I expect the honest starting value of A_cγ_c at ε_* = 10⁻⁴ to be **much larger
  than 4.7·10³** for that reason alone, so I expect the required drop in ε_* to be far more than the "factor of
  2-10" my brief quotes. **I register this now because it is a correction to the brief's framing and I want it
  on the record before I compute it.**

---

## 2. Scope, conventions, and what step (5) is

### 2.1 What I assume, named once

**(H1)** (★*), STAR_CONST.md §6.1, with its **three** coefficients and its prefactor:

> Σ|∇(ζW)|² ≤ β⁴[ Σ_p c_s·V_s·ζ̂²Ŵ² + Σ_p (c_K·M_3u + c_RB·(M_1u)²)·ζ̃²W̃² + c_g·g²·Σ_{supp⁺}W² ],
> **c_s = 411.9229708842423061, c_g = 5699.632830341894211** (STAR_CONST §7, exact),
> c_K = 17.51·C_K′·c_N, c_RB = 17.51·290·(576c_N² + C_B²c_N⁴), both **SUPPLIED**.

**(H2)** STAR_CONST's two restatements of SQ.md §15.1, §8.2 items 1-2 (proved there by its Lemmas A1-A3):
V carries three coefficients, not one; and the source group's neighbourhoods are
𝒩_S(p) = {p, p + e_{μ_p}, p + e_{ν_p}} (**3** plaquettes) and L(p) (**2** links, reverse count **3**), not
N_3 = 14406 or N_1 = 486. My brief instructs me to assume both. **Everything in §3-§7 is CONDITIONAL on (H2)**,
exactly as STAR_CONST's own §8.2 verdict is.

**(H3)** CONST_T.md §2.3-§2.5 downstream of (★): Lemma T, A := 36·C_1·|N|^{1/σ′}, γ := R^{2−4/σ}||V||_{ℓ^σ(B_R)},
Ĉ = ½(A_sγ_s)^a + ½(A_cγ_c)² + 288·C_1·Q, F ≤ 175.8, and (from STAR_CONST §6.4) the telescope factor
**B(4·max{a,2}) = B(8) = 1931.5 for every q ≥ 8** (P-max). I substitute into these; I do not change them.

**(H4)** REVIEW_SQ_S4 S4-3's added hypothesis sup_{p⊂B_R}||1 − U(p)|| ≤ ¼, which is what licenses η ≤ c_N|u|
inside c_K and c_RB. It does not enter anything I derive except through those two coefficients.

### 2.2 Notation (SQ.md §15.0-§15.1, CONST_T §2.1, STAR_CONST §2.1; nothing new)

u := 𝒫, ε := ||u||_{ℓ²(B_R)}, k := R^{1−4/q}||𝒮||_{ℓ^q(B_R)}, w := (|u|² + k²)^{1/2}, W := w^{(β+1)/2}; at **β = 1**,
which is all of Stage 1, **W = w** and β⁴ = 1. |N_3^plaq| = 7⁴·6 = 14406, |N_1^plaq| = 3⁴·6 = 486,
|𝒩_S| = |L_rev| = 3. g := sup|∇ζ|. Hypotheses: **ε ≤ ε_*** and **kR² = R^{3−4/q}||𝒮||_{ℓ^q} ≤ ε_***.

### 2.3 What step (5) is, and why it is the last symbol

SQ.md l.1489-1494 (Stage 1, β = 1) does exactly two things:

1. it **absorbs the critical part** V_c of the potential — the curvature terms — into the left side of (★),
   which is possible only if ||V_c|| is small, and the inequality that expresses "small enough" **is the
   definition of ε_***: l.1491's "absorbed for ε ≤ ε_*";
2. it converts (★) at β = 1 into the **ℓ⁴ ← ℓ² gain** of l.1494,
   ||w||_{ℓ⁴(B_{3R/4})} ≤ C_{S1}·R^{−1}·||w||_{ℓ²}, whose **only** job downstream is to supply the factor R^{−1}
   that makes γ_c = R·||V_c||_{ℓ⁴} finite as R → ∞ (l.1496).

Both halves are mine to compute: **ε_* comes from (1), C_{S1} from (2), and A_cγ_c is built from both.**
Neither SQ.md nor CONST_T.md nor STAR_CONST.md computes either; CONST_T §4 SUPPLIES c_c = 50 and ε_* = 10⁻⁴ and
labels them as supplied, and STAR_CONST §8.4 item 2 names this as the remaining gap.

---

## 3. STEP (5) EXPANDED — **PROVEN** given (H1)-(H4)

### 3.1 The Stage-1 cut-off, and g — **CHOICE, priced**

Take ζ_1 = 1 on B_{3R/4}, supported in B_{R−4} (post-proof correction (1) confines every local operator to
B_{R−4}), of the ℓ^∞-linear shape of CONST_T §2.3, so that with gap **d_1 := R/4 − 4** one has
**g = |∇ζ_1| ≤ 4/d_1 whenever d_1 ≥ 12, i.e. whenever R ≥ 64.** For R ≥ 64,

  **g ≤ 4/(R/4 − 4) = 16/(R − 16) ≤ (64/3)/R,  hence  g² ≤ (4096/9)·R^{−2}.**   [PROVEN]

*Three remarks, all of them prices I am paying openly.*
- I use the outer ball **B_{R−4}**, not l.1494's B_{7R/8}: the ℓ² norm is available on all of B_R by hypothesis
  and l.1496 uses ||w||_{ℓ²(B_R)} anyway, so the wider gap is free and it is what buys d_1 ≥ 12 at R = 64.
- **R ≥ 64** is SQ.md l.1466's own written R_0. It re-raises CONST_T §3.2's optimised R_0 = 32 to 64. CONST_T
  §3.3 proves this branch contributes only the floor (R_0 − 1)² ≤ 3969, swamped by ≥ 9 decades, so the cost is
  **zero**. [PROVEN, by CONST_T §3.3]
- I inherit CONST_T §2.3's convention "*from here on ζ denotes ζ^{++}*", which identifies the cut-off appearing
  on the two sides of (★) and is slightly loose: making it airtight needs one further 6-enlargement, i.e.
  |N_3| → |N_6^plaq| = 13⁴·6 = 171366 in the **Lemma-T factors only** (not in M_3's or M_1's own supports,
  which are forced). §4.3 prices that at exactly **×1.857** on my final bound, which §5 absorbs for free.

### 3.2 The curvature group, and the inequality that DEFINES ε_* — **PROVEN**

Write **Φ := c_K·M_3u + c_RB·(M_1u)²** (so Φ = C_1·V_c in CONST_T's normalisation). SOB (a) with C_S = 3 gives
𝒳 := ||ζ_1w||²_{ℓ⁴} ≤ 9·Σ|∇(ζ_1w)|². Hölder (ℓ² × ℓ²) and Lemma T at s = 4 (||ζ̃w̃||²_{ℓ⁴} ≤ |N_3|^{1/2}𝒳):

  **9·Σ_pΦ·ζ̃²w̃² ≤ 9·|N_3|^{1/2}·||Φ||_{ℓ²(B_R)}·𝒳.**

This is absorbed into a fraction 1/(4m) of 𝒳, for a **margin parameter m ≥ 1**, exactly when

> **(ABS-c)  9·|N_3|^{1/2}·||Φ||_{ℓ²(B_R)} ≤ 1/(4m).**

With ||M_3u||_{ℓ²} ≤ |N_3|^{1/2}||u||_{ℓ²} ≤ |N_3|^{1/2}ε and ||(M_1u)²||_{ℓ²} = ||M_1u||²_{ℓ⁴} ≤ ||M_1u||²_{ℓ²}
≤ |N_1|ε² (lattice ℓ⁴ ≤ ℓ², SOB (c)), **(ABS-c) holds for every configuration with ε ≤ ε_* as soon as**

> **(ABS-ε)  9·|N_3|·c_K·ε_*  +  9·|N_3|^{1/2}·|N_1|·c_RB·ε_*²  ≤  1/(4m)**
> i.e. **1.29654·10⁵·c_K·ε_* + 5.25005·10⁵·c_RB·ε_*² ≤ 1/(4m).**

**(ABS-ε) is the definition of an admissible ε_*** — it is l.1491's "absorbed for ε ≤ ε_*" written out. At
m = 1 it is Stage 1 exactly as SQ.md writes it; m > 1 is a *strengthening* of the hypothesis, which is always
available because ε_* is existentially quantified in EPS-T. **[PROVEN]**

**Two consequences to record before going on.**
- **CONST_T's SUPPLIED ε_* = 10⁻⁴ is not admissible at all.** (ABS-ε) at m = 1 gives
  ε_* ≤ 1/(36·|N_3|·c_K) = **1.9282·10⁻⁶/c_K**, which is ≤ 2.82·10⁻⁸ even at the most favourable admissible
  c_K = 17.51·3.9·1 = 68.29, and ≤ 2.87·10⁻¹² at c_K = 17.51·1.92·10⁴·2 = 6.724·10⁵. So ε_* = 10⁻⁴ overshoots
  Stage 1's own absorption by a factor between **3.5·10³ and 3.5·10⁷**. The reference value
  A_cγ_c = 236.9·C_1 = 4.7·10³ was therefore never a value this proof could take. **[PROVEN from (ABS-ε)]**
- My pre-stated **Y4 is confirmed**: at CONST_T's ε_* = 10⁻⁴ but with STAR_CONST's *computed* C_1 = 5699.63 in
  place of CONST_T's SUPPLIED C_1 = 20, the same formula A_cγ_c = 236.9·C_1 reads **1.348·10⁶**, not 4.7·10³ —
  **287× larger**, and 397× over the 3.4·10³ target. The brief's "ε_* must drop by a factor of 2-10" is an
  artefact of reading CONST_T's SUPPLIED C_1 together with STAR_CONST's §8.3 condition. **The true drop is
  2.4·10⁴ to 6.8·10¹¹** (§5).

### 3.3 The source group, and an exact cancellation at the sharpened counts — **PROVEN**

With V_s = |𝒮|²_L/k², Hölder at exponents q/2 and q/(q−2) (l.1492), Lemma T at s = 2q/(q−2), and interpolation
of ℓ^{2q/(q−2)} between ℓ² and ℓ⁴ (ϑ = 4/q):

  ||V_s||_{ℓ^{q/2}} = || |𝒮|_L ||²_{ℓ^q}/k² ≤ |L_rev|^{2/q}·||𝒮||²_{ℓ^q}/k² = **3^{2/q}·R^{−2+8/q}**,
  ||ζ̂ŵ||²_{ℓ^{2q/(q−2)}} ≤ |𝒩_S|^{(q−2)/q}·||ζ_1w||²_{ℓ^{2q/(q−2)}} = **3^{(q−2)/q}**·𝒴^{1−ϑ}𝒳^{ϑ},  𝒴 := ||ζ_1w||²_{ℓ²}.

**The two 3-powers multiply to exactly 3, for every q:** 3^{2/q}·3^{(q−2)/q} = 3^{2/q + 1 − 2/q} = 3. This is
CONST_T §2.5's "exact cancellation" (A_sγ_s is q-free) appearing in Stage 1, now at the sharpened counts.
Hence, with P := 27·c_s·R^{−2+8/q},

  9·c_s·Σ_pV_sζ̂²ŵ² ≤ P·𝒴^{1−ϑ}𝒳^{ϑ}.

Young at λ := 1/(4ϑ) (so that the absorbed share is ¼𝒳):

  **9·c_s·Σ_pV_sζ̂²ŵ² ≤ ¼𝒳 + c_ϑ·(27c_s)^a·R^{−2}·𝒴,  c_ϑ := (1 − ϑ)(4ϑ)^{ϑ/(1−ϑ)},  a := 1/(1 − ϑ) = q/(q−4),**

using **(−2 + 8/q)·q/(q−4) = −2 identically** — the same exact scale-invariance CONST_T §2.4(f) proves, verified
here as an exact rational at every q of the grid (ES1-2 **PASS**). At q = 12: ϑ = 1/3, a = 3/2,
c_ϑ = (2/3)(4/3)^{1/2} = 0.76980036 ≤ 1. **[PROVEN]**
*(Price of λ = 1/(4ϑ) rather than CONST_T's λ = 1/(2ϑ): a factor 2^{ϑ/(1−ϑ)} = √2 at q = 12 in c_ϑ. I pay it to
leave the fraction 1/(4m) free for the curvature absorption. CHOICE.)*

### 3.4 Assembly: Stage 1's constant C_{S1} — **PROVEN**

Adding §3.2, §3.3 and the cut-off term 9·c_g·g²·Σ_{supp⁺}w² ≤ **4096·c_g·R^{−2}·Σ_R** (§3.1, and
9·4096/9 = 4096 exactly), with Σ_R := ||w||²_{ℓ²(B_R)} and 𝒴 ≤ Σ_R:

  𝒳 ≤ [¼ + 1/(4m)]·𝒳 + [c_ϑ(27c_s)^a + 4096·c_g]·R^{−2}·Σ_R,

> **(5′) [PROVEN]  ||w||_{ℓ⁴(B_{3R/4})} ≤ C_{S1}(q, m)·R^{−1}·||w||_{ℓ²(B_R)},**
> **C_{S1}(q, m) := { [1 − ¼ − 1/(4m)]^{−1}·[ c_ϑ·(27·c_s)^a + 4096·c_g ] }^{1/2}.**

This is l.1494 with its constant. **COMPUTED (exact), es1_out.txt Block B:** at q = 12,
c_ϑ(27c_s)^{3/2} = 9.0288·10⁵ and 4096c_g = 2.33457·10⁷, so the bracket is **2.4248613·10⁷** and

| m | 1 | 8 | 100 | 19615 | → ∞ |
|---|---|---|---|---|---|
| **C_{S1}(12, m)** | **6963.995** | 5808.373 | 5695.579 | 5686.127 | 5686.125 |

**C_{S1} is dominated 96 % by 4096·c_g — Stage 1's cut-off bookkeeping, not its potentials.** It is bounded
uniformly for every m ≥ 1 and is **non-increasing in m**: strengthening the absorption cannot degrade it.
**This is my pre-stated Y2, CONFIRMED, and it is what rules out a circularity.** [PROVEN: C_{S1} depends on
ε_* only through the requirement (ABS-ε), monotonically in the helpful direction.]

### 3.5 A_c and γ_c, explicitly — **PROVEN**

By (H3), σ_c = 4 (Stage 1 delivers V_c in ℓ⁴), so ϑ_c = ½, **a_c = 2** and σ′_c = 4/3:

> **A_c = 36·C_1·|N_3^plaq|^{1/σ′_c} = 36·C_1·|N_3|^{3/4} = 36·C_1·1314.21 = 4.7312·10⁴·C_1**
> **γ_c = R^{2−4/σ_c}·||V_c||_{ℓ⁴(B_{3R/4−3})} = R·||V_c||_{ℓ⁴},  C_1·V_c = Φ = c_K·M_3u + c_RB·(M_1u)²,**

so that the product — the only combination that enters C_T — is

> **A_cγ_c = 36·|N_3|^{3/4}·R·||Φ||_{ℓ⁴(B_{3R/4−3})}.**

Now bound ||Φ||_{ℓ⁴} by (5′). With ||M_3u||_{ℓ⁴} ≤ |N_3|^{1/4}||w||_{ℓ⁴}, and
||(M_1u)²||_{ℓ⁴} = ||M_1u||²_{ℓ⁸} ≤ ||M_1u||_∞·||M_1u||_{ℓ⁴} ≤ ε·|N_1|^{1/4}||w||_{ℓ⁴} (SOB (c) gives
||M_1u||_∞ ≤ ||u||_∞ ≤ ε), and **||w||_{ℓ²(B_R)} ≤ ε + √6·kR² ≤ (1 + √6)·ε_* = 3.44949·ε_*** (l.1495 and the two
hypotheses; this is sharper than l.1495's 4):

> **(A_cγ_c) [PROVEN]  A_cγ_c ≤ 36·(1 + √6)·C_{S1}(q, m)·[ c_K·|N_3|·ε_* + c_RB·|N_3|^{3/4}|N_1|^{1/4}·ε_*² ]**
> **= 124.1816·C_{S1}·[ 14406·c_K·ε_* + 6171.3·c_RB·ε_*² ],**

using |N_3|^{3/4}·|N_3|^{1/4} = |N_3| = 14406 exactly. **A_cγ_c is linear in ε_* to leading order with an ε_*²
correction — my pre-stated Y1, CONFIRMED** (verified numerically over six decades of ε_*, ES1-6 **PASS**).

### 3.6 Every constant in step (5): FORCED or CHOICE

| constant | value | status |
|---|---|---|
| C_S = 3 ⟹ the factor 9 | 9 | **FORCED** (SOB (a), l.1453) |
| Hölder exponents on V_c at β = 1 | ℓ² × ℓ² | **FORCED** (l.1490 writes ||V_c||_{ℓ²}; σ_c = 2 is critical at β = 1) |
| Lemma-T factor on the curvature group | \|N_3\|^{1/2} | **FORCED** given CONST_T Lemma T (see §3.1's third remark and §4.3) |
| M_3's and M_1's own supports | \|N_3\|^{1/2}, \|N_1\| in ℓ²; \|N_3\|^{1/4}, \|N_1\|^{1/4} in ℓ⁴ | **FORCED** (l.1397's definition of M_r) |
| source Hölder / interpolation / Young exponents | σ = q/2, ϑ = 4/q, a = q/(q−4) | **FORCED** (l.1492; q > 4) |
| the source multiplicity product | exactly **3**, every q | **FORCED** given (H2) (§3.3's cancellation) |
| ‖w‖_{ℓ²(B_R)} bound | (1 + √6)ε_* | **FORCED** (l.1495 + both hypotheses) |
| the cut-off coefficient | 4096·c_g | **FORCED given §3.1's radii** |
| Stage-1 radii, d_1 = R/4 − 4 ≥ 12, R ≥ 64 | — | **CHOICE** (priced at 0: CONST_T §3.3) |
| the absorption split ¼ (source) + 1/(4m) (curvature) | m ≥ 1 | **CHOICE** — *this is the lever* |
| λ = 1/(4ϑ) in the source Young step | — | **CHOICE**, priced at √2 in c_ϑ at q = 12 |
| q | 12 | **CHOICE** (CONST_T §4.2's lever; I report a grid) |
| CONST_T §2.3's ζ ≡ ζ^{++} convention | — | **INHERITED**, disclosed, priced at ×1.857 (§4.3) |
| c_K, c_RB (hence C_K′, C_B, c_N) | SUPPLIED | **not pinned here, and §4 shows they do not need to be** |

---

## 4. THE RESULT: A_cγ_c is bounded UNIFORMLY in C_K′, C_B, c_N and ε_* — **PROVEN**

### 4.1 The theorem

The two inequalities of §3 are the *same* two quantities, and dividing one by the other eliminates every
SUPPLIED constant. Put 𝔞 := 9|N_3|c_Kε_* and 𝔟 := 9|N_3|^{1/2}|N_1|c_RBε_*², so that **(ABS-ε) reads
𝔞 + 𝔟 ≤ 1/(4m)**. Then in (A_cγ_c):

  c_K·|N_3|·ε_* = **𝔞/9**,  c_RB·|N_3|^{3/4}|N_1|^{1/4}·ε_*² = 𝔟·|N_3|^{1/4}/(9|N_1|^{3/4}) = **0.0117654·𝔟 ≤ 𝔟/9**

(because |N_3|^{1/4}/|N_1|^{3/4} = 10.9608/103.513 = 0.105889 < 1). Hence

> ### **Theorem ES-1 [PROVEN, given (H1)-(H4)].**
> **A_cγ_c ≤ 36·(1 + √6)·C_{S1}(q, m)·(𝔞 + 𝔟)/9 ≤ 4(1 + √6)·C_{S1}(q, m)·(𝔞 + 𝔟) ≤ (1 + √6)·C_{S1}(q, m)/m.**
>
> **Explicitly: for every ε_* satisfying Stage 1's own absorption inequality (ABS-ε) at margin m,**
> **A_cγ_c ≤ (1 + √6)·C_{S1}(q, m)/m, a bound containing NO c_K, c_RB, C_K′, C_B, c_N or ε_*.**

*Proof.* §3.2 (ABS-ε), §3.4 (5′), §3.5 (A_cγ_c), and the two displayed identities. ∎

The point is structural and worth saying in one line: **A_cγ_c and Stage 1's absorption condition are built
from the same norm of the same function Φ** — the first in ℓ⁴ with an R, the second in ℓ² — and Stage 1's own
ℓ⁴ ← ℓ² gain is what converts one into the other. So *every* curvature constant that makes the absorption
harder makes A_cγ_c larger by exactly the same factor, and the ratio is pinned. STAR_CONST §6.3 conjectured
this ("raising c_K or c_RB forces ε_* down and leaves A_cγ_c unchanged") and labelled it **ARGUED**; it is now
**PROVEN**, in the stronger form that the bound is uniform and m is a free lever.

### 4.2 The numbers, and the margin needed — **COMPUTED (exact), es1_out.txt Block C**

At q = 12:

| m | 1 | 2 | 4 | 6 | **7** | 8 | 10 | 100 | 10⁴ | **19615** | 25000 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **A_cγ_c ≤** | **2.402·10⁴** | 1.074·10⁴ | 5.122·10³ | 3.364·10³ | **2.871·10³** | 2.504·10³ | 1.995·10³ | 1.965·10² | 1.961 | **0.99996** | 0.785 |

- **At m = 1 — Stage 1 exactly as SQ.md writes it — A_cγ_c ≤ 2.40·10⁴**, which overshoots STAR_CONST §8.3's
  condition by **7.17×**. That is the honest statement of where the written proof stands. **[PROVEN]**
- **m = 7 is the smallest integer margin meeting STAR_CONST §8.3's condition** (A_cγ_c ≤ 2.871·10³ ≤ 3.35·10³ at
  q = 12 and ≤ 3.4·10³). **ES1-3 PASS.**
- **m = 19615 is the smallest integer margin giving A_cγ_c ≤ 1**, the reading STAR_CONST §6.3 assumed when it
  quoted C_T ≤ 5.3·10¹² at q = 12. **ES1-3b PASS.** §5-§6 show m = 19615 is as free as m = 7, so **this is the
  margin I recommend and the one §7 reports.**

**The uniformity was tested, not assumed:** es1_out.txt Block D re-evaluates C_T at all four corners of
C_K′ ∈ {3.9, 1.92·10⁴} × c_N ∈ {1, 2} and at C_B ∈ {3.6, 10², 10⁴}, and prints **the identical value**
5.288348·10¹² every time. Only ε_*'s *value* moves (Block E).

### 4.3 The one looseness I inherit, priced

If CONST_T §2.3's ζ ≡ ζ^{++} convention is made airtight by one further 6-enlargement, the **Lemma-T** factors
(and only those — M_3's and M_1's own supports are forced) become |N_6^plaq| = 13⁴·6 = 171366. Theorem ES-1's
constant is then multiplied by exactly

  4·(|N_6|/|N_3|)^{1/4} / 4 = (171366/14406)^{1/4} = **1.8571**,

because the ratio in §4.1 is 36|N_T|^{3/4}|N_3|^{1/4}/(9|N_T|^{1/2}|N_3|^{1/2}) = 4(|N_T|/|N_3|)^{1/4}. **A margin
m → 1.8571·m absorbs it exactly**, at a cost of 0.27 decades in ε_* out of the ≈ 21-25 decades §6 finds free.
**Not decisive, and disclosed.** [The same factor applies to CONST_T §2.5's A_c, which is why it cancels.]

---

## 5. The ε_* that does it, and the factor it drops by

### 5.1 The value

(ABS-ε) is a quadratic in ε_*; its positive root is the largest admissible threshold at margin m. **COMPUTED
(exact), es1_out.txt Block E**, at c_RB = 3.0·10⁶ (STAR_CONST's reference, (c_N, C_B) = (1, 3.6)):

| C_K′ | c_N | c_K = 17.51·C_K′·c_N | **ε_*(m = 7)** | **ε_*(m = 19615)** | drop vs CONST_T's SUPPLIED 10⁻⁴ |
|---|---|---|---|---|---|
| 3.9 (measured, q5 W3) | 1 | 6.829·10¹ | 4.031·10⁻⁹ | **1.440·10⁻¹²** | 2.5·10⁴ → **6.9·10⁷** |
| 3.9 | 2 | 1.366·10² | 2.017·10⁻⁹ | 7.198·10⁻¹³ | 5.0·10⁴ → 1.4·10⁸ |
| 1.92·10⁴ (WB's written bound) | 1 | 3.362·10⁵ | 8.194·10⁻¹³ | 2.924·10⁻¹⁶ | 1.2·10⁸ → 3.4·10¹¹ |
| 1.92·10⁴ | 2 | 6.724·10⁵ | 4.097·10⁻¹³ | **1.462·10⁻¹⁶** | 2.4·10⁸ → **6.8·10¹¹** |

The linear coefficient is **A_cγ_c ≈ 1.017·10¹⁰·c_K·ε_*** at m = 19615, so ε_* ≈ 9.83·10⁻¹¹/(m·c_K/19615) — i.e.
ε_* ∝ 1/(m·c_K), nothing else. C_B moves ε_* only through the quadratic clause, and not at all until
C_B ≳ 10⁴ (Block E's C_B sweep: ε_* unchanged to four digits at C_B = 10⁴).

### 5.2 **The factor ε_* must drop is 2.4·10⁴ to 6.8·10¹¹, not 2-10**

My brief, following STAR_CONST §8.3, says "ε_* must be lowered by about a factor 2-10 below CONST_T's 10⁻⁴".
**That is wrong by between four and eleven decades, and the reason is bookkeeping, not mathematics:**

1. STAR_CONST §8.3 quoted CONST_T's SUPPLIED reference A_cγ_c = 236.9·C_1 **at CONST_T's SUPPLIED C_1 = 20**,
   while in the same file computing **C_1 = 5699.63**. At its own C_1 the same expression is **1.348·10⁶**, so
   the overshoot is 397×, not 1.4×. (§3.2; pre-stated as **Y4** before I computed it.)
2. CONST_T's ε_* = 10⁻⁴ is not an admissible threshold for step (5) **at any** c_K: (ABS-ε) caps it at
   1.93·10⁻⁶/c_K ≤ 2.82·10⁻⁸ (§3.2). So there was no 10⁻⁴ baseline to drop from.

**Both corrections point the same way, and neither changes a conclusion**, because §6 shows the ε_* headroom is
≈ 21-25 decades and the drop needed is ≤ 11.8 of them.

---

## 6. THE AUDIT: is lowering ε_* free? — the important half

### 6.1 First finding: there are **four** distinct symbols called ε_* in this lane

I grepped every lane file for the string ε_* and read each occurrence with its defining formula. They are not
one constant:

| # | symbol | definition | where it lives |
|---|---|---|---|
| **1** | **EPS-T's ε_*(N, q)** — **mine** | the ε-regularity threshold on ‖𝒫‖_{ℓ²(B_R)} and R^{3−4/q}‖𝒮‖_{ℓ^q}; its *value* is fixed by (ABS-ε) | **SQ.md §15.1-§15.4 only** (l.1170-1172, 1318-1319, 1377, 1460-1462, 1491, 1495-1496, 1512, 1517-1518, 1622, 1667), plus REVIEW_SQ_S3, REVIEW_SQ_S4, LOG.md and the three session-24 files that discuss it (CONST_T, STAR_CONST, this one) |
| 2 | **N5-sf0's ε_*** | **ε_* := α_*/(10p_L(4R_* + 5)L) = 2.476·10⁻¹³/C_Δ** (PROOF.md l.5494, l.5544) | PROOF.md, SF.md, RLARGE.md l.69-76, NORMS.md l.748, PLD.md l.1022/1131, RTARGET.md l.891, BFT_B.md l.885, REVIEW_SF_S5-S7, REVIEW_S18_S19, REVIEW_S20, REVIEW_PLD_S3, REVIEW_RLARGE_V2, REVIEW_BFT_B_S2/S6 |
| 3 | **BG-b's ε_*** | **ε_* := (ε_1²/(4NB))^{1/2}**, "ε_* is g-independent" (PROOF.md l.1759); the M_2 ≤ ε_* of (b1) | PROOF.md l.331/1759-1775/2173/2296, LINEAR_PACKAGE.md l.182, REVIEW_S9_S10, REVIEW_S11_S12, REVIEW_S16_S17 |
| 4 | BFT_B's local ε_* | **ε_* := max_t ε_f(U_t, X)** (BFT_B.md l.2719) | BFT_B.md §19-§23 |

**My brief's comparator "PROOF's ε_* = 2.476·10⁻¹³/C_Δ (PROOF [SF7-edit])" is symbol 2, not symbol 1.** It is
not a constraint on my ε_* at all, and the near-coincidence between it and the value §5 produces (10⁻¹²-10⁻¹⁶)
is a coincidence of two unrelated thresholds. I state this because the coincidence is exactly the kind of thing
that would be read as a clash. **[PROVEN by inspection; the defining formulas are quoted above.]**

### 6.2 Second finding: EPS-T's ε_* reaches the rest of the project through exactly **one** channel

Within SQ.md, ε_* is used in five places, and only one of them propagates:

| use | line | direction |
|---|---|---|
| EPS-T's two hypotheses ‖𝒫‖_{ℓ²} ≤ ε_*, R^{3−4/q}‖𝒮‖_{ℓ^q} ≤ ε_* | 1460-1462 | **lowering ε_* STRENGTHENS the theorem** (smaller hypothesis set, same conclusion) |
| Stage 1's absorption "absorbed for ε ≤ ε_*" | 1491 | **lowering ε_* HELPS** — it is (ABS-ε), and a smaller ε_* makes it easier |
| Stage 2's ‖w‖_{ℓ²} ≤ 4ε_* and R‖V_c‖_{ℓ⁴} ≤ C′ε_* | 1495-1496 | **lowering ε_* HELPS** — this is precisely §3.5, A_cγ_c ∝ ε_* |
| EPS-0a's hypotheses ε_*²/16, ε_*/16 | 1512, 1517 | **the only propagating use**: it defines **θ_ε** |
| GAP/LU-ex's ε_G, ε_U ≤ ε_* | 1667, and REVIEW_SQ_S4 l.501 | lowering ε_* lowers ε_U, ε_G — **but route (α) is dead**: REVIEW_SQ_S4 **S4-20** verified that route β (§15.1-§15.3) cites GS, LU-ap, GAP or LU-ex **nowhere**, SQ.md's own route-(α) verdict says "not needed for (EPS-0)", and REVIEW_SQ_S4's fix (b) records that ε_U "is not explicit" anyway. **No numerical consumer.** |

The single propagating channel is, verbatim from SQ.md l.1622:

> θ_0 := min{θ_G, θ_ε}, **θ_ε the largest θ with 4·2.47N√κ_+θ ≤ ε_* and 16·32^{1/8}C_0θ ≤ ε_***

i.e. **θ_ε = ε_*/max{4·2.47N√κ_+, 16·32^{1/8}C_0} = ε_*/84** at the file's reference point (N = 2, κ_+ = 1,
C_0 = 3.34: the two clauses give 19.8 and 82.4), which is REVIEW_SQ_S4 S4-16's "θ_ε ≈ ε_*/84". **θ_ε is exactly
linear in ε_***, and the whole audit reduces to: how far can θ_ε fall?

**My pre-stated Y3 is CONFIRMED in mechanism and REFUTED in size.** The binding direction *is* the
hypothesis-verification direction, as I predicted, and it runs entirely through θ_ε. But I predicted the usable
headroom would be "about 8-10 decades, not 30", on the guess that θ_G ≈ 1.46·10⁻¹³ would be the comparator.
It is not: §6.4 shows the comparator is 1.33·10⁻³⁹, and the headroom is **≈ 21-25 decades**.

### 6.3 The chain, link by link, with the direction of each

θ_ε → θ_0^{SQ4} → τ_R → τ_♭ → {t_pr, η_♭} → RLARGE's a_bad, HIST A5. Each link, with its definition:

| link | definition | effect of lowering ε_* |
|---|---|---|
| θ_ε | = ε_*/84 (l.1622) | falls **∝ ε_*** |
| θ_0^{SQ4} | = min{θ_G, θ_ε} (l.1622), θ_G ≤ 1.46·10⁻¹³ (S4-14) | **unchanged while ε_* ≥ 84·θ_G = 1.23·10⁻¹¹**; then ∝ ε_* |
| τ_R | = min{τ_0, τ_*, τ_S, θ_S/C′, θ_0^{SQ4}/C′} (l.1633); S4-14 says θ_0^{SQ4}/C′ binds, giving 2.75·10⁻¹⁵ | falls ∝ θ_0^{SQ4} |
| τ_♭ | = min{τ_F, **τ_R**, **θ_0^{SUP}/C′**, ε_M/(C_DC′), θ_♯/C′, 1/(73.6Nc′²A′²)} (l.319) | **the binding entry is θ_0^{SUP}/C′, not τ_R** — see §6.4 |
| t_pr | = C′τ_♭ (S4-15) | unchanged while τ_R is not the binding entry of τ_♭ |
| η_♭ | = c_♭τ_♭²/C′² (l.319) | unchanged, same reason; **∝ ε_*² once θ_ε binds** |
| EPS-0's own hypothesis θ ≤ θ_0 | FORCE at l.1633-1634: a τ_R-small minimiser has θ < C′τ_R ≤ θ_0 | **automatic by construction** — τ_R is *defined* with θ_0/C′ in its min, so the hypothesis is never an extra assumption (REVIEW_SQ_S4 S4-15 verified exactly this) |
| (CLS-min)'s form | DESC (a) covers ‖1 − V_P‖ ≥ C′τ, DESC (b) covers < C′τ (S4-15) | **covers every top V at every θ_0**; only the *price* c_♭τ_♭² moves, and it moves with τ_♭, not with ε_* |

So **no statement in the chain needs ε_* to be large in order to COVER something**: the one covering-type
hypothesis, θ ≤ θ_0 in Theorem EPS-0, is discharged by FORCE from the same τ_R that θ_0 defines. The cost of a
smaller ε_* is entirely the smaller *price* at the end of the chain.

### 6.4 The no-change floor: **ε_* ≥ 1.12·10⁻³⁷**, and ≈ 21-25 decades of genuine headroom

τ_♭'s binding entry is the decisive point, and it is **not** the one REVIEW_SQ_S4 S4-14 names.
θ_0^{SUP} := 1/(2C_err) with C_err = 1.655·10⁷·C_D² (S4-16) and **C_D ≈ (0.5-0.9)·10³·C_T** (S4-16). At the
C_T this file delivers (5.288·10¹², §7):

  C_D = 4.76·10¹⁵ (worst end) ⟹ **θ_0^{SUP} = 1.334·10⁻³⁹**, τ_♭ = θ_0^{SUP}/53 = 2.52·10⁻⁴¹,
  **t_pr = θ_0^{SUP} = 1.334·10⁻³⁹**, and ε_1 = 6.7·10⁻⁴⁰ < t_pr with a margin of only **×1.99**.

τ_R = 2.75·10⁻¹⁵ is twenty-four decades *larger* than θ_0^{SUP}/C′ = 2.52·10⁻⁴¹, so **θ_0^{SUP}/C′ binds τ_♭
and τ_R does not.** Therefore:

> ### **The no-change floor [PROVEN given S4-16's C_err model].**
> **For every ε_* ≥ 84·θ_0^{SUP} = 1.12·10⁻³⁷ (3.6·10⁻³⁷ at the other end of C_D), θ_ε ≥ θ_0^{SUP}, so τ_♭,
> t_pr, η_♭, a_bad and every downstream constant are EXACTLY what they would be at ε_* = 10⁻⁴. Lowering ε_*
> to anywhere above that floor is free in the strict sense: it changes nothing at all.**

Against the ε_* that §5 needs, this is **ES1-5b PASS** at all four corners of C_K′ × c_N:

| C_K′, c_N | ε_*(m = 19615) | decades above the no-change floor |
|---|---|---|
| 3.9, 1 | 1.440·10⁻¹² | **25.1** |
| 3.9, 2 | 7.198·10⁻¹³ | 24.8 |
| 1.92·10⁴, 1 | 2.924·10⁻¹⁶ | 21.4 |
| **1.92·10⁴, 2** (worst) | **1.462·10⁻¹⁶** | **21.1** |

And against REVIEW_SQ_S4 S4-16's own published floor 5.6·10⁻³⁸ (which is the weaker requirement t_pr > ε_1 taken
through θ_ε directly): **ES1-5 PASS**, by 21.6-25.4 decades. **Answer to the brief's question: lowering ε_* is
free, with 21 decades to spare at the crudest admissible C_K′ and 25 at the measured one. No consumer needs
ε_* above the value I need.** [The ≈ 30 decades of REVIEW_SQ_S4 S4-16 is right in order and 5-9 decades
optimistic, because it compared θ_ε with ε_1 rather than with the actually-binding θ_0^{SUP}.]

### 6.5 Below the floor (not needed, recorded for completeness)

If ε_* were pushed below 1.12·10⁻³⁷, θ_ε would take over as τ_♭'s binding entry and then
t_pr = ε_*/84, η_♭ = t_pr²/5.05·10⁹. The first failure would be the **η_♭ clause** (§6.6), at
ε_* ≈ 84·3.01·10⁻³⁵√C_3 = 2.5·10⁻³³√C_3, not the ε_1 < t_pr clause at 5.6·10⁻³⁸. **Neither is in play.**

### 6.6 A side-finding that is NOT about ε_*, and is worth more than my main result

While checking the η_♭ direction I found an inconsistency *inside* the chain that lowering ε_* does not cause
and cannot cure. I report it because it is load-bearing and because it is exactly the class of thing this lane
keeps finding. **Status: ARGUED** — I did not re-derive C_err's model, C_3, ε_1, or HIST A5's energy bound; I
read them.

1. **HIST Theorem A5 (A)** feeds energy **E ≤ 4C_3ε_1²** into AE-red's size clause (REVIEW_HIST_S4 l.281: "δ =
   2ε_1 gives E ≤ 4C_3ε_1² ≤ η_AE"), and the clause needs **ε_1 ≤ ½√(η_AE/C_3)** (REVIEW_HIST_S4 strategic 4,
   l.498). SQ.md §0.3/§0.5 replaces AE-red by **Corollary DESC-ε**, whose threshold is η_♭ = c_♭τ_♭²/C′² — SQ.md
   l.223 states the substituted clause explicitly: "η_♭ ≈ 10⁻²⁶ gives ε_1 ≲ 5·10⁻¹⁴/√C_3".
2. **REVIEW_SQ_S4 uses two different binding entries of τ_♭ in two different items.** S4-16 takes
   t_pr = C′τ_♭ ≤ θ_0^{SUP} = 1/(3.31·10⁷C_D²) — correct at large C_D. S4-14 item 2 computes
   **η_♭ ≈ 4.2·10⁻³⁶ from τ_♭ = τ_R = 2.75·10⁻¹⁵** — which requires τ_R ≤ θ_0^{SUP}/C′, i.e. **C_D ≤ 4.55·10²**.
   At the C_D that EPS-T actually produces (≈ 5·10¹⁵), **η_♭ = c_♭t_pr²/C′⁴ = t_pr²/5.05·10⁹ = 3.5·10⁻⁸⁸**, not
   4.2·10⁻³⁶. The two items are mutually inconsistent by **52 decades** in η_♭.
3. **The consequence.** The DESC-ε substitution needs η_♭ ≥ 4C_3ε_1² = 1.80·10⁻⁷⁸·C_3; it delivers 3.5·10⁻⁸⁸.
   **Shortfall ≈ 9.7 decades in energy (4.85 in ε_1), at C_3 = 1.** Holding it would need
   t_pr ≥ 3.01·10⁻³⁵√C_3, i.e. **C_D ≤ 3.17·10¹³/C_3^{1/4}, i.e. C_T ≲ 3.5·10¹⁰ - 6.3·10¹⁰** — **2.2 to 2.5
   decades below REVIEW_SQ_S4 S4-16's recorded ceiling C_T ≲ 10¹³.**
4. **What it does and does not break.** It does **not** touch RLARGE's a_bad = c_prε_1² branch, which needs only
   the linear ε_1 < t_pr and holds (margin ×1.99). It does **not** break HIST A5 via **AE-red itself**, whose own
   threshold η_AE = 1.78·10⁻¹⁵ (REVIEW_HIST_S4 l.368) covers 4C_3ε_1² with ~63 decades to spare. **What it
   breaks is the replacement**: at the new C_D, DESC-ε cannot discharge AE-red's size clause for A5, so the
   (MS-Sob) hypothesis that DESC-ε was introduced to remove comes back for that consumer.
5. **This is a question for SQ.md's, HIST's and RLARGE's owners, not for me**, and it is in §9. It is also the
   sharpest form yet of lead decision D3: the quantity that broke is a threshold that is **quadratic** in the
   same t_pr whose **linear** clause S4-16 checked and passed.

---

## 7. C_T, with its status

### 7.1 The numbers — **COMPUTED (exact), es1_out.txt Block D**

M-sharp (|𝒩_S| = 3, (H2)), **P-max (B(8) = 1931.48, STAR_CONST §6.4's correction, NOT CONST_T's B(4a))**,
F = 175.8, R_0 = 64, A_sγ_s = 36·c_s·3 = 4.44876·10⁴:

| q | a = q/(q−4) | **C_T at m = 19615 (A_cγ_c ≤ 1)** | C_T at m = 7 (A_cγ_c ≤ 2.87·10³) | vs 10¹³ |
|---|---|---|---|---|
| 10 | 1.6667 | 2.463·10¹³ | 2.857·10¹³ | OVER |
| **11** | 1.5714 | **9.774·10¹²** | 1.333·10¹³ | **UNDER at m = 19615, over at m = 7** |
| **12** | **1.5000** | **5.288·10¹²** | **8.717·10¹²** | **UNDER both** |
| 16 | 1.3333 | 2.031·10¹² | 5.358·10¹² | UNDER |
| 24 | 1.2000 | 1.528·10¹² | 4.836·10¹² | UNDER |
| 32 | 1.1429 | 1.454·10¹² | 4.760·10¹² | UNDER |
| 100 | 1.0417 | 1.396·10¹² | 4.699·10¹² | UNDER (plateau) |

> ### **C_T(q = 12) = 5.288·10¹²,  q_min = 11.**

Two independent cross-checks of the harness, both clean: (i) B(4) = 43.9486 and B(8) = 1931.481 reproduce
CONST_T §3.1's 43.95 and 1931.5 to 3·10⁻⁵ and 1·10⁻⁵ (**ES1-1 PASS**); (ii) my q-row at A_cγ_c → 0 reproduces
**STAR_CONST §8.3's own numbers to three digits** — it reports C_T ≤ 9.8·10¹² at q = 11, 5.3·10¹² at q = 12 and a
plateau at 1.4·10¹² for q ≳ 30; I get 9.774·10¹², 5.288·10¹² and 1.454·10¹². The two files share no code.

Comparison readings, for the record (not the verdict): at q = 12, M-sharp/P-ct gives 7.98·10¹¹,
M-ct(486)/P-max gives 8.05·10¹⁵ and M-ct/P-ct gives 1.21·10¹⁵ — so **(H2) is worth 1523× at q = 12 and remains
the difference between a number and no number**, exactly as STAR_CONST §8.2 says. R_0 = 128 instead of 64
changes C_T by 0.2 % (5.276·10¹² — it only shrinks ‖V_s‖_∞ in Q).

### 7.2 Where the 5.29·10¹² sits — **[POST-HOC, ES1-P1]**

| term of Ĉ | value | share |
|---|---|---|
| ½(A_sγ_s)^a — **the source** | 4.6917·10⁶ | **73.8 %** |
| ½(A_cγ_c)² — **the curvature, i.e. my quantity** | **0.49996** | **0.00 %** |
| 288·C_1·Q — the cut-off | 1.6665·10⁶ | 26.2 % |

**A_cγ_c has been removed from the problem entirely.** The ceiling is now set by the source term and the
cut-off prefactor c_g = 5699.63, i.e. by steps (2) and (4) — STAR_CONST's territory, not step (5)'s.
*(This block was written after reading Block C/D and is labelled post-hoc in the script and the output.)*

### 7.3 Status, stated so a hostile reader can check it

- **PROVEN** (a complete proof written out above, from stated hypotheses): §3's expansion of step (5) —
  (ABS-ε), (5′) with C_{S1}, and A_c, γ_c explicitly; **Theorem ES-1**, A_cγ_c ≤ (1 + √6)C_{S1}(q, m)/m, uniform
  in C_K′, C_B, c_N and ε_*; the no-change floor ε_* ≥ 84·θ_0^{SUP} = 1.12·10⁻³⁷ (given S4-16's C_err model);
  the exact scale-invariance (−2 + 8/q)·q/(q−4) = −2 for every q > 4; the inadmissibility of ε_* = 10⁻⁴.
- **COMPUTED (exact)**: C_{S1}(12, m), the A_cγ_c table, m = 7 and m = 19615, ε_*'s four values, C_T's q-row,
  B(4), B(8). All in `fractions`/`Decimal`, identical at 40 and 60 digits (**ES1-7 PASS**).
- **CONDITIONAL**, and this is the honest headline: **C_T(q = 12) = 5.288·10¹² is CONDITIONAL on (H2)** — the two
  restatements of SQ.md §15.1 (three coefficients in V; the source term's 3-plaquette/3-link neighbourhoods).
  They are proved in STAR_CONST §2.2/§8.2 and are restatements, not new mathematics, but **SQ.md does not say
  them today**, and without them C_T = 8.05·10¹⁵ and there is no admissible q. It is also conditional on
  (H1)/(H3), i.e. on STAR_CONST.md's and CONST_T.md's own arithmetic — and **HANDOFF.md lists both as
  UNREVIEWED**, from this same session, in a project with sixteen historical reversals.
- **ARGUED**: §6.6's side-finding (the η_♭ clause and the two binding entries of τ_♭).
- **OPEN**: §8.3.
- **NOT CLAIMED**: I have not pinned C_K′ or C_B and I did not try; Theorem ES-1 is the statement that C_T does
  not need them. I have not re-derived (★), BIA, WB, SOB, C_err, C_3, ε_1, θ_G or F.

### 7.4 Does the (CLS-min) → RLARGE interface carry a number?

**Yes for RLARGE, with a thin margin; no for one other consumer, for a reason that is not ε_*.**

- **RLARGE's a_bad branch: YES.** C_T = 5.288·10¹² ⟹ C_D ≤ 4.76·10¹⁵ ≤ **6.7·10¹⁵** (REVIEW_SQ_S4 S4-16's
  condition), so t_pr = 1.334·10⁻³⁹ > ε_1 = 6.7·10⁻⁴⁰ and **a_bad = c_prε_1² holds**. The margin is **×1.41 in
  C_D and ×1.99 in t_pr vs ε_1** — met, but not comfortably. Status as in §7.3: a number, CONDITIONAL on (H2)
  and on the two unreviewed session-24 files.
- **HIST A5 (A)'s size clause via DESC-ε: NO**, by ≈ 9.7 decades of energy (§6.6). That clause needs
  C_T ≲ 3.5·10¹⁰, and it fails at every C_T this route can produce (the floor over all δ-budgets is
  c_s ≥ 319.2, giving C_T ≥ 4.4·10¹² at q = 12). **This is not caused by lowering ε_* and lowering ε_* cannot
  fix it.** It is a consequence of C_D being an *output* of EPS-T rather than an O(1) parameter.
- **What is NOT conditional on anything SUPPLIED:** the number 5.288·10¹² is the same for every
  C_K′ ∈ [3.9, 1.92·10⁴], every c_N ∈ [1, 2] and every C_B — tested at all corners (§4.2). **That is the part of
  STAR_CONST §8.4 item 1 ("harmless for C_T") that is now PROVEN rather than ARGUED.**

---

## 8. Checks — nine pre-registered verdicts, all PASS, and two disclosures

Criteria: `checks/es1_criteria.md`, written after EPSSTAR.md §1 and before `checks/es1_eps.py`. Script:
`checks/es1_eps.py` (one file; its single post-hoc block is labelled `[POST-HOC, ES1-P1]` in both source and
output). Outputs: `checks/es1_out.txt` (40 digits), `checks/es1_out_prec60.txt` (60 digits),
`checks/es1_time.txt`. Plain `python3 -I`, single thread, OMP/OPENBLAS/MKL = 1, nice 10, no numpy, no BLAS,
**no numeric lock taken** (exact `Fraction` + fixed-precision `Decimal` only; 1.91 s real, ~20 MB).

| id | verdict | result |
|---|---|---|
| **ES1-1** | B-harness reproduces CONST_T §3.1 | **PASS** — B(4) = 43.948619 (3.1·10⁻⁵), B(8) = 1931.4811 (9.8·10⁻⁶) |
| **ES1-2** | exact scale-invariance; C_{S1} finite | **PASS** — (−2 + 8/q)·q/(q−4) = −2 **exactly as a Fraction** at all eight q; C_{S1}(12, 1) = 6963.995 |
| **ES1-3** | A_cγ_c ≤ 3.4·10³ at some integer m ≤ 10³ | **PASS** — m = 7 gives 2.871·10³ |
| **ES1-3b** | A_cγ_c ≤ 1 at some integer m ≤ 10⁶ | **PASS** — m = 19615 gives 0.99996 |
| **ES1-4** | C_T(12, P-max) ≤ 10¹³ at m = 19615 | **PASS** — 5.288·10¹² |
| **ES1-4b** | same at m = 7 | **PASS** — 8.717·10¹² |
| **ES1-5** | ε_* > 5.6·10⁻³⁸ at both margins, both ends of C_K′ × c_N | **PASS** — worst 1.462·10⁻¹⁶ |
| **ES1-5b** | ε_* > 84·θ_0^{SUP} | **PASS** — by 21.1 to 25.1 decades |
| **ES1-6** | monotone in m, in q, in ε_* | **PASS** — all three; and the direct A_cγ_c(ε_*) equals the uniform bound at the root, as it must |
| **ES1-7** | 40 vs 60 digits | **PASS** — `diff es1_out.txt es1_out_prec60.txt` differs in exactly two lines, both of them the stated precision. Every value and every verdict identical |

**No check FAILED.** I record that plainly rather than manufacture one: the reason is that Theorem ES-1 was
derived before the script was written, and the script's only job was arithmetic, precision and monotonicity —
exactly what §1 of `es1_criteria.md` says. The one place my pre-registration could have failed, ES1-5/5b (the
audit floors), is the one I could not have predicted, and it is also where I had pre-stated the **wrong**
expectation (Y3, §9).

### 8.1 Disclosure 1 — a provenance inaccuracy in my own criteria header

`checks/es1_criteria.md` carries the header "Written **2026-10-28 14:14 UTC**". Its actual creation time is
**14:11:04 UTC**, as its mtime shows: I wrote the header forward-dated. The *order* it asserts is correct and
is what matters — EPSSTAR.md §1 (14:00:12 UTC) → es1_criteria.md (14:11:04) → es1_eps.py (14:12:50) →
es1_out.txt (14:12:56) → es1_out_prec60.txt (14:13:44) → everything in §2-§11 here — but the minute in that
header is wrong by three. **I have not edited the criteria file to fix it**, because editing a criteria file
after its script has run is the worse offence. Recording it here instead, as STAR_CONST §12 did.

### 8.2 Disclosure 2 — the criteria file names its own exception

`es1_criteria.md` §1 says in writing that "the formulas are inputs to the script, not outputs of it". That is
the correct description of this check and it is also its limitation: **the script cannot catch an error in
§3's derivation.** What it can and does catch is an arithmetic slip, a precision artefact, a monotonicity
violation and a uniformity violation, and it independently reproduces two numbers (B(m), and STAR_CONST §8.3's
q-row) that were computed elsewhere by other code. A reader who distrusts §3 should check §3, not the script.

### 8.3 What remains OPEN in step (5)

1. **Sharpness of C_{S1}.** 96 % of C_{S1}² is 4096·c_g — Stage 1's cut-off bookkeeping. The 4096 is
   9·(64/3)², i.e. SOB's 9 times my cut-off gradient; a β-adapted or sharper cut-off would reduce it, and c_g
   itself is STAR_CONST's. Since A_cγ_c now contributes 0.00 % of Ĉ, **this does not matter** and I did not
   pursue it. **OPEN, immaterial.**
2. **CONST_T §2.3's Lemma-T convention** (§3.1, §4.3): priced at ×1.857, absorbed by m. **OPEN, immaterial.**
3. **The factor 36 in A := 36·C_1·|N|^{1/σ′}.** Reading CONST_T §2.4(a)-(d) line by line I get 18, not 36
   (9 from SOB (a), ×2 from the ζ̃² ≤ 2ζ² split). CONST_T's 36 is therefore **conservative by 2×**, which at
   a_c = 2 is 4× in A_cγ_c and at a = 3/2 is 2.83× in the source term. **I did not change it** (my §1.4 says I
   substitute into CONST_T's formula), so every number here is up to 2.83× pessimistic. **OPEN; it is CONST_T's
   to confirm, and it can only improve C_T.**
4. **Whether a_c = 2 with a β⁴ coefficient is really forced** — STAR_CONST §8.4 item 3's P-max/P-ct question.
   I used P-max (the conservative one) throughout. P-ct would give C_T = 7.98·10¹¹ at q = 12. **OPEN, inherited.**
5. **The §6.6 side-finding.** Not mine to close. **OPEN, and it is now the live quantitative question on this
   chain.**

---

## 9. THE VERDICT, against §1.3's pre-registered table

> ### **PASS-UNIFORM**, with one condition inherited from my own scope and one new OPEN flagged separately.

Clause by clause against §1.3:

| requirement | met? |
|---|---|
| an explicit ε_* > 0, admissible for step (5) | **YES** — ε_* = the positive root of (ABS-ε) at m = 19615; **1.46·10⁻¹⁶ at the worst admissible C_K′·c_N, 1.44·10⁻¹² at the measured one** |
| **A_cγ_c ≤ 3.4·10³ PROVEN** from step (5) as expanded | **YES**, and far better: **A_cγ_c ≤ 1** (0.99996), by Theorem ES-1 |
| the audit finds no consumer needing ε_* above that | **YES** — the no-change floor is 1.12·10⁻³⁷, i.e. **21.1 decades below the value needed at the worst C_K′** and 25.1 at the measured one |
| C_T(q = 12, P-max) ≤ 10¹³ | **YES** — **5.288·10¹²**, and q_min = 11 |
| **PASS-UNIFORM's extra clause**: C_T's number independent of C_B, C_K′, c_N | **YES** — Theorem ES-1 contains none of them; tested at all four C_K′ × c_N corners and at C_B ∈ {3.6, 10², 10⁴}, identical to 7 digits |

**The one condition**, which is in my §1.4 because my brief put it there: everything is **CONDITIONAL on (H2)**,
STAR_CONST's two restatements of SQ.md §15.1. They are proved in STAR_CONST and are restatements rather than new
mathematics, but SQ.md does not state them today, and without them C_T = 8.05·10¹⁵ and no q works. Also
conditional on (H1)/(H3) — CONST_T.md and STAR_CONST.md, both **UNREVIEWED**.

**One new OPEN, raised separately from the table** (as §1.3's structure allows, and the analogue of
STAR_CONST's CONTRADICTS-CONST-T flag): **§6.6**. A second, stronger clause on the same (CLS-min) chain —
η_♭ ≥ 4C_3ε_1², i.e. HIST A5 (A)'s size clause taken through Corollary DESC-ε — fails by ≈ 9.7 decades at the
C_D that any C_T on this route produces, and would need C_T ≲ 3.5·10¹⁰. **It is not about ε_*, lowering ε_*
cannot fix it, and it is now the live quantitative question on this chain.** ARGUED.

### 9.1 My pre-stated expectations: three of four right, and the wrong one decided the task

| | pre-stated (§1.5) | outcome |
|---|---|---|
| **Y1** | A_cγ_c linear in ε_* with a subleading ε_*²; the drop factor = the overshoot factor | **CONFIRMED** (§3.5; verified over six decades, ES1-6). And the ε_*² term never binds until C_B ≳ 10⁴ |
| **Y2** | Stage 1's constant bounded uniformly below the threshold; no circularity | **CONFIRMED exactly** (§3.4): C_{S1}(q, m) is **non-increasing in m**, so strengthening the absorption can only help. This is what makes Theorem ES-1 non-circular |
| **Y3** | the binding direction is hypothesis-verification; usable headroom ≈ 8-10 decades, **not 30** | **CONFIRMED in mechanism, REFUTED in size — and this is what decided the task.** The channel is exactly θ_ε, as predicted, and the covering hypothesis is discharged by FORCE. But I guessed the comparator was θ_G = 1.46·10⁻¹³; it is **θ_0^{SUP} = 1.33·10⁻³⁹**, because C_D is now an output of EPS-T. Headroom **21-25 decades**. Had Y3 been right, A_cγ_c ≤ 1 would have cost real downstream price; it costs nothing |
| **Y4** | the honest A_cγ_c at ε_* = 10⁻⁴ is ≫ 4.7·10³ because CONST_T's C_1 = 20 was replaced by 5.70·10³; the drop is ≫ 2-10 | **CONFIRMED, and stronger than I registered**: the figure is **1.35·10⁶** (×287), the drop is **2.4·10⁴-6.8·10¹¹**, and ε_* = 10⁻⁴ is **not an admissible threshold for step (5) at all** (§3.2) |

The expectation I got wrong is the one that mattered, and the reason is the same one the lane keeps hitting:
**I compared against a constant someone fixed once (θ_G) instead of against the one the chain now actually
binds on (θ_0^{SUP}, which moved by 26 decades when C_D stopped being a parameter).** That is
HANDOFF.md's closing paragraph, one level further down.

---

## 10. FOR OTHER FILES (not edited)

I edited only this file and `checks/es1_*`. I did not touch SQ.md, CONST_T.md, STAR_CONST.md, NORMS.md, any
REVIEW_* file, or anything else. The following are requests.

### 10.1 For SQ.md's owner (§15.1 step (5), l.1489-1494; §15.3 l.1622)

1. **(the one that matters) l.1491: state the absorption inequality that defines ε_*.** It is
   **9·|N_3|^{1/2}·‖c_K·M_3u + c_RB·(M_1u)²‖_{ℓ²(B_R)} ≤ 1/(4m)**, i.e. (ABS-ε) of §3.2 here, and at m = 1 it
   caps ε_* at **1.93·10⁻⁶/c_K** — so **CONST_T's SUPPLIED ε_* = 10⁻⁴ is not admissible**, by 3.5·10³ to
   3.5·10⁷. Writing the inequality down is what turns ε_* from a symbol into a number, and it is also what
   makes **Theorem ES-1** available (A_cγ_c ≤ (1 + √6)C_{S1}/m, uniform in C_K′, C_B, c_N).
2. **l.1494: the constant is explicit.** ‖w‖_{ℓ⁴(B_{3R/4})} ≤ C_{S1}R^{−1}‖w‖_{ℓ²(B_R)} with
   **C_{S1}(q, m) = {[1 − ¼ − 1/(4m)]^{−1}[c_ϑ(27c_s)^a + 4096c_g]}^{1/2}**, = 5686-6964 at q = 12 (§3.4). The
   outer ball is better taken as **B_{R−4}** than l.1494's B_{7R/8}: the ℓ² norm is available there anyway and
   the wider gap is what gives d_1 ≥ 12 at R = 64.
3. **Record that Stage 1 is where ε_* is *defined*, not merely used.** l.1496's "R‖V_c‖_{ℓ⁴} ≤ C′ε_*" has
   C′ = 36·|N_3|^{3/4}·(1 + √6)·C_{S1}·|N_3|^{1/4}/… — §3.5 writes it out. The relation A_cγ_c ∝ ε_* and the
   relation (ABS-ε) are the **same** norm of the **same** function Φ, which is why their ratio is pinned.
4. **l.1489-1490's "C′(ε + ε²)" and "neighbour maxima cost a bounded factor" can be made numbers:**
   ‖M_3u‖_{ℓ²} ≤ |N_3|^{1/2}ε = 120.02·ε and ‖(M_1u)²‖_{ℓ²} ≤ |N_1|ε² = 486·ε² (§3.2).
5. **l.1622: θ_ε = ε_*/84 should be written as such** (the two clauses give 4·2.47N√κ_+ = 19.8 and
   16·32^{1/8}C_0 = 82.4 at the file's reference point), with the remark that **θ_ε is not the binding entry of
   τ_♭ for any ε_* ≥ 1.12·10⁻³⁷** — which is the precise form of REVIEW_SQ_S4 S4-16's "safe by ~30 orders"
   (§6.4), and is worth stating because it is what makes ε_* genuinely free.
6. **Rename one of the four ε_* (§6.1).** EPS-T's ε_* is a different constant from N5-sf0's
   ε_* = α_*/(10p_L(4R_*+5)L) = 2.476·10⁻¹³/C_Δ, from BG-b's ε_* = (ε_1²/(4NB))^{1/2} and from BFT_B l.2719's
   local ε_*. The numerical near-coincidence between symbol 1's new value (10⁻¹²-10⁻¹⁶) and symbol 2's
   2.476·10⁻¹³/C_Δ makes this **load-bearing, not cosmetic** — a reader will take it for a clash. Suggest
   **ε_T** for EPS-T's. (This is the same class of defect as REVIEW_SQ_S4 S4-14 item 4's θ_0 collision.)

### 10.2 For CONST_T.md's owner (not edited)

- **§4's SUPPLIED c_c = 50 and ε_* = 10⁻⁴ should be withdrawn, not merely re-valued.** ε_* = 10⁻⁴ violates
  step (5)'s own absorption inequality. The right entry is not a number but **Theorem ES-1**: with ε_* taken
  from (ABS-ε) at margin m, **A_cγ_c ≤ (1 + √6)·C_{S1}(q, m)/m**, so §6.1's ½(A_cγ_c)² term can be set to ½ at
  no cost and **A_cγ_c, c_c and ε_* drop out of §6.1 entirely.**
- **§2.4(d)'s A := 36·C_1·|N|^{1/σ′} appears to be 18·C_1·|N|^{1/σ′}**, and §2.4(d)'s own
  Z = 144·C_1·Q·β⁴·d_i^{−2}·Σ is consistent with 18, not 36: both come from the same two steps (SOB's 9, then
  ×2 from ζ̃² ≤ 2ζ² + 288/d²), and 9·16 = 144 fixes the normalisation. If 18 is right, **C_T improves by 2.83×
  at q = 12** (2^a) and by 2× as q → ∞. I did not use it — §1.4 says I substitute into CONST_T's formula — so
  every number in §7 is up to 2.83× pessimistic. **Please confirm or refute; it can only help.**
- **§5.3's caveat is now a theorem.** Its "if the added hypothesis is instead discharged by shrinking ε_*, then
  ε_* falls and the V_c term falls with it — the verdict only improves" is exactly Theorem ES-1, and the
  stronger statement holds: the V_c term can be driven to ½ **uniformly in C_B, C_K′ and c_N**.
- **§2.3's Lemma T convention** ("from here on ζ denotes ζ^{++}") identifies the cut-off on the two sides of
  (★) and is loose by one 6-enlargement; the airtight version replaces the **Lemma-T** multiplicities by
  |N_6^plaq| = 171366 and costs exactly **×1.857** in Theorem ES-1 (§4.3). Worth one sentence.
- **§3.2's R_0 = 32 does not survive Stage 1.** Stage 1's cut-off needs d_1 = R/4 − 4 ≥ 12, i.e. **R ≥ 64** —
  SQ.md's own written R_0. By §3.3 this costs nothing (floor 3969, swamped by ≥ 9 decades), but the table
  should say 64.

### 10.3 For REVIEW_SQ_S4's author, and for SQ.md §0.3/§0.5, HIST and RLARGE (§6.6)

- **S4-14 item 2 and S4-16 use different binding entries of τ_♭.** S4-16 correctly takes
  t_pr = C′τ_♭ ≤ θ_0^{SUP} = 1/(3.31·10⁷C_D²) at large C_D; S4-14 item 2 computes η_♭ ≈ 4.2·10⁻³⁶ from
  τ_♭ = τ_R = 2.75·10⁻¹⁵, which requires **C_D ≤ 4.55·10²**. At the C_D that EPS-T produces (≈ 5·10¹⁵),
  **η_♭ = t_pr²/5.05·10⁹ = 3.5·10⁻⁸⁸**. The two items differ by 52 decades in η_♭.
- **The consequence is a clause S4-16 did not price.** The DESC-ε replacement for AE-red needs
  **η_♭ ≥ 4C_3ε_1²** (REVIEW_HIST_S4 strategic 4 and l.281; SQ.md l.223 states the substituted form), i.e.
  **ε_1 ≤ t_pr/(1.42·10⁵√C_3)** — **5.15 decades stronger** than the ε_1 < t_pr that S4-16 checked and passed.
  It fails by ≈ 9.7 decades of energy and would need **C_T ≲ 3.5·10¹⁰**, which is **2.2-2.5 decades below
  S4-16's own recorded ceiling C_T ≲ 10¹³** and below this route's floor (c_s ≥ 319.2 ⟹ C_T ≥ 4.4·10¹² at
  q = 12).
- **What it costs.** Not RLARGE's a_bad (linear clause, holds, margin ×1.99). Not HIST A5 via **AE-red
  itself** (η_AE = 1.78·10⁻¹⁵ covers 4C_3ε_1² by ≈ 63 decades). **It costs the replacement**: DESC-ε cannot
  discharge AE-red's size clause for A5 at this C_D, so (MS-Sob) returns for that one consumer — which is the
  hypothesis DESC-ε existed to remove. **Please settle whether S4-14 item 2's η_♭ should be restated at the
  new C_D and whether SQ.md §0.5's "all five are discharged by Corollary DESC-ε" survives.** ARGUED; I did not
  re-derive C_err, C_3, ε_1 or A5's energy bound.

### 10.4 For the lead

- **(EPS-STAR) answer: A_cγ_c ≤ 1 is PROVEN at an admissible ε_*, uniformly in C_K′, C_B and c_N.** The margin
  parameter in Stage 1's absorption is the whole mechanism: **A_cγ_c ≤ (1 + √6)·C_{S1}(q, m)/m** (Theorem ES-1).
  **C_T(q = 12) = 5.29·10¹², q_min = 11**, under STAR_CONST's conservative β-power B(8). The number is
  independent of every constant SQ.md leaves SUPPLIED — **so STAR_CONST §8.4 item 1 ("C_B and C_K′ are harmless
  for C_T") is now PROVEN, not ARGUED, and the missing entrywise bound on WB's kernel and BIA's BCH remainder
  is not on the critical path for C_T at all.** It only moves ε_*, by at most 3.4 decades across the whole
  SUPPLIED range.
- **ε_* must drop by 2.4·10⁴ to 6.8·10¹¹, not the factor 2-10 in my brief** (§5.2). Two bookkeeping slips, both
  disclosed; neither changes a conclusion, because the headroom is 21-25 decades.
- **The last symbol in C_T is closed. The ceiling is now set by steps (2) and (4)**: the source term is 73.8 %
  of Ĉ and the cut-off prefactor c_g = 5699.63 is the other 26.2 %; the curvature branch is **0.00 %**.
  Anything further on C_T is STAR_CONST's §8.4 item 4 (the 4× from (β + 1)² ≤ 4β² and the 2× in
  |∇(ζW)|² ≤ 2ζ²|∇W|² + 2g²W²), plus CONST_T's possible 36 → 18 (§10.2), worth ≈ 8-23× together. **The
  interface does not need them.**
- **The thing that should worry you is not ε_* but §6.6.** The interface's *linear* clause (ε_1 < t_pr) passes
  with margin ×1.99; its *quadratic* clause (η_♭ ≥ 4C_3ε_1²), which nobody priced, fails by 9.7 decades and
  demands C_T ≲ 3.5·10¹⁰ — below this route's own floor. **Lowering ε_* cannot touch it; only C_D can, and C_D
  is now an output.** I recommend that as the next bounded task, and it is a review task, not a derivation:
  decide which entry binds τ_♭ and whether §0.5's five consumers still discharge.
- **Lead decision D3, one level finer than STAR_CONST's reading of it.** STAR_CONST found that the enemy was a
  *count and a form*. Here the enemy was a **quantifier**: ε_* is existentially quantified in EPS-T, so the
  margin in Stage 1's absorption is free, and the ratio of the two inequalities that both measure ‖Φ‖ is what
  removes four SUPPLIED constants at once. **Before attacking an estimate, check which of its constants the
  theorem lets you choose.**

---

## 11. Disclosure 3 — a second provenance note, on §1's own header

§1's header reads "first edit of this file, **2026-10-28 14:00:05 UTC**". The file's mtime is **14:00:12 UTC**:
I read the clock at 13:59:13 UTC and wrote 14:00:05 into the header while composing, so the stated time is
**7 seconds early**, not late. The order is unambiguous and is the thing that matters — §1 was on disk at
14:00:12, before any derivation, before `es1_criteria.md` (14:11:04) and before `es1_eps.py` (14:12:50) — but
the second in that header is not the second the file landed, and I am recording it rather than editing §1.

Taken with §8.1, that is **two** forward-dated timestamps in my own files, both in headers I wrote while
composing. Neither reverses an order. The lesson for the next worker is mechanical: **stamp a header from
`date -u` at the moment of writing, not from the clock read before it.**

*(End of EPSSTAR.md. Files written by this worker: this file, `checks/es1_criteria.md`, `checks/es1_eps.py`,
`checks/es1_out.txt`, `checks/es1_out_prec60.txt`, `checks/es1_time.txt`. Nothing else, anywhere. No git
command was run by me.)*
