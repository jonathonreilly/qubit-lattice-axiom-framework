#!/usr/bin/env python3
"""Mutation diagnostics on the exact frozen author source; no source edits."""
import hashlib,json,subprocess,sys,time
from pathlib import Path
base=Path(__file__).resolve().parent
rev='0ea4e56c4c00da4e70863eb274cbee987b7bd917'
source_path='.claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks/source_return_exact.py'
source=subprocess.check_output(['git','show',rev+':'+source_path],text=True)
assert hashlib.sha256(source.encode()).hexdigest()=='a41aec8a773fbd2f00f9cf675186f5aa4d62395602fe55b687f88656d44b03aa'
mutants=[
 ('parametrix_sign',[('r[i][j] = -r[i][j] if i not in omega else F(0)','r[i][j] = r[i][j] if i not in omega else F(0)')]),
 ('neumann_order',[('term = mul(term, r)','term = mul(r, term)')]),
 ('missing_collar',[('support = omega | {((x+j) % n) for x in omega for j in (-1, 1)}','support = omega')]),
 ('common_logdet_half',[('via_perm = -ddet/(2*det)','via_perm = -ddet/det'),('via_trace = -inverse(kd)[0][0]/2','via_trace = -inverse(kd)[0][0]')]),
 ('missing_marked_right',[('major_b = bp*sum(mr**j for j in range(4)) + mp*br*sum(j*mr**(j-1) for j in range(1, 4))','major_b = bp*sum(mr**j for j in range(4))')]),
 ('contour_side_sign',[('side = face_integral(pwidth)-face_integral(-pwidth)','side = face_integral(-pwidth)-face_integral(pwidth)')]),
]
records=[]
for name,changes in mutants:
    changed=source
    for old,new in changes:
        assert changed.count(old)==1,(name,old)
        changed=changed.replace(old,new)
    path=base/f'review_source_return_author_{name}.py'
    path.write_text(changed)
    start=time.monotonic()
    try:
        run=subprocess.run([sys.executable,'-B',str(path)],capture_output=True,text=True,timeout=60)
        stdout,stderr=run.stdout,run.stderr
        exit_code=run.returncode
        timed_out=False
    except subprocess.TimeoutExpired as e:
        stdout=e.stdout or '';stderr=e.stderr or ''
        if isinstance(stdout,bytes):stdout=stdout.decode(errors='replace')
        if isinstance(stderr,bytes):stderr=stderr.decode(errors='replace')
        exit_code=None;timed_out=True
    out=base/f'review_source_return_author_{name}_out.json'
    err=base/f'review_source_return_author_{name}_err.txt'
    out.write_text(stdout);err.write_text(stderr)
    try:
        result=json.loads(stdout)
        failed=[k for k,v in result.get('gates',{}).items() if not v]
        all_passed=result.get('all_passed')
    except json.JSONDecodeError:
        failed=[];all_passed=None
    records.append({'name':name,'changes':changes,'sha256':hashlib.sha256(changed.encode()).hexdigest(),'exit_code':exit_code,'timed_out':timed_out,'all_passed':all_passed,'failed_gates':failed,'seconds':time.monotonic()-start,'stdout':out.name,'stderr':err.name})
    print(json.dumps(records[-1]),flush=True)
(base/'review_source_return_author_controls_out.json').write_text(json.dumps({'source_commit':rev,'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'baseline_replay':'Not rerun: coordinator already reproduced the exact 21 predicates; this driver tests altered copies only.','records':records},indent=2)+'\n')
