#!/usr/bin/env python3
"""Referee for J:derive:su2-bond-links-exact-blindness-and-the-species:a3.

Exact Gaussian-rational SU(2) on the 4^3 torus. The operators are the task's,
written independently of the attempt's script.
"""
import itertools
import sys
from fractions import Fraction as Fr

FAILS = []
L = 4
SITES = list(itertools.product(range(L), repeat=3))
I2 = (((Fr(1), Fr(0)), (Fr(0), Fr(0))), ((Fr(0), Fr(0)), (Fr(1), Fr(0))))
Z2 = (((Fr(0), Fr(0)), (Fr(0), Fr(0))), ((Fr(0), Fr(0)), (Fr(0), Fr(0))))
# Pauli
S1 = (((Fr(0), Fr(0)), (Fr(1), Fr(0))), ((Fr(1), Fr(0)), (Fr(0), Fr(0))))
S2 = (((Fr(0), Fr(0)), (Fr(0), Fr(-1))), ((Fr(0), Fr(1)), (Fr(0), Fr(0))))
S3 = (((Fr(1), Fr(0)), (Fr(0), Fr(0))), ((Fr(0), Fr(0)), (Fr(-1), Fr(0))))
PAULI = (S1, S2, S3)


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


def gc(a, b=0):
    return (Fr(a), Fr(b))


def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def gsub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def gmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def gconj(z):
    return (z[0], -z[1])


def gzero(z):
    return z == (Fr(0), Fr(0))


def madd(a, b):
    return tuple(tuple(gadd(a[i][j], b[i][j]) for j in range(2)) for i in range(2))


def msub(a, b):
    return tuple(tuple(gsub(a[i][j], b[i][j]) for j in range(2)) for i in range(2))


def mm(a, b):
    out = [[gc(0), gc(0)], [gc(0), gc(0)]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                out[i][j] = gadd(out[i][j], gmul(a[i][k], b[k][j]))
    return tuple(tuple(row) for row in out)


def msc(a, z):
    return tuple(tuple(gmul(z, a[i][j]) for j in range(2)) for i in range(2))


def dag(a):
    return tuple(tuple(gconj(a[j][i]) for j in range(2)) for i in range(2))


def meq(a, b):
    return all(a[i][j] == b[i][j] for i in range(2) for j in range(2))


def det(a):
    return gsub(gmul(a[0][0], a[1][1]), gmul(a[0][1], a[1][0]))


def vadd(a, b):
    return (gadd(a[0], b[0]), gadd(a[1], b[1]))


def vsub(a, b):
    return (gsub(a[0], b[0]), gsub(a[1], b[1]))


def mv(a, v):
    return (gadd(gmul(a[0][0], v[0]), gmul(a[0][1], v[1])),
            gadd(gmul(a[1][0], v[0]), gmul(a[1][1], v[1])))


def veq(a, b):
    return a[0] == b[0] and a[1] == b[1]


def dot_sigma(v):
    m = Z2
    for a in range(3):
        m = madd(m, msc(PAULI[a], gc(v[a])))
    return m


def su2_quat(a, b, c, d):
    # a I + i (b σ1 + c σ2 + d σ3)
    return madd(msc(I2, gc(a)), msc(dot_sigma((b, c, d)), gc(0, 1)))


def stereo(x, y, z):
    r2 = Fr(x) ** 2 + Fr(y) ** 2 + Fr(z) ** 2
    den = 1 + r2
    return su2_quat((1 - r2) / den, 2 * Fr(x) / den, 2 * Fr(y) / den, 2 * Fr(z) / den)


def is_su2(g):
    return meq(mm(g, dag(g)), I2) and det(g) == gc(1)


def shift(x, j, s):
    y = list(x)
    y[j] = (y[j] + s) % L
    return tuple(y)


def link_of(U, x, j, s):
    if s == 1:
        return U[(x, j)]
    y = shift(x, j, -1)
    return dag(U[(y, j)])


def apply_S(U, psi, j):
    out = {}
    for x in SITES:
        hop = vsub(mv(link_of(U, x, j, 1), psi[shift(x, j, 1)]),
                   mv(link_of(U, x, j, -1), psi[shift(x, j, -1)]))
        out[x] = mv(msc(I2, gc(0, Fr(-1, 2))), hop)  # 1/(2i) = -i/2
    return out


def frame_A(E):
    return { (x, j): dot_sigma(E[(x, j)]) for x in SITES for j in range(3) }


def apply_H(E, U, psi):
    A = frame_A(E)
    out = {x: (gc(0), gc(0)) for x in SITES}
    for j in range(3):
        Spsi = apply_S(U, psi, j)
        Apsi = {x: mv(A[(x, j)], psi[x]) for x in SITES}
        SApsi = apply_S(U, Apsi, j)
        ASpsi = {x: mv(A[(x, j)], Spsi[x]) for x in SITES}
        for x in SITES:
            out[x] = vadd(out[x], vadd(SApsi[x], ASpsi[x]))
    half = gc(Fr(1, 2))
    return {x: (gmul(half, out[x][0]), gmul(half, out[x][1])) for x in SITES}


def field_eq(a, b):
    return all(veq(a[x], b[x]) for x in SITES)


def inner(a, b):
    s = gc(0)
    for x in SITES:
        s = gadd(s, gadd(gmul(gconj(a[x][0]), b[x][0]), gmul(gconj(a[x][1]), b[x][1])))
    return s


# ---------- explicit rational data ----------
GS = [stereo(0, 0, 0), stereo(1, 0, 0), stereo(1, 1, 0), stereo(1, 2, -1)]
ok("R1", all(is_su2(g) for g in GS), "inverse stereographic images of rational points are SU(2)")

# SO(3): g σ_b g† = Σ_a R_ab σ_a, R orthogonal det 1
def so3(g):
    cols = []
    for b in range(3):
        conj = mm(g, mm(PAULI[b], dag(g)))
        # extract coefficients: σ1_01 = 1, σ2_01 = -i, σ3_00 = 1
        r1 = conj[0][1][0]  # real part of (1,2) entry is the σ1 coeff; σ2 contributes imag
        # M = r1 σ1 + r2 σ2 + r3 σ3
        # M_00 = r3, M_01 = r1 - i r2
        r3 = conj[0][0][0]
        r1 = conj[0][1][0]
        r2 = -conj[0][1][1]
        if not (gzero((conj[0][0][1], Fr(0))) and conj[1][1][0] == -r3 and conj[0][1][1] == -r2):
            return None
        cols.append((r1, r2, r3))
    # columns are images of e_b, so R_ab = cols[b][a]
    R = tuple(tuple(cols[b][a] for b in range(3)) for a in range(3))
    RtR = tuple(tuple(sum(R[k][i] * R[k][j] for k in range(3)) for j in range(3)) for i in range(3))
    orth = all(RtR[i][j] == (Fr(1) if i == j else Fr(0)) for i in range(3) for j in range(3))
    detR = (R[0][0] * (R[1][1] * R[2][2] - R[1][2] * R[2][1])
            - R[0][1] * (R[1][0] * R[2][2] - R[1][2] * R[2][0])
            + R[0][2] * (R[1][0] * R[2][1] - R[1][1] * R[2][0]))
    return orth and detR == 1

ok("R2", all(so3(g) for g in GS), "conjugation by these SU(2) elements is a rational rotation, det 1")

def ident_U():
    return {(x, j): I2 for x in SITES for j in range(3)}


def ident_E():
    return {(x, j): tuple(Fr(1) if a == j else Fr(0) for a in range(3)) for x in SITES for j in range(3)}


# one non-trivial frame, links and state
E = {}
U = {}
psi = {}
phi = {}
gfield = {}
for n, x in enumerate(SITES):
    gx, gy, gz = (n % 3) - 1, ((n // 3) % 3) - 1, ((n // 9) % 3) - 1
    gfield[x] = stereo(gx, gy, gz)
    for j in range(3):
        E[(x, j)] = (Fr((n + j) % 3 - 1), Fr((n + 2 * j) % 3 - 1), Fr((n + j) % 2))
        U[(x, j)] = GS[(n + j) % 4]
    psi[x] = (gc(Fr((n % 5) - 2), Fr((n % 3) - 1)), gc(Fr((n % 4) - 1), Fr(0)))
    phi[x] = (gc(Fr((n % 2)), Fr(1, n + 1)), gc(Fr(0), Fr((n % 3) - 1)))

Hpsi = apply_H(E, U, psi)
Hphi = apply_H(E, U, phi)
ok("R3", inner(phi, Hpsi) == inner(Hphi, psi), "H[E, U] is hermitian on the 4^3 torus for this rational frame and these links")


def gauge_E(E, gfield):
    out = {}
    for x in SITES:
        for j in range(3):
            # v' · σ = g (v·σ) g†, read off by so3 coefficients
            conj = mm(gfield[x], mm(dot_sigma(E[(x, j)]), dag(gfield[x])))
            r3 = conj[0][0][0]
            r1 = conj[0][1][0]
            r2 = -conj[0][1][1]
            out[(x, j)] = (r1, r2, r3)
    return out


def gauge_U(U, gfield):
    return {(x, j): mm(gfield[x], mm(U[(x, j)], dag(gfield[shift(x, j, 1)]))) for x in SITES for j in range(3)}


psi_g = {x: mv(gfield[x], psi[x]) for x in SITES}
left = apply_H(gauge_E(E, gfield), gauge_U(U, gfield), psi_g)
right = {x: mv(gfield[x], Hpsi[x]) for x in SITES}
ok("R4", field_eq(left, right), "H[g E g†, g_x U g_y†] g ψ = g H[E, U] ψ at every site of the 4^3 torus")

# first order: link piece equals (1/2) sum_j C_j[d_j θ_j], and link+frame equals -(i/2)[θ·σ, H]
# θ rational and small enough that we compare the linearized operators, which are the derivatives.

def theta_of(x):
    return (Fr(x[0] - 1), Fr(x[1] % 2), Fr(1 - x[2]))


def dtheta(x, j):
    return tuple(theta_of(shift(x, j, 1))[a] - theta_of(x)[a] for a in range(3))


def delta_S(psi_, j):
    out = {}
    for x in SITES:
        vp = mv(dot_sigma(dtheta(x, j)), psi_[shift(x, j, 1)])
        vm = mv(dot_sigma(dtheta(shift(x, j, -1), j)), psi_[shift(x, j, -1)])
        out[x] = (gmul(gc(Fr(1, 4)), vadd(vp, vm)[0]), gmul(gc(Fr(1, 4)), vadd(vp, vm)[1]))
    return out


def twist(psi_):
    """(1/2) sum_j C_j[∂_j θ_j], C[v]ψ = (1/2)(v(x)ψ(x+e)+v(x-e)ψ(x-e))."""
    out = {x: (gc(0), gc(0)) for x in SITES}
    for j in range(3):
        for x in SITES:
            vp = (gmul(gc(dtheta(x, j)[j]), psi_[shift(x, j, 1)][0]),
                  gmul(gc(dtheta(x, j)[j]), psi_[shift(x, j, 1)][1]))
            xm = shift(x, j, -1)
            vm = (gmul(gc(dtheta(xm, j)[j]), psi_[xm][0]), gmul(gc(dtheta(xm, j)[j]), psi_[xm][1]))
            term = vadd(vp, vm)
            term = (gmul(gc(Fr(1, 4)), term[0]), gmul(gc(Fr(1, 4)), term[1]))  # 1/2 * 1/2
            out[x] = vadd(out[x], term)
    return out


def link_delta_H(psi_):
    """(1/2) sum_j {σ_j, δS_j} at the identity frame."""
    out = {x: (gc(0), gc(0)) for x in SITES}
    for j in range(3):
        dS = delta_S(psi_, j)
        spun = {x: mv(PAULI[j], psi_[x]) for x in SITES}
        dS_spun = delta_S(spun, j)
        for x in SITES:
            both = vadd(mv(PAULI[j], dS[x]), dS_spun[x])
            out[x] = vadd(out[x], (gmul(gc(Fr(1, 2)), both[0]), gmul(gc(Fr(1, 2)), both[1])))
    return out


def cross(t, j):
    e = [Fr(0), Fr(0), Fr(0)]
    e[j] = Fr(1)
    return (t[1] * e[2] - t[2] * e[1], t[2] * e[0] - t[0] * e[2], t[0] * e[1] - t[1] * e[0])


def frame_delta_H(psi_):
    out = {x: (gc(0), gc(0)) for x in SITES}
    U0 = ident_U()
    for j in range(3):
        dA = {x: dot_sigma(cross(theta_of(x), j)) for x in SITES}
        Spsi = apply_S(U0, psi_, j)
        S_dA = apply_S(U0, {y: mv(dA[y], psi_[y]) for y in SITES}, j)
        for x in SITES:
            both = vadd(mv(dA[x], Spsi[x]), S_dA[x])
            out[x] = vadd(out[x], (gmul(gc(Fr(1, 2)), both[0]), gmul(gc(Fr(1, 2)), both[1])))
    return out


def commutator_H(psi_):
    """-(i/2)[θ·σ, H_0] ψ = -(i/2)(θ·σ Hψ - H(θ·σ ψ))."""
    U0, E0 = ident_U(), ident_E()
    H0 = apply_H(E0, U0, psi_)
    spun = {x: mv(dot_sigma(theta_of(x)), psi_[x]) for x in SITES}
    Hspun = apply_H(E0, U0, spun)
    out = {}
    for x in SITES:
        comm = vadd(mv(dot_sigma(theta_of(x)), H0[x]), (gmul(gc(-1), Hspun[x][0]), gmul(gc(-1), Hspun[x][1])))
        # -(i/2) * comm
        factor = gmul(gc(0, Fr(-1, 2)), gc(1))  # -i/2
        out[x] = (gmul(factor, comm[0]), gmul(factor, comm[1]))
    return out


link = link_delta_H(psi)
hop = twist(psi)
total = {x: vadd(link[x], frame_delta_H(psi)[x]) for x in SITES}
comm = commutator_H(psi)
ok("R5", field_eq(link, hop) and field_eq(total, comm),
   "at first order the pure-gauge link is the twist hop, and link plus rotated frame equals -(i/2)[θ·σ, H]")

# species maps
flat = True
spec = True
su = True
for nvec in itertools.product((0, 1), repeat=3):
    for c in range(3):
        def g_at(x, nvec=nvec, c=c):
            sign = Fr(1) if sum(nvec[i] * x[i] for i in range(3)) % 2 == 0 else Fr(-1)
            return msc(msc(PAULI[c], gc(0, 1)), gc(sign))  # (-1)^{n·x} i σ_c

        for x in SITES:
            if not is_su2(g_at(x)):
                su = False
        # U' on +e_j is (-1)^{n_j}
        Usp = {(x, j): mm(g_at(x), dag(g_at(shift(x, j, 1)))) for x in SITES for j in range(3)}
        for x in SITES:
            for j in range(3):
                want = msc(I2, gc(1 if nvec[j] == 0 else -1))
                if not meq(Usp[(x, j)], want):
                    flat = False
        for x in SITES:
            for j, k in ((0, 1), (1, 2), (2, 0)):
                h = I2
                y1 = shift(x, j, 1)
                y2 = shift(y1, k, 1)
                y3 = shift(y2, j, -1)
                path = [(x, j, 1), (y1, k, 1), (y2, j, -1), (y3, k, -1)]
                for p, d, s in path:
                    h = mm(h, link_of(Usp, p, d, s))
                if not meq(h, I2):
                    flat = False
        # zero mode
        u = (gc(Fr(1), Fr(0)), gc(Fr(0), Fr(1)))
        mode = {}
        for x in SITES:
            sign = gc(1 if sum(nvec[i] * x[i] for i in range(3)) % 2 == 0 else -1)
            mode[x] = (gmul(sign, u[0]), gmul(sign, u[1]))
        if not field_eq(apply_H(ident_E(), ident_U(), mode), {x: (gc(0), gc(0)) for x in SITES}):
            spec = False
        image = {x: mv(g_at(x), mode[x]) for x in SITES}
        const = image[SITES[0]]
        if any(not veq(image[x], const) for x in SITES):
            spec = False
        # background (ρ_c E, U')
        rhoE = {}
        Up = {}
        for x in SITES:
            for j in range(3):
                # ρ_c sends σ_j to σ_c σ_j σ_c = +σ_j if j=c else -σ_j
                sgn = Fr(1) if j == c else Fr(-1)
                rhoE[(x, j)] = tuple(sgn if a == j else Fr(0) for a in range(3))
                Up[(x, j)] = msc(I2, gc(1 if nvec[j] == 0 else -1))
        if not field_eq(apply_H(rhoE, Up, {x: const for x in SITES}), {x: (gc(0), gc(0)) for x in SITES}):
            spec = False

ok("R6", su and flat and spec,
   "g_x = (-1)^{n·x} i σ_c is SU(2); U'=(-1)^{n_j} is a flat Z2 connection; species-n zero modes map to constant zero modes of the rotated background")

# response turns with R
def theta_resp(E_, U_, psi_):
    out = {}
    for j in range(3):
        Spsi = apply_S(U_, psi_, j)
        for a in range(3):
            for x in SITES:
                comp = inner_one(psi_[x], mv(PAULI[a], Spsi[x]))
                out[(x, a, j)] = comp[0]
    return out


def inner_one(p, q):
    return gadd(gmul(gconj(p[0]), q[0]), gmul(gconj(p[1]), q[1]))


Th = theta_resp(E, U, psi)
Thg = theta_resp(gauge_E(E, gfield), gauge_U(U, gfield), psi_g)
good = True
for x in SITES:
    g = gfield[x]
    # R_ab from g σ_b g†
    cols = []
    for b in range(3):
        conj = mm(g, mm(PAULI[b], dag(g)))
        cols.append((conj[0][1][0], -conj[0][1][1], conj[0][0][0]))
    for j in range(3):
        for a in range(3):
            acc = sum(cols[b][a] * Th[(x, b, j)] for b in range(3))
            if Thg[(x, a, j)] != acc:
                good = False
ok("R7", good,
   "the frame response Θ_a^j = Re ψ† σ_a S_j ψ turns by the SO(3) image of g_x")

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - the link-dressed frame walk is hermitian and gauge covariant, the pure-gauge link reproduces the twist hop at first order, and the species maps are a flat Z2 connection, so a coin-blind connection does not change the species count at first order.")
print("HIT: confirmed - on the 4^3 torus with Gaussian-rational SU(2), H[gEg†, gUg†]=gHg†, the first-order pure-gauge link equals the scalar twist hop and together with the rotated frame equals -(i/2)[θ·σ, H], and each species n is species 000 of a flat Z2 background (ρ_c E, (-1)^{n_j}); the served-species count is therefore unchanged at fixed links and, because those backgrounds are flat, at first order in a dynamical connection.")
