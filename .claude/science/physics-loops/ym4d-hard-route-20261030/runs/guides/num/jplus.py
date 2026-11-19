# Guide only: importance-sampling estimate of J_+(s) = int_{SU(2)^4} exp(-s sum_{i<j} a([h_i,h_j])) dh,
# with a([h,k]) = 2|u x v|^2 (vector parts). Compares s^3 J_+(s) with kappa*log(s), kappa = I_b/(2 pi^4),
# I_b = int_{[-1,1]^3} (1+|b|^2)^(-2) db (the scaling-limit coefficient), and with the 1D reduction R(s).
import numpy as np, sys
rng = np.random.default_rng(12345)

def cross_sq(a, b):
    c = np.cross(a, b)
    return np.einsum('...i,...i->...', c, c)

def psi(r, s, N):
    # E over u_2..u_4 with |u_j|<=r, u_1 = r z-hat; returns integral of prod_j [1_{|u_j|<=r} d^3u_j/(pi^2 sqrt(1-|u_j|^2))] exp(-2s sum_{i<j}|u_i x u_j|^2)
    tau2 = min(1.0/(4*s*r*r), r*r)
    alpha = rng.uniform(-r, r, size=(N, 3))
    v = rng.normal(0.0, np.sqrt(tau2), size=(N, 3, 2))
    u = np.empty((N, 3, 3)); u[..., 0] = v[..., 0]; u[..., 1] = v[..., 1]; u[..., 2] = alpha
    nu2 = np.einsum('nji,nji->nj', u, u)
    ok = nu2 <= r*r
    vv = v[..., 0]**2 + v[..., 1]**2
    # weight per j: 1/(pi^2 sqrt(1-|u|^2)) * exp(-2 s r^2 |v|^2) / q,  q = (1/(2r)) (1/(2 pi tau2)) exp(-|v|^2/(2 tau2))
    logw = np.log(4*np.pi*r*tau2) - 2*np.log(np.pi) - 0.5*np.log1p(-np.minimum(nu2, 1-1e-15)) + (-2*s*r*r + 1.0/(2*tau2))*vv
    logw = np.where(ok, logw, -np.inf).sum(axis=1)
    e = cross_sq(u[:, 0], u[:, 1]) + cross_sq(u[:, 0], u[:, 2]) + cross_sq(u[:, 1], u[:, 2])
    vals = np.exp(logw - 2*s*e)
    return vals.mean(), vals.std()/np.sqrt(N)

def J(s, N=40000, nlog=48, nhi=24):
    # r in [rmin, 1/2]: Gauss-Legendre in l = -log r ; r in [1/2, 1): r = sin(theta)
    tot = 0.0; var = 0.0
    lmin, lmax = np.log(2.0), np.log(2.0) + 0.25*np.log(s) + 8.0
    x, wq = np.polynomial.legendre.leggauss(nlog)
    for xi, wi in zip(x, wq):
        l = 0.5*(lmax-lmin)*xi + 0.5*(lmax+lmin); r = np.exp(-l)
        jac = 0.5*(lmax-lmin) * 4*r**3/(np.pi*np.sqrt(1-r*r))
        m, se = psi(r, s, N); tot += wi*jac*m; var += (wi*jac*se)**2
    x, wq = np.polynomial.legendre.leggauss(nhi)
    t0, t1 = np.arcsin(0.5), np.pi/2
    for xi, wi in zip(x, wq):
        th = 0.5*(t1-t0)*xi + 0.5*(t1+t0); r = np.sin(th)
        jac = 0.5*(t1-t0) * 4*np.sin(th)**2/np.pi
        m, se = psi(min(r, 1-1e-12), s, N); tot += wi*jac*m; var += (wi*jac*se)**2
    return 4*tot, 4*np.sqrt(var)

def R(s, n=4000):
    th = np.linspace(0, np.pi/2, n+1)[1:-1]; r = np.sin(th)
    f = r**11/(1+s*r**4)**3  # dr/sqrt(1-r^2) = dtheta
    return np.trapz(f, th)

g = np.polynomial.legendre.leggauss(60)
xb = g[0]; wb = g[1]
B1, B2, B3 = np.meshgrid(xb, xb, xb, indexing='ij'); W = np.einsum('i,j,k->ijk', wb, wb, wb)
Ib = float((W/(1+B1**2+B2**2+B3**2)**2).sum())
kappa = Ib/(2*np.pi**4)
print(f"I_b = {Ib:.6f}, kappa = I_b/(2 pi^4) = {kappa:.6e}")
rows = []
for s in [1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8]:
    j, se = J(s)
    rows.append((s, j, se))
    print(f"s={s:.0e}  J+={j:.4e} (se {se:.1e})  s^3 J+={s**3*j:.5e}  kappa*log s={kappa*np.log(s):.5e}  J+/R={j/R(s):.4f}", flush=True)
ls = np.log([r[0] for r in rows]); ys = np.array([r[0]**3*r[1] for r in rows])
A = np.vstack([ls, np.ones_like(ls)]).T
slope, icpt = np.linalg.lstsq(A[3:], ys[3:], rcond=None)[0]
print(f"fit of s^3 J+ on log s over s>=1e5: slope={slope:.5e} (kappa {kappa:.5e}), intercept={icpt:.4e}")
