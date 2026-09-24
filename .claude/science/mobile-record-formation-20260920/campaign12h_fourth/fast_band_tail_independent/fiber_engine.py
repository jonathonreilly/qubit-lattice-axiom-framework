"""Independent complete rotor cube Fourier fibers from charge/link definitions.

A spanning tree fixes the Gauss reference field for each matter word. The five
chord electric fields label physical Z^5 cycles; theta is their Fourier dual.
No campaign builder or author result is imported.
"""
from itertools import combinations
import numpy as np
A=(0,3,5,6)
B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if (a^b).bit_count()==1)
TREE=((0,1),(0,2),(0,4),(3,1),(5,1),(6,2),(3,7))
CHORDS=tuple(e for e in EDGES if e not in TREE)

def words(N):
 for occupied in combinations(range(8),N):
  for minus in combinations(occupied,(N-4)//2):
   yield tuple(-1 if x in minus else 1 if x in occupied else 0 for x in range(8))
WORDS=tuple(words(6));INDEX={q:i for i,q in enumerate(WORDS)}
GRADES=np.array([sum(q[a]==0 for a in A) for q in WORDS])
ONE=np.flatnonzero(GRADES==1)
DARK=np.array([i for i,k in enumerate(ONE) if (next(a for a in A if not WORDS[k][a]),next(b for b in B if not WORDS[k][b])) not in EDGES])
BRIGHT=np.array([i for i in range(len(ONE)) if i not in set(DARK)])

def reference(q):
 """Unique integral tree flow with divergence q-1_A; chord fields zero."""
 rhs=[q[v]-int(v in A) for v in range(8)];remaining=set(range(8));flow={e:0 for e in EDGES}
 assert sum(rhs)==0
 while len(remaining)>1:
  leaf=next(v for v in sorted(remaining) if sum(v in e and all(x in remaining for x in e) for e in TREE)==1)
  edge=next(e for e in TREE if leaf in e and all(x in remaining for x in e));other=next(x for x in edge if x!=leaf)
  sign=1 if edge[0]==leaf else -1
  flow[edge]=sign*rhs[leaf];rhs[other]+=rhs[leaf];remaining.remove(leaf)
 assert rhs[next(iter(remaining))]==0
 return tuple(flow[e] for e in EDGES)

def gauss(q,E):
 div=[0]*8
 for (a,b),e in zip(EDGES,E):div[a]+=e;div[b]-=e
 return all(div[v]==q[v]-int(v in A) for v in range(8))

def phase(phases,edge,step):
 return phases[CHORDS.index(edge)]**step if edge in CHORDS else 1

def matrices(phases):
 n=len(WORDS);F=np.zeros((n,n),complex)
 for col,q in enumerate(WORDS):
  for edge in EDGES:
   a,b=edge
   if not q[a] or q[b]:continue
   qq=list(q);qq[b],qq[a]=qq[a],0
   F[INDEX[tuple(qq)],col]+=phase(phases,edge,-q[a])
 G=(F@F.conj().T-F.conj().T@F)[np.ix_(ONE,ONE)]
 terminal=tuple(words(8));terminalindex={q:i for i,q in enumerate(terminal)};pairs=[]
 for edge in EDGES:
  a,b=edge;pair=[]
  for sign in (1,-1):
   j=np.zeros((len(terminal),len(ONE)),complex)
   for col,k in enumerate(ONE):
    q=WORDS[k]
    if q[a] or q[b]:continue
    qq=list(q);qq[a],qq[b]=sign,-sign
    j[terminalindex[tuple(qq)],col]=phase(phases,edge,sign)
   pair.append(j)
  pairs.append(pair)
 resolved=sum(j.conj().T@j for p in pairs for j in p)
 coherent=sum((p[0]+p[1]).conj().T@(p[0]+p[1]) for p in pairs)
 assert np.array_equal(resolved,coherent)
 assert np.max(np.abs(resolved-np.diag([0 if i in DARK else 2 for i in range(len(ONE))])))<1e-12
 return G,resolved,F
