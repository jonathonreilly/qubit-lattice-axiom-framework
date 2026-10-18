"""(e): re-run a seeded sample of B26 screen records with the own model and own spectrum code."""
import sys, itertools, time, collections
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from mymodel import *
from safepk import load
from scipy.optimize import minimize
P = F = 0
def check(n, ok, d=""):
    global P, F; P += bool(ok); F += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {n}  {d}", flush=True)
t0 = time.time(); rng = np.random.default_rng(2610)
D = '/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B26_new_shift_letters/'
PK = ['screen_one_PC_0-74.pkl', 'screen_one_PHL_0-22.pkl', 'screen_onesample_PHL_22-74_300.pkl', 'screen_two_0-3.pkl', 'screen_twosample_3-40_300.pkl']
kst = np.array([1, -1, 1]) * np.pi / 2
A0i = A0m.conj().T
PW = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}
def pal(n):
    if '*' in n: a, b = n.split('*'); return PC[a] @ PC[b]
    return PC[n]
def build(sk, names):
    it = iter(names); return [pal(next(it)) if t == 'o' else t for t in sk]
def W(w, k):
    M = np.eye(12, dtype=complex)
    for t in w:
        if isinstance(t, str):
            if t == 'R': M = M @ bloch(RL, k)
            elif t == 'Rt': M = M @ bloch(RTX, k)
            else: M = M @ Sk(k, PW[t])
        else: M = M @ t
    return M
def nS(sk): return sum(PW.get(t, 0) for t in sk)
def level_kind(Wm, E):
    e, V = np.linalg.eig(Wm); sel = np.abs(wrap(np.angle(e) - E)) < 1e-6; m = int(sel.sum())
    Q, _ = np.linalg.qr(V[:, sel])
    if m == 2:
        if np.linalg.norm(Q.conj().T @ DP) ** 2 > 1.999: return m, 'D+'
        if np.linalg.norm(Q.conj().T @ DM) ** 2 > 1.999: return m, 'D-'
        return m, '2?'
    if m == 4 and abs(np.linalg.norm(Q.conj().T @ DPM) ** 2 - 4) < 1e-6: return m, 'D+D-'
    return m, f'{m}-fold'
def rfun(w, ks, E, c0):
    return np.array([np.linalg.det(W(w, k) - np.exp(1j * E) * np.eye(12)) for k in ks]) / (np.exp(6j * E) * np.sqrt(c0))
g10 = np.linspace(-np.pi, np.pi, 10, endpoint=False) + 0.0533; GR10 = np.array(list(itertools.product(g10, repeat=3)))
def fermi_witness(w, E):
    """sign change of r on an own 10^3 grid, then bisection along the segment to an actual eigenvalue at e^{iE}."""
    c0 = np.linalg.det(W(w, np.zeros(3))); r = rfun(w, GR10, E, c0)
    imag = np.abs(r.imag).max() / max(np.abs(r).max(), 1e-300); rr = r.real
    if not (rr.max() > 0 and rr.min() < 0): return None, imag
    i = int(np.argmax(rr)); j = int(np.argmin(rr)); a, b = GR10[i], GR10[j]
    f = lambda t: rfun(w, [a + t * (b - a)], E, c0)[0].real
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if np.sign(f(mid)) == np.sign(f(lo)): lo = mid
        else: hi = mid
    kc = a + lo * (b - a); dist = np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(w, kc))) - E)))
    return (kc, dist), imag
DIRS50 = rng.normal(size=(50, 3)); DIRS50 /= np.linalg.norm(DIRS50, axis=1)[:, None]; DIRS50[:3] = np.eye(3)
def my_dpt(w, k0, E, h=1e-6):
    W0 = W(w, k0); e, V = np.linalg.eig(W0); sel = np.abs(wrap(np.angle(e) - E)) < 1e-6; m = int(sel.sum())
    if m == 0: return None
    Q, _ = np.linalg.qr(V[:, sel])
    G = []
    for j in range(3):
        dk = np.zeros(3); dk[j] = h; G.append((W(w, k0 + dk) - W(w, k0 - dk)) / (2 * h))
    hj = [-1j * np.exp(-1j * E) * Q.conj().T @ g @ Q for g in G]; hj = [(x + x.conj().T) / 2 for x in hj]
    tilt = max(abs(np.trace(x).real) / m for x in hj)
    sp = np.abs(np.array([np.linalg.eigvalsh(sum(d[j] * hj[j] for j in range(3))) for d in DIRS50]))
    return m, tilt, sp.min(), sp.max()
def verdict(r, v):
    m, tilt, smin, smax = r
    if smin < 1e-4: return 'flat'
    if tilt > 1e-4: return 'tilt'
    if smax - smin > 1e-4: return 'aniso'
    if abs(smin - v) > 1e-4: return 'iso-otherspeed'
    return 'ok'

# --------- sample
SAMPLE = []
for pk in PK:
    recs = load(D + pk)['recs']
    f8 = [r for r in recs if r['fermi'] and r['grid'] == 8]; f16 = [r for r in recs if r['fermi'] and r['grid'] == 16]
    sv = [r for r in recs if not r['fermi']]
    for pool, n in ((f8, 4), (f16, 2), (sv, 2)):
        for i in rng.choice(len(pool), size=min(n, len(pool)), replace=False): SAMPLE.append((pk, pool[i]))
print(f"sample: {len(SAMPLE)} records from {len(PK)} pickles")
okA = okF = okC = 0; nF = nC = 0; bad_lines = []
for pk, r in SAMPLE:
    w = build(r['sk'], r['names']); E = r['E']
    m, kind = level_kind(W(w, kst), E)
    a_ok = (kind == r['kind']); okA += a_ok
    if r['fermi']:
        nF += 1; wit, imag = fermi_witness(w, E)
        if wit is None:     # fall back: their grid
            g = (np.linspace(-np.pi, np.pi, 16, endpoint=False) + 0.0731); ks = np.array(list(itertools.product(g, repeat=3)))
            c0 = np.linalg.det(W(w, np.zeros(3))); rr = rfun(w, ks, E, c0).real; ok = rr.max() > 0 and rr.min() < 0
            line = f"own 10^3 grid: no sign change; 16^3 grid sign change: {ok}"
        else:
            kc, dist = wit; ok = dist < 1e-8 and imag < 1e-8
            line = f"crossing at k/pi={np.round(kc / np.pi, 4)} min|theta-E|={dist:.1e} Im/|r|={imag:.0e}"
        okF += ok
        if not (ok and a_ok): bad_lines.append((r['sk'], r['names'], E, kind, line))
        print(f"  FERMI {r['sk']} {r['names']} E={E:+.4f} {r['kind']}/{kind} grid{r['grid']}: {line}")
    else:
        nC += 1; v = abs(nS(r['sk'])) * np.sqrt(2) / 3
        b = r['bad'][0]; kb = np.array(b[0], float) * np.pi; res = my_dpt(w, kb, E)
        vd = verdict(res, v) if res else None
        ok = res is not None and res[0] == b[2] and vd == b[3]
        okC += ok
        if not (ok and a_ok): bad_lines.append((r['sk'], r['names'], E, b, res, vd))
        print(f"  SURV  {r['sk']} {r['names']} E={E:+.4f} {r['kind']}/{kind}: B26 first bad {b[1]} m={b[2]} {b[3]} (smin {b[4].get('smin')}, smax {b[4].get('smax')}); "
              f"own: m={res[0] if res else None} {vd} (smin {res[2]:.6f}, smax {res[3]:.6f}, tilt {res[1]:.1e})" if res else "own: no level")
check(f"k* level kind (D+/D-/D+D-) reproduced with own model for all {len(SAMPLE)} sampled records", okA == len(SAMPLE), f"{okA}/{len(SAMPLE)}")
check(f"Fermi-surface failures confirmed independently (own det-based r on an own 10^3 grid + bisection to an actual crossing)", okF == nF, f"{okF}/{nF}")
check(f"survivor failures confirmed: first defective node's multiplicity and defect type reproduced by own finite-difference DPT", okC == nC, f"{okC}/{nC}")
for x in bad_lines: print("   mismatch:", x)

# --------- best candidates
print("\nbest candidate S.o.Rt.o (L130, L332), E = 0:")
w = build(('S', 'o', 'Rt', 'o'), ('L130', 'L332')); v = np.sqrt(2) / 3
for E0 in (0.0,):
    lp = my_dpt(w, kst, E0); lm = my_dpt(w, -kst, E0)
    print(f"   +k*: m={lp[0]} tilt={lp[1]:.1e} smin={lp[2]:.6f} smax={lp[3]:.6f} -> {verdict(lp, v)} ; kind {level_kind(W(w, kst), E0)}")
    print(f"   -k*: m={lm[0]} tilt={lm[1]:.1e} smin={lm[2]:.6f} smax={lm[3]:.6f} -> {verdict(lm, v)}")
    check("best candidate: +k* is a 4-fold D+(+)D- isotropic untilted cone at sqrt2/3", lp[0] == 4 and verdict(lp, v) == 'ok' and level_kind(W(w, kst), E0)[1] == 'D+D-')
    check("best candidate FAILS: -k* level at E=0 is 8-fold and anisotropic (B26: smin 0.2357, smax 0.7071)",
          lm[0] == 8 and verdict(lm, v) == 'aniso' and abs(lm[2] - 0.235702) < 1e-3 and abs(lm[3] - 0.707107) < 1e-3)
    # own node search for further nodes at E
    f = lambda k: float(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(w, k))) - E0))))
    nodes = []
    for s in rng.uniform(-np.pi, np.pi, (40, 3)):
        rr = minimize(f, s, method='Nelder-Mead', options={'xatol': 1e-11, 'fatol': 1e-13, 'maxiter': 4000})
        if rr.fun < 1e-7:
            k = wrap(rr.x)
            if not any(np.linalg.norm(wrap(k - u_)) < 1e-4 for u_ in nodes): nodes.append(k)
    cls = collections.Counter()
    for k in nodes:
        res = my_dpt(w, k, E0, h=1e-7)
        if res: cls[(res[0], verdict(res, v))] += 1
    print(f"   own Nelder-Mead (40 random starts): {len(nodes)} distinct nodes at E=0, classes {dict(cls)}")
    check("own search finds additional defective (non-isotropic or tilted) nodes of the best candidate at E = 0",
          sum(n for (m_, vd), n in cls.items() if vd != 'ok') >= 1)
print("\nsecond candidate S.Rt.o (H20*L002), E = 0:")
w = build(('S', 'Rt', 'o'), ('H20*L002',))
cube = [np.array(s) * np.pi / 2 for s in itertools.product((1, -1), repeat=3)]
outs = []
for k in cube:
    res = my_dpt(w, k, 0.0)
    if res: outs.append((tuple(np.round(k / np.pi, 2)), res[0], verdict(res, v), round(res[2], 4), round(res[3], 4)))
for o in outs: print("   ", o)
check("second candidate: three 4-fold anisotropic cube doublets besides the isotropic 4-fold k* (B26: smin 0.2467, smax 0.6236)",
      sum(1 for o in outs if o[1] == 4 and o[2] == 'aniso') == 3 and sum(1 for o in outs if o[2] == 'ok') == 1)
print(f"\nTOTAL: PASS={P} FAIL={F}   [{time.time() - t0:.1f}s]")
