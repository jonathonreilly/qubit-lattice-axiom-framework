"""Independent reproduction: simplicial Laplacian + Regge action on Kuhn-triangulated T^4.
Everything derived from squared edge lengths only.  No external lane code consulted.
"""
import itertools, math
import numpy as np

PERMS = list(itertools.permutations(range(4)))

def kuhn_offsets():
    out = []
    for pi in PERMS:
        w = np.zeros((5,4), dtype=int)
        for j in range(1,5):
            w[j] = w[j-1]
            w[j][pi[j-1]] += 1
        out.append(w)
    return np.array(out)          # (24,5,4)

W = kuhn_offsets()

# ---------- metric: g_{mu nu}(x) = delta_{mu nu} (1 + eps P_mu cos(k x_0)) ----------
def gdiag(x0, eps, P, k):
    return 1.0 + eps*np.asarray(P,dtype=float)*math.cos(k*x0)

def edge_l2(p0, w, a, b, eps, P, k):
    """squared length of edge (a,b) of the Kuhn simplex based at x_0=p0.
    midpoint evaluation of g on the straight coordinate segment."""
    d = w[b]-w[a]
    x0mid = p0 + 0.5*(w[a][0]+w[b][0])
    gd = gdiag(x0mid, eps, P, k)
    return float(np.sum((d*d)*gd))

def simplex_geometry(p0, wi, eps, P, k):
    """Return (V, K5 (5x5 stiffness), Gtil (5x5 inner products of e_a=v_a-v_0))."""
    w = W[wi]
    l2 = np.zeros((5,5))
    for a in range(5):
        for b in range(a+1,5):
            v = edge_l2(p0,w,a,b,eps,P,k)
            l2[a,b] = v; l2[b,a] = v
    G = np.empty((4,4))
    for a in range(1,5):
        for b in range(1,5):
            G[a-1,b-1] = 0.5*(l2[0,a]+l2[0,b]-l2[a,b])
    detG = np.linalg.det(G)
    V = math.sqrt(detG)/math.factorial(4)
    Ginv = np.linalg.inv(G)
    K4 = V*Ginv
    K5 = np.zeros((5,5))
    K5[1:,1:] = K4
    K5[0,1:] = -K4.sum(axis=0)
    K5[1:,0] = -K4.sum(axis=1)
    K5[0,0]  = K4.sum()
    Gtil = np.zeros((5,5)); Gtil[1:,1:] = G
    return V, K5, Gtil, l2

def ip(Gtil, a,b,c,d):
    """<v_a - v_b , v_c - v_d>"""
    return Gtil[a,c]-Gtil[a,d]-Gtil[b,c]+Gtil[b,d]

HINGES = []   # (i,j,k, l,m)
for tri in itertools.combinations(range(5),3):
    rest = tuple(sorted(set(range(5))-set(tri)))
    HINGES.append((tri, rest))

def hinge_area_angle(Gtil, tri, rest):
    i,j,kk = tri; l,m = rest
    T = np.array([[ip(Gtil,j,i,j,i), ip(Gtil,j,i,kk,i)],
                  [ip(Gtil,kk,i,j,i), ip(Gtil,kk,i,kk,i)]])
    area = 0.5*math.sqrt(max(np.linalg.det(T),0.0))
    cu = np.array([ip(Gtil,j,i,l,i), ip(Gtil,kk,i,l,i)])
    cw = np.array([ip(Gtil,j,i,m,i), ip(Gtil,kk,i,m,i)])
    Ti = np.linalg.inv(T)
    uu = ip(Gtil,l,i,l,i) - cu@Ti@cu
    ww = ip(Gtil,m,i,m,i) - cw@Ti@cw
    uw = ip(Gtil,l,i,m,i) - cu@Ti@cw
    c = uw/math.sqrt(uu*ww)
    c = min(1.0,max(-1.0,c))
    return area, math.acos(c)
