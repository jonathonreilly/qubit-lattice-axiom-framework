---
claim_id: two_site_seed_nn_formation_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On Z^3, with off-support occupancy 0 and the displayed unread-site combination n_μ=(o_{+μ}−o_{-μ})/3, a two-site seed {0,v} with v≠0 is mutually formation-ready (both unread-site n values nonzero) if and only if v is a 6-NN of the origin. The seed is initial-condition occupancy content, not a privileged Lattice site. No axiom is added or rewritten."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_site_seed_nn_formation_2026_08_14.py
---

# Two-Site Seeds Are Mutually Formation-Ready Iff 6-NN

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact two-point evaluation of the displayed unread-site
occupancy combination on `Z^3`. The claim is the mutual `n ≠ 0`
predicate for a two-site seed, not a multi-step occupancy evolution
and not a twelve-seed occupancy clone.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_site_seed_nn_formation_2026_08_14.py`](../scripts/two_site_seed_nn_formation_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write occupancy `o : Z^3 → {0,1}` with value `0` off the occupied
support. At an unread site the displayed combination is

```text
n_μ = (o_{+μ} − o_{-μ}) / 3.
```

A two-site seed `{0, v}` with `v ≠ 0` is *mutually formation-ready*
when both seed sites are treated as unread and

- `n(0)` computed from occupancy `{v}` is nonzero, and
- `n(v)` computed from occupancy `{0}` is nonzero.

**Theorem.** This holds if and only if `v` is a 6-NN of the origin,
i.e. `v ∈ {±e_x, ±e_y, ±e_z}`.

The seed is initial-condition content. Placing one site at the origin
is a translation coordinate choice. No site is privileged.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact unread-site occupancy arithmetic on Z^3 classifies two-site mutual n≠0 as the 6-NN condition. The combination and seed are displayed initial-condition data, not axiom content."
trace_class: frontier_discovery
target_claim_id: two_site_seed_nn_formation
target_blocker_text: "whether a two-site seed is mutually formation-ready only when the two sites are 6-NN"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed unread-site combination on Z^3; no formation rate, multi-step evolution, or physical lock rule is asserted"
hypothetical_axiom_status: "none; occupancy seed and n are displayed initial-condition data and are not proposed as axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences quoted below supply cubic sites with nearest-neighbor
  adjacency, a nearest-neighbor condition for the local distribution,
  and unreadability of a site with no record. They are quoted without
  rewrite.
- **Explicit theorem-domain condition:** occupancy is a `{0,1}`-valued
  function on `Z^3` with value `0` off the displayed support, and `n`
  is the displayed unread-site combination. Those objects are supplied
  mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** whether Record locks at a site with `n ≠ 0`,
  any formation rate, and any multi-step occupancy update remain
  separate, open obligations outside the target proved here.

The Qubit sentence is not rewritten. Occupancy is not a change of the
one-site possibility domain.

## Exact Objects

Sites are points of `Z^3`. Write `e_x = (1,0,0)`, `e_y = (0,1,0)`,
`e_z = (0,0,1)`. The 6-NN set of a site `x` is
`{x ± e_x, x ± e_y, x ± e_z}`. Occupancy of a site not in the displayed
support is `0`. All coordinates of `n` are exact elements of `Q`.

For occupancy support `S` and unread site `x`,

```text
n_μ(x; S) = (o(x + e_μ) − o(x − e_μ)) / 3,     o(y) = 1[y ∈ S].
```

The two-site seed `{0, v}` is evaluated at both unread sites against
the complementary singleton occupancy. Mutual formation-readiness is
exactly the pair of inequalities `n(0; {v}) ≠ 0` and `n(v; {0}) ≠ 0`.
It is not a site readout of either unread site.

## Exact Target And Proof Obligations

The exact target is the classification of two-site seeds that are
mutually formation-ready under the displayed combination.

The obligation graph is:

1. expand `n(0; {v})` on the six axis neighbors of the origin;
2. expand `n(v; {0})` on the six axis neighbors of `v`;
3. observe that both triples are nonzero precisely on the 6-NN set;
4. evaluate the same pair on representatives of the first
   translation-fixed proper-rotation orbits, then on the full signed
   axis-permutation orbits of those representatives;
5. confirm that translating the pair `{a, a+v}` does not change the
   mutual predicate.

All five obligations are closed below and in the runner. The displayed
combination, the unread treatment of both seed sites, and the `{0,1}`
occupancy alphabet are theorem hypotheses. Multi-step evolution,
twelve-seed occupancy clones, and any lock-or-rate rule are outside
this theorem. There is no missing lemma for the bounded algebraic
target; a physical formation rule would be a separate claim with
separate support.

## Theorem 1 — unread `n` at the origin sees only the 6-NN of `0`

With occupancy `{v}`,

```text
n_μ(0; {v}) = (1[v = e_μ] − 1[v = −e_μ]) / 3.
```

Hence `n(0; {v}) ≠ 0` if and only if `v` equals one of `±e_x, ±e_y, ±e_z`.
At `v = e_x` one has `n(0; {e_x}) = (1/3, 0, 0)`. At `v = (2,0,0)` the
`±x` neighbors of the origin are both empty, so `n(0) = (0,0,0)`. At
`v = (1,1,0)` the same holds: no axis neighbor of the origin is occupied.

## Theorem 2 — unread `n` at `v` sees only the 6-NN of `v`

With occupancy `{0}`,

```text
n_μ(v; {0}) = (1[v + e_μ = 0] − 1[v − e_μ = 0]) / 3
            = (1[v = −e_μ] − 1[v = e_μ]) / 3.
```

Hence `n(v; {0}) ≠ 0` if and only if `v` is a 6-NN of the origin. At
`v = e_x` one has `n(e_x; {0}) = (−1/3, 0, 0)`.

## Theorem 3 — mutual formation-readiness is the 6-NN condition

The two unread-site conditions of Theorems 1 and 2 are the same
predicate. Therefore `{0, v}` is mutually formation-ready if and only
if `v ∈ {±e_x, ±e_y, ±e_z}`.

The same arithmetic at a translated pair `{a, a+v}` gives

```text
n_μ(a; {a+v}) = (1[v = e_μ] − 1[v = −e_μ]) / 3,
```

so the origin placement is a coordinate choice, not a privileged site.

## Theorem 4 — translation-fixed orbit representatives

Proper cubic rotations are the determinant-`+1` signed axis
permutations. They fix the origin and permute the 6-NN set. The first
translation-fixed orbits, with one representative each, evaluate as
follows.

| `v` | orbit name | `n(0)` from `{v}` | ready? |
|---|---|---|---|
| `(1,0,0)` | 6-NN | `(1/3,0,0)` | yes |
| `(2,0,0)` | axis-2 | `(0,0,0)` | no |
| `(1,1,0)` | face diagonal | `(0,0,0)` | no |
| `(1,1,1)` | space diagonal | `(0,0,0)` | no |
| `(2,1,0)` | knight | `(0,0,0)` | no |

Every proper-rotation image of a representative has the same readiness
as that representative: only the 6-NN orbit is mutually
formation-ready. Signed axis permutation of a 6-NN remains a 6-NN.

This is two-point `n` evaluation. It is not a multi-step occupancy
evolution on twelve seeds.

## Physical-Interpretation Boundary

The proved output is the mutual `n ≠ 0` classification. This note does
not assign that predicate a physical lock, rate, or gauge label, and it
does not change the one-site Qubit statement. Occupancy and `n` are
displayed initial-condition data, not axiom content, and no additional
axiom is proposed.

## Mutation Checks

Four non-equivalences guard the load-bearing conclusions:

1. `v = (2,0,0)` is not mutually formation-ready;
2. `v = (1,1,0)` is not mutually formation-ready;
3. `n(0; {e_x})` is not the zero triple;
4. a face-diagonal site is not a 6-NN of the origin.

## What This Does Not Claim

- The displayed combination is not proposed as axiom text and is not
  selected by the four axioms.
- Mutual formation-readiness is not a Record readout of an unread site.
- No formation rate, tick, or multi-step occupancy update is derived.
- No twelve-seed occupancy clone is executed.
- Independent class-`C` leftovers are not used as parents.
- The seed sites are not privileged Lattice sites.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> No site is privileged. Sites are distinguished by the supplied lattice
> structure alone.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

> Records form.

> A site with no record cannot be read.

Their dependency role is limited to cubic nearest-neighbor vocabulary,
the neighbor-conditioned distribution clause, and unreadability. This
theorem separately supplies the occupancy alphabet and the unread-site
combination; physical lock and rate remain outside its target.

## Runner Contract

The companion runner evaluates `n` from occupancy by exact rational
arithmetic. It checks Theorems 1–4 on a finite box of `Z^3`, on the
five orbit representatives, and on their full proper-rotation orbits.
It also checks the four mutations, quotes the live axiom sentences,
prints substantive N5 scope certificates, and records the import
boundary. Declared review inputs are this note and the axiom memo only.
