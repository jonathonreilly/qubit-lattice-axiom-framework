# checks/cw — scripts and outputs for MASS_GAP_CW_CROSSOVER_ATTACK.md

Environment used: Python 3 with numpy 2.5.4, scipy 1.18.1, mpmath 1.4.1, python-flint 0.9.0 (arb). Run from this directory.

| Script | Purpose | Output |
|---|---|---|
| `rigorous_bounds.py` | (1) character-coefficient check a_j = I_{2j+1}/I_1 vs Haar quadrature; (2a) naive ball check [superseded, see below]; (2b) validated-numerics Dobrushin MAD bound; (3) arb Kotecký–Preiss thresholds; (4) truncation tails τ_J(β) | `data/rigorous_bounds_out.txt`, `data/rigorous_bounds.json` |
| `var_certificate.py` | interval certificate Var_∥(κ) < 1/4 on (0, 1.2] (Prop. S) | `data/var_certificate_out.txt`, `data/var_certificate.json` |
| `su2_mc.py` | SU(2) d=4 heat-bath + overrelaxation MC (usage: `L beta ntherm nmeas nor seed outfile [cold|hot]`) | raw `data/su2_L*_b*_*.json` (not committed, ~6.7 MB) |
| `run_scan.sh` | the 40-run scan (`PYTHON=... ./run_scan.sh`) | `data/run_scan_out.txt` (log incl. `time`) |
| `analyze_mc.py` | jackknife plaquette, dP/dβ, Creutz χ(2,2), 0⁺⁺ effective mass, Polyakov loop | `data/mc_summary.txt`, `data/mc_summary.json` |
| (inline, see note §3) | strong/weak-coupling comparison | `data/sc_wc_compare.txt` |

Notes.
- Section (2a) of `rigorous_bounds_out.txt` reports a FAIL from a naive ball evaluation of 1 − R² − 3R/κ (dependency blow-up at small κ).
  It is superseded by `var_certificate.py` (monotone-R cell bounds plus a Taylor bound for κ ≤ 0.0263), which certifies Var_∥ < 1/4.
- The MC scan draws seeds from bash `$RANDOM`; seeds were stored in the raw JSON files, which are not committed. Reruns reproduce the
  numbers statistically, not bit-for-bit. `analyze_mc.py` needs the raw files.
- MC numbers are evidence only (Wilson action, small volumes); they verify nothing about the effective Balaban action.
