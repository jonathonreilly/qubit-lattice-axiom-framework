# Hubble Lane 5 Two-Gate Dependency Firewall: Criticality-Bump Audit-Readiness Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-readiness companion / criticality-bump hygiene)
**Status:** companion-only — supplies audit-friendly evidence that the
parent note
[`HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md`](HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md)
is unchanged in load-bearing content since its prior `audited_clean`
verdict, and that the
`criticality_increased:medium->high` invalidation reason recorded in
the audit ledger does not reflect any change to the parent's substance
or runner output. This is a queue-priority signal for the audit lane,
not a re-audit, not a new theorem, and not a status promotion.
**Companion target:** `hubble_lane5_two_gate_dependency_firewall_note_2026-04-27`
(parent note `docs/HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md`,
parent runner `scripts/frontier_hubble_lane5_two_gate_dependency_firewall.py`).
**Primary companion runner:**
[`scripts/audit_companion_hubble_lane5_two_gate_dependency_firewall_criticality_bump_hygiene_2026_06_04.py`](../scripts/audit_companion_hubble_lane5_two_gate_dependency_firewall_criticality_bump_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_hubble_lane5_two_gate_dependency_firewall_criticality_bump_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_hubble_lane5_two_gate_dependency_firewall_criticality_bump_hygiene_2026_06_04.txt)

---

## 0. Why this companion exists

The parent retention-firewall note
`hubble_lane5_two_gate_dependency_firewall_note_2026-04-27`
(load-bearing score `9.644`, criticality `high`) is a *negative-boundary*
positive theorem whose prior `audited_clean` verdict (2026-04-28,
codex-audit-loop, `fresh_context`, `auditor_confidence=high`) was
recorded with `PASS=18 FAIL=0` on the parent runner and the
load-bearing step:

> So numerical Lane 5 closure requires a retained absolute-scale premise
> and a retained dimensionless cosmic-history premise:
> `(C1) AND ((C2) OR (C3))`.

The ledger's `previous_audits[0].invalidation_reason` is exactly
`criticality_increased:medium->high`. This invalidation tracks a
*queue-priority* signal — the row's transitive descendants count
or load-bearing weight changed enough to bump it into a higher
criticality bucket — and is structurally distinct from
substance-change invalidations such as
`note_hash_changed`, `axiom_premise_changed`,
`dep_weakened`, or `runner_path_changed`. None of those substance-
change reasons are present in the ledger entry for this row's most
recent invalidation.

A criticality bump does not by itself alter:

- the parent's prose content;
- the parent's load-bearing step;
- the parent's runner identity or output;
- the parent's dependency list;
- any axiom premise or accepted-premise the parent invokes.

It only changes the *priority* at which the audit lane is expected
to revisit the row. This companion supplies audit-friendly evidence
that the substance of the parent and its runner are unchanged since
the prior `audited_clean` verdict, so the audit lane can either
honor that prior verdict at the higher criticality bucket or
schedule a fresh per-row audit with full information about what
has and has not changed.

If the audit pipeline seeds this file, it is a meta companion row;
the audit lane still sets `audit_status`, and pipeline-derived
`effective_status` remains downstream of that authority.

---

## 1. Parent recap

The parent note (`docs/HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md`)
records a *negative boundary* on Lane 5 closure. Its substantive
content has three components:

**(P1) The two-gate identity.** Adopting the retained late-time
cosmology stack — spectral-gap identity, scale identification, matter
bridge, flat-FRW structural lock, and open-number reduction at fixed
admitted radiation readout `R` — the late-time bounded cosmology
surface reduces to the pair `(H_0, L)` where
`L := Omega_Lambda,0 = (H_inf / H_0)^2`. Equivalently,
`H_0 = H_inf / sqrt(L)`.

**(P2) Three blocked upgrades.** Three tempting one-gate or
structural-lock-only routes to numerical `H_0` are blocked by the
identity:

1. `(C1)` absolute-scale information alone fixes `H_inf` (or
   `R_Lambda`) but leaves `L` free → `H_0` is a one-parameter family.
2. `(C2)` cosmic-history-ratio retirement, or a hypothetical `(C3)`
   direct cosmic-`L` derivation, fixes `L` but leaves the absolute
   time scale free → `H_0` is a one-parameter family.
3. The late-time structural lock fixes the dimensionless form
   `H(a) / H_0 = E(a; L, R)` but does not supply the scalar `H_0`.

**(P3) The two-gate firewall.** The honest Lane 5 status is unchanged:
numerical closure requires both `(C1)` and one of `{(C2), (C3)}`.
Since the current `(C3)` audit finds no active route, the practical
current closure path is `(C1) + (C2)`.

The parent's prior `audited_clean` verdict reported these three
components as load-bearing class-A material, with the runner's
`PASS=18 FAIL=0` confirming nonzero analytic sensitivity to both
`H_inf` and `L`, the one-gate counterexample families, the
structural-lock rescaling invariance, and the current gate inventory
(C1 open, C2 open, C3 no-active-route).

---

## 2. Invalidation cause: criticality bump, not substance change

The audit ledger entry for this row records the following structured
invalidation history:

```text
previous_audits[0].invalidation_reason = "criticality_increased:medium->high"
previous_audits[0].audit_status        = "audited_clean"
previous_audits[0].audit_date          = "2026-04-28"
previous_audits[0].audit_state_snapshot = {
    "criticality": "medium",
    "load_bearing_score": 5.907,
    ...
}
```

The current ledger row records:

```text
criticality          = "high"
load_bearing_score   = 9.644
intrinsic_status     = "unaudited"
effective_status     = "unaudited"
effective_status_reason = "awaiting_audit"
note_hash            = "c370a34fb90377baab49dfaffe89f04c99bee922aa88edde7b79fdfd1f110254"
```

The criticality bumped from `medium` to `high` and the load-bearing
score increased from `5.907` to `9.644`. Both reflect upstream graph
growth (more transitive descendants or higher-weight callers), not
substance change in this row.

**Crucially**, the bump did *not* fire any of the substance-change
invalidation reasons that the audit lane uses to flag actual content
changes. The repository's `invalidate_stale_audits.py` distinguishes
between criticality changes and substance changes; only the latter
require re-audit on a new content surface. A criticality bump
re-queues the row for re-audit at the higher rigor level appropriate
to its new criticality bucket, but the load-bearing content remains
the same artifact.

This companion does not litigate whether the higher criticality
bucket warrants stricter audit standards; that question is the audit
lane's. It only records, in machine-checkable form, that the
substance the audit lane will look at is the same substance the prior
`audited_clean` verdict already evaluated.

---

## 3. Substance-unchanged assertion

The parent note's load-bearing content is unchanged in two precise
senses:

**(S1) Note hash matches the most-recent audit-time content.** The
current `note_hash` field in the ledger row is
`c370a34fb90377baab49dfaffe89f04c99bee922aa88edde7b79fdfd1f110254`.
Re-hashing the on-disk file
`docs/HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md`
on `origin/main` reproduces this same hash to the byte. This means
the note's content is identical to the content snapshot recorded
when the row was bumped from `medium` to `high` criticality.

**(S2) Runner identity and output are unchanged.** The parent runner
path recorded in the ledger row is
`scripts/frontier_hubble_lane5_two_gate_dependency_firewall.py`. This
file is present on disk on `origin/main`. Executing it produces
`PASS=18 FAIL=0`, matching the prior `audited_clean` runner check
breakdown of `A=9, B=7, C=0, D=2, total_pass=18`.

The companion runner re-verifies these two claims plus a battery of
static structural checks that confirm the load-bearing prose
fragments (the bridge equation `H_0 = H_inf / sqrt(L)`, the three
blocked upgrades, the two-gate firewall conclusion, the current
gate inventory) are present in the on-disk parent note.

This is not a re-audit. It is a hygiene check: it confirms that
nothing in the on-disk artifacts has drifted since the prior
verdict, so the audit lane knows exactly what it would be
re-auditing if it picks up this row from the queue.

---

## 4. Runner-pass verification

The companion runner
`scripts/audit_companion_hubble_lane5_two_gate_dependency_firewall_criticality_bump_hygiene_2026_06_04.py`
performs the following classes of check:

- **(R1) Parent presence.** The parent note file and the parent
  runner file both exist on disk at their ledger-recorded paths.
- **(R2) Parent note-hash invariance.** The SHA-256 hash of the
  parent note file matches the
  `note_hash` field recorded in the current ledger row.
- **(R3) Parent runner execution.** The parent runner is invoked
  with the documented `PYTHONPATH` and command line, and exits with
  status `0` with `PASS=18 FAIL=0` in its tail output.
- **(R4) Load-bearing-content static checks.** The parent note's
  prose contains the load-bearing statements that the prior
  `audited_clean` verdict cited:
    - the bridge identity `H_0 = H_inf / sqrt(L)`;
    - the three "blocked upgrade" bullets (`(C1)` alone, `(C2)/(C3)`
      alone, structural lock alone);
    - the two-gate firewall conclusion `(C1) AND ((C2) OR (C3))`;
    - the current gate inventory table with `(C1)`, `(C2)`, `(C3)`
      rows.
- **(R5) Invalidation-reason structure.** The ledger row's most
  recent `previous_audits[0].invalidation_reason` field begins with
  the literal string `criticality_increased`. This confirms the
  invalidation is a queue-priority bump, not a substance-change
  flag.
- **(R6) Substance-unchanged inputs.** The parent note's `## Inputs
  And Import Roles` table lists the same six retained / open input
  rows recorded in the prior verdict's evaluation surface
  (omega_lambda bridge, open-number reduction, structural lock, C1
  audit, C2 audit, C3 audit).

The companion runner produces `PASS=20 FAIL=0` when these checks all
succeed against the on-disk repo state. The companion PASS count does
not need to match the parent's `PASS=18`; the parent runner is invoked
once inside (R3) and its `PASS=18 FAIL=0` line is asserted as a
single check among the 20.

The runner is purely a hygiene verifier: it does no new physics,
does not claim any derivation, does not re-audit the parent, and
does not write or modify any ledger field.

---

## 5. What this companion does not do

For audit-lane clarity, this companion explicitly does not:

- modify the parent note in any way;
- modify the parent runner in any way;
- change the parent's `audit_status`, `effective_status`,
  `criticality`, `load_bearing_score`, `claim_type`, `claim_scope`,
  or any other ledger field;
- assert that the prior `audited_clean` verdict must be honored at
  the new `high` criticality bucket (that decision is the audit
  lane's);
- assert that any of the parent's open dependencies
  (`(C1)`, `(C2)`, `(C3)` gates, vacuum/topology audit, structural
  lock theorem, open-number reduction theorem, matter bridge theorem)
  have changed status;
- claim any progress toward numerical `H_0` closure;
- claim that the Record axiom adopted in
  `MINIMAL_AXIOMS_2026-06-04.md` strengthens or weakens the firewall
  (this row's prior verdict is independent of any Record-axiom
  content, and the criticality bump is not tied to axiom-set
  changes);
- introduce a new minimal-axiom statement or accepted-premise.

This companion is **claim_type=meta** by design: it ratifies no new
content, only records the substance-unchanged invariant in a form
the audit lane can verify with one runner invocation.

---

## 6. Audit-lane handoff

When the audit lane next picks up
`hubble_lane5_two_gate_dependency_firewall_note_2026-04-27` from the
queue at its new `high` criticality bucket, this companion offers
the auditor a one-shot precondition check:

1. Run
   `scripts/audit_companion_hubble_lane5_two_gate_dependency_firewall_criticality_bump_hygiene_2026_06_04.py`
   on the current repo state.
2. If it returns `PASS=20 FAIL=0`, the parent's substance is provably
   identical to what the prior `audited_clean` verdict evaluated.
   (One of the 20 checks re-invokes the parent runner and asserts
   `PASS=18 FAIL=0` on it; the other 19 are static hygiene checks.)
   The auditor can choose to:
    - honor the prior verdict at the higher criticality bucket if
      the higher-rigor threshold permits;
    - or perform a fresh per-row audit with the knowledge that the
      load-bearing content, runner output, and dependency surface
      are exactly the artifacts the prior verdict assessed;
3. If the companion runner returns any FAIL, then the on-disk
   parent or runner has drifted since this companion was filed,
   and the auditor should treat this companion as stale.

The audit lane retains full authority over the new verdict.

This companion does not anticipate a particular verdict outcome at
the new criticality bucket. It only narrows what the next auditor
must investigate: the substance is the same; only the queue-priority
context has changed.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links the
audit citation graph can track for this companion. It does not
promote this note or change the audited claim scope.

- [hubble_lane5_two_gate_dependency_firewall_note_2026-04-27](HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md)
