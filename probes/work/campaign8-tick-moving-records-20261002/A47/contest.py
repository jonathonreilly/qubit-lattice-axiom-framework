"""A47 contest: E(j) = e_J' + 2 j c2 per NN bond (dual frame, J1' = 1) for every state and size, with binning
errors on the combined per-sweep series; optimum over the U(1) trial lam'; A45's success test.
Sources: A47 c_<L>_<kind><val>.npy [e_J', c2]; A46 vmcj_<L>_m<m>.npy (Neel field) and vmcjc_6_m<m>.npy
(collinear field) [e_J, e_K, ring, m_stag, c2]; LSWT from lswt47.npy (infinite lattice, stable states only)."""
import glob, sys, signal, numpy as np
signal.alarm(60)
D = __file__.rsplit('/', 1)[0]; D46 = D.rsplit('/', 1)[0] + "/A46"
sys.path.insert(0, D46)
from a46lib import binerr
def load():
    st = {}
    for f in glob.glob(f"{D}/c_*.npy"):
        tag = f.rsplit("/", 1)[1][2:-4]; L, rest = tag.split("_", 1)
        kind = "lp" if rest.startswith("lp") else ("neel" if rest.startswith("neel") else "col")
        val = float(rest[len(kind):]); T = np.load(f); st[(L, kind, val, "A47")] = T
    for f in glob.glob(f"{D46}/vmcj_*_m*.npy") + glob.glob(f"{D46}/vmcjc_*_m*.npy"):
        nm = f.rsplit("/", 1)[1]; kind = "col" if nm.startswith("vmcjc") else "neel"
        L = nm.split("_")[1]; val = float(nm.rsplit("_m", 1)[1][:-4]); S = np.load(f)
        T = np.c_[S[:, 0].real, S[:, 4].real]
        if kind == "neel" and val == 0.0: kind = "su2-A46"
        st[(L, kind, val, "A46")] = T
    return st
st = load(); LS = np.load(f"{D}/lswt47.npy")
js = [0.2, 0.25, 0.3, 0.35, 0.4]
for L in ("6", "8"):
    print(f"\n===== L = {L} =====")
    keys = sorted(k for k in st if k[0] == L)
    print("state             n_sweeps   e_J'        c2")
    for k in keys:
        T = st[k]; a, ea = binerr(T[:, 0]); c, ec = binerr(T[:, 1])
        print(f"  {k[1]:8s} {k[2]:5.3f} ({k[3]}) {len(T):6d}  {a:+.5f}({ea*1e5:.0f})  {c:+.5f}({ec*1e5:.0f})")
    for j in js:
        E = {}
        for k in keys:
            T = st[k]; E[k] = binerr(T[:, 0] + 2 * j * T[:, 1])
        lp = {k[2]: E[k] for k in E if k[1] == "lp"}
        if not lp: continue
        xb = min(lp, key=lambda x: lp[x][0]); Eb, sb = lp[xb]
        E0, s0 = lp.get(0.0, (np.nan, np.nan))
        d0 = E0 - Eb; sd0 = np.hypot(s0, sb)
        comps = {f"{k[1]} {k[2]} ({k[3]})": E[k] for k in E if k[1] in ("neel", "col")}
        row = LS[np.isclose(LS[:, 0], j)]
        if len(row):
            r = row[0]
            if r[2] > 0.5: comps["Neel LSWT"] = (r[1], r[3])
            if r[5] > 0.5: comps["collinear LSWT"] = (r[4], r[6])
        cb = min(comps, key=lambda c: comps[c][0]); Ec, sc = comps[cb]
        M = Ec - Eb; sM = np.hypot(sb, sc)
        print(f" j={j:.2f}: trial optimum lam'={xb:.2f}: E = {Eb:+.5f}+-{sb:.5f}; lam'=0: {E0:+.5f}+-{s0:.5f} -> gain {d0:+.5f} ({d0/sd0 if sd0>0 else np.nan:+.1f} sigma)")
        print(f"         lowest competitor {cb}: {Ec:+.5f}+-{sc:.5f} -> margin {M:+.5f} ({M/sM if sM>0 else np.nan:+.1f} combined sigma)")
        print("         lam' scan: " + ", ".join(f"{x:.2f}:{lp[x][0]:+.4f}({lp[x][1]*1e4:.0f})" for x in sorted(lp)))
        print("         competitors: " + ", ".join(f"{c}:{v[0]:+.4f}" for c, v in sorted(comps.items(), key=lambda kv: kv[1][0])[:5]))
