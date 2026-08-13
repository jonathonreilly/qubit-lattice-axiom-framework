---
claim_id: bilinear_normalized_pairing_uniqueness_newton_product_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The unique Q-bilinear map B:Q×Q→Q with B(1,1)=1 is ordinary multiplication, so any pairing that factors as B(I(S),I(T)) and is Q-bilinear and normalized equals π(S,T)=I(S)I(T); Record additivity, content-only readout, and I(empty)=0 do not select that pairing."
upstream_dependencies:
  - minimal_axioms
  - newton_law_derived_note
runner: scripts/bilinear_normalized_pairing_uniqueness_newton_product_2026_08_13.py
---

# Bilinear Normalized Pairing Uniqueness And The Newton Product Map

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact Q-bilinear uniqueness of multiplication on the Record
value group, and the constructed two-argument map `π(S,T)=I(S)I(T)`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/bilinear_normalized_pairing_uniqueness_newton_product_2026_08_13.py`](../scripts/bilinear_normalized_pairing_uniqueness_newton_product_2026_08_13.py)

## Result Up Front

The current Record axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies a
content-only additive scalar on finite pairwise-disjoint record collections.
Those sentences are quoted only as premises and are not edited:

> Only records are readable. A readout value is determined by record content alone.
> For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

Write `m_s := I(S)` and `m_t := I(T)` in the value group `Q`. The single
additive scalar on a disjoint union is the sum `I(S∪T)=I(S)+I(T)`. This
note constructs a second, two-argument map

`π(S,T) := I(S) I(T)`

on every pair of finite collections. Disjointness is not required for `π`.
The map is bi-additive in each slot separately, vanishes if either argument
is empty, and returns `0`, `1`, `0` on the three pairs `(2,0)`, `(1,1)`,
`(0,2)`. It returns `12` on unit collections of strengths `3` and `4`.

Any `Q`-bilinear map `B: Q×Q → Q` with `B(1,1)=1` equals ordinary
multiplication: `B(x,y)=x y`. Therefore any pairing that factors as
`B(I(S), I(T))` and is `Q`-bilinear and normalized is exactly `π`.

That uniqueness is among bilinear normalized maps on `Q`. Record additivity,
content-only readout, and `I(empty)=0` do not select a two-argument pairing.
The union readout cannot equal `π` on the three-pair rejector. The Newton
packet
[`NEWTON_LAW_DERIVED_NOTE.md`](NEWTON_LAW_DERIVED_NOTE.md) already lists
both `F = -M_test grad(phi)` and the physical product law `M_source M_test`
among its non-claims, and its Green pairing remains source-linear. This
note does not install `π`, does not claim a Newton force law, and does not
edit an axiom.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Q-bilinear maps Q×Q→Q are determined by B(1,1); B(1,1)=1 forces B(x,y)=xy. The constructed pairing π=I(S)I(T) is that unique map on strengths. Record additivity still does not select it."
trace_class: upstream_support
target_claim_id: newton_product_pairing
target_blocker_text: "supply the bilinear product M_source M_test from Record content"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "The unique bilinear normalized pairing on Q is multiplication; Record still does not select it. Do not adopt axiom text."
conditional_surface_status: "exact for Q-bilinear uniqueness of multiplication and the three-pair rejector; Record still does not select the pairing"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work with finite labeled record collections. A **collection** is a finite
family of labeled atoms, each carrying a formal rational strength. Scalar
readout `I` is the sum of those strengths. The empty collection has
`I(empty)=0`. If `A` and `B` are pairwise disjoint, Record additivity is

`I(A∪B)=I(A)+I(B)`.

The value group is `Q`. Strengths are `m_s = I(S)` and `m_t = I(T)` in `Q`.

The **product pairing** is the two-argument map

`π(S,T) := I(S) I(T)`.

It is defined for every pair of finite collections. Overlap of labels is
allowed because the definition never forms a union. The same pairing is
written `pairing(S,T)` in the runner; both names call the same product.

A map `B: Q×Q → Q` is **`Q`-bilinear** when

`B(x+x', y) = B(x,y)+B(x',y)`,
`B(x, y+y') = B(x,y)+B(x,y')`,
`B(q x, y) = q B(x,y) = B(x, q y)` for every `q` in `Q`.

It is **normalized** when `B(1,1)=1`.

The three rejector pairs, realized by unit-strength atoms, are:

| pair `(m_s,m_t)` | unit-atom realization | `I(S∪T)` | `π(S,T)` |
|---|---|---|---|
| `(2,0)` | `S={s0,s1}`, `T=empty` | `2` | `0` |
| `(1,1)` | `S={s0}`, `T={t0}` | `2` | `1` |
| `(0,2)` | `S=empty`, `T={t0,t1}` | `2` | `0` |

A further unit-atom witness is `S={s0,s1,s2}`, `T={t0,t1,t2,t3}`, with
`π(S,T)=12`. Lumped rationals with the same totals give the same products,
including `(3/2,1/2)` with product `3/4`.

The Newton packet supplies the radial Green kernel as a formal symbol

```text
G(r) = 1/(4 pi r),
phi(r) = M G(r) = M/(4 pi r),
|grad phi| = M/(4 pi r^2).
```

Exact checks below use the source-linear coefficient `I(S)/r^2`. That
coefficient carries no `I(T)` factor.

## Exact Target And Obligation Graph

**Exact target.** Construct `π(S,T)=I(S)I(T)`, prove it is the unique
`Q`-bilinear normalized pairing on the value group, and record that Record
additivity does not select it.

| Obligation | Role | Disposition |
|---|---|---|
| pin `I(empty)=0`, content-only readout, and disjoint additivity | premise | quoted from the axiom memo |
| pin Newton non-claim of `F = -M_test` and `M_source M_test` | premise | quoted from the Newton packet |
| show `π` is well-defined and bi-additive | Theorem 1 | product of two scalars |
| uniqueness of normalized `Q`-bilinear maps | Theorem 2 | `B(x,y)=x y B(1,1)` |
| show the union readout is not bilinear | Theorem 3 | three-pair rejector |
| show the Green gradient has no `I(T)` | Theorem 4 | source-linear kernel |
| record that Record does not select `π` | Theorem 5 | scoped residual |
| install `π` as physical, or derive a Newton force law | autonomous closure | open |
| edit an axiom to name `π` | non-claim | not required |

## Theorem 1 — Well-Defined Product Pairing

**Claim.** `π(S,T)=I(S)I(T)` is defined for every pair of finite
collections. If `S=S1∪S2` is a disjoint union then
`π(S,T)=π(S1,T)+π(S2,T)`, and symmetrically in `T`. `π(empty,T)=0`.
The pairing separates `(2,0)`, `(1,1)`, `(0,2)` as `0`, `1`, `0`, and
`π(unit_3, unit_4)=12`.

**Proof.** `I` is defined on every finite collection, so the product of the
two scalars is defined even when labels overlap. If `S=S1∪S2` is disjoint
then additivity gives `I(S)=I(S1)+I(S2)`, hence

`π(S,T)=(I(S1)+I(S2)) I(T)=I(S1)I(T)+I(S2)I(T)=π(S1,T)+π(S2,T)`.

The symmetric identity in `T` is the same computation. The empty collection
has `I(empty)=0`, so `π(empty,T)=0`.

On the three unit-atom rejector pairs the products are

`(2,0): 2·0=0`,
`(1,1): 1·1=1`,
`(0,2): 0·2=0`.

On unit collections of strengths `3` and `4` the product is `3·4=12`. The
same `12` is recovered by bi-additivity: if `S1` has two units, `S2` has
one unit, and `T` has four units, then

`π(S1,T)+π(S2,T)=8+4=12=π(S1∪S2,T)`.

## Theorem 2 — Uniqueness On The Value Group

**Claim.** Let `B: Q×Q → Q` be `Q`-bilinear with `B(1,1)=1`. Then
`B(x,y)=x y` for every `x,y` in `Q`. Consequently any pairing that factors
as `B(I(S), I(T))` and is `Q`-bilinear and normalized is exactly `π`.

**Proof.** `Q`-homogeneity in each slot gives

`B(x,y)=B(x·1, y·1)=x B(1, y·1)=x y B(1,1)`.

Normalization `B(1,1)=1` therefore forces `B(x,y)=x y`.

The same identity is visible from additivity before homogeneity is used.
For a nonnegative integer `n`,

`B(n,y)=B(1+⋯+1,y)=n B(1,y)`,

and `B(1,y)=B(1, y·1)=y B(1,1)`. Three summands of `B(1,4)` therefore
recover `12` when `B(1,1)=1`. For a rational `p/q`,

`q B(p/q, y)=B(p,y)=p B(1,y)`,

so `B(p/q,y)=(p/q) B(1,y)`. The second slot is symmetric. Thus every
`Q`-bilinear map is multiplication by the single scalar `B(1,1)`.

If a pairing of collections factors through the value group as
`Π(S,T)=B(I(S), I(T))` with this `B` and with `B(1,1)=1`, then
`Π(S,T)=I(S)I(T)=π(S,T)`.

A bilinear map with `B(1,1)=2` is `B(x,y)=2 x y`. It fails normalization,
so it is not the unique normalized pairing.

## Theorem 3 — Additivity On The Union Is Not Bilinear

**Claim.** On disjoint pairs the single-argument union readout
`U(S,T):=I(S∪T)` equals `I(S)+I(T)` and cannot equal `π` on the three-pair
rejector.

**Proof.** Record additivity and `I(empty)=0` give
`I(S∪T)=I(S)+I(T)` whenever `S` and `T` are disjoint. The three rejector
pairs are pairwise disjoint and share the same union scalar:

`(2,0): I(S∪T)=2`,
`(1,1): I(S∪T)=2`,
`(0,2): I(S∪T)=2`.

The products are `0`, `1`, `0`. No function of the single scalar `2` can
return both `0` and `1`. In particular `U` cannot equal `π` on those three
inputs. The same collision is the reason `U` is not `Q`-bilinear: a bilinear
map vanishing on `(2,0)` and on `(0,2)` would vanish on `(1,1)` after
rescaling, but `π(1,1)=1`.

## Theorem 4 — Green Pairing Still Source-Linear

**Claim.** The Newton kernel `G(r)=1/(4π r)`, kept as a formal symbol,
produces a source-linear gradient `|∇φ| ∝ I(S)/r^2` that carries no `I(T)`
factor. Multiplying that coefficient by `I(T)` is exactly `π`.

**Proof.** The packet algebra is `phi = I(S) G` and
`|grad phi| = I(S)/(4π r^2)`. The right-hand side does not depend on
`I(T)`. Exact checks use the coefficient `I(S)/r^2`. On the three rejector
pairs, at any common `r>0`, those coefficients are `2/r^2`, `1/r^2`, `0`.
The product-law coefficients `π(S,T)/r^2` are `0`, `1/r^2`, `0`. The pair
`(2,0)` is the witness: the Green gradient sees source strength `2` and is
not the vanishing product. Multiplying the Green coefficient by `I(T)`
returns `I(S)I(T)/r^2`, which is `π(S,T)/r^2`.

The Newton packet already lists `F = -M_test grad(phi)` and
`M_source M_test` as non-claims. Theorem 4 is the matching kernel fact:
the source-linear Green pairing never produces the second factor.

## Theorem 5 — Scoped Residual

**Claim.** `π` is an extra two-argument object. Record additivity,
content-only readout, and `I(empty)=0` do not select it. This note does not
adopt `π`, does not claim Newton's law, and does not edit an axiom.

**Proof.** Theorems 1 and 2 construct `π` and prove uniqueness *among
`Q`-bilinear normalized maps on the value group*. Those hypotheses —
two-argument domain, bilinearity, and `B(1,1)=1` — are not Record
additivity. Content-only readout says that a readout value is determined by
record content alone; it names one scalar, not a pairing of two collections.
`I(empty)=0` fixes the additive identity and does not name a second slot.

The attempted one-argument substitutes fail for independent reasons:

- union readout returns `2,2,2` on the rejector, not `0,1,0`;
- source-only readout `I(S)` returns `1` on both `(1,1)` and `(1,2)`;
- the Green coefficient is source-linear and misses `I(T)`.

Declaring `π` makes the product well-defined. That declaration is the extra
object. It is not forced by the quoted Record sentences. An axiom edit that
named `π` is not required by uniqueness of bilinear maps on `Q`.

The residual is scoped. It does not say that a later physical selection of
`π` is closed, and it does not say that a Newton force law cannot be reached
by some later bridge.

## Boundary And Non-Claims

The note does not:

- edit an axiom, or argue that an axiom update is necessary;
- identify `π` with a physical Record law or a Newton force law;
- restore `F = -M_test grad(phi)` as a derived response rule;
- derive the physical product law `M_source M_test`;
- close gravitational coupling normalization, `G_N`, or a continuum
  Einstein equation;
- exhaust other two-collection maps that are not `Q`-bilinear or not
  normalized.

The scope is the exact uniqueness of the bilinear normalized pairing on
`Q`, together with the residual that Record does not select it.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Record additivity sentence and `I(empty)=0` | premise | quoted; no edit |
| current content-only readout sentence | premise | quoted; no edit |
| Newton kernel `G(r)=1/(4 pi r)` and source-linear `phi` | common objects | restated from the Newton packet |
| Newton non-claim of `F = -M_test` and `M_source M_test` | scope pin | quoted; not reversed |
| three-pair rejector and `π=I(S)I(T)` | declared algebra | computed here |
| uniqueness of normalized `Q`-bilinear maps | Theorem 2 | computed here |
| physical source/test pairing | residual | live, not derived |

The exact advance is a finite bilinear-uniqueness theorem on `Q`. Independent
audit remains required before any effective status may change.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The Newton packet lists the physical product law `M_source M_test` and `F = -M_test grad(phi)` as non-claims. This note constructs the unique bilinear normalized pairing that would supply that product on strengths. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for bilinear pairing uniqueness, Newton product pairing, `Q`-bilinear normalization `B(1,1)=1`, and `π(S,T)=I(S)I(T)`. Hits: the Newton packet names `M_source M_test` only as a non-claim; the G-Newton mass-linear lemma is source-side linearity and explicitly refuses a force product law; neutrino and KCPT “normalized pairing” notes are different objects (Majorana blocks, symplectic forms). No landed uniqueness theorem for a bilinear Newton product pairing appears on that commit. An unmerged additivity-gap note is a sibling, not a premise. |
| V3 | Independently checkable? | Textbook uniqueness of bilinear forms on a one-dimensional `Q`-vector space does not mention Record collections or the Newton packet. The runner recomputes `π` from collections, reconstructs `B(n,y)` by integer additivity, and checks `B(x,y)=x y B(1,1)` in exact rationals. |
| V4 | More than a restatement? | Yes. The three-pair rejector together with `π(unit_3,unit_4)=12` and the uniqueness identity `B(x,y)=x y` are not restatements of the Newton non-claim sentence. |
| V5 | One-step relabel? | No. A non-claim that the packet does not derive `M_source M_test` is not a uniqueness theorem for bilinear normalized maps on `Q`. |

## No-Go Discipline Gate (Theorem 5 only)

The negative claim is restricted to this: Record additivity, content-only
readout, and `I(empty)=0` do not select the extra pairing `π`. The gate
does not ship a global non-existence theorem against later physical
selection, and it does not ship a Newton force law.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| union readout | set `U(S,T)=I(S∪T)` on disjoint pairs and ask it to equal `π` | Theorem 3: the three-pair rejector returns `2,2,2` against `0,1,0` | **ATTEMPTED** |
| source-only readout | set `Π(S,T)=I(S)` | fails `(1,1)` versus `(1,2)`: both return `1`, while `π` returns `1` and `2` | **ATTEMPTED** |
| Green pairing | read `|∇φ| ∝ I(S)/r^2` as the product law | Theorem 4: no `I(T)` factor; `(2,0)` is the witness | **ATTEMPTED** |
| declared `π` | introduce `π(S,T)=I(S)I(T)` as a second object | Theorems 1--2: well-defined and unique among bilinear normalized maps; Theorem 5: not selected by Record | **ATTEMPTED** (escape) |
| axiom edit naming `π` | add a pairing sentence to the Record axiom | not required by uniqueness on `Q`; see N6 | **ATTEMPTED** |
| bilinear map with `B(1,1)=2` | keep bilinearity but drop normalization | Theorem 2: `B(x,y)=2xy`, which fails `B(1,1)=1` | **ATTEMPTED** |

### N2 — wall independence

Theorem 5 closes only the claim that the quoted Record sentences select
`π`. It does not close uniqueness among bilinear maps (Theorem 2), the
Green source-linearity (Theorem 4), a later physical source/test split, or
a Newton response rule. Those walls remain independent. Uniqueness of
normalized bilinear maps on `Q` does not by itself make `π` a Record
output.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| finite labeled collections and `I` | declared Record objects |
| value group `Q` | declared scalar range of `I` |
| `π(S,T)=I(S)I(T)` | explicit two-argument construction |
| `Q`-bilinearity and `B(1,1)=1` | explicit hypotheses of Theorem 2 |
| three-pair rejector and `(3,4)=12` | explicit witnesses |
| Green kernel `G(r)=1/(4π r)` | formal symbol from the Newton packet |
| axiom edit naming `π` | live governance path; not required |
| physical Newton force law | open; not assumed |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | content-only readout; disjoint additivity; `I(empty)=0` | quoted as premises only; no edit |
| [`docs/NEWTON_LAW_DERIVED_NOTE.md`](NEWTON_LAW_DERIVED_NOTE.md) | kernel algebra; non-claim of `F = -M_test` and `M_source M_test` | scope pin only; not reversed |

No unmerged additivity-gap note is used as a parent. The three-pair
rejector is recomputed here.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | rejector pairs `(2,0)`, `(1,1)`, `(0,2)` and the unit witness `(3,4)` | no classification of every two-collection map |
| per site | two finite collections and their scalar strengths | no composite carrier or lattice source field |
| per mode | value-group bilinearity, not spectral modes | no harmonic-mode exhaustion |
| per block | uniqueness of normalized bilinear maps, plus the Record residual | no Newton force law and no axiom edit |
| lattice-wide | checked and not executed | no lattice-wide gravity statement |

The residual is a two-argument selection gap. It is not lattice-wide.

### N6 — live partial-closure paths

1. A later derivation that a physical source/test split exists and that
   the pairing of those collections is `Q`-bilinear and normalized.
2. A later selector that uses more than Record content — for example a
   declared two-argument readout — to name `π` without editing an axiom.
3. The Green kernel together with an independent test-mass response rule,
   which would multiply the source-linear gradient by `I(T)`.
4. An owner-approved typed axiom addition that named a pairing. Uniqueness
   on `Q` does not require that addition.

The quoted Record sentences already name content-only readout, disjoint
additivity, and `I(empty)=0`. They do not name `π`. No axiom sentence is
required by Theorem 5.

### N7 — hostile steelman

> Uniqueness of bilinear maps on `Q` already means Record selected `π`:
> the only bilinear pairing of two strengths is the product, so the
> product law is a theorem of additivity.

**Answer.** Uniqueness is conditional on a two-argument `Q`-bilinear
normalized map. Record additivity supplies one additive scalar, not that
map. Theorem 3 exhibits a one-argument substitute that is additive and is
not `π`. Theorem 5 is exactly the gap between “unique if bilinear and
normalized” and “selected by Record.”

### N8 — cross-cycle echo

The Newton packet already removed `F = -M_test grad(phi)` and
`M_source M_test` from its load-bearing claim. The G-Newton mass-linear
lemma is source-side linearity only. The present uniqueness theorem does
not reverse those non-claims. It answers a different question: among
bilinear normalized maps on `Q`, the pairing is multiplication; among
Record readouts, that pairing is still extra.

**Gate disposition.** PASS for bilinear uniqueness of multiplication and
for the scoped residual that Record does not select `π`. FAIL / DO NOT
SHIP for “Newton's law is derived,” “`π` is physical,” or “an axiom edit
is required.”

## Primary Runner

[`scripts/bilinear_normalized_pairing_uniqueness_newton_product_2026_08_13.py`](../scripts/bilinear_normalized_pairing_uniqueness_newton_product_2026_08_13.py)
recomputes `π` from collections, the three-pair rejector, the unit witness
`12`, `Q`-bilinear uniqueness, the union-versus-product collision, and the
source-linear Green coefficient in exact rational arithmetic. Identity
gates call `pi(S,T)` and `pairing()`. Replacing `pi` by `I(S)+I(T)` must
fail the three-pair rejector. Replacing `pi` by `I(S)` must fail `(1,1)`
versus `(1,2)`. A bilinear map with `B(1,1)=2` must fail uniqueness at
normalization.
