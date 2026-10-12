"""R12-2: homogeneous creation laws through a vacuum step (V3 + site creation).

Units: kappa/3 = 1, so Friedmann without Lambda reads H^2 = rho_nc.
Content: radiation (x=4), dust (x=3), vacuum rho_v(u) (u = ln a) with a smooth
step of size Delta released into radiation (total stress conserved; the latent
heat -> radiation assumption is stated, R11-3 referee finding 4).
In V3 + creation the densities are functions of u only (sites keep fixed
spacing; dilution is by creation), so a memoryless rule is a function of u.

Rules (H = c/3, c = creation rate per site per unit time; c >= 0 enforced:
destroying recorded sites violates Record permanence):
  A(rho_ref): H^2 = rho_tot - rho_ref            (algebraic, law constant / inherited C)
  U         : dH/dt = -(3/2)(rho+p)_tot           (vacuum-blind derivative law = unimodular)
  E         : H^2 = (rho+p)/(1+cs2), cs2 = dp/drho (equation-of-state rule)
  P         : H^2 = sum_i w_i/x_i, Prony on m_k = (-d/du)^k rho_tot, k=1..2N (time-derivative rule)
  R         : dH/dt = -H^2 - (1/2)(rho+3p)_P,  (rho+3p)_P = m1 - 2*rho_P  (Raychaudhuri, vacuum-blind)
  GR        : dH/dt = -H^2 - (1/2)(rho+3p)_tot   (control)
Diagnostic: X(u) = H^2 - rho_nc  (rho_nc = true radiation + dust).  Lambda-like if
X -> const != 0; curvature-like if X*a^2 -> const.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

u = sp.symbols('u')
W = 0.15          # transition width in ln a
U0 = 0.0          # transition at a = 1
s_expr = (1 + sp.tanh((u - U0) / W)) / 2
s_d = [sp.lambdify(u, sp.diff(s_expr, u, k), 'numpy') for k in range(0, 7)]

R0, M0 = 30.0, 0.5   # radiation and dust normalisations at a = 1 (before release)
V0 = 1.0             # initial vacuum energy (arbitrary; any constant)


def comps(uu, Delta):
    """Return rho_r, rho_m, rho_v and their u-derivatives up to order 6."""
    a = np.exp(uu)
    # radiation with source: rho_r' = -4 rho_r + Delta s'(u)
    # integrate source exactly on a fine grid
    grid = np.linspace(-3.0, uu, 4001) if np.isscalar(uu) else None
    src = Delta * s_d[1](grid) * np.exp(4 * grid)
    rr = (R0 * np.exp(-4 * 0.0) * 1.0 + np.trapezoid(src, grid) - 0.0) * a ** -4
    # note R0 is the comoving radiation constant: rho_r = (R0 + int) a^-4
    rm = M0 * a ** -3
    rv = V0 - Delta * s_d[0](uu)
    dr = [rr]; dm = [rm]; dv = [rv]
    for k in range(1, 7):
        dr.append(-4 * dr[-1] + Delta * s_d[k](uu))
        dm.append(-3 * dm[-1])
        dv.append(-Delta * s_d[k](uu))
    return np.array(dr), np.array(dm), np.array(dv)


def state(uu, Delta):
    dr, dm, dv = comps(uu, Delta)
    rho_nc = dr[0] + dm[0]
    rho_tot = rho_nc + dv[0]
    p_tot = dr[0] / 3 - dv[0]
    # derivatives of total density and pressure in u
    rho_d = dr + dm + dv
    p_d1 = dr[1] / 3 - dv[1]
    m = [(-1) ** k * rho_d[k] for k in range(7)]  # m_k = (-d/du)^k rho
    return dict(rho_nc=rho_nc, rho_tot=rho_tot, p_tot=p_tot, rho_u=rho_d[1], p_u=p_d1, m=m)


def prony_rho(m, N=2):
    """Reconstruct sum_i rho_i (x_i != 0) from m_1..m_2N: measure mu = sum (rho_i x_i) delta_{x_i}."""
    M = np.array(m[1:2 * N + 1], dtype=float)  # M_j = m_{j+1}, j = 0..2N-1
    if abs(M[0]) < 1e-300:
        return 0.0, None
    Hk = np.array([[M[i + j] for j in range(N)] for i in range(N)])
    rhs = -np.array([M[N + i] for i in range(N)])
    try:
        c = np.linalg.solve(Hk, rhs)
    except np.linalg.LinAlgError:
        return np.nan, None
    xs = np.roots(np.concatenate(([1.0], c[::-1])))
    V = np.vander(xs, N, increasing=True).T
    wts = np.linalg.solve(V, M[:N])
    return float(np.real(np.sum(wts / xs))), np.real(xs)


def H2_rule(name, st, rho_ref=None):
    if name == 'A':
        return st['rho_tot'] - rho_ref
    if name == 'E':
        cs2 = st['p_u'] / st['rho_u']
        return (st['rho_tot'] + st['p_tot']) / (1 + cs2)
    if name == 'P':
        return prony_rho(st['m'])[0]
    raise ValueError


def run_memoryless(name, Delta, rho_ref=None, us=None):
    out = []
    frozen = False
    for uu in us:
        st = state(uu, Delta)
        h2 = H2_rule(name, st, rho_ref)
        if h2 <= 0 or frozen:
            frozen = True
            out.append((uu, 0.0, st['rho_nc'], True))
            break
        out.append((uu, h2, st['rho_nc'], False))
    return out


LASTP = [1.0]
LB = -(V0 - 0.3)   # bare Lambda/3 tuned for the Delta = 0.3 final vacuum


def run_memory(name, Delta, H2_init, u_span=(-2.0, 9.0)):
    def rhs(uu, y):
        H = y[0]
        st = state(uu, Delta)
        if name == 'U':
            Hdot = -1.5 * (st['rho_tot'] + st['p_tot'])
        elif name == 'GR':
            Hdot = -H ** 2 - 0.5 * (st['rho_tot'] + 3 * st['p_tot'])
        elif name == 'R':
            rP, _ = prony_rho(st['m'], 3)
            if not np.isfinite(rP) or rP <= 0:
                rP, _ = prony_rho(st['m'], 2)
            if not np.isfinite(rP) or rP <= 0:
                rP = LASTP[0]
            LASTP[0] = rP
            Hdot = -H ** 2 - 0.5 * (st['m'][1] - 2 * rP)
        elif name == 'F':
            # hybrid: H^2 = rho_P + X, X carried as site memory with dX/dt = -2 H X
            # (y[0] here is X, not H); returns dX/du = -2 X
            return [-2 * y[0]]
        elif name == 'GRb':
            Hdot = -H ** 2 - 0.5 * (st['rho_tot'] + 3 * st['p_tot']) + LB
        return [Hdot / H]

    def hit0(uu, y):
        if name == 'F':
            st = state(uu, Delta)
            rP, _ = prony_rho(st['m'], 3)
            return rP + y[0] - 1e-12
        return y[0] - 1e-9
    hit0.terminal = True
    y0 = [H2_init] if name == 'F' else [np.sqrt(H2_init)]
    sol = solve_ivp(rhs, u_span, y0, events=hit0, rtol=1e-12, atol=1e-16,
                    dense_output=True, max_step=0.05)
    return sol


if __name__ == '__main__':
    np.set_printoptions(precision=5)
    us = np.linspace(-2.0, 12.0, 141)
    print('# Rules through a vacuum step. kappa/3 = 1; V0 =', V0, '; transition at a = 1, width', W)
    print('# X = H^2 - rho_nc ; Lambda-like if X -> const; curvature-like if X a^2 -> const')
    for Delta in (0.3, 0.7):
        print(f'\n## Delta = {Delta}  (final vacuum = {V0 - Delta})')
        # A with rho_ref tuned to the Delta = 0.3 final vacuum (a law constant fixed in advance)
        for rr in (V0, V0 - 0.3):
            o = run_memoryless('A', Delta, rho_ref=rr, us=us)
            last = o[-1]
            if last[3]:
                print(f'A(rho_ref={rr:.2f}): FROZEN (c -> 0, no site destruction) at u = {last[0]:.2f}, '
                      f'rho_nc there = {last[2]:.4e}')
            else:
                print(f'A(rho_ref={rr:.2f}): late X = H^2 - rho_nc = {last[1] - last[2]:+.6f} (Lambda-like, = V0-Delta-rho_ref = {V0 - Delta - rr:+.6f})')
        for name in ('E', 'P'):
            o = run_memoryless(name, Delta, us=us)
            arr = np.array([(x[0], x[1], x[2]) for x in o])
            post = arr[(arr[:, 0] > 1.5) & (arr[:, 0] <= 8.0)]
            relerr = np.max(np.abs(post[:, 1] / post[:, 2] - 1))
            print(f'{name}: max |H^2/rho_nc - 1| for 1.5 < u <= 8 = {relerr:.3e}; X/rho_nc at u=8: {(post[-1,1]-post[-1,2])/post[-1,2]:+.3e} '
                  f'(rho_nc(u=8) = {post[-1,2]:.3e}; a Lambda-like X would give X/rho_nc ~ 1e10)')
            pre = arr[arr[:, 0] < -1.0]
            print(f'   pre-transition max |H^2/rho_nc - 1| = {np.max(np.abs(pre[:,1]/pre[:,2]-1)):.3e}  '
                  f'(mixture estimator error; P exact, E Cauchy-Schwarz low)')
        # memory rules: initial data tuned so that Delta = 0.3 ends at X = 0 for U and GR
        st0 = state(-2.0, Delta)
        for name in ('U', 'GRb', 'R', 'F'):
            if name == 'U':
                H2i = st0['rho_nc'] + 0.3   # H^2 = rho_tot + C with C = -(final vacuum for Delta=0.3) = -0.7
            else:
                H2i = st0['rho_nc']         # flat start (GRb: rho_v + Lambda_b/3 = 0.3 initially... see note)
            if name == 'GRb':
                H2i = st0['rho_nc'] + V0 + LB
            LASTP[0] = st0['rho_nc']
            if name == 'F':
                sol = run_memory('F', Delta, 1e-3)   # initial curvature X_i = 1e-3 (open), any value
                uu = sol.t[-1]; Xe = sol.y[0, -1]
                print(f'F: X a^2 conserved: X*a^2 at u=-2: {1e-3*np.exp(-4):.4e}, at u={uu:.1f}: {Xe*np.exp(2*uu):.4e} '
                      f'(no kick; H^2 = rho_P + X, rho_P exact after the transient)')
                continue
            if name in ('U', 'GRb'):
                sol = run_memory(name, Delta, H2i, u_span=(-2.0, 3.0))
                st3 = state(sol.t[-1], Delta)
                Cc = sol.y[0, -1] ** 2 - st3['rho_tot']
                if name == 'U':
                    print(f'{name}: first integral C = H^2 - rho_tot at u={sol.t[-1]:.1f}: {Cc:+.9f} (initial {H2i - st0["rho_tot"]:+.9f}); '
                          f'implied late X = rho_v,final + C = {V0 - Delta + Cc:+.6f}  (<0 => freeze, >0 => de Sitter)')
                else:
                    print(f'{name}: bare Lambda/3 = {LB:+.3f}; implied late X = rho_v,final + Lambda_b/3 = {V0 - Delta + LB:+.6f}')
                continue
            sol = run_memory(name, Delta, H2i)
            if sol.status == 1 or sol.y[0, -1] < 1e-6:
                Xk = sol.y[0, -1] ** 2 - state(sol.t[-1], Delta)['rho_nc']
                msg = ''
                if name == 'R':
                    for uk in (-1.0, 1.0, 1.5):
                        Hk = sol.sol(uk)[0]; Xk = Hk ** 2 - state(uk, Delta)['rho_nc']
                        msg += f' X*a^2(u={uk})={Xk*np.exp(2*uk):+.4f};'
                    msg += f' expected kick -Delta*a_T^2 = {-Delta:+.2f}'
                print(f'{name}: FROZEN (H -> 0, no site destruction) at u = {sol.t[-1]:.3f}.' + msg)
                continue
            uu = sol.t[-1]
            H = sol.y[0, -1]
            rnc = state(uu, Delta)['rho_nc']
            X = H ** 2 - rnc
            u5 = 5.0
            H5 = sol.sol(u5)[0]; X5 = H5 ** 2 - state(u5, Delta)['rho_nc']
            print(f'{name}: X at u={uu:.1f}: {X:+.6e}; X/rho_nc = {X/rnc:+.3e}; X*a^2 at u=5,{uu:.0f}: {X5*np.exp(2*u5):+.4e}, {X*np.exp(2*uu):+.4e} (curvature-like if equal)')
    # stability of the derivative feedback H_new^3 = H_old * H_F^2
    Hs, HF = sp.symbols('H H_F', positive=True)
    g = (Hs * HF ** 2) ** sp.Rational(1, 3)
    print('\n# D-rule feedback map H -> (H H_F^2)^(1/3): derivative at fixed point =',
          sp.simplify(sp.diff(g, Hs).subs(Hs, HF)))
