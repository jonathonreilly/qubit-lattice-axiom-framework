# Native neutral source identification

**Type:** bounded_theorem

**Status:** exact-support and conditional finite numerical support; unaudited.

Runner: [native_neutral_source_identification.py](../scripts/native_neutral_source_identification.py). The smooth-profile calculation explicitly reuses and hashes stationary_spatial.json from the preceding stationary-response milestone; this runner does not independently recompute that spatial response.

Neutral collective modes exist in the finite supplied compass model, but neither their existence nor an engineered energy-shift pattern derives the scalar source/detector coupling. This block constructs a protected-factor decomposition and explicit source/response diagnostics. One physical qubit per site and the original microscopic interaction are unchanged throughout.

## Protected-factor decomposition

On the open 3³ cube the binary plane-Pauli span has dimension eight and symplectic rank two. The Hilbert space has 64 central sectors, each a protected dimension-two factor times a dimension-2^20 multiplicity space. Native H and every plane-neutral observable act trivially on the protected factor. Plane averaging any density matrix preserves all neutral multitime correlations exactly. The retained equality concerns the stated neutral multitime correlators before and after plane averaging. Central-sector weights and the multiplicity state remain undetermined. The relevant neutral matrix elements equal an identity on the protected factor tensored with the multiplicity operator. This is an exact conditional reduction, not a vacuum-selection derivation.

## Finite ladder and source tests

Using the previously resolved neutral eigenvectors, root tests C transitions out of the first excited mode at gap 1.738972318272. A linear harmonic readout would have upper weight 2Z and lower weight Z. The upper Gaussian-window weight divided by 2Z is 3.67e-8, .15348, 1.93503 and 5.92201 for widths .02,.05,.1,.2. The harmonic target for this quotient is one. The 128/256-step values agree; nearby reconstructed eigenvectors have full-H residuals below 1.4e-13. The result challenges this isolated linear-harmonic identification through C, not an interacting scalar or nonlinear readout. A synthetic anharmonic oscillator control demonstrates that distinction. Widths are exposed diagnostics, not chosen to fit the harmonic answer.

For the three resolved modes, the summed existing local composites give fractional diagonal gap-response candidates .064476408,.582717534,.432206918. These three floating candidates differ; the proposed common-rescaling exclusion is deferred. Their interpretation as perturbative branch derivatives requires resolving degeneracies in both reference and excited branches. These modes are not identified with physical matter species, and this is not an equivalence-principle test.

An explicit observable family realizes common diagonal blocks with varying transition weights. For neutral Hermitian A, B=[H,[H,A]] vanishes on every equal-energy block. Thus O_alpha=H+alpha B has the same diagonal energy blocks as H while its inelastic transition weights vary with alpha². This remains true at degeneracy. For local A, two finite-range commutators expand support by at most two interaction steps; no nonlocal spectral projector is needed for the counterexample. These are constructed observables, not added interactions. The explicit 3x2x1 control gives thermal inelastic weights approximately zero,43.964765,703.436241 for alpha=0,.25,1 while preserving all energy blocks to 1.4e-14. The observable family and its distinct weights are the promoted constructive result; the source-nonidentifiability theorem is deferred.

## Scale and environmental limits

H(J)=J H(1). For observables carrying J powers a,b at a fixed dimensionless state, response scales as J^(a+b-1) times the response at omega/J. Gap and velocity both scale with J, so their ratio-defined length equals its J=1 value under the stated fixed-dimensionless-state hypotheses. Physical lattice spacing, time conversion and state remain imports.

Since sum_x e_x=H, the isolated stationary retarded response to a uniform energy source is exactly zero. An inversion-symmetric smooth profile on the fixed finite cube starts with its Hessian at order R^-2; the fourth-order remainder is bounded and checked. This is profile widening on a fixed cube, not bulk scaling. Reequilibrated Gibbs response instead has derivative beta Cov(C,H), checked separately: thermal reequilibration is an additional protocol, not the isolated retarded experiment.

## Scope and next constructive requirement

All numerical data here are exposed model-development data, not independent observations. Supplied H, geometry, state, physical units, bulk persistence and the operational source/detector mapping remain open. The positive next step is to compute how native feature/environment dynamics selects a neutral operator and its transition vertex, rather than choosing an observable to reproduce common shifts. Detailed proofs, inputs, synthetic controls and independent checks are in the campaign native pack. No TOE closure is claimed.


## Source package and execution provenance

The source package (`outputs/neutral_composite_review_2026_10_18/README.md`) preserves the mathematical arguments and lists the live helpers, declared inputs and deferred negative conclusions. Supporting proofs for this note are PROTECTED_PLANE_FACTOR.md (`outputs/neutral_composite_review_2026_10_18/proofs/native/PROTECTED_PLANE_FACTOR.md`), SOURCE_IDENTIFICATION_NULLSPACE.md (`outputs/neutral_composite_review_2026_10_18/proofs/native/SOURCE_IDENTIFICATION_NULLSPACE.md`), OVERALL_SCALE_BOUNDARY.md (`outputs/neutral_composite_review_2026_10_18/proofs/native/OVERALL_SCALE_BOUNDARY.md`), SMOOTH_ENERGY_SOURCE.md (`outputs/neutral_composite_review_2026_10_18/proofs/native/SMOOTH_ENERGY_SOURCE.md`), INTERNAL_LADDER.md (`outputs/neutral_composite_review_2026_10_18/proofs/native/INTERNAL_LADDER.md`), MODE_CHARGE_DIAGNOSTIC.md (`outputs/neutral_composite_review_2026_10_18/proofs/native/MODE_CHARGE_DIAGNOSTIC.md`). The primary runner hashes these source files as explicit inputs. Original campaign execution reports are historical provenance, not current execution or audit authority. Fresh bounded reproduction is recorded separately by the integration coordinator.
