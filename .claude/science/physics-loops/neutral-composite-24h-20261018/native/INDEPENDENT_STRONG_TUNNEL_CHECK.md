# Independent minimal strong-longitudinal tunneling check

The stated coefficient and path completeness are correct for an open longitudinal chain, Jz>0, finite L, and the aligned-column low band of the positive-rung-parity tube. This is a finite weak-Jperp/Jz statement, not an isotropic or bulk conclusion. I inspected /private/tmp/neutral_strong_tunnel.py; it explicitly uses L−1 longitudinal bonds, so the open-end assumption is essential.

## Completeness and denominators

The target differs from the starting aligned configuration at exactly 2L physical sites, the two endpoints of one transverse edge on every rung. Each elementary transverse perturbation flips exactly two physical spins. A length-L sequence reaching that target therefore flips every target site exactly once and no other site. Consequently its edge on every rung must be the target edge; another transverse edge cannot contribute at this minimum order. The only freedom is the permutation of rung positions. No proper intermediate subset is in the aligned-column low band. With S the flipped rungs, each longitudinal domain wall changes two ferromagnetic bonds from −Jz to +Jz, costing 4Jz w(S). Thus every denominator E0−E(S) is −4Jz w(S), with w(S)>0 for nonempty proper subsets of the open chain.

Every X-edge matrix element is −Jperp. Its L vertices and L−1 negative denominators give an overall negative amplitude. Folded/reducible effective-H terms cannot modify this first off-diagonal coefficient: any low-band return uses operations without advancing the minimum Hamming distance to the target, so reaching the target then needs more than L operations. Lower-order energy shifts also enter denominators only at higher order.

## All-L path-sum proof via an explicitly derived subproblem

Retain only that one transverse edge. In the two-column subspace accessible from the starting configuration, define tau_z(j) to mark whether both endpoint spins on rung j have been reversed. Their two longitudinal bond energies sum to

H_edge=−K sum_(j=1..L−1) tau_z(j) tau_z(j+1)−h sum_j tau_x(j)+constant,

where K=2Jz and h=Jperp. For a Y edge its local sign can first be gauged into h; see below. This restriction is used solely to sum the just-proven complete minimum-order paths, not to discard other edges in the full theory at higher order.

For completeness the free-fermion reduction needs no imported spectral theorem. Set a_j=(prod_(l<j) tau_x(l)) tau_z(j) and b_j=(prod_(l<j) tau_x(l)) tau_y(j). Direct Pauli multiplication gives i a_j b_j=tau_x(j) and i b_j a_(j+1)=tau_z(j)tau_z(j+1). The resulting real a-to-b coupling matrix B is bidiagonal, with diagonal entries of magnitude h and adjacent entries of magnitude K. Its singular values sigma_j give independent fermion excitation energies 2 sigma_j by orthogonal rotations of the a and b Majoranas.

At h=0, B has L−1 singular values K and one zero. Since |det B|=|h|^L, their product identity yields

sigma_min=|h|^L/K^(L−1) [1+O((h/K)^2)]

for each fixed L>=2. The two lowest Ising states have splitting 2 sigma_min, hence off-diagonal aligned-state matrix element of magnitude |h|^L/K^(L−1). Its sign is fixed by the negative minimal paths above. Therefore

t_edge=−Jperp^L/(2Jz)^(L−1).

Equating this with the complete perturbative path expansion proves the exact combinatorial identity for all L, not just the enumerated L2..16:

sum_(permutations pi) prod_(m=1..L−1) [1/(4 w({pi1,...,pim}))]=2^(1−L).

The Python dynamic-programming recurrence is precisely this subset recurrence. L=1 has a direct first-order matrix element and is outside its domain-wall recurrence, but agrees with the natural coefficient formula.

## Y phase and parity

On a computational Z configuration, Y_a Y_b contributes the real factor −z_a z_b relative to X_a X_b. Reversing both endpoints preserves z_a z_b; before their unique flip at any rung the factor is the same initial aligned-column value. The total extra factor is (−z_a z_b)^L. For even L it is +1, so both physical edge types induce the same-sign effective column X-pair flip. For odd L it is −z_a z_b, precisely the matrix-element phase of a column Y-pair. This is a parity effect in the logical column representation; it does not replace the microscopic Y bonds by X bonds as operators on the full Hilbert space.

All these intermediate edge operations preserve positive rung parity. The aligned low band has four column signs constrained by their product +1, giving eight states. The local calculation is therefore compatible with that sector.

## Diagonal degeneracy and limits

The aligned configurations remain symmetry-equivalent for diagonal effective matrix elements. Physical conserved X planes flip the two columns at fixed transverse x, and Y planes flip the two at fixed transverse y, possibly with phases. The four associated flip masks span the three-dimensional even-column-flip space and act transitively on the eight aligned configurations. The low projector is invariant under these symmetries. A symmetry-equivariant canonical effective Hamiltonian consequently has equal diagonal entries on these aligned computational configurations. This does NOT mean its eigenvalues remain degenerate: the computed off-diagonal tunneling splits the band. It also does not remove higher-order non-diagonal terms or prove that the leading four-edge effective Hamiltonian is exact.

The leading coefficient is finite-L perturbation theory around an isolated band. A uniform expansion in L or control at Jperp=Jz has not been supplied. Periodic longitudinal boundaries change wall counting and the small-singular-value problem, so this coefficient must not be reused there without a new derivation. None of the calculation selects the full physical parity sector, identifies a scalar mediator, or supplies a cosmological source/detector coupling.
