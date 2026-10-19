"""More resolved neutral spectral benchmark using existing conserved Y-pair symmetries."""
import sys,json,time
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from compass_sector_basis import basis
from compass_sector_solve import apply
from neutral_extra_sector import reducer
P=Path(__file__).resolve().parent
D=basis((3,3,3));st=[]
for y in [0,1]:
 m=sum(1<<i for i,x in enumerate(D['sites']) if x[1] in [y,y+1]);st.append(D['reduce_term'](m,m,-1))
R=reducer(22,st,(1,1));terms=np.array([R['reduce'](t) for t in D['terms']],np.int64);H=lambda v:apply(v,*terms.T.copy())
s=np.load(P/'stationary_3x3x3_plus.npz');gfull=s['vectors'][:,0];e0=s['values'][0]
j=np.arange(R['dimension'],dtype=np.int64);r=np.zeros_like(j)
for k,f in enumerate(R['free']):r|=((j>>k)&1)<<f
from neutral_extra_sector import mul
groups=[(0,0,1),*st,mul(*st)];g=np.zeros(len(j))
for f,z,c in groups:
 parity=np.zeros_like(j)
 for b in range(22):
  if z>>b&1:parity^=(r>>b)&1
 g+=c*(1-2*parity)*gfull[r^f]/2
pn=float(g@g);g/=np.linalg.norm(g);del gfull,s,r,j
res=float(np.linalg.norm(H(g)-e0*g));assert abs(pn-1)<1e-10 and res<1e-9
idx={x:i for i,x in enumerate(D['sites'])};ct=[]
for a in range(3):
 l=[1,1,1];rr=[1,1,1];l[a]-=1;rr[a]+=1;m=(1<<idx[tuple(l)])|(1<<idx[tuple(rr)])
 ct.append(R['reduce'](D['reduce_term'](m if a!=2 else 0,m if a!=0 else 0,-1 if a==1 else 1)))
ct=np.array(ct,np.int64);C=lambda v:apply(v,*ct.T.copy());cg=C(g);v=cg-g*(g@cg);norm=np.linalg.norm(v)

m=np.load(P/'stationary_extra_vectors.npz')['vectors'][0];m/=np.linalg.norm(m);gap=float(m@(H(m)-e0*m));cm=C(m);cmmean=float(m@cm);v=cm-m*cmmean;norm=np.linalg.norm(v);z01=float((g@cm)**2)
prev=np.zeros_like(g);q=v/norm;beta=0;aa=[];bb=[];rows=[]
for k in range(256):
 w=H(q)-e0*q-beta*prev;alpha=float(q@w);w-=alpha*q;w-=m*(m@w);nxt=float(np.linalg.norm(w));aa.append(alpha)
 if k in [63,127,255]:
  T=np.diag(aa)+np.diag(bb,1)+np.diag(bb,-1);en,u=np.linalg.eigh(T);weights=norm**2*u[0]**2
  windows=[]
  for width in [.02,.05,.1,.2]:
   up=float(weights@np.exp(-((en-2*gap)/width)**2));down=float(weights@np.exp(-(en/width)**2))
   windows.append(dict(width=width,upper_weight=up,lower_weight=down,upper_over_2Z=up/(2*z01)))
  near=[dict(energy=float(a),weight=float(b)) for a,b in zip(en,weights) if abs(a-2*gap)<.5 and b>1e-9]
  rows.append(dict(steps=k+1,windows=windows,near_double_gap=near))
 if k<255:bb.append(nxt)
 prev,q=q,w/nxt;beta=nxt
chosen=np.flatnonzero((abs(en-2*gap)<.5)&(weights>1e-9));coeffs=u[:,chosen];vv=np.zeros((len(chosen),len(g)));prev=np.zeros_like(g);q=v/norm
for k in range(256):
 vv+=coeffs[k,:,None]*q[None,:]
 if k<255:
  w=H(q)-e0*q-(bb[k-1]*prev if k else 0)-aa[k]*q;w-=m*(m@w);prev,q=q,w/bb[k]
checked=[]
for vec,jj in zip(vv,chosen):
 vn=float(np.linalg.norm(vec));vec/=vn;hv=H(vec)-e0*vec;ray=float(vec@hv)
 checked.append(dict(energy=ray,delta_from_double_gap=ray-2*gap,residual=float(np.linalg.norm(hv-ray*vec)),weight=float((vec@v)**2),raw_norm=vn))
result=dict(gap=gap,ground_to_mode_weight=z01,excited_C_mean=cmmean,excited_connected_weight=float(norm**2),rows=rows,reconstructed_near_double_gap=checked,scope='Finite27site ladder diagnostic of chosen frequency-filtered C, no bulk scalar or interaction coefficient identification')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
