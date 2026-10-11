"""V1 (lane RV): real-space decay of the forced O(lambda) momentum correction P1 in the 0<->4 sector,
and (for comparison) of the optional 1<->3 correction (gapped denominator), onsite phi^4 on Z^3.

0<->4 kernel (a-mode basis):   B40(k1..k4) = [sum_l f_x(k_l) / sum_l w(k_l)] * prod_l (2 w(k_l))^(-1/2),  sum k = 0
phi-phi-phi-pi component of P1 (field basis, pi on leg 4): Bppp(k) = [sum_l f_x(k_l)/sum_l w(k_l)] / w(k4)   (up to const)
1/sum w = int_0^inf dt exp(-t sum w)  (t-quadrature exact to <1e-13 on [4m, 4 wmax]).
Real space: K(a1..a4) = sum_n wn sum_y sum_l F_l(y+a_l) prod_{j!=l} G_j(y+a_j)   (FFT, L^3 torus = lattice momentum sum).
"""
import numpy as np, sys, time
L = int(sys.argv[2]) if len(sys.argv) > 2 else 40
m = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
k1 = 2*np.pi*np.fft.fftfreq(L)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
W = np.sqrt(m**2 + 4*np.sin(KX/2)**2 + 4*np.sin(KY/2)**2 + 4*np.sin(KZ/2)**2)
FX = np.sin(KX)
wmax = np.sqrt(m**2 + 12)
def tquad(smin, smax, n=40):
    u, wu = np.polynomial.laguerre.laggauss(n)
    best = None
    for beta in np.linspace(0.3*smin, 3*smin, 60):
        tn, wn = u/beta, wu*np.exp(u)/beta
        s = np.linspace(smin, smax, 3001)
        err = np.max(np.abs((wn[None, :]*np.exp(-np.outer(s, tn))).sum(1)*s - 1))
        if best is None or err < best[0]: best = (err, tn, wn, beta)
    return best
err, tn, wn, beta = tquad(4*m, 4*wmax)
print(f'm={m} L={L}: t-quadrature for 1/s on [{4*m:.3f},{4*wmax:.3f}]: max rel err {err:.2e} (n=40, beta={beta:.3f})')
def ifft(a): return np.fft.ifftn(a)   # g(x) = (1/N) sum_k e^{ikx} a(k)
def legs(variant):
    out = []
    for t in tn:
        e = np.exp(-t*W)
        if variant == 'a':      # a-basis: every leg (2w)^-1/2
            g = e/np.sqrt(2*W); out.append((ifft(g), ifft(FX*g), ifft(g), ifft(FX*g)))
        else:                   # phi phi phi pi: legs 1-3 plain, leg 4 carries 1/w
            out.append((ifft(e), ifft(FX*e), ifft(e/W), ifft(FX*e/W)))
    return out
def kernel(LG, pts):
    tot = 0.0
    for n, (G, F, G4, F4) in enumerate(LG):
        sh = [np.roll(G, shift=tuple(-np.array(p)), axis=(0, 1, 2)) for p in pts[:3]]
        shF = [np.roll(F, shift=tuple(-np.array(p)), axis=(0, 1, 2)) for p in pts[:3]]
        g4 = np.roll(G4, shift=tuple(-np.array(pts[3])), axis=(0, 1, 2)); f4 = np.roll(F4, shift=tuple(-np.array(pts[3])), axis=(0, 1, 2))
        s = shF[0]*sh[1]*sh[2]*g4 + sh[0]*shF[1]*sh[2]*g4 + sh[0]*sh[1]*shF[2]*g4 + sh[0]*sh[1]*sh[2]*f4
        tot += wn[n]*s.sum()
    return tot*L**3   # normalisation irrelevant for decay rates
ex = np.array([1, 0, 0]); exy = np.array([1, 1, 0]); ey = np.array([0, 1, 0]); ez = np.array([0, 0, 1]); o = np.array([0, 0, 0])
configs = {
  'C1 three legs at 0, leg4 at r*x     ': lambda r: [o, o, o, r*ex],
  'C1b three legs at 0, leg1 at r*x    ': lambda r: [r*ex, o, o, o],
  'C2 pairs (0,0) and (r x, r x)       ': lambda r: [o, o, r*ex, r*ex],
  'C3 legs 0, r x, r y, r z            ': lambda r: [o, r*ex, r*ey, r*ez],
  'C4 three legs at 0, leg4 at r*(1,1,0)': lambda r: [o, o, o, r*exy],
}
kap_leg = 2*np.arcsinh(m/2)
print(f'single-leg branch-point rate 2 asinh(m/2) = {kap_leg:.4f} (axis); body-diag per unit |x|_1 differs')
rs = list(range(0, L//2 + 1, 2))
for variant in ['a', 'phi3pi']:
    t0 = time.time(); LG = legs(variant)
    print(f'\n--- variant {variant} ---')
    for name, cf in configs.items():
        vals = np.array([abs(kernel(LG, cf(r))) for r in rs])
        line = ' '.join(f'{v:.2e}' for v in vals)
        # fit rate on the middle range where values well above roundoff
        mask = (np.array(rs) >= 4) & (np.array(rs) <= L//2 - 6) & (vals > 1e-13*vals[0])
        rr = np.array(rs)[mask]; lv = np.log(vals[mask])
        rate = -np.polyfit(rr, lv, 1)[0] if len(rr) >= 3 else np.nan
        # local rates
        loc = -np.diff(np.log(vals + 1e-300))/2
        print(f'{name}: |K|(r=0,2,..,{L//2}) = {line}')
        print(f'      fitted exp. rate (r in [4,{L//2-6}]) = {rate:.4f} per site; local rates {" ".join(f"{x:.3f}" for x in loc)}')
    print(f'[{time.time()-t0:.0f}s]')
