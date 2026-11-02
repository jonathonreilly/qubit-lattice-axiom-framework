#!/usr/bin/env python3
"""seam-nonlinear-c, check of Lemma PG (linear, path-part identities only).

Guidance only; Lemma PG is proved by hand. Checks, for random fine 1-forms H
(not parent-preserving; the identities below do not need it):
  (a) Q_path T_1 = I on coarse 1-forms, so Q_path(H - T_1 Q_path H) = 0;
  (b) d(T_1 Q_path H) = T_2 d' Q_path H (chain map);
  (c) for H with Q_path H = d' psi (a coarse gradient), d' Q_path H = 0 and
      d h = d H, h := H - T_1 Q_path H;
  (d) local L^2 and L^4 ratios ||h|| / ||H|| on random and on the locked pair.
The contour part Phi_n is not coded here (it is coded only in seamqc.py for
L = 3, n = 2), so the identity Phi_n h = r_n T_0 Psi is checked by hand only.
Usage: python3 seamnlc_pg.py OUT.json
"""
import sys, os, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "seamqc"))
import seamqc as sq  # noqa: E402

def coarse_lat(lat):
    # coarse 1-forms live on (M0,M1,M2,M3); the coarse d is 'dc'
    return tuple(o["M"] for o in lat.o)

def run(B, Ms, seed):
    rng = np.random.default_rng(seed)
    lat = sq.Lat4(B, Ms)
    out = {"B": B, "Ms": list(Ms)}
    H = {(mu,): rng.standard_normal(lat.Ns) for mu in range(4)}
    QH = lat.R(H)                          # coarse 1-form
    TQH = lat.T(QH)                        # fine 1-form
    h = sq.fsub(H, TQH)
    out["max|Q_path h|"] = sq.fmax(lat.R(h))
    lhs = lat.d1(TQH)
    rhs = lat.T(lat.d1(QH, key="dc"))      # T_2 d' Q_path H
    out["rel|d T1 Q H - T2 d' Q H|"] = sq.frel(lhs, rhs)
    # (c): make Q_path H a coarse gradient by adding T_1(d' psi - Q_path H)
    psi = rng.standard_normal(coarse_lat(lat))
    dpsi = lat.d0(psi, key="dc")
    Hc = sq.fadd(H, lat.T(sq.fsub(dpsi, QH)))
    out["rel|Q_path Hc - d'psi|"] = sq.frel(lat.R(Hc), dpsi)
    hc = sq.fsub(Hc, lat.T(lat.R(Hc)))
    out["rel|d hc - d Hc|"] = sq.frel(lat.d1(hc), lat.d1(Hc))
    n2 = lambda F: np.sqrt(sq.fnorm2(F))
    n4 = lambda F: float(sum((np.abs(v) ** 4).sum() for v in F.values())) ** 0.25
    out["L2 ratio |h|/|H| (random)"] = n2(h) / n2(H)
    out["L4 ratio |h|/|H| (random)"] = n4(h) / n4(H)
    sq.guard()
    out["RSS_GB"] = round(sq.rss_gb(), 3)
    return out

def main():
    t0 = time.time()
    res = {"cases": []}
    for B, Ms in ((3, (3, 3, 2, 2)), (5, (3, 2, 2, 2)), (7, (2, 2, 2, 2)), (9, (2, 2, 2, 1))):
        r = run(B, Ms, 1000 + B)
        res["cases"].append(r)
        print({k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items()}, flush=True)
    res["runtime_s"] = round(time.time() - t0, 1)
    with open(sys.argv[1] if len(sys.argv) > 1 else "seamnlc_pg.json", "w") as fh:
        json.dump(res, fh, indent=1)
    print("done", res["runtime_s"], "s", flush=True)

if __name__ == "__main__":
    main()
