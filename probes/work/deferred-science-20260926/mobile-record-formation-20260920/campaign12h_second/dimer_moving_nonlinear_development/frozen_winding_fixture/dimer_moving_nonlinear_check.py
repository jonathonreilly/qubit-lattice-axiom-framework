#!/usr/bin/env python3
"""Author controls of the moving-geometry entropy extension, not a volume-limit simulation."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
import datetime,hashlib,json,math
import numpy as np
ROOT=Path(__file__).resolve().parent

def geometry_entropy():
 labels=np.array(list(product(range(14),repeat=2)),dtype=int);D=len(labels)
 swap=labels[:,1]*14+labels[:,0];rho=np.array([.9,.1]);rate=1/3
 weights=np.array([1+(labels[:,0]+3*labels[:,1])**2%29,2+(5*labels[:,0]+labels[:,1])**2%31],float)
 cond=weights/weights.sum(axis=1)[:,None];mu=rho[:,None]*cond
 def generator(x):return rate*(x[::-1]+x[::-1][:,swap]-2*x)
 def entropy(x):
  marginal=x.sum(axis=1);return float(np.sum(x*np.log(x/(marginal[:,None]/D))))
 dm=generator(mu);dr=dm.sum(axis=1)
 ref=np.repeat(rho[:,None]/D,D,axis=1);expected=np.repeat(dr[:,None]/D,D,axis=1)
 assert np.max(abs(generator(ref)-expected))<2e-17
 direct=float(np.sum(dm*np.log(mu/(rho[:,None]/D))));assert direct<0
 joint=float(np.sum(dm*np.log(mu*2*D)));marginal=float(np.sum(dr*np.log(rho*2)))
 assert abs(direct-(joint-marginal))<2e-15 and abs(marginal)>1e-3
 h=1e-3;after=mu+h*dm;assert np.min(after)>0 and entropy(after)<entropy(mu)
 # The same Euler Markov channel exactly maps rho*pi to rho_new*pi.
 assert np.max(abs((ref+h*generator(ref))-(rho+h*dr)[:,None]/D))<2e-17
 # Color-dependent geometry rates break that reference evolution.
 dep_rate=rate*(1+(labels[:,0]==0)+(labels[:,1]==0))
 dep_dm=dep_rate[None,:]*(ref[::-1]+ref[::-1][:,swap]-2*ref)
 dep_dr=dep_dm.sum(axis=1);res=float(np.max(abs(dep_dm-dep_dr[:,None]/D)))
 dependent_after=ref+h*dep_dm;assert res>1e-5 and entropy(dependent_after)>1e-9
 # Full fourteen-color canonical mean of a pair difference is exactly zero.
 canonical=[]
 for a,b in [(0,0),(0,7),(3,12)]:
  states=sorted(set([(a,b),(b,a)]));sums=[sum(int(x==c)-int(y==c) for x,y in states) for c in range(14)]
  assert sums==[0]*14;canonical.append({'colors':[a,b],'arrangements':len(states),'exact_difference_sum':sums})
 return dict(states=2*D,geometry_marginal=rho.tolist(),rate=rate,conditional_entropy_derivative=direct,
  joint_uniform_entropy_derivative=joint,geometry_uniform_entropy_derivative=marginal,
  before=entropy(mu),after_Euler_channel=entropy(after),reference_evolution_error=float(np.max(abs(generator(ref)-expected))),
  color_dependent_countercontrol=dict(reference_derivative_residual=res,conditional_entropy_after=entropy(dependent_after)),canonical=canonical)

def matching(N,seed,attempts):
 coords=np.array(list(product(range(N),repeat=3)),dtype=int);V=N**3
 def index(x):return (x[...,0]*N+x[...,1])*N+x[...,2]
 directions=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
 nn=np.stack([index((coords+d)%N) for d in directions],axis=1)
 black=np.flatnonzero(coords.sum(axis=1)%2==0);ix=np.full(V,-1,dtype=int);ix[black]=np.arange(len(black))
 partner=np.empty(V,dtype=int);partner[black]=nn[black,0];partner[partner[black]]=black
 rng=np.random.default_rng(seed);flips=0
 for _ in range(attempts):
  x=int(rng.integers(V));i,j=rng.choice(3,size=2,replace=False);a=nn[x,2*i];b=nn[a,2*j];c=nn[x,2*j]
  if partner[x]==a and partner[b]==c:edges=[(x,c),(a,b)]
  elif partner[x]==c and partner[a]==b:edges=[(x,a),(c,b)]
  else:continue
  for u,v in edges:partner[u]=v;partner[v]=u
  flips+=1
 assert np.array_equal(partner[partner],np.arange(V)) and np.all(ix[partner[black]]<0)
 owner=np.where(ix>=0,np.arange(V),partner);q=ix[owner[nn[black]]]
 for d in range(6):assert np.array_equal(np.sort(q[:,d]),np.arange(len(black)))
 displacement=(coords[partner[black]]-coords[black]+N//2)%N-N//2
 assert np.all(np.sum(abs(displacement),axis=1)==1)
 a=directions[None,:,:]-displacement[q]
 # Physical positive-coordinate edge ID is independent of the matching.
 edgeid=np.empty((V,3),dtype=int)
 for axis in range(3):
  white=nn[:,2*axis];isblack=ix>=0
  edgeid[:,axis]=np.where(isblack,ix,ix[white])*6+np.where(isblack,2*axis,2*axis+1)
 return coords,nn,black,ix,partner,owner,q,a,directions,edgeid,flips

def owner_blocks():
 rows=[];nonzero=False
 for N,L,seed,attempts in [(12,4,11,0),(12,4,37,12**3*8),(16,6,53,16**3*8)]:
  coords,nn,black,ix,partner,owner,q,a,delta,edgeid,flips=matching(N,seed,attempts);K=len(black);V=N**3
  offsets=np.array(list(product(range(L),repeat=3)),dtype=int);cover=np.zeros(K,dtype=int);edgecover=np.zeros(6*K,dtype=int)
  inside=[np.flatnonzero(offsets[:,j]<L-1) for j in range(3)]
  neighbor=[inside[j]+[L*L,L,1][j] for j in range(3)]
  counts=[];selected=[];origins={0,V//7,V//3,V-1}
  for z in range(V):
   xyz=(coords[z]+offsets)%N;physical=(xyz[:,0]*N+xyz[:,1])*N+xyz[:,2];anchors=np.unique(owner[physical]);B=ix[anchors];m=len(B)
   cover[B]+=1;counts.append(m);assert L**3//2<=m<=L**3
   for j in range(3):np.add.at(edgecover,edgeid[physical[inside[j]],j],1)
   if z not in origins:continue
   graph={int(u):set() for u in anchors}
   for j in range(3):
    left=owner[physical[inside[j]]];right=owner[physical[neighbor[j]]]
    for u,v in zip(left,right):
     if u!=v:graph[int(u)].add(int(v));graph[int(v)].add(int(u))
   seen={int(anchors[0])};todo=list(seen)
   while todo:
    for v in graph[todo.pop()]:
     if v not in seen:seen.add(v);todo.append(v)
   assert len(seen)==m
   # Every contracted physical edge appears among actual q routes.
   for u,neighbors in graph.items():assert all(ix[v] in q[ix[u]] or ix[u] in q[ix[v]] for v in neighbors)
   T2=np.einsum('udj,dk->jk',a[B],delta);res=T2-2*m*np.eye(3,dtype=int)
   maxres=int(np.max(abs(res)));nonzero|=maxres>0
   boundaries=[]
   Bset=set(B.tolist())
   for d in range(6):
    image=set(q[B,d].tolist());difference=len(Bset.symmetric_difference(image));assert difference<=12*L**2
    boundaries.append(difference)
   assert maxres<=36*L**2
   selected.append(dict(origin=z,block_count=m,connected=True,twice_tensor_residual=res.tolist(),six_image_boundary_counts=boundaries))
  assert np.all(cover==L**3+L**2) and np.all(edgecover==L**3-L**2)
  rows.append(dict(N=N,L=L,accepted_geometry_flips=flips,all_origins=V,minimum_block_count=min(counts),maximum_block_count=max(counts),
   exact_anchor_coverage=int(cover[0]),exact_physical_edge_coverage=int(edgecover[0]),selected=selected))
 assert nonzero,'rough matching must exhibit a nonzero finite-block tensor boundary term'
 return rows

def constants():
 alpha=F(1,1792);rows=[]
 for L in [16,18,32,64,128]:
  chi=32*L**3;mmin=F(L**3,2);assert chi>=(2*L+3)**3 and 2*alpha*chi==mmin/14
  assert F(L**3,L**3+L**2)<=1
  rows.append(dict(L=L,overlap_colors=chi,overlap_degree_plus_one_bound=(2*L+3)**3,minimum_count=str(mmin),twice_alpha_chi=str(2*alpha*chi),maximum_omega=str(F(L**3,L**3+L**2))))
 return dict(alpha=str(alpha),rows=rows,scope='Constants apply in the theorem range L>=16. Small torus geometry controls test the local identities under N>2L+3, not the full theorem hypothesis N>10L.')

def main():
 result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sources=[],geometry_entropy=geometry_entropy(),owner_blocks=owner_blocks(),exponential_constants=constants(),
  scope='New finite checks of conditional entropy, actual matching ownership, contracted connectivity, coverage and boundary tensor, and weighted exponential normalization. No trajectory hydrodynamic simulation or all-volume proof by enumeration.')
 for name in ['DIMER_MOVING_GEOMETRY_SMOOTH_NONLINEAR_EULER.md','DIMER_SMOOTH_NONLINEAR_EULER_LIMIT.md','DIMER_NONLINEAR_COLOR_FLUX_AND_OPTICAL_DIAGNOSTICS.md','DIMER_ROUTED_RECORD_TRANSPORT.md','DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.md',Path(__file__).name]:
  p=ROOT/name;result['sources'].append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 out=ROOT/'dimer_moving_nonlinear_checks';out.mkdir(exist_ok=True);(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print('three_moving_nonlinear_control_groups_complete',flush=True)
if __name__=='__main__':main()

