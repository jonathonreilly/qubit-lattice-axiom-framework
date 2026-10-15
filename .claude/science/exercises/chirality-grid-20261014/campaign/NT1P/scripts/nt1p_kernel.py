"""NT-1' RP kernel on a W-matched pool (PREREG section 6): chiral 11112 (all ordered pairs, no Hermitian fill), modulus,
vector O (m = 0.05, power reference), massless vector overlap, Wilson, PG.  Lx = 4, open time, hard delta = 0.6.
usage: python3 nt1p_kernel.py POOL.npz T [lo hi third] [nsub]"""
import numpy as np, sys, time
from nt1p_lib import *
from lat2d import Geom, nodes
import k2c_lib

fn, T = sys.argv[1], int(sys.argv[2])
NLO, NHI, N3 = (int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (3, 4, 5)
NSUB = int(sys.argv[6]) if len(sys.argv) > 6 else 12
delta = 0.6; S = Strip(4, T); G = Geom(4, T, False, -1); SK = -1; t00 = time.time(); CH = 32 if 8 * T <= 32 else 12
z = np.load(fn); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]; k = len(U)
M8 = Measure(S, '11112', Ns=8, sk=SK); M16 = Measure(S, '11112', Ns=16, sk=SK)
print(f"# NT-1' kernel pool={fn} Lx=4 Lt={2*T} k={k} model=11112 delta={delta} s_k={SK} quad lo/hi/third = {NLO}/{NHI}/{N3} "
      f"transport main R(4) (Ns 4+8), check R(8); kbb Simpson 8/16", flush=True)
GM = {'gmin': np.inf, 'idx': True, 'sumA': 0.0, 'maxW': 0.0}
PH = {'within': 0.0}


def entry(Mx, a, b, n):
    ph, w = nodes(G, U[a], U[b], delta, n, 'hard')
    if len(w) == 0 or w.sum() <= 0: return {'chi': -np.inf + 0j, 'mod': -np.inf + 0j}
    A = S.joined(U[a], U[b], ph); ls = []
    for c in range(0, len(A), CH):
        W, r, Ac = Mx.logrho(A[c:c+CH], parts=True); ls.append(W)
        GM['gmin'] = min(GM['gmin'], r['gmin']); GM['idx'] &= r['idx_ok']; GM['sumA'] = max(GM['sumA'], r['sumA'])
        GM['maxW'] = max(GM['maxW'], np.abs(S.FW(Ac)[1]).max())
    l = np.concatenate(ls); out = {}
    phs = np.angle(np.exp(1j * (l.imag - l.imag[np.argmax(w)]))); PH['within'] = max(PH['within'], np.abs(phs).max())
    for op, ll in (('chi', l), ('mod', l.real + 0j)):
        lm = ll.real.max(); out[op] = lm + np.log(np.sum(w * np.exp(ll - lm)) + 0j)
    return out


def kern(Mx, n, pairs):
    L = {op: np.full((k, k), -np.inf + 0j) for op in ('chi', 'mod')}
    for (a, b) in pairs:
        v = entry(Mx, a, b, n)
        for op in v: L[op][a, b] = v[op]
    return L


allp = [(a, b) for a in range(k) for b in range(k)]
Llo = kern(M8, NLO, allp); print(f"LOW (n={NLO}) done [{time.time()-t00:.0f}s]", flush=True)
Lhi = kern(M8, NHI, allp); print(f"HIGH (n={NHI}) done [{time.time()-t00:.0f}s]", flush=True)
rs = np.random.default_rng(99); sub = set()
while len(sub) < min(NSUB, k * (k - 1)):
    a_, b_ = int(rs.integers(k)), int(rs.integers(k))
    if a_ != b_: sub.add((a_, b_))
sub = sorted(sub); diag = [(i, i) for i in range(k)]
L3 = kern(M8, N3, sub + diag); print(f"third level (n={N3}) subset done [{time.time()-t00:.0f}s]", flush=True)
LPT = kern(M16, NHI, sub + diag); print(f"transport R(8) subset done [{time.time()-t00:.0f}s]", flush=True)

# Theta constant (gate d) from the HIGH kernel itself: K(b,a) = e^{c} conj K(a,b) -> c from the diagonal: K(a,a) = e^{c} conj K(a,a)
d = Lhi['chi'].diagonal(); cth = np.angle(np.exp(1j * 2 * d.imag)); cph0 = cth[0]
print(f"Theta constant from diagonals: 2 Im ln K(a,a) mod 2pi = {cph0:+.8f} (spread {np.abs(np.angle(np.exp(1j*(cth - cph0)))).max():.1e}); gate (d) value -7.962629 mod 2pi = {np.angle(np.exp(-7.962629j)):+.8f}")
cphase = -0.5j * cph0
dph = np.angle(np.exp(1j * (d.imag + cphase.imag)))
print(f"chi diagonal phases after cphase: min {dph.min():+.3e} max {dph.max():+.3e} (all |.| > pi/2: {np.all(np.abs(dph) > np.pi/2)}; all < pi/2: {np.all(np.abs(dph) < np.pi/2)})")
sgn = 1j * np.pi if np.all(np.abs(dph) > np.pi / 2) else 0.0
CP = {'chi': cphase + sgn, 'mod': 0.0}


def zn(L, op):
    Z, dim, h = normalize_raw(L + CP[op]); return Z, dim, h


def normalize_raw(L):
    dd = L.diagonal(); dim = np.abs(np.angle(np.exp(1j * dd.imag))).max(); dr = dd.real
    with np.errstate(invalid='ignore', over='ignore', under='ignore'):
        Z = np.where(np.isfinite(L.real), np.exp(L - 0.5 * (dr[:, None] + dr[None, :])), 0)
    return Z, dim, np.abs(Z - Z.conj().T).max()


res = {}; Zs = {}
for op in ('chi', 'mod'):
    Zl, _, _ = zn(Llo[op], op); Zh, dim, h = zn(Lhi[op], op); Z3, _, _ = zn(L3[op], op); Zp, _, _ = zn(LPT[op], op)
    q = np.abs(Zh - Zl).max(); q3 = max(abs(Z3[a, b] - Zh[a, b]) for (a, b) in sub); qpt = max(abs(Zp[a, b] - Zh[a, b]) for (a, b) in sub)
    E = k * max(q, q3, qpt, h) + 1e-13
    ev = np.linalg.eigvalsh(0.5 * (Zh + Zh.conj().T)); res[op] = (ev[0], E); Zs[op] = Zh
    print(f"FINAL {op:4s} k={k}: lam_min {ev[0]:+.4e} min/max {ev[0]/ev[-1]:+.4e} | q {q:.1e} q3 {q3:.1e} qPT {qpt:.1e} h {h:.1e} max|Im ln diag| {dim:.1e}"
          f" | E {E:.1e} | conv-negative {ev[0] < -10*E} | PSD-within-error {ev[0] > -10*E} | lowest {np.array2string(ev[:3], precision=3)} max {ev[-1]:.3f}", flush=True)
np.save(fn.replace('.npz', '_NT1P_Zchi.npy'), Zs['chi']); np.save(fn.replace('.npz', '_NT1P_Zmod.npy'), Zs['mod'])
np.savez(fn.replace('.npz', '_NT1P_logK.npz'), lo=Llo['chi'], hi=Lhi['chi'], third=L3['chi'], pt=LPT['chi'], cphase=cphase, sgn=sgn)
Zc, Zm = Zs['chi'], Zs['mod']
print(f"PHASE: max|Im Zn_chi| {np.abs(Zc.imag).max():.3e}; max|Zn_chi - Zn_mod| {np.abs(Zc - Zm).max():.3e}; max phase spread over nodes within an entry {PH['within']:.3e} rad; "
      f"arg Zn_chi off-diagonal range [{np.angle(Zc[~np.eye(k, dtype=bool)]).min():+.3e}, {np.angle(Zc[~np.eye(k, dtype=bool)]).max():+.3e}]", flush=True)
print(f"GATES on all kernel nodes: G5 min|eig H_W(U^e)| {GM['gmin']:.3f}; G6 index 0 {GM['idx']}; G7 max|sum Abar| {GM['sumA']:.1e}; max|W_t| (canonical) {GM['maxW']:.3f}")
# vector-like references on the same pool and quadrature levels
for op in ('O', 'W', 'PG'):
    Zl, _ = k2c_lib.full_kernel(G, U, NLO, None, op, 'hard'); Zh, _ = k2c_lib.full_kernel(G, U, NHI, None, op, 'hard')
    q = np.abs(Zh - Zl).max(); E = k * q + 1e-13; ev = np.linalg.eigvalsh(Zh); res[op] = (ev[0], E)
    print(f"REF   {op:4s} k={k}: lam_min {ev[0]:+.4e} min/max {ev[0]/ev[-1]:+.4e} q {q:.1e} E {E:.1e} | conv-negative {ev[0] < -10*E} | PSD-within-error {ev[0] > -10*E}", flush=True)
for (nm, mm) in (('vec0', 0.0),):
    LL = {}
    for nn in (NLO, NHI):
        Lv = np.full((k, k), -np.inf + 0j)
        for a in range(k):
            for b in range(a, k):
                ph, w = nodes(G, U[a], U[b], delta, nn, 'hard'); l, _ = vec_logdet(S, S.joined(U[a], U[b], ph), m=mm)
                lm = l.real.max(); v = lm + np.log(np.sum(w * np.exp(l - lm)) + 0j); Lv[a, b] = v; Lv[b, a] = np.conj(v)
        LL[nn] = normalize_raw(Lv)[0]
    ev = np.linalg.eigvalsh(0.5 * (LL[NHI] + LL[NHI].conj().T)); q = np.abs(LL[NHI] - LL[NLO]).max(); E = k * q + 1e-13; res[nm] = (ev[0], E)
    print(f"REF   {nm} k={k}: lam_min {ev[0]:+.4e} min/max {ev[0]/ev[-1]:+.4e} q {q:.1e} E {E:.1e} | conv-negative {ev[0] < -10*E} (massless vector overlap)", flush=True)
a_, E = res['chi']
print(f"SUMMARY {fn}: chi lam_min {a_:+.4e} E {E:.1e} conv-neg {a_ < -10*E} PSD {a_ > -10*E} | mod {res['mod'][0]:+.4e} | O {res['O'][0]:+.4e} "
      f"conv-neg {res['O'][0] < -10*res['O'][1]} | vec0 {res['vec0'][0]:+.4e} | W {res['W'][0]:+.1e} PG {res['PG'][0]:+.1e} | chi/O {a_/res['O'][0]:.2f}")
print(f"done [{time.time()-t00:.0f}s]")
