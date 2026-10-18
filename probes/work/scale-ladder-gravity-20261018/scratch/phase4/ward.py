# site-only scalar on Z^4: S = 1/2 sum_cells sqrt(g) g^{mu nu} D_mu phi D_nu phi, g = 1 + h(cell) read by the strain metric.
# Linear coupling c(T).h with T = D phi1 (x) D phi2 - 1/2 delta (D phi1 . D phi2) (sym). Ward: c(T(q))^T L(-q) G_site(-q) = 0 ?
from common import *
def grad_fwd(k):  return np.exp(1j * k) - 1                                   # forward difference at the cell corner
def grad_cell(k):                                                            # cell-averaged (8 parallel edges) gradient
    return np.array([(np.exp(1j * k[m]) - 1) * np.prod([(1 + np.exp(1j * k[n])) / 2 for n in range(4) if n != m]) for m in range(4)])
def shell_kt(ks, grad):
    # on-shell tick momentum for the scalar's own NN action: sum_mu |D_mu|^2-type symbol = 0 (bilinear: D(k).D(-k))
    f = lambda kt: grad(np.array([*ks, kt])) @ grad(-np.array([*ks, kt]))
    x = 1j * np.linalg.norm(ks)
    for _ in range(100):
        h = 1e-7; st = f(x) / ((f(x + h) - f(x - h)) / (2 * h)); x -= st
        if abs(st) < 1e-15: break
    return np.array([*ks, x], complex)
def stress_c(a, b):
    T = 0.5 * (np.outer(a, b) + np.outer(b, a)) - 0.5 * np.eye(4) * (a @ b); return cvec(T)
rng = np.random.default_rng(7); n1, n2 = rng.standard_normal(3), rng.standard_normal(3); n1 /= np.linalg.norm(n1); n2 /= np.linalg.norm(n2)
for nm, grad in (('forward', grad_fwd), ('cell-averaged', grad_cell)):
    prev = None
    for s in (0.2, 0.1, 0.05, 0.025):
        k1 = shell_kt(s * n1, grad); k2 = shell_kt(0.7 * s * n2, grad); q = k2 - k1
        a = grad(-k1); b = grad(k2); c = stress_c(a, b)
        W = strain_metric(Dc, -q) @ Dc.gauge(-q)[:, :4]
        # continuum reference: |c| |W| scale
        r = np.linalg.norm(c @ W) / (np.linalg.norm(c) * np.linalg.norm(W))
        # also continuum conservation of the same tensor with the continuum momentum q
        T = 0.5 * (np.outer(a, b) + np.outer(b, a)) - 0.5 * np.eye(4) * (a @ b); rc = np.linalg.norm(T @ q) / (np.linalg.norm(T) * np.linalg.norm(q))
        print(f"{nm:14s} s={s:.3f}: shell residual {abs(grad(k1)@grad(-k1)):.0e}; Ward ratio {r:.3e}" + (f" (x{prev/r:.2f} on halving)" if prev else "") + f"; continuum q.T ratio {rc:.2e}")
        prev = r
