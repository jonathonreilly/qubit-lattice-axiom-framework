from common import *
from ward import grad_cell, shell_kt, stress_c, n1, n2
PR = np.array([[.5 if m == a else .125 for m in range(4)] if a == b else [.5 if m in (a, b) else .25 for m in range(4)] for a, b in HC])
for sg in (+1, -1):
    prev = None
    for s in (0.2, 0.1, 0.05, 0.025):
        k1 = shell_kt(s * n1, grad_cell); k2 = shell_kt(0.7 * s * n2, grad_cell); q = k2 - k1
        c = stress_c(grad_cell(-k1), grad_cell(k2)) * np.exp(sg * 1j * (PR - 0.5) @ q)
        W = strain_metric(Dc, -q) @ Dc.gauge(-q)[:, :4]
        r = np.linalg.norm(c @ W) / (np.linalg.norm(c) * np.linalg.norm(W))
        print(f"matched placement sign {sg:+d} s={s:.3f}: Ward ratio {r:.3e}" + (f" (x{prev/r:.2f})" if prev else "")); prev = r
