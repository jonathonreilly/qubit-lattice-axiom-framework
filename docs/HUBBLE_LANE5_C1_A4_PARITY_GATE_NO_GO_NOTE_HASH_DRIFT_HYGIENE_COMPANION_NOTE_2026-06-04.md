# Hubble Lane 5 (C1) A4 Parity-Gate No-Go: Note-Hash-Drift Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / note-hash-drift hygiene evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
single 2026-05-09 `audit: salvage wave3c runner and citation hygiene`
edit to the parent
[`HUBBLE_LANE5_C1_A4_PARITY_GATE_NO_GO_NOTE_2026-04-28.md`](HUBBLE_LANE5_C1_A4_PARITY_GATE_NO_GO_NOTE_2026-04-28.md)
— which moved the parent's `note_hash` from
`b4b29e40` (last audited snapshot) to `88879a37` (current head) —
is a Section 7 cross-references citation hygiene edit
that converts the parent's legacy `A4` anchor pointer into a
backticked markdown link with a Section 2(i) dependency label, and
does NOT modify the parent's load-bearing proof content
(Sections 0-6, 8) in any substantive way.

The companion records, in machine-checkable form, that the prior
conditional evidence surface is unchanged by this citation-hygiene
edit.
It is not a new theorem claim, not a status promotion, and not an
attempt to perform re-audit work. If the audit pipeline seeds this
file, it is a meta companion row. This companion writes no audit
verdict and does not supply a direct effective-status change.

**Companion target:** `hubble_lane5_c1_a4_parity_gate_no_go_note_2026-04-28`
(parent note
[`docs/HUBBLE_LANE5_C1_A4_PARITY_GATE_NO_GO_NOTE_2026-04-28.md`](HUBBLE_LANE5_C1_A4_PARITY_GATE_NO_GO_NOTE_2026-04-28.md)).
**Primary runner:**
[`scripts/audit_companion_hubble_lane5_c1_a4_parity_gate_note_hash_drift_hygiene_2026_06_04.py`](../scripts/audit_companion_hubble_lane5_c1_a4_parity_gate_note_hash_drift_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_hubble_lane5_c1_a4_parity_gate_note_hash_drift_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_hubble_lane5_c1_a4_parity_gate_note_hash_drift_hygiene_2026_06_04.txt)

This is an audit-friendly meta companion: the parent's load-bearing
finite-algebra obstruction is independently re-verified by the
parent's own runner with the same `PASS=19 FAIL=0` summary used by
the prior audit, and the single intervening note edit is shown to be
citation hygiene on the bibliographic Section 7 cross-references list
that explicitly addresses the prior conditional verdict's
`notes_for_re_audit_if_any` repair-target text. The companion records
that substance-vs-citation separation as machine-checkable evidence
for later independent audit handling; it does not re-audit the parent
and does not promote status.

---

## 0. Why this companion exists

The parent's most recent archived audit snapshot
(`audit_date 2026-05-01T22:52:39`, codex-gpt-5,
conditional verdict) recorded for the row at
note_hash `b4b29e40...`:

```text
notes_for_re_audit_if_any: other: add the parity-gate carrier theorem
as a cited dependency source or make the runner parse/check the stated
assumption from that source.
```

That verdict's `chain_closure_explanation` reasoned:

```text
The algebraic countermodel part closes: the runner explicitly verifies
that 2+2 parity Z_2 structure is preserved by CAR and non-CAR
rank-four semantics. The carrier-theorem leg does not close from the
restricted inputs because the runner hard-codes the cross-note
assertion that the theorem's Assumption 1 is CAR, while no one-hop
dependency source was provided to verify it.
```

On 2026-05-09 the salvage-wave3c citation hygiene commit
`e954cac5522835993797a2fd76d7095201904f22`
(`audit: salvage wave3c runner and citation hygiene`) applied a
narrow Section 7 cross-references edit that directly addresses this
repair target by converting the unlinked Section 7 bullet for the
parity-gate carrier theorem into a backticked markdown link with the
parenthetical Section 2(i) dependency label.
This edit moved the parent's `note_hash` from `b4b29e40...` to
`88879a37...` and the audit pipeline accordingly archived the prior
conditional verdict and reset the row to `unaudited`.

The honest-stop question is then exactly:

> Did that 2026-05-09 edit modify the parent's load-bearing proof
> content (the Cycle 4 parity-gate no-go argument in Sections 0-6 and
> the boundary in Section 8) — or only the bibliographic
> cross-references list in Section 7, in a way that explicitly addresses the prior
> conditional verdict's stated repair target?

This companion records that the second reading is the one supported
by a line-by-line diff of the only intervening commit. The parent's
runner outputs are identical to the prior snapshot
(`SUMMARY: PASS=19 FAIL=0`), the parent's load-bearing finite-algebra
obstruction in Sections 0-6 is byte-for-byte unchanged, and the
Section 7 list edit is exactly the Section-2(i) dependency-citation
repair the prior audit explicitly requested.

This companion is therefore audit-friendly evidence that the prior
conditional evidence surface is unchanged across the 2026-05-09
citation-hygiene edit. It is not a re-audit and does not promote
status; it documents the substance-vs-citation surface in
machine-checkable form for later independent audit handling.

---

## 1. Parent Recap And Archived Snapshots

The parent
[`HUBBLE_LANE5_C1_A4_PARITY_GATE_NO_GO_NOTE_2026-04-28.md`](HUBBLE_LANE5_C1_A4_PARITY_GATE_NO_GO_NOTE_2026-04-28.md)
is a Lane 5 (C1)-gate Cycle 4 stretch-attempt no-go note closing the
legacy `A4` direct-derivation attack frame negatively. The parent's
theorem (Section 2) reads:

> **Theorem (A4 no-go).** Neither the primitive parity-gate carrier
> theorem nor the bare parity-gate Z_2 structure on `P_A H_cell`
> supplies a derivation of CAR semantics on `P_A H_cell`. Hence
> `A4` cannot close `(G1)` on `A_min` alone.

with proof split into two parts:

1. **(i)** The parity-gate carrier theorem assumes CAR as input
   (Assumption 1: `P_A H_cell ≅ F(C^2)`).
2. **(ii)** The bare parity Z_2 structure on the rank-four block
   has 2+2 spectrum and is preserved by CAR, two-qubit spin, and
   ququart semantics, hence cannot distinguish CAR from non-CAR.

The runner
[`scripts/frontier_hubble_c1_a4_parity_gate_no_go.py`](../scripts/frontier_hubble_c1_a4_parity_gate_no_go.py)
mechanically verifies both parts via 19 finite-algebra and exact
involution-counting checks: parity-signature computation on three
distinct rank-four realizations, CAR Majorana anticommutator
vanishing vs two-qubit `X⊗I, I⊗X` commutator vanishing, and exact
`τ(q)=q+π` involution partition on a 64^n grid for n ∈ {1, 2}
giving `μ=1/2` self-dual half-zone measure.

The earlier clean archived snapshot (codex-current-fresh-context,
high confidence, archived 2026-05-01T14:53 against `note_hash
2d62f33`) recorded a class-A load-bearing step with
`PASS=19 FAIL=0`.

The subsequent conditional archived snapshot
(codex-audit-loop-fresh-agent-hubble-c1-a4-parity-gate-no-go-20260501,
high confidence, archived 2026-05-12T08:18, against
`note_hash b4b29e40`) recorded the repair target
quoted in §0 above, while keeping `PASS=19 FAIL=0` and explicitly
acknowledging the algebraic countermodel closes.

That second snapshot's `verdict_rationale` summarized:

```text
Claim boundary until fixed: the note cleanly shows that a bare 2+2
Z_2 parity gate does not distinguish CAR from non-CAR semantics on
a rank-four block.
```

---

## 2. Invalidation cause

The audit pipeline does not currently record an explicit
`invalidation_reason` field on the second `previous_audits` entry
because the invalidation was driven by the source-side note_hash
drift path in `docs/audit/scripts/seed_audit_ledger.py` (the
`prior.get("note_hash") != node["note_hash"]` branch at line 488)
rather than by the dependency/criticality detector in
`docs/audit/scripts/invalidate_stale_audits.py` (which records
its reasons in `previous_audits[i]["invalidation_reason"]`).

The driving cause is therefore note_hash drift:

```text
note_hash_drift: b4b29e40...  ->  88879a37...
```

i.e., the parent's source-note SHA-256 has changed since the prior
audit was recorded, so the audit pipeline conservatively archived the
prior verdict to `previous_audits` and reset the row to `unaudited`,
even though that single intervening edit is a Section 7
cross-references citation hygiene edit that explicitly addresses the
prior conditional verdict's `notes_for_re_audit_if_any` repair target
and does not touch Sections 0-6, 8.

Git history (filtered to the parent note path) is exactly two
commits since file creation:

```text
5fd2c65a7 audit: capture yt pr230 lsp readout runner output       (file creation)
e954cac55 audit: salvage wave3c runner and citation hygiene       (citation hygiene)
```

Only the second commit is post-snapshot; it carries the
`b4b29e40 -> 88879a37` note_hash drift on this file.

---

## 3. Substance-vs-citation separation

The narrow auditable observation in this companion is:

**(C1) The parent's load-bearing substantive content was not modified
by the 2026-05-09 citation-hygiene edit.** The only line-level diff
on the parent note since the last conditional snapshot has this
material shape (normalized here to current dependency vocabulary):

```text
@@ -176,8 +176,8 @@
-- Primitive parity-gate carrier theorem (the `A4` anchor):
-  `AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md`.
+- Primitive parity-gate carrier theorem (the `A4` anchor; load-bearing one-hop dependency for Section 2(i)):
+  [`AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md`](AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md).
```

In words, the only change is:

1. the inline parenthetical label is extended from "the `A4` anchor"
   to a Section 2(i) one-hop dependency label — naming the same source
   the prior conditional verdict's
   repair target asked to be cited;
2. the bare filename `AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md`
   is wrapped in a backticked markdown link with the same target
   filename as the link href, so the dependency edge becomes
   machine-pickable by the audit pipeline.

No Section 0 (Context) text, no Section 1 (Setup) text, no Section 2
Theorem statement, no part (i)-(iii) of the proof, no Section 3
numerical-verification description, no Section 4 (what this closes)
text, no Section 5 (what this does not close) text, no Section 6
(Cycle ordering implication) text, and no Section 8 (Boundary) text
was modified.

The companion records this separation by:

1. Re-running the parent's runner on the current `origin/main` head
   and confirming the FINAL_TAG and pass count are unchanged with
   `SUMMARY: PASS=19 FAIL=0` (Block 1 of this companion's runner);
2. Confirming via static source-scan that the parent runner
   [`scripts/frontier_hubble_c1_a4_parity_gate_no_go.py`](../scripts/frontier_hubble_c1_a4_parity_gate_no_go.py)
   is byte-for-byte unchanged across the prior snapshot and current
   head (the prior snapshot's `runner_hash` field was `None` so a
   direct hash equality cannot be enforced; the companion instead
   verifies that there is exactly one historical commit touching that
   file path on `origin/main`, namely the file-creation commit
   `5fd2c65a7`, with no subsequent edits) (Block 2);
3. Confirming via static source-scan that the parent's load-bearing
   proof content (Sections 0-6 and Section 8) is byte-for-byte
   identical between the prior `b4b29e40` snapshot and the current
   `88879a37` head, with the only diff confined to the Section 7
   cross-references block (Block 3);
4. Confirming via static source-scan that the Section 7 edit does
   not introduce any new claim, theorem, or quantitative statement;
   the bullet's filename target is identical pre- and post-edit
   (Block 4);
5. Confirming via static source-scan that the Section 7 edit's
   parenthetical Section 2(i) dependency label addresses the prior
   verdict's stated repair target
   (Block 5);
6. Re-verifying the three rank-four parity signatures (CAR
   `(-1)^N`, two-qubit `Z⊗Z`, ququart `Z_4^2`) all give signature
   `(2, 2)` (Block 6);
7. Re-verifying CAR Majorana anticommutator vanishing and two-qubit
   `X⊗I, I⊗X` commutator vanishing (Block 7);
8. Re-verifying exact `τ(q)=q+π` involution partition on a 64^n
   grid for n ∈ {1, 2}: `(n_low, n_high, n_boundary) = (31, 31, 2)`
   for n=1 and `(1985, 1985, 126)` for n=2 (Block 8);
9. No-claim gate preservation across the runs (Block 9).

These are static and dynamic facts about the parent's runner, note,
and git history; they do not depend on generated audit-status fields.

---

## 4. Substance-unchanged assertion

The parent's runner on the current `origin/main` head outputs

```text
SUMMARY: PASS=19  FAIL=0
```

This matches the pass count recorded by both archived snapshots
(the earlier clean snapshot at note_hash `2d62f33`,
runner_check_breakdown A=19; and the later conditional snapshot at
note_hash `b4b29e40`, runner_check_breakdown A=15 B=4 total=19).
The parent's runner code
is byte-for-byte unchanged since file creation (no commits touch the
runner since `5fd2c65a7`). The parent note's load-bearing Sections
0-6 and 8 are byte-for-byte unchanged across the only intervening
note edit. Only the Section 7 cross-references list has the
two-line edit shown in §3.

The substantive bounded no-go content of the parent is therefore
unchanged, and the parent's runner continues to mechanically
demonstrate it. The present companion does not decide how the prior
conditional treatment should be handled under the current generated
ledger view; it only provides the machine-checkable evidence above.

---

## 5. What this companion does NOT do

This companion explicitly does **not**:

- claim a new theorem;
- promote the parent's `effective_status` or `audit_status`;
- modify the parent note text, the parent's runner, or any cited
  dependency note or runner;
- assert that the parent's bounded no-go scope is the only correct
  reading;
- close the parent's open `(G1)` / `(G2)` / `(C1)` gates (those
  remain open exactly as the parent and its sibling cycle notes
  state them);
- weigh in on the parent's status against the parent's open or
  newer sibling notes;
- back-fill or rebut any prior auditor verdict, or set any audit
  status;
- assert that the prior conditional verdict's `notes_for_re_audit_if_any`
  repair target is now mechanically discharged — only that the
  intervening note edit nominally addresses it via a Section 7
  citation; any audit verdict remains independent.

This companion's narrow auditable observation is exactly (C1) in §3.

---

## 6. Audit Handoff

Independent audit handling can decide whether and how to re-audit the
parent under the current `unaudited` state. The present companion
supplies:

- a line-by-line diff of the only intervening note edit on
  `origin/main` since the last audited snapshot, showing the diff is
  confined to the Section 7 cross-references list;
- a re-execution of the parent's runner on the current head, with
  the same `PASS=19 FAIL=0` summary used by both archived snapshots;
- a static source scan that confirms the parent's load-bearing
  Sections 0-6 and 8 are byte-for-byte unchanged across the edit;
- a small set of self-checks (parity signatures, CAR/spin
  anticommutator/commutator, `τ`-involution counts) that exercise
  the parent's substantive content directly.

If later independent audit handling treats the prior conditional
analysis of the parent as reusable under the current note_hash, this
companion records the evidence surface for that treatment. If later
handling re-audits from scratch under the present state, this
companion does not block that path; it only documents the parent's
substance-vs-citation surface across the citation hygiene edit.

This companion's type is meta, with audit-companion scope. It is
not a status change.
