# K2b: torus power, domain-wall control, and the Shamir kernel (exercise step 8 follow-up to K2)

**Agent and provenance.** Claude Opus 5.5 (test agent K2b), run 2026-10-14 from 16:17Z to 17:33Z. Same model family as K2, X3 and the supervisor: nothing here is independent or refereed. No repository was edited. Code: K2's `lat2d.py` copied unchanged into `K2b/scripts/` plus my own `k2b_lib.py` and test scripts. Every run used OMP_NUM_THREADS=2 and ran one at a time, with two exceptions reported in §5.

**Refresher read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (233 lines; cited AX). In full: `kills/K2/KILL_REPORT.md`, `kills/K2/PREREG.md`, `combos/X3/COMBO_REPORT.md`, and K2's `lat2d.py`, `k2t3_gi_rp.py`, `k2t3_verify.py`, `k2v5_clustered.py`, `k2v6_open_Lt.py` with their outputs.

**Paths.** `K2/` = `scratchpad/chirality_ex/kills/K2/`; `X3/` = `scratchpad/chirality_ex/combos/X3/`; `K2b/` = this folder. Script outputs are `K2b/scripts/<name>.out`.

**Labels.** proved (my argument, unrefereed) / checked (a script run here) / suggested / reading.

**Pre-registration.** `K2b/PREREG.md`: T1 and T2 at :23-92 (written 16:23Z, before any test script existed). Follow-ups V1 (:107), V2 (:121), V3 (:137), N2 (:165), V4 (:151) and V5 (:170) were each registered after seeing the previous result and before running. No reading was edited afterwards. A results log is at :179.

---

## 0. Plain-words summary

**1. Torus: still no violation, now with a search that has shown power.** I replaced K2's random sets with a greedy search: start from 8 configurations and keep adding whichever of 8 candidates pushes the kernel furthest toward a negative direction. Two objectives were used:
- the smallest eigenvalue of the kernel itself;
- the overlap kernel measured against the Wilson kernel on the same configurations (this cannot be fooled by near-duplicates).

On the open-time lattice (positive control), the overlap kernel was already negative by step 1 in 3/3 Neuberger runs (Lt = 12 twice, Lt = 20 once; one random starting pool was negative before any search step). All three end certified negative. With the Wilson-referenced objective, the overlap's quadratic form reaches −1.1 times Wilson's form.

On the torus (Lt = 12, up to 44 configurations; Lt = 16, 16 configurations), the same search never produced a negative eigenvalue. Its best Wilson-referenced value was +0.013, at Lt = 12 with 44 configurations (open lattice: −1.07 to −1.23). Pre-registered reading: **PASS-at-power on the explored pools**. This is not a proof of torus positivity, and no mechanism for one is known.

**Caveat.** On the torus the Wilson-referenced value keeps falling as the pool grows: 0.86 at 8 configurations, 0.21 at 20, 0.032 at 36, 0.013 at 44. The fall is slowing: a straight-line extrapolation from k = 36 predicted zero near k = 41, and it did not cross there. But it had not levelled off when I stopped. A larger search could still cross zero, so this pushes the torus question further without settling it.

**2. Domain-wall control: the method passes, but finite-L_s DWF is not an RP exit.**
- The bare 5D domain-wall determinant (a 3D Wilson fermion here, L_s = 4 and 8, no Pauli–Villars fields) is reflection-positive. This is proved by the Osterwalder–Seiler argument and checked PSD on all 6 open pools tested, including the pools where the overlap fails. So the method is not suspect.
- The physical DWF measure divides by the Pauli–Villars (PV) determinant. That measure has a **certified negative eigenvalue already at L_s = 4**, and at every L_s up to 48 and at L_s = ∞, on a searched pool (−2.2e-6, error 2e-13). Two code paths agree to 1e-13: the dense 5D ratio and a transfer-matrix formula.

**3. The violation is not a quirk of Neuberger's kernel.** The Shamir-kernel overlap (the L_s → ∞ limit of DWF) also violates RP on searched pools, with an eigenvalue about 70–1400× smaller than Neuberger's on the same pools. On K2's random sets it is PSD, while Neuberger fails.

**4. What is going on (reading).** Every DWF determinant here is a ratio: 5D fermions over 5D PV fields, det D5(mf) / det D5(1). The Shamir overlap is its L_s → ∞ limit (checked to 5e-13). Neuberger's overlap is, as I recall, the limit of the analogous construction with the Wilson kernel, which I did not compute. Numerator and denominator are each RP kernels: proved by the OS argument for any mf, and checked at mf = 0.05 and mf = 1 (N2). A ratio of two positive-definite kernels need not be positive-definite, and here it is not. This is where Kikukawa–Usui's proof hits its PV obstruction (X3/COMBO_REPORT.md:164). So on open time L3g fails for both overlap kernels tested and for PV-subtracted DWF, not just for Neuberger's kernel.

**5. Consequence.** X3 named "a DWF formulation at finite L_s, which is 5D-Wilson RP" as the fallback if L3g fails (X3/COMBO_REPORT.md:311; K2/KILL_REPORT.md:62). That fallback holds only if the PV subtraction is dropped. In that case the heavy 5D bulk fermions stay in the theory as physical heavy states: F2-R's finite-n price. There is now a finite counterexample showing that the PV-subtracted version is not RP.

**Not done.** The chiral (Weyl) measure (T3), site reflection, Lx = 4 on the torus (a 7-dimensional exact crossing integral; compute, not memory), and several dropped torus runs (§4).

---

## 1. Verdicts

| Item | Verdict | Reason (label) |
|---|---|---|
| **K2's FAIL (L3g dead on open time)** | **stands, strengthened** | The T2a control is PSD on all 6 open pools (proved + checked), so the method is not suspect. K2's value is reproduced exactly (−7.4055e-6, `k2b_sanity.out`). The open-lattice searches find much larger violations: λ_min −3.45e-4 (min/max −2.1e-5) at Lt = 12 and −1.58e-4 at Lt = 20, with E ≤ 4e-13 and Wilson PSD (checked). |
| **L3g on the torus** | **PASS-at-power on the explored pools; still OPEN as a lemma** | T1, V1, V4, V5 and the Lt = 16 run found no certified negative (checked). Power: the same search has the open overlap negative by step 1 in 3/3 runs. The torus Wilson-referenced minimum is +0.013 (k = 44), against −1.07 to −1.23 on open lattices. Caveat: the torus objective was still slowly falling at k = 44 (0.21 → 0.032 → 0.013 at k = 20 / 36 / 44). No mechanism for torus positivity: the PV-ratio structure (§2.3) is the same on the torus (reading). |
| **"DWF at finite L_s is RP" (X3:311, K2:62)** | **split** | *Bare* 5D det: RP (proved via OS; checked PSD on 6/6 open pools, L_s = 4, 8). *PV-subtracted* DWF measure: **not RP**, with a certified negative at L_s = 4, 6, 8, 12, …, 48, ∞ on the SH-search pool, and at L_s ≥ 6 on the Neuberger-search pool (checked, two code paths). |
| **Neuberger-kernel specificity (V2)** | **no, violation is kernel-generic** | The Shamir overlap is certified negative on 2 searched pools (−1.05e-6 and −2.5e-7, E ≈ 2e-13), PSD on 4/4 of K2's random pools (checked). Neuberger's violation is roughly 70–1400× larger on the same pools. |
| **Supervisor's T2 expectation ("DWF expected PSD")** | **right for the bare 5D det, wrong for the physical (PV) DWF measure** | as above |

---

## 2. Tests

### 2.1 K2b-T1 (+V1, V4, V5): torus with power (PREREG.md:23-60, :107-119, :151, :170)

**Method.** Exact gauge-invariant crossing integral (K2's reduction): Fejér weight; δ = 0.6; M = 1; m = 0.05.
- Open lattice: Lx = 2, antiperiodic x; GL 16/32.
- Torus: Lx = 2, periodic x, antiperiodic t; GL 4/6 per kink-free piece, Polyakov trapezoid 4/6.

The torus quadrature was checked converged to ~3e-12 in log Z before the runs (`timing_probe.py`; no kernel or eigenvalue computed).

**Search.** Greedy pool growth (`k2b_t1_search.py`); candidates per step: 3 random, 3 perturbed (σ = 0.02/0.05/0.1), 2 holonomy shifts.
- **Error bound.** E = k·q + 1e-13, where q is the largest entry change between the low and high quadratures (Weyl bound).
- **Certified negative.** λ_min < −10E.

| Run | Geometry | Objective | k | Overlap λ_min (min/max) | E | Wilson λ_min | gen-ratio min | Reading |
|---|---|---|---|---|---|---|---|---|
| T1 control (`t1_open_Lt12_search`) | open Lt = 12 | λ_min | 20 | **−3.45e-4 (−2.1e-5)**, 2 negative | 2.4e-13 | +7.9e-7 | −1.23 | certified negative; power shown (negative from step 1) |
| V1 control (`v1_open_Lt12_gsearch`) | open Lt = 12 | gen-ratio | 20 | **−1.40e-4 (−9.0e-6)**, 3 negative | 2.4e-13 | +3.5e-8 | −1.12 | certified negative (random start already −1.6e-6; objective −1.10 by step 3) |
| V2 (`v2_open_Lt20_gsearch_O`) | open Lt = 20 | gen-ratio | 20 | **−1.58e-4 (−9.6e-6)**, 3 negative | 3.6e-13 | +7.2e-7 | −1.07 | certified negative (negative from step 1) |
| T1 (`t1_torus_Lt12_search_rand`) | torus Lt = 12 | λ_min | 20 | +1.71e-5 (+1.6e-6) | 8.1e-9 | +1.81e-5 | +0.33 | PSD; search went to near-duplicates |
| V1 (`v1_torus_Lt12_gsearch`) | torus Lt = 12 | gen-ratio | 20 | +7.47e-4 (+6.7e-5) | 3.6e-9 | +7.33e-4 | +0.21 | PSD; objective 0.86 → 0.21, still falling |
| V4 (`v4_torus_Lt12_gsearch_K36`) | torus Lt = 12 | gen-ratio | 36 | +5.16e-5 (+2.4e-6) | 4.8e-9 (q from 112 entries, V4 rule) | +4.94e-5 | **+0.032** | PSD; objective 0.21 (k = 20) → 0.059 (k = 32) → 0.032 (k = 36), **still falling** |
| V5 (`v5_torus_Lt12_gsearch_resume_K44`; V4 pool resumed, new candidates) | torus Lt = 12 | gen-ratio | 44 | +3.89e-5 (+1.5e-6) | 1.4e-8 (q from 121 entries, V4 rule) | +3.91e-5 | **+0.013** | PSD; objective 0.032 → 0.024 → 0.020 → 0.013 (k = 36 / 37 / 41 / 44), still falling but slowing |
| V1 (`v1_torus_Lt16_gsearch`) | torus Lt = 16 | gen-ratio | 16 | +1.28e-5 (+1.1e-6) | 3.4e-9 | +1.28e-5 | +0.22 | PSD; objective 0.78 → 0.22 over 8 steps (similar to Lt = 12 at k = 20) |

All runs were clean: min|H_W| ≥ 0.71, q ≤ 7e-10.

**Reading (pre-registered, PREREG.md:44-56).**
- CONTROL-NO-POWER is not triggered: the open control is certified negative.
- No torus pool has a certified negative, so the reading is **PASS-at-power**.

**Power statement.**
- (a) Certification threshold on the torus: 10E ≈ 1e-7 (unit-diagonal units). Any negative eigenvalue below −1e-7 on these pools would have been certified. None appeared; the smallest λ_min reached was +1.7e-5.
- (b) Open control: λ_min/λ_max down to −2.1e-5.
- (c) Wilson-referenced: open-lattice directions exist where the overlap's form is −1.1 × Wilson's; on the torus the minimum found is +0.013 (Lt = 12, k = 44).
- (d) The torus objective falls monotonically with pool size, slowing down, and had not converged at k = 44. So the power statement is limited by pool size, and "no violation" holds for these pools only.

**Scope.**
- The explored pools only.
- Lx = 2; Lt = 12 and 16; Lt = 20 not searched (time).
- This is not a torus RP proof.

### 2.2 K2b-T2: domain-wall control (PREREG.md:62-92)

**Operator.** Shamir DWF with the same 2D gauge field, s-independent:
D5(mf) = (D_W − M + 1)δ − P₋δ_{s′,s+1} − P₊δ_{s′,s−1} + mf (P₋ at (L_s, 1) + P₊ at (1, L_s)).

**Kernels.** Seven kernels from the same quadrature points (`k2b_t2_dwf.py`):
- W: Wilson;
- O: Neuberger;
- SH: Shamir overlap, the L_s = ∞ limit;
- D5_Ls: bare det D5(mf);
- DWF_Ls: det D5(mf) / det D5(1).

**Code check.** At L_s = 40 the SH limit equals the dense 5D ratio to 4.9e-13 (`k2b_sanity.out`).

**Proof that the bare D5 is RP (proved, mine, unrefereed; PREREG.md:77-82).**
- D5 is a 3D Wilson r = 1 fermion with Hermitian anticommuting gammas (σ1, σ2, σ3) = (γ_x, γ_t, γ5), mass −M.
- The s-direction is intra-slice.
- With B the slice bilinear, γ_t B† γ_t = B holds term by term:
  - the s-hops, because γ_t P∓ γ_t = P± and the s-transpose swaps the two hops;
  - the mf corner terms, likewise;
  - the x-hops, the standard case.
- The t-hops have the r = 1 projector form. Osterwalder–Seiler then gives a PSD gauge-fixed kernel.
- The Fejér crossing weight is positive-type (K2 Amendment A1), so the gauge-invariant kernel is PSD too.

| Pool | O (Neuberger) λ_min | SH | DWF_4 | DWF_8 | D5_4 / D5_8 (control) | W |
|---|---|---|---|---|---|---|
| K2 G1p set 0 (`t2_g1p_262_s0`) | +7.6e-5 | +2.1e-4 | +2.8e-4 | +2.1e-4 | +5.6e-4 / +8.1e-4 | +2.2e-4 |
| K2 G1p set 1 (`t2_g1p_262_s1`) | **−4.46e-5** | +5.5e-5 | +8.5e-5 | +5.8e-5 | +1.8e-4 / +2.4e-4 | +6.5e-5 |
| K2 G1p set 2 (`t2_g1p_262_s2`) | **−3.55e-6** | +4.0e-6 | +7.6e-6 | +4.1e-6 | +2.4e-5 / +3.6e-5 | +9.7e-6 |
| K2 V6 Lt = 20 set 1 (`t2_v6_9010_s1`) | **−1.95e-4** | +1.6e-4 | +3.0e-4 | +1.8e-4 | +7.2e-4 / +1.1e-3 | +2.1e-4 |
| T1 Neuberger-search pool, k = 20 (`t2_pool_open_search`) | **−3.45e-4** | **−2.52e-7** | +3.1e-7 | **−2.93e-7** | +1.2e-6 / +1.4e-6 | +7.9e-7 |
| V2 SH-search pool, k = 20 (`t2_pool_open_search_SH`) | **−7.63e-5** | **−1.05e-6** | **−2.23e-6** | **−1.46e-6** | +1.4e-7 / +1.7e-7 | +8.9e-8 |

Bold means certified negative. E ≤ 5e-12 everywhere (q ≤ 2.3e-13); min|eig H_W|, min|eig H_T| ≥ 0.37.

**Readings (PREREG.md:83-90).**
- **T2a CONTROL-PASS** (open pools; the torus pool was dropped). The bare D5 is PSD on every pool at L_s = 4 and 8. On the SH-search pool its margin is +1.4e-7, against E ≈ 2e-12.
- **T2b.** On K2's random failing sets (G1p sets 1 and 2, V6 set 1), DWF_4 and DWF_8 are PSD while Neuberger fails. Those were the sets in T2's registered pool list.
- **T2b, searched pools (added to T2 by V3 before running).** DWF_8 is certified negative on both. DWF_4 is certified negative on the SH pool. So the pre-registered line **"PV subtraction breaks RP"** is met.
- **T2 (c).** **"Violation kernel-generic"**: SH is certified negative on 2 open pools.
- The torus T2 pool (g3p_565_s0) was dropped for time (V4 note).

### 2.3 V3: DWF versus L_s (`v3_dwf_Ls.out`; PREREG V3)

The transfer-matrix formula det D5(mf)/det D5(1) = det[(1+mf)/2 + (1−mf)/2 γ5 (1 − T^{L_s})/(1 + T^{L_s})], with T = (1 − H_T)/(1 + H_T), was checked against the dense 5D ratio at L_s = 4 and 8: max |Δ log det| = 8e-14 and 2e-13. Its values also match the dense T2 kernels to all printed digits (−2.2313e-6, −1.4610e-6, +3.0639e-7, −2.9323e-7).

| L_s | 4 | 6 | 8 | 12 | 16 | 24 | 32 | 48 | ∞ |
|---|---|---|---|---|---|---|---|---|---|
| SH-search pool λ_min | **−2.23e-6** | **−2.17e-6** | **−1.46e-6** | **−1.08e-6** | **−1.05e-6** | **−1.052e-6** | **−1.052e-6** | **−1.052e-6** | **−1.052e-6** |
| Neuberger-search pool λ_min | +3.1e-7 | **−1.42e-7** | **−2.93e-7** | **−2.62e-7** | **−2.52e-7** | **−2.52e-7** | … | … | **−2.52e-7** |
| K2 G1p set 1 | +8.5e-5 | +6.5e-5 | +5.8e-5 | +5.5e-5 | … | … | … | … | +5.5e-5 |

E ≈ 2e-13 throughout.

**Reading (pre-registered): "finite-L_s DWF inherits the violation from L_s = L\*", with L\* = 4,** the smallest L_s tested, on the SH-search pool. The violation is largest at small L_s and converges to the L_s = ∞ value. It is not a large-L_s limit effect.

**Mechanism (reading, with one proved step).**
- Proved (elementary): DWF_Ls = D5_Ls(mf) / D5_Ls(1) entrywise, at each quadrature point. Both factors are RP kernels (the OS argument above applies to any mf). The kernel is the crossing-integral of that ratio.
- Checked (note N2, `n2_pv_denominator.out`): the denominator's own kernel det D5(1) is PSD on the SH-search pool, with λ_min +1.34e-7 (L_s = 4) and +1.58e-7 (L_s = 8), E ≤ 3.5e-12. On that pool the numerator is PSD (D5_4 at +1.4e-7), the denominator is PSD, and their ratio is certified negative (−2.23e-6).
- Reading: a pointwise ratio of two positive-type kernels is not positive-type in general. Bosonic PV fields with a first-order (Dirac-type) action have no OS positivity of their own; they enter as 1/det.
- X3 recorded Kikukawa–Usui's PV obstruction, which needs [∇₀, ∇_k] ≠ 0 (X3/COMBO_REPORT.md:164). Every configuration here carries nonzero plaquettes (electric field) on both sides of the plane. The finite counterexamples sit where their proof breaks down (reading).

### 2.4 V2: Shamir-kernel searches (PREREG V2, :121-135)

| Run | k | SH λ_min (min/max) | E | Wilson λ_min | gen-ratio min | Reading |
|---|---|---|---|---|---|---|
| `v2_open_Lt12_search_SH` (λ_min objective, seed 1201) | 20 | **−1.05e-6 (−6.5e-8)**, 2 negative | 2.0e-13 | +8.9e-8 | −0.89 | **SH-FAIL** |
| `v2_open_Lt12_gsearch_SH` (gen-ratio, seed 4201) | 20 | +7.8e-8 | 2.0e-13 | +1.9e-6 | +0.014 | PSD |
| `v2_open_Lt20_gsearch_SH` (seed 5220) | 20 | +2.9e-7 | 2.4e-13 | +1.0e-6 | +0.089 | PSD; matched Neuberger run −1.58e-4 |

**Reading: SH-FAIL** (one certified negative with Wilson PSD). The gen-ratio searches missed it because the SH violation lives where Wilson's eigenvalues are ~1e-7, below that objective's 1e-6 cutoff (reading).

---

## 3. What this changes (suggested registry wording; owner and referee decide)

1. **K2 row L3g** (`K2/KILL_REPORT.md:78`).
   - Add: "control passed (bare 5D DWF det PSD on 6/6 open pools); open-lattice violation reproduced and enlarged by search (−3.45e-4); the violation is shared by the Shamir kernel and by PV-subtracted DWF at every L_s ≥ 4 tested on a searched pool."
   - Torus: "PASS-at-power on explored pools (the open search has the overlap negative by step 1 in 3/3 runs; torus none up to k = 44, Wilson-referenced minimum +0.013 and still slowly falling); no mechanism; still OPEN as a lemma."
2. **X3 price table / K2 exits** (`X3/COMBO_REPORT.md:311`, `:287`; `K2/KILL_REPORT.md:62`).
   - Change "DWF at finite L_s, which is 5D-Wilson RP" to "the **bare** 5D det (no PV fields) is RP; the PV-subtracted DWF measure is not (counterexample at L_s = 4)".
   - So the RP exit is "5D fermions without PV, bulk modes kept as heavy physical states". That is F2-R's finite-n price (AX:47 site content; AX:57 is not touched by locality, since the 5D operator is nearest-neighbour). It gives exact gauge invariance only in the vector-like case: the chiral case still needs the mirror wall gapped (F2-R). This is a reading.
   - X3's reopen condition 1 (`:287`, "a DWF formulation at finite L_s with RP and a controlled L_s → ∞ limit") is now partly answered. At finite L_s with PV: no RP. Without PV: RP, but the L_s → ∞ limit is not the overlap (the bulk does not decouple without PV). This is a reading.
3. **Referee owed** (codex sol): `k2b_lib.py` (DWF build, Shamir sgn), the OS argument for D5 (PREREG.md:77-82), `k2b_v3_dwf_Ls.py`'s formula, and `k2b_t1_search.py`'s certification bound.

## 4. Not done (time box)

- **T3: chiral U(1) measure.** Needs Lüscher's U(1) measure term; not attempted.
- **Site reflection.** Not attempted.
- **Lx = 4 on the torus.** The exact crossing integral is 7-dimensional (PREREG.md:27-28).
- **Dropped torus runs** (V4 note): the clustered-start search, the Lt = 16 λ_min search, the Lt = 20 search, the clustered k = 16 screens at Lt = 12/16/20, and the T2 torus pool.
- Lt = 20 on the torus was therefore not searched.

## 5. Files and notes (all in `K2b/`)

- `PREREG.md`: T1, T2 (16:23Z), N1, V1, V2, V3, V4, N2, V5.
- `scripts/lat2d.py`: K2's, unchanged copy. `scripts/k2b_lib.py`: kernels for W / O / SH / D5 / D5PV / D5ONE, pool class, certification helpers.
- `scripts/k2b_t1_search.py`: greedy search (modes `search`, `gsearch`, `screen`; optional target OP; V4 subset-q option via K2B_QSUB). Pools are saved as `pool_*.npz`.
- `scripts/k2b_t2_dwf.py`: T2. `scripts/k2b_v3_dwf_Ls.py`: V3. `scripts/k2b_n2_pv_denominator.py` → `n2_pv_denominator.out`: N2. `scripts/k2b_sanity.py` → `k2b_sanity.out`. `scripts/timing_probe.py`.
- `pool_V4_final_torus_Lt12_k36.npz`: the V4 torus pool, which V5 resumes. V5 output: `v5_torus_Lt12_gsearch_resume_K44.out`.
- Outputs: `t1_*.out`, `v1_*.out`, `v2_*.out`, `v3_dwf_Ls.out`, `v4_*.out`, `t2_*.out` (each ends with its peak RSS); `chain[A-E].sh` are the run queues.
- **Memory.**
  - Every production run peaked below 0.3 GB; the largest was 255 MB (`n2_pv_denominator`).
  - **Breach:** the one-off `k2b_sanity.py` check (dense L_s = 40 operator) peaked at 379 MB for a few seconds. It is recorded in PREREG N1.
  - **Concurrency slip:** when I re-queued runs at 16:33Z, an orphaned run (`v1_torus_Lt12_gsearch`, ~120 MB) overlapped the next queue's first run for about 25 s, before I killed it (two processes, together ~260 MB). Its output was overwritten by the later clean rerun.
  - Nothing of mine is left running.
- **Numerical note.** As in K2, numpy's slogdet emits spurious RuntimeWarnings (in the `.err` files). Values are cross-checked: K2's −7.4055e-6 is reproduced exactly, and the dense-vs-formula DWF paths agree to 1e-13.
