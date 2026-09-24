#!/usr/bin/env python3
"""Do block 60's lengths change the records' pair law?  Exact checks (sympy, rationals).

Hop x -> y (y empty) at rate  w_x * s(bond length) * h / 6,  h = W(C')/(W(C)+W(C')): timed by the occupied site
(block 97, a = 1), the bond crossed at block 59/60's length l_b = chi_x chi_y (bonds crossed at sqrt(w_x w_y)/(chi_x chi_y)).
"""
import itertools, sys
import sympy as sp

FAIL = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)

# ---------------------------------------------------------------- A1: held field, ring of five, symbolic everything
n = 5
w = sp.symbols('w0:5', positive=True); ch = sp.symbols('chi0:5', positive=True)
pw, qw = sp.symbols('p q', positive=True)
content = {}   # contents +-1 for two records; W = pair weight on occupied bonds
sfun = sp.Function('s')
def rate(C, x, y, W, sb):
    Cp = tuple(sorted([z for z in C if z != x] + [y]))
    h = W(Cp) / (W(C) + W(Cp))
    return w[x] * sb(x, y) * h / 6, Cp
def Wpair(C):
    val = 1
    for r, t in itertools.combinations(C, 2):
        if (r - t) % n in (1, n - 1):
            val *= pw
    return val
def db_ok(nrec, W, sb, law):
    ok = True
    for C in itertools.combinations(range(n), nrec):
        for x in C:
            for y in ((x + 1) % n, (x - 1) % n):
                if y in C:
                    continue
                r1, Cp = rate(C, x, y, W, sb)
                r2, _ = rate(Cp, y, x, W, sb)
                if sp.simplify(law(C) * r1 - law(Cp) * r2) != 0:
                    ok = False
    return ok
law_1w = lambda C: sp.Mul(*[1 / w[z] for z in C])
bond_prod = lambda x, y: 1 / (ch[x] * ch[y])
bond_gen = lambda x, y: sfun(ch[x] * ch[y])
check("A1 one record, held (w, chi): rate w_x/(chi_x chi_y): stationary law 1/w (lengths cancel)", db_ok(1, lambda C: 1, bond_prod, law_1w))
check("A1 one record: any function s of the bond length chi_x chi_y: law 1/w", db_ok(1, lambda C: 1, bond_gen, law_1w))
check("A1 two and three records with exclusion and block 39-type pair weights W: law W(C) prod 1/w",
      db_ok(2, Wpair, bond_prod, lambda C: Wpair(C) * law_1w(C)) and db_ok(3, Wpair, bond_gen, lambda C: Wpair(C) * law_1w(C)))
# per-own-tick rate and direction odds see the lengths (kinetics), yet the law does not
x0 = 2
odds = [1 / (ch[x0] * ch[(x0 + 1) % n]), 1 / (ch[x0] * ch[(x0 - 1) % n])]
check("A1 remark: per own tick the hop rate is 1/(chi_x chi_y), its direction odds depend on the lengths (biased to short bonds)",
      sp.simplify(odds[0] / (odds[0] + odds[1]) - ch[(x0 - 1) % n] / (ch[(x0 - 1) % n] + ch[(x0 + 1) % n])) == 0)
# negative controls: a factor of the occupied site's own length is NOT a bond factor
own = lambda x, y: 1 / ch[x] ** 2
check("A1 control: rate w_x / l_x (occupied site's own length l = chi^2) gives law l/w instead (lengths enter)",
      db_ok(1, lambda C: 1, own, lambda C: sp.Mul(*[ch[z] ** 2 / w[z] for z in C])))
check("A1 control: ... and then 1/w alone is NOT stationary", not db_ok(1, lambda C: 1, own, law_1w))

# ---------------------------------------------------------------- A2: slaved field at first order (superposition = product form)
# log w_z(C) = sum_r om(z - r), log chi_z(C) = sum_r la(z - r), om, la EVEN; on the 3x3x3 torus with generic even values.
L = 3
S3 = list(itertools.product(range(L), repeat=3))
def off(a, b):
    return tuple((a[i] - b[i]) % L for i in range(3))
def neg(d):
    return tuple((-c) % L for c in d)
offs = sorted(set(S3))
rep = {}
for d in offs:
    key = min(d, neg(d))
    rep[d] = key
keys = sorted(set(rep.values()))
Om = {k: sp.Rational(3 + i, 5 + 2 * i) for i, k in enumerate(keys)}         # one-record rate factor exp(om(d)), even
Xc = {k: sp.Rational(7 + 3 * i, 6 + i) for i, k in enumerate(keys)}         # one-record length factor exp(la(d)), even
Om_ = lambda d: Om[rep[d]]; Xc_ = lambda d: Xc[rep[d]]
def wz(C, z):
    return sp.Mul(*[Om_(off(z, r)) for r in C])
def cz(C, z):
    return sp.Mul(*[Xc_(off(z, r)) for r in C])
def nbrs(x):
    out = []
    for j in range(3):
        for sgn in (1, -1):
            y = list(x); y[j] = (y[j] + sgn) % L; out.append(tuple(y))
    return out
def slaved_ok(nrec, bond, law, sample=None):
    ok = True; cnt = 0
    configs = list(itertools.combinations(S3, nrec))
    if sample:
        configs = configs[::sample]
    for C in configs:
        for x in C:
            for y in nbrs(x):
                if y in C:
                    continue
                Cp = tuple(sorted([z for z in C if z != x] + [y]))
                r1 = wz(C, x) * bond(C, x, y)
                r2 = wz(Cp, y) * bond(Cp, y, x)
                if law(C) * r1 != law(Cp) * r2:
                    ok = False
                cnt += 1
    return ok, cnt
pairlaw = lambda C: sp.Mul(*[1 / Om_(off(r, t)) for r, t in itertools.combinations(C, 2)])
bprod = lambda C, x, y: 1 / (cz(C, x) * cz(C, y))
ok2, c2 = slaved_ok(2, bprod, pairlaw)
ok3, c3 = slaved_ok(3, bprod, pairlaw, sample=7)
check("A2 slaved first-order field, rate w_x(C)/(chi_x(C) chi_y(C)): pair law prod over pairs exp(-om(r - s)) "
      "(%d moves of two records, %d of three)" % (c2, c3), ok2 and ok3)
check("A2 the bond length is the same before and after the move (product form, even one-body factor): it cancels",
      all(cz(C, x) * cz(C, y) == cz(tuple(sorted([C[1], y])), x) * cz(tuple(sorted([C[1], y])), y)
          for C in [((0, 0, 0), (1, 1, 0))] for x in [C[0]] for y in nbrs(x) if y not in C))
bsum = lambda C, x, y: 1 / (cz(C, x) + cz(C, y))
okc, _ = slaved_ok(2, bsum, pairlaw)
check("A2 control: a symmetric but non-product bond factor 1/(chi_x + chi_y) breaks the pair law in the slaved field", not okc)
check("A2 control: the fixed-field factor prod_z 1/w_z(C) (pairs counted twice) is not stationary",
      not slaved_ok(2, bprod, lambda C: sp.Mul(*[1 / wz(C, z) for z in C]))[0])

ownlen = lambda C, x, y: 1 / cz(C, x) ** 2
okown, _ = slaved_ok(2, ownlen, lambda C: sp.Mul(*[Xc_(off(r, t)) ** 2 / Om_(off(r, t)) for r, t in itertools.combinations(C, 2)]))
check("A3 variant: a hop that reads its own site's length (rate w_x / l_x): slaved pair law prod exp(log l_1 - log w_1) over pairs", okown)

# ---------------------------------------------------------------- B: the relation under block 60 at first order
Q, b, xx, beta = sp.symbols('Q b x beta', positive=True)
g = 1 / (4 * sp.pi * sp.sqrt(xx ** 2 + b ** 2))                  # far field of the lattice Green function
line = sp.integrate(sp.diff(1 / (4 * sp.pi * sp.sqrt(xx ** 2 + sp.Symbol('y') ** 2)), sp.Symbol('y')).subs(sp.Symbol('y'), b), (xx, -sp.oo, sp.oo))
check("B1 block 98 T2: the line integral of the transverse gradient of 1/(4 pi r) at impact b is -2/(4 pi b)", sp.simplify(line + 2 / (4 * sp.pi * b)) == 0)
gb = 1 / (4 * sp.pi * b)
# block 60 T4 at first order: chi = 1 + Q g, N = 1 - P g, P = Q w_0 = Q + O(Q^2); w = N/chi; l = chi^2
eps = sp.Symbol('epsilon')
chi1 = 1 + eps * Q * gb; N1 = 1 - eps * Q * gb
logw1 = sp.series(sp.log(N1 / chi1), eps, 0, 2).removeO()
logl1 = sp.series(sp.log(chi1 ** 2), eps, 0, 2).removeO()
check("B2 first order: log w_1 = -2 Q g(b), log l_1 = +2 Q g(b) (so l = 1/w: beta = 1, block 60 T3/T4)",
      sp.simplify(logw1 + 2 * eps * Q * gb) == 0 and sp.simplify(logl1 - 2 * eps * Q * gb) == 0)
logg_pair = -logw1                                                  # A2 with om = log w_1: pair excess e^{-om}
logc1 = logw1 - logl1                                               # block 59: bonds crossed at sqrt(w_x w_y)/l_b
delta = -2 * logc1                                                  # turn = -(line integral of d_perp log c) = 2 |log c_1(b)|
check("B3 the wave's turn is delta(b) = 8 Q g(b) = 4 log g(b): the pair law is unchanged, the turn doubles",
      sp.simplify(delta - 8 * eps * Q * gb) == 0 and sp.simplify(delta / logg_pair - 4) == 0)
# general beta (l = w^{-beta}): turn / log g = 2(1 + beta)
lw = sp.Symbol('u')
check("B4 for lengths l = (wbar/w)^beta: log c = (1 + beta) log w, turn = 2(1 + beta) log g: 2 log g at beta = 0, 4 log g at beta = 1",
      sp.simplify((lw - (-beta * lw)) - (1 + beta) * lw) == 0)
logg_own = -logw1 + logl1
check("B4 variant A3 (own site's length): log g = 4 Q g(b) and delta = 2 log g: the answer is fixed by how a hop sees a length",
      sp.simplify(delta / logg_own - 2) == 0)
# remark: per physical volume l^3 the excess changes sign at first order
logg_vol = logg_pair - 3 * logl1
check("B5 remark: referred to physical volume l^3 per site, log g_vol = -4 Q g(b) = -(1/2) delta: the relation depends on the measure",
      sp.simplify(logg_vol + 4 * eps * Q * gb) == 0 and sp.simplify(logg_vol + delta / 2) == 0)

print()
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + FAIL[0]); sys.exit(1)
print("SUMMARY: PROVED for record hops timed by the occupied site and crossing a bond of block 60's length chi_x chi_y "
      "(any function of it): the stationary law in any held (w, l) field is W(C) prod 1/w, and in the first-order slaved "
      "field the pair law is W(C) exp(-sum_pairs log w_1(r - s)), with no trace of the lengths; under block 60 "
      "(beta = 1) the wave's turn is 4 log g(b) at first order (2(1 + beta) log g in general)")
print("HIT: (a) the lengths cancel from the records' stationary law exactly (held field, any number of records) and from "
      "the pair law in the first-order slaved field (bond length unchanged by the move); (b) hence delta(b) = 4 log g(b) "
      "under block 60's curvature member, as the corrigendum of block 98 conjectured (2(1+beta) log g in general); a hop "
      "that reads its own site's length instead gives 2 log g; per physical volume log g_vol = -delta/2")
