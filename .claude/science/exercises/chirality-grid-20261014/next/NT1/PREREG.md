# NT-1 pre-registration: chiral-measure reflection positivity (route 1 / set B)

Written 2026-10-14 ~21:00Z (`date -u` 20:55:47Z at folder creation), BEFORE any NT-1 script exists or runs.
Agent: Claude Opus 5.5, test agent NT-1. Same family as K2/K2b/K2c, X3 and the supervisor: NOT independent, NOT a referee.
Parent: TESTS.md "NT-1" (exercise branch `origin/claude/chirality-grid-exercise-20261014`, TESTS.md:30-33); K2c
(`kills/K2c/K2c_REPORT.md`, codex verdict ROUTES.md:190-204). Code base: K2's `lat2d.py` and K2b's `k2b_lib.py`, K2c's
`k2c_lib.py`, copied UNCHANGED (sha1 recorded in REPORT) plus my own `nt1_*.py`.
Rules: readings below are the FIXED TESTS.md readings, restated, never edited; anything later is a dated follow-up.
numpy/scipy only, OMP_NUM_THREADS=2, one process at a time, peak RSS <= 0.4 GB (measured, /usr/bin/time -l), kill what I start.

## FIXED readings (TESTS.md:30-33, copied verbatim in meaning)
- **CHI-RP-FAIL:** a quadrature-converged negative RP eigenvalue (< -10x the error estimate) on W-matched gauge-invariant
  witnesses.
- **CHI-RP-PASS-at-power:** PSD within error, with the vector-like K2c witness as the power reference.
- **OPEN:** otherwise, including "a gauge-invariant chiral measure could not be built in budget". State which.

## 1. Model (genuinely chiral, anomaly-free, 2D U(1))
Primary: the **11112 model**: four left-handed Weyl fermions of charge 1 and one right-handed Weyl fermion of charge 2
(gauge anomaly sum_L e^2 - sum_R e^2 = 4 - 4 = 0; three neutral right-handed spectators can be added for c_L = c_R; they are
gauge-field independent and drop out of every normalized kernel). It is chiral: no L/R pairing of equal charges.
Reason for choosing it over 3-4-5-0 as primary: the largest charge is 2, so the charge-e fields U^e stay admissible
(H_W gapped) at K2c's delta = 0.6 with a much better chance than charge 5 (5 x 0.55 = 2.75 rad plaquettes).
Secondary (optional, only if time after the primary): 3-4-5-0 at reduced delta (0.12, margin 0.11, charge-5 plaquettes <= 0.6),
with its own vector-like power reference at the same delta.

## 2. The measure (Lüscher-type abelian construction; derivation mine, unrefereed; verified by gates G1-G7)
Conventions (K2): 2D, Lx = 2, open time (antiperiodic x for the fermion), Wilson r = 1, M = 1, H_W = g5 (D_W - M),
S = sign(H_W), massless Neuberger overlap D = 1 + g5 S, GW relation g5 D + D g5 = D g5 D. Then g5hat = g5 (1 - D) = -S, so
Lüscher's left-handed space P̂_- = (1 + S)/2 = positive spectral subspace of H_W(U^e); right-handed P̂_+ = negative subspace;
fixed barred projectors P_+- = (1 +- g5)/2.
- Weyl determinant (L, charge e): det M_L = det(vbar^dag D V) with V an orthonormal basis of P̂_-(U^e), vbar the standard
  basis of P_+. Since D V = 2 P_+ V, det M_L = 2^n det(V restricted to g5 = +1 rows) (Narayanan–Neuberger overlap <v-|v+>).
  R, charge e: negative subspace, g5 = -1 rows. The moduli are basis independent; only the phase needs the measure.
- **Phase = Lüscher's abelian construction (straight path + gauge-restoring current).** Let A be the link-angle vector
  potential of the joined configuration (the stored angles; no wrapping occurs since all angles are small, checked).
  (i) W0[A]: parallel-transport the basis V along the ray U_t = exp(i t e A), t in [0, 1], from a FIXED free-field basis
      (discrete transport V_{j+1} = polar(P̂(t_{j+1}) V_j), N_s uniform steps). This equals Lüscher's straight-line
      homotopy measure term L0 = i int_0^1 dt Tr{P̂_t [d_t P̂_t, delta P̂_t]}, which vanishes along the ray.
  (ii) Anomaly density (derived from L_omega = -i Tr{delta_omega D P̂ D^-1 P}): A(x) = sum_L e q_e(x) - sum_R e q_e(x),
      q_e(x) = -(1/2) tr_spin S_e(x, x).
  (iii) k = a link current with lattice outflow-divergence div k = A along the ray; kbar = int_0^1 k[tA] dt.
      Choice in this Lx = 2 open geometry: t-links carry K(t)/2 each, K(t) = sum_{s <= t} sum_x A(x, s) (the 1D Poincaré sum;
      exists because sum_x A = 0 at index 0, gate G6); the two x-links of a slice carry +-(A(0,t) - A(1,t))/4.
      The remaining freedom (divergence-free additions) is the usual local-counterterm ambiguity.
  (iv) **W = W0 + i s_k sum_links A_l kbar_l**, rho_chi = exp(W), up to one global constant.
      Derivation (mine): L = L0 + d Psi, Psi = -sum A kbar, gives dL = curvature (integrability) and L(gauge direction) =
      the anomaly term, hence exact gauge invariance; anomaly freedom is what makes k LOCAL (diagnostic D1 below).
      The sign s_k in {+1, -1} is a convention sign: it is fixed by gate G2 on the first gate configuration; the other sign
      must FAIL G2 by > 100x, else G2 fails.

## 3. RP kernel for a complex weight (Hermiticity)
Witnesses as K2c V2: gauge-invariant functions concentrated on the gauge orbits of W-matched half-configurations
(boundary Wilson line W(slice 1) = 0). Kernel entry, K2 convention (`lat2d.py:179-241`): K(a, b) = sum_i w_i rho(J(a, b, phi_i)),
J = a on Lambda+, theta(b) on Lambda-, crossing links (0, phi_1) after exact gauge reduction, hard weight 1(|d| < delta).
- For a complex weight, RP means: K is Hermitian AND PSD. K(b, a) = conj K(a, b) for all witnesses holds iff the weight is
  Theta-real: rho(theta U) = conj rho(U) (theta = link reflection t -> 1 - t, t-links reversed; crossing angle phi -> -phi),
  up to one global constant phase which is removed by convention. This is checked (G3), never assumed: NT-1 computes BOTH
  K(a, b) and K(b, a) directly (no Hermitian fill), reports the Hermiticity defect h = max|Zn - Zn^dag|, and folds h into E.
- If Theta-reality fails beyond error (h > 1e-6 not explained by quadrature/transport), the reading is **OPEN ("a
  Theta-covariant gauge-invariant chiral measure was not built")**, NOT CHI-RP-FAIL (a non-Hermitian kernel is a failure of
  my measure's phase convention, not shown to be the theory's).
- Normalization Zn = K / sqrt(diag); requires K(a, a) real and > 0 (checked).

## 4. Gates (all must pass on a pool's configurations before its kernel counts)
- G1 (factorization): |det M_L(e)| |det M_R(e)| = |det D(e)| (massless overlap), and |det M_L| = |det M_R| at index 0;
  rel. error < 1e-10 on 5 configurations.
- G2 (gauge invariance of rho_chi): |Delta ln rho| < 1e-6 under (a) the lower-half constant shift (all crossing links + c,
  c = 0.3) and (b) random local gauge transformations (omega ~ N(0, 0.2^2) per site), on 5 joined configurations, after
  transport convergence. Reported alongside (descriptive): the same for W0 alone (must fail, showing the current matters).
- G3 (Theta-reality): rho(theta J) / conj rho(J) = constant c (same for all J) to 1e-6 on 5 configurations.
- G4 (transport convergence): N_s chosen as the smallest of {16, 32, 64, 128} with max |Delta ln rho| (N_s -> 2 N_s) < 1e-8
  on the gate configurations; q_PT = max |Zn(N_s) - Zn(2 N_s)| on a 24-entry subset of each pool is folded into E.
- G5 (admissibility for every charge): min |eig H_W(U_t^e)| > 0.1 at every evaluated ray point, node, charge.
- G6/G7: index 0 (n_+ = n_- = N/2) for every charge along every ray; |sum_x A(x)| < 1e-10.
If G5 fails on K2c's delta = 0.6 pools for charge 2: fall back to new W-matched pools at delta = 0.3 (margin 0.275) for
BOTH the chiral kernel and the vector-like reference (dated follow-up).

Diagnostic D1 (descriptive, not a gate; Lx = 2 cannot test 2D locality fully): locality of K(t) in t: change of K(t) under a
perturbation of the bottom-most slice, for 11112 vs the anomalous single left-handed charge-1 Weyl (expected: anomalous
K(t) carries the far-boundary Wilson line (e^2/2pi)(W_bottom - W_{t+1}); anomaly-free does not).

## 5. Tests
Error estimate as K2c: E = k max(q, q3, q_PT, h) + 1e-13; q = max |Zn(n=32) - Zn(n=16)|, q3 on 24 entries + diagonal at
n = 48. Certified negative: lam_min(Herm. part) < -10 E. PSD-within-error: lam_min > -10 E.
- **T1 (main): chiral kernel on K2c's W-matched open pools** (copied npz): Lt = 12 `wsearch_hard 1401`, `wgsearch_hard 4401`;
  Lt = 20 `wsearch_hard 1420`, `wgsearch_hard 5401`. On each pool also: vector-like overlap O (K2c's op, m = 0.05; power
  reference, must reproduce K2c's lam_min to 1e-6 relative), massless vector overlap, the modulus-only chiral weight |rho_chi|
  (descriptive: isolates the phase), Wilson + hard and PG controls.
- **T2: W-matched greedy search on the chiral kernel** (K2c wsearch rule: 8 matched random starts, per step 4 random +
  4 perturbations sigma 0.02/0.05/0.1/0.2, margin 0.55; objective lam_min of the Hermitian part at LOW quadrature),
  open Lt = 12, seed 7401, K = 20; vector-like O evaluated on the final pool as power reference.
- T3 (optional, time permitting): 3-4-5-0 at delta = 0.12 on a W-matched search pool (seed 7412), with vector-like
  reference at the same delta.
- Not planned (budget): torus (needs the harmonic/Polyakov part of k fixed by Theta-covariance), Lx >= 4, 4D, non-abelian.

## 6. Overall reading rule (applied mechanically)
- CHI-RP-FAIL: >= 1 pool with all gates passed and chiral lam_min certified negative.
- CHI-RP-PASS-at-power: every gated pool (>= 3 pools incl. T2) PSD-within-error for the chiral kernel AND the vector-like O
  certified negative on those same pools (power reference).
- OPEN otherwise, stating which (gates failed -> "measure not built in budget"; Hermiticity failed -> "Theta-covariant
  measure not built"; power missing -> "no power").
Scope stated in advance: finite 2D U(1) proxy, Lx = 2, open time, beta_g = 0, hard support, one choice of local current
(counterterm freedom not scanned); a PASS would not prove infinite-volume RP and a FAIL would not reach 4D or non-abelian.

---
## Dated follow-up F1 (2026-10-14 21:03Z, after `scripts/gates_Lt12_1401.out` and `scripts/g4r_Lt12.out`; readings unchanged)
Seen: G1 PASS (1.8e-14); G2 PASS with s_k = -1 (max phase violation 5.2e-7 at Ns = 128; other sign 5.6e-3; W0 alone
2.8e-3, so the current is doing the work); G3 PASS (constant c, spread 1.4e-13); G5 PASS (min gap 0.455 with charge 2 at
delta = 0.6); G6/G7 PASS. **G4 as registered FAILS**: the plain discrete transport converges only as Ns^-2 (3.0e-7 at
64 -> 128). Amendment (registered before any kernel is computed): transport = Richardson value R(N) = (4 W(2N) - W(N))/3,
whose change R(16) -> R(32) is 1.9e-9 and R(32) -> R(64) is 1.2e-10 (`g4r_Lt12.out`). Kernels use R(32) (= Ns 32 + 64);
q_PT := max |Zn(R(32)) - Zn(R(64))| on the 24-entry subset, folded into E as registered. The T2 search objective uses
R(16) at LOW quadrature; the final T2 kernel uses R(32). G2 is re-run with R(32) on every pool's gate configurations by
`nt1_kernel.py` before its kernel (threshold 1e-6 unchanged).
Diagnostic D1 as run perturbed the BOTTOM boundary slice; that change is absorbed at the open boundary for both models
(anomalous L1 also local), so it does not discriminate. D1' (descriptive, registered now): insert flux at the middle slice
(add delta/2 = 0.05 to both x-links of every slice above the middle; only one crossing-of-slices plaquette pair changes) and
compare |dK(s)| far above the middle for 11112 vs L1 (expected: L1 non-decaying ~ e^2 delta/2pi, 11112 decaying).
(Note: F1's header time '21:03Z' was typed ahead of the clock; `date -u` at the append was 21:01:46Z.)

## Dated follow-up F2 (21:15Z, before any kernel eigenvalue was seen; readings unchanged)
The first T1 run (R(32) transport) was killed after 11 min without reaching its LOW kernel (no kernel number produced; its
only output lines are the per-pool G2 = 8.2e-11 and G3 = 5.7e-14 gate passes). Speed-ups: (i) the Dirac operator is now
assembled by a sparse matmul (identical to the einsum form, max difference 0.0, `prof.py`); (ii) **kernels use R(8)**
(Ns 8 + 16; R(8) -> R(16) change 3.1e-8 in ln rho on the gate configurations, `g4r_Lt12.out`), with q_PT := max |Zn(R(8)) -
Zn(R(16))| on the 24-entry subset folded into E exactly as registered. G2/G3 per pool are run with R(8). The T2 search
objective uses R(4) at LOW quadrature (objective only); its final pool is evaluated by nt1_kernel.py with R(8).
Lt = 20 pools (N = 80) cost ~4x per entry; they run only if time remains after T1 (Lt = 12) and T2.

## Dated follow-up F3 (21:23Z, after T1 pool 1401's output; readings unchanged)
Bug found in nt1_kernel.py's normalization: (a) the Theta convention constant fixes the measure's global factor only up to
a sign (alpha = -c/2 mod pi); the run used the branch giving K(a, a) < 0 for every a (diag phase pi), so its printed chi
lam_min (-20.0 = -k) is the sign-flipped kernel; (b) the same complex constant was wrongly added to the modulus-only kernel
(mod row invalid). Fix: the global sign is the physical one, K(a, a) > 0 (partition function > 0); the script now checks
that all diagonal phases share one sign before choosing it (a mixed sign would itself be an RP violation and is reported);
mod gets no constant. Pool 1401's chi kernel is re-read from its saved Zn (sign flip only; q, q3, qPT, h unchanged) and
the pool is re-run in full with the fixed script at the end of the chain.

## Dated follow-up F4 (21:32Z; readings unchanged)
The first T2 search run had the F3 sign bug in its objective (killed after 2 steps; output kept as
`T2_search_Lt12_7401_killed_signbug.out`). Fixed the same way (global sign from K(u, u) > 0; every new diagonal entry
is checked for a nonzero phase) and restarted with the same seed. D1' ran (`D1p_Lt12.out`); its reading is in REPORT.
The 345 row of D1' has min |H_W| = 0.003 at delta = 0.6 (charge-5 fields not admissible), as anticipated in section 1.
An Lt = 20 kernel (pool 1420) is queued last and will be reported only if it finishes before ~22:35Z.

## Dated follow-up F5 (21:36Z; readings unchanged)
The T2 search's last addition (step 12) lowered min |H_W| to 0.060 < 0.1 (G5 fails for the k = 20 pool). Before any
T2 kernel number was produced, the k = 20 kernel run was stopped; the registered gate G5 is applied by evaluating the
k = 19 principal pool (members 0..18; search log min |H| 0.132 at k = 19) with nt1_kernel.py. The pool-1401 rerun is
kept after it; chain order: T2 k19 kernel -> 1401 rerun -> P1 -> Lt = 20 (if time).
