# Physical cell cutting: the covers and the pieces are inequivalent group sets, and the two censuses cross in the centre

Date: 2026-08-11
Authority: none
Audit: unset.
Claim type: bounded_theorem
Constitutional effect: none.

## 1. What this cycle asks

The unit four-cube cell has 2672 five-corner unit-determinant subsets, 400 of them at the
adjacency cost floor 6, and 15800 cuttings of 24 pieces, in which 192 pieces occur, each in
1975 cuttings, filling 379200 slots. Those pieces carry 192 eight-piece covers. The 384 signed
coordinate maps act freely on the 36864 pairs of a piece and a cover with 96 orbit tables; the
tables are pairwise disjoint and sum to the all-ones table, so any four of them add to a
zero-one matrix and the family of such members has 3321960 elements. The cover incidence is one
of them.

Cycle 776 cut that family by asking that every row of a member be a cover, and 48 members
survived. This cycle asks the mirror question on the columns: that every column of a member be
a column of the incidence, that is the set of covers through some one piece. The two brute
force censuses give 48 and 16. This note says where both numbers come from, and what happens
when the two conditions are imposed together.

## 2. The fixed-point formula

**Theorem.** Let a group act transitively on a set, and suppose the holder of each point has
order 2. Let g be the second map of one such holder. Then the number of relabellings of the set
that commute with the action equals the number of points that g leaves alone.

The double count is two lines. Every point has exactly one non-identity map holding it, and by
transitivity all of those maps are conjugate, so the conjugacy class of g meets every holder
exactly once per point it leaves alone: counting the pairs of a point and a map of the class
holding it gives class size times fixed count equals the number of points. The relabellings
commuting with the action are the index of the holder inside its normalizer, and since the
holder has order 2 the normalizer is the centralizer of g, so that index is the group order
divided by the class size and then by 2. Because the point holders have order 2 the number of
points is the group order divided by 2, and the two divisions cancel: the index is the fixed
count.

The two instances of the cell, each with its class equation:

- covers: class size 4 times fixed count 48 is 192; centralizer 96, equal to the normalizer;
  index 96 over 2 is 48, which is the fixed count.
- pieces: class size 12 times fixed count 16 is 192; centralizer 32, equal to the normalizer;
  index 32 over 2 is 16, which is the fixed count.

## 3. The covers and the pieces are inequivalent group sets

The two holder generators are different maps and are not conjugate. The cover holder generator
is a single-axis flip and lies in the flip group of 16 maps that the cover holders generate;
the piece holder generator is not a flip and lies outside that group. Each acts without a fixed
point on the other side: the cover holder leaves 0 pieces alone and the piece holder leaves 0
covers alone.

By the theorem of section 2 the two counts 48 and 16 are the two fixed counts, so 48 against 16
is exactly the statement that the 192 covers and the 192 pieces are inequivalent as group sets.
That inequivalence is what makes the object rigid: no relabelling can carry the one side onto
the other, and the two censuses therefore cannot be transported into each other.

## 4. The column census

The centralizer of the piece holder generator has 32 maps and yields 16 piece relabellings,
each a bijection of the 192 pieces commuting with the group action, checked on 1179648
comparisons with 0 misses, closed under composition and containing the identity. The images of
the incidence under those 16 relabellings are 16 four-table sets, and they are set-equal to the
16 members of the brute force column census, with symmetric difference 0. So the column count
16 is the index of section 2, not an accident of the search.

## 5. The crossing is an automorphism count

A member lying in both censuses is a relabelling of the rows and a relabelling of the columns
of the incidence at once, so the pair intertwines the incidence with itself; both components
already commute with the group. Counting directly over the 48 cover relabellings and the 16
piece relabellings gives 768 candidate pairs, of which 2 satisfy the intertwining relation.
Reading the four table labels off those 2 returns exactly the two members that the brute force
crossing found, with symmetric difference 0.

This count never mentions the family, the censuses, or the orbit tables: it is a count of pairs
of relabellings. Both components of both solutions are maps of the cell and both lie in the
centre, which has size 2, and the two cover components are closed under composition and contain
the identity.

## 6. The two purely combinatorial conditions reach the centre with no symmetry input

The row condition alone leaves 48 members and the column condition alone leaves 16; 46 members
satisfy the row condition and not the column condition, and 14 the other way, so neither
condition implies the other. Together they leave 2, and the incidence has 192 distinct rows and
192 distinct columns, so a member's row map and column map are each determined. The ladder is
3321960, then 48, then 16, then 2.

Neither step asks for a symmetry. Both are conditions on how the labels of a four-table member
fall inside the covers, and the maps of the cell only enter afterwards, when section 2 explains
the two numbers. Cycle 776's symmetry step is therefore a consequence of the combinatorics
rather than an extra requirement laid on top of it.

## 7. What rank cannot do

The incidence has block profile 9/9/6/6/0 over the sixteen sign patterns, constant inside each
pattern weight class, and every one of the 16 column-census members carries that same profile
triple at both fixed primes: 16 of 16 at the first and 16 of 16 at the second. So no rank
instrument built from the sixteen blocks separates the column census, exactly as none separates
the row census.

The instrument is nonetheless sound: at both primes the sixteen block ranks recompose to 105,
which is the rank of the incidence measured directly, so a wrong block basis would show up here
rather than hide.

## 8. Rejectors

- The cycle 773 twin, the four-table set 4/5/6/7, sits in neither census; both the row census of
  48 and the column census of 16 were tested.
- Precomposing the piece side with the central map sends each of the incidence's four tables to
  a partner table. Of the 16 variants obtained by swapping each subset of the four, 2 sit in the
  row census and 2 sit in the column census.
- Of the 352 maps outside the centralizer of the piece holder generator, 0 give the same piece
  map from two different coset representatives, so the 16 relabellings of section 4 are not an
  artefact of the choice of representatives.

## 9. Boundary and honest auditor read

The 2 members of the crossing are one object under two namings: the central map carries the
first to the second entry by entry, and it also carries the four tables of the first onto the
four tables of the second. So no instrument blind to the naming of the covers can separate
them, and cutting below 2 needs an instrument that is sensitive to that naming. This cycle does
not supply one. Neither census condition is linear either: two members sum to row sums 16 rather
than 8, so the sum leaves the family altogether, and both members have the same rank 105 as the
incidence.

The flip group of section 3 must be identified from the cover holders, by taking the
non-identity map of each cover holder and closing under the product. Identifying it by free
action does not work: the maps leaving no piece alone number 371, and imposing in addition that
the map square to the identity leaves 63, and neither of those is 16. Both wrong numbers are
measured, not derived. The nearest repair fails as well: the identity leaves every piece alone,
so it sits outside the 63, and adjoining it gives 64 maps that are not closed under the product,
so that set is not a subgroup at all.

The gate results are computational identities on one exact object, over the integers and two
fixed primes, with no floating point anywhere and no free parameter.

## 10. Reproduction

Runner `physical_cell_cutting_crossing_automorphism_cycle777_2026_08_11.py`, cached output
`physical_cell_cutting_crossing_automorphism_cycle777_2026_08_11.txt`. The runner is standalone
and rebuilds the cell object from the corners; it takes under a minute and stays well under a
gigabyte.
