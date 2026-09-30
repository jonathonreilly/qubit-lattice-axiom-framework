# E1, E2, E3, MC-C closed forms for T80.  Exact where stated.
import itertools, math, random
from fractions import Fraction as F

# ---------- E1: neutral two-valued gas == Ising HT loop gas ----------
# cube graph Q3 (8 vertices, 12 edges), and a 3-cycle-with-tail graph as second test.
def cube_edges():
    V=list(itertools.product((0,1),repeat=3)); idx={v:i for i,v in enumerate(V)}
    E=[]
    for v in V:
        for k in range(3):
            w=list(v); w[k]^=1; w=tuple(w)
            if idx[v]<idx[w]: E.append((idx[v],idx[w]))
    return 8,E
def zdirect(nv,E,t,z):
    Z=F(0)
    for cfg in itertools.product((-1,0,1),repeat=nv):
        w=F(1)
        for s in cfg:
            if s: w*=z
        for i,j in E: w*=(1+t*cfg[i]*cfg[j])
        Z+=w
    return Z
def zht(nv,E,t,z):
    Z=F(0)
    for mask in range(1<<len(E)):
        deg=[0]*nv; ne=0
        for k,(i,j) in enumerate(E):
            if mask>>k&1: deg[i]+=1; deg[j]+=1; ne+=1
        w=t**ne
        for d in deg:
            if d==0: w*=(1+2*z)
            elif d%2==1: w=0; break
            else: w*=2*z
        Z+=w
    return Z
ok=True
graphs={'cube Q3':cube_edges(),'triangle+tail (5 vtx)':(5,[(0,1),(1,2),(2,0),(2,3),(3,4)]),'K4':(4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])}
for name,(nv,E) in graphs.items():
    for t,z in ((F(3,7),F(5,3)),(F(1,2),F(1,8)),(F(9,10),F(20))):
        a=zdirect(nv,E,t,z); b=zht(nv,E,t,z)
        print(f"E1 {name:24s} t={t} z={z}: equal={a==b}")
        ok&=(a==b)
print("E1 ALL EQUAL:",ok)

# ---------- E2: 6N = 2 N_oo + N_oe ----------
def torus_nb(L):
    nb=[]
    for x in range(L):
        for y in range(L):
            for w in range(L):
                nb.append([(((x+1)%L)*L+y)*L+w,(((x-1)%L)*L+y)*L+w,(x*L+(y+1)%L)*L+w,(x*L+(y-1)%L)*L+w,(x*L+y)*L+(w+1)%L,(x*L+y)*L+(w-1)%L])
    return nb
L=4; nb=torus_nb(L); V=L**3; random.seed(3); bad=0
for _ in range(200):
    n=[random.random()<random.random() for _ in range(V)]
    N=sum(n); Noo=Noe=0
    for i in range(V):
        for j in nb[i]:
            if i<j:
                if n[i] and n[j]: Noo+=1
                elif n[i]!=n[j]: Noe+=1
    # pairs i<j with j in nb[i]: each bond once (L=4 no multiplicity)
    if 6*N!=2*Noo+Noe: bad+=1
print("E2 violations in 200 random configs:",bad)

# ---------- E3: mean-field mass channel, finite difference of the 7-outcome map ----------
def cmap(pis, z, g, T, w):
    # pis: list of 6 neighbour odds vectors over 7 outcomes [empty, a1..a6]; omega matrix w(a,b) with rows summing to T; c0=6/T; c=g*c0
    c=g*6.0/T
    out=[1.0]+[z]*6
    for pi in pis:
        m=[1.0]+[0.0]*6
        for a in range(6):
            m[1+a]=pi[0]*1.0+sum(c*w[a][b]*pi[1+b] for b in range(6))
        out=[o*mm for o,mm in zip(out,m)]
    tot=sum(out); return [o/tot for o in out]
p,q,r=3.0,1.0,2.0; T=p+q+4*r
# six-axis omega: axes +x,-x,+y,-y,+z,-z ; equal->p, opposite->q, orthogonal->r
ax=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def om(a,b):
    d=sum(u*v for u,v in zip(ax[a],ax[b])); return p if d==1 else (q if d==-1 else r)
w=[[om(a,b) for b in range(6)] for a in range(6)]
def rho_of(pi): return 1-pi[0]
def fixed(g,rho):
    z=rho/(6*(1-rho)*(1+rho*(g-1))**6); return z
maxerr=0
for g,rho in ((1.0,0.4),(2.0,0.5),(2.0,1/3),(3.0,0.2),(1.5,0.7)):
    z=fixed(g,rho); u=[1-rho]+[rho/6]*6
    base=cmap([u]*6,z,g,T,w); assert abs(rho_of(base)-rho)<1e-12, (g,rho,rho_of(base))
    eps=1e-6; up=[1-rho-eps]+[(rho+eps)/6]*6
    pert=cmap([up]+[u]*5,z,g,T,w)
    fd=(rho_of(pert)-rho)/eps
    cf=rho*(1-rho)*(g-1)/(1+rho*(g-1))
    maxerr=max(maxerr,abs(fd-cf)); print(f"E3 g={g} rho={rho:.4f}: finite diff {fd:.8f}  closed form {cf:.8f}  6*lambda_s={6*cf:.5f}")
print("E3 max abs error:",maxerr)
# massless (6 lambda_s = 1) density solutions: 6x rho^2 -5x rho +1 = 0, x=g-1
for x in (0.5,24/25,1.0,2.0,5.0):
    D=25*x*x-24*x
    if D<0: print(f"E3 x=g-1={x:.3f}: no real density (channel screened at every density)")
    else: print(f"E3 x=g-1={x:.3f}: massless at rho = {(5*x-math.sqrt(D))/(12*x):.4f} and {(5*x+math.sqrt(D))/(12*x):.4f}")
print("E3 critical point: g-1 = 24/25 (g=%.4f), rho=5/12=%.4f"%(1+24/25,5/12))

# ---------- MC-C: block 126 sufficient criterion, smallest proven c ----------
G0=0.2527  # lattice Green function at origin of -Laplacian with E(k)=sum 2(1-cos k_i); 3G0 = 0.758
G3=3*G0
print("MC-C 3G(0) =",G3)
print("beta  rho   g=beta-3G/rho   c*=g/sinh g    c0=beta/sinh beta    c*/c0     ln(c*/c0)")
for b in (1.0,1.5,2.0,3.0,5.0,8.0):
    for rho in (0.5,0.75,0.9,1.0):
        g=b-G3/rho
        if g<=0: print(f"{b:4.1f} {rho:5.2f}   proof cannot reach order (beta*rho <= 3G(0))"); continue
        cs=g/math.sinh(g); c0=b/math.sinh(b)
        print(f"{b:4.1f} {rho:5.2f}   {g:8.4f}   {cs:10.5f}   {c0:10.5f}   {cs/c0:8.3f}   {math.log(cs/c0):7.3f}")
