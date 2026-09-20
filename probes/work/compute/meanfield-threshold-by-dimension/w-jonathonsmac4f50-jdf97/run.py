#!/usr/bin/env python3
"""C:meanfield-threshold-by-dimension:a2   worker w-jonathonsmac4f50-jdf97 (claude-opus-5)

Where memory should appear, by dimension, in the simplest approximations, for the sphere formation law
with n predecessors (n = d + 1 backward, n = 2d + 1 light-cone).

A1  mean field: m' = A(n beta m), threshold n beta = 3, exact table for d = 1..4 and both neighbourhoods
A2  exact kernel identities that fix the two plane return sums G_3
A3  rigorous bracket for the light-cone G_3 from exact rational moments
N1  G_d by grid averaging with Richardson extrapolation in 1/L; the divergence for d <= 2
N2  spin-wave plateau 1 - sigma^2 G against the executed plateaus in logs/probes/X:formation-*/
N3  threshold sweeps for both neighbourhoods against the mean-field value
"""
import json, glob, time
from fractions import Fraction
from pathlib import Path
import numpy as np
import sympy as sp

t0 = time.time()
ROOT = next(p for p in (Path(__file__).resolve().parents[5], Path.cwd()) if (p / "logs" / "probes").exists())

# ---------------------------------------------------------------- A1 mean field (exact)
k = sp.symbols("k", positive=True)
A = sp.coth(k) - 1 / k
ser = sp.series(A, k, 0, 8).removeO()
print("A1 A(k) = coth k - 1/k =", sp.nsimplify(sp.expand(ser)), "+ O(k^8)")
print("A1 mean field m' = A(n beta m): the slope at m = 0 is n beta/3, so a positive fixed point appears at n beta = 3")
c1, c3 = sp.Rational(sp.expand(ser).coeff(k, 1)), sp.Rational(sp.expand(ser).coeff(k, 3))
x, M = sp.symbols("x M", positive=True)
print(f"A1 A(k) = k/3 - k^3/45 + ...: coefficients {c1} and {c3}")
root = sp.solve(sp.Eq(M, c1 * x * M + c3 * (x * M) ** 3), M)
pos = [r for r in root if r != 0]
print("A1 so m = A(x m) with x = n beta has the positive root m^2 = 45(x/3 - 1)/x^3 to this order :",
      any(sp.simplify(r ** 2 - 45 * (x / 3 - 1) / x ** 3) == 0 for r in pos))
print("A1 threshold table (exact):  d | backward n=d+1, beta_c=3/n | light-cone n=2d+1, beta_c=3/n")
for d in (1, 2, 3, 4):
    nb, nl = d + 1, 2 * d + 1
    print(f"A1   d={d}: backward n={nb} beta_c={Fraction(3, nb)} = {3/nb:.6f} | "
          f"light-cone n={nl} beta_c={Fraction(3, nl)} = {3/nl:.6f}")

def A_num(x): return 1.0 / np.tanh(x) - 1.0 / x
def mf_plateau(n, beta):
    m = 0.9
    for _ in range(500):
        m = A_num(max(n * beta * m, 1e-12))
    return m if m > 1e-6 else 0.0

# ---------------------------------------------------------------- A2 exact kernel identities
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
E = 2 * sum(1 - sp.cos(x) for x in (k1, k2, k3))
phi_lc = (1 + 2 * sum(sp.cos(x) for x in (k1, k2, k3))) / 7
print("A2 light-cone d=3 (n=7): 1 - |phi|^2 = E(14-E)/49 :",
      sp.simplify(1 - phi_lc ** 2 - E * (14 - E) / 49) == 0)
print("A2 hence 1/(1-|phi|^2) = (7/2)(1/E + 1/(14-E)), so G_3 = (7/2)(<1/E> + <1/(14-E)>),")
print("A2 where <1/E> = W/6 with W the simple-cubic Watson integral and <1/(14-E)> is a smooth average")
re_bw = 1 + sum(sp.cos(x) for x in (k1, k2, k3)); im_bw = sum(sp.sin(x) for x in (k1, k2, k3))
u_bw = (re_bw ** 2 + im_bw ** 2) / 16
lam = (2 * sum(sp.cos(x) for x in (k1, k2, k3))
       + 2 * (sp.cos(k1 - k2) + sp.cos(k1 - k3) + sp.cos(k2 - k3))) / 12
print("A2 backward d=3 (n=4): 1 - |phi|^2 = (3/4)(1 - lambda), lambda the symbol of the uniform walk on the twelve")
print("A2 vectors +-e_j, +-(e_i - e_j) :",
      sp.simplify(sp.expand_trig(sp.expand((1 - u_bw) - sp.Rational(3, 4) * (1 - lam)))) == 0)
print("A2 so the backward walk is that face-centred-cubic walk held with probability 1/4, and G_3^bw = (4/3) G_FCC(0)")
W = sp.sqrt(6) / (32 * sp.pi ** 3) * sp.gamma(sp.Rational(1, 24)) * sp.gamma(sp.Rational(5, 24)) \
    * sp.gamma(sp.Rational(7, 24)) * sp.gamma(sp.Rational(11, 24))
W_val = sp.N(W, 20)
print(f"A2 Watson integral W = sqrt(6)/(32 pi^3) Gamma(1/24)Gamma(5/24)Gamma(7/24)Gamma(11/24) = {W_val}")
print(f"A2 so <1/E> = W/6 = {sp.N(W/6, 20)} (block 22 pinned 3<1/E> between 75/100 and 76/100 by exact terms)")

# ---------------------------------------------------------------- A3 rigorous bracket (exact rational moments)
def moments_E(J):
    """exact <E^j>, j = 0..J, for E = 2(3 - cos k1 - cos k2 - cos k3), from <cos^a> = C(a,a/2)/4^(a/2)"""
    from math import comb, factorial
    mc = [Fraction(comb(a, a // 2), 4 ** (a // 2)) if a % 2 == 0 else Fraction(0) for a in range(J + 1)]
    e = [mc[a] / factorial(a) for a in range(J + 1)]                      # exponential generating coefficients
    def mul(p, q):
        out = [Fraction(0)] * (J + 1)
        for i, pi in enumerate(p):
            if pi:
                for jj in range(0, J + 1 - i):
                    if q[jj]: out[i + jj] += pi * q[jj]
        return out
    e3 = mul(mul(e, e), e)
    Cm = [e3[i] * factorial(i) for i in range(J + 1)]                     # <(cos k1 + cos k2 + cos k3)^i>
    return [Fraction(2) ** j * sum(Fraction(comb(j, i)) * Fraction(3) ** (j - i) * Fraction(-1) ** i * Cm[i]
                                   for i in range(j + 1)) for j in range(J + 1)]
J = 200
mom = moments_E(J)
low = sum(mom[j] / Fraction(14) ** (j + 1) for j in range(J + 1))
tail = Fraction(1, 2) * Fraction(6, 7) ** (J + 1)
print(f"A3 1/(14-E) = (1/14) sum_j (E/14)^j with E/14 <= 6/7, so exact rational moments give a rigorous bracket:")
print(f"A3   {float(low):.9f} <= <1/(14-E)> <= {float(low + tail):.9f}  (J={J} terms, tail {float(tail):.2e})")
print(f"A3 with block 22's rigorous 1/4 < <1/E> < 19/75 this gives")
print(f"A3   {float(Fraction(7,2)*(Fraction(1,4)+low)):.6f} < G_3 light-cone < {float(Fraction(7,2)*(Fraction(19,75)+low+tail)):.6f}")
print(f"A3 and with the Watson value for <1/E>, G_3 light-cone = {float(3.5*(float(sp.N(W/6,20)) + float(low))):.9f}")

# ---------------------------------------------------------------- N1 the plane return sums
def one_minus_u(shape_idx, L, d, sym):
    n = (2 * d + 1) if sym else (d + 1)
    c = np.cos(2 * np.pi * np.arange(L) / L); s = np.sin(2 * np.pi * np.arange(L) / L)
    if sym:
        phi = (1 + 2 * sum(c[i] for i in shape_idx)) / n
        return 1 - phi ** 2
    re = (1 + sum(c[i] for i in shape_idx)) / n; im = sum(s[i] for i in shape_idx) / n
    return 1 - (re * re + im * im)

def G_grid(L, d, sym):
    """(1/L^d) sum_{k != 0} 1/(1-|phi(k)|^2) over the L^d grid"""
    idx = np.meshgrid(*([np.arange(L)] * (d - 1)), indexing="ij") if d > 1 else []
    tot = 0.0
    for i in range(L):
        om = one_minus_u([np.full(idx[0].shape, i) if d > 1 else i] + list(idx), L, d, sym) if d > 1 \
            else one_minus_u([i], L, d, sym)
        om = np.atleast_1d(np.array(om, dtype=float)).copy()
        if i == 0:
            flat = om.reshape(-1); flat[0] = np.inf; om = flat.reshape(om.shape)
        tot += float(np.sum(1.0 / om))
    return tot / L ** d

print("N1 G_d = <1/(1-|phi|^2)> over the grid without the zero mode; Richardson assumes G_L = G_inf - c/L")
G3 = {}
for sym, name in ((True, "light-cone n=7"), (False, "backward n=4")):
    vals = {L: G_grid(L, 3, sym) for L in (48, 64, 96, 128, 192, 256)}
    print(f"N1 d=3 {name}: " + " ".join(f"L={L}:{v:.6f}" for L, v in vals.items()))
    r1, r2 = 2 * vals[192] - vals[96], 2 * vals[256] - vals[128]
    G3[sym] = r2
    print(f"N1 d=3 {name}: Richardson (96,192) = {r1:.6f}, (128,256) = {r2:.6f}, difference {abs(r1-r2):.2e}")
print(f"N1 light-cone against A2/A3: {G3[True]:.6f} vs {3.5*(float(sp.N(W/6,20)) + float(low)):.6f} "
      f"(difference {abs(G3[True] - 3.5*(float(sp.N(W/6,20)) + float(low))):.2e})")
print(f"N1 backward against the FCC constant 1.3446610: (4/3)*1.3446610 = {4/3*1.3446610:.6f} vs {G3[False]:.6f} "
      f"(difference {abs(G3[False] - 4/3*1.3446610):.2e})")
for d, sym, name in ((2, True, "light-cone n=5"), (2, False, "backward n=3"), (1, True, "light-cone n=3"), (1, False, "backward n=2")):
    vals = {L: G_grid(L, d, sym) for L in (64, 128, 256, 512)}
    print(f"N1 d={d} {name}: " + " ".join(f"L={L}:{v:.4f}" for L, v in vals.items()) +
          (f" | successive differences {vals[128]-vals[64]:.4f}, {vals[256]-vals[128]:.4f}, {vals[512]-vals[256]:.4f}"
           f" (constant differences = log L growth)" if d == 2 else
           f" | ratios {vals[128]/vals[64]:.4f}, {vals[256]/vals[128]:.4f}, {vals[512]/vals[256]:.4f} (2 = linear in L)"))

# ---------------------------------------------------------------- N2 spin-wave plateaus against executed logs
print("N2 executed plateaus in logs/probes/X:formation-*/ against 1 - sigma^2 G, sigma^2 = A(n beta)/(n beta),")
print("N2 with G taken on the same box (G_L) and in the limit (G_inf)")
rows = []
for f in sorted(glob.glob(str(ROOT / "logs" / "probes" / "X:formation-*" / "*.json"))):
    j = json.load(open(f))
    s = j.get("summary"); s = s.get("summary") if isinstance(s, dict) else s
    if not s or "menu=sphere" not in s: continue
    parts = dict(p.split("=") for p in s.split() if "=" in p)
    cmd = j.get("command", "")
    sym = " 3s " in cmd or " 2s " in cmd or " 4s " in cmd
    d = int(parts["dim"]); beta = float(parts["beta"]); L = int(parts["L"])
    plateau = float(parts["plateau_|m|"]); n = (2 * d + 1) if sym else (d + 1)
    rows.append((d, sym, n, beta, L, plateau, Path(f).parent.name))
for d, sym, n, beta, L, plateau, task in sorted(rows):
    s2 = A_num(n * beta) / (n * beta)
    GL = G_grid(L, d, sym); Ginf = G3[sym] if d == 3 else float("nan")
    pred_L = 1 - s2 * GL; pred_inf = 1 - s2 * Ginf
    mf = mf_plateau(n, beta)
    print(f"N2 d={d} {'light-cone' if sym else 'backward'} n={n} beta={beta} L={L}: executed |m|={plateau:.4f} | "
          f"spin wave 1-sigma^2 G_L={pred_L:.4f} (relative {abs(pred_L-plateau)/max(plateau,1e-9)*100:.1f}%), "
          f"G_inf={pred_inf:.4f} | mean field {mf:.4f} | sigma^2={s2:.6f} G_L={GL:.4f}  [{task}]")

# ---------------------------------------------------------------- N3 threshold sweeps
def formation_plateau(d, sym, beta, L, T, seed=5):
    rng = np.random.default_rng(seed); shape = (L,) * d
    s = np.zeros(shape + (3,)); s[..., 2] = 1; tail = []
    for t in range(1, T + 1):
        S = s + sum(np.roll(s, 1, axis=j) + (np.roll(s, -1, axis=j) if sym else 0) for j in range(d))
        nrm = np.linalg.norm(S, axis=-1); nrm = np.where(nrm < 1e-12, 1e-12, nrm)
        uu = S / nrm[..., None]; kappa = beta * nrm
        U = rng.random(shape); w = np.clip(1 + np.log(U + (1 - U) * np.exp(-2 * kappa)) / kappa, -1, 1)
        ph = rng.random(shape) * 2 * np.pi
        a = np.where((np.abs(uu[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
        b1 = a - (a * uu).sum(-1)[..., None] * uu; b1 /= np.linalg.norm(b1, axis=-1)[..., None]
        b2 = np.cross(uu, b1); r = np.sqrt(np.clip(1 - w * w, 0, 1))
        s = w[..., None] * uu + r[..., None] * (np.cos(ph)[..., None] * b1 + np.sin(ph)[..., None] * b2)
        if t > 0.75 * T: tail.append(float(np.linalg.norm(s.reshape(-1, 3).mean(0))))
    return float(np.mean(tail))

print("N3 threshold sweep on a 32^3 level plane, T = 2500 from an aligned start; the finite-size floor is about 0.02")
brackets = {}
for sym, name, betas in ((False, "backward n=4", (0.75, 0.9, 1.1, 1.3, 1.5)),
                         (True, "light-cone n=7", (0.43, 0.48, 0.52, 0.56, 0.60))):
    n = 7 if sym else 4
    vals = []
    for b in betas:
        p = formation_plateau(3, sym, b, 32, 2500)
        vals.append((b, p)); print(f"N3 {name} beta={b:.2f}: plateau |m| = {p:.4f} (mean field {mf_plateau(n, b):.4f})")
    ordered = [b for b, p in vals if p > 0.2]; floor = [b for b, p in vals if p <= 0.05]
    lo = max(floor) if floor else float("nan"); hi = min(ordered) if ordered else float("nan")
    brackets[sym] = (lo, hi)
    print(f"N3 {name}: executed threshold between {lo} and {hi}; mean field says 3/{n} = {3/n:.4f}")

print("N4 the task's stated coupling: my own runs at beta = 6 on a 32^3 plane, T = 2000")
own = []
for sym, name in ((False, "backward n=4"), (True, "light-cone n=7")):
    n = 7 if sym else 4
    pl = formation_plateau(3, sym, 6.0, 32, 2000, seed=9)
    s2 = A_num(n * 6.0) / (n * 6.0); GL = G_grid(32, 3, sym)
    pred = 1 - s2 * GL
    own.append((3, n, 6.0, 32, pl, pred))
    print(f"N4 {name} beta=6 L=32: executed |m| = {pl:.4f} vs spin wave 1 - sigma^2 G_L = {pred:.4f} "
          f"({abs(pred-pl)/pl*100:.2f}%), mean field {mf_plateau(n, 6.0):.4f}, sigma^2 = {s2:.6f}, G_L = {GL:.4f}, "
          f"G_inf gives {1 - s2*G3[sym]:.4f}")

mf_under = all(3 / (7 if sym else 4) < brackets[sym][0] for sym in (False, True))
print(f"N3 mean field below the executed bracket for both neighbourhoods: {mf_under}")
big = [(d, n, beta, L, pl, 1 - A_num(n*beta)/(n*beta) * G_grid(L, d, sym)) for d, sym, n, beta, L, pl, _ in rows
       if beta >= 6 and d == 3] + own
worst = max((abs(p - pl) / pl * 100, beta, L, pl, p) for d, n, beta, L, pl, p in big) if big else None
print("N2/N3 high-coupling check: " + ("; ".join(f"beta={b} L={L}: executed {pl:.4f} vs spin wave {p:.4f} "
      f"({abs(p-pl)/pl*100:.2f}%)" for d, n, b, L, pl, p in big) if big else "no executed point at beta >= 6"))
print(f"SUMMARY: mean-field threshold is 3/n exactly (0.75 backward, 3/7 light-cone in d=3) and the executed "
      f"brackets are ({brackets[False][0]},{brackets[False][1]}) and ({brackets[True][0]},{brackets[True][1]}), so "
      f"mean field underestimates: {mf_under}; G_3 = {G3[False]:.6f} backward (= (4/3)G_FCC) and {G3[True]:.6f} "
      f"light-cone (= (7/2)(W/6 + <1/(14-E)>)), and the spin-wave plateau at beta >= 6 is within "
      f"{worst[0]:.2f}% of the executed value; {time.time()-t0:.0f}s")
bad = []
if not mf_under: bad.append("mean field does not underestimate the threshold")
if worst and worst[0] > 3.0: bad.append(f"the spin-wave plateau at beta >= 6 is off by {worst[0]:.1f}%")
if bad: print("HIT: " + "; ".join(bad))
