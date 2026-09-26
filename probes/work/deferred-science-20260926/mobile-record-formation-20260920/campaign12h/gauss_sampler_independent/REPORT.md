# Gauss equilibrium sampler and staggered-sector review

2026-09-21. No actionable mathematical or implementation defect was found in
this bounded review. The auxiliary finite-volume sampler has the stated
stationary closed-state law and accessibility. The even-volume staggering
identity and adjoint-difference operator algebra are correct with their
stated boundaries. The Monte Carlo records support only a descriptive
finite-size signal, with substantial disclosed limitations; they do not
establish equilibrium, an infinite-volume phase or microscopic photon count.

The three plans/operator arguments were read first. The independent proof
and a different-geometry exact test were sealed before the author C++,
checkers, analysis code, metadata or results were opened. Pre-comparison seal:
`61db44bcef855bee635114f7055b4d8ab4e33c1d6aae642e723c75508af42e5a`.
This is independent reconstruction from supplied arguments, not blind-to-note
discovery. No production simulation, full raw-data scan or formal audit was
performed. No primary file was modified.

## 1. Stationary measure, relocation, trace and accessibility

For a positive axis label E_i(x)=1, regard the midpoint slot x as the charge
edge x-e_i -> x+e_i; a negative label reverses that edge. Its signed incidence
is exactly D2 E. The finite extended state space and weight are

    Omega={(E,t,h): D2 E=delta_t-delta_h},
    mu(E,t,h) proportional z^n(E), z>0.

The proposed head step (i,s) adds s at h+s e_i and moves the head to
h+2s e_i. The divergence change is delta_h-delta_(h+2s e_i), so the
constraint persists. Capacity permits creation in an empty slot or removal
of the opposite same-axis label. Each admissible move has a reverse with
the same proposal probability. Acceptance min(1,z^Delta_n) gives detailed
balance for the worm step, including its rejection holds.

At a closed state, every field has V equal-weight endpoint copies. Uniform
relocation of the common head/tail therefore separately preserves mu.
Relocation followed by the step need not itself be reversible: invariance
of the composition is sufficient, and is what the implementation requires.

For C={h=t}, the successive-visit trace kernel is

    Q=M_CC+M_CO (I-M_OO)^(-1) M_OC.

It has stationary law mu conditional on C. Summing out the endpoint gives
pi_z(E) proportional z^n(E) 1_(D2 E=0), exactly the intended single-species
seven-state ensemble. Visits include rejection/self visits; retaining only
changed configurations instead biases weights by their departure
probabilities. Deterministic thinning of the stationary trace by a fixed
visit stride preserves its invariant law. None of these facts proves a
finite-burn-in trajectory is equilibrated.

Every finite balanced directed occupied-edge graph decomposes into directed
cycles, including branched/shared-vertex and winding configurations. Relocate
the tail to a cycle and follow it backward, removing its occupied edges with
positive acceptance. This never introduces a midpoint capacity conflict.
Repeating reaches the empty field; reversing the path constructs any chosen
closed field. For an open feasible field, directed-flow decomposition gives
a t-to-h path plus cycles; remove the path backward to reach a closed field.
Thus there is no inaccessible feasible open trap. Relocation reaches all
charge components. The argument also works on even tori, notwithstanding
their parity components. It is a finite positive-z accessibility theorem,
not a mixing-time or thermodynamic theorem.

The sampler creates and removes auxiliary fields; it is not an implementation
of irreversible permanent-record motion/formation. Here z_B=0 means B labels
are absent, not summed over or equilibrated at another activity.

## 2. Independent exact square-cycle control

A square charge graph with four distinct midpoint slots in {-1,0,+1} gives
36 extended states and 12 closed states including their endpoint copies.
This is different from the author's one-dimensional three-site toy. At z=2,
exact rational matrix calculations verify detailed balance for the head step,
uniform relocation invariance, composition stationarity, the complete trace
law and reachability. For negative loop, empty, positive loop, the field
trace is

    [59/60  1/60       0]
    [ 4/15  7/15    4/15]
    [    0  1/60   59/60].

The target is (16/33,1/33,16/33), from Z=1+2z^4. Deleting field self visits
changes the stationary law to (1/4,1/2,1/4). This is a decisive normalization
control, not a mixing experiment. The square has no competing axes at a
shared midpoint, so full cubic capacity handling was checked separately in
the C++ source. The independent checker contains 13 exact groups; all passed
on first execution, with the full log and empty stderr preserved.

## 3. Implementation and production protocol comparison

Both complete 127-line C++ implementations were read. Their only differences
are the two declared job-list/seed lines; the full-file replacement comparison
agrees with `SOURCE_CHANGE.diff`. The sampler implements the above composed
kernel. In particular:

- Occupied slots store one signed axis label. Only empty creation and exact
  opposite-axis cancellation are accepted; no record can exceed capacity.
- Head direction and endpoint relocation use unbiased bounded integer draws.
  The added flux is s for both creation and cancellation, as required.
- Closed states are counted after every production attempt, including blocked
  or rejected attempts. Stride is 1024 at z=.2 and one otherwise.
- The burn-in boundary does not restart an open worm. No length cutoff,
  forced closure or discarded long-worm restart is present. Production may
  end open; the metadata discloses this.
- At every saved closed state the source recomputes integer divergence,
  occupancy and signed contents from labels. Fourier phases, all four modes,
  sin(k) longitudinal constraint and normalization |Ehat|^2/(2L^3) match the
  plan. Saved CSVs contain observables, not configurations; this review cannot
  independently recompute divergence from those CSVs.

All 18 screen cases and eight adaptive follow-up cases are present. Metadata
matches the prescribed sizes, activities, initializations, seeds, burn-in,
production attempts and thinning. Accepted=created+removed and final
occupancy=initial occupancy+created-removed in every case. Saved sample counts
are the required floor of production closed visits divided by stride.
The pre-production source/executable hashes and declared parameters match
the current bytes. The binaries were authenticated but not recompiled or
executed, so binary/source correspondence is not independently reproduced.
Recorded timestamps are provenance records, not an external time attestation.

The complete author trace and operator checkers/results/logs were inspected.
Their three and seven reported groups bind the current checker bytes and
agree with the independently reconstructed mathematics. They were not rerun
or counted as additional independent calculations.

## 4. Staggered symmetry and the separate adjoint operator

For even periods, epsilon_eta(x)=(-1)^(eta.x) and
T_eta E_i(x)=epsilon_eta(x)(-1)^eta_i E_i(x) give
D2(T_eta E)=epsilon_eta D2 E. Each neighboring parity sign cancels the
component sign. The map preserves menu, occupation, capacity and activity;
it is a statistical involution, not an immutable-record event. Separate E/B
sign maps preserve the shared two-species capacity as well.

Fourier transformation gives D_eta Ehat(k-pi eta). Therefore the finite even
grand covariance obeys S(k+pi eta)=D_eta S(k)D_eta, also for connected
covariance because global inversion gives zero mean. Symmetric even-periodic
local limits inherit this relation, interpreted for spectral measures if
necessary. It is not an identity for odd finite boxes, fixed winding/count
sectors that the map does not preserve, or arbitrary symmetry-broken selected
states. Eight parity charge graphs still interact through midpoint capacity;
they are not eight independent ensembles.

For the stipulated undamped centered Maxwell block, the transverse frequencies
are +/-c|sin k|, twice each, with two longitudinal zero directions away from
zeros. The eight corners are zeros of this supplied operator. By contrast,
the actual symmetric exchange floor contributes exactly
-4 kappa sum_i sin^2(k_i/2) to each Fourier feature, or N times this on the
Euler clock. At a nonzero corner its multiplier is -4 kappa times the number
of pi coordinates. Context terms can couple observables; this calculation
is neither a closed kinetic spectrum nor an all-time decay estimate.

For v_i=e^(ik_i)-1, C+=[v]_cross and C-=C+*=-[conj(v)]_cross. Direct
multiplication yields

    C+* C+=|v|^2 I-v v*,
    C+ C+*=|v|^2 I-conj(v) v^T.

Consequently c[[0,C-],[-C+,0]] is skew-Hermitian, preserves real quadratic
energy and conserves d- dot E and d+ dot B. At v!=0,c!=0 its eigenvalues
are +/-i c|v| twice each and two longitudinal zeros. The longitudinal null
vectors are v for E and conj(v) for B. Since
|v|^2=4 sum_i sin^2(k_i/2), only k=0 is a Brillouin-zone frequency zero;
degeneracies increase at k=0 or c=0. The independent checker verifies the
complex Gram identities symbolically and a nontrivial exact six-field
polynomial lambda^2(lambda^2+8)^2. It also checks all eight staggering
identities on arbitrary arrays on an N=4 torus.

The source correctly leaves microscopic realization, field placement and
cubic action of this new stencil open. Its improved operator zero structure
does not change the existing stochastic model or establish photon multiplicity.
The actual production boxes are odd: the even-volume identity is a separate
diagnostic and cannot be imposed as an exact relation on their recorded data.

## 5. Compact analysis and selective raw-data checks

Both complete Python analysis files and the complete reducer C++ were read.
The analysis uses paired mode-block means, keeps initializations separate,
and discloses dependence/coverage limitations. The follow-up is explicitly
adaptive. Full compact block tables total 37,918,791 bytes. Independently
recomputed block means, both spectral ratio estimates, all first/last-half
means, lag-one correlations, discarded counts and flags agree for all 26
cases and both follow-up block sizes. Reconstructing each full-sample mean
from all compact block means plus its actual residual raw tail agrees with
the reducer's summary. This checks coherence of the reductions without
claiming a complete raw-data re-reduction.

Raw files total 5,296,789,994 bytes. This review read only the first 256 data
rows and a bounded tail window from each file: 2,503,398 raw bytes and 20,276
selected rows in total. In every case, the first two and last full 128-row
block means match their stored blocks; endpoints, integer occupation,
L-multiple signed flux, sample numbering, increasing attempt indices and
reported ranges pass. All raw file sizes and metadata hashes match the
recorded identity manifests. The manifests' complete raw SHA-256 values
are retained as recorded provenance, NOT independently recomputed hashes.
No raw CSV was copied, no full raw hash was computed, and no production was
rerun. Global extrema/change counts were not independently recomputed from
all raw rows; they were checked for consistency and against selected windows.
The existing bootstrap intervals were inspected, not regenerated.

The first screen's preserved analysis attempt emitted NaN for one undefined
lag correlation (`L13_z2_init1`, flux-x). Its receipt, code, output and warning
log remain intact. The actual correction only guards both lagged arrays'
variances and forbids NaN JSON. No sampler or bootstrap target changed.
The corrected null treatment agrees with the independent calculation.
Both independent scripts passed their first executions. An oversized display
of metadata was subsequently replaced by complete structured checks and
concise case reads; no truncated display was treated as full verification.

## 6. What the numerical evidence does and does not show

All six z=.2 screen cases have only 13 complete 128-sample blocks, below the
planned minimum; their intervals are correctly withheld. At z=4 the full
starts for L=13 and L=17 retain exactly constant saved observables across
18,734,892 and 18,743,677 samples, respectively, with no observed winding
change and density one. Empty-start densities differ strongly. L=9's full
start also has a very long identical-observable run. These are disclosed
trapping/non-equilibration diagnostics; huge visit counts do not rescue them.

At z=1 the follow-up is compatible with nearly equal low-mode spectra in
the observed boxes. It is not a certified infrared law. For example, the
1024-block axis/diagonal ratio estimates at L=49 are approximately
1.058/1.023 (empty start) and 1.005/.985 (full start), with only 17 and 16
complete blocks. Their quoted descriptive intervals are broad and material
lag dependence is flagged; L=49 empty-start density-block lag correlation
is about .451. Several other profiles also flag dependence. Apparent
agreement of starts and flux changes are useful diagnostics, not proof of
stationarity or bootstrap coverage.

The finite-box flatness cannot distinguish a true nonanalytic infrared
spectrum from a long crossover beyond these sizes, and cannot establish a
phase transition, exponent, quantum vacuum or formation-selected state.
There is no rigorous mixing-time estimate here. Those unresolved scientific
obligations are already acknowledged; no narrow source correction is needed
for the reviewed claims.

## 7. Source/output seal and reproduction

Main implementation hashes:

- `gauss_worm_screen.cpp`: `1920e4df3144ae7fcdabd360428f1ab4bdee8a835b8a5b8460e9cbba53adb183`
- `gauss_worm_z1_followup.cpp`: `97f8c400731ddd36ec1c42d134c7106dbd09dbc5a43cabf7d6df8d53ca5f5268`
- `gauss_worm_trace_check.py`: `cc4221c0fc7d90c07a78a98549540a38d29e1c3179eed563123ec4a7ddf8816f`
- `centered_gauss_staggered_check.py`: `38116bc7fc36e2c819aa7a9e9863125e1742b584b339397ed8ae76bd3759b24c`
- `analyze_gauss_worm_screen.py`: `dad7e51a48d6de5cf4cee1a47a5f668c109f0ac55b20e1b58f64ddaad2e6e979`
- `analyze_gauss_worm_z1_followup.py`: `8ed5dda8312dee0109d535c03bea79ed43b2eb37a89ea9efc6a2aba3b70a3d6f`

The plans/operator hashes are in the immutable pre-comparison seal. Full
post-comparison source/output identities and recorded raw-data exclusions
are in `COMPARISON_RESULTS.json` and `FINAL_SEAL.json`. The former hash is
`4f4f0e662cc4ea81e534d243ca3fee5257195e90f0ef684a41e824a060cf40c8`.
All sources were checked for concurrent changes before sealing.

Run locally, with SymPy and NumPy available:

```sh
python3 gauss_sampler_independent/independent_check.py
python3 gauss_sampler_independent/compare_evidence.py
```

The first script uses only its own reduced graph and operator algebra. The
second reads existing source/evidence and bounded raw windows; all writes
remain in this review directory. Both full stdout/stderr pairs are preserved.
Original sealed pre-comparison files remain unchanged. No external literature
or unrelated primary research was required, and no audit status was applied.
