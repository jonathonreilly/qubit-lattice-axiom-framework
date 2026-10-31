from pathlib import Path
import subprocess,json,hashlib,time,sys
root=Path(__file__).parent
exact=(root/'source_return_cont_exact.py').read_text()
ball=(root/'source_return_cont_ball.py').read_text()
mutations=[
 ('source_force',exact,'ref_U = lambda w: eps * (B * w / sigma + w ** 2 / 2)','ref_U = lambda w: eps * (w ** 2 / 2)'),
 ('normalization',exact,'ratio = sp.cancel(pin / total)','ratio = sp.cancel(pin)'),
 ('remote_endpoint',exact,'pin_insert += w[1] * density / 32','pin_insert += density / 32'),
 ('jacobian',exact,'J = sigma ** 2 * C.det()','J = sigma ** 2 * C0.det()'),
 ('orientation',exact,'sum(upper - lower for upper, lower in fluxes)','sum(upper + lower for upper, lower in fluxes)'),
 ('action_prefactor',exact,'fixed_reference = sigma * mp.exp(-eps * B ** 2 / (2 * sigma ** 2)) * mp.quad','fixed_reference = sigma * mp.quad'),
 ('sphere_radius',ball,'surface = 4 * sp.pi * r ** 2 * sp.exp','surface = 4 * sp.pi * sp.exp'),
 ('ball_scalar_dimension',ball,'radial = lambda t: C(t) ** 3 *','radial = lambda t: C(t) *')
]
report=[]
for name,source,before,after in mutations:
    assert source.count(before)==1,(name,source.count(before))
    mutated=source.replace(before,after)
    path=root/('review_source_cont_mutant_'+name+'.py')
    path.write_text(mutated)
    started=time.monotonic()
    proc=subprocess.run([sys.executable,str(path)],capture_output=True,text=True,timeout=60)
    stdout=root/('review_source_cont_mutant_'+name+'.json')
    stderr=root/('review_source_cont_mutant_'+name+'.stderr')
    stdout.write_text(proc.stdout);stderr.write_text(proc.stderr)
    payload=json.loads(proc.stdout)
    failed=[key for key,value in payload['checks'].items() if not value]
    report.append({'name':name,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'exit_code':proc.returncode,'failed_predicates':failed,'elapsed_seconds':time.monotonic()-started,'stdout':str(stdout),'stderr':str(stderr),'mutation_before':before,'mutation_after':after})
    assert proc.returncode==1 and failed,(name,proc.returncode,failed)
print(json.dumps({'mutations':report,'all_rejected':all(r['exit_code']==1 and r['failed_predicates'] for r in report)},indent=2))
