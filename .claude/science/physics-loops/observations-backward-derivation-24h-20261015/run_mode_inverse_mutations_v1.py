"""Run declared source mutations on temporary copies; retain actual failures."""
import difflib
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

p=Path(__file__).resolve().parent
out=p/'mode_inverse_mutations_v1'
out.mkdir(exist_ok=True)
cases=[
 ('coupling_quotient_damping','check_mode_inverse_v1.py','aa = 3*ell-2*L','aa = 3*ell-L'),
 ('fixed_density_clock_curvature','check_mode_inverse_v1.py','cc = deff+L*L-s.diff(L, tau)-3*ell*L','cc = deff+L*L+s.diff(L, tau)-3*ell*L'),
 ('clock_second_derivative','check_mode_inverse_v1.py','jpp = dpi/tt**2-piv/tt**3','jpp = dpi/tt**2'),
 ('dust_momentum_sign','check_mode_inverse_v1.py','pd = (vv*uv-rr*vel)/2-HH*pv','pd = (vv*uv+rr*vel)/2-HH*pv'),
 ('missing_coupling_curvature','check_mode_inverse_jets_v1.py','mu=s.diff(V,phi,2)+(gamma+b*b)*r','mu=s.diff(V,phi,2)+b*b*r'),
 ('coefficient_jet_cross_term','check_mode_inverse_jets_v1.py','y2-d2@th0-2*d1@th1','y2-d2@th0-d1@th1'),
 ('common_gain_curvature_transform','check_mode_gain_v1.py','ct=c-a*drift-s.diff(drift,tau)+drift**2','ct=c-a*drift+s.diff(drift,tau)+drift**2'),
 ('common_gain_inverse_curvature','check_mode_gain_jets_v1.py','physical_c=ct+at*drift+drift*drift+driftp','physical_c=ct+at*drift-drift*drift+driftp'),
]
dependencies=['MODE_INVERSE_DERIVATION_v1.md','MODE_INVERSE_NEUTRAL_CONTRACT_v1.json',
 'SCALAR_RESPONSE_DERIVATION_v1.md','SCALAR_RESPONSE_CLOSURE_v1.md','MATTER_CLOCK_DERIVATION_v2.md',
 'MODE_GAIN_DERIVATION_v1.md','MODE_INVERSE_CONTROLS_v1.json']
results=[]
for name,script,before,after in cases:
    original=(p/script).read_text()
    if original.count(before)!=1:raise RuntimeError('nonunique mutation '+name)
    changed=original.replace(before,after,1)
    patch=''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile=script,tofile=name+'/'+script))
    (out/(name+'.diff')).write_text(patch)
    with tempfile.TemporaryDirectory(prefix='mode-inverse-mutant-') as tmp:
        task=Path(tmp)
        for dep in dependencies:shutil.copy2(p/dep,task/dep)
        (task/script).write_text(changed)
        run=subprocess.run(['/usr/local/bin/python3','-B',str(task/script)],capture_output=True,text=True,timeout=120)
    for suffix,value in [('stdout',run.stdout),('stderr',run.stderr)]:
        (out/(name+'.'+suffix+'.gz')).write_bytes(gzip.compress(value.encode(),mtime=0))
    parsed=None
    try:parsed=json.loads(run.stdout)
    except json.JSONDecodeError:pass
    failed=[] if parsed is None else [z['name'] for z in parsed['checks'] if not z['pass']]
    # An exception or missing output is not a successful targeted rejection.
    detected=run.returncode==1 and parsed is not None and parsed['failed']>0
    results.append({'case':name,'script':script,'source_sha256':hashlib.sha256(original.encode()).hexdigest(),
                    'mutated_sha256':hashlib.sha256(changed.encode()).hexdigest(),
                    'exit_code':run.returncode,'detected_by_failing_scientific_predicate':detected,'failed_checks':failed,
                    'stdout_sha256':hashlib.sha256(run.stdout.encode()).hexdigest(),'stderr_sha256':hashlib.sha256(run.stderr.encode()).hexdigest()})
report={'author':'/root','purpose':'Actual source-mutant executions, separate from analytic omission witnesses in the primary script',
        'cases':results,'passed':sum(v['detected_by_failing_scientific_predicate'] for v in results),
        'failed':sum(not v['detected_by_failing_scientific_predicate'] for v in results),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(out/'REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));raise SystemExit(int(report['failed']>0))
