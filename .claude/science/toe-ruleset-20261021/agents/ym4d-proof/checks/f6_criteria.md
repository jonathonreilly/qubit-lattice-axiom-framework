# f6 criteria (FLOW.md §22 target S3-3; written before checks/f6_iter_chain.py exists; the file's own stat is copied into
# FLOW_LOG.md before the script is created; this file is append-only from now on)

Purpose: a FALSIFICATION test of the composite structure (REVIEW_FLOW_S1_S2, strategic verdict): does the iterated
covariant chain, with composite paths through the intermediate centres and a background-dependent composite covariance,
put a log ℓ into the kernel-vertex part (failure mode U-F2 / S3-F4), which f5/f5b (one block, constant covariance) cannot
see? It is not evidence for (U-IR) beyond what it tests.

Object. Fine Z⁴, complex unit-charge scalar φ_0, U(1) background A, M_A as in f5 (massless). Two-level chain: level-1 blocks
of side L_1 = 3 (centres y), level-2 blocks of side L_2 ∈ {3, 5, 7} in level-1 units (centres c, which are level-1
centres; ℓ := 3L_2 ∈ {9, 15, 21}). Covariant averages:
  (Q0_Aφ_0)(y) := 3^{-4}Σ_{x∈B_1(y)}(1/24)Σ_σ exp(i∫_{σ: x→y}A)φ_0(x),
  (Q1_Aφ_1)(c) := L_2^{-4}Σ_{y∈B_2(c)}(1/24)Σ_σ exp(i∫_{σ: y→c}A)φ_1(y),
σ the 24 coordinate orders of the axial path, run on FINE links (the composite path x → y → c passes through the
intermediate centre y). Joint quadratic form (V = 0): φ_0^*M_Aφ_0 + κ_1Σ_y|φ_1(y) − (Q0_Aφ_0)(y)|² + κ_2Σ_c|(Q1_Aφ_1)(c)|²,
Γ_it(A) := log det of it (φ_0, φ_1 both integrated). Stiffnesses: κ_1 := s·3², κ_2 := s·ℓ² with s := κ_c(1 + L_2^{-2}),
chosen so that at A = 0 the fine marginal covariance equals f5's single-block covariance at the same ℓ and κ_c EXACTLY
(1/c_eff = 3²/s + ℓ²/s = ℓ²/κ_c, using Σ over level-1 aliases of |Q1 symbol|² = 1). κ_c ∈ {0.25, 1, 4}.
Γ_it = log det J_11(A) + log det(fine Schur complement), J_11 := κ_1 + κ_2Q1_A^†Q1_A on level-1 fields: the first term is the
scalar instance of Γ^cov (log det of the background-dependent composite covariance, up to a constant), the second the
scalar instance of Γ^{W0}.
Observables (β, c := β/2, per fine site, f5's definitions): c_it (total), c_it^M (diagrams whose vertices all come from
M_A), c_it^K := c_it − c_it^M (≥ 1 kernel vertex: Q0 or Q1), c^cov (the J_11 term alone; part of c_it^K). Single block:
f5's class integrand imported unchanged from checks/f5_cov_kernel.py at the same ℓ and κ_c: c_s, c_s^M, c_s^K.
Numerics: per coarse class, exact alias algebra (diagonal + per-level-1-alias rank + global rank); f5b's clustered
symmetric quadrature (P = t − 0.65 sin(ℓt)/ℓ, P3/P4 reflections and swap) with n = 10 points per coordinate; k-derivative
by central differences, h = 3e-4. NUMERIC LOCK; nice 10; 1 thread; peak < 1 GB.

Pre-registered criteria (validation):
- (V1) A = 0 propagator identity: at 4 random classes (ℓ = 9, κ_c = 1) the fine-fine block of the iterated joint covariance
  equals f5's single-block covariance: max relative difference ≤ 1e-12.
- (V1b) M-only identity: for every (ℓ, κ_c) of the scan, |c_it^M − c_s^M| ≤ 1e-9·|c_s^M|.
- (V2) reduction: with L_2 = 1 (no second-level paths; J_11 constant) the iterated per-class integrand (total and M-only)
  equals f5's at ℓ = 3 with c = c_eff, at 5 random classes and k = (1e-3, 2e-3, 0, 0): relative ≤ 1e-10.
- (V3) Ward identity of the iterated class formula on the torus of fine side 2ℓ (ℓ = 9; level-2 side 2; all 16 torus
  classes): |Σ_ν(e^{ik_ν} − 1)T_ν2(k)| ≤ 1e-10·Σ_ν|T_ν2(k)| at k ∈ {(2π/18)(1, 1, 0, 0), (2π/18)(1, 2, 1, 0)}, for κ_c = 1;
  the M-only analogue reported (informational).
- (V4) symmetry of the iterated integrand at 5 random classes (ℓ = 9, κ_c = 1, k = (1e-3, 2e-3, 0, 0)) under P3 → −P3,
  P4 → −P4, P3 ↔ P4: relative defect ≤ 1e-10.
- (V5) reality: max |Im| of every c value ≤ 1e-8·max|c|.
- (Q6) quadrature: c_it(9, κ_c = 1) with n = 10 and n = 14: relative difference ≤ 1e-4.
Pre-registered criteria (falsification; s(ℓ_1, ℓ_2) := (c(ℓ_2) − c(ℓ_1))/log(ℓ_2/ℓ_1), reported × 48π²):
- (G6) the iterated kernel-vertex part has no log: |s_it^K(9, 15)|·48π² ≤ 0.005 for each κ_c.
- (H6) the composite structure adds no log relative to the single block: Δ^K(ℓ) := c_it^K(ℓ) − c_s^K(ℓ);
  |s^Δ(9, 15)|·48π² ≤ 0.005 for each κ_c.
- (C6) the composite covariance term has no log: |s^cov(9, 15)|·48π² ≤ 0.005 for each κ_c.
- (G6') only if ℓ = 21 is run: for each κ_c, |s_it^K(15, 21)|·48π² ≤ 0.005 and |s_it^K(15, 21)| ≤ |s_it^K(9, 15)|; else
  reported NOT EVALUATED (neither PASS nor FAIL).
Rule for ℓ = 21 (fixed now): run it iff (wall time of the iterated ℓ = 15 scan, all κ_c) × 4.2 + (wall time of the single ℓ = 15
scan) × 4.2 ≤ 3000 s and the 1-minute load average is < 8 at that moment.
Informational: total slopes s_it(9, 15), s_s(9, 15) × 48π² (universal value 1); all c values; c^cov values.
Reading rule (fixed now): any FAIL of (G6), (H6), (C6) is reported as a FAIL. With two ℓ values f6 cannot separate a log
from an O(ℓ^{-2}) or O(L_2^{-2}) transient; failure mode S3-F4 is declared OBSERVED only if (G6') is evaluated and FAILS
for the same κ_c; any other interpretation of a FAIL is labelled post-hoc.

Outcome in checks/f6_out.txt, checks/f6_time.txt. A FAIL is reported as a FAIL.

---
AMENDMENT A1 (POST-HOC; appended 2026-10-28 ~03:50 UTC, AFTER f6's official run 02:08-02:44 UTC and AFTER REVIEW_FLOW_S3
fix S3-3; the text above is unchanged). Labelled as an amendment, not a reinterpretation: it replaces nothing above, and
the original (G6), (H6), (C6) FAILs stand as recorded in f6_out.txt.
Reason: REVIEW_FLOW_S3 §6.2 derived in closed form the scalar composite-covariance term of this file's chain,
  c^cov_closed(L_2) := −(L_2² − 1)²/(576 L_2⁴(L_2² + 1)),
which has zero log coefficient but a finite-difference slope s^cov(9, 15)·48π² = 0.0701 and s^cov(15, 21)·48π² = 0.0397, both
above the 0.005 threshold; so (C6) and (G6') as written test a slope threshold below a known transient (G6' would have
declared S3-F4 OBSERVED for a term that provably has no log). Do NOT run ℓ = 21 under the original (G6') rule.
Amended criteria (evaluated on the STORED f6 values, printed to 8 decimals in f6_out.txt; no re-run of f6):
- (A1-cov) closed-form identity: |c^cov_f6(ℓ) − c^cov_closed(ℓ/3)| ≤ 1e-8 at ℓ = 9 and ℓ = 15 (the printed rounding is 5e-9).
- (A1-G) residual kernel-vertex part: r^K(ℓ) := c_it^K(ℓ) − c^cov_closed(ℓ/3); |s_{r^K}(9, 15)|·48π² ≤ 0.005 for each κ_c.
- (A1-H) residual composite part: r^Δ(ℓ) := Δ^K(ℓ) − c^cov_closed(ℓ/3), Δ^K = c_it^K − c_s^K; |s_{r^Δ}(9, 15)|·48π² ≤ 0.005
  for each κ_c.
- (A1-G') if ℓ = 21 is ever run (not planned): the same two residual slopes over (15, 21), each ≤ 0.005·(48π²)^{-1}.
Reading rule: a PASS of A1-G/A1-H says only that, after removing the exactly known Γ^cov transient, the remaining kernel-
vertex and composite-path parts show no slope above 0.005 over (9, 15); two ℓ values cannot exclude a small log.
Outcome in checks/f6c_out.txt (script checks/f6c_closed.py, which only reads numbers from f6_out.txt).
(Correction to the A1 header, appended: the A1 block was appended at 2026-10-28 03:42:34 UTC per the file mtime, not "~03:50"; content unchanged.)
