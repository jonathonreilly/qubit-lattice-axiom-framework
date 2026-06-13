# Handoff

Changed source packet:

- `docs/GRAVITY_PREMISE4_REFRACTIVE_INDEX_FROM_DISPERSION_BOUNDED_THEOREM_NOTE_2026-06-07.md`
- `scripts/frontier_gravity_premise4_refractive_index_from_dispersion.py`

Science move:

- Routes weak-field scalar response through the retained-bounded
  `GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`.
- Adds a runner-checked finite-lattice operator-symbol proof of
  `H->H+phi`.
- Adds a runner-checked fixed-energy eikonal phase-counting proof of
  `n=k/k0`.
- Exposes retained source/Green authorities for the geometric `1/b` form.

Verification:

```bash
python3 -m py_compile scripts/frontier_gravity_premise4_refractive_index_from_dispersion.py
python3 scripts/frontier_gravity_premise4_refractive_index_from_dispersion.py
python3 scripts/cached_runner_output.py scripts/frontier_gravity_premise4_refractive_index_from_dispersion.py --refresh --timeout-sec 120
python3 scripts/cached_runner_output.py scripts/frontier_gravity_premise4_refractive_index_from_dispersion.py --check --timeout-sec 120
```

Expected runner result:

```text
TOTAL: PASS=36 FAIL=0
```

No audit ledger or publication-status file is edited.
