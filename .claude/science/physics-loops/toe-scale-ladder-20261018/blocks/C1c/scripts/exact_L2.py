#!/usr/bin/env python3
"""Exact thermal reference for L=2 over the FULL Gauss sector (brute-force enumeration of all 2^24
link configurations, dense diagonalisation per flip component). Independent of the QMC code (shares
only the Lat geometry). Writes data/exact_L2.json."""
import os, sys, json
import numpy as np
import numba as nb
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

sys.path.insert(0, os.path.dirname(__file__))
from ctqmc import Lat

HERE = os.path.dirname(os.path.abspath(__file__))


@nb.njit(cache=True)
def enum(tail, head, nv, nl):
    out = []
    for c in range(1 << nl):
        ok = True
        d = np.zeros(nv, dtype=np.int64)
        for l in range(nl):
            s = 1 if (c >> l) & 1 else -1
            d[tail[l]] += s
            d[head[l]] -= s
        for v in range(nv):
            if d[v] != 0:
                ok = False
                break
        if ok:
            out.append(c)
    return np.array(out, dtype=np.int64)


def main(V=0.0, betas=(0.25, 0.5, 1.0, 2.0, 4.0, 8.0)):
    lat = Lat(2)
    codes = enum(lat.tail, lat.head, lat.nv, lat.nl)
    S = np.array([[1 if (c >> l) & 1 else -1 for l in range(lat.nl)] for c in codes], dtype=np.int64)
    n = len(S)
    idx = {int(c): i for i, c in enumerate(codes)}
    circ = (S[:, lat.plinks] * lat.psign).sum(axis=2)
    fl = np.abs(circ) == 4
    rows, cols = [], []
    for i in range(n):
        for p in np.flatnonzero(fl[i]):
            t = S[i].copy()
            t[lat.plinks[p]] *= -1
            c = int(((t > 0).astype(np.int64) << np.arange(lat.nl)).sum())
            rows.append(i)
            cols.append(idx[c])
    A = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    assert (A - A.T).nnz == 0
    ncomp, lab = connected_components(A, directed=False)
    Nc = fl.sum(axis=1).astype(float)
    W = np.array([lat.winding(s) for s in S])
    W2 = (W ** 2).mean(axis=1)
    P0 = (W == 0).mean(axis=1)
    P1 = (np.abs(W) == 1).mean(axis=1)
    # S(q) with q = pi e_b (L=2), all three link directions a, averaged over b
    ph = np.exp(1j * np.pi * lat.lpos)  # (nl,3) e^{i pi r_b}
    Sq = np.zeros(n)
    for b in range(3):
        for a in range(3):
            sel = lat.ldir == a
            Ea = (S[:, sel] * 0.5 * ph[sel, b][None, :]).sum(axis=1)
            Sq += np.abs(Ea) ** 2
    Sq /= (3 * lat.nv)
    evals, obs = [], {k: [] for k in ("Nc", "W2", "P0", "P1", "Sq")}
    for c in range(ncomp):
        ii = np.flatnonzero(lab == c)
        Hc = -A[ii][:, ii].toarray() + V * np.diag(Nc[ii])
        e, U = np.linalg.eigh(Hc)
        evals.append(e)
        for k, arr in (("Nc", Nc), ("W2", W2), ("P0", P0), ("P1", P1), ("Sq", Sq)):
            obs[k].append(np.einsum("ij,i,ij->j", U, arr[ii], U))
    e_all = np.concatenate(evals)
    o_all = {k: np.concatenate(v) for k, v in obs.items()}
    E0 = e_all.min()
    res = {"n_states": int(n), "n_components": int(ncomp), "E0": float(E0), "V": V, "beta": {}}
    for b in betas:
        w = np.exp(-b * (e_all - E0))
        Z = w.sum()
        r = {"E": float((w * e_all).sum() / Z)}
        for k in o_all:
            r[k] = float((w * o_all[k]).sum() / Z)
        res["beta"][str(b)] = r
    return res


if __name__ == "__main__":
    out = {}
    for V in (0.0, 0.5):
        r = main(V)
        out[str(V)] = r
        print(json.dumps(r, indent=1))
    json.dump(out, open(os.path.join(HERE, "..", "data", "exact_L2.json"), "w"), indent=1)
