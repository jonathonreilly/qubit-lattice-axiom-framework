#!/usr/bin/env python3
"""Two bodies in the self-consistent odds field (blocks 41-42), measured.  Worked computation, run 1 of 2.

Six-axis rule, pair weight omega = (p, q, r) for equal / opposite / orthogonal contents; the full nonlinear map
pi_x(s) ~ prod over the six neighbours y of sum_b omega(s,b) pi_y(b), records held as point masses (block 42 T2).
Declared bookkeeping quantity (not an energy of the axioms): E = - sum over unformed sites of log(Z_x / Z_void),
Z_x = sum_s prod_y (omega pi_y)(s) the normalizer, Z_void = 6 (T/6)^6.  Interaction E_int = E(A+B) - E(A) - E(B).
Part X: exact (sympy) second-order identity for the normalizer (block 42 T4(b)) and the resulting pair form.
Parts N: floating point, torus of side L, Anderson-accelerated fixed-point iteration on log-odds (tolerance 1e-12).
Usage: run.py [L]   (default 41, the task's side).
"""
import sys, time, itertools
import numpy as np
import sympy as sp

L = int(sys.argv[1]) if len(sys.argv) > 1 else 41
SEPS = (6, 8, 10, 12, 14, 16)
SIDES = (1, 2, 3)
REL = (("equal", 0), ("opposite", 1), ("orthogonal", 2))

# ------------------------------------------------------------------ X: exact second-order identity (block 42 T4(b))
lam = sp.Symbol('lambda1')
E6 = [sp.Matrix(v) for v in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))]
eps = sp.Symbol('epsilon')
ms = [sp.Matrix(sp.symbols('m%d_1:4' % y)) for y in range(6)]
Zs = sum(sp.Mul(*[1 + 3 * lam * eps * (ms[y].T * E6[s])[0] for y in range(6)]) for s in range(6)) / 6
Zs = sp.expand(Zs)
first = Zs.coeff(eps, 1); second = Zs.coeff(eps, 2)
pair = 3 * lam ** 2 * sum((ms[y].T * ms[yy])[0] for y in range(6) for yy in range(y + 1, 6))
okx = sp.expand(Zs.coeff(eps, 0) - 1) == 0 and first == 0 and sp.expand(second - pair) == 0
print("X exact: (1/6) sum_s prod_y (1 + 3 l1 m_y.e(s)) = 1 + 3 l1^2 sum_{y<y'} m_y.m_y' + O(m^3), no first-order term: %s"
      % ("PASS" if okx else "FAIL"))
print("X hence for two sources m = m_A + m_B the cross term of log Z_x is 3 l1^2 [M_A.M_B - sum_y m_A(y).m_B(y)], M = sum over the six "
      "neighbours: E_int^(1) = -3 l1^2 sum_x [M_A.M_B - sum_y m_A(y).m_B(y)]  (the comparator below, from the single-body fields)")

# ------------------------------------------------------------------ numerics
def omega(p, q, r):
    return np.array([[p if a == b else q if a == (b ^ 1) else r for b in range(6)] for a in range(6)], float)
def nb_logs(pi, om):
    lp = np.zeros_like(pi)
    for d in range(3):
        for s in (1, -1):
            lp += np.log(np.roll(pi, s, axis=d) @ om.T)
    return lp
def phi_map(x, om, mask, recs):
    lp = nb_logs(np.exp(x), om)
    lp -= lp.max(axis=-1, keepdims=True)
    lp -= np.log(np.exp(lp).sum(axis=-1, keepdims=True))
    lp[mask] = recs[mask]
    return lp
def solve(om, mask, recs, x0, tol=1e-12, m=8, maxit=20000):
    x = x0.copy(); x[mask] = recs[mask]
    X, F = [], []
    for it in range(maxit):
        g = phi_map(x, om, mask, recs); f = g - x
        if np.abs(f).max() < tol:
            return g, it
        X.append(x.ravel().copy()); F.append(f.ravel().copy())
        if len(X) > m + 1:
            X.pop(0); F.pop(0)
        if len(X) >= 2:
            dF = np.array([F[i + 1] - F[i] for i in range(len(F) - 1)]).T
            dX = np.array([X[i + 1] - X[i] for i in range(len(X) - 1)]).T
            gam = np.linalg.lstsq(dF, f.ravel(), rcond=None)[0]
            x = (x.ravel() + f.ravel() - (dX + dF) @ gam).reshape(x.shape)
        else:
            x = g
        x[mask] = recs[mask]
    raise RuntimeError("no convergence")
def energy(x, om, mask):
    T = om[0].sum()
    lp = nb_logs(np.exp(x), om)
    mx = lp.max(axis=-1)
    logZ = mx + np.log(np.exp(lp - mx[..., None]).sum(axis=-1))
    logZv = np.log(6.0) + 6 * np.log(T / 6)
    return -float((logZ - logZv)[~mask].sum())
def lean(x):
    pi = np.exp(x)
    return np.stack([pi[..., 0] - pi[..., 1], pi[..., 2] - pi[..., 3], pi[..., 4] - pi[..., 5]], axis=-1)
def cube(x0, s):
    return [(x0 + i, c0 + j, c0 + k) for i in range(s) for j in range(s) for k in range(s)]
def setup(bodies):
    mask = np.zeros((L, L, L), bool); recs = np.full((L, L, L, 6), np.log(1 / 6.0))
    for sites, c in bodies:
        v = np.full(6, -80.0); v[c] = 0.0
        for st in sites:
            t = tuple(z % L for z in st); mask[t] = True; recs[t] = v
    return mask, recs
def green(m2):
    k = 2 * np.pi * np.arange(L) / L
    Ek = 6 - 2 * (np.cos(k)[:, None, None] + np.cos(k)[None, :, None] + np.cos(k)[None, None, :])
    D = Ek + m2
    D1 = np.where(D == 0, np.inf, D)
    return np.real(np.fft.ifftn(1 / D1)), np.real(np.fft.ifftn(1 / D1 ** 2))
def pair_first_order(xA, xB, maskAB, l1):
    mA, mB = lean(xA), lean(xB)
    MA = sum(np.roll(mA, s, axis=d) for d in range(3) for s in (1, -1))
    MB = sum(np.roll(mB, s, axis=d) for d in range(3) for s in (1, -1))
    same = sum((np.roll(mA, s, axis=d) * np.roll(mB, s, axis=d)).sum(-1) for d in range(3) for s in (1, -1))
    X = (MA * MB).sum(-1) - same
    return -3 * l1 ** 2 * float(X[~maskAB].sum())

c0 = L // 2
xA0 = L // 2 - 8
t_start = time.time()
results = {}
for (p, q, r) in ((2.95, 1, 2), (3, 1, 2)):
    om = omega(p, q, r); T = p + q + 4 * r; l1 = (p - q) / T
    m2 = (1 - 6 * l1) / l1 if 6 * l1 < 1 else 0.0
    G, GG = green(m2)
    tag = "(%g,%g,%g)" % (p, q, r)
    print("N %s: 6 l1 = %.4f, m^2 = %.4f (range %.2f), torus side %d" % (tag, 6 * l1, m2, (1 / np.sqrt(m2)) if m2 > 0 else float('inf'), L))
    void = np.full((L, L, L, 6), np.log(1 / 6.0))
    single = {}
    for s in SIDES:
        for c in (0, 1, 2):
            mask, recs = setup([(cube(xA0, s), c)])
            xs, its = solve(om, mask, recs, void)
            single[(s, c)] = (xs, mask)
        EA = energy(single[(s, 0)][0], om, single[(s, 0)][1])
        # far lean: 8 steps beyond the cube's back face along -x, as a multiple of one record's at the same distance from its face
        v = lean(single[(s, 0)][0])[xA0 - 8, c0, c0, 0]
        v1 = lean(single[(1, 0)][0])[xA0 - 8, c0, c0, 0]
        single[(s, 'E')] = EA; single[(s, 'far')] = v / v1
        print("N %s single cube side %d (%d records): E = %+.8e, far lean / one record's = %.4f" % (tag, s, s ** 3, EA, v / v1))
    for rel, cB in REL:
        for s in SIDES:
            row = []
            for d in SEPS:
                bodies = [(cube(xA0, s), 0), (cube(xA0 + d, s), cB)]
                mask, recs = setup(bodies)
                xA = single[(s, 0)][0]
                xB = np.roll(single[(s, cB)][0], d, axis=0)
                warm = xA + xB - np.log(1 / 6.0)
                xs, its = solve(om, mask, recs, warm)
                Eint = energy(xs, om, mask) - 2 * single[(s, 'E')]
                E1 = pair_first_order(xA, xB, mask, l1)
                row.append((d, Eint, E1, its))
                results[(tag, rel, s, d)] = (Eint, E1)
            print("N %s %-10s side %d: " % (tag, rel, s) + "  ".join("d=%d E_int=%+.4e (1st order %+.4e)" % (d, e, e1) for d, e, e1, _ in row))
    # decay: E_int(d)/E_int(6) against G(d)/G(6), G^2, and G*G (the convolution the first-order pair form gives)
    for s in SIDES:
        e = np.array([results[(tag, "equal", s, d)][0] for d in SEPS])
        g = np.array([G[d, 0, 0] for d in SEPS]); gg = np.array([GG[d, 0, 0] for d in SEPS])
        print("N %s decay, equal, side %d: E_int/E_int(6) = %s | G: %s | G^2: %s | G*G: %s" % (
            tag, s, " ".join("%.4f" % z for z in e / e[0]), " ".join("%.4f" % z for z in g / g[0]),
            " ".join("%.4f" % z for z in (g / g[0]) ** 2), " ".join("%.4f" % z for z in gg / gg[0])))
    for d in (8, 12, 16):
        rat = [results[(tag, "equal", s, d)][0] / results[(tag, "equal", 1, d)][0] for s in SIDES]
        far = [single[(s, 'far')] for s in SIDES]
        print("N %s sides at d=%d: E_int(side)/E_int(1) = %s ; record count^2 = %s ; (far-lean capacity ratio)^2 = %s" % (
            tag, d, ", ".join("%.3f" % z for z in rat), ", ".join("%d" % (s ** 6) for s in SIDES), ", ".join("%.3f" % (f * f) for f in far)))
print("N elapsed %.0f s" % (time.time() - t_start))

# ------------------------------------------------------------------ summary (data-driven)
def fit_rms(y, c):
    y, c = np.array(y), np.array(c)
    if np.any(np.sign(y) != np.sign(y[0])) or np.any(c <= 0):
        return float('inf')
    lr = np.log(np.abs(y)) - np.log(c)
    return float(np.sqrt(((lr - lr.mean()) ** 2).mean()))
lines = []
for (p, q, r) in ((2.95, 1, 2), (3, 1, 2)):
    tag = "(%g,%g,%g)" % (p, q, r); T = p + q + 4 * r; l1 = (p - q) / T
    m2 = (1 - 6 * l1) / l1 if 6 * l1 < 1 else 0.0
    G, GG = green(m2)
    se = [results[(tag, "equal", s, d)][0] for s in SIDES for d in SEPS]
    so = [results[(tag, "opposite", s, d)][0] for s in SIDES for d in SEPS]
    orth = max(abs(results[(tag, "orthogonal", s, d)][0]) / abs(results[(tag, "equal", s, d)][0]) for s in SIDES for d in SEPS)
    e1 = [results[(tag, "equal", 1, d)][0] for d in SEPS]
    g = [G[d, 0, 0] for d in SEPS]; gg = [GG[d, 0, 0] for d in SEPS]
    fits = {"G": fit_rms(e1, g), "G^2": fit_rms(e1, [z * z for z in g]), "G*G": fit_rms(e1, gg)}
    best = min(fits, key=fits.get)
    rat1 = [results[(tag, "equal", 1, d)][0] / results[(tag, "equal", 1, d)][1] for d in SEPS]
    capfit = [results[(tag, "equal", s, 12)][0] / results[(tag, "equal", 1, 12)][0] for s in SIDES]
    print("N %s fit of E_int(d), one record each, rms of log(E_int/comparator) after the best constant: %s" % (tag, ", ".join("%s %.3f" % kv for kv in fits.items())))
    print("N %s E_int / first-order pair form, one record each: %s" % (tag, " ".join("%.3f" % z for z in rat1)))
    lines.append("%s equal %s, opposite %s, orthogonal up to %.2f of equal; decay closest to %s (rms %.3f); sides at d=12: %s x one record's" % (
        tag, "negative" if all(z < 0 for z in se) else "of both signs", "positive" if all(z > 0 for z in so) else "of both signs",
        orth, best, fits[best], "/".join("%.2f" % z for z in capfit)))
print("SUMMARY: bookkeeping 'energy' E_int of two cubes in the nonlinear odds field, torus side %d: " % L + "; ".join(lines))
