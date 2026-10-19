#!/usr/bin/env python3
"""Reviewer report for route B (logs/r8_routeB.json) and route A (logs/r8_routeA.json).
Tolerances were fixed before looking at the n = 64 numbers (after seeing n <= 32 only)."""
import os, json, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
PASS = FAIL = 0
def check(n, ok):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok); print(('PASS' if ok else 'FAIL'), n, flush=True)
RB = json.load(open(os.path.join(HERE, 'logs', 'r8_routeB.json')))
def cG(walk, n, th=0.0, hang=np.pi/2, kind='M1', T=3.0, Fh='own'):
    tot = {}; s = None
    for oc in itertools.product((1, -1), repeat=3):
        key = f"{walk}|th={th}|hang={hang:.4f}|{kind}|n={n}|T={T}|Fh={Fh}|oct={oc}"
        if key not in RB: return None
        s = RB[key]['s']
        for c, v in RB[key]['I2'].items(): tot[c] = tot.get(c, 0.0) + v
    return {c: 2*(-0.25*v/(2*np.pi)**3)/s for c, v in tot.items()}
def cubic(c):
    K = {d: c[d+'A'] + c[d+'B'] for d in 'zfdw'}
    B = 2*(K['z'] - K['f']); A = K['z'] - B; C = 27*(K['d'] - A - B/3)
    q = np.array([2.0, 3, 6])/7
    return A, B, C, 0.5*(A + 0.6*B + C/105), A + B*np.sum(q**4) + C*np.prod(q**2), K['w']
AUTH = {'bstar': dict(zA=8.61015e-3, zB=8.30765e-3, fA=7.24188e-3, fB=6.93391e-3, dA=6.64891e-3, iso=7.36673e-3)}
print('Route B (matrix route + 5-point t-interpolation + octant tanh-sinh), b*, M1:')
rows = {}
for n in (24, 32, 48, 64):
    c = cG('bstar', n)
    if c is None: continue
    A, B, C, iso, pred, Kw = cubic(c); rows[n] = (c, iso)
    print(f"  n={n:3d}: " + '  '.join(f"{k} {c[k]:.9e}" for k in ('zA', 'zB', 'fA', 'fB', 'dA', 'dB')) +
          f"\n          cubic A={A:.6e} B={B:.6e} C={C:.6e}  c_G^iso = {iso:.9e}   K(2,3,6) fit {pred:.9e} vs direct {Kw:.9e}")
nmax = max(rows); c, iso = rows[nmax]; nprev = sorted(rows)[-2]
conv = abs(iso - rows[nprev][1])/iso
print(f"  convergence |iso(n={nmax}) - iso(n={nprev})|/iso = {conv:.1e}")
check(f'B1 route-B quadrature converged: |iso(n={nmax}) - iso(n={nprev})|/iso < 1e-6', conv < 1e-6)
check(f'B2 c_G^iso(b*, M1) = {iso:.7e} agrees with NOTE 7.36673e-3 to 1e-5 relative', abs(iso/7.36673e-3 - 1) < 1e-5)
for ch in ('zA', 'zB', 'fA', 'fB', 'dA'):
    check(f'B3 channel {ch}: {c[ch]:.7e} vs NOTE {AUTH["bstar"][ch]:.5e} (rel < 1e-5)', abs(c[ch]/AUTH['bstar'][ch] - 1) < 1e-5)
A, B, C, iso, pred, Kw = cubic(c)
check(f'B4 O_h cubic form fitted on z,(110),(111) predicts the unused direction (2,3,6)/7: rel {abs(pred/Kw-1):.1e} < 1e-6', abs(pred/Kw - 1) < 1e-6)
check('B5 (111) polarisations degenerate (rel < 1e-9)', abs(c['dA']/c['dB'] - 1) < 1e-9)
check('B6 sign: c_G > 0 in all 8 computed TT channels (b*, M1)', all(v > 0 for v in c.values()))
Ks = [c[d+'A'] + c[d+'B'] for d in 'zfd']
print(f"  anisotropy (max-min)/(2 c_G^iso) over z,f,d = {(max(Ks)-min(Ks))/(2*iso):.3f}  (NOTE: 24.6%)")
check('B7 polarisation-summed TT anisotropy at b* is 24-25% (NOTE 25%)', 0.24 < (max(Ks)-min(Ks))/(2*iso) < 0.25)
print(f"  a/l_P / sqrt(N_f) = sqrt(16 pi c_G) = {np.sqrt(16*np.pi*iso):.4f};  Lambda_eff a = sqrt(96 pi^2 c_G) = {np.sqrt(96*np.pi**2*iso):.4f} = {np.sqrt(96*iso):.4f} pi")
cl = cG('bstar', 32, kind='L1')
if cl is not None:
    mx = max(abs(v) for v in cl.values())
    print('  lapse L1 (vertex = H at midpoint), n=32: ', {k: f"{v:.2e}" for k, v in cl.items()})
    check(f'B8 Lemma L: lapse O(q^2) coefficient |c_N| = {mx:.1e} < 1e-9 (vs c_G ~ 7e-3)', mx < 1e-9)
# ---- b_gold
print('Route B at b_gold, M1 (own h-frame, hhat angle as given; author frame where marked):')
gold = {}
for key in sorted(set(k.rsplit('|oct=', 1)[0] for k in RB if k.startswith('gold'))):
    parts = dict(p.split('=', 1) for p in key.split('|')[1:] if '=' in p)
    th = float(parts['th']); hang = float(parts['hang']); n = int(parts['n']); Fh = parts['Fh']
    c = cG('gold', n, th, hang, 'M1', float(parts['T']), Fh)
    if c is None: continue
    iso = cubic(c)[3]
    gold[(Fh, round(hang, 4), th, n)] = (iso, c)
    print(f"  Fh={Fh:6s} hang={hang:.4f} theta={th:<7g} n={n}: zA {c['zA']:.6e} zB {c['zB']:.6e} fA {c['fA']:.6e} fB {c['fB']:.6e} dA {c['dA']:.6e}  iso {iso:.6e}")
NOTE_GOLD = {0.4: 11.970e-3, 0.2: 16.797e-3, 0.1: 23.098e-3, 0.05: 29.065e-3}
for th, v in NOTE_GOLD.items():
    cand = [(n, x[0]) for (Fh, hg, t, n), x in gold.items() if Fh == 'author' and abs(t - th) < 1e-12]
    if cand:
        n, iso = max(cand)
        check(f'G1 b_gold theta={th} in the author h-frame: iso {iso:.5e} vs NOTE {v:.5e} (rel < 1e-3)', abs(iso/v - 1) < 1e-3)
own = {th: x[0] for (Fh, hg, th, n), x in gold.items() if Fh == 'own' and n == 48}
own64 = {th: x[0] for (Fh, hg, th, n), x in gold.items() if Fh == 'own' and n == 64}
if 0.0 in own and 0.0 in own64:
    check(f'G2 b_gold theta=0 (no mass) quadrature: iso n=48 {own[0.0]:.6e} vs n=64 {own64[0.0]:.6e} (rel < 1e-3)', abs(own[0.0]/own64[0.0] - 1) < 1e-3)
if all(t in own for t in (0.05, 0.0125, 0.003, 0.0)):
    d = [abs(own[t] - own[0.0]) for t in (0.05, 0.0125, 0.003)]
    p1 = np.log(d[0]/d[1])/np.log(4); p2 = np.log(d[1]/d[2])/np.log(0.0125/0.003)
    print(f"  b_gold iso: theta=0.05 {own[0.05]:.5e}, 0.0125 {own[0.0125]:.5e}, 0.003 {own[0.003]:.5e}, 0 {own[0.0]:.5e};"
          f" |c(theta)-c(0)| ~ theta^p with p = {p1:.2f}, {p2:.2f}")
    check('G3 b_gold: c_G^iso(theta) has a finite theta -> 0 limit, approached ~ theta^p with p > 0.5 (contradicts NOTE section 5 "does not converge")',
          d[0] > d[1] > d[2] and min(p1, p2) > 0.5)
import r8_walk as rw
rng = np.random.default_rng(5)
mx = 0.0
for th in (0.0, 0.01, 0.05):
    Wg = rw.Walk(rw.B_GOLD, theta=th)
    k = np.array([np.pi, 0, 0]) + 0.05*rng.normal(size=(4000, 3))
    Hm = Wg.H(k)
    P = np.stack([-np.real(np.einsum('nij,ji->n', Hm, rw.T3S[j]))/4 for j in range(3)], 1)
    mx = max(mx, np.max(np.linalg.norm(P, axis=1)))
check(f'G4 M1 vertex near X at b_gold is bounded, |rho g| <= E <= pi (max sampled {mx:.4f}); NOTE "vertex ~ pi/theta" is incorrect', mx <= np.pi + 1e-12)
# ---- route A
pa = os.path.join(HERE, 'logs', 'r8_routeA.json')
if os.path.exists(pa):
    RA = json.load(open(pa))
    print('Route A (finite antiperiodic lattice, finite q along z), e2_L(q) per lambda^2, b*, M1:')
    Ls = sorted(set(v['L'] for v in RA.values())); ns = sorted(set(v['n'] for v in RA.values()))
    for ch in ('zA', 'zB'):
        tab = {(v['L'], v['n']): v['e2'][ch] for v in RA.values()}
        for n in ns:
            print(f"  {ch} n={n}: " + '  '.join(f"L={L}: {tab[(L, n)]:.10e}" for L in Ls if (L, n) in tab))
    RA_res = {}
    for ch in ('zA', 'zB'):
        tab = {(v['L'], v['n']): v['e2'][ch] for v in RA.values()}
        full = [L for L in Ls if all((L, n) in tab for n in ns)]
        if len(full) < 3: continue
        # L -> infinity: fit e(L) = e_inf + a L^-p (p from the data via the last three L)
        einf = {}
        for n in ns:
            y = np.array([tab[(L, n)] for L in full]); Lv = np.array(full, float)
            # fit e_inf + a/L^2 + b/L^4 by least squares (antiperiodic BC; checked on the data below)
            Mm = np.stack([np.ones_like(Lv), Lv**-2, Lv**-4], 1)
            sol = np.linalg.lstsq(Mm, y, rcond=None)[0]; einf[n] = sol[0]
            print(f"   {ch} n={n}: e_inf = {sol[0]:.10e} (a2 {sol[1]:.3e}, a4 {sol[2]:.3e}); last-L deviation {y[-1]-sol[0]:.2e}")
        qv = np.array([2*np.pi*n/32 for n in ns if n > 0]); dv = np.array([einf[n] - einf[0] for n in ns if n > 0])
        s = list(RA.values())[0]['s']
        pred_c2 = rows[max(rows)][0][ch]*s/2          # c2 = c_G s / 2 from route B
        # q-fit: (e(q)-e(0))/q^2 = c2 + q^2 (a + b ln q)
        Mq = np.stack([np.ones_like(qv), qv**2, qv**2*np.log(qv)], 1)
        sol = np.linalg.lstsq(Mq, dv/qv**2, rcond=None)[0]
        print(f"   {ch}: (e(q)-e(0))/q^2 at q = {np.round(qv,4)}: {dv/qv**2};  fit c2 = {sol[0]:.6e} vs route-B c2 = c_G s/2 = {pred_c2:.6e}")
        RA_res[ch] = (sol[0], pred_c2, dv)
    for ch, (c2A, c2Bv, dv) in RA_res.items():
        check(f'A1 {ch}: finite-lattice finite-q slope extrapolates to the Taylor coefficient (rel {abs(c2A/c2Bv-1):.1e} < 1e-2)', abs(c2A/c2Bv - 1) < 1e-2)
        check(f'A2 {ch}: e2(q) - e2(0) > 0 at every computed q (positive stiffness at finite q)', np.all(dv > 0))
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
