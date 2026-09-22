#!/usr/bin/env python3
"""J:derive:bound-bodies-and-the-two-far-fields:a1 -- exact checks.

Block 60's setting (supplied clauses, nothing adopted): rates w = e^u and one length l = e^lam per site, chi = sqrt(l),
N = w chi; the content's bonds are crossed at sqrt(w_x w_y)/(chi_x chi_y) and a rest term (block 77) is timed by the
clock, rho_z w_z; the curvature member's field energy in bond form F = -8K sum_bonds (N_y - N_x)(chi_y - chi_x), with
the walls held at w = l = 1.  Block 66 T3's relabelling G_xi = (1/2) sum_j {xi_j, S_j} on a box with walls.
All checks are exact: sympy symbols, sympy rationals and exact complex matrices.
"""
import sys
from itertools import product
import sympy as sy

OUT = []
FAIL = []


def rec(msg):
    OUT.append(msg)


def need(cond, msg):
    if not cond:
        FAIL.append(msg)


K = sy.symbols("K", positive=True)


# ------------------------------------------ (a) the two field equations and the two charges, from the bond form
def box_graph(shape):
    """interior sites of a box and its walls; bonds among interior sites and from interior sites to walls"""
    inner = list(product(*[range(1, L + 1) for L in shape]))
    iset = set(inner)
    bonds_in, bonds_wall = [], []
    for s in inner:
        for a in range(len(shape)):
            t = list(s)
            t[a] += 1
            t = tuple(t)
            if t in iset:
                bonds_in.append((s, t))
            else:
                bonds_wall.append((s, t))
            t2 = list(s)
            t2[a] -= 1
            t2 = tuple(t2)
            if t2 not in iset:
                bonds_wall.append((s, t2))
    return inner, bonds_in, bonds_wall


ok_a = True
for shape in ((3,), (2, 2)):
    inner, bin_, bwall = box_graph(shape)
    u = {s: sy.Symbol("u_%s" % "".join(map(str, s)), real=True) for s in inner}
    lm = {s: sy.Symbol("l_%s" % "".join(map(str, s)), real=True) for s in inner}
    h = {b: sy.Symbol("h_%d" % k) for k, b in enumerate(bin_)}           # bond energies at w = l = 1
    rho = {s: sy.Symbol("r_%s" % "".join(map(str, s))) for s in inner}   # rest energies at w = 1
    w = {s: sy.exp(u[s]) for s in inner}
    chi = {s: sy.exp(lm[s] / 2) for s in inner}
    Nn = {s: w[s] * chi[s] for s in inner}

    def CH(s):
        return chi.get(s, 1)

    def NN(s):
        return Nn.get(s, 1)

    Hc = sum(h[(x, y)] * sy.sqrt(w[x] * w[y]) / (chi[x] * chi[y]) for (x, y) in bin_)
    Hc += sum(rho[s] * w[s] for s in inner)
    Fb = -8 * K * sum((NN(y) - NN(x)) * (CH(y) - CH(x)) for (x, y) in bin_ + bwall)
    nbr = {s: [] for s in inner}
    for (x, y) in bin_:
        nbr[x].append(y)
        nbr[y].append(x)
    for (x, y) in bwall:
        nbr[x].append(y)

    def lap(f, s):
        return sum(f(t) - f(s) for t in nbr[s])

    for s in inner:
        e_s = sy.diff(Hc, u[s])
        t_s = -sy.diff(Hc, lm[s])
        ok_a &= sy.simplify(e_s - t_s - rho[s] * w[s]) == 0                   # e - tau = rest energy
        ok_a &= sy.simplify(sy.diff(Fb, u[s]) - 8 * K * Nn[s] * lap(CH, s)) == 0
        ok_a &= sy.simplify(sy.diff(Fb, lm[s]) - 4 * K * (Nn[s] * lap(CH, s) + chi[s] * lap(NN, s))) == 0
        # stationarity in u_s and lam_s solved for the two Laplacians
        Lc, Ln = sy.symbols("Lc Ln")
        sol = sy.solve([e_s + 8 * K * Nn[s] * Lc, -t_s + 4 * K * (Nn[s] * Lc + chi[s] * Ln)], [Lc, Ln], dict=True)[0]
        ok_a &= sy.simplify(sol[Lc] + e_s / (8 * K * Nn[s])) == 0
        ok_a &= sy.simplify(sol[Ln] - (e_s + 2 * t_s) / (8 * K * chi[s])) == 0
need(ok_a, "(a) field equations")
# the charges and their difference; the pinned point body of block 60 T4
e, t, ww, ch = sy.symbols("e tau w chi", positive=True)
Qz, Pz = e / (8 * K * ww * ch), (e + 2 * t) / (8 * K * ch)
ok = sy.simplify(Pz - Qz - (2 * t - e * (1 / ww - 1)) / (8 * K * ch)) == 0
m = sy.symbols("m", positive=True)
ok &= sy.simplify((Qz * ch).subs({t: 0, e: m * ww}) - m / (8 * K)) == 0     # Q chi = m/(8K)
ok &= sy.simplify((Pz - Qz * ww).subs({t: 0, e: m * ww})) == 0              # P = Q w
need(ok, "(a) charges")
rec("ok (a) on a 3-site line and a 2x2 box (symbolic rates, lengths, bond and rest energies): e = dH/du and "
    "tau = -dH/dlam differ exactly by the rest energy rho w; dF/du_z = 8K N_z Lap(chi)_z and dF/dlam_z = "
    "4K[N_z Lap(chi)_z + chi_z Lap(N)_z]; stationarity gives Lap chi = -e/(8K N), Lap N = (e + 2 tau)/(8K chi); "
    "so Q = sum e/(8KN), P = sum (e+2tau)/(8K chi) and P - Q = (1/8K) sum [2 tau - e(1/w - 1)]/chi; a pinned "
    "body (tau = 0, e = m w) has Q chi = m/(8K) and P = Q w, block 60 T4")

# ------------------------------------------ (c) light-like content and (b) the weak field
P_l, Q_l = (e + 2 * e) / (8 * K * ch), e / (8 * K * ww * ch)                 # tau = e: no rest term
ok = sy.simplify(P_l - 3 * Q_l - 3 * e * (ww - 1) / (8 * K * ww * ch)) == 0
eps, U, Lb, T = sy.symbols("epsilon U Lambda T")
diff_w = (2 * T * eps - e * (sy.exp(-eps * U) - 1)) / sy.exp(eps * Lb / 2)    # u, lam, tau/e all of order eps
ser = sy.series(diff_w, eps, 0, 3).removeO()
ok &= sy.expand(ser - ((2 * T + e * U) * eps - (e * U ** 2 / 2 + e * U * Lb / 2 + T * Lb) * eps ** 2)) == 0
need(ok, "(b),(c) expansions")
rec("ok (c) content without a rest term has e = tau at every site and every strength, so P = 3 sum e/(8K chi), "
    "Q = sum e/(8K w chi) and P - 3Q = (3/8K) sum e(w-1)/(w chi) exactly: P = 3Q at weak field; (b) with u, lam "
    "and tau/e of order eps (a bound body's hop energy is of the order of its binding), 8K(P - Q) = "
    "sum (2 tau + e u) + O(eps^2 e): P = Q at leading order iff 2 tau_tot = -sum e u")


# ------------------------------------------ (b) the lattice virial on a box with walls: block 66 T3 with xi = x
def box_ops(shape):
    sites = list(product(*[range(L) for L in shape]))
    ix = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    Ts = []
    for a in range(len(shape)):
        T_ = sy.zeros(n)
        for s in sites:
            t_ = list(s)
            t_[a] += 1
            if tuple(t_) in ix:
                T_[ix[s], ix[tuple(t_)]] = 1                       # (T psi)(x) = psi(x + e_a), 0 past the wall
        Ts.append(T_)
    return sites, ix, Ts


shape = (3, 2)
sites, ix, Ts = box_ops(shape)
n = len(sites)
I2 = sy.eye(2)
PA = [sy.Matrix([[0, 1], [1, 0]]), sy.Matrix([[0, -sy.I], [sy.I, 0]]), sy.Matrix([[1, 0], [0, -1]])]
Ss = [(T_ - T_.T) / (2 * sy.I) for T_ in Ts]
Cs = [(T_ + T_.T) / 2 for T_ in Ts]


def kr(A, B):
    return sy.kronecker_product(A, B)


H = sum((kr(Ss[a], PA[a]) for a in range(len(shape))), sy.zeros(2 * n))
Xs = [sy.diag(*[s[j] for s in sites]) for j in range(len(shape))]
G = sum((kr((Xs[j] * Ss[j] + Ss[j] * Xs[j]) / 2, I2) for j in range(len(shape))), sy.zeros(2 * n))
H2s = sum((kr((Ts[a] ** 2 - (Ts[a].T) ** 2) / (4 * sy.I), PA[a]) for a in range(len(shape))), sy.zeros(2 * n))
ok = all(sy.simplify((Cs[a] * Ss[a] + Ss[a] * Cs[a]) / 2 - (Ts[a] ** 2 - (Ts[a].T) ** 2) / (4 * sy.I))
         == sy.zeros(n) for a in range(len(shape)))
ok &= sy.simplify(sy.I * (H * G - G * H) - H2s) == sy.zeros(2 * n)
phiv = [sy.Rational(k + 2, k + 3) for k in range(n)]                  # any positive rates
Phi = sy.diag(*phiv)


def Cw(j, f):
    """C_j[d_j f]: the symmetric hop weighted by the bond difference of f (interior bonds only)"""
    M_ = sy.zeros(n)
    for s in sites:
        t_ = list(s)
        t_[j] += 1
        if tuple(t_) in ix:
            a_, b_ = ix[s], ix[tuple(t_)]
            v = f[b_] - f[a_]
            M_[a_, b_] += v / 2
            M_[b_, a_] += v / 2
    return M_


Lam = sum((kr((Xs[j] * Cw(j, phiv) + Cw(j, phiv) * Xs[j]) / 2, I2) for j in range(len(shape))), sy.zeros(2 * n))
Pk = kr(Phi, I2)
Hw = Pk * H * Pk
ok &= all(sy.simplify(sy.I * (Phi * Ss[j] - Ss[j] * Phi) + Cw(j, phiv)) == sy.zeros(n) for j in range(len(shape)))
ok &= sy.simplify(sy.I * (Hw * G - G * Hw) - (Pk * H2s * Pk - (Lam * H * Pk + Pk * H * Lam))) == sy.zeros(2 * n)
need(ok, "(b) lattice virial identity on the box")
# the staggered rest term: the one-step relabelling does not commute with it, the two-step one does
Eps = kr(sy.diag(*[(-1) ** sum(s) for s in sites]), I2)
Gp = sum((kr((Xs[j] * Ss[j] * Cs[j] + Ss[j] * Cs[j] * Xs[j]) / 2, I2) for j in range(len(shape))), sy.zeros(2 * n))
ok = sy.simplify(Eps * G - G * Eps - 2 * Eps * G) == sy.zeros(2 * n) and Eps * G != G * Eps
ok &= sy.simplify(Eps * Gp - Gp * Eps) == sy.zeros(2 * n)
ok &= sy.simplify(Eps * H + H * Eps) == sy.zeros(2 * n)
need(ok, "(b) staggered term and the two relabellings")
rec("ok (b) block 66 T3 with xi = x holds exactly on a 3x2 box with walls: (1/2){C_a,S_a} is exactly the truncated "
    "two-step hop (T_a^2 - T_a^+2)/(4i), i[H,G_x] = H2 := sum s_a (T_a^2 - T_a^+2)/(4i) with no wall operator, and "
    "i[phi H phi, G_x] = phi H2 phi - (Lam H phi + phi H Lam) for rational positive rates; so every stationary state "
    "on the box has <phi psi|H2|phi psi> = sum x.f exactly, and a free confined state has <H2> = 0 while its hop "
    "energy is E: the walls absorb the whole kinetic term; the staggered rest term eps has [eps,G_x] = 2 eps G_x "
    "(no virial for massive content from G_x) but commutes with G_P = (1/2) sum {x_j, S_j C_j}")

print("\n".join(OUT))
print("SUMMARY: " + ("ROUTE FAILS AT " + FAIL[0] if FAIL else
      "PARTIAL the supervisor's field equations and P - Q = (1/8K) sum [2 tau - e(1/w - 1)]/chi are re-derived "
      "exactly from block 60's bond form (e - tau = rest energy; pinned body P = Q w); content without a rest term "
      "has e = tau exactly, so P - 3Q = (3/8K) sum e(w-1)/(w chi); at weak field P = Q iff 2 tau = -sum e u, which the "
      "virial theorem supplies at leading order for a self-bound body (no failure of P = Q at leading order); block "
      "66 T3 with xi = x is exact on a box with no wall operator, and for staggered massive content the virial "
      "needs the two-step relabelling."))
if not FAIL:
    print("HIT: from block 60's bond form F = -8K sum (N_y - N_x)(chi_y - chi_x) with bonds crossed at "
          "sqrt(w_x w_y)/(chi_x chi_y): Lap chi = -e/(8KN), Lap N = (e + 2 tau)/(8K chi) exactly, e - tau = the "
          "rest energy, P - Q = (1/8K) sum [2 tau - e(1/w - 1)]/chi at every strength; content without a rest "
          "term has e = tau pointwise, hence P - 3Q = (3/8K) sum e(w-1)/(w chi) exactly.")
    print("HIT: on a box with walls i[phi H phi, G_x] = phi H2 phi - (Lam H phi + phi H Lam) exactly with H2 the "
          "truncated two-step walk and no wall operator (a free confined state has <H2> = 0), while the staggered "
          "rest term gives [eps, G_x] = 2 eps G_x and [eps, G_P] = 0 for G_P = (1/2) sum {x_j, S_j C_j}: the "
          "lattice virial for massive content must use the two-step relabelling.")
sys.exit(1 if FAIL else 0)
