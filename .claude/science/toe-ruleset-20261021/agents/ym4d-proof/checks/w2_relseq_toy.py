"""w2 (lane H, session 2): capped inequalities, Lemma REL-seq on an exact toy, loop arithmetic, (g3) count.
Criteria: checks/w2_criteria.md (written before this script). Informational, not a proof."""
import math, itertools, time
import numpy as np

t0 = time.time()
out = []
P = out.append
res = {}

# ---------------- A. capped inequalities ----------------
rng = np.random.default_rng(20261028)
n = 10**6
a = 10.0 ** rng.uniform(-6, 6, n); b = 10.0 ** rng.uniform(-6, 6, n); pi = 10.0 ** rng.uniform(-6, 6, n)
lhs = np.minimum(pi, a + b); rhs = a + np.minimum(pi, b)
v1 = int(np.sum(lhs > rhs * (1 + 1e-12)))
res['A1'] = v1 == 0; P(f"A1 min(pi,a+b) <= a+min(pi,b): violations {v1}/{n}  {'PASS' if res['A1'] else 'FAIL'}")
X = 10.0 ** rng.uniform(-6, 6, n); th = 10.0 ** rng.uniform(-3, 1, n)
ind = (X >= pi).astype(float)
with np.errstate(over='ignore', under='ignore'):
    r2 = np.exp(th * (np.minimum(X, pi) - pi))
v2 = int(np.sum(ind > r2 * (1 + 1e-12)))
res['A2'] = v2 == 0; P(f"A2 1{{X>=pi}} <= exp(th(min(X,pi)-pi)): violations {v2}/{n}  {'PASS' if res['A2'] else 'FAIL'}")
false = np.minimum(pi / 2, a) + np.minimum(pi / 2, b)
v3 = int(np.sum(lhs > false * (1 + 1e-12)))
res['A3'] = v3 > 0; P(f"A3 (neg. control) false split violated on {v3} samples  {'FAILS as required' if res['A3'] else 'DID NOT FAIL'}")

# ---------------- B. REL-seq toy ----------------
W_, H_ = 4, 4
NS = W_ * H_
sites = [(i, j) for i in range(H_) for j in range(W_)]
idx = {s: k for k, s in enumerate(sites)}
nbr = [0] * NS
for (i, j), k in idx.items():
    m = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if (di or dj) and (i + di, j + dj) in idx:
                m |= 1 << idx[(i + di, j + dj)]
    nbr[k] = m

def maxcomp(mask):
    best = 0
    rem = mask
    while rem:
        low = rem & -rem
        comp = low; frontier = low
        while frontier:
            f = frontier & -frontier; frontier ^= f
            k = f.bit_length() - 1
            new = nbr[k] & mask & ~comp
            comp |= new; frontier |= new
        rem &= ~comp
        c = bin(comp).count('1')
        if c > best: best = c
    return best

def comp_of(mask, k):
    comp = 1 << k; frontier = comp
    while frontier:
        f = frontier & -frontier; frontier ^= f
        j = f.bit_length() - 1
        new = nbr[j] & mask & ~comp
        comp |= new; frontier |= new
    return comp

configs = np.arange(1 << NS, dtype=np.int64)
popc = np.array([bin(c).count('1') for c in range(1 << NS)], dtype=np.int64)
# number of *-adjacent defect pairs
pairs = [(k, l) for k in range(NS) for l in range(k + 1, NS) if nbr[k] >> l & 1]
npair = np.zeros(1 << NS, dtype=np.int64)
for k, l in pairs:
    npair += ((configs >> k) & 1) & ((configs >> l) & 1)

U = [idx[(0, 0)], idx[(0, 1)], idx[(1, 0)], idx[(1, 1)]]
N1U = [idx[(i, j)] for i in range(3) for j in range(3)]
ALL = (1 << NS) - 1
S0 = ALL
for k in N1U: S0 &= ~(1 << k)

def animals(x, size, allowed):
    """all *-connected subsets of `allowed` (bitmask) of given size containing x."""
    found = set()
    def grow(cur, front):
        if bin(cur).count('1') == size:
            found.add(cur); return
        cand = 0
        k = cur
        while k:
            f = k & -k; k ^= f
            cand |= nbr[f.bit_length() - 1]
        cand &= allowed & ~cur
        while cand:
            f = cand & -cand; cand ^= f
            if (cur | f) not in seen:
                seen.add(cur | f); grow(cur | f, f)
    seen = {1 << x}
    grow(1 << x, 1 << x)
    return found

laws = [('Bern', p, None) for p in (0.02, 0.05, 0.1, 0.2)] + [('Ising', J, h) for J, h in ((0.5, -3.0), (1.0, -4.0), (0.3, -2.5))]
TABLE = np.array([maxcomp(c) for c in range(1 << NS)], dtype=np.int64)  # max *-component size of every mask
mc_cache = {}
def mc_all(S):
    if S not in mc_cache:
        mc_cache[S] = TABLE[configs & S]
    return mc_cache[S]

okB1 = okB2 = okB3 = okDECL = True; negB4_failed = False; tight = []
nB3 = 0
for nsh in (1, 2):
    for order_name, order in (('fwd', N1U), ('rev', N1U[::-1])):
        Ss = [S0]
        for k in order: Ss.append(Ss[-1] | (1 << k))
        # B2 containment (law-independent)
        for i, k in enumerate(order):
            Si, Si1 = Ss[i], Ss[i + 1]
            mi, mi1 = mc_all(Si), mc_all(Si1)
            bad = np.nonzero((mi <= nsh) & (mi1 > nsh))[0]
            for c in bad[:: max(1, len(bad) // 2000)]:
                c = int(c)
                if not (c >> k & 1): okB2 = False; continue
                C = comp_of(c & Si1, k)
                if bin(C).count('1') <= nsh: okB2 = False; continue
                if not animals(k, nsh + 1, C): okB2 = False
        for (kind, q1, q2) in laws:
            if kind == 'Bern':
                w = (q1 ** popc) * ((1 - q1) ** (NS - popc))
            else:
                w = np.exp(q1 * npair + q2 * popc)
            Z = lambda S: float(np.sum(w[mc_all(S) <= nsh]))
            Zs = [Z(S) for S in Ss]
            prod = 1.0
            for i in range(len(order)):
                mask_i = mc_all(Ss[i]) <= nsh
                prod *= float(np.sum(w[mask_i & (mc_all(Ss[i + 1]) <= nsh)])) / Zs[i]
            ratio = Zs[-1] / Zs[0]
            if abs(prod / ratio - 1) > 1e-12: okB1 = False
            # B3 exact step prices
            psum = 0.0; pmaxsum = 0.0; pmax_step = 0.0
            for i, k in enumerate(order):
                Si = Ss[i]; mask_i = mc_all(Si) <= nsh; Zi = Zs[i]
                pi_ = 0.0; mx = 0.0
                for D in animals(k, nsh + 1, Ss[i + 1]):
                    inD = (configs & D) == D
                    pD = float(np.sum(w[mask_i & inD])) / Zi
                    pi_ += pD; mx = max(mx, pD)
                    # declared-set inequality (checked on the subset where it matters, vectorised via cache)
                    maskd = TABLE[(configs | D) & Si] <= nsh
                    Zd = float(np.sum(w[maskd]))
                    pd = float(np.sum(w[maskd & inD])) / Zd if Zd > 0 else 0.0
                    if pD > pd * (1 + 1e-12) + 1e-300: okDECL = False
                psum += pi_; pmaxsum += mx; pmax_step = max(pmax_step, pi_)
            lr = math.log(ratio)
            if pmax_step <= 0.5:
                nB3 += 1
                if lr < -2 * psum * (1 + 1e-12): okB3 = False
                if lr < -2 * pmaxsum: negB4_failed = True
                tight.append((lr / (-2 * psum)) if psum > 0 else float('nan'))
            P(f"B n#={nsh} {order_name} {kind}({q1},{q2}): log Z(all)/Z(S0)={lr:.4e}  -2*sum p={-2*psum:.4e}  -2*sum max={-2*pmaxsum:.4e}  max p_i={pmax_step:.3f}")
res['B1'] = okB1; res['B2'] = okB2; res['B3'] = okB3 and okDECL and nB3 > 0; res['B4'] = negB4_failed; res['B5'] = okB1 and okB3
P(f"B1 identity {'PASS' if okB1 else 'FAIL'}; B2 containment {'PASS' if okB2 else 'FAIL'}; B3 bound {'PASS' if okB3 else 'FAIL'} on {nB3} cases, DECL {'PASS' if okDECL else 'FAIL'}")
P(f"B3 tightness log-ratio/(-2 sum p): min {min(tight):.3f} max {max(tight):.3f}")
P(f"B4 (neg. control, animal count removed) {'FAILS as required' if negB4_failed else 'DID NOT FAIL'}; B5 both orders {'PASS' if res['B5'] else 'FAIL'}")

# ---------------- C. arithmetic ----------------
L = 3; lnL = math.log(L)
okC1 = True
for c in (0.1, 1.0):
    for aa in (1e-17, 1e-23):
        for bm in (0.19, 0.37):
            nH = math.floor((4 + 38416 * c / lnL) / (aa * bm))
            if not ((nH + 1) * aa * bm * lnL >= 38416 * c): okC1 = False
P(f"C1 depth term absorbed at n_H for all (c,a,beta-): {'PASS' if okC1 else 'FAIL'}  (e.g. c=1,a=1e-17,b=0.37: n_H={math.floor((4+38416/lnL)/(1e-17*0.37)):.3e})")
okC2 = True; lines = []
for th in (1/6, 1/100):
    for aa in (2.3e-16, 5e-23):
        for bp in (0.56, 1.0, 10.0):
            for R in (0.0, 1.0):
                G = 81 * L ** (-th * aa * bp) * math.exp(-th * aa * R)
                if not G > 1: okC2 = False
                lines.append(G)
P(f"C2 LOOP-const growth G: min {min(lines):.15f} max {max(lines):.15f}; G^100 >= {min(lines)**100:.3e}  {'PASS' if okC2 else 'FAIL'}")
okC3 = True; ms = []
for rho in (4, 24, 96):
    thK = 1 / (2 * rho)
    for g2 in (0.1, 0.01):
        uK = 1 / g2; m = 0
        while not (rho ** m * thK * uK / (uK + 1.0 * m * lnL + 1.0) > 1 / rho):
            m += 1
            if m > 1000: break
        ms.append((rho, g2, m))
        if m > 20: okC3 = False
P("C3 LOOP-div m_*: " + ", ".join(f"rho={r},g2={g}:{m}" for r, g, m in ms) + f"  {'PASS' if okC3 else 'FAIL'}")
c4 = []
for ab in (1e-16, 1.0, 4.5):
    for K in (10, 50):
        c4.append((ab, K, sum(L ** ((4 - ab) * m) for m in range(K))))
okC4 = c4[1][2] / c4[0][2] > 1e10 and c4[3][2] / c4[2][2] > 1e10 and c4[5][2] < 3
P("C4 GAS sums: " + ", ".join(f"ab={ab},K={K}:{s:.3e}" for ab, K, s in c4) + f"  {'PASS' if okC4 else 'FAIL'}")
res['C'] = okC1 and okC2 and okC3 and okC4

# ---------------- D. (g3) count in Z^4 ----------------
offs = [o for o in itertools.product((-1, 0, 1), repeat=4) if any(o)]
def adj(x, y): return max(abs(p - q) for p, q in zip(x, y)) == 1
cnt = {1: 1, 2: len(offs)}
cand = set()
for o in offs:
    for o2 in offs:
        z = tuple(p + q for p, q in zip(o, o2))
        if any(z): cand.add(z)
cand |= set(offs)
cl = sorted(cand); c3 = 0
for i in range(len(cl)):
    for j in range(i + 1, len(cl)):
        A, B = cl[i], cl[j]
        e = [adj((0,0,0,0), A), adj((0,0,0,0), B), adj(A, B)]
        if sum(e) >= 2: c3 += 1
cnt[3] = c3
okD = all(cnt[k] <= 6400 ** (k - 1) for k in cnt)
P(f"D (g3) counts n=1,2,3: {cnt[1]}, {cnt[2]}, {cnt[3]} vs 6400^(n-1) = 1, 6400, 40960000  {'PASS' if okD else 'FAIL'}")
res['D'] = okD

overall = res['A1'] and res['A2'] and res['A3'] and res['B1'] and res['B2'] and res['B3'] and res['B4'] and res['B5'] and res['C'] and res['D']
P(f"OVERALL: {'PASS' if overall else 'FAIL'}  (A3, B4 are controls that must fail)   wall {time.time()-t0:.1f}s")
print("\n".join(out))
