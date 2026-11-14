D4 frame doublet on a Lorentzian lattice: the tick frame part becomes heavy and healthy, the other part stays massless as a ghost on its own cone; a uniform metric-only reading excludes the fixed-spoke frame deformation, and in the Euclidean reading the raw metric block keeps the birefringence law

Claim type: bounded_theorem (exact identities; finite supplied-model numerics on the coned D4 cell).
Runner: [`scripts/d4_frame_doublet_lorentzian_regge_stability_and_metric_only_removal_2026_10_26.py`](../scripts/d4_frame_doublet_lorentzian_regge_stability_and_metric_only_removal_2026_10_26.py) (seeded; it exits nonzero on any failed check). Its cache
[`logs/runner-cache/d4_frame_doublet_lorentzian_regge_stability_and_metric_only_removal_2026_10_26.txt`](../logs/runner-cache/d4_frame_doublet_lorentzian_regge_stability_and_metric_only_removal_2026_10_26.txt) holds the current output (the source run: 10 checks, 5.6 s).
Pre-registration: criteria_pre_run.txt (written before any computation).
Builds on: d4-frame-modes (#10101; recorded only in the source map of [the consolidation](D4_ROUTE_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md)), d4-gravity
([#10100](D4_EVENT_SET_ROOT_SLICED_HINGE_SUM_GRAVITY_CARRY_OVER_BOUNDED_THEOREM_NOTE_2026-10-26.md): G4, R1-R5, M2), time-blind D4 events ([#10094](D4_TIME_BLIND_EVENTS_KILL_DIMENSION_SIX_LIV_FOR_SCALAR_FERMION_PHOTON_BUT_THE_SLICING_DECIDES_LOCALITY_AND_SIGN_BOUNDED_THEOREM_NOTE_2026-10-26.md)); the last two are in this PR.

VERDICT (pre-registered labels; narrowed 2026-11-14): not TACHYONIC. y0 is STABLE. y1 is MARGINAL, with
the GHOST flag raised (both in the Lorentzian reading R-b). A uniform metric-only reading excludes the fixed-spoke
frame deformation (M1, algebraic). In the Euclidean reading (R-a, g = I) the raw metric block keeps the
birefringence law (M2). Whether metric-only reading removes the Lorentzian ghosts, and what the birefringence is in
(R-b), was NOT computed.
The Euclidean strain tachyon of frame-modes B3 is a feature of reading (R-a) only. It does not occur
in the Lorentzian Regge reading (R-b). So the (2) endpoint branch is not triggered.

Two readings (both reported)
- (R-a) Euclidean W(F4) lattice, with real time obtained by continuing the momentum. This is the
  reading used by d4-gravity and frame-modes.
- (R-b) The lattice itself is Lorentzian.
  - Background: g_L = P_perp - lam t t^T, so the tick root has s = -2 lam.
  - Action: the Euclidean hinge sum continued along g_tt = lam e^{i phi}, phi from 0 to pi.
    Supplied: Sorkin / Barrett-type Lorentzian Regge.
  - Every squared volume on the path has the form A + e^{i phi} B with A, B >= 0, so the branch is
    sqrt(z + i0).
  - Second order uses Schlaefli, d2S = Sum dA d eps. No arccos branch is needed.
  - At lam = 1 ("all roots alike") the spokes and some triangles are NULL. The Lorentzian complex
    degenerates there, so lam = 1 is reached as a limit from both sides (0.99, 1.01, 0.9, 1.1) and
    also at 0.5.

Theorems / exact
- [T] The swap x2 <-> x3 fixes t and exchanges the two non-tick frames. The time slicing therefore
  splits the S3 doublet into
  - y0 = (2,-1,-1), the tick frame against the other two, which is even;
  - y1 = (0,1,-1), the two non-tick frames against each other, which is odd.
  So y1^3 is forbidden.
- [T] Metric-only exclusion of the frame deformation, nonlinear in u. The 24 spokes fix every
  component of a uniform metric (rank 10, no free directions), so the only uniform metric that fits
  fixed spokes is g = delta. A frame rescaling at amplitude u != 0 changes root lengths but no spoke,
  so no single uniform metric reads it: the residual distance is 1.0, 0.999 and 0.995 of the
  deformation at u = .01, .1, .3. Scope: one uniform metric per cell and the specified frame-rescaled
  lengths. It says nothing about spacetime-dependent metric readings, and it is not a computation of
  the Lorentzian spectrum after the doublet is removed.

Finite diagnostics (supplied model)
- Validation:
  - V1: the Schlaefli Hessian equals frame-modes' length Hessian to 2e-10.
  - V2: the continued Hessian is exactly i x (real symmetric) and Hermitian at real K (1e-9), with
    trig identities to 3e-15.
- L1, k = 0 zeros on the Lorentzian lattice: 23 = 12 gauge + 10 metric + y1.
  - y1 stays an EXACT zero for every lam tested (off-null share 1e-9).
  - y0 is lifted.
  - Euclidean W(F4) has 24 zeros.
- L2, real-time census (roots in z = e^{i omega/sqrt2}, real spatial k = .05, two directions, lam in
  [0.5, 1.1]). Exactly 12 finite roots, all on |z| = 1, so there are no growing modes:
  - graviton x2 on the light cone of g_L (c = sqrt lam), Krein sign +;
  - y1: massless on its OWN cone, c = 1/sqrt(lam) in coordinates (physical speed 1/lam), with
    Krein sign OPPOSITE to the graviton, i.e. a GHOST;
  - y0: heavy, omega = 2.18-2.25 lattice units (1.94 at lam = .5), Krein sign +, i.e. healthy;
  - a metric-dominated heavy pair at omega ~ 2.2 with ghost sign: a cell-scale ghost of the full
    hinge sum.
  - All of this is continuous through lam -> 1, where the y1 cone meets the light cone.
- L3 controls:
  - The far off-circle roots (|ln z| >= 11.7) are float zeros of the rank-6 end coefficients. They are
    one-sided and move under rescaling of z.
  - A genuine z, 1/z instability appears only for lam > 3, where the pair-offset roots become
    time-like (|ln z| = 1.18 at lam = 3.5).
- L4 contrast: the same lattice strain read as (R-a) gives y0 a real Euclidean pole at 0.187, i.e. a
  tachyon (B3). Read as (R-b) it gives a real frequency of 2.18.
- M2, birefringence, Euclidean reading (R-a) with g = I: the raw metric block (no gapped modes,
  no doublet), with the line-integrated reading, which is exactly gauge-covariant (2e-8). Its light
  roots give A = +-1/6 (axis), +-1/8 (face) and 0 (body), identical to the full model, which
  reproduces d4-gravity R5/R7. So in (R-a) the birefringence law is unchanged. A is a phase-speed
  coefficient (E/k = 1 + A (ka)^2; the group speed has 3A).
  - Correction (2026-11-14). The source verdict and title said the metric-only reading removes the
    pair "with the birefringence unchanged", without naming the reading. This note's own open list
    says the raw metric block in (R-b) and the fate of the cell-scale ghost pair under metric-only
    reading in (R-b) were not run. Both stay OPEN; the runner prints them as NOT CHECKED.
- M3 control: the midpoint reading is not gauge-exact (7e-6). It keeps a nonzero splitting
  (half-split 0.29) but adds a polarisation-averaged shift of +0.086. So the O(k^2) coefficient is
  reading-dependent. By the pre-registered "both readings" clause this is PARTIAL, and the
  gauge-exact reading is the one to use.

Against measurement (estimates)
- y1 cone vs light cone: the speed offset is |1/lam - 1|. y1 couples to matter only at dimension 6
  (per-edge reading; frame-modes E1), so direct bounds are weak. The graviton itself sits on the
  g_L cone for every lam.
- A massless ghost with any graviton coupling (an h h y1 vertex is allowed by symmetry; its
  coefficient was NOT computed) makes the vacuum decay at a cutoff-limited rate. With a Planck-scale
  cutoff this is unacceptable (speculation: Cline-Jeon-Moore-type bounds).
- So keeping per-edge registers is now disfavoured on HEALTH grounds, not just as a risk.

Not done / open
- The quartic of y1 and the relaxed nonlinear potential in (R-b).
- The h h y1 vertex.
- The raw metric block in (R-b) (birefringence was checked in (R-a), the method of d4-gravity).
- lam = 1 exactly (degenerate null complex).
- Whether the cell-scale metric ghost pair disappears under metric-only reading in (R-b) (expected,
  since the 12 gapped modes are removed; not run).
- beta = 1 nonlinear: still ARGUED, as in frame-modes.
- The (2) endpoint and its dim-6 value: not triggered, because there is no tachyon in (R-b).

Proposed CL amendment (working, not adopted; same text as frame-modes D1)
"Edge registers enter the hinge sum and the matter odds only through the metric their records read
(order and count); the hinge sum is taken on metric-read (line-integrated) lengths of the coned D4
cells."
- Upgrade (narrowed 2026-11-14): in (R-b) the per-edge reading has a massless ghost (y1) and a
  cell-scale ghost pair, and a uniform metric-only reading excludes the frame deformation that
  carries y1. In (R-a) the raw metric block keeps linear GR and the birefringence law (1/3 (ka)^2
  phase splitting, same angular law). That the amendment removes the cell-scale ghost pair, and its
  (R-b) spectrum, are not computed.

Smuggling gate
- No measured number chosen.
- No observed structure named.
- Supplied: the coning; Lorentzian Regge via continuation (Sorkin / Barrett); the lam family and the
  lam -> 1 limit; the line-integrated metric reading.
- Prediction not built for: y1's cone and its ghost sign under per-edge reading. Under the
  amendment, the birefringence carry-over is TESTED in the Euclidean reading (R-a) only: it survives
  there. In (R-b) it is not tested.
- Bent clause: d4-gravity's "every edge responding" (CL-3 response variables). Axioms unchanged.
- Gate: PASS.
