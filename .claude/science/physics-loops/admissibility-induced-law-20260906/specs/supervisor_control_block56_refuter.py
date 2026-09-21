"""Block 56 refuting pass (supervisor-run; machinery disjoint from the runner: a direct non-linear solve in u = log w with no division by phi,
finite differences of the ledger, random arrangements, symbolic algebra, and a second bond energy of weight one).
W1  the clock law solved as a NON-LINEAR system in u on a 7^3 box (scipy root) against the linear solve in phi.
W2  the ledger at that solution: stationary under every interior variation of u (finite differences); the sum of its derivatives over the wall
    sites equals the ledger; equal to sum m phi.
W3  symbolic two-body problem: closed form of the ledger; the defect's leading term (gamma/6) m_1 m_2 c, its exact form in the 'charges' m phi, and the
    sign of d(ledger)/dc at any field strength.
W4  forty random arrangements with random bare energies: 0 < phi < 1, the ledger rises when any bare energy is raised, and stays below
    (12/gamma) Cap(B).
W5  a SECOND bond energy of weight one, (1/gamma) sum (w_x - w_y)^2/(w_x + w_y) (same second order): its static law is not linear in phi; solved as
    a non-linear system for one body: the ledger is still the sum over wall sites of dF/du_x (the surface term is general); phi_0 agrees at weak field,
    differs at strong field, and the clock at the body stops at the FINITE bare energy 18/gamma, beyond which no static solution has a positive rate there.
W6  (a) symbolic rates on a 3x3x3 torus: a nearest-neighbour energy bilinear in the root rates, alpha sum phi^2 + sum_e beta_e sum phi_x phi_(x+e), with
    equal beta_e (covariance) and a vanishing derivative at uniform rates, is -(beta/2) sum over bonds (phi_x - phi_y)^2.  (b) a random complex
    two-component amplitude under the walk with the qubit as coin on the 7^3 box: K_xy = Re chi_x^dagger H_xy chi_y; the solution of the LINEAR
    problem ((12/gamma)(1 - A) + K) phi = 0 satisfies the clock law with e_x computed directly from H_w = phi H phi."""
import sys

import numpy as np
import sympy as sp
from scipy.optimize import root

results = []
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
SIDE = 7
INTERIOR = [(x, y, z) for x in range(1, SIDE - 1) for y in range(1, SIDE - 1) for z in range(1, SIDE - 1)]
INDEX = {s: i for i, s in enumerate(INTERIOR)}
WALLS = [(x, y, z) for x in range(SIDE) for y in range(SIDE) for z in range(SIDE) if (x, y, z) not in INDEX]
BONDS = [((x, y, z), (x + d[0], y + d[1], z + d[2])) for x in range(SIDE) for y in range(SIDE) for z in range(SIDE) for d in NEIGH[::2] if max(x + d[0], y + d[1], z + d[2]) < SIDE]
GAMMA = 0.6


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


def full(u_int, u_wall=None):
    u = np.zeros((SIDE,) * 3)
    for s, i in INDEX.items():
        u[s] = u_int[i]
    if u_wall is not None:
        for s, v in zip(WALLS, u_wall):
            u[s] = v
    return u


def ledger_one(u, masses):
    phi = np.exp(u / 2)
    return sum(m * phi[s] ** 2 for s, m in masses.items()) + 2 / GAMMA * sum((phi[a] - phi[b]) ** 2 for a, b in BONDS)


def ledger_two(u, masses):
    w = np.exp(u)
    return sum(m * w[s] for s, m in masses.items()) + 1 / GAMMA * sum((w[a] - w[b]) ** 2 / (w[a] + w[b]) for a, b in BONDS)


def linear_phi(masses):
    n = len(INTERIOR)
    a = np.zeros((n, n)); b = np.zeros(n)
    for s, i in INDEX.items():
        a[i, i] = 1 + GAMMA / 12 * masses.get(s, 0.0)
        for d in NEIGH:
            t = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
            if t in INDEX:
                a[i, INDEX[t]] -= 1 / 6
            else:
                b[i] += 1 / 6
    return np.linalg.solve(a, b)


def grad(fn, u_int, masses, h=1e-6):
    g = np.zeros(len(u_int))
    for i in range(len(u_int)):
        e = np.zeros(len(u_int)); e[i] = h
        g[i] = (fn(full(u_int + e), masses) - fn(full(u_int - e), masses)) / (2 * h)
    return g


# ------------------------------------------------------------------------------------------------ W1
masses = {(2, 3, 3): 2.0, (4, 3, 2): 5.0, (3, 5, 4): 1.5}


def residual(u_int):
    u = full(u_int)
    phi = np.exp(u / 2)
    out = np.zeros(len(u_int))
    for s, i in INDEX.items():
        avg = sum(phi[s[0] + d[0], s[1] + d[1], s[2] + d[2]] for d in NEIGH) / 6
        out[i] = 12 / GAMMA * phi[s] * (phi[s] - avg) + masses.get(s, 0.0) * phi[s] ** 2
    return out


sol = root(residual, np.zeros(len(INTERIOR)), method="hybr", tol=1e-13)
phi_lin = linear_phi(masses)
gap = np.max(np.abs(np.exp(sol.x / 2) - phi_lin))
report("W1", sol.success and gap < 1e-9, f"the clock law solved as a non-linear system in u (no division by phi) agrees with the linear solve in phi to {gap:.1e} at all 125 interior sites")

# ------------------------------------------------------------------------------------------------ W2
u_star = 2 * np.log(phi_lin)
g_int = grad(ledger_one, u_star, masses)
total = ledger_one(full(u_star), masses)
h = 1e-6
wall_sum = 0.0
for k in range(len(WALLS)):
    e = np.zeros(len(WALLS)); e[k] = h
    wall_sum += (ledger_one(full(u_star, e), masses) - ledger_one(full(u_star, -e), masses)) / (2 * h)
direct = sum(m * phi_lin[INDEX[s]] for s, m in masses.items())
report("W2", np.max(np.abs(g_int)) < 1e-7 and abs(wall_sum - total) < 1e-6 and abs(direct - total) < 1e-10,
       f"at the solution the ledger is stationary under every interior variation (largest derivative {np.max(np.abs(g_int)):.1e}); the sum of its derivatives over the 218 wall sites is {wall_sum:.6f} against the ledger {total:.6f}; sum m phi = {direct:.6f}")

# ------------------------------------------------------------------------------------------------ W3
a, b, c, d1, d2, gam, eps = sp.symbols("a b c d1 d2 gamma epsilon", positive=True)
mat = sp.Matrix([[1 + a * d1, c * d2], [c * d1, 1 + b * d2]])
phis = mat.LUsolve(sp.Matrix([1, 1]))
pair = 12 / gam * (d1 * phis[0] + d2 * phis[1])
alone = 12 / gam * (d1 / (1 + a * d1) + d2 / (1 + b * d2))
defect = sp.simplify(alone - pair)
lead = sp.series(defect.subs({d1: eps * d1, d2: eps * d2}), eps, 0, 3).removeO().coeff(eps, 2)
m1, m2 = sp.symbols("m1 m2", positive=True)
lead_m = sp.simplify(lead.subs({d1: gam * m1 / 12, d2: gam * m2 / 12}))
# exact: defect = (12/gamma) d1 d2 c (phi1_alone phi2 + phi2_alone phi1)
charges = 12 / gam * d1 * d2 * c * (phis[1] / (1 + a * d1) + phis[0] / (1 + b * d2))
slope = sp.simplify(sp.diff(pair, c) + 24 / gam * d1 * d2 * (1 + d1 * (a - c)) * (1 + d2 * (b - c)) / mat.det() ** 2)
report("W3", sp.simplify(lead_m - gam * m1 * m2 * c / 6) == 0 and sp.simplify(defect - charges) == 0 and slope == 0,
       f"symbolic pair: the defect's leading term is {lead_m}; exactly, defect = (gamma/12) c (m_1 phi_1^alone m_2 phi_2 + m_2 phi_2^alone m_1 phi_1): bilinear in the 'charges' m phi, one of each pair taken alone; and d(ledger)/dc = -(24/gamma) d_1 d_2 (1 + d_1 (a - c)) (1 + d_2 (b - c))/det^2 < 0 because c < a, b: the ledger falls as the mutual potential grows, at any field strength")

# ------------------------------------------------------------------------------------------------ W4
rng = np.random.default_rng(56)
free = np.zeros((len(INTERIOR), len(INTERIOR)))
for s, i in INDEX.items():
    free[i, i] = 1
    for d in NEIGH:
        t = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
        if t in INDEX:
            free[i, INDEX[t]] -= 1 / 6
green = np.linalg.inv(free)
ok = True
worst_ratio = 0.0
for _ in range(40):
    k = int(rng.integers(1, 12))
    chosen = [INTERIOR[i] for i in rng.choice(len(INTERIOR), k, replace=False)]
    ms = {s: float(10 ** rng.uniform(-1, 4)) for s in chosen}
    phi = linear_phi(ms)
    led = sum(m * phi[INDEX[s]] for s, m in ms.items())
    gb = green[np.ix_([INDEX[s] for s in chosen], [INDEX[s] for s in chosen])]
    cap = np.ones(k) @ np.linalg.solve(gb, np.ones(k))
    raised = dict(ms); pick = chosen[int(rng.integers(0, k))]; raised[pick] *= 1.5
    phi_r = linear_phi(raised)
    led_r = sum(m * phi_r[INDEX[s]] for s, m in raised.items())
    ok = ok and 0 < phi.min() and phi.max() < 1 and led_r > led and led < 12 / GAMMA * cap and np.all(phi_r < phi + 1e-15)
    worst_ratio = max(worst_ratio, led / (12 / GAMMA * cap))
report("W4", ok, f"forty random arrangements (1 to 11 bodies, bare energies 0.1 to 10^4): 0 < phi < 1, raising any bare energy lowers every phi and raises the ledger, and the ledger stays below (12/gamma) Cap(B) (largest ratio {worst_ratio:.4f})")

# ------------------------------------------------------------------------------------------------ W5
centre = (3, 3, 3)


def second_law(m):
    ms = {centre: m}

    def res2(u_int):
        u = full(u_int)
        w = np.exp(u)
        r = np.zeros(len(u_int))
        for s, i in INDEX.items():
            acc = 0.0
            for d in NEIGH:
                t = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
                a_, b_ = w[s], w[t]
                acc += a_ * (a_ - b_) * (a_ + 3 * b_) / (a_ + b_) ** 2             # w_x d/dw_x of (w_x - w_y)^2/(w_x + w_y)
            r[i] = acc / GAMMA + ms.get(s, 0.0) * w[s]                             # coefficient 1/gamma: the same second order as the simplest energy
        return r

    s2 = root(res2, 2 * np.log(linear_phi(ms)), method="hybr", tol=1e-13)
    u2 = full(s2.x)
    led2 = ledger_two(u2, ms)
    wall2 = 0.0
    for k in range(len(WALLS)):
        e = np.zeros(len(WALLS)); e[k] = h
        wall2 += (ledger_two(full(s2.x, e), ms) - ledger_two(full(s2.x, -e), ms)) / (2 * h)
    return s2.success, led2, wall2, float(np.exp(u2[centre] / 2)), float(linear_phi(ms)[INDEX[centre]])


weak, strong, near, beyond = second_law(0.5), second_law(20.0), second_law(29.5), second_law(31.0)
ok = (weak[0] and strong[0] and near[0] and abs(weak[1] - weak[2]) < 1e-6 and abs(strong[1] - strong[2]) < 1e-5 and abs(weak[3] - weak[4]) < 1e-4
      and abs(strong[3] - strong[4]) > 0.05 and near[3] > 0.03 and (not beyond[0] or beyond[3] < 1e-4))
report("W5", ok, f"second bond energy of weight one, (1/gamma) sum (w_x - w_y)^2/(w_x + w_y) (non-linear static law, one body): m = 0.5: phi_0 = {weak[3]:.5f} against the simplest law's {weak[4]:.5f}, ledger {weak[1]:.6f} = wall sum {weak[2]:.6f}; m = 20: phi_0 = {strong[3]:.4f} against {strong[4]:.4f}, ledger {strong[1]:.5f} = wall sum {strong[2]:.5f}; m = 29.5: phi_0 = {near[3]:.4f}; m = 31 (beyond 18/gamma = {18 / GAMMA:.0f}): no static solution with a positive rate at the body (solver success {beyond[0]}, phi_0 -> {beyond[3]:.1e}).  The surface term is general; where and whether a clock stops depends on the bond energy")

# ------------------------------------------------------------------------------------------------ W6
side6 = 3
sites6 = [(x, y, z) for x in range(side6) for y in range(side6) for z in range(side6)]
ph = {s_: sp.Symbol(f"p{s_[0]}{s_[1]}{s_[2]}", positive=True) for s_ in sites6}
alpha, beta = sp.symbols("alpha beta", real=True)
bonds6 = [(s_, tuple((s_[i] + (1 if i == j else 0)) % side6 for i in range(3))) for s_ in sites6 for j in range(3)]
form = alpha * sum(ph[s_] ** 2 for s_ in sites6) + beta * sum(ph[a_] * ph[b_] for a_, b_ in bonds6)
uniform = sp.diff(form, ph[(0, 0, 0)]).subs({v: 1 for v in ph.values()})
alpha_star = sp.solve(sp.Eq(uniform, 0), alpha)[0]
part_a = sp.expand(form.subs(alpha, alpha_star) + beta / 2 * sum((ph[a_] - ph[b_]) ** 2 for a_, b_ in bonds6)) == 0 and alpha_star == -3 * beta

pauli = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
nint = len(INTERIOR)
hwalk = np.zeros((2 * nint, 2 * nint), complex)
for s_, i in INDEX.items():
    for j, d in enumerate(NEIGH[::2]):
        for sign in (+1, -1):
            t = (s_[0] + sign * d[0], s_[1] + sign * d[1], s_[2] + sign * d[2])
            if t in INDEX:
                hwalk[2 * INDEX[t]:2 * INDEX[t] + 2, 2 * i:2 * i + 2] += sign * 0.5j * pauli[j]
rng6 = np.random.default_rng(560)
chi6 = (rng6.normal(size=2 * nint) + 1j * rng6.normal(size=2 * nint)) * 0.6
kmat6 = np.zeros((nint, nint))
for i in range(nint):
    for j in range(nint):
        blk = hwalk[2 * i:2 * i + 2, 2 * j:2 * j + 2]
        if np.any(blk):
            kmat6[i, j] = np.real(np.vdot(chi6[2 * i:2 * i + 2], blk @ chi6[2 * j:2 * j + 2]))
lin = np.zeros((nint, nint)); rhs6 = np.zeros(nint)
for s_, i in INDEX.items():
    lin[i, i] = 1
    for d in NEIGH:
        t = (s_[0] + d[0], s_[1] + d[1], s_[2] + d[2])
        if t in INDEX:
            lin[i, INDEX[t]] -= 1 / 6
        else:
            rhs6[i] += 1 / 6
phi6 = np.linalg.solve(lin + GAMMA / 12 * kmat6, rhs6)
root6 = np.repeat(phi6, 2)
e6 = np.real((chi6.conj() * ((root6[:, None] * hwalk * root6[None, :]) @ chi6)).reshape(nint, 2).sum(axis=1))
full6 = np.ones((SIDE,) * 3)
for s_, i in INDEX.items():
    full6[s_] = phi6[i]
worst6 = 0.0
for s_, i in INDEX.items():
    avg = sum(full6[s_[0] + d[0], s_[1] + d[1], s_[2] + d[2]] for d in NEIGH) / 6
    worst6 = max(worst6, abs(12 / GAMMA * phi6[i] * (phi6[i] - avg) + e6[i]))
report("W6", part_a and phi6.min() > 0 and worst6 < 1e-12 and np.abs(kmat6 - np.diag(np.diag(kmat6))).max() > 0.05,
       f"(a) symbolic: alpha = {alpha_star} and the bilinear nearest-neighbour energy equals -(beta/2) sum over bonds (phi_x - phi_y)^2 identically; (b) a random complex amplitude under the walk with the qubit as coin on the 7^3 box: K has bond entries up to {np.abs(kmat6 - np.diag(np.diag(kmat6))).max():.2f} and no site entries; the linear solve satisfies the clock law with e_x from phi H phi to {worst6:.1e} (phi between {phi6.min():.3f} and {phi6.max():.3f}; above 1 where the amplitude's energy density is negative)")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
