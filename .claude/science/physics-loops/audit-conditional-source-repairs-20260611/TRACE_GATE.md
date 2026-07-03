# Trace Gate

## Commands run

```bash
python3 scripts/probe_kawamoto_smit_phase_forcing.py
python3 scripts/axiom_first_single_clock_codimension1_evolution_check.py
python3 scripts/frontier_hierarchy_dimensional_compression.py
python3 scripts/frontier_quark_generation_equivariant_ward_degeneracy_no_go.py
python3 scripts/frontier_taste_scalar_fermion_cw_isotropy_narrow.py
python3 scripts/frontier_koide_taste_cube_cyclic_source_descent.py
python3 scripts/frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17.py
python3 scripts/pauli_exclusion_check.py
python3 scripts/frontier_coulomb_stability_scaling_repair.py
python3 scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py
git diff --check
```

## Results

- Kawamoto-Smit: `TOTAL: PASS=47 FAIL=0`
- Single-clock: `TOTAL: PASS=42 FAIL=0`
- Hierarchy dimensional compression: `SCORECARD: 5 pass, 0 fail out of 5`
- Quark generation Ward no-go: `TOTAL: PASS=44, FAIL=0`
- Taste-scalar CW isotropy: `TOTAL: PASS=31, FAIL=0`
- Koide taste-cube descent: `PASS=15 FAIL=0`
- Gauge-vacuum evaluator route: `THEOREM PASS=5 SUPPORT=5 FAIL=0`
- Pauli exclusion: `OVERALL: PASS`
- Coulomb Green-kernel scaling: `SUMMARY: PASS=53 FAIL=0`
- D3 upper-bound gate: `SUMMARY: PASS=34 FAIL=0`
- `git diff --check`: clean

## Cache refresh

Refreshed caches via `scripts/cached_runner_output.py --refresh` for modified
runner outputs.
