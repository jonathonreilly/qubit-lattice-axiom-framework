"""R19-11 'what works' probe: a TWISTED-MASS Wilson-Dirac edge (mass term i m beta gamma5, orthogonal to the Wilson term
beta W; Frezzotti-Rossi construction, RECALLED). In the 4-component Clifford form c = (S_x, S_y, S_z, W_tot, m) with five
anticommuting matrices, E^2 = S^2 + W_tot^2 + m^2, so every row depends on m only through m^2 (proved by inspection: m enters
c only as a constant fifth component). This file re-implements R16-13's dfam.evaluate and R18-5's xiud.pointwise with that c
(archived files untouched); at m = 0 it must reproduce the archived rows exactly (validation)."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import dfam
from content3 import D1q
from xiud import Gvec
def evaluate_tw(law, m, npan, ngl, Nc=4):
    k, wq = dfam.gl_nodes(law.breaks(), npan, ngl)
    S, Sp, Spp, W, Wp, Wpp = law.tables(k)
    wt = wq[:, None, None]*wq[None, :, None]*wq[None, None, :]
    mean = lambda f: float(np.sum(wt*f))
    Sx, Sy, Sz = S[:, None, None], S[None, :, None], S[None, None, :]
    Mw = W[:, None, None] + W[None, :, None] + W[None, None, :]
    E2 = Sx**2 + Sy**2 + Sz**2 + Mw**2 + m*m; E = np.sqrt(E2)
    cp2 = (Sp**2 + Wp**2)[None, None, :]
    Azz = (Sp**2 + S*Spp + Wp**2)[None, None, :] + Mw*Wpp[None, None, :] - 1
    G2 = 0.25*(Sx**2 + Sy**2); out = {}
    aterm = (Nc/8)*mean(G2*(cp2 - 1)/E**3)
    for pol, V2 in (('T2g', 4*Sx**2*Sy**2), ('Eg', (Sx**2 - Sy**2)**2)):
        out[pol] = aterm - (Nc/32)*mean(V2*Azz/E**5)
    px = Sx*Sp[:, None, None] + Mw*Wp[:, None, None]; py = Sy*Sp[None, :, None] + Mw*Wp[None, :, None]
    Hxx = (Sp**2 + S*Spp + Wp**2)[:, None, None] + Mw*Wpp[:, None, None]
    Hyy = (Sp**2 + S*Spp + Wp**2)[None, :, None] + Mw*Wpp[None, :, None]
    Hxy = Wp[:, None, None]*Wp[None, :, None]
    out['muE'] = -Nc*(-0.125*mean((Hxx - Hyy)*(px**2 - py**2)/E)); out['muT2'] = -Nc*(-0.5*mean(Hxy*px*py/E))
    return out
def pointwise_tw(law, m, names, pol, npan, ngl, Nc=4):
    k, wq = dfam.gl_nodes(law.breaks(), npan, ngl)
    S, Sp, Spp, W, Wp, Wpp = law.tables(k)
    out = {n: 0.0 for n in names}
    Sy, Spy, Wpy = S[:, None], Sp[:, None], Wp[:, None]
    Sz, Spz, Sppz, Wz, Wpz, Wppz = (A[None, :] for A in (S, Sp, Spp, W, Wp, Wpp))
    wyz = wq[:, None]*wq[None, :]
    for ix in range(len(k)):
        Sx, Spx, Wpx = S[ix], Sp[ix], Wp[ix]
        Mw = W[ix] + W[:, None] + Wz; Z = 0*Mw
        c = [Sx + Z, Sy + Z, Sz + Z, Mw, m + Z]
        cp = [Z, Z, Spz + Z, Wpz + Z, Z]; cpp = [Z, Z, Sppz + Z, Wppz + Z, Z]
        E2 = sum(x*x for x in c); E = np.sqrt(E2)
        cc1 = sum(a*b for a, b in zip(c, cp)); c1c1 = sum(a*a for a in cp); cc2 = sum(a*b for a, b in zip(c, cpp))
        Ep = cc1/E; Epp = (c1c1 + cc2 - Ep**2)/E
        px = Sx*Spx + Mw*Wpx; py = Sy*Spy + Mw*Wpy
        for n in names:
            G = list(Gvec(n, pol, Sx, Sy, Spx, Spy, Wpx, Wpy, Mw, px, py, c[:4], E2)) + [Z]
            G2 = sum(a*a for a in G); g = sum(a*b for a, b in zip(c, G))
            g1 = sum(a*b for a, b in zip(cp, G)); g2 = sum(a*b for a, b in zip(cpp, G))
            t0 = (Nc/2)*(G2 - g*g/E2)
            al = 0.25*(t0*Epp/(2*E2) + (Nc/2)*(G2*(c1c1 - Ep**2) + g*g2 - g1**2 - g*g*(E*Epp - Ep**2)/E2)/E**3)
            be = -t0/(4*E**3)
            out[n] += wq[ix]*float(np.sum(wyz*(al + be)))
    return out
def rows_tw(bf, r, m, q):
    law = D1q(bf, r); ref = evaluate_tw(law, m, *q); res = []
    for pol in ('T2g', 'Eg'):
        pw = pointwise_tw(law, m, ['V0', 'UD'], pol, *q); res.append(ref[pol] + pw['UD'] - pw['V0'])
    return np.array([res[0], res[1], ref['muE'], ref['muT2']])
if __name__ == '__main__':
    from smud_lib import dirac
    z = np.load(os.path.join(HERE, 'root0_final.npy')); bf, r = z[1], z[2]; q = (4, 10)
    print('D1(%.10f, %.10f) UD, GL%s, per field. twisted mass m_t vs Wilson-shift mass m (archived smud_lib.dirac):' % (bf, r, q))
    print('validation m=0: twisted %s | archived %s' % (rows_tw(bf, r, 0.0, q), dirac(bf, r, m=0.0, q=q)), flush=True)
    for m in (2.5e-4, 5e-4, 1e-3, 2e-3, 4e-3):
        print('m=%-7g twisted (T2g, Eg, muE, muT2) %s | Wilson-shift %s' % (m, rows_tw(bf, r, m, q), dirac(bf, r, m=m, q=q)), flush=True)
