"""C5 R13-5 check: L edge at small mass. L has doublers at k = pi (u(pi) = 0) with A_zz ~ -2 dk^2 there, so
I(B) = int A_zz (B+u)^{-5/2} dk_z ~ -4/(3B) + O(1) as B -> 0 (proved asymptotics: int x^2 (B+x^2)^{-5/2} dx = 2/(3B)).
Fine 1D quadrature of I(B), then Xi_boxperp and the U/M totals by a k_perp grid x fine k_z quadrature (no subtraction).
"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r99_profiles_copy import profile, B as BOX
kz = np.linspace(-np.pi, np.pi, 400001)[:-1]; dk = kz[1]-kz[0]
for name in ['L', 'G']:
    u, up, upp = profile(name, kz); A = upp/2 - 1
    I = lambda Bv: np.sum(A/(Bv+u)**2.5)*dk
    print(name, 'I(B):', ' '.join('B=%.0e: %+.3e' % (b, I(b)) for b in [1e-4, 1e-3, 1e-2, 3e-2, 0.09, 0.3, 1.0]))
    if name == 'L':
        bs = np.logspace(-4, 0, 400); Iv = np.array([I(b) for b in bs])
        print('   L: I(B) changes sign at B ~ %.4f (I<0 below)' % bs[np.argmax(Iv > 0)])
# Xi for L at m = 0.3, 0.1, 0.01: k_perp grid N=256, I(B) by interpolation on a log grid
name = 'L'
u, up, upp = profile(name, kz); A = upp/2 - 1
lb = np.logspace(-5, np.log10(40), 3000); Ib = np.array([np.sum(A/(b+u)**2.5)*dk for b in lb])
Ifun = lambda Bv: np.interp(np.log(Bv), np.log(lb), Ib)
N = 256; k = 2*np.pi*(np.arange(N)-N//2)/N
uk, upk, _ = profile(name, k); pk = upk/2
ux, uy = uk[:, None], uk[None, :]; px, py = pk[:, None], pk[None, :]
bp = (np.abs(k)[:, None] <= BOX) & (np.abs(k)[None, :] <= BOX)
kx, ky = k[:, None], k[None, :]
for m in [0.3, 0.1, 0.01]:
    Iv = Ifun(m*m + ux + uy)
    f = lambda V: np.mean(V*Iv)/(2*np.pi)/32
    for pol, Vc, VU, VM in [('T2g', 4*kx**2*ky**2, 4*px**2*py**2, 4*ux*uy), ('Eg', (kx**2-ky**2)**2, (px**2-py**2)**2, (ux-uy)**2)]:
        print('L m=%.2f %-3s: Xi_boxperp=%+.4e | U total %+.4e | M total %+.4e | min I on edge-perp B values %+.2e' %
              (m, pol, f(Vc*bp), f(VU), f(VM), Iv[~bp].min()))
