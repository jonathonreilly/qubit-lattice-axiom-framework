"""Fresh exact rotor controls; no infinite-time numerical certification."""
from pathlib import Path
import tempfile,subprocess,sys,shutil
AUDIT_TIMEOUT_SEC=3600
AUDIT_INPUT_PATHS=('docs/ACTUAL_BIRTH_ROTOR_ENERGY_HAS_AN_ALGEBRAIC_LOWER_BOUND_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ROTOR_CUBE_FAST_ENERGY_STRONG_DECAY_WITHOUT_UNIFORM_DECAY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/mobile_rotor_local_rate_control_20260924.py')
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import mobile_rotor_local_rate_control_20260924
ROOT=Path(__file__).resolve().parents[1]
def main():
 with tempfile.TemporaryDirectory(prefix='rotor-tail-check-') as td:
  p=Path(td)/'mobile_rotor_local_rate_control_20260924.py'
  shutil.copyfile(ROOT/'scripts/mobile_rotor_local_rate_control_20260924.py',p)
  result=subprocess.run([sys.executable,'-u',str(p)],cwd=td,text=True,capture_output=True,timeout=3500)
  print(result.stdout)
  if result.stderr:print(result.stderr,file=sys.stderr)
  if result.returncode:raise SystemExit(result.returncode)
  for j in sorted(Path(td).glob('*.json')):print('RESULT '+j.name+'\n'+j.read_text())
 print('TOTAL: PASS=1 FAIL=0')
if __name__=='__main__':main()
