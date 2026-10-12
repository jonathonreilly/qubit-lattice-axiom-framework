"""R5-5 (B2): locate the cut-plane zeros of the mean symbol found in (B); growth rate of the corresponding mode.
In w = sqrt(z) (Re w > 0), a zero w0 gives a rest-frame mode e^{-i omega t} with omega = i w0: growth rate Re(w0) per lattice time.
Also re-count zeros with a larger outer radius (R = 1e6) for the smooth kernels (check the count is not an R artefact)."""
import numpy as np, sys
from scipy.special import kv
from scipy.optimize import root
exec(open('r55_B_mean_law_stability.py').read().split("kap = np.logspace")[0].split('"""', 2)[2])
def hw(w, g, c, mu2=0.0): return Bbar(np.asarray(w, complex)**2, g, c) - mu2
for name in ("4-shell {1,2,3,4}", "4-shell {1,2,4,7}", "4-shell {2,3,5,6}"):
    g, c = kernels[name]
    X, Y = np.meshgrid(np.linspace(0.02, 12, 600), np.linspace(-12, 12, 1200))
    W = X + 1j*Y; H = np.abs(hw(W, g, c))
    cand = []
    for i in range(1, H.shape[0]-1):
        for j in range(1, H.shape[1]-1):
            if H[i, j] <= H[i-1:i+2, j-1:j+2].min() and H[i, j] < 0.5:
                cand.append(W[i, j])
    zeros = []
    for w0 in cand:
        sol = root(lambda v: [hw(v[0]+1j*v[1], g, c).real, hw(v[0]+1j*v[1], g, c).imag], [w0.real, w0.imag], tol=1e-13)
        w = sol.x[0] + 1j*sol.x[1]
        if sol.success and abs(hw(w, g, c)) < 1e-9 and w.real > 0 and not any(abs(w - z) < 1e-6 for z in zeros):
            zeros.append(w)
    zeros.sort(key=lambda w: -w.real)
    print(f"\n== {name}: {len(zeros)} zeros found in w=sqrt(z), 0<Re w<12, |Im w|<12 (keyhole count from (B) applies to |z|<1e4)")
    for w in zeros:
        print(f"   w0 = {w.real:+.5f} {w.imag:+.5f}i   z0 = {(w*w).real:+.4f} {(w*w).imag:+.4f}i   growth rate Re w0 = {w.real:.4f}/a  (e-fold time {1/w.real:.2f} a)")
for name in ("smooth-f L=2 (all m<=96)", "smooth-f L=3 (all m<=96)"):
    g, c = kernels[name]
    for R in (1e4, 1e6):
        wnum, hmin = winding(g, c, 0.0, R=R, delta=1e-4)
        print(f"\n== {name}: zeros of Bbar in keyhole 1e-5<|z|<{R:.0e}: {wnum:+.3f} (min|h| {hmin:.2e})")
