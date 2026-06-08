# Conditional Safe Narrows Handoff

## Repairs

- `gauge_vacuum_plaquette_full_slice_rim_lift_integral_boundary_science_only_note_2026-04-17`:
  narrowed to the supplied-partition product-Fubini lemma.  The actual SU(3)
  Wilson slab rim/far support partition and marked/non-marked mixed-kernel
  compression bridge remain open.
- `higgs_lattice_eigenvalue_ratio_narrow_theorem_note_2026-05-02`:
  narrowed so the `d=4/Z^4` APBC carrier is an explicit unresolved bounded
  hypothesis.  The curvature identity remains exact inside that supplied
  finite packet.

## Verification

- `python3 scripts/frontier_gauge_vacuum_plaquette_full_slice_rim_lift_integral_identification_2026_04_17.py`
- `python3 scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_gauge_vacuum_plaquette_full_slice_rim_lift_integral_identification_2026_04_17.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_gauge_vacuum_plaquette_full_slice_rim_lift_integral_identification_2026_04_17.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py`
- `git diff --check`
- `git diff -- docs/audit`

## Remaining Science

The stronger outcomes are still open: a retained SU(3) slab support/compression
theorem for the PF lane, and a framework-native derivation of the Higgs
`d=4/Z^4` APBC carrier.
