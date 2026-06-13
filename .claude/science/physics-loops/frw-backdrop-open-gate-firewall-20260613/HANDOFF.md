# Handoff

Changed source packet:

- `docs/FRW_ADIABATIC_EXPANSION_COSMOLOGICAL_BACKDROP_OPEN_GATE_NOTE_2026-05-28.md`
- `scripts/frontier_frw_adiabatic_expansion_cosmological_backdrop_open_gate.py`

Science move:

- Adds `Downstream Source-Boundary Firewall`.
- Strengthens the runner from `PASS=48` to `PASS=57`.
- Blocks downstream retained-use claims for C1-C3, FRW dynamics, entropy
  conservation / adiabatic expansion, observational cosmology parameters, and
  parent theorem status.

Verification:

```bash
python3 -m py_compile scripts/frontier_frw_adiabatic_expansion_cosmological_backdrop_open_gate.py
python3 scripts/frontier_frw_adiabatic_expansion_cosmological_backdrop_open_gate.py
python3 scripts/cached_runner_output.py scripts/frontier_frw_adiabatic_expansion_cosmological_backdrop_open_gate.py --refresh --timeout-sec 120
python3 scripts/cached_runner_output.py scripts/frontier_frw_adiabatic_expansion_cosmological_backdrop_open_gate.py --check --timeout-sec 120
```

Expected runner result:

```text
TOTAL: PASS=57 FAIL=0
```
