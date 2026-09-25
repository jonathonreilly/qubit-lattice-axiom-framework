#!/usr/bin/env python3
"""Fresh source-reused controls for original counts and energy identifiability."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/ORIGINAL_COINCIDENCES_AND_NUMBER_ENERGY_IDENTIFIABILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ACTUAL_INPUT_ENERGY_AND_ORIGINAL_MARK_POWER_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/OPTICAL_REFERENCE_ENERGY_LIMITS_FOR_ORIGINAL_RECORD_COUNTS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORIGINAL_FORMATION_RECORD_PHOTON_READOUT_AND_MICROSCOPIC_FINITE_BINS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'scripts/review_support/unit28/pr9181/coincidence/coincidence_controls.py', 'scripts/review_support/unit28/pr9181/number_offset/number_offset_controls.py']
RESULT_PATH = 'outputs/count_interpretation_20260925/COUNT_INTERPRETATION_RESULTS.json'
RUNTIME = ['scripts/review_support/unit28/pr9181/coincidence/coincidence_controls.py', 'scripts/review_support/unit28/pr9181/number_offset/number_offset_controls.py']
from pathlib import Path
import hashlib, json, os, subprocess, sys, tempfile, time

def main():
    root = Path(__file__).resolve().parents[1]
    started = time.perf_counter()
    stages, payload = [], {}
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='original-count-interpretation-') as directory:
        tmp = Path(directory)
        for rel, result_name in zip(RUNTIME, ['COINCIDENCE_RESULTS.json', 'NUMBER_OFFSET_RESULTS.json']):
            source = root / rel
            target = tmp / source.parent.name / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
            tick = time.perf_counter()
            process = subprocess.run([sys.executable, str(target)], cwd=target.parent,
                                     capture_output=True, env=env, check=False)
            elapsed = time.perf_counter() - tick
            if process.returncode or process.stderr:
                raise RuntimeError(f'{source.name}: exit {process.returncode}; ' + process.stderr.decode())
            payload[result_name] = json.loads(process.stdout)
            stages.append({'program': source.name, 'code_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
                           'result': result_name, 'stdout_sha256': hashlib.sha256(process.stdout).hexdigest(),
                           'stdout_bytes': len(process.stdout), 'stderr_bytes': len(process.stderr),
                           'exit_code': process.returncode, 'elapsed_seconds': elapsed})
    result = {'scope': 'Source-reused author controls; independent reconstruction is separate. No laboratory fit.',
              'payload': payload, 'stages': stages,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'elapsed_seconds': time.perf_counter() - started, 'all_assertions_passed': True}
    target = root / RESULT_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(result, indent=2, allow_nan=False) + '\n'
    target.write_text(data)
    print(data, end='')
    print('TOTAL: PASS=2 FAIL=0')

if __name__ == '__main__':
    main()
