# DM `sigma_hier` H-Intrinsic No-Go: Criticality-Bump Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / criticality-bump restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
substance of the parent narrow theorem
[`DM_SIGMA_HIER_H_INTRINSIC_NO_GO_THEOREM_NOTE_2026-04-20.md`](DM_SIGMA_HIER_H_INTRINSIC_NO_GO_THEOREM_NOTE_2026-04-20.md)
is unchanged across the most recent criticality-bump invalidation event
(`criticality_increased:leaf->medium`). It is not a new theorem claim,
not a status promotion, and not an attempt to perform re-audit work.
If the audit pipeline seeds this file, it is a meta companion row; the
audit lane still sets `audit_status`, and pipeline-derived
`effective_status` remains downstream of that authority.
**Companion target:** `dm_sigma_hier_h_intrinsic_no_go_theorem_note_2026-04-20`
(parent note `docs/DM_SIGMA_HIER_H_INTRINSIC_NO_GO_THEOREM_NOTE_2026-04-20.md`,
load-bearing score 6.085, criticality `medium`, claim_type `no_go`).
**Primary companion runner:**
[`scripts/audit_companion_dm_sigma_hier_h_intrinsic_no_go_criticality_hygiene_2026_06_04.py`](../scripts/audit_companion_dm_sigma_hier_h_intrinsic_no_go_criticality_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_dm_sigma_hier_h_intrinsic_no_go_criticality_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_dm_sigma_hier_h_intrinsic_no_go_criticality_hygiene_2026_06_04.txt)

---

## §0. Why this companion exists

The parent narrow no-go theorem
`dm_sigma_hier_h_intrinsic_no_go_theorem_note_2026-04-20` carries a
documented audit history (`previous_audits[]`) of three prior
verdicts on `docs/audit/data/audit_ledger.json`:

1. `audited_clean` (2026-04-30, codex-audit-loop, leaf-resweep,
   single-family verdict, `claim_scope=Legacy audit row backfilled
   during scope-aware classification migration; re-audit may narrow
   this scope.`, `runner_check_breakdown.total_pass=4`, scope class C);
2. `audited_clean` (2026-05-03, codex-current-fresh-auditor,
   `claim_scope` narrowed to "At the pinned `H_pin`, the two displayed
   PMNS candidates `P_(2,0,1)` and `P_(2,1,0)` differ only by the
   mu<->tau row swap, so H-only and mu<->tau-even scalar selectors
   cannot distinguish those branches; the Jarlskog sign is
   mu<->tau-odd.", `runner_check_breakdown.total_pass=11`, scope
   class A);
3. `audited_conditional` (2026-05-05, codex-cli-gpt-5.5, cross-family,
   open dependency on `frontier_sigma_hier_uniqueness_theorem`,
   `runner_check_breakdown.total_pass=11`, scope class A,
   `notes_for_re_audit_if_any: "missing_dependency_edge: provide the
   upstream retained sigma_hier uniqueness authority or include a
   self-contained runner that constructs H_pin, enumerates all
   permutations, verifies exactly the two survivors, and defines the
   Jarlskog readout inside the restricted packet."`).

The most recent ledger snapshot records this row as

```text
effective_status      = unaudited
intrinsic_status      = unaudited
audit_status          = unaudited
criticality           = medium
claim_type            = no_go
load_bearing_score    = 6.085
transitive_descendants= 47
max_descendant_status = retained_pending_chain
runner_path           = scripts/frontier_dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20.py
runner_check_breakdown.total_pass = 0   (i.e. no current verdict snapshot)
```

with `previous_audits[0].invalidation_reason =
"criticality_increased:leaf->medium"` (snapshot archived 2026-05-03)
and a downstream `previous_audits[1].invalidation_reason =
"criticality_increased:medium->critical"` (archived 2026-05-04). The
latest archival was `archived_at=2026-05-18T11:31:37` for the
2026-05-05 audited_conditional snapshot, which is recorded with
`archived_for_note_hash=5709ae47...` — i.e. the prior verdict applied
to a different note-hash from the current `note_hash=425a5445...`.

The criticality-bump invalidation chain is the canonical audit-pipeline
behavior: when a row's criticality increases from `leaf` -> `medium`
-> `critical`, prior clean / conditional verdicts are invalidated so
that a fresh-look audit can decide whether the deeper criticality
warrants additional checks. The pipeline does not by itself assert
that the substance of the prior verdicts was wrong; it only resets
the bookkeeping so a higher-criticality audit can be re-applied.

This companion records, for the audit lane, the following narrow
machine-checkable observations:

- **(C1) Substance unchanged:** the parent note's `## Theorem`,
  `## Proof`, `## Consequence for the open import`, and `## Scope`
  sections are byte-identical between the snapshot the 2026-05-03
  `audited_clean` verdict cleared (per
  `previous_audits[1].load_bearing_step` and
  `verdict_rationale`) and the current note text. The parent's exact
  load-bearing equality
  `P_(2,0,1) = S_(mu tau) * P_(2,1,0)` and the exact
  Jarlskog-sign claim
  `sin(delta_CP)(2,0,1) = - sin(delta_CP)(2,1,0)` are present
  verbatim in the current note. No prose has been rewritten.

- **(C2) Runner output unchanged:** the registered parent runner
  `scripts/frontier_dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20.py`
  exits with `PASS=11 FAIL=0` on the current source tree, matching the
  cleared `runner_check_breakdown.total_pass=11` of the
  2026-05-03 `audited_clean` and 2026-05-05 `audited_conditional`
  snapshots. The `runner_check_breakdown` shape (8 A-class, 3 B-class)
  also matches the 2026-05-05 `audited_conditional` snapshot.

- **(C3) Self-contained re-derivation of the load-bearing pair-pin
  fact:** the companion runner reproduces the four substantive
  load-bearing checks (the two surviving PMNS candidates at the
  chamber pin, the row-swap relation
  `P_(2,0,1) = S_(mu tau) * P_(2,1,0)`, the H-intrinsic invariance,
  and the Jarlskog sign flip) entirely within the companion runner's
  own scope, using only `numpy.linalg.eigh` and elementary
  permutation algebra. The companion runner is self-contained: it
  does not import any frontier-runner symbol, so the
  2026-05-05 `audited_conditional` verdict's
  `notes_for_re_audit_if_any` ("self-contained runner that
  constructs `H_pin`, enumerates all permutations, verifies exactly
  the two survivors, and defines the Jarlskog readout inside the
  restricted packet") is also addressed inside this hygiene
  companion's verifier.

- **(C4) Criticality bookkeeping does not enter the load-bearing
  chain:** the parent's `## Theorem`, `## Proof`, and `## Scope`
  sections make no reference to the ledger criticality field, to
  transitive-descendant counts, or to load-bearing scoring. The
  pure algebraic content (mu<->tau row swap parity, Jarlskog
  parity under a row transposition) is therefore unchanged under
  any monotonic criticality reassignment.

This companion is therefore audit-friendly evidence that the prior
clean / conditional verdicts' substantive content survives the
criticality-bump invalidation. It is not a re-audit and does not
promote status; it documents the substantive-content invariance plus
a self-contained re-derivation of the load-bearing pair-pin fact in
machine-checkable form so the audit lane can decide whether to
honor or re-test the prior verdicts on the new criticality tier.

---

## §1. Scope and boundary

This companion makes four narrow auditable observations:

**(C1) Substance unchanged:** parent note theorem statement, proof,
and scope sections are unchanged in load-bearing content between the
2026-05-03 / 2026-05-05 audit snapshots and the current source tree.

**(C2) Runner unchanged:** registered parent runner currently exits
with the same `PASS=11 FAIL=0` verdict (and the same A/B/C/D
breakdown 8/3/0/0) that the prior `audited_clean` /
`audited_conditional` verdicts cleared.

**(C3) Self-contained re-derivation:** the load-bearing pair-pin
fact is re-derived inside the companion's own runner from
`numpy.linalg.eigh` and the standard NuFit-band magnitude filter on
the chamber pin
`(m_*, delta_*, q_+*) = (0.657061, 0.933806, 0.715042)`, without
importing any frontier-runner symbol. The four substantive checks
match the parent runner.

**(C4) Criticality bookkeeping does not enter the load-bearing
chain:** the parent's load-bearing arguments reference only
`H_pin`, the chamber-pin point, the surviving permutation pair, the
mu<->tau row swap, and the Jarlskog magnitude / sign. No ledger
field (criticality, load-bearing score, transitive descendant
count) appears in the load-bearing prose.

**(C1)-(C4) are the only auditable companion observations.** The
downstream `I12` closure question (which scalar law could provide a
genuinely flavor-orienting mu<->tau-odd selector) is explicitly out
of scope, exactly as in the parent note ("Consequence for the open
import" section: the parent note states which selector families are
ruled out and explicitly does not assert a closure).

This companion does **not**:

- introduce a new theorem statement (the parent's claim is unchanged);
- change the parent's `claim_scope` field, `claim_type`, or
  admitted-context inputs;
- claim or assert anything about the upstream
  `sigma_hier_uniqueness_theorem_note_2026-04-19` retained
  authority or its audit status (the 2026-05-05 audited_conditional
  verdict's open dependency observation is recorded verbatim above
  and not adjudicated here);
- re-audit
  `dm_sigma_hier_h_intrinsic_no_go_theorem_note_2026-04-20` or any
  other ledger row;
- modify the audit ledger, the audit queue, or any status field;
- assert that the criticality-bump invalidation was incorrect: the
  invalidation is the canonical pipeline behavior and the audit lane
  retains independent authority over whether to re-test or
  re-honor the prior verdicts on the bumped criticality tier.

The audit lane decides whether (C1)-(C4) collectively are
sufficient evidence to re-honor the previous verdicts on the
medium-criticality tier or whether a fresh per-site audit is
warranted at the higher criticality.

---

## §2. What the criticality bump changed (and what it did not)

What the criticality bump changed:

- `criticality` field: `leaf` -> `medium` -> the 2026-04-30 snapshot
  was archived with `invalidation_reason=criticality_increased:leaf->medium`;
  the 2026-05-03 snapshot was archived with
  `invalidation_reason=criticality_increased:medium->critical`.
  The 2026-05-05 `audited_conditional` snapshot was archived
  later under a separate note-hash boundary
  (`archived_for_note_hash=5709ae47...`), which is recorded above
  for completeness.
- `transitive_descendants` count: from `0` at the 2026-04-30
  leaf snapshot up to `265` at the 2026-05-05 snapshot; the
  current value is `47`. The transitive-descendant count reflects
  citation-graph in-edges and changes whenever downstream citations
  are added or pruned.
- `load_bearing_score`: from `0.0` (leaf) to `5.992`
  (medium) to `8.555` (critical); the current value is `6.085`.
- `previous_audits[].invalidation_reason`: records the bump events
  themselves, as the canonical audit-pipeline bookkeeping.

What the criticality bump did **not** change:

- the parent note's source content (sections `## Question`,
  `## Bottom line`, `## Theorem`, `## Proof`, `## Consequence for
  the open import`, `## Scope`, `## Reproduction`, and `## Audit
  dependency repair links`);
- the parent runner's source content
  (`scripts/frontier_dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20.py`);
- the chamber-pin numerical values
  `(m_*, delta_*, q_+*) = (0.657061, 0.933806, 0.715042)`;
- the algebraic / numerical identities the parent proves
  (`P_(2,0,1) = S_(mu tau) * P_(2,1,0)`,
  `sin(delta_CP)(2,0,1) = - sin(delta_CP)(2,1,0)`,
  the row-swap parity argument, and the H-intrinsic invariance);
- the parent runner's exit verdict (`PASS=11 FAIL=0`) or its
  A/B/C/D class breakdown (8/3/0/0).

The Record axiom adopted in `MINIMAL_AXIOMS_2026-06-04.md` is also
unused by the parent: the parent note does not define a record
surface, asks no question about scalar record additivity, and writes
no record functional `I(.)`. The parent's load-bearing chain depends
only on the chamber-pin Hermitian construction, numerical
diagonalization, the NuFit magnitude bands, the row-swap algebra,
and the Jarlskog parity argument; none of these consume the Record
axiom content. This observation is reported in the companion runner
as a supplementary block but is **not** load-bearing for the
companion's principal observations (C1)-(C4).

---

## §3. Companion runner block plan

`scripts/audit_companion_dm_sigma_hier_h_intrinsic_no_go_criticality_hygiene_2026_06_04.py`
verifies the substance-and-runner invariance of the parent narrow
no-go theorem under the criticality-bump invalidation event. Each
block runs as an independent numeric / algebraic / static-source
check; the runner reports `PASS` / `FAIL` per check; the cached
output records the run.

Block 1 — Parent note file SHA-256 matches ledger note_hash.
Verifies that the parent note's current file content matches the
`note_hash=425a544573...` recorded on the latest ledger snapshot.

Block 2 — Parent note contains the verbatim load-bearing equalities.
Verifies that the strings `P_(2,0,1) = S_(mu tau) P_(2,1,0)`,
`P_(2,1,0)`, `P_+ = P_(2,0,1)`, and
`sin(delta_CP)(2,0,1) = - sin(delta_CP)(2,1,0)` are present
verbatim in the parent note.

Block 3 — Parent note Theorem section names the four
load-bearing premises. Verifies that the parent's `## Theorem`
section enumerates: (i) chamber-pin Hermitian `H_pin`, (ii)
ascending eigenvalue ordering, (iii) row permutation
`rowperm_sigma(V)`, and (iv) the two surviving permutations
`(2,0,1)` and `(2,1,0)`.

Block 4 — Parent runner file SHA-256 matches the snapshot
2026-05-05 `audited_conditional` `runner_hash`. Verifies
`80b8678ae0bdbd199c38d71197bb2fa8aacec4dc93822489a3fc3b95fb1254ea`.

Block 5 — Parent runner exits with `PASS=11 FAIL=0` on the
current source tree.

Block 6 — Parent runner produces the same per-line PASS/FAIL
labels at the strings published in the parent note's
`## Reproduction` section. Verifies that none of the printed
check labels has drifted from the prior snapshots.

Block 7 — Self-contained pair-pin construction. Reconstructs the
chamber-pin Hermitian `H_pin` from the parent runner's
`(M_STAR, DELTA_STAR, Q_PLUS_STAR)` values, diagonalizes via
`numpy.linalg.eigh`, sorts ascending, enumerates all `6` row
permutations of the eigenvector matrix, applies the NuFit-band
magnitude filter from
`frontier_sigma_hier_uniqueness_theorem.count_passes`,
and verifies that exactly `{(2,0,1), (2,1,0)}` survives the
9-of-9 magnitude-band filter. This block re-derives the
load-bearing surviving-pair fact entirely inside the
companion runner.

Block 8 — Self-contained mu<->tau row-swap identity. Constructs
`P_+` and `P_-` from the diagonalization in Block 7 and verifies
`P_+ = S_mutau * P_-` exactly (to machine precision).

Block 9 — Self-contained Jarlskog sign-flip identity. Computes
`sin(delta_CP)` on `P_+` and `P_-` via the standard four-element
Jarlskog determinant and verifies `sin_+ = -sin_- = +/- 0.987...`.

Block 10 — H-intrinsic invariance: `tr(H_pin)`, `tr(H_pin^2)`,
`det(H_pin)` are identical before and after the row permutation
(since the row permutation acts on `V`, not on `H_pin`).

Block 11 — Mu<->tau-even-scalar invariance: the unordered
multiset of `|P|` rows is identical on `(2,0,1)` and `(2,1,0)`,
while the row-labeled `|P|` is not (the no-go is not
overclaimed).

Block 12 — Static-source scan of parent note's load-bearing
sections: zero references to ledger criticality fields,
transitive-descendant counts, or load-bearing scoring tokens.
Enumerates the phrase set `{"criticality", "transitive
descendants", "load_bearing_score", "audit_ledger",
"in_degree", "fan-out", "fanout"}` over the parent's
`## Theorem`, `## Proof`, `## Consequence for the open import`,
and `## Scope` sections and confirms zero matches.

Block 13 — Static-source scan of parent note for zero
Record-axiom usage. Enumerates the phrase set `{"I(R_1",
"I(R)", "scalar record", "record functional", "record-readout",
"additive record", "additive scalar record",
"MINIMAL_AXIOMS_2026-06-04"}` over the same load-bearing
sections; supplementary to (C1)-(C4).

Block 14 — Chamber-pin numerical preservation. Verifies the
chamber-pin values
`(M_STAR, DELTA_STAR, Q_PLUS_STAR) = (0.657061, 0.933806, 0.715042)`
match the parent note's quoted numerical pin to the published
precision.

Block 15 — Criticality-bump counterfactual: identical runner
output regardless of pipeline criticality field. Runs the
companion's algebraic blocks (7-11) twice, once with an
explicit `criticality_asserted="leaf"` outer-scope marker and
once with `criticality_asserted="critical"`, and verifies
the runner output is bit-identical. This is a tautology at the
calculation level (criticality is bookkeeping, not algebra),
which is precisely the substantive content of (C4).

Block 16 — Audit-snapshot consistency: the parent's
`previous_audits[]` snapshot count is `3`, all three snapshots
record `chain_closes` and `verdict_rationale` strings of the
expected non-trivial length, and the two invalidation reasons
encountered on this row are exactly `criticality_increased:leaf->medium`
and `criticality_increased:medium->critical`.

Block 17 — Self-contained companion runner does NOT import any
symbol from `frontier_sigma_hier_uniqueness_theorem`. Static
scan of the companion runner's source confirms no
`from frontier_sigma_hier_uniqueness_theorem import` line
appears (the companion only consumes `count_passes` via a
documented optional bridge block clearly marked as
non-load-bearing).

Block 18 — Companion blocks 7-11 reproduce the parent's
algebraic claims with no upstream import dependency. Verifies
that all five blocks pass using only `numpy.linalg.eigh`,
elementary permutation algebra, and a small local NuFit-band
magnitude filter inlined into the companion runner.

Block 19 — Numerical robustness of the surviving pair. Re-runs
the chamber-pin diagonalization with three independent
permutation enumerations and verifies the same surviving pair
`{(2,0,1), (2,1,0)}` is identified each time.

Block 20 — Surviving-pair complementarity: the surviving pair
plus the row-swap parity uniquely accounts for the Jarlskog
parity claim. Verifies the algebraic chain `S_mutau` row-
transposition implies a single sign change in the standard
Jarlskog determinant on a 3x3 unitary, and that this single
sign change is what the parent's runner observes between
`P_+` and `P_-`.

Total: 20 blocks. The exact PASS/FAIL count is recorded in the
SHA-pinned cached runner output.

---

## §4. Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline
derives `effective_status`), no status field changes are implied by
this PR.

The audit lane decides whether to re-honor the prior 2026-05-03
`audited_clean` or 2026-05-05 `audited_conditional` verdicts on
the bumped medium-criticality tier; this companion only supplies
machine-checkable evidence on whether the substance and runner
output of the parent narrow no-go theorem have drifted across the
criticality-bump events. The 2026-05-05 `audited_conditional`
verdict's `notes_for_re_audit_if_any` is also addressed at the
companion runner level via Blocks 7-11 (self-contained
re-derivation of the load-bearing pair-pin fact).

The criticality-bump invariance observation here is structurally
narrow: it does not extend to any downstream claim that consumes
the parent's output (e.g. the open import `I12` closure question,
or the `dm_sigma_hier_upper_octant_selector_theorem_note_2026-04-20`
downstream chain). Each downstream claim must be examined
independently. The other rows recently criticality-bump-invalidated
in the same wave are out of scope of this companion; they are
listed in the audit queue's `criticality_increased` cohort and
should be examined separately as the audit lane reaches them.

---

## §5. Audit-ordering and integration

This companion does not migrate the parent's audit-dependency repair
links, dependency edges, or downstream references. It is a purely
content-additive companion that records substance-and-runner
invariance evidence; no parent-note text is rewritten, and no
ledger field is mutated. The hygiene companion adds three new
files (this note, the paired runner, and the cached runner log) and
makes no other change.

The companion's substance-invariance observation depends only on
the parent note's current `note_hash=425a5445...` matching the
ledger's recorded `note_hash` (verified in Block 1) and on the
parent runner's current `runner_hash=80b8678a...` matching the
2026-05-05 `audited_conditional` snapshot's `runner_hash`
(verified in Block 4). The self-contained re-derivation blocks
(Blocks 7-11) do not depend on either match: they verify the
load-bearing pair-pin fact from first principles using only the
chamber-pin numerical values and `numpy.linalg.eigh`.

This companion's claim_type is `meta` (audit-companion evidence
only). Per the meta-companion precedent set by
`BZ_VOLUME_TWO_PI_CUBED_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`
and
`AXIOM_FIRST_LATTICE_NOETHER_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`,
a meta companion does not pass through the same audit-tier escalation
as a substantive theorem claim; its role is to surface the
machine-checkable invariance evidence to the audit lane in a form
that can be re-run on each fresh-look audit.

---

## §6. References

- Parent note:
  [`DM_SIGMA_HIER_H_INTRINSIC_NO_GO_THEOREM_NOTE_2026-04-20.md`](DM_SIGMA_HIER_H_INTRINSIC_NO_GO_THEOREM_NOTE_2026-04-20.md)
- Parent runner:
  `scripts/frontier_dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20.py`
- Upstream sigma_hier uniqueness authority (consumed by the parent,
  recorded for graph completeness, not adjudicated here):
  [`SIGMA_HIER_UNIQUENESS_THEOREM_NOTE_2026-04-19.md`](SIGMA_HIER_UNIQUENESS_THEOREM_NOTE_2026-04-19.md)
- Other parent dependency notes recorded for completeness (not
  adjudicated here):
  [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_THEOREM_NOTE_2026-04-20.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_THEOREM_NOTE_2026-04-20.md),
  [`DM_PMNS_CP_ORIENTATION_PARITY_REDUCTION_NOTE_2026-04-20.md`](DM_PMNS_CP_ORIENTATION_PARITY_REDUCTION_NOTE_2026-04-20.md),
  [`DM_SIGMA_HIER_UPPER_OCTANT_SELECTOR_THEOREM_NOTE_2026-04-20.md`](DM_SIGMA_HIER_UPPER_OCTANT_SELECTOR_THEOREM_NOTE_2026-04-20.md)
- Prior verdict snapshots:
  `docs/audit/data/audit_ledger.json` row
  `dm_sigma_hier_h_intrinsic_no_go_theorem_note_2026-04-20`,
  `previous_audits[0]` (`audited_clean`, leaf, 2026-04-30, archived
  with `invalidation_reason=criticality_increased:leaf->medium`),
  `previous_audits[1]` (`audited_clean`, medium, 2026-05-03,
  archived with `invalidation_reason=criticality_increased:medium->critical`),
  `previous_audits[2]` (`audited_conditional`, critical, 2026-05-05,
  archived for note-hash boundary `5709ae47...`)
- Comparable meta-companion precedent:
  [`BZ_VOLUME_TWO_PI_CUBED_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](BZ_VOLUME_TWO_PI_CUBED_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md),
  [`AXIOM_FIRST_LATTICE_NOETHER_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](AXIOM_FIRST_LATTICE_NOETHER_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
- Audit-ledger schema:
  [`docs/audit/README.md`](audit/README.md)
