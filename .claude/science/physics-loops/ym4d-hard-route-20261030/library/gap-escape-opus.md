lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T06:46Z

# Row 976 `gap-escape-opus`: escape test 1(e) of row 975 (GUIDE refutation test)

Pinned commit 5793df82e, branch claude/ym4d-hard-route. Started 2026-11-14 18:46Z (from `date -u`).
A run guides or refutes at GUIDE level; it proves nothing.

## Status log

- 2026-11-14 18:46Z: file created with plan (save protocol).
- 2026-11-14 18:49Z: steps 1-3 written (criteria fixed before any run); script `guide/lane976/esc976.py` written, not yet run. Numeric lock held by gap-tiesearch-973 (row 973, its tielab.py runs are live; lease to 22:53Z); memory 69 percent free. Waiting for the lock; no run of this row has started.
- 2026-11-14 20:49Z: a 2-hour background wait on the lock was stopped at its time limit; row 973 re-acquired the lock at 19:35Z (lease to 01:35Z, tielab.py runs live); memory 46 percent free (below the 50 percent rule). Still no run of this row; waiting again (at most 2 h).
- 2026-11-14 22:45Z: second wait ended, lock still held by gap-tiesearch-973 (lease to 01:35Z, tielab.py live); memory 49 percent free. No run of this row yet; a third wait started.
- 2026-11-14 23:30Z: lock free at 23:27Z; acquired as holder gap-escape-976 (status shows holder_id gap-escape-976). Memory 43-46 percent free (top users: an iOS Simulator runtime, not mine), below the 50 percent rule, so no run started; polling memory for at most 60 min.
- 2026-11-14 23:31Z: memory 60-62 percent free at 23:30Z; lock refreshed (holder gap-escape-976, to 03:31Z). Smoke test (L 8, T 40, beta 2.3, 28 sweeps, 4.5 s; log `guide/lane976/logs/smoke_b2.3_L8.npz`): 0.16 s per sweep; s_1 = 0.47. Production batch `guide/lane976/run976.sh` started 23:31Z with the sizes of 3.5 unchanged (48 runs + vacuum and buffer controls; estimate about 3 h, wall clock limit of the background job 2 h, so it may need a restart for the tail).
- 2026-11-15 00:14Z: batch done 00:13:31Z (60 runs, no errors), lock released 00:13Z; Steps 5-8 and RESULT written. Item finished.

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

## Step 4 (done). Script, smoke test, timing

`guide/lane976/esc976.py` loads row 952's `sg2lab.py` unchanged by exec and adds `measure` (s_k for the three planes,
O_k, D_k at every slice). `guide/lane976/run976.sh` is the production batch (sizes of 3.5 unchanged). `guide/lane976/ana976.py`
applies Section 3 to `guide/lane976/logs/*.npz` and writes `logs/ana976.json`; it also prints smax = the largest xy action
of slice k over all configurations (added after the criteria; reported, not used in a verdict). Timing: a full run (500
sweeps) at L 8, T 40 takes about 15 s (0.03 s per sweep; the smoke test's 4.5 s for 28 sweeps was mostly start-up).
First two runs (beta 2.3, L 8, cold, 80 configurations): s_1 = 0.463, s_2 = 0.402, s_k = 0.40 for k >= 2, largest s_1 seen
0.496; f_k = f'_k = 0 at every k. Bulk 1 - <P> = 0.40 matches the recalled <P> = 0.60 at beta 2.3.

## Steps 5-6 (done). Production runs (23:31:21Z-00:13:31Z under the numeric lock held by gap-escape-976, memory 60-62 percent free at start; lock released 00:13Z)

60 runs, no error in `guide/lane976/logs/batch976.log`. Sizes exactly as fixed in 3.5: beta 2.3, 2.4 at T = 40; beta 2.6 at
T = 56; L = 8 and 12; cold and hot starts; 4 seeds x 40 configurations (every 5 sweeps after 300) = 160 configurations per
cell, 12 cells, 1,920 u_xy configurations in all. Vacuum control: 2 seeds x 40 at L = 8 per beta (vacuum slice = middle
slice of a free hot-start slab, T 16, 300 sweeps). Buffer control: 1 seed x 40 at L = 8, T = 46 (beta 2.3, 2.4) and 61 (2.6).
Raw arrays: `guide/lane976/logs/*.npz`; analysis `guide/lane976/logs/ana976.txt` and `ana976.json` (from `ana976.py`).

## Step 7 (done). Results against the pre-set criteria

### 7.1 xy action s_k (mean +- s.e. over 4 seeds; cold start; hot start agrees, see 7.3) and the largest single value

| beta | L | s_0 | s_1 | s_2 | s_3 | s_8 | s_30 | s_45 | largest s_1 of 160 | f_k, f'_k at every k |
|---|---|---|---|---|---|---|---|---|---|---|
| 2.3 | 8 | 2 | 0.4650(15) | 0.4047(19) | 0.3990(6) | 0.3983(9) | 0.3965(21) | | 0.507 | 0 |
| 2.3 | 12 | 2 | 0.4653(5) | 0.4042(8) | 0.3969(9) | 0.3991(5) | 0.3991(7) | | 0.496 | 0 |
| 2.4 | 8 | 2 | 0.4364(13) | 0.3786(11) | 0.3722(8) | 0.3701(12) | 0.3710(6) | | 0.487 | 0 |
| 2.4 | 12 | 2 | 0.4376(7) | 0.3759(5) | 0.3715(9) | 0.3706(3) | 0.3692(4) | | 0.461 | 0 |
| 2.6 | 8 | 2 | 0.3874(26) | 0.3322(12) | 0.3300(11) | 0.3297(3) | 0.3310(10) | 0.3281(13) | 0.420 | 0 |
| 2.6 | 12 | 2 | 0.3905(13) | 0.3329(6) | 0.3316(9) | 0.3297(4) | 0.3293(3) | 0.3290(7) | 0.409 | 0 |

Not one of the 1,920 u_xy configurations has s_k >= 1.8 at any measured k >= 1: the largest xy action of slice 1 seen
anywhere is 0.507, against the threshold 1.8 and the frozen 2. So f_k = f'_k = 0 at k = 1, 2, 3, 4, 8, 16, 30 (45).
Error bars as fixed in 3.2: the conservative 95 percent bound with blocks as units is f <= 3/16 = 0.19 per cell; with
configurations 5 sweeps apart treated as units it is 3/160 = 0.019 per cell and 3/1920 = 0.0016 pooled. The margin
(0.51 against 1.8; the threshold lies 75 per-configuration standard deviations above the mean s_1 at beta 2.3, L 8
(spread 0.018), and 165 at beta 2.6, L 12 (spread 0.0085); computed from the npz files)
makes the bound academic. Slice 1 keeps about 0.06 more xy action than the bulk; by k = 2 it is within 0.005 of the bulk.

### 7.2 Colour order O_k and the frame memory D_k (secondary)

| beta | L | O_1bar cold / hot | O_2 | O_3 | O_k, k >= 4 (noise floor) | D_1 | D_3 | D_8 | D_16 |
|---|---|---|---|---|---|---|---|---|---|
| 2.3 | 8 | 0.091 / 0.092 | 0.022 | 0.021 | 0.019-0.020 | 0.091 | 0.048 | 0.024 | 0.025 |
| 2.3 | 12 | 0.041 / 0.033 | 0.012 | 0.011 | 0.010-0.011 | 0.041 | 0.025 | 0.013 | 0.014 |
| 2.4 | 8 | 0.126 / 0.130 | 0.024 | 0.020 | 0.020 | 0.126 | 0.074 | 0.028 | 0.024 |
| 2.4 | 12 | 0.060 / 0.059 | 0.013 | 0.011 | 0.011 | 0.060 | 0.036 | 0.014 | 0.013 |
| 2.6 | 8 | 0.230 / 0.233 | 0.030 | 0.019 | 0.019 | 0.230 | 0.145 | 0.037 | 0.024 |
| 2.6 | 12 | 0.123 / 0.168 | 0.016 | 0.010 | 0.010 | 0.123 | 0.078 | 0.021 | 0.013 |

The vacuum-start control gives O and D of 0.018-0.025 at L = 8 at every k: that is the noise floor of a disordered field.
Reading (GUIDE): the step-1 field carries the boundary-layer colour order of rows 950/952 (O_1 grows with beta, and at
beta 2.3 falls with L like L^(-3/2), i.e. no order, as row 950 found); the step-k field is at the noise floor from k = 2-3
on. The memory of slice 0's colour frame (D_k, the displacement of slice k from u_xy along the tie mode) decays over a few
slices (D_3/D_1 about 0.5-0.65, at the floor by k = 8-16 at every beta and L). One irregularity: at beta 2.6, L = 12, O_1bar
is 0.123 cold against 0.168 hot (27 percent apart). O_1 is not in a verdict except through the threshold O_1bar/2, and A
fails on its plaquette clause anyway; I record it as a sign that the colour direction of the ordered layer at beta 2.6,
L = 12 equilibrates slowly in the heat bath (consistent with row 950's growing susceptibility there), not as a result.

### 7.3 Controls (as fixed in 3.4)
- (C-start) PASS everywhere: f_3 and f_a are 0 for cold and hot; s_k cold against hot differ by at most 0.003 (k >= 4)
  against the tolerance 0.05.
- (C-vac) PASS: vacuum start against u_xy start at k >= 8: 0.399 / 0.398 (beta 2.3), 0.370 / 0.370 (2.4), 0.329 / 0.330 (2.6),
  within 0.002. Bulk <P> = 1 - s: 0.60, 0.63, 0.67 against the recalled 0.60, 0.63, 0.67. In the vacuum start the frozen
  slice is typical, so the analogous "within 10 percent of the frozen value" set holds with f' = 0.89-1.00 at every k: the
  pipeline does detect a set that is not left.
- (C-buffer) PASS: s_30 at L = 8 with T = 40 against T = 46: 0.397 / 0.399 (2.3), 0.371 / 0.370 (2.4); s_45 with T = 56 against
  T = 61 at 2.6: 0.328 / 0.334; all within 0.03. (The top slice itself sits higher, s_T about 0.42 at beta 2.3: the half-weight
  free top, which the buffer removes from k <= a.)

### 7.4 Verdicts (Section 3.3)
- beta 2.3, 2.4 (a = 30) and 2.6 (a = 45), L = 8 and 12, for A and for A': **TRANSIENT**. 1 - f_3 = 1.00 >= 0.95 (pooled:
  0 of 640 configurations per beta in A at k = 3). REFUTE is excluded: f_a = 0 against 0.30.
- Prediction of Step 3b scored: s_1 < 1.0 at all betas (seen 0.39-0.47): correct; f_1 = 0: correct; O_k decays in a few
  steps: correct (noise floor by k = 2-3).

## Step 8. What this shows and what it does not

Shown (GUIDE, not proof): from the layered pi-flux slice u_xy, the SU(2) Wilson half-slab at beta 2.3, 2.4, 2.6 on L = 8, 12
leaves the set A of row 975 1(e), and the purely gauge-invariant set A' = {s_xy >= 1.8}, in one step in every one of 1,920
configurations; the excess xy action is gone by step 2, and the colour order of the step field and the memory of the frozen
frame are at the noise floor by k = 2-3 and k = 8-16. So the high-action ties of rows 950, 952, 970 at u_xy are transient
for the trace at GUIDE level, Outcome B of row 975 8.2: by Lemma META, the set A (or A') adds nothing to S(a;B) beyond
its tiny stationary probability, and this test gives no objection to the box (a; (4a)^3) at a = 30 (beta 2.3-2.4) or 45 (2.6).
Not shown, and why the result is weak (ARGUED, Step 3b): u_xy is a hilltop of the slice potential (each xy plaquette a
thin centre vortex at action 2 beta, removable for about 0.9 beta per site in one step along the tie mode), so a set
defined by "xy action near the frozen value" is left in one step for a classical reason; the run confirms that but could
not have found anything else. The escape test of 1(e) therefore does NOT test the sets that could actually be metastable
after relaxation: (i) the colour direction n chosen by the ordered boundary layer at beta >= 2.5 (row 950's order lives in
the step-1 field, which is not a slice set; D_k suggests its memory is lost in about 8-16 slices, but D is frame-dependent,
caveat C1); (ii) spatial centre-holonomy (flux) sectors of a small torus at large beta, which a relaxed slice could sit in
for long (row 975 1(c)(ii) names this as the U(1) failure mode; for SU(2) at L = 8-12 and beta 2.6 the torus is near the
deconfinement extent, `gap-sc-max.md` 5.7 caveat). A later row that wants a real ESC test should take A = a holonomy
sector or a fixed-n neighbourhood of the RELAXED slice and start from pi(.|A), not from a frozen point (caveat R1).
Point start only (R1); L = 8, 12 only (C3; s_k agrees between L = 8 and 12 to 0.003, so no L dependence is visible).
Nothing in the proof chain changes; Lemma META and Corollary ESC-nec were not re-checked here.
Credits: slab code and the u_xy slice from row 952 (`guide/lane952/sg2lab.py`, Claude Opus 5.5), the colour-order
observable from row 950 (`gap-sc-max.md` 5.5-5.7), the test design from row 975 (`gap-ymcons-opus.md` 1(e)). The Sussman-Alpoge
repository was not needed for this numeric test and was not read in this row.

RESULT: Row 976 (GUIDE, Claude Opus 5.5 high, Mac mini): escape test 1(e) of row 975 run as pre-set: SU(2) half-slab frozen at u_xy, beta 2.3/2.4 (T 40, a 30) and 2.6 (T 56, a 45), L 8 and 12, cold and hot, 1,920 configurations: no configuration has xy action >= 1.8 at any k >= 1 (largest s_1 = 0.51 against frozen 2; s_k at the bulk 0.40/0.37/0.33 by k = 2), so f_k = 0 for A and the gauge-invariant A' at every k; verdict TRANSIENT at all three betas (ties of rows 950/952/970 at u_xy are transient, Outcome B), REFUTE excluded; start, vacuum and buffer controls pass; colour order and frame memory at noise by k = 2-3 and 8-16. Weak by construction (u_xy is a hilltop, left in one step classically, Step 3b); OPEN: escape from metastable sets of the relaxed slice (colour direction n of the ordered layer at beta >= 2.5, centre-holonomy sectors of small tori), a pi(.|A) start, and the seed itself.
