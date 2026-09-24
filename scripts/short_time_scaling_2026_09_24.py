"""Fresh finite controls for the companion supplied-model mathematical argument."""
from pathlib import Path
import tempfile,subprocess,sys,shutil,hashlib
AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('docs/SHORT_TIME_SCALING_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/core_derivation.py', 'scripts/finite_spin_jacobi_coefficients.py', 'scripts/residue_polynomial_check.py', 'scripts/scaled_time_limit_probe.py', 'scripts/spectral_fixed_time_probe.py')
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import core_derivation
    import finite_spin_jacobi_coefficients
    import residue_polynomial_check
    import scaled_time_limit_probe
    import spectral_fixed_time_probe
ROOT=Path(__file__).resolve().parents[1]
HELPERS=('scripts/core_derivation.py', 'scripts/finite_spin_jacobi_coefficients.py', 'scripts/residue_polynomial_check.py', 'scripts/scaled_time_limit_probe.py', 'scripts/spectral_fixed_time_probe.py')
COPY_DOCS=()
SEQUENCE=('core_derivation.py', 'residue_polynomial_check.py', 'finite_spin_jacobi_coefficients.py', 'scaled_time_limit_probe.py')
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
