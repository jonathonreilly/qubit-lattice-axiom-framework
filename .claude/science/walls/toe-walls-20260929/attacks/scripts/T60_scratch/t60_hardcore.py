"""T60 tests A2 (hard-core), A5, A7: exact hard-core (one record per site) hopping on small bipartite tori.
H = -sum_bonds t_b (b_i^dag b_j + h.c.) with hard-core bosons (spin-1/2 XY). Record number n is conserved.
Run: python3 t60_hardcore.py > t60_hardcore_output.txt
"""
import numpy as np, itertools
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

def build_sector(nsites, bonds, tvals, n):
    """bonds: list of (i,j); tvals: same length. Returns sparse H on the n-particle sector."""
    from math import comb
    states = [s for s in range(1<<nsites) if bin(s).count("1")==n]
    idx = {s:k for k,s in enumerate(states)}
    rows=[];cols=[];vals=[]
    for s in states:
        k = idx[s]
        for (i,j),t in zip(bonds,tvals):
            bi=(s>>i)&1; bj=(s>>j)&1
            if bi!=bj:
                s2 = s ^ ((1<<i)|(1<<j))
                rows.append(idx[s2]); cols.append(k); vals.append(-t)
    d=len(states)
    return sp.csr_matrix((vals,(rows,cols)),shape=(d,d)), d

def ground(nsites,bonds,tvals,n):
    if n==0 or n==nsites: return 0.0
    H,d = build_sector(nsites,bonds,tvals,n)
    if d<=400:
        return np.linalg.eigvalsh(H.toarray())[0]
    return eigsh(H,k=1,which='SA',return_eigenvectors=False)[0]

def torus2d(Lx,Ly):
    idx=lambda x,y:(x%Lx)*Ly+(y%Ly)
    bonds=[];axis=[]
    for x in range(Lx):
        for y in range(Ly):
            bonds.append((idx(x,y),idx(x+1,y)));axis.append(0)
            bonds.append((idx(x,y),idx(x,y+1)));axis.append(1)
    return Lx*Ly,bonds,np.array(axis)

# ---------- 4x4 torus ----------
N,bonds,axis = torus2d(4,4)
t = np.ones(len(bonds))
E = np.array([ground(N,bonds,t,n) for n in range(N+1)])
print("A5 hard-core 4x4 torus (t=1), exact E0(n):")
for n in range(N+1):
    print("   n=%2d  E0=%10.6f   e(n)=E0/N=%9.6f" % (n,E[n],E[n]/N))
print("   E0(0)=E0(N)=0: %s ; symmetric E0(n)=E0(N-n): max dev %.2e" % (E[0]==0 and E[N]==0, np.abs(E-E[::-1]).max()))
emin = E.min()/N; nmin=int(np.argmin(E))
print("   e_min = %.6f per site at n=%d" % (emin,nmin))
# sector n=8 spectrum symmetric?
H8,d8 = build_sector(N,bonds,t,8)
ev = np.linalg.eigvalsh(H8.toarray()) if d8<=13000 else None
print("   n=8 spectrum symmetric about 0 (max |E_k + E_{d-1-k}|) = %.2e ; min %.4f max %.4f" % (np.abs(ev+ev[::-1]).max(), ev[0], ev[-1]))

# leftover table
print("\nA5 leftover source per site (units of hop t) for three zeros, by record density n/N")
print("   n/N   Z_A=e(n)   Z_2=e(n)-e_min   Z_3=0 ; mu(n)=E0(n+1)-E0(n)")
for n in range(N+1):
    mu = (E[n+1]-E[n]) if n<N else float('nan')
    print("   %.3f  %9.5f  %9.5f            %9.5f" % (n/N, E[n]/N, E[n]/N-emin, mu))
maxA = np.abs(E/N).max()/abs(emin); maxZ2 = np.abs(E/N-emin).max()/abs(emin)
print("   max_n |leftover|/|e_min|: Z_A=%.3f  Z_2=%.3f   (pass needs <= 0.01)" % (maxA,maxZ2))
mu = E[1:]-E[:-1]
print("   sum_n mu(n) = %.2e (empty and full both have E=0); mu range [%.4f, %.4f]; total formation energy paid empty->half = %.4f per site" % (mu.sum(), mu.min(), mu.max(), E[N//2]/N))

# A2 hard-core: scale covariance, finite difference in ell
def Ehalf(tt): return ground(N,bonds,tt*np.ones(len(bonds)),8)
h=1e-4
E1=Ehalf(1.0); dE=(Ehalf(1/(1+h))-Ehalf(1/(1-h)))/(2*h)   # t = 1/ell
print("\nA2 hard-core half filling: E0(t=1/ell)=E0/ell ; p/rho = (-dE/dV)/(E/V) with V=N ell^3:")
rho=E1/N; p=-dE/(3*N)
print("   rho=%.6f p=%.6f p/rho=%.6f (prediction 1/3)" % (rho,p,p/rho))

# ---------- A7 shear lemma on 4x4 ----------
print("\nA7 volume-keeping shear t_x=e^s, t_y=e^-s at half filling (16 sites): E0(s) <= cosh(s) E0(0)?")
E0s = ground(N,bonds,np.ones(len(bonds)),8)
for s in (0.0,0.1,0.3,0.6,1.0):
    tt = np.where(axis==0,np.exp(s),np.exp(-s))
    Es = ground(N,bonds,tt,8)
    print("   s=%.1f  E0=%10.6f  cosh(s)*E0(0)=%10.6f  gap=%.2e  ok=%s" % (s,Es,np.cosh(s)*E0s,Es-np.cosh(s)*E0s, Es<=np.cosh(s)*E0s+1e-9))

# ---------- cube Q3, three-axis shear with AM-GM ----------
print("\nA7 cube Q3 (2x2x2 open, all axis permutations are symmetries), half filling n=4, t=(e^s1,e^s2,e^s3), sum s=0:")
def cube():
    idx=lambda x,y,z:x*4+y*2+z
    bonds=[];axis=[]
    for x,y,z in itertools.product(range(2),repeat=3):
        if x==0: bonds.append((idx(0,y,z),idx(1,y,z)));axis.append(0)
        if y==0: bonds.append((idx(x,0,z),idx(x,1,z)));axis.append(1)
        if z==0: bonds.append((idx(x,y,0),idx(x,y,1)));axis.append(2)
    return 8,bonds,np.array(axis)
N3,b3,ax3=cube()
E3_0=ground(N3,b3,np.ones(len(b3)),4)
for (s1,s2,s3) in ((0.2,-0.1,-0.1),(0.5,-0.5,0.0),(0.6,0.2,-0.8),(1.0,-0.5,-0.5)):
    tt = np.exp(np.array([s1,s2,s3]))[ax3]
    Es = ground(N3,b3,tt,4)
    tau = np.mean(np.exp([s1,s2,s3]))
    print("   s=(%.1f,%.1f,%.1f): E0=%9.5f <= tau*E0(1)=%9.5f (tau=%.4f>=1) ok=%s ; AM-GM tau>=1: %s" % (s1,s2,s3,Es,tau*E3_0,tau,Es<=tau*E3_0+1e-9,tau>=1))
