# Independent review of the conditional quantum lift

2026-09-21. **No unresolved mathematical or implementation finding.** The
orthogonal configuration-space intertwiner, the square coherence comparison
and the stated literal tensor-qubit Gram examples agree with independent
exact reconstruction. The negative examples are correctly scoped to the
specified product map and conditioned Hamiltonians. No source correction is
requested, and no audit or retained status is assigned.

## Read boundary and source identities

The complete note was read first. The new author checker, results and logs
were not opened until the independent derivation and controls were sealed in
`PRE_COMPARISON_SEAL.json`, SHA-256
`66ef74f915b5b5cbdcd72770637f9193bd355f704ee5fc5209257ea6285a812b`.
That seal and all its artifacts remain unchanged. The author checker was then
read completely; its unchanged matching helper had already been read and is
reused by exact identity. The entire result and run log were authenticated.

| Source/evidence | SHA-256 |
|---|---|
| `GEOMETRIC_QUANTUM_LIFT_BOUNDARY.md` | `935163267392a28e53447e940d0e4dd4b9cd07faa7ff146fc8a9740c61ac584d` |
| `geometric_quantum_lift_check.py` | `128602645f8ca7607a94f32c746ba8e251b644aabf8d45514d9129de1710a88c` |
| `geometric_corridor_transport_check.py` | `76ac19c67cd1d9d1c724f88f49a36c990524a5ee955a52058af4292c933d7f0c` |
| author `geometric_quantum_lift_checks/RESULTS.json` and byte-identical run log | `0ed01e84a5be5e725be07fe1d1b80335fccc61e5ea72c7eb0008b22de8458e76` |

The author result binds its runner and helper, not the prose note. This
review's source manifest and final seal additionally bind the note. Both
contextual literature paragraphs were read as part of the source; the papers
and their external receipt were not inspected, and no theorem from them was
used. This review does not independently verify their phase/dispersion claims.

## Reconstruction and precise conclusions

With distinct permanent key pairs, each matching has F=2^K K! marked states.
In the expressly additional orthogonal configuration Hilbert space, the
normalized fiber sums therefore define an isometry U. For each declared
square, clockwise and counterclockwise rotations each biject the source
fiber with the flipped fiber. They preserve flippability and commute with
its projector. Their sum yields twice the geometric flip; the coefficient
-t/2 gives exactly -t in the geometric Hamiltonian. Potential and geometric
diagonal observables also intertwine. This is valid for real t,v, with
channel multiplicities retained. It does not construct that carrier or its
preparation from the classical rules or local M_2(C) alone.

For one four-cycle orbit, the kinetic eigenvalues are -t,0,t,0. At u=t tau,
a definite even basis vector has odd amplitudes i sin(u)/2 at both odd
states, giving sin^2(u)/2. The equal incoherent mixture of the two even
states has the same probability. Their normalized coherent sum has odd
amplitudes i sin(u)/sqrt(2), giving sin^2(u). The independent checker also
verifies the exact propagator's unitarity. These are orthogonal-configuration
probabilities, not probabilities computed from the nonisometric literal
product map later in the note.

For the square product map, the stated distinct-geometry overlap is1/2 and
the z/x marked Gram rank is11. A symbolic calculation for the real second
pair(p,q),(-q,p), p^2+q^2=1 gives the fiber Gram

    [[1+(p^2-q^2)^2, 1], [1, 1+(p^2-q^2)^2]].

It specializes to the all-ones matrix for z/x and to the stated674/625
diagonal matrix for p=3/5,q=4/5. The latter determinant is63651/390625>0.
These fiber vectors are not assumed normalized after applying V; the diagonal
greater than one is consistent with V not being an isometry.

If H_phys and H_mark are Hermitian and H_phys V=V H_mark, then
V^dagger H_phys V=G H_mark is Hermitian. Thus[G,H_mark]=0 is necessary,
regardless of V's kernel. Independently assembled ladder matrices violate
this condition at each stated v. After comparison, the exact published
entries were recomputed directly from sparse local neighbors and products
of single-spinor overlaps:

| v | published indices | independently recovered entry |
|---|---|---|
|0|0,48|-5/16-i/16|
|1|0,104|1/2|
|2/3|0,104|1/3|

The first witness is purely kinetic; the latter two are purely potential at
their selected entries. Their actual configuration labels also agree with
the author enumeration. The full ladder kinetic matrix and flippability
diagonal agree with the independent construction after reindexing.

## Phase freedom and positive countercontrol

One representative spinor phase per fixed record is especially harmless
here: every full configuration contains every record once. Consequently all
columns of V acquire the same global phase, leaving G, the fiber Gram and
the commutator unchanged. The author uses(i,1)/sqrt(2) for the second y state;
the independent construction uses(-1,i)/sqrt(2). Their ratio is -i, exactly
one common factor in every complete product column. This explains the exact
agreement without depending on a preferred physical spinor phase.

A general configuration-basis rephasing D instead requires V'=VD and
H'=D^dagger H D. Then G'=D^dagger G D and the compatibility commutator is
unitarily conjugated. Holding H fixed while changing relative coherent
column phases changes the proposed lift. This is consistent with the note's
qualification; no representative-phase escape exists for the fixed-inventory
map tested here.

Nonorthogonality, dimension excess or the square fiber collapse alone is
not a blanket obstruction to a physical Hermitian intertwiner. A separate
positive control constructs the literal four-qubit cyclic tensor permutation
on one square and verifies P_phys V=VR, H_phys V=V H_mark and[G,H_mark]=0,
even though that V has rank11. Every allowed square configuration is
flippable, so no nontrivial geometric conditioning is required in that
example. This preserves the source's distinction between unconditional
tensor permutations and the conditioned ladder operation.

## Verification coverage, reproduction and limits

The precomparison programs independently enumerate the square, ladder and
cube:16,144,3456 marked configurations and32,384,18432 enabled two-sense
channels. Integer fiber identities, four-step rotations, inverse moves and
nearest-neighbor motion of each actual record are checked. Square ranks,
generic fiber Grams, propagator probabilities, representative-phase changes
and the positive square lift use exact symbolic arithmetic. Ladder Gram
entries are Gaussian integers divided by16; their commutators use exact
integer real/imaginary arrays and rational scaling. The later sparse witness
calculation provides a second implementation of the decisive entries.

The three runnable checks are `independent_check.py`, `positive_control.py`
and `compare_author.py`; their complete logs and receipts are retained. Each
passed its first execution with empty stderr. No failed checks occurred.
The author main routine was not rerun; only its small ladder constructor
was called for the complete matrix/index comparison. Stored author results
and logs were authenticated separately from the independent calculations.
The author floating-point search selects witnesses; their nonzero values
were verified exactly in both implementations.

To reproduce without overwriting sealed evidence, copy the two precomparison
programs to a fresh directory and run them with Python, NumPy and SymPy. For
the postcomparison program, use a fresh sibling directory containing those
programs, the comparison program and copies of the twelve precomparison
artifacts plus their seal. Its pre-seal check intentionally authenticates
the absolute original evidence paths. No program calls the author main or
writes to primary sources.

The result is conditional on a finite orthogonal marked carrier for the
positive bridge, and on the exact literal map/Hamiltonian for the ladder
counterexamples. It supplies no general quantum no-go, physical recognition
instrument, alternative-carrier classification, native coherent preparation,
ground-state selection, phase theorem or photon identification. The reviewed
source keeps those boundaries. All primary sources and earlier independent
evidence were left unchanged.
