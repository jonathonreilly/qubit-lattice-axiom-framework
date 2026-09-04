"""T137 - THE CORRECT PROBE: does curvature split the framework's OWN taste degeneracy?

R80 withdrew R79: the DEC cochain complex is not the framework's object.  The
framework puts the WHOLE exterior algebra at EACH SITE (Gamma_a = eps_a + iota_a,
a 2^d-component field per vertex, with hopping), whereas DEC distributes it across
cells of different dimension.  R16's exact 2^{d-1}-fold degeneracy is a statement
about the first.  Build that.

Operator, reducing to R16 on flat space:
   (D psi)_x = m psi_x + sum_a [ Gam_a(x,+) psi_{x+a} - Gam_a(x,-) psi_{x-a} ] / 2
with Gam_a(x,+-) = (Gamma_a(x) + Gamma_a(x +- a))/2 symmetrised for hermiticity,
Gamma_a(x) = eps_a + iota_a(g^{-1}(x)), and the volume weight V = sqrt(det g)
entering as the inner product sum_x V psi^dag psi, so the hermitian object is
V^{-1/2}(...)V^{-1/2}.  On flat space Fourier gives Q(q) = m + i sum_a Gamma_a
sin(q_a), which is exactly R16's Q.

d=2, fibre dim 4, taste count 2^{d/2} = 2, so R16 predicts every level of iD is
EXACTLY 2-fold degenerate on flat space.

THE TEST HAS TEETH THIS TIME, and here is what would make it fail:
   the flat case MUST come out 2-fold (validates the construction), AND
   the degeneracy must be capable of breaking -- so I also run a CONTROL that
   deliberately breaks the Clifford relation ({Gamma_a,Gamma_b} != 2 g^{-1}) and
   confirm the degeneracy is destroyed there.  Without that control this is
   another R79."""
import numpy as np, itertools
d=2
BAS=[]
for k in range(d+1): BAS+=[tuple(c) for c in itertools.combinations(range(d),k)]
IDX={b:i for i,b in enumerate(BAS)}; NF=len(BAS)
def epsm(a):
    M=np.zeros((NF,NF))
    for S in BAS:
        if a in S: continue
        T=tuple(sorted(S+(a,))); M[IDX[T],IDX[S]]=(-1)**sum(1 for i in S if i<a)
    return M
def iotam(a,gi):
    M=np.zeros((NF,NF))
    for S in BAS:
        for pos,i in enumerate(S):
            T=tuple(x for x in S if x!=i); M[IDX[T],IDX[S]]+=(-1)**pos*gi[a,i]
    return M
EPS=[epsm(a) for a in range(d)]
def Gam(gi):  return [EPS[a]+iotam(a,gi) for a in range(d)]

def build(L,gfun,m=0.0,break_clifford=0.0):
    N=L*L; sid={}
    for i,x in enumerate(itertools.product(range(L),repeat=d)): sid[x]=i
    gi={}; V=np.zeros(N)
    for x in sid:
        g=gfun(np.array(x,dtype=float)/L)
        gi[x]=np.linalg.inv(g); V[sid[x]]=np.sqrt(np.linalg.det(g))
    G={x:Gam(gi[x]) for x in sid}
    if break_clifford:                    # control: destroy {Gam,Gam} = 2 g^-1
        rng=np.random.default_rng(5)
        for x in sid:
            G[x]=[G[x][a]+break_clifford*rng.normal(size=(NF,NF)) for a in range(d)]
    D=np.zeros((N*NF,N*NF))
    def blk(i,j): return (slice(i*NF,(i+1)*NF), slice(j*NF,(j+1)*NF))
    for x in sid:
        i=sid[x]; D[blk(i,i)]+=m*np.eye(NF)
        for a in range(d):
            xp=list(x); xp[a]=(xp[a]+1)%L; xp=tuple(xp)
            xm=list(x); xm[a]=(xm[a]-1)%L; xm=tuple(xm)
            D[blk(i,sid[xp])]+= 0.5*0.5*(G[x][a]+G[xp][a])
            D[blk(i,sid[xm])]-= 0.5*0.5*(G[x][a]+G[xm][a])
    w=np.repeat(1.0/np.sqrt(V),NF)
    H=1j*(w[:,None]*D*w[None,:])
    return 0.5*(H+H.conj().T)

def report(nm,H):
    lam=np.linalg.eigvalsh(H); lam=np.sort(lam)
    pos=lam[lam>1e-9]
    d2=np.abs(pos[1::2]-pos[0::2])/np.maximum(pos[0::2],1e-12)
    print(f"   {nm:<38} pairs: max {d2.max():.3e}  median {np.median(d2):.3e}"
          f"   {'2-FOLD' if d2.max()<1e-8 else 'SPLIT'}")
    return lam

print("T137  the framework's site-based Kahler-Dirac operator, d=2, L=8 (fibre 4)")
print(f"      R16 predicts EXACT 2-fold degeneracy of every level on flat space.")
print()
flat=lambda x: np.eye(2)
def conf(amp):
    return lambda x: np.exp(2*amp*np.cos(2*np.pi*x[0]))*np.eye(2)
def aniso(amp):
    def g(x):
        f=amp*np.cos(2*np.pi*x[0])*np.sin(2*np.pi*x[1])
        return np.array([[1.0+f,0.4*f],[0.4*f,1.0-f]])
    return g
report("FLAT (validation -- must be 2-fold)", build(8,flat))
report("conformal, amp=0.10", build(8,conf(0.10)))
report("conformal, amp=0.30", build(8,conf(0.30)))
report("anisotropic curved, amp=0.15", build(8,aniso(0.15)))
report("anisotropic curved, amp=0.35", build(8,aniso(0.35)))
print()
print("   CONTROL -- deliberately break {Gamma_a,Gamma_b} = 2 g^{-1}.")
print("   If the degeneracy does NOT break here, the test has no teeth and is void.")
report("flat + Clifford broken by 0.02", build(8,flat,break_clifford=0.02))
report("flat + Clifford broken by 0.10", build(8,flat,break_clifford=0.10))
