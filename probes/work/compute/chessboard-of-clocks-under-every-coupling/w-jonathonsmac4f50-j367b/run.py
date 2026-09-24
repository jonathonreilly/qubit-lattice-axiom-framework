#!/usr/bin/env python3
"""Which supplied couplings see a chessboard of clock rates?  Exact (sympy rationals) on the 6x6x6 torus.

Chessboard: phi -> phi * c^eps, eps(x) = (-1)^(x1+x2+x3), c = 2 (rational; c^{+-2} = 4, 1/4).  A clocked term phi O phi has
matrix element phi_x phi_y O_xy between sites x, y; under the chessboard it is multiplied by c^(eps_x + eps_y), which is 1 when x and
y are on opposite sublattices (odd displacement) and c^(+-2) otherwise.  Each coupling is built with generic rational fields, a
generic rational base phi, and its exact change computed; energies likewise.
"""
import itertools, sys
import sympy as sp

FAIL = []
def out(s): print(s)
def check(name, cond):
    out(("PASS " if cond else "FAIL ") + name)
    if not cond: FAIL.append(name)

L = 6          # even (the chessboard is defined) and > 4 (on side 4 the two-step momentum P_j vanishes: T^2 = T^-2)
S = list(itertools.product(range(L), repeat=3)); N = len(S)
I2 = sp.eye(2); Z2 = sp.zeros(2, 2)
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def sh(x, j, s=1):
    y = list(x); y[j] = (y[j] + s) % L; return tuple(y)
eps = {x: (-1) ** sum(x) for x in S}
c = sp.Integer(2)
def rat(*k):
    return sp.Rational((sum((i + 3) * v for i, v in enumerate(k)) * 7 + 3) % 11 - 5, 4)
# --- sparse block operators
def add(*ops):
    o = {}
    for A in ops:
        for k, v in A.items(): o[k] = o.get(k, Z2) + v
    return {k: v for k, v in o.items() if v != Z2}
def scale(A, a): return {k: a * v for k, v in A.items()}
def mul(A, B):
    rows = {}
    for (p, q), v in B.items(): rows.setdefault(p, []).append((q, v))
    o = {}
    for (x, z), a in A.items():
        for (y, b) in rows.get(z, []): o[(x, y)] = o.get((x, y), Z2) + a * b
    return {k: v for k, v in o.items() if v != Z2}
def adj(A): return {(q, p): v.H for (p, q), v in A.items()}
def diag(f): return {(x, x): f(x) for x in S if f(x) != Z2}
def simp(A): return {k: v.applyfunc(sp.expand) for k, v in A.items() if v.applyfunc(sp.expand) != Z2}
T = [{(x, sh(x, j)): I2 for x in S} for j in range(3)]
Sj = [scale(add(T[j], scale(adj(T[j]), -1)), 1 / (2 * sp.I)) for j in range(3)]
Cj = [scale(add(T[j], adj(T[j])), sp.Rational(1, 2)) for j in range(3)]
Pj = [mul(Sj[j], Cj[j]) for j in range(3)]
def coin(M, A): return {k: M * v for k, v in A.items()}
def Cw(j, v):       # bond-weighted symmetric hop, v(x) on the bond (x, x+e_j)
    o = {}
    for x in S:
        o[(x, sh(x, j))] = o.get((x, sh(x, j)), Z2) + v(x) / 2 * I2
        o[(x, sh(x, j, -1))] = o.get((x, sh(x, j, -1)), Z2) + v(sh(x, j, -1)) / 2 * I2
    return o
def anti(A, B): return add(mul(A, B), mul(B, A))
# --- the couplings (unclocked), generic rational fields
walk = add(*[coin(SIG[j], Sj[j]) for j in range(3)])
ahop = add(*[scale(add(T[j], adj(T[j])), 1) for j in range(3)])
a0 = diag(lambda x: I2)
stag = diag(lambda x: eps[x] * I2)
Ef = lambda j: diag(lambda x: sum(((rat(*x, j, a) + (1 if a == j else 0)) * SIG[a] for a in range(3)), Z2))
frame = scale(add(*[anti(Ef(j), Sj[j]) for j in range(3)]), sp.Rational(1, 2))
th = lambda x, a: rat(*x, a, 5)
twist = scale(add(*[Cw(a, (lambda aa: (lambda x: th(sh(x, aa), aa) - th(x, aa)))(a)) for a in range(3)]), sp.Rational(1, 2))
def cross_frame():
    def f(j):
        def g(x):
            t = [th(x, a) for a in range(3)]; e = [1 if i == j else 0 for i in range(3)]
            cr = [t[1] * e[2] - t[2] * e[1], t[2] * e[0] - t[0] * e[2], t[0] * e[1] - t[1] * e[0]]
            return sum((cr[a] * SIG[a] for a in range(3)), Z2)
        return diag(g)
    return scale(add(*[anti(f(j), Sj[j]) for j in range(3)]), sp.Rational(1, 2))
blind = add(walk, cross_frame(), twist)
Bf = lambda a, j: (lambda x: rat(*x, a, j, 1))
reach2 = add(*[coin(SIG[a], scale(anti(Cw(a, Bf(a, j)), Sj[j]), sp.Rational(1, 2))) for a in range(3) for j in range(3)])
reach3 = add(*[coin(SIG[a], scale(anti(Cw(a, Bf(a, j)), Pj[j]), sp.Rational(1, 2))) for a in range(3) for j in range(3)])
p_alone = add(*[coin(SIG[j], Pj[j]) for j in range(3)])
couplings = [("block 54 walk sum sigma_a S_a", walk), ("block 77 a-hops sum (T_j + T_j^dag)", ahop), ("block 77 on-site a0", a0),
             ("block 77 staggered m eps(x)", stag), ("block 62 frame, varying E", frame), ("block 65 twist hop", twist),
             ("block 65 blind walk (walk + frame rotation + twist hop)", blind),
             ("block 63/64 reach-two strain sum sigma_a (1/2){C_a[B], S_j}", reach2),
             ("block 69 reach-three strain sum sigma_a (1/2){C_a[B], P_j}", reach3),
             ("contrast: the two-step momentum walk sum sigma_j P_j", p_alone)]
phi0 = {x: 1 + sp.Rational((3 * x[0] + 5 * x[1] * x[2] + x[2]) % 7, 5) for x in S}
def clock(O, ph):
    return {(x, y): ph[x] * ph[y] * v for (x, y), v in O.items()}
def ldist(x, y):
    return sum(min((x[i] - y[i]) % L, (y[i] - x[i]) % L) for i in range(3))
phic = {x: phi0[x] * c ** eps[x] for x in S}
res = {}
for name, O in couplings:
    O = simp(O)
    dO = simp(add(clock(O, phic), scale(clock(O, phi0), -1)))
    par = sorted(set(ldist(x, y) % 2 for (x, y) in O))
    reach = max(ldist(x, y) for (x, y) in O)
    res[name] = (len(dO) == 0, par, reach, len(dO))
    out("  %-58s reach %d, displacement parities %s: %s" % (name, reach, par,
        "INVISIBLE (phi c^eps O phi c^eps = phi O phi exactly)" if len(dO) == 0 else "VISIBLE (%d blocks change, by c^(+-2))" % len(dO)))
check("the walk, the a-hops, the frame, the twist hop and the blind walk are invisible (odd displacements only)",
      all(res[k][0] for k in ("block 54 walk sum sigma_a S_a", "block 77 a-hops sum (T_j + T_j^dag)", "block 62 frame, varying E",
                              "block 65 twist hop", "block 65 blind walk (walk + frame rotation + twist hop)")))
check("on-site a0, the staggered mass and the reach-two strain term are visible (even displacements)",
      not any(res[k][0] for k in ("block 77 on-site a0", "block 77 staggered m eps(x)", "block 63/64 reach-two strain sum sigma_a (1/2){C_a[B], S_j}")))
r3 = res["block 69 reach-three strain sum sigma_a (1/2){C_a[B], P_j}"]
check("the reach-three strain term has only ODD displacements (+-e_a +-2 e_j) and is therefore INVISIBLE", r3[0] and r3[1] == [1])
check("contrast: the two-step momentum alone (displacement 2) is visible", not res["contrast: the two-step momentum walk sum sigma_j P_j"][0])

# --- energies
gam = sp.Rational(3, 2)
bonds = [(x, sh(x, j)) for x in S for j in range(3)]
F56 = lambda ph: 2 / gam * sum((ph[x] - ph[y]) ** 2 for x, y in bonds)
one = {x: sp.Integer(1) for x in S}
chk = {x: c ** eps[x] for x in S}
check("block 56's simplest member: a chessboard on uniform rates costs (2/gamma) * 3N * (c - 1/c)^2 exactly (> 0)",
      sp.simplify(F56(chk) - F56(one) - 2 / gam * 3 * N * (c - 1 / c) ** 2) == 0 and F56(chk) > 0)
check("block 56's simplest member with a generic base phi also changes", sp.simplify(F56(phic) - F56(phi0)) != 0)
# block 60 T3 nearest-neighbour member G = K l^p (a Lap lam + b q), q = (1/2) sum_nbrs (lam_y - lam_x)^2; per-tick F = sum w_x G_x
K, p_, a_, b_ = sp.Rational(5, 3), 1, sp.Rational(-2), sp.Rational(-1)
nbrs = lambda x: [sh(x, j, s) for j in range(3) for s in (1, -1)]
def G(lam, x):
    lap = sum(lam[y] - lam[x] for y in nbrs(x)); q = sp.Rational(1, 2) * sum((lam[y] - lam[x]) ** 2 for y in nbrs(x))
    return K * sp.exp(p_ * lam[x]) * (a_ * lap + b_ * q)
Fper = lambda w, lam: sum(w[x] * G(lam, x) for x in S)
w0 = {x: phi0[x] ** 2 for x in S}; wc = {x: phic[x] ** 2 for x in S}
lam_u = {x: sp.Rational(1, 3) for x in S}
check("block 60 curvature-type member at UNIFORM lengths: G_x = 0 at every site, F = 0 for every rate field, so the chessboard changes nothing",
      all(G(lam_u, x) == 0 for x in S) and Fper(wc, lam_u) == 0 and Fper(w0, lam_u) == 0)
lam_v = {x: sp.Rational((x[0] + 2 * x[1] + x[2] * x[0]) % 5, 7) for x in S}
dF = sp.simplify(Fper(wc, lam_v) - Fper(w0, lam_v))
check("contrast: at NON-uniform lengths the per-tick F changes under the chessboard (every clock is a multiplier)", dF != 0)
chi_u = {x: sp.Rational(4, 3) for x in S}
F_T4 = lambda w, chi: 8 * K * sum(w[x] * chi[x] * sum(chi[y] - chi[x] for y in nbrs(x)) for x in S)
check("block 60 T4's exact form 8K sum w chi Lap chi: zero at uniform lengths for every w", F_T4(wc, chi_u) == 0 and F_T4(w0, chi_u) == 0)
c0 = sp.Rational(1, 2)
Fvol = lambda w: c0 * sum(w[x] * sp.Rational(4, 3) ** 3 for x in S)
check("contrast: a member with a volume term c0 det e sees the chessboard at uniform lengths (c0 sum w changes)", sp.simplify(Fvol(wc) - Fvol(w0)) != 0)

# --- the zero mode: curvature member (c0 = 0), uniform static lengths, couplings with odd displacements only
Hgen = add(walk, frame, twist, reach3)
psi = [sp.Rational(((i * 5 + 3) % 9) - 4, 3) + sp.I * sp.Rational(((i * 7 + 1) % 5) - 2, 4) for i in range(2 * N)]
idx = {x: k for k, x in enumerate(S)}
def expval(O, ph):
    tot = 0
    for (x, y), v in clock(O, ph).items():
        px = sp.Matrix(psi[2 * idx[x]:2 * idx[x] + 2]); py = sp.Matrix(psi[2 * idx[y]:2 * idx[y] + 2])
        tot += (px.H * v * py)[0]
    return sp.expand(tot)
E0 = expval(Hgen, phi0) + Fper(w0, lam_u); E1 = expval(Hgen, phic) + Fper(wc, lam_u)
check("zero mode: for walk + varying frame + twist hop + reach-three strain with the curvature member at uniform static lengths, "
      "<H_w> + F is unchanged by the chessboard of clocks, for a generic state (exact)", sp.simplify(E1 - E0) == 0)
Hvis = add(Hgen, reach2)
check("... and it is NOT a zero mode once the reach-two strain term is present", sp.simplify(expval(Hvis, phic) - expval(Hvis, phi0)) != 0)

print()
if FAIL:
    print("SUMMARY: FAIL at " + FAIL[0]); sys.exit(1)
print("SUMMARY: exact on 6^3 with generic rational fields: a chessboard of clocks is invisible to every coupling whose hops are odd "
      "(walk, a-hops, varying frame, twist hop, blind walk, AND the reach-three strain term, displacements +-e_a +-2e_j) and visible to "
      "even ones (on-site a0, staggered mass, reach-two strain); the simplest member pays (2/gamma) 3N (c - 1/c)^2, the curvature member "
      "at uniform lengths pays nothing (G = 0), so there the chessboard is a zero mode of the walk and the ledger together")
print("HIT: the task's premise that the reach-three strain term sees the chessboard (two-step hops) is wrong: C_a[B] P_j moves by "
      "+-e_a +-2 e_j, always an odd number of steps, so phi_x phi_y is unchanged and the term is invisible (exact); the curvature "
      "member's HIT condition is NOT met (it does not change at uniform lengths)")
