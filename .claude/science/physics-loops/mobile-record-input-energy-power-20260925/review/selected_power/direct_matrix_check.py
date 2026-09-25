#!/usr/bin/env python3
"""Separate finite-graph implementation: complex five-input Gram matrices.

Does not import the Laurent-word implementation or any author code.
Enumerates every H4 pair on the finite graph, including commuting far terms.
"""
from collections import defaultdict
from itertools import product
from pathlib import Path
import hashlib,json,math
import numpy as np

HERE=Path(__file__).resolve().parent
L=6
vertices=list(product(range(L),repeat=3))
aside=[v for v in vertices if sum(v)%2==0]
def nb(v):
 for mu in range(3):
  for sign in (-1,1):
   w=list(v);w[mu]=(w[mu]+sign)%L;yield tuple(w)
neighbors={v:list(nb(v)) for v in vertices}
pairs=set()
for u in aside:
 for b in neighbors[u]:
  for v in neighbors[b]:
   if u!=v:pairs.add(tuple(sorted((u,v))))
pairs=sorted(pairs)
edges=[(a,b) for a in aside for b in neighbors[a]]
a=(0,0,0);d=(1,1,0);h=(2,2,0);c=(1,0,0);e=(0,1,0);b=(5,0,0)
old_destinations=[x for x in neighbors[a] if x!=b]
charges={u:(-1 if u in (d,h) else 1) for u in aside}
pre=[{x:1 for x in old_destinations if x!=vacant} for vacant in old_destinations]
finalB={x:1 for x in neighbors[a]}
def outbound_pair(u,v,Aq,Bq,angles):
 answer=defaultdict(complex)
 for x in neighbors[u]:
  if x in Bq:continue
  for y in neighbors[v]:
   if y in Bq or y==x:continue
   after=dict(Bq);after[x]=Aq[u];after[y]=Aq[v]
   key=tuple(sorted(after.items()))
   answer[key]+=np.exp(-1j*(Aq[u]*angles[u,x]+Aq[v]*angles[v,y]))
 return answer
def pair_gram(images):
 matrix=np.zeros((len(images),len(images)),complex)
 for i,left in enumerate(images):
  for j,right in enumerate(images):
   matrix[i,j]=sum(np.conj(value)*right.get(key,0) for key,value in left.items())
 return matrix
laurent=json.loads((HERE/'L6_RESULTS.json').read_text())['answers'][0]['twice_power_laurent']
def polynomial(angles):
 return sum(row['coefficient']/2*np.exp(1j*sum(x['shift']*angles[tuple(x['a']),tuple(x['b'])] for x in row['flow'])) for row in laurent)
rng=np.random.default_rng(7351)
samples=[]
for sample in range(4):
 if sample==0:angles={edge:0. for edge in edges}
 elif sample==1:
  harmonic=np.array([.37,-.23,.51]);angles={}
  for u,v in edges:
   delta=np.array(v)-np.array(u);delta=np.where(delta>3,delta-L,np.where(delta<-3,delta+L,delta))
   angles[u,v]=float(delta@harmonic)
 else:angles={edge:float(rng.normal(scale=.23 if sample==2 else .013)) for edge in edges}
 Hpre=np.zeros((5,5),complex);Hout=0.
 for u,v in pairs:
  images=[outbound_pair(u,v,charges,q,angles) for q in pre]
  Hpre-=2*pair_gram(images)
  image=outbound_pair(u,v,charges,finalB,angles)
  Hout-=2*sum(abs(value)**2 for value in image.values())
 assert np.max(abs(Hpre-Hpre.conj().T))<1e-10
 psi=np.zeros(5,complex)
 psi[old_destinations.index(e)]=np.exp(-1j*angles[d,c])/math.sqrt(2)
 psi[old_destinations.index(c)]=-np.exp(-1j*angles[d,e])/math.sqrt(2)
 for sigma in (-1,1):
  coefficients=np.array([np.exp(1j*(sigma*angles[a,b]-angles[a,x])) for x in old_destinations])
  born=coefficients@psi
  gain=abs(born)**2*Hout
  subtract=float(np.real(np.conj(born)*(coefficients@Hpre@psi)))
  power=gain-subtract;expected=polynomial(angles)
  assert abs(expected.imag)<1e-8
  assert abs(power-expected.real)<2e-8,(sample,sigma,power,expected)
  loop_angle=angles[a,c]-angles[d,c]+angles[d,e]-angles[a,e]
  assert abs(abs(born)**2-(1-math.cos(loop_angle)))<1e-13
  if sample==0:assert Hout==-321*L**3+7146
  samples.append(dict(sample=sample,sigma=sigma,born_norm_squared=abs(born)**2,
      full_gain=gain,full_anticommutator_subtrahend=subtract,full_power=power,
      laurent_power=expected.real,difference=power-expected.real,
      full_output_H4_diagonal=Hout))
summary=dict(scope='Separate complex matrix implementation of full side-six pair Hamiltonian on the five relevant prebirth words; original selected mark.',
    full_H4_pairs=len(pairs),prebirth_words=len(pre),samples=samples,
    all_actual_electric_terms_excluded_from_this_magnetic_check=True,
    no_author_code_or_Laurent_implementation_imported=True,
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
with (HERE/'DIRECT_MATRIX_RESULTS.json').open('x') as f:json.dump(summary,f,indent=2);f.write('\n')
print(json.dumps(summary,indent=2))
