"""Run the four known-false concrete geometry assertions after ControlData compiles.

Independent processes share only read-only imports; all logs and outputs are local.
The individual Lean time limit is 120 seconds, with 135 seconds for its wrapper.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, subprocess, sys

D = Path(__file__).resolve().parent
cases = [
    ('FalseNoNoncoplanarity', 'RigidityControls.square_edges_true'),
    ('FalseMissingEdge', 'RigidityControls.tetra_three_edges_true'),
    ('FalseCoplanarResidual', 'RigidityControls.coplanar_residual_true'),
    ('FalseCycleSign', 'RigidityControls.wrong_cycle_nonzero'),
]
assert (D/'ControlData.olean').exists(), 'Compile and inspect the positive controls first'


def run(case):
    name, marker = case
    label = 'false_' + name
    p = subprocess.run([sys.executable, str(D/'run_lean.py'), name+'.lean', label],
                       cwd=D, text=True, capture_output=True, timeout=135)
    (D/'logs'/(label+'.wrapper.log')).write_text(p.stdout+p.stderr)
    logpath = D/'logs'/(label+'.log')
    text = logpath.read_text()
    execution = json.loads((D/'logs'/(label+'.json')).read_text())
    unexpected = [term for term in ['Application type mismatch', 'unknown module',
        'unknown constant', 'Unknown identifier', 'failed to synthesize',
        'object file', 'PROCESS TIMEOUT', 'unexpected token'] if term in text]
    reached = marker in text and 'unsolved goals' in text and not unexpected
    record = {'case':name,'expected_exit':1,'wrapper_exit':p.returncode,
              'actual_exit':execution['exit'],'reached_intended_mathematical_goal':reached,
              'unexpected_failure_markers':unexpected,'execution':execution,
              'source_sha256':hashlib.sha256((D/(name+'.lean')).read_bytes()).hexdigest(),
              'log_sha256':hashlib.sha256(logpath.read_bytes()).hexdigest()}
    return record


with ThreadPoolExecutor(max_workers=2) as pool:
    records = list(pool.map(run, cases))
(D/'false_controls_manifest.json').write_text(json.dumps(records,indent=2)+'\n')
for record in records:
    print(record['case'], 'exit',record['actual_exit'],
          'mathematical goal reached',record['reached_intended_mathematical_goal'])
assert all(r['wrapper_exit']==r['actual_exit']==1 and
           r['reached_intended_mathematical_goal'] for r in records)
print('EXPECTED REJECTIONS VERIFIED: four concrete false geometry statements')
