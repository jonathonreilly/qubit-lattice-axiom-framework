#!/usr/bin/env python3
"""J:derive:the-members-velocity-dependent-pull:a1 -- worker w-macbookpro9927a-j4748 (Claude Opus 5.5).

Independent exact checks of block 144 (landed on main 2026-09-25) by routes other than its own runner and the a2
attempt's: T1 for arbitrary fields (Euler operator, not plane waves); T2 at generic (non-axis) wave vectors, with and
without the shift, and its failure at alpha != K/4; T4 from a Legendre transform done here and exact expectation
values on explicit hydrogenic states, without the virial step; T5(b)-(d) as identities.
Block 144's Lagrangian (position space, beta = -alpha, w = 1):
  L = alpha[tr(Hd^2) - (tr Hd)^2] + K(u R1 + R2) - e u + N.P + (1/2) sum Theta_ij h_ij,  Hd = h' - dN - dN^T."""
import random, time
import sympy as sp

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"{tag} {'PASS' if ok else 'FAIL'}: {msg}", flush=True)


t, x, y, z = sp.symbols('t x y z', real=True)
X = (x, y, z)
K, al = sp.symbols('K alpha', positive=True)
PAIRS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]


def R1R2(Hf):
    trh = sum(Hf(i, i) for i in range(3))
    r1 = sum(sp.diff(Hf(i, j), X[i], X[j]) for i in range(3) for j in range(3)) - sum(sp.diff(trh, X[k], 2) for k in range(3))
    r2 = (-sp.Rational(1, 4) * sum(sp.diff(Hf(i, j), X[k]) ** 2 for i in range(3) for j in range(3) for k in range(3))
          + sp.Rational(1, 2) * sum(sum(sp.diff(Hf(i, k), X[i]) for i in range(3)) ** 2 for k in range(3))
          - sp.Rational(1, 2) * sum(sum(sp.diff(Hf(i, j), X[i]) for i in range(3)) * sp.diff(trh, X[j]) for j in range(3))
          + sp.Rational(1, 4) * sum(sp.diff(trh, X[k]) ** 2 for k in range(3)))
    return r1, r2


# ---------------------------------------------------------------- T1: the comparator's second-order action, any field
eps = sp.symbols('epsilon', real=True)
hs = {ij: sp.Function('g%d%d' % (ij[0] + 1, ij[1] + 1))(x, y, z) for ij in PAIRS}
Hm = sp.Matrix(3, 3, lambda i, j: hs[(min(i, j), max(i, j))])
gm = sp.eye(3) + eps * Hm
gi = sp.eye(3) - eps * Hm + eps ** 2 * Hm * Hm


def trunc(e_, n=2):
    return sp.series(sp.expand(e_), eps, 0, n + 1).removeO() if e_.has(eps) else e_


Gam = [[[trunc(sum(gi[k, l] * (sp.diff(gm[j, l], X[i]) + sp.diff(gm[i, l], X[j]) - sp.diff(gm[i, j], X[l])) for l in range(3)) / 2)
         for j in range(3)] for i in range(3)] for k in range(3)]


def Ric(i, j):
    r = 0
    for k in range(3):
        r += sp.diff(Gam[k][i][j], X[k]) - sp.diff(Gam[k][i][k], X[j])
        for l in range(3):
            r += Gam[k][k][l] * Gam[l][i][j] - Gam[k][j][l] * Gam[l][i][k]
    return trunc(r)


Rs = trunc(sum(gi[i, j] * Ric(i, j) for i in range(3) for j in range(3)))
trH = Hm.trace()
dens = sp.expand(trunc((1 + eps * trH / 2 + eps ** 2 * (trH ** 2 / 8 - (Hm * Hm).trace() / 4)) * Rs))
r1s, r2s = R1R2(lambda i, j: Hm[i, j])
first_ok = sp.simplify(dens.coeff(eps, 1) - r1s) == 0
eul = sp.euler_equations(sp.expand(dens.coeff(eps, 2) - r2s), list(hs.values()), [x, y, z])
second_ok = all(sp.simplify(q.lhs - q.rhs) == 0 for q in eul)
# kinetic: first-order extrinsic curvature K_ij = Hd_ij/2 -> (1/4)[tr Hd^2 - (tr Hd)^2]; the member's (alpha, beta) form
A_, B_ = sp.symbols('A_ B_')
Hd = sp.Matrix(3, 3, lambda i, j: sp.Symbol('d%d%d' % (min(i, j), max(i, j))))
mem = al * (Hd * Hd).trace() + sp.Symbol('beta') * Hd.trace() ** 2
adm = K * ((Hd * Hd).trace() - Hd.trace() ** 2) / 4
kin = sp.solve(sp.Poly(sp.expand(mem - adm), *Hd.free_symbols).coeffs(), [al, sp.Symbol('beta')], dict=True)
check("T1", first_ok and second_ok and kin == [{al: K / 4, sp.Symbol('beta'): -K / 4}],
      "for every field h(x): (sqrt(g) R)^(1) = R1 exactly and (sqrt(g) R)^(2) - R2 has identically zero Euler derivatives "
      "(a total divergence); the kinetic parts match iff alpha = K/4, beta = -alpha: the member is K x the comparator's "
      "second-order lapse-and-shift action")

# ---------------------------------------------------------------- T2: the exchange at generic wave vectors
hf = {ij: sp.Function('h%d%d' % (ij[0] + 1, ij[1] + 1))(t, x, y, z) for ij in PAIRS}
Nf = [sp.Function('N%d' % (j + 1))(t, x, y, z) for j in range(3)]
u = sp.Function('u')(t, x, y, z)
ef = sp.Function('e')(t, x, y, z)
Pf = [sp.Function('P%d' % (j + 1))(t, x, y, z) for j in range(3)]
Thf = {ij: sp.Function('Th%d%d' % (ij[0] + 1, ij[1] + 1))(t, x, y, z) for ij in PAIRS}


def Hh(i, j):
    return hf[(min(i, j), max(i, j))]


def Lag(shift):
    Hdd = [[sp.diff(Hh(i, j), t) - ((sp.diff(Nf[j], X[i]) + sp.diff(Nf[i], X[j])) if shift else 0) for j in range(3)] for i in range(3)]
    trd = sum(Hdd[i][i] for i in range(3))
    r1, r2 = R1R2(Hh)
    src = -ef * u + (sum(Nf[j] * Pf[j] for j in range(3)) if shift else 0) + \
        sp.Rational(1, 2) * sum(Thf[(min(i, j), max(i, j))] * Hh(i, j) for i in range(3) for j in range(3))
    return al * (sum(Hdd[i][j] ** 2 for i in range(3) for j in range(3)) - trd ** 2) + K * (u * r1 + r2) + src


def FP(sa, sb):
    def T4(s):
        M = sp.zeros(4)
        M[0, 0] = s[0]
        for i in range(3):
            M[0, i + 1] = s[1 + i]; M[i + 1, 0] = s[1 + i]
        for k, (i, j) in enumerate(PAIRS):
            M[i + 1, j + 1] = s[4 + k]; M[j + 1, i + 1] = s[4 + k]
        return M
    A, B = T4(sa), T4(sb)
    eta = sp.diag(-1, 1, 1, 1)
    Al = eta * A * eta
    return sum(Al[m, n] * B[m, n] for m in range(4) for n in range(4)) - \
        sum(eta[m, m] * A[m, m] for m in range(4)) * sum(eta[m, m] * B[m, m] for m in range(4)) / 2


def book(p, w, th):
    Tm = sp.zeros(3)
    for k, (i, j) in enumerate(PAIRS):
        Tm[i, j] = th[k]; Tm[j, i] = th[k]
    P = [sum(p[i] * Tm[i, j] for i in range(3)) / w for j in range(3)]
    return [sum(p[j] * P[j] for j in range(3)) / w] + P + list(th)


random.seed(11)
ok2 = True
det = []
for shift in (True, False):
    Lg = Lag(shift)
    flds = ([u] + Nf if shift else [u]) + [hf[ij] for ij in PAIRS]
    eqs = sp.euler_equations(Lg, flds, [t, x, y, z])
    for p, w in (((1, 2, 2), sp.Rational(7, 3)), ((sp.Rational(2, 5), sp.Rational(1, 3), -sp.Rational(3, 7)), sp.Rational(5, 11))):
        amp = sp.symbols('A0:%d' % len(flds))
        ph = sp.exp(sp.I * (p[0] * x + p[1] * y + p[2] * z - w * t))
        th1 = [sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(6)]
        th2 = [sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(6)]
        s1, s2 = book(p, w, th1), book(p, w, th2)
        sub = {f: a * ph for f, a in zip(flds, amp)}
        sub.update({ef: s1[0] * ph})
        sub.update({Pf[j]: s1[1 + j] * ph for j in range(3)})
        sub.update({Thf[ij]: s1[4 + k] * ph for k, ij in enumerate(PAIRS)})
        rows = [sp.expand((q.lhs - q.rhs).subs(sub).doit() / ph) for q in eqs]
        for alv in (K / 4, K / 3):
            sol = sp.linsolve([r.subs(al, alv) for r in rows], amp)
            if sol == sp.EmptySet:
                ok2 &= (alv == K / 3)
                continue
            ok2 &= (alv == K / 4)
            fm = dict(zip(flds, list(sol)[0]))
            pair = -s2[0] * fm[u] + (sum(s2[1 + j] * fm[Nf[j]] for j in range(3)) if shift else 0) + \
                sp.Rational(1, 2) * sum(s2[4 + k] * fm[hf[ij]] * (1 if ij[0] == ij[1] else 2) for k, ij in enumerate(PAIRS))
            q2 = sum(v ** 2 for v in p)
            diff = sp.simplify(pair - FP(s2, s1) / (2 * K * (q2 - w ** 2)))
            ok2 &= diff == 0 and pair.free_symbols <= {K}
check("T2", ok2, "at p = (1,2,2), omega = 7/3 and p = (2/5,1/3,-3/7), omega = 5/11 (not along an axis), with and without the "
      "shift: sources that keep the books have a solution at alpha = K/4, the pairing -e'u + N.P' + (1/2)Th'.h is free of "
      "the relabellings and equals (1/(2K))[T'.T - (1/2)T'T]/(p^2 - omega^2); at alpha = K/3 no solution")

# ---------------------------------------------------------------- T4: Legendre transform and explicit bound states
m1, m2, kk, lam = sp.symbols('m1 m2 k lambda', positive=True)
a, b, c = sp.symbols('a b c', real=True)
nv = sp.Matrix(sp.symbols('n1:4', real=True))
rr = sp.Symbol('r', positive=True)
v1 = sp.Matrix(sp.symbols('v1x v1y v1z', real=True)); v2 = sp.Matrix(sp.symbols('v2x v2y v2z', real=True))
p1 = sp.Matrix(sp.symbols('p1x p1y p1z', real=True)); p2 = sp.Matrix(sp.symbols('p2x p2y p2z', real=True))


def Lfun(V1, V2, kv):
    return -m1 * sp.sqrt(1 - V1.dot(V1)) - m2 * sp.sqrt(1 - V2.dot(V2)) + \
        (kv / rr) * (1 + a * (V1.dot(V1) + V2.dot(V2)) + b * V1.dot(V2) + c * nv.dot(V1) * nv.dot(V2))


# scaling: v ~ lam, k ~ lam^2; invert p = dL/dv to O(lam^3), then H = p.v - L to O(lam^4)
w1 = sp.Matrix(sp.symbols('w1x w1y w1z')); w2 = sp.Matrix(sp.symbols('w2x w2y w2z'))
V1 = lam * p1 / m1 + lam ** 3 * w1
V2 = lam * p2 / m2 + lam ** 3 * w2
Ls = Lfun(V1, V2, lam ** 2 * kk)
eqs = []
for j in range(3):
    for Vv, pp, ww in ((V1, p1, w1), (V2, p2, w2)):
        dL = sp.diff(Lfun(sp.Matrix(sp.symbols('q1:4')), V2, lam ** 2 * kk) if Vv is V1 else Lfun(V1, sp.Matrix(sp.symbols('q1:4')), lam ** 2 * kk),
                     sp.symbols('q1:4')[j])
        dL = dL.subs({sp.symbols('q1:4')[i]: Vv[i] for i in range(3)})
        eqs.append(sp.expand(sp.series(dL - lam * pp[j], lam, 0, 4).removeO()).coeff(lam, 3))
wsol = sp.solve(eqs, list(w1) + list(w2), dict=True)[0]
Hs = sp.expand(sp.series((lam * p1.dot(V1) + lam * p2.dot(V2) - Ls).subs(wsol), lam, 0, 5).removeO())
Hexp = (m1 + m2 + lam ** 2 * (p1.dot(p1) / (2 * m1) + p2.dot(p2) / (2 * m2)) - lam ** 4 * ((p1.dot(p1)) ** 2 / (8 * m1 ** 3) + (p2.dot(p2)) ** 2 / (8 * m2 ** 3))
        - lam ** 2 * kk / rr - lam ** 4 * (kk / rr) * (a * (p1.dot(p1) / m1 ** 2 + p2.dot(p2) / m2 ** 2) + b * p1.dot(p2) / (m1 * m2)
                                                       + c * nv.dot(p1) * nv.dot(p2) / (m1 * m2)))
legendre_ok = sp.simplify(Hs - sp.expand(Hexp)) == 0
# centre of mass: p1 = (m1/M) P e + q, p2 = (m2/M) P e - q ; the P^2 coefficient operator along e
M = m1 + m2
mu = m1 * m2 / M
Pp = sp.Symbol('P')
qv = sp.Matrix(sp.symbols('qx qy qz', real=True))
ev = sp.Matrix(sp.symbols('e1:4', real=True))
Hcm = sp.expand(Hexp.subs(lam, 1).subs({p1[i]: m1 / M * Pp * ev[i] + qv[i] for i in range(3)}, simultaneous=True)
                .subs({p2[i]: m2 / M * Pp * ev[i] - qv[i] for i in range(3)}, simultaneous=True))
C2 = sp.expand(sp.diff(Hcm, Pp, 2).subs(Pp, 0) / 2)            # coefficient of P^2 (with e.e = 1 to be imposed)
# hydrogenic states of H0 = q^2/(2 mu) - k/r, Bohr radius a0 = 1/(mu k); real wavefunctions in position space
rs, th_, ph_ = sp.symbols('rho theta phi', positive=True)
a0 = 1 / (mu * kk)
xs = [rs * sp.sin(th_) * sp.cos(ph_), rs * sp.sin(th_) * sp.sin(ph_), rs * sp.cos(th_)]
states = {'1s': sp.exp(-rs / a0) / sp.sqrt(sp.pi * a0 ** 3),
          '2p0': xs[2] * sp.exp(-rs / (2 * a0)) / (4 * sp.sqrt(2 * sp.pi) * a0 ** sp.Rational(5, 2)),
          '2px': xs[0] * sp.exp(-rs / (2 * a0)) / (4 * sp.sqrt(2 * sp.pi) * a0 ** sp.Rational(5, 2))}
X3 = sp.symbols('X1:4', real=True)


def expect_state(psi_sph):
    """<q_i q_j> = int d_i psi d_j psi, <n_i n_j / r>, <1/r>, norm; via Cartesian derivatives of psi(X)"""
    Rr = sp.sqrt(X3[0] ** 2 + X3[1] ** 2 + X3[2] ** 2)
    psiX = sp.simplify(psi_sph.subs(rs, Rr).subs({xs[0].subs(rs, Rr): X3[0], xs[1].subs(rs, Rr): X3[1], xs[2].subs(rs, Rr): X3[2]}))
    grad = [sp.diff(psiX, X3[i]) for i in range(3)]
    back = {X3[0]: xs[0], X3[1]: xs[1], X3[2]: xs[2]}
    jac = rs ** 2 * sp.sin(th_)

    def integ(f):
        g_ = sp.simplify(f.subs(back, simultaneous=True) * jac)
        return sp.simplify(sp.integrate(sp.integrate(sp.integrate(g_, (ph_, 0, 2 * sp.pi)), (th_, 0, sp.pi)), (rs, 0, sp.oo)))
    out = {'norm': integ(psiX ** 2), 'inv_r': integ(psiX ** 2 / Rr)}
    for i in range(3):
        for j in range(i, 3):
            out[('qq', i, j)] = integ(grad[i] * grad[j])
            out[('nn', i, j)] = integ(psiX ** 2 * X3[i] * X3[j] / Rr ** 3)
    return out


def weight(expv, e_dir, coeffs):
    """W - 1 at first order in the binding, from <C2> without any virial step"""
    sub = dict(zip(list(ev), e_dir))
    Cop = sp.expand(C2.subs(sub).subs({a: coeffs[0], b: coeffs[1], c: coeffs[2]}) - 1 / (2 * M))   # corrections beyond P^2/(2M)
    val = 0
    # C2 is a polynomial of degree <= 2 in q and depends on n, r only through k n_i n_j / r and k / r
    poly = sp.Poly(Cop, *qv)
    for mon, co in poly.terms():
        if sum(mon) == 2:
            idx = [i for i in range(3) for _ in range(mon[i])]
            val += co * expv[('qq', min(idx), max(idx))]
        elif sum(mon) == 0:
            co_n = sp.Poly(sp.expand(co * rr / kk), *nv)
            for mon2, co2 in co_n.terms():
                if sum(mon2) == 2:
                    idx = [i for i in range(3) for _ in range(mon2[i])]
                    val += co2 * kk * expv[('nn', min(idx), max(idx))]
                elif sum(mon2) == 0:
                    val += co2 * kk * expv['inv_r']
                else:
                    raise ValueError
        else:
            raise ValueError
    E_int = sp.simplify((expv[('qq', 0, 0)] + expv[('qq', 1, 1)] + expv[('qq', 2, 2)]) / (2 * mu) - kk * expv['inv_r'])
    return sp.simplify((E_int + 2 * M ** 2 * val) / M), E_int


ok4 = legendre_ok
table = {}
for name, psi in states.items():
    ex = expect_state(psi)
    ok4 &= sp.simplify(ex['norm'] - 1) == 0
    U = -kk * ex['inv_r']
    for dname, dvec in (('x', (1, 0, 0)), ('z', (0, 0, 1))):
        i = 0 if dname == 'x' else 2
        UP = -kk * ex[('nn', i, i)]
        TP = ex[('qq', i, i)] / (2 * mu)
        vir = sp.simplify(2 * TP + UP) == 0
        w_eih, Eint = weight(ex, dvec, (sp.Rational(3, 2), -sp.Rational(7, 2), -sp.Rational(1, 2)))
        w_clk, _ = weight(ex, dvec, (0, 0, 0))
        ok4 &= vir and w_eih == 0 and sp.simplify(w_clk - (U + UP) / M) == 0
        table[(name, dname)] = sp.nsimplify(sp.simplify(w_clk / (U / M)))
ok4 &= table[('1s', 'x')] == sp.Rational(4, 3) and table[('2p0', 'z')] == sp.Rational(8, 5) and table[('2p0', 'x')] == sp.Rational(6, 5)
check("T4", ok4, "Legendre transform to first order derived here; on 1s, 2p0, 2px and along x, z: the P^2 coefficient gives "
      "W = 1 exactly for (a,b,c) = (3/2,-7/2,-1/2), and W - 1 = (<U> + <U_P>)/M for the clock alone; directional virial "
      "2<T_P> = -<U_P> holds state by state; clock-only (W-1)/(<U>/M) = 4/3 (1s), 8/5 (2p0 along z), 6/5 (2p0 across)")
# necessity: generic (a,b,c) -- two states/directions with different <U_P>/<U> force both conditions
ex1s = expect_state(states['1s']); ex2p = expect_state(states['2p0'])
wa, _ = weight(ex1s, (0, 0, 1), (a, b, c)); wb, _ = weight(ex2p, (0, 0, 1), (a, b, c)); wc, _ = weight(ex2p, (1, 0, 0), (a, b, c))
sol = sp.solve([wa, wb, wc], [b, c], dict=True)
check("T4c", sol == [{b: -2 * a - sp.Rational(1, 2), c: -sp.Rational(1, 2)}],
      "W = 1 on 1s and on 2p0 along and across its axis forces 2a + b = -1/2 and c = -1/2 (block 144 T4(c))")

# ---------------------------------------------------------------- T5 (b)-(d): without the shift
xi = [sp.Function('xi%d' % (j + 1))(x, y, z) for j in range(3)]
hdrift = lambda i, j: t * (sp.diff(xi[j], X[i]) + sp.diff(xi[i], X[j]))
L0 = Lag(False).subs({ef: 0, Pf[0]: 0, Pf[1]: 0, Pf[2]: 0}).subs({Thf[ij]: 0 for ij in PAIRS})
eqs0 = sp.euler_equations(L0, [u] + [hf[ij] for ij in PAIRS], [t, x, y, z])
subd = {hf[ij]: hdrift(*ij) for ij in PAIRS}
subd[u] = 0
res = [sp.simplify((q.lhs - q.rhs).subs(subd).doit().subs(al, K / 4)) for q in eqs0]
Cj = [sp.simplify((4 * (K / 4) * sum(sp.diff(sp.diff(hdrift(i, j), t) - (sp.diff(sum(hdrift(k, k) for k in range(3)), t) if i == j else 0), X[i])
                                      for i in range(3))).doit()) for j in range(3)]
Cwant = [K * (sum(sp.diff(xi[j], X[i], 2) for i in range(3)) - sp.diff(sum(sp.diff(xi[i], X[i]) for i in range(3)), X[j])) for j in range(3)]
# (d): (1/2) Th.h with the books = d/dt(t xi.P) - xi.P + divergence
Pd = [sp.Function('Q%d' % (j + 1))(t, x, y, z) for j in range(3)]
Thd = {ij: sp.Function('S%d%d' % (ij[0] + 1, ij[1] + 1))(t, x, y, z) for ij in PAIRS}
TH = lambda i, j: Thd[(min(i, j), max(i, j))]
coup = sp.Rational(1, 2) * sum(TH(i, j) * hdrift(i, j) for i in range(3) for j in range(3))
target = sp.diff(t * sum(xi[j] * Pd[j] for j in range(3)), t) - sum(xi[j] * Pd[j] for j in range(3)) + \
    sum(sp.diff(t * sum(TH(i, j) * xi[j] for j in range(3)), X[i]) for i in range(3))
books = {sp.diff(Pd[j], t): -sum(sp.diff(TH(i, j), X[i]) for i in range(3)) for j in range(3)}
dres = sp.simplify(sp.expand(coup - target).subs(books))
check("T5", all(r == 0 for r in res) and all(sp.simplify(cj - cw) == 0 for cj, cw in zip(Cj, Cwant)) and dres == 0,
      "without the shift at alpha = K/4: h = t(d xi + d xi^T), u = 0 solves the source-free member for every xi(x); its "
      "momentum-constraint residual is K(lap xi - grad div xi); (1/2)Theta.h = d(t xi.P)/dt - xi.P + divergence by the books")

npass = sum(1 for _, v in RES if v)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass} ({time.time() - T0:.0f}s)")
if npass == len(RES):
    print("SUMMARY: PROVED (confirmation) block 144 T1, T2, T4 and T5(b)-(d) by independent exact routes; T3 not "
          "re-derived here (its a2 check and block 144's own stand)")
    print("HIT: block 144 confirmed by routes independent of its runner and of attempt a2: (T1) for every field h, "
          "(sqrt(g)R)^(1) = R1 and (sqrt(g)R)^(2) - R2 has zero Euler derivatives, so the member is K times the "
          "comparator's second-order lapse-and-shift action iff alpha = K/4, beta = -alpha; (T2) at non-axis wave vectors, "
          "with and without the shift, book-keeping sources give the pairing (1/(2K))[T'.T - T'T/2]/(p^2 - omega^2) free of "
          "relabellings, and no solution at alpha = K/3; (T4) from a Legendre transform derived here and exact hydrogenic "
          "expectation values (1s, 2p0, 2px; along x and z; no virial step), W = 1 for (3/2, -7/2, -1/2), W - 1 = "
          "(<U> + <U_P>)/M for the clock alone (4/3, 8/5, 6/5 times <U>/M), the directional virial holds state by state, and "
          "W = 1 on 1s and 2p0 forces 2a + b = -1/2 and c = -1/2; (T5) the drifting lengths, their residual and their "
          "-xi.P coupling hold as identities")
else:
    print("SUMMARY: ROUTE FAILS AT " + ",".join(tg for tg, v in RES if not v))
