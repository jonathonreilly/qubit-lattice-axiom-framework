"""NT-1 T1: chiral-measure RP kernel on a W-matched pool (PREREG.md sections 3-6, follow-up F1).
usage: python3 nt1_kernel.py POOL.npz T [model] [delta]"""
import numpy as np, sys, time
from nt1_lib import *
from lat2d import Geom, nodes
import k2c_lib

fn, T = sys.argv[1], int(sys.argv[2]); model = sys.argv[3] if len(sys.argv) > 3 else '11112'
delta = float(sys.argv[4]) if len(sys.argv) > 4 else 0.6
G = Geom(2, T, False, -1); LK = Links(G); t00 = time.time(); SK = -1; k2c_lib.DELTA = delta
z = np.load(fn); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]; k = len(U)
print(f"# NT-1 kernel pool={fn} Lt={G.Lt} k={k} model={model} delta={delta} s_k={SK} transport=Richardson R(N)=(4W(2N)-W(N))/3", flush=True)


class ChiralR:
    def __init__(self, N):
        self.a = Chiral(LK, model, Ns=N, sk=SK); self.b = Chiral(LK, model, Ns=2 * N, sk=SK)

    def logrho(self, A):
        Wa, ga, oka = self.a.logrho(A); Wb, gb, okb = self.b.logrho(A)
        Wa = Wa + 2j * np.pi * np.round((Wb - Wa).imag / (2 * np.pi))
        return (4 * Wb - Wa) / 3, min(ga, gb), (oka and okb)


def entry(CH, ua, ub, n, chunk=16):
    ph, w = nodes(G, ua, ub, delta, n, 'hard')
    if len(w) == 0 or w.sum() <= 0: return {'chi': -np.inf + 0j, 'mod': -np.inf + 0j}, np.inf
    A = LK.joined(ua, ub, ph); ls = []; gm = np.inf
    for c in range(0, len(w), chunk):
        l, g, ok = CH.logrho(A[c:c+chunk])
        if not ok: raise RuntimeError('index != 0 on a ray')
        ls.append(l); gm = min(gm, g)
    l = np.concatenate(ls); out = {}
    for op, ll in (('chi', l), ('mod', l.real + 0j)):
        lm = ll.real.max(); out[op] = lm + np.log(np.sum(w * np.exp(ll - lm)) + 0j)
    return out, gm


def kern(CH, n, pairs=None):
    L = {op: np.full((k, k), -np.inf + 0j) for op in ('chi', 'mod')}; gm = np.inf
    todo = pairs if pairs is not None else [(a, b) for a in range(k) for b in range(k)]
    for (a, b) in todo:
        v, g = entry(CH, U[a], U[b], n); gm = min(gm, g)
        for op in v: L[op][a, b] = v[op]
    return L, gm


CH32 = ChiralR(8)   # F2: main transport R(8)
# --- per-pool gates with the main transport: G2 (gauge), G3 (Theta reality -> cphase) ---
rng = np.random.default_rng(5); gc = []
for (a, b) in [(0, 1), (3, 7), (k - 2, k - 1)]:
    ph, w = nodes(G, U[a], U[b], delta, 16, 'hard'); i = len(w) // 3; gc.append((a, b, ph[i:i+1]))
A = np.concatenate([LK.joined(U[a], U[b], ph) for (a, b, ph) in gc])
W1, g1, _ = CH32.logrho(A)
lower = (LK.site_t < G.T - 1).astype(float); viol = 0.0
for om in (np.repeat((0.3 * lower)[None], len(A), 0), rng.normal(0, 0.2, (len(A), LK.nsite))):
    Wg, _, _ = CH32.logrho(LK.gauge(A, om)); d = Wg - W1
    viol = max(viol, np.abs(d.real).max(), np.abs(np.angle(np.exp(1j * d.imag))).max())
Ar = np.concatenate([LK.joined(U[b], U[a], -ph) for (a, b, ph) in gc]); W2, _, _ = CH32.logrho(Ar)
c = W2 - np.conj(W1); cph = np.angle(np.exp(1j * c.imag)); spread = np.abs(np.angle(np.exp(1j * (cph - cph[0])))).max()
cphase = -0.5j * cph[0]
print(f"G2 (R8): max |d ln rho| under gauge transformations {viol:.2e} -> {'PASS' if viol < 1e-6 else 'FAIL'}; "
      f"G3: Theta phase c {cph[0]:+.8f} spread {spread:.2e}, |Re| {np.abs(c.real).max():.1e} -> {'PASS' if spread < 1e-6 else 'FAIL'}; min|H| {g1:.3f} [{time.time()-t00:.0f}s]", flush=True)

# --- kernels: chiral (chi), modulus-only (mod) at n = 16, 32; subset n = 48 and transport R(64) ---
res = {}
Llo, glo = kern(CH32, 16); print(f"LOW done min|H| {glo:.3f} [{time.time()-t00:.0f}s]", flush=True)
Lhi, ghi = kern(CH32, 32); print(f"HIGH done min|H| {ghi:.3f} [{time.time()-t00:.0f}s]", flush=True)
rs = np.random.default_rng(99); sub = set()
while len(sub) < min(24, k * (k - 1)):
    a_, b_ = int(rs.integers(k)), int(rs.integers(k))
    if a_ != b_: sub.add((a_, b_))
sub = sorted(sub); diag = [(i, i) for i in range(k)]
L48, g48 = kern(CH32, 48, sub + diag); print(f"n=48 subset done [{time.time()-t00:.0f}s]", flush=True)
CH64 = ChiralR(16); LPT, gpt = kern(CH64, 32, sub + diag); print(f"R16 subset done [{time.time()-t00:.0f}s]", flush=True)
gmin = min(glo, ghi, g48, gpt)


# F3: overall constant of the Theta-real measure = +-exp(cphase); the sign is fixed by K(a, a) > 0 (physical Z > 0).
dph = np.angle(np.exp(1j * (Lhi['chi'].diagonal().imag + cphase.imag)))
print(f"chi diagonal phases after cphase: min {dph.min():+.3e} max {dph.max():+.3e} (all |.| > pi/2: {np.all(np.abs(dph) > np.pi/2)}; all < pi/2: {np.all(np.abs(dph) < np.pi/2)})")
sgn = 1j * np.pi if np.all(np.abs(dph) > np.pi / 2) else 0.0
CP = {'chi': cphase + sgn, 'mod': 0.0}


def zn(L, op):
    Z, dim, h = normalize_raw(L + CP[op]); return Z, dim, h


for op in ('chi', 'mod'):
    Zl, _, _ = zn(Llo[op], op); Zh, dim, h = zn(Lhi[op], op); Z48, _, _ = zn(L48[op], op); Zpt, _, _ = zn(LPT[op], op)
    q = np.abs(Zh - Zl).max(); q3 = max(abs(Z48[a, b] - Zh[a, b]) for (a, b) in sub)
    qpt = max(abs(Zpt[a, b] - Zh[a, b]) for (a, b) in sub)
    E = k * max(q, q3, qpt, h) + 1e-13
    ev = np.linalg.eigvalsh(0.5 * (Zh + Zh.conj().T)); a_, b_ = ev[0], ev[-1]
    res[op] = (a_, E)
    print(f"FINAL {op:4s} k={k}: lam_min {a_:+.4e} min/max {a_/b_:+.4e} | q {q:.1e} q3 {q3:.1e} qPT {qpt:.1e} herm-defect h {h:.1e} max|Im ln diag| {dim:.1e}"
          f" | E {E:.1e} | certified-negative {a_ < -10*E} | PSD-within-error {a_ > -10*E} | lowest {np.array2string(ev[:4], precision=3)} max {b_:.3f}", flush=True)
    if op == 'chi':
        offim = np.abs(Zh.imag).max(); print(f"   chi: max |Im Zn| {offim:.3e} (phase content of the chiral kernel)")
        np.save(fn.replace('.npz', f'_NT1_{model}_Zchi.npy'), Zh)

# --- vector-like references: massive overlap O (K2c power reference), massless vec0, Wilson, PG ---
for op in ('O', 'W', 'PG'):
    Zl, gl = k2c_lib.full_kernel(G, U, 16, None, op, 'hard'); Zh, gh = k2c_lib.full_kernel(G, U, 32, None, op, 'hard')
    q = np.abs(Zh - Zl).max(); E = k * q + 1e-13; ev = np.linalg.eigvalsh(Zh)
    res[op] = (ev[0], E)
    print(f"REF   {op:4s} k={k}: lam_min {ev[0]:+.4e} min/max {ev[0]/ev[-1]:+.4e} q {q:.1e} E {E:.1e} | certified-negative {ev[0] < -10*E} | PSD-within-error {ev[0] > -10*E}", flush=True)
Lv = np.full((k, k), -np.inf + 0j); Lv16 = np.full((k, k), -np.inf + 0j)
for a in range(k):
    for b in range(a, k):
        for (nn, LL) in ((32, Lv), (16, Lv16)):
            v, _ = entry_chi(LK, None, U[a], U[b], nn, delta, op='vec0'); LL[a, b] = v; LL[b, a] = np.conj(v)
Zv, _, _ = normalize_raw(Lv); Zv16, _, _ = normalize_raw(Lv16); ev = np.linalg.eigvalsh(0.5 * (Zv + Zv.conj().T)); q = np.abs(Zv - Zv16).max(); E = k * q + 1e-13
res['vec0'] = (ev[0], E)
print(f"REF   vec0 k={k}: lam_min {ev[0]:+.4e} min/max {ev[0]/ev[-1]:+.4e} q {q:.1e} E {E:.1e} | certified-negative {ev[0] < -10*E} (massless vector overlap)", flush=True)

clean = viol < 1e-6 and spread < 1e-6 and gmin > 0.1
a_, E = res['chi']
print(f"SUMMARY {fn} model={model} delta={delta}: gates-clean {clean} (G2 {viol:.1e}, G3 {spread:.1e}, min|H| {gmin:.3f}) | chi lam_min {a_:+.3e} E {E:.1e} cert-neg {a_ < -10*E}"
      f" PSD {a_ > -10*E} | mod lam_min {res['mod'][0]:+.3e} | O(ref) {res['O'][0]:+.3e} cert-neg {res['O'][0] < -10*res['O'][1]} | vec0 {res['vec0'][0]:+.3e} | W {res['W'][0]:+.1e} PG {res['PG'][0]:+.1e}")
print(f"done [{time.time()-t00:.0f}s]")
