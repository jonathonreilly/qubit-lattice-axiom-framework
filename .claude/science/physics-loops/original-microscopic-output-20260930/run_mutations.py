#!/usr/bin/env python3
"""Isolated actual source mutations, with lossless diffs and output capture."""
import ast
import difflib
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

AUDIT_TIMEOUT_SEC = 90
pack = Path(__file__).resolve().parent
repo = pack.parents[3]
runner = Path('scripts/original_microscopic_local_output_2026_09_30.py')
source = (repo/runner).read_text()
inputs = next(ast.literal_eval(n.value) for n in ast.parse(source).body
              if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in n.targets))
changes = [
    ('birth_orientation','BIRTH_SHIFT_SIGN = 1','BIRTH_SHIFT_SIGN = -1','original_source_words'),
    ('coherent_normalization','COHERENT_AMPLITUDE = Q(1)','COHERENT_AMPLITUDE = Q(1,2)','coherent_original_gain_and_linear_weight'),
    ('spin_boundary','DROP_SPIN_BOUNDARY = False','DROP_SPIN_BOUNDARY = True','spin_boundary_and_common_carrier'),
    ('outside_zero','OUTSIDE_ZERO = True','OUTSIDE_ZERO = False','spin_boundary_and_common_carrier'),
    ('overflow_loss','OVERFLOW_LOSS = True','OVERFLOW_LOSS = False','original_register_gain_loss_and_overflow'),
    ('overflow_update','UPDATE_ALL_WORDS = True','UPDATE_ALL_WORDS = False','original_register_gain_loss_and_overflow'),
    ('electric_halo','INCLUDE_INCIDENT_LINKS = True','INCLUDE_INCIDENT_LINKS = False','electric_occupancy_halo'),
    ('linear_shift','LINEAR_SHIFT_BUDGET = 2','LINEAR_SHIFT_BUDGET = 1','coherent_original_gain_and_linear_weight'),
    ('word_error_factor','WORD_ERROR_FACTOR = 2','WORD_ERROR_FACTOR = 0','actual_two_link_source_word_bound'),
]
rows=[]
for name,old,new,expected in changes:
    assert source.count(old)==1
    mutated=source.replace(old,new)
    dest=pack/'mutations'/name
    dest.mkdir(parents=True,exist_ok=False)
    diff=''.join(difflib.unified_diff(source.splitlines(True),mutated.splitlines(True),
                                   fromfile=str(runner),tofile=str(runner)))
    raw=diff.encode()
    (dest/'mutation.diff.gz').write_bytes(gzip.compress(raw,mtime=0))
    with tempfile.TemporaryDirectory(prefix='microscopic-output-'+name+'-') as tmp:
        scratch=Path(tmp)
        for path in inputs:
            target=scratch/path
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes((repo/path).read_bytes())
        (scratch/runner).parent.mkdir(parents=True,exist_ok=True)
        (scratch/runner).write_text(mutated)
        r=subprocess.run([sys.executable,str(scratch/runner)],capture_output=True,timeout=10)
        (dest/'stdout.txt').write_bytes(r.stdout)
        (dest/'stderr.txt').write_bytes(r.stderr)
        output=(scratch/'outputs'/runner.with_suffix('.json').name).read_bytes()
        (dest/'output.json').write_bytes(output)
        result=json.loads(output)
    ok=r.returncode!=0 and expected in result['failures'] and result['fail_count']>0
    row={'name':name,'pass':ok,'expected_failure':expected,'exit_code':r.returncode,
         'observed_failures':result['failures'],'mutated_runner_sha256':hashlib.sha256(mutated.encode()).hexdigest(),
         'raw_diff_sha256':hashlib.sha256(raw).hexdigest(),
         'diff_container_sha256':hashlib.sha256((dest/'mutation.diff.gz').read_bytes()).hexdigest()}
    rows.append(row)
    print(('PASS ' if ok else 'FAIL ')+name+' '+json.dumps(row,sort_keys=True))
assert (repo/runner).read_text()==source
out={'runner_sha256':hashlib.sha256(source.encode()).hexdigest(),
     'input_sha256':{x:hashlib.sha256((repo/x).read_bytes()).hexdigest() for x in inputs},
     'scope':'actual scratch mutation rejection, not a theorem proof','mutations':rows}
(pack/'MUTATION_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
passed=sum(r['pass'] for r in rows)
print('TOTAL: PASS=%d FAIL=%d' % (passed,len(rows)-passed))
raise SystemExit(0 if passed==len(rows) else 1)
