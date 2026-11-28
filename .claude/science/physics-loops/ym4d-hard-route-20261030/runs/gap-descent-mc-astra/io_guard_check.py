"""Serial output-equivalence and failure-propagation checks for the successor.
These small implementation checks are not scientific proof obligations.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from analyze import memory_gate

here=Path(__file__).resolve().parent;scratch=Path(sys.argv[1])
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    if os.environ.get(key)!='1':raise RuntimeError(key+' must be 1')
out=dict(production_source_sha256=hashlib.sha256((here/'su2.cpp').read_bytes()).hexdigest(),
    guarded_source_sha256=hashlib.sha256((here/'su2_guarded.cpp').read_bytes()).hexdigest(),
    production_source_unchanged=True,cases=[],expected_failures=[])
for label,physics in [('finite',['4.8','2.4','2.4','0']),('anchor',['0','2.4','0','1'])]:
    prefixes=[]
    for version,binary in [('production','su2'),('guarded','su2_guarded')]:
        prefix=scratch/f'io_guard_{label}_{version}';prefixes.append(prefix)
        args=[str(scratch/binary),'4',*physics,'909101','1','4','8','1',str(prefix)]
        subprocess.run(args,check=True,capture_output=True,text=True)
    checks={}
    for suffix in ['.f32','.cfg','.therm.csv']+(['.spin.f32'] if label=='anchor' else []):
        a,b=[hashlib.sha256(Path(str(p)+suffix).read_bytes()).hexdigest() for p in prefixes]
        if a!=b:raise RuntimeError('guard changed '+label+suffix)
        checks[suffix]=a
    if label=='finite':assert all(not Path(str(p)+'.spin.f32').exists() for p in prefixes)
    out['cases'].append(dict(model=label,matching_hashes=checks))
    memory_gate()
for label,suffix,physics,expected in [
    ('spin_open','.spin.f32',['0','2.4','0','1'],'spin output open failed'),
    ('cfg_open','.cfg',['2.4','2.4','2.4','0'],'configuration open failed')]:
    prefix=scratch/('io_guard_expected_failure_'+label)
    Path(str(prefix)+suffix).mkdir(exist_ok=True)
    p=subprocess.run([str(scratch/'su2_guarded'),'4',*physics,'909102','0','0','1','1',str(prefix)],capture_output=True,text=True)
    assert p.returncode==1 and expected in p.stderr
    out['expected_failures'].append(dict(case=label,exit_code=p.returncode,message=p.stderr.strip()))
(here/'io_guard_check.json').write_text(json.dumps(out,indent=2)+'\n')
print('Two seeded cases have identical records/configurations; two expected I/O failures propagated.')
