"""Independent replication of the PR 9008 draft: does uniform cubic ice keep the transverse angular form on L = 16?

Own directed-loop sampler (numba), own estimators.  Differences from the note's runner, on purpose:
  * arrows are stored and walked by my own code; the sampler is validated at L = 2 against the exact 9600-state enumeration with a chi-square over all 9600 states;
  * the covariance is measured for ALL THREE arrow components on every loop, so the angular test compares components of the same sample
    (S_ii(k)/P_ii(k) for the same k and different i), which cancels common-mode noise; the note used only E_z;
  * 7 seeds x 4.0e6 loops (28e6 loops; the note used 4e6) with 40 bins per seed.
Model: uniform 3-in/3-out arrows on the L^3 torus, S_ii(k) = |FFT_i(k)|^2 / N, P_ii = 1 - s_i^2/Q, K_cont = (2N+1)/(3N), c = K_cont/(2 r).
"""
import os, sys, time, math
import numpy as np
from numba import njit
from multiprocessing import Pool

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)

@njit(cache=False)
def seed_nb(s):
    np.random.seed(s)

@njit(cache=False)
def one_loop(E, L):
    """reverse one directed cycle: start at a random site, keep leaving by a random outgoing arrow except the one just reversed."""
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

@njit(cache=False)
def defects(E, L):
    bad = 0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                d = (E[0, x, y, z] - E[0, (x - 1) % L, y, z] + E[1, x, y, z] - E[1, x, (y - 1) % L, z] + E[2, x, y, z] - E[2, x, y, (z - 1) % L])
                if d != 0: bad += 1
    return bad

def start_config(L):
    """a zero-winding ice state: E_x alternates along y, E_y along z, E_z along x."""
    E = np.empty((3, L, L, L), np.int8); alt = (-1) ** np.arange(L)
    E[0] = alt[None, :, None]; E[1] = alt[None, None, :]; E[2] = alt[:, None, None]
    return E

@njit(cache=False)
def l2_histogram(E, nsamples, stride, counts):
    for t in range(nsamples):
        for s_ in range(stride): one_loop(E, 2)
        code = 0
        b = 0
        for i in range(3):
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        if E[i, x, y, z] == 1: code |= (1 << b)
                        b += 1
        counts[code] += 1

def worker(args):
    L, nloops, nbins, sd = args
    seed_nb(sd)
    E = start_config(L)
    steps = 0
    for _ in range(max(nloops // 20, 100)): steps += one_loop(E, L)
    N = L ** 3
    per = nloops // nbins
    Sb = np.zeros((nbins, 3, L, L, L)); W2 = np.zeros(nbins); tot_steps = 0
    for b in range(nbins):
        for t in range(per):
            tot_steps += one_loop(E, L)
            F = np.fft.fftn(E.astype(np.float64), axes=(1, 2, 3))
            Sb[b] += (F.real ** 2 + F.imag ** 2) / N
        Sb[b] /= per
    assert defects(E, L) == 0
    return Sb, tot_steps / (nbins * per)

if __name__ == "__main__":
    T0 = time.time()
    # ---- exact L = 2 census, own enumeration -----------------------------------------------------------------
    def lid2(i, x, y, z): return i * 8 + (x % 2) * 4 + (y % 2) * 2 + (z % 2)
    sites = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
    outs = [[lid2(0, x, y, z), lid2(1, x, y, z), lid2(2, x, y, z)] for (x, y, z) in sites]
    ins = [[lid2(0, x - 1, y, z), lid2(1, x, y - 1, z), lid2(2, x, y, z - 1)] for (x, y, z) in sites]
    planes = [[lid2(0, 0, y, z) for y in range(2) for z in range(2)], [lid2(1, x, 0, z) for x in range(2) for z in range(2)], [lid2(2, x, y, 0) for x in range(2) for y in range(2)]]
    codes = []; sect = {}; w2sum = 0
    for chunk in range(16):
        idx = np.arange(chunk << 20, (chunk + 1) << 20, dtype=np.int64)
        bits = (((idx[:, None] >> np.arange(24)) & 1) * 2 - 1).astype(np.int8)
        ok = np.ones(len(idx), bool)
        for o, b in zip(outs, ins): ok &= bits[:, o].sum(1) == bits[:, b].sum(1)
        g = bits[ok]; codes.append(idx[ok])
        Ws = np.stack([g[:, p].sum(1) for p in planes], axis=1).astype(np.int64)
        w2sum += int((Ws ** 2).sum())
        for w in map(tuple, Ws): sect[w] = sect.get(w, 0) + 1
    codes = np.concatenate(codes)
    from fractions import Fraction
    W2 = Fraction(w2sum, 3 * len(codes))
    check("own enumeration of all 2^24 arrow patterns on L=2: 9600 ice states, 125 winding sectors, <W^2> = 76/25", len(codes) == 9600 and len(sect) == 125 and W2 == Fraction(76, 25), f"{len(codes)} states, {len(sect)} sectors, <W^2> = {W2}")
    # ---- sampler validation: uniform over all 9600 states ------------------------------------------------------
    seed_nb(31415); E2 = start_config(2)
    counts = np.zeros(1 << 24, np.int64)
    NL2 = 4_000_000; STRIDE = 10          # one sample per 10 loops: successive loops are correlated at L = 2 (chi2/dof 1.03-1.05 unthinned, 1.00 thinned)
    l2_histogram(E2, NL2, STRIDE, counts)
    c = counts[codes]
    check("the sampler visits only ice states and every one of the 9600", counts.sum() == NL2 and (c > 0).all() and c.sum() == NL2)
    from scipy.stats import chi2
    stat = ((c - NL2 / 9600.0) ** 2 / (NL2 / 9600.0)).sum(); pval = chi2.sf(stat, 9599)
    check("chi-square of the visit counts against the uniform law on the 9600 states has p > 0.001", pval > 1e-3, f"chi2/dof = {stat/9599:.4f} for 9599 dof, p = {pval:.3f} ({NL2} samples, one per {STRIDE} loops, mean {NL2/9600:.0f} per state)")
    print(f"   ({time.time()-T0:.0f}s so far)", flush=True)

    # ---- L = 16 sampling ---------------------------------------------------------------------------------------------
    L = 16; N = L ** 3
    NLOOPS = int(os.environ.get("PROBE_LOOPS", 4_000_000)); NSEED = int(os.environ.get("PROBE_SEEDS", 7)); NB = 40
    seeds = [7001 + 13 * s for s in range(NSEED)]
    with Pool(NSEED) as pool:
        res = pool.map(worker, [(L, NLOOPS, NB, s) for s in seeds])
    Sb = np.concatenate([r[0] for r in res])          # (batches, 3, L, L, L)
    nbatch = len(Sb); seed_of = np.repeat(np.arange(NSEED), NB)
    print(f"   sampling done in {time.time()-T0:.0f}s: {NSEED} seeds x {NLOOPS} loops, mean loop length {np.mean([r[1] for r in res]):.0f} steps", flush=True)
    check("every batch obeys the unit-arrow sum rule sum_k S_ii = N for each component", np.abs(Sb.reshape(nbatch, 3, -1).sum(2) - N).max() < 1e-8)

    k = 2 * np.pi * np.arange(L) / L; s2 = 2 - 2 * np.cos(k)
    Q = s2[:, None, None] + s2[None, :, None] + s2[None, None, :]
    Sg = [np.broadcast_to(s2[:, None, None], Q.shape), np.broadcast_to(s2[None, :, None], Q.shape), np.broadcast_to(s2[None, None, :], Q.shape)]
    Pm = np.zeros((3, L, L, L)); nz = Q > 0
    for i in range(3): Pm[i][nz] = 1 - Sg[i][nz] / Q[nz]
    KL = (2 * N + 1) / (3 * N)
    fold = np.minimum(np.arange(L), L - np.arange(L))
    FX, FY, FZ = np.meshgrid(fold, fold, fold, indexing='ij'); Fc = [FX, FY, FZ]; F2 = FX ** 2 + FY ** 2 + FZ ** 2

    def ratio(mask_by_comp):
        num = sum(Sb[:, i][:, mask_by_comp[i]].sum(1) for i in range(3)); den = sum(Pm[i][mask_by_comp[i]].sum() for i in range(3))
        return KL * num / den
    def ratio_z(mask):        # the note's estimator: E_z only
        return KL * Sb[:, 2][:, mask].sum(1) / Pm[2][mask].sum()
    def mean_err(x):
        return x.mean(), x.std(ddof=1) / math.sqrt(len(x))

    small = [(F2 <= 3) & (Pm[i] > 0.05) for i in range(3)]
    r_all = ratio(small); r_z = ratio_z(small[2])
    for name, r in (("all three components", r_all), ("E_z only (the note's estimator)", r_z)):
        rm, re = mean_err(r); c_, ce = KL / (2 * rm), KL / (2 * rm) * re / rm; cL = KL / 2
        print(f"   offset, {name}: c = {c_:.5f} +- {ce:.5f}, {(c_/cL-1)*100:+.3f}% above K_cont/2, {(c_-cL)/ce:.1f} binned s.e.")
    rm, re = mean_err(r_all); c_all, ce_all = KL / (2 * rm), KL / (2 * rm) * re / rm; cL = KL / 2
    # seed-to-seed consistency of the offset
    cs = [KL / (2 * r_all[seed_of == s].mean()) for s in range(NSEED)]
    print("   offset per seed:", [round(v, 5) for v in cs], "sd across seeds", round(float(np.std(cs, ddof=1)), 5))
    note_c = (0.33450, 0.00010); prior = [(0.33434, 0.00016), (0.33447, 0.00018)]
    check("offset: 0.1%..0.5% above K_cont/2 by more than 5 binned standard errors", 0.001 < c_all / cL - 1 < 0.005 and (c_all - cL) > 5 * ce_all, f"c = {c_all:.5f} +- {ce_all:.5f} ({(c_all/cL-1)*100:+.3f}%)")
    sd_seeds = float(np.std(cs, ddof=1)) / math.sqrt(NSEED)
    for lab, (v, e) in (("the note's four seeds", note_c), ("landed PR 8968 seed A", prior[0]), ("landed PR 8968 seed B", prior[1])):
        z = (c_all - v) / math.hypot(max(ce_all, sd_seeds), e)
        check(f"offset agrees with {lab} ({v} +- {e}) within 4 combined errors", abs(z) < 4, f"z = {z:+.2f}")

    # ---- angular form ---------------------------------------------------------------------------------------------
    multisets = [ms for ms in sorted({tuple(sorted((a, b, c3))) for a in range(4) for b in range(4) for c3 in range(4)}) if 0 < sum(x * x for x in ms) <= 9]
    rows = []
    for ms in multisets:
        groups = {}
        for zv in set(ms):
            rest = list(ms); rest.remove(zv)
            masks = []
            for i in range(3):
                others = [Fc[j] for j in range(3) if j != i]
                m = (Fc[i] == zv) & (np.minimum(others[0], others[1]) == min(rest)) & (np.maximum(others[0], others[1]) == max(rest)) & (Pm[i] > 0.05)
                masks.append(m)
            if sum(int(m.sum()) for m in masks) > 0:
                groups[zv] = (sum(Pm[i][masks[i]].sum() for i in range(3)) / sum(int(m.sum()) for m in masks), masks)
        if len(groups) >= 2:
            hi = max(groups, key=lambda z_: groups[z_][0]); lo = min(groups, key=lambda z_: groups[z_][0])
            rows.append((ms, groups[hi][0], groups[lo][0], ratio(groups[lo][1]) - ratio(groups[hi][1]), ratio_z(groups[lo][1][2]) - ratio_z(groups[hi][1][2])))
    check("five multisets with |k|^2 <= 9 have two usable assignments, with the note's P_zz values", [r[0] for r in rows] == [(0, 1, 1), (0, 1, 2), (0, 2, 2), (1, 1, 2), (1, 2, 2)] and all(abs(a - b) < 6e-4 for (a, b) in zip([r[1] for r in rows] + [r[2] for r in rows], [1.000, 1.000, 1.000, 0.829, 0.885, 0.500, 0.206, 0.500, 0.342, 0.558])), "; ".join(f"{r[0]} P {r[1]:.3f}/{r[2]:.3f}" for r in rows))
    print("   ratio difference (smallest-P assignment minus largest-P assignment), all components in-sample | E_z only:")
    diffs = []; diffsz = []
    for ms, phi, plo, d_all, d_z in rows:
        m1, e1 = mean_err(d_all); m2, e2 = mean_err(d_z)
        sd_seed = np.std([d_all[seed_of == s].mean() for s in range(NSEED)], ddof=1) / math.sqrt(NSEED)
        diffs.append((ms, m1, e1, sd_seed)); diffsz.append((ms, m2, e2))
        print(f"     {ms}: {m1:+.5f} +- {e1:.5f} (seed-to-seed s.e. {sd_seed:.5f}) | E_z only {m2:+.5f} +- {e2:.5f}")
    Dm = np.mean([r[3] for r in rows], axis=0); dm, de = mean_err(Dm)
    print(f"   mean over the five multisets: {dm:+.5f} +- {de:.5f}")
    check("no multiset's angular difference exceeds 0.25% (the note's bound: no seed set exceeds 0.25% in any multiset)", all(abs(d[1]) < 0.0025 for d in diffs), f"largest {max(abs(d[1]) for d in diffs):.5f}")
    check("no multiset is more than 3 standard errors above 0.2% in magnitude (the note's 'holds within about 0.2%')", all(abs(d[1]) - 3 * max(d[2], d[3]) < 0.002 for d in diffs))
    sig = [(d[0], d[1] / max(d[2], d[3])) for d in diffs if abs(d[1]) > 3 * max(d[2], d[3])]
    print("   multisets whose difference differs from zero by more than 3 s.e. (informational):", sig)
    print(f"   done in {time.time()-T0:.0f}s", flush=True)
    if FAIL == 0:
        print(f"SUMMARY: no falsifier fires: independent worm (chi-square p = {pval:.3f} against the exact L=2 uniform law) at L=16, {NSEED*NLOOPS} loops all three components: c = {c_all:.5f} +- {ce_all:.5f} ({(c_all/cL-1)*100:+.3f}% above K_cont/2); angular differences by multiset {[(d[0], round(d[1], 5)) for d in diffs]}, mean {dm:+.5f} +- {de:.5f}; {PASS} checks pass")
    else:
        print(f"SUMMARY: {FAIL} of my own checks failed; see the [FAIL] lines above")
    sys.exit(0)
