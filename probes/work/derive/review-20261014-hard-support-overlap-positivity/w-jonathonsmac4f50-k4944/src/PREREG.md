# K2c pre-registrations (written 2026-10-14 17:38Z by `date -u`, BEFORE any K2c test script is run)

Agent: Claude Opus 5.5, test agent K2c (same family as K2, K2b, X3 and the supervisor; NOT an independent referee).
Parent: K2 (`kills/K2/`), codex referee on K2 (`ref_K2/REFEREE_VERDICT.md`, `REFEREE_CHECKS.md`), K2b (`kills/K2b/`), X3.
Code base: K2's `lat2d.py` and K2b's `k2b_lib.py`, copied UNCHANGED into `K2c/scripts/` (sha1 5f1de922…, 0b74107f…, equal
to the originals), plus my own `k2c_lib.py` and test scripts. Conventions unchanged: 2D U(1), Lx = 2, Wilson r = 1, M = 1,
m = mf = 0.05, link reflection t -> 1 - t, Theta = theta o conj on temporal links, beta_g = 0, exact gauge-invariant
reduction of the crossing-link integral (K2 `nodes`).
Rules: readings fixed now, never edited; later changes go in dated follow-ups. numpy/scipy, OMP_NUM_THREADS=2, one run at
a time, peak RSS < 0.3 GB (measured with /usr/bin/time -l), kill what I start.
Only pre-run probe: `scripts/quad_probe.py` -> `quad_probe.out` (log Z of ONE off-diagonal entry per geometry with the HARD
weight, O and W; no kernel matrix, no eigenvalue). Seen: open Lt = 12, 20: GL n = 8..32 agree to 1e-14 in log Z; torus
Lt = 12, 16: (n, nw) = (6, 4) vs (8, 6) vs (12, 8) agree to 2.5e-12 / 4e-14; (4, 4) is off by 3.6e-11 at Lt = 16. Peak 160 MB.

## The measure under test (X3's, exactly)
Crossing plaquettes carry the HARD admissibility indicator 1(|arg U_p| < delta), delta = 0.6, beta_g = 0 (X3 T-X3f/f':
"crossing-link Haar integral restricted to the admissible set |arg P_x| < delta"; X3 price P-X3d "plaquette bound as a hard
support constraint"). Bulk plaquettes of Lambda+ and Lambda- carry the same indicator; the pool configurations are admissible
WITH MARGIN: every bulk plaquette |arg U_p| <= 0.55 = delta - 0.05 (enforced by the candidate generators: rejection at 0.55).
This restricts the test functions f only, not the measure. The crossing integral runs over the full admissible set |d| < 0.6.

## Is the hard-measure kernel RP for pure gauge? (stated now; proved = mine, unrefereed)
- Character expansion: 1(|theta| < delta) = sum_n c_n e^{in theta}, c_n = sin(n delta)/(n pi), sign-changing (at delta = 0.6:
  c_n < 0 for n = 6..10, 16..20, ...).
- 2D, one crossing plane with Lx crossing plaquettes, beta_g = 0, NO fermions: integrating the crossing links gives
  K_PG(a, b) = sum_n c_n^Lx e^{in(W_b - W_a)}, W = Wilson line of the boundary slice. **Lx even (here Lx = 2): positive-type,
  so the pure-gauge kernel IS RP (proved).** For Lx = 2 it is the triangle (2 delta - |W_b - W_a|)_+ (the code's weight sum).
  Torus (two planes): product of two such positive-type kernels -> PSD by Schur's product theorem (proved).
- **Lx odd: NOT positive-type (c_n^Lx < 0 for n = 6..10)** -> the pure-gauge hard measure is NOT RP (proved via Bochner,
  since W ranges over the whole circle). Checked below by a pure-function computation (PG-odd).
- Higher-dimensional slices (suggested, not tested): the gauge projection keeps closed currents n on the slice; the current
  3 dP1 - 3 dP2 on two adjacent plaquettes has coefficient c_6 c_3^6 c_0^rest < 0, so the hard measure's pure-gauge character
  coefficients are not all >= 0 in >= 3D either. Whether that yields an actual negative eigenvalue depends on the support of
  the slice plaquettes (|theta_P| < delta), so this is suggested only.
- With charged fermions (Wilson OR overlap): NOT guaranteed RP even for Lx = 2 (K2 Amendment A1: Gauss law lets n_x differ,
  products c_{n0} c_{n1} of mixed sign enter). So Wilson + hard is a same-measure comparison, not a guaranteed-PSD control.

## Common definitions
- Kernel Zn_ab = Z_ab / sqrt(Z_aa Z_bb) (unit diagonal); lam_min, lam_max its extreme eigenvalues. Kernels: PG (no fermion),
  W (Wilson + m), O (Neuberger overlap), SH (Shamir-kernel overlap), DWF_Ls (PV-subtracted Shamir DWF det D5(mf)/det D5(1),
  transfer-matrix formula of K2b V3, re-checked here against the dense 5D ratio on 3 points per pool, < 1e-10 required, else
  the pool's DWF columns are dropped), D5_Ls (bare dense 5D det, open pools only).
- Quadrature: open: GL n = 16 (LOW, used in the search) and 32 (HIGH). Torus: (n per plaquette, nw Polyakov) = (6, 4) LOW,
  (8, 6) HIGH. Third level on a subset (open n = 48; torus (10, 8)): 24 random off-diagonal entries + the diagonal.
- q = max_ab |Zn_HIGH - Zn_LOW|; q3 = max over the subset |Zn_THIRD - Zn_HIGH|. **Error estimate E = k max(q, q3) + 1e-13**
  (Weyl: |d lam| <= k max |dZ_ab|; 1e-13 roundoff floor). E is an a-posteriori estimate that bounds the HIGH-level error
  only if convergence is monotone/geometric (supported by the probe and by q3 << q); it is NOT a rigorous analytic bound.
- Clean pool: q < 1e-6, every pool member has max bulk |arg U_p| <= 0.55, and min |eig H| > 0.1 at every evaluated point
  (H_W for O; H_T as well for SH/DWF).
- Certified negative: lam_min < -10 E. PSD-within-error: lam_min > -10 E.

## K2c-A (open time) and K2c-B (torus): K2b's greedy search under the HARD measure
Search (K2b-T1/V1 rule, unchanged except weight and margin): start k0 = 8 random admissible-with-margin configurations
(links N(0, 0.25^2)); per step C = 8 candidates (3 random, 3 perturbations sigma 0.02/0.05/0.1 of pool members, 2 holonomy
shifts c ~ U(-0.3, 0.3)), all margin-admissible; add the best by the objective, at LOW quadrature:
- `search`: smallest eigenvalue lam_min of the bordered overlap kernel;
- `gsearch` (Wilson-referenced): min generalized eigenvalue of (Zn_O, Zn_W) on Zn_W's span with eigenvalue > 1e-6 of max.
Runs (seeds = K2b's where K2b had them):
- A (open, Lx = 2 antiperiodic x): Lt = 12: search 1201, gsearch 4201, K = 20; Lt = 20: search 1220, gsearch 5220, K = 20.
- B (torus, Lx = 2 periodic x, antiperiodic t): Lt = 12: gsearch 4212 K = 32, search 1212 K = 24; Lt = 16: gsearch 4216
  K = 24, search 1216 K = 20.
- Power reference (in-run, same code, same margin generator, Fejer weight = K2's A1 measure): open Lt = 12 search 1201 and
  gsearch 4201, Lt = 20 gsearch 5220 (K = 20). The K2b Fejer searches (certified negatives -3.45e-4, -1.40e-4, -1.58e-4;
  gen-ratio -1.23, -1.12, -1.07) are the external power reference.
Final pool: O, W, PG at LOW and HIGH; third level on the subset; report lam_min, min/max, q, q3, E, gen-ratio, Wilson and PG.

**Readings (fixed now), per geometry G in {open, torus}:**
- **PG-CONTROL-FAIL:** a clean final pool whose PG kernel is certified negative -> method suspect; every reading -> OPEN.
- **FAIL_G (X3's hard measure not RP in this proxy):** some clean final hard pool in G has a certified negative OVERLAP
  eigenvalue (PG PSD-within-error). Sub-label: **FAIL_G-overlap** if Wilson + hard is PSD-within-error on that pool;
  **FAIL_G-shared** if Wilson + hard is also certified negative on it (then the hard support with charged matter is itself
  non-RP; the failure is not overlap-specific).
- **PASS-at-power_G:** every hard pool in G is clean with no certified negative overlap eigenvalue, AND the in-run Fejer
  power reference gives a certified negative on >= 1 open run (otherwise CONTROL-NO-POWER -> OPEN). A PASS-at-power is
  not a proof; it says no violation > 10 E on the explored pools. Reported with: smallest hard lam_min and gen-ratio reached,
  vs the Fejer runs.
- **OPEN_G:** anything else (unclean pool; lam_min in [-10E, -E); power reference fails).
- Overall verdict on X3's measure (hard, Lx = 2 proxy): FAIL if FAIL_open or FAIL_torus; PASS-at-power if both
  PASS-at-power; OPEN otherwise.
- Expectation stated now: I do not predict the signs. The referee's hard-indicator rerun of K2's failing set gave +1.3e-3.

## K2c-C: PV-subtracted DWF under the hard measure on the searched pools
Pools: every final hard pool of A and B; plus K2b's two Fejer-searched open pools where K2b found PV-DWF negatives
(`pool_search_open_Lt12_seed1201_SH.npz`, `pool_search_open_Lt12_seed1201.npz`; these are admissible at 0.6, their margin
is reported, not enforced). Kernels from the same quadrature points, HARD weight: PG, W, O, SH, DWF_4, DWF_8, and bare D5_4,
D5_8 on open pools. (Torus: no dense D5, for cost.)
**Readings:** "PV-DWF-hard FAIL at L_s" if DWF_Ls (L_s in {4, 8}) is certified negative on some clean pool; "PV-DWF-hard
PSD on the searched pools" if none is. Bare D5 + hard: reported; a certified negative there is attributed to the hard
indicator with charged matter (A1), not to PV. Expectation: none stated.
Optional (only if time remains; registered now): a DWF_4-targeted `search` on open Lt = 12 (seed 1301, K = 20, hard), same
readings for DWF_4.

## PG-odd: pure-gauge hard kernel for odd Lx (pure functions, no lattice fermions)
K_PG(Phi) = (f^{*Lx})(Phi) on the circle, f = 1(|theta| < 0.6), computed by direct numerical convolution on a fine grid and
compared with the closed form (B-spline); circulant matrix on N = 64 equally spaced Wilson-line values W_a.
**Reading:** "hard measure non-RP for pure gauge at odd Lx (checked)" if Lx = 3 gives a certified negative eigenvalue
(< -1e3 x the grid-convergence change); Lx = 2, 4 must be PSD (else the code is wrong and PG-odd is void).

---
### Follow-up V1 (registered 2026-10-14 17:45Z, after seeing PG-odd (`pg_odd.out`); readings above unchanged)
Seen: the registered grid method is too crude: the FFT of the sampled box converges only O(1/M) (grid change 1.9e-4 at
Lx = 2, 5.3e-5 at Lx = 3). Lx = 3 gave lam_min -3.99e-3 against a grid change 5.3e-5 (ratio 75 < the registered 1e3), so
the registered PG-odd reading is NOT met as registered (no certification by that method). Lx = 2, 4 PSD; Lx = 1 (not
registered, descriptive) -2.9 relative -0.22.
V1 (exact method): for N equally spaced Wilson-line values the circulant's eigenvalues are EXACTLY
lam_j = N sum_{n = j mod N} c_n^Lx (aliasing identity), c_n = sin(n delta)/(n pi). Sum truncated at |n| <= 10^6 with the
rigorous tail bound sum_{|n| > Nmax} |c_n|^Lx <= 2 / (pi^Lx (Lx - 1) Nmax^(Lx-1)) for Lx >= 2.
Reading: "hard measure non-RP for pure gauge at Lx = 3 (checked, exact)" if min_j lam_j < -1e3 x N x tail bound;
Lx = 2, 4 must give min_j lam_j > -N x tail bound (else V1 is void). Run queued after chain A (one run at a time).
Timestamp correction (appended 17:42Z): V1 above was registered at 17:40Z by `date -u`, not 17:45Z as typed in its header.

---
### Follow-up V2 (registered 2026-10-14 17:42Z, after seeing the first open-time results: hard search 1201 PSD +1.68e-4,
hard gsearch 4201 PSD with gen-ratio +0.66, while the in-run Fejer power reference 1201 is certified negative (-2.77e-4,
gen-ratio -1.23) and Fejer gsearch 4201 reached objective -1.05; readings of K2c-A/B unchanged)
Seen: on every hard pool the O, W and PG kernels have nearly the same lam_min (PG +1.8e-4 vs O +1.7e-4 on 1201), i.e. the
pure-gauge factor dominates. Proved (elementary): for Lx = 2 open, PG = (2 delta - |W_b - W_a|)_+ has a cusp at W_a = W_b
(Fourier coefficients ~ n^-2), while the Fejer PG = tri*tri is C^2 there (~ n^-4; Fejer PG lam_min +7.9e-10 on pool 1201).
Suspicion (stated before testing): the hard indicator's cusp adds a large positive-definite floor between configurations
with different boundary Wilson lines and may MASK a fermionic violation; if so the registered searches lack power.
V2 = W-MATCHED searches: every pool member and candidate is shifted to boundary Wilson line W(slice 1) = 0 (holonomy shift
c = -W/2 on all Lambda+ x-links; plaquettes unchanged); on the torus also W(slice T) is set to the first member's value by
adding the difference to the x-link (T, x=0) (changes one bulk plaquette; candidate kept only if the 0.55 margin holds).
Then Phi = 0 on every pair and the PG factor is constant (rank one): the kernel tests the fermion measure inside fixed-W
sectors (legitimate gauge-invariant test functions). Candidates per step: 4 random + 4 perturbations (sigma 0.02, 0.05,
0.1, 0.2), re-matched; no holonomy candidates. Same objectives, quadratures, E, clean and certification rules.
Runs: open Lt = 12: hard wsearch 1401, hard wgsearch 4401, Fejer wsearch 1401 and wgsearch 4401 (power reference for
this mode); open Lt = 20: hard wgsearch 5401, hard wsearch 1420; torus Lt = 12 hard wgsearch 4412 K = 24 and, if time,
torus Lt = 16 hard wgsearch 4416 K = 16. K = 20 for open.
Readings: **FAIL_G (hard, W-matched)** exactly as K2c-A/B (certified negative overlap eigenvalue on a clean hard pool;
sub-labels -overlap / -shared by Wilson + hard); this counts as FAIL_G for the overall verdict. **Power for this mode:**
the Fejer W-matched open runs give a certified negative ("W-matched mode has power") or not ("Fejer violation needs
distinct Wilson lines": then hard-W-matched PSD results carry no power reading). PASS-at-power_G is strengthened only if
hard W-matched runs are PSD while the Fejer W-matched reference is certified negative. OPEN otherwise.
Timestamp correction (appended 17:41Z by date -u): V2 above was registered at 17:41Z, and the V1 correction line at 17:41Z; the typed 17:42Z values were my estimates.

---
### Follow-up V3 (registered 2026-10-14 17:43Z by date -u, after seeing all seven open-time runs: hard 1201/4201 (Lt 12),
1220/5220 (Lt 20) all PSD with gen-ratio +0.50..+0.66; in-run Fejer reference 1201/4201/5220 all certified negative,
gen-ratio -1.13..-1.73; readings of K2c-A/B/C, V1, V2 unchanged)
V3 (descriptive, no reading): cross-evaluation on identical configurations: (i) the three in-run Fejer-negative pools
(pool_K2c_*_tri_O_open_*) evaluated under the HARD weight with k2c_dwf.py (all kernels); (ii) the K2c-A hard pool 1201
(Lt 12) evaluated under the Fejer weight. Queued after chain C, then (if time) the optional DWF_4-targeted hard search
(registered in K2c-C: open Lt 12, seed 1301, K = 20) and V2's torus Lt = 16 W-matched hard wgsearch 4416 K = 16.

---
### Follow-up V4 (registered 2026-10-14 17:44Z by date -u, after seeing the open hard gsearch objective traces still falling
at K = 20 (Lt 12: 0.91 -> 0.66; Lt 20: 0.97 -> 0.63), unlike the Fejer reference (below -1 within 3-7 steps); readings unchanged)
V4: the same deterministic runs continued to K = 48 (same seeds, so the first 12 steps reproduce): open Lt = 12 hard
gsearch 4201 and open Lt = 20 hard gsearch 5220. Readings exactly as K2c-A (FAIL_open if certified negative; otherwise the
pool counts toward PASS-at-power_open), and the report states whether the objective crossed zero, levelled off, or kept
falling. Queued in chain E after chain D.

---
### Follow-up V5 (registered 2026-10-14 18:04Z by date -u, after seeing V2: the W-matched HARD open Lt = 12 searches are
certified negative (wsearch 1401: lam_min -2.42e-3, min/max -1.21e-4, E 3.1e-13; wgsearch 4401: -1.13e-3, gen-ratio -1.13),
Wilson + hard and PG PSD within error on the same pools; the W-matched Fejer reference gives nearly the same numbers
(-2.40e-3, -1.12e-3). Readings of K2c-A/B/C, V1-V4 unchanged.)
V5 = bug hunt and robustness on pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz (the -2.42e-3 pool), BEFORE interpretation:
(V5a) independent builder (K2 V1b's explicit-link code, re-typed with the crossing links (0, phi_1) explicit): every
plaquette computed from links; bulk margin asserted (<= 0.55) from the explicit plaquettes; the admissible phi_1 set found
from the two explicit crossing plaquettes (each affine in phi_1, unwrapped branch chosen by wrap) and checked against a
dense scan; D_ov = 1 + X (X^dag X)^{-1/2}, X = D_W - M (no sgn(H_W)); Gauss-Legendre n = 32 and 64 on the admissible set.
Reading: the hard-measure FAIL stands as a code-level fact if V5a reproduces lam_min within 10% (relative to the main code)
with its own n32-n64 change < 1e-10; otherwise FAIL_open is downgraded to OPEN pending a fix.
(V5b) W-jitter: each member gets an independent holonomy shift so that its boundary Wilson line becomes eps * xi_a,
xi_a ~ U(-1, 1), eps in {1e-4, 1e-3, 1e-2, 3e-2, 1e-1} (main code, hard, GL 16/32); descriptive: lam_min vs eps (how
fast the PG cusp |W_b - W_a| restores positivity).
Queue reorganised (no reading changes): chains C, D, E are stopped before their next run; new chain F runs, one at a time:
V2_open_Lt20_wsearch_hard (as registered), V5, V2_torus_Lt12_wgsearch_hard, then K2c-C on: K2b's two pools, the two V2
open Lt 12 hard W-matched pools, the two A open Lt 12 hard pools, the torus hard pools (Lt 12 gsearch, Lt 16 gsearch),
the V2 torus pool; then V3; then V2 torus Lt 16; V4 last if time.

---
### Follow-up V6 (registered 2026-10-14 18:10Z by date -u, after seeing V5 (independent open builder reproduces -2.42150e-3 to
all printed digits; W-jitter keeps lam_min negative up to eps = 0.1: -2.35e-3 .. -1.8e-4) and V2 torus Lt = 12 W-matched hard
wgsearch 4412 certified negative (lam_min -1.473e-4, min/max -6.3e-6, E 5.5e-11, Wilson + hard +8e-15, PG -5e-15,
gen-ratio -0.28). Readings unchanged.)
The torus reduction (two crossing planes + Polyakov phase, K2's lat2d) has not been independently checked (K2 V1b and the
referee checked the open geometry only). V6 = independent torus builder on pool_K2c_wgsearch_hard_O_torus_Lt12_seed4412.npz:
explicit links on the antiperiodic-time torus (own indexing), crossing links (0, a1) on plane A and (b0, b1) on plane B,
EVERY plaquette (including both crossing rows and their orientation) computed from links; the admissible a1 and
y = b1 - b0 sets found from the explicit crossing plaquettes (checked by a dense scan); b0 (Polyakov) by trapezoid over the
full circle; D_ov = 1 + X (X^dag X)^{-1/2}. Quadrature (n_A, n_B, nw) = (6, 6, 4) on all entries, (8, 8, 6) on all entries
if time allows, else on the diagonal plus 10 entries. Reading: the torus FAIL stands as a code-level fact if V6 reproduces
lam_min within 10% with its own quadrature change < 1e-8 and the Wilson + hard kernel PSD; otherwise FAIL_torus is
downgraded to OPEN pending a fix. Queue: V6 runs next after the current chain-F job; chain F is restarted as chain G
with the same remaining order.

---
### Follow-up V7 (registered 2026-10-14 18:15Z by date -u, after seeing K2c-C on the W-matched torus pool: DWF_4 -5.08e-6,
DWF_8 -8.23e-6, SH -7.25e-6 certified negative; bare D5 not computed on the torus. Readings unchanged.)
V7 (control, only if chain G finishes before 18:40Z): bare D5_4 and D5_8 (dense) + hard on pool_K2c_wgsearch_hard_O_torus_Lt12_seed4412.npz
at (n, nw) = (6, 4) on all entries; change to (8, 6) on 10 entries + diagonal; E = k x change + 1e-13 (subset estimate,
labelled). Reading: "bare 5D det PSD on the torus pool" if lam_min > -10 E; a certified negative is recorded and attributed
to the hard indicator with charged matter (A1), not to PV.

---
### Results log (appended 18:28Z by date -u; readings applied as registered, none edited)
- PG-odd as registered: NOT met (grid method too crude, ratio 75 < 1e3). V1 exact: Lx = 3 certified negative (-3.99e-3,
  N x tail 2.1e-12); Lx = 2, 4 PSD -> "hard measure non-RP for pure gauge at Lx = 3 (checked, exact)".
- K2c-A (open, unmatched, hard): 4/4 pools clean and PSD (+7.0e-5 .. +2.75e-4; gen-ratio +0.50 .. +0.66); in-run Fejer
  reference certified negative 3/3 -> PASS-at-power_open (registered reading for these runs).
- K2c-B (torus, unmatched, hard): 4/4 PSD (+3.2e-3 .. +4.5e-2; gen-ratio +0.43 .. +0.94) -> PASS-at-power_torus (same).
- V2 (W-matched, hard): open Lt 12 (1401, 4401) and Lt 20 (5401, 1420) certified negative -1.13e-3 .. -2.58e-3, Wilson +
  hard and PG PSD; torus Lt 12 (4412) -1.473e-4 (E 5.5e-11) and torus Lt 16 (4416) -7.27e-5 (E 3.2e-13), Wilson + hard and
  PG PSD; Fejer W-matched reference certified negative (power) -> FAIL_open-overlap and FAIL_torus-overlap; per V2 these
  count for the overall verdict: OVERALL FAIL (hard measure, 2D U(1) Lx = 2 proxy).
- V5: independent open builder -2.42150e-3 (main -2.4215e-3), change 1.1e-14 -> FAIL stands as a code-level fact; jitter
  eps 1e-4 .. 1e-1: -2.35e-3 .. -1.79e-4 (all negative).
- V6: independent torus builder -1.47281e-4 (main -1.4728e-4), change 1.1e-12, Wilson +8.8e-15 -> torus FAIL stands.
- K2c-C (hard): DWF_4 / DWF_8 certified negative on both W-matched open pools and on the W-matched torus pool -> "PV-DWF-hard
  FAIL at L_s = 4 and 8"; bare D5 PSD on the open W-matched pools; all kernels PSD on K2b's two pools and on the unmatched
  A/B pools.
- V3: Fejer-negative pool PSD under hard; hard-PSD pool certified negative under Fejer (O, SH, DWF_4, DWF_8).
- Not run (time): V4, C on A Lt 20 and B search pools, V3 on two pools, optional DWF_4-targeted search.
- V7 (appended 18:30Z): bare D5_4 +4.68e-8 (E 1.4e-12), D5_8 +9.40e-8 (E 6.8e-11) on the W-matched torus pool -> "bare 5D det PSD on the torus pool".
