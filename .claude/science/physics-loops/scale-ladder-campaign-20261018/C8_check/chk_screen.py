"""C8 check (d): re-run a seeded sample of C8 screen records with the B26 checker's model (mymodel) and own spectrum code.
Pickles are read as data through the whitelisting unpickler safepk.py.  No C8 / b26lib / chklib / chk_model import."""
import os, sys, itertools, time, collections
os.environ.setdefault('OMP_NUM_THREADS', '3')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mymodel import *
from safepk import load
from scipy.optimize import minimize
P = F = 0
def check(n, ok, d=""):
    global P, F; P += bool(ok); F += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {n}  {d}", flush=True)
t0 = time.time(); rng = np.random.default_rng(8804)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'C8_beyond_permutation_letters')
PK = ['screen_one_PC_0-60.pkl', 'screen_one_PHL_0-8.pkl', 'screen_onesample_PC_60-348_40.pkl', 'screen_two_0-4.pkl', 'screen_twosample_0-84_120.pkl']
kst = np.array([1, -1, 1]) * np.pi / 2; I12 = np.eye(12)
PW = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}
SIG = np.array([S1[tuple(FACE[c])][c, c] for c in range(12)])
RLK = list(RL.keys()); RLM = np.array([RL[a] for a in RLK]); RLA = np.array(RLK, float)
RTK = list(RTX.keys()); RTM = np.array([RTX[a] for a in RTK]); RTA = np.array(RTK, float)
def pal(n):
    if '*' in n: a, b = n.split('*'); return PC[a] @ PC[b]
    return PC[n]
def build(sk, names):
    it = iter(names); return [pal(next(it)) if t == 'o' else t for t in sk]
def Wb(w, ks):
    """batched Bloch word, ks (N,3)"""
    ks = np.atleast_2d(ks); N = len(ks); M = np.broadcast_to(I12.astype(complex), (N, 12, 12)).copy()
    for t in w:
        if isinstance(t, str):
            if t in PW:
                p = PW[t]; M = M * ((SIG ** abs(p)) * np.exp(1j * p * ks @ FACE.T))[:, None, :]
            elif t in ('R', 'E+', 'E-'):
                R = np.einsum('nt,tij->nij', np.exp(1j * ks @ RLA.T), RLM)
                M = M @ (R if t == 'R' else (I12 + 1j * (1 if t == 'E+' else -1) * R) / np.sqrt(2))
            elif t == 'Rt': M = M @ np.einsum('nt,tij->nij', np.exp(1j * ks @ RTA.T), RTM)
            else: raise KeyError(t)
        else: M = M @ t
    return M
def W(w, k): return Wb(w, np.asarray(k, float)[None])[0]
def nS(sk): return sum(PW.get(t, 0) for t in sk)
# self-test of the batched evaluator against the plain mymodel letters
k_ = rng.uniform(-np.pi, np.pi, 3); w_ = ['S', 'E+', PC['L123'], 'S2i', 'Rt', 'E-', 'R']
ref = Sk(k_, 1) @ (I12 + 1j * bloch(RL, k_)) / np.sqrt(2) @ PC['L123'] @ Sk(k_, -2) @ bloch(RTX, k_) @ (I12 - 1j * bloch(RL, k_)) / np.sqrt(2) @ bloch(RL, k_)
check("batched evaluator == product of mymodel letters", np.allclose(W(w_, k_), ref))
def level_kind(Wm, E):
    e, V = np.linalg.eig(Wm); sel = np.abs(wrap(np.angle(e) - E)) < 1e-6; m = int(sel.sum())
    if m == 0: return 0, 'absent'
    Q, _ = np.linalg.qr(V[:, sel])
    if m == 2:
        if np.linalg.norm(Q.conj().T @ DP) ** 2 > 1.999: return m, 'D+'
        if np.linalg.norm(Q.conj().T @ DM) ** 2 > 1.999: return m, 'D-'
        return m, '2?'
    if m == 4 and abs(np.linalg.norm(Q.conj().T @ DPM) ** 2 - 4) < 1e-6: return m, 'D+D-'
    return m, f'{m}-fold'
def rfun(w, ks, E, c0):
    return np.linalg.det(Wb(w, ks) - np.exp(1j * E) * I12) / (np.exp(6j * E) * np.sqrt(c0))
g11 = np.linspace(-np.pi, np.pi, 11, endpoint=False) + 0.0417; GR11 = np.array(list(itertools.product(g11, repeat=3)))
def fermi_witness(w, E):
    c0 = np.linalg.det(W(w, np.zeros(3))); r = rfun(w, GR11, E, c0)
    imag = np.abs(r.imag).max() / max(np.abs(r).max(), 1e-300); rr = r.real
    tag = '11^3'; G = GR11
    if not (rr.max() > 0 and rr.min() < 0):
        tag = None
        for n, off in ((18, 0.0123), (16, 0.0731), (24, 0.0311), (32, 0.0177), (40, 0.0091)):
            g = np.linspace(-np.pi, np.pi, n, endpoint=False) + off; ks = np.array(list(itertools.product(g, repeat=3)))
            rr = np.concatenate([rfun(w, ks[i:i + 8000], E, c0).real for i in range(0, len(ks), 8000)])
            if rr.max() > 0 and rr.min() < 0: tag = f'{n}^3'; G = ks; break
        if tag is None: return None, imag, 'none'
    a, b = G[int(np.argmax(rr))], G[int(np.argmin(rr))]
    f = lambda t: rfun(w, (a + t * (b - a))[None], E, c0)[0].real
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if np.sign(f(mid)) == np.sign(f(lo)): lo = mid
        else: hi = mid
    kc = a + lo * (b - a); dist = np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(w, kc))) - E)))
    return (kc, dist), imag, tag
DIRS60 = rng.normal(size=(60, 3)); DIRS60 /= np.linalg.norm(DIRS60, axis=1)[:, None]; DIRS60[:3] = np.eye(3)
def my_dpt(w, k0, E, h=1e-6):
    W0 = W(w, k0); e, V = np.linalg.eig(W0); sel = np.abs(wrap(np.angle(e) - E)) < 1e-6; m = int(sel.sum())
    if m == 0: return None
    Q, _ = np.linalg.qr(V[:, sel]); hj = []
    for j in range(3):
        dk = np.zeros(3); dk[j] = h; G = (W(w, k0 + dk) - W(w, k0 - dk)) / (2 * h)
        x = -1j * np.exp(-1j * E) * Q.conj().T @ G @ Q; hj.append((x + x.conj().T) / 2)
    tilt = max(abs(np.trace(x).real) / m for x in hj)
    sp = np.abs(np.array([np.linalg.eigvalsh(sum(d[j] * hj[j] for j in range(3))) for d in DIRS60]))
    return m, tilt, sp.min(), sp.max()
def verdict(r, v):
    m, tilt, smin, smax = r
    if m == 1: return 'band'
    if smin < 1e-4: return 'flat'
    if tilt > 1e-4: return 'tilt'
    if smax - smin > 1e-4: return 'aniso'
    if abs(smin - v) > 1e-4: return 'iso-otherspeed'
    return 'ok'

SAMPLE = []; tot = collections.Counter()
for pk in PK:
    recs = load(os.path.join(D, pk))['recs']
    tot['levels'] += len(recs); tot['fermi'] += sum(r['fermi'] for r in recs); tot['surv'] += sum(not r['fermi'] for r in recs)
    tot['clean'] += sum((not r['fermi']) and (not r['bad']) for r in recs)
    f8 = [r for r in recs if r['fermi'] and r['grid'] == 8]; f16 = [r for r in recs if r['fermi'] and r['grid'] == 16]
    sv = [r for r in recs if not r['fermi']]
    for pool, n in ((f8, 4), (f16, 2), (sv, 2)):
        for i in rng.choice(len(pool), size=min(n, len(pool)), replace=False): SAMPLE.append((pk, pool[i]))
print(f"pickle totals: {dict(tot)}")
check("pickle totals match C8 FINDINGS (69,660 levels; 69,021 fail sign test; 639 survivors; 0 with no defective node)",
      tot['levels'] == 69660 and tot['fermi'] == 69021 and tot['surv'] == 639 and tot['clean'] == 0, f"{dict(tot)}")
print(f"sample: {len(SAMPLE)} records")
okA = okF = okC = nF = nC = 0; mism = []
for pk, r in SAMPLE:
    w = build(r['sk'], r['names']); E = r['E']
    m, kind = level_kind(W(w, kst), E); a_ok = kind == r['kind']; okA += a_ok
    if r['fermi']:
        nF += 1; wit, imag, tag = fermi_witness(w, E)
        ok = wit is not None and wit[1] < 1e-8 and imag < 1e-8; okF += ok
        line = f"own {tag} sign change; crossing k/pi={np.round(wit[0] / np.pi, 4)} min|theta-E|={wit[1]:.1e}" if wit else "no own sign change"
        print(f"  FERMI {r['sk']} {r['names']} E={E:+.4f} {r['kind']}/{kind} grid{r['grid']}: {line}")
    else:
        nC += 1; v = abs(nS(r['sk'])) * np.sqrt(2) / 3; b = r['bad'][0]; kb = np.array(b[0], float) * np.pi
        fd = lambda k: float(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(w, k))) - E))))
        if fd(kb) > 1e-7:                                     # C8 stores k/pi rounded to 5 digits: polish locally
            rr_ = minimize(fd, kb, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 4000, 'initial_simplex': kb + 1e-4 * np.vstack([np.zeros(3), np.eye(3)])})
            if np.linalg.norm(wrap(rr_.x - kb)) < 1e-3 and rr_.fun < 1e-7: kb = rr_.x
        res = my_dpt(w, kb, E); vd = verdict(res, v) if res else None
        ok = res is not None and res[0] == b[2] and vd == b[3]; okC += ok
        print(f"  SURV  {r['sk']} {r['names']} E={E:+.4f} {r['kind']}/{kind}: C8 first bad k/pi={b[0]} {b[1]} m={b[2]} {b[3]} (smin {b[4].get('smin')}, smax {b[4].get('smax')});"
              f" own m={res[0] if res else None} {vd}" + (f" (smin {res[2]:.6f}, smax {res[3]:.6f}, tilt {res[1]:.1e})" if res else ""))
    if not (ok and a_ok): mism.append((r['sk'], r['names'], E))
check(f"k* level kind reproduced (own model, own E+- = (1 +- i R_L)/sqrt2)", okA == len(SAMPLE), f"{okA}/{len(SAMPLE)}")
check("sign-test failures confirmed independently (own det-based r on own 11^3 / 18^3 grid + bisection to an actual eigenvalue at e^{iE})", okF == nF and nF > 0, f"{okF}/{nF}")
check("survivor failures confirmed (first defective node: multiplicity and defect type by own finite-difference DPT)", okC == nC, f"{okC}/{nC}")
for x in mism: print("   mismatch:", x)

# closest cases
def census(w, E, v, nstart=60, seed=0):
    rg = np.random.default_rng(seed); f = lambda k: float(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(w, k))) - E))))
    nodes = []
    for s in itertools.product((1, -1), repeat=3): nodes.append(np.array(s) * np.pi / 2)
    for s in rg.uniform(-np.pi, np.pi, (nstart, 3)):
        rr = minimize(f, s, method='Nelder-Mead', options={'xatol': 1e-11, 'fatol': 1e-13, 'maxiter': 4000})
        if rr.fun < 1e-7: nodes.append(wrap(rr.x))
    uniq = []
    for k in nodes:
        if f(k) < 1e-7 and not any(np.linalg.norm(wrap(k - u_)) < 1e-4 for u_ in uniq): uniq.append(k)
    cls = collections.Counter(); out = []
    for k in uniq:
        res = my_dpt(w, k, E)
        if res: vd = verdict(res, v); cls[(res[0], vd)] += 1; out.append((np.round(k / np.pi, 4), res[0], vd, round(res[2], 4), round(res[3], 4)))
    return cls, out
print("\nclosest case E+.S.o (L033), E = -pi/4:")
w = build(('E+', 'S', 'o'), ('L033',)); E0 = -np.pi / 4; v = np.sqrt(2) / 3
lp = my_dpt(w, kst, E0); lm = my_dpt(w, -kst, E0)
print(f"   +k*: kind {level_kind(W(w, kst), E0)} m={lp[0]} tilt={lp[1]:.1e} smin={lp[2]:.6f} smax={lp[3]:.6f} -> {verdict(lp, v)}")
print(f"   -k*: kind {level_kind(W(w, -kst), E0)} m={lm[0]} tilt={lm[1]:.1e} smin={lm[2]:.6f} smax={lm[3]:.6f} -> {verdict(lm, v)}")
check("E+.S.L033: +k* is a 4-fold D+(+)D- untilted isotropic cone at sqrt2/3", lp[0] == 4 and verdict(lp, v) == 'ok' and level_kind(W(w, kst), E0)[1] == 'D+D-')
check("E+.S.L033 FAILS: -k* level at E is 8-fold and not an isotropic cone", lm[0] == 8 and verdict(lm, v) != 'ok', verdict(lm, v))
cls, out = census(w, E0, v, nstart=60, seed=1)
print(f"   own census (8 cube points + 60 Nelder-Mead starts): {sum(cls.values())} nodes, classes {dict(cls)}")
check("own search finds further defective nodes of E+.S.L033 at E (generic tilted/anisotropic)", sum(n for (m_, vd), n in cls.items() if vd != 'ok') >= 2)
# second closest
w2 = build(('E+', 'Rt', 'S', 'o'), ('L011',)); l2 = my_dpt(w2, -kst, E0); l2p = my_dpt(w2, kst, E0)
print(f"   E+.Rt.S.L011: +k* m={l2p[0]} {verdict(l2p, v)}; -k* m={l2[0]} {verdict(l2, v)} smin={l2[2]:.6f} smax={l2[3]:.6f}")
check("E+.Rt.S.L011: +k* isotropic 4-fold, -k* 8-fold defective", l2p[0] == 4 and verdict(l2p, v) == 'ok' and l2[0] == 8 and verdict(l2, v) != 'ok')
print(f"\nTOTAL: PASS={P} FAIL={F}   [{time.time() - t0:.0f}s]")
