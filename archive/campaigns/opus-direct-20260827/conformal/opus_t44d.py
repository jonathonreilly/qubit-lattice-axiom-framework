"""T44d - the d=2 gate with reordering-proof observables.
T44c's element-wise comparison of sorted spectra is legitimate but fragile at
coarse L: the curvilinear complex splits degeneracies differently, so the sorted
lists can pair the wrong modes and the metric goes non-monotone (it did, at
L=8->12).  Use observables that cannot care about ordering:
   E1  = the first nonzero energy level (mean of its multiplicity cluster)
   S64 = the sum of the lowest 64 energies  -- a smooth spectral functional
   HK  = the heat-kernel trace  sum_i exp(-|Im lambda_i|^2 / 4)  over the whole
         spectrum -- smooth, global, and dominated by the low modes
Each is compared between the curvilinear complex and the uniform one at the same
L.  All three must converge to zero, and the exact uniform value E1 =
L sin(2 pi/L) / T is known analytically, which pins the construction independently."""
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
def spec(L,m,amp):
    P=np.zeros((L+1,L+1,2))
    for i in range(L+1):
        for j in range(L+1):
            P[i,j]=Phi(i*T1/L, j*T2/L, amp)
    NC=L*L; cid=lambda x,y:(x%L)*L+(y%L)
    V=np.zeros(NC); Sx=np.zeros((L,L)); Nx=np.zeros((L,L,2)); Sy=np.zeros((L,L)); Ny=np.zeros((L,L,2))
    for x in range(L):
        for y in range(L):
            c=[P[x,y],P[x+1,y],P[x+1,y+1],P[x,y+1]]
            A=sum(c[k][0]*c[(k+1)%4][1]-c[(k+1)%4][0]*c[k][1] for k in range(4))
            V[cid(x,y)]=abs(A)/2.0
            e=P[x+1,y+1]-P[x+1,y]; Sx[x,y]=np.linalg.norm(e); n=np.array([e[1],-e[0]]); Nx[x,y]=n/np.linalg.norm(n)
            e2=P[x+1,y+1]-P[x,y+1]; Sy[x,y]=np.linalg.norm(e2); n2=np.array([-e2[1],e2[0]]); Ny[x,y]=n2/np.linalg.norm(n2)
    K=np.zeros((NC*NF,NC*NF))
    for x in range(L):
        for y in range(L):
            i=cid(x,y)*NF; vc=V[cid(x,y)]
            for (S,N,dx,dy,sg) in ((Sx[x,y],Nx[x,y],1,0,+1),(Sx[(x-1)%L,y],Nx[(x-1)%L,y],-1,0,-1),
                                   (Sy[x,y],Ny[x,y],0,1,+1),(Sy[x,(y-1)%L],Ny[x,(y-1)%L],0,-1,-1)):
                j=cid(x+dx,y+dy)*NF
                K[i:i+NF,j:j+NF]+=0.5*(S/vc)*sg*(N[0]*GAM[0]+N[1]*GAM[1])
    ev=np.linalg.eigvals(m*np.eye(NC*NF)+K)
    return np.sort(np.abs(ev.imag))
def obs(e):
    nz=e[e>1e-8]
    cl=[nz[0]]
    for z in nz[1:]:
        if z-cl[0]>0.06: break
        cl.append(z)
    return float(np.mean(cl)), float(np.sum(e[:64])), float(np.sum(np.exp(-e**2/4.0)))
m=0.8
print("T44d  d=2 cell complex, flat torus, m=0.8.  Curvilinear vs uniform, same L.")
print(f"   {'L':>4} {'E1(unif)':>10} {'exact':>10} | {'amp':>4} {'|dE1|':>11} {'r':>5} "
      f"{'|dS64|/S64':>11} {'r':>5} {'|dHK|/HK':>11} {'r':>5}")
prev={}
for L in (8,12,16,20,24,28,32):
    t0=time.time(); eu=spec(L,m,0.0); E1u,S64u,HKu=obs(eu)
    exact=L*np.sin(2*np.pi/L)/T1
    line=f"   {L:4d} {E1u:10.6f} {exact:10.6f} |"
    out=[]
    for amp in (0.5,1.0):
        e=spec(L,m,amp); E1,S64,HK=obs(e)
        d1=abs(E1-E1u); d2=abs(S64-S64u)/abs(S64u); d3=abs(HK-HKu)/abs(HKu)
        rs=[]
        for key,val in (("1",d1),("2",d2),("3",d3)):
            k=(amp,key); rs.append(prev[k]/val if k in prev and val>0 else float('nan')); prev[k]=val
        out.append(f" {amp:4.1f} {d1:11.4e} {rs[0]:5.2f} {d2:11.4e} {rs[1]:5.2f} {d3:11.4e} {rs[2]:5.2f}")
    print(line+out[0], flush=True)
    print(" "*33+"|"+out[1]+f"   [{time.time()-t0:.0f}s]", flush=True)
print()
print("   E1(unif) must equal L sin(2 pi/L)/T exactly -- that pins the operator.")
print("   Second-order convergence at these L steps (x1.5,1.33,1.25,1.2,1.17,1.14)")
print("   predicts ratios 2.25, 1.78, 1.56, 1.44, 1.36, 1.31.")
