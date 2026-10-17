"""Bounded copied-code scientific discriminators; no source-input corruption."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

D = Path(__file__).resolve().parent
W = D.parents[1]/'correlation_worktree'
O = D/'mutations'
O.mkdir(exist_ok=False)
primary=W/'scripts/structural_coefficient_box_2026_10_17.py'
helper=W/'scripts/structural_coefficient_box_check_2026_10_17.py'
bases={'author':primary.read_text(),'independent':helper.read_text()}
cases=[
 ('coefficient_box_overextension','author','a = F(1, 10**8)','a = F(1, 10**6)','assert eta < F(1226, 10**10) and A*eta < 1'),
 ('inverse_ceiling_overextension','author','A = F(166)','A = F(167)','assert actual_inverse_bound < 167'),
 ('omitted_closed_tail_variation','author','eta = b+c+J*J*b/(g*(g-b))','eta = b+c',"assert author['constants']['extra_reflection_error']['exact_rational'] == independent['derived_bounds']['extra_reflection']['exact']"),
 ('lost_vacuum_darkness','independent',"derivatives = {'DeltaA': nA,", "derivatives = {'DeltaA': eye-nA,",'DeltaA_annihilates_full_vacuum_embedding'),
 ('closed_surface_sign','independent','G = q/J','G = -q/J','surface_endpoint_1/7'),
 ('noncommuting_resolvent_order','independent',"zero('noncommuting_resolvent_identity', Rs-Rt+Rs*dHt*Rt)","zero('noncommuting_resolvent_identity', Rs-Rt+Rs*Rt*dHt)",'noncommuting_resolvent_identity'),
 ('common_phase_sign','independent','zeta = -alpha/z**4','zeta = alpha/z**4','nominal_common_phase_contract'),
 ('finite_clock_horizon_overextension','independent','T, N, M, Tobs = 10**13, 22*10**12, 9*10**14, 4*10**13','T, N, M, Tobs = 10**13, 22*10**12, 9*10**14, 5*10**13','finite_clock_chebyshev_exponent_margin'),
]
def pin(raw): return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
plan={'scope':'Scientific rejection tests, not additional independent theorem evidence. Frozen sources/inputs unchanged. Only an intended scientific assertion failure counts; a checksum failure, timeout or syntax failure does not.',
      'declared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'max_cases':8,'max_attempts_per_case':1,'per_case_cpu_cap_seconds':60,'per_case_external_wall_cap_seconds':20,
      'source_pins':{'author':pin(primary.read_bytes()),'independent':pin(helper.read_bytes())},
      'cases':[dict(zip(('name','source_role','old','new','expected_scientific_assertion'),c)) for c in cases]}
(O/'PLAN.json').write_text(json.dumps(plan,indent=2)+'\n')
env=os.environ.copy()
env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONPATH=str(W/'scripts'))
records=[]
for name,role,old,new,expected in cases:
    base=bases[role]
    assert base.count(old)==1,(name,base.count(old))
    folder=O/name
    folder.mkdir()
    code=base.replace(old,new,1)
    if role=='author':
        code=code.replace('REPO = Path(__file__).resolve().parents[1]','REPO = Path('+repr(str(W))+')',1)
        code=code.replace("REPO/'outputs/structural_coefficient_box_2026_10_17.json'",'Path('+repr(str(folder/'unexpected_result.json'))+')',1)
    else:
        code+='\nimport resource\nresource.setrlimit(resource.RLIMIT_CPU,(60,60))\nrun_independent_checks(Path('+repr(str(W/'outputs/structural_coefficient_box_2026_10_17_inputs/review'))+'))\n'
    script=folder/'mutated.py'
    script.write_text(code)
    started=datetime.datetime.now(datetime.timezone.utc).isoformat(); clock=time.monotonic()
    try:
        proc=subprocess.run([sys.executable,str(script)],cwd=W,env=env,capture_output=True,timeout=20)
        stdout,stderr,exit_code,timed_out=proc.stdout,proc.stderr,proc.returncode,False
    except subprocess.TimeoutExpired as exc:
        stdout,stderr,exit_code,timed_out=exc.stdout or b'',exc.stderr or b'',None,True
    elapsed=time.monotonic()-clock
    (folder/'stdout').write_bytes(stdout); (folder/'stderr').write_bytes(stderr)
    rejected=(exit_code==1 and b'AssertionError' in stderr and expected.encode() in stderr)
    row={'name':name,'source_role':role,'started_utc':started,'elapsed_seconds':elapsed,
         'exit_code':exit_code,'timed_out':timed_out,'cpu_cap_seconds':60,'external_wall_cap_seconds':20,
         'old':old,'new':new,'expected_scientific_assertion':expected,'scientific_assertion_rejected':rejected,
         'source':pin(script.read_bytes()),'stdout':pin(stdout),'stderr':pin(stderr)}
    (folder/'EXECUTION.json').write_text(json.dumps(row,indent=2)+'\n')
    records.append(row)
    (O/'RESULTS.json').write_text(json.dumps({'scope':plan['scope'],'plan':pin((O/'PLAN.json').read_bytes()),'cases':records},indent=2)+'\n')
    if not rejected:
        raise SystemExit('Unexpected mutation result retained: '+name)
print(json.dumps({'cases':len(records),'all_expected_scientific_rejections':True,'elapsed_seconds':sum(x['elapsed_seconds'] for x in records)}))
