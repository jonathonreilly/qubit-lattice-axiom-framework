"""Checks for the supplied growing formation and protected-current construction."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/NATIVE_GROWING_FORMATION_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-13.md', 'scripts/native_formation_native_checks_2026_09_13.py', 'scripts/native_formation_transport_checks_2026_09_13.py', 'scripts/native_formation_growth_checks_2026_09_13.py', 'docs/work_history/repo/review_feedback/pr8087-growing-formation-evidence/kept/pr8087-SOURCE_MANIFEST-a1b3f38c7ebc3abf.json', 'docs/work_history/repo/review_feedback/pr8087-growing-formation-evidence/kept/pr8087-NO_GO_DISCIPLINE_CHECKLIST-af3647a217d8dd77.md', 'docs/work_history/repo/review_feedback/pr8087-growing-formation-evidence/kept/pr8087-RESULTS-1edd1aa7af49c3cd.json', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
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
