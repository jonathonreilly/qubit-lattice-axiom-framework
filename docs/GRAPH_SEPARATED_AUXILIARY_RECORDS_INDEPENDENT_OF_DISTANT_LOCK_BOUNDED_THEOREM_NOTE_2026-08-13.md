---
claim_id: graph_separated_auxiliary_records_independent_of_distant_lock_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On Z^3 with nearest-neighbor adjacency, a one-site Admissibility law at graph distance at least 2 from the origin has a condition 6-tuple that excludes the origin; spacing 3 sites have pairwise-disjoint neighbor supports, so their product law is not a function of the origin possibility; adjacent placement does not force independence, and neither uniformity nor record formation is derived."
upstream_dependencies:
  - minimal_axioms
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
runner: scripts/graph_separated_auxiliary_records_independent_of_distant_lock_2026_08_13.py
---

# Graph-Separated Auxiliary Records Independent Of A Distant Lock

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact cubic nearest-neighbor inclusion, exclusion, and spacing-3
disjoint neighbor supports for one-site Admissibility condition tuples;
formation and a fair binary margin remain open.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/graph_separated_auxiliary_records_independent_of_distant_lock_2026_08_13.py`](../scripts/graph_separated_auxiliary_records_independent_of_distant_lock_2026_08_13.py)

## Result Up Front

The August 10 type-separation note
[`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md)
leaves open a physical construction that produces registered measurable event partitions. A finite register of bits
independent of a system possibility would be one such construction. This note
does not install that compiler. It proves an exact cubic-lattice split for
one-site Admissibility condition tuples.

The current Lattice sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The current Admissibility sentence is likewise quoted only as a premise:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The current Record sentences are quoted only to type a binary readout of a
locked auxiliary possibility as a bit. Formation is not derived:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.

Five exact statements locate the split.

1. **Adjacent inclusion.** `0 ∈ N(e1)`. Any one-site law at `e1` has the
   possibility at the origin as a coordinate of its condition 6-tuple.
   Independence of that law from the origin possibility is not a theorem of
   Admissibility: the axiom permits laws that depend on that coordinate.
2. **Distance ≥ 2 exclusion.** `0 ∉ N(2e1)` and `0 ∉ N(3e1)`. A one-site law
   at those sites is a function of a 6-tuple that does not include the origin.
   It is not a function of the origin possibility.
3. **Spacing 3 disjoint neighbor supports.** For `k=1,2,3` the sites
   `x_k=3k e1` satisfy `0 ∉ N(x_k)`, `N(x_j) ∩ N(x_k)=empty` for `j≠k`, and
   `N(0) ∩ N(x_k)=empty`. Spacing 2 is not disjoint-support:
   `N(0) ∩ N(2e1)={e1}`.
4. **Product law independent of the origin.** The product of the three
   one-site laws on `{x_1,x_2,x_3}` has conditions only on `⋃_k N(x_k)`,
   which does not contain `0`. The product is therefore not a function of the
   origin possibility. This is a conditional independence compiler of those
   auxiliary sites from a distant lock, conditional on the one-site laws and
   on records forming there.
5. **Scoped negatives.** Adjacent placement does not force independence.
   Graph separation does not force uniform binary margins: any product of
   one-site laws is allowed, including biased coins. Graph separation does
   not force records to form at the auxiliary sites. The note is not a physical menu compiler.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The six-neighbor inclusion and exclusion identities, the spacing-3 disjoint-support listing, and the product-law condition-domain claim are proved by finite lattice enumeration; formation and a fair binary margin remain open."
trace_class: direct_blocker_closure
target_claim_id: admissibility_distribution_to_effect_grade_bridge
target_blocker_text: "derive distribution-to-effect-grade identification/functionality and universal binary-and-ternary physical menu eligibility"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "A physical compiler still needs record formation at the separated sites and a fair binary margin; do not adopt axiom text."
conditional_surface_status: "exact for cubic NN inclusion/exclusion and spacing-3 disjoint supports; formation and uniformity open"
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

A **one-site law** at `x` is any map `P_x(· | η)` whose condition `η` is a
6-tuple of possibilities on `N(x)` (or “no record / unspecified” labels).
The theorems use only the *domain* of `η`, namely the six neighbor sites.

The system site is the origin. Auxiliary candidates executed below are
`e1`, `2e1`, `3e1`, and the spacing-3 family `x_k=3k e1` for `k=1,2,3`,
so `{x_1,x_2,x_3}={(3,0,0),(6,0,0),(9,0,0)}`.

Explicit neighbor lists used as witnesses:

```text
N(0)   = {(±1,0,0),(0,±1,0),(0,0,±1)}
N(e1)  = {(0,0,0),(2,0,0),(1,±1,0),(1,0,±1)}   — 0 ∈ N(e1)
N(2e1) = {(1,0,0),(3,0,0),(2,±1,0),(2,0,±1)}   — no origin; shares (1,0,0) with N(0)
N(3e1) = {(2,0,0),(4,0,0),(3,±1,0),(3,0,±1)}   — disjoint from N(0)
N(6e1) = {(5,0,0),(7,0,0),(6,±1,0),(6,0,±1)}   — disjoint from N(3e1) and N(0)
N(9e1) = {(8,0,0),(10,0,0),(9,±1,0),(9,0,±1)}
```

Distances: `d(0,e1)=1`, `d(0,2e1)=2`, `d(0,3e1)=3`, `d(0,6e1)=6`,
`d(0,9e1)=9`.

A **product law** on a finite set of auxiliary sites `{x_1,...,x_n}` is

`P = ⊗_k P_{x_k}`,

with joint condition supported on `⋃_k N(x_k)`. Executed `n` is `3`.

Record lock, content-only readout, and additivity of `I` type a binary
readout of a locked auxiliary possibility as a bit. They do not force that
bit to form, and they do not force its margin to be uniform.

The August 10 interface phrase, quoted only as the open parent, is that a
physical construction that produces registered measurable event partitions
remains open. The present objects are Lattice-typed condition domains, not
that construction.

## Exact Target And Obligation Graph

**Exact target.** On declared cubic nearest-neighbor objects, decide which
auxiliary sites include the origin in their Admissibility condition tuple;
exhibit a spacing-3 family whose neighbor supports are pairwise disjoint and
disjoint from `N(0)`; and record that the resulting product law is not a
function of the origin possibility, without deriving formation or a fair
binary margin.

| Obligation | Role | Disposition |
|---|---|---|
| pin Lattice NN adjacency and `N(x)` | premise | quoted; `|N(x)|=6` listed |
| pin the Admissibility distribution sentence | premise | quoted; no edit |
| pin Record lock, content-only, and additivity | typing only | quoted; formation not derived |
| show `0 ∈ N(e1)` so independence is not forced | Theorem 1 | listing |
| show `0 ∉ N(2e1)` and `0 ∉ N(3e1)` | Theorem 2 | listing |
| show spacing 3 disjoint supports, and the spacing-2 contrast | Theorem 3 | listing |
| show the n=3 product is not a function of the origin | Theorem 4 | condition-domain union |
| record that uniformity and formation are not forced | Theorem 5 | scoped negative |
| derive a physical menu compiler of fair formed bits | autonomous closure | open |
| claim that no compiler exists | non-claim | not attempted |

## Theorem 1 — Adjacent Inclusion

**Claim.** `0 ∈ N(e1)`. Therefore any one-site law at `e1` has the
possibility at the origin as a coordinate of `η`. Independence of that law
from the origin possibility is not a theorem of Admissibility.

**Proof.** By definition

`N(e1)={e1±e1, e1±e2, e1±e3}={(2,0,0),(0,0,0),(1,1,0),(1,-1,0),(1,0,1),(1,0,-1)}`.

The origin appears as `e1-e1`. The Admissibility sentence says that the
probability distribution at `e1` is determined by, and varies with, the
nearest-neighbor conditions. Those conditions are a 6-tuple indexed by
`N(e1)`, one coordinate of which is the possibility at `0`. A law that
depends on that coordinate is permitted. A law that ignores that coordinate
is also permitted. Neither extreme is forced. In particular, independence
from the origin is not a consequence of placing an auxiliary site at graph
distance `1`.

## Theorem 2 — Distance ≥ 2 Exclusion

**Claim.** `0 ∉ N(2e1)` and `0 ∉ N(3e1)`. A one-site law at either site is
therefore a function of a 6-tuple that does not include the origin, and is
not a function of the origin possibility.

**Proof.** The six neighbors of `2e1=(2,0,0)` are

`(1,0,0)`, `(3,0,0)`, `(2,1,0)`, `(2,-1,0)`, `(2,0,1)`, `(2,0,-1)`.

None is the origin. The six neighbors of `3e1=(3,0,0)` are

`(2,0,0)`, `(4,0,0)`, `(3,1,0)`, `(3,-1,0)`, `(3,0,1)`, `(3,0,-1)`.

None is the origin. In both cases `d(0,x)≥2`, and the origin is not among
the six nearest neighbors. The condition domain of `P_x` is exactly `N(x)`.
A map whose arguments are a 6-tuple on a set that does not contain `0` is
not a function of the possibility at `0`.

The same listing shows the spacing-2 contrast used in Theorem 3:
`e1=(1,0,0)` lies in both `N(0)` and `N(2e1)`.

## Theorem 3 — Spacing 3 Disjoint Neighbor Supports

**Claim.** For `k=1,2,3` let `x_k=3k e1`. Then

- `0 ∉ N(x_k)` for each `k`,
- `N(x_j) ∩ N(x_k)=empty` whenever `j≠k`,
- `N(0) ∩ N(x_k)=empty` for each `k`.

Spacing 2 is not disjoint-support: `N(0) ∩ N(2e1)={e1}`.

**Proof.** The three sites are `(3,0,0)`, `(6,0,0)`, and `(9,0,0)`. Their
neighbor sets are the six-point lists recorded in Exact Objects. Direct
comparison of those finite sets gives empty pairwise intersections, empty
intersection with `N(0)`, and exclusion of the origin. The same comparison
for spacing 2 gives

`N(0) ∩ N(2e1)={(1,0,0)}={e1}`.

A one-line metric reason is available and is not a substitute for the
listing. Distinct sites have disjoint neighbor sets if and only if
`d(x,y)≥3`, because a shared neighbor `z` would give `d(x,y)≤d(x,z)+d(z,y)=2`.
Along the `e1` axis, `d(3j e1, 3k e1)=3|j-k|≥3` for `j≠k`, and
`d(0,3k e1)=3k≥3`. Spacing 2 yields `d(0,2e1)=2`, so a shared neighbor is
possible and, by the listing, actual.

Thus `N(6e1)` is disjoint from `N(3e1)` and from `N(0)`, as executed.

## Theorem 4 — Product Law Independent Of The Origin

**Claim.** Let `P=⊗_{k=1}^{3} P_{x_k}` be a product of one-site laws on the
spacing-3 sites of Theorem 3. The joint condition of `P` is supported only
on `⋃_k N(x_k)`, which does not contain `0`. Therefore `P` is not a function
of the origin possibility. Conditional on those one-site laws and on records
forming at the three sites, this is a conditional independence compiler of
the three auxiliary sites from a distant lock.

**Proof.** Each factor `P_{x_k}` is a map of a 6-tuple on `N(x_k)`. The
product is a map of the concatenated tuple on the union
`U=⋃_k N(x_k)`. Theorem 3 gives `0 ∉ N(x_k)` for each `k`, hence `0 ∉ U`.
Two global configurations that differ only at the origin induce the same
tuple on `U`, and therefore the same product value. The product cannot
depend on the origin possibility.

The three neighbor sets are pairwise disjoint, so the concatenated tuple
has eighteen distinct site coordinates and no shared condition site among
the factors. Pairwise disjointness of the *condition* supports is stronger
than origin-exclusion; it is recorded because a later fair-bit compiler
would also need the factors not to condition on one another. It is not used
to force uniformity.

The compiler is conditional. It assumes one-site laws at the declared sites
and assumes records form there. Neither assumption is derived from the four
axioms in this note.

## Theorem 5 — Scoped Negatives

**Claim.** The following three statements are not theorems of Lattice,
Admissibility, and Record on the objects above.

1. Adjacent placement forces independence. False by Theorem 1: `0 ∈ N(e1)`,
   so a one-site law at `e1` is permitted to depend on the origin.
2. Graph separation forces uniform binary margins. False: any product of
   one-site laws on `{x_1,x_2,x_3}` is allowed, including a product of
   biased coins. Uniform `λ_n` is an extra selector.
3. Graph separation forces records to form at the auxiliary sites. False:
   the Admissibility reading note states that the distribution concerns
   which possibility a forming record locks, conditional on formation at
   that site; it does not supply the formation site, probability, or rate.

**Scope.** The negatives are restricted to *forcing* independence from
adjacency, *forcing* `p=1/2` from graph separation, and *forcing* formation
from graph separation. They do not say that no compiler exists. They do not
say that bits are physically formed. They do not propose axiom text.

**Constant-law steelman.** A constant one-site law at `e1` is independent of
every neighbor, including the origin. That special case does not empty
Theorem 1. Theorem 1 says independence is not *forced*; a constant law is an
allowed special case, not a derivation that every law at `e1` is independent.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom update is necessary;
- install a physical menu compiler of registered event partitions;
- claim that no such compiler exists;
- claim that auxiliary bits are physically formed, or that they are fair;
- replace nearest-neighbor adjacency by the 26-site Moore neighborhood;
- identify the present condition-domain split with a continuum `[0,1]`
  factor, or with a bonded-pair `C^2⊗C^2` edge arena;
- close content-only identification of a mathematical event label with
  Record readout beyond the quoted typing sentences.

The scope is the exact cubic split: adjacent inclusion, distance-2
exclusion, spacing 3 disjoint supports, and a product law that is not a
function of the origin.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Lattice NN sentence | premise | quoted; no edit |
| current Admissibility distribution sentence | premise | quoted; no edit |
| current Record lock, content-only, and additivity sentences | typing premises | quoted; formation not derived |
| August 10 type-separation note | open interface phrase only | parent dependency; not re-proved |
| six-neighbor listings and spacing 3 disjointness | Theorems 1--4 | computed here |
| physical bit compiler (formation and fair margin) | residual | open |
| observed frequencies or fitted margins | none | not used |

The exact advance is a finite lattice-geometry theorem. Independent audit
is required. This note authors no audit verdict.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | August 10 states that a physical construction that produces registered measurable event partitions remains open. This note supplies a Lattice-typed independence split for auxiliary sites. It does not call the upstream interface unratified. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for disjoint nearest-neighbor supports, graph-separated auxiliary records, and independent uniform bits. Hits: the August 10 type-separation note names the registered-partition interface and leaves construction open; the bonded-pair color-arena note is a different object (`C^2⊗C^2` on an edge); the QG/microcausality notes are different objects (walk expansions and Lieb-Robinson cones). No landed spacing-3 disjoint-NN independence theorem appears on that commit. Unmerged pull request 6170 constructs a finite `U_n` kernel and leaves independence open; it is not on `origin/main` and is not a premise. |
| V3 | Independently checkable? | Textbook `Z^3` nearest-neighbor adjacency does not mention the August 10 open interface or Record-bit registration. The runner recomputes `N(x)`, graph distance, and disjoint supports by exact integer listing. |
| V4 | More than a restatement? | Yes. The exact `0 ∈ N(e1)` versus `0 ∉ N(2e1)` split, and the shared neighbor at spacing 2 versus empty intersection at spacing 3, are not restatements of the parent type-separation. |
| V5 | One-step relabel? | No. The claim is not a corollary of August 10 or of Record additivity. The closest unmerged comparison is a finite `U_n` kernel that does not use lattice geometry. |

## No-Go Discipline Gate (Theorems 1 and 5 only)

The negative claims are restricted to: adjacent placement does not force
independence; graph separation does not force a uniform binary margin; graph
separation does not force record formation. The gate does not ship a global
non-existence theorem against compilers.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| nearest-neighbor auxiliary at `e1` | treat `P_{e1}` as independent of the origin | Theorem 1: `0 ∈ N(e1)`, so independence is not forced | **ATTEMPTED** |
| distance ≥ 2 one-site law | place the auxiliary at `2e1` or `3e1` | Theorem 2: origin-exclusion holds; this escapes Theorem 1, it does not refute it | **ATTEMPTED** (escape) |
| spacing 3 product | take `P=⊗_k P_{x_k}` on `{3e1,6e1,9e1}` | Theorem 4: the product is not a function of the origin; again an escape from Theorem 1 | **ATTEMPTED** (escape) |
| force `p=1/2` from Admissibility | deduce a fair binary margin from the distribution sentence and graph separation | not derived; any product of one-site laws, including biased coins, remains allowed | **ATTEMPTED** |
| force formation at the auxiliary sites | deduce that records form at `x_k` from Admissibility or from separation | reading note: the distribution does not supply the formation site, probability, or rate | **ATTEMPTED** |
| 26-site Moore neighborhood | replace `N(x)` by the Chebyshev-1 26-set | different adjacency; the diagonal site `e1+e2` has `d(0,e1+e2)=2` yet `0` lies in its Moore neighborhood, so a blanket distance-2 exclusion fails | **ATTEMPTED** (mutation) |
| continuum `[0,1]` factor | replace the lattice sites by a unit-interval ancilla | a different object, not a counterexample to the cubic listing | **ATTEMPTED** |

### N2 — wall independence

Theorems 1 and 5 close only forced independence at an adjacent site, forced
uniformity from separation, and forced formation from separation. They do
not close a later physical compiler, a fair-margin selector, or a
content-only event-label bridge. Those walls remain independent.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `Z^3` with six-neighbor `N(x)` | declared Lattice object |
| one-site condition 6-tuple | declared domain of `η` |
| spacing 3 family `x_k=3k e1` | explicit hypothesis of Theorems 3 and 4 |
| product of one-site laws | declared map on `⋃_k N(x_k)` |
| uniform `λ_n` | extra selector; not derived |
| record formation at `x_k` | open; not assumed as a theorem |
| Moore adjacency | live mutation; not the Lattice adjacency |
| continuum factor | live escape; not executed here |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Lattice NN sentence; Admissibility distribution sentence; Record lock, content-only, and additivity sentences; formation reading note | quoted as premises only; no edit |
| August 10 type-separation note | “a physical construction that produces registered measurable event partitions” remains open | interface parent only; not re-proved |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | named sites `0`, `e1`, `2e1`, `3e1`, `6e1`, `9e1` and their six-point neighbor sets | no classification of every map on `Z^3` |
| per site | one-site laws and the n=3 product on an axis family | no composite bonded-pair theorem |
| per mode | nearest-neighbor condition tuples, not spectral modes | no harmonic-mode exhaustion |
| per block | inclusion/exclusion and spacing-3 disjointness only | no dynamics, formation rate, or fair-margin derivation |
| lattice-wide | checked and not executed | no lattice-wide no-go against compilers |

The obstruction is per-site / declared axis family; it is not lattice-wide.

### N6 — live partial-closure paths

1. A later derivation that records form at the spacing-3 sites.
2. A later selector that forces each binary margin to `p=1/2`.
3. A content-only bridge from the locked auxiliary possibility to a
   registered event-partition label.
4. A different auxiliary geometry, including a continuum factor, if and
   when that object is constructed from the axioms.

The four quoted axiom sentences already name nearest-neighbor conditions,
lock, content-only readout, and additivity. Formation and a fair binary
margin remain open selectors. No axiom sentence is edited here.

### N7 — hostile steelman

> A constant law at `e1` is independent even of its neighbors, so Theorem 1
> is empty: adjacency never forces dependence.

**Answer.** Theorem 1 says independence is not *forced*. A constant law is
an allowed special case of a one-site map `P_{e1}(· | η)`. It is not a
derivation that every law at `e1` is independent of the origin. The
Admissibility sentence permits laws that vary with the origin coordinate of
`η`. The discriminating fact remains `0 ∈ N(e1)`.

### N8 — cross-cycle echo

August 10 Theorems 1--3 are parent negatives about singleton mass,
atomless restriction, and contextual restriction at one `M_2(C)` site. The
present negatives are a different residual: adjacency does not force
independence of an auxiliary one-site law, and graph separation does not
force uniformity or formation. The positive listing (Theorems 2--4) does
not cancel the parent type-separation; it answers the open construction
interface inside a Lattice-typed condition-domain split.

**Gate disposition.** PASS for the scoped cubic split and the three
negatives of Theorems 1 and 5. FAIL / DO NOT SHIP for "no compiler exists"
or "bits are physically formed and fair."

## Primary Runner

[`scripts/graph_separated_auxiliary_records_independent_of_distant_lock_2026_08_13.py`](../scripts/graph_separated_auxiliary_records_independent_of_distant_lock_2026_08_13.py)
recomputes nearest-neighbor sets, graph distances, spacing-3 disjoint
supports, the spacing-2 shared-neighbor contrast, and the product-law
condition-domain claim in exact integer lattice geometry. Identity gates
call `neighbors(x)` and `disjoint_supports(sites)`. Replacing `neighbors`
by the 26-site Moore neighborhood must fail a blanket distance-2 exclusion.
Replacing spacing 3 by spacing 2 must fail disjoint-support. A declared
always-independent-even-of-neighbors predicate must fail Theorem 1.
