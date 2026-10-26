#!/usr/bin/env python3
"""check.py for J:derive:review-20261016-nearest-site-prime-closure:a1

Exact (sympy rings over QQ, exact integer linear algebra) regeneration of the two
nearest-site spinorial families and their unitarity ideals from the declared signed
generators, an exhaustive elimination tree for each variety, trace-power flatness on
every leaf, and cross-validation against the printed Singular components.
Python with numpy, scipy, sympy only; one process; no files read or written.
The EMBED table holds hash-checked copies of source files (main at
2bb6c1a54721e70512922fb10d4495adf8ea3042) used only for comparison.
Expected runtime: about 4-5 minutes of CPU (longer on a loaded machine); peak memory about 120 MB.
"""
EMBED = {
  'model.json': ('1c34e2ea4264c0872e1438bb31984fb7d6dd1122bf407ba0058983cd2fa89159', (
      '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'
  )),
  'model1.json': ('271cd5acd6f16289a4ad2b16d9e2d6a9eedd5ed509e35617fb427e204d858a81', (
      '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'
  )),
  'sing0.log': ('f5acab33a55d85c5d3fa064faa67d86219dc074af0ca01781b1f0ad2065faf41', (
      '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'
      'pof/AhObvEI='
  )),
  'sing1.log': ('9840f520b80a09a6c4c91399a32cd8cc1b7189560f41476a8a26032d05fb4672', (
      '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'
      'oP6EYxZdo/7nxyy+PM16NcrHrCaFhH8B4FGvVQ=='
  )),
  'nn_min.sing': ('cb52d7ca90e8468126472aed7418ccbee79175d0bd36e98dd30791b2c356a11a', (
      'eNrFV02PmzAUvOdXoJwg4AowBluUQ3updrXHnlr1UEhaIW2yqySnVv3vtYPhjR2y20QrNVIkY8bjec/vwzzcfQyWz/t+u9507x77'
      'dlkv9v3uZ7Bv0iTs0qTLki5POp50RdKJpCuTrko6mXRKv9KvW/PXmFaDWo1qNazVuFYDW41sNbRVBpNGyfq5XvTrzffH4K5ZhCyL'
      'Vl26Mq+S4SEzT+NDvjIkw7hcmQ1ohYrtAsBkJ6aYFiv7QpnFMeyQwQ5FHJphARuYaTFMC5g2kHKYNnIKOy3caQGKs5gEpKDewjMw'
      'JEc3mLXpgFFAc9KOInPSLmJaWp5DxGDpGcQwVnqeWzk8Ds2QD7saROVprwaEBbNX0BLOqYCxdS8Hg3xvSIKUMblauHBAMx9eDKdk'
      'hhKmFWhR4LqTe3ky2XGKJW4Xq8FshTad3OHiAc4u4ScLOR1fRsdkhxI8yTGyC/CTICeYU5UQqXjanChzMDyDCBbEwi3kEjz1zjKn'
      'aJaYfXR+ggzFwBO00OUAisn+gjyECV/GTipPcAW+TWmpBK8ol8bLfI9Egseno7AsU/0gH2bgQ0GZzGlYYlTYKBXg8dINhcIhYbMs'
      'AmIrg2gB+znULyLHOpW7JCMHJw60XoCdcyype7ZeCWD5WObh5KQb5xDm5BcsMRw4q/n6kZ7XSUEeqFxP5y73zdTsBW4/V6rzQPfy'
      'hgM5J905HKLLfTM1e4E7dy3OMCnscZYQw9KLVghip+iWSThXu8V870KNCjRCx6yQXV7LfoGcXWJnr9QLLDoV0ZfgJUhGLBf/xA3U'
      '7Hru1Gb02NQzO7aXh6nBj81+7C2cGsdpXMKuFdwqpBU8dkPlXMSGM8PQLSh0OYRu7lYIr2/6PbGCnkgOF+QI7HHOveCNlMwLYTcq'
      'EReVzBXN6uwu4V8TyCXFTKb6SsS1Sq4Rwm5RkhJjRhUJrwA5lBgOuVG4t2YZY9+dySlFruJuSmF7p3Z8rcA30MduEQh3LrwtcO8W'
      'Jc4uAPARJLzeUUKZK+CDCCRKivsKvm9SrAnqv0gEhex1ieNX7H1zOK7Du6gO9Bf07hgu1/12OT3ph/A+iurFY384Bg/Ntt99OBw+'
      'ff5iVizsiu5p+/y02+yOB1p46H9twgezUj8FfR38eNqHfZPV/fvGvqv7OI5+j9s2TTDxBMv4cDSf8GEfxctAi6AZo8gofvjaf4v0'
      'b9zw9FwHfxZ/AdcUy/E='
  )),
  'nn_min.out': ('8341787d5d1ddac9f875bfa49d19ef8d7415c2f173edb0ffd975d6dc1aa72412', (
      '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'
      'z97/5Nn7V16jLDI='
  )),
}

# ---------------------------------------------------------------------------
# check.py body.  Everything below is regenerated from the declared signed
# generators; the embedded blobs above are only the SOURCE files (hash-checked)
# used for comparison.
# ---------------------------------------------------------------------------
import sys, time, json, re, itertools, hashlib, zlib, base64, math, warnings
import numpy as np
import sympy as sp
from sympy import QQ
from sympy.polys.rings import ring
from sympy.polys.orderings import grevlex
from sympy.polys.groebnertools import groebner as ring_gb

warnings.filterwarnings("ignore")
T0 = time.time()
RESULTS = []
INFEAS = {}


def rec(ok, msg):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + msg, flush=True)


def blob(name):
    h, chunks = EMBED[name]
    raw = zlib.decompress(base64.b64decode("".join(chunks)))
    return raw, h


# ---------------------------------------------------------------- geometry
corners = list(itertools.product([0, 1], repeat=3))
cidx = {v: i for i, v in enumerate(corners)}
offs = list(itertools.product([-1, 0, 1], repeat=3))
RZ = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
RX = ((1, 0, 0), (0, 0, -1), (0, 1, 0))


def apply_R(R, v):
    return tuple(sum(R[i][j] * v[j] for j in range(3)) for i in range(3))


def corner_perm(R):
    p = {}
    for v in corners:
        w = apply_R(R, tuple(2 * a - 1 for a in v))
        p[v] = tuple((a + 1) // 2 for a in w)
    return p


def D_matrix(R, signs):
    """D e_v = signs[v] e_{R v}   (entry-sign convention)"""
    p = corner_perm(R)
    M = np.zeros((8, 8), dtype=np.int64)
    for v in corners:
        M[cidx[p[v]], cidx[v]] = signs[cidx[v]]
    return M


def mat_mul3(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def build_group(Dz, Dx):
    I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    I8 = np.eye(8, dtype=np.int64)
    seen = {(I3, I8.tobytes()): (I3, I8)}
    fr = [(I3, I8)]
    gens = [(RZ, Dz), (RX, Dx)]
    while fr:
        nf = []
        for R, D in fr:
            for Rg_, Dg in gens:
                R2 = mat_mul3(Rg_, R)
                D2 = Dg @ D
                k = (R2, D2.tobytes())
                if k not in seen:
                    seen[k] = (R2, D2)
                    nf.append((R2, D2))
        fr = nf
        if len(seen) > 400:
            return None
    return list(seen.values())


# --------------------------------------------------- Part A: sign-pair census
def partA():
    Pz = D_matrix(RZ, [1] * 8)
    Px = D_matrix(RX, [1] * 8)
    I8 = np.eye(8, dtype=np.int64)

    def quarter_ok(P, s):
        D = P * np.array(s)[None, :]
        return np.array_equal(np.linalg.matrix_power(D, 4), -I8)

    SZ = [s for s in itertools.product([1, -1], repeat=8) if quarter_ok(Pz, s)]
    SX = [s for s in itertools.product([1, -1], repeat=8) if quarter_ok(Px, s)]
    reps = []
    for sz in SZ:
        Dz = Pz * np.array(sz)[None, :]
        for sx in SX:
            Dx = Px * np.array(sx)[None, :]
            G = build_group(Dz, Dx)
            if G is not None and len(G) == 48:
                reps.append((sz, sx, frozenset(D.tobytes() for R, D in G)))
    rec(len(SZ) == 64 and len(SX) == 64, "A1 sign vectors with D^4=-1: %d (Rz), %d (Rx)" % (len(SZ), len(SX)))
    rec(len(reps) == 512, "A2 sign pairs generating an order-48 signed group with central -1: %d" % len(reps))
    groups = {}
    for sz, sx, key in reps:
        groups.setdefault(key, (sz, sx))
    rec(len(groups) == 128, "A3 distinct generated matrix groups: %d" % len(groups))
    Ss = [np.diag(s).astype(np.int64) for s in itertools.product([1, -1], repeat=8)]
    CLS = {0: ([1, 1, 1, 1, -1, -1, 1, 1], [1, 1, -1, 1, -1, -1, 1, -1]),
           1: ([1, 1, 1, 1, -1, -1, 1, 1], [-1, 1, 1, 1, -1, -1, -1, 1])}
    keys = {}
    for c, (sz, sx) in CLS.items():
        G = build_group(D_matrix(RZ, sz), D_matrix(RX, sx))
        keys[c] = frozenset(D.tobytes() for R, D in G)

    def conj_key(key, S):
        return frozenset((S @ np.frombuffer(b, dtype=np.int64).reshape(8, 8) @ S).tobytes() for b in key)

    cache = {c: set(conj_key(keys[c], S) for S in Ss) for c in (0, 1)}
    cnt = {0: 0, 1: 0}
    other = 0
    for key in groups:
        hit = None
        for c in (0, 1):
            if key in cache[c]:
                hit = c
                break
        if hit is None:
            other += 1
        else:
            cnt[hit] += 1
    rec(other == 0 and cnt[0] > 0 and cnt[1] > 0,
        "A4 every one of the 128 groups is diagonal-sign-gauge equivalent to class 0 (%d groups) or class 1 (%d groups); none other" % (cnt[0], cnt[1]))
    rec(keys[1] not in cache[0], "A5 class 0 and class 1 are not diagonal-sign-gauge equivalent")
    return CLS


# ------------------------------------------------- Part B: family and ideal
def allowed_entries():
    out = []
    for n in offs:
        for vo in corners:
            for vi in corners:
                if all(abs(vo[a] - vi[a] - 2 * n[a]) <= 1 for a in range(3)):
                    out.append((n, vo, vi))
    return out


def family(sz, sx):
    Dz, Dx = D_matrix(RZ, sz), D_matrix(RX, sx)
    G = build_group(Dz, Dx)
    assert G is not None and len(G) == 48
    ent = allowed_entries()
    eset = set(ent)
    pat = {}
    params = []
    for e in ent:
        if e in pat:
            continue
        sgn = {e: 1}
        stack = [e]
        ok = True
        while stack:
            x = stack.pop()
            n, vo, vi = x
            io, ii = cidx[vo], cidx[vi]
            for R, D in G:
                Rn = apply_R(R, n)
                jo = int(np.nonzero(D[:, io])[0][0])
                ji = int(np.nonzero(D[:, ii])[0][0])
                s = int(D[jo, io] * D[ji, ii])
                y = (Rn, corners[jo], corners[ji])
                assert y in eset
                if y in sgn:
                    if sgn[y] != sgn[x] * s:
                        ok = False
                else:
                    sgn[y] = sgn[x] * s
                    stack.append(y)
        if ok:
            k = len(params)
            params.append(sorted(sgn))
            for y, s in sgn.items():
                pat[y] = (k, s)
        else:
            for y in sgn:
                pat[y] = None
    return G, params, pat


NAMES = ['c%d' % i for i in range(11)] + ['cb%d' % i for i in range(11)]
Rg, *GENS = ring(NAMES, QQ, order=grevlex)
CG = GENS[:11]
CBG = GENS[11:]
ZERO = Rg.zero


def normalize(p):
    return p if p.LC > 0 else -p


def build_matrices(pat):
    A = {n: [[ZERO] * 8 for _ in range(8)] for n in offs}
    Ab = {n: [[ZERO] * 8 for _ in range(8)] for n in offs}
    for (n, vo, vi), v in pat.items():
        if v is None:
            continue
        k, s = v
        A[n][cidx[vo]][cidx[vi]] = s * CG[k]
        Ab[n][cidx[vo]][cidx[vi]] = s * CBG[k]
    return A, Ab


def unitarity(A, Ab, two_sided):
    eqs = []
    for m in itertools.product(range(-2, 3), repeat=3):
        S = [[ZERO] * 8 for _ in range(8)]
        for n in offs:
            n2 = tuple(a + b for a, b in zip(n, m))
            if n2 not in A:
                continue
            for i in range(8):
                for j in range(8):
                    t = ZERO
                    for l in range(8):
                        if two_sided:
                            a, b = A[n2][i][l], Ab[n][j][l]
                        else:
                            a, b = Ab[n][l][i], A[n2][l][j]
                        if a != 0 and b != 0:
                            t += a * b
                    S[i][j] += t
        if m == (0, 0, 0):
            for i in range(8):
                S[i][i] -= 1
        for i in range(8):
            for j in range(8):
                if S[i][j] != 0:
                    eqs.append(S[i][j])
    return eqs


def parse_src_poly(s):
    ex = sp.sympify(s)
    sub = {}
    for sy in ex.free_symbols:
        n = str(sy)
        if n.startswith('cb'):
            sub[sy] = sp.Symbol('cb%d' % (int(n[2:]) - 1))
        else:
            sub[sy] = sp.Symbol('c%d' % (int(n[1:]) - 1))
    return Rg.from_expr(ex.xreplace(sub))


def partB(CLS):
    FAM = {}
    for c in (0, 1):
        sz, sx = CLS[c]
        G, params, pat = family(sz, sx)
        A, Ab = build_matrices(pat)
        eq1 = unitarity(A, Ab, False)
        eq2 = unitarity(A, Ab, True)
        FAM[c] = dict(G=G, params=params, pat=pat, A=A, Ab=Ab,
                      E=sorted(set(normalize(e) for e in eq1), key=str),
                      E2=sorted(set(normalize(e) for e in eq2), key=str))
        sizes = [len(p) for p in params]
        rec(len(G) == 48 and len(params) == 11 and sizes == [8, 24, 24, 24, 24, 24, 24, 8, 24, 24, 8],
            "B1.%d class %d: signed group order 48; covariant nearest-site family has %d complex parameters, orbit sizes %s" % (c, c, len(params), sizes))
        # source comparison (entry by entry) and equation set comparison
        raw, h = blob('model.json' if c == 0 else 'model1.json')
        rec(hashlib.sha256(raw).hexdigest() == h, "B2.%d embedded source %s matches task sha256" % (c, 'model.json' if c == 0 else 'model1.json'))
        m = json.loads(raw)
        bad = 0
        for n in offs:
            Asrc = m['A'][str(n)]
            for vo in corners:
                for vi in corners:
                    s = Asrc[cidx[vo]][cidx[vi]]
                    mine = A[n][cidx[vo]][cidx[vi]]
                    if s == '0':
                        bad += (mine != 0)
                    else:
                        want = parse_src_poly(s)
                        bad += (want != mine)
        rec(bad == 0, "B3.%d class %d: regenerated hop matrices A_n equal the source model entry-by-entry (mismatches %d)" % (c, c, bad))
        srcE = set(normalize(parse_src_poly(e)) for e in m['eqs'])
        rec(len(m['eqs']) == 79 and srcE == set(FAM[c]['E']),
            "B4.%d class %d: regenerated W^dagger W = 1 polynomials (%d distinct up to sign) equal the source's 79 listed polynomials (%d up to sign)" % (c, c, len(FAM[c]['E']), len(srcE)))
    # nn_min.sing (original nearest_site input) vs class 0 / class 1 two-sided
    raw, h = blob('nn_min.sing')
    rec(hashlib.sha256(raw).hexdigest() == h, "B5 embedded nn_min.sing matches task sha256")
    txt = raw.decode()
    body = txt.split("ideal I=")[1].split(";\nideal J")[0].replace("\n", "").split(",")
    flip = {3, 4, 8, 9}

    def flipp(p):
        d = {}
        for mon, co in p.terms():
            s = 1
            for k in flip:
                s *= (-1) ** (mon[k] + mon[11 + k])
            d[mon] = co * s
        return Rg.from_dict(d)

    nn = [Rg.from_expr(sp.sympify(s.replace("^", "**"))) for s in body]
    nnf = set(normalize(flipp(p)) for p in nn)
    for c in (0, 1):
        two = set(FAM[c]['E']) | set(FAM[c]['E2'])
        if c == 0:
            rec(len(nn) == 55 and nnf == two,
                "B6 nn_min.sing's 55 generators = class-0 two-sided (W^dagger W and W W^dagger) unitarity set, after sign flips c3,c4,c8,c9 -> -c (exact set equality)")
        else:
            rec(nnf != two, "B6' control: the same 55 generators are NOT the class-1 two-sided set")
    # independent linear-algebra count of the covariant family (exact rank over Q)
    from sympy.polys.matrices import DomainMatrix
    ent = allowed_entries()
    idx = {e: i for i, e in enumerate(ent)}
    sz, sx = CLS[0]
    rows = []
    for Rm, Dm in [(RZ, D_matrix(RZ, sz)), (RX, D_matrix(RX, sx))]:
        for n in offs:
            Rn = apply_R(Rm, n)
            for a in range(8):
                for b in range(8):
                    row = {}
                    key = (Rn, corners[a], corners[b])
                    if key in idx:
                        row[idx[key]] = row.get(idx[key], 0) + 1
                    for ap in range(8):
                        if Dm[a, ap] == 0:
                            continue
                        for bp in range(8):
                            if Dm[b, bp] == 0:
                                continue
                            k2 = (n, corners[ap], corners[bp])
                            if k2 in idx:
                                row[idx[k2]] = row.get(idx[k2], 0) - int(Dm[a, ap] * Dm[b, bp])
                    row = {k: v for k, v in row.items() if v != 0}
                    if row:
                        rows.append(row)
    M = [[QQ(0)] * len(ent) for _ in rows]
    for i, r in enumerate(rows):
        for k, v in r.items():
            M[i][k] = QQ(v)
    dm = DomainMatrix(M, (len(rows), len(ent)), QQ)
    rk = dm.rank()
    rec(len(ent) == 216 and len(ent) - rk == 11,
        "B7 independent exact linear algebra (covariance of the two generators only): %d allowed entries, rank %d, solution space dimension %d" % (len(ent), rk, len(ent) - rk))
    return FAM


# --------------------------------------------- Part C: elimination tree

_SUBRINGS = {}


def gb_sub(gens, base_ring, names):
    """Groebner basis (sympy buchberger, grevlex) computed in the sub-ring of the variables that actually occur
    (the relative variable order is kept, so the reduced basis is the same as in the full ring); mapped back."""
    active = sorted(set(i for p in gens for m, _ in p.terms() for i, e in enumerate(m) if e))
    key = (id(base_ring), tuple(active))
    if key not in _SUBRINGS:
        _SUBRINGS[key] = ring([names[i] for i in active], QQ, order=grevlex)[0]
    Rs = _SUBRINGS[key]
    conv = [Rs.from_dict({tuple(m[i] for i in active): co for m, co in p.terms()}) for p in gens]
    G = ring_gb(conv, Rs)
    nv = len(base_ring.gens)
    out = []
    for q in G:
        d = {}
        for m, co in q.terms():
            mm = [0] * nv
            for j, i in enumerate(active):
                mm[i] = m[j]
            d[tuple(mm)] = co
        out.append(base_ring.from_dict(d))
    return out

def zsub(p, zs):
    if not zs:
        return p
    d = {m: co for m, co in p.terms() if not any(m[i] for i in zs)}
    return p.ring.from_dict(d) if d else p.ring.zero


def subs_one(p, v):
    d = {}
    for m, co in p.terms():
        mm = list(m)
        mm[v] = 0
        mm = tuple(mm)
        d[mm] = d.get(mm, 0) + co
    d = {m: co for m, co in d.items() if co != 0}
    return p.ring.from_dict(d) if d else p.ring.zero


def is_const(p):
    return all(sum(m) == 0 for m, _ in p.terms())


def monomial_leaves(E):
    """exhaustive case split on monomial generators (x*y*... = 0 -> one factor vanishes)."""
    leaves = []
    seen = set()

    def rec_(zset, P):
        P = [zsub(p, zset) for p in P]
        P = [p for p in P if p != 0]
        for p in P:
            if is_const(p):
                return
        best = None
        for p in P:
            ts = p.terms()
            if len(ts) == 1:
                vs = [i for i, e in enumerate(ts[0][0]) if e]
                if best is None or len(vs) < len(best):
                    best = vs
        if best is not None:
            for v in best:
                rec_(zset | {v}, P)
            return
        key = frozenset(zset)
        if key in seen:
            return
        seen.add(key)
        leaves.append((frozenset(zset), P))

    rec_(frozenset(), E)
    return [(z, P) for z, P in leaves if not any(z2 < z for z2, _ in leaves)]


class Decomposer:
    def __init__(self):
        self.memo = set()
        self.leaves = []
        self.nodes = 0
        self.nsplit_f = 0
        self.nsplit_m = 0
        self.nzero = 0

    def expand(self, zs, one, gens):
        gens = [zsub(p, zs) for p in gens]
        gens = [p for p in gens if p != 0]
        if any(is_const(p) for p in gens):
            return
        best = None
        for p in gens:
            ts = p.terms()
            if len(ts) == 1:
                vs = [i for i, e in enumerate(ts[0][0]) if e]
                if best is None or len(vs) < len(best):
                    best = vs
        if best is not None:
            self.nsplit_m += 1
            for v in best:
                self.expand(zs | {v}, one, gens)
            return
        G = gb_sub(gens, Rg, NAMES)
        if any(is_const(p) for p in G):
            return
        key = (frozenset(zs), one, tuple(sorted(tuple(sorted(p.terms())) for p in G)))
        if key in self.memo:
            return
        self.memo.add(key)
        self.nodes += 1
        cand = None
        for p in G:
            ts = p.terms()
            if len(ts) == 1:
                mon = ts[0][0]
                vs = [i for i, e in enumerate(mon) if e]
                if len(vs) == 1:
                    cand = ('var', vs)
                    break
                score = (len(vs), sum(mon))
                if cand is None or score < cand[2]:
                    cand = ('mono', vs, score)
        if cand is not None:
            self.nsplit_m += 1
            if cand[0] == 'var':
                return self.expand(zs | {cand[1][0]}, one, G)
            for v in cand[1]:
                self.expand(zs | {v}, one, G)
            return
        best = None
        for p in G:
            cst, fl = p.factor_list()
            facs = [f for f, mult in fl if not is_const(f)]
            if len(facs) >= 2:
                # exact check that the factorization multiplies back
                prod = Rg.one * cst
                for f, mult in fl:
                    prod = prod * f ** mult
                assert prod == p
                score = (sum(p.terms()[0][0]), len(p.terms()))
                if best is None or score < best[0]:
                    best = (score, facs)
        if best is None:
            self.leaves.append((frozenset(zs), one, G))
            return
        self.nsplit_f += 1
        for f in best[1]:
            self.expand(zs, one, G + [f])

    def root_leaf(self, zs, P):
        cfree = [i for i in range(11) if i not in zs]
        zc = set(zs)
        for a in cfree:
            Q = [subs_one(zsub(p, zc), a) for p in P]
            Q = [p for p in Q if p != 0]
            self.expand(frozenset(zc), a, Q)
            zc = zc | {a}
        Q = [zsub(p, zc) for p in P]
        # all free c vanish: the normalisation equation becomes -1 = 0
        assert any(is_const(p) for p in Q if p != 0)


def decompose(E):
    D = Decomposer()
    roots = monomial_leaves(E)
    for zs, P in roots:
        D.root_leaf(zs, P)
    return D, roots


# -------------------------------------------------------- Part D: flatness
def W_dict(pat):
    W = [[dict() for _ in range(8)] for _ in range(8)]
    for (n, vo, vi), v in pat.items():
        if v is None:
            continue
        k, s = v
        W[cidx[vo]][cidx[vi]][n] = s * CG[k]
    return W


def nf(p, G):
    return p.rem(G) if G else p


def mat_mul(X, Y, G):
    out = [[dict() for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for l in range(8):
            xi = X[i][l]
            if not xi:
                continue
            for j in range(8):
                yj = Y[l][j]
                if not yj:
                    continue
                o = out[i][j]
                for n1, p1 in xi.items():
                    for n2, p2 in yj.items():
                        n = (n1[0] + n2[0], n1[1] + n2[1], n1[2] + n2[2])
                        q = p1 * p2
                        o[n] = o[n] + q if n in o else q
    for i in range(8):
        for j in range(8):
            d = out[i][j]
            for n in list(d):
                r = nf(d[n], G)
                if r == 0:
                    del d[n]
                else:
                    d[n] = r
    return out


def tr_of(X, G):
    t = {}
    for i in range(8):
        for n, p in X[i][i].items():
            t[n] = t[n] + p if n in t else p
    return {n: nf(q, G) for n, q in t.items()}


def tr_prod(X, Y, G):
    t = {}
    for i in range(8):
        for l in range(8):
            xi, yl = X[i][l], Y[l][i]
            if not xi or not yl:
                continue
            for n1, p1 in xi.items():
                for n2, p2 in yl.items():
                    n = (n1[0] + n2[0], n1[1] + n2[1], n1[2] + n2[2])
                    q = p1 * p2
                    t[n] = t[n] + q if n in t else q
    return {n: nf(q, G) for n, q in t.items()}


def flat_bad(Wd, zs, one, G, pmax=8):
    """returns list of (p, number of nonconstant z-monomials whose coefficient does not reduce to 0 mod G)"""
    def prep(p):
        p = zsub(p, zs)
        if p != 0 and one is not None:
            p = subs_one(p, one)
        return p
    W = [[{n: q for n, q in ((n, prep(p)) for n, p in e.items()) if q != 0} for e in row] for row in Wd]
    pw = {1: W}
    for p in (2, 3, 4):
        if p <= min(pmax, 4):
            pw[p] = mat_mul(pw[p - 1], W, G)
    bad = []

    def chk(p, tr):
        nz = [n for n, q in tr.items() if q != 0 and n != (0, 0, 0)]
        if nz:
            bad.append((p, len(nz)))

    for p in (1, 2, 3, 4):
        if p <= pmax:
            chk(p, tr_of(pw[p], G))
    if pmax >= 5:
        chk(5, tr_prod(pw[2], pw[3], G))
    if pmax >= 6:
        chk(6, tr_prod(pw[3], pw[3], G))
    if pmax >= 7:
        chk(7, tr_prod(pw[3], pw[4], G))
    if pmax >= 8:
        chk(8, tr_prod(pw[4], pw[4], G))
    return bad


# ----------------------------------------------------- Part E: primes
def parse_b8_primes(text):
    parts = re.split(r'^prime (\d+)\n', text, flags=re.M)
    primes = []
    for k in range(1, len(parts), 2):
        body = parts[k + 1]
        gens = re.findall(r'^_\[\d+\]=(.*)$', body, flags=re.M)
        dim = int(re.search(r'dim (\d+)', body).group(1))
        primes.append((dim, [parse_src_poly(g.replace('^', '**')) for g in gens]))
    return primes


def parse_nn_out(text, flipfun):
    comps = re.split(r'^== component (\d+) dim (\d+)\n', text, flags=re.M)
    out = []
    for k in range(1, len(comps), 3):
        dim = int(comps[k + 1])
        body = comps[k + 2].replace("\n", "")
        gens = [g for g in body.split(",") if g.strip()]
        polys = []
        for g in gens:
            ex = sp.sympify(g.replace('^', '**'))
            polys.append(flipfun(Rg.from_expr(ex)))
        out.append((dim, polys))
    return out


def leaf_in_prime(zs, one, G, P):
    maxpow = 1
    for g in P:
        h = zsub(g, zs)
        if h != 0 and one is not None:
            h = subs_one(h, one)
        if h == 0:
            continue
        r = nf(h, G)
        if r == 0:
            continue
        hp = h
        good = False
        for k in range(2, 4):
            hp = nf(hp * h, G)
            if hp == 0:
                good = True
                maxpow = max(maxpow, k)
                break
        if not good:
            return None
    return maxpow



# ------------------------------------------------ Part G: real-locus closure
RN = ['x%d' % i for i in range(11)] + ['y%d' % i for i in range(11)] + ['r']
RR, *RG = ring(RN, QQ, order=grevlex)
RX_, RY_, RV_ = RG[:11], RG[11:22], RG[22]


def orbit_type(e):
    n, vo, vi = e
    t = []
    for a in range(3):
        if n[a] != 0:
            t.append('o')
        elif vo[a] != vi[a]:
            t.append('i')
        else:
            t.append('0')
    return ''.join(sorted(t, key=lambda x: 'o0i'.index(x)))


def to_real(p, zs, one):
    """Real points: cb = conj(c).  On the chart c_one = 1 (obtained from the point by the scaling
    c -> c/c_one, cb -> c_one*cb) one has c'_k = x_k + i y_k, cb'_k = r*(x_k - i y_k), r = |c_one|^2 > 0,
    c'_one = 1, cb'_one = r.  Returns the real and imaginary parts as polynomials over Q."""
    re = RR.zero
    im = RR.zero
    for m, co in p.terms():
        tre, tim = RR.one, RR.zero
        ok = True
        for k in range(22):
            e = m[k]
            if not e:
                continue
            if k < 11:
                if k == one:
                    continue
                if k in zs:
                    ok = False
                    break
                base = (RX_[k], RY_[k])
            else:
                kk = k - 11
                if kk in zs or k in zs:
                    ok = False
                    break
                if kk == one:
                    base = (RV_, RR.zero)
                else:
                    base = (RV_ * RX_[kk], -RV_ * RY_[kk])
            for _ in range(e):
                tre, tim = tre * base[0] - tim * base[1], tre * base[1] + tim * base[0]
        if ok:
            re += co * tre
            im += co * tim
    return re, im


def sos_monomials(q):
    ts = q.terms()
    sgn = 1 if ts[0][1] > 0 else -1
    for m, co in ts:
        if co * sgn <= 0:
            return None
        for k in range(22):
            if m[k] % 2:
                return None
    return [m for m, co in ts]


def real_rec(polys, zr, zs, one):
    """Real points (r > 0) of the polynomial system with the real variables in zr set to 0.
    Rules (all sound): a constant or a pure power of r in the Groebner basis -> no points;
    a monomial -> one of its x,y-variables vanishes; a polynomial whose monomials are all even in
    every x,y-variable with coefficients of one sign -> each monomial vanishes.
    Returns a list of residual 'stuck' states (support upper bounds)."""
    def sub0(q):
        d = {m: co for m, co in q.terms() if not any(m[i] for i in zr)}
        return RR.from_dict(d) if d else RR.zero

    P = [sub0(q) for q in polys]
    P = [q for q in P if q != 0]
    if any(all(sum(m) == 0 for m, _ in q.terms()) for q in P):
        return []
    G = gb_sub(P, RR, RN) if P else []
    if any(all(sum(m) == 0 for m, _ in q.terms()) for q in G):
        return []
    for q in G:
        ts = q.terms()
        if len(ts) == 1:
            vs = [i for i, e in enumerate(ts[0][0]) if e and i != 22]
            if not vs:
                return []
            out = []
            for v in vs:
                out += real_rec(G, zr | {v}, zs, one)
            return out
        info = sos_monomials(q)
        if info is not None:
            best = None
            for m in info:
                vs = [i for i, e in enumerate(m) if e and i != 22]
                if not vs:
                    return []
                if best is None or len(vs) < len(best):
                    best = vs
            out = []
            for v in best:
                out += real_rec(G, zr | {v}, zs, one)
            return out
    sup = set()
    for k in range(11):
        if k in zs or k + 11 in zs:
            continue
        if k in zr and k + 11 in zr:
            continue
        sup.add(k)
    if one is not None:
        sup.add(one)
    return [frozenset(sup)]


def real_close(G, zs, one):
    polys = []
    for g in G:
        re, im = to_real(g, zs, one)
        for q in (re, im):
            if q != 0:
                polys.append(q)
    return real_rec(polys, frozenset(), zs, one)


# ------------------------------------------------------- Part F: numerics
def compile_polys(E):
    mons, co, idx = [], [], []
    for k, p in enumerate(E):
        for m, c in p.terms():
            mons.append(m)
            co.append(float(c))
            idx.append(k)
    return np.array(mons, dtype=int), np.array(co), np.array(idx), len(E)


def evalp(cp, v):
    mons, co, idx, n = cp
    vals = np.prod(np.where(mons > 0, v[None, :] ** mons, 1.0), axis=1) * co
    out = np.zeros(n, dtype=complex)
    np.add.at(out, idx, vals)
    return out


def find_solutions(E, nstart, seed):
    from scipy.optimize import least_squares
    cp = compile_polys(E)
    rng = np.random.default_rng(seed)
    sols = []

    def res(x):
        z = x[:11] + 1j * x[11:]
        r = evalp(cp, np.concatenate([z, np.conj(z)]))
        return np.concatenate([r.real, r.imag])

    for _ in range(nstart):
        x0 = rng.normal(size=22) * rng.choice([0.2, 0.5, 1.0])
        mask = rng.random(11) < rng.choice([0.3, 0.6, 1.0])
        x0[:11] *= mask
        x0[11:] *= mask
        r = least_squares(res, x0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=400)
        if np.abs(r.fun).max() < 1e-11:
            sols.append(r.x[:11] + 1j * r.x[11:])
    return sols


def W_numeric(pat, c, k):
    W = np.zeros((8, 8), dtype=complex)
    for (n, vo, vi), v in pat.items():
        if v is None:
            continue
        kk, s = v
        W[cidx[vo], cidx[vi]] += s * c[kk] * np.exp(1j * np.dot(k, n))
    return W



def leaf_contains(cvec, cbv, leaf, tol=1e-4, ztol=1e-4):
    """does the numerical point (c, cb) (after the chart scaling) satisfy the zero pattern and every basis element of the leaf?
    Tolerances are loose on purpose: at points where the ideal is not radical (e.g. the constant walk, c7*cb7 = 1) a
    residual of 1e-11 only fixes the remaining coordinates to about 3e-6."""
    zs, one, G = leaf
    if any(abs(cvec[i]) > ztol for i in zs if i < 11) or any(abs(cbv[i - 11]) > ztol for i in zs if i >= 11):
        return False
    if one is not None:
        if abs(cvec[one]) < 1e-9:
            return False
        lam = 1.0 / cvec[one]
    else:
        lam = 1.0
    v = np.concatenate([cvec * lam, cbv / lam])
    for g in G:
        val = 0
        for m, co in g.terms():
            val += float(co) * np.prod([v[i] ** e for i, e in enumerate(m) if e])
        if abs(val) > tol:
            return False
    return True


def find_complex_solutions(E, nstart, seed):
    """points of the complex variety V(I) (c and cb independent)"""
    from scipy.optimize import least_squares
    cp = compile_polys(E)
    rng = np.random.default_rng(seed)
    sols = []

    def res(x):
        v = x[:22] + 1j * x[22:]
        r = evalp(cp, v)
        return np.concatenate([r.real, r.imag])

    for _ in range(nstart):
        x0 = rng.normal(size=44) * rng.choice([0.2, 0.5, 1.0])
        mask = rng.random(11) < rng.choice([0.3, 0.6, 1.0])
        mk = np.concatenate([mask, mask, mask, mask])
        mk = np.concatenate([mask, mask, mask, mask])
        x0[:11] *= mask; x0[11:22] *= mask; x0[22:33] *= mask; x0[33:] *= mask
        r = least_squares(res, x0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=300)
        if np.abs(r.fun).max() < 1e-11:
            v = r.x[:22] + 1j * r.x[22:]
            sols.append((v[:11], v[11:]))
    return sols


# =============================================================== main
def main():
    CLS = partA()
    FAM = partB(CLS)
    LEAVES = {}
    for c in (0, 1):
        t = time.time()
        D, roots = decompose(FAM[c]['E'])
        LEAVES[c] = D.leaves
        rec(len(roots) > 0 and len(D.leaves) > 0,
            "C1.%d class %d: elimination tree built: %d monomial-split roots, %d tree nodes, %d factor splits, %d leaves (%.0fs)" % (c, c, len(roots), D.nodes, D.nsplit_f, len(D.leaves), time.time() - t))
        # leaves lie in V(I): every original generator reduces to 0 modulo each leaf basis
        okI = True
        okJ = True
        for zs, one, G in D.leaves:
            for p in FAM[c]['E']:
                h = zsub(p, zs)
                if h != 0 and one is not None:
                    h = subs_one(h, one)
                if h != 0 and nf(h, G) != 0:
                    okI = False
            for p in FAM[c]['E2']:
                h = zsub(p, zs)
                if h != 0 and one is not None:
                    h = subs_one(h, one)
                if h != 0 and nf(h, G) != 0:
                    okJ = False
        rec(okI, "C2.%d class %d: every original W^dagger W - 1 generator reduces to 0 modulo every leaf basis (each leaf variety lies in V(I); with C1 this makes V(I) equal to the union of the leaves)" % (c, c))
        rec(okJ, "C3.%d class %d: every W W^dagger - 1 generator also reduces to 0 modulo every leaf basis (same variety for the two-sided ideal)" % (c, c))
    # flatness
    for c in (0, 1):
        t = time.time()
        Wd = W_dict(FAM[c]['pat'])
        allbad = []
        for j, (zs, one, G) in enumerate(LEAVES[c]):
            b = flat_bad(Wd, zs, one, G, 8)
            if b:
                allbad.append((j, b))
        rec(not allbad, "D1.%d class %d: on all %d leaves, every non-constant z-coefficient of tr W(z)^p (p=1..8) reduces to 0 modulo the leaf basis, so the characteristic polynomial of W(z) is z-independent at every complex point of V(I) (%.0fs)%s"
            % (c, c, len(LEAVES[c]), time.time() - t, "" if not allbad else " FAILURES %s" % allbad[:3]))
    # controls for the flatness test
    c = 0
    Wd = W_dict(FAM[c]['pat'])
    b0 = flat_bad(Wd, frozenset(), 0, [], 2)
    rec(len(b0) > 0, "D2 control: with no constraints (empty basis, chart c0=1) the same test reports k-dependence at p=%s" % ([p for p, _ in b0][:4],))
    # weaken one leaf: delete the quadratic-and-higher elements involving the leading chart and see the test fail
    bigj = max(range(len(LEAVES[0])), key=lambda j: len(LEAVES[0][j][2]))
    zs, one, G = LEAVES[0][bigj]
    G2 = sorted(G, key=lambda p: (sum(p.terms()[0][0]), len(p.terms())))[len(G) // 2:]
    b1 = flat_bad(Wd, zs, one, G2, 3)
    rec(len(b1) > 0, "D3 control: dropping the lower half (by degree) of the largest leaf basis (%d of %d elements) makes the test report k-dependence" % (len(G) // 2, len(G)))
    # singular primes
    for c in (0, 1):
        raw, h = blob('sing%d.log' % c)
        rec(hashlib.sha256(raw).hexdigest() == h, "E1.%d embedded source sing%d.log matches task sha256" % (c, c))
        primes = parse_b8_primes(raw.decode())
        homog = all(len(set(sum(m[:11]) - sum(m[11:]) for m, _ in g.terms())) == 1 for d, P in primes for g in P)
        rec(homog, "E1b.%d every printed Singular generator of class %d is homogeneous for the scaling weight (#c - #cb), so evaluating it on a chart c_a = 1 is legitimate" % (c, c))
        rec([d for d, _ in primes] == [4, 4, 2, 2, 2, 2, 4, 4] or sorted(d for d, _ in primes) == [2, 2, 2, 2, 4, 4, 4, 4],
            "E2.%d Singular printout for class %d lists %d components of dimensions %s" % (c, c, len(primes), [d for d, _ in primes]))
        cover = []
        for j, (zs, one, G) in enumerate(LEAVES[c]):
            cover.append([i for i, (d, P) in enumerate(primes) if leaf_in_prime(zs, one, G, P) is not None])
        unc = [j for j, f in enumerate(cover) if not f]
        used = sorted(set(i for f in cover for i in f))
        private = sorted(i for i in range(len(primes)) if any(f == [i] for f in cover))
        rec(not unc, "E3.%d class %d: each of the %d exact leaves lies inside at least one printed Singular component (all printed generators vanish on the leaf)" % (c, c, len(LEAVES[c])))
        rec(used == list(range(len(primes))), "E4.%d class %d: every printed component receives a leaf (components used: %s); components with a leaf lying in no other component: %s" % (c, c, [i + 1 for i in used], [i + 1 for i in private]))
        if c == 0:
            raw2, h2 = blob('nn_min.out')
            rec(hashlib.sha256(raw2).hexdigest() == h2, "E5 embedded source nn_min.out matches task sha256")
            flip = {3, 4, 8, 9}

            def flipp(p):
                d = {}
                for mon, co in p.terms():
                    s = 1
                    for k in flip:
                        s *= (-1) ** (mon[k] + mon[11 + k])
                    d[mon] = co * s
                return Rg.from_dict(d)

            comps = parse_nn_out(raw2.decode(), flipp)
            homog2 = all(len(set(sum(m[:11]) - sum(m[11:]) for m, _ in g.terms())) == 1 for d, P in comps for g in P)
            rec(homog2, "E5b every printed nn_min.out generator is homogeneous for the scaling weight (#c - #cb)")
            cover2 = []
            for j, (zs, one, G) in enumerate(LEAVES[0]):
                cover2.append([i for i, (d, P) in enumerate(comps) if leaf_in_prime(zs, one, G, P) is not None])
            unc2 = [j for j, f in enumerate(cover2) if not f]
            used2 = sorted(set(i for f in cover2 for i in f))
            rec(len(comps) == 8 and not unc2 and used2 == list(range(8)),
                "E6 the original nearest_site decomposition (nn_min.out, 8 components dims %s, sign-flipped to class-0 coordinates) is also covered leaf-by-leaf, all 8 components used" % ([d for d, _ in comps],))

    # real-locus closure (independent of the trace route)
    TYPES = {}
    for c in (0, 1):
        types = [set(orbit_type(e) for e in p) for p in FAM[c]['params']]
        TYPES[c] = [sorted(t)[0] for t in types]
        rec(all(len(t) == 1 for t in types) and TYPES[c] == ['ooo', 'oo0', 'ooi', 'o00', 'o0i', 'o0i', 'oii', '000', '00i', '0ii', 'iii'],
            "G0.%d class %d: each of the 11 parameter orbits has one hop type; types in order %s" % (c, c, TYPES[c]))
    OUT = lambda t: 'i' not in t
    INN = lambda t: 'o' not in t
    # algebraic flatness of pure supports: out/on-site types have n = vo - vi, in/on-site types have n = 0
    for c in (0, 1):
        okout = True
        okin = True
        for k, orb in enumerate(FAM[c]['params']):
            t = TYPES[c][k]
            for (n, vo, vi) in orb:
                if OUT(t) and tuple(n) != tuple(vo[a] - vi[a] for a in range(3)):
                    okout = False
                if INN(t) and tuple(n) != (0, 0, 0):
                    okin = False
        rec(okout and okin, "G1.%d class %d: every entry of an out-or-on-site orbit has n = vo - vi, so W(z) = Z W(1) Z^-1 with Z = diag(z^v); every entry of an in-or-on-site orbit has n = 0, so W is z-independent; both are flat for all coefficients" % (c, c))
    for c in (0, 1):
        t = time.time()
        res_all = []
        inf = 0
        for zs, one, G in LEAVES[c]:
            res = real_close(G, zs, one)
            if not res:
                inf += 1
            res_all += res
        INFEAS[c] = inf
        mixed = [sorted(s) for s in res_all if not (all(OUT(TYPES[c][k]) for k in s) or all(INN(TYPES[c][k]) for k in s))]
        nout = sum(1 for s in res_all if all(OUT(TYPES[c][k]) for k in s))
        nin = sum(1 for s in res_all if all(INN(TYPES[c][k]) for k in s) and not all(OUT(TYPES[c][k]) for k in s))
        rec(not mixed, "G2.%d class %d: real-locus closure (cb = conj c, chart scaling with r=|c_a|^2>0; Groebner bases over Q of the real and imaginary parts, positivity rules for monomials and even-power sums): %d of %d leaves have no real point; the others leave support inside {ooo,oo0,o00,000} (%d states) or {000,00i,0ii,iii} (%d states); mixed states: %s (%.0fs)"
            % (c, c, inf, len(LEAVES[c]), nout, nin, mixed, time.time() - t))

    # numerics
    names = TYPES[0]
    hasO = ['o' in n for n in names]
    hasI = ['i' in n for n in names]
    rng = np.random.default_rng(7)
    for c in (0, 1):
        t = time.time()
        sols = find_solutions(FAM[c]['E'], 70, 11 + c)
        # coverage by leaves
        unc = sum(0 if any(leaf_contains(z, np.conj(z), lf) for lf in LEAVES[c]) else 1 for z in sols)
        rec(len(sols) >= 20 and unc == 0, "F1.%d class %d: %d numerical unitary solutions (cb = conj c, residual < 1e-11) found; all lie on some exact leaf (uncovered: %d) [sampling evidence only]" % (c, c, len(sols), unc))
        var = 0.0
        pure = 0
        for z in sols:
            ev0 = None
            for _ in range(4):
                k = rng.uniform(-np.pi, np.pi, 3)
                W = W_numeric(FAM[c]['pat'], z, k)
                assert np.abs(W.conj().T @ W - np.eye(8)).max() < 1e-8
                cp_ = np.poly(np.linalg.eigvals(W))
                if ev0 is None:
                    ev0 = cp_
                var = max(var, np.abs(cp_ - ev0).max())
            sup = [i for i in range(11) if abs(z[i]) > 1e-6]
            o = any(hasO[i] for i in sup)
            ii_ = any(hasI[i] for i in sup)
            mixed = any(hasO[i] and hasI[i] for i in sup)
            pure += (not mixed) and not (o and ii_)
        rec(var < 1e-8, "F2.%d class %d: numerical solutions are unitary at random k and their characteristic polynomials are k-independent (max variation %.1e)" % (c, c, var))
        rec(pure == len(sols), "F3.%d class %d: numerically, %d/%d solutions are purely in-type or purely out-type (no mixed o/i hop type, no in+out coexistence) [numerical reading of the candidate's real-locus claim, not a proof]" % (c, c, pure, len(sols)))
        csols = find_complex_solutions(FAM[c]['E'], 60, 31 + c)
        # complex points (c and cb independent) must also lie on leaves; the generic ones are not unitary
        uncc = sum(0 if any(leaf_contains(a, b, lf) for lf in LEAVES[c]) else 1 for a, b in csols)
        nonreal = sum(1 for a, b in csols if np.abs(b - np.conj(a)).max() > 1e-6)
        rec(len(csols) >= 20 and uncc == 0, "F5.%d class %d: %d numerical points of the complex variety V(I) (c, cb independent; %d with cb != conj c) found; all lie on some exact leaf (uncovered: %d) [sampling evidence only]" % (c, c, len(csols), nonreal, uncc))
        # control: non-solution covariant coefficient vector is not flat
        zr = rng.normal(size=11) + 1j * rng.normal(size=11)
        ev = []
        for _ in range(3):
            k = rng.uniform(-np.pi, np.pi, 3)
            ev.append(np.poly(np.linalg.eigvals(W_numeric(FAM[c]['pat'], zr, k))))
        rec(max(np.abs(e - ev[0]).max() for e in ev) > 1e-3, "F4.%d control: a random covariant (non-unitary) coefficient vector has k-dependent characteristic polynomial" % c)
    return LEAVES, FAM


if __name__ == "__main__":
    LEAVES, FAM = main()
    npass = sum(RESULTS)
    nfail = len(RESULTS) - npass
    if nfail == 0:
        print("HIT: within the declared model and the two declared signed classes (checked in sympy; conditional on sympy groebner/factor soundness, no cofactor certificates): an exhaustive elimination cover of V(unitarity ideal) by %d + %d leaf varieties built without Singular output, every leaf inside a printed Singular component and all 8 printed components used (so the printed list covers V(I)); tr W(z)^p (p<=8) is z-independent on every leaf, hence for every complex point; an independent real-locus route gives only purely-inward or purely-outward supports (%d and %d leaves have no real point); so no nearest-site covariant walk disperses." % (len(LEAVES[0]), len(LEAVES[1]), INFEAS[0], INFEAS[1]))
    print("TOTAL: PASS=%d FAIL=%d" % (npass, nfail))
    print("SUMMARY: regenerates both nearest-site spinorial families and unitarity ideals from signed generators, covers each variety exhaustively with a sympy elimination tree, and shows every leaf lies in a printed Singular component, has k-independent tr W^p (p<=8) and (real locus) pure inward or outward support; runtime %.0fs." % (time.time() - T0))
    sys.exit(0 if nfail == 0 else 1)
