# Covariance Under The Cell's Symmetry Does Not Determine The Cover Table's Dimension

Date: 2026-08-09

Authority: none

Status: proposed_retained

Claim type: no_go

Runner:

- [self-contained rebuild-and-gate runner](../scripts/physical_cell_cutting_symmetry_underdetermines_cycle763_2026_08_09.py)

## Trace gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "test what the finite four-cube coordinate-relabeling symmetry fixes about the cutting and cover incidence spaces"
source_of_blocker_text: frontier_question
reachability_to_target: none
artifact_role: runner_certificate
next_trace_action: "identify an additional retained structure, if any, that selects the measured cover-table row space inside the covariant family"
```

## Status fields

```yaml
actual_current_surface_status: no-go
target_claim_type: no_go
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "finite counterexamples and a sampled rank census are offered to delimit what the explicitly rebuilt coordinate-relabeling symmetry fixes"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What this is

The object is one cell, taken as the unit four-cube on its sixteen corners. A piece
is a five-corner sub-simplex whose four edge vectors from its first corner have
determinant of absolute value 1; among those, the pieces at the adjacency cost
floor are kept. A cutting is a set of kept pieces with pairwise disjoint interiors
that together fill the cell. A cover is an eight-piece set no two of whose pieces
ever share a cutting, and gate G1 re-certifies that each such set meets every
cutting exactly once. The cutting table records which piece belongs to which
cutting; the cover table records which piece belongs to which cover.

The preceding cycle of this lane ended on a stated boundary. Its two dimensions,
88 for the cutting table and 105 for the cover table, were **measured, not derived**:
nothing in that cycle predicted either number from the shape of the four-cube. This
cycle asks the next question. The cell has a symmetry group, and the admissibility
axiom asks a local rule to be covariant. Does covariance under the cell's own
symmetry deliver the two dimensions?

The measured answer is no, and this note makes the no quantitative in four steps.
Covariance fixes the entire shape of the split of both row spaces by a stabiliser,
leaving exactly one integer free, and that integer stays measured. It forces every
one of the 96 elementary symmetric tables to dimension 144, for a reason that can
be given by hand and is checked against a bound derived from three counts alone.
But the cover table is one particular sum of 4 of those 96, and the tables of its
exact shape that the symmetry permits run in dimension from 57 up to 144, with the
cover table's own 105 far down in the low tail: 42 of 1500 sampled tables lie at or
below it.

Two exact numerical agreements between symmetry counts and the two dimensions turn
up on the way, and both are measured here to be agreements of counting rather than
of structure. Recording that demotion is part of the result, not an aside.

## The object

The runner builds the cell from scratch and re-measures every input number rather
than citing it. Of the five-corner sub-simplices of the four-cube, 2672 have
determinant of absolute value 1; the adjacency cost floor among them is 6, attained
by 400 of them. Cuttings are found as exact covers of 625 sample points chosen so
that no sample point lies on a facet plane of any kept piece, which gate G0 checks
directly; genericity is what makes the sample search complete, and gate G1
certifies the other direction, that what the search returns really is a tiling.
There are 15800 cuttings, each of 24 pieces of volume 1 over 24, with all 15168
co-occurring piece pairs certified interior-disjoint exactly, 13632 of them by a
separating facet plane. Exactly 192 of the 400 floor pieces occur in a cutting at
all, and there are 192 covers. Gate G8 re-measures the two tables: rank 88 with
kernel 104 for the cutting table, rank 105 with kernel 87 for the cover table.

## The symmetry

Gate G4 builds 384 distinct maps of the cell by permuting the four coordinates and
flipping any of them, and checks closure over all 147456 products. Gate G6 measures
one orbit on the 192 pieces, so the group is transitive there, and gate G26
measures the same for the 192 covers. Gate G5 measures that every one of the 384
carries the sorted cutting table and the sorted cover table to themselves, so both
row spaces stand under the whole group. This is the strongest symmetry statement
the object supports, and everything negative below is therefore a negative for
every subgroup as well: gate G30 exhibits four subgroups of order 24 built from
proper rotations, each of which breaks the 192 pieces into 8 orbits instead of one
and gives 1536 orbits on ordered pairs, far above the full group's 104, and a
group with more orbits constrains less.

Three counts organise the rest. Gate G6 measures fixed-piece counts
[(0, 371), (16, 12), (192, 1)], whose squares sum to 384 times 104, giving 104
orbits on ordered pairs of pieces; gate G7 confirms that count independently by
union-find over all 36864 ordered pairs. Gate G27 measures fixed-cover counts
[(0, 379), (48, 4), (192, 1)], whose squares sum to 384 times 120, giving 120
orbits on ordered pairs of covers. Gate G33 pairs the two counts against each
other and obtains 96 orbits on cover-piece cells. The three numbers 104, 120 and 96
are the whole input to what follows.

That the piece count and the cover count differ is itself a result, and gate G29
states it as a test rather than a caveat: the two fixed-point counts do not agree
element by element, and equal counts would force equal orbit counts, which is
impossible here because 104 is not 120. The two sides of the object are not
symmetric copies of each other.

## What covariance does fix: the split by a stabiliser

Gate G20 measures that the stabiliser of a piece has order 2, with orbit sizes
[(1, 16), (2, 88)]: sixteen fixed pieces and eighty-eight transposed pairs. Its
non-identity element therefore has a plus space of dimension 104 and a minus space
of dimension 88, and gate G21 obtains both by two independent exact ranks summing
to 192. Those two numbers come off the cycle structure of the element and are not
measured against anything else.

That element is a symmetry of both tables, so it preserves both row spaces and each
one splits. Gate G22 measures the splits: the cutting row space splits 50 plus 38,
the cover row space 55 plus 50, against the ranks 88 and 105.

Given the preceding cycle, those four numbers are not four independent quantities.
That cycle established that the two row spaces together span all 192 dimensions and
meet exactly in the constants, and gate G10 re-measures both facts here rather than
citing them. Applying the projector onto either eigenspace to a
decomposition of a vector into a cutting-side part and a cover-side part keeps each
part inside its own row space, because the element preserves both; so the two plus
parts already span the plus space and the two minus parts span the minus space. The
intersection splits along with everything else, and the constants sit on the plus
side. Hence the two plus parts must add to 104 plus one and the two minus parts to
88, which is exactly what gate G23 measures: 50 plus 55 is 105, and 38 plus 50 is
88. Both identities are obtained by addition of separately measured dimensions,
never by subtracting one from a total.

Combine that with the two ranks and one more equality falls out: the cutting side's
plus part and the cover side's minus part must be equal, and both are 50. Every one
of the four dimensions is then a function of that single number. **Covariance fixes
the shape of the split completely and leaves exactly one integer free, and this
note measures that integer rather than deriving it.** Gate G24 measures that all 12
order-two elements fixing a piece give the same six dimensions
[104, 88, 50, 38, 55, 50], each by its own exact rank, so the split belongs to the
conjugacy class and not to a chosen element.

## The two agreements, and why they are demoted

104 is the plus dimension and it is also the cutting table's kernel dimension. 88 is
the minus dimension and it is also the cutting table's rank. Both agreements are
exact. Neither is a derivation, and the runner says so in its own output rather than
in prose: after gate G21 it prints that 104 matches the cutting kernel and 88
matches the rank, and that neither is derived.

Gate G25 demotes the second agreement by measurement rather than by assertion. If
the minus space were the cutting table's row space wearing another name, the two
would coincide. They do not: the cutting rows meet the minus part in dimension 38,
not 88, and they do not lie inside the 89-dimensional span of the minus part
together with the constants. The equality of two numbers is not an equality of two
spaces here, and the note claims nothing from it.

Gate G31 carries the same warning for the first agreement: the pair-orbit count and
the cutting kernel are both 104 by unrelated routes, and that is recorded as an
agreement, not offered as evidence. The gate says so in its own text and is
non-discriminating by construction.

Two further gates measure how far the symmetry is from determining the tables at
all. The 104 pair-orbits give a 104-dimensional space of matrices commuting with
the whole group, which gate G11 certifies by measuring that the orbit labels cut all
36864 entries into classes of sizes from 192 to 384. Of those 104 commuting
matrices, gate G12 measures that only 2 carry the cutting row space into itself, and
gate G13 measures that only 2 carry the cover row space into itself. The row spaces
are very far from being closed under everything the symmetry allows.

## Every elementary table has dimension 144, and that one is derived

Gate G38 measures that all 96 cover-piece orbits have size 384, the full order of
the group, summing to 36864 cells; the group acts freely on the cells of any one
orbit. A cover therefore lies in 384 over 192, that is 2, of the cells of a given
orbit, and so does a piece. Read as a bipartite graph on covers and pieces, one
orbit is 2-regular: a disjoint union of cycles. A cycle visiting k covers and k
pieces contributes a k-by-k table with two cyclically placed ones in every row and
column, whose determinant is 1 plus minus-one to the power k plus one; so such a
cycle contributes one less than its length when the length is even, and its full
length when the length is odd.

Gate G36 measures the cycle structure of all 96 orbits and finds a single type: 48
cycles of length 4 covering all 192 covers, in every orbit. The rule above then
predicts one dimension for every orbit, and 0 of the 96 orbits differ from the
prediction. Gate G34 measures the dimensions directly and finds the single value
144 with count 96. This number is derived, not measured: the cycle rule fixes it,
and the direct measurement agrees.

Gate G37 checks the largest of them against a bound obtained from the three orbit
counts alone, with no reference to either table. Both sides break into the same
list of parts, the covers appearing with one multiplicity in each part and the
pieces with another; the sum of the squares of the differences of those two
multiplicities is 104 plus 120 less twice 96, which is 32. Multiplied by the group
order that is 12288, and the sum of the absolute differences weighted by the part
dimensions is at most the integer square root of that, by the inequality between a
sum of products and the two lengths. That weighted sum splits into a positive and a
negative half which are equal, because the signed version is the difference of the
two totals 192 and 192 and so vanishes; the positive half is therefore at most half
the integer square root, that is 55. A symmetric table can reach, in each part, only
the smaller of the two multiplicities, so the greatest dimension available to any
symmetric table at all is the total 192 less exactly that positive half: at least
192 less 55, that is 137. The measured largest, 144, clears the bound. Everything
here is integer arithmetic; the square root enters only through an integer
certificate, which gate G37 checks rather than trusting a floating value.

## Where the cover table's own dimension is not fixed

A table carrying entries zero and one that is constant on the 96 cell orbits is a
union of whole orbits, and gate G39 measures that each orbit puts exactly 2 ones in
every cover row. A table of the cover table's shape, meaning entries zero and one,
constant on the orbits, and every one of its 192 rows summing to 8, is therefore a
union of exactly 4 of them; gate G39 identifies the 4 that rebuild the cover table.
This is the decisive structural statement of the cycle: **the symmetric tables of
the cover table's shape are precisely the 4-element subsets of the 96 orbits, and
the cover table is one of them.**

Gate G40 then measures what those 4 do. Each one alone has dimension 144, the
largest among the 96. Added one at a time the running dimensions are
[144, 93, 114, 105], ending at the cover rank 105 as they must. Adding symmetric
structure lowers the dimension by 39 from where a single orbit sits, and gate G35
records the bookkeeping that goes with a single orbit: 192 less that dimension plus
one is 49, not 105.

Gate G41 samples 1500 of the 4-element subsets. The dimensions run from a least of
57 through a middle value of 135 to a greatest of 144, and 42 of the 1500 lie at or
below the cover table's 105. The symmetry permits tables of exactly the cover
table's shape with dimensions spread over most of the available range, and the real
one sits low among them. Covariance under the cell's full symmetry does not deliver
105; it does not even make 105 a typical value.

## The axiom contact

The admissibility axiom in [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md)
says, verbatim:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

Covariance is the whole of what that clause supplies about symmetry, and this note
takes it in its strongest available form: not the proper rotations alone, but the
cell's full symmetry, which contains them. Gate G30 measures that the proper
rotation subgroups available here have order 24 and give 1536 orbits on ordered
pairs against the full group's 104, so they constrain strictly less.

Under that strongest reading, covariance is measured here to fix the shape of the
split by a stabiliser down to one free integer, and to fix the dimension of every
elementary symmetric table exactly; and it is measured not to fix the dimension of
the cover table, which is one choice of 4 elementary tables among many that
covariance permits equally. Whatever supplies 105 is therefore not covariance, and
this note names that as the input still to be found rather than treating the
agreement of counts as if it supplied it.

The identification of a piece as an object to which the axioms speak is open, is
inherited unchanged from the preceding cycle, and is not derived here. All claims
below the axiom contact are **computational identities** about this one cell and do
not depend on that identification.

## Controls

Gate G14 measures that the constants times each of the 104 commuting matrices stays
a multiple of the constants, so gates G12 and G13 are reporting content rather than
a construction that could not have come out otherwise. Gate G15 measures that a
cyclic shift of the 192 pieces is not one of the 384 and does not keep the cutting
table, so the group is not accidentally everything. Gate G16 measures that the first
commuting matrix failing G12 has, together with the identity, rank 192, and that its
88 moved rows have rank 88 and all lie outside. Gate G17 measures that two named
elements generate all 384 and that the moved span keeps rank 88 when stacked with
its image under each. Gate G28 measures the cover stabiliser, of order 2 with orbit
sizes [(1, 48), (2, 72)], and that it fixes 0 pieces, so the two stabilisers act
differently.

Gate G18 is non-discriminating by construction and says so in its own text: it
checks a property that holds because the orbits were built to have it. Gate G31
could fail, and does not, but what it certifies is an agreement of two counts
reached by unrelated routes, which its own text records as an agreement rather
than as evidence.

The dimensions in gates G34, G36, G40 and G41 are counted modulo a single prime.
Three controls bound what that can cost. D8 measures that the identity table of size
192 returns dimension 192 over the integers. D9 measures that the cover table
stacked on itself gives 105, as does the cover table alone, so stacking a repeat
adds nothing. D10 computes the cover table's dimension exactly over the integers,
with no modulus at all, obtains 105, and confirms it agrees with the modular count.
A modular count can only fall short of the exact one, never exceed it, so the
sampled tail count of 42 is an upper bound on the true tail and the least value 57
is a lower bound on the true least: both errors would run in the direction that
weakens the negative, not in the direction that manufactures it.

## Measured totals

The runner has 47 gates and prints `TOTAL: PASS=47 FAIL=0`, exiting 0. Elapsed time
is under 600 seconds and peak resident memory is under 2500 MB; gate G43 reports
both as bounds rather than as timings, so the output carries no machine-dependent
number. Total stdout is 5652 characters. The only randomness is the fixed-seed draw
of the 1500 sampled subsets in gate G41, and two runs give byte-identical output.
All ranks and kernels of the two tables, and both eigenspace splits, are computed
exactly over the rationals.

## Boundary

- Nothing here derives 105, and nothing here derives 88. They remain **measured, not
  derived**. What this cycle adds is a measurement of how far the cell's symmetry is
  from supplying them, and the answer is that it is far.
- The single free integer in the stabiliser split, 50, is measured. The note derives
  that every other dimension in the split follows from it, and does not derive it.
- The two numerical agreements, 104 with the cutting kernel and 88 with the cutting
  rank, are recorded and demoted. Gate G25 measures the overlap at 38 rather than
  88. No claim in this note rests on either agreement.
- Gate G39's statement that the symmetric tables of the cover table's shape are
  exactly the 4-element subsets of the 96 orbits uses the row sum 8 and the fact
  that each orbit contributes 2 per row. It says nothing about tables of other
  shapes, and nothing about tables that are symmetric under a proper subgroup only.
- The dimensions in gates G34, G36, G40 and G41 are modular. Gate D10 gives the one
  number the argument leans on, the cover table's 105, exactly over the integers;
  the others are lower bounds on their exact values, which is the safe direction for
  every negative stated here.
- The 1500 subsets in gate G41 are a sample, not a census. The least, middle and
  greatest values and the tail count are properties of that fixed-seed sample. The
  spread they exhibit is what the negative rests on, and a wider spread in the full
  set would only widen it.
- This is one cell. Nothing here says how cells join to each other, and the spatial
  question and the whole-number bookkeeping of this lane remain different questions.
- The group used is the cell's own full symmetry. The axiom names proper cubic
  rotations, which sit inside it as subgroups of order 24; gate G30 measures that
  those constrain strictly less. The note therefore states its negative for the
  larger group, where it is strongest, and inherits it for the smaller ones.
