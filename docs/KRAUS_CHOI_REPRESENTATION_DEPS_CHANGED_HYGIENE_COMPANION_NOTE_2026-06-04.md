# Kraus-Choi Representation on Qubit Lattice: Deps-Changed Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / deps-changed hygiene evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
parent
[`KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
does not load-bear on the *Record-axiom content* of its renamed dep
`minimal_axioms`. The new `minimal_axioms` premise node packages
Lattice + Quantum + Record together, but the parent's load-bearing
chain uses only the Lattice + Quantum content (per-site
`A_x ~= M_2(C)` and the `Z^3` finite-region indexing). The new dep
edge from the deps-changed rewire is therefore not load-bearing on
Record content. This is not a new theorem claim, not a status
promotion, and not an attempt to perform re-audit work. If the audit
pipeline seeds this file, it is a meta companion row; the audit lane
still sets `audit_status`, and the pipeline-derived `effective_status`
remains downstream of that authority.
**Companion target:** `kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20`
(parent note
[`docs/KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)).
**Primary runner:**
[`scripts/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.py`](../scripts/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.txt)

---

## 0. Why this companion exists

The parent narrow positive theorem
`kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20`
was previously `audited_clean` twice in the ledger:

- 2026-05-22 (archived 2026-05-23) — first clean verdict, chain
  closure explained by per-site `M_2(C)` plus standard finite-
  dimensional Kraus/Choi.
- 2026-05-23 (archived 2026-06-04) — re-affirmed `audited_clean`
  against the prior `minimal_axioms_2026-05-20` premise hash
  `1d36a556`.

The second verdict was archived with invalidation reason

```text
axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8
```

reflecting the 2026-06-04 axiom adoption from
`MINIMAL_AXIOMS_2026-05-20.md` to `MINIMAL_AXIOMS_2026-06-04.md`
(Lattice + Quantum + Record). The current effective state is

```text
audit_status        = unaudited
effective_status    = unaudited
effective_status_reason = awaiting_audit
deps                = ["minimal_axioms"]
intrinsic_status    = unaudited
load_bearing_score  = 5.822
claim_type          = positive_theorem
```

with the active invalidation cause recorded as the deps-changed event

```text
deps_changed:dep_added:minimal_axioms|dep_removed:minimal_axioms_2026-05-20
```

This is a stable-premise-node renaming (`minimal_axioms_2026-05-20`
-> `minimal_axioms`) that coincides with the Record-axiom adoption
because the premise node was simultaneously rewired to the new memo.
The honest-stop question is then exactly:

> Does the parent's substantive claim load-bear on the *Record-axiom
> content* of the renamed `minimal_axioms` premise node, or only on
> the Lattice + Quantum content that the prior premise node already
> supplied?

This companion records that the second reading is the one supported
by the parent's note and the prior auditor verdicts. The parent's
load-bearing step is the identification

> `A_Lambda = (tensor)_{x in Lambda} M_2(C) ~= M_d(C)` for `d = 2^|Lambda|`,

which uses only per-site `M_2(C)` (Quantum) and finite `Z^3` regions
(Lattice) — no Record-axiom content enters anywhere in the load-
bearing chain. Steps 1-3 of the parent are pure standard finite-
dimensional Kraus/Choi C\*-algebra theory applied to that matrix
algebra; Step 4 is an explicit downward-pointing consistency
statement to the existing record lane (not an upstream input).

This companion is therefore audit-friendly evidence that the prior
clean verdicts' substantive content survives the deps-changed
rewire. It is not a re-audit and does not promote status; it
documents the load-bearing-step dependency surface in machine-
checkable form so the audit lane can decide whether the rewire
needs fresh per-claim review.

---

## 1. Parent recap and prior audit grades

The parent
[`KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
states a narrow application theorem:

> For finite `Lambda subset Z^3`, the qubit-lattice operator algebra
> is `A_Lambda = (tensor)_{x in Lambda} M_2(C) ~= M_d(C)` for
> `d = 2^|Lambda|`. A linear map `Phi : A_Lambda -> A_Lambda` is CP
> iff it has an operator-sum (Kraus) representation
> `Phi(X) = sum_r K_r X K_r^dag` with `K_r in A_Lambda`; it is TP iff
> `sum_r K_r^dag K_r = I`; and it is CP iff the Choi matrix
> `C_Phi = (I (tensor) Phi)(|Omega><Omega|)` is positive
> semidefinite.

The note explicitly admits Kraus 1971 and Choi 1975 as standard-math
imports and explicitly scopes itself to finite regions: thermodynamic-
limit channel claims and specific record-formation dynamics
identifications are placed in "What this does not close".

Both prior clean snapshots reached the same chain-closure judgement:

> The cited axiom memo supplies the per-site `M_2(C)` algebra and
> finite-region tensor-product structure, and the source note
> explicitly admits the standard finite-dimensional Kraus and Choi
> theorems. The audited claim is only the finite-region application,
> not an infinite-volume channel theorem or a derivation of record
> dynamics.

with explicit "thermodynamic-limit and record-dynamics claims are
explicitly excluded, so they do not create an open dependency for
this narrow claim" language in the first verdict's rationale.

That is, both clean verdicts had already separated the parent's
load-bearing surface (per-site `M_2(C)` + finite `Lambda` + standard
Kraus/Choi) from the parent's downward-pointing consistency
discussion of the record lane.

---

## 2. Invalidation cause

The active invalidation reason on the current ledger snapshot is

```text
deps_changed:dep_added:minimal_axioms|dep_removed:minimal_axioms_2026-05-20
```

This event is a stable-premise-node renaming: the dep edge formerly
pointing at `minimal_axioms_2026-05-20` now points at the stable
`minimal_axioms` premise node. The underlying mathematical content
supplied by that node — per-site `A_x ~= M_2(C)` (Quantum) and the
`Z^3` lattice with finite-region indexing (Lattice) — is preserved
across the rewire. The 2026-06-04 axiom memo
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) names
those two as Quantum and Lattice and adds a third axiom, Record:

> When a finite record-readout surface is specified, its scalar
> record functional is additive over disjoint record collections:
> `I(R_1 sqcup R_2) = I(R_1) + I(R_2)` with `I(empty) = 0` after
> an explicit additive-baseline convention.

The Record axiom adds an additive scalar record-readout statement;
it does not modify the per-site qubit algebra, the `Z^3` lattice,
finite-region tensor-product structure, or any standard finite-
dimensional matrix-algebra content.

The invalidation is therefore a dep-graph rewiring event rather than
a content change to the per-site algebra. The auditor lane decides
whether and how to re-honor the prior clean treatment under the new
dep wiring; this companion only provides evidence on whether the
rewire disturbs the parent's load-bearing chain.

The companion is *not* an attempt to assert that the rewire is
content-free in general. It is restricted to the narrow observation
that, for this specific parent, the new dep edge to `minimal_axioms`
does not pull in Record-axiom content as a load-bearing input.

---

## 3. Non-load-bearing assertion

The narrow auditable observation in this companion is:

**(C1) The parent's load-bearing chain uses zero Record-axiom
content.** The new dep edge to `minimal_axioms` is satisfied entirely
by Lattice + Quantum content (per-site `M_2(C)` and finite `Z^3`
regions), which is exactly what the parent's load-bearing step
"Step 3 — Application to the qubit-lattice substrate" requires. The
Record axiom is neither cited nor used in any step of the parent's
Kraus/Choi argument.

The parent's load-bearing chain decomposes as:

1. **Per-site Quantum content**: `A_x ~= M_2(C)` for each `x`
   (Quantum axiom).
2. **Lattice content**: `Lambda subset Z^3` finite, so
   `|Lambda| < infty` (Lattice axiom).
3. **Standard finite-dim tensor algebra**:
   `A_Lambda = (tensor)_{x in Lambda} M_2(C) ~= M_d(C)` with
   `d = 2^|Lambda|` (standard finite-dimensional matrix-algebra
   theory; no axiom content).
4. **Standard Kraus 1971 representation theorem** on `M_d(C)`
   (admitted import; no axiom content).
5. **Standard Choi 1975 CP characterization theorem** on `M_d(C)`
   (admitted import; no axiom content).
6. **Application step**: hypotheses of (4) and (5) are satisfied
   on `A_Lambda` by (3), so the standard theorems apply directly to
   any CP / CPTP linear map `Phi : A_Lambda -> A_Lambda`.

The Record axiom — additive scalar record-readout functional `I(.)`
on disjoint record collections — does not appear in any of steps
1-6. The parent's chain neither defines a record surface, asks any
question about scalar record additivity, nor writes a record
functional `I(.)`. The Record axiom is a strictly additive,
non-overlapping, downstream-facing scalar-additivity statement; the
finite-dimensional matrix algebra and the Kraus/Choi theorems do
not consume it.

The parent's Section 4 ("Consistency with the framework's record
lane") is a downward-pointing pointer from the proven finite-region
representation theorem to the framework's existing record lane that
plans to *use* the representation downstream. It is not an upstream
input. The clean verdicts' rationales explicitly noted this
direction (record-dynamics claims are explicitly excluded), and the
parent's own "What this does not close" section disavows any
upstream record-axiom dependency.

This companion records this separation by:

1. **Block 1**: Static source scan of the parent note — counts
   Record-axiom usage tokens
   (`I(R_1`, `I(R)`, `scalar record`, `record functional`,
   `record-readout`, `additive record`, `additive scalar record`,
   `Record axiom`, `MINIMAL_AXIOMS_2026-06-04`) in the
   load-bearing surface (Honest scope, Claim, Setup, Step 1, Step 2,
   Step 3, Admitted inputs sections) and verifies zero hits.
   Record mentions in the parent's pointer / "what this does not
   close" / consistency-with-record-lane sections are flagged as
   non-load-bearing pointers.
2. **Block 2**: Kraus operator-sum complete-positivity verification
   on small finite-region algebras — verifies the standard Kraus
   `Phi(X) = sum_r K_r X K_r^dag` map is CP and is TP iff
   `sum_r K_r^dag K_r = I`. Pure standard matrix algebra; no axiom
   content.
3. **Block 3**: Choi matrix positive-semidefiniteness verification
   on small finite-region algebras — verifies the Choi matrix
   `C_Phi = (I (tensor) Phi)(|Omega><Omega|)` is positive
   semidefinite for CP `Phi` and exhibits a non-CP counter-example
   with negative Choi eigenvalue. Pure standard matrix algebra.
4. **Block 4**: Counterfactual (Record axiom asserted vs not) —
   re-runs Blocks 2-3 inside an explicit "Record axiom asserted"
   outer scope and an explicit "Record axiom not asserted" outer
   scope, verifying that the load-bearing conclusions (Kraus
   operator-sum CP and Choi-positivity CP characterizations) are
   identical in both runs. The counterfactual is a tautology at the
   algebra level (no Record-axiom content enters the matrix-algebra
   or Kraus/Choi steps).
5. **Block 5**: Quantum / Lattice content preservation across memos
   — verifies that `MINIMAL_AXIOMS_2026-05-20.md`'s qubit-local-
   algebra and `Z^3`-lattice content is preserved in
   `MINIMAL_AXIOMS_2026-06-04.md` under the explicit names Quantum
   and Lattice; verifies that the new Record axiom is a third,
   additive, non-overlapping statement.
6. **Block 6**: Hypothesis-set parity check — re-derives the
   parent's load-bearing matrix-algebra steps (per-site qubit,
   finite tensor product, `M_d(C)` identification, Kraus, Choi)
   without any reference to the Record axiom, confirming that the
   parent's premise set is strictly the Lattice + Quantum subset of
   `{Lattice, Quantum, Record}` and is unchanged across the
   2026-05-20 -> 2026-06-04 axiom-set update.
7. **Block 7**: Standard Kraus / Choi import-content invariance
   under the dep-edge rewire — verifies that the standard Kraus
   1971 and Choi 1975 theorems quoted in the parent are
   axiom-set-independent finite-dimensional C\*-algebra content;
   their hypotheses (`M_d(C)`, finite `d`) are met by Quantum +
   Lattice; they make no reference to record additivity.
8. **Block 8**: Finite-region tensor-product structure invariance
   under the dep-edge rewire — verifies that `A_Lambda` is
   isomorphic to `M_d(C)` with `d = 2^|Lambda|` for
   `|Lambda| in {1, 2, 3, 4}` using direct construction from
   per-site `M_2(C)`; the isomorphism uses no Record content.
9. **Block 9**: Choi-Jamiolkowski isomorphism reproduction — re-
   verifies the explicit Choi map / inverse map identity
   `Phi(X) = Tr_1[(X^T (tensor) I) C_Phi]` on small CP test
   channels (depolarizing on 1 qubit, dephasing on 1 qubit, partial
   trace on 2 qubits); confirms the parent's load-bearing inverse
   formula and uses zero Record content.
10. **Block 10**: TP characterization `sum_r K_r^dag K_r = I` —
    verifies the trace-preservation condition for a unitary channel,
    a depolarizing channel, and a non-TP CP map (positive but not
    normalized) on 1-qubit and 2-qubit algebras; uses zero Record
    content.
11. **Block 11**: Parent-note pointer scan — verifies the
    parent's "Plain-text pointer references (NOT load-bearing
    deps)" subsection contains the three pointer notes
    (`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`,
    `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`,
    `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`) under the
    explicit "NOT load-bearing deps" label. This is a
    text-structure check that the parent itself flags its
    record-lane references as non-load-bearing.
12. **Block 12**: New deps-graph rewire static check — verifies on
    the working tree that `minimal_axioms_2026-05-20.md` and
    `MINIMAL_AXIOMS_2026-06-04.md` differ only by adding the
    Record axiom + ancillary metadata, and that the per-site
    `M_2(C)` plus `Z^3` content is preserved verbatim under the new
    Quantum / Lattice names; this confirms the rewire's content
    delta is restricted to Record-axiom addition.
13. **Block 13**: Companion's own runner has zero Record-axiom usage
    tokens in its load-bearing computational core — static self-
    scan of the runner script confirming the verifying algebra
    itself does not depend on Record content.

These are static and dynamic facts about the parent's note text
and the parent's load-bearing algebra; they do not depend on the
audit lane's decisions about the deps-changed event.

---

## 4. Counterfactual verification

The parent's standard Kraus/Choi application is mathematically
identical whether or not the Record axiom is asserted as an
upstream statement. The companion's Block 4 makes this explicit:

- In the "Record-axiom not asserted" scope, the parent's chain
  reads as the original 2026-05-22 / 2026-05-23 audited content:
  per-site `M_2(C)` (Quantum) + finite `Z^3` (Lattice) +
  standard finite-dim Kraus/Choi -> finite-region representation
  theorem holds.
- In the "Record-axiom asserted" scope, the additional Record
  axiom `I(R_1 sqcup R_2) = I(R_1) + I(R_2)` is available as an
  ambient axiom but is unused by any step of the chain; the
  parent's conclusion is identical.

The conclusion under both scopes is the same finite-region
representation theorem. The Record axiom is therefore not load-
bearing on the parent's chain, and its addition to the dep node
is not a content change to the parent's claim.

Companion Block 6 (hypothesis-set parity) re-derives the parent's
load-bearing steps explicitly without any Record-axiom reference
to confirm the strict-subset relation
`Premises(Parent) subseteq {Lattice, Quantum}` strictly
`subsetneq {Lattice, Quantum, Record}`.

---

## 5. What this companion does NOT do

This companion explicitly does **not**:

- claim a new theorem;
- promote the parent's `effective_status` or `audit_status`;
- modify the parent note text, the parent's runner (the parent
  has no runner), or the `minimal_axioms` premise node;
- assert that the Record axiom is content-free in general (it adds
  a strictly new additive scalar record statement; the assertion
  here is restricted to the parent's load-bearing chain);
- re-derive Kraus 1971 or Choi 1975 (cited as standard math);
- close the parent's open infinite-volume / thermodynamic-limit
  representation gap (the parent's "What this does not close"
  section preserves that gap);
- close the framework's record-formation derivation lane (a
  separate lane handled in
  [`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`](PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md)
  and downstream rows);
- back-fill or rebut any prior auditor verdict; the audit lane sets
  `audit_status` independently.

This companion's narrow auditable observation is exactly (C1) in §3.

---

## 6. Audit-lane handoff

The audit lane decides whether the deps-changed rewire on the
parent justifies a fresh per-claim re-audit, or whether the prior
clean verdicts (2026-05-22 / 2026-05-23) can be re-honored under
the new dep wiring on the basis that the new edge does not pull
in load-bearing Record-axiom content. The present companion
supplies:

- block-level static evidence that the parent's note text uses
  zero Record-axiom content in its load-bearing surface (Block 1);
- block-level dynamic evidence (Blocks 2-3, 8-10) that the
  standard finite-dim Kraus/Choi representation theorem holds on
  `A_Lambda ~= M_d(C)` using only per-site `M_2(C)` + finite `Z^3`
  + standard matrix algebra;
- a "Record axiom asserted vs not" counterfactual (Block 4)
  confirming identical conclusions in both scopes;
- Quantum / Lattice cross-memo preservation evidence (Block 5) and
  hypothesis-set parity (Block 6) confirming the strict-subset
  relation `Premises(Parent) subseteq {Lattice, Quantum}`;
- a static check that the standard Kraus / Choi imports are
  axiom-set-independent finite-dim C\*-algebra content (Block 7);
- a finite-region tensor-product reproduction (Block 8);
- a Choi-Jamiolkowski reproduction (Block 9);
- a TP-characterization reproduction (Block 10);
- a parent-note pointer scan (Block 11) confirming the parent
  itself flags its record-lane references as non-load-bearing;
- a deps-graph rewire content-delta check (Block 12) confirming
  the rewire's content delta is restricted to Record-axiom
  addition;
- a static self-scan of the companion runner (Block 13) confirming
  the runner's own load-bearing algebra is Record-axiom-free.

If the audit lane chooses to treat the prior clean verdicts as
re-usable under the deps-changed rewire on the basis that the
rewire does not change the parent's load-bearing chain, this
companion records the basis on which that decision can be made.
If the audit lane chooses to re-audit from scratch, this companion
does not block that path; it only documents the parent's load-
bearing dependency surface for the deps-changed event.

This companion's type is meta, with audit-companion scope. It is
not a status change.

---

## References

- Parent note:
  [`KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- Companion runner:
  [`scripts/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.py`](../scripts/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.py)
- Cached runner log:
  [`logs/runner-cache/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.txt)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-
  algebra content):
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
- Prior judicial verdicts (archived):
  `docs/audit/data/audit_ledger.json` row
  `kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20`,
  `previous_audits[0]` (2026-05-22, `audited_clean`,
  `chain_closes=true`, archived via
  `deps_changed:dep_added:minimal_axioms|dep_removed:minimal_axioms_2026-05-20`),
  `previous_audits[1]` (2026-05-23, `audited_clean`,
  `chain_closes=true`, archived 2026-06-04 via
  `axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`)
- Current ledger state: `audit_status=unaudited`,
  `effective_status=unaudited`,
  `effective_status_reason=awaiting_audit`,
  `load_bearing_score=5.822`, `claim_type=positive_theorem`,
  `deps=["minimal_axioms"]`
- Template companion (signed-gravity, deps-graph-event flavour):
  [`SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md`](SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md)
- Template companion (PMNS, axiom-premise flavour):
  [`PMNS_RIGHT_CONJUGACY_INVARIANT_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](PMNS_RIGHT_CONJUGACY_INVARIANT_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)
