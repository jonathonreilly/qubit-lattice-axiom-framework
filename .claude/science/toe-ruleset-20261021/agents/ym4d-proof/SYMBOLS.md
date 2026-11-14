# SYMBOLS — the canonical symbol table for the YM4D proof lane, with the rename plan

*Owner: the T55-C worker (session 25). This file is the lane's symbol authority. It does not edit any
other file: every rename it proposes is listed in `## FOR OTHER FILES (not edited)` for the lead to land.*

---

## §0. PRE-STATED (first edit of this file, 2026-10-28T21:05:35Z)

**This is the first edit of SYMBOLS.md and it contains STATEMENTS ONLY.** No derivation, no grep, no
classification and no numeric check of mine precedes it. It cites nothing produced in session 25. The
defect it is commissioned against was named in session 24 (RTARGET.md §53 item 1; SESSION24_RESULTS.md).

### §0.1 What I was asked to do

Build the canonical symbol table for the proof lane. For every glyph that denotes more than one
mathematical object: enumerate the distinct objects with a precise definition and the file:line where
each is **defined** (not merely used); list every **use** site by file:line and say which object it
means; propose one distinct canonical name per object and give the rename as a mechanical table
(file, line, old, new). Start from the four families session 24 named — **ε_\***, **θ_0**, **ε_1**,
**η_1** — then sweep for unnamed families among the thresholds, the small parameters, the coupling
symbols, and the constants that occur with and without subscripts.

### §0.2 What I will NOT do

1. I will not rename anything in anyone else's file. Rule 8 (single-writer ownership). I write only
   `SYMBOLS.md` and `checks/sy1_*`.
2. I will not invent vocabulary where the lane already has a name. Where a distinguishing superscript
   or subscript is already in use **somewhere** in the lane for an object, that is the canonical name I
   propose. New glyphs are a last resort and are flagged as such.
3. I will not treat a **bound variable** (a letter quantified inside one proof and never exported) as
   a collision needing a rename, unless its scope leaks — i.e. unless a statement outside the binding
   proof refers to it. I will say for each such case which it is.
4. I will not rename anything in a `*_snapshot.md` file, in a `REVIEW_*.md` file, or in `HIST.md`'s
   historical record. Snapshots are frozen history; reviews are dated audits of the text as it then
   stood. Renaming them would falsify the record. For these I propose **annotation**, not renaming.
5. I will not report a family as "consistent" on the strength of having looked at it. See §0.4.

### §0.3 Pre-registered targets

- **S1.** The four named families, each with: the object list, a definition citation per object, a
  complete use-site classification, and a rename table.
- **S2.** A sweep of the candidate glyphs `c_1, C_1, C_Ω, κ, θ_w, m, η, η_q, a_RS, a_η, τ_♭, ε_loc,
  ε_♭, t_pr` plus whatever the sweep turns up, each either declared a family (≥2 objects) or declared
  single-object with the evidence for that.
- **S3.** A `## LIVE DEFECTS (SYM-F1)` section: every place where two objects sharing a glyph have
  been **combined, compared, or substituted for each other** — an inequality between them, one supplied
  as the other's input, or a numerical figure computed with the wrong one. For each: the file:line, the
  value that is wrong, the value that is right, and what changes downstream.
- **S4.** A verdict on whether the rename is mechanical or needs a human decision, per family.

### §0.4 Pre-registered falsifiability: what an inconsistency would LOOK like, named per family BEFORE I look

Session-25 brief defect 3: *a symbol audit that reports "all uses consistent" without having been able
to detect an inconsistency is a check that cannot fail.* So I state, in advance and per family, the
observable that would make me report a collision, and the observable that would make me report a live
SYM-F1 defect. If a family's observables are absent I report the family as clean **and say which
observable I searched for**, so that "clean" is a finding and not a shrug.

**The collision observable (COLL).** Two occurrences of one glyph with defining right-hand sides that
are not equal as formulas, and no superscript/subscript or sectioning that separates them, where at
least one occurrence is quoted or consumed outside the file that defines it.

**The live-defect observables (SYM-F1), in increasing severity:**
- **(F1-a) CROSS-QUOTE.** File A states "B's X" and gives a formula or number that is not the formula
  or number B's X has at the cited line.
- **(F1-b) MIXED MIN/MAX.** A `min` or `max` whose entries are two different objects of the same glyph
  family, so the min is over incommensurable quantities.
- **(F1-c) SUBSTITUTED INPUT.** Object P is supplied as the input of a lemma whose hypothesis names
  object Q of the same glyph, so the lemma's conclusion is drawn at the wrong value.
- **(F1-d) ARITHMETIC CARRIED.** A decade figure, margin or ceiling computed from one object and
  quoted as the other's — the shape of session 24's three multi-decade errors.
- **(F1-e) STALE EVALUATION OF A MIN** (§53 defect 2, adjacent but distinct): one glyph, one object,
  but several numerical values in force in several files, so which value binds depends on which file a
  reader opens. I record these separately from true collisions, because the repair is different: a
  single-valuation decision, not a rename.

**Per family, in advance:**
- **ε_\***: four objects were named by EPSSTAR §6.1. The collision observable is any file that quotes
  one object's *value* as a constraint on another's; the live-defect observable is (F1-a) or (F1-d) on
  the near-coincidence of EPS-T's ε_\* with N5-sf0's 2.476e-13/C_Δ, which EPSSTAR itself calls a
  coincidence of unrelated thresholds. If no file does that, ε_\* is a naming hazard and not a defect,
  and I will say so.
- **θ_0**: the observable is (F1-b) — a `min` taken over a θ_0 from one lane and a θ_0 from another —
  or (F1-c), a θ ≤ θ_0 hypothesis discharged against the wrong θ_0. θ_0 is the family most likely to
  carry (F1-b), because θ_0 is *defined* as a min in at least one place.
- **ε_1**: the observable is (F1-c) — option C's ε_1 lowered into BFT_B's 𝒦(ε_1), or BFT_B's O(1)
  formula read as ≈1e-40 — and (F1-e), the four live numerical values of symbol 1. I expect (F1-e)
  present and (F1-c) absent-but-one-step-away; if I find (F1-c) present, that is the session's finding
  and I stop renaming and report it.
- **η_1**: the observable is (F1-a), already on the record at REVIEW_PLD_S3 l.463, plus whatever
  (F1-c)/(F1-d) that cross-quote has propagated into. **This is the family where I expect to find a
  live defect**, because two of its objects are two values of the same quantity in the same lemma; the
  question I must answer is not whether the names clash but **whether any number in the lane was
  computed with the wrong one**. The specific thing I will look for: a PLD figure derived from
  η_1 = c_1ε_1 that is quoted anywhere as holding for RLARGE's (R3) threshold, or vice versa.

**What my audit cannot catch, stated now rather than later.** (i) A collision in which both objects
happen to have the same formula today and diverge later — my method is textual and a textual method
cannot see that. (ii) A glyph collision inside a `checks/*.py` script's variable names, which I sample
but do not sweep exhaustively. (iii) Objects that collide only after a LaTeX-vs-unicode normalisation I
do not perform (e.g. `\eta_1` vs `η_1`); I will grep both forms for the four named families and report
the coverage I achieved. (iv) A missing definition: if no file defines a glyph, I can record that it is
undefined but not what was meant.

### §0.5 Pre-registered method

Textual, exact, no numerics required. Where I compute, it is exact rational/decimal arithmetic in plain
python under `checks/sy1_*` with a criteria file written first (rule 2), used only to *price* a live
defect — never to decide a rename. The classification itself is reading, and is labelled COMPUTED
(reading) with the quoted defining line, never PROVEN.

### §0.6 Pre-registered statuses

- **COMPUTED (reading)** — a classification backed by a quoted defining line and a quoted use line.
- **ARGUED** — a classification where the defining line is ambiguous and I say why I chose as I did.
- **LIVE DEFECT** — an (F1-a)…(F1-d) instance, with the wrong value named.
- **STALE VALUATION** — an (F1-e) instance.
- **OPEN** — a glyph whose objects I could not separate from the text.
- A rename is **MECHANICAL** only if every use site is classified and no site is ambiguous. One
  ambiguous site makes the family's rename **OWNER-GATED**, and I say which line gates it.

### §0.7 Pre-registered anti-inflation clause

I claim no mathematics. Every number in this file is quoted from the file that owns it, with its line.
Where I report a value as wrong, I state the arithmetic that makes it wrong in full, so a hostile
reader can check it without re-running anything. If I find zero live defects in a family I say zero.

---

## §1. Scope, method, and one practical warning about line numbers

**Audit timestamp: 2026-10-28T21:05Z–22:10Z.** Every file:line below was read at that state.

**Files in scope.** All 110 live `*.md` of `agents/ym4d-proof` plus `agents/ym4d-existence/EXISTENCE.md`,
and `checks/*` sampled where a criteria file carries a symbol definition. **`*_snapshot.md` are
excluded** (frozen history) and **`REVIEW_*.md` are read but never renamed** (a review is a dated audit
of the text as it then stood; renaming it would falsify the record). For those two classes the
instruction is **annotation**, given in §11.

### §1.1 The rename rule I apply, stated before the tables

Renaming the majority object of a glyph costs hundreds of edits and buys nothing where the file is
unambiguous. So:

> **R1. A file that contains exactly ONE object of a glyph is not renamed.** It gets a one-line scope
> note in its notation section naming which object it means.
> **R2. A file that contains TWO OR MORE objects of a glyph has the minority object(s) renamed.**
> **R3. An object whose glyph is quoted ACROSS files with a different meaning is renamed everywhere,
> whatever the counts** — this is the only case where R1 is overridden, and it is the case that
> produced every defect in §10.
> **R4. The canonical name is one already in use in the lane.** Every name proposed below is quoted
> from the file that introduced it; §9 lists the three places where no name existed and I had to form
> one from an existing glyph.

### §1.2 **A warning the lead must act on before applying any rename table: PROOF.md's line numbers have moved by +79.**

**[COMPUTED, exact.]** EPSSTAR §6.1 cites N5-sf0's ε_* definition at **PROOF.md l.5494, l.5544**; it is
now at **l.5573**. EPSSTAR cites BG-b's ε_* at **l.1759**; it is now at **l.1838**. Both differences are
**exactly +79**, the length of the session-24 header inserted at the top of PROOF.md. I verified three
further pairs (l.331 → l.410, l.2173 → l.2252, l.2296 → l.2375): **+79 in every case.**

> **Consequence.** Every cross-file citation into PROOF.md written before the session-24 header landed
> is off by 79 lines, and **a rename applied by line number into PROOF.md will hit the wrong line.**
> Every table below therefore carries the **exact old string** as well as the line, and the rename must
> be applied by string match within the named file. The line is a locator, not the key.

---

## §2. FAMILY η_1 — **three objects; the lane's worst collision; one LIVE DEFECT (SYM-F1 #1)**

### §2.1 The objects

| # | canonical name | definition in force | DEFINED at | value at the live ε_1 = 6.7·10⁻⁴⁰ (N = 2) |
|---|---|---|---|---|
| **1** | **η_1^RS** | **η_1 := min{ε_1/(2L²), ε_1²/(512·N·A_d(L))}**; Lemma RS (R3)'s dichotomy threshold. At d = 4, L = 3: min{ε_1/18, ε_1²/(4608N)}, and the **quadratic entry is active at every admissible ε_1** (it binds for ε_1 < 512 at N = 2) | **RLARGE.md l.64**, restated **l.976**, numerics **l.1009** | **4.870877·10⁻⁸³** |
| **2** | **η_1^KN** | **η_1 := c_1ε_1, c_1 := 1/(2(L² + 5.5A_d(L))) = 1/117**; Corollary KN-step's re-centred dichotomy threshold | **EXISTENCE.md l.1771, l.1774** | **5.726496·10⁻⁴²** |
| **3** | **η_1^gauge** | **η_1 := η_U/2**, an ℓ⁴ threshold on a Neumann–Coulomb log-gauge potential, bound inside one connectedness argument | **SQ.md l.1679** | not a lane constant (bound variable) |

Objects 1 and 2 differ by **41.07 decades** at the live ε_1, and **their ratio is not a constant**:
η_1^KN/η_1^RS = 4608N/(117ε_1) → ∞ as ε_1 → 0. The names η_1^RS / η_1^KN / η_1^gauge are **already in
use** (ARS_FIX.md §1 l.203-209; echoed at PROOF.md l.59 and in `checks/ar1_criteria.md` l.14), so R4 is
satisfied with no new vocabulary. I verified each definition against its owning file; I did not take
ARS_FIX's table as given.

**Where η_1 does NOT occur, checked by grep over the live set:** HW.md, NORMS.md, BFT_A.md, BFT_B.md,
FLOW.md, LINEAR_PACKAGE.md, CONST_T.md, STAR_CONST.md, NLOC.md, GREENT.md, TENTQ.md, YSUP.md,
TGAUGE_PRICE.md, TAUFLAT.md — **zero occurrences in all fourteen.** The hazard is confined to
RLARGE / PLD / HIST / SF / SQ / PROOF / EXISTENCE.

### §2.2 Use sites, classified

**RLARGE.md — 16 sites, ALL object 1. No rename needed under R1; scope note only.**
l.64 (def), l.65, l.261, l.761, l.830, l.976 (def restated), l.978, l.981, l.994, l.995, l.999, l.1003,
l.1009, l.1026, l.1184, l.1248.

**HIST.md — 9 sites, ALL object 1** (l.151, l.181, l.186, l.1167, l.1377, l.1378, l.1379, l.1386,
l.1481); l.1167 and l.1377 quote RLARGE's defining formula verbatim. **No rename; scope note only.**

**SF.md — 2 sites, both object 1** (l.2203, l.2204; l.2204 quotes the defining min). **No rename.**

**SQ.md — 5 sites, ALL object 3** (l.1679 def, l.1680, l.1681, l.1682 ×2, l.1685). **RENAME (R3: the
glyph is a lane-wide quantity owned elsewhere).**

**EXISTENCE.md — 2 sites, TWO DIFFERENT OBJECTS in one file** (l.1771 = object 2's definition;
l.1804 "instead of the fixed η_1" = object 1). **RENAME BOTH (R2).**

**PROOF.md — 7 sites** (l.58, l.59 ×3, l.60, l.63, l.67, l.71, l.82, l.6894): all are the session-24
header's own flag of this collision, already written with the superscripts. **No rename.**

**PLD.md — 16 sites, MIXED, and this is the defect.** Classified one by one:

| line | text as written | object meant | verdict |
|---|---|---|---|
| 42 | "η_1, ε_loc, a″, a_♯, n_♯ **from RLARGE**" | declares **object 1** | **WRONG as a declaration** — the file then uses object 2 in seven places |
| 50 | (PLD-i)_k, "P(‖1 − U_k(p)‖ ≥ η_1 ∀p ∈ A)", cited to RLARGE §8.2 | object 1 | correct |
| 197 | "a_η = a_kη_1²/16" | object 1 | correct |
| 202 | (via a_η) | object 1 | correct |
| 276 | "e^{−a_dη_1²/g_k²}" | object 1 | correct |
| 767 | "at the thresholds actually used (η_1, η_♭ ≤ ε_1/4)" | either; true of both | harmless, **AMBIGUOUS** |
| **772** | "at t = **η_1 = c_1ε_1 ≤ 2/117** only for N ≥ 507954" | **object 2** | **MISLABEL** (REVIEW_PLD_S3 F-9′). The N-threshold 507954 is object 2's; at object 1 it is astronomically larger. Direction **conservative** — the no-go survives either way |
| **1010** | "coherent level-k curvature ≥ **η_1 = c_1ε_1**" | **object 2** | **MISLABEL** (INH-1) |
| 1048 | "At τ = η_1 this is **RLARGE's** (PLD)_k (i) … a_η = 49η_1²/(256σ_*²)" | **claims object 1** | **AMBIGUOUS AND LOAD-BEARING** — see §2.4; this is the line that gates a mechanical rename |
| 1066 | Proposition INH's title, "above η_1" | object 2 as proved, object 1 a fortiori | **AMBIGUOUS** |
| **1071** | "every level-k (1,2)-plaquette has ‖1 − U_p‖ ≥ **c_1ε_1 = η_1**" | **object 2** | **MISLABEL** (INH-1) |
| **1077** | "**RLARGE's η_1 = c_1ε_1** lies below …" | **object 2** | **MISLABEL** (INH-1) |
| 1078 | "{all level-k plaquettes of a region ≥ η_1}" | object 2 (follows l.1077) | **MISLABEL** |
| **1096** | "does NOT contain **RLARGE's η_1 = c_1ε_1** (c_1 = 1/117 < 2/L² = 2/9)" | **object 2** | **MISLABEL, and it FEEDS the live defect** |
| **1204** | "**RLARGE's thresholds η_1 = c_1ε_1** and η_♭ lie below 2τ_bg" | **object 2** | **MISLABEL** |
| 1211 | "τ = η_1 (in-step part)" | object 2 (same argument) | **MISLABEL** |
| **1259** | "**RLARGE's η_1 = c_1ε_1** is below that" | **object 2** | **MISLABEL** |

**Count: 16 PLD sites — 4 correct at object 1, 8 mislabelled object 2, 3 ambiguous, 1 wrong declaration.**

### §2.3 Was it already on the record? Yes, for two review cycles.

- **REVIEW_PLD_S3 l.463**: *"Today PLD and RLARGE use different η_1."*
- **REVIEW_PLD_S3 l.299 (INH-1)**: *"'RLARGE's η_1 = c_1ε_1' (l.1010, 1071, 1077, 1096, 1204, 1259) is
  wrong"*; **l.39-40** records REVIEW_PLD_S1_S2's F-9 making the same slip.
- **REVIEW_PLD_S3 l.462 (E9)** offered two horns: adopt KN-step in RLARGE §6, **or** replace every
  "η_1 = c_1ε_1" in PLD §15 by (R3)'s η_1. **RLARGE v3 chose the second horn at l.830** ("η_1 is
  v2/v3's η_1 (E9)") — and PLD was never edited to match. **The lane therefore holds a decision that
  one of its two files did not implement.** That is why the rename here is not bookkeeping.

### §2.4 **LIVE DEFECT — SYM-F1 #1: PLD's m_τ = 3 is object 2's number, asserted of object 1's threshold**

**Status: LIVE DEFECT [COMPUTED, exact, `checks/sy1_symbols.py` → `checks/sy1_out.txt`, SY1-1/2/3].**

PLD.md l.1096-1100 runs the descent recursion and concludes, **in object 1's name**:

> l.1097-1098: *"the thresholds grow by L²/(2C_I) per level until they exceed 2τ_bg, after m_τ levels:
> **(L²/(2C_I))^m c_1 ≥ 2C_I L^{−2}, i.e. m_τ = 3 at L = 3 if C_I = 1**"*
> l.1100: *"**Hence: (PLD)_k at RLARGE's thresholds is an output of steps k, …, k + m_τ**"*

The recursion at l.1097 has `c_1` — i.e. the **ratio η_1/ε_1 of object 2** — substituted for the ratio
η_1/ε_1. **That ratio is a constant only for object 2.** For object 1 it is ε_1/(4608N), so m_τ is
ε_1-dependent, and at the live ε_1 it is not 3:

| C_I | m_τ at **η_1^KN** (what PLD computed) | m_τ at **η_1^RS** (what l.1100 claims) | factor |
|---|---|---|---|
| 1 | **3** | **66** | ×22 |
| 1.5 | **4** | **90** | ×22.5 |
| 2 | **5** | **122** | ×24.4 |

(ε_1 = 6.7·10⁻⁴⁰, N = 2, L = 3, exact rational arithmetic; `sy1_out.txt` SY1-1, SY1-2.)

> **The wrong value: `m_τ = 3` at PLD.md l.1098, repeated at l.1206, l.1244 ("m_τ = 3, 4, 5") and
> l.1260. The right value at the threshold l.1100 names is `m_τ = 66` (C_I = 1), 90 (C_I = 1.5),
> 122 (C_I = 2).**

**What changes.** m_τ is the **look-ahead depth** of PLD's architecture: l.1100 and l.1260 say
(PLD)_k at RLARGE's thresholds is an output of steps k, …, k + m_τ, and l.1210-1212 says *"evaluating
them after m_τ more steps changes no other step"*. A look-ahead of 66 levels rather than 3 is a
different architecture: REVIEW_PLD_S3 l.343 already holds that l.1211-1212's "changes no other step"
is false, and at depth 66 the product structure across the m_τ levels (l.1098-1099, already ARGUED and
resting on Lemma LC's ℓ² transfer) is being asked to hold 22× further. **This is why the rename must
stop here: mechanically rewriting l.1096's "RLARGE's η_1 = c_1ε_1" to "η_1^KN = c_1ε_1" would leave
l.1098's `m_τ = 3` attached to l.1100's "RLARGE's thresholds", which is the error itself.**

**Was it on the record?** REVIEW_PLD_S3 **(Arch-3)** l.345-350 found it: *"m_τ = 3 uses η_1 = c_1ε_1,
which is not RLARGE's η_1"*, and l.350: *"'m_τ = 3' is not RLARGE's number"*. **It was recorded in
review cycle 3 and has not been fixed in PLD through session 7.** ARS_FIX §4.2 re-derived 66/90/122
in session 24. I have now re-derived all of it independently from PLD's own recursion and RLARGE's own
definition (not from either file's summary), with the designed-FAIL control below.

**Could this check have failed?** Yes, and I ran the control. `sy1_criteria.md` SY1-3 runs the SAME code
path with the SAME criterion ("every entry ≥ 40") at ε_1 = 2 — RLARGE's illustrative value — where the
answer should be small. It returned **(5, 7, 10)** and the criterion **FAILED as designed**, and the
triple reproduces REVIEW_PLD_S3 l.435's independently recorded 5/7/10 exactly. So SY1-2's criterion is
ε_1-sensitive and its PASS carries information.

### §2.5 A second recorded fact that the two objects decide differently [COMPUTED, SY1-4]

**RLARGE.md l.65**: *"For ε_1 ≤ 2, **η_1 ≤ η_q** unless δ_0/A_d binds (**"CORRECT", REVIEW_RLARGE_V2
§2.3**)."* With η_q := min{ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d} (RLARGE l.64; δ_0 entry omitted as
unevaluated, which can only make η_q smaller):

| | η_1/η_q at ε_1 = 6.7·10⁻⁴⁰ | ordering |
|---|---|---|
| **object 1 (η_1^RS)** | 3.35·10⁻⁴⁰ | **η_1 ≤ η_q — RLARGE l.65 HOLDS** |
| **object 2 (η_1^KN)** | **512/13 = 39.3846** (N = 2); **59.0769** (N = 3) | **η_1 > η_q — RLARGE l.65 REVERSES** |

So l.65's recorded ordering is **true of object 1 and false of object 2 by ×39.4**. This is not yet a
live defect, because every file that *uses* the ordering (HIST l.181, l.186) uses object 1. It becomes
one the moment the KN adoption lands, and HIST l.186's *"the rest from η_q² against η_1²"* — the reason
HIST's joint route is called the better route — reverses with it. **Recorded here so the adoption does
not silently invalidate it.** (ARS_FIX §5.1 reached 39.3846 by a different route; REVIEW_PLD_S3 l.433
reached it a third way. Three independent arrivals.)

### §2.6 Rename table for η_1 — **OWNER-GATED, not mechanical**

Apply by **string match inside the named file**, not by line number.

| file | line | old string | new string | note |
|---|---|---|---|---|
| SQ.md | 1679 | `‖w‖_{ℓ⁴} < η_1 := η_U/2` | `‖w‖_{ℓ⁴} < η_1^gauge := η_U/2` | R3 |
| SQ.md | 1680 | `‖w‖_{ℓ⁴} ≤ η_1}` | `‖w‖_{ℓ⁴} ≤ η_1^gauge}` | |
| SQ.md | 1681 | `\|w\| ≤ η_1 pointwise` | `\|w\| ≤ η_1^gauge pointwise` | |
| SQ.md | 1681 | `C_Uε_U < η_1 for ε_U` | `C_Uε_U < η_1^gauge for ε_U` | |
| SQ.md | 1682 | `C(η_1 + η_1²)` | `C(η_1^gauge + (η_1^gauge)²)` | two in one line |
| SQ.md | 1685 | `‖w‖ < η_1. 𝒯 ∋ t_*` | `‖w‖ < η_1^gauge. 𝒯 ∋ t_*` | |
| EXISTENCE.md | 1771 | `The gain is in η_1: from min{…} … to c_1ε_1` | `The gain is in the dichotomy threshold: from η_1^RS = min{…} … to η_1^KN := c_1ε_1` | R2 |
| EXISTENCE.md | 1804 | `instead of the fixed η_1` | `instead of the fixed η_1^RS` | R2 |
| PLD.md | 42 | `η_1, ε_loc, a″, a_♯, n_♯ from RLARGE` | `η_1^RS, ε_loc, a″, a_♯, n_♯ from RLARGE; η_1^KN := c_1ε_1 from Corollary KN-step` | fixes the wrong declaration |
| PLD.md | 50, 197, 202, 276 | `η_1` | `η_1^RS` | the four correct object-1 uses |
| PLD.md | 767 | `(η_1, η_♭ ≤ ε_1/4)` | `(η_1^RS, η_1^KN, η_♭ ≤ ε_1/4)` | true of both; make it say so |
| PLD.md | 772 | `at t = η_1 = c_1ε_1 ≤ 2/117` | `at t = η_1^KN = c_1ε_1 ≤ 2/117` | plus the clause in §11.2 |
| PLD.md | 1010 | `≥ η_1 = c_1ε_1` | `≥ η_1^KN = c_1ε_1` | |
| PLD.md | 1066 | `above η_1` | `above η_1^KN` | and add "a fortiori above η_1^RS" |
| PLD.md | 1071 | `≥ c_1ε_1 = η_1` | `≥ c_1ε_1 = η_1^KN` | |
| PLD.md | 1077 | `RLARGE's η_1 = c_1ε_1` | `KN-step's η_1^KN = c_1ε_1` | |
| PLD.md | 1078 | `≥ η_1}` | `≥ η_1^KN}` | |
| PLD.md | 1096 | `RLARGE's η_1 = c_1ε_1` | `KN-step's η_1^KN = c_1ε_1` | **do not land without §2.4's fix** |
| PLD.md | 1204 | `RLARGE's thresholds η_1 = c_1ε_1 and η_♭` | `KN-step's η_1^KN = c_1ε_1 and RLARGE's η_♭` | |
| PLD.md | 1211 | `τ = η_1 (in-step part)` | `τ = η_1^KN (in-step part)` | |
| PLD.md | 1259 | `RLARGE's η_1 = c_1ε_1` | `KN-step's η_1^KN = c_1ε_1` | |
| **PLD.md** | **1048** | `At τ = η_1 this is RLARGE's (PLD)_k (i)` | — | **BLOCKED: owner must say which object. See §2.7** |
| **PLD.md** | **1098, 1206, 1244, 1260** | `m_τ = 3` / `m_τ = 3, 4, 5` | — | **BLOCKED by §2.4** |
| RLARGE / HIST / SF / PROOF | — | — | — | **no rename (R1)**; scope note in §11 |

### §2.7 The one site that a human must decide: PLD.md l.1048

> *"At τ = η_1 this is **RLARGE's (PLD)_k (i)** on (M3) with **a_η = 49η_1²/(256σ_*²)**, C = C_net; at
> τ = η_q it is HIST's (PLD-q)_k."*

This line **supplies a_η to RLARGE**: RLARGE.md l.1020-1021 defines **a_RS := min{a_η, κε_1²/(256N)}**
with *"a_η from (PLD)_k (i)"*. If PLD's η_1 here is object 2, the a_η supplied is **82.14 decades larger**
than the a_η RLARGE's own ledger carries, and RLARGE would be consuming a rate proved at a threshold
**41 decades coarser than the one its dichotomy needs** — (F1-c), the substituted input. If it is
object 1, the line is correct and only its name is wrong.

**Which it is cannot be read off the text**, because the sentence names RLARGE (object 1) while sitting
inside the §15 argument that uses object 2 throughout. **I did not guess.** What I can report is the
direction and the consequence either way:

- **RLARGE's recorded number is safe either way.** I checked: a_RS's ledger value **5.93136·10⁻¹⁶⁶**
  (ARS_FIX §4.1) is computed from **η_1^RS** through RLARGE's own bare-level a_η = η_1²/(2N) (l.981,
  l.1026), not through PLD l.1048. So no number in RLARGE is currently inflated. **This is the reason
  l.1048 is a naming defect today and not a 82-decade arithmetic one.**
- **But the supply relation is then unsatisfied, not satisfied.** A probability bound at the larger
  threshold η_1^KN is a *weaker* statement than at η_1^RS; it does not imply the one RLARGE needs. So if
  l.1048 means object 2, RLARGE l.1021's "a_η from (PLD)_k (i)" has **no supplier**, and a_RS's
  CONDITIONAL hypothesis is on a statement nobody has proved at the right threshold.
- Either way **a_RS's status is unchanged** — ARS_FIX §3.4 is right that (PLD)_k at η_1 is not an
  in-step output at any RS-compatible threshold (REVIEW_PLD_S3 l.304-309) — so this is a question about
  what the lane has *written*, not about what it has proved.

**Decision needed from PLD's owner, one word:** at l.1048, is τ = η_1^RS or τ = η_1^KN? Everything else
in the η_1 table is mechanical once that is answered.

---

## §3. FAMILY ε_* — **four objects (five counting the level-indexed sub-family); ZERO live defects, and I say what I looked for**

### §3.1 The objects

| # | canonical name | definition in force | DEFINED at | value |
|---|---|---|---|---|
| **1** | **ε_*^{EPS-T}** | the ε-regularity threshold of Theorem EPS-T: ‖𝒫‖_{ℓ²(B_R)} ≤ ε_* **and** R^{3−4/q}‖𝒮‖_{ℓ^q(B_R)} ≤ ε_*; existential in (N, q), pinned by (ABS-ε) | **SQ.md l.1460-1461** | EPSSTAR §5; CONST_T's reference 10⁻⁴ is **not admissible** (EPSSTAR §3.2) |
| **2** | **ε_*** (keeps the bare glyph) | **ε_* := α_*/(10·p_L(4R_* + 5)L)** — Theorem N5-sf0's level-0 curvature threshold | **PROOF.md l.5573** | **2.476·10⁻¹³/C_Δ** (session-23 class) |
| **2′** | **ε_*^{(i)}** | the level-i member of the same family (ε_*^{(1)} at l.6029-6031) | **PROOF.md l.6029-6031** | a sub-family of #2, already distinguished; **not a collision** |
| **3** | **ε_*^{BG-b}** | **ε_* := (ε_1²/(4N·B_LF))^{1/2}**, g-independent; the M_2 ≤ ε_* of hypothesis (BG-b) (b1) | **PROOF.md l.1838** | symbolic in B_LF |
| **4** | **ε_f^{max}** | **ε_* := max_t ε_f(U_t, X)**, a bound variable of one continuation argument | **BFT_B.md l.2719** | O(1), local |

**Line numbers corrected.** EPSSTAR §6.1 cites #2 at PROOF l.5494/l.5544 and #3 at l.1759; at today's
state those are **l.5573** and **l.1838** (§1.2's +79 drift). The definitions themselves reproduce
exactly; only the locators moved.

### §3.2 Use sites, by file, with the object each file contains

| file | objects present | sites | action |
|---|---|---|---|
| SQ.md | **#1 only** | l.1170, 1171, 1172, 1318, 1319, 1377, 1460, 1461, 1462, 1491, 1495, 1496, 1512, 1517, 1518, 1622, 1667 | R1 — scope note |
| CONST_T.md | **#1 only** | 19 sites (l.15, 292, 355, 400, …) | R1 — scope note |
| STAR_CONST.md | **#1 only** | 20 sites | R1 — scope note |
| EPSSTAR.md | **#1** (plus #2/#3/#4 quoted *as* the other objects, in §6.1, correctly labelled) | 144 sites | R1 — scope note |
| **PROOF.md** | **#2 AND #3 AND #2′** | #2: l.129, 225, 226, 5559, 5560, 5565, **5573 (def)**, 5577, 5615, 5617, 5623, 5626, 5633, 5762, 5777, 5779, 5844, 5846, 5859, 5867, 5983, 6101, 6123, 6299, 6302, 6310, 6718. #3: l.410, **1838 (def)**, 1839, 1854, 1919, 1922, 1939, 1949, 1950, 1953, 2252, 2375. #2′: l.6029, 6030, 6031, 6032, 6047, 6123, 6155, 6299, 6302, 6310 | **R2 — rename #3's 12 sites** |
| **BFT_B.md** | **#2 AND #4** | #2: l.885, 886 (already written **ε_*(R)**). #4: l.2719 (def), 2721, 2722, 2733, 3151, 3155 | **R2 — rename #4's 6 sites** |
| LINEAR_PACKAGE.md | **#3 only** | l.35 (def, with B already renamed B_LF), l.182 | **R3 — rename, to match PROOF** |
| SF.md | #2 only | l.2789, 2817, 2818, 2858 + 11 more | R1 |
| RLARGE.md | #2 only | l.69, 71, 76, 261 | R1 |
| NORMS.md | #2 only | l.748 (+1) | R1 |
| PLD.md | #2 only | l.1022, 1131, 1132 | R1 |
| RTARGET.md | **#2 AND #3** | #2: l.749, 758, 891, 1062, 1089. **#3: l.219** | R2 — rename l.219 |
| TAUFLAT.md | #1 (and names #2/#3/#4 correctly at l.156) | l.156 + 5 | R1 |
| EXISTENCE.md | #2 only | 1 site | R1 |

### §3.3 Why #2 keeps the bare glyph

PROOF.md is the master ledger and #2 is its own; #2 is also the most widely distributed (8 files) and
already carries a level-indexed sub-family ε_*^{(i)} that a new superscript would collide with. The
alternative — giving the bare glyph to #1 — would rename ~60 PROOF/SF/RLARGE sites instead of ~20.
**Total rename cost under this choice: 12 + 6 + 2 + 1 = 21 edits.**

### §3.4 The live-defect hunt: **ZERO found. Here is exactly what I searched for.**

My §0.4 pre-registered two observables for ε_*: (F1-a) a file quoting one object's *value* as a
constraint on another's, and (F1-d) a decade figure carried across the near-coincidence between #1's
value (10⁻¹²-10⁻¹⁶, EPSSTAR §5) and #2's 2.476·10⁻¹³/C_Δ. I checked:

1. **Every file that contains two objects** (PROOF, BFT_B, RTARGET): no `min`, inequality or
   substitution joins them. PROOF's #3 lives entirely in §… l.1838-2375 (the BG-b/large-field block)
   and #2 entirely in l.5559-6718 (the N5-sf0 block); they never appear in one expression.
2. **Every numerical comparison against 2.476·10⁻¹³/C_Δ** (RLARGE l.69-76, NORMS l.748, PLD l.1022,
   SF l.2818): all are #2 against #2.
3. **The θ_ε channel** (SQ l.1622), which is the only place #1 propagates: it is #1 against #1, and
   the normalisation matches l.1512's ε_*²/16 (I checked the square).
4. **The one historical instance, now closed.** The lead's brief to the EPSSTAR worker relayed
   "PROOF's ε_* = 2.476e-13/C_Δ" as a comparator for #1. That **was** an (F1-a), and EPSSTAR §6.1
   caught it before it entered any arithmetic: *"It is not a constraint on my ε_* at all."* It is
   recorded in RTARGET §53 against the lead. **Closed, not live.**

**Verdict: ε_* is a naming hazard with no corrupted value today.** That is a finding, not a shrug: the
check that produced it is the same check that produced §2.4's defect, run over a different family.

### §3.5 One finding adjacent to ε_*, which is NOT a collision between objects [ARGUED, owner's call]

**SQ.md states (EPS-0a) twice with ε_* at two different normalisations.**

- **l.1171** (the §13.5 statement, as restated by S3-6): *"if **Σ_{B_R}|𝒫|² ≤ ε_*** and
  **R³sup_{B_R}|𝒮| ≤ ε_*^{1/2}**"*.
- **l.1512** (Corollary EPS-0a, §15.3, the one actually proved via EPS-T): *"with
  **Σ_{box_0}|𝒫|² ≤ ε_*²/16**, n^{3−4/q}(Σ|𝒮|^q)^{1/q} ≤ ε_*/16"*.

The curvature clause is `≤ ε_*` in one and `≤ ε_*²/16` in the other; the source clause is `≤ ε_*^{1/2}`
in one and `≤ ε_*/16` in the other. For ε_* ≪ 1 these differ by a square and a square root, so
**l.1171's (EPS-0a) is a strictly STRONGER claim than l.1512's** (weaker hypotheses, same conclusion).
Only l.1512's form is proved. The operative chain is self-consistent — Theorem EPS-0 (l.1622-1628) and
θ_ε are built on l.1512 — so nothing downstream is wrong. But **l.1171 as written is not what §15
delivers**, and a consumer reading §13.5 rather than §15.3 would over-claim. SQ's own l.1517-1518
notices the gap ("the analogue of its hypothesis R³sup|𝒮| ≤ ε_*^{1/2}") without resolving it.
**Proposed fix (SQ's owner): at l.1171 write ε_*^{(13.5)} and state ε_*^{(13.5)} := (ε_*^{EPS-T})²/16,
or restate l.1171 in the l.1512 normalisation.** Filed in §11.

---

## §4. FAMILY θ_0 — **FOUR objects, not two; the collision that caused the 52-decade τ_♭ error**

### §4.1 The objects

| # | canonical name | definition in force | DEFINED at | value |
|---|---|---|---|---|
| **1** | **θ_0^{SUP}** | **θ_0 := 1/(2C_err)**, C_err := C_p(K² + K_top²) + 4C_e[K²/(L(L−1)) + 1.011·K·C_D·L/(L²−1)]; the admissible-θ ceiling of Theorem SUP-price | **SQ.md l.188** | **≈ 3·10⁻⁸/C_D²** (l.216; l.212's "10⁻⁸/C_D²" is 3× low **by SQ's own correction**) = **1/(3.31·10⁷C_D²)** |
| **2** | **θ_0^{SQ4}** | **θ_0 := min{θ_G, θ_ε}**, θ_ε the largest θ with 4·2.47N√κ_+θ ≤ ε_*^{EPS-T} and 16·32^{1/8}C_0θ ≤ ε_*^{EPS-T}; Theorem EPS-0's threshold | **SQ.md l.1622** (existentially introduced at **l.1167**) | **≤ 1.46·10⁻¹³** (θ_G binds, REVIEW_SQ_S4 S4-14) |
| **3** | **θ^{(0)}_{tilt}** | the **Chernoff tilt parameter θ at level 0**: "(SDP)^A_0 with a_A^{(0)} = θ_0ε_1²/(2N)", where θ is the tilt of l.1430's e^{θY}e^{−6θa_bad u_k} | **PLD.md l.1437** | a free parameter, not a threshold |
| **4** | **θ^{(0)}_{loc}** | the **level-0 value of the iterated first-order localisation error**: "CURV1_k at θ needs CURV1_0 at θ_0 = θ·Π_j(16κ_j𝔠_∞^{(j+1)})^{−1}" | **PROOF.md l.6502** | a bound variable of failure mode CURV-F2″ |

Objects 3 and 4 are "θ at level 0", not thresholds; session 24 counted two θ_0 because it looked only
at SQ. **Four is the honest count.** Objects 3 and 4 are bound variables, but both sit in files whose
other occupants read θ_0 as a threshold, so R2 applies.

### §4.2 Use sites in SQ.md — all 24, classified

| object | sites |
|---|---|
| **θ_0^{SUP}** (18) | l.183, **188 (def)**, 210, 212, 216, 217, 218, 219, 225, 231, 294, 306, 318, 342, 557, 930 |
| **θ_0^{SQ4}** (8) | **l.1167**, 1168, 1357, **1622 (def)**, 1623, 1628, 1633, 1634 |

Elsewhere: **HW.md l.183, l.604 — θ_0^{SUP}** (both). **PLD.md l.1437 — object 3.**
**PROOF.md l.6502 — object 4**; PROOF l.52, 92, 94, 6894 are the session-24 flag, already superscripted.
**EPSSTAR, TAUFLAT, REVIEW_SQ_S4, CONST_T, KN_ADOPT, EPS1_SWEEP, ARS_FIX** already use the superscripts
or discuss the collision as such.

### §4.3 The collision is the root cause of a 52-decade error, and the rename was already ordered

**REVIEW_SQ_S4 S4-14 item 4** (l.318-320): *"**θ_0 collides with §0.3's θ_0.** §0.3 l.188 defines
θ_0 := 1/(2C_err); §15.3 l.1622 redefines θ_0 := min{θ_G, θ_ε}. Both appear as 'θ_0/C′' inside
τ-formulas (l.1633 and l.294/l.318), and **both constraints apply**. Rename one … this is load-bearing,
not cosmetic."* **TAUFLAT l.555**: *"S4-14 item 4's instruction to rename one θ_0 is the root cause and
should be executed."* **It has not been executed.**

The mechanism, which is exactly my §0.4 observable **(F1-b) MIXED MIN**:

- **τ_R := min{τ_0, τ_*, τ_S, θ_S/C′, **θ_0^{SQ4}**/C′}** (SQ l.1633)
- **τ_♭ := min{τ_F, **τ_R**, **θ_0^{SUP}**/C′, ε_M/(C_DC′), θ_♯/C′, 1/(73.6Nc′²A′²)}** (SQ l.294, l.318)

Both minima are written with the glyph `θ_0/C′`. A reader who carries §15.3's definition into §0.3's
formula sees τ_♭'s θ_0/C′ entry as **already inside τ_R**, and collapses τ_♭ to τ_R — dropping the
θ_0^{SUP} entry. **REVIEW_SQ_S4 S4-14 item 1 did exactly that**, writing that τ_R *"becomes the binding
entry … displacing SUP-price's θ_0/C′"*. The two are not alternatives; they are two entries of one min
and both bind.

**I reproduced TAUFLAT's window independently** [`sy1_out.txt` SY1-5]: τ_R ≤ θ_0^{SUP}/C′ holds iff
**C_D ≤ 455.283301** (exact C_D² = 40000000000/192973), against the C_D ≈ 4.76·10¹⁵ that the same review
produces nine items later. Designed-FAIL control at τ_R = 2.75·10⁻¹⁴ returns C_D ≤ 143.97 and **fails**
the ±10⁻⁴ test, as designed.

**Is it live?** The corrected η_♭ = 3.52·10⁻⁸⁸ is now in use downstream (EPS1_SWEEP §4.5 derives
ε_1^cut ≤ 9.38495·10⁻⁴⁵ from it). The stale 4.2·10⁻³⁶ survives only in **REVIEW_SQ_S4 l.314** (a review
file — annotate, do not edit) and in EPSSTAR l.51's comparator list, which labels it as the figure
under dispute. **So the 52-decade error is CORRECTED-BUT-NOT-RENAMED: the number is fixed, the glyph
collision that produced it is not, and it will produce another one.**

### §4.4 **LIVE DEFECT — SYM-F1 #2: HW.md quotes a θ_0 figure that SQ.md itself corrects four lines later**

**Status: LIVE DEFECT (stale quoted constant, ×9) [COMPUTED, exact, `sy1_out.txt` SY1-6].**

- **SQ.md l.212**: *"θ_0 ≈ 10⁻⁸/C_D² at C_D = 2."*
- **SQ.md l.216** (the [RSQ1-fix M-6] correction, four lines later): *"**θ_0 ≈ 3·10⁻⁸/C_D² (the
  '10⁻⁸/C_D²' above is 3× low)**."*
- **HW.md l.183**: *"τ_♭ ≤ θ_0/C′ with **SQ's θ_0 ≈ 10⁻⁸/C_D²**."*
- **HW.md l.604**: *"a_bad = c_♭τ_♭² ≤ (1/640)(θ_0/C′)² **≈ 5·10⁻²³/C_D⁴** [arithmetic from SQ's stated
  θ_0 ≈ 10⁻⁸/C_D²]."*

**HW quotes the superseded figure.** At SQ's corrected θ_0 = 3·10⁻⁸/C_D², the same formula gives

  a_bad = (1/640)·(3·10⁻⁸/(53·C_D²))² = **5.00623·10⁻²²/C_D⁴**, not 5·10⁻²³/C_D⁴.

> **The wrong value: `a_bad ≈ 5·10⁻²³/C_D⁴` at HW.md l.604 (and the θ_0 it rests on at HW.md l.183).
> The right value is `a_bad ≈ 5.01·10⁻²²/C_D⁴` — HW's figure is low by ×10.0 as displayed (×9 exactly,
> since θ_0 enters squared and the correction factor is 3; the extra 11% is HW's rounding of
> 5.56·10⁻²³ to 5·10⁻²³).**

**Direction: conservative.** a_bad is a suppression rate, so HW's figure under-states the suppression;
no conclusion of HW's flips, and the g_0² ≈ 2.5·10⁻¹⁵²/C_Ω ceiling that HW compares against
(l.1758, l.2033, l.2183) is unaffected. But it is a quoted constant that the owning file had already
corrected, carried for two sessions, and it is the same shape as the 52-decade error one level down.

### §4.5 Rename table for θ_0 — **MECHANICAL**

| file | lines | old string | new string |
|---|---|---|---|
| SQ.md | 183, **188**, 210, 212, 216, 217, 218, 219, 225, 231, 294, 306, 318, 342, 557, 930 | `θ_0` | `θ_0^{SUP}` |
| SQ.md | **1167**, 1168, 1357, **1622**, 1623, 1628, 1633, 1634 | `θ_0` | `θ_0^{SQ4}` |
| HW.md | 183, 604 | `θ_0` | `θ_0^{SUP}` (and apply §4.4's value fix in the same edit) |
| PLD.md | 1437 | `a_A^{(0)} = θ_0ε_1²/(2N)` | `a_A^{(0)} = θ^{(0)}ε_1²/(2N)` (θ^{(0)} the level-0 tilt) |
| PROOF.md | 6502 | `CURV1_0 at θ_0 =` | `CURV1_0 at θ^{(0)} =` |

**No ambiguous site.** Every SQ occurrence is inside either the §0.3 SUP-price block (l.183-930) or the
§13.5/§15.3 EPS-0 block (l.1167-1634), with no interleaving; I checked each line individually rather
than by block. **This family's rename is mechanical and can be landed as written.**

---

## §5. FAMILY ε_1 — **six objects; the collision is real but inert; one STALE VALUATION with four live numbers**

### §5.1 The objects

| # | canonical name | definition in force | DEFINED at | scale |
|---|---|---|---|---|
| **1** | **ε_1** (keeps the bare glyph) | the small-field plaquette cut: χ_Q := Π_{p⊂int Q}**1{‖1 − U(p)‖_op < ε_1}** | **RLARGE.md l.58**; ceiling **l.70-72** | **≈ 10⁻⁴⁰** |
| **2** | **ε_1^{N2}** | **ε_1 := [Λ_2(L²/(L²−1))(4C_eΛ_2 + 12c_h(Λ_2^{(1)})²Λ_2)]^{−1}·min(1,…)**, a bound on the coarse flatness f_k defining 𝒦(ε_1) | **BFT_B.md l.3058** | **O(1)** — an explicit geometric formula |
| **3** | **ε_1^{disc}** | a fixed disc radius, "on a disc \|φ\| ≤ ε_1" / "\|q_αF\| ≤ ε_1" | **FLOW.md l.1927** | O(1) |
| **4** | **ε_1^{mode}** | a mode amplitude, "modes ε_1e^{ikx} on 1-links, ε_2e^{−ikx} on 2-links" | **FLOW.md l.771** | bound variable |
| **5** | **ε_1^{exp}** | a ±1 exponent index on a loop word, "C = c_1^{ε_1}⋯c_ℓ^{ε_ℓ}" | **EXISTENCE.md l.2205** | ±1 |
| (6) | ε_1^{gas} | an activity bound, **already superscripted** | HW.md l.1444 | — **not a collision** |

I verified each independently of EPS1_SWEEP §1 and reproduce its split exactly, with one addition: it
did not state that **BFT_A.md contains ZERO ε_1** (checked), which bounds the lane-B exposure to BFT_B.

### §5.2 Use sites

| file | objects | action |
|---|---|---|
| RLARGE (73), HIST (78), SF (90), PLD (155), HW (22 + the superscripted gas one), PROOF (77), SQ, NORMS, TAUFLAT, EPSSTAR, EPS1_SWEEP, ARS_FIX | **#1 only** | R1 — no rename |
| **BFT_B.md** | **#2 only**, 17 sites: l.2773, 2870, 2871, 2909, 2927, 3055, **3058 (def)**, 3059, 3077, 3105, 3148, 3229, 3276, 3311, 3312, 3429, 4600 | **R3 — rename** (see §5.3) |
| **FLOW.md** | **#3 AND #4**: #3 at l.1927, 1931, 2834, 3000; #4 at l.771 | **R2 — rename both** |
| **EXISTENCE.md** | **#1 AND #5**: #5 at l.2205 only; the other 31 are #1 | **R2 — rename l.2205** |
| BFT_A.md | **none** | — |

### §5.3 Why BFT_B's ε_1 is renamed although BFT_B contains only one object

R3. The hazard is not within BFT_B; it is that **BFT_B states (N2-0)_j in the same words RLARGE states
its own threshold in**: BFT_B l.2870 *"There are ε_1 > 0 and C_N, C_ax, C_box < ∞ … such that for every
V ∈ 𝒦(ε_1)"* against RLARGE l.130 *"There are g-independent constants ε_1 > 0, a > 0, …"*. A reader
aggregating them either reads BFT's threshold as ≈10⁻⁴⁰ (false: it is an explicit O(1) formula) or
carries an ε_1 *lowering* into 𝒦(ε_1), shrinking lane B's class and forcing 𝒞_glob(ε)'s ε down with it
(𝒞_glob(ε) ⊂ 𝒦(4ε + Cε²), BFT_B l.2866) — **a cascade nobody has priced**. The option-C ε_1 move is
live this session, which makes this the one ε_1 collision that is one step from becoming a defect.

### §5.4 The live-defect hunt for ε_1: **ZERO cross-object defects. What I searched for.**

(F1-c), the substituted input, was my pre-registered observable. I checked:
1. **Does anything outside BFT_B quote BFT_B's ε_1?** PROOF mentions it at l.53 and l.90 — both inside
   the session-24 header's own flag, both correctly labelled. **No other file does.** BFT_A: zero.
2. **Does anything outside FLOW quote FLOW's?** No.
3. **Is the option-C ceiling scoped?** EPS1_SWEEP §1 scopes it to symbol 1 explicitly. Checked.
4. **Does 𝒦(ε_1) appear outside BFT_B?** Only at PROOF l.112, in the flag.

**Verdict: inert today, and the rename is what keeps it inert.**

### §5.5 **STALE VALUATION (F1-e): symbol 1 has FOUR live numerical values in four files**

| value | source | status of that source | a_bad = c_prε_1² at it |
|---|---|---|---|
| 1.27·10⁻³⁹ | **SF.md l.2837** | SF l.2834 labels the whole block *"illustrative in the unevaluated constants"* | 8.972·10⁻⁸⁵ |
| 9.52·10⁻⁴⁰ | **RLARGE.md l.71** | first entry of the ceiling min, superseded in the same line by TB-1 | 5.041·10⁻⁸⁵ |
| 8.95·10⁻⁴⁰ | **RLARGE.md l.611** | SF §22.7 / REVIEW_SF_S7 TB-1, in a comparison table | 4.456·10⁻⁸⁵ |
| **6.7·10⁻⁴⁰** | **RLARGE.md l.72** | **the headline**: *"So ε_1 ≲ 6.7·10⁻⁴⁰"* | 2.497·10⁻⁸⁵ |

Spread **×1.90** in ε_1, **×3.59** in a_bad. **One quoting error worth naming: NORMS.md l.746 quotes
SF l.2837's 1.27·10⁻³⁹ as the current ε_1** — *"So ε_1 = 1.27·10⁻³⁹ (SF.md l.2837) … are already
k-independent"* — without SF's own "illustrative" caveat. NORMS's conclusion is qualitative
(k-independence), so **no number of NORMS's breaks**; but it is a figure quoted past its own
disclaimer. **This is a single-valuation decision for RLARGE's and SF's owners, not a rename**; filed
in §11. The audit's recommendation: **6.7·10⁻⁴⁰ is the headline and should be the only quoted value**,
with the other three marked as superseded where they stand.

### §5.6 Rename table for ε_1 — **MECHANICAL**

| file | lines | old | new |
|---|---|---|---|
| BFT_B.md | 2773, 2870, 2871, 2909, 2927, 3055, **3058**, 3059, 3077, 3105, 3148, 3229, 3276, 3311, 3312, 3429, 4600 | `ε_1` | `ε_1^{N2}` (and `𝒦(ε_1)` → `𝒦(ε_1^{N2})`) |
| FLOW.md | 1927, 1931, 2834, 3000 | `ε_1` | `ε_1^{disc}` |
| FLOW.md | 771 | `modes ε_1e^{ikx} … ε_2e^{−ikx}` | `modes ε^{mode}_1e^{ikx} … ε^{mode}_2e^{−ikx}` |
| EXISTENCE.md | 2205 | `C = c_1^{ε_1}⋯c_ℓ^{ε_ℓ}` | `C = c_1^{s_1}⋯c_ℓ^{s_ℓ}` (s_i = ±1) — **the one place I had to form a name; see §9** |

---

## §6. THE SWEEP — families nobody had named

Method: for each candidate glyph I grepped the live set for a *defining* occurrence (`X :=`, `X =`,
"there are X") and read the surrounding statement. A glyph is declared a **FAMILY** when two defining
occurrences have right-hand sides that are not equal as formulas. It is declared **SINGLE** only when
I found exactly one defining form and every other occurrence is consistent with it — and I say below
which defining line I took.

### §6.1 **C_1 — FAMILY, at least THIRTEEN objects. The largest collision in the lane.**

| # | definition | DEFINED at | value |
|---|---|---|---|
| 1 | `C_1 := 2κ_0B`, B := C_Ke^{κ_0}K_0 — Theorem CE's polymer prefactor | **PROOF.md l.2066, l.2433**; LINEAR_PACKAGE l.299 | astronomical (κ_0 ≈ 151.3) |
| 2 | `C_1 := L² + 4cA_L`, c = 4 arcsin(1/4) | **PROOF.md l.3982** | **45.4** (d = 4); 33.26 (d = 3) |
| 3 | `C_1 = C(R_0)` — a localisation constant | **PROOF.md l.1949** | symbolic |
| 4 | `C_1 := Õ_1(V, W)^{−1} − (1 − Π_V)` — **an OPERATOR, not a scalar** | **PROOF.md l.6437** | — |
| 5 | `C_1 := ((2L−1)/(L−1))·max{2.06N, 32N/κ_−}` — Theorem SUP-price | **SQ.md l.190** | **160** |
| 6 | `C_1 := (9/8)·5⁴·49√6·L⁴` | **SQ.md l.1587** | ≈ 1.8·10⁷ |
| 7 | the prefactor of the energy inequality (★) | **SQ.md l.1485** | SUPPLIED **20** (CONST_T l.292); computed **5699.63** (STAR_CONST l.412) |
| 8 | `C_1 := d^{(d−1)/2}Ĉ_1` — Green's-function first-difference constant | **GREENT.md l.288** | **54** |
| 9 | `C_1 := 2c_C·S_1·n_g·e^{μ_1r_g}` | **BFT_B.md l.228** | symbolic |
| 10 | `C_1 := 5κ̂/(L^{1−α} − 1)` | **BFT_B.md l.2632** | symbolic |
| 11 | `C_1 = 775` — Lemma LR-pot | **BFT_A.md l.1123** | 775 |
| 12 | `C_1 := C_SPD` | **BFT_A.md l.1554** | symbolic |
| 13 | `C_1 := 64K_𝔫c_yy_bgn'_cN_0√N` — **already renamed C_1^Q** | **SF.md l.1122**, renamed at **l.1123** | symbolic |
| 14 | `C_1` = the three-element SET {ζ_1−1, ζ_1, ζ_1+1} | **HW.md l.1918, l.1922** | a set |

**PROOF.md alone holds four of them (#1, #2, #3, #4); SQ.md holds three (#5, #6, #7).**
**The precedent is already in the lane**: SF.md l.1029 renames three of its own to C_1^Q/C_2^Q/C_3^Q
*"(they clash with Theorem CE's prefactor C_1 = 2κ_0B)"*. That is exactly R2, applied once.

**Live defect?** I looked for an inequality or substitution joining two of them and **found none**: each
is confined to one theorem's proof. **But there is a STALE VALUATION inside object #7, already on the
record and worth restating**: CONST_T.md built its whole §6.3 q_min table at the **SUPPLIED C_1 = 20**;
STAR_CONST.md l.412 then **computed C_1 = 5699.63** and, at l.470 of the same file, still quoted
CONST_T's `A_cγ_c = 236.9·C_1 = 4.7·10³ at C_1 = 20`. EPSSTAR §9.1 Y4 priced the consequence:
**1.348·10⁶, not 4.7·10³ — a factor 287**. That is a file quoting a number it had itself superseded
twelve pages earlier, and it is the same shape as §4.4. Recorded in §10 as a STALE VALUATION, not a
collision.

**Action: OWNER-GATED and NOT mechanical** — 540 lines, and object #4 is an operator, so a blind
string rename would be wrong. The affordable move, and the one I recommend: **a scope declaration at
the head of each owning section** (PROOF §…, SQ §0.3 / §15.1 / §15.2, BFT_A, BFT_B, GREENT), naming
which C_1 that section means, following SF.md l.1029's precedent. Full renaming is a session of its own.

### §6.2 **c_1 — FAMILY, at least ELEVEN objects, and two of them are dangerous**

| # | definition | DEFINED at | value |
|---|---|---|---|
| **1** | `c_1 := 1/(2(L² + 5.5A_d))` — KN-step's re-centring constant | **EXISTENCE.md l.1774**; declared **PLD.md l.42** | **1/117** |
| **2** | `c_1 := 1/(3.5·10⁶)` — Proposition PG's coercivity constant | **PROOF.md l.3629**, l.5324, l.5674; **LINEAR_PACKAGE.md l.354** | **2.857·10⁻⁷** |
| 3 | `c_1 := 5L/((L−1)κ_−)` — Lemma BL-3's shift | **BFT_A.md l.500** | symbolic |
| 4 | `c_1 := c_LI + c_f` | **HW.md l.1194** | symbolic |
| 5 | `c_1 = (X, X+e_μ)` — a coarse LINK label (c_1…c_4 of a plaquette) | **RLARGE.md l.967**; `checks/p5_criteria.md` l.15, `checks/c32_criteria.md` l.11 | a link |
| 6 | `c_1 := 1` — Lemma BB-W's marginal coefficient, "fixed, not fitted" | **BFT_B.md l.984, l.986** | 1 |
| 7 | `c_1(q̂)|q|^{−3}` — an angular coefficient function | **FLOW.md l.4133** | a function |
| 8 | `c_1 = 0.178 → 0.0188` — a transverse coefficient | **FLOW.md l.4770** | 0.178 |
| 9 | `c_1 = −1/12` — a rectangle weight | **PROOF.md l.1373** | −1/12 |
| 10 | `c_1 = d_1` — a combinatorial multiplicity | **PROOF.md l.2103** | integer |
| 11 | `log c_1 = 18190.95` — a Gaussian normalisation | **PLD.md l.2764** | — |

**The dangerous pair is #1 against #2.** Both are dimensionless O(10⁻⁷…10⁻²) constants written `c_1`,
both are *quoted across files* (PLD l.42 declares #1; LINEAR_PACKAGE l.354 declares #2), and **PROOF.md
carries both** — #1 at l.74 (`(L² + 5.5A_d)c_1 = ½ exactly`) and #2 at l.3629/5324/5674. They differ by
**×4.1·10⁴**, and #2 sets γ_i, which PROOF l.5674 names as the quantity with *"no cheap rigorous
improvement found"*. **I found no arithmetic that joins them** — this is a loaded gun, not a wound.

**Action: MECHANICAL for the two that matter.** Rename **#2 → `c_PG`** (PROOF already attributes it to
"Proposition PG" at l.3629 and l.5674 says *"γ_i is set by PG's c_1"*, so the name is the lane's own)
at **PROOF.md l.3629, l.5324, l.5674 and LINEAR_PACKAGE.md l.354** — four edits. Leave #1 as `c_1`
(it is the one PLD, EXISTENCE, ARS_FIX, EPS1_SWEEP and KN_ADOPT all use). The other nine are
file-local bound variables or labels; scope note only.

### §6.3 **θ_w — ONE glyph that must become TWO. OWNER-GATED.**

θ_w is the weight exponent of L^{θ_w(k−j)} (PROOF l.6732-6739). It is **not** two objects today; it is
one object that **must be split**, which makes it a rename problem of the same kind:

> **PROOF.md l.30 [S24-fix 3]:** *"BFT-1 must be restated with a WEIGHT PAIR. NORMS.md:
> A = L^{d − **θ_w^r** − 2θ_A}"*. **BFT_B.md l.4364:** *"BFT-1's maximal curvature weight is
> **θ_w^c = 2** (SESSION24_RESULTS, NORMS Part 4)"*. HANDOFF: *"With a single common θ_w there is no
> solution in (0, 2] for any consumer."*

The names θ_w^c and θ_w^r are already in use. **But the rename is not mechanical**: each of the 267
occurrences must be read to decide whether its slot is curvature or residual, and some (PROOF l.6105,
l.6746, l.6748, RLARGE l.76: "BFT-1 (θ_w = 0)") are statements *about the parameter* rather than uses
of it. **OWNER-GATED, for NORMS's and BFT_B's owners jointly.** This is the one sweep item that is on
the critical path rather than hygiene.

### §6.4 **a_η — ONE object, FOUR different constants. STALE VALUATION, priced.**

a_η is the exponent of (PLD-i)_k / (PLD)_k (i). Its **η_1² scaling is invariant; its constant is not**:

| form | where |
|---|---|
| **η_1²/(2N)** | RLARGE.md l.981 ((R5)'s inequality (B)), l.1026 (the bare-level value) |
| **a_kη_1²/16** | PLD.md l.197 |
| **a_dη_1²** | PLD.md l.276 |
| **49η_1²/(256σ_*²)** | PLD.md l.1044, l.1048 — the effective-level value a_RS actually names |

I reproduced the spread independently: at the Gaussian instance σ_*² = N(1 + 18/κ) = 38 (N = 2, κ = 1,
PLD l.341), 49/(256·38) = 5.037·10⁻³ against 1/(2N) = 0.25 — **a ratio of 49.63, i.e. 1.696 decades**,
confirming ARS_FIX §4.3's ×49.6 / 1.70 decades by my own arithmetic. **No sign changes anywhere**; the
a_RS margin moves from −15.617 to −17.313 decades depending on which constant is taken. **Action: a
single-valuation decision for RLARGE's and PLD's owners — state which a_η the ledger's a_RS uses.**

### §6.5 **κ (with κ_0, κ_±, κ̂) — FAMILY, at least FIVE objects for bare κ and THREE for κ_0**

Bare κ: the coupling-ratio bound in `g² ≤ κ` (RLARGE l.978, HIST l.159, PLD, ARS_FIX; κ ∈ {1, 0.25} at
PROOF l.3071); the polymer decay rate with `κ > 3κ_0 + 3 ≈ 457` (PROOF l.463, l.2062, l.2070; SF l.822
`κ := 273κ' + 1296w_8`); Balaban's large-field parameter `κ ≥ κ_0` (PROOF l.1298); a gauge group element
`κ := g_2g_1^{−1}` (BFT_B l.2678); and a scalar `κ := the constant μ(c_X)` (BFT_B l.4469); plus
`κ := 1 − δ_2 − …` (STAR_CONST l.318).
κ_0: **16 log 12800 ≈ 151.3** (LINEAR_PACKAGE l.299, PROOF l.463) vs **6.154034·10⁻⁴** (FLOW l.2860, an
integral) vs **1** (BFT_B l.3635, a level-0 coupling in the bb9 model).

**PROOF.md carries at least three bare-κ objects.** Spread: κ ≤ 1 against κ > 457 — **a factor ≥ 457
between two objects of the same glyph inside one file.** I found no expression joining them.
**Action: scope declaration per section. A rename over 3351 lines is not a session's work and I do not
propose one.** I record this as the lane's largest *unmanaged* glyph and the most likely home of the
next collision defect.

### §6.6 **C_3 — FAMILY, at least six objects**

HIST (a3-q)'s depth-uniform cone constant `E_𝒞(P)(ψ*) ≤ C_3δ²` (**HIST.md l.1669**, reference value 1,
used by TAUFLAT l.211 and EPS1_SWEEP l.453); SF's `C_3 := 16384S_Tn_bN_0³N^{3/2}/r_T³` (**SF.md l.1122**,
**already renamed C_3^Q** at l.1123/l.1205); BFT_A's `C_3 = 205` (**BFT_A.md l.1123**); FLOW's
log-divergent integral constant (**FLOW.md l.3581**); PROOF's Poincaré constant
`C_3 := sup_n max|f(s_0) − f̄|²/Σ|∇f|²` (**PROOF.md l.2857**). The ε_1^cut derivation
(4C_3ε_1² ≤ η_♭ at C_3 = 1) uses HIST's — **checked, correct object**. Action: scope note; SF's
precedent already covers its own.

### §6.7 Glyphs I checked and found **SINGLE** — the honest zeros

| glyph | the one defining form | DEFINED at | lines in lane |
|---|---|---|---|
| **a_RS** | `a_RS := min{a_η, κε_1²/(256N)}` | RLARGE.md l.1020 | 300 |
| **τ_♭** | `τ_♭ := min{τ_F, τ_R, θ_0^{SUP}/C′, ε_M/(C_DC′), θ_♯/C′, 1/(73.6Nc′²A′²)}` | SQ.md l.318 (= l.294) | 134 |
| **t_pr** | `t_pr = C′τ_♭` | REVIEW_SQ_S4 S4-15; HW.md l.182 | 206 |
| **ε_loc** | `ε_loc := min{ε_1/4, (ε_1²/(4Nb_1))^{1/2}}` | RLARGE.md l.907 | 101 |
| **ε_♭** | `ε_♭(D; Y) := min_{U°}[max_p‖1 − U°_p‖ + max_c‖V_c − S_c(U°)‖]` | RLARGE.md l.909 | 26 |
| **η_q** | `η_q := min{ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d}` | RLARGE.md l.64 | 135 |
| **C_Ω** | `C_Ω := C + 3(N² − 1)/2` | SF.md l.2073 | 100 |
| **m_τ** | least m with (L²/(2C_I))^m η_1 ≥ 2C_Iε_1/L² | PLD.md l.1097 | 49 |
| **η_♭, η_AE, η_U, ε_♮, ε^J_loc, ε_1^{gas}** | each one form | — | — |

**τ_♭ needs one caveat, not a rename:** "τ_♭ = τ_R" (REVIEW_SQ_S4 S4-14 item 1, SQ l.218-219) is an
**evaluation of a minimum at a superseded C_D**, not an identity — §4.3. The glyph is single; the
*number* behind it is the one that moved.

**m, θ (bare), C_2, A_0, B_0, G: NOT SWEPT.** I sampled each and all look like families, but single
Latin letters used as both indices and constants are not separable by my textual method at the
reliability the rest of this file is written to. I record them as **OPEN-NOT-SWEPT** rather than
claim a count. (θ in particular is used for the Chernoff tilt, for ‖1 − V_P‖, for the weight exponent
L^{θ(k−l)} and for the localisation error — and §4.1's objects 3 and 4 are its level-0 values.)

---

## §7. Counts, and what "classified" means here

| | |
|---|---|
| **Glyph families declared** | **11**: ε_*, θ_0, ε_1, η_1, C_1, c_1, κ (+κ_0), C_3, a_η (one object/four constants), θ_w (one object that must become two), and the SF-precedent families already renamed (B→B_LF, C_i→C_i^Q) |
| **Distinct objects found** | ε_* **4** (+1 level-indexed sub-family) · θ_0 **4** · ε_1 **6** · η_1 **3** · C_1 **≥13** · c_1 **≥11** · κ **≥5** (κ_0 **≥3**) · C_3 **≥6** |
| **Session 24's counts, corrected** | ε_* 4 ✓ · ε_1 5 → **6** (ε_1^{gas} is superscripted, so 5 colliding + 1 safe; I count the safe one) · η_1 3 ✓ · **θ_0 2 → 4** |
| **Use sites classified individually, by file:line** | **239** (η_1 57, ε_* 82, θ_0 32, ε_1 23 minority sites, sweep definitions 45) |
| **Sites classified at file level** | a further ≈1600, in the 20 files that provably contain exactly one object of their glyph. "Provably" = I grepped the file for every *defining* occurrence and read each; file-level classification is used only where exactly one defining form was found |
| **Sites marked AMBIGUOUS or WRONG** | **13** — PLD l.42 (wrong declaration), l.767, l.1048, l.1066, l.1211 (ambiguous), and the eight explicit `η_1 = c_1ε_1` mislabels |
| **LIVE DEFECTS (SYM-F1)** | **2** (§10) |
| **STALE VALUATIONS (F1-e)** | **4** (§10) |
| **Families where the rename is MECHANICAL** | θ_0, ε_1, ε_*, c_1 (the two that matter) |
| **Families where it is OWNER-GATED** | η_1 (one line), θ_w (every line), C_1, κ |
| **Checks run** | `checks/sy1_criteria.md` → `checks/sy1_symbols.py` → `checks/sy1_out.txt`; 6 pre-registered verdicts, all returned; **1 designed-FAIL control, which FAILED as designed** |

## §8. What this audit cannot catch (as pre-stated in §0.4, repeated so it is not lost)

(i) Two objects whose formulas agree today and diverge later. (ii) Collisions inside `checks/*.py`
variable names — I sampled `ar1_*`, `tf1_*`, `e1_*`, `sc1_*`, `c13_*`, `c31_*` and found the criteria
files already careful (e.g. `ar1_criteria.md` l.14 defines η_1^KN explicitly), but I did not sweep 736
files. (iii) LaTeX-vs-unicode variants: I grepped the unicode forms only; a `\eta_1` would be missed.
I checked for backslash forms of the four named glyphs and found **none** in the live `.md` set.
(iv) Glyphs with no definition anywhere. (v) **m, bare θ, C_2, A_0, B_0, G** — declared
**OPEN-NOT-SWEPT** in §6.7 rather than counted.

## §9. The three places I had to form a name

R4 says prefer a name already in use. Three objects had none:

1. **EXISTENCE.md l.2205's ε_1^{exp}** (a ±1 exponent on a loop word) → I propose **s_i**, the standard
   letter for a sign index; `ε_i` there is not a smallness parameter at all and no lane name exists.
2. **PLD.md l.1437 / PROOF.md l.6502's θ_0** (both "θ at level 0") → **θ^{(0)}**, formed from the
   lane's own level-superscript convention (ε_*^{(1)}, C_θ^{(i)}, 𝔠_∞^{(i)}, C_♭^{(i)} are all in use).
3. **PROOF/LINEAR_PACKAGE's c_1 = 1/(3.5·10⁶)** → **c_PG**, formed from the lane's own attribution
   (PROOF l.3629 *"Proposition PG at κ = 1"*; l.5674 *"γ_i is set by PG's c_1"*).

Everything else — η_1^RS, η_1^KN, η_1^gauge, θ_0^{SUP}, θ_0^{SQ4}, ε_1^{N2}, ε_1^{disc}, ε_*^{EPS-T},
ε_*^{BG-b}, ε_f, θ_w^c, θ_w^r, C_1^Q — is quoted from a file that already uses it.

---

## §10. LIVE DEFECTS (SYM-F1)

**Two live defects, and four stale valuations. Each states the wrong value, the right value, and what
changes. I stopped renaming through both live defects rather than carrying the rename over them.**

### SYM-F1 #1 — PLD.md l.1098: `m_τ = 3` is η_1^KN's number, asserted of η_1^RS's threshold

- **File:line of the wrong value:** **PLD.md l.1098**, repeated at **l.1206**, **l.1244**, **l.1260**.
- **Wrong:** `m_τ = 3` (and `m_τ = 3, 4, 5` for C_I = 1, 1.5, 2), carried into **l.1100**'s
  *"(PLD)_k at **RLARGE's thresholds** is an output of steps k, …, k + m_τ"*.
- **Right, at the threshold l.1100 names** (η_1^RS, ε_1 = 6.7·10⁻⁴⁰, N = 2, L = 3):
  **m_τ = 66 (C_I = 1), 90 (C_I = 1.5), 122 (C_I = 2)** — a factor **22 to 24.4**.
- **Mechanism:** l.1097's recursion substitutes **c_1** for the ratio η_1/ε_1. That ratio is a constant
  only for η_1^KN. For η_1^RS it is ε_1/(4608N), so m_τ is ε_1-dependent and grows as ε_1 falls.
- **What changes:** the look-ahead depth of PLD's architecture, and with it l.1210-1212's *"evaluating
  them after m_τ more steps changes no other step"* (already contradicted by REVIEW_PLD_S3 l.343) and
  l.1098-1099's ARGUED product structure across the m_τ levels, now asked to hold 22× further.
- **Evidence:** `checks/sy1_out.txt` SY1-1 (reproduces PLD's 3/4/5 at η_1^KN), SY1-2 (66/90/122 at
  η_1^RS), **SY1-3 designed-FAIL control FAILED as designed** and independently reproduced
  REVIEW_PLD_S3 l.435's 5/7/10 at ε_1 = 2.
- **Age:** found by REVIEW_PLD_S3 (Arch-3) l.345-350 — *"'m_τ = 3' is not RLARGE's number"* — and
  unfixed through PLD session 7. ARS_FIX §4.2 re-derived it in session 24.
- **Blocks:** the η_1 rename at PLD l.1096-1100 (§2.6).

### SYM-F1 #2 — HW.md l.604: a_bad quoted from a θ_0 figure SQ corrects four lines later

- **File:line of the wrong value:** **HW.md l.604** (and the θ_0 it rests on at **HW.md l.183**).
- **Wrong:** `a_bad = c_♭τ_♭² ≤ (1/640)(θ_0/C′)² ≈ **5·10⁻²³/C_D⁴**`, *"[arithmetic from SQ's stated
  θ_0 ≈ 10⁻⁸/C_D²]"*.
- **Right:** SQ.md **l.216** corrects l.212's figure — *"θ_0 ≈ 3·10⁻⁸/C_D² (the '10⁻⁸/C_D²' above is
  3× low)"* — and the same formula then gives **a_bad ≈ 5.00623·10⁻²²/C_D⁴**. HW is low by **×10.0 as
  displayed (×9 exactly; the extra 11% is HW's rounding of 5.56·10⁻²³ to 5·10⁻²³)**.
- **What changes:** nothing flips. a_bad is a suppression rate, so HW's figure under-states the
  suppression and every HW conclusion that uses it is conservative; the binding
  g_0² ≈ 2.5·10⁻¹⁵²/C_Ω ceiling (HW l.1758, l.2033, l.2183) is untouched. **It is still a constant
  quoted past the owning file's own correction, in the family whose collision cost 52 decades.**
- **Evidence:** `checks/sy1_out.txt` SY1-6, exact rationals; control at the stale value reproduces
  HW's 5.56·10⁻²³ to confirm the arithmetic path is HW's.

### STALE VALUATION #1 — ε_1 has four live numbers (§5.5)

1.27·10⁻³⁹ (SF l.2837, in a block SF itself calls *illustrative*), 9.52·10⁻⁴⁰ (RLARGE l.71),
8.95·10⁻⁴⁰ (RLARGE l.611), **6.7·10⁻⁴⁰ (RLARGE l.72, the headline)**. Spread ×1.90 in ε_1, ×3.59 in
a_bad. **NORMS.md l.746 quotes the illustrative 1.27·10⁻³⁹ as current**, without the caveat; NORMS's
own conclusion is qualitative so nothing of NORMS's breaks. Decision needed: one value, quoted once.

### STALE VALUATION #2 — a_η has four constants (§6.4)

η_1²/(2N) · a_kη_1²/16 · a_dη_1² · 49η_1²/(256σ_*²). Spread **1.696 decades** (reproduced here
independently). a_RS's margin reads −15.617 or −17.313 decades depending on the choice. No sign change.

### STALE VALUATION #3 — C_1 = 20 superseded by C_1 = 5699.63 inside STAR_CONST itself (§6.1)

STAR_CONST l.412 computes **C_1 = 5.70·10³**; STAR_CONST l.470 still quotes CONST_T's
`A_cγ_c = 236.9·C_1 = 4.7·10³ at C_1 = 20`. At its own C_1 the same expression is **1.348·10⁶**
(EPSSTAR §9.1 Y4) — **×287**. CONST_T's entire §6.3 q_min table is at the SUPPLIED 20.

### STALE VALUATION #4 — τ_♭ = τ_R is an evaluation at a superseded C_D (§4.3)

The 52-decade η_♭ error. **The number is corrected downstream** (3.52·10⁻⁸⁸ is what EPS1_SWEEP §4.5
uses); **the glyph collision that produced it is not**, and REVIEW_SQ_S4 S4-14 item 4's instruction to
rename one θ_0 — endorsed by TAUFLAT l.555 as *"the root cause … should be executed"* — is still
outstanding. §4.5's table executes it.

### What I did NOT find, said plainly

- **ε_* : ZERO live defects**, with the four searches of §3.4 named.
- **ε_1 : ZERO cross-object defects**, with the four searches of §5.4 named.
- **C_1, c_1, κ, C_3 : ZERO expressions joining two objects of one glyph**, searched for `min`/`max`
  over two, and for one supplied as the other's input. These are loaded guns, not wounds.
- The η_1 collision, although it is the worst in kind, has **not inflated a_RS**: RLARGE's ledger value
  5.93136·10⁻¹⁶⁶ is computed through RLARGE's own bare-level a_η = η_1²/(2N) at η_1^RS, not through
  PLD l.1048. **One live consequence (m_τ), not two.**

---

## §11. FOR OTHER FILES (not edited)

**Apply every rename by STRING MATCH inside the named file. Line numbers are locators only — §1.2:
PROOF.md's have moved by +79 since the session-24 files recorded theirs, and any other file edited
today will have moved too.**

Ordered by priority. Items marked **[BLOCKED]** must not be landed until the named defect is fixed.

### §11.1 For PLD.md's owner — the largest item, and two of them are not renames

1. **[BLOCKED — SYM-F1 #1] Fix m_τ before renaming §15.3.** l.1098's `m_τ = 3` is η_1^KN's number;
   at the threshold l.1100 names it is **66 / 90 / 122** (C_I = 1 / 1.5 / 2) at ε_1 = 6.7·10⁻⁴⁰.
   Either (a) restate l.1097-1100 as a statement about **η_1^KN** throughout, dropping the claim about
   "RLARGE's thresholds"; or (b) keep the claim and replace 3 by 66, which makes l.1210-1212's
   "changes no other step" a 66-level claim. Repeat at l.1206, l.1244, l.1260. **This is
   REVIEW_PLD_S3 (Arch-3), open since review cycle 3.**
2. **[BLOCKED — needs one word from you] l.1048.** *"At τ = η_1 this is RLARGE's (PLD)_k (i) … with
   a_η = 49η_1²/(256σ_*²)"* — is τ = **η_1^RS** or **η_1^KN**? RLARGE l.1021 takes a_η *from this
   line*. If η_1^KN, RLARGE's "a_η from (PLD)_k (i)" has no supplier at the threshold RLARGE needs
   (the bound at the coarser threshold does not imply the bound at the finer one). RLARGE's recorded
   a_RS = 5.93·10⁻¹⁶⁶ is safe either way (§2.7), so this is about what is written, not what is proved.
3. **Rename, mechanical once 1 and 2 are answered:** §2.6's table — l.42 (fix the declaration),
   l.50/197/202/276 → `η_1^RS`, l.767 → name both, l.772/1010/1066/1071/1077/1078/1096/1204/1211/1259
   → `η_1^KN`.
4. **l.1437:** `a_A^{(0)} = θ_0ε_1²/(2N)` → `θ^{(0)}` (your θ_0 is the level-0 Chernoff tilt, not SQ's
   threshold; §4.1 object 3).
5. **Scope note for §… :** `ε_*` in PLD (l.1022, l.1131, l.1132) is **N5-sf0's**; say so once.

### §11.2 For SQ.md's owner — the rename that a review ordered two cycles ago

1. **Execute REVIEW_SQ_S4 S4-14 item 4.** §4.5's table: l.183, **188**, 210, 212, 216, 217, 218, 219,
   225, 231, 294, 306, 318, 342, 557, 930 → **`θ_0^{SUP}`**; l.**1167**, 1168, 1357, **1622**, 1623,
   1628, 1633, 1634 → **`θ_0^{SQ4}`**. **Mechanical; no ambiguous site; I checked each line.** TAUFLAT
   l.555 calls this *"the root cause"* of the 52-decade error.
2. **l.1679-1685:** `η_1 := η_U/2` → **`η_1^gauge`** (6 strings, §2.6). η_1 is a lane-wide quantity
   owned by RLARGE; a bound variable should not take its letter.
3. **§3.5, and it is a statement question, not a rename.** (EPS-0a) is stated twice with ε_* at two
   normalisations: l.1171 (`Σ|𝒫|² ≤ ε_*`, `R³sup|𝒮| ≤ ε_*^{1/2}`) against l.1512 (`Σ|𝒫|² ≤ ε_*²/16`,
   `≤ ε_*/16`). **Only l.1512's form is proved**; l.1171's is strictly stronger as a claim. Either
   write `ε_*^{(13.5)} := (ε_*^{EPS-T})²/16` at l.1171 or restate l.1171 in l.1512's normalisation.
4. **Scope notes:** SQ holds **three** C_1 (l.190 = 160, l.1485 = the (★) prefactor, l.1587) — name
   each at the head of its section, as SF.md l.1029 does.
5. **l.212/l.216:** HW.md quotes l.212's superseded `10⁻⁸/C_D²` (§10 SYM-F1 #2). Consider striking
   l.212's figure rather than correcting it four lines later.

### §11.3 For HW.md's owner — one value fix, two renames

1. **[SYM-F1 #2] l.604:** `a_bad ≈ 5·10⁻²³/C_D⁴` → **`≈ 5.01·10⁻²²/C_D⁴`**, and l.183's
   `SQ's θ_0 ≈ 10⁻⁸/C_D²` → `SQ's θ_0^{SUP} ≈ 3·10⁻⁸/C_D² (SQ.md l.216; l.212's figure is 3× low)`.
   The direction is conservative, so nothing of yours flips — but the constant is wrong by ×9.
2. Same two lines: `θ_0` → `θ_0^{SUP}`.
3. `ε_1^{gas}` at l.1444 is correctly superscripted; no change. `C_1` at l.1918/l.1922 is a **set**,
   not a constant — worth a word, since every other C_1 in the lane is a number.

### §11.4 For RLARGE.md's owner

1. **No η_1 rename needed** — all 16 sites are η_1^RS (R1). Add one scope line to §0's threshold
   block: *"η_1 in this file is always (R3)'s η_1^RS; KN-step's η_1^KN = c_1ε_1 is a different symbol
   (EXISTENCE l.1771) and PLD §15 uses that one."* That line is what stops this recurring.
2. **l.65's ordering is object-specific.** *"η_1 ≤ η_q"* is **true of η_1^RS** (ratio 3.35·10⁻⁴⁰) and
   **false of η_1^KN by ×39.3846 (N = 2) / ×59.0769 (N = 3)** — exact ratio **512/13**, reproduced
   three independent ways (`sy1_out.txt` SY1-4; ARS_FIX §5.1; REVIEW_PLD_S3 l.433). If the KN adoption
   lands, l.65 and HIST l.186's route-superiority claim both reverse. Add the conditional now.
3. **ε_1 single-valuation (STALE VALUATION #1).** Four live numbers; l.72's **6.7·10⁻⁴⁰** is the
   headline. Mark l.71's 9.52·10⁻⁴⁰ and l.611's 8.95·10⁻⁴⁰ as superseded where they stand.
4. **a_η single-valuation (STALE VALUATION #2).** l.1020-1021 says *"a_η from (PLD)_k (i)"*; PLD offers
   three different constants for it (l.197, l.276, l.1048). State which one a_RS's ledger value uses.
   (I verified it is RLARGE's own bare-level η_1²/(2N) — so say that.)

### §11.5 For PROOF.md's owner / the lead

1. **Rename ε_*^{BG-b}, 12 strings:** l.410, **1838**, 1839, 1854, 1919, 1922, 1939, 1949, 1950, 1953,
   2252, 2375 → `ε_*^{BG-b}`. Leaves N5-sf0's ε_* (27 sites) and ε_*^{(i)} untouched. Mechanical.
2. **l.6502:** `CURV1_0 at θ_0` → `θ^{(0)}`.
3. **Rename c_PG, 3 strings:** l.3629, l.5324, l.5674 — `c_1 := 1/(3.5·10⁶)` → `c_PG := 1/(3.5·10⁶)`.
   PROOF currently holds both this and KN-step's c_1 = 1/117 (l.74), differing by ×4.1·10⁴.
4. **Record the +79 line drift (§1.2).** Every cross-file citation into PROOF.md written before the
   session-24 header is off by 79 lines, including EPSSTAR §6.1's l.5494/l.5544/l.1759. A future
   worker following those pointers lands in unrelated text.
5. **Correct the session-24 header's own count:** l.52 and l.6894 say *"two distinct θ_0"*; there are
   **four** (§4.1) — PLD l.1437 and PROOF l.6502 are two more. l.53's *"at least FIVE ε_1"* is right.
6. **Scope notes for C_1 (4 objects in PROOF) and κ (3 objects in PROOF)**, following SF.md l.1029.

### §11.6 For BFT_B.md's owner

1. **`ε_1` → `ε_1^{N2}`, 17 strings** (l.2773, 2870, 2871, 2909, 2927, 3055, **3058**, 3059, 3077,
   3105, 3148, 3229, 3276, 3311, 3312, 3429, 4600), and `𝒦(ε_1)` → `𝒦(ε_1^{N2})`. **Reason (§5.3):
   your threshold is an explicit O(1) formula and RLARGE's is ≈10⁻⁴⁰, and (N2-0)_j is phrased in the
   same words as RLARGE l.130. The option-C ε_1 move is live this session.** This is the one ε_1
   rename that is urgent rather than hygienic.
2. **`ε_*` → `ε_f^{max}`, 6 strings** (l.**2719**, 2721, 2722, 2733, 3151, 3155). Your file also holds
   N5-sf0's ε_* at l.885-886, already written `ε_*(R)`; leave that.
3. **θ_w:** l.4364 already uses θ_w^c; the other 14 sites need the §6.3 split.

### §11.7 For FLOW.md's owner

`ε_1` → `ε_1^{disc}` at l.1927, 1931, 2834, 3000; at l.771 the mode amplitudes `ε_1, ε_2` →
`ε^{mode}_1, ε^{mode}_2`. Five strings, mechanical. FLOW also holds three `c_1` objects (l.4133,
l.4770, and l.1661's check output) — scope note.

### §11.8 For EXISTENCE.md's owner

1. **l.1771:** rewrite as *"from η_1^RS = min{ε_1/(2L²), ε_1²/(512NA_d)} … to η_1^KN := c_1ε_1"*;
   **l.1804:** `the fixed η_1` → `the fixed η_1^RS`. Your file defines one and refers to the other.
2. **l.2205:** `C = c_1^{ε_1}⋯c_ℓ^{ε_ℓ}` → `C = c_1^{s_1}⋯c_ℓ^{s_ℓ}` (s_i = ±1). Here `ε_i` is a sign
   index, and `c_1` is a loop letter — both collide with lane constants in the same expression.

### §11.9 For LINEAR_PACKAGE.md's owner — **errata class only (v1.1 is frozen)**

l.35 and l.182: `ε_*` → `ε_*^{BG-b}`; l.354: `c_1 := 1/(3.5·10⁶)` → `c_PG`. Both are consistency
errata of exactly the kind l.35 already performs for B → B_LF (*"renamed here because B in Theorem 5.1
is a different constant"*) — **that line is the precedent this whole file is built on.**

### §11.10 For NORMS.md's and SF.md's owners

- **NORMS l.746** quotes SF l.2837's **1.27·10⁻³⁹** as the current ε_1; SF l.2834 labels that block
  *"illustrative in the unevaluated constants"*, and RLARGE l.72's headline is 6.7·10⁻⁴⁰. Your
  k-independence conclusion is qualitative and does not break — add the caveat or requote.
- **NORMS**: 52 θ_w sites, the largest single holding; the §6.3 split is mostly yours.
- **SF**: your l.1029/l.1123 C_i^Q rename is the lane's model for §6.1 and §6.6. No change asked.

### §11.11 For RTARGET.md and the lead

- **l.219's `ε_*`** is BG-b's, not N5-sf0's → `ε_*^{BG-b}`.
- **§53 item 1 and §54's T55-C** say *"2 θ_0"*; the count is **4**.

### §11.12 For every REVIEW_*.md and *_snapshot.md — **ANNOTATE, DO NOT RENAME**

A review is a dated audit of the text as it then stood and a snapshot is frozen history; renaming
either falsifies the record. Two annotations are worth adding as footnotes, not edits:

- **REVIEW_SQ_S4 l.314 (S4-14 item 2):** η_♭ ≈ 4.2·10⁻³⁶ is computed at τ_♭ = τ_R, valid only for
  C_D ≤ 455.283301; at the C_D that **item 16 of the same review** produces (≈4.76·10¹⁵) it is
  **3.52·10⁻⁸⁸**. (Adjudicated by TAUFLAT §2; reproduced here at `sy1_out.txt` SY1-5.)
- **REVIEW_PLD_S3 (Arch-3) l.345-350** is correct and still unimplemented; §10 SYM-F1 #1.

---

## §12. Status of this file

| item | status |
|---|---|
| The four named families enumerated, defined, and their use sites classified | **COMPUTED (reading), with every defining line quoted and verified against the owning file** |
| θ_0's count corrected from 2 to 4 | **COMPUTED (reading)** |
| SYM-F1 #1 (m_τ = 3 vs 66) | **LIVE DEFECT**, exact arithmetic, designed-FAIL control run and failed as designed |
| SYM-F1 #2 (HW's a_bad ×9) | **LIVE DEFECT**, exact arithmetic |
| Four stale valuations | **STALE VALUATION**, each priced |
| θ_0, ε_1, ε_*, c_PG rename tables | **MECHANICAL** — landable as written |
| η_1 rename table | **OWNER-GATED on one line (PLD l.1048) and blocked on one defect (PLD l.1098)** |
| θ_w split, C_1, κ | **OWNER-GATED**; for C_1 and κ I recommend scope declarations, not renames, and say why |
| m, bare θ, C_2, A_0, B_0, G | **OPEN-NOT-SWEPT** — not counted, not claimed |
| New mathematics claimed | **none** |

---

## §13. CORRECTION, appended 2026-10-28T21:29Z — **PROOF.md's line numbers moved AGAIN, during this audit**

Rule 8 is append-only, so the tables above stand as written and this section corrects them.

**PROOF.md was edited between my first pass (21:08Z, 6905 lines) and my verification pass (21:28Z,
6930 lines). Every PROOF.md line number in §3, §4, §6 and §11.5 is 25 too small.** I re-verified every
other file I give a table for — SQ, PLD, RLARGE, HW, BFT_B, FLOW, NORMS, SF, LINEAR_PACKAGE,
EXISTENCE, RTARGET — by reading the cited line and matching the string: **all correct, none moved.**

> **So PROOF.md has moved twice in the time it took to audit it: +79 since the session-24 files cited
> it, then +25 during this session. A rename applied to PROOF.md by line number will be wrong by the
> time it is applied. Use the strings.** This is no longer a caveat; it is the operating instruction
> for PROOF.md, and it is why every table above carries the old string.

### §13.1 PROOF.md line numbers, re-verified at 2026-10-28T21:28Z (6930 lines)

| object | §-above said | **current** |
|---|---|---|
| ε_*^{BG-b} — definition | l.1838 | **l.1863** |
| ε_*^{BG-b} — all 12 sites | 410, 1838, 1839, 1854, 1919, 1922, 1939, 1949, 1950, 1953, 2252, 2375 | **435, 1863, 1864, 1879, 1944, 1947, 1964, 1974, 1975, 1978, 2277, 2400** |
| ε_* (N5-sf0) — definition | l.5573 | **l.5598** |
| ε_* (N5-sf0) — sites | 129, 225, 226, 5559-6718 | **154, 250, 251, 5584, 5585, 5590, 5598, 5602, 5640, 5642, 5648, 5651, 5658, 5787, 5802, 5804, 5869, 5871, 5884, 5892, 6126, 6324, 6327, 6335, 6743** |
| ε_*^{(i)} sub-family | 6029-6047, 6155 | **6054-6072, 6180** |
| θ^{(0)} (CURV-F2″) | l.6502 | **l.6527** |
| C_1 #1 (`:= 2κ_0B`) | l.2066, l.2433 | **l.2091, l.2458** |
| C_1 #2 (`:= L²+4cA_L`) | l.3982 | **l.4007** |
| C_1 #3 (`= C(R_0)`) | l.1949 | **l.1974** |
| C_1 #4 (the **operator**) | l.6437 | **l.6462** |
| c_PG (`c_1 := 1/(3.5·10⁶)`) | l.3629, l.5324, l.5674 | **l.3654, l.3667, l.5349, l.5699, l.6087** |
| κ (polymer, > 457) | l.463, l.2062, l.2070 | **l.488, l.2087, l.2095** |
| κ (coupling, ∈ {1, 0.25}) | l.3071 | **l.3096** |
| session-24 header's own θ_0/ε_* flags | l.52, 88-90, 92, 94-96, 6894 | **l.77, 113-115, 117, 119-121, 6919** |

### §13.2 One correction to §6.2 on the merits, not just the locator

**c_PG has FIVE sites in PROOF.md, not three.** I missed `γ_i is set by PG's c_1 = 1/(3.5·10⁶)` at the
current **l.5699** and the second occurrence inside l.3654's own paragraph at **l.3667**, and there is a
fifth at **l.6087** (*"Lemma E-low's c_E and PG's c_1"*). Full rename list for §11.5 item 3:
**PROOF.md l.3654, 3667, 5349, 5699, 6087 — five strings — plus LINEAR_PACKAGE.md l.354.**

### §13.3 What this does to the audit's own reliability, stated rather than left implied

Everything I classified in PROOF.md I classified by reading the line, and the strings are quoted, so
the classifications survive the drift. What does **not** survive is any reader who follows a bare line
number. **Three of the four files that cite PROOF.md by line (EPSSTAR, REVIEW_RLARGE_V2, NORMS) are
already pointing at the wrong text today** — EPSSTAR §6.1's l.5494 now lands in Theorem RW's partition
discussion, 104 lines from the ε_* definition it means. That is a lane-wide hygiene defect of the same
kind as a symbol collision: a pointer that silently resolves to the wrong object. **Recommended to the
lead: cross-file citations into PROOF.md should quote a string or a section label, not a line.**

### §13.4 One row of §13.1 was wrong, and I correct it here rather than leave it

The session-24 header's own flag lines did **not** shift by +25: the header itself grew, so the drift
inside it is **+8**, not +25. Re-verified by string at 21:32Z:

| flag | §13.1 said | **actual** |
|---|---|---|
| *"**two** distinct θ_0 … 52-decade τ_♭ error"* | l.77 | **l.60** |
| *"at least FIVE distinct ε_1"* | — | **l.61** |
| *"η_1 is THREE symbols"* | — | **l.66** |
| *"[S24-flag 2] … FOUR distinct symbols are called ε_*"* | l.113-115 | **l.96** |
| *"S4-14 item 2 computes η_♭ ≈ 4.2e-36"* | l.119-121 | **l.103** |
| the closing three-defects paragraph | l.6919 | **l.6919** ✓ |

**The drift inside one file is not uniform.** I asserted +25 across PROOF.md from four verified samples
in the body; it holds in the body (l.488, l.2087, l.2095, l.3096, l.1863, l.5598, l.6462, l.6527,
l.3654, l.6919 all check) and **fails in the header**, because the header is where the growth happened.
That is exactly the trap: a uniform-offset correction is itself a line-number assumption.
**Operating rule, final form: for PROOF.md, locate by string. Never by line, and never by offset.**

§11.11's item for the lead stands and gains a second clause: **PROOF.md l.60 and l.6919 say "two
distinct θ_0"; the count is four** (§4.1 — PLD.md l.1437's level-0 Chernoff tilt and PROOF.md l.6527's
level-0 localisation error are two more).
