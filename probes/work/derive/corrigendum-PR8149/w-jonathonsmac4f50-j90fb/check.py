#!/usr/bin/env python3
"""Corrigendum packet for PR #8149 (block 15, the formation-unit clause witness): exact checks for ATTEMPT.md.

Definitions are block 15's (note and runner on the PR branch): six-axis menu, value index = the runner's STEPS order
(+x, -x, +y, -y, +z, -z); product rule phi(a, b) = p, q, r for equal, opposite, orthogonal values; K(b, a) = phi/Z1,
Z1 = p + q + 4r; K_k(v_A) = sum_s prod_{y in A} K(v_y, s).  Sequential law along an order:
mu_sigma(v_U | v_O) = prod_x r(v_x | v_{A_x}), r(a | {}) = 1/6, r(a | A) = prod_{y in A} K(v_y, a) / K_|A|(v_A),
A_x = recorded outside neighbours of x together with the inside neighbours formed before x.  Joint law: the product of
phi over the edges inside U and from U to the recorded outside sites, normalized (block 15's U1; the runner's joint_law).
Environments: records on any subset O' of O = N(U) \\ U (O' = O: full; O' empty: isolated).

Sections (the step numbers of ATTEMPT.md in brackets):
 C  the exact criterion [S3]: mu_sigma = mu_J iff N_sigma(v_U) = prod_{x: A_x nonempty} K_|A_x|(v_{A_x}) does not depend
    on v_U; the two-inside lemma [S4-S5] (the Lagrange identity symbolically, and on every executed case); the
    decomposition [S6]: when every site records at most one inside neighbour, equality iff every Phi_y is constant;
 D  where block 15's original criterion is also necessary [S7]: isolated units and constant environments;
 S  the failure of the original U2 'only if' and of U4 [S8]: the star, centre first, in the 216 full environments that
    are equivariant under sigma = -rho (a six-cycle on the directions), for eight rules; the full laws compared pattern
    by pattern (6^7 patterns) in two of them; the runner's executed star numbers reproduced exactly;
 L  the single-dependent lemma [S10], against every value multiset of size <= 6;
 T  the tree / growth-order lemma behind corrected U4 [S9], on every order of the executed units;
 X  facts on the corrected domain [S11]: products of d five-record leaf factors (d <= 4, and d = 5 at (3,1,2)) are never
    constant at the executed rule and two generic ones; two further counterexamples to the original 'only if'.
Exact rational / integer / symbolic arithmetic only (a modular image is used only to prove that a product is NEVER
constant: equal rationals have equal images, so no modular match means no exact match; denominators are checked prime
to the modulus).
"""
import random
import sys
import time
from fractions import Fraction as F
from itertools import combinations_with_replacement, permutations, product

import sympy as sp

M = 6
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
IDX = {d: i for i, d in enumerate(STEPS)}
FAILS = []
T0 = time.time()


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


def rel(a, b):
    return 0 if a == b else (1 if a // 2 == b // 2 else 2)      # equal (p), opposite (q), orthogonal (r)


class Rule:
    def __init__(self, p, q, r):
        self.p, self.q, self.r = p, q, r
        self.w = (p, q, r)
        self.Z1 = p + q + 4 * r
        self.phi = [[self.w[rel(a, b)] for b in range(M)] for a in range(M)]
        self.K = [[F(self.phi[a][s], self.Z1) for s in range(M)] for a in range(M)]
        self._kk = {}
        self._cond = {}

    def __repr__(self):
        return f"({self.p},{self.q},{self.r})"

    def Kk(self, vals):
        key = tuple(sorted(vals))
        if key not in self._kk:
            tot = F(0)
            for s in range(M):
                t = F(1)
                for v in key:
                    t *= self.K[v][s]
                tot += t
            self._kk[key] = tot
        return self._kk[key]

    def cond(self, rec, s):
        key = (rec, s)
        if key not in self._cond:
            if not rec:
                self._cond[key] = F(1, M)
            else:
                num = F(1)
                for v in rec:
                    num *= self.K[v][s]
                self._cond[key] = num / self.Kk(rec)
        return self._cond[key]

    def KH(self, outs):
        """(K H)(a) for H(s) = prod_{v in outs} K(v, s): the factor a dependent contributes (a = the inside value)."""
        return tuple(self.Kk((a,) + tuple(outs)) for a in range(M))


def nbrs(x):
    return [(x[0] + d[0], x[1] + d[1], x[2] + d[2]) for d in STEPS]


def outside(U):
    S = set(U)
    return sorted({y for x in U for y in nbrs(x) if y not in S})


def records(U, env, order):
    """per site in order: (position index, inside earlier neighbour indices, recorded outside values)"""
    pos = {x: i for i, x in enumerate(U)}
    done, out = set(), []
    for x in order:
        ins = [pos[y] for y in nbrs(x) if y in pos and y in done]
        outs = [env[y] for y in nbrs(x) if y in env]
        out.append((pos[x], ins, outs))
        done.add(x)
    return out


def seq_law(U, env, order, R):
    recs = records(U, env, order)
    law = {}
    for v in product(range(M), repeat=len(U)):
        pr = F(1)
        for xi, ins, outs in recs:
            pr *= R.cond(tuple(sorted([v[j] for j in ins] + outs)), v[xi])
        law[v] = pr
    return law


def joint_law(U, env, R):
    pos = {x: i for i, x in enumerate(U)}
    inner = [(pos[x], pos[y]) for x in U for y in nbrs(x) if y in pos and pos[y] > pos[x]]
    outer = [(pos[x], env[y]) for x in U for y in nbrs(x) if y in env]
    w = {}
    for v in product(range(M), repeat=len(U)):
        t = 1
        for i, j in inner:
            t *= R.phi[v[i]][v[j]]
        for i, b in outer:
            t *= R.phi[v[i]][b]
        w[v] = t
    Z = sum(w.values())
    return {v: F(t, Z) for v, t in w.items()}


def seq_law_and_N(U, env, order, R):
    """the sequential law and, from the same recorded sets, the set of values of N_sigma(v) = prod_{A_x nonempty} K_|A_x|(v_{A_x})"""
    recs = records(U, env, order)
    law, Nvals = {}, set()
    for v in product(range(M), repeat=len(U)):
        pr, nn = F(1), F(1)
        for xi, ins, outs in recs:
            rec = tuple(sorted([v[j] for j in ins] + outs))
            pr *= R.cond(rec, v[xi])
            if rec:
                nn *= R.Kk(rec)
        law[v] = pr
        Nvals.add(nn)
    return law, Nvals


def structure(U, env, order, R):
    """(i) = no site records two inside neighbours; Phi_y for every y; the original criterion of block 15"""
    recs = records(U, env, order)
    cond_i = all(len(ins) <= 1 for _, ins, _ in recs)
    original = all(not (ins and len(ins) + len(outs) >= 2) for _, ins, outs in recs)
    phis = {}
    for xi, ins, outs in recs:
        if len(ins) == 1 and outs:
            y = ins[0]
            f = R.KH(outs)
            phis[y] = tuple(a * b for a, b in zip(phis.get(y, (F(1),) * M), f))
    phi_const = all(len(set(v)) == 1 for v in phis.values())
    return cond_i, phi_const, original, phis


def is_constant_env(env):
    return len(set(env.values())) <= 1


# ------------------------------------------------------------------------------------------ the executed units
UNITS = {
    "single": [(0, 0, 0)],
    "domino": [(0, 0, 0), (1, 0, 0)],
    "path3": [(-1, 0, 0), (0, 0, 0), (1, 0, 0)],
    "bent3": [(1, 0, 0), (0, 0, 0), (0, 1, 0)],
    "plaquette": [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)],
    "Tclaw": [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0)],
    "cornerclaw": [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)],
    "path4": [(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0)],
}
RULES = [Rule(3, 1, 2), Rule(5, 1, 2), Rule(7, 2, 3), Rule(2, 2, 1), Rule(4, 1, 2), Rule(1, 3, 2), Rule(2, 1, 1), Rule(1, 1, 2)]
R312, R512, R723, R221, R412 = RULES[0], RULES[1], RULES[2], RULES[3], RULES[4]


# ============================================================================================ section C / D
def section_CD():
    print("=" * 100)
    print("C/D  the exact criterion, the two-inside lemma, the decomposition, and the domain of the original criterion")
    # C-sym: the Lagrange identity behind the two-inside lemma, symbolically
    p, q, r = sp.symbols("p q r", positive=True)
    d = sp.symbols("d0:6", positive=True)
    Z = p + q + 4 * r
    w = (p, q, r)
    K = [[w[rel(a, s)] / Z for s in range(M)] for a in range(M)]
    a, c = 0, 2                                       # +x and +y: an orthogonal pair
    G = lambda u, v: sum(K[u][s] * K[v][s] * d[s] for s in range(M))
    lhs = G(a, a) * G(c, c) - G(a, c) ** 2
    rhs = sp.Rational(1, 2) * sum(d[s] * d[t] * (K[a][s] * K[c][t] - K[a][t] * K[c][s]) ** 2 for s in range(M) for t in range(M))
    lag = sp.expand(lhs - rhs) == 0
    t_ac = sp.simplify(K[a][a] * K[c][c] - K[a][c] * K[c][a] - (p ** 2 - r ** 2) / Z ** 2) == 0
    t_aa = sp.simplify(K[a][a] * K[c][1] - K[a][1] * K[c][a] - r * (p - q) / Z ** 2) == 0
    check("C-sym", lag and t_ac and t_aa,
          "Lagrange identity (KDK)_aa (KDK)_cc - (KDK)_ac^2 = 1/2 sum_{s,t} d_s d_t (K_as K_ct - K_at K_cs)^2 for a = +x, c = +y "
          "(symbolic in p, q, r, d_0..d_5); its (s,t) = (a,c) and (a,-a) brackets are (p^2 - r^2)/Z1^2 and r(p - q)/Z1^2, "
          "so the minor is > 0 for every positive diagonal D unless p = q = r")
    rng = random.Random(20260919)
    stats = dict(cases=0, eq=0, orig_fail=0, not_i=0)
    bad = {"C1": 0, "C3": 0, "C5": 0, "D-suff": 0, "D-nec": 0}
    orig_fail_cases = []
    for R in (R312, R512, R221):
        for name, U in UNITS.items():
            O = outside(U)
            envs = [("isolated", {}), ("const+x", {y: 0 for y in O}), ("const-z", {y: 5 for y in O})]
            for k in range(2):
                envs.append((f"randfull{k}", {y: rng.randrange(M) for y in O}))
            for k in range(2):
                envs.append((f"randpart{k}", {y: rng.randrange(M) for y in O if rng.random() < 0.5}))
            for ename, env in envs:
                J = joint_law(U, env, R)
                for order in permutations(U):
                    L, Ns = seq_law_and_N(U, env, order, R)
                    eq = all(L[v] == J[v] for v in L)
                    ci, pc, orig, _ = structure(U, env, order, R)
                    stats["cases"] += 1
                    stats["eq"] += eq
                    stats["not_i"] += not ci
                    bad["C1"] += eq != (len(Ns) == 1)
                    bad["C3"] += (len(Ns) == 1) != (ci and pc)
                    bad["C5"] += (not ci) and eq
                    bad["D-suff"] += orig and not eq
                    if ename == "isolated" or is_constant_env(env):
                        bad["D-nec"] += eq != orig
                    if eq and not orig:
                        stats["orig_fail"] += 1
                        orig_fail_cases.append((repr(R), name, ename, order))
    check("C1", bad["C1"] == 0, f"equality of the laws (all patterns, exact) iff N_sigma constant: {stats['cases']} cases (8 units, 7 environments "
          f"incl. partial ones, every order, rules (3,1,2), (5,1,2), (2,2,1)), {bad['C1']} mismatches; {stats['eq']} equal")
    check("C3", bad["C3"] == 0, f"N_sigma constant iff [(i) no site records two inside neighbours and every Phi_y constant]: {bad['C3']} mismatches")
    check("C5", bad["C5"] == 0, f"every case violating (i) differs from the joint law: {stats['not_i']} such cases, {bad['C5']} equal")
    check("D-suff", bad["D-suff"] == 0, f"block 15's criterion is sufficient in every executed environment: {bad['D-suff']} exceptions")
    check("D-nec", bad["D-nec"] == 0, f"isolated and constant environments: equality iff block 15's criterion: {bad['D-nec']} exceptions")
    print(f"     original 'only if' failures met among these cases (equal although the criterion is violated): {stats['orig_fail']}"
          + (f", e.g. {orig_fail_cases[:3]}" if orig_fail_cases else ""))
    return stats, orig_fail_cases


# ============================================================================================ section S
def sigma_pos(x):
    return (-x[2], -x[0], -x[1])        # sigma = -rho, rho(x, y, z) = (z, x, y)


SIG_VAL = [IDX[sigma_pos(STEPS[i])] for i in range(M)]
CENTER = (0, 0, 0)
LEAVES = nbrs(CENTER)
STAR = [CENTER] + LEAVES
STAR_O = outside(STAR)


def equivariant_envs():
    orbits, seen = [], set()
    for o in STAR_O:
        if o in seen:
            continue
        orb = [o]
        while True:
            nx = sigma_pos(orb[-1])
            if nx == o:
                break
            orb.append(nx)
        seen |= set(orb)
        orbits.append(orb)
    envs = []
    for vals in product(range(M), repeat=len(orbits)):
        env = {}
        for orb, v in zip(orbits, vals):
            for k, site in enumerate(orb):
                env[site] = v
                v = SIG_VAL[v]
        envs.append(env)
    return orbits, envs


def star_phi(env, R):
    phi = (F(1),) * M
    for e in LEAVES:
        outs = [env[y] for y in nbrs(e) if y in env]
        phi = tuple(a * b for a, b in zip(phi, R.KH(outs)))
    return phi


def dec(x, n=5):
    s = x.numerator * 10 ** n // x.denominator
    return f"{s // 10 ** n}.{str(s % 10 ** n).zfill(n)}"


def section_S():
    print("=" * 100)
    print("S  the failure of block 15's U2 'only if' and U4: the star, centre first, sigma-equivariant full environments")
    six_cycle = sorted(_cycle(SIG_VAL, 0)) == list(range(M))
    orbits, envs = equivariant_envs()
    free = all(len(o) == 6 for o in orbits) and len(orbits) == 3 and sum(len(o) for o in orbits) == 18 == len(STAR_O)
    rel_inv = all(rel(SIG_VAL[a], SIG_VAL[b]) == rel(a, b) for a in range(M) for b in range(M))
    check("S0", six_cycle and free and rel_inv and len(envs) == 216,
          "sigma = -rho acts on the six values as one six-cycle, preserves equal/opposite/orthogonal, and acts freely on the "
          "star's 18 outside sites (3 orbits of 6): 6^3 = 216 equivariant full environments")
    order = [CENTER] + LEAVES
    per_rule = []
    for R in RULES:
        n_const = 0
        viol = True
        for env in envs:
            ph = star_phi(env, R)
            n_const += len(set(ph)) == 1
            ci, pc, orig, _ = structure(STAR, env, order, R)
            viol = viol and ci and pc and not orig
        per_rule.append((repr(R), n_const))
        check(f"S1 {R}", n_const == 216 and viol,
              f"all 216 equivariant environments: Phi_centre = prod over the six leaves of (K H_leaf) is constant ({n_const}/216), "
              f"(i) holds and every leaf records the centre with five outside records (block 15's criterion violated): {viol}")
    # full-law comparison, every one of the 6^7 patterns, in two of the environments at two rules
    for R, k in ((R312, 0), (R512, 137)):
        env = envs[k]
        t = time.time()
        L = seq_law(STAR, env, order, R)
        J = joint_law(STAR, env, R)
        eq = all(L[v] == J[v] for v in L)
        check(f"S2 {R} env#{k}", eq, f"sequential (centre first) and joint laws equal on all {len(L)} patterns ({time.time() - t:.0f}s)")
    # a leaf-first order in the same environment still differs (two inside neighbours at the centre)
    env = envs[0]
    lf = LEAVES + [CENTER]
    ci, pc, orig, _ = structure(STAR, env, lf, R312)
    check("S3", not ci, "the leaves-first order in the same environment: the centre records six inside neighbours, so (i) fails and it differs")
    # the runner's executed star numbers (all+x and its seeded mixed environment, centre first) from the centre-marginal
    # formula TV = 1/2 sum_a |1/6 - Phi(a)/sum Phi|; the formula checked against a full enumeration on the claws first
    ok_formula = True
    for name in ("Tclaw", "cornerclaw"):
        U = UNITS[name]
        O = outside(U)
        rng = random.Random(7)
        for _ in range(2):
            env2 = {y: rng.randrange(M) for y in O}
            L = seq_law(U, env2, U, R312)             # U[0] is the centre: centre first
            J = joint_law(U, env2, R312)
            tv_brute = sum((abs(L[v] - J[v]) for v in L), F(0)) / 2
            ph = (F(1),) * M
            for e in U[1:]:
                outs = [env2[y] for y in nbrs(e) if y in env2]
                ph = tuple(a * b for a, b in zip(ph, R312.KH(outs)))
            s = sum(ph)
            # the centre's own outside records enter only through an order-independent factor of both laws
            outs_c = [env2[y] for y in nbrs(U[0]) if y in env2]
            hc = tuple(F(1) for _ in range(M))
            if outs_c:
                hc = tuple(_prodK(R312, outs_c, a) for a in range(M))
            w_seq = [R312.cond(tuple(sorted(outs_c)), a) for a in range(M)]
            w_joint = [hc[a] * ph[a] for a in range(M)]
            zj = sum(w_joint)
            tv_formula = sum((abs(w_seq[a] - w_joint[a] / zj) for a in range(M)), F(0)) / 2
            ok_formula = ok_formula and tv_brute == tv_formula
    vO_allx = {y: 0 for y in STAR_O}
    random.seed(3)
    vO_mixed = {y: random.randrange(M) for y in STAR_O}
    tvs = {}
    for nm, env2 in (("all+x", vO_allx), ("mixed", vO_mixed)):
        ph = star_phi(env2, R312)
        s = sum(ph)
        tvs[nm] = sum((abs(F(1, 6) - x / s) for x in ph), F(0)) / 2
    runner = {"all+x": "0.40289", "mixed": "0.14626"}
    check("S4", ok_formula and all(dec(tvs[k]) == runner[k] for k in runner),
          f"centre-first TV = TV of the centre marginals (checked by full enumeration on the two claws); the runner's cached star values "
          f"reproduced exactly: all+x/k=0 {dec(tvs['all+x'])} = {tvs['all+x']}, mixed/k=0 {dec(tvs['mixed'])} (runner: 0.40289, 0.14626)")
    return per_rule, tvs


def _cycle(perm, start):
    out, x = [start], perm[start]
    while x != start:
        out.append(x)
        x = perm[x]
    return out


def _prodK(R, outs, a):
    t = F(1)
    for v in outs:
        t *= R.K[v][a]
    return t


# ============================================================================================ section L
def predicted_constant(ms, R):
    npl = [sum(1 for v in ms if v == 2 * i) for i in range(3)]
    nmi = [sum(1 for v in ms if v == 2 * i + 1) for i in range(3)]
    p, q, r = R.p, R.q, R.r
    if p != q:
        if any(npl[i] != nmi[i] for i in range(3)):
            return False
        if p + q - 2 * r == 0 or p * q == r * r:
            return True
        return npl[0] == npl[1] == npl[2]
    ax = [npl[i] + nmi[i] for i in range(3)]
    return ax[0] == ax[1] == ax[2]


def section_L():
    print("=" * 100)
    print("L  the single-dependent lemma: when is one factor (K H)(a) constant in a")
    tot = mism = 0
    counts = {}
    for R in RULES:
        for m in range(1, 7):
            n_c = 0
            for ms in combinations_with_replacement(range(M), m):
                c = len(set(R.KH(ms))) == 1
                tot += 1
                mism += c != predicted_constant(ms, R)
                n_c += c
            counts[(repr(R), m)] = n_c
    check("L1", mism == 0, f"(K H) constant iff [p != q: the values are balanced on every axis, and if (p+q-2r)(pq-r^2) != 0 the three axes "
          f"carry equal counts] / [p = q: equal axis counts]: every multiset of size 1..6 at eight rules ({tot} cases), {mism} mismatches")
    five = all(counts[(repr(R), 5)] == 0 for R in RULES)
    check("L2", five, "no factor with five outside records is ever constant (every rule): a site whose only dependent is a leaf of a "
          "full environment separates the readings")
    print("     constant single factors by size m = 1..6: " + "; ".join(
        f"{repr(R)}: " + ",".join(str(counts[(repr(R), m)]) for m in range(1, 7)) for R in RULES))
    return counts


# ============================================================================================ section T
def is_tree(U):
    S = set(U)
    edges = sum(1 for x in U for y in nbrs(x) if y in S) // 2
    return edges == len(U) - 1


def section_T():
    print("=" * 100)
    print("T  the tree / growth-order lemma: in a full environment (i) holds iff the unit is a tree and the order a growth order")
    bad = 0
    n = 0
    for name, U in UNITS.items():
        if len(U) < 2:
            continue
        env = {y: 0 for y in outside(U)}
        for order in permutations(U):
            ci, _, _, _ = structure(U, env, order, R312)
            done, growth = set(), True
            for i, x in enumerate(order):
                if i and not any(y in done for y in nbrs(x)):
                    growth = False
                done.add(x)
            bad += ci != (is_tree(U) and growth)
            n += 1
    check("T1", bad == 0, f"{n} (unit, order) pairs over seven connected units: {bad} mismatches")


# ============================================================================================ section X
P_MOD = (1 << 61) - 1


def norm_vec(v):
    return tuple(x / v[0] for x in v[1:])


def section_X():
    print("=" * 100)
    print("X  the corrected domain at the executed rule; two further counterexamples to the original 'only if'")
    ms5 = list(combinations_with_replacement(range(M), 5))
    res = {}
    for R in (R312, R512, R723):
        vecs = sorted({norm_vec(R.KH(ms)) for ms in ms5})
        vset = set(vecs)
        inv = lambda v: tuple(1 / x for x in v)
        mul = lambda u, v: tuple(x * y for x, y in zip(u, v))
        d1 = sum(1 for v in vecs if all(x == 1 for x in v))
        d2 = sum(1 for v in vecs if inv(v) in vset)
        d3 = 0
        for i, v1 in enumerate(vecs):
            for v2 in vecs[i:]:
                d3 += inv(mul(v1, v2)) in vset
        pairs = {}
        for i, v1 in enumerate(vecs):
            for v2 in vecs[i:]:
                pairs.setdefault(mul(v1, v2), 0)
        d4 = sum(1 for k in pairs if inv(k) in pairs)
        res[repr(R)] = (d1, d2, d3, d4)
    check("X1", all(v == (0, 0, 0, 0) for v in res.values()),
          "no product of d = 1, 2, 3, 4 five-record leaf factors is constant at (3,1,2), (5,1,2), (7,2,3) (every value multiset): "
          + str(res))
    # d = 5 at the executed rule, by modular images (a match is necessary for an exact match)
    t = time.time()
    fv = [R312.KH(ms) for ms in ms5]
    nv = [norm_vec(v) for v in fv]
    assert all(x.denominator % P_MOD and x.numerator % P_MOD for v in nv for x in v)
    mv = [tuple(x.numerator % P_MOD * pow(x.denominator, P_MOD - 2, P_MOD) % P_MOD for x in v) for v in nv]
    n = len(mv)
    mm = lambda u, v: tuple(x * y % P_MOD for x, y in zip(u, v))
    pairs = set()
    for i in range(n):
        for j in range(i, n):
            pairs.add(mm(mv[i], mv[j]))
    hits5 = 0
    for i in range(n):
        for j in range(i, n):
            mij = mm(mv[i], mv[j])
            for k in range(j, n):
                key = mm(mij, mv[k])
                if tuple(pow(x, P_MOD - 2, P_MOD) for x in key) in pairs:
                    hits5 += 1
    check("X2", hits5 == 0, f"no product of five five-record leaf factors is constant at (3,1,2) (all {n}^5 multiset choices; "
          f"{time.time() - t:.0f}s): the star's one-leaf-first order separates in every full environment at the executed rule")
    # consequences at the executed rule, from S10/L2/X1/X2 and the tree lemma (every full environment):
    #   domino, the two paths of three, both claws, the straight path of four: separate under every order;
    #   the star: separates under every order except centre first, where the 216 environments of S1 agree.
    # two further counterexamples to the original 'only if'
    dom = UNITS["domino"]
    env = {(2, 0, 0): 2, (1, 1, 0): 3}          # the second site sees +y and -y outside: a partial environment
    order = [(0, 0, 0), (1, 0, 0)]
    e312 = _same(seq_law(dom, env, order, R312), joint_law(dom, env, R312))
    e512 = _same(seq_law(dom, env, order, R512), joint_law(dom, env, R512))
    _, _, orig, _ = structure(dom, env, order, R312)
    check("X3", e312 and not e512 and not orig,
          "partial environment: the domino formed left then right, the right site recording its left neighbour with two outside "
          f"records +y, -y: equal to the joint law at (3,1,2) [{e312}], different at (5,1,2) [{not e512}]; block 15's criterion is violated")
    p3 = UNITS["path3"]
    env = {y: 0 for y in outside(p3)}
    left = [y for y in nbrs((-1, 0, 0)) if y not in set(p3)]
    right = [y for y in nbrs((1, 0, 0)) if y not in set(p3)]
    for y, v in zip(left, (0, 0, 1, 2, 4)):
        env[y] = v
    for y, v in zip(right, (0, 1, 1, 3, 5)):
        env[y] = v
    order = [(0, 0, 0), (-1, 0, 0), (1, 0, 0)]
    eq412 = _same(seq_law(p3, env, order, R412), joint_law(p3, env, R412))
    eq312 = _same(seq_law(p3, env, order, R312), joint_law(p3, env, R312))
    _, _, orig, _ = structure(p3, env, order, R412)
    check("X4", eq412 and not eq312 and not orig,
          "full environment: the straight path of three, middle first, leaves seeing {+x,+x,-x,+y,+z} and {+x,-x,-x,-y,-z}: equal to the "
          f"joint law at (4,1,2) (pq = r^2) [{eq412}], different at (3,1,2) [{not eq312}]; block 15's criterion is violated")
    return res


def _same(a, b):
    return a.keys() == b.keys() and all(a[v] == b[v] for v in a)


def main():
    stats, fails_cd = section_CD()
    per_rule, tvs = section_S()
    counts = section_L()
    section_T()
    res = section_X()
    print("=" * 100)
    print(f"runtime {time.time() - T0:.0f}s")
    summary_core = ("corrected U2: mu_sigma = mu_joint iff the normalizer product N_sigma is constant in v_U; a site recording two inside "
                    "neighbours always separates (Lagrange minor > 0); otherwise equality iff every Phi_y = prod_{dependents} (K H_x) is constant; "
                    "block 15's criterion is sufficient everywhere and necessary for isolated units and constant environments; corrected U4: "
                    "in a full environment a connected unit with >= 2 sites agrees under sigma iff it is a tree, sigma a growth order and every "
                    "Phi_y constant")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({len(FAILS)} failing checks: {FAILS})")
        return 0
    print(f"SUMMARY: executed cases {stats['cases']} (C1/C3/C5/D exact, 0 mismatches); star centre first equal to its joint law in 216/216 "
          f"sigma-equivariant full environments at {len(per_rule)} rules (full-law equality on 6^7 patterns in two); single-factor lemma, "
          f"tree lemma, and at (3,1,2) no product of 1-5 five-record leaf factors constant")
    print("SUMMARY: PROVED (ATTEMPT.md S1-S11, finite facts CHECKED here) " + summary_core
          + "; COUNTEREXAMPLE to block 15's U2 'only if' and U4 as stated: the star, centre first, in the 216 sigma-equivariant full "
          "environments, every rule")
    print("HIT: corrigendum for PR #8149 — " + summary_core + "; the original U2 'only if' and U4 fail for the centre-first star in "
          "every sigma-equivariant full environment (216, every non-constant rule), at (3,1,2) for a partial-environment domino, and at "
          "(4,1,2) for the middle-first path of three")
    return 0


if __name__ == "__main__":
    sys.exit(main())
