"""T44 - THE d-DIMENSIONAL CELL COMPLEX: cells carry volume, faces carry area
AND DIRECTION.  Lifting Result 23 out of one dimension.

DERIVATION (this is the construction, not a guess).  The divergence theorem on
one cell says   int_cell d_mu psi dV = closed-int_(boundary) psi n_mu dS.
Discretise the face value as the average of the two cells it separates:

   (Gamma . d psi)_c = (1/V_c) sum_f S_f (n_f . Gamma) * (1/2)(psi_c + psi_nbr)
                     = (1/V_c) * (1/2) * sum_f S_f (n_f . Gamma) psi_nbr

because sum_f S_f n_f = 0 for any closed cell, which kills the psi_c term
exactly.  So

   *** faces compare, with their area and their normal direction;
       cells weigh, with their volume. ***

Skew-adjointness w.r.t.  <phi,psi> = sum_c V_c phi_c psi_c  is immediate: the two
cells sharing a face see opposite outward normals and the same area, and
(n.Gamma) is a symmetric fibre matrix.  No calculation needed, exactly as in 1D.

THE GATE.  Chop a FLAT periodic rectangle two ways: the uniform grid, and the
image of that grid under a genuine 2D periodic DIFFEOMORPHISM (curvilinear cells,
non-product, faces not axis-aligned).  Same flat space, radically different
complex.  The spectrum must agree -- and must equal the continuum answer that
Result 16's master identity predicts,  lambda = m +- i sqrt(k1^2 + k2^2)."""
import numpy as np, itertools, time
NF=4
BAS=[(),(0,),(1,),(0,1)]; IDX={b:i for i,b in enumerate(BAS)}
def epsm(a):
    M=np.zeros((NF,NF))
    for Sx in BAS:
        if a in Sx: continue
        T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]]=(-1)**sum(1 for i in Sx if i<a)
    return M
def iotam(a):
    M=np.zeros((NF,NF))
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            if i!=a: continue
            T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]]+=(-1)**pos
    return M
GAM=[epsm(a)+iotam(a) for a in range(2)]           # flat gammas, {g_a,g_b}=2 delta
assert np.allclose(GAM[0]@GAM[0], np.eye(NF)) and np.allclose(GAM[0]@GAM[1]+GAM[1]@GAM[0], 0)
T1=T2=2*np.pi
def Phi(u,v,amp):
    """periodic diffeomorphism of the flat torus; amp=0 is the identity"""
    a,b=amp*0.35,amp*0.28
    return (u + a*np.sin(2*np.pi*v/T2) + 0.15*amp*np.sin(4*np.pi*u/T1),
            v + b*np.sin(2*np.pi*u/T1))
def build(L1,L2,m,amp):
    us=np.arange(L1+1)*T1/L1; vs=np.arange(L2+1)*T2/L2
    P=np.zeros((L1+1,L2+1,2))
    for i,u in enumerate(us):
        for j,v in enumerate(vs):
            X,Y=Phi(u,v,amp); P[i,j]=(X,Y)
    def corner(i,j):
        # unwrap: add the winding of the periodic images so cells stay convex
        return np.array([P[i%(L1+1) if i<=L1 else 0,j%(L2+1) if j<=L2 else 0]])
    NC=L1*L2; cid=lambda x,y:(x%L1)*L2+(y%L2)
    V=np.zeros(NC)
    Sx=np.zeros((L1,L2)); Nx=np.zeros((L1,L2,2))    # face between (x,y),(x+1,y)
    Sy=np.zeros((L1,L2)); Ny=np.zeros((L1,L2,2))    # face between (x,y),(x,y+1)
    for x in range(L1):
        for y in range(L2):
            c=[P[x,y],P[x+1,y],P[x+1,y+1],P[x,y+1]]
            # shoelace (corners are ordered, and Phi keeps them so for small amp)
            A=0.0
            for k in range(4):
                p,q=c[k],c[(k+1)%4]; A+=p[0]*q[1]-q[0]*p[1]
            V[cid(x,y)]=abs(A)/2.0
            e=P[x+1,y+1]-P[x+1,y]; Sx[x,y]=np.linalg.norm(e)
            n=np.array([e[1],-e[0]]); Nx[x,y]=n/np.linalg.norm(n)
            e2=P[x+1,y+1]-P[x,y+1]; Sy[x,y]=np.linalg.norm(e2)
            n2=np.array([-e2[1],e2[0]]); Ny[x,y]=n2/np.linalg.norm(n2)
    Q=np.zeros((NC*NF,NC*NF))
    for x in range(L1):
        for y in range(L2):
            c=cid(x,y); i=c*NF
            Q[i:i+NF,i:i+NF]+=m*np.eye(NF)
            for (S,N,dx,dy,sgn) in ((Sx[x,y],Nx[x,y],1,0,+1),(Sx[(x-1)%L1,y],Nx[(x-1)%L1,y],-1,0,-1),
                                    (Sy[x,y],Ny[x,y],0,1,+1),(Sy[x,(y-1)%L2],Ny[x,(y-1)%L2],0,-1,-1)):
                nb=cid(x+dx,y+dy); j=nb*NF
                nG=sgn*(N[0]*GAM[0]+N[1]*GAM[1])
                Q[i:i+NF,j:j+NF]+=0.5*(S/V[c])*nG
    return Q,V
def energies(L,m,amp,k=8):
    Q,V=build(L,L,m,amp)
    ev=np.linalg.eigvals(Q)
    return np.sort(np.abs(ev.imag))[:2*k], np.sort(ev.real)
print("T44  d=2 cell complex on a flat 2pi x 2pi torus, m = 0.8")
print("     continuum (Result 16): |Im lambda| = sqrt(k1^2+k2^2), k_i integers")
print("     -> 0, 1,1,1,1, sqrt2 x4, 2,2,2,2, ...")
print()
m=0.8
for amp in (0.0, 0.5, 1.0):
    tag = "UNIFORM grid" if amp==0 else f"CURVILINEAR complex (diffeo amp={amp})"
    print(f"  {tag}")
    for L in (8,12,16,20):
        t0=time.time(); e,re=energies(L,m,amp)
        def distinct(v):
            out=[]
            for z in v:
                if not out or abs(z-out[-1])>1e-4: out.append(z)
            return out[:5]
        d=distinct(e)
        pred=[0.0,1.0,np.sqrt(2),2.0,np.sqrt(5)]
        err=max(abs(a-b) for a,b in zip(d,pred[:len(d)]))
        print(f"    L={L:3d}  |Im| = {[f'{z:.6f}' for z in d]}   Re in [{re[0]:.5f},{re[-1]:.5f}]"
          f"   max|err| = {err:.3e}   [{time.time()-t0:.0f}s]", flush=True)
    print(flush=True)
