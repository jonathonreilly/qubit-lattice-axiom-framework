---
claim_id: f_cut_k4_v30_two_site_miss_equality_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the 2-site miss sets of F_cut maps (1,1,1,0,0) and (1,1,1,0,1) are equal. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_k4_v30_two_site_miss_equality_2026_08_15.py
---

# The Two Vertex3=0 k=4 F_cut Maps Miss the Same 2-Site Seeds

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact 2-site fill/miss comparison of two displayed F_cut maps on
the twelve-vertex two-cube with off-patch occupancy `0`. No physical
Admissibility selector and no axiom edit are asserted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_k4_v30_two_site_miss_equality_2026_08_15.py`](../scripts/f_cut_k4_v30_two_site_miss_equality_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write remaining bits in the order `(wt1, opp2, adj2, vertex3, mixed3)`.
On the two-cube with off-patch occupancy `0`, the two F_cut maps

```text
f00 = (1, 1, 1, 0, 0),
f01 = (1, 1, 1, 0, 1)
```

each fill `cov = 36` of the `C(12,2) = 66` unordered two-site seeds and
therefore each miss `|M| = 30` seeds. Their miss sets are equal:

```text
|intersection| = 30,
|symmetric difference| = 0,
equality bit = 1.
```

So mixed3 is free on the 2-site fill set inside this vertex3=0 k=4 pair.
Displayed, not adopted. Do not adopt mixed3. Do not list the 30 seeds.
The 30 missed seeds are not listed.

Not leftover-character of #6446: that only reported cov=36.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact occupancy-to-lock enumeration on one finite two-cube compares the 2-site miss sets of two displayed F_cut maps."
trace_class: frontier_discovery
target_claim_id: f_cut_k4_v30_two_site_miss_equality
target_blocker_text: "whether the two vertex3=0 k=4 F_cut maps miss the same 2-site seeds"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied two-cube with off-patch occupancy 0; no physical Admissibility selector is asserted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies `Z^3` with
  nearest-neighbor adjacency and proper cubic rotations. The live
  Admissibility sentence supplies one covariant nearest-neighbor rule. Both
  are quoted without rewrite.
- **Explicit theorem-domain condition:** the two-cube is the twelve sites
  `{0,1,2} × {0,1} × {0,1}`. Off-patch occupancy is the explicit `0`
  default; a blank-block is a different rule and is not used.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing the displayed equality, or mixed3, into
  Admissibility remains a separate obligation.
  Do not write the equality into Admissibility.

## Exact Objects

A neighbor 6-tuple `c ∈ {0,1}^6` is typed by the three axis pairs
`(c_{+μ}, c_{-μ})`. The axis type is
`(n_unbalanced, n_both, n_empty)`. Cube rotations preserve that type.
`F_cut` is the cube-covariant class with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. After those constraints, five remaining bits label a map:
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced, equivalently
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

Dynamics are occupancy-to-lock: an unlocked two-cube site locks when `f`
accepts its six-direction neighborhood. A seed fills when the iteration
reaches all twelve sites. The miss set of `f` is the collection of
two-site seeds that do not fill.

## Theorem 1 — both maps have cov = 36

Each of `f00` and `f01` has `(wt1, opp2, adj2) = (1, 1, 1)` and
`vertex3 = 0`. Each fills all four long-axis two-site seeds
`{(0,y,z),(2,y,z)}`, so both are k=4 maps. Direct enumeration on the 66
two-site seeds reconfirms

```text
cov(f00) = 36,
cov(f01) = 36.
```

That is the #6446 count, recomputed here as a premise, not as the new
object.

## Theorem 2 — intersection and symmetric difference

The complementary miss sets therefore each have cardinality 30. Direct
set comparison on the same 66 seeds yields

```text
|M(f00)| = 30,
|M(f01)| = 30,
|intersection| = 30,
|symmetric difference| = 0.
```

The 30 missed seeds are not listed.

## Theorem 3 — equality bit, mixed3 not adopted

Because the symmetric difference is empty, the miss sets are equal and
the displayed equality bit = 1. Inside this pair the two maps differ
only by mixed3, so mixed3 is free on the 2-site fill set. That is a
displayed comparison on this finite patch. Do not adopt mixed3.

## No-Go Discipline

The negative content is only that mixed3 does not split the 2-site fill
set inside this displayed pair. It is not a no-go against mixed3 in any
other domain.

No-Go Discipline disposition: **PASS**

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| Hamming parity as a substitute for `f_L1` | **ATTEMPTED** | Hamming `|c|_1 mod 2` is a different cube function and is not used |
| blank-block off-patch occupancy | **ATTEMPTED** | blank-block is a different rule; off-patch occupancy is the explicit `0` |
| one-site miss sets of the same pair | **ATTEMPTED** | one-site misses are a different seed class and are not the 2-site object |
| full 32-map coverage ranking | **ATTEMPTED** | ranking reports cardinalities, not whether these two miss sets coincide |
| adopt mixed3 as an Admissibility bit | **ATTEMPTED** | equality is displayed comparison data, not a selector |
| list the 30 missed seeds as the claim | **ATTEMPTED** | the new object is the equality bit, not the seed list |

### N2 — wall independence

One comparison is claimed: equality of two finite miss sets. No second
impossibility wall is used.

### N3 — hidden-wall scan

The two-cube, off-patch `0`, F_cut remaining-bit labels, and occupancy-
to-lock tick are declared. No continuum limit, no physical formation
rate, and no Admissibility rewrite is imported.

### N4 — residual matching

The residual after #6446 was whether the two cov=36 maps miss the same
seeds. This note answers that residual and does not reopen the coverage
count as a new ranking.

### N5 — certificate granularity

```text
per-element: executed — each neighbor 6-tuple is assigned its axis-type orbit
per-site: executed — each of the twelve two-cube vertices uses the same stencil
per-mode: executed — both displayed maps are scored on the same 66 seeds
per-block: executed — intersection and symmetric difference are computed on this patch
lattice-wide: not executed — no Z^3-wide formation law is claimed
```

### N6 — partial-closure paths

A larger patch, a different off-patch rule, or a different seed arity
could split the pair. Those are live routes and are outside the stated
two-cube 2-site comparison.

### N7 — steelman

The strongest objection is that equal miss sets on 2-site seeds need not
imply equal dynamics on other seeds. Correct: Theorem 3 claims only the
2-site fill-set comparison inside this pair.

### N8 — cross-cycle echo

#6446 reported `cov = 36` for each map. This note keeps that count as a
reconfirmed premise and adds only the equality of the complementary
miss sets.

## Boundaries and explicit non-claims

- The theorem is conditional on the two-cube with off-patch occupancy `0`.
- It does not list the 30 seeds.
- It does not adopt mixed3, vertex3, or any remaining bit.
- It does not claim a physical Admissibility selector.
- No axiom, primitive, registry, or audit verdict is edited.

## Verification

Run:

```bash
python3 scripts/f_cut_k4_v30_two_site_miss_equality_2026_08_15.py
```

The runner enumerates the 66 two-site seeds, recomputes both coverages,
compares miss sets by intersection and symmetric difference, and refuses
to print the missed seeds. Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
