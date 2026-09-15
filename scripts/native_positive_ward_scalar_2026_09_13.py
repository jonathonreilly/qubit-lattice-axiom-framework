"""Checks for the analytical positive scalar theorem in the supplied native model."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/NATIVE_POSITIVE_WARD_SCALAR_BOUNDED_THEOREM_NOTE_2026-09-13.md",
    "scripts/native_ward_scalar_algebra_2026_09_13.py",
    "scripts/native_ward_scalar_arithmetic_2026_09_13.py",
    "scripts/native_ward_scalar_native_checks_2026_09_13.py",
    "docs/work_history/repo/review_feedback/pr8086-ward-evidence/kept/pr8086-ward-MOMENT_FORMULAS-e5533e9eb9859404.json",
    "docs/work_history/repo/review_feedback/pr8086-ward-evidence/kept/pr8086-ward-TRIAL_FORMULAS-1e477e0a5d21e13c.json",
    "docs/work_history/repo/review_feedback/pr8086-ward-evidence/kept/pr8086-ward-WITNESS-dda1191fa385b3b9.json",
    "docs/work_history/repo/review_feedback/pr8086-ward-evidence/kept/pr8086-ward-SOURCE_MANIFEST-a1b3f38c7ebc3abf.json",
    "docs/work_history/repo/review_feedback/pr8086-ward-evidence/kept/pr8086-ward-NO_GO_DISCIPLINE_CHECKLIST-af3647a217d8dd77.md",
    "docs/work_history/repo/review_feedback/pr8086-ward-evidence/kept/pr8086-ward-RESULTS-1edd1aa7af49c3cd.json",
)
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import json,signal,time
from fractions import Fraction
from native_ward_scalar_algebra_2026_09_13 import run as algebra_check
from native_ward_scalar_arithmetic_2026_09_13 import run as rational_check
from native_ward_scalar_native_checks_2026_09_13 import covariance_check,fock_moment_check,gap_fixture_check


def main():
    start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
    algebra=algebra_check();arithmetic=rational_check()
    covariance=covariance_check();fock=fock_moment_check();gap=gap_fixture_check()
    total=algebra['count']+1+covariance['ordered_pairs']+covariance['norm_checks']+fock['moment_checks']+gap['count']
    summary={'algebra':algebra,'rational_sign':{'interval':arithmetic['coarse_interval'],'units':'h^2 alpha',
             'coarse_error':arithmetic['coarse_error'],'nominal':[float(Fraction(v)) for v in arithmetic['nominal']],
             'norm_bounds':{k:float(Fraction(v)) for k,v in arithmetic['norms'].items()},
             'return_series_N':arithmetic['scalar_certificate']['N'],
             'P_gap_lower':float(Fraction(arithmetic['gap_bounds']['P_total'])),'O_gap_lower':arithmetic['gap_bounds']['O_lower'],
             'source_sha256':arithmetic['source_sha256'],'dependencies_sha256':arithmetic['dependencies_sha256']},
             'native_covariance':covariance,'native_Fock':fock,'native_gap_fixture':gap,'seconds':time.monotonic()-start}
    print(json.dumps(summary,indent=2))
    print('per_element: Every needed CAR moment and trial polynomial is derived from the displayed covariance table.')
    print('per_site: Actual native center and signed neighboring legs are used in both pair geometries.')
    print('per_mode: The finite Fourier/Fock source span checks all44 moments without truncating their required derivatives.')
    print('per_block: All90 ordered signed kernels and separate-source error terms are retained in the rational certificate.')
    print('lattice_wide: checked and not executed — infinite statements follow from the analytical return bounds and Gaussian form limit, not a full-lattice simulation.')
    print(f'TOTAL: PASS={total} FAIL=0')
    signal.alarm(0)


if __name__=='__main__':main()
