from pathlib import Path
import sys,types,json,copy,tempfile,shutil,hashlib
W=Path(__file__).resolve().parents[4];sys.path.insert(0,str(W/'scripts'))
import ens_physical_parity_2026_09_27 as original
import ens_cavity_holdout_2026_09_27 as primary
full=json.load(open(W/'outputs/ens_cavity_holdout_2026_09_27.json'));source=(W/'scripts/ens_physical_parity_2026_09_27.py').read_text();results=[]
def attempt(name,fn):
 try:fn()
 except AssertionError as e:results.append({'mutation':name,'rejected':True,'message':str(e)})
 else:results.append({'mutation':name,'rejected':False})
def module(text):
 m=types.ModuleType('fault_only');exec(compile(text,'fault_only','exec'),m.__dict__);return m
attempt('remove physical offset displacement factor',lambda:module(source.replace('q*(1-delta)','q')).construct_parity(copy.deepcopy(full)))
m=module(source);base=m.physical
def altered(p,q,**kw):
 f,d=base(p,q,**kw)
 if kw.get('N')==24:f=f.copy();f[5]+=2e-9
 return f,d
m.physical=altered;attempt('two Hz fine-cutoff perturbation',lambda:m.construct_parity(copy.deepcopy(full)))
attempt('independent physical coupling reverted to n',lambda:module(source.replace('physical_offset=True','physical_offset=False')).construct_parity(copy.deepcopy(full)))
attempt('period discrepancy injected two Hz',lambda:module(source.replace("assert abs(period)<1.","period+=2.; assert abs(period)<1.")).construct_parity(copy.deepcopy(full)))
attempt('quarter parity splitting perturbed',lambda:module(source.replace("assert pairs[16]['splitting_MHz']<1e-6","pairs[16]['splitting_MHz']+=.01; assert pairs[16]['splitting_MHz']<1e-6")).construct_parity(copy.deepcopy(full)))
figure=json.load(open(W/'scripts/data/ens_cavity_holdout_2026_09_27/ramsey_figure7_bins.json'));pred=copy.deepcopy(full['physical_parity'])
for r in pred.values():r['numerical_maximum_MHz']/=6
attempt('incorrect division of Ramsey energy envelope by six',lambda:original.compare_figure(pred,figure))
with tempfile.TemporaryDirectory(prefix='ens-parity-fault-') as d:
 d=Path(d);shutil.copy2(primary.DATA,d/'Experiment.csv');f=copy.deepcopy(figure);f['rows'][0]['bins'][0]['center_MHz']+=.01;(d/'ramsey_figure7_bins.json').write_text(json.dumps(f));primary.DATA=d/'Experiment.csv';primary.construct=lambda calibration:copy.deepcopy(full)
 attempt('digitized data changed after fixed hash',primary.main)
record={'scope':'Scratch/isolated mutations of new parity checks only; inherited calibration families not rerun here. No real source or result inputs modified.','helper_sha256':hashlib.sha256(source.encode()).hexdigest(),'primary_sha256':hashlib.sha256((W/'scripts/ens_cavity_holdout_2026_09_27.py').read_bytes()).hexdigest(),'controls':results};p=W/'.claude/science/physics-loops/ens-cavity-holdout-20260927/PARITY_PUBLICATION_FAULT_CONTROLS.json';p.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2));assert all(x['rejected'] for x in results)
