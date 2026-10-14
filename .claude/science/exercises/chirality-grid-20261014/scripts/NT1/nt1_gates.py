"""NT-1 gates G1-G7 and diagnostic D1 (PREREG.md section 4). usage: python3 nt1_gates.py POOL.npz T [model]"""
import numpy as np, sys, time
from nt1_lib import *
from lat2d import Geom, nodes

fn, T = sys.argv[1], int(sys.argv[2]); model = sys.argv[3] if len(sys.argv) > 3 else '11112'
G = Geom(2, T, False, -1); LK = Links(G); t00 = time.time()
z = np.load(fn); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]
print(f"# NT-1 gates  pool={fn} Lt={G.Lt} N={G.N} links={LK.nl} model={model}", flush=True)

# configurations: 5 joined configs J(a, b, phi) at a mid quadrature node
rng = np.random.default_rng(11); cfg = []
for (a, b) in [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]:
    ph, w = nodes(G, U[a], U[b], 0.6, 16, 'hard'); i = len(w) // 3
    cfg.append((a, b, ph[i:i+1]))
A = np.concatenate([LK.joined(U[a], U[b], ph) for (a, b, ph) in cfg])

# builder check vs lat2d.full_D
dmax = max(np.abs(LK.D(LK.joined(U[a], U[b], ph))[0] - G.full_D(U[a], U[b], ph[0])).max() for (a, b, ph) in cfg)
print(f"builder vs lat2d.full_D: max |dD| = {dmax:.1e}")

# G1 factorization
CH = Chiral(LK, 'vecW', Ns=32)
W, P = CH.logrho(A, parts=True)
ld0, g0 = vec_logdet(LK, A, 0.0)
# |det M_L| |det M_R| = 2^N |det V+rows| |det V-rows|
r = np.abs((W.real + G.N * np.log(2)) - ld0.real).max()
Wl = Chiral(LK, 'L1', Ns=32).logrho(A)[0].real; Wr = W.real - Wl
print(f"G1: max | ln|detM_L detM_R| - ln|det D| | = {r:.2e} ; max | ln|det M_L| - ln|det M_R| | = {np.abs(Wl - Wr).max():.2e}  -> {'PASS' if r < 1e-10 and np.abs(Wl-Wr).max() < 1e-10 else 'FAIL'}")

# G4 transport convergence
prev = None; Ns_ok = None
for Ns in (16, 32, 64, 128):
    CHm = Chiral(LK, model, Ns=Ns, sk=+1); Wn, Pn = CHm.logrho(A, parts=True)
    if prev is not None:
        dW0 = np.abs(Pn['W0'] - prev['W0']).max(); dc = np.abs(Pn['corr'] - prev['corr']).max(); dW = np.abs(Wn - prevW).max()
        print(f"G4: Ns {Ns//2}->{Ns}: max|dW0| {dW0:.2e} max|dcorr| {dc:.2e} max|dW| {dW:.2e}", flush=True)
        if Ns_ok is None and dW < 1e-8: Ns_ok = Ns // 2
    prev, prevW = Pn, Wn
print(f"G4: Ns_main = {Ns_ok}  [{time.time()-t00:.0f}s]")
Ns = Ns_ok or 128

# G2 gauge invariance (both signs; W0 alone)
def ev(model_, Aset, sk=+1):
    return Chiral(LK, model_, Ns=Ns, sk=sk).logrho(Aset, parts=True)
lower = (LK.site_t < G.T - 1).astype(float)          # sites with t <= 0
res = {}
for mdl in (model, 'L1'):
    Wp, Pp = ev(mdl, A, +1)
    for tag, om in (('lower-shift c=0.3', np.repeat((0.3 * lower)[None], len(A), 0)),
                    ('random omega 0.2', rng.normal(0, 0.2, (len(A), LK.nsite)))):
        Ag = LK.gauge(A, om); Wg, Pg = ev(mdl, Ag, +1)
        d0 = Pg['W0'] - Pp['W0']; dc = Pg['corr'] - Pp['corr']
        def ph(x): return np.abs(np.angle(np.exp(1j * x.imag))).max()
        dre = np.abs(d0.real).max()
        print(f"G2 [{mdl}] {tag}: |dRe W| {dre:.1e} | W0 alone: |dIm| {ph(d0):.2e} | W0 + i sum A kbar (s=+1): {ph(d0 + dc):.2e} | (s=-1): {ph(d0 - dc):.2e}"
              f" | min|H| {min(Pp['gmin'], Pg['gmin']):.3f}", flush=True)
        res[(mdl, tag)] = (ph(d0 + dc), ph(d0 - dc), ph(d0))
sp = max(res[(model, t)][0] for t in ('lower-shift c=0.3', 'random omega 0.2')); sm = max(res[(model, t)][1] for t in ('lower-shift c=0.3', 'random omega 0.2'))
sk = +1 if sp < sm else -1; best, other = min(sp, sm), max(sp, sm)
print(f"G2 [{model}]: s_k = {sk:+d}; max phase violation {best:.2e} (other sign {other:.2e}) -> {'PASS' if best < 1e-6 and other > 100 * best else 'FAIL'}")

# G3 Theta reality: rho(J(b, a, -phi)) = c conj rho(J(a, b, phi))
CHs = Chiral(LK, model, Ns=Ns, sk=sk)
Ar = np.concatenate([LK.joined(U[b], U[a], -ph) for (a, b, ph) in cfg])
W1 = CHs.logrho(A)[0]; W2 = CHs.logrho(Ar)[0]
c = W2 - np.conj(W1); cph = np.angle(np.exp(1j * c.imag)); cre = c.real
spread = np.abs(np.angle(np.exp(1j * (cph - cph[0])))).max()
print(f"G3: ln rho(thetaJ) - conj ln rho(J): Re max|.| {np.abs(cre).max():.2e}; phase c = {cph[0]:+.6f}, spread {spread:.2e} -> {'PASS' if spread < 1e-6 and np.abs(cre).max() < 1e-6 else 'FAIL'}")
# same for W0 alone (descriptive)
P1 = CHs.logrho(A, parts=True)[1]; P2 = CHs.logrho(Ar, parts=True)[1]
c0 = P2['W0'] - np.conj(P1['W0']); c0p = np.angle(np.exp(1j * c0.imag))
print(f"G3 (W0 alone, descriptive): phase spread {np.abs(np.angle(np.exp(1j*(c0p - c0p[0])))).max():.2e}")

# G5-G7
_, P5 = CHs.logrho(A, parts=True)
print(f"G5: min|eig H_W(U_t^e)| over rays = {P5['gmin']:.3f} -> {'PASS' if P5['gmin'] > 0.1 else 'FAIL'}; G7 index ok {P5['idx_ok']}; G6 max|sum_x Abar| {P5['sumA']:.1e}")

# D1 locality of K(t): perturb the bottom-most lower slice (t = 1 - T) x-links by +0.05 each
Ab = A.copy()
for x in range(2): Ab[:, LK.key[('x', x, 1 - G.T)]] += 0.05
for mdl in (model, 'L1'):
    _, Pa = Chiral(LK, mdl, Ns=Ns, sk=sk).logrho(A, parts=True); _, Pb = Chiral(LK, mdl, Ns=Ns, sk=sk).logrho(Ab, parts=True)
    dK = np.abs(Pb['K'] - Pa['K']).max(0)
    print(f"D1 [{mdl}] max_cfg |dK(slice s)|, s = 0 (bottom) .. Lt-1: " + " ".join(f"{v:.1e}" for v in dK))
print(f"cphase (for kernels) = {-0.5 * cph[0]:+.8f}   Ns = {Ns}   s_k = {sk:+d}")
print(f"done [{time.time()-t00:.0f}s]")
