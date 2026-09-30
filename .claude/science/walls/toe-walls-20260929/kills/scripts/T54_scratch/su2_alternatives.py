"""Kill check: (1) other landed weak-SU(2) realisations on C^8 -> any singlets?  (2) closure of three axis conjugates.
(3) a Hamming-weight-graded (3,2)+(1,1)+(1,1) algebra: consistent as abstract algebra, but what does Y do?"""
import itertools, numpy as np
X=np.array([[0,1],[1,0]],complex);Z=np.diag([1,-1]).astype(complex);I2=np.eye(2,dtype=complex);Yp=np.array([[0,-1j],[1j,0]])
k3=lambda a,b,c:np.kron(np.kron(a,b),c)
G=[k3(X,I2,I2),k3(Z,X,I2),k3(Z,Z,X)]
ac=max(np.abs(G[i]@G[j]+G[j]@G[i]-2*(i==j)*np.eye(8)).max() for i in range(3) for j in range(3))
print("staggered Gammas Clifford check:",ac)
# Cl+(3) su(2): J_k = -(i/2) eps_kij Gamma_i Gamma_j /2 ... fix orientation numerically
e=[G[1]@G[2],G[2]@G[0],G[0]@G[1]]
for sgn in (+1,-1):
    J=[sgn*0.5j*x for x in e]
    err=max(np.abs(J[a]@J[b]-J[b]@J[a]-1j*sum((1 if (a,b,c) in [(0,1,2),(1,2,0),(2,0,1)] else -1 if (a,b,c) in [(0,2,1),(2,1,0),(1,0,2)] else 0)*J[c] for c in range(3))).max() for a in range(3) for b in range(3))
    cas=np.linalg.eigvalsh(sum(j@j for j in J))
    print(f" sign {sgn:+d}: su(2) algebra residual {err:.1e}; Casimir eigenvalues {np.round(cas,4)}")
# (1b) fibre su(2) on each single qubit: Casimir
for f in range(3):
    ops=[[X,Yp,Z][a] for a in range(3)]
    J=[]
    for a in range(3):
        fac=[I2,I2,I2]; fac[f]=ops[a]/2; J.append(k3(*fac))
    print(f" fibre qubit {f}: Casimir eigenvalues {np.round(np.linalg.eigvalsh(sum(j@j for j in J)),4)}")
# (2) closure of the three axis conjugates (independent implementation)
s=1/np.sqrt(2)
E=np.zeros((4,4));E[0,0]=1;E[1,1]=s;E[2,1]=s;E[3,2]=1;E[1,3]=s;E[2,3]=-s
gm=[np.array(m,dtype=complex) for m in ([[0,1,0],[1,0,0],[0,0,0]],[[0,-1j,0],[1j,0,0],[0,0,0]],[[1,0,0],[0,-1,0],[0,0,0]],
 [[0,0,1],[0,0,0],[1,0,0]],[[0,0,-1j],[0,0,0],[1j,0,0]],[[0,0,0],[0,0,1],[0,1,0]],[[0,0,0],[0,0,-1j],[0,1j,0]],(np.diag([1,1,-2])/np.sqrt(3)).tolist())]
def gens_last():
    T=[]
    for g in gm:
        M=np.zeros((4,4),complex);M[:3,:3]=g/2;T.append(np.kron(E@M@E.conj().T,I2))
    J=[np.kron(np.eye(4),x/2) for x in (X,Yp,Z)]
    P=E@np.diag([1,1,1,0])@E.conj().T
    Y=np.kron(P/3-(np.eye(4)-P),I2)
    return T+J+[Y]
def permute(A,perm):
    Pm=np.zeros((8,8))
    for i,b in enumerate(itertools.product([0,1],repeat=3)):
        nb=[0,0,0]
        for q in range(3): nb[perm[q]]=b[q]
        Pm[int("".join(map(str,nb)),2),i]=1
    return Pm@A@Pm.T
base=gens_last()
allg=[]
for f in range(3):
    others=[i for i in range(3) if i!=f]
    allg+= [permute(a,[others[0],others[1],f]) for a in base]
def basis(mats,tol=1e-9):
    V=np.array([np.concatenate([m.real.ravel(),m.imag.ravel()]) for m in mats])
    u,sv,vt=np.linalg.svd(V,full_matrices=False); r=int((sv>tol).sum())
    out=[]
    for row in vt[:r]:
        n=64; out.append((row[:n]+1j*row[n:]).reshape(8,8))
    return out
cur=basis([1j*m for m in allg]); d=len(cur)
for it in range(6):
    new=cur+[a@b-b@a for a,b in itertools.combinations(cur,2)]
    nb=basis(new); 
    if len(nb)==d: break
    cur=nb; d=len(nb)
print("dim of Lie closure of three axis-conjugate gauge algebras:",d,"(su(8)=63, u(8)=64)")
# commutant
rows=[np.kron(g,np.eye(8))-np.kron(np.eye(8),g.T) for g in allg]
sv=np.linalg.svd(np.vstack(rows),compute_uv=False); print("commutant dim:",int((sv<1e-9).sum()))
# (3) hw-graded alternative: SU(3) acting identically on hw=1 and hw=2 (the 3+3 -> (3,2)), SU(2) mixing hw1_i with hw2_i
states=list(itertools.product([0,1],repeat=3)); idx={s_:i for i,s_ in enumerate(states)}
hw1=[(1,0,0),(0,1,0),(0,0,1)]; hw2=[(0,1,1),(1,0,1),(1,1,0)]   # complement pairing i <-> hw2 state missing bit i
T=[];J=[]
for g in gm:
    M=np.zeros((8,8),complex)
    for a in range(3):
        for b in range(3):
            M[idx[hw1[a]],idx[hw1[b]]]=g[a,b]/2; M[idx[hw2[a]],idx[hw2[b]]]=g[a,b]/2
    T.append(M)
for x in (X,Yp,Z):
    M=np.zeros((8,8),complex)
    for a in range(3):
        M[idx[hw1[a]],idx[hw1[a]]]=x[0,0]/2; M[idx[hw1[a]],idx[hw2[a]]]=x[0,1]/2; M[idx[hw2[a]],idx[hw1[a]]]=x[1,0]/2; M[idx[hw2[a]],idx[hw2[a]]]=x[1,1]/2
    J.append(M)
comm=max(np.abs(a@b-b@a).max() for a in T for b in J)
S=sum(g.conj().T@g for g in T+J); ev=np.linalg.eigvalsh(S)
print("hw-graded (3,2)+(1,1)+(1,1) algebra: [colour,weak]=%.1e ; gauge singlets (S0,S3) = %d"%(comm,int((ev<1e-9).sum())))
# hypercharge: commutant of T,J in u(8) is 4-dim abelian? (u(1) on the six, u(2) on S0,S3)
rows=[np.kron(g,np.eye(8))-np.kron(np.eye(8),g.T) for g in T+J]
sv=np.linalg.svd(np.vstack(rows),compute_uv=False); print(" commutant dim in gl(8) (1 on six + 4 on singlet pair =",1+4,"):",int((sv<1e-9).sum()))
print(" traceless Y in that commutant with Y|S0>=Y|S3>=0 is Y=0 on the six (Tr Y = 6y = 0)")
