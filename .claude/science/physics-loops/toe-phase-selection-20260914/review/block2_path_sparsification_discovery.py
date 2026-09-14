from pathlib import Path
import importlib.util,json
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy import sparse
pack=Path('/Users/jonreilly/Documents/Codex/toe-phase-selection-20260914/.claude/science/physics-loops/toe-phase-selection-20260914')
spec=importlib.util.spec_from_file_location('cells',pack/'block1_projection_sector_check.py');cells=importlib.util.module_from_spec(spec);spec.loader.exec_module(cells)
levels,_,F,D=cells.box_complex((3,3,3));old=json.loads((pack/'BLOCK2_CUBIC_PATH_WITNESS.json').read_text());cols=old['columns'];rows=old['rows'];prefix=np.column_stack([np.zeros(F.shape[0],dtype=int),np.cumsum(F[:,cols],axis=1)])
low=-1-prefix.min(axis=1);high=1-prefix.max(axis=1);p,c=D.shape[1],D.shape[0];n=2*(p+c)
# Variables x,q,abs(x),abs(q); require a nonzero charge at the first cube.
A=np.zeros((c,n));A[:,:p]=D;A[:,p:p+c]=-3*np.eye(c)
B=np.zeros((2*(p+c),n))
for i in range(p+c):B[2*i,i]=1;B[2*i,p+c+i]=-1;B[2*i+1,i]=-1;B[2*i+1,p+c+i]=-1
lb=np.r_[low,-np.ones(c),np.zeros(p+c)];ub=np.r_[high,np.ones(c),np.ones(p+c)]
lb[p]=ub[p]=1
obj=np.r_[np.zeros(p+c),np.ones(p),100*np.ones(c)]
r=milp(obj,integrality=np.r_[np.ones(p+c),np.zeros(p+c)],bounds=Bounds(lb,ub),constraints=[LinearConstraint(sparse.csr_matrix(A),0,0),LinearConstraint(sparse.csr_matrix(B),-np.inf,0)],options={'time_limit':30})
print(r.message)
if r.x is not None:
 x=np.rint(r.x[:p]).astype(int);q=np.rint(r.x[p:p+c]).astype(int)
 assert np.array_equal(D@x,3*q) and np.all(abs(x[:,None]+prefix)<=1)
 old['initial_flux']=x.tolist();old['initial_charge']=q.tolist();old['sparsification']={'optimal':bool(r.success),'absolute_charge':int(sum(abs(q))),'nonzero_flux':int(sum(abs(x))),'forced_cube':0,'forced_charge':1}
 (pack/'BLOCK2_CUBIC_PATH_WITNESS.json').write_text(json.dumps(old,indent=2)+'\n')
 print(old['sparsification']);print('charges',[(i,int(v)) for i,v in enumerate(q) if v]);print('flux',[(i,int(v)) for i,v in enumerate(x) if v])
