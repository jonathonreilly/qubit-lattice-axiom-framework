#!/usr/bin/env python3
"""lane954 (FINISH row 954): GUIDE estimate of the lightest centre-even zero-momentum energy E_1 (0++ channel) on an
open-time slab, from APE-smeared (spatial, slice by slice) plaquette and 2x2-loop sums.  Used only for the floor
1/(2 beta E_1) of Lemma GAP-R (library/gap-lsij-scale-opus.md 4.2).  No gradients.  GUIDE only.
Claude Opus 5.5 (max), 2026-11-14.
Usage: python3 -I glueball954.py --lib <liblgt954.dylib> --beta 2.6 --L 16 --K 13 --nmeas 400
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import sys, time, json, argparse, ctypes, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rj954", os.path.join(HERE, "rj954.py"))
rj = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rj)
qmul, qc, sh, ev, PLANES = rj.qmul, rj.qc, rj.sh, rj.ev, rj.PLANES


def ape(x, n, alpha):
    """n steps of spatial APE smearing inside one slice; SU(2): normalise the quaternion sum."""
    for _ in range(n):
        new = []
        for i in range(3):
            S = 0
            for j in range(3):
                if j == i:
                    continue
                S = S + qmul(qmul(x[j], sh(x[i], ev(j))), qc(sh(x[j], ev(i))))           # forward staple
                xb = sh(x[j], ev(j, -1))
                S = S + qmul(qmul(qc(xb), sh(x[i], ev(j, -1))), sh(sh(x[j], ev(i)), ev(j, -1)))  # backward staple
            y = (1-alpha)*x[i] + (alpha/4)*S
            new.append(y/np.linalg.norm(y, axis=-1, keepdims=True))
        x = new
    return x


def slice_ops(x):
    out = []
    for (i, j) in PLANES:
        W = qmul(qmul(x[i], sh(x[j], ev(i))), qmul(qc(sh(x[i], ev(j))), qc(x[j])))
        out.append(W[..., 0].sum())
    for (i, j) in PLANES:
        a = qmul(x[i], sh(x[i], ev(i)))
        b = qmul(x[j], sh(x[j], ev(j)))
        W = qmul(qmul(a, sh(b, ev(i, 2))), qmul(qc(sh(a, ev(j, 2))), qc(b)))
        out.append(W[..., 0].sum())
    return [sum(out[:3]), sum(out[3:])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib", required=True)
    ap.add_argument("--beta", type=float, default=2.6)
    ap.add_argument("--L", type=int, default=16)
    ap.add_argument("--K", type=int, default=13)
    ap.add_argument("--nmeas", type=int, default=400)
    ap.add_argument("--nsep", type=int, default=2)
    ap.add_argument("--ntherm", type=int, default=300)
    ap.add_argument("--nsmear", type=int, default=10)
    ap.add_argument("--alpha", type=float, default=0.5)
    ap.add_argument("--edge", type=int, default=3)
    ap.add_argument("--seed", type=int, default=954954)
    ap.add_argument("--out", default=None)
    ap.add_argument("--tmax", type=float, default=1e9)
    a = ap.parse_args()
    lib = ctypes.CDLL(a.lib)
    Nt = 2*a.K+2
    lat = rj.Lattice(lib, "su2", a.L, Nt, a.beta, a.seed)
    rj.log(f"glueball954 beta={a.beta} L={a.L} Nt={Nt} nmeas={a.nmeas} nsmear={a.nsmear} alpha={a.alpha}")
    lat.sweep(a.ntherm, 2)
    rj.log("thermalised")
    ser = []
    for r in range(a.nmeas):
        lat.sweep(a.nsep, 2)
        row = []
        for t in range(Nt):
            q = lat.quat(t)
            x = [q[..., d+1, :] for d in range(3)]
            row.append(slice_ops(ape(x, a.nsmear, a.alpha)))
        ser.append(row)
        if (r+1) % max(1, a.nmeas//10) == 0:
            rj.log(f"meas {r+1}")
        if time.time()-rj.T0 > a.tmax:
            rj.log("time limit")
            break
    Z = np.array(ser)                       # (n, Nt, 2)
    Z = Z-Z.mean(0, keepdims=True)
    n = Z.shape[0]
    tmax = Nt-2*a.edge-1

    def corr(sel):
        cs = []
        for tau in range(tmax):
            ts = range(a.edge, Nt-a.edge-tau)
            cs.append(np.mean([(Z[sel, t, :]*Z[sel, t+tau, :]).mean(0) for t in ts], 0))
        return np.array(cs)                 # (tmax, 2)
    full = corr(np.ones(n, bool))
    blocks = np.array_split(np.arange(n), 20)
    jk = []
    for b in blocks:
        sel = np.ones(n, bool)
        sel[b] = False
        jk.append(corr(sel))
    jk = np.array(jk)
    with np.errstate(all="ignore"):
        E = np.log(full[:-1]/full[1:])
        Ej = np.log(jk[:, :-1]/jk[:, 1:])
    Ee = np.sqrt((len(blocks)-1)/len(blocks)*np.nansum((Ej-np.nanmean(Ej, 0))**2, 0))
    out = dict(args=vars(a), nmeas=n, Nt=Nt, C=full.tolist(), Eeff=E.tolist(), Eeff_err=Ee.tolist())
    for k, nm in enumerate(("smeared plaquette sum", "smeared 2x2 sum")):
        print(f"  {nm}: Eeff(tau) " + " ".join(f"{e:.3f}+-{s:.3f}" for e, s in zip(E[:, k], Ee[:, k])))
    if a.out:
        json.dump(out, open(a.out, "w"))
    rj.log("done")


if __name__ == "__main__":
    main()
