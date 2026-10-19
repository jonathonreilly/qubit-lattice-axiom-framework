import json,numpy as np
from scipy.sparse.linalg import eigsh
from collections import defaultdict
from neutral_cube_model import sector,op,mult

def comm(a,b):
 d=defaultdict(float)
 for x in a:
  for y in b:
   u=mult(x,y);v=mult(y,x);d[u[:2]]+=u[2];d[v[:2]]-=v[2]
 return [(x,z,c) for (x,z),c in d.items() if c]
D=sector(3);ht=sum(D['H'],[]);qt=[]
for a in D['H']:qt+=comm(a,comm(ht,a))
qdict=defaultdict(float)
for x,z,c in qt:qdict[x,z]+=c
qt=[(x,z,c) for (x,z),c in qdict.items() if c]
H=op(ht,D['dim']);Q=op(qt,D['dim']);E,V=eigsh(H,k=1,which='SA',tol=1e-12,ncv=24,v0=np.random.default_rng(42).normal(size=D['dim']));g=V[:,0];E0=E[0]
# Verify double commutator against sequential matrix actions.
explicit=np.zeros_like(g)
for a in D['H']:
 A=op(a,D['dim']);explicit+=2*A@(H@(A@g))-A@(A@(H@g))-H@(A@(A@g))
error=np.linalg.norm(Q@g-explicit)
src=Q@g;mean=g@src;src-=g*mean;norm=np.linalg.norm(src);q=src/norm;prev=np.zeros_like(q);bp=0;aa=[];bb=[]
for j in range(140):
 v=H@q-E0*q-bp*prev;alpha=q@v;v-=alpha*q;v-=g*(g@v);beta=np.linalg.norm(v);aa.append(alpha)
 if j<139:bb.append(beta)
 prev,q=q,v/beta;bp=beta
T=np.diag(aa)+np.diag(bb,1)+np.diag(bb,-1);es,U=np.linalg.eigh(T);weights=norm**2*U[0]**2;selected=np.argsort(weights)[-6:][::-1];vectors=np.zeros((D['dim'],len(selected)));q=src/norm;prev=np.zeros_like(q);bp=0
for j in range(140):
 vectors+=q[:,None]*U[j,selected][None,:]
 if j==139:break
 v=H@q-E0*q-bp*prev-aa[j]*q;v-=g*(g@v);prev,q=q,v/bb[j];bp=bb[j]
s=op(D['S'],D['dim'])@g;s-=g*(g@s);peaks=[]
for i,k in enumerate(selected):
 v=vectors[:,i];v/=np.linalg.norm(v);en=v@(H@v);res=np.linalg.norm(H@v-en*v)
 peaks.append(dict(gap=float(en-E0),residual=float(res),weight=float((src@v)**2),plaquette_weight=float((s@v)**2),accepted=bool(res<1e-8)))
out=dict(ground=float(E0),ground_residual=float(np.linalg.norm(H@g-E0*g)),operator='Q=sum_a [H_a,[H,H_a]]',terms=len(qt),sequential_error=float(error),mean=float(mean),variance=float(norm**2),peaks=peaks,scope='Chosen native-derived diagnostic, no new Hamiltonian term; finite27sites')
print(out,flush=True);open('/private/tmp/neutral_cube_native_scalar.json','w').write(json.dumps(out,indent=2)+'\n')
