---
claim_id: born_extra_under_c1_is_menu_kernel_not_occupancy_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Hypothetical C1 follow-on, not an adoption. On a two-site window the displayed site-indexed lock readout J already names the formed site by retract, so occupancy is not an independent Born extra under that counterfactual. The same J takes values in lock labels and does not name an effect menu or a trace kernel. Exact one-site arithmetic on rho=diag(3/5,2/5) separates K(rho,P_z)=3/5 from K(rho,P_x)=1/2 and from the unit-lock Record count I_J=1. The smallest complete Born extra under displayed C1 is therefore (M,K), not (o,M,K). No Born axiom, no Gleason import, no pairing on J, and C1 itself is not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/born_extra_under_c1_is_menu_kernel_not_occupancy_hypothetical_2026_08_13.py
---

# Born Extra Under C1 Is Menu-Kernel, Not Occupancy

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** hypothetical discriminating test of C1's dissolution claim
for the Born cluster on a two-site window. Not a second Born exercise.
Not a fifth extra. Not pairing-on-J. Not C6/C7.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/born_extra_under_c1_is_menu_kernel_not_occupancy_hypothetical_2026_08_13.py`](../scripts/born_extra_under_c1_is_menu_kernel_not_occupancy_hypothetical_2026_08_13.py)

## Result Up Front

The current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
supplies Lattice sites, a one-site possibility domain `M_2(C)`, a
nearest-neighbor law, and Record lock plus additive scalar readout `I`.
It does not supply a site-indexed lock-label field `J`, an effect menu,
or a Born kernel.

C1 is reconstructed here only as a displayed counterfactual readout, not
as a parent on `origin/main` and not as an adopted primitive:

`J : W -> {0} union {A,B}`,

with definitional retract

`o_J(z) = 0` if `J(z)=0`, else `1`.

Five exact statements follow.

1. **Occupancy dies as an independent extra under C1.** On every `{0,1}`
   occupancy the retract `o_J` equals occupancy. The formed site is
   `{z : J(z) != 0}`. A compiler handed `J` already has the site.
2. **Menu survives.** `K(rho, P_z)=3/5 != 1/2=K(rho, P_x)`. Lock labels
   are not projectors, so `J` does not name `M_z` versus `M_x`.
3. **Kernel survives.** `I_J(J10A)=1 != 3/5=K(rho, P_z)`. The J-count is
   not a Born number.
4. **Smallest complete Born extra under C1 is therefore `(M,K)`, not
   `(o,M,K)`.** Occupancy changed type. Menu and kernel did not. Display
   `(M,K)`. This is C1's dissolution ledger for the Born cluster, not a
   new named extra.
5. **Do not import Gleason. Do not force `r=1/2`. Do not adopt `L_phys`.
   Do not put a pairing on `J`. Do not adopt a Born axiom. Do not adopt
   C1.**

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The retract, two-menu kernel split, and J-count versus kernel split are exact on declared finite objects. C1 is a displayed counterfactual, not adopted. Menu and kernel remain extras. No Born axiom is written."
trace_class: negative_route_pruning
target_claim_id: born_cluster_extra_under_displayed_c1
target_blocker_text: "under site-indexed J, decide whether occupancy remains an independent Born extra or becomes a definitional retract, while menu and kernel stay independent of J"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed C1 retract and the one-site (M,K) witnesses; C1 and any Born axiom remain unadopted"
hypothetical_axiom_status: "C1 follow-on: under site-indexed J, Born extra is (M,K) not (o,M,K); not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let the window be

`W = {x, y}`.

Lock labels are `{A, B}`. The displayed C1 readout is a function

`J : W -> {0} union {A, B}`.

The occupancy retract is

`o_J(z) = 0` if `J(z) = 0`, else `1`.

Unit-lock histories used below:

`J10A = (A, 0)`, `J01A = (0, A)`,

read as `J(x), J(y)` in that order. Then

`o_J(J10A) = (1, 0)`, `o_J(J01A) = (0, 1)`.

The Record count on a displayed history is the additive scalar

`I_J(J) = |{z in W : J(z) != 0}|`.

Both unit-lock histories have `I_J = 1`.

Work at one `M_2(C)` site with the exact one-site law

`rho = diag(3/5, 2/5)`.

Pauli `sigma_x` is the off-diagonal unit matrix. Effect menus:

`M_z = {P_z, I - P_z}` with `P_z = diag(1, 0)`,

`M_x = {P_x, I - P_x}` with `P_x = (I + sigma_x)/2`.

The kernel is the exact trace grade

`K(rho, P) = Tr(rho P)`.

Direct matrix arithmetic:

`K(rho, P_z) = 3/5`, `K(rho, P_x) = 1/2`.

`J` takes values in lock labels, not in projectors. Nothing in `J10A` or
`J01A` selects `M_z` versus `M_x`, and nothing in the J-count returns
`3/5` or `1/2`.

These objects are reconstructed here from the C1 retract and Born
arithmetic. They are not imported from an unmerged parent.

## Theorem 1 — Occupancy Dies Under C1

On every `{0,1}`-valued occupancy of `W`, `o_J` equals occupancy. Proof:
`J(z)=0` is the unformed site and `J(z) in {A,B}` is the formed site, so
the indicator `o_J` is occupancy by definition of the displayed readout.

The formed site is therefore `{z : J(z) != 0}`. A compiler that is handed
`J` already has the site. Drop-occupancy is not a missing input **under
the C1 counterfactual**.

Identity gates call `o_from_J` on `J10A` and `J01A`:

`o_from_J(J10A) = (1, 0)`, `o_from_J(J01A) = (0, 1)`.

The predicate "`o` is independent of `J`" fails on this pair.

This theorem is counterfactual on displayed C1. The current axiom memo
does not contain `J`. Occupancy remains an open extra on the actual
current surface.

## Theorem 2 — Menu Survives

`K(rho, P_z) = 3/5 != 1/2 = K(rho, P_x)`.

The two binary menus are distinct resolutions of `I`. The kernel values
differ, so a compiler that is not handed a declared effect menu has no
outcome list and no grade. `J` cannot supply that list: its values are
lock labels `{0, A, B}`, not projectors.

Identity gates call `born(rho,Pz)` and `born(rho,Px)`:

`born(rho, Pz) = 3/5`, `born(rho, Px) = 1/2`.

The predicate "`K(rho, P_z) = K(rho, P_x)`" fails.

The equality `K(rho, P_x) = 1/2` is an exact trace on this `rho` and
this menu. It is not a forced universal `r=1/2`.

## Theorem 3 — Kernel Survives

`I_J(J10A) = 1 != 3/5 = K(rho, P_z)`.

The same holds for `J01A`. The J-count is the Record additive readout of
formed locks on the window. It is not the Born number of any effect.
Record readout is not a Born number.

Identity gates call `I_J` on both unit-lock histories. The predicate
"`I_J` equals `K(rho, P_z)`" fails.

## Theorem 4 — Smallest Complete Born Extra Under C1 Is `(M,K)`

Under displayed C1, occupancy changed type: it is the definitional
retract of `J`. Menu and kernel did not change type. The smallest
complete Born extra on this counterfactual is therefore `(M, K)`, not
`(o, M, K)`.

Display `(M, K)`. Do not adopt a Born axiom. Do not adopt C1. This is
not a new named extra and not a fifth extra. It is C1's dissolution
ledger for the Born cluster.

On the actual current axiom surface, `J` is absent, so this shrinkage is
not in force.

## Theorem 5 — Forbidden Closures

- Do not import Gleason.
- Do not force `r = 1/2`.
- Do not adopt `L_phys`.
- Do not put a pairing on `J`.
- Do not write a Born axiom.
- Do not adopt C1.

No inner product, frame function, or pairing is placed on lock labels.
The kernel used here is the declared one-site trace `K(rho, P) = Tr(rho P)`
on two explicit menus. That is reconstruction of Born arithmetic, not a
Gleason derivation and not an axiom.

## Mutation Ledger

| Predicate | Witness | Required result |
|---|---|---|
| `o` is independent of `J` | `o_from_J(J10A)=(1,0) != (0,1)=o_from_J(J01A)` | must fail |
| `K(rho, P_z) = K(rho, P_x)` | `3/5 != 1/2` | must fail |
| `I_J` equals `K(rho, P_z)` | `1 != 3/5` | must fail |

Identity gates must call `o_from_J`, `born(rho,Pz)`, `born(rho,Px)`, and
`I_J`.

## Consequence For The Axiom Surface

The current public wording remains
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).
No sentence of that memo is edited. In particular the memo is not given
a site-indexed lock-label field, an effect menu, a Born kernel, a
pairing, or `L_phys`.

Under the displayed C1 counterfactual only, occupancy is no longer an
independent input to a Born compiler. Menu and kernel still are. That is
the whole advance.

## No-Go Discipline Gate

The negative claims are restricted to three predicates on the displayed
objects. The gate does not certify a Born derivation, a C1 adoption, or
exhaustion of other extras.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Occupancy as independent extra under C1 | compare `o_from_J` on `J10A` and `J01A` | Theorem 1: retract equals occupancy; independence fails | **ATTEMPTED** |
| Menu named by lock labels | compare `K(rho, P_z)` and `K(rho, P_x)` | Theorem 2: `3/5 != 1/2`; `J` has no projector values | **ATTEMPTED** |
| Kernel named by J-count | compare `I_J(J10A)` with `K(rho, P_z)` | Theorem 3: `1 != 3/5` | **ATTEMPTED** |
| Pairing on `J` | treat lock labels as a pairing/inner-product carrier | forbidden by Theorem 5; not constructed | **REJECTED** |
| Gleason import | force the trace form from a frame function | forbidden by Theorem 5; not used | **REJECTED** |
| Force `r=1/2` | replace the exact `3/5` witness by a universal half | forbidden by Theorem 5 | **REJECTED** |
| Adopt C1 or a Born axiom | write either into the axiom memo | out of scope; not adopted | **REJECTED** |

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| occupancy retract / menu | no: `o_J` names a site, not a projector list | no: a menu does not form a site | independent |
| occupancy retract / kernel | no: `{0,1}` occupancy is not `3/5` | no: a trace grade does not name the formed site | independent |
| menu / kernel | no: two menus are needed before `K` is evaluated | no: a single number does not name `M_z` versus `M_x` | independent |
| `I_J` / `K` | no: unit-lock count is `1` on both histories | no: `3/5` is not a Record count | independent |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `J` | displayed C1 counterfactual readout; not in the current axiom memo |
| `o_J` | definitional retract of displayed `J` |
| `rho = diag(3/5, 2/5)` | exact one-site law used as a witness, not a derived state |
| `M_z`, `M_x` | declared binary effect menus |
| `K(rho, P) = Tr(rho P)` | declared kernel on those menus; not a Gleason output |
| `I_J` | additive Record count of locked sites on the window |
| Gleason / pairing / `L_phys` / `r=1/2` | explicitly not used |
| observations or empirical frequencies | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | `M_2(C)` one-site domain; Record lock; additive scalar `I`; no menu; no kernel; no `J` | current wording only; C1 reconstructed, not cited as a parent |

No unmerged PR is cited. C1 retract arithmetic is reconstructed in this
note.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | two unit-lock histories, two projectors, two kernel values | no classification of every readout |
| per site | one `M_2(C)` law and a two-site window | no composite Born theorem |
| per mode | not used | no spectral claim |
| per block | Born-cluster extras under displayed C1 only | no fifth extra, no pairing-on-J, no C6/C7 |
| lattice-wide | not executed | no lattice-wide dynamics |

### N6 — live partial-closure paths

1. Derive a physical `J` from Record content without adopting C1 as an
   axiom; occupancy would then be a retract on that derived surface only.
2. Derive a physical effect menu from neighboring records; that would
   supply `M` rather than dissolve it.
3. Derive the trace kernel from a retained one-site law; that would
   supply `K` rather than dissolve it.

None of those routes is closed here.

### N7 — hostile steelman

> If C1 is adopted, perhaps lock labels already encode the menu, or the
> additive Record count already is the Born number, so `(M,K)` also dies.

The exact witnesses reject both halves: lock labels are not projectors,
and `I_J=1` is not `3/5`. Menu and kernel survive the steelman.

### N8 — cross-cycle echo

This is a C1 follow-on, not a second Born exercise, not a fifth extra,
and not pairing-on-J. Earlier Born-form and measure/menu-kernel notes
remain on their own surfaces. They are not parents of this note.

**Gate disposition:** PASS for (i) occupancy is a retract under displayed
C1, (ii) menu and kernel remain independent extras, and (iii) the
displayed extra is `(M,K)` not `(o,M,K)`. FAIL / DO NOT SHIP for "adopt
C1," "adopt a Born axiom," "Gleason is used," "force `r=1/2`," "adopt
`L_phys`," or "put a pairing on `J`."

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axiom sentences | exact semantic baseline | supplied; no edit |
| displayed C1 readout `J` and retract `o_J` | counterfactual reconstruction | not adopted |
| `rho`, `M_z`, `M_x`, `K=Tr` | exact one-site Born arithmetic | reconstructed here |
| Gleason, pairing on `J`, `L_phys`, Born axiom | forbidden | not used |
| observed probabilities | none | not used |

## Review Record

Independent audit remains required before any effective status may
change. No axiom file is edited. No runner cache, citation manifest, or
unmerged parent is attached.
