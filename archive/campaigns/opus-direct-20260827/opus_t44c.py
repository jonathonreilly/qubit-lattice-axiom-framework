"""T44c - the d=2 refinement gate, measured correctly, with the geometry checked.
T44b's error metric compared against the CONTINUUM, which at these L is dominated
by ordinary lattice dispersion (the uniform grid reproduces L sin(2 pi n/L)/T
exactly: 8 sin(pi/4)/2pi = 0.90032, measured 0.90032).  That is a property of the
symmetric difference, not of the chopping.  The gate is CURVILINEAR vs UNIFORM at
the SAME L -- same flat space, radically different complex.

Independent verifications of the construction, all of which must hold exactly:
  (G1) sum_f S_f n_f = 0 for every cell.  This is the closure identity that made
       the psi_c term drop out of the derivation; if it fails the operator has a
       spurious on-site term.
  (G2) sum_c V_c = the total area -- the cells actually tile the region.
  (G3) V K + K^T V = 0 exactly: skew-adjointness in the volume-weighted inner
       product, which is the structural property the whole construction rests on.
  (G4) the uniform case reproduces the exact lattice dispersion."""
import numpy as np, time
NF=4; BAS=[(),(0,),(1,),(0,1)]; IDX={b:i for i,b in enumerate(BAS)}
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
GAM=[epsm(a)+iotam(a) for a in range(2)]
T1=T2=2*np.pi
def Phi(u,v,amp):
    a,b=amp*0.35,amp*0.28
    return (u + a*np.sin(2*np.pi*v/T2) + 0.15*amp*np.sin(4*np.pi*u/T1),
            v + b*np.sin(2*np.pi*u/T1))
def build(L,m,amp):
    P=np.zeros((L+1,L+1,2))
    for i in range(L+1):
        for j in range(L+1):
            X,Y=Phi(i*T1/L, j*T2/L, amp); P[i,j]=(X,Y)
    NC=L*L; cid=lambda x,y:(x%L)*L+(y%L)
    V=np.zeros(NC); Sx=np.zeros((L,L)); Nx=np.zeros((L,L,2))
    Sy=np.zeros((L,L)); Ny=np.zeros((L,L,2)); closure=0.0
    for x in range(L):
        for y in range(L):
            c=[P[x,y],P[x+1,y],P[x+1,y+1],P[x,y+1]]
            A=sum(c[k][0]*c[(k+1)%4][1]-c[(k+1)%4][0]*c[k][1] for k in range(4))
            V[cid(x,y)]=abs(A)/2.0
            e=P[x+1,y+1]-P[x+1,y]; Sx[x,y]=np.linalg.norm(e)
            n=np.array([e[1],-e[0]]); Nx[x,y]=n/np.linalg.norm(n)
            e2=P[x+1,y+1]-P[x,y+1]; Sy[x,y]=np.linalg.norm(e2)
            n2=np.array([-e2[1],e2[0]]); Ny[x,y]=n2/np.linalg.norm(n2)
    for x in range(L):                                   # (G1) closure per cell
        for y in range(L):
            s=(Sx[x,y]*Nx[x,y] - Sx[(x-1)%L,y]*Nx[(x-1)%L,y]
               + Sy[x,y]*Ny[x,y] - Sy[x,(y-1)%L]*Ny[x,(y-1)%L])
            closure=max(closure,float(np.linalg.norm(s)))
    K=np.zeros((NC*NF,NC*NF))
    for x in range(L):
        for y in range(L):
            c=cid(x,y); i=c*NF
            for (S,N,dx,dy,sg) in ((Sx[x,y],Nx[x,y],1,0,+1),(Sx[(x-1)%L,y],Nx[(x-1)%L,y],-1,0,-1),
                                   (Sy[x,y],Ny[x,y],0,1,+1),(Sy[x,(y-1)%L],Ny[x,(y-1)%L],0,-1,-1)):
                j=cid(x+dx,y+dy)*NF
                K[i:i+NF,j:j+NF]+=0.5*(S/V[c])*sg*(N[0]*GAM[0]+N[1]*GAM[1])
    return K,V,closure
def spec(L,m,amp,n=160):
    K,V,cl=build(L,m,amp)
    Vd=np.repeat(V,NF)
    skew=float(np.max(np.abs(Vd[:,None]*K + (Vd[:,None]*K).T)))       # (G3)
    ev=np.linalg.eigvals(m*np.eye(K.shape[0])+K)
    return np.sort(np.abs(ev.imag))[:n], cl, abs(V.sum()-T1*T2), skew
m=0.8
print("T44c  d=2 cell complex, flat 2pi x 2pi torus, m=0.8")
print("  geometry + structure checks (must be ~0):")
for L in (8,16,24):
    for amp in (0.0,1.0):
        _,cl,dv,sk=spec(L,m,amp,n=4)
        print(f"    L={L:2d} amp={amp}:  (G1) max|sum S_f n_f| = {cl:.2e}   "
              f"(G2) |sum V - area| = {dv:.2e}   (G3) max|VK + (VK)^T| = {sk:.2e}", flush=True)
print()
print("  THE GATE: curvilinear vs uniform at the same L, lowest 160 |Im| values")
print(f"   {'L':>4} {'amp=0.5 max gap':>18} {'ratio':>8} {'amp=1.0 max gap':>18} {'ratio':>8}")
prev={0.5:None,1.0:None}
for L in (8,12,16,20,24,28):
    base,_,_,_=spec(L,m,0.0); row=f"   {L:4d}"
    for amp in (0.5,1.0):
        e,_,_,_=spec(L,m,amp)
        g=float(np.max(np.abs(e-base)))
        r=prev[amp]/g if prev[amp] else float('nan')
        row+=f"{g:18.5e}{r:8.2f}" if prev[amp] else f"{g:18.5e}{'--':>8}"
        prev[amp]=g
    print(row, flush=True)
print()
print("  ratio ~4 per L-doubling-equivalent = O(1/L^2); the L steps here are")
print("  x1.5, x1.33, x1.25, x1.2, x1.17 so the expected ratios are 2.25, 1.78,")
print("  1.56, 1.44, 1.36 for second order.")
