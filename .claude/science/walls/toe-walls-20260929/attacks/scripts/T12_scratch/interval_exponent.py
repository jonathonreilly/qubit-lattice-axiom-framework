"""T12 test: interval-size exponent of event posets on Z^3 (site-once vs turnover).
Pre-registration: PREREG.md (same folder). Run: python3 interval_exponent.py [quick]

Estimator (fixed before the final run, see PREREG.md addendum): for a target event y and each
longest-chain height h, take the M ancestors x with longest chain h(x,y) = h that are spatially
NEAREST to y in l1 distance (rest-frame choice; the volume-height lemma bounds the maximum over
x, so the maximum is the right statistic), compute N(x,y) = |[x,y]| for each and record max/median.
"""
import sys, json, itertools, time
import numpy as np
from numba import njit
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

rng = np.random.default_rng(20260929)
QUICK = len(sys.argv) > 1 and sys.argv[1] == "quick"


def B3(h):
    return (2 * h + 1) * (2 * h * h + 2 * h + 3) / 3.0


@njit(cache=True)
def anc_lp(preds, y):
    n, K = preds.shape
    lp = np.full(n, -1, np.int32)
    lp[y] = 0
    for e in range(y, -1, -1):
        le = lp[e]
        if le < 0:
            continue
        for k in range(K):
            p = preds[e, k]
            if p < 0:
                continue
            if lp[p] < le + 1:
                lp[p] = le + 1
    return lp


@njit(cache=True)
def interval_count(preds, x, y, lp):
    """|{z : x <= z <= y}| : z in Anc(y) (lp>=0) and descendant of x (endpoints included)."""
    n, K = preds.shape
    mark = np.zeros(y + 1, np.uint8)
    mark[x] = 1
    cnt = 1
    for e in range(x + 1, y + 1):
        if lp[e] < 0:
            continue
        m = 0
        for k in range(K):
            p = preds[e, k]
            if p >= x and mark[p] == 1:
                m = 1
                break
        if m == 1:
            mark[e] = 1
            cnt += 1
    return cnt


def d1(pos, cand, y, L, periodic):
    d = np.abs(pos[cand] - pos[y][None, :])
    if periodic:
        d = np.minimum(d, L - d)
    return d.sum(axis=1)


def sample_pairs(preds, pos, L, periodic, ys, hs, M, res):
    for y in ys:
        lp = anc_lp(preds, y)
        for h in hs:
            cand = np.nonzero(lp == h)[0]
            if len(cand) == 0:
                continue
            dist = d1(pos, cand, y, L, periodic) + 1e-3 * rng.random(len(cand))
            take = cand[np.argsort(dist)[:M]]
            for x in take:
                res.setdefault(h, []).append(interval_count(preds, int(x), int(y), lp))
    return res


def fit(res, hmin=4, hmax=None):
    hs = sorted(h for h in res if h >= hmin and (hmax is None or h <= hmax) and len(res[h]) >= 3)
    if len(hs) < 3:
        return None
    lx = np.log(hs)
    mx = [float(np.max(res[h])) for h in hs]
    md = [float(np.median(res[h])) for h in hs]
    p_max = float(np.polyfit(lx, np.log(mx), 1)[0])
    p_med = float(np.polyfit(lx, np.log(md), 1)[0])
    k = max(1, len(hs) // 3)
    p_hi = float((np.log(mx[-1]) - np.log(mx[-k - 1])) / (np.log(hs[-1]) - np.log(hs[-k - 1])))
    return dict(p_max=p_max, p_med=p_med, p_max_upper_third=p_hi, hs=hs, max=mx, med=md,
                ratio_max=[m / B3(h) for m, h in zip(mx, hs)],
                maxratio_all=float(max(max(res[h]) / B3(h) for h in res)))


# ---------- site-once posets ----------
def grid_preds(t, L):
    n = L ** 3
    order = np.argsort(t, kind="stable")
    rank = np.empty(n, np.int64)
    rank[order] = np.arange(n)
    idx = np.arange(n).reshape(L, L, L)
    P = np.full((n, 6), -1, np.int32)
    k = 0
    for ax in range(3):
        for s in (-1, 1):
            nbr = np.full((L, L, L), -1, np.int64)
            src = [slice(None)] * 3
            dst = [slice(None)] * 3
            if s == 1:
                src[ax] = slice(0, L - 1); dst[ax] = slice(1, L)
            else:
                src[ax] = slice(1, L); dst[ax] = slice(0, L - 1)
            nbr[tuple(dst)] = idx[tuple(src)]
            nbr = nbr.reshape(-1)
            nodes = np.nonzero(nbr >= 0)[0]
            rn = rank[nbr[nodes]]
            rv = rank[nodes]
            good = rn < rv
            P[rv[good], k] = rn[good]
            k += 1
    X, Y, Z = np.meshgrid(*(np.arange(L),) * 3, indexing="ij")
    coords = np.stack([X.reshape(-1), Y.reshape(-1), Z.reshape(-1)], axis=1)
    pos = np.empty((n, 3), np.int64)
    pos[rank] = coords  # event index = rank
    return P, rank, pos


def grid_graph(L, w):
    n = L ** 3
    idx = np.arange(n).reshape(L, L, L)
    rows, cols = [], []
    for ax in range(3):
        a = [slice(None)] * 3; b = [slice(None)] * 3
        a[ax] = slice(0, L - 1); b[ax] = slice(1, L)
        u = idx[tuple(a)].reshape(-1); v = idx[tuple(b)].reshape(-1)
        rows += [u, v]; cols += [v, u]
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    return csr_matrix((w[cols], (rows, cols)), shape=(n, n))


def eden_times(L, seed_plane=False):
    n = L ** 3
    w = rng.exponential(1.0, size=n)
    G = grid_graph(L, w)
    idx = np.arange(n).reshape(L, L, L)
    src = idx[:, :, 0].reshape(-1) if seed_plane else [idx[L // 2, L // 2, L // 2]]
    d = dijkstra(G, directed=True, indices=src, min_only=True)
    return d + 1e-9 * rng.random(n)


def pick_ys(L, n, mode):
    X, Y, Z = np.meshgrid(*(np.arange(L),) * 3, indexing="ij")
    if mode == "point":
        c = L // 2
        r = np.sqrt((X - c) ** 2 + (Y - c) ** 2 + (Z - c) ** 2)
        m = (r > 0.55 * L / 2 * 2 * 0.5) & (r < 0.8 * L / 2)
    elif mode == "plane":
        m = (Z > 0.55 * L) & (Z < 0.7 * L) & (X > L // 5) & (X < L - L // 5) & (Y > L // 5) & (Y < L - L // 5)
    else:
        m = (X > L // 6) & (X < L - L // 6) & (Y > L // 6) & (Y < L - L // 6) & (Z > L // 6) & (Z < L - L // 6)
    cand = np.nonzero(m.reshape(-1))[0]
    return rng.choice(cand, size=n, replace=False)


# ---------- turnover posets ----------
@njit(cache=True)
def sim_async_ca(L, nevents, seed):
    np.random.seed(seed)
    n = L * L * L
    last = np.full(n, -1, np.int32)
    preds = np.full((nevents, 7), -1, np.int32)
    site = np.empty(nevents, np.int32)
    for e in range(nevents):
        z = np.random.randint(0, n)
        x = z // (L * L); y = (z // L) % L; w = z % L
        preds[e, 0] = last[z]
        preds[e, 1] = last[((x + 1) % L) * L * L + y * L + w]
        preds[e, 2] = last[((x - 1) % L) * L * L + y * L + w]
        preds[e, 3] = last[x * L * L + ((y + 1) % L) * L + w]
        preds[e, 4] = last[x * L * L + ((y - 1) % L) * L + w]
        preds[e, 5] = last[x * L * L + y * L + (w + 1) % L]
        preds[e, 6] = last[x * L * L + y * L + (w - 1) % L]
        last[z] = e
        site[e] = z
    return preds, site


@njit(cache=True)
def sim_ssep(L, rho, nattempts, seed):
    np.random.seed(seed)
    n = L * L * L
    occ = np.zeros(n, np.uint8)
    for z in range(n):
        if np.random.random() < rho:
            occ[z] = 1
    last = np.full(n, -1, np.int32)
    preds = np.full((nattempts, 2), -1, np.int32)
    site = np.empty(nattempts, np.int32)
    e = 0
    nocc = 0
    pos = np.empty(n, np.int32)
    for z in range(n):
        if occ[z] == 1:
            pos[nocc] = z
            nocc += 1
    for it in range(nattempts):
        i = np.random.randint(0, nocc)
        a = pos[i]
        x = a // (L * L); y = (a // L) % L; w = a % L
        d = np.random.randint(0, 6)
        if d == 0: x = (x + 1) % L
        elif d == 1: x = (x - 1) % L
        elif d == 2: y = (y + 1) % L
        elif d == 3: y = (y - 1) % L
        elif d == 4: w = (w + 1) % L
        else: w = (w - 1) % L
        b = x * L * L + y * L + w
        if occ[b] == 1:
            continue
        preds[e, 0] = last[a]
        preds[e, 1] = last[b]
        last[a] = e
        last[b] = e
        occ[a] = 0
        occ[b] = 1
        pos[i] = b
        site[e] = b
        e += 1
    return preds[:e], site[:e]


def sync_lightcone(L, T):
    """synchronous Z^3 x N: event (t,x) depends on (t-1,x) and (t-1,x+-e_j): exactly 3+1, 7 preds."""
    n = L ** 3
    idx = np.arange(n).reshape(L, L, L)
    nbrs = [idx]
    for ax in range(3):
        for s_ in (1, -1):
            nbrs.append(np.roll(idx, s_, axis=ax))
    nb = np.stack([a.reshape(-1) for a in nbrs], axis=1)
    preds = np.full((n * T, 7), -1, np.int32)
    for t in range(1, T):
        preds[t * n:(t + 1) * n] = nb + (t - 1) * n
    site = np.tile(np.arange(n), T).astype(np.int32)
    return preds, site


def site_to_pos(site, L):
    return np.stack([site // (L * L), (site // L) % L, site % L], axis=1).astype(np.int64)


def run_turnover(preds, site, L, hs, M, nys, lo_frac=0.9):
    """Rest-frame sampling for turnover posets: for each target y, candidates x are ALL earlier
    events located at the y's site or its 6 lattice neighbours (l1 <= 1) that are ancestors of y;
    each is binned by its measured longest-chain height h(x,y) (no exact-h selection)."""
    n = preds.shape[0]
    ys = rng.choice(np.arange(int(lo_frac * n), n), size=nys, replace=False)
    res = {}
    for y in ys:
        lp = anc_lp(preds, int(y))
        zy = int(site[y])
        x0, y0, w0 = zy // (L * L), (zy // L) % L, zy % L
        near = [zy]
        for dx, dy, dw in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            near.append(((x0 + dx) % L) * L * L + ((y0 + dy) % L) * L + (w0 + dw) % L)
        cand = np.nonzero(np.isin(site[:y], near) & (lp[:y] >= 2))[0]
        for x in cand:
            res.setdefault(int(lp[x]), []).append(interval_count(preds, int(x), int(y), lp))
    return res


def main():
    out = {}
    t0 = time.time()
    # (f) covariance of the level order's predecessor set under the 24 proper cubic rotations
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            Mx = np.zeros((3, 3), int)
            for i, p in enumerate(perm):
                Mx[i, p] = signs[i]
            if round(np.linalg.det(Mx)) == 1:
                mats.append(Mx)
    pred = {(-1, 0, 0), (0, -1, 0), (0, 0, -1)}
    stab = sum(1 for Mx in mats if {tuple(int(c) for c in Mx @ np.array(v)) for v in pred} == pred)
    out["proper_rotations"] = len(mats)
    out["stabiliser_of_level_predecessor_set"] = stab
    # (g) the wall's numbers
    inc = np.array([(0, 0), (1, 0), (0, 1)], float)
    mean = inc.mean(axis=0)
    d = inc - mean
    out["step_mean"] = mean.tolist()
    out["step_cov"] = (d.T @ d / 3).tolist()
    out["step_third_central"] = {"xxx": float(np.mean(d[:, 0] ** 3)), "xxy": float(np.mean(d[:, 0] ** 2 * d[:, 1])),
                                 "xyy": float(np.mean(d[:, 0] * d[:, 1] ** 2)), "yyy": float(np.mean(d[:, 1] ** 3))}
    out["two_over_27"] = 2 / 27
    out["minus_one_over_27"] = -1 / 27
    ok = True
    for m in range(1, 7):
        cnt = sum(1 for a in range(-m, m + 1) for b in range(-m, m + 1) for c in range(-m, m + 1)
                  if abs(a) + abs(b) + abs(c) <= m)
        ok &= (abs(cnt - B3(m)) < 1e-9)
    out["ball_formula_ok"] = bool(ok)
    ng = 96
    k = (np.arange(ng) + 0.5) * 2 * np.pi / ng - np.pi
    K1, K2, K3 = np.meshgrid(k, k, k, indexing="ij")
    E = 6 - 2 * (np.cos(K1) + np.cos(K2) + np.cos(K3))
    I2 = float(np.mean(1 / (E + 2)))
    I0 = 0.25273100985866  # Watson integral for 1/(6 - 2 sum cos)
    out["I0"] = I0; out["I2_midpoint96"] = I2; out["onset_3(I0+I2)/2"] = 1.5 * (I0 + I2)

    # --- E1 level/product order (exact enumeration of all compositions) ---
    res1 = {}
    for h in range(2, 61):
        res1[h] = [(a + 1) * (b + 1) * (h - a - b + 1) for a in range(h + 1) for b in range(h - a + 1)]
    out["E1"] = fit(res1, 4, 60)
    out["E1_max_ratio_N_over_B3"] = max(max(v) / B3(h) for h, v in res1.items())

    # --- E2 Eden point seed, E2b plane seed, E3 iid ---
    Lg = 41 if QUICK else 61
    hs_grid = [2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32]
    for name, mode in (("E2_eden_point", "point"), ("E2b_eden_plane", "plane")):
        t = eden_times(Lg, seed_plane=(mode == "plane"))
        P, rank, pos = grid_preds(t, Lg)
        ys_nodes = pick_ys(Lg, 12 if not QUICK else 4, mode)
        ys = rank[ys_nodes]
        res = {}
        sample_pairs(P, pos, Lg, False, ys, hs_grid, 60, res)
        out[name] = dict(fit=fit(res, 4), fit_h_le_16=fit(res, 4, 16), counts={int(h): len(v) for h, v in res.items()})
        print(name, "done", round(time.time() - t0, 1), "s", flush=True)
    t = rng.random(Lg ** 3)
    P, rank, pos = grid_preds(t, Lg)
    ys = rank[pick_ys(Lg, 40 if not QUICK else 8, "interior")]
    hist = {}
    for y in ys:
        m = int(anc_lp(P, int(y)).max())
        hist[m] = hist.get(m, 0) + 1
    out["E3_iid"] = dict(max_height_over_targets=max(hist), per_target_max_height_histogram=hist)
    print("E3 done", round(time.time() - t0, 1), flush=True)

    hs_t = [2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 25, 28]
    # --- E4 asynchronous CA (turnover) ---
    Lc = 32 if QUICK else 44
    T = 12 if QUICK else 24
    nev = int(Lc ** 3 * T)
    preds, site = sim_async_ca(Lc, nev, 11)
    res = run_turnover(preds, site, Lc, hs_t, 25, 5 if not QUICK else 3)
    out["E4_async_ca"] = dict(fit=fit(res, 4), fit_h_le_20=fit(res, 4, 20), counts={int(h): len(v) for h, v in res.items()}, nevents=nev)
    print("E4 done", round(time.time() - t0, 1), flush=True)

    # --- E6 synchronous 3+1 calibration ---
    Lc6 = 24 if QUICK else 36
    preds, site = sync_lightcone(Lc6, 40 if not QUICK else 22)
    res = run_turnover(preds, site, Lc6, hs_t, 25, 4 if not QUICK else 2, lo_frac=0.97)
    out["E6_sync_lightcone_3plus1"] = dict(fit=fit(res, 4), counts={int(h): len(v) for h, v in res.items()})
    print("E6 done", round(time.time() - t0, 1), flush=True)

    # --- E5 SSEP moving records ---
    for rho, T5 in ((0.5, 90), (0.2, 180)):
        Ls = 32 if QUICK else 44
        natt = int(rho * Ls ** 3 * T5)
        preds, site = sim_ssep(Ls, rho, natt, 5)
        res = run_turnover(preds, site, Ls, hs_t, 25, 5 if not QUICK else 3)
        out["E5_ssep_rho%.1f" % rho] = dict(fit=fit(res, 4), fit_h_le_20=fit(res, 4, 20),
                                            counts={int(h): len(v) for h, v in res.items()}, nevents=int(preds.shape[0]))
        print("E5", rho, "done", round(time.time() - t0, 1), flush=True)

    with open("interval_exponent_results%s.json" % ("_quick" if QUICK else ""), "w") as fh:
        json.dump(out, fh, indent=1, default=float)

    def brief(v):
        if not isinstance(v, dict):
            return v
        r = {}
        for kk, vv in v.items():
            if isinstance(vv, dict) and "p_max" in vv:
                r[kk] = {a: (round(b, 3) if isinstance(b, float) else b) for a, b in vv.items()
                         if a in ("p_max", "p_med", "p_max_upper_third", "maxratio_all")}
                r[kk]["h_range"] = [vv["hs"][0], vv["hs"][-1]]
                r[kk]["ratio_max_first_last"] = [round(vv["ratio_max"][0], 4), round(vv["ratio_max"][-1], 4)]
            elif kk in ("max_height_over_targets", "per_target_max_height_histogram", "nevents"):
                r[kk] = vv
        return r
    for k, v in out.items():
        if k == "E1":
            v = {"E1": v}
        print(k, json.dumps(brief(v), default=float) if isinstance(v, dict) else v)


if __name__ == "__main__":
    main()
