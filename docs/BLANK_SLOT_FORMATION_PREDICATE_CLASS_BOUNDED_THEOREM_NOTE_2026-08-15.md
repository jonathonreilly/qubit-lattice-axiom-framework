---
claim_id: blank_slot_formation_predicate_class_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cube-covariant boolean predicates on {0,1,blank}^6 form a set of size 2^{N_orb_⊥} with N_orb_⊥ > 10. Restriction to {0,1}^6 is onto F_G. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/blank_slot_formation_predicate_class_2026_08_15.py
---

# Blank-Slot Formation-Predicate Class

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact orbit count of cube-covariant boolean predicates on the
six nearest-neighbor slots with alphabet `{0,1,blank}`. The class is
displayed, not adopted as a physical formation law.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/blank_slot_formation_predicate_class_2026_08_15.py`](../scripts/blank_slot_formation_predicate_class_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The six nearest-neighbor slots at one site carry letters from the three-letter
alphabet `A = {0,1,blank}`. The configuration space is `A^6` and has 729
cells. The group `G` of 24 proper cube rotations permutes those slots and
fixes the letter `blank`: a rotation never turns `blank` into `0` or `1`.

A boolean ready-predicate is a map `f: A^6 → {0,1}`. It is cube-covariant
when `f(g·x) = f(x)` for every `g ∈ G`. Such maps are exactly the
assignments of a bit to each `G`-orbit, so if `N_orb_perp` is the number of
orbits then

`|F_perp| = 2^{N_orb_perp}`.

Theorem 1 enumerates all 729 cells under the 24 rotations and obtains

`N_orb_perp = 57`, `|F_perp| = 2^{57} = 144115188075855872`.

The same count is recovered from Burnside's lemma. The binary subset
`{0,1}^6` is `G`-invariant and splits into 10 orbits, so the previously
counted covariant class `F_G` on `{0,1}^6` has size `2^{10} = 1024`.
Restriction `F_perp → F_G` is a surjective homomorphism of Boolean cubes:
every covariant binary predicate extends by the constant `0` on any cell
that contains a `blank`. Because `N_orb_perp > 10`, one has the strict
enlargement `|F_perp| > |F_G|`. Blank is new orbit content, not a
relabeling of `0`.

No member of `F_perp` is selected as a formation site, formation
probability, formation rate, or Record compiler. The class is displayed,
not adopted.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The only use of those sentences is to name the six nearest-neighbor slots
and the 24 proper rotations that permute them. The axiom does not name the
three-letter alphabet, a ready-predicate, or a formation selector.

The current Record wording is:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility, read with Record, concerns which possibility a forming record
locks, conditional on formation at that site; it does not supply the formation
site, probability, or rate. Counting `F_perp` does not close that gap.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 729-cell enumeration, the 24-element rotation group, the orbit count N_orb_perp=57, the identification |F_perp|=2^{N_orb_perp}, the surjective restriction onto F_G, and the strict inequality N_orb_perp>10 are finite exact identities. No physical ready-predicate is selected."
trace_class: negative_route_pruning
target_claim_id: blank_slot_formation_predicate_class
target_blocker_text: "count the cube-covariant boolean ready-predicates on {0,1,blank}^6 and compare the class to F_G"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Do not adopt a member of F_perp as a formation law. Any physical use must separately derive a selector, a Record content map, and a formation site."
conditional_surface_status: "exact for boolean G-covariant maps on the displayed three-letter six-slot cube; ternary ready/blocked/no maps and physical adoption remain unclaimed"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Label the six nearest-neighbor directions at the origin by

`(+x,-x,+y,-y,+z,-z)`.

A configuration is a 6-tuple with values in `A = {0,1,blank}`. The letter
`blank` is a third alphabet symbol, not a synonym for `0`. The group `G` is
the group of `3×3` signed permutation matrices of determinant `+1`. Each
matrix sends face normals to face normals and therefore induces a permutation
of the six slots. There are 24 such matrices, they form a group, and the
induced slot permutations are 24 distinct elements of `S_6`.

The action on configurations is the ordinary left action

`(g·x)_i = x_{g^{-1}i}`.

Because `g` only permutes coordinates, the letter-count triple

`(n_0, n_1, n_blank)`

is a `G`-invariant. In particular `blank` remains `blank`.

Write `F_perp` for the set of functions `f: A^6 → {0,1}` satisfying
`f(g·x)=f(x)` for all `g∈G`. Write `F_G` for the same class on the
`G`-invariant subset `{0,1}^6`.

## Theorem 1 — Orbit Count

Enumerate the 729 cells. For each cell form the 24 images under `G` and
retain the lexicographic minimum as the orbit representative. The distinct
representatives number

`N_orb_perp = 57`.

Independently, Burnside's lemma applied to the same 24 permutations gives

```text
(1 · 3^6 + 6 · 3^3 + 3 · 3^4 + 8 · 3^2 + 6 · 3^3) / 24
  = (729 + 162 + 243 + 72 + 162) / 24
  = 1368 / 24
  = 57.
```

The five summands are the identity, the six 90°/270° face rotations (cycle
type `4,1,1`), the three 180° face rotations (cycle type `2,2,1,1`), the
eight 120°/240° vertex rotations (cycle type `3,3`), and the six 180°
edge rotations (cycle type `2,2,2`). A coloring is fixed only when it is
constant on cycles, so the displayed powers of 3 are exact.

Covariant boolean predicates assign one bit per orbit, therefore

`|F_perp| = 2^{57} = 144115188075855872`.

This is a new alphabet, not a leftover character of the binary count on
`{0,1}^6`.

## Theorem 2 — Restriction Onto `F_G`

The subset `{0,1}^6` is `G`-invariant: a rotation never manufactures a
`blank`. The same enumeration, now restricted to the 64 binary cells, yields
exactly 10 orbits. Burnside with two letters recovers the same 10. Hence
`|F_G| = 2^{10} = 1024`.

Restriction of a covariant `f ∈ F_perp` to `{0,1}^6` is a covariant
predicate on `{0,1}^6`, so there is a well-defined map `F_perp → F_G`.
It is surjective: given `h ∈ F_G`, set

`f(x) = h(x)` if `x ∈ {0,1}^6`, and `f(x) = 0` if `x` contains a `blank`.

The blank-bearing set is itself `G`-invariant, so `f` is covariant, and
`f` restricts to `h`. The runner checks this extension on all 1024 members
of `F_G`.

## Theorem 3 — Strict Enlargement

Of the 57 orbits, exactly 10 are binary and 47 contain at least one
`blank`. Therefore `N_orb_perp > 10` and

`|F_perp| = 2^{57} > 2^{10} = |F_G|`.

Letter counts distinguish the new orbits from any relabeling of `0`. The
all-zero cell `(0,0,0,0,0,0)` and the all-blank cell
`(blank,blank,blank,blank,blank,blank)` lie in different orbits. The cell
with a single `blank` and five zeros has letter count `(5,0,1)` and cannot
be rotated onto any binary cell.

The 10 binary orbits are the classical two-color face colorings of the
cube. The 47 blank-bearing orbits are additional content. Treating `blank`
as `0` would collapse those 47 orbits into the 10 binary ones and would
erase the inequality.

## Mutations

1. Replace `blank` by `0` before counting: the letter-count invariant is
   destroyed and the orbit count collapses to 10.
2. Count all boolean maps on `A^6` without covariance: the class has size
   `2^{729}`, not `2^{57}`.
3. Replace `G` by the 48-element group that includes reflections: that is
   a different group and a different class.
4. Count maps to `{ready, blocked, no}`: that class has size `3^{57}`,
   which this note does not claim.
5. Adopt one displayed member of `F_perp` as the formation law: no such
   selection is performed or licensed.
6. Claim that restriction `F_perp → F_G` misses some binary predicate:
   the zero-on-blank extension hits every member of `F_G`.

## What This Does Not Claim

- No physical formation site, probability, or rate.
- No member of `F_perp` is selected as the Admissibility rule.
- No ternary ready/blocked/no classification is counted.
- No Record content map, readout compiler, or occurrence law.
- No leftover-character reading of the binary class `F_G`.
- No axiom edit and no approved-primitive registration.

## No-Go Discipline Gate

The negative claim is only that the three-letter covariant class is
strictly larger than `F_G` and is not a relabeling of the binary alphabet.
It is not a claim that a physical ready-predicate is impossible, and it is
not a claim that any particular member of `F_perp` is the formation law.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| leftover-character collapse | Identify `blank` with `0` and reuse the 10 binary orbits. | Theorem 3: letter counts are `G`-invariants; 47 orbits carry a `blank`. | **ATTEMPTED** |
| unconstrained function count | Count all maps `A^6 → {0,1}` without covariance. | Theorem 1: covariance forces constancy on orbits, so `2^{57}` not `2^{729}`. | **ATTEMPTED** |
| full octahedral group | Replace the 24 proper rotations by the 48-element group with reflections. | Theorem 1 constructs `G` as determinant-`+1` signed permutation matrices only. | **ATTEMPTED** |
| ternary ready/blocked/no class | Count maps to a three-value codomain. | The displayed class is boolean; a ternary count would be `3^{57}` and is unclaimed. | **ATTEMPTED** |
| physical adoption | Treat the existence of `F_perp` as a selected formation predicate. | The class is displayed, not adopted; Admissibility still withholds formation. | **ATTEMPTED** |
| restriction failure | Claim some covariant binary predicate has no covariant three-letter extension. | Theorem 2: zero-on-blank extension is covariant and hits every member of `F_G`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one counting theorem and one comparison. The Burnside evaluation
and the 729-cell enumeration are two certificates of the same orbit count;
they collapse rather than count as independent walls. The surjective
restriction and the strict inequality are separate conclusions: one compares
domains, the other compares cardinalities.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| enumeration / Burnside | yes, both compute `N_orb_perp` | yes | collapse into Theorem 1 |
| restriction onto `F_G` / `|F_perp| > |F_G|` | no: surjectivity does not force extra orbits | no: extra orbits do not by themselves construct the extension | independent conclusions |
| letter-count invariant / leftover-character collapse | yes, for the relabeling route | yes, as the explicit invariant | collapse into Theorem 3 |

Physical formation, ternary maps, and axiom edits are not walls: this note
makes no negative theorem that they are impossible and simply does not
claim them.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| six nearest-neighbor slots | cited Lattice adjacency; grants only the geometric domain |
| 24 proper cube rotations | cited Lattice/Admissibility covariance group; constructed as det `+1` signed permutation matrices |
| alphabet `{0,1,blank}` | explicit theorem hypothesis; not supplied by the axioms |
| boolean ready-predicate | explicit codomain `{0,1}`; ternary maps excluded |
| “displayed, not adopted” | status of the counted class; not a selected law |
| Record lock/content/absence | cited only to keep formation and readout unclaimed |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | geometric six-slot domain | cubic nearest-neighbor sites and proper rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:56` | covariance group | one admissibility rule, covariant under proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:68` | formation gap | formation site, probability, and rate remain unsupplied | yes; boundary stays open |
| `scripts/blank_slot_formation_predicate_class_2026_08_15.py:129` | orbit enumeration | 729 cells under 24 rotations | yes |
| `scripts/blank_slot_formation_predicate_class_2026_08_15.py:296` | Burnside cross-check | same `N_orb_perp` from cycle index | yes |
| `scripts/blank_slot_formation_predicate_class_2026_08_15.py:365` | restriction onto `F_G` | zero-on-blank extension hits all 1024 binary predicates | yes |
| `scripts/blank_slot_formation_predicate_class_2026_08_15.py:380` | strict enlargement | `N_orb_perp > 10` | yes |

No evidence citation is used to claim that a physical ready-predicate,
formation site, or Record compiler has been selected.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 729 cells | each cell is assigned its orbit representative |
| per site | yes: six slots at one displayed site | no other site or composite is classified |
| per mode | yes: boolean `G`-covariant predicates | ternary ready/blocked/no maps are uncounted |
| per block | yes: restriction `F_perp → F_G` | zero extension is onto; no physical selector is inferred |
| lattice wide | no | no lattice-wide ready law or formation process is asserted |

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies the three-letter alphabet or a ready-predicate.
None is reclassified as an import or wall.

Two partial-closure mechanisms were tested rather than suppressed. Burnside
reproduces the enumeration, and zero-on-blank extension reproduces every
binary covariant predicate. Neither mechanism selects a physical member of
`F_perp` or supplies formation. Those remaining choices stay explicit and
do not require an axiom edit to state honestly.

### N7 — hostile steelman

The strongest objection is that `blank` is only an unread site, already
typed by Record as “a site with no record cannot be read,” so identifying
`blank` with `0` should not change the covariant class. That objection
names a reading of absence, not an alphabet identification. The theorem
treats `blank` as a third letter on the six condition slots. The
letter-count invariant then produces 47 orbits that no rotation can carry
onto `{0,1}^6`. To overturn the strict enlargement one would have to
exhibit a `G`-equivariant bijection between `A^6` and `{0,1}^6`, which
these sets do not admit, or change the group, or change the alphabet.

### N8 — cross-cycle echo

This note does not load a parent counting surface. The binary count
`|F_G|=2^{10}` is recomputed here by the same 24 rotations acting on the
64 binary cells. No earlier mechanism retires the three-letter enlargement.
A leftover-character reading of the binary class is exactly the mutation
ruled out by Theorem 3.

No-Go Discipline disposition: **PASS** for the algebraic class-count and
the display-only status stated at the start of this section.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility.

> A readout value is determined by record content alone.

> A site with no record cannot be read.

## Runner Contract

The companion runner constructs the 24 proper rotations, enumerates the 729
cells, matches Burnside, counts the 10 binary orbits, checks that
zero-on-blank extension hits every member of `F_G`, verifies
`N_orb_perp > 10`, and pins the quoted axiom boundary. Declared audit
inputs are this note and the axiom memo only.
