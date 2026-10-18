# NT-1″ pre-registration: completing the chiral measure (route 1; NT-1′'s open item G-LEG (b))

Written 2026-10-15, started 14:38Z (`date -u`), BEFORE any NT-1″ script exists or runs.
Agent: Claude Opus 5.5 (xhigh), test agent NT-1″. Same model family as NT-1′, K2/K2c and the supervisor: NOT independent.
Parent: TESTS.md "Campaign wave 2c", item NT-1″ (exercise branch `origin/claude/chirality-grid-exercise-20261014`).
Referee checklist: `campaign/NT1P/referee/REFEREE.md` §1 (codex, CONFIRMED WITH CORRECTIONS; OPEN at G-LEG (b)).
Code base: NT-1′'s `scripts/` copied into `NT1PP/scripts/` unchanged (`nt1p_lib.py` sha1 3ce22737…, identical to the NT1P
copy; `lat2d.py` 5f1de922…). New scripts are `nt1pp_*.py`. Every run goes through `scripts/capped.sh` (0.5 GB cap, OMP 2
threads), one process at a time. Deadline 19:00Z.

## 0. FIXED readings (TESTS.md wave 2c, NT-1″; restated, not edited)
- Readings CHI-RP-FAIL / CHI-RP-PASS-at-power / OPEN are NT-1′'s, unchanged. G-LEG (b) is made concrete by two items; both must pass.
- **(b′) finite-volume part.** Either (1) replace it by an explicit Wilson-line measure term of Kadoh–Kikukawa type
  (arXiv:0709.3656) and demonstrate its locality bound numerically; or (2) show that the anomaly-free x-flat tail falls
  exponentially with Lx: at least 3 sizes among Lx = 4, 6, 8, 10, a fitted rate > 0 at ≥ 3σ, and the L1 plateau ∝ 1/Lx as a contrast.
- **(b″) integrability around the Wilson-line circle.** Transport the measure around closed loops in Wilson-line space, including at
  least one non-contractible loop. The accumulated phase must be trivial (a multiple of 2π) to stated precision for 11112, and the
  anomalous control should fail.
- **CHI-RP-FAIL:** (b′) and (b″) pass, NT-1′'s (a), (c), (d) hold, and at least one NT-1′ pool recomputed with the completed measure
  stays below −10E. **CHI-RP-PASS-at-power:** gate passes and the kernel is PSD within error. **OPEN:** otherwise, naming the failed item.

## 1. Prior art (step 0) and literature
- `git grep -i -E "kadoh|kikukawa|toron|wilson.line measure|measure term" origin/main -- docs scripts`: no chiral-measure
  construction on main (toron hits are pure-gauge notes, e.g. `docs/COMPACT_U1_WILSON_TO_SOURCE_FREE_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-02.md:266`).
  `chern insulator|qi-wu-zhang|edge zero mode`: no hit on main.
- Packet prior art used: NT-1′ (measure, code, gates, kernels; REPORT/PREREG/referee); K2 `kills/K2/KILL_REPORT.md:55`
  (open time + periodic x: exact H_W zero modes at the time edges, "the Chern edge states of the 2D Wilson operator") and its
  referee `kills/K2/REFEREE_VERDICT.md:37` (free zero modes invalidate a uniform-gap argument); NT-1′ PREREG:49 (antiperiodic x
  chosen to avoid them; gap 0.707 at Lx = 4).
- Lüscher hep-lat/9811032 (text extraction from NT-1′'s download, read only): Thm 5.1 (reconstruction from a current with
  (a)–(d)); eq. (5.8) (infinite-volume straight-ray measure term); Thm 5.4 (finite volume: |j − j⋆| ≤ κ L^ν e^{−L/ϱ},
  uniformly in the field); §7 (torus, field space with Wilson-line circles); §8 eq. (8.9) and Lemma 8.1 (the Wilson line of a
  closed curve; the Berry holonomy as a projector product); §10.1 (bundle triviality = vanishing magnetic-flux quantum numbers);
  §10.3–10.4 (gauge loops and the non-gauge loops (10.10), which wind a Wilson line by 2π). **All of this is on the periodic torus**,
  where admissibility (small plaquettes) guarantees a uniform H_W gap.
- Kadoh–Kikukawa arXiv:0709.3656 (abstract only): closed finite-volume formula; Wilson lines treated separately for global
  integrability; local counterterm from the cohomologically trivial part of the anomaly. Finite periodic lattice assumed (not
  confirmed from the abstract). I do not reproduce its formula.

## 2. Analytic facts stated before running (my derivations; labels as given)
- **A1 (proved, free field).** On the open-time strip (t = −T+1..T), x-ring of Lx sites, fermion antiperiodic in x, M = 1, r = 1, a
  uniform field with zero plaquettes and Wilson line W is diagonal in the twisted momentum k′ = (π(2n+1) + eW)/Lx. At k′ = 0,
  (D − 1)ψ = −½(1 − γ_t)ψ(t+1) − ½(1 + γ_t)ψ(t−1), so ψ = δ_{t,T}χ with γ_t χ = χ and ψ = δ_{t,−T+1}χ with γ_t χ = −χ are
  exact zero modes of H_W = γ5(D − 1) for every Lt. k′ = 0 occurs iff eW ≡ π (mod 2π). Hence at zero plaquettes the winding
  W: 0 → 2π passes through exact H_W zero modes: at W = π for charge 1, at W = π/2 and 3π/2 for charge 2.
- **A2 (proved at first order in k′, free field).** The two edge modes have energies ≈ ∓ sin k′ (top/bottom), so at W = 0 the
  edge gap is sin(π/Lx): 0.707, 0.500, 0.383, 0.309 at Lx = 4, 6, 8, 10. It closes as Lx grows. H_W(k) = (sin k_t, −sin k_x,
  1 − cos k_x − cos k_t)·σ is the Qi–Wu–Zhang Chern insulator (bulk |d|² = 1 + 2(1 − cos k_x)(1 − cos k_t) ≥ 1); these are its chiral edge states.
- **Hypotheses to test (suggested, not assumed):** H1, the non-contractible Wilson-line loop is not admissible on the RP geometry
  for any admissible plaquette background (spectral flow of the edge states); H2, the anomaly-free x-flat tail contains an
  edge-sourced component that is not exponentially small in Lx.
- **Consequence I commit to in advance.** If H1 holds, the fixed (b″) wording cannot be met on the RP geometry: there is no
  admissible non-contractible Wilson-line loop to transport around. I will then read (b″) as **NOT MET as worded** and the campaign
  reading as **OPEN at (b″)**. I will state the substance separately: the admissible index-0 field space is then fibre-wise an
  interval in W, so global integrability reduces to local integrability of the explicit straight-ray frame. Whether that vacuity
  closes (b″) in substance is for the referee/supervisor, not for me.

## 3. Geometry and code (fixed)
NT-1′'s: 2D U(1), Strip(Lx, T = 4) (Lt = 8) unless stated, fermions antiperiodic in x, Wilson r = 1, M = 1, canonical
θ-covariant representative, measure W = W0 + i s_k Σ A_c·k̄̄ with s_k = −1, k̄̄ = k_loc + Q(Ā − ∂*k_loc), transport Ns = 8 (Richardson).
G5 (min|eig H_W(U^e)| > 0.1 along the ray, both charges) and G6 (index 0) as NT-1′.

## 4. (b″) operational
**B2a, admissibility of the non-contractible loop (primary).**
- Loop: A(τ) = A_c + τ·(2π/Lx)·1_x (every x-link), τ ∈ [0, 1]. U(1) is gauge-equivalent to U(0) by the large transformation
  e^{i2πx/Lx}; in gauge-invariant data the loop is W → W + 2π at fixed plaquettes (Lüscher's non-gauge loop (10.10)).
- Backgrounds: (i) A = 0; (ii) 10 random admissible configurations per Lx from NT-1′'s generator (`rand_half` σ = 0.25,
  margin 0.55, both halves; crossing angles N(0, 0.25)), canonical rep, seed 4401; (iii) at Lx = 4, 6 kernel nodes of pool P-B
  (pairs (0,1), (2,5), (7,9), 2 Duffy n = 3 nodes each, rng seed 7, as `nt1p_ward.py`). Lx = 4 is primary; Lx = 6, 8 descriptive.
- On a 2000-step τ grid plus golden-section refinement of the minimum: for e = 1, 2, min_τ min|eig H_W(eA(τ))| and whether
  the count of positive eigenvalues ever differs from N/2. Also the set of τ where both charges have gap ≥ 0.1 and index 0
  (number of intervals and total length).
- **Loop admissible** iff both charges keep gap ≥ 0.1 and index 0 for every τ.
- **Predicted (A1):** background (i) has exact zeros at τ = 1/2 (e = 1) and τ = 1/4, 3/4 (e = 2).
- **If no sampled loop at Lx = 4 is admissible:** (b″) NOT MET as worded (no admissible non-contractible loop on the RP geometry). Then:
  - B2b is not run on the RP geometry;
  - the classification is "genuine obstruction of the open-time geometry (H_W edge states), not a defect of the measure";
  - the L1 control cannot fail (b″) on this geometry either (same loop, same obstruction), so no (b″) contrast exists here.
- **B2b, transport (only if some admissible loop exists at Lx = 4):** Δ = W[A_c + 2π/Lx·1_x] − W[A_c] from the un-canonicalized
  ray measure at Ns = 8 and 16; pass if |Im Δ mod 2π| ≤ 1e-6 and ≤ 10× its Ns change for 11112. L1 is reported.

**B2c, the same question where the loop exists (descriptive; a different geometry, not a gate item).**
- Geometry: periodic 4×4 torus, fermions antiperiodic in both directions, zero plaquettes, uniform torons (w_x, w_t) ∈ [0, 2π)²
  (charge e sees e·w).
- Fukui–Hatsugai–Suzuki lattice Chern number of the L (positive-H_W) and R (negative) Weyl bundles over the toron torus, for
  e = 1, 2, on a 24×24 grid (and 32×32 as a check). Also the min gap over the grid.
- C(11112) = 4C_L(1) + C_R(2); C(L1) = C_L(1). Expected: C_L(e) = ±e², C(11112) = 0, C(L1) = ±1.
- This is Lüscher §10.1's flux-number condition for a global measure. It is a statement about the Weyl bundle, not about NT-1′'s
  measure term. It is the (b″) contrast where non-contractible Wilson-line loops are admissible.

## 5. (b′) operational (route 2: does the anomaly-free x-flat tail fall exponentially with Lx?)
**E1, the fixed minimal test.** It uses NT-1′'s statistic on an ensemble.
- Lx ∈ {4, 6, 8, 10}, Lt = 8.
- **Configurations:** NT-1′'s generator as in B2a, then a uniform holonomy shift of all x-links setting the central Wilson line
  (W_0 + W_1)/2 to 0 (to keep the edge Wilson lines away from the A1 crossings).
  - Accept only if G5 and G6 hold on the base ray for both charges; redraw up to 40 times and record the rejections.
  - n_c = 6 accepted configurations per Lx; seed 4600 + Lx.
- **Response:** central-difference ε = 1e-4 response of k̄̄, k_loc and kQ to y ∈ {x-link (0, t = 0), x-link (0, t = 1),
  t-link (0, t = 0)}.
- **Statistic, per configuration:** τ_c = max over y and over pairs (m, y) with |Δt_mid| ≤ 0.5 and x-separation exactly
  s* = Lx/2 − 0.5 (mixed pairs, NT-1′'s "largest mixed separation") of |∂kQ_m/∂A_y|. Also reported:
  - the same-type value at s = Lx/2;
  - the total k̄̄ at s*;
  - the transported charge Lx·τ_c.
- **Per Lx:** mean τ̄, standard error SE (std/√n_c) and maximum.
- **Fit:** ln τ̄ = a − ν·Lx by weighted least squares (σ_ln = SE/τ̄). σ_ν is the larger of the unscaled covariance and the
  √(χ²/dof)-scaled one.
- **L1 contrast:** same configurations, charge 1 only (G5/G6 for charge 1). Its plateau P̄_L1 is the same τ statistic.
- **(b′)-fixed items met** iff all three hold:
  - ≥ 3 sizes have ≥ 4 accepted configurations;
  - ν > 0 with ν/σ_ν ≥ 3;
  - Lx·P̄_L1 is constant within ±20% across those sizes (∝ 1/Lx), with P̄_L1/τ̄ ≥ 10 at each size.

**E2, discriminating exponential from algebraic decay.** It is deterministic: no ensemble noise. **My operationalization of "falls
exponentially", which I register as part of (b′).**
- Background: zero plaquettes and a uniform Wilson line, A_x = W0/Lx on every x-link, A_t = 0, with W0 ∈ {0.3, 0.6}.
- Sizes: Lx ∈ {4, 6, 8, 10, 12, 14, 16} at Lt = 8 (primary). Lt = 12 for Lx ≤ 12 is descriptive (it shows whether the effect
  tracks the open ends).
- **Measured on the base ray:**
  - J_Q = max |kQ| over bulk t-links. This is the x-flat current Q carries through the bulk, equal to the anomaly charge it
    transports across the slices;
  - the row profile of Ā(t);
  - max |m̄| and max |h̄| in the edge rows and in the central rows.
- **Measured by finite differences:** τ_E2, the E1 statistic for y ∈ {x-link (0, 0), t-link (0, 0)}.
- **L1** is computed alongside.
- **Classification.** For each quantity and each W0, local rates ν_L = ½ ln(q(L)/q(L+2)) for L = 4..14.
  - **E2-ALG (algebraic):** for both W0, ν_14 < ½ max_L ν_L, and a power-law fit ln q = a − p ln L over L ≥ 8 has a smaller
    residual than ln q = a − νL over the same points. An exponential with a power prefactor has local rates that rise or level
    off with L. A power law has rates falling like p/L.
  - **E2-EXP:** for both W0, ν_L over L ≥ 8 stays ≥ ½ of its maximum, or q drops below 1e-12 (roundoff).
  - Otherwise **E2-UNDECIDED**.
  - The decisive quantity is τ_E2. J_Q is reported alongside.
- **(b′) MET** iff the E1 fixed items are met AND E2 is not E2-ALG for τ_E2.
  - **If the E1 items are met but E2-ALG holds,** (b′) is NOT MET: "the fixed minimal items pass, but the decay is algebraic,
    so Lüscher's exponential bound is not shown". I will report the E1 items alone too, so the referee can apply the parent wording.
- **Source location (descriptive).** The rows where Ā and the transported charge sit; whether J_Q tracks the edge rows.
- If τ_E2 is identically zero by symmetry (|τ| < 1e-13 at every L), E2 is uninformative and (b′) rests on E1 alone, so stated.

(b′) route (1), an explicit Kadoh–Kikukawa Wilson-line term, is not attempted: KK's formula has not been read beyond the
abstract, and it is a torus construction. If E2 shows algebraic, edge-sourced Wilson-line dependence, any Wilson-line term on
this geometry inherits it.

## 6. Kernel step and reading rule (mechanical)
- **Kernel step.** Only if (b′) and (b″) both pass, rerun `nt1p_kernel.py` on pool P-B (Lt 8, random, k = 10), with the same
  levels as NT-1′. The completed measure under route (2) is NT-1′'s measure. The kernel reads FAIL-type if λ_min < −10E.
- **CHI-RP-FAIL / PASS / OPEN** exactly as fixed (§0). NT-1′'s (a), (c), (d) are taken as referee-confirmed (REFEREE.md §5).
- **Classification of a failed item:**
  - **(b″) failing by inadmissibility** is a genuine obstruction of the open-time RP geometry: the H_W edge zero modes of A1.
    No change of measure term removes it; a change of geometry (a torus, or other time boundaries) would.
  - **(b′) failing with E2-ALG and edge-row-sourced transported charge** is a genuine obstruction of the same geometry: chiral
    edge states with gap ∝ 1/Lx.
  - **(b′) failing with bulk-sourced non-exponential decay** is a construction-defect candidate: the cohomology current or Q.
- **Scope.**
  - Stated next to every headline: finite 2D U(1), open time, antiperiodic x, M = 1, 11112 / L1.
  - Sizes: Lx ≤ 16; Lt = 8 (12 descriptive).
  - Only the one explicit current of NT-1′, with no counterterm scan.
  - Not the torus measure (B2c is a bundle statement only), not 4D, not non-abelian, not infinite volume.

## 7. Budget and order
1. T0: library unchanged, Lx = 16 timing and memory probe (no physics numbers read).
2. B2a.
3. E2 (Lt 8).
4. E1.
5. B2c.
6. E2 at Lt 12 (descriptive).
7. Report by ~18:40Z.

Memory estimate at Lx = 16, Lt = 8 (N = 256): `dq_dA`'s Φ array is 256 × 128² complex ≈ 67 MB per configuration, and the
Poincaré path tensors are about 30 MB each. Runs use one configuration per batch at N ≥ 192, so the expected peak is about 250 MB.
If time runs out, the reading is OPEN, naming the unfinished item.

---
## Dated follow-up F1 (2026-10-15 14:46Z; after B2A_Lx{4,6,8}.out and E2 Lt 8 (E2_ANALYSIS_Lt8.out); readings and decisive quantities unchanged)
Seen so far:
- **B2a.** 0 of 17 (Lx 4), 0 of 11 (Lx 6), 0 of 11 (Lx 8) winding loops are admissible.
  - At F = 0 the zeros sit exactly where A1 says: τ = 1/2 for e = 1, and τ = 1/4, 3/4 for e = 2, with gap ≤ 6e-16.
  - With plaquettes, each zero sits where an edge Wilson line e·W_edge ≡ π, gap ≤ 2e-12, and the index changes between the two edge crossings.
  - Per §2/§4: **(b″) NOT MET as worded**; B2b is not run.
- **E2 at Lt 8.** τ_E2 (decisive) is E2-EXP for both W0: local rates 0.83 → 0.77, and Lx·τ has rate → 0.70 ≈ ln 2. J_Q and the central-row |m̄| are also E2-EXP.
  - The edge-row quantities (Ā edge row, |h̄| edge, the edge-row Q t-current, edge |m̄|) are classified E2-ALG by the same rule: local rates 0.87 → 0.38, power fit p ≈ 6.3, much better than the exponential.
  - These were registered as descriptive ("source location").
Added now, before running them (descriptive only, not gate criteria):
- **E2-edge.** τ_edge is the E2 statistic with y moved to the bottom edge: the x-link (0, t = −T+1) and the t-link (0, t = −T+1).
  - F = 0, W0 = 0.3, Lx 4..16, Lt 8; classified by the same E2 rule.
  - It tests whether the measure current's response near the time boundary keeps a uniform exponential bound in Lx.
  - If it is E2-ALG, I will report that Lüscher's uniform (position-independent) bound is not established near the open time
    boundaries, as a scope limit on any (b′) pass. It does not change the mechanical (b′) rule of §5.
- **E2 at Lt 12** for Lx ≤ 10 (as registered; Lx 12 skipped for memory).
Next: E1 (fixed minimal items), then B2c, E2-edge, E2 Lt 12.

---
## Dated follow-up F2 (2026-10-15 14:52Z; after E1 (E1_FIT.out), B2c, E2-edge Lt 8 and E2 Lt 12; readings and decisive quantities unchanged)
Seen:
- **E1.** ν = 0.869 ± 0.064 (13.5σ) on Lx 4–10, and 0.746 ± 0.104 (7.2σ) on 6–10. L1's Lx·plateau is 0.035–0.040.
  - The fixed-wording items are met.
  - My extra registered sub-condition (L1/11112 ≥ 10 at each size) misses at Lx = 4 (9.8×). It holds at 6, 8, 10.
- **B2c.** C_L(1) = −1, C_L(2) = −4, C(11112) = 0, C(L1) = −1. The w_x-loop holonomy has winding 0 (11112) and 1 (L1).
- **E2-edge (W0 = 0.3, Lt 8).** Local rates are 0.89, 0.79, 0.66, 0.52, 0.40, 0.33 (Lx 4→16). This is the E2-ALG pattern
  (power fit p ≈ 5.5, residual 14× smaller than the exponential fit).
- **E2 at Lt 12.** The central and edge quantities equal their Lt 8 values to 3–4 digits for Lx ≤ 10.

Added now, before running it (descriptive only, not a gate item):
- **Larger sizes.** Extend the deterministic E2 and E2-edge (W0 = 0.3, Lt 8) to Lx = 18, 20, 22, 24, using a memory-lean
  `dq_dA` (`nt1pp_lean.py`).
  - It has the same formula. It is checked equal to `nt1p_lib.dq_dA` to 2.3e-16 (`LEAN_CHECK.out`).
  - Lx 16 is rerun with it as a reproduction check.
- **Purpose.** To see whether the edge local rate keeps falling (rate × Lx roughly constant, i.e. algebraic) or levels off
  (exponential with a smaller rate). The same holds for whether the central τ stays exponential.
- **Pre-stated reading of the outcome.**
  - If the edge local rate at 22→24 is below 0.25 and rate × Lx_mid stays within a factor 1.5 of its Lx 8–16 values, I
    report the near-edge finite-volume dependence as **algebraic (checked to Lx 24, Lt 8, F = 0 backgrounds)**.
  - If it levels off at ≥ 0.3, I report it as exponential with a smaller edge rate.
  - Otherwise, undecided.

---
## Dated follow-up F3 (2026-10-15 14:57Z; after the Lx 16–24 runs; readings unchanged)
Seen (W0 = 0.3, Lt 8):
- **Lx 16 reproduced** by the lean code to every printed digit.
- **Edge-y τ.** 1.70e-7, 9.52e-8, 5.64e-8, 3.50e-8, 2.26e-8 at Lx 16–24. Local rates 0.290, 0.262, 0.238, 0.218, and rate × Lx_mid = 4.93, 4.97, 5.00, 5.02.
  - **Per the F2 rule this is algebraic**, ∝ Lx^−5 (checked to Lx 24).
  - The edge |h̄| behaves the same way.
- **Central τ.** Local rates 0.760, 0.751, 0.747, then 0.688 at 22→24.
  - J_Q (the net charge carried through the bulk) stays at 0.75–0.74.
Added now, before running them (descriptive only):
- **(i) E2-edge at W0 = 0.6**, Lx 4–24, to check that the power does not depend on W0.
- **(ii) B2c at L = 6, 8, 10** (L×L torus, grid 16).
  - It measures the spread over w_t of the 11112 Berry phase around the non-contractible w_x loop. This is the toron dependence a
    torus measure term must absorb.
  - Expectation (suggested): it decays exponentially in L, because the torus has no edges. That would contrast with the strip's
    algebraic edge term.

---
## Dated follow-up F4 (2026-10-15 15:00Z; after F3's runs; readings unchanged)
Seen:
- **E2-edge at W0 = 0.6.** Same local rates as 0.3 (16→18: 0.290). G5 fails (gmin < 0.1) at Lx ≥ 20 for W0 = 0.6, so only Lx ≤ 18 is used there.
- **B2c, torus.** The 11112 w_x-loop phase spread over w_t is 1.46, 0.36, 0.090, 0.023 rad at L = 4, 6, 8, 10.
  - That is exponential, rate ½ln 4 ≈ ln 2 per spacing.
  - C(11112) = 0 and C(L1) = −1 at every L.
Added now (descriptive only): **does the edge's algebraic piece reach the bulk?**
- The E2 statistic for y at rows t = −2 and t = −1 (1 and 2 rows in from the bottom edge slice t = −3), with x-link and t-link at x = 0.
- W0 = 0.3, Lt 8, Lx 12–24 (lean code).
- **Reading.** If, at fixed row, the local rate falls toward the edge-y value as Lx grows, the algebraic piece reaches the
  interior, suppressed by the distance to the edge. I then state that, at fixed Lt, the interior tail turns algebraic
  asymptotically (checked for these rows).

---
## Dated follow-up F5 (2026-10-15 15:05Z; closing log; readings unchanged)
- **Rows −2 and −1.** Row −2 (one row in) turns algebraic by Lx ≈ 20; its rate × Lx goes 7.4 → 5.5. Row −1 stays exponential to Lx 24 (0.77 → 0.74).
  - The algebraic piece is confined to the outer two slices at Lx ≤ 24.
  - The central 22→24 rate (0.688) is within reach of the finite-difference floor (same-type values about 2e-12, against τ = 5e-11).
- **A1 strengthened to every background (proved; see report).** At row T the operator (D − 1) restricted to a single-row
  mode with γ_tχ = χ is the ring operator 1 − cos k′ + iγ_x sin k′. The hop into row T−1 is killed by (1 − γ_t)χ = 0. So an exact
  zero mode exists iff e·W_top ≡ π (mod 2π), for any plaquettes; the bottom edge is the same with γ_tχ = −χ.
  - B2a's crossings sit exactly at e·W_edge ≡ π (e.g. rand0: 0.887 + 2π·0.359 = 3.143).
- **Mechanical reading per §6:** **OPEN, failed item (b″)** (not met as worded: no admissible non-contractible Wilson-line loop on the RP geometry).
  - (b′) on the registered statistic: the fixed-wording items are met; my extra ratio sub-condition misses at Lx = 4.
    Near the edges the dependence is algebraic (descriptive).
  - The kernel step is not run.
