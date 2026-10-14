"""NT-2 follow-up F2: open 1xL strips (L plaquettes in a row, L-1 interior links, end plaquettes 3 outer links, middle 2).
Point kernel h(Phi) = int prod_k b(e_k) T3(Phi_1 - e_1) prod_{p=2}^{L-1} T2(Phi_p + e_{p-1} - e_p) T3(Phi_L + e_{L-1}).
Smooth B-spline test functions (half-width rho) on a grid of centres in the admissible box (margin 0.05); chain
Nystrom with Gauss-Legendre at two levels. L = 2 at small rho is cross-checked against the exact O12 kernel (o12.py).
Usage: python o1L.py L NGRID [RHO N1 N2]"""
import sys, time, resource, itertools, numpy as np
from scipy.interpolate import BSpline, PPoly
L = int(sys.argv[1]); ng = int(sys.argv[2]); rho = float(sys.argv[3]) if len(sys.argv) > 3 else 0.1
n1 = int(sys.argv[4]) if len(sys.argv) > 4 else 48; n2 = int(sys.argv[5]) if len(sys.argv) > 5 else 64
d = 0.6; w = 2 * d; t0 = time.time()
def boxk(x, k):
    x = np.asarray(x, float); tot = np.zeros_like(x)
    for eps in itertools.product((1, -1), repeat=k):
        s = x + 0.5 * w * sum(eps); tot += np.prod(eps) * np.where(s > 0, s, 0.0) ** (k - 1)
    import math
    return tot / math.factorial(k - 1)
tk = np.linspace(-2 * rho, 2 * rho, 9); Psi = BSpline.basis_element(tk, extrapolate=False); mass = 4 * rho / 8
def Psi_f(y):
    v = Psi(y); return np.where(np.isnan(v), 0.0, v) / mass
gx, gw = np.polynomial.legendre.leggauss(8)
def make(k):
    tb = w * (np.arange(k + 1) - k / 2)  # knots of the k-fold box convolution
    def ex(x):
        out = np.zeros(len(x))
        for i, xv in enumerate(x):
            bps = np.unique(np.clip(np.concatenate([tk, xv - tb]), -2 * rho, 2 * rho)); tot = 0.0
            for lo, hi in zip(bps[:-1], bps[1:]):
                if hi - lo < 1e-15: continue
                y = 0.5 * (hi - lo) * gx + 0.5 * (hi + lo); tot += 0.5 * (hi - lo) * np.dot(gw, boxk(xv - y, k) * Psi_f(y))
            out[i] = tot
        return out
    kn = np.unique(np.concatenate([tk + c for c in tb])); R = k * d + 2 * rho
    kn = np.concatenate([[-R - 1], kn, [R + 1]]); C = np.zeros((10, len(kn) - 1))
    for j, (lo, hi) in enumerate(zip(kn[:-1], kn[1:])):
        xs = lo + (hi - lo) * (1 - np.cos(np.pi * (np.arange(10) + 0.5) / 10)) / 2; ys = ex(xs)
        C[:, j] = np.polyfit(xs - lo, ys, 9) if np.abs(ys).max() > 0 else 0
    pp = PPoly(C, kn, extrapolate=False)
    return lambda x: np.nan_to_num(pp(x)), ex
f3, ex3 = make(3); f2, _ = make(2)
xs = np.linspace(-2.2, 2.2, 301); print("PPoly check T3*Psi:", np.abs(f3(xs) - ex3(xs)).max(), flush=True)
def hval(D, n):
    y, wt = np.polynomial.legendre.leggauss(n); y = d * y; wt = d * wt
    v = wt * f3(D[0] - y)                              # over e_1
    for p in range(1, L - 1):
        v = (v @ f2(D[p] + y[:, None] - y[None, :])) * wt   # e_{p} -> e_{p+1}
    return float(v @ f3(D[L - 1] + y))
a = d - 0.05 - rho; ax = np.linspace(-a, a, ng); step = ax[1] - ax[0]
offs = list(itertools.product(range(-(ng - 1), ng), repeat=L))
H = {n: {o: hval(np.array(o) * step, n) for o in offs} for n in (n1, n2)}
idx = list(itertools.product(range(ng), repeat=L)); k = len(idx)
Q = {n: np.array([[H[n][tuple(pi - qi for pi, qi in zip(p, q))] for q in idx] for p in idx]) for n in (n1, n2)}
e1 = np.linalg.eigvalsh(Q[n1]); e2 = np.linalg.eigvalsh(Q[n2]); E = k * np.abs(Q[n1] - Q[n2]).max() + k * 1e-15 * e2[-1]
print(f"RESULT O1{L} ng={ng} ({k} smooth test fns, rho={rho}): lam_min {e2[0]:+.4e} (n1: {e1[0]:+.4e}) lam_max {e2[-1]:.4e} rel {e2[0]/e2[-1]:+.3e} "
      f"| E {E:.1e} | neg-converged {e2[0] < -10*E and e2[0]/e2[-1] < -1e-9} | {time.time()-t0:.1f}s RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f}MB")
if L == 2 and rho <= 0.02:
    sys.argv = ['o12.py', 'grid', '2']; src = open('o12.py').read().split("t0 = time.time()")[0]; exec(src)
    C2 = np.array([(x, y) for x in ax for y in ax])
    Kp = np.array([[h_exact(*(p - q)) for q in C2] for p in C2])
    print(f"  L=2 cross-check vs exact point kernel (rho -> 0): max|Q - K_point| {np.abs(Q[n2] - Kp).max():.2e} (max K {Kp.max():.3f}); point lam_min {np.linalg.eigvalsh(Kp)[0]:+.4e}")
