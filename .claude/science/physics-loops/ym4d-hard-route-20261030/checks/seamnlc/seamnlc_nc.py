#!/usr/bin/env python3
"""seam-nonlinear-c, kill test K1/K2: is the path-gauge primitive critical?

Guidance only; the statement tested is proved by hand (Lemma NC of
library/seam-nonlinear-c.md, Section 2). A growing ratio confirms the hand
lower bound; a bounded control proves nothing.

Field: the locked pair of library/seam-nlpay.md Section 4, abelian, unit
amplitude: H_0 = delta(bond in direction mu at c + e_off) - delta(bond in
direction mu at c - e_off), c a block centre. Q_path H_0 = 0 exactly.
G = d H_0. The path-gauge primitive is hG (tensor homotopy of
library/seam-quadratic-c.md Section 4, coded in checks/seamqc/seamqc.py).

Usage: python3 seamnlc_nc.py OUT.json
"""
import sys, os, json, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "seamqc"))
import seamqc as sq  # noqa: E402

PAIRS = sq.PAIRS


def pair_field(lat, mu, off):
    """Locked pair: +1 on the mu-bond at c + e_off, -1 at c - e_off, c = 0."""
    H = {(a,): np.zeros(lat.Ns) for a in range(4)}
    p = [0, 0, 0, 0]; q = [0, 0, 0, 0]
    p[off] = 1 % lat.Ns[off]; q[off] = (-1) % lat.Ns[off]
    H[(mu,)][tuple(p)] += 1.0
    H[(mu,)][tuple(q)] -= 1.0
    return H


def s_p4(lat, h):
    """sum over plaquettes (mu<nu, base x) of (|h_mu(x)| + |h_nu(x+e_mu)|
    + |h_mu(x+e_nu)| + |h_nu(x)|)^4."""
    tot = 0.0
    for (mu, nu) in PAIRS:
        a = np.abs(h[(mu,)]); b = np.abs(h[(nu,)])
        s = a + np.roll(b, -1, axis=mu) + np.roll(a, -1, axis=nu) + b
        tot += float((s ** 4).sum())
    return tot


def run_case(B, Ms, mu, off):
    lat = sq.Lat4(B, Ms)
    H0 = pair_field(lat, mu, off)
    out = {"B": B, "Ms": list(Ms), "mu": mu, "off": off}
    QH0 = lat.R(H0)                           # Q_path on 1-forms
    out["max|Q_path H0|"] = sq.fmax(QH0)
    G = lat.d1(H0)
    out["max|dG|"] = sq.fmax(lat.d2(G))
    out["max|C_B G|"] = sq.fmax(lat.R(G))     # C_B on 2-forms
    hG = lat.hmap(G)
    hH0 = lat.hmap(H0)[()]
    resid = sq.fsub(hG, sq.fsub(H0, lat.d0(hH0)))
    out["rel|hG-(H0-d hH0)|"] = float(np.sqrt(sq.fnorm2(resid)) / max(np.sqrt(sq.fnorm2(hG)), 1e-300))
    G2 = sq.fnorm2(G)
    out["||G||^2"] = G2
    out["rho_4"] = float(sum((np.abs(v) ** 4).sum() for v in hG.values())) / G2 ** 2
    out["sigma_4"] = s_p4(lat, hG) / G2 ** 2
    out["rho_4(H0)"] = float(sum((np.abs(v) ** 4).sum() for v in H0.values())) / G2 ** 2
    out["max|hG|"] = sq.fmax(hG)
    # count bonds with |hG| > 1/4 (hand lemma: at least 12 m of them)
    out["#|hG|>1/4"] = int(sum(int((np.abs(v) > 0.25).sum()) for v in hG.values()))
    out["RSS_GB"] = round(sq.rss_gb(), 3)
    sq.guard()
    return out


def main():
    t0 = time.time()
    res = {"cases": []}
    for B in (3, 5, 7, 9, 11, 13):
        Ms = (3, 2, 1, 1) if B == 3 else (3, 1, 1, 1)
        for (mu, off) in ((0, 1), (3, 0), (1, 2)):
            r = run_case(B, Ms, mu, off)
            res["cases"].append(r)
            print({k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items()}, flush=True)
    res["runtime_s"] = round(time.time() - t0, 1)
    with open(sys.argv[1] if len(sys.argv) > 1 else "seamnlc_nc.json", "w") as fh:
        json.dump(res, fh, indent=1)
    print("done", res["runtime_s"], "s", flush=True)


if __name__ == "__main__":
    main()
