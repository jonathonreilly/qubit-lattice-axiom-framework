"""Resolve the failed 128/256 phase-grid control without relaxing tolerance."""
from pathlib import Path
import importlib.util,json,hashlib
import numpy as np
from scipy.linalg import expm
D=Path(__file__).resolve().parent
p=D/'second_event_probe.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='4827171a51e018b306302b0fac315c000c63bb7311e69fcab18ad666916f1f25'
s=importlib.util.spec_from_file_location('probe',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
rows=[]
for grid in [512,1024]:
    acc=np.zeros((2,3))
    for q in range(grid):
        theta=2*np.pi*(q+.5)/grid;t=np.zeros(8);t[-1]=theta
        words,H,H4,jumps,G=m.target_matrices('ring8',t)
        states=np.column_stack([m.first_output('ring8',t,words,coh)[0] for coh in [False,True]])
        result=expm(-.7j*(320*H+1.3*H4-.35j*G))@states
        acc+=np.sum(abs(result)**2,axis=0)[:,None]*np.array([1,1+np.cos(theta),1-np.cos(theta)])[None,:]/grid
    rows.append({'grid':grid,'survivals':acc.tolist()})
difference=float(np.max(abs(np.array(rows[0]['survivals'])-np.array(rows[1]['survivals']))))
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'eta':320,'t':.7,'delta':1.3,'kappa':.7,
     'instrument_order':['resolved','coherent'],'field_order':['integer_flux_0','plus_adjacent_flux','minus_adjacent_flux'],
     'rows':rows,'max_grid_difference':difference,'declared_resolution_tolerance':1e-8,
     'scope':'Numerical quadrature corroboration; analytic phase integration is proved separately.'}
p=D/'QUADRATURE_REFINEMENT_RESULTS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
assert difference<1e-8
