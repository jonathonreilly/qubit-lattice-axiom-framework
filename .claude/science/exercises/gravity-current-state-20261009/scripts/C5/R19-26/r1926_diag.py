"""R19-26 diagnosis at the referee's cut point (ref_cut_check.py:131-163): k2 = (0.4, 1, 0.7), k1 = (0.4 - pi -+ eps, 1, 0.7).
For the R19-16 kernel (unpatched) and the re-placed kernel (lib1926.patch()), per (mu, nu) and per piece-B channel:
  RAW   = max |M_a - M_b|                         (the referee's metric: no placement factor)
  PLACE = max |M_a - (-1)^{2 p_x} M_b|            (the tilde kernel of any local stress at R9-9's placement must obey this)
  on the full 6x6 block and on the physical block P_T(k1) . P_T(k2).
Also: VW spatial alone, tested as a site operator (p = 0: no factor) and as a plaquette operator (p = (e_i+e_j)/2)."""
import numpy as np, lib1926 as R
L = R.L
k2 = np.array([0.4, 1.0, 0.7]); r = 0.1
names = ['0', 'x', 'y', 'z']

def sides(eps):
    xa = float(L.wrap(np.array([0.4 + np.pi - eps]))[0]); xb = float(L.wrap(np.array([0.4 - np.pi + eps]))[0])
    return np.array([xa, 1.0, 0.7]), np.array([xb, 1.0, 0.7])

def channels(k1):
    Msp = L.spatial_VW(k1, k2)
    tot = L.piece_B(k1, k2, Msp); sc = L.piece_B(k1, k2, 0*Msp)
    return dict(total=L.glued(k1, k2, r), scattering=sc, pair=tot - sc), Msp

def report(tag):
    s = R.cut_sign(0)
    for eps in (1e-6, 1e-8):
        ka, kb = sides(eps)
        Ca, Spa = channels(ka); Cb, Spb = channels(kb)
        PTa, PTb, PT2 = L.projs(ka)[4], L.projs(kb)[4], L.projs(k2)[4]
        print('[%s] eps %.0e  q_x(a,b) = %+.10f %+.10f' % (tag, eps, float(L.wrap(ka - k2)[0]), float(L.wrap(kb - k2)[0])))
        for ch in ('total', 'scattering', 'pair'):
            Ma, Mb = Ca[ch], Cb[ch]
            raw = np.abs(Ma - Mb).max(axis=(2, 3)); pl = np.abs(Ma - s[:, :, None, None]*Mb).max(axis=(2, 3))
            plT = np.array([[np.abs(PTa @ Ma[m, n] @ PT2 - s[m, n]*(PTb @ Mb[m, n] @ PT2)).max() for n in range(4)] for m in range(4)])
            worst = np.unravel_index(np.argmax(pl), pl.shape)
            print('   %-10s RAW max %.3e | PLACE max %.3e at M^{%s%s} | PLACE phys-block max %.3e' % (
                ch, raw.max(), pl.max(), names[worst[0]], names[worst[1]], plT.max()))
            if ch == 'total' and eps == 1e-8:
                print('      PLACE phys-block per (mu,nu):\n' + '\n'.join('      ' + ' '.join('%.2e' % plT[m, n] for n in range(4)) for m in range(4)))
                ratio = [np.vdot(Mb[0, 1].ravel(), Ma[0, 1].ravel()).real/max(np.vdot(Mb[0, 1].ravel(), Mb[0, 1].ravel()).real, 1e-300)]
                print('      M^{0x}: <M_b, M_a>/<M_b, M_b> = %+.12f  (a local link operator must give -1)' % ratio[0])
        # VW spatial kernel alone: site placement vs plaquette placement
        site = max(np.abs(Spa[i, j] - Spb[i, j]).max() for i in range(3) for j in range(3))
        plaq = max(np.abs(Spa[i, j] - s[1 + i, 1 + j]*Spb[i, j]).max() for i in range(3) for j in range(3))
        print('   spatial kernel alone: jump as a SITE operator (p=0) %.3e | as a PLAQUETTE operator (p=(e_i+e_j)/2) %.3e' % (site, plaq))

R.unpatch(); report('R19-16 kernel')
R.patch(); report('re-placed kernel')
