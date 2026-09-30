"""M2: pi-flux cubic sea on an LxLxL torus, APBC, staggered mass m; planar slab region
{(h x + k y + l z) mod L in [0, L/2)}; eta = S_A/(2*L^2*sqrt(h^2+k^2+l^2))."""
import numpy as np, sys, time, itertools
def build(L, m):
    N = L**3
    idx = lambda x,y,z: ((x%L)*L + (y%L))*L + (z%L)
    H = np.zeros((N,N))
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = idx(x,y,z)
                H[i,i] += m*(-1)**(x+y+z)
                # +x bond, eta=1, APBC sign on wrap
                s = -1.0 if x==L-1 else 1.0
                j = idx(x+1,y,z); H[i,j] += s; H[j,i] += s
                s = (-1.0)**x * (-1.0 if y==L-1 else 1.0)
                j = idx(x,y+1,z); H[i,j] += s; H[j,i] += s
                s = (-1.0)**(x+y) * (-1.0 if z==L-1 else 1.0)
                j = idx(x,y,z+1); H[i,j] += s; H[j,i] += s
    return H
def S_of_corr(C):
    nu = np.linalg.eigvalsh(C)
    nu = np.clip(nu, 1e-14, 1-1e-14)
    return float(-np.sum(nu*np.log(nu)+(1-nu)*np.log(1-nu)))
def run(L, m, orients, check=False):
    H = build(L,m)
    E, V = np.linalg.eigh(H)
    if check:
        ks = 2*np.pi*(np.arange(L//2)+0.5)/L
        ref = []
        for a,b,c in itertools.product(ks,ks,ks):
            e = np.sqrt(4*(np.cos(a)**2+np.cos(b)**2+np.cos(c)**2)+m*m)
            ref += [e]*4 + [-e]*4
        ref = np.sort(ref)
        print("  spectrum check max|E-ref| =", np.max(np.abs(np.sort(E)-ref)), " min|E| =", np.min(np.abs(E)))
    occ = V[:, E<0]
    assert occ.shape[1] == L**3//2, occ.shape
    P = occ @ occ.T
    out = {}
    X,Y,Z = np.meshgrid(np.arange(L),np.arange(L),np.arange(L),indexing='ij')
    for (h,k,l) in orients:
        q = (h*X + k*Y + l*Z) % L
        sel = np.where((q < L//2).ravel())[0]
        S = S_of_corr(P[np.ix_(sel,sel)])
        area = L*L*np.sqrt(h*h+k*k+l*l)
        out[(h,k,l)] = S/(2*area)
    return out
if __name__ == "__main__":
    L = int(sys.argv[1]); m = float(sys.argv[2])
    t = time.time()
    res = run(L, m, [(1,0,0),(1,1,0),(1,1,1)], check=(L<=8))
    print(f"L={L} m={m}", {k: round(v,5) for k,v in res.items()}, f"({time.time()-t:.1f}s)")
