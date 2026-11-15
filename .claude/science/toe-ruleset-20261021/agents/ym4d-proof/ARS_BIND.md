# ARS_BIND — does a_RS bind anything on the live RLF-step v3 route?

Worker file for target **T55-M**, session 25. Owner: this worker. Append-only.

---

## §0. PRE-STATED (first edit, 2026-10-28T21:34:24Z)

This is the first edit to this file. It is written **before any derivation, any grep, any script, and
before reading RLARGE §3.5**. It contains statements only. It cites nothing produced in session 25.

### §0.1 The question

`RLARGE.md` defines a constant **a_RS** (the Russakovskii/re-centring exponent of the RS route) and a
companion **c_RS**. Two session-24 files — `ARS_FIX.md` and `EPS1_SWEEP.md` — are built on the premise
that *a_RS binds today*, i.e. that some live smallness condition or counted item of the RLF-step **v3**
route consumes a_RS, and that at today's constants the resulting requirement breaches an available
ceiling by ≈ 15.6 decades. `ARS_FIX.md` l.304 raises, but does not answer, whether v3 intends a_RS to
enter **no** smallness condition at all.

**The decidable question:** *is there, today, on the live v3 route, at least one item whose validity
depends on the value of a_RS?*

### §0.2 Pre-stated targets (statements only)

- **(M1)** Enumerate **every** occurrence in the lane of `a_RS`, `a_♯`/`a_sharp`, `n_♯`/`n_sharp`,
  `c_RS`, and of the *numeric value* of a_RS where the symbol is absent. For each, classify as
  **LIVE-v3**, **FROZEN** (v1/v2 snapshot, Appendix A frozen content, superseded §), or
  **COMMENTARY** (prose about the constant, not a consumer).
- **(M2)** Define "consumer" **before** looking: an occurrence C is a *consumer of a_RS* iff the truth
  of some statement that the live v3 route asserts or requires would change if a_RS were replaced by a
  different positive real, all else fixed. Mere appearance in a definition, a table, a comparison, or a
  discarded branch is **not** consumption.
- **(M3)** Read `RLARGE.md` §3.5 (l.433-439), l.1024, l.1183-1186, l.832 and l.835 in full context and
  determine, **by quotation**, what each actually says. Four quotations attributed to these lines by a
  session-25 review are to be checked verbatim; the review is itself unreviewed and may be wrong in
  either direction.
- **(M4)** Examine `RLARGE.md` l.830 specifically. If a_RS appears there with the **opposite** sign
  (i.e. as a factor `e^{a_RS R}` that *helps* rather than costs), determine whether l.830 is on the live
  v3 route, and whether that site alone constitutes consumption in the sense of (M2). Determine the
  standing hypothesis under which the l.830 correction is bounded, and what happens without it.
- **(M5)** Attempt, in good faith, to **construct a consumer**. "a_RS is not consumed" is a negative
  claim and gets the scrutiny of a positive theorem. The construction attempt is to be made from v3's
  own stated requirements, not from the reviewer's framing. Report the attempt and whether it succeeds.
- **(M6)** Conditional on the (M1)-(M5) verdict, state what becomes of:
  (a) `EPS1_SWEEP.md`'s condition **(C2)**, in particular its second horn (*"record that the RS/joint
      route's ceiling already sits 15.62 decades below DX′"*);
  (b) `RLARGE.md` l.618's "false sentence today" claim;
  (c) `ARS_FIX.md`'s and `EPS1_SWEEP.md`'s headline findings.
  Each of (a)-(c) is to be given an explicit status word, including "about nothing" if that is the case.
- **(M7)** Independently verify the claim that **HIST's Lemma RS-lin is PROVEN-HERE at `RLARGE.md`
  l.628**, set in RLARGE §6's own setting, delivering a linear threshold by the same re-centring
  mechanism. Three sub-questions, each answered separately: (i) is the PROVEN-HERE genuine — is a
  complete proof written out from stated hypotheses, or is it a label? (ii) is RS-lin on the **live v3**
  route or in frozen/superseded material? (iii) does anything — a hypothesis, a quantifier, a
  dependence on an object v3 does not have — prevent the lane from simply using it?
  **This target is not conditional on the a_RS verdict and is to be answered even if (M1)-(M5) are
  inconclusive.** If RS-lin is proven and live, whether a_RS binds matters much less.
- **(M8)** Apply the binding defect-2 rule throughout: an inequality binds only at the constants it was
  evaluated at. For every "breach by X decades" encountered, record the constants it was evaluated at
  and whether each is still an **input** today or has since become an **output**.
- **(M9)** Apply the binding defect-1 rule: before comparing or combining any symbol, verify by
  file:line which object it is. `c_1` and `κ` are known to be multiply-overloaded in this material;
  a_RS is believed single-object but that belief is to be spot-checked, not assumed.

### §0.3 Pre-stated verdict forms

Exactly one of the following is to be asserted in §9, with no hedging:

- **(V-YES)** a_RS binds on the live v3 route. *Then*: the consumer is named by `file:line`, the
  statement it makes is quoted, and the session-25 review's item 3 is itself wrong.
- **(V-NO)** a_RS binds nothing on the live v3 route. *Then*: the 15.6-decade breach is against a
  quantity nothing reads; the construction attempt of (M5) is reported as having failed and **why**;
  and (M6)(a)-(c) are discharged as about-nothing to the extent they are.
- **(V-SPLIT)** a_RS binds only via a site that is itself conditional on a standing hypothesis. *Then*:
  the site, the hypothesis, and the consequence of dropping the hypothesis are all named.

### §0.4 Pre-stated failure modes for this worker

- **M-F1.** I read "not consumed" as a global statement when RLARGE scopes it to a *particular counted
  family* (e.g. "no **counted item**" ≠ "no item"). Guard: quote the quantifier, not the sentence.
- **M-F2.** I classify a site as FROZEN because it sits under a v1 heading, when a v3 reading note
  re-adopts it. Guard: for every FROZEN classification, check whether a v3 reading note covers it.
- **M-F3.** I conflate "a_RS is not consumed" with "the RS route is dead". They are different claims;
  the RS route can be live and still not consume a_RS, if v3 uses a different exponent for it.
- **M-F4.** I accept RS-lin's PROVEN-HERE as a certificate (the banked-review defect) instead of
  reading the proof. Guard: (M7)(i) requires me to read the body, not the label.
- **M-F5.** The search misses a consumer because the symbol is spelled differently (`a_{RS}`, `a_RS'`,
  `aRS`, unicode sharp vs `#`). Guard: (M1) searches value-substitutions too, and I enumerate the
  spellings I searched.
- **M-F6.** I pronounce on l.830 without checking whether its standing hypothesis g_K² ≤ 1/(2R) is
  itself live, and so give a verdict conditional on something already dead or already discharged.

### §0.5 Checks

Any numeric check gets `checks/ab1_<id>_criteria.md` written **before** the script, with pre-registered
PASS/FAIL verdicts and a **designed-FAIL control**. Arithmetic is exact rational in plain python. No
numeric lock will be taken (no BLAS, no array work).

### §0.6 Scope

Writes: this file and `checks/ab1_*` only. Reads: anything. No git.

---

## §1. Method and what §0's targets became

Order of work, for the record: §0 (PRE-STATED) → forward trace (M1) → verbatim reading (M3, M4) →
construction attempt (M5) → `checks/ab1_criteria.md` → `checks/ab1_margins.py` → §6-§9. Nothing below
was written before §0. The only numeric work is exact rational arithmetic in plain python; no numeric
lock was taken.

Spellings searched for (M-F5): `a_RS`, `a_{RS}`, `aRS`, `a_♯`, `a_sharp`, `a_\sharp`, `n_♯`,
`n_sharp`, `c_RS`, `e^{a_RS`, plus value-substitution searches on `256N`, `η_1²/(2N)`,
`5.93`, and the whole-lane symbol counts recorded in §2.1.

---

## §2. (M1) Forward trace: every occurrence of a_RS in the lane, classified

### §2.1 Whole-lane census

`a_RS` occurs in 21 files. Eleven are session-24/25 working files or reviews **about** the question
(`ARS_FIX`, `EPS1_SWEEP`, `EPS1_EXEC`, `KN_ADOPT`, `REVIEW_ARS_EPS_S1`, `SYMBOLS`, `SESSION24_RESULTS`,
`SESSION25_RESULTS`, `RTARGET`, `LOG`, `FLOW_LOG`), three are frozen snapshots
(`RLARGE_v1_snapshot`, `RLARGE_v2_snapshot`, `RLARGE_session17_snapshot`), one is a review of a
superseded version (`REVIEW_FLOW_S1_S2`, `REVIEW_S16_S17`, `REVIEW_SF_S5`). **Four files carry it in
substantive text: `RLARGE.md` (5), `FLOW.md` (3), `PROOF.md` (6), `SF.md` (1).**

**The decisive negative:** `a_RS` occurs **zero times** in `HIST.md`, `HW.md`, `PLD.md`, `SQ.md`,
`BFT_A.md`, `BFT_B.md`, `NORMS.md`, `LINEAR_PACKAGE.md`. Those are the files that carry the live v3
route's mathematics. The symbol never reaches them.

### §2.2 `RLARGE.md` — all five occurrences, and where they sit

`RLARGE.md` is 1267 lines. **Appendix A ("Frozen and one-step content of v1 (§3-§9A), verbatim from
`RLARGE_v1_snapshot.md`") begins at l.824.** The live v3 body is l.1-823.

| line | text | section | class |
|---|---|---|---|
| **830** | *"**§6 Lemma RS:** "1/g_i² ≥ 1/g_{i+1}² under (F)" is not implied by (F_R): factor e^{a_RS R} (§0, F-mono)."* | Appendix A **v3 reading note** | **LIVE TEXT**, commentary on frozen §6 — see §4 |
| **1020** | *"a_RS := min{a_η, κε_1²/(256N)} (the two branches of Lemma RS at effective levels; a_η from (PLD)_k (i))"* | App. A §7.1, `[R1617-fix R-8, R-10]` | FROZEN; **superseded by l.832** |
| **1023** | *"(Ce^{-a_RS/g_k²})^{n/c_RS} ≤ (Ce^{-a_RS/g_{k+1}²})^{n/c_RS}"* | App. A §7.1, inside the c_RS := 5⁴ justification | FROZEN; **superseded by l.832 and l.435** |
| **1024** | *"**a_♯ := min{a'', a_♭, a_RS/c_RS}, n_♯ := ⌊4/(a_♯β_-)⌋ ≥ n_*.**"* | App. A §7.1 | FROZEN; **superseded by l.832** |
| **1247** | *"After R-8 the exponent that matters is a_♯ = min{a'', a_♭, a_RS/c_RS} …"* | App. A §9, check **c32's record** | FROZEN RECORD; reading note l.837-839 calls c32's numerics *"illustrative only"* |

**Not one of the five is in the live body l.1-823.** The claim at `REVIEW_ARS_EPS_S1` that "a_RS
reaches a ceiling only via a_♯ (l.1024)" is an inference; I have now verified it exhaustively — there
is no other arithmetic path from a_RS to anything.

### §2.3 What the live body puts in a_RS's place, by name

- **`RLARGE.md` l.87-89 (§0, "The defect exponent"):** *"The unreturned per-defect exponent is
  **a := min{θa_bad, a_A}**, **a_bad := c_pr·min{ε_1², t_pr²}** (HW Lemma W-bad)"*; and l.94:
  ***"v2's a_♯ formula (§3.4) is superseded for unreturned defects (§3.5)."***
- **l.414 (§3.3, the HW net):** *"with **a = θa_bad**"*; l.398 pins **a_A ≥ θa_bad** inside (SDP)^A,
  so the min is θa_bad.
- **l.545 (end of §4.3, RLF-step v3):** ***"Constants (C_ℓ, B_0, E_0, a, n_♯) are the same at every
  level"*** — the live constant list. **No a_RS, no a_♯, no c_RS.**
- **l.586-587 (§5.2):** n_H := ⌊(4 + c_B)/(aβ_-)⌋, and l.590 ***"[v3-3′] a is HW's a =
  min{θa_bad, a_A}, not v2's a_♯."***
- **l.829 (Appendix A reading note on §3):** the cutoff is *"n_♯ ≥ max{n^J_*, n_H} with n_H from
  **v3's a** (§5.2)"* — so v3 keeps the **name** n_♯ but takes its defining requirement from **a**,
  not from a_♯. (Recorded as a collision in §8.)

### §2.4 The one place a_RS is still read downstream, and why it is not a consumer

`EXISTENCE.md` (live) uses **a_♯** at l.1882-1886, l.3072-3083, l.3362-3403. It never uses the
**formula** a_♯ = min{a'', a_♭, a_RS/c_RS}; every statement is of the form "with exponent a_♯" and
holds for any positive exponent obeying (n_♯+1)a_♯β_- > 4. `RLARGE.md` l.767 already says
***"The exponent EXISTENCE should read is a (not a_♯)"***, and §8's **U11/K8** is the open item to
confirm it. So this is a **stale label on the live existence lane**, not a consumption of a_RS's
value. Flagged in "FOR OTHER FILES".

`SF.md` l.2204's single hit is a sensitivity-table cell (*"a_RS ∝ η_1² ≈ 6·10⁻⁴¹⁶"* at N = 3) —
commentary. `PROOF.md`'s six hits are all `[S24-flag 6]` and `[S25-fix 1]`, i.e. the claim under test.

---

## §3. (M3) The four quotations, checked verbatim. Three hold; one is truncated; the grep claim is wrong

I read l.433-439, l.832, l.835, l.1024 and l.1183-1186 in full context.

| # | as attributed by `REVIEW_ARS_EPS_S1` §1 item 3 | what the file actually says | verdict |
|---|---|---|---|
| 1 | §3.5 says the `a_♯ := min{…}` formula is *"not consumed"* | l.434-435: *"the case split …, the greedy disjointness factors 7⁴, 81, 5⁴, RS-joint's c_RS = 81 ⇐ (PLD-q)_k, and the **a_♯ := min{…}/greedy formula are not consumed**"* | **HOLDS** (the file writes "/greedy"; immaterial) |
| 2 | *"the exponent of unreturned defects is a = min{θa_bad, a_A}"* | l.438: *"The exponent of unreturned defects is a = min{θa_bad, a_A} (§0)."* | **HOLDS verbatim** |
| 3 | *"No counted item depends on a_♯ or n_♯"* **stands** | l.438-439: *"v2's remark "No counted item depends on a_♯ or n_♯" stands **for the frozen lemmas** (R1/R1^J hold for every cutoff n_c ≥ n_*, n^J_*)."* | **TRUNCATED** — see below |
| 4 | l.835 calls §7.3 *"not used by RLF-step v3"* | l.835: *"**§7.3 Theorem TS, §7.4:** frozen-background shadow; not used by RLF-step v3."* | **HOLDS verbatim** |

**On #3 (my pre-stated failure mode M-F1).** The review dropped a scope clause, and the clause it
dropped narrows the remark to the frozen lemmas. Reported as a defect. **It does not reverse the
conclusion**, and the reason must be stated rather than assumed: the live-route content is carried by
#1 and #2, not by #3. #3's job in §3.5 is only to say that the *frozen* lemmas R1/R1^J — which do
mention a_♯ — have no counted item depending on it, because they hold for every cutoff n_c ≥ n_*.
Read correctly, #1 + #2 + #3 together say: **a_♯ is not used live, and where it is still written
(frozen), nothing counted depends on it.** That is stronger than the truncated form, not weaker.

**The grep claim is wrong as stated.** The review says *"Neither ARS_FIX nor EPS1_SWEEP cites §3.5,
l.435, l.438 or l.835 — grep returns zero hits in both."* Token by token:

| token | `ARS_FIX.md` | `EPS1_SWEEP.md` |
|---|---|---|
| `§3.5` | **2** (l.294, l.788) | 0 |
| `l.435` / `l.438` / `l.835` | 0 / 0 / 0 | 0 / 0 / 0 |
| `not consumed` | 0 | 0 |
| `min{θa_bad` | **1** (l.294) | 0 |

So the accurate statement is: *neither file cites l.435, l.438 or l.835, and neither contains the
phrase "not consumed"; `ARS_FIX` names §3.5 twice, but only inside its own quotation of l.832, and
never reads §3.5's body.* **This correction makes `ARS_FIX`'s position worse, not better.** At l.293-294
`ARS_FIX` quotes l.832 *including the replacement exponent* — *"superseded by §3.5 and §5.2
**(a = min{θa_bad, a_A})**"* — and then concludes at l.302-304 that a_RS binds. The failure was not
missing the pointer. It was quoting the replacement and not following it.

**Fifth site, l.1183-1186 ((TS-c)).** The review's reading is right about what (TS-c) is and right
that l.835 excludes §7.3; `RLARGE.md` l.517 independently lists *"Theorem TS / TS_K"* among the
**"Not hypotheses of RLF-step v3"**, and the frozen text itself says at l.1204 *"Proposition RLF-step
(§8.3) does not use TS"* — three independent exclusions. **But the review's "the one place η_1²/(2N)
becomes a cost" is false**: `HIST.md` l.1379 is another (*"at i = 0, E_𝒞(p) ≥ s(U_0(p)) ≥ η_1²/(2N)
directly (the (R5) branch)"*, Corollary CLS-cone (b)). CLS-cone is CONDITIONAL ⇐ (AE) and `RLARGE.md`
l.517 puts it *"off the HW route"*, so it does not create a consumer of **a_RS** — but the review's
enumeration was not exhaustive and should not be relied on as one.

---

## §4. (M4) l.830: the one live mention, graded

**l.830 is live text** — it is a v3 reading note, in the block l.826-839 that the file introduces with
*"v3 reading notes (the text below is not edited; read it with these notes; they replace v2's notes)"*.
`ARS_FIX` l.296 is therefore right that l.830 is not frozen. The question is what it does.

**What it says.** Frozen §6's commentary paragraph *What RS buys (RLF-F4)* (l.1003-1007) asserts the
kernel branch is *"priced unconditionally by the normalised soft kernel at the FINER coupling g_i
(1/g_i² ≥ 1/g_{i+1}² under (F))"*. l.830 corrects that: the ordering is not implied by (F_R), and the
repair is a factor e^{a_RS R}.

**Where the repaired step is performed.** Exactly one place: **l.1023**,
`(Ce^{-a_RS/g_k²})^{n/c_RS} ≤ (Ce^{-a_RS/g_{k+1}²})^{n/c_RS}`. `FLOW.md` l.909 — the lane's
authoritative (F)→(F_R) consumer table, §19A — puts §6's sentence and l.1023 in **one row** and quotes
both, with effect *"factor e^{a_RS R} per priced cube, **absorbed in C**; with Lemma F-R (iii) the
monotonicity itself holds at all levels k ≥ k_0"*. l.1023 is inside the material l.832 declares
superseded and l.435 declares not consumed.

**What the live route does instead.** Three independent statements, all in the live body:

1. **`RLARGE.md` l.112:** *"Every "priced at the finer coupling" use acquires **e^{aR}**"* — at **a**.
2. **`RLARGE.md` l.114-116:** ***"On the HW route the bad window is priced at its own level's coupling
   u_j, so the defect price itself carries no e^{aR} (HW Theorem HW); HIST-sum's constant uses
   C_ℓe^{aR}."*** The live route **does not perform the cross-level conversion at all** for the defect
   price; the only surviving e^{aR} is HIST-sum's constant, at **a**.
3. **`RLARGE.md` l.586-587 (§5.2)** instantiates it: `6400C_ℓ**e^{aR}**e^{38417B_0}e^{-a/g_K²} ≤ ½`
   and `C_H := 2·6400^{n_♯}(C_ℓ**e^{aR}**e^{38417B_0})^{n_♯+1}/(1 - L^{-γ_H})`.

Lemma F-mono (ii) at l.106-107 is the general statement, `e^{−a/g_k²} ≤ e^{aR}e^{−a/g_{k+1}²}`, with a
**generic** exponent. l.830 instantiates it at a_RS for the superseded pricing; §5.2 instantiates it
at the live **a**. **The live instance exists and it is not a_RS's.**

**Verdict on l.830.** It is a live reading note whose arithmetic repairs a step the live route does not
take. Under §0's (M2) definition it is **not a consumer**: replacing a_RS by any other positive real
changes nothing the live route asserts or requires, because the factor it scales multiplies a weight
(l.1023's) that is not formed on the live route.

**(M-F6) discharged.** `KN_ADOPT.md` §4's standing hypothesis **g_K² ≤ 1/(2R)** *is* live — `RLARGE.md`
l.113 and, in the live HW net, l.413 (*"(H-w′) ⇐ (F_R) [g_K² ≤ 1/(2R)] + …"*) and l.407. So `KN_ADOPT`'s
0.30103-decade pricing is correct arithmetic against a live hypothesis. **It is correct and it is about
l.1023.** `KN_ADOPT`'s own caveat — *"Without g_K² ≤ 1/(2R) the correction e^{a_RS R} is unbounded and
grows with a_RS"* — is therefore also about l.1023, and so is moot on the live route. `KN_ADOPT` §4 is
not wrong; it priced a real site. The site is superseded.

---

## §5. (M5) The construction attempt: eight candidate consumers, all fail

Rule 3 requires that "a_RS is not consumed" be attacked as a positive theorem would be. I tried to
build a live consumer from v3's own stated requirements, not from the review's framing. Seven routes:

**(K1) Through the cutoff n_♯.** v3's cutoff is `n_♯ ≥ max{n^J_*, n_H}` (l.829), with n_H from **a**
(l.586). n^J_* comes from a''^J. l.439 adds that R1/R1^J hold for **every** cutoff n_c ≥ n_*, n^J_*, so
no counted item depends on n_♯ even where it is written. **FAILS.**

**(K2) Through Lemma RS (R4) feeding the mismatch moment (M-i).** §3.3 l.386-390: (M-i) ⇐ Lemma H4-red′
⇐ (LI^F), peeling int(𝒰) links with **Lemma KS (c)** `∫k_ce^{λκuφ} ≤ (1-λ)^{-3/2}`. The live constant is
`C_ℓ = (1 - λ_*)^{-3n_int/2}C_fc` (l.414) — KS's, not (R4)'s. **FAILS.**

**(K3) Through the collar family.** §3.6 l.443-444:
`a_cb := min{c_pr·min{ε_loc²/4, t_pr²}, κε_loc²/(64N), c_pr·min{η_q², t_pr²}}`, `a_D := min{a_bad, a_cb}`.
Uses **η_q** (RS-lin's), ε_loc, c_pr. No a_RS, no η_1. **FAILS** — and see §7, because this is where
RS-lin's threshold is already live.

**(K4) Through Theorem TS.** Excluded three times over: l.835 (reading note), l.517 (**"Not hypotheses
of RLF-step v3"**), l.1204 (frozen text's own Role note). **FAILS.**

**(K5) Through EXISTENCE's (RLF-3^dis).** §2.4: opaque exponent, stale label, l.767 already says it
should read **a**. **FAILS.**

**(K6) Through l.830's e^{a_RS R}.** §4. **FAILS** — the strongest of the eight, and the only one that
required reading three live statements to kill.

**(K7) `ARS_FIX`'s own construction, stated and refuted.** `ARS_FIX` l.298-300: *"Lemma RS is v3-live …
and **its output is a weight with a_RS in the exponent**. **Any** such weight must have its base below 1
against the C_ℓ-type constants, which is exactly l.616-617's condition."* **Both halves fail.**
*(a)* Lemma RS's output is clauses (R1)-(R5); **none of them contains a_RS**. (R4)'s exponent is
κε_1²/(256Ng²); (R5) is a pointwise lower bound s ≥ η_1²/(2N). The single weight `Ce^{-a_RS/g²}` is
formed **only** at l.1020-1023, in the superseded greedy joint pricing. What §3.4 (i) l.421 keeps live
is *"Lemma RS (R3)-(R4)"* — the two clauses, separately. *(b)* l.615-617 is not a condition on "any
weight": its own subject is ***"HIST-sum's, REL-seq's and (RLF-δ)'s smallness conditions"***, three
named items, all of which carry exponent **a**.

**(K8) The independent kill.** a_RS := min{a_η, κε_1²/(256N)} with *"a_η from (PLD)_k (i)"* (l.1020-1021).
`RLARGE.md` l.513-514 lists **"(PLD)_k (i)-(ii)"** among the **"Not hypotheses of RLF-step v3
(withdrawn, relocated, or off the HW route)"**, alongside ***"RS-joint and the greedy joint pricing
(§3.5)"***. **a_RS's own input is off the live route**, so a_RS is not even a well-defined derived
quantity there. This kill is independent of (K1)-(K7) and of every quotation in §3.

**The construction attempt failed.** I could not build a live consumer. That is the honest result, and
it is a negative claim held to positive-theorem scrutiny: eight routes, each killed by live text
quoted by line, two of them (K7, K8) killed without using the review's evidence at all.

---

## §6. (M8) The numbers: `checks/ab1_*`. All ten pre-registered verdicts PASS; all four controls failed as designed

Criteria `checks/ab1_criteria.md` (written before the script, with every input's file:line and a note
of whether it is still an input); script `checks/ab1_margins.py`; output `checks/ab1_out.txt`;
`checks/ab1_err.txt` is empty. Exact `fractions.Fraction`, 60-digit `Decimal` only for the final log₁₀.

| id | result | verdict |
|---|---|---|
| A1 | a_RS at ε_1 = 6.7·10⁻⁴⁰ = **5.931360·10⁻¹⁶⁶**, = `SYMBOLS.md` l.356's ledger value to 0.000000 decades | PASS |
| A2 | the min in a_RS is the **plaquette** branch at all four live ε_1 (5.93·10⁻¹⁶⁶ vs 8.77·10⁻⁸²) | PASS |
| A3 | RS-lin per-cube = **6.524987·10⁻⁸⁹** vs the claimed 6.525·10⁻⁸⁹ (Δ = 1·10⁻⁶ decades) | PASS |
| A4 | gain over a_RS/625 = **79.83731** vs claimed 79.84 (Δ = 0.0027) | PASS |
| A5 | RS-lin ceiling vs DX′ = **+61.41664** vs claimed +61.42 (Δ = 0.0034) | PASS |
| A6 | a_RS ceiling vs DX′ = **−15.62479** vs `PROOF.md` l.71-73's −15.62 (Δ = 0.0048); with c_RS = 625, **−18.42067** | PASS |
| **A7** | **live a = θc_prε_1² = 1.040415·10⁻⁸⁶; a/10² clears DX′ by +63.61927 decades — `RLARGE.md` l.618 is TRUE when evaluated at the exponent l.617 names** | PASS |
| A8 | the a_RS breach reverses at **C_Ω = 4.2149·10¹⁵** vs the claimed 4.14·10¹⁵ (Δ = 0.0078) | PASS |
| A9 | (A4) = log₁₀(η_q/η_1)² + log₁₀(625/81) = **78.94991 + 0.88739**, and 78.94991 = log₁₀(4/ε_1²) exactly, as `HIST.md` l.181 predicts | PASS |
| A10 | no sign changes across all four live ε_1 (see below) | PASS |

**(A10), the defect-2 spread.** Over ε_1 ∈ {6.7, 8.95, 9.52}·10⁻⁴⁰ and 1.27·10⁻³⁹:
(A4) 79.84 → 79.28; (A5) +61.42 → +61.97; (A6) −15.62 → −14.51; (A7) +63.62 → +64.17. **No sign
changes.** So the a_RS *breach*, the RS-lin *gain* and l.618's *truth at a* all survive the ε_1
dispute — which is worth saying plainly, because it means **(C6) does not rescue (C2)**.

**Designed-FAIL controls (defect 3), each reported as failing:**
- **(C-F1)** η_q → η_1 in RS-lin's plaquette branch (mechanism removed): gain collapses **79.837 →
  0.887**. Control failed as designed; (A4) is measuring re-centring, not bookkeeping.
- **(C-F2)** "a_RS's min is the kernel branch": **False**. Control failed as designed.
- **(C-F3)** (A7)'s ceiling test re-run with a_RS in place of a: does **not** clear DX′. Control failed
  as designed; (A7) genuinely discriminates between the two exponents.
- **(C-F4)** (A1) re-run at `RLARGE.md` l.1248's illustrative ε_1 = 0.5: a_RS = 1.84·10⁻¹⁰, does not
  match the ledger. Control failed as designed; the script is not ε_1-blind.

**POST-HOC (not pre-registered, labelled as such):** the **live** exponent a = 1.040·10⁻⁸⁶ is
**2.20263 decades BETTER** than RS-lin's joint-route per-cube value 6.525·10⁻⁸⁹. See §7.

**Two defect-2 notes on figures I reproduced.** (i) The −15.62 breach is evaluated at **C_Ω = 1**, a
value stated nowhere; (A8) shows it reverses at C_Ω = 4.21·10¹⁵. (ii) My (A8) differs from the review's
4.14·10¹⁵ by 0.0078 decades because the review carried −15.617 where the exact figure is −15.6248.
Within tolerance; recorded so nobody re-derives it as a discrepancy.

---

## §7. (M7) RS-lin: genuinely proven, genuinely live — and it rescues nothing, for the same reason a_RS breaks nothing

Three sub-questions, answered separately, each by reading rather than by citing the label (M-F4).

**(i) Is the PROVEN-HERE genuine? YES.** `RLARGE.md` l.628 lists *"HIST: Lemma PM (with KQ), **Lemma
RS-lin**, …"* under PROVEN-HERE. I did not stop at the label. **`HIST.md` l.168-179** states RS-lin and
writes out a three-line proof; its two inputs, **Lemma PM** (l.140-149) and **Lemma KQ** (l.155-166),
are each proven in full on the page. I re-derived (b) by hand:
δ ≤ A_dη_q with η_q ≤ ε_1/(256NA_d) gives ‖W_0 − S‖ ≤ 3δ ≤ 3ε_1/(256N) (PM); so on {‖V−S‖ ≥ ε_1/8},
x := ‖V − W_0‖ ≥ ε_1/8 − 3ε_1/(256N) = 0.11914ε_1 ≥ ε_1/16 at N = 2; ‖M̄ − W_0‖ ≤ 4δ ≤ ε_1/(64N) ≤ x/(4N);
KQ (lower) gives φ ≥ x²/(2N) − x·x/(4N) = x²/(4N) ≥ ε_1²/(1024N). **The exponent κε_1²/(1024N) is right.**
The one hypothesis is `ε_1 ≤ 256Nδ_0` (= 0.4 at N = 2, 3; `HIST.md` l.152, l.183); at every live ε_1 it
holds with 39 decades to spare, and `ab1` asserts the δ_0/9 cap does not bind. **PROVEN, re-derived, not
cited.**

**(ii) Is it live? YES, and it is already being used.** `RLARGE.md` l.421 keeps *"Lemma RS (R3)-(R4),
**RS-lin (b)-(c)**"* for the representation route and collar links. `HIST.md` l.741's DAG runs
`PM → KQ → RS-lin → CL^J → Lemma 7.2-0^J`, and **CL^J (a)-(b) is step 1 of RLF-step v3** (`RLARGE.md`
l.521-522). Further, **RS-lin's threshold η_q is the threshold v3's live body actually uses** — and
this is the part nobody has written down:

> In `RLARGE.md`'s **live body (l.1-823)**, **η_1 appears only in its own definition (l.64) and in two
> index rows (l.261, l.761) — it has no consumer there at all.** **η_q has three live consumers:**
> **(TC)** at l.82-83, the quiet / collar-bad definition at l.297, and **a_cb** at l.443.

So RS-lin is not an overlooked lemma. Its mechanism was adopted where v3 needed a threshold of this
kind, and `RLARGE.md` l.64-65 carries both thresholds side by side with the comparison already stated.

**(iii) Does anything prevent the lane from simply using it — i.e. would adopting it help? NO, and the
answer is the same one that dissolves the a_RS crisis.** RS-lin's *defect-pricing* use is the **joint /
RS-joint route**, and `RLARGE.md` l.513-514 lists ***"RS-joint and the greedy joint pricing (§3.5)"***
among the **"Not hypotheses of RLF-step v3"**; §3.5 l.435 says RS-joint's **c_RS = 81 ⇐ (PLD-q)_k** is
**not consumed**; and `HIST.md` l.745's DAG routes `RS-lin + TD + (PLD-q) → RS-joint [CONDITIONAL]`,
whose hypothesis (PLD-q)_k is also on l.513's excluded list. **The 6.525·10⁻⁸⁹ is a per-cube exponent
of the same dead sub-route the 15.62-decade breach is against.**

And the arithmetic closes it from the other side (POST-HOC): the **live** exponent a = θa_bad =
1.040·10⁻⁸⁶ is **2.203 decades better** than RS-lin's 6.525·10⁻⁸⁹, and clears DX′ by **+63.62** against
RS-lin's **+61.42**. **Adopting RS-lin as the defect price would be a 2.2-decade downgrade on the live
route.**

**Status of (M7): RS-lin is PROVEN (re-derived here) and LIVE (as an input to CL^J, and via η_q to
(TC), quietness and a_cb). Its use as a defect price is CONDITIONAL on (PLD-q)_k and OFF the live
route.** The review's framing — *"whether a_RS binds matters much less than whether anyone noticed
RS-lin"* — is half right and half an over-read. RS-lin was noticed and partly adopted. What nobody
noticed is that **both** the a_RS crisis and the RS-lin rescue are priced against the same superseded
route, and that the live route's own exponent beats both.

---

## §8. (M9) Symbol hygiene found along the way

- **a_RS is single-object**, as `SYMBOLS.md` l.766 records (`a_RS := min{a_η, κε_1²/(256N)}`,
  `RLARGE.md` l.1020, one definition site). Confirmed by my own census. One fewer worry, as briefed.
- **c_RS is TWO objects, and `SYMBOLS.md` has no entry for it** (grep: zero hits). **c_RS = 5⁴ = 625**
  is the greedy factor of `RLARGE.md` l.1021 (RS alone); **c_RS = 81** is RS-joint's, `RLARGE.md` l.435
  and `HIST.md` l.185-186. Both are superseded, so nothing live breaks — but every "a_RS/c_RS" figure
  in this sub-lane depends on which one is meant, and the 625/81 asymmetry is worth exactly **0.88739
  decades** (`ab1` A9). Anyone re-deriving the 79.84 or the −18.41 without pinning c_RS by line will be
  off by that much.
- **n_♯ is two objects.** Frozen: `n_♯ := ⌊4/(a_♯β_-)⌋` (`RLARGE.md` l.1024). Live: *"the cutoff is
  n_♯ ≥ max{n^J_*, n_H} with n_H from v3's a"* (l.829). Same glyph, different defining requirement,
  12 lines apart in the same reading-note block that supersedes the first.
- **a_η has no live supplier.** `RLARGE.md` l.1021 says *"a_η from (PLD)_k (i)"*; l.513 puts (PLD)_k (i)
  off the live route. `SYMBOLS.md` l.362 independently reports a_η's supply problem from the PLD side.

---

## §9. VERDICT

### **(V-NO). a_RS binds nothing on the live RLF-step v3 route.**

Stated without hedging, in the form §0.3 pre-registered:

1. **No consumer exists.** Five occurrences in `RLARGE.md`, all in Appendix A; three of them
   (l.1020, l.1023, l.1024) explicitly superseded by l.832 and l.435; one (l.1247) a record of a check
   whose own reading note calls it illustrative; one (l.830) a live note repairing a step the live
   route does not take (§4). Zero occurrences in `HIST.md`, `HW.md`, `PLD.md`, `SQ.md`, `BFT_A.md`,
   `BFT_B.md`, `NORMS.md`, `LINEAR_PACKAGE.md`. The live constant list is `(C_ℓ, B_0, E_0, a, n_♯)`
   (l.545).
2. **The construction attempt failed**, over eight routes (§5), two of which (K7, K8) use no part of
   the session-25 review's evidence. (K8) is the cleanest: a_RS's own input (PLD)_k (i) is on l.513's
   list of things that are **not hypotheses of RLF-step v3**.
3. **Therefore the 15.62-decade breach is against a quantity nothing reads.** The arithmetic is right
   (`ab1` A6 reproduces −15.62479 exactly) and it prices a superseded object.

**Status words.** The *reading* — a_RS has no live consumer — is **ARGUED, not PROVEN**: it is an
exhaustive-search negative over a corpus, and an exhaustive search is only as good as its spellings
(§1) and its corpus. What is **PROVEN** is each individual exclusion, since each is a quotation of live
text: l.513-514 excludes (PLD)_k (i)-(ii) and RS-joint/greedy joint pricing; l.517 excludes TS; l.832
and l.435 supersede a_♯/c_RS/n_♯ and the a_♯ formula; l.545 lists the live constants; l.114-116 says the
live defect price carries no e^{aR} at all. The residual risk is a consumer written with a spelling I
did not search, in a file I did not open.

### Consequences, each with a status word

**(a) `EPS1_SWEEP` (C2) — DISSOLVED. Both horns are about nothing.**
(C2) reads *"Adopt KN-step's linear η_1 first, **or** scope RLARGE l.618 … **or** record that the
RS/joint route's ceiling already sits 15.62 decades below DX′"* (`EPS1_SWEEP.md` l.481-484), and
*"**This is the binding condition; everything else is bookkeeping**"*. Under (V-NO): the second horn
records a fact about a superseded exponent, and the first horn would adopt a linear η_1 to fix an
exponent that is not read. **Not merely "not binding" — vacuous.** `EPS1_SWEEP.md` l.679 (*"that is
more than bookkeeping is (C2), the a_RS quartic"*) and l.598 go with it. This **confirms the session-25
finding that D4's ordering is wrong, by a third route**, and strengthens it: D4 fails not only because
(C6) and (C7) are prior, but because **(C2)'s object does not exist on the live route**.

**(b) `RLARGE.md` l.618 — TRUE AS WRITTEN; the defect is wording, not arithmetic.**
`PROOF.md` l.71-73's `[S24-flag 6]` (*"a_RS BINDS TODAY, and RLARGE l.618 is FALSE"*) is **REFUTED**.
The bullet at l.615-618 enumerates its own scope — *"HIST-sum's, REL-seq's and (RLF-δ)'s smallness
conditions"*, all three carrying exponent **a** — and l.617's `g_K² ≲ a/10²` is the subject of l.618's
clause. `ab1` A7: at the live a, the ceiling clears DX′ by **+63.62 decades**, at every live ε_1.
`EPS1_SWEEP.md` l.425-426 splits a two-clause sentence to make l.618 unscoped. **Recommended edit
(not mine to make): l.618 should read "RLF's own ceilings — HIST-sum's, REL-seq's and (RLF-δ)'s — do
not bind", so the next reader cannot repeat this.**

**(c) `ARS_FIX.md` and `EPS1_SWEEP.md` headline findings — the a_RS halves EVAPORATE.**
What survives is everything that does not depend on a_RS binding: `ARS_FIX`'s rebuild of KN-step′
(independently confirmed by `KN_ADOPT`), its c_RS asymmetry finding, its (C7) operator, the ε_1
census, (C1)/(C3)/(C4)/(C6)/(C7). What goes is **(G6)/(V2)**, **(C2)**, **(C5)'s a_RS half** (*"a_RS ∝
ε_1⁴ (19.415 decades)"* — correct arithmetic, no live consumer), and `EPS1_SWEEP` §4.3 in its entirety.
`KN_ADOPT` §4's 0.30103 decades is correct arithmetic against a live hypothesis (g_K² ≤ 1/(2R) is live
at l.113/l.407/l.413) about a superseded site, so the two corrected margins **−15.918 / +66.222** are
likewise about nothing.

### The single biggest thing this changes

**The sub-lane's constants crisis is not a crisis, and the keystone adoption's headline is not a gain —
because the breach, the repair and the rescue are all priced against the same superseded route, while
the live route's own defect exponent `a = θa_bad = 1.04·10⁻⁸⁶` already clears DX′ by 63.6 decades at
every live ε_1.** Three separate sessions of work — `ARS_FIX`, `EPS1_SWEEP`, and the RS-lin comparison
— measured the same dead object from three directions and got three mutually consistent, mutually
irrelevant answers.

### Against the lead, and against the review

- **Against the lead (D4).** D4 reads (C2) as the binding link in a chain. (C2) is vacuous. The lead's
  own D6 invites this; reported as instructed.
- **Against the review.** Its item 3 is right in substance and I have independently confirmed it by a
  route it did not use. But its quotation #3 is truncated in a way that over-states §3.5's scope, its
  grep claim is false for `ARS_FIX` + `§3.5`, and its *"the one place η_1²/(2N) becomes a cost"* misses
  `HIST.md` l.1379. More importantly, its lead finding — that RS-lin is the overlooked rescue — **is an
  over-read**: RS-lin is proven and live and partly adopted already, and adopting it as the *defect
  price* would cost the live route 2.20 decades. The review compared RS-lin against a_RS/c_RS, i.e.
  against the same superseded baseline it had just shown nobody reads. It never compared RS-lin against
  the **live** exponent a.

---

## FOR OTHER FILES (not edited)

1. **`PROOF.md` l.71-78 `[S24-flag 6]` and l.6921** — the claim *"a_RS BINDS TODAY, and RLARGE l.618 is
   FALSE"* is REFUTED (§9(b)). Suggested replacement: *"a_RS has no consumer on the live RLF-step v3
   route (ARS_BIND §2, §5); l.618 is true at the exponent it names (a), ARS_BIND `checks/ab1` A7."*
   `PROOF.md` l.92's `[S25-fix 1]` sentence *"a_RS's STATUS is unchanged — CONDITIONAL on (PLD)_k (i)"*
   should note that (PLD)_k (i) is itself on `RLARGE.md` l.513's not-a-hypothesis list.
2. **`RLARGE.md` l.618 (owner: RLARGE)** — restate the scope inside the sentence, as §9(b).
3. **`RLARGE.md` l.830-832 (owner: RLARGE)** — l.830 and l.832 still read as if in tension (`ARS_FIX`
   §8.1 item 7, `KN_ADOPT` §6 item 1 both ask for this). The resolution is in §4 here: l.830 repairs
   l.1023, which l.832 supersedes. One clause would close it.
4. **`RLARGE.md` l.767 / U11 / K8 (owners: RLARGE, EXISTENCE)** — `EXISTENCE.md` still writes **a_♯** at
   l.1882-1886, l.3072-3083, l.3362-3403 where l.767 says it should read **a**. Harmless today (opaque
   exponent, §2.4) and a live mislabelling of the kind that produced this whole episode.
5. **`SYMBOLS.md` (owner: SYMBOLS)** — no entry for **c_RS**, which is ≥2 objects (625 at `RLARGE.md`
   l.1021, 81 at l.435 / `HIST.md` l.185-186), worth 0.887 decades; and **n_♯** is ≥2 objects
   (`RLARGE.md` l.1024 vs l.829). §8.
6. **`EPS1_SWEEP.md` §5 (C2) and §4.3 (owner: EPS1_SWEEP / lead)** — DISSOLVED, §9(a). The §5 verdict
   word should change: with (C2) vacuous, "SAFE WITH NAMED CONDITIONS" rests on (C1), (C3), (C4), (C6),
   (C7), of which (C7) is a hypothesis rather than a condition.
7. **`RTARGET` §54 / the lead's D4 (owner: lead)** — D4's chain `H1 → KN-step′ → (C2) → bookkeeping`
   breaks at (C2) for a reason independent of H1 and independent of failure mode C2-F1 as written.
8. **For whoever owns the η_1 question (lead)** — a flag, **ARGUED, scoped to `RLARGE.md`'s live body
   only**, raised here because it fell out of the trace and is outside my scope to settle: in
   `RLARGE.md` l.1-823, **η_1 has no consumer** (definition l.64 + index rows l.261, l.761), while
   **η_q has three** (l.82-83, l.297, l.443). `HIST.md` (l.1377-1379, l.1386) and `PLD.md` still consume
   η_1. **If the KN-step′ adoption's value is measured through η_1's consumers, that measurement should
   be redone against this list before anyone prices it again** — the same error-shape as the one this
   file closes.
