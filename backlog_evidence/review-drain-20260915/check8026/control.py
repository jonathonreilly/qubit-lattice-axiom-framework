from itertools import product,permutations
from fractions import Fraction as F
import json,time
from pathlib import Path
start=time.monotonic(); checks=[]
def ck(name,test):
 assert test,name
 checks.append(name)
# Independent exhaustive 3x3 torus: edge coefficients are adjacent-cell differences.
L=3
def bd(a):return tuple((a[x*L+y]-a[((x-1)%L)*L+y])%3 for x in range(L) for y in range(L))+tuple((a[x*L+y]-a[x*L+(y-1)%L])%3 for x in range(L) for y in range(L))
allchains=list(product(range(3),repeat=9))
for R,S in [(1,1),(1,2),(2,2)]:
 target=tuple(int(x<R and y<S) for x in range(L) for y in range(L));sol=[a for a in allchains if bd(a)==bd(target)];ck(f'complete affine family {R}x{S}',len(sol)==3);ck(f'minimum support {R}x{S}',min(sum(z!=0 for z in a) for a in sol)==min(R*S,9-R*S))
# SU3 diagonal torus phases followed by permutations form an exact first-moment
# ensemble: average phases kill differing row indices, permutations give1/3.
# Verify all matrix-unit contractions without copying a Kronecker formula.
for i,j,k,l in product(range(3),repeat=4):
 hits=sum(1 for p in permutations(range(3)) if p[i]==j and p[k]==l)
 covariance=F(hits,6) if i==k else F(0)
 ck(f'first Haar moment {i}{j}{k}{l}',covariance==F(int(i==k and j==l),3))
# Trace(AU) trace(U*B) at A=E01,B=E10 samples |U10|².
ck('offdiagonal trace contraction',F(sum(p[1]==0 for p in permutations(range(3))),6)==F(1,3))
one=F(2)*F(2)*F(1,6)*F(1,6)/16
middle=F(2,9)/(6*16)**2; ends=2*F(2,9)/(36*16*24)
ck('one face',one==F(1,144));ck('two face',middle+ends==F(7,124416));ck('wrong energy adverse',middle+2*F(2,9)/(36*16*16)!=middle+ends)
q=F(1,4);ck('KP ordinary slack',q/(1-q)<=F(1,2))
for m in range(1,12):ck(f'marked geometric reserve {m}',1/(1-q)<=2**m)
print(json.dumps({'checks':checks,'PASS':len(checks),'FAIL':0,'elapsed_sec':time.monotonic()-start,'scope':'Independent finite F3 exhaustive family and first Haar-moment ensemble/rational perturbation/KP arithmetic; no primary imports or theorem-by-simulation.'},indent=2))
