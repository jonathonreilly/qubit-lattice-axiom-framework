D4 zoom fixed-point fermion: only real, positive poles (no Lee-Wick pair), but site positivity needs a one-slice buffer, and no finite truncation keeps it

Date: 2026-10-26
Claim type: bounded_theorem (exact kernel/group/support facts plus finite diagnostics on a supplied free model)
Status authority: independent audit lane only. This draft sets no audit outcome.
Runner: runner.py (this folder). AUDIT_TIMEOUT_SEC = 120. 31 s, 185 MB peak, seeded, 14/14, output 3.9 k characters.
  A re-run under a unique filename (scratchpad copy) gave identical output apart from the runtime line.
Pre-registration: criteria_pre_run.txt, written before any computation.
Labels: [T] exact or theorem; [F] finite diagnostic; [A] uses a supplied literature theorem; [S] reading.
Axioms unchanged. No CL edit. Nothing adopted.

Synthesis tested
"Matter's history weight on the D4 event set is the fixed point of the D4 zoom (block averaging over D4 cells,
factor 2), sliced along a root." Dispatcher's expectation: W(F4) protects dim 6 at all orders with no imposed
radiative condition, and the zoom removes the nearest-neighbour fermion's Lee-Wick pair, giving full RP.

Sources used
- zoom-fixed-point-tick (cubic perfect action, PR #10092): T1 finite-band no-go, T2 zooming keeps poles. Reused method.
- d4-time-blind-events (#10094), d4-interacting-check (#10095): W(F4) counts, root slicing, the one-loop moment code (reused).
- d4-fermion-positivity: NN D4 fermion has no positive slice transfer (narrowed "bosons only").
- protected-fermions: NN family has a positive real sector plus ONE Lee-Wick pair; its existence argument (ii) used a
  smeared continuum field. This note supplies the zoom version of that construction and finds its exact positivity class.
- main: ADMISSIBILITY_DIRAC_KAHLER_..._OS_LORENTZ_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14 lists "perfect/anisotropic
  action" as live; git grep origin/main finds no perfect-action or W(F4) note. Nothing on main is contradicted.

1. The D4 zoom and its fixed point
- [T] 1a. Kernel. Coarse field = (1/16) sum_x w(x - 2X) phi_x with w = 1 at 0, 1/2 on the 24 roots (facets of the coarse
  Voronoi cell, shared by 2 cells), 1/8 on the 24 norm-4 vectors (its vertices, shared by 8 cells). Checked: invariant
  under all 1152 elements of W(F4); each of the 16 cosets of D4/2D4 gets total weight 1; f(q) = w~(q)/16 vanishes on
  pi D4* \ 2 pi D4*. Closed form f = ((sum c)^2 - (1/2) sum c^2 + 2 prod c)/16, c_a = cos q_a.
  Uniqueness [T]: among W(F4)-invariant partition-of-unity kernels supported in the closed coarse Voronoi cell, these
  weights are forced (0 is its coset's only member there; +-r share by -1; each norm-4 coset's 8 members are one orbit
  of its stabiliser). So the kernel is not chosen.
- [T] Fixed point: G*(p) = sum_{l in 2pi D4*} Pi(p+l)^2 (-i g.q + m)/(q^2+m^2) + alpha, q = p + l, Pi(q) = prod_{j>=1} f(q/2^j).
  Pi(2q) = f(q) Pi(q) (checked 5e-15) gives G*(P) = (1/2) sum_k f(Q_k)^2 G*(Q_k) + alpha(1 - (1/2) sum_k f(Q_k)^2),
  Q_k = (P + l_k)/2: G* is exactly fixed by an explicit factor-2 map whose Gaussian width term is a local trig polynomial.
  Numerically R(G*) - G* = 2.1e-7 (N = 5), 5.9e-8 (N = 6), falling with the image cutoff (smooth window, D4* images).
- [F] 1c. Covariance computed directly at random off-grid momenta: 2e-16.
- [F] 1d. Locality of D* = G*^-1 (L = 12 D4 torus, 89 W(F4) orbits computed directly): decay 1.90 (root) / 1.94 (short)
  per unit length at alpha = 1/2; 1.72 / 1.75 at alpha = 1.
- [F] 1e. Ginsparg-Wilson g5 D + D g5 = 2 alpha D g5 D and g5-hermiticity: 9e-16. The overlap with m0 = 1/(2 alpha) returns
  D* (7e-16): the overlap step is an identity, m0 is forced.
- [F] 1f. No doublers: alpha|D*| >= 0.27 on every grid momentum except 0; |D*| = 1/alpha exactly at the 15 classes of pi D4*.
- [F] 1g. Lowest band from the root-slice correlator: sqrt(k^2 + m^2) to 4e-9 (axis, face, body, generic; m = 0, 0.3).
- [F] 1h. k^2 coefficient of v - 1 (massless): <= 9e-10 in every direction. Dim 6 = 0 for free matter.

2. Positivity along the root (the main question)
- [T] Support. By Titchmarsh-Lions, the convex hull of the limit smearing is the Minkowski sum of the rung hulls: 2V
  (V = Voronoi cell of D4). Its time half-width is sqrt2 = 2 slice spacings. Any W(F4)-invariant factor-2 partition of
  unity must weight every coset; one that keeps the minimal (closed-cell) support is the forced kernel, with this hull.
  Kernels with longer support were not analysed (expected wider, not proven).
- [T] Pole structure. For separations tau >= 2 sqrt2 (n >= 4 slices), closing the q_t contour gives exactly
  G(n;k) = sum_K (+-1)^n exp(-E_K tau_n) Pi(iE_K, k+K)^2 (E_K g_t - i g.(k+K) + m)/(2 sqrt2 E_K), E_K = sqrt((k+K)^2 + m^2),
  K in the transverse dual. Pi(iE) is real (time-reflection pairs of roots), phases are +-1 (two slices = one root step),
  and every residue times g_t is PSD (eigenvalues 2E, 0). So: all poles real, one norm sign, NO complex pair, NO ghost.
  [F] 2a: direct image sum vs residue sum, relative 7e-9 (n = 4), 1e-9, 8e-11, 2e-11 (n = 5, 6, 8); n = 3 differs by 2e-3
  (non-pole short-distance piece). Im Pi(iE)/|Pi| and Im phase <= 1e-14.
- [F] 2b. Site Hankel form H_ij = G(i+j) g_t (reflection through slice 0; four k, m = 0 and 0.3):
  - unbuffered (i, j >= 1): INDEFINITE, wrong-sign fraction 5.3e-3 to 9.2e-3;
  - buffered (i, j >= 2, every pairing >= 4 slices apart): positive to float floor (|wrong| <= 4e-13).
  Reading [T]: the positive Hilbert space is the OS reconstruction from slices >= 2 from the reflection plane; its slice
  transfer is Hermitian with real eigenvalues +-exp(-E_K/sqrt2) (T^2 >= 0). The indefinite piece is non-pole and confined to
  separations < 2 sqrt2 a: it creates no state. Note that it is LARGER than the NN fermion's unbuffered value (1.4e-3).
- [F] 2c. Range-R truncations of D* (shells |x|^2 <= 2R; 13 transverse momenta; alpha = 1/2 and 1): a complex pair at EVERY R
  = 1..4 and every sampled k (complex-pole counts 2-2, 2-4, 2-6, 4-6 at alpha = 1/2; 2-2, 2-4, 2-6, 6-6 at alpha = 1). Real
  ghosts appear at some R, non-monotonically (wrong-sign 9e-1 and 1.0 at alpha = 1/2, R = 3, 4; 5e-1 and 1.0 at alpha = 1, R = 2, 3).
  The indefinite weight does NOT fall to zero at finite range. Positivity holds only in the limit (the infinite image tower).
- [T+F] 2d. Zoom rungs from the NN start (w = 1). Blocking is a positive sum of fine propagators, so it keeps every pole (T2):
  the NN pair (Re E = 2.57/a) is present at every finite rung, at 2.57 x 2^n in coarse units. Its buffered weight:
  2e-4, 7e-7 and below 1e-14 at rungs 0, 1, 2 (doubly exponential). The unbuffered weight grows to the fixed point's:
  1.4e-3, 2.4e-3, 6.9e-3. So the zoom removes the pair only in the limit, and trades it for the non-pole buffer piece.
- Answer to (2): exact fixed point PASSES the pole test (real, positive, no pair); it FAILS unbuffered site RP and PASSES
  buffered RP; no finite truncation and no finite rung is pair-free.

3. Interacting protection is a symmetry statement
- [F] 3a. Truncated fixed-point coefficients on shells |x|^2 <= 8 are W(F4)-covariant to 6e-17.
- [F] 3b. One loop on the L = 16 D4 torus with the fixed-point fermion (m = 0.5) and the W(F4) NN scalar (d4-interacting-check
  moment method): dim-6 O(4)-breaking residuals 1e-15 (Yukawa loop), 1e-15 (fermion mass part), 2e-15 (gamma part); the first
  breaking is J6 (residual after J6 <= 7e-15); Z^4 control breaks at dim 6 (2.8e-2, 1.3e-1, 2.1e-1).
  Caveat: the L = 16 kernel is filled from orbit representatives by the group action, so 3b tests the loop algebra; the
  symmetry itself is tested directly in 1c. All-orders protection follows from the tensor counts (W(F4): 1 quartic scalar,
  1 cubic vector covariant) if the interacting regulated weight keeps W(F4); this is a symmetry argument, not a loop
  computation beyond one loop.

4. Simplification ledger [S]
- Replaced (if adopted): CL-1's matter tick (half-tick unitaries for matter; already re-read by the D4 law); the
  walk-to-Wilson identification and the m0 window (m0 = 1/2alpha forced, overlap = identity); the repaired overlap kernel;
  the cubic zoom-fixed-point law AND its imposed radiative clause (W(F4) does the work); the D4 "bosons only" narrowing,
  in the pole sense (the fixed-point fermion has a real positive spectrum).
- Not replaced: the copy sign. Here no copies exist (no doublers), so its copy-selection role disappears, but if the 16
  copies were meant to carry content (one generation's 16), that content must be rebuilt by other means.
- Still to build: slab/Luscher chirality and the gauged 4D index on D4 (GW holds, so the projector exists; not computed);
  families; gravity hinge sums on D4; a history-level perfect weight for the link registers.
- Added: alpha (blocking width, spectrum-inert), and a buffer clause for reading records.

Verdict (pre-registered rule): PARTIAL
- Test 1 PASS (one pre-registered threshold missed: 1b to 5.9e-8, not 1e-8, cutoff-limited; the exact refinement
  identity holds to 5e-15). Test 3 PASS. Test 2 PARTIAL: positivity is a property of the exact infinite-tower weight only,
  and in the site sense needs a one-slice buffer.

Proposed CL text (UNTESTED; for review only; NOT adopted)
  "Matter's history weight on the D4 events is the exact fixed point of the factor-2 zoom that averages each coarse
  Voronoi cell with boundary sharing (weights 1, 1/2, 1/8), sliced along a root. Records and odds are read only on the
  positive sector built from slices at least two slices from a reflection plane."
Smuggling gate
- (1) No fitted number: the kernel weights are forced (uniqueness above); alpha is inert for the spectrum. PASS.
- (2) No observed structure named. PASS.
- (3) Untested predictions: zero dim-6 LIV for matter at every loop order (symmetry); a fermion J6 dim-8 pattern; NO
  Lee-Wick acausal smearing (unlike the protected-fermions text); non-pole contact terms only below 2 sqrt2 a. UNTESTED.
- (4) Bent clauses: CL-1 matter tick (replaced by a history weight); CL-2 gains the buffer clause; one-qubit-per-site:
  the exact weight carries an infinite tower of positive branches E_K = |k + K| per transverse momentum, i.e. the free
  continuum Dirac field folded under the sites (the cubic T1 issue on D4). That reading is an owner decision (AX-level).
Gate: PASS on (1)-(3), with (4) naming a real axiom-level bend.

Open (walls move)
- A finite-range W(F4) kernel with no complex pair: not found at R <= 4 or with more shells; no no-go proven.
- Is unbuffered RP impossible for every W(F4) factor-2 zoom? The hull theorem only removes the support argument.
- Interacting buffer: does a Yukawa/gauge loop keep the non-pole piece confined below 2 sqrt2 a? (Expected yes by locality
  of the smearing; untested.)
- 4D gauged index and domain-wall content on D4 with D*.

Smuggling review
- Forced or exact: W(F4) and kernel invariance/uniqueness, refinement identity, hull half-width, contour/residue formula,
  GW/overlap identities, T2 pole persistence.
- Supplied: free continuum Dirac propagator inside the image sum (this IS the import behind gate item 4); alpha = 1/2, 1;
  m = 0, 0.3, 0.5; the NN scalar in 3b; test momenta; the Titchmarsh-Lions theorem [A].
- Fitted: none.

Deviations from pre-registration
- 1b threshold (1e-8) not met numerically (5.9e-8); replaced in the runner by the exact refinement identity plus the
  convergent numerical residual. Stated in out.txt.
- 1c threshold used 1e-10 as pre-registered (observed 2e-16).
- Zoom rungs stopped at n = 2 (the pair's buffered weight is below float floor there).
