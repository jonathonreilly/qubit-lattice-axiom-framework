# Four-cube cutting fixed-point counts, cell freeness, and a modular blind-floor identity

Date: 2026-08-11

Authority: none

Status: proposed_retained

Claim type: bounded_theorem

Runner:

- [`four_cube_cutting_fixed_point_orbit_floor_2026_08_11.py`](../scripts/four_cube_cutting_fixed_point_orbit_floor_2026_08_11.py)

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, effective status, or framework claim.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The prime-free geometric and group-action counts are exact for one finite four-cube cutting system; the 20-row part table and its numerical floor are computed over the explicitly declared field F_1000003."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "seek a characteristic-zero derivation of the full 20-row part table and a structural explanation of the values 8 and 48"
conditional_surface_status: "exact finite geometry, fixed-point, orbit, and freeness results; fixed-field support for the part-table floor and ceiling"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target contract

For the explicitly constructed four-cube cutting system and its order-384
coordinate symmetry group, the four stabilizer fixed-set sizes

```text
(Fix_P(s_p), Fix_C(s_p), Fix_P(s_c), Fix_C(s_c)) = (16, 0, 0, 48)
```

force ordered-pair orbit counts `(104, 120, 96)`, imply that the action on the
36,864 cover-by-piece cells is free, and, conditional on the 20-row
decomposition computed over `F_1000003`, give blind floor 48 and the rowwise
identity `ceiling 144 + floor 48 = 192`. The full 20-row characteristic-zero
decomposition is not claimed.

## Computational conditions and imported-value boundary

The runner reads no external scientific input. It constructs the finite object
from the sixteen corners of the unit four-cube. The two explicit computational
fields are:

- `p = 1,000,003`: the load-bearing field for the complete 20-row modular part
  table, including its multiplicities, blind dimensions, floor 48, and ceiling
  144;
- `p2 = 1,000,033`: a limited comparator used only to recompute the rank of one
  192-by-192 cell-orbit matrix in C30.

Neither prime is derived from a framework axiom, fitted to an observation, or a
certificate for all characteristic-zero ranks. The construction of the cutting
corpus, the group action, the four fixed counts, the three orbit counts, and
cell freeness are field-independent exact finite combinatorics. The numerical
part-table conclusions inherit the `F_1000003` boundary.

## Finite object and exact geometric cutting gate

Among five-corner simplices of unit absolute determinant, the adjacency-cost
floor is 6 and 400 candidates attain it. A 625-point generic grid is used only
to enumerate candidate 24-piece exact covers efficiently; it is not treated as
a universal detector of simplex overlap.

The runner then closes that gap exactly. It gathers all 15,168 distinct simplex
pairs that co-occur in one of the 15,800 candidates and checks rational
half-space feasibility for strict interior intersection. The coordinate group
reduces these pairs to exact orbit representatives, and the runner checks each
representative using only rational arithmetic. No co-occurring pair has
intersecting strict interiors. The known adversarial pair with corner sets
`(0,1,2,4,8)` and `(0,1,3,7,15)` is also checked: its sample masks are disjoint,
but both interiors contain `(4,3,2,1)/11`, so the exact gate rejects it.

Each selected simplex lies inside the four-cube and has four-volume `1/24`.
Thus 24 pairwise interior-disjoint selected simplices have total volume one,
equal to the four-cube. A nonempty uncovered interior region would have positive
volume, so the selected union covers the cube up to the shared boundary. This
turns each selected candidate into a genuine cutting rather than a sample-grid
partition.

The resulting exact corpus contains 15,800 cuttings, 192 pieces that occur, and
192 covers. Each cutting has 24 pieces; each piece lies in 1,975 cuttings; each
cover has eight pieces and meets every cutting exactly once.

## Stabilizer-orbit lemma

Let a finite group `G` act transitively on `X`, choose `x0`, and suppose
`Stab(x0) = {e,s}`. For any `G`-set `Y`, every orbit in `X x Y` meets
`{x0} x Y`, and two points in that slice are equivalent exactly when their
`Y`-coordinates lie in the same `Stab(x0)`-orbit. Therefore

```text
number of G-orbits on X x Y = (|Y| + Fix_Y(s)) / 2.
```

The runner constructs all 384 coordinate permutations and flips and proves
that they act transitively on both the 192 pieces and the 192 covers. The
stabilizer of a selected piece and the stabilizer of a selected cover both have
order two.

## Fixed sets, orbit counts, and freeness

Writing `s_p` and `s_c` for the nonidentity elements of the piece and cover
stabilizers, direct enumeration gives

```text
s_p fixes 16 pieces and 0 covers;
s_c fixes 0 pieces and 48 covers.
```

The stabilizer-orbit lemma then gives

```text
ordered piece-pair orbits = (192 + 16) / 2 = 104,
ordered cover-pair orbits = (192 + 48) / 2 = 120,
cover-by-piece orbits      = (192 +  0) / 2 = 96.
```

The sweep, generator walk, and fixed-point average are three internally
distinct calculations on the same constructed action. They are cross-checks,
not three implementation-independent constructions. An additional direct
coordinate-set calculation bypasses the stored piece and cover permutation
tables and independently recomputes the four fixed sets.

Because the nonidentity element of a cover stabilizer fixes no piece, the
intersection of that cover stabilizer with every piece stabilizer is trivial.
Transitivity carries this statement to every cover. Hence every cell
stabilizer is trivial, the action on `192 * 192 = 36,864` cells is free, and

```text
36,864 / 384 = 96 = 384 / (2 * 2).
```

## Fixed-field part table and positive floor

Over `F_1000003`, each of the 20 part-table rows has dimension per copy `d` and
multiplicities `m` and `mc`. The runner gates

```text
sum m^2    = 104,
sum mc^2   = 120,
sum m*mc   = 96,
sum d*m    = 192,
sum d*mc   = 192.
```

Consequently `sum m(m-mc) = 8 > 0`. Since all multiplicities are
nonnegative, at least one row has `m > mc`; the table contains ten such rows.
The modular blind floor

```text
sum d*max(0,m-mc)
```

is therefore positive and evaluates to 48 in this table.

For every row,

```text
d*min(m,mc) + d*max(0,m-mc) = d*m.
```

Summing gives `ceiling 144 + floor 48 = 192`. This additive identity is
algebraic once the row values are supplied; the numerical values 144 and 48
retain the fixed-field boundary. C30 also finds rank 144 and nullity 48 for one
cell-orbit matrix at both declared primes, but that limited comparison does not
recompute the full table at `p2`.

## Proof-obligation graph

| ID | Obligation | Depends on | Status in this package |
| --- | --- | --- | --- |
| O1 | Enumerate the candidate simplices and sample-grid covers. | none | proved by C0-C1 |
| O2 | Prove every selected 24-set is a geometric cutting by exact pair compatibility and total volume. | O1 | proved by C35, including an overlap mutation |
| O3 | Construct the order-384 action, transitivity, and order-two stabilizers. | O1-O2 | proved by C2-C7 |
| O4 | Prove the stabilizer-orbit lemma. | none | proved above |
| O5 | Establish the four fixed-set sizes by the action and direct coordinate sets. | O3 | proved by C11-C13 and C36 |
| O6 | Derive orbit counts and cell freeness. | O3-O5 | proved by C8-C19 |
| O7 | Construct and bridge the 20-row table over `F_1000003`. | O3 | bounded computation, C20-C24 |
| O8 | Derive the positive floor and rowwise additive identity from O7. | O7 | proved conditionally, C25-C30 |
| O9 | Lift every row rank to characteristic zero. | O7 | open; not used as a claim |

There is no hidden target-equivalent lemma. O9 is a strictly stronger statement
than the fixed-field target and remains open.

## Boundary and degenerate cases

- The stabilizer-orbit formula in this form assumes a transitive action on the
  first factor and a stabilizer of order exactly two. Nontransitive actions or
  other stabilizer orders require the general orbit decomposition instead.
- The geometric conclusion applies to the explicitly enumerated unit-volume
  simplices. Degenerate simplices or overlapping strict interiors fail the
  exact gate.
- The rowwise additive identity permits zero multiplicities, but the runner
  separately establishes `m > 0` for every constructed row over `F_1000003`.
- A bad-prime rank drop could alter a modular row. The bridge to the exact orbit
  counts constrains aggregate sums but does not by itself lift each row to
  characteristic zero.
- This note makes a finite combinatorial and fixed-field algebraic statement.
  It does not assign a physical interpretation to the floor or the table.

## Mutation and independent-check record

The runner performs reverted in-memory mutations, each against its named
load-bearing family:

- the exact geometry gate rejects the sample-grid false-negative overlap pair;
- a corrupted stabilizer permutation fails the group/action validator;
- a nonzero cross-fixed cell count fails the freeness validator;
- a changed part multiplicity fails the row/bridge validator;
- a changed floor term fails the rowwise additive validator.

The pre-existing generator swaps and wrong-value rejectors remain additional
sensitivity checks. Every mutation is confined to a copied value or structure;
the accepted computation is then checked unchanged. The runner exits nonzero
if any top-level gate fails.

An implementation-independent review calculation rebuilt the candidates,
sample-grid solutions, covers, and coordinate action without importing runner
code. It reproduced 400 candidates, 15,800 selected solutions, 192 pieces, 192
covers, stabilizer orders two, fixed sets `(16,0,0,48)`, and orbit counts
`(104,120,96)`. A separate literal-row calculation reproduced all stated
part-table sums, and exact rational rank of the single C30 matrix was 144 with
nullity 48. These checks support the finite result without widening the landed
claim beyond the declared field.

## Review record

Review on 2026-08-17 narrowed the package to its exact finite and fixed-field
content. It replaced campaign naming with a domain-explicit identity, removed
an unused axiom dependency, separated prime-free from modular leaves, named
both computational fields, added the obligation graph and edge cases, added an
exact geometric admissibility certificate with a false-negative mutation, and
made the shared-action cross-check language explicit. No effective status or
independent audit result is asserted here.
