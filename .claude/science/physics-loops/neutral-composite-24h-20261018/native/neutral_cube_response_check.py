import json,numpy as np,time
from scipy.sparse.linalg import eigsh
from neutral_cube_model import sector,op
D=sector(3);H=op(sum(D['H'],[]),D['dim']);E,vec=eigsh(H,k=1,which='SA',tol=1e-12,ncv=24,v0=np.random.default_rng(18).normal(size=D['dim']));g=vec[:,0];E0=E[0]
rows=[]
for name,terms in [('cubic_plaquette',D['S']),('nematic',[(x,z,c*(1 if a==2 else -.5)) for a,gg in enumerate(D['H']) for x,z,c in gg])]:
 C=op(terms,D['dim']);src=C@g;src-=g*(g@src);norm=np.linalg.norm(src);q=src/norm;prev=np.zeros_like(q);bprev=0.;aa=[];bb=[]
 for j in range(120):
  v=H@q-E0*q-bprev*prev;alpha=q@v;v-=alpha*q;v-=g*(g@v);beta=np.linalg.norm(v);aa.append(alpha)
  if j<119:bb.append(beta)
  prev,q=q,v/beta;bprev=beta
 T=np.diag(aa)+np.diag(bb,1)+np.diag(bb,-1);es,U=np.linalg.eigh(T);weights=norm**2*U[0]**2
 selected=np.argsort(weights)[-5:][::-1];vectors=np.zeros((D['dim'],len(selected)));q=src/norm;prev=np.zeros_like(q);bprev=0.
 for j in range(120):
  vectors+=q[:,None]*U[j,selected][None,:]
  if j==119:break
  v=H@q-E0*q-bprev*prev-aa[j]*q;v-=g*(g@v);prev,q=q,v/bb[j];bprev=bb[j]
 result=[]
 for i,k in enumerate(selected):
  v=vectors[:,i];v/=np.linalg.norm(v);energy=v@(H@v)-E0;res=np.linalg.norm(H@v-(E0+energy)*v);weight=(src@v)**2
  result.append(dict(gap=float(energy),residual=float(res),weight=float(weight),quadrature_energy=float(es[k]),accepted=bool(res<1e-8)))
 rows.append(dict(source=name,variance=norm**2,peaks=result));print(rows[-1],flush=True)
open('/private/tmp/neutral_cube_response_check.json','w').write(json.dumps(dict(ground=E0,ground_residual=float(np.linalg.norm(H@g-E0*g)),rows=rows,scope='Finite27physicalqubit cube; direct eigenvector residual checks, no thermodynamic limit'),indent=2)+'\n')
