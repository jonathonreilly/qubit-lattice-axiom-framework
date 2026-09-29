"""PR 9008 attack-e: SAMPLED EVIDENCE.  The note's 'the transverse form holds within about 0.2%' and 'no seed set exceeds 0.25% in any multiset' rest on
five hand-picked multisets and random seeds.  Adversarial replacement of more samples of the same five: an own numba directed-loop sampler (8 fresh seeds x 1.5M loops at
L = 16, the note's estimator) is searched over ALL 23 contrasts (every multiset with |k|^2 <= 18, every pair of usable assignments) for the largest standardised
difference (calibrated by a centred block bootstrap of the maximum), and the optimal linear detector of the only distortion the assignment test can see
(S = P (1 + eps h)/K with h singling out the z axis; h = s_z^2 and h = s_z^4/Q) is fitted over all contrasts at once, with its implied size in the note's five rows.
Uses PR9008_ATTACK_CACHE (the sibling attack-d data) when present, otherwise runs the sampler.
"""
import os, sys, time, math, itertools
import numpy as np
from numba import njit
from multiprocessing import Pool

L = 16
N = L ** 3
NSEED, NLOOP, BASE = 8, int(os.environ.get('PR9008_TEST_NLOOP', 1_500_000)), 250          # 8 fresh seeds x 1.5M loops; batch means of 250 loops are stored
SEEDS = [9101 + i for i in range(NSEED)]
CACHE = os.environ.get("PR9008_ATTACK_CACHE", "")   # optional .npz reused between the two attack scripts; regenerated when absent

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

@njit(cache=False)
def seed_nb(s):
    np.random.seed(s)

@njit(cache=False)
def one_loop(E, L):
    """one directed-loop update: start at a random site, leave by a random outgoing arrow other than the one just reversed, stop on return to the start."""
    x0 = np.random.randint(L); y0 = np.random.randint(L); z0 = np.random.randint(L)
    x = x0; y = y0; z = z0
    lastl = -1
    cd = np.empty(6, np.int64); cl = np.empty(6, np.int64)
    steps = 0
    while True:
        m = 0
        for d in range(6):
            i = d % 3
            if d < 3:
                bx = x; by = y; bz = z
                out = E[i, bx, by, bz] == 1
            else:
                bx = (x - 1) % L if i == 0 else x
                by = (y - 1) % L if i == 1 else y
                bz = (z - 1) % L if i == 2 else z
                out = E[i, bx, by, bz] == -1
            if out:
                lid = ((i * L + bx) * L + by) * L + bz
                if lid != lastl:
                    cd[m] = d; cl[m] = lid; m += 1
        k = np.random.randint(m)
        d = cd[k]; lid = cl[k]
        i = d % 3
        bz = lid % L; t = lid // L; by = t % L; t //= L; bx = t % L
        E[i, bx, by, bz] = -E[i, bx, by, bz]
        lastl = lid
        if d < 3:
            if i == 0: x = (x + 1) % L
            elif i == 1: y = (y + 1) % L
            else: z = (z + 1) % L
        else:
            x = bx; y = by; z = bz
        steps += 1
        if x == x0 and y == y0 and z == z0:
            return steps

def start_config():
    E = np.empty((3, L, L, L), np.int8); alt = (-1) ** np.arange(L)
    E[0] = alt[None, :, None]; E[1] = alt[None, None, :]; E[2] = alt[:, None, None]
    return E

# ---- wavevector groups: every folded multiset with 0 < |k|^2 <= 18, split by the folded z-component, usable when P_zz > 0.05
kk = 2 * np.pi * np.arange(L) / L
s2 = 2 - 2 * np.cos(kk)
Qk = s2[:, None, None] + s2[None, :, None] + s2[None, None, :]
Pk = np.zeros((L, L, L)); _nz = Qk > 0
Pk[_nz] = 1 - np.broadcast_to(s2[None, None, :], Qk.shape)[_nz] / Qk[_nz]
fold = np.minimum(np.arange(L), L - np.arange(L))
FX, FY, FZ = np.meshgrid(fold, fold, fold, indexing="ij")
F2 = FX ** 2 + FY ** 2 + FZ ** 2
MULTISETS = sorted({tuple(sorted((a, b, c))) for a in range(5) for b in range(5) for c in range(5) if 0 < a * a + b * b + c * c <= 18})
GROUPS = []   # (multiset, zfold)
gid = -np.ones((L, L, L), np.int64)
for m in MULTISETS:
    for zc in sorted(set(m)):
        rest = list(m); rest.remove(zc)
        mk = (FZ == zc) & (np.minimum(FX, FY) == min(rest)) & (np.maximum(FX, FY) == max(rest)) & (Pk > 0.05)
        if mk.sum():
            gid[mk] = len(GROUPS); GROUPS.append((m, zc))
G = len(GROUPS)
gflat = gid.ravel(); VALID = np.nonzero(gflat >= 0)[0]; GV = gflat[VALID]
SUMP = np.bincount(GV, weights=Pk.ravel()[VALID], minlength=G)      # sum of P_zz over each group
GAVGS2 = np.bincount(GV, weights=(Pk.ravel()[VALID] * s2[np.indices((L, L, L))[2].ravel()[VALID]]), minlength=G) / SUMP   # P-weighted <s_z^2> of each group
KC = (2 * N + 1) / (3 * N)
NOTE5 = [(0, 1, 1), (0, 1, 2), (0, 2, 2), (1, 1, 2), (1, 2, 2)]

def seed_run(sd):
    seed_nb(sd)
    E = start_config()
    for _ in range(NLOOP // 20): one_loop(E, L)
    nb = NLOOP // BASE
    out = np.zeros((nb, G)); tot = 0
    for b in range(nb):
        acc = np.zeros(G)
        for t in range(BASE):
            tot += one_loop(E, L)
            F = np.fft.fftn(E[2].astype(np.float64))
            Sflat = (F.real ** 2 + F.imag ** 2).ravel()[VALID] / N
            acc += np.bincount(GV, weights=Sflat, minlength=G)
        out[b] = acc / BASE
    return out, tot / (nb * BASE)

def data():
    """returns array (NSEED, nbins, G): batch means (BASE loops) of sum_{k in group} S_zz(k)"""
    if CACHE and os.path.exists(CACHE):
        z = np.load(CACHE); return z["S"], float(z["steps"])
    with Pool(4) as pool:
        res = pool.map(seed_run, SEEDS)
    S = np.stack([r[0] for r in res]); steps = float(np.mean([r[1] for r in res]))
    if CACHE: np.savez(CACHE, S=S, steps=steps)
    return S, steps

def ratios(S):
    """R_g = K_cont * sum S / sum P per group; works on any leading shape"""
    return KC * S / SUMP

def contrasts(pairs_only_note=False):
    """(multiset, lowP group, highP group) for every multiset with >= 2 usable groups; all pairs when a multiset has 3 groups"""
    out = []
    for m in MULTISETS:
        idx = [i for i, (mm, zc) in enumerate(GROUPS) if mm == m]
        if len(idx) < 2: continue
        idx.sort(key=lambda i: SUMP[i] / (gid.ravel() == i).sum())   # by mean P
        for a, b in itertools.combinations(idx, 2):
            out.append((m, a, b))
    return out

# =====================================================================================================================
# attack-e  SAMPLED EVIDENCE: 'holds within about 0.2%', 'no seed set exceeds 0.25% in any multiset' rest on five hand-picked multisets.
# Adversarial replacement of more samples of the same five: (1) search ALL 23 contrasts (every multiset with |k|^2 <= 18, every pair of usable assignments)
# for the largest standardised difference, calibrated against a centred block bootstrap of the maximum; (2) the optimal linear detector of the only
# distortion the test can see (S = P(1 + eps h)/K with h singling out the z axis) fitted over all contrasts at once, with its implied size in the note's five rows.
# =====================================================================================================================
if __name__ == "__main__":
    T0 = time.time()
    HITS = []
    S, steps = data()
    ns, nb, _ = S.shape
    print(f"data: {ns} seeds x {nb * BASE} loops, {G} groups, mean worm length {steps:.0f}; {time.time()-T0:.0f} s")
    R = ratios(S)
    sel = [i for i, (m, zc) in enumerate(GROUPS) if sum(x * x for x in m) <= 3]
    Ssel = S[:, :, sel].sum(2); Psel = SUMP[sel].sum()
    cser = Psel / (2 * Ssel.mean(1)); c_all = Psel / (2 * Ssel.mean()); ce = np.std(cser, ddof=1) / np.sqrt(ns)
    check("the sampler reproduces the note's offset: c from the 24 smallest wavevectors = 0.33450 +- 0.00010 (note) within 5 combined standard errors",
          abs(c_all - 0.33450) < 5 * math.hypot(ce, 0.00010), f"c = {c_all:.5f} +- {ce:.5f} from {ns} seeds of {nb*BASE} loops")
    B0 = 100
    k = nb // B0
    Rb = R[:, :k * B0, :].reshape(ns, k, B0, G).mean(2).reshape(ns * k, G)           # bins of 25000 loops (the note's bin length)
    cons = contrasts()
    gsize = np.bincount(GV, minlength=G)
    def cvals(Rbins):
        return np.stack([Rbins[..., a] - Rbins[..., b] for (m, a, b) in cons], axis=-1)   # lowP minus highP
    C = cvals(Rb)                                                                          # (nbins, ncons)
    mean = C.mean(0); se = C.std(0, ddof=1) / np.sqrt(len(C)); z = mean / se
    order = np.argsort(-np.abs(z))
    print(f"\n== 1. all {len(cons)} contrasts (pooled over {ns*nb*BASE/1e6:g}M loops; the note's five are marked *) ==")
    print("   multiset   groups(zfold lo,hi)   P(lo),P(hi)     difference     se       z")
    for j in order[:12]:
        m, a, b = cons[j]
        star = "*" if m in NOTE5 and a == min(i for i, (mm, zc) in enumerate(GROUPS) if mm == m and SUMP[i] / gsize[i] > 0.05 and SUMP[i] / gsize[i] == min(SUMP[i2] / gsize[i2] for i2, (mm2, _) in enumerate(GROUPS) if mm2 == m)) else " "
        print(f"   {str(m):9s}  ({GROUPS[a][1]},{GROUPS[b][1]})            {SUMP[a]/gsize[a]:.3f},{SUMP[b]/gsize[b]:.3f}   {100*mean[j]:+8.4f}%  {100*se[j]:.4f}%  {z[j]:+6.2f}")
    zmax = float(np.abs(z).max())
    rng = np.random.default_rng(90085)
    Cc = C - mean
    nboot = 4000
    zm = np.empty(nboot)
    # centred bootstrap within seeds: resample bins with replacement, recompute standardised means, keep the maximum |z|
    seed_idx = np.repeat(np.arange(ns), k)
    Cs = Cc.reshape(ns, k, -1)
    for t in range(nboot):
        pick = rng.integers(k, size=(ns, k))
        Bt = np.take_along_axis(Cs, pick[:, :, None], axis=1).reshape(ns * k, -1)
        zm[t] = np.abs(Bt.mean(0) / (Bt.std(0, ddof=1) / np.sqrt(len(Bt)))).max()
    pmax = float((zm >= zmax).mean())
    print(f"   largest |z| over the {len(cons)} contrasts = {zmax:.2f}; under the centred bootstrap null the maximum of {len(cons)} standardised means exceeds it with probability {pmax:.3f} (median max {np.median(zm):.2f})")
    note5 = [j for j, (m, a, b) in enumerate(cons) if m in NOTE5]
    big = [(cons[j][0], mean[j]) for j in range(len(cons)) if abs(mean[j]) - 3 * se[j] > 0.0020]
    print(f"   contrasts with |difference| more than 3 se above 0.2%: {len(big)}")
    for m, x in big:
        HITS.append(f"the fresh-seed pooled difference of {m} is {100*x:+.3f}% with se beyond 3-sigma above 0.2%")

    # ---- 2. optimal linear detector of a z-axis distortion, over all contrasts at once
    print("\n== 2. fitted z-axis distortion S = P(1 + eps h)/K over all contrasts ==")
    Qg = np.array([sum(s2[a] for a in GROUPS[i][0]) for i in range(G)])
    s2z = np.array([s2[GROUPS[i][1]] for i in range(G)])
    hs = {"h = s_z^2": s2z, "h = s_z^4/Q": s2z ** 2 / Qg}
    results = {}
    for nm, h in hs.items():
        x = np.array([h[a] - h[b] for (m, a, b) in cons])
        # weighted least squares through the origin on the contrast means (weights 1/se^2); bootstrap for the error
        def fit(Cm, sem):
            w = 1 / sem ** 2
            return float((w * x * Cm).sum() / (w * x * x).sum())
        e0 = fit(mean, se)
        eb = np.empty(1000)
        for t in range(1000):
            pick = rng.integers(k, size=(ns, k))
            Bt = np.take_along_axis(C.reshape(ns, k, -1), pick[:, :, None], axis=1).reshape(ns * k, -1)
            eb[t] = fit(Bt.mean(0), Bt.std(0, ddof=1) / np.sqrt(len(Bt)))
        ee = float(eb.std(ddof=1))
        # implied differences in the note's five rows
        imp = {}
        for j in note5:
            imp[cons[j][0]] = imp.get(cons[j][0], 0) + 0
        rowsz = []
        for m in NOTE5:
            us = [i for i, (mm, zc) in enumerate(GROUPS) if mm == m]
            lo = min(us, key=lambda i: SUMP[i] / gsize[i]); hi = max(us, key=lambda i: SUMP[i] / gsize[i])
            rowsz.append(e0 * (h[lo] - h[hi]))
        results[nm] = (e0, ee)
        print(f"   {nm:14s}: eps = {e0:+.5f} +- {ee:.5f}  (z = {e0/ee:+.1f}); implied note-row differences " + " ".join(f"{100*x_:+.3f}%" for x_ in rowsz))
        if max(abs(v) for v in rowsz) - 3 * ee * np.abs(np.array([h[min(i for i, (mm, zc) in enumerate(GROUPS) if mm == m)] for m in NOTE5])).max() > 0.0020:
            HITS.append(f"the fitted distortion {nm} implies a note-row difference above 0.2%")
    print()
    for h_ in HITS: print("HIT:", h_)
    print(f"time {time.time()-T0:.0f} s")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    e1 = results["h = s_z^2"]
    print(f"SUMMARY: attack-e sampled evidence on PR 9008: adversarial search over {len(cons)} contrasts (all multisets |k|^2<=18, all usable assignment pairs) on 8 fresh seeds x {NLOOP/1e6:.1f}M loops: largest |z| = {zmax:.2f} (bootstrap-null probability of a maximum this large {pmax:.3f}); "
          f"optimal z-axis-distortion detector eps = {e1[0]:+.5f} +- {e1[1]:.5f} (z = {e1[0]/e1[1]:+.1f}); "
          + ("HIT recorded; " if HITS else "no contrast beyond the note's 0.2%; ") + f"PASS={PASS} FAIL={FAIL}")
    sys.exit(1 if FAIL else 0)
