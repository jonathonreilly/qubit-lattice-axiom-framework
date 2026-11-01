# checks/cw — scripts and outputs for MASS_GAP_CW_CROSSOVER_ATTACK.md

**These scripts support no proved statement.** Every number they produce is used in the notes only as (i) evidence for an
explicitly named Open Lemma, (ii) a "Computed observation", or (iii) numerical evidence in Appendix N ("Numerical evidence
(not used in any proof)"). No theorem, proposition or lemma marked proved in MASS_GAP_CW_CROSSOVER_ATTACK.md or
MASS_GAP_CROSSOVER_REDUCTION.md depends on any of them. The scripts are kept for reproducibility.

Environment used: Python 3 with numpy 2.5.4, scipy 1.18.1, mpmath 1.4.1, python-flint 0.9.0 (arb). Run from this directory.

| Script | Purpose | Role in the notes | Output |
|---|---|---|---|
| `rigorous_bounds.py` | (1) character-coefficient check a_j = I_{2j+1}/I_1 vs Haar quadrature; (2a) naive ball check [superseded, see below]; (2b) MAD grid bound; (3) arb Kotecký–Preiss thresholds; (4) truncation tails τ_J(β) | (1) cross-check of a proved identity (not used); (2b) computed observation O-MAD (Conjecture S♯); (3) computed observation O-KP; (4) computed observation O-τ | `data/rigorous_bounds_out.txt`, `data/rigorous_bounds.json` |
| `var_certificate.py` | ball-arithmetic evaluation of Var_∥(κ) < 1/4 on (0, 1.2] | evidence for **Open Lemma OL-S1** only; Prop. S is stated as conditional on OL-S1 | `data/var_certificate_out.txt`, `data/var_certificate.json` |
| `su2_mc.py` | SU(2) d=4 heat-bath + overrelaxation MC (usage: `L beta ntherm nmeas nor seed outfile [cold|hot]`) | Appendix N evidence | raw `data/su2_L*_b*_*.json` (not committed, ~6.7 MB) |
| `run_scan.sh` | the 40-run scan (`PYTHON=... ./run_scan.sh`) | Appendix N evidence | `data/run_scan_out.txt` (log incl. `time`) |
| `analyze_mc.py` | jackknife plaquette, dP/dβ, Creutz χ(2,2), 0⁺⁺ effective mass, Polyakov loop | Appendix N evidence | `data/mc_summary.txt`, `data/mc_summary.json` |
| (inline, see note Appendix N) | strong/weak-coupling comparison | Appendix N evidence | `data/sc_wc_compare.txt` |

Notes.
- Section (2a) of `rigorous_bounds_out.txt` reports a FAIL from a naive ball evaluation of 1 − R² − 3R/κ (dependency blow-up at
  small κ) and then prints the line "certified Dobrushin: q(beta) = 9 beta" unconditionally; that line is not supported by
  section (2a) (open item OI-2 in the attack note). Section (2a) is superseded by `var_certificate.py` (monotone-R cell bounds
  plus a Taylor bound for κ ≤ 0.0263), whose output is evidence for Open Lemma OL-S1, not a proof used in the notes. It has not
  been independently re-run or reviewed.
- Part (4) sums the terms 2j ≤ 79 with ball arithmetic and adds no bound for the omitted tail; the τ_J values are computed
  values, not certified bounds (open item OI-1).
- The MC scan draws seeds from bash `$RANDOM`; seeds were stored in the raw JSON files, which are not committed. Reruns reproduce
  the numbers statistically, not bit-for-bit. `analyze_mc.py` needs the raw files.
- MC numbers are evidence only (Wilson action, small volumes); they verify nothing about the effective Bałaban action.
