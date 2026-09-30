"""B2: block 56's second bond energy F2 = sum_bonds (w_x-w_y)^2/(w_x+w_y) (gamma = 1), one body of
bare energy m at the centre of an L^3 box (walls w=1).  Parameterise by the body's rate w0:
for each w0 the empty-site equations are the stationarity of a CONVEX energy (perspective of t^2),
so they have a unique positive solution; then m(w0) = -sum_y g(w0, w_y),
g(a,b) = (a-b)(a+3b)/(a+b)^2 = 1 - 4 b^2/(a+b)^2.  Prediction: m -> 18 as w0 -> 0 and
(18-m)/w0 -> 8 sum_y 1/w_y."""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl, json, sys

def make(L):
    c = (L - 1) // 2
    idx = np.arange(L)
    X, Y, Z = np.meshgrid(idx, idx, idx, indexing="ij")
    wall = (X == 0) | (X == L-1) | (Y == 0) | (Y == L-1) | (Z == 0) | (Z == L-1)
    n = L**3
    centre = c*L*L + c*L + c
    free = np.flatnonzero((~wall).reshape(-1)); free = free[free != centre]
    fid = -np.ones(n, dtype=int); fid[free] = np.arange(len(free))
    shifts = [L*L, -L*L, L, -L, 1, -1]
    return dict(L=L, c=c, n=n, centre=centre, free=free, fid=fid, shifts=shifts)

def energy(W, L):
    W3 = W.reshape(L, L, L); F = 0.0
    for ax in range(3):
        a = np.take(W3, range(0, L-1), axis=ax); b = np.take(W3, range(1, L), axis=ax)
        F += np.sum((a-b)**2/(a+b))
    return F

def grad_hess(W, G, need_H=True):
    free, fid, shifts = G["free"], G["fid"], G["shifts"]
    a = W[free]; g = np.zeros(len(free)); diag = np.zeros(len(free))
    rows, cols, vals = [], [], []
    for s in shifts:
        nb = free + s; b = W[nb]
        g += 1 - 4*b*b/(a+b)**2
        if need_H:
            diag += 8*b*b/(a+b)**3
            isf = fid[nb] >= 0
            rows.append(fid[free][isf]); cols.append(fid[nb][isf]); vals.append(-8*a[isf]*b[isf]/(a[isf]+b[isf])**3)
    if not need_H: return g
    H = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(len(free),)*2) + sp.diags(diag)
    return g, H

def solve_field(W, G, tol=1e-11, maxit=60):
    free = G["free"]; L = G["L"]
    for it in range(maxit):
        g, H = grad_hess(W, G)
        gn = np.max(np.abs(g))
        if gn < tol: return W, it, gn
        Dinv = 1.0 / H.diagonal()
        M = spl.LinearOperator(H.shape, matvec=lambda x: Dinv * x)
        d, info = spl.cg(H, -g, rtol=1e-10, atol=0, maxiter=4000, M=M)
        F0 = energy(W, L); t = 1.0
        while True:
            Wn = W.copy(); Wn[free] = W[free] + t*d
            if np.all(Wn[free] > 0.2*W[free]) and energy(Wn, L) <= F0 + 1e-14*abs(F0): break
            t *= 0.5
            if t < 1e-12: return W, it, gn
        W = Wn
    return W, maxit, gn

if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 41
    G = make(L)
    W = np.ones(G["n"])
    rows = []
    print(f"L={L}; gamma=1, 18/gamma=18.  w0 -> m(w0) = -sum g(w0,w_y);  ratio = (18-m)/w0 versus 8 sum 1/w_y")
    print("      w0          m        18-m     (18-m)/w0   8*sum(1/w_y)   min_neighbour_w   newton_it  |grad|")
    for w0 in [0.9,0.7,0.5,0.35,0.25,0.15,0.1,0.06,0.03,0.015,0.008,0.004,0.002,0.001,5e-4,2e-4,1e-4,1e-5,1e-6]:
        W[G["centre"]] = w0
        W, it, gn = solve_field(W, G)
        nb = np.array([W[G["centre"] + s] for s in G["shifts"]])
        m = -np.sum(1 - 4*nb*nb/(w0+nb)**2)
        pred = 8*np.sum(1/nb)
        print(f" {w0:10.2e} {m:10.5f} {18-m:10.5f} {(18-m)/w0:12.4f} {pred:12.4f} {nb.min():14.5f} {it:7d}  {gn:8.1e}")
        rows.append(dict(w0=w0, m=float(m), deficit=float(18-m), ratio=float((18-m)/w0), pred=float(pred), nbmin=float(nb.min())))
    json.dump(rows, open(f"B2_results_L{L}.json", "w"), indent=1)
