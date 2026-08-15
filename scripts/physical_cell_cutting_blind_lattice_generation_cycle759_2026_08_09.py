"""Rebuild and gate finite integer-lattice identities of a four-cube cutting system.

The runner constructs the finite cell complex, its minimum-cost cuttings, the
cutting-by-piece incidence matrix, and the eight-piece exact covers. It then
computes exact ranks, determinant-one saturation witnesses, a generating family
for the integer kernel, certified integer bases, and three Smith presentations of
one finite quotient. Fixed controls exercise the determinant, rank, index, and
Smith-form routines.
"""
import itertools
import math
import resource
import sys
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 300

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
I4 = np.eye(4, dtype=np.int64)
INV_OK = (
    np.array_equal(
        np.einsum("nij,njk->nik", MM, IV),
        np.broadcast_to(I4, MM.shape),
    )
    and np.array_equal(
        np.einsum("nij,njk->nik", IV, MM),
        np.broadcast_to(I4, MM.shape),
    )
)


def permutation_sign(perm):
    """Exact sign of a finite permutation."""
    inversions = sum(
        1
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
        if perm[i] > perm[j]
    )
    return -1 if inversions % 2 else 1

ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        if permutation_sign(perm) * math.prod(sg) == 1:
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
NORB = len(REPS)

OFF = np.array([0, 1, 7, 49, 343], dtype=np.int64)
L = np.einsum("nij,nmj->nmi", IV, V[None, :, :] - V[UNI[:, 0]][:, None, :])
CB = max(int(np.abs(L).max()), int(np.abs(L.sum(axis=2) - 1).max()))
WT = 2 * (CB * int(OFF.sum()) + 1 + OFF)
SB = int(WT.sum())
SC = np.array([SB // 2, SB // 2, SB // 2], dtype=np.int64)
lab, coll = {}, 0
for o, i in enumerate(REPS):
    q = (WT[:, None] * V[UNI[i]]).sum(axis=0)
    for (R, tf, _) in G:
        u = R @ (q[:3] - SC) + SC
        key = (int(u[0]), int(u[1]), int(u[2]), (SB - int(q[3])) if tf else int(q[3]))
        if lab.setdefault(key, o) != o:
            coll += 1
KEYS = sorted(lab)
Q = np.array(KEYS, dtype=np.int64)
NQ = len(Q)
QT = Q.T
face, MASK = 0, []
MI = np.zeros((NPIECE, NQ), dtype=np.int64)
for i in range(NPIECE):
    lam = IV[i] @ (QT - (SB * V[UNI[i, 0]])[:, None])
    tot = lam.sum(axis=0)
    face += int(((lam == 0).any(axis=0) | (tot == SB)).sum())
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
SOL, NODE, FULL = [], [0], set()


def rec(cov, chosen):
    NODE[0] += 1
    if cov == ALLQ:
        FULL.add(len(chosen))
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

INC = np.zeros((NS, NPO), dtype=np.uint8)
BITS = [0] * NS
for i, s in enumerate(SOL):
    v = 0
    for p in s:
        a = P2I[p]
        INC[i, a] = 1
        v |= 1 << a
    BITS[i] = v
INCL = INC.astype(np.int64)
PMS = []
M2I = dict((int(CM[i]), i) for i in range(NPIECE))
for (_, _, g) in G:
    arr = np.zeros(NPIECE, dtype=np.int32)
    for i in range(NPIECE):
        w = 0
        for c in range(16):
            if (int(CM[i]) >> c) & 1:
                w |= 1 << int(g[c])
        arr[i] = M2I[w]
    PMS.append(arr)
SOLARR = np.array(SOL, dtype=np.int32)
KEYMAP = dict((np.sort(SOLARR[i]).tobytes(), i) for i in range(NS))
PERMS = []
for arr in PMS:
    img = np.sort(arr[SOLARR], axis=1)
    PERMS.append(np.array([KEYMAP[img[i].tobytes()] for i in range(NS)], dtype=np.int64))


# ---- column permutations and column orbits ----
CP = []
CPOK = True
for gi in range(48):
    cp = np.array([P2I[int(PMS[gi][USED[a]])] for a in range(NPO)], dtype=np.int64)
    CPOK = CPOK and len(set(cp.tolist())) == NPO
    CPOK = CPOK and np.array_equal(INC[PERMS[gi]][:, cp], INC)
    CP.append(cp)
lab = -np.ones(NPO, dtype=np.int64)
NORB = 0
for a in range(NPO):
    if lab[a] < 0:
        for cp in CP:
            lab[int(cp[a])] = NORB
        NORB += 1
OSZ = sorted(int((lab == j).sum()) for j in range(NORB))


# ------------------------------------------------- Part 2: the object and its carriers

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
COV = INCL @ W.T


# ------------------------------------------ Part 2: the sharing tables of the covers

emit("Every count below is measured here.")
emit("the object: {0} cuttings and {1} pieces, {2} pieces to a cutting, "
     "{3} cuttings through a piece".format(NS, NPO, int(RW.min()), int(CS.min())))
gate(NS == 15800 and NPO == 192 and int(RW.min()) == int(RW.max()) == 24
     and int(CS.min()) == int(CS.max()) == 1975 and int(RW.sum()) == int(CS.sum())
     and len(SUB) == 4368 and NPIECE == 2672 and LO == 6 and NQ == 2736
     and coll == 0 and face == 0 and CB == 3 and SB == 12810
     and FULL == {24} and len(KEYMAP) == NS and INV_OK
     and len(ROT) == 24 and len(G) == 48 and len(PMS) == len(PERMS) == 48
     and len(CP) == 48 and CPOK and sum(OSZ) == NPO,
     "C0", "the cell sample is collision- and boundary-free; incidence degrees, "
     "exact inverses, and the declared action match")

emit("the {0} eight piece sets no cutting uses twice meet each of the {1} cuttings "
     "between {2} and {3} times".format(NC, NS, int(COV.min()), int(COV.max())))
gate(NC == 192 and int(COV.min()) == int(COV.max()) == 1, "C1",
     "each of the {0} sets is an exact cover: the table sends it to the all ones "
     "column over all {1} cuttings".format(NC, NS))

M = W
RSUM = M.sum(axis=1)
CSUM = M.sum(axis=0)
emit("the cover by piece table has row sums {0} to {1} and column sums {2} to "
     "{3}".format(int(RSUM.min()), int(RSUM.max()), int(CSUM.min()), int(CSUM.max())))
gate(M.shape == (NC, NPO) and set(int(x) for x in np.unique(M)) == set([0, 1])
     and int(RSUM.min()) == int(RSUM.max()) == 8
     and int(CSUM.min()) == int(CSUM.max()) == 8, "C2",
     "the zero one table is {0} regular on both sides".format(int(RSUM.min())))
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
# --------------------------------------- Part 3: rank, kernel and the whole spectrum

PMOD = 1000003


def rank_mod(rows, p):
    """rank of an integer matrix over the field with p elements

    Ordinary elimination with every value reduced by p through divmod, and the
    pivot turned around by raising it to the power p minus two.
    """
    wk = [[divmod(int(x), p)[1] for x in r] for r in rows]
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
        inv = pow(wk[rk][col], p - 2, p)
        pr = [divmod(x * inv, p)[1] for x in wk[rk]]
        wk[rk] = pr
        for r in range(rk + 1, nr):
            f = wk[r][col]
            if f:
                rw = wk[r]
                wk[r] = rw[:col] + [divmod(rw[c] - f * pr[c], p)[1]
                                    for c in range(col, m)]
        rk += 1
    return rk


# ----------------------------------------------- Part 4: exact integer machinery


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
    W = np.mod(A, p).astype(np.int64)
    n = W.shape[0]
    rowsel, colsel = [], []
    used = np.zeros(n, dtype=bool)
    for c in order:
        col = W[:, c].copy()
        col[used] = 0
        nz = np.nonzero(col)[0]
        if nz.size == 0:
            continue
        i = int(nz[0])
        used[i] = True
        rowsel.append(i)
        colsel.append(int(c))
        inv = pow(int(W[i, c]), p - 2, p)
        W[i] = np.mod(W[i] * inv, p)
        hit = np.nonzero(W[:, c])[0]
        hit = hit[hit != i]
        if hit.size:
            W[hit] = np.mod(W[hit] - np.outer(W[hit, c], W[i]), p)
    return rowsel, colsel


def divisor_witness(A, r):
    """greatest common divisor of two independently chosen r by r minors of A

    For an integer matrix of rank r the greatest common divisor of all r by r minors is
    the product of the invariant factors. A single minor equal to one or minus one
    therefore forces every invariant factor to be one: the rank is r over every field
    and the cokernel has no torsion at any prime. Two different choices are taken here,
    forward and reverse in the column order, and their greatest common divisor reported.
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


def rank_mod_np(A, p):
    """rank over the field with p elements, the row operations done with numpy"""
    W = np.mod(A, p).astype(np.int64)
    n, m = W.shape
    r = 0
    for c in range(m):
        nz = np.nonzero(W[r:, c])[0]
        if nz.size == 0:
            continue
        i = r + int(nz[0])
        if i != r:
            W[[r, i]] = W[[i, r]]
        inv = pow(int(W[r, c]), p - 2, p)
        W[r] = np.mod(W[r] * inv, p)
        col = W[r + 1:, c]
        hit = np.nonzero(col)[0]
        if hit.size:
            W[r + 1 + hit] = np.mod(W[r + 1 + hit] - np.outer(col[hit], W[r]), p)
        r += 1
        if r == n:
            break
    return r


def certified_basis(A, r, order):
    """Select rows certified as an integer-lattice basis by a unit minor."""
    rs, cs = sub_full(A, PMOD, order)
    if len(rs) != r or len(cs) != r:
        return np.empty((0, A.shape[1]), dtype=np.int64), 0
    basis = A[rs]
    certificate = abs(det_exact(basis[:, cs].tolist()))
    return basis, certificate


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


# -------------------------- Part 5: sharing, support-eight exchanges and the lattices

S = M @ M.T
OFFMASK = ~np.eye(NC, dtype=bool)
OFFD = S[OFFMASK]
SHARE = mset(OFFD)
DIAG = sorted(set(int(x) for x in np.diag(S)))
SVAL = sorted(SHARE)
SCNT = dict((v, ((S == v) & OFFMASK).sum(axis=1)) for v in SVAL)
SFIX = all(int(SCNT[v].min()) == int(SCNT[v].max()) for v in SVAL)
PER = [int(SCNT[v][0]) for v in SVAL]
emit("two covers share " + msets(SHARE) + " off the diagonal and " + joins(DIAG)
     + " on it, so per cover " + joins(PER) + " of the other covers")
gate(SHARE == {0: 30144, 1: 3840, 2: 1920, 4: 768} and DIAG == [8]
     and SVAL == [0, 1, 2, 4] and SFIX and PER == [157, 20, 10, 4]
     and sum(PER) == NC - 1, "C3",
     "the sharing counts are the same for every cover and take in all {0} of the "
     "others".format(NC - 1))

SMAX = int(OFFD.max())
SUPP = 16 - 2 * SMAX
PAIRS = [(i, j) for i in range(NC) for j in range(i + 1, NC) if int(S[i, j]) == SMAX]
D = np.array([M[i] - M[j] for i, j in PAIRS], dtype=np.int64)
NZC = sorted(set(int(x) for x in (D != 0).sum(axis=1)))
DVAL = sorted(set(int(x) for x in np.unique(D)))
emit("maximum sharing {0} gives support-{1} exchanges: {2} such "
     "pairs, moved counts {3}, entry values {4}".format(SMAX, SUPP, len(PAIRS),
                                                        joins(NZC), joins(DVAL)))
gate(SMAX == 4 and SUPP == 8 and len(PAIRS) == 384 and NZC == [SUPP]
     and DVAL == [-1, 0, 1], "C4",
     "exhaustive sharing values give difference support twice eight minus sharing")

BLIND = INCL @ D.T
emit("the cutting table sends all {0} support-eight exchanges to zero: the "
     "image is {1} by {2} with largest absolute value {3}".format(
         len(PAIRS), BLIND.shape[0], BLIND.shape[1], int(np.abs(BLIND).max())))
gate(BLIND.shape == (NS, len(PAIRS)) and int(np.abs(BLIND).max()) == 0, "C5",
     "a cutting meets each cover exactly once, so it meets a difference of two covers "
     "zero times")

RKI = rank_exact((INCL.T @ INCL).tolist())
RKM = rank_exact((M.T @ M).tolist())
RKD = rank_exact((D.T @ D).tolist())
emit("exact rank over the rationals: cutting table {0}, cover table {1}, support-eight "
     "exchanges {2}, and {0} plus {2} is {3}".format(RKI, RKM, RKD, RKI + RKD))
gate(RKI == 88 and RKM == 105 and RKD == 104 and RKI + RKD == NPO, "C6",
     "a matrix and its product with its transpose share a kernel, so the support-eight "
     "exchanges span the full rational kernel")

GI, DI = divisor_witness(INCL, RKI)
emit("two {0} by {0} minors of the cutting table, from opposite column orders, have "
     "absolute values {1} and greatest common divisor {2}".format(RKI, joins(DI), GI))
gate(GI == 1 and DI == [1, 1], "C7",
     "every invariant factor is one, so the cutting table has rank {0} in every "
     "characteristic and a quotient free of rank {1}".format(RKI, NPO - RKI))

GM, DM = divisor_witness(M, RKM)
emit("two {0} by {0} minors of the cover table have absolute values {1} and greatest "
     "common divisor {2}".format(RKM, joins(DM), GM))
gate(GM == 1 and DM == [1, 1], "C8",
     "every invariant factor is one, so the cover table has rank {0} in every "
     "characteristic and a quotient free of rank {1}".format(RKM, NPO - RKM))

GD, DD = divisor_witness(D, RKD)
emit("two {0} by {0} minors of the support-eight exchanges have absolute values {1} and "
     "greatest common divisor {2}, so their row lattice is saturated".format(
         RKD, joins(DD), GD))
gate(GD == 1 and DD == [1, 1], "C9",
     "the 384 support-eight exchanges generate the integer kernel and contain a "
     "{0}-row determinant-one basis".format(RKD))

ALL = np.array([M[0] - M[j] for j in range(1, NC)], dtype=np.int64)
RKA = rank_exact((ALL.T @ ALL).tolist())
GA, DA = divisor_witness(ALL, RKA)
emit("the {0} differences from a single cover have exact rank {1}, two minors of "
     "absolute value {2} and greatest common divisor {3}".format(
         len(ALL), RKA, joins(DA), GA))
gate(RKA == 104 and GA == 1 and DA == [1, 1], "C10",
     "the 191 fixed-cover differences generate the integer kernel and contain a "
     "104-row determinant-one basis")

DGV = [2, 6, 12]
CTLM = np.diag(np.array(DGV, dtype=np.int64))
K1 = det_exact([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
K2 = det_exact(CTLM.tolist())
K3 = det_exact([[2, 1], [1, 1]])
GC, DC = divisor_witness(CTLM, len(DGV))
emit("controls fixed in advance: determinants {0}, {1} and {2}, and the witness on a "
     "fixed diagonal gives {3} from minors {4}".format(K1, K2, K3, GC, joins(DC)))
gate(K1 == 0 and K2 == 144 and K3 == 1 and GC == 144 and GC != 1 and DC == [144, 144],
     "C11", "the witness reports a value other than one when the invariant factors are "
     "not all one, so a report of one is information")

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 101]
RI = sorted(set(rank_mod_np(INCL, p) for p in PRIMES))
RM = sorted(set(rank_mod_np(M, p) for p in PRIMES))
RSC = rank_mod(M.tolist(), PMOD)
CTL = [rank_mod_np(CTLM, q) for q in (2, 3, 5)]
CTLE = [sum(1 for x in DGV if divmod(x, q)[1]) for q in (2, 3, 5)]
emit("over {0} primes the cutting table holds rank {1} and the cover table {2}; a "
     "scalar second routine gives {3}; the fixed control drops to {4}".format(
         len(PRIMES), joins(RI), joins(RM), RSC, joins(CTL)))
gate(RI == [88] and RM == [105] and RSC == 105 and CTL == CTLE
     and min(CTL) < len(DGV) and max(CTL) == len(DGV), "C12",
     "C7 forces this at every prime: a determinant one minor stays invertible, and "
     "prime field rank never exceeds rational rank")

FACS, OKS, RKS, CERTS, BAS = [], [], [], [], []
for order in (range(NPO), range(NPO - 1, -1, -1)):
    AL, certL = certified_basis(INCL, RKI, order)
    BK, certK = certified_basis(D, RKD, order)
    IDX = abs(det_exact(np.vstack([AL, BK]).tolist()))
    GL = abs(det_exact((AL @ AL.T).tolist()))
    GK = abs(det_exact((BK @ BK.T).tolist()))
    RKS.append((len(AL), len(BK)))
    CERTS.append((certL, certK))
    OKS.append(IDX == GL and GL == GK and IDX > 1)
    FACS.append(pfac(IDX))
    BAS.append((AL, BK))
emit("the row lattice plus its integer kernel has quotient index {0}, agreeing three "
     "ways and from two certified basis pairs".format(fshow(FACS[0])))
gate(all(OKS) and len(OKS) == 2 and FACS[0] == FACS[1] and len(FACS[0]) > 0
     and RKS == [(RKI, RKD), (RKI, RKD)] and CERTS == [(1, 1), (1, 1)], "C13",
     "unit-minor certificates make both selected row sets integer bases, and the "
     "stacked determinant gives the quotient index")

FGL = invfac((BAS[0][0] @ BAS[0][0].T).tolist())
FGK = invfac((BAS[0][1] @ BAS[0][1].T).tolist())
FST = invfac(np.vstack([BAS[0][0], BAS[0][1]]).tolist())
PGL, PGK, PST = parts(FGL), parts(FGK), parts(FST)
NCY = sum(c for _, c in PST)
BIG = max(FST)
emit("one finite group of piece labels modulo the two lattices from the {0} by {0} "
     "row, the {1} by {1} kernel and the {2} by {2} stacked matrices".format(
         RKI, RKD, NPO))
emit("it has {0} cyclic parts, of order:count {1}".format(NCY, msets(dict(PST))))
gate(PGL == PGK and PGK == PST and NCY == 42 and len(FGL) == RKI
     and len(FGK) == RKD and len(FST) == NPO, "C14",
     "the two Gram presentations and the stacked presentation have the same "
     "nontrivial invariant factors")

PRD = 1
for d in FST:
    PRD *= d
CHN = all(divmod(FST[i + 1], FST[i])[1] == 0 for i in range(len(FST) - 1))
emit("the parts divide one another in turn and multiply to the index above, so the "
     "largest is the exponent: {0}, which is {1} times the {2} pieces"
     .format(BIG, BIG // NPO, NPO))
gate(CHN and pfac(PRD) == FACS[0] and BIG == 5 * NPO
     and BIG == max(d for d, _ in PST), "C15",
     "the largest invariant factor is the exponent of the finite quotient")

KA = invfac([[2]])
KB = invfac([[2, 0, 0], [0, 6, 0], [0, 0, 12]])
KC = invfac([[2, 0], [0, 3]])
KD = invfac([[4, 0], [0, 6]])
emit("controls fixed in advance: the chains {0} and {1} are their own diagonals, while "
     "{2} and {3} are not the diagonals 2 3 and 4 6 they came from"
     .format(joins(KA), joins(KB), joins(KC), joins(KD)))
gate(KA == [2] and KB == [2, 6, 12] and KC == [1, 6] and KD == [2, 12], "C16",
     "the routine returns the true chain and not the entries it was handed, so a chain "
     "of ones is information")

ACT = np.array([[1, 1]], dtype=np.int64)
BCT = np.array([[1, -1]], dtype=np.int64)
IC = abs(det_exact(np.vstack([ACT, BCT]).tolist()))
GLC = abs(det_exact((ACT @ ACT.T).tolist()))
GKC = abs(det_exact((BCT @ BCT.T).tolist()))
emit("control in the integer plane: stacked determinant {0}, and the two inner product "
     "determinants {1} and {2}".format(IC, GLC, GKC))
gate(IC == 2 and GLC == 2 and GKC == 2, "C17",
     "the hand-computed index-two example exercises all three index presentations")

ELAP = time.monotonic() - T0
RAW_RSS = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
RSS = RAW_RSS / (1024.0 * 1024.0) if sys.platform == "darwin" else RAW_RSS / 1024.0
EBD = 30 * (int(ELAP // 30) + 1)
RBD = 500 * (int(RSS // 500) + 1)
emit("elapsed under {0} s and peak memory under {1} MB, both measured in this "
     "run".format(EBD, RBD))
gate(ELAP < AUDIT_TIMEOUT_SEC and RSS < 2500.0
     and EBD <= AUDIT_TIMEOUT_SEC and RBD <= 2500, "C18",
     "inside its time and memory allowance")

emit("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
raise SystemExit(1 if PF[1] else 0)
