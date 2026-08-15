---
claim_id: sparsest_filler_identity_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 96 cube-covariant 1-site fillers on the two-cube with off-patch o=0, the unique support-26 map is identified by its orbit bits and F_cut membership. It is not f_L1. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/sparsest_filler_identity_2026_08_15.py
---

# The Unique Support-26 1-Site Filler Is Identified And Is Not `f_L1`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact orbit census and occupancy dynamics on the supplied
twelve-vertex two-cube `{0,1,2} × {0,1} × {0,1}` with seed `(0,0,0)` and
off-patch occupancy `0`. The unique support-26 filler among the 96
cube-covariant 1-site fillers is named by its axis-type orbit bits and
by non-membership in `F_cut`. No Admissibility rewrite is asserted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/sparsest_filler_identity_2026_08_15.py`](../scripts/sparsest_filler_identity_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Among the 96 cube-covariant maps that fill the two-cube from a 1-site seed,
support size has a unique minimum `m = 26` attained by exactly `N_min = 1`
map. That map is **not** `f_L1`. It is displayed here as a named rival
member of the 96, not adopted.

Write a neighbor occupancy as `c ∈ {0,1}^6`. Each of the three axes is
empty `(0,0)`, unbalanced `(1,0)` or `(0,1)`, or both-occupied `(1,1)`.
The axis type is the triple `(n_unbalanced, n_both, n_empty)`. The ten
types are the ten orbits under the 24 proper cube rotations. The five
named remaining bits used below are

```text
wt1 = (1,0,2), opp2 = (0,1,2), adj2 = (2,0,1),
vertex3 = (3,0,0), mixed3 = (1,1,1).
```

Their complements are `wt5 = (1,2,0)`, `opp4 = (0,2,1)`, `adj4 = (2,1,0)`.
The remaining two orbits are empty `(0,0,3)` and full `(0,3,0)`.

`f_L1(c)=1` if and only if some axis is unbalanced, equivalently
`n_μ = c_{+μ} − c_{-μ}` is nonzero on at least one axis. This is **not** Hamming parity `|c|_1 mod 2`. Then `supp(f_L1) = 56`, and `f_L1` fills
with lock history `(1, 4, 8, 11, 12)`.

The unique support-26 filler `f_min` is the nonempty `n_both = 0` map:

```text
f_min(c) = 1  iff  n_both(c) = 0 and some axis is unbalanced.
```

Equivalently `f_min` fires exactly on the three orbits `wt1`, `adj2`, and
`vertex3`. Its named tuple and its value on every axis-type orbit are

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 0),
(empty, wt1, opp2, adj2, vertex3, mixed3, wt5, opp4, adj4, full)
  = (0, 1, 0, 1, 1, 0, 0, 0, 0, 0).
```

`F_cut` is the 32-element class of cube-covariant maps with
`f(empty)=f(full)=0` and `f(c)=f(1-c)` for all `c`. Complement swaps
`n_both` with `n_empty`, so `wt1` is paired with `wt5`. Because
`f_min(wt1)=1` and `f_min(wt5)=0`, f_min is not a member of `F_cut`.
By contrast `f_L1` is complement-even and sits in `F_cut`.

`N_fill = 96`. Hamming parity is a different cube-covariant map, lies in
`F_cut`, has support 32, and halts at 9 locks. It is not a filler.

Displayed, not adopted. Do not write `f_min` into Admissibility.

Not leftover-character of #6400: that census reported only `m` and `N_min`.
The present object is the identity of the unique minimizer.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact orbit-bit identification of the unique support-26 cube-covariant 1-site filler on the supplied two-cube; the map is displayed and is not f_L1."
trace_class: frontier_discovery
target_claim_id: sparsest_filler_identity
target_blocker_text: "whether the unique support-26 1-site filler is identified by orbit bits and F_cut membership"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied two-cube with off-patch occupancy 0; no Admissibility rewrite is asserted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences below supply `Z^3`, proper cubic rotations, a covariant
  nearest-neighbor rule, and the unread-site sentence. They are quoted
  without rewrite.
- **Explicit theorem-domain condition:** the two-cube
  `{0,1,2} × {0,1} × {0,1}`, the 1-site seed `(0,0,0)`, and the off-patch
  occupancy `0` default are supplied mathematical data. blank-block is a
  different rule and is not used.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection of `f_min` or `f_L1` by Record or
  Admissibility remains a separate, open obligation outside the identity
  proved here.

## Exact Objects

A configuration is a 6-tuple of occupancies on the six nearest-neighbor
directions `(±e_1, ±e_2, ±e_3)`. Cube covariance means constancy on the
orbits of the 24 proper cube rotations. Restricting to `f(empty)=0` leaves
512 maps. Support is

```text
supp(f) = |{ c ∈ {0,1}^6 : f(c)=1 }|.
```

The two-cube has twelve vertices. Off-patch occupancy is the explicit `0`
default: a neighbor not in the two-cube contributes `0` to the 6-tuple.
The seed locks `(0,0,0)`. Each tick, every unlocked on-patch site evaluates
`f` on its current 6-tuple and locks if `f=1`. Halt is a fixed point of
that step. A map fills when the halt lock-set has size 12.

`f_L1(c)=1` if and only if some axis is unbalanced. This is **not** Hamming parity.

## Exact Target And Proof Obligations

The exact target is to reconfirm the 96-filler census, compute the unique
minimum support, and identify that minimizer by orbit bits and `F_cut`
membership.

The obligation graph is:

1. the 24 proper rotations partition `{0,1}^6` into the ten axis-type orbits;
2. the 512 maps with `f(empty)=0` are enumerated by free bits on the other
   nine orbits;
3. occupancy dynamics on the two-cube classifies exactly 96 fillers;
4. support sizes on that set have unique minimum 26, not attained by `f_L1`;
5. the unique minimizer equals the nonempty `n_both=0` map, with named tuple
   `(1, 0, 1, 1, 0)`, and fails complement-even, hence is not in `F_cut`.

All five obligations are closed below and in the runner. The two-cube, the
`o=0` default, and cube covariance are theorem hypotheses. Other patches,
blank-block, and any Admissibility rewrite are outside this theorem.

## Theorem 1 — unique minimum support among the 96 is 26 and is not `f_L1`

`N_fill = 96`. `f_L1` is one of those 96 maps and fills with lock history
`(1, 4, 8, 11, 12)`. Direct cell count gives `supp(f_L1) = 56`: the eight
configurations with `n_unbalanced=0` are silent, and `64-8=56`.

On the 96 fillers the support sizes have minimum `m = 26`, attained by
`N_min = 1` map. That unique minimizer is not `f_L1`, because
`56 ≠ 26`.

## Theorem 2 — orbit bits of `f_min` and non-membership in `F_cut`

Let `f_min` be that unique support-26 filler. Evaluating it on a
representative of each axis-type orbit gives

```text
f_min(empty)=0, f_min(wt1)=1, f_min(opp2)=0, f_min(adj2)=1,
f_min(vertex3)=1, f_min(mixed3)=0, f_min(wt5)=0, f_min(opp4)=0,
f_min(adj4)=0, f_min(full)=0.
```

The named five-bit tuple is therefore `(1, 0, 1, 1, 0)`. The same
assignment is the closed form `n_both=0` and not empty: those three
orbits have sizes `6+12+8=26`. `f_min` also fills, with the same lock
history `(1, 4, 8, 11, 12)`.

`F_cut` requires `f(empty)=f(full)=0` and `f(c)=f(1-c)` for every `c`.
The second condition forces `f(wt1)=f(wt5)`. `f_min` violates that
equality, so `f_min` is not a member of `F_cut`. `f_L1` satisfies it.

## Theorem 3 — displayed rival member, not adopted

`f_min` is displayed as a named rival member of the 96 cube-covariant
1-site fillers: the unique support-26 map with orbit bits
`(1, 0, 1, 1, 0)` on `(wt1, opp2, adj2, vertex3, mixed3)` and with
`f_min ∉ F_cut`. It is not `f_L1`. Displayed, not adopted. Do not write
`f_min` into Admissibility. No axiom or approved primitive is added.

## Physical-Interpretation Boundary

The proved output is the identity of one occupancy predicate on one
supplied finite patch. This note neither assigns that predicate a physical
label nor changes the Admissibility sentence. `f_min` is displayed
two-cube occupancy data, not axiom content, and no additional
axiom is proposed.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. `f_min` is not `f_L1`: their named tuples differ in the `mixed3` bit,
   and their supports are 26 and 56;
2. `f_min` is not Hamming parity: Hamming has support 32, lies in `F_cut`,
   and halts at 9 locks;
3. `f_min` is not in `F_cut`: `f_min(wt1) ≠ f_min(wt5)`.

## No-Go Discipline

The negative result is only that sparsity among the 96 does not select
`f_L1`, together with the positive identity of the actual minimizer. It
is not a universal no-go against a later derived selection rule.

No-Go Discipline disposition: **PASS**

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| identify the unique support-26 filler with `f_L1` | **ATTEMPTED** | `supp(f_L1)=56`; the minimizer has mixed3=0 |
| identify the unique support-26 filler with Hamming parity | **ATTEMPTED** | Hamming has support 32 and does not fill |
| treat sparsity as an Admissibility rewrite | **ATTEMPTED** | the map is displayed occupancy data, not axiom content |
| restrict uniqueness to the 32-element class `F_cut` | **ATTEMPTED** | the unique minimizer among the 96 is not in `F_cut` |
| treat leftover-character of #6400 as identification | **ATTEMPTED** | that census reported only `m` and `N_min` |
| replace off-patch occupancy `0` by blank-block | **ATTEMPTED** | blank-block is a different rule and empties the first wave |

### N2 — wall independence

One type of result is claimed: identity of the unique support-26 filler
among the 96. Non-membership in `F_cut` is a derived bit of that same
map, not a second impossibility wall.

### N3 — hidden-wall scan

The two-cube, the 24 rotations, the `o=0` default, and the fill halt are
all declared. No full-lattice formation law, blank-block, Hamming
substitution, or Admissibility rewrite is imported.

### N4 — residual matching

The residual after this identity is selection: nothing here derives that
Admissibility or Record must use `f_min` or `f_L1`. The residual is not
enlarged by naming the minimizer.

### N5 — certificate granularity

```text
per-element: executed — each of the 64 neighbor 6-tuples is assigned its axis-type orbit
per-site: executed — each of the twelve two-cube vertices uses the same six-direction stencil
per-mode: executed — every cube-covariant f(empty)=0 map is classified as filler or not
per-block: executed — the unique support-26 filler is named by orbit bits and F_cut membership
lattice-wide: not executed — no Z^3-wide formation law or Admissibility rewrite is claimed
```

### N6 — partial-closure paths

A later derived selection among the 96, or a separately supported reason
to impose `F_cut` before minimizing support, remains live. Either route
can proceed without rewriting the axioms.

### N7 — steelman

The strongest objection is that a different covariance group, a different
off-patch rule, or a different seed could change the minimizer. Correct:
those are different theorem domains. On the declared two-cube with
off-patch occupancy `0` and proper cube rotations, the unique support-26
filler is the map identified here.

### N8 — cross-cycle echo

#6400 reported `m` and `N_min` without naming the minimizer. This note
agrees with that count and contributes only the orbit-bit identity and
the `F_cut` membership bit.

## What This Does Not Claim

- The two-cube is not claimed to be a physically derived finite world.
- `f_min` is not assigned a gauge, particle, or other physical label.
- No claim is made that Record locks `f_min` or that Admissibility
  selects it.
- Other seeds, other patches, and blank-block are not classified.
- Independent class leftovers are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Their dependency role is limited to the repository's lattice, covariance,
and lock vocabulary. This theorem separately supplies the two-cube and the
occupancy predicates; physical selection of `f_min` remains outside its
target.

## Runner Contract

The companion runner reconstructs the 24 rotations and ten orbits,
enumerates the 512 maps with `f(empty)=0`, runs occupancy dynamics on
the two-cube, computes support sizes, and identifies the unique
support-26 filler by orbit bits and `F_cut` membership. It also checks
the three mutations, quotes the live axiom sentences, prints substantive
N5 scope certificates, and records the import boundary. Declared review
inputs are this note and the axiom memo only.
