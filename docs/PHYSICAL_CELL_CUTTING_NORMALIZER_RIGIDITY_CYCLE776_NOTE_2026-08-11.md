# Physical cell cutting: the cover incidence is forced by the symmetry group, up to the centre (cycle 776)

Date: 2026-08-11
Authority: none
Audit: unset.
Claim type: bounded_theorem
Constitutional effect: none.

**One combinatorial condition collapses the family from 3321960 to 48, and the 48 is a group index.** Cycles 771 to 775 found the cover incidence sitting inside a family of 3321960 four-table sums that no linear instrument separates: the family shares its rank, its kernel, its regularity, its block-rank profile, and after the finest label of `cycle 775` there were still 30720 candidates. This cycle imposes instead a condition that is part of the object's own definition — every row of the member must be a cover of the cell, not merely some 8-element set of pieces — and 48 members survive. That 48 is not a measurement. A family member is a union of orbits of the diagonal action, so if its rows are the covers under a bijection then that bijection commutes with the whole group; the group is transitive on the 192 covers with a point stabiliser of order 2, so the commuting bijections are the right multiplications by the normalizer of that stabiliser, and there are exactly as many as the index 96 over 2.

**A second condition reaches 2, and 2 is the order of the centre.** A commuting bijection is realized by an actual symmetry of the cell exactly when it is a left multiplication as well as a right one, which is the centre. The centre of this group has order 2: the identity and the all-axes sign flip. The two survivors are the cover incidence and the cover incidence with its covers relabelled by that flip, so they differ by a renaming and by nothing else.

**The two counts of 48 are the same 48.** The group-theoretic construction and an independent brute-force census over the family produce sets that are equal element by element, not merely equinumerous.

## 1. What is measured

The object is the unit four-cube cell and the ways of cutting it. Its 16 corners carry 2672 five-corner subsets of unit determinant; 400 of those sit at the adjacency cost floor 6; the 400 pieces admit 15800 cuttings of the cell into 24 pieces; 192 distinct pieces occur, each in exactly 1975 cuttings, filling 379200 slots; and the pieces are grouped by 192 covers of 8.

The paired runner is [`../scripts/physical_cell_cutting_normalizer_rigidity_cycle776_2026_08_11.py`](../scripts/physical_cell_cutting_normalizer_rigidity_cycle776_2026_08_11.py), it builds everything in-run from the corners upward, reads no cached data and no input file, works exactly over the integers and two fixed primes, uses no floating point in any gate, fits no constant, and prints one line per gate. The object is built from the lattice and admissibility content of the four axioms in [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) and imports nothing else.

The group of 384 signed coordinate maps — the 24 permutations of the four coordinates composed with the 16 sign flips — acts freely on the 36864 pairs of a piece and a cover, giving 96 orbits of size 384, each read as a zero-one table over covers by pieces. The 96 tables are pairwise disjoint and sum to the all-ones table, so every 4-subset of them is an 8-regular zero-one member of a family of 3321960; the cover incidence is one member.

## 2. Why the row condition forces a commuting bijection

Each of the 96 tables is a single orbit of the diagonal action of the group on pairs of a piece and a cover, so each table, and therefore each family member, is carried to itself by every group element acting on both sides at once. Suppose a member has every row a cover, so that row `c` of the member is cover `s(c)` for some map `s` of the cover set. Diagonal invariance says a piece `p` lies in row `c` exactly when the moved piece lies in the moved row, and reading both sides as covers turns that into the statement that `p` lies in cover `s(c)` exactly when the moved piece lies in cover `s` of the moved cover. That is the definition of a bijection commuting with the group action.

The runner does not take this on trust. It builds the 384 by 384 multiplication table, checks that the cover action is a homomorphism on all pairs, and then, for each of the 48 members it has censused, forms the induced row map directly and tests the commuting identity against every one of the 384 group elements at every one of the 192 covers. That is 3538944 individual comparisons and there are 0 misses.

## 3. The index: 48 is 96 over 2, and 96 is 6 times 16

The group is transitive on the 192 covers. The stabiliser of a cover has order 2, and its non-identity element is a single-axis sign flip. For a transitive action the bijections commuting with the group are exactly the right multiplications by the normalizer of a point stabiliser, one for each coset of the stabiliser inside its normalizer, so their number is the index.

The normalizer here has order 96 and coincides with the centralizer of the stabiliser's generator. Its order factors for a reason that is visible on the axes. Conjugating the flip of an axis by a signed coordinate map gives the flip of the permuted axis, so a group element commutes with the generator exactly when its coordinate permutation fixes that one axis. The permutations of four coordinates fixing a given one number 6, and all 16 sign flips commute because the sign group is abelian, giving 6 times 16 equal to 96. The index is then 96 over 2, which is 48.

The runner builds all 96 normalizer elements, forms the 48 bijections, and confirms each is a bijection of the 192 covers, that each arises from exactly 2 normalizer elements, and that each is independent of which coset representative was used, on all 96 elements. It then decomposes each image back into tables and finds that all 48 give family members, all 48 distinct, with the cover incidence among them.

## 4. The census, and the theorem that the two 48s coincide

Independently of any of that, the runner censuses the family directly. Reading off, for each ordered pair of covers, which tables own the eight pieces of the second cover along the row of the first, a family member has row `c` equal to cover `d` exactly when those eight pieces fall into four tables two at a time. Intersecting the resulting sets over all 192 rows leaves exactly the members every one of whose rows is a cover. The census returns 48.

The two 48s are the same 48: their symmetric difference is 0. This is the load-bearing gate of the cycle. Without it the agreement of two counts would be a coincidence of arithmetic; with it, the brute-force census has been identified as the coset space of the normalizer.

Every one of the 48 sends the 192 rows bijectively onto the 192 covers. Composing two of the induced maps gives a third, so the 48 form a group of order 48 acting simply transitively on the 48 members: inside the census nothing is distinguished, and no further group-theoretic condition can single out a member without an extra requirement.

## 5. The extra requirement, and why it lands on 2

The extra requirement is that the relabelling of covers induced by the member be realized by an actual symmetry of the cell rather than by an abstract bijection. A commuting bijection is a right multiplication; it is also a left multiplication exactly when it lies in the centre. The centre of this group has order 2, consisting of the identity and the all-axes sign flip. The runner tests all 48 induced maps against the 384 group elements and finds exactly 2 in the group, and those 2 are exactly the centre. Their members are the cover incidence and one other. So 46 of the 48 realize their cover bijection by a map outside the 384, and the identification stops at a pair, both counts being group indices rather than measurements.

## 6. Two rejectors

The first shows the pair is not an artefact of how covers were numbered. Relabelling the covers of the incidence by a group element and asking whether the result is still a sum of four tables succeeds for the 2 central elements and fails for all 382 others.

The second shows the row condition is doing work no linear instrument could have done. The all-axes flip induces an involution on the 96 tables with no fixed point, and swapping any subset of a member's four parts for their partners gives a four-element swap group of 16 variants of the incidence. Two of the variants this runner tests carry the incidence's entire 16-pattern block-rank profile at both primes and are nevertheless outside the census. So a member can agree with the incidence on every rank this framework measures and still fail to have covers for rows. The rank profile could not have replaced the row test, and the two "fours" appearing in this note — the four profile-carrying variants just tested and the label-and-row survivors of section 7 — are different sets.

## 7. Rank is blind on the census; the image label is not

Inside the census the block-rank profile separates nothing: all 48 members carry the incidence's whole profile across all 16 flip patterns, and at both primes, which agree entry for entry. This is a sharp statement of where the linear instruments of cycles 771 to 775 run out — they are blind on precisely the set the row condition isolates, while remaining sharp on the wider family, where they cut 3321960 down to 30720.

The image label of `cycle 775` is not blind there. Labelling each table by the column space of its restriction to a weight-1 block and taking the sorted multiset over a member's four parts, exactly 4 of the 48 carry the incidence's label at all four weight-1 patterns. Those 4 are closed under the partner involution and form two partner pairs with no fixed point, and the symmetry pair of section 5 is one of the two. Filtering the census by the 11 low-weight block ranks as well as the label gives the same 4. So the identification ladder is 3321960 members, 30720 after the label, 48 after the row condition, 4 after both, and 2 after the symmetry requirement.

## 8. The partner map is precomposition by the centre

The involution used above is not an ad-hoc pairing. Precomposing the piece side of a table by a group element and asking that the result be again one of the 96 tables succeeds for exactly 2 of the 384 elements, and those 2 are the centre; each of the 14 non-central pure sign flips sends 0 of the 96 tables back into the set. So the partner map is precomposition by the all-axes flip, and nothing else.

Two consequences. First, a character law: comparing a table's restriction to a flip-pattern block with its partner's, the two are equal at even weight and exact negatives at odd weight, on all 96 tables, all 16 patterns and both primes. Second, a relabelling identity: summing the partners of the incidence's four parts returns the incidence with its covers relabelled by the central flip. The residual pair is therefore the same object twice under two namings of the covers, which is why no instrument in this runner that is blind to the naming of covers can separate them.

## 9. Boundary and honest negatives

The census is 48 and not 2; only the symmetry requirement of section 5 reaches 2, and the label-and-row filter of section 7 reaches 4 rather than 2. The block-rank profile separates none of the 48 at either prime, so section 7's ladder depends on the image label and the row condition, not on rank. 46 of the 48 realize their cover bijection by a map outside the 384, so the census members are not all symmetries in disguise. The residual pair cannot be separated by any rank or image instrument in this runner, because the two members differ by a relabelling of the covers and every such instrument is blind to that relabelling; reducing the pair to a single member would need an instrument sensitive to the naming of covers, which this note does not supply. The reduction from 3321960 to 48 uses the row condition and the diagonal orbit structure; it says nothing about members that fail the row condition, and in particular the `cycle 773` twin remains a member of the family in good standing that is simply not in the census. The row condition is one of a pair of natural conditions a member could be asked to satisfy; the mirror condition, that every column of the member be the set of covers meeting some piece, is not measured in this runner.

## 10. What this changes

Before this cycle the honest description of the cover incidence was that it is one of millions of look-alikes, distinguished from them by nothing the framework could compute. That description was wrong in an instructive way: the look-alikes are look-alikes only to linear instruments. The defining combinatorial property of the object — that its rows are covers — cuts the family to a coset space of the symmetry group, and the requirement that the induced relabelling be a symmetry cuts that to the centre. Both of the surviving counts are indices read off the group, so nothing in the construction of the cover incidence was a free choice, up to the naming of the covers. That is the property the wider evidence-ceiling programme has been asking for: a structure whose identification is derived rather than observed.
