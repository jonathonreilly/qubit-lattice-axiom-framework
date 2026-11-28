#!/usr/bin/env python3
"""lane976 (queue row 976, gap-escape-opus): escape test 1(e) of row 975 at the layered pi-flux slice u_xy.

Half-infinite slab (slices 0..T, slice 0 frozen, top slice T free at half spatial weight), SU(2) Wilson, temporal gauge.
Reuses row 952's code unchanged (library/guide/lane952/sg2lab.py: quaternions, Kennedy-Pendleton heat bath, SlabSU2,
make_slice_su2, eps_pattern), loaded by exec. Adds only the per-slice measurement:
  s_xy[k], s_xz[k], s_yz[k] = mean (1 - Re P) of slice k per plane;
  O[k] = |sum_l eps_l Im(U_l(k) U_l(k-1)^*)| / (2 L^3)  (colour order of the step-k field, tie mode of row 950), k >= 1;
  D[k] = |sum_l eps_l Im(U_l(k) u_l^*)| / (2 L^3).
Writes one npz per run with arrays of shape (n_meas, T+1). GUIDE only.
Written by Claude Opus 5.5 for row 976.
"""
import argparse, json, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SG2 = os.path.join(HERE, "..", "lane952", "sg2lab.py")
ns = {"__name__": "sg2lab"}
exec(compile(open(SG2).read(), SG2, "exec"), ns)
qmul, qc, sh = ns["qmul"], ns["qc"], ns["sh"]
SlabSU2, make_slice_su2, eps_pattern = ns["SlabSU2"], ns["make_slice_su2"], ns["eps_pattern"]


def plaq_re(U, i, j):
    """Re P_ij for all slices: U (T+1, 3, L, L, L, 4) -> (T+1, L, L, L)."""
    Ui, Uj = U[:, i], U[:, j]
    P = qmul(qmul(Ui, sh(Uj, i, 1)), qmul(qc(sh(Ui, j, 1)), qc(Uj)))
    return P[..., 0]


def measure(U, u, eps):
    L = u.shape[1]
    sxy = 1.0 - plaq_re(U, 0, 1).mean(axis=(1, 2, 3))
    sxz = 1.0 - plaq_re(U, 0, 2).mean(axis=(1, 2, 3))
    syz = 1.0 - plaq_re(U, 1, 2).mean(axis=(1, 2, 3))
    Ek = qmul(U[1:], qc(U[:-1]))[..., 1:]                 # (T, 3, L, L, L, 3): field on step k = 1..T
    Ok = np.linalg.norm(np.einsum("ixyz,tixyza->ta", eps, Ek), axis=1) / (2 * L ** 3)
    Dk = qmul(U, qc(u)[None])[..., 1:]
    Dv = np.linalg.norm(np.einsum("ixyz,tixyza->ta", eps, Dk), axis=1) / (2 * L ** 3)
    O = np.concatenate([[np.nan], Ok])
    return sxy, sxz, syz, O, Dv


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slice", default="xy", help="xy (u_xy) or vac (vacuum slice from --vacfile)")
    ap.add_argument("--vacfile", default=None)
    ap.add_argument("--genvac", type=int, default=0)
    ap.add_argument("--beta", type=float, default=2.3)
    ap.add_argument("--L", type=int, default=8)
    ap.add_argument("--T", type=int, default=40)
    ap.add_argument("--start", default="cold")
    ap.add_argument("--therm", type=int, default=300)
    ap.add_argument("--meas", type=int, default=40)
    ap.add_argument("--every", type=int, default=5)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    L = a.L
    t0 = time.time()
    info = {"args": vars(a)}
    if a.genvac:
        u0 = make_slice_su2("one", L)
        slab = SlabSU2(u0, a.beta, a.T, rng, start="hot", free_bottom=True)
        for _ in range(a.therm):
            slab.sweep()
        uv = slab.U[a.T // 2].copy()
        np.save(a.vacfile, uv)
        info["vac_sxy"] = float(1.0 - plaq_re(uv[None], 0, 1).mean())
        info["seconds"] = time.time() - t0
        json.dump(info, open(a.out, "w"), indent=1)
        print(json.dumps(info))
        return
    u = make_slice_su2(a.slice, L, vacfile=a.vacfile)
    eps = eps_pattern(L)
    slab = SlabSU2(u, a.beta, a.T, rng, start=a.start)
    for _ in range(a.therm):
        slab.sweep()
    info["t_therm"] = time.time() - t0
    rec = {k: [] for k in ("sxy", "sxz", "syz", "O", "D")}
    for m in range(a.meas):
        for _ in range(a.every):
            slab.sweep()
        for k, v in zip(("sxy", "sxz", "syz", "O", "D"), measure(slab.U, u, eps)):
            rec[k].append(v)
    info["seconds"] = time.time() - t0
    np.savez(a.out, **{k: np.array(v) for k, v in rec.items()}, info=json.dumps(info))
    s = np.array(rec["sxy"]).mean(axis=0)
    o = np.array(rec["O"]).mean(axis=0)
    ks = [k for k in (0, 1, 2, 3, 4, 8, 16, 30, 45) if k <= a.T]
    print(json.dumps({"args": vars(a), "seconds": round(info["seconds"], 1),
                      "sxy": {k: round(float(s[k]), 4) for k in ks},
                      "O": {k: round(float(o[k]), 4) for k in ks if k >= 1}}))


if __name__ == "__main__":
    main()
