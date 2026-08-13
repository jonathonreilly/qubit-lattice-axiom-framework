---
claim_id: smallest_complete_born_extra_is_occupancy_menu_kernel_triple_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-site window with one shared one-site law and a unit record, dropping occupancy, dropping the outcome menu, or dropping the trace kernel each fails to produce a Born number at a named formed site. The displayed triple (occupancy, menu, kernel) separates those three failures and is therefore a lower bound, up to relabeling, on any complete extra with that output type. The triple is displayed only; no axiom is edited and no frame-function theorem is imported."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/smallest_complete_born_extra_is_occupancy_menu_kernel_triple_2026_08_13.py
---

# Smallest Complete Born Extra Is The Occupancy-Menu-Kernel Triple

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite algebra on a two-site window and two binary
projective menus; a completeness lower bound for extras that emit a Born
number at a named formed site.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/smallest_complete_born_extra_is_occupancy_menu_kernel_triple_2026_08_13.py`](../scripts/smallest_complete_born_extra_is_occupancy_menu_kernel_triple_2026_08_13.py)

Parent mathematical surface (ledger `effective_status: unaudited`; used only
as the named display of a trace form after a supplied grade, not as a
ratified premise):
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md).

Current axiom wording:
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

A compiler that is supposed to emit a Born number at a named formed site
needs three independent pieces of extra data beyond the current axiom
sentences and a unit record:

1. occupancy `o`, which names the formed site;
2. a menu `M`, which names the outcome list;
3. a kernel `K`, which assigns the number.

On the two-site window below, the same one-site law and the same unit
record count are compatible with two different formed sites; the same
density is compatible with two different binary menus and two different
kernel values; and the record count is not the kernel value. Any complete
extra that produces a Born number at a named site must distinguish those
three failures, so it is at least as fine as the triple `(o, M, K)` up to
relabeling.

The triple is displayed. This note does not add an axiom. Do not import
Gleason. The computed kernel value `1/2` on the `x` menu is not a selected
parameter.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
target_claim_id: smallest_complete_born_extra_occupancy_menu_kernel_triple
target_blocker_text: "name the smallest complete extra that produces a Born number at a named formed site"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Derive occupancy, a physical menu, and a kernel from present structure, or keep the triple as an explicit open extra."
conditional_surface_status: "exact finite-window completeness lower bound; extras remain undisplayed by the four axioms"
hypothetical_axiom_status: "candidate consequence map only; no canonical axiom edit"
admitted_observation_status: null
claim_type_reason: "The three drop-one failures and the triple lower bound are exact on declared finite objects, while physical derivation of occupancy, menu, and kernel remains open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `W={x,y}` be a two-site window in the cubic lattice. The same one-site
law on the two labeled local possibilities `{A,B}` is the supplied input

`μ(A)=3/5`, `μ(B)=2/5`.

Occupancy is a map

`o:W→{0,1}`.

Write `o10` for the occupancy with `o(x)=1`, `o(y)=0`, and `o01` for
`o(x)=0`, `o(y)=1`. Each is a unit occupancy: exactly one site of `W` is
occupied.

The two binary projective menus are

`M_z={P_z, I−P_z}`, `M_x={P_x, I−P_x}`,

with

`P_z=diag(1,0)`, `P_x=(I+σ_x)/2`.

Explicitly,

`P_x=((1/2,1/2),(1/2,1/2))`.

The displayed density matching the supplied law in the `z` eigenbasis is

`ρ=diag(3/5,2/5)`.

The kernel is the trace pairing

`K(ρ,P)=Tr(ρ P)`.

A compiler, in this note, is a map that is supposed to emit a Born number
at a named formed site from the displayed extra. Record scalar readout `I`
of a unit lock is `1`, by finite additivity and `I(empty)=0`.

These objects are declared inputs or finite algebra. The four axioms name
neither a formation-site rule, nor an outcome menu, nor a trace kernel.
The August 9 parent, still `unaudited` on the ledger, is cited only as the
named surface on which a menu-independent grade on a declared eligible
family becomes a unique density-matrix trace form. That parent is not
re-proved here, and its named frame-function input is not used.

## Proof-Obligation Graph

| Obligation | Role | Disposition |
|---|---|---|
| two unit occupancies share `μ` and `I=1` | drop occupancy | Theorem 1, exact |
| the two menus are resolutions of `I` and give distinct kernel values | drop menu | Theorem 2, exact |
| unit-lock `I` differs from `K(ρ,P_z)` | drop kernel | Theorem 3, exact |
| any complete extra separates the three failures | lower bound | Theorem 4, finite-witness |
| display the triple without axiom change or frame-function import | hygiene | Theorem 5 |
| derive `o`, `M`, or `K` from present axioms | autonomous closure | open |

## Theorem 1 (drop occupancy)

The occupancies `o10` and `o01` each lock exactly one site. Finite Record
additivity therefore assigns both the same unit-lock readout `I=1`. Both
carry the same supplied law `μ`. Their formed sites differ:

`formed(o10)={x}`, `formed(o01)={y}`.

Without occupancy the compiler has no formed site. The pair `(μ,I)` does
not name the site.

## Theorem 2 (drop menu)

Both menus are binary resolutions of the identity:

`P_z+(I−P_z)=I`, `P_x+(I−P_x)=I`.

The kernel values are

`K(ρ,P_z)=Tr(diag(3/5,2/5) diag(1,0))=3/5`

and

`K(ρ,P_x)=Tr(ρ P_x)`.

The product is

`ρ P_x=((3/10,3/10),(1/5,1/5))`,

so

`K(ρ,P_x)=3/10+1/5=1/2`.

Thus

`K(ρ,P_z)=3/5 ≠ 1/2=K(ρ,P_x)`.

Without a menu the compiler has no outcome list, and the same density does
not determine a single number.

## Theorem 3 (drop kernel)

A unit lock has record count `I=1`. The displayed kernel value on `P_z` is
`3/5`. Therefore

`I=1 ≠ 3/5`.

Record count is not the kernel. The pair `(μ,I)` does not determine the
Born number.

## Theorem 4 (completeness lower bound)

The triple `(o, M, K)` assigns a site, a menu, and a number:

- occupancy selects the formed site in `W`;
- the menu selects the outcome list;
- the kernel assigns `K(ρ,P)` to each listed outcome.

Any complete extra that produces a Born number at a named site must
distinguish the three failures of Theorems 1--3. If it failed to distinguish
`o10` from `o01`, it would lack a formed site. If it failed to distinguish
`M_z` from `M_x`, it would lack an outcome list and would identify `3/5`
with `1/2`. If it failed to distinguish `I` from `K`, it would emit the
record count in place of the Born number. Therefore every such complete
extra is at least as fine as the triple, up to relabeling of the three
coordinates.

This is a finite-witness lower bound on extras with that output type. It is
not a classification of every encoding, and it is not a derivation of any
coordinate from the axioms.

## Theorem 5 (display only)

Display the triple; do not add an axiom. Do not import Gleason. Do not
select the computed value `1/2` as a parameter. The four axioms still
supply no formation-site rule, no outcome menu, and no trace kernel. The
August 9 parent still requires a supplied grade and an eligible menu
family before it produces a unique trace form; that parent remains
`unaudited` and is not consumed as a frame-function proof.

## Hostile Predicates

The predicate "`(μ,I)` determines the Born number and site" fails by
Theorems 1 and 3: `o10` and `o01` share `μ` and `I=1` while naming
different sites, and `I=1` is not `K(ρ,P_z)=3/5`.

The predicate "`K(ρ,P_z)=K(ρ,P_x)`" fails by Theorem 2.

## No-Go Discipline Gate

The negative claims are only the three drop-one failures and the lower
bound on extras with the stated output type. They are not a global Born
impossibility claim.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Use `(μ,I)` alone | identify the formed site and the Born number with the law and the unit-lock count | Theorems 1 and 3 separate site and number from `(μ,I)` | **ATTEMPTED** |
| Omit the menu | evaluate the kernel on an unnamed projector | Theorem 2 gives `3/5 ≠ 1/2` | **ATTEMPTED** |
| Identify `I` with `K` | treat scalar record count as the Born number | Theorem 3, `1 ≠ 3/5` | **ATTEMPTED** |
| Collapse occupancy into the law | let the same `μ` on `{A,B}` name the site | both occupancies carry the same `μ` | **ATTEMPTED** |
| Collapse the menu into `ρ` | let one density name one number | the same `ρ` yields two kernel values | **ATTEMPTED** |
| Derive the triple from the four axioms | occupancy from Record formation, menu from Admissibility, kernel from Qubit | not attempted; the axioms do not name those maps | **LIVE** |
| Finer extra | add further labels beyond `(o,M,K)` | compatible with Theorem 4, which is a lower bound | **LIVE** |

The last two routes remain open. The broad statement that no extra can
ever produce a Born number is not shipped.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| occupancy / menu | no: a formed site names no outcome list | no: a menu names no formed site | independent |
| occupancy / kernel | no: a site does not assign `Tr(ρ P)` | no: a number does not name the site | independent |
| menu / kernel | no: a list of projectors does not evaluate them | no: a number does not name the list | independent |

The three drop-one witnesses therefore do not collapse to one wall.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| window `W={x,y}` | declared two-site test window, not a lattice-wide dynamics |
| `μ(A)=3/5`, `μ(B)=2/5` | supplied one-site law; not derived |
| `ρ=diag(3/5,2/5)` | displayed density matching that law in the `z` basis; not derived |
| occupancy `o` | declared extra, not axiom content |
| menus `M_z`, `M_x` | declared binary projective resolutions |
| kernel `K(ρ,P)=Tr(ρ P)` | declared pairing; identity gates compute it |
| unit-lock `I=1` | Record additivity on one lock |
| August 9 parent | named unaudited display surface; frame-function step unused |
| observations or fits | none |

No continuity, typicality, or hidden frame-function hypothesis is used.

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | neighbor-determined distribution sentence; Record additivity with `I(empty)=0`; open formation-site and probability-value gates | exact current wording only |
| [`docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md) | named unique trace form after a supplied menu-independent grade | display parent only; ledger `effective_status: unaudited`; frame-function step unused |

The new arithmetic — occupancy split, the two kernel values, and
`I ≠ K` — is proved here and checked by the runner.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | two occupancies, two menus, two kernel values, one unit lock | no classification of every map from laws to numbers |
| per site | two named sites in one window | no composite-carrier theorem |
| per mode | not used | no spectral exhaustion |
| per block | the drop-one extra block only | no complete Born/Record/history closure |
| lattice-wide | not executed | no lattice-wide no-go |

The runner emits `per_element`, `per_site`, `per_mode`, `per_block`, and
`lattice_wide` lines.

### N6 — live partial-closure paths

1. A formation-site rule could derive occupancy from neighboring records.
2. A physical instrument encoded in neighbors could derive a menu.
3. A constructed effect-functional grade on an eligible family could, with
   the August 9 parent, supply a kernel after that parent is independently
   available; this note does not perform that step.
4. Record dynamics could generate exclusive outcome events whose additive
   readout is not the kernel but still feeds a later pairing.
5. A finer extra may add labels, provided it still refines `(o, M, K)`.

The approved primitives were checked in
`docs/audit/data/axiom_premise_nodes.json`. Scale reference is units
conversion only. Kinetic isotropy is the kinetic-form ratio only.
Realized state is pointwise evaluation only. None supplies occupancy, a
menu, or a kernel, and none is counted as an extra wall.

### N7 — hostile steelman

> The current axioms already name sites, a possibility domain, a
> distribution, and a unit record. Perhaps the formed site is the site
> that happens to carry the record, the menu is the support of `μ`, and
> the number is `μ` itself, so no extra is required.

The steelman is accepted as a live constructive program and rejected as
an identification on the present objects. Record says that a record locks
one available possibility when present; it does not name which site of a
window forms when two sites share the same law. The support `{A,B}` is
not a choice between `M_z` and `M_x`. The law values are not the record
count, and they are not the kernel value on `P_x`.

### N8 — cross-cycle echo

| Earlier surface | Later movement | Echo here |
|---|---|---|
| Admissibility names a whole-domain distribution | August 9 displays a trace form after a supplied grade | a number still needs a menu and a pairing |
| Record names locking and additive `I` | formation site, rate, and values remain open gates in the axiom memo | `I=1` is not the Born number |
| type separation of a global measure from a menu kernel | present note | occupancy is a third coordinate, independent of menu and kernel |

Cross-cycle movement weakens axiom-necessity rhetoric and sharpens the
displayed extra.

**Gate disposition:** PASS for (i) the three drop-one failures on the
declared window and menus, and (ii) the finite-witness lower bound that
any complete extra with that output type is at least as fine as
`(o, M, K)` up to relabeling. FAIL / DO NOT SHIP for "Born is impossible
from the four axioms," "an axiom update is necessary," "every extra is
exactly the triple," or "constructive routes are exhausted."

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axiom sentences | semantic baseline | supplied; no edit |
| Record additivity | Theorem 1 and Theorem 3 | axiom wording |
| two-site occupancies and two binary menus | finite witnesses | constructed here |
| exact `Tr(ρ P)` arithmetic | Theorem 2 | computed by the runner |
| August 9 unique trace form | named parent display | unaudited; not a proof input here |
| frame-function theorem | unused | not imported |
| occupancy, menu, kernel as physical law | extras | displayed only; not derived |
| observed frequencies or fits | none | not used |

## Review Record

Independent audit remains required before any effective status may change.
No `review-loop` was invoked in producing this artifact.
