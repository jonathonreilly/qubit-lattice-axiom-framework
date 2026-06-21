# Foundation Revision Changeset — Claim Status Certificate (block02)

**Loop slug:** `foundation-revision-proposal`
**Campaign:** `foundation-revision-changeset-block02-20260620`
**Block:** block02
**Cycle:** 1
**Date:** 2026-06-21
**Branch:** `physics-loop/foundation-revision-changeset-block02-20260620`

## Output type

**READY-TO-APPLY governance CHANGESET (DRAFT)** — not an adoption, not a retained
claim, not a derivation to be promoted. `hypothetical_axiom_status: proposed`;
`proposal_allowed=false`. The owner plus the independent audit lane are the
**sole authority** to adopt. Nothing here sets, predicts, or estimates an audit
verdict.

## What block02 produced (over block01's proposal)

block01 produced the OLD->NEW proposal + adversarial re-checks
(`docs/FOUNDATION_REVISION_PROPOSAL_2026-06-20.md`). block02 turns that into an
**applyable changeset draft** and folds in the independent Codex cross-check:

1. **`docs/MINIMAL_AXIOMS_2026-06-21_PROPOSED.md`** — full proposed revised memo,
   supersedes-references the 2026-06-05 canonical memo **on approval only** (does
   not replace it). Contains revised A1 (annotated), A2 (amended + the new
   composition/state-space clause per Codex), A3a (additivity valuation axiom) +
   A3b (conditional realized-outcome identification; neutral antiunitary `K`, not
   CPT), the open-gates section (G-DYN / G-SECT / G-TIME / G-ARROW + Codex's
   G-COMPOSE), and a PROPOSED-REVISION status header.
2. **`.claude/science/physics-loops/foundation-revision-proposal/registry_changeset.patch`**
   — git-applyable unified diff: removes `kinetic_isotropy_primitive` from
   `axiom_premise_nodes.json` (`canonical_ids` + `nodes`) and adds
   `kinetic_isotropy_renormalized_anisotropy_target_2026-06-21` (label `xi_R`) to
   `tier_a_admissions.json` (`genuine_admitted_input_count` 2->3). Verified by
   `git apply --check` (EXIT 0) and a trial application in a scratch copy
   (both JSONs parse valid). **NOT applied.**
3. **`docs/FOUNDATION_REVISION_CHANGESET_README_2026-06-21.md`** — apply-order
   checklist; the human-readable mirror of the patch; the P2 demotion as an
   explicit REVERSAL of the 2026-06-09 owner approval; the P1
   keep-vs-convention open choice; the Codex concordance; the adoption
   consequences (P2-dependent rows -> `retained_bounded` with active re-audit;
   A3b consumers re-cite; hash-guard re-audit).
4. **This certificate** + **STATE.yaml** update.

## How Codex's two additions were incorporated

- **(i) Missing global composition / state-space (Codex's #1).** Folded into the
  **Quantum axiom** as the composition/state-space clause (finite-region tensor
  product `A_R ~= M_{2^{|R|}}(C)`; infinite quasi-local `C*`-algebra `A` =
  UHF/hyperfinite inductive limit; state = normalized positive functional on `A`)
  **AND** added as gate **G-COMPOSE** for any structure beyond the bare factor
  `A`. Consistency guard: `A` remains a **factor** (trivial center), so the
  composition clause does **not** manufacture the sectors A3b needs — G-SECT is
  still load-bearing.
- **(ii) P1 -> unit convention (Codex harsher than the Claude clean panel).**
  Presented as an explicit **OPEN OWNER CHOICE** in both the proposed memo and the
  README §7: Framing K (keep-as-primitive, Claude clean-panel pass) vs Framing C
  (reclassify-as-convention, Codex). The changeset does **not** move P1; if the
  owner picks Framing C, a second small registry patch is needed (not drafted).

## V1-V5 promotion-value gate (changeset/proposal variant)

| # | Question | Answer |
|---|---|---|
| V1 | What finding does this narrow? | Turns block01's adversarially-re-checked proposal into an applyable changeset; closes Codex's two gaps (global composition/state-space; P1-as-convention). |
| V2 | New content? | Verified-applyable registry patch (kinetic_isotropy_primitive demotion); the proposed revised memo with the folded composition/state-space clause + G-COMPOSE; the P1 keep-vs-convention open choice with both framings. |
| V3 | Could the audit lane already produce this? | No — it is wording/governance requiring owner authority to adopt; the audit lane sets statuses but does not author premise-surface wording. |
| V4 | Non-trivial marginal content? | Yes: a verified git patch reversing a logged owner approval (P2); a genuine premise-count reduction (primitives 3->2, possibly ->1 under Framing C); conversion of silent presuppositions into five auditable gates. |
| V5 | One-step variant of a landed cycle? | No — first changeset-assembly cycle; incorporates an independent second-model (Codex) cross-check. |

**V-gate result:** PASS for `changeset / proposal` output type.

## Status fields

```yaml
actual_current_surface_status: proposal
target_claim_type: governance_changeset_draft
hypothetical_axiom_status: proposed
proposal_allowed: false
conditional_surface_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
owner_and_audit_lane_sole_authority: true
claim_type_reason: |
  Ready-to-apply foundation-revision changeset DRAFT for the owner's governance
  decision + independent audit-lane review. Edits no canonical/registry surface:
  the registry mutation is emitted as a git-applyable patch (verified by
  git apply --check) plus a human-readable diff, never written. P2's re-tier
  reverses the logged 2026-06-09 owner approval and cannot land without explicit
  owner reversal + audit-lane re-audit.
```

## Cross-check concordance (two independent models)

Claude clean first-principles panel and Codex / gpt-5.5 (xhigh) **agree** on:
A3 split (Record FAIL -> A3a axiom + A3b conditional, `K` not CPT); P2 re-tier
(kinetic_isotropy_primitive FAIL -> demote); system dynamics+time
under-completeness. **Codex adds:** (i) missing global composition/state-space
(its #1; folded into Quantum + G-COMPOSE); (ii) P1-as-convention (open owner
choice). Direction identical; Codex one notch harsher
(`unsound as a complete foundation` vs `needs_revision`).

## Independent audit + owner approval required

YES. Adoption requires explicit owner approval recorded in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` and the machine registry (including
explicit **reversal** of the 2026-06-09 `kinetic_isotropy_primitive` approval),
plus independent audit-lane review and hash-guard re-audit of all dependents.

## What this does NOT do

- Does not edit `docs/MINIMAL_AXIOMS_2026-06-05.md` (canonical memo intact).
- Does not edit `docs/audit/data/axiom_premise_nodes.json` or
  `docs/audit/data/tier_a_admissions.json` (changes emitted as the patch + diff).
- Does not apply the patch, adopt the memo, set any audit status, reverse the
  2026-06-09 approval, or move P1.
- Does not add a dynamics axiom (gaps are flagged gates).
