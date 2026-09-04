"""T191 - DOES M_4(C) WITH DIRAC GAMMAS COUPLE THE BLOCKS?  The decisive test.

R123 named this, and there is a subtlety that must be got right first.  T186's
k=2 enlargement used Gamma_a = sigma_a (x) I_2, which keeps the extra M_2 factor
PURELY INTERNAL -- it supplies gauge room but NO fourth gamma, so chirality is
still absent there.  R123's point requires a different construction:

   (a) T186's:  Gamma_a = sigma_a (x) I_2      -- extra factor internal, no gamma_5
   (b) R123's:  Gamma_a = gamma_a of M_4(C)    -- three of the FOUR Dirac gammas,
                                                  so gamma_4 and gamma_5 EXIST

Under (b) the chirality gamma_5 ANTI-commutes with every gamma_a, hence with the
whole Dirac operator D = sum_a gamma_a d_a.  An anticommuting chirality maps its
+1 eigenspace to its -1 eigenspace -- so if the taste blocks are the gamma_5
eigenspaces, D COUPLES THEM, and R120's obstruction dissolves.

Test, on construction (b):
  (1) does gamma_5 anticommute with D(p) at every momentum?
  (2) what is the continuum taste algebra, and its centre?
  (3) is the central splitting element still Gamma_1 Gamma_2 Gamma_3 (which in
      d=3 commuted, R121), and does D now connect the blocks?
CONTROL: construction (a) must reproduce T186's result (u(8)+u(8), centre 2)."""
import numpy as np, itertools
s=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex); Z2=np.zeros((2,2),dtype=complex)
blk=lambda a,b,c,d: np.block([[a,b],[c,d]])
g0=blk(I2,Z2,Z2,-I2); gi=[blk(Z2,x,-x,Z2) for x in s]
g5=1j*g0@gi[0]@gi[1]@gi[2]
print("T191  M_4(C) with Dirac gammas: does D couple the blocks?")
print(f"   CONTROL gamma_5 anticommutes with each spatial gamma: "
      f"{max(np.abs(g5@x+x@g5).max() for x in gi):.1e}")
print(f"   CONTROL gamma_5^2 = I: {np.abs(g5@g5-np.eye(4)).max():.1e}")
R8=[tuple(r) for r in itertools.product([0,1],repeat=3)]; I8={r:i for i,r in enumerate(R8)}
def shift3(a,sg,p):
    M=np.zeros((8,8),dtype=complex)
    for r in R8:
        t=list(r)
        if sg>0:
            if r[a]==0: t[a]=1; ph=1.0
            else: t[a]=0; ph=np.exp(1j*p[a])
        else:
            if r[a]==1: t[a]=0; ph=1.0
            else: t[a]=1; ph=np.exp(-1j*p[a])
        M[I8[tuple(t)],I8[r]]+=ph
    return M
def Db(p): return sum(np.kron(shift3(a,1,p)-shift3(a,-1,p),gi[a]) for a in range(3))/2.0
G5=np.kron(np.eye(8),g5)
rng=np.random.default_rng(6)
ps=[rng.uniform(-np.pi,np.pi,size=3) for _ in range(20)]
print()
print("(1) does gamma_5 anticommute with D(p)?")
print(f"    max |{{G5, D(p)}}| over 20 momenta = "
      f"{max(np.abs(G5@Db(p)+Db(p)@G5).max() for p in ps):.2e}   (0 = chirality works)")
print()
N=32
G=[]
for mu in range(3):
    e=np.zeros(3); e[mu]=1e-5; G.append((Db(e)-Db(-e))/2e-5)
A=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in G])
U,sv,Vt=np.linalg.svd(A,full_matrices=False)
k=int(np.sum(sv<=max(A.shape)*np.finfo(float).eps*sv.max()))
B=[Vt[len(Vt)-k+i].conj().reshape(N,N) for i in range(k)]
C=np.vstack([np.array([(Bi@Bj-Bj@Bi).ravel() for Bi in B]).T for Bj in B])
U2,s2,V2=np.linalg.svd(C,full_matrices=False)
kc=int(np.sum(s2<=max(C.shape)*np.finfo(float).eps*s2.max()))
print(f"(2) continuum taste algebra dim = {k},  centre dim = {kc}")
cen=[sum(V2[len(V2)-kc+i].conj()[j]*B[j] for j in range(len(B))) for i in range(kc)]
Zc=None
for Zt in cen:
    H=0.5*(Zt+Zt.conj().T); H=H-np.trace(H).real/N*np.eye(N)
    if np.abs(H).max()>1e-8: Zc=H/np.abs(np.linalg.eigvalsh(H)).max(); break
print()
if Zc is None:
    print("(3) the centre is TRIVIAL (scalars only) -> ONE BLOCK, nothing to decouple")
    print("    -> R120's obstruction DISSOLVES: there is no block split to bridge.")
else:
    w=np.linalg.eigvalsh(Zc); u,c=np.unique(np.round(w,7),return_counts=True)
    print(f"(3) central element eigenvalues {np.round(u,4)} multiplicities {list(c)}")
    i0=np.where(np.abs(w-u[0])<1e-5)[0]; i1=np.where(np.abs(w-u[-1])<1e-5)[0]
    V=np.linalg.eigh(Zc)[1]
    P0=V[:,i0]@V[:,i0].conj().T; P1=V[:,i1]@V[:,i1].conj().T
    print(f"    does D connect the blocks?  max |P0 D P1| = "
          f"{max(np.abs(P0@g@P1).max() for g in G):.3e}")
    print(f"    (nonzero = the blocks COUPLE and R120's obstruction dissolves)")
