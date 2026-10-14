"""NT-2 O22 RP test with smooth (B-spline) gauge-invariant test functions; quadratic-form matrix at two Nystrom levels.
Usage: python o22_rp.py MODE NGRID [RHO N1 N2]
 MODE grid  : centres on {-a..a}^4 grid (NGRID per axis), a = delta - 0.05 - rho (test functions supported in the
              admissible box with margin 0.05)
 MODE unres : power reference R1, centres on an NGRID^4 grid of the full plaquette torus (NOT admissible); spectrum
              by 4D FFT of the (wrapped) difference table (block-circulant matrix)."""
import sys, time, resource, itertools, numpy as np
from o22lib import *
mode = sys.argv[1]; ng = int(sys.argv[2]); rho = float(sys.argv[3]) if len(sys.argv) > 3 else 0.1
n1 = int(sys.argv[4]) if len(sys.argv) > 4 else 48; n2 = int(sys.argv[5]) if len(sys.argv) > 5 else 64
d = 0.6; t0 = time.time()
f, _ = make_TPsi(d, rho)
def table(offsets_list, n):
    y, w = np.polynomial.legendre.leggauss(n); y = d * y; w = d * w
    return np.array([h_smooth(np.array(D), f, y, w) for D in offsets_list])
if mode == 'grid':
    a = d - 0.05 - rho; ax = np.linspace(-a, a, ng); C = np.array(list(itertools.product(ax, repeat=4)))
    step = ax[1] - ax[0]
    offs = list(itertools.product(range(-(ng - 1), ng), repeat=4))
    H1 = dict(zip(offs, table([np.array(o) * step for o in offs], n1)))
    H2 = dict(zip(offs, table([np.array(o) * step for o in offs], n2)))
    idx = list(itertools.product(range(ng), repeat=4)); k = len(idx)
    Q1 = np.zeros((k, k)); Q2 = np.zeros((k, k))
    for i, p in enumerate(idx):
        for j, q in enumerate(idx):
            o = tuple(pi - qi for pi, qi in zip(p, q)); Q1[i, j] = H1[o]; Q2[i, j] = H2[o]
    e1 = np.linalg.eigvalsh(Q1); e2, V = np.linalg.eigh(Q2)
    E = k * np.abs(Q1 - Q2).max() + k * 1e-15 * np.abs(Q2).max()
    print(f"RESULT O22 grid ng={ng} ({k} smooth test functions, rho={rho}, centres |c|<={a:.3f}): lam_min(n={n2}) {e2[0]:+.4e} "
          f"(n={n1}: {e1[0]:+.4e}) lam_max {e2[-1]:.4e} rel {e2[0]/e2[-1]:+.3e} | E {E:.1e} | neg-converged {e2[0] < -10*E and e2[0]/e2[-1] < -1e-9} "
          f"| support max|phi| {a+rho:.3f} | {time.time()-t0:.1f}s RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f}MB")
    v = V[:, 0].reshape((ng,) * 4)
    print("  negative eigenvector: antisymmetry under p1<->p2 swap:", np.abs(v + v.transpose(1, 0, 2, 3)).max() / np.abs(v).max(),
          " under p1<->p3:", np.abs(v + v.transpose(2, 1, 0, 3)).max() / np.abs(v).max())
else:
    N = ng; st = 2 * np.pi / N
    offs = list(itertools.product(range(N), repeat=4))
    def wr(o): return ((np.array(o) * st + np.pi) % (2 * np.pi)) - np.pi
    res = {}
    for n in (n1, n2):
        y, w = np.polynomial.legendre.leggauss(n); y = d * y; w = d * w
        T = np.zeros((N,) * 4)
        for o in offs:
            D = wr(o)
            if np.all(np.abs(D) < 4 * d + 4 * rho):
                T[o] = h_smooth(D, f, y, w)
        lam = np.real(np.fft.fftn(T)); res[n] = (lam, T)
    lam = res[n2][0]; E = np.abs(res[n1][1] - res[n2][1]).sum() + 1e-15 * N ** 4 * np.abs(lam).max()
    km = np.unravel_index(np.argmin(lam), lam.shape)
    print(f"RESULT O22 unres N={N} (R1 power reference, rho={rho}): lam_min {lam.min():+.4e} at k={km} lam_max {lam.max():.4e} rel {lam.min()/lam.max():+.3e} "
          f"| E {E:.1e} | neg-converged {lam.min() < -10*E} | {time.time()-t0:.1f}s RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f}MB")
