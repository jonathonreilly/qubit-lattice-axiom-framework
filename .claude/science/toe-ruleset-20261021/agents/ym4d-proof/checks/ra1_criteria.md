# ra1_criteria — pre-registered criteria for the ARS_FIX / EPS1_SWEEP arithmetic re-derivation

**Written BEFORE `ra1_margins.py` exists.** Every constant named below is **transcribed from a file
written in an earlier session** (ARS_FIX.md, EPS1_SWEEP.md, RLARGE.md, HIST.md, REVIEW_SF_S7) and is the
claim **under test**; no constant here is derived by me. Method: exact `fractions.Fraction` plus
`decimal.Decimal` at 60 digits for log10 display only, plain `python3 -I`, no numpy/BLAS, no numeric lock
(brief rule 6).

Reviewer's tolerance, fixed here: **0.01 decade** on any decades figure, **1 part in 10³** on any pure
ratio. Outside tolerance ⇒ **SOURCE-DISAGREES**, with the corrected value and its direction
(favourable / unfavourable to the claim under test) stated.

## The structural inputs (transcribed, with file:line)

- `A_d(L) := (d-1)L(L-1)/2`, `= 9` at `d = 4, L = 3` — **RLARGE.md l.973**.
- `η_1^quad := min{ε_1/(2L²), ε_1²/(512 N A_d)}` — **RLARGE.md l.64**, **l.976** (R3), `= min{ε_1/18,
  ε_1²/(4608N)}` at d=4,L=3 — **RLARGE.md l.1009**.
- `η_q := min{ε_1/(2L²), ε_1/(256 N A_d), δ_0/A_d}` — **RLARGE.md l.64**, **HIST.md l.170**.
- `a_η := η_1²/(2N)` — **RLARGE.md l.1026**, **l.981** (R5).
- `a_RS := min{a_η, κ ε_1²/(256N)}` — **RLARGE.md l.1020**.
- `c_RS := 5⁴ = 625` (RS route) — **RLARGE.md l.1021**; `c_RS = 81` (RS-joint / joint route) —
  **RLARGE.md l.435**, **HIST.md l.185**.
- `a_♯ := min{a'', a_♭, a_RS/c_RS}`, `a'' = 0.9ε_1²/(4N)` — **RLARGE.md l.1024**, **l.1245**.
- `c_1 := 1/(2(L² + 5.5 A_d(L)))` — **EXISTENCE.md l.1771**, quoted at **ARS_FIX.md l.365**.
- Ceiling convention `g² ≲ a/10²` — **RLARGE.md l.616-617**.
- `DX′ = 2.456·10⁻¹⁵²/C_Ω` — REVIEW_SF_S7 l.203, quoted at **ARS_FIX.md l.275**.
- ε_1 values in force: `1.27e-39` (SF l.2837), `9.52e-40` (RLARGE l.71), `8.95e-40` (RLARGE l.611),
  `6.7e-40` (RLARGE l.72, headline); proposed `9.38495112638e-45` (EPS1_SWEEP l.455).
- `N ∈ {2, 3}`, `κ = 1` **as ARS_FIX evaluates it** (the value is not cited in either file; see RA1-7).

## Pre-registered checks, each with BOTH verdicts

**RA1-1 — the four headline decade figures.** Recompute, from the chain above and nothing else, the
margin of `a_RS/10²` against DX′ at C_Ω = 1, and the gain of the linear form over the quadratic one.
- **REPRODUCES** iff all four of ARS_FIX's figures **−15.617**, **−18.413** (ARS_FIX l.272),
  **+82.141**, **+91.848** (ARS_FIX l.455) land within 0.01 decade.
- **SOURCE-DISAGREES** otherwise, with my value.

**RA1-2 — the c_RS reconciliation of the −15.62/−18.41 pair.** ARS_FIX l.288-289 asserts the honest
margin is **"between −15.62 and −18.41"** *because* a_RS is priced per cube as `a_RS/c_RS`, `c_RS = 625`.
- **RECONCILES** iff `(−15.617) − log10(625) = −18.413` to within 0.001 decade.
- **DOES-NOT-RECONCILE** otherwise: then the stated mechanism does not produce the stated interval and at
  least one endpoint is wrong.
- *Designed-FAIL control (RA1-2c):* the same reconciliation with `c_RS = 81` **must** return
  DOES-NOT-RECONCILE. If it returns RECONCILES the check has no power.

**RA1-3 — the gain is quoted at ONE of four live ε_1.** Compute the gain at each of the four live values.
- **GAIN-DETERMINATE** iff the four gains agree within 0.01 decade (so "the gain at today's ε_1" is a
  well-defined number).
- **GAIN-INDETERMINATE** otherwise, with the spread reported: then the headline figure is a figure at one
  chosen value and must be quoted with that value attached.

**RA1-4 — `c_1 = 1/117` and the identity `(L² + 5.5A_d)c_1 = ½`.**
- **DERIVES** iff `1/(2(L²+5.5A_d))` is exactly `1/117` at d=4,L=3 **and** `117 = 2(9 + 49.5)`.
- **FAILS** otherwise.
- *Power note, pre-registered:* the identity `(L²+5.5A_d)c_1 = ½` is **true by the definition of c_1** and
  therefore **cannot fail**. I record it as a **NO-POWER** line, not as evidence, and test instead whether
  the `5.5` used in `c_1` is the same `5.5` the dichotomy's first part uses (if one were the sharper
  `4.75889` and the other `5.5`, the identity would break). That comparison **can** fail.

**RA1-5 — `117/4608`, `39.3846`, `59.0769`, and whether the two `4608`s are the same 4608.**
- **EXACT** iff `4608/117 = 39.3846…`, `6912/117 = 59.0769…` and `117/4608 = 0.025390625` exactly, **and**
  `256·N·A_d|_{N=2} = 4608` while `512·A_d = 4608` — i.e. the two occurrences of the integer 4608 in this
  lane have **different** factorisations that coincide only at N = 2.
- **COLLISION-FREE** iff they are the same quantity. (Pre-registered as the more likely wrong answer.)

**RA1-6 — the route reversal that ARS_FIX l.537 prices at `1551×`.** HIST.md l.185-186 states the
compared quantity as *"the binding exponent of the joint route is the plaquette branch **a_η/81**"*
against the RS route's `a_RS/c_RS` with `c_RS = 625`. Compute the per-cube ratio
`[a_η(η_1^lin)/625] / [a_η(η_q)/81]` at N = 2.
- **AGREES-1551** iff that ratio is 1551 ± 1.
- **SOURCE-DISAGREES** otherwise, with the corrected ratio. *Pre-registered consequence if it disagrees:*
  ARS_FIX applies `c_RS = 625` where it worsens the margin (its own §2.2 Correction 1) and omits the
  `625 vs 81` asymmetry where it would shrink the route gain — a currency inconsistency, which is a
  finding and not a rounding.

**RA1-7 — what the headline rests on that neither file evaluates.** Both files state every margin is
linear in `C_Ω` (ARS_FIX l.275, l.706) and EPS1_SWEEP (C7) (l.494-496) makes the verdict conditional on
`c_+·C_Ω ≲ 1.5·10⁴⁶`. Compute (i) the value of `C_Ω` at which each a_RS margin crosses zero, and (ii)
whether that value lies inside (C7)'s own admissible window.
- **INSIDE-WINDOW** (the dangerous answer): the crossover is **below** 1.5e46, so (C7) admits a range of
  `C_Ω` over which (C2)'s premise — *a_RS binds* — is **false**.
- **OUTSIDE-WINDOW**: the crossover exceeds (C7)'s allowance and the premise holds throughout it.
- Also recompute (C7)'s own four exhaustion figures `8.31e53`, `1.54e46`, `4.24e63`, `7.87e55`
  (EPS1_SWEEP l.443-444) and report whether they are figures for `c_+·C_Ω`, for `c_+/C_Ω`, or for
  `1/C_Ω`. **OPERATOR-AS-WRITTEN** / **OPERATOR-DISAGREES**.
- Separately: report the κ at which `a_RS`'s min changes branch under the linear form, and the gain as a
  function of κ below it (pre-registered failure mode (G4) of ARS_FIX §0.4, which ARS_FIX tested only
  against ε_1 and not against κ). **KAPPA-IMMATERIAL** iff the gain loses less than 1 decade for every
  κ ≥ 1e-4; **KAPPA-MATERIAL** otherwise.

**RA1-8 — the net value of the adoption over the lane's own already-PROVEN alternative.** HIST Lemma
RS-lin is listed **PROVEN-HERE** at **RLARGE.md l.628** and delivers a **linear** threshold `η_q`
(HIST l.151, l.168-186). Compute, at today's ε_1 and N = 2: (i) the joint route's per-cube exponent
`a_η(η_q)/81` and its margin against DX′; (ii) the ratio of the post-adoption RS per-cube exponent to it.
- **ADOPTION-NET-SMALL** iff the joint route's margin is already positive and the adoption's net gain
  over it is under 10 decades. *Pre-registered consequence:* then "82.141 decades" is the gain of the
  adoption **over RLARGE's own RS route only**, not over the lane's best proven route, and the headline
  must say which.
- **ADOPTION-NET-LARGE** iff the joint route also binds or the net gain exceeds 10 decades.

**RA1-9 — H5's numerical value.** ARS_FIX l.408 gives `t ≤ 1/(106√N A_d²c_1²)` as **1.12737** (N = 2) and
**0.920492** (N = 3).
- **REPRODUCES** iff both land within 1 part in 10³.
- **SOURCE-DISAGREES** otherwise (immaterial to any verdict at ε_1 ≈ 10⁻⁴⁰; recorded for the record only,
  since both files claim exact rational arithmetic verified at 50 and 100 digits).

## Designed-FAIL controls (brief defect 3: a gate with no control is not evidence)

Run with the criteria above **unchanged**, on inputs I know should fail:
- **(F-a)** `η_1 := ε_1` (i.e. `c_1 = 1`). RA1-1's margin verdict **must** read NOT-BINDING and the gain
  **must** exceed 82.141. If it still reads BINDS, the margin gate has no power.
- **(F-b)** `η_1 := ε_1³/(512NA_d)` (a cubic threshold, `a_RS ∝ ε_1⁶`). RA1-1 **must** read BINDS with a
  margin far worse than −15.617. If the verdict does not move, the gate is insensitive to the exponent.
- **(F-c)** RA1-2 with `c_RS = 81` — **must** return DOES-NOT-RECONCILE (see RA1-2c).
- **(F-d)** RA1-6 with the `625/81` asymmetry **removed** (both routes at 625) — must return
  AGREES-1551, demonstrating that the disagreement in RA1-6, if any, is *caused by* the asymmetry and is
  not a bookkeeping slip of mine.

A control that does not fail is reported as **NO POWER** for the gate it controls, and that gate's result
is then reported as not-evidence rather than as a verdict.

## What this check cannot decide, stated now

It cannot validate `DX′`, `C_Ω`, `c_+`, `κ`, `δ_0`, `a_♭`, `β_-`, HW's constants or PLD's `σ_*`. It
cannot settle whether RLARGE v3 consumes `a_RS` at all — that is a **reading** question about
RLARGE §3.5 / l.832 / l.835, decided in the review text, not here. It cannot check Lemma KN′'s proof,
which is checked by hand in the review text line by line.
