# Ranked opportunity queue

## Current re-rank after ten route reviews — 2026-09-24 21:17 UTC

The candidate source is at 2d36bafc9ba85a2cd1e5e588d7892a79aa086903
against origin/main 0e6ad8285096ed668816f18caaa6fbbfbd9c50e8. Seven of ten
read-only reviewers rank finite-endpoint selection of the decaying Airy mode
as the next leverage point. Two prefer direct prepared-weighted phase/readout
control; one prefers central-detuning uniformity. These are route
recommendations, not independent reviews of candidate theorem proofs.

1. **Finite-boundary selection of the decaying Airy mode — active campaign.**
   For compact Lambda subset (0,4), start from the exact right boundary of
   the five-site Jacobi family. Prove that backward recurrence enters and
   stays in a positive monotonicity cone on a fixed forbidden interval, then
   map that cone into the Airy Jordan coordinates at
   u=a_lambda+R S^-2/3. The decisive conclusion is a uniform estimate
   showing the growing Airy coefficient is zero in the limit (or is bounded
   relative to the decaying coefficient strongly enough for matching).
   First prove the terminal coefficient, five-residue signs, strict row
   dominance, and compact-energy uniformity. The cone alone does not prove
   Ai selection until its relation to the Airy coordinates and projective
   normalization are controlled.
2. **Prepared-weighted phase stability for the actual scalar.** Use the
   observable-sensitive bound on delta q with the actual |c_j c_k V_jk|
   and phase differences. The finite low-lag diagnostics are small but do not
   control all lags; avoid an unweighted operator-norm phase approximation.
   This route can bypass full eigenvector norm accuracy only if every
   macroscopic lag and reciprocal alias is bounded.
3. **Two-turn quantization and prepared-overlap transport.** After endpoint
   mode selection, carry amplitudes/phases through the opposite turn and
   every simple/central Bragg layer. Determine whether termwise o(S^-2)
   eigenvalue control is obtainable or replace it with a proved weighted
   stability estimate for the readout.
4. **Central and spectral-edge uniformity.** The fixed-energy central
   transfer cannot be made energy-uniform from its present note. A fixed
   central energy window can be removed from the qualitative scalar at
   O(sqrt(delta)) using the prepared arcsine spectral law; this supplies
   no shrinking-window rate. Reopen this route if a global quantization
   theorem requires such a rate or if the forbidden constants degenerate
   near lambda=0,4.
5. **Native axiom-to-model bridge.** The four axioms leave supplier dynamics,
   preparation, and readout downstream. No incompatibility has been shown.
   Reopen only with a constructive bridge failure or two axiom-compatible
   models giving incompatible target behavior; current evidence does not
   warrant an axiom revision.

The forbidden-tail reviewer derived the exact terminal relation and a
row-dominance estimate; it remains a proposed lemma until the entire backward
induction and cone-to-Airy passage are proved with uniform constants. The
other reviewers identify the next alternate scalar route and rule out
repeating finite central scans as a substitute for uniform estimates.

## Re-ranked after ten current-head reviews — 2026-09-24 17:10 UTC

The ten read-only reviews used `c734332ca227c4371f3c188f96227c494b43f533`
and current main `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. They preserve the
actual fixed-time interior scalar as the principal target. The active first
block is the exact five-site transfer trace and local eigenphase through
`S^-2`, with a uniform `O(S^-3)` remainder on compact regular bulk arcs and
exact regrouping into three shifted five-site cells. This is a feed-in to
global quantization, not a readout theorem.

1. **Actual-index transfer phase through `S^-2` (active block).** New
   derivation of the determinant-one cell transfer, its second trace
   coefficient, and the locally oriented phase with an explicit regular-arc
   remainder. First checks: independent coefficient convolution, finite
   exact-cell comparisons, and equality of the direct 15-site product with
   three genuinely shifted five-site factors. A wrong product order,
   incorrect `tau_2`, failed determinant, or product regrouping mismatch
   rejects the derivation. Even a pass leaves the global `O(S)`-cell
   accumulated phase, crossings, and prepared overlaps open.
2. **Global phase and prepared-overlap transport.** Establish a phase-accurate
   global quantization law (uniform eigenvalue `o(S^-2)` error is sufficient
   for an `o(1)` termwise phase error) or a proved weighted approximation for
   the exact bilinear readout. Must handle the true shifted cells, Bragg,
   central, turning and boundary layers. The present local block is useful
   only if it yields a construction across those layers.
3. **Joint alias-complete interior two-index estimate.** Bound the prepared
   weighted sum across both spectral indices and all reciprocal aliases,
   retaining diagonal, crossings, central mass and any terminal terms. A
   fixed-lag alias condition does not imply coordinatewise nonresonance.
   The first missing bound is weighted mass/variation on joint-resonance
   strips; a surviving coherently weighted bulk patch falsifies a proposed
   cancellation mechanism.
4. **Exact terminal spectral row (small support route).** Nonatomic prepared
   spectral-measure convergence implies the largest atom tends to zero, so
   one terminal row (or a fixed number of rows) has vanishing total absolute
   contribution. This can simplify the double-sum boundary bookkeeping but
   has no rate and does not control a growing strip or interior aliases.
5. **Framework-to-model comparison.** Current axioms leave the Hamiltonian and
   physical readout downstream. A pair of compatible models would show
   underdetermination only; no contradiction or axiom change is supported.
   Defer unless a concrete supplier/observable bridge is identified.

The existing phase-accuracy gate and the source search were read before this
block. Do not repeat them without a changed mathematical object or error
scale. The transfer source search at main and the relevant proposal heads
found the existing first-order frozen five-site correction, but no matching
actual-index trace/phase expansion through `S^-2`.

1. **Joint discrete stationary phase across macroscopic spectral lags.** Write
   the exact profile scalar as its diagonal term plus positive lag sums
   (L_{S,h}=sum_j W_{S,j,h}e^{iC(\lambda_{j+h}-\lambda_j)/4}). The new
   all-lag scan at S=96,192,384,512 finds \(\sum_h|L_{S,h}|\approx0.37\),
   while \(\operatorname{Re}\sum_hL_{S,h}\) changes sign and has magnitude
   0.0141, 0.00470, 0.0118, 0.00620. For S=512, no tested individual lag
   contributes above 4.7e-4, while the full real scalar is 0.0125. The target
   therefore needs collective cancellation across the two spectral indices;
   finite frozen-symbol stationary phase or a fixed-lag estimate is not enough.
   For theta_j=C lambda_j/4 and alpha_j=theta_(j+1)-theta_j, the exact
   fixed-lag phase difference has discrete derivative
   alpha_(j+h)-alpha_j. Thus its cancellation points satisfy
   alpha_(j+h)-alpha_j=2 pi m, for all integers m, not only m=0. The new
   S=96,192,384,512 census finds 4,7,13,17 distinct alias integers in the
   one-index phase slopes; the prepared-mode mass within 0.01 rad of any
   individual alias is about 0.0043--0.0048, while the all-lag weighted mass
   within 0.01 rad of a lag-derivative alias grows 0.0193, 0.0260, 0.0371,
   0.0424. A zero-alias frozen-symbol calculation cannot control this sum.
   Seek a phase-accurate, weight-aware Poisson/van-der-Corput decomposition
   that sums every reciprocal alias and includes Bragg crossings, the central
   layer, endpoints, the diagonal, and the terminal pair omitted by a forward
   difference. Uniform branch quantization and overlap transport are still
   missing; the census only identifies the obligation.
   The primitive five-site action gives a useful scale check. Its lobe area
   A_+(lambda)=pi(2-sqrt(lambda)) implies the principal Weyl count
   N_(<=lambda)~5S sqrt(lambda), so the smoothed sorted spectrum obeys
   lambda_j~(j/(5S))^2 and theta_j~(S+1)j^2/(100S). This predicts the O(S)
   alias range quantitatively: the expected maximum nearest-alias index is
   S/(10pi), equal after rounding to the observed 3,6,12,16 at
   S=96,192,384,512. The actual alpha_j regression has slope 0.020000 rad
   per spectral index at all four sizes and correlation 0.985--0.997 with
   that Weyl increment. However the Weyl density does not determine local
   gaps: quadratic phase fits still leave up to 7.88 radians of phase error
   and change q_S by as much as 0.0232, comparable to the target scalar.
   Under the quadratic surrogate the narrow (0.01-rad) predicted resonant-lag
   set carries only 0.0011--0.0018 of sum |L_h|, versus total near 0.37;
   widening to 0.1 rad raises this only to about 0.012--0.015. Thus the
   principal quadratic aliases organize the scale but do not isolate the
   readout contribution. Next derive phase-accurate subprincipal action and
   preserve the full weighted lag coupling.
   The macroscopic distribution is now proved as a separate support theorem
   in `POSTMARK_ELECTRIC_PRINCIPAL_WEYL_COUNT_BOUNDED_THEOREM_NOTE_2026-09-24.md`:
   fixed trace moments converge to `4^m/(2m+1)`, hence the empirical density
   is `1/(4 sqrt(lambda))` on `(0,4)`. Its quantile profile proves only
   `lambda_(j,S)->4 rho^2` when `j/D_S->rho`; it gives no rate on individual
   gaps. Use it as the principal phase scale, not as a spacing theorem.
   The new phase-accuracy probe gives an exact finite stability gate. For
   spectral phase errors `e_j`,
   `|delta q| <= sum_jk |c_j c_k V_jk| min(2,|e_k-e_j|)`; common phase cancels,
   and an operator-norm bound controls the change by twice the prepared-state
   phase-vector error. A best quadratic fit leaves the prepared state at
   distance 0.98--1.19 from its exact phased version at S=96--512, so uniform
   state accuracy does not certify the readout. Its actual q error is
   nonmonotone, 0.00030--0.0232. Absolute overlap weight is dominated by
   macroscopic lags `h>D/4` (7.5--17.1), while lags `h<=32` carry only
   0.26--0.58 and the diagonal is below 0.009. These finite scans do not prove
   asymptotic growth or a readout limit. Refine the campaign toward a joint
   overlap-weighted oscillatory estimate over macroscopic lags and every
   reciprocal alias; pointwise quantization accuracy and fixed-lag bounds
   remain only sufficient/support routes. Total pair-weight L1 divided by
   `sqrt(S)` is 1.197--1.209 at the four tested spins, consistent with the
   exact envelope `||V|| ||c||_2 ||c||_1 <= O(sqrt(S))`; the Cauchy envelope
   itself gives no signed cancellation.
2. **Phase-accuracy gate for quantized WKB.** Local eigenvalue expansions with
   an O(S^-2) remainder are not automatically accurate at time C/4 because
   the leading phase sensitivity is O(S^2). Derive the sharp tolerance and
   then seek either a global o(S^-2) quantization remainder or a cancellation
   proof robust to the residual order-one phase error through Bragg and central
   layers.
3. **Pole-aware all-energy Schur reconstruction as support.** The exact
   two-energy anchor pencil reduces dimension away from the four-site poles.
   A Moore-Penrose/kernel-constraint extension can remove this coordinate
   exclusion, but its normalized overlap is bounded by unitarity and gives no
   selected-time cancellation. Reopen only if a derivative, residue, or
   prepared-weighted pole estimate feeds item 1.
4. **Actual weighted lag-phase cancellation by one-lag Abel bounds.** The
   all-lag diagnostic verifies the exact decomposition, but the aggregate
   triangle/Abel bound grows from 238 at S=96 to 1386 at S=512. The sum of
   absolute lag amplitudes remains about 0.37. Do not reuse that bound; a
   two-index estimate must exploit phase and weight correlations across lags.
5. **Five-cell quantization and accumulated phase.** The principal lobe action
   and first scalar (1/S) band correction are derived. A global quantization
   estimate must resolve Bragg and central layers at phase-accurate scale.
6. **Complex-time birth-death kernel.** The full generator has a reversible
   birth-death representation, but its period-three classes are not lumpable.
   Reopen only if the supplied rates yield a pointwise estimate at the selected
   complex time, rather than importing real-time mixing.
7. **Actual-readout separated subsequence.** Finite scans do not certify a
   wall. Continue only if exact/interval enclosures and an all-index error
   establish disjoint limiting intervals for actual integer-spin readouts.
   Direct float64 spectral values at S=512,640,768,896,1024 are
   0.34167,0.33705,0.33726,0.33621,0.32857. This narrows no limit claim and
   certifies no separated subsequence.
8. **Framework-to-model derivation.** The four current axioms explicitly leave
   Hamiltonian choice and record-production dynamics downstream. This confirms
   an import boundary, but neither proves the supplied model impossible to
   derive nor forces an axiom update. A separate candidate must derive the
   supplier or construct two axiom-compatible models with distinct target
   predictions.
9. **Prepared-state endpoint strip — completed support.** The fixed-energy
   eigenfunction barrier and arcsine spectral law give a uniform-in-phase
   shrinking-strip bound. Reuse it in any interior propagation proof.

Re-rank after each analytic discriminator. Do not repeat finite scans unless
they test a changed estimate, invariant, or error scale.
