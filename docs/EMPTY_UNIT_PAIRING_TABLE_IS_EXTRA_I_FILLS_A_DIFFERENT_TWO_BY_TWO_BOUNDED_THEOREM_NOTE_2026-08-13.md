---
claim_id: empty_unit_pairing_table_is_extra_i_fills_a_different_two_by_two_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On two named unit atoms, Record's one-argument additive I fills the 2×2 of pair-unions by (0,1,1,2). A separately declared product table T_π fills the same four cells by (0,0,0,1) and therefore disagrees at three cells, including the unit-unit cell 2≠1. Record does not name a two-argument table; T_π is extra. A later supplier of T_π on {empty,unit}² together with separate additivity on N uniquely extends to (n,m)↦nm, and that supplier is not Record additivity. No pairing axiom is adopted. Newton is not claimed. G_N and 1/r are not installed."
upstream_dependencies:
  - minimal_axioms
  - newton_law_derived_note
runner: scripts/empty_unit_pairing_table_is_extra_i_fills_a_different_two_by_two_2026_08_13.py
---

# Empty/Unit Pairing Table Is Extra; I Fills A Different 2×2

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact four-cell comparison of one-argument Record readout against a
declared extra product table on two named unit locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/empty_unit_pairing_table_is_extra_i_fills_a_different_two_by_two_2026_08_13.py`](../scripts/empty_unit_pairing_table_is_extra_i_fills_a_different_two_by_two_2026_08_13.py)

## Result Up Front

Record supplies a one-argument scalar readout `I`. On two named unit atoms
`s` and `t`, treated as disjoint unit locks, that readout fills the four pair
cells

```text
(∅,∅), (∅,{t}), ({s},∅), ({s},{t})
```

by the I-table `(0, 1, 1, 2)`.

A product table `T_π` may be *declared* on the same four cells, with values
`(0, 0, 0, 1)`. That table is extra: it is not named by Record. It disagrees
with the I-table at three of the four cells, including the unit-unit cell
`2 ≠ 1`.

If a later supplier provides those four `T_π` values and, separately,
additivity on `N` in each argument, the unique extension to unit-lock counts
is `(n, m) ↦ n m`. That supplier is not Record additivity. The extension
evaluates to `12` at `(3, 4)`.

This note does not adopt a pairing axiom, does not claim Newton, and does not
install `G_N` or `1/r`. The Newton packet's physical product law remains a
non-claim.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The four-cell I-table is recomputed from I(empty)=0 and disjoint additivity; T_π is a declared extra table; disagreement is exact; the N×N product extension is unique only after a later supplier is granted; no pairing axiom or Newton claim is made."
trace_class: negative_route_pruning
target_claim_id: empty_unit_pairing_table_is_extra_i_fills_a_different_two_by_two
target_blocker_text: "Record additivity does not supply a two-argument pairing table; any product extension is a later extra supplier"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the four named cells and on the unique N×N extension after the extra supplier; physical product law and Newton remain non-claims"
hypothetical_axiom_status: "no pairing axiom is adopted, recommended, or edited"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Quoted Parents

The current Record axiom, from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), is used only
for its one-argument additive readout:

```text
Only records are readable. A readout value is determined by record content
alone. For any finite collection of pairwise-disjoint records, scalar readout
`I` is additive, with `I(empty)=0`.
```

That sentence names a function of one collection. It does not name a function
of an ordered pair of collections.

The Newton packet
[`NEWTON_LAW_DERIVED_NOTE.md`](NEWTON_LAW_DERIVED_NOTE.md) is used only for
its product-law **non-claim**. Among the items that packet does not prove is:

> the physical product law `M_source M_test`;

No other Newton-packet claim is used. In particular this note does not import
the packet's kernel, gradient, coupling, or force-law surface.

## Exact Objects

Let `s` and `t` be two named unit atoms. Write

```text
∅, {t}, {s}, {s} ∪ {t}
```

for the four collections they generate. Treat `{s}` and `{t}` as disjoint
unit locks, so `{s} ∪ {t}` is the disjoint union `{s} ⊔ {t}`. A *unit lock*
is a one-atom collection whose Record readout is normalized to `I = 1`.

The four *pair cells* are the ordered pairs of collections

```text
(∅, ∅), (∅, {t}), ({s}, ∅), ({s}, {t}).
```

The **I-table** is the four-tuple of one-argument Record values of the
corresponding unions (equivalently, of the four collections themselves):

```text
I(∅) = 0,
I({t}) = 1,
I({s}) = 1,
I({s} ∪ {t}) = 2.
```

Displayed as a 2×2 with rows `{∅, {s}}` and columns `{∅, {t}}`:

```text
        ∅     {t}
∅       0      1
{s}     1      2
```

The **product table** `T_π` is a separately declared two-argument table on
the same four pair cells, *not* an axiom:

```text
T_π(∅, ∅) = 0,
T_π(∅, {t}) = 0,
T_π({s}, ∅) = 0,
T_π({s}, {t}) = 1.
```

Displayed on the same 2×2:

```text
        ∅     {t}
∅       0      0
{s}     0      1
```

All displayed scalars are exact rational values (`Fraction` in the runner).

## Theorem 1 — The I-table is `(0, 1, 1, 2)`

**Statement.** Record's one-argument additive `I`, together with the unit-lock
normalization `I({s}) = I({t}) = 1`, fills the four pair cells by
`(0, 1, 1, 2)`.

**Proof.** The axiom supplies `I(empty) = 0`, so the `(∅, ∅)` cell is `0`.
The collections `{s}` and `{t}` are named unit locks, so

```text
I({s}) = 1,    I({t}) = 1.
```

Those are the `({s}, ∅)` and `(∅, {t})` cells. The remaining collection is
the disjoint union `{s} ⊔ {t}`. Finite additivity on pairwise-disjoint
records gives

```text
I({s} ⊔ {t}) = I({s}) + I({t}) = 1 + 1 = 2.
```

Hence the I-table is exactly `(0, 1, 1, 2)`.

## Theorem 2 — `T_π` is `(0, 0, 0, 1)` and disagrees at three cells

**Statement.** The declared extra table `T_π` fills the same four cells by
`(0, 0, 0, 1)`. It disagrees with the I-table at three of the four cells,
including the unit-unit cell, where `2 ≠ 1`.

**Proof.** The values of `T_π` are the declared four-cell table in Exact
Objects. Cellwise comparison against Theorem 1:

| cell | I | `T_π` | equal? |
|---|---:|---:|---|
| `(∅, ∅)` | `0` | `0` | yes |
| `(∅, {t})` | `1` | `0` | no |
| `({s}, ∅)` | `1` | `0` | no |
| `({s}, {t})` | `2` | `1` | no |

Three of four cells disagree. At the unit-unit cell `({s}, {t})` one has
`I({s} ∪ {t}) = 2` and `T_π({s}, {t}) = 1`, so `2 ≠ 1`.

A predicate “I-table equals `T_π`” is therefore false, and it fails in
particular at the unit-unit cell.

## Theorem 3 — Record fills the I-table and does not name `T_π`

**Statement.** The quoted Record sentence fills the I-table of Theorem 1. It
does not name a two-argument table. `T_π` is extra.

**Proof.** The quoted Record sentence supplies a scalar `I` of one finite
collection of pairwise-disjoint records, with `I(empty) = 0` and additivity.
Theorem 1 uses only that one-argument structure plus the named unit-lock
normalization. The same sentence does not introduce a symbol for a map

```text
(collection, collection) ↦ scalar
```

and does not assign values to the four ordered pairs independently of the
union. The table `T_π` is therefore a declared extra object. It is not an
axiom, not a Record consequence, and not adopted here.

## Theorem 4 — Unique `N × N` extension of a later `T_π` supplier

**Statement.** Suppose a later supplier provides the four `T_π` values on
`{empty, unit}²` and, separately, additivity on `N` in each argument of a
map `T: N × N → Q`. Then the unique such extension is

```text
T(n, m) = n m
```

on unit-lock counts. That supplier is not Record additivity. The extension
satisfies `T(3, 4) = 12`.

**Proof.** Write `0` for the empty count and `1` for one unit lock. The
supplied unit square is

```text
T(0, 0) = 0,    T(0, 1) = 0,    T(1, 0) = 0,    T(1, 1) = 1.
```

Separate additivity in the first argument gives, for every `m` and every
`n ≥ 0`,

```text
T(n, m) = T(1, m) + ⋯ + T(1, m)   (n times)   = n T(1, m),
```

and `T(0, m) = 0` because `T(0, m) = T(0, m) + T(0, m)`. Separate additivity
in the second argument likewise gives `T(1, m) = m T(1, 1)` and `T(n, 0) = 0`.
Therefore

```text
T(n, m) = n m T(1, 1) = n m · 1 = n m.
```

Any other separately additive map with the same unit square would have the
same values, so the extension is unique. In particular

```text
T(3, 4) = 3 · 4 = 12.
```

Record additivity is a one-argument identity on disjoint collections. It does
not supply a two-argument table on `{empty, unit}²`, and it does not supply
a separate additivity axiom for a map `N × N → Q`. The later supplier that
does so is therefore not Record additivity.

## Theorem 5 — No pairing axiom, no Newton claim, no `G_N` or `1/r`

**Statement.** This note does not adopt a pairing axiom. It does not claim
Newton. It does not install `G_N` or `1/r`. The Newton packet's physical
product law remains a non-claim.

**Proof.** Theorems 1–3 compare two four-cell tables and identify `T_π` as
extra. Theorem 4 is a conditional uniqueness statement about a later
supplier. None of those statements introduces, recommends, or edits an axiom.
None identifies `T(n, m) = n m` with a physical source-test product, a force
law, a coupling, or a radial kernel.

The Newton parent is quoted only for the non-claim

> the physical product law `M_source M_test`;

That sentence is used as a boundary, not as a derivation license. The
physical product law is therefore still a non-claim. `G_N` and `1/r` are not
defined, fitted, or installed here.

## Mutation

The predicate “I-table equals `T_π`” must fail. By Theorem 2 it fails at the
unit-unit cell, where the I-table value is `2` and the `T_π` value is `1`.
The runner evaluates that predicate by calling `i_table()` and `pi_table()`;
identity gates for the two tables likewise call those functions rather than
substituting a hardcoded four-tuple in place of the table constructors.

## Non-Claims

This note does not:

- adopt, recommend, or edit a pairing axiom;
- claim that Record additivity forces `T_π` or ` (n, m) ↦ n m `;
- claim Newton, a force law, a test-mass response, or a gravitational
  coupling;
- install `G_N` or `1/r`;
- identify unit-lock counts with physical masses;
- cite an unmerged pairing reconstruction as a parent.

The physical product law named by the Newton packet remains a non-claim.

## Verification

Run:

```bash
python3 scripts/empty_unit_pairing_table_is_extra_i_fills_a_different_two_by_two_2026_08_13.py
```

Expected closeout includes `TOTAL: PASS>=10 FAIL=0`, identity gates that call
`i_table()` and `pi_table()`, and a failing equality predicate at the
unit-unit cell.
