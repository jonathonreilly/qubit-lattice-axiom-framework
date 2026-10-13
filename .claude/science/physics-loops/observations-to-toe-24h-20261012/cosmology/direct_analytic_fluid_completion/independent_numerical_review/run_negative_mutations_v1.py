#!/usr/bin/env python3
"""Execute immutable author-source mutants as negative sensitivity evidence."""
from pathlib import Path
import collections
import datetime
import difflib
import hashlib
import json
import os
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
ORIGINAL=(ROOT/'source_snapshot/check_analytic_fluid_v1.py').read_text()
FIXTURE=(ROOT/'source_snapshot/NUMERICAL_FIXTURES_v1.json').read_bytes()
MUTATIONS=[
    ('omit_connection', "-np.einsum('ijk,j,k->i',gamma,p,p)", "-0.0*np.einsum('ijk,j,k->i',gamma,p,p)"),
    ('omit_dust_mass_exchange', '(-3+np.sqrt(a)*p[0])*sm', '(-3)*sm'),
    ('omit_scalar_matter_force', 'force = dv+np.array([np.sqrt(a)*sm,0.,0.])', 'force = dv+np.array([0.,0.,0.])'),
    ('omit_u_restoring_force', 'force = dv+np.array([np.sqrt(a)*sm,0.,0.])', 'force = dv+np.array([np.sqrt(a)*sm,0.,0.])\n    force[0] -= hv*hv*phi[0]*(4*phi[1]*phi[1]+nu)'),
]
CHILD='''from pathlib import Path
import importlib.util,json,sys
p=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("negative_mutant",p/"check_analytic_fluid_v1.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
rows=m.off_trajectory_controls()
out={"scope":"Negative sensitivity only; not independent positive evidence", "rows":rows,"checks":m.CHECKS,"passed":sum(c["passed"] for c in m.CHECKS),"failed":sum(not c["passed"] for c in m.CHECKS)}
(p/"RESULTS.json").write_text(json.dumps(out,indent=2,allow_nan=False)+"\\n")
print(json.dumps({"passed":out["passed"],"failed":out["failed"]},sort_keys=True))
raise SystemExit(int(out["failed"]>0))
'''

records=[]
for name,old,new in MUTATIONS:
    assert ORIGINAL.count(old)==1,(name,ORIGINAL.count(old))
    path=ROOT/'negative_mutations'/name;path.mkdir(parents=True)
    changed=ORIGINAL.replace(old,new,1)
    source=path/'check_analytic_fluid_v1.py';source.write_text(changed)
    (path/'NUMERICAL_FIXTURES_v1.json').write_bytes(FIXTURE)
    (path/'run_off_trajectory_only.py').write_text(CHILD)
    patch=''.join(difflib.unified_diff(ORIGINAL.splitlines(True),changed.splitlines(True),fromfile='frozen_author/check_analytic_fluid_v1.py',tofile=name+'/check_analytic_fluid_v1.py'))
    (path/'MUTATION.diff').write_text(patch)
    before=hashlib.sha256(source.read_bytes()).hexdigest()
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    child=subprocess.run([sys.executable,str(path/'run_off_trajectory_only.py')],cwd=path,env=env,capture_output=True,text=True,timeout=30)
    ended=datetime.datetime.now(datetime.timezone.utc).isoformat()
    (path/'stdout.txt').write_text(child.stdout);(path/'stderr.txt').write_text(child.stderr)
    results=json.loads((path/'RESULTS.json').read_text()) if (path/'RESULTS.json').exists() else None
    fails=[c for c in results['checks'] if not c['passed']] if results else []
    families=collections.Counter(' '.join(c['name'].split()[:-1]) for c in fails)
    record={'mutation':name,'started_at':started,'ended_at':ended,'exit_code':child.returncode,
            'original_source_sha256':hashlib.sha256(ORIGINAL.encode()).hexdigest(),'mutant_source_sha256':before,
            'source_unchanged':before==hashlib.sha256(source.read_bytes()).hexdigest(),
            'fixture_sha256':hashlib.sha256(FIXTURE).hexdigest(),
            'preserved_failure_count':len(fails),'failure_families':dict(families),
            'max_tolerance_units':max((c.get('max_tolerance_units',0) for c in fails),default=0),
            'mutation_detected_by_actual_control_failure':child.returncode==1 and bool(fails)}
    (path/'EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
    records.append(record);print(json.dumps(record,sort_keys=True),flush=True)

out={'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'records':records,
     'all_four_detected':all(r['mutation_detected_by_actual_control_failure']for r in records)}
(ROOT/'MUTATION_SUMMARY_v1.json').write_text(json.dumps(out,indent=2)+'\n')
raise SystemExit(0 if out['all_four_detected'] else 1)
