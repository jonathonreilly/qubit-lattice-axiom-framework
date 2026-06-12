# Handoff

## Summary

This branch repairs the atomic companion row's source-side runner artifact
blocker. The note previously still said the readouts were not pinned to
runner-cache stdout and that the runner-source repair remained open. Current
repo state has the full hydrogen, helium Hartree, and helium Jastrow runner
sources plus cache certificates. The note now reflects that.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
checks = {
    'scripts/frontier_atomic_hydrogen_lattice_companion.py': ['def build_graph_laplacian', 'def build_coulomb_potential', 'def solve_hamiltonian'],
    'scripts/frontier_atomic_helium_hartree_companion.py': ['def solve_poisson_for_hartree', 'def helium_variational_scf', 'Hartree equation derived'],
    'scripts/frontier_atomic_helium_jastrow_companion.py': ['def make_jastrow', 'def local_energy', 'Jastrow form'],
    'logs/runner-cache/frontier_atomic_hydrogen_lattice_companion.txt': ['E_2/E', '0.25857', 'PASS'],
    'logs/runner-cache/frontier_atomic_helium_hartree_companion.txt': ['1.3424', 'Hartree equation derived', 'SUMMARY: HELIUM HARTREE COMPANION'],
    'logs/runner-cache/frontier_atomic_helium_jastrow_companion.txt': ['1.43572', 'Jastrow', 'SUMMARY: HELIUM JASTROW COMPANION'],
    'logs/runner-cache/frontier_hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_verifier.txt': ['PASS=28', 'FAIL=0'],
}
for path, needles in checks.items():
    text = Path(path).read_text()
    missing = [n for n in needles if n not in text]
    if missing:
        raise SystemExit(f'FAIL {path}: missing {missing}')
    print(f'PASS {path}')
PY
python3 scripts/precompute_audit_runners.py --check-only --pr-diff origin/main --allow-non-main --push-mode none
git diff --check
```

Observed result: source/cache visibility checks pass, all relevant caches fresh,
and whitespace check clean.

## Remaining Work

Independent review and audit should decide whether the narrowed dependency
repair is sufficient for the diagnostic finite-box scope.
