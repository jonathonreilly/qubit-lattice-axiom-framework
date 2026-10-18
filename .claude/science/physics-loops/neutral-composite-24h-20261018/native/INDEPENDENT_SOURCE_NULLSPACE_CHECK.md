# Independent source-identification nullspace check

Reviewed `native/SOURCE_IDENTIFICATION_NULLSPACE.md` and `neutral_source_ambiguity.py`. The mathematical construction and full degenerate-block claim are correct. No repository files were changed, no formal audit was applied, and the finite-control spectrum was not promoted to an observed result.

## Full blocks, not just diagonal matrix elements

For spectral projectors P_E and Hermitian A,

P_E [H,[H,A]] P_F=(E−F)² P_E A P_F.

The operator B=[H,[H,A]] is Hermitian and vanishes on ENTIRE equal-energy blocks. Consequently O_alpha=H+alpha B satisfies P_E O_alpha P_E=E P_E for every real alpha. Under H_lambda=H−lambda O_alpha, degenerate perturbation theory diagonalizes −P_E O_alpha P_E, which is already −E times identity. Every branch emerging from that whole eigenspace therefore has first derivative −E, without needing to choose a preferred basis within the degeneracy. All first-order gap slopes are −(E_n−E_0). Higher-order energy shifts generally differ with alpha; the result is first order, not exact finite-lambda spectral rescaling.

For unequal energies, O_alpha,EF=alpha(E−F)² A_EF. In a fixed stationary state of the unchanged H, inelastic AUTO-spectral weights of O_alpha therefore scale as alpha² and vanish at alpha=0. A cross response to another fixed observable generally scales linearly with alpha instead. The note's quadratic phrase should be read specifically as this auto/inelastic-weight statement; it is not a universal statement about every possible measured cross response.

For a finite spectrum, prescribing P_E O P_E=(aE+b)P_E leaves precisely an arbitrary Hermitian off-diagonal-block operator B. Set A_EF=B_EF/(E−F)² for E different from F, and choose equal-energy blocks freely (zero is sufficient). This gives B=[H,[H,A]]. This is a complete finite-dimensional algebraic characterization under the stated full-block requirement. Observing only a few diagonal slopes would impose still weaker restrictions.

## Support, symmetry and units

If A has finite spatial support and H is a sum of finite-range bond terms, [h_b,A] is zero for disjoint support. A second commutator can enlarge the original support by at most two interaction neighborhoods. Thus B is local in this finite-range sense, with no spectral inverse required for the forward construction. Summing translated local A produces a corresponding extensive local sum, with boundary terms treated according to the actual graph.

If a plane symmetry commutes with H and A, it also commutes with both nested commutators. The neutral construction remains in the native-bond associative algebra when A belongs to that algebra; the previously established plane-centralizer theorem supplies this for plane-neutral Pauli combinations on the stated complete rectangular native geometry. In the specific 3x2x1 control, A is explicitly built from squared local energies and hence from bond products directly, so no extension of a three-dimensional classification theorem is needed.

An antiunitary time reversal that leaves H and A even also leaves the double commutator even. There is no explicit i in [H,[H,A]], so no missing antiunitary sign occurs. Equivalently D=i[H,.] maps even to odd and D² maps even to even, with B=−D²A. Imposing time-reversal evenness therefore does not remove these null directions.

If H has energy units and A is dimensionless, B has energy-squared units and alpha must have inverse-energy units for O_alpha=H+alpha B to be homogeneous. The J=1 control uses numerical units; alpha remains a free construction parameter, not a derived scale or coupling.

## Inverse locality and state limits

The algebraic inverse divides by energy differences and generally produces a nonlocal A even when B looks simple. Its norm can grow without bound as gaps close or volume increases. Therefore the full finite spectral parameterization is not a classification of all LOCAL source ambiguities in the thermodynamic theory. Conversely, choosing any local A first already supplies explicit local ambiguities whenever its double commutator is nonzero. No inverse-locality claim is needed for that constructive result.

The construction does not add a term to the native H. Actually coupling a new source through O_alpha would be an additional microscopic/operational hypothesis. The diagnostic establishes that universal first-order energy slopes alone do not select that hypothesis or its transition residues.

## Numerical-control review

The supplied control uses H as a real dense native matrix, builds partial C through 2e_x²−d_x I/2, computes B by nested matrix multiplication, and groups equal energies with tolerance 1e−9. The double-commutator spectral identity and all full-block residuals are checked, not merely each diagonal. Its thermal weight sum excludes equal-energy blocks; since absolute matrix-element squares are symmetric for Hermitian O, weighting rows rather than columns gives the same total inelastic weight. This is the full thermal dynamic-structure inelastic weight, not a positive-frequency retarded spectral weight, which would need population differences and frequency restriction.

An independent six-dimensional COMPLEX Hermitian test with deliberate twofold degeneracies verified the block identity and all equal-block zeros, and gave inelastic weights 0, 29.9093234765, 478.5491756242 at alpha=0,0.25,1, with ratio exactly 16 at floating precision. This independently checks the algebra beyond the real native-matrix special case; it does not independently reproduce the root's native numeric values.

The note's source-identification conclusion is justified: matching universal diagonal first-order shifts does not determine off-diagonal dynamical coupling. It is not a scalar/gravity no-go and does not choose the missing physical source/detector mechanism.
