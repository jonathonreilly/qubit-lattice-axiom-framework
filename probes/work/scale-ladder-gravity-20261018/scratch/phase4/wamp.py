# physical size of the Ward violation: gauge-fixing (lambda) dependence of the on-shell scalar-scalar exchange
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from common import *
    from ward import grad_fwd, grad_cell, shell_kt, stress_c
rng = np.random.default_rng(11); dirs = [rng.standard_normal(3) for _ in range(4)]; dirs = [d / np.linalg.norm(d) for d in dirs]
def amp(q, c1, c2, lam):
    G, Gm = Dc.gauge(q), Dc.gauge(-q)
    Qgf = Dc.Q(q) + lam * G @ Gm.T
    return c2 @ strain_metric(Dc, q) @ np.linalg.solve(Qgf, strain_metric(Dc, -q).T @ c1)
def Tm(c):
    return T_of_c(c)
for nm, grad in (('forward', grad_fwd), ('cell-averaged', grad_cell)):
    for s in (0.2, 0.1, 0.05):
        # source 1: phi_a(-k1) phi_b(k2), momentum q = k2 - k1 ; source 2: momentum -q from phi_c(k1') ... choose k3 - k4 = -q
        k1 = shell_kt(s * dirs[0], grad); k2 = shell_kt(0.8 * s * dirs[1], grad); q = k2 - k1
        k3 = shell_kt(0.9 * s * dirs[2], grad); k4 = k3 + q                               # k4 = k3 + q must be on shell: solve its tick part
        k4 = shell_kt(k4[:3].real, grad) if False else None
        # simpler: second source = the reversed pair (phi(-k2) phi(k1)) at momentum -q
        c1 = stress_c(grad(-k1), grad(k2)); c2 = stress_c(grad(-k2), grad(k1))
        A1, A10 = amp(q, c1, c2, 1.0), amp(q, c1, c2, 10.0)
        T1, T2 = Tm(c1), Tm(c2); qq = q @ q
        gr = -4 * (np.sum(T1 * T2) - 0.5 * np.trace(T1) * np.trace(T2)) / qq
        print(f"{nm:14s} s={s:.2f}: |q^2|={abs(qq):.1e} A(lam=1) {A1:.4e}  lam-dependence {abs(A10-A1)/abs(A1):.1e}  vs GR formula {abs(A1-gr)/abs(gr):.1e}")
