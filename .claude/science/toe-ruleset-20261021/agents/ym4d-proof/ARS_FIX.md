# ARS_FIX — the a_RS ceiling, and whether KN-step's linear η_1 repairs it

Owner of this file: the a_RS/η_1 repair worker, session 24 (ym4d-proof lane).
Scope: ONE bounded repair. Writable by me: **this file** and new files under `checks/` prefixed `ar1_`.
Nothing else, anywhere. No git command will be run by me.

---

## §0. PRE-STATED (first edit of this file)

**This is the first edit made to this file. UTC time of this edit: 2026-10-28T15:11Z.**

Statements only, and **no number at all** except the pre-registered tolerance factors named in §0.5, which
are chosen here and are not derived from anything. Written **before** reading RLARGE.md's definitions of
a_RS, a_η, η_1 or DX′, **before** reading EXISTENCE.md's Lemma KN / Corollary KN-step, **before** reading
REVIEW_PLD_S3, SESSION24_RESULTS.md, HW.md or PLD.md, and **before** any arithmetic. It cites **no
quantity produced in session 24**, and in particular no figure from EPS1_SWEEP.md, TAUFLAT.md or
EPSSTAR.md: those three have been read only for the *statement* of the claim I am auditing, and none of
their numbers is assumed below or used as a criterion.

### §0.1 What I was asked to do

EPS1_SWEEP.md §4.3 (check e1-4) reports a FAIL against **RLARGE.md l.617-618**: that the RS/joint route's
coupling ceiling, derived from **a_RS** (RLARGE l.1020) via **a_η = η_1²/4** (RLARGE l.1248) with a
**quadratic** η_1, is **quartic in ε_1**, and that this ceiling already sits **below** the programme's
binding DX′ ceiling **at today's ε_1**, independently of TAUFLAT §4's proposed ε_1 move. It proposes the
repair: adopt **Corollary KN-step's linear η_1** from **EXISTENCE.md l.1771**, which EPS1_SWEEP says is
already PROVEN there and was already requested of RLARGE in **REVIEW_PLD_S3 item E9**.

My job is five things, in order:

- **T1 (independent verification).** Re-derive a_RS's ε_1-dependence **from RLARGE's own definitions**,
  not from EPS1_SWEEP's summary, and re-compute its margin against DX′ at the **current** constants. If
  EPS1_SWEEP is wrong, say so and stop.
- **T2 (rebuild, not cite).** Rebuild KN-step's linear η_1 from EXISTENCE l.1771 **on our structures**,
  per the standing rule that load-bearing cited mathematics is rebuilt rather than cited. State its
  hypotheses **precisely**, and check **each one** is available at the point in RLARGE where the η_1 it
  would replace is consumed. I pre-register the expectation that a lemma proven in the existence lane may
  carry a hypothesis RLARGE does not supply, and that this is the most likely reason a review asked for
  the adoption and it never happened; I will look for it specifically and report it whether or not it
  exists.
- **T3 (carry-through).** With the linear η_1 in force, recompute a_RS, its margin against DX′, and
  **every other entry of RLARGE's ceiling table that η_1 touches** — not only the row EPS1_SWEEP names.
- **T4 (symbol gate, settled before any aggregation).** Is **η_1 one symbol or several**? EPS1_SWEEP
  reports ε_1 is at least five symbols, EPSSTAR reports four distinct ε_*, and TAUFLAT reports θ_0 is two
  symbols whose collision caused a large error. I will therefore read the **definition in force at each
  occurrence** of η_1 in its owning file, not the letter, and will **not aggregate across occurrences
  until this gate is settled**. Two occurrences are the same symbol only if I can cite one definition both
  use, or a line in an owning file equating them. If η_1 is several symbols I will report that **first and
  loudly**, because in that case the proposed adoption may be addressed to the wrong symbol.
- **T5 (consumer sweep for breakage).** Find **every** consumer of RLARGE's current η_1 and say, for each,
  whether the linear form serves it. A linear η_1 is **larger** than a quadratic one at small ε_1, so I
  pre-register that the hazard direction is **consumers that need η_1 SMALL**, and that these are the ones
  the adoption could break.

### §0.2 What I will NOT do

- **I will not change ε_1**, request that it be changed, or assume TAUFLAT §4's ε_1 move happens: it is
  owner-gated and undecided. Every number I report will be given **both** at today's ε_1 and at the
  proposed one, labelled.
- I will not edit RLARGE.md, PLD.md, HW.md, EXISTENCE.md, EPS1_SWEEP.md, SF.md, HIST.md, SQ.md, BFT_*.md,
  NORMS.md, GREENT.md, YSUP.md, PROOF.md, HANDOFF.md, SESSION24_RESULTS.md or any REVIEW_* file. Every
  request on them goes in a "FOR OTHER FILES (not edited)" section at the end of this file.
- I will not re-judge the DESC-ε (iii) failure, TAUFLAT's adjudication, the status of (MS-Sob), (AE),
  AE-red or (REG-min), the ×82 ring price, or EPS1_SWEEP's verdict on option C as a whole. Those are
  quoted from their owners.
- I will not re-derive DX′, HW's b_n, PLD's λ_min, SQ's η_♭ or C_Ω. Transcribed constants carry file+line
  citations; a number reproduced here is **not** an endorsement of its source.

### §0.3 Pre-registered statement of what confirms and what refutes EPS1_SWEEP's finding

The finding under test has **three separable claims**. Each gets its own verdict, and they can disagree.

**(V1) The exponent claim.** *a_RS is quartic in ε_1 under RLARGE's current η_1.*
- **CONFIRMED** if, reading only RLARGE's own definitions of a_RS, a_η and η_1, the exponent of ε_1 in the
  branch of a_RS that is **active at today's ε_1** is exactly 4.
- **REFUTED** if that exponent is 2, or if the active branch at today's ε_1 is not the η_1-bearing one, or
  if a_RS's definition does not in fact route through η_1.
- **AMBIGUOUS** (a reportable third outcome) if RLARGE's η_1 is a min whose active branch cannot be
  determined from RLARGE's own text without an input RLARGE does not supply. I pre-register AMBIGUOUS as a
  real possible answer, not a failure to decide.

**(V2) The binding claim.** *a_RS's ceiling is below DX′ already at today's ε_1.*
- **CONFIRMED** if, with the current constants (HW session 6's g²_CRC, PLD session 7's ×82 closed column),
  the a_RS-derived coupling ceiling divided by the DX′ ceiling is **less than 1** at today's ε_1, i.e. the
  margin in decades is **negative**, and the sign is robust to the factor-ε_1 and factor-DX′ ambiguities
  §0.5 names.
- **REFUTED** if that ratio is **greater than 1** at today's ε_1, i.e. the margin is positive, at every
  one of the live ε_1 values and under both normalisations of the /10² convention.
- **SIGN-FRAGILE** (reportable) if the sign of the margin changes across the live ε_1 values or across a
  defensible reading of RLARGE's own ceiling convention. Because EPS1_SWEEP reports its own margin as
  being of order ten decades, I pre-register that a sign flip would require a discrepancy of many decades,
  so SIGN-FRAGILE is **unlikely**; if it occurs it is the headline.

**(V3) The repair claim.** *Adopting KN-step's linear η_1 moves that margin from negative to positive, and
the size of the gain is as EPS1_SWEEP states.*
- **CONFIRMED** if the rebuilt linear η_1, **with every hypothesis it needs verified available in RLARGE at
  the point of consumption**, makes a_RS quadratic in ε_1 and the margin positive at today's ε_1 **and** at
  the proposed one; and the two gains EPS1_SWEEP quotes reproduce within the §0.5 tolerance.
- **REFUTED** if the margin stays negative after adoption, or if the linear form is not available in
  RLARGE's setting because a hypothesis is missing there, or if some other consumer of η_1 fails under the
  linear form (T5), or if the gain is outside the §0.5 tolerance in the **unfavourable** direction.
- **CONDITIONAL** if the arithmetic goes through but a hypothesis of KN-step is **not** supplied by RLARGE:
  then the repair is CONDITIONAL on that named input and I will name it, and the honest verdict on the
  92-decade gain is "available only if X", not "available".

**Pre-registered as NOT sufficient to confirm anything:** that EPS1_SWEEP's arithmetic reproduces (that is
the claim under test, not an input); that RLARGE l.633 lists Lemma KN as PROVEN-HERE (a listing is not a
proof, and whether its hypotheses are met in RLARGE is the actual question); that REVIEW_PLD_S3 E9 asked
for the adoption (a request is not a licence); that the margin is large after the repair (a margin is only
meaningful if its inputs are the ones in force).

### §0.4 Pre-registered failure modes — the ways my own repair should break

Written before any derivation, so that finding one is a result and not a surprise.

- **(G1) Hypothesis gap.** KN-step's linear η_1 holds under a hypothesis the existence lane supplies and
  RLARGE does not — a re-centring, a flatness or a gauge condition, a restriction to a slice or to the
  trivial background, or a dimension/geometry constraint. **(G1) forces the repair to CONDITIONAL at best**
  and is the single most likely outcome by my own prior.
- **(G2) Symbol split on η_1.** The η_1 of EXISTENCE l.1771 and the η_1 of RLARGE l.64/l.1248 are
  **different constants with the same letter**, so the "adoption" is a category error and the 92 decades
  are not available at all. This is the (F2)-shaped failure that EPS1_SWEEP found for ε_1, one symbol over.
  **(G2) would refute (V3) outright** while leaving (V1) and (V2) untouched.
- **(G3) A consumer that needs η_1 small.** The linear η_1 is larger at small ε_1. Any consumer that
  bounds something **by** η_1, or that needs η_1 below another threshold, gets **worse**. If such a
  consumer exists and its clause fails at the linear value, the repair trades one breach for another.
- **(G4) The min's other branch.** If a_RS or η_1 is a min, adopting the linear branch may simply move the
  min to a different entry, so the quartic is replaced by something else rather than by ε_1². Then the gain
  is capped by that other entry and is **not** the full 92 decades.
- **(G5) Double-counting the repair.** If RLARGE's quadratic η_1 is itself *derived* from something that
  the linear η_1 would contradict, adopting the linear form requires re-deriving that something, and the
  repair is not the one-line substitution it looks like.
- **(G6) The /10² convention.** If RLARGE's "a/10²" ceiling convention is not the right one to apply to
  a_RS — e.g. if the RS/joint route's ceiling carries a different numerical convention — then the margin
  arithmetic is comparing unlike quantities and both (V2) and (V3) are mis-stated. I will read the
  convention in its owning file rather than inherit it.
- **(G7) My own check has no power.** Six findings in session 24 were verification gates incapable of
  failing. See §0.6; if this happens I will report NO POWER and re-run under a new id with the criteria
  untouched.

### §0.5 Pre-registered arithmetic method and tolerances

- Exact `fractions.Fraction`, with `decimal.Decimal` at fixed high precision **for display only**, in
  plain `python3 -I`, single thread, no numpy, no BLAS, no SciPy. **No floating-point intermediate will
  carry a decade comparison, and nothing will be floated across more than a few decades**: ratios are
  formed as exact rationals and displayed as log10. No numeric lock is needed or will be taken (exact
  rational arithmetic, brief rule 6).
- **Tolerance for "reproduces":** a factor **1.2** on any quantity I compare against a transcribed figure,
  and **0.1 decade** on any quantity quoted in decades. A disagreement outside tolerance is reported as
  **SOURCE-DISAGREES** with both figures given exactly, and its direction (favourable / unfavourable to
  the claim under test) stated.
- Because the lane holds **more than one live numerical value of ε_1** (EPS1_SWEEP §1.1, read for the
  statement that this is so; I take none of its four values on faith and will read them from their owning
  files), **every margin will be evaluated at every live value** and its sign reported for each. A verdict
  that depends on which value is taken is reported as such.
- **Verdicts at two precisions.** Every decade figure will be recomputed at two display precisions and
  must agree; a disagreement is a FAIL of the arithmetic, not of the claim.

### §0.6 Pre-registered falsifiability and the power check, named in advance

- **Every check I run must be able to return both verdicts**, and for each I will name the **independent
  construction** it is tested against — independent meaning a transcription from a **different owning file**
  than the one whose claim is under test, or a threshold fixed **before** this proposal existed.
- **The mandatory power check, pre-registered now.** I will construct the **counterfactual at which my own
  verdict flips** and run it:
  - a **value of the η_1 exponent** (i.e. the quadratic form) at which my (V2) verdict must read BINDS, and
    the **linear** form at which it must read NOT-BINDING — both from the same script, same constants;
  - and a value of the **ε_1-exponent of a_RS** interpolating between them at which the margin crosses
    zero, reported, so that the verdict is shown to be a function of the exponent and not of my
    bookkeeping.
  If **no** choice of exponent or of η_1 form can flip any verdict my script returns, the script **has no
  power** and I will report NO POWER, not a PASS, and re-run under a new id.
- **A check that merely re-evaluates the formula its source evaluated is not evidence.** The things with
  power here are (i) the definition comparison of T4, (ii) the hypothesis-availability check of T2, which
  is a reading check and can fail, and (iii) reconstructing each ceiling **from the chain that produces it**
  rather than from the summary line that quotes it.
- **Grading.** Each check is graded **strong / medium / weak** with a stated reason, in the same sense
  EPS1_SWEEP §6.1 used: strong = it can and does return a FAIL against a claim written by another author
  for another purpose; weak = it can only catch my own bookkeeping slip.

### §0.7 Pre-registered statuses

**PROVEN** (a complete argument written out in this file from stated hypotheses) / **COMPUTED** (exact) /
**ARGUED** (convincing with an identified hole) / **CONDITIONAL** (naming the open input) / **GAP** /
**OPEN**. A failed check is reported as a **FAIL** with its output and script kept **unaltered**; a re-run
takes a **new id** and leaves the criteria untouched; any probe run **after** seeing a result is labelled
**POST-HOC** and carries no pre-registered verdict. I will not inflate: a wrong PROVEN is worse than an
honest OPEN.

*(End of §0, the pre-stated section. Everything below this line was written after it.)*

---

## §1. T4 — THE SYMBOL GATE, SETTLED FIRST: **η_1 IS THREE SYMBOLS, AND PLD ALREADY USES THE LINEAR ONE**

> ### **η_1 is at least THREE distinct symbols, and the proof lane's two main files are using DIFFERENT ones for the SAME object — RLARGE's (R3) threshold.**

Status: **COMPUTED (reading, definitions quoted from owning files).** Pre-registered as failure mode
**(G2)** in §0.4. It does **not** kill the repair — but it reframes it, because the adoption is not a new
proposal: **PLD has already made it and RLARGE has already refused it**, and the two files have been
inconsistent ever since.

| # | symbol | definition in force, with citation | same as #1? |
|---|---|---|---|
| **1** | **η_1^RS** — RLARGE's (R3) dichotomy threshold | **η_1 := min{ε_1/(2L²), ε_1²/(512N·A_d(L))}** (**RLARGE.md l.64** and again inside Lemma RS at **l.976**; = min{ε_1/18, ε_1²/(4608N)} at d = 4, L = 3, **l.1009**). Quoted in this form by **HIST.md l.1167, l.1377** and **SF.md l.2204**; used as symbol 1 at **HIST l.151, l.181, l.186, l.1481** and **RLARGE l.978, l.981, l.994-999, l.1003, l.1026, l.1184, l.1248** | — |
| **2** | **η_1^KN** — KN-step's re-centred threshold | **η_1 := c_1ε_1, c_1 = 1/(2(L² + 5.5A_d(L))) = 1/117** (**EXISTENCE.md l.1771**, l.1774). **PLD.md uses this as "RLARGE's η_1" at l.42, l.772, l.1010, l.1071, l.1077, l.1096, l.1204, l.1259** | **NO — it is 39.4× (N = 2) / 59.1× (N = 3) larger than η_q, and ~41 decades larger than symbol 1 at the live ε_1** |
| **3** | **η_1^gauge** — a local bound variable in SQ | **η_1 := η_U/2**, an ℓ⁴-norm threshold on a Neumann-Coulomb log-gauge potential inside a connectedness argument (**SQ.md l.1679**, used l.1680-1685). A bound variable, re-used letter | **NO** |

**Where it does NOT collide, checked:** η_1 occurs **zero** times in HW.md, NORMS.md, BFT_A.md, BFT_B.md,
FLOW.md and LINEAR_PACKAGE.md. EXISTENCE has exactly two occurrences (l.1771 = symbol 2's definition;
l.1804 = symbol 1's role, "instead of the fixed η_1"). PROOF.md has one (l.63, session 24's own flag).
**η_q, η_♭, η_AE, η_U are separately named and are not collisions.** So, unlike ε_1 (five symbols) and ε_*
(four), the η_1 hazard is confined to the proof lane and the existence lane — but it is **worse in kind**,
because symbols 1 and 2 are two different values *of the same quantity in the same lemma*, not two
different quantities sharing a letter.

### §1.1 This is a recorded, unresolved cross-file conflict, not a discovery

- **REVIEW_PLD_S3 l.463** states it outright: ***"Today PLD and RLARGE use different η_1."***
- **REVIEW_PLD_S3 l.299 (fix INH-1)**: *"'RLARGE's η_1 = c_1ε_1' (l.1010, 1071, 1077, 1096, 1204, 1259)
  is wrong"*; **l.39-40** records that REVIEW_PLD_S1_S2's F-9 *"made the same slip"*, so the
  misidentification has survived two reviews.
- **REVIEW_PLD_S3 l.462 (E9)** is an **either/or**: *"**Either** adopt KN-step's re-centred dichotomy in
  RLARGE §6 (η_1 := c_1ε_1 …), **or** replace every 'η_1 = c_1ε_1' in PLD §15 by (R3)'s η_1."*
- **RLARGE v3 ANSWERED E9 — by taking the second horn.** **RLARGE l.830** (a v3 reading note, i.e. current
  text): *"**§6 Lemma RS:** … **η_1 is v2/v3's η_1 (E9).**"*

> **SOURCE-DISAGREES with EPS1_SWEEP §4.3 / §6.4 and with PROOF.md [S24-flag 6] on one word.** They say the
> adoption was *"already requested … and has not"* been carried out, which reads as an omission. It is not
> an omission: **E9 offered two horns and RLARGE v3 explicitly chose the other one at l.830.** The lane's
> state is a *decision*, taken without pricing the a_RS consequence. That changes what this repair is: not
> "apply a pending request" but **"reopen a decision, now that the price of the horn chosen is known"** —
> and it means the change needs RLARGE's owner, not a bookkeeper. It also means the inconsistency has a
> second, cheaper resolution (fix PLD's text instead), which does **not** repair a_RS. Both horns must be
> on the table when the owner decides, and only one of them is worth 82 decades.

---

## §2. T1 — INDEPENDENT VERIFICATION OF THE FINDING

Re-derived from RLARGE's own definitions, not from EPS1_SWEEP's summary.
[`checks/ar1_criteria.md` → `checks/ar1_margins.py` → `checks/ar1_out.txt`; re-run `ar1b_power.py` →
`ar1b_out.txt`, §7.]

### §2.1 (V1) The exponent: **CONFIRMED, EXP-4** [COMPUTED, exact]

The chain is three definitions deep and each step is in RLARGE:

1. **η_1 = min{ε_1/(2L²), ε_1²/(512NA_d)}** (l.64, l.976). The **quadratic** entry is active iff
   ε_1 < 512NA_d/(2L²) = **512** (N = 2) / **768** (N = 3) at d = 4, L = 3 — so active at **every**
   admissible ε_1 (the lane's ceiling is ε_1 ≤ 2 even in the illustrative numerics, RLARGE l.73).
2. **a_η = η_1²/(2N)** (l.1026's bare-level value; = (R5)'s inequality (B) bound at l.981), hence
   **∝ ε_1⁴**.
3. **a_RS = min{a_η, κε_1²/(256N)}** (l.1020). The a_η entry is active iff
   ε_1² < (512NA_d)²·2N/(256N) = **663 552** (N = 2), i.e. ε_1 < **814.587** — confirming EPS1_SWEEP's
   "it would need ε_1 > 814" exactly.

**Verdict EXP-4 at all four live ε_1 and at the proposed one, for N = 2 and N = 3.** Power demonstrated:
at the counterfactual ε_1 = 1000 (N = 2) and ε_1 = 1000 (N = 3) the same script returns **EXP-2**, because
the η_1 min changes branch. **HAS-POWER.**

### §2.2 (V2) The binding claim: **CONFIRMED at every live ε_1, under both ceiling conventions** [COMPUTED]

RLARGE l.616-617's convention is g_K² ≲ a/10², the 10² being log C_ℓ ≈ 93. Applied to the RS exponent:

| ε_1, with its owning file | a_RS | ceiling a_RS/10² | margin vs DX′ | with the c_RS divisor | margin |
|---|---|---|---|---|---|
| 1.27·10⁻³⁹ (SF l.2837) | 7.65720·10⁻¹⁶⁵ | 7.65720·10⁻¹⁶⁷ | **−14.506** | 1.22515·10⁻¹⁶⁹ | **−17.302** |
| 9.52·10⁻⁴⁰ (RLARGE l.71) | 2.41770·10⁻¹⁶⁵ | 2.41770·10⁻¹⁶⁷ | **−15.007** | 3.86832·10⁻¹⁷⁰ | **−17.803** |
| 8.95·10⁻⁴⁰ (RLARGE l.611) | 1.88863·10⁻¹⁶⁵ | 1.88863·10⁻¹⁶⁷ | **−15.114** | 3.02181·10⁻¹⁷⁰ | **−17.910** |
| **6.7·10⁻⁴⁰ (RLARGE l.72, headline)** | 5.93136·10⁻¹⁶⁶ | **5.93136·10⁻¹⁶⁸** | **−15.617** | 9.49018·10⁻¹⁷¹ | **−18.413** |
| proposed 9.38495112638·10⁻⁴⁵ | 2.28341·10⁻¹⁸⁵ | 2.28341·10⁻¹⁸⁷ | **−35.032** | 3.65345·10⁻¹⁹⁰ | **−37.828** |

DX′ = 2.456·10⁻¹⁵²/C_Ω (REVIEW_SF_S7 l.203, DX′-1 (iii)), at C_Ω = 1; every row is linear in C_Ω.

> ### **a_RS's ceiling BINDS TODAY. EPS1_SWEEP's −15.62 / −35.03 reproduce exactly (−15.617 / −35.032).**
> Not SIGN-FRAGILE: the margin is negative at **all four** live ε_1 values and under **both** conventions,
> and the spread across the four is only 1.11 decades against margins of 14.5-18.4. **RLARGE l.618's
> unscoped "RLF's own ceilings do not bind at the current constants" is FALSE, and I confirm it
> independently of EPS1_SWEEP.**

**One correction, in the unfavourable direction [SOURCE-DISAGREES with EPS1_SWEEP §4.3].** EPS1_SWEEP
applies the bare /10². But RLARGE l.1023 prices n bad cubes as **(Ce^{−a_RS/g_k²})^{n/c_RS}** with
**c_RS = 5⁴ = 625** (l.1021), and l.1024 forms **a_♯ := min{a″, a_♭, a_RS/c_RS}** — so the exponent
actually carried per cube is a_RS/c_RS, not a_RS. Requiring the per-cube weight to beat the L⁴ cube
entropy gives a denominator between 10² and c_RS·10²; **the two columns above bracket the honest
requirement, and both have the same sign.** The true margin today is therefore between **−15.62 and
−18.41 decades**, i.e. **up to 2.80 decades worse than reported**.

### §2.3 The scope caveat that the finding needs, and that EPS1_SWEEP does not state [ARGUED]

**RLARGE l.832** (a v3 reading note): *"**§7.1:** n_* unchanged; **a_♯, c_RS = 5⁴ and n_♯ := ⌊4/(a_♯β_-)⌋
are superseded by §3.5 and §5.2** (a = min{θa_bad, a_A})."* So v3 has retired the §7.1 *bookkeeping* that
carries a_RS into the cutoff. Two facts cut the other way and are why I do not treat a_RS as dead:
- **l.830 (also a v3 note) keeps a_RS live**: *"§6 Lemma RS: … is not implied by (F_R): **factor
  e^{a_RS R}**"* — v3 is still correcting Lemma RS's pricing *in a_RS*.
- Lemma RS is v3-live (it is what makes **RLF-F4 AVOIDED**, l.1007, l.1226), and its output is a weight
  with a_RS in the exponent. **Any** such weight must have its base below 1 against the C_ℓ-type
  constants, which is exactly l.616-617's condition.

> **So the finding stands, but its honest statement is: *as RLARGE now reads*, l.616-617's convention
> applies to a_RS and a_RS binds. If v3 intends a_RS to enter no smallness condition at all, that has to
> be SAID — l.832 retires the symbols a_♯/n_♯, not the exponent. Either way RLARGE l.618 needs editing:
> the sentence is false under the first reading and unsupported under the second.** This is finding
> **(G6)** of my own pre-registered list, and it is why I report (V2) as CONFIRMED-at-scope rather than
> unconditionally.

---

## §3. T2 — REBUILDING KN-STEP'S LINEAR η_1 ON OUR STRUCTURES (not citing it)

Status: **PROVEN** (complete, from the stated hypotheses H1-H7, every one of which is checked against
RLARGE in §3.3). RLARGE l.633 lists *"EXISTENCE: Lemma KN, Corollary KN-step"* as PROVEN-HERE reviewed —
**in the other lane**; the standing rule requires the rebuild, and the rebuild is below. Internal
inequalities verified in `checks/ar1c_knrebuild_posthoc.py` → `ar1c_out.txt` (**POST-HOC**, no
pre-registered verdict).

### §3.1 First: WHY RLARGE's η_1 is quadratic. The quadratic entry is not a choice.

RLARGE's (R4) (l.995-999) bounds the kernel by expanding about the **straight transporter S_c**:

  1 − N⁻¹Re tr(V_c⁻¹M̄_c) ≥ ‖V_c − S_c‖²_op/(2N) − **δ_c**,  δ_c := max_{σ,y}‖T^σ_y − S_c‖_op ≤ A_dη  (R1),

and the maximiser step costs a second δ_c, giving the bracket **‖V_c − S_c‖²/(2N) − 2δ_c**. On the event
‖V_c − S_c‖ ≥ ε_1/8 the first term is ε_1²/(128N), so the bracket is useful only if

  **2A_dη_1 ≤ ε_1²/(256N)  ⟺  η_1 ≤ ε_1²/(512N·A_d)** — exactly the quadratic entry of l.64.

> **This is (G5) of my pre-registered list, and it is REAL: the quadratic η_1 is *derived* from (R4)'s
> linear δ_c loss. It cannot be swapped for c_1ε_1 as a constant. (R3) and (R4) must BOTH be replaced.**
> EXISTENCE l.1767 names the same thing from its own side: Lemma KN *"removes the **linear δ_c loss** of
> RLARGE Lemma RS (R4)"*.

### §3.2 The rebuild

**Lemma KN′ (re-centred kernel concentration; rebuilt here).** Let M̄ = Σ_i w_i T_i with **w_i ≥ 0,
Σw_i = 1**, each T_i = S e^{X_i} ∈ SU(N) with X_i ∈ su(N), and put δ := max_i‖X_i‖_op ≤ 1/4,
X̄ := Σ_i w_i X_i, **W′ := S e^{X̄}**. Assume g² ≤ κ. Then ‖W′^{-1}M̄ − 1‖_op ≤ 3δ², and for every
t ≥ 12√N δ²,

  ∫_{‖V − W′‖_HS ≥ t} k(V, M̄) dV ≤ e·c_N^{-1}(κ/g²)^{N²−1} **e^{−κt²/(4Ng²)}**.

*Proof.* Write R := W′^{-1}M̄ − 1. Using Σ_i w_i X_i = X̄,
R = Σ_i w_i[(e^{−X̄} − 1)(e^{X_i} − 1)] + (e^{−X̄} − 1 + X̄) + Σ_i w_i(e^{X_i} − 1 − X_i), whence
‖R‖ ≤ (e^δ − 1)² + δ²e^δ ≤ δ²(e^{2δ} + e^δ) ≤ **3δ²** for δ ≤ ¼. [Checked: the ratio
((e^δ−1)² + δ²e^δ)/δ² is increasing and equals **2.57475** at δ = ¼; EXISTENCE's own looser form
e^{1/2} + e^{1/4} = **2.93275** ≤ 3. `ar1c` [1].]
Put Z := W′^{-1}V ∈ SU(N) and x := ‖V − W′‖_HS = ‖1 − Z‖_HS. For unitary Z,
‖1 − Z‖²_HS = tr(2 − Z − Z^†) = 2 Re tr(1 − Z^{-1}) **exactly** (`ar1c` [3]). With
|tr(AB)| ≤ ‖A‖_HS‖B‖_HS,

  Re tr((W′^{-1} − V^{-1})M̄) = Re tr((1 − Z^{-1})(1 + R)) ≥ ½x² − x√N‖R‖_op ≥ ½x² − 3√Nδ²x ≥ **¼x²**

for x ≥ 12√Nδ² — and that threshold is **forced algebraically**, not estimated: ½x² − 3√Nδ²x ≥ ¼x² is
*equivalent* to x ≥ 12√Nδ² (`ar1c` [2]). D4-norm (2) gives
𝒩(M̄) ≥ e^{−(κ/g²)(1 − N^{-1}Re tr V_0^{-1}M̄)}e^{−1}c_N(g²/κ)^{N²−1} with V_0 the SU(N)-maximiser, and
Re tr(V_0^{-1}M̄) ≥ Re tr(W′^{-1}M̄) since W′ is a candidate. Hence
k(V) ≤ e c_N^{-1}(κ/g²)^{N²−1}exp(−(κ/(Ng²))Re tr((W′^{-1} − V^{-1})M̄)) ≤ (same)·e^{−κx²/(4Ng²)}; Haar
mass ≤ 1. ∎

**The mechanism, in one line:** centring at **W′ instead of S** makes the error term **quadratic** in δ
(the ‖R‖ ≤ 3δ² above) where RLARGE's (R4) had it **linear** (the −2δ_c). That is the whole 82 decades.

**Corollary KN-step′ (the re-centred dichotomy; rebuilt here).** With **c_1 := 1/(2(L² + 5.5A_d(L)))**
(= **1/117** at d = 4, L = 3), for a coarse plaquette P and η := max{‖1 − U_k(p)‖_op : p a fine plaquette
of U_4(P)}, provided

  **t ≤ 1/(106√N·A_d²c_1²)**  and  **(π/3)A_dc_1t ≤ 1/4**,

the dichotomy *"‖1 − V_P‖ ≥ t ⟹ either η ≥ c_1t, or some c ∈ ∂P has ‖V_c − W′_c‖_op ≥ t/8"* holds, and
the second branch is priced by Lemma KN′ at exponent **κt²/(256Ng_k²)**.

*Proof.* ‖1 − V_P‖ ≤ ‖1 − W′_P‖ + Σ_{c∈∂P}‖V_c − W′_c‖ and
‖1 − W′_P‖ ≤ ‖1 − S_P‖ + Σ_c‖W′_c − S_c‖ ≤ **L²η** (RS (R2)) **+ 4(e^δ − 1)** with δ ≤ (π/3)A_dη
(RS (R1) plus |θ| ≤ (π/3)‖e^{iθ} − 1‖ for ‖·‖ ≤ 1). For δ ≤ ¼,
4(e^δ − 1) ≤ 4·((e^{1/4} − 1)/(1/4))·(π/3)·A_dη = **4.75889 A_dη ≤ 5.5 A_dη** (`ar1c` [4]). So on
{η < c_1t},

  ‖1 − W′_P‖ ≤ (L² + 5.5A_d)η < (L² + 5.5A_d)c_1t = **t/2  exactly**, since (L² + 5.5A_d)c_1 = ½ identically

— and if in addition all four ‖V_c − W′_c‖ < t/8 then ‖1 − V_P‖ < t/2 + 4·(t/8) = **t**. The dichotomy is
therefore **exhaustive by construction** (`ar1c` [4]), and the t/8 is what makes it so. Lemma KN′ applies
at threshold t/8 provided t/8 ≥ 12√Nδ², and δ ≤ (π/3)A_dc_1t gives
**t ≤ 1/(8·12·(π/3)²√N·A_d²c_1²) = 1/(105.276√N·A_d²c_1²)** — which **rebuilds EXISTENCE l.1775's
coefficient 106 to a ratio of 1.00688** (`ar1c` [5]). The kernel exponent is
κ(t/8)²/(4Ng²) = **κt²/(256Ng²)**. ∎

**With t = ε_1 this delivers, in place of RLARGE (R3)+(R4):**

  **η_1 := c_1ε_1   (LINEAR)**,  kernel branch exponent **κε_1²/(256N)**,
  plaquette branch (RS (R5), unchanged in form) **a_η = η_1²/(2N) = c_1²ε_1²/(2N)**.

> **A structural check with real force, and it passes: the kernel branch constant is IDENTICAL before and
> after.** RLARGE (R4) reaches κε_1²/(256N) by halving ε_1²/(128N) to absorb 2δ_c; KN′ reaches
> κε_1²/(256N) from ¼·(ε_1/8)². **Same constant, two different routes** (`ar1c` [7]). So the adoption
> changes **exactly one entry** of a_RS = min{a_η, κε_1²/(256N)} and leaves the other numerically
> untouched — which is why no other RLARGE constant moves.

### §3.3 The hypotheses, and whether RLARGE supplies each one — **the heart of T2**

| | hypothesis of KN′/KN-step′ | where RLARGE supplies it | verdict |
|---|---|---|---|
| **H1** | M̄ is a **probability** mixture Σw_iT_i, w_i ≥ 0, Σw_i = 1 | RLARGE l.992: *"M̄_c is **a mean of** the T^σ_y"*, over S4′ contour orders σ and endpoints y | **AVAILABLE but UNDER-STATED — the one residual, see (G1) below** |
| **H2** | a **common** S with T_i = S e^{X_i}, X_i ∈ su(N) | RS (R1) gives ‖T^σ_y − S_c‖_op ≤ A_dη for the single straight transporter S_c (l.970, l.973) | **AVAILABLE** |
| **H3** | the **traceless-log chart**: a traceless X with e^X = S_c^{-1}T and ‖X‖ ≤ (π/3)‖S_c^{-1}T − 1‖ | det = 1 puts Σθ_j ∈ 2πZ and |θ_j| ≤ (π/3)A_dη each, so Σθ_j = 0 whenever **η < 6/(NA_d)**, i.e. ε_1 < **78/N** at d = 4, L = 3. Live ε_1 ≈ 10⁻⁴⁰ | **AVAILABLE** (`ar1c` [6]); note the **N-dependence**, which binds only for N ≳ 39 at ε_1 ≈ 2 |
| **H4** | δ ≤ 1/4 | (π/3)A_dc_1ε_1 ≤ ¼ ⟺ ε_1 ≤ **3.10352**; EXISTENCE l.1772's weaker "A_dη ≤ 1" likewise | **AVAILABLE** (holds at every live ε_1; FAILS at the counterfactual t = 10, `ar1_out.txt` ar1-3 (b)) |
| **H5** | t ≤ 1/(106√N A_d²c_1²) = **1.12737** (N = 2), **0.920492** (N = 3) | t = ε_1 ≈ 10⁻⁴⁰ | **AVAILABLE** (FAILS at the counterfactuals t = 2, 10, 1000) |
| **H6** | g² ≤ κ, and **D4-norm (2)** | RS (R4) **already assumes both** (RLARGE l.978, l.996). No new import | **AVAILABLE — same tool RLARGE already uses** |
| **H7** | conditional independence of the four coarse-link kernels given U_k | RLARGE §0 **Lemma TD**; and RS (R4) itself: *"for distinct coarse links the bound multiplies"* (l.980) | **AVAILABLE** |

> ### **(G1) HYPOTHESIS GAP, and it is one word wide.**
> **H1 is the only hypothesis RLARGE does not state.** Lemma KN′ needs M̄_c to be a mixture with
> **nonnegative weights summing to 1**; RLARGE l.992 says only *"M̄_c is a mean of the T^σ_y"*. The S4′
> average is a probability average by construction (RLARGE §0's S4′ averaging), so this is almost
> certainly a wording gap and not a mathematical one — but it is **load-bearing**: KN′'s convexity step
> (‖R‖ ≤ 3δ² via Σw_iX_i = X̄) is false for signed weights. **Status of the repair on this account:
> CONDITIONAL on RLARGE stating that the S4′ weights defining M̄_c are nonnegative and normalised.**
> I flag it because the project's record is that exactly this kind of unstated positivity is what
> EXISTENCE's own (RLF-3^dis) and Lemma MIX turn on (EXISTENCE l.1718, l.1729-1731 both hinge on
> *"nonnegative history weights"*). **This is the most likely answer I found to "why was it requested and
> not adopted" — together with §1.1's finding that RLARGE actually chose the other horn.**

### §3.4 What the repair does NOT fix [CONDITIONAL — name the input]

**a_RS's STATUS is unchanged; only its SIZE moves.** RLARGE l.1020 says a_η comes from **(PLD)_k (i)** at
effective levels. PLD §15 and REVIEW_PLD_S3 establish that **(PLD)_k at τ = η_1 is not derivable in-step**
at *any* RS-compatible threshold: REVIEW_PLD_S3 l.304-309 — *"every RS-compatible threshold satisfies
η_RS ≤ ε_1/L²(1 + o(1))"*, INH realises every η < ε_1/L² with cut-good V, *"hence no choice of thresholds
puts η_RS in PLD-desc's in-step range"*, and l.309: ***"Choosing η_1 relative to τ_bg cannot restore
in-step derivation."*** REVIEW_PLD_S3 l.356 adds that (PLD)_k at η_1 is *"very plausibly TRUE with uniform
constants"* and that what fails is only the in-step proof. **That obstruction is threshold-independent and
so is untouched by this repair.** Honest label: **a_RS is CONDITIONAL on (PLD)_k (i) both before and
after; the repair makes it 82 decades larger, not better-founded.**

---

## §4. T3 — CARRY-THROUGH: EVERY ENTRY η_1 TOUCHES, BEFORE AND AFTER

[COMPUTED exact, `ar1_out.txt` / `ar1b_out.txt`; the n_♯ and m_τ rows are marked POST-HOC where they were
not pre-registered.]

### §4.1 The headline row

| | at today's ε_1 = 6.7·10⁻⁴⁰ | at the proposed 9.38495112638·10⁻⁴⁵ |
|---|---|---|
| η_1, quadratic (RLARGE l.64) | 4.87088·10⁻⁸³ | 9.55700·10⁻⁹³ |
| η_1, linear (KN-step) | 5.72650·10⁻⁴² | 8.02133·10⁻⁴⁷ |
| a_RS, quadratic | 5.93136·10⁻¹⁶⁶ | 2.28341·10⁻¹⁸⁵ |
| a_RS, linear | 8.19819·10⁻⁸⁴ | 1.60854·10⁻⁹³ |
| **margin vs DX′, quadratic, /10²** | **−15.617** | **−35.032** |
| **margin vs DX′, linear, /10²** | **+66.523** | **+56.816** |
| margin, quadratic, /(c_RS·10²) | −18.413 | −37.828 |
| margin, linear, /(c_RS·10²) | +63.728 | +54.020 |
| **GAIN** | **+82.141 decades** | **+91.848 decades** |

**EPS1_SWEEP's +66.52 and +56.82 both reproduce to 0.01 decade.** The repair turns a 15.6-decade breach
into a 66.5-decade margin today, and a 35.0-decade breach into a 56.8-decade margin under the (undecided,
owner-gated) ε_1 move. **At the c_RS-corrected convention it is +63.73 / +54.02 — still a clean
NOT-BINDING.** I have not changed ε_1 and do not recommend that it be changed.

> ### **[ar1-5] SOURCE-DISAGREES on the headline "92 decades". The gain at TODAY's ε_1 is 82.141 decades, not 92.**
> EPS1_SWEEP §4.3 writes *"the ceiling moves from −15.62 to +66.52 decades against DX′ — a gain of 92
> decades"*, and §7.1 item 2 says *"a gain of **92 decades at today's ε_1**"*. PROOF.md l.63-66 and this
> worker's brief repeat it. But 66.523 − (−15.617) = **82.141**; the **91.848** ≈ 92 is the gain **at the
> proposed ε_1** (56.816 − (−35.032)). The discrepancy is **exactly 2 × 4.854 = 9.707 decades**, which is
> structurally right: the gain is the difference of an ε_1⁴ and an ε_1² margin, so lowering ε_1 by 4.854
> decades *increases the gain* by twice that. **Both of EPS1_SWEEP's own margin figures are correct; only
> their difference is attributed to the wrong ε_1.** Direction: **unfavourable to the headline by 9.71
> decades**; no verdict changes, and 82 decades is still decisive.

### §4.2 The other η_1-touched entries [POST-HOC for n_♯ and m_τ; not pre-registered]

| quantity | formula, citation | quadratic η_1 | linear η_1 | change |
|---|---|---|---|---|
| **a_♯ = min{a″, a_♭, a_RS/c_RS}** (l.1024) | a″ = 0.9ε_1²/(4N) = 5.05012·10⁻⁸⁰ (l.1245) | **9.49018·10⁻¹⁶⁹** (a_RS/c_RS binds) | **1.31171·10⁻⁸⁶** (a_RS/c_RS still binds) | +82.14 |
| **n_♯ = ⌊4/(a_♯β_-)⌋** (l.1024) | β_- = 0.186 (l.612) | **2.26607·10¹⁶⁹** | **1.63949·10⁸⁷** | **−82.14 decades** |
| its level count log_L(2n_♯) | l.612's W-convention, applied to n_♯ | **355.6 levels** | **183.4 levels** | **−172.2 levels** |
| same, at the proposed ε_1 | | 5.88632·10¹⁸⁸ / 396.3 levels | 8.35593·10⁹⁶ / 203.8 levels | −191.8 decades of n_♯ |
| **m_τ** (REVIEW_PLD_S3 Arch-3) | least m with (L²/2C_I)^mη_1 ≥ 2C_Iε_1/L² | **66 / 90 / 122** (C_I = 1/1.5/2) at 6.7·10⁻⁴⁰; **73 / 100 / 136** at the proposed | **3 / 4 / 5, ε_1-INDEPENDENT** | the ε_1-dependence is **removed** |
| HIST's chain-energy floor E_𝒞(p) ≥ η_1²/(2NC_cone) | **HIST l.1377-1379** | — | — | **+82.14 decades** |
| RLARGE l.1184's per-plaquette cost e^{−η_1²/(2Ng_{k−1}²)} | l.1184 | — | — | **+82.14 decades** |
| kernel branch κε_1²/(256N) | l.1020, l.979 | 8.76758·10⁻⁸² (1.72026·10⁻⁹¹ at the proposed ε_1) | identical | **exactly invariant (§3.2)**; never the active entry of the min (it would need ε_1 > 814.587) |
| n_*, a″, a_bad, a, n_H, the l.612 wrap count | l.1017, l.1245, l.88, l.87, l.612 | — | — | **contain no η_1: UNCHANGED** |
| (TC) for the collar (l.66-68), ε_loc, η_q | uses **η_q**, not η_1 | — | — | **UNCHANGED** |

> **A substantive by-product, and it is a second defect in RLARGE §5.4's table.** l.612 reports **≈ 184
> wrap levels** from n_H ≳ 2·10⁸⁷. But l.1024 says *"the induction uses n_c = n_♯"*, and at the current
> quadratic η_1 **n_♯ = 2.27·10¹⁶⁹, whose level count is 355.6 — 172 levels worse than the number the
> table records.** Under the repair n_♯ falls to 1.64·10⁸⁷ and its level count to **183.4**, i.e.
> **essentially equal to n_H's 183.6**, so the table becomes self-consistent. I report the coincidence as
> a coincidence, not a derivation, and the row as **ARGUED by analogy with l.612's own W-convention**: the
> wrap convention is RLARGE's to apply. Caveat: l.832 declares the a_♯/n_♯ symbols superseded (§2.3), so
> this row is **CONDITIONAL on the same reading question as §2.3**.

### §4.3 Sensitivity to which a_η constant is used [COMPUTED]

a_η's *constant* is multi-valued across the lane while its **η_1² scaling is not**: η_1²/(2N) (RLARGE
l.1026 / (R5) l.981), a_kη_1²/16 (PLD l.197), a_dη_1² (PLD l.276), **49η_1²/(256σ_*²)** (PLD l.1044,
l.1048 — the effective-level value a_RS actually names). At the Gaussian instance σ_*² = N(1 + 18/κ)
(PLD l.341), the last is ×49.6 **smaller** than RLARGE's bare-level value, i.e. 1.70 decades worse:

| | margin, quadratic | margin, linear |
|---|---|---|
| today's ε_1, PLD's a(η_1) | **−17.313** | **+64.828** |
| proposed ε_1, PLD's a(η_1) | **−36.727** | **+55.120** |

**No sign changes.** The finding and the repair are both robust to which a_η constant is taken; only the
margin size moves by ≈ 1.7 decades.

---

## §5. T5 — CONSUMER SWEEP: WHAT THE LINEAR η_1 BREAKS

Pre-registered hazard direction (G3): the linear η_1 is **≈ 41 decades LARGER** than the quadratic one at
the live ε_1, so the consumers at risk are those needing η_1 **small**.

### §5.1 **ORDER-REVERSED: the one recorded fact that the adoption falsifies** [COMPUTED]

**RLARGE l.65** records, with a review's endorsement: *"For ε_1 ≤ 2, **η_1 ≤ η_q** unless δ_0/A_d binds
(**"CORRECT", REVIEW_RLARGE_V2 §2.3**)."* Under the adoption:

| form | η_1/η_q, N = 2 | N = 3 | verdict |
|---|---|---|---|
| quadratic (now) | 3.35·10⁻⁴⁰ | 3.35·10⁻⁴⁰ | ORDER-PRESERVED |
| **linear (KN-step)** | **39.3846** | **59.0769** | **ORDER-REVERSED** |

(η_q := min{ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d}, l.64; the δ_0 entry is unevaluated and omitted, which can
only make η_q smaller and the reversal larger. The ratio 4608/117 = 39.3846 is the same number
REVIEW_PLD_S3 l.433 reports as *"c_1ε_1/η_1 = 39-229"* at its own ε_1 range — an independent arrival at
the same constant.)

**What consumes the ordering, and what happens:**
- **HIST l.186**: *"the reduction of n_♯ comes from c_RS = 81 against 5⁴ = 625, and the rest from **η_q²
  against η_1²**"* — HIST's joint route (Lemma RS-lin) is the better route **precisely because** η_q is
  linear and η_1 quadratic. **After the adoption the comparison reverses: the RS route's exponent becomes
  (η_1/η_q)² = 1551× BETTER than the joint route's** (N = 2). HIST l.181's *"for ε_1 → 0,
  η_q/η_1 = 2/ε_1"* becomes η_q/η_1 = 117/4608 = 0.0254, a constant.
- **This is an improvement, not a breakage** — larger η_1 means larger a_η, hence a higher ceiling and a
  smaller n_♯. But it **invalidates a comparison HIST has banked**, and HIST l.151's *"PM is what makes
  the threshold linear (Lemma RS-lin)"* stops being the only way to a linear threshold. **Nothing fails;
  one recorded ordering and one route-superiority claim must be restated.** Request filed in §8.
- **No consumer anywhere bounds a quantity BY η_1 from above** in a way that the larger value breaks: I
  grepped all 16 RLARGE, 9 HIST, 16 PLD, 2 SF, 1 PROOF and 2 EXISTENCE occurrences (§1). Every one either
  (i) is the (R3)/(R5) dichotomy threshold itself, (ii) carries η_1², which improves, or (iii) is a
  different symbol.

### §5.2 The three consumers that could have failed, and did not [COMPUTED]

| consumer, with its independent source | test | result |
|---|---|---|
| **RS-compatibility ceiling.** REVIEW_PLD_S3 l.302, l.305: *"every RS-compatible threshold satisfies η_RS ≤ ε_1/L²(1 + o(1))"*, stated as η ≤ ε_1/(1.001L²) — a threshold fixed before this proposal, for a different question | c_1ε_1 = 5.72650·10⁻⁴² against the bound 7.43701·10⁻⁴¹ | **RS-COMPATIBLE**, with ×12.99 to spare. Power: at the counterfactual c_1 = 1/6 the same check returns **RS-INCOMPATIBLE**; at c_1 = 1/(2L²) = 1/18 it is compatible by only ×2.0 — so c_1 = 1/117 is comfortably inside and the hoped-for O(ε_1/L²) of RLARGE §11 item 7 would have been **marginal** |
| **PLD's LD-arith no-go.** PLD l.765-776: route (a) needs αt²β_1 > log n_U/log L, α = 1/(2(N−1)), n_U = 24L⁴ | log n_U/log L = **6.89279** (PLD states 6.893). Least N: **37** at t = 2, **593** at t = ½, **507954** at t = 2/117 | **SU23-STANDS.** Not summable at N = 2, 3 under **either** form, so PLD's conclusion *"route (a)'s answer is no for SU(2), SU(3)"* survives the adoption. **All three of REVIEW_PLD_S3 l.160-162's independently scanned values reproduce exactly** |
| **m_τ, the coherent-descent depth.** REVIEW_PLD_S3 l.346-350 | RS form: **5/7/10** at ε_1 = 2, **6/8/12** at 0.517, **10/14/19** at 10⁻³, **54/74/101** at 2·10⁻³² — **all four reproduce l.347 exactly, integer for integer**; KN form **3/4/5**, reproducing l.349 | **MTAU-REPRODUCES.** And the adoption *removes* m_τ's ε_1-dependence (l.350: *"Either way the depth is g-independent, but 'm_τ = 3' is not RLARGE's number"* — after the adoption it is) |

### §5.3 Proposition INH is unaffected, and so is its obstruction

**PLD Proposition INH (PROVEN-HERE, l.1066)** is *stated at* c_1ε_1 — i.e. at symbol 2 — but
REVIEW_PLD_S3 l.300-302 established it *"holds for any threshold η < ε_1/L²"* and **a fortiori** with
RLARGE's η_1. So INH is insensitive to the choice, in both directions. **Its obstruction (§3.4) is
likewise threshold-independent.** No change.

---

## §6. VERDICTS

### §6.1 On EPS1_SWEEP's finding

> ### **CONFIRMED, with three corrections, one of which makes the problem WORSE.**

- **(V1) the ε_1⁴ exponent: CONFIRMED** [COMPUTED, exact]. EXP-4 at every live and proposed ε_1, N = 2
  and 3, re-derived from RLARGE l.64 + l.981/l.1026 + l.1020 alone. The crossovers (512 / 768 and
  814.587) are reproduced.
- **(V2) a_RS binds today: CONFIRMED at scope** [COMPUTED]. Margin **−15.617** at RLARGE's headline ε_1
  and negative at **all four** live values (−14.506, −15.007, −15.114, −15.617) and under **both**
  conventions (to −18.413). Not SIGN-FRAGILE. **RLARGE l.618's unscoped sentence is FALSE.** Scope: see
  §2.3 — it is false under the live reading of l.830 and unsupported under l.832's.
- **Correction 1 [SOURCE-DISAGREES, direction UNFAVOURABLE].** The honest ceiling carries **c_RS = 625**
  (RLARGE l.1021/l.1023/l.1024), so the margin today is between **−15.62 and −18.41 decades** — up to
  **2.80 decades worse** than reported.
- **Correction 2 [SOURCE-DISAGREES, direction UNFAVOURABLE to the headline].** The gain at **today's** ε_1
  is **82.141 decades, not 92**; 91.848 is the gain at the **proposed** ε_1. §4.1.
- **Correction 3 [reading].** The adoption was **not** merely "requested and not carried out": E9 was an
  either/or and **RLARGE v3 chose the other horn at l.830**. §1.1.

### §6.2 On the repair

> ### **ADOPTABLE, and CONDITIONAL on exactly one stated input.**

- **Lemma KN′ and Corollary KN-step′: PROVEN** here from hypotheses H1-H7 (§3.2), rebuilt rather than
  cited, with EXISTENCE's constants **106** (rebuilt as 105.276, ratio 1.00688) and **5.5** (rebuilt as
  4.75889 ≤ 5.5) independently recovered, and the identity (L² + 5.5A_d)c_1 = ½ verified exactly.
- **H2-H7 are all AVAILABLE in RLARGE** at the point of consumption, and H6 is the *same* D4-norm (2) and
  g² ≤ κ that RS (R4) already uses — **no new import**.
- **CONDITIONAL on H1**: that the S4′ weights defining M̄_c (RLARGE l.992, *"a mean of the T^σ_y"*) are
  **nonnegative and normalised**. KN′'s convexity step is false without it. One sentence in RLARGE
  discharges it; until then the repair is CONDITIONAL and I will not call it PROVEN-in-RLARGE.
- **The adoption is a replacement of (R3) AND (R4), not a constant swap** (§3.1) — the quadratic η_1 *is*
  (R4)'s linear-δ_c condition. The kernel-branch constant comes out identical, so nothing else moves.
- **Nothing breaks.** One recorded fact is falsified — **RLARGE l.65's η_1 ≤ η_q** — and one route
  comparison (HIST l.186) reverses in the *favourable* direction. Both need restating, neither fails.
- **It does not change a_RS's STATUS**, which is CONDITIONAL on (PLD)_k (i) before and after (§3.4).

### §6.3 Status summary

| item | status |
|---|---|
| a_RS ∝ ε_1⁴ under RLARGE's current η_1 | **COMPUTED (exact)** |
| a_RS's coupling ceiling is below DX′ at every live ε_1 | **COMPUTED (exact)**, CONDITIONAL on §2.3's reading and on C_Ω, DX′ remaining the binding ceiling |
| RLARGE l.618's unscoped sentence | **FALSE** |
| Lemma KN′ + Corollary KN-step′, rebuilt | **PROVEN** from H1-H7 |
| the hypotheses H2-H7 available in RLARGE | **PROVEN (reading, cited line by line)** |
| H1 (nonnegative normalised S4′ weights) | **CONDITIONAL — the named input; owner: RLARGE** |
| margin after adoption: +66.52 (today), +56.82 (proposed); +63.73 / +54.02 with c_RS | **COMPUTED (exact)** |
| gain 82.141 (today) / 91.848 (proposed) | **COMPUTED (exact)**; SOURCE-DISAGREES with the quoted 92-at-today |
| η_1 is three symbols; PLD and RLARGE differ | **COMPUTED (reading)** |
| η_1 ≤ η_q (RLARGE l.65) after adoption | **FALSE** — reverses to 39.4× (N = 2) |
| a_RS's status (CONDITIONAL on (PLD)_k (i)) | **unchanged by the repair** |
| n_♯ falls 82.14 decades; its level count 355.6 → 183.4 | **COMPUTED**, the level-count row **ARGUED by analogy** with l.612 |


---

## §7. CHECKS, POWER, THE ONE FAIL, AND DISCLOSURES

### §7.1 The check table

| id | pre-registered verdict | result |
|---|---|---|
| **ar1-1** | EXP-4 / EXP-2 / EXP-OTHER | **EXP-4** at all four live ε_1 and the proposed one, N = 2 and 3; **EXP-2** at the counterfactuals |
| **ar1-2 (V2)** | BINDS / NOT-BINDING, all live ε_1, both conventions | **BINDS at all ten rows** → (V2) **CONFIRMED** (not SIGN-FRAGILE) |
| **ar1-2 (V3)** | same grid, linear form | **NOT-BINDING at all ten rows** → arithmetic half **CONFIRMED** |
| **ar1-3** | HYP-AVAILABLE / HYP-FAILS | **HYP-AVAILABLE**; (c) IDENTITY-HOLDS, (d) REPRODUCES (ratio 1.00688), (e) RECONSTRUCTS, (f) SAME-CONSTANT |
| **ar1-4 (a)** | ORDER-PRESERVED / ORDER-REVERSED | **ORDER-REVERSED** under the linear form (39.3846 at N = 2, 59.0769 at N = 3) |
| **ar1-4 (b)** | RS-COMPATIBLE / RS-INCOMPATIBLE | **RS-COMPATIBLE** (×12.99 to spare); RS-INCOMPATIBLE at the counterfactual c_1 = 1/6 |
| **ar1-4 (c)** | SU23-STANDS / SU23-FAILS | **SU23-STANDS**; 37 / 593 / 507954 all reproduce REVIEW_PLD_S3 l.160-162 |
| **ar1-4 (d)** | MTAU-REPRODUCES / SOURCE-DISAGREES | **MTAU-REPRODUCES** — 5/7/10, 6/8/12, 10/14/19, 54/74/101 and 3/4/5, integer for integer |
| **ar1-5** | GAIN-REPRODUCES / SOURCE-DISAGREES | **SOURCE-DISAGREES**: 82.141 at today's ε_1 against the quoted 92; 91.848 at the proposed |
| **ar1-6** | PASS / FAIL (two precisions) | **PASS** — worst disagreement 4.564·10⁻⁴⁹ decades over 20 margin rows (50 vs 100 digits) |
| **ar1 power line** | both counterfactuals must flip, else NO POWER | **FAIL on the first run** (a reporting bug, §7.2); **HAS-POWER** on the re-run `ar1b` |

### §7.2 **The one FAIL, reported as a FAIL**

`ar1_margins.py`'s power-summary line printed **"NO POWER"** although every one of its 20 margin rows
flips between the two forms. The cause is a bug **in the reporting line, not in the arithmetic**: it
compared the two *aggregate* verdict strings `v2` and `v3`, which are **both** the string `"CONFIRMED"`
(one meaning "BINDS everywhere", the other "NOT-BINDING everywhere"), instead of the per-row
BINDS/NOT-BINDING verdicts.

**`ar1_margins.py` and `ar1_out.txt` are kept byte-unaltered.** Re-run under a **new id**,
`ar1b_power.py` → `ar1b_out.txt`, with the criteria file untouched and with **only** that reporting line
and two display-format lines changed (an unformatted `%s` in the ar1-3 (d) header and a dead "see below"
placeholder in ar1-1). `diff` over all VERDICT, (V2)/(V3) and GAIN lines of the two outputs:
**identical**. The re-run prints the per-row evidence — RS form returns `['BINDS']`, KN form returns
`['NOT-BINDING']` — and **HAS-POWER**.

### §7.3 The power check, as §0.6 required

**Leg 1 — the two forms.** Same script, same constants, same twenty rows: the quadratic form returns
**BINDS** on every row and the linear form **NOT-BINDING** on every row. The verdict is a function of the
η_1 form, not of my bookkeeping.

**Leg 2 — the interpolating exponent.** With η_1^{(s)} := c_1^{1−s}·(1/(512NA_d))^s·ε_1^{1+s} (so
s = 0 is KN-step's linear form, s = 1 is RLARGE's quadratic one, and a_η ∝ ε_1^p with p = 2 + 2s), the
margin crosses zero at

> **p\* = 3.61975 at today's ε_1, and p\* = 3.23718 at the proposed ε_1**

with margin(p\* − 0.01) = **+0.411** and margin(p\* + 0.01) = **−0.411** at today's ε_1 (and ±0.459 at the
proposed). **The verdict demonstrably changes sign across p\*.** This is the single most informative
number in the file: the quartic is over the line today by only **0.38 of an exponent** — any exponent
below 3.62 would not bind — but the ε_1 move pulls the line down to 3.24, so the breach is not marginal
once the move is made. **That is the counterfactual at which my verdict flips, constructed and run.**

**Leg 3 — the hypothesis checks flip too.** ar1-3 (a) **FAILS** at t = 2, 10 and 1000; (b) **FAILS** at
t = 10 and holds at t = 2. ar1-4 (b) returns **RS-INCOMPATIBLE** at the counterfactual c_1 = 1/6. None of
these thresholds was set by anything in this session.

### §7.4 Power grading, honestly

- **ar1-2 is STRONG.** It returns a FAIL against **RLARGE l.618**, a sentence written by a different
  author for a different purpose, and it is tested against **DX′ from REVIEW_SF_S7** — a different owning
  file, written to answer the τ_c question, before this proposal existed. It flips on the form, and it
  flips on the exponent at a boundary (p\* = 3.62) that nothing in this session chose.
- **ar1-4 (c) and (d) are STRONG.** They reproduce **seven** figures (37, 593, 507954; 5/7/10, 6/8/12,
  10/14/19, 54/74/101) that **REVIEW_PLD_S3 obtained by its own independent scan** for the PLD-architecture
  question. Had my reconstruction of PLD's formulas been wrong, these would have disagreed; they agree
  integer for integer, which validates the formulas I then used at the live ε_1 where no published figure
  exists.
- **ar1-3 (d) and (e) are STRONG for a reading check.** They **rebuild EXISTENCE's 106 and 5.5 from Lemma
  KN's own 12 and from e^{1/4}**, and could have exposed either constant as wrong. 105.276 vs 106 and
  4.75889 vs 5.5 are both reproductions, the second with deliberate slack in the safe direction.
- **ar1-1 is MEDIUM.** It is a branch determination from a transcribed formula; it can only catch a
  mis-read of l.64. Its value is that it is the **input** to ar1-2.
- **ar1-3 (a)/(b) at the live ε_1 are WEAK** — they hold by ~40 decades, so they cannot discriminate. I
  report them as satisfied, not as evidence.
- **ar1-6 is WEAK by construction** (it checks my own arithmetic against itself at two precisions).
- **The §3.2 rebuild is the part with no numerical power at all**: it is a proof, and its force is that
  every step is written out and every hypothesis is traced to a RLARGE line in §3.3's table. Its one
  honest residual is H1, which I have labelled CONDITIONAL rather than argued away.

### §7.5 What these checks cannot catch, stated rather than left implied

They cannot validate RLARGE's ε_1 ceiling, SF's DX′ evaluation, HW's b_n or ring price, PLD's σ_*, λ_min
or (SG^net), SQ's η_♭, or the unevaluated **C_Ω, c_+, C_Δ, C_♭, r_♭, N′, c_A**. **Every margin in this
file is linear in C_Ω** and is CONDITIONAL on DX′ remaining the binding programme ceiling
(REVIEW_SF_S7 l.225: C_Ω *"is an explicit hand constant, not a certificate"*). They cannot settle §2.3's
reading question, which is RLARGE's. They cannot find a consumer of η_1 that does not name it. And
**they cannot discharge H1**: whether the S4′ weights are nonnegative and normalised is a reading
question about RLARGE l.992, and I have left it open rather than assume it.

### §7.6 Numerics and provenance

Exact `fractions.Fraction` throughout; `Decimal` for log10 and display only, verified at **50 and 100
digits**. Plain `python3 -I`, single thread (OMP/OPENBLAS/MKL = 1), `nice 10`, **no numpy, no BLAS**.
**2.1 s real** for ar1, under a second for ar1b and ar1c. **No numeric lock taken and none needed**
(exact rational arithmetic, brief rule 6); machine load was 3.89 at the start. **No git command was run
by me.** π and e are 50-digit truncations and √N a 60-digit truncation; they enter only ar1-3 (c)-(e) and
ar1-4 (c), where the slack is tens of decades or the comparison is against an integer, so **no verdict
turns on the truncation** (disclosed in both outputs' footers).

File order, by mtime converted to UTC (host clock UTC−4):
**ARS_FIX.md §0 at 15:11Z** (the pre-stated section; its stamp was read from `date -u` immediately before
writing) → `ar1_criteria.md` **15:20:49Z** → `ar1_margins.py` **15:23:19Z** → `ar1_out.txt`
**15:23:26Z** → `ar1b_power.py` **15:24:37Z** → `ar1b_out.txt` **15:24:47Z** →
`ar1c_knrebuild_posthoc.py` **15:27:37Z** → `ar1c_out.txt` **15:27:52Z** → §1-§8 of this file.
**The pre-stated section precedes the criteria by 9 minutes, and the criteria precede the first script by
2.5 minutes.**

**Disclosure on provenance, as the lane's convention requires** (EPSSTAR §8.1, STAR_CONST §12,
TAUFLAT §5.2, EPS1_SWEEP §6): this file has been appended to since §0 was written, so **its mtime is now
that of the last append and the 15:11Z creation time of §0 is not demonstrable from the filesystem** —
only the check files' order is. What *is* demonstrable is that `ar1_criteria.md` contains **no numerical
constant of any kind** and precedes every script, and that §0 cites **no quantity produced in session
24** and **no number at all** beyond the two tolerance factors it declares. §0's byte size, measured on the file as
it now stands (lines 1-191, through its own end-marker): **14 659 bytes** (`ar1_criteria.md`:
**8 251 bytes**).

Files written by me: **ARS_FIX.md**, `checks/ar1_criteria.md`, `checks/ar1_margins.py`,
`checks/ar1_out.txt`, `checks/ar1_err.txt`, `checks/ar1b_power.py`, `checks/ar1b_out.txt`,
`checks/ar1b_err.txt`, `checks/ar1c_knrebuild_posthoc.py`, `checks/ar1c_out.txt`,
`checks/ar1c_err.txt`. **Nothing else, anywhere.** I did not touch RLARGE.md, PLD.md, HW.md,
EXISTENCE.md, EPS1_SWEEP.md, SF.md, HIST.md, SQ.md, BFT_*.md, NORMS.md, GREENT.md, YSUP.md, PROOF.md,
HANDOFF.md, SESSION24_RESULTS.md or any REVIEW_* file.

### §7.7 The single biggest remaining obstruction in my scope

**Not the arithmetic — the decision.** The repair is one lemma replacement in RLARGE §6 worth **82 decades
today**, its hypotheses are all available bar one word (H1), and nothing breaks. What stands in the way is
that **RLARGE v3 already decided this question the other way at l.830**, without the price in front of it,
and **the price was never computed until today**. Below that sits the obstruction the repair does **not**
touch: **a_RS is CONDITIONAL on (PLD)_k (i), which REVIEW_PLD_S3 l.304-309 shows is not derivable in-step
at any RS-compatible threshold.** Making a_RS 82 decades larger does not make it proven.

---

## §8. FOR OTHER FILES (not edited)

I wrote only ARS_FIX.md and `checks/ar1*`. The following are requests on their owners.

### §8.1 For RLARGE's owner — binding, and the largest item here

1. **l.618 is false as written and must be edited regardless of what else is decided.** *"RLF's own
   ceilings do not bind at the current constants"* is true for the exponent l.617 names and **false for
   a_RS**, whose ceiling sits **15.62 to 18.41 decades BELOW** DX′ = 2.456·10⁻¹⁵²/C_Ω **at every one of the
   four live ε_1 values**, today, with no change to anything. Confirmed independently of EPS1_SWEEP
   (§2.2). Minimum edit: scope the sentence to the (REG-min)/HW route as l.617 already does, and add one
   line recording the RS/joint route's ceiling.
2. **Reopen E9, and this time with the price.** **l.830's v3 note *"η_1 is v2/v3's η_1 (E9)"* is a
   decision, not an omission** — REVIEW_PLD_S3 l.462 offered two horns and v3 took the second. The first
   horn (adopt η_1 := c_1ε_1, EXISTENCE l.1771) is worth **+82.141 decades at today's ε_1** and
   **+91.848 at the proposed one**; the second horn (fix PLD's text) is worth **nothing** on this ceiling.
   §1.1, §4.1.
3. **The adoption is a replacement of (R3) AND (R4), not a constant swap.** The quadratic entry
   ε_1²/(512NA_d) **is** (R4)'s condition 2A_dη_1 ≤ ε_1²/(256N) — the linear δ_c loss. §3.1. The rebuilt
   replacement, with proofs, is §3.2; the hypothesis-availability table is §3.3. **Good news: the kernel
   branch constant κε_1²/(256N) comes out IDENTICAL by both routes (§3.2), so no other constant in your
   file moves.**
4. **One hypothesis of Lemma KN is not stated in your file, and it is load-bearing.** KN needs M̄_c to be
   a mixture with **nonnegative weights summing to 1**; **l.992 says only "M̄_c is a mean of the T^σ_y"**.
   Please state that the S4′ weights are nonnegative and normalised. Until then the repair is
   **CONDITIONAL** on it, and that is how §6.2 labels it. §3.3 H1.
5. **l.65's "η_1 ≤ η_q" becomes FALSE under the adoption** — it reverses to η_1/η_q = **39.3846** (N = 2),
   **59.0769** (N = 3). REVIEW_RLARGE_V2 §2.3's "CORRECT" endorsement is of the current form only. §5.1.
6. **The honest ceiling convention for a_RS carries c_RS = 625.** l.1023 prices n cubes as
   (Ce^{−a_RS/g²})^{n/c_RS} and l.1024 forms a_♯ = min{a″, a_♭, **a_RS/c_RS**}, so the bare a_RS/10² of
   l.617's convention understates the breach by up to **2.80 decades**. §2.2.
7. **l.832 vs l.830: say which.** l.832 declares a_♯, c_RS and n_♯ *"superseded by §3.5 and §5.2"*, while
   l.830 still corrects Lemma RS's pricing **in a_RS** (the e^{a_RS R} factor). If v3 intends a_RS to
   enter no smallness condition at all, that needs saying — as the file reads, l.616-617's convention
   applies to it. §2.3.
8. **§5.4's table has a second defect, independent of ε_1.** l.612 reports ≈ 184 wrap levels from n_H, but
   l.1024 says *"the induction uses n_c = n_♯"*, and at the current η_1 **n_♯ = 2.27·10¹⁶⁹, level count
   355.6 — 172 levels worse than the table's figure.** Under the adoption n_♯ = 1.64·10⁸⁷ and its level
   count is **183.4**, essentially n_H's 183.6, and the table becomes self-consistent. §4.2 (ARGUED by
   analogy with your own W-convention; the convention is yours to apply).
9. **Not an ε_1 request.** I have not changed ε_1 and do not recommend that it be changed; every figure
   above is given at today's ε_1 **and** at the proposed one. **a_RS binds at today's ε_1 either way** —
   that is the point of §2.2.

### §8.2 For PLD's owner

1. **REVIEW_PLD_S3's fix (INH-1) and (F-9′) are still outstanding, and they are now consequential.**
   *"RLARGE's η_1 = c_1ε_1"* at **l.42, l.772, l.1010, l.1071, l.1077, l.1096, l.1204, l.1259** is not
   RLARGE's η_1 (RLARGE l.64, l.830). If RLARGE adopts (§8.1 item 2) your text becomes correct as it
   stands; **if it does not, every one of those eight lines needs the other threshold.** Either way the
   two files must stop disagreeing. §1, §1.1.
2. **Your LD-arith conclusion survives the adoption**, and I reproduce all three of REVIEW_PLD_S3's
   scanned values (least N = **37** at t = 2, **593** at t = ½, **507954** at t = 2/117). At t = η_1 the
   summability condition fails at N = 2 and N = 3 under **both** forms, so **l.775's "route (a)'s answer
   is no for SU(2), SU(3)" is unaffected.** §5.2.
3. **(Arch-3)'s m_τ: the adoption removes its ε_1-dependence.** At RLARGE's η_1 it is **66/90/122**
   (C_I = 1/1.5/2) at ε_1 = 6.7·10⁻⁴⁰ and **73/100/136** at the proposed value — not the 54/74/101 at
   2·10⁻³² that REVIEW_PLD_S3 l.347-348 quotes, because it grows like log(1/ε_1) and ε_1 has moved since.
   With c_1ε_1 it is **3/4/5 at every ε_1**. §4.2, §5.2.
4. **Your a(τ) = 49τ²/(256σ_*²) (l.1044, l.1048) is the a_η that a_RS actually names** at effective
   levels, and at the Gaussian σ_*² = N(1 + 18/κ) (l.341) it is **×49.6 smaller** than RLARGE's bare-level
   η_1²/(2N) — **1.70 decades**. No sign changes (margins −17.313 / +64.828 today), but if you and RLARGE
   disagree about which a_η is in force, say so. §4.3.
5. **Proposition INH is unaffected in both directions** (REVIEW_PLD_S3 l.300-302's a fortiori reading),
   and so is its obstruction. No edit needed; recorded so it is not re-opened. §5.3.

### §8.3 For the existence lane's owner (EXISTENCE.md)

1. **Lemma KN and Corollary KN-step rebuild correctly on our structures, and your two constants are
   recovered independently.** KN-step l.1775's **106** rebuilds as 8·12·(π/3)² = **105.276** (ratio
   1.00688) and l.1771's **5.5** as 4·((e^{1/4} − 1)/(1/4))·(π/3) = **4.75889 ≤ 5.5**; the identity
   (L² + 5.5A_d)c_1 = **½ exactly** makes KN-step's first part exactly t/2 on {η < c_1t}, and
   t/2 + 4·(t/8) = t makes the dichotomy **exhaustive by construction**. §3.2, `ar1c_out.txt`. Nothing in
   your statements needed repair.
2. **One hypothesis is implicit in your Lemma KN and should be explicit, because the consuming lane does
   not supply it.** KN needs **probability** weights w_i ≥ 0 with Σw_i = 1; RLARGE l.992 says only *"a
   mean of"*. Your l.1722's Lemma MIX and l.1718's (RLF-3^dis) both already turn on nonnegative weights,
   so the lane has the habit — please say it in KN too. §3.3 H1.
3. **A hypothesis with an N-dependence worth recording.** Feeding RS (R1) into KN's T_i = S e^{X_i} needs
   the **traceless** log, which exists with ‖X‖ ≤ (π/3)‖·‖ only while N·(π/3)A_dη < 2π, i.e.
   **ε_1 < 78/N** at d = 4, L = 3. Irrelevant at ε_1 ≈ 10⁻⁴⁰, but it bites for **N ≳ 39 at ε_1 ≈ 2**, and
   your l.1772 records only the weaker "A_dη ≤ 1". §3.3 H3, `ar1c` [6].
4. **Your l.1771 is worth 82 decades in the proof lane** — more than the "92" that has been quoted, at the
   ε_1 where it has been quoted. It may be worth one line in your own file saying so, since the
   beneficiary is another lane's ceiling. §4.1.

### §8.4 For HIST's owner

1. **l.186's route comparison reverses under the adoption.** *"the reduction of n_♯ comes from c_RS = 81
   against 5⁴ = 625, and the rest from **η_q² against η_1²**"* — with η_1 = c_1ε_1 the RS route's exponent
   becomes **1551× better** than the joint route's (N = 2), not worse, and **l.181's "η_q/η_1 = 2/ε_1"
   becomes the constant 117/4608 = 0.0254.** The joint route stops being the better one on this count.
   §5.1.
2. **l.151's *"PM is what makes the threshold linear (Lemma RS-lin)"* stops being the only mechanism**:
   KN-step's re-centring also makes it linear, at the RS threshold, with a better constant. Worth one
   line, since your own file already names the mechanism (*"the kernel exponent … forces η_1 ∝ ε_1²"*) —
   and KN is exactly what removes that forcing. §3.1.
3. **l.1377-1379's chain-energy floor E_𝒞(p) ≥ η_1²/(2NC_cone) gains 82.141 decades** under the adoption,
   at no cost, since it carries η_1². Recorded in case it is load-bearing anywhere. §4.2.

### §8.5 For SF's owner

1. **Your §16.3 table already carries this exponent and should be pointed at.** **l.2203-2204**:
   *"HIST n_♯, RS route (η_1 quadratic) | ε_1^{−4}"* and *"RLARGE η_1 = min{ε_1/18, ε_1²/(4608N)} | ε_1² |
   … a_RS ∝ η_1² ≈ 6·10⁻⁴¹⁶"*. **That is the ε_1⁴ finding, written before this proposal existed, for a
   different question.** It is the strongest independent record in the lane and neither RLARGE l.617-618
   nor TAUFLAT consulted it.
2. **DX′ is the quantity every margin here is measured against**, at 2.456·10⁻¹⁵²/C_Ω (REVIEW_SF_S7
   l.203). Every figure in this file is **linear in C_Ω** and conditional on DX′ remaining the binding
   programme ceiling. No request beyond noting it.

### §8.6 For the lead (HANDOFF.md, SESSION24_RESULTS.md, PROOF.md)

1. **EPS1_SWEEP's e1-4 is CONFIRMED independently.** a_RS binds today at **all four** live ε_1 and under
   both ceiling conventions; **RLARGE l.618 has a false sentence today, with no change to anything.**
   §2.2.
2. **Three corrections to the ledger, two of them unfavourable.** (i) The honest margin is **−15.62 to
   −18.41** decades, not −15.62, because a_RS is priced per cube as a_RS/c_RS with c_RS = 625. (ii) The
   gain at **today's** ε_1 is **82.141 decades, not 92**; 91.85 is the gain at the **proposed** ε_1.
   PROOF.md l.63-66 and the ledger both carry "92" attached to today's constants. (iii) The adoption was
   **not** simply "requested and not carried out": **RLARGE v3 chose the other horn of E9 at l.830.**
   §2.2, §4.1, §1.1.
3. **The repair is ADOPTABLE and CONDITIONAL on one word**: that RLARGE l.992's S4′ weights are
   nonnegative and normalised (Lemma KN's convexity hypothesis). Please route that to RLARGE rather than
   let the repair be banked as unconditional. §6.2.
4. **η_1 is three symbols, and the dangerous pair is inside this lane**: RLARGE's quadratic (R3) threshold
   and PLD's c_1ε_1, which PLD calls "RLARGE's η_1" in eight places. **Unlike the ε_1 and ε_* splits,
   these two are two different values of the SAME quantity in the SAME lemma.** REVIEW_PLD_S3 l.463 said
   so and it has not been fixed in two review cycles. §1.
5. **Nothing breaks, and one recorded fact dies**: RLARGE l.65's η_1 ≤ η_q, endorsed "CORRECT" by
   REVIEW_RLARGE_V2 §2.3, reverses. HIST l.186's route comparison reverses with it, in the favourable
   direction. §5.1.
6. **The repair does not improve a_RS's STATUS.** a_RS is CONDITIONAL on (PLD)_k (i) before and after, and
   REVIEW_PLD_S3 l.309 shows that *"choosing η_1 relative to τ_bg cannot restore in-step derivation"* at
   **any** RS-compatible threshold. If the ledger records a_RS as repaired, it should record it as
   **82 decades larger and still conditional**. §3.4.
7. **The pattern HANDOFF's closing paragraph names holds again, twice.** The quartic came from a threshold
   fixed once (l.64's min, v2-E9) and never revisited against its own consumer; and the 92-vs-82 slip came
   from a difference quoted at the wrong one of two ε_1 values. **Before attacking an estimate, check what
   someone fixed once and nobody revisited** — and check which ε_1 a decade-figure was evaluated at.

*(End of ARS_FIX.md. Files written by this worker: this file, `checks/ar1_criteria.md`,
`checks/ar1_margins.py`, `checks/ar1_out.txt`, `checks/ar1_err.txt`, `checks/ar1b_power.py`,
`checks/ar1b_out.txt`, `checks/ar1b_err.txt`, `checks/ar1c_knrebuild_posthoc.py`, `checks/ar1c_out.txt`,
`checks/ar1c_err.txt`. Nothing else, anywhere. No git command was run by me.)*
