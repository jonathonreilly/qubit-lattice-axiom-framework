# Under Born-Weighted Branching the Record-Budget Ledger Becomes an Inequality: Branches Can Consume Blanks Without Registering, and the Branch-Averaged Budget Bound Survives (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (the branching extension of the landed record-budget ledger)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_branching_record_budget_inequality_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_branching_record_budget_inequality_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=14 FAIL=0` — exact
16-dim tree enumeration, deterministic, no MC, memory trivial.

## The question

The record-budget ledger note
([`THERMODYNAMIC_PH_QUANTITATIVE_CLAUSE_RECORD_BUDGET_LEDGER_BOUNDED_THEOREM_NOTE_2026-06-11.md`](THERMODYNAMIC_PH_QUANTITATIVE_CLAUSE_RECORD_BUDGET_LEDGER_BOUNDED_THEOREM_NOTE_2026-06-11.md);
linear, no branching; context link, with the `epsilon = 0` control
independently reproduced in this runner) found exact 1:1 accounting:
each clean record consumes one aligned blank. Does that survive **Born-weighted
branching** — the unraveling situation, where a weak measurement splits the history
into branches?

## The findings (runner `PASS=14`; 1 pointer + 3 fragments, broadcast + two-outcome
weak Kraus per step, 8 branches at depth 3)

**(B1) The exact equality breaks — by measurement, not error.** At the record
threshold `|C| > 0.5` (a **declared choice**; the strict-branch count is
threshold-relative and probed at `0.3/0.5/0.7` in-runner), 2 of 8 branches have
`R_b < 3 − B_b`: a branch can **consume a blank without a threshold-clearing record**
(the weak measurement lowers that branch's pointer–fragment connected correlator
below threshold while the register is no longer blank — a record-functional
statement, not a decoherence claim). The exceptions are printed verbatim; the
observed relation on *every* branch, at **every probed threshold**, is

> `R_b ≤ 3 − B_b` — **records ≤ blanks consumed, per branch** — the ledger is an
> inequality under branching.

**(B2) The branch-averaged budget bound survives.** `Σ_b w_b S_b = 1.22 ≤ 3` (the
initial blank budget bounds the Born-weighted marginal-sum entropy), and every branch
individually respects the register deficit bound `R_b ≤ 3`. All quoted numbers (`1.44`, `1.22`, the strict-branch counts) are **`ε = 0.6` realized
model/state data**, labeled as such. The thresholded count exceeding the entropy sum
off the deterministic point is consistent with the full-alignment-coincidence
disclosure in the linked record-budget note, with the deterministic control
reproduced in-runner.

**(B3) Controls.** `ε = 0` (no branching) recovers the landed linear ledger exactly
(`R = 3`, `S = 3`, `B = 0`); `ε = 1` (projective) gives pointer-eigenstate branches with zero
connected-correlator records (`R_b = 0` — the record-functional statement;
formation is realized-state data); the `|0⟩`-pointer initial condition registers nothing on any branch; weights
sum to one (`1e−12`) with the no-prune guard clean.

## Scope

The broadcast + two-outcome weak-measurement model, 4 qubits, depth 3, exact; the
branch-resolved inequality and the surviving budget bound are the data. **Not
claimed:** thermodynamic specialness (the separately registered input); any measure
over states; Born derivation (the derived-chain cap is inherited); general dynamics
or other models. The named next path: the depth/size scaling of the branching slack
`(3 − B_b) − R_b`. Standard math (method only): Kraus trees; partial traces;
connected correlators.

No new axiom, primitive, measure over states, external fitted weight, or
weighting rule is introduced; branch weights are only the supplied
Kraus/Born weights of this finite model. `r` untouched; discrete
throughout. The audit lane grades.
