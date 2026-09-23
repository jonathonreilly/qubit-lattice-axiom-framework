#!/usr/bin/env python3
"""a-law-for-the-rotation-of-the-coin-axes, attempt 2 (worker w-jonathonsmac4f50-j330f, claude-opus-5-5).

All claims are checked in exact arithmetic (sympy: Gaussian rationals, rational unit quaternions).
Step labels refer to ATTEMPT.md.
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
ZERO2 = sp.zeros(2, 2)


def vs(v):
    """v . sigma"""
    return v[0] * SIG[0] + v[1] * SIG[1] + v[2] * SIG[2]


def su2(q):
    """unit quaternion (q0, q1, q2, q3) -> q0 - i q.sigma"""
    return q[0] * ONE - I * vs(q[1:])


def cayley(v):
    """rational unit quaternion from a rational 3-vector"""
    n2 = sum(x * x for x in v)
    return [(1 - n2) / (1 + n2)] + [2 * x / (1 + n2) for x in v]


def rot_of(U):
    """R with U (v.sigma) U^dagger = (R v).sigma"""
    R = sp.zeros(3, 3)
    for b in range(3):
        M = U * SIG[b] * U.H
        for a in range(3):
            R[a, b] = sp.simplify(sp.expand((M * SIG[a]).trace() / 2))
    assert all(q.is_Rational for q in R), "rotation entries must be exact rationals"
    return R


def dag(M):
    return M.H


def X(e):
    return sp.expand(e)


def eq0(M):
    return all(sp.simplify(sp.expand(x)) == 0 for x in M)


# ---------------------------------------------------------------- Step 1 (a): a varying rotation is not a conjugation of the frame
R_ = random.Random(20260923)
rq = lambda: sp.Rational(R_.randint(-4, 4), R_.randint(1, 4))
Ux, Uy = su2(cayley([rq(), rq(), rq()])), su2(cayley([rq(), rq(), rq()]))
ok("1.0 the Cayley quaternions give exact SU(2) matrices", eq0(Ux * Ux.H - ONE) and eq0(Uy * Uy.H - ONE) and sp.simplify(Ux.det()) == 1)
Rx, Ry = rot_of(Ux), rot_of(Uy)
Ex, Ey = sp.Matrix([rq(), rq(), rq()]), sp.Matrix([rq(), rq(), rq()])
Ebar = (Ex + Ey) / 2
M_conj = Ux * vs(Ebar) * Uy.H  # bond matrix of U H[E] U^dagger
M_frame = vs((Rx * Ex + Ry * Ey) / 2)  # bond matrix of H[R E]
extra = (Ux * vs(Ex) * (Uy.H - Ux.H) + (Ux - Uy) * vs(Ey) * Uy.H) / 2
ok("1.1 U_x (Ebar.s) U_y^dag - ((R_x E_x + R_y E_y)/2).s = (1/2)[U_x (E_x.s)(U_y^dag - U_x^dag) + (U_x - U_y)(E_y.s) U_y^dag] exactly",
   eq0(M_conj - M_frame - extra))
ok("1.2 the transformed bond matrix has a coin-scalar part (tr != 0), which no frame generator has: U H[E] U^dag is not H[E'] for any E'",
   sp.simplify(M_conj.trace()) != 0 and all(sp.simplify(vs(v).trace()) == 0 for v in (Ex, Ey)),
   f"tr = {sp.simplify(M_conj.trace())}")
# first order: U = exp(-i th.s/2), bond (x, x + e_j), identity frame -> frame rotation averaged on the bond + twist hop
t1 = sp.Matrix(sp.symbols("ta1:4", real=True))
t2 = sp.Matrix(sp.symbols("tb1:4", real=True))
eps = sp.symbols("epsilon", real=True)
U1 = ONE - I * eps * vs(t1) / 2 - eps ** 2 * (t1.dot(t1)) * ONE / 8
U2 = ONE - I * eps * vs(t2) / 2 - eps ** 2 * (t2.dot(t2)) * ONE / 8
fo_ok = True
for j in range(3):
    ej = sp.Matrix([1 if i == j else 0 for i in range(3)])
    Mb = (U1 * SIG[j] * U2.H).applyfunc(lambda z: sp.expand(z).coeff(eps, 1))
    target = vs(((t1 + t2) / 2).cross(ej)) + (I / 2) * (t2[j] - t1[j]) * ONE
    fo_ok &= eq0(Mb - target)
ok("1.3 first order (identity frame): U_x s_j U_y^dag = s_j + [((th_x+th_y)/2) x e_j].s + (i/2)(th_y - th_x)_j + O(th^2): block 65 T1's frame rotation and twist hop", fo_ok)

# ---------------------------------------------------------------- Step 2 (b): links that make local coin rotations a symmetry
qW = cayley([rq(), rq(), rq()])
W = su2(qW)
B = lambda Ea, Eb, Wb: (vs(Ea) * Wb + Wb * vs(Eb)) / 2
Bp = B(Rx * Ex, Ry * Ey, Ux * W * Uy.H)
ok("2.1 B = (1/2)(E_x.s W + W E_y.s) is covariant: B[R_x E_x, R_y E_y, U_x W U_y^dag] = U_x B[E_x, E_y, W] U_y^dag", eq0(Bp - Ux * B(Ex, Ey, W) * Uy.H))
ok("2.2 at W = 1 it is block 62's bond matrix ((E_x + E_y)/2).s", eq0(B(Ex, Ey, ONE) - vs((Ex + Ey) / 2)))
# flat links determined by the frame's rotation part: E = R_E S  ->  W = Uhat_x Uhat_y^dag gives B = Uhat_x B[S_x, S_y, 1] Uhat_y^dag
Sx = sp.Matrix(3, 3, lambda i, j: 0)
Sy = sp.Matrix(3, 3, lambda i, j: 0)
for i in range(3):
    for j in range(i, 3):
        Sx[i, j] = Sx[j, i] = rq() + (3 if i == j else 0)
        Sy[i, j] = Sy[j, i] = rq() + (3 if i == j else 0)
Uhx, Uhy = su2(cayley([rq(), rq(), rq()])), su2(cayley([rq(), rq(), rq()]))
Rhx, Rhy = rot_of(Uhx), rot_of(Uhy)
flat_ok = True
for j in range(3):
    Exj, Eyj = (Rhx * Sx)[:, j], (Rhy * Sy)[:, j]
    flat_ok &= eq0(B(Exj, Eyj, Uhx * Uhy.H) - Uhx * B(Sx[:, j], Sy[:, j], ONE) * Uhy.H)
ok("2.3 flat links W_b = Uhat_x Uhat_y^dag from E = R_E S: every bond matrix equals Uhat_x B[S_x, S_y, 1] Uhat_y^dag (the walker sees only S = sqrt(g))", flat_ok)
ok("2.4 the lift sign: U -> -U leaves R(U) and E unchanged but flips W = U_x ... ; so a link fixed by E alone is covariant only up to a site sign (a unitary, psi_x -> -psi_x)",
   eq0(rot_of(-Ux) - Rx) and eq0(B(Ex, Ey, (-Ux) * W) + B(Ex, Ey, Ux * W) - 2 * B(Ex, Ey, ZERO2)))

# ---------------------------------------------------------------- Step 3 (c): the exact Noether identity on a torus


def build(L, E, Wl, psi):
    sites = list(itertools.product(range(L), repeat=3))
    sh = lambda x, j, s=1: tuple((x[i] + (s if i == j else 0)) % L for i in range(3))
    Bb = {(x, j): B(E[x][:, j], E[sh(x, j)][:, j], Wl[(x, j)]) for x in sites for j in range(3)}
    Hpsi = {}
    for x in sites:
        v = sp.zeros(2, 1)
        for j in range(3):
            v += Bb[(x, j)] * psi[sh(x, j)] / (2 * I)
            xm = sh(x, j, -1)
            v += (Bb[(xm, j)] / (2 * I)).H * psi[xm]
        Hpsi[x] = v.applyfunc(sp.expand)
    return sites, sh, Bb, Hpsi


def re(z):
    return sp.re(sp.expand(z))


def noether(L, E, Wl, psi):
    sites, sh, Bb, Hpsi = build(L, E, Wl, psi)
    out = {}
    for x in sites:
        for c in range(3):
            # frame part: sum_j (E^j x Theta^j)_c, Theta_a^j(x) = d<H>/dE_a^j(x)
            ec = sp.Matrix([1 if i == c else 0 for i in range(3)])
            frame = 0
            for j in range(3):
                y, xm = sh(x, j), sh(x, j, -1)
                dE = ec.cross(E[x][:, j])  # rotation of E^j(x) about e_c
                d1 = (vs(dE) * Wl[(x, j)]) / 2  # x is the left end of bond (x, j)
                d2 = (Wl[(xm, j)] * vs(dE)) / 2  # x is the right end of bond (xm, j)
                frame += 2 * re((psi[x].H * d1 * psi[y])[0] / (2 * I)) + 2 * re((psi[xm].H * d2 * psi[x])[0] / (2 * I))
            link = 0
            for j in range(3):
                y, xm = sh(x, j), sh(x, j, -1)
                dW1 = -I * SIG[c] * Wl[(x, j)] / 2  # W -> U W at the left end
                dW2 = I * Wl[(xm, j)] * SIG[c] / 2  # W -> W U^dag at the right end
                link += 2 * re((psi[x].H * B(E[x][:, j], E[y][:, j], dW1) * psi[y])[0] / (2 * I))
                link += 2 * re((psi[xm].H * B(E[xm][:, j], E[x][:, j], dW2) * psi[x])[0] / (2 * I))
            dG = -sp.im(sp.expand((Hpsi[x].H * SIG[c] * psi[x])[0]))  # d<sigma_c/2>/dt = i<[H, sigma_c/2]>
            out[(x, c)] = (sp.simplify(sp.expand(frame)), sp.simplify(sp.expand(link)), sp.simplify(sp.expand(dG)))
    return out


L = 3
sites3 = list(itertools.product(range(L), repeat=3))
E3 = {x: sp.Matrix(3, 3, lambda i, j: rq() + (2 if i == j else 0)) for x in sites3}
W3 = {(x, j): su2(cayley([rq(), rq(), rq()])) for x in sites3 for j in range(3)}
P3 = {x: sp.Matrix([rq() + I * rq(), rq() + I * rq()]) for x in sites3}
t_ = time.time()
res = noether(L, E3, W3, P3)
ident = all(sp.simplify(f + l - g) == 0 for f, l, g in res.values())
nontriv = sum(1 for f, l, g in res.values() if f != 0 and l != 0 and g != 0)
ok("3.1 for EVERY state, frame and link field (3^3 torus, random exact data): frame torque + link part = (1/2) d<psi^dag s_c psi>(x)/dt at every site and axis",
   ident and nontriv > 60, f"{len(res)} identities, {nontriv} with all three terms non-zero, {time.time() - t_:.1f} s")

# the exactly stationary state of the 4^3 torus (identity frame, W = 1): plane waves at pi/2 along each axis, energy +1
L4 = 4
sites4 = list(itertools.product(range(L4), repeat=3))
coins = [sp.Matrix([1, 1]), sp.Matrix([1, I]), sp.Matrix([1, 0])]
P4 = {x: sum((I ** x[j] * coins[j] for j in range(3)), sp.zeros(2, 1)) for x in sites4}
Eid = {x: sp.eye(3) for x in sites4}
W1 = {(x, j): ONE for x in sites4 for j in range(3)}
_, _, _, Hp4 = build(L4, Eid, W1, P4)
ok("3.2 the 4^3 state sum_j i^{x_j} c_j (c = (1,1), (1,i), (1,0)) is an eigenstate of block 54's walk with energy +1",
   all(eq0(Hp4[x] - P4[x]) for x in sites4))
t_ = time.time()
res4 = noether(L4, Eid, W1, P4)
f_nz = sum(1 for f, l, g in res4.values() if f != 0)
ok("3.3 on it, with no links (W = 1): the antisymmetric frame response is non-zero and equals minus the link part (the twist-hop bond term); d<s_c>/dt = 0",
   all(g == 0 and sp.simplify(f + l) == 0 for f, l, g in res4.values()) and f_nz > 0,
   f"frame torque non-zero at {f_nz} of {len(res4)} (site, axis) pairs; {time.time() - t_:.1f} s")

# flat links fixed by the frame: E = R_E(x) (rotations), W = Uhat_x Uhat_y^dag, state Uhat psi0 -> the total torque vanishes
Uh = {x: su2(cayley([rq(), rq(), rq()])) for x in sites4}
Er = {x: rot_of(Uh[x]) for x in sites4}
sh4 = lambda x, j: tuple((x[i] + (1 if i == j else 0)) % L4 for i in range(3))
Wf = {(x, j): Uh[x] * Uh[sh4(x, j)].H for x in sites4 for j in range(3)}
Pr = {x: (Uh[x] * P4[x]).applyfunc(sp.expand) for x in sites4}
_, _, _, Hpr = build(L4, Er, Wf, Pr)
ok("3.4 with flat links fixed by a rotated frame, Uhat psi0 is again an eigenstate (energy +1): H[R_E, W(R_E)] = Uhat H Uhat^dag",
   all(eq0(Hpr[x] - Pr[x]) for x in sites4))
t_ = time.time()
resr = noether(L4, Er, Wf, Pr)
tot0 = all(sp.simplify(f + l) == 0 and g == 0 for f, l, g in resr.values())
fz = sum(1 for f, l, g in resr.values() if f != 0)
ok("3.5 there, rotating E at a site moves W(E) by exactly the link transformation, so the TOTAL torque (frame + induced links) is zero on the stationary state",
   tot0, f"frame part alone non-zero at {fz} of {len(resr)}; {time.time() - t_:.1f} s")

# a link field with its own energy: a plaquette energy is invariant under every local rotation of the links alone
Lp = 3
sh3 = lambda x, j: tuple((x[i] + (1 if i == j else 0)) % Lp for i in range(3))


def plaq(Wl):
    tot = 0
    for x in sites3:
        for i, j in ((0, 1), (0, 2), (1, 2)):
            Wp = Wl[(x, i)] * Wl[(sh3(x, i), j)] * Wl[(sh3(x, j), i)].H * Wl[(x, j)].H
            tot += sp.re(sp.expand(Wp.trace()))
    return sp.simplify(sp.expand(tot))


Ug = {x: su2(cayley([rq(), rq(), rq()])) for x in sites3}
Wg = {(x, j): Ug[x] * W3[(x, j)] * Ug[sh3(x, j)].H for x in sites3 for j in range(3)}
p0, p1 = plaq(W3), plaq(Wg)
ok("3.6 a plaquette energy sum Re tr(W W W^dag W^dag) is unchanged by an exact finite local rotation of the links: its own link part vanishes identically",
   sp.simplify(p0 - p1) == 0 and p0 != 12 * len(sites3) * 0, f"plaquette sum = {p0}")

print(f"total {time.time() - T0:.1f} s; PASS={NP} FAIL={NF}")
if NF:
    print(f"SUMMARY: ROUTE FAILS AT the first FAIL line above ({NF} failures)")
    sys.exit(1)
print("SUMMARY: PARTIAL exact to all orders: (a) a varying coin rotation turns block 62's bond matrix into U_x (Ebar.s) U_y^dag, "
      "which differs from the rotated frame's by (1/2)[U_x(E_x.s)(U_y^dag - U_x^dag) + (U_x - U_y)(E_y.s)U_y^dag] and has a "
      "coin-scalar part no frame has (first order: block 65's twist hop); (b) an SU(2) link on each bond in the covariant form "
      "(1/2)(E_x.s W + W E_y.s) makes local coin rotations an exact symmetry; the frame fixes such a link only up to a site sign "
      "and a rotation-invariant rule f(S_x, S_y) of the stretches; with f = 1 (flat) the walker sees only sqrt(g); (c) for every "
      "state, frame and link field, frame torque + link part = (1/2) d<psi^dag s_c psi>/dt, so on stationary states the "
      "antisymmetric frame response vanishes iff the link part does: with W = 1 it does not (block 62 N1.2); with flat links "
      "fixed by the frame the total torque vanishes; with links as a field in equilibrium under their own gauge-invariant energy "
      "the frame torque vanishes")
print("HIT: exact all-orders construction closing block 65's first-order limit: covariant SU(2) bond links B = (1/2)(E_x.s W + W E_y.s); "
      "the Noether identity frame torque + link part = (1/2) d<s_c>/dt for every state, frame and link; links fixed by the frame are "
      "Uhat_x f(S_x, S_y) Uhat_y^dag up to a site sign, and the flat choice makes the walk unitarily H[sqrt g, 1]; the antisymmetric frame "
      "response vanishes on stationary states exactly when the link part does")
