import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from seg import *
    from wamp2 import pair_at, shell_f
rng = np.random.default_rng(11); ds = [rng.standard_normal(3) for _ in range(4)]; ds = [x / np.linalg.norm(x) for x in ds]
def amp(q, b1, b2, lam):
    G, Gm = Dc.gauge(q), Dc.gauge(-q)
    return b2 @ segment_readings(Dc, q)[0] @ np.linalg.solve(Dc.Q(q) + lam * G @ Gm.T, segment_readings(Dc, -q)[0].T @ b1)
grad = grad_cell
for mode in ('cell (old)', 'local midpoint'):
    out = []
    for s in (0.2, 0.1, 0.05, 0.025):
        k1 = shell_kt(s * ds[0], grad); k2 = shell_kt(0.8 * s * ds[1], grad); q = k2 - k1; k3, k4 = pair_at(q, 0.9 * s, grad, ds[2], ds[3])
        c1 = stress_c(grad(-k1), grad(k2)); c2 = stress_c(grad(-k3), grad(k4))
        b1, b2 = c1 @ Lt, c2 @ Lt
        if mode != 'cell (old)':
            b1 = b1 * np.array([place(q, m, 'local') for m in MID]); b2 = b2 * np.array([place(-q, m, 'local') for m in MID])
        A = [amp(q, b1, b2, l) for l in (1.0, 10.0)]
        T1, T2 = T_of_c(c1), T_of_c(c2); gr = -4 * (np.sum(T1 * T2) - 0.5 * np.trace(T1) * np.trace(T2)) / (q @ q)
        out.append((abs(A[1] - A[0]) / abs(A[0]), abs(A[0] - gr) / abs(gr)))
    print(f"{mode:15s}: gauge dep " + ", ".join(f"{o[0]:.1e}" for o in out) + " | from EH form " + ", ".join(f"{o[1]:.1e}" for o in out))
