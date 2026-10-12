"""B1 (lane RB): d = 2, 3 checks.
 (a) d=2 KG: deformed rotation W = J grad u commutes with H; zeros and their type (elliptic/hyperbolic);
     orbit period T(E) (non-compact 'rotation'; non-integer angular momentum 2*pi*n/T)
 (b) d=2: undeformed rotation acting on a vector P (W.grad p = J p) -- for random odd C4-covariant p:
     zeros of p have degree sum 0; fold set det Dp = 0 is nonempty and adj(Dp) J p != 0 there => W blows up
 (c) first-moment (lapse-smearing) algebra with P = grad u: double points of (H,P) on C4/O orbits of
     critical points, Hessians differ => [K_a,P_b] is not a function of (H,P). Random cubic-covariant u, d=2,3.
     Also the van Hove-line collisions for the d=2 KG.
 (d) d=3 KG: first-moment rotations L_ab = u_a d_b - u_b d_a do not close so(3) (deformed)
 (e) orbit-average sum rule along a random (non-first-moment) boost flow in d=2: <F_11>_orbit -> 0
"""
import numpy as np, sympy as sp, itertools
from scipy.optimize import root
from scipy.integrate import solve_ivp
rng = np.random.default_rng(7)

print("=== (a) d=2 lattice KG: W = J grad u ===")
k1,k2,m = sp.symbols('k1 k2 m', real=True)
u = (m**2 + 2*(2-sp.cos(k1)-sp.cos(k2)))/2
w = sp.sqrt(2*u)
W = (-sp.diff(u,k2), sp.diff(u,k1))
print("W.grad w =", sp.simplify(W[0]*sp.diff(w,k1)+W[1]*sp.diff(w,k2)))
JW = sp.Matrix([[sp.diff(W[i],v) for v in (k1,k2)] for i in range(2)])
for name,pt in [("Gamma",(0,0)),("X",(sp.pi,0)),("X'",(0,sp.pi)),("M",(sp.pi,sp.pi))]:
    J0 = JW.subs({k1:pt[0],k2:pt[1]})
    ev = list(J0.eigenvals().keys())
    print(f"  zero at {name}: linearization eigenvalues {ev} ->", "hyperbolic (boost-like)" if all(e.is_real for e in ev) else "elliptic (rotation)")
# orbit periods
mm = 1.0
def Wf(t,y):
    return [-np.sin(y[1]), np.sin(y[0])]
def period(y0):
    # integrate until angle around Gamma (or M) winds once: use return to y0 crossing
    def ev(t,y): return y[1]-y0[1] if t>1e-3 else 1.0
    ev.direction = 1
    sol = solve_ivp(Wf, [0, 2000], y0, events=ev, rtol=1e-11, atol=1e-12, max_step=0.05)
    ts = sol.t_events[0]
    return ts[0] if len(ts) else np.inf
print("  orbit through (k,0): E = sqrt(m^2+2(1-cos k)) ; period T ; T/2pi - 1 ; ~ k^2/8 ?")
for kv in [0.05, 0.2, 0.5, 1.0, 2.0, 3.0, 3.1, 3.14]:
    T = period([kv, 0.0])
    print(f"   k={kv:5.2f}  T={T:10.4f}  T/2pi-1={T/(2*np.pi)-1:+.3e}  k^2/8={kv**2/8:.3e}")

print("\n=== (b) d=2: undeformed rotation acting on a vector momentum P ===")
def make_p(c):
    # odd, C4-covariant vector field: p_1(k1,k2) = sum c_j * basis_j, p_2 = p_1(k2,-k1) rotated
    def p1(a,b):
        return (np.sin(a) + c[0]*np.sin(a)*np.cos(b) + c[1]*np.sin(2*a) + c[2]*np.sin(a)*np.cos(2*b)
                + c[3]*np.sin(2*a)*np.cos(b) + c[4]*np.sin(b)*np.cos(a)*0)  # (last term killed to keep p ~ k)
    def p(a,b):
        # C4: R(k1,k2)=(-k2,k1); covariance p(Rk) = R p(k) => p_2(k1,k2) = p_1(k2,-k1)
        return np.array([p1(a,b), p1(b,-a)])
    return p
g = np.linspace(-np.pi, np.pi, 801)[:-1]
A,B = np.meshgrid(g,g,indexing='ij')
for trial in range(5):
    c = rng.normal(0,0.35,5) if trial>0 else np.zeros(5)
    p = make_p(c)
    h = 1e-5
    P = p(A,B)
    D11 = (p(A+h,B)[0]-p(A-h,B)[0])/(2*h); D12 = (p(A,B+h)[0]-p(A,B-h)[0])/(2*h)
    D21 = (p(A+h,B)[1]-p(A-h,B)[1])/(2*h); D22 = (p(A,B+h)[1]-p(A,B-h)[1])/(2*h)
    det = D11*D22-D12*D21
    # adj(Dp) J p, J p = (-p2, p1)
    Jp = np.array([-P[1], P[0]])
    adj = np.array([D22*Jp[0]-D12*Jp[1], -D21*Jp[0]+D11*Jp[1]])
    # fold: sign change of det between grid neighbours
    fold = (np.sign(det)!=np.sign(np.roll(det,1,0)))|(np.sign(det)!=np.sign(np.roll(det,1,1)))
    nadj = np.hypot(*adj)
    # zeros of p: Newton from grid minima
    zs = []
    idx = np.argwhere(np.hypot(*P) < 0.05)
    for i,j in idx[::7]:
        sol = root(lambda y: p(y[0],y[1]), [A[i,j],B[i,j]], tol=1e-13)
        if sol.success:
            z = (np.mod(sol.x+np.pi, 2*np.pi)-np.pi)
            if not any(np.linalg.norm(np.mod(z-q+np.pi,2*np.pi)-np.pi)<1e-6 for q in zs): zs.append(z)
    degs = []
    for z in zs:
        y=z; Dz = np.array([[(p(y[0]+h,y[1])[i]-p(y[0]-h,y[1])[i])/(2*h) for i in range(2)],[(p(y[0],y[1]+h)[i]-p(y[0],y[1]-h)[i])/(2*h) for i in range(2)]]).T
        degs.append(int(np.sign(np.linalg.det(Dz))))
    print(f"trial {trial}: zeros of p: {len(zs)}, degree signs sum = {sum(degs)} (list {degs});  fold cells = {fold.sum()};  fraction of fold cells with |adj(Dp)Jp|>0.05 (no W exists there) = {np.mean(nadj[fold]>0.05):.3f}")

print("\n=== (c) lapse-smearing (first-moment) algebra: double points of (H,P=grad u) ===")
def cubic_u(d, c, m=1.0):
    # cubic-invariant u = m^2/2 + sum of invariant cos-harmonics with coefficients c (nearest neighbour fixed = 1)
    def u(k):
        k = np.asarray(k)
        cs = np.cos(k); c2 = np.cos(2*k)
        t1 = np.sum(1-cs, axis=0)
        t2 = sum(1-cs[i]*cs[j] for i in range(d) for j in range(i+1,d))
        t3 = np.sum(1-c2, axis=0)
        t4 = (1-np.prod(cs,axis=0))
        return m**2/2 + t1 + c[0]*t2 + c[1]*t3 + c[2]*t4
    return u
def grad_hess(u, k, h=1e-4):
    d = len(k); g = np.zeros(d); Hs = np.zeros((d,d))
    for i in range(d):
        e = np.zeros(d); e[i]=h
        g[i] = (u(k+e)-u(k-e))/(2*h)
        for j in range(d):
            f = np.zeros(d); f[j]=h
            Hs[i,j] = (u(k+e+f)-u(k+e-f)-u(k-e+f)+u(k-e-f))/(4*h*h)
    return g,Hs
def rotations(d):
    if d==2:
        R = np.array([[0,-1],[1,0]])
        return [np.linalg.matrix_power(R,n) for n in range(4)]
    mats=[]
    for perm in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M = np.zeros((3,3))
            for i in range(3): M[i,perm[i]] = s[i]
            if abs(np.linalg.det(M)-1)<1e-9: mats.append(M)
    return mats
for d in (2,3):
    Rs = rotations(d)
    for trial in range(4):
        c = rng.normal(0,0.15,3) if trial>0 else np.zeros(3)
        u = cubic_u(d,c)
        # critical points: Newton from a grid
        n = 16 if d==2 else 10
        gr = np.linspace(-np.pi,np.pi,n,endpoint=False)
        crit=[]
        for kk in itertools.product(gr,repeat=d):
            sol = root(lambda y: grad_hess(u,y)[0], np.array(kk), tol=1e-12)
            if sol.success and np.linalg.norm(grad_hess(u,sol.x)[0])<1e-8:
                z = np.mod(sol.x+np.pi,2*np.pi)-np.pi
                z[np.abs(np.abs(z)-np.pi)<1e-6] = np.pi
                if not any(np.linalg.norm(np.mod(z-q+np.pi,2*np.pi)-np.pi)<1e-5 for q in crit): crit.append(z)
        idxs=[]; worst=0; nviol=0; ncrit=len(crit); morse=True
        for z in crit:
            _,Hs = grad_hess(u,z); ev = np.linalg.eigvalsh(Hs)
            if np.min(np.abs(ev))<1e-5: morse=False
            idxs.append(int(np.sum(ev<0)))
            # orbit partners with the same (H,P=0): compare Hessians
            for R in Rs:
                z2 = np.mod(R@z+np.pi,2*np.pi)-np.pi
                if np.linalg.norm(np.mod(z2-z+np.pi,2*np.pi)-np.pi) > 1e-6:
                    _,H2 = grad_hess(u,z2)
                    diff = np.linalg.norm(Hs-H2)
                    if diff>1e-6: nviol+=1; worst=max(worst,diff)
        hist = {i:idxs.count(i) for i in sorted(set(idxs))}
        print(f"d={d} trial {trial}: critical points {ncrit}, Morse={morse}, index histogram {hist}, "
              f"orbit-partner pairs with same (H,P=0) but different Hess u: {nviol} (max |dHess| {worst:.3f})")
# van Hove line collisions for the d=2 KG
print("  d=2 KG van Hove line: k=(a, pi-a) vs k'=(pi-a, a)... use (k1,k2) and (pi-k1, pi-k2) with cos k1 = -cos k2")
for a in [0.3, 0.8, 1.2]:
    ka = np.array([a, np.pi-a]); kb = np.array([np.pi-a, a])   # cos ka1 = cos a, cos ka2 = -cos a
    kb = np.array([np.pi-ka[0], np.pi-ka[1]])
    uu = cubic_u(2,np.zeros(3))
    ga,Ha = grad_hess(uu,ka); gb,Hb = grad_hess(uu,kb)
    print(f"   a={a}: dw={np.sqrt(2*uu(ka))-np.sqrt(2*uu(kb)):+.1e}  |dP|={np.linalg.norm(ga-gb):.1e}  Hess(k)=diag{np.round(np.diag(Ha),4)}  Hess(k')=diag{np.round(np.diag(Hb),4)}")

print("\n=== (d) d=3 KG first-moment rotations: do L_ab close so(3)? ===")
k = sp.symbols('k1:4', real=True)
U = (m**2 + 2*sum(1-sp.cos(x) for x in k))/2
du = [sp.diff(U,x) for x in k]
def L(a,b):  # vector field components
    v=[sp.Integer(0)]*3; v[b]+=du[a]; v[a]-=du[b]; return v
def bracket(X,Y):
    return [sp.simplify(sum(X[j]*sp.diff(Y[i],k[j]) - Y[j]*sp.diff(X[i],k[j]) for j in range(3))) for i in range(3)]
Bk = bracket(L(0,1), L(1,2))
target = L(0,2)
print("  [L12,L23] =", Bk, "  L13 =", target)
print("  [L12,L23] - cos(k2)*L13 =", [sp.simplify(Bk[i]-sp.cos(k[1])*target[i]) for i in range(3)])
# test: Bk = c*L(0,2) for a constant c? evaluate ratio at points
pts = [(0.1,0.2,0.3),(1.0,0.5,0.2),(2.0,1.0,0.4)]
for pt in pts:
    sub = dict(zip(k,pt))
    bv = np.array([float(x.subs(sub)) for x in Bk]); tv = np.array([float(x.subs(sub)) for x in target])
    # residual after best scalar fit
    cfit = bv@tv/(tv@tv); res = np.linalg.norm(bv-cfit*tv)/np.linalg.norm(bv)
    print(f"   at k={pt}: best scalar c={cfit:+.4f}, relative residual {res:.3e}; [L12,L23] tangent to level set of u: {abs(sum(bv[i]*float(du[i].subs(sub)) for i in range(3))):.1e}")

print("\n=== (e) orbit-average sum rule along a random non-first-moment boost flow, d=2 ===")
cc = rng.normal(0,0.3,4)
def wfun(y): return np.sqrt(1.0 + 2*(2-np.cos(y[0])-np.cos(y[1])))
def V1(y):
    a,b = y
    f = wfun(y)*(1 + cc[0]*(1-np.cos(a)) + cc[1]*(1-np.cos(b)))
    return np.array([f*(1+0.1*cc[2]*np.cos(b)), cc[3]*0.3*np.sin(a)*np.sin(b)])
def rhs(t,y): return V1(y)
for S in [10, 100, 1000]:
    sol = solve_ivp(rhs,[0,S],[0.0,0.0],rtol=1e-10,atol=1e-12,dense_output=True,max_step=0.05)
    ts = np.linspace(0,S,200001); Y = sol.sol(ts)
    Hs = np.array([wfun(Y[:,i]) for i in range(0,len(ts))])
    dH = np.gradient(Hs,ts); d2H = np.gradient(dH,ts)
    print(f"   S={S:5d}: <F_11>_orbit = <d^2H/ds^2> = {np.trapezoid(d2H,ts)/S:+.3e};  F_11 at rest = {d2H[5]:+.4f};  min F_11 on orbit = {d2H.min():+.4f};  H range [{Hs.min():.3f},{Hs.max():.3f}]")
