"""Source-mutant challenge driver; archival validation, not the physics runner."""
AUDIT_TIMEOUT_SEC = 120
from pathlib import Path
import gzip, hashlib, json, os, shutil, subprocess, sys, tempfile, time
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'outputs/scalar_metric_inverse/mutations'
MUTATIONS=[
 ('geometry_lapse','scalar_metric_geometry.py','gtt=-1+2*eps*psi*co','gtt=-1+3*eps*psi*co'),
 ('constraint_raychaudhuri','scalar_metric_constraints.py','H:-(r+v*v)/(2*M*M)','H:-(r+v*v)/(3*M*M)'),
 ('coefficient_coupling','scalar_metric_coefficients.py','ee = 2*b*b','ee = 3*b*b'),
 ('varying_log_derivative','scalar_metric_varying_coupling.py','Lval=Bp/(2*BB)','Lval=Bp/BB'),
 ('joint_gain_coupling','scalar_metric_joint_gain.py','qq=BB*trace[2];','qq=trace[2];'),
 ('photon_mixed_derivative','scalar_metric_photon_map.py','lapcone=lambda f:(s.diff(f,r,2)+2*s.diff(f,r,u)+s.diff(f,u,2)','lapcone=lambda f:(s.diff(f,r,2)+s.diff(f,r,u)+s.diff(f,u,2)'),
 ('transport_characteristic','scalar_metric_transport.py','T=lambda f:s.diff(f,r)+2*s.diff(f,u)+Hc*f','T=lambda f:s.diff(f,r)+s.diff(f,u)+Hc*f'),
 ('spherical_curvature','scalar_metric_fixed_background.py','D=Lam-C*C-C/r','D=Lam-C*C'),
 ('conditioning_stencil','scalar_metric_conditioning.py','w0=-ri*ri/(dr*dr)','w0=-ri*ri/(2*dr*dr)'),
 ('kernel_polynomial','scalar_metric_local_kernels.py','2*ss2/lam**2+ss1*mu/lam','3*ss2/lam**2+ss1*mu/lam'),
 ('nonsingular_reconstruction','scalar_metric_local_kernels.py','s.diff(N,r)-cc*N-D*f','s.diff(N,r)-cc*N+D*f'),
 ('planar_geometry','scalar_metric_local_kernels.py','s.exp(Z+s.sqrt(14)*X)','s.exp(Z+s.sqrt(13)*X)'),
]
def main():
 OUT.mkdir(exist_ok=True); results=[]
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
 for name,filename,old,new in MUTATIONS:
  original=(ROOT/'scripts'/filename).read_text(); count=original.count(old)
  if count!=1: raise RuntimeError(f'{name}: expected one source replacement, got {count}')
  mutant=original.replace(old,new,1)
  with tempfile.TemporaryDirectory(prefix='metric-mutant-') as td:
   d=Path(td); (d/filename).write_text(mutant)
   harness='import json;from '+Path(filename).stem+' import run_checks;c,d=run_checks();print(json.dumps(c));raise SystemExit(int(any(not x["pass"] for x in c)))'
   start=time.monotonic();p=subprocess.run([sys.executable,'-B','-c',harness],cwd=d,env=env,capture_output=True,timeout=120)
   stem=OUT/name;(stem.with_suffix('.py.gz')).write_bytes(gzip.compress(mutant.encode(),mtime=0));stem.with_suffix('.stdout.gz').write_bytes(gzip.compress(p.stdout,mtime=0));stem.with_suffix('.stderr.gz').write_bytes(gzip.compress(p.stderr,mtime=0))
   try:checks=json.loads(p.stdout);failed=[x for x in checks if x.get('pass') is False]
   except (ValueError,TypeError):failed=[]
   results.append({'name':name,'source':filename,'source_sha256':hashlib.sha256(original.encode()).hexdigest(),'mutant_sha256':hashlib.sha256(mutant.encode()).hexdigest(),'old':old,'new':new,'exit_code':p.returncode,'elapsed_seconds':time.monotonic()-start,'failed_scientific_controls':failed,'detected_without_crash':p.returncode==1 and bool(failed) and not p.stderr,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()})
 report={'scope':'Actual source perturbations; failures must be scientific predicates, not exceptions or integrity-only checks','results':results,'detected':sum(x['detected_without_crash'] for x in results),'total':len(results),'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (OUT/'RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'detected':report['detected'],'total':report['total'],'not_detected':[x['name'] for x in results if not x['detected_without_crash']]}))
 raise SystemExit(int(report['detected']!=report['total']))
if __name__=='__main__':main()
