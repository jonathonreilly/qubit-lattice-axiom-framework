"""NT-1'' B2a (PREREG section 4): admissibility of the non-contractible Wilson-line loop A(tau) = A_c + tau (2 pi/Lx) 1_x on the
open-time RP strip. For charges 1 and 2: min_tau min|eig H_W(e A(tau))|, index changes, and the admissible tau-set.
usage: python3 nt1pp_b2a.py Lx [ngrid]"""
import sys, time
import numpy as np
from nt1pp_common import *
from lat2d import Geom, nodes

Lx = int(sys.argv[1]); ng = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
T = 4; S = Strip(Lx, T); n = S.N // 2; one_x = np.zeros(S.nl); one_x[S.xl.reshape(-1)] = 2 * np.pi / Lx
t00 = time.time(); print(f"# NT-1'' B2a Lx={Lx} Lt={2*T} N={S.N}; loop A_c + tau*(2pi/Lx)*1_x, grid {ng}", flush=True)
bgs = [('F=0,W=0', np.zeros((1, S.nl)))]
rng = np.random.default_rng(4401)
for i in range(10): bgs.append((f'rand{i}', gen_config(S, rng, center=False)))
if Lx == 4:
    G = Geom(4, 4, False, -1); z = np.load('pool_NT1P_PB_random_Lx4_Lt8_seed2504.npz')
    U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]; r7 = np.random.default_rng(7)
    for (a, b) in [(0, 1), (2, 5), (7, 9)]:
        ph, w = nodes(G, U[a], U[b], 0.6, 3, 'hard'); idx = r7.choice(len(w), 2, replace=False)
        J = S.canon(S.joined(U[a], U[b], ph[idx]))
        for k in range(2): bgs.append((f'PB({a},{b})n{k}', J[k:k + 1]))


def spec(A, e):
    w = np.linalg.eigvalsh(S.H(e * A)); return np.abs(w).min(1), (w > 0).sum(1) - n


def gmin_at(A0, e, tau): return spec(A0 + tau * one_x[None], e)[0][0]


taus = np.linspace(0, 1, ng + 1)[:-1]
nadm = 0; rows = []
for name, A0 in bgs:
    F, W = S.FW(A0); Wb, Wt = W[0, 0], W[0, -1]
    line = f"{name:12s} Wbot {Wb:+.3f} Wtop {Wt:+.3f} max|F| {np.abs(F).max():.3f} |"
    good = np.ones(ng, bool); allok = True
    for e in (1, 2):
        g = np.zeros(ng); ix = np.zeros(ng, int)
        for c in range(0, ng, 200):
            Ab = A0 + taus[c:c + 200, None] * one_x[None]; g[c:c + 200], ix[c:c + 200] = spec(Ab, e)
        j = int(np.argmin(g)); a, b = taus[j] - 1.0 / ng, taus[j] + 1.0 / ng; phi = (np.sqrt(5) - 1) / 2
        x1, x2 = b - phi * (b - a), a + phi * (b - a); f1, f2 = gmin_at(A0, e, x1), gmin_at(A0, e, x2)
        for _ in range(40):
            if f1 < f2: b, x2, f2 = x2, x1, f1; x1 = b - phi * (b - a); f1 = gmin_at(A0, e, x1)
            else: a, x1, f1 = x1, x2, f2; x2 = a + phi * (b - a); f2 = gmin_at(A0, e, x2)
        gref = min(f1, f2, g.min()); tref = x1 if f1 < f2 else x2
        # all local minima below 0.1 (crossings)
        locmin = [i for i in range(ng) if g[i] < 0.1 and g[i] <= g[i - 1] and g[i] <= g[(i + 1) % ng]]
        idx_change = bool(np.any(ix != 0))
        good &= (g >= 0.1) & (ix == 0); allok &= (gref >= 0.1) and not idx_change
        line += f" e={e}: min gap {gref:.2e} at tau {tref:.4f} (W={W[0, T-1]+2*np.pi*tref:+.3f}); minima<0.1 at tau " + \
                ",".join(f"{taus[i]:.3f}" for i in locmin[:6]) + f"; index change {idx_change}, idx range [{ix.min()},{ix.max()}] |"
    # admissible tau intervals (cyclic)
    if good.all(): nint = 0; L = 1.0
    else:
        st = [i for i in range(ng) if good[i] and not good[i - 1]]; nint = len(st); L = good.mean()
    adm = bool(allok and good.all()); nadm += adm
    line += f" LOOP ADMISSIBLE {adm}; admissible tau-set: {nint} interval(s), total length {L:.3f}"
    print(line, flush=True)
print(f"SUMMARY Lx={Lx}: {nadm} of {len(bgs)} sampled winding loops admissible (gap >= 0.1 and index 0 for e = 1, 2 at every tau) [{time.time()-t00:.0f}s]")
