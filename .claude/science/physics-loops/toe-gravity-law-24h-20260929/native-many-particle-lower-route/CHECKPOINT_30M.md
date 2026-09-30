# First checkpoint: exact lower comparison, not EOS

The frozen small control succeeded (capacity_controls.json): literal N2
symbol error8.88e-16; actual N3/N4/N6 identity max7.11e-15; capacities and
35+35 background block inequalities hold in all tested instances. CPU4.48221s,
wall4.512936s,RSS117915648B. No failed run or increased budget.

The positive route has advanced to an actual all-N lower comparison:
H=mu D+T†direct_sum(K2)T, with the near-isometric single-pair extraction.
Hard-core output constraints yield a finite matrix capacity for every
occupation background, no denominator at extensive many-body energy.
A smooth high-frequency split gives Green kernel
|G_kappa(r)|<=C_m(1+|r|)^-1(1+kappa|r|)^-m. For background dimers separated
byR, off-block row sums are O(R^-1+kappa^-2 R^-3), uniformly in their number
and volume. Their block diagonals converge to fixed35-pin infinite-lattice
Green matrices. This gives a controlled positive physical lower form after
retaining low-frequency kinetic energy. Details are being written in full.

The local pinned-box estimate implies a mesoscopic crowding bound
B_R<=C R^3 H/a for particles outside R-isolated physical dimers, with a safe
explicit C to be checked in the final report. Pair removal cannot destroy
an already R-isolated dimer except by deleting that whole dimer. Therefore
the residual-background bad-particle fraction is O(R^3 E/N), not a presumed
small global Q norm. R=rho^-1/4 and kappa=rho^1/3 make both the fraction and
the block error small. The discarded higher clusters can still carry a
leading energy fraction; this is NOT an EOS identification.

A new threshold consequence appears to be T0 >= [4a/(21g)] I_15,
g=int_BZ ell(k)^-1 dk/(2pi)^3 <=sqrt(3)pi/8. The proof uses the all-N
capacity inequality at N4, compact corrections, and exact far incoming
normalization sqrt2 A u_edge; it does not compute T0. This factor proof is
still under adversarial checking before final freeze.

An exact reset-channel family is being derived to distinguish actual ground
states from merely low-energy states. Rare guarded K6 motifs and two odd
triangles can be added to the exact pair-pulse/threshold-upper state at
probability delta*u^4 per fixed box. The density stays2u^2+O(u^4), energy
O(u^4), but higher clusters have positive order-rho^2 density and global
isolated-dimer/perfect-matching projections tend to zero. This would refute
those precise uniform shortcuts, not a ground-state phase or lower theorem.

Next: complete matrix kernel proof and reset constants, audit every scope
and pair factor, then freeze the scoped lower-comparison report for a fresh
independent check. The leading EOS/ODLRO target remains open.
