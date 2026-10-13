"""F3 structural account: split the linear response of the symmetric dressing, d(c, M) = 2 eps (f M, -f.c), into
  L_M : mass part only  (M -> M - 2 eps f.c ; inside the box W = 0 this is a Wilson-like term -2 eps sum_j f_j s_j ~ -2 eps k^2)
  L_c : kinetic part only (c -> c + 2 eps f M ; lives only where W != 0, outside the box |k_j| > b)
(L = L_M + L_c by linearity; each part alone is NOT spectrum-preserving -- diagnostic only), and the mass part further into the
region inside the box (all |k_j| <= b) and outside, via a smooth-free indicator on the evaluation point (diagnostic only)."""
import numpy as np, time
from f3_lib import *
t00 = time.time()
F = Ferm(*ROOT); G = Phot(CPH)
g = mkgrid(ROOT[0], 6, 0.25, 6)
dx, dy, dz = photon_syms(G, g.x)
def cM_part(name, eps, part):
    def cM(kx, ky, kz):
        kx = kx + 0*ky + 0*kz; ky = ky + 0*kx + 0*kz; kz = kz + 0*kx + 0*ky
        c = [F.s(kx), F.s(ky), F.s(kz)]; M = F.W(kx) + F.W(ky) + F.W(kz)
        f = fvec(name, kx, ky, kz)
        fc = f[0]*c[0] + f[1]*c[1] + f[2]*c[2]
        if part in ('M', 'Min', 'Mout'):
            dM = -2*eps*fc
            inside = (np.abs(kx) <= ROOT[0]) & (np.abs(ky) <= ROOT[0]) & (np.abs(kz) <= ROOT[0])
            if part == 'Min': dM = dM*inside
            if part == 'Mout': dM = dM*(~inside)
            M = M + dM
        if part == 'c':
            c = [c[j] + 2*eps*f[j]*M for j in range(3)]
        return c[0], c[1], c[2], M
    return cM
print('split of L (156 nodes, central eps = 1e-3), R18-9 root; per e^2 per unit eps')
for name in ('G1', 'G2'):
    out = {}
    for part in ('M', 'c', 'Min', 'Mout'):
        p = dm_gen(cM_part(name, 1e-3, part), dx, dy, dz, g.x, g.w, parts=True)
        m = dm_gen(cM_part(name, -1e-3, part), dx, dy, dz, g.x, g.w, parts=True)
        out[part] = [(p[i] - m[i])/2e-3 for i in range(3)]
    print('   %s: L_M %+.6e (tad %+.4e, exch %+.4e) ; L_c %+.6e (tad %+.4e, exch %+.4e) ; L_M + L_c %+.6e'
          % (name, *out['M'], *out['c'], out['M'][0] + out['c'][0]))
    print('       L_M inside the box %+.6e ; outside %+.6e (diagnostic indicator split)' % (out['Min'][0], out['Mout'][0]), flush=True)
print('time %.0f s' % (time.time() - t00))
