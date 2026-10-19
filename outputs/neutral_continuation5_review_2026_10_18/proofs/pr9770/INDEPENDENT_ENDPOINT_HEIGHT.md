<!-- Original PR9770 source SHA256 364129ae9b7878e17f4e7a6f9584b64e584e0a972c43cc607685a2eac3bfdc55. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Independent native endpoint-height and readout check

Read `/private/tmp/neutral_endpoint_root.md`. The first-order rules, rigid-state leakage coefficient, and the stronger constant-readout statement below are correct in the stated long-interval regime.

## First-order endpoint matrix elements

For one down interval [l_c,h_c] in each occupied column, length at least two, a single spin flip preserves that column's two longitudinal walls precisely when it extends or contracts an endpoint. In the upper interface the allowed sites are h_c and h_c+1. With the lower endpoint far away, intersection of the two neighboring columns' allowed sets gives:

- equal heights h: layer h lowers both heights, layer h+1 raises both;
- heights h and h+1: their sole common layer h+1 lowers the higher and raises the lower, exchanging the heights;
- height separation greater than one: no upper-interface first-order transition.

The native bond is -J_a sigma^a sigma^a. XX always contributes -Jx. Since Y|up>=i|down> and Y|down>=-i|up>, YY has product -1 for equal physical spins and +1 for opposite spins. Its Hamiltonian amplitude is therefore +Jy for equal-height simultaneous raising/lowering, and -Jy for the mixed-spin height swap. No extra Pauli or orientation sign is missing.

The criterion is local to intervals of length>=2 with no one-site holes or isolated spins. In a more general wall configuration, one column can lose two walls while another gains two, preserving total N without both flips individually preserving its wall count. Such processes must not be excluded from the full N sector by the restricted height rule. Collisions, disappearing intervals, nearby lower/upper ends, or extra intervals require their actual spin configuration.

## Rigid rectangle leakage

Let the initial state have the same interval of length ell>=3 in every column of a rectangle F, area A>2, and all other columns unflipped. For each internal transverse bond there are four distinct wall-preserving pair flips, at the two extension/contraction layers of the upper and lower ends. A change of only the two columns on the bond cannot leave both interfaces flat over all A columns, so every target is outside the fixed-shape rigid subspace.

Different edges or different layers give distinct flipped-spin sets and hence orthogonal product targets. Their XX/YY relative phases cannot cancel. Edges crossing the transverse feature boundary create extra walls in the empty column and do not contribute to this N-preserving leakage from the flat long-interval state. The exact norm squared is consequently

||Q_rigid P_N V |flat>||^2
=4[Jx^2 (nx-1)ny + Jy^2 nx(ny-1)].

This refers to the physical first-order transverse Hamiltonian; if K1 is defined dimensionlessly, remove the corresponding coupling units. A direct 3 by 2, ell=3 set enumeration gives seven internal edges and 28 distinct targets, as predicted. For A=2 the single internal edge can move a whole flat end within the rigid subspace, so the exclusion A>2 is necessary. Positivity also presumes at least one internal edge with nonzero corresponding coupling.

This is instantaneous coefficient leakage from the rigid ansatz, not a lifetime, linewidth, or general collective-mode no-go. The complete many-height sector could contain nontrivial stationary states; it needs to be solved rather than replaced by the flat ansatz.

## Stronger original uniform-readout conclusion

For C=sum_(column,j) Z_j Z_(j+2), a single finite interval of length ell>=2 has exactly four mismatched distance-two pairs. Every mismatch changes the reference value by -2. Hence its C excess is -8, independent of interval length and position. For fixed occupied column set F with every column interval length>=2,

P_heights C P_heights=(C_vac-8A)P_heights.

There are no off-diagonal matrix elements because C is diagonal in this product basis; moreover all diagonal values coincide. Thus the projected *uniform bare readout is proportional to the identity* throughout this pure-height configuration space. After centering it is zero. It cannot excite internal endpoint-height modes at this level, even though their native Hamiltonian has nonzero matrix elements.

Length-one intervals have only two distance-two mismatches, with excess -4, so the identity fails if those states are admitted. It also requires endpoints away from physical longitudinal boundaries, no periodic wrapping/aliased bonds, and a single interval per column. A nonzero longitudinal Fourier readout is not constant under moving heights, because its bond-center phases distinguish endpoints. Dressing, transitions to excluded configurations, or a different specified observable can therefore change the source conclusion; none should be silently supplied.

Finally, the restricted fixed-F height space is not itself invariant under all physical plane flips. The full N projection respects those symmetries, but a selected reference/height chart need not. One must construct the appropriate sector states before assigning symmetry labels or calling a resulting mode neutral. No measured detector coupling or cosmological field connection follows from the present matrix rules.
