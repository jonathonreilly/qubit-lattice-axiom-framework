# NT-1″ report: completing the chiral measure (route 1)

> **Referee (codex gpt-5.6-sol, 15:17Z): CONFIRMED WITH CORRECTIONS. OPEN at (b″) is correct.**
> - **Independently confirmed:** the edge lemma, the bulk exponential decay and C(11112) = 0.
> - **Not proved from finite sizes:** the universal "no local measure on this strip" claim. It is strongly supported.
>
> See `REFEREE_VERDICT.md` and `referee/REFEREE.md`.

**Reading: OPEN, failing (b″).**
- **(b″) cannot be met on NT-1′'s geometry.** The reason is the geometry, not the measure.
- **(b′) passes the fixed minimal wording for the bulk tail.** But near the open time edges, the finite-volume dependence falls only as a power of Lx, so Lüscher's uniform exponential bound fails there too.
- **Step 3, recomputing a kernel, was not triggered.**

**Provenance.** The worker was Claude Opus 5.5 at xhigh, the same family as NT-1′ and the supervisor, so not independent. Unrefereed. The window was 14:3x–15:05Z on 2026-10-15. The harness blocks subagents from writing REPORT.md, so the supervisor saved this file from the worker's final message, lightly condensed. All numbers and file references are the worker's.

## Plain words

1. **The Wilson-line circle cannot be wound on this lattice.**
   - On the open-time strip, the Wilson kernel H_W has exact zero modes on the top or bottom time slice whenever that slice's Wilson line times the charge equals π. This holds for any plaquettes.
   - Winding the Wilson line once around the circle always hits such a point, where the overlap is undefined and the index changes. So there is no admissible non-contractible loop to transport the measure around.
   - The anomalous L1 control is blocked the same way, so the strip gives no contrast.
   - The admissible field space breaks into contractible pieces. On those, global integrability reduces to local integrability, which the explicit straight-ray measure has by construction. Whether that vacuity counts as passing (b″) is for the referee or the owner to decide, not the worker.
2. **On a torus the same question has content, and 11112 passes it.**
   - Both Wilson lines are then free circles.
   - The toron Chern number is 0 for 11112 and −1 for L1.
   - Around the non-contractible loop, the 11112 holonomy has winding 0 and L1's has winding 1.
3. **The anomaly-free x-flat tail decays exponentially in the bulk:** at 0.87 ± 0.06 per spacing on random fields, and about ln 2 on clean backgrounds out to Lx = 22. L1's plateau falls exactly as 1/Lx.
4. **Within two slices of the open time edges, the tail decays only as about Lx⁻⁵** (checked to Lx = 24).
   - The source is the anomaly's own Wilson-line dependence at the edges.
   - The current's divergence must equal the anomaly, so any measure current on this geometry inherits it. It is not a defect of NT-1′'s finite-volume term Q.
5. **Both failures have one cause.** H_W is a Chern insulator, and its edge states have a gap sin(π/Lx) that closes as Lx grows. Changing the measure term cannot remove this. Changing the geometry to periodic time would.

## Results

### (b″) on the RP strip (Lx 4, Lt 8, antiperiodic x, M = 1)

**Edge zero modes (proved: worker's derivation, PREREG §2 A1 and F5).**
- A mode on the boundary row with γ_t χ = ±χ satisfies (D−1)ψ = (1 − cos k′ + iγ_x sin k′)χ, with the hop into the bulk projected out.
- It is an exact zero mode iff e·W_edge ≡ π (mod 2π), for any plaquettes.

**No admissible winding loop (checked).**

| Lx | Admissible loops / sampled | Source |
|---|---|---|
| 4 | 0/17, including 6 P-B kernel nodes | `B2A_Lx4.out:19` |
| 6 | 0/11 | `B2A_Lx6.out:13` |
| 8 | 0/11 | `B2A_Lx8.out:13` |

**The zero modes sit where predicted (checked).**
- At zero plaquettes the gap is ≤ 6e-16 exactly at τ = ½ (charge 1) and at τ = ¼ and ¾ (charge 2) (`B2A_Lx4.out:2`).
- With plaquettes, each zero sits exactly where e·W_edge ≡ π. For example, rand0 gives 0.887 + 2π·0.359 = 3.143 (`B2A_Lx4.out:3`).
- The index changes between the two edge crossings.

**Torus (a different geometry; descriptive; checked).**
- 4×4 torus toron Chern numbers: C_L(1) = −1, C_L(2) = −4, C(11112) = 0, C(L1) = −1 (`B2C_Lx4_Lt4_g24.out:5-6`).
- The spread of the 11112 holonomy over the other toron falls exponentially, at rate ln 2 (`B2C_Lx10_Lt10_g16.out:12`):

| L | Spread (rad) |
|---|---|
| 4 | 1.46 |
| 6 | 0.36 |
| 8 | 0.090 |
| 10 | 0.023 |

### (b′): the tail

| Test | Result | Source |
|---|---|---|
| E1 (fixed test): Lt 8, 6 W-centred random fields per Lx, central links | τ̄ = 8.9e-4, 8.9e-5, 1.8e-5, 4.5e-6 at Lx 4–10. Fit ν = 0.869 ± 0.064 (13.5σ); on Lx 6–10 alone, 0.746 ± 0.104 (7.2σ). L1's Lx·plateau: 0.035, 0.039, 0.0395, 0.0397 | `E1_FIT.out:1-6`, `E1_Lx*.out` |
| E2 (deterministic; zero plaquettes; W0 = 0.3, 0.6), central links | Exponential. The local rate falls from 0.83 to 0.75 by Lx 22. Bulk transport of Q (J_Q) is 0.74; bulk monopole defect 0.693–0.694 (= ln 2). The same at Lt 12 for Lx ≤ 10 | `SUMMARY_E2_W0.3_Lt8.out:2-7,17-18`, `E2_ANALYSIS_Lt12.out` |
| Edge links and edge rows | Algebraic. The local rate falls from 0.89 to 0.22, while rate × Lx settles at 5.0, i.e. about Lx⁻⁵. The edge Wilson-line response of the anomaly scales the same way. W0 = 0.6 gives the same rates | `SUMMARY_E2_W0.3_Lt8.out:8-13` |
| Penetration into the bulk | One row in, edge behaviour takes over by Lx ≈ 20. Two rows in, decay is still exponential at Lx 24 | `E2ROW-2_Lx24.out:7`, `E2ROW-1_Lx24.out:7` |
| L1 contrast | Lx·plateau → 0.0398 = 1/(8π); Lx × edge response → 0.1591 = 1/(2π) | `SUMMARY_E2_W0.3_Lt8.out:20-21` |

**Labelled statements.**
- **Proved (elementary).** If a gauge-invariant current satisfies ∂*j = 𝒜, its response to a Wilson-line shift is at least a quarter of the anomaly's. Lüscher-type locality would force that response below e^(−Lx/2ϱ).
- **Suggested.** Given the checked algebraic edge response, no measure on this geometry meets a uniform exponential bound as Lx → ∞. At Lx = 4 the edge and bulk rates are similar (0.87 against 0.83), so the distinction does not matter numerically there.
- **Reading.** NT-1′'s negative kernels are carried by the modulus |det D(1)|²|det D(2)|^½, which does not depend on the measure. Completing the measure moves λ_min only at second order, through the phase. So this obstruction is about legitimacy, not about the sign mechanism.

## Mechanical status

- **(b″): NOT MET as worded.** The pre-registered consequence is OPEN at (b″) (PREREG §2).
- **(b′): meets the fixed minimal items.** One stricter sub-condition the worker added (L1/11112 ≥ 10 at every size) misses at Lx 4 (9.8×) and holds at Lx 6, 8 and 10. The edge result was registered as descriptive (F1), so it does not change the mechanical (b′).
- **Classification.** This is a genuine obstruction of the open-time geometry, not a defect of NT-1′'s construction.
- **What a fixed-rule reading would need.** A periodic-time geometry with kernels at Lx ≥ 4. K2c's torus code covers Lx = 2 only, so this is new work.

**Scope.**
- Finite 2D U(1), open time, antiperiodic in x, M = 1, charge sets 11112 and L1.
- Sizes: Lx ≤ 24 at Lt 8; Lt 12 only for Lx ≤ 10.
- Fields: zero-plaquette backgrounds for the scaling; 6 random fields per size for E1.
- NT-1′'s one current, with no counterterm scan.
- Errors are finite-difference and fit errors only, not rigorous bounds.

## Deviations

- **PREREG** was written at 14:38Z, before any run. Descriptive add-ons F1–F4 were each registered before running; F5 is the closing log.
- **Two crashes, fixed, with no numbers affected:**
  - a pairing bug in the finite-difference helper crashed the first Lx 12–16 runs, which were rerun;
  - an index-change assertion at Lx 10 crashed E1. That draw now counts as a rejection, and the rerun reproduced the same accepted fields.
- **A memory-lean `dq_dA` was used for Lx ≥ 16.** It equals the original to 2.3e-16 (`LEAN_CHECK.out`), and Lx 16 reproduced every printed digit.
- **Excluded:** the W0 = 0.6 edge runs at Lx ≥ 20 fail the gap gate (gap < 0.1) and are not used.
- **Noise:** the central 22→24 rate (0.688) is near the finite-difference noise floor (about 2e-12 against 5e-11).
- **Not done:**
  - the Kadoh–Kikukawa route (only the abstract was read);
  - the transport test (no admissible loop exists);
  - the kernel step, since (b″) did not pass.
- **Memory:** peak ≤ 424 MB per run.

## Files (`campaign/NT1PP/`)

- `PREREG.md`, with F1–F5.
- `scripts/`. NT-1′'s `nt1p_lib.py` is unchanged (sha1 3ce22737).
  - **Code:** `nt1pp_common`, `_t0`, `_b2a`, `_b2c`, `_e1`, `_e1_fit`, `_e2`, `_e2edge`, `_e2row`, `_e2_analysis`, `_lean`, `_lean_check`, `_run_lean`, `_summary` (`.py`).
  - **Output:** `*.out`.
  - **Data:** `e1_Lx*.npy`, `e2_*.npz`, `e2edge_*.npy`, `e2row*_*.npy`, `b2c_*.npz`, `nt1pp_summary.npz`.
