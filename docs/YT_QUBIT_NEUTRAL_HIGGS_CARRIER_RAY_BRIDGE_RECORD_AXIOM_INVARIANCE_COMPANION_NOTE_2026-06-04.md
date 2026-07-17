# YT Qubit Neutral-Higgs Carrier-Ray Bridge: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing carrier-ray identification in
[`YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md`](YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md)
is invariant under the 2026-06-04 Record-axiom adoption. It is not a
new theorem claim, not a status promotion, and not an attempt to
perform re-audit work. If the audit pipeline seeds this file, it is a
meta companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that
authority.
**Companion target:** `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25`
(parent note
`docs/YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md`).
**Primary companion runner:**
[`scripts/audit_companion_yt_qubit_neutral_higgs_carrier_ray_bridge_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_yt_qubit_neutral_higgs_carrier_ray_bridge_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_yt_qubit_neutral_higgs_carrier_ray_bridge_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_yt_qubit_neutral_higgs_carrier_ray_bridge_record_axiom_invariance_2026_06_04.txt)

---

## Why this companion exists

The parent narrow theorem
`yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` was
previously audit-loop-resolved as `audited_clean` (`bounded_theorem`,
class A; load-bearing score 6.322) on the narrowed scope:

> On the current qubit-on-`Z^3` surface, the one-site signed-record
> source used by the Y_T source-action support packet is, up to an
> affine source-coordinate reparameterization, the `P_-` occupation
> source on the qubit, and `P_-` is the unique neutral-charge ray of
> the retained one-Higgs electroweak doublet (Q_H = T_3 + Y_H acting on
> H_0 = (0, v/sqrt(2))^T). The radial tangent dH/ds remains on the
> neutral ray and is annihilated by Q_H. No physical Y_T coefficient,
> Yukawa value, or g_2(v) closure is audited.

That quoted audit history describes the earlier source content; it is not
current physical authority. After the defined-algebra repair, the cited
diagonalization theorem supplies only matrices and a kernel ray in an abstract
`C^2`, so the physical qubit/EW/Higgs same-carrier step remains open.

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md`
section 6) changed the stable `minimal_axioms` premise-node note-hash
from `1d36a556` to `b8848fc8`. The audit pipeline correctly
invalidated the prior `audited_clean` snapshot via
`invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`,
returning the row to unaudited effective status.

This companion records, for the audit lane, that the parent's
load-bearing carrier-ray identification is **independent of the
Record axiom**: its finite-dimensional calculation uses the Quantum-axiom
content (one-qubit local algebra at each site; equivalently
`M_2(C) ~= Cl(3,0)`) plus separately defined matrices `T_3`, `Y`, `T_3+Y`,
and `h0` from the historical
`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26` path.
That cited theorem no longer supplies a physical one-Higgs/electroweak
carrier, so the parent's physical carrier-ray identification remains open.
Adopting the Record axiom adds a strictly additive scalar
record-readout statement that is neither used nor invoked anywhere in
the carrier-ray identification. The projector-algebra identity
`sigma_z = P_+ - P_- = I - 2 P_-`, the affine source-coordinate
equivalence `exp(h sigma_z) = exp(h) exp(-2 h P_-)`, the
neutral-ray annihilation `Q_H H_0 = 0`, and the radial-tangent
neutrality `Q_H dH/ds = 0` are unchanged.

This companion is therefore audit-friendly evidence that the prior
substantive reading survives the axiom-set change. It is not a
re-audit and does not promote status; it documents the
load-bearing-step dependency surface in machine-checkable form so the
audit lane can decide how to treat the parent on the new premise hash.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the carrier-ray identification.**
The parent's load-bearing chain (note's "Theorem" section through the
projector and neutral-ray steps) depends only on:

1. the one-qubit local Pauli/projector algebra at a site
   (`sigma_z`, `P_+`, `P_-`, `I`; the Quantum-axiom content);
2. the affine source-coordinate identity
   `exp(h sigma_z) = exp(h) * exp(-2 h P_-)`, which is elementary
   matrix-exponential algebra on a diagonal Pauli generator;
3. the defined `C^2` bookkeeping
   `T_3 = sigma_z / 2`, `Y = (1/2) I`, `Q = T_3 + Y`,
   `h0 = (0, v/sqrt(2))^T`
   (cited authority
   `EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`);
4. one-dimensional radial calculus on H(s) = (0, v(s)/sqrt(2))^T.

None of items 1-4 use the Record axiom's additive scalar
record-readout content. They use only the Quantum axiom (one-qubit /
`Cl(3,0)` local algebra), the Lattice axiom (`Z^3` site set; only as
the carrier of the qubit), the separately defined `C^2` matrix theorem, and
elementary finite-dimensional linear algebra. None of these facts identifies
the two algebraic carriers as the same physical surface.

**(C1) is the only auditable companion observation.** The bridge from
the carrier-ray identification to a physical Y_T coefficient, the
coefficient-certified top/W response rows, the canonical scalar LSZ
normalization, and the retained physical-scale `g_2(v)` all remain
explicitly out of scope, exactly as in the parent note (parent's
"What This Still Does Not Close" section).

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs;
- assert anything about Record-axiom content or its scope;
- re-audit `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25`
  or any other ledger row;
- modify the audit ledger, the audit queue, or any status field;
- claim physical Y_T closure, top-coefficient certification, retained
  one-Higgs/top-Yukawa selection authority, retained hypercharge
  uniqueness authority, or retained physical-scale `g_2(v)` authority.

The audit lane decides whether (C1) is sufficient evidence for the
parent's fresh treatment on the new premise hash or whether a fresh
per-site audit is warranted.

---

## The Record axiom is not used by the load-bearing step

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing chain defines no record surface, asks no
question about scalar record additivity, and writes no record
functional `I(.)`. It computes:

- the spectral decomposition of `sigma_z` on a single qubit
  (`sigma_z = P_+ - P_-`, both projectors orthogonal, summing to `I`);
- the affine identity `sigma_z = I - 2 P_-`, which implies
  `exp(h sigma_z) = exp(h) * exp(-2 h P_-)` by commuting-exponential
  algebra (`[I, P_-] = 0`);
- the action of `P_-`, `P_+`, and `Q_H = T_3 + Y_H` on the retained
  doublet vacuum `H_0 = (0, v/sqrt(2))^T` (which gives
  `P_- H_0 = H_0`, `P_+ H_0 = 0`, `Q_H H_0 = 0`);
- the radial-tangent computation
  `dH/ds = (0, v'(s)/sqrt(2))^T`, with `P_- dH/ds = dH/ds`,
  `Q_H dH/ds = 0`;
- the same-source top/W response-ratio bookkeeping
  `(dm_t/ds) / (dm_W/ds) = sqrt(2) * y_t / g_2`, an algebraic
  Jacobian cancellation.

These are pure finite-dimensional Pauli/projector identities plus
one-variable calculus on a smooth profile. None of them invokes a
record additivity functional `I(.)`, a record collection algebra, a
disjoint-union additivity statement, an additive-baseline convention,
or any Record-axiom citation.

The term "signed record" appears in the parent note as inherited
naming from the predecessor support packet
`YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md` (which uses
`epsilon_x in {-1, +1}` as the one-site signed indicator). At the
load-bearing-content level, "signed record" is just the Pauli
generator `sigma_z` whose spectrum is `{+1, -1}`; the parent does
not invoke the Record-axiom's additive scalar functional content to
operate on it. The terminological inheritance does not flow Record-
axiom content into the parent's projector-algebra reasoning.

The Record axiom is a separate, non-overlapping framework axiom (per
the new memo's own scope statement, it does not supply rules for
record production, persistence, measurement / decoherence, Born
weights, P2 / modulus / phase-blindness, log-det structure, time
arrow, system composition, normalization / scale, source / action
identification, `AC_phi_lambda`, theta, or arbitrary observable
identification). The parent's projector-algebra and retained-EW
content are likewise outside the Record axiom's content. So the
carrier-ray identification, the affine source-coordinate equivalence,
and the neutral-ray annihilation are invariant under the axiom-set
change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing algebraic check passes using only Quantum-axiom
(one-qubit Pauli) content, defined C^2 matrix content, and elementary
calculus, and a "Record-axiom counterfactual" block confirms that the
output is unchanged whether or not a Record-axiom statement is
appended.

---

## Companion runner block plan

`scripts/audit_companion_yt_qubit_neutral_higgs_carrier_ray_bridge_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the carrier-ray identification
load-bearing step. Each block runs as an independent numeric /
algebraic check; nothing is hard-coded against an expected target value
beyond standard finite-dimensional algebra. The runner reports
`PASS` / `FAIL` per check; the cached output records the run.

Block 1 — Pauli/projector algebra. Verifies
`sigma_z^2 = I`, `P_+^2 = P_+`, `P_-^2 = P_-`, `P_+ P_- = 0`,
`P_+ + P_- = I`, `sigma_z = P_+ - P_-`, `sigma_z = I - 2 P_-`. One-
qubit Quantum-axiom content only.

Block 2 — Affine source-coordinate equivalence. Verifies the matrix-
exponential identity `exp(h sigma_z) = exp(h) * exp(-2 h P_-)` on a
sample of real values of `h` (including `h = 0`, small positive,
large positive, negative). Uses only commuting-exponential algebra
(`[I, P_-] = 0` is checked explicitly).

Block 3 — Normalized weight equivalence. Verifies that the diagonal
weight vector `(exp(h), exp(-h))^T` from `exp(h sigma_z)` equals
`exp(h) * (1, exp(-2h))^T` from the `exp(-2 h P_-)` reading, so the
common factor `exp(h)` cancels in the normalized source family.

Block 4 — Defined C^2 matrix bookkeeping. Verifies
`T_3 = sigma_z / 2`, `Y_H = (1/2) I`, `Q_H = T_3 + Y_H` equals
`diag(1, 0)`. Loads explicit retained doublet vacuum
`H_0 = (0, v / sqrt(2))^T`.

Block 5 — Neutral-ray annihilation. Verifies `P_- H_0 = H_0`,
`P_+ H_0 = 0`, `Q_H H_0 = 0`. Verifies `Q_H` acts as identity on the
charged upper component `(1, 0)^T`.

Block 6 — Neutral ray uniqueness inside stipulated C^2. Verifies
`rank(Q_H) = 1` and that `nullspace(Q_H) = span((0, 1)^T)` (a single
ray, the defined lower ray). Confirms parent's "neutral ray is unique
in the one-Higgs doublet" line.

Block 7 — Radial tangent stays neutral. Verifies symbolically that
`H(s) = (0, v(s) / sqrt(2))^T` satisfies `P_- H = H`, `P_+ H = 0`,
`Q_H H = 0`, `P_- dH/ds = dH/ds`, `Q_H dH/ds = 0`. Uses sympy
symbolic differentiation; no record functional appears.

Block 8 — Top / W response-ratio Jacobian cancellation. Verifies
that with `m_t(s) = y_t * v(s) / sqrt(2)` and
`m_W(s) = g_2 * v(s) / 2`, the ratio
`(dm_t/ds) / (dm_W/ds)` simplifies to `sqrt(2) * y_t / g_2`
independent of `v'(s)`. This is the parent's source-coordinate-scale
cancellation, and it is algebraic in `v`, `y_t`, `g_2`; no Record
content enters.

Block 9 — Static-source scan of parent note. Reads the parent note's
"Theorem" + "What This Closes" sections and verifies zero occurrences
of the Record-axiom usage tokens
`{"I(R_1", "I(R)", "I(empty)", "scalar record functional",
"record functional", "additive scalar record",
"additive over disjoint", "MINIMAL_AXIOMS_2026-06-04"}`
inside the load-bearing section. Confirms that the structural Pauli /
projector / EW tokens `{"sigma_z", "P_-", "P_+", "Q", "H_0",
"P_- H_0 = H_0"}` are present (the actual load-bearing content).

Block 10 — Record-axiom counterfactual. Re-runs Blocks 1-7 inside an
explicit "Record axiom is asserted" outer scope and an explicit
"Record axiom is not asserted" outer scope; verifies that every
load-bearing numeric / matrix output is bit-identical in both runs.
The counterfactual is a tautology at the calculation level (no
Record-axiom content enters the Pauli / projector / EW steps), which
is precisely the substantive content of (C1).

Block 11 — Axiom-name vs axiom-content separation. Verifies that the
parent note's `MINIMAL_AXIOMS_2026-05-20.md` citation refers to the
historical two-axiom wording for the qubit local algebra and `Z^3`
lattice, and that those content statements are preserved in
`MINIMAL_AXIOMS_2026-06-04.md` under the explicit names Quantum and
Lattice. Verifies that the Record axiom's own scope statement
excludes the bridges (source/action identification, log-det,
production, measurement, etc.) that would otherwise be needed to
turn the carrier-ray identification into a physical Y_T result —
which is exactly why the parent's "What This Still Does Not Close"
section is preserved.

Block 12 — Independent recomputation of the carrier-ray
identification. Constructs an independent finite-dimensional symbolic
representation of `sigma_z`, `P_-`, `P_+`, `T_3`, `Y_H`, `Q_H`,
`H_0` from scratch (without re-importing parent-note constants), and
verifies that the load-bearing identities `sigma_z = P_+ - P_-`,
`Q_H H_0 = 0`, `P_- H_0 = H_0` hold on this independent
construction.

Total: 12 blocks. The exact PASS / FAIL count is recorded in the
SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline
derives `effective_status`), no status field changes are implied by
this PR.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
output. Each downstream claim must be examined independently against
the new axiom-set premise hash. The other rows recently
axiom-invalidated under the same hash change are out of scope of this
companion; they are listed in the audit queue's
`axiom_premise_changed` cohort and should be examined separately as
the audit lane reaches them.

---

## Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-20.md` citation to
`MINIMAL_AXIOMS_2026-06-04.md`. The current framework baseline is the
2026-06-04 memo; the predecessor memo is used here only as a historical
continuity check for the local-algebra wording. A separate
citation-migration PR (if desired) can refresh the parent note's
authority surface; this companion is independent of that text update
and is content-only.

This companion's load-bearing-step invariance observation depends
only on the Quantum and Lattice content being preserved across the
two memos — verified in Block 11 — and on the Record axiom adding a
strictly additive non-overlapping statement — confirmed by direct
reading of `MINIMAL_AXIOMS_2026-06-04.md` §"Record".

---

## References

- Parent note:
  [`YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md`](YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md)
- Parent runner:
  `scripts/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py`
- Cited defined-algebra source for the `C^2` matrix bookkeeping only:
  [`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md)
- Predecessor support packet (signed-record naming source, non-load-bearing
  reader pointer):
  `YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md`
- Prior judicial verdict snapshot:
  `docs/audit/data/audit_ledger.json` row
  `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25`,
  `previous_audits[-1]` (archived with
  `invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`)
- Current framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework memo used for continuity checking:
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
