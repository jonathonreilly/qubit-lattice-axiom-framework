# Supplied POVM observation-comparator input convention

Date: 2026-07-30

Authority: none

Audit: unset

Status: supplied convention metadata

Claim type: meta

Runner:

- [`frontier_povm_observation_comparator_independent_check_2026_07_30.py`](../scripts/frontier_povm_observation_comparator_independent_check_2026_07_30.py)

Constitutional effect: none. This note adds no axiom, primitive, registry
entry, audit result, or audit status. It records one finite supplied protocol
so that its labels and associations are not presented as theorem content.

## Supplied protocol

Use the ordered outcome labels

```text
(x+, x-, y+, y-, z+, z-)
```

and the six qubit effects

```text
E_(a,s) = (I + s sigma_a)/6,
    a in {x,y,z},  s in {+1,-1}.
```

Each effect is one third of an axis projector. The six effects sum to `I`.
The state-like comparator input is the supplied Bloch vector

```text
r = (21/100, -32/100, 41/100).
```

It is copied from the held consistency fixture in
[`physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py`](../scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py).
That provenance is a pinned executable-source fact. It does not make the
literal framework-derived, physically selected, measured, or retained.

The comparator functional is also supplied:

```text
rho = (I + r_x X + r_y Y + r_z Z)/2,
q_(a,s) = Tr(rho E_(a,s)).
```

For a declared positive exposure `M`, an observation row carries only:

- a unique row identifier;
- the supplied menu identifier;
- the supplied exposure identifier; and
- one of the six ordered outcome labels.

Rows are required by this protocol to be exhaustive and mutually exclusive
for that exposure. Their count vector is normalized by the supplied rule
`f_i=n_i/M`. Optional provenance strings, coarse groupings, same-effect tags,
or calibration functions may be useful in other protocols; this convention
does not assert that any such representation is universal or minimal.

## Declared fixtures

The matching synthetic profile has exposure `M=600` and counts

```text
(121, 79, 68, 132, 141, 59).
```

The counterfactual synthetic profile moves one row from `x+` to `x-`:

```text
(120, 80, 68, 132, 141, 59).
```

Both profiles are authored test inputs. They are not sampled data,
observational frequencies, realized outcomes, or empirical calibration.

## Record boundary

`ObservationRow` is an apparatus-test schema name. It is not identified with
the framework Record of
[`MINIMAL_AXIOMS_2026-06-29.md`](./MINIMAL_AXIOMS_2026-06-29.md).
The minimal axiom fixes locking and readout once a Record is present; it does
not type these rows, form Records, select an occurrence, supply a probability
law, or calibrate an empirical frequency.

Class/object fields, module or closure state, imported state, callbacks,
process history, encoded-domain protocols, and direct empirical functionals
are all outside this one convention. Their availability is neither affirmed
nor denied here.

## Scope

This note supplies labels, finite arrays, an exposure rule, and a comparator.
It contains no representation-independent interface theorem. The paired
bounded theorem proves only the exact algebra that follows after these inputs
are stipulated.
