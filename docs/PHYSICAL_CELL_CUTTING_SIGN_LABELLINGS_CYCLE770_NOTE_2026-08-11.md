# Three sign labellings split every finite four-cube cover four and four

Date: 2026-08-11

Authority: none

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Machine status:

```yaml
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Send the self-contained finite theorem and runner to independent audit; no downstream consumer is yet known."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact finite theorem for sign characters, transported piece labellings, cover sums, ranks, and corner-subset and orientation censuses on one declared unit-four-cube object."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Runner:

- [physical_cell_cutting_sign_labellings_cycle770_2026_08_11.py](../scripts/physical_cell_cutting_sign_labellings_cycle770_2026_08_11.py)

Framework premise edges: 0.

This finite construction adds no axiom to the framework. The current Minimal
Axioms file, `MINIMAL_AXIOMS_2026-06-29.md`, is a scope marker only and supplies
no premise to the theorem.

## Imports and provenance

- Scientific file inputs: none. The unit four-cube, determinant-one simplex
  rule, adjacency-cost minimum, divisor-80 rational sample, full signed
  coordinate action, two primes, and orientation ordering are declared finite
  construction choices. Every count, incidence, character, rank, and census is
  recomputed by the runner.
- Measured, fitted, literature, predecessor, sibling-branch, and framework
  inputs: none. In particular, this theorem carries no rank ceiling or global
  deficit from another cycle.
- Package-local reads: the runner reads its own `__file__` only for source
  integrity and hygiene. That read is not a scientific input. The canonical
  cache records a run but is never read by the runner.
- Implementation provenance: the exact rational intersection algorithm was
  adapted from the current-main runner
  `physical_cell_cutting_complement_rank_corner_strata_2026_08_09.py`, then
  included and gated self-contained here. No count, certificate, or output is
  imported from that runner.
- Arithmetic: mathematical gates use Python integers, exact `Fraction`
  arithmetic, and two declared finite fields. Wall time and peak memory appear
  only in the support budget gate.

## Exact target and obligation graph

Let `P` be the 192 used determinant-one pieces, `K` the 15800 declared
24-piece cuttings, `C` the 192 eight-piece covers, and `G` the 384 signed
coordinate maps constructed below. The exact finite target is: `G` has exactly
four sign characters; each transports to a `+1/-1` labelling of `P`; each of
the three nonconstant labellings sums to zero on every cover, so every cover
contains four pieces of each sign; and the accompanying character-sector,
incidence-rank, corner-subset, axis, and orientation counts stated below hold
for these declared finite sets.

The acyclic proof obligations are:

- `P0` [proved here]: enumerate the unit-determinant pieces, cost minimum, and
  generic rational sample (`C0`).
- `P1` [proved here; depends on `P0`]: exhaust the sample exact covers and
  certify every co-occurring pair by exact rational facet separation or an
  intersection of affine dimension at most one. With 24 simplex volumes of
  `1/24`, pairwise interior disjointness gives geometric cuttings (`C0`).
- `P2` [proved here; depends on `P1`]: enumerate the used pieces and all
  eight-piece covers, and verify that every cover meets every cutting once
  (`C0`, `C1`).
- `P3` [proved here; depends on `P0`-`P2`]: build `G`, its actions, orbits,
  stabilizers, and exactly four sign characters (`C2`-`C8`).
- `P4` [proved here; depends on `P3`]: transport all four characters to
  well-defined equivariant piece labellings (`C9`).
- `P5` [proved here; depends on `P2`, `P4`]: certify the three cover-balanced
  nonconstant labellings and their four-plus/four-minus splits (`C10`).
- `P6` [proved here; depends on `P2`, `P4`]: derive the flip-parity closed form
  and the exact four-axis cover histograms (`C11`-`C14`).
- `P7` [proved here; depends on `P2`, `P4`]: certify rational independence,
  integer blindness, and rank 105 by a determinant-unit minor plus integral
  row-lattice reconstruction (`C16`-`C18`).
- `P8` [proved here; depends on `P3`, `P5`]: compute the four one-dimensional
  character-sector multiplicities, two structural zeros, and one measured rank
  deficit inside those sectors (`C19`-`C21`).
- `P9` [proved here; depends on `P2`, `P4`, `P6`]: enumerate all 65536 corner
  subsets and record the exact blind-subset, axis, and orientation-match
  censuses (`C25`-`C27`).

Every obligation of the finite target is proved here; none is retained-cited or
open. The strongest missing lemma is therefore none within this bounded target.
Any map from these finite objects to Record content, any multi-cell extension,
and any physical interpretation lie outside the target and would require a
separate claim package.

## 1. Finite object and geometric certificate

Write the sixteen cube corners as `V = {0,1}^4`. A candidate piece is a
five-corner subset with determinant magnitude one, hence volume `1/24`. Its
adjacency cost counts corner pairs whose Hamming distance exceeds one. Of 2672
unit-determinant candidates, 400 attain the minimum cost 6.

The runner finds 15800 sample exact covers of size 24 on a 625-point rational
grid avoiding every selected-piece facet. It then checks every pair of pieces
co-occurring in any such cover. Of 15168 pairs, 13632 are separated by a simplex
facet; the remaining intersections have affine dimension zero for 864 pairs and
one for 672 pairs. Thus all co-occurring interiors are disjoint. Their 24 volumes
sum to the cube volume, so each sample cover is a geometric cutting. Conversely,
every cutting covers the generic sample and therefore occurs in the exhaustive
sample-cover search (`C0`).

Exactly 192 pieces occur. Each lies in 1975 cuttings. A cover is an eight-piece
set whose members never co-occur in a cutting; the runner enumerates 192 and
checks that each meets every cutting exactly once (`C0`, `C1`).

The boundary cases are explicit: candidate determinants of magnitude other
than one and costs above six are outside `P`; intersections of affine dimension
zero or one are allowed boundary contacts; positive-volume intersections would
fail `C0`; the cutting size is exactly 24 and the cover size exactly eight.

## 2. Group, characters, and transported labellings

Permuting four coordinates and flipping any subset gives 384 maps. The runner
checks closure, distinctness, the induced piece and cover bijections, transitivity
of both 192-element actions, and order-two point stabilizers (`C2`-`C5`).

Two exhibited elements generate all 384 maps, so a sign character is fixed by
two binary values and at most four exist. The trivial character, permutation
sign, flip parity, and their product are four distinct homomorphisms on all
147456 products, establishing exactly four (`C6`). Their values on both point
stabilizers and the corresponding fixed-point counts are checked in `C7` and
`C8`.

All four characters are trivial on the piece stabilizer. Giving piece zero
label `+1` therefore transports each character uniquely across the orbit, up to
a global sign. The runner checks well-definedness and equivariance on all 73728
map-piece pairs. The plus counts are 192, 96, 96, and 96 (`C9`).

## 3. Cover splitting and closed form

The trivial labelling sums to 8 on every cover. Each nonconstant labelling sums
to zero on all 192 covers, so each cover contains four plus and four minus pieces
for each of those three labellings (`C10`).

The flip-parity labelling equals the parity of the total number of ones across
the five corner vectors of a piece (`C11`). It is the product of four single-axis
parities (`C12`). Each axis has 96 labels of each sign and the same cover-sum
histogram: `-8` on 24 covers, `0` on 144, and `8` on 24 (`C13`). The four sets
of 48 one-sided covers are pairwise disjoint and partition all covers (`C14`).

## 4. Independence, exact rank, and character sectors

The three nonconstant labellings have Gram matrix `diag(192,192,192)`, hence are
rationally independent (`C16`). Each lies in the integer kernel of the
192-by-192 cover-by-piece incidence matrix (`C17`). A 105-by-105 minor has
determinant `-1`, and every incidence row is reconstructed as an integer
combination of those 105 rows. The rank is therefore exactly 105 and the blind
dimension exactly 87 over every field (`C18`). The two fixed-prime ranks are
corroboration rather than the characteristic-independent proof.

In the four one-dimensional character sectors, piece multiplicities are
`[1,1,1,1]` and cover multiplicities are `[1,1,0,0]`. The last two characters
have no cover-side copy, so their zero cover sums are structural (`C19`). The
permutation-sign sector occurs once on each side; its one even cover block is
measured as zero (`C20`). Consequently the sector rank ceiling is two, the
actual sector rank is one, and the rank deficit within these four sectors is one
(`C21`). This statement is scoped only to the four one-dimensional sectors.

## 5. Corner-subset, axis, and orientation finite censuses

An exact walk over all 65536 subsets of the 16 corners finds exactly two whose
induced piece-parity vector has zero sum on every cover. Both have size eight:
mask 27030, the odd-weight corners, and complementary mask 38505 (`C25`). Since
each piece has five corners, complementing a subset negates its vector. Mask
27030 reproduces the flip-parity labelling (`C26`). Thus the census contains one
cover-balanced piece-parity vector up to global sign.

The four single-axis masks all have the cover-sum histogram stated in section 3.
The separately declared orientation sign uses the determinant of the ordered
four edge vectors from each piece's first corner. It has 96 signs of each kind,
cover-sum histogram `{-8:6,-4:32,-2:16,0:84,2:16,4:32,8:6}`, and Hamming
distance 96 from the corner-ones parity (`C15`). Among the 65536 explicitly
enumerated subset-parity vectors, the number matching either global orientation
sign is zero (`C27`). These are finite census results only.

## 6. Validation and support gates

The mathematical result is carried by `C0`-`C21` and `C25`-`C27`. Gates
`C22`-`C24` are validation-only controls for label and action perturbations.
`C28` is an environment-dependent support budget, bound to the runner's declared
300-second audit timeout and a 2500 MB peak-memory limit. `C29` is source hygiene.
The runner exits nonzero whenever any gate fails.

Independent review also exercised scratch-source mutations across every
load-bearing family; the mutation-to-failing-tag table is recorded with the PR
review provenance rather than counted as a theorem premise. The canonical cache
is generated through the repository envelope. A successful run ends with:

```text
TOTAL: PASS=30 FAIL=0
```

## Review record

- Removed the unaudited carried ceiling, global deficit, and earlier-cycle
  numerical comparison; the surviving deficit statement is local to the four
  one-dimensional character sectors.
- Recast the orientation and axis results as positive exact finite censuses.
- Added the exact pairwise geometric certificate, fail-closed exit, declared
  timeout, platform-aware peak-memory normalization, complete import/status
  record, obligation graph, and explicit boundary.
- No framework premise, methodology change, generated audit verdict, effective
  status, or physical-law interpretation is included.
