---
claim_id: additive_i_is_a_lemma_of_j_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the two-site window with one displayed double-lock J, the set function I_J(S)=|{z in S: J(z)!=0}| has I_J(empty)=0 by counting and is modular on all 16 subset pairs. Under the displayed C1 readout those two Record sentences are lemmas of I_J, not independent commitments. The I-table on the four occupancies remains (0,1,1,2); the declared product table remains (0,0,0,1) and extra. C1 is not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/additive_i_is_a_lemma_of_j_hypothetical_2026_08_13.py
---

# Additive `I` Is a Lemma of `I_J` (Hypothetical)

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact two-site counting for one displayed double-lock map `J`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/additive_i_is_a_lemma_of_j_hypothetical_2026_08_13.py`](../scripts/additive_i_is_a_lemma_of_j_hypothetical_2026_08_13.py)

## Result Up Front

Current Record writes two scalar-readout sentences as primitive content:
`I` is additive, and `I(empty)=0`. Those sentences stay in the axiom file.
This note does not drop them and does not rewrite Record.

On the two-site window, reconstruct the C1 displayed readout as a
site-indexed map `J` and define the counting function

```text
I_J(S) = |{z in S : J(z) != 0}|.
```

For the fixed double lock `J11 = (A,B)`, both of the following are ordinary
counting facts about `I_J`:

1. `I_J(empty) = 0`, because the empty set contributes no counted sites.
2. `I_J(S union T) + I_J(S intersect T) = I_J(S) + I_J(T)` on every pair of
   subsets of the window (sixteen pairs).

Under that displayed C1 readout, the two Record sentences change type from
primitive to theorem: they are lemmas of `I_J`, not independent commitments.
The current axiom surface is unchanged. C1 is displayed, not adopted.

The occupancy I-table on the four subsets is still `(0,1,1,2)`. The declared
product table is still `(0,0,0,1)`. A pairing through `I` or through `I_J`
remains extra. This note does not put a pairing on `J`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Empty-set counting and sixteen-pair modularity are exact on a declared two-site window; C1 remains a displayed counterfactual, and the product table remains extra."
trace_class: upstream_support
target_claim_id: additive_i_as_lemma_of_I_J
target_blocker_text: "decide whether Record additivity and I(empty)=0 are independent primitives once readout is a site-indexed J"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Under displayed C1, additive I(empty)=0 is a lemma of I_J. Product table stays extra. Do not adopt C1."
hypothetical_axiom_status: "C1 follow-on: additive I(empty)=0 is a lemma of I_J; product table still extra; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let the window and menu be

```text
W = {x, y},    M = {A, B}.
```

The four subsets of `W` are

```text
empty,    {x},    {y},    {x, y}.
```

Reconstruct the C1 displayed readout locally (not as a cited sibling). A
site-indexed map is

```text
J : W -> {0} union M,
```

with `J(z) = 0` on an unlocked site and `J(z)` equal to the locked menu
entry on a locked site. This note fixes one displayed map, the double lock

```text
J11 = (A, B),
```

meaning `J(x) = A` and `J(y) = B`. Both values are nonzero.

For every subset `S` of `W` define

```text
I_J(S) = |{z in S : J(z) != 0}|.
```

This is a counting function of the restriction of `J` to `S`. It is not an
axiom sentence.

The four occupancies of `W` are the four subsets above, read as occupancy
supports. The I-table is the four-tuple of `I_J` values in the order

```text
(empty, {x}, {y}, {x, y}).
```

The declared product table on those four labels is the extra two-argument
table

```text
(0, 0, 0, 1).
```

That table is displayed as a contrast. It is not derived from `J`, and this
note does not put a pairing on `J`.

## Exact Target

**Exact target.** On this declared window and this declared `J11`, prove that
`I_J(empty)=0` and modularity of `I_J` are counting lemmas; display the
current Record additivity sentences as changing type under C1; keep the
I-table and the extra product table distinct; do not adopt C1, do not force
`r=1/2`, and do not adopt `L_phys`.

The only parent on `origin/main` is the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). C1 J
arithmetic is reconstructed here.

## Theorem 1 — `I_J(empty)=0` By Counting

The set `{z in empty : J(z) != 0}` is empty, because there is no `z` in the
empty set. Therefore

```text
I_J(empty) = 0.
```

The identity gate is `I_J_empty`. The value is a cardinality. It is not the
Record sentence `I(empty)=0` used as a premise. The same number appears,
but the warrant is counting.

## Theorem 2 — `I_J` Is Modular On All Sixteen Pairs

Let `S` and `T` be subsets of `W`. A site of `W` is counted by `I_J` exactly
when it lies in the argument and carries a nonzero `J` value. For the fixed
double lock `J11`, both sites are nonzero, so `I_J(S) = |S|`. In any case,
whether a site is counted is a yes/no property of that site, so the counting
function is modular:

```text
I_J(S union T) + I_J(S intersect T) = I_J(S) + I_J(T).
```

There are `4 x 4 = 16` ordered pairs `(S,T)`. Direct evaluation on each pair
confirms the identity. The four named identity-gate pairs, each calling
`I_J` on the union, the intersection, `S`, and `T`, are

```text
(empty, W),    ({x}, {y}),    ({x}, W),    ({x}, {x}).
```

Explicit values for those four:

| `S` | `T` | `S union T` | `S intersect T` | left | right |
|---|---|---|---|---|---|
| empty | `{x,y}` | `{x,y}` | empty | `2+0` | `0+2` |
| `{x}` | `{y}` | `{x,y}` | empty | `2+0` | `1+1` |
| `{x}` | `{x,y}` | `{x,y}` | `{x}` | `2+1` | `1+2` |
| `{x}` | `{x}` | `{x}` | `{x}` | `1+1` | `1+1` |

The remaining twelve pairs are the same arithmetic on a two-element set.
No additivity axiom is used.

## Theorem 3 — The Two Record Sentences Change Type Under C1

The current Record axiom, quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), includes:

> Only records are readable. A readout value is determined by record content alone. For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.

The two scalar sentences named by the target are

```text
scalar readout I is additive, with I(empty)=0.
```

Those sentences remain in the axiom file. This note does not drop them and
does not edit the memo.

Under displayed C1 the readout is the site-indexed map `J`, and the scalar
`I` used by those sentences is the counting function `I_J`. Theorems 1 and 2
then supply both sentences as lemmas of `I_J`. They change type from
primitive to theorem. They are not independent commitments once `I` is
identified with `I_J`.

On the current, unadopted axiom surface the same two sentences remain
primitive Record content. Displaying the type change is not an adoption of
C1 and is not a Record rewrite.

## Theorem 4 — I-Table `(0,1,1,2)`; Product Table Still Extra

On the four occupancies, with the identity gate `I_table`,

```text
I_table = (I_J(empty), I_J({x}), I_J({y}), I_J({x,y})) = (0, 1, 1, 2).
```

The declared product table, with the identity gate `product_table`, is

```text
product_table = (0, 0, 0, 1).
```

These four-tuples disagree in three cells, including the double-occupancy
cell `2 != 1`. A pairing through scalar `I` or through `I_J` is therefore
still extra: modularity of a one-argument counting function does not fill a
two-argument product table. This note does not put a pairing on `J`.

## Theorem 5 — Scoped Residual

This note does not adopt C1. It does not force `r=1/2`. It does not adopt
`L_phys`. It does not install a pairing, a product law, or a Record rewrite.
The current axiom file is not edited. The product table remains extra.

## Mutation And Identity Gates

Identity gates call `I_J_empty`, call `I_J` on the union, intersection, `S`,
and `T` for the four named pairs, and call `I_table` and `product_table`.

The following predicates must fail:

- `I_J(empty) != 0`
- `I_J({x}) + I_J({y}) != I_J({x,y}) + I_J(empty)`
- `I-table equals product table`

## Negative Scope

The residual in Theorem 5 is only that C1 and a pairing stay off the axiom
surface. Live routes that this note does not close include: keep the current
additive primitive and do not retype it; keep `I_J` as a derived count and
still refuse C1; supply a pairing by a later two-argument object, not by
`I_J`; leave `r` and `L_phys` unset; refuse any Record rewrite. No route
here claims gravity is impossible.

## Independence

The algebra is finite counting on a two-element set. It does not use a
Newton packet, a Green kernel, a force law, or an unmerged sibling note.
The axiom memo is the only parent.

## No-Go Discipline Gate

The negative claims are restricted to type-change of additive `I` under
displayed C1 on one double-lock window. The gate does not certify a
Record rewrite or a pairing.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| `I_J(empty)=0` as counting | evaluate `I_J` on `empty` | Theorem 1: `0` by cardinality | **ATTEMPTED** |
| Modularity of `I_J` | check all 16 subset pairs | Theorem 2: identity holds | **ATTEMPTED** |
| Additivity as a surviving primitive under C1 | identify `I` with `I_J` | Theorem 3: type changes to lemma | **ATTEMPTED** |
| Product table from `I_J` | compare I-table with `(0,0,0,1)` | Theorem 4: `(0,1,1,2)≠(0,0,0,1)` | **ATTEMPTED** |
| Adopt C1, pairing on `J`, `r=1/2`, `L_phys` | enlarge the display | Theorem 5: refused | **ATTEMPTED** |

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| empty-zero / modularity | no: empty count is one cell | no: modularity is 16 pairs | independent obligations |
| `I_J` lemmas / product table | no: a one-argument count is not a pairing | no: a product table would still need two arguments | independent |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| window `W={x,y}`, `J11=(A,B)` | stipulated finite objects |
| `I_J` as cardinality | reconstructed count |
| product table `(0,0,0,1)` | declared extra contrast; not derived |
| pairing, `r=1/2`, `L_phys` | not used |
| observations | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | additive scalar `I` with `I(empty)=0` | exact current wording; sentences stay in the file |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | `I_J` on four subsets; sixteen pairs | no classification of every `J` |
| per site | window `{x,y}`; double lock `J11` | no lattice-wide additivity theorem |
| per mode | I-table is a cardinality | no product table |
| per block | additive-`I` type change under displayed C1 | no pairing or Newton-π closure |
| lattice-wide | not executed | two-site window only |

The runner emits substantive `per_element`, `per_site`, `per_mode`,
`per_block`, and `lattice_wide` lines.

### N6 — live partial-closure paths

1. Keep current Record: additive `I` remains primitive.
2. Owner wording could adopt `J` later; additivity would then be a lemma.
3. A later two-argument object could supply a pairing; `I_J` does not.

None of those paths is taken here.

### N7 — hostile steelman

> Once `I` is a count of occupied sites, additivity is automatic, so this
> note only restates `I(empty)=0`. The product table is beside the point.

The steelman is half right: the count is automatic. Theorem 4 is the
point of the residual — that automatic count still does not give
`(0,0,0,1)`. Type change of additivity does not dissolve Newton `π`.

### N8 — cross-cycle echo

This is a C1 follow-on keep-candidate, not pairing-on-`J`, not a second
Newton-π, and not a fifth extra. Earlier C1 occupancy notes remain on
their own surfaces and are not parents.

**Gate disposition:** PASS for (i) `I_J(empty)=0` by counting, (ii)
modularity on 16 pairs, and (iii) product table still extra. FAIL / DO
NOT SHIP for "adopt C1," "drop the additive sentences from the file,"
"put a pairing on `J`," "force `r=1/2`," or "adopt `L_phys`."

## Review Record

Independent audit remains required before any effective status may
change. No `review-loop` was invoked in producing this artifact.
