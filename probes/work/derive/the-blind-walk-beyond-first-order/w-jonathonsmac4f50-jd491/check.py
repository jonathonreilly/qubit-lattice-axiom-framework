#!/usr/bin/env python3
"""the-blind-walk-beyond-first-order, attempt 1 (worker w-jonathonsmac4f50-jd491, claude-opus-5-5).

Exact claims: sympy (Gaussian rationals, rational unit quaternions, symbols). Step labels refer to ATTEMPT.md.
Part (c)'s classification is carried out in the long-wavelength symbols (leading order in k), stated as such.
"""
import itertools
import random
import sys
import time

import sympy as sp

T0 = time.time()
NP = NF = 0


def ok(label, cond, detail=""):
    global NP, NF
    if cond:
        NP += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        NF += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


I = sp.I
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
ONE = sp.eye(2)


def vs(v):
    return v[0] * SIG[0] + v[1] * SIG[1] + v[2] * SIG[2]


def su2(q):
    return q[0] * ONE - I * vs(q[1:])


def cayley(v):
    n2 = sum(x * x for x in v)
    return [(1 - n2) / (1 + n2)] + [2 * x / (1 + n2) for x in v]


def rot_of(U):
    R = sp.zeros(3, 3)
    for b in range(3):
        M = U * SIG[b] * U.H
        for a in range(3):
            R[a, b] = sp.simplify(sp.expand((M * SIG[a]).trace() / 2))
    assert all(q.is_Rational for q in R)
    return R


def eq0(M):
    return all(sp.simplify(sp.expand(x)) == 0 for x in M)


R_ = random.Random(914)
rq = lambda: sp.Rational(R_.randint(-4, 4), R_.randint(1, 4))
rU = lambda: su2(cayley([rq(), rq(), rq()]))

# ---------------------------------------------------------------- Step 1 (a): the covariant generator
Ux, Uy, V0 = rU(), rU(), rU()
Ex = sp.Matrix([rq(), rq(), rq()])
M0 = vs(Ex)
ok("1.1 bond matrix M_a(x) V_a(x): under M -> U_x M U_x^dag, V -> U_x V U_y^dag it goes to U_x (M V) U_y^dag (exact, rational quaternions)",
   eq0((Ux * M0 * Ux.H) * (Ux * V0 * Uy.H) - Ux * (M0 * V0) * Uy.H))


def build_H(L, Mf, Vf):
    """dense H on a 1-D ring of L sites along axis a (enough for the bond algebra): sum_x (1/2i)[psi_x^dag M V psi_{x+1} - h.c.]"""
    H = sp.zeros(2 * L, 2 * L)
    for x in range(L):
        y = (x + 1) % L
        B = Mf[x] * Vf[x] / (2 * I)
        H[2 * x:2 * x + 2, 2 * y:2 * y + 2] += B
        H[2 * y:2 * y + 2, 2 * x:2 * x + 2] += B.H
    return H


Lr = 3
Us = [rU() for _ in range(Lr)]
Ms = [vs(sp.Matrix([rq(), rq(), rq()])) for _ in range(Lr)]
Vs_ = [rU() for _ in range(Lr)]
Hr = build_H(Lr, Ms, Vs_)
Ubig = sp.diag(*Us)
Hr_t = build_H(Lr, [Us[x] * Ms[x] * Us[x].H for x in range(Lr)], [Us[x] * Vs_[x] * Us[(x + 1) % Lr].H for x in range(Lr)])
ok("1.2 the generator is hermitian and H[U M U^dag, U_x V U_y^dag] = U H[M, V] U^dag exactly (ring of 3, random exact data)",
   eq0(Hr - Hr.H) and eq0(Hr_t - Ubig * Hr * Ubig.H))
ok("1.3 at M_a = sigma_a, V = 1 the bond matrix is sigma_a: block 54's walk", eq0(SIG[0] * ONE - SIG[0]))

# ---------------------------------------------------------------- Step 2 (b): links built from the sites' rotations; block 65 as first order
Ur = [rU() for _ in range(Lr)]
H0 = build_H(Lr, [SIG[0]] * Lr, [ONE] * Lr)
Hsite = build_H(Lr, [Ur[x] * SIG[0] * Ur[x].H for x in range(Lr)], [Ur[x] * Ur[(x + 1) % Lr].H for x in range(Lr)])
ok("2.1 with M_a(x) = U_x s_a U_x^dag and V_a = U_x U_(x+a)^dag the generator is exactly U H U^dag (to all orders)",
   eq0(Hsite - sp.diag(*Ur) * H0 * sp.diag(*Ur).H))
t1 = sp.Matrix(sp.symbols("ta1:4", real=True))
t2 = sp.Matrix(sp.symbols("tb1:4", real=True))
ep = sp.symbols("epsilon", real=True)


def U_series(th, order=3):
    X = -I * ep * vs(th) / 2
    out, term = ONE, ONE
    for n in range(1, order + 1):
        term = term * X / n
        out = out + term
    return out.applyfunc(sp.expand)


U1, U2 = U_series(t1), U_series(t2)
fo_ok, so_terms = True, {}
for j in range(3):
    ej = sp.Matrix([1 if i == j else 0 for i in range(3)])
    Mb = (U1 * SIG[j] * U2.H).applyfunc(sp.expand)
    c1 = Mb.applyfunc(lambda z: z.coeff(ep, 1))
    fo_ok &= eq0(c1 - (vs(((t1 + t2) / 2).cross(ej)) + (I / 2) * (t2[j] - t1[j]) * ONE))
    so_terms[j] = Mb.applyfunc(lambda z: z.coeff(ep, 2))
ok("2.2 first order: U_x s_a U_y^dag = s_a + [((th_x + th_y)/2) x e_a].s + (i/2)(th_y - th_x)_a + O(th^2): block 65's H[vartheta] (its bond-averaged frame rotation and its scalar hop)", fo_ok)
ok("2.3 the scalar hop is the trace part (1/2) tr(s_a V_a): the twist of the link about its own bond, (i/2)(th_y - th_x)_a at first order",
   sp.simplify(sp.expand((SIG[0] * (U1 * U2.H)).trace() / 2).coeff(ep, 1) - (I / 2) * (t2[0] - t1[0])) == 0)
# second order, exact: the blind walk beyond block 65
d = t2 - t1
so_claim0 = (-(t1.dot(t1) + t2.dot(t2)) / 8 * SIG[0] + (vs(t1) * SIG[0] * vs(t2)) / 4)
ok("2.4 second order, exact: the e^2 term of U_x s_a U_y^dag is (1/4)(th_x.s) s_a (th_y.s) - (|th_x|^2 + |th_y|^2)/8 s_a - what block 65's H[vartheta] omits",
   eq0(so_terms[0] - so_claim0.applyfunc(sp.expand)))
# a varying frame: the scalar weight is E^a(x).(th_y - th_x), not the naive d_a(th.E^a)
Ef = [sp.Matrix(sp.symbols(f"E{w}1:4", real=True)) for w in ("x", "y")]
Mb_frame = (U1 * vs(Ef[0]) * U2.H).applyfunc(sp.expand)
scal = sp.simplify(sp.expand(Mb_frame.trace() / 2).coeff(ep, 1))
naive = (I / 2) * (t2.dot(Ef[1]) - t1.dot(Ef[0]))
ok("2.5 frame E at the bond's first end: the scalar hop's weight is (i/2) E(x).(th_y - th_x); the naive (i/2)[th_y.E(y) - th_x.E(x)] differs by (i/2) th_y.(E(y) - E(x)) (block 65 N1.3)",
   sp.simplify(scal - (I / 2) * Ef[0].dot(t2 - t1)) == 0 and sp.simplify(naive - scal - (I / 2) * t2.dot(Ef[1] - Ef[0])) == 0)

# ---------------------------------------------------------------- Step 3 (c): links as functions of the frame
# 3.1 the rotation part is pure gauge: E = R_E S, V = Uhat_x f Uhat_y^dag  =>  bond matrix = Uhat_x (S_x e_a).s f Uhat_y^dag
Uh = [rU() for _ in range(2)]
Rh = [rot_of(u) for u in Uh]
Sx = sp.Matrix(3, 3, lambda i, j: 0)
for i in range(3):
    for j in range(i, 3):
        Sx[i, j] = Sx[j, i] = rq() + (3 if i == j else 0)
f = rU()
Ma = vs(Rh[0] * Sx[:, 0])
ok("3.1 E = R_E S: M_a V_a with V = Uhat_x f Uhat_y^dag equals Uhat_x [(S_x e_a).s f] Uhat_y^dag: the frame's rotation part is a change of coin basis",
   eq0(Ma * (Uh[0] * f * Uh[1].H) - Uh[0] * (vs(Sx[:, 0]) * f) * Uh[1].H))
# 3.2 long-wavelength classification of link rules linear in the stretch s (S = 1 + s)
kv = sp.Matrix(sp.symbols("k1:4", real=True))
xv = sp.Matrix(sp.symbols("x1:4"))
Ssym = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"s{min(i, j)}{max(i, j)}"))
kap = sp.symbols("kap1:5")
E = [sp.Matrix([1 if i == a else 0 for i in range(3)]) for a in range(3)]


def L_bond(a, s):  # every linear map Sym(3) -> R^3 covariant under the proper rotations about e_a (4 parameters)
    ea = E[a]
    se = s * ea
    return kap[0] * ea.cross(se) + kap[1] * se + kap[2] * s.trace() * ea + kap[3] * ea.dot(se) * ea


omega_bond = lambda a, s: I * kv[a] * L_bond(a, s)  # reach: the bond's two ends -> derivative along a only
omega_tf = lambda a, s: -(I * kv).cross(s * E[a])  # the curl of column a of s: block 64's curls
hol = lambda a, b, om: I * kv[a] * om(b) - I * kv[b] * om(a)
gauge = (I / 2) * (kv * xv.T + xv * kv.T)
eqs = []
for a, b in ((0, 1), (0, 2), (1, 2)):
    for comp in hol(a, b, lambda c_: omega_bond(c_, gauge)):
        eqs += sp.Poly(sp.expand(comp), *kv, *xv).coeffs()
sol = sp.solve(eqs, kap, dict=True)
ok("3.2 bond reach (the stretches at the bond's two ends, linear, vanishing on uniform stretch): the plaquette holonomy is blind to every relabelling only for the zero rule",
   sol == [{kap[0]: 0, kap[1]: 0, kap[2]: 0, kap[3]: 0}], f"solutions {sol}")
tf_blind = all(sp.simplify(x) == 0 for a, b in ((0, 1), (0, 2), (1, 2)) for x in hol(a, b, lambda c_: omega_tf(c_, gauge)))
H01 = [sp.expand(x) for x in hol(0, 1, lambda c_: omega_tf(c_, Ssym))]
Riem = sp.expand(kv[0] ** 2 * Ssym[1, 1] - 2 * kv[0] * kv[1] * Ssym[0, 1] + kv[1] ** 2 * Ssym[0, 0])
ok("3.3 plaquette reach: omega_a = -curl(s e_a) = block 64's curls F^a of the stretch; its holonomy is blind to relabellings and not zero: in plane (0,1) the normal component is the linearized curvature R_0101 of g = 1 + 2s",
   tf_blind and sp.simplify(H01[2] - Riem) == 0 and any(x != 0 for x in H01), f"hol_01 = {H01}")
# 3.4 block 64's curl: F_bd^a = d_b s_da - d_d s_ba ; -curl(s e_a)_c = -(1/2) eps_cbd F_bd^a
F = lambda a, b_, d_: I * kv[b_] * Ssym[d_, a] - I * kv[d_] * Ssym[b_, a]
ok("3.4 omega_a^c = -(1/2) eps_cbd F_bd^a with F_bd^a = d_b s_da - d_d s_ba (block 64's curls of the strain placed as the stretch)",
   all(sp.simplify(omega_tf(a, Ssym)[c_] + sum(sp.LeviCivita(c_, b_, d_) * F(a, b_, d_) for b_ in range(3) for d_ in range(3)) / 2) == 0
       for a in range(3) for c_ in range(3)))

print(f"total {time.time() - T0:.1f} s; PASS={NP} FAIL={NF}")
if NF:
    print(f"SUMMARY: ROUTE FAILS AT the first FAIL line above ({NF} failures)")
    sys.exit(1)
print("SUMMARY: PARTIAL (a) the bond form M_a(x) V_a(x) with SU(2) links is exactly covariant and hermitian; (b) with links from the sites' "
      "rotations it is exactly U H U^dag, block 65's H[vartheta] is its first order, the scalar hop is the link's twist about its own bond "
      "(i/2)(th_y - th_x)_a, and the second-order term is (1/4)(th_x.s)s_a(th_y.s) - (|th_x|^2+|th_y|^2)/8 s_a; for a varying frame the weight "
      "is E(x).(th_y - th_x), not the naive difference of th.E; (c) as functions of the frame, links are Uhat_x f Uhat_y^dag (the rotation part "
      "is a change of coin basis); at bond reach the only link linear in the stretch with relabelling-blind holonomy is the flat one; reading "
      "block 64's curls on the adjoining plaquettes gives omega_a = -curl(s e_a), blind, with the linearized curvature of g = 1 + 2s as holonomy "
      "(long-wavelength symbols). No new field is needed at first order in the stretch, at plaquette reach; beyond first order not constructed.")
print("HIT: exact covariant blind walk beyond first order (links U_x U_y^dag; second-order term (1/4)(th_x.s)s_a(th_y.s) - (|th_x|^2+|th_y|^2)/8 s_a; "
      "varying-frame weight E(x).(th_y - th_x)); links fixed by the frame alone carry curvature only at plaquette reach: at bond reach the only "
      "relabelling-blind linear rule is flat, and omega_a = -curl(s e_a) (block 64's curls) is blind with the linearized curvature as holonomy")
