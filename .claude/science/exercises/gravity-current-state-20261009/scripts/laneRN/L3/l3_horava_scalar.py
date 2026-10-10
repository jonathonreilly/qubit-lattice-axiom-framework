"""L3 check 2: drop the local scalar constraint (Horava projectable analogue: lapse N(t) only).
Keep the vector constraint k.E = 0 and vector gauge.  Kinetic J/2[E:E - c (trE)^2], potential g/2 h:R(h)
(sign chosen so TT is positive, as in the 09-14 note).  Report omega^2/(J g k^2) of the TT pair and of the
transverse scalar t, versus c.  c = lambda/(3 lambda - 1) maps to Horava's lambda (c=1/2 <-> lambda=1)."""
import numpy as np, itertools
eps = np.zeros((3,3,3))
for (i,j,k),s in (((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((2,1,0),-1),((1,0,2),-1)): eps[i,j,k]=s
def basis():
    B=[]
    for i in range(3):
        m=np.zeros((3,3)); m[i,i]=1; B.append(m)
    for (i,j) in ((0,1),(1,2),(0,2)):
        m=np.zeros((3,3)); m[i,j]=m[j,i]=1/np.sqrt(2); B.append(m)
    return B
B=basis()
def Rop(k,h): return -np.einsum('iab,jcd,a,c,bd->ij',eps,eps,k,k,h)
def run(kdir, c):
    k=np.array(kdir,float); k/=np.linalg.norm(k)
    M=np.array([[np.sum(B[a]*Rop(k,B[b])) for b in range(6)] for a in range(6)])
    Kc=np.array([[np.sum(B[a]*B[b]) - c*np.trace(B[a])*np.trace(B[b]) for b in range(6)] for a in range(6)])
    # transverse subspace: tensors with k_i X_ij = 0
    C=np.array([[ (k@B[a])[j] for a in range(6)] for j in range(3)])
    _,s,vt=np.linalg.svd(C); T=vt[3:].T          # 6x3 basis of ker
    Mt=T.T@M@T; Kt=T.T@Kc@T
    # identify TT vs scalar: scalar = trace-carrying direction in T
    tr=np.array([np.trace(sum(T[a,i]*B[a] for a in range(6))) for i in range(3)])
    w=np.linalg.eigvals(Kt@Mt)
    return Mt, Kt, np.sort(w.real), tr
for kdir in ((0,0,1),(1,2,3)):
    Mt,_,_,_=run(kdir,0.5)
    # choose sign so that TT block is positive
    sgn = 1.0
    w = np.linalg.eigvalsh(Mt)
    print("k dir",kdir,"eig of h:R on transverse subspace:",np.round(w,6))
for c in (0.0, 0.25, 1/3, 0.45, 0.5, 0.55, 0.75, 1.0):
    out=[]
    for kdir in ((0,0,1),(1,2,3)):
        Mt,Kt,w,tr=run(kdir,c)
        # sign convention: potential g/2 * s * h:R with s chosen so TT positive (TT eigenvalues of h:R are negative here)
        w=np.sort(np.linalg.eigvals(Kt@(-Mt)).real)
        out.append(np.round(w,6))
    lam = c/(3*c-1) if abs(3*c-1)>1e-12 else np.inf   # invert c = lambda/(3 lambda -1)
    print(f"c={c:.3f} (Horava lambda={lam:.3f}): omega^2/(J g k^2) k||z {out[0]}, generic {out[1]};  predicted scalar -(1-2c)={-(1-2*c):.3f}")

print("\n--- corrected sign: potential +g/2 h:R(h) with R = -eps eps k k h makes the TT pair positive ---")
for c in (0.0, 0.25, 0.45, 0.5, 0.55, 0.75, 1.0):
    Mt,Kt,_,tr=run((1,2,3),c)
    w,v=np.linalg.eig(Kt@Mt)
    rows=[]
    for i in range(3):
        vec=v[:,i].real; trc=abs(tr@vec)/np.linalg.norm(vec)
        # sign of kinetic and potential on this eigenvector (ghost test)
        kin=vec@Kt@vec; pot=vec@Mt@vec
        rows.append((round(w[i].real,4), 'scalar' if trc>1e-6 else 'TT', round(float(np.sign(kin)),0), round(float(np.sign(pot)),0)))
    print(f"c={c:.2f}: (omega^2/(Jgk^2), type, sign kinetic, sign potential):", sorted(rows))
