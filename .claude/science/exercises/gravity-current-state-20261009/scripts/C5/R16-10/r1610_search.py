"""R16-10: random search for F_s(0+) >= 0 inside the class with SUBLUMINAL nondecreasing photons (d' in [0,1]),
and (scalar) also with stiff nondecreasing photons. Matter in the class (S <= q; u'/2 <= q).
Families:
  photon Gph(c) [d' in [0,1]];  photon R85(c1,c2,1) when numerically monotone [d' <= 1 always];
  photon R85(c1,c2,G>=pi/2) stiff (superluminal; nondecreasing proved).
  scalar ScalFlat(b, w): u = h^2, h' = 1 - sstep((|k|-b)/w), flat beyond b+w (w <= pi-b).  (G(b) = ScalFlat(b, pi-b))
  Dirac D1(b, r<=1/sqrt3); literal(b1,b2); dip-rise S = rho k + (1-rho)(sin k - (beta/2) sin 2k) (R16-2), S<=q checked.
"""
import numpy as np, sys, time
from r1610_eval import *
from r1610_laws import *
from sublum import sstep, dsstep, wrap, Phi
from r85_box_qed_copy import plateau
t0 = time.time()
rng = np.random.default_rng(int(sys.argv[2]))
spin = float(sys.argv[1]); nlaw = int(sys.argv[3]); stiff = len(sys.argv) > 4 and sys.argv[4] == 'stiff'
qq = np.linspace(0, np.pi, 4001)
def scal_flat(b, w):
    def h(k):
        a = np.abs(wrap(np.asarray(k, float))); x = np.clip((a - b)/w, 0, 1)
        return np.where(a <= b, a, b + w*Phi(x) * 0 + w*(x - Phi(x)))   # int_b^a (1 - sstep) = w (x - Phi(x))
    return lambda k: h(k)**2
def diprise(b1, b2, beta):
    def S(k):
        k = np.asarray(k, float); rho = plateau(k, b1, b2); return rho*k + (1 - rho)*(np.sin(k) - 0.5*beta*np.sin(2*k))
    return S, (lambda k: 0.0*np.asarray(k, float))
best = None
for it in range(nlaw):
    # photon
    if stiff:
        c1 = rng.uniform(0.5, 2.5); c2 = rng.uniform(c1 + 0.3, min(c1 + 2.0, 3.1)); G = rng.uniform(1.6, 8.0)
        ph = ('R85', c1, c2, G)
    elif rng.random() < 0.5:
        ph = ('Gph', rng.uniform(0.4, 3.1))
    else:
        c1 = rng.uniform(0.4, 2.6); c2 = rng.uniform(c1 + 0.3, min(c1 + 2.5, 3.14)); ph = ('R85', c1, c2, 1.0)
    d = photon(*ph); dd = np.gradient(d(qq), qq)
    if dd.min() < -1e-6:
        continue
    cbox = ph[1]
    # matter
    if spin == 0:
        b = rng.uniform(0.3, 3.0); w = rng.uniform(0.05, np.pi - b); mat = ('Flat', b, w); matter = scal_flat(b, w); m = 0.0
        chk = np.max((0.5*np.gradient(matter(qq), qq) - qq)[1:-1])
        bb = b
    else:
        kind = rng.integers(3)
        if kind == 0:
            b = rng.uniform(0.4, 1.5); r = rng.uniform(0, 1/np.sqrt(3)); mat = ('D1', b, r); matter = dirac_D1(b, r); bb = b
        elif kind == 1:
            b1 = rng.uniform(0.3, 2.6); b2 = rng.uniform(b1 + 0.3, min(b1 + 2.5, 3.14)); mat = ('lit', b1, b2); matter = dirac_lit(b1, b2); bb = b1
        else:
            b1 = rng.uniform(0.3, 2.0); b2 = rng.uniform(b1 + 0.3, min(b1 + 2.5, 3.14)); beta = rng.uniform(0, 2.0)
            mat = ('diprise', b1, b2, beta); matter = diprise(b1, b2, beta); bb = b1
        m = 1e-6
        chk = np.max(matter[0](qq) - qq)
    if chk > 1e-5:
        continue
    box = min(cbox, bb); r1 = min(0.75*box, 0.9); r0 = 0.35*r1
    lp, tp = lattice_part(spin, 32, m, 0.0, matter, d, r0, r1, 0.02)
    F = K[spin] + lp
    print('%-55s %-45s maxd\'=%.2f | F(0+)~%+8.4f [tad/sea %+8.4f]' % (str(tuple(np.round(mat[1:], 3)))+mat[0], str(tuple(np.round(ph[1:], 3)))+ph[0], dd.max(), F, tp), flush=True)
    if best is None or F > best[0]:
        best = (F, mat, ph)
print('BEST', best)
print('elapsed %.1fs' % (time.time() - t0))
