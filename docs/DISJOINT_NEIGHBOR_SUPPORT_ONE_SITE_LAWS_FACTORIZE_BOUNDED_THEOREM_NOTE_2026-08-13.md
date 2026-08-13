---
claim_id: disjoint_neighbor_support_one_site_laws_factorize_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On Z^3, a pair of one-site Admissibility laws whose conditions live on the disjoint nearest-neighbor 6-tuples of 3e1 and 6e1 is a product measure on the two possibility sets; the perfectly correlated fair joint violates the independence identity and is therefore not that product, so a distant correlated assignment is not supplied by those one-site laws alone."
upstream_dependencies:
  - minimal_axioms
runner: scripts/disjoint_neighbor_support_one_site_laws_factorize_2026_08_13.py
---

# Disjoint-Neighbor-Support One-Site Laws Factorize

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact cubic nearest-neighbor listings for `3e1` and `6e1`, product
factorization of a pair of one-site laws on those disjoint 6-tuples, and the
`1/4` versus `0` independence-identity split for the perfectly correlated fair
joint; a joint on distant sites remains extra.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/disjoint_neighbor_support_one_site_laws_factorize_2026_08_13.py`](../scripts/disjoint_neighbor_support_one_site_laws_factorize_2026_08_13.py)

## Result Up Front

Admissibility is a per-site distribution. Its current sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The current Lattice sentence is likewise quoted only as a premise:

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

Five exact statements locate the split.

1. **Disjoint supports.** The six-point sets `N(3e1)` and `N(6e1)` are
   disjoint. Neither contains the origin.
2. **Product factorization.** A pair of one-site laws whose conditions live
   on those two 6-tuples is the product measure
   `P(α,β)=P_x(α|η_x) P_y(β|η_y)` on the two possibility sets. Every such
   product obeys the independence identity
   `P(α,β) P(α',β') = P(α,β') P(α',β)`.
3. **Correlated witness is not a product.** The joint
   `P(00)=P(11)=1/2`, `P(01)=P(10)=0` has fair margins and violates the
   identity: `P(00)P(11)=1/4` while `P(01)P(10)=0`. Fair margins do not imply
   a product.
4. **Path residual (scoped).** That correlated joint is therefore not
   supplied by one-site Admissibility laws at `3e1` and `6e1` alone. Possible
   escapes, none of them derived and none of them declared here, are a law
   whose condition includes sites outside `N(3e1)∪N(6e1)`, intermediate records on a connecting path, or a declared joint `L_phys`.
5. **Not a global no-go.** The result is a factorization theorem for one-site
   laws on disjoint neighbor supports. It does not rule out every distant
   correlation. It does not declare `L_phys`. It does not edit an
   axiom sentence.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The neighbor listings, the product factorization identity, and the 1/4-versus-0 correlated witness are proved by finite lattice enumeration and exact Fraction arithmetic; a joint on distant sites remains extra and is not declared."
trace_class: negative_route_pruning
target_claim_id: joint_law_l_phys
target_blocker_text: "a physical joint law on distant sites, including correlated bits"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "One-site laws on disjoint neighbor supports factorize. A joint L_phys remains extra and must not be adopted until executable. Do not adopt axiom text."
conditional_surface_status: "exact for disjoint NN 6-tuples at spacing 3 and for the product-versus-correlated 2x2 table; a joint on distant sites remains extra"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work on the cubic lattice `Z^3` with the Lattice axiom's nearest-neighbor
adjacency. Write

`e1=(1,0,0)`, `e2=(0,1,0)`, `e3=(0,0,1)`, `0=(0,0,0)`.

The neighbor set of a site `x` is the six-point set

`N(x)={x±e1, x±e2, x±e3}`.

Thus `|N(x)|=6` at every site. Graph distance is the taxicab metric

`d(x,y)=|x_1-y_1|+|x_2-y_2|+|x_3-y_3|`.

The executed sites are `x=3e1=(3,0,0)` and `y=6e1=(6,0,0)`, with system
origin `0`. Distances: `d(0,x)=3`, `d(0,y)=6`, `d(x,y)=3`.

A **one-site law** at a site `z` is a map `P_z(· | η_z)` from 6-tuples of
labels on `N(z)` to a probability distribution on a declared two-element
possibility set `{0,1}`. The executed `{0,1}` is that declared finite menu.
It is not a derivation that the Qubit one-site domain is binary.

A **product assignment** on `{x,y}` is `P_x ⊗ P_y`, the joint

`P(α,β) = P_x(α | η_x) P_y(β | η_y)`, `α,β ∈ {0,1}`.

A **correlated assignment** on `{0,1}^2` is any joint that is not a product.
The executed witness is the perfectly correlated fair law

`P_corr(00)=P_corr(11)=1/2`, `P_corr(01)=P_corr(10)=0`.

Its one-site margins are fair, `P_corr,x(0)=P_corr,y(0)=1/2`, yet
`P_corr(00) ≠ (1/2)·(1/2)`.

The fair product used as the positive control is

`P_prod(α,β)=1/4` for every `(α,β) ∈ {0,1}^2`.

Explicit neighbor lists used as witnesses:

```text
N(0)    = {(±1,0,0),(0,±1,0),(0,0,±1)}
N(2e1)  = {(1,0,0),(3,0,0),(2,±1,0),(2,0,±1)}   — shares e1 with N(0)
N(3e1)  = {(2,0,0),(4,0,0),(3,±1,0),(3,0,±1)}   — 0 ∉ N(3e1)
N(6e1)  = {(5,0,0),(7,0,0),(6,±1,0),(6,0,±1)}   — 0 ∉ N(6e1)
N(3e1) ∩ N(6e1) = empty
```

The 26-site Moore neighborhood of a site is the Chebyshev-1 punctured cube.
It is a live adjacency mutation, not the Lattice neighbor set.

## Exact Target And Obligation Graph

**Exact target.** On declared cubic nearest-neighbor objects, list `N(3e1)`
and `N(6e1)`, prove those supports are disjoint and exclude the origin, prove
that a pair of one-site laws on those 6-tuples is a product obeying the
independence identity, and exhibit the perfectly correlated fair joint as a
non-product with the same fair margins.

| Obligation | Role | Disposition |
|---|---|---|
| pin the Admissibility distribution sentence | premise | quoted; no edit |
| pin Lattice NN adjacency and `N(x)` | premise | quoted; `|N(x)|=6` listed |
| show `N(3e1) ∩ N(6e1)=empty` and origin exclusion | Theorem 1 | listing |
| show `P(α,β)=P_x(α\|η_x) P_y(β\|η_y)` and the identity | Theorem 2 | product of Fractions |
| show `P_corr(00)P_corr(11)=1/4 ≠ 0=P_corr(01)P_corr(10)` | Theorem 3 | 2x2 table |
| record that a correlated joint is not supplied by the pair alone | Theorem 4 | scoped residual |
| record that this is not a no-go against all distant correlation | Theorem 5 | scoped negative |
| declare a joint `L_phys` | non-claim | not attempted |
| claim that every distant correlation is ruled out | non-claim | not attempted |

## Theorem 1 — Disjoint Supports

**Claim.** `N(3e1) ∩ N(6e1)=empty`, `0 ∉ N(3e1)`, and `0 ∉ N(6e1)`.

**Proof.** The six neighbors of `3e1=(3,0,0)` are

`(2,0,0)`, `(4,0,0)`, `(3,1,0)`, `(3,-1,0)`, `(3,0,1)`, `(3,0,-1)`.

None is the origin. The six neighbors of `6e1=(6,0,0)` are

`(5,0,0)`, `(7,0,0)`, `(6,1,0)`, `(6,-1,0)`, `(6,0,1)`, `(6,0,-1)`.

None is the origin. The two six-point sets are disjoint by direct comparison.

A one-line metric reason is available and is not a substitute for the
listing. Distinct sites share a nearest neighbor if and only if `d≤2`,
because a shared neighbor `z` would give `d(x,y)≤d(x,z)+d(z,y)=2`. Here
`d(3e1,6e1)=3`, so a shared neighbor is impossible, matching the listing.

The spacing-2 contrast used by the identity gate is the nonempty intersection

`N(0) ∩ N(2e1)={(1,0,0)}={e1}`.

A predicate that returns disjointness at every pair of sites is therefore
false on `(0,2e1)`.

## Theorem 2 — Product Factorization

**Claim.** Let `P_x(· | η_x)` and `P_y(· | η_y)` be one-site laws whose
conditions live on `N(3e1)` and `N(6e1)` respectively. The pair defines the
product measure

`P(α,β) = P_x(α | η_x) P_y(β | η_y)`

on `{0,1}^2`. In particular the independence identity

`P(α,β) P(α',β') = P(α,β') P(α',β)`

holds for every `α,β,α',β' ∈ {0,1}`.

**Proof.** By definition a one-site law at `x` is a function of a 6-tuple
indexed by `N(x)` only, and likewise at `y`. Theorem 1 says those index sets
are disjoint, so the pair is a function of two disjoint condition tuples.
The joint assigned to the two possibility sets is the product of the two
one-site values. Expanding both sides of the identity then gives

`P_x(α) P_y(β) P_x(α') P_y(β')`

on each side, so the identity holds in `Q`.

The executed fair product has every atom equal to `1/4`. Its margins are
fair, and the identity holds as ` (1/4)·(1/4)=(1/4)·(1/4) `. Every other
pair of Bernoulli one-site laws, including biased coins, likewise yields a
product: if `P_x(1)=p` and `P_y(1)=q` then the four atoms are
`(1-p)(1-q)`, `(1-p)q`, `p(1-q)`, `pq`.

The identity is a statement about the pair of one-site maps. It is not a
statement that neighbor *values* on the two 6-tuples are themselves
independent, and it is not a statement that records form at `x` or `y`.

## Theorem 3 — Correlated Witness Is Not A Product

**Claim.** The joint `P_corr(00)=P_corr(11)=1/2`, `P_corr(01)=P_corr(10)=0`
violates the independence identity and is therefore not a product of one-site
Bernoulli laws. Fair margins do not imply a product.

**Proof.** Direct evaluation gives

`P_corr(00) P_corr(11) = (1/2)·(1/2) = 1/4`,

`P_corr(01) P_corr(10) = 0·0 = 0`.

The independence identity requires these products to be equal. They are not.
Hence `P_corr` is not a product assignment.

The same table has fair one-site margins:

`P_corr(0,*) = 1/2 + 0 = 1/2`, `P_corr(*,0) = 1/2 + 0 = 1/2`.

If those margins came from one-site laws, the product assignment would be
the fair product of Theorem 2, whose four atoms are each `1/4`. That is a
different table: `P_corr(00)=1/2 ≠ 1/4`. Fair margins therefore do not
select the product.

The witness is also not a product of *any* Bernoulli pair, fair or biased.
A product with `P(01)=0` would force `P_x(0)=0` or `P_y(1)=0`; the first
makes `P(00)=0`, the second makes `P(11)=0`; both contradict
`P(00)=P(11)=1/2`.

## Theorem 4 — Path Residual (Scoped)

**Claim.** A correlated joint on `{3e1,6e1}` is not supplied by one-site
Admissibility laws at those two sites alone.

**Proof.** Theorems 2 and 3. Every pair of one-site laws on the disjoint
6-tuples of Theorem 1 lands in the product class. The executed correlated
table is not in that class.

The following escapes are recorded as residuals. None is derived. None is declared.

1. A law whose condition includes at least one site outside `N(3e1)∪N(6e1)`.
   That object is not a pair of one-site Admissibility maps.
2. Intermediate records on a path joining `3e1` to `6e1`. Neighbor *values*
   on the two 6-tuples could then carry dependence even though the
   *conditional* pair remains a product given those values. No such path of
   records is constructed here.
3. A declared joint `L_phys` on the two sites. That would be an extra law,
   not a consequence of the two one-site maps.

The Admissibility sentence determines, for each site, a distribution from
that site's nearest-neighbor conditions. It does not, by itself, name a
joint on a distant pair, a path of intermediate records, or `L_phys`.

## Theorem 5 — Not A Global No-Go

**Claim.** Theorem 4 is a factorization theorem for one-site laws on
disjoint neighbor supports. It is not a no-go against all distant
correlation.

**Scope.** The negative is restricted to the claim that the executed
correlated table is already a pair of one-site Admissibility laws at
`3e1` and `6e1`. The note does not rule out every distant correlation.
It does not say that an axiom sentence must be edited. Do not declare `L_phys`.

In particular `L_phys` is not required as an axiom. If a later derivation
produces a joint on a distant pair from executable objects, that derivation
can be checked then. Until it is executable it remains extra.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom update is necessary;
- declare a joint `L_phys`, or treat `L_phys` as named axiom content;
- claim that every distant correlation is ruled out;
- construct intermediate records on a path, or derive record formation;
- replace nearest-neighbor adjacency by the 26-site Moore neighborhood;
- identify the executed `{0,1}` menu with the full one-site possibility
  domain `M_2(C)`;
- derive a physical compiler of fair formed bits.

The scope is the exact cubic split: disjoint 6-tuples at spacing 3, product
factorization of one-site laws on those tuples, and the `1/4` versus `0`
witness that the perfectly correlated fair joint is not that product.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Lattice NN sentence | premise | quoted; no edit |
| current Admissibility distribution sentence | premise | quoted; no edit |
| six-neighbor listings at `3e1` and `6e1` | Theorem 1 | computed here |
| product of one-site Bernoulli laws | Theorem 2 | computed here |
| perfectly correlated fair 2x2 table | Theorem 3 | computed here |
| path records, non-one-site laws, `L_phys` | residuals | extra; not declared |
| observed frequencies or fitted joints | none | not used |

The exact advance is a finite lattice-geometry theorem plus a four-atom
exact table. Independent audit is required. This note authors no audit verdict.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The current Admissibility sentence says that for each site the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions. The named residual is a physical joint on distant sites, including correlated bits. This note asks whether that joint is already a pair of one-site maps on disjoint 6-tuples, and answers no. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for disjoint-support factorization of one-site Admissibility laws, distant correlation supplied by nearest-neighbor 6-tuples, and a joint `L_phys`. Hits: the 2026-06-18 outcome-factorization note uses the same `1/4` versus `(1/2,0,0,1/2)` table to show that one-copy Born margins do not *force* factorization — the opposite implication; the 2026-07-11 G3 note likewise leaves cross-edge factorization unforced by an unraveled step-law; the Tomita/tensor-trace notes factorize a tracial state on a tensor product of one-site algebras, a different object; the token `L_phys` on that commit is a continuum path length in the valley-linear note, not a joint law. An unmerged 2026-08-13 graph-separated origin-exclusion listing treats product-law independence from the origin; it is not this factorization identity and is not a landed premise. No landed disjoint-NN one-site factorization identity appears on that commit. |
| V3 | Independently checkable? | Textbook independence of a 2x2 table does not mention nearest-neighbor 6-tuples, the sites `3e1` and `6e1`, or the Admissibility distribution sentence. The runner recomputes `N(x)` by integer shifts and the four-atom table by exact `Fraction` arithmetic. |
| V4 | More than a restatement? | Yes. The discriminating witness is `P_corr(00)P_corr(11)=1/4` against `P_corr(01)P_corr(10)=0`, together with the empty intersection `N(3e1) ∩ N(6e1)`. Neither identity is a restatement of the axiom sentence. |
| V5 | One-step relabel? | No. The claim is not a corollary of the Admissibility sentence alone. That sentence names a per-site distribution determined by nearest-neighbor conditions; it does not name the pairing of two such maps, the independence identity, or the correlated non-product. |

## No-Go Discipline Gate (Theorems 4 and 5 only)

The negative claims are restricted to: a correlated joint on `{3e1,6e1}` is
not a pair of one-site Admissibility laws on those disjoint 6-tuples; this
is not a no-go against all distant correlation; `L_phys` is extra and is
not declared. The gate does not ship a global non-existence theorem against
distant correlation.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| one-site product | take `P_x ⊗ P_y` on the disjoint 6-tuples | Theorem 2: the joint is a product and the independence identity holds, including the fair table of four `1/4` atoms | **ATTEMPTED** |
| correlated joint | take `P(00)=P(11)=1/2`, `P(01)=P(10)=0` as if it were that product | Theorem 3: `1/4 ≠ 0`; the table is not a product of one-site Bernoulli laws | **ATTEMPTED** |
| path records | let intermediate records on a path join `3e1` to `6e1` and correlate neighbor values | residual; not constructed and not declared; the *conditional* pair remains a product given the 6-tuples | **ATTEMPTED** (escape) |
| declared `L_phys` | name a joint on the distant pair as an extra law | residual; extra; not declared and not executable here | **ATTEMPTED** (escape) |
| 26-site Moore neighborhood | replace `N(x)` by the Chebyshev-1 26-set | different adjacency; `0` lies in the Moore neighborhood of the L1-distance-2 site `e1+e2`, so a blanket distance-2 origin exclusion fails | **ATTEMPTED** (mutation) |
| axiom edit | treat the residual as requiring an axiom-sentence change | Theorem 5: factorization is already the content of pairing one-site laws; an axiom edit is not required and is not performed | **ATTEMPTED** |

### N2 — wall independence

Theorems 4 and 5 close only the route that reads a correlated distant joint
off a pair of one-site Admissibility maps on disjoint supports. They do not
close a later path-of-records construction, a later executable joint, or a
content-only event-label bridge. Those walls remain independent.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `Z^3` with six-neighbor `N(x)` | declared Lattice object |
| one-site condition 6-tuple | declared domain of `η` |
| sites `3e1`, `6e1` and origin `0` | explicit hypothesis of Theorems 1--4 |
| declared menu `{0,1}` | executed possibility set; not the full `M_2(C)` domain |
| product of one-site laws | declared pairing `P_x ⊗ P_y` |
| perfectly correlated fair table | executed non-product witness |
| path of intermediate records | residual; not constructed |
| declared `L_phys` | extra; not declared |
| Moore adjacency | live mutation; not the Lattice adjacency |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Lattice NN sentence; Admissibility distribution sentence | quoted as premises only; no edit |
| one-site pairing on disjoint 6-tuples | product class and independence identity | computed here |
| perfectly correlated fair table | `1/4` versus `0` | computed here |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | named sites `0`, `2e1`, `3e1`, `6e1` and the four atoms of the 2x2 table | no classification of every map on `Z^3` |
| per site | one-site laws at `3e1` and `6e1` and their product | no composite bonded-pair theorem |
| per mode | nearest-neighbor condition 6-tuples and the independence identity, not spectral modes | no harmonic-mode exhaustion |
| per block | disjointness, product factorization, and the correlated non-product only | no dynamics, formation rate, or declared joint |
| lattice-wide | checked and not executed | no lattice-wide no-go against distant correlation |

The obstruction is per-site / declared axis pair; it is not lattice-wide.

### N6 — live partial-closure paths

1. A later construction of intermediate records on a path joining the two
   sites, making neighbor *values* dependent while the conditional pair
   remains a product.
2. A later executable joint whose condition includes sites outside
   `N(3e1)∪N(6e1)`.
3. A later executable object that one might label `L_phys`, if and when it
   is derived rather than declared. That object is not required as an axiom.
4. A different adjacency, including the 26-site Moore neighborhood, if and
   when that adjacency is the Lattice object. It is not the present object.

The quoted Admissibility sentence already names a per-site distribution
determined by nearest-neighbor conditions. Pairing two such maps on disjoint
supports is already a product. No axiom sentence is edited here.

### N7 — hostile steelman

> Any two bits may be correlated, so one can simply write down the
> perfectly correlated fair table on `{3e1,6e1}`. Factorization of one-site
> laws is then empty: the joint is already there.

**Answer.** Writing down a non-product joint is exactly declaring an object
other than a pair of one-site Admissibility maps. Theorems 2 and 3 identify
that extra object: it is not in the image of `P_x ⊗ P_y` on the disjoint
6-tuples. Theorem 4 records the residual; Theorem 5 does not convert the
residual into a global no-go or into axiom text. The discriminating fact
remains `1/4 ≠ 0` together with `N(3e1) ∩ N(6e1)=empty`.

### N8 — cross-cycle echo

The 2026-06-18 outcome-factorization note and the 2026-07-11 G3 note prune
routes that would *force* a product from one-copy Born margins or from an
unraveled step-law. The present negatives face the opposite direction: when
the maps *are* one-site Admissibility laws on disjoint neighbor supports,
the product *is* forced, and the same numerical table is then a witness
that a correlated joint is not those maps. The earlier notes are not
cancelled. They remain notes about different premises.

**Gate disposition.** PASS for the scoped factorization and the two
negatives of Theorems 4 and 5. FAIL / DO NOT SHIP for ruling out every
distant correlation or for declaring `L_phys`.

## Primary Runner

[`scripts/disjoint_neighbor_support_one_site_laws_factorize_2026_08_13.py`](../scripts/disjoint_neighbor_support_one_site_laws_factorize_2026_08_13.py)
recomputes nearest-neighbor sets, the spacing-3 disjoint-support listing,
the spacing-2 shared-neighbor contrast, the product of one-site Bernoulli
laws, and the four-atom product-versus-correlated table in exact integer
lattice geometry and `Fraction` arithmetic. Identity gates call
`neighbors(x)` and `is_product(joint)`. Replacing spacing 3 by spacing 2
must fail disjoint-support. A declared always-disjoint predicate must fail
on `(0,2e1)`. Replacing the correlated witness by the fair product must fail
the "not a product" assertion. Replacing `neighbors` by the 26-site Moore
neighborhood must fail a blanket distance-2 origin exclusion.
