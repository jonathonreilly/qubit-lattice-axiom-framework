"""R15-4 (construction + (a)): a regular P-T reader = a causal LINEAR filter with finite state.

Reader (kappa = 1, u = ln a = (1/3) ln(site count), d/du = (3/theta) d/dt):
    input   E(u) := -d rho_tot/du  (= 3 (rho+p)_nc homogeneously; = 2 S(t)/kappa in the CMC model, see r154_lumpy.py)
    state   y_j' = E - beta_j y_j          (j = 1..M, beta_j > 4)       [M memory registers, first-order, linear]
    output  rho_hat = sum_j k_j y_j ;  3 H^2 = rho_hat
Kernel K(s) = sum_j k_j exp(-beta_j s) (causal, fading). Constants in rho_tot never enter (only E is read).
Response to a constant-w component rho ~ e^{-x u}:  rho_hat/rho = G(x) := sum_j k_j x/(beta_j - x);  G(0) = 0.
Exactness for radiation (x=4) and dust (x=3) imposed:  G(3) = G(4) = 1.
Design: least squares of G - 1 on a stated x-window plus a ridge mu*|k|^2, subject to the two equalities.

Step response (proved, linearity): latent heat Delta into a sector with rate x_s at u_T gives, for tau = u - u_T > 0,
    rho_hat - rho_nc = -Delta_s(u) * (1 - G_tau(x_s)),  G_tau(x) = sum_j k_j x (1 - e^{-(beta_j - x) tau})/(beta_j - x)
so  eps := rho_hat/rho_nc - 1 = -(Delta_s(u)/rho_nc(u)) (1 - G_tau(x_s)), bounded by alpha * T_K, T_K = sup_tau |1 - G_tau|,
for ANY release width W (a smooth release is the step response convolved with s'(u) >= 0).
Subtraction rule: eps uses the exact non-vacuum density rho_nc (radiation + dust + released heat); Lt := rho_hat - rho_nc
(= lambda + rho_v, R14-5's Lambda-tilde); nothing else is subtracted.
"""
import numpy as np
from scipy.integrate import solve_ivp

np.set_printoptions(linewidth=160)


def design(betas, xwin, mu=1e-6, nodes=(3.0, 4.0), wfun=None):
    betas = np.asarray(betas, float)
    xs = np.linspace(*xwin, 400)
    A = xs[:, None] / (betas[None, :] - xs[:, None])
    w = np.ones_like(xs) if wfun is None else wfun(xs)
    Q = (A * w[:, None]).T @ A + mu * np.eye(len(betas))
    c = (A * w[:, None]).T @ np.ones_like(xs)
    Aeq = np.array([[x / (b - x) for b in betas] for x in nodes])
    KKT = np.block([[2 * Q, Aeq.T], [Aeq, np.zeros((len(nodes), len(nodes)))]])
    rhs = np.concatenate([2 * c, np.ones(len(nodes))])
    sol = np.linalg.solve(KKT, rhs)
    return betas, sol[:len(betas)]


def G(x, b, k):
    x = np.asarray(x, float)
    r = np.sum(k * x[..., None] / (b - x[..., None]), axis=-1)
    return float(r) if r.ndim == 0 else r


def Gtau(x, tau, b, k):
    return np.sum(k * x * (1 - np.exp(-(b - x) * tau)) / (b - x))


DESIGNS = {
    'D1 minimal (2 regs)': design([6.0, 8.0], (3.0, 4.0), mu=0.0),
    'D2 flat x in [0.3,4.5]': design([5.0, 7.0, 10.0, 15.0], (0.3, 4.5), mu=1e-6),
    'D3 flat x in [0.15,4.5]': design([5.0, 7.0, 10.0, 15.0, 22.0], (0.15, 4.5), mu=1e-7),
    # D5: exact G(3)=G(4)=1 and lag-free for radiation releases, G'(4)=1/4 (r154_lagfree_scan.py); k solved exactly
    'D5 lag-free x=4 (3 regs)': (np.array([5.0, 6.0, 7.0]), np.array([1.25, -11.0, 13.5])),
    # R*: fast two-register reader, exact G(3)=G(4)=1 (k solved exactly); chosen for the e+e- (BBN) test, r154_bbn.py
    'R* fast (2 regs, beta 20,24)': (np.array([20.0, 24.0]), np.array([-136.0, 175.0])),
}

if __name__ == '__main__':
    print('# Part 1. Designs: betas, k, sum k (= K(0)), int K ds = sum k/beta, |K|_1-type size sum|k|/beta, T_K(S1: x=4), T_K(S2: x=3)')
    taus = np.linspace(0, 30, 30001)
    for name, (b, k) in DESIGNS.items():
        T4 = max(abs(1 - Gtau(4.0, t, b, k)) for t in taus)
        T3 = max(abs(1 - Gtau(3.0, t, b, k)) for t in taus)
        print(f'{name}: beta={b}, k={np.round(k, 5)}')
        print(f'    G(3)-1={G(3.0, b, k)-1:+.1e}, G(4)-1={G(4.0, b, k)-1:+.1e}; K(0)={k.sum():+.4f}; intK={np.sum(k/b):+.4f};'
              f' sum|k|/beta={np.sum(np.abs(k)/b):.4f}; T_K(x=4)={T4:.4f}; T_K(x=3)={T3:.4f}')
        xs = [-1.5, -0.6, 0.0, 0.03, 0.15, 0.3, 0.45, 0.75, 1.0, 2.0, 2.5, 3.5, 3.9, 4.5, 6.0]
        print('    G(x): ' + ', '.join(f'x={x}:{G(x, b, k):.4f}' for x in xs))
        # dead band (proved generic: G(0)=0): smallest x>0 with |G-1|<=0.1 and <=0.01
        xg = np.linspace(1e-4, 4, 40001); g = G(xg, b, k)
        for tol in (0.1, 0.01):
            bad = np.where(np.abs(g - 1) > tol)[0]
            print(f'    |G-1|<={tol} for all x in [{xg[bad[bad < 39000].max()+1] if np.any(bad < 39000) else 0:.3f}, 4] '
                  f'(i.e. w >= {-1 + (xg[bad[bad < 39000].max()+1])/3:.3f})')

    print('\n# Part 2. R14-5 runner setting (rv0=5, q0=1, m0=0.05, latent heat -> radiation), same 5 runs + an exact step; reader = D1 (primary)')
    b, k = DESIGNS['D1 minimal (2 regs)']

    def run(D, W, sector='S1', uT=0.0, rv0=5.0, q0=1.0, m0=0.05, span=None, label=''):
        us0 = uT - 12 * W - 2 if span is None else span[0]
        us1 = uT + 12 * W + 3 if span is None else span[1]
        sp = lambda u: 0.0 if W == 0 else 0.5 / W / np.cosh((u - uT) / W) ** 2
        xs_ = 4.0 if sector == 'S1' else 3.0

        def rhs(u, Y):
            q, m = Y[0], Y[1]
            src = D * sp(u)
            dq = -4 * q + (src if sector == 'S1' else 0.0)
            dm = -3 * m + (src if sector == 'S2' else 0.0)
            E = 4 * q + 3 * m
            return np.concatenate([[dq, dm], E - b * Y[2:]])
        q_i, m_i = q0 * np.exp(-4 * us0), m0 * np.exp(-3 * us0)
        Y0 = np.concatenate([[q_i, m_i], 4 * q_i / (b - 4) + 3 * m_i / (b - 3)])
        us = np.linspace(us0, us1, 8001)
        ms = min(W / 20, 0.01) if W > 0 else 0.01
        if W == 0:  # exact step: integrate piecewise, inject Delta at uT
            s1 = solve_ivp(rhs, (us0, uT), Y0, rtol=1e-12, atol=1e-30, method='DOP853', max_step=ms, dense_output=True)
            Y1 = s1.y[:, -1].copy(); Y1[0 if sector == 'S1' else 1] += D
            s2 = solve_ivp(rhs, (uT, us1), Y1, rtol=1e-12, atol=1e-30, method='DOP853', max_step=ms, dense_output=True)
            Y = np.where(us[None, :] <= uT, s1.sol(np.minimum(us, uT)), s2.sol(np.maximum(us, uT)))
        else:
            sol = solve_ivp(rhs, (us0, us1), Y0, t_eval=us, rtol=1e-12, atol=1e-30, method='DOP853', max_step=ms)
            Y = sol.y
        q, m = Y[0], Y[1]; yv = Y[2:]
        rh = k @ yv; rnc = q + m; E = 4 * q + 3 * m
        if W == 0:
            rv = rv0 - D * (us > uT)
        else:
            rv = rv0 - D * (1 + np.tanh((us - uT) / W)) / 2
        eps = rh / rnc - 1
        Lt = rh - rnc; lam = rh - (rnc + rv)
        drh = k.sum() * E - (k * b) @ yv           # exact d rho_hat/du from the ODE (no finite differences)
        g_over_H2 = -(drh + E) / rh                  # g = -(1/3)(d rho_hat/du + E), H^2 = rho_hat/3
        iT = np.searchsorted(us, uT)
        after = us > uT
        idx_small = np.where(after & (np.abs(eps) < 1e-6))[0]
        u_small = (us[idx_small[0]] - uT) if len(idx_small) else np.nan
        # last time |eps| >= 1e-6 after uT
        big = np.where(after & (np.abs(eps) >= 1e-6))[0]
        u_last = (us[big[-1]] - uT) if len(big) else 0.0
        ext = np.trapezoid(np.sqrt(np.clip(rh / rnc, 0, None)) - 1, us)
        alpha = D / (q0 * np.exp(-4 * uT) + m0 * np.exp(-3 * uT))
        print(f'[{label}{sector}] D={D} alpha(=D/rho_nc(uT-))={alpha:.3g} W={W}: min rho_hat/rho_nc={np.min(rh/rnc):+.5f}; max|eps|={np.max(np.abs(eps)):.3e};'
              f' eps(uT+)={eps[min(iT+1, len(us)-1)]:+.3e}; |eps|<1e-6 for all tau>{u_last:.2f}; eps(end)={eps[-1]:+.1e}')
        print(f'      Lt/rho_nc end={Lt[-1]/rnc[-1]:+.1e}; lam end={lam[-1]:+.6f} vs -rho_v,final={-(rv0-D):+.6f};'
              f' g/H^2: start={g_over_H2[0]:+.1e}, max|.| in [uT-6W,uT+3]={np.max(np.abs(g_over_H2[(us>=uT-6*W-1e-12)&(us<=uT+3)])):.3e}, end={g_over_H2[-1]:+.1e};'
              f' extra e-folds int(sqrt(rho_hat/rho_nc)-1)du={ext:+.3e}')
        return us, eps, rh, rnc

    for D, W in [(0.01, 0.15), (0.05, 0.3), (0.3, 0.3), (0.7, 0.3), (0.01, 0.02), (0.7, 0.0)]:
        run(D, W, label='R14-5 ')
    print('  same with the span extended to uT+12W+8 (relaxation visible):')
    for D, W in [(0.3, 0.3), (0.7, 0.0)]:
        run(D, W, span=(-12 * W - 2, 12 * W + 8), label='R14-5 long ')
    print('  CONTROL unimodular (g == 0, tuned to the initial vacuum): Lambda_eff = -D after the step (Lemma PT; analytic, R14-5 runner).')

    print('\n# Part 3. R13-3 transition grid (R0=30, M0=0.5, uT=0; alpha = Delta/rho_r(uT)); sectors S1 (heat->radiation), S2 (heat->w=0 condensate)')
    for name in DESIGNS:
        b, k = DESIGNS[name]
        print(f'-- reader {name}')
        for sector in ('S1', 'S2'):
            for alpha in (0.01, 0.1, 0.5):
                for W in (0.3, 0.05, 0.005, 0.0):
                    run(alpha * 30.0, W, sector=sector, q0=30.0, m0=0.5, span=(-4.0, 12.0), label='')

    print('\n# Part 4. Step-response formula check (proved form vs ODE), D2 and D1, S1 alpha=0.5 W=0 at tau = 0.1, 0.5, 1, 2')
    for nm in ('D2 flat x in [0.3,4.5]', 'D1 minimal (2 regs)'):
      b, k = DESIGNS[nm]
      print('  reader', nm)
      us, eps, rh, rnc = run(15.0, 0.0, sector='S1', q0=30.0, m0=0.5, span=(-4.0, 12.0), label='chk ')
      for tau in (0.1, 0.5, 1.0, 2.0):
        i = np.searchsorted(us, tau)
        u = us[i]; Dr = 15.0 * np.exp(-4 * u); rn = (30 + 15) * np.exp(-4 * u) + 0.5 * np.exp(-3 * u)
        pred = -(Dr / rn) * (1 - Gtau(4.0, u, b, k))
        print(f'   tau={u:.4f}: eps ODE={eps[i]:+.8e}, formula={pred:+.8e}')
    print('\n# Part 5. D1 positivity theorem ingredients (proved analytically; numerical confirmation):')
    b5, k5 = DESIGNS['D5 lag-free x=4 (3 regs)']
    tt5 = np.linspace(0, 20, 100001)
    H5 = np.array([Gtau(4.0, t, b5, k5) for t in tt5]) / 4
    print(f'   D5: H(t) min = {H5.min():+.3e} (>=0: positive on reheating histories), max = {H5.max():.4f}; G\'(4) = {np.sum(k5*b5/(b5-4)**2):.6f} (1/4 = lag-free)')
    b, k = DESIGNS['D1 minimal (2 regs)']
    tt = np.linspace(0, 20, 200001)
    H4 = np.array([Gtau(4.0, t, b, k) for t in tt]) / 4
    H3 = np.array([Gtau(3.0, t, b, k) for t in tt]) / 3
    print(f'   H(t) = int_0^t K e^(4s) ds = (1 + 4e^(-2t) - 5e^(-4t))/4: min over t = {H4.min():+.3e}, max = {H4.max():.4f} (t={tt[H4.argmax()]:.4f}), H(inf)=0.25')
    print(f'   1 - G_t(4) = -4e^(-2t) + 5e^(-4t) in [{(1-4*H4).min():+.4f}, {(1-4*H4).max():+.4f}];  1 - G_t(3) = -2e^(-3t)+3e^(-5t) in [{(1-3*H3).min():+.4f}, {(1-3*H3).max():+.4f}]')
    print(f'   G(x) >= 0 on [0,4]: min = {min(G(x, b, k) for x in np.linspace(0, 4, 4001)):.4f}; G(x) max on [0,4] = {max(G(x, b, k) for x in np.linspace(0, 4, 4001)):.4f}')
    # QCD/EW residual at BBN with D1 (S1 step, worst case): eps(tau) bounded by alpha*|1-G_tau(4)|
    for lab, alpha, T0 in (('EW (alpha=5.1e-3, T=160 GeV)', 5.1e-3, 160e3), ('QCD (alpha=0.5 upper, T=150 MeV)', 0.5, 150.0)):
        for Tb in (1.0, 0.07):
            tau = np.log(T0 / Tb)
            print(f'   {lab}: worst |eps| at T={Tb} MeV (tau={tau:.2f}) <= alpha*|1-G_tau(4)| = {alpha*abs(1-Gtau(4.0, tau, b, k)):.2e}')
