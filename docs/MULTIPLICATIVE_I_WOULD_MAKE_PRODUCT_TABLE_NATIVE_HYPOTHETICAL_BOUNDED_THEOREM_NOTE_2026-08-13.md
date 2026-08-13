---
claim_id: multiplicative_i_would_make_product_table_native_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "A one-argument multiplicative retype I_× of Record readout, with I_×(empty)=1 and I_×(n units)=q^n, has a different identity from current additive I and never equals a two-cardinality product n m. The 2×2 product table T_π therefore stays two-argument. The C8 slogan that replacing + by × on I would make T_π native fails. I_× is displayed and is not adopted. No axiom is edited."
upstream_dependencies:
  - minimal_axioms
runner: scripts/multiplicative_i_would_make_product_table_native_hypothetical_2026_08_13.py
---

# Multiplicative I Would Make The Product Table Native — Hypothetical Failure

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** one-argument Record readout on finite unit-lock collections;
displayed counterfactual `I_×` versus current additive `I`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/multiplicative_i_would_make_product_table_native_hypothetical_2026_08_13.py`](../scripts/multiplicative_i_would_make_product_table_native_hypothetical_2026_08_13.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Current Record supplies a one-argument additive scalar `I` with
`I(empty)=0`. On two named unit locks the filled I-table is `(0,1,1,2)`.
The two-argument product table on the same four pairs is `T_π=(0,0,0,1)`.

The C8 counterfactual replaces that additive sentence by a one-argument
multiplicative readout `I_×` with empty-product identity `I_×(empty)=1` and
`I_×(n units)=q^n` for a declared rational `q`. That retype has a different
identity (`0≠1`) and, at two units with `q=1`, a different value (`2≠1`).
Neither one-argument map on a single collection equals a product of two
cardinalities. So “replace `+` by `×` on `I`” does not make `T_π` native.
The pairing remains two-argument. `I_×` is displayed only. It is not
adopted. The current Record sentence is not edited.

A different cut — site-indexed `J` rather than scalar `I` — is a different
counterfactual. It is not this note’s object and is not adopted here.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The empty-identity mismatch, the two-unit q=1 mismatch, the reconstructed 2×2 tables, and the incompatibility of I_×(empty)=1 with additivity are exact finite identities. Adoption of I_×, a two-argument pairing primitive, Newton’s law, G_N, and 1/r remain closed."
trace_class: negative_route_pruning
target_claim_id: newton_product_pairing_from_record_readout
target_blocker_text: "one-argument Record readout, additive or multiplicative, does not supply the two-argument product table T_π"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed I / I_× / T_π tables on empty-or-unit pairs; no physical pairing is selected"
hypothetical_axiom_status: "C8 counterfactual: Record readout is multiplicative I_× with I_×(empty)=1; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `s` and `t` be two named unit atoms, treated as disjoint unit locks.
The four pairs of collections are

`(∅,∅)`, `(∅,{t})`, `({s},∅)`, `({s},{t})`.

Write `I_+` for the current one-argument readout: cardinality of a finite
unit-lock collection. Record additivity and `I(empty)=0` give

`I_+(∅)=0`, `I_+({t})=1`, `I_+({s})=1`, `I_+({s}⊔{t})=I_+({s})+I_+({t})=2`.

The I-table on those four pairs, read as the one-argument union when the
two sides are disjoint, is therefore

`T_+ = (0, 1, 1, 2)`.

The declared two-argument product table (extra, not axiom content) is

`T_π(∅,∅)=0`, `T_π(∅,{t})=0`, `T_π({s},∅)=0`, `T_π({s},{t})=1`,

i.e. `T_π=(0,0,0,1)`. Equivalently `T_π(S,T)=I_+(S) I_+(T)`, which is
already a pairing of two values, not a retype of one readout.

The C8 counterfactual is still one-argument. For a declared rational `q`
and an integer lock count `n≥0`,

`I_×(empty)=1`, `I_×(n units)=q^n`.

This is the empty-product convention together with a constant per-unit
factor `q`. For `q=1` one has `I_×(n)=1` for every `n`, so `I_×` is
blind to cardinality. The one-argument `I_×`-table on
`∅,{t},{s},{s}⊔{t}` is then `(1,1,1,1)`. The induced pairing
`I_×(S) I_×(T)` on the four pairs is likewise `(1,1,1,1)`.

A two-argument primitive `Π(S,T)` with `Π(empty,T)=0`, `Π(S,empty)=0`,
`Π(unit,unit)=1`, and bi-additivity would make `T_π` axiom content. That
is a pairing axiom, not a one-argument retype of `I`. It is not the C8
object, and it is not adopted.

Identity gates in the runner call `I_plus(n)` and `I_times(n,q)`.

## Reconstructed Tables

One-argument values on the four named collections:

| collection | `I_+` | `I_×` at `q=1` |
|---|---|---|
| `∅` | `0` | `1` |
| `{t}` | `1` | `1` |
| `{s}` | `1` | `1` |
| `{s}⊔{t}` | `2` | `1` |

Two-argument tables on `(∅,∅)`, `(∅,{t})`, `({s},∅)`, `({s},{t})`:

| table | values |
|---|---|
| union readout `T_+` | `(0, 1, 1, 2)` |
| product `T_π` | `(0, 0, 0, 1)` |
| pairing `I_×(S) I_×(T)` at `q=1` | `(1, 1, 1, 1)` |

`T_+` disagrees with `T_π` at three of four cells, including the
`(unit,unit)` cell `2≠1`. The `I_×` pairing disagrees with `T_π` at
every cell.

## Theorem 1 — Different identities

`I_+(empty)=I_plus(0)=0` and `I_×(empty)=I_times(0,q)=q^0=1` for every
declared `q`. In particular `I_+(empty)≠I_×(empty)`. The additive
identity and the empty-product identity are different numbers. The
predicate `I_+(empty)=I_×(empty)` fails.

## Theorem 2 — Two units, and no one-argument product

`I_+(2 units)=I_plus(2)=2`. `I_×(2 units)=I_times(2,q)=q^2`. For the
unit-factor choice `q=1`, `I_×(2)=1≠2`. The predicate
`I_+(2)=I_×(2)` at `q=1` fails.

Neither map, evaluated on a *single* collection, equals a product of two
cardinalities. For lock counts `n=2` and `m=3` one has `n m=6`, while

`I_plus(2)=2`, `I_plus(3)=3`, `I_plus(5)=5`,
`I_times(2,1)=1`, `I_times(3,1)=1`, `I_times(5,1)=1`.

None equals `6`. For `q=1`, `I_×` is constantly `1` and cannot see
`n` or `m`. For any other declared `q`, `I_×` is an exponential of one
integer, still one-argument.

## Theorem 3 — C8 fails to make `T_π` native

A one-argument retype of `I` therefore cannot make `T_π` native.
`T_π` is a function of an ordered pair of collections. C8 as “replace
`+` by `×` on `I`” fails to dissolve the two-argument Newton-B residual.
The pairing remains two-argument.

Displaying `I_+(S) I_+(T)` recovers `T_π` only by introducing that
pairing. That is not a retype of the one-argument readout. Displaying
`Π` as a primitive pairing is adopting the product table as axiom
content. Neither move is made here. `I_×` is not adopted. Site-indexed
`J` is a different cut and is not this counterfactual.

## Theorem 4 — Additivity forces `I(empty)=0`

The current Record axiom states that only records are readable, that a
readout value is determined by record content alone, and that for any
finite collection of pairwise-disjoint records, scalar readout `I` is
additive, with `I(empty)=0`.

Additivity on the empty collection against itself forces the identity:
`empty ⊔ empty = empty`, so `I(empty)=I(empty)+I(empty)`, hence
`I(empty)=0`. The counterfactual `I_×(empty)=1` is incompatible with
that additive sentence, because `1=1+1` is false. The axiom is not
edited. The incompatibility is the reason C8 is a counterfactual rather
than a rewrite.

## Mutation Predicates

The following predicates are required to fail, and the identity gates
must call `I_plus(n)` and `I_times(n,q)`:

1. `I_plus(0)=I_times(0,1)` fails because `0≠1`.
2. `I_plus(2)=I_times(2,1)` fails because `2≠1`.

## What This Note Does Not Do

- It does not adopt `I_×`.
- It does not adopt a pairing primitive `Π` or the table `T_π`.
- It does not install `G_N` or `1/r`.
- It does not claim Newton’s law.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not treat site-indexed `J` as a parent or as adopted content.

## Quoted Current Record Wording

From [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.
