"""GEN-1 (b): one-loop Yukawa velocity kernel at Gamma for X2' (PREREG.md (b)).
Adapted from OBS-2 yuk_lv.py `kin` (same Brillouin-Wigner model, grid, finite differences), restricted to the Gamma
corner, with the mirror proxy m(k) = m0 + Delta*fmass(k):
   fmass = 'G'  : f_Gamma = (3 - sum cos k)/2  (X2' proxy; vanishes only at Gamma)
   fmass = 'NN' : f_NN = (1 - sum cos k)/2     (OBS-2's proxy; used only for control C1)
Vertex symbols: '0' on-site (g = 1), 'G' Gamma-selective flavour-universal g_G = (1 + sum cos k)/4 (= 1 at Gamma).
Variants sym/int/ext as in OBS-2.  Output: for each pair, B (per axis, d b_a/d p_a / v_tree) and S1;  dv = B + S1.
usage: python3 gen1_kernel.py N m0 Delta fmass [mH]"""
import numpy as np, sys, time, json
t0 = time.time()
SYMS = ['0', 'G']

def grid(N):
    u = -np.pi + (np.arange(N) + 0.5) * 2 * np.pi / N
    return u * np.abs(u) / np.pi, 2 * np.abs(u) / np.pi

def gsym(s, k):
    if s == '0':
        return np.ones_like(np.asarray(k[0], float))
    return (1 + np.cos(k[0]) + np.cos(k[1]) + np.cos(k[2])) / 4

def fm(name, k):
    c = np.cos(k[0]) + np.cos(k[1]) + np.cos(k[2])
    return (3 - c) / 2 if name == 'G' else (1 - c) / 2

def kin_gamma(N, m0, Delta, fmass, mH, dq=1e-3):
    pairs = [('0', '0'), ('0', 'G'), ('G', 'G')]
    qg, jac = grid(N)
    qy, qz = np.meshgrid(qg, qg, indexing='ij'); jyz = np.outer(jac, jac).ravel(); qy = qy.ravel(); qz = qz.ravel()
    e = np.zeros(3)
    pts = [('c', e)] + [(f'{a}{sg}', e + sg * dq * np.eye(3)[a]) for a in range(3) for sg in (+1, -1)]
    acc = {}
    for lab, p in pts:
        res = {v: {pr: np.zeros(4) for pr in pairs} for v in ('sym', 'int', 'ext')}
        gp = {s: float(gsym(s, [np.array(p[a]) for a in range(3)])) for s in SYMS}
        for ix in range(N):
            q = [np.full(qy.shape, qg[ix]), qy, qz]; w = jac[ix] * jyz / N**3
            k = [p[a] - q[a] for a in range(3)]
            Om = np.sqrt(sum(4 * np.sin(q[a] / 2)**2 for a in range(3)) + mH**2)
            s = [np.sin(k[a]) for a in range(3)]
            m = m0 + Delta * fm(fmass, k)
            E = np.sqrt(sum(x**2 for x in s) + m**2)
            Fb = [w * s[a] / (2 * E * Om * (E + Om)) for a in range(3)]
            Fz = -w / (2 * Om * (E + Om)**2)
            gk = {sy_: gsym(sy_, k) for sy_ in SYMS}
            Yv = {'sym': {sy_: (gk[sy_] + gp[sy_]) / 2 for sy_ in SYMS}, 'int': gk,
                  'ext': {sy_: np.full(qy.shape, gp[sy_]) for sy_ in SYMS}}
            for v in Yv:
                for (a_, b_) in pairs:
                    YY = Yv[v][a_] * Yv[v][b_]
                    r = res[v][(a_, b_)]
                    r[0] += (YY * Fb[0]).sum(); r[1] += (YY * Fb[1]).sum(); r[2] += (YY * Fb[2]).sum(); r[3] += (YY * Fz).sum()
        acc[lab] = res
    out = {}
    for v in ('sym', 'int', 'ext'):
        out[v] = {}
        for pr in pairs:
            D = np.zeros((3, 3))
            for b in range(3):
                D[:, b] = (acc[f'{b}{+1}'][v][pr][:3] - acc[f'{b}{-1}'][v][pr][:3]) / (2 * dq)
            Bd = np.diag(D).copy()   # v_tree = cos(0) = +1 on every axis at Gamma
            out[v]['%s%s' % pr] = {'B': Bd.tolist(), 'offdiag': float(np.abs(D - np.diag(np.diag(D))).max()),
                                   'S1': float(acc['c'][v][pr][3]), 'b_at_corner': acc['c'][v][pr][:3].tolist(),
                                   'dv': (Bd + acc['c'][v][pr][3]).tolist()}
    return out

if __name__ == '__main__':
    N = int(sys.argv[1]); m0 = float(sys.argv[2]); Delta = float(sys.argv[3]); fmass = sys.argv[4]
    mH = float(sys.argv[5]) if len(sys.argv) > 5 else m0
    print(f"N={N} m0={m0} Delta={Delta} fmass={fmass} mH={mH}", flush=True)
    r = kin_gamma(N, m0, Delta, fmass, mH)
    for v in r:
        for pr, d in r[v].items():
            print(f"  {v:3s} {pr}: B = {d['B'][0]:+.10e} (aniso {max(d['B'])-min(d['B']):.1e}, offdiag {d['offdiag']:.1e})"
                  f"  S1 = {d['S1']:+.10e}  dv = {d['dv'][0]:+.10e}", flush=True)
    fn = f"gk_N{N}_m{m0}_D{Delta}_{fmass}_mH{mH}.json"
    json.dump(r, open(fn, 'w'), indent=0)
    print(f"saved {fn} ({time.time()-t0:.0f}s)", flush=True)
