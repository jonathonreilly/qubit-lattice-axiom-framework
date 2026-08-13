---
claim_id: uniqueness_per_site_is_j_type_not_a_theorem_of_i_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-site window, a legal unit lock is a value of the displayed C1 map J:W→{0}∪M, while a double mark at one site is not; current scalar I is not even defined on that double mark, so one-lock-per-site uniqueness is the type of J rather than a theorem of I. The C1 type is displayed and not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/uniqueness_per_site_is_j_type_not_a_theorem_of_i_hypothetical_2026_08_13.py
---

# Uniqueness Per Site Is J's Type, Not A Theorem Of I

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact two-site typing of a displayed site-indexed lock map
against current scalar Record readout. Hypothetical only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/uniqueness_per_site_is_j_type_not_a_theorem_of_i_hypothetical_2026_08_13.py`](../scripts/uniqueness_per_site_is_j_type_not_a_theorem_of_i_hypothetical_2026_08_13.py)

Parents on `origin/main`: the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Current Record says a record "locks exactly one admissible local possibility"
and "A site never carries more than one record." Those sentences name a
codomain constraint. They are not an equation in the scalar readout `I`.

On the displayed two-site window the honest C1 type is a map

`J : W → {0} ∪ M`.

A legal unit lock is a value of that type. A double mark at one site is a
map into finite subsets of `M`, so it is not a value of `J`. Current `I` is
defined on legal occupancies and unit locks; the double mark is outside that
domain. Extending occupancy-count to the double mark still returns `1`, the
same integer carried by the legal unit lock. Therefore `I` does not forbid
the double mark.

This note reconstructs that type gap. It does not adopt C1, does not enlarge
`J` to power-set valued maps, does not edit an axiom, and does not put a
pairing on `J`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "L is exhibited as a value of J:W→{0}∪M and D is exhibited as not a value; I(L)=1 is the unit-count convention on the legal lock; occupancy-count of D is 1; uniqueness-per-site is therefore typed as J's codomain, not an I-equation. C1 is not adopted."
trace_class: negative_route_pruning
target_claim_id: uniqueness_per_site_from_scalar_I
target_blocker_text: "derive 'a site never carries more than one record' as a theorem of scalar I"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the displayed two-site window, honest menu, legal unit lock, and counterfactual double mark; C1 not adopted"
hypothetical_axiom_status: "C1 follow-on: at most one lock per site is J's type, not a property of I; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let

`W = {x, y}`

be a two-site window and

`M = {A, B}`

an honest finite menu with `0 ∉ M`. The honest C1 type, displayed and not
adopted, is

`J : W → {0} ∪ M`.

The token `0` is absence, not a menu element. Occupancy of a C1 value is the
retract

`o_J(z) = 0` if `J(z) = 0`, else `1`.

**Legal unit lock `L`.** The map `J_L = (A, 0)`, meaning `J_L(x) = A` and
`J_L(y) = 0`, with occupancy `o_L = (1, 0)`. Scalar readout on this legal
unit lock is the unit-count convention

`I(L) = 1`.

Record additivity with `I(empty) = 0` does not force that unit. The integer
`1` is a choice of scale for one occupied site, not a derived theorem of
additivity.

**Counterfactual double mark `D` at the single site `x`.** A map

`J* : W →` finite subsets of `M`

with

`J*(x) = {A, B}`, `J*(y) = ∅`.

The value `J*(x)` is a two-element set. It is not an element of `{0} ∪ M`.
So `D` is not a value of `J : W → {0} ∪ M`.

Occupancy-count of a mark-map is the number of sites whose mark is nonempty.
That count is defined on `D` without making `D` a legal occupancy:

`occ_count(D) = 1`.

Current scalar `I` is not defined on `D`. There is therefore no `I`-equation
that can fail on `D`.

## Exact Target And Obligation Graph

**Exact target.** Decide whether "a site never carries more than one record"
is a theorem of current scalar `I` on the displayed window, or only a typing
constraint of the displayed C1 map.

| Obligation | Role | Disposition |
|---|---|---|
| exhibit `L` as a value of `J : W → {0} ∪ M` | type witness | proved; identity gate `J_of(L)` |
| exhibit `D` as not a value of that type | type rejector | proved; identity gate `is_J_value(D)` is false |
| evaluate `I` on the legal unit lock | current readout | `I(L) = 1` by unit-count convention; identity gate `I_of(L)` |
| show `I` has no equation on `D` | domain gap | `D` is not a legal occupancy |
| evaluate occupancy-count on `D` | naive extension | `occ_count(D) = 1`; identity gate `occ_count(D)` |
| quote current Record uniqueness sentences | source pin | axiom memo; those sentences name `J`'s type |
| keep the gap distinct from a zero-token menu | sibling type | not the `0 ∈ M` confusion |
| adopt C1 or enlarge `J` to power-set maps | non-goal | not done |

## Theorem 1 — `L` Is A Value Of `J`; `D` Is Not

The pair `(A, 0)` has both coordinates in `{0, A, B} = {0} ∪ M`. Hence `L`
is a value of `J : W → {0} ∪ M`.

The pair `({A, B}, ∅)` has first coordinate a two-element subset of `M`.
That subset is not an element of `{0} ∪ M`. Hence `D` is not a value of
`J`.

The identity gates are `J_of(L) = (A, 0)` and `is_J_value(D) = false`.

This is a type statement. It does not say `D` is physically realized. It
says the honest C1 codomain already excludes two labels at one site.

## Theorem 2 — Scalar `I` Does Not Forbid `D`

Current scalar `I` is defined on legal occupancies and unit locks. On `L`
the unit-count convention gives `I(L) = 1`. The identity gate is `I_of(L)`.

`D` is not in that domain: it is not an occupancy `W → {0, 1}` and not a
value of `J`. There is no current `I`-equation that can be evaluated on `D`,
so there is no `I`-equation that fails on `D`. Scalar `I` therefore does not
forbid the double mark.

If occupancy-count is extended to mark-maps by counting sites with a
nonempty mark, then `occ_count(D) = 1`, the same integer as `I(L)`. The
identity gate is `occ_count(D)`. A one-site double mark and a one-site legal
lock are not separated by that count.

Record additivity is not used and is not claimed to force `I(L) = 1`.

## Theorem 3 — The Record Uniqueness Sentences Are The Type Of `J`

The current Record axiom reads:

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

The two uniqueness sentences constrain what a lock is allowed to be at a
site: exactly one admissible local possibility, and never more than one
record. Those sentences are the type of J (codomain `{0}∪M`), not a theorem of I. On the displayed C1 type they say that each site
value lies in `{0} ∪ M`, not in the set of two-element subsets of `M`.

Theorem 2 shows why they cannot be a theorem of `I` on this window: `I`
does not take `D` as an argument, and the naive occupancy-count extension
agrees on `L` and `D`.

This note does not drop those sentences from the axiom file. It displays
their type. Under displayed C1 they are already encoded by the codomain of
`J`. They are not an extra scalar constraint.

## Theorem 4 — This Is Not A Zero-Token Menu Gap

A different type error is to put the absence token into the menu,
`0 ∈ M`, so that the same symbol is both unformed and a lock label. That
is not the object here. The honest menu is `{A, B}` with `0 ∉ M`. The
rejector is two distinct lock labels `{A, B}` at the single site `x`, not a
zero token.

The type gap displayed here is

`{A, B} ∉ {0} ∪ M`,

not

`0 ∈ M`.

C1 is not adopted. The map `J` is not enlarged to power-set valued maps.
Doing so would type `D` and would erase the uniqueness sentences as
codomain constraints.

## Theorem 5 — No Pairing, No Half-Rate, No Physical Carrier

This note does not force a formation rate `r = 1/2`. It does not adopt a
physical lattice carrier `L_phys`. It does not put a pairing, product
table, or two-argument readout on `J`. Those objects are extra relative to
both current `I` and displayed `J`.

Displayed C1 is a retype of site-indexed lock content. It is not a
dynamics axiom, not a Born compiler, and not a Newton pairing.

## Consequence For The Axiom Surface

The current canonical wording is
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). Record
already states one-lock-per-site uniqueness in English. The displayed C1
map makes that statement a typing fact about `J`. Current `I` does not.

No axiom text is edited. No Record rewrite is adopted. The hypothetical
status is only that uniqueness-per-site, if one writes C1, is already `J`'s
type and is not a property one should expect scalar `I` to prove.

## No-Go Discipline Gate

The negative claim is restricted to: uniqueness-per-site is not a theorem
of current scalar `I` on the displayed window, because `D` is outside `I`'s
domain and occupancy-count does not split `D` from `L`. The gate does not
certify that C1 must be adopted or that uniqueness cannot be derived from
some other later object.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Evaluate `I` on `D` | treat `D` as a legal occupancy | `D` is not in the domain of current `I` | **ATTEMPTED** |
| Extend `I` by occupancy-count | `occ_count(D)` | equals `1`, same as `I(L)` | **ATTEMPTED** |
| Record additivity | use `I(S ∪ T) = I(S) + I(T)` on disjoint collections | additivity never sees two labels at one site; it also does not force the unit `I = 1` | **ATTEMPTED** |
| `I(empty) = 0` | empty-collection normalization | does not constrain a nonempty double mark | **ATTEMPTED** |
| Site-blind bag of labels | `{A, B}` versus `{A}` | a bag can split contents, but that is not scalar `I` | **ATTEMPTED** |
| Enlarge `J` to power-set maps | type `D` as legal | would erase uniqueness as a codomain fact; not adopted | **ATTEMPTED** |
| Zero-token menu `0 ∈ M` | confuse absence with a lock label | a different type gap; not this rejector | **ATTEMPTED** |
| Axiom edit | add an `I`-equation forbidding `D` | not required to display the type; not done | **ATTEMPTED** |

The first four routes concern scalar `I`. They do not forbid `D`. The last
four use other objects or an edit. None is shipped as an axiom change.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `I`-domain gap / occupancy-count equality | no: undefined is not the integer `1` | no: equal counts do not decide domain | independent |
| uniqueness as `J`-type / uniqueness as `I`-theorem | no: typing `L` does not create an `I`-equation on `D` | no: an `I`-equation would not be the C1 codomain | independent |
| double mark / zero-token menu | no: `{A, B}` is not the token `0` | no: `0 ∈ M` is not two labels at one site | independent |

### N3 — residual after the displayed type

After Theorems 1–3 the residual is not "how to make `I` reject `D`." The
residual is whether a later retained construction should adopt C1, keep
uniqueness as English axiom text, or derive uniqueness from some other
named object. That residual is open.

### N4 — what would close the residual

A close would be either (i) an adopted C1-type Record rewrite, which this
note does not perform, or (ii) a retained derivation of uniqueness from
objects already on the axiom surface other than the English uniqueness
sentences themselves. Scalar `I` is not that derivation.

### N5 — scoped negatives

- `D` is not a value of `J : W → {0} ∪ M`.
- `I` is not defined on `D`.
- `occ_count(D) = 1 = I(L)` under the unit-count convention.
- Therefore uniqueness-per-site is not a theorem of `I` on this window.
- These negatives do not say gravity is impossible, do not say formation is
  impossible, and do not say a later object cannot enforce uniqueness.

### N6 — axiom update is not required

Displaying the type gap does not require an axiom update. The current
Record sentences already state uniqueness in English. This note does not
claim an axiom update is necessary, sufficient, or cheapest.

### N7 — non-claims

This note does not adopt C1. It does not enlarge `J` to power-set valued
maps. It does not force `r = 1/2`. It does not adopt `L_phys`. It does not
put a pairing on `J`. It does not claim Record additivity forces `I = 1`.
It does not install a vacuum possibility. It does not pick the menu
`{A, B}` as physical.

### N8 — FAIL / DO NOT SHIP

Do not ship any of the following as retained content of this note:

- "scalar `I` forbids a double mark";
- "Record additivity forces `I(L) = 1`";
- "C1 is adopted";
- "enlarge `J` to maps into subsets of `M`";
- "this is the zero-token menu gap";
- "an axiom update is necessary";
- any pairing, `r = 1/2`, or `L_phys` adoption.

## Identity And Mutation Gates

The runner must call `J_of(L)`, `is_J_value(D)`, `I_of(L)`, and
`occ_count(D)`.

- The predicate "`D` is a value of `J : W → {0} ∪ M`" must fail.
- The predicate "`I(L) ≠ 1`" must fail.
- The predicate "`occ_count(D) ≠ 1`" must fail.

Mutating `J_of` off `(A, 0)`, mutating `is_J_value(D)` to true, mutating
`I_of(L)` off `1`, or mutating `occ_count(D)` off `1` fails the runner.
