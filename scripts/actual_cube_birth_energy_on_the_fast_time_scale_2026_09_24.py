"""Fresh finite controls for the companion supplied-model mathematical argument."""
from pathlib import Path
import tempfile,subprocess,sys,shutil,hashlib
AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GENERAL_MICROSCOPIC_BIRTH_ENERGY_AND_CUBE_POWER_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/complete_spin_one_cube_control.py', 'scripts/exact_fast_band_paths.py')
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import complete_spin_one_cube_control
    import exact_fast_band_paths
ROOT=Path(__file__).resolve().parents[1]
HELPERS=('scripts/complete_spin_one_cube_control.py', 'scripts/exact_fast_band_paths.py')
SEQUENCE=('exact_fast_band_paths.py', 'complete_spin_one_cube_control.py')
def main():
    print('Evidence boundary: supplied models and stated limits; finite controls confer no audit verdict.',flush=True)
    with tempfile.TemporaryDirectory(prefix='formation-energy-controls-') as td:
        work=Path(td)
        for rel in HELPERS:shutil.copyfile(ROOT/rel,work/Path(rel).name)
        for name in SEQUENCE:
            result=subprocess.run([sys.executable,'-u',str(work/name)],cwd=work,text=True,capture_output=True,timeout=3500)
            print('COMPONENT '+name+'; stdout sha256='+hashlib.sha256(result.stdout.encode()).hexdigest(),flush=True)
            print(result.stdout,flush=True)
            if result.stderr:print(result.stderr,file=sys.stderr)
            if result.returncode:
                print('TOTAL: PASS=0 FAIL=1');raise SystemExit(result.returncode)
        for path in sorted(work.glob('*.json')):
            print('RESULT '+path.name)
            print(path.read_text())
    print(f'TOTAL: PASS={len(SEQUENCE)} FAIL=0')
if __name__=='__main__':main()
