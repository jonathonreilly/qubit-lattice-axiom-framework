# EPS1_EXEC — executing EPS1_SWEEP §5's conditions (C1)-(C7) for target T55-B

Owner of this file: the T55-B execution worker, session 25 (ym4d-proof lane).
Writable by me: this file and new files under `checks/` prefixed `ee1_`. Nothing else, anywhere.
No git command will be run by me.

---

## §0. PRE-STATED (first edit of this file)

**This is the first edit made to this file. UTC time of this edit: 2026-10-28T21:04:53Z.**

Statements only. No number is derived below in this section, and nothing produced in session 25 is cited.
What I have read before writing this: the session-25 shared brief, `HANDOFF.md`, and `EPS1_SWEEP.md`
(a session-24 file) for the *statement* of the conditions I am to discharge. No constant from any of them
appears in this section. I have not yet opened RLARGE.md, EXISTENCE.md, PLD.md, HIST.md, NORMS.md, SF.md,
BFT_B.md, FLOW.md or ARS_FIX.md, and I have run no arithmetic.

### §0.1 The task, as given

`EPS1_SWEEP.md` §5 returned **SAFE WITH NAMED CONDITIONS (C1)-(C7)** on TAUFLAT §4 option C — lowering the
small-field plaquette cut. The owner has instructed that the change be **executed, not surfaced again**.
My job is to discharge the seven conditions, one at a time, each with its own verdict, and to write the
executed change as **append-ready patch text** for the lead to land. I write no file but my own.

### §0.2 Targets, in the order I will take them

- **(T-C6) The number, first.** Determine by file:line which numerical value of the small-field cut is
  **in force** for the χ_Q threshold of RLARGE §0, and what each other live value is and what it is for.
  (C6) is a **genuine prerequisite**: a symbol with several live values cannot be lowered, because "lower
  it by N decades" has no referent. **If the value is not determinate, T55-B stops here and I say so.**
  I pre-register that outcome as a legitimate result, not a failure to deliver.
- **(T-C1) Scope.** Write the scoping sentence that confines the change to one symbol, and **verify by
  reading** the four cited line references that the other two named thresholds are in fact different
  objects with different definitions — not merely differently named.
- **(T-C3) The floor.** Record that the floor is of the form "the cut must exceed the typical field", not
  "none", and re-derive the three margin figures and the three clauses that live on it from their owning
  files' own formulas.
- **(T-C4) The admissible value.** Derive the requirement the proposed value must satisfy from its own
  chain, and state the largest admissible value, with the direction of the rounding made explicit.
- **(T-C5) The two steeper exponents.** Re-derive both prices from the owning files' formulas rather than
  from the summary lines that quote them.
- **(T-C7) The conditionality.** State in the patch text which two uncertified hand constants the verdict
  rests on, and the ceiling value at which the margin is exhausted. Do not write the patch as
  unconditional.
- **(T-C2) NOT MINE.** A parallel worker owns the adoption that changes one exponent's steepness. I will
  **not** duplicate it. I will instead write my patch so that it is **correct under both outcomes**: the
  (C5) price is given at both steepnesses, and I will name the single clause of my patch that changes in
  each case.

### §0.3 Pre-registered verdict scale, per condition

Exactly one of, for each of (C1), (C3), (C4), (C5), (C6), (C7):

- **DISCHARGED** — the condition is met, the facts it asks for are established here from the owning files,
  and the patch text carries them.
- **DISCHARGED WITH NOTE** — met, but a residual is recorded that a reader must see (a stale evaluation
  elsewhere, an ARGUED rather than PROVEN step, a transcription to reconcile).
- **NOT DISCHARGED** — not met, with the reason. If any condition is NOT DISCHARGED, the patch text for
  the clauses depending on it is **withheld**, not weakened.

### §0.4 Pre-registered failure modes (how this execution should break)

Written before any derivation, so that finding one is a result:

- **(X1) The number is indeterminate.** Two or more live values are each defensible as "in force" for the
  χ_Q threshold, with no line in an owning file selecting between them. Then **(C6) is NOT DISCHARGED and
  T55-B stops**. Pre-registered as the single most likely way this target fails.
- **(X2) C2-F1 — a condition that is not bookkeeping.** The lead's reading (D4) is that (C2) is the only
  non-bookkeeping condition. If any of (C1), (C3)-(C7) turns out to require new mathematics, a new
  decision, or to change a status, that reading is wrong and the session reorders. I pre-register that I
  will report it **loudly and first** if found.
- **(X3) A scoping sentence that does not actually separate the symbols.** If one of the three named
  thresholds turns out to be *defined in terms of* another, the scoping sentence is a fiction and (C1) is
  NOT DISCHARGED.
- **(X4) A floor clause that is not merely tightened but emptied.** If any of the three clauses on the
  floor has a threshold that does **not** move with the cut, then no number of decades of price buys it
  and (C3) is NOT DISCHARGED.
- **(X5) The admissible value's own chain has moved.** The requirement that fixes the value was evaluated
  at some constant; if that constant is now an output rather than an input anywhere in the lane, the value
  is stale before it is written. This is the brief's defect 2 and the shape of session 24's 52-decade
  error. I will check it explicitly rather than assume it.
- **(X6) A price whose exponent I cannot source.** If a steeper exponent rests on a constant that its
  owning file never writes, it is ARGUED and must be labelled so in the patch, not quietly priced.

### §0.5 Pre-registered method

- **Symbol discipline.** For every occurrence I rely on, I read the **definition in force at that
  occurrence in its owning file**, and I quote the file:line in my text. Two occurrences are the same
  symbol only if I can cite one definition both use or a line equating them. This is the brief's defect 1.
- **Stale-constant discipline.** For every inequality I rely on, I state **what constant it was evaluated
  at** and **whether that constant is still an input**. This is the brief's defect 2.
- **Banked results.** A banked PROVEN is evidence, not a certificate. Where a load-bearing step is cited
  as proven elsewhere, I re-derive it here or I label the dependence.
- **Arithmetic.** Exact `fractions.Fraction` in plain `python3 -I`, single thread, no numpy, no BLAS, no
  numeric lock (brief rule 6). Decades displayed via `Decimal` at high fixed precision; no floating-point
  intermediate carries a decade comparison.
- **Criteria before scripts** (brief rule 2). Any numeric check gets `checks/ee1_<id>_criteria.md` with
  pre-registered PASS/FAIL verdicts written **before** the script, containing no constant derived in this
  session.
- **A designed-FAIL control for every gate** (brief defect 3). Every check I run gets an input I know
  should fail it, and I report that the control failed. A gate with no control is not evidence, and I will
  grade my own checks' power honestly, including "NO POWER" if that is the answer.

### §0.6 What this file will NOT do

- It will **not edit any file but this one** and `checks/ee1_*`. All requested changes go in
  `## FOR OTHER FILES (not edited)` as literal append-ready text for the lead to land.
- It will **not** do (C2)'s work (the adoption that re-steepens one exponent), which is another worker's.
- It will **not** re-judge the DESC-ε failure, TAUFLAT's adjudication, EPS1_SWEEP's SAFE-WITH-CONDITIONS
  verdict, or the status of (MS-Sob), (AE), AE-red or (REG-min). Those are quoted from their owners.
- It will **not** write distance-to-finish commentary (owner instruction, 2026-10-28).
- It will **not** claim that executing a bookkeeping change proves anything about the construction. The
  change moves one threshold and repairs the records that quote it; the mathematics is unchanged, and the
  patch text will say so.

### §0.7 Pre-registered statuses

PROVEN (a complete argument written out here from stated hypotheses) / COMPUTED (exact) / ARGUED /
CONDITIONAL (naming the input) / GAP / OPEN. A failed check is reported as a FAIL with output and script
unaltered; a re-run takes a new id and leaves the criteria untouched; any probe run after seeing a result
is labelled POST-HOC.

---

## §1. (C6) FIRST — which ε_1 is in force. **DISCHARGED WITH NOTE.**

> ### The four values are not four candidates. They are a **2 × 2 table** — (old class / rerun class) × (pre-TB-1 / post-TB-1) — and **both axes are resolved by named, binding, already-recorded decisions**. The cell in force is **ε_1 ≤ 6.7·10⁻⁴⁰**, RLARGE.md l.72 and l.612.

Status: **COMPUTED (reading, with the factorisation verified exactly: `checks/ee1b_out.txt`, ee1b-1
**FACTORISES**, worst cell ×1.0021, designed-FAIL control separates).**

### §1.1 What the symbol is, at the occurrence that matters

**RLARGE.md l.58**: `χ_Q := Π_{p⊂int Q}1{||1 - U(p)||_op < ε_1}` (cube-INTERIOR plaquettes only). So
ε_1^cut is a cut on the **operator norm of 1 − U(p)**, over **cube-interior level-k plaquettes**. That
is the object option C moves, and no other.

### §1.2 The two axes, each with the line that resolves it

**Axis 1 — the TB-1 correction.** REVIEW_SF_S7.md l.198-200: *"**TB-1 (binding).** The binding entry is
ε_bg^{(TH-bg)}/C_bg with the a_p entry only, but (TH-bg) (l.2117) is ε_bg²(n_1/2 + 1.03κ_sn_K) ≤
½min{a_p, a_c}. With a_c ≈ a_p/2 (KF, κ_s = 1; SF's own A-1) and n_K = 1024 **the factor is 0.7056**"*.
It is listed as *"1 binding threshold fix (TB-1)"* at l.61 and as binding fix 2 at l.297. **So the
factor 0.7056 is applied**; a value without it is pre-TB-1 and stale on this axis.

*Where 0.7056 comes from, since a factor nobody can decompose is a factor nobody can check*:
0.7056² = 0.49787, against ½ = 0.50000 (`ee1_out.txt`). So 0.7056 = (1/√2)·0.99787 — the 1/√2 is
a_c = a_p/2 entering under a square root (ε_bg² ≤ ½min{a_p,a_c}), and the residual 0.99787 is the
1.03κ_sn_K = 1054.7 term added to n_1/2. Both halves are named at l.199 and neither is mine.

**Axis 2 — the constant class.** REVIEW_SF_S7.md l.249-250 states the rule: *"a PROOF edit must adopt
𝔠, λ_min and ε_* **for the same class**. Either keep the old class (236.43 / 4.2295·10⁻³ / 1.7·10⁻²⁴) or
adopt the new one (315.19 / 3.1727·10⁻³ / 2.48·10⁻¹³)."* l.251 prices the axis: the rerun class is
*"slightly worse (**×0.75**)"* for ε_1 below the C_Δ break-even.

**RLARGE declares which class is in force, in the sentence that heads the ceiling.** RLARGE.md l.70:
*"**Current ε_1 ceiling [v3-T, A5].** On the class adopted by PROOF session 23 ([SF7-edit]:
𝔠_∞^♯ = 315.19, λ_min ≥ 3.17·10⁻³, ε_* = 2.476·10⁻¹³/C_Δ)"* — the **rerun** class, by l.250's own
triple.

### §1.3 The table, and the exact factorisation [COMPUTED, `checks/ee1b_out.txt`]

Base: REVIEW_SF_S7 l.196, *"At τ^A, (TH-ch′) gives **1.2687·10⁻³⁹**"* — old class, a_p entry only.

| | **a_p entry only** (pre-TB-1) | **full (TH-bg), ×0.7056** (TB-1, BINDING) |
|---|---|---|
| **old class** (𝔠 = 236.43, λ_min = 4.2295·10⁻³, ε_* = 1.7·10⁻²⁴) | **1.2687·10⁻³⁹** — REVIEW_SF_S7 l.196, l.44; **SF.md l.2837**; **NORMS.md l.746** | **8.95·10⁻⁴⁰** — REVIEW_SF_S7 l.47, l.200, l.297; **RLARGE.md l.611** |
| **rerun class, ×0.75** (𝔠 = 315.19, λ_min = 3.1727·10⁻³, ε_* = 2.476·10⁻¹³/C_Δ) — **ADOPTED, RLARGE l.70** | **9.52·10⁻⁴⁰** — REVIEW_SF_S7 l.53, l.247; **RLARGE.md l.71**, first entry of the min | **6.7·10⁻⁴⁰** — **IN FORCE**; REVIEW_SF_S7 l.53, l.247, l.297; **RLARGE.md l.72, l.612** |

| cell | recorded | predicted = 1.2687·10⁻³⁹ × (class) × (TB-1) | ratio |
|---|---|---|---|
| old, pre | 1.2687·10⁻³⁹ | 1.2687·10⁻³⁹ | 1.000000 |
| old, TB-1 | 8.95·10⁻⁴⁰ | 8.951947·10⁻⁴⁰ | 1.000218 |
| rerun, pre | 9.52·10⁻⁴⁰ | 9.515250·10⁻⁴⁰ | 0.999501 |
| **rerun, TB-1** | **6.7·10⁻⁴⁰** | **6.713960·10⁻⁴⁰** | 1.002084 |

Worst cell ×1.0021 against a pre-registered ×1.01. **Neither factor was read from the cell it predicts**
(0.7056 from l.199, 0.75 from l.251, the cells from l.196/l.47/l.53/l.247), so this is not a tautology.
**Designed-FAIL control**: with the TB-1 factor replaced by ½ — the plausible misreading, "a_c ≈ a_p/2"
taken as a factor on ε_1 rather than under the square root — the gate returns **DOES-NOT-FACTORISE**
(worst ×1.4109). **The control failed, as required. HAS-POWER.**

### §1.4 Verdict, and the three records that are stale

**(C6) DISCHARGED.** The ε_1 in force for RLARGE §0's χ_Q threshold is **ε_1 ≤ 6.7·10⁻⁴⁰**
(**RLARGE.md l.72**, repeated at **l.612**), being REVIEW_SF_S7's base 1.2687·10⁻³⁹ carried through the
binding TB-1 fix and the adopted rerun class. The number **is** determinate, failure mode (X1) does not
fire, and T55-B proceeds.

**The note, and it is the substance of (C6).** The other three values are each stale on a named axis,
and one of them is worse than stale:

1. **RLARGE.md l.71**'s 9.52·10⁻⁴⁰ is pre-TB-1 — but the *same line* carries the correction in
   parentheses, *"(TB-1: ≈ 6.7·10⁻⁴⁰)"*, and l.72 takes it. **Not a defect; a correction shown in place.**
2. **RLARGE.md l.611**'s 8.95·10⁻⁴⁰ is old-class — and l.611 is a row of a **recomputation table** whose
   own status column reads *"v1's n_* formula, not n_H"*, directly above the v3 row at l.612 that uses
   6.7·10⁻⁴⁰. **Not a defect; a historical row, labelled.** (l.609's row is likewise labelled
   *"illustrative; not admissible under (TH-ch″)"*.)
3. **SF.md l.2837**'s 1.27·10⁻³⁹ **is** a defect: it is stale on **both** axes, and REVIEW_SF_S7 l.298
   issued a **binding** order to repair exactly it — *"Rescale the §22.7 ε_1 rows"* — which has not been
   carried out. Its companion row l.2840, `HW a_bad = 8.4·10⁻⁸⁵`, is stale by the same ×1/0.7056² = ×2.0.
4. **NORMS.md l.746 is the one that can mislead a reader**, and worse than EPS1_SWEEP recorded. It
   quotes *"ε_1 = 1.27·10⁻³⁹ (SF.md l.2837)"* and then, **in the same sentence** (l.747-748), names the
   constants that set it as *"(𝔠_∞^♯ = 315.19, λ_min ≥ 3.17·10⁻³, ε_* = 2.476·10⁻¹³/C_Δ, r_♭ = 1/220)"* —
   **the rerun class**. So NORMS pairs an **old-class, pre-TB-1 value** with **rerun-class constants**:
   precisely the pairing REVIEW_SF_S7 l.249-250's rule forbids. **EPS1_SWEEP §1.1 calls this "one
   evaluation stale"; it is two, and they are inconsistent with each other inside one sentence.**

**Does this change NORMS's conclusion?** No, and I checked rather than assumed. NORMS l.752 concludes
*"this result does not improve ε_1 or g_K². It restores the legitimacy of their k-independence."* That
is a statement about the **existence** of a k-independent ε_1, not its value; the value appears only as
an illustration. The stale number is a citation defect, not a load-bearing one. Recorded as an edit in
§9, not as an obstruction.

### §1.5 One correction to the brief, per lead decision D6

My scope prompt says: *"Note the brief's defect 1: there are FIVE distinct ε_1 in this lane, not four,
per ARS_FIX §1."* **This conflates two different counts, and both files were already right.**

- **ARS_FIX.md §1 is about η_1, not ε_1.** Its heading is *"η_1 IS THREE SYMBOLS"*. The "five" appears
  only in a parenthesis at **ARS_FIX.md l.213**, *"unlike ε_1 (five symbols) and ε_* (four)"*, which
  cites EPS1_SWEEP's own count back at it.
- **EPS1_SWEEP §1 already says five**, in its heading: *"ε_1 IS SEVERAL SYMBOLS — at least FIVE"*.
- **(C6)'s "four" is a count of numerical VALUES of symbol 1** (§1.1 of that file), not of symbols.
  Four values of one symbol and five distinct symbols are both correct and are not the same count.

So there is no discrepancy to repair, and (C6) as written needed no amendment on this point. I record it
because acting on the correction would have had me hunting a fifth *value* that does not exist.

---

## §2. (C1) Scope. **DISCHARGED.**

Status: **PROVEN from the cited text** (the four references were read; the definitions are quoted).

### §2.1 The four references, read

| ref | what is actually there | type of object |
|---|---|---|
| **BFT_B.md l.3058** | `ε_1 := [Λ_2(L²/(L²−1))(4C_eΛ_2 + 12c_h(Λ_2^{(1)})²Λ_2)]^{−1}·min(1,…)`, introduced as the threshold at which `f_{j_0} ≤ 2Λ_2f_k`; l.3059 adds *"ε_1 = ε_1(L, φ, N, d) independent of k, T, j and of any global gauge"* | an **explicit formula** in O(1) geometric constants, bounding the **coarse flatness f_k** |
| **BFT_B.md l.2870** | *"(N2-0)_j … There are ε_1 > 0 and C_N, C_ax, C_box < ∞ … such that for every V ∈ 𝒦(ε_1)"*, with 𝒦(ε) := {V : f_k(V) ≤ ε} at **l.2865** | the **radius of a configuration class in coarse flatness** |
| **FLOW.md l.1927** | *"On a disc \|φ\| ≤ ε_1 (fixed): ‖𝒯(φ) − Q‖ ≤ c_Tφ², π_- ≤ 𝒫(φ) ≤ π_+"*, φ the Cartan variable of l.1925 (`X = i·diag(x)`) | a **disc radius** in a Cartan expansion parameter |
| **FLOW.md l.2834** | *"B a Cartan level-k background of constant level-k flux F … \|q_αF\| ≤ ε_1"* | a bound on a **root-projected constant flux** |

Against **RLARGE.md l.58**'s `χ_Q := Π_{p⊂int Q}1{‖1 − U(p)‖_op < ε_1}`: four different objects, in
three different variables, none of them a cube-interior plaquette-norm cut. **They are different
thresholds, confirmed by reading.**

### §2.2 The (X3) test: is any of them *defined in terms of* another?

Pre-registered failure mode (X3) was that the scoping sentence might be a fiction. It is not:

- BFT_B's ε_1 is an explicit function of Λ_2, Λ_2^{(1)}, C_e, c_h, L alone (l.3058) — **no RLARGE
  quantity appears**.
- FLOW's two are a free small parameter ("(fixed)") and a hypothesis radius — neither is derived.
- RLARGE's ε_1 is bounded by the five-entry min at l.71, whose entries are τ_c/C_bg-driven together with
  C_Δ, C_♭, r_♭ — **no BFT_B or FLOW quantity appears**.
- Grep confirms the absence of a tie: **BFT_B.md and FLOW.md contain no statement equating their ε_1 to
  RLARGE's**, and BFT_B's single `χ_Q` (l.971) is a *smooth weight* with coarse gradient 1/M_c, not
  RLARGE's indicator — a sixth collision, on the symbol χ_Q, incidental here.

**(X3) does not fire.** The scoping sentence separates genuinely independent objects.

### §2.3 The scoping sentence, to be written exactly

> **The threshold lowered here is ε_1^cut, the small-field plaquette cut of RLARGE §0 — the ε_1 of
> `χ_Q := Π_{p⊂int Q}1{‖1 − U(p)‖_op < ε_1}` at RLARGE.md l.58, bounded above by the five-entry min at
> RLARGE.md l.70-72. It is NOT BFT_B's Theorem N2 threshold (BFT_B.md l.3058, the class radius of
> 𝒦(ε_1) at l.2865, l.2870), which is defined by an explicit formula in O(1) geometric constants and
> must not be moved; and it is NOT FLOW's disc radius (FLOW.md l.1927) or its root-flux bound
> (FLOW.md l.2834). No quantity in BFT_B or FLOW changes as a result of this edit.**

**Why the "must not be moved" clause is load-bearing and not boilerplate:** BFT_B.md l.2866 records
`𝒞_glob(ε) ⊂ 𝒦(4ε + Cε²)`. Lowering 𝒦's radius would propagate into 𝒞_glob's ε, a cascade nobody has
priced. The sentence exists to stop that, not to be tidy.

---

## §3. (C3) The floor. **DISCHARGED WITH NOTE — and the note is a sign correction to (C3) itself.**

Status: **COMPUTED** (`checks/ee1_out.txt`, ee1-4, both designed-FAIL controls passed).

### §3.1 The floor exists and it is ε_1 ≫ g, confirmed by reading the two clauses

- **EXISTENCE.md l.3111-3112**: *"**(b) coercivity away from the flat set inside 𝒮_j**: u𝓔_k ≥ u·c·
  (distance to the flat set)², uniformly in k, **for configurations at distance ≫ g but < ε_1**."*
  Quoted verbatim. The window is (≫ g, ε_1) and it empties if ε_1 ↓ g.
  *Status of the clause itself, read rather than assumed:* l.3112-3113 marks it **"Corollary CLS-cone,
  CONDITIONAL ⇐ (AE), OPEN"**. So narrowing the window makes an **open** item harder; it does not break
  a proven one.
- **EXISTENCE.md l.4191-4192**: *"**[RX11-fix 6] ε := ε_1** (the (RLF-3^dis) threshold of §13.4; nothing
  in §20 needs ε < ε_1, **ε only has to contain the typical field ≍ g**; for ε < ε_1, (RLF-3^dis)_ε is a
  strictly stronger hypothesis)."* Quoted verbatim. This is the floor's statement.

**The (X4) test — is either threshold one that does not move with ε_1?** Yes for `g`: g is fixed by the
DX′ ceiling and is **ε_1-independent** (SF.md l.2587: *"(GF-B^𝔥) drives only the τ_c rows … **not
ε_1**"*). So the window genuinely narrows. But it does not **empty**, and nothing acquires a
threshold-form hypothesis it cannot meet. **(X4) does not fire: the cost is quantitative.**

*One reading that could have fired (X4) and does not.* EXISTENCE l.4198-4200 says that for ε < ε_1,
(LF-loc)^ε *"would be a strengthened hypothesis (more cubes bad, smaller a_d), **not implied by
§13.4**"*. That is about choosing ε **below** the ε_1 in force. Option C lowers **ε_1 itself**, and
RX11-fix 6's identification ε := ε_1 moves with it, so the hypothesis remains (RLF-3^dis) itself at the
new threshold. What the proof lane must deliver is the same parametric theorem re-evaluated — which is
exactly what EPS1_SWEEP §3 prices — not a statement of a new kind.

### §3.2 The margin, re-derived [COMPUTED, `checks/ee1_out.txt`]

g at the binding DX′ ceiling is `g_0 ≤ 1.57·10⁻⁷⁶/√C_Ω` (**REVIEW_SF_S7.md l.204**). At C_Ω = 1:

| | ε_1 | g | log₁₀(ε_1/g) |
|---|---|---|---|
| in force | 6.7·10⁻⁴⁰ | 1.57·10⁻⁷⁶ | **36.6302** |
| proposed | 9.38·10⁻⁴⁵ (§4) | 1.57·10⁻⁷⁶ | **31.7765** |

**Reproduces EPS1_SWEEP §2.2's 36.63 → 31.78 exactly.** The window narrows by 4.854 decades and retains
31.78. **Defect-2 note on the constant this is evaluated at:** C_Ω is set to 1 here, and larger C_Ω
*lowers* g, which *widens* the window. So 31.78 is a **lower bound in C_Ω ≥ 1** — the one direction in
this whole exercise where an uncertified constant can only help.

### §3.3 **The sign of PLD l.995 is inverted in (C3) as written. Reported as a correction.**

(C3) instructs me to record *"PLD l.995's ℓ¹ absorption margin 2m_*g/ε_1, which loses 4.854 decades"*,
following EPS1_SWEEP §2.2's *"the ℓ¹ absorption margin is proportional to **g/ε_1** and **shrinks as ε_1
falls at fixed g**"* and §2.3's row *"**falls 4.854 decades** … the one ratio with the unhelpful sign"*.

**At fixed g, g/ε_1 rises when ε_1 falls.** [COMPUTED, ee1-4]

| | g/ε_1 at fixed g = 1.57·10⁻⁷⁶ |
|---|---|
| at ε_1 = 6.7·10⁻⁴⁰ | 2.343284·10⁻³⁷ |
| at the proposed ε_1 | 1.672891·10⁻³² |
| change | **+4.8536 decades — RATIO-RISES** |

**Two designed-FAIL controls, both of which behaved as required**, so this is not my own arithmetic slip:
1. *Known-invariant control.* With g ∝ ε_1 (the ε-driven ceiling, EPS1_SWEEP §2.4's own structural fact)
   the gate returns **INVARIANT** to 10⁻⁴⁵ decades — it does not report a change where the lane's own
   structural fact says there is none.
2. *Reversed-input control.* With ε_1 **raised** ×10 at fixed g, the gate returns **RATIO-FALLS**. It is
   not a gate that says "rises" whatever it is fed.

**And the direction matters for the clause, not just for the ratio.** PLD.md l.994-995 reads: *"(SG^{net})
with constants (σ_*, m_*) holds at t = ε_1/(σ_*²g²) **iff v ≤ σ_*²g² + 2m_*σ_*²g³/ε_1**. Hence no Gaussian
model whose aligned variance exceeds **σ_*²g²(1 + 2m_*g/ε_1)** satisfies (SG^{net})."* The quantity
2m_*g/ε_1 is the amount by which the aligned variance **may exceed** σ_*²g². It **rises** by 4.854
decades, so the admissible set of models **grows** and the no-go of l.1003-1004 (*"no proof of
(SG^{net})_k by Gaussian domination with the true two-point function can work for aligned (smooth)
families"*) becomes **weaker**. **Every reading of the clause moves in the helpful direction.**

### §3.4 What the honest cost on PLD actually is

Not the margin — the **range**. **PLD.md l.983-984** defines *"(SG^{net})_k (the form RLF-step consumes;
weaker). The same inequality only for s_p = t·u_p with |u_p|_HS = 1 and **0 ≤ t ≤ ε_1/(σ_*²g_k²)**."*
Lowering ε_1 **shrinks the amplitude range on which (SG^net) is asserted** by 4.854 decades at fixed g.
A smaller range is an easier hypothesis to prove and a weaker one to consume.

**Is that a cost?** Priced honestly: it is **neutral at the ε-driven ceiling and not priced at the DX′
one.** The range exists because RLF-step needs tilts up to the size that pushes a plaquette to the ε_1
threshold, so range and requirement are the *same* ε_1 and scale together — the same invariance
EPS1_SWEEP §2.4 found everywhere else. What is **not** established, by me or by anyone, is whether the
consumer's needed t is ε_1-proportional in every use. That is PLD's to say, and §9 asks for one sentence.

I also note a **second** ε_1 occurrence in the same block that (C3) does not mention: **PLD.md l.987**'s
`𝒱^{sf}(A) := {every level-(k+1) plaquette within level-(k+1) distance R_bg of A has ‖1 − V_P‖_op < ε_1}`,
flagged in the file itself as *"(a cut-good neighbourhood; **all plaquettes, not only cube-interior
ones**)"*. Same threshold constant, a **different plaquette set** from χ_Q's. Lowering ε_1 shrinks
𝒱^{sf}, so (SG^fl) is asserted for fewer V — again a weakened hypothesis, again unpriced.

### §3.5 Verdict

**(C3) DISCHARGED WITH NOTE.** The floor is real, it is ε_1 ≫ g and not "none", it is respected with
**31.78 decades** after the move (36.63 before), and the three clauses were read in their owning files.
**The note is binding on the patch text: (C3)'s third clause has its sign the wrong way round.** Writing
it into PLD.md as given would plant a false sentence in the file that owns the quantity. The patch in §9
records the corrected direction and names the range, not the margin, as the thing that narrows.

---

## §4. (C4) The admissible value. **NOT DISCHARGED AS WRITTEN — and this is the C2-F1 finding.**

Status: **COMPUTED** (ee1-2, `checks/ee1_out.txt`; POST-HOC EE1-P1/EE1-P2, `checks/ee1b_out.txt`,
`checks/ee1c_out.txt`).

(C4) as given: *"Use 9.38495e-45 or lower, not 9.38496e-45 (EPS1_SWEEP §4.5 — the quoted value was on the
wrong side of its own bound). Derive the bound and state the admissible value."* I derived the bound.
It does not support the condition as stated, in **three** independent ways.

### §4.1 The bound, derived

The clause is **DESC-ε (iii)**'s gate `E < η_♭` met by the size-clause consumers' `E ≤ 4C_3ε_1²`
(**HIST.md l.1698**: *"By (a3-q) with δ = 2ε_1 ≤ δ_a, every full cone has E_𝒞(P)(ψ*) ≤ 4C_3ε_1² ≤ η_AE"*).
So

> **ε_1^cut ≤ √(η_♭/(4C_3))**,  with  **η_♭ = t_pr²/5.04991·10⁹** and **t_pr = θ_0^SUP = 1/(3.31·10⁷·C_D²)**
> (TAUFLAT.md l.371-372), i.e. **ε_1^cut ≤ t_pr/(142125·√C_3)** (the 142125 = 2√(C′⁴/c_♭), TAUFLAT l.205).

### §4.2 **FAIL 1 — at the η_♭ its own source publishes, (C4) has no content.** [ee1-2(a): NO-DISCRIMINATION]

η_♭ is published by TAUFLAT at **six** significant figures (l.196, l.213: **3.52310·10⁻⁸⁸**) and at
three (l.561: 3.52·10⁻⁸⁸). EPS1_SWEEP §4.5 carries it at **twelve** (3.52309230578·10⁻⁸⁸), a figure that
appears in no owning file. The clause verdict depends on which:

| η_♭ as published | exact bound √(η_♭/4), C_3 = 1 | TAUFLAT's 9.38496e-45 | EPS1_SWEEP's 9.38495112638e-45 |
|---|---|---|---|
| **3 s.f.** (TAUFLAT l.561) | 9.38083151964686·10⁻⁴⁵ | **FAILS** | **FAILS** |
| **6 s.f.** (TAUFLAT l.196, l.213) | 9.38496137445434·10⁻⁴⁵ | **holds** | **holds** |
| **12 s.f.** (EPS1_SWEEP §4.5) | 9.384951126377803·10⁻⁴⁵ | **FAILS** | **FAILS** |

**At the precision TAUFLAT actually publishes, the value TAUFLAT quoted passes.** EPS1_SWEEP §4.5's
finding — *"the clause FAILS at the quoted value, by 8.21·10⁻⁷ decades of energy"* — exists only at
twelve significant figures of a constant published at six. Pre-registered verdict **NO-DISCRIMINATION**,
with the designed-FAIL control (9.3850·10⁻⁴⁵) correctly returning **UNSAFE-SIDE**. **HAS-POWER.**

### §4.3 **FAIL 2 — EPS1_SWEEP's own replacement value is above its own bound.** [POST-HOC, EE1-P2]

At EPS1_SWEEP's own twelve-digit η_♭, the exact bound is

> √(η_♭/4) = **9.384951126377803359263720·10⁻⁴⁵** (exact integer `isqrt`, no float decides anything)

and EPS1_SWEEP §4.5's recommended **9.38495112638·10⁻⁴⁵ sits 2.3406·10⁻¹³ ABOVE it** — one unit in the
twelfth significant figure. The largest admissible decimal at twelve figures is **9.38495112637·10⁻⁴⁵**.

> **This is the same defect EPS1_SWEEP §4.5 is about, reproduced by its own repair.** A ceiling that is
> a square root of a rational has no exact decimal; **it must be truncated DOWN, and both quoted values
> were rounded to nearest.** §4.5's closing sentence — *"a ceiling quoted above its own bound is exactly
> the defect TAUFLAT's own §6.6 is about"* — applies to §4.5.

### §4.4 **FAIL 3, and it is the one that matters — the value is an evaluation at a free parameter.** [ee1-2(b): VALUE-PARAMETRIC]

Because ε_1^cut = t_pr/(142125√C_3) with t_pr = 1/(3.31·10⁷·C_D²), and **C_D ≈ (0.5-0.9)·10³·C_T**
(S4-16, quoted at TAUFLAT.md l.182), the value obeys

> ### **ε_1^cut ∝ C_D⁻² ∝ C_T⁻² ∝ C_3^{−1/2}.**

TAUFLAT l.182-183 is explicit that **C_D is an output, not a parameter**: *"S4-16 … is the item that
turns C_D into an output: 'C_D ≈ (0.5-0.9)·10³·C_T' (l.374), after which C_T ≈ 5.288·10¹² (EPSSTAR §7.1)
gives C_D ≈ 4.76·10¹⁵."* And **C_T is a function of the free exponent q**, chosen at **q = 12** by
EPSSTAR §7.1 **for a different question** (whether C_T clears 10¹³ for the (CLS-min) → RLARGE interface).
Evaluating the value over EPSSTAR's own q-row (EPSSTAR.md l.547-553), at the conservative 0.9 end of the
C_D band that TAUFLAT itself used:

| q | C_T (EPSSTAR l.547-553) | C_D = 0.9·10³C_T | ε_1^cut | decades vs q = 12 |
|---|---|---|---|---|
| 10 | 2.463·10¹³ | 2.2167·10¹⁶ | 4.326·10⁻⁴⁶ | **−1.336** |
| 11 (= q_min, EPSSTAR l.555) | 9.774·10¹² | 8.7966·10¹⁵ | 2.747·10⁻⁴⁵ | −0.534 |
| **12 (EPSSTAR's choice)** | **5.288·10¹²** | **4.7592·10¹⁵** | **9.385·10⁻⁴⁵** | **0.000** |
| 16 | 2.031·10¹² | 1.8279·10¹⁵ | 6.362·10⁻⁴⁴ | +0.831 |
| 24 | 1.528·10¹² | 1.3752·10¹⁵ | 1.124·10⁻⁴³ | +1.078 |
| 32 | 1.454·10¹² | 1.3086·10¹⁵ | 1.241·10⁻⁴³ | +1.122 |
| 100 (plateau) | 1.396·10¹² | 1.2564·10¹⁵ | 1.347·10⁻⁴³ | **+1.157** |
| **q = 8** (HANDOFF item 4) | ≥ 1.27·10¹⁴ | 1.1430·10¹⁷ | 1.627·10⁻⁴⁷ | **−2.761** |
| **without (H2)** (EPSSTAR l.590) | 8.05·10¹⁵ | 7.2450·10¹⁸ | 4.050·10⁻⁵¹ | **−6.365** |

**Spread over EPSSTAR's own q-row: 2.493 decades. Over the admissible range q ≥ 11: 1.690 decades.**
Pre-registered threshold for VALUE-PARAMETRIC was 0.30 decades — chosen because EPS1_SWEEP §1.1 dismissed
a ×1.90 (0.28-decade) spread in ε_1 as immaterial, so a spread at that scale is material by its own
standard. **Designed-FAIL control** (a constant C_T row) returns **VALUE-PINNED**, spread exactly 0.
**HAS-POWER.**

**And the lane is actively moving q.** HANDOFF critical-path item 4: *"at q = 8, C_T ≥ 1.27·10¹⁴, provably
over the 10¹³ the (CLS-min) → RLARGE interface needs; **at q ≈ 30 it is under**, with compatibility
checked clause by clause"*, and *"**q = 8 is the worst admissible choice**"*. So the parameter this value
silently inherits is one the project is in the middle of choosing, and the preferred direction (larger q)
makes the required lowering **1.1 decades smaller**, not larger.

**Reproduction gate.** Rebuilding the value from the C_T chain rather than from EPS1_SWEEP's summary line
gives 9.384986·10⁻⁴⁵ against its 9.384951·10⁻⁴⁵, ratio 1.000004 — the chain reproduces, and the 7th
significant figure already disagrees with itself depending on whether C_D is taken as 4.76·10¹⁵ (TAUFLAT's
rounding) or 4.7592·10¹⁵ (0.9·10³ × 5.288·10¹²).

### §4.5 A by-product: TAUFLAT §4 A's "0.080 decades of room" is itself evaluated at fixed q

TAUFLAT.md l.375-378 kills option A with *"C_T has only **0.080 decades of room** above that floor
[C_T ≥ 4.4·10¹²] … those buy only 0.160 decades of C_err against the 4.854 needed."* The floor 4.4·10¹²
is EPSSTAR l.608's, stated *"at q = 12"*. EPSSTAR's own table has C_T = 1.454·10¹² at q = 32 and
1.396·10¹² at q = 100 — **below that floor**, because the floor falls with q too (the source term
½(A_sγ_s)^a with a = q/(q−4) is 73.8 % of Ĉ at q = 12, EPSSTAR §7.2, and collapses as a → 1).

Over q, the room is **0.578 decades of C_T = 1.156 decades of C_err**, not 0.160 — **×7.2 more than
recorded**. **Option A stays dead** (1.156 bought against 4.854 needed), so no conclusion of TAUFLAT §4
changes. But it is the same defect shape one more time, and it is the reason the two levers are coupled:
spending the q lever on C_err reduces what the ε_1 lever must deliver, decade for decade.

### §4.6 Verdict, and the value I propose instead

**(C4) NOT DISCHARGED as written.** It is not a rounding fix. Executing it verbatim — writing
`ε_1 ≤ 9.38495·10⁻⁴⁵` into RLARGE — would write **twelve significant figures of a quantity whose input
band is a factor 3.24 wide from C_D's `(0.5-0.9)` alone and whose free parameter moves it 1.7 decades**,
and would do it with a value that is above its own bound at the precision it is quoted to. That is a new
instance of the defect class this whole chain of work exists to repair.

**What I execute instead**, and it is executable rather than a request for another decision:

> **ε_1^cut ≤ t_pr/(142125·√C_3), with t_pr = θ_0^SUP = 1/(3.31·10⁷·C_D²) — and, at the constants in
> force (C_D = 4.76·10¹⁵ from C_T(q = 12) = 5.288·10¹² under (H2); C_3 = 1), ε_1^cut ≤ 9.38·10⁻⁴⁵.**

**Why three significant figures and why that one.** 9.38·10⁻⁴⁵ is admissible at **every** precision at
which η_♭ is published — the 3-s.f., the 6-s.f. and the 12-s.f. bounds are 9.38083·10⁻⁴⁵,
9.38496·10⁻⁴⁵ and 9.38495·10⁻⁴⁵, and 9.38·10⁻⁴⁵ is below all three. Neither quoted value is. It is
4.854 decades below the ceiling in force, so every price in §5 is unchanged. And the parametric form is
carried beside it, so that when C_D moves the number is visibly stale rather than silently wrong —
**the instruction TAUFLAT.md l.566-567 already issued for η_♭ itself**: *"state η_♭ as a **function of
C_D** … and **never as a number**"*.

---

## §5. (C5) The two steeper exponents. **DISCHARGED.**

Status: **COMPUTED (exact)**, `checks/ee1_out.txt` ee1-3, **PRICES-AGREE**, designed-FAIL control
separates by 9.71 decades. **HAS-POWER.**

### §5.1 Re-derived from RLARGE's own definitions, not from the summary lines

Each step read in the owning file; N = 2, L = 3, d = 4, A_d(3) = 9 (fixed by RLARGE.md l.1009's
`η_1 = min{ε_1/18, ε_1²/(4608N)}`).

1. **η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d(L))}** — **RLARGE.md l.64**, repeated inside Lemma RS at
   l.976. The **quadratic** entry is active iff ε_1 < 512NA_d/(2L²) = 512 (N = 2), hence at every
   admissible ε_1.
2. **a_η = η_1²/(2N)** — **RLARGE.md l.1026** (*"a_η taken at its bare-level value η_1²/(2N)"*); the same
   number as l.1248's `η_1²/4`, which is written at N = 2. So **a_η ∝ ε_1⁴**.
3. **a_RS := min{a_η, κε_1²/(256N)}** — **RLARGE.md l.1020**. The a_η entry binds (at ε_1 = 6.7·10⁻⁴⁰:
   5.93·10⁻¹⁶⁶ against κε_1²/512 = 8.77·10⁻⁸²); the ε² entry would need ε_1 > 814.

| quantity | at 6.7·10⁻⁴⁰ | at the proposed ε_1 | decades | = k × Δ |
|---|---|---|---|---|
| **a_RS, RLARGE's quadratic η_1 (∝ ε_1⁴)** | 5.93136·10⁻¹⁶⁶ | 2.28341·10⁻¹⁸⁵ | **19.4146** | 4 × 4.8536 |
| **a_RS, KN-step's linear η_1 (∝ ε_1²)** | 8.19819·10⁻⁸⁴ | 1.60854·10⁻⁹³ | **9.7073** | 2 × 4.8536 |
| **Cauchy C³ on 𝔇_{α_E} (∝ ε_1⁻³)** | — | — | **14.5609** | 3 × 4.8536 |

with **Δ := log₁₀(6.7·10⁻⁴⁰ / 9.38495112638·10⁻⁴⁵) = 4.853643 decades**. Each price was computed twice —
once as k·Δ, once by evaluating the owning file's formula at both ε_1 — and the two routes agree to
**8·10⁻⁴⁸ decades**. All three reproduce EPS1_SWEEP §4.2's 19.415 / 9.707 / 14.561 to ±0.01.

**Cross-file transcription gate**: the absolute values 5.931360·10⁻¹⁶⁶ and 2.283406·10⁻¹⁸⁵ reproduce
**ARS_FIX §2.2**'s table (5.93136·10⁻¹⁶⁶, 2.28341·10⁻¹⁸⁵) — a different file, a different author, a
different question.

**Designed-FAIL control, as §0.5 and defect 3 require.** Asserting the price at exponent 2 **against the
quadratic branch** returns **PRICES-DISAGREE**, missing by 9.7073 decades. A check that passed under the
wrong exponent could not tell the two (C2) outcomes apart and would be worthless for the job it is run
for. **The control failed, as required.**

### §5.2 The ε_1⁻³ item stays ARGUED, and the citation is off by two lines

**HIST.md l.857**: *"α_E ≥ c·ε_1 (a g-INDEPENDENT radius: the whole ε_1-domain)"*, with **SF.md l.870**'s
`s_5 ≤ min{ε_1/5, 0.01}` and **RLARGE.md l.455**'s `α_E ≤ s_5/4` pinning **α_E ≍ ε_1** from both sides.
The Cauchy statement is at **HIST.md l.864** — *"C³ bounds in the data follow by Cauchy on 𝔇_α"* —
**not l.862**, which EPS1_SWEEP cites; l.862 is *"E_0 is bounded but NOT small"*. HIST writes neither the
constant nor the exponent, so the α_E⁻³ is the standard Cauchy estimate supplied from outside the file.
**Status: ARGUED**, and the patch text says so rather than pricing it as established.

### §5.3 The clause that changes under (C2), named

**(C2) is another worker's and I have not duplicated it.** My patch is written to be correct under both
outcomes, and **exactly one clause changes**:

> **If the KN-step adoption lands** (η_1 := c_1ε_1, c_1 = 1/(2(L² + 5.5A_d)) = 1/117, EXISTENCE.md
> l.1771): a_RS ∝ ε_1², the price is **9.707 decades**, a_RS falls 8.19819·10⁻⁸⁴ → 1.60854·10⁻⁹³, and the
> RS/joint ceiling a_RS/10² sits **+56.82 decades above DX′** at the proposed ε_1.
> **If it does not**: a_RS ∝ ε_1⁴, the price is **19.415 decades**, a_RS falls 5.93136·10⁻¹⁶⁶ →
> 2.28341·10⁻¹⁸⁵, and the ceiling sits **−35.03 decades below DX′** — a breach that exists today at
> −15.62 and that option C deepens but does not create.

Everything else in the patch — the scope sentence, the floor record, the value, the Cauchy item, the
conditionality — is identical under both. **One further caveat I take from ARS_FIX §2.2 and do not
smooth over:** RLARGE.md l.1021-1024 prices n bad cubes as `(Ce^{−a_RS/g_k²})^{n/c_RS}` with
**c_RS = 5⁴ = 625**, so the exponent carried per cube is a_RS/c_RS and the honest margin is between the
/10² and the /(c_RS·10²) columns — **up to 2.80 decades worse** than the figures above, with the same
sign in both.

---

## §6. (C7) The conditionality. **DISCHARGED WITH NOTE — the list is incomplete.**

### §6.1 The two named conditions, verified

- **c_+·C_Ω ≲ 1.5·10⁴⁶.** From EPS1_SWEEP §4.4: the margins are exhausted at c_+·C_Ω = 1.54·10⁴⁶
  (g²_CRC at the ×82 ring) at the proposed ε_1, against 7.87·10⁵⁵ today.
  *Two citation corrections, and the first is not cosmetic.* **(C7) cites "g²_CRC at the ×82 ring (HW
  l.2006)". HW.md l.2006 is the ×17 row** (`17 | 1115603075 | … | 8.96376·10⁻⁹⁶`); **the ×82 row is
  l.2007** (`82 | 5381106005 | … | 1.85835·10⁻⁹⁶`). The number quoted is the ×82 one, so the arithmetic
  is right and only the pointer is off by one — but ×17-vs-×82 is precisely the cross-lane disagreement
  HANDOFF item 1 settled, with the standing lesson *"a proof of the wrong statement is not better
  support"*, so a reference pointing at the wrong column is worth fixing before someone re-reads it.
  **Second: (C7) cites "PLD l.1902" for "c_A uncertified". PLD.md l.1902 names c_lcr**, not c_A
  (*"**c_lcr:** not certified … the Gaussian value (1 − λ_f)^{−dof/2} per column remains the ARGUED
  heuristic"*). c_A appears in c_+ at **PLD.md l.3072** (*"c_+ = c_A + 82c_U"*). The substance — there is
  an uncertified hand constant in c_+'s chain — stands; the symbol does not.
- **DX′ remaining the binding programme ceiling**, and **C_Ω an uncertified hand constant**:
  **REVIEW_SF_S7.md l.225**, *"**C_Ω** (DX′; C + 3(N² − 1)/2 from SLC-sh): enters linearly. It is an
  explicit hand constant, not a certificate."* Confirmed verbatim.

### §6.2 Four conditions (C7) does not name, all of which the value depends on

From §4.4, and each is an input the value is **quantitatively** a function of:

| omitted input | status, by file:line | effect on ε_1^cut |
|---|---|---|
| **C_3** | **(a3-q) is [OPEN; lane D; classical]**, HIST.md l.1669. Set to the reference C_3 = 1 (TAUFLAT l.211). EPSSTAR l.596 lists C_3 among *"I have not re-derived"* | ∝ C_3^{−1/2} |
| **(H2)** | *"C_T(q = 12) = 5.288·10¹² is **CONDITIONAL on (H2)**… **SQ.md does not say them today**, and without them C_T = 8.05·10¹⁵"*, EPSSTAR.md l.587-590 | **−6.365 decades** if (H2) is not adopted |
| **q** | free; fixed at 12 by EPSSTAR §7.1 for the C_T ≤ 10¹³ question; HANDOFF item 4 is actively choosing it | **+1.157 to −2.761 decades** across the range |
| **(H1)/(H3)** | *"conditional on … STAR_CONST.md's and CONST_T.md's own arithmetic — and **HANDOFF.md lists both as UNREVIEWED**"*, EPSSTAR.md l.591-592 | unquantified |

**Verdict: (C7) DISCHARGED WITH NOTE.** The conditionality is stated in the patch text and not pretended
away, but it is stated **longer than (C7) asks**, because (C7)'s own list covers only the coupling-ceiling
half. The half it omits is the half that fixes the number being written.

---

## §7. C2-F1: the lead's reading D4 is **broken**, and here is exactly where

> ### **Lead decision D4 says (C2) is the binding condition and "the ε_1 move carries only bookkeeping". That is wrong for (C4), and mildly wrong for (C3). Failure mode C2-F1 has fired.**

Said loudly, per the scope prompt and per D6.

1. **(C4) is not bookkeeping.** It is presented as a rounding fix in the 7th significant figure. It is
   in fact a demand to write a number that (i) has no content at the precision its own source publishes
   (§4.2), (ii) is above its own bound at the precision it is quoted to, exactly as the value it
   replaces was (§4.3), and (iii) is an evaluation at a **free parameter the project is in the middle of
   choosing**, moving 1.7 decades over the admissible range and 6.4 more if (H2) is not adopted (§4.4).
   Executing it as written plants a false-precision constant of the same class as the ones this campaign
   exists to remove.
2. **(C3) carries a sign error.** Its third clause instructs that PLD's 2m_*g/ε_1 "loses 4.854 decades".
   It gains them (§3.3, two designed-FAIL controls). Writing (C3) as given would put a false sentence
   into the file that owns the quantity.
3. **(C6) is bookkeeping after all, but only because the answer came out determinate.** Both axes
   resolved to one cell, so T55-B proceeded. Had either been unresolved, (C6) alone would have stopped
   the target — which is what makes it a prerequisite rather than a formality, exactly as the scope
   prompt said.

**What this reorders.** (C2) remains the largest item by decades (92, per ARS_FIX). But the ε_1 move is
**not** a bookkeeping tail that can be landed behind it: the number to be written is coupled to the q
choice of HANDOFF critical-path item 4, and the two levers trade against each other decade for decade
(§4.5). Landing the ε_1 edit as a bare decimal **before** q is fixed writes a constant that the next
session's own preferred move invalidates.

**Smaller corrections to records, for completeness:** EPS1_SWEEP's (C7) misnames a symbol (c_A for
c_lcr) and points at the ×17 row for the ×82 figure (§6.1); its Cauchy citation is two lines off
(§5.2); and the scope prompt's "five ε_1 not four" conflates a symbol count with a value count (§1.5).
None of these changes a conclusion. All four are instances of the one pattern.

---

## §8. Checks, controls, power, and the one FAIL

Files written by me: **this file**, `checks/ee1_criteria.md`, `checks/ee1_exec.py`, `checks/ee1_out.txt`,
`checks/ee1_run1_abort_out.txt`, `checks/ee1_run1_abort_err.txt`, `checks/ee1b_exec.py`,
`checks/ee1b_out.txt`, `checks/ee1c_bound.py`, `checks/ee1c_out.txt`,
`checks/ee1c_run1_display_out.txt`. **Nothing else, anywhere. No git command was run by me.**

| id | pre-registered verdict | result | designed-FAIL control | power |
|---|---|---|---|---|
| **ee1-1** | FACTORISES / DOES-NOT-FACTORISE | **FAIL — DOES-NOT-FACTORISE** (my own transcription error; see below) | also failed, same common cause | **power NOT established on this run** |
| **ee1b-1** (re-run, new id, criteria untouched) | as above | **FACTORISES**, worst cell ×1.0021 | **DOES-NOT-FACTORISE** at ×1.4109 | **HAS-POWER** |
| **ee1-2(a)** | SAFE-SIDE / UNSAFE-SIDE / NO-DISCRIMINATION | **NO-DISCRIMINATION** | **UNSAFE-SIDE** as required | **HAS-POWER** |
| **ee1-2(b)** | VALUE-PINNED / VALUE-PARAMETRIC | **VALUE-PARAMETRIC**, spread 2.493 decades | **VALUE-PINNED**, spread 0 | **HAS-POWER** |
| **ee1-3** | PRICES-AGREE / PRICES-DISAGREE | **PRICES-AGREE** to 8·10⁻⁴⁸ decades | **PRICES-DISAGREE** by 9.7073 decades | **HAS-POWER** |
| **ee1-4** | RATIO-RISES / RATIO-FALLS | **RATIO-RISES**, +4.8536 decades | **INVARIANT** at the ε-driven ceiling; **RATIO-FALLS** on reversed input | **HAS-POWER** |
| precision | STABLE / UNSTABLE | **PRECISION-STABLE** (50 and 100 digits) | — | — |

### §8.1 The FAIL, reported as a FAIL

`ee1_exec.py`'s ee1-1 returned **DOES-NOT-FACTORISE**. The cause was a transcription error **in my own
script**: `E_OLD_PRE` was written `F(12687,10)*1e-39` = 1.2687·10⁻³⁶, a factor 10³ too large. The
signature is visible in the output — the three failing ratios are 1000.2, 999.5 and 1002.1.
`ee1_out.txt` is kept **unaltered**, the FAIL stands as reported, and the re-run took a **new id**
(`ee1b_exec.py`) with `ee1_criteria.md` untouched.

**A second, smaller disclosure that the first run's own power claim was unsupported.** Its designed-FAIL
control also returned DOES-NOT-FACTORISE, so the script printed "HAS-POWER" — but both verdicts came
from the **same** common cause, so main and control did not separate and the claim was not evidence.
This is precisely the session-24 lens (*could this check have failed?*) turned on my own gate, and the
answer on that run was: it could only have failed. The power verdict is established in `ee1b` instead,
where main returns FACTORISES and control DOES-NOT-FACTORISE.

**Two further disclosures.** (i) `ee1_exec.py` aborted once on a syntax error before producing any
verdict; both logs are kept (`ee1_run1_abort_*.txt`) and neither produced a number used anywhere.
(ii) `ee1c_bound.py`'s first run printed the floor digits through a `Decimal` format that **rounds to
nearest**, so it displayed the 12-digit floor as `…638` and appeared to contradict the table two blocks
above it. The display was repaired to print the truncated integer literally; **the arithmetic and the
pre-registered question were not touched**, and the first output is kept as
`ee1c_run1_display_out.txt`. The repaired run's digit-count labels are off by one (the row labelled
"11 s.f." carries the 12-figure floor 9.38495112637·10⁻⁴⁵); the digit strings themselves are correct and
are what §4.3 quotes. Noting a display defect inside the probe whose subject is a display defect is not
lost on me.

### §8.2 Power grading, honestly

- **ee1-4 is the strongest.** It flips, it has two controls of opposite kinds, and one of them
  (INVARIANT at the ε-driven ceiling) is a *known answer fixed by the lane's own structural fact*, not
  by me. It overturned a banked finding.
- **ee1-2(b) is strong**: the q-row it is tested against is EPSSTAR's, written to answer the C_T ≤ 10¹³
  question, not this one, and the control pins the gate at zero spread.
- **ee1-3 is strong on transcription and medium on modelling**: it reproduces a second author's
  absolute numbers in a different file, and its control separates by 9.7 decades — but it cannot
  validate RLARGE's definition of a_η.
- **ee1-1/ee1b-1 is medium**: it compares transcriptions, so it catches a factored structure and a wrong
  factor, but it cannot validate SF's derivation of either factor, and it does **not** decide which cell
  is in force — that was decided by reading RLARGE l.70 and REVIEW_SF_S7's "TB-1 (binding)", not by
  arithmetic.
- **ee1-2(a) is medium and did its job by returning the negative verdict** it was given the option to
  return.

### §8.3 What these checks cannot catch, stated rather than left implied

They cannot validate SQ's derivation of η_♭, S4-16's C_err model or its `(0.5-0.9)·10³` band, EPSSTAR's
C_T harness, STAR_CONST's or CONST_T's arithmetic, HIST's C_3, RLARGE's ceiling chain, SF's DX′
evaluation, PLD's (SG) hypotheses, or any of C_Δ, C_♭, r_♭, C_Ω, c_+, c_A, N′. **A number reproduced here
is not an endorsement of its source.** They cannot find an ε_1 consumer that does not name ε_1, and the
consumer enumeration is EPS1_SWEEP's, not re-done here. And the ε_1⁻³ Cauchy item remains **ARGUED**:
HIST.md l.864 states the method and not the constant.

### §8.4 Numerics

Exact `fractions.Fraction` throughout; exact integer `isqrt` for every square root; `Decimal` at 50 and
100 digits for display and for the precision control only. Plain `python3 -I`, single thread,
`OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1`, `nice 10`, no numpy, no BLAS. Three runs, well
under a second each. **No numeric lock taken and none needed** (brief rule 6).

---

## §9. FOR OTHER FILES (not edited)

I wrote only this file and `checks/ee1_*`, `checks/ee1b_*`, `checks/ee1c_*`. I did not touch RLARGE.md,
SF.md, HIST.md, PLD.md, NORMS.md, SQ.md, HW.md, TAUFLAT.md, EPSSTAR.md, EPS1_SWEEP.md, ARS_FIX.md,
BFT_*.md, FLOW.md, PROOF.md, HANDOFF.md, SESSION24_RESULTS.md, EXISTENCE.md or any REVIEW_* file.

**Everything below is literal append-ready text for the lead to land.** Each block is to be appended
to the named file. **Blocks P1-P7 are the executed change.** Block P2 is the only one with a variant,
and the variant depends on (C2), which is another worker's; both forms are given and the lead takes one.

**One standing caveat that belongs on the whole patch and is repeated inside each block that needs it:**
this change moves one threshold and repairs the records that quote it. **It adds no mathematics and
proves nothing about the construction.** Every status in every file is unchanged by it.

---

### P1 — RLARGE.md, §0 Thresholds (append after the "Current ε_1 ceiling" entry, l.70-72)

```
  - **ε_1^cut lowered for DESC-ε (iii) [EPS1_EXEC, T55-B; executes TAUFLAT §4 option C under
    EPS1_SWEEP §5's conditions (C1)-(C7)].**
    **Scope.** The threshold lowered here is ε_1^cut, the small-field plaquette cut of §0 — the ε_1 of
    χ_Q := Π_{p⊂int Q}1{||1 - U(p)||_op < ε_1} at l.58, bounded above by the five-entry min at l.70-72.
    It is **NOT** BFT_B's Theorem N2 threshold (BFT_B l.3058, the radius of the class 𝒦(ε_1) at l.2865,
    l.2870), which is defined by an explicit formula in O(1) geometric constants and **must not be
    moved** (lowering it would propagate through 𝒞_glob(ε) ⊂ 𝒦(4ε + Cε²), BFT_B l.2866, a cascade
    nobody has priced); and it is **NOT** FLOW's disc radius (FLOW l.1927) or its root-flux bound
    (FLOW l.2834). Nothing in BFT_B or FLOW changes.
    **The value in force before this edit is ε_1 ≤ 6.7·10⁻⁴⁰** (l.72, l.612) — REVIEW_SF_S7 l.196's
    base 1.2687·10⁻³⁹ carried through the **binding** TB-1 fix (×0.7056, REVIEW_SF_S7 l.199-200, l.297)
    and the **adopted rerun class** (×0.75, REVIEW_SF_S7 l.251; the class declared at l.70). l.71's
    9.52·10⁻⁴⁰ is the same entry pre-TB-1; l.611's 8.95·10⁻⁴⁰ is old-class; SF l.2837 / NORMS l.746's
    1.27·10⁻³⁹ is stale on **both** axes.
    **The new ceiling, parametrically — this is the form that is correct, and the number below is only
    its current evaluation:**
      **ε_1^cut ≤ t_pr/(142125·√C_3),  t_pr = θ_0^SUP = 1/(3.31·10⁷·C_D²)**
    (TAUFLAT l.371-372, l.205), from DESC-ε (iii)'s gate E < η_♭ met by HIST l.1698's E ≤ 4C_3ε_1².
    Equivalently ε_1^cut ≤ √(η_♭/(4C_3)) with η_♭ = 1/(5.04991·10⁹·(3.31·10⁷C_D²)²).
    **At the constants in force** (C_D = 4.76·10¹⁵ from C_T(q = 12) = 5.288·10¹² under (H2), EPSSTAR
    §7.1; C_3 = 1, the reference value, (a3-q) being OPEN at HIST l.1669):
      **ε_1^cut ≤ 9.38·10⁻⁴⁵,  i.e. 4.854 decades below 6.7·10⁻⁴⁰.**
    **Three significant figures, truncated down, deliberately.** ε_1^cut is a square root of a rational
    and has no exact decimal; a ceiling must be truncated DOWN. 9.38·10⁻⁴⁵ is admissible at **every**
    precision at which η_♭ is published (bounds 9.38083·10⁻⁴⁵ at TAUFLAT l.561's 3 s.f.,
    9.38496·10⁻⁴⁵ at l.196/l.213's 6 s.f., 9.384951126377803·10⁻⁴⁵ at EPS1_SWEEP §4.5's 12 s.f.).
    **Do not write more figures.** TAUFLAT l.408's 9.38496·10⁻⁴⁵ and EPS1_SWEEP §4.5's
    9.38495112638·10⁻⁴⁵ are each **above** their own bound at the precision they are quoted to (by
    9.4552·10⁻⁷ and 2.3406·10⁻¹³ relative); the largest admissible 12-figure decimal is
    9.38495112637·10⁻⁴⁵. Carry the parametric form, per TAUFLAT l.566-567's standing instruction for
    η_♭ itself: *state it as a function of C_D and never as a number.*
    **CONDITIONAL, and on more than the coupling ceiling.** ε_1^cut ∝ C_D⁻² ∝ C_T⁻² ∝ C_3^{−1/2}, and
    C_D is an **output**, not a parameter (S4-16 via TAUFLAT l.182). So the number above is conditional
    on: **(i)** C_3 = 1, with (a3-q) OPEN (HIST l.1669); **(ii)** **(H2)**, which SQ.md does not state
    today — without it C_T = 8.05·10¹⁵ and the ceiling is **6.365 decades lower**, 4.05·10⁻⁵¹
    (EPSSTAR l.587-590); **(iii)** **q = 12**, a free exponent fixed by EPSSTAR §7.1 for a different
    question — over EPSSTAR's own q-row the ceiling moves **+1.157 decades** (q at the plateau) to
    **−2.761** (q = 8, HANDOFF item 4's worst admissible choice), a spread of 1.690 decades over the
    admissible q ≥ 11; **(iv)** (H1)/(H3), i.e. STAR_CONST.md's and CONST_T.md's arithmetic, both
    listed UNREVIEWED; **(v)** c_+·C_Ω ≲ 1.5·10⁴⁶ and DX′ remaining the binding programme ceiling, both
    uncertified hand constants (REVIEW_SF_S7 l.225; PLD l.3072's c_+ = c_A + 82c_U with c_lcr not
    certified at PLD l.1902). **If q moves, this number moves quadratically with C_T. Re-evaluate it;
    do not carry it.**
    **Price, in this file's own currency** [EPS1_EXEC §3, §5; exact]: a_bad = c_prε_1² and every
    ∝ ε_1² quantity fall **9.707 decades** (a_bad 2.497·10⁻⁸⁵ → 4.899·10⁻⁹⁵; a = θa_bad ≲ 2.04·10⁻⁹⁶);
    n_* and n_H rise 9.707 (n_H ≈ 2.07·10⁸⁷ → 1.05·10⁹⁷); wrap levels 183.6 → 204.0; the torus-caveat
    count 42.2 → 47.3. **g_K² ≲ a/10² falls 1.040·10⁻⁸⁸ → 2.041·10⁻⁹⁸, which keeps 53.92 decades over
    DX′ (63.63 before).** The large-field region grows: the suppression exponent ε_1²/(4Ng²) is
    **exactly invariant** at the ε-driven coupling ceiling and keeps 60.06 decades of margin at the
    ε-independent one. **Nothing changes in kind, and this edit adds no mathematics.**
    **The floor, which this file did not record and now does: it is ε_1 ≫ g, not "none."** See P4.
```

### P2 — RLARGE.md, §5.4 coupling ceilings (append after l.618) — **TWO FORMS; take one**

**Form P2-α — if the KN-step adoption (C2) does NOT land (η_1 stays quadratic, a_RS ∝ ε_1⁴):**

```
- **[EPS1_EXEC, T55-B / ARS_FIX] l.618's "RLF's own ceilings do not bind at the current constants" is
  scoped, and the scope matters.** It is true for the exponent l.617 names (a = θa_bad: margin 63.63
  decades over DX′ before this edit, 53.92 after). It is **false for a_RS.** Because η_1 (l.64) is
  quadratic in ε_1 at every admissible ε_1 (the quadratic entry is active for ε_1 < 512 at N = 2) and
  a_η = η_1²/(2N) (l.1026), **a_RS (l.1020) is ∝ ε_1⁴**, so a_RS/10² = 5.93136·10⁻¹⁶⁸ sits **15.62
  decades BELOW** DX′ = 2.456·10⁻¹⁵²/C_Ω **already today**, and **35.03 decades below** after this
  edit. Lowering ε_1 does not create this breach; it **inherits it and deepens it by 19.415 decades**
  (= 4 × 4.854). Honest margin: between −15.62 and −18.41 decades today, since l.1021-1024 carries
  a_RS/c_RS with c_RS = 5⁴ per cube, not a_RS. **Scope l.618 to the (REG-min)/HW route, as l.617
  already does.**
```

**Form P2-β — if the KN-step adoption (C2) DOES land (η_1 := c_1ε_1, a_RS ∝ ε_1²):**

```
- **[EPS1_EXEC, T55-B] With KN-step's linear η_1 adopted (η_1 := c_1ε_1, c_1 = 1/(2(L² + 5.5A_d)) =
  1/117, EXISTENCE l.1771), a_RS is ∝ ε_1² like every other exponent in this file**, and this edit
  costs it **9.707 decades**, not 19.415: a_RS 8.19819·10⁻⁸⁴ → 1.60854·10⁻⁹³, with the ceiling
  a_RS/10² sitting **+56.82 decades above** DX′ at the new ε_1 (66.52 before). l.618's sentence is then
  true for a_RS as well, and may stand. Note that l.1021-1024's c_RS = 5⁴ per-cube divisor costs a
  further up-to-2.80 decades on any a_RS margin quoted at the bare /10².
```

### P3 — SF.md §22.7 (append after l.2840) — **this executes a binding fix that is already outstanding**

```
**[EPS1_EXEC, T55-B; executes REVIEW_SF_S7 E-2 item 2 (TB-1), outstanding.]** The ε_1-driven rows at
l.2837-2840 are **pre-TB-1 and old-class**, and REVIEW_SF_S7 l.298 ordered them rescaled. Corrected:
- ε_1 = 1.27·10⁻³⁹ → **6.7·10⁻⁴⁰** (×0.75 for the rerun class, REVIEW_SF_S7 l.251; ×0.7056 for TB-1,
  l.199-200) — and then to **≤ 9.38·10⁻⁴⁵** under the DESC-ε (iii) edit of RLARGE §0 (P1).
- HW a_bad = 8.4·10⁻⁸⁵ → **2.50·10⁻⁸⁵** at 6.7·10⁻⁴⁰, and **4.90·10⁻⁹⁵** at the new cut.
- The §16.3 (l.2199-2206) and §19.4 (l.2578-2583) tables already carry the **ε_1^{−4}** row for the
  HIST n_♯ / RS route and already evaluate at ε_1 values 14-57 decades below this edit. They are the
  independent record that this move is not novel territory; please point RLARGE at them.
- l.2587's *"(GF-B^𝔥) drives only the τ_c rows … not ε_1"* is what makes this edit affordable **and**
  what makes its floor cost real: because DX′ is τ_c-driven, g does **not** fall with ε_1, so the
  window ratio ε_1/g loses the full 4.854 decades (36.63 → 31.78). It cuts both ways; one sentence.
```

### P4 — EXISTENCE.md (append near §13.4 / l.4191, the (RLF-3^dis) threshold)

```
**[EPS1_EXEC, T55-B] This lane holds the only floor on ε_1 in the project, and it is now 4.854 decades
tighter.** l.4191's *"ε only has to contain the typical field ≍ g"* and l.3112's coercivity window
*"at distance ≫ g but < ε_1"* are the statements that make **ε_1 ≫ g** a real constraint. The project's
standing record *"no lane found requires ε_1 ≥ (g-independent constant)"* (REVIEW_SF_S5 l.332, SF
l.2207) remains true as written and should be amended to: **"no lane needs ε_1 above a g-independent
constant; the window ε_1 ≫ g is the floor."**
Margin, at the binding DX′ coupling g ≤ 1.57·10⁻⁷⁶/√C_Ω (REVIEW_SF_S7 l.204), C_Ω = 1:
**log₁₀(ε_1/g) = 36.63 before the RLARGE §0 edit, 31.78 after.** FLOOR-RESPECTED. Larger C_Ω lowers g
and so **widens** the window, making 31.78 a lower bound in C_Ω ≥ 1.
The window is **exactly invariant** at the ε-driven coupling ceiling (every ε_1-derived coupling ceiling
in the lane is ∝ ε_1²); the 4.854 decades are lost only because DX′ is τ_c-driven and ε_1-independent
(SF l.2587).
**Two readings that do not break, checked rather than assumed:** (i) l.3112's clause is itself
**CONDITIONAL ⇐ (AE), OPEN**, so a narrower window makes an open item harder, not a proven one false;
(ii) RX11-fix 6's identification **ε := ε_1 moves with ε_1**, so the hypothesis remains (RLF-3^dis)
itself at the new threshold and not the strengthened (RLF-3^dis)_{ε<ε_1} of l.4198-4200 — the proof
lane must re-deliver the same parametric theorem at worse constants, which is what RLARGE §0's price
list does. l.3556's u_0 = 64/min{δ_3, ε_1}² rises 9.707 decades to 7.27·10⁸⁹ (g² ≤ 1.38·10⁻⁹⁰, not
binding). l.1692's non-triviality clause is **helped**: Haar{||W − 1|| > ε_1} → 1 as ε_1 falls.
```

### P5 — PLD.md §(SG) (append near l.995) — **note the corrected sign**

```
**[EPS1_EXEC, T55-B] Effect of the RLARGE §0 ε_1^cut edit on (SG^{net}) and (SG^{fl}): neutral to
helpful, and the direction is the opposite of the one EPS1_SWEEP §2.2/§2.3 recorded.**
- **l.995's 2m_*g/ε_1 RISES by 4.854 decades** at the ε_1-independent DX′ coupling (g/ε_1 goes
  2.343·10⁻³⁷ → 1.673·10⁻³²), and is **exactly invariant** at the ε-driven coupling ceiling. Since
  2m_*g/ε_1 is the amount by which the aligned variance **may exceed** σ_*²g², the admissible set of
  models **grows** and Finding 1's no-go at l.1003-1004 (*"no proof of (SG^{net})_k by Gaussian
  domination … can work for aligned (smooth) families"*) becomes **weaker**. EPS1_SWEEP §2.2's *"the
  ℓ¹ absorption margin is proportional to g/ε_1 and shrinks as ε_1 falls at fixed g"* and §2.3's row
  *"falls 4.854 decades … the one ratio with the unhelpful sign"* have the sign inverted; this file
  should not record that direction. [EPS1_EXEC §3.3, exact, with two designed-FAIL controls.]
- **What does narrow is the RANGE, not the margin.** l.984's (SG^{net})_k is asserted only for
  0 ≤ t ≤ ε_1/(σ_*²g_k²), and l.987's 𝒱^{sf}(A) is a cut-good neighbourhood at threshold ε_1. Both
  shrink by 4.854 decades at fixed g, so **the hypothesis gets weaker in both directions: easier to
  prove, less to give RLF-step.** Range and requirement are the same ε_1 and scale together, so this
  is expected to be neutral — **but nobody has checked that the consumer's needed t is ε_1-proportional
  in every use. One sentence from this file's owner would close it**, and Finding 1 (SG-F3) calls the
  ℓ¹ term load-bearing, so it is worth the sentence.
- **l.2307 / l.1888's coherent-chain depth** goes 41.4 → 46.5 and the constant 81^depth goes 10^78.9 →
  10^88.7; it is still annihilated by e^{−486·a·u_k}, because **a·u_k = 5.381·10⁹ is exactly invariant**
  under the scaling. **a_ret** falls 9.707 decades (2.005·10⁻⁹¹ → 3.934·10⁻¹⁰¹). a_A's two ε-driven
  entries scale identically, so the min does not change branch; C_A **improves**, its two ε_1-bearing
  exponentials falling to 1.
```

### P6 — HIST.md (append near l.857-864)

```
**[EPS1_EXEC, T55-B] Two consequences of the RLARGE §0 ε_1^cut edit, and one request.**
- **[GAP S2-2] (l.857-859) is unaffected.** l.857's α_E ≥ c·ε_1 with SF l.870's s_5 ≤ min{ε_1/5, 0.01}
  and RLARGE l.455's α_E ≤ s_5/4 pin **α_E ≍ ε_1**, so α_E/ε_1 is invariant and *"m > 4α_E/ε_1"* bites
  at the same polymer size. Recorded so it is not re-opened.
- **A5's size clause gains.** 4C_3ε_1² falls 9.707 decades, and AE-red's own margin of 63.00 decades
  gains all of it.
- **Request: write the Cauchy constant explicitly.** **l.864** (*"C³ bounds in the data follow by Cauchy
  on 𝔇_α"*; EPS1_SWEEP §2.3/§4.2 cite l.862, which is the "E_0 is bounded but NOT small" sentence) is
  the **only place in the lane with an ε_1⁻³**. With α_E ≍ ε_1 the standard Cauchy estimate gives a C³
  constant ∝ E_0/α_E³, i.e. **∝ ε_1⁻³, rising 14.561 decades (= 3 × 4.854)** under this edit. **This
  is ARGUED, not computed**: the file states the method and not the constant, so the exponent is
  supplied from outside. Please write it, or refute it.
```

### P7 — NORMS.md (append near l.744-752)

```
**[EPS1_EXEC, T55-B] l.746's ε_1 value is stale on two axes, and is inconsistent with the constants
named beside it in the same sentence.** l.746 quotes *"ε_1 = 1.27·10⁻³⁹ (SF.md l.2837)"* while
l.747-748 names the constants that set it as *"(𝔠_∞^♯ = 315.19, λ_min ≥ 3.17·10⁻³, ε_* =
2.476·10⁻¹³/C_Δ, r_♭ = 1/220)"* — those are the **rerun class**, whereas 1.27·10⁻³⁹ is the **old-class,
pre-TB-1** value. REVIEW_SF_S7 l.249-250's rule is that 𝔠, λ_min and ε_* must be adopted for the same
class. Corrected: at the rerun class with the binding TB-1 fix, **ε_1 = 6.7·10⁻⁴⁰** (RLARGE l.72), and
**≤ 9.38·10⁻⁴⁵** after the RLARGE §0 edit (P1). l.746's companion *"g²_CRC ≈ 4.9·10⁻⁹⁷/c_+"* is
session 5's and is likewise stale; the current closed-column figure is **1.85835·10⁻⁹⁶/c_+** at the ×82
ring (**HW l.2007** — note l.2006 is the ×17 row).
**This changes no conclusion of §N-k.** l.752's *"this result does not improve ε_1 or g_K². It restores
the legitimacy of their k-independence"* is a statement about the **existence** of a k-independent ε_1,
not about its value; the number appears only as an illustration. Citation fix only.
```

### P8 — for EPS1_SWEEP.md's author and for the lead (ledger items, not edits to the construction)

1. **(C4) is not a rounding fix and should not be landed as one.** §4.5's own replacement value
   9.38495112638·10⁻⁴⁵ is **2.34·10⁻¹³ above its own bound** — the same defect the item is about, since
   a square-root ceiling must be truncated down, not rounded to nearest. And at the **six** significant
   figures TAUFLAT publishes η_♭ to (l.196, l.213), **TAUFLAT's 9.38496·10⁻⁴⁵ passes the clause**, so
   §4.5's finding exists only at a precision no owning file supports. Use **9.38·10⁻⁴⁵** with the
   parametric form beside it.
2. **The value is an evaluation at q = 12.** ε_1^cut ∝ C_T⁻², C_T is EPSSTAR §7.1's function of a free
   exponent, and over EPSSTAR's own q-row the required cut moves **1.690 decades across q ≥ 11** and
   6.365 more without (H2). HANDOFF critical-path item 4 is actively choosing q, and the preferred
   direction (larger q) makes this edit **smaller**. The two levers trade decade for decade.
3. **§2.2/§2.3's sign on PLD l.995 is inverted** (EPS1_EXEC §3.3, two designed-FAIL controls).
   (C3) should be restated: the margin rises; what narrows is the asserted t-range at PLD l.984.
4. **TAUFLAT §4 A's "0.080 decades of room" in C_T is evaluated at fixed q = 12**, against a floor
   (C_T ≥ 4.4·10¹², EPSSTAR l.608) that is itself stated at q = 12 and falls with q. Over q the room is
   **0.578 decades of C_T = 1.156 of C_err**, ×7.2 more. **Option A stays dead** (1.156 against 4.854
   needed) — no conclusion changes — but the figure belongs in the ledger as one more stale minimum.
5. **Two citation repairs in (C7) and one in §2.3.** (C7)'s *"g²_CRC at the ×82 ring (HW l.2006)"*
   points at the **×17** row; the ×82 row is **l.2007**. (C7)'s *"PLD l.1902: c_A uncertified"* names
   **c_lcr** at that line, not c_A (c_A is at PLD l.3072). §2.3/§4.2's Cauchy citation is **HIST l.864**,
   not l.862.
6. **(C6)'s "four live values" was correct as written**, and so was §1's "five symbols": they count
   different things (four numerical values of symbol 1; five distinct symbols). ARS_FIX §1 is about
   **η_1**, not ε_1. No amendment needed; recorded because the two counts have already been conflated
   once.
7. **The four values are a 2 × 2 table that factorises exactly** (EPS1_EXEC §1.3): base 1.2687·10⁻³⁹
   × 0.75 (class) × 0.7056 (TB-1), worst cell ×1.0021. Of the three non-current cells, two are rows of
   RLARGE's own recomputation table and are **labelled as superseded**; only **SF l.2837 / NORMS l.746**
   is an uncorrected defect, and **REVIEW_SF_S7 E-2 item 2 already ordered it fixed**. Settling (C6) is
   therefore a two-line edit (P3, P7), not an investigation.

---

*(End of EPS1_EXEC.md. Files written by this worker: this file, `checks/ee1_criteria.md`,
`checks/ee1_exec.py`, `checks/ee1_out.txt`, `checks/ee1_run1_abort_out.txt`,
`checks/ee1_run1_abort_err.txt`, `checks/ee1b_exec.py`, `checks/ee1b_out.txt`,
`checks/ee1c_bound.py`, `checks/ee1c_out.txt`, `checks/ee1c_run1_display_out.txt`. Nothing else,
anywhere. No git command was run by me.)*
