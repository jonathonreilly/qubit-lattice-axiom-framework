# Independent all-height complementary-hop check

The proposed coefficient and open-Ising proof check out as a fixed-height leading matrix element. I replayed `/tmp/neutral_complementary_all_length.py`; its exact rational amplitudes agree with 2^(-(L-2)) for L=2,...,15. The all-length argument below does not rely on extrapolating that table.

## Physical path and denominators

Initially column i has its singleton at layer 0 and column j is aligned. Flip the same transverse edge on a subset S of the complementary layers 1,...,L-1. With c(S) its number of occupied runs and a(S) its number of occupied open-chain ends, the vertical wall count is

N(S)=2+4c(S)-2a(S).

The energy above the initial N=2 configuration is therefore J[8c(S)-4a(S)]=4J[2c(S)-a(S)]. Every proper nonempty subset has strictly positive gap. The final full subset restores N=2, with the singleton at j, layer 0, and both aligned-background signs reversed. Counting the two boundary bonds touching layer 0 explicitly is important: their combined contribution stays the same when both endpoints of a transverse pair flip.

The initial and final physical strings differ on exactly 2(L-1) spins. At order L-1, every insertion must flip two of those target spins exactly once. Since transverse native bonds preserve layer, the only permissible insertion at each complementary layer is the original edge joining i and j. No other edges or repeated insertions can contribute at this order on a nonaliased transverse grid.

Every ordering stays outside the N=2 block until its last insertion. Thus folded canonical terms cannot connect these endpoints at the minimal order: a factorization through an intermediate model-space state would require an intermediate proper S with N=2, which does not exist. This excludes folds for this matrix element, not all folded contributions at that order elsewhere.

## All-length path sum

Put n=L-1. The auxiliary open chain

H_aux=-2 sum_(j=1)^(n-1) Z_j Z_(j+1)-lambda sum_(j=1)^n X_j

has the same intermediate excitation energies 4[2c(S)-a(S)]. Its first off-diagonal tunneling term between its two aligned vacua is minus lambda^n times the positive path sum in the supplied recurrence.

For completeness, with Jordan-Wigner Majoranas a_j,b_j, this Hamiltonian is a bilinear coupling between the two Majorana sublattices with bidiagonal matrix having diagonal lambda and neighboring off-diagonal 2, up to removable signs. If its singular values are s_j, the fermionic excitation energies are 2s_j. The determinant has modulus lambda^n. As lambda tends to zero, n-1 singular values tend to 2, while one tends to zero. Hence

s_min=lambda^n/2^(n-1) [1+o(1)].

The two lowest many-body states differ by occupation of this one mode and have splitting 2s_min. Spin-flip symmetry makes the two aligned-state diagonal effective energies equal. The magnitude of their effective off-diagonal matrix element is consequently s_min; its leading sign is negative from the ordered perturbative paths. Therefore the exact minimal-path sum is 2^(-(n-1))=2^(-(L-2)). For n=1 there are no denominators and the same formula is immediate.

## Native signs and normalization

Each XX insertion has matrix element -J lambda. The L-2 negative resolvent denominators give a net negative x-edge amplitude for every L:

-J lambda^(L-1)/2^(L-2).

At an untouched complementary layer, YY acting on the aligned pair has matrix element -s_i s_j; the native minus sign thus gives +J lambda s_i s_j per insertion. For even L the net y-edge amplitude is

+J lambda^(L-1) s_i s_j/2^(L-2).

For odd L it instead equals -J lambda^(L-1)/2^(L-2), independent of the two background signs. This is a useful parity qualification if the result is stated beyond even heights. In particular L=4 reproduces the independently checked x=-J lambda^3/4 and y=+J lambda^3 s_i s_j/4.

The L=2 numerical row is a valid auxiliary path-sum check, but a physical singleton/majority-background identification is redundant at height two and should not be inferred from it. The intended even-height native application should use L>=4 and transverse dimensions without duplicated edges.

## Scope

This is an actual native coefficient for an assisted hop, not an introduced interaction. It is one background-changing channel, not the complete effective Hamiltonian at that order. The result is for each fixed L as lambda tends to zero. It supplies no uniform dominance estimate when L grows, no selected height or feature radius, and no experimentally identified hierarchy. Different supplied slab heights have different perturbative exponents; that fact alone does not derive a hierarchy of physical species.
