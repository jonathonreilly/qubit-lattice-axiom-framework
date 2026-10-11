# VERDICT: CONFIRMED WITH CORRECTIONS

The finite-band C3 obstruction and the associated finite-tower face floor are
confirmed for the report's stated free, periodic, quadratic, standard-generator
class.  Several stronger readings are not established: an arbitrary `N`-site
cell is not thereby a fine lattice; the three-dimensional band count is
mislabelled; the `Z_N` interaction claim is sufficient rather than necessary;
and the loop diagnostics do not by themselves determine a P0-level TT response
or a universal finite-`N*` statement.

## 1. Exact generator equivalence and three dimensions

**Confirmed for a reblocked uniform fine lattice, with a dimensional
correction.**  The worker's matrix is not a general `N`-site-cell network: it
is the uniform one-dimensional fine chain written in `N`-site cells
(`i2_fold.py:25-36`).  Likewise the stored generator calculation is explicitly
one-dimensional (`i2_poincare_exact.py:1-13`).  Its printed `0.0` values are
floating-point evaluations, not an exact-arithmetic certificate—the bracket is
evaluated with NumPy float arrays and polarization (`i2_poincare_exact.py:20-33`)—but
the identity itself is exact by elementary telescoping.

In three dimensions let `L` be the refinement per axis, write a fine site as
`x=L X+delta`, and define

`B_i(X)=sum_delta (delta_i/L)t(X,delta)` and
`T'(X)=T(X)-sum_i[B_i(X)-B_i(X-e_i)]`.

Then, for every component `j`,

`sum_X X_j T'(X)=sum_{X,delta}(X_j+delta_j/L)t(X,delta)=K_f,j/L`.

Consequently `P'_j=-{K'_j,H}=P_f,j/L` exactly.  An independent rational check
gave zero in all three components for `L=2,3,4`, and an independent cubic
folding calculation gave normalized spectral errors `4.44e-16` and `6.58e-16`
for `L=2,3` (`referee_independent_checks.py:20-102`,
`referee_independent_checks.out:1-7`).

The correction is essential: spacing `a/L` in `d=3` uses an `L x L x L`
supercell and hence **`L^3` sites/bands per coarse cell**, not `L` bands.  An
arbitrary `N`-site cell need not possess the internal translations or uniform
couplings of a fine lattice; if `N=L^3`, the isotropic spacing is `a/N^(1/3)`,
not `a/N`.  Thus C3 may be reapplied verbatim to this specifically reblocked
fine cubic lattice with `a -> a/L`.  The report did not separately construct
the three-dimensional rotation-density improvement and admits that rotations
were not computed (`I2_report.md:75`); reblocking makes an analogous local
construction available, but the stored `0.0` test covers boosts/momenta only.

## 2. C1 two-band equivalence

**Sound for the specific one-dimensional C1 ansatz, but not proved by the
spectrum alone and not established in three dimensions.**  The numerical test
only compares the eigenvalue multiset and samples high Fourier coefficients
(`i2_sumrule.py:79-91`).  However, C1's actual matrix has equal diagonals and an
off-diagonal factor `(1+e^{ik}) alpha(k)` (`RC_C1_report.md:186`).  It therefore
commutes with the exact fine-site translation

`T_f(k)=[[0,e^{-ik}],[1,0]]`, with `T_f(k)^2=e^{-ik} I`.

The independent check finds `||[h,T_f]||_inf <= 3.33e-16` and zero square-law
residual (`referee_independent_checks.py:105-126`,
`referee_independent_checks.out:8-9`).  This is stronger and cleaner than the
report's unexecuted quasi-local-unitary argument.  The unfolded `4pi`-periodic
band is therefore an exact fine chain, and its fine-face residual is exactly
`2pi=pi N` for `N=2`; the `6.2825` value is only the finite-difference endpoint
approximation (`i2_sumrule.out:12-18`).  But C1 checked this construction only
in 1D (`RC_C1_report.md:196,236`); its `d=2,3` extension was merely suggested
and would require `2^d` bands (`RC_C1_report.md:247`).

## 3. S1, S2, and the band-diagonal reduction

**S1 is exact; the reduction is valid under the stated standard-generator
hypotheses.**  For `u_n=lambda_n(W)/2`,
`sum_n u_n=tr(W)/2`, so the distributional band sum of every Hessian has zero
Brillouin-zone integral.  Crossings do not alter the trace identity.  This is
the same sum rule as I1's Theorem 2 (`I1_report_unrefereed.md:107-116`), with
I1 slightly broader because it allows distributional periodicity and arbitrary
locality; I2 assumes periodic `C^2` `W` (`I2_report.md:93-97`).  The random
network rerun reproduced residuals at `1e-13`-level or below
(`i2_sumrule.out:1-10`).

The report labels the band-diagonal step “ARGUED,” but it closes in the regular
first-moment setting.  In one-particle notation,
`K={X,h}/2+a` gives `P=i[h,K]=D(h^2)/2+i[h,a]`.  Conservation `[h,P]=0` removes
all matrix elements between distinct energy eigenspaces.  Projected onto a
degenerate energy block, the commutator term vanishes and
`P=partial(E^2/2)` times the block identity.  Hence Berry-connection
commutators have zero block diagonal, and the diagonal bracket is
`E Hess(E^2/2)` almost everywhere; isolated crossings are handled
distributionally.  Requiring one nonzero C3 structure constant `beta` for all
bands then contradicts S1.  This does not cover altered boosts, extra
band-resolved constraints, singular improvements, or interacting/dressed
many-body sectors; those are outside the stated class.  I1 states the same
reduction at `I1_report_unrefereed.md:47-59` but is itself unrefereed.

**S2 is also correct with a scope qualifier.**  If `N` bands are assigned to
`N` lifted tower branches, `sum_n f_n=(tr W/2)'` is periodic while
`sum_n beta K_n` changes by `2pi beta N` across the face.  Therefore one face
side has `|sum_n(f_n-beta K_n)| >= pi |beta| N`, and consequently the sum of
absolute residuals obeys the same lower bound (`I2_report.md:107-110`).  This
is a theorem about approximation to the specified tower lift, not an
observable attached to an arbitrary network with no tower assignment.  In a
three-dimensional `L^3`-band supercell the corresponding band count is
`N_band=L^3`.

## 4. Scattering and the `Z_N` claim

**The calculations reproduce; the claimed necessity does not follow.**  The
rerun exactly reproduced the on-shell, thermal, vacuum-loop and perturbed-cell
tables (`i2_umklapp.py:24-113`; `i2_umklapp.out:1-35`).  Exact fine translation
is sufficient to impose the displayed selection rule, and the chosen forbidden
vertex amplitude turns on as `O(delta)` under the tested random onsite
perturbation (`i2_umklapp.out:27-35`).  A scattering probability/rate would
start as `O(delta^2)`.

One perturbation family does not prove that every tower-normal interaction
must possess that symmetry.  Projected or fine-tuned vertices, decoupled
sectors, or other charges can give zeros without a geometric fine translation;
a necessity theorem would need robustness/genericity and locality hypotheses
that are not supplied.  Moreover `T_f^N=T_coarse` is a translation extension,
not simply an onsite internal `Z_N`, and it only removes coarse-reciprocal
tower-changing processes.  Ordinary fine-lattice umklapp remains and becomes
order one near the truncation edge (`i2_umklapp.out:1-12`), with a large
zone-sampled fraction (`i2_umklapp.out:14-25`).  Thus the finite construction
does not meet the fixed PASS requirement of interacting matter free of
umklapp (`TESTS.md:1281-1284`).

## 5. Scalings, loop weights, and readout

**The displayed nearest-neighbour and improved-stencil scalings are correct.**
Independent symbolic expansion gives
`A=-x^2/2,-x^4/6,-x^6/20,-x^8/70,-x^10/252+...`, and the exact face sequence is
`-2,-8/3,-16/5,-128/35,-256/63`, consistent with
`i2_fold.py:78-93` and `i2_nstar.py:1-17`.  Full reruns reproduced the stored
tables.  A separate uniform-grid 3D quadrature gives, for `N=4,16,64`,
`R_1=(-1.090879,-1.092062,-1.092138)`,
`R_-1=(-0.879896,-0.874549,-0.873981)`, and
`abs/N^4=(-1.310001,-1.304190,-1.303826)`
(`referee_independent_checks.out:10-13`).

Three qualifications are required.

1. The exact `-1` theorem is the **unweighted signed** zone-and-band average.
   The loop-weighted ratios are not exactly `N`-independent at finite mass;
   after `K=Nx`, they depend on `m/N` and only approach constants for the
   selected UV-dominated weights.  The worker's own `R_-3` and `R_-5` rows vary
   strongly with `N` (`I2_report.md:79-84`).  No universal weighted-loop sum
   rule follows from S1.
2. The `N^4` absolute growth is correct for this `d=3` nearest-neighbour scalar
   when `N` denotes linear refinement (`N^3` modes times cutoff energy `N`),
   not for every finite-band network and not when `N` denotes the total band
   count (`I2_report.md:77-89`).
3. The window-only `N*` arithmetic is correct conditional on the assumed
   response law and with `N` interpreted as linear refinement
   (`i2_nstar.out:1-15`).  Exact-closure `N*` is indeed infinite.  But a
   P0-level **loop/TT-response** `N*` is not established: the report itself says
   the TT response is I3's unperformed computation (`I2_report.md:42,230`) and
   finally makes the no-finite-`N*` claim conditional on “relative anomaly ->
   response” (`I2_report.md:240-250`).

## 6. Fixed-reading verdict

Against the fixed readings (`TESTS.md:1259-1285`), I2 does establish the
“every finite-`N` truncation inexact” component **for its explicitly stated
free finite-component periodic `C^2` quadratic class, with the standard
first-moment boost/conserved energy current and the band-diagonal C3/HDA
sector**.  S1 alone rules out exact nonzero-`beta` C3 closure at every finite
band count, and S2 locates an aggregate C1 residual at a finite tower's face.
It does not prove the statement for arbitrary interacting composites,
singular/nonperiodic constructions, altered generators/constraints, or every
network allowed by the four axioms.  Nor can I2 set the lane FAIL: the fixed
clause separately requires I1's infinite-degree necessity and I3's
non-decaying anomaly or TT response (`TESTS.md:1281-1284`), and I1 is
unrefereed while I3 is not supplied here.

## Strongest correct statement

For a free quadratic theory with a finite-dimensional Hermitian periodic `C^2` Bloch dynamical matrix, the standard first moment of a local energy density (up to regular translation-invariant improvement), its conserved energy current, and one common nonzero C3/HDA coefficient `beta`, conservation makes the current scalar on each energy eigenspace and band-diagonal almost everywhere; periodicity then gives `sum_n integral_BZ Hess(lambda_n/2)=0`, so the signed band-and-zone averaged boost anomaly is exactly `-beta` per mode and no finite band count closes C3 exactly, while any `N_band`-branch tower assignment also has an aggregate C1 face residual at least `pi |beta| N_band`.  A uniform `L x L x L` cubic supercell is exactly a reblocking of a fine lattice of spacing `a/L` with `L^3` bands and admits the exact local divergence improvement above, and the specific one-dimensional C1 two-band ansatz is exactly the `a/2` folded chain; these facts do not make an arbitrary `N`-site cell a fine lattice, do not prove that all tower-normal interactions require an internal `Z_N`, and do not determine a universal loop-weighted TT response or P0-level `N*` without I3.
