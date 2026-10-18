import sys, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
from d4e import on_shell, C
def svn(k):
    s = np.sort(np.linalg.svd(C.Q(k), compute_uv=False)); return s/s[-1]
def golden(f, lo, hi):
    gr = (5**.5-1)/2; a, b = lo, hi; c, d = b-gr*(b-a), a+gr*(b-a); fc, fd = f(c), f(d)
    for _ in range(120):
        if fc < fd: b, d, fd = d, c, fc; c = b-gr*(b-a); fc = f(c)
        else: a, c, fc = c, d, fd; d = a+gr*(b-a); fd = f(d)
        if b-a < 1e-14: break
    return (a+b)/2
for name, n in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n)
    for km in (0.2, 0.1):
        ks = km*n
        oms = np.linspace(0.9*km, 1.05*km, 120); f32 = [svn(np.array([*ks, 1j*o]))[32] for o in oms]; f33 = [svn(np.array([*ks, 1j*o]))[33] for o in oms]
        i32, i33 = int(np.argmin(f32)), int(np.argmin(f33))
        w1 = golden(lambda o: svn(np.array([*ks, 1j*o]))[32], oms[max(i32-2,0)], oms[min(i32+2,119)])
        w2 = golden(lambda o: svn(np.array([*ks, 1j*o]))[33], oms[max(i33-2,0)], oms[min(i33+2,119)])
        s1, s2 = svn(np.array([*ks, 1j*w1])), svn(np.array([*ks, 1j*w2]))
        kS, _, _ = on_shell(ks, 1j*km)
        print(f"{name} |k|={km}: graviton w/k = {w1/km:.6f}, {w2/km:.6f} (sv33,34 at roots {s1[32]:.0e},{s2[33]:.0e}); scalar w/k = {abs(kS[3])/km:.6f}; alpha_g {(w1**2/km**2-1)/km**2:+.4f} {(w2**2/km**2-1)/km**2:+.4f} alpha_s {(abs(kS[3])**2/km**2-1)/km**2:+.4f}")
