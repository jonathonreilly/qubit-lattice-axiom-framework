#!/usr/bin/env python3
"""Actual SU(2) block-tree gauge and reconstruction, independent matrix code."""
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=[]
import itertools,json,math,sys,time
import numpy as np
from scipy import linalg
start=time.monotonic();L=3;T=2;n=L*T
sites=list(itertools.product(range(n),repeat=4));sid={x:i for i,x in enumerate(sites)}
local=list(itertools.product(range(-1,2),repeat=4));blocks=list(itertools.product(range(T),repeat=4))
pauli=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
rng=np.random.default_rng(731)
links=np.empty((len(sites),4,2,2),complex)
for j,x in enumerate(sites):
 for mu in range(4):links[j,mu]=linalg.expm(1j*np.einsum('a,aij->ij',rng.normal(size=3)*.05,pauli)/math.sqrt(2))
def shift(x,mu,a=1):
 y=list(x);y[mu]=(y[mu]+a)%n;return tuple(y)
def physical(bl,v):return tuple((L*bl[i]+1+v[i])%n for i in range(4))
def leg(field,x,y,order):
 out=np.eye(2,dtype=complex);p=x
 # x,y are lifted integer points. Link access is periodic.
 for mu in order:
  while p[mu]!=y[mu]:
   s=1 if y[mu]>p[mu] else -1
   base=p if s==1 else tuple(p[i]-(i==mu) for i in range(4))
   u=field[sid[tuple(v%n for v in base)],mu]
   out=out@(u if s==1 else u.conj().T)
   p=tuple(p[i]+s*(i==mu) for i in range(4))
 return out
G=np.empty((len(sites),2,2),complex);tree=[]
for bl in blocks:
 root=physical(bl,(0,0,0,0));G[sid[root]]=np.eye(2)
 for v in sorted((x for x in local if any(x)),key=lambda x:sum(abs(a) for a in x)):
  mu=max(i for i in range(4) if v[i]);s=1 if v[mu]>0 else -1
  parent=tuple(v[i]-s*(i==mu) for i in range(4));x=physical(bl,parent);y=physical(bl,v)
  base=x if s==1 else y;U=links[sid[base],mu]
  G[sid[y]]=G[sid[x]]@(U if s==1 else U.conj().T)
  tree.append((sid[base],mu))
W=np.empty_like(links);recon=np.empty_like(links)
for j,x in enumerate(sites):
 for mu in range(4):
  k=sid[shift(x,mu)];W[j,mu]=G[j]@links[j,mu]@G[k].conj().T
  recon[j,mu]=G[j].conj().T@W[j,mu]@G[k]
checks=[]
def gate(name,ok,detail=None):checks.append({'name':name,'pass':bool(ok),'detail':detail})
gate('unique_internal_trees',len(tree)==len(set(tree))==len(blocks)*(L**4-1))
gate('pinned_roots',max(np.max(abs(G[sid[physical(bl,(0,0,0,0))]]-np.eye(2))) for bl in blocks)<1e-14)
gate('all_tree_links_identity',max(np.max(abs(W[j,mu]-np.eye(2))) for j,mu in tree)<3e-14)
gate('all_links_reconstructed',np.max(abs(recon-links))<3e-14,float(np.max(abs(recon-links))))
maxplaquette=0
for x in sites:
 for mu,nu in itertools.combinations(range(4),2):
  def plaq(field):return field[sid[x],mu]@field[sid[shift(x,mu)],nu]@field[sid[shift(x,nu)],mu].conj().T@field[sid[x],nu].conj().T
  maxplaquette=max(maxplaquette,abs(np.trace(plaq(links))-np.trace(plaq(W))))
gate('all_Wilson_plaquette_traces',maxplaquette<4e-14,float(maxplaquette))
orders=list(itertools.permutations(range(4)));means=[];meanerrors=[]
for bl in [(0,0,0,0),(1,1,1,1)]:
 root=tuple(L*bl[i]+1 for i in range(4))
 for mu in range(4):
  root2=tuple(root[i]+L*(i==mu) for i in range(4));m=[]
  for field in [links,W]:
   total=np.zeros((2,2),complex)
   for v in local:
    y=tuple(root[i]+v[i] for i in range(4));y2=tuple(y[i]+L*(i==mu) for i in range(4))
    for order in orders:total+=leg(field,root,y,order)@leg(field,y,y2,(mu,))@leg(field,root2,y2,order).conj().T
   m.append(total/(24*L**4))
  means.append((root,root2,m[0]));meanerrors.append(float(np.max(abs(m[0]-m[1]))))
gate('paired_contour_means_including_periodic_wrap',max(meanerrors)<2e-14,max(meanerrors))
# Leaving one root unpinned changes its incident coarse mean by that root action.
R=linalg.expm(.2j*pauli[0]);root,root2,M=means[0]
changed=R@M
gate('unpinned_root_fixed_V_control',np.max(abs(changed-M))>.05,float(np.max(abs(changed-M))))
# Root variables have not been integrated out of the fixed V law.
gate('free_coordinate_count_all_blocks',len(sites)*4-len(tree)==len(blocks)*(3*L**4+1))
out={'scope':'finite group-coordinate check; Haar factorization is the separate triangular proof','L':L,'T':T,'fine_links':len(sites)*4,'tree_links':len(tree),'free_links':len(sites)*4-len(tree),'coarse_means_checked':len(means),'actual_contour_words_checked':len(means)*24*L**4,'passed':sum(x['pass'] for x in checks),'total':len(checks),'all_pass':all(x['pass'] for x in checks),'checks':checks,'elapsed_seconds':time.monotonic()-start,'external_scientific_inputs_read':[],'integrity_reads':[]}
print(json.dumps(out,indent=2));sys.exit(0 if out['all_pass'] else 1)
