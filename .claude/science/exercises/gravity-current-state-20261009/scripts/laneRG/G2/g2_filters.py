"""Lane RG probe G2, part 1: vertex filters and the sup-norm umklapp ratio.

Filters act on each matter leg: F(k) = prod_j f(k_j), f even, degree n in cos k
(= range-n kernel = depth-n chain of nearest-neighbour nodes).  The tree amplitude through
ANY mediator (t- plus u-channel) is then T_n = F(k1)F(k2)F(k3)F(k4) * T_0 exactly.

(a) binomial:  f_r(k) = ((1+cos k)/2)^r          (degree r)
(c) minimax:   best degree-n f with |f-1|<=delta on |k|<=kappa, |f|<=delta on pi/2<=|k|<=pi
               (LP on a fine grid), compared with the Bernstein-Walsh rate exp(-g_E(c)),
               E = [-1,0] u [cos kappa, 1] in x = cos k (two-interval Green function).

eps_sup(n) = sup over umklapp configurations of prod_legs F / F(0)^4, computed by
reduction to one crossing component:  max_{s in [pi,2pi]} M(s) M(2pi - s),
M(s) = max_{a+b=s} |f(a) f(b)|  (other components at 0 where f = f(0)).
"""
import numpy as np, sys
from scipy.optimize import linprog
from scipy.integrate import quad


def f_binom(r):
    return lambda k: ((1 + np.cos(k)) / 2) ** r


def minimax_filter(n, kappa, ngrid=3000, zero_at_pi=False):
    """LP: minimise delta. Returns coefficient vector c (cos basis) and delta."""
    kp = np.linspace(0, kappa, ngrid // 3)
    ks = np.linspace(np.pi / 2, np.pi, ngrid // 3)
    kt = np.linspace(kappa, np.pi / 2, ngrid // 3)
    def B(k):
        M = np.cos(np.outer(k, np.arange(n + 1)))
        if zero_at_pi:
            M = M * (1 + np.cos(k))[:, None] / 2
        return M
    Bp, Bs, Bt = B(kp), B(ks), B(kt)
    nv = n + 2  # c_0..c_n, delta
    A = []; b = []
    one = np.ones((len(kp), 1)); ones_s = np.ones((len(ks), 1)); ones_t = np.ones((len(kt), 1))
    # passband: f - 1 <= d ; 1 - f <= d
    A.append(np.hstack([Bp, -one])); b.append(np.ones(len(kp)))
    A.append(np.hstack([-Bp, -one])); b.append(-np.ones(len(kp)))
    # stopband: |f| <= d
    A.append(np.hstack([Bs, -ones_s])); b.append(np.zeros(len(ks)))
    A.append(np.hstack([-Bs, -ones_s])); b.append(np.zeros(len(ks)))
    # transition: -d <= f <= 1 + d
    A.append(np.hstack([Bt, -ones_t])); b.append(np.ones(len(kt)))
    A.append(np.hstack([-Bt, -ones_t])); b.append(np.zeros(len(kt)))
    A = np.vstack(A); b = np.concatenate(b)
    cost = np.zeros(nv); cost[-1] = 1
    res = linprog(cost, A_ub=A, b_ub=b, bounds=[(None, None)] * (n + 1) + [(0, None)], method='highs')
    c = res.x[:-1]
    def f(k, c=c, zero_at_pi=zero_at_pi):
        v = np.cos(np.multiply.outer(k, np.arange(len(c)))) @ c
        return v * (1 + np.cos(k)) / 2 if zero_at_pi else v
    # true sup errors on a finer grid
    kpf = np.linspace(0, kappa, 20001); ksf = np.linspace(np.pi / 2, np.pi, 20001)
    dp = np.max(np.abs(f(kpf) - 1)); ds = np.max(np.abs(f(ksf)))
    return f, max(dp, ds), dp, ds


def green_rate(kappa):
    """g_E(c) for E = [-1,0] u [a,1], a = cos kappa: the Bernstein-Walsh exponent."""
    a = np.cos(kappa)
    # on (0,a): q(t) = (t+1) t (t-a)(t-1) > 0 ; write 1/sqrt(q) = w(t) * t^-1/2 (a-t)^-1/2
    h = lambda t: 1.0 / np.sqrt((t + 1) * (1 - t))
    I0 = quad(h, 0, a, weight='alg', wvar=(-0.5, -0.5))[0]
    I1 = quad(lambda t: t * h(t), 0, a, weight='alg', wvar=(-0.5, -0.5))[0]
    c = I1 / I0
    g = quad(lambda t: (c - t) / np.sqrt((t + 1) * (1 - t) * (a - t)), 0, c, weight='alg', wvar=(-0.5, 0))[0]
    return g, c


def eps_sup(f, ngrid=4001):
    """sup over one-component-crossing umklapp configurations of f(a)f(b)f(c)f(d)/f(0)^4."""
    f0 = f(np.array([0.0]))[0]
    ss = np.linspace(np.pi, 2 * np.pi, 801)
    best = 0.0
    for s in ss:
        a = np.linspace(s - np.pi, np.pi, ngrid); Ms = np.max(np.abs(f(a) * f(s - a)))
        u = 2 * np.pi - s
        c = np.linspace(u - np.pi, np.pi, ngrid); Mu = np.max(np.abs(f(c) * f(u - c)))
        best = max(best, Ms * Mu)
    return best / f0 ** 4


if __name__ == '__main__':
    print("== (a) binomial filter ((1+cos k)/2)^r: sup umklapp ratio vs 16^-r (proved value)")
    for r in [1, 2, 4, 8, 16, 32]:
        e = eps_sup(f_binom(r))
        print(f"  r={r:3d}  eps_sup={e:.6e}  16^-r={16.0**-r:.6e}  ratio={e/16.0**-r:.6f}")
    print("\n== Bernstein-Walsh exponent g_E(c) per degree (one leg), E=[-1,0]u[cos kappa,1]")
    for kap in [1e-6, 0.1, np.pi / 8, np.pi / 6, np.pi / 4, np.pi / 3, 0.4 * np.pi, 0.45 * np.pi]:
        g, c = green_rate(kap)
        print(f"  kappa={kap:.4f} ({kap/np.pi:.3f} pi)  g1={g:.5f}  critical x={c:.4f}   2*g1={2*g:.5f}")
    print("  check kappa->0 limit: arccosh(3) =", np.arccosh(3.0))
    print("\n== (c) LP minimax filters: delta_n, its local rate, and eps_sup for 2<->2 (product filter)")
    for kap in [np.pi / 6, np.pi / 4, np.pi / 3]:
        g, _ = green_rate(kap)
        print(f" kappa = {kap/np.pi:.3f} pi ; Bernstein-Walsh one-leg rate g1 = {g:.4f}")
        prev = None
        for n in [2, 4, 6, 8, 12, 16, 20, 24, 28, 32, 40]:
            f, dl, dp, ds = minimax_filter(n, kap)
            es = eps_sup(f, ngrid=2001)
            rate = '' if prev is None else f"local rate -dln(delta)/dn={-(np.log(dl)-np.log(prev[1]))/(n-prev[0]):.4f}"
            print(f"   n={n:3d} delta={dl:.3e} (pass {dp:.1e}, stop {ds:.1e})  eps_sup={es:.3e}  "
                  f"-ln(eps_sup)/n={-np.log(es)/n:.4f}  {rate}")
            prev = (n, dl)
            if dl < 1e-12: break
        sys.stdout.flush()
