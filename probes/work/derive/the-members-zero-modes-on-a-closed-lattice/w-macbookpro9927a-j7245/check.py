#!/usr/bin/env python3
"""Exact checks for J:derive:the-members-zero-modes-on-a-closed-lattice:a1
(worker w-macbookpro9927a-j7245).  Independent re-derivation of blocks 146,
147 and 148 (open PRs #9237, #9240, #9241).  The Euler-Lagrange equations are
derived here by sympy from the homogeneous actions, not taken from the notes.
Every claimed solution is substituted into those equations.  All exact.
"""
import itertools
import time

import sympy as sp
from sympy.calculus.euler import euler_equations

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}")


t = sp.symbols('t', real=True)
al, be, K, mu, eps, m0, I_ = sp.symbols('alpha beta K mu epsilon m0 I', positive=True)

# ------------------------------------------------------------------ block 146
# (a) kinetic term on a uniform stretch h_ij = 2 lam delta_ij
lam = sp.Function('lam')(t)
Hd = sp.diag(*([2 * lam.diff(t)] * 3))
ck = sp.expand((al * (Hd * Hd).trace() + be * Hd.trace() ** 2) / lam.diff(t) ** 2)
okA1 = ck == 12 * al + 36 * be and ck.subs(be, -al) == -24 * al
# (b) EL equations of c_k e^{s lam} lamdot^2 / w - w m(lam), derived here
w = sp.Function('w')(t)
m = sp.Function('m')
c = sp.symbols('c_k')
L146 = c * sp.exp(3 * lam) * lam.diff(t) ** 2 / w - w * m(lam)
el = euler_equations(L146, [w, lam], t)
con = sp.simplify(el[0].lhs.subs(w, 1).doit())            # -c e^{3lam} lamdot^2 - m
leq = sp.simplify(el[1].lhs.subs(w, 1).doit())
# the constraint's time derivative is a multiple of the length's equation, for any m(lam)
dcon = sp.diff(con, t)
ratio = sp.simplify(dcon / leq)
okA2 = sp.simplify(dcon - ratio * leq) == 0 and sp.simplify(ratio - lam.diff(t)).free_symbols == set() or \
    sp.simplify(dcon + lam.diff(t) * leq) == 0 or sp.simplify(dcon - lam.diff(t) * leq) == 0
# (c) the coupling: u = -e/(4K p^2) -> -m/(16 pi K r); the Friedmann form iff alpha = K/4
p, r = sp.symbols('p r', positive=True)
green = sp.integrate(sp.sin(p * r) / p, (p, 0, sp.oo)) / (2 * sp.pi ** 2 * r)   # int e^{ipr}/p^2 d^3p/(2pi)^3
G = sp.simplify(1 / (4 * K) * green * r * 1)       # |u| r / m
okA3 = sp.simplify(green - 1 / (4 * sp.pi * r)) == 0 and sp.simplify(G - 1 / (16 * sp.pi * K)) == 0
rho = sp.symbols('rho', positive=True)
sol_alpha = sp.solve(sp.Eq(rho / (24 * al), 8 * sp.pi * G / 3 * rho), al)
okA3 = okA3 and sol_alpha == [K / 4]
# (d) lddot/l = -(rho + 3p)/(48 alpha) at c_k = -24 alpha, with dm/dlam = -3 p l^3
pr = sp.symbols('p_pr')
ld, ldd, lv = sp.symbols('ld ldd lv')
subsd = {lam.diff(t, 2): ldd, lam.diff(t): ld, lam: lv}
con_s = con.subs(c, -24 * al).subs(subsd)
leq_s = leq.subs(c, -24 * al).subs(subsd)
mval = sp.symbols('mval')
leq_s = leq_s.subs(sp.Subs(sp.Derivative(m(lam), lam), lam, lv), sp.Symbol('dm')).subs(
    sp.Derivative(m(lv), lv), sp.Symbol('dm')).subs(m(lv), mval)
con_s = con_s.subs(m(lv), mval)
dm = sp.Symbol('dm')
sol = sp.solve([con_s, leq_s.subs(dm, -3 * pr * sp.exp(3 * lv))], [mval, ldd], dict=True)[0]
accel = sp.simplify(sol[ldd] + ld ** 2)
rho_expr = sol[mval] / sp.exp(3 * lv)
okA4 = sp.simplify(accel + (rho_expr + 3 * pr) / (48 * al)) == 0
okA4 = okA4 and sp.simplify((1 / (48 * al)).subs(al, K / 4) - 4 * sp.pi * (1 / (16 * sp.pi * K)) / 3) == 0
check("A1", okA1 and okA2 and okA3 and okA4,
      "block 146: c_k = 12 alpha + 36 beta = -24 alpha on h = 2 lam delta; EL of c_k l^3 lamdot^2/w - w m derived: "
      "the constraint's rate is lamdot times the length's equation for every m(lam); int e^{ipr}/p^2 = 1/(4 pi r) "
      "gives G = 1/(16 pi K); rho/(24 alpha) = (8 pi G/3) rho iff alpha = K/4; lddot/l = -(rho + 3p)/(48 alpha) "
      "= -(4 pi G/3)(rho + 3p) at alpha = K/4")


def check_solution(mfun, lsol):
    """substitute l(t) into the constraint and the length's equation at c_k = -24 alpha, w = 1"""
    out = []
    for e in (con.subs(c, -24 * al), leq.subs(c, -24 * al)):
        e = e.subs(m(lam), mfun(lam))
        e = e.replace(lambda z: isinstance(z, sp.Subs), lambda z: z.doit()).doit()
        e = e.subs(lam, sp.log(lsol)).doit()
        out.append(sp.simplify(e) == 0)
    return all(out)


t1 = sp.sqrt(6 * al / eps)
t0 = sp.Rational(4, 3) * sp.sqrt(6 * al / m0)
okA5 = (check_solution(lambda x: eps * sp.exp(-x), (1 + t / t1) ** sp.Rational(1, 2))
        and check_solution(lambda x: m0 + 0 * x, (1 + t / t0) ** sp.Rational(2, 3)))
# pressure: dm/dlam = -3 p l^3 -> p = rho/3 for m = eps/l; mixture: only the top-speed part
xx = sp.symbols('x')
p_top = sp.simplify(-sp.diff(eps * sp.exp(-xx), xx) / (3 * sp.exp(3 * xx)))
p_mix = sp.simplify(-sp.diff(m0 + eps * sp.exp(-xx), xx) / (3 * sp.exp(3 * xx)))
okA5 = okA5 and sp.simplify(p_top - eps * sp.exp(-xx) / sp.exp(3 * xx) / 3) == 0 and sp.simplify(p_mix - p_top) == 0
# the walk on a stretched lattice commutes with itself at all times: H(k)/l(t)
kk = sp.symbols('k1:4', real=True)
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
hk = sum((sp.sin(kk[a]) * SIG[a] for a in range(3)), sp.zeros(2))
l1, l2 = sp.symbols('l1 l2', positive=True)
okA5 = okA5 and (hk / l1 * hk / l2 - hk / l2 * hk / l1).applyfunc(sp.expand) == sp.zeros(2)
check("A2", okA5, "block 146 T3: l = (1 + t/t1)^(1/2), t1 = sqrt(6 alpha/eps), solves constraint and length's equation "
      "for m = eps/l; l = (1 + t/t0)^(2/3), t0 = (4/3) sqrt(6 alpha/m0), for rest content; p = rho/3 for m = eps/l; "
      "a mixture's pressure is its top-speed part's; H(k)/l(t) commutes at all times")

# ------------------------------------------------------------------ block 147
# (a) I on the 4^3 torus by counting components with sin^2 = 1
cnt = {n: 0 for n in range(4)}
for kv in itertools.product(range(4), repeat=3):
    cnt[sum(1 for j in kv if j % 2 == 1)] += 1
I4 = sum(cnt[n] * sp.sqrt(n) for n in cnt) / 64
okB1 = sp.simplify(I4 - (3 + sp.sqrt(3) + 3 * sp.sqrt(2)) / 8) == 0
# (b) staggered mass, from position space on the 4^3 torus: H^2 = (sum S_a^2)/l^2 + mu^2 exactly
Lt = 4
sites = list(itertools.product(range(Lt), repeat=3))
ix = {x: i for i, x in enumerate(sites)}
Nn = len(sites)
lval, muval = sp.Rational(3, 2), sp.Rational(2, 5)
Hm = sp.zeros(2 * Nn, 2 * Nn)
SS = sp.zeros(Nn, Nn)
for x in sites:
    i = ix[x]
    stag = (-1) ** (sum(x) % 2)
    Hm[2 * i, 2 * i] += muval * stag
    Hm[2 * i + 1, 2 * i + 1] += muval * stag
for a in range(3):
    S = sp.zeros(Nn, Nn)
    for x in sites:
        y = list(x); y[a] = (y[a] + 1) % Lt; y = tuple(y)
        # S_a = (T_a - T_a^{-1})/(2i)
        S[ix[x], ix[y]] += sp.Rational(1, 2) / sp.I
        S[ix[y], ix[x]] -= sp.Rational(1, 2) / sp.I
    SS += S * S
    Hm += sp.kronecker_product(S, SIG[a]) / lval
okB2 = (Hm * Hm - sp.kronecker_product(SS, sp.eye(2)) / lval ** 2 - muval ** 2 * sp.eye(2 * Nn)).applyfunc(
    sp.expand) == sp.zeros(2 * Nn, 2 * Nn)
# (c) pressure ratio of a massive mode and the bounce
y = sp.symbols('y', positive=True)
Em = sp.sqrt(mu ** 2 + y * sp.exp(-2 * xx))          # y = s^2, l = e^x
pm = -sp.diff(-Em, xx) / (3 * sp.exp(3 * xx))        # sea mode energy is -Em
ratio = sp.simplify(pm / (-Em / sp.exp(3 * xx)))
ym = y * sp.exp(-2 * xx)
okB3 = sp.simplify(ratio - ym / (3 * (mu ** 2 + ym))) == 0
# bounce with m = m0 - I/l: EL at lamdot = 0, l = I/m0
cb = con.subs(c, -24 * al).subs(m(lam), m0 - I_ * sp.exp(-lam))
lb = leq.subs(c, -24 * al).subs(m(lam), m0 - I_ * sp.exp(-lam)).doit()
lamb = sp.log(I_ / m0)
lddot_b = sp.solve(lb.subs({lam.diff(t, 2): ldd, lam.diff(t): 0, lam: lamb}), ldd)[0]
okB4 = sp.simplify(lddot_b - m0 ** 4 / (48 * al * I_ ** 3)) == 0 and sp.simplify(cb.subs(
    {lam.diff(t): 0, lam: lamb})) == 0
lv2 = sp.symbols('l', positive=True)
thist = sp.sqrt(24 * al) / m0 ** 2 * (sp.Rational(2, 3) * (m0 * lv2 - I_) ** sp.Rational(3, 2)
                                       + 2 * I_ * (m0 * lv2 - I_) ** sp.Rational(1, 2))
# dt/dl must equal 1/ldot with ldot^2 = l^2 lamdot^2 = l^2 (m0 - I/l)/(24 alpha l^3)
okB4 = okB4 and sp.simplify(sp.diff(thist, lv2) ** 2 - 24 * al * lv2 / (m0 - I_ / lv2)) == 0
# massive sea: each mode's sqrt(mu^2 + s^2/l^2) decreases with l
okB5 = sp.simplify(sp.diff(sp.sqrt(mu ** 2 + y / lv2 ** 2), lv2) + y / (lv2 ** 3 * sp.sqrt(mu ** 2 + y / lv2 ** 2))) == 0
check("B1", okB1 and okB2 and okB3 and okB4 and okB5,
      f"block 147: I(4^3) = sum_n C(3,n) sqrt(n)/8 = (3 + sqrt3 + 3 sqrt2)/8; from position space on the 4^3 torus "
      f"(l = 3/2, mu = 2/5) H^2 = (sum S_a^2)/l^2 + mu^2 exactly (staggered mass anticommutes with every hop); "
      f"p/rho = y/(3(mu^2 + y)) per massive mode; with m = m0 - I/l the turn at l = I/m0 has lamddot = "
      f"m0^4/(48 alpha I^3) > 0 and the stated history t(l) has (dt/dl)^2 = 24 alpha l/(m0 - I/l); "
      f"sqrt(mu^2 + s^2/l^2) falls with l")
# (d) hard-core: two records on a 4x2x2 torus, every compressed hop anticommutes with the product of site signs
dims = (4, 2, 2)
hs = list(itertools.product(*[range(d) for d in dims]))
hix = {x: i for i, x in enumerate(hs)}
states = [(x, cx, yv, cy) for x in hs for yv in hs if x != yv for cx in (0, 1) for cy in (0, 1)]
sidx = {s_: i for i, s_ in enumerate(states)}
sign = lambda x: (-1) ** (sum(x) % 2)
okB6 = True
nh = 0
for s_ in states:
    x, cx, yv, cy = s_
    for walker in (0, 1):
        pos = x if walker == 0 else yv
        oth = yv if walker == 0 else x
        for a in range(3):
            for sg in (1, -1):
                q_ = list(pos); q_[a] = (q_[a] + sg) % dims[a]; q_ = tuple(q_)
                if q_ == oth or q_ == pos:
                    continue          # one record per site; a hop onto itself (side 2) is excluded
                new = (q_, cx, yv, cy) if walker == 0 else (x, cx, q_, cy)
                nh += 1
                okB6 = okB6 and sign(new[0]) * sign(new[2]) == -sign(x) * sign(yv)
check("B2", okB6 and nh > 0, f"block 147 T1(d) on another torus (4x2x2, two records, {len(states)} states, {nh} hops "
      f"inside the one-record-per-site space): every hop flips the product of the occupied sites' signs, so the "
      f"compressed hopping anticommutes with it and its spectrum is symmetric about zero")

# ------------------------------------------------------------------ block 148
lam3 = [sp.Function(f'lam{i}')(t) for i in range(3)]
Hd3 = sp.diag(*[2 * x.diff(t) for x in lam3])
kin = sp.expand(al * (Hd3 * Hd3).trace() + be * Hd3.trace() ** 2)
sq = sum(x.diff(t) ** 2 for x in lam3)
cr = sum(lam3[i].diff(t) * lam3[j].diff(t) for i in range(3) for j in range(i + 1, 3))
okC1 = sp.expand(kin - (4 * (al + be) * sq + 8 * be * cr)) == 0 and sp.expand(kin.subs(be, -al) + 8 * al * cr) == 0
V = sp.exp(sum(lam3))
L148 = -8 * al * V * cr / w - w * m0
el3 = euler_equations(L148, [w] + lam3, t)
con3 = el3[0].lhs.subs(w, 1).doit()
eqs3 = [e.lhs.subs(w, 1).doit() for e in el3[1:]]
# Kasner family: the raw equations divided by V = e^{sum lam} involve only lamdot, lamddot
u = sp.symbols('u', positive=True)
den = 1 + u + u ** 2
pk = [-u / den, (1 + u) / den, u * (1 + u) / den]


def on(e, lamdot, lamddot):
    rep = {}
    for k in range(3):
        rep[lam3[k].diff(t, 2)] = lamddot[k]
        rep[lam3[k].diff(t)] = lamdot[k]
    return sp.simplify(e.subs(rep))


def per_volume(e):
    return sp.simplify(sp.expand(e * sp.exp(-sum(lam3)), power_exp=False))


L148e = -8 * al * V * cr / w
el3e = euler_equations(L148e, [w] + lam3, t)
okC2 = all(on(per_volume(e.lhs.subs(w, 1).doit()), [q / t for q in pk], [-q / t ** 2 for q in pk]) == 0 for e in el3e)
okC2 = okC2 and sp.simplify(sum(pk) - 1) == 0 and sp.simplify(sum(x ** 2 for x in pk) - 1) == 0
pp = sp.symbols('p1:4', real=True)
okC2 = okC2 and sp.expand(sum(pp) ** 2 - sum(x ** 2 for x in pp) - 2 * (pp[0] * pp[1] + pp[0] * pp[2] + pp[1] * pp[2])) == 0
# the rest-content family
D0, D1, D2 = sp.symbols('D0 D1 D2', real=True)
Dk = [D0, D1, D2]
Dsum = D0 + D1 + D2
Vt = (sp.Rational(3, 2) * m0 * t ** 2 + Dsum * t) / (16 * al)
S_ = sp.diff(Vt, t) / Vt
lamdots = [S_ - (m0 * t + Dk[k]) / (8 * al * Vt) for k in range(3)]
lamddots = [sp.diff(x, t) for x in lamdots]
okC3 = sp.simplify(sum(lamdots) - S_) == 0             # so e^{sum lam} = Vt up to the normalization chosen
cone = D0 ** 2 + D1 ** 2 + D2 ** 2 - 2 * (D0 * D1 + D0 * D2 + D1 * D2)
con_f = on(con3.subs(sp.exp(sum(lam3)), Vt), lamdots, lamddots)     # 8 alpha V sigma2 - m0
eq_f = [on(per_volume(e), lamdots, lamddots) for e in eqs3]         # raw equations per unit volume
# the raw equations read (d/dt + S)(8 alpha (S - lamdot_k)) = 8 alpha sigma2 = m0/V on the constraint
con_on_cone = all(sp.simplify(con_f.subs(D2, r)) == 0 for r in sp.solve(cone, D2))
con_off = sp.simplify(con_f.subs({D0: 1, D1: 2, D2: 7})) != 0
eqs_on_cone = all(sp.simplify(x.subs(D2, r)) == 0 for x in eq_f for r in sp.solve(cone, D2))
eq_ok = eqs_on_cone
con_ok = con_on_cone and con_off
lim_ok = all(sp.limit(lamdots[k] * t, t, sp.oo) == sp.Rational(2, 3) and
             sp.limit(lamdots[k] * t, t, -sp.oo) == sp.Rational(2, 3) for k in range(3))
rev_ok = all(sp.simplify(lamdots[k].subs({t: -t, D0: -D0, D1: -D1, D2: -D2}, simultaneous=True) + lamdots[k]) == 0
             for k in range(3))
check("C1", okC1 and okC2 and okC3 and eq_ok and con_ok and lim_ok and rev_ok,
      "block 148: on h_ii = 2 lam_i the kinetic term is 4(alpha+beta) sum lamdot^2 + 8 beta sum_{i<m} lamdot_i lamdot_m "
      "(-8 alpha cross term at beta = -alpha); EL of -8 alpha V sum_{i<m} lamdot lamdot/w - w m0 derived: Kasner "
      "t^{p_i}, p = (-u, 1+u, u(1+u))/(1+u+u^2), solves the empty equations with sum p = sum p^2 = 1; the family "
      "V = (3 m0 t^2/2 + D t)/(16 alpha), lamdot_k = S - (m0 t + D_k)/(8 alpha V) solves the three equations and "
      "the constraint on the cone D0^2 + D1^2 + D2^2 = 2(D0 D1 + D0 D2 + D1 D2); lamdot_k t -> 2/3 at both ends; "
      "t -> -t, D -> -D reverses it")

# ------------------------------------------------------------------ two small additions
# (i) near V = 0 the rest-content family is Kasner: lamdot_k t -> 1 - 2 D_k/D, sum = 1, sum of squares = 1 on the cone
pk0 = [sp.simplify(sp.limit(lamdots[k] * t, t, 0, '+')) for k in range(3)]
okD1 = all(sp.simplify(pk0[k] - (1 - 2 * Dk[k] / Dsum)) == 0 for k in range(3)) and sp.simplify(sum(pk0) - 1) == 0
sq0 = sp.simplify(sum(x ** 2 for x in pk0) - 1)
okD1 = okD1 and all(sp.simplify(sq0.subs(D2, r)) == 0 for r in sp.solve(cone, D2))
# (ii) with unequal lengths the walk does not commute with itself at two times
la = sp.symbols('a1:4', positive=True)
lb = sp.symbols('b1:4', positive=True)
Ha = sum((sp.sin(kk[i]) * SIG[i] / la[i] for i in range(3)), sp.zeros(2))
Hb = sum((sp.sin(kk[i]) * SIG[i] / lb[i] for i in range(3)), sp.zeros(2))
comm_ab = (Ha * Hb - Hb * Ha).applyfunc(sp.expand)
okD2 = comm_ab != sp.zeros(2) and comm_ab.subs({lb[0]: 2 * la[0], lb[1]: 2 * la[1], lb[2]: 2 * la[2]}).applyfunc(
    sp.expand) == sp.zeros(2)
check("D1", okD1 and okD2, "additions: near V = 0 block 148's rest-content family tends to Kasner, lamdot_k t -> "
      "1 - 2 D_k/D with sum 1 and, on the cone, sum of squares 1; with unequal lengths [H(k; l(t)), H(k; l(t'))] "
      "!= 0 unless the three ratios agree, so block 146's exact 1/l law for top-speed walkers does not carry over "
      "to three lengths (it needs slow stretching)")

npass = sum(ok for _, ok in RES)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass}  ({time.time() - T0:.0f} s)")
if npass == len(RES):
    print("SUMMARY: PROVED blocks 146, 147 and 148 hold as stated within their supplied homogeneous models, by "
          "Euler-Lagrange equations derived here: c_k = -24 alpha; G = 1/(16 pi K) and the Friedmann form iff "
          "alpha = K/4; the pressure form; t^(1/2), t^(2/3); the sea's -I/l with I(4^3) = (3 + sqrt3 + 3 sqrt2)/8, "
          "the staggered square from position space; the bounce at l = I/m0; the cross-term-only kinetic term, "
          "Kasner, and the rest-content family on its cone. Additions: that family is Kasner near V = 0; with three "
          "unequal lengths the walk does not commute in time.")
    print("HIT: blocks 146, 147 and 148 confirmed independently: from c_k l^3 lamdot^2/w - w m and "
          "-8 alpha V sum_{i<m} lamdot_i lamdot_m/w - w m with Euler-Lagrange equations derived here, every stated "
          "solution (t^(1/2), t^(2/3), the bounce at l = I/m0 with lamddot = m0^4/(48 alpha I^3), Kasner with "
          "sum p = sum p^2 = 1, the rest-content family on D0^2 + D1^2 + D2^2 = 2 sum D_i D_j) satisfies them exactly, "
          "and G = 1/(16 pi K), alpha = K/4 and I(4^3) hold; new: the rest-content family starts as Kasner with "
          "p_k = 1 - 2 D_k/D, and with unequal lengths top-speed walkers lose the exact 1/l law.")
else:
    print("SUMMARY: ROUTE FAILS AT a failed check above")
