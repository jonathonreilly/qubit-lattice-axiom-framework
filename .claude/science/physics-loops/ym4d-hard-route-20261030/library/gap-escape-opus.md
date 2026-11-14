lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T06:46Z

# Row 976 `gap-escape-opus`: escape test 1(e) of row 975 (GUIDE refutation test)

Pinned commit 5793df82e, branch claude/ym4d-hard-route. Started 2026-11-14 18:46Z (from `date -u`).
A run guides or refutes at GUIDE level; it proves nothing.

## Status log

- 2026-11-14 18:46Z: file created with plan (save protocol).
- 2026-11-14 18:49Z: steps 1-3 written (criteria fixed before any run); script `guide/lane976/esc976.py` written, not yet run. Numeric lock held by gap-tiesearch-973 (row 973, its tielab.py runs are live; lease to 22:53Z); memory 69 percent free. Waiting for the lock; no run of this row has started.

## Plan (at most eight steps; one per response)

1. Read row 975 Approach 1 (Lemma META, Corollary ESC-nec, test 1(e)) and row 974 summary; record the exact
   statement being tested.
2. Read rows 950/952 and `library/guide/lane952/` code: what the layered pi-flux slice u_xy is, how it is built,
   which observables (colour order of the electric field, xy-plaquette action) already exist.
3. Write the pre-set criteria (set A, thresholds, refute / transient verdicts, control, sample sizes, error bars)
   in this file BEFORE any run.
4. Write the half-infinite slab script in `library/guide/lane976/` (bottom slice frozen at u_xy, top open with a
   buffer), smoke test, time it; vacuum control smoke test.
5. Production runs, beta 2.3 and 2.4 (>= 32 slices + buffer), sides 8 to 12, under the numeric lock.
6. Production runs, beta 2.6 (>= 48 slices + buffer), plus vacuum control.
7. Analysis against the pre-set criteria, with sample sizes and error bars.
8. Verdict and RESULT line.

## Step 1 (done). What is tested (READ; pointers, no new claim)

Source: row 975, `library/gap-ymcons-opus.md` Approach 1, lines 127-174, and 8.2 item 1 (lines 503-508). Lemma META (PROVED
there, not re-checked here): for a gauge-invariant set A of slice configurations with pi(A) = p in (0,1) and
r_A(a) = P_(pi(.|A))(x_a in A), S(a;B) >= (r_A(a) - p)/(1 - p). Corollary ESC-nec: S(a;B) < 3/10 forces r_A(a) < 3/10 + 7p/10
for every A. Test 1(e) is the GUIDE probe of (ESC)_a at the named bad set "neighbourhood of the gauge orbit of the layered
pi-flux slice u_xy". The row (FINISH row 976) moves the betas to 2.3 and 2.4 (at least 32 slices plus buffer, a = 30)
and 2.6 (at least 48 slices, a = 45, from row 974: at beta 2.6 the box needs a >= 45). I follow the row, not 1(e)'s 2.5/2.6.

Two reading points I record before running (ARGUED here):
- (R1) Lemma META starts the chain from pi(.|A), the stationary law conditioned on A. The slab with a FROZEN bottom
  slice starts from one point of A, x_0 = u_xy. These agree only if A is small around the orbit of u_xy. The run
  measures the point start, as 1(e) asks; r from the point start is a guide to r_A, not r_A itself.
- (R2) The law of slice k in a slab with frozen bottom x_0 = u and slices 1..T (top slice at half spatial weight, free)
  is P^k(u, .) of the transfer-matrix chain up to the top-boundary effect, which the buffer (slices a+1..T) is there
  to remove. Each "run" below is one equilibrium configuration of that slab.

## Step 2 (done). The code and the observables of rows 950, 952 (READ)

`library/guide/lane952/sg2lab.py` (row 952, Claude Opus 5.5): SU(2) Wilson slab in temporal gauge, links unit
quaternions, slices t = 0..T, slice 0 frozen at the datum u, spatial plaquettes at weight beta (slice T at beta/2),
temporal plaquettes <U_l(t), U_l(t+1)> at weight beta, spatial torus L^3, checkerboard Kennedy-Pendleton heat bath.
The layered pi-flux slice u_xy = `make_slice_su2("xy")`: u_x = 1, u_y(x) = (-1)^x, u_z = 1, so every xy plaquette is -1
(the centre element) and every xz, yz plaquette is +1. First-step field E_l = Im(U_l(1) u_l^*) (3 colour components).
The colour order of rows 950/952 is the tie mode eps_l = (-1)^(x+y) on x-links, -(-1)^(x+y) on y-links, 0 on z-links
(Fourier (pi,pi,0), polarization (1,-1,0)); row 950 measured lambda = top eigenvalue of the covariance of that mode:
at beta 2.3 it saturates (2.5, no order), at 2.4 about 8 (saturated), at 2.5-2.6 it grows like L^3 (colour order of the
boundary layer; `gap-sc-max.md` 5.7, lines 405-430). I reuse `qmul`, `qc`, `sh`, `heatbath_su2`, `make_slice_su2`,
`plaquettes`, `eps_pattern` and `SlabSU2` from that file unchanged (credit row 952), and add only the measurement.

## Step 3 (done). Pre-set criteria (written 2026-11-14 18:49Z per date -u, BEFORE any run of this row; nothing of this row has run)

### 3.1 Observables (per equilibrium configuration of the slab, at each step k)
- xy action density s_k = mean over the L^3 xy plaquettes of slice k of (1 - Re P), Re P = real part of the quaternion
  plaquette = tr P / 2. Frozen value at u_xy: s_0 = 2 exactly. Gauge invariant (a function of slice k alone).
- Colour order O_k = | sum_l eps_l E^(k)_l | / (2 L^3), the length of a colour 3-vector, with E^(k)_l = Im(U_l(k) U_l(k-1)^*)
  the electric field on step k (k = 1 is the first-step field of rows 950/952), eps the tie mode of row 950 (x, y links).
  O = sin(theta) for a field fully ordered along the tie mode with angle theta. Temporal gauge is referenced to the frozen
  slice, whose stabilizer is the global SU(2) (u_xy fixes the gauge up to a constant), so O_k is well defined; but it reads
  the order in the frame transported straight down to slice 0 (caveat (C1) below).
- Secondary, reported but not used in the verdict: D_k = the same with Im(U_l(k) u_l^*) (distance of slice k from u_xy in
  the tie mode); the xz and yz action densities of slice k.
- Step-1 value O_1bar = ensemble mean of O_1 at the same (beta, L, start).

### 3.2 The set A and the fractions
- Slice k is "in A" iff s_k >= 1.8 (within 10 percent of s_0 = 2) AND O_k > O_1bar / 2 (row 975 1(e), verbatim).
- Also reported: A' = {s_k >= 1.8} alone. A' is a gauge-invariant set of slice configurations, so Lemma META applies to it
  directly; A is not purely a slice set (O_k uses slice k-1 and the transport to slice 0), A' is. Since A is a subset of
  A', "out of A'" implies "out of A".
- f_k = fraction of measured configurations with slice k in A (and f'_k for A'), at k = 1, 2, 3, 4, 8, 16, 30 (and 45 at
  beta 2.6). k = 3 is added because the transience criterion is stated at k = 3.
- Error bar: the measurements of one seed are blocked; the standard error is over seeds (s.e. of the per-seed fractions,
  ddof 1), and when every seed gives 0 or 1 I report the binomial bound: with N configurations and none in A, the
  95 percent upper bound is 3/N_eff with N_eff = number of seeds x blocks (conservative: blocks treated as the
  independent units).

### 3.3 Verdicts (per beta, at L = 8 and L = 12, and only when the start control passes)
- REFUTE (GUIDE): f_a >= 0.30 at k = a (a = 30 at beta 2.3 and 2.4, a = 45 at beta 2.6) at the largest L run, with the point
  estimate minus 2 s.e. >= 0.20. Reading: by Lemma META (p negligible) the seed on (a; (4a)^3) fails at GUIDE level at that beta.
- TRANSIENT (GUIDE): 1 - f_3 >= 0.95 (at least 95 percent out of A by k = 3) at every L run. Reading: the u_xy ties of
  row 970 are transient for the trace, as row 975 8.2 Outcome B says.
- Otherwise INTERMEDIATE: report f_k at all k and the decay of s_k.
- The same three verdicts are stated for A'.

### 3.4 Controls (each must pass, else the verdict at that beta is "no verdict")
- (C-start) Monte Carlo start: cold (all slices = u_xy) and hot (slices 1..T Haar random) must give f_3 and f_a within
  0.1 of each other, and the profile s_k within 0.05 at every k >= 4. A cold-only retention would be Monte Carlo
  metastability of the heat bath, not of the transfer chain.
- (C-vac) Vacuum start: bottom slice frozen at a vacuum slice of the same beta and L (generated as in row 952 `--genvac`,
  middle slice of a free slab). Same observables. Pass: s_k at k >= 8 agrees with the u_xy start within 0.05, and both
  agree with the bulk plaquette 1 - <P>: <P> is about 0.60 at beta 2.3, 0.63 at 2.4, 0.67 at 2.6 (RECALLED, rough, 4D
  SU(2) Wilson, infinite volume; only used as a sanity scale, tolerance 0.03).
- (C-buffer) Top-boundary effect: s_k at k = a must not change by more than 0.03 between T = a + 8 and T = a + 16 at L = 8
  (one run per beta, if time allows; else stated as not done).

### 3.5 Sizes (fixed before the run; changed only if the timing smoke test makes them impossible, and then stated)
- beta 2.3 and 2.4: T = 40 (k <= 30 measured, buffer 10); beta 2.6: T = 56 (k <= 45, buffer 11). L = 8 and 12.
- Each (beta, L, start): 4 seeds, 300 thermalization sweeps, then 40 measurements every 5 sweeps (160 configurations,
  4 x 4 blocks of 10). The vacuum control: 2 seeds at L = 8 per beta.

### 3.6 Caveats fixed in advance
- (C1) O_k at large k reads the colour frame transported along the temporal line to slice 0; in a confining slab that
  frame decorrelates, so O_k can fall even if slice k keeps a local u_xy-like order in its own frame. This biases A
  toward "transient". A' does not have this bias; the verdict for A' is the cleaner one.
- (C2) Point start, not pi(.|A) (R1 above). (C3) L = 8, 12 is far below the (4a)^3 = 120^3 of the seed box; escape from a
  dense centre-flux slice is local, so I expect (ARGUED, not shown) little L dependence; the run checks L = 8 against 12.
- Prediction written before the run (ARGUED, to be scored): every xy plaquette of u_xy is a thin centre vortex costing
  2 beta per plaquette per slice, while undoing it over k steps costs about beta pi^2/(2k) per link in temporal plaquettes,
  so the classical relaxation takes O(1) slices; I predict TRANSIENT at all three betas for A', with s_1 already
  well below 1.8.

## Step 3b (done, by hand, written 18:51Z while the lock is held by row 973; still before any run of this row)

One-mode classical escape path (ARGUED; arithmetic checked by a 3-line numpy grid, not a lattice run). Keep u_x = u_z = 1
and put on y-links u_y(x even) = exp(alpha_t n.sigma i), u_y(x odd) = -exp(-alpha_t n.sigma i) on slice t (quaternion
notation: exp(alpha k) for n = e_3), alpha_0 = 0 (this is u_xy). Then every xy plaquette of slice t is
P = u_y(x+1) u_y(x)^* = -exp(-2 alpha_t k), so Re P = -cos(2 alpha_t), and xz, yz plaquettes stay 1. At alpha = pi/2 the slice
is flat (u_y = k everywhere; y-holonomy k^L = (-1)^(L/2), trivial for L = 8, 12; for L = 2 mod 4 the sign can be fixed by
flipping alpha on one y-row, so there is no sector obstruction). This path is exactly the colour-3 tie mode of row 950 on
the y-links: the boundary-layer "colour order" IS the first step of escape, its colour direction n being the free choice.
Action per site, in units of beta: spatial 1 + cos(2 alpha_t), temporal 1 - cos(alpha_(t+1) - alpha_t).
- Slice 1 alone: minimize (1 - cos alpha) + (1 + cos 2 alpha): sin alpha (1 - 4 cos alpha) = 0, cos alpha_1 = 1/4, alpha_1 = 1.318,
  total 0.875 against 2 for staying (alpha_1 = 0); the xy action of slice 1 is s_1 = 1 + cos(2 alpha_1) = 0.125.
- Slices 1, 2 (grid): alpha_1 = 1.361, alpha_2 = 1.529, xy actions 0.086, 0.004; total 0.896 against 4 for staying.
- Continuum-in-time version: alpha' = 2 cos alpha, sin alpha(t) = tanh(2t): relaxation length 1/2 slice.
So classically u_xy is a hilltop of the slice potential and is left in ONE step, at a cost of about beta x 0.9 per site
against beta x 2 per site per slice for staying. Thermal fluctuation at beta 2.3-2.6 adds about the vacuum action
(s near 0.4) but cannot plausibly hold s_k >= 1.8. Quantified prediction (to be scored): s_1 < 1.0 at all three betas,
f'_1 = f_1 = 0 within errors, verdict TRANSIENT for A and A'; the colour order O_k decays over a few steps.
What this means for the test (ARGUED): the plaquette clause of A in 1(e) makes A a set the chain leaves in one step,
so the run can only confirm transience of the high-action slice; it cannot see a metastable set that a relaxed slice
might sit in (for example a fixed colour direction n of the relaxed state, or a spatial centre-holonomy sector on a
small torus at large beta). Those would need a different A; I do not add one to the verdicts (criteria are fixed), but
I record O_k and D_k at all k so that a later row can read the colour-direction memory.
