#!/usr/bin/env python3
"""lane946 (row 946), extra GUIDE probe: worst f in the span of zero-momentum slice observables.

theta_zm := sup over f in span{ sum_p h(c_p) (h in c, tanh3c, tanh10c, c^3; one plane each), sum_y line_y
(one direction each) } of E_nu|grad P f|^2 / E_nu|grad f|^2 = top generalised eigenvalue of (A, Bm),
A_ij = E_nu <grad P F_i, grad P F_j> (unbiased: symmetrised product of the two independent half-chain
covariances), Bm_ij = E_nu <grad F_i, grad F_j>.  A variational lower bound on theta_GC of the box.
GUIDE only.  Author: Claude Opus 5.5 (max), 2026-11-14.
"""
import os, sys, json, time, argparse
import numpy as np
import scipy.sparse as ssp
from scipy.linalg import eigh
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fct
from fct import (spatial_box, Lat4, ObsSU2, Acc, sweep_su2, slices_su2, loop_prod, loop_grads, cmult, log)


def zm_rows(ob):
    rows, cols, vals, labels = [], [], [], []
    for name in ("c", "t3", "t10", "c3"):
        off = ob.boff[name][0]
        for gi, g in enumerate(ob.zm_groups):
            for i in g:
                rows.append(len(labels)); cols.append(off + i); vals.append(1.0)
            labels.append(f"{name}_o{gi}")
    off = ob.boff["line"][0]
    for gi, g in enumerate(ob.xs_groups):
        for i in g:
            rows.append(len(labels)); cols.append(off + i); vals.append(1.0)
        labels.append(f"line_d{gi}")
    return ssp.csr_matrix((vals, (rows, cols)), shape=(len(labels), ob.NF)), labels


def zm_grads(ob, x, nsl):
    """per-link gradients of every zero-momentum row at x: (B, nz, nsl*4)."""
    B = x.shape[0]
    c = loop_prod(x, ob.pidx, ob.pmul)[..., 0]
    G = loop_grads(x, ob.pidx, ob.pneg, ob.pmul)
    hp = {"c": np.ones_like(c), "t3": 3 / np.cosh(3 * c) ** 2, "t10": 10 / np.cosh(10 * c) ** 2, "c3": 3 * c * c}
    out = []
    for name in ("c", "t3", "t10", "c3"):
        for g in ob.zm_groups:
            acc = np.zeros((B, nsl, 4))
            np.add.at(acc, (slice(None), ob.pidx[g].ravel()), (hp[name][:, g, None, None] * G[:, g]).reshape(B, -1, 4))
            out.append(acc.reshape(B, -1))
    Gl = loop_grads(x, ob.lidx, ob.lneg, ob.lmul)
    for g in ob.xs_groups:
        acc = np.zeros((B, nsl, 4))
        np.add.at(acc, (slice(None), ob.lidx[g].ravel()), Gl[:, g].reshape(B, -1, 4))
        out.append(acc.reshape(B, -1))
    return np.stack(out, 1)


def top_gev(A, Bm, rel=1e-8):
    """top generalised eigenvalue of (A, Bm) on the range of Bm above rel * max eigenvalue."""
    ev, V = np.linalg.eigh(Bm)
    keep = ev > rel * ev.max()
    Wh = V[:, keep] / np.sqrt(ev[keep])
    M = Wh.T @ A @ Wh
    e, u = np.linalg.eigh((M + M.T) / 2)
    return e[-1], Wh @ u[:, -1], int(keep.sum())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", type=int, default=4); ap.add_argument("--K", type=int, default=6)
    ap.add_argument("--beta", type=float, default=2.3); ap.add_argument("--B", type=int, default=16)
    ap.add_argument("--m", type=int, default=8); ap.add_argument("--nsep", type=int, default=10)
    ap.add_argument("--n", type=int, default=300); ap.add_argument("--ntherm", type=int, default=200)
    ap.add_argument("--nor", type=int, default=2); ap.add_argument("--seed", type=int, default=21)
    ap.add_argument("--tag", default="zmvar")
    args = ap.parse_args()
    sp = spatial_box(args.L); lat = Lat4(sp, args.K); ob = ObsSU2(sp)
    Wz, labels = zm_rows(ob)
    nz, B, beta = len(labels), args.B, args.beta
    rng = np.random.default_rng(args.seed)
    log(f"zmvar L={args.L} K={args.K} beta={beta} B={B} m={args.m} n={args.n} nz={nz}")
    U = np.zeros((B, lat.nl, 4)); U[..., 0] = 1.0
    for i in range(args.ntherm):
        sweep_su2(U, lat.tab_all, beta, rng, args.nor)
    A = np.zeros((B, nz, nz)); Bm = np.zeros((B, nz, nz))
    na = lat.nsl * 4
    for r in range(args.m):
        for i in range(args.nsep):
            sweep_su2(U, lat.tab_all, beta, rng, args.nor)
        Ui = U.copy()
        x, _, _ = slices_su2(lat, Ui)
        Gz = zm_grads(ob, x, lat.nsl)
        Bm += np.einsum("bik,bjk->bij", Gz, Gz)
        aF, aB = Acc(B, na, ob.NF), Acc(B, na, ob.NF)
        for i in range(args.n):
            sweep_su2(Ui, lat.tab_frz, beta, rng, args.nor)
            _, w, wp = slices_su2(lat, Ui)
            a = w - (w * x).sum(-1, keepdims=True) * x
            ap_ = wp - (wp * x).sum(-1, keepdims=True) * x
            aF.add(a.reshape(B, -1), ob.base(w)); aB.add(ap_.reshape(B, -1), ob.base(wp))
        CF, CB = aF.cov(), aB.cov()
        for b in range(B):
            XF = Wz @ CF[b].T; XB = Wz @ CB[b].T
            A[b] += beta * beta * (XF @ XB.T + XB @ XF.T) / 2
        th, vec, k = top_gev(A.sum(0), Bm.sum(0))
        log(f"round {r+1}/{args.m}: theta_zm={th:.4g} (rank {k}); diag R: " +
            " ".join(f"{lb}={A.sum(0)[i,i]/Bm.sum(0)[i,i]:.3g}" for i, lb in enumerate(labels)))
    At, Bt = A.sum(0), Bm.sum(0)
    th, vec, k = top_gev(At, Bt)
    thj = np.array([top_gev(At - A[b], Bt - Bm[b])[0] for b in range(B)])
    err = float(np.sqrt((B - 1) / B * ((thj - thj.mean()) ** 2).sum()))
    # sectors: centre-even plaquette functions and centre-odd lines separately
    ie = [i for i, lb in enumerate(labels) if not lb.startswith("line")]
    io = [i for i, lb in enumerate(labels) if lb.startswith("line")]
    the = top_gev(At[np.ix_(ie, ie)], Bt[np.ix_(ie, ie)])[0]
    tho = top_gev(At[np.ix_(io, io)], Bt[np.ix_(io, io)])[0]
    thej = np.array([top_gev((At - A[b])[np.ix_(ie, ie)], (Bt - Bm[b])[np.ix_(ie, ie)])[0] for b in range(B)])
    erre = float(np.sqrt((B - 1) / B * ((thej - thej.mean()) ** 2).sum()))
    nv = vec / np.sqrt(vec @ Bt @ vec)
    res = {"args": vars(args), "labels": labels, "theta_zm": float(th), "err": err, "rank": k,
           "theta_even": float(the), "err_even": erre, "theta_odd_lines": float(tho),
           "top_vector_B_normalised": dict(zip(labels, map(float, nv))),
           "diag_R": {lb: float(At[i, i] / Bt[i, i]) for i, lb in enumerate(labels)}}
    od = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    json.dump(res, open(os.path.join(od, args.tag + ".json"), "w"), indent=1)
    np.savez(os.path.join(od, args.tag + ".npz"), A=A, Bm=Bm, labels=np.array(labels))
    log(f"RESULT {args.tag}: theta_zm = {th:.5g} +- {err:.2g} (rank {k}); centre-even sector {the:.5g} +- {erre:.2g};"
        f" lines only {tho:.5g}")
    log("top vector:", {lb: round(float(v), 4) for lb, v in zip(labels, nv)})


if __name__ == "__main__":
    main()
