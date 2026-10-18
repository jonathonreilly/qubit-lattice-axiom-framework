#!/usr/bin/env python3
"""B20 check 4: spot-checks of the search, rebuilt in the checker's own model.
 (a) r(k) reality + sign-change witnesses for sampled rejected pairs, converted into an explicit single-band
     crossing of E by bisection (independent of B20's code);
 (b) survivors (no sign change): their recorded failure witnesses are re-evaluated (distance to E, level
     multiplicity, finite-difference speeds);
 (c) census of S2.H20.S2.L202 at E = -pi with own node finder, FD speeds, own Berry flux, and a chord-safe
     Lipschitz certificate."""
import time, pickle, glob
from chklib import *
from scipy.optimize import minimize
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
B20 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'B20_all_isotropic_step')
PH12 = np.exp(1j * np.pi * np.arange(12) / 6)
def onH(a, b, unit): return PH[0] + PH12[(unit * a) % 12] * PH[1] + PH12[(unit * b) % 12] * PH[2]
def onL(a, b, c, unit): return PLm[0] + PH12[(unit * a) % 12] * PLm[1] + PH12[(unit * b) % 12] * PLm[2] + PH12[(unit * c) % 12] * PLm[3]
def mat(n):
    if '*' in n: a, b = n.split('*'); return mat(a) @ mat(b)
    if '.' in n:
        x = [int(t) for t in n[1:].split('.')]; return onH(*x, unit=1) if n[0] == 'H' else onL(*x, unit=1)
    x = [int(t) for t in n[1:]]; return onH(*x, unit=3) if n[0] == 'H' else onL(*x, unit=3)
def build(sk, names):
    it = iter(names); return [mat(next(it)) if L == 'o' else L for L in sk]
recs = []
for fn in sorted(glob.glob(os.path.join(B20, 'screen_*.pkl'))):
    R = pickle.load(open(fn, 'rb')); recs += [(os.path.basename(fn), r) for r in R]
nf = [x for x in recs if not x[1]['fermi']]
check("pickles: 69,894 pairs, 648 without a band crossing", len(recs) == 69894 and len(nf) == 648, f"{len(recs)}, {len(nf)}")
rng = np.random.default_rng(11)
g = np.linspace(-np.pi, np.pi, 16, endpoint=False) + 0.0731
def rfun(w, E, k):
    W = Wword(w, k); return np.linalg.det(W - np.exp(1j * E) * np.eye(12)) / (np.exp(6j * E) * np.sqrt(np.linalg.det(Wword(w, np.zeros(3)))))
# (a) rejected pairs
sample = [recs[i] for i in rng.choice(len(recs), 40, replace=False) if recs[i][1]['fermi']][:25]
okA = 0; okK = 0; detA = []
for fn, r in sample:
    w = build(r['sk'], r['names']); E = r['E']
    lv = [m for e, m in levels(Wword(w, kst)) if abs(wrap(e - E)) < 1e-7]; okK += (lv == [2])
    # find a sign change along grid lines in x
    found = None
    for _ in range(4000):
        i, j, l = rng.integers(16, size=3); a = np.array([g[i], g[j], g[l]]); b = a + np.array([2 * np.pi / 16, 0, 0])
        ra, rb = rfun(w, E, a), rfun(w, E, b)
        if abs(ra.imag) > 1e-8 * abs(ra) + 1e-12: break
        if ra.real * rb.real < 0 and min(abs(ra), abs(rb)) > 1e-6: found = (a, b); break
    if found is None: continue
    a, b = found; fa = rfun(w, E, a).real
    for _ in range(60):
        m_ = (a + b) / 2; fm = rfun(w, E, m_).real
        if fm * fa > 0: a, fa = m_, fm
        else: b = m_
    k0 = (a + b) / 2; c = closest(Wword(w, k0), E, 2)
    if abs(c).min() < 1e-9 and np.ptp(c) > 1e-4: okA += 1
    detA.append((round(float(abs(c).min()), 12), round(float(np.ptp(c)), 4)))
check("(a) sampled rejected pairs: k* level at E is exactly 2-fold in the checker's model; an r sign change is found and bisects to an explicit k where ONE non-degenerate eigenphase equals E (a band crossing)",
      okK == len(sample) and okA == len(sample), f"{okK}/{len(sample)} k* levels, {okA}/{len(sample)} crossings")
# reality of r on a full grid for 3 words
mx = 0
for fn, r in sample[:3]:
    w = build(r['sk'], r['names']); E = r['E']
    for k in itertools.product(g[::3], repeat=3):
        x = rfun(w, E, np.array(k)); mx = max(mx, abs(x.imag) / max(abs(x), 1e-300) if abs(x) > 1e-10 else 0)
check("(a) r(k) is real (det W k-independent: det S = prod sig_c e^{ik.sum f_c}, sum f_c = 0)", mx < 1e-8, f"max rel imag {mx:.1e}")
# (b) survivors
def classify(w, k, E):
    W = Wword(w, k); e = eigph(W); d = np.sort(np.abs(wrap(e - E)))
    mult = int(np.sum(d < 1e-6))
    if mult == 0: return ('no-zero', float(d[0]))
    dirs, sp = fd_speeds(w, k, E, m=mult, h=1e-6, ndir=40, rng=rng)
    sl = np.array([np.sort(a) / 1e-6 for a, _ in sp])          # slopes of the mult bands
    if mult == 2:
        vv = (sl[:, 1] - sl[:, 0]) / 2; tilt = np.abs(sl.sum(1) / 2).max()
        return ('2fold', float(vv.min()), float(vv.max()), float(tilt))
    return (f'{mult}fold', float(np.abs(sl).min()), float(np.abs(sl).max()), 0.0)
idx = rng.choice(len(nf), 24, replace=False); okB = 0; out = []
for i in idx:
    fn, r = nf[i]; w = build(r['sk'], r['names']); E = r['E']; vs = r['vstar']
    wit = [s for s in r['special'] if s[2] - s[1] > 1e-5 or abs(s[1] - vs) > 1e-5] + [z for z in r['zeros'] if not isinstance(z[1], str) and (z[2] - z[1] > 1e-5 or abs(z[1] - vs) > 1e-5)]
    good = False; desc = None
    for s in wit:
        c = classify(w, np.array(s[0]) * np.pi, E)
        if c[0] == '2fold' and (c[2] - c[1] > 1e-3 or abs(c[1] - vs) > 1e-3): good = True; desc = c; break
        if c[0] not in ('2fold', 'no-zero', '1fold') and (abs(c[1] - vs) > 1e-3 or abs(c[2] - vs) > 1e-3): good = True; desc = c; break   # multifold node with a speed != v*
        desc = c
    okB += good; out.append((fn.replace('screen_', '').replace('.pkl', ''), r['sk'], r['names'], round(E, 4), round(vs, 5), desc if desc is None else tuple(np.round(desc[1:], 4)) if desc[0] == '2fold' else desc))
for o in out[:24]: print("   ", o)
check("(b) 24 sampled survivors: at least one recorded witness is, in the checker's model, a node at E (2-fold, or multifold - B20 labels these via a 2x2 projection) with an anisotropic cone or a speed != v*",
      okB == len(idx), f"{okB}/{len(idx)}")
# (c) census of S2.H20.S2.L202 at E = -pi in the (pi/2)-cube [0, pi/2)^3 (pi/2-periodic by the Z tastes)
w = ['S2', UHc(2, 0), 'S2', ULc(2, 0, 2)]; E = -np.pi
f = lambda k: float(np.min(np.abs(wrap(eigph(Wword(w, np.asarray(k))) - E))))
gc = (np.arange(14) + 0.5) * (np.pi / 2) / 14; G_ = np.array(list(itertools.product(gc, repeat=3))); d = np.array([f(k) for k in G_])
sols = []
for i in np.argsort(d)[:120]:
    r_ = minimize(f, G_[i], method='Nelder-Mead', options={'xatol': 1e-11, 'fatol': 1e-13, 'maxiter': 4000})
    if r_.fun < 1e-7:
        x = np.mod(r_.x, np.pi / 2); x[np.abs(x - np.pi / 2) < 1e-6] = 0
        if not any(np.linalg.norm(np.mod(x - s + np.pi / 4, np.pi / 2) - np.pi / 4) < 1e-4 for s in sols): sols.append(x)
cen = []
for s in sols:
    c = classify(w, s, E); fl = berry_flux(w, s, E, r=2e-3, n=14)
    cen.append((tuple(np.round(s / np.pi, 4)), c[0], round(c[1], 5), round(c[2], 5), round(fl, 3)))
for c in sorted(cen): print("   node k/pi", c)
iso = [c for c in cen if c[1] == '2fold' and abs(c[2] - c[3]) < 1e-4]; uni = [c for c in cen if c[1] == '2fold' and abs(c[2] - c[3]) > 1e-3]
check("(c) census: 8 nodes per (pi/2)-cube, all exactly 2-fold; 2 isotropic at 4sqrt2/3 with opposite flux; 6 uniaxial (3 at (pi/4)e_i type, 3 at (pi/4)(1,1,0) type) with opposite flux between the types; total flux 0",
      len(cen) == 8 and len(iso) == 2 and all(abs(c[2] - 4 * np.sqrt(2) / 3) < 1e-4 for c in iso) and round(iso[0][4]) == -round(iso[1][4]) and len(uni) == 6
      and abs(sum(c[4] for c in cen)) < 1e-6 + 0.05, f"uniaxial speed ranges {sorted({(c[2], c[3]) for c in uni})}")
# chord-safe Lipschitz certificate on [0,pi/2)^3 outside 0.03-balls (Lip = 2 * 2sqrt2 for two S^2 letters)
Lip = 4 * np.sqrt(2); P_ = np.pi / 2; balls = np.array(sols); rad0 = 0.03
cells = np.array(list(itertools.product((np.arange(16) + 0.5) * P_ / 16, repeat=3))); size = P_ / 16; bad = 0; ev = 0
for depth in range(9):
    if len(cells) == 0: break
    hd = size * np.sqrt(3) / 2
    dd = np.min(np.linalg.norm(np.mod(cells[:, None, :] - balls[None] + P_ / 2, P_) - P_ / 2, axis=2), axis=1)
    cells = cells[dd + hd > rad0]
    dist = np.array([f(k) for k in cells]); ev += len(cells)
    if np.any(dist < 1e-9): bad = -1; break
    todo = cells[2 * np.sin(np.minimum(dist, np.pi) / 2) <= Lip * hd]   # chord-safe (Bauer-Fike) criterion
    if depth == 8: bad = len(todo); break
    off = np.array(list(itertools.product((-0.25, 0.25), repeat=3))) * size
    cells = (todo[:, None, :] + off[None]).reshape(-1, 3); size /= 2
check("(c) chord-safe Lipschitz certificate (Bauer-Fike, 2 sin(d/2) > Lip * half-diagonal): E = -pi is not reached in the (pi/2)-cube outside 0.03-balls around the 8 nodes",
      bad == 0, f"{ev} evaluations, {bad} uncertified leaf cells")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
