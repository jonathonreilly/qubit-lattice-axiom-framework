# Independent check of MT1 Theorems 1,4,5,7,8, Cor 9.1, C3, C7(b,c,d) from the lattice definitions in LW1 section 1.
# Everything is built from R_e,R_o on an even torus; fibre matrices are obtained by Bloch projection, not from the text's formulas.
import numpy as np, itertools, sys
np.set_printoptions(linewidth=200, precision=4, suppress=True)
def torus(L):
    sites=list(itertools.product(range(L),repeat=3)); idx={s:i for i,s in enumerate(sites)}
    return sites,idx
def eta(i,x): return (-1)**(sum(x[:i]))
def hops(L):
    sites,idx=torus(L); n=len(sites)
    Re=np.zeros((n,n)); Ro=np.zeros((n,n)); edges=[]
    for x in sites:
        for i in range(3):
            y=list(x); y[i]=(y[i]+1)%L; y=tuple(y)
            s=eta(i,x)
            M = Re if x[i]%2==0 else Ro
            M[idx[y],idx[x]]+=s; M[idx[x],idx[y]]+=s
            edges.append((x,y,i,s))
    return sites,idx,Re/np.sqrt(3),Ro/np.sqrt(3),edges
def rotations():
    out=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            Q=np.zeros((3,3),int)
            for j in range(3): Q[p[j],j]=s[j]
            if round(np.linalg.det(Q))==1: out.append((Q,p,s))
    return out
def gmap(Q,x,L):
    v=Q@(2*np.array(x)-1)  # 2(x-c0)
    return tuple(((v+1)//2)%L)
def find_lift(Q,L,sites,idx,Re,Ro,improper=False):
    # solve for site signs d: P D commutes with Re and Ro. BFS over edges of Re+Ro
    n=len(sites); P=np.zeros((n,n))
    for x in sites: P[idx[gmap(Q,x,L)],idx[x]]=1
    Ae=P.T@Re@P; Ao=P.T@Ro@P   # need D Ae' ... : (P D) R (P D)^-1 = R  <=> D (P^T R P) D = R... careful
    # (PD) R (PD)^T = R  <=> D R D = P^T R P
    d=np.zeros(n); d[0]=1; stack=[0]; M=Re+2*Ro; T=P.T@M@P
    while stack:
        a=stack.pop()
        for b in np.nonzero(M[a])[0]:
            if abs(T[a,b])<1e-12: return None
            r=T[a,b]/M[a,b]
            if d[b]==0: d[b]=d[a]*r; stack.append(b)
    D=np.diag(d); rho=P@D
    ok=np.allclose(rho@Re@rho.T,Re) and np.allclose(rho@Ro@rho.T,Ro)
    return rho if ok else None
def bloch(L,sites,idx,K):
    # columns |K,r> = sum_b e^{iK.b}|2b+r>, normalised
    nb=(L//2)**3; B=np.zeros((len(sites),8),complex)
    for x in sites:
        b=[c//2 for c in x]; r=[c%2 for c in x]
        B[idx[x], r[0]*4+r[1]*2+r[2]]=np.exp(1j*np.dot(K,b))/np.sqrt(nb)
    return B
def cellmats():
    rs=list(itertools.product([0,1],repeat=3)); ri={r:i for i,r in enumerate(rs)}
    A=[];Z=[]
    for j in range(3):
        a=np.zeros((8,8)); z=np.zeros((8,8))
        for r in rs:
            z[ri[r],ri[r]]=(-1)**r[j]
            if r[j]==0:
                r2=list(r); r2[j]=1; r2=tuple(r2); s=(-1)**sum(r[:j])
                a[ri[r2],ri[r]]=s; a[ri[r],ri[r2]]=s
        A.append(a); Z.append(z)
    G=[1j*Z[j]@A[j] for j in range(3)]
    return A,Z,G
def acomm(a,b): return a@b+b@a
def prop(a,b):
    # is a = c*b with |c|=1 ?
    k=np.argmax(abs(b)); c=a.flat[k]/b.flat[k]
    return np.allclose(a,c*b) and abs(abs(c)-1)<1e-9, c
A,Z,G=cellmats(); I8=np.eye(8)
ok=True
def chk(name,cond):
    global ok; ok=ok and bool(cond); print(('PASS ' if cond else 'FAIL ')+name)
# ---- Theorem 4: Clifford relations, monomial basis
gens=A+G
chk('T4 six generators Hermitian involutions, pairwise anticommuting', all(np.allclose(g,g.conj().T) and np.allclose(g@g,I8) for g in gens) and all(np.allclose(acomm(gens[i],gens[j]),0) for i in range(6) for j in range(i)))
mons=[]
for bits in itertools.product([0,1],repeat=6):
    m=I8.astype(complex)
    for g,b in zip(gens,bits):
        if b: m=m@g
    mons.append(m.reshape(-1))
Gram=np.array(mons).conj()@np.array(mons).T
chk('T4 64 monomials orthogonal basis of M_8', np.allclose(Gram,8*np.eye(64)))
chi=-1j*G[0]@G[1]@G[2]
for L in (2,4,6):
    sites,idx,Re,Ro,edges=hops(L)
    chk(f'L={L}: R_e^2=R_o^2=1 (LW1 A1 given)', np.allclose(Re@Re,np.eye(len(sites))) and np.allclose(Ro@Ro,np.eye(len(sites))))
    Ks=[2*np.pi*np.array(k)/(L//2) for k in itertools.product(range(L//2),repeat=3)]
    good=True
    for K in Ks:
        B=bloch(L,sites,idx,K)
        ReK=B.conj().T@Re@B; RoK=B.conj().T@Ro@B
        good&=np.allclose(ReK,sum(A)/np.sqrt(3))
        good&=np.allclose(RoK,sum(np.cos(K[j])*A[j]-np.sin(K[j])*G[j] for j in range(3))/np.sqrt(3))
        # control: wrong sign of sin term must fail when sin K != 0
    chk(f'L={L}: T4 fibre formulas R_e(K), R_o(K) at all {len(Ks)} momenta', good)
    if L==6:
        K=Ks[5]; B=bloch(L,sites,idx,K); RoK=B.conj().T@Ro@B
        bad=np.allclose(RoK,sum(np.cos(K[j])*A[j]+np.sin(K[j])*G[j] for j in range(3))/np.sqrt(3))
        chk('L=6 control: R_o(K) with +sin K Gamma is rejected', not bad)
    rots=rotations(); lifts={}
    allp=True; cov=True; rules=True; uniq=True
    for Q,p,s in rots:
        rho=find_lift(Q,L,sites,idx,Re,Ro)
        if rho is None: allp=False; continue
        lifts[(p,s)]=rho
        # cell periodic sign: compare sign at x and x+2e_k
        d={x: rho[idx[gmap(Q,x,L)],idx[x]] for x in sites}
        for x in sites:
            for k in range(3):
                y=list(x); y[k]=(y[k]+2)%L
                if d[tuple(y)]!=d[x]: allp=False
        # uniqueness: commutant of R_e,R_o among diagonal matrices is constants
        # (diagonal Dg commuting with Re and Ro) -> nullspace dimension
        # fibre covariance
        for K in Ks:
            B=bloch(L,sites,idx,K); QK=Q@K; B2=bloch(L,sites,idx,QK)
            rh=B2.conj().T@rho@B
            if not np.allclose(rh@rh.conj().T,I8): cov=False
            for R in (Re,Ro):
                if not np.allclose(rh@(B.conj().T@R@B)@rh.conj().T, B2.conj().T@R@B2): cov=False
        B0=bloch(L,sites,idx,np.zeros(3)); rh=B0.conj().T@rho@B0
        lifts[(p,s,'hat')]=rh
        for j in range(3):
            if not np.allclose(rh@A[j]@rh.conj().T,A[p[j]]): rules=False
            if not np.allclose(rh@G[j]@rh.conj().T,s[j]*G[p[j]]): rules=False
    chk(f'L={L}: T1 all 24 sign lifts exist, cell-periodic', allp and len([k for k in lifts if len(k)==2])==24)
    chk(f'L={L}: T1 fibre covariance rho R_T(K) rho* = R_T(QK), rho-hat K-independent unitary', cov)
    chk(f'L={L}: T4 rotation rules A_j->A_pi(j), Gamma_j->s_j Gamma_pi(j)', rules)
    # uniqueness: diagonal matrices commuting with Re,Ro
    n=len(sites); rows=[]
    M=Re+2*Ro
    for a in range(n):
        for b in np.nonzero(M[a])[0]:
            row=np.zeros(n); row[a]+=1; row[b]-=1; rows.append(row)
    rk=np.linalg.matrix_rank(np.array(rows))
    chk(f'L={L}: T1 uniqueness (diagonal commutant is 1-dimensional)', n-rk==1)
    # Theorem 5
    h=[lifts[((0,1,2),(1,-1,-1))],lifts[((0,1,2),(-1,1,-1))],lifts[((0,1,2),(-1,-1,1))]]
    chk(f'L={L}: T5 perpendicular face half-turn lifts anticommute on the torus', all(np.allclose(acomm(h[i],h[j]),0) for i in range(3) for j in range(i)))
    hh=lifts[((0,1,2),(1,-1,-1),'hat')]
    chk(f'L={L}: T5 rho-hat(h_1) proportional to Gamma_2 Gamma_3', prop(hh,G[1]@G[2])[0])
    # edge half-turns: axes (1,1,0) and (1,-1,0): Q swaps e1,e2 and negates e3 ; and e1->-e2,e2->-e1,e3->-e3
    e1=lifts[((1,0,2),(1,1,-1))]; e2=lifts[((1,0,2),(-1,-1,-1))]
    chk(f'L={L}: T5 remark: perpendicular edge half-turn lifts anticommute', np.allclose(acomm(e1,e2),0))
    q=lifts[((1,0,2),(1,-1,1))]  # quarter turn about e3
    chk(f'L={L}: T5 remark: sign-lift face quarter-turn fourth power = -1', np.allclose(np.linalg.matrix_power(q,4),-np.eye(n)))
    # C7(b): which sign lifts commute with W V W* generators
    Wd=np.diag([1j**(sum(x)) for x in sites]) if L%4==0 else None
    if Wd is not None:
        cnt=0; which=[]; dform=True; cform=True
        for Q,p,s in rots:
            rho=lifts[(p,s)]
            c=np.allclose(rho@(Wd@Re@Wd.conj().T)@rho.T,Wd@Re@Wd.conj().T) and np.allclose(rho@(Wd@Ro@Wd.conj().T)@rho.T,Wd@Ro@Wd.conj().T)
            if c: cnt+=1; which.append((p,s))
            DQ=np.diag([np.prod([(-1)**x[j] for j in range(3) if s[j]==-1]) for x in sites]).astype(float)
            dform&=prop(Wd@rho@Wd.conj().T, rho@DQ)[0] and prop(Wd.conj().T@rho@Wd, rho@DQ)[0]
            f=lifts[(p,s,'hat')]@np.linalg.multi_dot([I8]+[Z[j] for j in range(3) if s[j]==-1]+[I8])
            for k in range(3):
                cform&=np.allclose(f@G[k]@f.conj().T,G[p[k]]) and np.allclose(f@A[k]@f.conj().T,s[k]*A[p[k]])
        chk(f'L={L}: C7(b) exactly 3 of 24 sign lifts commute with W R_T W* (found {cnt}: {which})', cnt==3 and all(s==(1,1,1) for p,s in which))
        chk(f'L={L}: C7(d) W rho W* and W* rho W are phases times rho D_Q', dform)
        chk(f'L={L}: C7(c) rho-hat prod Z_j maps Gamma_k->Gamma_pi(k), A_k->s_k A_pi(k)', cform)
    # C3: tau = D_s D_d T_1 with tau R_e tau^-1 = -R_o, tau R_o tau^-1 = -R_e
    n=len(sites); P=np.zeros((n,n))
    for x in sites: P[idx[tuple((c+1)%L for c in x)],idx[x]]=1
    Ds=np.diag([(-1.0)**sum(x) for x in sites])
    # find sign gauge d: (P D) Re (P D)^T = +Ro  (then D_s flips the sign)
    T1=P.T@Ro@P; T2=P.T@Re@P
    d=np.zeros(n); d[0]=1; st=[0]; fail=False
    M=Re+2*Ro; T=T1+2*T2
    while st:
        a=st.pop()
        for b in np.nonzero(M[a])[0]:
            r=T[a,b]/M[a,b]
            if abs(abs(r)-1)>1e-9: fail=True
            if d[b]==0: d[b]=d[a]*r; st.append(b)
    tau=Ds@P@np.diag(d)
    c3=(not fail) and np.allclose(tau@Re@tau.T,-Ro) and np.allclose(tau@Ro@tau.T,-Re)
    chk(f'L={L}: C3/LW1 A2: signed diagonal translation tau with tau R_e tau^-1=-R_o, tau R_o tau^-1=-R_e exists', c3)
    if c3:
        B0=bloch(L,sites,idx,np.zeros(3)); t0=B0.conj().T@tau@B0
        chk(f'L={L}: C3 tau-hat(0) proportional to chi', prop(t0,chi)[0])
        from scipy.linalg import expm
        for eps in (0.3,0.9,1.4):
            U=expm(1j*eps*sum(A)/np.sqrt(3)/2); Gg=[U@g@U.conj().T for g in G]; chiG=-1j*Gg[0]@Gg[1]@Gg[2]
            Ve=expm(-1j*eps*Re); Vo=expm(1j*eps*Ro); V=Vo@Ve
            sig=Ve.conj().T@tau
            good=np.allclose(sig@V@np.linalg.inv(sig),V) and prop(B0.conj().T@sig@B0,chiG)[0] and np.allclose(chiG,U@chi@U.conj().T)
            good&= not prop(B0.conj().T@sig@B0,chi)[0]   # control: sigma-hat(0) is NOT prop to chi
            chk(f'L={L} eps={eps}: sigma=V_e^-1 tau commutes with V; sigma-hat(0) prop chi_G (and not prop chi)', good)
# ---- Theorem 7 (uses fibre formulas verified above, L=6 torus fibres are exact Bloch fibres; here use formula for general K)
from scipy.linalg import expm, logm
Rsum=sum(A)/np.sqrt(3)
def VK(K,eps,mu=0.0):
    Ro=sum(np.cos(K[j])*A[j]-np.sin(K[j])*G[j] for j in range(3))/np.sqrt(3)
    return expm(1j*(eps+mu/2)*Ro)@expm(-1j*(eps-mu/2)*Rsum)
rng=np.random.default_rng(1)
good=True; ctrl=True
for eps in (0.2,0.7,1.3,1.55):
    U=expm(1j*eps*Rsum/2); v=np.sin(eps)/np.sqrt(3)
    Gg=[U@g@U.conj().T for g in G]
    for t in (1e-3,1e-4):
        n_=rng.normal(size=3); n_/=np.linalg.norm(n_); K=t*n_
        h=1j*logm(VK(K,eps))
        lead=v*sum(K[j]*Gg[j] for j in range(3))
        good&=np.linalg.norm(h-lead)<20*t*t
        ctrl&=np.linalg.norm(h-v*sum(K[j]*G[j] for j in range(3)))>0.05*t  # un-conjugated Gamma fails
        ev=np.sort(np.linalg.eigvalsh((h+h.conj().T)/2))
        good&=np.allclose(ev[:4],-v*t,atol=20*t*t) and np.allclose(ev[4:],v*t,atol=20*t*t)
chk('T7 h(K)=v sum K_j G_j + O(K^2), eigenvalues +-v|K| fourfold (4 eps values)', good)
chk('T7 control: leading term with Gamma_j instead of G_j is rejected', ctrl)
# only V=I node: scan grid
mn=1e9
for eps in (0.2,0.7,1.3):
    for K in itertools.product(np.linspace(-np.pi,np.pi,13),repeat=3):
        K=np.array(K)
        dist=np.linalg.norm(VK(K,eps)-I8)
        if np.linalg.norm(K)>1e-9: mn=min(mn,dist)
        else: assert dist<1e-12
chk(f'T7 V(K)=I only at K=0 on a 13^3 grid (min distance elsewhere {mn:.3f})', mn>1e-2)
chk('T7 mu>0: V(0)=exp(i mu R_e), R_e anticommutes with Gamma_j', np.allclose(VK(np.zeros(3),0.7,0.4),expm(1j*0.4*Rsum)) and all(np.allclose(acomm(Rsum,g),0) for g in G))
# ---- Theorem 8
eps3=np.zeros((3,3,3)); eps3[0,1,2]=eps3[1,2,0]=eps3[2,0,1]=1; eps3[0,2,1]=eps3[2,1,0]=eps3[1,0,2]=-1
S=[-(1j/4)*sum(eps3[k,a,b]*G[a]@G[b] for a in range(3) for b in range(3)) for k in range(3)]
SA=[-(1j/4)*sum(eps3[k,a,b]*A[a]@A[b] for a in range(3) for b in range(3)) for k in range(3)]
def su2(T): return all(np.allclose(T[a]@T[b]-T[b]@T[a],1j*sum(eps3[a,b,c]*T[c] for c in range(3))) for a in range(3) for b in range(3)) and np.allclose(sum(t@t for t in T),0.75*I8)
chk('T8 S and S^A are spin-1/2 triples, mutually commuting, S commutes with R_e', su2(S) and su2(SA) and all(np.allclose(S[a]@SA[b],SA[b]@S[a]) for a in range(3) for b in range(3)) and all(np.allclose(s@Rsum,Rsum@s) for s in S))
chk('T8 chi commutes with Gamma, S, S^A; anticommutes with A; eigenspaces 4+4', all(np.allclose(chi@g,g@chi) for g in G+S+SA) and all(np.allclose(acomm(chi,a),0) for a in A) and abs(np.trace(chi))<1e-12 and np.allclose(chi@chi,I8))
sites,idx,Re,Ro,edges=hops(4); B0=bloch(4,sites,idx,np.zeros(3))
hats={}
for Q,p,s in rotations():
    hats[(p,s)]=(Q,B0.conj().T@find_lift(Q,4,sites,idx,Re,Ro)@B0)
import scipy.linalg as sl
def axis_angle(Q):
    w,v=np.linalg.eig(Q); 
    ang=np.arccos(np.clip((np.trace(Q)-1)/2,-1,1))
    if ang<1e-9: return np.array([0,0,1.]),0.0
    ax=np.real(v[:,np.argmin(abs(w-1))]); ax/=np.linalg.norm(ax)
    # fix sign: Q - Q^T = 2 sin(ang) [ax]_x
    if ang<np.pi-1e-9:
        sk=(Q-Q.T)/2; ax2=np.array([sk[2,1],sk[0,2],sk[1,0]])/np.sin(ang); ax=ax2
    return ax,ang
t8=True; scal=True; pure=[]; moduli={}
comm_rows=[]
ew,ev=np.linalg.eigh(chi); Pp=ev[:,ew>0]; Pm=ev[:,ew<0]
for (p,s),(Q,rh) in hats.items():
    ax,ang=axis_angle(Q)
    Sp=sl.expm(-1j*ang*sum(ax[k]*S[k] for k in range(3)))
    T=Sp.conj().T@rh
    t8&=all(np.allclose(T@g,g@T) for g in G) and all(np.allclose(T@A[j]@T.conj().T,A[p[j]]) for j in range(3))
    # Sp acts on Gamma as rotation
    t8&=all(np.allclose(Sp@G[j]@Sp.conj().T,s[j]*G[p[j]]) for j in range(3))
    isscalar=prop(T,I8)[0]
    if isscalar: pure.append((p,s))
    # taste form
    if p in ((1,2,0),(2,0,1)):
        cands=[sl.expm(-1j*sg*2*np.pi/3*sum(SA)/np.sqrt(3)) for sg in (1,-1)]
        t8&=any(prop(T,c)[0] for c in cands)
    if sorted(p)!=list(p) and p not in ((1,2,0),(2,0,1)):
        j,k=[i for i in range(3) if p[i]!=i]
        n_=np.zeros(3); n_[j]=1; n_[k]=-1; n_/=np.sqrt(2)
        c=chi@sl.expm(-1j*np.pi*sum(n_[m]*SA[m] for m in range(3)))
        t8&=prop(T,c)[0]
    cls=(round(float(np.trace(Q))),p==(0,1,2))
    for nm,Pc in (('+',Pp),('-',Pm)):
        moduli.setdefault((cls,nm),set()).add(round(abs(np.trace(Pc.conj().T@rh@Pc)),6))
chk('T8 rho-hat(Q)=S(Q~)T(Q), T commutes with Gamma, T A_j T*=A_pi(j); 3-cycles taste 2pi/3 about (1,1,1); transpositions chi*taste pi about (e_j-e_k)/sqrt2', t8)
chk(f'T8 scalar T exactly for identity and three face half-turns (Cor 9.1 third claim): {sorted(pure)}', sorted(pure)==sorted([((0,1,2),(1,1,1)),((0,1,2),(1,-1,-1)),((0,1,2),(-1,1,-1)),((0,1,2),(-1,-1,1))]))
print('   character moduli per chirality by class (trQ, pi=id):',{k:sorted(v) for k,v in sorted(moduli.items())})
exp_mod={((3,True)):4.0,((0,False)):1.0,((-1,True)):0.0,((1,False)):0.0,((-1,False)):0.0}
chk('T8 remark: character moduli 4,1,0,0,0 on id, 3-fold, face half-turn, quarter-turn, edge half-turn', all(v=={exp_mod[k[0]]} for k,v in moduli.items()))
# irreducibility: commutant of the projective rep on each chirality, and of taste operators
for nm,Pc in (('+',Pp),('-',Pm)):
    rows=[]
    for (p,s),(Q,rh) in hats.items():
        r4=Pc.conj().T@rh@Pc
        rows.append(np.kron(r4,np.eye(4))-np.kron(np.eye(4),r4.T))
    nul=16-np.linalg.matrix_rank(np.vstack(rows),tol=1e-9)
    chk(f'T8 chirality {nm}: commutant of the 4-dim projective cell representation has dimension {nul}', nul==1)
    # taste: algebra generated by T(Q) restricted: commutant within operators commuting with S -> dimension
    rows=[]
    for (p,s),(Q,rh) in hats.items():
        ax,ang=axis_angle(Q); Sp=sl.expm(-1j*ang*sum(ax[k]*S[k] for k in range(3)))
        T=Pc.conj().T@(Sp.conj().T@rh)@Pc
        rows.append(np.kron(T,np.eye(4))-np.kron(np.eye(4),T.T))
    nul=16-np.linalg.matrix_rank(np.vstack(rows),tol=1e-9)
    chk(f'T8 chirality {nm}: commutant of taste operators has dimension {nul} (=4 iff taste irreducible on C^2)', nul==4)
# Cor 9.1: T commutes with U and with G_j
eps=0.7; U=expm(1j*eps*Rsum/2); Gg=[U@g@U.conj().T for g in G]
c91=True
for (p,s),(Q,rh) in hats.items():
    ax,ang=axis_angle(Q); Sp=sl.expm(-1j*ang*sum(ax[k]*S[k] for k in range(3))); T=Sp.conj().T@rh
    c91&=np.allclose(U@T@U.conj().T,T) and all(np.allclose(T@g,g@T) for g in Gg)
c91&=all(np.allclose(U@s_@U.conj().T,s_) for s_ in S)
chk('Cor 9.1 / T9: U commutes with S and T(Q); T(Q) commutes with G_j', c91)
# D conjugation for L5-O frame
D=np.diag([1j**sum(r) for r in itertools.product([0,1],repeat=3)])
print('   D S_k D* == S^A_k up to sign pattern:',[ [np.allclose(D@S[k]@D.conj().T,sg*SA[k]) for sg in (1,-1)] for k in range(3)])
print('ALL PASS' if ok else 'SOME FAIL')
