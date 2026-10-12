"""R13-4 (iii): d = 2 (R9-5's dimension) leakage outside the c = 1 cone for the R7-1/R9-5 box law
(b=2.0, b2=3.1, m=0.3) and the subluminal box (b=1.4), by FFT on an N x N torus (N = 2048 > 2 v_max t).
Subtraction as r134_cone.py: D_cont = 0 for r > t.  Reports max |D| on annuli r/t in [1.2,1.3] and
x = r - t windows, and t*|D| (stationary phase predicts t^{-d/2} = t^{-1} inside the superluminal window)."""
import numpy as np
def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def s_box(k, b=2.0, b2=3.1):
    r = sstep((b2 - np.abs(k))/(b2 - b)); return r*k + (1-r)*np.sin(k)
def s_sub(k, b=1.4, n=2**16):
    q = np.linspace(0, np.pi, n+1); sig = 1 - 2*sstep((q - b)/(np.pi - 2*b))
    sv = np.concatenate([[0], np.cumsum(0.5*(sig[1:] + sig[:-1])*np.diff(q))])
    return np.sign(k)*np.interp(np.abs(k), q, sv)
N = 2048
k = 2*np.pi*np.fft.fftfreq(N); k = np.where(k >= np.pi, k - 2*np.pi, k)
X = np.fft.fftfreq(N, d=1.0/N); R = np.sqrt(X[:, None]**2 + X[None, :]**2)
out = []
for name, sf in [("R7-1/R9-5 box b=2", s_box), ("subluminal box b=1.4", s_sub)]:
    S1 = sf(k); E = np.sqrt(0.09 + S1[:, None]**2 + S1[None, :]**2)
    for t in [50, 100, 200]:
        D = np.real(np.fft.ifft2(np.sin(E*t)/E))
        ann = np.abs(D[(R >= 1.2*t) & (R <= 1.3*t)]).max()
        xs = [5, 20, 80, 160, 320]
        win = [np.abs(D[(R >= t + x) & (R < t + x + 4)]).max() for x in xs]
        line = (f"{name:22s} t={t:3d}: max|D| on r/t in [1.2,1.3] = {ann:.3e} (t*|D| = {t*ann:.3f}); "
                f"x=r-t {xs}: " + " ".join(f"{w:.1e}" for w in win))
        print(line, flush=True); out.append(line)
open(__file__.replace('.py', '.out'), 'w').write("\n".join(out) + "\n")
