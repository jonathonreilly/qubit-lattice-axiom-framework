"""C2: Kitaev honeycomb energy current in the Majorana representation, all flux sectors.

H = sum_bonds J_a s^a_j s^a_k  ->  (i/4) c^T A c,  A_jk = 2 J_a u_jk (j in A, k in B), A antisymmetric.
Spin energy densities h_b (bond terms) map to bilinears with bond matrices M_b.
Energy current (x component), single-particle matrix:
   B = sum_site sum_{b,b' touching site} (m_b'^x - m_b^x) [M_b, M_b']      (overall factor irrelevant)
The total current operator is conserved in sector s iff [A_s, B_s] = 0.
Drude ratio at Majorana temperature beta (ratio of ensemble sums):
   r = sum_{lam~mu} |K_lm|^2 w(lam,mu) / sum_{lam,mu} |K_lm|^2 w(lam,mu),  K = B in eigenbasis of iA,
   w = f(lam)(1-f(mu)), f = Fermi function of the eigenvalue lam of iA (H = sum eps (n-1/2)).
At beta = 0 this is ||Bbar||^2/||B||^2 with Bbar the time average (projection on the commutant of A).
Fact used (proved in report): r(L) is exactly L-independent once L exceeds the support, if a local
conserved improved current J + i[H,B'] != 0 exists; decay of r(L) excludes every local improvement.
"""
import numpy as np, sys
rng = np.random.default_rng(12345)
s3 = np.sqrt(3.0)
a1 = np.array([1.0, 0.0]); a2 = np.array([0.5, s3/2])
dB = np.array([0.0, 1/s3])

def build(L, J=(1.0, 1.0, 1.0), u=None):
    N = 2*L*L
    idx = lambda x, y, s: 2*(((x % L)*L) + (y % L)) + s
    bonds = []  # (j in A, k in B, type, vector from A to B)
    for x in range(L):
        for y in range(L):
            jA = idx(x, y, 0)
            # z bond: B(x,y); x bond: B(x+1,y-1); y bond: B(x,y-1)
            bonds.append((jA, idx(x, y, 1), 2, dB))
            bonds.append((jA, idx(x+1, y-1, 1), 0, a1 - a2 + dB))
            bonds.append((jA, idx(x, y-1, 1), 1, -a2 + dB))
    nb = len(bonds)
    if u is None:
        u = np.ones(nb)
    A = np.zeros((N, N))
    Ms = []
    for b, (j, k, t, v) in enumerate(bonds):
        val = 2*J[t]*u[b]
        A[j, k] += val; A[k, j] -= val
        Ms.append((j, k, val))
    # current: for each site, bonds touching it, midpoint relative to that site
    touch = [[] for _ in range(N)]
    for b, (j, k, t, v) in enumerate(bonds):
        touch[j].append((b, +0.5*v))   # midpoint relative to A site
        touch[k].append((b, -0.5*v))   # midpoint relative to B site
    B = np.zeros((N, N))
    def Mmat(b):
        j, k, val = Ms[b]
        M = np.zeros((N, N)); M[j, k] = val; M[k, j] = -val
        return M
    for s in range(N):
        for (b, mb) in touch[s]:
            for (bp, mbp) in touch[s]:
                if b == bp: continue
                d = mbp[0] - mb[0]
                # [M_b, M_b'] restricted: compute via small sparse product
                j, k, v1 = Ms[b]; jp, kp, v2 = Ms[bp]
                # build commutator entries explicitly (only 3 sites involved)
                sites = sorted(set([j, k, jp, kp]))
                P = np.zeros((len(sites), len(sites))); Q = np.zeros_like(P)
                pos = {q: i for i, q in enumerate(sites)}
                P[pos[j], pos[k]] = v1; P[pos[k], pos[j]] = -v1
                Q[pos[jp], pos[kp]] = v2; Q[pos[kp], pos[jp]] = -v2
                C = P@Q - Q@P
                for a_, sa in enumerate(sites):
                    for b_, sb in enumerate(sites):
                        B[sa, sb] += d*C[a_, b_]
    return A, B, bonds

def fluxes(L, bonds, u):
    # plaquette flux W_p = product of u around hexagon (sign only); hexagon around cell (x,y): use
    # the 6 bonds; easier: compute via A matrix loop product. Use A-site (x,y) and neighbours.
    # hexagon sites: A(x,y) -zb- B(x,y) -xb- A(x-1,y+1) -zb- B(x-1,y+1)... we just count via gauge-invariant loops:
    bmap = {}
    for b, (j, k, t, v) in enumerate(bonds):
        bmap[(j, k)] = b
    idx = lambda x, y, s: 2*(((x % L)*L) + (y % L)) + s
    W = []
    for x in range(L):
        for y in range(L):
            # hexagon: A(x,y)->B(x,y) [z], B(x,y)<-A(x-1,y+1) [x bond of A(x-1,y+1): B(x,y)], A(x-1,y+1)->B(x-1,y) [y bond],
            # B(x-1,y)<-A(x-1,y) [z], A(x-1,y)->B(x,y-1) [x bond], B(x,y-1)<-A(x,y) [y bond]
            loop = [(idx(x,y,0), idx(x,y,1)), (idx(x-1,y+1,0), idx(x,y,1)), (idx(x-1,y+1,0), idx(x-1,y,1)),
                    (idx(x-1,y,0), idx(x-1,y,1)), (idx(x-1,y,0), idx(x,y-1,1)), (idx(x,y,0), idx(x,y-1,1))]
            p = 1.0
            for e in loop:
                p *= u[bmap[e]]
            W.append(p)
    return np.array(W)

def drude_ratio(A, B, betas=(0.0,), tol=1e-8):
    w, V = np.linalg.eigh(1j*A)       # eigenvalues lam of iA (pairs +-eps)
    K = V.conj().T @ (1j*B) @ V
    K2 = np.abs(K)**2
    same = np.abs(w[:, None] - w[None, :]) < tol*max(1.0, np.max(np.abs(w)))
    out = []
    for beta in betas:
        f = 1.0/(np.exp(beta*w) + 1.0)
        W = f[:, None]*(1 - f[None, :])
        out.append(np.sum(K2*W*same)/np.sum(K2*W))
    comm = np.linalg.norm(A@B - B@A)/(np.linalg.norm(A)*np.linalg.norm(B))
    return out, comm

if __name__ == "__main__":
    betas = (0.0, 1.0, 3.0)
    print("Kitaev honeycomb, isotropic J=1, Majorana per flux sector. r = Drude ratio (ensemble sums), beta = Majorana inverse T")
    print("columns: L  sector  flux_density  ||[A,B]||/(||A||||B||)  r(beta=0)  r(beta=1)  r(beta=3)   [mean +- sem over samples]")
    for L in [4, 6, 8, 12, 16, 20, 24]:
        A, B, bonds = build(L)
        rs, c = drude_ratio(A, B, betas)
        print(f"L={L:3d} uniform(0-flux)  rho=0.000  comm={c:.2e}  r=" + " ".join(f"{x:.4f}" for x in rs), flush=True)
        nb = len(bonds)
        for label, q in [("random u (beta=0 all sectors)", 0.5), ("dilute flips q=0.05", 0.05), ("dilute flips q=0.01", 0.01)]:
            nsamp = 12 if L <= 12 else (6 if L <= 16 else 3)
            R = []; C = []; RH = []
            for sidx in range(nsamp):
                u = np.where(rng.random(nb) < q, -1.0, 1.0)
                Au, Bu, _ = build(L, u=u)
                rs, c = drude_ratio(Au, Bu, betas)
                R.append(rs); C.append(c); RH.append(np.mean(fluxes(L, bonds, u) < 0))
            R = np.array(R)
            m = R.mean(0); e = R.std(0)/np.sqrt(len(R))
            print(f"L={L:3d} {label:30s} rho={np.mean(RH):.3f}  comm={np.mean(C):.2e}  r=" +
                  " ".join(f"{mm:.4f}+-{ee:.4f}" for mm, ee in zip(m, e)), flush=True)
