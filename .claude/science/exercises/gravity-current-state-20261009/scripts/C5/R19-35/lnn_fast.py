"""R19-35: vacuum degree-0 (uniform-strain, SF) Hessian along nn, n=(1,1,0)/sqrt2, at vR18-9's root; per species and totals.
Units = archived shear-row units (scalar mu_E = Hess(diag(1,-1,0)) of (1/2)<eps o Phi>; Dirac -Nc*scalar formula, Nc=4;
vector 2 x scalar formula), i.e. R19-29's lam_nn units (its G(0)/4).  Rank-one identity: Hess(nn) = -(2w/24)<u^4/E^3>, u = n.p."""
import os, sys, time, numpy as np
from math import sqrt
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'arch18'))
import dfam
from content3 import D1q
from zz import ZLaw, mu_E
from photon import photonGw
t0 = time.time()
BS, BF, RR, AST, FR, BG, FW, M0 = np.load(os.path.join(HERE, 'root_refR18-9.npy'))
def sep(sigf, spf, sppf, m, N, w):
    kk = 2*np.pi*(np.arange(N) + 0.5)/N - np.pi
    s, sp, spp = sigf(kk), spf(kk), sppf(kk)
    g = s*s; f = s*sp; fp = sp*sp + s*spp
    X = lambda v, ax: np.expand_dims(v, [d for d in range(3) if d != ax])
    E = np.sqrt(m*m + X(g, 0) + X(g, 1) + X(g, 2))
    u = (X(f, 0) + X(f, 1))/sqrt(2.); dnu = 0.5*(X(fp, 0) + X(fp, 1))
    mean = lambda F: float(np.mean(np.broadcast_to(F, E.shape)))
    seag = 2*w*mean(u*u*dnu/(4*E)); bub = 2*w*(-mean(u**4/(8*E**3))); ibp = 2*w*(-mean(dnu*u*u/(8*E)))
    trH = X(fp, 0) + X(fp, 1) + X(fp, 2); ff = X(f, 0)**2 + X(f, 1)**2 + X(f, 2)**2
    hI = 2*w*(-mean(trH*ff/E)/8.)
    muE = 2*w*(-mean((X(fp, 0) - X(fp, 1))*(X(f, 0)**2 - X(f, 1)**2)/E)/8.)
    return dict(seag=seag, bub=bub, hnn=seag + bub, hnn_ibp=ibp, hI=hI, muE=muE, muT2=0.0,
                e0=w*mean(E), tau=2*w*0.25*mean(X(f, 0)**2/E))
def scalar(N):
    wA = FR*(np.pi - BS); L = ZLaw([1.0, 0.0], [BS + wA/2], wA); d2 = np.gradient(L.sp, L.k)
    sg = lambda k: np.sign(k)*np.interp(np.abs(k), L.k, L.sig); sp = lambda k: np.interp(np.abs(k), L.k, L.sp)
    spp = lambda k: np.sign(k)*np.interp(np.abs(k), L.k, d2)
    r = sep(sg, sp, spp, M0, N, 0.5); g, f = L.samples(1 << 14); r['muE_arch'] = mu_E(g, f, M0); return r
def photon(N, mreg=1e-3):
    L = photonGw(BG, FW*(np.pi - BG)); d2 = np.gradient(L.dp, L.a)
    sg = lambda k: L.sig(k); sp = lambda k: L.dpr(k); spp = lambda k: np.sign(k)*np.interp(np.abs(k), L.a, d2)
    r = sep(sg, sp, spp, mreg, N, 1.0); g, f = L.samples(1 << 14); r['muE_arch'] = 2*mu_E(g, f, 1e-3); return r
def dirac(npan, ngl, Nc=4):
    law = D1q(BF, RR); k, wq = dfam.gl_nodes(law.breaks(), npan, ngl)
    S, Sp, Spp, W, Wp, Wpp = law.tables(k)
    X = lambda v, ax: np.expand_dims(v, [d for d in range(3) if d != ax])
    wt = X(wq, 0)*X(wq, 1)*X(wq, 2); Mm = M0 + X(W, 0) + X(W, 1) + X(W, 2); Sv = [X(S, d) for d in range(3)]
    E = np.sqrt(Sv[0]**2 + Sv[1]**2 + Sv[2]**2 + Mm**2)
    p = [Sv[d]*X(Sp, d) + Mm*X(Wp, d) for d in range(3)]
    Hd = [X(Sp**2 + S*Spp, d) + Mm*X(Wpp, d) for d in range(3)]; Wv = [X(Wp, d) for d in range(3)]
    mean = lambda F: float(np.sum(wt*np.broadcast_to(F, E.shape)))
    n = np.array([1., 1., 0.])/sqrt(2.); w = -Nc/2.
    u = sum(n[d]*p[d] for d in range(3)); nW = sum(n[d]*Wv[d] for d in range(3))
    nHn = sum(n[d]**2*Hd[d] for d in range(3)) + nW**2
    ibp = 2*w*(-mean(nHn*u*u/E)/8.); rank1 = 2*w*(-mean(u**4/E**3)/24.)
    dc = [0.5*u*n[d]*X(Sp, d) for d in range(3)] + [0.5*u*nW]; cv = Sv + [Mm]
    cdc = sum(c*x for c, x in zip(cv, dc))/E; dperp2 = sum(x*x for x in dc) - cdc**2
    bub_phys = w*mean(dperp2/E)
    trH = sum(Hd) + sum(x*x for x in Wv); pp = sum(x*x for x in p)
    Hxx, Hyy = Hd[0] + Wv[0]**2, Hd[1] + Wv[1]**2
    o = dfam.evaluate(law, M0, npan, ngl)
    return dict(hnn=ibp, hnn_rank1=rank1, bub_phys=bub_phys, seag_phys=ibp - bub_phys,
                bub_band=2*w*(-mean(u**4/(8*E**3))), hI=2*w*(-mean(trH*pp/E)/8.),
                muE=2*w*(-mean((Hxx - Hyy)*(p[0]**2 - p[1]**2)/E)/8.), muT2=2*w*(-mean(Wv[0]*Wv[1]*p[0]*p[1]/E)/2.),
                muE_arch=o['muE'], muT2_arch=o['muT2'], e0=w*mean(E), tau=2*w*0.25*mean(p[0]**2/E), nodes=len(k))
Ns = int(sys.argv[1]); Ng = int(sys.argv[2]); q = tuple(int(v) for v in sys.argv[3].split(','))
sc = scalar(Ns); ph = photon(Ng); di = dirac(*q)
print('root (bs,bf,r,a,fr,bg,fw,m) =', np.round([BS, BF, RR, AST, FR, BG, FW, M0], 7))
for nm, r in (('scalar N=%d' % Ns, sc), ('photon N=%d' % Ng, ph), ('Dirac GL%s nodes %d' % (q, di['nodes']), di)):
    print('%-22s ' % nm + '  '.join('%s %+.6e' % (k, v) for k, v in r.items() if k != 'nodes'))
wts = (NS, ND, NV) = (4.0, 22.5, 12.0)
tot = lambda key: NS*sc[key] + ND*di[key] + NV*ph[key]
lam = tot('hnn'); e0 = tot('e0'); tau = tot('tau'); muE = tot('muE'); muT2 = tot('muT2'); hI = tot('hI')
print('\nTOTALS (4 S + 22.5 D + 12 V):')
print('  shear rows (validation, should be ~0 at root): muE_tot %+.4e (arch %+.4e)  muT2_tot %+.4e' % (muE, NS*sc['muE_arch'] + ND*di['muE_arch'] + NV*ph['muE_arch'], muT2))
print('  contributions to lam_nn: scalars %+.5f  Dirac %+.5f  vectors %+.5f' % (NS*sc['hnn'], ND*di['hnn'], NV*ph['hnn']))
print('  LAM_NN (bare, SF)            = %+.6f   [check (1/9)Hess(I) + muE/12 + muT2/4 = %+.6f]' % (lam, hI/9 + muE/12 + muT2/4))
print('  4*lam_nn = %+.5f  vs R19-29 bubble 4nn:Pi^b(0):nn = -25.883 -> ratio |lam_nn|/|bubble/4| = %.4f' % (4*lam, abs(lam)/(25.88266/4)))
print('  one-point: e0_tot %+.5f  tau_tot %+.5f  (W_tot = e0 + p = e0 + 2 tau = %+.5f)' % (e0, tau, e0 + 2*tau))
print('  variants: A (all ct linear in h_SF) %+.5f | B ((S) = -e0 sqrt g, exp param) %+.5f | C (ct linear in h_lin) %+.5f | D ((S) sqrt g lin + P-Tad lin) %+.5f'
      % (lam, lam - e0/4, lam + tau, lam + tau + e0/4))
print('  fluid control (Pi_SF = e0/4, tau = -e0/2): A %+.3f B %+.3f C %+.3f D %+.3f' % (e0/4, 0.0, -e0/4, 0.0))
print('runtime %.1f s' % (time.time() - t0))
