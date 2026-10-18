# X3 pre-registration (written 2026-10-14 ~14:18Z, BEFORE any run)

Agent: Claude Opus 5.5 (same family as supervisor and route agents; not a referee).
Nothing below has been run when this file was written. Amendments, if any, are
appended below a dated line and never overwrite this text.

## T-X3: where do the free overlap's would-be doublers sit after OS reconstruction?

### Object
Free overlap Dirac operator on Euclidean Z^4 (a_t = a_s = 1, infinite time extent
emulated by an N4-point p4 grid, N4 = 4096), Neuberger form

    D = 1 + X / sqrt(X^dag X),  X = sum_mu i gamma_mu sin p_mu + sum_mu (1 - cos p_mu) - M,

Euclidean Hermitian gammas, chiral basis (gamma5 = diag(1,1,-1,-1), gamma4 = sigma1 x 1),
M in {0.5, 1.0, 1.5, 1.9}. At fixed spatial momentum p the time correlator is
C(t;p) = int dp4/2pi e^{i p4 t} D^{-1}(p4, p), t >= 1 (4x4 matrix).

Controls (same code path):
- POS: Wilson r = 1, mass m = +0.5 (known link-RP, positive transfer matrix; Lüscher 1977,
  recalled). Used to FIX the reflection convention Gamma in {+gamma4, -gamma4} x {left, right}
  as the one making the POS control's link Hankel form PSD. If no Gamma makes POS PSD,
  the test is declared BROKEN (no reading).
- NEG1: naive fermion (r = 0), m = +0.5: has a time-doubler pole at lambda = -e^{-E} (control
  that the code detects a pi-type (negative transfer eigenvalue) sector).
- CMP: Wilson r = 1 with mass -1.5 (B(p) < 0 near p = 0): comparator for overlap M > 1.

### Analytic predictions made before running (to be checked, not assumed)
With beta(p) = 1 - M + sum_k (1 - cos p_k), S^2 = sum_k sin^2 p_k, z = e^{i p4}:
- omega^2 = 1 + S^2 + beta^2 - beta (z + 1/z)  (linear in z + 1/z).
- D^{-1} = 1/2 - i gamma.s / (2 (omega + b)), b = beta - cos p4.
- Light pole: z1 = e^{-E}, sinh E = S, present iff beta < sqrt(1 + S^2); at the 15 doubler
  corners (spatial corners and the time corner) NO pole for 0 < M < 2.
- Cut (the would-be doubler content): branch point z_b with cosh E1 = (1 + S^2 + beta^2)/(2|beta|);
  transfer eigenvalues lambda in (0, e^{-E1}] if beta > 0, in [-e^{-E1}, 0) if beta < 0.
  So for M <= 1 everything has lambda > 0; for 1 < M < 2 a pi-type (lambda < 0) continuum
  appears for spatial momenta with beta(p) < 0 (a ball around p = 0).
- E1_min(M = 1) = ln 2 ~ 0.69 (at the (pi,0,0)-type corners); E1(p=0, M=0.5) = ln 2.

### Measurements
(a) Decomposition check: C_FFT(t) (t = 1..12) vs pole term + numerically integrated cut term,
    over >= 40 spatial momenta (random + near each corner) per M. Sign of the cut term fixed
    by the formula, not fitted. Max relative residual reported.
(b) Light-state count: over the full 16^3 spatial momentum grid (and exact corners), the set
    where a pole exists; its energy E_p(p); points with E_p < 0.3; rank of the pole residue in
    the full Dirac 4x4 and in each Weyl block (gamma5-projected rows/cols per Kikukawa-Usui (47)).
(c) Doubler location: E1(p) over the grid: min, value at the 15 doubler corners; sign of lambda.
(d) Positivity: Gamma-weighted residue and cut densities PSD (link form: Gamma W / lambda PSD);
    model-independent cross-check by block-Hankel matrices H0_ij = Gamma C(i+j-1),
    H1_ij = Gamma C(i+j), i,j = 1..6, min eigenvalue / max eigenvalue > -1e-10 counts as PSD.
(e) Reconstructed per-site dimension: numerical rank (tol 1e-11 rel) of H0 for n = 2..8 blocks:
    Wilson r = 1 saturates at a fixed small rank; overlap rank grows with n (continuum).

### Readings (fixed now)
- **PASS** ("doublers harmless"): there is a window of M containing M = 1 in which ALL hold:
  (i) exactly one light pole region (contains p = 0, contains no doubler corner), E_p -> 0 only at
  p = 0; Dirac residue rank 2 and each Weyl block rank 1 (one light Weyl per chirality projection);
  (ii) no pole at any of the 15 doubler corners (spatial or time);
  (iii) the doubler content is a continuum with lambda > 0 only, E1(p) >= 0.3 for all p
  (i.e. >= O(1/a));
  (iv) positive weight: Gamma-weighted residue and cut density PSD, H0 and H1 PSD (T >= 0);
  (v) decomposition residual <= 1e-8 (so no hidden extra poles).
- **FAIL-pi** ("pi-type copy"): at M = 1 (or every M in (0, 2)) a lambda < 0 sector exists with
  E1 < 0.3 or a pole at a doubler corner, i.e. the Euclidean analogue of F3-A's pi copy is light.
- **FAIL-RP**: negative weight (H0 indefinite beyond tolerance) at M = 1.
- **OPEN**: decomposition residual > 1e-8, or POS control not PSD for any Gamma (test BROKEN).
- **Secondary reading (recorded either way, not part of PASS/FAIL):** for 1 < M < 2, whether the
  predicted lambda < 0 continuum exists, its threshold, and whether H0 stays PSD there
  (link-RP with negative transfer eigenvalues) or not (link RP lost: a scope limit on the
  Kikukawa-Usui theorem, whose contour (their eq. 27-28) sits on Re p0 = 0 only).

Expectation (stated before running): PASS for M in (0, 1]; for M in (1, 2) a gapped pi-type
continuum near p = 0 (threshold ~ 0.69 at M = 1.5, ~ 0.1 at M = 1.9); its RP status I do not
predict.

Budget: numpy only, < 100 MB, OMP_NUM_THREADS=2, < 10 min.

---
### Amendment A1 (2026-10-14 14:19Z by `date -u`, still BEFORE any run; nothing executed yet)
Working the contour orientation out by hand (principal square-root branch, continuous on the
disc minus the cut) before coding gives two refinements of the predictions. The readings above
are unchanged.
- beta > 0 cut: C_cut(t) = (1/2pi) int_{E1}^inf e^{-Et} (g4 sinh E - i g.s) |omega| / (sinh^2 E - S^2) dE,
  so gamma4 x density has eigenvalues (sinh E +- S) x positive: PSD (positive weight, lambda > 0).
- beta < 0 cut (only M > 1): C_cut(t) = int lambda^t W dE with lambda = -e^{-E} and gamma4 W NSD,
  so gamma4 W / lambda is PSD. Prediction: for 1 < M < 2 LINK RP SURVIVES, but the transfer
  matrix has negative eigenvalues (H1 = Gamma C(i+j) indefinite), exactly like Wilson r = 1 with
  B(p) < 0 (comparator CMP). I.e. a gapped, positive-norm, NON-inverted pi-sector.
- Light residue: gamma4 x Res is block diagonal in the chiral basis, blocks sinh E +- sigma.s,
  rank 1 each at sinh E = S: one helicity state per Weyl block.

---
## T-X3b (registered 2026-10-14 ~14:28Z, after T-X3 ran, BEFORE T-X3b is written or run)

**Why.** T-X3 settles the free theory. The set-B package's open lemma L3g is RP once gauge
fields are dynamical. A NECESSARY condition for it: in every theta-symmetric background
(U on Lambda- equal to the theta-image of U on Lambda+; crossing temporal links = 1),
the fermion's one-particle RP matrix P_xy = Gamma D^{-1}(x, theta y), x,y in Lambda+, must be PSD
(take F = f(U+) psi-linear with f concentrated near a background u; the gauge cross terms are
positive numbers there). K-U's sufficient criterion (iv) is also measured: cross kernels
Q1 = [D(x, theta y) g0] and Q2 = [g0 D(theta x, y)], sign fixed by the free Wilson control.

**Object.** 2D, U(1), L_x = 8 periodic, t in {-3..4} antiperiodic (K-U's finite lattice),
link reflection t -> 1 - t. Massive Dirac overlap D_m = (1 - m/2) D + m, m = 0.05, M = 1
(and M = 1.5 as a side run); Wilson r = 1 (m = 0.05) as positive control in the same backgrounds.
Gamma calibrated on free Wilson (must be PSD; else BROKEN).
Backgrounds (>= 20 each): (S) static: all temporal links 1, spatial links exp(iA(x)) the same on
every slice, A ~ N(0, s^2); (E) generic theta-symmetric: independent random temporal and spatial
links on Lambda+ (mirrored to Lambda-), A ~ N(0, s^2); s in {0.3, 1.0}.

**Readings.**
- **BG-PASS:** overlap P PSD (min eig / max eig > -1e-10) in all S and E backgrounds at both s.
  Then the per-background necessary condition holds; L3g's remaining obstruction is the
  non-factorization of D[U] across the plane (K-U criterion (iv)), measured separately.
- **BG-E-FAIL:** P PSD in all S backgrounds but < -1e-6 in some E background: the gauged
  Dirac overlap is not RP with dynamical gauge fields at fixed lattice spacing (the necessary
  condition fails exactly when [nabla_0, nabla_k] != 0).
- **BG-FAIL:** fails already in S backgrounds.
- **OPEN:** Wilson control fails, or results in between thresholds.
Expectation (stated before writing the script): BG-PASS for P in S backgrounds; I do not predict E.

### T-X3b result line (recorded 14:26Z; full output scripts/tx3b_gauged_rp_2d.out)
BG-PASS: overlap P PSD in all 160 theta-symmetric backgrounds (S and E, s = 0.3 and 1.0, M = 1 and 1.5);
K-U cross kernels Q1 NSD / Q2 PSD in every one; Wilson control PSD throughout.

---
## T-X3c (registered 2026-10-14 ~14:28Z, BEFORE writing or running it)

**Why.** T-X3b only tests backgrounds that are theta-symmetric across the plane (the diagonal
U- = theta U+). Full RP needs the kernel in (U+, U-) to be positive-type OFF the diagonal, because
the overlap kernel couples U+ and U- non-factorizably. At gauge coupling beta_g = 0 (where RP must
also hold if it holds for all couplings) the gauge cross factor is the all-ones kernel, so a
NECESSARY condition is: for any finite set u_1..u_k of Lambda+ configurations, the matrix
Z_ab = det D_m[(u_a on Lambda+, theta u_b on Lambda-)] (crossing links = 1) is Hermitian PSD, and
in the one-particle sector the block matrix B[b,a] = Z_ab * Gamma D_m^{-1}[(a,b)](x, theta y) is PSD.

**Object.** Same lattice as T-X3b (2D U(1), 8 x 8, antiperiodic t), D_m = (1 - m/2) D + m, m = 0.05,
overlap M = 1; Wilson r = 1 (m = 0.05) control (must be PSD, else BROKEN). k = 8 configurations per set,
10 sets per (type, s); types: S (each u static inside its half: temporal links 1, spatial links
t-independent) and E (generic); s in {0.3, 1.0}. Report min eig / max |eig| of Z (normalized
Z_ab / sqrt(Z_aa Z_bb)) and of B, Hermiticity defects.

**Readings.**
- **Z-PASS:** overlap Z and B PSD (> -1e-10 relative) in every set, Wilson PSD: evidence (not proof)
  that the vector-like gauged overlap meets the off-diagonal necessary condition at beta_g = 0.
- **Z-FAIL:** some overlap set has min eig < -1e-6 relative while Wilson is PSD in the same sets:
  the gauged overlap measure (this formulation, link reflection) is NOT reflection positive at
  beta_g = 0 on this lattice: L3g fails as posed; the set-B package then needs a different
  gauge-fermion coupling or the R2-4 price Pi-W (non-positive / complex weight) for matter too.
- **OPEN:** in between, or control fails.
Expectation (before running): Z-FAIL at a small relative size (the overlap determinant is a
Hadamard ratio of two RP-positive kernels, DWF fermion over Pauli-Villars boson, which need not be
positive-type). Low confidence.

### T-X3c result line (recorded ~14:29Z; output scripts/tx3c_offdiag_rp_2d.out)
As registered (crossing links fixed to 1 on both planes, i.e. the axial-gauge-fixed formulation):
**Z-FAIL**. Overlap Z min eig / max = -6.2e-3, -0.31, -1.9e-2 (S 0.3, S 1.0, E 0.3; E 1.0 stayed PSD);
one-particle B (in the arrangement where the Wilson control is Hermitian PSD) -1.0e-2, -0.34, -2.3e-2, -0.23.
Wilson control PSD everywhere (Z >= +8e-4 relative, B >= -5e-16).
**Caveat found after the run (my own check, not a referee):** with crossing links fixed, f concentrated on
one configuration is not gauge-invariant under gauge rotations of the Lambda+ boundary slices. Physical RP
only needs gauge-invariant F. So T-X3c tests the gauge-fixed formulation; it does not by itself establish
failure on gauge-invariant observables. Hence T-X3d.

---
## T-X3d (registered ~14:30Z, BEFORE writing or running it): gauge-invariant version

**Necessary condition, gauge-invariant form.** For f depending only on gauge-invariant data of U+, at
gauge coupling beta_g = 0 the kernel is Zt_ab = int dU_c det D_m[(u_a, U_c, theta u_b)], with the crossing
links U_c Haar-integrated (equivalently: averaged over gauge rotations of u_a's boundary slice).
Zt must be Hermitian PSD.

**Object.** 2D U(1), Lx = 4 periodic, t in {-3..4} with OPEN time ends (one reflection plane, between
t = 0 and 1; four crossing links). Overlap M = 1, m = 0.05; Wilson r = 1 control (its det is a
trigonometric polynomial of degree <= 1 per crossing angle, so an n >= 3 grid is exact for it).
Haar integral by an n^4 product trapezoid grid, n = 6, with an n = 4/6/8 convergence check on one set.
k = 5 configurations per set (generic E type: random spatial and temporal links on Lambda+),
s in {0.3, 1.0}, 4 sets each.

**Readings.**
- **GI-FAIL:** overlap Zt has min eig / max < -1e-6 AND larger in size than 10x the n=6 vs n=8 change,
  in some set, with the Wilson control PSD: the gauged overlap measure violates RP on gauge-invariant
  observables at beta_g = 0 (this lattice): L3g fails as posed.
- **GI-PASS:** Zt PSD (min > -max(1e-10, 10x quadrature change)) in every set: the T-X3c violation was
  a gauge-fixing artefact; L3g stays open.
- **OPEN:** otherwise, or control fails.
Expectation: I do not predict; T-X3c's sizes (up to -0.3) suggest GI-FAIL survives averaging, but
averaging over boundary gauge rotations can restore positivity.

### T-X3d result line (recorded 14:41Z; scripts/tx3d_gauge_invariant_rp_2d.out; run killed after 5 of 8 sets)
**OPEN (quadrature not converged).** Wilson control: PSD, n-independent to 4e-15 (exact, as expected).
Overlap: the Haar-integrated kernel is NOT converged on the n^4 grid: min eig/max = +3.5e-2 (n=4),
+4.9e-3 (n=6), -6.0e-4 (n=8); max |Zt(8) - Zt(6)| = 4.1e-2. The n = 6 sets (all positive, +3e-3..+2e-2)
are therefore not readable. Likely cause (reading): Haar-random crossing links make crossing plaquettes
large, H_W gets zero modes, and det D_ov jumps (the overlap is discontinuous there), so the trapezoid rule
converges slowly. This is itself the admissibility issue (Lüscher's plaquette bound is a CROSS-PLANE
support constraint).

---
## T-X3e (registered 14:41Z, BEFORE writing or running it): same as T-X3d with Lx = 2
Two crossing links only, so an n^2 grid with n in {32, 64, 128} is affordable. 2D U(1), Lx = 2 periodic,
t in {-3..4} open ends, overlap M = 1, m = 0.05, Wilson r = 1 control; k = 5 configurations per set,
E type, s in {0.3, 1.0}, 4 sets each; main runs at n = 128 with the n = 64 change reported per set.
Readings as T-X3d: **GI-FAIL** if min eig/max < -1e-6 and |min| > 10 x max|Zt(128) - Zt(64)| in some set
(Wilson PSD); **GI-PASS** if every set has min eig/max > -max(1e-10, 10 x quadrature change);
**OPEN** otherwise. Also reported: the fraction of grid points where min|H_W| < 0.05 (non-admissible).
No expectation.

### T-X3e result line (recorded 14:45Z; scripts/tx3e_gauge_invariant_rp_2d_Lx2.out; killed after 1 of 8 sets)
**OPEN.** Killed for memory (280 MB resident > 0.25 GB rule). One set (s = 0.3): Wilson PSD exact (-2.4e-16,
dZ 6e-16); overlap min eig/max -2.6e-4 (n=64), -1.5e-4 (n=128) but quadrature change 6.2e-3 >> |min|, so no
reading. 65.5% of the Haar grid has min|H_W| < 0.05: Haar-integrated crossing links are mostly
NON-ADMISSIBLE, where the overlap is discontinuous. The gauge-invariant test must integrate crossing links
over the admissible set only (plaquette bound), which makes the measure's support itself a cross-plane
constraint. Not run.

---
## T-X3f (registered 14:47Z, BEFORE writing or running it): gauge-invariant RP on the ADMISSIBLE set
Same as T-X3d (2D U(1), Lx = 4 periodic, t in {-3..4} open, one plane, overlap M = 1, m = 0.05, Wilson r = 1
control), but the crossing-link Haar integral is restricted to the admissible set |arg P_x| < delta = 0.5 for
the four cross plaquettes (the global crossing phase is a gauge zero mode and is dropped). Variables
d_x = arg P_x, nested Gauss-Legendre with exact piecewise-linear limits for d_2; n = 8 vs n = 12 change
reported. u's: random links N(0, s^2), s in {0.15, 0.3}; k = 5 per set, 3 sets per s.
Note derived before running (proved, character expansion): at beta_g = 0 the pure-gauge part of this
kernel is sum_n c_n^4 (W_b conj W_a)^n with c_n = sin(n delta)/(n pi); since Lx = 4 is even, it is
positive-type. So the admissibility indicator alone does not break RP here, and Wilson + indicator is a
fair control.
**Readings.** GIA-FAIL: overlap min eig/max < -1e-6 and |min| > 10 x max|Z(12) - Z(8)| in some set, with
Wilson + indicator PSD within its own quadrature error. GIA-PASS: overlap PSD within quadrature error in
every set (evidence for L3g at beta_g = 0, admissible, on this lattice). CONTROL-FAIL: Wilson + indicator
also fails (then the indicator, not the overlap, is responsible). OPEN otherwise. Also reported:
min|H_W| over all evaluated points, which must stay > 0.05 for the admissible reading to be clean.
No expectation.

### T-X3f result line (recorded 14:49Z; killed after 1 of 6 sets for memory, 306 MB)
One set (s = 0.15): Wilson + indicator min eig/max +1.3e-3 (n=8), +6.3e-4 (n=12); overlap +3.4e-3, +1.2e-3;
quadrature change 5.7e-3 for both; min|H_W| = 0.021 (< 0.05, so the admissible reading is NOT clean at
delta = 0.5). No reading (OPEN); direction: no violation seen.

### Amendment T-X3f' (registered 14:49Z, BEFORE the rerun)
Rerun with eigen-batch chunk 64 (memory), delta = 0.3 (tighter cross-plaquette bound), s = 0.15 only,
3 sets, n = 8 and 12. Readings unchanged from T-X3f (GIA-FAIL / GIA-PASS / CONTROL-FAIL / OPEN), plus:
the reading counts as clean only if min|H_W| > 0.05 over all evaluated points.

### T-X3f' result line (recorded 14:55Z; scripts/tx3fp_admissible_gi_rp_2d.out; peak RSS 261 MB = 249 MiB, at the limit)
Overlap min eig/max (n=12) +2.1e-3, +2.5e-3, +3.5e-3; Wilson + indicator +1.3e-3, +2.0e-3, +1.3e-3; quadrature
change 2.6e-3 to 5.7e-3 (same size as the eigenvalues). Formally **GIA-PASS** (no negative eigenvalue, and
min > -10 x quadrature change), but **NOT CLEAN**: min|H_W| = 0.002-0.021 < 0.05 (bulk plaquettes up to 0.74),
and the quadrature error equals the signal. Reading: no RP violation seen on gauge-invariant observables
over the admissible crossing set; not decisive.

### Diagnostic D1 (registered 14:55Z, before running; no PASS/FAIL, diagnostic only)
On the SAME lattice and SAME configurations as T-X3f' (seed 31, s = 0.15, 3 sets), compute the gauge-FIXED
kernel (crossing links = 1, T-X3c style). If it is non-PSD where the admissible gauge-averaged kernel was PSD,
the T-X3c violation is attributed to gauge fixing (non-gauge-invariant observables), not to the overlap.
If it is PSD too, T-X3c's violation is lattice/ensemble-specific and unattributed.

### D1 result line (recorded 14:55Z; scripts/d1_gaugefixed_same_configs.out)
Gauge-fixed kernel on the same configs: Wilson PSD (+4.7e-5, +6.1e-5, +6.1e-5); overlap NEGATIVE (-1.0e-4,
-1.4e-3, -1.2e-3), where the admissible gauge-averaged kernel was positive (+2.1e-3..+3.5e-3, with quadrature
error ~5e-3). So the T-X3c violation is reproduced in the gauge-fixed form and is not seen after gauge
averaging: consistent with a gauge-fixing (non-gauge-invariant observable) effect; not decisive.
