#!/usr/bin/env python3
"""J:note falsifiers for U1_FINITE_STEP_GAUGE_COVARIANT_MATTER_CURRENT_OPERATOR_WORK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-09-03 (on main).

Falsifiers implemented (the note's list): the bond unitary is not unitary or fails charge conservation; the integrated current fails
either endpoint continuity equation; "the analytic current formula, gauge covariance, or orientation rule fails"; "endpoint and
midpoint refinement orders do not separate as stated"; "an operational colored-layer current has off-bond support"; "any of the
three-site or 64-site continuity equations fails" (here at 216 and 512 sites); the Gauss residual; "anticommutator work differs from
the operator field-energy change"; "the anticommutator work is non-Hermitian"; "the left-ordered control accidentally satisfies the
noncommuting identity"; "the commuting operator limit fails to recover classical midpoint work".

Disjoint machinery, exact arithmetic, beyond the note's sizes (the note's runner is floating point at L = 4 and with three Pauli field
components):
  1. symbolic bond (sympy, symbols t, h, A, alpha_t, alpha_h): V_h, the current (V^dag n_h V - n_h)/h against the closed form, both
     endpoint equations, Hermiticity, tracelessness, t = 0, G H G^dag = H(A + alpha_h - alpha_t) for H, V and the current, the
     orientation rule X Jbar(A) X = -Jbar(-A), and the refinement orders as exact h-series of Jbar - J_0 and Jbar - J(h/2);
  2. colored cubic tori L = 4, 6, 8 in exact Gaussian-rational arithmetic: per-bond hopping and link phases on rational points of the
     unit circle (cos th, sin th, cos A, sin A rational), h = 1/2; every color a perfect matching, every layer exactly unitary, every
     operational current exactly the closed form and on its bond, and at EVERY vertex the full-tick change T^dag n_x T - n_x equal
     exactly to h sum_l (+-) P_{l-1}^dag J_l P_{l-1} (currents transported through their actual prefix); with E_e' = E_e + h J_e^init
     this is the Gauss-residual preservation (in-minus-out divergence) at every vertex; support of the initial-frame currents reported;
  3. operator field work on the periodic cubic curl lattice L = 3 (81 electric + 81 magnetic operator components) in exact QQ(i):
     the parent's update B1 = B + (h/2) C E, E' = E - h C^T B1 + h J, B' = B1 + (h/2) C E', H_h = (1/2) x^T M x, with every J_e an
     actual integrated bond current of a hop dressed by a Z_3 clock link (so J_e contains the link shift and does not commute with the
     link electric field), all components 6 x 6 operators; plus the scalar (commuting) limit.
"""
from __future__ import annotations

import random
from collections import defaultdict

import sympy as sp
from sympy.polys.domains import QQ, QQ_I

ZERO, ONE, IU = QQ_I(0, 0), QQ_I(1, 0), QQ_I(0, 1)
TRIPLES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (12, 35, 37), (9, 40, 41)]


def conj(z):
    return QQ_I(z.x, -z.y)


# ----------------------------------------------------------------------------------------------------------------- 1. symbolic bond
def symbolic():
    X = sp.Matrix([[0, 1], [1, 0]])
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    Z = sp.Matrix([[1, 0], [0, -1]])
    I2 = sp.eye(2)
    t, h, A, at, ah = sp.symbols("t h A alpha_t alpha_h", real=True)
    zero = sp.zeros(2, 2)

    def is0(M):
        return all(sp.simplify(sp.expand(sp.expand_trig(sp.expand(e)).rewrite(sp.exp))) == 0 for e in M)
    Hb = lambda a: -t * (sp.cos(a) * X + sp.sin(a) * Y)
    Vh = lambda a, hh: sp.cos(t * hh) * I2 + sp.I * sp.sin(t * hh) * (sp.cos(a) * X + sp.sin(a) * Y)
    nt, nh = (I2 + Z) / 2, (I2 - Z) / 2
    V = Vh(A, h)
    res = {}
    # V_h really is exp(-i h H_b): d/dh V = -i H_b V and V(0) = I
    res["V = exp(-ihH)"] = is0(sp.diff(V, h) + sp.I * Hb(A) * V) and V.subs(h, 0) == I2
    res["unitary"] = is0(V.H * V - I2)
    res["charge conserved"] = is0(V.H * (nt + nh) * V - (nt + nh))
    Jb = lambda a: (Vh(a, h).H * nh * Vh(a, h) - nh) / h
    J = Jb(A)
    closed = sp.sin(2 * t * h) / (2 * h) * (sp.cos(A) * Y - sp.sin(A) * X) + (1 - sp.cos(2 * t * h)) / (2 * h) * Z
    res["closed form"] = is0(sp.expand_trig(J - closed))
    res["head continuity"] = is0(V.H * nh * V - nh - h * J)
    res["tail continuity"] = is0(V.H * nt * V - nt + h * J)
    res["Hermitian"] = is0(J - J.H)
    res["traceless"] = sp.simplify(J.trace()) == 0
    res["t = 0 gives 0"] = is0(J.subs(t, 0))
    G = sp.diag(sp.exp(sp.I * at), sp.exp(sp.I * ah))
    Ap = A + ah - at
    res["gauge H"] = is0(G * Hb(A) * G.H - Hb(Ap))
    res["gauge V"] = is0(G * V * G.H - Vh(Ap, h))
    res["gauge Jbar"] = is0(G * J * G.H - Jb(Ap))
    res["orientation"] = is0(X * J * X + Jb(-A))
    J0 = sp.I * (Hb(A) * nh - nh * Hb(A))
    res["J0 = t(cosA Y - sinA X)"] = is0(J0 - t * (sp.cos(A) * Y - sp.sin(A) * X))
    Vm = Vh(A, h / 2)
    Jmid = Vm.H * J0 * Vm

    def lowest(D, nmax=5):
        ser = D.applyfunc(lambda e: sp.series(e, h, 0, nmax).removeO())
        for k in range(nmax):
            ck = ser.applyfunc(lambda e: sp.simplify(sp.expand(e).coeff(h, k)))
            if ck != zero:
                return k, ck
        return None, zero

    k0, c0 = lowest(J - J0)
    km, cm = lowest(J - Jmid)
    res["orders"] = (k0, km)
    res["ok orders"] = k0 == 1 and km == 2 and is0(c0 - t ** 2 * Z) and \
        is0(cm + t ** 3 / 6 * (sp.cos(A) * Y - sp.sin(A) * X))
    return res


# ------------------------------------------------------------------------------------------------------ 2. exact colored tori
def unit_point(rng):
    a, b, c = rng.choice(TRIPLES)
    if rng.random() < 0.5:
        a, b = b, a
    return QQ(a, c), QQ(b, c)


def phase(rng):
    ca, sa = unit_point(rng)
    return QQ_I(ca * rng.choice((1, -1)), sa * rng.choice((1, -1)))


def bond_blocks(c, s, eA, h):
    """V = c I + i s N, N = [[0, e^{-iA}], [e^{iA}, 0]] in basis (tail, head); operational current (V^dag n_h V - n_h)/h."""
    cI, sI = QQ_I(c, 0), QQ_I(s, 0)
    V = [[cI, IU * sI * conj(eA)], [IU * sI * eA, cI]]
    Vd = [[conj(V[j][i]) for j in range(2)] for i in range(2)]
    # V^dag n_h V: n_h = diag(0, 1)
    M = [[Vd[i][1] * V[1][j] for j in range(2)] for i in range(2)]
    invh = QQ_I(1 / h, 0)
    J = [[(M[i][j] - (ONE if (i == j == 1) else ZERO)) * invh for j in range(2)] for i in range(2)]
    s2, c2 = 2 * s * c, c * c - s * s
    k1, k2 = QQ_I(s2 / (2 * h), 0), QQ_I((1 - c2) / (2 * h), 0)
    closed = [[k2, k1 * (-IU) * conj(eA)], [k1 * IU * eA, -k2]]
    unitary = all(sum((Vd[i][k] * V[k][j] for k in range(2)), ZERO) == (ONE if i == j else ZERO) for i in range(2) for j in range(2))
    return V, J, J == closed, unitary, all(J[i][j] == conj(J[j][i]) for i in range(2) for j in range(2))


def torus(L, h=QQ(1, 2), seed=7):
    rng = random.Random(seed * 1000 + L)
    n = L ** 3
    idx = lambda c: (c[0] % L) * L * L + (c[1] % L) * L + (c[2] % L)
    layers = []  # each: dict site -> (partner, is_head, bond id); bond list [(tail, head, V, J)]
    ok = {"matching": True, "unitary": True, "closed form": True, "Hermitian": True}
    nbonds = 0
    for axis in range(3):
        for parity in (0, 1):
            site, bonds = {}, []
            for x in range(L):
                for y in range(L):
                    for z in range(L):
                        c = (x, y, z)
                        if c[axis] % 2 != parity:
                            continue
                        d = list(c)
                        d[axis] += 1
                        a, b = idx(c), idx(d)
                        cc, ss = unit_point(rng)
                        V, J, closed, unit, herm = bond_blocks(cc, ss, phase(rng), h)
                        ok["closed form"] &= closed
                        ok["unitary"] &= unit
                        ok["Hermitian"] &= herm
                        if a in site or b in site:
                            ok["matching"] = False
                        site[a] = (b, False, len(bonds))
                        site[b] = (a, True, len(bonds))
                        bonds.append((a, b, V, J))
            ok["matching"] &= len(site) == n
            nbonds += len(bonds)
            layers.append((site, bonds))
    # prefixes P_0 = I, P_l = U_l P_{l-1}; rows as sparse dicts
    P = [[{x: ONE} for x in range(n)]]
    for site, bonds in layers:
        prev, new = P[-1], []
        for x in range(n):
            partner, is_head, bid = site[x]
            a, b, V, _ = bonds[bid]
            i = 1 if is_head else 0
            row = defaultdict(lambda: ZERO)
            for col_site, coef in ((a, V[i][0]), (b, V[i][1])):
                if coef == ZERO:
                    continue
                for k, v in prev[col_site].items():
                    row[k] += coef * v
            new.append({k: v for k, v in row.items() if v != ZERO})
        P.append(new)
    T = P[-1]
    hI = QQ_I(h, 0)
    cont_ok, max_res_entries, support = True, 0, [0] * 6
    for x in range(n):
        lhs = defaultdict(lambda: ZERO)
        for i, vi in T[x].items():
            cvi = conj(vi)
            for j, vj in T[x].items():
                lhs[(i, j)] += cvi * vj
        lhs[(x, x)] -= ONE
        rhs = defaultdict(lambda: ZERO)
        for l, (site, bonds) in enumerate(layers):
            partner, is_head, bid = site[x]
            a, b, _, J = bonds[bid]
            sgn = hI if is_head else -hI
            rows = (P[l][a], P[l][b])
            term = defaultdict(lambda: ZERO)
            for pi in range(2):
                for qi in range(2):
                    Jpq = J[pi][qi]
                    if Jpq == ZERO:
                        continue
                    for i, vi in rows[pi].items():
                        cvi = conj(vi) * Jpq * sgn
                        for j, vj in rows[qi].items():
                            term[(i, j)] += cvi * vj
            sup = set()
            for (i, j), v in term.items():
                if v != ZERO:
                    rhs[(i, j)] += v
                    sup.update((i, j))
            support[l] = max(support[l], len(sup))
        keys = set(lhs) | set(rhs)
        bad = sum(1 for k in keys if lhs.get(k, ZERO) != rhs.get(k, ZERO))
        if bad:
            cont_ok = False
            max_res_entries = max(max_res_entries, bad)
    # total charge: sum_x of the full-tick change vanishes because T is unitary; check T T^dag = I row-wise on a sample of pairs
    unit_T = all(sum((v * conj(T[y].get(k, ZERO)) for k, v in T[x].items()), ZERO) == (ONE if x == y else ZERO)
                 for x in range(0, n, max(1, n // 16)) for y in range(n))
    return {"sites": n, "bonds": nbonds, **ok, "tick unitary (rows)": unit_T, "continuity at every vertex": cont_ok,
            "max bad entries": max_res_entries, "initial-frame support by layer": support}


# ------------------------------------------------------------------------------------------------ 3. exact operator field work
D = 6


def mz():
    return [[ZERO] * D for _ in range(D)]


def madd(A, B, cb=ONE):
    return [[A[i][j] + cb * B[i][j] for j in range(D)] for i in range(D)]


def msc(A, c):
    return [[c * A[i][j] for j in range(D)] for i in range(D)]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(D)), ZERO) for j in range(D)] for i in range(D)]


def mdag(A):
    return [[conj(A[j][i]) for j in range(D)] for i in range(D)]


def rand_herm(rng, lo=-3, hi=3):
    M = mz()
    for i in range(D):
        M[i][i] = QQ_I(rng.randint(lo, hi), 0)
        for j in range(i + 1, D):
            z = QQ_I(rng.randint(lo, hi), rng.randint(lo, hi))
            M[i][j], M[j][i] = z, conj(z)
    return M


def clock_current(c, s, h):
    """Hop tail -> head dressed by a Z_3 clock link U (unitary shift): K = |h><t| (x) U + |t><h| (x) U^dag, K^2 = I,
    V = cI + i s K = exp(i t h K), current (V^dag n_h V - n_h)/h on C^2 (x) C^3."""
    U = [[ZERO] * 3 for _ in range(3)]
    for k in range(3):
        U[(k + 1) % 3][k] = ONE
    K = mz()
    for i in range(3):
        for j in range(3):
            K[3 + i][j] = U[i][j]          # |head><tail| (x) U   (tail = block 0, head = block 1)
            K[i][3 + j] = conj(U[j][i])    # |tail><head| (x) U^dag
    V = madd(msc(identity(), QQ_I(c, 0)), K, IU * QQ_I(s, 0))
    nh = mz()
    for i in range(3, 6):
        nh[i][i] = ONE
    Jc = madd(mm(mm(mdag(V), nh), V), nh, -ONE)
    unit = mm(mdag(V), V) == identity()
    return msc(Jc, QQ_I(1 / h, 0)), unit


def identity():
    M = mz()
    for i in range(D):
        M[i][i] = ONE
    return M


def curl_lattice(L):
    idx = lambda c: ((c[0] % L) * L + (c[1] % L)) * L + (c[2] % L)
    edge = lambda c, mu: 3 * idx(c) + mu
    faces = []
    for x in range(L):
        for y in range(L):
            for z in range(L):
                c = (x, y, z)
                for mu, nu in ((0, 1), (0, 2), (1, 2)):
                    cm = list(c); cm[mu] += 1
                    cn = list(c); cn[nu] += 1
                    faces.append({edge(c, mu): 1, edge(cm, nu): 1, edge(cn, mu): -1, edge(c, nu): -1})
    return faces, 3 * L ** 3


def field_work(L=3, h=QQ(1, 2), seed=11, scalar=False):
    global D
    D = 1 if scalar else 6
    rng = random.Random(seed)
    faces, ne = curl_lattice(L)
    a = h / 2
    aI, hI = QQ_I(a, 0), QQ_I(h, 0)
    CT = defaultdict(dict)
    for f, row in enumerate(faces):
        for e, v in row.items():
            CT[e][f] = v
    if scalar:
        E = [[[QQ_I(rng.randint(-5, 5), 0)]] for _ in range(ne)]
        B = [[[QQ_I(rng.randint(-5, 5), 0)]] for _ in range(len(faces))]
        J = [[[QQ_I(QQ(rng.randint(-9, 9), rng.randint(1, 4)), 0)]] for _ in range(ne)]
        unit_all = True
    else:
        Eclock = mz()
        for k in range(6):
            Eclock[k][k] = QQ_I((k % 3) - 1, 0)       # I_2 (x) diag(-1, 0, 1)
        E = [madd(msc(Eclock, QQ_I(rng.randint(1, 3), 0)), rand_herm(rng, -1, 1)) for _ in range(ne)]
        B = [rand_herm(rng) for _ in faces]
        J, unit_all = [], True
        for _ in range(ne):
            c, s = unit_point(rng)
            Je, u = clock_current(c, s, h)
            J.append(Je)
            unit_all &= u
    curlE = lambda Ev: [sum_ops([(v, Ev[e]) for e, v in row.items()]) for row in faces]

    def curlT(Bv):
        return [sum_ops([(v, Bv[f]) for f, v in CT[e].items()]) for e in range(ne)]

    def energy(Ev, Bv):
        CE = curlE(Ev)
        MEE = [madd(Ev[e], w, -aI * aI) for e, w in enumerate(curlT(CE))]
        tot = mz()
        for e in range(ne):
            tot = madd(tot, mm(Ev[e], MEE[e]))
        for f in range(len(faces)):
            tot = madd(tot, mm(Bv[f], Bv[f]))
        return msc(tot, QQ_I(QQ(1, 2), 0))

    B1 = [madd(B[f], w, aI) for f, w in enumerate(curlE(E))]
    CTB1 = curlT(B1)
    E2 = [madd(madd(E[e], CTB1[e], -hI), J[e], hI) for e in range(ne)]
    B2 = [madd(B1[f], w, aI) for f, w in enumerate(curlE(E2))]
    dH = madd(energy(E2, B2), energy(E, B), -ONE)
    anti, left = mz(), mz()
    for e in range(ne):
        S = madd(E[e], E2[e])
        anti = madd(anti, madd(mm(J[e], S), mm(S, J[e])))
        left = madd(left, mm(J[e], S))
    anti = msc(anti, hI * QQ_I(QQ(1, 4), 0))
    left = msc(left, hI * QQ_I(QQ(1, 2), 0))
    comm = any(mm(J[e], E[e]) != mm(E[e], J[e]) for e in range(ne))
    rl = madd(left, dH, -ONE)
    al = madd(left, mdag(left), -ONE)
    mx = lambda M: max(abs(complex(float(z.x), float(z.y))) for row in M for z in row)
    return {"components": (ne, len(faces)), "dim": D, "clock hops unitary": unit_all, "[J_e, E_e] != 0 somewhere": comm,
            "dH == (h/4) sum {J, E+E'}": dH == anti, "dH Hermitian": dH == mdag(dH), "left residual max": mx(rl),
            "left anti-Hermitian max": mx(al)}


def sum_ops(terms):
    tot = mz()
    for v, M in terms:
        tot = madd(tot, M, QQ_I(v, 0))
    return tot


def main():
    s = symbolic()
    print(f"1. symbolic bond: {s}")
    tori = {}
    for L in (4, 6, 8):
        tori[L] = torus(L)
        print(f"2. exact torus L = {L}: {tori[L]}")
    w = field_work()
    print(f"3. exact operator field work, cubic curl lattice L = 3, clock-link currents: {w}")
    ws = field_work(scalar=True)
    key = "dH == (h/4) sum {J, E+E'}"
    print(f"3'. commuting (scalar) limit, same lattice: dH == h J^T (E+E')/2: {ws[key]}, "
          f"left-ordered residual {ws['left residual max']}")
    fails = [k for k, v in s.items() if k not in ("orders",) and v is not True]
    for L, r in tori.items():
        fails += [f"L={L} {k}" for k in ("matching", "unitary", "closed form", "Hermitian", "tick unitary (rows)",
                                          "continuity at every vertex") if not r[k]]
        if r["bonds"] != 3 * L ** 3:
            fails.append(f"L={L} bond count")
    if not (w["clock hops unitary"] and w["[J_e, E_e] != 0 somewhere"] and w[key] and w["dH Hermitian"]):
        fails.append("operator work")
    if w["left residual max"] == 0 or w["left anti-Hermitian max"] == 0:
        fails.append("left-ordered control satisfies the identity")
    if not ws[key] or ws["left residual max"] != 0:
        fails.append("commuting limit")
    if fails:
        print(f"HIT: a falsifier fires: {fails}")
    k0, km = s["orders"]
    sup = {L: tori[L]["initial-frame support by layer"] for L in tori}
    print(f"SUMMARY: bond identities hold symbolically (closed form, both continuity equations, Hermitian, traceless, gauge covariance "
          f"of H, V and the current, orientation, t = 0); Jbar - J_0 starts at h^{k0} (t^2 h Z) and Jbar - J(h/2) at h^{km} "
          f"(-(t^3/6) h^2 (cosA Y - sinA X)); on exact rational-phase cubic tori L = 4, 6, 8 (64, 216, 512 vertices; 192, 648, 1536 "
          f"bonds) every color is a perfect matching, every layer unitary, every operational current the closed form on its bond, and "
          f"the full-tick change of n_x equals the prefix-transported layer currents exactly at every vertex (initial-frame support "
          f"by layer {sup[8]} sites at L = 8); operator work on 81 + 81 components of 6 x 6 clock-link operators equals "
          f"(h/4) sum {{J, E + E'}} exactly and is Hermitian, the left-ordered product misses it by {w['left residual max']:.3g} and "
          f"is non-Hermitian by {w['left anti-Hermitian max']:.3g}; the scalar limit is the classical midpoint law")


if __name__ == "__main__":
    main()
