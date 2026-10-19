# Strong mixing and feature length: exploratory partial narrowing

Author: root, direct continuation requested by user. No new interaction or qubit per physical site. Independent review unavailable after existing workers reported usage limits; no audit verdict or retained claim. This is post-campaign work, not an extension of the closed 24-hour clock.

## Question and premises

Can the original native Hamiltonian select a stable finite feature size outside the weak-coupling expansion? Here we test H = -sum_x XX -sum_y YY -sum_z ZZ, in units J=1, on 2 by 2 by L grids. All couplings are equal: no weak-coupling truncation enters. The Hamiltonian, grid, selected symmetry sector, reference state and probe family remain adopted inputs. This is exposed model-development computation, with no calibration to or independent test against observations.

A physical string U[a,b] applies X on (x=0,y=0 or 1,z=a..b). Its even length ell preserves plane characters and acts on 2ell physical qubits. These are candidates for extended features, not assumed particles. The eight-dimensional rung tensor coordinate is an exact parity-sector representation of four physical qubits, not eight physical states added at a site.

## Exact nonperturbative identity

For an interior interval, Pauli conjugation gives

    U† H U - H = B_(a-1) + B_b,
    B_z = 2 sum_(y=0,1) Z_(0,y,z) Z_(0,y,z+1).

All XX terms commute with U. YY terms have either zero or two flipped sites. Interior ZZ terms also have zero or two; only the four bonds at the end cuts change sign. The operator norm of this difference is at most 8. This holds at arbitrary transverse coupling; it does not rely on a perturbative normal form. For an exact eigenstate g with energy E, (H-E)Ug=U(B_left+B_right)g. Hence the excitation-energy mean is the endcap expectation and its spectral variance is the endcap variance, bounded by 64.

In a longitudinally translation-invariant reference, the raw energy is independent of ell. In an open reference it samples the location-dependent endcut correlations. For every native bond away from the cuts, its energy expectation in Ug equals that in g exactly. Thus this family describes endpoint excitations linked by a string; a large flipped-site count alone is not a large region carrying excitation energy.

This is NOT a statement about all compact 3D features. The string fills the entire y width. A patch terminating inside a wider y direction has additional YY side-boundary terms. Neither this lemma nor these thin-grid calculations eliminate that route. Even in the thin geometry, off-diagonal mixing can bind endpoints; constant diagonal energy does not preclude a bound state.

## Full-H checks

`algebra_control.py` checks the four changed bonds for 450 open/periodic cases with L=4..32 and even interior lengths. All pass by integer Pauli support algebra.

`exact_size.py` solves the selected CSS sector on open grids of 16, 24 and 32 physical qubits. It forms centered sources (U-<U>)g and then adds their first full-H Krylov vectors. At L=8, the lowest projected energy falls from 5.702867 to 3.521989, but the corresponding full-H residual remains 2.425594. A Ritz eigenvalue is not a certified stationary feature. The L=4 and 6 residuals are also order one. This failure is preserved, not converted to a stability claim.

`mps_size.py` evaluates the same source family on 32, 48 and 64 physical qubits, using previously saved variational references and recomputing their full-H residuals. On L=16 the raw energy decreases from 6.929090 for ell=2 to 5.783950 for ell=14. The lowest projected state has largest normalized overlap with the longest available probe. The preferred tested length tracks the box. These overlaps are not probabilities over mutually exclusive sizes: the source basis is nonorthogonal.

`endcap_control.py` reproduces the raw energies from the exact identity. At L=16 the boundary-near cut expectation is about 2.891975, while central cuts approach 3.46462. This explains the open-grid apparent attraction toward long strings. Connected endcap covariance is recorded but is not an interaction potential; tiny values are not independently certified against MPS error.

`periodic_exact.py` restores the four native longitudinal wrap bonds and solves L=4,6,8 in the same selected sector. At L=8, E=-36.09464451590366 with residual 2.86e-10; raw string energies at ell=2 and 4 are 6.920552375525311 and 6.920552375520622. The open-boundary trend disappears. Boundary conditions are a diagnostic variation, not a new term in the bulk Hamiltonian.

`periodic_mps.py` extends the periodic diagnostic variationally. Every stage reports a full-H residual; energy convergence alone is insufficient. At L=8 the final energy is -36.09453840534206 and residual .041805, compared with the exact result above. Reported projected excitation energies do not include full Ritz residuals and cannot certify eigenmodes. See JSON for the completed larger sizes and all convergence failures.

## What remains to derive

No stable finite size has been selected by this block. No universal absence theorem follows. The decisive unresolved calculation is a genuinely compact, transversely growing feature and its relaxed quantum dressing, compared against separated and merged alternatives with controlled residuals and volume dependence. A stable size requires an interior optimum that persists as all boundaries recede, plus an eigenstate or lifetime argument. Larger longitudinal strings alone cannot supply that evidence.

The next useful route is to include finite-width side boundaries and quantum mixing in the original Hamiltonian, rather than introduce repulsion to obtain a desired minimum. Also open: endpoint binding after a much richer full-H Krylov treatment, other symmetry sectors and reference phases, excited-state metastability, and connection to observed matter/scalar coupling.

## Prior art and novelty boundary

Directional compass-model interactions and subsystem-symmetry consequences are established prior art: Nussinov and van den Brink, Rev. Mod. Phys. 87, 1 (2015), https://doi.org/10.1103/RevModPhys.87.1; Nussinov and Fradkin, Phys. Rev. B 71, 195120 (2005), https://doi.org/10.1103/PhysRevB.71.195120. The present work is a source-specific diagnostic and elementary conjugation derivation, not a claim to invent compass symmetries or prove a general no-go.

## Extension retaining the missing side boundaries

For a genuinely interior rectangular X patch at fixed x, width w in y and length ell in z, the same calculation gives 2ell changed YY bonds and 2w changed ZZ bonds, and no changed XX bonds. Thus U†HU-H is twice the native YY and ZZ terms' positive Pauli products on that perimeter. In a homogeneous reference with bond correlations C_y and C_z, its raw energy is exactly 4 J_y C_y ell + 4 J_z C_z w. Correlations and their signs are not supplied by this identity. For positive correlations, bare-patch energy rises with both dimensions, but this does not determine relaxed quantum binding or energy per constituent. The thin-grid family removed the YY side boundaries by spanning the width. `compact_patch_control.py` checks 56 interior even-by-even patches on wider grids by exact integer algebra. This extension identifies a native side-boundary contribution worth retaining in the next full quantum calculation; it adds no stabilizing interaction and selects no size by itself.

## Replay and source identities

`INPUTS.json` records exact hashes of inherited local states and source inputs. Open-reference binaries are local checkpoints, not embedded in this branch; the open-state replay therefore requires those files. Periodic and algebra scripts generate their states directly. Python dependencies: NumPy, SciPy, numba for sector calculations; quimb 1.15 for tensor calculations. The existing isolated tensor Python is `/private/tmp/neutral-tensor-venv/bin/python`. Run the periodic scripts from their saved paths; `check_results.py` cross-checks saved data without a tensor runtime. No claim that the local inherited binary inputs are a portable public dataset.

Seven direct four-physical-qubit parity-isometry/MPO checks in `rung_control.py` give zero algebraic error. This checks the representation independently of MPS optimization; it does not certify any optimized state. Exact open ED regenerates its L=8 reference if the inherited checkpoint is absent.

Initial periodic MPS L=16 and 24 (64 and 96 physical qubits) returned energy-converged flags but full-H residuals about 0.32766. Those states are explicitly not stationary certificates. L=12 reached residual 0.00813. `periodic_retry.py` reruns larger grids from wider random initial states with eight forced sweeps per stage; all outcomes, including incomplete convergence, remain in `periodic_retry.json`.

Retry outcome: L=16 reaches energy -72.17865200914464 and residual 0.0067296. Its raw string energies vary by only 2.36e-6 across ell=2,4,6,8, while its smallest restricted Ritz value is 6.199651; no excitation residual is certified. L=24 remains at residual 0.32765967 even with wider initialization and forced sweeps (actual bond47). This is a failed reference-convergence check, not evidence about stable size. No further enlargement is justified as a stationary-mode result in this packet.
