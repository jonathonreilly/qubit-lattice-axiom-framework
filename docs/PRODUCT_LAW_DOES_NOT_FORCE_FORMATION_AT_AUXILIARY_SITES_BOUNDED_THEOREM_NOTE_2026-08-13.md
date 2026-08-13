---
claim_id: product_law_does_not_force_formation_at_auxiliary_sites_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On Z^3, the sites 3e1 and 6e1 have disjoint nearest-neighbor 6-tuples, so a product of one-site laws on {0,1} is the same function of those 6-tuples whether or not records occupy the two sites; the histories H_form and H_empty share that product law and differ only in occupancy; a bit compiler that needs records at those sites requires H_form, but the axioms do not select H_form over H_empty."
upstream_dependencies:
  - minimal_axioms
runner: scripts/product_law_does_not_force_formation_at_auxiliary_sites_2026_08_13.py
---

# Product Law Does Not Force Formation At Auxiliary Sites

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact cubic nearest-neighbor listings for `3e1` and `6e1`; product
of one-site laws as a function of those disjoint 6-tuples; occupancy-tagged
histories `H_form` and `H_empty` sharing the same content law; a bit compiler
that needs records at those sites is not selected by the axioms.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/product_law_does_not_force_formation_at_auxiliary_sites_2026_08_13.py`](../scripts/product_law_does_not_force_formation_at_auxiliary_sites_2026_08_13.py)

## Result Up Front

A product of one-site Admissibility laws is a content law. Occupancy is a
separate mark: whether a record is present at a named site. The two objects
are not the same.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The current Lattice sentence is likewise quoted only as a premise:

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The Admissibility reading note is quoted only as a premise. The distribution
concerns which possibility a forming record locks, conditional on formation at
that site; it does not supply the formation site, probability, or rate.

The current Record lock sentence is quoted only as a premise:

When present, a record locks exactly one admissible local possibility.

Five exact statements locate the split.

1. **Disjoint supports.** The six-point sets `N(3e1)` and `N(6e1)` are
   disjoint. Neither contains the origin. Neither site lies in its own
   neighbor set.
2. **Content law is not occurrence.** The product `P_x ⊗ P_y` is a function
   of the two 6-tuples on `N(x)` and `N(y)`. Occupancy of `x` is not a
   coordinate of either 6-tuple, and likewise for `y`. The product is the
   same function of those 6-tuples whether `o(x)` is formed or unformed.
3. **Two histories share the law.** The history `H_form` occupies both sites.
   The history `H_empty` occupies neither. They carry the same product law
   and differ only in occupancy. Both are compatible with the quoted
   Admissibility reading (the distribution is conditional on formation) and
   with the quoted Record lock sentence (“when present”).
4. **Compiler demand is not an axiom selector.** A bit compiler that needs
   records at those two sites requires `H_form`. The quoted axiom sentences
   do not select `H_form` over `H_empty`.
5. **Scoped negatives.** The note does not claim that no compiler exists.
   It does not edit an axiom sentence to name a formation site. A
   formation-site selector remains extra.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The neighbor listings, the occupancy-independence of the product as a function of the two 6-tuples, and the H_form versus H_empty split are proved by finite lattice enumeration and exact Fraction arithmetic; a formation-site selector remains extra."
trace_class: negative_route_pruning
target_claim_id: formation_at_auxiliary_compiler_sites
target_blocker_text: "derive record formation at graph-separated auxiliary sites from a product of one-site laws"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "A bit compiler that needs records at those sites still requires a formation rule; the product law does not select H_form over H_empty. Do not adopt axiom text."
conditional_surface_status: "exact for disjoint NN 6-tuples at spacing 3 and for the shared-law occupancy pair H_form, H_empty; formation-site selection remains extra"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work on the cubic lattice `Z^3` with the Lattice axiom's nearest-neighbor
adjacency. Write

`e1=(1,0,0)`, `e2=(0,1,0)`, `e3=(0,0,1)`, `0=(0,0,0)`.

The neighbor set of a site `z` is the six-point set

`N(z)={z±e1, z±e2, z±e3}`.

Thus `|N(z)|=6` at every site, and `z ∉ N(z)`. Graph distance is the taxicab
metric

`d(a,b)=|a_1-b_1|+|a_2-b_2|+|a_3-b_3|`.

The executed sites are `x=3e1=(3,0,0)` and `y=6e1=(6,0,0)`. Distances:
`d(0,x)=3`, `d(0,y)=6`, `d(x,y)=3`.

A **one-site law** at a site `z` is a map `P_z(· | η_z)` from 6-tuples of
labels on `N(z)` to a probability distribution on a declared two-element
possibility set `{0,1}`. The executed `{0,1}` is that declared finite menu.
It is not a derivation that the Qubit one-site domain is binary. Executed
margins are `p=1/2` and, as a non-fair control, `p=1/3`. Fairness is not
derived.

A **product law** on `{x,y}` is `P_x ⊗ P_y`, the joint

`P(α,β) = P_x(α | η_x) P_y(β | η_y)`, `α,β ∈ {0,1}`.

**Occupancy** at a site is a two-valued mark `o(z) ∈ {formed, unformed}`.
It is not a coordinate of `η_z`. A forming record at `z` would lock a value
in `{0,1}`; an unformed site carries no lock.

A **history** is a pair `(law, occupancy)`. The two executed histories are

- `H_form = (P_x ⊗ P_y, o(x)=formed, o(y)=formed)`,
- `H_empty = (P_x ⊗ P_y, o(x)=unformed, o(y)=unformed)`.

`H_empty` is emptiness of the two named auxiliary sites. It is not a claim
that the whole lattice is empty. The Record occurrence sentence “Records
form.” may be realized at other sites.

Explicit neighbor lists used as witnesses:

```text
N(0)    = {(±1,0,0),(0,±1,0),(0,0,±1)}
N(2e1)  = {(1,0,0),(3,0,0),(2,±1,0),(2,0,±1)}   — shares e1 with N(0)
N(3e1)  = {(2,0,0),(4,0,0),(3,±1,0),(3,0,±1)}   — 0 ∉ N(3e1), 3e1 ∉ N(3e1)
N(6e1)  = {(5,0,0),(7,0,0),(6,±1,0),(6,0,±1)}   — 0 ∉ N(6e1), 6e1 ∉ N(6e1)
N(3e1) ∩ N(6e1) = empty
```

## Exact Target And Obligation Graph

**Exact target.** On declared cubic nearest-neighbor objects, list `N(3e1)`
and `N(6e1)`, prove those supports are disjoint, prove that the product of
one-site laws is the same function of the two 6-tuples whether or not the
two sites are occupied, exhibit `H_form` and `H_empty` as distinct
occupancies of one product law, and record that a bit compiler needing
records at those sites is not selected by the quoted axiom sentences.

| Obligation | Role | Disposition |
|---|---|---|
| pin the Admissibility distribution sentence | premise | quoted; no edit |
| pin the formation-site/rate reading note | premise | quoted; no edit |
| pin Record “when present” | premise | quoted; no edit |
| pin Lattice NN adjacency and `N(z)` | premise | quoted; `|N(z)|=6` listed |
| show `N(3e1) ∩ N(6e1)=empty` and self-exclusion | Theorem 1 | listing |
| show the product is the same function of the two 6-tuples at either occupancy | Theorem 2 | product of Fractions |
| exhibit `H_form` and `H_empty` sharing the law | Theorem 3 | occupancy pair |
| record that a compiler needing those records requires `H_form` | Theorem 4 | scoped residual |
| record that no-compiler and axiom-edit claims are out of scope | Theorem 5 | scoped negative |
| claim that no compiler exists | non-claim | not attempted |
| edit an axiom sentence to name a formation site | non-claim | not attempted |

## Theorem 1 — Disjoint Supports

**Claim.** `N(3e1) ∩ N(6e1)=empty`. Also `0 ∉ N(3e1)`, `0 ∉ N(6e1)`,
`3e1 ∉ N(3e1)`, and `6e1 ∉ N(6e1)`.

**Proof.** The six neighbors of `3e1=(3,0,0)` are

`(2,0,0)`, `(4,0,0)`, `(3,1,0)`, `(3,-1,0)`, `(3,0,1)`, `(3,0,-1)`.

None is the origin. None is `(3,0,0)`. The six neighbors of `6e1=(6,0,0)`
are

`(5,0,0)`, `(7,0,0)`, `(6,1,0)`, `(6,-1,0)`, `(6,0,1)`, `(6,0,-1)`.

None is the origin. None is `(6,0,0)`. The two six-point sets are disjoint
by direct comparison.

A one-line metric reason is available and is not a substitute for the
listing. Distinct sites share a nearest neighbor if and only if `d≤2`,
because a shared neighbor `z` would give `d(x,y)≤d(x,z)+d(z,y)=2`. Here
`d(3e1,6e1)=3`, so a shared neighbor is impossible, matching the listing.

The spacing-2 contrast used by the identity gate is the nonempty intersection

`N(0) ∩ N(2e1)={(1,0,0)}={e1}`.

A predicate that returns disjointness at every pair of sites is therefore
false on `(0,2e1)`.

## Theorem 2 — Content Law Is Not Occurrence

**Claim.** The product `P_x ⊗ P_y` is the same function of the two 6-tuples
`η_x` on `N(x)` and `η_y` on `N(y)` whether `o(x)` is formed or unformed,
and whether `o(y)` is formed or unformed. Content law is not occurrence.

**Proof.** By definition a one-site law at `x` is a function of a 6-tuple
indexed by `N(x)` only. Theorem 1 gives `x ∉ N(x)` and `y ∉ N(y)`, and
`N(x) ∩ N(y)=empty`. Therefore

- occupancy of `x` is not a coordinate of `η_x` and not a coordinate of
  `η_y`,
- occupancy of `y` is not a coordinate of `η_x` and not a coordinate of
  `η_y`.

Two global configurations that differ only in `o(x)` or `o(y)` induce the
same pair of 6-tuples. The product

`P(α,β) = P_x(α | η_x) P_y(β | η_y)`

is therefore the same function of those 6-tuples.

The executed fair product has every atom equal to `1/4`. The executed
non-fair control with both margins `1/3` has `P(00)=1/9`. Both tables are
functions of the 6-tuples alone. Neither table names `o(x)` or `o(y)`.
Fairness is not derived: `1/9 ≠ 1/4`.

The Admissibility sentence determines, for each site, a distribution from
that site's nearest-neighbor conditions. Occupancy of the site itself is
not among those conditions.

## Theorem 3 — Two Histories Share The Product Law

**Claim.** The histories `H_form` (both sites formed) and `H_empty` (neither
site formed) share the same product law and differ in occupancy. Both are
compatible with Admissibility, whose distribution is conditional on
formation, and with Record’s “when present” lock sentence.

**Proof.** By definition both histories carry the same pair `(P_x, P_y)` and
therefore the same product `P_x ⊗ P_y`. Theorem 2 says that product does
not depend on `o(x)` or `o(y)`. The occupancy maps differ:

| History | `o(x)` | `o(y)` | product law |
|---|---|---|---|
| `H_form` | formed | formed | `P_x ⊗ P_y` |
| `H_empty` | unformed | unformed | `P_x ⊗ P_y` |

Compatibility with Admissibility is the quoted reading note: the
distribution concerns which possibility a forming record locks, conditional
on formation at that site; it does not supply the formation site,
probability, or rate. On `H_form` the product is the content law of the two
forming records. On `H_empty` there is no forming record at `x` or at `y`,
so the same content law is not asked to lock a value at those sites.

Compatibility with Record is the quoted lock sentence. When present, a
record locks exactly one admissible local possibility. On `H_form` each of
`x` and `y` is present and locks one value in `{0,1}`. On `H_empty` neither
record is present at those sites, so the lock sentence does not apply there.
The sentence is a constraint on present records, not a selector that makes
them present.

`H_empty` does not contradict “Records form.” That sentence is a global
occurrence mark. It may be realized at sites other than `{x,y}`. Emptiness
of the two auxiliary sites is not emptiness of the lattice.

## Theorem 4 — A Compiler Needing Those Records Requires `H_form`

**Claim.** A bit compiler that needs records at `x` and `y` requires
`H_form`. The quoted axiom sentences do not select `H_form` over `H_empty`.

**Proof.** A bit compiler that reads locked possibilities at `x` and at `y`
needs those records to be present. That is the occupancy of `H_form`.
Theorem 3 supplies a second history `H_empty` with the same product law and
the opposite occupancy at those sites. The Admissibility distribution
sentence names a content law from nearest-neighbor conditions. The reading
note says that distribution does not supply the formation site, probability,
or rate. The Record lock sentence applies when a record is present. None of
those sentences selects the occupancy of `H_form` over the occupancy of
`H_empty`.

The residual is therefore a formation-site selector at the two named sites.
It is not supplied by the product law.

A predicate that reads “the history carries a product law, therefore both
sites are formed” fails on `H_empty`: that history carries the product and
has both sites unformed.

## Theorem 5 — Scoped Negatives

**Claim.** Theorem 4 is a selection residual for occupancy at two named
sites. It is not a claim that no compiler exists. It is not an invitation
to edit an axiom sentence.

**Scope.** The negatives are restricted to *forcing* occupancy of `{3e1,6e1}`
from a product of one-site laws. They do not say that no bit compiler can
ever be constructed. They do not say that records never form. They do not
edit the four axiom sentences. A formation-site selector remains extra
until it is derived from executable objects.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom-sentence change is
  necessary;
- claim that no compiler exists;
- claim that records never form, or that `H_empty` is a completed empty
  universe;
- derive a fair binary margin (the `1/3` control is displayed exactly so
  that fairness is not smuggled in);
- replace nearest-neighbor adjacency by the 26-site Moore neighborhood;
- identify the executed `{0,1}` menu with the full one-site possibility
  domain `M_2(C)`;
- construct a physical menu compiler of registered event partitions.

The scope is the exact cubic split: disjoint 6-tuples at spacing 3, a
product that is a function of those 6-tuples alone, and two occupancies of
that product.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Lattice NN sentence | premise | quoted; no edit |
| current Admissibility distribution sentence | premise | quoted; no edit |
| Admissibility reading note on formation site/rate | premise | quoted; no edit |
| Record “when present” lock sentence | premise | quoted; no edit |
| six-neighbor listings at `3e1` and `6e1` | Theorem 1 | computed here |
| product of one-site Bernoulli laws | Theorem 2 | computed here |
| occupancy pair `H_form`, `H_empty` | Theorems 3--4 | computed here |
| formation-site selector at `{x,y}` | residual | extra; not derived |
| observed frequencies or fitted occupancies | none | not used |

The exact advance is a finite lattice-geometry theorem plus an occupancy
tag on one product. Independent audit is required. This note authors no audit verdict.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The current Admissibility reading note states that the distribution is conditional on formation and does not supply the formation site, probability, or rate. The named residual is a bit compiler that needs records at two graph-separated auxiliary sites. This note asks whether the product of the one-site laws already selects those records to form, and answers no. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for a product of one-site laws forcing occupancy at auxiliary sites, for histories `H_form`/`H_empty`, and for formation at `3e1` and `6e1`. Hits: the 2026-06-06 record-formation no-go is a general process/rule residual from the axiom baseline, not a spacing-3 occupancy pair; the 2026-07-04 AC-phi occupancy append is a different object; the 2026-08-10 type-separation note leaves physical construction of registered partitions open and does not tag occupancy of a product law. No landed `H_form`/`H_empty` split for a product of one-site laws on `N(3e1)` and `N(6e1)` appears on that commit. Unmerged neighbor-listing drafts are not premises. |
| V3 | Independently checkable? | Textbook product measures do not mention nearest-neighbor 6-tuples, occupancy marks, or the Record “when present” sentence. The runner recomputes `N(x)` by integer shifts and the two histories by exact `Fraction` arithmetic. |
| V4 | More than a restatement? | Yes. The discriminating witness is that `H_empty` carries the same product as `H_form` while both sites are unformed, together with the empty intersection `N(3e1) ∩ N(6e1)` and the self-exclusions `x ∉ N(x)`, `y ∉ N(y)`. Those identities are not restatements of the axiom sentence. |
| V5 | One-step relabel? | No. The claim is not a corollary of the Admissibility sentence alone. That sentence names a per-site distribution determined by nearest-neighbor conditions; it does not name occupancy of the site, the pairing of two such maps, or the compiler demand for `H_form`. |

## No-Go Discipline Gate (Theorems 4 and 5 only)

The negative claims are restricted to: a product of one-site laws on the
disjoint 6-tuples of `{3e1,6e1}` does not select occupancy of those sites;
a bit compiler that needs those records therefore still needs a
formation-site selector; this is not a claim that no compiler exists. The
gate does not ship a global non-existence theorem against compilers.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| product forces occupancy | treat `P_x ⊗ P_y` as already selecting `o(x)=o(y)=formed` | Theorems 2--3: `H_empty` carries the same product with both sites unformed | **ATTEMPTED** |
| Admissibility distribution forces the site | read the NN-determined law as a formation-site rule | reading note: the distribution is conditional on formation and does not supply the formation site, probability, or rate | **ATTEMPTED** |
| “Records form.” forces `{x,y}` | treat global occurrence as occupancy of the two auxiliary sites | Theorem 3: occurrence may be realized at other sites; `H_empty` empties only `{x,y}` | **ATTEMPTED** |
| “when present” forces presence | treat the lock sentence as a selector that makes the record present | the lock sentence constrains a present record; it does not create one | **ATTEMPTED** |
| compiler demand | a bit compiler needs records at `{x,y}`, therefore the axioms do | Theorem 4: the compiler requires `H_form`; the axioms do not select it | **ATTEMPTED** |
| axiom-sentence edit | add a formation-site sentence to close the residual | Theorem 5: the residual is extra; no axiom sentence is edited | **ATTEMPTED** |
| 26-site Moore neighborhood | replace `N(z)` by the Chebyshev-1 26-set | different adjacency; not the Lattice neighbor set used by Theorem 1 | **ATTEMPTED** (mutation) |

### N2 — wall independence

Theorems 4 and 5 close only the route that reads occupancy of `{3e1,6e1}`
off a product of one-site Admissibility maps. They do not close a later
formation-site derivation, a later executable compiler, or a fair-margin
selector. Those walls remain independent.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `Z^3` with six-neighbor `N(z)` | declared Lattice object |
| one-site condition 6-tuple | declared domain of `η` |
| sites `3e1`, `6e1` | explicit hypothesis of Theorems 1--4 |
| declared menu `{0,1}` | executed possibility set; not the full `M_2(C)` domain |
| product of one-site laws | declared pairing `P_x ⊗ P_y` |
| occupancy mark `formed`/`unformed` | declared second coordinate of a history |
| histories `H_form`, `H_empty` | executed occupancy pair of one product |
| bit compiler needing those records | residual demand; not constructed |
| formation-site selector | extra; not derived |
| Moore adjacency | live mutation; not the Lattice adjacency |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Lattice NN sentence; Admissibility distribution sentence; formation-site/rate reading note; Record “when present” | quoted as premises only; no edit |
| one-site pairing on disjoint 6-tuples | product as a function of those 6-tuples | computed here |
| occupancy pair `H_form`, `H_empty` | shared law, distinct occupancy | computed here |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | named sites `0`, `2e1`, `3e1`, `6e1` and the four atoms of the product table | no classification of every map on `Z^3` |
| per site | one-site laws at `3e1` and `6e1`, and occupancy marks at those two sites | no composite bonded-pair theorem |
| per mode | nearest-neighbor condition 6-tuples and occupancy tags, not spectral modes | no harmonic-mode exhaustion |
| per block | disjointness, occupancy-independence of the product, and the `H_form`/`H_empty` split only | no dynamics, formation rate, or compiler construction |
| lattice-wide | checked and not executed | no lattice-wide no-go against compilers |

The obstruction is per-site / declared axis pair; it is not lattice-wide.

### N6 — live partial-closure paths

1. A later derivation that records form at the two named sites.
2. A later executable bit compiler that constructs `H_form` from objects
   already in the axioms, rather than reading it off the product law.
3. A later selector for a fair binary margin, independent of occupancy.
4. A different adjacency, including the 26-site Moore neighborhood, if and
   when that adjacency is the Lattice object. It is not the present object.

The quoted Admissibility sentence already names a per-site distribution
determined by nearest-neighbor conditions. Pairing two such maps on disjoint
supports is already a product. Occupancy of the two sites is a different
coordinate. No axiom sentence is edited here. A later derivation is not
forbidden.

### N7 — hostile steelman

> The product law is a law of records at `x` and `y`. If the law is present,
> the records are present. Therefore `H_empty` is not a history of that law,
> and the compiler is already selected.

**Answer.** That identification is exactly the predicate “product law
implies both sites formed.” Theorem 2 separates the product, a function of
the two neighbor 6-tuples, from occupancy of `x` and `y`. Theorem 3 exhibits
`H_empty` as a history that carries the product and leaves both sites
unformed. The Admissibility reading note already types the distribution as
conditional on formation. The discriminating fact remains that `H_form` and
`H_empty` share one product and differ in occupancy.

### N8 — cross-cycle echo

The 2026-06-06 record-formation no-go and the 2026-07-04 formation-append
notes prune routes that would force a formation *rule, site, or rate* from
the axiom baseline. The 2026-08-10 type-separation note leaves a physical
construction of registered partitions open. The present negatives face a
narrower residual: even after a product of one-site laws is written on two
graph-separated sites, occupancy of those sites is still not selected. The
earlier notes are not cancelled. They remain notes about different
premises.

**Gate disposition.** PASS for the scoped occupancy split and the two
negatives of Theorems 4 and 5. FAIL / DO NOT SHIP for “no compiler exists”
or for editing an axiom sentence to name a formation site.

## Primary Runner

[`scripts/product_law_does_not_force_formation_at_auxiliary_sites_2026_08_13.py`](../scripts/product_law_does_not_force_formation_at_auxiliary_sites_2026_08_13.py)
recomputes nearest-neighbor sets, the spacing-3 disjoint-support listing,
the self-exclusions `x ∉ N(x)` and `y ∉ N(y)`, the product of one-site
Bernoulli laws as a function of the two 6-tuples, and the occupancy pair
`H_form`, `H_empty` in exact integer lattice geometry and `Fraction`
arithmetic. Identity gates call `neighbors(x)` and `product_law`. A
predicate “product law implies both sites formed” must fail on `H_empty`.
Replacing spacing 3 by spacing 2 must fail disjoint-support.
