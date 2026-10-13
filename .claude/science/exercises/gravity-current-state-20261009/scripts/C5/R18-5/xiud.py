"""R18-5 (b): one-loop graviton-cone shift Xi = d_{q^2}Pi + d_{w^2}Pi for a Clifford-linear Dirac TT vertex
Gamma = G(k).gamma whose G may depend on k_z (axial q = q z), with the midpoint prescription G(k) for the pair
(k - q/2, k + q/2) (stated law datum; O(q^2) placement, cf. R17-12 Lemma I).  Ultralocal seagull (drops out).
Pointwise expansion (derived here; reduces to R16-13 Theorem DT when c.G is k_z-independent):
  t0 = (Nc/2)(|G|^2 - g^2/E^2),  g = c.G, g1 = c'.G, g2 = c''.G  (' = d/dk_z)
  alpha = < (1/4)[ t0 E''/(2E^2) + (Nc/2)( |G|^2(|c'|^2 - E'^2) + g g2 - g1^2 - g^2 (E E'' - E'^2)/E^2 )/E^3 ] >
  beta  = -< t0/(4 E^3) >
Xi_X = Xi_V0[dfam closed form, R16-13] + < (alpha+beta)_X - (alpha+beta)_V0 >   (difference vanishes where |k_x|,|k_y| < b).
Vertices: V0, UD = (1/2)(p_j d_i h + p_i d_j h), V0* = V0 + h(p_i p_j - s_i s_j)/E^2 (and Eg analogues)."""
import numpy as np, sys
sys.path.insert(0, '.')
import dfam
from content3 import D1q

def Gvec(name, pol, Sx, Sy, Spx, Spy, Wpx, Wpy, M, px, py, c, E2):
    """returns G as list of 4 arrays over (alpha_x, alpha_y, alpha_z, beta)."""
    z = 0.0*M
    if pol == 'T2g':
        G0 = [0.5*Sy + z, 0.5*Sx + z, z, z]; dlt = px*py - Sx*Sy
        GU = [0.5*py*Spx, 0.5*px*Spy, z, 0.5*(py*Wpx + px*Wpy)]
    else:
        G0 = [0.5*Sx + z, -0.5*Sy + z, z, z]; dlt = 0.5*(px**2 - py**2) - 0.5*(Sx**2 - Sy**2)
        GU = [0.5*px*Spx, -0.5*py*Spy, z, 0.5*(px*Wpx - py*Wpy)]
    if name == 'V0': return G0
    if name == 'UD': return GU
    if name == 'V0*': return [G0[a] + c[a]*dlt/E2 for a in range(4)]
    if name.startswith('mix'):          # convex family (1-u) V0* + u UD: same forward block, interpolated pair block
        u = float(name[3:]); Gs = [G0[a] + c[a]*dlt/E2 for a in range(4)]
        return [(1-u)*Gs[a] + u*GU[a] for a in range(4)]

def pointwise(law, m, names, pol, npan=3, ngl=8, Nc=4):
    k, wq = dfam.gl_nodes(law.breaks(), npan, ngl)
    S, Sp, Spp, W, Wp, Wpp = law.tables(k)
    out = {n: 0.0 for n in names}
    Sy, Spy, Wpy = S[:, None], Sp[:, None], Wp[:, None]          # (ky, kz)
    Sz, Spz, Sppz, Wz, Wpz, Wppz = (A[None, :] for A in (S, Sp, Spp, W, Wp, Wpp))
    wyz = wq[:, None]*wq[None, :]
    for ix in range(len(k)):
        Sx, Spx, Wpx = S[ix], Sp[ix], Wp[ix]
        M = m + W[ix] + W[:, None] + Wz
        c = [Sx + 0*M, Sy + 0*M, Sz + 0*M, M]
        cp = [0*M, 0*M, Spz + 0*M, Wpz + 0*M]
        cpp = [0*M, 0*M, Sppz + 0*M, Wppz + 0*M]
        E2 = sum(x*x for x in c); E = np.sqrt(E2)
        cc1 = sum(a*b for a, b in zip(c, cp)); c1c1 = sum(a*a for a in cp); cc2 = sum(a*b for a, b in zip(c, cpp))
        Ep = cc1/E; Epp = (c1c1 + cc2 - Ep**2)/E
        px = Sx*Spx + M*Wpx; py = Sy*Spy + M*Wpy
        for n in names:
            G = Gvec(n, pol, Sx, Sy, Spx, Spy, Wpx, Wpy, M, px, py, c, E2)
            G2 = sum(a*a for a in G); g = sum(a*b for a, b in zip(c, G))
            g1 = sum(a*b for a, b in zip(cp, G)); g2 = sum(a*b for a, b in zip(cpp, G))
            t0 = (Nc/2)*(G2 - g*g/E2)
            al = 0.25*(t0*Epp/(2*E2) + (Nc/2)*(G2*(c1c1 - Ep**2) + g*g2 - g1**2 - g*g*(E*Epp - Ep**2)/E2)/E**3)
            be = -t0/(4*E**3)
            out[n] += wq[ix]*float(np.sum(wyz*(al + be)))
    return out

def xi_vertices(law, m, names=('V0', 'UD', 'V0*'), npan=3, ngl=8):
    ref = dfam.evaluate(law, m, npan, ngl)
    res = {}
    for pol in ('T2g', 'Eg'):
        pw = pointwise(law, m, ['V0'] + [n for n in names if n != 'V0'], pol, npan, ngl)
        for n in names:
            res[(n, pol)] = ref[pol] + (pw[n] - pw['V0'])
        res[('V0pw', pol)] = pw['V0']
    res['muE'] = ref['muE']; res['muT2'] = ref['muT2']
    return res

def brute(law, m, name, pol, N, shifts=(1, 2, 4), Nc=4):
    """direct finite-q evaluation on a uniform midpoint grid: legs k -+ q/2 at grid shifts -+n, q = 4 pi n / N."""
    kk = (np.arange(N) + 0.5)*2*np.pi/N - np.pi
    S, Sp, Spp, W, Wp, Wpp = law.tables(kk)
    def at(ix, iz):
        pass
    tot = {}
    vals = []
    for n in (0,) + tuple(shifts):
        acc = 0.0
        for ix in range(N):
            Sx, Spx, Wpx = S[ix], Sp[ix], Wp[ix]
            Sy, Spy, Wpy = S[:, None], Sp[:, None], Wp[:, None]
            Mz = m + W[ix] + W[:, None] + W[None, :]
            c = [Sx + 0*Mz, Sy + 0*Mz, S[None, :] + 0*Mz, Mz]
            E2 = sum(x*x for x in c)
            px = Sx*Spx + Mz*Wpx; py = Sy*Spy + Mz*Wpy
            G = Gvec(name, pol, Sx, Sy, Spx, Spy, Wpx, Wpy, Mz, px, py, c, E2)
            ca = [np.roll(x, n, axis=1) for x in c]; cb = [np.roll(x, -n, axis=1) for x in c]
            Ea = np.sqrt(sum(x*x for x in ca)); Eb = np.sqrt(sum(x*x for x in cb))
            G2 = sum(a*a for a in G)
            caG = sum(a*b for a, b in zip(ca, G)); cbG = sum(a*b for a, b in zip(cb, G)); cab = sum(a*b for a, b in zip(ca, cb))
            t = (Nc/4)*(G2*(1 + cab/(Ea*Eb)) - 2*caG*cbG/(Ea*Eb))
            acc += float(np.mean(2*t/(Ea + Eb)))
            if n == 0:
                pass
        vals.append(acc/N)
    c0 = vals[0]; d = []
    for n, v in zip(shifts, vals[1:]):
        q = 4*np.pi*n/N; d.append(-(v - c0)/q**2)
    r1 = (4*d[0] - d[1])/3; r2 = (4*d[1] - d[2])/3; alpha = (16*r1 - r2)/15
    # beta
    acc = 0.0
    for ix in range(N):
        Sx, Spx, Wpx = S[ix], Sp[ix], Wp[ix]
        Sy, Spy, Wpy = S[:, None], Sp[:, None], Wp[:, None]
        Mz = m + W[ix] + W[:, None] + W[None, :]
        c = [Sx + 0*Mz, Sy + 0*Mz, S[None, :] + 0*Mz, Mz]; E2 = sum(x*x for x in c)
        px = Sx*Spx + Mz*Wpx; py = Sy*Spy + Mz*Wpy
        G = Gvec(name, pol, Sx, Sy, Spx, Spy, Wpx, Wpy, Mz, px, py, c, E2)
        G2 = sum(a*a for a in G); g = sum(a*b for a, b in zip(c, G))
        t0 = (Nc/2)*(G2 - g*g/E2)
        acc += float(np.mean(-t0/(4*E2**1.5)))
    beta = acc/N
    return alpha + beta, alpha, beta

if __name__ == '__main__':
    import time
    t0 = time.time()
    mode = sys.argv[1]
    if mode == 'validate':
        law = D1q(1.4, 0.3); m = 0.3
        for (npan, ngl) in ((3, 8), (4, 10)):
            r = xi_vertices(law, m, ('V0', 'UD', 'V0*'), npan, ngl)
            print('GL(%d,%d) D1(1.4,0.3) m=0.3:' % (npan, ngl), ' '.join('%s/%s %+.6e' % (n, p, r[(n, p)]) for n in ('V0', 'V0pw', 'UD', 'V0*') for p in ('T2g', 'Eg')), flush=True)
        for N in (64, 96):
            for name in ('V0', 'UD', 'V0*'):
                x, a, b = brute(law, m, name, 'T2g', N)
                print('brute N=%d %s T2g: Xi %+.6e (alpha %+.6e beta %+.6e)  [%.0fs]' % (N, name, x, a, b, time.time()-t0), flush=True)
            x, a, b = brute(law, m, 'UD', 'Eg', N)
            print('brute N=%d UD Eg: Xi %+.6e  [%.0fs]' % (N, x, time.time()-t0), flush=True)
    elif mode == 'laws':
        m = float(sys.argv[2])
        for (b, r) in ((1.4, 0.3), (1.4, 0.5773), (1.313474886012, 0.572783392213), (0.916719, 0.559627), (1.0, 0.3), (0.6, 0.5), (0.3, 0.5), (1.55, 0.5)):
            law = D1q(b, r)
            rr = [xi_vertices(law, m, ('V0', 'UD', 'V0*'), *q) for q in ((3, 8), (4, 10))]
            R = rr[-1]
            print('D1(%.6f,%.6f) m=%g: V0 (%+.4e, %+.4e)  UD (%+.4e, %+.4e)  V0* (%+.4e, %+.4e)  muE %+.4e muT2 %+.3e | biref V0 %+.3e UD %+.3e V0* %+.3e | GL-change UD %.1e' % (
                b, r, m, R[('V0', 'T2g')], R[('V0', 'Eg')], R[('UD', 'T2g')], R[('UD', 'Eg')], R[('V0*', 'T2g')], R[('V0*', 'Eg')], R['muE'], R['muT2'],
                R[('V0', 'T2g')] - R[('V0', 'Eg')], R[('UD', 'T2g')] - R[('UD', 'Eg')], R[('V0*', 'T2g')] - R[('V0*', 'Eg')],
                max(abs(rr[0][('UD', p)] - R[('UD', p)]) for p in ('T2g', 'Eg'))), flush=True)
        print('%.0fs' % (time.time()-t0))
