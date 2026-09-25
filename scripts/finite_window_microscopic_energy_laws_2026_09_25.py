#!/usr/bin/env python3
"""Source-reused controls for finite-window microscopic energy laws."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/FINITE_WINDOW_MICROSCOPIC_ENERGY_LAWS_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', '.claude/science/physics-loops/mobile-record-finite-window-energy-20260925/runtime/root_generic/finite_window_energy_controls.py', '.claude/science/physics-loops/mobile-record-finite-window-energy-20260925/runtime/independent_native/primitive_energy_control.py')
RESULT_PATH = 'outputs/finite_window_energy_20260925/FINITE_WINDOW_ENERGY_PUBLIC_RESULTS.json'
RUNTIME = ['.claude/science/physics-loops/mobile-record-finite-window-energy-20260925/runtime/root_generic/finite_window_energy_controls.py', '.claude/science/physics-loops/mobile-record-finite-window-energy-20260925/runtime/independent_native/primitive_energy_control.py']
from pathlib import Path
import hashlib, json, os, subprocess, sys, tempfile, time

def main():
    root = Path(__file__).resolve().parents[1]
    tick = time.perf_counter()
    stages, payload = [], {}
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='finite-window-energy-') as directory:
        tmp = Path(directory)
        for rel in RUNTIME:
            source = root / rel
            target = tmp / source.parent.name / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
            start = time.perf_counter()
            p = subprocess.run([sys.executable, str(target)], cwd=target.parent,
                               capture_output=True, env=env, check=False)
            if p.returncode or p.stderr:
                raise RuntimeError(f'{source.name}: exit {p.returncode}; '+p.stderr.decode())
            payload[source.parent.name] = json.loads(p.stdout)
            stages.append({'program': source.name,
                           'code_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
                           'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(),
                           'stdout_bytes': len(p.stdout), 'stderr_bytes': len(p.stderr),
                           'exit_code': p.returncode, 'elapsed_seconds': time.perf_counter()-start})
    result = {'scope': 'Exact-source root generic and independent native graph controls reused for publication; no new independent reconstruction or experimental fit.',
              'payload': payload, 'stages': stages,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'elapsed_seconds': time.perf_counter()-tick, 'all_assertions_passed': True}
    path = root / RESULT_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, indent=2, allow_nan=False)+'\n'
    path.write_text(text)
    print(text, end='')
    print('TOTAL_PASS: 2')

if __name__ == '__main__':
    main()
