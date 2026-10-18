"""T-SPIRAL simulation: irreversible record formation on the torus Z_L^d.
Content: P(s|N) = e^{K s m}/(2cosh K m), m = sum of recorded neighbour values (binary class (P), formation reading).
Order:   hazard e^{mu n}, n = number of recorded neighbours (record-determined clock; mu = 0 uniform race).
Exact rejection-free KMC (embedded jump chain; times are not readable). Records never unlock.
Also returns the path score (d/dK, d/dmu of log P(path)) for score-function derivatives.
usage: python3 sim.py OUT.npz d L_big b S [quick]
"""
import sys, time
import numpy as np
from numba import njit, prange

@njit(cache=True)
def nbr_table(L, d):
    N = L ** d
    nb = np.empty((N, 2 * d), np.int32)
    for x in range(N):
        r = x
        coords = np.empty(d, np.int64)
        for a in range(d):
            coords[a] = r % L
            r //= L
        k = 0
        for a in range(d):
            stride = L ** a
            for step in (1, -1):
                c = (coords[a] + step) % L
                nb[x, k] = x + (c - coords[a]) * stride
                k += 1
    return nb

@njit(cache=True)
def one_run(nb, N, z, K, mu, seed, out_state):
    np.random.seed(seed)
    ncls = z + 1
    lists = np.empty((ncls, N), np.int32)
    pos = np.empty(N, np.int32)
    cnt = np.zeros(ncls, np.int64)
    nrec = np.zeros(N, np.int32)
    msum = np.zeros(N, np.int32)
    for x in range(N):
        lists[0, x] = x
        pos[x] = x
        out_state[x] = 0
    cnt[0] = N
    w = np.empty(ncls)
    for c in range(ncls):
        w[c] = np.exp(mu * c)
    sK = 0.0
    sM = 0.0
    nuc = 0
    for step in range(N):
        tot = 0.0
        mom = 0.0
        for c in range(ncls):
            tot += cnt[c] * w[c]
            mom += c * cnt[c] * w[c]
        r = np.random.random() * tot
        cc = ncls - 1
        acc = 0.0
        for c in range(ncls):
            acc += cnt[c] * w[c]
            if r < acc and cnt[c] > 0:
                cc = c
                break
        while cnt[cc] == 0:
            cc -= 1
        idx = np.random.randint(0, cnt[cc])
        x = lists[cc, idx]
        last = lists[cc, cnt[cc] - 1]
        lists[cc, idx] = last
        pos[last] = idx
        cnt[cc] -= 1
        sM += cc - mom / tot
        if cc == 0:
            nuc += 1
        m = msum[x]
        pplus = 1.0 / (1.0 + np.exp(-2.0 * K * m))
        s = 1 if np.random.random() < pplus else -1
        sK += s * m - m * np.tanh(K * m)
        out_state[x] = s
        for k in range(z):
            y = nb[x, k]
            if out_state[y] == 0:
                c0 = nrec[y]
                i0 = pos[y]
                l0 = lists[c0, cnt[c0] - 1]
                lists[c0, i0] = l0
                pos[l0] = i0
                cnt[c0] -= 1
                c1 = c0 + 1
                nrec[y] = c1
                lists[c1, cnt[c1]] = y
                pos[y] = cnt[c1]
                cnt[c1] += 1
                msum[y] += s
    return sK, sM, nuc

@njit(parallel=True, cache=True)
def many_runs(nb, N, z, K, mu, seed0, S):
    states = np.empty((S, N), np.int8)
    scores = np.empty((S, 3))
    for i in prange(S):
        st = np.empty(N, np.int8)
        a, b, c = one_run(nb, N, z, K, mu, seed0 + 7919 * i, st)
        states[i, :] = st
        scores[i, 0] = a
        scores[i, 1] = b
        scores[i, 2] = c
    return states, scores

def block(cfg, d, b, rng):
    """majority rule on b^d blocks; cfg shape (S, L,...,L); ties -> fair coin"""
    S, L = cfg.shape[0], cfg.shape[1]
    Lb = L // b
    shp = [S]
    for _ in range(d):
        shp += [Lb, b]
    t = cfg.reshape(shp).astype(np.int16)
    t = t.sum(axis=tuple(range(2, 2 * d + 1, 2)))
    out = np.sign(t).astype(np.int8)
    ties = out == 0
    if ties.any():
        out[ties] = rng.choice(np.array([-1, 1], np.int8), size=int(ties.sum()))
    return out

def observables(cfg, d):
    """per-sample: nn, plaquette, face diagonal, axis distance-2, (2^d block magnetisation)^2"""
    f = cfg.astype(np.float32)
    ax = list(range(1, d + 1))
    nn = np.mean([np.mean(f * np.roll(f, 1, a), axis=tuple(ax)) for a in ax], axis=0)
    pl, dg = [], []
    for i in range(d):
        for j in range(i + 1, d):
            a, b = ax[i], ax[j]
            fa = np.roll(f, 1, a); fb = np.roll(f, 1, b); fab = np.roll(fa, 1, b)
            pl.append(np.mean(f * fa * fb * fab, axis=tuple(ax)))
            fam = np.roll(np.roll(f, 1, a), -1, b)
            dg.append(0.5 * np.mean(f * fab + f * fam, axis=tuple(ax)))
    pl = np.mean(pl, axis=0); dg = np.mean(dg, axis=0)
    d2 = np.mean([np.mean(f * np.roll(f, 2, a), axis=tuple(ax)) for a in ax], axis=0)
    S, L = cfg.shape[0], cfg.shape[1]
    shp = [S]
    for _ in range(d):
        shp += [L // 2, 2]
    bm = f.reshape(shp).mean(axis=tuple(range(2, 2 * d + 1, 2)))
    bm2 = np.mean(bm ** 2, axis=tuple(range(1, d + 1)))
    return np.stack([nn, pl, dg, d2, bm2], axis=1)

def xi2(cfg, d, rmax=16):
    """axis correlation function C(r), r = 0..rmax, averaged over axes, sites and samples"""
    f = cfg.astype(np.float32)
    ax = tuple(range(1, d + 1))
    return np.array([np.mean([np.mean(f * np.roll(f, r, a)) for a in ax]) for r in range(rmax + 1)])

def run_size(d, L, b, levels, K, mu, S, seed, rng, chunk=64):
    nb = nbr_table(L, d)
    N = L ** d
    res = {lev: [] for lev in levels}
    scs, xis = [], []
    for c0 in range(0, S, chunk):
        Sc = min(chunk, S - c0)
        states, scores = many_runs(nb, N, 2 * d, K, mu, seed + 104729 * c0, Sc)
        cfg = states.reshape((Sc,) + (L,) * d)
        xis.append(xi2(cfg, d))
        cur = cfg
        for lev in range(max(levels) + 1):
            if lev in levels:
                res[lev].append(observables(cur, d))
            if lev < max(levels):
                cur = block(cur, d, b, rng)
        scs.append(scores[:, :2])
    res = {lev: np.concatenate(v) for lev, v in res.items()}
    return res, np.concatenate(scs), np.mean(xis, axis=0)

if __name__ == "__main__":
    out, d, Lbig, b, S = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    quick = len(sys.argv) > 6
    nlev = 2 if (Lbig // b ** 2) >= 4 and not (d == 3 and b == 3) else 1
    tK = np.array([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, .95])
    MU = np.arange(-3, 10, 1.0)
    if quick:
        tK = np.array([0.5]); MU = np.array([0.0, 4.0])
    rng = np.random.default_rng(20261018 + 31 * d + b)
    Ls = Lbig // b
    # big lattice: levels 1..nlev ; small lattice: levels 0..nlev-1
    shapeA = (len(tK), len(MU))
    data = {k: np.zeros(shapeA + (5,)) for k in ["big_m", "big_e", "small_m", "small_e"]}
    data = {}
    t0 = time.time()
    for i, tk in enumerate(tK):
        K = float(np.arctanh(tk))
        for j, mu in enumerate(MU):
            seed = int(1000003 * (i + 1) + 7777 * (j + 1) + 13 * d + b)
            rb, scb, xib = run_size(d, Lbig, b, list(range(1, nlev + 1)), K, mu, S, seed, rng)
            rs, scs, xis = run_size(d, Ls, b, list(range(0, nlev)), K, mu, S, seed + 5, rng)
            for n in range(nlev):
                ob, os_ = rb[n + 1], rs[n]
                for tag, o, sc in (("big", ob, scb), ("small", os_, scs)):
                    key = f"{tag}_n{n}"
                    data.setdefault(key + "_m", np.zeros(shapeA + (5,)))[i, j] = o.mean(0)
                    data.setdefault(key + "_e", np.zeros(shapeA + (5,)))[i, j] = o.std(0, ddof=1) / np.sqrt(S)
                    oc = o - o.mean(0); scc = sc - sc.mean(0)
                    data.setdefault(key + "_J", np.zeros(shapeA + (5, 2)))[i, j] = (oc[:, :, None] * scc[:, None, :]).mean(0)
            data.setdefault("C_big", np.zeros(shapeA + (17,)))[i, j] = xib
        print(f"tK={tk:.2f} done, elapsed {time.time()-t0:.1f}s, C_big(r=1,4,8,16)={np.round(data['C_big'][i][:, [1,4,8,16]],3).tolist()}", flush=True)
    np.savez(out, tK=tK, MU=MU, d=d, Lbig=Lbig, b=b, S=S, nlev=nlev, **data)
    print("saved", out, "total", round(time.time() - t0, 1), "s")
