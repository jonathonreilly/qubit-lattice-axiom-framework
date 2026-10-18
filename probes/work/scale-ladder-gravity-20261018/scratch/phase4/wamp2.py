import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from common import *
    from ward import grad_fwd, grad_cell, shell_kt, stress_c
rng = np.random.default_rng(11); dirs = [rng.standard_normal(3) for _ in range(4)]; dirs = [d / np.linalg.norm(d) for d in dirs]
def shell_f(k, grad): return grad(k) @ grad(-k)
T0 = 0.1
def pair_at(q, s, grad, d, e):
    """k3 = (s d + t e, k3_t on shell), with k4 = k3 - q also on shell: Newton in complex t."""
    def F(t):
        k3 = shell_kt(s * d + t * e, grad); return shell_f(k3 - q, grad), k3
    t = T0 * s
    for _ in range(60):
        f, _ = F(t); h = 1e-7; df = (F(t + h)[0] - F(t - h)[0]) / (2 * h); st = f / df; t -= st
        if abs(st) < 1e-15: break
    _, k3 = F(t); return k3, k3 - q
def amp(q, c1, c2, lam):
    G, Gm = Dc.gauge(q), Dc.gauge(-q)
    return c2 @ strain_metric(Dc, q) @ np.linalg.solve(Dc.Q(q) + lam * G @ Gm.T, strain_metric(Dc, -q).T @ c1)
for nm, grad in (('forward', grad_fwd), ('cell-averaged', grad_cell)):
    for s in (0.2, 0.1, 0.05):
        k1 = shell_kt(s * dirs[0], grad); k2 = shell_kt(0.8 * s * dirs[1], grad); q = k2 - k1
        k3, k4 = pair_at(q, 0.9 * s, grad, dirs[2], dirs[3])
        if not (abs(shell_f(k4, grad)) < 1e-12 and abs(shell_f(k3, grad)) < 1e-12):
            for T0 in (0.5, -0.5, 1.0, -1.0, 0.3j, -0.3j):
                globals()["T0"] = T0; k3, k4 = pair_at(q, 0.9 * s, grad, dirs[2], dirs[3])
                if abs(shell_f(k4, grad)) < 1e-12: break
            globals()["T0"] = 0.1
        assert abs(shell_f(k4, grad)) < 1e-12, abs(shell_f(k4, grad))
        c1 = stress_c(grad(-k1), grad(k2)); c2 = stress_c(grad(-k3), grad(k4))          # momenta q and -q
        W1 = strain_metric(Dc, -q) @ Dc.gauge(-q)[:, :4]; W2 = strain_metric(Dc, q) @ Dc.gauge(q)[:, :4]
        e1 = np.linalg.norm(c1 @ W1) / (np.linalg.norm(c1) * np.linalg.norm(W1)); e2 = np.linalg.norm(c2 @ W2) / (np.linalg.norm(c2) * np.linalg.norm(W2))
        A = [amp(q, c1, c2, l) for l in (1.0, 10.0, 100.0)]
        T1, T2 = T_of_c(c1), T_of_c(c2); gr = -4 * (np.sum(T1 * T2) - 0.5 * np.trace(T1) * np.trace(T2)) / (q @ q)
        print(f"{nm:14s} s={s:.2f}: Ward ratios {e1:.1e},{e2:.1e}; gauge dependence |A(10)-A(1)|/|A| {abs(A[1]-A[0])/abs(A[0]):.1e}, |A(100)-A(1)|/|A| {abs(A[2]-A[0])/abs(A[0]):.1e}; |A - GR(T)|/|GR| {abs(A[0]-gr)/abs(gr):.1e}")
