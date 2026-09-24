"""Fresh finite controls for the companion conditional mathematical note."""
from pathlib import Path
import tempfile,subprocess,sys,shutil,hashlib
AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('docs/UNIFORM_RECORD_DENSITY_WITH_LIVE_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/record_density_and_fast_defect_check.py', 'scripts/hardcore_record_ring_and_formation_check.py', 'scripts/local_gauge_record_cooling_check.py')
from typing import TYPE_CHECKING
# Static packet dependencies; controls execute only in the temporary workspace.
if TYPE_CHECKING:
    import record_density_and_fast_defect_check
    import hardcore_record_ring_and_formation_check
    import local_gauge_record_cooling_check
ROOT=Path(__file__).resolve().parents[1]
HELPERS=('scripts/record_density_and_fast_defect_check.py', 'scripts/hardcore_record_ring_and_formation_check.py', 'scripts/local_gauge_record_cooling_check.py')
SEQUENCE=('record_density_and_fast_defect_check.py',)
def main():
    print('Evidence boundary: supplied models; finite controls do not establish native physics, limit interchange or audit status.',flush=True)
    with tempfile.TemporaryDirectory(prefix='mobile-record-controls-') as td:
        work=Path(td)
        for rel in HELPERS:
            shutil.copyfile(ROOT/rel,work/Path(rel).name)
        for name in SEQUENCE:
            result=subprocess.run([sys.executable,'-u',str(work/name)],cwd=work,text=True,capture_output=True)
            if result.returncode:
                print(result.stdout);print(result.stderr,file=sys.stderr)
                print('TOTAL: PASS=0 FAIL=1');raise SystemExit(result.returncode)
            print('[PASS] component '+name+'; stdout sha256='+hashlib.sha256(result.stdout.encode()).hexdigest(),flush=True)
            if result.stderr:print(result.stderr,file=sys.stderr)
        results=sorted(work.glob('*RESULTS.json'))
        assert results, 'scientific controls produced no result records'
        for path in results:
            print('RESULT '+path.name)
            print(path.read_text())
    print(f'TOTAL: PASS={len(SEQUENCE)} FAIL=0')
if __name__=='__main__':main()
