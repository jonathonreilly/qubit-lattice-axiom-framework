# NT-1′ independent referee record

## VERDICT: CONFIRMED WITH CORRECTIONS

The worker's **OPEN** headline is the correct fixed reading, but not for the
reason given.  G-LEG(c) passes the wording fixed in `TESTS.md`: the anomalous
L1 construction visibly fails locality.  The monopole defect tends to the
nonzero anomaly coefficient and the compensating current has a spatial
plateau with fixed total weight.  The worker's narrower operational pointer
was blind to that plateau and cannot override the parent fixed wording.

What remains unconfirmed is G-LEG(b), hence the premise needed for
`CHI-RP-FAIL`: the supplied code is a serious and substantially correct
finite-chart implementation of the structure of Lüscher's eq. (5.8), but the
explicit finite-volume term is a global right inverse of the divergence, not
Lüscher's proved exponentially small finite-volume correction.  The data show
a small spatially flat tail in the anomaly-free current but do not establish a
uniform exponential-in-volume bound for it, and global integrability around
the Wilson-line circle is not checked.  Thus I confirm the numerical RP
negatives, the anomalous-control diagnosis, the reflection condition, and the
local straight-ray construction on the sampled chart.  I do **not** confirm
that the sampled weight has been completed to a legitimate global local
Lüscher measure, so this is not confirmation of `CHI-RP-FAIL` as fixed.

If one elects to accept the anomaly-free flat tail as Lüscher's exponentially
small finite-volume term and treats a chart-local measure as sufficient, then
the fixed rule gives `CHI-RP-FAIL`, not OPEN: under that interpretation all of
G-LEG, including (c), passes and all three kernels exceed the registered
negative threshold.

## Materials and independent checks

I read `TESTS.md`, `PREREG.md`, `REPORT.md`, `NT1_REPORT.md`,
`NT1_REFEREE.md`, the K2c report and verdict, every `nt1p_*.py` file, the
support libraries, all saved text outputs, and the saved pools and kernels.  I
also checked the construction against:

- M. Lüscher, *Abelian chiral gauge theories on the lattice with exact gauge
  invariance*, especially Theorems 5.1, 5.3, 5.4 and eq. (5.8),
  <https://arxiv.org/abs/hep-lat/9811032>;
- D. Kadoh and Y. Kikukawa, *A simple construction of fermion measure term in
  U(1) chiral lattice gauge theories with exact gauge invariance*, especially
  the separate Wilson-line construction and the locality bound on the
  finite-volume term, <https://arxiv.org/abs/0709.3656>.

All referee computations were serial, used two numerical threads, ran below
0.3 GB RSS, and created no auxiliary files.  The main independent checks were:

1. Reloading every `*_NT1P_logK.npz`, reconstructing the normalized matrices,
   and diagonalizing their Hermitian parts reproduced the saved `Zchi` arrays
   exactly and gave:

   | Pool | `lambda_min` | `lambda_max` | `E` | `|lambda_min|/E` |
   |---|---:|---:|---:|---:|
   | P-A, Lt 8, k=12 | `-2.448469823641e-3` | `11.935795419464` | `4.992699895517e-5` | `49.0410` |
   | P-B, Lt 8, k=10 | `-9.578705782897e-4` | `9.936235198134` | `3.680084510841e-5` | `26.0285` |
   | P-C, Lt 12, k=8 | `-5.367897477690e-4` | `7.956768381050` | `2.432321433648e-5` | `22.0690` |

   These agree with `scripts/K_PA_Lt8_1504.out:14`,
   `scripts/K_PB_Lt8_2504.out:14`, and
   `scripts/K_PC_Lt12_1512.out:14`.

2. I freshly recomputed P-B entry `(1,5)` through the worker's measure at
   Duffy levels 3, 4 and 5, and entry `(5,1)` at level 4, using link chunks of
   four.  Each raw complex log integral agreed with its saved value to the last
   printed bit.  For example, the level-4 `(1,5)` value was
   `-2.982696752503008e1 + 2.300514516993097 i`; level 5 moved it by only
   `5.44e-7 + 1.53e-8 i`.

3. I separately rebuilt the overlap modulus for P-B entry `(1,5)` directly
   from the Wilson matrix, spectral sign, and
   `|det D(1)|^2 |det D(2)|^(1/2)`, including fresh diagonal normalizations.
   It gave `0.9972312884804894`; the saved modulus entry is
   `0.9972312884804823`, a difference of `7.1e-15`.  This is independent of
   the cohomology-current and Weyl-basis code and corroborates the worker's
   factorization check at `scripts/INDEP_PA.out:7-9`.

4. Reading the pool arrays directly gives maximum mismatch of the positive-half
   boundary Wilson angle of `5.6e-17`, `8.3e-17`, and `5.6e-17` for P-A,
   P-B, and P-C, respectively, agreeing with
   `scripts/SEARCH_PA_Lt8_1504.out:13`, `scripts/GATES_Lx4_Lt8.out:1`, and
   `scripts/SEARCH_PC_Lt12_1512.out:9`.

## 1. Measure legitimacy

### 1.1 What is correctly implemented

The repair is not merely NT-1's cumulative anomaly current.  The following
load-bearing pieces are present and mutually consistent.

- The charge content is genuinely chiral and anomaly-free in two dimensions:
  four left charge-1 Weyl fermions and one right charge-2 Weyl fermion,
  $4(1)^2-(2)^2=0$ (`scripts/nt1p_lib.py:13-14`).  The code first weights the
  anomaly by chirality times charge and then supplies the second charge factor
  when differentiating with respect to the charge-one potential
  (`scripts/nt1p_lib.py:223-250`).
- The positive/negative overlap spectral subspaces and barred chiral rows are
  the correct Weyl spaces.  The basis is transported from the free field along
  the straight ray by the polar/SVD parallel-transport step
  (`scripts/nt1p_lib.py:228-258`), and its Weyl determinant is then formed from
  the correct rows (`scripts/nt1p_lib.py:270-275`).  This is the finite
  implementation of the first term in Lüscher's eq. (5.8).
- The spectral derivative of the overlap anomaly is coded analytically
  (`scripts/nt1p_lib.py:202-220`) and agrees with a central finite difference
  to `6.77e-11`; it also annihilates a gauge variation to `8.6e-16`
  (`scripts/T0_checks_Lx4_Lt8_after_refactor.out:8-9`).
- The plaquette derivative at fixed nearby Wilson data is assembled at
  `scripts/nt1p_lib.py:260-265`.  Its monopole part is explicitly removed,
  the zero-sum source is sent to the plaquette corners by the symmetric path
  operator, and the resulting local Poincaré current is formed at
  `scripts/nt1p_lib.py:266-269`; the paths themselves are at
  `scripts/nt1p_lib.py:142-187`.  Algebraically, the path current has the
  required divergence.
- The straight-ray weights are correct: interchanging the two ray integrations
  yields the factor $1-t$ used at `scripts/nt1p_lib.py:269`, and the scalar
  phase $A\cdot\bar{\bar k}$ is added to the transported determinant at
  `scripts/nt1p_lib.py:283-293`.  The un-fixed Ward test selects `s_k=-1` and
  converges with fourth-order Richardson/Simpson scaling
  (`scripts/WARD_Lx4_Lt8.out:7-9`); the opposite sign stalls
  (`scripts/WARD_Lx4_Lt8.out:10-12`).
- The finite-volume residual is sent through an exact right inverse $Q$ of
  the divergence (`scripts/nt1p_lib.py:130-140,277-280`).  Consequently
  `div kbb = Abar` to `1.6e-15` and `kbb` is gauge-invariant to `1.7e-15`
  (`scripts/T0_checks_Lx4_Lt8_after_refactor.out:11-12`).  These are real
  improvements over NT-1.

Thus the implementation follows the **algebraic structure** of Lüscher's
infinite-volume eq. (5.8) on its straight-ray chart.  The monopole subtraction
also isolates anomaly cancellation in the right place: for L1 the bulk defect
is essentially independent of field amplitude (`scripts/DIAG_m_Lx4_L1.out:2-7`),
whereas the 11112 defect is field- and finite-size-dependent
(`scripts/DIAG_m_Lx4_11112.out:2-7`,
`scripts/DIAG_m_Lx8_11112.out:2-7`).

### 1.2 What is not yet Lüscher's finite-volume theorem

Lüscher's Theorem 5.4 does not say that an arbitrary inverse divergence may
be appended to make the Ward identity exact.  It constructs a correction to
the **measure connection** that simultaneously has the required curvature,
global integrability, symmetries, and a uniform bound of the form
$\kappa L^\nu e^{-L/\rho}$.  Kadoh--Kikukawa likewise separate the toron
connection and prove the finite-volume part exponentially small.  Here $Q$
uses whole-slice sums and cumulative sums around the full spatial circle
(`scripts/nt1p_lib.py:131-140`).  It proves exact divergence, but locality must
be supplied separately.

The measured locality does not close that step:

- The reported taxicab slopes `nu=1.59, 1.71, 1.64` are real, but the fit mixes
  spatial and temporal separations and is dominated by the long open-time
  direction (`scripts/nt1p_locality.py:13-18,38-46`).  The same statistic even
  labels the manifestly anomalous L1 current local
  (`scripts/LOC_Lx8_Lt8_L1_F1.out:10-12`).  It therefore cannot by itself be a
  locality test.
- In the dedicated spatial profile, the 11112 $Q$-response is essentially
  flat around the circle: at Lx 4 it is `4.39e-4`--`5.19e-4`
  (`scripts/XPROF_rows.out:1-6`); at Lx 6 it is mostly
  `5.34e-4`--`6.31e-4` (`scripts/XPROF_rows.out:7-12`); at Lx 8 it alternates
  near `1.06e-4`--`2.67e-4` (`scripts/XPROF_rows.out:13-18`).  Moving the open
  ends from Lt 8 to Lt 12 leaves a `0.7e-4`--`1.7e-4` spatially flat component
  (`scripts/LOC_Lx8_Lt12_11112_desc_s302.out:15-19`).
- The **total** far response does decrease, from `4.16e-4` at Lx 4 through
  `2.31e-4` at Lx 6 to `1.07e-4` at Lx 8
  (`scripts/XPROF_rows.out:1-18`).  That trend is compatible with an
  exponentially small wrapping correction multiplied by a polynomial in the
  volume.  It is not evidence of a definite locality failure.  But three small
  sizes, evaluated on different random fields, also cannot distinguish such a
  bound from an algebraic tail.  In particular the isolated $Q$ amplitude is
  not even monotone from Lx 4 to 6.

Accordingly, the x-flat piece is best classified as an **unresolved
finite-volume tail**, not as a proved defect and not as a proved Lüscher
correction.  It is consistent with exponential locality, but the fixed demand
that exponential decay be measured in all relevant directions is not met at a
Nature-grade level.  The worker's later 41-fold endpoint test
(`PREREG.md:169-177`) is too weak to establish the required uniform
exponential bound.

There is also a terminology issue.  The numerical response in
`scripts/nt1p_locality.py:24-53` is the response of the auxiliary ray-averaged
cohomology current `kbb`, not a direct response measurement of the full
Lüscher measure current $j_\mu$ defined by varying both terms of eq. (5.8).
Locality of the latter follows from locality of the projector and of the
cohomology current in Lüscher's proof, but only after the finite-volume bound
has been established.  The current diagnostic is useful and relevant; it is
not by itself the full reconstruction-theorem locality check.

### 1.3 Canonical representative and reflection

Evaluating the weight on the canonical representative is legitimate **on the
tested chart**.  The map preserves plaquettes and Wilson data, is independent
of ordinary gauge transformations to `1.1e-15`, and commutes with link
reflection to `1.1e-16`
(`scripts/T0_checks_Lx4_Lt8_after_refactor.out:10`).  Therefore it does not
manufacture kernel Hermiticity, and it makes the finite numerical evaluation
orbit-independent.  The un-fixed Ward identity's fourth-order convergence
(`scripts/WARD_Lx4_Lt8.out:7-9`) is important: it shows that canonicalization
is evaluating the gauge-invariant limit of the constructed ray measure, rather
than merely hiding an uncancelled anomaly.  The canonical result is invariant
to `6.75e-14` (`scripts/GATES_Lx4_Lt8.out:19`).

This conclusion is limited to the real-potential chart.  `canon` operates on
unwrapped angle sums (`scripts/nt1p_lib.py:93-106`), and neither it nor the
straight-ray basis checks a loop around the compact Wilson-line variable.

### 1.4 Does untested global integrability matter here?

It does not invalidate the finite matrices: all evaluated rays stay gapped,
remain in one chart, and have maximum canonical `|W_t| <= 1.238`
(`scripts/K_PA_Lt8_1504.out:17`, `scripts/K_PB_Lt8_2504.out:17`,
`scripts/K_PC_Lt12_1512.out:17`).  On a contractible chart the explicit basis
and scalar phase are integrable by construction.

It **does** matter to the headline word "legitimate."  A global Lüscher
measure must be smooth and single-valued on the compact admissible field
space, with the Wilson-line holonomy treated consistently.  The open-time
cylinder has fewer toron directions than Lüscher's periodic torus, and 11112
has no evident charge-parity obstruction, so the omission is not evidence
that the extension fails.  But no loop transport, patching construction, or
Wilson-line connection was supplied.  Straight rays prove local integrability
only.  The local-chart negative is therefore a strong conditional result, not
a completed global-measure result.

**Item-1 finding:** the eq. (5.8) straight-ray/cohomology structure, connected
Ward identity, canonical gauge invariance, and reflection-compatible chart
are confirmed.  A legitimate global local finite-volume Lüscher measure is
not established.  G-LEG(b) remains OPEN because the anomaly-free flat tail is
only consistent with, not demonstrated to satisfy, exponential finite-volume
locality, and Wilson-line global integrability is untested.

## 2. G-LEG(c): the anomalous control

The governing language is the parent campaign rule, not the worker's surrogate
metric.  `TESTS.md:299-302` says the readings are fixed before the agents'
pre-registrations, and `TESTS.md:343-347` requires only that the same anomalous
construction "visibly fail gauge invariance, locality or integrability."
`PREREG.md:105-108` operationalized that requirement with a taxicab fit or a
same-type endpoint comparison.  Once those pointers were found to be
structurally blind, they ceased to be valid measurements of the fixed semantic
condition; they did not acquire authority to narrow it.  The F1 endpoint at
exactly `s=4` was also added after seeing Lx 4 data
(`PREREG.md:151-171`) and is not the parent fixed rule.

The substantive L1 evidence is decisive:

- Its bulk monopole-defect magnitude changes from about `0.140` to `0.154` to
  `0.158` for Lx 4, 6, 8, approaching $1/(2\pi)=0.15915\ldots$
  (`PREREG.md:178-185`; direct Lx 4 rows are
  `scripts/DIAG_m_Lx4_L1.out:2-7`).
- The mixed-link $Q$-response remains flat out to the largest available
  mixed separation.  The representative plateau is about `8.9e-3`,
  `6.5e-3`, `4.95e-3`; multiplying by Lx gives approximately
  `0.036, 0.039, 0.040` (`PREREG.md:182-185`).  Fixed total weight with a
  `1/Lx` pointwise plateau is incompatible with a volume-independent
  exponential locality bound.
- The apparent fall at the antipode is a selector artifact: only same-link-type
  pairs occur at exactly `s=Lx/2`, while the nonlocal inverse-divergence
  response is on mixed pairs (`PREREG.md:178-184`).  The raw profiles display
  the plateau directly (`scripts/XPROF_rows.out:19-36`).
- Removing $Q$ leaves the L1 Ward residual at `1.94e-2` for a modest random
  transformation and about `0.20` for the large transformation, with no
  transport convergence (`scripts/WARD_Lx4_Lt8.out:19-21`).  Restoring $Q$
  restores the Ward identity (`scripts/WARD_Lx4_Lt8.out:16-18`) precisely by
  introducing the nonlocal plateau.

This is exactly the anomaly-control behavior the fixed gate asks for: the
anomalous theory can be gauge-restored on the finite chart only by the visibly
nonlocal part.  Failure of the worker's blind `s=4` statistic is not failure of
G-LEG(c).

**Item-2 finding:** G-LEG(c) **PASSES the fixed wording**.  The worker's
pre-registered operationalization governs honesty about that particular
statistic, but the fixed wording in `TESTS.md` governs the campaign reading.

## 3. RP kernels, errors, and witnesses

### 3.1 Eigenvalues and spot checks

The three negative eigenvalues and all saved-matrix normalizations are
reproduced in the table above.  The full level-3/level-4 difference is evaluated
on every ordered pair (`scripts/nt1p_kernel.py:44-46,76-83`), and the phase is
not made Hermitian by filling: every ordered chiral entry is computed directly
(`scripts/nt1p_kernel.py:36-45`).  The observed Hermiticity defects are included
in $E$.

The fresh P-B raw-entry recomputation and the independent modulus entry check
show that the saved artifacts are internally faithful.  The modulus kernels are
independently negative too:

- P-A `-2.44299e-3` (`scripts/K_PA_Lt8_1504.out:15`);
- P-B `-9.46751e-4` (`scripts/K_PB_Lt8_2504.out:15`);
- P-C `-5.3642e-4` (`scripts/K_PC_Lt12_1512.out:15`).

### 3.2 What $E$ does and does not mean


The formula $E=k\max(q,q_3,q_{PT},h)+10^{-13}$ is honestly implemented at
`scripts/nt1p_kernel.py:76-83`.  Multiplication by $k$ is the standard bound
of spectral norm by $k$ times a maximum entry error.  But $q_3$ and
$q_{PT}$ are measured only on a random off-diagonal subset plus the diagonal
(`scripts/nt1p_kernel.py:47-53,78-80`).  No analytic remainder bound shows that
those subset maxima bound every untested entry.  Thus $E$ is an empirical
convergence estimate, not a rigorous quadrature error bar.

That correction in wording does not make the observed signs doubtful.  The
full level-3/4 changes dominate P-A and P-C, the level-5 changes are only
`4e-8`--`7e-8`, and the separate modulus matrices have the same negatives with
no transport-phase sensitivity (`scripts/K_PA_Lt8_1504.out:14-16`,
`scripts/K_PB_Lt8_2504.out:14-16`,
`scripts/K_PC_Lt12_1512.out:14-16`).  The correct phrase is
**quadrature-converged negative**, not certified negative.

### 3.3 Witness legitimacy

The stored pools are W-matched to roundoff, as independently checked above.
P-A was searched on the vector-like O kernel, not on the chiral answer
(`scripts/nt1p_search.py:16-31`); P-B is a ten-member random pool
(`scripts/nt1p_gates.py:11-21`); P-C consists only of its eight random starts
and has no greedy step (`scripts/SEARCH_PC_Lt12_1512.out:8-9`).  Hence the
three negatives are not all products of chiral-witness tuning.

The point-orbit matrices are not literally smooth test functions, but the
plaquette margins and nonzero overlap gaps allow each orbit point to be
replaced by a sufficiently narrow smooth gauge-invariant bump.  Eigenvalues
vary continuously, so the strict negative survives.  W matching selects orbit
centers and removes the pure-gauge boundary mode; it does not make the witness
gauge-variant.  The kernel nodes have minimum overlap gaps `0.314`, `0.384`,
and `0.290` (`scripts/K_PA_Lt8_1504.out:17`,
`scripts/K_PB_Lt8_2504.out:17`, `scripts/K_PC_Lt12_1512.out:17`).

**Item-3 finding:** the three finite-chart RP negatives, W matching,
gauge-invariant bump-witness interpretation, and controls are confirmed.  $E$
is conservative-looking empirical transport/quadrature evidence, not a proof
of the remaining quadrature error.

## 4. The phase

After removal of the reflection constant, expand the Hermitian chiral kernel
in the small node phases as

\[
  Z^\chi_{ab}=Z^{\rm mod}_{ab}+iA_{ab}+O(\phi^2),\qquad
  A_{ba}=-A_{ab}\in\mathbb R,
\]

where $Z^{\rm mod}$ is the real symmetric kernel obtained by dropping the
node phases.  The first-order term is $i$ times a real antisymmetric matrix.
A real normalized eigenvector $v$ of $Z^{\rm mod}$ therefore satisfies
$v^T(iA)v=0$.  For a nondegenerate eigenvalue, the first nonzero
eigenvalue displacement is consequently second order in the phase (including
the usual second-order mixing term).  The worker's statement is mathematically
correct under the measured reflection/Hermiticity condition, not merely a
numerical coincidence.

The saved data agree: the first-order expectations are `1.1e-8` to `4.5e-8`,
while the finite eigenvalue shifts are `3.6e-7`, `5.5e-6`, and `1.1e-5`, with
lowest-eigenvector overlaps `0.99986`, `0.99938`, and `0.99680`
(`scripts/POST.out:1-3`).  The phase varies by `7.3e-3`--`8.9e-3` across nodes
and individual normalized entries move by up to `3.25e-3`
(`scripts/K_PA_Lt8_1504.out:16`, `scripts/K_PB_Lt8_2504.out:16`,
`scripts/K_PC_Lt12_1512.out:16`), so it is not literally absent.

"The negativity is carried by the modulus" is nevertheless an accurate
description of these matrices: the modulus kernel is separately negative on
all three pools and its lowest eigenpair nearly coincides with the chiral one.
It is not a theorem that the phase is irrelevant for other witnesses, other
measure-current counterterms, or other geometries.

**Item-4 finding:** second-order entry of the phase into the isolated lowest
eigenvalue is confirmed; modulus-carried negativity is confirmed for the three
reported pools, with the stated scope qualification.

## 5. Fixed reading

The fixed reading I find correct is **OPEN**.

- G-LEG(a): pass (`Lx=4`).
- G-LEG(b): **not established**.  The construction is legitimate and
  integrable on the sampled straight-ray chart, but the flat anomaly-free
  finite-volume tail has not been shown to obey the required exponential
  bound, the diagnostic is not a direct measurement of the full measure
  current, and no global Wilson-line-circle completion is supplied.
- G-LEG(c): pass under the fixed wording; L1 visibly fails locality.
- G-LEG(d): pass on the tested geometry.  The reflection constant has spread
  `1.42e-13` at Lt 8 (`scripts/GATES_Lx4_Lt8.out:22-24`), and the directly
  computed Lt 12 matrix has Hermiticity defect `1.63e-7`, included in its error
  estimate (`scripts/K_PC_Lt12_1512.out:12-14`).
- G1 and G5--G7: pass on every evaluated kernel node
  (`scripts/K_PA_Lt8_1504.out:17`, `scripts/K_PB_Lt8_2504.out:17`,
  `scripts/K_PC_Lt12_1512.out:17`).
- Conditional on G-LEG(b), every pool satisfies the numerical
  `CHI-RP-FAIL` inequality by a factor of 22--49 over $E$.

This reading is strictly scoped to two-dimensional compact U(1), 11112,
`Lx=4`, open time with antiperiodic spatial fermions, primary `Lt=8` plus one
`Lt=12` pool, overlap parameter `M=1`, hard crossing support `delta=0.6`,
`beta_g=0`, link reflection, W-matched gauge-invariant witnesses, the one
explicit cohomology/current choice in `nt1p_lib.py`, and its non-wrapping
straight-ray chart.  There is no counterterm scan, no Lx greater than 4 kernel,
no Wilson-line-circle loop test, no torus, no infinite-volume limit, no 4D or
nonabelian result, and no statement that every allowed local measure phase
fails RP.

## Strongest correct statement

For the finite two-dimensional `Lx=4` open-time 11112 overlap system at `M=1`, `delta=0.6`, and `beta_g=0`, the worker has constructed a gauge-invariant and reflection-compatible straight-ray Weyl measure on the non-wrapping chart whose cohomology current exhibits the expected anomaly-cancellation contrast: the anomalous L1 control requires a nonlocal `1/Lx` plateau, while the anomaly-free residual is much smaller and decreases with size.  On three W-matched gauge-invariant witness pools, this chart weight has quadrature-converged negative RP kernels with `lambda_min=-2.4485e-3`, `-9.5787e-4`, and `-5.3679e-4`; the separately reconstructed modulus `|det D(1)|^2|det D(2)|^(1/2)` is negative on all three, and the chiral phase changes the lowest eigenvalue only at second order.  What is not yet established is that the anomaly-free x-flat tail is uniformly exponentially small and that this chart measure extends around the Wilson-line circle as the same legitimate global local Lüscher measure; therefore the strongest fixed reading is OPEN at G-LEG(b), not OPEN at (c), and the data become `CHI-RP-FAIL` if and only if that remaining legitimacy step is accepted or completed.
