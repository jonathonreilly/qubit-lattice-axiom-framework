**Same-family referee record for QMC-1b** (Claude Opus 5.5 checking a Claude Opus 5.5 worker, so this is not independent)

**VERDICT: CONFIRMED WITH CORRECTIONS.**

**Correct fixed reading: OPEN.** f_Γ has no suppressed window at W = 2 or 4, so neither FILTER-SENSITIVE nor FILTER-ROBUST can be read.

### Checks

- **Engine arithmetic.**
  - `equiv_check.out:7-8`: accept counts are identical (2186/2560, 2176/2560), the fields agree exactly, and max|ΔG| is 9.7e-14 and 1.9e-13. I read the diff against `QMC1/scripts/afqmc.py`. The matmul DFT and the in-place zgemm (`afqmc.py:183-189, 306-314`) compute the same thing.
  - The equivalence check covers upward sweeps only. The alternating sweeps are covered separately: the wrapped-vs-fresh deviation is ≤ 1e-12 (`test_alternate2.out:7-8`) and gate (iii) passes.
- **Gates.** These are confirmed from the outputs:
  - (i) 4.9e-15 to 6.4e-15 (`gates_i_iia.out:6-8`);
  - (ii-a) phase ≤ 1.6e-14;
  - (iii) every observable within 1.61σ of ED, including g1 with negative taps (`gate3_compare.out:1-6`);
  - (ii-b) and (iv) hold in every kept run: phase ≤ 1.1e-9, light-corner deviation ≤ 1.5e-13 (my recompute).
- **Readout.** I recomputed it from the npz files with my own script (`ref_QMC1b_sf/recompute.py`), which does not import the worker's code. Every value matches `readout_final2.out:12-37`:
  - f2: ratios 0.9630(283) and 0.8648(372); E3w 0.0821(61) and 0.0630(75) at W = 2, 0.0010(76) and 0.0105(109) at W = 4.
  - f_Γ at L4: E3w 1.1340(68) at W = 2 and 0.1818(71) at W = 4.
  - W = 8: 0.8051(629) and 0.8612(466); difference 0.056 ± 0.078.
- **Why OPEN is right.** f_Γ at W = 4 fails the precondition under every definition: primary 0.182, s-block 0.190, about 11σ above 0.1. FILTER-ROBUST would hold only on a vacuous reading of "every window W". PREREG.md:134 excluded that reading before any data (stamp at PREREG.md:159).

### Findings

1. **"Not filter-specific" is overclaimed** (REPORT.md:25; TESTS.md:776).
   - The comparison is at W = 8, which is outside the registered set and was added after f_Γ failed at W = 4.
   - The f2 L6 chain is incomplete (171 of 200 sweeps).
   - The 2σ resolution of the difference is 0.157, and a 0.11 gap between a 0.75 and a 0.86 ratio would show at only 1.4σ. The test cannot resolve a difference the size of the gap between the readings' thresholds.
   - Equal W does not mean equal effective coupling at the mirrors: two of f_Γ's three mirrors have f = ½.
   - Allowed wording: no filter dependence was detected, and none is excluded.
2. **The n_s = 4 rerun was registered after the full readout.** Follow-up D (PREREG.md:203-217, 18:44Z) was written one minute after `readout_final.out` (mtime 18:43:03Z). That readout already held the fixed f2 ratios and the discarded W = 8 ratios (0.843 and 0.838).
   - REPORT.md:59 ("no other observable had been read") is true only of follow-up B (12:40Z). Follow-up B itself checks out: it came after only the fG W4 queue line (`production_driver.log:11`) and before any W = 8 run (15:31Z).
   - Mitigation: the rerun was forced by the gate and only n_s changed. It also moved the two ratios apart (from 0.005 to 0.056), so it was not selected to make them agree.
3. **Undisclosed deviation in the rerun driver.** `supp_ns4.sh:9-10` drops follow-up B's rule that an L6 run needs at least 2.3 h left (`supplementary.sh:25-26`). Follow-up D says "same rules as follow-up B otherwise" (PREREG.md:212). L6 f2 W8 started at 20:45Z with 1 h 50 min left (`production_driver.log:39`), so under the inherited rule it would not have run. The only matched f2 W = 8 point therefore comes from a run the rule says to skip.
4. **Factual error** (REPORT.md:60). The discarded n_s = 8 runs' max phase spans 5.9e-8 to 4.4e-7, not "2.3e-7 to 4.4e-7". The L4 fG run had 5.9e-8 (PREREG.md:208).
5. **"Barely shrinks" is too strong at W = 4** (REPORT.md:20). 0.865(37) is 3.6σ below 1, and the two W = 8 ratios are about 3σ below 1. The W = 4 value is only 0.4σ above 0.85 (REPORT.md:45 holds only on central values).
   - The causal claim that QMC-1's 1.35(26) "came down … at the smaller time step and longer chain" (REPORT.md:22) is unsupported. The two values differ by 1.8σ, which statistics alone explain.
6. **Errors may be optimistic** (REPORT.md:76).
   - For fG L4 W4 (τ_int 3.2) and fG L6 W8, the 5-bin error does not plateau: 0.40 against the quoted 0.30, and 0.38 against 0.27. With 5-bin errors the f_Γ W = 8 ratio's σ is about 0.083.
   - The discarded n_s = 8 chains are independent replicas of the same physics. All four of their S10/L² values sit below the kept ones, fG L4 by 1.9σ (4.775(171) against 5.353(243)). The ratios do replicate.
   - None of this affects the fixed reading.
7. **Minor.** Follow-up A says the gates ran "with the production engine" (PREREG.md:163). In fact the memory edit (afqmc.py mtime 11:48:47Z) came after the gates (11:43–11:47Z).
   - The edit only sets consumed stack entries to None (`afqmc.py:332-333, 353-354, 391`), so it can only crash or compute the same thing.
   - The wrap check was re-run afterwards (`test_alternate2.out`).
   - The impact is nil, but the wording is inexact.

### Strongest correct statement

Scope: the ungauged 2+1D X2 λ1 = 0 analogue, global Spin(10), β = 4, Δτ = 0.05, L = 4 and 6, single 200-sweep chains.

- The engine is validated. The speed changes leave the arithmetic unchanged, and the alternating sweeps are checked by the wrap test and against ED.
- f_Γ fails the suppression precondition at W = 2 and 4. Its (π,0) and (0,π) mirrors, at filter value ½, stay light: L4 E3w 1.68 and 0.28. So the fixed reading is OPEN.
- f2 reproduces QMC-1 with ratios 0.963(28) and 0.865(37). These are far from the free value 0.54 and the short-range value 0.44. The W = 4 ratio is resolved below 1 and is not resolved from 0.85.
- At W = 8 (supplementary, post hoc, one chain incomplete), both ratios are about 0.81–0.86 and about 3σ below 1. Their difference, 0.06(8), detects no filter dependence but is too coarse to exclude one.
- Nothing here bears on a gap, SMG or GPR.

My only files are `.../chirality_ex/ref_QMC1b_sf/recompute.py` and its outputs; no repository was edited. Everything ran as short single processes with OMP_NUM_THREADS=2.