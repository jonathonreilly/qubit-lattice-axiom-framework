# CLAIM STATUS CERTIFICATE — Block 08 (yt vertex-power operator-counting lemma)

**Date:** 2026-05-17
**Block:** 08
**Branch:** `physics-loop/yt-vertex-power-derivation-block08-2026-05-17`
**Campaign:** `filter-excluded-positive-closures-2026-05-17`
**Primary artifact:** `docs/YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md`
**Primary runner:** `scripts/frontier_yt_vertex_power_operator_counting_lemma.py`
**Cache:** `logs/runner-cache/frontier_yt_vertex_power_operator_counting_lemma.txt`

## Status fields

```yaml
actual_current_surface_status: conditional-bounded operator-counting lemma (positive closure of S1/S2/S3)
target_claim_type: bounded_theorem
conditional_surface_status: conditional on three named admissions (see below)
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: |
  The lemma states that the staggered Dirac operator's vacuum-polarization
  functional carries exactly two single-link vertex insertions (n_link = 2),
  conditional on (i) the staggered-Dirac realization gate, (ii) the
  link-exponential gauge convention, and (iii) the bare-coupling-map
  identity alpha_eff = alpha_bare / u_0^{n_link}. Items (i)-(iii) are
  named, not closed. Within those admissions the count is exact integer
  arithmetic on the operator structure, machine-precision verified by
  the paired runner (8/8 PASS, slopes 2.0000 and 1.0000 to ≤3.4e-16).
audit_required_before_effective_retained: true
bare_retained_allowed: false
proposal_allowed: true
proposal_allowed_reason: |
  Tier: narrow operator-counting lemma. Closes the gap explicitly
  disclaimed by the retained companion ALPHA_S_TADPOLE_IMPROVEMENT_
  VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10 (which says "k=2 enters
  as the algebraic exponent in definition (2)"; not a derivation).
  Honest tier: conditional-bounded structural support theorem with
  three explicitly named admissions.
```

## 7-criterion retained-proposal certificate

| # | Criterion | Pass? | Notes |
|---|---|---|---|
| 1 | `proposal_allowed: true` | YES | Conditional-bounded structural lemma; cleanly scoped |
| 2 | No open imports | PARTIAL | Three admissions explicitly named (staggered-Dirac gate, link convention, bare-coupling-map identity); not silent imports |
| 3 | No load-bearing observed/fitted/admitted unit conventions | YES | No PDG / observational targets; no fitted exponents; counting is integer |
| 4 | Every dep retained | PARTIAL | A1, A2 retained; staggered-Dirac realization is the open gate named in MINIMAL_AXIOMS_2026-05-03; companion algebraic theorem is `retained`; parent vertex-power note is `unaudited` |
| 5 | Runner checks dep classes | YES | Paired runner verifies S1 (single-link, dev=0), S2 (degree-2, slope=2.0000), S3 (relative count 2/1), tadpole companion (slope=1.0000), and bubble non-triviality. 8/8 PASS |
| 6 | Review-loop disposition | PASS (self-review) | See REVIEW_HISTORY.md §1 |
| 7 | PR body says independent audit required | YES | Note includes "Status authority: independent audit lane only" |

**Result:** Honest tier: **conditional-bounded operator-counting structural lemma**.

## Promotion Value Gate (V1-V5)

Recorded in `REVIEW_HISTORY.md` §1. Disposition: **PASS**.

## Cluster-cap / volume-cap

- Volume cap (this campaign): 1 of N used (single PR by this block).
- Cluster cap (`yt_vertex_power_*`): 1 of cap used.
- Corollary churn: closes the gap explicitly disclaimed by the retained
  companion `alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10`;
  this is the missing operator-level bridge, not a relabeling.

## Imports retired

None directly. The lemma reduces the *informal* "vertex insertion has one
gauge link" claim in the parent `YT_VERTEX_POWER_DERIVATION.md` to an
explicit operator-level statement with a machine-precision check.

## Imports newly exposed

| Item | Class | Notes |
|---|---|---|
| Staggered-Dirac realization gate | open gate (already exposed in MINIMAL_AXIOMS_2026-05-03) | Explicit admission |
| Link-exponential convention `U = exp(i A)` | gauge convention (named) | Standard lattice convention |
| Bare-coupling-map identity `alpha_eff = alpha_bare / u_0^{n_link}` | parent-note assertion | Consumed from YT_VERTEX_POWER_DERIVATION.md |

## Honest classification

**Conditional-bounded operator-counting structural lemma:**
- Establishes S1: `D' = dD/dA` is degree-1 in `U` (single-link vertex) — machine-precision verified across `lambda ∈ {0.5, 0.7, 1.0, 1.3, 2.0}` (max deviation 0.00e+00).
- Establishes S2: `Pi = -Tr[D^{-1} D' D^{-1} D']` is degree-2 in `D'` (slope = 2.000000 in log-log, indistinguishable from 2; explicitly excludes 1 and 4).
- Establishes S3: `n_link(VP) = 2 = 2 × n_link(hopping)` (relative count verified at 2.000000 to 2.22e-15).
- Companion: `Tr[D^{-1} D'']` is degree-1 in `D''` (slope = 1.000000), confirming the tadpole-vs-bubble structural distinction.

This is **NOT** a derivation of the staggered-Dirac realization itself, and **NOT** a closure of the renormalized `y_t` lane, the `v`-endpoint selection, or the running bridge to `M_Z`. It is the operator-level structural input that the retained companion algebraic theorem explicitly disclaims.

## Repo-weaving recommendation (for later integration, NOT executed in this PR)

For the later review/integration process:

- Cross-reference this lemma in `YT_VERTEX_POWER_DERIVATION.md` §Core Derivation step (2)-(3) as the operator-level support for "each vertex insertion contributes one gauge-link dressing".
- After audit ratification: this lemma would let the companion narrow algebraic theorem `ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10` drop the disclaimer "k=2 enters as the algebraic exponent" and instead cite this lemma for the structural support.
- Audit lane retains all decisions on effective status.

## Stop conditions checked

- Runtime exhaustion: no (~60 min wall used)
- Volume cap: no
- Cluster cap: no
- Corollary exhaustion: no (this is the missing operator bridge, not a relabel)
- Value-gate exhaustion: V1-V5 PASS
- Tooling: no (runner runs in 0.1s; cache built via `cached_runner_output.py`)

## Next action

Commit + push + open PR `[physics-loop] yt-vertex-power-derivation-block08: conditional-bounded operator-counting lemma`. Audit lane decides retained tier.
