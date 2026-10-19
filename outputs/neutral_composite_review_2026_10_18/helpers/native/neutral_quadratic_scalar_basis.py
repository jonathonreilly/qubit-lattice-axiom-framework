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
import itertools
lookup={tuple(sorted((D['sites'][i],D['sites'][j]))):k for k,(i,j,a) in enumerate(D['bonds'])}
perms=[]
for p in itertools.permutations(range(3)):
 for signs in itertools.product([-1,1],repeat=3):
  def tr(x):return tuple(1+signs[a]*(x[p[a]]-1) for a in range(3))
  perms.append([lookup[tuple(sorted((tr(D['sites'][i]),tr(D['sites'][j]))))] for i,j,a in D['bonds']])
groups={}
for i in range(54):
 for j in range(i+1,54):
  f,z,c=D['terms'][i];bf,w,d=D['terms'][j]
  if ((z&bf).bit_count()+(w&f).bit_count())%2:continue
  key=min(tuple(sorted((pm[i],pm[j]))) for pm in perms)
  groups.setdefault(key,[]).append((i,j))
ops=[];labels=[]
for radius in [.25,1.25,2.25]:
 ts=[]
 for t,(i,j,a) in zip(terms,D['bonds']):
  midpoint=(np.array(D['sites'][i])+D['sites'][j])/2-1
  if abs(midpoint@midpoint-radius)<1e-10:ts.append(tuple(t))
 ops.append(ts);labels.append(dict(kind='linear',radius=radius))
from neutral_extra_sector import mul
for key,pairs in groups.items():
 ts=[mul(tuple(terms[i]),tuple(terms[j])) for i,j in pairs]
 ops.append(ts);labels.append(dict(kind='quadratic',representative=key,count=len(pairs)))
V=np.empty((len(ops),len(g)));W=np.empty_like(V)
for i,ts in enumerate(ops):
 v=apply(g,*np.array(ts,np.int64).T.copy())/len(ts);v-=g*(g@v);V[i]=v;W[i]=H(v)-e0*v
S=V@V.T;K=V@W.T;out={}
for name,count in [('linear',3),('linear_and_quadratic',len(ops))]:
 ss=S[:count,:count];kk=K[:count,:count];ev,U=eigh(ss);keep=ev>max(ev)*1e-10;T=U[:,keep]/np.sqrt(ev[keep]);en,u=eigh(T.T@kk@T);coeff=T@u;rows=[]
 for k in range(min(5,len(en))):
  c=coeff[:,k];v=c@V[:count];hv=c@W[:count];norm=np.linalg.norm(v);v/=norm;hv/=norm;ray=float(v@hv)
  rows.append(dict(energy=ray,residual=float(np.linalg.norm(hv-ray*v)),overlaps_with_refined_modes=[float((v@m)**2/(m@m)) for m in s['vectors']],coefficients=c.tolist()))
 projection=[]
 for m in s['vectors']:
  m=m/np.linalg.norm(m);b=V[:count]@m;pc=T.T@b;weight=float(pc@pc);c=T@pc/np.sqrt(weight)
  vv=c@V[:count];hh=c@W[:count];energy=float(vv@hh)
  assert abs((vv@m)**2-weight)<1e-9
  projection.append(dict(maximum_overlap_squared_in_kept_space=weight,energy=energy,residual=float(np.linalg.norm(hh-energy*vv)),coefficients=c.tolist()))
 out[name]=dict(rank=int(sum(keep)),rows=rows,targeted_projection=projection)
result=dict(labels=labels,sets=out,scope='Finite27site scalar operator orbit sums through quadratic native bonds; selected coefficients are model development, not physical source identification or bulk particle.')
(P/'neutral_quadratic_scalar_basis.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:dict(rank=v['rank'],modes=[(r['energy'],r['residual'],r['overlaps_with_refined_modes'][0]) for r in v['rows']]) for k,v in out.items()})
