---
claim_id: record_additivity_does_not_supply_newton_product_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Scalar Record additivity supplies I(S∪T)=I(S)+I(T) on disjoint finite collections, a function of the sum only. That single scalar cannot separate (m_s,m_t)=(2,0) from (1,1) from (0,2), so it cannot equal the product m_s m_t. The Newton kernel Green pairing remains source-linear and does not produce a test-mass factor. A declared pairing π(S,T)=I(S)I(T) would be a second object; this note does not install that pairing, edit an axiom, or claim gravity is impossible."
upstream_dependencies:
  - minimal_axioms
  - newton_law_derived_note
runner: scripts/record_additivity_does_not_supply_newton_product_2026_08_13.py
---

# Record Additivity Does Not Supply The Newton Product

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** finite exact algebra of scalar Record additivity versus the
bilinear product `m_s m_t` used by a Newton test-mass factor.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/record_additivity_does_not_supply_newton_product_2026_08_13.py`](../scripts/record_additivity_does_not_supply_newton_product_2026_08_13.py)

## Result Up Front

The current Record axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies a
single additive scalar on finite pairwise-disjoint record collections:

> For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

Let `S` and `T` be finite pairwise-disjoint record collections, and write
`I(S)=m_s`, `I(T)=m_t` for formal integers or rationals. Additivity forces

`I(S∪T)=I(S)+I(T)=m_s+m_t`.

Any function of that one scalar is a function of the sum only. It cannot
separate the three pairs `(m_s,m_t)=(2,0)`, `(1,1)`, `(0,2)`, which share
the same union readout `2`. The products of those pairs are `0`, `1`, `0`.
Therefore no function of `I(S∪T)` equals `m_s m_t` on those three inputs.

The Newton potential-kernel packet
[`NEWTON_LAW_DERIVED_NOTE.md`](NEWTON_LAW_DERIVED_NOTE.md) already records
the source-linear Green pairing

`G(r)=1/(4 pi r)`, `phi=m_s G`, `|grad phi|=m_s/(4 pi r^2)`.

That gradient still carries no test-mass factor. Multiplying by `m_t` is an
extra bilinear map `B(S,T)=I(S)I(T)`, which is not determined by `I` on the
union. The same packet lists both `F = -M_test grad(phi)` and the physical
product law `M_source M_test` among its non-claims.

If a second readout of `T`, or a declared pairing `π(S,T)`, is supplied,
then `B=I(S)I(T)` is well-defined as a two-argument map. That pairing is
the missing object. It is not `I` on `S∪T`, is not installed here, and is
not claimed to be physical.

This is a scoped algebraic gap. It does not say gravity is impossible.

## Machine Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "I on a disjoint union is the sum, and the three-pair rejector shows that sum cannot equal the product. The Newton Green pairing remains source-linear. A two-argument pairing would supply B=I(S)I(T) but is not Record additivity."
trace_class: negative_route_pruning
target_claim_id: record_additivity_does_not_supply_newton_product
target_blocker_text: "decide whether scalar Record additivity yields the Newton product M_source M_test"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the three-pair rejector, source-linear Green pairing, and the displayed two-argument escape; physical pairing remains open"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work with finite record collections in the sense of the Record axiom. A
**collection** is a finite family of pairwise-disjoint records, each carrying
a formal rational strength. Scalar readout `I` is the sum of those
strengths. The empty collection has `I(empty)=0`. If `A` and `B` are
disjoint, additivity is

`I(A∪B)=I(A)+I(B)`.

Fix two disjoint collections `S` and `T` and write

`m_s := I(S)`, `m_t := I(T)`.

The three rejector pairs below are realized by unit-strength atoms, and
again by lumped rational strengths with the same totals. In every
realization the only Record datum on the disjoint union is the one scalar
`I(S∪T)`.

| pair `(m_s,m_t)` | unit-atom realization | `I(S∪T)` | `m_s m_t` |
|---|---|---|---|
| `(2,0)` | `S={s1,s2}`, `T=empty` | `2` | `0` |
| `(1,1)` | `S={s1}`, `T={t1}` | `2` | `1` |
| `(0,2)` | `S=empty`, `T={t1,t2}` | `2` | `0` |

The same sums and products are obtained from lumped strengths
`S` of total `2` with `T` empty, `S` of total `1` with `T` of total `1`,
and `S` empty with `T` of total `2`. An extra rational witness with the
same union sum is `(m_s,m_t)=(3/2,1/2)`, which has `I(S∪T)=2` and
product `3/4`.

A **function of the union scalar** is any map of the form
`f(I(S∪T))`. A **bilinear pairing** of the two collections is any map
`B(S,T)` that is separately linear in `I(S)` and in `I(T)`. The product
pairing used by a Newton test-mass factor is

`B(S,T)=I(S)I(T)=m_s m_t`.

The Newton packet supplies the radial Green kernel and its source-linear
potential, not that pairing. Its in-scope algebra, with source coefficient
written `m_s`, is

```text
G(r) = 1/(4 pi r),
phi(r) = m_s G(r) = m_s/(4 pi r),
|grad phi| = m_s/(4 pi r^2).
```

The 2026-05-29 scope repair of that packet removed the force/source
coupling `F = -M_test grad(phi)` from the load-bearing claim. The
source-side mass-linearity lemma
[`G_NEWTON_MASS_LINEAR_POISSON_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-05-10.md`](G_NEWTON_MASS_LINEAR_POISSON_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-05-10.md)
is likewise only linearity in the source mass.

## Exact Target And Obligation Graph

**Exact target.** Decide whether the single additive scalar `I` on a
disjoint union can equal the Newton product `m_s m_t`, and whether the
already-recorded Green pairing produces a test-mass factor.

| Obligation | Role | Disposition |
|---|---|---|
| pin `I(empty)=0` and disjoint additivity | premise | quoted from the axiom memo |
| pin Newton non-claim of `F = -M_test` and `M_source M_test` | premise | quoted from the Newton packet |
| show `I(S∪T)` is the sum only | Theorem 1 | additivity |
| rejector `(2,0)`, `(1,1)`, `(0,2)` | Theorem 1 | common sum `2`, products `0,1,0` |
| show the Green gradient has no `m_t` | Theorem 2 | `|grad phi|=m_s/(4 pi r^2)` |
| exhibit `B=I(S)I(T)` as a two-argument map | Theorem 3 | declared pairing; not physical |
| derive a physical pairing or force law | autonomous closure | open |
| claim gravity is impossible | non-claim | not attempted |

## Theorem 1 — A Function Of `I(S∪T)` Cannot Equal The Product

Let `S` and `T` be disjoint. Record additivity and `I(empty)=0` give

`I(S∪T)=I(S)+I(T)=m_s+m_t`,

and `I(S∪empty)=I(S)`, `I(empty∪T)=I(T)`. The value `I(S∪T)` is therefore
exactly the sum. Any function of that one scalar is constant on the level
set `m_s+m_t=σ`.

On the three rejector pairs the sum is the same:

`(2,0): I(S∪T)=2`,
`(1,1): I(S∪T)=2`,
`(0,2): I(S∪T)=2`.

The products are not the same:

`(2,0): m_s m_t=0`,
`(1,1): m_s m_t=1`,
`(0,2): m_s m_t=0`.

Suppose there existed a function `f` of one scalar such that
`f(I(S∪T))=m_s m_t` on those three inputs. Then `f(2)=0` from `(2,0)` and
`f(2)=1` from `(1,1)`, which is impossible. The same collision occurs for
every other pair of distinct products with a common sum, including the
rational witness `(3/2,1/2)` with product `3/4`.

Explicit one-variable trial maps fail in the same way. The identity
`f(σ)=σ` returns `2,2,2`. The constant `f(σ)=1` matches only `(1,1)`. The
quadratic `f(σ)=σ(σ-2)` returns `0,0,0` and matches the two vanishing
products but not `(1,1)`. No choice of `f` hits `0,1,0` at a single
argument `2`.

Thus `I` on the disjoint union cannot distinguish `(2,0)`, `(1,1)`, and
`(0,2)`, while `m_s m_t` can. Scalar Record additivity does not yield the
product law.

## Theorem 2 — The Newton Green Pairing Still Has No Test-Mass Factor

The Newton packet's in-scope algebra is the radial kernel `G(r)=1/(4 pi r)`
and the source-linear potential `phi=m_s G`. Differentiating in `r>0` gives

`d phi/dr = -m_s/(4 pi r^2)`, `|grad phi|=m_s/(4 pi r^2)`.

The right-hand side does not depend on `m_t`. On the three rejector pairs,
at any common `r>0`, the gradient magnitudes are

`(2,0): 2/(4 pi r^2)`,
`(1,1): 1/(4 pi r^2)`,
`(0,2): 0`.

The would-be product-law magnitudes `m_s m_t/(4 pi r^2)` are instead

`(2,0): 0`,
`(1,1): 1/(4 pi r^2)`,
`(0,2): 0`.

The pair `(2,0)` is the witness: the Green gradient sees source strength
`2` and is not the vanishing product. The pair `(1,1)` agrees only because
`m_t=1`, which is not a derivation of a test-mass factor. Multiplying
`|grad phi|` by `m_t` is exactly the extra bilinear map

`B(S,T)=I(S)I(T)`,

which Theorem 1 showed is not a function of `I(S∪T)`. Source-side
linearity of the Poisson potential, as in the G-Newton mass-linear lemma,
likewise scales only with `m_s`.

The Newton packet already lists the test-mass force/source response rule
`F = -M_test grad(phi)` and the physical product law `M_source M_test` as
non-claims. Theorem 2 is the matching algebraic reason: the kernel algebra
never produces the second factor.

## Theorem 3 — A Declared Pairing Supplies `B`, And Is A Second Object

Suppose a second readout of `T` is available separately from the readout of
`S`, or a pairing `π(S,T)` of the two collections is declared. Then the
product

`B(S,T) := I(S)I(T)`

is well-defined. On the three rejector pairs it returns `0`, `1`, `0`, so
it does distinguish `(1,1)` from `(2,0)` and from `(0,2)`. It is a
function of two scalars, not of their sum.

This pairing is the missing object for a product law. It is not Record
additivity. It is not `I(S∪T)`. The four axioms do not name `π`. This note
does not install `π`, does not argue that an axiom update is required, and
does not claim that forming records physically carry a source/test split.

The discriminating gate is only this: a bilinear pairing on two disjoint
additively-read collections can produce an `M_s M_t` number; `I` alone on
the disjoint union cannot. Both sides are exhibited.

## Boundary And Non-Claims

The note does not:

- edit an axiom, or argue that an axiom update is necessary;
- claim that gravity is impossible, or that a Newton force law cannot be
  reached by some later bridge;
- identify `B(S,T)=I(S)I(T)` with a physical Record law;
- restore `F = -M_test grad(phi)` as a derived response rule;
- derive the physical product law `M_source M_test`;
- close gravitational coupling normalization, `G_N`, or a continuum
  Einstein equation;
- exhaust other two-collection maps.

The scope is the exact gap: scalar Record additivity does not yield the
product law.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Record additivity sentence and `I(empty)=0` | premise | quoted; no edit |
| Newton kernel `G(r)=1/(4 pi r)` and source-linear `phi` | common objects | restated from the Newton packet |
| Newton non-claim of `F = -M_test` and `M_source M_test` | scope pin | quoted; not reversed |
| three-pair rejector and `B=I(S)I(T)` | declared algebra | computed here |
| physical source/test pairing | escape route | live, not derived |

The exact advance is a finite additivity-versus-product theorem. Independent
audit remains required before any effective status may change.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The Newton packet removed the test-mass product from its claim. This note proves the matching algebraic gap on Record additivity. |
| V2 | New content? | Yes: the three-pair rejector, the explicit mismatch of `|grad phi|` with `m_s m_t/(4 pi r^2)`, and the two-argument pairing as a second object. |
| V3 | Independently checkable? | Yes. The runner recomputes `I` from collections, the products from `m_s m_t`, and the Green derivative from `G`. |
| V4 | More than a restatement? | Yes. The Newton non-claim is a scope sentence; this note supplies the additivity-versus-bilinear witness. |
| V5 | One-step relabel? | No. Quoting additivity and quoting the Newton non-claim does not by itself exhibit the `(2,0),(1,1),(0,2)` collision. |

## Primary Runner

[`scripts/record_additivity_does_not_supply_newton_product_2026_08_13.py`](../scripts/record_additivity_does_not_supply_newton_product_2026_08_13.py)
recomputes disjoint additivity, the three-pair rejector, the Green
gradient, and the two-argument pairing in exact arithmetic.
