"""Measure the fraction of each piece that the cuttings of the unit four-cube see.

Every count below is measured here. The runner rebuilds the cell complex, the least
volume pieces, the cuttings at the adjacency cost floor, the cutting by piece table
and the eight piece exact covers. It then builds the maps got by permuting the four
coordinates of the four-cube and flipping any of them, measures the blocks those maps
cut the pieces into, and certifies an exact whole number multiple of the orthogonal
projector onto the span of the cuttings. The diagonal of that projector is the
fraction of each piece the cuttings see, and it is the same at every piece. The
smallest whole multiplier that clears the projector is measured on both tables and
set beside the largest invariant factor of the same table's Gram. Four controls fixed
in advance show the gates fail when the hypotheses they rest on are taken away.
"""
import itertools
import math
import resource
import time

import numpy as np

T0 = time.monotonic()
PF = [0, 0]
OUT = [0]


def emit(s):
    """print one line, refusing any barred digit pair or over-long line"""
    txt = "{0}".format(s)
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    if len(txt) > 149:
        raise ValueError("line over the length limit")
    OUT[0] += len(txt) + 1
    print(txt)


def gate(ok, name, detail):
    PF[0 if ok else 1] += 1
    emit(("PASS " if ok else "FAIL ") + name + "  " + detail)


def joins(xs):
    """one space separated string of a sequence of integers"""
    return " ".join(str(int(x)) for x in xs)


def mset(a):
    """value to count dictionary of an integer array"""
    v, c = np.unique(np.asarray(a), return_counts=True)
    return dict((int(x), int(y)) for x, y in zip(v, c))


def msets(d):
    """value:count string of a value to count dictionary"""
    return " ".join("{0}:{1}".format(k, d[k]) for k in sorted(d))


# ---------------------------------------------------------------- Part 1: machinery


def det4(A):
    def minors(r0, r1):
        out = {}
        for i in range(4):
            for j in range(i + 1, 4):
                out[(i, j)] = (A[:, r0, i] * A[:, r1, j] - A[:, r0, j] * A[:, r1, i])
        return out
    m, c = minors(0, 1), minors(2, 3)
    return (m[(0, 1)] * c[(2, 3)] - m[(0, 2)] * c[(1, 3)] + m[(0, 3)] * c[(1, 2)]
            + m[(1, 2)] * c[(0, 3)] - m[(1, 3)] * c[(0, 2)] + m[(2, 3)] * c[(0, 1)])


CORN = [(x, y, z, t) for x in (0, 1) for y in (0, 1) for z in (0, 1) for t in (0, 1)]
V = np.array(CORN, dtype=np.int64)
POS = dict((c, i) for i, c in enumerate(CORN))
PAIRS = list(itertools.combinations(range(5), 2))
SUB = np.array(list(itertools.combinations(range(16), 5)), dtype=np.int64)
VOL = np.abs(det4(V[SUB[:, 1:]] - V[SUB[:, 0]][:, None, :]))
UNI = SUB[VOL == 1]
NPIECE = len(UNI)


def cost(P, cols):
    tot = np.zeros(len(P), dtype=np.int64)
    for a, b in PAIRS:
        d = np.abs(V[P[:, a]][:, cols] - V[P[:, b]][:, cols]).sum(axis=1)
        tot = tot + (d > 1).astype(np.int64)
    return tot


C4 = cost(UNI, [0, 1, 2, 3])
LO = int(C4.min())
MINP = [i for i in range(NPIECE) if int(C4[i]) == LO]
MM = np.stack([(V[p[1:]] - V[p[0]]).T for p in UNI])
IV = np.rint(np.linalg.inv(MM.astype(float))).astype(np.int64)

ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        if int(round(np.linalg.det(R.astype(float)))) == 1:
            ROT.append(R)
CEN = np.array([1, 1, 1], dtype=np.int64)
G = []
for R in ROT:
    for tf in (0, 1):
        img = []
        for (x, y, z, t) in CORN:
            w = R @ (2 * np.array([x, y, z], dtype=np.int64) - CEN) + CEN
            key = (int(w[0]) // 2, int(w[1]) // 2, int(w[2]) // 2, (1 - t) if tf else t)
            if key not in POS:
                img = None
                break
            img.append(POS[key])
        if img is not None:
            G.append((R, tf, np.array(img, dtype=np.int64)))

posp = dict((tuple(int(c) for c in s), i) for i, s in enumerate(UNI))
LAB = -np.ones(NPIECE, dtype=np.int64)
REPS = []
for i in range(NPIECE):
    if LAB[i] >= 0:
        continue
    o = len(REPS)
    REPS.append(i)
    for (_, _, g) in G:
        LAB[posp[tuple(sorted(int(g[c]) for c in UNI[i]))]] = o
REPS = np.array(REPS, dtype=np.int64)

OFF = np.array([0, 1, 7, 49, 343], dtype=np.int64)
L = np.einsum("nij,nmj->nmi", IV, V[None, :, :] - V[UNI[:, 0]][:, None, :])
CB = max(int(np.abs(L).max()), int(np.abs(L.sum(axis=2) - 1).max()))
WT = 2 * (CB * int(OFF.sum()) + 1 + OFF)
SB = int(WT.sum())
SC = np.array([SB // 2, SB // 2, SB // 2], dtype=np.int64)
lab = {}
for o, i in enumerate(REPS):
    q = (WT[:, None] * V[UNI[i]]).sum(axis=0)
    for (R, tf, _) in G:
        u = R @ (q[:3] - SC) + SC
        key = (int(u[0]), int(u[1]), int(u[2]), (SB - int(q[3])) if tf else int(q[3]))
        lab.setdefault(key, o)
KEYS = sorted(lab)
Q = np.array(KEYS, dtype=np.int64)
NQ = len(Q)
QT = Q.T
MASK = []
MI = np.zeros((NPIECE, NQ), dtype=np.int64)
for i in range(NPIECE):
    lam = IV[i] @ (QT - (SB * V[UNI[i, 0]])[:, None])
    tot = lam.sum(axis=0)
    ins = (lam > 0).all(axis=0) & (tot < SB)
    MI[i] = ins.astype(np.int64)
    b = 0
    for j in np.flatnonzero(ins):
        b |= 1 << int(j)
    MASK.append(b)
ALLQ = (1 << NQ) - 1

BY, MK = {}, dict((i, MASK[i]) for i in MINP)
for i in MINP:
    for j in np.flatnonzero(MI[i]):
        BY.setdefault(int(j), []).append(i)
SOL = []


def rec(cov, chosen):
    if cov == ALLQ:
        SOL.append(tuple(sorted(chosen)))
        return
    rem = ALLQ & ~cov
    j = (rem & -rem).bit_length() - 1
    for i in BY[j]:
        if MK[i] & cov:
            continue
        chosen.append(i)
        rec(cov | MK[i], chosen)
        chosen.pop()


rec(0, [])
NS = len(SOL)
USED = sorted(set(i for s in SOL for i in s))
NPO = len(USED)
P2I = dict((p, a) for a, p in enumerate(USED))

CM = np.zeros(NPIECE, dtype=np.int64)
for i in range(NPIECE):
    b = 0
    for t in UNI[i]:
        b |= 1 << int(t)
    CM[i] = b
M2I = dict((int(CM[i]), i) for i in range(NPIECE))

INC = np.zeros((NS, NPO), dtype=np.uint8)
for i, s in enumerate(SOL):
    for p in s:
        INC[i, P2I[p]] = 1
INCL = INC.astype(np.int64)

INT = INCL.astype(np.int32)
GR = (INT.T @ INT).astype(np.int64)
RW = INC.sum(axis=1).astype(np.int64)
CS = INC.sum(axis=0).astype(np.int64)

NSH = (GR == 0)
np.fill_diagonal(NSH, False)
ADJ = [0] * NPO
for a in range(NPO):
    m = 0
    for b in np.flatnonzero(NSH[a]):
        m |= 1 << int(b)
    ADJ[a] = m
CLQ = []


def extend(cur, cand):
    if len(cur) == 8:
        CLQ.append(tuple(cur))
        return
    c = cand
    while c:
        low = c & -c
        v = low.bit_length() - 1
        c ^= low
        extend(cur + [v], c & ADJ[v])


extend([], (1 << NPO) - 1)
NC = len(CLQ)
W = np.zeros((NC, NPO), dtype=np.int64)
for i, s in enumerate(CLQ):
    for p in s:
        W[i, int(p)] = 1


# ----------------------------------------------- Part 2: exact integer machinery

PMOD = 1000003


def rank_exact(rows):
    """exact rank over the rationals of an integer matrix, integer arithmetic only

    One step fraction free elimination: each combined row is divided through by
    the greatest common divisor of its entries, so no denominator is ever needed
    and no floating point is used.
    """
    wk = [[int(x) for x in r] for r in rows]
    nr = len(wk)
    if nr == 0:
        return 0
    m = len(wk[0])
    rk = 0
    for col in range(m):
        piv = -1
        for r in range(rk, nr):
            if wk[r][col]:
                piv = r
                break
        if piv < 0:
            continue
        wk[rk], wk[piv] = wk[piv], wk[rk]
        pr = wk[rk]
        pv = pr[col]
        for r in range(rk + 1, nr):
            f = wk[r][col]
            if f:
                rw = wk[r]
                nw = [0] * col + [pv * rw[c] - f * pr[c] for c in range(col, m)]
                g = 0
                for x in nw:
                    if x:
                        g = math.gcd(g, x if x > 0 else -x)
                        if g == 1:
                            break
                if g > 1:
                    nw = [x // g for x in nw]
                wk[r] = nw
        rk += 1
    return rk


def det_exact(rows):
    """exact determinant of an integer matrix, fraction free, no division left over

    Every combined entry is divided by the previous pivot, which always goes in
    exactly, so the whole elimination stays inside the integers and the sign is
    carried by hand through the row swaps.
    """
    A = [[int(x) for x in r] for r in rows]
    n = len(A)
    sign, prev = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            sw = -1
            for i in range(k + 1, n):
                if A[i][k]:
                    sw = i
                    break
            if sw < 0:
                return 0
            A[k], A[sw] = A[sw], A[k]
            sign = -sign
        for i in range(k + 1, n):
            Ai, Ak = A[i], A[k]
            aik = Ai[k]
            for j in range(k + 1, n):
                Ai[j] = (Ak[k] * Ai[j] - aik * Ak[j]) // prev
            Ai[k] = 0
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


def sub_full(A, p, order):
    """row and column indices of a submatrix of full rank, chosen over the field with p

    Gauss-Jordan over the prime field, walking the columns in the given order. The
    columns that take a pivot and the rows that supply one index a square submatrix
    whose rank over that field is the rank of A, hence its determinant is nonzero
    there.
    """
    W2 = np.mod(A, p).astype(np.int64)
    n = W2.shape[0]
    rowsel, colsel = [], []
    used = np.zeros(n, dtype=bool)
    for c in order:
        col = W2[:, c].copy()
        col[used] = 0
        nz = np.nonzero(col)[0]
        if nz.size == 0:
            continue
        i = int(nz[0])
        used[i] = True
        rowsel.append(i)
        colsel.append(int(c))
        inv = pow(int(W2[i, c]), p - 2, p)
        W2[i] = np.mod(W2[i] * inv, p)
        hit = np.nonzero(W2[:, c])[0]
        hit = hit[hit != i]
        if hit.size:
            W2[hit] = np.mod(W2[hit] - np.outer(W2[hit, c], W2[i]), p)
    return rowsel, colsel


def divisor_witness(A, r):
    """greatest common divisor of two independently chosen r by r minors of A

    For an integer matrix of rank r the greatest common divisor of all r by r minors
    is the product of the invariant factors. A single minor equal to one or minus one
    therefore forces every invariant factor to be one, so the row lattice is saturated
    and the rank is r over every field. Two choices are taken here, forward and
    reverse in the column order, and their greatest common divisor reported.
    """
    m = A.shape[1]
    ds = []
    for order in (range(m), range(m - 1, -1, -1)):
        rs, cs = sub_full(A, PMOD, order)
        if len(rs) != r or len(cs) != r:
            ds.append(0)
            continue
        ds.append(abs(det_exact(A[np.ix_(rs, cs)].tolist())))
    g = 0
    for d in ds:
        g = math.gcd(g, d)
    return (g, ds)


def basis_rows(A, p, roworder):
    """indices of rows forming a basis of the row space over the field with p"""
    W2 = np.mod(A, p).astype(np.int64)
    n, m = W2.shape
    order = list(range(n)) if roworder is None else list(roworder)
    rowsel = []
    used = [False] * n
    for c in range(m):
        colv = W2[:, c].tolist()
        i = -1
        for r in order:
            if not used[r] and colv[r]:
                i = r
                break
        if i < 0:
            continue
        used[i] = True
        rowsel.append(i)
        inv = pow(int(W2[i, c]), p - 2, p)
        W2[i] = np.mod(W2[i] * inv, p)
        hit = np.nonzero(W2[:, c])[0]
        hit = hit[hit != i]
        if hit.size:
            W2[hit] = np.mod(W2[hit] - np.outer(W2[hit, c], W2[i]), p)
    return rowsel


def least_spot(wk, t, nr, nc):
    """position of the smallest nonzero entry in the block from t on, or None"""
    best = None
    spot = None
    for i in range(t, nr):
        ri = wk[i]
        for j in range(t, nc):
            v = ri[j]
            if v:
                if v < 0:
                    v = -v
                if best is None or v < best:
                    best = v
                    spot = (i, j)
    return spot


def invfac(rows):
    """the chain of invariant factors of an integer matrix, integer arithmetic only"""
    wk = [[int(x) for x in r] for r in rows]
    nr = len(wk)
    nc = len(wk[0])
    facs = []
    t = 0
    while t < min(nr, nc):
        spot = least_spot(wk, t, nr, nc)
        if spot is None:
            break
        while True:
            i0, j0 = spot
            wk[t], wk[i0] = wk[i0], wk[t]
            for r in range(nr):
                wk[r][t], wk[r][j0] = wk[r][j0], wk[r][t]
            pv = wk[t][t]
            for i in range(t + 1, nr):
                if wk[i][t]:
                    q = wk[i][t] // pv
                    ri = wk[i]
                    rt = wk[t]
                    for j in range(t, nc):
                        ri[j] -= q * rt[j]
            for j in range(t + 1, nc):
                if wk[t][j]:
                    q = wk[t][j] // pv
                    for i in range(t, nr):
                        wk[i][j] -= q * wk[i][t]
            if any(wk[i][t] for i in range(t + 1, nr)):
                spot = least_spot(wk, t, nr, nc)
                continue
            if any(wk[t][j] for j in range(t + 1, nc)):
                spot = least_spot(wk, t, nr, nc)
                continue
            bad = None
            for i in range(t + 1, nr):
                for j in range(t + 1, nc):
                    if divmod(wk[i][j], pv)[1]:
                        bad = i
                        break
                if bad is not None:
                    break
            if bad is None:
                break
            wk[t] = [wk[t][j] + wk[bad][j] for j in range(nc)]
            spot = least_spot(wk, t, nr, nc)
        v = wk[t][t]
        facs.append(v if v > 0 else -v)
        t += 1
    return facs


def parts(fs):
    """the nontrivial part of a chain of invariant factors, as value and count pairs"""
    out = {}
    for d in fs:
        if d != 1:
            out[d] = out.get(d, 0) + 1
    return sorted(out.items())


def pfac(n):
    """prime factorisation of a positive integer as a list of base and power pairs"""
    out = []
    m = int(n)
    d = 2
    while d * d <= m:
        e = 0
        while divmod(m, d)[1] == 0:
            e += 1
            m = m // d
        if e:
            out.append((d, e))
        d += 1 if d == 2 else 2
    if m > 1:
        out.append((m, 1))
    return out


def fshow(fs):
    """a factorisation as a product string like 2^7 x 3 x 5^2"""
    return " x ".join(str(b) if e == 1 else "{0}^{1}".format(b, e) for b, e in fs)


# ------------------------------- Part 3: the relabellings and the visibility matrix


def colperm(img):
    """a map of the 16 corners turned into a permutation of the pieces"""
    out = [0] * NPO
    for a, p in enumerate(USED):
        w = 0
        for c in range(16):
            if (int(CM[p]) >> c) & 1:
                w |= 1 << img[c]
        out[a] = P2I[M2I[w]]
    return tuple(out)


FULL, T96, T48, T24 = [], [], [], []
for perm in itertools.permutations(range(4)):
    for sg in itertools.product((0, 1), repeat=4):
        img = tuple(POS[tuple(c[perm[i]] ^ sg[i] for i in range(4))] for c in CORN)
        cp = colperm(img)
        FULL.append(cp)
        if perm[3] == 3:
            T96.append(cp)
            d3 = 1
            for i in range(3):
                for j in range(i + 1, 3):
                    if perm[i] > perm[j]:
                        d3 = -d3
            if d3 * (1 if divmod(sum(sg[:3]), 2)[1] == 0 else -1) == 1:
                T48.append(cp)
                if sg[3] == 0:
                    T24.append(cp)
PA = np.array(FULL, dtype=np.int32)


def blocks(ps):
    """the sizes of the blocks a set of piece relabellings cuts the pieces into"""
    seen = [-1] * NPO
    sz = []
    for s in range(NPO):
        if seen[s] >= 0:
            continue
        o = len(sz)
        blk = {s}
        front = [s]
        seen[s] = o
        while front:
            x = front.pop()
            for pm in ps:
                y = pm[x]
                if y not in blk:
                    blk.add(y)
                    seen[y] = o
                    front.append(y)
        sz.append(len(blk))
    return sorted(sz)


def bstr(sz):
    """block sizes as a count of equal blocks when they are equal"""
    return "{0} of {1}".format(len(sz), sz[0]) if len(set(sz)) == 1 else joins(sz)


def rowset(A):
    """the rows of an index table, each sorted, then put in one fixed order"""
    S = np.sort(A, axis=1)
    return S[np.lexsort(S.T[::-1])]


def keeps(cp, A, K):
    """whether relabelling the pieces by cp carries the row set of A onto itself"""
    return bool(np.array_equal(rowset(cp[A]), K))


PMEMO = {}


def liftN(A, D):
    """the exact integer matrix D times the projector onto the row space of A

    The projector is formed over the field with PMOD elements from a basis of the
    row space, multiplied by D, and each entry lifted into the range symmetric about
    zero. That step only proposes the lift. The whole number identities N N = D N
    and N B transpose = D B transpose, checked by the caller in Python object
    arithmetic, are what certify it.
    """
    key = id(A)
    if key not in PMEMO:
        rows = basis_rows(A, PMOD, None)
        B = np.mod(A[rows], PMOD).astype(np.int64)
        k = len(rows)
        aug = np.concatenate([np.mod(B @ B.T, PMOD), B], axis=1)
        for c in range(k):
            nz = [i for i in range(c, k) if aug[i, c]]
            aug[[c, nz[0]]] = aug[[nz[0], c]]
            aug[c] = np.mod(aug[c] * pow(int(aug[c, c]), PMOD - 2, PMOD), PMOD)
            hit = np.nonzero(aug[:, c])[0]
            hit = hit[hit != c]
            if hit.size:
                aug[hit] = np.mod(aug[hit] - np.outer(aug[hit, c], aug[c]), PMOD)
        PMEMO[key] = (np.mod(B.T @ aug[:, k:], PMOD), k, A[rows], A)
    Pm, k, B, _ = PMEMO[key]
    N = np.mod(Pm * D, PMOD)
    N = np.where(N > PMOD // 2, N - PMOD, N).astype(np.int64)
    return N, k, B


def clears(A, D):
    """whether D times the projector onto the row space of A is a whole matrix"""
    NO = liftN(A, D)[0].astype(object)
    return bool((NO @ NO == D * NO).all())


def least_mult(A, cands):
    """the smallest candidate multiplier that clears the projector, and the failures"""
    bad = []
    for D in sorted(cands):
        if clears(A, D):
            return D, bad
        bad.append(D)
    return None, bad


def constant_on(N, cls, ncl):
    """whether an integer matrix takes one value on each class of ordered pairs"""
    for c in range(ncl):
        v = N[cls == c]
        if int(v.min()) != int(v.max()):
            return False
    return True


# --------------------------------------------------- Part 4: the object and the gates

emit("Every count below is measured here.")
emit("the object: {0} cuttings and {1} pieces, {2} pieces to a cutting, "
     "{3} cuttings through a piece".format(NS, NPO, int(RW.min()), int(CS.min())))
gate(NS == 15800 and NPO == 192 and int(RW.min()) == int(RW.max()) == 24
     and int(CS.min()) == int(CS.max()) == 1975 and NC == 192, "C0",
     "the pieces per cutting and the cuttings through a piece are each the same "
     "number for every one of them, and there are {0} exact covers".format(NC))

DIST = len(set(FULL))
ISP = all(sorted(cp) == list(range(NPO)) for cp in FULL)
gate(len(FULL) == 384 and DIST == 384 and ISP, "C1",
     "permuting the four coordinates and flipping any of them gives {0} maps of the "
     "{1} corners and {2} distinct piece relabellings".format(len(FULL), 16, DIST))

CUTS = np.zeros((NS, int(RW.min())), dtype=np.int32)
for i, s in enumerate(SOL):
    CUTS[i] = sorted(P2I[p] for p in s)
COVS = np.zeros((NC, 8), dtype=np.int32)
for i, s in enumerate(CLQ):
    COVS[i] = sorted(int(p) for p in s)
CUTKEY, COVKEY = rowset(CUTS), rowset(COVS)
KEPT = sum(1 for i in range(len(FULL))
           if keeps(PA[i], CUTS, CUTKEY) and keeps(PA[i], COVS, COVKEY))
SWP = PA[0].copy()
SWP[0], SWP[1] = SWP[1], SWP[0]
CTL2 = keeps(SWP, CUTS, CUTKEY)
gate(KEPT == 384 and not CTL2, "C2",
     "{0} of the {1} carry the {2} cuttings and the {3} covers onto themselves; one "
     "of them after a swap of two pieces gives {4}".format(KEPT, len(FULL), NS, NC,
                                                           CTL2))

B24, B48, B96, BAL = blocks(T24), blocks(T48), blocks(T96), blocks(FULL)
emit("blocks on the {0} pieces: turns {1} give {2}, with the tick flip {3} give {4}, "
     "tick fixed {5} give {6}, all {7} give {8}".format(
         NPO, len(T24), bstr(B24), len(T48), bstr(B48), len(T96), bstr(B96),
         len(FULL), bstr(BAL)))
gate(len(T24) == 24 and len(T48) == 48 and len(T96) == 96 and B24 == [24] * 8
     and B48 == [48] * 4 and B96 == [96] * 2 and BAL == [NPO], "C3",
     "one block only once a relabelling may carry the tick coordinate onto a "
     "spatial one")

RKI = rank_exact((INCL.T @ INCL).tolist())
RKM = rank_exact((W.T @ W).tolist())
GI, DI = divisor_witness(INCL, RKI)
GM, DM = divisor_witness(W, RKM)
gate(RKI == 88 and RKM == 105 and GI == 1 and GM == 1 and DI == [1, 1]
     and DM == [1, 1], "C4",
     "exact ranks {0} and {1}; minors {2} and {3}, so each row lattice is "
     "saturated".format(RKI, RKM, joins(DI), joins(DM)))

CLS = -np.ones((NPO, NPO), dtype=np.int64)
NCLS = 0
PL = PA.astype(np.int64)
for a in range(NPO):
    for b in range(NPO):
        if CLS[a, b] >= 0:
            continue
        CLS[a, b] = NCLS
        fx = np.array([a], dtype=np.int64)
        fy = np.array([b], dtype=np.int64)
        while fx.size:
            ix = PL[:, fx].ravel()
            iy = PL[:, fy].ravel()
            m = CLS[ix, iy] < 0
            kk = np.unique(ix[m] * NPO + iy[m])
            fx = kk // NPO
            fy = kk - fx * NPO
            CLS[fx, fy] = NCLS
        NCLS += 1


def side(A, D, cands, want):
    """certify D times the projector and collect its diagonal, classes and glue"""
    N, k, B = liftN(A, D)
    NO = N.astype(object)
    BO = B.T.astype(object)
    sym = bool((N == N.T).all())
    idm = bool((NO @ NO == D * NO).all())
    fix = bool((NO @ BO == D * BO).all())
    tr = int(np.trace(N))
    dg = mset(np.diag(N))
    gv = math.gcd(k, NPO)
    dmin, bad = least_mult(A, cands)
    return dict(N=N, B=B, k=k, tr=tr, dg=dg, lo=int(N.min()), hi=int(N.max()),
                nv=len(set(N.ravel().tolist())), num=k // gv, den=NPO // gv,
                sym=sym, idm=idm, fix=fix, dmin=dmin, bad=bad,
                ok=(sym and idm and fix and tr == D * k and k == want),
                dgok=(len(dg) == 1 and int(np.diag(N).min()) * NPO == tr),
                cst=constant_on(N, CLS, NCLS))


def report(s, D, nm):
    """the two measurement lines for one side"""
    emit("{0} side rank {1}: N = {2} P symmetric {3}, N N = {2} N {4}, N fixes the "
         "rows {5}, trace {6} = {2} x {1}".format(nm, s["k"], D, s["sym"], s["idm"],
                                                  s["fix"], s["tr"]))
    emit("{0} side diagonal {1}, entries {2} to {3} taking {4} values, seen fraction "
         "{5} over {6} which is {7} over {8}".format(nm, msets(s["dg"]), s["lo"],
                                                     s["hi"], s["nv"], s["k"], NPO,
                                                     s["num"], s["den"]))


SA = side(INCL, 960, [192, 320, 480, 960], 88)
NN = SA["N"]
report(SA, 960, "cutting")
gate(SA["ok"], "C5",
     "the cutting side certificate holds over the whole numbers at rank {0}, trace "
     "{1}".format(SA["k"], SA["tr"]))
gate(SA["dgok"] and SA["num"] == 11 and SA["den"] == 24, "C6",
     "every one of the {0} diagonal entries is the same, so each piece is seen in "
     "the fraction {1} over {2}".format(NPO, SA["num"], SA["den"]))

COM = all(bool((NN[np.ix_(PA[i], PA[i])] == NN).all()) for i in range(len(FULL)))
gate(COM, "C7",
     "N is unchanged by relabelling the pieces by any of the {0}, so its diagonal is "
     "constant on each block".format(len(FULL)))

CB2 = np.zeros((2, NPO), dtype=np.int64)
SEEN = [-1] * NPO
BK = []
for s in range(NPO):
    if SEEN[s] >= 0:
        continue
    o = len(BK)
    blk = {s}
    front = [s]
    SEEN[s] = o
    while front:
        x = front.pop()
        for pm in T48:
            y = pm[x]
            if y not in blk:
                blk.add(y)
                SEEN[y] = o
                front.append(y)
    BK.append(sorted(blk))
for r in range(2):
    CB2[r, BK[r]] = 1
NB, KB, _ = liftN(CB2, 96)
QA = np.array(T48, dtype=np.int32)
K48 = all(bool((NB[np.ix_(QA[i], QA[i])] == NB).all()) for i in range(len(T48)))
K384 = all(bool((NB[np.ix_(PA[i], PA[i])] == NB).all()) for i in range(len(FULL)))
DB = mset(np.diag(NB))
gate(KB == 2 and K48 and not K384 and DB == {0: 96, 2: 96}
     and 96 * KB // NPO == 1, "C8",
     "control, two of the {0} blocks of the {1}: rank {2}, kept by the {1} {3}, by "
     "the {4} {5}, diagonal {6}".format(len(B48), len(T48), KB, K48, len(FULL),
                                        K384, msets(DB)))

E1 = np.zeros((1, NPO), dtype=np.int64)
E1[0, 0] = 1
NE, KE, _ = liftN(E1, 1)
DE = mset(np.diag(NE))
gate(KE == 1 and DE == {0: NPO - 1, 1: 1}, "C9",
     "control, the indicator of one piece with multiplier 1: rank {0}, diagonal {1}, "
     "not constant although the {2} give one block".format(KE, msets(DE), len(FULL)))

DMA, BDA = SA["dmin"], SA["bad"]
gate(DMA == 960 and BDA == [192, 320, 480], "C10",
     "smallest whole multiplier on the cutting side {0} = {1}; {2} each leave a "
     "fraction".format(DMA, fshow(pfac(DMA)), joins(BDA)))

gate(NCLS == 104 and SA["cst"] and SA["nv"] == 23, "C11",
     "the {0} carry the ordered pairs of pieces into {1} classes; N is constant on "
     "every one and takes {2} values".format(len(FULL), NCLS, SA["nv"]))

SB2 = side(W, 320, [64, 160, 320], 105)
NM = SB2["N"]
DMB, BDB = SB2["dmin"], SB2["bad"]
report(SB2, 320, "cover")
gate(SB2["ok"] and SB2["dgok"] and SB2["num"] == 35 and SB2["den"] == 64
     and DMB == 320 and BDB == [64, 160] and SB2["cst"] and SB2["nv"] == 23
     and NCLS == 104, "C12",
     "cover side certificate holds, fraction {0} over {1}, smallest multiplier {2} "
     "= {3}, {4} leave a fraction, constant on {5} classes".format(
         SB2["num"], SB2["den"], DMB, fshow(pfac(DMB)), joins(BDB), NCLS))

FI = invfac((SA["B"].astype(object) @ SA["B"].T.astype(object)).tolist())
FM = invfac((SB2["B"].astype(object) @ SB2["B"].T.astype(object)).tolist())
gate(max(FI) == DMA and max(FM) == DMB and len(FI) == RKI and len(FM) == RKM,
     "C13",
     "Gram largest invariant factor: cutting {0} with {1} nontrivial, cover {2} with "
     "{3}; each is that side's smallest whole multiplier".format(
         max(FI), sum(c for _, c in parts(FI)), max(FM),
         sum(c for _, c in parts(FM))))

LF, DL = [], []
for rows in ([[1, 2]], [[2, 0]]):
    Ax = np.array(rows, dtype=np.int64)
    LF.append(max(invfac((Ax.astype(object) @ Ax.T.astype(object)).tolist())))
    DL.append(least_mult(Ax, range(1, 40))[0])
gate(LF == [5, 4] and DL == [5, 1] and LF[0] == DL[0] and LF[1] != DL[1], "C14",
     "control, the line 1 2 is saturated and gives {0} against {1}; the line 2 0 is "
     "not and gives {2} against {3}".format(LF[0], DL[0], LF[1], DL[1]))

KC = invfac([[2, 0], [0, 3]])
KD = invfac([[4, 0], [0, 6]])
gate(KC == [1, 6] and KD == [2, 12], "C15",
     "control, the invariant factor routine returns {0} from the diagonal 2 3 and "
     "{1} from the diagonal 4 6, not the entries handed to it".format(joins(KC),
                                                                      joins(KD)))

A5 = DMA // NPO if DMA else 0
A3 = DMA // DMB if DMA and DMB else 0
IO = np.zeros((NPO, NPO), dtype=object)
for i in range(NPO):
    IO[i, i] = 1
JO = np.ones((NPO, NPO), dtype=object)
NO1 = NN.astype(object)
NO2 = NM.astype(object)
DIF = A3 * NO2 - (DMA * IO - NO1 + A5 * JO)
TIE = bool((DIF == 0).all())
NZ = int((DIF != 0).sum())
BIG = max([abs(int(x)) for x in DIF.ravel()]) if NZ else 0
DIF4 = A3 * NO2 - (DMA * IO - NO1 + (A5 - 1) * JO)
CTL7 = bool((DIF4 == 0).all())
ONES = np.ones(NPO, dtype=object)
SEES = bool((NO1 @ ONES == DMA * ONES).all())
DIMS = (NPO - RKI + 1) == RKM

ELAP = time.monotonic() - T0
RSS = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0
EBD = 300 * (int(ELAP // 300) + 1)
RBD = 500 * (int(RSS // 500) + 1)
gate(ELAP < 900.0 and RSS < 2500.0 and EBD <= 900 and RBD <= 2500, "C16",
     "elapsed under {0} s and peak memory under {1} MB, both measured in this "
     "run".format(EBD, RBD))

emit("the tie: {0} N2 = {1} I - N + {2} J over the whole numbers {3}, differing "
     "entries {4}, largest difference {5}; with {6} J it is {7}".format(
         A3, DMA, A5, TIE, NZ, BIG, A5 - 1, CTL7))
gate(TIE and SEES and DIMS and not CTL7, "C17",
     "N times the all ones vector is {0} times it {1}, and {2} - {3} + 1 = {4} "
     "{5}".format(DMA, SEES, NPO, RKI, RKM, DIMS))

TOT = "TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1])
CNT = "stdout characters: {0}"
n = OUT[0] + len(TOT) + 1
for _ in range(6):
    n = OUT[0] + len(CNT.format(n)) + 1 + len(TOT) + 1
emit(CNT.format(n))
emit(TOT)
if PF[1]:
    raise SystemExit(1)
