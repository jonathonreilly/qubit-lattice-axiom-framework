from pathlib import Path
import tempfile,shutil,subprocess,os,json
root=Path(__file__).resolve().parents[2];src=(root/'scripts/collective_corner_response.py').read_text()
cases={'omit_degenerate':('D[deg]=(fm*(1-fm)/T)[deg]','D[deg]=0'),'double_folded':('sum()/(2*len(h))','sum()/len(h)'),'wrong_dynamic_factor':('de**2/(Delta','unused')}
cases['wrong_dynamic_factor']=('de**2,de**2+om**2','de**2+om**2,de**2')
out=[]
for name,(old,new) in cases.items():
 assert old in src,name
 with tempfile.TemporaryDirectory(prefix='collective-mutation-') as d:
  p=Path(d);(p/'scripts').mkdir();shutil.copytree(root/'data/collective_corner_response',p/'data/collective_corner_response')
  (p/'scripts/collective_corner_response.py').write_text(src.replace(old,new))
  r=subprocess.run(['/usr/local/bin/python3',str(p/'scripts/collective_corner_response.py')],capture_output=True,text=True,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'},timeout=120)
  out.append(dict(mutation=name,exit_code=r.returncode,detected=r.returncode!=0,stderr=r.stderr[-1200:]))
assert all(x['detected'] for x in out)
(root/'outputs/collective_corner_response/mutations.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
