"""Fresh finite controls for the companion supplied-model mathematical argument."""
from pathlib import Path
import tempfile,subprocess,sys,shutil,hashlib
AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('docs/ROTOR_DRIFT_AND_FINITE_SPIN_HIGH_FLUX_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/HIGH_FLUX_ACTUAL_BIRTH_ENERGY_SPREAD_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/cube_high_flux_birth.py', 'scripts/finite_spin_path_comparison.py', 'scripts/full_rotor_energy_control.py', 'scripts/mobile_compensation_model_20260924.py', 'scripts/symbolic_spin_energy_balance.py')
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import cube_high_flux_birth
    import finite_spin_path_comparison
    import full_rotor_energy_control
    import mobile_compensation_model_20260924
    import symbolic_spin_energy_balance
ROOT=Path(__file__).resolve().parents[1]
HELPERS=('scripts/cube_high_flux_birth.py', 'scripts/finite_spin_path_comparison.py', 'scripts/full_rotor_energy_control.py', 'scripts/mobile_compensation_model_20260924.py', 'scripts/symbolic_spin_energy_balance.py')
SEQUENCE=('full_rotor_energy_control.py', 'symbolic_spin_energy_balance.py', 'finite_spin_path_comparison.py')
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
