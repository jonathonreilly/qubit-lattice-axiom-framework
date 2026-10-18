# K2b pre-registrations (written 2026-10-14 16:23Z by `date -u`, BEFORE any K2b test script is written or run)

Agent: Claude Opus 5.5 (same family as K2, X3 and the supervisor; NOT an independent referee).
Parent: `kills/K2/KILL_REPORT.md` §4 item 4 (next tests (i), (iii), (ii)/(iv)).
Code base: K2's `lat2d.py` copied into `K2b/scripts/` (same conventions: 2D U(1), Wilson r = 1, M = 1, m = 0.05,
link reflection t -> 1 - t, Theta = theta o conj on temporal links, Fejer crossing weight (K2 Amendment A1), exact
gauge-invariant reduction of the crossing integral). Only one pre-run probe was made: `timing_probe.py` (cost and
quadrature convergence of ONE torus kernel entry; no kernel matrix, no eigenvalue; result: GL n = 4 vs 6 and Polyakov
trapezoid nw = 4 vs 6 agree to ~3e-12 in log Z at Lt = 12, 16, 20; entry cost 0.2 / 0.1 / 0.65 s).
Rules: readings fixed now, never edited; later changes in dated follow-ups. numpy/scipy, OMP_NUM_THREADS=2, one run at a
time, peak RSS < 0.3 GB (measured with /usr/bin/time -l), kill what I start.

Common definitions (all tests).
- Kernel Z_ab for a pool of k half-lattice configurations u_1..u_k (Lambda+ links), normalized to unit diagonal
  Zn_ab = Z_ab / sqrt(Z_aa Z_bb). lam_min, lam_max = extreme eigenvalues of Zn.
- Error: Zn computed at a LOW quadrature and a HIGH quadrature; q = max_ab |Zn_hi - Zn_lo|. Certified error bound on the
  eigenvalues of Zn_hi: E = k q + 1e-13 (Weyl: |d lam| <= ||dZ||_2 <= k max|dZ_ab|; the 1e-13 is a roundoff floor).
- Clean pool: q < 1e-6 and min|eig H_W| > 0.1 at every evaluated overlap point.
- Certified negative: lam_min < -10 E. K2's FAIL line (lam_min/lam_max < -1e-6) is reported alongside, as a flag.
- Wilson control on the same pool: PSD iff lam_min^W > -10 E^W.

---
## K2b-T1: torus gauged RP with power (K2 next test (i))

**Object.** Torus in t (antiperiodic fermions), Lx = 2 periodic x (K2's G3/G3p convention), Lt in {12, 16, 20}, delta = 0.6,
Fejer weight. Low/high quadrature: GL n = 4 / 6 per kink-free piece, Polyakov trapezoid nw = 4 / 6.
Lx = 4 on the torus is NOT run: the exact crossing integral is 2(Lx-1)+1 = 7-dimensional and the overlap entry cost is
then > 100x the Lx = 2 cost (stated now as a scope limit, not a result).

**Search (the direct search for the most negative direction).** Greedy pool growth on the overlap kernel:
start from k0 = 8 configurations; at each step draw C = 8 candidates, compute each candidate's new row (LOW quadrature),
and add the candidate that gives the smallest lam_min of the bordered unit-diagonal matrix; stop at k = 20 (torus Lt = 12,
two independent runs: random start seed A, clustered start seed B), k = 16 (torus Lt = 16, one run) and, if time, k = 14
(torus Lt = 20, one run). Candidate mix per step: 3 fresh admissible random configurations (links N(0, 0.25^2), rejection
on bulk plaquettes < delta), 3 perturbations of pool members (N(0, sigma^2) on every link, sigma in {0.02, 0.05, 0.1},
admissible), 2 holonomy shifts of pool members (every Lambda+ x-link + c, c ~ U(-0.3, 0.3); plaquettes unchanged).
The optimal observable on the final pool is the lam_min eigenvector (f = sum_a v_a delta_{u_a}, gauge-orbit concentrated).
Final pool: recomputed at LOW and HIGH quadrature for overlap AND Wilson (same pool).
Plus a clustered screen: one k = 16 clustered pool (one base, perturbation 0.05) at each of Lt = 12, 16, 20.

**Positive control of search power (same code, same budget).** The identical greedy search on the OPEN-time lattice
(Lx = 2 antiperiodic x, Lt = 12; K2's G1p geometry, where K2 found violations), k0 = 8 -> k = 20, GL n = 16 / 32.

**Readings (fixed now).**
- **CONTROL-NO-POWER:** the open-lattice search ends without a certified negative overlap eigenvalue. Then every torus
  result below is read OPEN (search lacks power), whatever its sign.
- **FAIL (torus violation found):** some clean torus pool (final or screen) has a certified negative overlap eigenvalue
  with the Wilson control PSD on the same pool. Then the open-end escape for L3g is closed: gauge-invariant RP of the
  gauged Dirac overlap fails on the torus too (2D U(1) proxy, same family, referee owed).
- **PASS-at-power:** the open control finds a certified negative, and every torus pool is clean with no certified
  negative. Power statement reported with it: (a) the smallest torus lam_min reached (the explored PSD margin), (b) the
  open control's most negative lam_min/lam_max, (c) E. A PASS-at-power does NOT prove L3g on the torus; it says no
  violation of size > 10E exists on the explored pools.
- **OPEN:** anything else (unclean pools; or lam_min in [-10E, -E)).
- Expectation stated now: I do not predict the torus sign. I expect the open control to find a certified negative (K2 V6
  found FAIL-line sets in 3/6 random Lt = 12 pools).

Diagnostic (no reading): generalized eigenvalues of (Zn_overlap, Zn_Wilson) restricted to the span of Zn_Wilson eigenvectors
with eigenvalue > 1e-8 lam_max^W; reported as min ratio.

---
## K2b-T2: domain-wall control at finite L_s (K2 next test (iii))

**Object.** Shamir DWF for the same 2D gauge fields: 3D (x, t, s) operator
D5(mf) = delta_ss' (D_W - M + 1) - P_- delta_{s',s+1} - P_+ delta_{s',s-1} + mf (P_- at (s,s') = (L_s,1) + P_+ at (1,L_s)),
P_pm = (1 pm g5)/2, M = 1, mf = 0.05, L_s in {4, 8}; D_W = K2's 2D Wilson operator. Measures:
 (a) the bare 5D determinant det D5(mf) (no Pauli-Villars);
 (b) the PV-subtracted DWF measure det D5(mf) / det D5(1) (the 2D effective DWF determinant);
 (c) its L_s = infinity limit, the Shamir-kernel overlap det[(1+mf)/2 + (1-mf)/2 g5 sgn(H_T)], H_T = g5 A (2 + A)^{-1},
     A = D_W - M (code-checked against (b) at L_s = 40 on one configuration before use: |d log det| < 1e-8 required, else
     (c) is dropped).
**Pools.** Open time, Lx = 2 antiperiodic x: K2's G1p delta = 0.6 sets 0, 1, 2 (seed 262; set 1 = K2's -7.4e-6 FAIL set),
and K2 V6's Lt = 20 set 1 (seed 9010, the -3.3e-5 set). Torus Lt = 12 (K2 G3p convention): one random set (seed 565, set 0
= K2 G3p set 0). Quadratures as in K2 (open: GL 16/32; torus: n 4/6, nw 4/6). K2's Neuberger overlap and Wilson are
recomputed on the same pools for side-by-side comparison.

**Proof that (a) must be PSD (stated now, mine, unrefereed).** D5 is a 3D Wilson r = 1 fermion with gammas (g_x, g_t, g5)
= (s1, s2, s3) (Hermitian, anticommuting), mass -M, open in s, with the mf boundary term as an intra-slice coupling.
Its t-hops are the r = 1 projector form; its slice action is Theta-symmetric (g_t P_pm g_t = P_mp together with the
s-transpose maps the s-hops and the mf term onto themselves). So the Osterwalder-Seiler argument gives a PSD gauge-fixed
kernel, and averaging over the crossing links with a positive-type weight (Fejer, K2 A1) keeps it PSD.

**Readings (fixed now).**
- **T2a CONTROL-PASS:** every clean pool has (a) lam_min > -10E at L_s = 4 and 8. **T2a CONTROL-FAIL:** a clean pool with a
  certified negative in (a) -> the method is suspect and K2's FAIL and every K2b reading are downgraded to OPEN.
- **T2b readings (no prediction):** "finite-L_s DWF RP-safe on the failing sets" if (b) has no certified negative at
  L_s = 4 and 8 on the open pools where the Neuberger overlap is certified negative; "PV subtraction breaks RP" if (b) is
  certified negative at some finite L_s. For (c): "violation kernel-generic" if (c) is certified negative on some open
  pool; "Neuberger-kernel-specific on these pools" if (c) is PSD on all of them. Descriptive otherwise.
- Expectation stated now: (a) PSD (proved above). (b): the supervisor's brief expects PSD; my own expectation is NOT
  fixed: (b) is a ratio of two PSD kernels, which need not be PSD.

---
## K2b-T3 (only if time remains after T1 and T2): not registered yet. If run, it is registered in a dated follow-up
before the run.

---
### Note N1 (16:25Z, before any T1/T2 kernel run; readings unchanged)
Code sanity (`scripts/k2b_sanity.py`, output in `k2b_sanity.out`): my K2b library reproduces K2's G1p delta = 0.6 set 1
overlap min/max -7.4055e-6 exactly; T2 (c) check: |log det D5PV - log det SH| = 1.25e-2 / 9.8e-6 / 1.1e-8 / 4.9e-13 at
L_s = 8 / 16 / 24 / 40, so (c) passes its registered check (< 1e-8 at L_s = 40) and is kept. That check run peaked at
379 MB RSS (dense L_s = 40 operator, 1920 x 1920; seconds long): OVER the 0.3 GB rule, reported. Production runs use L_s <= 8.
Seeds fixed now: T1 open control 1201; torus Lt=12 random start 1212, clustered start 2212; torus Lt=16 1216; Lt=20 1220;
clustered screens (k = 16) 3012, 3016, 3020.

---
### Follow-up V1 (registered 16:32Z, after seeing T1 open control (certified negative, lam_min -3.45e-4, min/max
-2.14e-5, Wilson PSD, gen-ratio -1.23) and T1 torus Lt = 12 random-start search (lam_min +1.7e-5, gen-ratio +0.33); readings
of T1 unchanged)
Seen: the lam_min objective drives a PSD pool toward near-duplicate configurations (lam_min -> 0+), which wastes the search.
Change for a SECOND search mode `gsearch` (added code; `search` unchanged): objective = min generalized eigenvalue of
(Zn_overlap, Zn_Wilson) on the span of Zn_Wilson eigenvectors with eigenvalue > 1e-6 of its max (both kernels go degenerate
together on near-duplicates, so the ratio is not fooled). Everything else (candidates, k0 = 8, quadratures, final
verification, clean/certified/FAIL/PASS-at-power/OPEN readings of T1) is unchanged; FAIL still needs a certified negative
eigenvalue of the overlap kernel itself with Wilson PSD.
Runs: open Lt = 12, K = 20, seed 4201 (power control for this mode; CONTROL-NO-POWER reading applies to it); torus Lt = 12,
K = 20, seed 4212; and, if time, torus Lt = 16, K = 16, seed 4216.
Also (no reading change): the open control search 1201 is re-run once only to save its pool (deterministic seed) for T2.

---
### Follow-up V2 (registered 16:33Z, after seeing T2 on K2's failing set g1p_262_s1: Neuberger overlap certified
negative (-7.4055e-6, reproduced) while the Shamir-kernel overlap (c), DWF L_s = 4, 8 (b) and the bare 5D det (a) are all PSD;
T1/T2 readings unchanged)
Question: is the open-lattice RP violation specific to the Neuberger kernel H_W = g5(D_W - M), or does the Shamir-kernel
overlap (the L_s -> infinity limit of PV-subtracted DWF) also violate when searched with power?
Runs (same search code, target measure switched by a new optional argument OP = SH; everything else unchanged):
open Lt = 12: `search` seed 1201 and `gsearch` seed 4201 with OP = SH (same seeds as the Neuberger runs, so the
starting pools coincide); open Lt = 20 (T = 10): `gsearch` seed 5220 with OP = O and with OP = SH (matched pair); K = 20.
Readings: **SH-FAIL** if any SH run ends with a certified negative SH eigenvalue (< -10E) with Wilson PSD (then the violation
is kernel-generic, and finite-L_s DWF inherits it as L_s grows); **SH-PSD-at-power** if no SH run is certified negative
while the matched Neuberger runs (1201, 4201, 5220-O) are certified negative (then: "the K2 FAIL is Neuberger-kernel-
specific in this proxy; the Shamir/DWF route to L3g is open"); OPEN otherwise. Scope: same as K2 (2D U(1), Lx = 2, open time,
vector-like Dirac, gauge-only observables). No proof is implied by SH-PSD-at-power.
Queue re-ordered (no reading changes): remaining T1/T2 runs follow after V1-torus and V2.

---
### Follow-up V3 (registered 16:36Z, after seeing V2's first SH run: Shamir-kernel overlap search seed 1201 ends
certified negative (lam_min -1.05e-6, E 2e-13, min/max -6.5e-8, Wilson PSD, gen-ratio -0.89), i.e. the V2 SH-FAIL line is met;
the SH gsearch seed 4201 ended PSD (gen-ratio +0.014); readings unchanged)
Question: at which finite L_s does the PV-subtracted Shamir DWF measure inherit the violation?
Object: det D5(mf)/det D5(1) for L_s in {4, 6, 8, 12, 16, 24, 32, 48} and L_s = infinity, computed by the transfer-matrix
formula (1 - T^Ls)/(1 + T^Ls), T = (1 - H_T)/(1 + H_T), which is first checked against the dense 5D ratio at L_s = 4 and 8 on
3 points per pool (required max |d log det| < 1e-10, else that pool is skipped). Pools: the SH-failing pool
(pool_search_open_Lt12_seed1201_SH.npz), the Neuberger-failing open pool (pool_search_open_Lt12_seed1201.npz), K2's g1p_262_s1.
Quadrature and certification as T2. Readings: "finite-L_s DWF inherits the violation from L_s = L*" with L* the smallest
L_s certified negative on the SH-failing pool; "finite-L_s DWF PSD up to L_s = 48 on this pool" if none is certified
negative (then the L_s = infinity violation is a limit effect not seen at any tested finite L_s). Plus: T2 is run on the
SH-failing pool too, so the bare 5D det control (a) is checked on the very pool where SH fails.

---
### Follow-up V4 (registered 16:48Z, after seeing V1 torus Lt = 12 gsearch end PSD with the objective still falling
(0.86 -> 0.21 over 12 steps; open gsearch reached -1.1 by step 3); V3 result also seen (PV-subtracted DWF certified negative
from L_s = 4 on the SH-failing pool, bare D5 PSD there); readings of T1/V1 unchanged)
Reason: the torus search had not converged, so its PASS-at-power would be weak. Change: continue the SAME torus Lt = 12
gsearch (seed 4212; its first 12 steps reproduce V1 exactly) to K = 36. To fit the time box, the final verification is
cheaper when the pool is clearly positive: if the LOW-quadrature lam_min > 1e-6, q is estimated on 80 random off-diagonal
entries plus the diagonal at HIGH quadrature (overlap and Wilson), and the reported eigenvalues are LOW-quadrature; otherwise
the full HIGH-quadrature recomputation is done as before. Readings unchanged (FAIL needs a certified negative; a clearly
positive end is PASS-at-power for this pool, with E from the subset estimate, labelled as such).
Queue from now: T2 on v6_9010_s1, g1p_262_s0, g1p_262_s2 (pre-registered T2 pools); V4; V1 torus Lt = 16 gsearch (seed 4216).
Dropped for time (stated now, not run unless time remains): T1 torus clustered-start search 2212, Lt = 16 search 1216,
Lt = 20 search 1220, the three clustered k = 16 screens, T2 torus pool g3p_565_s0.

---
### Note N2 (17:08Z; descriptive, no reading): the PV denominator det D5(1) is claimed RP by the same OS argument
(PREREG.md:77-82 covers any real mf). Checked on the SH-search pool at L_s = 4, 8 after the Lt = 16 torus run
(`k2b_n2_pv_denominator.py`). If it were NOT PSD, the "ratio of two RP kernels" mechanism reading in the report is withdrawn.

---
### Follow-up V5 (registered 17:17Z, after seeing V4 end PSD at k = 36 with the torus objective still falling
(0.21 at k = 20, 0.089 at 28, 0.059 at 32, 0.032 at 36; a straight-line extrapolation crosses zero near k ~ 41) and the Lt = 16
gsearch end PSD at k = 16 (objective +0.22); N2 seen (det D5(1) kernel PSD); readings unchanged)
Run: resume the V4 pool (saved as pool_V4_final_torus_Lt12_k36.npz, k = 36) with the same gsearch rule, new candidate seed
5212, to K = 44 (time box: killed at 17:40Z if not done; then only the last completed step is reported, without
certification). Verification as V4. Readings as T1: FAIL if certified negative with Wilson PSD; otherwise PASS-at-power for
this pool, and the report states whether the objective crossed zero, levelled off, or kept falling.

---
### Results log (appended 17:28Z; readings applied as registered, none edited)
- T1 open control (16:26Z): certified negative, lam_min -3.45e-4, E 2.4e-13, Wilson PSD -> CONTROL-NO-POWER not triggered.
- T1 torus Lt = 12 random start (16:31Z): PSD, lam_min +1.71e-5, E 8.1e-9.
- V1 open gsearch: certified negative -1.40e-4. V1 torus Lt = 12 gsearch: PSD +7.47e-4 (objective +0.21). V1 torus Lt = 16:
  PSD +1.28e-5 (objective +0.22).
- V2: SH search 1201 certified negative -1.05e-6 (SH-FAIL); SH gsearch 4201 PSD; Lt = 20 matched pair: O certified negative
  -1.58e-4, SH PSD +2.9e-7.
- T2: bare D5 PSD on all 6 open pools (T2a CONTROL-PASS, open pools; torus pool dropped). DWF_4/8 PSD on K2's random pools;
  certified negative on the two searched pools (DWF_8 both; DWF_4 on the SH pool) -> "PV subtraction breaks RP". (c) SH
  certified negative on 2 pools -> "violation kernel-generic".
- V3: L* = 4 on the SH-search pool (negative at every L_s in 4..48 and infinity); Neuberger-search pool negative from L_s = 6.
- N2: det D5(1) kernel PSD on the SH-search pool (+1.34e-7, +1.58e-7).
- V4: torus Lt = 12 k = 36 PSD, lam_min +5.16e-5, objective +0.032. V5: k = 44 PSD, lam_min +3.89e-5, objective +0.013
  (still falling, slowing). T1 torus reading: PASS-at-power on the explored pools (pool-size-limited).
