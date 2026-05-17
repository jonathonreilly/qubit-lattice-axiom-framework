# CLAIM STATUS CERTIFICATE — Block 25 (axiom-first reflection positivity)

**Date:** 2026-05-17
**Campaign:** filter-excluded-positive-closures-2026-05-17
**Block:** 25 — axiom-first reflection positivity (target row
  `axiom_first_reflection_positivity_theorem_note_2026-04-29`, 31 direct
  in-degree, 822 transitive descendants, currently `unaudited` post-
  2026-05-17 narrowing)
**Branch:** `physics-loop/axiom-first-reflection-positivity-block25-2026-05-17`
**Slug:** `axiom-first-reflection-positivity-block25-2026-05-17`
**Primary artifact:** `docs/STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`
**Primary runner:** `scripts/staggered_only_det_positivity_case_a_2026-05-17.py`
**Runner cache:** `logs/runner-cache/staggered_only_det_positivity_case_a_2026-05-17.txt`

## Status

```yaml
actual_current_surface_status: standalone closed-form sub-theorem (Case A)
target_claim_type: positive_theorem (narrow)
proposal_allowed: false
proposal_allowed_reason: |
  Strictly additive sub-theorem note supplying a cleaner self-contained
  derivation of the parent reflection-positivity note's Case A
  determinant input. Parent note text is NOT modified; no parent note
  dependency is added or removed. Source-only PR. Independent audit lane
  required before any retained-grade elevation.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## V1-V5 Promotion Value Gate (fresh lane)

- **V1 (Reframing):** The parent note's §"Step 3a — historical
  staggered-only derivation" (post-2026-05-17 narrowing) gets the
  correct answer `det(M_KS + mI) ≥ 0` but in an abbreviated form (parent
  eqs (14a)-(14b)) that does not write out the `det(γ_5)` sign
  reconciliation — the same sign that the bridge note carefully tracks
  (bridge eqs (15)-(17)) for the joint Wilson sector. PASS — the new
  note specialises that careful treatment to the `M_W = 0` regime where
  it becomes unconditional and strictly positive.
- **V2 (Novelty):** No existing note proves `det(M_KS + mI) > 0`
  standalone with full `det(ε)` sign reconciliation. Parent's eq (14b)
  skips signs; bridge note handles joint `M_KS + M_W` only under
  symmetric-canonical hypothesis (D4). New content. PASS.
- **V3 (Could-audit-compile?):** Non-trivial sub-theorem with explicit
  sign reconciliation written out as a self-contained closed-form;
  not currently captured anywhere standalone. PASS.
- **V4 (Non-trivial):** Yes — adds a load-bearing closed-form chain for
  the parent's Case A path that is independent of the (currently
  `audited_conditional`) bridge note. Strengthens the parent's only
  currently-unconditional sub-case. PASS.
- **V5 (Distinct from prior cycles):** Yes — distinct sub-theorem,
  narrower scope (Wilson term excluded), strictly-positive lower bound
  `m^n` derived as Corollary C2. PASS.

**Disposition: PASS** for narrow sub-theorem note purposes.

## 7-criterion certificate

| # | Criterion | Pass |
|---|---|---|
| 1 | proposal_allowed | NO (sub-theorem note, strictly additive) |
| 2 | No open imports | YES (standalone closed-form using only A_min, the {ε,M_KS}=0 parent E5 verified identity, SVD, and 2×2 block-determinant arithmetic) |
| 3 | No load-bearing observed/fitted | YES (no numerical, observed, or fitted inputs) |
| 4 | Every dep retained | N/A (no new dependency added; sub-theorem stands on its own staggered-only inputs, independent of bridge note's conditional status) |
| 5 | Runner checks dep classes | YES (V1-V4 verify each load-bearing identity numerically; 60/60 SU(3) configurations pass V4 to machine precision) |
| 6 | Review-loop pass | self-review PASS (closed-form derivation written out in full; runner output cached and re-run-identical) |
| 7 | PR body says independent audit required | YES |

**Honest tier:** branch-local closed-form sub-theorem on the explicit
framework baseline, supplying a self-contained derivation of the parent
note's Case A determinant input with explicit `det(ε)` sign
reconciliation. Strictly additive on the parent note.

## Imports

None retired. None added. The new sub-theorem note has zero new
dependencies and is independent of the (currently `audited_conditional`)
bridge note `STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md`.

## Honest classification

**Narrow standalone closed-form sub-theorem note** for the staggered-only
sector. Cleans up the parent note's Case A path by writing out the
explicit factorisation
`det(M_KS + m·I) = ∏_{i=1}^{n/2} (m² + σ_i²) > 0`
together with the `det(γ_5) = (-1)^{n/2}` sign reconciliation that the
parent's eq (14b) suppresses. Independent of any Wilson-sector
conditional dependency.

## Runner result

```
PASSED: 4/4
   V1 (block decomp: M_KS purely off-diagonal in eps-sorted basis): PASS
   V2 (gamma_5 M Hermitian): PASS
   V3 (sign reconciliation det(g5 M) = (-1)^(n/2) * prod (m^2+sigma^2)): PASS
   V4 (strict positivity det(M) > 0 with lower bound m^n): PASS
```

V4 verified on 60 random SU(3) gauge configurations spanning
`L_t ∈ {4, 6}`, `L_s ∈ {4, 6}`, `m ∈ {0.1, 0.3, 0.5, 1.0, 2.0}`, three
seeds each. All passed to machine precision.

## Cluster cap

- Volume cap: 1 of 5 PRs (this campaign block).
- Cluster: this PR is in the `axiom_first_reflection_positivity_*`
  family; first PR in that cluster for this campaign.

## Hard rules adherence

- A_min only: YES — uses only Cl(3) staggered phases, Z^d spatial
  substrate, Grassmann staggered-Dirac action, no external imports.
- Source-only PR: YES — adds 1 docs/ note, 1 scripts/ runner,
  1 logs/runner-cache/ output, 1 block artifact (this file). No
  atlas/harness/audit-data writes.
- No main push: YES — work pushed only to the block25 branch.
- No merge: YES — PR opened for review; not merged.

## Stop criterion

Closure achieved at the narrow-sub-theorem level. Further generalisation
(Wilson sector, asymmetric M_W) belongs to the bridge note's open
frontier; no churn from this block on that front.
