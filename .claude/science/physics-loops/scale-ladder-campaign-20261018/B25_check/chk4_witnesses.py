#!/usr/bin/env python3
"""B25_check part 4: failure witnesses of screen survivors, re-derived in the independent build (corelib).
One survivor per obstruction class (C2-pair 4-fold anisotropic; 'low' 4-fold anisotropic; generic anisotropic doublet;
generic single band = Fermi crossing).  For each: the k* level (multiplicity, isotropic cone speed |n_S| sqrt2/3 by finite
differences); the witness node re-found in the independent build (grid nodes exact; generic nodes re-converged by my own
Nelder-Mead on the m eigenphases nearest E); multiplicity at E; finite-difference cone over 300 directions (no DPT); the
point's stabiliser in O mod Lambda_u and mod Lambda_sp (linear action around k* = (pi/2)(1,-1,1); own lattice formulas).
Prints PASS/FAIL, TOTAL."""
import sys, os, itertools, pickle, time
import numpy as np
from scipy.optimize import minimize
import corelib as cl
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
W1 = lambda w, k: cl.Wc(w, np.asarray(k, float)[None])[0]
KST = np.pi / 2 * np.array([1, -1, 1])
rng = np.random.default_rng(44)
DIRS = np.vstack([np.eye(3), rng.normal(size=(300, 3))]); DIRS /= np.linalg.norm(DIRS, axis=1)[:, None]
def phases(w, k, E): return cl.wrap(np.angle(np.linalg.eigvals(W1(w, k))) - E)
def mult(w, k, E, tol=1e-6): return int(np.sum(np.abs(phases(w, k, E)) < tol))
def fd_cone(w, k0, E, m, h=1e-5):
    sl = []; p0 = phases(w, k0, E); p0 = np.sort(p0[np.argsort(np.abs(p0))[:m]]).mean()
    for d in DIRS:
        p = phases(w, k0 + h * d, E); pp = p[np.argsort(np.abs(p))[:m]]
        sl.append(np.sort(pp - p0) / h)                                    # one-sided slopes of the m branches
    sl = np.array(sl); tilt = np.abs(sl.mean(1)).max(); sp = np.abs(sl - sl.mean(1, keepdims=True))
    return float(sp.min()), float(sp.max()), float(tilt)
def refine(w, k0, E, m):
    f = lambda k: float(np.sum(np.sort(np.abs(phases(w, k, E)))[:m]))
    r = minimize(f, k0, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 8000})
    return r.x, r.fun
# lattices (unit pi/32), membership by formula
def member(name, v):
    kind, a = name.split('(')[0], int(name[name.index('(') + 1:-1]) * 2          # B25 names are in pi/16 units
    v = np.asarray(v)
    if kind == 'sc': return bool(np.all(v % a == 0))
    if kind == 'fcc': return bool(np.all(v % a == 0) and (np.sum(v // a) % 2 == 0))
    return bool(np.all(v % a == 0) or np.all((v - a // 2) % a == 0))
ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: ROT.append(M)
def rtype(R):
    t = int(np.trace(R)); return {3: 'E', -1: 'C2', 0: 'C3', 1: 'C4'}[t]
def stab(k, lat):
    q = (np.asarray(k) - KST) / (np.pi / 32); qi = np.round(q).astype(int)
    if np.abs(q - qi).max() > 1e-6: return 'generic', []
    F = [i for i, R in enumerate(ROT) if member(lat, R @ qi - qi)]
    isT = all(i in F for i, R in enumerate(ROT) if rtype(R) in ('E', 'C3') or (rtype(R) == 'C2' and np.all(np.abs(np.diag(R)) == 1)))
    c2p = any(i in F and j in F and np.array_equal(ROT[i] @ ROT[j], ROT[j] @ ROT[i]) for i in F for j in F if i < j and rtype(ROT[i]) == rtype(ROT[j]) == 'C2')
    hasC3 = any(rtype(ROT[i]) == 'C3' for i in F)
    return ('T' if isT else 'C2pair' if c2p else 'C3' if hasC3 else 'low'), sorted({rtype(ROT[i]) for i in F})
# ---- pick survivors
rec = {}
for tag in ('S', 'S2', 'S4'):
    d = pickle.load(open(os.path.join(cl.HERE, '..', 'B25_spectral_tastes', f'screen25_{tag}.pkl'), 'rb'))
    for r in d['recs']:
        if 'nodes' not in r or not r['bad']: continue
        cls_ = {(x[1], x[2], x[3]) for x in r['bad']}
        for key in (('C2', 4, 'aniso'), ('low', 4, 'aniso'), ('gen', 2, 'aniso'), ('gen', 1, 'band')):
            if key in cls_ and key not in rec and (key != ('low', 4, 'aniso') or r['names'] == ('P1', 'L130', 'P11', 'L130')): rec[key] = r
print("   chosen survivors:", {k: (v['sk'][0], v['names'], round(v['E'], 4), v['kind'], v['Lu'], v['Lsp']) for k, v in rec.items()})
for key, r in rec.items():
    w = cl.build(r['sk'], r['names']); E = r['E']; vs = abs(cl.nSw(w)) * np.sqrt(2) / 3
    print(f"\n== {key}: {'.'.join(r['sk'])} {r['names']} E={E:+.4f} ({r['kind']}), Lu={r['Lu']} Lsp={r['Lsp']}, v_D = {vs:.4f}")
    # spectrum identity with the B25 model at the same k (global sign allowed)
    mk = mult(w, KST, E)
    smin, smax, tilt = fd_cone(w, KST, E, mk)
    check(f"{key}: k* level has the screened multiplicity ({r['m']}) and an isotropic untilted cone at |n_S|sqrt2/3 (FD)",
          mk == r['m'] and abs(smin - vs) < 1e-4 and abs(smax - vs) < 1e-4 and tilt < 1e-4, f"m={mk} speeds [{smin:.5f}, {smax:.5f}] tilt {tilt:.1e}")
    x = [x for x in r['bad'] if (x[1], x[2], x[3]) == key][0]
    k0 = np.array(x[0], float) * np.pi; m = x[2]
    if key[0] == 'gen':
        k0, fval = refine(w, k0, E, m)
    else:
        fval = float(np.sum(np.sort(np.abs(phases(w, k0, E)))[:m]))
    mm = mult(w, k0, E, 1e-6)
    s1, s2, tl = fd_cone(w, k0, E, mm if mm else m)
    st_u = stab(k0, r['Lu']); st_s = stab(k0, r['LspE'])
    print(f"   witness k/pi = {np.round(k0 / np.pi, 6)}: residual {fval:.1e}, multiplicity at E {mm}; FD speeds [{s1:.4f}, {s2:.4f}], tilt {tl:.1e}; "
          f"stabiliser mod Lu {st_u}, mod Lsp(E) {st_s}; B25: {x[1]} m={x[2]} {x[3]} smin={x[4].get('smin')} smax={x[4].get('smax')}")
    if key[2] == 'aniso':
        check(f"{key}: witness reproduced -- {m}-fold node at E, anisotropic (FD), point type as B25 states", mm == m and s2 - s1 > 1e-2 and
              (key[0] == 'gen' or (key[0] == 'C2' and st_s[0] == 'C2pair' and st_u[0] == 'C2pair') or (key[0] == 'low' and st_s[0] in ('low', 'C3'))),
              f"aniso ratio {s2 / max(s1, 1e-12):.1f}")
    else:
        # Fermi crossing: one band through E with nonzero slope -> a Fermi surface at level E
        def near(k): p = phases(w, k, E); return p[np.argmin(np.abs(p))]
        g = np.array([(near(k0 + 1e-6 * d) - near(k0 - 1e-6 * d)) / 2e-6 for d in np.eye(3)])
        gh = g / np.linalg.norm(g); flips = near(k0 + 1e-4 * gh) * near(k0 - 1e-4 * gh) < 0
        print(f"   band velocity {np.round(g, 4)}; phase - E changes sign across the node along grad: {flips}")
        check(f"{key}: witness reproduced -- a single band crosses E with nonzero group velocity (Fermi surface, step not gapped at E)", mm == 1 and np.linalg.norm(g) > 1e-3 and flips,
              f"|grad| {np.linalg.norm(g):.3f}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
