"""Fresh finite controls for the companion supplied-model mathematical argument."""
from pathlib import Path
import tempfile,subprocess,sys,shutil,hashlib
AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('docs/CUBE_ACTUAL_FORMATION_LOCAL_DENSITY_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/CUBE_SIX_RECORD_ROTOR_POINT_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/CUBE_TWO_MARK_LOOP_READOUT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/cube_physical_controls.py', 'scripts/second_event_probe.py')
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import cube_physical_controls
    import second_event_probe
ROOT=Path(__file__).resolve().parents[1]
HELPERS=('scripts/cube_physical_controls.py', 'scripts/second_event_probe.py')
COPY_DOCS=()
SEQUENCE=('cube_physical_controls.py',)
def main():
    print('Evidence boundary: supplied models and stated limits; no audit verdict or native physical law is established by finite controls.',flush=True)
    with tempfile.TemporaryDirectory(prefix='postbirth-controls-') as td:
        work=Path(td)
        for rel in (*HELPERS,*COPY_DOCS):shutil.copyfile(ROOT/rel,work/Path(rel).name)
        for name in SEQUENCE:
            result=subprocess.run([sys.executable,'-u',str(work/name)],cwd=work,text=True,capture_output=True)
            if result.returncode:
                print(result.stdout);print(result.stderr,file=sys.stderr)
                print('TOTAL: PASS=0 FAIL=1');raise SystemExit(result.returncode)
            print('[PASS] component '+name+'; stdout sha256='+hashlib.sha256(result.stdout.encode()).hexdigest(),flush=True)
            if result.stderr:print(result.stderr,file=sys.stderr)
        results=sorted(work.glob('*.json'));assert results, 'no scientific output generated'
        for path in results:
            print('RESULT '+path.name)
            print(path.read_text())
    print(f'TOTAL: PASS={len(SEQUENCE)} FAIL=0')
if __name__=='__main__':main()
