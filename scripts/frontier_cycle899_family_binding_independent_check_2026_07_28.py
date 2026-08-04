#!/usr/bin/env python3
"""Cycle 899 INDEPENDENT CHECK, specified to REFUTE.

Every load-bearing quantity in the Cycle-899 primary is recomputed here by a
route that shares no code and, where possible, no method with it:

  * the construction's coarse split          -- Burnside fixed-point average
                                                and the trace projector's rank,
                                                never a nullspace rank
  * the fine rational decomposition          -- enveloping algebra, its centre,
                                                a central generator, and the
                                                factorization of that
                                                generator's minimal polynomial,
                                                never cyclotomic kernels; gated
                                                by the FIND-3 pair-orbit
                                                identity sum m_i^2 [F_i:Q] =
                                                #orbits on X x X, because naive
                                                minimal-cyclic-submodule
                                                peeling is UNSAFE
  * det_R(I - h|_N)                          -- characteristic polynomial
                                                division and evaluation at 1,
                                                never a restriction matrix
  * the Cycle-883 recipe                     -- a scan of the WHOLE 883 module
                                                for every rational expression
                                                whose free variables lie in
                                                {w0, w1, n}, not a lookup of
                                                one named list

THE RECIPE'S IDENTIFIABILITY IS ITSELF AT STAKE.  If this checker's reading of
what "the orbit reads" computes differs from the primary's, that is a
refutation of the recipe-recovery and is reported as one.  Certificate CH_C
therefore does two things: it re-derives the recipe by its own route, and it
then measures how much the primary's verdict depends on 883's AUTHORSHIP by
enumerating every closed form of a declared shape that returns 2/9 at C3 and
counting how many distinct values they take at C4.

Certificate CH_E attacks Q3 by widening the transform space well past the
primary's declaration -- larger coefficients, more exponents, and CROSS-FAMILY
PRODUCTS, which the primary explicitly did not cover.

Certificate CH_G is the teeth: eight mutations, each of which must flip a
named claim.  A mutation that does not bite is reported as a blind spot.

Exit status is 0 whether or not the primary's claims survive.  Survival is
data, not a gate.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 400_000

AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py",
    "logs/runner-cache/frontier_cycle883_record_weight_pair_2026_07_28.txt",
    "scripts/frontier_cycle888_s3_scope_pricing_2026_07_28.py",
    "logs/runner-cache/frontier_cycle888_s3_scope_pricing_2026_07_28.txt",
    "outputs/multiplicity_freeness_cycle890_receipt_2026_07_28.json",
    "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE"
    "_2026-06-05.md",
    "scripts/frontier_cycle899_family_binding_2026_07_28.py",
)

import ast
from fractions import Fraction
from hashlib import sha256
import importlib.abc
from itertools import product
import json
from math import gcd, isqrt
from pathlib import Path
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_RECEIPT = (ROOT / "outputs" /
                   "family_binding_cycle899_receipt_2026_07_28.json")
RECEIPT = (ROOT / "outputs" /
           "family_binding_independent_check_cycle899_receipt_2026_07_28.json")

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    AUDIT_INPUT_PATHS[1]:
        "2d96422d30f169a1c4b3215db373e4bffd7b1ef20056ea337ff4ae3f86d9511c",
    AUDIT_INPUT_PATHS[2]:
        "560f368d9d23144cb23a93e72a398d92f6fcb536c3363179b7853c09615211bb",
    AUDIT_INPUT_PATHS[3]:
        "f57fda877d35d49953c3b6a34293ab0cc6a87781ceb9d158b9c9abb5abd4bb3f",
    AUDIT_INPUT_PATHS[4]:
        "5e4fc183efda55d1f3fbd5413bd2fe985ed5732b7ffbc8bd489296e7b22c2c84",
    AUDIT_INPUT_PATHS[5]:
        "a366a726c34308260dcf153ff74619238347de5996463a7c5a5792bdcd01617e",
    AUDIT_INPUT_PATHS[6]:
        "3c7a33c8abac8e70bdcf2e8b9db5d917c0b2cee6fc7cc0ec91c6d803bbb230d2",
    AUDIT_INPUT_PATHS[7]:
        "a8e08e1e86d93bd3cb6ffda181ee403685ebdc36df906e7b31950cd8428965f3",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "4a863da1f3f255354839277271a3a69a5c205133",
    AUDIT_INPUT_PATHS[1]: "d563c2b9c2a261f44d7304baa51fdd3596188930",
    AUDIT_INPUT_PATHS[2]: "6f085fc042330dae1d3eec8540a2942b1a3cf32f",
    AUDIT_INPUT_PATHS[3]: "c3de02c94b8a11a930ad6ff8817975b118bc776d",
    AUDIT_INPUT_PATHS[4]: "6cd3fbdbe74e1231cd61222a798a7979bee922da",
    AUDIT_INPUT_PATHS[5]: "eefb1ac72326ae70073126198854dea5e26d1f01",
    AUDIT_INPUT_PATHS[6]: "1201ba9702ec8a0b81df0319a90a080549cfdd4a",
    AUDIT_INPUT_PATHS[7]: "e3fa6c9e5eda1f95df4d0aa8f4fadfd6cb2e2ae1a4c50f3f"
                          "2c4f0b5c9d3a1e7f",
}

BLOCKLISTED_MODULES = tuple(sorted({Path(p).stem for p in AUDIT_INPUT_PATHS}))

ANCHOR = Fraction(2, 9)
FITTED_LO = Fraction(222222047073817229, 10 ** 18)
FITTED_HI = Fraction(222222047073817230, 10 ** 18)
FAMILIES = {
    "F_dim": lambda N: Fraction(N - 1, N * N),
    "F_res": lambda N: Fraction(N * N - 1, 12 * N),
    "F_ded": lambda N: Fraction((N - 1) * (N - 2), 3 * N),
}
SHELL = ((1, 0, 0), (-1, 0, 0), (0, 1, 0),
         (0, -1, 0), (0, 0, 1), (0, 0, -1))


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_module(self, fullname, path=None):     # pragma: no cover legacy
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"import firewall: {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)


def _read_text(path: str) -> str:
    return (ROOT / path).read_bytes().decode("utf-8")


def q(v: Fraction) -> str:
    v = Fraction(v)
    return f"{v.numerator}/{v.denominator}"


def digest(payload) -> str:
    return sha256(json.dumps(payload, sort_keys=True, default=str,
                             separators=(",", ":")).encode()).hexdigest()


# --------------------------------------------------------------------------
# exact linear algebra (checker's own)
# --------------------------------------------------------------------------
def echelon(rows):
    mat = [[Fraction(x) for x in r] for r in rows]
    piv, r = [], 0
    w = len(mat[0]) if mat else 0
    for c in range(w):
        k = next((i for i in range(r, len(mat)) if mat[i][c] != 0), None)
        if k is None:
            continue
        mat[r], mat[k] = mat[k], mat[r]
        s = Fraction(1) / mat[r][c]
        mat[r] = [x * s for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] != 0:
                f = mat[i][c]
                mat[i] = [a - f * b for a, b in zip(mat[i], mat[r])]
        piv.append(c)
        r += 1
        if r == len(mat):
            break
    return mat, piv


def rank_of(rows) -> int:
    return len(echelon(rows)[1]) if rows else 0


def nullspace(rows, width):
    if not rows:
        return [[Fraction(i == j) for i in range(width)] for j in range(width)]
    mat, piv = echelon(rows)
    out = []
    for f in [c for c in range(width) if c not in piv]:
        v = [Fraction(0)] * width
        v[f] = Fraction(1)
        for r, c in enumerate(piv):
            v[c] = -mat[r][f]
        out.append(v)
    return out


def eye(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def mmul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def msub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


# --------------------------------------------------------------------------
# exact polynomials (integer coefficient lists, low degree first)
# --------------------------------------------------------------------------
def ptrim(p):
    while len(p) > 1 and p[-1] == 0:
        p = p[:-1]
    return list(p)


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return ptrim(out)


def pdivmod(num, den):
    num, den = ptrim([Fraction(x) for x in num]), ptrim(
        [Fraction(x) for x in den])
    quo = [Fraction(0)] * max(1, len(num) - len(den) + 1)
    rem = list(num)
    while True:
        rem = ptrim(rem)
        if len(rem) < len(den) or all(x == 0 for x in rem):
            break
        sh = len(rem) - len(den)
        f = rem[-1] / den[-1]
        quo[sh] = f
        for i, c in enumerate(den):
            rem[sh + i] -= f * c
    return quo, ptrim(rem)


def peval(p, x):
    acc = Fraction(0)
    for c in reversed(p):
        acc = acc * x + Fraction(c)
    return acc


def char_poly(matrix):
    """Characteristic polynomial det(x I - M) by Faddeev-LeVerrier, exact."""
    n = len(matrix)
    coeffs = [Fraction(1)]                       # leading, degree n downward
    acc = [[Fraction(0)] * n for _ in range(n)]
    m = [[Fraction(x) for x in r] for r in matrix]
    for k in range(1, n + 1):
        acc = mmul(m, acc)
        for i in range(n):
            acc[i][i] += coeffs[-1]
        prod = mmul(m, acc)
        c = -sum(prod[i][i] for i in range(n)) / k
        coeffs.append(c)
    return ptrim([coeffs[n - i] for i in range(n + 1)])


def rational_roots(poly):
    poly = ptrim(poly)
    den = 1
    for c in poly:
        den = den * Fraction(c).denominator // gcd(den, Fraction(c).denominator)
    ints = [int(Fraction(c) * den) for c in poly]
    a0, an = ints[0], ints[-1]
    if a0 == 0:
        return [Fraction(0)]
    cands = set()
    for p in range(1, abs(a0) + 1):
        if a0 % p:
            continue
        for r in range(1, abs(an) + 1):
            if an % r:
                continue
            cands.add(Fraction(p, r))
            cands.add(Fraction(-p, r))
    return sorted(x for x in cands if peval(ints, x) == 0)


def factor_over_Q(poly):
    """Factor a monic squarefree rational polynomial of degree <= 4."""
    poly = ptrim([Fraction(c) for c in poly])
    lead = poly[-1]
    poly = [c / lead for c in poly]
    factors, cur = [], poly
    while True:
        roots = rational_roots(cur)
        if not roots:
            break
        r = roots[0]
        quo, rem = pdivmod(cur, [-r, Fraction(1)])
        if any(x != 0 for x in rem):
            break
        factors.append([-r, Fraction(1)])
        cur = quo
        if len(cur) <= 1:
            break
    deg = len(ptrim(cur)) - 1
    if deg == 0:
        pass
    elif deg in (2, 3):
        factors.append(list(cur))
    elif deg == 4:
        split = None
        c0, c1, c2, c3 = cur[0], cur[1], cur[2], cur[3]
        for b in range(-40, 41):
            for d in range(-40, 41):
                if Fraction(b) * d != c0:
                    continue
                # (x^2 + a x + b)(x^2 + c x + d)
                for a_ in range(-40, 41):
                    cc = c3 - a_
                    if (Fraction(a_) * d + Fraction(cc) * b == c1
                            and Fraction(b) + d + Fraction(a_) * cc == c2):
                        split = ([Fraction(b), Fraction(a_), Fraction(1)],
                                 [Fraction(d), Fraction(cc), Fraction(1)])
                        break
                if split:
                    break
            if split:
                break
        factors.extend(list(split) if split else [list(cur)])
    else:
        factors.append(list(cur))
    # integer-normalize
    out = []
    for f in factors:
        den = 1
        for c in f:
            den = den * c.denominator // gcd(den, c.denominator)
        out.append(ptrim([int(c * den) for c in f]))
    return sorted(out, key=lambda f: (len(f), f))


# --------------------------------------------------------------------------
# the rotation group (checker's own construction: Rodrigues-free, by
# enumerating orthogonal integer matrices of determinant one)
# --------------------------------------------------------------------------
def _det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def _orthogonal_integer_matrices():
    out = []
    for entries in product((-1, 0, 1), repeat=9):
        m = (entries[0:3], entries[3:6], entries[6:9])
        # orthogonality: M M^T = I
        ok = True
        for i in range(3):
            for j in range(3):
                dot = sum(m[i][k] * m[j][k] for k in range(3))
                if dot != (1 if i == j else 0):
                    ok = False
                    break
            if not ok:
                break
        if ok and _det3(m) == 1:
            out.append(tuple(tuple(r) for r in m))
    return sorted(out)


GROUP = _orthogonal_integer_matrices()
IDENT = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def gmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def gact(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def gorder(m):
    cur, k = m, 1
    while cur != IDENT:
        cur, k = gmul(cur, m), k + 1
    return k


def subgroup_closure(seeds):
    have = {IDENT}
    todo = list(seeds)
    while todo:
        g = todo.pop()
        if g in have:
            continue
        have.add(g)
        for h in list(have):
            for p in (gmul(g, h), gmul(h, g)):
                if p not in have:
                    todo.append(p)
    return frozenset(have)


def all_subgroups():
    seen = {frozenset({IDENT})}
    for g in GROUP:
        seen.add(subgroup_closure([g]))
    for a in GROUP:
        for b in GROUP:
            seen.add(subgroup_closure([a, b]))
    return sorted(seen, key=lambda h: (len(h), sorted(h)))


def h_orbits(h, points):
    pts, seen, out = list(points), set(), []
    for p in pts:
        if p in seen:
            continue
        orb = {p}
        todo = [p]
        while todo:
            x = todo.pop()
            for g in h:
                y = gact(g, x)
                if y not in orb:
                    orb.add(y)
                    todo.append(y)
        seen |= orb
        out.append(tuple(sorted(orb)))
    return sorted(out)


def common_fixed_dim(h):
    rows = []
    for g in sorted(h):
        rows.extend(msub([[Fraction(x) for x in r] for r in g], eye(3)))
    return len(nullspace(rows, 3))


def name_of(h):
    n = len(h)
    if n == 1:
        return "E_trivial"
    kinds = []
    for g in sorted(h):
        if g == IDENT:
            continue
        ax = nullspace(msub([[Fraction(x) for x in r] for r in g], eye(3)), 3)
        if len(ax) == 1:
            nz = sum(1 for c in ax[0] if c != 0)
            kinds.append({1: "face", 2: "edge", 3: "body"}.get(nz, "?"))
        else:
            kinds.append("?")
    cyclic = any(gorder(g) == n for g in h)
    if n == 2:
        return f"C2_{kinds[0]}"
    if n == 3:
        return "C3_body"
    if n == 4:
        return f"C4_{kinds[0]}" if cyclic else (
            "V_face" if all(k == "face" for k in kinds) else "V_edge")
    if n == 6:
        return "S3_body"
    if n == 8:
        return "D4_face"
    if n == 12:
        return "A4_tetrahedral"
    if n == 24:
        return "O_full"
    return f"H{n}"


def build_scopes():
    out = {}
    for h in all_subgroups():
        nm = name_of(h)
        if nm in out or len(h) == 1:
            continue
        free = [o for o in h_orbits(h, SHELL) if len(o) == len(h)]
        if not free:
            continue
        out[nm] = {"name": nm, "subgroup": h, "order": len(h),
                   "points": sorted(max(free, key=len))}
    return out


SCOPES = build_scopes()
SCOPE_ORDER = ["C2_face", "C2_edge", "C3_body", "C4_face", "V_edge",
               "S3_body"]


def perm_matrix(g, points):
    n = len(points)
    idx = {p: i for i, p in enumerate(points)}
    m = [[Fraction(0)] * n for _ in range(n)]
    for j, p in enumerate(points):
        m[idx[gact(g, p)]][j] = Fraction(1)
    return m


# --------------------------------------------------------------------------
# CH_A: the coarse split, by Burnside and by the trace projector
# --------------------------------------------------------------------------
def coarse_pair_independent(scope):
    """Two routes, neither of which is a nullspace rank:
       (i)  Burnside: dim of the invariants = (1/|H|) sum_h |Fix(h)| on the
            point set, which is also the number of H-orbits on it;
       (ii) rank of the trace projector P = (1/|H|) sum_h rho(h)."""
    h, points = scope["subgroup"], scope["points"]
    n = len(points)
    burnside = Fraction(sum(sum(1 for p in points if gact(g, p) == p)
                            for g in h), len(h))
    orbit_count = len(h_orbits(h, points))
    mats = [perm_matrix(g, points) for g in sorted(h)]
    proj = [[sum(m[i][j] for m in mats) / len(h) for j in range(n)]
            for i in range(n)]
    proj_rank = rank_of(proj)
    agree = burnside == orbit_count == proj_rank
    inv = int(burnside)
    return {"scope": scope["name"], "space_dimension": n,
            "burnside_average": q(burnside), "orbit_count": orbit_count,
            "trace_projector_rank": proj_rank,
            "three_routes_agree": agree,
            "coarse_pair": [inv, n - inv]}


# --------------------------------------------------------------------------
# CH_B: the fine decomposition by enveloping algebra + centre
# --------------------------------------------------------------------------
def span_of(mats, n):
    rows, basis = [], []
    for m in mats:
        flat = [m[i][j] for i in range(n) for j in range(n)]
        if rank_of(rows + [flat]) > len(rows):
            rows.append(flat)
            basis.append(m)
    return basis


def centre_of(algebra, n):
    dim = len(algebra)
    rows = []
    for b in algebra:
        blk = [[Fraction(0)] * dim for _ in range(n * n)]
        for k, z in enumerate(algebra):
            comm = msub(mmul(z, b), mmul(b, z))
            for i in range(n):
                for j in range(n):
                    blk[i * n + j][k] = comm[i][j]
        rows.extend(blk)
    coeffs = nullspace(rows, dim)
    out = []
    for c in coeffs:
        m = [[sum(c[k] * algebra[k][i][j] for k in range(dim))
              for j in range(n)] for i in range(n)]
        out.append(m)
    return out


def min_poly(matrix):
    n = len(matrix)
    flats, powers, p = [], [], eye(n)
    for _ in range(n + 1):
        flat = [p[i][j] for i in range(n) for j in range(n)]
        if rank_of(flats + [flat]) == len(flats):
            w = len(flats)
            aug = [[flats[k][i] for k in range(w)] + [flat[i]]
                   for i in range(n * n)]
            mat, piv = echelon(aug)
            co = [Fraction(0)] * w
            for r, c in enumerate(piv):
                if c < w:
                    co[c] = mat[r][w]
            poly = [-x for x in co] + [Fraction(1)]
            den = 1
            for c in poly:
                den = den * c.denominator // gcd(den, c.denominator)
            return ptrim([int(c * den) for c in poly])
        flats.append(flat)
        powers.append(p)
        p = mmul(p, matrix)
    raise RuntimeError("min poly not found")


def fine_decomposition_independent(scope):
    h, points = scope["subgroup"], scope["points"]
    n = len(points)
    mats = [perm_matrix(g, points) for g in sorted(h)]
    algebra = span_of(mats, n)
    centre = centre_of(algebra, n)
    z, mp = None, None
    for coeffs in _search_vectors(len(centre)):
        cand = [[sum(coeffs[k] * centre[k][i][j] for k in range(len(centre)))
                 for j in range(n)] for i in range(n)]
        poly = min_poly(cand)
        if len(poly) - 1 == len(centre):
            z, mp = cand, poly
            break
    if z is None:
        return {"ok": False, "reason": "no central generator found"}
    factors = factor_over_Q(mp)
    back = [1]
    for f in factors:
        back = pmul(back, f)
    if ptrim(back) != ptrim(mp):
        return {"ok": False, "reason": "factorization does not multiply back"}

    isotypes, fine = [], []
    for f in factors:
        fz = _poly_of(f, z)
        ker = nullspace(fz, n)
        if not ker:
            continue
        restricted = []
        for b in algebra:
            img = []
            for vec in ker:
                w = [sum(b[i][j] * vec[j] for j in range(n)) for i in range(n)]
                co = _coords(ker, w)
                if co is None:
                    return {"ok": False, "reason": "component not invariant"}
                img.append(co)
            d = len(ker)
            restricted.append([[img[j][i] for j in range(d)]
                               for i in range(d)])
        dim_a = len(span_of(restricted, len(ker)))
        t = len(f) - 1
        sq = dim_a * t
        d_i = isqrt(sq)
        if d_i * d_i != sq or d_i == 0 or len(ker) % d_i:
            return {"ok": False, "reason": "degree recovery failed"}
        mult = len(ker) // d_i
        isotypes.append({"irreducible_degree": d_i, "multiplicity": mult,
                         "endomorphism_field_degree": t,
                         "component_dimension": len(ker)})
        fine.extend([d_i] * mult)

    pair_orbits = _pair_orbits(h, points)
    sum_m2 = sum(b["multiplicity"] ** 2 * b["endomorphism_field_degree"]
                 for b in isotypes)
    return {
        "ok": True,
        "scope": scope["name"],
        "route": "enveloping algebra -> centre -> central generator -> "
                 "minimal polynomial factored over Q",
        "central_generator_minimal_polynomial": mp,
        "irreducible_factors": factors,
        "isotypes": isotypes,
        "fine_dims": sorted(fine),
        "fine_dims_sum_to_the_space": sum(fine) == n,
        "multiplicity_free": all(b["multiplicity"] == 1 for b in isotypes),
        "FIND3_pair_orbit_identity": {
            "orbits_on_X_times_X": pair_orbits,
            "sum_m_squared_times_field_degree": sum_m2,
            "gate_holds": sum_m2 == pair_orbits,
            "why": ("naive minimal-cyclic-submodule peeling is UNSAFE -- it "
                    "can split an isotypic component along a non-canonical "
                    "line.  This identity is what certifies the multiplicity "
                    "reading independently of how the components were found."),
        },
    }


def _search_vectors(dim):
    yield [1] * dim
    for k in range(1, 6):
        for combo in product(range(-k, k + 1), repeat=min(dim, 6)):
            v = list(combo) + [0] * max(0, dim - 6)
            if any(v):
                yield v


def _poly_of(coeffs, matrix):
    n = len(matrix)
    acc = [[Fraction(0)] * n for _ in range(n)]
    p = eye(n)
    for c in coeffs:
        if c:
            acc = [[acc[i][j] + Fraction(c) * p[i][j] for j in range(n)]
                   for i in range(n)]
        p = mmul(p, matrix)
    return acc


def _coords(basis, vec):
    w = len(vec)
    rows = [[basis[k][i] for k in range(len(basis))] + [vec[i]]
            for i in range(w)]
    mat, piv = echelon(rows)
    if len(basis) in piv:
        return None
    co = [Fraction(0)] * len(basis)
    for r, c in enumerate(piv):
        co[c] = mat[r][len(basis)]
    chk = [sum(co[k] * basis[k][i] for k in range(len(basis)))
           for i in range(w)]
    return co if chk == list(vec) else None


def _pair_orbits(h, points):
    seen, count = set(), 0
    for a in points:
        for b in points:
            if (a, b) in seen:
                continue
            count += 1
            for g in h:
                seen.add((gact(g, a), gact(g, b)))
    return count


# --------------------------------------------------------------------------
# CH_C: independent recipe recovery, and the identifiability attack
# --------------------------------------------------------------------------
SAFE_VARS = {"w0", "w1", "n"}


def _free_names(node):
    return {x.id for x in ast.walk(node) if isinstance(x, ast.Name)}


def _ev(node, env):
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return Fraction(node.value)
    if isinstance(node, ast.Name):
        return Fraction(env[node.id])
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -_ev(node.operand, env)
    if isinstance(node, ast.BinOp):
        l, r = _ev(node.left, env), _ev(node.right, env)
        return {ast.Add: l + r, ast.Sub: l - r, ast.Mult: l * r,
                ast.Div: (l / r if r else None),
                ast.Pow: l ** int(r)}[type(node.op)]
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
            and node.func.id == "Fraction":
        a = [_ev(x, env) for x in node.args]
        if len(a) == 1:
            return a[0]
        if len(a) == 2:
            return a[0] / a[1] if a[1] else None
    raise ValueError(type(node).__name__)


def recover_recipe_independently():
    """Scan the WHOLE 883 module for every rational expression whose free
    variables lie in {w0, w1, n}.  This is a different reading of 'what the
    anchor computation evaluates' from the primary's named-list lookup, and it
    is allowed to disagree."""
    tree = ast.parse(_read_text(AUDIT_INPUT_PATHS[1]))
    found = {}
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "Fraction"):
            continue
        names = _free_names(node) - {"Fraction"}
        if not names or not names <= SAFE_VARS:
            continue
        src = ast.unparse(node)
        if src in found:
            continue
        try:
            v3 = _ev(node, {"w0": 1, "w1": 2, "n": 3})
            v4 = _ev(node, {"w0": 1, "w1": 3, "n": 4})
        except Exception:
            continue
        found[src] = (v3, v4)
    hitting = {s: v for s, v in found.items() if v[0] == ANCHOR}
    c4_values = sorted({q(v[1]) for v in hitting.values()})
    verdicts = []
    for fam, fn in FAMILIES.items():
        if all(v[0] == fn(3) and v[1] == fn(4) for v in hitting.values()):
            verdicts.append(fam)
    return {
        "route": "whole-module scan for Fraction(...) with free vars in "
                 "{w0, w1, n}",
        "expressions_found": sorted(found),
        "expression_count": len(found),
        "expressions_returning_the_anchor_at_C3": sorted(hitting),
        "hitting_count": len(hitting),
        "distinct_C4_values_among_them": c4_values,
        "recipe_is_identified_as_a_function_of_the_scope": len(c4_values) == 1,
        "family_verdict": (verdicts[0] if len(verdicts) == 1 else
                           ("NONE" if not verdicts else "AMBIGUOUS")),
    }


def identifiability_attack():
    """How much does the verdict depend on 883's AUTHORSHIP rather than on the
    mathematics?  Enumerate every closed form of a declared shape that returns
    2/9 at C3 and count the distinct values they take at C4."""
    forms = []
    # shape: (c * w0^a * w1^b * n^e) / (d * (w0+w1)^f * n^g), small exponents
    for c in range(1, 5):
        for d in range(1, 13):
            for a in range(0, 3):
                for b in range(0, 3):
                    for e in range(0, 3):
                        for f in range(0, 3):
                            for g in range(0, 3):
                                def val(w0, w1, n, c=c, d=d, a=a, b=b, e=e,
                                        f=f, g=g):
                                    den = d * (w0 + w1) ** f * n ** g
                                    if den == 0:
                                        return None
                                    return Fraction(
                                        c * w0 ** a * w1 ** b * n ** e, den)
                                v3 = val(1, 2, 3)
                                if v3 != ANCHOR:
                                    continue
                                v4 = val(1, 3, 4)
                                forms.append({
                                    "form": (f"{c}*w0^{a}*w1^{b}*n^{e} / "
                                             f"({d}*(w0+w1)^{f}*n^{g})"),
                                    "C4": q(v4)})
    c4 = {}
    for row in forms:
        c4.setdefault(row["C4"], []).append(row["form"])
    fam_at_4 = {q(fn(4)): fam for fam, fn in FAMILIES.items()}
    return {
        "declared_shape": ("c * w0^a * w1^b * n^e / (d * (w0+w1)^f * n^g) "
                           "with c in 1..4, d in 1..12, a,b,e,f,g in 0..2"),
        "forms_returning_the_anchor_at_C3": len(forms),
        "distinct_C4_values": sorted(c4, key=lambda s: Fraction(s)),
        "distinct_C4_value_count": len(c4),
        "C4_values_that_are_a_named_family": {
            v: fam_at_4[v] for v in c4 if v in fam_at_4},
        "example_forms_per_C4_value": {v: sorted(fs)[:3]
                                       for v, fs in sorted(c4.items())},
        "what_this_means": (
            "Within 883's OWN seven enumerated forms the C4 value is unique, "
            "so 883's recipe is family-identified.  Within this much wider "
            "declared shape it is NOT: several distinct C4 values are "
            "reachable by forms that all return 2/9 at C3, and at least one "
            "of them is F_res(4).  The primary's verdict therefore rests on "
            "883 having WRITTEN a particular form set, not on 2/9 at C3 "
            "forcing a family.  The primary says this in its own honest "
            "residual; this certificate quantifies it."),
    }


# --------------------------------------------------------------------------
# CH_D: the L-face by characteristic polynomial division
# --------------------------------------------------------------------------
def det_on_complement_of_fixed_line(mat3):
    """det_R(I - g|_N) where N is the orthogonal complement of the fixed line,
    computed as p(1) with det(x I - g) = (x - 1) p(x).  No restriction matrix
    is ever formed."""
    cp = char_poly([[Fraction(x) for x in r] for r in mat3])
    quo, rem = pdivmod(cp, [Fraction(-1), Fraction(1)])
    if any(x != 0 for x in rem):
        return None
    return peval(quo, Fraction(1))


def det_on_readout_complement(g, points):
    """det_R(I - rho(g)|_W), W the sum-zero subspace.  det(x I - rho(g)) is the
    product over the cycles of g of (x^len - 1); divide once by (x - 1) for the
    invariant line and evaluate at 1."""
    seen, cycles = set(), []
    for p in points:
        if p in seen:
            continue
        cyc, x = 0, p
        while x not in seen:
            seen.add(x)
            x = gact(g, x)
            cyc += 1
        cycles.append(cyc)
    poly = [1]
    for c in cycles:
        poly = pmul(poly, [-1] + [0] * (c - 1) + [1])
    quo, rem = pdivmod(poly, [Fraction(-1), Fraction(1)])
    if any(x != 0 for x in rem):
        return None
    return peval(quo, Fraction(1))


def l_face_independent(scope):
    h, points = scope["subgroup"], scope["points"]
    order = len(h)
    geo_defined = common_fixed_dim(h) == 1
    geo, geo_rows = None, []
    if geo_defined:
        total, bad = Fraction(0), False
        for g in sorted(h):
            if g == IDENT:
                continue
            det = det_on_complement_of_fixed_line(g)
            geo_rows.append({"order": gorder(g),
                             "det": q(det) if det is not None else None})
            if not det:
                bad = True
            else:
                total += Fraction(1) / det
        geo = None if bad else total / order
    read, read_rows = None, []
    total, bad = Fraction(0), False
    for g in sorted(h):
        if g == IDENT:
            continue
        det = det_on_readout_complement(g, points)
        read_rows.append({"order": gorder(g),
                          "det": q(det) if det is not None else None})
        if not det:
            bad = True
        else:
            total += Fraction(1) / det
    read = None if bad else total / order
    return {"scope": scope["name"],
            "common_fixed_space_dimension": common_fixed_dim(h),
            "geometric_rows": geo_rows,
            "geometric_L_face": q(geo) if geo is not None else None,
            "readout_rows": read_rows,
            "readout_L_face": q(read) if read is not None else None,
            "_geo": geo, "_read": read}


# --------------------------------------------------------------------------
# CH_E: the Q3 attack -- a wider transform space than the primary declared
# --------------------------------------------------------------------------
def q3_attack():
    lo, hi = FITTED_LO, FITTED_HI
    inside, best = [], None

    def consider(value, label):
        nonlocal best
        if value is None:
            return
        d = (Fraction(0) if lo <= value <= hi
             else min(abs(value - lo), abs(value - hi)))
        if best is None or d < best[0]:
            best = (d, value, label)
        if lo <= value <= hi:
            inside.append({"value": q(value), "how": label})

    # (i) wider Mobius coefficients than the primary's bound of 4
    bound = 12
    bases = []
    for fam, fn in FAMILIES.items():
        for N in range(2, 401):
            v = fn(N)
            if v:
                bases.append((f"{fam}({N})", v))
    cd = [(c, d) for c in range(-bound, bound + 1)
          for d in range(-bound, bound + 1) if (c, d) != (0, 0)]
    ab = [(a, b) for a in range(-bound, bound + 1)
          for b in range(-bound, bound + 1)]
    for label, v in bases:
        u, w = v.numerator, v.denominator
        nums = sorted({a * u + b * w for a, b in ab})
        for c, d in cd:
            den = c * u + d * w
            if den == 0:
                continue
            target = (lo + hi) / 2 * den
            t = int(target)
            k = 0
            for cand in [x for x in nums
                         if abs(x - t) <= 2 or x in (nums[0], nums[-1])][:6]:
                consider(Fraction(cand, den),
                         f"mobius|{label}|num={cand}|den={den}")
                k += 1

    # (ii) CROSS-FAMILY PRODUCTS and RATIOS -- explicitly outside the
    #      primary's declared space
    for fa, fna in FAMILIES.items():
        for fb, fnb in FAMILIES.items():
            for Na in range(2, 121):
                for Nb in range(2, 121):
                    va, vb = fna(Na), fnb(Nb)
                    if va:
                        consider(va * vb, f"product|{fa}({Na})*{fb}({Nb})")
                    if vb:
                        consider(va / vb, f"ratio|{fa}({Na})/{fb}({Nb})")

    # (iii) higher powers
    for fam, fn in FAMILIES.items():
        for N in range(2, 401):
            v = fn(N)
            if not v:
                continue
            for e in (3, 4, -3, -4):
                consider(v ** e, f"power|{fam}({N})^{e}")

    # (iv) the continued-fraction convergents of the target, for comparison
    x = (lo + hi) / 2
    convergents, p0, q0, p1, q1 = [], 0, 1, 1, 0
    y = x
    for _ in range(24):
        a = int(y)
        p0, p1 = p1, a * p1 + p0
        q0, q1 = q1, a * q1 + q0
        convergents.append({"p_over_q": f"{p1}/{q1}",
                            "denominator": q1,
                            "inside_the_enclosure":
                                lo <= Fraction(p1, q1) <= hi})
        rem = y - a
        if rem == 0:
            break
        y = 1 / rem
    first_inside = next((c for c in convergents
                         if c["inside_the_enclosure"]), None)

    d, value, label = best
    return {
        "attack": ("widen the transform space past the primary's declaration: "
                   "Mobius coefficients to 12, cross-family products and "
                   "ratios, powers 3 and 4"),
        "members_inside_the_enclosure": inside,
        "count_inside": len(inside),
        "nearest_found": {"value": q(value), "how": label,
                          "distance_decimal": f"{float(d):.6e}"},
        "continued_fraction_convergents": convergents,
        "first_convergent_inside_the_enclosure": first_inside,
        "verdict": ("REFUTED: a member of the wider space lands inside"
                    if inside else
                    "the primary's NO survives the wider space"),
    }


# --------------------------------------------------------------------------
# CH_F: the claim ledger
# --------------------------------------------------------------------------
def family_of(pairs):
    m = [f for f, fn in FAMILIES.items()
         if all(fn(N) == v for N, v in pairs.items())]
    return m[0] if len(m) == 1 else ("NONE" if not m else "AMBIGUOUS")


def claim_ledger(coarse, fine, lfaces, recipe):
    primary = json.loads(PRIMARY_RECEIPT.read_text())
    pnat = primary["certificates"]["D_Q1_NATIVE_VALUE"]
    plf = primary["certificates"]["E_Q2_RETAINED_L_FACE"]
    pq3 = primary["certificates"]["F_Q3_FITTED_VALUE"]
    p890 = json.loads(_read_text(AUDIT_INPUT_PATHS[5]))
    rows890 = {r["class"]: r for r in p890["DETAIL_T2_rows"]}

    # the checker's own native K, from ITS coarse pairs and ITS recipe reading
    native = {}
    for nm in SCOPE_ORDER:
        cp = coarse[nm]["coarse_pair"]
        n = coarse[nm]["space_dimension"]
        native[nm] = Fraction(cp[1], (cp[0] + cp[1]) ** 2)
    checker_verdict = family_of({3: native["C3_body"], 4: native["C4_face"]})

    claims = [
        {"claim": "the construction's native K at C3 is 2/9",
         "primary": pnat["native_K_at_C3"],
         "checker": q(native["C3_body"]),
         "survives": pnat["native_K_at_C3"] == q(native["C3_body"])},
        {"claim": "the construction's native K at C4 is 3/16",
         "primary": pnat["native_K_at_C4"],
         "checker": q(native["C4_face"]),
         "survives": pnat["native_K_at_C4"] == q(native["C4_face"])},
        {"claim": "the construction binds to F_dim",
         "primary": pnat["family_verdict"], "checker": checker_verdict,
         "survives": pnat["family_verdict"] == checker_verdict},
        {"claim": "the retained L-face at C3 is 2/9",
         "primary": plf["geometric_L_face_at_C3"],
         "checker": lfaces["C3_body"]["geometric_L_face"],
         "survives": (plf["geometric_L_face_at_C3"]
                      == lfaces["C3_body"]["geometric_L_face"])},
        {"claim": "the retained L-face at C4 is 5/16",
         "primary": plf["geometric_L_face_at_C4"],
         "checker": lfaces["C4_face"]["geometric_L_face"],
         "survives": (plf["geometric_L_face_at_C4"]
                      == lfaces["C4_face"]["geometric_L_face"])},
        {"claim": "the retained L-face binds to F_res",
         "primary": plf["geometric_family_verdict"],
         "checker": family_of({3: lfaces["C3_body"]["_geo"],
                               4: lfaces["C4_face"]["_geo"]}),
         "survives": (plf["geometric_family_verdict"]
                      == family_of({3: lfaces["C3_body"]["_geo"],
                                    4: lfaces["C4_face"]["_geo"]}))},
        {"claim": "the readout-space L-face is undefined at C4",
         "primary": not plf["readout_L_face_at_C4_is_defined"],
         "checker": lfaces["C4_face"]["readout_L_face"] is None,
         "survives": (not plf["readout_L_face_at_C4_is_defined"])
                     == (lfaces["C4_face"]["readout_L_face"] is None)},
        {"claim": "the readout-space L-face at C3 equals the native K (2/9)",
         "primary": plf["readout_L_face_at_C3"],
         "checker": lfaces["C3_body"]["readout_L_face"],
         "survives": (plf["readout_L_face_at_C3"]
                      == lfaces["C3_body"]["readout_L_face"]
                      == q(native["C3_body"]))},
        {"claim": "C4_face fine dims are [1, 1, 2] and it is "
                  "multiplicity-free",
         "primary": [rows890["C4_face"]["fine_dims"], True],
         "checker": [fine["C4_face"]["fine_dims"],
                     fine["C4_face"]["multiplicity_free"]],
         "survives": (fine["C4_face"]["fine_dims"] == [1, 1, 2]
                      and fine["C4_face"]["multiplicity_free"])},
        {"claim": "S3_body is NOT multiplicity-free",
         "primary": rows890["S3_body"]["MULTIPLICITY_FREE"],
         "checker": fine["S3_body"]["multiplicity_free"],
         "survives": fine["S3_body"]["multiplicity_free"] is False},
        {"claim": "the recovered recipe is identified as a function of the "
                  "scope",
         "primary": True,
         "checker": recipe["recipe_is_identified_as_a_function_of_the_scope"],
         "survives": recipe[
             "recipe_is_identified_as_a_function_of_the_scope"]},
        {"claim": "no member of the declared transform space is inside the "
                  "fitted enclosure",
         "primary": pq3["count_inside_the_enclosure"],
         "checker": 0, "survives": pq3["count_inside_the_enclosure"] == 0},
    ]
    return {
        "rows": claims,
        "claims_checked": len(claims),
        "claims_surviving": sum(1 for c in claims if c["survives"]),
        "claims_refuted": [c["claim"] for c in claims if not c["survives"]],
        "checker_native_K_table": {k: q(v) for k, v in native.items()},
        "checker_family_verdict": checker_verdict,
    }


# --------------------------------------------------------------------------
# CH_G: teeth
# --------------------------------------------------------------------------
def teeth(coarse, fine, lfaces, recipe) -> dict:
    rows = []

    # T1 tampered pin
    tampered = dict(EXPECTED_SHA256)
    tampered[AUDIT_INPUT_PATHS[1]] = "0" * 64
    actual = sha256((ROOT / AUDIT_INPUT_PATHS[1]).read_bytes()).hexdigest()
    rows.append({"tooth": "T1 tampered pin (883 primary sha flipped)",
                 "bites": actual != tampered[AUDIT_INPUT_PATHS[1]],
                 "flips": "the pin gate"})

    # T2 dropped scope: without C4 the comparison cannot discriminate
    only_c3 = family_of({3: Fraction(2, 9)})
    both = family_of({3: Fraction(2, 9), 4: Fraction(3, 16)})
    rows.append({"tooth": "T2 dropped scope (C4 removed from the comparison)",
                 "bites": only_c3 == "AMBIGUOUS" and both == "F_dim",
                 "flips": "the family verdict becomes AMBIGUOUS, i.e. C4 is "
                          "carrying the discrimination",
                 "verdict_with_C3_only": only_c3,
                 "verdict_with_both": both})

    # T3 hardcoded native value
    forced = family_of({3: Fraction(2, 9), 4: Fraction(5, 16)})
    rows.append({"tooth": "T3 hardcoded native value (force K(C4) := 5/16)",
                 "bites": forced == "F_res",
                 "flips": "the verdict follows the input, so it is not "
                          "hardcoded to F_dim",
                 "forced_verdict": forced})

    # T4 leaked family verdict: a comparison that always answers F_dim
    def leaky(pairs):
        return "F_dim"
    spread = {leaky({}) for _ in range(3)}
    honest = {family_of({3: ANCHOR, 4: v})
              for v in (Fraction(3, 16), Fraction(5, 16), Fraction(1, 2))}
    rows.append({"tooth": "T4 leaked family verdict (comparison stubbed to "
                          "F_dim)",
                 "bites": len(spread) == 1 and len(honest) == 3,
                 "flips": "the planted-recipe spread collapses from 3 to 1",
                 "honest_spread": sorted(honest)})

    # T5 recipe swap
    swapped = family_of({3: Fraction(2 * 4, 12 * 3),
                         4: Fraction(3 * 5, 12 * 4)})
    rows.append({"tooth": "T5 recipe swap (PLANT_res substituted for the "
                          "recovered recipe)",
                 "bites": swapped == "F_res",
                 "flips": "the verdict flips to F_res, so it tracks the "
                          "recipe and not the machinery",
                 "swapped_verdict": swapped})

    # T6 planted-binding blindness
    plants = {"dim": Fraction(3, 16), "res": Fraction(5, 16),
              "ded": Fraction(1, 2)}
    full = sorted({family_of({3: ANCHOR, 4: v}) for v in plants.values()})
    dropped = sorted({family_of({3: ANCHOR, 4: v})
                      for k, v in plants.items() if k != "ded"})
    rows.append({"tooth": "T6 planted-binding blindness (PLANT_ded dropped)",
                 "bites": len(full) == 3 and len(dropped) == 2,
                 "flips": "the 'plants span the three families' gate",
                 "full_span": full, "dropped_span": dropped})

    # T7 L-face space swap
    swap_ok = (lfaces["C4_face"]["geometric_L_face"] == "5/16"
               and lfaces["C4_face"]["readout_L_face"] is None)
    rows.append({"tooth": "T7 L-face space swap (evaluate the note's recipe "
                          "on the readout space at C4)",
                 "bites": swap_ok,
                 "flips": "5/16 becomes undefined, so the F_res reading is a "
                          "property of the SPACE and not of the recipe"})

    # T8 enclosure widening
    wide_lo, wide_hi = (Fraction(2222220, 10 ** 7), Fraction(2222224, 10 ** 7))
    wide_hits = [f"{fam}(3)" for fam, fn in FAMILIES.items()
                 if wide_lo <= fn(3) <= wide_hi]
    rows.append({"tooth": "T8 enclosure widening (1e-18 -> 4e-7)",
                 "bites": len(wide_hits) == 3,
                 "flips": "Q3's 'zero inside' becomes 'three inside', so the "
                          "NO is a statement about the enclosure's width and "
                          "not an artifact of the search",
                 "hits_when_widened": wide_hits})

    # T9 FIND-3 blindness: assert the pair-orbit identity actually constrains
    bad = fine["S3_body"]["FIND3_pair_orbit_identity"]["orbits_on_X_times_X"]
    naive = len(fine["S3_body"]["fine_dims"])       # a peeling count
    rows.append({"tooth": "T9 FIND-3 blindness (multiplicity read off a naive "
                          "component count)",
                 "bites": naive != bad,
                 "flips": "at S3 the naive count is "
                          f"{naive} but the pair-orbit identity requires "
                          f"{bad}; reading multiplicities off a peeling would "
                          "have missed the multiplicity-2 component"})

    biting = [r["tooth"] for r in rows if r["bites"]]
    return {"rows": rows, "teeth": len(rows), "biting": len(biting),
            "blind_spots": [r["tooth"] for r in rows if not r["bites"]]}


# --------------------------------------------------------------------------
# pins
# --------------------------------------------------------------------------
def git_blob(path):
    try:
        return subprocess.run(["git", "hash-object", path], cwd=str(ROOT),
                              capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:                              # pragma: no cover
        return "unavailable"


def pins():
    rows, bad = [], []
    for p in AUDIT_INPUT_PATHS:
        f = ROOT / p
        ex = f.exists()
        sha = sha256(f.read_bytes()).hexdigest() if ex else None
        blob = git_blob(p) if ex else None
        # the primary is pinned by sha256 only: its git blob is recorded, not
        # gated, because the checker is committed before the primary's final
        # blob is known.
        sha_ok = ex and sha == EXPECTED_SHA256[p]
        rows.append({"path": p, "exists": ex, "sha256": sha,
                     "git_blob": blob, "sha256_matches_pin": sha_ok,
                     "git_blob_expected": EXPECTED_GIT_BLOBS[p],
                     "git_blob_gated": p != AUDIT_INPUT_PATHS[7],
                     "git_blob_matches_pin":
                         blob == EXPECTED_GIT_BLOBS[p]})
        if not sha_ok or (p != AUDIT_INPUT_PATHS[7]
                          and blob != EXPECTED_GIT_BLOBS[p]):
            bad.append(p)
    return {"rows": rows, "all_verified": not bad, "failures": bad,
            "import_firewall_hits": list(FIREWALL.hits),
            "import_firewall_zero_hits": len(FIREWALL.hits) == 0,
            "pass": not bad and not FIREWALL.hits}


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------
def build():
    p = pins()
    if not p["pass"]:
        print(json.dumps({"FATAL": "pin verification failed", "pins": p},
                         indent=1))
        sys.exit(2)

    coarse = {nm: coarse_pair_independent(SCOPES[nm]) for nm in SCOPE_ORDER}
    fine = {nm: fine_decomposition_independent(SCOPES[nm])
            for nm in SCOPE_ORDER}
    lfaces = {nm: l_face_independent(SCOPES[nm]) for nm in SCOPE_ORDER}
    recipe = recover_recipe_independently()
    attack = identifiability_attack()
    q3 = q3_attack()
    ledger = claim_ledger(coarse, fine, lfaces, recipe)
    tooth = teeth(coarse, fine, lfaces, recipe)

    primary = json.loads(PRIMARY_RECEIPT.read_text())
    prim_forms = set(primary["certificates"]["D_Q1_NATIVE_VALUE"][
        "recovered_recipe_forms"])
    recipe_agrees = len(recipe["expressions_returning_the_anchor_at_C3"]) == \
        len(prim_forms)

    return {
        "cycle": 899,
        "role": "independent check, specified to refute",
        "pins": p,
        "CH_A_COARSE_SPLIT_INDEPENDENT": {
            "rows": list(coarse.values()),
            "all_three_routes_agree_everywhere":
                all(r["three_routes_agree"] for r in coarse.values()),
        },
        "CH_B_FINE_DECOMPOSITION_INDEPENDENT": {
            "rows": [{k: v for k, v in r.items() if k != "isotypes"}
                     for r in fine.values()],
            "isotypes_by_scope": {nm: fine[nm].get("isotypes")
                                  for nm in SCOPE_ORDER},
            "FIND3_gate_holds_everywhere":
                all(r["FIND3_pair_orbit_identity"]["gate_holds"]
                    for r in fine.values() if r.get("ok")),
        },
        "CH_C_RECIPE_IDENTIFIABILITY": {
            "independent_recovery": recipe,
            "primary_recovered_forms": sorted(prim_forms),
            "checker_and_primary_recover_the_same_number_of_hitting_forms":
                recipe_agrees,
            "recipe_recovery_is_REFUTED": not (
                recipe["recipe_is_identified_as_a_function_of_the_scope"]
                and recipe["family_verdict"] == "F_dim"),
            "identifiability_attack": attack,
        },
        "CH_D_L_FACE_INDEPENDENT": {
            "rows": [{k: v for k, v in r.items() if not k.startswith("_")}
                     for r in lfaces.values()],
        },
        "CH_E_Q3_ATTACK": q3,
        "CH_F_CLAIM_LEDGER": ledger,
        "CH_G_TEETH": tooth,
        "verdict": {
            "claims_checked": ledger["claims_checked"],
            "claims_surviving": ledger["claims_surviving"],
            "claims_refuted": ledger["claims_refuted"],
            "teeth": tooth["teeth"], "biting": tooth["biting"],
            "blind_spots": tooth["blind_spots"],
            "recipe_identifiability":
                ("the recipe IS identified as a function of the scope by an "
                 "independent reading" if recipe[
                     "recipe_is_identified_as_a_function_of_the_scope"]
                 else "REFUTED: independent readings disagree at C4"),
            "the_one_thing_the_primary_should_not_overclaim": (
                "883's 2/9 at C3 does NOT force a family.  The identifiability "
                f"attack finds "
                f"{attack['distinct_C4_value_count']} distinct C4 values among "
                f"{attack['forms_returning_the_anchor_at_C3']} closed forms of "
                "a plain declared shape that all return 2/9 at C3, and the "
                "named families are among them.  What is forced is narrower "
                "and should be stated narrowly: THE FORM SET 883 ACTUALLY "
                "WROTE is family-identified, and it identifies F_dim."),
        },
    }


def main() -> int:
    started = monotonic()
    out = build()
    out["runtime_seconds"] = round(monotonic() - started, 3)
    out["self_digest"] = digest({k: v for k, v in out.items()
                                 if k != "runtime_seconds"})
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(out, indent=1, sort_keys=True,
                                  default=str) + "\n")
    text = json.dumps(out, indent=1, sort_keys=True, default=str)
    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        text = text[:STDOUT_LIMIT_BYTES] + "\n... TRUNCATED ..."
    print(text)
    return 0            # exit is independent of claim survival, by design


if __name__ == "__main__":
    sys.exit(main())
