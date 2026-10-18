"""NT-1 T2: W-matched greedy search on the chiral kernel (K2c wsearch rule; objective lam_min of the Hermitian part, LOW n = 16,
transport R(4) per F2). Hermitian fill is used for the OBJECTIVE only (Theta reality checked by G3); the saved pool is then evaluated
in full (all ordered pairs, R(32), n = 16/32/48) by nt1_kernel.py.
usage: python3 nt1_search.py T K SEED [model] [delta] [margin]"""
import numpy as np, sys, time
from nt1_lib import *
from lat2d import Geom, nodes, rand_half, wrap
from k2b_lib import perturb, admissible

T, K, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
model = sys.argv[4] if len(sys.argv) > 4 else '11112'; delta = float(sys.argv[5]) if len(sys.argv) > 5 else 0.6
DB = float(sys.argv[6]) if len(sys.argv) > 6 else 0.55; s0 = 0.25 * delta / 0.6
G = Geom(2, T, False, -1); LK = Links(G); rng = np.random.default_rng(seed); t00 = time.time(); SK = -1
print(f"# NT-1 T2 wsearch model={model} open Lt={G.Lt} K={K} seed={seed} delta={delta} margin {DB} link sigma {s0:.3f}", flush=True)
CA, CB = Chiral(LK, model, Ns=4, sk=SK), Chiral(LK, model, Ns=8, sk=SK)   # F2: objective R(4)


def logrho(A):
    Wa, ga, oka = CA.logrho(A); Wb, gb, okb = CB.logrho(A)
    Wa = Wa + 2j * np.pi * np.round((Wb - Wa).imag / (2 * np.pi))
    if not (oka and okb): raise RuntimeError('index')
    return (4 * Wb - Wa) / 3, min(ga, gb)


# Theta phase constant (G3 convention) from one joined config
u0 = rand_half(rng, G, s0, DB)
def match(u): return {'x': u['x'] - 0.5 * u['x'][0].sum(), 't': u['t'].copy()}
def rand_m(): return match(rand_half(rng, G, s0, DB))
def pert_m(u, sig):
    v = perturb(rng, G, u, sig, DB)
    return None if v is None else match(v)
ua, ub = rand_m(), rand_m(); ph, w = nodes(G, ua, ub, delta, 16, 'hard'); i = len(w) // 3
W1, _ = logrho(LK.joined(ua, ub, ph[i:i+1])); W2, _ = logrho(LK.joined(ub, ua, -ph[i:i+1]))
cphase = -0.5j * np.angle(np.exp(1j * (W2 - np.conj(W1)).imag))[0]
# F3: global sign fixed by K(u, u) > 0 (checked on the first diagonal entry; every later diagonal is checked too)
_ph, _w = nodes(G, ua, ua, delta, 16, 'hard'); _l, _ = logrho(LK.joined(ua, ua, _ph)); _lm = _l.real.max()
_d = np.angle(np.sum(_w * np.exp(_l - _lm)) * np.exp(cphase))
if abs(_d) > np.pi / 2: cphase = cphase + 1j * np.pi
print(f"cphase {cphase.imag:+.8f}", flush=True)


def ent(ua, ub):
    ph, w = nodes(G, ua, ub, delta, 16, 'hard')
    if len(w) == 0 or w.sum() <= 0: return -np.inf + 0j, np.inf
    l, g = logrho(LK.joined(ua, ub, ph)); lm = l.real.max()
    return lm + np.log(np.sum(w * np.exp(l - lm)) + 0j) + cphase, g


def zn(L):
    d = L.diagonal().real
    with np.errstate(invalid='ignore', over='ignore', under='ignore'):
        Z = np.where(np.isfinite(L.real), np.exp(L - 0.5 * (d[:, None] + d[None, :])), 0)
    return 0.5 * (Z + Z.conj().T)


Upool = []; L = np.zeros((0, 0), complex); gmin = np.inf
def bordered(u):
    kk = len(Upool); r = [ent(a, u) for a in Upool]; dd = ent(u, u)
    B = np.full((kk + 1, kk + 1), -np.inf + 0j); B[:kk, :kk] = L
    for j, (v, g) in enumerate(r): B[j, kk] = v; B[kk, j] = np.conj(v)
    if abs(np.angle(np.exp(1j * dd[0].imag))) > 1e-6: print(f"WARNING diagonal phase {dd[0].imag:+.3e}", flush=True)
    B[kk, kk] = dd[0].real
    return B, min([dd[1]] + [g for (_, g) in r])
for _ in range(8):
    u = rand_m(); L, g = bordered(u); Upool.append(u); gmin = min(gmin, g)
ev = np.linalg.eigvalsh(zn(L)); print(f"start k={len(Upool)}: lam_min {ev[0]:+.3e} min/max {ev[0]/ev[-1]:+.3e} min|H| {gmin:.3f} [{time.time()-t00:.0f}s]", flush=True)
step = 0
while len(Upool) < K:
    step += 1; cands = [('rand', rand_m()) for _ in range(4)]
    for sig in (0.02, 0.05, 0.1, 0.2):
        v = pert_m(Upool[rng.integers(len(Upool))], sig)
        if v is not None: cands.append((f'pert{sig}', v))
    best = None
    for (tag, u) in cands:
        B, g = bordered(u); ev = np.linalg.eigvalsh(zn(B))
        if best is None or ev[0] < best[0]: best = (ev[0], ev[-1], tag, u, B, g)
    L = best[4]; Upool.append(best[3]); gmin = min(gmin, best[5])
    print(f"step {step}: k={len(Upool)} added {best[2]:8s} lam_min {best[0]:+.3e} min/max {best[0]/best[1]:+.3e} min|H| {gmin:.3f} [{time.time()-t00:.0f}s]", flush=True)
fn = f"pool_NT1_wsearch_{model}_open_Lt{G.Lt}_seed{seed}_d{delta}.npz"
np.savez(fn, ux=np.array([u['x'] for u in Upool]), ut=np.array([u['t'] for u in Upool]))
mb = max(max(abs(wrap(u['x'][t, x] + u['t'][t, (x + 1) % 2] - u['x'][t + 1, x] - u['t'][t, x])) for t in range(G.T - 1) for x in range(2)) for u in Upool)
print(f"pool saved {fn}; W-match max|W1| {max(abs(wrap(u['x'][0].sum())) for u in Upool):.1e}; max bulk plaquette {mb:.4f}")
print(f"done [{time.time()-t00:.0f}s]")
