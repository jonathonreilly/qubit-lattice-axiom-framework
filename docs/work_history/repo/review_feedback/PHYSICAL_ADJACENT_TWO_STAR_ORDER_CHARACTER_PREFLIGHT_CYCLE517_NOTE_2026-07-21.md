# Physical adjacent-two-star order-character preflight — Cycle 517 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

## Result

Cycle 517 gives a bounded constructive preflight for two adjacent Cycle-330
stars.  On twelve physical M2 cells, with six logical modes per cell and
global total number (N=0,1,2), the logical dimension is

\[
1+72+\binom{72}{2}=2629.
\]

The two stars have eleven unique update seams: their common center seam, five
other seams incident on the left center, and five incident on the right
center.  The induced physical Pauli anticommutation graph has fifteen edges,
not eleven, because four transverse nearest-neighbor rungs also carry
anticommutation.  The runner exhausts all 66 unordered cell pairs and all
3,964 allowed local gauge-term pairs at train (L=5) and held (L=6):
261,624 exact commutation tests per size.  Precisely the same fifteen pairs are
active at both sizes.  Every active edge has exactly 200 anticommuting cases,
all in the split (n_i=n_j=1) sector; all 51 nonedges have zero.

This graph has one center edge, two axial leaves, and four four-cycle pages
sharing the center edge.  Its chromatic polynomial is independently recovered
by the (2^{15})-term spanning-subgraph expansion and by the page
factorization

\[
P(q)=q(q-1)^3(q^2-3q+3)^4.
\]

Therefore (P(-1)=19,208).  Direct enumeration of all 32,768 edge
orientations finds exactly 19,208 acyclic orientations and reconstructs every
one from a canonical topological order.  These are exactly the equivalence
classes of total factor orders that agree on every possible static Pauli
order character.  The physical search derives a full twelve-factor branch
with singleton anticommutation mask for every one of the fifteen edges.  The
same structural witnesses pass at L5, held L6, and after direct reconstruction
in all 24 proper-cubic frames.  Hence all fifteen character bits are
independently distinguishable on the declared physical domain.

Within this precise static-character architecture, the quotient is exact and
minimal: it has 19,208 classes, so fourteen M2 role bits are short by 2,824
states and 15 M2 bits suffice.  The direct fifteen-bit orientation address has
13,560 cyclic words that are not lawful quotient states.  Their exclusion,
initialization, and local enforcement are supplied structure, not a derived
constraint mechanism.

This is not the requested adjacent-star compiler.  In particular,

\[
E\,G_{\rm coarse}=G_{\rm physical}\,E
\]

remains open.  Encoding injectivity and isometry, the free-plus-contact
update, the one-particle mass fixture on this widened cell, primitive
application, constraint enforcement, and recurrent overlap consistency were
not proved.  The fifteen graph edges are not fifteen dynamic seams; the
coarse two-star update still has eleven unique seams.

## Static quotient versus a schedule

The quotient does not inherit a uniform measure from the 12! order labels.
For an acyclic orientation (O), let (L(O)) be its number of linear
extensions.  Exact dynamic programming over all orientation words gives 375
distinct nonzero fiber sizes, from 54 through 2,727,432, with histogram digest
`fa2bf7a73849928daad03cbb74182ba46b7f8c06dd1c6449a99bc37ebe7ca379`.
Their multiplicity-weighted sum is (12!=479,001,600).  An isometric
compression of the uniform order state therefore has quotient amplitude

\[
\sqrt{L(O)/12!},
\]

not a uniform amplitude over the 19,208 orientations.

A fixed adjacent-position transposition also fails to descend to a
deterministic action on this quotient.  In the runner's physical cell order,

```
o1 = (0,2,7,8,3,9,4,10,5,11,1,6)
o2 = (0,2,7,8,9,3,4,10,5,11,1,6)
```

have the same input orientation word, 63.  Swapping zero-based slots 3 and 4
crosses the active rung `(3,8)` in `o1`, producing word 2111, but crosses the
nonedge `(8,9)` in `o2`, leaving word 63.  A second deletion fixture has
27,720 linear extensions in its canonical orientation, 2,520 after an axial
leaf flip, and zero after the center-edge flip.  Thus quotient schedule
weights and even lawfulness depend on the orientation.  This falsifies only
the naive fixed-position schedule on the bare static quotient.  It does not
falsify a factor-labelled local swap, an augmented quotient carrying fiber
data, a gauge construction, or a time-multiplexed implementation.

## Proper-cubic and lawful-domain controls

The geometric action closes for all (24^2=576) frame products.  At both L5
and L6 every transformed patch has the same abstract fifteen-edge graph, and
all 15 singleton physical witnesses are reconstructed and retested in every
frame.  This is covariance of the bounded preflight data, not a proof of a
covariant update.

One directed adjacent-center bond has proper-cubic stabilizer four and a
six-direction orbit.  An unordered bond has stabilizer eight and a
three-axis orbit.  Consequently one fixed placement does not itself carry a
full 24-frame physical law; a covariant construction must include the full
six-direction directed orbit (or an explicitly equivalent relational
encoding).

The lawful domain requires adjacent, distinct centers, proper determinant-one
cubic frames, (L\geq5), and global (N\leq2).  L4 is rejected: periodicity
adds a sixteenth wrap edge between the two axial leaves.  Duplicate centers,
nonadjacent centers, and determinant-minus-one frames are rejected.  Every
one-edge graph deletion changes the exact chromatic polynomial.  For every
character bit, the runner exhibits two lawful acyclic words that differ only
on that bit and would collide if it were deleted.  These are deletion tests,
not claims that the corresponding physical constraints have been synthesized.

## Resource and support discipline

The exact twelve-cell branch inventory is

| sector | structural branches |
|---|---:|
| (N=0) | 4,096 |
| (N=1) | 1,474,560 |
| (N=2), same cell | 737,280 |
| (N=2), split cells | 243,302,400 |
| total | 245,518,336 |

The full branch census was not run.  It is unnecessary for this graph gate:
the exhaustive pair census proves that every lawful full branch has support
only on the fifteen graph edges, while the fifteen explicit full-branch unit
masks prove character separation.  No numerical amplitude, machine-zero
query, tolerance, or magnitude cutoff selects support.  The target runner has
a 1,200-second hard wall, a 3 GB checkpoint abort ceiling, a 2.85 GB guard,
and zero-swap checkpoints.  Caught failures preserve the final exception but
partial rows are not durable across an OS kill or process OOM.

The final target run passed all seven top-level gates in 44.705 seconds with
maximum RSS 105,283,584 bytes and process swap count zero.  L5 and L6 each
executed 261,624 pair tests, found 3,000 anticommuting term pairs, and produced
the same canonical pair-summary digest
`e38941f1753d51a72c43c3f62091c71b802060b08adbdf62a40c32997c420157`.
The fifteen CSP-derived witness signatures have digest
`6e83bc192e672215f921832677bb3a2bc857a82c912b2c58b45f1ef06b299186`;
all 720 size/frame/edge witness tests passed.

## Supplied and open structure

The physical inputs are the pinned Cycle-311/315 local gauge-term grammar and
the Cycle-516 proper-cubic affine Clifford action.  Cycle 516 explicitly left
adjacent stars open.  Cycle 517 supplies only the bounded static orientation
address, the rule excluding its 13,560 cyclic words, and the assumption that
this address can be initialized and enforced.  It imports no Cycle-514
mediator, response law, beta, or source fixture.

Still open are:

- an injective and isometric twelve-cell encoding;
- locally generated constraints selecting exactly the 19,208 lawful role
  states and making overlapping patches agree;
- a schedule or autonomous update that acts well on the selected quotient;
- the physical free-plus-contact update and the exact intertwiner;
- explicit preservation of the Cycle-219 one-particle mass fixture;
- primitive synthesis, larger number sectors, recurrent volume, physical
  time, Record formation, source/gravity response, and Born/probability.

The strongest justified statement is therefore: the adjacent-two-star
physical gauge terms have an exact, proper-frame-covariant fifteen-edge static
order-character preflight with an exact 19,208-state quotient and physical
unit-mask witnesses.  E G_coarse = G_physical E remains open.  There is no
obstruction and no axiom pressure.

## Proof-search governance

The target statement is a bounded static-character classification, not a
compiler theorem.  Its evidence tier is executable exact preflight with
authority none and audit unset.  The dependency graph is explicit:
Cycle-311/315 gauge terms feed the pair census; the pair census and singleton
masks feed character separation; the independently computed graph polynomial
and orientation enumeration feed the quotient count; Cycle 516 feeds only the
proper-frame physical reconstruction.  The lower bound is 19,208 distinct
static character classes, while the matching upper construction is their
fifteen-bit acyclic-orientation address.  That upper construction is logical:
physical synthesis of its constraints is not claimed.

The admitted-route ledger is deliberately incomplete for broader purposes.
Only the direct static route is classified.  Full S12 storage, augmented
fiber roles, factor-labelled dynamics, local gauge/auxiliary encodings, and
time-multiplexed schedules remain admissible.  The exact verifier covers all
graph subsets, all orientation words, every local pair term at L5/L6, and the
derived unit witnesses in all proper frames.  It does not cover all
245,518,336 full branches, a twelve-cell Gram, overlap tilings, or primitive
updates.  Thus the verifier is complete for the stated graph and static
quotient gates and incomplete for every compiler or no-go statement.

## N1–N8 no-go discipline

### N1 — alternative-route map

The viable routes are: retain the full S12 order role; use the 19,208-state
static orientation quotient; augment that quotient by linear-extension or
schedule residual data; use factor-labelled local swaps; replace explicit
order data by a local gauge/auxiliary encoding; or use a staggered or
time-multiplexed schedule.  This cycle constructs and audits only the static
orientation route.

### N2 — wall-independence audit

The 19,208 lower bound uses two assumptions jointly: the role is a static
exact order-character label, and the fifteen physical singleton masks remain
lawful witnesses.  The fixed-position non-descent result adds the assumption
that the same position generator must act deterministically on quotient
classes.  Neither result constrains gauge redundancy, relational placement,
factor-labelled swaps, or time-multiplexed state.

### N3 — hidden-wall scan

Unclosed walls include cyclic-word exclusion, local constraint generation,
role initialization, overlap agreement, placement over the six directed bond
orientations, fiber-dependent amplitudes, schedule memory, physical primitive
application, and the widened encoding Gram.  None is silently charged to the
M2 substrate.

### N4 — residual matching

The exact positive residuals are the 15-edge pair support, 200 active cases
per edge, zero nonedge cases, the chromatic coefficients, 19,208 acyclic
words, fifteen singleton physical masks, held-L6 equality, and all-frame
witness transport.  The exact negative residual is only the unequal targets
of the same-fiber fixed-position swap.  It is matched to that schedule and no
broader claim.

### N5 — rhetoric audit

“Minimal” means minimal number of classes and M2 address bits for an exact
static order-character quotient on this declared twelve-cell graph.  It does
not mean a minimum physical compiler, minimum gauge content, minimum dynamic
memory, or a constitutional lower bound.

### N6 — partial-closure path

The constructive closure path is to synthesize the cyclic-word and overlap
constraints, choose either a quotient-compatible factor-labelled schedule or
an augmented role, prove the twelve-cell encoding Gram exactly, and only then
lift the free-plus-contact update and retest the mass fixture.

### N7 — hostile steelman

A strong opposing construction can encode orientation relationally in local
gauge constraints, reuse a small role through a covariant multi-step schedule,
or keep enough fiber data to make swaps deterministic.  The singleton masks
help such constructions by exposing the exact character generators; they do
not rule them out.  A reviewer should reject any compiler no-go inferred from
the fixed-position counterexample.

### N8 — cross-cycle echo

Cycle 515 removed the sampled-order wall by proving all S7 order isometries,
and Cycle 516 removed the bare-frame sign wall with a Koszul correction.
Cycle 517 similarly converts adjacent-star order bookkeeping into a smaller
exact static object, but finds that one naive schedule does not survive the
compression.  The repeated lesson is constructive: add the missing bounded
role or correction and retest.  No route-independent failure has survived,
so no obstruction and no axiom pressure may be shipped.

## Optimal next attack

Build the local gauge/auxiliary realization of the fifteen-bit acyclic
orientation address across overlapping adjacent-star patches.  The gate must
derive local invalid-word and overlap constraints, include all six directed
center-bond placements, give a quotient-compatible schedule (or prove the
needed augmentation), and establish an exact L5/L6 twelve-cell Gram before
any (G_{\rm physical}) or compiler claim.
