from pathlib import Path
import tempfile,shutil,subprocess,os,json,sys
root=Path(__file__).resolve().parents[2];src=(root/'scripts/microscopic_flux_interaction.py').read_text()
cases={'flux_changing_hop':('hops=[A(q,r) for q,r in edges];charges=','hops=[A(q,r) for q,r in edges]+[(0,1,0)];charges='),'wrong_schur_sign':('A0-h[:2,2:]@','A0+h[:2,2:]@'),'wrong_fermion_commutator':('comm=lambda a,b:a@b-b@a','comm=lambda a,b:a@b+b@a')}
out=[]
for name,(old,new) in cases.items():
 assert old in src
 with tempfile.TemporaryDirectory(prefix='micro-flux-mutation-') as d:
  p=Path(d);(p/'scripts').mkdir()
  dep='corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17.py'
  shutil.copy(root/'scripts'/dep,p/'scripts'/dep)
  (p/'scripts/microscopic_flux_interaction.py').write_text(src.replace(old,new))
  r=subprocess.run([sys.executable,str(p/'scripts/microscopic_flux_interaction.py')],capture_output=True,text=True,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'},timeout=120)
  result=json.loads((p/'outputs/microscopic_flux_interaction/result.json').read_text())
  out.append({'mutation':name,'exit_code':r.returncode,'failed_checks':[k for k,v in result['checks'].items() if not v]})
assert all(x['exit_code'] and x['failed_checks'] for x in out)
(root/'outputs/microscopic_flux_interaction/mutations.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
