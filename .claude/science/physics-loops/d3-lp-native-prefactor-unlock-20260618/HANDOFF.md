# Handoff

Target:
`d3_orbital_response_decomposition_bounded_theorem_note_2026-06-13`

What changed:

- D3 no longer computes its LP integral with a hard-coded scalar described as a
  raw Landau-Peierls input.
- D3 imports `derive_symbolic_prefactor()` from the native-prefactor companion
  runner, checks the returned rational and symbolic residuals, and uses that
  returned value in the Brillouin-zone integral.
- The D3 note now asks review/audit to grade the companion first, then D3 as a
  consumer of that companion plus its own independent finite Peierls reference.

Verification:

```bash
python3 -m py_compile scripts/frontier_landau_peierls_prefactor_native_derivation_2026_06_13.py scripts/frontier_d3_orbital_response_decomposition_2026_06_13.py
python3 scripts/frontier_landau_peierls_prefactor_native_derivation_2026_06_13.py
python3 scripts/frontier_d3_orbital_response_decomposition_2026_06_13.py
```

Results:

- native-prefactor companion: `TOTAL: PASS=8 FAIL=0`
- D3 decomposition consumer: `TOTAL: PASS=10 FAIL=0`

Not done:

- No audit verdicts were run or applied.
- No audit ledger, audit queue, publication status, front-door status, or lane
  registry files were edited.
- No stale existing PR was refreshed against `main`.

Next exact action:
Open the PR and ask the reviewer to extract the science, then audit the
companion-first dependency order if the reviewer accepts the repair shape.
