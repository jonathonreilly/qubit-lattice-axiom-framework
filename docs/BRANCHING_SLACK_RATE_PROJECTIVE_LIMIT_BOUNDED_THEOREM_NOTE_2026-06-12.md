# The Branching Slack Increases on the ε = 0.3/0.6/0.9 Grid and Its Per-Step Rate Trends to the Projective Endpoint (max |rate−1|: 0.81 → 0.48 → 0.014 → 0.0036 → 0.00015 Across ε = 0.3…0.99, With the ε = 1 Endpoint Exact): Near-Projective Branching Consumes the Budget Recordlessly (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_branching_slack_rate_eps_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_branching_slack_rate_eps_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=7 FAIL=0` — exact
trees (`NFRAG ∈ {3,4,5}`, up to 32 branches), no MC.

## Findings

- **The hard bounds hold everywhere**: `R_b ≤ NFRAG − B_b` at every
  `(NFRAG, ε, branch)` and at record thresholds `0.3/0.5/0.7`; the weighted
  marginal-sum entropy obeys the budget bound at every instance.
- **Slack is strictly ε-increasing on the `0.3/0.6/0.9` grid** at every `NFRAG`
  (weighted mean slack, e.g. `NFRAG = 3`: `0.95 → 1.56 → 3.00`). On the
  fuller near-endpoint grid, some rows saturate after `ε = 0.9`; that plateau
  is rate data, not a strict-monotonicity claim.
- **The sampled-grid trend to the projective endpoint**: the per-step slack rate's
  worst deviation from `1` falls as `0.81 → 0.48 → 0.014 → 0.0036 → 0.00015` across
  `ε = 0.3/0.6/0.9/0.95/0.99` (per-`NFRAG` values printed; the `ε = 0.9` worst case
  is `NFRAG = 4` at `1.35%` — stated exactly), with the `ε = 1` endpoint exact
  (pointer-eigenstate control). Small `ε` shows large threshold/parity spread
  (disclosed; finite-depth pattern — no `NFRAG → ∞` claim). The deviation bounds in
  the gate are measured ceilings, regression-style; the claim is the printed
  progression.
- **Controls**: `ε = 0` gives exactly zero slack (the linear ledger) at every
  `NFRAG`; `ε = 1` branches are pointer eigenstates with zero
  connected-correlator records; the `|0⟩`-pointer registers nothing.

## Scope

The broadcast + weak-measurement model, exact, finite depth (= `NFRAG`); the slack
table and its ε/NFRAG patterns are the data (`ε`-grid model/state data, labeled).
Not claimed: thermodynamic specialness; measures over states; other dynamics;
asymptotics in depth or size. The branching-ledger and Born-cap references are
context only, not graded authorities for this claim.

No new axiom, primitive, measure, or weight; `r` untouched. The audit lane grades.
