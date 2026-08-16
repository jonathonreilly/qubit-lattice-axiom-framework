# Complementary ranks and corner-overlap strata for the unit four-cube

Date: 2026-08-09

Authority: none

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
next_trace_action: "Send the self-contained finite theorem and measurements to independent audit; no downstream consumer is yet known."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The note proves one finite complementary-rank identity and records exact measurements on its explicitly defined unit-four-cube object."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Runner:

- [physical_cell_cutting_complement_rank_corner_strata_2026_08_09.py](../scripts/physical_cell_cutting_complement_rank_corner_strata_2026_08_09.py)

Framework premise edges: 0.

The construction uses no framework axiom, approved primitive, measured input,
fitted constant, literature value, predecessor note, or sibling branch. Its only
inputs are the finite definitions below, integer and rational arithmetic, and two
declared primes used for non-authoritative cross-checks. This note changes no
axiom, primitive, registry, policy, audit verdict, effective status, or framework
claim.

## Finite object

Write the sixteen corners of the unit four-cube as
$V=\{0,1\}^4$. A candidate piece is a five-element subset
$P=\{v_0,\ldots,v_4\}$ for which

\[
\left|\det(v_1-v_0,\ldots,v_4-v_0)\right|=1.
\]

Thus every candidate has four-volume $1/24$. Define its adjacency cost by

\[
a(P)=\#\bigl\{\{u,v\}\subset P:d_H(u,v)>1\bigr\},
\]

where $d_H$ is four-bit Hamming distance. The selected pieces are exactly the
candidates attaining the minimum cost. The runner reconstructs 2672 candidates,
minimum cost 6, and 400 selected pieces.

A cutting is a set of 24 selected pieces with pairwise disjoint interiors whose
union is the cube. The runner builds these as exact covers on a rational sample
grid that avoids every piece facet, then separately verifies exact
interior-disjointness and total volume. There are 15800 cuttings. A piece is
*used* when it occurs in a cutting; 192 pieces are used.

A cover is an eight-element set of used pieces such that no two occur in a
common cutting and each cutting contains exactly one of them. There are 192
covers. The $192\times192$ cover table $B$, indexed by covers and used
pieces, has $B_{C,P}=1$ exactly when $P\in C$. Its exact rational rank is 105.

Permuting the four coordinates and independently flipping them gives a group
$G$ of order 384. The runner verifies the action on pieces and covers, its
transitivity on both 192-element sets, and its 96 orbits on cover-piece cells.
For a cell orbit $o$, let $M_o$ be its $0/1$ orbit table. The four orbits
whose cells are incidences sum to $B$.

## Complementary-rank theorem

For every nonempty proper subset $S$ of the 96 cell orbits,

\[
\operatorname{rank}_{\mathbb Q}\!\left(\sum_{o\in S}M_o\right)
=
\operatorname{rank}_{\mathbb Q}\!\left(\sum_{o\notin S}M_o\right).
\]

The proof uses only two runner-certified properties of this finite object.
First, the 96 cell orbits partition all $192^2$ cells, so their tables sum to
the all-ones matrix $J$. Second, every $M_o$ has two ones in every row and
two in every column.

Split both rational coordinate spaces into the constant line and the
coordinate-sum-zero subspace. The sum over $S$ acts by the nonzero scalar
$2|S|$ on the constant line and by a block $A_S$ on the zero-sum
subspace. Since $J$ vanishes on the zero-sum subspace,
$A_{S^c}=-A_S$. Both $S$ and $S^c$ are nonempty, so both constant-line
blocks have rank one. The displayed ranks are therefore both
$1+\operatorname{rank}(A_S)$.

The runner separately constructs each complementary table, checks disjointness
and entrywise recombination to $J$, and computes exact rational ranks at these
representative subsets:

- the four incidence orbits and their 92-orbit complement both have rank 105;
- an incidence orbit and its 95-orbit complement both have rank 144;
- the six incidence pairs and their complements have ranks
  $72,93,117,129,144,144$.

The excluded endpoints are also checked: the empty sum has rank 0 and the full
sum $J$ has rank 1.

## Corner- and body-overlap fibres

For a cell $(C,P)$, define the corner profile

\[
A(C,P)=\operatorname{sort}\bigl(|P\cap Q|:Q\in C\bigr).
\]

The runner recomputes this profile on all 36864 cells and verifies that it is
constant on every cell orbit. Its fibres partition the 96 orbits into 25
strata: 12 strata of size 2, 7 of size 4, 4 of size 6, 1 of size 8, and 1 of
size 12. The profile contains 5 exactly on the four incidence orbits, which
form one complete stratum.

Define the body-overlap profile by

\[
B(C,P)=\operatorname{sort}\bigl(
  \#\{T:T\text{ is a cutting and }P,Q\in T\}:Q\in C
\bigr).
\]

It has 83 values on the 96 cell orbits, strictly refines the corner profile,
and contains 1975 exactly on the incidence orbits.

For every corner-profile stratum, the runner sums its orbit tables and computes
the exact rational rank. The 25 computed ranks have maximum 143; the incidence
stratum has rank 105.

## Incidence orbits inside a cover

The subgroup fixing a cover has order 2. Its nonidentity element fixes none of
the cover's eight pieces and partitions them into four partner pairs. The four
pairs belong to four distinct cell orbits, exactly the incidence orbits, and
the two pieces in every partner pair share two corners.

The exact ranks of the six sums of two incidence-orbit tables are
$72,93,117,129,144,144$. Exactly one pair attains the least observed value
72; the next value is 93.

## Evidence boundary

- The theorem is the displayed complement identity. It does not assert a
  universal rank bound for arbitrary covariant tables.
- The counts, profiles, stratum ranks, stabilizer action, partner overlaps, and
  selected exact ranks are bounded measurements of the declared finite object.
- Raw enumeration ordinals are implementation details and carry no semantic
  meaning.
- Supporting central-component and modular calculations in the runner are
  internal consistency checks; no imported census or predecessor authority is
  used.
- Nothing here is a physics claim or an audit outcome.

## Reproduction

Run
`scripts/physical_cell_cutting_complement_rank_corner_strata_2026_08_09.py`.
The canonical cache records the declared 600-second execution envelope, the
source hash, the complete deterministic stdout, and the process exit code. The
source-matched run prints `TOTAL: PASS=55 FAIL=0` in 5751 characters.
