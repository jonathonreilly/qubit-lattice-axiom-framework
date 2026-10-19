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

ss=np.load(P/'stationary_extra_vectors.npz');allct=[]
for x,i in idx.items():
 for a in range(3):
  if x[a]!=1:continue
  l=list(x);rr=list(x);l[a]-=1;rr[a]+=1;mask=(1<<idx[tuple(l)])|(1<<idx[tuple(rr)])
  allct.append(R['reduce'](D['reduce_term'](mask if a!=2 else 0,mask if a!=0 else 0,-1 if a==1 else 1)))
allct=np.array(allct,np.int64);Ctotal=lambda v:apply(v,*allct.T.copy());rows=[]
for label,op in [('central_C',C),('sum_existing_C',Ctotal)]:
 c0=float(g@op(g));modes=[]
 for m in ss['vectors']:
  m=m/np.linalg.norm(m);gap=float(m@(H(m)-e0*m));cm=float(m@op(m));dc=cm-c0
  modes.append(dict(gap=gap,C_mean=cm,delta_C=dc,conditional_branch_gap_derivative_for_H_minus_lambda_C=-dc,conditional_fractional_gap_derivative=-dc/gap,uniform_H_rescale_derivative=gap))
 rows.append(dict(operator=label,initial_mean=c0,modes=modes))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(rows=rows,scope='Expectation diagnostic; Feynman-Hellmann interpretation requires a resolved branch or perturbation diagonalized within degeneracy. Lambda is only a differentiation probe, not an adopted interaction. Neither operator is identified as a physical scalar background and these are not physical matter species.'),indent=2)+'\n');print(rows)
