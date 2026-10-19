import json,time,numpy as np
from scipy.sparse.linalg import eigsh
from neutral_cube_model import sector,op
D=sector(3);rows=[]
for lam in [.2,.5,1.]:
 start=time.time();H=op([(x,z,c*(lam if a<2 else 1)) for a,g in enumerate(D['H']) for x,z,c in g],D['dim']);S=op(D['S'],D['dim'])
 rng=np.random.default_rng(1810);vals,vecs=eigsh(H,k=2,which='SA',tol=1e-10,maxiter=2000,ncv=24,v0=rng.normal(size=D['dim']))
 g=vecs[:,0];res=np.linalg.norm(H@g-vals[0]*g);src=S@g;mean=g@src;src-=mean*g;norm=np.linalg.norm(src);q=src/norm;prev=np.zeros_like(q);bprev=0.;aa=[];bb=[]
 for j in range(100):
  v=H@q-vals[0]*q-bprev*prev;alpha=q@v;v-=alpha*q;v-=g*(g@v);beta=np.linalg.norm(v);aa.append(float(alpha))
  if j<99:bb.append(float(beta))
  if beta<1e-12:break
  prev,q=q,v/beta;bprev=beta
 T=np.diag(aa)+np.diag(bb[:len(aa)-1],1)+np.diag(bb[:len(aa)-1],-1);ev,U=np.linalg.eigh(T);weights=norm**2*U[0]**2
 peaks=sorted([(float(w),float(e)) for w,e in zip(weights,ev)],reverse=True)[:8]
 row=dict(lam=lam,ground=float(vals[0]),first_gap=float(vals[1]-vals[0]),ground_residual=float(res),source_mean=float(mean),source_variance=float(norm**2),quadrature_peaks=peaks,lanczos_steps=len(aa),seconds=time.time()-start,scope='Selected commuting-plane sector; quadrature nodes not certified eigenmodes; no global ground or thermodynamic inference')
 rows.append(row);print(json.dumps(row),flush=True);open('/private/tmp/neutral_cube_probe.json','w').write(json.dumps(rows,indent=2)+'\n')
