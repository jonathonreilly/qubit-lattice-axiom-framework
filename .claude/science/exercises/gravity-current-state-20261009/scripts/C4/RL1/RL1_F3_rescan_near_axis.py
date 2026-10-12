"""RL1 (F3): re-scan the 5- and 6-layer local operator families with a contour that reaches the imaginary axis
(Re z from 0.003, |Im z| <= 60), exact in-script coefficients (moment constraints to machine precision; normalised at z = 1e-3,
which puts an artificial real zero at z ~ 1e-3 < 0.003, outside the contour).  Then locate the zeros of the best member."""
import numpy as np
from scipy.special import kv, gammaln
exec(open("RL1_E_layer_family_scan.py").read().split('if __name__ == "__main__":')[0])
def cont(x0, x1, y, n):
    return np.concatenate([x0+1j*np.linspace(-y, y, 4*n), np.linspace(x0, x1, n)+1j*y,
                           x1+1j*np.linspace(y, -y, 4*n), np.linspace(x1, x0, n)-1j*y])
pathA = cont(0.003, 20.0, 60.0, 3000)        # whole right half-plane box
pathS = cont(0.003, 0.03, 60.0, 3000)        # near-axis strip
for L in [4, 5, 6]:
    Fb = basis(L)
    A_ = np.array([[np.exp(gammaln(n+(k+1)/2) - gammaln(n+1)) for n in range(L)] for k in range(3)])
    null = np.linalg.svd(A_)[2][3:]
    TA = trans(Fb, pathA); TS = trans(Fb, pathS); T0 = trans(Fb, np.array([1e-3]))[0]
    if L == 4: params = [np.array([1.0])]
    elif L == 5: params = [np.array([np.cos(t), np.sin(t)]) for t in np.linspace(0, np.pi, 721)[:-1]]
    else: params = [np.array([np.cos(t), np.sin(t)*np.cos(p), np.sin(t)*np.sin(p)])
                    for t in np.linspace(0, np.pi, 91) for p in np.linspace(0, 2*np.pi, 181)[:-1]]
    nst = 0; tot = 0; hist = {}
    for q in params:
        C = q @ null; f0 = (T0 @ C).real
        if abs(f0) < 1e-6: continue
        C = C/f0; tot += 1
        def cnt(T):
            ph = np.unwrap(np.angle(T @ C - 1.0)); return -int(round((ph[-1]-ph[0])/(2*np.pi)))
        nA = cnt(TA); nS = cnt(TS); hist[(nA, nS)] = hist.get((nA, nS), 0) + 1
        if nA == 0: nst += 1
    print("L=%d: members=%d  stable in [0.003,20]x[-60,60]: %d   histogram {(#zeros box, #zeros near-axis strip): count}: %s"
          % (L, tot, nst, dict(sorted(hist.items()))))
