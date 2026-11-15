# Event lattice E = {v in Z^4 : all coordinates of equal parity}; shortest vectors, similarity to D4, stabilizers.
import itertools, numpy as np
from fractions import Fraction
# events from the definition: active even cubes at even h (X in 2Z^3), odd cubes at odd h (X in 2Z^3+1)
R=3
ev=set()
for h in range(-R,R+1):
    for b in itertools.product(range(-R-1,R+2),repeat=3):
        X=tuple(2*c+(h%2) for c in b)
        if all(abs(c)<=R for c in X): ev.add(X+(h,))
par=set(v for v in itertools.product(range(-R,R+1),repeat=4) if len(set(c%2 for c in v))==1)
print("A3 event set equals equal-parity set in box:",ev==par)
twoD4s=set()
for v in itertools.product(range(-R,R+1),repeat=4): twoD4s.add(tuple(2*c for c in v))
for v in itertools.product(range(-R-1,R+1),repeat=4): twoD4s.add(tuple(2*c+1 for c in v))
print("A3 equals 2*D4^* in box:",par==set(v for v in twoD4s if all(abs(c)<=R for c in v)))
nz=[v for v in par if any(v)]; m=min(sum(c*c for c in v) for v in nz)
short=[v for v in nz if sum(c*c for c in v)==m]
print("A3 min norm^2:",m,"count:",len(short),"all-odd:",sum(1 for v in short if v[0]%2),"axis:",sum(1 for v in short if v[0]%2==0), "contains (0,0,0,2):",(0,0,0,2) in short, " e4 in lattice:",(0,0,0,1) in par)
def Phi(v): return (Fraction(v[0]+v[1],2),Fraction(v[0]-v[1],2),Fraction(v[2]+v[3],2),Fraction(v[2]-v[3],2))
img=set(Phi(v) for v in par)
okint=all(all(c.denominator==1 for c in z) and sum(z)%2==0 for z in img)
okn=all(2*sum(c*c for c in Phi(v))==sum(c*c for c in v) for v in par)
# surjectivity onto D4 inside a small ball
D4=[z for z in itertools.product(range(-1,2),repeat=4) if sum(z)%2==0]
inv=lambda z:(z[0]+z[1],z[0]-z[1],z[2]+z[3],z[2]-z[3])
print("A3 Phi(E) subset D4:",okint," norm halves:",okn," inverse of small D4 vectors in E:",all(len(set(c%2 for c in inv(z)))==1 for z in D4)," Phi(inv)=id:",all(tuple(Phi(inv(z)))==tuple(z) for z in D4))
# B12: orthogonal automorphisms of the lattice = maps permuting the 24 shortest vectors preserving Gram.
S=[np.array(v) for v in short]
basis=[np.array(b) for b in [(2,0,0,0),(0,2,0,0),(0,0,2,0),(1,1,1,1)]]  # Z-basis of E
B=np.array(basis).T
G=B.T@B
auts=[]
def rec(k,imgs):
    if k==4:
        M=np.array(imgs).T@np.linalg.inv(B)
        auts.append(M); return
    for s in S:
        if all(int(s@imgs[j])==G[j,k] for j in range(k)) and int(s@s)==G[k,k]:
            rec(k+1,imgs+[s])
rec(0,[])
sset=set(short)
auts=[M for M in auts if all(tuple(int(round(c)) for c in M@np.array(v)) in sset for v in short)]
print("B12 |Aut(E)| (orthogonal, origin fixed):",len(auts)," (|W(F4)|=1152)")
e4=np.array([0,0,0,1.])
st=[M for M in auts if np.allclose(M@e4,e4)]; line=[M for M in auts if np.allclose(abs(M@e4),[0,0,0,1])]
print("B12 stabilizer of oriented time direction:",len(st)," of the line:",len(line)," elements moving it off its line:",len(auts)-len(line))
print("B12 all stabilizer elements are signed spatial permutations:",all(np.allclose(abs(M[:3,:3]).sum(0),1) and np.allclose(M[3,3],1) for M in st))
# slices: an automorphism maps every time slice into a time slice iff it keeps the line
def keeps_slices(M):
    for h in (0,1):
        sl=[np.array(v) for v in par if v[3]==h and max(abs(c) for c in v)<=2]
        hs=set(round(float((M@v)[3]),9) for v in sl)
        if len(hs)>1: return False
    return True
ks=[keeps_slices(M) for M in auts]
print("B12 automorphisms mapping slices h=0,1 into single slices:",sum(ks)," ; all of them keep the time line:",all(np.allclose(abs(M@e4),[0,0,0,1]) for M,k in zip(auts,ks) if k))
sw=np.eye(4)[[3,1,2,0]]
print("B12 swap(1,4) is an automorphism:",any(np.allclose(M,sw) for M in auts))
