# OBS-2 report: Lorentz violation from X2's flavour pattern, and the T₂g strain channel

**Readings: LV-PRICE(n), with n = 19 tuned coefficients (14 if set C's counterterm already includes the tetragonal operator). FLAV2-NEAR.**

> **Referee (codex gpt-5.6-sol, 11:51Z): CONFIRMED WITH CORRECTIONS.**
> - **Confirmed independently:** c_TT^d ≈ −2.1e-8 and its sign; LV-SAFE fails robustly on the direct d-quark vector and axial rows; tuning of about 1e-14 is needed.
> - **Not established:** that 19 or 14 is the minimal count. The strict reading is LV-PRICE with n open.
> - **Further corrections:**
>   - the s-quark row depends on an unverified kaon map;
>   - the cited bound row has been corrected;
>   - the up-quark residual enters through Q_L;
>   - CKM alone does not fix the magnitude.
>
> See `REFEREE_VERDICT.md` and `referee/REFEREE.md`.

**Provenance (supervisor's note).** The harness blocks subagents from writing REPORT.md, so the supervisor saved this file from the worker's final message, lightly condensed; every number and file reference is the worker's.
- **Worker:** Claude Opus 5.5 at xhigh, the same model family as the supervisor. Unrefereed.
- **Run windows:** 00:29–00:47Z and 11:22–11:40Z on 2026-10-15. The gap is recorded in `PREREG_FOLLOWUP_2026-10-15.md`.
- **Memory:** peak 169 MB, one process at a time.
- `dl_kr/`, a downloaded copy of the Kostelecký–Russell tables, is not archived, for copyright reasons.

## Plain words

1. **Higgs loops give each generation its own speed, and each corner a preferred direction.**
   - The part shared by all three corners of one field is removed by two cubic-symmetric terms per field:
     - the speed counterterm set C already pays for;
     - a "tetragonal" term, Σ_a σ_a sin p_a (cos p_b + cos p_c). It is checked to be cubic-invariant, and it shifts only the speed along each corner's own axis.
   - The tetragonal term is **not** in set C's count as the gravity PRICE_NOTE states it.
2. **What remains is the flavour pattern.** On branch B it comes only from the down-quark sector, where CKM mixing spoils the circulant pattern. Up quarks and charged leptons are circulant, so their residual cancels exactly.
   - The d quark comes out about 2×10⁻⁸ faster than light. Astrophysics bounds this at 10⁻²² (Kostelecký–Russell Table D44, part 3).
   - The s quark exceeds a kaon bound by 1.5–28×.
   - e, μ, τ, c, b and t are within their bounds.
   - Local counterterms can remove the residual, but only by tuning. That is LV-PRICE.
3. **Side finding (checked): OBS-1's off-diagonal generation masses are themselves Lorentz-violating.**
   - OBS-1 used a spin-blind (π,π,0) condensate. With it, mixed generations move at direction-dependent speeds, with an effect of order (off-diagonal mass)/(mass).
   - Giving the condensate spin along the third axis (τ_x σ_c) makes it exactly Lorentz-invariant. This costs nothing and keeps cubic covariance.
   - This is a fix to the model's completion, not a kill.
4. **T₂g (off-diagonal) shear has no first-order effect on spin-averaged masses** (proved by symmetry; checked to 10⁻¹³). OBS-1's E_g clock row is therefore the full first-order answer: branch B sits at 0.09–2.5× the clock bound.

## Readings (FIXED, TESTS.md:304-320)

### LV-PRICE(n)

**Scope.**
- X2's walker on Z³, continuous time, at one loop.
- A Dirac-embedded Yukawa pair, and a nearest-neighbour lattice Higgs in the symmetric phase.
- Corner-selective Yukawa symbols g_c = (1 − cos k_c)/2, plus an on-site symbol.
- OBS-1's bilinear mirror proxy Δ·f_NN, with Δ ∈ {0, 0.5}.
- IR regulators m0 = mH ∈ {0.1, 0.05, 0.025}, and three vertex placements.

**Error estimate.** The spread over these 18 variants is about ×4. The headline residuals converge in N to better than 2% between N = 48 and 96 (`sizes2_M2.out:2-7`).

**LV-SAFE fails on branch B (checked):**
- **d quark:** c_TT = −2.2e-8 (range −0.9 to −3.5e-8) at low-scale couplings, and −(1.8–7.1)e-9 with Planck-scale couplings. The sign is negative in every variant (`sign_check.out`).
  - The bound row is Table D44 part 3, "c_TT^d > −1×10⁻²²" (Astrophysics [100]*, [22]*, [325]*).
  - It is exceeded ×2e13–3.5e14 (`sizes2_A.out:17,27`; the Planck bracket is at `:72` onward).
- **s quark:** c_TT = +(0.7–2.8)e-8, against Table D44 part 4, |c_K| < 1e-9 (Astrophysics [90]*). That is ×1.5–28. The mapping from kaon to valence quark is suggested.
- **u/d anisotropy:** about 1e-9. It exceeds the nucleon comagnetometer rows (Tables D15 and D11 [115], about 1e-29) only through a suggested parton mapping. It is within the direct quark DIS rows (D44 part 1, about 3e-4).
- **e, μ, τ, c, b, t:** within their bounds.
  - Charged-lepton residuals from Y_e are exactly 0 (circulant); only Y_ν remains, at about 10⁻²⁷.
  - Rows: D6 (trapped Yb⁺ [64], about 8e-21), D28, D30, and D44 part 4 (c_D, c_B, c^t).

**Not LV-KILL.** The residual consists of local, translation-invariant, G_SM-invariant, corner-selective kinetic terms. These counterterms remove it:

| Counterterm | Coefficients | Tuning | X2-symmetric? |
|---|---|---|---|
| (a) Flavour-pattern operators, δH = Σ_{c,a} κ_{ca} ψ_f† σ_a sin k_a g_c(k) ψ_f, on Q and d^c | 7 real coefficients per field after the universal part: 14 | 3e-15 to 6e-14 of the residual (d row); about 1e-19 for the nucleon-mapped anisotropy (suggested); 0.04–0.7 (s) | Range √2–2. Cubic-covariant only when written with the flavour spurion (a flavon or a spontaneous completion). With explicit Yukawa symbols they break cubic rotations exactly as those symbols already do. |
| (b) Tetragonal operator, Σ_a σ_a sin p_a (cos p_b + cos p_c), one per charged field (Q, u^c, d^c, L, e^c) | 5 | ≲1e-16 (electron) to about 1e-25 (quarks, suggested mapping) | Yes. A₁, checked to 9.9e-16 over all 24 rotations. At each hw1 corner it shifts v_∥ by 2β and leaves v_⊥ alone (`ct_check.out`). |

- **How (b) is counted.** Set C's speed counterterm alone cannot remove the corner-universal tetragonal part. OBS-1 REPORT:76 counts it inside "set C's cubic counterterm", while the gravity PRICE_NOTE:313 lists only speed counterterms. Hence n = 14 + 5 = 19, or 14 if (b) is counted as existing.
- **Robustness.** Spending set C's per-field speed counterterm on zeroing the d quark instead leaves the s quark at about +4e-8, ×40 over the kaon row. No allowed reallocation gives LV-SAFE.

### FLAV2-NEAR

**T₂g = 0 at first order for spin-averaged masses (proved, unrefereed).**
- **Diagonal corner masses.** Each hw1 corner's little group is D4, or D2 with a selective symbol. It has no invariant that pairs a scalar mass with T₂g strain.
- **Off-diagonal (π,π,0) entries.** C2x and C2y forbid a T₂g response in the entry's own spin channel. Any other spin component that the strain induces is traceless in the common Lorentz frame, so it gives no first-order spin-averaged shift.
- **Checked** on the Yukawa loop with the SF flow:
  - every T₂g derivative of a corner mass is ≤1.7e-15 (`strain_N48_m0.1_D0.5.out`, `strain_N32_m0.1_D0.0.out`);
  - the off-diagonal own-channel derivatives are ≤1.5e-13 for B = τ_x, τ_xσ_z and τ_xσ_x (`offd_N24/32_*.out`).

**Clock row, E_g + T₂g.** TW-2's estimator, unchanged (`sizes2_B.out:46-52`):

| Branch | Registered τ_x completion | Covariant τ_xσ_c completion |
|---|---|---|
| B trace | ×0.118–0.447 | ×0.089–0.34 |
| B selective | ×0.65–2.46 | ×0.62–2.35 |
| A | ×80–357 | ×80–357 |
| B′ | ×2.2–93 | ×2.9–96 |

- The registered column reproduces OBS-1 to every printed digit.
- Branch B is within 10×, so the reading is NEAR. No branch is below 1e-2, so it is not SAFE.
- The scope is OBS-1's: U(1) stand-in, bilinear mirror proxy, SF strain, one loop.

## Controls (all passed)

- **OBS-1 reproduced:** leak L0 = 8.209558e-2 at N = 32, identical to OBS-1 (`ctl_leak_N32.out:8`). U(1) Ward residual 1.1e-16 (`ctl_loop_N24.out:2`).
- **Yukawa analogue of the Ward check, the continuum log:** halving m0 changes Σ1 by −4.50e-3 and −4.46e-3, against the continuum −(ln 4)/32π² = −4.39e-3. The velocity part changes by the opposite amount, so the IR log is Lorentz-invariant (`ana_kin.out:12,15`).
- **Cubic covariance:** C3 about [111] permutes the results to ≤8.4e-15 absolute. Off-diagonal velocities are ≤3.9e-15 (`ana_kin.out:5-8`).
- **Staggered reflection:** with an on-site vertex at Δ = 0, K = 3.5e-16, and the hw1 corner equals the origin (`ana_kin.out:3`).
- **N-convergence:** the loop tables change by ≤11% from N = 48 to 96 (`ana_kin.out`); the headline residuals by under 2%.

## Further results

- **Universal part (i)**, branch B trace, low-scale couplings (`sizes2_A.out:6-10`). Gauge loops add OBS-1's K_v = 6.2e-3·e² at Δ = 0.5.

  | Field | Speed shift | Tetragonal shift |
  |---|---|---|
  | Q | −1.28e-3 | +2.4e-5 |
  | u^c | −2.55e-3 | +4.9e-5 |
  | d^c, L, e^c | 10⁻⁶ to 10⁻⁹ | — |

- **Branches A and B′ are far over** (`sizes2_A.out:31-68`). For example: the top quark's c_TT is about 5e-3 against a bound of 1.6e-7, and the electron's is about 3e-7 (A) or 3e-8 (B′) against 5e-21.
- **Dimension-3 side finding (checked).**
  - Exact Bloch block with the spin-blind condensate: E² − m² − q² = ±0.385 q² along x and y, and 0 along z (`lv3.out:1-6`).
  - With σ_z the same block is exactly isotropic (`:7-12`).
  - In the flavon loop, the spin-blind vertex's anisotropy grows by 2·(ln 4)/16π² per halving of m0. The σ_c vertex gives exactly the isotropic on-site value at Δ = 0 (`flav_N96_*.out`).
- **Comparator M2:** off-diagonal entries carried by covariant flavons, with the flavon vev set equal to v (a choice). Branch B gives d c_TT = −1.1e-8 and s = +8.9e-9: the same order and sign as M1, so the two add rather than cancel (`sizes2_M2.out:9`).
- **Couplings.**
  - Low-scale: y = m/v with v = 174.1 GeV, giving y_t = 0.99, y_b = 0.024 and y_τ = 0.0102 (OBS-1's inputs).
  - Planck-scale bracket: quark Yukawas ×0.45 (recalled SM running); leptons ×1.
- **Loop-order caveat.**
  - One loop only: no y²g² or y⁴ terms.
  - The slow logarithmic flow from 1/a down to observed energies is not included. Main's `LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md` puts that at most a few orders.
  - The Yukawa loop's own E_g strain contribution is about 10⁻⁴ of the gauge term (suggested estimate).

## Prior art (counted once)

- **Main's `LORENTZ_NATURALNESS…2026-06-06.md`:** the Collins-type speed problem. It is the flavour-blind part here.
- **`TASTE_SECTOR_MARGINAL_LV_B4…2026-06-13.md`:** per-taste anisotropy that cancels only across the orbit. It is the precedent for the corner-universal tetragonal part.
- **Not found on main:** any Yukawa-induced Lorentz violation at the corners.
- **`SUPERVISOR_OWN_THREAD.md`** was read after the gap. It estimated n ≈ 6, with LV-SAFE possible.
  - The computed branch-B residual is far smaller than y_t²·K_v, because the up sector is circulant.
  - It still exceeds the d-quark astrophysical row.

## Deviations (all in `PREREG_FOLLOWUP_2026-10-15.md`)

- **m0 = 0.025:** this point was added before any of its runs.
- **First M2 grid:** it was clustered at q = 0 and under-resolved the flavon. It was discarded and rerun clustered at Q, before any number was read.
- **Added after the PREREG:**
  - `lv3.py`, `r1_offdiag_sz.py` and `ct_check.py`;
  - exact C3 symmetrisation of the loop tables, which removed a spurious 6e-20 electron roundoff;
  - the nucleon- and meson-mapped bounds (labelled suggested).

## Files (`campaign/OBS2/`)

- `PREREG.md` and `PREREG_FOLLOWUP_2026-10-15.md`.
- In `scripts/`:
  - `yuk_lv.py`: the loop code (modes kin, strain, offd, flav);
  - `ana_kin`, `sizes2`, `sizes2_B`, `sizes2_M2`, `sign_check`, `lv3`, `ct_check` (`.py` / `.out`);
  - `obs1_copy/`: OBS-1's code plus `r1_offdiag_sz.py`;
  - the `kin_*`, `flav_*`, `strain_*`, `offd_*` and `offdiag_sz_*` outputs and their JSON files;
  - `obs2_archive.npz`: 1,700 arrays, which reproduce the readings.
