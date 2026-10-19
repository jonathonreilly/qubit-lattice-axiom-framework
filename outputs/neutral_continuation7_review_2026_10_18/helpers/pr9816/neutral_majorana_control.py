"""Exact constrained Majorana identities; auxiliary variables add no physical qubits."""
AUDIT_TIMEOUT_SEC=300
from functools import reduce
import json

def mul(a,b):
 x,p=a;y,q=b;sign=0
 for i in range(y.bit_length()):
  if y>>i&1:sign+=(x>>(i+1)).bit_count()
 return x^y,p*q*(-1)**sign
def prod(*args):return reduce(mul,args,(0,1))
def scale(a,c):return a[0],a[1]*c
def major(i,a):return 1<<(4*i+a),1
def spin(i,a):return scale(prod(major(i,a),major(i,3)),1j)
def D(i):return prod(*(major(i,a) for a in range(4)))
def link(i,j,a):return scale(prod(major(i,a),major(j,a)),1j)
for i in range(6):
 assert prod(D(i),D(i))==(0,1)
 for a in range(3):
  assert prod(spin(i,a),spin(i,a))==(0,1)
  assert prod(D(i),spin(i,a))==prod(spin(i,a),D(i))
 assert prod(spin(i,0),spin(i,1))==scale(prod(D(i),spin(i,2)),1j)
for a in range(3):
 u=link(0,1,a);v=link(1,2,a);w=link(1,2,(a+1)%3)
 assert prod(u,v)==scale(prod(v,u),-1)
 assert prod(u,w)==prod(w,u)
 h=scale(prod(v,major(1,3),major(2,3)),1j)
 # i[H_neighbor,u] = 2 u u_neighbor c1 c2.
 left=scale(prod(h,u),1j);right=scale(prod(u,h),-1j)
 assert left[0]==right[0]
 assert (left[0],left[1]+right[1])==scale(prod(u,v,major(1,3),major(2,3)),2)
 assert h==scale(prod(spin(1,a),spin(2,a)),-1)

def loop(verts):
 n=len(verts);axes=[]
 for i,p in enumerate(verts):
  q=verts[(i+1)%n];assert abs(p[0]-q[0])+abs(p[1]-q[1])==1
  axes.append(0 if p[1]==q[1] else 1)
 turns=[i for i in range(n) if axes[i-1]!=axes[i]]
 w=prod(*(link(i,(i+1)%n,axes[i]) for i in range(n)))
 expected=prod(*(prod(D(i),spin(i,2)) for i in turns))
 phase=(-1)**(n//2+(0 in turns))
 assert w==scale(expected,phase)
 return dict(perimeter=n,turns=len(turns),start_turn=0 in turns,phase=phase)
verts=[(0,0),(1,0),(2,0),(2,1),(1,1),(0,1)]
rows=[loop(verts[k:]+verts[:k]) for k in range(len(verts))]
for n in range(1,9):
 transport=prod(*(link(i,i+1,0) for i in range(n)))
 endpoint=scale(prod(major(0,3),transport,major(n,3)),1j)
 expected=scale(prod(spin(0,0),spin(n,0)),1j**(n+1))
 assert endpoint==expected
print(json.dumps(dict(status='exact-algebra-pass',loop_basepoints=rows,straight_endpoint_lengths=list(range(1,9)),scope='Constrained rewriting, not physical deconfined fermions or independent static links')))
