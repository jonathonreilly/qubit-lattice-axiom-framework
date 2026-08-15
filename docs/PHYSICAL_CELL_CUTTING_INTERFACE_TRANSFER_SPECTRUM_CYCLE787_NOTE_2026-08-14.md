# Physical cell cutting: the interface transfer operator, its exact spectrum, and strip growth

Date: 2026-08-14
Authority: none
Audit: unset
Status: proposed_retained
Claim type: bounded_theorem
Constitutional effect: none.

## Trace gate

- `trace_class: frontier_discovery`
- `target_claim_id: null`
- `target_blocker_text: null`
- `source_of_blocker_text: frontier_question`
- `reachability_to_target: unknown_frontier`
- `artifact_role: theorem`
- `next_trace_action: test whether the growth eigenvalue and the positive eigenvector class weights have a canonical downstream consumer; none is claimed here`

## Status contract

- `actual_current_surface_status: bounded-support`
- `target_claim_type: bounded_theorem`
- `trace_class: frontier_discovery`
- `reachability_to_target: unknown_frontier`
- `conditional_surface_status: null`
- `hypothetical_axiom_status: null`
- `admitted_observation_status: null`
- `claim_type_reason: exact spectrum, integer invariants, strip counts and evenness certificates for the interface transfer operator of the declared unit four-cube object; no physical or lattice-wide identification`
- `audit_required_before_effective_retained: true`
- `bare_retained_allowed: false`

## Scope and objects

The declared finite object consists of the 16 corners of the unit four-cube, the 2672
five-corner pieces of determinant one built on them, the 400 pieces surviving at the adjacency
cost floor 6, the 15800 cuttings assembled from 24 such pieces each, the 192 pieces that occur
in some cutting, and the 384 signed coordinate maps of the cell. These are finite-scope object
choices, not imported physical primitives. There are no load-bearing literature, empirical,
fitted, external-data, or repository-derived scientific inputs. The linked runner uses the
standard library only, performs no file input or output, draws no random numbers, and carries
out every load-bearing check in integer or exact rational arithmetic; it rebuilds the whole
object from the corner list before any gate runs, so every integer below is recomputed here
rather than carried in.

Each cutting dissects every one of the 8 boundary three-cubes into 6 tetrahedra, and only 16
such dissections ever occur. They are the letters of the facet alphabet, and the letter set is
literally the same 16 on all 8 slots. A letter is either light, occurring on a given slot in
862 cuttings, or heavy, occurring in 1364; 12 letters are light and 4 are heavy, and
12 x 862 + 4 x 1364 = 15800. The alphabet, its multiplicities and the parity law it carries
are the subject of the sibling note
`PHYSICAL_CELL_CUTTING_FACET_ALPHABET_HEAVY_PARITY_CYCLE786_NOTE_2026-08-14`; every fact of
that kind used below is recomputed by this cycle's own runner from the object, not cited.

## The transfer operator

Fix an axis a. Every cutting shows one letter on side 0 of that axis and one letter on side 1,
so the cuttings distribute over ordered letter pairs. The interface transfer operator of the
axis is the 16 by 16 integer matrix whose entry in row k and column j is the number of cuttings
whose letter on side 0 is k and whose letter on side 1 is j.

The four axes give the same matrix entry for entry, on all 256 entries with 0 misses. This is
an equality, not a conjugacy: the cell group permutes the axes and therefore conjugates one
axis matrix into another by a letter relabelling, which by itself would only force the four
matrices to be similar. That the relabelling can be taken to be the identity on the alphabet is
a certified computation of this object. One matrix, written T below, therefore carries the
whole interface.

T is symmetric, T[k][j] = T[j][k], on all 256 entries. Its row sums are exactly the letter
multiplicities, so the row-sum census is 12 rows of 862 and 4 rows of 1364. Its entry census is
{18: 24, 36: 48, 50: 48, 52: 48, 90: 12, 92: 48, 100: 12, 104: 12, 200: 4}; the least entry is
18, so T is strictly positive, meaning every ordered letter pair is actually realised by some
cutting. Its trace is 2000, that is 2 x 1000, and each of the 16 diagonal entries is even on
its own.

## Commutation and the pair orbits

The maps of the cell that hold the chosen axis are the 96 signed coordinate maps whose
coordinate permutation fixes that axis. Such a map sends the pair of bounding hyperplanes of
the axis to itself, and it acts on the remaining three coordinates by one signed map of the
three-cube. That single three-cube map is applied to both boundary cubes at once: the axis sign
bit decides only whether the two sides keep their names or trade them, and it never enters the
transverse action. So each holding map carries one letter map of the alphabet, the same on both
sides. The runner checks this mechanism directly on 15800 cuttings x 48 maps x 2 sides with 0
misses.

The 48 letter maps obtained from the side-preserving half are distinct, contain the identity,
are closed under composition, and each permutes the 16 letters, so they form a group of order
48 acting on the alphabet. Because the letters follow the cuttings, T is invariant under this
group acting on rows and columns simultaneously: 0 misses. Equivalently, T lies in the algebra
of matrices commuting with all the letter maps, and that algebra has dimension twelve, because
the group has exactly 12 orbits on ordered letter pairs. The orbits have sizes
[4,12,12,12,12,12,24,24,24,24,48,48] and carry the constant entries
[200,18,18,90,100,104,50,50,92,92,36,52]. Only 9 distinct values appear on the 12 orbits: the
values 18, 50 and 92 each occur on two different orbits, so equal entries do not always mean
equivalent pairs, and orbit membership is finer than the entry census.

## The exact spectrum

The characteristic polynomial of T factors exactly over the integers as

`(t - 50)^2 (t - 42)^2 (t - 10)^3 (t + 54) (t^2 - 1090 t + 53968) (t^2 - 250 t + 7728)^3`

with degrees 2 + 2 + 3 + 1 + 2 + 6 = 16. Three independent computations certify it. First, the
factored form is compared against the determinant of t I - T at all 17 points t = 0 to 16;
since both sides are of degree 16, agreement at 17 points is an identity, not a sample. Second,
the eigenspace dimensions are computed as exact kernel dimensions: 2 at 50, 2 at 42, 3 at 10, 1
at -54, and 2 and 6 at the two quadratic factors, summing to 16. Because the multiplicities are
attained by the kernels, T is diagonalisable and its minimal polynomial is the product of the 6
distinct factors, of degree 8; the runner confirms that this product annihilates T and that
each of the 6 single-factor drops leaves a nonzero matrix, so the test is fully discriminating
and no smaller product would do.

Third, both quadratics are irreducible with square-free discriminant:
1090^2 - 4 x 53968 = 972228 = 4 x 243057 with 243057 = 3 x 81019, 81019 prime and not divisible
by 3; and 250^2 - 4 x 7728 = 31588 = 4 x 7897 with 7897 = 53 x 149. So the eigenvalues outside
the integers live in the two real quadratic fields adjoining the square roots of 243057 and
7897, and nothing is approximated anywhere.

## The class block and the growth eigenvalue

Split the alphabet by weight into the 12 light letters and the 4 heavy ones. The number of
cuttings joining a letter to a whole class does not depend on which letter of a class one
starts from: a light row sends 578 to the light class and 284 to the heavy class, and a heavy
row sends 852 to the light class and 512 to the heavy class, with 578 + 284 = 862 and
852 + 512 = 1364. The class split is therefore an equitable partition, and its two-by-two block
has trace 1090 and determinant 53968, which is exactly the quadratic factor
t^2 - 1090 t + 53968 of the characteristic polynomial.

Write w for the positive square root of 243057. The block eigenvalue is 545 + w, and the vector
with light component 284 and heavy component w - 33 is an exact eigenvector of the block over
the ring adjoining w: both sides of the eigenvalue equation agree entry for entry, with no
rounding. The vector is strictly positive because 1089 < 243057. Bracketing w between
consecutive integers, 493^2 = 243049 < 243057 < 244036 = 494^2, so 1038 < 545 + w < 1039. Every
other eigenvalue is smaller in size than 214: the integer ones are 50, 42, 10 and -54, the
companion root 545 - w is below 52, and the other quadratic contributes 125 plus or minus a
number below 89, since 88^2 = 7744 < 7897 < 7921 = 89^2. The gap between 214 and 1038 is
therefore certified by integer comparisons alone, and the growth eigenvalue is simple and
dominant.

The positive eigenvector weights heavy letters more heavily than their share of the cuttings
would suggest. The weight ratio is (w - 33) to 284, while the multiplicity ratio is 1364 to
862; the first exceeds the second exactly when 862 x w exceeds 284 x 1364 + 33 x 862 = 415822,
which after squaring is the integer inequality 862^2 x 243057 = 180602045508 > 172907935684 =
415822^2. So a heavy letter carries strictly more growth weight per letter than its raw
frequency, and the certificate is an exact integer comparison.

## Closed strips

Stack cells along the chosen axis and require the letters to match across each interface. A
closed strip of n cells is a cyclic sequence of n cuttings in which the side-1 letter of each
matches the side-0 letter of the next, cyclically, so the number of closed strips of n cells is
the trace of the n-th power of T. For n = 1 the condition is that a single cutting shows the
same letter on both sides of the axis; the runner counts those cuttings directly and finds the
trace value 2000, which is why the trace has a counting meaning and not merely a spectral one.

The counts for n = 1 to 6 are 2000, 1233040, 1148284352, 1167237515200, 1206389522378240 and
1251135002657559808. As a cross-check on the factored characteristic polynomial, the same six
numbers are regenerated from the power-sum recurrence driven by the expanded coefficients, with
0 misses; the two routes share no arithmetic. Since the growth eigenvalue is simple and
dominant, the counts multiply by a factor between 1038 and 1039 for each further cell, and the
class weights above say how that growth is shared between light and heavy letters.

## Integer invariants

The invariant factors of T over the integers are eleven copies of 2, then 210, 420, 19320,
96600 and 17594917200, each dividing the next. Their product is
5931574826283246551040000000, which equals the absolute value of the determinant, and the
determinant itself is negative, as it must be, since -54 is the only negative eigenvalue and it
is simple. The same absolute value is the spectral product 50^2 x 42^2 x 10^3 x 54 x 53968 x
7728^3, so the invariant-factor route and the spectral route agree. Every invariant factor is
even, and the largest is 17594917200 = 2^4 x 3^4 x 5^2 x 7 x 23 x 3373.

## Evenness

Every one of the 256 entries of T is even. Most of that statement is derived, and the runner is
explicit about which part is not.

Group the cuttings into the 256 fibers of the ordered letter pair they show on the axis, so the
fiber over a pair has exactly the size given by the corresponding entry. A holding map keeps a
fiber to itself precisely when its letter map fixes both letters of the pair, if the map
preserves the two sides, or exchanges them, if the map trades the sides; the runner cross-checks
this criterion against the direct test on every fiber and every one of the 96 maps with 0
mismatches. If some map keeping a fiber acts on it with no fixed point and with every orbit of
size 2, that map pairs the fiber with itself and the entry is even. Counting such free-pairing
witnesses per fiber gives the census {0: 48, 1: 156, 2: 48, 4: 4}, so 208 of the 256 fibers
have at least one witness and their entries are even by an explicit pairing.

The cleanest special case is the axis reversal that flips the chosen coordinate and leaves the
other three alone. Its letter map is the identity, it trades the two sides, and it fixes 0 of
the 15800 cuttings, so it pairs every diagonal fiber freely and all 16 diagonal entries are
even for that single reason.

The remaining 48 fibers are exactly one orbit: the size-48 orbit of pairs whose entry is 36.
There the negative is sharp. Not only does no map act freely on those fibers, but 0 of the 48
fibers admit any of the 96 holding maps whose orbits on the fiber are all of even size, which
is the weakest condition under which a group element could certify evenness at all. Their
entries are even, but that fact is measured, not derived: the symmetry mechanism provably
cannot supply a certificate there, and any derivation of it must come from outside the group
action.

## Boundary and honest reading

Measured, not derived, at the declared finite scope: the entries of T themselves and every
census quoted above, including the entry census, the row-sum census and the free-pairing
census; the entrywise equality of the four axis matrices, which is stronger than the conjugacy
the cell group supplies; the class-block values 578, 284, 852 and 512; the factorisation of the
characteristic polynomial as a factorisation of this particular matrix; and the evenness of the
48 entries in the entry-36 orbit.

Derived at the declared finite scope: the mechanism by which a holding map acts by one letter
map on both boundary cubes; the consequent invariance of T under the group of order 48 and its
constancy on the 12 pair orbits; diagonalisability and the degree-8 minimal polynomial, from
the certified kernel dimensions; the identification of the class block with a quadratic factor;
the exact eigenvector, the bracketing between 1038 and 1039, the domination gap and the heavy
over-weighting inequality; the reading of traces of powers as closed strip counts; and the
evenness of the entries on 208 of the 256 fibers.

All of the above are computational identities of the declared unit four-cube object and its
15800 cuttings. No physical, dynamical, or lattice-wide identification is claimed, no continuum
limit is taken, no growth statement is transported to any infinite system, and nothing here is
asserted about cell-cutting systems outside the declared object.

## Reproduction

Run
[physical_cell_cutting_interface_transfer_spectrum_cycle787_2026_08_14.py](../scripts/physical_cell_cutting_interface_transfer_spectrum_cycle787_2026_08_14.py).
The reviewed cached output belongs at
[physical_cell_cutting_interface_transfer_spectrum_cycle787_2026_08_14.txt](../logs/runner-cache/physical_cell_cutting_interface_transfer_spectrum_cycle787_2026_08_14.txt)
and is regenerated by the reviewer. The runner declares an `AUDIT_TIMEOUT_SEC` budget, typically
finishes in well under a minute, and stays far under one gigabyte. Its final line is
`TOTAL: PASS=22 FAIL=0`, and it exits nonzero if any gate fails.

## Review record and boundary

- The runner prints censuses, orbit data, spectral certificates and derived identities only;
  the full interface matrix is deliberately not printed, so the note quotes its entry census,
  row sums, trace and class block instead.
- The exact immutable reviewed head and landing SHA belong in the PR review comment because a
  commit cannot contain its own hash.
- The new citation-graph node must be regenerated and co-landed with this note.
- Independent review is required before any downstream use of these results.

Within those boundaries, the appropriate review classification is **bounded support** for the
declared exact finite object.
