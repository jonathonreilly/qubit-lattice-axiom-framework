# Independent check: patch symmetry multiplicity

The revised argument in `/tmp/neutral-soft-multiplicity-draft.md` is sound given the uniform patch upper bound, the global fourth-order normal-form remainder, and the odd-sector lower/cluster separation bounds already established in the dressed-patch proof. In particular, exact odd physical Z parity fixes the earlier minmax concern: one need not first project every trial into the exact heavy spectral cluster.

## Orbit and phases

At periodic longitudinal height four, X and Y plane operators intersect on four physical sites and commute, square to identity, and preserve total Z parity. On an aligned column, Y tensor four equals X tensor four times Z tensor four, with phase i^4=1. Its phase is therefore +1 on an aligned column and -1 on a column carrying the singleton defect. This is precisely the particle-position-dependent gauge phase, not a change in trial energy. Retaining the exact physical plane operators automatically retains it.

Choose m row planes and m-1 column planes meeting the reset square. Their action on the square has 2^(2m-1) distinct patterns. If r rows and c columns are flipped, the number of changed column signs is m(r+c)-2rc. With one of the two families missing one generator, a nonidentity restricted pattern changes at least m columns. Thus there is no stabilizer or minus-identity relation on this orbit. Transformations can change the outside vector arbitrarily without spoiling this argument: orthogonality is already certified inside the reset patch.

Choose a pure component of the outside reduced density once. Linearity of expectation guarantees at least one component with energy no larger than the mixed trial average. Apply exact symmetries to that same trial. No simultaneous optimization of exponentially many outside states is required.

## Compression, not invariance

Two orbit configurations differ in at least m background columns in the reset patch. Height four gives at least 4m-2 different physical spins after allowing the singleton positions in bra and ket to differ. A fourth-order native word contains at most four transverse insertions and flips at most eight spins; diagonal resolvents, wall filters and projectors do not change this count. Hence sufficiently large m gives zero cross matrix element for every coefficient through order four, including the height-four winding terms. The more general bounded-support version in the draft also suffices.

Consequently the compression of B4 to the orthonormal orbit span is the common scalar trial expectation. The span need not be invariant. Minmax only requires its Rayleigh quotient bound. A global operator-norm remainder contributes its norm once, with no orbit-dimension factor. The SW inverse preserves orthogonality and, for an equivariant construction, every selected plane character.

The orbit is a regular representation of the chosen commuting subgroup. Its normalized character Fourier sums give one trial vector in each character sector. Flat-pattern orbit vectors themselves are not charge eigenvectors; the Fourier step is necessary for the selection-rule statement.

## Exact odd-sector minmax

Every height-four N=0 aligned-column state has even physical Z parity. A singleton or complementary three-spin column defect has odd parity, whereas a half-column defect has even parity. The trial, plane subgroup and normal-form unitary all preserve the odd sector. Thus minmax can be applied directly to the exact Hamiltonian restricted to odd parity (also separately to each selected subgroup character).

Given the existing wall-relative bound separating N>=4 from the energies near 4J and the O(J lambda^3) global remainder, the resulting low odd eigenvalues belong to the heavy cluster. The heavy lower bound Eb+4J-4J lambda-O(J lambda^3), together with the patch upper bound and m~lambda^(-3/4), places at least 2^(2m-1) eigenvalues, counted with multiplicity, in an O(J lambda^(5/2)) interval above the odd heavy bottom. Replacing Eb by the actual vacuum energy changes only the already controlled O(J lambda^3) error. This does not imply that these eigenvalues are all distinct.

## Interpretation

This establishes many low-cost symmetry characters under the stated joint-box bounds. It establishes neither many neutral-accessible internal levels in one fixed character nor a scalar oscillator. An original neutral observable commuting with the selected subgroup has exactly zero matrix elements between different characters. The variational outside-state choice is an existence argument, not state preparation or state selection. No lifetime, fermion statistics, or selected radius follows.
