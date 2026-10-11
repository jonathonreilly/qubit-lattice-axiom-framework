"""V3 (a): real-space decay of one leg of the forced 0<->4 staggered dressing kernel.
Every leg is a matrix function of h: P_pm/(omega+S) and f*P_pm/(omega+S) with S >= 3m (other three legs), and
g(h) = a(omega) + b(omega) h with omega = sqrt(m^2 + sum sin^2 p) a full-zone scalar symbol (h^2 = omega^2).
So the leg decays like the Fourier transforms of a = 1/(2(omega+S)), b = 1/(2 omega (omega+S)) and of f*a, f*b
(f = 1/2 sin 2p_x). Branch point of omega at sin p = i m -> expected rate asinh(m) per site."""
import numpy as np
L = 96
p = 2*np.pi*np.fft.fftfreq(L)
PX, PY, PZ = np.meshgrid(p, p, p, indexing='ij')
for m in [0.3, 0.5, 1.0]:
    w = np.sqrt(m*m + np.sin(PX)**2 + np.sin(PY)**2 + np.sin(PZ)**2)
    S = 3*m
    f = 0.5*np.sin(2*PX)
    out = []
    for lab, sym in [('a', 1/(2*(w+S))), ('b', 1/(2*w*(w+S))), ('f a', f/(2*(w+S))), ('f b', f/(2*w*(w+S)))]:
        g = np.fft.ifftn(sym)
        # along x (even and odd sites separately: staggered symbols are pi-periodic in p for a,b -> support on even r)
        r = np.arange(2, 30, 2)   # pi-periodic symbols: support on even r only (odd r are 1e-17 noise)
        v = np.abs(g[r, 0, 0])
        nz = v > 1e-300
        rr = r[nz]; lv = np.log(v[nz])
        sel = (rr >= 14) & (rr <= 26)
        rate = -np.polyfit(rr[sel], lv[sel], 1)[0] if sel.sum() > 2 else float('nan')
        out.append(f'{lab}: |g|(r=4,8,16,24)=' + ','.join(f'{abs(g[i,0,0]):.1e}' for i in [4, 8, 16, 24]) + f' rate {rate:.3f}')
    print(f'm={m}: asinh(m)={np.arcsinh(m):.3f} | ' + ' | '.join(out))
