# Handoff

Changed source packet:

- `docs/RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`
- `scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py`

Science move:

- Adds a 2026-06-13 one-hop dispersion bridge lock.
- States the spectral claim as one-particle/free-bilinear.
- Adds runner checks that the d-dimensional free staggered dispersion bridge
  note/runner/cache are present, scoped, passing, and SHA-fresh.

Verification:

```bash
python3 -m py_compile scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py
python3 scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py
python3 scripts/cached_runner_output.py scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py --refresh --timeout-sec 180
python3 scripts/cached_runner_output.py scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py --check --timeout-sec 180
```

Expected runner result:

```text
TOTAL: PASS=10, FAIL=0
```

No audit ledger or publication-status file is edited.
