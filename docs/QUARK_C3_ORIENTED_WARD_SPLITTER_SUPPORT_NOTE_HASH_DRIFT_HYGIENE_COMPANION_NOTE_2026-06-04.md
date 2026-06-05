# Quark C3-Oriented Ward Splitter Support: Note-Hash-Drift Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / note-hash-drift hygiene evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
single 2026-05-12
`audit: nightly repair and pipeline refresh (automated) [skip ci]`
edit to the parent
[`QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md`](QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md)
— which moved the parent's `note_hash` from
`b44ed058` (last audited snapshot) to `d92f91a2` (current head) —
is an appended `Audit dependency repair links` graph-bookkeeping
section that directly addresses the prior conditional verdict's
`missing_dependency_edge` repair target by listing the four named
one-hop dependency surfaces as explicit backticked
references, and does NOT modify the parent's load-bearing proof
content (Sections 1-9 and the `Hypothesis set used` paragraph) in
any substantive way.

The companion records, in machine-checkable form, that the prior
audit's substantive content survives this dependency-edge bookkeeping
edit. It is not a new theorem claim, not a status promotion, and not
an attempt to perform re-audit work. If the audit pipeline seeds
this file, it is a meta companion row. This companion writes no
audit verdict and does not supply a direct effective-status change.

**Companion target:** `quark_c3_oriented_ward_splitter_support_note_2026-04-28`
(parent note
[`docs/QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md`](QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md)).
**Primary runner:**
[`scripts/audit_companion_quark_c3_oriented_ward_splitter_note_hash_drift_hygiene_2026_06_04.py`](../scripts/audit_companion_quark_c3_oriented_ward_splitter_note_hash_drift_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_quark_c3_oriented_ward_splitter_note_hash_drift_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_quark_c3_oriented_ward_splitter_note_hash_drift_hygiene_2026_06_04.txt)

This is an audit-friendly meta companion: the parent's load-bearing
exact C3-equivariant Hermitian normal-form algebra is independently
re-verified by the parent's own runner with the same
`TOTAL: PASS=51, FAIL=0` summary used by the prior audit, and the
single intervening note edit is shown to be a strictly-additive
dependency-edge bookkeeping append that explicitly addresses the
prior conditional verdict's stated repair target. The companion
records that substance-vs-bookkeeping separation as machine-checkable
evidence for later independent audit handling; it does not re-audit
the parent and does not promote status.

---

## 0. Why this companion exists

The parent's most recent archived audit snapshot
(`audit_date 2026-05-11T17:53`, codex-gpt-5.5,
conditional verdict, against `note_hash b44ed058...`) recorded:

```text
notes_for_re_audit_if_any: missing_dependency_edge: wire the named
hw=1 triplet, induced C3[111], S3 degeneracy, and staggered-Dirac
gate surfaces as explicit dependencies; if the intended claim is only
abstract finite C3 algebra, split that into a dependency-free note and
keep this physical Ward-support row conditional.
```

That verdict's `chain_closure_explanation` reasoned:

```text
The finite C3 normal-form algebra closes, and the runner reports
PASS=51 FAIL=0, but the source and runner import dependency surfaces
for the hw=1 triplet, induced C3[111] cycle, prior S3 degeneracy,
and the staggered-Dirac realization gate while the ledger row has no
dependency edges. The canonical staggered-Dirac parent is an open gate
and several named dependency surfaces are not closed, so the physical
support claim cannot close from the current packet.
```

On 2026-05-12 the audit-bot nightly-repair commit
`7a214c3d90a4479cb0b41fe1be46b49ab8819280`
(`audit: nightly repair and pipeline refresh (automated) [skip ci]`)
appended a new `Audit dependency repair links` section at the end of
the parent note that exactly addresses this repair target by listing
four named one-hop dependency references — the same four dependency
surfaces named in the prior conditional verdict. This
edit moved the parent's `note_hash` from `b44ed058...` to
`d92f91a2...` and the audit pipeline accordingly archived the prior
conditional verdict and reset the row to `unaudited`.

That same nightly-repair commit also wrote the corresponding four
explicit dependency edges into the parent's ledger row, so the row
now reads

```text
deps = [
  staggered_dirac_realization_gate_note_2026-05-03,
  three_generation_observable_theorem_note,
  quark_generation_equivariant_ward_degeneracy_no_go_note_2026-04-28,
  s3_taste_cube_decomposition_note,
]
```

i.e., the prior conditional verdict's `missing_dependency_edge`
repair target is mechanically discharged in the audit graph.

The honest-stop question is then exactly:

> Did that 2026-05-12 edit modify the parent's load-bearing proof
> content (the exact C3-equivariant Hermitian normal-form algebra
> in Sections 1-9, the `Hypothesis set used` paragraph, and the
> 51-check runner) — or only append a graph-bookkeeping section
> recording the named dependency edges that the prior conditional
> verdict explicitly requested?

This companion records that the second reading is the one supported
by a line-by-line diff of the only intervening commit. The parent's
runner outputs are identical to the prior snapshot
(`TOTAL: PASS=51, FAIL=0`), the parent's Sections 1-9 and the
`Hypothesis set used` paragraph are byte-for-byte unchanged, and
the appended `Audit dependency repair links` section is exactly the
missing-dependency-edge bookkeeping the prior audit explicitly
requested.

This companion is therefore audit-friendly evidence that the prior
conditional evidence surface is unchanged across the 2026-05-12
dependency-edge bookkeeping append. It is not a re-audit and does
not promote status; it documents the substance-vs-bookkeeping
surface in machine-checkable form for later independent audit
handling.

---

## 1. Parent recap and prior audit grade

The parent
[`QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md`](QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md)
is a Lane 3 block-06 bounded support/boundary theorem that identifies
the smallest local source/readout primitive that can split the `S3`
doublet found in the retained Ward-degeneracy no-go on the retained
`hw=1` generation triplet.

The parent's Section 6 theorem reads:

> **Theorem (`C3`-oriented Ward splitter support/boundary).** On the
> retained `hw=1` generation triplet, the Hermitian Ward
> endomorphisms that commute with the retained induced `C3[111]`
> cycle are exactly
>
> ```text
> W(a,b,c) = a I + b (C + C^2) + c (C - C^2)/(i sqrt(3)),
> ```
>
> with `a,b,c in R`. ... Therefore oriented `C3` is an exact local
> splitter primitive for the 3C residual, but not a retained
> non-top quark mass derivation.

The runner
[`scripts/frontier_quark_c3_oriented_ward_splitter_support.py`](../scripts/frontier_quark_c3_oriented_ward_splitter_support.py)
mechanically verifies this via 51 finite-algebra checks: cycle
identity verification, Hermitian C3-invariant normal form,
diagonalization in the Fourier basis, eigenvalue strata, splitting
under nonzero `c`, reflection-odd transformation of the `(C - C^2)`
channel, diagonal-generation-readout scalar collapse, and a set of
guardrail checks that no observed quark masses / fitted Yukawa
entries / CKM data / nearest-rational selection enters the proof.

The earlier clean archived snapshot (codex-current-fresh-context,
high confidence, archived 2026-05-03T13:40 against `note_hash
7a27ede9`) recorded `PASS=51 FAIL=0` with a class-A load-bearing
step (oriented C3 supplies exact local splitter primitive on the S3
doublet).

The subsequent conditional archived snapshot
(codex-audit-loop, high confidence, archived 2026-05-12T08:18,
against `note_hash b44ed058`, runner_hash
`b3e8581f8e63aa58c4fdf55393ebf876ee68c7b19e22f8fdd6f1e5800813ceda`)
recorded the missing-dependency-edge repair
target quoted in §0 above, while keeping `PASS=51 FAIL=0` and
explicitly acknowledging that the finite C3 normal-form algebra
closes.

That second snapshot's `verdict_rationale` summarized:

```text
Claim boundary until fixed: the abstract Hermitian C3 normal form
and generic Fourier-channel splitting are usable finite algebra;
it is not retained support for physical quark-mass Ward channels
or a closed source/readout primitive.
```

---

## 2. Invalidation cause

The audit pipeline does not currently record an explicit
`invalidation_reason` field on the second `previous_audits` entry
because the invalidation was driven by the source-side note_hash
drift path in `docs/audit/scripts/seed_audit_ledger.py` (the
`prior.get("note_hash") != node["note_hash"]` branch at line 488)
rather than by the dependency/criticality detector in
`docs/audit/scripts/invalidate_stale_audits.py` (which records its
reasons in `previous_audits[i]["invalidation_reason"]`).

The driving cause is therefore note_hash drift:

```text
note_hash_drift: b44ed058...  ->  d92f91a2...
```

i.e., the parent's source-note SHA-256 has changed since the prior
audit was recorded, so the audit pipeline conservatively archived
the prior verdict to `previous_audits` and reset the row to
`unaudited`, even though that single intervening edit is the
audit-bot nightly-repair commit that appended an `Audit dependency
repair links` section recording the four named one-hop dependency
edges that the prior conditional verdict explicitly requested.

Git history of the file's content (filtered to commits whose blob
SHA changed for this file on `origin/main`) is exactly two distinct
content states:

```text
5fd2c65a7 audit: capture yt pr230 lsp readout runner output
          blob 9a6f90ae0 -> file content sha256 b44ed058...
7a214c3d9 audit: nightly repair and pipeline refresh (automated) [skip ci]
          blob 752cb3230 -> file content sha256 d92f91a2...
```

Only the second commit is post-snapshot; it carries the
`b44ed058 -> d92f91a2` note_hash drift on this file.

The runner file itself is unchanged: the runner's current SHA-256
is `b3e8581f8e63aa58c4fdf55393ebf876ee68c7b19e22f8fdd6f1e5800813ceda`,
which exactly matches the `runner_hash` field recorded in the
`audit_state_snapshot` of the prior conditional snapshot.

---

## 3. Substance-vs-bookkeeping separation

The narrow auditable observation in this companion is:

**(C1) The parent's load-bearing substantive content was not modified
by the 2026-05-12 nightly-repair commit.** The only line-level diff
on the parent note since the last conditional snapshot is
a strictly-additive append at the end of file:

```text
@@ -195,3 +195,12 @@ Canonical parent note: ...
 - `GENERATION_AXIOM_BOUNDARY_NOTE.md` (preserved)

 Therefore `claim_type: bounded_theorem` until that gate closes. ...
+
+## Audit dependency repair links
+
+This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.
+
+- [staggered_dirac_realization_gate_note_2026-05-03](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
+- [three_generation_observable_theorem_note](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
+- [quark_generation_equivariant_ward_degeneracy_no_go_note_2026-04-28](QUARK_GENERATION_EQUIVARIANT_WARD_DEGENERACY_NO_GO_NOTE_2026-04-28.md)
+- [s3_taste_cube_decomposition_note](S3_TASTE_CUBE_DECOMPOSITION_NOTE.md)
```

In words, the only change is:

1. a new section heading `## Audit dependency repair links`;
2. one prose sentence stating that this is graph bookkeeping and does
   not promote the note or change audit scope;
3. four backticked dependency references — exactly the four named
   one-hop dependency surfaces from the prior conditional verdict.

No Section 1 (Question) text, no Section 2 (Minimal Premise Set)
text, no Section 3 (Exact C3-Equivariant Hermitian Normal Form),
no Section 4 (Spectrum), no Section 5 (Diagonal Generation Readout
Boundary), no Section 6 (Theorem), no Section 7 (What This Adds),
no Section 8 (What Remains Open), no Section 9 (Verification), and
no `Hypothesis set used` paragraph text was modified.

The companion records this separation by:

1. Re-running the parent's runner on the current `origin/main` head
   and confirming the SUMMARY is unchanged with
   `TOTAL: PASS=51, FAIL=0` (Block 1 of this companion's runner);
2. Confirming via SHA-256 equality that the parent runner
   [`scripts/frontier_quark_c3_oriented_ward_splitter_support.py`](../scripts/frontier_quark_c3_oriented_ward_splitter_support.py)
   is byte-for-byte unchanged across the prior conditional snapshot's
   recorded `runner_hash` field and the current head
   (Block 2);
3. Confirming via static source-scan that the parent's load-bearing
   Sections 1-9 and the `Hypothesis set used` paragraph are
   byte-for-byte identical between the prior `b44ed058` snapshot
   and the current `d92f91a2` head, with the only diff confined to
   the appended `Audit dependency repair links` graph-bookkeeping
   section at end-of-file (Block 3);
4. Confirming via static source-scan that the appended section lists
   exactly the four named one-hop dependency surfaces requested by
   the prior conditional verdict (Block 4);
5. Re-verifying the exact C3-equivariant Hermitian normal-form
   spectrum independently: lambda_0 = a + 2b, lambda_+ = a - b + c,
   lambda_- = a - b - c (Block 5);
6. Re-verifying the doublet-splitting boundary: c != 0 and c != +/- 3b
   gives three distinct eigenvalues, c = 0 gives the E doublet
   degeneracy (Block 6);
7. Re-verifying the reflection-odd transformation of the splitter
   K_C3 = (C - C^2) / (i sqrt(3)) (Block 7);
8. Re-verifying the diagonal-generation-readout scalar collapse
   from C3 equivariance (Block 8);
9. No-claim gate preservation across runs: parent note continues
   to disclaim Yukawa-ratio derivation, absolute non-top quark
   mass scale, down-type 5/6 exponent, and up-type amplitude
   scalar law (Block 9).

These are static and dynamic facts about the parent's runner, note,
and git history; they do not depend on generated audit-status fields.

---

## 4. Substance-unchanged assertion

The parent's runner on the current `origin/main` head outputs

```text
TOTAL: PASS=51, FAIL=0
VERDICT: oriented C3 supplies an exact local splitter primitive,
but leaves the Lane 3 quark-mass Ward source/readout law open.
```

This matches the pass count recorded by both archived snapshots
(the earlier clean snapshot at note_hash `7a27ede9`,
runner_check_breakdown A=35 B=16 total=51; and the later conditional
snapshot at note_hash `b44ed058`, runner_check_breakdown A=41 B=10
total=51). The parent's
runner code is SHA-256-identical to the recorded `runner_hash` field
on the prior snapshot. The parent note's load-bearing Sections 1-9
and `Hypothesis set used` paragraph are byte-for-byte unchanged
across the only intervening note edit. Only the appended
`Audit dependency repair links` graph-bookkeeping section is new.

The substantive bounded support content of the parent is therefore
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
- assert that the parent's bounded support scope is the only
  correct reading;
- close the parent's open Lane 3 quark-mass Ward source/readout law
  (it remains open exactly as Section 8 states);
- close the staggered-Dirac realization gate that the parent depends
  on (it remains `open_gate` as the parent's `Hypothesis set used`
  paragraph states);
- weigh in on the parent's status against the parent's open or
  newer sibling notes;
- back-fill or rebut any prior auditor verdict, or set any audit
  status;
- assert that the prior conditional verdict's
  `missing_dependency_edge` repair target is now mechanically
  discharged — only that the appended `Audit dependency repair links`
  section nominally addresses it by listing the four named
  dependency surfaces; any audit verdict remains independent.

This companion's narrow auditable observation is exactly (C1) in §3.

---

## 6. Audit Handoff

Independent audit handling can decide whether and how to re-audit the
parent under the current `unaudited` state. The present companion
supplies:

- a line-by-line diff of the only intervening content-state change
  on `origin/main` since the last audited snapshot, showing the
  diff is a strictly-additive append of an `Audit dependency repair
  links` graph-bookkeeping section listing the four named one-hop
  dependency surfaces;
- a re-execution of the parent's runner on the current head, with
  the same `TOTAL: PASS=51, FAIL=0` summary used by both archived
  snapshots;
- a SHA-256 equality check showing the parent's runner code is
  byte-for-byte identical to the runner_hash recorded on the prior
  snapshot;
- a static source scan that confirms the parent's load-bearing
  Sections 1-9 and the `Hypothesis set used` paragraph are
  byte-for-byte unchanged across the edit;
- a small set of self-checks (Hermitian C3-equivariant normal form,
  Fourier-channel spectrum, doublet-splitting boundary, reflection-
  odd splitter, diagonal-readout scalar collapse, no-claim gate)
  that exercise the parent's substantive content directly.

If later independent audit handling treats the prior conditional
analysis of the parent as reusable under the current note_hash, this
companion records the evidence surface for that treatment. If later
handling re-audits from scratch under the present state, this
companion does not block that path; it only documents the parent's
substance-vs-bookkeeping surface across the dependency-edge append.

This companion's type is meta, with audit-companion scope. It is
not a status change.
