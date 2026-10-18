# K2c: K2b's searches under X3's hard admissibility measure (exercise step 8)

**Agent and provenance.** Claude Opus 5.5, test agent K2c, run 2026-10-14 from 17:31Z to 18:35Z (`date -u`). Same model family as K2, K2b, X3, the supervisor and the route agents; nothing here is independent or refereed. No repository was edited. Code: K2's `lat2d.py` and K2b's `k2b_lib.py`, copied unchanged (sha1 checked equal), plus my own `k2c_lib.py` and test scripts. All runs used OMP_NUM_THREADS=2, one at a time; the largest peak RSS was 234 MB.

**Read first.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (233 lines; cited AX).
- In full: `kills/K2/KILL_REPORT.md`, `kills/K2/PREREG.md`, `ref_K2/REFEREE_VERDICT.md`, `ref_K2/REFEREE_CHECKS.md`, `kills/K2b/K2b_REPORT.md`, `kills/K2b/PREREG.md`, `combos/X3/COMBO_REPORT.md`.
- `combos/X3/PREREG.md` lines 190-262, which define X3's admissible-set measure (T-X3f/f').
- Scripts: K2's `lat2d.py`, `k2t3_gi_rp.py`, `k2t3_verify.py`; K2b's `k2b_lib.py`, `k2b_t1_search.py`, `k2b_t2_dwf.py`, `k2b_v3_dwf_Ls.py`.
- The referee wrote no separate hard-indicator script. It ran K2's own `k2t3_gi_rp.py ... hard` (`REFEREE_CHECKS.md:34-47`), and I use the same `weight='hard'` path of K2's `nodes`.

**Labels.** proved (my argument, unrefereed) / checked (a script run here) / suggested / reading.

**Paths.** `K2c/` = `scratchpad/chirality_ex/kills/K2c/`. Scripts and outputs are in `K2c/scripts/`, and each `.out` ends with its peak RSS.

**Pre-registration.** `K2c/PREREG.md`. The main tests (K2c-A, B, C and PG-odd) were written at 17:38Z, before any test ran. Follow-ups V1 to V7 were each registered after seeing earlier results and before their own runs. No reading was edited. Two header timestamps that I typed ahead of the clock are corrected by appended notes.

---

## 0. Plain-words summary

**1. The hard indicator is reflection-positive for pure gauge in this proxy, but not in general.**
- Lx = 2 crossing plaquettes (this proxy, open time and torus): yes. Proved by the character expansion: the coefficients are c_n² ≥ 0. Checked: the pure-gauge kernel is PSD on every pool.
- Odd Lx: no. Proved, and checked exactly at Lx = 3 (relative eigenvalue −9e-3, error bound 2e-12).
- 3D or 4D slices: not RP either (suggested). Some closed-current coefficients are negative, e.g. c₆c₃⁶ < 0.
- With charged fermions the hard measure is not guaranteed RP even for Wilson fermions (K2's Amendment A1). In fixed-Wilson-line sectors of this proxy, though, Wilson + hard is RP: proved on the open lattice, suggested on the torus by the same argument, and checked on both.

**2. K2b's searches rerun with the hard measure, as registered: no violation.**
- Open time (Lt = 12 and 20) and torus (Lt = 12 and 16), both objectives, 8 runs: every hard pool is PSD.
  - The Wilson-referenced objective stays at +0.43 to +0.94.
  - The in-run Fejér reference (same code, same configuration generator) is certified negative in 3 of 3 runs (objective −1.13 to −1.73).
- So the registered reading for these runs is PASS-at-power.
- Why (checked): on every hard pool the overlap, Wilson and pure-gauge kernels have nearly the same smallest eigenvalue. The pure-gauge factor dominates.
  - For the hard indicator that factor is the triangle (2δ − |W_b − W_a|)₊ in the boundary Wilson lines W. It has a cusp at W_a = W_b, so it puts a large positive floor between any two configurations whose Wilson lines differ.
  - The Fejér pure-gauge factor is smooth there; its smallest eigenvalue is about 1e-9 on the same kind of pools.

**3. With the cusp removed, the hard measure fails on both open and torus lattices.**
- Method: every configuration is shifted to the same boundary Wilson line ("W-matched" pools; follow-up V2). These are legitimate gauge-invariant test functions.
- Open time:
  - certified negative in 4 of 4 runs (Lt = 12 and 20), λ_min −1.1e-3 to −2.6e-3 (−5e-5 to −1.3e-4 of the largest eigenvalue);
  - error estimate ≤ 5e-13 (sign margin about 1e9);
  - random W-matched sets are already negative before any search (6 of 6);
  - the violation persists when the Wilson lines are spread by up to ±0.1.
- Torus (antiperiodic time):
  - Lt = 12: certified negative, λ_min −1.47e-4 (−6.3e-6 of max), error estimate 5.5e-11;
  - Lt = 16: certified negative, λ_min −7.3e-5 (−5.1e-6 of max), error estimate 3.2e-13.
- Controls on every W-matched pool: Wilson + hard is PSD (proved for open time, checked everywhere), and the pure-gauge kernel is PSD.
- Independent code reproduces both values to all printed digits: an explicit-link builder for the open lattice (V5) and for the torus (V6).
- **Reading: FAIL, X3's hard admissibility measure is not RP for the gauged overlap in this proxy, on the torus included.** The referee's hard-indicator positivity (+1.3e-3 on K2's set) is a property of configuration sets with spread-out Wilson lines, not of the measure.

**4. Pauli–Villars-subtracted domain-wall fermions also fail under the hard measure.**
- On the W-matched open pools, DWF is certified negative at both L_s = 4 (−2.6e-5, −1.1e-5) and L_s = 8 (−1.6e-5, −1.4e-5).
- On the W-matched torus pool it is certified negative too (−5.1e-6, −8.2e-6; error ≤ 3e-11).
- The Shamir overlap also fails on all three pools.
- The bare 5D determinant (no PV fields) is PSD on all three pools (torus: V7).
- On K2b's Fejér-searched pools the hard measure shows nothing, again because of the cusp.

**5. Consequence (reading).**
- K2's L3g failure now covers X3's exact measure and the antiperiodic torus, which was the escape left open by K2, K2b and the referee.
- The set-B package's real-time branch needs Π-W for matter, or 5D fermions without PV (F2-R's finite-n price). This is the X3 contingency row.
- Scope: 2D U(1), Lx = 2, vector-like Dirac overlap, β_g = 0, gauge-only observables. The chiral measure and 4D were not tested. Other-vendor referee owed.

---

## 1. Verdicts

| Item | Verdict | Reason (label) |
|---|---|---|
| Hard measure, pure gauge, this proxy (Lx = 2) | **RP** | proved (c_n² ≥ 0; torus by Schur), checked (PG PSD on all pools) |
| Hard measure, pure gauge, odd Lx | **not RP** | proved (Bochner), checked exactly (V1: Lx = 3, λ_min −3.99e-3, min/max −8.9e-3, tail bound 2.1e-12) |
| Hard measure, pure gauge, ≥ 3D slices | **not RP (suggested)** | a negative closed-current coefficient c₆c₃⁶c₀^rest; not tested |
| K2c-A/B as registered (K2b's searches, hard) | **PASS-at-power on the explored pools** (open and torus) | all 8 hard pools PSD; in-run Fejér reference certified negative 3/3 (checked). Superseded by V2 |
| **K2c-V2: hard measure, W-matched, open time** | **FAIL_open-overlap** | 4/4 certified negative; Wilson + hard and PG PSD; independent code exact (V5) (checked) |
| **K2c-V2: hard measure, W-matched, torus Lt = 12 and 16** | **FAIL_torus-overlap** | Lt 12: −1.47e-4, E 5.5e-11, independent torus code exact (V6). Lt 16: −7.27e-5, E 3.2e-13. Wilson + hard and PG PSD on both (checked) |
| **Overall: X3's hard measure, 2D U(1) proxy** | **FAIL** (open and torus) | as registered in V2 ("counts as FAIL_G for the overall verdict") |
| K2c-C: PV-subtracted DWF under the hard measure | **FAIL at L_s = 4 and 8** (open and torus) | certified negative on both W-matched open pools and on the W-matched torus pool; bare D5 PSD on all three (checked) |
| Referee's correction "hard-indicator matrices are positive" | **true for K2's sets; does not extend to the measure** | cusp masking (checked; §3.3, V5b) |

---

## 2. Is the hard-measure kernel RP for pure gauge?

Items (a)-(c) were stated in PREREG before any test. Item (d) was sharpened after the K2c-A results, before V2 ran.

**Setting.** One crossing plane with Lx crossing plaquettes, β_g = 0, hard indicator f = 1(|θ| < δ) on each crossing plaquette. Its expansion is f = Σ c_n e^{inθ} with c_n = sin(nδ)/(nπ). At δ = 0.6, c_n < 0 for n = 6..10, 16..20, ...

**(a) Pure gauge, Lx even (this proxy, Lx = 2): RP.**
- Proved (X3's character expansion, re-derived). Integrating the crossing links gives K_PG(a, b) = Σ_n c_n^{Lx} e^{in(W_b − W_a)}, with c_n^{Lx} ≥ 0.
- For Lx = 2 this is (2δ − |W_b − W_a|)₊, which is exactly the code's weight sum.
- On the torus the kernel is the product of the two planes' kernels, so it is PSD by Schur's product theorem.
- Checked: PG is PSD on every pool (§3).

**(b) Pure gauge, Lx odd: not RP.**
- Proved: c_n^{Lx} < 0 for n = 6..10, and W ranges over the whole circle, so by Bochner the kernel is not positive-type.
- Checked by `pg_odd_exact.out` (V1), using the exact aliasing identity λ_j = N Σ_{n≡j mod N} c_n^{Lx} on N = 64 equally spaced Wilson lines:

| Lx | λ_min | min/max | Tail bound | Reading |
|---|---|---|---|---|
| 2 | +3.23e-3 | — | — | PSD |
| 3 | −3.99e-3 | −8.9e-3 | 2.1e-12 | negative modes j = 6..10, 16..20, ... |
| 4 | +2.8e-8 | — | — | PSD |

- Honesty note: the registered grid method (`pg_odd.out`) failed its own certification criterion, because a sampled box converges only as O(1/M). V1 replaced it with the exact formula. Lx = 1, not registered and descriptive only, is −0.22 relative.

**(c) Higher-dimensional slices: suggested, not tested.**
- The gauge projection keeps closed currents. The current 3∂P₁ − 3∂P₂ on two adjacent plaquettes has coefficient c₆c₃⁶c₀^rest < 0.
- Whether this gives a negative eigenvalue depends on the support of the slice plaquettes. So: suggested.
- If true, the hard plaquette bound (X3 price P-X3d) is non-RP in 4D even without matter.

**(d) With charged fermions.** Not guaranteed RP, even for Wilson (K2 A1). Sharper, for this proxy (proved, mine, elementary):
- The Wilson r = 1 determinant depends on the one free crossing link only through charges q ∈ {−1, 0, +1}. The forward and backward hops are rank one, so this follows from the matrix determinant lemma.
- In a W-matched sector (W_a = W_b, so Φ = 0) the hard weight is a single box in that link, and only c₀ and c_{±1}, both > 0, enter.
- Then Wilson + hard equals a positive multiple of Wilson + a positive-type weight (Fejér of suitable width), so it is PSD there. Checked: −6.5e-14 to +9e-15 on all W-matched pools, inside E each time. Labelled a proof sketch: in a W-matched sector the Fejér weight acts as tri(d)², whose q = ±1 to q = 0 coefficient ratio can be tuned to the box's sin δ/δ = 0.94 by its width.
- The same argument holds for the bare D5 at L_s = 4, where |q| ≤ 4. At L_s = 8, c₆..c₈ < 0 can enter.
- The overlap determinant is not a polynomial in the link, so all charges enter and c₆..c₁₀ < 0 multiply its charge-6..10 parts. Its W-matched failure is visible with the Fejér weight too (§3.3), so the failure is the overlap's own.

---

## 3. Tests

**Common settings.**
- 2D U(1), Lx = 2; open time has antiperiodic x, the torus has periodic x and antiperiodic t. M = 1, m = mf = 0.05, β_g = 0, δ = 0.6, link reflection, Θ = θ∘conj (K2 conventions, refereed).
- Pools are admissible with margin: every bulk plaquette is ≤ 0.55 (max over all K2c pools: 0.5495).
- min|eig H| > 0.1 at every evaluated point (worst: 0.707 for H_W; 0.297 for H_T in the C runs).

**Quadrature.**
- Open: Gauss–Legendre n = 16 / 32, with a third level n = 48 on 24 entries plus the diagonal.
- Torus: (n, nw) = (6, 4) / (8, 6), third level (10, 8).
- Pre-run probe: `quad_probe.out`.

**Error estimate.** E = k · max(q, q₃) + 1e-13, where q is the largest entry change between the two levels (Weyl).
- E is an a-posteriori estimate. It bounds the HIGH-level error only under monotone geometric convergence, which q₃ ≪ q supports everywhere. It is not a rigorous analytic bound.
- Certified negative: λ_min < −10E.

### 3.1 K2c-A: open time, K2b's search, hard measure (registered)

| Run (K = 20) | Overlap λ_min (min/max) | E | Wilson λ_min | PG λ_min | Gen-ratio (start → end) |
|---|---|---|---|---|---|
| Lt 12 search 1201 | +1.68e-4 (+1.2e-5) | 3.7e-13 | +2.46e-4 | +1.83e-4 | +0.65 |
| Lt 12 gsearch 4201 | +1.30e-4 (+8.2e-6) | 3.4e-13 | +1.65e-4 | +7.8e-5 | 0.91 → 0.66 |
| Lt 20 search 1220 | +7.02e-5 (+4.1e-6) | 4.9e-13 | +1.29e-4 | +6.35e-5 | +0.50 |
| Lt 20 gsearch 5220 | +2.75e-4 (+1.6e-5) | 6.1e-13 | +2.73e-4 | +2.66e-4 | 0.97 → 0.63 |
| *Fejér ref.* Lt 12 search 1201 | **−2.77e-4 (−2.0e-5)** | 3.1e-13 | +1.06e-6 | +7.9e-10 | −1.23 |
| *Fejér ref.* Lt 12 gsearch 4201 | **−1.15e-4 (−7.7e-6)** | 2.7e-13 | +1.40e-7 | +1.6e-9 | −1.73 |
| *Fejér ref.* Lt 20 gsearch 5220 | **−2.17e-4 (−1.3e-5)** | 5.2e-13 | +4.43e-6 | +3.8e-8 | −1.13 |

- All runs are clean. Bold means certified negative.
- The Fejér reference reproduces K2b's power: −3.45e-4 / −1.40e-4 / −1.58e-4 there, without the margin.
- The hard gsearch objective was still falling at K = 20.

### 3.2 K2c-B: torus, K2b's search, hard measure (registered)

| Run | k | Overlap λ_min (min/max) | E | Wilson | PG | Gen-ratio |
|---|---|---|---|---|---|---|
| Lt 12 gsearch 4212 | 32 | +1.07e-2 (+6.2e-4) | 1.3e-10 | +9.3e-3 | +5.8e-3 | 0.93 → 0.43, still falling |
| Lt 12 search 1212 | 24 | +3.19e-3 (+2.0e-4) | 7.3e-11 | +3.20e-3 | +3.19e-3 | +0.90 |
| Lt 16 gsearch 4216 | 24 | +4.46e-2 (+3.8e-3) | 1.2e-12 | +3.50e-2 | +1.57e-2 | 0.90 → 0.71 |
| Lt 16 search 1216 | 20 | +1.70e-2 (+1.3e-3) | 7.7e-13 | +1.62e-2 | +9.4e-3 | +0.94 |

- Registered reading for A and B: **PASS-at-power_open and PASS-at-power_torus on the explored pools.**
- In every hard row, O, W and PG are within a factor of about 2 of each other, which is the masking described in §0.

### 3.3 V2: W-matched pools (the cusp removed)

**Method.** Each configuration is holonomy-shifted to boundary Wilson line W(slice 1) = 0, which leaves its plaquettes unchanged. On the torus, W(slice T) is also matched, by one x-link; the 0.55 margin is re-checked.
- Then Φ = 0 for every pair, and the PG factor is a constant (rank one).
- Candidates per step: 4 random plus 4 perturbations (σ = 0.02 to 0.2), re-matched.

| Run (hard unless marked) | k | Start (k = 8, no search) | Overlap λ_min (min/max) | E | Wilson + hard | PG | Gen-ratio |
|---|---|---|---|---|---|---|---|
| open Lt 12 wsearch 1401 | 20 | −3.87e-4 | **−2.42e-3 (−1.21e-4)** | 3.1e-13 | −1.7e-14 (PSD) | −8.6e-15 (PSD) | −1.10 |
| open Lt 12 wgsearch 4401 | 20 | −3.71e-4 | **−1.13e-3 (−5.7e-5)** | 3.8e-13 | −1.8e-14 | −8.6e-15 | −1.13 |
| open Lt 20 wgsearch 5401 | 20 | −1.72e-4 | **−1.08e-3 (−5.4e-5)** | 5.3e-13 | −6.5e-14 (E 9.5e-13) | −8.6e-15 | −1.15 |
| open Lt 20 wsearch 1420 | 20 | −4.26e-4 | **−2.58e-3 (−1.29e-4)** | 5.3e-13 | −6.1e-14 | −8.6e-15 | −1.40 |
| **torus Lt 12 wgsearch 4412** | 24 | +3.47e-5 | **−1.473e-4 (−6.3e-6)** | 5.5e-11 | +8.3e-15 | −5.3e-15 | −0.28 |
| *Fejér* open Lt 12 wsearch 1401 | 20 | −3.81e-4 | **−2.40e-3** | 3.1e-13 | PSD | PSD | −1.10 |
| *Fejér* open Lt 12 wgsearch 4401 | 20 | −3.67e-4 | **−1.12e-3** | 3.1e-13 | PSD | PSD | −1.12 |

**Readings (V2, as registered).**
- **FAIL_open-overlap** and **FAIL_torus-overlap.**
- "W-matched mode has power": the Fejér W-matched reference is certified negative.
- The torus objective crossed zero at step 2 (k = 10) and kept falling to −0.28.
- The hard and Fejér W-matched numbers agree to about 1%. With Φ = 0 the two weights differ only in how they weight the crossing plaquette across [−δ, δ]. So the violation belongs to the overlap determinant, not to the gauge weight (reading).

**V5 bug hunt (`V5_verify_wsearch_hard_Lt12.out`).**
- V5a, independent explicit-link builder:
  - its own site indexing; every plaquette computed from links;
  - margin asserted (max bulk 0.5490);
  - admissible set found from the explicit crossing plaquettes and checked by a dense scan;
  - D_ov = 1 + X(X†X)^{−1/2}.
- V5a result: λ_min −2.42150e-3 at both n = 32 and n = 64 (change 1.1e-14). Symmetry defect 7e-15. Wilson −2e-14.
- Pre-registered reading: the FAIL stands as a code-level fact.

**V5b, Wilson-line jitter** (each member's W set to ε·ξ_a, ξ_a uniform in (−1, 1)):

| ε | 1e-4 | 1e-3 | 1e-2 | 3e-2 | 1e-1 |
|---|---|---|---|---|---|
| Overlap λ_min | −2.35e-3 | −2.01e-3 | −1.30e-3 | −8.6e-4 | −1.79e-4 |
| Wilson + hard λ_min | +4.9e-7 | +3.6e-6 | +3.0e-5 | +8.5e-5 | +2.7e-4 |
| PG λ_min | +2.6e-7 | +2.6e-6 | +2.6e-5 | +7.9e-5 | +2.6e-4 |

- E ≤ 5e-13 throughout.
- The violation is not tied to exact matching. It survives a Wilson-line spread of ±0.1 and shrinks as the cusp's floor (∝ ε) grows. This is the masking mechanism, measured.
- It also means the point-configuration kernel is a valid limit of smooth test functions (reading).

**V6 bug hunt, torus (`V6_torus_verify_wgsearch_hard_Lt12.out`).**
- Independent builder on the antiperiodic-time torus, with explicit crossing links (0, a₁) and (b₀, b₁).
- Both crossing rows and their orientation are computed from links. The domains are checked by a scan. The Polyakov link b₀ is integrated by the trapezoid rule over the full circle.
- Result: λ_min −1.47281e-4 (main code −1.4728e-4). Change (6,6,4) → (8,8,6) is 1.1e-12, so E = 2.6e-11. Wilson +8.8e-15.
- Pre-registered reading: the torus FAIL stands as a code-level fact.

### 3.4 Torus Lt = 16, W-matched

V2 run: torus Lt = 16, hard, W-matched, `wgsearch` seed 4416, K = 16 (`V2_torus_Lt16_wgsearch_hard.out`). Both Wilson lines matched exactly (check 0.0); max bulk plaquette 0.5436.

| Quantity | Value |
|---|---|
| Start (k = 8) | +8.5e-5 |
| Overlap λ_min | **−7.27e-5** (min/max −5.1e-6), certified negative |
| E | 3.2e-13 (q 1.4e-14, q₃ 3.4e-15) |
| Wilson + hard | +3.2e-9 (PSD) |
| PG | −6e-16 (PSD) |
| Gen-ratio | −2.48 |
| min\|H_W\| | 0.796 |

- The objective was negative from step 1 (−4.8e-3) and fell to −1.11 at k = 16.
- Reading (V2): **FAIL_torus-overlap at Lt = 16 too.**
- The torus violation does not fade from Lt = 12 to Lt = 16. Relative to the largest eigenvalue it is −6.3e-6 at Lt = 12 and −5.1e-6 at Lt = 16. These are different pools and searches, so this is not a convergence statement (reading).
- No independent-code rerun at Lt = 16. V6 covers the same torus code path at Lt = 12.

### 3.5 K2c-C: PV-subtracted DWF under the hard measure

**Kernel definitions.**
- DWF_Ls is computed by K2b's transfer formula, re-checked against the dense 5D ratio on each pool (≤ 1.7e-13).
- SH is the L_s = ∞ limit; the formula agrees with direct SH to 0.
- D5 is the bare dense 5D determinant, computed on open pools, plus the W-matched torus pool in V7.

| Pool (hard weight) | O | SH | DWF_4 | DWF_8 | D5_4 | D5_8 | W | PG | Max E |
|---|---|---|---|---|---|---|---|---|---|
| K2b SH-search pool (Fejér-searched; max bulk 0.5995, no margin) | +1.95e-4 | +1.96e-4 | +1.96e-4 | +1.96e-4 | +1.92e-4 | +1.88e-4 | +1.95e-4 | +1.95e-4 | 4.6e-12 |
| K2b Neuberger-search pool (max bulk 0.5995) | +8.8e-4 | +1.04e-3 | +1.11e-3 | +1.05e-3 | +1.26e-3 | +1.35e-3 | +1.07e-3 | +9.7e-4 | 5.7e-12 |
| V2 open Lt 12 wsearch 1401 | **−2.42e-3** | **−1.08e-5** | **−2.57e-5** | **−1.62e-5** | +6.1e-12 | +2.1e-11 | −1.7e-14 | −8.6e-15 | 4.6e-12 |
| V2 open Lt 12 wgsearch 4401 | **−1.13e-3** | **−1.36e-5** | **−1.10e-5** | **−1.40e-5** | +1.8e-12 | +4.2e-12 | −1.8e-14 | −8.6e-15 | 5.8e-12 |
| **V2 torus Lt 12 wgsearch 4412** | **−1.47e-4** | **−7.25e-6** | **−5.08e-6** | **−8.23e-6** | +4.7e-8 (V7) | +9.4e-8 (V7) | +8.3e-15 | −5.3e-15 | 1.1e-10 |
| A open Lt 12 search 1201 (unmatched) | +1.68e-4 | +2.33e-4 | +2.79e-4 | +2.37e-4 | +4.26e-4 | +5.52e-4 | +2.46e-4 | +1.83e-4 | 4.6e-12 |
| A open Lt 12 gsearch 4201 (unmatched) | +1.30e-4 | +1.79e-4 | +2.33e-4 | +1.87e-4 | +3.39e-4 | +4.13e-4 | +1.65e-4 | +7.8e-5 | 3.6e-12 |
| B torus Lt 12 gsearch 4212 (unmatched) | +1.07e-2 | +1.06e-2 | +1.05e-2 | +1.05e-2 | not run | not run | +9.3e-3 | +5.8e-3 | 2.9e-10 |
| B torus Lt 16 gsearch 4216 (unmatched) | +4.46e-2 | +4.24e-2 | +4.14e-2 | +4.24e-2 | not run | not run | +3.50e-2 | +1.57e-2 | 4.4e-12 |

**Reading (registered): "PV-DWF-hard FAIL at L_s = 4 and 8"**, on the open pools and on the torus pool.
- The torus pool is clean: min|eig H_T| = 0.297 > 0.1. Its errors are E ≤ 1.1e-10, and the DWF formula agrees with the dense ratio to 4.4e-13.
- The bare D5 + hard is PSD on the open W-matched pools (positive, at the 1e-12 to 1e-11 level). At L_s = 4 this is guaranteed by §2(d).
- V7 (registered 18:15Z) adds the bare D5 control on the W-matched torus pool. It uses the (6, 4) quadrature, with E from a 10-entry change to (8, 6). D5_4 is +4.7e-8 (E 1.4e-12) and D5_8 is +9.4e-8 (E 6.8e-11): both PSD.
- So on the torus as on the open lattice, removing the PV fields restores positivity on the very pool where PV-DWF fails.
- On K2b's Fejér-searched pools every hard kernel is PSD, with O ≈ W ≈ PG. This is the cusp again, so those pools carry no information about the hard measure.

### 3.6 V3 cross-evaluations (descriptive)

Identical configurations under the two weights (`k2c_dwf.py`, all kernels):

| Pool | Weight | O | SH | DWF_4 | DWF_8 | D5_4 / D5_8 | W | PG |
|---|---|---|---|---|---|---|---|---|
| Fejér-searched pool `search_tri` 1201 (Fejér O = −2.77e-4) | **hard** | +1.71e-4 | +2.35e-4 | +2.85e-4 | +2.40e-4 | +4.4e-4 / +5.6e-4 | +2.48e-4 | +1.83e-4 |
| Hard-searched pool `search_hard` 1201 (hard O = +1.68e-4) | **Fejér** | **−1.28e-4** | **−6.0e-7** | **−2.2e-7** | **−6.5e-7** | +1.4e-6 / +1.9e-6 | +6.1e-7 | +7.8e-10 |

- E ≤ 4.5e-12 throughout.
- The pool that the hard search left positive is certified negative under the Fejér weight, for O, SH and both PV-DWF.
- The Fejér-negative pool turns positive under the hard weight, with O ≈ W ≈ PG.
- So the hard/Fejér difference on unmatched pools is the weight's pure-gauge factor, not the configurations: masking confirmed on identical sets (checked).

---

## 4. What this changes (suggested wording; the owner and referee decide)

1. **K2 / referee (L3g).** The referee's scope correction ("valid for the Fejér-weighted measure; does not establish failure for the hard-admissibility measure") should be updated:
   - With X3's hard measure, gauge-invariant RP of the gauged Dirac overlap also fails, on open-time lattices (Lt = 12, 20) and on the antiperiodic torus (Lt = 12, 16).
   - It shows up in fixed-boundary-Wilson-line sectors. Two independent builders agree.
   - Same family; other-vendor referee owed.
2. **Torus / infinite-time escape.** K2, K2b and the referee all left "torus or infinite-time positivity" open. In this proxy the torus fails at Lt = 12 and 16 (relative size −6.3e-6 and −5.1e-6, on different pools), so that escape is closed for the hard measure.
   - The Fejér measure on the torus was not run W-matched here. Reading: it would very likely fail too, since the W-matched hard and Fejér open results agree to 1%.
   - Infinite time is not tested directly. On open lattices the violation does not shrink from Lt = 12 to Lt = 20 (−2.42e-3 → −2.58e-3 for the λ_min search).
3. **X3 contingency row (`X3/COMBO_REPORT.md:252`) is triggered** for X3's specified measure: "Euclidean-only without RP" (forbidden, `CH/WALL.md:44`) unless matter pays Π-W.
   - K2b's finding extends to the hard measure: PV-subtracted DWF at L_s = 4 and 8 also fails, while the bare 5D determinant is PSD.
   - So the only RP exit seen here is 5D fermions without PV, i.e. F2-R's finite-n price (AX:47).
4. **New for X3's price P-X3d (reading).** The hard plaquette bound is RP for pure gauge only in special geometries: even Lx in 2D (proved). For odd Lx it fails (proved and checked), and in ≥ 3D it likely fails (suggested).
   - Admissibility read as hard support (AX:63-73, reading note 3) may therefore be in tension with OS positivity, independently of fermions. This is proved only for odd Lx in 2D.
   - A cheap test is owed: a pure-gauge 3D slice with 2 × 2 plaquettes.
5. **Method lesson.** A non-smooth gauge weight (here the hard indicator's cusp in the boundary Wilson line) can make RP kernels look positive on generic configuration sets. Searches should include sectors where such factors are constant.

**Scope (reading).**
- 2D U(1), Lx = 2 (degenerate x extent), vector-like Dirac overlap (not the chiral measure), β_g = 0, gauge-only observables, link reflection.
- Torus at Lt = 12 and 16; independent code at Lt = 12 only.
- Not tested: Lx ≥ 4, 4D, non-abelian groups, the chiral (Weyl) measure, site reflection.

## 5. Not done, deviations, files

**Dropped for time** (registered, not run):
- V4: open hard gsearch continued to K = 48. It was superseded by V2.
- K2c-C on the A Lt = 20 pools and on the torus `search` pools.
- V3 on the Lt = 12 gsearch and Lt = 20 Fejér pools; the two V3 runs that were done are in §3.6.
- The optional DWF_4-targeted search.

**Process notes.**
- (i) `k2c_search.py` was edited (V2 modes added) at 17:41:28Z, while chain A was running. By file birth times, only the four B runs (started from 17:43Z) used the edited file. Its non-matched path makes the same random draws in the same order. The one exception is a perturbation that fails 2000 consecutive margin checks; I judge that very unlikely, but did not log it per step.
- (ii) Chains C, D, E and F were stopped between jobs and re-queued as F and G (V5 and V6 put first). One orphaned job each time finished alone before the next started, so runs stayed one at a time.
- (iii) Two PREREG header times were typed ahead of the clock. They are corrected by appended notes and not edited.

**Memory.** Every run stayed below 0.3 GB. The largest was 234 MB (`R_open_Lt20_gsearch_tri`). Nothing of mine is left running.

**Files** (all in `K2c/`):
- `PREREG.md`.
- `scripts/k2c_lib.py`.
- `scripts/k2c_search.py`: modes `search`, `gsearch`, `wsearch`, `wgsearch`; weights `hard` and `tri`.
- `scripts/k2c_dwf.py`.
- `scripts/k2c_pg_odd.py` and `k2c_pg_odd_exact.py` (V1).
- `scripts/k2c_v5_verify.py`.
- `scripts/k2c_v6_torus_verify.py`.
- `scripts/k2c_v7_torus_d5.py`.
- `scripts/quad_probe.py`.
- Outputs: `A_*.out`, `R_*.out` (Fejér reference), `B_*.out`, `V2_*.out`, `V5_*.out`, `V6_*.out`, `V7_*.out`, `C_*.out`, `V3_*.out`, `pg_odd*.out`, `quad_probe.out`.
- Pools: `pool_K2c_*.npz`, plus `pool_A_K20_*` if V4 had run (it did not).
- Queues: `chainA.sh`, `chainC.sh` through `chainH.sh`. Copies of `lat2d.py` and `k2b_lib.py`, unchanged.

**Numerical note.** numpy's slogdet RuntimeWarnings appear in the `.err` files, as in K2 and K2b. Values are cross-checked by the independent builders (V5, V6) to all printed digits.
