"""B1 of CRITERIA.md. A rotation-invariant positive Gaussian potential on a torus, A = a + grad phi, phi linear in a,
with link variance near that of Feynman gauge, matching the pair values and the rectangle T^(k) values of the Wilson tree on an
explicit family. Far fields of size |x|^-2 in gradient form. This tests the role of (B) in Theorem 3.5."""
import numpy as np
from scipy.optimize import least_squares
from wnlib import *
from wn02_rect import square, sigma, tau_path

T = 16
d = 4
D = 1
c3 = 7
ys = square(c3, c3, D)
rng = np.random.default_rng(5)


def rho_xy(x):
    return ((1 - x[1]) % T, x[0] % T)


near_paths = [plaq(y, 0, 1) for y in ys]
Jn = [current(p, T, d) for p in near_paths]
En = [green(J, T, d) for J in Jn]
Pk = [np.sum(Jn[k] * En[(k + 1) % 4]) for k in range(4)]
print("P_k", Pk, flush=True)

# far (3,4)-plaquettes: base positions (x1, x2, x3, x4), taken with their rho orbit; corners disjoint by spacing
base = [(4, 1, c3 + 3, c3 - 1), (5, 2, c3 - 3, c3 + 1), (6, 0, c3 + 1, c3 + 4), (1, 5, c3 - 4, c3 - 3)]
far = []
for b in base:
    xy = (b[0], b[1])
    for r in range(4):
        far.append((xy[0], xy[1], b[2], b[3]))
        xy = rho_xy(xy)
far = list(dict.fromkeys(far))
print("far plaquettes", len(far), flush=True)
far_paths = [plaq(x, 2, 3) for x in far]
Jf = [current(p, T, d) for p in far_paths]
Ef = [green(J, T, d) for J in Jf]

# Wilson tree values
Ktot = {}
Fl = {}
for m, x in enumerate(far[::4]):
    pass
for m, x in enumerate(far):
    fl = sum(incr(Ef[m], sigma(k, ys, D), T).sum() for k in range(4))
    Fl[m] = fl
    for k in range(4):
        kp = (k + 1) % 4
        tau = tau_path(ys[k], x)
        paths = [near_paths[k], lasso(sigma(k, ys, D), near_paths[kp]), lasso(tau, far_paths[m])]
        kc = K_comp(paths, [En[k], En[kp], Ef[m]], T)
        kv = 12 * sumV(En[k], En[kp], Ef[m], T, d)
        Ktot[(k, m)] = (kc, kv, paths)
print("Stk_total / -24Flux at first far:", sum((Ktot[(k,0)][0]+Ktot[(k,0)][1])/Pk[k] for k in range(4)), -24*Fl[0], flush=True)

# unknowns: theta_k on the four corners of each far plaquette (orbit shares values), chi_m at the square corners.
theta = [np.zeros((T,) * d) for _ in range(4)]
chi = [np.zeros((T,) * d) for _ in far]


def corners(x):
    return [tuple(x), tuple(np.array(x) + np.array([0, 0, 1, 0])), tuple(np.array(x) + np.array([0, 0, 1, 1])), tuple(np.array(x) + np.array([0, 0, 0, 1]))]


def levy_inc(e, f):
    return sum(e[s] * f[t] - e[t] * f[s] for s in range(4) for t in range(s + 1, 4))


inplane = [(0, 0), (1, 0), (1, 1), (0, 1)]  # successive images under rho


def lev_sum_coeff(b0):
    """Linear system: unknown chi_0 at (inplane p, y_k), 16 values, and A_l3 target per k (4 values)."""
    rows = []
    rhs = []
    for r in range(4):
        m = b0 + r
        for k in range(4):
            kp = (k + 1) % 4
            paths = Ktot[(k, m)][2]
            kc0 = Ktot[(k, m)][0]
            row = np.zeros(20)
            for p in range(4):
                for ks in range(4):
                    ch = np.zeros((T,) * d)
                    pp = inplane[(p + r) % 4]
                    ch[(pp[0], pp[1], ys[ks][2], ys[ks][3])] = 1.0
                    row[4 * p + ks] = K_comp(paths, [En[k], En[kp], Ef[m] + grad0(ch, d)], T) - kc0
            row[16 + k] = -12.0
            rows.append(row)
            rhs.append(Ktot[(k, m)][1])
    return np.array(rows), np.array(rhs)


for b0, x in enumerate(far):
    if b0 % 4 != 0:
        continue
    A, r = lev_sum_coeff(b0)
    u, res, rk, sv = np.linalg.lstsq(A, r, rcond=1e-10)
    print(f"orbit rep {x}: linear system rank {rk}, residual {np.max(np.abs(A@u-r)):.2e}, K_vert scale {np.max(np.abs(r)):.2e}, |chi| {np.max(np.abs(u[:16])):.2e}", flush=True)
    tar = u[16:]
    for rr in range(4):
        for p in range(4):
            for ks in range(4):
                pp = inplane[(p + rr) % 4]
                chi[b0 + rr][(pp[0], pp[1], ys[ks][2], ys[ks][3])] = u[4 * p + ks]

    def eqs(z):
        th = z.reshape(4, 3)
        out = []
        for k in range(4):
            a = np.r_[0.0, th[k]]
            b = np.r_[0.0, th[(k + 1) % 4]]
            ea = np.array([a[(i + 1) % 4] - a[i] for i in range(4)])
            eb = np.array([b[(i + 1) % 4] - b[i] for i in range(4)])
            out.append(levy_inc(ea, eb) - tar[k])
        return np.array(out) / np.max(np.abs(tar))

    best = None
    s = np.sqrt(np.max(np.abs(tar)))
    for tr in range(40):
        rs = least_squares(eqs, rng.normal(size=12) * s, xtol=1e-15, ftol=1e-15, gtol=1e-15)
        if best is None or np.max(np.abs(rs.fun)) < np.max(np.abs(best.fun)) - 1e-13 or (np.max(np.abs(rs.fun)) < 1e-10 and np.linalg.norm(rs.x) < np.linalg.norm(best.x)):
            best = rs
    z = best.x.reshape(4, 3)
    print(f"   A targets {tar}, solve residual {np.max(np.abs(best.fun)):.2e}, |theta| {np.max(np.abs(z)):.3e}", flush=True)
    for o in range(4):
        y = far[b0 + o]
        cs = corners(y)
        for k in range(4):
            for i in range(1, 4):
                theta[k][tuple(c % T for c in cs[i])] = z[k, i - 1]
            theta[k][tuple(c % T for c in cs[0])] = 0.0

# actual covariance: a ~ G (units 4 g^2), phi = sum_i Theta_i eta_i, eta_i = sum_j (M^-1)_ij <J_j, a>
sources = Jn + Jf
Eall = En + Ef
Theta = theta + chi
n = len(sources)
M = np.array([[np.sum(sources[i] * Eall[j]) for j in range(n)] for i in range(n)])
print("smallest eigenvalue of M", np.linalg.eigvalsh(M)[0], flush=True)
Minv = np.linalg.inv(M)
gradTheta = [grad0(th, d) for th in Theta]


def cprime(J):
    """c' J for arbitrary link function J: Cov(<J, A>, A) with A = a + sum_i grad(Theta_i) eta_i"""
    GJ = green(J, T, d)
    # Cov(eta_i, <J,a>) = sum_j Minv_ij <J_j, G J>
    r = np.array([np.sum(sources[j] * GJ) for j in range(n)])
    w = Minv @ r
    # Cov(<J, A>, A) = G J + sum_i grad(Theta_i) w_i + sum_i <J, grad Theta_i> (G-part of eta_i) + sum <J,grad Theta_i><J..>
    gt = np.array([np.sum(J * g) for g in gradTheta])
    out = GJ + sum(w[i] * gradTheta[i] for i in range(n))
    # eta_i with a: Cov(eta_i, a) = sum_j Minv_ij E_j
    co = Minv @ gt
    out = out + sum(co[j] * Eall[j] for j in range(n))
    # eta_i eta_j covariance is Minv
    out = out + sum((Minv @ gt)[i] * gradTheta[i] for i in range(n))
    return out


# check: E' for each family source, then evaluate K_comp[c'] by Levy areas against the Wilson tree values
Epn = [cprime(J) for J in Jn]
Epf = [cprime(J) for J in Jf]
print("max |c' J_k - (G J_k + grad theta_k)|:", max(np.abs(Epn[k] - En[k] - gradTheta[k]).max() for k in range(4)), flush=True)
worst = 0
scale = 0
for m in range(len(far)):
    for k in range(4):
        kp = (k + 1) % 4
        kc0, kv0, paths = Ktot[(k, m)]
        kcp = K_comp(paths, [Epn[k], Epn[kp], Epf[m]], T)
        worst = max(worst, abs(kcp - kc0 - kv0))
        scale = max(scale, abs(kc0 + kv0), abs(kc0))
print(f"B1 worst |K_comp^(k)[c'] - K_total^(k)| over family = {worst:.3e}; scale of K values {scale:.3e}; rel {worst/scale:.2e}", flush=True)
# compare with the plain Feynman Gaussian
worst0 = max(abs(Ktot[(k, m)][1]) for m in range(len(far)) for k in range(4))
print(f"   for comparison Feynman |K_comp - K_total| max = {worst0:.3e}", flush=True)
# rectangle sum on c'
for m in (0, 4, 8, 12):
    s = sum(K_comp(Ktot[(k, m)][2], [Epn[k], Epn[(k + 1) % 4], Epf[m]], T) / Pk[k] for k in range(4))
    w = sum((Ktot[(k, m)][0] + Ktot[(k, m)][1]) / Pk[k] for k in range(4))
    print(f"   far {far[m]}: sum K_comp[c']/P_k {s:.5e}; Wilson Stk {w:.5e}; -24 Flux {-24*Fl[m]:.5e}", flush=True)
# pair values on the family: conserved currents, unchanged
J_test = [Jn[0], Jn[2], Jf[0], Jf[5], current(lasso(sigma(0, ys, D), near_paths[1]), T, d)]
mx = 0
for a in J_test:
    ca = cprime(a)
    for b in J_test:
        mx = max(mx, abs(np.sum(b * ca) - np.sum(b * green(a, T, d))))
print(f"   pair values: max |<J', c' J> - <J', G J>| = {mx:.2e}", flush=True)
# rotation invariance of c': apply to J and rho J
from wn02_rect import rot_field
Jr = rng.normal(size=(d,) + (T,) * d)
Jr = Jr - green(Jr * 0, T, d)
c1 = rot_field(cprime(Jr), T)
c2 = cprime(rot_field(Jr, T))
print(f"   rotation invariance: max |rho c' J - c' rho J| = {np.abs(c1-c2).max():.2e} (norm {np.abs(c1).max():.2e})", flush=True)
# positivity is by construction: A is a linear function of a Gaussian. Link variance.
lv = 0
G0 = green(current([((0, 0, 0, 0), 0, +1)], T, d), T, d)[0][(0, 0, 0, 0)]
for k_b in [((4, 1, c3 + 3, c3 - 1), 2), ((0, 0, c3, c3), 2), ((0, 0, c3, c3), 0), ((1, 1, c3, c3), 3)]:
    Jb = np.zeros((d,) + (T,) * d)
    Jb[(k_b[1],) + k_b[0]] = 1
    v = np.sum(Jb * cprime(Jb))
    lv = max(lv, v)
    print(f"   link variance at {k_b}: {v:.4f} (Feynman {G0:.4f})", flush=True)
for k in range(4):
    print(f"   (B) norm^2 near-plaquette k={k}: Feynman {np.sum(En[k]**2):.4f}, c' {np.sum(Epn[k]**2):.4f}")
