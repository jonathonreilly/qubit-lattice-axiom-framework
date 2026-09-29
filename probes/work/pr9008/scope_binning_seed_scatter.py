"""PR 9008 attack-d: QUANTIFIER SCOPE of 'binned errors are descriptive / seed sets scatter more than the binned errors allow / the transverse form holds within about 0.2%'.

The note tests the transverse angular form of uniform ice's covariance on L = 16 with 4 seeds (runner), 4 control seeds and 2 seeds of PR 8968, and reads the control's 3.0-sigma
excursion as evidence that 'the binned errors understate the spread'.  Here: 8 FRESH seeds x 1.5M loops (12M loops, three times the note's 4M) with own directed-loop sampler
(numba), the note's estimator (E_z only, ratio r_g = K_cont sum S / sum P per (multiset, z-fold) group, difference smallest-P minus largest-P for the five multisets), and
  1. a binning analysis of the differences' standard errors as a function of bin length, against the note's 25000-loop bins;
  2. the seed-to-seed scatter of the differences against the within-seed binned errors (chi2, Fisher over the five multisets);
  3. the note's 0.25% seed-set bound on 8 fresh seeds (two sets of four).
Batch means of 250 loops are stored per group; the script reuses PR9008_ATTACK_CACHE when set (the sibling attack-e script uses the same data).
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
# attack-d  QUANTIFIER SCOPE: 'binned errors are descriptive', 'the seed sets scatter more than the binned errors allow',
# 'the transverse form holds within about 0.2%'  ->  a binning analysis and a seed-scatter test on 8 fresh seeds
# =====================================================================================================================
def chi2_sf(x, k):
    # regularised upper incomplete gamma via series/continued fraction (no scipy needed)
    from math import lgamma, exp, log
    a = k / 2.0; xx = x / 2.0
    if xx <= 0: return 1.0
    if xx < a + 1:
        s = 1.0 / a; term = s; n = a
        for _ in range(2000):
            n += 1; term *= xx / n; s += term
            if term < s * 1e-16: break
        return 1 - s * exp(-xx + a * log(xx) - lgamma(a))
    b = xx + 1 - a; c = 1e300; d = 1 / b; h = d
    for i in range(1, 2000):
        an = -i * (i - a); b += 2; d = an * d + b; d = 1 / d if abs(d) > 1e-300 else 1e300
        c = b + an / c if abs(c) > 1e-300 else 1e300; dl = d * c; h *= dl
        if abs(dl - 1) < 1e-16: break
    return exp(-xx + a * log(xx) - lgamma(a)) * h

if __name__ == "__main__":
    T0 = time.time()
    HITS = []
    S, steps = data()
    ns, nb, _ = S.shape
    print(f"data: {ns} seeds x {nb * BASE} loops (batch means of {BASE} loops), mean worm length {steps:.0f} steps, {G} wavevector groups; {time.time()-T0:.0f} s")
    R = ratios(S)                       # (ns, nb, G)
    # ---- sampler fidelity: the 24 smallest wavevectors imply the note's stiffness
    sel = [i for i, (m, zc) in enumerate(GROUPS) if sum(x * x for x in m) <= 3]
    Ssel = S[:, :, sel].sum(2); Psel = SUMP[sel].sum()
    c_b = Psel / (2 * Ssel)             # per batch c = sum P / (2 sum S)
    cser = Psel / (2 * Ssel.mean(1))    # per seed
    c_all = Psel / (2 * Ssel.mean()); ce = np.std(cser, ddof=1) / np.sqrt(ns)
    check("the sampler reproduces the note's offset: c from the 24 smallest wavevectors = 0.33450 +- 0.00010 (note) within 5 combined standard errors",
          abs(c_all - 0.33450) < 5 * math.hypot(ce, 0.00010), f"c = {c_all:.5f} +- {ce:.5f} from {ns} seeds of {nb*BASE} loops")

    lo_hi = {}
    for (m, a, b) in contrasts():
        if m in NOTE5:
            us = [i for i, (mm, zc) in enumerate(GROUPS) if mm == m]
            pm = {i: SUMP[i] / (gid.ravel() == i).sum() for i in us}
            lo = min(us, key=pm.get); hi = max(us, key=pm.get)
            lo_hi[m] = (lo, hi)
    D = np.stack([R[:, :, lo] - R[:, :, hi] for m, (lo, hi) in lo_hi.items()], axis=2)   # (ns, nb, 5)
    print("multisets:", list(lo_hi))

    # ---- 1. binning analysis: standard error of the pooled mean vs bin length
    print("\n== 1. standard error of the pooled difference vs bin length (loops per bin) ==")
    print("   loops/bin   " + "   ".join(f"{str(m):>10s}" for m in lo_hi) + "   mean-of-5")
    ses = {}
    Dm = np.concatenate([D, D.mean(2, keepdims=True)], axis=2)
    BL = [B for B in (1, 4, 20, 100, 400, 1000, 2000) if nb // B >= 2]
    for B in BL:
        k = nb // B
        Bm = Dm[:, :k * B, :].reshape(ns, k, B, -1).mean(2).reshape(ns * k, -1)
        se = Bm.std(axis=0, ddof=1) / np.sqrt(ns * k)
        ses[B] = se
        print(f"   {B * BASE:>9d}   " + "   ".join(f"{100 * x:10.4f}" for x in se) + "   (percent)")
    B0 = 100   # the note's 25000-loop bins
    BBIG = BL[-1]
    infl = ses[BBIG] / ses[B0]
    print("   inflation of the plateau (longest bins) over the note's 25000-loop bin errors:", " ".join(f"{x:.2f}" for x in infl))
    print("   ratio of the two longest bin lengths' errors:", " ".join(f"{x:.2f}" for x in ses[BL[-2]] / ses[BL[-1]]))

    # ---- 2. seed-to-seed scatter against the binned within-seed errors (the note's item 3 reading)
    print("\n== 2. seed scatter vs binned errors, per multiset (8 seeds; within-seed error from 60 bins of 25000 loops) ==")
    k = nb // B0
    Bs = Dm[:, :k * B0, :].reshape(ns, k, B0, -1).mean(2)              # (ns, k, 6)
    seed_mean = Bs.mean(1); seed_se = Bs.std(1, ddof=1) / np.sqrt(k)
    pooled = seed_mean.mean(0)
    names = [str(m) for m in lo_hi] + ["mean-of-5"]
    ps = []
    for j, nm in enumerate(names):
        chi = float((((seed_mean[:, j] - pooled[j]) / seed_se[:, j]) ** 2).sum())
        p = chi2_sf(chi, ns - 1); ps.append(p)
        sdev = seed_mean[:, j].std(ddof=1)
        print(f"   {nm:>10s}: pooled {100*pooled[j]:+.4f}% +- {100*ses[B0][j]:.4f}% (binned) ; seed means {100*seed_mean[:, j].min():+.3f}..{100*seed_mean[:, j].max():+.3f}% ; "
              f"chi2 = {chi:5.1f} / {ns-1} dof, p = {p:.3f} ; scatter/binned-se ratio {sdev/np.mean(seed_se[:, j]):.2f}")
    fisher = -2 * sum(math.log(max(p, 1e-300)) for p in ps[:5])
    pf = chi2_sf(fisher, 10)
    print(f"   Fisher combination over the five multisets: chi2 = {fisher:.1f} / 10 dof, p = {pf:.3f}")
    print("   pooled differences (percent):", " ".join(f"{100*x:+.3f}" for x in pooled[:5]), " ; note's claim: all within about 0.2%")
    for j, m in enumerate(lo_hi):
        if abs(pooled[j]) - 3 * ses[B0][j] > 0.0020:
            HITS.append(f"pooled difference of {m} is {100*pooled[j]:+.3f}% +- {100*ses[B0][j]:.3f}% (binned): beyond the note's 'within about 0.2%' by more than 3 standard errors on 12M fresh loops")
    # seed SETS of four (the note's runner used four seeds; the control four more)
    for a, b in ((0, 4), (4, 8)):
        sm = Dm[a:b].mean((0, 1))
        print(f"   seeds {a}-{b-1} pooled (12 M loops/4 => {NLOOP*4/1e6:.0f}M loops): " + " ".join(f"{100*x:+.3f}%" for x in sm))
    mx = np.abs(np.stack([Dm[a:b].mean((0, 1)) for a, b in ((0, 4), (4, 8))])[:, :5]).max()
    print(f"   largest four-seed-set difference {100*mx:.3f}% (note: no seed set exceeds 0.25% in any multiset)")
    scatter_ok = pf > 0.05
    verdict = ("the between-seed scatter is CONSISTENT with the 25000-loop binned errors (Fisher p = %.3f): this measurement does not support the note's suggestion that binned errors understate the spread; "
               "the 3.0-sigma control seed reads as chance" % pf) if scatter_ok else \
              ("the between-seed scatter EXCEEDS the binned errors (Fisher p = %.3f): the note's suggestion that binned errors understate the spread is supported" % pf)
    print("\n" + verdict)
    tau = (ses[BBIG] / ses[1]) ** 2 * 0.5   # integrated autocorrelation time in units of BASE-loop bins (rough)
    print(f"   integrated autocorrelation time of the differences ~ {' '.join(f'{x*BASE:.0f}' for x in tau)} loops (from the plateau/base error ratio; the base bin is {BASE} loops)")
    print()
    for h in HITS: print("HIT:", h)
    print(f"time {time.time()-T0:.0f} s")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(f"SUMMARY: attack-d quantifier scope on PR 9008: 8 fresh seeds x {NLOOP/1e6:.1f}M loops (12M total, note 4M); sampler reproduces c={c_all:.5f}+-{ce:.5f}; pooled five differences "
          + " ".join(f"{100*x:+.3f}%" for x in pooled[:5]) + f" (mean {100*pooled[5]:+.3f}% +- {100*ses[B0][5]:.3f}%); binning plateau/note-error {np.min(infl):.2f}..{np.max(infl):.2f}; seed-scatter Fisher p={pf:.3f}; "
          + ("scatter consistent with binned errors; " if scatter_ok else "scatter exceeds binned errors; ") + f"largest four-seed-set |difference| {100*mx:.3f}%; PASS={PASS} FAIL={FAIL}; " + ("HIT recorded" if HITS else "no HIT"))
    sys.exit(1 if FAIL else 0)
