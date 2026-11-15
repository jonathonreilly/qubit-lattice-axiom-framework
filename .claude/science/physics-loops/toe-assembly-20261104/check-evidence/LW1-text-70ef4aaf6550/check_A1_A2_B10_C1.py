# Independent check of A1, A2, B10(1-3), C1 on a periodic torus and on Bloch fibres.
# Written from the definitions in LW1.md section 1, not from the proofs.
import numpy as np, itertools, sys
np.set_printoptions(linewidth=200)
L=6
sites=list(itertools.product(range(L),repeat=3)); idx={s:i for i,s in enumerate(sites)}; n=len(sites)
E=np.eye(3,dtype=int)
def eta(i,x): return (-1)**(sum(x[:i])%2)
def add(x,v): return tuple((np.array(x)+v)%L)
def Rmat(o):
    R=np.zeros((n,n))
    for x in sites:
        for i in range(3):
            if x[i]%2==o:   # edge (x,x+e_i) lies in a cube of tiling with offset o
                y=add(x,E[i]); R[idx[y],idx[x]]+=eta(i,x)/np.sqrt(3); R[idx[x],idx[y]]+=eta(i,x)/np.sqrt(3)
    return R
Re,Ro=Rmat(0),Rmat(1)
# ownership: check the edge really lies in one cube b+{0,1}^3 (b even / b odd) directly
bad=0
for x in sites:
    for i in range(3):
        y=np.array(x)+E[i]
        own=[]
        for o in (0,1):
            b=[(c-o)//2*2+o for c in x]   # base of the tiling cube containing x
            own.append(all(b[j]<=y[j]<=b[j]+1 for j in range(3)))
        if sum(own)!=1 or own[x[i]%2]!=True: bad+=1
print("A1 ownership violations:",bad)
# faces
fb=0
for x in sites:
    for i in range(3):
        for j in range(i+1,3):
            p=eta(i,x)*eta(j,add(x,E[i]))*eta(i,add(x,E[j]))*eta(j,x)
            if p!=-1: fb+=1
print("A1 faces with product != -1:",fb)
print("A1 |Re^2-I|,|Ro^2-I|:",abs(Re@Re-np.eye(n)).max(),abs(Ro@Ro-np.eye(n)).max())
# B10 anticommutator identity
T2=np.zeros((n,n))
for x in sites:
    for i in range(3):
        for s in (2,-2): T2[idx[add(x,s*E[i])],idx[x]]+=1/3
print("B10 |{Re,Ro}-(1/3)sum T_{+-2e_i}|:",abs(Re@Ro+Ro@Re-T2).max())
def V(eps,mu):
    ae,ao=eps-mu/2,eps+mu/2
    Ve=np.cos(ae)*np.eye(n)-1j*np.sin(ae)*Re; Vo=np.cos(ao)*np.eye(n)+1j*np.sin(ao)*Ro
    return Vo@Ve,Ve,Vo
for eps,mu in [(0.7,0.3),(1.3,0.0),(0.2,0.39),(1.5,2.9)]:
    Vm,Ve,Vo=V(eps,mu)
    ev=np.linalg.eigvals(Vm); w=np.abs(np.angle(ev))
    print(f"eps={eps} mu={mu}: unitary err {abs(Vm.conj().T@Vm-np.eye(n)).max():.1e}; min|w|={w.min():.6f} (mu={mu}) max|w|={w.max():.6f} (2eps={2*eps})",
          "n(+)=",int((np.angle(ev)>1e-9).sum()),"n(-)=",int((np.angle(ev)<-1e-9).sum()),"n(0)=",int((abs(np.angle(ev))<=1e-9).sum()))
    # compare whole spectrum with formula on torus momenta K=2*pi*m/(L/2)
    ab=(np.cos(mu)-np.cos(2*eps))/2; bb=(-np.cos(2*eps)-np.cos(mu))/2
    pred=[]
    for m in itertools.product(range(L//2),repeat=3):
        K=2*np.pi*np.array(m)/(L//2); chi=np.cos(K).sum()/3
        ww=np.arccos(np.clip(ab*chi-bb,-1,1)); pred+= [ww]*4+[-ww]*4
    print("   spectrum vs formula (sorted angle diff):",abs(np.sort(np.angle(ev))-np.sort(pred)).max())
    # Theta symmetry: D_s conj(V) D_s = V
    Ds=np.diag([(-1)**(sum(s)%2) for s in sites])
    print("   |Theta V Theta^-1 - V|:",abs(Ds@Vm.conj()@Ds-Vm).max())
    if mu>0:
        lam,U=np.linalg.eig(Vm)   # V normal
        # quasi-energy: eigenvalue e^{-iw}; P = modes with w in (-pi,0) i.e. angle(lam) in (0,pi)
        sel=np.angle(lam)>0
        Q,_=np.linalg.qr(U[:,sel]); P=Q@Q.conj().T
        print("   P_xx range:",P.diagonal().real.min(),P.diagonal().real.max()," |Theta P Theta^-1-(I-P)|:",abs(Ds@P.conj()@Ds-(np.eye(n)-P)).max()," |[P,V]|:",abs(P@Vm-Vm@P).max())
# A2: classify all orientation-preserving isometries mod even translations
def signed_perms():
    out=[]
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1,-1),repeat=3):
            Q=np.zeros((3,3),dtype=int)
            for r in range(3): Q[r,p[r]]=sg[r]
            if round(np.linalg.det(Q))==1: out.append(Q)
    return out
O=signed_perms(); print("A2 |O|=",len(O))
eps,mu=0.7,0.3
Vm,Ve,Vo=V(eps,mu)
c0=np.array([.5,.5,.5])
def perm_matrix(Q,t):
    Pm=np.zeros((n,n)); img=[]
    for x in sites:
        y=Q@(np.array(x)-c0)+c0+np.array(t); y=tuple(int(round(v))%L for v in y)
        Pm[idx[y],idx[x]]=1; img.append(y)
    return Pm
def gauge_fix(M_t, M):  # find sign diag d with D M_t D = M (real symmetric hop matrices), by BFS; return None if impossible
    d=np.zeros(n); d[0]=1; stack=[0]
    while stack:
        a=stack.pop()
        for b in np.nonzero(abs(M[a])>1e-12)[0]:
            if abs(abs(M_t[a,b])-abs(M[a,b]))>1e-12: return None
            r=np.sign(M[a,b]/M_t[a,b])*d[a]
            if d[b]==0: d[b]=r; stack.append(b)
            elif d[b]!=r: return None
    if (d==0).any(): return None
    return d
nsym=0; nexcl=0; fail=0
for Q in O:
    for t in itertools.product((0,1),repeat=3):
        Pm=perm_matrix(Q,t)
        Vt=Pm@Vm@Pm.T
        modeq=abs(abs(Vt)-abs(Vm)).max()<1e-10
        if not any(t):
            Rs=Pm@(Re+Ro)@Pm.T
            d=gauge_fix(Rs,Re+Ro)
            ok = d is not None and abs(np.diag(d)@Pm@Re@Pm.T@np.diag(d)-Re).max()<1e-12 and abs(np.diag(d)@Pm@Ro@Pm.T@np.diag(d)-Ro).max()<1e-12
            ok = ok and abs(np.diag(d)@Vt@np.diag(d)-Vm).max()<1e-12
            if ok: nsym+=1
            else: fail+=1
        else:
            if modeq: fail+=1   # an odd translation class with matching moduli would contradict exclusion proof (necessary condition)
            else: nexcl+=1
print("A2: rotations about c0 (t=0) that are symmetries with a common sign gauge for BOTH half ticks:",nsym,"/24; odd-translation classes excluded by moduli:",nexcl,"/168; anomalies:",fail)
# stabilizer of site 0 in G and orbit
stab=0; orbit=set()
for Q in O:
    y=Q@(np.zeros(3)-c0)+c0
    orbit.add(tuple(int(round(v))%2 for v in y))
    # need an even translation t with y+t=0  <=> y even vector
    if all(int(round(v))%2==0 for v in y): stab+=1
print("A2 stabilizer of site 0 in G:",stab," residues reached from 0 by O_{c0}:",len(orbit))
# mu=0 half-step exchange: translation by 1 + D_s + sign gauge
for mu0 in (0.0,0.3):
    Vm,Ve,Vo=V(0.7,mu0)
    Pm=perm_matrix(np.eye(3,dtype=int),(1,1,1)); Ds=np.diag([(-1.0)**(sum(s)%2) for s in sites])
    d=gauge_fix(Pm@(Re+Ro)@Pm.T,Re+Ro); D=np.diag(d)
    S=Ds@D@Pm
    print(f"A2 mu={mu0}: |S Ve S^-1 - Vo|={abs(S@Ve@S.T-Vo).max():.2e}, |S Vo S^-1 - Ve|={abs(S@Vo@S.T-Ve).max():.2e}")
# ---- Bloch fibre (cell momentum K), residues r in {0,1}^3
res=list(itertools.product((0,1),repeat=3)); ridx={r:i for i,r in enumerate(res)}
def fibre(K,o):
    R=np.zeros((8,8),dtype=complex)
    for r in res:
        for i in range(3):
            if r[i]%2==o:
                y=np.array(r)+E[i]; cell=y//2; rr=tuple(y%2)
                ph=np.exp(-1j*np.dot(K,cell))   # convention: psi(2b+r)=e^{iK.b}u_r
                R[ridx[rr],ridx[r]]+=eta(i,r)*ph/np.sqrt(3); R[ridx[r],ridx[rr]]+=eta(i,r)*np.conj(ph)/np.sqrt(3)
    return R
def Vk(K,eps,mu):
    ae,ao=eps-mu/2,eps+mu/2
    Re_,Ro_=fibre(K,0),fibre(K,1)
    return (np.cos(ao)*np.eye(8)+1j*np.sin(ao)*Ro_)@(np.cos(ae)*np.eye(8)-1j*np.sin(ae)*Re_)
rng=np.random.default_rng(1); worst=0; mult_bad=0
for _ in range(2000):
    eps=rng.uniform(0.01,np.pi/2-0.01); mu=rng.uniform(0,2*eps) if rng.random()<0.8 else 0.0
    K=rng.uniform(-np.pi,np.pi,3)
    ev=np.linalg.eigvals(Vk(K,eps,mu)); ang=np.angle(ev)
    chi=np.cos(K).sum()/3; ab=(np.cos(mu)-np.cos(2*eps))/2; bb=(-np.cos(2*eps)-np.cos(mu))/2
    w=np.arccos(ab*chi-bb)
    worst=max(worst,abs(np.sort(ang)-np.sort([w]*4+[-w]*4)).max())
    if not (mu-1e-9<=w<=2*eps+1e-9): mult_bad+=1
print("B10(1) fibre spectrum vs formula, 2000 random (eps,mu,K): max err",worst," interval violations",mult_bad)
print("B10 trace of fibre hops at random K:",abs(np.trace(fibre(K,0))),abs(np.trace(fibre(K,1))))
# C1: compare numerical w from fibre with the stated expansion
import mpmath as mp
for eps in (0.3,1.1,1.55):
    s=np.sin(eps)
    for nh in ([1,0,0],[1,1,1],[1,2,-0.5],[0.3,-0.7,0.2]):
        nh=np.array(nh,float); nh/=np.linalg.norm(nh); T4=(nh**4).sum()
        errs=[]
        for k in (0.2,0.1,0.05):
            ev=np.linalg.eigvals(Vk(k*nh,eps,0.0)); w=np.abs(np.angle(ev)).mean()
            pred=s*k/np.sqrt(3)*(1+k*k*(s*s/72-T4/24))
            errs.append(abs(w-pred)/ (s*k/np.sqrt(3)))
        # relative error should scale as k^4: ratios ~16
        print(f"C1 eps={eps} T4={T4:.4f} rel.err at k=.2,.1,.05: {errs[0]:.3e} {errs[1]:.3e} {errs[2]:.3e} ratios {errs[0]/errs[1]:.1f} {errs[1]/errs[2]:.1f}")
        # control: perturb coefficient T4/24 -> T4/23 ; should give ratio ~4 not 16
    k1,k2=0.1,0.05
    def e(k,c):
        ev=np.linalg.eigvals(Vk(k*nh,eps,0.0)); w=np.abs(np.angle(ev)).mean()
        return abs(w-s*k/np.sqrt(3)*(1+k*k*(s*s/72-T4/c)))/(s*k/np.sqrt(3))
    print("   control (T4/23 instead of T4/24) ratio:",round(e(k1,23)/e(k2,23),2)," (s^2/70 instead of /72 not shown)")
import sympy as sp
k,s,T=sp.symbols('k s T',positive=True)
# independent series: w = arccos(1 - s^2(1-chi)), 1-chi expanded with T4 = T, and T2=1
n1,n2,n3=sp.symbols('n1 n2 n3',real=True)
chi=(sp.cos(k*n1)+sp.cos(k*n2)+sp.cos(k*n3))/3
ser=sp.series(1-chi,k,0,8).removeO()
ser=sp.expand(ser)
ser4=ser.coeff(k,2)*k**2+ser.coeff(k,4)*k**4
ser4=ser4.subs(n1**2,1-n2**2-n3**2) # not full reduction; do numerically below instead
x=sp.symbols('x',positive=True)
om=sp.series(sp.acos(1-s**2*(x**2/6-x**4*T/72)),x,0,5).removeO()
print("C1 sympy series of w in k:",sp.simplify(sp.expand(om)))
print("   stated:",sp.expand(s*x/sp.sqrt(3)*(1+x**2*(s**2/72-T/24))))
print("   difference:",sp.simplify(sp.expand(om)-sp.expand(s*x/sp.sqrt(3)*(1+x**2*(s**2/72-T/24)))))
