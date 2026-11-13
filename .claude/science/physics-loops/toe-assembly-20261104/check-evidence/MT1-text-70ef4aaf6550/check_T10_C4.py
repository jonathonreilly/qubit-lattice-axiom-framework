# Theorem 10 and C4 (Proposition C). Symmetry matrices come from torus lifts (check_lib), not from the text's closed forms.
import numpy as np, itertools, scipy.linalg as sl
from check_lib import *
A,Z,G=cellmats(); I8=np.eye(8); Rsum=sum(A)/np.sqrt(3)
ok=True
def chk(n,c):
    global ok; ok&=bool(c); print(('PASS ' if c else 'FAIL ')+n)
L=4; sites,idx,Re,Ro,edges=hops(L); B0=bloch(L,sites,idx,np.zeros(3))
rots=rotations(); hat={}
for Q,p,s in rots: hat[(p,s)]=(Q,B0.conj().T@find_lift(Q,L,sites,idx,Re,Ro)@B0)
# inversion lift from the torus: I(x)=1-x
n=len(sites); P=np.zeros((n,n))
for x in sites: P[idx[tuple((1-c)%L for c in x)],idx[x]]=1
M=Re+2*Ro; T=P.T@M@P; d=np.zeros(n); d[0]=1; st=[0]
while st:
    a=st.pop()
    for b in np.nonzero(M[a])[0]:
        if d[b]==0: d[b]=d[a]*T[a,b]/M[a,b]; st.append(b)
rI=P@np.diag(d)
chk('inversion x->1-x has a sign lift commuting with R_e and R_o on the L=4 torus', np.allclose(rI@Re@rI.T,Re) and np.allclose(rI@Ro@rI.T,Ro))
Ihat=B0.conj().T@rI@B0
chk('its fibre is +-A1A2A3', prop(Ihat,A[0]@A[1]@A[2])[0])
# fibre covariance under inversion at K != 0
K=np.array([np.pi,0,np.pi]); B=bloch(L,sites,idx,K); Bm=bloch(L,sites,idx,-K)
Dr=Z[0]@Z[1]@Z[2]
# Theta = D_s K : check Theta V Theta^-1 = V on the torus
Ds=np.diag([(-1.0)**sum(x) for x in sites])
for eps in (0.4,1.1):
    V=sl.expm(1j*eps*Ro)@sl.expm(-1j*eps*Re)
    chk(f'eps={eps}: Theta=D_s K satisfies D_s conj(V) D_s = V (LW1 B10 given, rechecked)', np.allclose(Ds@V.conj()@Ds,V))
def node_conditions(eps):
    U=sl.expm(1j*eps*Rsum/2); Gg=[U@g@U.conj().T for g in G]; chiG=-1j*Gg[0]@Gg[1]@Gg[2]
    return U,Gg,chiG
def residual(N,which,eps):
    U,Gg,chiG=node_conditions(eps); r=0
    if 'R' in which:
        for (p,s),(Q,rh) in hat.items():
            for j in range(3):
                r=max(r,np.linalg.norm(rh@N[j]@rh.conj().T-sum(Q[i,j]*N[i] for i in range(3))))
    if 'I' in which: r=max(r,max(np.linalg.norm(Ihat@N[j]@Ihat.conj().T+N[j]) for j in range(3)))
    if 'T' in which: r=max(r,max(np.linalg.norm(Dr@N[j].conj()@Dr-N[j]) for j in range(3)))
    if 'S' in which: r=max(r,max(np.linalg.norm(N[j]@chiG-chiG@N[j]) for j in range(3)))
    return r
def soldim(which,eps):
    # real-linear solution space of Hermitian triples: parametrise by 3*64 real coordinates
    basis=[]
    for a in range(8):
        for b in range(a,8):
            E=np.zeros((8,8),complex); E[a,b]=E[b,a]=1; basis.append(E)
            if a!=b:
                E=np.zeros((8,8),complex); E[a,b]=1j; E[b,a]=-1j; basis.append(E)
    cols=[]
    U,Gg,chiG=node_conditions(eps)
    gens=[hat[((1,2,0),(1,1,1))],hat[((1,0,2),(1,-1,1))],hat[((0,1,2),(1,-1,-1))]] if 'R' in which else []
    for j in range(3):
        for E in basis:
            N=[np.zeros((8,8),complex)]*3; N=list(N); N[j]=E
            out=[]
            for Q,rh in gens:
                for jj in range(3):
                    out.append(rh@N[jj]@rh.conj().T-sum(Q[i,jj]*N[i] for i in range(3)))
            if 'I' in which: out+= [Ihat@N[jj]@Ihat.conj().T+N[jj] for jj in range(3)]
            if 'T' in which: out+= [Dr@N[jj].conj()@Dr-N[jj] for jj in range(3)]
            if 'S' in which: out+= [N[jj]@chiG-chiG@N[jj] for jj in range(3)]
            vec=np.concatenate([o.reshape(-1) for o in out]) if out else np.zeros(1)
            cols.append(np.concatenate([vec.real,vec.imag]))
    Mx=np.array(cols).T
    return 192-np.linalg.matrix_rank(Mx,tol=1e-8)
for eps in (0.5,1.2):
    dims={w:soldim(w,eps) for w in ('R','RI','RIT','RITS','RIS','RTS','RST','ITS')}
    print(f'   eps={eps}: real solution dimensions',dims)
    chk(f'eps={eps}: C4 (R,I,Theta,sigma) solution space is 1-dimensional', dims['RITS']==1)
    chk(f'eps={eps}: C4 [check] dims 8,4,3,1,2,2', (dims['R'],dims['RI'],dims['RIT'],dims['RITS'],dims['RIS'],dims['RTS'])==(8,4,3,1,2,2))
    U,Gg,chiG=node_conditions(eps)
    chk(f'eps={eps}: a G_j satisfies all four conditions', residual(Gg,'RITS',eps)<1e-10)
    chk(f'eps={eps}: control: Gamma_j (unconjugated) violates them', residual(G,'RITS',eps)>1e-3)
    eps3=np.zeros((3,3,3)); eps3[0,1,2]=eps3[1,2,0]=eps3[2,0,1]=1; eps3[0,2,1]=eps3[2,1,0]=eps3[1,0,2]=-1
    S=[-(1j/4)*sum(eps3[k,a,b]*G[a]@G[b] for a in range(3) for b in range(3)) for k in range(3)]
    def others(j): return [k for k in range(3) if k!=j]
    W1=[U@(1j*S[j]@A[j]@(A[others(j)[0]]+A[others(j)[1]]))@U.conj().T for j in range(3)]
    W2=[U@(Z[j]@(A[others(j)[0]]+A[others(j)[1]]))@U.conj().T for j in range(3)]
    W3=[U@Z[j]@U.conj().T for j in range(3)]
    for nm,Wt,sat,fails in (('witness 1 (not I)',W1,'RTS','I'),('witness 2 (not Theta)',W2,'RIS','T'),('witness 3 = Z^G (not sigma)',W3,'RIT','S')):
        herm=all(np.allclose(w,w.conj().T) for w in Wt)
        iso=[]
        for u in (1e-3,1e-2,0.1,-0.05):
            N=[Gg[j]+u*Wt[j] for j in range(3)]
            # isotropic Clifford cone <=> {N_i,N_j}=2c^2 delta_ij
            c2=np.trace(N[0]@N[0]).real/8
            dev=max(np.linalg.norm(N[i]@N[j]+N[j]@N[i]-2*c2*(i==j)*I8) for i in range(3) for j in range(3))
            iso.append(dev>1e-6*abs(u))
        chk(f'eps={eps}: C4 {nm}: Hermitian={herm}, satisfies {sat} (res {residual(Wt,sat,eps):.1e}), violates {fails} (res {residual(Wt,fails,eps):.2f}), no isotropic cone for u in (1e-3,1e-2,0.1,-0.05): {iso}', herm and residual(Wt,sat,eps)<1e-10 and residual(Wt,fails,eps)>1e-3 and all(iso))
    for nm,Wt,expect in (('without Theta',W2,2*np.sqrt(2)),('without I',W1,np.sqrt(2))):
        u=0.01; M1=Gg[0]+u*Wt[0]; ev=np.linalg.eigvalsh(M1@M1); spread=ev.max()-ev.min()
        print(f'   squared-speed spread along e_1 at u=0.01, {nm}: {spread:.4f} (text: {2*expect*u:.4f})')
        chk(f'eps={eps}: C4 squared speeds along e_1 = 1 +- {expect:.3f} u + O(u^2), {nm}', abs(spread-2*expect*u)<1e-3)
    # Theorem 10 proper
    u=0.03; N=[Gg[j]+u*W3[j] for j in range(3)]
    ax=np.linalg.eigvalsh(N[2]@N[2]); 
    nd=sum(N)/np.sqrt(3); dg=np.linalg.eigvalsh(nd@nd)
    Y=1j*sum(G[i]@G[j]@(A[i]-A[j]) for i in range(3) for j in range(i+1,3))
    Md=sum(G[j]+u*Z[j] for j in range(3))/np.sqrt(3)
    quad=u*u*(sum(Z)@sum(Z))/3
    chk(f'eps={eps}: T10 axial squared speed = 1+u^2 exactly; diagonal squared velocity = 1+(2u/3)Y+u^2(sum Z)^2/3; Y Hermitian traceless nonzero with eigenvalues {np.round(np.linalg.eigvalsh(Y),3)}', np.allclose(ax,1+u*u) and np.allclose(Md@Md,I8+(2*u/3)*Y+quad) and np.allclose(Y,Y.conj().T) and abs(np.trace(Y))<1e-12 and np.linalg.norm(Y)>1)
    chk(f'eps={eps}: T10 diagonal speeds differ from axial (spread {dg.max()-dg.min():.4f})', dg.max()-dg.min()>1e-3)
    chk(f'eps={eps}: T10 h_u covariant under 24 rotations and inversion, obeys antiunitary condition, fails sigma', residual(N,'RIT',eps)<1e-10 and residual(N,'S',eps)>1e-3)
# finite-range operator with fibre sum_j sin K_j Z_j
L=6; sites,idx,Re,Ro,edges=hops(L); n=len(sites)
def Tr(t):
    Pm=np.zeros((n,n))
    for x in sites: Pm[idx[tuple((c+tt)%L for c,tt in zip(x,t))],idx[x]]=1
    return Pm
Zs=[np.diag([(-1.0)**x[j] for x in sites]) for j in range(3)]
Op=sum(Zs[j]@(Tr(tuple(-2*(k==j) for k in range(3)))-Tr(tuple(2*(k==j) for k in range(3))))/(2j) for j in range(3))
good=True
for k in itertools.product(range(3),repeat=3):
    K=2*np.pi*np.array(k)/3; B=bloch(L,sites,idx,K)
    good&=np.allclose(B.conj().T@Op@B,sum(np.sin(K[j])*Z[j] for j in range(3)))
chk('T10 sum_j Z_j (T_{-2e_j}-T_{2e_j})/(2i) has fibre sum_j sin K_j Z_j (L=6, 27 momenta)', good)
print('ALL PASS' if ok else 'SOME FAIL')
