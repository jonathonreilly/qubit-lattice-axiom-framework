# Conditional-Tier Chain Closure: Methodology Proposal

**Date:** 2026-07-08
**Type:** meta (audit-methodology proposal; no physics claim; no premise or
interpretive weight)
**Status authority:** this document changes no row status by itself. The
accompanying code and policy-text changes take effect only when this PR
lands through normal review; statuses then re-derive mechanically on the
next pipeline run.

## The problem

The ledger's chain-closure rule treats an `audited_conditional` dependency
exactly like a failed one: nothing standing on it can be scheduled for
audit at all. As of 2026-07-08 this leaves a large blocked mass (measured
in the hundreds of rows) that is not wrong, not failed, and not even
examined — merely downstream of an honest, named IF.

The audit lane itself already distinguishes these cases inside single
rows: conditional verdicts restate their premises, and several recent
verdicts explicitly declared the row's algebra exact while naming the one
supplied input. The machinery tracks scope fences (`retained_bounded`)
perfectly; it has no way to track inherited conditions at all.

## The change

Mirror the existing Tier-A pattern one tier down. Tier-A admitted
derivation targets already "satisfy chain closure only at the bounded
tier": a clean row depending on one is capped at `retained_bounded`.
This proposal adds, with identical mechanics:

- `audited_conditional` and `retained_conditional` dependencies satisfy
  chain closure only at the CONDITIONAL tier.
- A clean row standing on one is capped at the new effective status
  `retained_conditional`, and the pipeline records the inherited sources
  in a new `inherited_conditional_deps` ledger field.
- The conditional cap dominates the Tier-A bounded cap when both apply
  (conditional is the weaker tier).
- The audit queue marks such rows `ready_tier: conditional` and counts
  them separately; the audit-loop skill gains the corresponding protocol
  (packet must include each conditional dependency's audited claim scope
  verbatim; session reports must name the inherited conditions).

## Invariants (each checkable from the diff)

1. **Monotone honesty.** Conditional-in can only ever produce
   conditional-out. `retained_conditional` is not retained-grade, never
   confers retained-grade support, and `RETAINED_GRADES` is unchanged.
2. **No silent promotions.** Simulated against the live ledger at
   proposal time: ZERO existing rows change effective status on landing
   (no clean row currently sits behind a purely-conditional frontier).
   The change only makes new audits possible; it re-grades nothing.
3. **Immediate effect is scheduling only.** The same simulation finds 26
   unaudited rows become auditable at the conditional tier, including
   `cl3_color_automorphism_theorem` (direct in-degree 55) and
   `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge`
   (gateway to the largest transitive subtree in the backlog). Their
   verdicts remain entirely the audit lane's to decide.
4. **Everything else still blocks.** Failed, renaming, open-gate,
   pending-chain, and unaudited dependencies gate exactly as before; this
   proposal touches only the two conditional statuses.
5. **Visibility.** Every `retained_conditional` row carries
   `inherited_conditional_deps`; the full tower hanging on any given
   condition is a one-line ledger query.
6. **Determinism.** Effective statuses remain a pure function of ledger
   state; no auditor discretion is added or removed.

## Why this is the community norm, not a relaxation

Hypothesis inheritance is the standard convention of the mathematical
literature: results conditional on a named hypothesis state it and
downstream results restate it (the "assuming the Riemann Hypothesis"
genre). Physics practice is the same in prose ("in the quenched
approximation", "assuming factorization"). The current hard block is
stricter than the community norm; this change adopts the norm and adds
what prose citation cannot: mechanical, queryable propagation of every
inherited condition.

The block's original virtue — pressure to derive supplied inputs rather
than build on them — is preserved where it matters and has already done
its work where it cannot: the ledger's own no-go and boundary rows now
prove that several of the load-bearing conditional inputs are not
derivable on their current surfaces at all. For those, the choice is not
"derive vs. inherit" but "inherit visibly vs. never examine".

## What this proposal does NOT do

- No axiom, primitive, Tier-A, or physics-content change of any kind.
- No re-typing of any existing verdict; no retroactive grade changes.
- No change to what `audited_clean` requires.
- No change to renaming/failed/open-gate handling.
- No publication-surface promotion: `retained_conditional` ranks below
  `retained_bounded` in the status ranking and front-door surfaces can
  filter on it explicitly.

## Files changed by this PR

- `docs/audit/scripts/compute_effective_status.py` — conditional-tier
  branch in `clean_status` (mirrors the Tier-A branch), status rank entry,
  `inherited_conditional_deps` persistence.
- `docs/audit/scripts/compute_audit_queue.py` — `ready_tier` computation,
  `conditional_ready_count`, queue rendering.
- `docs/audit/README.md` — the `retained_conditional` status definition
  and the conditional-tier chain-closure paragraph.
- `docs/ai_methodology/skills/audit-loop/SKILL.md` — the conditional-tier
  protocol section and the clarified `audited_conditional` verdict bullet.
- This proposal document.

Generated data files are NOT hand-edited by this PR; the pipeline
re-derives them at landing.

## Rollout and reversibility

Single atomic PR; the behavior is gated entirely by the queue's
`ready_tier` marker and the effective-status computation, so reverting the
PR restores the prior blocking behavior exactly (no data migration in
either direction; `inherited_conditional_deps` fields disappear on the
next pipeline run after a revert).
