import numpy as np,time,json,os
from pathlib import Path
from scipy.sparse.linalg import eigsh,LinearOperator
from neutral_translation_model import translation_tables,orbits,orbit_op
from neutral_rect_model import sector
p=Path('/private/tmp/neutral_rect_data');p.mkdir(exist_ok=True);start=time.time();D=sector((3,3,4));T,R,C=translation_tables(D)
print('tables ready',D['n'],time.time()-start,flush=True)
data=orbits(D['dim'],T,R,C);labels,signs,reps,sizes,excluded=data
print('orbits',len(reps),'excluded',excluded,'seconds',time.time()-start,flush=True)
for name,array in zip(['labels','signs','reps','sizes'],data[:4]):np.save(p/(name+'.npy'),array)
H0=orbit_op(sum(D['H'],[]),data);count=[0]
def mv(v):
 count[0]+=1
 if count[0]%25==0:print('matvec',count[0],'seconds',time.time()-start,flush=True)
 return H0@v
H=LinearOperator(H0.shape,matvec=mv,dtype=float)
rng=np.random.default_rng(987);a=rng.normal(size=len(reps));b=rng.normal(size=len(reps));a/=np.linalg.norm(a);b/=np.linalg.norm(b);herm=abs(a@(H@b)-(H@a)@b);print('hermiticity',herm,flush=True);assert herm<1e-10
E,V=eigsh(H,k=2,which='SA',tol=1e-10,ncv=24,maxiter=1000,v0=a)
res=[float(np.linalg.norm(H@V[:,i]-E[i]*V[:,i])) for i in range(2)]
np.save(p/'ground.npy',V[:,0]);np.save(p/'first.npy',V[:,1]);out=dict(dims=[3,3,4],physical_qubits=36,plane_sector_dimension=D['dim'],zero_momentum_dimension=len(reps),excluded=int(excluded),energies=E.tolist(),residuals=res,hermiticity_error=float(herm),seconds=time.time()-start,matvecs=count[0],scope='All-positive commuting-plane sector, momentumzero only; numerical eigenpairs, no global ground proof')
print(out,flush=True);(p/'ground.json').write_text(json.dumps(out,indent=2)+'\n')
