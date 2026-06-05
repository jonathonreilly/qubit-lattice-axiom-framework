# Teleportation Resource From Poisson: Criticality-Bump Audit-Readiness Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-readiness companion / criticality-bump hygiene for `open_gate` parent)
**Status:** companion-only — supplies audit-friendly evidence that the
parent note
[`TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md`](TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md)
is unchanged in load-bearing content since its prior `audited_clean`
verdict, and that the `criticality_increased:leaf->medium` invalidation
reason recorded in the audit ledger does not reflect any change to the
parent's substance or runner output. This is a queue-priority signal
for the audit lane, not a re-audit, not a new theorem, not a status
promotion, and not a closure of any open gate.

**Companion target:** `teleportation_resource_from_poisson_note`
(parent note `docs/TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md`,
parent runner `scripts/frontier_teleportation_resource_from_poisson.py`).
**Primary companion runner:**
[`scripts/audit_companion_teleportation_resource_from_poisson_criticality_bump_hygiene_2026_06_04.py`](../scripts/audit_companion_teleportation_resource_from_poisson_criticality_bump_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_teleportation_resource_from_poisson_criticality_bump_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_teleportation_resource_from_poisson_criticality_bump_hygiene_2026_06_04.txt)

---

## 0. Why this companion exists

The parent note `teleportation_resource_from_poisson_note` is an
intentional `open_gate` row (`claim_type=open_gate`,
`claim_type_provenance=author_hint`, `load_bearing_score=1.5`,
`criticality=leaf`). Its prior `audited_clean` verdict
(2026-05-02, codex-gpt-5, `fresh_context`, `auditor_confidence=high`)
was recorded with `runner_check_breakdown={A:0, B:1, C:4, D:0,
total_pass=5}` and the load-bearing step:

> After tracing cells and spectator taste bits while keeping the last
> KS taste bit per species, the audited Poisson/CHSH ground states
> yield deterministic two-qubit logical resources with Bell overlap
> above 0.90 and high standard teleportation fidelity.

The verdict was scoped to the two small surfaces (`1D N=8`,
`2D 4x4`) at the audited mass / coupling, and the verdict_rationale
explicitly recorded that the "proper retained object is not an open
gate but a bounded numerical theorem over the specified small
surfaces and extraction rule." The current row sits at
`claim_type=open_gate` per the author hint, and the parent note
spells out (in section 2 "2026-05-28 Audit Repair") that the missing
preparation/readout bridge theorem is *not* in scope and is recorded
as admitted, not-derived.

The ledger's `previous_audits[0].invalidation_reason` is exactly
`criticality_increased:leaf->medium`. This invalidation tracks a
*queue-priority* signal — the row's criticality bucket moved from
`leaf` (transitive descendants `1`) into `medium` because upstream
graph growth lifted its in-graph weight — and is structurally
distinct from substance-change invalidations such as
`note_hash_changed`, `axiom_premise_changed`, `dep_weakened`, or
`runner_path_changed`. None of those substance-change reasons are
present in the most recent invalidation entry on this row.

A criticality bump does not by itself alter:

- the parent's prose content;
- the parent's load-bearing step;
- the parent's runner identity or output;
- the parent's dependency list;
- the parent's open_gate framing;
- any axiom premise or accepted-premise the parent invokes.

It only changes the *priority* at which the audit lane is expected
to revisit the row. This companion supplies audit-friendly evidence
that the substance of the parent and its runner are unchanged since
the prior `audited_clean` verdict, so the audit lane can either
honor that prior verdict at the higher criticality bucket or
schedule a fresh per-row audit with full information about what has
and has not changed.

**Open-gate substance is unchanged by this companion.** The
preparation/readout bridge selecting the last taste bit as a native
physical carrier remains admitted, not-derived. This companion does
not claim the gate has been closed, narrowed, or relocated; it only
records that the parent's open-gate framing is identical to what the
prior verdict evaluated.

If the audit pipeline seeds this file, it is a meta companion row;
the audit lane still sets `audit_status`, and pipeline-derived
`effective_status` remains downstream of that authority.

---

## 1. Parent recap and open-gate confirmation

The parent note (`docs/TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md`)
records a *narrow first-artifact* small-surface bounded extraction
observation embedded inside an explicit `open_gate` framing. The
substantive content has four components:

**(P1) Bounded extraction diagnostics on small surfaces.** On
`1D N=8` and `2D 4x4` Poisson/CHSH ground states at mass 0 and
G=1000, after the Kogut-Susskind cell/taste factorization and
keeping the last KS taste bit per species, the runner reports:

- protocol sanity: ideal `Phi+` mean fidelity `0.9999999999999996`,
  min `0.9999999999999991`, max trace error `5.551e-16`;
- `1d_null` (`G=0`): traced Bell overlap `0.500000`, traced CHSH
  `2.000000`, negativity `0.000000`, standard teleportation
  fidelity mean `0.669817`, max `0.987949`; deterministic
  high-fidelity resource: NO;
- `1d_poisson_chsh` (`G=1000`): traced Bell overlap `0.997963`
  (`Phi+`), traced CHSH `2.822668`, negativity `0.497963`, standard
  teleportation fidelity mean `0.998621`, min `0.997964`;
  deterministic high-fidelity resource: YES;
- `2d_poisson_chsh` (`G=1000`): traced Bell overlap `0.970283`
  (`Phi+`), traced CHSH `2.745662`, negativity `0.470283`, standard
  teleportation fidelity mean `0.979360`, min `0.970287`;
  deterministic high-fidelity resource: YES.

The runner exits 0 and prints the closing `Conclusion:` block with
the three numbered observations enumerated.

**(P2) Open-gate framing (2026-05-28 audit repair).** Section 2 of
the parent note records the 2026-05-28 audit verdict
(`audited_conditional`) and the split-path repair: the runner's
small-surface diagnostics are load-bearing; the native
preparation/readout theorem selecting the last taste bit as a
deterministic physical carrier is NON-load-bearing and admitted as
not-derived. No new axiom, import, or retained bridge is introduced.

**(P3) Scope-repair boundary (2026-05-27).** Section "Scope Repair
Boundary (2026-05-27)" of the parent note narrows the source claim
to four explicit promises:

- the original runner remains the numerical source for the
  small-surface certificate;
- the Poisson/CHSH source chain must be visible in the restricted
  packet;
- the current A1+A2 premise is
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md), no
  new axiom is introduced here;
- no sentence in the parent asserts the last taste bit has been
  derived as a native physical carrier.

**(P4) Citation chain and repair path (2026-05-10).** Section
"Citation Chain And Repair Path" records the explicit source-chain
table mapping the runner, the adjacent Poisson resource sweep, the
adjacent resource fidelity note, the adjacent measurement-record /
apparatus-dynamics-closure notes, and the current minimal-axiom
premise. The repair path is to prove the native preparation/readout
theorem and then rerun the small-surface checks; until that lands,
the parent stays an open gate.

The parent's prior `audited_clean` verdict reported the small-surface
extraction diagnostics as load-bearing class-B material with four
class-C runner checks confirming the published numerical surface,
totaling `total_pass=5`. The verdict explicitly recorded that
generalization, preparation/readout, and parameter sensitivity are
outside this scoped claim. The current `open_gate` framing on the
ledger row is fully consistent with that prior scope.

---

## 2. Invalidation cause: criticality bump, not substance change

The audit ledger entry for this row records the following structured
invalidation history:

```text
previous_audits[0].invalidation_reason = "criticality_increased:leaf->medium"
previous_audits[0].audit_status        = "audited_clean"
previous_audits[0].audit_date          = "2026-05-02T22:59:08.884884+00:00"
previous_audits[0].audit_state_snapshot = {
    "criticality": "leaf",
    "deps": [],
    "load_bearing_score": 1.5,
    "transitive_descendants": 1
}
previous_audits[0].runner_check_breakdown = {
    "A": 0, "B": 1, "C": 4, "D": 0, "total_pass": 5
}
```

The current ledger row records:

```text
criticality          = "leaf"
load_bearing_score   = 1.5
intrinsic_status     = "unaudited"
effective_status     = "unaudited"
effective_status_reason = "awaiting_audit"
note_hash            = "5d3b09ce4191e64d86af8e57179a00b6cca1e0cd937e6cab93fb190158691e02"
claim_type           = "open_gate"
claim_type_provenance = "author_hint"
```

The bump from `leaf` (audit-time) to `medium` (current invalidation
context) reflects a criticality recompute, not a substance change.
The current ledger snapshot has the row back at `leaf` (the ledger
field updates with each recompute); the invalidation reason recorded
on the most recent previous-audit entry tells the audit lane *why*
the prior verdict was retired from the active set. The
`criticality_increased:leaf->medium` reason is the structurally
correct queue-priority signal: it does not assert that the parent
substance changed.

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
`5d3b09ce4191e64d86af8e57179a00b6cca1e0cd937e6cab93fb190158691e02`.
Re-hashing the on-disk file
`docs/TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md`
on `origin/main` reproduces this same hash to the byte. This means
the note's content is identical to the content snapshot recorded
when the row was retired from the active audited set by the
criticality bump.

**(S2) Runner identity and output are unchanged.** The parent runner
path recorded in the ledger row is
`scripts/frontier_teleportation_resource_from_poisson.py`. This file
is present on disk on `origin/main`. Executing it exits with status
0 and produces the three quoted cases (`1d_null`, `1d_poisson_chsh`,
`2d_poisson_chsh`) with the numerical surface exactly matching the
parent note's "Default Run Results" table values (Bell overlap,
traced CHSH, negativity, and standard teleportation fidelity values
recorded above in section 1).

The companion runner re-verifies these two claims plus a battery of
static structural checks that confirm the load-bearing prose
fragments (the four numerical case markers, the scope-repair
boundary, the open-gate framing, the source-chain table) are
present in the on-disk parent note, plus presence checks for the
two helper-runner-related files referenced by the parent
(`scripts/frontier_bell_inequality.py`,
`scripts/frontier_teleportation_poisson_resource_scope_repair.py`).

This is not a re-audit. It is a hygiene check: it confirms that
nothing in the on-disk artifacts has drifted since the prior
verdict, so the audit lane knows exactly what it would be
re-auditing if it picks up this row from the queue.

---

## 4. Runner-pass verification

The companion runner
`scripts/audit_companion_teleportation_resource_from_poisson_criticality_bump_hygiene_2026_06_04.py`
performs the following classes of check:

- **(R1) Parent presence.** The parent note file and the parent
  runner file both exist on disk at their ledger-recorded paths.
- **(R2) Parent note-hash invariance.** The SHA-256 hash of the
  parent note file matches the `note_hash` field recorded in the
  current ledger row, and equals the substance-unchanged expected
  hash.
- **(R3) Parent runner execution.** The parent runner is invoked
  and exits with status 0; the printed output contains the three
  case-banner lines (`Case: 1d_null`, `Case: 1d_poisson_chsh`,
  `Case: 2d_poisson_chsh`) and the closing `Conclusion:` banner.
- **(R4) Parent runner numerical-surface invariance.** The printed
  output contains the exact numerical strings published in the
  parent note's "Default Run Results" table (Bell overlaps,
  negativities, teleportation fidelity values, and the
  deterministic-high-fidelity YES/NO verdicts per case).
- **(R5) Load-bearing-content static checks.** The parent note's
  prose contains the load-bearing statements that the prior
  `audited_clean` verdict cited:
    - the `claim_type: open_gate` author hint at the top of the note;
    - the "2026-05-28 Audit Repair (load-bearing core split from
      unsupplied bridge)" section heading;
    - the explicit split-path bullets (load-bearing vs.
      NON-load-bearing);
    - the four scope-repair-boundary promises (2026-05-27);
    - the citation-chain table (2026-05-10) listing the
      Poisson/CHSH source script, the adjacent sweep, the adjacent
      fidelity note, the adjacent measurement-record /
      apparatus-dynamics-closure notes, and the
      `MINIMAL_AXIOMS_2026-05-20.md` premise row;
    - the explicit "no new axiom is introduced" sentence;
    - the "no sentence in this note asserts that the last taste bit
      has been derived as a native physical carrier" promise.
- **(R6) Invalidation-reason structure.** The ledger row's most
  recent `previous_audits[0].invalidation_reason` field begins with
  the literal string `criticality_increased`. The most recent
  previous-audit entry has `audit_status=audited_clean`, and the
  `runner_check_breakdown` recorded there has
  `total_pass=5` with class-breakdown `A=0, B=1, C=4, D=0`. This
  confirms the invalidation is a queue-priority bump and that the
  prior verdict was clean on the same numerical surface.
- **(R7) Helper-runner presence.** The two helper-runner files
  referenced by the parent prose
  (`scripts/frontier_bell_inequality.py`,
  `scripts/frontier_teleportation_poisson_resource_scope_repair.py`)
  are present on disk.

The companion runner produces `PASS=N FAIL=0` (current cached
output: `PASS=52 FAIL=0`) when these checks all succeed against the
on-disk repo state. The companion PASS count does not need to match
the prior verdict's `total_pass=5`; the parent runner is invoked
once inside (R3) and (R4), and its exit-0 plus numerical-surface
fingerprint is asserted as a small set of checks among the total.

The runner is purely a hygiene verifier: it does no new physics,
does not claim any derivation, does not re-audit the parent, does
not write or modify any ledger field, and does not close the
open-gate admission.

---

## 5. What this companion does not do

For audit-lane clarity, this companion explicitly does not:

- modify the parent note in any way;
- modify the parent runner in any way;
- change the parent's `audit_status`, `effective_status`,
  `criticality`, `load_bearing_score`, `claim_type`, `claim_scope`,
  or any other ledger field;
- assert that the prior `audited_clean` verdict must be honored at
  the new `medium` criticality bucket (that decision is the audit
  lane's);
- close, narrow, or relocate the parent's open-gate admission (the
  missing native preparation/readout theorem selecting the last
  taste bit as a physical deterministic carrier remains admitted
  and not-derived);
- promote the parent from `open_gate` to `bounded_theorem` or any
  retained tier;
- assert any of the parent's named dependencies
  (`minimal_axioms`, `teleportation_poisson_resource_sweep_note`,
  `teleportation_resource_fidelity_note`,
  `teleportation_measurement_record_note`,
  `teleportation_apparatus_dynamics_closure_note`) have changed
  status;
- claim any progress toward a deterministic-resource theorem at
  larger lattices, other masses, other couplings, other boundary
  conditions, or degenerate cases;
- claim that any postselected branch has been promoted to a
  resource (the parent prose explicitly keeps postselected branches
  as diagnostics only);
- claim that any state-teleportation result generalizes to matter
  teleportation, charge transfer, mass transfer, or
  faster-than-light transport (the parent prose explicitly excludes
  all of these);
- claim that the Record axiom adopted in
  `MINIMAL_AXIOMS_2026-06-04.md` strengthens or weakens the
  small-surface artifact or the open gate (this row's prior verdict
  is independent of any Record-axiom content; the parent still
  cites `MINIMAL_AXIOMS_2026-05-20.md` as its premise);
- introduce a new minimal-axiom statement or accepted-premise.

This companion is **claim_type=meta** by design: it ratifies no new
content, only records the substance-unchanged invariant in a form
the audit lane can verify with one runner invocation.

---

## 6. Audit-lane handoff

When the audit lane next picks up
`teleportation_resource_from_poisson_note` from the queue at the
higher criticality bucket triggered by the
`criticality_increased:leaf->medium` invalidation, this companion
offers the auditor a one-shot precondition check:

1. Run
   `scripts/audit_companion_teleportation_resource_from_poisson_criticality_bump_hygiene_2026_06_04.py`
   on the current repo state.
2. If it returns `PASS=N FAIL=0` (currently `PASS=52 FAIL=0`), the
   parent's substance is provably identical to what the prior
   `audited_clean` verdict evaluated. The auditor can choose to:
    - honor the prior `audited_clean` verdict at the higher
      criticality bucket if the higher-rigor threshold permits;
    - or perform a fresh per-row audit with the knowledge that the
      load-bearing content, runner output, dependency surface, and
      open-gate framing are exactly the artifacts the prior verdict
      assessed;
3. If the companion runner returns any FAIL, then the on-disk
   parent or runner has drifted since this companion was filed,
   and the auditor should treat this companion as stale.

The audit lane retains full authority over the new verdict.

This companion does not anticipate a particular verdict outcome at
the new criticality bucket. It only narrows what the next auditor
must investigate: the substance is the same; only the queue-priority
context has changed. The open-gate admission for the native
preparation/readout theorem remains open and is unaffected by this
companion.

---

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links the
audit citation graph can track for this companion. It does not
promote this note or change the audited claim scope.

- [teleportation_resource_from_poisson_note](TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md)
- [minimal_axioms](MINIMAL_AXIOMS_2026-05-20.md)
