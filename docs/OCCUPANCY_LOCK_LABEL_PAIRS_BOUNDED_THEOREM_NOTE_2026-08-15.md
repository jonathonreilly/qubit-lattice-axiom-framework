---
claim_id: occupancy_lock_label_pairs_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Occupancy-only lock labels are the 8 pairs (S,k) for S⊆{x,y,z}. This is not a PVM and does not use Aut(M_2). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/occupancy_lock_label_pairs_2026_08_15.py
---

# Occupancy Lock Labels Are The Pairs (S,k)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact census of occupancy-only labels on the 64 binary six-tuples.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/occupancy_lock_label_pairs_2026_08_15.py`](../scripts/occupancy_lock_label_pairs_2026_08_15.py)

## Result up front

A nearest-neighbor occupancy cell is a binary 6-tuple, one bit for each
directed neighbor of a cubic site. Occupancy-only content forgets every
further pairing and keeps only which axes fail to match on the two opposite
rays. The displayed label is the pair `(S,k)` with `S` the set of unmatched
axes and `k=|S|`. Enumerating all 64 cells yields exactly eight labels: the
empty set and the seven nonempty subsets of `{x,y,z}`. Cells sharing a label
are indistinguishable by occupancy-only content.

This is a new content object. It is not the leftover Aut yes/no character of
claim `#6383`. It is not a rank-1 projector: those require an axis–Pauli
pairing that is not supplied here. The pairs are displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The image of the occupancy label map on the 64 binary six-tuples is the eight pairs (S,k); projector and Aut identifications are refused. Formation, readout, and any operator pairing remain unsupplied."
trace_class: negative_route_pruning
target_claim_id: occupancy_lock_rank_one_projector_from_occupancy_bits
target_blocker_text: "identify occupancy-only six-tuple content with a rank-1 projector or leftover Aut character"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "keep occupancy labels as displayed (S,k) pairs; do not identify them with Aut leftover or with an axis–Pauli projector pairing"
conditional_surface_status: "exact on the declared 64-cell occupancy carrier; not adopted as a physical lock menu"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

The current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
nearest-neighbor adjacency on the cubic lattice, a nearest-neighbor
admissibility rule, and the Record sentences

```text
When present, a record locks exactly one admissible local possibility.
A readout value is determined by record content alone.
```

Those sentences identify lock and content-only readout. They do not name a
binary occupancy alphabet, do not enumerate six-tuples, and do not pair an
axis with a Pauli generator. The 64-cell carrier and the map `λ` below are
declared finite test objects. No axiom is edited. `Aut(M_2)` is not used.

## Exact objects

Write the directed axes in the fixed order

```text
(+x, -x, +y, -y, +z, -z).
```

A cell is a 6-tuple

```text
c ∈ {0,1}^6,
c = (c_{+x}, c_{-x}, c_{+y}, c_{-y}, c_{+z}, c_{-z}).
```

There are `2^6 = 64` cells. For each axis `μ ∈ {x,y,z}` the two opposite bits
are `c_{+μ}` and `c_{-μ}`. Define

```text
S(c) = { μ ∈ {x,y,z} : c_{+μ} ≠ c_{-μ} },
k(c) = |S(c)|,
λ(c) = (S(c), k(c)).
```

The integer `k` is determined by `S`. It is displayed so that the label is
the pair `(S,k)` rather than the set `S` alone. An axis in `S` is
unbalanced; an axis outside `S` is balanced (`c_{+μ} = c_{-μ}`).

## Theorem 1 — the image of λ has size 8

Every value of `λ` is a pair `(S, |S|)` for some `S ⊆ {x,y,z}`. There are
`2^3 = 8` subsets of a three-element set: the empty set and seven nonempty
subsets. Grouped by cardinality they are

```text
k=0:  ∅
k=1:  {x}, {y}, {z}
k=2:  {x,y}, {x,z}, {y,z}
k=3:  {x,y,z}.
```

That is the split `1+3+3+1 = 8`. Each subset occurs: for any prescribed `S`,
set the two bits of every `μ ∈ S` to `(1,0)` and the two bits of every
balanced axis to `(0,0)`. Then `S(c)=S` and `k(c)=|S|`. Hence

```text
im(λ) = { (S, |S|) : S ⊆ {x,y,z} },
|im(λ)| = 8.
```

## Theorem 2 — balanced cells and nonempty fibers

The cells with `k=0` are exactly the axis-balanced 6-tuples: `c_{+μ}=c_{-μ}`
on every axis. Each axis then has two choices, `(0,0)` or `(1,1)`, so there
are `2^3 = 8` such cells.

For a fixed subset `S`, each axis still has two occupancy choices: a
balanced axis may be `(0,0)` or `(1,1)`, and an unbalanced axis may be
`(1,0)` or `(0,1)`. Thus every fiber of `λ` has exactly eight cells. In
particular every nonempty `S` is realized, and any two distinct cells in the
same fiber are indistinguishable by occupancy-only content.

The k-census on the 64 cells is therefore

```text
k=0: 8,   k=1: 24,   k=2: 24,   k=3: 8.
```

## Theorem 3 — displayed invariances; not a rank-1 projector

The map `λ` depends only on which axes have unequal opposite bits.

- Swapping the two bits on a balanced axis leaves those bits equal, so the
  swap is the identity on that axis and `S` is unchanged.
- Swapping the two bits on an unbalanced axis together means flipping both
  bits. The pair `(1,0)` becomes `(0,1)` and conversely; the bits remain
  unequal, so `S` is unchanged.

Both operations therefore fix `λ(c)`. They do not mix distinct labels.

The same occupancy pair is not a rank-1 projector. A rank-1 projector on the
one-site algebra would require an axis–Pauli pairing, which is the extra
content of `#6383` and is not supplied by occupancy bits. The present object
is a function from `{0,1}^6` to eight discrete pairs. It does not assign an
operator, does not use `Aut(M_2)`, and is not the leftover Aut yes/no
character of `#6383`.

## Negative check — not a projector-valued measure

This paragraph is a negative check, not a theorem statement. The eight labels
do not form a projector-valued measure: there is no supplied family of
operators summing to the identity, and no axis–Pauli pairing with which to
build one. Occupancy-only indistinguishability is equality of `(S,k)`, not
equality of spectral projections.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| 64-cell binary six-tuple carrier | declared; enumerated |
| definition of `S`, `k`, and `λ` | declared |
| `|im(λ)|=8` with split `1+3+3+1` | proved by listing subsets and exhibiting a preimage |
| `k=0` cells are the 8 axis-balanced 6-tuples | proved by independent bit choices |
| every nonempty `S` has a nonempty fiber | proved; each fiber has 8 cells |
| swap on a balanced axis and joint flip on an unbalanced axis fix `λ` | proved |
| not a rank-1 projector and not Aut leftover | negative check; pairing unsupplied |
| formation site, process, or rate | open; not used |
| axiom edit | none |

## No-go discipline

The only wall is the identification of occupancy-only labels with a rank-1
projector or with the Aut leftover of `#6383`. The positive census of eight
pairs is not itself an impossibility claim.

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| count distinct occupancy pairs `(S,k)` on 64 cells | **USED** | image size 8 |
| treat leftover Aut yes/no as the occupancy label | **ATTEMPTED** | that character is `#6383`, a different object |
| identify each `(S,k)` with a rank-1 projector | **ATTEMPTED** | requires an unsupplied axis–Pauli pairing |
| use `Aut(M_2)` to reduce cells | **ATTEMPTED** | `Aut(M_2)` is not used |
| derive formation site or rate from `S` | **ATTEMPTED** | `S` is occupancy content, not a formation rule |
| adopt the eight pairs as a physical menu | **ATTEMPTED** | displayed, not adopted |

### N2 — wall independence

One identification wall is claimed: occupancy pairs are not projectors and
not Aut leftover. The image-size count is a positive finite census, not a
second wall.

### N3 — hidden-wall scan

The carrier, bit order, and label map are declared. No formation process,
clock, operator pairing, leftover Aut character, or adopted physical menu is
imported.

### N4 — residual matching

The residual after this census is any later pairing of occupancy bits with
operators, formation, or Aut data. The residual is not closed and is not
enlarged.

### N5 — certificate granularity

```text
per-element: executed — every one of the 64 cells is labeled
per-site: executed — the three axes x,y,z are the only site directions used
per-mode: not applicable — no modal or spectral decomposition is used
per-block: executed — image, fibers, invariances, and the projector refusal
lattice-wide: not executed — no global history or formation law is claimed
```

### N6 — partial-closure paths

A separately supplied axis–Pauli pairing could still define projectors. A
separately supplied formation rule could still lock one admissible
possibility. Those routes remain live and are outside the occupancy census.

### N7 — steelman

The strongest objection is that `k` is redundant because `k=|S|`, so the
true label is just `S`. Correct that `k` is determined by `S`. The displayed
object is nevertheless the pair `(S,k)`, as required by the occupancy-lock
split against projectors. Redundancy of the integer does not identify the
pair with a projector.

### N8 — cross-cycle echo

Claim `#6383` split Aut yes/no leftover character from other content. This
note does not replay that split. It pins only the occupancy-only label set
`(S,k)` and refuses the projector reading.

## Boundaries and explicit non-claims

- The eight pairs are displayed, not adopted.
- Occupancy bits are a declared finite alphabet, not a derived local
  possibility domain.
- The theorem does not construct `Aut(M_2)` and does not consume leftover
  Aut character.
- The theorem does not supply formation site, process, rate, or readout
  values beyond occupancy equality.
- No axiom, primitive, registry, or audit verdict is edited.

FAIL / DO NOT SHIP for “occupancy labels are rank-1 projectors”, “this is the
Aut leftover of `#6383`”, or “the eight pairs are adopted physical content”.

## Verification

Run:

```bash
python3 scripts/occupancy_lock_label_pairs_2026_08_15.py
```

The runner enumerates the 64 cells, checks the image, fibers, invariances,
and the projector/Aut refusal, and pins the declared source paths. Expected
summary:

```text
TOTAL: PASS>=14 FAIL=0
```
