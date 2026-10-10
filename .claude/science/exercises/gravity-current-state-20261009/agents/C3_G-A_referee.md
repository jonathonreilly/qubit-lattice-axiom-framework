# C3 lane G-A: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-10)

Completed the independent referee audit.

**Verdict: FAIL**, narrowly scoped to the fixed-coordinate coupling and ensemble-RMS noise specified by G‑A.

Key rulings:

- The Last–Penrose second-chaos bound and Rosen causal-order formula check out.
- Local BD alone triggers FAIL; the imported \(\ell_k\le10^{-19}\,\mathrm m\) bar is not required.
- Smeared BD is FAIL through \(\ell_k\approx3.15\times10^{-19}\,\mathrm m\), then INCONCLUSIVE.
- Variance does not establish typical-realization behavior.
- Pure-gauge crackle is a coupling artefact: co-moving points and window give \(\Delta S\equiv0\).
- This is not a gauge-invariant no-go for order-based gravitons.

Files:

- [REFEREE_VERDICT.md](REFEREE_VERDICT.md)
- [referee_checks.py](referee_checks.py)