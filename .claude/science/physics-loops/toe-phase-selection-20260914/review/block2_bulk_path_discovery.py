from pathlib import Path
import importlib.util,json
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy import sparse
pack=Path('/Users/jonreilly/Documents/Codex/toe-phase-selection-20260914/.claude/science/physics-loops/toe-phase-selection-20260914')
spec=importlib.util.spec_from_file_location('cells',pack/'block1_projection_sector_check.py');cells=importlib.util.module_from_spec(spec);spec.loader.exec_module(cells)
levels,_,F,D=cells.box_complex((5,5,5));old=json.loads((pack/'BLOCK2_CUBIC_PATH_WITNESS.json').read_text())
cols=[levels[1].index((tuple(axes),tuple(x+1 for x in anchor))) for axes,anchor in old['original_edges']]
oldminor=json.loads((pack/'BLOCK2_CUBIC_BOUNDARY_MINOR_PROBE.json').read_text())['found']
rows=[levels[2].index((tuple(axes),tuple(x+1 for x in anchor))) for axes,anchor in oldminor['faces']]
prefix=np.column_stack([np.zeros(F.shape[0],dtype=int),np.cumsum(F[:,cols],axis=1)])
low=-1-prefix.min(axis=1);high=1-prefix.max(axis=1);p,c=D.shape[1],D.shape[0]
boundary=np.flatnonzero(np.count_nonzero(D,axis=0)==1);low[boundary]=0;high[boundary]=0
q=np.zeros(c,dtype=int);q[levels[3].index(((0,1,2),(1,1,1)))]=1;q[levels[3].index(((0,1,2),(0,1,1)))]=-1
A=sparse.hstack([sparse.csr_matrix(D),sparse.csr_matrix((c,p))]).tocsr();I=sparse.eye(p);B=sparse.vstack([sparse.hstack([I,-I]),sparse.hstack([-I,-I])]).tocsr()
r=milp(np.r_[np.zeros(p),np.ones(p)],integrality=np.r_[np.ones(p),np.zeros(p)],bounds=Bounds(np.r_[low,np.zeros(p)],np.r_[high,np.ones(p)]),constraints=[LinearConstraint(A,3*q,3*q),LinearConstraint(B,-np.inf,0)],options={'time_limit':30})
print(r.message)
if r.x is not None:
 x=np.rint(r.x[:p]).astype(int);assert np.array_equal(D@x,3*q) and np.all(abs(x[:,None]+prefix)<=1) and np.all(x[boundary]==0)
 assert all(np.count_nonzero(F[:,l])==4 for l in cols)
 out={'box':[5,5,5],'columns':cols,'rows':rows,'original_edges':[levels[1][i] for i in cols],'selected_faces':[levels[2][i] for i in rows],'nonzero_initial_flux':[(levels[2][i],int(v)) for i,v in enumerate(x) if v],'nonzero_initial_charge':[(levels[3][i],int(v)) for i,v in enumerate(q) if v],'initial_flux':x.tolist(),'initial_charge':q.tolist(),'minor':F[np.ix_(rows,cols)].tolist(),'allocation_rhs':(F[:,cols].sum(axis=1)[rows]//2).tolist(),'all_selected_stars_bulk':True,'boundary_flux_zero':True,'optimal_sparsification':bool(r.success)}
 (pack/'BLOCK2_CUBIC_BULK_PATH_WITNESS.json').write_text(json.dumps(out,indent=2)+'\n')
 print('nonzero flux',len(out['nonzero_initial_flux']));print('charges',out['nonzero_initial_charge']);print('flux',out['nonzero_initial_flux'])
