# DM Neutrino `K00` Bosonic Normalization: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
runner-checked algebraic content of
[`DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md`](DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md)
is invariant under the 2026-06-04 Record-axiom adoption in
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md). It is
not a new theorem claim, not a status promotion, and not an attempt to
perform re-audit work. If the audit pipeline seeds this file, it is a
meta companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that
authority.
**Companion target:** `dm_neutrino_k00_bosonic_normalization_theorem_note_2026-04-15`
(parent note `docs/DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md`).
**Primary companion runner:**
[`scripts/audit_companion_dm_neutrino_k00_bosonic_normalization_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_dm_neutrino_k00_bosonic_normalization_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_dm_neutrino_k00_bosonic_normalization_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_dm_neutrino_k00_bosonic_normalization_record_axiom_invariance_2026_06_04.txt)

---

## Why this companion exists

The parent narrow theorem
`dm_neutrino_k00_bosonic_normalization_theorem_note_2026-04-15` is a
*conditional* `bounded_theorem` whose prior audit verdict
(2026-05-05) was `audited_renaming` with class-F load-bearing step.
The prior verdict noted:

> The algebraic isospectrality check closes, but the bridge from
> isospectral bosonic response to the physical coefficient identity
> `K00 = 2 tau_+` is asserted rather than derived from the single
> axiom in the packet. The runner then hard-codes `tau_E = tau_T = 1/2`
> and `k00 = 2*tau_plus` rather than computing them from `Cl(3)` on
> `Z^3`.

The parent's own headline matches this: it is presented explicitly as
conditional on (a) the observable-principle premise (upstream
authority `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, currently
`audited_conditional`) and (b) the source-amplitude premise (upstream
authorities currently `unaudited`). The narrow runner-checked content
is `exact finite-dimensional matrix algebra` on the 3 x 3 heavy basis
and the 2 x 2 source row-sum block.

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per
[`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
section 6) changed the stable `minimal_axioms` premise-node note-hash
and so invalidated all prior audit snapshots that chained through that
premise node — including this row's `audited_renaming` snapshot, which
returned to `effective_status=unaudited`.

This companion records, for the audit lane, that the parent's
runner-checked algebraic content is **independent of the Record
axiom**. It uses only the Lattice and Quantum axiom content (the
`Cl(3)` local algebra and the `Z^3` cubic lattice, both preserved
without change across the 2026-05-20 and 2026-06-04 memos), plus
explicit matrix-algebra identities on small numerical matrices.
Adopting the Record axiom adds a strictly additive scalar
record-readout statement — `I(R_1 sqcup R_2) = I(R_1) + I(R_2)` —
which is neither used nor invoked anywhere in this packet's algebra,
and which the 2026-06-04 memo itself explicitly excludes from the
log-det / source/action / observable-bridge scope that the parent's
conditional `observable-principle premise` separately supplies.

This companion is therefore audit-friendly evidence that the prior
`audited_renaming` verdict's substantive content survives the
axiom-set change unchanged: the algebraic surface still closes
conditionally on the same two upstream premises named by the prior
verdict, and the Record-axiom adoption neither closes those gaps nor
introduces new ones. It is not a re-audit and does not promote
status; it documents the load-bearing-step dependency surface in
machine-checkable form so the audit lane can decide whether to honor
or re-test the prior conditional verdict on the new premise hash.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the K00 algebraic surface.** The
parent's load-bearing algebraic content — the four runner parts —
depends only on:

1. the rank-one projector identity `F00 = J3/3` on a 3 x 3 real
   matrix and its target-trace pairing
   `K00 = Tr(H F00) = (A + 4b + 2c + 2d)/3`
   (Part 1 of the parent);
2. isospectrality of `F00` with the scaled source row-sum generator
   `(1/2) J2` on a 2 x 2 real matrix (both rank-one projectors with
   spectrum `{1}` plus zeros; Part 2 of the parent);
3. identical exact bosonic scalar-baseline `log|det|` response of
   `F00` and `(1/2) J2` evaluated on a 1 x 1 / 2 x 2 / 3 x 3 free
   determinant (Part 3 of the parent);
4. linear arithmetic on hard-coded source amplitudes
   `tau_E = tau_T = 1/2` yielding `tau_+ = 1` and `K00 = 2`
   (Part 4 of the parent).

Items 1-4 use only:

- the Lattice axiom (the `Z^3` lattice / index structure the
  parent inherits via the `Cl(3)` on `Z^3` framework sentence);
- the Quantum axiom (one-qubit / `Cl(3,0)` local algebra; the
  finite-dimensional matrix algebra on small index-counted blocks);
- standard finite-dimensional linear algebra (rank-one projectors,
  eigenvalue decomposition, the determinant identity
  `log|det(M + tN)| - log|det M|` on numerical matrices).

None of items 1-4 invoke the Record axiom's additive scalar
record-readout content. The conditional load-bearing bridges that
the prior `audited_renaming` verdict explicitly named (the
observable-principle premise and the source-amplitude premise) are
themselves NOT supplied by the Record axiom either: the 2026-06-04
memo says explicitly that the Record axiom "does not supply [...] a
log-det structure, [...] source/action identification, [...] or
arbitrary observable identification". So the conditional premise
structure named by the prior verdict is unchanged under the axiom-set
adoption.

**(C1) is the only auditable companion observation.** The two
conditional load-bearing premises (observable-principle premise;
source-amplitude premise) remain conditional load-bearing premises
exactly as in the parent note and the prior audit verdict. This
companion does **not**:

- close or weaken either of those upstream conditional premises;
- re-audit `dm_neutrino_k00_bosonic_normalization_theorem_note_2026-04-15`
  or any other ledger row;
- introduce a new minimal-axiom statement (the
  explicit-owner-approved axiom set is fixed at
  `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs;
- assert anything about Record-axiom content or its scope;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1) is sufficient evidence to
re-honor the previous `audited_renaming` verdict on the new premise
hash or whether a fresh per-site audit is warranted.

---

## The Record axiom is not used by the load-bearing step

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` section "Record")
says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The 2026-06-04 memo's scope statement is explicit about what the
Record axiom does *not* supply:

> This axiom supplies only additive scalar record readout. It does not
> supply a rule for record production, persistence,
> measurement/decoherence, Born weights, P2/modulus/phase-blindness,
> log-det structure, time arrow, system composition, normalization/scale,
> source/action identification, `AC_phi_lambda`, theta, or arbitrary
> observable identification.

The parent's runner-checked algebraic content defines no record
surface, asks no question about scalar record additivity, and writes
no record functional `I(.)`. It computes:

- A trace of `H` against a 3 x 3 rank-one projector `F00`
  (Part 1: Frobenius pairing identity on a numerical matrix).
- An eigenvalue spectrum check of two small rank-one projectors
  (Part 2: standard `eigvalsh` of `J3/3` and `(1/2) J2`).
- An equality of two scalar log-determinant scans
  `log|det(m I + s F00)|` versus `log|det(m I + s F_row)|`
  on numerical matrices (Part 3: a numerical equality of two
  determinant expressions; the log-det machinery itself is the
  parent's conditional `observable-principle premise`, **not**
  the Record axiom).
- A linear arithmetic step `K00 = 2 tau_+` with
  `tau_+ = tau_E + tau_T = 1/2 + 1/2 = 1` (Part 4: arithmetic on
  hard-coded source amplitudes; the source-amplitude values
  themselves are the parent's conditional `source-amplitude premise`,
  **not** the Record axiom).

The Record axiom adds an additive scalar record functional and
nothing else. It does not modify (and is not modified by) the
Lattice index structure, the Quantum local algebra, the
finite-dimensional matrix algebra of `F00` versus `(1/2) J2`, the
numerical eigenvalue check, the numerical log-det response check, or
the linear-arithmetic step on `tau_E`, `tau_T`. So the algebraic
content of all four parts is invariant under the axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every runner-checked arithmetic / algebraic identity of the parent
passes using only Lattice + Quantum content plus standard
finite-dimensional matrix algebra, and a "Record-axiom counterfactual"
block confirms that the runner's numeric outputs are unchanged
whether or not a Record-axiom statement is appended.

---

## Companion runner block plan

`scripts/audit_companion_dm_neutrino_k00_bosonic_normalization_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the parent's runner-checked
algebraic content. Each block runs as an independent
numeric/algebraic check; nothing is hard-coded against an expected
target value beyond standard finite-dimensional linear algebra. The
runner reports `PASS` / `FAIL` per check; the cached output records
the run.

- **Block 1 — `K00` target formula.** Verifies the closed-form
  identity `K00 = (A + 4b + 2c + 2d)/3 = Tr(H F00)` with
  `F00 = J3/3`, independent of `(delta, rho, gamma)`. Two random
  numerical fills of the breaking triplet are checked; the diagonal
  entry, the Frobenius pairing, and the closed-form polynomial all
  agree to machine precision.
- **Block 2 — Rank-one projector spectrum.** Verifies
  `eigvalsh(F00) = {0, 0, 1}` and `eigvalsh(FROW) = {0, 1}` with
  `FROW = (1/2) J2`. Both are rank-one projectors with one nonzero
  eigenvalue `+1`.
- **Block 3 — Isospectrality of `F00` and `(1/2) J2`.** Verifies the
  nonzero spectra agree as multisets (both equal `{+1}`).
- **Block 4 — Identical bosonic scalar-baseline response.** Evaluates
  the scan `log|det(m I + s X)| - n log|m|` for `X in {F00, FROW}`
  on 8 source values `s in [-0.35, 0.35]` at `m = 1.73`. Verifies
  identical numeric output to machine precision for all 8 samples.
- **Block 5 — Coefficient law `K00 = 2 tau_+`.** Verifies the
  factor-of-2 arithmetic between the source-side `J2` amplitude and
  the scaled `(1/2) J2` generator: `K00 = 2 tau_+` (no Record-axiom
  content; this is the parent's `observable-principle premise`,
  imported as a conditional load-bearing input).
- **Block 6 — Source amplitudes and `K00 = 2`.** Verifies the
  arithmetic `tau_+ = tau_E + tau_T = 1/2 + 1/2 = 1`, so
  `K00 = 2 * 1 = 2` (no Record-axiom content; the source amplitudes
  are the parent's `source-amplitude premise`, imported as a
  conditional load-bearing input).
- **Block 7 — `K00` is `(delta, rho, gamma)`-independent.**
  Verifies that two random fills of the breaking triplet with
  identical aligned core `(A, b, c, d)` give identical
  `K00 = (A + 4b + 2c + 2d) / 3`.
- **Block 8 — Mass-basis kernel reconstruction.** Builds
  `H = H_core + B(delta, rho, gamma)` from a random parameter fill,
  applies the `UZ3 R` mass-basis transform from the parent runner,
  and verifies the resulting heavy-basis `[0,0]` entry equals the
  closed-form `K00` polynomial.
- **Block 9 — Static-source scan of parent note's load-bearing
  section.** Verifies that the auditable algebraic core does not
  invoke a record functional `I(.)`, a record additivity statement,
  a record collection, or a Record-axiom citation. Enumerates the
  phrase set
  `{"I(R_1", "I(R)", "scalar record", "record functional",
  "record-readout", "additive record", "additive scalar record",
  "MINIMAL_AXIOMS_2026-06-04"}`
  over the load-bearing section of the parent note and confirms zero
  matches inside the auditable core.
- **Block 10 — Record-axiom counterfactual.** Re-runs Blocks 1, 4, 5,
  and 6 inside an explicit "Record axiom is asserted" outer scope and
  an explicit "Record axiom is not asserted" outer scope; verifies
  identical numeric output in both runs. The counterfactual is a
  tautology at the calculation level (no Record-axiom content enters
  any algebraic step), which is precisely the substantive content of
  (C1).
- **Block 11 — Quantum/Lattice content preservation across memos.**
  Verifies the historical `MINIMAL_AXIOMS_2026-05-20.md` content
  (qubit local algebra; `Z^3` lattice) is preserved verbatim in
  `MINIMAL_AXIOMS_2026-06-04.md` under the explicit names "Quantum"
  and "Lattice", and that the 2026-06-04 memo's own Record-axiom
  scope statement explicitly excludes log-det / source/action
  bridges.
- **Block 12 — Cross-check on hard-coded numerical inputs.** Verifies
  the parent's three hard-coded numerical inputs (`tau_E = 1/2`,
  `tau_T = 1/2`, `mass = 1.73`) appear in the parent runner exactly
  as cited and that none of them depend on the Record axiom.

Total: 12 blocks. The exact PASS / FAIL count is recorded in the
SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline
derives `effective_status`), no status field changes are implied by
this PR. The audit lane decides whether to re-honor the prior
`audited_renaming` verdict on the new premise hash; this companion
only supplies machine-checkable evidence on whether the new Record
axiom disturbs the parent's runner-checked algebraic content.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
conditional `K00 = 2` output. Each downstream claim must be examined
independently against the new axiom-set premise hash. The other rows
recently axiom-invalidated under the same hash change are out of
scope of this companion; they are listed in the audit queue's
`axiom_premise_changed` cohort and should be examined separately as
the audit lane reaches them.

The two conditional load-bearing upstream premises that the parent's
2026-05-16 honest demotion and the 2026-05-05 audit verdict named
(observable-principle premise; source-amplitude premise) remain
conditional load-bearing premises after this companion lands and
after the Record-axiom adoption. Closing those upstream gaps remains
out of scope of this companion exactly as it is out of scope of the
parent's runner-checked content.

---

## Audit-ordering and integration

This companion does not migrate the parent's `Cl(3)` on `Z^3`
framework-sentence citations to `MINIMAL_AXIOMS_2026-06-04.md`. Both
the 2026-05-20 and 2026-06-04 memos preserve the Quantum (`Cl(3,0)` /
qubit) and Lattice (`Z^3`) content unchanged; the 2026-06-04 memo
cites the 2026-05-20 memo as the "local-algebra authority and
historical source for the prior two-axiom wording." A separate
citation-migration PR (if desired) can refresh the parent note's
`Source` column; this companion is independent of that text update
and is content-only.

This companion's load-bearing-step invariance observation depends only
on the Quantum and Lattice content being preserved across the two
memos — verified in Block 11 — and on the Record axiom adding a
strictly additive non-overlapping statement — confirmed by direct
reading of `MINIMAL_AXIOMS_2026-06-04.md` section "Record".

---

## References

- Parent note:
  [`DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md`](DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md)
- Parent runner:
  `scripts/frontier_dm_neutrino_k00_bosonic_normalization_theorem.py`
- Prior audit-verdict snapshot:
  `docs/audit/data/audit_ledger.json` row
  `dm_neutrino_k00_bosonic_normalization_theorem_note_2026-04-15`,
  `previous_audits[-1]` (`audited_renaming`, `positive_theorem`,
  class F, `codex-cli-gpt-5.5`, 2026-05-05; subsequently archived
  under the `minimal_axioms` hash bump)
- Upstream conditional authorities (named by the parent and by the
  prior audit verdict, unchanged by this companion):
  - [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
    (currently `audited_conditional`)
  - [`DM_NEUTRINO_WEAK_EVEN_SWAP_REDUCTION_THEOREM_NOTE_2026-04-15.md`](DM_NEUTRINO_WEAK_EVEN_SWAP_REDUCTION_THEOREM_NOTE_2026-04-15.md)
    (currently `unaudited`)
  - [`DM_NEUTRINO_TRIPLET_CHARACTER_SOURCE_THEOREM_NOTE_2026-04-15.md`](DM_NEUTRINO_TRIPLET_CHARACTER_SOURCE_THEOREM_NOTE_2026-04-15.md)
    (currently `unaudited`)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for the
  Quantum / Lattice content the parent uses):
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
- Sister-row companion (the template for this PR):
  [`YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)
