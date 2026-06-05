# Scalar-Trace Tensor Completion No-Go: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise invariance evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing same-scalar-data/distinct-tensor-channel witness in
[`SCALAR_TRACE_TENSOR_NO_GO_NOTE.md`](SCALAR_TRACE_TENSOR_NO_GO_NOTE.md)
is invariant under the 2026-06-04 Record-axiom adoption. It is not a
new theorem claim, not a status promotion, and not an attempt to
perform re-audit work. If the audit pipeline seeds this file, it is a
meta companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that
authority.
**Companion target:** `scalar_trace_tensor_no_go_note` (parent note
`docs/SCALAR_TRACE_TENSOR_NO_GO_NOTE.md`).
**Primary companion runner:**
[`scripts/audit_companion_scalar_trace_tensor_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_scalar_trace_tensor_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_scalar_trace_tensor_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_scalar_trace_tensor_record_axiom_invariance_2026_06_04.txt)

---

## Why this companion exists

The parent note `scalar_trace_tensor_no_go_note` is a conditional
no-go (bounded_theorem author hint; load-bearing score 7.17) ruling
out completion principles that factor only through the current scalar
shell trace / Schur boundary data on the configured `O_h` and
finite-rank witness classes. The most recent archived audit
(2026-05-11, `audited_conditional`) recorded `PASS=6 FAIL=0` against
the (then) ledger state, with the conditional verdict driven not by
the algebra of the no-go but by the runner's `_frontier_loader`
imports of the scalar-functional, probe-family, and Einstein-residual
modules. The current ledger row is `unaudited` (with the prior
conditional verdict archived).

The 2026-06-04 framework axiom update from
`MINIMAL_AXIOMS_2026-05-20.md` to `MINIMAL_AXIOMS_2026-06-04.md`
(Lattice + Quantum + Record; explicit-owner-approved per
`docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6) changed the stable
`minimal_axioms` premise-node note-hash from `1d36a556` to
`b8848fc8`. As the audit lane re-examines this row on the new premise
hash, this companion records, for the audit lane, that the parent's
load-bearing observation is **independent of the Record axiom**: the
same-scalar-data invariance and the distinct-tensor-channel witness
use only the standard Riemannian-geometry / Schur-complement
constructions of the imported runner modules. Adopting the Record
axiom adds a strictly additive scalar record-readout statement, which
is neither used nor invoked anywhere in the scalar action, the probe
families, or the Einstein-tensor channel computation. The conclusion
("no completion principle that factors only through the current
scalar shell trace / Schur data can determine the full `3+1` metric
on this branch") is unchanged.

This companion is therefore audit-friendly evidence that the prior
conditional verdict's substantive content survives the axiom-set
change. It is not a re-audit and does not promote status; it
documents the load-bearing-step dependency surface in machine-checkable
form so the audit lane can decide whether to honor or re-test the
prior verdict on the new premise hash. It also does not address the
parent's separate, longstanding `missing_dependency_edge` repair path
(retained-grade promotion of the three imported runner authorities or
inlining their constructions), which remains the parent's named
non-Record-axiom open admission.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the scalar-trace-only completion
no-go witness.** The parent's load-bearing step — same scalar
boundary action under scalar / vector / tensor / mixed perturbations,
together with nonzero independent `G_{0i}` and traceless `G_{ij}`
Einstein-tensor residuals — depends only on:

1. the Schur-complement boundary functional
   `S_bdry[f] = (1/2) f^T Λ f − j^T f` of a scalar `f` over the
   `O_h` and finite-rank probe grids (parent §"Exact statement");
2. the explicit vector-shift, traceless-shear, and mixed perturbation
   families that hold the scalar boundary data `f` fixed by
   construction (parent §"Tensorial witness");
3. the standard ADM metric reconstruction, Christoffel/Ricci/Einstein
   numerical evaluation on those probes (parent §"Tensorial witness",
   imported via `frontier_tensorial_einstein_regge_completion.py`).

None of items 1-3 use the Record axiom's additive scalar
record-readout content. They use only the imported scalar
boundary-functional construction, the imported probe-family
definitions, and standard Riemannian-geometry numerical derivatives.
The "additive scalar functional `I(R)` over disjoint record
collections" content added by the Record axiom is not referenced in
any equation, identity, or numerical step that produces the no-go.

**(C1) is the only auditable companion observation.** All other
content of the parent — the imported scalar-functional authority, the
imported probe-family authority, the imported Einstein-residual
authority, and the parent's explicit `notes_for_re_audit_if_any`
repair path — is out of scope of this companion.

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs (the conditional-on-imports witness on the `O_h` and
  finite-rank classes);
- assert anything about Record-axiom content or its scope;
- discharge the parent's `missing_dependency_edge` repair path; the
  three imported runner authorities and their retained-grade promotion
  remain a separate, non-Record-axiom open repair;
- re-audit `scalar_trace_tensor_no_go_note` or any other ledger row;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1) is sufficient evidence to re-honor
the previous conditional verdict on the new premise hash or whether a
fresh per-site audit is warranted.

---

## The Record axiom is not used by the load-bearing step

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing step defines no record surface, asks no
question about scalar record additivity, and writes no record
functional `I(.)`. It computes:

- a scalar boundary action `S_bdry[f] = (1/2) f^T Λ f − j^T f`
  evaluated on two scalar `phi`-grid families (`O_h` symmetric class
  and finite-rank class), where `Λ` and `j` are produced by the
  imported `frontier_oh_schur_boundary_action.schur_dtn_matrix(...)`
  Schur Dirichlet-to-Neumann construction;
- four perturbation labels (`scalar bridge`, `vector shift`,
  `tensor shear`, `mixed`) on each `phi`-grid, with vector and tensor
  modes constructed from the imported envelope, the imported
  rotational shift mode, and the imported traceless quadrupole mode
  acting on the spatial metric. The vector and tensor modes are
  designed to leave the scalar boundary data `f` (computed from the
  scalar `phi`-grid) unchanged;
- the full 4D Einstein tensor `G_{μν}` numerically at shell-adjacent
  probe points using the standard ADM metric reconstruction,
  Christoffel symbols, Ricci tensor, and the trace-reversed
  Einstein-tensor formula;
- four scalar summaries per probe: the scalar boundary action, and
  the maxima `|G_{tt}|`, `|G_{ti}|`, `|G_{ij}^{TF}|` of the
  Einstein-tensor components.

The Record axiom adds an additive scalar record functional. It does
not modify (and is not modified by) the Schur boundary functional,
the perturbation modes, the ADM metric reconstruction, the
Christoffel/Ricci/Einstein numerical derivatives, or the maximum-norm
summaries. So the same-scalar-data invariance and the
distinct-tensor-channel witness are invariant under the axiom-set
change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic check passes using only standard
finite-dimensional / Schur / Riemannian-geometry content, and a
"Record-axiom counterfactual" block confirms that the no-go verdict
is unchanged whether or not a Record-axiom statement is appended.

---

## Companion runner block plan

`scripts/audit_companion_scalar_trace_tensor_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the scalar-trace-only
completion no-go witness. Each block runs as an independent
numeric/algebraic check; no block hard-codes the expected target
beyond standard finite-dimensional algebra. The runner reports
`PASS` / `FAIL` per check; the cached output records the run.

The runner is deliberately self-contained: it does **not** import
`_frontier_loader` or the three upstream `frontier_*` modules. It
reproduces the load-bearing structural ingredients (Schur
boundary-action shape, vector-mode and traceless-quadrupole
constructions, ADM metric reconstruction, Christoffel and Einstein
tensor) as standalone reference implementations on small explicit
grids and small explicit ansätze, and verifies the structural
properties the parent's no-go relies on. This isolates the companion
from the parent's separate `missing_dependency_edge` admission about
those imports.

Block 1 — Schur-functional bilinear structure. Verifies that a
representative symmetric positive-semidefinite Dirichlet-to-Neumann
`Λ` and source `j` produce a scalar boundary action `(1/2) f^T Λ f −
j^T f` whose value depends only on `f` (not on the spatial bulk or
the perturbation labels). Confirms the structural property used by
the parent's "scalar boundary action is unchanged across the scalar,
vector, tensor, and mixed perturbations" claim.

Block 2 — Vector-mode divergence structure. Constructs the rotational
shift mode `β(x,y,z) = (−y, x, 0) / r^2` used in the parent's vector
perturbation and verifies it has zero radial component
(`x β_x + y β_y + z β_z ≡ 0`) at every off-axis test point, so it
does not perturb a spherically symmetric scalar `f(r)`.

Block 3 — Traceless-quadrupole structure. Constructs the
traceless-shear quadrupole mode
`q_ij = n_i n_j − (1/3) δ_ij` from the radial unit vector and
verifies (i) symmetry `q_ij = q_ji`, (ii) zero trace `q_ii = 0` to
machine precision, on a sample of off-axis test points. Both
properties are load-bearing for the parent's "scalar boundary data
unchanged" claim under tensor perturbation.

Block 4 — ADM metric reconstruction sanity. Builds the full 4×4 ADM
metric `g_{μν}` from a conformal lapse-and-spatial-metric pair `(α,
γ_ij)` plus shift `β^i` and tensor perturbation `h_ij`, and verifies
that (i) the time-time block reduces to `g_{00} = −α^2 + β·γβ`,
(ii) the spatial block is symmetric, (iii) the off-diagonal `g_{0i}`
equals `γ_{ij} β^j` exactly. These are textbook ADM relations,
reproduced standalone here.

Block 5 — Einstein tensor of flat space. Builds the Christoffel
symbols and Ricci tensor of flat Minkowski space (constant identity
metric) via the standard finite-difference scheme used in the parent
runner and verifies all Christoffel symbols and all Ricci components
vanish to numerical precision, and the Einstein tensor is zero. This
checks the parent runner's `christoffel` / `ricci_and_einstein`
algebra independently.

Block 6 — Einstein tensor channel separation. Constructs a small
analytic perturbation `h_{ij}(x,y,z) = ε · (n_i n_j − δ_ij/3) · f(r)`
on a flat background and verifies that the resulting Einstein tensor
has (i) zero `G_{00}` at leading order in `ε`, (ii) nonzero traceless
`G_{ij}^{TF}` at order `ε`, (iii) `G_{ti} = 0` at this order (since
`h_{ij}` is purely spatial and static). This reproduces the
structural channel-separation argument the parent uses to claim the
tensor perturbation activates the traceless spatial Einstein channel
without disturbing the scalar boundary data.

Block 7 — Shift-vector Einstein channel separation. Constructs a
small time-dependent shift `β^i(t,x,y,z) = ε · sin(ω t) · η(r) ·
β_rot^i` with rotational `β_rot` and verifies that the resulting
Einstein tensor has nonzero `G_{0i}` at order `ε` and zero traceless
`G_{ij}^{TF}` at leading order in `ε`. This reproduces the structural
channel-separation argument the parent uses to claim the vector
perturbation activates the `G_{0i}` Einstein channel without
disturbing the scalar boundary data.

Block 8 — Same-scalar-data invariance (witness). On an explicit small
scalar `phi`-grid, computes the scalar boundary action under
unperturbed, vector-shift, tensor-shear, and mixed perturbations
(with the shift and shear constructed so they leave the underlying
scalar `phi`-grid unchanged) and verifies all four scalar actions are
bit-for-bit identical. This is the structural content of the parent's
"the scalar boundary action is unchanged across the scalar, vector,
and tensor perturbations" claim, reproduced standalone.

Block 9 — Static-source scan of parent note. Reads
`docs/SCALAR_TRACE_TENSOR_NO_GO_NOTE.md` and confirms that the
load-bearing structural section (between the `## Exact statement`
heading and the `## What still remains open` heading) contains zero
Record-axiom tokens (`I(R_1`, `I(R)`, `scalar record`,
`record functional`, `record-readout`, `additive record`,
`additive scalar record`, `MINIMAL_AXIOMS_2026-06-04`). Confirms
that the Schur boundary-data, tensorial-witness, and Einstein-tensor
content **is** present (`scalar shell trace`, `Schur`,
`tensorial Einstein`, `vector-shift`, `traceless shear`).

Block 10 — Static-source scan of parent runner. Reads
`scripts/frontier_scalar_trace_tensor_nogo.py` and confirms zero
Record-axiom tokens in the load-bearing source, while confirming
the structural-witness tokens (`scalar_action`, `e_ti`,
`e_spatial_tf`, `vector shift`, `tensor shear`, `mixed`) are present
as the load-bearing checks.

Block 11 — Record-axiom counterfactual. Re-runs Blocks 1, 6, 7, 8
inside an explicit "Record axiom is asserted" outer scope and an
explicit "Record axiom is not asserted" outer scope; verifies that
the same-scalar-data invariance, the `G_{0i}` activation, the
traceless `G_{ij}^{TF}` activation, and the no-go verdict
(`same scalar data, distinct tensor channels`) are bit-for-bit
identical in both runs. The counterfactual is a tautology at the
calculation level (no Record-axiom content enters the
Schur-functional / probe / Einstein-residual steps), which is
precisely the substantive content of (C1).

Block 12 — Quantum/Lattice content preservation across memos.
Verifies that the Quantum and Lattice content statements of
`MINIMAL_AXIOMS_2026-05-20.md` (one-qubit local algebra and `Z^3`
cubic lattice) are preserved in `MINIMAL_AXIOMS_2026-06-04.md` under
the explicit names Quantum and Lattice. Verifies that the
2026-06-04 memo states the Record axiom is additive in scalar
record-readout content over disjoint record collections, and
explicitly disclaims that Record supplies log-det / source / action
/ measurement-rule / Born / observable / scale content (none of which
are used by the parent no-go's load-bearing step in any case).

Block 13 — Channel-distinctness summary. Re-states the no-go's
logical structure in machine-checkable form: if scalar boundary
action is invariant under three perturbation labels (vector shift,
tensor shear, mixed) AND the Einstein-tensor channels `(G_{0i},
G_{ij}^{TF})` are nonzero on those same perturbations, then any
completion principle factoring only through the scalar boundary
action assigns the same value to physically distinct completions —
i.e., the parent's "no scalar-trace-only completion can determine
the full `3+1` metric" conclusion. Verifies that the booleans
computed in Blocks 6-8 satisfy the precondition of this implication.

Block 14 — Four-route cross-check on the no-go boolean. Computes the
no-go verdict four independent ways: (i) directly from Blocks 6-8
booleans; (ii) from a flat-background analytic check with the same
modes evaluated at three different probe radii; (iii) under the
Record-axiom-asserted outer scope of Block 11; (iv) under the
Record-axiom-not-asserted outer scope of Block 11. Verifies all four
agree.

Total: 14 blocks, with the exact PASS/FAIL count recorded in the
SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline
derives `effective_status`), no status field changes are implied by
this PR.

The audit lane decides whether to re-honor the prior conditional
verdict on the new premise hash; this companion only supplies
machine-checkable evidence on whether the new Record axiom disturbs
the load-bearing step. It explicitly does not address the parent's
separate `notes_for_re_audit_if_any` repair path
(`missing_dependency_edge` — attach retained-grade notes for the
three imported runner authorities or inline their constructions),
which is a pre-existing, non-Record-axiom audit gap.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
output. Each downstream claim must be examined independently against
the new axiom-set premise hash. The other rows axiom-invalidated
under the same hash change are out of scope of this companion; they
are listed in the audit queue's `axiom_premise_changed` cohort and
should be examined separately as the audit lane reaches them.

---

## Audit-ordering and integration

This companion does not migrate the parent's existing axiom
citations (the parent does not cite a specific `MINIMAL_AXIOMS_*.md`
file by name; it cites no minimal-axiom memo directly). The parent's
text content is unchanged by this PR.

This companion's load-bearing-step invariance observation depends
only on the Quantum and Lattice content being preserved across the
two memos — verified in Block 12 — and on the Record axiom adding a
strictly additive non-overlapping statement — confirmed by direct
reading of `MINIMAL_AXIOMS_2026-06-04.md` §"Record".

---

## References

- Parent note:
  [`SCALAR_TRACE_TENSOR_NO_GO_NOTE.md`](SCALAR_TRACE_TENSOR_NO_GO_NOTE.md)
- Parent runner:
  `scripts/frontier_scalar_trace_tensor_nogo.py`
- Prior conditional verdict snapshot:
  `docs/audit/data/audit_ledger.json` row
  `scalar_trace_tensor_no_go_note`, `previous_audits[-1]`
  (`audited_conditional`, `no_go`, class B, `cross_family`,
  2026-05-11, archived 2026-05-18; conditional driver:
  `missing_dependency_edge` for the three imported runner
  authorities, which remains a separate, non-Record-axiom open
  repair)
- Template companion (this PR mirrors PR #2616's pattern):
  [`YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-algebra
  content):
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit-lane README (auditor sets `claim_type` and `audit_status`;
  pipeline derives `effective_status`):
  [`docs/audit/README.md`](audit/README.md)
