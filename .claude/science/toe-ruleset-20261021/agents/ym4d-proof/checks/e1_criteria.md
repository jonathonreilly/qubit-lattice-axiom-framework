# checks/e1_criteria.md — pre-registered criteria for the ε_1 consumer sweep

Written BEFORE any script in this check family. **This file contains no numeric constant at all**, and in
particular no constant derived in session 24: every quantity is named symbolically and every verdict is a
comparison rule. Constants will be transcribed into the script from their owning files with file+line
citations, and the script will not re-derive them.

## Symbols used below (all defined in owning files, none evaluated here)

- **E_t** — the ε_1 value currently recorded as the lane ceiling in RLARGE.md §0 ("Current ε_1 ceiling").
- **E_p** — the value TAUFLAT.md §4 option C proposes. Referred to only as "the proposed value".
- **E_c1, E_c2** — two counterfactual ε_1 values chosen by the script for the power check (§e1-5).
- **G_DX** — the DX′ programme coupling ceiling on g_0², REVIEW_SF_S7 / RLARGE §5.4, carried with its
  symbolic C_Ω.
- **G_CRC(ε)** — HW's (S2) ceiling g²_CRC at the ring value PLD session 7 settled for the closed column.
- **a_bad(ε), a(ε), a_RS(ε), a_ret(ε), n_*(ε), n_H(ε), W(ε)** — as defined in RLARGE §0, §5.4, §6 and
  PLD §16.8, evaluated at threshold ε.
- **η_♭, t_pr, C_3** — as in SQ.md Corollary DESC-ε and its consumers.

## Checks, with their pre-registered verdicts

### e1-1 SCALING CENSUS — exponent classification
For every consumer enumerated in EPS1_SWEEP.md §2, the script computes the quantity at E_t and at E_p and
reports the exact ratio. For each consumer I will have recorded, before running, the exponent n with which
I claim it scales (value ∝ ε^n, or "log", or "invariant").
- **PASS (CLASSIFICATION-HOLDS)** if every computed ratio equals (E_p/E_t)^n for the claimed n, exactly,
  for every consumer with a claimed power law, and the "log" and "invariant" entries behave accordingly.
- **FAIL (CLASSIFICATION-WRONG)** on any mismatch. A mismatch is a defect in my enumeration, not in the
  source, and is reported as my error.

### e1-2 FLOOR — the window g ≪ ‖·‖ < ε_1 must stay open
The existence lane requires the small-field threshold to contain the typical field (EXISTENCE §20.2's
"ε only has to contain the typical field ≍ g"; §19's coercivity clause is stated "at distance ≫ g but
< ε_1"). The script forms the window ratio ε/g at the coupling that actually binds the programme.
- **PASS (FLOOR-RESPECTED)** if the window ratio at E_p is > 1, and the script reports its decades.
- **FAIL (FLOOR-VIOLATED)** if it is ≤ 1 at E_p.
- The script reports the ratio at **both** the ε-independent binding ceiling and the ε-driven ceiling,
  because which one is in force changes the answer, and I pre-register that both must be shown.

### e1-3 DECLARED PRICE — reproduction of TAUFLAT §4 C's five figures
a_bad, a, n_H, wrap levels and g_K², each recomputed from the owning files' formulas at E_p.
- **SOURCE-REPRODUCED** if each agrees with TAUFLAT's declared figure within a factor 1.2.
- **SOURCE-DISAGREES** on any figure outside that factor; the disagreement is reported with its direction
  and the exact figures, and the script and output are kept unaltered.
- Pre-registered as a separate line: whether TAUFLAT's declared price list is **complete**, i.e. whether
  every ε-driven quantity the sweep finds scales with an exponent no steeper than the steepest one the
  declared list exhibits. **PRICE-COMPLETE / PRICE-INCOMPLETE.**

### e1-4 DOES THE PRICE BIND — each ceiling against the programme ceiling
For every coupling ceiling the sweep finds, the script asks whether at E_p it falls **below** G_DX, i.e.
whether it becomes the binding constraint.
- **NOT-BINDING** for a ceiling that stays above G_DX at E_p; the script reports the remaining margin in
  decades and the value of (c_+ · C_Ω) at which the margin is exhausted.
- **BINDS** for any ceiling that falls below G_DX at E_p. **A ceiling that already sits below G_DX at E_t
  is reported as BINDS-ALREADY**, with both margins, so that what option C causes is separated from what
  it inherits. Any BINDS or BINDS-ALREADY result is a FAIL of this check and is reported as a FAIL.

### e1-5 POWER (anti-tautology; mandatory)
Pre-registered before running, per the brief and EPS1_SWEEP §0.6. The script re-runs e1-2 and the
DESC-ε (iii) clause test at two counterfactual thresholds, chosen inside the script:
- **E_c1 := an ε_1 below the ε-independent programme coupling ceiling** (so the small-field window closes).
  Required outcome: **e1-2 flips to FLOOR-VIOLATED.**
- **E_c2 := the lane's current ceiling E_t itself.** Required outcome: **the DESC-ε (iii) clause test flips
  to CLAUSE-FAILS**, while e1-2 stays FLOOR-RESPECTED.
- **PASS (HAS-POWER)** only if BOTH flips occur. If either verdict is the same at the counterfactual as at
  E_p, the corresponding check **has no power** and will be reported as having none, not as a PASS.
- The independent constructions each check is tested against are named in EPS1_SWEEP §3.4: e1-2 against
  the existence lane's own window statement (a different file from the one proposing the change); e1-3 and
  e1-4 against HW's own §35.7 constants table and SF's own ε_1-scaling tables, neither written for this
  question.

### e1-6 PRECISION
Every verdict is decided on exact `fractions.Fraction`; `Decimal` is used only for display, at two
precisions.
- **PASS** if every verdict is identical at both display precisions.
- **FAIL** otherwise.

## What these checks cannot do, stated in advance
They are arithmetic-consistency checks between transcriptions. They cannot validate RLARGE's ε_1 ceiling,
HW's b_n, SF's DX′ evaluation, PLD's ring price or SQ's η_♭ derivation; a number reproduced here is **not**
an endorsement of its source. They also cannot find a consumer that uses ε_1 without naming it, and the
enumeration is therefore COMPUTED only over the files listed in EPS1_SWEEP §2.0.
