---
claim_id: site_indexed_j_restricts_scalar_i_does_not_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-site window with a one-site subsite and two unit-A lock histories, scalar additive I on the window does not determine I on the subsite, while site-indexed J restricts by evaluation. The C1 retype of Record readout from scalar I to J is displayed only; it is not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/site_indexed_j_restricts_scalar_i_does_not_hypothetical_2026_08_13.py
---

# Site-indexed J restricts; scalar I does not

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** hypothetical C1 follow-on on one two-site window. Not pairing-on-J.
Not a second Newton-π. Not a fifth extra.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/site_indexed_j_restricts_scalar_i_does_not_hypothetical_2026_08_13.py`](../scripts/site_indexed_j_restricts_scalar_i_does_not_hypothetical_2026_08_13.py)
**Parent on origin/main:** axiom memo only,
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Current Record names a scalar additive readout `I` determined by content
alone. On the two-site window below, that scalar does not determine the
same occupancy count on a one-site subsite. The site-indexed lock field
`J` does restrict, by evaluation. A C1 retype of the named readout from
`I` to `J` would make this window restriction-stable. That retype is
displayed only. It is not adopted. No sheaf axiom is imported. No pairing
is formed. No Newton-π product table is computed. No fifth extra is named.
`r=1/2` is not forced. `L_phys` is not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact two-history occupancy and restriction arithmetic on a declared two-site window; C1 retype of Record readout remains hypothetical and not adopted."
trace_class: negative_route_pruning
target_claim_id: record_readout_restriction_stability
target_blocker_text: "a local TOE readout must be site-indexed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for I_W versus I_U non-functionality and J restriction-by-evaluation on W={x,y}, U={x}; axiom adoption remains closed"
hypothetical_axiom_status: "C1 follow-on: J restricts to subsites, scalar I does not; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Window `W={x,y}`. Subsite `U={x}`. Menu `M={A,B}`.

A history on `W` is a site-indexed lock field `J` with values in
`M union {0}`, where `0` means no record. The two unit locks of `A` are

- `h10`: `J_W=(A,0)`, so `J(x)=A` and `J(y)=0`
- `h01`: `J_W=(0,A)`, so `J(x)=0` and `J(y)=A`

Occupancy counts are exact cardinalities

`I_W(h)=|{z∈W: J(z)≠0}|`

`I_U(h)=|{z∈U: J(z)≠0}|`

Restriction of `J` is evaluation: `(J|_U)(x)=J(x)`.

C1 `J` arithmetic reconstructed here is only that pair of definitions:
`J` is the site-indexed lock field, and `I` on a region is the number of
nonzero locks in that region. Identity gates call `I_W`, `I_U`, `J_of`,
and `J_restrict`.

## Theorem 1 — Scalar I on W does not determine I on U

Identity gates call `I_W` and `I_U`. Direct evaluation gives

`I_W(h10)=I_W(h01)=1`

and

`I_U(h10)=1 ≠ 0=I_U(h01)`.

There is no function `f:ℕ→ℕ` such that `f(I_W(h))=I_U(h)` for both
histories: the pairs `(I_W,I_U)` are `(1,1)` and `(1,0)`. Scalar `I` on a
window does not determine `I` on a subsite.

The mutation predicate “`I_U` is a function of `I_W`” fails.

## Theorem 2 — Restriction of J is a function of J

Identity gates call `J_of` and `J_restrict`. Direct evaluation gives

`J_W(h10)=(A,0)` and `(J|_U)(h10)=A`

`J_W(h01)=(0,A)` and `(J|_U)(h01)=0`

So `J_W(h10)` determines `J|_U=A`, and `J_W(h01)` determines `J|_U=0`.
Restriction of `J` is evaluation at sites of `U`, hence a function of `J`.

The mutation predicate “`J|_U(h10)=J|_U(h01)`” fails.

## Theorem 3 — Current Record readout cannot restrict

Current Record, quoted from the axiom memo:

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

The named readout is a scalar additive `I` determined by content alone. A
scalar on `W` is not a local field, so the named readout cannot restrict.
A C1 retype to `J` is the cheapest change that makes Record
restriction-stable on this window. That sentence is a comparison of types
on the displayed window. It is not an axiom edit.

## Theorem 4 — Not a sheaf, not a pairing, not Newton-π, not a fifth extra

This is not a sheaf axiom and not a pairing. It does not dissolve Newton π
(the product table is still extra; this note and runner do not compute
one). It does not name a fifth extra.

## Theorem 5 — Display restriction only

Display restriction. Do not adopt C1. Do not force `r=1/2`. Do not adopt `L_phys`.
Do not adopt a Record rewrite. Do not import a sheaf axiom.

## Identity Gates And Mutation Predicates

Identity gates must call `I_W(h10)`, `I_W(h01)`, `I_U(h10)`, `I_U(h01)`,
`J_restrict(h10)`, and `J_restrict(h01)`. Theorem 1 gates also call
`I_W` and `I_U`. Theorem 2 gates also call `J_of` and `J_restrict`.

Required failures:

- predicate “`I_U` is a function of `I_W`” must fail
- predicate “`J|_U(h10)=J|_U(h01)`” must fail

## Negative Scope

The result is exact finite arithmetic on two unit-`A` histories of one
window. It does not classify all windows, does not derive a local field
from current Record, and does not promote C1. No unmerged PR is cited.
No runner cache and no citation manifest are part of this surface.

## No-Go Discipline Gate

The negative claims are restricted to restriction of `I` versus `J` on
two unit-`A` histories. The gate does not certify a sheaf axiom or a
Record rewrite.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Scalar `I_U` as a function of `I_W` | compare `(I_W,I_U)` on `h10` and `h01` | Theorem 1: pairs `(1,1)` and `(1,0)` | **ATTEMPTED** |
| Restriction of `J` as evaluation | compare `J|_U` on both histories | Theorem 2: `A` versus `0` | **ATTEMPTED** |
| Current Record as a local field | quote content-only additive `I` | Theorem 3: a scalar on `W` cannot restrict | **ATTEMPTED** |
| Sheaf axiom, pairing, Newton-π product table | enlarge the display | Theorem 4: refused; no product table computed | **ATTEMPTED** |
| Adopt C1, force `r=1/2`, adopt `L_phys` | rewrite Record | Theorem 5: refused | **ATTEMPTED** |

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `I` non-functionality / `J` restriction | no: `I_W` is constant while `I_U` splits | no: `J|_U` being a function of `J` does not restore an `f(I_W)` | independent |
| restriction type / Newton product table | no: restriction is not a pairing | no: a product table would still need a local field | independent |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| window `W={x,y}`, subsite `U={x}` | stipulated finite objects |
| unit locks of `A` | stipulated witnesses |
| `I` as cardinality of nonzero locks | reconstructed C1 count |
| `J|_U` as evaluation | reconstructed restriction |
| sheaf, pairing, product table, `r=1/2`, `L_phys` | not used |
| observations | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | content-only readout; additive scalar `I` with `I(empty)=0` | exact current wording; no restriction rule borrowed from the memo |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | two unit-`A` lock histories | no classification of every history |
| per site | restriction is evaluation at the single site of `U` | no lattice-wide locality theorem |
| per mode | occupancy `I` is a cardinality | no product table |
| per block | Record readout restriction type only | no sheaf, pairing, or Newton-π closure |
| lattice-wide | not executed | only `W={x,y}` is in scope |

The runner emits substantive `per_element`, `per_site`, `per_mode`,
`per_block`, and `lattice_wide` lines.

### N6 — live partial-closure paths

1. Keep current Record as a window scalar.
2. Owner wording could pick `J` later; restriction would then be evaluation.
3. A later derivation could produce a local field without adopting C1.

None of those paths is taken here.

### N7 — hostile steelman

> Content-only readout already includes which records are present, so
> restriction is just forgetting the records outside `U`. Scalar `I` on
> `W` plus the bag already determines `I` on `U`.

The steelman is false on the displayed pair. Both histories have
`I_W=1` and the same letter `A`. The forgotten site is the one that
carries `A` on `h01`. A window scalar cannot name that site.

### N8 — cross-cycle echo

This is a C1 follow-on locality test, not pairing-on-`J`, not a second
Newton-π, and not a fifth extra. Earlier C1 occupancy-retract notes
remain on their own surfaces and are not parents.

**Gate disposition:** PASS for (i) `I_U` is not a function of `I_W` and
(ii) `J|_U` is evaluation of `J`. FAIL / DO NOT SHIP for "adopt C1,"
"import a sheaf axiom," "put a pairing on `J`," "compute a Newton-π
product table," "force `r=1/2`," "adopt `L_phys`," or "name a fifth extra."

## Review Record

Independent audit remains required before any effective status may
change. No `review-loop` was invoked in producing this artifact.
