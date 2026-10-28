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
