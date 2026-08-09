# The cuttings see the pieces through an 88-dimensional shadow — Cycle 754

Date: 2026-08-09

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_2026_08_09.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the cuttings, the readings and the block bookkeeping from scratch and
gates each quantity in place. Constitutional effect: none. This package
changes no axiom, no framework Admissibility rule, no primitive, no policy,
and no audit status, and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## What this answers

The unit four-cube cuts into least-volume pieces at the adjacency cost floor
in 15800 ways, and those cuttings use 192 pieces between them, 24 to a
cutting and 1975 cuttings through each piece. Several preceding cycles ranked
and separated sixteen-piece sets by numbers built from how often pairs of
pieces share cuttings. Every one of those numbers is a function of a single
object: the vector recording, for each of the 15800 cuttings, how many of the
sixteen pieces it meets. This cycle asks what that object can and cannot
distinguish, and the answer puts a ceiling on the whole family of such
numbers.

## Two results against interest, first

**The spectral floor this cycle was opened to derive does not exist.** The
plan was to write the ranked total as a quadratic form in the indicator of a
piece-set and read a floor off the smallest eigenvalue of the incidence
table's Gram matrix. Measured exactly over the rationals, that matrix is
singular. Its rank is 88, not 192, so it is a positive semi-definite matrix
whose smallest eigenvalue is zero with multiplicity 104, and the bound the
plan would have produced returns 15800 and nothing beyond it. Nothing here
accounts for 19640.

**The rank argument for the two-cover question does not hold either.** The
statement "no sixteen pieces meet every one of the 15800 cuttings exactly
twice" would follow at once if the incidence table had full column rank,
since that equation has an evident rational solution. It does not have full
column rank, so the solution space has affine dimension 104 and the question
stays live. What this cycle supplies in its place is a sharp per-piece test,
given below.

## The shadow, and the space the cuttings cannot see

The incidence table is 15800 by 192, every column carrying 1975 ones and
every row 24. Its exact rational rank is 88. So there is a 104-dimensional
space of piece-weightings that every one of the 15800 cuttings totals to
zero. Call it the blind space; 88 and 104 together make 192.

The blind space is not an artefact of repetition. All 192 columns are
distinct, the largest number of cuttings two different pieces share is 1266
against the 1975 each of them lies on, and no two pieces and no three pieces
are linearly dependent.

A basis for the blind space is produced by exact rational elimination and
then checked against the incidence table in exact integers, all 104 vectors,
so the dimension does not rest on floating-point arithmetic. Its entries lie
in minus one, zero and one, with supports 8, 12, 14, 16, 18 and 20 occurring
38, 30, 14, 13, 3 and 6 times.

## Every blind vector is balanced, and that is derived

The 15800 rows of the table sum to 1975 times the all-ones vector, because
every column carries 1975 ones. So the all-ones vector lies in the span of
the rows, and the blind space, being the orthogonal complement of that span,
is orthogonal to it. Every blind vector therefore sums to zero. This is an
argument, not an observation; the runner gates the premise and the
conclusion separately.

A blind vector whose entries lie in minus one, zero and one is then exactly
an **exchange**: two disjoint sets of pieces, necessarily of equal size, that
every one of the 15800 cuttings meets equally often.

The same fact is what defeats the spectral plan above, and it is worth
stating in one place. Subtracting its average from the indicator of a
sixteen-piece set leaves a balanced vector, and the ranked total is 15800 plus
half the Gram form evaluated on it. A useful floor therefore needs the Gram
form to be bounded away from zero **on balanced vectors specifically**. But
the blind space is balanced, so it sits inside exactly the subspace the bound
must avoid, and the smallest value there is zero. The bound returns the floor
that was already in hand and adds nothing to it.

## The smallest exchange no cutting sees is four pieces for four

| exchange size | verdict | how it is settled |
| --- | --- | --- |
| one for one | none | all 192 columns distinct |
| two for two | none | exact determinants, and an exact sweep |
| three for three | none | exact determinants, and an exact sweep |
| four for four | **exists** | pieces 4, 5, 10, 11 against 1, 3, 7, 9 |

Two independent routes settle the negative rows, and the stronger of them is
the determinant route. For every pair and every triple of pieces the runner
forms the small Gram matrix of shared-cutting counts and evaluates its
determinant in exact integers. None vanishes. That rules out not merely an
exchange but **any** linear dependence among three or fewer columns, whatever
the coefficients, so no blind vector has support three or less.

The second route is a sifting argument. If two disjoint sets of pieces have
the same column sum, then any weighting of the cuttings gives them the same
total; weighting a cutting by its index, its square and its cube turns that
into a three-number signature a genuine exchange is obliged to share. The
runner groups all pairs and all triples by signature and reports what it
finds. **It finds no signature shared by two different sets at either size**,
so no candidate ever reached the exact confirmation step and none was run.
That makes the count of confirmations zero by absence of candidates rather
than by anything having been checked, and the note says so rather than
presenting a zero as evidence. What shows the sift is not simply letting
everything through is that the known four-for-four exchange **does** share
its signature across the two halves under the same weighting, which the
runner gates. The integer range of the weighted sums is gated as well, so the
signature is exact.

The four-for-four exchange is met equally often by every one of the 15800
cuttings, verified directly against the table rather than inferred, and its
orbit under the 384 symmetries has 96 members. Those 384 symmetries fix the
table of shared-cutting counts and carry the blind space into itself.

## The blindness is realized on the census, not only in principle

The 132 sixteen-piece carriers of the charge called four fall into six
families of sizes 12, 12, 12, 24, 24 and 48. They give only **108 distinct
multiplicity vectors**. The 24 coincidences are the substance:

- each is a pair, never a larger group
- the two members are **wholly disjoint**, symmetric difference 32
- both members lie in the same family
- the difference of their indicators lies in the blind space

So there are 24 pairs of disjoint sixteen-piece sets, both members carrying
the charge called four, that no cutting in the system tells apart. Across the
wider population the same collapse appears: the 59736 four-cube-shaped sets,
4978 through each piece, give 53632 distinct multiplicity vectors, 6104 fewer
than there are sets.

**The consequence for the preceding cycles is stated plainly.** A ranked
total or a spread built from shared-cutting counts is a function of the
multiplicity vector, so it is constant across every one of these
coincidences. What those cycles separate is classes of sets, not sets. That
ceiling covers the entire family of numbers of that kind, and it is derived
here rather than supposed.

## Over the field of two

Reducing the same table modulo two, the rank is 88 again, by rows and by
columns alike, so the piece-sets carrying no reading at all form a space of
dimension 104. The reachable readings therefore number two raised to the
rank, and each reachable reading is carried by exactly two raised to the
blind dimension piece-sets. All 8 named readings are reachable.

## The floor gains a per-piece test

The ranked total of a sixteen-piece set is bounded below by 15800, and a
preceding cycle derived that bound from a mean the system fixes in advance.
This cycle localizes the excess onto individual pieces. Write the shortfall
of a piece in a sixteen-piece set as the number of cuttings it shares with
the rest of that set, less 1975. Counting incidences two ways gives

```
sum of the per-piece shortfalls  =  2 x (ranked total - 15800)
```

so the excess above the floor is exactly half the total shortfall, and

**a sixteen-piece set attains the absolute floor if and only if every one of
its pieces shares exactly 1975 cuttings with the rest of the set.**

That is an equivalence, argued in both directions, and it is the sharp test
the failed rank route was meant to supply. Both sides are computed on all 132
carriers by two routes that do not share machinery — one from the table of
shared-cutting counts, one directly from the incidence table — and gated to
agree. No carrier passes the test, and the least ranked total among them is
19640.

## What the runner gates

45 gates, `TOTAL: PASS=45 FAIL=0`, under 300 s and under 2500 MB, output
under 6000 characters. The Gram matrix is built in exact integers and gated
against a table of shared-cutting counts computed by a different arithmetic
route. The rank comes from exact rational elimination, and the resulting
basis is confirmed against the incidence table in exact integers. The
symmetry check is gated by an explicit integer bound that keeps the
arithmetic exact. Both sweeps run over every pair and every triple; the
signature sweep additionally has its coverage gated against the binomial
counts rather than assumed, while the determinant sweep covers the full index
range by construction.

## Boundary and honest read

**Derived, and holding for every sixteen-piece set in the system:** the
balance of every blind vector; the localization identity and its
equivalence; the soundness of the signature sift; the count of piece-sets per
reachable reading.

**Measured on this object, and not claimed beyond it:** the rank 88 and the
blind dimension 104; the support histogram; the coincidence counts; the
census numbers. The rank is a measurement. Nothing here derives 88 from the
symmetries, and this note does not pretend otherwise.

**Where a gate follows from its premise, that is disclosed.** Once two
carriers are measured to have the same multiplicity vector, their agreement
on the ranked total follows by algebra; what the runner genuinely measures is
the premise and the agreement of two separately computed numbers, and the
ranked total takes only 4 distinct values across the 132 carriers, so
agreement on it is weak evidence on its own. The shortfall identity likewise
follows from the symmetry of the shared-cutting table; what discriminates
there is the agreement of the two routes.

**What the minimality claim does and does not cover.** Settled with
certainty: no linear dependence among three or fewer columns, for any
coefficients; and no two-for-two and no three-for-three exchange. A general
integer relation on four or more columns with coefficients outside minus one,
zero and one was not swept.

**Standing negatives, repeated unchanged.** The floor derived in the
preceding cycle is still not shown to be attained; 19640 is still not shown
to be forced; and within this population carrying a reading and carrying the
charge called four coincide, so nothing here tells that charge from a
different reading.
