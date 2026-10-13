"""R19-29 (c)/(d): the A_1 gauge-block numbers at R18-13's root (m = 0.01), per species and in R18-13's totals convention
(4 scalars [e:e = 2] + 22.5 Dirac [dface normalization e:e = 1/2, i.e. 1/4 of the E1F kernel] + 12 vectors [e:e = 2]).
Closed forms (P1 contact identities, checked in r1929_struct/dirac/photon .out):
   Pi(e1, gn) = s D(s),  D = -4 <Gam(e1, nn)/E>;   Pi_b(gn, gn) = s^2 G(s),  G = -8 <Gam(nn, nn)/E>;
   Pi(g0, g0) = -8 s^4 X(s), X = <Gam(nn, nn)/E^3>;  Pi(g0, gn) = 8 omega s^3 X;   Pi(e1, g0) = 0.
   kappa = lim (D(s) - D(0))/s^2 ; c4 = lim (G(s) - G(0))/s^2 ; X = X(0).
   If the total degree-0 longitudinal entry lam_nn = nn:Pi0:nn vanishes, the face1 pole coefficient = row - kappa^2/(c4 + 8X);
   otherwise the Schur term is kappa^2 s^2/(4 lam_nn) + O(s^4) relative, i.e. it vanishes at the row's order.
usage: python r1929_root.py Ns Nd Ngam"""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'arch18'))
from a1lib import *
t0 = time.time()
Ns, Nd, Ng = (int(v) for v in sys.argv[1:4])
root = np.load(os.path.join(HERE, 'root_refR18-9.npy')); bs, bf, rr, a, fr, bg, fw, m = root
wd, wo = -1.171554, -0.195418          # R18-13's N = 224 solve (C5_R18-13_report.md:282)
NNs = np.outer(n3, n3); E13 = E1F[1:, 1:]
out = {}
# ---------- scalar (U, E1) ----------
law, _ = root_scalar_law(); sc = Scalar(law, m, Ns)
def scal_g(s):
    ep, em = sc.amps(s*n3); E = ep + em; w = 1/(8*ep*em)
    te, tn = sc.tau(E13), sc.tau(NNs)
    # Pi = -<Gam [1/(E-w) + 1/(E+w)]> with Gam = w tau tau  -> same closed forms
    return (-4*np.sum(sc.W*w*te*tn/E), -8*np.sum(sc.W*w*tn*tn/E), np.sum(sc.W*w*tn*tn/E**3))
# ---------- Dirac (UD midpoint) ----------
from content3 import D1q
dl = D1q(bf, rr); x = 2*np.pi*(np.arange(Nd)+0.5)/Nd - np.pi
K = [k.ravel() for k in np.meshgrid(x, x, x, indexing='ij')]
S0 = [dl.S(k) for k in K]; Sp0 = [dl.dS(k) for k in K]; W0 = [dl.W(k) for k in K]; Wp0 = [dl.dW(k) for k in K]
M0 = m + sum(W0); p0 = [S0[i]*Sp0[i] + M0*Wp0[i] for i in range(3)]
def Gv(e3):
    ep = [sum(e3[aa, j]*p0[j] for j in range(3)) for aa in range(3)]
    return [ep[aa]*Sp0[aa] for aa in range(3)] + [sum(Wp0[i]*ep[i] for i in range(3))]
Ge, Gn = Gv(E13), Gv(NNs)
def dirac_g(s):
    q = s*n3
    def cvec(Ks):
        return [dl.S(k) for k in Ks] + [m + sum(dl.W(k) for k in Ks)]
    cp = cvec([k + qq/2 for k, qq in zip(K, q)]); cm = cvec([k - qq/2 for k, qq in zip(K, q)])
    Ep = np.sqrt(sum(c*c for c in cp)); Em = np.sqrt(sum(c*c for c in cm)); E = Ep + Em
    u = [c/Ep for c in cp]; v = [c/Em for c in cm]; uv = sum(aa*bb for aa, bb in zip(u, v))
    def gram(A, B):
        return 1.0*(sum(aa*bb for aa, bb in zip(A, B))*(1 + uv) - sum(aa*bb for aa, bb in zip(u, A))*sum(aa*bb for aa, bb in zip(v, B))
                    - sum(aa*bb for aa, bb in zip(u, B))*sum(aa*bb for aa, bb in zip(v, A)))   # Nc/4 = 1
    gen, gnn = gram(Ge, Gn), gram(Gn, Gn); Wt = 1.0/Nd**3
    return (-4*Wt*np.sum(gen/E), -8*Wt*np.sum(gnn/E), Wt*np.sum(gnn/E**3))
# ---------- photon (VWa-geo + own-direction data) ----------
from photon import kgrid, crossmat, photonGw
import vwface_copy as V
pl = photonGw(bg, fw*(np.pi - bg)); kg = kgrid(Ng); sg = pl.sig(kg); cg = pl.c(kg); jj = np.arange(Ng)
def phot_g(n):
    sh = (n, n, 0); j2 = [(sh[d] - jj - 1) % Ng for d in range(3)]
    Y, Z = np.meshgrid(jj, jj, indexing='ij'); acc = np.zeros(3)
    for ix in range(Ng):
        X_ = np.full_like(Y, ix); I1 = [X_, Y, Z]; I2 = [j2[0][X_], j2[1][Y], j2[2][Z]]
        s1 = np.stack([sg[I] for I in I1], -1); s2 = np.stack([sg[I] for I in I2], -1)
        c1 = np.stack([cg[I] for I in I1], -1); c2 = np.stack([cg[I] for I in I2], -1)
        ssum = np.stack([kg[I1[d]] + kg[I2[d]] for d in range(3)], -1)
        w1 = np.sqrt((s1*s1).sum(-1)); w2 = np.sqrt((s2*s2).sum(-1)); rw = np.sqrt(w1*w2); E = w1 + w2
        X1 = crossmat(s1); X2 = crossmat(s2)
        P1 = np.eye(3) - s1[..., :, None]*s1[..., None, :]/(w1*w1)[..., None, None]
        P2 = np.eye(3) - s2[..., :, None]*s2[..., None, :]/(w2*w2)[..., None, None]
        Nm = []
        for e in (E13, NNs):
            ME, MB = V.vertex_geo(e, c1, c2, ssum, a, wd, wo)
            Bp = np.einsum('...ji,...jk,...kl->...il', X1, MB, X2)/rw[..., None, None]
            Nm.append(0.5*(rw[..., None, None]*ME + Bp))
        g = lambda A, B: 0.5*np.einsum('...ij,...jk,...kl,...il->...', P1, A, P2, B)
        gen, gnn = g(Nm[0], Nm[1]), g(Nm[1], Nm[1])
        acc += [np.sum(-4*gen/E), np.sum(-8*gnn/E), np.sum(gnn/E**3)]
    return acc/Ng**3, 2*np.pi*np.sqrt(2)*n/Ng
def extrap(f, ss):
    v = np.array([f(s) for s in ss])                  # rows: s; cols D, G, X
    return v
res = {}
ss = [0.0, 0.04, 0.02]
for nm, f in (('scalar', scal_g), ('dirac', dirac_g)):
    v = np.array([f(s) for s in ss])
    k1 = (v[1, 0] - v[0, 0])/ss[1]**2; k2 = (v[2, 0] - v[0, 0])/ss[2]**2; kap = (4*k2 - k1)/3
    c1 = (v[1, 1] - v[0, 1])/ss[1]**2; c2_ = (v[2, 1] - v[0, 1])/ss[2]**2; c4 = (4*c2_ - c1)/3
    res[nm] = (kap, c4, v[0, 2], v[0, 0], v[0, 1])
    print('%-7s: D(0)=%+.6e G(0)=%+.6e X(0)=%+.6e | kappa: s=0.04 %+.6e, s=0.02 %+.6e -> %+.6e | c4: %+.6e, %+.6e -> %+.6e'
          % (nm, v[0, 0], v[0, 1], v[0, 2], k1, k2, kap, c1, c2_, c4), flush=True)
pv0, _ = phot_g(0); pv1, s1 = phot_g(1); pv2, s2 = phot_g(2)
k1 = (pv1[0] - pv0[0])/s1**2; k2 = (pv2[0] - pv0[0])/s2**2; kap = (4*k1 - k2)/3
c1 = (pv1[1] - pv0[1])/s1**2; c2_ = (pv2[1] - pv0[1])/s2**2; c4 = (4*c1 - c2_)/3
res['photon'] = (kap, c4, pv0[2], pv0[0], pv0[1])
print('photon : N=%d D(0)=%+.6e G(0)=%+.6e X(0)=%+.6e | kappa: s=%.4f %+.6e, s=%.4f %+.6e -> %+.6e | c4: %+.6e, %+.6e -> %+.6e'
      % (Ng, pv0[0], pv0[1], pv0[2], s1, k1, s2, k2, kap, c1, c2_, c4), flush=True)
mult = {'scalar': 4.0, 'dirac': 22.5*0.25, 'photon': 12.0}
tot = sum(mult[k_]*np.array(res[k_]) for k_ in res)
print('\nTOTALS (R18-13 convention: 4 scalars + 22.5 Dirac x 1/4 + 12 vectors): kappa %+.6e  c4 %+.6e  X %+.6e  D(0) %+.6e  G(0) %+.6e'
      % tuple(tot))
for k_ in res:
    print('   share of kappa: %-7s %+.4e' % (k_, mult[k_]*res[k_][0]))
print('lam_nn = 0 branch: face1 pole coefficient shift  -kappa^2/(c4 + 8X) = %+.6e (R18-13 totals units)' % (-tot[0]**2/(tot[1] + 8*tot[2])))
print('compare: face1 total before the own-direction solve +2.6424; d face1/d w_d (totals) = 1.676 (R18-13 Sec 3.4)')
print('runtime %.1f s' % (time.time() - t0))
