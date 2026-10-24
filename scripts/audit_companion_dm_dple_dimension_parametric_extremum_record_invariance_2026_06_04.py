#!/usr/bin/env python3
"""Historical DPLE provenance only; no ledger or physical closure assertion."""

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('archive/notes/review_feedback/pr9845-consumers-2026-10-23/DPLE-original-parent.md.txt', 'archive/notes/review_feedback/pr9845-consumers-2026-10-23/audit_companion_dm_dple_dimension_parametric_extremum_record_invariance_2026_06_04.py.txt', 'docs/DM_DPLE_DIMENSION_PARAMETRIC_EXTREMUM_RECORD_INVARIANCE_COMPANION_NOTE_2026-06-04.md', 'docs/DM_DPLE_DIMENSION_PARAMETRIC_EXTREMUM_THEOREM_NOTE_2026-04-19.md')

from pathlib import Path
import hashlib
ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_BINDINGS = {'archive/notes/review_feedback/pr9845-consumers-2026-10-23/DPLE-original-parent.md.txt': 'e927842ce7225e7f03aab68214b365f61a27c847dd2e546435d0b01cce28458b', 'archive/notes/review_feedback/pr9845-consumers-2026-10-23/audit_companion_dm_dple_dimension_parametric_extremum_record_invariance_2026_06_04.py.txt': 'b50e94f5e7cd66c6df398480da15bf22fc726a83afd24745f4509dbf1e1fcc24'}

def main():
    failed = 0
    for rel, expected in HISTORICAL_BINDINGS.items():
        actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        ok = actual == expected
        failed += not ok
        print(('PASS ' if ok else 'FAIL ') + 'historical recovery hash: ' + rel)
    current = ROOT / 'docs/DM_DPLE_DIMENSION_PARAMETRIC_EXTREMUM_THEOREM_NOTE_2026-04-19.md'
    print('Current parent SHA256: ' + hashlib.sha256(current.read_bytes()).hexdigest())
    print('Historical positive_theorem/19-PASS/ledger assertions are superseded.')
    print('No current theorem, Record-invariance proof, ledger status or count is certified here.')
    return 1 if failed else 0
if __name__ == '__main__':
    raise SystemExit(main())
