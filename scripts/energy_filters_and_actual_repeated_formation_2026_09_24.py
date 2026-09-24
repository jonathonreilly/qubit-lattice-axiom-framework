"""Fresh finite controls for the companion supplied-model mathematical argument."""
from pathlib import Path
import tempfile,subprocess,sys,shutil,hashlib
AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('docs/ENERGY_FILTERS_AND_ACTUAL_REPEATED_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/PREPARED_FLAT_SECTOR_WITH_ELECTRIC_DYNAMICS_AND_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/CUBE_SIX_RECORD_ROTOR_POINT_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/energy_filter_check.py', 'scripts/finite_spin_dynamics_check.py', 'scripts/flat_band_spin_correction_probe.py', 'scripts/flat_compressed_operators.py')
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import energy_filter_check
    import finite_spin_dynamics_check
    import flat_band_spin_correction_probe
    import flat_compressed_operators
ROOT=Path(__file__).resolve().parents[1]
HELPERS=('scripts/energy_filter_check.py', 'scripts/finite_spin_dynamics_check.py', 'scripts/flat_band_spin_correction_probe.py', 'scripts/flat_compressed_operators.py')
SEQUENCE=('flat_band_spin_correction_probe.py', 'flat_compressed_operators.py', 'energy_filter_check.py')
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
