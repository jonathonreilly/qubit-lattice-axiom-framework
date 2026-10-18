"""B24 library: taste-enlarged parameter-free steps.
Model: b24base.py = verbatim copy of B23_dirac_level_screen/b23lib.py (-> B20_check/chklib.py -> B18_check/chk_model.py).
Adds:
  * letters S^{+-4} (S4, S4i) to the batched word builder (S^4(k) = diag(exp(4 i k.f_c)), gauge signs^4 = 1);
  * plane letters: the commutant of the corner-plane signs Z_i inside the symmetric on-site algebra is span{1, PP}
    with PP = PLm[0] + PLm[2] (rank 6); plane letters PL(phi) = PP + e^{i phi} (1 - PP)  (L101, L202, L303 for Clifford
    phases; the pi/6 ones for P6);
  * spectral taste detection: t in (pi/4)Z^3 is a taste with factor omega if spec W(k+t) = omega spec W(k) at random k
    (spectral invariance is what forces cone isotropy at fixed points; operator-level V is checked separately);
  * the PSG affine momentum action (from the operators) and, for a node k on (pi/16)Z^3, its type mod Lambda_0:
    'T' (T-fixed), 'C2' (fixed by a commuting C2 pair, not T), 'low' (neither);
  * generalized stage A/B/C screen for 2-fold (spin-1/2 doublet) and 4-fold D+ (+) D- (Dirac) k* levels."""
import os, sys, collections, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from b25base import *            # noqa
import numpy as np
from scipy.optimize import minimize

PW.update({'S4': 4, 'S4i': -4}); NSP.update({'S4': 4, 'S4i': -4})
fcI = fc.astype(int)
Zs = [np.diag(np.where(fcI[:, i] != 0, -1.0, 1.0)) for i in range(3)]
Ymat = np.diag((-1.0) ** (fcI.sum(1) // 2))
PP = PLm[0] + PLm[2]
def PL(phi): return PP + np.exp(1j * phi) * (np.eye(12) - PP)
PLANE = {'L101': PC['L101'], 'L202': PC['L202'], 'L303': PC['L303']}
PLANE6 = {f"P{a}": PL(np.pi * a / 6) for a in range(1, 12)}
ALL.update(PLANE6)

# ---- PSG affine action (units pi/16, mod 32), from the operators
def _affine():
    out = []
    for (P, s), R in zip(rots, ROTS):
        R = np.array(R, int); cs = set()
        for k in GRIDK:
            kk, U = op_bloch(P, s, k)
            n = np.round(k / (np.pi / 2)).astype(int); n2 = np.round(kk / (np.pi / 2)).astype(int)
            cs.add(tuple((n2 - R @ n) % 4))
        assert len(cs) == 1
        out.append((R, (np.array(list(cs)[0]) // 2) * 16))
    return out
ACT = _affine()
def _typ(R): return {3: 'E', -1: 'C2', 0: 'C3', 1: 'C4'}[int(round(np.trace(R)))]
IST = [_typ(R) == 'E' or _typ(R) == 'C3' or (_typ(R) == 'C2' and np.allclose(np.abs(np.diag(R)), 1)) for R, _ in ACT]
_C2 = [i for i, (R, _) in enumerate(ACT) if _typ(R) == 'C2']
C2PAIRS = [(i, j) for i in _C2 for j in _C2 if i < j and np.array_equal(ACT[i][0] @ ACT[j][0], ACT[j][0] @ ACT[i][0])]

def lat_member(lat16, v):
    """lat16: set of vectors (units pi/16 mod 32) forming the lattice Lambda/2piZ^3."""
    return tuple(int(x) % 32 for x in v) in lat16
def point_type(k, lat16):
    v = np.asarray(k) / (np.pi / 16); vi = np.round(v).astype(int)
    if np.abs(v - vi).max() > 1e-3: return 'gen'
    f = {i for i, (R, c) in enumerate(ACT) if lat_member(lat16, R @ vi + c - vi)}
    if all(i in f for i in range(24) if IST[i]): return 'T'
    if any(i in f and j in f for i, j in C2PAIRS): return 'C2'
    return 'low'

# ---- spectral taste detection on (pi/4)Z^3
_rng = np.random.default_rng(24)
KT = _rng.uniform(-np.pi, np.pi, (2, 3))
TV = [np.array(v) for v in itertools.product(range(8), repeat=3)]      # units pi/4
def spec_match(e1, e2, tol=1e-7):
    """omegas with {e1 + omega} = {e2} as multisets on the circle (Hausdorff both ways; multiplicities via sorted compare)"""
    out = []
    z2 = np.exp(1j * np.asarray(e2))
    for x in e1:
        om = wrap(e2[0] - x); z1 = np.exp(1j * (np.asarray(e1) + om))
        D = np.abs(z1[:, None] - z2[None, :])
        if D.min(1).max() < tol and D.min(0).max() < tol and np.allclose(np.sort((D < tol).sum(1)), np.sort((D < tol).sum(0))):
            out.append(round(float(om), 6))
    return sorted(set(out))
def tastes(w):
    """returns dict t(units pi/4) -> set of omegas (common to both test k)"""
    base = [np.angle(np.linalg.eigvals(Wb(w, k[None])[0])) for k in KT]
    ks = np.array([k + np.pi / 4 * t for t in TV for k in KT])
    Ws = Wb(w, ks); E = np.angle(np.linalg.eigvals(Ws)).reshape(len(TV), len(KT), 12)
    out = {}
    for it, t in enumerate(TV):
        oms = None
        for j in range(len(KT)):
            o = set(spec_match(base[j], E[it, j]))
            oms = o if oms is None else {a for a in oms if any(abs(wrap(a - b)) < 1e-5 for b in o)}
            if not oms: break
        if oms: out[tuple(int(x) for x in t)] = oms
    return out
def lattices(w):
    """Lambda_t (all tastes) and Lambda_0 (tastes with omega = 1 available), as sets in pi/16 units mod 32"""
    T = tastes(w)
    Lt = {tuple((4 * np.array(t)) % 32) for t in T}
    L0 = {tuple((4 * np.array(t)) % 32) for t, o in T.items() if any(abs(x) < 1e-5 for x in o)}
    return Lt, L0
def lat_name(L):
    n = len(L)
    def has(v): return tuple(x % 32 for x in v) in L
    sc = [s for s in (4, 8, 16, 32) if has((s, 0, 0))]; a = min(sc) if sc else 64
    kind = 'sc'
    if a > 4 and has((a // 2, a // 2, 0)): kind = 'fcc'
    elif a > 4 and has((a // 2, a // 2, a // 2)): kind = 'bcc'
    return f"{kind}(a={a}pi/16)|{n}|"

# ---- screen
g16 = np.linspace(-np.pi, np.pi, 16, endpoint=False) + 0.0731
def grid(n): g = np.linspace(-np.pi, np.pi, n, endpoint=False) + 0.0731 * 16 / n; return np.array(list(itertools.product(g, repeat=3)))
SPEC8 = np.array(list(itertools.product(np.arange(-8, 8) * np.pi / 8, repeat=3)))   # (pi/8)Z^3: 4096 points
def maxpow(w): return max([abs(PW[L]) for L in w if isinstance(L, str) and L != 'R'] + [1])
def stageAB(job):
    sk, names = job; w = build(sk, names); ns = nS(w); out = []
    if ns == 0: return ('nS0', [])
    W0 = Wb(w, kst[None])[0]; e, V = np.linalg.eig(W0); st = collections.Counter()
    G = None
    for E, m in levels(W0):
        Vd = V[:, np.abs(wrap(np.angle(e) - E)) < 1e-6]; Q, _ = np.linalg.qr(Vd)
        if m == 2: kind = 'D2'
        elif m == 4 and abs(np.linalg.norm(Q.conj().T @ Dpm) ** 2 - 4) < 1e-6: kind = 'D+D-'
        else: st[f'm{m}'] += 1; continue
        st[kind] += 1
        if G is None:
            G = grid(16 if maxpow(w) <= 2 else 24); Ws = Wb(w, G); c0 = np.linalg.det(Wb(w, np.zeros((1, 3)))[0])
        r = np.linalg.det(Ws - np.exp(1j * E) * np.eye(12)) / (np.exp(6j * E) * np.sqrt(c0))
        rim = float(np.abs(r.imag).max() / max(np.abs(r).max(), 1e-300))
        fermi = bool(r.real.max() > 0 and r.real.min() < 0)
        out.append(dict(sk=sk, names=names, E=float(E), m=m, kind=kind, nS=ns, nR=nR(w), fermi=fermi, rimag=rim))
    return (dict(st), out)
def stageC(rec):
    w = build(rec['sk'], rec['names']); E = rec['E']; vs = abs(rec['nS']) * np.sqrt(2) / 3
    f = lambda k: float(dist_E(w, np.asarray(k)[None], E)[0])
    G = grid(16 if maxpow(w) <= 2 else 24)
    d = dist_E(w, G, E); ds = dist_E(w, SPEC8, E)
    nodes = [k for k, x in zip(SPEC8, ds) if x < 1e-7]
    for i in np.argsort(d)[:int(os.environ.get('B24_NM', '40'))]:
        r_ = minimize(f, G[i], method='Nelder-Mead', options={'xatol': 1e-11, 'fatol': 1e-13, 'maxiter': 3000})
        if r_.fun < 1e-7: nodes.append(r_.x)
    uniq = []
    for k in nodes:
        k = wrap(k)
        if not any(np.linalg.norm(wrap(k - u)) < 1e-4 for u in uniq): uniq.append(k)
    Lt, L0 = lattices(w)
    res = []
    for k in uniq:
        c = classify(w, k, E, vs)
        if c is None: continue
        res.append((tuple(np.round(k / np.pi, 5)), point_type(k, L0), c[0], c[1], {a: round(b, 6) for a, b in c[2].items()}))
    rec = dict(rec); rec['vs'] = vs; rec['gridmin'] = float(d.min()); rec['nodes'] = res
    rec['L0'] = lat_name(L0); rec['Lt'] = lat_name(Lt)
    rec['bad'] = [x for x in res if x[3] != 'ok']
    return rec

# ---- B24 families (no R_L: R_L restricts every taste lattice to 2piZ^3 + pi(1,1,1), see FINDINGS)
MIX2 = [('S', 'o', 'S2', 'o'), ('S', 'o', 'S2i', 'o'), ('S', 'o', 'S4', 'o'), ('S', 'o', 'S4i', 'o'),
        ('S2', 'o', 'S4', 'o'), ('S2', 'o', 'S4i', 'o'), ('S4', 'o', 'S4', 'o')]
PLSK = [('S', 'p', 'S2', 'o'), ('S2', 'p', 'S', 'o'), ('S', 'p', 'S2i', 'o'), ('S2', 'p', 'Si', 'o'),
        ('S', 'p', 'S4', 'o'), ('S4', 'p', 'S', 'o'), ('S2', 'p', 'S4', 'o'), ('S4', 'p', 'S2', 'o'),
        ('S2', 'p', 'S4i', 'o'), ('S4', 'p', 'S2i', 'o'), ('S4', 'p', 'S4', 'o'), ('S', 'p', 'S4i', 'o')]
def jobs24(tag):
    fam, idx = tag.split(':'); sel = [int(i) for i in idx.split(',')]
    if fam == 'mix2':
        for i in sel:
            for n1 in PC:
                for n2 in PC: yield MIX2[i], (n1, n2)
    elif fam == 'plane':
        for i in sel:
            for p in list(PLANE):
                for g in PHL: yield PLSK[i], (p, g)
            for p in PLANE6:
                for g in PC: yield PLSK[i], (p, g)
def build24(sk, names):
    it = iter(names); return [ALL[next(it)] if L in ('o', 'p') else L for L in sk]
build = build24

# ---- taste-designed families (gauge-chain rule: between generic letters, partial S-power sums N_j at plane letters need
#      N_j t in piZ^3 and the segment total N needs N t in 2pi D3*; equal-power segments maximise Lambda_0)
TSK = {'A': ('S4', 'p', 'S4', 'o'),            # Lambda_0 = sc (pi/4) (+ Y-type)
       'B': ('S2', 'p', 'S2', 'o'),            # sc (pi/2), p != L202 (L202 done in B20/B23)
       'C': ('S', 'p', 'S', 'o'),              # sc (pi),   p != L202
       'D': ('S4', 'p', 'S2', 'q', 'S2', 'o'),  # sc (pi/2), mixed powers
       'E': ('S2', 'p', 'S4', 'q', 'S2', 'o'),  # sc (pi/2), mixed powers
       'F': ('S4', 'p', 'S4', 'q', 'S4', 'o')}  # bcc (pi/2) + (pi/4)(1,1,1)
PLALL = {**PLANE, **PLANE6}
def jobsT(tag):
    for f in tag.split(':')[1].split(','):
        sk = TSK[f]
        if sk.count('q'):
            for p in PLANE:
                for q in PLANE:
                    for g in PHL: yield sk, (p, q, g)
        else:
            pl = PLALL if f == 'A' else {n: M for n, M in PLALL.items() if n != 'L202'}
            for p in pl:
                for g in PHL: yield sk, (p, g)
_j24 = jobs24
def jobs24(tag):
    if tag.startswith('taste'): yield from jobsT(tag)
    else: yield from _j24(tag)
def build24(sk, names):
    it = iter(names); return [ALL[next(it)] if L in ('o', 'p', 'q') else L for L in sk]
build = build24

# ---- reduced subfamilies (time budget): plane letters L101, L202, L303 x generic Clifford PC letters
_j24b = jobs24
def jobs24(tag):
    if tag.startswith('small'):
        for f in tag.split(':')[1].split(','):
            sk = TSK[f]
            for p in (PLANE if f == 'A' else ('L101', 'L303')):
                if sk.count('q'):
                    for q in PLANE:
                        for g in PC: yield sk, (p, q, g)
                else:
                    for g in PC: yield sk, (p, g)
    else: yield from _j24b(tag)
