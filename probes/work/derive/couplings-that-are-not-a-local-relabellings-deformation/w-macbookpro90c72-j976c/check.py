#!/usr/bin/env python3
"""J:derive:couplings-that-are-not-a-local-relabellings-deformation:a1 -- worker w-macbookpro90c72-j976c.

Block 54's walk H(k) = sigma.s(k), s_a = sin k_a (block 63's shifts), eight zeros k = pi n, D_n = diag((-1)^{n_a}).
A coupling dH[B] (hermitian, linear in a bond field B, translation-covariant, finite reach); on gradients X = dH[d xi]; for xi a plane
wave of wave vector p it maps k to k + p through a 2x2 kernel X_p(k).
  D1  the division: L(G) = H'G - GH, Phi(W) = H'W + WH obey L Phi = Phi L = Delta, Delta = |s(k+p)|^2 - |s(k)|^2
      = sum_a sin p_a sin(2k_a + p_a); so X = iL(G) has G = -i Phi(X)/Delta, local iff Delta divides Phi(X)       (exact)
  D2  on the shell |s'| = |s|: Phi(X) has no cross-band blocks and its same-band blocks are 2 sigma r times X's    (exact)
  D3  on a torus of side 2q (q prime >= 13) equal |s|^2 means related by the 384 symmetries of |s|^2; on 24^3 not   (lemma
      proved; q = 13 checked at 40 digits; the 24^3 pair exact)
  D4  at the species momenta p = pi n: H(k + pi n) = s_n R H(k) R^+ with a coin half turn R; the generator is local  (exact)
  D5  the example: X = i[F, xi], F = e_2(cos 2k) (reach four): conserved on every 2q torus, generator not local,
      not conserved on 24^3; it fails demands 2 and 3                                                              (exact)
  D6  the theorem: reach <= 2 and U_(111)'s reversal force one-step hops; species n then sees D_n g D_n            (exact)
  D7  the ladder: block 63's coupling (reach two) and block 69's (reach three) against demands 2 and 3            (exact)
  D8  curls: curl d = 0 and curl(uniform) = 0 on a torus; the divergence of a curl coupling's response vanishes     (exact)
  D9  executed: every nearest-neighbour coupling on gradients with an exact current on 2q tori (anchors in the
      search windows) is the U(1) coupling i[H, xi] (search_exact_current.py outputs)                               (float)
"""
import itertools
import os
import re

import numpy as np
import sympy as sp

NF = 0
NP = 0
HERE = os.path.dirname(os.path.abspath(__file__))
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
I2 = sp.eye(2)


def rep(tag, ok, msg):
    global NF, NP
    NF += (not ok)
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def sdot(v):
    return sum((SIG[a] * v[a] for a in range(3)), sp.zeros(2, 2))


def zero(M):
    return all(sp.simplify(e) == 0 for e in M)


# ---------------------------------------------------------------- D1
def D1():
    s = sp.symbols('s1:4'); t = sp.symbols('t1:4')
    W = sp.Matrix(2, 2, sp.symbols('w0:4'))
    H, Hp = sdot(s), sdot(t)
    L = lambda G: Hp * G - G * H
    Phi = lambda G: Hp * G + G * H
    Delta = sum(x**2 for x in t) - sum(x**2 for x in s)
    ok1 = zero((L(Phi(W)) - Delta * W).applyfunc(sp.expand)) and zero((Phi(L(W)) - Delta * W).applyfunc(sp.expand))
    k = sp.symbols('k1:4', real=True); p = sp.symbols('p1:4', real=True)
    d1 = sum(sp.sin(k[a] + p[a])**2 - sp.sin(k[a])**2 for a in range(3))
    d2 = sum(sp.sin(p[a]) * sp.sin(2 * k[a] + p[a]) for a in range(3))
    d3 = sum(sp.cos(2 * k[a]) - sp.cos(2 * k[a] + 2 * p[a]) for a in range(3)) / 2
    ok2 = sp.simplify(sp.expand_trig(d1 - d2)) == 0 and sp.simplify(sp.expand_trig(d1 - d3)) == 0
    rep("D1 the division", ok1 and ok2,
        "for symbolic s, s' and W: L(Phi(W)) = Phi(L(W)) = (|s'|^2 - |s|^2) W; so X = iL(G) forces G = -i Phi(X)/Delta wherever Delta "
        "!= 0, and a local G exists iff Delta divides Phi(X) (then G = -i Phi(X)/Delta solves X = iL(G) identically); Delta_p(k) = "
        "|s(k+p)|^2 - |s(k)|^2 = sum_a sin p_a sin(2k_a + p_a) = (1/2) sum_a [cos 2k_a - cos 2(k_a + p_a)]")


# ---------------------------------------------------------------- D2
def D2():
    s = sp.Matrix([3, 4, 0]) / 5 * 2; t = sp.Matrix([0, 3, 4]) / 5 * 2      # |s| = |t| = 2
    r = sp.sqrt(sum(x**2 for x in s))
    X = sp.Matrix([[sp.Rational(1, 3) + 2 * sp.I, sp.Rational(-5, 7)], [sp.Rational(2, 9) - sp.I, 3]])
    H, Hp = sdot(s), sdot(t)
    P = lambda v, sg: (I2 + sg * sdot(v) / r) / 2
    N = Hp * X + X * H
    ok = all(zero((P(t, sg) * N * P(s, -sg)).applyfunc(sp.simplify)) for sg in (1, -1))
    ok = ok and all(zero((P(t, sg) * N * P(s, sg) - 2 * sg * r * P(t, sg) * X * P(s, sg)).applyfunc(sp.simplify)) for sg in (1, -1))
    rep("D2 on the shell", ok,
        "for |s'| = |s| = r > 0 (exact rational instance, random X): Phi(X) has no cross-band blocks and P'_sg Phi(X) P_sg = 2 sg r "
        "P'_sg X P_sg; so X's same-energy blocks vanish at a pair exactly when Phi(X) does there")


# ---------------------------------------------------------------- D3
def D3():
    import mpmath as mp
    mp.mp.dps = 40
    q = 13
    vals = {}
    for j in itertools.product(range(q), repeat=3):
        v = mp.fsum(mp.cos(2 * mp.pi * x / q) for x in j)
        key = mp.nstr(v, 30)
        vals.setdefault(key, set()).add(tuple(sorted(min(x % q, (-x) % q) for x in j)))
    ok13 = all(len(cls) == 1 for cls in vals.values())
    # 24^3: k = (pi/3, 0, 0) and k' = (pi/6, pi/4, 0): cos 2k sums agree exactly, the pair is not symmetry-related
    c = lambda x: sp.cos(2 * x)
    k = (sp.pi / 3, 0, 0); kp = (sp.pi / 6, sp.pi / 4, 0)
    e1 = sp.nsimplify(sum(c(x) for x in k)); e1p = sp.nsimplify(sum(c(x) for x in kp))
    absk = sorted(sp.nsimplify(abs(c(x))) for x in k); abskp = sorted(sp.nsimplify(abs(c(x))) for x in kp)
    ok24 = e1 == e1p == sp.Rational(3, 2) and absk != abskp
    rep("D3 which pairs are degenerate", ok13 and ok24,
        f"on the torus of side 2q, q prime, 2k_a is a multiple of 2 pi/q, and |s(k)|^2 = |s(k')|^2 is a vanishing sum of 12 q-th roots of "
        f"unity with signs; for q >= 13 it cancels in pairs, so k' = g(k) for one of the 384 symmetries (proof in ATTEMPT S3); at q = 13 "
        f"the {len(vals)} values of sum cos 2k_a are exactly the classes of the multisets {{+-2k_a}} (40 digits); on 24^3 the pair "
        f"(pi/3,0,0), (pi/6,pi/4,0) has sum cos 2k = 3/2 for both and is not related by any symmetry (exact)")


# ---------------------------------------------------------------- D4
def D4():
    k = sp.symbols('k1:4', real=True)
    s = sp.Matrix([sp.sin(x) for x in k])
    ok = True
    halfturn = {0: SIG[0], 1: SIG[1], 2: SIG[2]}
    for n in itertools.product((0, 1), repeat=3):
        if n == (0, 0, 0):
            continue
        Dn = sp.diag(*[(-1)**x for x in n])
        sn = Dn.det()
        shifted = sp.Matrix([sp.sin(k[a] + sp.pi * n[a]) for a in range(3)])
        ok = ok and sp.simplify(shifted - Dn * s) == sp.zeros(3, 1)
        rot = sn * Dn                          # a proper rotation: a half turn about the axis it fixes, or the identity
        axis = [a for a in range(3) if rot[a, a] == 1]
        R = halfturn[axis[0]] if rot != sp.eye(3) else I2
        lhs = sdot(Dn * s)
        rhs = sn * R * sdot(s) * R.H
        ok = ok and zero((lhs - rhs).applyfunc(sp.simplify))
    # Koszul (the proof is in ATTEMPT S4): sin k_a = (z_a^2 - 1)/(2 i z_a) are a regular sequence, so every x with x.s = 0 is s x w;
    # the direction checked here is that such x are indeed relations
    w = sp.Matrix([sp.cos(k[1]), sp.sin(k[0] + k[2]), 1])
    x = s.cross(w)
    ok = ok and sp.simplify((x.T * s)[0]) == 0
    rep("D4 the species momenta", ok,
        "for all seven n != 0: sin(k + pi n) = D_n sin k and sigma.(D_n s) = s_n R (sigma.s) R^+ with R the coin's half turn about the axis "
        "fixed by s_n D_n; so at p = pi n the equation X = iL(G) becomes i(s_n H G~ - G~ H) = X~ at one wave vector; with the conditions at "
        "the zeros the solution is polynomial by the exactness of Koszul's complex for (sin k_1, sin k_2, sin k_3) (ATTEMPT S4): no "
        "obstruction at the species momenta")


# ---------------------------------------------------------------- D5
def D5():
    k = sp.symbols('k1:4', real=True)
    c2 = [sp.cos(2 * x) for x in k]
    F = c2[0] * c2[1] + c2[0] * c2[2] + c2[1] * c2[2]
    e1 = sum(c2)
    sub = lambda f, rep_: sp.simplify(sp.expand_trig(f.subs(rep_, simultaneous=True)))
    gens = [{k[0]: -k[0]}, {k[0]: k[0] + sp.pi}, {k[0]: k[1], k[1]: k[0]}, {k[0]: k[1], k[1]: k[2], k[2]: k[0]}]
    inv = all(sp.simplify(sub(F, g) - F) == 0 for g in gens)
    kk = (sp.pi / 3, 0, 0); kp = (sp.pi / 6, sp.pi / 4, 0)
    val = lambda f, pt: sp.nsimplify(f.subs({k[a]: pt[a] for a in range(3)}))
    f = val(F, kp) - val(F, kk)
    same_e1 = val(e1, kp) == val(e1, kk)
    s_of = lambda pt: sp.Matrix([sp.sin(x) for x in pt])
    N = sp.I * f * (sdot(s_of(kp)) + sdot(s_of(kk)))          # Phi(X) at the pair, X = i f 1
    nonzero_N = not zero(N.applyfunc(sp.simplify))
    r = sp.sqrt(sum(x**2 for x in s_of(kk)))
    P = lambda pt, sg: (I2 + sg * sdot(s_of(pt)) / r) / 2
    block = (P(kp, 1) * (sp.I * f * I2) * P(kk, 1)).applyfunc(sp.simplify)
    not_conserved_24 = not zero(block)
    # reach: the Fourier support of F (grid 8^3, the coefficients are 0 or +-1/4); the uniform strain: the coupling's symbol for a
    # uniform B_1 is lim X/(e^{ip_1} - 1) = d F/d k_1 times the identity (a scalar); U_(111) leaves F unchanged
    g8 = 2 * np.pi * np.arange(8) / 8
    K1, K2, K3 = np.meshgrid(g8, g8, g8, indexing='ij')
    Fn = np.cos(2 * K1) * np.cos(2 * K2) + np.cos(2 * K1) * np.cos(2 * K3) + np.cos(2 * K2) * np.cos(2 * K3)
    co = np.fft.fftn(Fn) / 512
    mm = [tuple(((i + 4) % 8) - 4 for i in ix) for ix in zip(*np.nonzero(np.abs(co) > 1e-9))]
    reach = max(sum(abs(x) for x in m) for m in mm)
    pp = sp.Symbol('p', real=True)
    Xp = sp.I * (F.subs(k[0], k[0] + pp) - F)
    sym_uniform = sp.simplify(sp.limit(Xp / (sp.exp(sp.I * pp) - 1), pp, 0) - sp.diff(F, k[0]))
    uniform_scalar = sym_uniform == 0 and reach == 4
    u111 = sp.simplify(sub(F, {k[0]: k[0] + sp.pi, k[1]: k[1] + sp.pi, k[2]: k[2] + sp.pi}) - F) == 0
    ok = inv and f != 0 and same_e1 and nonzero_N and not_conserved_24 and u111 and uniform_scalar
    rep("D5 a coupling with an exact current and no local generator", ok,
        f"F = e_2(cos 2k_1, cos 2k_2, cos 2k_3) is unchanged by the 384 symmetries and is not a function of |s|^2: at the 24^3 pair "
        f"e_1 agrees and F differs by {f}; X = i[F, xi] (hops of four steps) has kernel i(F(k+p) - F(k)); on every 2q torus F is constant "
        f"on the walk's eigenspaces, so every stationary expectation of X vanishes; at the pair (Delta = 0) Phi(X) != 0, so no local G; on "
        f"24^3 its same-energy block there is nonzero (not conserved); for a uniform strain it adds B.grad F times 1 (no lengths); "
        f"F(k + pi(1,1,1)) = F(k), so U_(111) does not reverse it: demands 2 and 3 fail")


# ---------------------------------------------------------------- D6
def herm(prefix):
    a0, a1, a2, a3 = sp.symbols(prefix + '0:4', real=True)
    return a0 * I2 + a1 * SIG[0] + a2 * SIG[1] + a3 * SIG[2], (a1, a2, a3)


def D6():
    k = sp.symbols('k1:4', real=True); q = sp.symbols('q1:4', real=True); eps = sp.Symbol('epsilon')
    al = [herm(f'al{b}_') for b in range(3)]
    be = [herm(f'be{b}_') for b in range(3)]
    dH = sum((al[b][0] * sp.cos(k[b]) + be[b][0] * sp.sin(k[b]) for b in range(3)), sp.zeros(2, 2))
    # (i) one-step hops are reversed by U_(111): dH(k + pi(1,1,1)) = -dH(k); a two-step term is not
    shift = {k[a]: k[a] + sp.pi for a in range(3)}
    ok_rev = zero((dH.subs(shift) + dH).applyfunc(sp.simplify))
    two = sp.cos(k[0] + k[1]) * SIG[2]
    ok_two = zero((two.subs(shift) - two).applyfunc(sp.simplify))
    # (ii) near pi n the sigma part of H + eps dH is sigma_a M_ab q_b + ... with M = (1 + eps betatilde) D_n
    bt = sp.Matrix(3, 3, lambda a, b: be[b][1][a])
    ok_M = True
    Htot = sdot([sp.sin(k[a]) for a in range(3)]) + eps * dH
    for n in itertools.product((0, 1), repeat=3):
        Dn = sp.diag(*[(-1)**x for x in n])
        pt = {k[a]: sp.pi * n[a] + q[a] for a in range(3)}
        comp = [sp.expand_trig(((Htot * SIG[a]).trace() / 2).subs(pt)) for a in range(3)]
        Msig = sp.Matrix(3, 3, lambda a, b: sp.simplify(sp.diff(comp[a], q[b]).subs({x: 0 for x in q})))
        ok_M = ok_M and sp.simplify(Msig - (sp.eye(3) + eps * bt) * Dn) == sp.zeros(3, 3)
    # (iii) the first-order metric D_n (bt + bt^T) D_n: off-diagonal entries flip sign for a species reflected along one of the two axes
    g1 = bt + bt.T
    flips = all(((sp.diag(1, -1, 1) * g1 * sp.diag(1, -1, 1))[0, 1] + g1[0, 1]) == 0 for _ in [0])
    rep("D6 no coupling of reach two meets demands 2 and 3", ok_rev and ok_two and ok_M and flips,
        "U_(111) multiplies a hop of m steps by (-1)^m, so the reversal of the coupled walk needs every hop odd, and at reach <= 2 every hop "
        "one step (a two-step term like cos(k_1 + k_2) sigma_3 is not reversed); a one-step symbol sum_b (alpha_b cos k_b + beta_b sin k_b) "
        "(general hermitian alpha, beta, symbolic) gives near every zero pi n the sigma part (1 + eps betatilde) D_n (checked for all "
        "eight n), betatilde_ab = the sigma_a part of beta_b; so species n sees D_n (1 + betatilde)^T (1 + betatilde) D_n, whose shear "
        "entries change sign for the species reflected along one of the two axes: (1 + B)^T (1 + B) for all eight only without shear")


# ---------------------------------------------------------------- D7
def D7():
    k = sp.symbols('k1:4', real=True); q = sp.symbols('q1:4', real=True)
    B = sp.Matrix(3, 3, sp.symbols('B0:9'))
    s = [sp.sin(x) for x in k]; c = [sp.cos(x) for x in k]

    def coupled(M):
        # uniform strain: sum_{a,j} B_aj (1/2){sigma_a C_a, M_j}; symbols commute here, so it is sum B_aj sigma_a c_a M_j
        return sdot(s) + sum((B[a, j] * SIG[a] * c[a] * M[j] for a in range(3) for j in range(3)), sp.zeros(2, 2))

    res = {}
    for name, M in (("reach two (M_j = sin k_j)", s), ("reach three (M_j = sin 2k_j / 2)", [sp.sin(2 * x) / 2 for x in k])):
        Ht = coupled(M)
        shift = {k[a]: k[a] + sp.pi for a in range(3)}
        reversed_ = zero((Ht.subs(shift) + Ht).applyfunc(sp.simplify))
        geos = []
        for n in itertools.product((0, 1), repeat=3):
            Dn = sp.diag(*[(-1)**x for x in n])
            pt = {k[a]: sp.pi * n[a] + q[a] for a in range(3)}
            Msig = sp.Matrix(3, 3, lambda a, b: sp.diff(sp.expand_trig((Ht.subs(pt) * SIG[a]).trace() / 2), q[b]).subs({x: 0 for x in q}))
            geos.append(sp.simplify(Msig.T * Msig))
        same = all(sp.simplify(g - geos[0]) == sp.zeros(3, 3) for g in geos)
        res[name] = (reversed_, same)
    ok = res["reach two (M_j = sin k_j)"] == (False, False) and res["reach three (M_j = sin 2k_j / 2)"] == (True, True)
    rep("D7 the ladder against demands 2 and 3", ok,
        "uniform strain, exact symbols: block 63's coupling (M_j = sin k_j, hops of 0 and 2 steps) is not reversed by U_(111) and shows the "
        "species (1 + BD)^T (1 + BD); block 69's (M_j = (1/2) sin 2k_j, hops of 1 and 3 steps) is reversed and shows all eight (1 + B)^T "
        "(1 + B); so demands 2 and 3 together are met at reach three and, by D6, at no smaller reach")


# ---------------------------------------------------------------- D8
def D8():
    L = 3
    sites = list(itertools.product(range(L), repeat=3))
    idx = {x: i for i, x in enumerate(sites)}
    nb = len(sites)
    add = lambda x, a: tuple((x[i] + (1 if i == a else 0)) % L for i in range(3))
    grad = sp.zeros(3 * nb, nb)                         # (d_a xi)(x) = xi(x + e_a) - xi(x)
    for x in sites:
        for a in range(3):
            grad[3 * idx[x] + a, idx[add(x, a)]] += 1
            grad[3 * idx[x] + a, idx[x]] -= 1
    curl = sp.zeros(3 * nb, 3 * nb)                     # plaquette (x; a < b): B_a(x) + B_b(x + e_a) - B_a(x + e_b) - B_b(x)
    for x in sites:
        for pi_, (a, b) in enumerate(((0, 1), (0, 2), (1, 2))):
            row = 3 * idx[x] + pi_
            curl[row, 3 * idx[x] + a] += 1
            curl[row, 3 * idx[add(x, a)] + b] += 1
            curl[row, 3 * idx[add(x, b)] + a] -= 1
            curl[row, 3 * idx[x] + b] -= 1
    ok1 = (curl * grad) == sp.zeros(3 * nb, nb)
    uniform = sp.Matrix([[sp.Symbol(f'u{a}')] for _ in sites for a in range(3)])
    ok2 = sp.simplify(curl * uniform) == sp.zeros(3 * nb, 1)
    # a curl coupling dH[B] = sum_rows (curl B)_row V_row has response R = curl^T <V>; its divergence grad^T R = (curl grad)^T <V> = 0
    ok3 = (grad.T * curl.T) == sp.zeros(nb, 3 * nb)
    rep("D8 couplings through the curls alone", ok1 and ok2 and ok3,
        f"on the 3^3 torus (exact integer matrices, {3 * nb} plaquettes): curl(d xi) = 0, curl(uniform) = 0, and grad^T curl^T = 0; so a "
        "coupling through the curls vanishes on every gradient (dH[d xi] = 0: the relabelling Ward identity and with it block 72's "
        "requirement are unchanged by adding it), its response is divergence-free in every state, and it makes no lengths for uniform "
        "strains")


# ---------------------------------------------------------------- D9
def D9():
    rows = []
    ok = True
    for fn in sorted(os.listdir(HERE)):
        if fn.startswith("search_") and fn.endswith(".txt"):
            txt = open(os.path.join(HERE, fn)).read()
            m = re.search(r"window (\d+), hops (\w+): (\d+) unknowns", txt)
            d = re.search(r"solution space dimension: (\d+)", txt)
            u = re.search(r"U\(1\) residual ([0-9.e+-]+)", txt)
            fam = re.search(r"family i\[H, zeta\]: rank (\d+); its residual outside the solution space ([0-9.e+-]+)", txt)
            eq = re.search(r"solution space equals the family: (\w+)", txt)
            if not (m and d):
                continue
            if fam and eq:
                rows.append(f"window {m.group(1)} ({m.group(3)} unknowns): dimension {d.group(1)} = rank of the family i[H, zeta] "
                            f"({fam.group(1)}), family inside to {float(fam.group(2)):.0e}")
                ok = ok and eq.group(1) == "True"
            else:
                rows.append(f"window {m.group(1)}, hops {m.group(2)} ({m.group(3)} unknowns): dimension {d.group(1)}, the U(1) coupling "
                            f"(residual {float(u.group(1)):.0e})" if u else f"window {m.group(1)}: dimension {d.group(1)}")
                ok = ok and d.group(1) == "1" and u is not None and float(u.group(1)) < 1e-10
    ok = ok and len(rows) >= 3
    rep("D9 nearest-neighbour couplings with an exact current (executed)", ok,
        "null space of (C0) X(k,0) = 0, (C1) Phi(X) = 0 on the 384 symmetry families, (C2) X = 0 between zeros (singular values, "
        "tolerance 1e-9): " + "; ".join(rows) + ": every one is i[H, zeta] with zeta an on-site coin field linear in xi (local "
        "generator; zeta = c xi in the smallest window); covariance forces zeta's uniform part to vanish, and then a uniform strain only "
        "turns the coin (no lengths)")


def D10():
    """a second route to (d) (the species average; the statement is attempt a2's, the derivation here is independent):
    for any symbol of reach <= 2 the eight species' first-order shear metrics average to zero; at reach three they need not"""
    ms2 = [m for m in itertools.product(range(-2, 3), repeat=3) if 0 < sum(abs(x) for x in m) <= 2]
    avg_zero = True
    for a, c in ((0, 1), (0, 2), (1, 2)):
        tot = 0
        for n in itertools.product((0, 1), repeat=3):
            Da, Dc = (-1)**n[a], (-1)**n[c]
            # first-order metric entry (a, c): D_a dM[a][c] + D_c dM[c][a], dM[a][b] = sum_m A_m^a (i m_b) (-1)^{n.m}
            for m in ms2:
                sgn = (-1)**sum(x * y for x, y in zip(n, m))
                tot += Da * sp.Symbol(f"A{m}_{a}") * sp.I * m[c] * sgn + Dc * sp.Symbol(f"A{m}_{c}") * sp.I * m[a] * sgn
        avg_zero = avg_zero and sp.expand(tot) == 0
    # reach three: the term sigma_1 cos k_1 sin 2k_2 (block 69's kind) gives the same shear to all eight
    k = sp.symbols('k1:4', real=True); q = sp.symbols('q1:4', real=True)
    term = sp.cos(k[0]) * sp.sin(2 * k[1]) / 2
    same = set()
    for n in itertools.product((0, 1), repeat=3):
        pt = {k[x]: sp.pi * n[x] + q[x] for x in range(3)}
        dM = sp.diff(sp.expand_trig(term.subs(pt)), q[1]).subs({x: 0 for x in q})
        same.add(sp.simplify((-1)**n[0] * dM))
    rep("D10 the species average (second route to (d))", avg_zero and same == {1},
        "for a general symbol of reach <= 2 (all 24 monomials, symbolic coin parts), the first-order shear metric entry (a, c), a != c, "
        "summed over the eight species vanishes identically: the monomials that survive the average are m = +-e_a, which carry no "
        "component along e_c; so equal shear for all species forces zero shear, without demand 3; the reach-three term sigma_1 cos k_1 "
        "(1/2) sin 2k_2 gives every species the same shear, D_1 d/dq_2 = 1")


def main():
    D1(); D2(); D3(); D4(); D5(); D6(); D7(); D8(); D9(); D10()
    print(f"TOTAL: PASS={NP} FAIL={NF}")
    if NF == 0:
        print("SUMMARY: PROVED no coupling of reach <= 2, of any kind, meets demands 2 and 3: the energy reversal by U_(111) "
              "forces one-step hops, and species n then sees D_n (1 + b)^T (1 + b) D_n, the shear reversed for six species; the species "
              "average (attempt a2's statement, re-derived) removes demand 3; block 69 meets both at reach three, the least among all "
              "couplings. (a) G = -i(H'X + XH)/(|s(k+p)|^2 - |s(k)|^2): local on Z^3 with nothing assumed (division in z_3, Gauss) and "
              "at the species momenta (Koszul); on 2q tori the hypothesis is weaker: i[e_2(cos 2k), xi] has an exact current there and no "
              "local generator; nearest-neighbour exact currents are i[H, zeta] (executed). The task's HIT condition is refuted: no HIT")
    else:
        print(f"SUMMARY: ROUTE FAILS AT {NF} check(s) above")


if __name__ == "__main__":
    main()
