#!/usr/bin/env python3
"""Sequential scratch mutations; no canonical source/input/cache writes."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

pack = Path(__file__).resolve().parent
repo = pack.parents[3]
source = repo/'scripts/native_dilute_thermodynamics_2026_09_30.py'
original = source.read_bytes()
original_hash = hashlib.sha256(original).hexdigest()
root = pack/'mutations'
root.mkdir(exist_ok=True)
result_path = root/'results.json'
if result_path.exists():
    raise SystemExit('Refusing to overwrite mutation evidence.')
specs = [
    ('gradient_weight', 'GRADIENT_WEIGHT = 1', 'GRADIENT_WEIGHT = 2', 'literal diagonal'),
    ('individual_rows', 'RETAIN_INDIVIDUAL_PLANE_ROWS = True', 'RETAIN_INDIVIDUAL_PLANE_ROWS = False', 'individual rows'),
    ('incident_pins', 'KEEP_INCIDENT_PINS = True', 'KEEP_INCIDENT_PINS = False', 'physical incident pin'),
    ('plane_multiplicity', 'PLANE_GRADIENT_MULTIPLICITY = 2', 'PLANE_GRADIENT_MULTIPLICITY = 1', 'gradient multiplicity'),
    ('safe_diagonal', 'SAFE_BOUNDARY_SUBTRACTION = 1', 'SAFE_BOUNDARY_SUBTRACTION = 0', 'safe boundary diagonal'),
    ('bad_particle_charge', 'BAD_PARTICLE_F_CHARGE = 2', 'BAD_PARTICLE_F_CHARGE = 1', 'actual bad-particle count'),
    ('center_holes', 'CENTER_BEFORE_HOLES = True', 'CENTER_BEFORE_HOLES = False', 'full-anchor Neumann centering'),
    ('husimi_coefficient', 'HUSIMI_MIXED_COEFFICIENT = 4', 'HUSIMI_MIXED_COEFFICIENT = 2', 'complex sphere identity'),
    ('number_reserve', 'RESERVE_NUMBER_BUFFER = True', 'RESERVE_NUMBER_BUFFER = False', 'reserved exact integer capacity'),
    ('seam_width', 'SEAM_WIDTH = 2', 'SEAM_WIDTH = 1', 'actual radius-two centers'),
    ('pair_factor', 'PAIR_QUARTIC_DIVISOR = 2', 'PAIR_QUARTIC_DIVISOR = 1', 'computed_quartic_ratio == raw_vector_scale_squared/incoming_scale_squared'),
]
results = []
for index, (name, old, new, expected) in enumerate(specs, 1):
    if source.read_bytes() != original:
        raise SystemExit('Canonical source changed during controls.')
    folder = root/f'{index:02d}_{name}'
    folder.mkdir()
    text = original.decode()
    assert text.count(old+'\n') == 1
    mutated = text.replace(old+'\n', new+'\n', 1).encode()
    candidate = folder/'candidate.py'
    candidate.write_bytes(mutated)
    prefix = folder/'run'
    command = [sys.executable, str(pack/'managed_run.py'), '--cpu', '30',
               '--wall', '180', '--rss-mib', '200', '--prefix', str(prefix),
               '--', sys.executable, str(candidate)]
    completed = subprocess.run(command, cwd=repo, capture_output=True, text=True)
    (folder/'wrapper.stdout.txt').write_text(completed.stdout)
    (folder/'wrapper.stderr.txt').write_text(completed.stderr)
    receipt = json.loads(Path(str(prefix)+'.execution.json').read_text())
    output = Path(str(prefix)+'.stdout.txt').read_text()+Path(str(prefix)+'.stderr.txt').read_text()
    killed = (receipt['exit_code'] == 1 and receipt['termination_reason'] is None
              and 'AssertionError' in output and expected in output)
    results.append({'name': name, 'original_assignment': old, 'mutated_assignment': new,
                    'original_sha256': original_hash,
                    'candidate_sha256': hashlib.sha256(mutated).hexdigest(),
                    'expected_assertion': expected, 'actual_assertion_detected': killed,
                    'wrapper_exit_code': completed.returncode,
                    'execution': receipt})
    print(json.dumps({'mutation': name, 'actual_assertion_detected': killed}), flush=True)
    if not killed:
        break
assert source.read_bytes() == original
summary = {'primary_sha256': original_hash, 'scientific_inputs_edited': False,
           'canonical_cache_edited': False, 'planned': len(specs), 'executed': len(results),
           'all_planned_detected': len(results) == len(specs) and all(x['actual_assertion_detected'] for x in results),
           'results': results}
result_path.write_text(json.dumps(summary, indent=2)+'\n')
raise SystemExit(0 if summary['all_planned_detected'] else 1)
