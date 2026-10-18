# Dilute neutral-cluster Fock algebra

Disposition: PASS with the explicit projector and finite-particle hypotheses below. This is a kinematic statement about the specified native aligned-column code and motif operators, not a Hamiltonian eigenmode, statistics-of-all-excitations, or growing-occupation theorem. No repository edits or formal audit.

## Setup and essential monotonicity

Let the label a=(r,o) include x/y orientation if both are used. There are O(R^2) labels. A motif flips the two columns T_a and toggles a nonempty four-plaquette syndrome S_a. Let F_a be a fixed finite translated footprint containing S_a (and any desired positive-plaquette buffer), and define

 b_a^dagger = X_(T_a) P_(F_a,+),   b_a = P_(F_a,+) X_(T_a).

All constants below may depend on the fixed footprints and on a fixed maximum particle number m, but not R or the compatible flat character. Distinct labels must mean distinct motifs/syndromes; duplicate labels must first be identified. Take R sufficiently large compared with m and footprint diameters.

On a syndrome-basis vector with bad set C, a nonzero creation requires C intersect F_a empty. Its output syndrome is exactly C union S_a. Thus it increases the number of bad plaquettes by four. Conversely a nonzero annihilation requires S_a subset C and (C minus S_a) intersect F_a empty, and removes exactly S_a. In particular b_a annihilates the flat vacuum and b_a^dagger creates a unit vector. This monotonicity is crucial: an unrestricted X motif would permit repeated operations to erase pairs and produce macroscopically many coherent vacuum histories. Merely asserting commutation at disjoint supports would not suffice.

The flat-character orbit states reached here are orthonormal when their column-flip masks differ, modulo the flat group. For fixed m all differences have at most 4m flipped columns; if R>4m, a nonzero flat group element (minimum weight R) cannot identify them. Their syndrome determines the mask uniquely in this finite-flip class. All statements therefore hold uniformly in character.

## Bounded finite-sector operator norm

Write H_n for the span of reachable syndrome states with 4n bad plaquettes, allowing all configurations, including close ones. A configuration in H_(n+1) can have only C_n possible incoming creation labels: each S_a must be a four-site subset of its 4(n+1) bad sites, and each such finite pattern determines at most a fixed number of labels. For normalized f, Cauchy-Schwarz over these incoming labels gives

 ||B_f^dagger v||^2 <= C_n sum_C |v_C|^2 sum_(a eligible at C) |f(a)|^2
                         <= C_n ||v||^2,
 B_f^dagger = sum_a f(a) b_a^dagger.

The adjoint has the same norm between the corresponding sectors. This O_m(1) bound, rather than the crude sum |f|=O(R), is what makes full-vector error propagation valid. It also bounds the map from an ordered n-label coefficient tensor to the physical product: final histories have at most C_n multiplicity, because each of their disjoint four-site syndromes is contained in the final 4n-site set. Permutation factors are harmless at fixed n.

## Good configurations and collision estimate

Choose a finite-range incompatibility relation a~b wide enough that compatible motifs have disjoint footprints and their syndrome components are separated. Each label has at most z incompatible labels, with z independent of R. On mutually compatible distinct labels, all creations commute and the final syndrome decomposes uniquely into its motif components. The physical normalized state is therefore canonically identified with the corresponding ideal bosonic occupation vector. Denote this isometry on good configurations by J_n; set it to zero on the complement of the ideal boson space.

For normalized wavefunctions f_1,...,f_n satisfying max_a |f_j(a)| <= C/R, the unsymmetrized product measure has collision probability at most

 sum_(i<j) sum_a |f_i(a)|^2 sum_(b~a) |f_j(b)|^2
 <= binom(n,2) z C^2/R^2.

Symmetrization introduces only fixed-n constants. Hence the ideal bosonic product has bad-configuration norm O_n(1/R), whether or not the f_j are orthogonal. Applying the bounded physical history map to the same bad coefficient tensor shows

 || B_(f_1)^dagger ... B_(f_n)^dagger Omega
       - J_n a_(f_1)^dagger ... a_(f_n)^dagger |0> || <= C_n/R.

This includes all coherent overlaps of bad histories; no unsupported identification of amplitude norm with a classical collision probability is made. For finitely many orthonormal modes and any fixed occupation vector, divide by the usual sqrt(product n_j!) factors. Physical norms are 1+O_m(1/R), and their Gram matrix is I+O_m(1/R). The bound is sufficient and not claimed sharp.

## Full lowering and CCR

On a good configuration, a nonzero b_a removes exactly one existing motif. A spurious four-site syndrome cannot be assembled from distinct well-separated motif components. The leftover configuration is good. Thus physical and ideal lowering intertwine exactly on the good part. On its complement the finite-sector operator bounds above control the error. Consequently, for the unnormalized product Psi_n(f_1,...,f_n),

 B_h Psi_n = sum_(j=1)^n <h,f_j> Psi_(n-1)(f_1,...,omit f_j,...,f_n)
                 + e_n,       ||e_n|| <= C_n/R,

for normalized h; the product modes obey the stated infinity-norm bound. This is a full Hilbert-space vector estimate, including leakage into close or otherwise unwanted motif configurations, not just a selected matrix element.

For delocalized f,g and any state in the fixed finite span of these packet products, apply the lowering identity to B_g^dagger Psi_n and use the bounded creation norm on its error. It follows that

 ||([B_f,B_g^dagger]-<f,g>) Psi_n|| <= C_m/R.

Likewise the creation-creation and annihilation-annihilation commutators are O_m(1/R) on that prepared span. After normalizing occupation states, lowering has the usual sqrt(n_j) coefficient with O_m(1/R) full-vector error. Since only finitely many modes and occupations are retained, the estimates extend uniformly to their bounded-coefficient superpositions; their Gram matrix is uniformly invertible for large R.

## Scope and failure conditions

The proof requires the projector to include the complete toggled syndrome, fixed footprint size, fixed m and a fixed finite set of delocalized modes. It does not provide full-space operator-norm CCR, uniformity for growing m, or a claim that the motif is an energy eigenparticle. Internal-mode sums or extended motifs need their own uniform support/multiplicity bounds. Microscopic dressing and dynamical transfer must preserve the stated errors separately. The optional buffer changes the fixed exclusion relation but not the conclusion. Character superpositions are harmless for invariant operators with the same packet because exact sectors are orthogonal and all these constants are uniform.
