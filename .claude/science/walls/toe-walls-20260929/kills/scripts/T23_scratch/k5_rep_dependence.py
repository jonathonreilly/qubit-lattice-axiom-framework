#!/usr/bin/env python3
"""K5: the attack's orbit/stabiliser numbers (block B4, A2) use the sign-free PERMUTATION action of O on the triplet.
Block E / plain verdict ('a direction along a cube diagonal') use the VECTOR action (signed permutation matrices).
Compare orbit sizes and stabilisers of the same circulant W(delta) under the two actions."""
import itertools, numpy as np
np.set_printoptions(precision=4, suppress=True)
G=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        M=np.zeros((3,3))
        for j in range(3): M[p[j],j]=s[j]
        G.append((p,s,M))
det=lambda M:int(round(np.linalg.det(M)))
C=np.roll(np.eye(3),1,axis=0)      # real cyclic shift
def W(b): return np.eye(3)+b*C+np.conj(b)*C@C
b=np.sqrt(2)/2*np.exp(1j*2/9)
W0=W(b)
def orbit(actfun,group):
    orb=[];stab=0
    for g in group:
        X=actfun(g)@W0@actfun(g).conj().T
        if np.allclose(X,W0): stab+=1
        if not any(np.allclose(X,Y) for Y in orb): orb.append(X)
    return len(orb),stab
perm=lambda g: np.abs(g[2])                  # sign-free permutation action (attack's blocks A-D)
vec =lambda g: g[2]                          # vector action (Block E reading)
prop=[g for g in G if det(g[2])==1]
print("action        group   |orbit of W(delta)|  |stabiliser|")
for nm,a in (("permutation",perm),("vector T1",vec)):
    for gn,gr in (("O",prop),("O_h",G)):
        o,s=orbit(a,gr); print(f"{nm:12s}  {gn:4s}    {o:3d}                  {s:3d}")
# under the vector action is W(-delta) reachable by a proper rotation?
Wm=W(np.conj(b))
reach=[g for g in prop if np.allclose(vec(g)@W0@vec(g).T,Wm)]
print("proper rotations (vector action) mapping W(delta) -> W(-delta):",len(reach), [(g[0],g[1]) for g in reach][:3])
# under vector action does C4z map n.L to -n.L?
Lk=[ -1j*np.array([[ (1 if (k,i,j) in [(0,1,2),(1,2,0),(2,0,1)] else -1 if (k,i,j) in [(0,2,1),(2,1,0),(1,0,2)] else 0) for j in range(3)] for i in range(3)]) for k in range(3)]
nL=sum(Lk)/1.0
C4z=[g for g in prop if g[0]==(1,0,2) and g[1]==(-1,1,1)][0]
X=vec(C4z)@nL@vec(C4z).T
print("vector action: C4z (n.L) C4z^T == -(n.L)?",np.allclose(X,-nL),"  == (m.L) for m=R n =(-1,1,1)?",np.allclose(X,-1j*0+sum(c*Lk[k] for k,c in enumerate([-1,1,1]))))
X2=perm(C4z)@nL@perm(C4z).T
print("permutation action: C4z (n.L) C4z^T == -(n.L)?",np.allclose(X2,-nL))
