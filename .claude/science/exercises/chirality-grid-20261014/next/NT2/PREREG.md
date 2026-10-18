# NT-2 PREREG: is the hard plaquette bound |arg U_p| < delta itself reflection-positive in 3D pure U(1)?

Written 2026-10-14 ~20:58Z (`date -u` at start of session 20:44Z), before any NT-2 run. Never edited after
the first run; any change goes in a dated follow-up section at the end.

Agent: Claude Opus 5.5 (test agent NT-2), same family as K2c, its referee input aside. Folder:
`scratchpad/chirality_ex/next/NT2/`. Memory cap 0.4 GB per run, one process at a time, OMP_NUM_THREADS=2.

FIXED readings (TESTS.md, item NT-2, not changed here):
- **PG3-NEG**: a converged negative eigenvalue (the bound itself is not RP in 3D).
- **PG3-PSD**: PSD on searched pools at power.
- **OPEN**: otherwise.

## 1. Model

- 3D lattice = (2D spatial slice) x (time), U(1) links, beta_g = 0 (no Wilson term).
- Measure: Haar on every link times the hard indicator f(theta_p) = 1(|arg U_p| < delta) on EVERY plaquette
  (spatial and temporal). delta = 0.6 (K2c's value) is primary.
- Link reflection: the plane bisects the temporal links between slices t = 0 and t = 1. Theta maps t -> 1 - t
  (with complex conjugation of observables, K2 convention). Crossing plaquettes = the temporal plaquettes on the
  crossing links, one per spatial link of the slice.
- Open time is primary. (Reduction to the time-torus: see Sec. 2(e).)

Slice geometries:
- **T22 (primary)**: spatial slice = 2x2 periodic torus (4 sites, 8 links, 4 plaquettes; 8 crossing plaquettes).
- **O22 (primary)**: spatial slice = open 2x2 block of plaquettes (3x3 sites, 12 links; 12 crossing plaquettes).
- **O12 (secondary)**: open 1x2 strip (2x3 sites, 7 links, 2 plaquettes): the minimal slice that carries the
  referee's closed current 3dP1 - 3dP2 (coefficient c6 c3^6 < 0).
- **Controls**: the 2D proxy (1D slice, Lx = 2 periodic: PSD; Lx = 3: negative, -8.95e-3 relative, K2c V1 and
  its referee), rebuilt with this folder's code.

## 2. Reductions to be used (to be written out as proofs in REPORT; labelled proved only after checking)

(a) **Kernel.** For gauge-invariant positive-half observables F, integrating the crossing links and using
positive-half gauge invariance gives <Theta(F) F> = sum over boundary-slice configurations u, v of
G(u) conj(G(v)) K(u, v), K(u, v) = integral over slice gauge transforms g of prod_l f(u_l - v_l + (dg)_l),
where G(u) = (positive-half marginal weight) x F restricted to the boundary slice. Every gauge-invariant G
supported in the admissible boundary set S_delta = {all slice plaquettes |phi_p| < delta} is realisable
(the bulk marginal is > 0 there). So: RP <=> K is a PSD kernel on gauge-invariant functions on S_delta.
Point-configuration matrices [K(u_i, u_j)] are legitimate witnesses because K is continuous (K2c referee's
bump-function argument).

(b) **Fourier form.** K(u, v) = sum over integer closed currents n on the slice of C(n) e^{i n.(u - v)},
C(n) = prod_l c_{n_l}, c_n = sin(n delta)/(n pi). Negative C(n) shows non-RP only on the full group; the
restriction to S_delta (all slice plaquettes in (-delta, delta)) is exactly what the referee said is missing.

(c) **T22 closed form (derived before running; to be checked numerically by an independent builder).**
Gauge-invariant coordinates: row Wilson lines X0, X1, column Wilson lines Y0, Y1, and plaquettes phi_p.
K(u, v) = (2 pi)^-3 (B_a0 * B_a1 * B_b0 * B_b1)(sigma), where B_a = indicator of [-a/2, a/2],
a_j = (2 delta - |X_j(u) - X_j(v)|)_+, b_i = (2 delta - |Y_i(u) - Y_i(v)|)_+ (differences reduced to (-pi, pi]),
sigma = (Delta phi_10 + Delta phi_01)/2; valid for 4 delta < pi. Also X1 = X0 - (phi00 + phi10),
Y1 = Y0 + (phi00 + phi01). S_delta in coordinates (P, Q, R) = (phi00+phi10, phi00+phi01, phi10+phi01) is the
octahedron |P| + |Q| + |R| < 2 delta, times the free holonomy torus (X0, Y0).

(d) Expected PSD sub-families (to be proved in REPORT): fully W-matched pools (all four Wilson lines equal)
give K = (B_{2delta})^{*4}(Delta sigma), Fourier transform (2 sin(delta w)/w)^4 >= 0, so PSD; pools with all
plaquettes equal and only holonomies varying are PSD (tau-representation). So the W-matching that exposed
the overlap's failure in K2c is NOT a power source here; the open directions are mixed holonomy/plaquette ones.

(e) Time-torus: if a single plane gives a negative matrix, fixing the far-boundary slice configuration to one
common value makes the second plane's factor a positive constant, so the torus (two planes) is negative too.

## 3. Pools and searches (all configurations admissible with margin: every slice plaquette |phi_p| <= delta - 0.05)

For T22 (kernel exact, closed form):
- P1 random: k = 24 configs, uniform in the margin octahedron, holonomies X0, Y0 uniform on the circle. 20 seeds.
- P2 W0-matched: as P1 but X0 = Y0 = 0 for all members. 20 seeds.
- P3 fully W-matched (control, expected PSD by 2(d)).
- P4 structured: product grids {plaquette grid points} x {N equally spaced X0 (and/or Y0)}; also the
  holonomy-charge-projected kernel K_{nm}(P, Q, R) evaluated through such rings (N = 32 or 64).
- P5 searched: random-perturbation / greedy hill-climb on k = 16..32 member pools minimising
  lambda_min of the unit-diagonal-normalised matrix (inertia-preserving), started from P1 and P2;
  at least 8 searches per start type, 400 steps each (more if cheap).
For O22 and O12 (kernel by quadrature; see Sec. 4): P1, P5 analogues plus regular grids in plaquette space
(O12: 2D grid in (-0.55, 0.55)^2 up to 41^2 points; O22: 4D grid up to 7^4 points if cost allows).

**Power references (must succeed for a PSD reading):**
- R1 (unrestricted domain): the same kernel and the same search code, but slice plaquettes allowed up to
  |phi_p| <= pi - 0.05 (outside S_delta, i.e. not admissible). Non-RP on the full group is guaranteed by 2(b)
  (C(n) < 0 exists); the search must find a converged negative there within the same budget.
- R2: the 2D Lx = 3 control: holonomy ring N = 64 reproduces -3.99e-3 / -8.95e-3 relative.

## 4. Numerics and error estimates

- T22: closed form (signed truncated-power formula for the 4-box convolution). Independent builder: explicit
  link angles on the 8 links -> intervals A_j, B_i computed on the circle from the links -> the tau-integral of
  the product of two interval-overlap trapezoids done exactly (piecewise quadratic; breakpoints + Gauss).
  E = k * max_ij |K_closed - K_indep| + k * 1e-15 * max|K|.
- O12: K(Phi) = int de b(e) T3(Phi1 - e) T3(Phi2 + e) (b = box on (-delta, delta), T3 = b*b*b); exact by
  Gauss-Legendre on breakpoint pieces (piecewise degree 4). Independent: composite rule on a uniform fine grid
  with two resolutions. E as above.
- O22: K(Phi) = int_{[-delta,delta]^4} de prod_p T(Phi_p + e_{p-1} - e_p) (T = b*b, cyclic in p). Computed by
  Nystrom/Gauss-Legendre at two resolutions (and with smoothed test functions if point kernels converge too
  slowly). E = k * max entry change between levels (a-posteriori, as K2c; referee's wording applies:
  "quadrature-converged", not certified).
- **Converged negative**: lambda_min < -10 E and lambda_min/lambda_max < -1e-9, sign reproduced by the
  independent builder.

## 5. Readings (consistent with the FIXED ones)

- **PG3-NEG** if a primary geometry (T22 or O22) gives a converged negative eigenvalue on an admissible pool
  (Sec. 3 margin), or if a proof of negativity for a primary geometry is completed (then labelled proved,
  with the numbers as check).
- **PG3-PSD** if every primary pool type (P1, P2, P4, P5; O22 grids and searches) is PSD within 10 E AND the
  power reference R1 finds a converged negative with the same code and budget (and R2 reproduces).
- **OPEN** otherwise (including: R1 fails; O22 quadrature not converged; builders disagree in sign; PSD on
  T22 but O22 undecided — then say which).
- O12 (secondary) and any extra geometry or delta (0.3, 0.45, 0.75; 4 delta < pi needed for the T22 formula)
  get their own NEG/PSD/OPEN label by the same criteria; they do not change the primary reading.
- Analytic: attempt a proof of positivity (e.g. a manifest sum-of-squares form) or negativity (explicit test
  function supported in S_delta) for T22/O22/O12, in particular whether the referee's c6 c3^6 < 0 coefficient
  survives restriction to S_delta.

**What it means for the price (registered interpretation):**
- PG3-NEG: P-X3d ("plaquette bound as a hard support constraint") is itself not RP on that 3D lattice, with no
  matter; set B would need a positive-type (soft) plaquette weight or a different reading of admissibility
  support, independent of the fermion failure found in K2c.
- PG3-PSD: the hard bound survives this cheap 3D test (scope: the slices tested, delta values tested); K2c's RP
  failure stays attributable to the overlap determinant, not to the bound.

---

## Follow-up notes (appended 2026-10-14T21:17Z; nothing above was edited)

F1 (after the first ring results, before V1-V4, the exact witnesses and the strip scan). Added checks, registered as
follow-ups, not changing any reading:
- V1: an explicit admissible point pool (R-line x X0-ring), all entries from the independent builder, full matrix.
- V2/V2b: exact rational witness for T22 (Fractions; exact LDL inertia; explicit vector; delta-scaling by homogeneity).
- V3: exact rational witness for O12 (Boole's rule exact on degree-4 pieces; exact LDL inertia).
- V4: independent-builder rebuild of the W0-matched octahedron grid pool.
- O22 is computed with smooth B-spline test functions (Sec. 4 allowed this), two Nystrom levels.
- F2: open 1xL strips, L = 2..5, smooth test functions; L = 2 cross-checked against the exact O12 kernel.
- Label correction: the run first saved as "P3_fullmatched_oct" (ring 1x1 on the octahedron grid) is NOT fully
  W-matched: it fixes X0 = Y0 only, while X1 = X0 - P and Y1 = Y0 + Q vary. It is a P2-type (W0-matched) grid pool and
  was renamed P2_w0matched_oct_grid_h0.15.out. The fully matched control (P3) is the line_R pool with ring 1x1.
- Memory incidents (to be reported): the first t22_ring.py run (unres grid, M = 2744, ring 32x32) was killed by the
  coordinator at 5.2 GB; afterwards a guard and an RSS watchdog (capped.sh) were added. Two later watchdog kills:
  plane pools at 458 MB (above the 0.4 GB cap for < 0.2 s; tensordot made complex copies; fixed) and o22_check at 317 MB
  (watchdog then lowered to 300 MB). No reading depends on a killed run.
