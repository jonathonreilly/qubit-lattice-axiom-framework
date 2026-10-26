# Compact-source-visible levels and native bond correlations

This package reproduces a positive finite-volume result of the unchanged one-qubit compass candidate and directly measures of the resolved states' bond correlations. It is model-development evidence, with no fitted or independent observational data. The finite internal size of a physical feature remains the research target.

The [claim-status certificate](CLAIM_STATUS_CERTIFICATE.md) records `open_gate` / `open`; the [trace](TRACE_GATE.md) names the consumer. The [premise ledger](ASSUMPTIONS_AND_IMPORTS.md) separates the supplied Hamiltonian, scale, finite geometry, state and probe from calculated consequences.

## Exact computational model

Take H=-sum_x XX-sum_y YY-sum_z ZZ with one qubit per site and J=1. The principal calculation uses 27 sites on a 3-by-3-by-3 periodic cube. Each direction has 27 distinct bonds. We fix every Z-plane character and every adjacent-X-plane-pair character to +1, giving an invariant subspace of dimension 2^22. The reference is the lowest returned eigenvector in that sector. Global-sector selection is a separate question.

Binary CSS coordinates implement an exact isometry; matrix-vector action uses every native bond, including the periodic seams. The independent physical-action control explicitly enumerates a 12-qubit graph, constructs the full-space isometry and compares H U with U H_reduced for two character choices. Both errors are zero. Reversing one YY coefficient produces error 1; omitting one wrap produces error .5. This is an implementation check on that graph, not an independent solution of the 27-qubit spectrum.

Two probes are products of X over 1-by-2-by-2 and 2-by-2-by-2 supports. For each, s=(U-<U>)g, with the entire returned ground subspace removed. Normalized overlap weights |<v_j,s>|²/||s||² identify source-visible levels. Near-degenerate returned weights are grouped before the cube visibility threshold is applied, and reported as captured weights, invariant under rotations within that returned span; a full degeneracy certificate is not supplied.

## Positive spectral result

The previously obtained level at gap approximately 1.423237955386 J is reproduced with an expanded 16-vector eigensolve. Fresh results, full-H residuals and weights are in the [numerical receipt](../../../../outputs/native_mode_correlations_20261019/exact_cube_poles.json). The ground energy is approximately -38.191649892398 J. The two returned vectors at that level have maximum full-H residual 3.06e-13 J. Captured normalized probe weights sum to .01961581498535 and .001179426989425. Both probe supports have nonzero overlap with the level. The calculation therefore supplies a numerically resolved finite-sector eigenstate for further structural measurements without introducing a collective coordinate or another interaction.

A chosen probe support does not measure an internal radius. The periodic box has only three sites per direction; its odd seams, available wavelengths and selected sector are explicit parts of this result. No scalar irrep, constituent count, rest mass, scattering threshold or infinite-volume pole is assigned.

## Bond correlations measured from the states

Use the native bond observable B_r=Z_r Z_(r+e_z). For the ground state and rho=P_returned/rank on the resolved level's returned span, calculate

    C(r)=Tr(rho B_0 B_r)-Tr(rho B_0) Tr(rho B_r).

The [correlation receipt](../../../../outputs/native_mode_correlations_20261019/correlations.json) stores every displacement, each bond mean, C, and the difference from the ground. The computation uses (B_0 v)^T(B_r v), valid for these commuting Hermitian observables. It checks C(0)=1-<B_0>². A separate dense density-matrix implementation agrees within 1.2e-16 and detects omission of the centering term.

For example, C(0) changes from .7776860 in the ground to .7939466 in the returned-mode mixture; C(1,0,0) changes from .1043131 to .0667871; C(1,1,1) changes from .0022711 to .0103329. The mixed-state bond means are spatially uniform to about 1e-13 in this run. These are reproducible state-structure diagnostics within this box.

This is the covariance of the mixed state, including variation of expectations across its components; it need not equal the average of pure-state connected covariances. Signed excess correlations are not a distribution of constituent separation. Center-of-mass structure and incomplete returned eigenspaces remain possible contributions. We do not fit a radius or supply a selected feature size.

## Larger longitudinal controls

The [longitudinal calculation](longitudinal.py) extends native boxes to 3-by-2-by-L with open x/y and periodic z boundaries. Its sources span the full two-site y width. This is controlled growth in one direction, not a three-dimensional bulk limit or a continuation certified to be the same excitation as the periodic cube.

For each box it reports the low spectrum, full residuals, captured weights and the anchor-averaged longitudinal covariance. The first visible levels on L=3 and L=4 have gaps approximately .4375815 J and .1816249 J. Selecting the lowest visible level separately can switch excitation branches. Consequently these numbers are reported as finite-box observations of the model rather than a stable-size trend. The [longitudinal receipt](../../../../outputs/native_mode_correlations_20261019/longitudinal.json) records the completed sizes; OPERATIONS.md separately preserves the resource interruption.

## Dependency and proof obligations

The exact CSS isometry and native Pauli signs are implemented here and independently checked on a finite full-space graph. The residual identity ||Hv-Ev|| supplies the numerical eigenpair check; normalized spectral overlaps and the displayed covariance follow directly from finite-dimensional linear algebra. All helpers are included in this PR. No unmerged ancestor conclusion is needed for replay.

The strongest missing scientific step is a consistently identified excitation family with an operational relative-structure observable, converged residuals and volume dependence as every spatial dimension grows. This is the original open target, not a claimed reduction that has solved it. The proposed next calculation resolves momentum and full degenerate spaces before tracking bond spectral weight and relative correlations.

## Replay and review record

Run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=4 python3 scripts/native_compact_mode.py` from repository root with NumPy, SciPy and numba installed. It independently checks the physical mapping and covariance algebra, solves the cube afresh, then computes correlations in memory. Peak memory is several GB; no binary from an earlier branch is required. JSON receipts are generated under `outputs/native_mode_correlations_20261019/`. The canonical envelope in `scripts/runner_cache.py` pins all declared helper source bytes and captures live stdout.

Run `python3 scripts/native_longitudinal_mode.py` for L=3,4. The optional `--lengths 3 4 5` requests the resource-heavier 30-qubit extension, which was interrupted in this author run and supplies no result. A source provenance and conformance record appears in [REVIEW_HISTORY.md](REVIEW_HISTORY.md). An independent focused reviewer checked the Hamiltonian construction, periodic bonds, covariance interpretation and mutation controls. No formal audit or retained status is claimed. The earlier broad compact-patch/MPS block stays on its original branch; this PR isolates the self-contained exact spectral and correlation result.
