"""A53 ref51: parton (and A51 reference states) energies per site under A51's B4_inner and B4_r4 rules, from A51's saved
VMC samples (s51_<L>_<spec>_<seed>.npy: class estimators then four-spin estimators).  Binning errors per file, combined.
Usage: ref51.py"""
import sys, signal, glob, numpy as np
signal.alarm(120)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
A = f"{D53}/../A51"
for L in (6, 8, 10):
    R = np.load(f"{A}/rules51_{L}.npz"); N = L ** 3
    for spec in ("lp:0", "neez:0.05", "colz:0.1", "vbs"):
        fs = sorted(glob.glob(f"{A}/s51_{L}_{spec}_*.npy"))
        if not fs: continue
        out = []
        for key in ("B4_inner", "B4_r4"):
            v = R[key]; mus, errs, n = [], [], 0
            for fn in fs:
                S = np.load(fn); e = (S.real @ v) / N; mu, err = binerr(e); mus.append(mu); errs.append(err); n += len(e)
            w = 1 / np.array(errs) ** 2; mu = (w @ np.array(mus)) / w.sum(); err = 1 / np.sqrt(w.sum())
            out.append(f"{key} {mu:+.5f}({err*1e5:.0f}e-5)")
        print(f"L={L} {spec:10s} ({len(fs)} files, {n} samples): " + "  ".join(out), flush=True)
