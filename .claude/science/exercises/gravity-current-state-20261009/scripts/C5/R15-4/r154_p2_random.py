"""R15-4 Lemma P2 check: rho_hat >= 0 on random histories of class H4 (components with 0 <= x <= 4, nonnegative densities,
random nonnegative releases of random size, sector and width, including exact steps and pure reheating starts), for the
positive two-register readers D1 and R*; and a control outside H4 (a dominant phantom component, x = -1).
Output: min over the run of rho_hat / max(rho_nc) and min rho_hat/rho_nc where rho_nc > 1e-12 max."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r154_reader import DESIGNS
rng = np.random.default_rng(7)
us = np.linspace(0, 12, 120001); du = us[1] - us[0]
def history(phantom=False):
    nc = rng.integers(1, 4)
    xs = list(rng.uniform(0, 4, nc)); rho0 = list(rng.uniform(0, 1, nc) * (rng.random(nc) < 0.7))
    if phantom: xs.append(-1.0); rho0.append(5.0)
    rel = []
    for _ in range(rng.integers(1, 6)):
        rel.append((rng.uniform(0.2, 10), rng.integers(0, len(xs)), 10 ** rng.uniform(-2, 1.5), 10 ** rng.uniform(-3, -0.3) if rng.random() < 0.7 else 0.0))
    x = np.array(xs); r = np.array(rho0, float)
    E = np.empty_like(us); R = np.empty_like(us)
    for i, u in enumerate(us):
        src = np.zeros(len(x))
        for (uT, j, D, W) in rel:
            if W == 0.0:
                if abs(u - uT) < du / 2: src[j] += D / du
            else:
                src[j] += D * 0.5 / W / np.cosh(np.clip((u - uT) / W, -300, 300)) ** 2
        r = r + du * (-x * r + src)
        r = np.maximum(r, 0) if not phantom else r
        E[i] = np.sum(x * r); R[i] = np.sum(r)
    return E, R
for name in ('D1 minimal (2 regs)', 'R* fast (2 regs, beta 20,24)'):
    b, k = DESIGNS[name]
    for phantom in (False, True):
        worst, worst_rel = np.inf, np.inf
        for trial in range(30 if not phantom else 10):
            E, R = history(phantom)
            y = np.zeros(len(b)); rh = np.empty_like(us)
            a_ = np.exp(-b * du)
            for i in range(len(us)):          # exact exponential integrator for piecewise-constant E
                y = a_ * y + (1 - a_) / b * E[i]
                rh[i] = k @ y
            sc = np.max(np.abs(R))
            worst = min(worst, rh.min() / sc)
            m = R > 1e-6 * sc
            if m.any(): worst_rel = min(worst_rel, np.min(rh[m] / R[m]))
        print(f'{name}, {"CONTROL with dominant phantom (outside H4)" if phantom else "class H4 random histories"}: min rho_hat/max rho = {worst:+.3e}; min rho_hat/rho_nc = {worst_rel:+.3e}')
