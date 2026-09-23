#!/usr/bin/env python3
"""J:derive:su2-bond-links-exact-blindness-and-the-species:a3

Link-dressed frame walk on the qubit coin (blocks 54, 62, 65, 70, 74; PRs #8570 #8592 #8596 #8602 #8607;
supplied clauses, nothing adopted):
  H[E, U] = (1/2) sum_j { A_j , S_j^U },  A_j(x) = sum_a E_a^j(x) sigma_a,
  (S_j^U psi)(x) = (1/(2i)) [ U_{x,x+e_j} psi(x+e_j) - U_{x,x-e_j} psi(x-e_j) ],  U_{y,x} = U_{x,y}^dagger in SU(2).
  E = identity, U = 1 is block 54's walk H = sum_j sigma_j S_j (symbol sin k_j).
Families: A covariance and hermiticity (exact, 4^3 torus, Gaussian-rational SU(2) elements); B the
first-order pure-gauge link is block 65's twist hop; C the species maps are a flat Z2 connection; D the
frame's response is gauge covariant (so block 74's count is gauge invariant) and a flat background.
"""
import itertools
import random
import sys
import time
from fractions import Fraction as F

T0 = time.time()
FAILS = []


def ok(tag, cond, msg=""):
    print(("ok " if cond else "FAIL ") + tag + (" " + msg if msg else ""))
    if not cond:
        FAILS.append(tag)


class G:
    __slots__ = ("r", "i")

    def __init__(s, r=0, i=0):
        s.r, s.i = F(r), F(i)

    def __add__(s, o):
        return G(s.r + o.r, s.i + o.i)

    def __sub__(s, o):
        return G(s.r - o.r, s.i - o.i)

    def __mul__(s, o):
        if isinstance(o, G):
            return G(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
        return G(s.r * o, s.i * o)

    __rmul__ = __mul__

    def conj(s):
        return G(s.r, -s.i)

    def __eq__(s, o):
        return s.r == o.r and s.i == o.i


Z, O, I = G(0), G(1), G(0, 1)


# 2x2 matrices as tuples of four G (row-major)
def mm(a, b):
    return (a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3], a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3])


def madd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def msc(a, c):
    return tuple(x * c for x in a)


def dag(a):
    return (a[0].conj(), a[2].conj(), a[1].conj(), a[3].conj())


def mv(a, v):
    return (a[0] * v[0] + a[1] * v[1], a[2] * v[0] + a[3] * v[1])


ID = (O, Z, Z, O)
SIG = [(Z, O, O, Z), (Z, G(0, -1), I, Z), (O, Z, Z, G(-1))]
ZM = (Z, Z, Z, Z)


def su2_from_quat(a, b, c, d):      # a + b i sigma... : g = a*1 + i(b s1 + c s2 + d s3), a^2+b^2+c^2+d^2 = 1
    g = msc(ID, G(a))
    for coef, s in zip((b, c, d), SIG):
        g = madd(g, msc(s, G(0, coef)))
    return g


def rand_su2(rng):                  # rational point on S^3 by inverse stereographic projection
    x, y, z = (F(rng.randint(-7, 7), rng.randint(1, 5)) for _ in range(3))
    n = x * x + y * y + z * z + 1
    return su2_from_quat((n - 2) / n, 2 * x / n, 2 * y / n, 2 * z / n)


def is_su2(g):
    p = mm(g, dag(g))
    det = g[0] * g[3] - g[1] * g[2]
    return p == ID and det == O


L = 4
SITES = list(itertools.product(range(L), repeat=3))
IDX = {x: n for n, x in enumerate(SITES)}
V = len(SITES)


def nb(x, j, s):
    y = list(x)
    y[j] = (y[j] + s) % L
    return tuple(y)


def link(U, x, j, s):               # U_{x, x + s e_j}
    if s == 1:
        return U[(x, j)]
    return dag(U[(nb(x, j, -1), j)])


def S_U(U, psi, j):
    out = {}
    for x in SITES:
        fwd = mv(link(U, x, j, 1), psi[nb(x, j, 1)])
        bwd = mv(link(U, x, j, -1), psi[nb(x, j, -1)])
        out[x] = tuple((f - b) * G(0, F(-1, 2)) for f, b in zip(fwd, bwd))      # 1/(2i) = -i/2
    return out


def Hop(A, U, psi):                 # (1/2) sum_j { A_j, S_j^U }
    out = {x: (Z, Z) for x in SITES}
    for j in range(3):
        s1 = S_U(U, psi, j)
        Apsi = {x: mv(A[(x, j)], psi[x]) for x in SITES}
        s2 = S_U(U, Apsi, j)
        for x in SITES:
            a = mv(A[(x, j)], s1[x])
            out[x] = tuple(o + (p + q) * F(1, 2) for o, p, q in zip(out[x], a, s2[x]))
    return out


def inner(a, b):
    acc = Z
    for x in SITES:
        acc = acc + a[x][0].conj() * b[x][0] + a[x][1].conj() * b[x][1]
    return acc


rng = random.Random(7)


def rand_state():
    return {x: (G(rng.randint(-3, 3), rng.randint(-3, 3)), G(rng.randint(-3, 3), rng.randint(-3, 3))) for x in SITES}


def rand_frame():
    A = {}
    for x in SITES:
        for j in range(3):
            m = ZM
            for a in range(3):
                m = madd(m, msc(SIG[a], G(F(rng.randint(-4, 4), rng.randint(1, 3)))))
            A[(x, j)] = m
    return A


# ---------------------------------------------------------------- A covariance and hermiticity
ok("A.su2", all(is_su2(rand_su2(rng)) for _ in range(20)), "rational points of S^3 give exact SU(2) matrices (g g^dag = 1, det 1)")
A0 = rand_frame()
U0 = {(x, j): rand_su2(rng) for x in SITES for j in range(3)}
psi = rand_state()
phi = rand_state()
Hpsi = Hop(A0, U0, psi)
Hphi = Hop(A0, U0, phi)
ok("A.hermitian", inner(phi, Hpsi) == inner(Hphi, psi), "<phi, H[E,U] psi> = <H[E,U] phi, psi> for random frame, links, states")
gx = {x: rand_su2(rng) for x in SITES}
A1 = {(x, j): mm(mm(gx[x], A0[(x, j)]), dag(gx[x])) for x in SITES for j in range(3)}
U1 = {(x, j): mm(mm(gx[x], U0[(x, j)]), dag(gx[nb(x, j, 1)])) for x in SITES for j in range(3)}
gpsi = {x: mv(gx[x], psi[x]) for x in SITES}
lhs = Hop(A1, U1, gpsi)
rhs = {x: mv(gx[x], Hpsi[x]) for x in SITES}
ok("A.covariant", all(lhs[x] == rhs[x] for x in SITES),
   "H[g E g^dag, g_x U g_y^dag] (g psi) = g H[E, U] psi exactly for a random site-dependent g in SU(2)")
# ---------------------------------------------------------------- B first order of the pure-gauge link = block 65's twist hop
theta = {x: [F(rng.randint(-5, 5), rng.randint(1, 4)) for _ in range(3)] for x in SITES}


def tsig(v):
    m = ZM
    for a in range(3):
        m = madd(m, msc(SIG[a], G(v[a])))
    return m


Aid = {(x, j): SIG[j] for x in SITES for j in range(3)}
Uid = {(x, j): ID for x in SITES for j in range(3)}
# g = exp(-i theta.sigma/2) (block 65's convention): U_{x,y} = g_x g_y^dag = 1 + (i/2)(theta_y - theta_x).sigma + O(2)
dU = {(x, j): msc(tsig([a - b for a, b in zip(theta[nb(x, j, 1)], theta[x])]), G(0, F(1, 2))) for x in SITES for j in range(3)}


def cross(t, j):                    # theta x e_j
    e = [0, 0, 0]
    e[j] = 1
    return [t[1] * e[2] - t[2] * e[1], t[2] * e[0] - t[0] * e[2], t[0] * e[1] - t[1] * e[0]]


dA = {(x, j): tsig(cross(theta[x], j)) for x in SITES for j in range(3)}


def dS(psi_, j):                     # first-order change of S_j^U
    out = {}
    for x in SITES:
        fwd = mv(dU[(x, j)], psi_[nb(x, j, 1)])
        bwd = mv(dag(dU[(nb(x, j, -1), j)]), psi_[nb(x, j, -1)])
        out[x] = tuple((f - b) * G(0, F(-1, 2)) for f, b in zip(fwd, bwd))
    return out


def dH_link(psi_):
    out = {x: (Z, Z) for x in SITES}
    for j in range(3):
        a1 = dS(psi_, j)
        s2 = dS({x: mv(SIG[j], psi_[x]) for x in SITES}, j)
        for x in SITES:
            a = mv(SIG[j], a1[x])
            out[x] = tuple(o + (p + q) * F(1, 2) for o, p, q in zip(out[x], a, s2[x]))
    return out


def twist_hop(psi_):                 # (1/2) sum_a C_a[d_a theta_a], C_a[v] psi(x) = (1/2)[v(x) psi(x+e_a) + v(x-e_a) psi(x-e_a)]
    out = {x: (Z, Z) for x in SITES}
    for a in range(3):
        for x in SITES:
            v1 = theta[nb(x, a, 1)][a] - theta[x][a]
            xm = nb(x, a, -1)
            v0 = theta[x][a] - theta[xm][a]
            out[x] = tuple(o + (p * v1 + q * v0) * F(1, 4) for o, p, q in zip(out[x], psi_[nb(x, a, 1)], psi_[xm]))
    return out


def comm_block65(psi_):              # -(i/2)[theta.sigma, H] psi
    Hp = Hop(Aid, Uid, psi_)
    tp = {x: mv(tsig(theta[x]), psi_[x]) for x in SITES}
    Htp = Hop(Aid, Uid, tp)
    return {x: tuple((a - b) * G(0, F(-1, 2)) for a, b in zip(mv(tsig(theta[x]), Hp[x]), Htp[x])) for x in SITES}


ps = rand_state()
link_part = dH_link(ps)
hop = twist_hop(ps)
ok("B.link", all(link_part[x] == hop[x] for x in SITES),
   "first-order term of the pure-gauge links g_x g_y^dag (g = exp(-i theta.sigma/2)) = (1/2) sum_a C_a[d_a theta_a], block 65's twist hop")
frame_part = Hop(dA, Uid, ps)
total = {x: tuple(a + b for a, b in zip(frame_part[x], link_part[x])) for x in SITES}
c65 = comm_block65(ps)
ok("B.total", all(total[x] == c65[x] for x in SITES),
   "frame rotation (1/2) sum {(theta x e_j).sigma, S_j} + link term = -(i/2)[theta.sigma, H] exactly (block 65 T1)")

# ---------------------------------------------------------------- C species maps as a flat Z2 connection
good = True
flat = True
spec = True
for n in itertools.product((0, 1), repeat=3):
    for c in range(3):
        gsp = {x: msc(msc(SIG[c], I), (-1) ** sum(a * b for a, b in zip(n, x))) for x in SITES}
        good &= all(is_su2(gsp[x]) for x in SITES[:2])
        A2 = {(x, j): mm(mm(gsp[x], SIG[j]), dag(gsp[x])) for x in SITES for j in range(3)}
        U2 = {(x, j): mm(gsp[x], dag(gsp[nb(x, j, 1)])) for x in SITES for j in range(3)}
        good &= all(U2[(x, j)] == msc(ID, G((-1) ** n[j])) for x in SITES for j in range(3))
        good &= all(A2[(x, j)] == msc(SIG[j], G(1 if j == c else -1)) for x in SITES for j in range(3))
        for x in SITES[:8]:
            for (i1, j1) in ((0, 1), (0, 2), (1, 2)):
                h = mm(mm(U2[(x, i1)], U2[(nb(x, i1, 1), j1)]), mm(dag(U2[(nb(x, j1, 1), i1)]), dag(U2[(x, j1)])))
                flat &= h == ID
        # species n zero mode (-1)^{n.x} u of H maps to a constant (species 000) zero mode of H[rho_c E, D]
        u = (G(1), G(2, -1))
        chi = {x: tuple(t * ((-1) ** sum(a * b for a, b in zip(n, x))) for t in u) for x in SITES}
        spec &= all(v == (Z, Z) for v in Hop(Aid, Uid, chi).values())
        img = {x: mv(gsp[x], chi[x]) for x in SITES}
        spec &= all(img[x] == img[SITES[0]] for x in SITES)
        spec &= all(v == (Z, Z) for v in Hop(A2, U2, img).values())
ok("C.gauge", good, "g_x = (-1)^{n.x} i sigma_c is in SU(2) (centre times a half turn); it sends (E = 1, U = 1) to "
   "(rho_c E, U' = (-1)^{n_j} on bonds along j) for every n and c")
ok("C.flat", flat, "every plaquette holonomy of U' = (-1)^{n_j} is the identity: a flat Z2 connection")
ok("C.species", spec, "species n's zero modes (-1)^{n.x} u map to constant (species 000) zero modes of H[rho_c E, D]")

# ---------------------------------------------------------------- D the frame's response is gauge covariant
def theta_resp(A, U, psi_):          # Theta_a^j(x) = Re psi^dag sigma_a (S_j^U psi) (block 62's site stress at the identity frame)
    out = {}
    for j in range(3):
        s1 = S_U(U, psi_, j)
        for x in SITES:
            for a in range(3):
                v = mv(SIG[a], s1[x])
                out[(x, a, j)] = (psi_[x][0].conj() * v[0] + psi_[x][1].conj() * v[1]).r
    return out


def rot_image(g):                    # R_ab with g sigma_b g^dag = sum_a R_ab sigma_a
    R = [[F(0)] * 3 for _ in range(3)]
    for b in range(3):
        m = mm(mm(g, SIG[b]), dag(g))
        for a in range(3):
            tr = mm(SIG[a], m)
            R[a][b] = (tr[0] + tr[3]).r / 2
    return R


so3 = True
for x in SITES[:16]:
    R = rot_image(gx[x])
    so3 &= all(sum(R[a][c] * R[b][c] for c in range(3)) == (1 if a == b else 0) for a in range(3) for b in range(3))
    so3 &= (R[0][0] * (R[1][1] * R[2][2] - R[1][2] * R[2][1]) - R[0][1] * (R[1][0] * R[2][2] - R[1][2] * R[2][0])
            + R[0][2] * (R[1][0] * R[2][1] - R[1][1] * R[2][0])) == 1
ok("D.so3", so3, "g sigma_b g^dag = sum_a R_ab sigma_a with R rational, orthogonal, det 1: the frame's coin index turns in SO(3)")
th0 = theta_resp(Aid, U0, psi)
th1 = theta_resp(Aid, U1, gpsi)
good = True
for x in SITES[:16]:
    R = rot_image(gx[x])
    for j in range(3):
        for a in range(3):
            good &= th1[(x, a, j)] == sum(R[a][b] * th0[(x, b, j)] for b in range(3))
ok("D.covariant", good, "Theta_a^j[g psi; g U g^dag] = R(g_x)_ab Theta_b^j[psi; U]: the frame's response turns with the coin, "
   "so which species a gauge-invariant coin-blind field energy serves is gauge invariant (block 74's 2 of 8 at fixed links)")

print("runtime %.1f s" % (time.time() - T0))
if FAILS:
    print("CHECK FAIL: " + ", ".join(FAILS))
    print("SUMMARY: ROUTE FAILS AT a failed exact check (" + ", ".join(FAILS) + ")")
    sys.exit(1)
HITS = [
    "HIT: the link-dressed frame walk H[E, U] = (1/2) sum_j {E^j.sigma, S_j^U} with SU(2) links is hermitian and exactly "
    "gauge covariant (checked with Gaussian-rational SU(2) elements on the 4^3 torus); its pure-gauge links g_x g_y^dag "
    "give at first order exactly block 65's twist hop (1/2) sum_a C_a[d_a theta_a], and with the frame rotation block 65's "
    "-(i/2)[theta.sigma, H].",
    "HIT: block 70's species maps are gauge transformations g_x = (-1)^{n.x} i sigma_c: species n of (E, U = 1) is species "
    "000 of (rho_c E, U = (-1)^{n_j} on bonds along j), a flat Z2 connection; the frame's response turns covariantly, so "
    "block 74's count (two of eight) is unchanged at fixed links, and connection terms, proportional to plaquette "
    "curvature, vanish on these flat backgrounds (no supply of the missing shear at first order).",
]
print("SUMMARY: PARTIAL SU(2) links make the frame walk exactly gauge covariant, give block 65's twist hop as pure gauge, and "
      "turn the species maps into a flat Z2 connection; the species count is unchanged (task HIT not met)")
print("\n".join(HITS))
