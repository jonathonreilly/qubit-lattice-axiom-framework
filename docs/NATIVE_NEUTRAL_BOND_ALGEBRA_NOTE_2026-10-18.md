# Native neutral bond algebra and collective source search

**Type:** bounded_theorem

**Status:** exact finite operator algebra and conditional numerical support; unaudited.

Runner: [native_neutral_bond_algebra.py](../scripts/native_neutral_bond_algebra.py).

The supplied compass Hamiltonian already contains an algebra capable of expressing every plane-neutral Pauli feature on an open rectangular grid. This is a constructive search space for the user's large-feature approach, without adding a microscopic interaction. Algebraic generation does not derive a scalar particle, dynamics selection, preparation, or physical matter coupling.

## Exact classification

For H=-J sum_(x,a) sigma_x^a sigma_(x+e_a)^a, the product of sigma^a on each plane normal to a commutes with every native bond. Represent a Pauli string by binary X/Z fields u,v. Commutation with x bonds makes v independent of x; z bonds make u independent of z; y bonds make u+v independent of y. Consequently u=A(x)+B(y), v=C(z)+B(y), with one common-constant redundancy. On an open Lx by Ly by Lz grid, all dimensions at least2, the bond-set Pauli commutant therefore has dimension Lx+Ly+Lz-1 and is precisely the plane-symmetry span.

The binary Pauli symplectic form is nondegenerate. Double orthogonality shows that the native bond span is precisely the centralizer of all planes. Every plane-neutral Pauli string is a product of native bonds up to phase; general neutral observables are linear combinations. This is associative algebra generation, not Lie/Krylov reachability from a selected source, nor a statement that all these products are Hamiltonian terms. Exact binary controls through10³ sites check the rank identity; these are algebra controls, not spectra on1000sites.

For a state invariant under a conserved plane, two-point functions of operators with different plane signs vanish. Translation shifts the finite sign pattern by the corresponding displacement. The charged-feature infinite-grid immobility conclusion is preserved as a deferred negative theorem, outside this note's promoted scope. The finite charge selection identity and constructive neutral bond algebra remain live. Stationarity alone does not imply plane invariance; the symmetry-invariant state remains an explicit premise. In particular, the selected pure odd-cube CSS eigenvector is not invariant under all anticommuting individual planes. Gibbs or symmetry-averaged stationary states supply the finite-volume premise; no spontaneous-state selection is derived.


## More precise finite neutral spectrum

The [previous finite benchmark](NATIVE_STATIONARY_RESPONSE_NOTE_2026-10-18.md) used five commuting CSS stabilizers. Two adjacent Y-plane pair products give two additional independent commuting labels, reducing each2^22block to four2^20blocks. The exact signed-orbit map retains every native term and every tested neutral observable. Root10800intertwining controls and200independent physical-bit tests pass. A general phase formula was corrected during review; actual real18-Y generator results were unchanged.

The numerical initial state has both Y-pair signs positive. The next degenerate pair occupies the mixed-sign subspace, and the fourth vector has both signs negative. C preserves these signs, explaining their negligible centralC transition weights. This is not an inferred scalar gap or global-ground certificate.

Within the preserved++subspace,256Lanczos steps and direct reconstructed-vector residuals resolve gaps1.738972318272,2.132564259427,2.642077610056 with residuals approximately4.3e-14,3.2e-14,5.4e-14. Their centralC weights remain .003524947757,.000791489127,.00003066600008. These are finite27site numerical eigenpair diagnostics, not interval-certified eigenvalues, a bulk pole, or physical masses. The supplied starting vector/preparation and open geometry remain conditional.

## Collective source construction

Root forms connected source vectors from19nonzero localC operators and54native bonds in the same finite state. Covariance whitening retains eigenvalues above1e-10times the largest. The full local source space has rank72; cubic-invariant orbit sums have rank5. The lowest scalar variational excitation has energy6.70876 and full-H residual1.71075, so it is not the resolved low scalar-visible eigenvector.

All1287commuting distinct bond pairs partition into40cubic orbits. With3linear bond orbits the connected space has rank41. These are symmetrized quadratic products: squares center to zero and anticommuting anticommutators vanish. This is not completeness for every Hermitian quadratic expression such as i[A,B]. The lowest scalar variational energy falls to6.18076, residual1.27341. Cubic-invariant operator construction does not establish continuum particle spin or certify the state's symmetry.

For each already resolved eigenvector m, covariance whitening gives its orthogonal projection onto the kept source space. The squared projection is the maximum normalized overlap in that numerical space. For the lowest tested mode it rises from .00697486 for the localC/bond space to .07449410 for the symmetrized quadratic scalar space. The latter optimized source has mean excitation energy8.76748 and residual4.73145: improved overlap still leaves a broad spectral mixture. It is not a clean collective particle or a physical universal coupling. The coefficients are developed against the same model eigenvector, not fitted observations or an independent test.

Independent source review confirms orbit coverage, reduction, generalized Ritz and target-projection formulas. All detailed proofs, controls and limitations are in the branch-local native pack. No new physical qubit or interaction was introduced. No empirical dataset was used. Hamiltonian selection, physical state, bulk propagation, scales and source/detector identification remain open.


## Source package and execution provenance

The source package (`outputs/neutral_composite_review_2026_10_18/README.md`) preserves the mathematical arguments and lists the live helpers, declared inputs and deferred negative conclusions. Supporting proofs for this note are NEUTRAL_BOND_ALGEBRA.md (`outputs/neutral_composite_review_2026_10_18/proofs/native/NEUTRAL_BOND_ALGEBRA.md`), PLANE_MOBILITY.md (`outputs/neutral_composite_review_2026_10_18/proofs/native/PLANE_MOBILITY.md`). The primary runner hashes these source files as explicit inputs. Original campaign execution reports are historical provenance, not current execution or audit authority. Fresh bounded reproduction is recorded separately by the integration coordinator.
