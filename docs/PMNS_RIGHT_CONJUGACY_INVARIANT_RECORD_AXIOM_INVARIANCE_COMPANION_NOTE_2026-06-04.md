# PMNS Right-Conjugacy-Invariant No-Go: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing right-conjugacy-orbit argument in
[`PMNS_RIGHT_CONJUGACY_INVARIANT_NO_GO_NOTE.md`](PMNS_RIGHT_CONJUGACY_INVARIANT_NO_GO_NOTE.md)
is invariant under the 2026-06-04 Record-axiom adoption. It is not a
new theorem claim, not a status promotion, and not an attempt to
perform re-audit work. If the audit pipeline seeds this file, it is a
meta companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that
authority.
**Companion target:** `pmns_right_conjugacy_invariant_no_go_note`
(parent note `docs/PMNS_RIGHT_CONJUGACY_INVARIANT_NO_GO_NOTE.md`).
**Primary companion runner:**
[`scripts/audit_companion_pmns_right_conjugacy_invariant_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_pmns_right_conjugacy_invariant_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_pmns_right_conjugacy_invariant_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_pmns_right_conjugacy_invariant_record_axiom_invariance_2026_06_04.txt)

---

## Why this companion exists

The parent narrow no-go theorem
`pmns_right_conjugacy_invariant_no_go_note` was previously
audit-loop-touched on 2026-05-04 as `audited_clean` (`chain_closes=true`,
`auditor_confidence=high`) and re-touched 2026-05-05 as
`audited_conditional` (chain held the standard-algebra step but flagged
upstream-naming inputs). Both prior verdicts have since been archived;
the current effective state is `unaudited` (`effective_status_reason =
awaiting_audit`, `load_bearing_score = 10.19`,
`claim_type = no_go`).

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md`
section 6) changed the stable `minimal_axioms` premise-node note-hash
from `1d36a556` to `b8848fc8`. That same axiom adoption motivated
upstream Record-axiom-repair edits on the parent's named dependency
`observable_principle_from_axiom_note`. The current `unaudited` state
of the parent was not itself produced by an `axiom_premise_changed`
invalidation in the ledger snapshot, but the 2026-06-04 axiom change
is the most recent framework-level disturbance that an audit lane
reviewing this row will want to discharge before re-issuing a verdict.

This companion records, for the audit lane, that the parent's
load-bearing right-conjugacy-orbit argument is **independent of the
Record axiom**: it uses only standard finite-dimensional linear
algebra (Hermitian conjugation, right `U(3)` action, spectral data on
`K = Y^dag Y`) plus two upstream source rows whose content predates
and is independent of the Record axiom. Adopting the
Record axiom adds a strictly additive scalar record-readout
statement, which is neither used nor invoked anywhere in the
right-conjugacy-orbit no-go. The right-orbit invariance of `K`'s
spectral signature, the explicit parent-runner witnesses showing
`m_R(Y)` and `|(Y^dag Y)_{12}|` vary along the same right orbit, and
the conclusion that no right-conjugacy-invariant observable of `K`
can intrinsicize the admitted right-Gram route are all unchanged.

This companion is therefore audit-friendly evidence that the prior
clean/conditional verdicts' substantive content survives the
axiom-set change. It is not a re-audit and does not promote status;
it documents the load-bearing-step dependency surface in
machine-checkable form so the audit lane can decide whether the
2026-06-04 axiom change creates any disturbance to the parent's
algebraic claim.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the right-conjugacy-orbit no-go.**
The parent's load-bearing chain is:

1. Right `U(3)` action `Y -> Y U^dag` preserves the right Gram matrix
   `K = Y^dag Y` up to unitary conjugation `K -> U K U^dag` (Hermitian
   conjugation algebra; one line);
2. Any right-conjugacy-invariant observable `I(Y) = F(K)` with
   `F(U K U^dag) = F(K)` for all `U in U(3)` is therefore constant
   on every right orbit (definition of conjugacy invariance);
3. Spectral data of `K` (eigenvalues, traces of powers, determinant)
   are conjugacy invariants and therefore constant on the orbit;
4. Explicit parent-runner witness pairs exist where the admitted
   right-Gram selector datum `m_R(Y)` (parametrized via
   `right_score`) and the admitted sheet-fixing scalar
   `|(Y^dag Y)_{12}|` vary while the spectral signature of `K` is
   fixed (constructed in the parent runner from monomial and
   canonical `Y` parametrizations rotated by an explicit `U`);
5. Conclusion: no right-conjugacy-invariant observable of `K`
   can intrinsicize the admitted right-Gram route.

Steps 1-5 use only:

- Standard finite-dimensional matrix algebra over `C` (Hermitian
  conjugation, `U(3)` action, eigendecomposition of Hermitian
  matrices, polynomial invariants);
- The Lattice axiom (`Z^3` site set, supplying the indexing context
  in which `Y` is read as a `3 x 3` flavor / generation matrix) and
  the Quantum axiom (one-qubit / `Cl(3)` local algebra, supplying
  the algebraic ambient through the upstream source rows);
- Two upstream source rows cited in the
  parent's "Atlas and axiom inputs" list:
  `pmns_scalar_bridge_nonrealization_note` (Part 3 string-check)
  and `observable_principle_from_axiom_note` (Part 3 string-check).

None of items 1-5 use the Record axiom's additive scalar
record-readout content. Steps 1-2 are pure linear algebra. Step 3 is
spectral theory on a finite-dimensional Hermitian operator. Step 4 is
an explicit numeric construction from two parametrized matrix
families. Step 5 follows by direct contraposition. The two upstream
source rows in step 5 are cited only to record that the additive
scalar bank is *separately* ruled out for the admitted PMNS bridge:
the parent's load-bearing claim does not require either upstream
source row to be re-derived from the Record axiom; it requires
only that the upstream rows' content (additive scalar bank cannot
realize the missing PMNS bridge) is read out as a string match in
the parent runner's Part 3.

**(C1) is the only auditable companion observation.** This companion
does *not* re-derive the upstream narrow inputs, does *not* claim
that the upstream inputs are themselves Record-axiom-invariant, and
does *not* extend any audit verdict to downstream rows that consume
the parent no-go.

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs (the no-go remains exactly what the parent states: a no-go
  for right-conjugacy-invariant observables of `K`);
- assert anything about Record-axiom content or its scope;
- re-audit `pmns_right_conjugacy_invariant_no_go_note` or any other
  ledger row;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1) is sufficient evidence to re-honor
the previous judicial pattern (algebra-clean conditional on upstream
naming) or whether a fresh per-claim audit is warranted on the new
premise hash.

---

## The Record axiom is not used by the load-bearing chain

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing chain (Steps 1-5 above) defines no record
surface, asks no question about scalar record additivity, and writes
no record functional `I(.)`. It manipulates one finite-dimensional
matrix `Y` and one Hermitian matrix `K = Y^dag Y`, computes
right-`U(3)`-orbit invariants of `K`, and exhibits witness pairs
that distinguish the admitted right-Gram selector and sheet scalars
from every such invariant. The right-orbit conjugacy invariance step
(`F(U K U^dag) = F(K)`), the witness construction, and the
contraposition conclusion are fixed by:

- finite-dimensional matrix algebra over `C` (Hermitian conjugation
  is the standard `.conj().T`, `U(3)` is the standard `3 x 3`
  unitary group, polynomial invariants of `K` are eigenvalues +
  traces of powers + det, all standard linear algebra);
- the Lattice axiom (`Z^3` indexing context, supplied via the upstream
  PMNS-frame chain whose `Y` is a `3 x 3` matrix on generation labels);
- the Quantum axiom (one-qubit / `Cl(3)` local algebra, supplied via
  the upstream chain whose `Y` lives in the generation-flavor sector of
  the `Cl(3)`-on-`Z^3` package).

The Record axiom adds an additive scalar record functional. It does
not modify (and is not modified by) finite-dimensional matrix
algebra, Hermitian-conjugation rules, the `U(3)` action on a
right-multiplied `Y`, spectral theory of `K`, or the parametrized
witness families used in the parent runner. So the conclusion (no
right-conjugacy-invariant observable can intrinsicize the admitted
route) is invariant under the axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic check passes using only Hermitian-
conjugation algebra + `U(3)` action + spectral theory, and a
"Record-axiom counterfactual" block confirms that the conclusion is
unchanged whether or not a Record-axiom statement is appended.

---

## Companion runner block plan

`scripts/audit_companion_pmns_right_conjugacy_invariant_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the parent's right-conjugacy-
orbit no-go. Each block runs as an independent numeric / algebraic
check; nothing is hard-coded against an expected target value beyond
standard finite-dimensional linear-algebra identities. The runner
reports `PASS` / `FAIL` per check; the cached output records the run.

Block 1 — Hermitian-conjugation algebra. Verifies the basic algebraic
fact `(Y U^dag)^dag (Y U^dag) = U Y^dag Y U^dag = U K U^dag` for
random `Y in C^{3x3}` and random `U in U(3)`. Pure matrix algebra; no
axiom content.

Block 2 — Right-orbit preserves spectral signature of `K`. Generates
explicit `(Y, U)` pairs using the parent runner's `monomial_y`,
`canonical_y`, `dft3`, and `rotation12` helpers and verifies that the
eigenvalues of `K = Y^dag Y` and of `K' = (Y U^dag)^dag (Y U^dag)`
agree to machine precision, along with `Tr(K^n)` for `n = 1, 2, 3`
and `det(K)`. Reproduces the parent runner's Part 1 spectral-signature
witness.

Block 3 — Every conjugacy-invariant function is orbit-constant.
Constructs three explicit conjugacy-invariant functionals `F_1(K) =
Tr(K)`, `F_2(K) = Tr(K^2)`, `F_3(K) = det(K)` and verifies
`F_i(U K U^dag) = F_i(K)` to machine precision for 5 random
`(K, U)` pairs (`K` Hermitian PSD). Pure spectral algebra.

Block 4 — Witness that `m_R(Y)` (right-score) varies along the orbit.
Reproduces the parent runner's monomial-then-DFT witness: starts at
`Y_mono` with `right_score = 0` (diagonal `K`), rotates by
`U = dft3()` to `Y_mono_rot` with `right_score = 3` (fully off-
diagonal `K`), while the spectral signature is preserved. Confirms
the witness exhibits the orbit-variance of the admitted selector
datum.

Block 5 — Witness that `|K_{12}|` varies along the orbit. Reproduces
the parent runner's canonical-`Y` witness with a `12`-rotation
`U = rotation12(theta)` of the right frame, confirming `|K_{12}|`
changes by `>= 1e-3` while the spectral signature is preserved.
Confirms the witness exhibits the orbit-variance of the admitted
sheet datum.

Block 6 — Conclusion-of-no-go check. Combines Blocks 3-5: any
candidate intrinsic observable `I(Y) = F(K)` invariant under right
`U(3)` must equal a function of the spectral signature alone (Block
3); but two named admitted data (`m_R(Y)`, `|K_{12}|`) take distinct
values along the same orbit (Blocks 4-5); therefore no
right-conjugacy-invariant `I(Y)` can equal either admitted datum on
a single orbit. The contraposition is a logical step on the
verifications themselves; the block records the truth-value of the
combined premise.

Block 7 — Parent runner reproduction. Independently re-runs the
parent runner's four parts via direct function calls and confirms
all four parts pass with the same numeric witnesses as the parent
runner. Provides a one-shot check that the companion's algebra
agrees with the parent runner's algebra.

Block 8 — Static-source scan of parent note. Reads
`docs/PMNS_RIGHT_CONJUGACY_INVARIANT_NO_GO_NOTE.md` and
verifies that the parent's "Question", "Bottom line",
"Theorem-level statement", "What this closes", and "What this does
not close" sections contain zero Record-axiom usage tokens
(`I(R_1`, `I(R)`, `scalar record`, `record functional`,
`record-readout`, `additive record`, `additive scalar record`,
`MINIMAL_AXIOMS_2026-06-04`, `Record axiom`). Confirms the
parent's load-bearing surface does not invoke Record-axiom content.

Block 9 — Static-source scan of parent runner. Reads
`scripts/frontier_pmns_right_conjugacy_invariant_nogo.py` and
verifies the same zero-Record-axiom-token property for the parent
runner. Confirms the load-bearing algebra at the script level
does not invoke Record-axiom content.

Block 10 — Record-axiom counterfactual. Re-runs Blocks 2-6 inside an
explicit "Record axiom is asserted" outer scope and an explicit
"Record axiom is not asserted" outer scope; verifies that the
load-bearing conclusion (no right-conjugacy-invariant `I(Y)` can
intrinsicize the admitted right-Gram route) is identical in both
runs. The counterfactual is a tautology at the algebra level (no
Record-axiom content enters the spectral / `U(3)` / witness steps),
which is precisely the substantive content of (C1).

Block 11 — Quantum / Lattice content preservation across memos.
Verifies that the `MINIMAL_AXIOMS_2026-05-20.md` qubit-local-algebra
and `Z^3`-lattice content is preserved verbatim in
`MINIMAL_AXIOMS_2026-06-04.md` under the explicit names Quantum and
Lattice; verifies that the new Record axiom is a third, additive,
non-overlapping statement; verifies that the new memo's `Record`
scope statement explicitly excludes the bridge content that the
parent's chain would otherwise require if it depended on the Record
axiom (it does not).

Block 12 — Hypothesis-set parity check. Re-derives the parent's
load-bearing matrix-algebra steps (right-orbit conjugacy, spectral
preservation, two witness pairs) without any reference to the
Record axiom, confirming that the parent's premise set is
strictly smaller than `{Lattice, Quantum, Record}` and is
unchanged across the 2026-05-20 -> 2026-06-04 axiom-set update.

Block 13 — Upstream-naming surface scan. Reads the parent's two
named upstream narrow inputs
(`docs/PMNS_SCALAR_BRIDGE_NONREALIZATION_NOTE.md` and
`docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`) and verifies that
the parent's Part 3 string-matched evidence ("does not realize the
missing PMNS" / "does not generate a mixed scalar bridge"; "W[J] =
log |det(D+J)| - log |det D|" or `W[J] = log|det(D+J)| - log|det D|`)
is still present on `origin/main` after the upstream Record-axiom
repair. Confirms the parent's Part 3 scalar-bank rule-out evidence
still string-matches; this is a graph-bookkeeping continuity check,
not a Record-axiom argument.

Total: 13 blocks, with the exact `PASS` / `FAIL` count recorded in
the SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline
derives `effective_status`), no status field changes are implied by
this PR. The audit lane decides whether to re-honor the prior
judicial verdict pattern on the new premise hash; this companion
only supplies machine-checkable evidence on whether the new Record
axiom disturbs the load-bearing right-conjugacy-orbit chain.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the
parent's no-go output, nor does it close the gap that the parent's
own "What this does not close" section flags (canonical right-handed
frame; non-conjugacy-invariant right-sensitive observable principle;
selected-branch Hermitian data law). Each downstream claim and each
open right-sensitive bridge must be examined independently.

---

## Audit-ordering and integration

This companion does not migrate the parent note or the parent runner.
The parent note cites the older `MINIMAL_AXIOMS_2026-05-20.md`-era
axiom inputs only implicitly (via the named upstream PMNS and
observable-principle rows); a separate citation-migration PR (if
desired) can refresh the parent note's source rows on its own
schedule. This companion is independent of that text update and is
content-only.

This companion's load-bearing-step invariance observation depends only
on the Quantum and Lattice content being preserved across the two
memos — verified in Block 11 — and on the Record axiom adding a
strictly additive non-overlapping statement — confirmed by direct
reading of `MINIMAL_AXIOMS_2026-06-04.md` §"Record" and by the
parent's load-bearing chain having zero Record-axiom usage tokens
(Blocks 8-9).

---

## References

- Parent note:
  [`PMNS_RIGHT_CONJUGACY_INVARIANT_NO_GO_NOTE.md`](PMNS_RIGHT_CONJUGACY_INVARIANT_NO_GO_NOTE.md)
- Parent runner:
  `scripts/frontier_pmns_right_conjugacy_invariant_nogo.py`
- Prior judicial verdicts (archived):
  `docs/audit/data/audit_ledger.json` row
  `pmns_right_conjugacy_invariant_no_go_note`,
  `previous_audits[0]` (2026-05-04, `audited_clean`,
  `chain_closes=true`, archived via
  `criticality_increased:high->critical`),
  `previous_audits[1]` (2026-05-05, `audited_conditional`,
  `chain_closes=false`, archived for prior note hash
  `9b84b6e8`)
- Current ledger state: `audit_status=unaudited`,
  `effective_status=unaudited`,
  `effective_status_reason=awaiting_audit`,
  `load_bearing_score=10.19`, `claim_type=no_go`
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-algebra
  content):
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
- Template companion (yt_ward):
  [`YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)
