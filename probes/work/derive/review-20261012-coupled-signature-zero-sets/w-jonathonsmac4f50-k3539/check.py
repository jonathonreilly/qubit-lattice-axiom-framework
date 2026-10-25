#!/usr/bin/env python3
"""Coupled-signature quadratic zero sets: the 72 unresolved unequal+unequal pairs.

Disjoint exact re-implementation (shares no code with the source runner).

Setting (all supplied, see ATTEMPT.md):
  proper cubic group G (24 rotations); alphabet = G-orbit of (1,2,3) (24 points);
  uniform one-site law r0 (forced by G-invariance + transitivity);
  soldered bond factors phi_d(a,b) = 1 + L_d(a,b), L_{gd}(ga,gb) = L_d(a,b),
  L_d(a,b) = L_{-d}(b,a), slice sums sum_a L_d(a,b) = 0;
  L supported on the bonds of two height signatures (S,T), coordinates x in Q^6.
  Necessary conditions for order-blindness (parent Theorem 2): the pair moments
  sum_a L_d(a,b) L_e(a,c) = 0 for all d != e, b, c  (full symmetric product).

Question: do the pair moments force x = 0 for the 72 pairs left open by the
linear monomial test?  Answer certified here: yes (degree-3 Nullstellensatz).

Only numpy, scipy, sympy and the standard library are used.  Exact arithmetic
(Fraction) for every finite claim; sympy Groebner bases as a second exact route;
scipy multi-start minimisation as a (non-rigorous) floating-point cross-check.
"""
import itertools
import random
import sys
import time
from fractions import Fraction as Fr

T0 = time.time()
PASS = 0
FAIL = 0


def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print("PASS " + name)
    else:
        FAIL += 1
        print("FAIL " + name)


def note(s):
    print("# " + s)


# ----------------------------------------------------------------------------
# 1. group, alphabet, bonds, signatures
# ----------------------------------------------------------------------------
def perm_sign(p):
    s = 1
    p = list(p)
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s = -s
    return s


GROUP = []
for p in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        if perm_sign(p) * sg[0] * sg[1] * sg[2] == 1:
            M = [[0] * 3 for _ in range(3)]
            for j in range(3):
                M[p[j]][j] = sg[j]
            GROUP.append(tuple(tuple(r) for r in M))


def act(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def neg(v):
    return tuple(-t for t in v)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


ORBIT = sorted({act(M, (1, 2, 3)) for M in GROUP})
DIRS = [tuple(s if k == ax else 0 for k in range(3)) for ax in range(3) for s in (1, -1)]
check("proper cubic group has 24 elements; orbit of (1,2,3) has 24 points; 6 directions",
      len(GROUP) == 24 and len(ORBIT) == 24 and len(DIRS) == 6)
check("G acts freely on the alphabet (uniform r0 forced by invariance)",
      all(len({act(M, p) for M in GROUP}) == 24 for p in ORBIT[:3]))

# ordered bond orbits under G, then identification by reversal (d,a,b)~(-d,b,a)
OID = {}
n_ord = 0
for d in DIRS:
    for a in ORBIT:
        for b in ORBIT:
            if (d, a, b) in OID:
                continue
            for M in GROUP:
                OID[(act(M, d), act(M, a), act(M, b))] = n_ord
            n_ord += 1
REVC = {}
CLS = {}
n_cls = 0
for k in range(n_ord):
    REVC[k] = None
for (d, a, b), k in OID.items():
    REVC[k] = OID[(neg(d), b, a)]
for k in range(n_ord):
    if k in CLS:
        continue
    CLS[k] = n_cls
    CLS[REVC[k]] = n_cls
    n_cls += 1
BOND_CLASS = {key: CLS[k] for key, k in OID.items()}  # (d,a,b) -> unordered bond class
check("144 ordered bond orbits, 84 bond classes after reversal", n_ord == 144 and n_cls == 84)


def signature(d, a, b):
    f = (dot(a, d), dot(b, d))
    r = (-f[1], -f[0])
    return min(f, r)


SIG_OF_CLASS = {}
for (d, a, b), k in BOND_CLASS.items():
    s = signature(d, a, b)
    if k in SIG_OF_CLASS:
        assert SIG_OF_CLASS[k] == s
    SIG_OF_CLASS[k] = s
SIGS = sorted(set(SIG_OF_CLASS.values()))
OPP = [s for s in SIGS if s[0] == -s[1]]
EQ = [s for s in SIGS if s[0] == s[1]]
UNEQ = [s for s in SIGS if s[0] != -s[1] and s[0] != s[1]]
check("21 height signatures: 6 opposite, 3 equal, 12 unequal; 4 bond classes each",
      len(SIGS) == 21 and (len(OPP), len(EQ), len(UNEQ)) == (6, 3, 12)
      and all(sum(1 for k in SIG_OF_CLASS if SIG_OF_CLASS[k] == s) == 4 for s in SIGS))


# ----------------------------------------------------------------------------
# 2. exact linear algebra helpers (Fractions)
# ----------------------------------------------------------------------------
def rref(rows, ncols):
    """Reduced row echelon form; returns (rows, pivots)."""
    m = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(m)) if m[i][c] != 0), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        s = m[r][c]
        m[r] = [v / s for v in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [x - f * y for x, y in zip(m[i], m[r])]
        piv.append(c)
        r += 1
        if r == len(m):
            break
    return m[:r], piv


def nullspace(rows, ncols):
    R, piv = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for f in free:
        v = [Fr(0)] * ncols
        v[f] = Fr(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][f]
        out.append(v)
    return out, len(piv)


# slice rows: for each (d,b): sum over a of L_d(a,b) = 0   (as rows on bond classes)
SLICE_ROWS = set()
for d in DIRS:
    for b in ORBIT:
        row = [0] * n_cls
        for a in ORBIT:
            row[BOND_CLASS[(d, a, b)]] += 1
        SLICE_ROWS.add(tuple(row))

KER = {}      # signature -> list of 3 vectors over bond classes
for s in SIGS:
    cols = [k for k in range(n_cls) if SIG_OF_CLASS[k] == s]
    rows = [[Fr(r[c]) for c in cols] for r in SLICE_ROWS if any(r[c] for c in cols)]
    ns, rk = nullspace(rows, len(cols))
    assert rk == 1 and len(ns) == 3, (s, rk, len(ns))
    vecs = []
    for v in ns:
        full = [Fr(0)] * n_cls
        for i, c in enumerate(cols):
            full[c] = v[i]
        vecs.append(full)
    KER[s] = vecs
check("each signature: slice-row rank 1, kernel dimension 3 (rational basis)", all(len(KER[s]) == 3 for s in SIGS))

# sanity on a random kernel element: covariance, bond symmetry, slice sums
rng = random.Random(20261012)
def rand_fr():
    return Fr(rng.randint(-9, 9), rng.randint(1, 5))

ok_cov = ok_sym = ok_slice = True
for s in SIGS[:7]:
    co = [rand_fr() for _ in range(3)]
    Lf = lambda d, a, b: sum(c * KER[s][i][BOND_CLASS[(d, a, b)]] for i, c in enumerate(co))
    for d in DIRS:
        for a in ORBIT[:6]:
            for b in ORBIT[:6]:
                if Lf(d, a, b) != Lf(neg(d), b, a):
                    ok_sym = False
                for M in GROUP[:6]:
                    if Lf(act(M, d), act(M, a), act(M, b)) != Lf(d, a, b):
                        ok_cov = False
    for d in DIRS:
        for b in ORBIT:
            if sum(Lf(d, a, b) for a in ORBIT) != 0:
                ok_slice = False
check("kernel elements are soldered (covariant), bond-symmetric, slice-zero (samples, exact)",
      ok_cov and ok_sym and ok_slice)


# ----------------------------------------------------------------------------
# 3. pair-moment quadrics for a support of signatures
# ----------------------------------------------------------------------------
def lin_vec(sigs, d, a, b):
    """Coefficient vector of L_d(a,b) over the 3*len(sigs) kernel coordinates."""
    k = BOND_CLASS[(d, a, b)]
    out = []
    for s in sigs:
        for v in KER[s]:
            out.append(v[k] if SIG_OF_CLASS[k] == s else Fr(0))
    return out


def raw_moment_rows(sigs, symmetric=True):
    """dict (d,e,b,c) -> {(i,j): coeff}  of sum_a L_d(a,b) L_e(a,c); i<=j.
    symmetric=False is a MUTANT that drops the second cross coefficient."""
    nv = 3 * len(sigs)
    near = {}  # (a, d) -> list of (b, vec) with nonzero vec
    for a in ORBIT:
        for d in DIRS:
            lst = []
            for b in ORBIT:
                v = lin_vec(sigs, d, a, b)
                if any(v):
                    lst.append((b, v))
            near[(a, d)] = lst
    rows = {}
    for i1, d in enumerate(DIRS):
        for e in DIRS[i1 + 1:]:
            for a in ORBIT:
                for b, l in near[(a, d)]:
                    for c, r in near[(a, e)]:
                        row = rows.setdefault((d, e, b, c), {})
                        for i in range(nv):
                            if l[i] == 0:
                                continue
                            for j in range(nv):
                                if r[j] == 0:
                                    continue
                                if not symmetric and i > j:
                                    continue
                                key = (min(i, j), max(i, j))
                                row[key] = row.get(key, Fr(0)) + l[i] * r[j]
    return rows


def span_basis(rows, nv):
    """Reduced basis (list of quadric dicts) of the span of the given quadric dicts."""
    mono = [(i, j) for i in range(nv) for j in range(i, nv)]
    mi = {t: q for q, t in enumerate(mono)}
    uniq = set()
    vecs = []
    for row in rows.values():
        v = [Fr(0)] * len(mono)
        for t, c in row.items():
            v[mi[t]] = c
        if any(v):
            tv = tuple(v)
            if tv not in uniq:
                uniq.add(tv)
                vecs.append(v)
    R, piv = rref(vecs, len(mono))
    return [{mono[q]: c for q, c in enumerate(r) if c != 0} for r in R], mono


def quad_to_poly(qd):
    """quadric dict {(i,j):c} -> polynomial dict {exponent tuple:c} in 6 variables."""
    p = {}
    for (i, j), c in qd.items():
        e = [0] * 6
        e[i] += 1
        e[j] += 1
        p[tuple(e)] = p.get(tuple(e), Fr(0)) + c
    return p


QUAD_CACHE = {}


def quadrics(S, T, symmetric=True):
    key = (S, T, symmetric)
    if key not in QUAD_CACHE:
        rows = raw_moment_rows([S, T], symmetric)
        basis, _ = span_basis(rows, 6)
        QUAD_CACHE[key] = (basis, rows)
    return QUAD_CACHE[key]


def eval_quad(qd, x):
    return sum(c * x[i] * x[j] for (i, j), c in qd.items())


# brute-force check of the assembled moment polynomials against direct evaluation
def brute_moment(sigs, x, d, e, b, c):
    def Lv(dd, a, bb):
        k = BOND_CLASS[(dd, a, bb)]
        t = Fr(0)
        for si, s in enumerate(sigs):
            if SIG_OF_CLASS[k] == s:
                for ki in range(3):
                    t += x[3 * si + ki] * KER[s][ki][k]
        return t
    return sum(Lv(d, a, b) * Lv(e, a, c) for a in ORBIT)


def assembly_matches_bruteforce(S, T, symmetric=True, trials=6):
    rows = raw_moment_rows([S, T], symmetric)
    keys = list(rows)
    rr = random.Random(hash((S, T)) & 0xFFFF)
    good = True
    for _ in range(trials):
        x = [Fr(rr.randint(-5, 5), rr.randint(1, 3)) for _ in range(6)]
        for key in rr.sample(keys, min(25, len(keys))):
            d, e, b, c = key
            val = eval_quad(rows[key], x)
            if val != brute_moment([S, T], x, d, e, b, c):
                good = False
    return good


check("assembled pair-moment polynomials = direct lattice sums at random rational points (unequal pairs)",
      all(assembly_matches_bruteforce(S, T) for S, T in [((-3, -2), (-3, -1)), ((-3, -1), (-2, 1)), ((2, -3), (-1, -3))]))
check("MUTANT: dropping the second symmetric cross coefficient is caught by that same check",
      not assembly_matches_bruteforce((-3, -2), (-3, -1), symmetric=False))


# ----------------------------------------------------------------------------
# 4. the 240 ordered pairs: linear (monomial) test, replicated independently
# ----------------------------------------------------------------------------
def linear_squares_forced(S, T, symmetric=True):
    """Are x0^2,x1^2,x2^2 in the linear span of the pair-moment quadrics?"""
    basis, _ = quadrics(S, T, symmetric)
    mono = [(i, j) for i in range(6) for j in range(i, 6)]
    mi = {t: q for q, t in enumerate(mono)}
    vecs = []
    for qd in basis:
        v = [Fr(0)] * len(mono)
        for t, c in qd.items():
            v[mi[t]] = c
        vecs.append(v)
    R, piv = rref(vecs, len(mono))
    for i in range(3):
        e = [Fr(0)] * len(mono)
        e[mi[(i, i)]] = Fr(1)
        # reduce e by R
        for r, pc in zip(R, piv):
            if e[pc] != 0:
                f = e[pc]
                e = [x - f * y for x, y in zip(e, r)]
        if any(e):
            return False
    return True


t1 = time.time()
CERT_LINEAR = []
UNRESOLVED = []
for S in UNEQ:
    for T in SIGS:
        if T == S:
            continue
        if linear_squares_forced(S, T):
            CERT_LINEAR.append((S, T))
        else:
            UNRESOLVED.append((S, T))
note("linear test over 240 ordered pairs took %.1fs" % (time.time() - t1))
check("linear monomial test certifies 168 of 240 ordered pairs and leaves 72 (independent reproduction)",
      len(CERT_LINEAR) == 168 and len(UNRESOLVED) == 72)

# the 72 unresolved ordered pairs as printed by the source runner (data, copied verbatim as pairs)
SOURCE_72 = """
(-3,-2)(-3,-1) (-3,-2)(-3,1) (-3,-2)(-3,2) (-3,-2)(-1,-2) (-3,-2)(1,-2) (-3,-2)(2,-3)
(-3,-1)(-3,-2) (-3,-1)(-3,1) (-3,-1)(-3,2) (-3,-1)(-2,-1) (-3,-1)(1,-3) (-3,-1)(1,-2)
(-3,1)(-3,-2) (-3,1)(-3,-1) (-3,1)(-3,2) (-3,1)(-2,1) (-3,1)(-1,-3) (-3,1)(-1,-2)
(-3,2)(-3,-2) (-3,2)(-3,-1) (-3,2)(-3,1) (-3,2)(-2,-3) (-3,2)(-2,-1) (-3,2)(-2,1)
(-2,-3)(-3,2) (-2,-3)(-2,-1) (-2,-3)(-2,1) (-2,-3)(-1,-3) (-2,-3)(1,-3) (-2,-3)(2,-3)
(-2,-1)(-3,-1) (-2,-1)(-3,2) (-2,-1)(-2,-3) (-2,-1)(-2,1) (-2,-1)(1,-3) (-2,-1)(1,-2)
(-2,1)(-3,1) (-2,1)(-3,2) (-2,1)(-2,-3) (-2,1)(-2,-1) (-2,1)(-1,-3) (-2,1)(-1,-2)
(-1,-3)(-3,1) (-1,-3)(-2,-3) (-1,-3)(-2,1) (-1,-3)(-1,-2) (-1,-3)(1,-3) (-1,-3)(2,-3)
(-1,-2)(-3,-2) (-1,-2)(-3,1) (-1,-2)(-2,1) (-1,-2)(-1,-3) (-1,-2)(1,-2) (-1,-2)(2,-3)
(1,-3)(-3,-1) (1,-3)(-2,-3) (1,-3)(-2,-1) (1,-3)(-1,-3) (1,-3)(1,-2) (1,-3)(2,-3)
(1,-2)(-3,-2) (1,-2)(-3,-1) (1,-2)(-2,-1) (1,-2)(-1,-2) (1,-2)(1,-3) (1,-2)(2,-3)
(2,-3)(-3,-2) (2,-3)(-2,-3) (2,-3)(-1,-3) (2,-3)(-1,-2) (2,-3)(1,-3) (2,-3)(1,-2)
"""
import re
_nums = [int(t) for t in re.findall(r"-?\d+", SOURCE_72)]
SRC72 = {((_nums[i], _nums[i + 1]), (_nums[i + 2], _nums[i + 3])) for i in range(0, len(_nums), 4)}
check("my 72 unresolved ordered pairs coincide with the list printed by the source runner (hard-coded data)",
      SRC72 == set(UNRESOLVED) and len(SRC72) == 72)
check("all 72 partners are themselves unequal-height signatures (equal/opposite partners are always linearly certified)",
      all(T in UNEQ for S, T in UNRESOLVED))
check("MUTANT: with the symmetric cross term dropped the linear test would 'certify' a different count (assembly matters)",
      sum(1 for S in UNEQ for T in SIGS if T != S and linear_squares_forced(S, T, symmetric=False)) != 168)

# ----------------------------------------------------------------------------
# 5. polynomial arithmetic on dicts and degree-3 Nullstellensatz certificates
# ----------------------------------------------------------------------------
def pmul(p, q):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(a + b for a, b in zip(e1, e2))
            out[e] = out.get(e, Fr(0)) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def padd(p, q):
    out = dict(p)
    for e, c in q.items():
        out[e] = out.get(e, Fr(0)) + c
    return {e: c for e, c in out.items() if c != 0}


def pscale(p, s):
    return {e: c * s for e, c in p.items() if c * s != 0}


def var_poly(k):
    e = [0] * 6
    e[k] = 1
    return {tuple(e): Fr(1)}


def monos_of_degree(k, n=6):
    out = []
    for c in itertools.combinations_with_replacement(range(n), k):
        e = [0] * n
        for i in c:
            e[i] += 1
        out.append(tuple(e))
    return out


def macaulay_certificates(polys, deg, targets):
    """For each target monomial (exponent tuple of total degree `deg`) find
    cofactors h_{j} (homogeneous of degree deg-2) with sum_j h_j * poly_j = target.
    Returns dict target -> list of cofactor polys, or None if some target is not in I_deg."""
    mons = monos_of_degree(deg)
    mi = {m: i for i, m in enumerate(mons)}
    gens = []  # (j, multiplier monomial)
    for j in range(len(polys)):
        for m in monos_of_degree(deg - 2):
            gens.append((j, m))
    ng = len(gens)
    # augmented rows: [ coefficients over degree-deg monomials | identity over gens ]
    rows = []
    for g, (j, m) in enumerate(gens):
        row = [Fr(0)] * (len(mons) + ng)
        for e, c in polys[j].items():
            ee = tuple(a + b for a, b in zip(e, m))
            row[mi[ee]] += c
        row[len(mons) + g] = Fr(1)
        rows.append(row)
    # eliminate on the first len(mons) columns only
    piv_row = {}
    r = 0
    nm = len(mons)
    for c in range(nm):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        s = rows[r][c]
        rows[r] = [v / s for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[r])]
        piv_row[c] = r
        r += 1
    out = {}
    for t in targets:
        c = mi[t]
        if c not in piv_row:
            return None
        row = rows[piv_row[c]]
        # row is e_c (+ combination of non-pivot columns); target in I iff the part on non-pivot
        # monomial columns vanishes
        if any(row[k] != 0 for k in range(nm) if k != c):
            return None
        cof = [dict() for _ in polys]
        for g, (j, m) in enumerate(gens):
            coef = row[nm + g]
            if coef != 0:
                cof[j][m] = cof[j].get(m, Fr(0)) + coef
        out[t] = cof
    return out


def verify_certificate(polys, cof, target_poly):
    """Independent exact check of  sum_j cof_j * polys_j == target  (polynomial identity)."""
    acc = {}
    for h, p in zip(cof, polys):
        acc = padd(acc, pmul(h, p))
    diff = padd(acc, pscale(target_poly, Fr(-1)))
    return len(diff) == 0


def cube(k):
    e = [0] * 6
    e[k] = 3
    return tuple(e)


t2 = time.time()
cert_ok = True
cert_count = 0
hilb = {}
sizes = {}
CERTS = {}
for (S, T) in UNRESOLVED:
    basis, _ = quadrics(S, T)
    polys = [quad_to_poly(q) for q in basis]
    sizes[(S, T)] = len(polys)
    certs = macaulay_certificates(polys, 3, [cube(k) for k in range(6)])
    if certs is None:
        cert_ok = False
        continue
    CERTS[(S, T)] = (polys, certs)
    for k in range(6):
        cert_count += 1
        if not verify_certificate(polys, certs[cube(k)], {cube(k): Fr(1)}):
            cert_ok = False
note("degree-3 certificates for 72 pairs computed+verified in %.1fs" % (time.time() - t2))
check("72 pairs x 6 variables: x_i^3 = sum_j (linear form)_j * (pair-moment quadric)_j, exact identity verified (%d certificates)" % cert_count,
      cert_ok and cert_count == 432)
check("quadric-span dimensions over the 72 pairs are 20 (48 pairs) or 18 (24 pairs) out of 21",
      sorted(set(sizes.values())) == [18, 20] and sum(1 for v in sizes.values() if v == 20) == 48)

# full Macaulay statement: all 56 cubic monomials in the ideal (so the quotient has Hilbert function (1,6,21-q) )
all_cubics_ok = True
for (S, T) in UNRESOLVED[:12]:
    polys = CERTS[(S, T)][0]
    r = macaulay_certificates(polys, 3, monos_of_degree(3))
    if r is None:
        all_cubics_ok = False
check("sample of 12 of the 72: every one of the 56 cubic monomials lies in the quadrics' degree-3 part", all_cubics_ok)

# explicit certificate printout for the lead case (-3,-2) vs (-3,-1)
lead = ((-3, -2), (-3, -1))
polys, certs = CERTS[lead]
def fmt_poly(p):
    names = "x0 x1 x2 x3 x4 x5".split()
    terms = []
    for e, c in sorted(p.items(), reverse=True):
        mon = "*".join(names[i] + ("^%d" % e[i] if e[i] > 1 else "") for i in range(6) if e[i])
        terms.append("(%s)%s" % (c, "*" + mon if mon else ""))
    return " + ".join(terms) if terms else "0"
note("LEAD CASE (-3,-2) vs (-3,-1): %d quadrics:" % len(polys))
for j, p in enumerate(polys):
    note("  q%d = %s" % (j, fmt_poly(p)))
# tidy hand certificate for x5^3
lead_poly_set = {tuple(sorted(p.items())) for p in polys}
def has(p):
    return tuple(sorted(p.items())) in lead_poly_set
x = [var_poly(k) for k in range(6)]
q_x2sq = padd(pmul(x[2], x[2]), pscale(pmul(x[5], x[5]), Fr(-1)))
q_x2x5 = pmul(x[2], x[5])
check("lead case: the quadrics contain x2^2 - x5^2 and x2*x5 (as the task states: x_i^2 - x_5^2 and x0*x2 families)",
      has(q_x2sq) and has(q_x2x5))
# hand identity  x5^3 = x2*(x2 x5) - x5*(x2^2 - x5^2)
lhs = padd(pmul(x[2], q_x2x5), pscale(pmul(x[5], q_x2sq), Fr(-1)))
check("lead case hand certificate:  x5^3 = x2*(x2*x5) - x5*(x2^2 - x5^2)  (exact)",
      lhs == {cube(5): Fr(1)})
q02 = pmul(x[0], x[2])
q00 = padd(pmul(x[0], x[0]), pscale(pmul(x[5], x[5]), Fr(-1)))
check("lead case: the quadrics contain x0*x2 and x0^2 - x5^2 (so over R: x0 x2 = 0 and x0^2 = x2^2 force x0=x2=0)",
      has(q02) and has(q00) and has(padd(pmul(x[1], x[1]), pscale(pmul(x[5], x[5]), Fr(-1)))))

# tamper test: a corrupted cofactor must be rejected
polys_t, certs_t = CERTS[lead]
bad = [dict(h) for h in certs_t[cube(0)]]
jj = next(j for j, h in enumerate(bad) if h)
mm = next(iter(bad[jj]))
bad[jj][mm] = bad[jj][mm] + Fr(1, 7)
check("MUTANT: tampered cofactor is rejected by the identity verifier",
      not verify_certificate(polys_t, bad, {cube(0): Fr(1)}))

# ----------------------------------------------------------------------------
# 6. consequence statements
# ----------------------------------------------------------------------------
# x_i^3 = 0 forces x_i = 0 in any field of characteristic 0 (and indeed in any reduced ring);
# hence over Q, R, C the pair-moment system has only the origin for every one of the 72 pairs.
check("conclusion A: for each of the 72 pairs the pair-moment zero set (over Q, R and C) is {0} in all six coordinates",
      cert_ok and len(CERTS) == 72)

# the 168 linear pairs: squares of the unequal block are in the span => x_i^2 = 0 => block zero
check("conclusion B: with the 168 linear cases, x(unequal block)=0 for all 240 ordered unequal+partner pairs",
      len(CERT_LINEAR) + len(CERTS) == 240)

# all 132 ordered pairs of two unequal signatures: both blocks zero (adds partner info to the 72)
unun = [(S, T) for S in UNEQ for T in UNEQ if S != T]
check("132 ordered unequal+unequal pairs = 60 linear + 72 nonlinear", len(unun) == 132 and
      sum(1 for p in unun if p in set(CERT_LINEAR)) == 60 and sum(1 for p in unun if p in CERTS) == 72)

# sigma: d -> -d symmetry maps the problem to itself; the 72 are closed under the induced label map
def canon(s):
    return min(s, (-s[1], -s[0]))
SIG = lambda s: canon((-s[0], -s[1]))
SIG_closed = all((SIG(S), SIG(T)) in set(UNRESOLVED) for S, T in UNRESOLVED)
orbits = {frozenset({frozenset({S, T}), frozenset({SIG(S), SIG(T)})}) for S, T in UNRESOLVED}
check("the 72 ordered pairs are closed under height negation d->-d; 36 unordered pairs, %d classes under it" % len(orbits),
      SIG_closed and len({frozenset({S, T}) for S, T in UNRESOLVED}) == 36 and len(orbits) == 18)

# ----------------------------------------------------------------------------
# 7. second exact route: Groebner bases (sympy), radical membership over Q (hence over C)
# ----------------------------------------------------------------------------
import sympy as sp
from sympy import groebner, symbols

X = symbols("x0:6")
TT = symbols("tt")


def to_sympy(qd):
    return sum(sp.Rational(c.numerator, c.denominator) * X[i] * X[j] for (i, j), c in qd.items())


t3 = time.time()
gb_ok = True
for (S, T) in UNRESOLVED:
    basis, _ = quadrics(S, T)
    polys_sp = [to_sympy(q) for q in basis]
    for k in range(6):
        g = groebner(polys_sp + [1 - TT * X[k]], *X, TT, order="grevlex")
        if list(g.exprs) != [1]:
            gb_ok = False
note("sympy Groebner radical tests (72 x 6) in %.1fs" % (time.time() - t3))
check("sympy Groebner: 1 in (I, 1 - t*x_k) for all 72 pairs and all six k  (x_k in the radical over C)", gb_ok)

# ----------------------------------------------------------------------------
# 8. floating-point cross-check (not a proof): minimise sum q_j(x)^2 on the unit sphere
# ----------------------------------------------------------------------------
import numpy as np
from scipy.optimize import minimize

def sphere_min(basis, starts=12, seed=1):
    mats = []
    for qd in basis:
        A = np.zeros((6, 6))
        for (i, j), c in qd.items():
            if i == j:
                A[i, i] += float(c)
            else:
                A[i, j] += float(c) / 2
                A[j, i] += float(c) / 2
        mats.append(A)
    mats = np.array(mats)
    def f(z):
        x = z / np.linalg.norm(z)
        v = np.einsum("jab,a,b->j", mats, x, x)
        return float(v @ v)
    rs = np.random.RandomState(seed)
    best = 1e9
    for _ in range(starts):
        r = minimize(f, rs.randn(6), method="BFGS", options={"gtol": 1e-12, "maxiter": 400})
        best = min(best, r.fun)
    return best

t4 = time.time()
mins = []
for (S, T) in UNRESOLVED:
    basis, _ = quadrics(S, T)
    mins.append(sphere_min(basis))
note("global-ish minimum of sum q^2 on unit sphere over the 72 pairs: %.3e .. %.3e (%.1fs)" % (min(mins), max(mins), time.time() - t4))
check("floating-point multistart: min over unit sphere of sum of squared moments stays above 1e-4 for all 72 (consistent with origin-only)",
      min(mins) > 1e-4)

# ----------------------------------------------------------------------------
# 9. controls: equal-height control, positive control (nonzero solution exists), non-unequal pairs
# ----------------------------------------------------------------------------
# 9a equal-height control: (-3,-3) beside (3,-3): linear square test fails, as in the equal-height note
EQC = ((-3, -3), (3, -3))
check("control: equal-height signature (-3,-3) beside opposite (3,-3) is NOT forced by the linear square test (as in the source)",
      not linear_squares_forced(*EQC))
basis_c, _ = quadrics(*EQC)
polys_c = [quad_to_poly(q) for q in basis_c]
# smallest degree k <= 6 at which x0^k, x1^k, x2^k lie in I_k (nonlinear route works, but not at degree 2)
kmin = None
for kk in range(3, 8):
    tg = []
    for v in range(3):
        e = [0] * 6
        e[v] = kk
        tg.append(tuple(e))
    if macaulay_certificates(polys_c, kk, tg) is not None:
        kmin = kk
        break
note("equal-height control: equal block coordinates nilpotent mod the quadrics, first at degree %s" % kmin)
check("control: equal-height block is nevertheless forced to zero by a higher-degree certificate (failure of the linear test is not a nonzero solution)",
      kmin is not None and kmin > 2)

# 9b positive control: two opposite signatures -> nonzero rational solution of every pair moment; certificate machinery refuses
OPC = ((-3, 3), (-2, 2))
basis_o, _ = quadrics(*OPC)
polys_o = [quad_to_poly(q) for q in basis_o]
pt = [Fr(1), Fr(-2), Fr(3), Fr(0), Fr(0), Fr(0)]
check("positive control: opposite+opposite pair has nonzero rational points (1,-2,3,0,0,0) killing every pair-moment quadric",
      all(eval_quad(q, pt) == 0 for q in basis_o))
check("positive control: degree-3 certificate machinery correctly fails (returns no certificate) for that pair",
      macaulay_certificates(polys_o, 3, [cube(0)]) is None)
# also: the brute-force lattice sums agree that this point is a pair-moment solution
rowsO = raw_moment_rows(list(OPC))
check("positive control: all raw lattice pair moments vanish at that point (direct sums)",
      all(eval_quad(rowsO[k], pt) == 0 for k in rowsO))

# 9c a single opposite signature has no pair-moment constraint at all
check("positive control: a single opposite signature has an empty set of pair-moment quadrics",
      len(span_basis(raw_moment_rows([(-3, 3)]), 3)[0]) == 0)

# ----------------------------------------------------------------------------
# 10. scope guard and result
# ----------------------------------------------------------------------------
note("scope: pair moments only (necessary conditions); two-signature support; orbit of (1,2,3); uniform r0; rational kernel coordinates.")
note("not claimed: classification on three or more signatures, the full affine bond space, positivity of any factor, or any physical law selection.")
if FAIL == 0 and PASS > 0:
    print("HIT: all 72 coupled unequal-height signature pairs left open by the 2026-10-10 direct test have origin-only pair-moment zero sets over Q, R and C, certified by exact degree-3 Nullstellensatz identities; so the unequal block is zero in all 240 ordered cases (scope: two-signature ansatz on the orbit of (1,2,3), pair moments, uniform average).")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
print("SUMMARY: exact degree-3 Nullstellensatz certificates show the pair-moment quadrics of every one of the 72 unresolved unequal+unequal signature pairs vanish only at the origin (over Q, R, C), completing the elimination of the unequal block in all 240 ordered cases of the two-signature ansatz (runtime %.0fs)." % (time.time() - T0))
sys.exit(0 if FAIL == 0 else 1)
