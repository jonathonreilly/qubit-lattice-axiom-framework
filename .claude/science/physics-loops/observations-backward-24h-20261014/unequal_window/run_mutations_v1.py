"""Actual isolated source mutations of M16's mathematical operators."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib, json, subprocess, sys, time
ROOT=Path(__file__).resolve().parents[5]
HERE=Path(__file__).resolve().parent
OUT=HERE/'mutations_v1'
OUT.mkdir(exist_ok=True)
CASES=[
 ('geometry_U_sign','scalar_unequal_geometry.py','U = s.factor(s.diff(gamma, A))','U = -s.factor(s.diff(gamma, A))',1),
 ('geometry_six_annihilators','scalar_unequal_geometry.py','range(7)','range(6)',3),
 ('geometry_spatial_missing_product_term','scalar_unequal_geometry.py','kap*pg(ff)-s.diff(kap,r)*ff-kap*kap*pg(rr)','kap*pg(ff)-kap*kap*pg(rr)',1),
 ('sampling_frozen_y_adjoint','scalar_unequal_sampling.py','Ts=lambda f:-s.diff(y*f,n)+c*f','Ts=lambda f:-y*s.diff(f,n)+c*f',1),
 ('sampling_reversed_spatial_adjoint','scalar_unequal_sampling.py','ksu=-Ds(Ps(Ls(z)))','ksu=-Ds(Ls(Ps(z)))',1),
 ('sampling_born_factor_two','scalar_unequal_sampling.py','psi=s.integrate((1/t-1/q)*t**degree,(t,0,q))','psi=s.integrate(2*(1/t-1/q)*t**degree,(t,0,q))',1),
 ('sampling_spin_factor_half','scalar_unequal_sampling.py','Q=s.Rational(2,M)','Q=s.Rational(1,M)',1),
 ('sampling_auto_including_self_normalization','scalar_unequal_sampling.py','if i!=j)/6','if i!=j)/9',1),
]
HARNESS="""import importlib.util,json,sys,traceback
from pathlib import Path
try:
 spec=importlib.util.spec_from_file_location('variant',sys.argv[1])
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 result=module.controls()
 failures=[x for x in result['checks'] if not x['passed']]
 Path(sys.argv[2]).write_text(json.dumps({'checks':result['checks'],'failed':failures},indent=2)+'\\n')
 print(json.dumps({'checks':len(result['checks']),'failed':len(failures)}))
 raise SystemExit(bool(failures))
except Exception:
 traceback.print_exc()
 raise SystemExit(2)
"""
(OUT/'harness.py').write_text(HARNESS)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(case,filename,before=None,after=None,count=0):
 source=ROOT/'scripts'/filename
 text=source.read_text()
 if before is not None:
  assert text.count(before)==count,(case,text.count(before),count)
  text=text.replace(before,after)
 directory=OUT/case;directory.mkdir(exist_ok=True)
 variant=directory/filename;variant.write_text(text)
 started=time.monotonic()
 proc=subprocess.run([sys.executable,str(OUT/'harness.py'),str(variant),str(directory/'RESULTS.json')],text=True,capture_output=True,timeout=90)
 elapsed=time.monotonic()-started
 (directory/'stdout.txt').write_text(proc.stdout);(directory/'stderr.txt').write_text(proc.stderr)
 result=json.loads((directory/'RESULTS.json').read_text()) if (directory/'RESULTS.json').exists() else None
 return {'case':case,'base_source':str(source.relative_to(ROOT)),'base_sha256':sha(source),'variant_sha256':sha(variant),'selector':before,'replacement':after,'expected_matches':count,'exit_code':proc.returncode,'elapsed_seconds':elapsed,'checks':len(result['checks']) if result else None,'failed_checks':[x['name'] for x in result['failed']] if result else None,'classification':'baseline_pass' if before is None and proc.returncode==0 else 'detected_by_failed_controls' if proc.returncode==1 and result and result['failed'] else 'exception' if proc.returncode==2 else 'unexpected'}
baselines=[run('baseline_geometry','scalar_unequal_geometry.py'),run('baseline_sampling','scalar_unequal_sampling.py')]
assert all(x['classification']=='baseline_pass' for x in baselines),baselines
with ThreadPoolExecutor(max_workers=2) as pool:
 rows=list(pool.map(lambda c:run(*c),CASES))
report={'created_utc':datetime.now(timezone.utc).isoformat(),'scope':'Actual source mutations in isolated copies; failure detection does not prove the theorem','baselines':baselines,'mutations':rows,'counts':{'mutations':len(rows),'failed_controls':sum(x['classification']=='detected_by_failed_controls' for x in rows),'exceptions':sum(x['classification']=='exception' for x in rows)}}
(OUT/'REPORT_v1.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
raise SystemExit(any(x['classification']!='detected_by_failed_controls' for x in rows))
