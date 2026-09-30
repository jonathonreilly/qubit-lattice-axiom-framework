#!/usr/bin/env python3
"""Source-recoverable negative controls, not a second scientific primary."""
from pathlib import Path
import subprocess,sys,json,hashlib,difflib,time,datetime,gzip,os
root=Path(__file__).resolve().parents[4]
p=Path(__file__).resolve().parent
primary=root/'scripts/original_record_thermodynamic_dynamics_and_energy_density_2026_09_30.py'
original=primary.read_text()
cases=[
 ('hop_charge_sign','sf[d]=-q','sf[d]=q','star_controls'),
 ('birth_charge_sign','wb[b]=-sigma','wb[b]=sigma','star_controls'),
 ('coherent_output_identity','channels[b,sigma][(sigma,tuple(wb))]','channels[b,sigma][(q,tuple(wb))]','star_controls'),
 ('loss_pairing','loss_half=F(1,2)','loss_half=F(1,1)','star_controls'),
 ('original_Gamma_factor','v=2*(5-o)*value','v=(5-o)*value','star_controls'),
 ('omit_diagonal_pairs','ds|={add(scale(s,e[i]),scale(t,e[j]))','ds|={add(scale(s,e[i]),scale(t,e[j]))','geometry_controls'),
 ('connected_count','assert c<=16641**n','assert c<=16000**n','series_controls'),
 ('timestamp_simplex','coeff[j]/math.factorial(n-j)','coeff[j]','series_controls'),
 ('power_majorant','partial<=exact<=240*z','partial<=exact<=200*z','series_controls'),
 ('circulation_increment','after=4*(j+1)**2','after=4*(j-1)**2','domain_controls'),
 ('boundary_shift_bandwidth','M=length;r=F(1,3)','M=1;r=F(1,3)','domain_controls'),
]
out=p/'mutations';out.mkdir(exist_ok=True);results=[]
for name,old,new,fn in cases:
 runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
 assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
 assert not any((runtime/s).exists() for s in ('STOP_REQUESTED.json','STOP_CAMPAIGN.json'))
 if name=='omit_diagonal_pairs':
  old='for i,j in itertools.combinations(range(3),2) for s,t in itertools.product((-1,1),repeat=2)}'
  new='for i,j in [] for s,t in itertools.product((-1,1),repeat=2)}'
 assert original.count(old)==1,(name,original.count(old))
 mutated=original.replace(old,new)
 script=out/(name+'.py');script.write_text(mutated+'\n'+fn+'()\n')
 # Suppress the primary main call only in the actual recoverable mutant.
 source=script.read_text().replace("if __name__=='__main__':main()", "# Main suppressed: invoke the named actual finite control below.")
 script.write_text(source)
 st=time.monotonic();r=subprocess.run([sys.executable,str(script)],cwd=root,text=True,capture_output=True,timeout=20)
 stdout=out/(name+'.stdout.gz');stderr=out/(name+'.stderr.gz')
 stdout.write_bytes(gzip.compress(r.stdout.encode(),mtime=0));stderr.write_bytes(gzip.compress(r.stderr.encode(),mtime=0))
 results.append({'name':name,'control':fn,'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'primary_sha256':hashlib.sha256(original.encode()).hexdigest(),'replacement':{'old':old,'new':new},'exit_code':r.returncode,'wall_seconds':time.monotonic()-st,'stdout_sha256':hashlib.sha256(r.stdout.encode()).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr.encode()).hexdigest(),'assertion_detected':r.returncode!=0 and 'AssertionError' in r.stderr})
(p/'MUTATION_RESULTS.json').write_text(json.dumps({'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cases':results,'scope':'Tests detect these finite-law/control corruptions; no CP/thermodynamic theorem is certified by mutation count.'},indent=2)+'\n')
print(json.dumps({'mutations':len(results),'rejected':sum(x['assertion_detected'] for x in results),'survivors':[x['name'] for x in results if not x['assertion_detected']]}))
assert all(x['assertion_detected'] for x in results)
