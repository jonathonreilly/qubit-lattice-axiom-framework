#!/usr/bin/env python3
"""C10 exact runner (sympy): identities behind the burn-and-turn vs metric-coupling comparison on the
C7 two-qubit walk. General b = (b0,b1,b2) symbolic unless a named point is substituted.

E1  BT algebra: burns + turns = eps m m for ANY normalised weights (so only m = v matters).
E2  Clifford band: on the upper band of U = f + i x.Gamma, <Gamma_A> = -x_A/|x|  =>  <alpha_i> = g_i/|x|.
E3  Massless member: D = -grad f satisfies D_1 - s g_1 = sin k1 [-3 beta (x2+x3) + C x2 x3], x_a = 1 - cos k_a,
    beta = -s(b0-b1-2b2)/3 (C7/parent k^4 anisotropy), C = -3b0b1+2b0b2-3b1^2+7b1b2+5b2^2.
E4  Massive member U_theta = M U0 M: g unchanged, f_theta = cos(th) f0 - sin(th) hhat.h0, and
    D_theta,1 - lam s g_1 = sin k1 [E1 (x2+x3) + E2 x2 x3], lam = cos th - sin th (hhat.W)/s^2.
E5  Consequences at the named points (beta, C exact algebraic) and the O(a^2) mismatch tensors of M1..M4
    (massless, exact in b along a generic direction).
E6  E-W rest clock: sum_n |n|^2 w_n at k = 0 equals 3 s^2 - 3 i hhat.W for every theta.
"""
from __future__ import annotations
import sympy as sp

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


b0, b1, b2 = sp.symbols('b0 b1 b2', real=True)
k1, k2, k3 = K = sp.symbols('k1 k2 k3', real=True)
s = b0 + 2 * b1 + b2
G = sp.Matrix([[1 - 3 * b0**2, -2 * b0 * b1, b1**2 - b0**2 - b0 * b2, -3 * b1 * (b0 - b2)],
               [-2 * b0 * b1, b0**2 - 2 * b1**2, b1 * (b0 - b2), b0 * b2 - b1**2 + b2**2],
               [b1**2 - b0**2 - b0 * b2, b1 * (b0 - b2), 2 * b1**2 - b2**2, 2 * b1 * b2],
               [-3 * b1 * (b0 - b2), b0 * b2 - b1**2 + b2**2, 2 * b1 * b2, 3 * b2**2]])
c = [sp.cos(x) for x in K]; sn = [sp.sin(x) for x in K]
phi = sp.Matrix([1, sum(c), c[0] * c[1] + c[0] * c[2] + c[1] * c[2], c[0] * c[1] * c[2]])
phi0 = sp.Matrix([1, 3, 3, 1]); wv = sp.Matrix([0, 1, 2, 1])
f0 = sp.expand((G * phi0).dot(phi))
g = [sn[a] * (b0 + b1 * (c[(a + 1) % 3] + c[(a + 2) % 3]) + b2 * c[(a + 1) % 3] * c[(a + 2) % 3]) for a in range(3)]
beta = -s * (b0 - b1 - 2 * b2) / 3
Cc = -3 * b0 * b1 + 2 * b0 * b2 - 3 * b1**2 + 7 * b1 * b2 + 5 * b2**2
x2, x3 = 1 - c[1], 1 - c[2]


def main():
    # ---------------- E1
    n = 5
    P = sp.symbols(f'P0:{n}'); dv = [sp.Matrix(sp.symbols(f'd{i}x d{i}y d{i}z')) for i in range(n)]
    Ps = sum(P)
    m = sum((P[i] * dv[i] for i in range(n)), sp.zeros(3, 1)) / Ps
    burn = sum((P[i] * dv[i] * dv[i].T for i in range(n)), sp.zeros(3, 3)) / Ps
    turn = sp.zeros(3, 3)
    for i in range(n):
        for j in range(n):
            if i != j:
                dd = dv[j] - dv[i]; turn -= 2 * P[i] * P[j] / Ps**2 * dd * dd.T / 4
    res = sp.simplify(sp.expand((burn + turn - m * m.T) * Ps**2))
    check('E1: burns + turns = eps m m for arbitrary (complex) weights, 5 arbitrary step vectors in 3D', res == sp.zeros(3, 3))
    act = sum(2 * P[i] * P[j] / Ps**2 * (dv[j] - dv[i]).dot(dv[j] - dv[i]) / 4 for i in range(n) for j in range(n) if i != j)
    n2 = sum(P[i] * dv[i].dot(dv[i]) for i in range(n)) / Ps
    check('E1b: turn action = eps(<|d|^2> - m.m) for arbitrary weights', sp.simplify(sp.expand((act - n2 + m.dot(m)) * Ps**2)) == 0)
    # ---------------- E2 Clifford band expectation
    t1 = sp.Matrix([[0, 1], [1, 0]]); t2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); t3 = sp.Matrix([[1, 0], [0, -1]]); one = sp.eye(2)
    kr = lambda A, B: sp.Matrix(sp.BlockMatrix([[A[i, j] * B for j in range(2)] for i in range(2)]).as_explicit())
    Gam = [kr(t1, one), kr(t2, one), kr(t3, t1), kr(t3, t2), kr(t3, t3)]
    xs = sp.symbols('y1:6', real=True); X = sum((xs[i] * Gam[i] for i in range(5)), sp.zeros(4, 4)); nx = sp.sqrt(sum(v**2 for v in xs))
    Pi = (sp.eye(4) - X / nx) / 2
    okP = sp.simplify(Pi * Pi - Pi) == sp.zeros(4, 4) and sp.simplify(Pi.trace()) == 2
    U = sp.Symbol('f') * sp.eye(4) + sp.I * X
    ok_ev = sp.simplify((U * Pi - (sp.Symbol('f') - sp.I * nx) * Pi)) == sp.zeros(4, 4)
    exps = [sp.simplify((Pi * Gam[A]).trace() / 2 + xs[A] / nx) for A in range(5)]
    check('E2: Pi = (1 - X/|x|)/2 is the rank-2 band of U with eigenvalue f - i|x| = exp(-i omega); '
          'band-averaged <Gamma_A> = -x_A/|x|', okP and ok_ev and all(e == 0 for e in exps))
    # every vector, not only the average: Pi Gamma_A Pi = -(x_A/|x|) Pi  (anticommutation)
    okall = all(sp.simplify(Pi * Gam[A] * Pi + xs[A] / nx * Pi) == sp.zeros(4, 4) for A in range(5))
    check('E2b: Pi Gamma_A Pi = -(x_A/|x|) Pi, so <alpha_i> = g_i/|x| for every vector of the degenerate band', okall)
    # ---------------- E3 massless D - s g
    D1 = -sp.diff(f0, k1)
    r = sp.expand(D1 - s * g[0] - sn[0] * (-3 * beta * (x2 + x3) + Cc * x2 * x3))
    check('E3: D_1 - s g_1 = sin k1 [-3 beta (x2+x3) + C x2 x3] exactly, all b (D = -grad f, massless member)', sp.simplify(r) == 0)
    # axis identity and continuum: D = s^2 k + O(k^3), g = s k + O(k^3)
    kap = sp.Symbol('kappa'); nn = sp.symbols('n1:4', real=True)
    sub = {k1: kap * nn[0], k2: kap * nn[1], k3: kap * nn[2]}
    Dser = sp.series(D1.subs(sub), kap, 0, 2).removeO(); gser = sp.series(g[0].subs(sub), kap, 0, 2).removeO()
    check('E3b: continuum order D = s^2 k, g = s k  (so T^BT,W -> s^2 T^M1 at continuum order)',
          sp.simplify(Dser - s**2 * kap * nn[0]) == 0 and sp.simplify(gser - s * kap * nn[0]) == 0)
    # ---------------- E4 massive
    th = sp.Symbol('theta', real=True); cv = sp.symbols('c0:4', real=True)   # hhat.C row (C = h rows of F)
    hW = cv[1] + 2 * cv[2] + cv[3]                                           # hhat.W = hhat.C w
    cons = {cv[0]: -(3 * cv[1] + 3 * cv[2] + cv[3])}                          # C phi0 = 0 (massless h(0) = 0)
    hh0 = sum(cv[i] * phi[i] for i in range(4)).subs(cons)
    fth = sp.cos(th) * f0 - sp.sin(th) * hh0
    Dth = -sp.diff(fth, k1)
    lam = sp.cos(th) - sp.sin(th) * hW / s**2
    E1c = -3 * beta * sp.cos(th) + sp.sin(th) * (cv[2] + cv[3]) - sp.sin(th) * hW * (b1 + b2) / s
    E2c = sp.cos(th) * Cc - sp.sin(th) * cv[3] + sp.sin(th) * hW * b2 / s
    r4 = sp.expand((Dth - lam * s * g[0] - sn[0] * (E1c * (x2 + x3) + E2c * x2 * x3)) * s)
    check('E4: D_theta,1 - lam s g_1 = sin k1 [E1 (x2+x3) + E2 x2 x3] exactly (all b, theta, mass direction)', sp.simplify(r4) == 0,
          'lam = cos th - sin th (hhat.W)/s^2; E1 = -3 beta cos th + sin th (c2 + c3 - (hhat.W)(b1+b2)/s); '
          'E2 = C cos th - sin th (c3 - (hhat.W) b2/s)')
    # g unchanged by the mass: M (i tau3 g.sigma) M = i tau3 g.sigma since tau3 anticommutes with hhat.tau
    hp = sp.Symbol('p', real=True); hv = (sp.cos(hp), sp.sin(hp))
    Mh = (sp.cos(th / 2) * sp.eye(4) + sp.I * sp.sin(th / 2) * (hv[0] * Gam[0] + hv[1] * Gam[1]))
    okg = all(sp.simplify(Mh * Gam[2 + a] * Mh - Gam[2 + a]) == sp.zeros(4, 4) for a in range(3))
    check('E4b: M Gamma_{3,4,5} M = Gamma_{3,4,5} (the spin part g is mass-independent)', okg)
    # ---------------- E5 named points
    r5, r6, r15 = sp.sqrt(5), sp.sqrt(6), sp.sqrt(15)
    iso = {b0: (r6 + 2 * r15) / 27, b1: (5 * r6 - 2 * r15) / 27, b2: (2 * r15 - 2 * r6) / 27}
    gold = {b0: (9 * r5 - 5) / 38, b1: (5 * r5 - 7) / 19, b2: (71 - 29 * r5) / 38}
    ustar_poly = [259200000000, -453744000000, 12644840000, 1185396800, -39225499]
    u = sp.Symbol('u'); ust = min(r for r in sp.Poly(ustar_poly, u).nroots(n=40) if r.is_real and r > 0)
    bst = {b0: sp.Rational(11, 30), b1: sp.sqrt(ust), b2: sp.Rational(3, 20)}
    vals = {nm: (sp.nsimplify(sp.simplify(beta.subs(p))) if nm != 'bstar' else sp.N(beta.subs(p), 12),
                 sp.simplify(Cc.subs(p)) if nm != 'bstar' else sp.N(Cc.subs(p), 12), sp.simplify(s.subs(p)) if nm != 'bstar' else sp.N(s.subs(p), 12))
            for nm, p in (('bstar', bst), ('iso', iso), ('gold', gold))}
    for nm, (bb, cc, ss) in vals.items():
        print(f'   {nm}: s = {ss} ({sp.N(ss, 8)}), beta = {bb} ({sp.N(bb, 8)}), C = {cc} ({sp.N(cc, 8)})')
    check('E5: beta(b_iso) = 0 exactly; C(b_iso) = -3(2b1-3b2)(b1+b2) != 0; beta(b_gold) = 7/6 - sqrt5/2; beta(b*) != 0',
          sp.simplify(beta.subs(iso)) == 0 and abs(sp.N(Cc.subs(iso))) > 1e-3 and sp.simplify(beta.subs(gold) - (sp.Rational(7, 6) - r5 / 2)) == 0
          and abs(vals['bstar'][0]) > 1e-2 and sp.simplify((Cc + 3 * (2 * b1 - 3 * b2) * (b1 + b2)).subs(b0, b1 + 2 * b2)) == 0)
    # O(a^2) mismatch tensors (massless), direction n symbolic, exact in b
    # T^X sin^2(om)/om:  BT/s^2 -> D D / s^2 ; M1 -> g g ; M2 -> g g q ; M3 -> s sym(g, sin k) q ; M4 -> sym(D, sin k) q,
    # q = sin(om)/om = 1 - om^2/6 + ...,  om^2 = s^2 kappa^2 |n|^2 + O(kappa^4)
    Dv = [(-sp.diff(f0, x)).subs(sub) for x in K]; gv = [gi.subs(sub) for gi in g]; sk = [sp.sin(kap * ni) for ni in nn]
    q = 1 - s**2 * kap**2 * sum(ni**2 for ni in nn) / 6
    ser = lambda e: sp.expand(sp.series(sp.expand(e), kap, 0, 5).removeO())
    def tens(X, i, j):
        if X == 'BT': return Dv[i] * Dv[j] / s**2
        if X == 'M1': return gv[i] * gv[j]
        if X == 'M2': return gv[i] * gv[j] * q
        if X == 'M3': return s * (gv[i] * sk[j] + gv[j] * sk[i]) / 2 * q
        if X == 'M4': return (Dv[i] * sk[j] + Dv[j] * sk[i]) / 2 * q
    mis = {}
    for X in ('M1', 'M2', 'M3', 'M4'):
        mis[X] = {}
        for (i, j) in ((0, 0), (0, 1)):
            e = ser(tens(X, i, j) - tens('BT', i, j))
            mis[X][(i, j)] = (sp.factor(e.coeff(kap, 2)), sp.factor(e.coeff(kap, 4)))
    ok_c = all(sp.simplify(mis[X][ij][0]) == 0 for X in mis for ij in mis[X])
    check('E5b: at continuum order (kappa^2 in T sin^2/om) all four couplings equal T^BT,W/s^2 exactly (all b, all n)', ok_c)
    print('   O(a^2) mismatch, coefficient of kappa^4 in (T^X - T^BT/s^2) sin^2(om)/om, component xx and xy:')
    for X in mis:
        for ij in mis[X]:
            print(f'     {X} {ij}: {mis[X][ij][1]}')
    m1 = [sp.simplify(mis['M1'][ij][1] / beta) for ij in mis['M1']]
    check('E5c: the M1 O(a^2) mismatch is beta x (polynomial in n, s, b) [i.e. vanishes iff beta = 0 or k on an axis]',
          all(sp.simplify(mis['M1'][ij][1].subs(b0, b1 + 2 * b2)) == 0 for ij in mis['M1']) and
          all(sp.simplify(mis['M1'][ij][1].subs({nn[1]: 0, nn[2]: 0})) == 0 for ij in mis['M1']),
          f'xx: {sp.factor(mis["M1"][(0, 0)][1])}')
    # M2..M4 nonzero at each named point along (1,2,3)
    nz = {}
    for X in ('M2', 'M3', 'M4'):
        nz[X] = [abs(sp.N(mis[X][(0, 0)][1].subs({nn[0]: 1, nn[1]: 2, nn[2]: 3}).subs(p))) for p in (bst, iso, gold)]
    print('   |kappa^4 xx mismatch| along (1,2,3) at (b*, b_iso, b_gold): ' + '; '.join(f'{X}: ' + ', '.join(f'{float(v):.4e}' for v in nz[X]) for X in nz))
    m1n = [abs(sp.N(mis['M1'][(0, 0)][1].subs({nn[0]: 1, nn[1]: 2, nn[2]: 3}).subs(p))) for p in (bst, iso, gold)]
    print('   M1 same quantity: ' + ', '.join(f'{float(v):.4e}' for v in m1n))
    check('E5d: M2, M3, M4 mismatch T^BT,W/s^2 at O(a^2) at all three points (generic direction); M1 only at b*, b_gold',
          all(v > 1e-6 for X in nz for v in nz[X]) and m1n[0] > 1e-6 and m1n[1] < 1e-30 and m1n[2] > 1e-6)
    d111 = {X: sp.simplify(mis[X][(0, 1)][1].subs({nn[0]: 1, nn[1]: 1, nn[2]: 1}).subs(iso)) for X in ('M2', 'M3', 'M4')}
    d111xx = {X: sp.simplify(mis[X][(0, 0)][1].subs({nn[0]: 1, nn[1]: 1, nn[2]: 1}).subs(iso)) for X in ('M2', 'M3', 'M4')}
    check('E5e (non-generic): at b_iso along (111) the O(a^2) mismatch of M3 and M4 vanishes, that of M2 does not',
          d111['M3'] == 0 and d111['M4'] == 0 and d111xx['M3'] == 0 and d111xx['M4'] == 0 and d111xx['M2'] != 0, f'M2 xx: {d111xx["M2"]}')
    # b_iso: the h row orthogonal to W is proportional to (-1, 1, -1, 1), i.e. hperp.h0 = -c x1 x2 x3 = O(k^6)
    xprod = sp.expand(sum(v * phi[i] for i, v in enumerate((-1, 1, -1, 1))) + (1 - c[0]) * (1 - c[1]) * (1 - c[2]))
    check('E5f: (-1,1,-1,1).phi = -(1-c1)(1-c2)(1-c3) (used to explain the O(a^4) maximal-twist residual at b_iso; the row itself is numerical)', xprod == 0)
    # ---------------- E6 E-W rest clock
    # sum_n |n|^2 w_n = -exp(i om) <u| lap U |u>; at k = 0 the band vector satisfies hhat.tau u = -u (U(0) = exp(i th hhat.tau))
    lapf0 = sp.simplify(sum(sp.diff(f0, x, 2) for x in K).subs({k1: 0, k2: 0, k3: 0}))
    laph0 = sp.simplify(sum(sp.diff(hh0, x, 2) for x in K).subs({k1: 0, k2: 0, k3: 0}))
    # (f, hhat.h) rotate: f_th = c f0 - s hh0 ; hhat.h_th = s f0 + c hh0 ; <u|tau_j|u> = -hhat_j ; <u|tau3 sigma|u> part has lap g(0) = 0
    lapg0 = [sp.simplify(sum(sp.diff(gi, x, 2) for x in K).subs({k1: 0, k2: 0, k3: 0})) for gi in g]
    val = -sp.exp(sp.I * th) * ((sp.cos(th) * lapf0 - sp.sin(th) * laph0) - sp.I * (sp.sin(th) * lapf0 + sp.cos(th) * laph0))
    check('E6: E-W rest value sum_n |n|^2 w_n = 3 s^2 - 3 i hhat.W, independent of theta', all(v == 0 for v in lapg0) and
          sp.simplify(sp.expand(sp.expand_complex(sp.expand(val - (3 * s**2 - 3 * sp.I * hW))))) == 0, f'lap f0(0) = {sp.factor(lapf0)}, lap hhat.h0(0) = {sp.factor(laph0)}')
    print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')


if __name__ == '__main__':
    main()
