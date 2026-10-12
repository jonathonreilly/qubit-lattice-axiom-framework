"""C5 R13-5: dependence of the G-edge class floor on the size b' of the region where the TT vertex is fixed to the
continuum (b' = B = 2: full box; b' = 1.6: R8-2's chi_1 gluing region; b' = 1.0). Fine k_z quadrature, k_perp N = 256.
No subtraction. On G, I(B) < 0 for all B (A_zz <= 0, proved), so any b' > 0 gives a strictly negative floor."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r99_profiles_copy import profile
kz = np.linspace(-np.pi, np.pi, 200001)[:-1]; dk = kz[1]-kz[0]
u, up, upp = profile('G', kz); A = upp/2 - 1
lb = np.logspace(-5, np.log10(40), 2000); Ib = np.array([np.sum(A/(b+u)**2.5)*dk for b in lb])
N = 256; k = 2*np.pi*(np.arange(N)-N//2)/N
uk = profile('G', k)[0]; kx, ky = k[:, None], k[None, :]
for m in [1.0, 0.3, 0.01]:
    Iv = np.interp(np.log(m*m + uk[:, None] + uk[None, :]), np.log(lb), Ib)
    out = []
    for bp in [2.0, 1.6, 1.0]:
        msk = (np.abs(kx) <= bp) & (np.abs(ky) <= bp)
        xT = np.mean(4*kx**2*ky**2*msk*Iv)/(2*np.pi)/32; xE = np.mean((kx**2-ky**2)**2*msk*Iv)/(2*np.pi)/32
        out.append("b'=%.1f: T2g %+.3e Eg %+.3e (at a=l_P: %.2e, %.2e)" % (bp, xT, xE, 8*np.pi*abs(xT), 8*np.pi*abs(xE)))
    print('G m=%.2f | ' % m + ' | '.join(out))
