"""GUIDE run for row 1113 (check of row 1109, Example Q8-INF). Refutes or guides only.
Two Q_8 nearest-neighbour models on a periodic strip of width L, transfer matrix in time:
  'inf': one sheet at beta_L = infinity, bond weight phi(q) = exp(b Re q);
  'zero': the rho model at beta_L = 0, bond weight f(q) = (1/8) sum_a phi(a) phi(a q).
Sector: functions of the row invariant under r_x -> c r_x k (all x), c, k in Q_8.
(For 'inf' this is the K-neutral, gauge-invariant sector of one sheet; for 'zero' it is the
K-neutral sector of rho, on which K acts by rho -> k1^(-1) rho k2.)
Output: gap m = log(lam0/lam1) in that sector, for each b and L.
Usage: python3 -I q8strip.py   (adds the user site path for numpy; one BLAS thread set by caller)
"""
import sys, math, itertools
import site; sys.path.append(site.getusersitepackages())
import numpy as np

# Q_8 as unit quaternions (w, x, y, z)
E = [(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0), (0,0,1,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1)]
def qmul(p, q):
    a1,b1,c1,d1 = p; a2,b2,c2,d2 = q
    return (a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2, a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2)
IDX = {e: i for i, e in enumerate(E)}
MUL = np.array([[IDX[qmul(E[a], E[b])] for b in range(8)] for a in range(8)])
INV = np.array([IDX[(E[a][0], -E[a][1], -E[a][2], -E[a][3])] for a in range(8)])
RE = np.array([E[a][0] for a in range(8)], dtype=float)
assert all(MUL[a, INV[a]] == 0 for a in range(8))

def weights(model, b):
    phi = np.exp(b * (RE - 1.0))            # phi(q)/phi(1)
    if model == 'inf':
        w = phi
    else:
        w = np.array([sum(math.exp(b*(RE[a] + RE[MUL[a, q]])) for a in range(8)) for q in range(8)])
        w = w / w[0]
    return w

def rows(L):
    R = np.array(list(itertools.product(range(8), repeat=L)), dtype=np.int64)
    return R

def index(R):
    L = R.shape[1]
    return (R * (8 ** np.arange(L - 1, -1, -1))).sum(axis=1)

def orbits(R):
    best = index(R).copy()
    for c in range(8):
        for k in range(8):
            img = MUL[MUL[c, R], k]
            best = np.minimum(best, index(img))
    reps, oid, size = np.unique(best, return_inverse=True, return_counts=True)
    return reps, oid, size

def reduced(model, b, L, R, reps, oid, size):
    w = weights(model, b)
    # horizontal (periodic) factor H(r) = prod_x w(r_x^(-1) r_(x+1))
    H = np.ones(len(R))
    for x in range(L):
        H *= w[MUL[INV[R[:, x]], R[:, (x + 1) % L]]]
    sH = np.sqrt(H)
    n = len(reps)
    M = np.zeros((n, n))
    for a, ra in enumerate(reps):
        r = R[ra]
        vec = np.ones(1)
        for x in range(L):
            vx = w[MUL[INV[r[x]], np.arange(8)]]
            vec = np.kron(vec, vx)
        vec = vec * sH[ra] * sH
        row = np.bincount(oid, weights=vec, minlength=n)
        M[a, :] = np.sqrt(size[a] / size) * row
    return M

def gap(M):
    Ms = 0.5 * (M + M.T)
    asym = np.abs(M - M.T).max() / np.abs(M).max()
    ev = np.linalg.eigvalsh(Ms)
    return math.log(ev[-1] / ev[-2]), asym

def fullcheck(model, b, L):
    R = rows(L); N = len(R)
    w = weights(model, b)
    H = np.ones(N)
    for x in range(L):
        H *= w[MUL[INV[R[:, x]], R[:, (x + 1) % L]]]
    V = np.ones((N, N))
    for x in range(L):
        V *= w[MUL[INV[R[:, x]][:, None], R[:, x][None, :]]]
    T = np.sqrt(H)[:, None] * V * np.sqrt(H)[None, :]
    P = np.zeros((N, N))
    ix = index(R)
    for c in range(8):
        for k in range(8):
            img = index(MUL[MUL[c, R], k])
            P[img, ix] += 1.0 / 64
    ev = np.linalg.eigvalsh(P @ T @ P)
    ev = ev[np.abs(ev) > 1e-12 * ev.max()]
    return math.log(ev[-1] / ev[-2])

if __name__ == '__main__':
    print("# check: full projected T vs orbit-reduced T, L = 3")
    R = rows(3); reps, oid, size = orbits(R)
    for model in ('inf', 'zero'):
        for b in (2.4, 6.0):
            g1 = fullcheck(model, b, 3); g2, asym = gap(reduced(model, b, 3, R, reps, oid, size))
            print(f"  {model:4s} b {b:4.1f}  full {g1:.10f}  reduced {g2:.10f}  asym {asym:.1e}")
    bs = [2.4, 3.0, 4.0, 6.0, 8.0, 10.0, 12.0]
    for L in (3, 4, 5):
        R = rows(L); reps, oid, size = orbits(R)
        print(f"# L {L}  rows {len(R)}  orbits {len(reps)}")
        for b in bs:
            gi, ai = gap(reduced('inf', b, L, R, reps, oid, size))
            gz, az = gap(reduced('zero', b, L, R, reps, oid, size))
            print(f"  b {b:5.1f}  m_inf {gi:10.6f} (2b {2*b:6.2f})  m_0 {gz:10.6f} (2b-2log2 {2*b-2*math.log(2):8.4f})  m_0 - m_inf {gz-gi:+9.5f}  asym {max(ai,az):.0e}")
