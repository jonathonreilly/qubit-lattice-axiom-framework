"""Variational collective neutral sources, without adding Hamiltonian terms."""
from pathlib import Path
import json,time
import numpy as np
from scipy.linalg import eigh
from compass_sector_basis import basis
from compass_sector_solve import apply
from neutral_extra_sector import reducer
P=Path(__file__).resolve().parent;D=basis((3,3,3));st=[]
for y in [0,1]:
 m=sum(1<<i for i,x in enumerate(D['sites']) if x[1] in [y,y+1]);st.append(D['reduce_term'](m,m,-1))
R=reducer(22,st,(1,1));terms=np.array([R['reduce'](t) for t in D['terms']],np.int64);H=lambda v:apply(v,*terms.T.copy())
s=np.load(P/'stationary_extra_vectors.npz');g=s['ground'];e0=float(s['energy']);idx={x:i for i,x in enumerate(D['sites'])}
ops=[];labels=[];classes=[]
for x,i in idx.items():
 ct=[]
 for a in range(3):
  if x[a]!=1:continue
  l=list(x);r=list(x);l[a]-=1;r[a]+=1;m=(1<<idx[tuple(l)])|(1<<idx[tuple(r)])
  ct.append(R['reduce'](D['reduce_term'](m if a!=2 else 0,m if a!=0 else 0,-1 if a==1 else 1)))
 if ct:ops.append(ct);labels.append(dict(kind='C',site=x));classes.append(('C',sum((v-1)**2 for v in x)))
for t,(i,j,a) in zip(terms,D['bonds']):
 midpoint=(np.array(D['sites'][i])+D['sites'][j])/2-1
 ops.append([t]);labels.append(dict(kind='bond',ends=[D['sites'][i],D['sites'][j]],axis=a));classes.append(('bond',float(midpoint@midpoint)))
V=np.empty((len(ops),len(g)));W=np.empty_like(V)
for i,ts in enumerate(ops):
 v=apply(g,*np.array(ts,np.int64).T.copy());v-=g*(g@v);V[i]=v;W[i]=H(v)-e0*v
S=V@V.T;K=V@W.T;M=W@W.T
sets={'all_neutral_local':np.eye(len(ops)),'C_only':np.eye(len(ops))[:sum(l['kind']=='C' for l in labels)]}
unique=list(dict.fromkeys(classes));A=np.array([[int(cl==k) for cl in classes] for k in unique],float)
sets['cubic_scalar_orbit_sums']=A
out={}
for name,A in sets.items():
 ss=A@S@A.T;kk=A@K@A.T;evals,U=eigh(ss);keep=evals>max(evals)*1e-10
 T=U[:,keep]/np.sqrt(evals[keep]);ek,uk=eigh(T.T@kk@T);coeff=A.T@T@uk
 rows=[]
 for k in range(min(5,len(ek))):
  c=coeff[:,k];v=c@V;hv=c@W;norm=float(np.linalg.norm(v));v/=norm;hv/=norm
  energy=float(v@hv);res=float(np.linalg.norm(hv-energy*v));assert abs(energy-ek[k])<1e-8
  rows.append(dict(energy=energy,residual=res,coefficients=c.tolist(),overlaps_with_refined_modes=[float((v@m)**2/(m@m)) for m in s['vectors']],moment_variance=float(c@M@c-energy**2)))
 projection=[]
 for m in s['vectors']:
  m=m/np.linalg.norm(m);b=A@(V@m);pc=T.T@b;weight=float(pc@pc);c=A.T@T@pc/np.sqrt(weight)
  vv=c@V;hh=c@W;energy=float(vv@hh)
  assert abs((vv@m)**2-weight)<1e-9
  projection.append(dict(maximum_overlap_squared_in_kept_space=weight,energy=energy,residual=float(np.linalg.norm(hh-energy*vv)),coefficients=c.tolist()))
 out[name]=dict(source_count=len(A),rank=int(sum(keep)),min_metric_kept=float(min(evals[keep])),rows=rows,targeted_projection=projection)
result=dict(labels=labels,scalar_classes=unique,sets=out,scope='Finite stationary27site variational excitation/source optimization; coefficients are developed on this same model. No new H interaction, bulk mode, empirical fit or independent observation.')
(P/'neutral_collective_basis.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:dict(rank=v['rank'],modes=[(r['energy'],r['residual']) for r in v['rows']]) for k,v in out.items()})
