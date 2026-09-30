"""T72 Part A: eight doubler species of the 3D two-component walk H = sum_j sigma_j S_j, clocked H_w = phi H phi.
V_n = (-1)^{n.x} (x) U_n with U_n = I, sigma_a (|n|=1, a the flipped axis), sigma_c (|n|=2, c the unflipped axis), I (|n|=3);
s_n = (-1)^{|n|}.  Checks: V H_w V^dag = s_n H_w (arbitrary positive phi, open box); acceleration of <X_j> identical
for all species; one-step momentum S_j rate differs by s_n D_j (ledger sign), D_j = (-1)^{n_j}."""
import numpy as np, scipy.sparse as sp, itertools
L=6
pa=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
def site(x,y,z): return (x*L+y)*L+z
N=L**3
def Sj(j):
    rows=[];cols=[];vals=[]
    for x in range(L):
        for y in range(L):
            for z in range(L):
                c=[x,y,z]
                if c[j]<L-1:
                    d=list(c); d[j]+=1
                    a=site(*c); b=site(*d)
                    rows+= [b,a]; cols+=[a,b]; vals+=[1/(2j),-1/(2j)]   # (S psi)(x)=(psi(x-1)-psi(x+1))/2i
    return sp.csr_matrix((vals,(rows,cols)),shape=(N,N),dtype=complex)
S=[Sj(j) for j in range(3)]
def clocked(phi):
    P=sp.diags(phi)
    H=sum(sp.kron(P@S[j]@P, sp.csr_matrix(pa[j])) for j in range(3))
    return H.tocsr()
rng=np.random.default_rng(7)
coords=np.array([(x,y,z) for x in range(L) for y in range(L) for z in range(L)],float)
xc=(L-1)/2
u=0.06*(coords[:,0]-xc)+0.03*(coords[:,1]-xc)-0.04*(coords[:,2]-xc)+0.05*rng.standard_normal(N)   # arbitrary positive clock incl. noise
phi=np.exp(u/2)
H=clocked(phi)
def Vn(n):
    sgn=np.array([(-1.0)**(n[0]*int(c[0])+n[1]*int(c[1])+n[2]*int(c[2])) for c in coords])
    w=sum(n)
    if w==0: U=np.eye(2,dtype=complex)
    elif w==1: U=pa[n.index(1)]
    elif w==2: U=pa[n.index(0)]
    else: U=np.eye(2,dtype=complex)
    return sp.kron(sp.diags(sgn.astype(complex)),sp.csr_matrix(U)).tocsr(), (-1)**w
X=[sp.kron(sp.diags(coords[:,j].astype(complex)),sp.identity(2)).tocsr() for j in range(3)]
psi0=np.exp(-((coords-xc)**2).sum(1)/(2*1.5**2)).astype(complex)
psi0=psi0*np.exp(1j*(0.9*coords[:,0]+0.4*coords[:,1]-0.7*coords[:,2]))*(1+0.2*rng.standard_normal(N))
psi0=np.kron(psi0,np.array([0.8,0.6j]))
psi0/=np.linalg.norm(psi0)
def acc(psi,j):
    A=H@X[j]-X[j]@H; B=H@A-A@H
    return -np.vdot(psi,B@psi).real
def prate(psi,j):
    Sfull=sp.kron(S[j],sp.identity(2)).tocsr()   # one-step momentum generator (coin-blind)
    C=H@Sfull-Sfull@H
    return (1j*np.vdot(psi,C@psi)).real
print("n     s_n  max|V H V^dag - s H|   a_x        a_y        a_z      | d<S_x>/dt (one-step momentum rate)")
base=None
for n in itertools.product((0,1),repeat=3):
    V,s=Vn(list(n))
    err=abs(V@H@V.conj().T - s*H).max()
    psi=V@psi0
    a=[acc(psi,j) for j in range(3)]
    pr=[prate(psi,j) for j in range(3)]
    if base is None: base=(a,pr)
    print(f"{n}  {s:+d}  {err:9.2e}        {a[0]:+.8f} {a[1]:+.8f} {a[2]:+.8f} | {pr[0]:+.8f}  (ratio to species 0: {pr[0]/base[1][0]:+.3f}, {pr[1]/base[1][1]:+.3f}, {pr[2]/base[1][2]:+.3f})")
print("max deviation of accelerations from species 0:", max(abs(np.array([acc(Vn(list(n))[0]@psi0,j) for j in range(3)])-np.array(base[0])).max() for n in itertools.product((0,1),repeat=3)))
