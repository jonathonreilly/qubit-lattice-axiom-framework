#!/usr/bin/env python3
"""Route A (reviewer): genuine finite periodic-lattice second-order sea energy at finite q.
Lattice L^3 with antiperiodic boundary conditions (k on the grid 2 pi (n + 1/2)/L, so the massless node at
Gamma is not a grid point and the half-filled sea is unambiguous). For q = 2 pi m/L along z,
  e2_L(q) = -(1/L^3) sum_{k} sum_{bands} |<i,k+q|V(k+q/2)|j,k>|^2/gap   (both orderings),
i.e. lambda^2 coefficient of the sea energy per site for delta H = lambda (O_q + O_q^dag) (contact term dropped:
it is q-independent, Lemma C).  Checkpointed to logs/r8_routeA.json.  Usage: r8_routeA.py L
"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r8_walk as rw
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'r8_routeA.json')
EPS = {'zA': np.diag([1.0, -1, 0])/np.sqrt(2), 'zB': np.array([[0, 1.0, 0], [1, 0, 0], [0, 0, 0]])/np.sqrt(2)}
QN = (0, 1, 2, 3, 4)       # q = 2 pi n / 32

def main(L):
    res = json.load(open(OUT)) if os.path.exists(OUT) else {}
    W = rw.Walk(rw.bstar())
    g1 = 2*np.pi*(np.arange(L) + 0.5)/L - np.pi
    todo = [n for n in QN if f"L={L}|n={n}" not in res]
    if not todo:
        return res
    t0 = time.time()
    KX, KY, KZ = np.meshgrid(g1, g1, g1, indexing='ij')
    K = np.stack([KX, KY, KZ], -1).reshape(-1, 3)
    om = np.empty((K.shape[0], 4)); V = np.empty((K.shape[0], 4, 4), complex)
    for i in range(0, K.shape[0], 1 << 16):
        om[i:i+(1 << 16)], V[i:i+(1 << 16)] = W.bands(K[i:i+(1 << 16)])
    om = om.reshape(L, L, L, 4); V = V.reshape(L, L, L, 4, 4)
    print(f'L={L}: grid bands {time.time()-t0:.0f}s', flush=True)
    for n in todo:
        t1 = time.time()
        m = n*L//32; assert (n*L) % 32 == 0
        q = 2*np.pi*m/L
        acc = {c: 0.0 for c in EPS}
        for ix in range(L):          # slab over kx
            kb = np.stack(np.meshgrid([g1[ix]], g1, g1, indexing='ij'), -1).reshape(-1, 3)
            kmid = kb + np.array([0, 0, q/2])
            Hm = W.H(kmid)
            P = np.stack([-np.real(np.einsum('nij,ji->n', Hm, rw.T3S[j]))/4 for j in range(3)], 1)
            ob = om[ix].reshape(-1, 4); Vb = V[ix].reshape(-1, 4, 4)
            oa = np.roll(om[ix], -m, axis=1).reshape(-1, 4); Va = np.roll(V[ix], -m, axis=1).reshape(-1, 4, 4)
            for c, eps in EPS.items():
                w = P @ eps.T
                Vm = 0.5*sum(w[:, b, None, None]*rw.T3S[b] for b in range(3))
                acc[c] += float(np.sum(rw.bubble(W, Vm, None, None, (oa, Va), (ob, Vb))))
        res[f"L={L}|n={n}"] = dict(L=L, n=n, q=q, e2={c: -v/L**3 for c, v in acc.items()}, s=W.s, sec=time.time()-t1)
        json.dump(res, open(OUT, 'w'), indent=0)
        print(f'L={L} n={n} q={q:.5f} e2={res[f"L={L}|n={n}"]["e2"]} ({time.time()-t1:.0f}s)', flush=True)
    return res

if __name__ == '__main__':
    main(int(sys.argv[1]))
