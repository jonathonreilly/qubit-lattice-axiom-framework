---
claim_id: native_mode_correlations_open_gate_note_2026-10-21
claim_type: open_gate
claim_scope: "Finite selected-sector spectral levels and native bond covariances under a supplied compass Hamiltonian. Excitation-family tracking, full returned spaces, relative-structure interpretation and growth in all dimensions remain open."
runner: scripts/native_compact_mode.py
---

# Compact-source-visible levels and native bond correlations

This package records a positive finite-volume result of a supplied one-qubit compass candidate and directly measures the resolved states' bond correlations. It is model-development evidence, with no fitted or independent observational data. The finite internal size of a physical feature remains the research target.

Claim type: open_gate. Primary runner: `scripts/native_compact_mode.py`. Companion primary runner: `scripts/native_longitudinal_mode.py`; it is also imported as a packet helper for complete source discovery. The scientific premises are included below. Original author certificates, plans, review narratives, interrupted attempts and exact source/cache/JSON bytes are preserved in `archive/native_mode_correlations_20261019/MANIFEST.json`; they are historical provenance, not this independent review or audit authority.

## Exact computational model

Take H=-sum_x XX-sum_y YY-sum_z ZZ with one qubit per site and J=1. The principal calculation uses 27 sites on a 3-by-3-by-3 periodic cube. Each direction has 27 distinct bonds. We fix every Z-plane character and every adjacent-X-plane-pair character to +1, giving an invariant subspace of dimension 2^22. The reference is the lowest returned eigenvector in that sector. Global-sector selection is a separate question.

Binary CSS coordinates implement an exact isometry; matrix-vector action uses every native bond, including the periodic seams. The independent physical-action control explicitly enumerates a 12-qubit graph, constructs the full-space isometry and compares H U with U H_reduced for two character choices. Both errors are zero. Reversing one YY coefficient produces error 1; omitting one wrap produces error .5. This is an implementation check on that graph, not an independent solution of the 27-qubit spectrum.

Two probes are products of X over 1-by-2-by-2 and 2-by-2-by-2 supports. For each, s=(U-<U>)g, with the entire returned ground subspace removed. Normalized overlap weights |<v_j,s>|²/||s||² identify source-visible levels. Near-degenerate returned weights are grouped before the cube visibility threshold is applied, and reported as captured weights, invariant under rotations within that returned span; a full degeneracy certificate is not supplied.

## Positive spectral result

The previously obtained level at gap approximately 1.423237955386 J is reproduced with an expanded 16-vector eigensolve. Original successful cube results, full-H residuals and weights are in the [numerical receipt](../outputs/native_mode_correlations_20261019/exact_cube_poles.json). The ground energy is approximately -38.191649892398 J. The two returned vectors at that level have maximum full-H residual 3.06e-13 J. Captured normalized probe weights sum to .01961581498535 and .001179426989425. Both probe supports have nonzero overlap with the level. The calculation therefore supplies a numerically resolved finite-sector eigenstate for further structural measurements without introducing a collective coordinate or another interaction.

A chosen probe support does not measure an internal radius. The periodic box has only three sites per direction; its odd seams, available wavelengths and selected sector are explicit parts of this result. No scalar irrep, constituent count, rest mass, scattering threshold or infinite-volume pole is assigned.

## Bond correlations measured from the states

Use the native bond observable B_r=Z_r Z_(r+e_z). For the ground state and rho=P_returned/rank on the resolved level's returned span, calculate

    C(r)=Tr(rho B_0 B_r)-Tr(rho B_0) Tr(rho B_r).

The [correlation receipt](../outputs/native_mode_correlations_20261019/correlations.json) stores every displacement, each bond mean, C, and the difference from the ground. The computation uses (B_0 v)^T(B_r v), valid for these commuting Hermitian observables. It checks C(0)=1-<B_0>². A separate dense density-matrix implementation agrees within 1.2e-16 and detects omission of the centering term.

For example, C(0) changes from .7776860 in the ground to .7939466 in the returned-mode mixture; C(1,0,0) changes from .1043131 to .0667871; C(1,1,1) changes from .0022711 to .0103329. The mixed-state bond means are spatially uniform to about 1e-13 in this run. These are reproducible state-structure diagnostics within this box.

This is the covariance of the mixed state, including variation of expectations across its components; it need not equal the average of pure-state connected covariances. Signed excess correlations are not a distribution of constituent separation. Center-of-mass structure and incomplete returned eigenspaces remain possible contributions. We do not fit a radius or supply a selected feature size.

## Larger longitudinal controls

The [longitudinal calculation](../scripts/native_mode_longitudinal.py) extends native boxes to 3-by-2-by-L with open x/y and periodic z boundaries. Its sources span the full two-site y width. This is controlled growth in one direction, not a three-dimensional bulk limit or a continuation certified to be the same excitation as the periodic cube.

For each box it reports the low spectrum, full residuals, captured weights and the anchor-averaged longitudinal covariance. The first visible levels on L=3 and L=4 have gaps approximately .4375815 J and .1816249 J. Selecting the lowest visible level separately can switch excitation branches. Consequently these numbers are reported as finite-box observations of the model rather than a stable-size trend. The [longitudinal receipt](../outputs/native_mode_correlations_20261019/longitudinal.json) records the completed sizes; the historical OPERATIONS.md bytes in the archive separately preserve the resource interruption.

## Dependency and proof obligations

The exact CSS isometry and native Pauli signs are implemented here and independently checked on a finite full-space graph. The residual identity ||Hv-Ev|| supplies the numerical eigenpair check; normalized spectral overlaps and the displayed covariance follow directly from finite-dimensional linear algebra. All helpers are included in this PR. No unmerged ancestor conclusion is needed for replay.

The strongest missing scientific step is a consistently identified excitation family with an operational relative-structure observable, converged residuals and volume dependence as every spatial dimension grows. This is the original open target, not a claimed reduction that has solved it. The proposed next calculation resolves momentum and full degenerate spaces before tracking bond spectral weight and relative correlations.

## Explicit premises


- Supplied native compass candidate H=-sum_x XX-sum_y YY-sum_z ZZ, one physical qubit/site, unit energy scale. Provenance: current-main native composite transport note, evaluated at K=-1. The minimal axioms do not uniquely select this candidate or sign/scale.
- Finite geometry and boundary conditions are supplied computational controls. The 3-cube is periodic in all directions; 3-by-2-by-L controls are open transversely and periodic longitudinally. Odd seams and the thin transverse direction are part of the tested models.
- All selected Z-plane and adjacent-X-plane-pair characters are +1. This is an invariant sector; the global ground sector is not certified.
- The lowest returned eigenstate supplies the reference. X-product patches are supplied probes. Both remain physical-preparation inputs.
- Euclidean eigenvector norm, eigensolver tolerances and visibility thresholds are numerical conventions. No observed energy, mass or radius is fitted.
- Connected native bond covariances are state diagnostics. A probability of relative constituent separation, scalar transformation law, continuum threshold and finite internal size remain to be constructed and checked.

## Replay, identities and review boundary

Run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=4 PYTHONDONTWRITEBYTECODE=1 python3 scripts/native_compact_mode.py` from repository root with NumPy, SciPy and numba installed. It runs physical mapping and covariance controls, solves the cube afresh, and computes correlations in memory. The canonical runner envelope has a 1800-second cap. Peak memory is several GB; no prior binary or archive member is required. JSON outputs go under `outputs/native_mode_correlations_20261019/`. All seven helpers are durable `scripts/native_mode_*.py` modules. Helper metadata caps bound review declarations; an enclosing primary-runner capture enforces its aggregate cap.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/native_longitudinal_mode.py` for L=3,4 under its 120-second primary capture cap. The optional `--lengths 3 4 5` asks for the resource-heavier 30-qubit extension; the original interrupted attempt supplies no L=5 result and this packaging does not execute it.

The original cube runner cache and its complete original source closure are preserved byte-for-byte in the archive. They bind the original paths and hashes only. Moving helpers and adding the canonical note changes the invocation identity; the old cube cache is not relabeled fresh. No new several-GB cube replay is claimed by this packaging. The displayed cube JSON is the original recorded result. A source-closure receipt may validate the current package without establishing fresh cube execution; fresh cube replay remains explicitly pending. The original environment.json likewise describes that historical run. The inexpensive longitudinal runner is recaptured separately against final current source. Its result is not evidence of a new cube solve.

The prior author's focused review is historical, not the present independent source confirmation. Independent current review checks packaging, model/implementation preservation and evidence identities; formal audit and combined integration checks are separate. The earlier broad compact-patch/MPS block remains on its original branch and is not a premise here.
