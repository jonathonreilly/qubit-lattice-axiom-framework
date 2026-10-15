# OBS-2 dated follow-ups to PREREG.md (PREREG.md itself is unedited)

## 2026-10-15 11:23Z

1. **Gap.** Work stopped at about 00:47Z when the supervisor's session ended, and resumed at 11:23Z on the
   coordinator's instruction (new deadline 14:00Z). Finished before the gap: control 1 (OBS-1 leak
   reproduced, `scripts/ctl_leak_N32.out`), the Ward residual of the copied U(1) code
   (`scripts/ctl_loop_N24.out`), and every registered `kin` run (N = 24, 32, 48, 64, 96; m0 = mH = 0.1,
   0.05, 0.025; Delta = 0, 0.5; `scripts/kin_*.out`, `yuk_kin_*.json`, `run_kin.done`). These are not rerun.
   No result had been read out before the gap. The m0 = 0.025 point was added to the registered 0.1/0.05
   before those runs started (an extra IR point for the m0 -> 0 extrapolation; registered values unchanged).
2. **File found in my folder.** `SUPERVISOR_OWN_THREAD.md` (timestamp 20:31 local = 00:31Z) is the
   supervisor's independent estimate, written before my PREREG. I read it after the gap. It changes no
   registered rule.
3. **Bounds source.** arXiv:0801.0287 v19 (5 Feb 2026) PDF saved untrusted in `dl_kr/`; text is extracted
   with PyMuPDF under `python3 -I`, reading only.

## 2026-10-15 11:35Z (additions after the first post-gap runs; reading rules unchanged)

4. **Comparator M2 run** (registered "if time"). First run used the q = 0-clustered grid, which under-resolves the
   flavon's light point Q; kept in `scripts/flav_v1_unclustered/` and not used. Rerun with the grid clustered at Q
   (v2, `flav_N*.out`) before any M2 number was read.
5. **Added (not registered):**
   - `lv3.py`: exact Bloch-block test of the spin structure of an hw2-momentum off-diagonal mass (dimension-3 LV check).
   - `obs1_copy/r1_offdiag_sz.py`: OBS-1's gauge-loop E_g off-diagonal coefficient with the covariant tau_x sigma_z
     condensate (N = 24-64), to recompute the clock row for that completion.
   - `ct_check.py`: cubic invariance and corner action of the tetragonal counterterm.
   - Assembly imposes exact C3[111] covariance on the loop tables (measured violation <= 8e-15 absolute) to
     remove roundoff from exactly symmetric sectors (it had produced a spurious 6e-20 electron residual).
   - Bounds: besides direct quark rows (Table D44), nucleon rows (D11/D15) and meson rows (D44 part 4) are used
     with a parton/valence mapping, labelled SUGGESTED wherever used.
6. OBS-1's registered clock numbers are reproduced to every printed digit by `sizes2_B.py` (second control).
