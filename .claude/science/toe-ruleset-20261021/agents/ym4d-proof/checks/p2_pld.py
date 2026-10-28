"""p2 (lane E session 2): linear block-map identities and arithmetic used by PLD.md section 14.
Criteria: checks/p2_criteria.md (written first). Abelian linear model and arithmetic only."""
import itertools, math, sys, time
import numpy as np

t0 = time.time()
L = 3
d = 4
PAIRS = [(m, n) for m in range(d) for n in range(m + 1, d)]
res = {}

def m_w(t):
    return min(t + 1, 2 * L - 1 - t)

def build(T):
    n = L * T
    sites = np.array(list(itertools.product(range(n), repeat=d)))
    def sidx(x):
        x = np.mod(x, n)
        return ((x[..., 0] * n + x[..., 1]) * n + x[..., 2]) * n + x[..., 3]
    ns = n ** d
    rows, cols, vals = [], [], []
    pl = 0
    for (mu, nu) in PAIRS:
        emu = np.eye(d, dtype=int)[mu]; enu = np.eye(d, dtype=int)[nu]
        base = sites
        r = np.arange(ns) + pl * ns
        for (shift, dirn, sgn) in [(0 * emu, mu, 1), (emu, nu, 1), (enu, mu, -1), (0 * emu, nu, -1)]:
            rows.append(r); cols.append(sidx(base + shift) * d + dirn); vals.append(np.full(ns, sgn, float))
        pl += 1
    rows = np.concatenate(rows); cols = np.concatenate(cols); vals = np.concatenate(vals)
    return n, sites, sidx, rows, cols, vals

def apply_d(rows, cols, vals, A, nrows):
    out = np.zeros(nrows)
    np.add.at(out, rows, vals * A[cols])
    return out

def apply_dT(rows, cols, vals, F, ncols):
    out = np.zeros(ncols)
    np.add.at(out, cols, vals * F[rows])
    return out

lines = []
def say(s):
    lines.append(s); print(s, flush=True)

# ---------------- A and B ----------------
okA = True; okB = True
for T in (2, 3):
    n, sites, sidx, rows, cols, vals = build(T)
    ns = n ** d; nl = ns * d; npl = ns * len(PAIRS)
    # weights for the coarse plaquette at X = 0, (mu, nu) = (0, 1)
    def weight_vec(mu, nu, X):
        pidx = PAIRS.index((mu, nu))
        w = np.zeros(npl)
        perp = [a for a in range(d) if a not in (mu, nu)]
        for zm in range(2 * L - 1):
            for zn in range(2 * L - 1):
                for zp in itertools.product(range(L), repeat=2):
                    z = np.zeros(d, dtype=int)
                    z[mu] = zm; z[nu] = zn; z[perp[0]] = zp[0]; z[perp[1]] = zp[1]
                    z = z + L * np.array(X)
                    w[pidx * ns + sidx(z)] += L ** -4 * m_w(zm) * m_w(zn)
        return w
    # A: identity on random fields
    maxrel = 0.0
    for seed in range(3):
        rng = np.random.default_rng(100 + seed)
        A = rng.standard_normal(nl)
        F = apply_d(rows, cols, vals, A, npl)
        for (mu, nu) in PAIRS:
            for X in [(0, 0, 0, 0), (1, 0, 1, 0)] if T == 2 else [(0, 0, 0, 0), (2, 1, 0, 1)]:
                X = np.array(X)
                def Qstr(Xc, a):
                    s = 0.0
                    for y in itertools.product(range(L), repeat=d):
                        y = np.array(y) + L * Xc
                        for j in range(L):
                            s += A[sidx(y + j * np.eye(d, dtype=int)[a]) * d + a]
                    return s / L ** 4
                emu = np.eye(d, dtype=int)[mu]; enu = np.eye(d, dtype=int)[nu]
                lhs = Qstr(X, mu) + Qstr(X + emu, nu) - Qstr(X + enu, mu) - Qstr(X, nu)
                w = weight_vec(mu, nu, X)
                rhs = w @ F
                maxrel = max(maxrel, abs(lhs - rhs) / max(1.0, abs(lhs)))
    w = weight_vec(0, 1, (0, 0, 0, 0))
    sw, sw2 = w.sum(), (w ** 2).sum()
    passA = maxrel <= 1e-12 and abs(sw - L ** 2) <= 1e-12 and abs(sw2 - 361 / 729) <= 1e-14
    okA &= passA
    say(f"A T={T}: max rel |dQ_str A - <w,dA>| = {maxrel:.2e}; sum w = {sw:.15f}; sum w^2 = {sw2:.15f} "
        f"(361/729 = {361/729:.15f}) -> {'PASS' if passA else 'FAIL'}")
    # B: projection onto im d via CG on d^T d x = d^T w
    b = apply_dT(rows, cols, vals, w, nl)
    x = np.zeros(nl); r = b.copy(); p = r.copy(); rr = r @ r; bn = math.sqrt(rr)
    it = 0
    while math.sqrt(rr) > 1e-13 * bn and it < 20000:
        Ap = apply_dT(rows, cols, vals, apply_d(rows, cols, vals, p, npl), nl)
        al = rr / (p @ Ap); x += al * p; r -= al * Ap
        rr2 = r @ r; p = r + (rr2 / rr) * p; rr = rr2; it += 1
    Pw = apply_d(rows, cols, vals, x, npl)
    resid = np.linalg.norm(apply_dT(rows, cols, vals, w - Pw, nl)) / np.linalg.norm(w)
    nPw = Pw @ Pw
    passB = nPw <= 361 / 729 + 1e-9 and resid <= 1e-8
    okB &= passB
    say(f"B T={T}: ||Pi w||^2 = {nPw:.6f} (<= ||w||^2 = {sw2:.6f}); ratio = {nPw/sw2:.4f}; "
        f"1/||Pi w||^2 = {1/nPw:.4f}; CG its {it}, resid {resid:.1e} -> {'PASS' if passB else 'FAIL'}")
res['A'] = okA; res['B'] = okB

# ---------------- C ----------------
lL = math.log(L)
bm, bp = 0.3, 0.45
okC = True
rng = np.random.default_rng(7)
for gk2 in (0.05, 0.2):
    for kind in ('bm', 'bp', 'rand'):
        for k in (10, 100, 1000, 10000, 100000):
            if kind == 'bm': inc = np.full(k, bm * lL)
            elif kind == 'bp': inc = np.full(k, bp * lL)
            else: inc = rng.uniform(bm, bp, k) * lL
            # inv[n] = 1/g_{k-n}^2, n = 0..k
            inv = 1 / gk2 + np.concatenate([[0.0], np.cumsum(inc)])
            gj2 = 1 / inv[1:]           # levels j = k-1 ... 0 (n = 1..k)
            g02 = 1 / inv[k]
            S4 = (gj2 ** 2).sum()
            c4 = S4 <= gk2 / (bm * lL) + gk2 ** 2
            okC &= c4
            for th in (0.5, 1.0, 1.5):
                c = th * bm * lL
                logP = np.log1p(c * gj2).sum()
                bound = th * math.log(gk2 / g02)
                R = math.exp(logP) * g02 / gk2
                c1 = logP <= bound + 1e-12
                c2 = True if th > 1 else (R <= 1 + 1e-12)
                okC &= c1 and c2
                res[('R', gk2, kind, k, th)] = R
    for kind in ('bm',):
        Rs = [res[('R', gk2, kind, k, 1.5)] for k in (10, 100, 1000, 10000, 100000)]
        incr = all(Rs[i + 1] > Rs[i] for i in range(4))
        pred = ((1 + bm * 1e5 * lL * gk2) / (1 + bm * 1e4 * lL * gk2)) ** 0.5
        meas = Rs[4] / Rs[3]
        c3 = incr and abs(meas / pred - 1) <= 0.2
        okC &= c3
        say(f"C g_k^2={gk2}: theta=1.5, b=beta_-: R_k = " + ", ".join(f"{r:.4g}" for r in Rs)
            + f"; R(1e5)/R(1e4) = {meas:.4f} vs predicted {pred:.4f} -> {'ok' if c3 else 'BAD'}")
    for th in (0.5, 1.0):
        Rs = [res[('R', gk2, 'bm', k, th)] for k in (10, 100, 1000, 10000, 100000)]
        say(f"C g_k^2={gk2}: theta={th}, b=beta_-: R_k = " + ", ".join(f"{r:.4g}" for r in Rs))
say(f"C overall (C1 upper bound, C2 theta<=1 uniform, C3 growth rate, C4 sum g^4): {'PASS' if okC else 'FAIL'}")
res['C'] = okC

# ---------------- D ----------------
b1 = lambda N: 11 * N ** 2 / (12 * math.pi ** 2)
eps1 = 0.5
nst = {N: math.floor(4 / ((0.9 * eps1 ** 2 / (4 * N)) * b1(N))) for N in (2, 3)}
thr = math.log(24 * L ** 4) / lL
Nmin = next(N for N in range(2, 1000) if (2 / N) * 4 * b1(N) > thr)
okD = nst[2] == 382 and nst[3] == 255
say(f"D beta_1(2) = {b1(2):.6f}, beta_1(3) = {b1(3):.6f}; n_* = {nst[2]} (SU(2)), {nst[3]} (SU(3)); "
    f"log(24 L^4)/log L = {thr:.4f}; smallest N with (2/N)*4*beta_1 > that: {Nmin} -> {'PASS' if okD else 'FAIL'}")
res['D'] = okD

# ---------------- E ----------------
okE = True
M = 10 ** 6
tt = (np.arange(M) + 0.5) * (2.0 / M)
for (a, C, p) in [(0.1, 1.0, 0), (1 / (4 * 117 ** 2), 10.0, 8), (0.25, 1e3, 3)]:
    for g in (0.05, 0.1, 0.3):
        for e1 in (0.5, 2.0):
            B = C * g ** -p
            prof = np.where(tt <= e1, np.minimum(1, B * np.exp(-a * tt ** 2 / g ** 2)),
                            min(1.0, B * math.exp(-a * e1 ** 2 / g ** 2)))
            num = (2 * tt * prof).sum() * (2.0 / M)
            closed = (g ** 2 / a) * (1 + max(0.0, math.log(B))) + 4 * B * math.exp(-a * e1 ** 2 / g ** 2)
            ok = closed >= num * (1 - 1e-9)
            okE &= ok
            if not ok:
                say(f"E FAIL a={a} C={C} p={p} g={g} eps1={e1}: num {num} closed {closed}")
say(f"E (18 cases): closed form >= numerical E X^2 in all -> {'PASS' if okE else 'FAIL'}")
res['E'] = okE

say(f"SUMMARY A={res['A']} B={res['B']} C={res['C']} D={res['D']} E={res['E']}; wall {time.time()-t0:.1f}s")
