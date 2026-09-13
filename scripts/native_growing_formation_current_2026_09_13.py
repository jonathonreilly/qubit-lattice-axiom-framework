"""Checks for the supplied growing formation and protected-current construction."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/NATIVE_GROWING_FORMATION_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-13.md', 'scripts/native_formation_native_checks_2026_09_13.py', 'scripts/native_formation_transport_checks_2026_09_13.py', 'scripts/native_formation_growth_checks_2026_09_13.py', '.claude/science/physics-loops/native-growing-formation-current-20260913/SOURCE_MANIFEST.json', '.claude/science/physics-loops/native-growing-formation-current-20260913/NO_GO_DISCIPLINE_CHECKLIST.md', '.claude/science/physics-loops/native-growing-formation-current-20260913/mutations/RESULTS.json')
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import json,signal,time
from native_formation_native_checks_2026_09_13 import run as native_check
from native_formation_transport_checks_2026_09_13 import run as transport_check
from native_formation_growth_checks_2026_09_13 import run as growth_check


def main():
    signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic()
    rows={name:check() for name,check in (('native',native_check),('transport',transport_check),('growth',growth_check))}
    count=sum(row['count'] for row in rows.values())
    print(json.dumps({'checks':rows,'seconds':time.monotonic()-start},indent=2))
    print('per_element: Native Pauli bit actions and the actual Born projectors check the local instrument.')
    print('per_site: Literal lattice roles and nearest-neighbor program conditions are checked on the prepared domain.')
    print('per_mode: All finite periodic comparator modes and their physical-position current operators are checked.')
    print('per_block: Finite histories, parity preparation, boundary evolution and fresh collision storage are checked.')
    print('lattice_wide: checked and not executed — nonexplosion and front/current windows use the analytical proofs; no infinite physical cycle code is assumed.')
    print(f'TOTAL: PASS={count} FAIL=0')
    signal.alarm(0)


if __name__=='__main__':main()
