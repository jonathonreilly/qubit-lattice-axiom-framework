# GOAL — Incumbent Axioms + Primitives Panel (block01, 2026-06-20)

**Date:** 2026-06-20
**Slug:** `incumbent-axiom-panel`
**Branch:** `physics-loop/incumbent-axiom-panel-block01-20260620`
**Mode:** blind expert-panel review (meta / governance)
**Target:** honest first-principles verdict on whether the EXISTING foundation
passes muster, held to the SAME standard that just rejected the four proposed
adds (block05 companion).

## Goal

Convene a blind ten-physicist panel to judge the framework's six EXISTING
foundation items from first principles — **not** deferring to the framework's own
self-justification or admissibility rulings:

- **A1 Lattice**, **A2 Quantum**, **A3 Record** (`docs/MINIMAL_AXIOMS_2026-06-05.md`)
- **P1 `scale_reference_primitive`** (`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`)
- **P2 `kinetic_isotropy_primitive`** (`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`)
- **P3 `realized_state_primitive`** (`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`)

For each item decide: passes muster (pass/concern/fail); correctly tiered
(axiom genuinely axiom-class; primitive genuinely a single narrow dynamics-free
datum, not a smuggled axiom); smuggling (does it covertly supply content beyond
its stated scope — esp. A3's K/CPT-orbit clause; P2's emergent-Lorentz/isotropy
answer; P3's typicality/past-hypothesis; the "accept X so lane Y closes"
pattern); objection + minimal fix. Then judge the SYSTEM: minimal, independent,
non-redundant (kinetic_isotropy vs scale_reference; realized_state vs Record),
free of smuggling — remove/demote/split/merge anything?

## Status discipline (binding — physics-loop SKILL.md / AXIOM_MINIMALITY_POLICY.md)

- This lane is a **review**. It sets **no** `audit_status` and **no**
  `effective_status`; the independent audit lane / owner is the sole status
  authority.
- It **adopts, demotes, splits, merges, or re-grades nothing.** Recommended
  changes are recorded as "unmade science-level decisions" per policy §1/§4;
  approval routes through §6 and the machine registry.
- `proposal_allowed = false`. **READ-ONLY** on `docs/audit/data/` and on every
  axiom/primitive source note. No git checkout/commit/push/fetch (orchestrator
  owns git).
- No forbidden audit/publication file touched.

## This block's deliverable (SYNTHESIS author)

- `docs/INCUMBENT_AXIOMS_PRIMITIVES_PHYSICIST_PANEL_REVIEW_2026-06-20.md` — the
  per-item tally (pass/concern/fail; correctly-tiered split; smuggling flagged
  by >=2 panelists with counts), the items that did not cleanly pass, the SYSTEM
  verdict (minimal? independent? non-redundant? + redundancy findings), the
  system-level smuggling consensus, recommended changes, and an honest OVERALL
  bottom line (incl. whether incumbents are held to the same standard as the four
  rejected adds). Header: meta/governance; sets no audit status; independent
  audit lane / owner sole authority.
- pack files: `CLAIM_STATUS_CERTIFICATE_block01.md`, `STATE.yaml`, `GOAL.md`.
- `vocab_lint --fix`; verify no forbidden file touched.

## Out of scope

- Adopting/demoting/splitting any axiom or primitive; setting any audit verdict;
  editing any axiom file or `docs/audit/data/`.
- Re-deriving any downstream physics; re-litigating the four block05 proposals
  (judged separately).

## Stop conditions

- synthesis delivered and pack written (this block's completion);
- worktree externally changes.
