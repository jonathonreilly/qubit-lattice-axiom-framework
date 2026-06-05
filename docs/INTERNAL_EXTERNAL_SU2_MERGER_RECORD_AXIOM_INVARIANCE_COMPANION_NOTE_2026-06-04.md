# Internal-External SU(2) Merger Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing operator-identification claim in
[`INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md`](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md)
is invariant under the 2026-06-04 Record-axiom adoption. It is not a new
theorem claim, not a status promotion, and not an attempt to perform
re-audit work. If the audit pipeline seeds this file, it is a meta
companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that authority.
**Companion target:** `internal_external_su2_merger_from_universal_property_narrow_theorem_note_2026-05-27`
(parent note `docs/INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md`).
**Primary companion runner:**
[`scripts/audit_companion_internal_external_su2_merger_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_internal_external_su2_merger_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_internal_external_su2_merger_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_internal_external_su2_merger_record_axiom_invariance_2026_06_04.txt)

---

## Why this companion exists

The parent narrow theorem
`internal_external_su2_merger_from_universal_property_narrow_theorem_note_2026-05-27`
states an operator-level identification between the per-site internal
`su(2)` spin generators on `H_x = C^2` and the infinitesimal
`Spin(3)` generators coming from the Clifford universal property of
`Cl(3,0)`. Concretely it asserts that

```text
S_i := sigma_i / 2
B_i := (1/2) gamma_j gamma_k   for (i,j,k) cyclic in (1,2,3)
```

obey `B_i = i * S_i`, `[S_i, S_j] = i epsilon_{ijk} S_k`, and that the
spatial-rotation lift `U(R)` on `H_x` for `R` in the cubic point group
`O_h` acts as `U(R) sigma_i U(R)^* = sum_j R_ij sigma_j` for the 24
proper rotations, with the 24 improper rotations checked as signed
real-Clifford generator actions.

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md`
section 6) changed the stable `minimal_axioms` premise-node note-hash.
The audit pipeline correctly invalidates downstream `audited_clean`
snapshots that depended on the prior premise hash and returns the
affected rows to an unaudited effective status.

This companion records, for the audit lane, that the parent's
load-bearing step is **independent of the Record axiom**: it uses only
the Quantum axiom (one-qubit / `Cl(3,0)` per-site algebra) plus standard
finite-dimensional Clifford-algebra / Lie-algebra / signed-permutation
group identities. Adopting the Record axiom adds a strictly additive
scalar record-readout statement, which is neither used nor invoked
anywhere in the operator-identification chain. The Pauli identities, the
bivector closure, the `O_h` cofactor representation on bivectors, the
`SO(3) -> SU(2)` double cover on proper cubic rotations, and the
infinitesimal generator coincidence `S_i = -i B_i = sigma_i / 2` are
unchanged.

This companion is therefore audit-friendly evidence that the parent's
substantive content survives the axiom-set change. It is not a re-audit
and does not promote status; it documents the load-bearing-step
dependency surface in machine-checkable form so the audit lane can
decide whether to honor or re-test the prior judicial verdict on the new
premise hash.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the SU(2) merger identification.**
The parent's load-bearing identification

```text
B_i = i * S_i,   [S_i, S_j] = i epsilon_{ijk} S_k,
U(R) sigma_i U(R)^* = sum_j R_ij sigma_j  for proper R in O_h,
phi_R(sigma_i) = sum_j R_ij sigma_j (signed) for improper R in O_h
```

depends only on:

1. the Pauli realization `gamma_i = sigma_i` of `Cl(3,0)` on `H_x = C^2`
   (the parent's load-bearing Pauli irrep; standard Quantum axiom
   content via the retained `Cl(3,0)` per-site algebra);
2. anticommutator and pseudoscalar identities of the Pauli matrices
   (`{sigma_i, sigma_j} = 2 delta_ij I`, `sigma_1 sigma_2 sigma_3 = i I`);
3. bivector-product identities (`sigma_j sigma_k = i sigma_i` for
   `(i,j,k)` cyclic, giving `B_i = (i/2) sigma_i = i S_i`);
4. signed-permutation enumeration of `O_h` and the cofactor
   representation on the bivector subspace
   (`phi_R(B_i) = sum_j (cof R)_ij B_j` for all `R` in `O_h`);
5. the axis-angle / half-angle construction of `U(R)` for proper `R`,
   verified by exact sympy conjugation.

None of items 1-5 use the Record axiom's additive scalar record-readout
content. They use only the Quantum axiom (the one-qubit `Cl(3,0)`
algebraic carrier on `H_x`) and standard finite-dimensional algebra.

**(C1) is the only auditable companion observation.** The bridge from
the per-site operator identification to any downstream observable
(`AC_phi_lambda`, Yukawa structure, Planck-surface tadpole transport,
gauge-group emergence) is explicitly out of scope, exactly as in the
parent note (parent's "What This Does Not Claim" section).

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs (per-site Pauli irrep of `Cl(3,0)`; cubic `O_h` point group);
- assert anything about Record-axiom content or its scope;
- re-audit the parent row or any other ledger row;
- modify the audit ledger, the audit queue, or any status field;
- migrate the parent note's `MINIMAL_AXIOMS_2026-05-20.md` citations to
  `MINIMAL_AXIOMS_2026-06-04.md` (the parent text is unchanged; a
  separate citation-migration PR could refresh that if desired).

The audit lane decides whether (C1) is sufficient evidence to honor the
prior judicial verdict (if any) or whether a fresh per-site audit is
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

The parent's load-bearing chain defines no record surface, asks no
question about scalar record additivity, and writes no record functional
`I(.)`. It performs:

- exact `sympy` Pauli anticommutator and pseudoscalar checks on `M_2(C)`;
- exact bivector commutator `[B_i, B_j] = -epsilon_ijk B_k` (equivalently
  `[S_i, S_j] = i epsilon_ijk S_k` with `S_i = -i B_i`) verification;
- signed-permutation enumeration of the 48 elements of `O_h`, with the
  cofactor representation `cof(R)` verifying
  `phi_R(B_i) = sum_j (cof R)_ij B_j` for every `R`;
- axis-angle / half-angle construction of `U(R)` for each of the 24
  proper rotations, with exact verification that
  `U(R) sigma_i U(R)^* = sum_j R_ij sigma_j`;
- exact verification that the bivector lift `B_i` and the spin operator
  `S_i = sigma_i / 2` are the same generator data via `B_i = i S_i`;
- a `[S_i, sigma_a] = i epsilon_iab sigma_b` infinitesimal-generator
  check that ties the proper-rotation half-angle generator on `H_x` to
  the per-site spin operator.

The Record axiom adds an additive scalar record functional. It does not
modify (and is not modified by) the per-site `Cl(3,0)` algebra, the
Pauli realization, signed-permutation enumeration of `O_h`, the
cofactor representation on bivectors, or the `SO(3) -> SU(2)` double
cover construction. So the operator identification `B_i = i S_i` and
`U(R) sigma_i U(R)^* = (R . sigma)_i` is invariant under the axiom-set
change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing identity check passes using only Quantum-axiom
content (the per-site `Cl(3,0)` carrier on `H_x = C^2`) plus standard
finite-dimensional algebra, and a "Record-axiom counterfactual" block
confirms that the identifications are unchanged whether or not a
Record-axiom statement is appended.

---

## Companion runner block plan

`scripts/audit_companion_internal_external_su2_merger_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the SU(2) merger identification.
Each block runs as an independent algebraic check; nothing is hard-coded
against an expected target beyond standard finite-dimensional algebra.
The runner reports `PASS` / `FAIL` per check; the cached output records
the run.

Block 1 — Per-site `Cl(3,0)` carrier dimension. Verifies
`dim(H_x) = 2` and the Pauli realization
`{gamma_i = sigma_i}_{i=1,2,3}` of `Cl(3,0)`. Quantum-axiom content
only; no Record axiom appears.

Block 2 — Pauli anticommutator and pseudoscalar. Verifies
`{sigma_i, sigma_j} = 2 delta_ij I_2` for `i, j in {1,2,3}` and
`sigma_1 sigma_2 sigma_3 = i I_2`. Standard `Cl(3,0)` identities.

Block 3 — Bivector closure. Verifies
`B_i = (1/2) gamma_j gamma_k = (i/2) sigma_i` for `(i, j, k)` cyclic in
`(1,2,3)`, and the bivector commutator
`[B_i, B_j] = -epsilon_ijk B_k`.

Block 4 — Internal `su(2)` commutator. Verifies
`[S_i, S_j] = i epsilon_ijk S_k` with `S_i = sigma_i / 2 = -i B_i`,
recovering the canonical per-site `su(2)` Lie bracket.

Block 5 — Cofactor representation on bivectors. Enumerates the 48
elements of `O_h` (signed permutations of three coordinates), verifies
24 proper and 24 improper, and checks
`phi_R(B_i) = sum_j (cof R)_ij B_j` for every `R` (where
`cof(R) = det(R) R^{-T}` is the cofactor matrix). Confirms the
universal-property action on the bivector subspace is the
`Lambda^2(R^3) ~= R^3` (Hodge-dual) vector representation, with the
det-sign pickup for improper rotations.

Block 6 — Proper-rotation double cover. For each of the 24 proper
cubic rotations `R`, constructs the half-angle `SU(2)` lift `U(R)` via
axis-angle and verifies exactly
`U(R) sigma_i U(R)^* = sum_j R_ij sigma_j` for `i = 1, 2, 3`.

Block 7 — Improper-rotation signed-Clifford action. For each of the 24
improper rotations `R = (-I_3) R'` with `R' = -R` proper, verifies the
signed real-Clifford generator action
`phi_R(sigma_i) = -U(R') sigma_i U(R')^* = sum_j R_ij sigma_j` for
`i = 1, 2, 3`. The improper checks are real-Clifford universal-property
actions on the odd generators, not ordinary complex-linear unitary
conjugations on `H_x`.

Block 8 — Infinitesimal generator coincidence. Verifies
`[S_i, sigma_a] = i epsilon_iab sigma_b` for `i, a in {1,2,3}` and
`B_i = i S_i`. Confirms the operator-level identification
"internal `su(2)` generators = spatial `Spin(3)` infinitesimal action
on `H_x`".

Block 9 — Record-axiom usage scan. Static-source scan of the parent
note for Record-axiom usage tokens. The check enumerates the phrase
set
`{"I(R_1", "I(R)", "scalar record", "record functional",
"record-readout", "additive record", "additive scalar record",
"MINIMAL_AXIOMS_2026-06-04"}`
and confirms zero matches inside the load-bearing core of the parent
note.

Block 10 — Record-axiom counterfactual. Re-runs Blocks 1-8 inside an
explicit "Record axiom is asserted" outer scope and an explicit
"Record axiom is not asserted" outer scope; verifies that the
operator-identification claims are identical in both runs. The
counterfactual is a tautology at the algebra level (no Record-axiom
content enters any Pauli / Clifford / signed-permutation step), which
is precisely the substantive content of (C1).

Block 11 — Quantum content preservation across memos. Verifies that
the new memo `MINIMAL_AXIOMS_2026-06-04.md` preserves the historical
qubit / `Cl(3,0)` local-algebra wording of `MINIMAL_AXIOMS_2026-05-20.md`
under the explicit name Quantum, and that the Record axiom is a
strictly additive scalar record-readout statement added alongside.

Block 12 — Five-route cross-check on the operator-identification core.
Verifies five independent computations of the same operator data:
(a) `B_1 = (i/2) sigma_1` via direct sympy product;
(b) `S_1 = -i B_1` via the bivector-spin relation;
(c) `U(R(pi/2 about +x)) sigma_2 U^* = sigma_3` via half-angle
construction; (d) `[S_1, S_2] = i S_3` via direct commutator;
(e) `S_1 = sigma_1 / 2` via the Pauli definition.
All five must agree to exact sympy equality.

Total: 12 blocks, with the exact PASS/FAIL count recorded in the
SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline derives
`effective_status`), no status field changes are implied by this PR.
The audit lane decides whether to honor the prior judicial verdict on
the new premise hash; this companion only supplies machine-checkable
evidence on whether the new Record axiom disturbs the load-bearing
operator identification.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
output. Each downstream claim must be examined independently against
the new axiom-set premise hash. Other rows recently axiom-invalidated
under the same hash change are out of scope of this companion; they
are listed in the audit queue's `axiom_premise_changed` cohort and
should be examined separately as the audit lane reaches them.

---

## Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-20.md` citations to `MINIMAL_AXIOMS_2026-06-04.md`.
Both are valid framework axiom memos; the 2026-06-04 memo cites the
2026-05-20 memo as the "local-algebra authority and historical source
for the prior two-axiom wording." A separate citation-migration PR (if
desired) can refresh the parent note's source-column citations; this
companion is independent of that text update and is content-only.

This companion's load-bearing-step invariance observation depends only
on the Quantum content being preserved across the two memos — verified
in Block 11 — and on the Record axiom adding a strictly additive
non-overlapping statement — confirmed by direct reading of
`MINIMAL_AXIOMS_2026-06-04.md` §"Record".

---

## References

- Parent note:
  [`INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md`](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md)
- Parent runner:
  `scripts/internal_external_su2_merger_runner.py`
- Sibling companion (template):
  [`YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-algebra
  content): [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
