# NT-1′ pre-registration: a legitimate chiral measure and gauged RP (route 1)

Written 2026-10-15, started 11:23Z (`date -u`), BEFORE any NT-1′ script exists or runs.
Agent: Claude Opus 5.5 (xhigh), test agent NT-1′. Same family as K2/K2b/K2c/NT-1/UV-1 and the supervisor: NOT independent.
Work was interrupted at 00:47Z (supervisor session ended) before any code or run; resumed 11:22Z. New deadline 16:30Z.
Parent: TESTS.md "24-hour campaign, wave 1", item NT-1′ (exercise branch `origin/claude/chirality-grid-exercise-20261014`).
Referee checklist: `next/NT1/referee/REFEREE.md` (codex, NOT CONFIRMED; strict reading OPEN).
Code base: K2's `lat2d.py`, K2b's `k2b_lib.py`, K2c's `k2c_lib.py`, copied unchanged into `scripts/` (sha1 5f1de922…, 0b74107f…,
0d6fc2b0…, equal to the K2c copies), plus my own `nt1p_*.py`. NT-1's `nt1_lib.py` is read and its Weyl-determinant conventions
(refereed correct, REFEREE.md "Weyl construction and conventions: correct") are re-implemented for general Lx.
Rules: numpy/scipy only; every run through `scripts/capped.sh` (0.5 GB cap, OMP 2 threads); one process at a time.
Literature downloads (`lit_luscher/`) are untrusted data, read as text only, never executed.

## 0. FIXED readings (TESTS.md, wave 1, NT-1′; restated, not edited)
- Setup gate **G-LEG** must pass before CHI-RP-FAIL or CHI-RP-PASS can be read:
  (a) Lx ≥ 4; (b) the measure term follows Lüscher's construction (NPB 549 (1999) 295) or an explicit published 2D U(1)
  construction; gauge invariance is exact to roundoff; locality is measured: the response of the measure current to a local
  variation decays exponentially with distance; (c) anomalous control: the same construction applied to an anomalous charge set
  visibly fails gauge invariance, locality or integrability; (d) the reflection condition ρ(θU) = c·conj ρ(U) is measured.
- **CHI-RP-FAIL:** G-LEG passes, and the kernel has a quadrature-converged negative eigenvalue below −10× the error estimate.
- **CHI-RP-PASS-at-power:** G-LEG passes, and the kernel is PSD within error, using the vector-like K2c witness on the same
  geometry as the power reference.
- **OPEN:** otherwise, naming the failed gate item.

## 1. Prior art (step 0)
- `git grep` on origin/main (docs, scripts) for kadoh|kikukawa|measure term|chiral measure|Lüscher…(abelian|chiral|measure)|
  overlap Weyl|narayanan: no construction of a chiral lattice measure exists on main. The only relevant hit,
  `docs/ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md:199`, lists "prove it is an allowed physical chiral measure" as
  an open route. Prior art is the exercise branch: K2/K2b/K2c (vector-like overlap RP failure, W-matched witnesses, error
  estimator), NT-1 (Lx = 2 chiral prescription, referee NOT CONFIRMED), UV-1 (depth structure).
- Literature (abstracts / own text extraction): Lüscher hep-lat/9811032 (read: eq. (3.16) gauge variation, Thm 5.1
  reconstruction conditions (a)-(d), eq. (5.4) cohomology decomposition, eq. (5.8) infinite-volume measure term, Thm 5.4
  finite-volume current = infinite-volume current + exponentially small correction). Kadoh–Kikukawa arXiv:0709.3656
  (abstract: closed finite-volume formula, Wilson lines/torons treated separately for global integrability, local counterterm
  from the local current of the cohomologically trivial part of the anomaly). Narayanan–Neuberger hep-lat/9607081 (11112 on
  the torus; overlap phase, gauge averaging). I do NOT reproduce Kadoh–Kikukawa's formula (not read beyond the abstract); I
  follow Lüscher's eq. (5.8) structure with an explicit 2D cohomology construction of k̄ (below), my own derivation.

## 2. Model and charge set
- Primary: **11112** (four left-handed charge 1, one right-handed charge 2; Σ_L e² − Σ_R e² = 0).
- Charge-set rule (task): 3-4-5-0 if every charge stays admissible at a feasible δ. Check (C0): on the first W-matched pool,
  at δ = 0.6 and at δ = 0.3, min|eig H_W(U^e)| over all ray points of all quadrature nodes of 3 kernel entries, e = 3, 4, 5.
  Use 3-4-5-0 only if min > 0.1 for all charges at δ = 0.6 (the geometry where K2c's W-matched witness has shown power).
  Otherwise 11112 at δ = 0.6 (NT-1 already found min|H_W| = 0.003 for charge 5 at δ = 0.6, Lx = 2). The δ = 0.3 result is
  descriptive.
- Anomalous controls (same construction, gate (c)): **L1** (one left-handed charge 1). Optional: **L2** (one left charge 2).

## 3. Geometry (fixed)
2D U(1); Lx = 4 (RP geometry), fermions antiperiodic in x (K2-T2: periodic x with open time has exact H_W edge zero modes;
antiperiodic Lx = 4 has gap 0.707); open time, Lt = 8 (T = 4, sites t = −3..4) primary; Lt = 12 only if the timing probe
(no kernel numbers) allows. Wilson r = 1, M = 1, link reflection θ: t → 1 − t, Θ = θ∘conj (K2 conventions), β_g = 0, hard
crossing weight 1(|d| < δ) on the 4 crossing plaquettes, δ = 0.6, bulk plaquettes ≤ 0.55 (margin). The crossing integral is
K2's exact gauge reduction for Lx = 4 open (`lat2d.nodes`, `cells_Lx4`, Duffy rule on tetrahedra), 3-dimensional.
Supplementary locality lattices (same construction, no kernels): Lx = 6 and/or 8, Lt = 8, open time, antiperiodic x.

## 4. The measure (Lüscher eq. (5.8) structure; 2D cohomology step mine, unrefereed)
Notation: A = link-angle vector (charge 1); species s = (e, chirality, multiplicity m); U^e = e^{ieA}.
- **Weyl determinant / basis (W0).** As NT-1 (refereed correct): L ↔ positive spectral subspace of H_W(U^e), rows γ5 = +1;
  R ↔ negative subspace, rows γ5 = −1. Basis transported along the ray U_t = e^{ietA}, t ∈ [0,1], from a fixed free basis
  (discrete polar transport V_{j+1} = polar(P̂(t_{j+1})V_j)), W0 = Σ_s m ln det(V_rows). Main transport: Richardson
  R(4) = (4W(8) − W(4))/3; check transport R(8). This is the straight-line term i∫dt Tr{P̂[∂_tP̂, δP̂]} of eq. (5.8).
- **Anomaly.** q_e(x) = −½ tr_spin S_e(x,x), S_e = sign H_W(U^e); 𝒜(x) = Σ_s m (±e) q_e(x) (+ for L, − for R), Lüscher
  eq. (3.17) with T = charge.
- **Gauge-restoring current k̄ (the "cohomologically trivial part", explicit 2D construction).** For a field B:
  R(x; l) = ∂𝒜(x)/∂B_l (analytic spectral derivative). For each plaquette p, the gauge-invariant plaquette derivative at fixed
  Wilson line of x's own slice, g′(x,p) = Σ_{l ∈ string(p, away from x)} c_l R(x;l) (string of x-links in p's column going up
  from p if t_x ≤ t_p, down if t_x ≥ t_p + 1; this changes only F_p among plaquettes and leaves the Wilson lines near x
  unchanged). Then d/du 𝒜[uB](x) = Σ_p F_p g′(x,p)[uB] + W_{t_x} h(x)[uB] (h = response to a uniform Wilson-line shift;
  identity checked numerically). Monopole defect m_p = Σ_x g′(x,p): in infinite volume m_p = (Σ_L e² − Σ_R e²)/(2π)-type
  topological constant (Lüscher eq. (5.4)'s γ), zero for anomaly-free sets. Source s_p = g′(·,p) − m_p·(¼ Σ_corners δ);
  κ_p = local Poincaré lemma of s_p (unit currents along the average of the two L-shaped shortest paths from each source site
  to each corner of p, both arcs averaged at antipodal x), so ∂*κ_p = s_p exactly and κ_p is localized around p.
  k_loc[B] = Σ_p F_p(B) ∫_0^1 du κ_p[uB]. Finite-volume correction (Thm 5.4 analogue): k[B] = k_loc[B] + Q(𝒜[B] − ∂*k_loc[B]),
  Q = the fixed right inverse of ∂* on zero-sum site functions used by NT-1 generalized to Lx (slice sums cumulated in t and
  spread uniformly over the slice's t-links; within-slice remainder by the zero-mean circle cumulative sum). So ∂*k = 𝒜
  exactly, k is gauge invariant exactly (built only from F_p, Wilson lines and gauge-invariant responses), and k is local iff
  the correction Q(·) is small, i.e. iff m_p ≈ 0 and h ≈ 0 — the place where anomaly cancellation enters.
  The ray-averaged current entering the measure: k̄̄[A] = ∫_0^1 dt k[tA] dt = Σ_p F_p ∫_0^1 du (1−u) κ_p[uA] + Q(𝒜̄ − ∂*(…)),
  𝒜̄ = ∫_0^1 𝒜[tA] dt (integrals by composite Simpson on the transport grid, 8 intervals main / 16 check).
- **Effective action:** W[A] = W0[A] + i s_k Σ_l A_l k̄̄_l[A] (eq. (5.8): L = L0 + δ(Σ A·k̄̄)). The sign s_k ∈ {±1} is a
  convention fixed by the Ward test (gate b1-W): the other sign must fail by > 100×.
- **Exact gauge invariance by construction:** ρ(U) := exp W[A_c(U)], with A_c the canonical θ-covariant representative of U's
  gauge orbit: axial gauge A_t ≡ 0 on all t-links (crossing links included); residual t-independent gauge fixed by requiring
  A_x(x,0) + A_x(x,1) = (W_0 + W_1)/Lx for every x (W_t = real Wilson-line angle of slice t). A_c is a linear function of the
  gauge-invariant data (plaquette angles, one Wilson line), so ρ depends only on the gauge orbit to roundoff; θ maps the
  canonical gauge to itself.
- **Integrability:** W is the logarithm of an explicit determinant in an explicit basis plus an explicit function, so the
  measure term is integrable on the chart reached by straight rays (no wrapping of the Wilson-line circle occurs in the
  kernels: all W-matched witness fields have small Wilson lines; checked, max |W_t| reported). Global integrability around the
  Wilson-line circle is NOT tested (named scope limit).

## 5. Gate G-LEG, operational (all items on the RP geometry Lx = 4, Lt = 8 unless stated)
- **(a)** Lx = 4. PASS by construction.
- **(b1) exact gauge invariance:** max |ln ρ(U^Λ) − ln ρ(U)| ≤ 1e-10 (real part and phase mod 2π) on 6 joined configurations,
  Λ random with σ = 0.3 and σ = 2.0 per site, plus a constant shift of the lower half. Exactness checks of the current:
  max |∂*k̄̄ − 𝒜̄| ≤ 1e-12 and max |k̄̄[A + dω] − k̄̄[A]| ≤ 1e-12.
  (b1-W, descriptive, fixes s_k): the un-canonicalized ray measure W[A] vs W[A + dω]: residual must fall with the transport
  level (R(2)→R(4)→R(8)) for 11112; the wrong sign must fail by > 100×.
- **(b2) locality (11112):** response χ(m,y) = |∂k̄̄_m/∂A_y| (central difference, ε = 1e-4) at 2 random admissible
  configurations (plaquettes ≤ 0.55); distance d(m,y) = taxicab distance of link midpoints on the cylinder. Profile
  χ(d) = max over pairs at distance d. PASS if a least-squares fit ln χ(d) = a − ν d over d = 1..d_max gives ν ≥ 0.3 per spacing
  AND χ(d_max) ≤ 1e-2·χ(1). Report ν, the profile, the split into the k_loc part and the finite-volume correction Q-part, and
  the same profile at Lx = 6 or 8 (supplementary, descriptive). Diagnostic: bulk monopole defects m̄ (ray-averaged m_p).
  Note (scope, stated in advance): with Lx = 4 the x-separation is at most 2; the decisive distances are mostly in t.
- **(c) anomalous control (L1, same construction, same configurations):** "visibly fails" if BOTH (i) its bulk monopole defect
  |m̄| ≥ 10× that of 11112, and (ii) its k̄̄ fails the (b2) locality criterion at Lx = 4 or at the supplementary Lx, or its
  χ at the largest same-slice x-separation exceeds 11112's by ≥ 10×. Descriptive: L1 without the Q correction fails the
  Ward identity at a level that does not fall with transport resolution.
- **(d) reflection condition:** c(J) := ln ρ(θJ) − conj ln ρ(J) on ≥ 6 joined configurations (pool pairs, quadrature nodes);
  PASS if the spread of c (real part, and imaginary part mod 2π) ≤ max(1e-6, 10× the transport change R(4)→R(8) of the same
  quantity). If (d) fails, the reading is OPEN ("Θ-covariant measure not built"), never FAIL.
- **Admissibility/consistency gates** (as NT-1): G1 |det M_L||det M_R| = |det D| (≤ 1e-10); G5 min|eig H_W(U^e)| > 0.1 for
  every charge at every evaluated ray point of every kernel node; G6 index 0 along every ray; G7 |Σ_x 𝒜| ≤ 1e-10.
G-LEG passes iff (a), (b1), (b2), (c), (d) and G1, G5–G7 pass.

## 6. RP kernel (only read if G-LEG passes; computed anyway if time allows, labelled accordingly)
- Witnesses: W-matched (boundary Wilson line W(slice 1) = 0 by a holonomy shift), gauge-invariant point-orbit witnesses as K2c
  V2 (referee-accepted construction). Pools on Lx = 4, Lt = 8:
  - **P-A**: W-matched greedy search on the vector-like O (m = 0.05) kernel (K2c wsearch rule: 8 random matched starts; per
    step 4 random + 4 perturbations σ ∈ {0.02, 0.05, 0.1, 0.2}, re-matched, margin 0.55; objective λ_min/λ_max at LOW), seed
    1504, to k = 12;
  - **P-B**: 10 random W-matched configurations, seed 2504, no search.
- Kernels on each pool: chiral 11112 (complex; all ordered pairs, no Hermitian fill), modulus |ρ_χ|, vector O (m = 0.05; the
  K2c power reference), massless vector overlap, Wilson (m = 0.05), pure gauge PG.
- Quadrature: Duffy–Gauss–Legendre on the tetrahedra of the crossing polytope, LOW n = 3, HIGH n = 4 (all entries), third
  level n = 5 on 12 off-diagonal entries + diagonal (q3). Transport check: R(8) on the same subset (q_PT). If the timing
  probe shows this does not fit, fallback (registered now): LOW/HIGH = 2/3, third = 4.
- Error estimate (K2c/NT-1 style): E = k·max(q, q3, q_PT, h) + 1e-13, q = max|Zn(HIGH) − Zn(LOW)|, h = Hermiticity defect
  max|Zn − Zn†| of the directly computed matrix. "Quadrature-converged negative" (= the K2c "certified" rule, wording as the
  K2c referee required): λ_min(Hermitian part of Zn) < −10E. PSD within error: λ_min > −10E.
- Global constant: as NT-1 F3: the Θ constant c from (d) is removed, and the sign is fixed by K(a,a) > 0 (all diagonal
  phases must agree; a mixed sign is reported as an RP violation by itself).
- Phase diagnostics: spread of arg ρ over nodes within entries and over entries; max|Im Zn_chi|; ‖Zn_chi − Zn_mod‖ and the
  two λ_min.

## 7. Reading rule (mechanical)
- CHI-RP-FAIL: G-LEG passes and at least one pool's chiral λ_min < −10E.
- CHI-RP-PASS-at-power: G-LEG passes, every pool's chiral kernel PSD within error, and the vector O kernel is quadrature-
  converged negative on those same pools.
- OPEN otherwise, naming the failed G-LEG item (or "no power" if O is not negative on the pools).
Scope stated in advance: finite 2D U(1), Lx = 4, Lt = 8 (12 if run), open time, antiperiodic x, hard support δ = 0.6,
β_g = 0, M = 1, one explicit local current (counterterm freedom not scanned), chart of straight rays (global integrability
around the Wilson-line circle not tested), link reflection. Not 4D, not non-abelian, not the torus, not infinite volume.

## 8. Budget
Deadline 16:30Z. Order: library + exactness checks → G-LEG (b1, d, C0) → locality (b2, c) → P-A search → chiral kernels.
If G-LEG is not complete by ~15:30Z, the reading is OPEN naming the unfinished item; partial kernels may be reported as
descriptive only.

---
## Dated follow-up F1 (2026-10-15 11:30Z, after `scripts/T0_checks_Lx4_Lt8.out`, `LOC_Lx4_Lt8_11112.out`, `LOC_Lx4_Lt8_L1.out`; readings unchanged)
Seen: code checks pass (builder = lat2d to 0.0; analytic dq/dA = finite differences to 7e-11; decomposition identity 1e-15;
|div kbb − Abar| ≤ 2e-15; kbb gauge invariant to 2e-15; canonical gauge orbit-independent to 1e-15 and θ-covariant to 1e-16).
Registered (b2) for 11112 at Lx = 4: ν = 1.59, ratio 7.8e-6 (passes). Monopole defect m̄: 11112 ≈ 1.5e-3–3.9e-3, L1 ≈ 0.140
((c)(i) satisfied, ratio ≈ 80). But the registered (b2) fit also passes for L1 at Lx = 4 (ν = 1.97), and the registered
"same-slice x-separation" secondary uses x-link→x-link pairs on one slice, where the anomalous Q-response is absent by
construction (an x-link variation is a dipole in t; a t-link variation is a dipole in x whose cumulative lands on x-links of the
same row but is registered under different pairs). Diagnosis: Q's non-locality is only around the x-circle (x-link↔t-link and
t-link↔x-link pairs show a flat response over the whole circle: L1 8.9e-3 at d = 1 and 2), and at Lx = 4 the circle is 2
spacings, so a taxicab fit dominated by t-distances cannot see it. The (b2)/(c) criteria as registered therefore have no
discriminating power in x at Lx = 4. This is a design flaw of my registration, recorded here, not a result.
Added now, BEFORE any supplementary-Lx run (new diagnostic; labelled as registered after seeing Lx = 4 data):
- **x-profile** χ_x(s): max |∂kbb_m/∂A_y| over pairs whose link midpoints differ by |Δt| ≤ 0.5, as a function of the
  x-separation s of the midpoints (s = 0, 0.5, …, Lx/2), all link types. Computed from the saved χ arrays at Lx = 4 and on
  supplementary lattices Lx = 6 and 8 (Lt = 8, same construction, 2 configurations each, seed 301), for 11112 and L1.
- **Finite-volume scaling** (Lüscher Thm 5.4 analogue): bulk m̄ and the Q-part of χ_x at the largest s, against Lx = 4, 6, 8.
- **Criterion (c)-x (added):** the anomalous control visibly fails locality if, at Lx = 8, its χ_x at the largest
  separation s = 4 is ≥ 10× that of 11112, and its χ_x drops by less than 2× from s = 1.5 to s = 4 (plateau).
  **Criterion (b2)-x (added, must also hold for G-LEG to pass):** 11112's χ_x falls by ≥ 10× from s = 0.5 to s = Lx/2 at
  Lx = 8, and its Q-part at the largest s decreases from Lx = 4 to Lx = 8.
If (b2)-x fails, G-LEG (b) fails (locality in x not shown) and the reading is OPEN. If (c)-x fails, G-LEG (c) fails.

---
## Dated follow-up F2 (11:37Z, after the Lx = 6 and 8 locality runs and `XPROF_rows.out`; readings unchanged, nothing re-registered)
Results against the F1 criteria:
- (b2)-x for 11112 at Lx = 8: χ_x falls 4.43e-3 → 1.07e-4 (41×) from s = 0.5 to s = 4, and its Q-part at the largest s falls
  4.93e-4 (Lx = 4) → 2.06e-4 (Lx = 8): **met as registered**.
- (c)-x for L1 at Lx = 8, as registered at s = 4: L1 1.16e-5 vs 11112 1.07e-4: **NOT met as registered.** Diagnosis: at
  Lx = 8 the separation s = 4 is reachable only by same-type pairs (x-link↔x-link on one slice, t-link↔t-link on one row);
  the Q correction's response to a single-link variation lives on mixed pairs and on the neighbouring rows (an x-link
  variation is a dipole in t, a t-link variation a dipole in x whose zero-mean circle cumulative is a sawtooth crossing zero
  at the antipode), so the registered pointer s = 4 cannot see it for any charge set. At s = 3.5 (largest mixed-pair
  separation) L1 = 4.95e-3 vs 11112 = 1.10e-4 (45×), and L1 is flat from s = 1.5 (4.94e-3) to 3.5 (4.95e-3); the L1
  plateau times Lx is constant (0.036, 0.039, 0.040 at Lx = 4, 6, 8: a Wilson-line-type response of fixed total weight);
  L1's monopole defect m̄ = 0.140/0.154/0.158 at Lx = 4/6/8 (→ 1/2π = 0.159), 11112's bulk mean 1.5e-3/1.1e-3–3e-3/3e-4–6e-4.
- I do NOT re-register (c). Mechanical consequence (PREREG §5, F1): G-LEG item (c) is not met as operationalized, so the
  registered reading is **OPEN (G-LEG (c), registration defect)** whatever the kernel shows. The report will state the
  substance separately and give the kernel results as conditional/descriptive.
- Noted for the report (not a criterion): 11112's own Q-part has an x-flat component (≈ 4.6e-4 at Lx = 4, ≈ 1–2e-4 at
  Lx = 8, also in the bulk rows), i.e. its x-locality improves with Lx but not demonstrably exponentially for Lx ≤ 8 at Lt = 8.
Remaining gate items (b1, d, G1, G5–G7, C0) and the kernels proceed as registered.

---
## Dated follow-up F3 (11:40Z, after `scripts/GATES_Lx4_Lt8.out` and `scripts/WARD_Lx4_Lt8.out`; readings unchanged)
- (b1) exact gauge invariance of the canonical measure: 6.8e-14 (PASS). G1 2.1e-14, G5 0.384, G6, G7 7e-15 on the gate fields.
- (d) reflection: c = ln ρ(θU) − conj ln ρ(U) = −7.962629 i, spread 1.4e-13 (PASS).
- C0: charge 5 has min|H_W| = 0.000 (δ = 0.6) and 0.018 (δ = 0.3); charge 4 0.147/0.142 → **11112** (rule of §2).
- (b1-W): the first output (max over three gauge transformations) mixed a transport-limited large transformation (σ = 2.0)
  with the clean ones (ratio 8 < 100). Per-transformation breakdown (WARD_Lx4_Lt8.out): with s_k = −1 the residual converges
  as Ns^-4 for every transformation (shift 0.3: 3.1e-9 → 2.0e-10; σ = 0.3: 3.0e-8 → 1.9e-9; σ = 2.0: 1.0e-3 → 5.1e-5 at
  R(8) → R(16)); with s_k = +1 it stalls at 4.8e-4 / 7.4e-4 / 7.4e-3 (ratios 2.4e6, 3.9e5, 145 at R(16)). **s_k = −1** (same
  as NT-1). Descriptive: 11112 without the Q correction stalls at 6.1e-4 (σ = 0.3); L1 without Q stalls at 1.9e-2 / 0.20;
  L1 with Q converges (the non-local Q "restores" the anomalous model, as expected; the failure is locality, §F2).
- Kernel plan unchanged: Lt = 8 only (one Lt = 8 entry at n = 3 costs 3 s; Lt = 12 would cost ~3.4× and is not run).
  Chunk of 32 nodes per batch (the gate run peaked at 412 MB).

---
## Dated follow-up F4 (11:59Z, while the P-A kernel runs; no kernel number seen; readings unchanged)
Queued after the kernel chain (descriptive only, not gate criteria): (i) `nt1p_indep.py`: same construction with different
numerics (plain transport Ns = 64, finite-difference anomaly derivative, 12-point Gauss-Legendre ray integrals) on 6 P-A
kernel nodes, plus the modulus factorization |ρ| ∝ |det D(1)|²|det D(2)|^½; (ii) locality at Lx = 8, Lt = 12 (1 configuration,
11112 and L1) to see whether 11112's x-flat Q-part (F2) shrinks when the open ends move away (open-end origin) or not.

---
## Dated follow-up F5 (12:29Z; after the P-A kernel result, before any Lt = 12 kernel run; readings unchanged)
Seen: P-A (Lt = 8) chiral λ_min −2.4485e-3, E 5.0e-5 (quadrature-converged negative); O −5.74e-4 (power shown).
Added (time allows): **P-C**, Lt = 12 (T = 6), W-matched O-search (same rule), seed 1512, k = 8; kernel with the same levels
(n = 3/4/5, transport R(4)/R(8)), subset 8 off-diagonal entries. It runs after the queued descriptive runs (F4), only if it
starts before 14:15Z. It counts as an additional pool under §7 (it can only turn a PASS-type outcome into FAIL-type).

---
## Dated follow-up F6 (14:01Z; closing log; readings unchanged)
- Kernels done: P-A (Lt 8, k 12), P-B (Lt 8, k 10), P-C (Lt 12, k 8; the 8 random matched starts, no greedy step since K = 8).
  All three chiral kernels are quadrature-converged negative; O is negative on all three; W and PG PSD (scripts/K_*.out).
- P-C: the watchdog killed the run at 518 MB during the optional massless-vector (vec0) reference, after the chiral, modulus,
  O, W and PG results were printed and the chiral/modulus kernels saved. vec0 for P-C is missing (descriptive only).
- 13:55Z: `dq_dA` in nt1p_lib.py was re-written to loop over link chunks (memory only), after all kernels had run, for the
  descriptive Lx = 8, Lt = 12 locality run (which had been killed at the cap). Re-verified identical: T0 checks unchanged and
  the Lx = 4 locality profiles identical to every printed digit (`T0_checks_Lx4_Lt8_after_refactor.out`,
  `LOC_Lx4_Lt8_11112_after_refactor.out`).
- Descriptive Lx = 8, Lt = 12: L1 plateau 4.96e-3 (same as Lt = 8); 11112 (seed 301) hit an index change on the charge-2 ray
  (G6) and was not used; seed 302: Q-part x-flat 0.7–1.5e-4 (Lt = 8: 1–2.7e-4).
