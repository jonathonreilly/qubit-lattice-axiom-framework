from pathlib import Path
import importlib.util,json,numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('core',HERE/'check_block10.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
def gauge_hess(L=3,seed=73):
 rng=np.random.default_rng(seed);theta=rng.normal(size=(L,L,L));size=2*L**3
 mats=[np.zeros((size,size),complex) for _ in range(3)];test=np.zeros((size,size),complex)
 hop=[-c.SIG[2]/2-1j*c.SIG[i]/2 for i in range(2)]+[-c.SIG[2]/2]
 def sl(x):
  idx=np.ravel_multi_index(tuple(x),(L,L,L));return slice(2*idx,2*idx+2)
 for idx in np.ndindex(L,L,L):
  p=np.array(idx);sp=sl(p);mats[0][sp,sp]+=(2+.7)*c.SIG[2];test[sp,sp]+=(2+.7)*c.SIG[2]
  for axis in range(3):
   q=(p+np.eye(3,dtype=int)[axis])%L;sq=sl(q);delta=theta[tuple(q)]-theta[idx]
   for j in range(3):
    val=(1j*delta)**j*hop[axis];mats[j][sp,sq]+=val;mats[j][sq,sp]+=val.conj().T
   val=np.exp(.37j*delta)*hop[axis];test[sp,sq]+=val;test[sq,sp]+=val.conj().T
 H,H1,H2=mats;energy,U=np.linalg.eigh(H);occ=energy<0;gap=min(abs(energy));pert=U.conj().T@H1@U;contact=np.trace((U[:,occ].conj().T@H2@U[:,occ])).real
 bubble=2*np.sum(abs(pert[np.ix_(occ,~occ)])**2/(energy[occ,None]-energy[None,~occ])).real
 return dict(seed=seed,gap=gap,contact=contact,bubble=bubble,sum=contact+bubble,spectrum_error=float(np.max(abs(np.linalg.eigvalsh(test)-energy))),matrix_hermiticity=max(float(np.max(abs(A-A.conj().T))) for A in mats))
if __name__=='__main__':
 rows=[gauge_hess(seed=seed) for seed in [73,91,127]]
 (HERE/'BLOCK10_PEI ERLS_EXPLORATION.json'.replace(' ','')).write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
