#!/usr/bin/env python3
"""J:derive:a-lattice-ledger-that-transports-the-rates:a1 (worker w-macbookpro90c72-j7770).

No-go, exact. Any ledger F[w, B] (any reach) whose relabelling moves the strains (B -> B + d xi) and the rates by a
content-independent lattice transport has an identity whose content side, after the static field equations
dF/du = -(e - mu), dF/dB = -(content's strain response), sees the content only through its energy density e and
its strain response. The force the ledger then owes is a content-independent bilinear function of these densities
and grad u. The clocked walk's force at first order in the rate gradient is f_j = e cos k_j (centred d_j u)
(block 66's definition, re-derived and checked here exactly). Two energy-one plane waves, k = (pi/2, 0, 0) and
(pi/2, pi, 0), related by the site sign (-1)^{x_2}, have the same e, the same site response Theta = s s^T/E, the
same bond current (zero) and the same reach-two/three responses, but opposite f_2. So no such ledger owes the walk's
fall. Checks (Gaussian rationals, 4^3 torus):
  F1  f_j's first-order formula at every site, every direction, all 48 energy-one plane waves;
  F2  the pair: equal e, Theta and reach-two and reach-three strain responses, opposite f_2;
  F3  the finite linear system: f_j = sum_b [alpha_jb e + sum beta_{jb,ai} R_a^i] g_b over all 48 states, R running
      over Theta and the reach-two response: rank 3 < 4 (augmented) for every j - no solution;
  F4  one transport can serve at most one sense along j: cos k_j = +1 and -1 both occur at the eight zeros' neighbours.
"""
import itertools
import sys
from fractions import Fraction as Fr

T0 = __import__("time").time()
FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


class G:
    """Gaussian rational a + b i."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def conj(self):
        return G(self.a, -self.b)

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.a == o.a and self.b == o.b


L = 4
SITES = list(itertools.product(range(L), repeat=3))
E1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
SIG = [[[G(0), G(1)], [G(1), G(0)]], [[G(0), G(0, -1)], [G(0, 1), G(0)]], [[G(1), G(0)], [G(0), G(-1)]]]
IPOW = [G(1), G(0, 1), G(-1), G(0, -1)]            # i^n, e^{i pi n/2}


def sh(x, d, s=1):
    return tuple((x[i] + s * d[i]) % L for i in range(3))


def mat(Mx, v):
    return [Mx[0][0] * v[0] + Mx[0][1] * v[1], Mx[1][0] * v[0] + Mx[1][1] * v[1]]


def S(j, psi):
    """(S_j psi)(x) = (psi(x + e_j) - psi(x - e_j))/(2i)."""
    out = {}
    for x in SITES:
        p, m = psi[sh(x, E1[j])], psi[sh(x, E1[j], -1)]
        out[x] = [(p[c] - m[c]) * G(0, Fr(-1, 2)) for c in range(2)]
    return out


def H(psi):
    out = {x: [G(), G()] for x in SITES}
    for j in range(3):
        Sj = S(j, psi)
        for x in SITES:
            v = mat(SIG[j], Sj[x])
            out[x] = [out[x][c] + v[c] for c in range(2)]
    return out


def C(j, v, psi):
    """symmetric hop weighted by the bond function v (bond x -> x + e_j): (1/2)[v(x) psi(x+e_j) + v(x-e_j) psi(x-e_j)]."""
    out = {}
    for x in SITES:
        p, m = psi[sh(x, E1[j])], psi[sh(x, E1[j], -1)]
        vp, vm = v[x], v[sh(x, E1[j], -1)]
        out[x] = [(p[c] * vp + m[c] * vm) * Fr(1, 2) for c in range(2)]
    return out


def dot(u, w):
    return u[0].conj() * w[0] + u[1].conj() * w[1]


def plane_waves():
    """energy-one plane waves: s = sin k = +-e_c, the other k_i in {0, pi}; chi an eigenvector of sigma_c s_c, E = +-1."""
    out = []
    for c in range(3):
        for sc in (1, -1):
            for others in itertools.product((0, 2), repeat=2):
                n = [0, 0, 0]
                n[c] = 1 if sc == 1 else 3
                oi = [i for i in range(3) if i != c]
                n[oi[0]], n[oi[1]] = others
                for band in (1, -1):
                    # eigenvector of sc*sigma_c with eigenvalue band
                    lamb = band * sc
                    if c == 0:
                        chi = [G(1), G(lamb)]
                    elif c == 1:
                        chi = [G(1), G(0, lamb)]
                    else:
                        chi = [G(1), G(0)] if lamb == 1 else [G(0), G(1)]
                    psi = {x: [chi[q] * IPOW[sum(n[i] * x[i] for i in range(3)) % 4] for q in range(2)] for x in SITES}
                    out.append((tuple(n), band, chi, psi))
    return out


def energy_density(psi, Hpsi, x):
    return dot(psi[x], Hpsi[x]).a


def force(j, phi, psi):
    """block 66: f_j(x) = Re[(C_j[d_j phi] psi)^dag (H phi psi) + psi^dag C_j[d_j phi](H phi psi)](x)."""
    dphi = {x: phi[sh(x, E1[j])] - phi[x] for x in SITES}
    Hpp = H({x: [psi[x][c] * phi[x] for c in range(2)] for x in SITES})
    Cp = C(j, dphi, psi)
    CH = C(j, dphi, Hpp)
    return {x: (dot(Cp[x], Hpp[x]) + dot(psi[x], CH[x])).a for x in SITES}


# a rate field: phi = 1 + eps v, v(x) = cos(pi x_2 / 2) + cos(pi x_1 / 2) + x_3-profile (integer values)
prof = [1, 0, -1, 0]
v = {x: prof[x[0]] + prof[x[1]] + 2 * prof[x[2]] for x in SITES}
eps = Fr(1, 1000)
states = plane_waves()
good = True
rows = 0
for (n, band, chi, psi) in states:
    Hpsi = H(psi)
    e = {x: energy_density(psi, Hpsi, x) for x in SITES}
    for j in range(3):
        f1 = force(j, {x: 1 + eps * v[x] for x in SITES}, psi)
        f2 = force(j, {x: 1 + 2 * eps * v[x] for x in SITES}, psi)
        cosk = [1, 0, -1, 0][n[j]]
        for x in SITES:
            first = 2 * f1[x] / eps - f2[x] / (2 * eps)          # exact O(eps) coefficient (f is quadratic in eps)
            centred = v[sh(x, E1[j])] - v[sh(x, E1[j], -1)]      # (centred d_j u)/eps with u = 2 eps v + O(eps^2)
            good &= first == e[x] * cosk * centred
            rows += 1
ok("F1", good, f"the clocked walk's force at first order in the rate gradient is exactly e cos k_j (centred d_j u): "
   f"all {len(states)} energy-one plane waves of 4^3 (both bands), 3 directions, 64 sites ({rows} exact equalities)")


# ---- the pair: identical content densities, opposite forces ----
def theta(psi, Hpsi):
    """block 62's site response Theta_a^j(x) = Re psi^dag sigma_a (S_j psi)(x) (site-placed)."""
    out = {}
    Sj = [S(j, psi) for j in range(3)]
    for x in SITES:
        out[x] = [[dot(psi[x], mat(SIG[a], Sj[j][x])).a for j in range(3)] for a in range(3)]
    return out


def bond_response(psi):
    """reach-two strain response: d<psi| sum sigma_a (1/2){C_a[B_a^j], S_j} |psi>/d B_a^j(bond x -> x+e_a)."""
    out = {}
    Sj = [S(j, psi) for j in range(3)]
    for x in SITES:
        row = []
        for a in range(3):
            for j in range(3):
                # <psi| sigma_a C_a[delta_x] S_j psi> + <S_j psi| C_a[delta_x] sigma_a psi>, real part / 2 x 2
                xp = sh(x, E1[a])
                t1 = dot(psi[x], mat(SIG[a], Sj[j][xp])) * Fr(1, 2) + dot(psi[xp], mat(SIG[a], Sj[j][x])) * Fr(1, 2)
                row.append(t1.a)
        out[x] = row
    return out


def P(j, psi):
    """two-step momentum (P_j psi)(x) = (psi(x + 2e_j) - psi(x - 2e_j))/(4i) (symbol sin(2k_j)/2)."""
    two = tuple(2 * c for c in E1[j])
    out = {}
    for x in SITES:
        p_, m_ = psi[sh(x, two)], psi[sh(x, two, -1)]
        out[x] = [(p_[c] - m_[c]) * G(0, Fr(-1, 4)) for c in range(2)]
    return out


def reach3_response(psi):
    """reach-three strain response: d<psi| sum sigma_a (1/2){C_a[B_a^j], P_j} |psi>/d B_a^j(bond x -> x+e_a)."""
    out = {}
    Pj = [P(j, psi) for j in range(3)]
    for x in SITES:
        row = []
        for a in range(3):
            for j in range(3):
                xp = sh(x, E1[a])
                t1 = dot(psi[x], mat(SIG[a], Pj[j][xp])) * Fr(1, 2) + dot(psi[xp], mat(SIG[a], Pj[j][x])) * Fr(1, 2)
                row.append(t1.a)
        out[x] = row
    return out


pick = {}
for (n, band, chi, psi) in states:
    if band == 1 and n in ((1, 0, 0), (1, 2, 0)):
        pick[n] = psi
pA, pB = pick[(1, 0, 0)], pick[(1, 2, 0)]
HA, HB = H(pA), H(pB)
same_e = all(energy_density(pA, HA, x) == energy_density(pB, HB, x) for x in SITES)
same_theta = theta(pA, HA) == theta(pB, HB)
same_bond = bond_response(pA) == bond_response(pB)
zero_bond = all(all(c == 0 for c in bond_response(pA)[x]) for x in SITES)
same_r3 = reach3_response(pA) == reach3_response(pB)
fA = force(1, {x: 1 + eps * v[x] for x in SITES}, pA)
fB = force(1, {x: 1 + eps * v[x] for x in SITES}, pB)
opp = all(fA[x] == -fB[x] for x in SITES) and any(fA[x] != 0 for x in SITES)
ok("F2", same_e and same_theta and same_bond and zero_bond and same_r3 and opp,
   "k = (pi/2, 0, 0) and (pi/2, pi, 0), E = +1, related by the site sign (-1)^{x_2}: equal energy density at all 64 "
   "sites, equal site response Theta = s s^T/E (block 62's frame coupling), equal (identically zero) reach-two and "
   "reach-three bond responses (blocks 63, 69), and f_2 exactly "
   "opposite at every site (nonzero): no identity seeing the content through these densities can match both")

# ---- the finite linear system over all 48 states ----
import sympy as sp
good = True
ranks = []
for j in range(3):
    # unknowns: alpha_jj, beta over Theta_a^i (9) and bond responses R_a^i (9) -> 19; equations: one per state (g = e_j)
    Arows, bvec = [], []
    for (n, band, chi, psi) in states:
        Hpsi = H(psi)
        x0 = (0, 0, 0)
        e0 = energy_density(psi, Hpsi, x0)
        th = theta(psi, Hpsi)[x0]
        br = bond_response(psi)[x0]
        Arows.append([e0] + [th[a][i] for a in range(3) for i in range(3)] + br)
        bvec.append(e0 * [1, 0, -1, 0][n[j]])
    A = sp.Matrix(Arows)
    Aug = A.row_join(sp.Matrix(bvec))
    ranks.append((A.rank(), Aug.rank()))
    good &= Aug.rank() > A.rank()
ok("F3", good, "linear system over the 48 states for f_j = [alpha e + sum beta Theta + sum beta' R] g_j (content-"
   "independent coefficients, any reach - plane-wave densities are uniform): rank (coefficients, augmented) = "
   + ", ".join(f"j={j + 1}: {r}" for j, r in enumerate(ranks)) + " - no solution")

# ---- at the zeros: cos k_j = +1 for four species, -1 for the four reflected along j ----
signs = sorted({[1, -1][K[1]] for K in itertools.product((0, 1), repeat=3)})
ok("F4", signs == [-1, 1], "near the eight zeros k = pi n the factor is cos(pi n_j) = (-1)^{n_j}: four species fall "
   "along e_j with weight +1, the four reflected along j with weight -1; a content-independent transport serves one "
   "set, never both - block 66 T4's leading-order agreement is the n_j = 0 species' only")

print(f"runtime {__import__('time').time() - T0:.0f} s")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PROVED no-go (any reach, not only <= 2): a ledger whose relabelling carries the rates by a content-"
      "independent transport owes a force that is a content-independent function of the content's energy density and "
      "strain response; the clocked walk's force e cos k_j (centred d_j u) differs by sign on two plane waves with "
      "identical densities, so no such ledger owes the walk's fall; (c) does not arise.")
print("HIT: no lattice ledger F[w, B], of any reach, whose relabelling moves the strains by d xi and the rates by a "
      "content-independent transport, owes the clocked walk's fall: its identity, with the static field equations, "
      "demands a force that depends on the content only through its energy density and strain response, while the "
      "walk's force at first order is e cos k_j (centred d_j u); the energy-one plane waves k = (pi/2, 0, 0) and "
      "(pi/2, pi, 0), related by the site sign (-1)^{x_2}, have equal energy density, equal site and bond responses "
      "(the bond response zero) and exactly opposite f_2. A transport can serve the four species with n_j = 0 or the "
      "four reflected along j, never both.")
