#!/usr/bin/env python3
"""A first theory of the clumping onset of the six-axis gas with vacancies (block 39; weights c*(p,q,r), empty bonds 1).

Mean field = the variational (Gibbs-Bogoliubov / Bragg-Williams) bound with a product trial law: a site is occupied with probability
rho and carries content s with probability x_s.  Free energy per site (the static law's -log weight per site, z/2 = 3 bonds):
    f(rho, x) = -3 rho^2 sum_{s,s'} x_s x_s' log(c omega(s,s')) + rho log rho + (1 - rho) log(1 - rho) + rho sum_s x_s log x_s.
Part X (exact, sympy): the Hessian at the disordered point and the three spinodals.  Part M (floating point): the coexistence of a
dilute and a dense aligned phase (convex hull of min_x f(rho, x)) and the onset p* on (p,1,2) at rho = 0.3.  Part E: the executed
brackets from logs/probes/X:moving-clumping-line-p12/ (if present).
"""
import glob, json, os, re, sys
import numpy as np
import sympy as sp
from scipy.optimize import minimize

def out(s): print(s, flush=True)

# ------------------------------------------------------------------ X: exact
rho, c, p, q, r = sp.symbols('rho c p q r', positive=True)
xs = sp.symbols('x0:6', positive=True)
def om(a, b): return p if a == b else q if a == (b ^ 1) else r
f = -3 * rho ** 2 * sum(xs[a] * xs[b] * sp.log(c * om(a, b)) for a in range(6) for b in range(6)) \
    + rho * sp.log(rho) + (1 - rho) * sp.log(1 - rho) + rho * sum(x * sp.log(x) for x in xs)
uni = {x: sp.Rational(1, 6) for x in xs}
Lbar = sp.log(c) + (sp.log(p) + sp.log(q) + 4 * sp.log(r)) / 6
frho = sp.simplify(sp.diff(f, rho, 2).subs(uni))
okd = sp.simplify(frho - (-6 * Lbar + 1 / rho + 1 / (1 - rho))) == 0
# content Hessian on the sum-zero subspace: vector mode e_z (+1 at +z, -1 at -z) and quadrupole mode (2,2,-1,-1,-1,-1) along z
H = sp.Matrix(6, 6, lambda i, j: sp.diff(f, xs[i], xs[j]).subs(uni))
vz = sp.Matrix([0, 0, 0, 0, 1, -1]); qz = sp.Matrix([-1, -1, -1, -1, 2, 2])
ev = sp.simplify((vz.T * H * vz)[0] / (vz.T * vz)[0]); eq_ = sp.simplify((qz.T * H * qz)[0] / (qz.T * qz)[0])
okv = sp.simplify(ev - (6 * rho - 6 * rho ** 2 * sp.log(p / q))) == 0
okq = sp.simplify(eq_ - (6 * rho - 6 * rho ** 2 * sp.log(p * q / r ** 2))) == 0
cross = [sp.simplify(sp.diff(f, rho, xs[i]).subs(uni) - sp.diff(f, rho, xs[0]).subs(uni)) for i in range(6)]
out("X exact: at the disordered point d2f/drho2 = 1/rho + 1/(1-rho) - 6 Lbar, Lbar = log c + (log p + log q + 4 log r)/6: %s" % ("PASS" if okd else "FAIL"))
out("X exact: vector-alignment curvature 6 rho (1 - rho log(p/q)), quadrupole 6 rho (1 - rho log(pq/r^2)); no rho-content cross term on the sum-zero subspace: %s"
    % ("PASS" if (okv and okq and all(z == 0 for z in cross)) else "FAIL"))
out("X spinodals: density (uniform clumping) 6 rho (1 - rho) Lbar = 1 (Lbar > 0); alignment rho log(p/q) = 1; quadrupole rho log(pq/r^2) = 1")
R0 = sp.Rational(3, 10)
for lab, cv in (("neutral", 6 / (p + 1 + 8)), ("1", sp.Integer(1)), ("1/2", sp.Rational(1, 2))):
    Lb = (sp.log(cv) + (sp.log(p) + 4 * sp.log(2)) / 6)
    g = sp.lambdify(p, 6 * R0 * (1 - R0) * Lb - 1)
    grid = np.linspace(1.01, 5000, 200000); vals = np.array([g(z) for z in grid[::50]])
    pd = None
    if (vals > 0).any():
        i = np.argmax(vals > 0); lo, hi = grid[::50][max(i - 1, 0)], grid[::50][i]
        pd = float(sp.nsolve(6 * R0 * (1 - R0) * Lb - 1, p, (lo + hi) / 2))
    out("X (p,1,2), c = %-7s rho = 0.3: density spinodal p = %s; alignment spinodal p = e^(1/0.3) = %.2f; quadrupole p = 4 e^(1/0.3) = %.1f"
        % (lab, ("%.2f" % pd) if pd else "none (Lbar < 0 for all p)", np.exp(1 / 0.3), 4 * np.exp(1 / 0.3)))

# ------------------------------------------------------------------ M: coexistence (numerical minimisation)
def fnum(r_, x, P, Q, Rr, C):
    W = np.array([[P if a == b else Q if a == (b ^ 1) else Rr for b in range(6)] for a in range(6)]) * C
    Lm = np.log(W)
    ent = r_ * np.sum(x * np.log(np.clip(x, 1e-300, None)))
    return -3 * r_ ** 2 * x @ Lm @ x + (r_ * np.log(r_) if r_ > 0 else 0) + ((1 - r_) * np.log(1 - r_) if r_ < 1 else 0) + ent
def fmin_x(r_, P, Q, Rr, C):
    best = fnum(r_, np.full(6, 1 / 6), P, Q, Rr, C)
    for a in (0.3, 0.6, 0.9, 0.99, 0.999999):
        def g(y):
            aa = 1 / (1 + np.exp(-y[0]))
            x = np.array([(1 - aa) / 5] * 4 + [aa, (1 - aa) / 5]); return fnum(r_, x, P, Q, Rr, C)
        res = minimize(g, [np.log(a / (1 - a))], method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-14})
        best = min(best, res.fun)
    return best
def coexist(P, C, r0=0.3, n=241):
    rs = np.linspace(1e-4, 1 - 1e-6, n)
    fm = np.array([fmin_x(r_, P, 1.0, 2.0, C) for r_ in rs])
    # lower convex hull
    pts = list(zip(rs, fm)); hull = []
    for pt in pts:
        while len(hull) >= 2 and (hull[-1][0] - hull[-2][0]) * (pt[1] - hull[-2][1]) - (hull[-1][1] - hull[-2][1]) * (pt[0] - hull[-2][0]) <= 0:
            hull.pop()
        hull.append(pt)
    hx = np.array([h[0] for h in hull]); hy = np.array([h[1] for h in hull])
    f0 = fmin_x(r0, P, 1.0, 2.0, C); fh = np.interp(r0, hx, hy)
    k = np.searchsorted(hx, r0)
    return f0 - fh > 1e-9, (hx[max(k - 1, 0)], hx[min(k, len(hx) - 1)])
def onset(Cfun, lo=1.01, hi=400.0):
    if not coexist(hi, Cfun(hi))[0]:
        return None, None
    for _ in range(40):
        mid = np.sqrt(lo * hi)
        if coexist(mid, Cfun(mid))[0]: hi = mid
        else: lo = mid
        if hi / lo < 1.002: break
    return hi, coexist(hi * 1.01, Cfun(hi * 1.01))[1]
res = {}
for lab, Cfun in (("neutral", lambda P: 6 / (P + 9)), ("1", lambda P: 1.0), ("1/2", lambda P: 0.5)):
    ps, tie = onset(Cfun)
    res[lab] = ps
    out("M (p,1,2), c = %-7s rho = 0.3: mean-field coexistence onset p* = %s%s" % (lab, ("%.2f" % ps) if ps else "none below 400",
        ("; just above it the tie line joins rho = %.3f (dilute) and %.3f (dense, aligned)" % tie) if ps else ""))

# ------------------------------------------------------------------ E: executed brackets
exe = {}
logs = glob.glob(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', 'logs', 'probes', 'X:moving-clumping-line-p12', '*.json'))
for fpath in logs:
    try:
        d = json.load(open(fpath))
    except Exception:
        continue
    m = re.search(r'moving_gas\.py (\S+) (\S+) (\S+) (\S+) (\S+)', d.get('command', ''))
    s = d.get('summary', {}).get('summary', '')
    mm = re.search(r'nbrs_over_random=([\d.]+).*aligned=([\d.]+) S=([\d.]+)', s)
    if not m or not mm: continue
    P, sc, rh = float(m.group(1)), m.group(4), float(m.group(5))
    exe.setdefault((sc, rh), []).append((P, float(mm.group(1)), float(mm.group(3))))
out("E executed X logs found: %d (clumped := nbrs/random > 1.5)" % len(logs))
brk = {}
for sc, lab in (("neutral", "neutral"), ("1", "1"), ("0.5", "1/2")):
    rows = sorted(exe.get((sc, 0.3), []))
    if not rows: continue
    agg = {}
    for P, nb, S in rows: agg.setdefault(P, []).append(nb)
    table = [(P, float(np.mean(v))) for P, v in sorted(agg.items())]
    below = [P for P, v in table if v <= 1.5]; above = [P for P, v in table if v > 1.5]
    b = (max([P for P in below if not above or P < min(above)], default=None), min(above, default=None))
    brk[lab] = b
    out("E c = %-7s rho = 0.3: nbrs/random by p: %s -> onset bracket %s" % (lab, " ".join("%g:%.2f" % t for t in table), b))
out("E task's first-look brackets: neutral 8-12 (near 10); scale 1: 5-6; scale 1/2: 8-12")
lines = []
for lab in ("neutral", "1", "1/2"):
    ps = res.get(lab); b = brk.get(lab)
    ref = (0.5 * (b[0] + b[1])) if (b and b[0] and b[1]) else {"neutral": 10.0, "1": 5.5, "1/2": 10.0}[lab]
    lines.append("c=%s: MF %.2f vs executed %s (%+.0f%% of %.1f)" % (lab, ps if ps else float('nan'), b if b else "8-12/5-6", 100 * ((ps or np.nan) / ref - 1), ref))
order_mf = [lab for lab, _ in sorted(((l, res[l]) for l in res if res[l]), key=lambda z: z[1])]
print()
print("SUMMARY: Bragg-Williams (variational product-law) mean field for the six-axis gas with vacancies, rho = 0.3, (p,1,2): " + "; ".join(lines)
      + "; MF onset order (low to high): " + " < ".join(order_mf))
low = all(res[l] and res[l] < ((brk[l][0] if brk.get(l) and brk[l][0] else {"neutral": 8, "1": 5, "1/2": 8}[l])) for l in res)
order_exe = [lab for lab, _ in sorted(((l, 0.5 * (brk[l][0] + brk[l][1])) for l in brk if brk[l][0] and brk[l][1]), key=lambda z: z[1])]
print("E executed onset order (low to high): " + " < ".join(order_exe) + "; same as mean field: %s" % (order_exe == order_mf))
if not low:
    print("HIT: mean field does not put the onset too low at every scale: " + "; ".join(lines))
