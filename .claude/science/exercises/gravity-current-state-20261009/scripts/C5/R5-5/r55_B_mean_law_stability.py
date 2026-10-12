"""R5-5 (B): is the ensemble-mean law itself stable? (relevant to the 'ensemble-only law' escape, which collapses to set A)
Mean retarded symbol of R4-1's kernels as a function of z = p^2 (p in the forward tube <=> z in C minus (-inf,0]):
   Bbar(z) = c + sum_m g_m 2 pi sqrt(m) K1(sqrt(z m))/sqrt(z),   g_m = C_m f_m   (R4-1 report :101-112; referee-confirmed)
Growing modes of (Bbar - mu^2) phi = 0  <=>  zeros of h(z) = Bbar(z) - mu^2 in the cut plane (cf. Aslanbeigi-Saravani-Sorkin 2014).
Count zeros by the argument principle on a keyhole contour r<|z|<R, |arg z| < pi - delta. Also list the sign of Bbar on z>0 (the
imaginary-timelike axis p = i kappa u, z = kappa^2), where a real zero is an e^{kappa t} mode.
"""
import numpy as np, sys
from scipy.special import kv
C = np.load(sys.argv[1]); M = 96; mv = np.arange(1, M+1).astype(float); Cm = C[1:M+1]
def finish(g):
    nrm = (np.pi/16)*np.sum(g*mv**2*np.log(mv)); g = -g/nrm; c = -(np.pi/2)*np.sum(g*mv*np.log(mv)); return g, c
def divided_diff(sh):
    g = np.zeros(M)
    for i, mi in enumerate(sh): g[mi-1] = 1.0/np.prod([mi-mj for j, mj in enumerate(sh) if j != i])
    return finish(g)
def smooth_f(L):
    x = mv/L**2; base = np.exp(-x); G = np.stack([base*x**j for j in range(4)], 1)*Cm[:, None]
    A = np.stack([G.T @ mv**k for k in range(3)] + [G.T @ (mv**2*np.log(mv))]); b = np.array([0, 0, 0, -16/np.pi])
    return finish(G @ np.linalg.lstsq(A, b, rcond=None)[0])
def Bbar(z, g, c):
    z = np.asarray(z, complex); sz = np.sqrt(z)
    out = np.full(z.shape, c, complex)
    for m in np.nonzero(g)[0] + 1:
        out += g[m-1]*2*np.pi*np.sqrt(m)*kv(1, sz*np.sqrt(m))/sz
    return out
def winding(g, c, mu2, r=1e-5, R=1e4, delta=1e-7, n=20000):
    th = np.pi - delta
    t = np.linspace(0, 1, n)
    seg = [R*np.exp(1j*(-th + 2*th*t)),                       # outer arc ccw
           np.exp(1j*th)*np.exp(np.log(R) + (np.log(r)-np.log(R))*t),   # upper ray inward
           r*np.exp(1j*(th - 2*th*t)),                         # inner arc cw
           np.exp(-1j*th)*np.exp(np.log(r) + (np.log(R)-np.log(r))*t)]  # lower ray outward
    z = np.concatenate(seg); h = Bbar(z, g, c) - mu2
    ph = np.unwrap(np.angle(h)); return (ph[-1]-ph[0])/(2*np.pi), np.abs(h).min()
kernels = {"4-shell {1,2,3,4}": divided_diff([1, 2, 3, 4]), "4-shell {1,2,4,7}": divided_diff([1, 2, 4, 7]),
           "4-shell {2,3,5,6}": divided_diff([2, 3, 5, 6]), "smooth-f L=2 (all m<=96)": smooth_f(2.0), "smooth-f L=3 (all m<=96)": smooth_f(3.0)}
kap = np.logspace(-3, 2.5, 4000)
for name, (g, c) in kernels.items():
    b = Bbar(kap**2, g, c).real
    print(f"\n== {name}: c = {c:+.4f};  on z = kappa^2 > 0: max Bbar = {b.max():+.4e} at kappa = {kap[b.argmax()]:.3f};"
          f"  Bbar/(-kappa^2) at kappa=0.01,0.1,1: {b[np.searchsorted(kap,0.01)]/(-0.01**2):.4f}, {b[np.searchsorted(kap,0.1)]/(-0.1**2):.4f}, {b[np.searchsorted(kap,1.0)]/(-1.0):.4f}")
    sc = np.nonzero(np.diff(np.sign(b)))[0]
    print(f"   sign changes on the imaginary-timelike axis at kappa ~ {[round(float(kap[i]),4) for i in sc]}")
    for mu2 in (0.0, 1e-4, 1e-2):
        for delta in (1e-6, 1e-3):
            w, hmin = winding(g, c, mu2, delta=delta)
            print(flush=True); print(f"   mu^2 = {mu2:7.1e}, delta = {delta:.0e}: zeros of Bbar - mu^2 in keyhole (1e-5<|z|<1e4) = {w:+.3f}   (min|h| on contour {hmin:.2e})")
