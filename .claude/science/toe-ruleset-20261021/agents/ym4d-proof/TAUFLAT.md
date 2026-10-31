# TAUFLAT — adjudication of the τ_♭ binding-entry conflict inside REVIEW_SQ_S4

Owner of this file: the τ_♭ adjudication worker, session 24 (ym4d-proof lane).
Scope: ONE bounded review decision. This file is not a derivation lane and adds no new mathematics to
the RG construction. Writable by me: this file and `checks/tf1_*`. Nothing else, anywhere.

---

## §0. PRE-STATED (first edit of this file)

**This is the first edit made to this file. UTC time of this edit: 2026-10-28T14:25Z.**

Statements only. Written before reading EPSSTAR.md §6.6, REVIEW_SQ_S4 S4-14/S4-16, SQ.md Sec. 13-§16,
HIST.md (AE-red / A5), REVIEW_HIST_S4 or SESSION24_RESULTS.md, and before any arithmetic. It cites no
quantity produced in session 24, and no number at all.

### §0.1 What I was asked to adjudicate

A worker in another lane (EPSSTAR.md, §6.6, self-labelled ARGUED and flagged separately by its author)
reports that the already-banked review REVIEW_SQ_S4 uses **two different binding entries of τ_♭** in two
of its own items, and that the discrepancy is many decades wide. The three questions, in order:

- **Q1 (fact).** Is the conflict real? Do the two cited items of REVIEW_SQ_S4 in fact take different
  binding entries for τ_♭, and does the decade gap in η_♭ follow when the chain's current C_D is used?
  The cheapest admissible outcome is that EPSSTAR has misread one of the two items, which would retire
  the whole finding.
- **Q2 (adjudication).** Is the Corollary DESC-ε replacement **load-bearing**? Specifically: what does
  DESC-ε feed; who consumes it; and is DESC-ε an *alternative* route to (AE) adopted because
  Theorem AE-red is conditional on (MS-Sob), or is it the *primary* route with AE-red as fallback?
- **Q3 (pricing, only if Q2 says load-bearing).** Name what a repair would have to be — a different
  (AE) route, a weakened DESC-ε, or (MS-Sob) proven so that AE-red carries (AE) by itself — and say
  which is cheapest. I will NOT attempt the repair.

### §0.2 Pre-registered definition of "LOAD-BEARING"

Fixed here, before reading. I will call the DESC-ε replacement **LOAD-BEARING** if and only if **both**
of the following hold, each established by citation to the *owning* file:

- **(LB-a) Unique supply.** Some statement S that a named consumer requires is, on this route, supplied
  *only* by DESC-ε — i.e. every other route to S named anywhere in the lane files is itself recorded in
  its owning file with a status of GAP, OPEN, or CONDITIONAL on an input that is itself recorded OPEN.
  A route recorded PROVEN, ARGUED, or CONDITIONAL-on-an-input-that-is-itself-live does **not** satisfy
  this; in that case the alternative route is alive and DESC-ε is redundant.
- **(LB-b) Live consumer.** At least one consumer of S is itself on a path that the lane's own ledgers
  describe as current (not withdrawn, not superseded, not recorded as dead).

If (LB-a) fails because AE-red's own route is alive, I will record the verdict as **NOT LOAD-BEARING**
and the finding as closed at a cost of nothing but the review text — regardless of how large the decade
gap in Q1 turns out to be. A large number attached to a redundant lemma is noise, and I pre-commit to
saying so.

If (LB-a) and (LB-b) both hold, I will record **LOAD-BEARING**, and then (AE) is dead *on this route*,
which is a major finding and must be reported as one.

**Explicitly pre-registered as NOT sufficient for LOAD-BEARING:**
- that DESC-ε is cited by many files (citation count is not consumption);
- that DESC-ε is the *newest* or the *sharpest* route (recency is not necessity);
- that AE-red's conditioning input is unproven (conditional-but-live is still a live route — the
  question is whether that input is recorded OPEN *and* unreachable, not merely unproven).

### §0.3 Pre-registered status rule for EPSSTAR §6.6

EPSSTAR's §6.6 is labelled ARGUED by its author. I will assign exactly one of:
- **CONFIRMED** — the arithmetic reproduces, the two items do use different binding entries, and the
  consequence EPSSTAR draws (which object pays) is the consequence I independently reach;
- **NARROWED** — the arithmetic reproduces but the consequence is smaller than stated (e.g. the object
  that pays is redundant, or the failing clause is not the one EPSSTAR names);
- **WRONG** — EPSSTAR misread one of the two items, or the two symbols it equates are distinct symbols,
  or the arithmetic does not reproduce.

I will quote statuses from the owning files verbatim rather than re-judging the underlying mathematics.
Where a status in an owning file is itself ambiguous I will say so and will not resolve it.

### §0.4 Pre-registered symbol-identity discipline

EPSSTAR §5 records that four distinct symbols in this lane are all written ε_*. Before I treat any two
occurrences of **τ_♭**, **θ_0**, **η_♭**, **t_pr**, **C_D**, **C_3**, **ε_1** or **C_T** as the same
quantity, I will check the *definition* at each occurrence in its owning file and record the check. If
two occurrences are distinct symbols, the conflict dissolves and the verdict is WRONG by §0.3. I
pre-register this as the single most likely way EPSSTAR's finding fails, and therefore as the first
thing I test after Q1's transcription.

### §0.5 Pre-registered arithmetic method

Any arithmetic will be done in exact `fractions.Fraction` or `decimal.Decimal` at fixed high precision,
in plain `python3 -I`, single-threaded, no numpy/BLAS, needing no numeric lock. Decade gaps will be
reported as exact rational ratios and as their `log10` only for display. No floating-point intermediate
will be allowed to carry a decade comparison.

### §0.6 Pre-registered falsifiability check on my own check (anti-tautology clause)

Session 24 found three verification gates that lacked the power to fail: a literal tautology, a gate
assembled from its own object's primitives, and an abelian model vacuous for a nonabelian claim. I
pre-register the following for anything I run here:

- My script must be able to return **both** verdicts. I will state, before running, an input
  substitution (a counterfactual value of the binding entry) under which the script returns the
  opposite verdict, and I will run that counterfactual as a designed-FAIL companion. If the
  counterfactual cannot make the check fail, the check is a tautology and I will report it as having
  no power, not as a PASS.
- My script will **transcribe** the lane constants from the owning files with file+line citations and
  will **not re-derive** them. Its job is arithmetic consistency between two transcriptions, nothing
  more. It therefore cannot and does not validate the constants themselves, and I will say so in the
  verdict rather than letting a reproduced number read as an endorsement of its source.
- A check that merely re-evaluates the same formula the source evaluated is not evidence. The only
  thing with the power to decide Q1 is the *definition* comparison of §0.4 plus the arithmetic under
  **each** of the two candidate binding entries, both computed, both reported.

### §0.7 What this file will NOT do

- It will not edit, restate or re-judge SQ.md, HIST.md, RLARGE.md, EPSSTAR.md, CONST_T.md,
  STAR_CONST.md or any REVIEW_* file. Requests on those go in a "FOR OTHER FILES (not edited)" section.
- It will not attempt the repair priced in Q3.
- It will not assign a status to any statement other than EPSSTAR §6.6 and (by the §0.2 test) the
  load-bearing question. Statuses of AE-red, A5, DESC-ε, (AE), (MS-Sob) and (REG-min) are quoted from
  their owners, not reassigned by me.

---

## §1. TF1-A — the symbol-identity gate, settled first

My §0.4 pre-registered this as the likeliest way the finding dissolves, and therefore as the first thing
to test. EPSSTAR §5/§6.1 records that **four** distinct constants in this lane are all written ε_*; the
same hazard plainly could apply to θ_0 and τ_♭. It does apply to θ_0, and it does **not** dissolve the
conflict. Verdict: **DISTINCT-AND-BOTH-BIND.**

**θ_0 is two different symbols**, and REVIEW_SQ_S4 says so itself:

- **θ_0^SUP := 1/(2·C_err)** — SQ.md Theorem SUP-price, l.188, with
  C_err := C_p(K² + K_top²) + 4C_e[K²/(L(L−1)) + 1.011·K·C_D·L/(L²−1)].
- **θ_0^{SQ4} := min{θ_G, θ_ε}** — SQ.md Theorem EPS-0, l.1622, a different object entirely (CARL's
  β-condition and ε_*/84).
- **REVIEW_SQ_S4 S4-14 item 4** flags exactly this: *"θ_0 collides with §0.3's θ_0 … Both appear as
  'θ_0/C′' inside τ-formulas (l.1633 and l.294/l.318), and **both constraints apply**. Rename one …
  this is load-bearing, not cosmetic."*

That last clause is decisive for Q1, because it means the two θ_0 are **not alternatives**: they are two
separate entries of the same minimum. Reading the two definitions:

- **τ_R := min{τ_0, τ_*, τ_S, θ_S/C′, θ_0^{SQ4}/C′}** (SQ.md l.1633, and §15.3's corollary l.1634).
- **τ_♭ := min{τ_F, τ_R, θ_0^SUP/C′, ε_M/(C_D·C′), θ_♯/C′, 1/(73.6·N·c′²·A′²)}** (SQ.md Corollary
  DESC-ε, l.317-319; the same list as Lemma DESC, l.294).

So **τ_R and θ_0^SUP/C′ are both entries of τ_♭'s min**, and τ_R itself carries θ_0^{SQ4}/C′ inside it.
Writing "τ_♭ = τ_R" is therefore an **evaluation of a minimum**, valid only while τ_R ≤ θ_0^SUP/C′. It is
not a definitional identity and it is not a symbol confusion. The conflict survives the gate.

**The other identity I was required to check** (§0.4): the ε_1 in HIST Theorem A5's clause and the ε_1 in
RLARGE's a_bad are **the same symbol**. RLARGE.md l.70 heads its ceiling table *"Current ε_1 ceiling
[v3-T, **A5**]"* and l.71's min is taken over A5's and SF's clauses together; HIST A5 l.1684 fixes
ε_1 ≤ ½δ_a with δ_a := min{δ_3, √(η_AE/C_3), ε_R/(C_♮√C_3), ε_R}. One symbol, two files. Good — because
Q3's cheapest lever turns out to be ε_1, and that would be worthless if the two were distinct.

**One symbol I did NOT equate, and the reader should not either:** the ε_* inside θ_ε (hence inside
θ_0^{SQ4}, hence inside τ_R) is **EPS-T's ε_*, symbol 1 of EPSSTAR §6.1** — not N5-sf0's
ε_* = 2.476·10⁻¹³/C_Δ, not BG-b's (ε_1²/(4NB))^{1/2}, not BFT_B l.2719's local one. Nothing in this file
compares across them.

---

## §2. Q1 — is the conflict real? **CONFIRMED**, and one of EPSSTAR's own numbers is wrong against it

Checks: `checks/tf1_criteria.md` → `checks/tf1_tau.py` → `checks/tf1_out.txt`. Exact `Fraction`
throughout; `Decimal` only to display; every decade comparison made on exact rationals.

### 2.1 The two items do use different binding entries

- **S4-16** (REVIEW_SQ_S4 l.366) takes **t_pr = C′τ_♭ ≤ θ_0^SUP**. Because θ_0^SUP/C′ is an entry of
  τ_♭'s min, this is an **upper bound that is valid whichever entry binds**. S4-16 is sound as written.
- **S4-14 item 2** (l.314) computes **η_♭ = c_♭τ_♭²/C′² ≈ 4.2·10⁻³⁶** from **τ_♭ = τ_R = 2.75·10⁻¹⁵**,
  having asserted in item 1 (l.311-313) that *"τ_R becomes the binding entry of DESC's τ_♭ … displacing
  SUP-price's θ_0/C′ = 7.6·10⁻⁹/53 = 1.43·10⁻¹⁰"*. That displacement is an **equality**, and it holds only
  inside a window.

**[TF1-C] The window, computed exactly.** τ_R ≤ θ_0^SUP/C′ ⟺ C_D² ≤ 1/(3.31·10⁷·C′·τ_R)
= 40000000000/192973 = 207283, i.e.

> **C_D ≤ 455.283301** (exact to 20 digits) — EPSSTAR's "C_D ≤ 4.55·10²", reproduced.

S4-14 item 1 is correct **at the C_D values in front of it** (0.45, 2, 2.25 — SQ.md l.218-219), and those
are the values SQ.md §0.3 Remark (a) records. But **S4-16, nine items later in the same file**, is the
item that turns C_D into an output: *"C_D ≈ (0.5-0.9)·10³·C_T"* (l.374), after which C_T ≈ 5.288·10¹²
(EPSSTAR §7.1) gives **C_D ≈ 4.76·10¹⁵ — outside the window by a factor 1.045·10¹³.** The two items of one
review are therefore **jointly consistent only on a C_D range that the later of the two destroys.**

I record what this is and is not. It is **not** an arithmetic error in either item. It is a **stale
evaluation of a minimum**: item 2 evaluated τ_♭ at a C_D that item 16 then superseded, and nothing in the
file re-ran item 2. That is the classic shape named in HANDOFF.md's closing paragraph — *"check what
someone fixed once and nobody revisited"* — occurring **inside a single review**.

### 2.2 The 52 decades, re-derived in exact arithmetic

| quantity | exact input | value |
|---|---|---|
| η_♭ at entry **A** (τ_♭ = τ_R) | c_♭τ_R²/C′², c_♭ = 1/640, C′ = 53 | **4.20662·10⁻³⁶** |
| η_♭ at entry **B** (τ_♭ = θ_0^SUP/C′) at C_D = 4.76·10¹⁵ | c_♭(θ_0^SUP/C′)²/C′² | **3.52310·10⁻⁸⁸** |
| exact ratio A/B | 1.1940126778191374946845063424·10⁵² (an exact integer) | **52.077 decades** |

> **[TF1-B] CONFLICT-REAL.** Threshold was ≥ 10 decades; the gap is **52.077**. At the other end of
> S4-16's own C_D band (0.5·10³·C_T) it is **51.056 decades** — so the finding does not depend on which
> end of the band is taken.

Also reproduced exactly: θ_0^SUP = **1.33384·10⁻³⁹**, t_pr = C′τ_♭ = θ_0^SUP = **1.33384·10⁻³⁹**,
1/(c_♭/C′⁴) = **5.04991·10⁹** (EPSSTAR's "t_pr²/5.05·10⁹"), and the strengthening factor of the clause
over the linear one, **2√(C′⁴/c_♭) = 142125 = 5.153 decades** (EPSSTAR's "1.42·10⁵", "5.15 decades").

### 2.3 **[TF1-D] CLAUSE-FAILS.** The DESC-ε (iii) hypothesis is missed by 9.707 decades

Corollary DESC-ε (iii) is gated on **E < η_♭**. Its size-clause consumers supply **E ≤ 4·C_3·ε_1²** (HIST
A5 (A), l.1698: *"By (a3-q) with δ = 2ε_1 ≤ δ_a, every full cone has E_𝒞(P)(ψ*) ≤ 4C_3ε_1² ≤ η_AE"*). At
ε_1 = 6.7·10⁻⁴⁰ (RLARGE l.71-72) and the reference C_3 = 1:

  4·C_3·ε_1² = **1.7956·10⁻⁷⁸**   against   η_♭ = **3.52310·10⁻⁸⁸**.

> **Shortfall: 9.707 decades of energy, 4.854 decades of ε_1.** Reported as a FAIL. EPSSTAR's "≈ 9.7
> decades (4.85 in ε_1)" is **exact**.

### 2.4 **[TF1-E] SOURCE-DISAGREES** — EPSSTAR's three repair figures are each off by √10, against itself

This was pre-registered at a tolerance of ×1.2 and it did not pass. I report it unaltered.

| | mine (exact) | EPSSTAR §6.6 l.525-526 | ratio |
|---|---|---|---|
| t_pr required | **9.5224·10⁻³⁵·√C_3** | 3.01·10⁻³⁵·√C_3 | **3.16359** |
| C_D ceiling | **1.7812·10¹³/C_3^{1/4}** | 3.17·10¹³/C_3^{1/4} | 0.561893 |
| C_T ceiling | **1.97911·10¹⁰ to 3.5624·10¹⁰** | 3.5·10¹⁰ to 6.3·10¹⁰ | 0.56546 |

The first ratio is **3.16359 against √10 = 3.16228** — a one-decade slip under a square root
(√(9.07·10⁻⁶⁹) read as √(9.07·10⁻⁷⁰)), which then propagates as √ into C_D and C_T. **The direction
matters and it is unfavourable to EPSSTAR's own case: the repair bar is 1.78× harder than it reported**,
and the corrected C_T ceiling sits **2.347 decades below this route's own floor** (C_T ≥ 4.4·10¹², from
c_s ≥ 319.2, EPSSTAR §7.4) rather than the 2.2-2.5 decades it quotes against S4-16's recorded ceiling.
**No conclusion of §6.6 changes; the finding is marginally stronger than its author stated.**

### 2.5 **[TF1-G] The check has the power to fail**

Per §0.6, mandatory. One input substituted — C_D set to the TF1-C window boundary / 2 = 227.642, chosen by
the script, nothing else touched — and the script returns **CONFLICT-ABSENT** (gap −1.204 decades) and
**CLAUSE-HOLDS** (margin 42.370 decades of energy). Both verdicts flip. The gate is not a tautology, is
not assembled from the object's own primitives (it compares **two independent transcriptions** against a
threshold fixed before either was read), and is not vacuous for the statement at issue.

**What it still cannot catch, stated rather than left implied:** it cannot detect an error in SQ.md's
derivation of η_♭, in S4-16's C_err model, in EPSSTAR's C_T, or in RLARGE's ε_1 ceiling. It is an
arithmetic-consistency check between transcriptions and a reproduced number here is **not** an
endorsement of its source. **[TF1-H] PASS**: the 52.077008938-decade figure is identical at 40 and 80
digits, and every verdict was decided on exact rationals, not on those displays.

---

## §3. Q2 — THE ADJUDICATION. Is the DESC-ε replacement LOAD-BEARING?

### 3.1 What DESC-ε feeds, and who consumes it

Corollary DESC-ε (SQ.md l.317-328) has three conclusions, and **only the third is gated on η_♭**:

- **(i) Sizes** and **(ii) Top** are parametric in τ ≤ τ_♭ (hypothesis "E < c_♭τ²/C′²") — **unaffected**.
- **(iii) AE-red's two conclusions** — the log bound |log U_k(P)|²_HS ≤ (1.011²NC′²/c_♭)·E **and** the size
  bound (C′/√c_♭)√E — are gated on **E < η_♭**. **This is the clause that fails.**

SQ.md §0.5's completed consumer list ([RSQ1-fix S1-2]) names **five** consumers, and the failure splits
them cleanly in two:

| # | consumer | what it consumes | survives the §6.6 failure? |
|---|---|---|---|
| 1 | **HIST Theorem A5 (A)** (HIST l.1684-1702) | the **size clause**, via E ≤ 4C_3ε_1² | **NO** |
| 2 | **HIST (I_k^E)′ (a4)** (HIST l.1411-1415) | the **size clause** | **NO** |
| 3 | **SF.md** l.97-99, l.838 (via A5) | the **size clause** | **NO** |
| 4 | **HW TE (ii)** (W-bad, W-cb, FV) | the **infimum/energy form** — (ii) on a minimiser, or DESC (b) | **YES** |
| 5 | **RLARGE §3.3 branch (iii)** (Lemma INF) | the **infimum form** | **YES** |

Consumers 4 and 5 run on (CLS-min) via DESC (b)'s min-form, whose binding clause is the **linear** one
ε_1 < t_pr: 6.7·10⁻⁴⁰ < 1.33·10⁻³⁹, margin **×1.99** (S4-16; EPSSTAR §7.4). They are untouched.
**3 of 5 consumers lose their DESC-ε supply; 2 of 5 keep it.** Nothing else consumes it: Theorem RED-0
cites only *"DESC-ε's **conventions**"* (SQ.md l.1153, the height ordering), not η_♭.

### 3.2 Replacement or primary? **Replacement — offered by SQ.md and not yet adopted by the consuming files**

The brief asked me to decide this, and the files answer it in their own words.

- SQ.md §0.3, l.348: *"So every consumer of AE-red's size clause (§0.5) **may cite DESC-ε instead**."* And
  it names the exchange rate: AE-red's conclusions *"on E < η_♭ in place of E ≤ η_AE, and **with NO
  (MS-Sob)**"*. The word is "instead". DESC-ε is an **option**.
- SQ.md §0.6 [RSQ1-fix S1-3/S1-4], the superseding paragraph: *"(SQ) and the general-chain (AE) **remain
  true-in-kind and stay a parallel route**."* The AE route was explicitly **retained**, not withdrawn.
- **HIST has not been edited to cite DESC-ε.** Theorem A5 is still stated *"CONDITIONAL ⇐ (a5-G) +
  (a5-U) + (a3-q) + (MS-Sob) **(the last through Theorem AE-red, §26)**"* (HIST l.1683-1684). So in the
  owning file, **AE-red is still A5's route of record.**
- **The existence lane never adopted DESC-ε at all.** `grep` over EXISTENCE.md returns **zero**
  occurrences of "DESC-ε" and **zero** of "(REG-min)". Its chain is CLS-cone ⇐ (AE), and it records
  **(AE) OPEN** (EXISTENCE.md l.4784 *"branch (iii) ⇐ CLS-sf cone form ⇐ (AE) ⇐ (MSG) + (MS-Sob) … (AE)
  **OPEN**"*; l.4801; l.3113; l.3548).

### 3.3 Is AE-red's own route alive? Its **number** is; its **status** is OPEN

Two separate questions, and conflating them is how this item could be got wrong in either direction.

- **The number: alive, comfortably. [TF1-F] AE-CLAUSE-HOLDS.** AE-red's gate is E ≤ η_AE with
  η_AE = 1.776·10⁻¹⁵ (REVIEW_HIST_S4 l.368, at C_S ≤ 10²). Against the same 4C_3ε_1² = 1.7956·10⁻⁷⁸ it
  holds by **63.00 decades of energy (31.50 in ε_1)**, and at the other end of the recorded C_S range
  (C_S = 10⁴, η_AE = 8.9·10⁻¹⁶) by **62.70 decades**. EPSSTAR's "≈ 63 decades to spare" is right.
  REVIEW_HIST_S4's binding instruction *"Write η_AE as a function of (C_S, ε_S), not as a number"*
  (l.370-371) does **not** threaten this: 2 decades of C_S move η_AE by 0.3 decades against a 63-decade
  margin.
- **The status: CONDITIONAL on an input recorded OPEN.** REVIEW_HIST_S4 l.50 and its tally l.448:
  **"Theorem AE-red: CONFIRMED as CONDITIONAL ⇐ (MS-Sob)."** And HIST l.1323: **"(MS-Sob) [OPEN; P]"**,
  with HIST l.1325 (CONFIRMED at REVIEW_HIST_S4 l.84): *"MS-Sob ⇐ MSG-loc-dev **[OPEN]** + MS-HLS
  [PROVEN] + (SQ-dev) **[OPEN]**: ARGUED"*. HIST l.1892 states the trade plainly: *"(AE) OPEN →
  CONDITIONAL ⇐ (MS-Sob); **(MS-Sob) becomes the named OPEN wall in its place**."*

### 3.4 The fact that decides it: **DESC-ε's own hypothesis is discharged, and AE-red's is not**

This is the point the brief's framing did not have, and it is in SQ.md's own tally.

SQ.md §16's post-session-4 tally reads: **"PROVEN-HERE counted 14 / CONDITIONAL 1 (linear MS-Sob …;
**PRICE-iii and DESC-ε have their hypothesis (REG-min) discharged by §15.3**) / OPEN 1"**. The discharge
is Theorem EPS-0 (§15.3) ⇒ (REG-min) by Theorem RED-0 (§13.5), and REVIEW_SQ_S4's tally row confirms it:
*"**Theorem EPS-0** | PROVEN as an implication, uncounted | **CONFIRMED**; 'no bootstrap' is TRUE."*
SQ.md §15.3 states the corollary in terms: *"Hence the session-1/2 CONDITIONAL items lose their
hypothesis: Corollary PRICE-iii … and **Corollary DESC-ε**."*

So, immediately before §6.6, the ledger was:

| route to AE-red's size clause | hypothesis | status of that hypothesis |
|---|---|---|
| **Theorem AE-red** (HIST §26) | (MS-Sob) | **OPEN** (⇐ ARGUED ⇐ two further OPEN items) |
| **Corollary DESC-ε** (SQ.md §0.3) | (REG-min) | **DISCHARGED** by Theorem EPS-0 (CONFIRMED) |

**DESC-ε was the only route to that clause with no OPEN hypothesis.** That is what §6.6 destroys — not by
finding a gap in it, but by showing its threshold is 9.707 decades too small for the energy its consumers
supply.

### 3.5 Verdict

> ### **LOAD-BEARING — YES**, by the test pre-registered in §0.2, with the scope stated exactly.
>
> **(LB-a) Unique supply: SATISFIED.** The only other route to DESC-ε (iii)'s conclusions named anywhere
> in the lane files is Theorem AE-red, recorded by its own reviewer as **CONDITIONAL ⇐ (MS-Sob)**, and
> (MS-Sob) is recorded **OPEN** in its owning file (HIST l.1323), reducing only ARGUED to two further
> OPEN items. DESC-ε was therefore the unique route to that clause **free of an OPEN hypothesis**.
>
> **(LB-b) Live consumer: SATISFIED.** HIST A5 (A) is live (REVIEW_HIST_S4 re-labels it ARGUED and says
> it *"becomes CONDITIONAL as soon as S4-1 and S4-2 are applied"*, both statement-level edits — not
> withdrawn); SF.md's (BG-loc) and STEP-3 wall list consume it; the existence lane consumes CLS-cone ⇐
> (AE) in eight places.

**And now the part that keeps this from being an over-claim, which my §0.2 obliges me to state as
plainly as the verdict.** The honest consequence is a **status regression, not a new death**:

1. **(AE) is not newly dead, and I do not claim it is.** (AE) is recorded OPEN in HIST (l.1366, l.1495),
   OPEN in EXISTENCE.md (l.4784, l.4801), and named as OPEN in RLARGE's branch-(iii) chain. For every
   consumer that reads its status from those files, **nothing changed today**: they were already consuming
   an OPEN item.
2. **What dies is the merger claim.** SQ.md §0 fix (4) — *"(SQ)/(MS-Sob) leave the critical path only
   CONDITIONALLY: DESC-ε derives every consumed conclusion ⇐ (REG-min)"* — and §0.5's headline **"All five
   are discharged by Corollary DESC-ε"** are **false for consumers 1-3** at the current C_D. They stand
   for consumers 4-5.
3. **(MS-Sob) and (SQ-dev) therefore return to the critical path** for HIST A5 (A), HIST (I_k^E)′ (a4) and
   SF.md. **HANDOFF.md's seven-item critical path names neither** — precisely because SQ.md's merger had
   taken them off it. That list is now incomplete, and that is the single most consequential downstream
   effect of this item.
4. **EPSSTAR §6.6 item 4 is correct clause by clause** ("not RLARGE's a_bad; not HIST A5 via AE-red
   itself; what it breaks is the replacement"). What it **understates** is that the replacement was the
   only route without an OPEN hypothesis, so the cost is not the loss of a convenience but a regression in
   the project's status ledger. I record that as an **extension** of its finding, not a correction to it.

---

## §4. Q3 — pricing the alternatives. The cheapest is **ε_1**, and nobody priced it

The clause to be met is **η_♭ ≥ 4·C_3·ε_1²**, with η_♭ = c_♭τ_♭²/C′² = t_pr²·(c_♭/C′⁴) = t_pr²/5.04991·10⁹
and t_pr = θ_0^SUP = 1/(3.31·10⁷·C_D²). **Only three quantities appear: t_pr (i.e. C_err, i.e. C_D, i.e.
C_T), ε_1, and C_3.** Every repair must move one of them, so the list of alternatives is closed and short.

**A. Sharpen C_T. DEAD, and by more than reported.** Needs C_T ≲ 1.98·10¹⁰ (§2.4), i.e. **2.347 decades
below** this route's own floor C_T ≥ 4.4·10¹². Worse, C_T has only **0.080 decades of room** above that
floor, and since C_err ∝ C_D² ∝ C_T², those buy only **0.160 decades of C_err** against the **4.854**
needed. Confirmed dead, with the brief's framing confirmed.

**B. Sharpen C_err's PREFACTOR — a lever the brief's framing missed, but it falls ~1.7 decades short.**
θ_0^SUP = 1/(2C_err) has **two** independent levers, not one: C_D (lever A, floored) and the prefactor
1.655·10⁷ in C_err = 1.655·10⁷·C_D². SQ.md's own Remark (a) (l.206, l.224) says *"C_e and K dominate C_err
(h6 measured MSG at 3.5 against 66), so **optimisation could gain several orders: unclaimed**"* — so this
lever is explicitly on offer and unexplored. **[POST-HOC, TF1-P2]** prices it
(`checks/tf1b_posthoc.py`, `checks/tf1b_out.txt`; transcription gate: it reconstructs C_err/C_D² =
1.65954·10⁷ against S4-16's stated 1.655·10⁷, ratio 1.00274 — which also **independently corroborates
S4-16's C_err model**):

- Required: **C_err down ×71391 (4.854 decades)**, since η_♭ ∝ 1/C_err².
- The 4C_e bracket is **96.32 %** of C_err. **Deleting it entirely** gives only **1.433 decades.**
- The residue C_p(K² + K_top²) then forces **K/C_D from 78.3 down to 1.525, a factor 51.3**, where h6's
  measured-against-proven ratio for the MSG constant is **18.9**.
- **Most optimistic package on record** (C_e deleted *and* K taking h6's full ×18.9): C_err/C_D² ≈ 1.72·10³
  against the 2.32·10² target — still **≈ 0.87 decades short in C_err, ≈ 1.74 decades short in energy.**

So B is the only *constant-sharpening* route that is not already floored, it is session-scale rather than
paper-scale, and on the file's own measured evidence it lands **about 1.7 decades short**. It is worth
naming; it is not a repair.

**C. Lower ε_1 by 4.854 decades. THE CHEAPEST, and it needs no new mathematics. [POST-HOC, TF1-P1]**

ε_1 appears in the clause **quadratically and with the helpful sign**, and **ε_1 is bounded only from
above**: RLARGE.md l.70-72 heads its entry *"**Current ε_1 ceiling** [v3-T, A5]"* and gives a min of five
upper bounds. Nothing in the files I read bounds ε_1 from below. (SQ.md l.312's and HW.md l.603's
"ε_1 ≥ C′τ_♭" is **not** a floor — it selects which branch of a_bad := c_pr·min{ε_1², t_pr²} applies, and
it already fails at today's numbers, which is exactly why RLARGE is in the ε_1² branch.) So:

- **Required: ε_1 ≤ t_pr/142125 = 9.38496·10⁻⁴⁵**, against today's ceiling 6.7·10⁻⁴⁰ — a drop of
  **4.854 decades**. **ε_1 < t_pr is preserved** (the ratio becomes ×142125, vastly better than today's
  ×1.99), so **consumers 4 and 5 and RLARGE's a_bad branch are not disturbed in kind.**
- **Price, in RLARGE's own currency:** a_bad = c_pr·ε_1² falls by **9.707 decades**
  (2.5·10⁻⁸⁵ → ≈ 5.0·10⁻⁹⁵); a = θa_bad ≲ 2·10⁻⁹⁶; n_H ≳ 4/(aβ_−) rises from ≈ 2·10⁸⁷ to ≈ 10⁹⁷;
  the wrap levels rise from ≈ 184 to ≈ 205; and g_K² ≲ a/10² falls from ≈ 10⁻⁸⁸ to ≈ 10⁻⁹⁸.
- **Why that price looks affordable on the files' own reading:** RLARGE l.617-618 says of exactly these
  quantities *"This is far above the binding DX′ ceiling g_0² ≲ 2.5·10⁻¹⁵²/C_Ω (REVIEW_SF_S7 C-1), so
  **RLF's own ceilings do not bind** at the current constants"* — a 54-decade margin, of which this costs
  ≈ 10. HANDOFF.md's withdrawn item 1 says the same in general terms (binding ceiling g_0² ≲
  2.5·10⁻¹⁵²/C_Ω, slack ×3.59·10⁵⁶). The cost is paid in n_H and wrap levels, which RLARGE already
  chose as *"many-level, K-independent"* (l.792).
- **What I have NOT done, and this is a condition on the recommendation:** I have not swept every ε_1
  consumer in RLARGE, HW, SF, PLD and EXISTENCE. Lowering ε_1 **enlarges the large-field region** (χ_Q's
  indicator, RLARGE l.58), and whether any clause needs ε_1 large is for RLARGE's and SF's owners.
  **This is a priced candidate, not a verified repair**, and it goes to them in §5.

**D. Prove (MS-Sob) so AE-red carries the clause by itself. The structurally cheapest, and already the
project's route of record.** AE-red's number holds by **63 decades** (§3.3), so **no constant work is
needed at all** — the whole cost is the OPEN item (MS-Sob) ⇐[ARGUED] MSG-loc-dev [OPEN] + MS-HLS [PROVEN]
+ (SQ-dev) [OPEN]. This is paper-scale, it is the route HIST, SF and the existence lane already cite, and
it is the only option that restores **all three** lost consumers at once rather than one clause.

**E. A different (AE) route, as named by the reviewer who confirmed AE-red.** REVIEW_HIST_S4 strategic 4:
*"A **per-scale sup pricing** (MSG-type conditions at each level, as in Balaban CMP 109 (1.14)-(1.16))
would avoid (MS-Sob), η_AE and these constants entirely."* Paper-scale, and it would retire this whole
item along with (MS-Sob). Named for completeness; I have not assessed it.

**F. A weaker DESC-ε.** I price this at **not available**, with a reason rather than a shrug: DESC-ε
(iii)'s threshold is η_♭ = c_♭τ_♭²/C′² because the descent of Lemma DESC must **terminate below τ_♭**
(SQ.md l.330-338: each case needs E ≥ c_♭τ²/C′², and τ ≤ τ_♭ is what makes FORCE, KQ and SUP-price
applicable at all). The **quadratic** dependence on τ_♭ is the mechanism, not a bookkeeping loss. Any
weakening must therefore raise τ_♭, which is lever A or B. There is no third place to stand.

> ### **Cheapest, named: C (lower ε_1 by 4.854 decades)** — zero new mathematics, ~10 decades spent out of
> a recorded 54-decade margin, and it must be ratified by RLARGE's and SF's owners because I did not sweep
> every ε_1 consumer. **Cheapest that restores all three consumers: D ((MS-Sob)), which is the route of
> record anyway.** B is worth one session and lands ≈1.7 decades short. **A is dead.**

---

## §5. Status assigned, and the ledger delta

> ### **EPSSTAR.md §6.6: ARGUED → CONFIRMED.**

Against the three options pre-registered in §0.3:

- The arithmetic reproduces exactly (52.077 decades; 9.707-decade shortfall; 5.153-decade strengthening;
  C_D window 455.283301) — **[TF1-B] CONFLICT-REAL, [TF1-D] CLAUSE-FAILS**.
- The two items **do** use different binding entries of τ_♭, and the two θ_0 in play are **distinct
  symbols both of which bind** — **[TF1-A] DISTINCT-AND-BOTH-BIND**, so it is not the symbol collision
  that would have made it WRONG.
- The consequence EPSSTAR draws — *which object pays* — is the one I independently reach: **the
  replacement**, not RLARGE's a_bad, not A5 via AE-red itself.

**Two amendments, both recorded against it rather than folded in:**

- **An arithmetic correction, unfavourable to the source. [TF1-E] SOURCE-DISAGREES.** Its three repair
  figures are each off by **√10** from a one-decade slip under a square root: t_pr required is
  **9.5224·10⁻³⁵√C_3** (not 3.01·10⁻³⁵), C_D ≤ **1.7812·10¹³/C_3^{1/4}** (not 3.17·10¹³),
  C_T ≲ **1.98·10¹⁰-3.56·10¹⁰** (not 3.5-6.3·10¹⁰). The repair bar is **1.78× harder** than reported. No
  conclusion changes.
- **An extension.** §6.6 does not say that DESC-ε was the **only** route to that clause with a discharged
  hypothesis (SQ.md §16's own tally), so it understates the cost as the loss of an option when it is a
  regression in the status ledger (§3.4-§3.5). And it does not price the **ε_1** lever, which is the
  cheapest repair and which its own framing ("only C_D can touch it, and C_D is now an output") rules out
  by inspection rather than by computation.

### 5.1 What dies, exactly

- **DIES.** The claim that DESC-ε discharges the **size clause** for **HIST A5 (A), HIST (I_k^E)′ (a4) and
  SF.md** — SQ.md §0.5's "All five are discharged by Corollary DESC-ε" and §0 fix (4)'s "(SQ)/(MS-Sob)
  leave the critical path", for 3 of the 5. With it dies the only route to that clause whose own
  hypothesis is discharged.
- **DIES.** The reading, implicit in HANDOFF.md's critical-path list, that **(MS-Sob) and (SQ-dev) are off
  the critical path.** They are back on it, for three named consumers.
- **SURVIVES.** **(CLS-min)** to **HW TE (ii)** and **RLARGE §3.3 branch (iii)** (the min-form/infimum
  form, linear clause ε_1 < t_pr, margin ×1.99). **RLARGE's a_bad = c_pr·ε_1²**. **Theorem A5 via AE-red
  itself** (63 decades of margin on the number; status unchanged at CONDITIONAL ⇐ (MS-Sob)).
  **DESC-ε (i) and (ii)**, which are parametric in τ and never see η_♭. **Theorem RED-0**, which uses only
  DESC-ε's conventions. **Theorem EPS-0, EPS-T, (REG-min)** — all untouched; this is a threshold being too
  small, not a proof being wrong.
- **UNCHANGED.** The **existence lane**, which never adopted DESC-ε (zero occurrences in EXISTENCE.md) and
  already records **(AE) OPEN**. Nothing in layer 2 moves.

### 5.2 Checks, provenance, and disclosures

Files written by me: **this file**, `checks/tf1_criteria.md`, `checks/tf1_tau.py`, `checks/tf1_out.txt`,
`checks/tf1_stdout.txt`, `checks/tf1_time.txt`, `checks/tf1b_criteria.md`, `checks/tf1b_posthoc.py`,
`checks/tf1b_out.txt`. **Nothing else, anywhere. No git command was run by me.**

| id | pre-registered verdict | result |
|---|---|---|
| **TF1-A** | symbol identity: DISSOLVED or DISTINCT-AND-BOTH-BIND | **DISTINCT-AND-BOTH-BIND** (reading; §1) |
| **TF1-B** | CONFLICT-REAL iff ≥ 10 decades | **CONFLICT-REAL** — 52.077 (51.056 at the band's other end) |
| **TF1-C** | report the joint-consistency window exactly | **C_D ≤ 455.283301**; current C_D outside it by ×1.045·10¹³ |
| **TF1-D** | CLAUSE-HOLDS / CLAUSE-FAILS | **CLAUSE-FAILS** — 9.707 decades of energy, 4.854 of ε_1 |
| **TF1-E** | SOURCE-REPRODUCED within ×1.2 | **SOURCE-DISAGREES** — three figures off by √10, against the source |
| **TF1-F** | AE-CLAUSE-HOLDS / FAILS | **AE-CLAUSE-HOLDS** — by 63.00 decades (62.70 at C_S = 10⁴) |
| **TF1-G** | counterfactual must flip the verdicts, else NO POWER | **PASS** — both flip; the gate can fail |
| **TF1-H** | exact/displayed verdicts agree at two precisions | **PASS** — identical at 40 and 80 digits |

**One pre-registered verdict did not pass: TF1-E.** Output kept unaltered, criteria untouched, script
unedited; the disagreement is reported in §2.4 with its direction and its probable cause.

Order, by mtime (UTC): **TAUFLAT.md §0 14:25:40** → tf1_criteria.md 14:33:00 → tf1_tau.py 14:34:35 →
tf1_out.txt 14:34:41 → tf1b_* 14:36:33 → §1-§6 of this file. §0's header states "14:25Z" and the file
landed at 14:25:40Z, i.e. **within the stated minute and not forward-dated** — I read the clock
immediately before writing, which is the mechanical lesson EPSSTAR §11 left for the next worker.

**Disclosure.** `tf1b_criteria.md` and `tf1b_posthoc.py` share an mtime second (both written in one shell
block), so **file order is not demonstrable for the post-hoc probe**. Nothing rests on it: TF1-P2 is
labelled POST-HOC in its source, its output and in §4, carries **no** pre-registered verdict, and its only
check with force is the transcription gate (reconstructed C_err within ×1.00274 of S4-16's figure). The
pre-registered chain (tf1) is unaffected and its order is clean by seven minutes.

**Numerics.** Exact `fractions.Fraction` throughout; `Decimal` only to display; plain `python3 -I`, single
thread, OMP/OPENBLAS/MKL = 1, nice 10, no numpy, no BLAS. **0.04 s real.** No numeric lock taken and none
needed (exact rational arithmetic, per the brief's rule 6).

### 5.3 The single biggest remaining obstruction in my scope

**None that is mine to close** — this was an adjudication and it is closed. The obstruction it *hands on*
is: **(MS-Sob) is back on the critical path for three named consumers, and the cheapest alternative
(lowering ε_1 by 4.854 decades) is a decision for RLARGE's and SF's owners, not a derivation.** The
deeper obstruction is the one lead decision D3 names, in its sharpest form yet: **a threshold that is
quadratic in a constant that is now an output of the very theorem it is meant to gate.** t_pr ∝ 1/C_D² and
η_♭ ∝ 1/C_D⁴, so **every decade of C_D costs four decades of this clause.** That is why no sharpening
reaches it.

---

## §6. FOR OTHER FILES (not edited)

I wrote only this file and `checks/tf1_*`, `checks/tf1b_*`. I did not touch SQ.md, HIST.md, RLARGE.md,
EPSSTAR.md, CONST_T.md, STAR_CONST.md, HANDOFF.md, SESSION24_RESULTS.md, EXISTENCE.md or any REVIEW_*
file. The following are requests.

### 6.1 For REVIEW_SQ_S4's author (binding, and it is the smallest fix on this list)

**S4-14 item 2 is stale, not wrong.** Its η_♭ ≈ 4.2·10⁻³⁶ and item 1's *"τ_R becomes the binding entry of
DESC's τ_♭"* are both correct **only for C_D ≤ 455.283301** (TF1-C, exact), i.e. only at the C_D values
SQ.md l.218-219 records (0.45, 2, 2.25). **S4-16, in the same file, supersedes them** by making
C_D ≈ (0.5-0.9)·10³·C_T. Suggested edit: add one sentence to item 2 reading *"valid only while
C_D ≤ 4.55·10²; at the C_D that S4-16's own model produces, the binding entry is θ_0^SUP/C′ and
η_♭ = t_pr²/5.05·10⁹"*, and one to item 1 saying which entry binds **as a function of C_D** rather than
as a fact. **S4-16 itself needs no change**: its t_pr ≤ θ_0^SUP is an upper bound and is valid whichever
entry binds. **S4-14 item 4's instruction to rename one θ_0 is the root cause and should be executed**,
because this error is exactly what that collision makes easy.

### 6.2 For SQ.md's owner (§0.3 l.348, §0.5 l.376, §0 fix (4) l.90)

1. **§0.5's "All five are discharged by Corollary DESC-ε" does not survive, for three of the five.** At
   C_D ≈ 4.76·10¹⁵, η_♭ = 3.52·10⁻⁸⁸ against the 4C_3ε_1² = 1.80·10⁻⁷⁸ that consumers 1-3 supply —
   **short by 9.707 decades**. Consumers **4 (HW TE (ii))** and **5 (RLARGE branch (iii))** are
   **unaffected**: they take the infimum/min-form, whose binding clause is the linear ε_1 < t_pr
   (margin ×1.99). Please split the sentence in two accordingly.
2. **§0.3 l.349's "η_♭ ≈ 10⁻²⁶ (C_D = 2)" and l.223's "η_♭ ≈ 10⁻²⁶ gives ε_1 ≲ 5·10⁻¹⁴/√C_3" are now
   three evaluations out of date** (10⁻²⁶ → 4.2·10⁻³⁶ → 3.5·10⁻⁸⁸). Suggested: state η_♭ as a **function
   of C_D**, η_♭ = 1/(5.04991·10⁹·(3.31·10⁷·C_D²)²), and never as a number — the same instruction
   REVIEW_HIST_S4 l.370 gave HIST for η_AE, for the same reason.
3. **§0 fix (4) must be narrowed.** "(SQ)/(MS-Sob) leave the critical path only CONDITIONALLY" is true for
   the energy/infimum form and **false for the size clause** at this C_D. Note also that **§0.6's retained
   "parallel route" is now the *only* route** to the size clause, so its parenthetical "(worth having as
   classical results, but are not consumed)" is no longer accurate.
4. **One sentence worth adding to Remark (a) (l.206, l.224).** Your own "C_e and K dominate C_err …
   optimisation could gain several orders: unclaimed" is now a **priced** item: η_♭ ∝ 1/C_err², the clause
   needs C_err down ×71391 (4.854 decades), deleting the whole 4C_e bracket gives only **1.433** of them,
   and the residue needs K/C_D from 78.3 to **1.525** (×51.3) against h6's measured ×18.9 — so the most
   optimistic package on record lands **≈1.7 decades short in energy**. Worth recording so the next worker
   does not spend a session on it. (`checks/tf1b_out.txt`; POST-HOC, and it reconstructs S4-16's
   C_err = 1.655·10⁷·C_D² to ×1.00274, which corroborates that model independently.)

### 6.3 For HIST's owner, and for SF.md's owner

- **Theorem A5 (A)'s route of record is unchanged and remains AE-red ⇐ (MS-Sob).** Its **number** is
  healthy: 4C_3ε_1² = 1.80·10⁻⁷⁸ against η_AE = 1.776·10⁻¹⁵ clears by **63.00 decades** of energy, and by
  **62.70** at C_S = 10⁴, so REVIEW_HIST_S4 l.370's "write η_AE as a function of (C_S, ε_S)" does not
  threaten the clause. **No edit is needed on that account.**
- **What is needed is a note that the alternative offered in SQ.md §0.3 is not available at the current
  C_D.** If HIST or SF had been about to cite DESC-ε to drop (MS-Sob) from A5's hypothesis list — SQ.md
  l.348 invites exactly that — **do not**, at C_D ≈ 4.76·10¹⁵. Same for **(I_k^E)′ (a4)** (HIST
  l.1411-1415) and **SF.md l.97-99 / l.838**.

### 6.4 For RLARGE's owner and SF.md's owner (the Q3 decision, and it is yours)

**The cheapest repair of the DESC-ε clause is to lower ε_1 by 4.854 decades, to ≤ 9.38496·10⁻⁴⁵, and only
you can say whether it is admissible.** What I can say:

- ε_1 enters the clause **quadratically with the helpful sign**, and RLARGE l.70-72 records a **ceiling**,
  never a floor. I found **no lower bound on ε_1** in RLARGE, HW, SQ, HIST or PROOF. SQ.md l.312's and
  HW.md l.603's "ε_1 ≥ C′τ_♭" is a **branch selector** for a_bad := c_pr·min{ε_1², t_pr²}, not a floor,
  and it already fails today.
- **ε_1 < t_pr is preserved and improved**, from ×1.99 to ×142125 — so the thin margin S4-16 flagged as
  "met, but not comfortably" becomes comfortable.
- **The price, in your currency:** a_bad ≈ 2.5·10⁻⁸⁵ → ≈ 5.0·10⁻⁹⁵; a ≲ 2·10⁻⁹⁶; n_H ≈ 2·10⁸⁷ → ≈ 10⁹⁷;
  wrap levels ≈ 184 → ≈ 205; g_K² ≈ 10⁻⁸⁸ → ≈ 10⁻⁹⁸. **Your own l.617-618 says these do not bind** (the
  binding DX′ ceiling is g_0² ≲ 2.5·10⁻¹⁵²/C_Ω, ≈ 54 decades below), so ≈ 10 decades looks affordable.
- **The question I could not answer:** lowering ε_1 **enlarges the large-field region** (χ_Q, l.58). Does
  any clause — (TH-ch″), (TC), the §9/§9A records, the (SF-last)/torus many-level item, PLD's — need ε_1
  **large**? Please settle it. Also note **U7** (l.815, *"which (CLS-min) source is primary given the
  current ε_1 ceiling"*) is now a sharper question than when it was written.

### 6.5 For the lead (HANDOFF.md, SESSION24_RESULTS.md, PROOF.md)

1. **HANDOFF.md's critical-path list is incomplete.** Its seven items name neither **(MS-Sob)** nor
   **(SQ-dev)/MSG-loc-dev**, because SQ.md §0's merger had taken them off the path. For **HIST A5 (A),
   HIST (I_k^E)′ (a4) and SF.md**, the merger does not hold at this C_D and **they are back on it.**
   This is the main ledger consequence of the item and it is a one-line addition.
2. **SESSION24_RESULTS.md propagated the inconsistency.** Its REVIEW_SQ_S4 entry carries *"τ_R ≤ 2.75e-15
   (**now the binding entry of τ_♭**, displacing 1.43e-10), η_♭ 1e-26 → 4.2e-36"* in the **same entry**
   as *"C_D ≈ (0.5-0.9)e3 · C_T"*. Both halves are in your ledger and they contradict each other for any
   C_T > 4.55·10²/900 ≈ 0.5. Worth one correction line, since your own note on this item already says
   *"a review is evidence, not a certificate"*.
3. **The DESC-ε replacement is LOAD-BEARING** in the specific sense of §3.4-§3.5: it was the only route to
   AE-red's size clause whose own hypothesis was **discharged** (SQ.md §16: *"PRICE-iii and DESC-ε have
   their hypothesis (REG-min) discharged by §15.3"*), the alternative being CONDITIONAL ⇐ (MS-Sob) [OPEN].
   **But (AE) is not newly dead** — it is recorded OPEN in HIST, in RLARGE's branch-(iii) chain and in
   eight places in EXISTENCE.md, and the existence lane never adopted DESC-ε, so **layer 2 does not move.**
   Please do not let this be written up as "(AE) died today"; what died is a merger that was banked.
4. **Cheapest repair: lower ε_1 (§4 C), owner-gated to RLARGE/SF.** Cheapest that restores all three
   consumers: **prove (MS-Sob)** (§4 D) — paper-scale, and already the route of record. **C_T sharpening
   is dead** (§4 A), with only 0.080 decades of room above its own floor against 4.854 needed.
5. **EPSSTAR §6.6 → CONFIRMED**, with its three repair figures corrected **upward in difficulty by √10**
   (§2.4). Its author's recommendation to run this as a review task rather than a derivation was right,
   and the whole item cost one script, 0.04 s and no numeric lock.
6. **A process observation, since the session has been collecting them.** The defect was not an error in
   anybody's mathematics. It was a **minimum evaluated once and never re-evaluated** after a later item in
   the **same file** changed one of its entries — and the reason it was easy is the **θ_0 name collision**
   that S4-14 item 4 had itself flagged as *"load-bearing, not cosmetic"* and that nobody renamed. The
   mechanical rule that would have caught it: **a `min{…}` whose entries depend on quantities still being
   derived should be recorded as a function, never evaluated to a number** — which is precisely what
   REVIEW_HIST_S4 l.370 told HIST to do with η_AE, and what §6.2 item 2 now asks of η_♭.

*(End of TAUFLAT.md. Files written by this worker: this file, `checks/tf1_criteria.md`,
`checks/tf1_tau.py`, `checks/tf1_out.txt`, `checks/tf1_stdout.txt`, `checks/tf1_time.txt`,
`checks/tf1b_criteria.md`, `checks/tf1b_posthoc.py`, `checks/tf1b_out.txt`. Nothing else, anywhere. No
git command was run by me.)*

---

## §7. Scope disclosure (appended; §5.2 left as written)

My scope was **this file and new files under `checks/` prefixed `tf1_`**. The three post-hoc files are
named `tf1b_criteria.md`, `tf1b_posthoc.py`, `tf1b_out.txt` — prefix **`tf1b_`**, not `tf1_`. That is a
deviation from the letter of my scope. They are new files in the same private namespace, they overwrite
nothing, no other worker in this session uses a `tf1*` id, and I have not renamed them because the mtimes
recorded in §5.2 would then be wrong. Recording it here rather than quietly fixing it, which is the
convention EPSSTAR §8.1 and STAR_CONST §12 set for provenance in this lane. If the lead prefers strict
naming, they are `tf1_p2_*` under any rename and nothing in §4 or §5 depends on the filenames beyond the
citations given.

Everything else in my scope was observed: **no file outside this one and `checks/tf1*` was written or
modified**; SQ.md, HIST.md, RLARGE.md, EPSSTAR.md, CONST_T.md, STAR_CONST.md, HANDOFF.md,
SESSION24_RESULTS.md, EXISTENCE.md and every REVIEW_* file were **read only**; requests on them are
confined to §6; **no git command was run.**
