#!/usr/bin/env python3
"""B23 fresh-context spot check with an independent model build (core_build.py, from B7_check/chk_core.py).
b23lib/chklib are imported ONLY to (i) fix the momentum/sign dictionary between the two gauges by comparing spectra
of random words, and (ii) read the stored screen records.  Every verdict below is recomputed in core_build:
  survivors (~10 + the two 'closest cases'): k* level = D+ (+) D- at E, its two Weyl blocks (own finite differences),
      the first stored defective node re-located and re-classified by own directional slopes;
  sign-test rejections (~10): own random-point sign test of r(k), a bisected explicit crossing point at E;
  counts: re-tallied from the pickles."""
import os, sys, glob, pickle, itertools, collections, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from scipy.optimize import minimize
import core_build as B
sys.path.insert(0, os.path.join(HERE, '..', 'B23_dirac_level_screen'))
import b23lib as R            # reference only: dictionary + records
t0 = time.time()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)
def wrap(x): return np.angle(np.exp(1j * np.asarray(x)))

# ---------------- (0) dictionary k' = s k + pi lam, W' ~ sgn^{n_S} (D W D)
rng = np.random.default_rng(20261018)
tests = [(('S', 'R', 'o'), ('H13',)), (('S', 'o', 'R', 'o'), ('L123', 'H2.7')), (('S2', 'o', 'Si', 'R', 'o'), ('H31*L012', 'L3.5.11')), (('R',), ()), (('S',), ())]
ks = rng.uniform(-np.pi, np.pi, size=(6, 3))
best = []
for s in (1, -1):
    for lam in itertools.product((0, 1), repeat=3):
        for sg in (1, -1):
            err = 0
            for sk, nm in tests:
                wR = R.build(sk, nm); wB = B.word(sk, nm); g = sg ** B.nS(wB)
                for k in ks:
                    a = np.sort_complex(np.round(np.linalg.eigvals(R.Wword(wR, k)), 10))
                    b = np.sort_complex(np.round(g * np.linalg.eigvals(B.Wk(wB, s * k + np.pi * np.array(lam))), 10))
                    err = max(err, np.abs(a - b).max())
            best.append((err, s, lam, sg))
best.sort(key=lambda x: x[0]); err, SG, LAM, SSIGN = best[0]
print("dictionary candidates (err, s, lam, S-sign):", [(round(e, 3), s, l, g) for e, s, l, g in best[:3]])
check("a unique dictionary k' = s k + pi lam, S' = +-S maps the reference spectra onto the independent build's (5 words x 6 random k)",
      err < 1e-8 and best[1][0] > 1e-3, f"s={SG} lam={LAM} S-sign={SSIGN} err={err:.1e} next={best[1][0]:.2e}")
def kmap(k): return SG * np.asarray(k, float) + np.pi * np.array(LAM)
def Emap(E, w): return float(wrap(E + (np.pi if (SSIGN == -1 and B.nS(w) % 2) else 0)))

# ---------------- records
recs = []
for fn in sorted(glob.glob(os.path.join(HERE, '..', 'B23_dirac_level_screen', 'screen_*.pkl'))):
    d = pickle.load(open(fn, 'rb')); fam = d['tag'].split(':')[0]
    for r in d['recs']: recs.append((fam, d['tag'], r))
surv = [(f, r) for f, t, r in recs if not r['fermi']]; rej = [(f, r) for f, t, r in recs if r['fermi']]
kst = np.array([1, -1, 1]) * np.pi / 2

def eigph(W, E): return wrap(np.angle(np.linalg.eigvals(W)) - E)
def near(W, E, m): e = eigph(W, E); return np.sort(e[np.argsort(np.abs(e))[:m]])
lw, lv = np.linalg.eigh(B.Dsp.conj().T @ B.Lam0 @ B.Dsp)
Bp, Bm = B.Dsp @ lv[:, lw < 0], B.Dsp @ lv[:, lw > 0]; BB = np.hstack([Bp, Bm])
PAU = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
def kstar_blocks(w, E):
    k0 = kmap(kst); W0 = B.Wk(w, k0)
    e, V = np.linalg.eig(W0); sel = np.abs(wrap(np.angle(e) - E)) < 1e-6
    Q, _ = np.linalg.qr(V[:, sel]); Pe = Q @ Q.conj().T; Pd = B.Dsp @ B.Dsp.conj().T
    h = 1e-6; hs = []
    for j in range(3):
        dk = np.zeros(3); dk[j] = h
        G = (B.Wk(w, k0 + dk) - B.Wk(w, k0 - dk)) / (2 * h)
        x = -1j * np.exp(-1j * E) * BB.conj().T @ G @ BB; hs.append((x + x.conj().T) / 2)
    off = max(np.abs(x[:2, 2:]).max() for x in hs); out = []
    for s_ in (slice(0, 2), slice(2, 4)):
        M = np.array([[np.trace(x[s_, s_] @ p).real / 2 for p in PAU] for x in hs]); tr = max(abs(np.trace(x[s_, s_]).real) / 2 for x in hs)
        sv = np.linalg.svd(M, compute_uv=False); out.append((sv.min(), sv.max(), tr, int(np.sign(np.linalg.det(M)))))
    return int(sel.sum()), float(np.abs(Pe - Pd).max()) if sel.sum() == 4 else 9.0, off, out

DIR = rng.normal(size=(60, 3)); DIR /= np.linalg.norm(DIR, axis=1)[:, None]
def node_verdict(w, k0, E, m, vs):
    f = lambda k: float(np.min(np.abs(np.linalg.eigvals(B.Wk(w, k)) - np.exp(1j * E))))
    if f(k0) > 1e-9:
        k0 = minimize(f, k0, method='Powell', options={'xtol': 1e-13, 'ftol': 1e-15, 'maxiter': 20000}).x
        if f(k0) > 1e-9:
            k0 = minimize(f, k0, method='Nelder-Mead', options={'xatol': 1e-13, 'fatol': 1e-15, 'maxiter': 8000}).x
    at = f(k0); e0 = eigph(B.Wk(w, k0), E); mult = int(np.sum(np.abs(e0) < 1e-6))
    sl = []; sl2 = []
    for d in DIR:
        sl.append(near(B.Wk(w, k0 + 1e-6 * d), E, m) / 1e-6); sl2.append(near(B.Wk(w, k0 + 2e-6 * d), E, m) / 2e-6)
    sl, sl2 = np.array(sl), np.array(sl2); A = np.abs(sl)
    lin = float(np.abs(sl - sl2).max())
    tilt = float(np.abs(sl.sum(1)).max() / m); spread = float(A.max() - A.min())
    if m == 1: v = 'band'
    elif A.min() < 1e-3: v = 'flat'
    elif tilt > 1e-3: v = 'tilt'
    elif spread > 1e-3: v = 'aniso'
    elif abs(A.min() - vs) > 1e-3: v = 'iso-otherspeed'
    else: v = 'ok'
    return dict(at=at, mult=mult, verdict=v, smin=float(A.min()), smax=float(A.max()), tilt=tilt, lin=lin, k=k0)

# ---------------- (1) survivors
by = collections.defaultdict(list)
for f, r in surv: by[f].append(r)
pick = []
for f, nsel in (('cliff2', 5), ('pi6', 3), ('taste_pi6', 2)):
    ii = rng.choice(len(by[f]), size=nsel, replace=False); pick += [(f, by[f][i]) for i in ii]
for f, r in surv:      # the two named closest cases
    if (r['sk'] == ('S', 'o', 'R', 'o') and r['names'] == ('H00', 'L022')) or (r['sk'] == ('S', 'R', 'o') and r['names'] == ('L0.6.6',)):
        if not any(r is q for _, q in pick): pick.append((f, r))
ok_lvl = ok_blk = ok_bad = 0; agree = collections.Counter(); nbad_named = {}
for f, r in pick:
    w = B.word(r['sk'], r['names']); E = Emap(r['E'], w); vs = abs(r['nS']) * np.sqrt(2) / 3
    m4, pdev, off, blk = kstar_blocks(w, E)
    lvl = (m4 == 4 and pdev < 1e-8); ok_lvl += lvl
    bk = (off < 1e-6 and all(abs(b[0] - vs) < 1e-6 and abs(b[1] - vs) < 1e-6 and b[2] < 1e-6 for b in blk) and blk[0][3] * blk[1][3] == -1)
    ok_blk += bk
    b0 = r['bad'][0]; nv = node_verdict(w, kmap(np.array(b0[0]) * np.pi), E, b0[2], vs)
    good = nv['at'] < 1e-8 and nv['mult'] == b0[2] and nv['verdict'] != 'ok'; ok_bad += good
    agree[(b0[3], nv['verdict'])] += 1
    nm = f"{f} {r['sk']} {r['names']}"
    if (r['sk'], r['names']) in ((('S', 'o', 'R', 'o'), ('H00', 'L022')), (('S', 'R', 'o'), ('L0.6.6',))):
        nbad_named[nm] = [(x[0], x[1], x[2], x[3]) for x in r['bad']]
    print(f"  SURV {nm} E={r['E']:+.4f}->{E:+.4f} nS={r['nS']} vs={vs:.4f}: k* mult {m4}, |P_E - P_D| {pdev:.1e}, cross {off:.1e}, "
          f"blocks (svmin, svmax, trace, chi) {[(round(a, 6), round(b, 6), round(c, 9), d) for a, b, c, d in blk]}; "
          f"first bad k/pi={b0[0]} ({b0[1]}, m={b0[2]}, stored {b0[3]}): own at-E {nv['at']:.1e}, mult {nv['mult']}, verdict {nv['verdict']} "
          f"|slope| [{nv['smin']:.4f}, {nv['smax']:.4f}] tilt {nv['tilt']:.2e} lin-dev {nv['lin']:.1e}  (#bad stored {len(r['bad'])})", flush=True)
N = len(pick)
check(f"survivors: the k* level is a 4-fold eigenvalue at E whose eigenspace is the H_on = 2 (D+ + D-) space, in the independent build", ok_lvl == N, f"{ok_lvl}/{N}")
check(f"survivors: k* velocity matrices block-diagonal in D+/D-, each block an untilted isotropic cone at |n_S| sqrt2/3, chiralities opposite (own FD)",
      ok_blk == N, f"{ok_blk}/{N}")
check(f"survivors: the first stored defective node is re-located at E (<1e-8) with the stored multiplicity and is NOT an isotropic untilted v_D cone (own slopes)",
      ok_bad == N, f"{ok_bad}/{N}; (stored, own) verdicts {dict(agree)}")
for k_, v_ in nbad_named.items(): print("  named closest case:", k_, "stored bad nodes:", v_)

# ---------------- (2) sign-test rejections
pickr = []
byr = collections.defaultdict(list)
for f, r in rej: byr[f].append(r)
for f, nsel in (('cliff2', 4), ('pi6', 3), ('taste_pi6', 3)):
    ii = rng.choice(len(byr[f]), size=nsel, replace=False); pickr += [(f, byr[f][i]) for i in ii]
KR = rng.uniform(-np.pi, np.pi, size=(3000, 3))
ok_A = ok_sign = ok_cross = 0
for f, r in pickr:
    w = B.word(r['sk'], r['names']); E = Emap(r['E'], w); z = np.exp(1j * E)
    m4, pdev, _, _ = kstar_blocks(w, E); okA = (m4 == 4 and pdev < 1e-8); ok_A += okA
    d0 = np.linalg.det(B.Wk(w, np.zeros(3))); sq = np.sqrt(d0)
    def rr(k):
        Wm = B.Wk(w, k); return np.linalg.det(Wm - z * np.eye(12)) / (z ** 6 * sq), np.linalg.det(Wm)
    vals = [rr(k) for k in KR]; rv = np.array([v[0] for v in vals]); dets = np.array([v[1] for v in vals])
    detc = float(np.abs(dets - d0).max()); rim = float(np.abs(rv.imag).max() / np.abs(rv).max())
    pos_, neg_ = np.where(rv.real > 0)[0], np.where(rv.real < 0)[0]
    sc = len(pos_) > 0 and len(neg_) > 0 and detc < 1e-9 and rim < 1e-8; ok_sign += sc
    cross = None
    if sc:
        a, b = KR[pos_[0]], KR[neg_[0]]; fa = rr(a)[0].real
        for _ in range(80):
            c = (a + b) / 2; fc = rr(c)[0].real
            if np.sign(fc) == np.sign(fa): a, fa = c, fc
            else: b = c
        c = (a + b) / 2; e = eigph(B.Wk(w, c), E); cross = (float(np.min(np.abs(e))), int(np.sum(np.abs(e) < 1e-6)), c / np.pi)
    okc = cross is not None and cross[0] < 1e-9; ok_cross += okc
    print(f"  REJ {f} {r['sk']} {r['names']} E={r['E']:+.4f}: k* D+D- 4-fold {okA}; det W const {detc:.1e}; Im r/|r| {rim:.1e}; "
          f"#r>0 {len(pos_)}, #r<0 {len(neg_)}; bisected crossing: dist {cross[0] if cross else None}, mult {cross[1] if cross else None}, "
          f"k/pi {np.round(cross[2], 4) if cross else None}", flush=True)
M_ = len(pickr)
check("rejections: the k* level is a D+ (+) D- 4-fold level at E in the independent build", ok_A == M_, f"{ok_A}/{M_}")
check("rejections: det W is k-independent, r(k) real, and r changes sign on 3000 independent random momenta", ok_sign == M_, f"{ok_sign}/{M_}")
check("rejections: bisection gives an explicit momentum with an eigenvalue at e^{iE} (< 1e-9): a band crosses the level (Fermi surface)", ok_cross == M_, f"{ok_cross}/{M_}")

# ---------------- (3) counts re-tallied from the pickles
cnt = collections.defaultdict(collections.Counter)
for f, t, r in recs:
    cnt[f]['Dirac'] += 1; cnt[f]['fermi'] += r['fermi']; cnt[f]['surv'] += (not r['fermi'])
    if not r['fermi']: cnt[f]['surv_with_bad'] += bool(r['bad'])
print("  pickle tallies:", {f: dict(c) for f, c in cnt.items()})
exp = {'cliff2': (7352, 6690, 662), 'pi6': (726, 672, 54), 'taste_pi6': (224, 192, 32)}
check("pickle tallies match FINDINGS table (Dirac levels, sign fails, survivors) and every survivor has >= 1 defective node",
      all((cnt[f]['Dirac'], cnt[f]['fermi'], cnt[f]['surv']) == exp[f] and cnt[f]['surv_with_bad'] == exp[f][2] for f in exp))
dv = collections.Counter(); single = 0
for f, t, r in recs:
    if r['fermi']: continue
    for x in r['bad']: dv[x[3]] += 1
print("  defective-node verdict totals over survivors:", dict(dv))
check("defective-node totals match FINDINGS (32,652 aniso, 12,549 tilt, 7,425 flat, 317 band)",
      dv.get('aniso') == 32652 and dv.get('tilt') == 12549 and dv.get('flat') == 7425 and dv.get('band') == 317, str(dict(dv)))

# ---------------- (4) stratified: stored tilt / flat / band defective nodes (3 each), re-classified in the independent build
strat = collections.defaultdict(list)
for f, r in surv:
    for x in r['bad']:
        if x[3] in ('tilt', 'flat', 'band'): strat[x[3]].append((f, r, x))
ok_st = 0; nst = 0; agree2 = collections.Counter()
for vtype in ('tilt', 'flat', 'band'):
    for i in rng.choice(len(strat[vtype]), size=3, replace=False):
        f, r, x = strat[vtype][i]; w = B.word(r['sk'], r['names']); E = Emap(r['E'], w); vs = abs(r['nS']) * np.sqrt(2) / 3
        nv = node_verdict(w, kmap(np.array(x[0]) * np.pi), E, x[2], vs); nst += 1
        good = nv['at'] < 1e-8 and nv['mult'] == x[2] and nv['verdict'] != 'ok'; ok_st += good; agree2[(x[3], nv['verdict'])] += 1
        print(f"  STRAT {vtype}: {f} {r['sk']} {r['names']} k/pi={x[0]} m={x[2]}: own at-E {nv['at']:.1e} mult {nv['mult']} verdict {nv['verdict']} "
              f"|slope| [{nv['smin']:.2e}, {nv['smax']:.3f}] tilt {nv['tilt']:.2e}", flush=True)
check("stratified tilt/flat/band stored defects (3 each): re-located at E with stored multiplicity and NOT ok in the independent build",
      ok_st == nst, f"{ok_st}/{nst}; (stored, own) {dict(agree2)}")
# ---------------- (5) bookkeeping re-tallies of the FINDINGS side statements (from the pickles; not independent physics)
mk = collections.Counter(); noR = []; tgen = []; nfc = 0
for f, r in surv:
    hit = [x for x in r['nodes'] if np.allclose(np.array(x[0]), -kst / np.pi, atol=1e-4)]
    mk[(hit[0][2], hit[0][3]) if hit else 'not at E'] += 1
    if 'R' not in r['sk']: noR.append(len(r['bad']))
    if f == 'taste_pi6': tgen.append(sum(1 for x in r['nodes'] if x[1] == 'generic'))
    if any(x[3] == 'band' for x in r['bad']): nfc += (f == 'cliff2')
print("  -k* node tallies:", dict(mk), "; min #bad for words without R:", min(noR), "; min #generic nodes (taste):", min(tgen), "; cliff2 survivors with a band node:", nfc)
check("bookkeeping: -k* (4 ok) 490 / (8 aniso) 78 / not at E 180; words without R_L >= 26 defective nodes; taste >= 40 generic nodes",
      mk[(4, 'ok')] == 490 and mk[(8, 'aniso')] == 78 and mk['not at E'] == 180 and min(noR) >= 26 and min(tgen) >= 40)
print(f"\nB23_check TOTAL: PASS={PASS} FAIL={FAIL}  [{time.time() - t0:.0f}s]")
