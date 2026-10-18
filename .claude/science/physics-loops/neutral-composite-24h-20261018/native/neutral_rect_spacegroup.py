import numpy as np,json,time
from pathlib import Path
from scipy.sparse.linalg import eigsh
from neutral_rect_model import sector
from neutral_spacegroup_model import translation_tables,orbits,orbit_op
p=Path('/private/tmp/neutral_rect_spacegroup_data');p.mkdir(exist_ok=True);old=Path('/private/tmp/neutral_rect_data');start=time.time();D=sector((3,3,4));T,R,C=translation_tables(D);print('group tables',len(T),time.time()-start,flush=True);data=orbits(D['dim'],T,R,C);labels,signs,reps,sizes,excluded=data;print('orbits',len(reps),'excluded',excluded,time.time()-start,flush=True)
for name,array in zip(['labels','signs','reps','sizes'],data[:4]):np.save(p/(name+'.npy'),array)
oreps=np.load(old/'reps.npy',mmap_mode='r');osizes=np.load(old/'sizes.npy',mmap_mode='r');og=np.load(old/'ground.npy');lab=labels[oreps];ok=lab>=0;factors=signs[oreps[ok]]*np.sqrt(osizes[ok]/sizes[lab[ok]]);g=np.bincount(lab[ok],weights=factors*og[ok],minlength=len(reps));embedded=np.zeros_like(og);embedded[ok]=factors*g[lab[ok]];projerror=np.linalg.norm(embedded-og);gn=np.linalg.norm(g);g/=gn;H=orbit_op(sum(D['H'],[]),data);E0=float(g@(H@g));res=float(np.linalg.norm(H@g-E0*g));print('projectedground',E0,res,projerror,gn,flush=True);assert projerror<1e-8 and res<1e-8
np.save(p/'ground.npy',g)
E,V=eigsh(H,k=20,which='SA',tol=1e-11,ncv=56,v0=np.random.default_rng(3).normal(size=len(reps)));np.save(p/'low_vectors.npy',V)
rows=[dict(energy=float(e),gap=float(e-E[0]),residual=float(np.linalg.norm(H@V[:,i]-e*V[:,i]))) for i,e in enumerate(E)]
out=dict(physical_qubits=36,dimension=len(reps),excluded=int(excluded),group_elements=len(T),projection_error=float(projerror),rows=rows,seconds=time.time()-start,scope='Exact translation+D4xy+zreflection invariant sector; no fullcubicirrep or globalground claim');print(out,flush=True);(p/'low.json').write_text(json.dumps(out,indent=2)+'\n')
