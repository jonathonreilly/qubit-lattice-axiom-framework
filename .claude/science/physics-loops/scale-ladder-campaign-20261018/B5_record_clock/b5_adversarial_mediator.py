"""B5 supplement: D2 mediator-bond tolerance along the ADVERSARIAL direction
u_e = sign(d log t_eff / d eps_e): +1 on gamma and q bonds, -1 on J_m bonds
(t_eff = gam^2 q^(n-1)/J_m^n).  Random directions (scan D) mostly cancel; this
is the direction the repo's O(m eps) worst-case bound refers to.
Metric a_act (actual scalar) on the output register, budget e=1e-2, t in {T,2T}.
Tolerance from linear response (x0 small), then re-verified directly.
PREDICTION (declared before running): tolerance*(2n+1) roughly constant
(slope of log tol vs log(2n+1) in [-1.3,-0.7]); flat in T at n=3."""
import numpy as np
from b5_device import d2_chain, m_vec
Jm, q, g, E = 1.0, 0.8, 0.05, 1e-2
r = q / Jm

def run(n, Tl, x):
    gam = np.sqrt(0.01 * Jm / r ** (n - 1)); lam = 2 * 0.01 ** 2 / g; T = Tl / lam
    M = int(1.2 * 2 * g * 2 * T) + 50
    u = np.array([1.0] + [(-1.0 if i % 2 == 0 else 1.0) for i in range(2 * n - 1)] + [1.0])
    H0, s, b0 = d2_chain(n, gam, Jm, q, g, M)
    H1, _, b1 = d2_chain(n, gam, Jm, q, g, M, eps_med=x * u)
    R = slice(1 + 2 * n + 30, None)
    p0 = H0.evolve(s, [T, 2 * T]); p1 = H1.evolve(s, [T, 2 * T])
    return max(m_vec(a[R], b[R]) for a, b in zip(p1, p0)), T

rows = []
for n, Tl in [(1, 25), (2, 25), (3, 25), (4, 25), (5, 25), (3, 50)]:
    x0 = 1e-4
    y0, T = run(n, Tl, x0)
    xs = x0 * E / y0
    yv, _ = run(n, Tl, xs)
    ok = 0.8 * E <= yv <= 1.25 * E
    rows.append((n, T, xs))
    print(f"n={n} 2n+1={2*n+1} T={T:.0f}: tol={xs:.3e}  tol*(2n+1)={xs*(2*n+1):.3e}  verify={yv:.3e} {'PASS' if ok else 'FAIL'}")
base = [(n, x) for n, T, x in rows if T == 6250]
sl = np.polyfit(np.log([2 * n + 1 for n, _ in base]), np.log([x for _, x in base]), 1)[0]
print(f"{'PASS' if -1.3 <= sl <= -0.7 else 'FAIL'}  adversarial tol ~ (2n+1)^{sl:.2f}")
t3 = [x for n, T, x in rows if n == 3]
print(f"{'PASS' if abs(np.log(t3[1]/t3[0])/np.log(2)) < 0.15 else 'FAIL'}  n=3 tolerance flat in T: {t3[0]:.3e} (T=6250) vs {t3[1]:.3e} (T=12500)")
