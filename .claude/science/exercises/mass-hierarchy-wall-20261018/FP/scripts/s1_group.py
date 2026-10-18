# S1: exact group theory of the Lattice axiom (Z^3, translations, proper cubic rotations).
import itertools, numpy as np
from fractions import Fraction as Fr
def rot_group(d):
    G=[]
    for p in itertools.permutations(range(d)):
        for s in itertools.product([1,-1],repeat=d):
            M=np.zeros((d,d),int)
            for i in range(d): M[i,p[i]]=s[i]
            if round(np.linalg.det(M))==1: G.append(M)
    return G
O=rot_group(3); print("|O| =",len(O), " contains -1:", any((M==-np.eye(3,dtype=int)).all() for M in O))
# star sizes on the BZ, k = 2*pi*n/N, N in {2,4,6,8,12}
sizes={}
for N in [2,4,6,8,12]:
    for n in itertools.product(range(N),repeat=3):
        k=np.array(n)
        orb={tuple((M@k)%N) for M in O}
        key=len(orb)
        sizes.setdefault(key,set()).add(tuple(Fr(int(x),N) for x in sorted(np.minimum(k%N,(N-k)%N))))
print("star sizes found:",sorted(sizes))
print("size-3 stars (k/2pi, up to sign/perm):",sorted(sizes[3]))
# corner orbits
corners=list(itertools.product([0,1],repeat=3))
orbs={}
for c in corners:
    o=frozenset(tuple((M@np.array(c))%2) for M in O); orbs[o]=1
print("corner orbit sizes:",sorted(len(o) for o in orbs))
# generalisation: Z^d, minimal nontrivial period-2 orbit = d
for d in [2,3,4,5]:
    Gd=rot_group(d); cs=list(itertools.product([0,1],repeat=d))
    os_={frozenset(tuple((M@np.array(c))%2) for M in Gd) for c in cs}
    print(f"d={d}: corner orbit sizes {sorted(len(o) for o in os_)}")
# image of G on the scalar X triplet: translations e_j -> diag((-1)^{delta_ij}), rotation R -> permutation of axes
X=[np.array(v) for v in [(1,0,0),(0,1,0),(0,0,1)]]
def rep_rot(M):
    P=np.zeros((3,3),int)
    for i in range(3):
        j=[jj for jj in range(3) if (((M@X[i])%2)==X[jj]).all()][0]; P[j,i]=1
    return P
def rep_tr(t): return np.diag([(-1)**int(X[i]@t) for i in range(3)])
gens=[rep_rot(M) for M in O]+[rep_tr(np.array(t)) for t in [(1,0,0),(0,1,0),(0,0,1)]]
grp={tuple(np.eye(3,dtype=int).ravel())}; frontier=list(grp)
while frontier:
    new=[]
    for a in frontier:
        A=np.array(a).reshape(3,3)
        for g in gens:
            b=tuple((g@A).ravel())
            if b not in grp: grp.add(b); new.append(b)
    frontier=new
print("image group order on X triplet:",len(grp))
signed=all(sorted(np.abs(np.array(g)).tolist())==sorted(np.eye(3,dtype=int).ravel().tolist()) for g in grp)
print("all elements signed permutations:",signed)
# irreducibility: commutant dimension via averaging
mats=[np.array(g).reshape(3,3).astype(float) for g in grp]
Cm=np.zeros((9,9))
for g in mats: Cm+=np.kron(g,np.linalg.inv(g).T)
Cm/=len(mats); print("commutant dim (1 => irreducible):",int(round(np.trace(Cm))))
print("translation (1,1,1) acts as:",np.diag(rep_tr(np.array((1,1,1)))))
print("translations e_j+e_k act as:",[list(np.diag(rep_tr(np.array(t)))) for t in [(0,1,1),(1,0,1),(1,1,0)]])
ker=[M for M in O if (rep_rot(M)==np.eye(3,dtype=int)).all()]; print("rotations acting trivially on labels:",len(ker),"(V4)")
# det+1 subgroup = S4 in T1 form?  equals the set of rotation matrices O?
det1={g for g in grp if round(np.linalg.det(np.array(g).reshape(3,3)))==1}
print("det+1 subgroup order:",len(det1)," equals O (T1 matrices):",det1=={tuple(M.ravel()) for M in O})
# induced reps Ind_{D4}^{O}: characters via Frobenius
def cls(M):
    tr=int(np.trace(M)); 
    # order
    A=M.copy(); n=1
    while not (A==np.eye(3,dtype=int)).all(): A=A@M; n+=1
    return (n,tr)
cl={}
for M in O: cl.setdefault(cls(M),[]).append(M)
print("O classes (order,trace):count",{k:len(v) for k,v in cl.items()})
