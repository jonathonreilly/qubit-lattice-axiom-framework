#!/usr/bin/env python3
"""B24_check part 3 (claims 4 and 5).
Own word builder from the B18_check/chk_model primitives (SKc, PH, PLm) -- not b24base/b24lib/b23lib Wb/dpt/classify.
Own node refinement (Nelder-Mead on the m smallest |E - theta|), own cone diagnosis (finite-difference eigenphase slopes over
300 directions, not DPT), own spectral taste lattice Lambda_0 and own point typing (linear O action around k*).
 (4) three survivors' failure witnesses re-derived:
     A  mix2  S.H20.S2.L020        E=0     D+D-  : 4-fold nodes at cube points that are C2-type mod Lambda_0
     B  small S4.L101.S4.H13       E=-pi/2 D2    : 2-fold node at k* + (pi/8) e_z (the sc scale-free witness at a = pi/4)
     C  small S4.L101.S4.L123      E=0     D+D-  : 2-fold nodes at generic momenta
 (5) pinning at the bad points: for every recorded survivor, at every C2-pair-fixed-but-not-T class mod its own Lambda_0,
     are all 12 levels even?  (tests whether 'C2-pair point' and 'pinning point' coincide in the screened families)."""
import os, sys, itertools, pickle, collections, time
import numpy as np
from scipy.optimize import minimize
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B18_check'))
import chk_model as cm
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
B24 = os.path.join(HERE, '..', 'B24_taste_enlarged_steps')
wrap = lambda x: np.angle(np.exp(1j * np.asarray(x)))
POW = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2, 'S4': 4, 'S4i': -4}
I4 = [1, 1j, -1, -1j]
def onsite(name):
    if name[0] == 'H': a, b = int(name[1]), int(name[2]); return cm.PH[0] + I4[a] * cm.PH[1] + I4[b] * cm.PH[2]
    a, b, c = (int(x) for x in name[1:4]); return cm.PLm[0] + I4[a] * cm.PLm[1] + I4[b] * cm.PLm[2] + I4[c] * cm.PLm[3]
def word(sk, names):
    it = iter(names); return [L if L in POW else onsite(next(it)) for L in sk]
def W(w, k):
    d = np.diag(cm.SKc(np.asarray(k, float))); M = np.eye(12, dtype=complex)
    for L in w:
        if isinstance(L, str): p = POW[L]; M = M @ np.diag(d ** p if p > 0 else np.conj(d) ** (-p))
        else: M = M @ L
    return M
def ph(w, k): return np.angle(np.linalg.eigvals(W(w, k)))
def mults(e, tol=1e-6):
    z = np.sort(np.mod(e + 0.1234, 2 * np.pi)); out = []; i = 0
    while i < len(z):
        j = i
        while j + 1 < len(z) and z[j + 1] - z[i] < tol: j += 1
        out.append(j - i + 1); i = j + 1
    if len(out) > 1 and (z[0] + 2 * np.pi - z[-1]) < tol: out[0] += out.pop()
    return out
def nS(sk): return sum(POW.get(L, 0) for L in sk)
KST = np.array([1, -1, 1]) * np.pi / 2

# ---- rotations (own), T, commuting C2 pairs
ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: ROT.append(M)
tr = [int(np.trace(R)) for R in ROT]
isT = [t in (3, 0) or (t == -1 and np.all(np.abs(np.diag(R)) == 1)) for R, t in zip(ROT, tr)]
C2 = [i for i, t in enumerate(tr) if t == -1]
C2P = [(i, j) for i in C2 for j in C2 if i < j and np.array_equal(ROT[i] @ ROT[j], ROT[j] @ ROT[i])]

# ---- own spectral Lambda_0 on (pi/4)Z^3 (omega = 1 only)
rng = np.random.default_rng(99); KT = rng.uniform(-np.pi, np.pi, (3, 3))
def same_spec(a, b, tol=1e-7):
    za, zb = np.exp(1j * a), np.exp(1j * b); D = np.abs(za[:, None] - zb[None, :])
    return D.min(1).max() < tol and D.min(0).max() < tol and sorted((D < tol).sum(1)) == sorted((D < tol).sum(0))
def lambda0(w):
    base = [ph(w, k) for k in KT]
    return {t for t in itertools.product(range(8), repeat=3) if all(same_spec(b, ph(w, k + np.pi / 4 * np.array(t))) for b, k in zip(base, KT))}
def lname(L):
    n = len(L); m = min(s for s in (1, 2, 4, 8) if (s % 8, 0, 0) in L)
    if n == (8 // m) ** 3: return f"sc({m}pi/4)"
    if (m // 2, m // 2, 0) in L and m > 1: return f"fcc({m // 2}pi/4)"
    if (m // 2, m // 2, m // 2) in L and m > 1: return f"bcc({m}pi/4)"
    return f"?({n})"
def in_L(L, v16):          # v16 in pi/16 units
    v = [int(x) % 32 for x in v16]; return all(x % 4 == 0 for x in v) and tuple(x // 4 for x in v) in L
def ptype(L, k):
    q = (np.asarray(k) - KST) / (np.pi / 16); qi = np.round(q).astype(int)
    if np.abs(q - qi).max() > 1e-3: return 'gen', None
    fix = [i for i, R in enumerate(ROT) if in_L(L, R @ qi - qi)]
    if all(i in fix for i in range(24) if isT[i]): return 'T', fix
    if any(i in fix and j in fix for i, j in C2P): return 'C2', fix
    return 'low', fix

# ---- own node refinement + finite-difference cone diagnosis
DIRS = np.vstack([np.eye(3), rng.normal(size=(300, 3))]); DIRS /= np.linalg.norm(DIRS, axis=1)[:, None]
def gapE(w, k, E, m): return np.sort(np.abs(wrap(ph(w, k) - E)))[:m].sum()
def refine(w, k, E, m):
    r = minimize(lambda x: gapE(w, x, E, m), k, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 4000})
    return r.x, r.fun
def cone(w, k, E, m, h=1e-5):
    sl = []
    for d in DIRS:
        e = ph(w, k + h * d); dd = wrap(e - E); idx = np.argsort(np.abs(dd))[:m]; sl.append(np.sort(dd[idx]) / h)
    sl = np.array(sl); tilt = np.abs(sl.mean(1)).max(); sp = np.abs(sl - sl.mean(1, keepdims=True))
    return dict(smin=float(sp.min()), smax=float(sp.max()), tilt=float(tilt))

def load(f): return [r for r in pickle.load(open(os.path.join(B24, f), 'rb'))['recs'] if not r['fermi']]
SM = load('screen_small_A-B-C-D-E.pkl'); MX = load('screen_mix2_0-1-2-3.pkl')
def find(recs, sk, names, E):
    return [r for r in recs if r['sk'] == sk and r['names'] == names and abs(wrap(r['E'] - E)) < 1e-6][0]
CASES = [('A', MX, ('S', 'o', 'S2', 'o'), ('H20', 'L020'), 0.0), ('B', SM, ('S4', 'p', 'S4', 'o'), ('L101', 'H13'), -np.pi / 2),
         ('C', SM, ('S4', 'p', 'S4', 'o'), ('L101', 'L123'), 0.0)]
for tag, recs, sk, names, E in CASES:
    r = find(recs, sk, names, E); w = word(sk, names); vs = abs(nS(sk)) * np.sqrt(2) / 3
    L0 = lambda0(w); e0 = ph(w, KST)
    mk = int(np.sum(np.abs(wrap(e0 - E)) < 1e-6))
    print(f"\n  case {tag}: {sk} {names} E={E:+.4f}  recorded kind {r['kind']} L0={r['L0']} nbad={len(r['bad'])};  own: m(k*)={mk}, Lambda_0={lname(L0)} |{len(L0)}|, v_s={vs:.4f}")
    c0 = cone(w, KST, E, mk)
    check(f"{tag}: k* level at E has the recorded multiplicity and is an isotropic untilted cone at v_s = |n_S|sqrt2/3 (FD slopes)",
          mk == r['m'] and abs(c0['smin'] - vs) < 1e-4 and abs(c0['smax'] - vs) < 1e-4 and c0['tilt'] < 1e-4, f"{c0}")
    picks = []
    want = {'A': 'C2', 'B': 'C2', 'C': 'gen'}[tag]
    for x in r['bad']:
        if x[1] == want and x[3] in ('aniso',) and len(picks) < 3: picks.append(x)
    okall = True
    for x in picks:
        k = np.array(x[0], float) * np.pi; m = x[2]
        kk, res = refine(w, k, E, m) if x[1] == 'gen' else (k, gapE(w, k, E, m))
        c = cone(w, kk, E, m); t_, _ = ptype(L0, kk); mm = mults(ph(w, kk))
        good = res < 1e-8 and (c['smax'] - c['smin']) > 1e-2 and t_ == x[1]
        okall &= good
        print(f"    witness {x[0]} rec ({x[1]}, m={m}, {x[3]}, smin={x[4]['smin']:.4f}, smax={x[4]['smax']:.4f}) -> own: node residual {res:.1e}, "
              f"type {t_}, FD smin={c['smin']:.4f} smax={c['smax']:.4f} tilt={c['tilt']:.1e}, level mults at k {mm}")
    check(f"{tag}: recorded failure witnesses reproduced (node at E, same point type mod own Lambda_0, anisotropic speeds)", okall and len(picks) > 0, f"{len(picks)} witnesses")
    check(f"{tag}: own Lambda_0 equals the recorded one", lname(L0).replace('pi/4', '') == {
        'sc(a=4pi/16)|512|': 'sc(1)', 'sc(a=8pi/16)|64|': 'sc(2)', 'sc(a=16pi/16)|8|': 'sc(4)', 'bcc(a=32pi/16)|2|': 'bcc(8)', 'bcc(a=8pi/16)|128|': 'bcc(2)'}[r['L0']],
          f"{lname(L0)} vs {r['L0']}")

# ---- (5) even levels at every bad class, all recorded survivors
print("\n  (5) level multiplicities at C2-pair-not-T classes mod each survivor's own Lambda_0")
grid = np.array(list(itertools.product(range(32), repeat=3)))
stat = collections.Counter(); odd_examples = []
cacheL = {}
for recs, fam in ((SM, 'small'), (MX, 'mix2')):
    seen = set()
    for r in recs:
        key = (r['sk'], r['names'])
        if key in seen: continue
        seen.add(key); w = word(*key)
        L0 = lambda0(w)
        # classes of C2-pair-not-T points mod L0 (q on (pi/16) grid), vectorised
        memb = np.zeros((32, 32, 32), bool)
        for t in L0: memb[tuple(4 * np.array(t))] = True
        FIX = np.array([memb[tuple(((grid @ R.T - grid) % 32).T)] for R in ROT])
        pair = np.zeros(len(grid), bool)
        for i, j in C2P: pair |= FIX[i] & FIX[j]
        badm = pair & ~np.all(FIX[np.array(isT)], axis=0)
        Lv = 4 * np.array(sorted(L0)); covered = np.zeros((32, 32, 32), bool); reps = {}
        for q in grid[badm]:
            if covered[tuple(q)]: continue
            reps[tuple(int(x) for x in q)] = 1; covered[tuple(((q + Lv) % 32).T)] = True
        for rep in reps:
            mm = mults(ph(w, KST + np.pi / 16 * np.array(rep)))
            ev = all(x % 2 == 0 for x in mm); stat[(fam, lname(L0), ev)] += 1
            if not ev and len(odd_examples) < 6: odd_examples.append((key, lname(L0), rep, mm))
print("   (family, Lambda_0, all levels even) -> #bad classes:", dict(stat))
for o in odd_examples: print("   odd-level bad class:", o)
check("(5) audit ran over every distinct recorded survivor word", sum(stat.values()) > 0, f"{sum(stat.values())} bad classes examined")
print(f"   all-even at every bad class: {all(k[2] for k in stat)}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
