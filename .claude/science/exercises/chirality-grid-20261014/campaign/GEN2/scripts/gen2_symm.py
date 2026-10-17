import numpy as np, itertools
rng=np.random.default_rng(20261017)
# O_h as 48 signed permutation matrices
G=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        M=np.zeros((3,3));
        for i in range(3): M[i,p[i]]=s[i]
        G.append(M)
G=np.array(G)
P=np.abs(G)                       # action on unoriented axes = generation rep
chiP=np.trace(P,axis1=1,axis2=2); chiv=np.trace(G,axis1=1,axis2=2)
chiv2=np.array([np.trace(g@g) for g in G])
chiS2=(chiv**2+chiv2)/2
mult=lambda chi: np.sum(chi)/48
print("S1 A1g in P:",mult(chiP)," A1g in End(P):",mult(chiP**2)," A1g in End(P)xSym2(R3):",mult(chiP**2*chiS2),
      " A1g in End(P)xSym2_traceless:",mult(chiP**2*(chiS2-1)), " A1g in Sym2:",mult(chiS2))
# S3 image, E projector on End(P)
S3=[np.eye(3)[list(p)] for p in itertools.permutations(range(3))]
def chiE(g):
    t=np.trace(g); return {3:2,1:0,0:-1}[int(round(t))]
def projE(M): return (2/6)*sum(chiE(g)*g@M@g.T for g in S3)
C=np.roll(np.eye(3),1,axis=0)
# S2: circulants have zero E projection; zero E projection => circulant
a,b,c=rng.normal(size=3)+1j*rng.normal(size=3)
Yc=a*np.eye(3)+b*C+c*C@C
print("S2 |P_E(circulant)|:",np.abs(projE(Yc)).max())
M=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); Mn=M-projE(M)
coef=[np.mean(np.diag(Mn@np.linalg.matrix_power(C,k).T)) for k in range(3)]
print("S2 |M - P_E M - circulant fit|:",np.abs(Mn-sum(coef[k]*np.linalg.matrix_power(C,k) for k in range(3))).max())
a2,b2,c2=rng.normal(size=3)+1j*rng.normal(size=3); Yc2=a2*np.eye(3)+b2*C+c2*C@C
Hu=Yc@Yc.conj().T; Hd=Yc2@Yc2.conj().T
Uu=np.linalg.eigh(Hu)[1]; Ud=np.linalg.eigh(Hd)[1]; V=Uu.conj().T@Ud
print("S2 |[Yu,Yd]| circulants:",np.abs(Yc@Yc2-Yc2@Yc).max()," CKM |V| rows (perm-like):",np.round(np.abs(V),12).tolist())
# S3: first-order eigenvalue response to an E (strain-like) perturbation of Y
X=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); dY=projE(X)
def resp(Y,dY):
    H=Y@Y.conj().T; w,U=np.linalg.eigh(H); dH=dY@Y.conj().T+Y@dY.conj().T
    return w, np.real(np.diag(U.conj().T@dH@U))
w,r=resp(Yc,dY); print("S3 circulant: eigen",w," first-order shifts",r)
Yg=Yc+0.3*projE(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
w,r=resp(Yg,dY); print("S3 with E component: eigen",w," first-order shifts",r)
# S4: anomaly arithmetic for generation permutations (per 16-plet)
q3=[0,1,2]
print("S4 Z3: 16*Sum q mod3 =",16*sum(q3)%3," 16*Sum q^3 mod 9 =",16*sum(x**3 for x in q3)%9,
      " Spin(10)^2-Z3: T(16)*Sum q mod 3 =",2*sum(q3)%3, "; transposition: odd 16-plets =1 -> nu =16 mod 16 =",16%16)
# S5: folding of the 8 corners under residual translations c Z^3
for cc in range(2,9):
    fold=[n for n in itertools.product([0,1],repeat=3) if all(((cc*ni)%2)==0 for ni in n)]
    idx=3+(-3 if len(fold)==8 else 0)
    print(f"S5 c={cc}: corners on Gamma label {len(fold)} ; folded Gamma index per component {idx}")
