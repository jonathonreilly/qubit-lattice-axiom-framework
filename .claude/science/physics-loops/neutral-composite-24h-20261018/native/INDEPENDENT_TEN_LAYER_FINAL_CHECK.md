# Final focused check: ten-layer neutral bound block

Reviewed the current `native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md`, public note, runner and both executed helpers in `/private/tmp/scalar-environment-20261017`, together with `/tmp/neutral-ten-layer-transfer-check.md` and `/tmp/neutral-eighth-attraction-check.md`. No repository edits or formal audit were performed.

Disposition: no blocking issue found in the scoped claims. The two distinct conclusions—an actual finite-H zero-momentum atom in a selected symmetry fibre, and a positive-curvature coefficient-fibre dispersion—are explicitly kept separate in both the proof and the public note.

## Science and scope

The eighth-order attraction classification and coefficient agree with my preceding check. The sixth-order common thin excitation coefficient also checks: the single-plaquette term contributes 100L/9216 and the nearest-plaquette term contributes 81L/9216, totaling 181L/9216. Unknown higher common diagonal shifts remain explicitly unknown; they are not omitted to manufacture a numerical absolute frequency.

The positive curvature has order lambda^12 at height ten, whereas orientation mixing has order lambda^14. The stated q much smaller than lambda condition is necessary to select the infinitesimal symmetric branch. The logarithmic transverse boxes in the actual-pole transfer do not resolve that momentum scale. The proof expressly acknowledges this, and the public note repeats it. Thus the coefficient curvature is not being promoted to a resolved finite-H dispersion or a relativistic limit.

The actual pole statement is restricted to zero momentum and the exact C4-even positive-plane fibre. In that fibre the two shortest orientations leave a one-dimensional symmetric subspace, and the relevant next-thin gap is order lambda^8. The nearby C4-odd orientation state does not enter the restricted projector. The transfer check establishes the source expansion before applying the final projector, avoiding an insufficient estimate from the global uncentered source norm. This remains conditional on the inherited canonical reductions and their polynomial fixed-order bounds.

The source coefficient is correctly 2 gamma_L^2 beta_L^2/L, and the prepared local heavy vertex retains its 1/R^2 squared-overlap factor. The latter is explicitly a prepared, matched dressed channel, not an emission rate or relaxed-heavy scattering calculation.

Fixed-R all-positive ground selection is stated separately and does not remove the sector premise in the joint logarithmic-box family. This is appropriate: the R-dependent weak-coupling threshold has not been bounded uniformly. An actual finite-H spectral atom here is not a fixed-coupling infinite-volume isolated pole; its source weight tends to zero as lambda^20 at height ten. The proof does not claim otherwise.

## Reproducibility

I executed both helpers directly and independently repeated the runner's checks, without writing the runner's generated output directory. Both completed successfully. Exact loop outputs were -1/128, -3/8192, -9/262144 and -9/262144 for the four listed rectangles. The last 70-digit star-control row, lambda=.02, gave:

- Source weight 1.999999977734371 (normalized coefficient-graph source, not physical C weight).
- Curvature scaled 0.0000955552490617449, versus expected 0.00009555371232434279.
- Splitting scaled 0.000035831298049018594, versus expected 0.000035832642121628545.

These satisfy the runner tolerances. The exact physical source-weight rational coefficient also agrees with the independent transfer check. The helper uses mpmath at 70 digits and then serializes final values as ordinary floats; that is sufficient for the stated validation tolerances. Its below-band Green-function branch has the correct negative sign. The runner is genuinely executing the helpers rather than merely reading frozen numerical results.

The executed numerics establish only the exact local loop sums and the displayed coefficient-graph limits. They do not numerically replay the analytic full-H block-transfer theorem; the source manifest and prose identify its analytic dependencies. The failed double-precision curvature attempt is described as rejected, and no numerical result from that failed attempt is used as physical evidence.

Overall the current block is a conditional supplied-Hamiltonian result with derived attraction and source coupling. Height, anisotropy, units, empirical measurement identification and any cosmological connection remain unresolved premises, as stated.
