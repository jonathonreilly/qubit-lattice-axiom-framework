# Gauge Wilson Isotropy Boundary: Record-Axiom Invariance Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing two-route boundary checks in
[`GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md`](GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md)
are invariant under the 2026-06-04 `minimal_axioms` premise-node note-hash
bump from `1d36a556` to `b8848fc8` caused by Record-axiom adoption. It is
not a new theorem claim, not a status promotion, and not an attempt to
perform re-audit work. If the audit pipeline seeds this file, it is a
meta companion row; the audit lane still sets `audit_status`, and the
pipeline-derived `effective_status` remains downstream of that authority.
**Companion target:** `gauge_wilson_isotropy_boundary_note_2026-05-04`
(parent note
`docs/GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md`).
**Primary companion runner:**
[`scripts/audit_companion_gauge_wilson_isotropy_boundary_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_gauge_wilson_isotropy_boundary_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_gauge_wilson_isotropy_boundary_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_gauge_wilson_isotropy_boundary_record_axiom_invariance_2026_06_04.txt)

```yaml
actual_current_surface_status: companion-only
target_claim_type: meta
trace_class: axiom_premise_restoration_evidence
reachability_to_target: none
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Audit-friendly meta companion: the parent narrow no-go's two load-bearing checks ((B1) Cl(3) pseudoscalar centrality with omega = G_1 G_2 G_3 commuting with each G_i and squaring to -I in the Pauli irrep; and (B2) staggered eta plaquette-product equals -1 on all six orientations xy, xz, xt, yz, yt, zt) are purely exact symbolic linear-algebra and combinatorial-arithmetic statements about Pauli matrices and the standard staggered phases eta_mu(x). Neither uses the Record axiom (additive scalar record-readout functional I(.)); the parent's negative boundary that the two PR #528 routes do not derive orientation-dependent Wilson plaquette coefficients is therefore invariant under the 2026-06-04 minimal_axioms premise hash change 1d36a556->b8848fc8. This companion records that invariance as machine-checkable evidence for the audit lane; it does NOT re-audit and does NOT promote status."
proposal_allowed: false
proposal_allowed_reason: "Meta audit-companion only: no new theorem claim, no status promotion, no edit to audit-lane-owned data. The parent narrow no-go's claim scope, claim type, deps list, and effective_status are untouched. The audit lane decides whether to honor the prior judicial/cross-family verdict pattern on the new premise hash; this companion supplies machine-checkable evidence on whether Record-axiom adoption disturbs the load-bearing two-route checks."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

---

## 0. Why this companion exists

The parent narrow no-go
`gauge_wilson_isotropy_boundary_note_2026-05-04` records the following
route-specific negative boundary on the accepted isotropic Wilson
nearest-neighbor plaquette surface:

> On the accepted Wilson nearest-neighbor plaquette surface, the two
> PR #528 mechanisms checked here do not derive orientation-dependent
> plaquette coefficients. They provide no basis for changing the accepted
> isotropic Wilson action or adding an anisotropy axiom.

The two PR #528 mechanisms attacked in the parent are:

1. **The Cl(3) pseudoscalar as a "fourth Clifford generator."** The parent
   shows `omega = G_1 G_2 G_3` is central in odd-dimensional `Cl(3)` and so
   does not anticommute with the three spatial generators, hence cannot
   supply an independent time-like Clifford direction or a temporal-vs-
   spatial gauge-coupling split. In the Pauli irrep, `omega = i I` and
   `omega^2 = -I`.
2. **The standard staggered eta plaquette-product.** The parent shows that
   for `mu < nu`, the four-factor sign product
   `E_{mu nu}(x) = eta_mu(x) eta_nu(x + e_mu) eta_mu(x + e_nu) eta_nu(x)`
   equals `-1` for every site `x` and every one of the six orientations
   `xy`, `xz`, `xt`, `yz`, `yt`, `zt`. So this mechanism supplies at most
   one common sign on all six plaquette orientations, not a
   spatial/temporal split.

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md`
section 6) changed the stable `minimal_axioms` premise-node note-hash
from `1d36a556` to `b8848fc8`. The audit pipeline correctly invalidated
the prior `audited_clean` snapshot for the parent via
`invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`,
returning the row to its `unaudited` effective status pending re-audit.

This companion records, for the audit lane, that the parent's two
load-bearing route checks **(B1)** and **(B2)** are **independent of
the Record axiom**: they use only the Quantum axiom content (the
one-qubit local algebra `M_2(C) ~= Cl(3,0)`, supplying the three Pauli
generators `G_i = sigma_i`, their anticommutation relations
`{G_i, G_j} = 2 delta_{ij} I`, and the volume element `omega = i I` of
the Pauli irrep) and the Lattice axiom content (the discrete site set
that the staggered phases `eta_mu(x) = (-1)^{x_0 + ... + x_{mu-1}}`
are defined on), plus standard finite-dimensional complex linear
algebra and the elementary combinatorics of binary parity sums.

The Record axiom (additive scalar record-readout `I(R_1 sqcup R_2)
= I(R_1) + I(R_2)`) is neither used nor invoked anywhere in the parent's
two-route argument. The numeric and algebraic outputs (the centrality
relations `[omega, G_i] = 0`, the non-anticommutation `{omega, G_i}
= 2 omega G_i != 0`, the pseudoscalar square `omega^2 = -I`, and the
six orientation-blind eta plaquette values `-1`) are unchanged.

This companion is therefore audit-friendly evidence that the prior
clean (and judicially-reconfirmed) reading of the parent's substantive
content survives the axiom-set change. It is not a re-audit and does
not promote status; it documents the load-bearing-chain dependency
surface in machine-checkable form so the audit lane can decide whether
to honor or re-test the prior verdict pattern on the new premise hash.

---

## 1. Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the Wilson-isotropy boundary's two
route checks.** The parent's load-bearing content — the Cl(3)-pseudoscalar
centrality check (B1) and the staggered-eta plaquette orientation-blindness
check (B2) of §Closed Derivation in
`GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md`, together with the
boundary theorem combining them — depends only on:

1. the one-qubit on-site local operator algebra `M_2(C) ~= Cl(3,0)`
   (Quantum axiom content); in particular, the three Pauli generators
   `sigma_1, sigma_2, sigma_3` with `{sigma_i, sigma_j} = 2 delta_{ij} I`
   and `sigma_i^2 = I`, and their volume element
   `omega = sigma_1 sigma_2 sigma_3 = i I` (centrality of the volume
   element of `Cl(3,0)` is a structural property of odd-dimensional
   Clifford algebras);
2. the `Z^d` discrete site set (Lattice axiom content, here applied at
   `d >= 4` for the spatial-plus-temporal index range `mu in {0,1,2,3}`
   used by the standard staggered-phase definition);
3. the standard staggered-phase function `eta_0(x) = 1`,
   `eta_mu(x) = (-1)^{x_0 + ... + x_{mu-1}}` for `mu > 0`, defined
   coordinatewise on the site set (definition, not a Record-axiom
   consequence);
4. standard finite-dimensional complex linear algebra (matrix
   multiplication, anticommutator computation) and the elementary
   combinatorics of binary parity sums (`eta_mu^2(x) = 1`,
   `eta_mu(x + e_nu) = eta_mu(x) * (-1)^{delta_{nu < mu}}`).

None of items 1-4 use the Record axiom's additive scalar record-readout
content. They use only the Quantum axiom (one-qubit / `M_2(C)` /
`Cl(3,0)` local algebra; the Pauli matrices and their volume element),
the Lattice axiom (`Z^d` site set on which the staggered phases are
indexed), and standard finite-dimensional complex linear algebra and
elementary binary-parity combinatorics cited as admitted-context
mathematical infrastructure in the parent's `Closed Derivation` (§§1-2
of the parent).

**(C1) is the only auditable companion observation.** This companion
does **not** revisit the parent's open future paths in `What This Does
Not Close` of the parent (a future independently audited theorem could
still derive an anisotropic Wilson action from a separately approved
primitive; the analytic plaquette value at `beta = 6` also remains
open); those remain open exactly as the parent states them, on whatever
axiom set is in force at the time they are attacked.

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, deps list, or
  admitted-context inputs;
- assert anything about Record-axiom content or its scope;
- assert that the parent's prior treatment was clean or unclean — it
  merely records that the parent's two load-bearing checks do not
  consume Record content;
- re-audit `gauge_wilson_isotropy_boundary_note_2026-05-04` or any
  other ledger row;
- modify the audit ledger, the audit queue, or any status field;
- promote, demote, or accept any future independently audited
  anisotropy theorem;
- read on the parent's one-hop dependencies
  `gauge_scalar_temporal_completion_theorem_note` (retained accepted
  Wilson grammar with one common plaquette coefficient) or
  `gauge_vacuum_plaquette_constant_lift_obstruction_note` (retained
  no-go on the constant-lift Wilson plaquette reduction) beyond noting
  that the parent cites them as already-retained authorities supplying
  the boundary against which (B1) and (B2) are checked.

The audit lane decides whether (C1) is sufficient evidence to honor
the parent's prior treatment pattern on the new premise hash or
whether a fresh per-route audit is warranted.

---

## 2. The Record axiom is not used by the load-bearing checks

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing checks (B1) and (B2) define no record
surface, ask no question about scalar record additivity, and write no
record functional `I(.)`. They compute:

- **(B1)** the on-site values of the Pauli anticommutation relations
  `{sigma_i, sigma_j} = 2 delta_{ij} I` and self-squares `sigma_i^2 = I`;
  the value of the volume element `omega = sigma_1 sigma_2 sigma_3
  = i I` in the Pauli irrep; the commutator `[omega, sigma_i] = 0`
  (centrality); the anticommutator `{omega, sigma_i} = 2 omega sigma_i
  = 2 i sigma_i != 0` (non-anticommutation); and the irrep square
  `omega^2 = (i I)^2 = -I`. From these, the boundary statement: `omega`
  is central in `Cl(3,0)` so a putative fourth Clifford generator
  satisfying `{T, sigma_i} = 0` cannot be `omega`. The Cl(3) pseudoscalar
  is a central complex-structure element, not a fourth anticommuting
  generator;
- **(B2)** the values of the standard staggered phases `eta_0(x) = 1`,
  `eta_mu(x) = (-1)^{x_0 + ... + x_{mu-1}}` for `mu > 0` on the discrete
  site set; the four-factor plaquette-sign product `E_{mu nu}(x)
  = eta_mu(x) eta_nu(x + e_mu) eta_mu(x + e_nu) eta_nu(x)` for `mu < nu`;
  and the algebraic identities `eta_mu(x + e_nu) = eta_mu(x)` if
  `nu >= mu` (because `eta_mu` only depends on `x_0, ..., x_{mu-1}` and
  `nu >= mu` means `e_nu` does not move those coordinates), and
  `eta_nu(x + e_mu) = -eta_nu(x)` if `mu < nu` (because `eta_nu` does
  depend on `x_mu`). Hence `E_{mu nu}(x) = -eta_mu(x)^2 eta_nu(x)^2
  = -1` for every site `x` and every one of the six orientations
  `xy`, `xz`, `xt`, `yz`, `yt`, `zt`. The eta-product mechanism
  supplies the same factor `-1` on every plaquette orientation: at most
  one common sign, no orientation-dependent split.

The operator content (Pauli `sigma_1, sigma_2, sigma_3`, the volume
element `omega = sigma_1 sigma_2 sigma_3`, the Pauli irrep identification
`omega -> i I`), the on-site `Cl(3,0)` algebra closure with the
centrality identity, the staggered-phase definition, and the binary
parity sum identities are fixed by:

- the one-qubit on-site `M_2(C) ~= Cl(3,0)` algebra (Quantum axiom
  content);
- the `Z^d` site set with the standard staggered phases
  (Lattice axiom content);
- standard finite-dimensional complex linear algebra, tensor products,
  and the Pauli algebra (admitted-context mathematical infrastructure
  cited in the parent's §1-2 derivation chain).

The Record axiom adds an additive scalar record functional. It does
**not** modify (and is not modified by) the Pauli algebra, the volume
element of `Cl(3,0)`, the staggered phases, the binary parity sums, or
the orientation index `{(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)}`. So
the values of all of (B1) and (B2) are invariant under the axiom-set
change. The boundary theorem combining the two route walls is likewise
invariant: each rules out a candidate forcing argument purely from those
finite-dimensional facts and combinatorial-arithmetic identities.

In particular, the Record-axiom scope statement
(`MINIMAL_AXIOMS_2026-06-04.md` §"Record" closing paragraph) explicitly
excludes from the Record axiom's content: "rule for record production,
persistence, measurement/decoherence, Born weights, P2/modulus/phase-
blindness, log-det structure, time arrow, system composition,
normalization/scale, source/action identification, `AC_phi_lambda`,
theta, or arbitrary observable identification." None of those bridges
enter the parent note's two-route load-bearing content either; the
route checks are about the **absence** of (1) a fourth anticommuting
Clifford generator from the central `omega` and (2) an
orientation-dependent staggered-eta plaquette factor, neither of which
is provided or revoked by the additive scalar Record functional.

This invariance is what the companion runner verifies block-by-block:
every load-bearing finite-dimensional check in (B1) and (B2) passes
using only Quantum + Lattice content and standard finite-dimensional
linear algebra and elementary parity arithmetic, and a "Record-axiom
counterfactual" block confirms that all numeric outputs are unchanged
whether or not a Record-axiom statement is appended.

---

## 3. Companion runner block plan

`scripts/audit_companion_gauge_wilson_isotropy_boundary_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the Wilson-isotropy boundary's
two route checks. Each block runs as an independent symbolic / numeric
check; nothing is hard-coded against an expected target value beyond
standard finite-dimensional linear algebra and elementary binary-parity
combinatorics. The runner reports `PASS` / `FAIL` per check; the cached
output records the run.

**Block 1 — Pauli anticommutation `{G_i, G_j} = 2 delta_{ij} I`.**
Verifies the three on-site Clifford `Cl(3,0)` relations in the Pauli
irrep. Uses only the one-qubit `M_2(C)` content; no Record axiom enters.

**Block 2 — On-site Pauli self-squares `G_i^2 = I`.** Verifies the
Clifford diagonal `i = j` case. Uses only the one-qubit `M_2(C)`
content.

**Block 3 — Volume element `omega = G_1 G_2 G_3` in the Pauli irrep.**
Verifies `omega = i I` exactly in the Pauli irrep and `omega^2 = -I`.
Uses only the Pauli matrix products.

**Block 4 — Centrality `[omega, G_i] = 0`.** Verifies the commutator
identity for `i = 1, 2, 3`. This is the load-bearing fact that `omega`
cannot be a fourth anticommuting Clifford generator.

**Block 5 — Non-anticommutation `{omega, G_i} = 2 omega G_i != 0`.**
Verifies that the candidate anticommutator is nonzero for every `i`,
ruling out `omega` as a Cl(3,1)-style fourth generator `T` with
`{T, G_i} = 0`.

**Block 6 — Pseudoscalar-as-fourth-generator wall.** Confirms the
combined logical statement: a fourth Clifford generator `T` with
`{T, G_i} = 0` for all three spatial generators cannot equal `omega`,
because `omega` commutes with each `G_i` (Block 4) and so its
anticommutator with `G_i` is `2 omega G_i != 0` (Block 5).

**Block 7 — Staggered-phase definition `eta_mu`.** Verifies the
standard definition `eta_0(x) = 1`, `eta_mu(x) = (-1)^{x_0 + ... +
x_{mu-1}}` for `mu = 1, 2, 3` and `eta_mu(x) in {-1, +1}` for every
sampled site on a sufficiently large parity cube.

**Block 8 — Staggered-phase squares `eta_mu(x)^2 = 1`.** Verifies the
elementary identity used in the eta-product reduction. Uses only the
parity-sum definition.

**Block 9 — Coordinate-shift identity for `eta_mu` under `e_nu`.**
Verifies `eta_mu(x + e_nu) = eta_mu(x)` when `nu >= mu` (because
`eta_mu` depends only on `x_0, ..., x_{mu-1}`) and
`eta_mu(x + e_nu) = -eta_mu(x)` when `nu < mu`. This is the
combinatorial input to the orientation-blind plaquette-product result.

**Block 10 — Staggered eta plaquette product `E_{mu nu}(x) = -1` on
all six orientations.** Verifies the four-factor sign product
`E_{mu nu}(x) = eta_mu(x) eta_nu(x + e_mu) eta_mu(x + e_nu) eta_nu(x)`
equals `-1` for every `mu < nu in {(0,1), (0,2), (0,3), (1,2), (1,3),
(2,3)}` and every site `x` in a parity-cube sample. This is the
load-bearing orientation-blindness fact.

**Block 11 — Orientation-blindness boundary statement.** Confirms the
combined logical statement: every one of the six plaquette orientations
yields the same `E_{mu nu}(x) = -1`, so the eta-product mechanism
supplies at most one common sign and no spatial/temporal split.

**Block 12 — Static-source scan of parent note.** Reads the parent
note's load-bearing structural section (`## Closed Derivation` through
the end of `### Boundary theorem`) and confirms zero occurrences of
Record-axiom usage tokens. The token set scans for `{"I(R_1", "I(R)",
"scalar record", "record functional", "record-readout", "additive
record", "additive scalar record", "MINIMAL_AXIOMS_2026-06-04"}` over
the load-bearing core. Confirms zero matches.

**Block 13 — Record-axiom counterfactual.** Re-runs the symbolic core
of Blocks 1-11 inside an explicit "Record axiom is asserted" outer
scope and an explicit "Record axiom is not asserted" outer scope;
verifies that every load-bearing value (the Pauli anticommutators, the
`omega = i I` value, the `omega^2 = -I` value, the centrality
identities, the non-anticommutators, the staggered-phase squares,
the coordinate-shift identities, and the six orientation-blind plaquette
sign products) is identical in both runs. The counterfactual is a
tautology at the calculation level (no Record-axiom content enters the
symbolic linear algebra or the parity arithmetic), which is precisely
the substantive content of (C1).

**Block 14 — Quantum / Lattice content preservation across the two
memos.** Reads `MINIMAL_AXIOMS_2026-05-20.md` and
`MINIMAL_AXIOMS_2026-06-04.md` and confirms that (a) the one-qubit
local-algebra content used by the parent (per-site `M_2(C) ~=
Cl(3,0)`) is present in both memos under the historical wording and
the new "Quantum" name; (b) the `Z^d` site set with discrete
nearest-neighbor adjacency (used to index the staggered phases) is
present in both; (c) the Record axiom in the new memo asserts only
additive scalar record-readout and explicitly excludes "log-det
structure", "source/action identification", "rule for record
production", "P2/modulus/phase-blindness", "Born weights", and related
bridges from its scope; (d) none of those excluded bridges are
load-bearing in the parent note's two-route argument.

**Block 15 — Parent runner-output preservation.** Confirms that the
exact summary line of the parent's paired runner
`scripts/frontier_gauge_wilson_isotropy_boundary_2026_05_04.py` —
namely `SUMMARY: PASS=19 FAIL=0` — is preserved under the new memo:
the symbolic Pauli/staggered checks performed by the parent runner are
the same finite-dimensional checks verified here in Blocks 1-11,
producing the same outputs regardless of which `minimal_axioms` memo
is loaded.

Total: 15 blocks. The exact PASS/FAIL count is recorded in the cached
runner output.

---

## 4. Cited authorities (one hop)

Load-bearing (markdown-linked):

- **Parent narrow no-go.**
  [`GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md`](GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md):
  the two PR #528 mechanisms do not derive orientation-dependent
  Wilson plaquette coefficients on the accepted isotropic Wilson
  surface.
- **New framework axioms.**
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md):
  Quantum one-qubit local algebra, `Z^3` Lattice, and Record additive
  scalar readout (the third explicitly approved premise; the only
  premise this companion addresses).
- **Predecessor framework axioms (still authoritative for local-algebra
  and `Z^3` content):**
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md).
- **Axiom-minimality policy and explicit-owner-approval ledger:**
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md).
- **Audit lane authority statement:**
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md).
- **Audit pipeline ground rules:**
  [`docs/audit/README.md`](audit/README.md).

Plain-text / backtick reader pointers (non-load-bearing):
`GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md` (one-hop dep:
retained accepted Wilson nearest-neighbor grammar with one common
plaquette coefficient), `GAUGE_VACUUM_PLAQUETTE_CONSTANT_LIFT_OBSTRUCTION_NOTE.md`
(one-hop dep: retained no-go on the constant-lift Wilson plaquette
reduction), `scripts/frontier_gauge_wilson_isotropy_boundary_2026_05_04.py`
(the parent's own paired runner, whose 19 PASS / 0 FAIL the present
companion does not consume as load-bearing — it independently rederives
the same symbolic and combinatorial facts).

No PDG values, fitted selectors, scale, mass input, `g_bare`,
lattice-action carrier, or literature-comparator load-bearing
consumption. The Clifford-algebra structure and the staggered-phase
definition are textbook **mathematical infrastructure** cited by name
in the parent's `Closed Derivation` (and previously verified by
multiple independent auditors as such; see the parent's
`previous_audits` cross-confirmation panel).

---

## 5. Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline
derives `effective_status`), no status field changes are implied by
this PR.

The audit lane decides whether to honor the prior treatment of the
parent no-go on the new premise hash; this companion only supplies
machine-checkable evidence on whether the new Record axiom disturbs
the load-bearing two-route checks. The Record-axiom-invariance
observation here is structurally narrow: it does not extend to any
downstream claim that consumes the parent's output, and it does not
re-open or pre-close the parent's `What This Does Not Close` future
paths.

Other rows recently axiom-invalidated under the same hash change
remain out of scope of this companion; they are listed in the audit
queue's `axiom_premise_changed` cohort and should be examined
separately as the audit lane reaches them.

---

## 6. Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-20.md` citations to
`MINIMAL_AXIOMS_2026-06-04.md`. Both are valid framework axiom memos;
the 2026-06-04 memo cites the 2026-05-20 memo as the predecessor
explicit-owner-approved axiom set. A separate citation-migration PR
(if desired) can refresh the parent note's `Qubit-Reframe Grounding`
section pointers; this companion is independent of that text update
and is content-only.

This companion's load-bearing-step invariance observation depends only
on the Quantum and Lattice content being preserved across the two
memos — verified in Block 14 — and on the Record axiom adding a
strictly additive non-overlapping statement — confirmed by direct
reading of `MINIMAL_AXIOMS_2026-06-04.md` §"Record" and its
scope-exclusion list.

---

## References

- Parent note:
  [`GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md`](GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md)
- Parent runner:
  `scripts/frontier_gauge_wilson_isotropy_boundary_2026_05_04.py`
- Prior treatment snapshot:
  `docs/audit/data/audit_ledger.json` row
  `gauge_wilson_isotropy_boundary_note_2026-05-04`,
  `previous_audits[-1]` with
  `invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms:
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
