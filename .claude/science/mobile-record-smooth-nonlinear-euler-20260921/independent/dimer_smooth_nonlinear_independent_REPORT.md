# Bounded review of the smooth nonlinear Euler theorem

**Disposition:** no actionable mathematical gap or consequential source/code
discrepancy found. The supplied proof establishes its conditional
fixed-winding, smooth-time hydrodynamic conclusion under the stated
hypotheses. This is an independent scientific proof assessment, not a
formal audit or retained-status decision.

The complete source was reconstructed before any author checker or result
was accessed. The prior nonlinear flux and initial-drift packet was already
sealed; its algebra and the unchanged actual rate premises were reused by
identity. Neither the initial-derivative result nor the earlier stationary
fluctuation theorem was treated as a proof of this extension. The new
load-bearing estimates were checked directly. No primary source, earlier
packet, Git state or audit record was changed.

## Five load-bearing steps

1. **Entropy dissipation and fixed block gaps.** The homogeneous product
   reference is invariant by the route-cycle sum of the antisymmetric
   drive. Detailed balance is unnecessary. With the displayed bare
   Dirichlet convention, the entropy bound is exactly
   `H(mu|pi)' <= -2 N r_* D_N(sqrt(f))`. Its integrated bound is O(K/N).
   The rectangular blocks use three actual route displacements that
   generate the black sublattice; their bare swaps are irreducible within
   each fixed color-count sector. Finitely many sectors at fixed block
   size give a positive minimum gap. No uniform bound as the block grows
   is assumed or needed in the ordered limits.

2. **Conditional one-block current replacement.** The source conditions
   the uniform reference measure on exterior colors and block counts,
   rather than assuming the actual conditional law is uniform. Writing
   `f=g^2`, subtracting `(E_B g)^2`, and applying two Cauchy-Schwarz
   inequalities gives the stated factor `2 ||V||_infinity`. Together with
   the block gap, edge multiplicity and integrated dissipation this gives
   `K C_(ell,T)/sqrt(N)`. Canonical four-site sampling differs from product
   sampling by at most C/m via repeated-index coupling, including boundary
   count vectors. Current boundary loss and coefficient translation cost
   O(1/ell) and O(ell/N). This is an expectation-level time-integrated
   replacement; that is sufficient for the entropy proof.

3. **Entropy cancellation.** The exact log-product generator difference
   has the correct sign and Euler factor. The outer half rate in the
   homogeneous current cancels against the route tensor
   `(1/2)sum a_delta tensor delta=I`. The constant spatial term is a
   periodic divergence using the already verified entropy flux. The
   linear term cancels on the mass-zero tangent space using the PDE and
   the entropy symmetrizer. It need not vanish as an ambient
   fourteen-vector. The remaining cubic-flux Taylor error is bounded by
   the sum of squared block-density deviations, even when an empirical
   block density touches the simplex boundary.

4. **Product exponential bound and Gronwall.** The coordinate Hoeffding
   bound, fourteen-coordinate union bound and tail integration give
   exactly 28 exp(-s/7) and 29. The overlap graph has at most
   `(2ell-1)^3-1` neighbors. A coloring with 8m slots is valid on finite
   tori without an exact block tiling. Holder's inequality with
   alpha=1/224 gives `2 alpha (8m)=m/14`. Crucially, the resulting
   coefficient of the relative entropy is independent of ell. Gronwall
   at fixed ell, followed by N tending to infinity and then ell tending
   to infinity, proves the uniform entropy-density conclusion without
   assuming a quantitative gap law.

5. **Uniform-time empirical convergence.** Fixed-time product concentration
   transfers by the entropy event inequality. A smooth empirical test has
   jumps O(1/(N K)), uniformly bounded drift, and martingale bracket
   O(1/(N K)) on the Euler time interval. Doob's inequality and a fixed
   time mesh yield the stated supremum-in-time probability limit. No
   pathwise current-replacement statement is smuggled into this step.

`INDEPENDENT_DERIVATION.md` contains the complete reconstruction, including
the Bernoulli moment bound, count-conditioning calculation, periodic block
geometry, Riemann normalization and the limiting order. Small blocks with
no internal four-site stencil can be omitted in the final ell-to-infinity
limit, or their averages normalized by all m sites as allowed in the
source; no estimate needs division by an empty stencil set.

## Decisive independent controls

Before comparison, the standalone `independent_check.py` assembled all
14^4 states of one actual four-anchor N=8 owner-route cycle, with
gamma=2/3 and k0=5/2. Its integer stationary balance residual is zero and
rates range from 11/12 to 19/12. For a correlated positive density, the
Euler entropy derivative is -51.5968, below its correctly normalized
-14.8546 bound; the exact inhomogeneous-reference decomposition has zero
floating-point residual in this control. All 2380 count sectors are
retained in the conditional variance calculation.

The independent checker computes exact bare four-cycle spectra for every
partition of four color counts. Relabeling covers all fourteen-color count
sectors of that cycle; the nontrivial gaps equal two. These finite cycle
calculations test the local identities and conventions. They do not replace
the general connected rectangular-block argument.

Two countercontrols test premises that could otherwise be overlooked:

- A density depending only on one color's count has zero swap Dirichlet
  energy, while an incorrectly grand-canonically centered observable has
  expectation 13/252. Thus count-sector centering is essential. The source
  uses the correct centering.
- At a separately chosen rational profile and gradients, the linear entropy
  coefficient is the nonzero constant vector `(64/15015) one`. Its tangent
  pairing is exactly zero. The source correctly requires only that pairing.

Independent periodic block checks use N=24,40,48,80 and ell=2,4,5,9,
including sizes not divisible by ell. They verify embedding, internal edge
multiplicity, overlap degree and all five stencil losses. Exact symbolic
controls check the entropy-divergence identity and constants in the
exponential estimate. A nonidentically distributed categorical example
and canonical boundary-count examples provide direct probability controls.

The first independent execution succeeded. Full stdout, empty stderr,
versions, source identity and command receipt are preserved; no failed
attempt was discarded.

## Author comparison and verification limits

After the pre-comparison seal, the complete author checker, result file,
run receipt and logs were read. The imported nonlinear helper was already
fully reviewed at the same identity. All result-source bindings and the
successful receipt are authenticated. The author code distinguishes exact
connectivity/covariance arithmetic from numerical eigenvalues and entropy
values, and explicitly states that finite controls are not the proof of
the all-volume theorem.

The post-comparison helper imports only the independent checker. It
independently reconstructs the author's two-color cube sectors at counts
two and four using bitmasks and hypercube edges, and compares the exact
variance, Dirichlet form and centered pairing, connectivity rank, and
numerical gap/entropy derivative. It also checks all five block-arithmetic
rows, four exact tangent coefficients, eight exact sampling-coupling rows,
the Holder constant and thirty Bernoulli moment rows. Full comparison
details are in `AUTHOR_COMPARISON.json` and its raw execution log.
The selected exact sector quantities agree exactly; their numerical gap
and entropy-derivative differences are zero in this replay. The maximum
Bernoulli log-moment difference is 8.89e-16.

The first comparison attempt was deliberately stopped after about 175
seconds without completion. It had not reported an assertion failure.
Its code, empty output streams, signal-exit receipt and diagnosis are
preserved under `failed_attempts/generic_exact_rank`. The only helper
change replaces generic symbolic matrix rank with the equivalent exact
DomainMatrix rank call; the connectivity assertion and all mathematical
criteria remain the same. No per-line profiler was captured. The final
comparison completed with the unchanged criteria.

The author checker itself was not executed here, and the three-group suite
was not replayed for its completion count. The general proof assessment is
the independently sealed derivation. No simulation or finite-volume
trajectory calculation was used to infer the limiting theorem.

## Exact sources and reproduction

Paths below are relative to the campaign's `campaign12h_second` directory;
the manifests contain complete absolute paths, byte sizes and hashes.

| Source | SHA-256 |
|---|---|
| DIMER_SMOOTH_NONLINEAR_EULER_LIMIT.md | dbd07eca8db76c58f672791aa0f20b8483886352d79638931702306518b829b4 |
| DIMER_ROUTED_RECORD_TRANSPORT.md | dc7bac51a1ffb273e11e9356713778aeb645acbfb280973f927c1f1de007d873 |
| DIMER_NONLINEAR_COLOR_FLUX_AND_OPTICAL_DIAGNOSTICS.md | d6a3689bb2ab6bf627886a77f4f197bb6a2478da59264b0dde91d3bf1f131e69 |
| DIMER_NONLINEAR_INITIAL_DRIFT.md | a67bc5a0b8f9a85e0eccba11fc56870e7861410044ff5d6e28d1ddd05d384c78 |
| dimer_smooth_nonlinear_check.py | d97be26aa22fad562ac9419566bcb09c4c97db01dcbd598bca0d601f968f7eb8 |
| dimer_smooth_nonlinear_checks/RESULTS.json | 7eab8d3d38a557a89baae56552c87930d568d4a395e04651974eabff262166be |
| independent_check.py | d4a4b9ada84e826681ab7739184c0a84fe3dacc6e630176db472364f52a3e48a |
| PRE_COMPARISON_SEAL.json | 791aa05ecfe1369949692ad72226b45fb085a05eb8b1f8d82a3de8185075bb6c |

The scripts use Python 3.13.5, SymPy 1.14.0 and NumPy 2.4.4. Their exact
commands are preserved in run receipts. Output files use exclusive
creation: reproduction should use a fresh appropriately mirrored directory
and retain the original sealed packet. The post-comparison helper requires
the recorded primary and pre-seal source paths. `FINAL_SEAL.json`
reauthenticates the pre-comparison bytes and binds the final report,
comparison source, outputs and logs.

The theorem is qualitative, for the color projection on a fixed winding
matching with a fixed positive floor and a supplied C3 strictly interior
PDE solution over a fixed finite interval. Initial entropy density must
vanish relative to that profile. Existence or continuation of the solution,
preparation by births, other or moving matching geometry, shocks, boundary
densities, microscopic key statistics and quantum or spacetime
interpretations remain outside this result. No formal retained status is
conferred by this review.
