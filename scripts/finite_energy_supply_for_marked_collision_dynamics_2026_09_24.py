"""Fresh finite controls for the companion supplied-model mathematical argument."""
from pathlib import Path
import tempfile,subprocess,sys,shutil,hashlib
AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('docs/FINITE_ENERGY_SUPPLY_FOR_MARKED_COLLISION_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/FINITE_TIME_STAR_ENERGY_AND_SUPPLY_BOUND_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/STAR_ENERGY_COST_ACROSS_THE_ELECTRIC_FAMILY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/exact_star_energy.py', 'scripts/finite_battery_control.py', 'scripts/marked_collision_control.py')
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import exact_star_energy
    import finite_battery_control
    import marked_collision_control
ROOT=Path(__file__).resolve().parents[1]
HELPERS=('scripts/exact_star_energy.py', 'scripts/finite_battery_control.py', 'scripts/marked_collision_control.py')
SEQUENCE=('finite_battery_control.py', 'marked_collision_control.py')
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
