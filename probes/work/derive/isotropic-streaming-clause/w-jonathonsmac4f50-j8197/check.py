#!/usr/bin/env python3
"""J:derive:isotropic-streaming-clause:a1 - worker w-jonathonsmac4f50-j8197 (claude-opus-5-5).

Setting (block 51, open PR 'ail51'; block 44, open PR 'ail44'; supplied clauses, nothing adopted): sphere menu, a record of content s
(a unit vector) hops to x + d at rate a(s, d); block 51's clause is a(s, sign(s_k) e_k) = |s_k|/sqrt3 on the six axis neighbours.
Streaming of the content-s density f: sum_d a(s,d)[f(x - d) - f(x)] = -(sum_d a d).grad f + (1/2) M_kl d_k d_l f + ...,
M_kl(s) = sum_d a(s,d) d_k d_l.  The fourth-rank moment asked for is T_ijkl = <s_i s_j M_kl(s)> over the uniform sphere.
Route of this attempt (different from a2's pointwise M(s) = m(s) I): the FORWARD-ONLY SHELL RULE
        a(s, d) = lambda_|d|^2 * (s.d/|d|)_+       on the 6 axis, 12 face-diagonal, 8 body-diagonal neighbours,
continuous in s, and the EXACT isotropy condition on T (not a pointwise sufficient condition).
Exact arithmetic throughout (sympy: rationals, sqrt(2), sqrt(3); Fraction for the Markov-chain balance checks).
"""
import itertools
import random
from fractions import Fraction as Fr

import sympy as sp

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


D = [d for d in itertools.product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]
SHELL = {1: [d for d in D if sum(v * v for v in d) == 1], 2: [d for d in D if sum(v * v for v in d) == 2],
         3: [d for d in D if sum(v * v for v in d) == 3]}
l1, l2, l3 = sp.symbols('lambda1 lambda2 lambda3', nonnegative=True)
LAM = {1: l1, 2: l2, 3: l3}
delta = lambda i, j: 1 if i == j else 0

# ================================================================ A1 the sphere lemma
th, ph = sp.symbols('theta phi', real=True)
S = (sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th))


def sphere_avg(expr_pos, expr_neg):
    """(1/4pi) integral over the sphere, split at the equator (|s_3| = +-cos theta)."""
    top = sp.integrate(sp.integrate(expr_pos * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi / 2))
    bot = sp.integrate(sp.integrate(expr_neg * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, sp.pi / 2, sp.pi))
    return sp.simplify((top + bot) / (4 * sp.pi))


ok = True
lemma = {}
for i in range(3):
    for j in range(i, 3):
        val = sphere_avg(S[i] * S[j] * sp.cos(th), -S[i] * S[j] * sp.cos(th))
        lemma[(i, j)] = val
        ok &= val == sp.Rational(delta(i, j) + delta(i, 2) * delta(j, 2), 8)
ok &= sphere_avg(sp.cos(th), -sp.cos(th)) == sp.Rational(1, 2)
check('A1', ok, "EXACT (sphere integrals with n = e_3; the uniform measure is rotation invariant, so for every unit n): "
      "<s_i s_j |s.n|> = (delta_ij + n_i n_j)/8 and <|s.n|> = 1/2; hence <s_i s_j (s.n)_+> = (delta_ij + n_i n_j)/16 (the odd "
      "part vanishes). Block 51's moments are the cases n = e_k: 1/2, 1/4, 1/8",
      f"<s_i s_j |s_3|> = {dict((k, str(v)) for k, v in lemma.items())}")

# ================================================================ A2 the fourth-rank moment of the shell rule
def T_shell():
    """T_ijkl = sum_d lambda_d d_k d_l <s_i s_j (s.dhat)_+> = (1/16) sum_d lambda_d d_k d_l (delta_ij + dhat_i dhat_j)."""
    T = {}
    for idx in itertools.product(range(3), repeat=4):
        i, j, k, l = idx
        tot = 0
        for sh, vecs in SHELL.items():
            for d in vecs:
                tot += LAM[sh] * d[k] * d[l] * (delta(i, j) + sp.Rational(d[i] * d[j], sh))
        T[idx] = sp.expand(tot / 16)
    return T


T = T_shell()
alpha = T[(0, 0, 1, 1)]
beta = T[(0, 1, 0, 1)]
iso = {idx: alpha * delta(idx[0], idx[1]) * delta(idx[2], idx[3])
       + beta * (delta(idx[0], idx[2]) * delta(idx[1], idx[3]) + delta(idx[0], idx[3]) * delta(idx[1], idx[2])) for idx in T}
resid = {idx: sp.factor(T[idx] - iso[idx]) for idx in T}
cond = l1 - l2 - sp.Rational(8, 3) * l3
ok = all(sp.simplify(r) == 0 or sp.simplify(r / cond) .is_number for r in resid.values())
nonzero = [r for r in resid.values() if sp.simplify(r) != 0]
ok &= len(nonzero) > 0 and all(sp.simplify(r.subs(l1, l2 + sp.Rational(8, 3) * l3)) == 0 for r in resid.values())
ok &= sp.simplify(resid[(0, 0, 0, 0)] - cond / 8) == 0
# block 51's axis clause reproduced: lambda1 = 1/sqrt3, others 0
ax = {l1: 1 / sp.sqrt(3), l2: 0, l3: 0}
ok &= sp.simplify(T[(0, 0, 0, 0)].subs(ax) - 1 / (4 * sp.sqrt(3))) == 0 and sp.simplify(T[(0, 0, 1, 1)].subs(ax) - 1 / (8 * sp.sqrt(3))) == 0
ok &= T[(0, 1, 0, 1)].subs(ax) == 0
check('A2', ok, "EXACT (all 81 components): for a(s,d) = lambda_shell (s.dhat)_+ the fourth-rank moment is "
      "T_ijkl = (1/16)[delta_ij S_kl + Q_ijkl], S = (2 lambda1 + 8 lambda2 + 8 lambda3) I, Q the shells' fourth moment; its "
      "departure from isotropy is the single number T_1111 - T_1122 - 2 T_1212 = (lambda1 - lambda2 - (8/3) lambda3)/8, so T is "
      "isotropic IFF lambda1 = lambda2 + (8/3) lambda3; axis hops alone (lambda2 = lambda3 = 0) never, and block 51's values "
      "T_1111 = 1/(4 sqrt3), T_1122 = 1/(8 sqrt3), T_1212 = 0 are the case lambda1 = 1/sqrt3",
      f"alpha = T_1122 = {alpha}; beta = T_1212 = {beta}; T_1111 - iso = {resid[(0, 0, 0, 0)]}")

# ================================================================ A3 mean displacement proportional to s, with one constant
kappa = l1 + 2 * sp.sqrt(2) * l2 + 4 * l3 / sp.sqrt(3)
ok = True
samples = [(1, 0, 0), (0, -1, 0), (1, 1, 1), (3, 2, 1), (5, -1, 2), (2, 2, -1), (7, 3, -4), (1, -2, 0), (-3, 5, 11)]
for s in samples:
    mean = [0, 0, 0]
    for sh, vecs in SHELL.items():
        for d in vecs:
            sd = sum(a * b for a, b in zip(s, d))
            if sd > 0:
                for k in range(3):
                    mean[k] += LAM[sh] * sd / sp.sqrt(sh) * d[k]
    ok &= all(sp.simplify(mean[k] - kappa * s[k]) == 0 for k in range(3))
check('A3', ok, "EXACT (nine directions, including generic ones; the rule is homogeneous of degree 1 in s): the mean "
      "displacement is sum_d a(s,d) d = kappa s with ONE constant kappa = lambda1 + 2 sqrt2 lambda2 + 4 lambda3/sqrt3 for every "
      "s ((t)_+ = (t + |t|)/2; the |t| part cancels between d and -d; each shell's sum of d d^T is a multiple of I); the rule is "
      "non-negative, continuous in s, and forward-only (a(s,d) > 0 only when s.d > 0)")

# ================================================================ A4 the viscous and number terms; block 51's obstruction removed
iso_l = {l1: l2 + sp.Rational(8, 3) * l3}
a_iso, b_iso = sp.simplify(alpha.subs(iso_l)), sp.simplify(beta.subs(iso_l))
sigma = 2 * l1 + 8 * l2 + 8 * l3
Dn = sp.simplify(sigma / 8)
ok = sp.simplify(a_iso - (sigma.subs(iso_l) + 16 * b_iso) / 16) == 0 and sp.simplify(b_iso - (2 * l2 + sp.Rational(8, 3) * l3) / 16) == 0
# potential inflow chi = 1/r: the viscous term (3/2)[alpha Lap g + 2 beta grad div g] vanishes identically
X = sp.symbols('x y z', real=True)
chi = 1 / sp.sqrt(sum(v ** 2 for v in X))
g = [sp.diff(chi, v) for v in X]
lap = [sp.simplify(sum(sp.diff(gi, v, 2) for v in X)) for gi in g]
div = sp.simplify(sum(sp.diff(g[k], X[k]) for k in range(3)))
ok &= all(v == 0 for v in lap) and div == 0
check('A4', ok, "EXACT: on the isotropy line the second-order streaming term gives the momentum equation "
      "(3/2)[alpha Lap g_i + 2 beta d_i div g] with alpha = (3/4) lambda2 + lambda3 and beta = lambda2/8 + lambda3/6 "
      "(the local-equilibrium content law (n/4pi)(1 + 3u.s) gives 3 T_ijkl g_j), no term of cubic symmetry, and the number "
      "equation (sigma/8) Lap n = ((5/4) lambda2 + (5/3) lambda3) Lap n; on a potential inflow "
      "(g = grad(1/r)) both terms vanish identically, so block 51 T3's obstruction (a viscous stress no pressure can balance) "
      "is absent for these rates",
      f"alpha = {a_iso}, beta = {b_iso}, D_n = sigma/8 = {sp.simplify(Dn.subs(iso_l))}")

# ================================================================ B1 the uniform product measure is stationary, for ANY rates
def balance(L, N, contents, vec, rates, solid, gamma, exchange=True):
    """Exact inflow - outflow of the uniform measure for every configuration of N records on the L^3 torus.
    Events: record at y, content c, hop d at rate rates[c][d]: empty target -> move; occupied -> exchange contents (if
    exchange) else nothing; solid -> content reversed (c -> c^1). Bonds (6-neighbour) with two records re-draw the ordered
    pair of contents uniformly over pairs with the same vector sum, at rate gamma."""
    sites = [p for p in itertools.product(range(L), repeat=3) if p not in solid]
    wrap = lambda p: tuple(v % L for v in p)
    bonds = []
    for p in itertools.product(range(L), repeat=3):
        for k in range(3):
            q = list(p); q[k] += 1; q = wrap(q)
            if p not in solid and q not in solid:
                bonds.append((p, q))
    classes = {}
    for c1 in contents:
        for c2 in contents:
            key = tuple(a + b for a, b in zip(vec[c1], vec[c2]))
            classes.setdefault(key, []).append((c1, c2))
    inflow, outflow = {}, {}

    def add(dct, key, v):
        dct[key] = dct.get(key, 0) + v

    configs = []
    for occ in itertools.combinations(sites, N):
        for cs in itertools.product(contents, repeat=N):
            configs.append(tuple(sorted(zip(occ, cs))))
    for conf in configs:
        where = dict(conf)
        for y, c in conf:
            for d, rate in rates[c].items():
                t = wrap((y[0] + d[0], y[1] + d[1], y[2] + d[2]))
                new = dict(where)
                if t in solid:
                    new[y] = c ^ 1
                elif t in where:
                    if not exchange:
                        continue
                    new[y], new[t] = where[t], c
                else:
                    del new[y]; new[t] = c
                target = tuple(sorted(new.items()))
                add(outflow, conf, rate); add(inflow, target, rate)
        for p, q in bonds:
            if p in where and q in where:
                cls = classes[tuple(a + b for a, b in zip(vec[where[p]], vec[where[q]]))]
                for c1, c2 in cls:
                    new = dict(where); new[p], new[q] = c1, c2
                    target = tuple(sorted(new.items()))
                    add(outflow, conf, gamma / len(cls)); add(inflow, target, gamma / len(cls))
    bad = [cf for cf in configs if inflow.get(cf, 0) != outflow.get(cf, 0)]
    return len(configs), len(bad)


random.seed(20260923)
six = list(range(6))
vec6 = {0: (1, 0, 0), 1: (-1, 0, 0), 2: (0, 1, 0), 3: (0, -1, 0), 4: (0, 0, 1), 5: (0, 0, -1)}
rates = {}
for c in (0, 2, 4):
    rates[c] = {d: Fr(random.randint(1, 9), random.randint(1, 9)) for d in D}
    rates[c ^ 1] = {d: rates[c][tuple(-v for v in d)] for d in D}          # a(-s, d) = a(s, -d)
n1, b1 = balance(3, 2, six, vec6, rates, {(0, 0, 0)}, Fr(3, 2))
n2, b2 = balance(3, 2, six, vec6, rates, set(), Fr(3, 2))
two = [0, 1]
n3, b3 = balance(3, 3, two, vec6, {c: rates[c] for c in two}, set(), Fr(2, 1))
n4, b4 = balance(3, 2, six, vec6, rates, set(), Fr(3, 2), exchange=False)
ok = b1 == 0 and b2 == 0 and b3 == 0 and b4 > 0
check('B1', ok, "EXACT (3^3 torus, all 26 hop vectors with RANDOM positive rational rates a(c, d), one reflecting solid "
      "site, bond re-draws on momentum classes): the uniform measure balances in every configuration - for each record at y "
      "with content s and each hop vector d there is exactly one predecessor (the record at y - d moved, or exchanged, or "
      "for a solid y - d the record at y with -s was reflected, which needs a(-s, d) = a(s, -d), true for the shell rule), "
      "so inflow = sum_d a(s,d) = outflow whatever the rates; block 44's T2 carries over to any hop set and rates. Without "
      "the exchange it fails",
      f"2 records + solid: {n1} configs, {b1} unbalanced; 2 records: {n2}, {b2}; 3 records (2 contents): {n3}, {b3}; "
      f"no exchange: {b4} of {n4} unbalanced")

# ================================================================ B2 the capture law of a site
def r_direct(s):
    tot = 0
    for sh, vecs in SHELL.items():
        for d in vecs:
            sd = sum(a * b for a, b in zip(s, d))
            if sd > 0:
                tot += LAM[sh] * sd / sp.sqrt(sh)
    return tot


def r_closed(s):
    a = [abs(v) for v in s]
    face = sp.sqrt(2) * sum(max(a[i], a[j]) for i, j in ((0, 1), (0, 2), (1, 2)))
    body = sum(abs(s[0] + e2 * s[1] + e3 * s[2]) for e2 in (1, -1) for e3 in (1, -1)) / sp.sqrt(3)
    return l1 * sum(a) + l2 * face + l3 * body


ok = all(sp.simplify(r_direct(s) - r_closed(s)) == 0 for s in samples)
unit = {'axis': (1, 0, 0), 'face': (1, 1, 0), 'body': (1, 1, 1)}
rv = {k: sp.simplify(r_closed(v) / sp.sqrt(sum(x * x for x in v))) for k, v in unit.items()}
mean_r = sp.Rational(3, 2) * l1 + 3 * l2 + 2 * l3                    # <|s.dhat|> = 1/2 on each of the N/2 pairs of a shell
on_line = {k: sp.expand(v.subs(iso_l)) for k, v in rv.items()}
gap = sp.expand(on_line['body'] - on_line['axis'])
c2, c3 = gap.coeff(l2), gap.coeff(l3)
ok &= sp.N(c2) > 0 and sp.N(c3) > 0
check('B2', ok, "EXACT: a capturing site takes records of content s at rate rho r(s), r(s) = sum_d a(s,d) = lambda1 |s|_1 + "
      "lambda2 sqrt2 sum_{i<j} max(|s_i|,|s_j|) + lambda3 (1/sqrt3) sum_{sign patterns} |s_1 +- s_2 +- s_3| (block 48's |s|_1 "
      "is the axis case), <r> = (3/2) lambda1 + 3 lambda2 + 2 lambda3; r is never constant on the sphere (a positive "
      "combination of finitely many |s.dhat| is linear on an open cone of the sphere, and a linear function is not constant "
      "there): on the isotropy line r(body diagonal) - r(axis) = c2 lambda2 + c3 lambda3 with c2, c3 > 0, so every "
      "isotropic-moment member of the family captures body-diagonal contents faster than axis contents",
      f"r per unit content: axis {rv['axis']}, face {rv['face']}, body {rv['body']}; on the line body - axis = "
      f"{sp.nsimplify(c2)} lambda2 + {sp.nsimplify(c3)} lambda3 = {float(c2):.4f} lambda2 + {float(c3):.4f} lambda3")

# ================================================================ B3 the collisionless shadow far away
members = {'axis clause (block 51)': {l1: 1 / sp.sqrt(3), l2: 0, l3: 0},
           'axes + face diagonals (1,1,0)': {l1: 1, l2: 1, l3: 0},
           'axes + body diagonals (8,0,3)': {l1: 8, l2: 0, l3: 3}}
rows = []
ok = True
for name, sub in members.items():
    vals = [sp.nsimplify(sp.simplify(rv[k].subs(sub))) for k in ('axis', 'face', 'body')]
    lo, hi = min(vals, key=lambda v: float(v)), max(vals, key=lambda v: float(v))
    rows.append(f"{name}: r(axis) : r(face) : r(body) = {', '.join(f'{float(v):.4f}' for v in vals)} (max/min {float(hi / lo):.4f})")
    ok &= float(hi / lo) > 1
ax_vals = [sp.simplify(rv[k].subs(members['axis clause (block 51)'])) for k in ('axis', 'face', 'body')]
ok &= sp.simplify(ax_vals[1] / ax_vals[0] - sp.sqrt(2)) == 0 and sp.simplify(ax_vals[2] / ax_vals[0] - sp.sqrt(3)) == 0
check('B3', ok, "EXACT ratios (the leading far shadow per unit capture has angular density r(n)/(4 pi <r>) - see ATTEMPT step "
      "8, via the strong law of large numbers for the directed walk, an ASSUMED import): the collisionless shadow stays "
      "anisotropic for every member of the family; the axis clause reproduces block 48's leading term |n|_1 (1 : sqrt2 : "
      "sqrt3, 73% spread); axes + face diagonals with equal rates spread 15%, axes + body diagonals 33%",
      "; ".join(rows))

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PARTIAL, exact: the forward-only rule a(s,d) = lambda_shell (s.dhat)_+ on the 26 neighbours has mean "
      "displacement kappa s with one constant for every unit s, is continuous in s, and has an isotropic fourth-rank "
      "moment IFF lambda_axis = lambda_face + (8/3) lambda_body (axes + face diagonals at equal rates, or axes + body "
      "diagonals at 8 : 3); then the momentum equation's second-order term is (3/2)[alpha Lap g + 2 beta grad div g] and "
      "block 51's obstruction to the potential inflow is absent; the uniform product measure is stationary for every rate "
      "function (one predecessor per record and hop vector); the capture law is r(s) = sum_d a(s,d), never constant for a "
      "forward-only rule of this form, so the collisionless shadow remains anisotropic (15% for the best member)")
if all(RESULTS):
    print("HIT: for block 51's inertial record gas, the forward-only hop rule a(s,d) = lambda_|d|^2 (s.d/|d|)_+ on the 6 "
          "axis, 12 face-diagonal and 8 body-diagonal neighbours (continuous and non-negative in s, mean displacement kappa s "
          "with one constant) has an isotropic fourth-rank streaming moment exactly when lambda_1 = lambda_2 + (8/3) lambda_3 "
          "- the departure from isotropy is (lambda_1 - lambda_2 - (8/3) lambda_3)/8 - which answers attempt a2's open "
          "question (a continuous forward-only rule exists; M(s) proportional to I is not needed); the uniform product "
          "measure stays stationary for every rate function (block 44's predecessor argument, per hop vector); the capture "
          "law is r(s) = sum_d a(s,d), never constant for such rules, so the collisionless shadow keeps an anisotropy "
          "(r(body)/r(axis) > 1 on the whole isotropy line)")
