"""Fresh finite controls for the companion conditional mathematical note."""
from pathlib import Path
import tempfile,subprocess,sys,shutil,hashlib
AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('docs/CHARGED_RECORD_EXCHANGE_BAND_FIELD_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/HOMOGENEOUS_MOBILE_CHARGED_RECORDS_AND_FIELD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/charged_record_potential_hessian_check.py', 'scripts/charged_band_packet_check.py', 'scripts/charged_band_geometry_check.py')
from typing import TYPE_CHECKING
# Static packet dependencies; controls execute only in the temporary workspace.
if TYPE_CHECKING:
    import charged_record_potential_hessian_check
    import charged_band_packet_check
    import charged_band_geometry_check
ROOT=Path(__file__).resolve().parents[1]
HELPERS=('scripts/charged_record_potential_hessian_check.py', 'scripts/charged_band_packet_check.py', 'scripts/charged_band_geometry_check.py')
SEQUENCE=('charged_record_potential_hessian_check.py', 'charged_band_packet_check.py', 'charged_band_geometry_check.py')
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
