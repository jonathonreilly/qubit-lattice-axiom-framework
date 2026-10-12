# O3 part 2: Fendley-Schoutens-de Boer M1 lattice supersymmetry on one fermion mode (one M_2(C)) per site.
#   Q(eps) = sum_i c_i^dag B_i(eps),  B_i = prod_{j in N1(i)} (1-n_j) * exp(eps*(sum_{j in N2x(i)} n_j - sum_{j in N2y(i)} n_j))
#   (nilpotent for any symmetric dressing; eps is an E_g-odd (x<->y antisymmetric) local deformation)
#   H(eps) = {Q(eps), Q(eps)^dag}.
# Checks: Q^2 = 0; E0(eps) = 0 for all eps when Witten index W != 0; exact Q-doublet pairing of the
# spectrum between fermion-number sectors F and F+1; comparison with a "naive" strain applied to H
# directly (x-hops * e^eps, y-hops * e^-eps), which is not of {Q,Q^dag} form.
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, sys, time

def torus(Lx, Ly):
    N = Lx*Ly; idx = lambda x,y: (x%Lx) + Lx*(y%Ly)
    N1 = [set() for _ in range(N)]; N2x = [set() for _ in range(N)]; N2y = [set() for _ in range(N)]
    dirx = {}
    for x in range(Lx):
        for y in range(Ly):
            i = idx(x,y)
            for d in (1,-1):
                if Lx > 1: N1[i].add(idx(x+d,y)); dirx[(i, idx(x+d,y))] = 'x'
                if Ly > 1: N1[i].add(idx(x,y+d)); dirx[(i, idx(x,y+d))] = 'y'
                if Lx > 2: N2x[i].add(idx(x+2*d,y))
                if Ly > 2: N2y[i].add(idx(x,y+2*d))
    for i in range(N):
        N1[i].discard(i); N2x[i] -= N1[i] | {i}; N2y[i] -= N1[i] | {i}
    return N, N1, N2x, N2y, dirx

def indep_sets(N, N1):
    nbmask = [sum(1<<j for j in N1[i]) for i in range(N)]
    out = []
    def rec(i, s, forb):
        if i == N: out.append(s); return
        rec(i+1, s, forb)
        if not (forb >> i) & 1: rec(i+1, s | (1<<i), forb | nbmask[i])
    rec(0, 0, 0)
    return out

def build(N, N1, N2x, N2y, eps, states, index):
    rows, cols, vals = [], [], []
    for a, s in enumerate(states):
        for i in range(N):
            if (s>>i)&1: continue
            if any((s>>j)&1 for j in N1[i]): continue
            t = s | (1<<i)
            sign = -1.0 if bin(s & ((1<<i)-1)).count('1') % 2 else 1.0
            dress = np.exp(eps*(sum((s>>j)&1 for j in N2x[i]) - sum((s>>j)&1 for j in N2y[i])))
            rows.append(index[t]); cols.append(a); vals.append(sign*dress)
    D = len(states)
    Q = sp.csr_matrix((vals, (rows, cols)), shape=(D, D))
    H = (Q @ Q.T + Q.T @ Q).tocsr()
    return Q, H

def naive_strain(H0, states, dirx, eps):
    H = H0.tocoo(); v = H.data.copy()
    for k,(r,c) in enumerate(zip(H.row, H.col)):
        if r == c: continue
        d = states[r] ^ states[c]
        bits = [b for b in range(64) if (d>>b)&1]
        dd = dirx.get((bits[0], bits[1]), None)
        v[k] *= np.exp(eps) if dd == 'x' else np.exp(-eps)
    return sp.csr_matrix((v, (H.row, H.col)), shape=H.shape)

def run(Lx, Ly, dense=True, epss=(0.0, 0.05, 0.1, 0.2, 0.4)):
    t0 = time.time()
    N, N1, N2x, N2y, dirx = torus(Lx, Ly)
    states = indep_sets(N, N1); index = {s:a for a,s in enumerate(states)}
    F = np.array([bin(s).count('1') for s in states]); W = int(np.sum((-1)**F))
    print("\n=== %dx%d torus: N=%d sites, %d hard-core states, Witten index W = sdim = %d" % (Lx, Ly, N, len(states), W))
    for eps in epss:
        Q, H = build(N, N1, N2x, N2y, eps, states, index)
        q2 = abs(Q @ Q).max() if (Q@Q).nnz else 0.0
        if dense:
            ev = np.linalg.eigvalsh(H.toarray())
            nz0 = np.sum(np.abs(ev) < 1e-9)
            # pairing: singular values of Q from sector F to F+1 reproduce all nonzero levels
            pair_ok = True; maxdev = 0.0
            Hd = H.toarray(); Qd = Q.toarray()
            for f in range(F.max()+1):
                a = np.where(F==f)[0]; b = np.where(F==f+1)[0]
                if len(a)==0 or len(b)==0: continue
                sv = np.linalg.svd(Qd[np.ix_(b,a)], compute_uv=False)**2
                sv = np.sort(sv[sv>1e-9])
                # levels of Q^dag Q on sector f and Q Q^dag on sector f+1 coincide by construction; check against H spectra
                evf = np.sort(np.linalg.eigvalsh(Hd[np.ix_(a,a)])); evf1 = np.sort(np.linalg.eigvalsh(Hd[np.ix_(b,b)]))
                for lv in sv:
                    maxdev = max(maxdev, np.min(np.abs(evf-lv)), np.min(np.abs(evf1-lv)))
            print("  eps=%.2f  ||Q^2||=%.1e  E0=%.3e  #zero modes=%d  doublet-pairing max dev=%.1e  E1=%.5f" % (eps, q2, ev[0], nz0, maxdev, ev[nz0] if nz0 < len(ev) else np.nan))
        else:
            ev = sla.eigsh(H, k=4, which='SA', return_eigenvectors=False, tol=1e-12)
            print("  eps=%.2f  ||Q^2||=%.1e  lowest 4: %s" % (eps, q2, np.sort(ev)))
    # naive strain on H (not a {Q,Q^dag} deformation)
    Q0, H0 = build(N, N1, N2x, N2y, 0.0, states, index)
    h = 1e-3
    def e0(M):
        if dense: return np.linalg.eigvalsh(M.toarray())[0]
        return sla.eigsh(M, k=1, which='SA', return_eigenvectors=False, tol=1e-13)[0]
    Ep, E0, Em = e0(naive_strain(H0, states, dirx, h)), e0(H0), e0(naive_strain(H0, states, dirx, -h))
    print("  naive hop strain (x e^eps, y e^-eps): E0(0)=%.3e  E0''(0)/N = %.6e   E0(+-0.2) = %.4e, %.4e" %
          (E0, (Ep-2*E0+Em)/h**2/N, e0(naive_strain(H0, states, dirx, 0.2)), e0(naive_strain(H0, states, dirx, -0.2))))
    print("  [%.1fs]" % (time.time()-t0)); sys.stdout.flush()

# 1D chain (Ly=1): M1 model; Witten index and z=1 check
def chain(L, k=6):
    N, N1, _, _, _ = torus(L, 1)
    states = indep_sets(N, N1); index = {s:a for a,s in enumerate(states)}
    F = np.array([bin(s).count('1') for s in states]); W = int(np.sum((-1)**F))
    _, H = build(N, N1, [set()]*N, [set()]*N, 0.0, states, index)
    ev = np.sort(sla.eigsh(H, k=k, which='SA', return_eigenvectors=False, tol=1e-12)) if len(states) > 400 else np.sort(np.linalg.eigvalsh(H.toarray()))[:k]
    nz = ev[ev > 1e-8]
    return len(states), W, ev, nz[0] if len(nz) else np.nan

if __name__ == "__main__":
    print("1D periodic M1 chain: dim, W, lowest levels, gap*L")
    for L in [9, 10, 11, 12, 15, 18, 21, 24]:
        D, W, ev, gap = chain(L)
        print("  L=%2d dim=%6d W=%+d  lowest=%s  gap*L=%.4f" % (L, D, W, np.array2string(ev, precision=5), gap*L))
    run(4, 4, dense=True)
    run(4, 5, dense=True)
    run(5, 5, dense=False, epss=(0.0, 0.2))
    run(4, 6, dense=False, epss=(0.0, 0.2))
