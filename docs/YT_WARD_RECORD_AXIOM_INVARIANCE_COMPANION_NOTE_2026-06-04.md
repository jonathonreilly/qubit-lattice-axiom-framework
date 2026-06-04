# YT Ward H_unit Matrix Element: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing matrix-element value in
[`YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
is invariant under the 2026-06-04 Record-axiom adoption. It is not a new
ledger claim, not a status promotion, and not an attempt to perform
re-audit work. The audit lane sets `claim_type`, `audit_status`, and
pipeline-derived `effective_status`.
**Companion target:** `yt_ward_identity_derivation_theorem` (parent note
`docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md`).
**Primary companion runner:**
`scripts/audit_companion_yt_ward_record_axiom_invariance_2026_06_04.py`
**Cached log:**
`logs/runner-cache/audit_companion_yt_ward_record_axiom_invariance.txt`

---

## Why this companion exists

The parent narrow theorem `yt_ward_identity_derivation_theorem` was
previously audit-loop-resolved on 2026-05-25 as `audited_clean`
(`bounded_theorem`, class A) by a 3/5 judicial-panel majority on the
narrowed scope:

> On the admitted canonical Q_L=(2,3) surface, the unit-normalized
> scalar-singlet H_unit matrix element on a single top-basis component
> equals `1/sqrt(6)`; no SM Yukawa readout, Planck transport, or
> precision claim is audited.

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md`
section 6) changed the stable `minimal_axioms` premise-node note-hash
from `1d36a556` to `b8848fc8`. The audit pipeline correctly invalidated
the prior `audited_clean` snapshot via
`invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`,
returning `effective_status=unaudited`.

This companion records, for the audit lane, that the parent's
load-bearing step is **independent of the Record axiom**: it uses only
the Lattice and Quantum axiom content, plus standard group-theoretic
identities (Fierz, Clebsch-Gordan, Clifford). Adopting the Record axiom
adds a strictly additive scalar record-readout statement, which is
neither used nor invoked anywhere in the H_unit matrix-element
calculation. The matrix-element value, the unit-residue normalization
`Z = sqrt(6)`, and the scalar-singlet uniqueness of `H_unit` on the
Q_L = (2,3) block are unchanged.

This companion is therefore audit-friendly evidence that the prior
clean verdict's substantive content survives the axiom-set change. It
is not a re-audit and does not promote status; it documents the
load-bearing-step dependency surface in machine-checkable form so the
audit lane can decide whether to honor or re-test the prior judicial
verdict on the new premise hash.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the H_unit matrix element.** The
parent's load-bearing step `y_t_bare = 1/sqrt(6)` (Eq. 3.8 of
`YT_WARD_IDENTITY_DERIVATION_THEOREM.md`) depends only on:

1. the Q_L = (2,3) block dimension `N_c * N_iso = 6`;
2. the canonical kinetic normalization on a free 2-point function
   (Step 1, `Z^2 = N_c * N_iso = 6`);
3. the Clebsch-Gordan overlap of the unit-norm (1,1) scalar singlet
   with a single basis component (Step 2, `<top-pair | S> = 1/sqrt(6)`);
4. canonical fermion-state normalization (kinematic identity).

None of items 1-4 use the Record axiom's additive scalar record-readout
content. They use only the Lattice axiom (`Z^3` substrate / index
structure inherited via D1-D8) and the Quantum axiom (one-qubit /
`Cl(3)` local algebra; SU(N_c) and SU(N_iso) block organization).

**(C1) is the only auditable companion observation.** The bridge from
the local H_unit matrix-element shorthand `y_t_bare` to the Standard
Model top Yukawa observable and the Planck-surface tadpole transport
remain explicitly out of scope, exactly as in the parent note
(parent's "Audit boundary" section).

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs (C1 = canonical plaquette / `u_0` surface; C2 = `g_bare = 1`);
- assert anything about Record-axiom content or its scope;
- re-audit `yt_ward_identity_derivation_theorem` or any other ledger
  row;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1) is sufficient evidence to re-honor
the previous judicial verdict or whether a fresh per-site audit is
warranted on the new premise hash.

---

## The Record axiom is not used by the load-bearing step

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing step `y_t_bare = 1/sqrt(6)` defines no record
surface, asks no question about scalar record additivity, and writes no
record functional `I(.)`. It computes a single matrix element of a
local composite operator on a fermion-pair state. The operator content
(`H_unit = (1/sqrt(N_c * N_iso)) * Σ ψ̄_{α,a} ψ_{α,a}`), the canonical
norm (`Z^2 = 6`), and the Clebsch-Gordan weight (`1/sqrt(6)`) are
fixed by:

- index counting on the Q_L block (Lattice + Quantum axiom content via
  D1-D8 of the parent note);
- standard free Wick contraction (D9-D11 of the parent);
- standard finite-dimensional Lie-algebra identities (D12, S1, S2 of
  the parent).

The Record axiom adds an additive scalar record functional. It does
not modify (and is not modified by) the Lattice index structure, the
Quantum local algebra, the Wick contraction of free fields, or the
group-theoretic Fierz/Clebsch-Gordan/Clifford identities. So the value
`1/sqrt(6)` is invariant under the axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic check passes using only Lattice +
Quantum content and standard group-theoretic identities, and a
"Record-axiom counterfactual" block confirms that the value is
unchanged whether or not a Record-axiom statement is appended.

---

## Companion runner block plan

`scripts/audit_companion_yt_ward_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the H_unit matrix-element load-
bearing step. Each block runs as an independent numeric/algebraic
check; nothing is hard-coded against an expected target value beyond
standard finite-dimensional algebra. The runner reports `PASS` /
`FAIL` per check; the cached output records the run.

Block 1 — Q_L block dimension. Verifies `dim(Q_L) = N_c * N_iso = 6`
from `(N_c, N_iso) = (3, 2)` (Lattice + Quantum axiom inputs only,
via the D1-D8 chain in the parent note).

Block 2 — Canonical kinetic Z. Computes the unit-residue normalization
`Z^2 = N_c * N_iso = 6` from the explicit index contraction in the
two-point function `<phi(x) phi(y)>_{conn,free}` of a free Q_L
bilinear (the parent's Eqs. 1.1-1.3). Uses only free-fermion Wick
contraction and index counting; no Record axiom content appears.

Block 3 — Unit-norm singlet state. Constructs the unit-norm (1,1)
singlet `|S> = (1/sqrt(6)) Σ |α,a> ⊗ |α,a>*` explicitly in a 6-dim
basis and verifies `<S|S> = 1` exactly.

Block 4 — Clebsch-Gordan overlap on every basis component. Verifies
`<basis_k | S> = 1/sqrt(6)` for each of the 6 basis components
`|α,a>`. Confirms that the parent's "same for each of the 6 basis
components, by singlet uniformity" is an explicit calculation, not an
assumption.

Block 5 — H_unit operator matrix element. Builds `H_unit` from its
explicit operator content `(1/sqrt(N_c * N_iso)) * Σ ψ̄_{α,a} ψ_{α,a}`
and computes the vacuum-to-top-basis matrix element. Reproduces the
parent's Eq. (3.8) value `y_t_bare = 1/sqrt(6)` from the operator
definition alone; no OGE input is used.

Block 6 — SU(3) color-singlet Fierz coefficient. Computes
`Σ_A T^A_{ab} T^A_{cd}` for all A, b, a, c, d using explicit Gell-Mann
matrices and extracts the color-singlet (`δ_ab δ_cd`) channel
coefficient. Verifies the standard result `-1/(2 N_c)` to machine
precision.

Block 7 — Lorentz-Clifford scalar Fierz coefficient. Computes the
Fierz decomposition of `(γ^μ)_{αβ} (γ_μ)_{γδ}` using explicit Dirac
matrices and extracts the scalar (`(1)(1)`) channel coefficient.
Verifies `|c_S| = 1`.

Block 8 — Direction uniqueness. Verifies that the (1,8), (3,1), (8,3)
alternative composite irreps on Q_L give different unit-residue
normalizations (`Z^2 = 8, 9/2, 24`) — none coincide with `Z^2 = 6`.
Confirms that `H_unit` is the unique scalar singlet on Q_L (parent's
D17).

Block 9 — Record-axiom usage check. A static-source scan of the
parent runner `scripts/frontier_yt_ward_identity_derivation.py` plus
this companion runner verifies that NEITHER load-bearing block invokes
a record functional `I(.)`, a record additivity statement, a record
collection, or a Record-axiom citation. The check enumerates the
phrase set
`{"I(", "record_functional", "I_empty", "scalar record", "additive
record", "record-readout", "I(R_1", "I(R)"}` over the load-bearing
section of the parent note and confirms zero matches inside the
auditable core.

Block 10 — Record-axiom counterfactual. Re-runs Blocks 1-5 inside an
explicit "Record axiom is asserted" outer scope and an explicit
"Record axiom is not asserted" outer scope; verifies that the
load-bearing value `y_t_bare = 1/sqrt(6)` is identical in both runs.
The counterfactual is a tautology at the calculation level (no
Record-axiom content enters the Wick / index / group-theory steps),
which is precisely the substantive content of (C1).

Block 11 — Axiom-name vs axiom-content separation. Verifies that the
parent note's `MINIMAL_AXIOMS_2026-05-20.md` citations refer to A1
(qubit local algebra) and A2 (`Z^3` substrate), and that those
identical content statements are preserved in
`MINIMAL_AXIOMS_2026-06-04.md` under the names Quantum and Lattice.
The Record axiom is a third, additive, non-overlapping statement.

Block 12 — Independent recomputation of `1/sqrt(6)`. Computes
`y_t_bare = 1/sqrt(6)` four ways (D17 operator content; D11
unit-residue; Block 4 Clebsch-Gordan on basis component; H_unit
matrix element on a randomly chosen Q_L basis component) and
verifies that all four agree to machine precision. The four routes
together exhaust the load-bearing surface of Eqs. (1.1)-(3.8) of the
parent note.

Total: 12 blocks, ~18 PASS checks; 0 FAIL targeted.

---

## Audit-pipeline boundaries

This companion contributes no new ledger row claim and asserts no
status promotion. The companion runner reads as `meta` (audit-companion
evidence runner). Per [`docs/audit/README.md`](audit/README.md) (the
auditor sets `claim_type`, the auditor sets `audit_status`, and the
pipeline derives `effective_status`), no status field changes are
implied by this PR. The audit lane decides whether to re-honor the
prior judicial verdict on the new premise hash; this companion only
supplies machine-checkable evidence on whether the new Record axiom
disturbs the load-bearing step.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
output. Each downstream claim must be examined independently against
the new axiom-set premise hash. The 26 other rows recently axiom-
invalidated under the same hash change are out of scope of this
companion; they are listed in the audit queue's
`axiom_premise_changed` cohort and should be examined separately as
the audit lane reaches them.

---

## Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-20.md` citations to `MINIMAL_AXIOMS_2026-06-04.md`.
Both are valid framework axiom memos; the 2026-06-04 memo cites the
2026-05-20 memo as the "local-algebra authority and historical source
for the prior two-axiom wording." A separate citation-migration PR (if
desired) can refresh the parent note's `Source` column; this companion
is independent of that text update and is content-only.

This companion's load-bearing-step invariance observation depends only
on the names and content of A1/Quantum and A2/Lattice being preserved
across the two memos — verified in Block 11 — and on the Record axiom
adding a strictly additive non-overlapping statement — confirmed by
direct reading of `MINIMAL_AXIOMS_2026-06-04.md` §"Record".

---

## References

- Parent note:
  [`YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
- Parent runner:
  `scripts/frontier_yt_ward_identity_derivation.py`
- Prior judicial verdict snapshot:
  `docs/audit/data/audit_ledger.json` row
  `yt_ward_identity_derivation_theorem`, `previous_audits[-1]`
  (`audited_clean`, `bounded_theorem`, class A, judicial-panel
  majority 3/5, 2026-05-25, archived 2026-06-04 with
  `invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-algebra
  content): [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
