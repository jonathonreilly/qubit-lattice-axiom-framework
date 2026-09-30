"""T05 calibration test (see PREREG.md; fixed before running).

Block-01 setting: six-axis menu, product rule with orbit weights (3,1,2),
records-only reading, open 4x4x4 window.
"""
import sys, time
import numpy as np

SEED = 20260929
L = 4
N = L ** 3
M = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
P_, Q_, R_ = 3.0, 1.0, 2.0
rng = np.random.default_rng(SEED)

# ---- lattice ----------------------------------------------------------------
def sid(x, y, z):
    return (x * L + y) * L + z

coords = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
nb = -np.ones((N, 6), dtype=np.int64)  # directions +x,-x,+y,-y,+z,-z
for i, (x, y, z) in enumerate(coords):
    for d, (dx, dy, dz) in enumerate([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]):
        a, b, c = x + dx, y + dy, z + dz
        if 0 <= a < L and 0 <= b < L and 0 <= c < L:
            nb[i, d] = sid(a, b, c)
parity = np.array([(x + y + z) % 2 for (x, y, z) in coords])

# ---- rule -------------------------------------------------------------------
PHI = np.zeros((6, 6))
for s in range(6):
    for t in range(6):
        if s == t:
            PHI[s, t] = P_
        elif s // 2 == t // 2:
            PHI[s, t] = Q_
        else:
            PHI[s, t] = R_
PHIX = np.vstack([np.ones((1, 6)), PHI])  # row v+1; row 0 = unrecorded neighbour
H_HAZ = np.array([1, 1, 1, 1, 2, 2], dtype=float)


def rule_probs(nbv, hazard=None):
    """nbv (...,6) neighbour values (-1 = unrecorded/absent) -> probs (...,6)."""
    w = np.prod(PHIX[nbv + 1], axis=-2)  # (..., 6 dirs, 6 s) -> product over dirs
    if hazard is not None:
        w = w * hazard
    return w / w.sum(axis=-1, keepdims=True)


def draw(p):
    u = rng.random(p.shape[0])[:, None]
    c = np.cumsum(p, axis=1)
    return (u > c).sum(axis=1).clip(0, 5)


def gather_nb(vals, x):
    """vals (M,N); x (M,) site per history -> (M,6) neighbour values, -1 for absent/unrecorded."""
    m = np.arange(vals.shape[0])[:, None]
    idx = nb[x]  # (M,6)
    v = vals[m, np.maximum(idx, 0)]
    return np.where(idx >= 0, v, -1)


# ---- worlds -----------------------------------------------------------------
def world_formation(M, order_mode="random", hazard=None):
    vals = -np.ones((M, N), dtype=np.int64)
    P = np.zeros((M, N, 6), dtype=np.float32)   # predictive probs under r
    Ph = np.zeros((M, N, 6), dtype=np.float32)  # predictive probs under r_h (content law given formation)
    X = np.zeros((M, N), dtype=np.int64)
    if order_mode == "random":
        order = rng.permuted(np.tile(np.arange(N), (M, 1)), axis=1)
    else:
        score = np.zeros((M, N))
        unrec = np.ones((M, N), dtype=bool)
    m = np.arange(M)
    for t in range(N):
        if order_mode == "random":
            x = order[:, t]
        else:  # value-dependent ADAPTED order: prefer sites with many recorded +z neighbours
            s_ = np.where(unrec, score + 0.5 * rng.random((M, N)), -1e9)
            x = s_.argmax(axis=1)
        nbv = gather_nb(vals, x)
        p = rule_probs(nbv)
        ph = rule_probs(nbv, hazard) if hazard is not None else p
        s = draw(ph)
        vals[m, x] = s
        P[:, t, :] = p
        Ph[:, t, :] = ph
        X[:, t] = s
        if order_mode != "random":
            unrec[m, x] = False
            hit = (s == 4)  # +z recorded
            for d in range(6):
                nn = nb[x, d]
                ok = (nn >= 0) & hit
                score[m[ok], nn[ok]] += 1.0
    return vals, P, Ph, X


def world_static(M, sweeps=150):
    vals = rng.integers(0, 6, size=(M, N))
    sites = [np.where(parity == par)[0] for par in (0, 1)]
    CH = 3000
    for c0 in range(0, M, CH):
        v = vals[c0:c0 + CH]
        for _ in range(sweeps):
            for par in (0, 1):
                sx = sites[par]
                idx = nb[sx]                            # (ns,6)
                nbv = np.where(idx[None] >= 0, v[:, np.maximum(idx, 0)], -1)  # (m,ns,6)
                p = rule_probs(nbv)                     # (m,ns,6)
                cum = np.cumsum(p, axis=2)
                u = rng.random(p.shape[:2])[:, :, None]
                v[:, sx] = (u > cum).sum(axis=2).clip(0, 5)
        vals[c0:c0 + CH] = v
    return vals


# ---- observers --------------------------------------------------------------
def static_probs(vals, sites):
    idx = nb[sites]
    nbv = np.where(idx[None] >= 0, vals[:, np.maximum(idx, 0)], -1)
    return rule_probs(nbv)  # (M, ns, 6)


def imposed_order_probs(vals):
    Mv = vals.shape[0]
    rank = np.argsort(rng.random((Mv, N)), axis=1).argsort(axis=1)  # random rank per history
    P = np.zeros((Mv, N, 6))
    m = np.arange(Mv)[:, None]
    for x in range(N):
        idx = nb[x]
        ok = idx >= 0
        nbrank = np.where(ok[None], rank[:, np.maximum(idx, 0)], 10 ** 9)  # (M,6)
        earlier = nbrank < rank[:, x][:, None]
        nbv = np.where(earlier, vals[:, np.maximum(idx, 0)], -1)
        P[:, x, :] = rule_probs(nbv)
    return P


# ---- calibration statistic ---------------------------------------------------
def calib(Pm, Xv, min_frac=0.05):
    """Pm (K,6) predicted probs, Xv (K,) outcomes. Returns dict."""
    K = Pm.shape[0]
    chi2_tot, df_tot, zmax, ece_tot = 0.0, 0, 0.0, 0.0
    per = []
    for s in range(6):
        p = Pm[:, s].astype(np.float64)
        y = (Xv == s).astype(np.float64)
        o = np.argsort(p, kind="stable")
        p, y = p[o], y[o]
        # distinct-value groups
        pr = np.round(p, 9)
        change = np.r_[True, pr[1:] != pr[:-1]]
        starts = np.flatnonzero(change)
        ends = np.r_[starts[1:], K]
        bins, cs = [], starts[0]
        for a, b in zip(starts, ends):
            if b - cs >= min_frac * K:
                bins.append((cs, b))
                cs = b
        if cs < K:
            if bins:
                bins[-1] = (bins[-1][0], K)
            else:
                bins.append((0, K))
        chi2, ece, zm = 0.0, 0.0, 0.0
        for a, b in bins:
            d = (y[a:b] - p[a:b]).sum()
            v = (p[a:b] * (1 - p[a:b])).sum()
            z = d / np.sqrt(v)
            chi2 += z * z
            zm = max(zm, abs(z))
            ece += (b - a) / K * abs(y[a:b].mean() - p[a:b].mean())
        per.append((s, len(bins), chi2 / len(bins), zm, ece))
        chi2_tot += chi2
        df_tot += len(bins)
        zmax = max(zmax, zm)
        ece_tot += ece / 6
    return dict(chi2_df=chi2_tot / df_tot, chi2=chi2_tot, df=df_tot, zmax=zmax, ece=ece_tot, K=K, per=per)


def show(tag, r):
    print(f"{tag:46s} K={r['K']:8d} chi2/df={r['chi2_df']:9.3f} (chi2={r['chi2']:.1f}, df={r['df']})  max|z|={r['zmax']:.2f}  ECE={r['ece']:.5f}")


if __name__ == "__main__":
    t0 = time.time()
    print(f"M={M} histories per world, window {L}^3 open, phi=(3,1,2), seed={SEED}")
    evens = np.where(parity == 0)[0]
    results = {}

    # World F
    vals, P, Ph, X = world_formation(M, "random")
    r_a = calib(P.reshape(-1, 6), X.reshape(-1))
    show("(a)  F x Pred(true order)", r_a)
    qs = static_probs(vals, evens)
    r_c = calib(qs.reshape(-1, 6), vals[:, evens].reshape(-1))
    show("(c)  F x Stat (coding set, final pattern)", r_c)
    results["a"], results["c"] = r_a, r_c
    # excess chi2 per trial -> N for 4 sigma
    excess = (r_c["chi2"] - r_c["df"]) / r_c["K"]
    print(f"     excess chi2 per trial (F vs Stat) = {excess:.3e}; records for chi2 excess of 16: {16/excess:.0f}")
    # marginal value frequencies (sanity: symmetric => 1/6)
    print("     marginal value freq in F:", np.round(np.bincount(X.reshape(-1), minlength=6) / X.size, 4))
    # mean |r_t - static| total variation over even sites (descriptive)
    # Predictive probs at even sites, aligned by site: need order info; compute via stored steps
    print(f"     [{time.time()-t0:.0f}s]")

    # World F2 (value-dependent adapted order)
    vals2, P2, _, X2 = world_formation(M, "adapted")
    r_a2 = calib(P2.reshape(-1, 6), X2.reshape(-1))
    show("(a2) F2 x Pred (value-dependent adapted order)", r_a2)
    qs2 = static_probs(vals2, evens)
    r_c2 = calib(qs2.reshape(-1, 6), vals2[:, evens].reshape(-1))
    show("     F2 x Stat", r_c2)
    print("     F2 marginal value freq:", np.round(np.bincount(X2.reshape(-1), minlength=6) / X2.size, 4))
    results["a2"] = r_a2
    print(f"     [{time.time()-t0:.0f}s]")

    # World S
    valsS = world_static(M)
    qsS = static_probs(valsS, evens)
    r_b = calib(qsS.reshape(-1, 6), valsS[:, evens].reshape(-1))
    show("(b)  S x Stat (coding set)", r_b)
    PS = imposed_order_probs(valsS)
    r_d = calib(PS.reshape(-1, 6), valsS.reshape(-1))
    show("(d)  S x Pred(imposed random order)", r_d)
    results["b"], results["d"] = r_b, r_d
    print(f"     [{time.time()-t0:.0f}s]")

    # World H
    valsH, PH, PhH, XH = world_formation(M, "random", hazard=H_HAZ)
    r_e1 = calib(PH.reshape(-1, 6), XH.reshape(-1))
    show("(e)  H x Pred(r)   [odds read as pre-formation r]", r_e1)
    r_e2 = calib(PhH.reshape(-1, 6), XH.reshape(-1))
    show("     H x Pred(r_h) [odds = content law given formation]", r_e2)
    results["e1"], results["e2"] = r_e1, r_e2
    print(f"     [{time.time()-t0:.0f}s]")

    # verdicts
    def inband(r): return 0.6 <= r["chi2_df"] <= 1.6 and r["zmax"] < 4.5
    print("\nVERDICTS against PREREG.md")
    print(" (a)  F x Pred in band            :", inband(results["a"]))
    print(" (a2) F2 x Pred in band           :", inband(results["a2"]))
    print(" (b)  S x Stat in band            :", inband(results["b"]))
    print(" (c)  F x Stat chi2/df >= 5       :", results["c"]["chi2_df"] >= 5)
    print(" (d)  S x Pred(imposed) >= 5      :", results["d"]["chi2_df"] >= 5)
    print(" (e)  H x Pred(r) >=5 & r_h in band:", results["e1"]["chi2_df"] >= 5 and inband(results["e2"]))
