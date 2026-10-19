"""T-F3 task 4-5: leakage of G-allowed cross-sector operators into M_l, M_nu; Delta distribution with
theta13 refit; tuning needed for median Delta < 0.003.  See ../PREREG_NOTES.md.
usage: python3 t4_leak.py [ndraw] [spectrum: NO|NO0|IO] [seed] [nwords: int | count]"""
import sys, numpy as np
from scipy.optimize import brentq
from t4_core import *
MAIN = __name__ == '__main__'
argv = sys.argv if MAIN else ['x']
ND = int(argv[1]) if len(argv) > 1 else 1000
SPEC = argv[2] if len(argv) > 2 else 'NO'
rng = np.random.default_rng(int(argv[3]) if len(argv) > 3 else 21)
LOOP = 1 / (16 * np.pi ** 2)
ORDER = 'IO' if SPEC == 'IO' else 'NO'
NW = argv[4] if len(argv) > 4 else '8'
NWL, NWN = (414, 342) if NW == 'count' else (int(NW), int(NW))   # 414/342 = dims of G-equivariant trilinear maps (t4_count.out)
def coef(n):
    return 10 ** rng.uniform(np.log10(1 / 3), np.log10(3), n) * np.exp(1j * rng.uniform(0, 2 * np.pi, n))
def unit(X):
    n = np.linalg.norm(X); return X / n if n > 1e-14 else X * 0
WORDS = ['LNN', 'NLN', 'NNL', 'LtNN', 'NLtN', 'HAD', 'PRJ']
def word(kind, L, N1, N2, r):
    if kind == 'LNN': return L @ N1 @ N2
    if kind == 'NLN': return N1 @ L @ N2
    if kind == 'NNL': return N1 @ N2 @ L
    if kind == 'LtNN': return L.T @ N1 @ N2
    if kind == 'NLtN': return N1 @ L.T @ N2
    if kind == 'HAD': return L * N1 * N2                        # triple Hadamard: B3-covariant (signed permutations)
    return PROJ[r](L @ N1 + N2 @ L)
class Ops:
    """one random draw of every leading cross operator (coefficients and word choices frozen)."""
    def __init__(self, scale_loop=True, nwl=None, nwn=None):
        nwl = NWL if nwl is None else nwl; nwn = NWN if nwn is None else nwn
        s = LOOP if scale_loop else 1.0
        self.cL1_l = s * coef(6); self.cL1_n = s * coef(4)           # nu comps (A1,E,3M x Re,Im) -> M_l ; l comps (A1,3M x Re,Im) -> M_nu
        self.w_l = [(rng.choice(WORDS), rng.integers(0, 6), rng.integers(0, 6), rng.integers(0, 6), rng.choice(list(PROJ))) for _ in range(nwl)]
        self.w_n = [(rng.choice(WORDS), rng.integers(0, 6), rng.integers(0, 6), rng.integers(0, 6), rng.choice(MAJ_IRREPS)) for _ in range(nwn)]
        self.cL2_l = s * coef(nwl); self.cL2_n = s * coef(nwn)
        self.pi = LOOP * 10 ** rng.uniform(np.log10(1 / 3), np.log10(3), 3) * np.sign(rng.normal(size=3))
        h = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); h = (h + h.conj().T) / 2
        self.q0 = rng.normal(); self.h = h
def comps_full(M, irreps):
    Z = M / np.linalg.norm(M); out = []
    for r in irreps:
        K = PROJ[r](Z); out += [K.real, K.imag]
    return out
def leak(Ml, Mn, ops, classes):
    dl = np.zeros((3, 3), complex); dn = np.zeros((3, 3), complex)
    nl, nn = np.linalg.norm(Ml), np.linalg.norm(Mn)
    Cn = comps_full(Mn, ['A1', 'E', '3M'])                       # 6 real comps of phi_nu
    Cl = comps_full(Ml, ['A1', '3M', "3M'"])                     # 6 real comps of phi_l
    if 'L1' in classes:
        dl += nl * sum(c * unit(K) for c, K in zip(ops.cL1_l, Cn))
        dn += nn * sum(c * unit(K) for c, K in zip(ops.cL1_n, Cl[:4]))   # A1, 3M only (3M' cannot enter a Majorana mass)
    if 'L2' in classes:
        for c, (k, i, j1, j2, r) in zip(ops.cL2_l, ops.w_l):
            dl += nl * c * unit(word(k, Cl[i], Cn[j1], Cn[j2], r))
        for c, (k, i, j1, j2, r) in zip(ops.cL2_n, ops.w_n):
            W_ = word(k, Cn[i], Cl[j1], Cl[j2], r); dn += nn * c * unit((W_ + W_.T) / 2)
    if 'W' in classes:
        P = FOUR @ np.diag(ops.pi) @ FOUR.conj().T                 # generic C3-invariant Hermitian
        dn += P.T @ Mn + Mn @ P
        Q = ops.q0 * np.outer(V1, V1) + np.column_stack([W1, W2]) @ ops.h @ np.column_stack([W1, W2]).T
        dl += Ml @ (LOOP * Q)                                       # generic g_nu-invariant Hermitian
    if 'PHYS' in classes:
        v = 174.1; t = np.log(1.22e19 / 91.19) / (16 * np.pi ** 2)
        P = -1.5 * t * (Ml.conj().T @ Ml) / v ** 2
        dn += P.T @ Mn + Mn @ P
    return dl, dn
def run_draw(classes, ops, cfg, tscale=1.0):
    swap, ph, mlight, phi, majph = cfg
    Ml = Ml0(ph, swap); masses = nu_masses(mlight, ORDER)
    def state(th):
        Mn = Mnu0(th, phi, masses, majph)
        dl, dn = leak(Ml, Mn, ops, classes)
        return obs(pmns(Ml + tscale * dl, Mn + tscale * dn)[0], ORDER)
    o_unrefit = state(THETA0)
    f = lambda th: state(th)['s13'] - S13_OBS
    try:
        a, b = 0.9, np.pi / 2
        if f(a) * f(b) > 0: raise ValueError
        th = brentq(f, a, b, xtol=1e-12); o = state(th); o['refit'] = True
    except ValueError:
        o = o_unrefit; o['refit'] = False
    o['s13_unrefit'] = o_unrefit['s13']
    return o
def config():
    while True:
        swap = rng.random() < 0.5; ph = rng.uniform(0, 2 * np.pi, 3); phi = rng.uniform(0, 2 * np.pi); majph = rng.uniform(0, 2 * np.pi, 3)
        mlight = 1e-4 if SPEC == 'NO0' else 10 ** rng.uniform(-4, -2)
        U = pmns(Ml0(ph, swap), Mnu0(THETA0, phi, nu_masses(mlight, ORDER), majph))[0]
        o = obs(U, ORDER)
        if 0.435 <= o['s23'] <= 0.585 and o['Delta'] < 1e-10: return (swap, ph, mlight, phi, majph)
CLASSES = {'L1-loop': (['L1'], True), 'L2-loop': (['L2'], True), 'W-loop': (['W'], True),
           'ALL-loop': (['L1', 'L2', 'W'], True), 'TREE': (['L1', 'L2'], False), 'PHYS': (['PHYS'], True)}
def summarise(name, res):
    D = np.array([r['Delta'] for r in res]); dm = np.array([r['dmu1'] for r in res]); dt = np.array([r['dtau1'] for r in res])
    ds13 = np.array([abs(r['s13_unrefit'] - S13_OBS) for r in res]); rf = np.mean([r['refit'] for r in res])
    print(f"{name:12s} N={len(res)} refit {rf:.2f} | Delta median {np.median(D):.3g} [16%,84%: {np.percentile(D,16):.2g}, {np.percentile(D,84):.2g}] "
          f"P(D<0.003) {np.mean(D<0.003):.2f} P(D>0.01) {np.mean(D>0.01):.2f} | |dU_mu1| med {np.median(np.abs(dm)):.3g} |dU_tau1| med {np.median(np.abs(dt)):.3g} "
          f"(signed med {np.median(dm):+.2g},{np.median(dt):+.2g}) | |s13-0.022| before refit med {np.median(ds13):.2g}")
    return np.median(D)
if MAIN:
    print(f"spectrum {SPEC}, draws {ND}, loop factor {LOOP:.4g}, trilinear words per draw: l {NWL}, nu {NWN}")
    cfgs = [config() for _ in range(ND)]
    opsL = [Ops(True) for _ in range(ND)]; opsT = [Ops(False) for _ in range(ND)]
    med = {}
    for name, (cls, loop) in CLASSES.items():
        ops = opsL if loop else opsT
        res = [run_draw(cls, ops[i], cfgs[i]) for i in range(ND)]
        med[name] = summarise(name, res)
    # sector split of ALL-loop: leak into M_l only vs into M_nu only
    def split(side):
        out = []
        for i in range(ND):
            swap, ph, mlight, phi, majph = cfgs[i]; ops = opsL[i]
            Ml = Ml0(ph, swap); Mn = Mnu0(THETA0, phi, nu_masses(mlight, ORDER), majph)
            dl, dn = leak(Ml, Mn, ops, ['L1', 'L2', 'W'])
            if side == 'l': dn = 0 * dn
            else: dl = 0 * dl
            out.append(obs(pmns(Ml + dl, Mn + dn)[0], ORDER)['Delta'])
        return np.median(out)
    print(f"ALL-loop without refit: leak into M_l only -> median Delta {split('l'):.3g}; into M_nu only -> {split('n'):.3g}")
    # tuning: overall factor t on the natural coefficients giving median Delta = 0.003
    print("\ntuning t_req (median Delta = 0.003 when every leakage coefficient is multiplied by t):")
    for name in ['ALL-loop', 'L1-loop', 'L2-loop', 'W-loop', 'TREE']:
        cls, loop = CLASSES[name]; ops = opsL if loop else opsT
        t = 0.003 / med[name]
        for it in range(3):
            m = np.median([run_draw(cls, ops[i], cfgs[i], t)['Delta'] for i in range(min(ND, 400))]); t *= 0.003 / m
        m = np.median([run_draw(cls, ops[i], cfgs[i], t)['Delta'] for i in range(min(ND, 400))])
        print(f"  {name:9s}: t_req = {t:.3g}  (check median at t_req: {m:.4f}); relative to O(1) tree size: {t*(LOOP if loop else 1):.3g}")
