"""Actual source-copy discriminators for the final walk primary candidate."""
from pathlib import Path
from hashlib import sha256
import json, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
out=Path(__file__).resolve().parent
source=out.parent/'root_walk_primary.py'
text=source.read_text()
changes=[
 ('resolvent_channel_numerator','uu = sum((x+y)**2 for x,y in zip(a,b))','uu = sum((x-y)**2 for x,y in zip(a,b))','singlet resolvent from exact matrix inverse'),
 ('corner_atom_measure','fs += sum(cs[j]**2 for j in range(r))/eps2/8','fs += sum(cs[j]**2 for j in range(r))/eps2/4','total-corner contact atom'),
 ('auxiliary_contact_resolvent','scale(C,-1/z)','scale(C,1/z)','compressed resolvent including auxiliary contact eigenstate'),
 ('on_shell_h_factor','row = [[Q(1),E]]','row = [[Q(1),2*E]]','stationary on-shell auxiliary-matrix reduction'),
 ('current_scattering_adjoints','expected = add(scale(mul(w,star(v)),s-1),scale(mul(v,star(w)),s.conj()-1))','expected = add(scale(mul(w,star(v)),s.conj()-1),scale(mul(v,star(w)),s-1))','coherent current change adjoints'),
 ('missing_relative_corners','rho = 4/pi**2*sum','rho = 2/pi**2*sum','eight-cone spectral-density normalization'),
 ('axis_only_dipole','Hdiff={n:M for La in L for n,M in La.items()}','Hdiff=L[0]','original-position free-current identity'),
 ('canonical_contact_sign','F(-1,2))','F(1,2))','canonical finite-rank correction sign and coefficient'),
 ('coherent_phase_reversal','chi = add(v,scale(u,Q(0,1)))','chi = add(v,scale(u,Q(0,-1)))','nonzero coherent packet current change'),
 ('angular_measure_denominator','odd_double_factorial(sum(indices)+1)','odd_double_factorial(sum(indices)+3)','continuum angular second and fourth moments'),
 ('cook_tail_denominator','tail=1/(F(r-1)*T**(r-1))','tail=1/(T**(r-1))','integrated Cook tail denominator'),
 ('packet_time_scale','r=7;time_power=F(3,2)','r=7;time_power=F(1)','finite-time coherent packet separation powers'),
]
def run(row):
    name,path,before,after,expected=row
    log=out/(name+'.log');start=time.monotonic()
    with log.open('w') as f:
        p=subprocess.run([sys.executable,str(path)],stdout=f,stderr=subprocess.STDOUT,timeout=180)
    output=log.read_text()
    success=(p.returncode==0) if expected is None else (p.returncode==1 and 'AssertionError: '+expected in output)
    return {'name':name,'source':path.name,'sha256':sha256(path.read_bytes()).hexdigest(),'before':before,'after':after,'expected_assertion':expected,'command':[sys.executable,str(path)],'exit_code':p.returncode,'expected_result':success,'seconds':time.monotonic()-start,'log':log.name}
rows=[('baseline',source,None,None,None)]
for name,before,after,expected in changes:
    assert text.count(before)==1,(name,text.count(before))
    path=out/('mutant_'+name+'.py');path.write_text(text.replace(before,after,1))
    rows.append((name,path,before,after,expected))
with ThreadPoolExecutor(max_workers=3) as pool:
    results=list(pool.map(run,rows))
manifest={'baseline_sha256':sha256(source.read_bytes()).hexdigest(),'timeout_seconds':180,'executions':results}
(out/'mutation_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
for row in results:print(json.dumps(row),flush=True)
assert all(r['expected_result'] for r in results)
print('Baseline and all 12 actual scientific source mutations produced intended results.')
