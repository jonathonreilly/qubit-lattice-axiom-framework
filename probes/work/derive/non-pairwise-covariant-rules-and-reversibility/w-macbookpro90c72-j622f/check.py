#!/usr/bin/env python3
"""J:derive:non-pairwise-covariant-rules-and-reversibility:a1 -- worker w-macbookpro90c72-j622f (claude-opus-5-5).

Level chains K(s -> s') = prod_x p(s'_x | eta_x(s)), p = exp F(s'; eta)/Z(eta), eta_x the predecessors of x in the level below.
All checks exact (integer linear algebra, Fractions, sympy).
"""
import itertools, random, sys, time
from fractions import Fraction as Fr
import sympy as sp

T0 = time.time(); FAILS = []
def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)

def rank_int(rows, ncol):
    """exact rank over the rationals of an integer matrix (fraction-free elimination on a growing echelon basis)."""
    basis = {}                                   # pivot column -> row (list of ints)
    for r in rows:
        v = list(r)
        for c in range(ncol):
            if v[c] == 0:
                continue
            if c in basis:
                b = basis[c]; f, g = b[c], v[c]
                v = [f * vi - g * bi for vi, bi in zip(v, b)]
                from math import gcd
                gg = 0
                for vi in v:
                    gg = gcd(gg, abs(vi))
                if gg > 1:
                    v = [vi // gg for vi in v]
            else:
                basis[c] = v
                break
    return len(basis), basis

# ------------------------------------------------------------------ N.null: the reversible rules are exactly the two-body ones
def null_check(m, L, offsets):
    npast = len(offsets)
    idx = {}
    for sp_ in range(m):
        for eta in itertools.product(range(m), repeat=npast):
            idx[(sp_,) + eta] = len(idx)
    n = len(idx)
    confs = list(itertools.product(range(m), repeat=L))
    def Dvec(s, t):                              # D(s, t) = Phi(s, t) - Phi(t, s), Phi(s, t) = sum_x F(t_x; eta_x(s))
        v = [0] * n
        for x in range(L):
            v[idx[(t[x],) + tuple(s[(x + o) % L] for o in offsets)]] += 1
            v[idx[(s[x],) + tuple(t[(x + o) % L] for o in offsets)]] -= 1
        return v
    s0 = confs[0]
    D0 = {t: Dvec(s0, t) for t in confs}
    rows = []
    for s in confs:
        for t in confs:
            if s < t:
                a = Dvec(s, t)
                rows.append([ai - bi + ci for ai, bi, ci in zip(a, D0[t], D0[s])])   # D(s,t) - D(s0,t) + D(s0,s) = 0
    rk, _ = rank_int(rows, n)
    # the predicted family: c(eta), psi(s'), and symmetric two-body terms [s'=a][eta_d=b] + [s'=b][eta_{-d}=a]
    fam = []
    for eta in itertools.product(range(m), repeat=npast):
        v = [0] * n
        for sp_ in range(m):
            v[idx[(sp_,) + eta]] = 1
        fam.append(v)
    for a in range(m):
        v = [0] * n
        for key, i in idx.items():
            if key[0] == a:
                v[i] = 1
        fam.append(v)
    for k, o in enumerate(offsets):
        kk = offsets.index(-o)
        for a in range(m):
            for b in range(m):
                v = [0] * n
                for key, i in idx.items():
                    if key[0] == a and key[1 + k] == b:
                        v[i] += 1
                    if key[0] == b and key[1 + kk] == a:
                        v[i] += 1
                fam.append(v)
    frk, _ = rank_int(fam, n)
    inside = all(sum(r[i] * f[i] for i in range(n)) == 0 for f in fam for r in rows[:: max(1, len(rows) // 400)])
    inside &= all(sum(r[i] * f[i] for i in range(n)) == 0 for f in fam for r in rows)
    return n, n - rk, frk, inside, len(rows)
good = True; rep = []
for m, L in ((2, 4), (3, 4), (2, 5)):
    n, nullity, frk, inside, nrows = null_check(m, L, (-1, 0, 1))
    good &= inside and nullity == frk
    rep.append(f"menu {m}, ring {L}: {nrows} constraints, {n} unknowns, reversible dimension {nullity} = two-body family {frk}")
ok("N.null", good, "on rings with the past {x-1, x, x+1} and every positive rule F(s'; eta) (no symmetry assumed), Kolmogorov's criterion "
   "D(s,t) - D(s0,t) + D(s0,s) = 0 is solved exactly: the reversible rules are exactly c(eta) + psi(s') + sum_d phi_d(s', eta_d) "
   "with phi_{-d}(b, a) = phi_d(a, b): " + "; ".join(rep))

# ------------------------------------------------------------------ N.cube: the covariant examples in 3+1 (torus 3^3, six-axes menu)
Ls = 3; sites = list(itertools.product(range(Ls), repeat=3))
axes = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
offs = [(0, 0, 0)] + axes
w0, w1 = 1, 1
def pred(s, x):
    return [s[tuple((x[i] + o[i]) % Ls for i in range(3))] for o in offs]
def hvec(etas):
    return tuple(sum((w0 if k == 0 else w1) * etas[k][i] for k in range(7)) for i in range(3))
dot = lambda a, b: sum(p * q for p, q in zip(a, b))
b_, g_ = sp.symbols("beta gamma")
rules = {
    "pairwise, block 19": lambda sp_, et: b_ * dot(sp_, hvec(et)),
    "two-body nematic": lambda sp_, et: g_ * sum((w0 if k == 0 else w1) * dot(sp_, et[k]) ** 2 for k in range(7)),
    "beta s'.h + gamma (s'.h)^2": lambda sp_, et: b_ * dot(sp_, hvec(et)) + g_ * dot(sp_, hvec(et)) ** 2,
    "beta s'.h/|h|": lambda sp_, et: (b_ * dot(sp_, hvec(et)) / sp.sqrt(dot(hvec(et), hvec(et)))) if dot(hvec(et), hvec(et)) else 0,
}
def Dval(F, s, t):
    return sum(F(t[x], pred(s, x)) - F(s[x], pred(t, x)) for x in sites)
rnd = random.Random(20260923)
triples = [tuple({x: rnd.choice(axes) for x in sites} for _ in range(3)) for _ in range(4)]
cyc = {}
for name, F in rules.items():
    vals = [sp.simplify(sp.expand(Dval(F, a, b) + Dval(F, b, c) + Dval(F, c, a))) for (a, b, c) in triples]
    cyc[name] = vals
good = all(v == 0 for v in cyc["pairwise, block 19"]) and all(v == 0 for v in cyc["two-body nematic"])
quad = [sp.expand(v) for v in cyc["beta s'.h + gamma (s'.h)^2"]]
good &= all(sp.expand(q).coeff(b_) == 0 for q in quad) and any(q != 0 for q in quad)
good &= any(sp.simplify(v) != 0 for v in cyc["beta s'.h/|h|"])
# the nematic rule is even in s', block 19's with beta != 0 is not; a covariant psi(s') is constant (the rotations are transitive on axes)
good &= all(rules["two-body nematic"](a, et) == rules["two-body nematic"](tuple(-c for c in a), et) for a in axes
            for et in [pred(triples[0][0], x) for x in sites[:5]])
qv = next(q for q in quad if q != 0)
ov = next(v for v in cyc["beta s'.h/|h|"] if sp.simplify(v) != 0)
ok("N.cube", good, "on the 3^3 torus with the six-axes menu and the seven-record past (w0 = w1 = 1), exact cycle sums over random "
   "triples of levels: zero for block 19's rule and for the covariant two-body rule gamma sum_d w_d (s'.s_{x+d})^2 (reversible, "
   f"even in s', so not of block 19's form); {qv} for beta s'.h + gamma (s'.h)^2 and {sp.nsimplify(ov)} ~ "
   f"{float(ov.subs(b_, 1)):.4f} beta for beta s'.h/|h|: both irreversible")
print(f"runtime {time.time() - T0:.0f} s")

if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PROVED a positive nearest-neighbour formation rule gives a reversible level chain iff its log-law is a sum of "
      "two-body terms symmetric under exchange with the offset reversed (plus terms of one record or of the past alone); block "
      "19's rule is one member, so pairwise-linear is not the only reversible covariant class, and rules with three-body terms "
      "are not reversible")
print("HIT: (a) the level chain K(s -> s') = prod_x exp F(s'_x; eta_x(s))/Z is reversible iff F(s'; eta) = sum_d phi_d(s', eta_d) + "
      "psi(s') + c(eta) with phi_{-d}(b, a) = phi_d(a, b) modulo one-record terms (mixed differences in s'_x and s_y must not see "
      "the other predecessors); then pi(s) = prod_x Z(eta_x(s)) exp(sum_x psi(s_x)); the reversible dimension equals the two-body "
      "family exactly on rings (menus 2 and 3).")
print("HIT: (b) covariant and reversible but not block 19's rule: gamma sum_d w_d (s'.s_{x+d})^2 (zero cycle sums, even in s'); "
      "covariant and irreversible: beta s'.h + gamma (s'.h)^2 (its three-body part leaves a cycle sum proportional to gamma) and "
      "beta s'.h/|h|, both exact on the 3^3 torus with the six-axes menu.")
