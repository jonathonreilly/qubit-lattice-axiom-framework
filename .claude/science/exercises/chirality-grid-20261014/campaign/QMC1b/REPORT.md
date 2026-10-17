**Provenance:** the worker's final message, saved verbatim by the supervisor.

# QMC-1b report: is the GPR-like signal set by the corner filter?

**Fixed reading: OPEN.** The new filter f_Γ never reaches the required suppressed window at the registered couplings W = 2 and 4, so neither FILTER-SENSITIVE nor FILTER-ROBUST can be read.

Worker: Claude Opus 5.5 at xhigh (same family as the other agents, so not independent). Unrefereed. Window: 11:23Z–22:45Z on 2026-10-17.

## Plain-words summary

1. **The engine still works with the new filter** (checked). All four validation gates passed again before production:
   - no interaction gives free particles exactly;
   - every weight is real and positive;
   - two reduced-flavour versions match exact diagonalisation, one of them with the negative filter taps that f_Γ uses;
   - the light corner stays exactly free in every configuration.
2. **The new filter does not make all the mirrors heavy at the registered couplings** (checked).
   - f_Γ = (2 − cos p_x − cos p_y)/4 leaves Γ light. Of its three mirror corners, (π,π) has filter value 1 and gets suppressed. The other two, (π,0) and (0,π), have filter value ½ and stay largely unsuppressed at W = 2 and 4.
   - The pre-registered suppression test therefore fails at both couplings, already at L = 4. With no window to compare, the fixed reading is mechanically OPEN.
3. **The old filter f2 reproduces QMC-1's pattern with 4× the statistics** (checked).
   - Once the mirrors are suppressed, the 10-vector correlation per site barely shrinks from 4×4 to 6×6: ratios 0.963(28) at W = 2 and 0.865(37) at W = 4.
   - For comparison, the free value is 0.54 and the short-range value is 0.44.
   - QMC-1's W = 4 value of 1.35(26) came down to 0.865(37) at the smaller time step and longer chain. It still sits on the GPR-like side of the 0.85 line, but only just.
4. **Supplementary, not a fixed reading.** At W = 8 both filters suppress every mirror, and their size ratios agree within errors: f_Γ 0.805(63), f2 0.861(47). The f2 6×6 run stopped at 171 of 200 sweeps at the wall-clock limit.
   - So where a matched comparison exists, the box-spanning correlation does not look filter-specific (suggested).
   - But W = 8 is outside the registered set, and f_Γ's 0.805 sits between the two thresholds.
5. **Neither reading would establish a gap, SMG or GPR**, and none is claimed.

## Reading (fixed text: TESTS.md:667-678; operational definitions: PREREG.md §6–7)

**Scope:**
- Model: the ungauged 2+1D analogue of the X2 λ1 = 0 matter Hamiltonian, global Spin(10).
- Lattice: periodic L = 4 and 6, β = 4, Δτ = 0.05, n_s = 8.
- Statistics: single chains of 200 measured sweeps.
- Errors: σ = max(binning error with 20 bins, binning error with 10 bins).

| Filter, W | E3w at L4 (primary) | E3w at L6 | Window? | S10/L² at L4 → L6 | Ratio |
|---|---|---|---|---|---|
| fΓ, 2 | 1.134(7) | not run (queue rule) | no | 4.09(10) → – | – |
| fΓ, 4 | 0.182(7) | not run | no | 5.10(30) → – | – |
| f2, 2 | 0.082(6) | 0.063(8) | yes | 3.564(53) → 3.432(87) | **0.963(28)** |
| f2, 4 | 0.001(8) | 0.011(11) | yes | 5.068(152) → 4.383(135) | **0.865(37)** |

Sources: `scripts/runs/readout_final2.out:6-7, 27-33`.

**Mechanical reading: OPEN**, because no f_Γ window exists. The f2 half of either reading holds: f2 is ≥ 0.85 at every f2 window.

**Which f_Γ mirrors stay unsuppressed** (checked; registered secondary, PREREG §6). E3w by corner class at L4:
- W = 2: (π,π) 0.051; (π,0)/(0,π) 1.675.
- W = 4: (π,π) −0.013; (π,0)/(0,π) 0.279.

The mirrors at filter value ½ are the ones that stay light. This is a filter-induced hierarchy (reading).

**Free references** (one exact sweep at W = 0):
- f2: 0.541 → 0.294, ratio 0.544.
- f_Γ: 0.640 → 0.319, ratio 0.499.

## Supplementary W = 8 (follow-ups B–D; cannot change the fixed reading)

- **How it was added.** It was pre-registered after the queue log showed f_Γ failing at W = 4. At that point no other observable had been read.
- **First attempt discarded.** All four W = 8 runs at n_s = 8 failed gate (ii-b): max phase 2.3e-7 to 4.4e-7, from roundoff growth over 8 strong time slices. Per the PREREG they are discarded; they are archived in `runs/discarded_ns8_W8/`. For the record, their ratios were 0.843 (f_Γ) and 0.838 (f2).
- **Rerun at n_s = 4.** Gate (ii-b) passes: max phase ≤ 1.1e-9.

| Filter | E3w at L4 → L6 | S10/L² at L4 → L6 | Ratio | Sweeps (L4/L6) |
|---|---|---|---|---|
| fΓ | 0.009(5) → 0.013(5) | 5.35(24) → 4.31(27) | 0.805(63) | 200/200 |
| f2 | −0.000(4) → 0.001(4) | 4.92(23) → 4.24(11) | 0.861(47) | 200/**171, incomplete** |

Source: `readout_final2.out:36-37`.

The two ratios differ by 0.06 ± 0.08 (checked). Applying the fixed thresholds to W = 8 alone would give neither pattern, and the f2 6×6 run is incomplete anyway.

## Systematics (checked)

- **Spin(10) direction pinning persists at Δτ = 0.05.** The share of S10 in the (9,10) plane is 0.57–0.82 for W ≥ 4, against 0.2 if isotropic. At W = 2 it is near-isotropic (0.20 at L4, 0.31 at L6). Readings use the component sum, as QMC-1 did; no Δτ → 0 extrapolation was made.
- **β = 4 is a finite temperature.** Mermin–Wagner forbids true continuous order in 2D at T > 0, so a flat ratio means a long correlation length, not a condensate. E3w bounds low-energy spectral weight; it is not a gap estimator (REFEREE.md:194-224).
- **Autocorrelation is short:** τ_int(S10) is 0.5–3.2 sweeps. The drift by thirds stays within errors.
- **Gates (ii-b) and (iv) hold in every kept run:** max phase ≤ 1.1e-9, light-corner deviation ≤ 1.5e-13 (`readout_final2.out:24`).

## Validation gates, re-passed before production (checked; PREREG follow-up A)

| Gate | Result | Source |
|---|---|---|
| (i) W = 0 free G | 4.9e-15 (f2 L4), 4.9e-15 (fΓ L4), 6.4e-15 (fΓ L6) | `runs/gates_i_iia.out` |
| (ii-a) random-field weights, fΓ L4 | phase ≤ 1.6e-14; T2 commutes with each slice to 8e-16 | same file |
| (iii) reduced flavours vs ED, 1D L = 3, W = 2, 6000 sweeps | f1: 0.09, 1.30, 0.26σ; g1 (negative taps): 1.61, 1.06, 0.61σ, for W⟨Q⟩, ΣS and E_kin | `runs/gate3_compare.out` |
| (iv) light corners | ≤ 1.5e-13 per configuration in every kept run | `readout_final2.out:24` |

## Deviations

1. **Engine changes** (disclosed in PREREG §3 before any run):
   - **f_Γ and g1 filters added.**
   - **Two speed changes that leave the arithmetic unchanged:** a matmul DFT and an in-place zgemm update. Against QMC-1's engine they give identical accept sequences and G equal to 1.9e-13 (`equiv_check.out`).
   - **Alternating up/down sweeps.** These are MCMC-valid but change the sampling order. They were adopted only after the wrap check passed at ≤ 1e-12 and gate (iii) passed.
   - **Stack-memory release.** No arithmetic change.
   - **Thinned diagnostics:** S(π,π) and ⟨WQ⟩ are measured every 4th sweep.
2. **Before the PREREG** I ran engineering-only checks: two timing profiles and a benchmark. No observable was read from them.
3. **One parse check ran outside capped.sh**, concurrently with a run: `python3 -c ast.parse`, a few milliseconds.
4. **A shell heredoc mistake.** Unquoted backticks in the follow-up A text tried to execute paths. Each failed with "no such file", so nothing ran. The text was corrected in the same minute (noted in follow-up A).
5. **Readout scope.** The "f2 gives ≥ 0.85" clause was read as "at every f2 window" (PREREG §7). The same-W alternative is moot, because f_Γ has no window.
6. **Run order.** Production L4 runs used 20 warm-up sweeps; L6 runs used 10. Per the queue rule, no L6 f_Γ run was made at W = 2 or 4.

## Files (all under `.../chirality_ex/campaign/QMC1b/`)

- **`PREREG.md`**, stamped 11:40Z, with follow-ups A–E.
- **`scripts/`:**
  - engine and model: `afqmc.py`, `runner.py`, `x2model.py`, `ed_exact.py`;
  - analysis: `analysis_b.py`, `readout_b.py`, `queue_b.py`, `e3w_of.py`;
  - checks: `validate_b.py`, `gate3_compare.py`, `equiv_check.py`/`.out`, `test_alternate*.py`/`.out`, `test_mem_L6.*`;
  - drivers: `gates.sh`, `production.sh`, `supplementary.sh`, `supp_ns4.sh`;
  - engineering profiles: `prof/`.
- **`scripts/runs/`:** every `.npz` and log; the readouts `readout_final.out` and `readout_final2.out`; the run history in `production_driver.log`; the discarded n_s = 8 W = 8 runs in `discarded_ns8_W8/`.

No process of mine is running. The two Python processes still on the machine belong to other sessions (`cl3-review`, a codex worktree).