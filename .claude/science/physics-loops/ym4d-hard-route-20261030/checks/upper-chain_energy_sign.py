#!/usr/bin/env python3
"""Criteria E1, E2: sign of energy correlators in orthogonal planes, periodic SU(2)."""
import importlib.util, os, sys, resource
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np

spec = importlib.util.spec_from_file_location("ie", os.path.join(os.path.dirname(os.path.abspath(__file__)), "upper-chain_ie4d.py"))
ie = importlib.util.module_from_spec(spec); spec.loader.exec_module(ie)


class Torus(ie.Cube):
    def __init__(self, T, beta, rng):
        self.N = N = T
        self.beta = beta
        self.rng = rng
        self.U = [np.zeros((N, N, N, N, 4)) for _ in range(4)]
        for m in range(4):
            self.U[m][..., 0] = 1.0
        self.masks = []
        idx = np.indices((N, N, N, N))
        for m in range(4):
            par = sum(idx[n] for n in range(4) if n != m)
            self.masks.append((par % 2 == 0, par % 2 == 1))

    def clover(self, s):
        e = np.zeros_like(next(iter(s.values())))
        for (m, n), a in s.items():
            e += 0.25 * (a + np.roll(a, 1, axis=m) + np.roll(a, 1, axis=n) + np.roll(np.roll(a, 1, axis=m), 1, axis=n))
        return e


def run(T, beta, nsweeps, seed):
    rng = np.random.default_rng(seed)
    lat = Torus(T, beta, rng)
    for _ in range(300):
        lat.sweep()
    ys = {"0": (0, 0, 0, 0), "e1": (1, 0, 0, 0), "e3": (0, 0, 1, 0), "e1+e3": (1, 0, 1, 0)}
    ey = {"e1": (1, 0, 0, 0), "2e1": (2, 0, 0, 0), "e1+e2": (1, 1, 0, 0)}
    rec = {k: [] for k in ys}
    rec_e = {k: [] for k in ey}
    m12, m34, me = [], [], []
    for it in range(nsweeps):
        lat.sweep()
        s = {(m, n): 1 - lat.plaq_trace(m, n) for m in range(4) for n in range(m + 1, 4)}
        a, b = s[(0, 1)], s[(2, 3)]
        m12.append(a.mean()); m34.append(b.mean())
        for k, y in ys.items():
            rec[k].append(np.mean(a * np.roll(b, y, axis=(0, 1, 2, 3))))
        e = lat.clover(s)
        me.append(e.mean())
        for k, y in ey.items():
            rec_e[k].append(np.mean(e * np.roll(e, y, axis=(0, 1, 2, 3))))
        if it % 2000 == 0 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > 2.0:
            sys.exit("RSS")
    nb = 20

    def conn(xy, xm, ym):
        xy, xm, ym = np.array(xy), np.array(xm), np.array(ym)
        L = len(xy) // nb * nb
        bx = xy[:L].reshape(nb, -1).mean(1)
        bm = xm[:L].reshape(nb, -1).mean(1)
        bn = ym[:L].reshape(nb, -1).mean(1)
        # jackknife
        jk = [(bx.sum() - bx[i]) / (nb - 1) - (bm.sum() - bm[i]) / (nb - 1) * (bn.sum() - bn[i]) / (nb - 1) for i in range(nb)]
        jk = np.array(jk)
        return jk.mean(), np.sqrt((nb - 1) * jk.var())

    out = [f"beta={beta}"]
    for k in ys:
        c, er = conn(rec[k], m12, m34)
        out.append(f"C_perp({k})={c:.3e}+-{er:.1e}")
    for k in ey:
        c, er = conn(rec_e[k], me, me)
        out.append(f"C_e({k})={c:.3e}+-{er:.1e}")
    print(" ".join(out), flush=True)


if __name__ == "__main__":
    for i, beta in enumerate((2.5, 4.0, 8.0)):
        run(6, beta, 20000, 100 + i)
