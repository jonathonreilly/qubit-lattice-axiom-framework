"""d=4 scaling check: KD fibre (16) vs 4-component Wilson-Dirac, identical L^4 torus & gauge field.
Flux n12 in the 1-2 plane and n34 in the 3-4 plane (both needed for a nonzero 4d index)."""
import numpy as np, time
from kd import kd_gammas

def gauge_links_4d(L, n12, n34):
    """U_mu(x) for mu=0..3 on L^4. Constant field strength in planes (0,1) and (2,3)."""
    def f(nn, u, v, Lu, Lv):   # returns (A_u, A_v) style phases for a 2-plane
        return None
    def U(mu, x):
        x0,x1,x2,x3 = x
        if mu==0: return np.exp(-1j*2*np.pi*n12*x1/(L*L))
        if mu==1: return np.exp(1j*2*np.pi*n12*x0/L) if x1==L-1 else 1.0+0j
        if mu==2: return np.exp(-1j*2*np.pi*n34*x3/(L*L))
        if mu==3: return np.exp(1j*2*np.pi*n34*x2/L) if x3==L-1 else 1.0+0j
    return U

def build_DW4(L, n12, n34, Gam, r=1.0, a=1.0):
    f=Gam[0].shape[0]; N=L**4; If=np.eye(f,dtype=complex)
    D=np.zeros((f*N,f*N),dtype=complex); U=gauge_links_4d(L,n12,n34)
    def ix(x): return ((x[0]*L+x[1])*L+x[2])*L+x[3]
    from itertools import product
    for x in product(range(L),repeat=4):
        i=ix(x); D[f*i:f*i+f, f*i:f*i+f]+=(4*r/a)*If
        for mu in range(4):
            y=list(x); y[mu]=(y[mu]+1)%L; j=ix(y); u=U(mu,x)
            D[f*i:f*i+f, f*j:f*j+f]+=-(1/(2*a))*(r*If-Gam[mu])*u
            D[f*j:f*j+f, f*i:f*i+f]+=-(1/(2*a))*(r*If+Gam[mu])*np.conj(u)
    return D

def idx_of(DW, CH, mrho=1.0, a=1.0):
    N=DW.shape[0]//CH.shape[0]; C=np.kron(np.eye(N),CH)
    H=C@(DW-(mrho/a)*np.eye(DW.shape[0])); hh=np.max(np.abs(H-H.conj().T))
    w,v=np.linalg.eigh((H+H.conj().T)/2); sg=v@np.diag(np.sign(w))@v.conj().T
    Dov=(1.0/a)*(np.eye(DW.shape[0])+C@sg)
    gw=np.max(np.abs(C@Dov+Dov@C-a*(Dov@C@Dov)))
    return hh, gw, np.min(np.abs(w)), -0.5*np.sum(np.sign(w))

def idx_of_OLD(DW, CH, mrho=1.0, a=1.0):
    n=DW.shape[0]; C=np.kron(np.eye(n//CH.shape[0]),CH)
    ch=np.max(np.abs(C@DW@C-DW.conj().T))
    A=DW-(mrho/a)*np.eye(n); U,S,Vh=np.linalg.svd(A); V=U@Vh
    Dov=(1.0/a)*(np.eye(n)+V)
    gw=np.max(np.abs(C@Dov+Dov@C-a*(Dov@C@Dov)))
    ind=0.5*np.real(np.trace(C@(2*np.eye(n)-a*Dov)))
    return ch,gw,S.min(),ind

# 4d Euclidean gammas (4x4)
s1=np.array([[0,1],[1,0]],dtype=complex); s2=np.array([[0,-1j],[1j,0]],dtype=complex)
s3=np.array([[1,0],[0,-1]],dtype=complex); I2=np.eye(2,dtype=complex)
g=[np.kron(s1,s1),np.kron(s1,s2),np.kron(s1,s3),np.kron(s2,I2)]
g5=np.kron(s3,I2)
assert max(np.max(np.abs(g[a]@g[b]+g[b]@g[a]-2*(a==b)*np.eye(4))) for a in range(4) for b in range(4))<1e-12
assert max(np.max(np.abs(g5@g[a]+g[a]@g5)) for a in range(4))<1e-12

Gam,Gbar,G=kd_gammas(4)
CL=Gam[0]@Gam[1]@Gam[2]@Gam[3]
print("d=4 Clifford chirality CL = G1G2G3G4:",
      f"herm={np.max(np.abs(CL-CL.conj().T)):.1e} CL^2-I={np.max(np.abs(CL@CL-np.eye(16))):.1e}",
      f"{{CL,Gam}}={max(np.max(np.abs(CL@x+x@CL)) for x in Gam):.1e} TrCL={np.real(np.trace(CL)):.2f}",
      f"conj(CL)-CL={np.max(np.abs(CL.conj()-CL)):.1e}")
print(f"grade chirality G: conj(G)-G={np.max(np.abs(G.conj()-G)):.1e}  TrG={np.real(np.trace(G)):.2f}")
L=4
for (n12,n34) in [(0,0),(1,1),(1,2),(2,1)]:
    t=time.time()
    DWc=build_DW4(L,n12,n34,g); r1=idx_of(DWc,g5)
    print(f"  (n12,n34)=({n12},{n34})  Wilson f=4 : chirherm={r1[0]:.1e} GW={r1[1]:.2e} gap={r1[2]:.3f} index={r1[3]:+.6f}   [{time.time()-t:.0f}s]",flush=True)
    t=time.time()
    DKD=build_DW4(L,n12,n34,Gam); rG=idx_of(DKD,G); rC=idx_of(DKD,CL)
    print(f"                        KD f=16   : GW={max(rG[1],rC[1]):.2e} gap={rG[2]:.3f} "
          f"index(grade G)={rG[3]:+.6f}  index(Clifford CL)={rC[3]:+.6f}   [{time.time()-t:.0f}s]",flush=True)
