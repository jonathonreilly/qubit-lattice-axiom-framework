"""T1c: restrict T1b placements by symmetry (C3[111]-invariant, or Z2 y<->z invariant)."""
import itertools
import numpy as np
from common import MZ, LOW, CKM, LN3, obs_logs, null_N1, null_N2

rng = np.random.default_rng(11)
E = np.eye(3, dtype=int)
L = [E[0], E[1], E[2]]
ORB = {"hw1": [E[0], E[1], E[2]], "hw2": [E[1] + E[2], E[2] + E[0], E[0] + E[1]]}
SIG = np.linspace(0.25, 12.0, 48)


def area(p, q, r):
    return 0.5 * np.abs(np.cross(q - p, r - p)).sum()


def build(filter_ht):
    cf = []
    for on, orb in ORB.items():
        for t in itertools.product((-1, 0, 1), repeat=3):
            for h in itertools.product((-1, 0, 1, 2), repeat=3):
                if not filter_ht(np.array(h), np.array(t)):
                    continue
                R = [o + np.array(t) for o in orb]
                A = np.array([[area(L[i], np.array(h), R[j]) for j in range(3)] for i in range(3)])
                cf.append((on, t, h, A))
    AM = np.array([c[3] for c in cf])
    LS = np.empty((len(SIG), len(cf), 3)); UL = np.empty((len(SIG), len(cf), 3, 3))
    for a, sg in enumerate(SIG):
        U, s, _ = np.linalg.svd(np.exp(-sg * AM))
        LS[a] = np.log(np.maximum(s[:, ::-1], 1e-300)); UL[a] = U[:, :, ::-1]
    return cf, LS, UL


def score(Y, LS):
    hs = []
    for s in range(3):
        R = Y[:, s, None, None, :] - LS[None]
        hs.append((0.5 * (R.max(-1) - R.min(-1))).min(-1))
    hs = np.stack(hs, 1)
    return hs.max(1).min(-1)


def ckm(yu, yd, LS, UL, target=CKM):
    best = np.inf
    for a in range(len(SIG)):
        iu = np.where(0.5 * np.ptp(yu - LS[a], -1) <= LN3)[0]
        idd = np.where(0.5 * np.ptp(yd - LS[a], -1) <= LN3)[0]
        if len(iu) and len(idd):
            V = np.einsum("aki,bkj->abij", UL[a, iu], UL[a, idd])
            v = np.abs(np.stack([V[..., 0, 1], V[..., 1, 2], V[..., 0, 2]], -1))
            best = min(best, np.abs(np.log(np.maximum(v, 1e-300) / target)).max(-1).min())
    return best


FILTERS = {
    "C3[111]-invariant (h,t on body diagonal)": lambda h, t: h[0] == h[1] == h[2] and t[0] == t[1] == t[2],
    "Z2 (y<->z)-invariant": lambda h, t: h[1] == h[2] and t[1] == t[2],
    "canonical h=0, t=0": lambda h, t: not h.any() and not t.any(),
}
for name, flt in FILTERS.items():
    cf, LS, UL = build(flt)
    degen = np.mean(np.abs(np.diff(LS, axis=2)).min(axis=2) < 1e-6)
    out = [f"{name}: {len(cf)} placements/sector; degenerate-pair fraction {degen:.2f}"]
    for label, data in (("MZ", MZ), ("LOW", LOW)):
        Yo = obs_logs(data)[None]
        so = score(Yo, LS)[0]
        fc = ckm(Yo[0, 0], Yo[0, 1], LS, UL)
        out.append(f"  {label}: masses best x{np.exp(so):.2f} pass={so <= LN3}; CKM best (given u,d masses x3) "
                   + (f"x{np.exp(fc):.2f}" if np.isfinite(fc) else "none"))
    Y = null_N1(rng, 1000)
    sr = np.concatenate([score(Y[i:i + 50], LS) for i in range(0, 1000, 50)])
    Y2 = null_N2(rng, 1000)
    sr2 = np.concatenate([score(Y2[i:i + 50], LS) for i in range(0, 1000, 50)])
    out.append(f"  random masses pass rate N1 {np.mean(sr <= LN3):.3f}, N2 {np.mean(sr2 <= LN3):.3f}")
    m = 100; ok = 0
    for i in range(m):
        if sr[i] <= LN3:
            ok += ckm(Y[i, 0], Y[i, 1], LS, UL, np.exp(rng.uniform(np.log(1e-4), 0, 3))) <= LN3
    out.append(f"  random masses+CKM (N1, random CKM) pass {ok}/{m}")
    print("\n".join(out), flush=True)
