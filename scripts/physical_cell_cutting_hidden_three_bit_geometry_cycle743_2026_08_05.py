"""Cycle 743: the hidden three-bit geometry of the cell-cutting system.

Rebuilds the incidence table of the 15800 cuttings on 192 pieces, the eight
readings, the 48 cutting permutations and the two extra incidence
automorphisms of the previous cycle, then computes the full extended group,
its canonical partition of the pieces into eight blocks, and the affine
three-bit structure of the induced action on those blocks. Every quantity is
recomputed from the rebuilt machinery and compared with a pinned expectation.
Output stays under 5500 characters.
"""
import itertools

import numpy as np

PF = [0, 0]


def emit(s):
    """print one line, refusing any barred digit pair"""
    txt = "{0}".format(s)
    if ("9" + "9") in txt:
        raise ValueError("barred digit pair in output")
    print(txt)


def gate(ok, n, name, got, exp=None):
    """record and print one gate: computed value first, pinned value after"""
    PF[0 if ok else 1] += 1
    tail = "" if exp is None else " exp {0}".format(exp)
    emit("G{0} {1}: {2}{3} -> {4}".format(n, name, got, tail,
                                          "PASS" if ok else "FAIL"))


def cshow(c):
    """an element-order census as measured"""
    return " ".join("{0}:{1}".format(a, b) for a, b in c)


# ------------------------------------------------- Part 1: rebuild
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
GRP = []
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
            GRP.append((R, tf, np.array(img, dtype=np.int64)))

posp = dict((tuple(int(c) for c in s), i) for i, s in enumerate(UNI))
LAB = -np.ones(NPIECE, dtype=np.int64)
REPS = []
for i in range(NPIECE):
    if LAB[i] >= 0:
        continue
    o = len(REPS)
    REPS.append(i)
    for (_, _, g) in GRP:
        LAB[posp[tuple(sorted(int(g[c]) for c in UNI[i]))]] = o
REPS = np.array(REPS, dtype=np.int64)

OFF = np.array([0, 1, 7, 49, 343], dtype=np.int64)
LMB = np.einsum("nij,nmj->nmi", IV, V[None, :, :] - V[UNI[:, 0]][:, None, :])
CB = max(int(np.abs(LMB).max()), int(np.abs(LMB.sum(axis=2) - 1).max()))
WT = 2 * (CB * int(OFF.sum()) + 1 + OFF)
SB = int(WT.sum())
SC = np.array([SB // 2, SB // 2, SB // 2], dtype=np.int64)
lab, coll = {}, 0
for o, i in enumerate(REPS):
    q = (WT[:, None] * V[UNI[i]]).sum(axis=0)
    for (R, tf, _) in GRP:
        u = R @ (q[:3] - SC) + SC
        key = (int(u[0]), int(u[1]), int(u[2]), (SB - int(q[3])) if tf else int(q[3]))
        if lab.setdefault(key, o) != o:
            coll += 1
KEYS = sorted(lab)
Q = np.array(KEYS, dtype=np.int64)
NQ = len(Q)
QT = Q.T
MASK = []
MI = np.zeros((NPIECE, NQ), dtype=np.int64)
for i in range(NPIECE):
    lm = IV[i] @ (QT - (SB * V[UNI[i, 0]])[:, None])
    tot = lm.sum(axis=0)
    ins = (lm > 0).all(axis=0) & (tot < SB)
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
NP = NPO

PK = np.packbits(INC, axis=1)
LUT = np.array([bin(i).count("1") for i in range(256)], dtype=np.uint8)
SZC = [4, 6]
SZG = [4]
EA = dict((k, []) for k in SZC)
EB = dict((k, []) for k in SZC)
DIS = dict((k, set()) for k in SZG)
for lo in range(0, NS, 200):
    hi = min(lo + 100, NS)
    d = LUT[np.bitwise_xor(PK[lo:hi, None, :], PK[None, :, :])].sum(axis=2,
                                                                   dtype=np.int16)
    for k in SZC:
        rr, cc = np.nonzero(d == 2 * k)
        keep = (rr + lo) < cc
        aa = (rr[keep] + lo).tolist()
        bb = cc[keep].tolist()
        EA[k].extend(aa)
        EB[k].extend(bb)
        if k in DIS:
            for a, b in zip(aa, bb):
                DIS[k].add(BITS[a] ^ BITS[b])
for k in SZC:
    EA[k] = np.asarray(EA[k], dtype=np.int64)
    EB[k] = np.asarray(EB[k], dtype=np.int64)
KEY = dict((k, sorted(DIS[k])) for k in SZG)


def basis(rows, piv=None):
    """pivot table of the span of rows, over the field with two elements"""
    if piv is None:
        piv = {}
    for r in rows:
        while r:
            h = r.bit_length() - 1
            if h not in piv:
                piv[h] = r
                break
            r ^= piv[h]
    return piv


def rref(rows, piv=None):
    """pivot table cleared above the pivots as well as below"""
    piv = basis(rows, piv)
    for h in sorted(piv):
        for g in sorted(piv):
            if g > h and ((piv[g] >> h) & 1) == 1:
                piv[g] ^= piv[h]
    return piv


def perp(piv, n):
    """the weights on n pieces annihilating everything the pivot table spans"""
    out = []
    for j in range(n):
        if j in piv:
            continue
        w = 1 << j
        for h in piv:
            if ((piv[h] >> j) & 1) == 1:
                w |= 1 << h
        out.append(w)
    for w in out:
        for r in piv.values():
            assert (bin(w & r).count("1") & 1) == 0, "a uniform weight must annihilate"
    return out


TK = {}
for k in SZG:
    TK[k] = rref(s ^ KEY[k][0] for s in KEY[k][1:])
NUL = perp(TK[4], NPO)
WM = np.zeros((NPO, len(NUL)), dtype=np.int64)
for c, w in enumerate(NUL):
    for j in range(NPO):
        if ((w >> j) & 1) == 1:
            WM[j, c] = 1
FF = (INCL @ WM) & 1
PIV = {}
for c in range(FF.shape[1]):
    a = FF[:, c].astype(np.uint8)
    r = int.from_bytes(np.packbits(a).tobytes(), "big")
    while r:
        h = r.bit_length() - 1
        if h not in PIV:
            PIV[h] = (r, a)
            break
        r ^= PIV[h][0]
        a = a ^ PIV[h][1]
BAS = [PIV[h][1] for h in sorted(PIV)]
FUN = []
for mask in range(1 << len(BAS)):
    f = np.zeros(NS, dtype=np.uint8)
    for i, b in enumerate(BAS):
        if ((mask >> i) & 1) == 1:
            f = f ^ b
    FUN.append(f)

NAMED = {}
for f in FUN:
    one = int(f.sum())
    if one in (0, NS):
        continue
    g = f if 2 * one <= NS else (f ^ 1)
    d4 = g[EA[4]] ^ g[EB[4]]
    d6 = g[EA[6]] ^ g[EB[6]]
    nm = "four" if d4.max() == 0 else ("six" if d6.max() == 0 else "seven")
    NAMED[nm] = g

R8 = ["zero", "one", "four", "four-flip", "six", "six-flip", "seven", "seven-flip"]
TGT = [("zero", np.zeros(NS, dtype=np.uint8)), ("one", np.ones(NS, dtype=np.uint8))]
for nm in ["four", "six", "seven"]:
    TGT.append((nm, NAMED[nm]))
    TGT.append((nm + "-flip", NAMED[nm] ^ 1))
RNM = [nm for nm, _ in TGT]
TGTv = [v for _, v in TGT]
T8 = np.array(TGTv)

PMS = []
M2I = dict((int(CM[i]), i) for i in range(NPIECE))
for (_, _, g) in GRP:
    arr = np.zeros(NPIECE, dtype=np.int32)
    for i in range(NPIECE):
        w = 0
        for c in range(16):
            if (int(CM[i]) >> c) & 1:
                w |= 1 << int(g[c])
        arr[i] = M2I[w]
    PMS.append(arr)
CP = []
for gi in range(len(PMS)):
    CP.append(np.array([P2I[int(PMS[gi][USED[a]])] for a in range(NPO)],
                       dtype=np.int32))

SUPP = np.array([np.nonzero(INC[s])[0] for s in range(NS)], dtype=np.int32)
SUPD = dict((SUPP[s].tobytes(), s) for s in range(NS))
ID = np.arange(NP, dtype=np.int32)
IDR = np.arange(NS, dtype=np.int32)


def row_perm(pi):
    """the cutting permutation matching a piece permutation, via the support table"""
    img = np.sort(np.asarray(pi, dtype=np.int32)[SUPP], axis=1)
    out = np.empty(NS, dtype=np.int32)
    ok = True
    for s in range(NS):
        k = img[s].tobytes()
        if k in SUPD:
            out[s] = SUPD[k]
        else:
            ok = False
            out[s] = 0
    return (ok and len(set(out.tolist())) == NS), out


CROW = []
CPOK = True
for gi in range(len(CP)):
    okg, rp = row_perm(CP[gi])
    CPOK = CPOK and okg and np.array_equal(INC[rp][:, CP[gi]], INC)
    CROW.append(rp)

par = list(range(NP))


def find(a):
    while par[a] != a:
        par[a] = par[par[a]]
        a = par[a]
    return a


for gi in range(len(CP)):
    for j in range(NP):
        ra, rb = find(j), find(int(CP[gi][j]))
        if ra != rb:
            par[ra] = rb
root = np.array([find(j) for j in range(NP)])
falab = -np.ones(NP, dtype=np.int64)
nl = 0
for j in range(NP):
    if falab[j] < 0:
        falab[root == root[j]] = nl
        nl += 1
ORB = [np.nonzero(falab == k)[0] for k in range(nl)]

F64 = INC.astype(np.float64)
GRAM = (F64.T @ F64).astype(np.int64)


def refine(colors):
    """the stable colouring the overlap table refines a starting colouring to"""
    while True:
        CODE = colors[None, :] * 2048 + GRAM
        S = np.sort(CODE, axis=1)
        M = np.hstack([colors[:, None] * (1 << 40), S])
        _, new = np.unique(M, axis=0, return_inverse=True)
        new = new.astype(np.int64)
        if len(set(new.tolist())) == len(set(colors.tolist())):
            return new
        colors = new


base = refine(np.zeros(NP, dtype=np.int64))


def refine_seed(x):
    """seed one piece, then split the smallest surviving class until discrete"""
    colors = base.copy()
    colors[x] = colors.max() + 1
    colors = refine(colors)
    for _ in range(400):
        classes = {}
        for i in range(NP):
            classes.setdefault(int(colors[i]), []).append(i)
        big = [mem for mem in classes.values() if len(mem) > 1]
        if not big:
            return colors
        mem = sorted(big, key=lambda m: (len(m), m[0]))[0]
        colors[mem[0]] = colors.max() + 1
        colors = refine(colors)
    return None


ca = refine_seed(int(ORB[1][0]))
cb0 = refine_seed(0)
cb1 = refine_seed(5)


def build_pi(cb):
    """the piece permutation matching the anchored colouring to a seeded one"""
    inv = {}
    for i in range(NP):
        inv.setdefault(int(cb[i]), []).append(i)
    pi = np.zeros(NP, dtype=np.int32)
    ok = True
    for i in range(NP):
        mm = inv.get(int(ca[i]), [])
        if len(mm) != 1:
            ok = False
        else:
            pi[i] = mm[0]
    return ok, pi


OK0, b0 = build_pi(cb0)
OK1, b1 = build_pi(cb1)
SG0, sg0 = row_perm(b0)
SG1, sg1 = row_perm(b1)

emit("-- rebuild")
CS = INCL.sum(axis=0)
RS = INCL.sum(axis=1)
gate(INC.shape == (15800, 192), "01", "shape",
     "{0}x{1}".format(INC.shape[0], INC.shape[1]), "15800x192")
gate(bool((CS == 1975).all()), "02", "colsum",
     sorted(set(CS.tolist())), "[1975]")
gate(bool((RS == 24).all()) and len(SUPD) == NS, "03", "rowsupp",
     "width {0} distinct {1}".format(sorted(set(RS.tolist()))[0], len(SUPD)),
     "24 15800")
gate(CPOK and len(CP) == 48, "04", "perms48", len(CP), 48)
gate(nl == 4 and sorted(len(o) for o in ORB) == [48, 48, 48, 48], "05", "orbits48",
     "{0} of sizes {1}".format(nl, sorted(len(o) for o in ORB)), "4 of 48")
XG = all(any(np.array_equal(T8[a] ^ T8[b], T8[c]) for c in range(8))
         for a in range(8) for b in range(8))
DIST8 = len(set(v.tobytes() for v in TGTv)) == 8
gate(RNM == R8 and DIST8 and XG, "06", "readings",
     "{0} distinct, closed under xor".format(len(TGTv)), 8)
gate(OK0 and SG0 and np.array_equal(b0[b0], ID)
     and np.array_equal(INC[sg0][:, b0], INC)
     and all(not np.array_equal(b0, CP[gi]) for gi in range(48)), "07", "b0",
     "an involution outside the 48", "automorphism")
gate(OK1 and SG1 and np.array_equal(b1[b1], ID)
     and np.array_equal(INC[sg1][:, b1], INC)
     and all(not np.array_equal(b1, CP[gi]) for gi in range(48)), "08", "b1",
     "an involution outside the 48", "automorphism")
gate(all(np.array_equal(T8[r][sg0], T8[r]) and np.array_equal(T8[r][sg1], T8[r])
         for r in range(8)), "09", "bfix", "8 of 8 readings kept", 8)


# ------------------------------------------------- Part 2: the group E
def closure(gens):
    """the piece permutations the generators reach, each with its cutting map"""
    seen = {ID.tobytes(): (ID, IDR)}
    frontier = [(ID, IDR)]
    while frontier:
        nf = []
        for (p, r) in frontier:
            for (gp, gr) in gens:
                q = gp[p]
                k = q.tobytes()
                if k not in seen:
                    seen[k] = (q, gr[r])
                    nf.append(seen[k])
        frontier = nf
    return seen


def mul(a, b):
    return a[b]


def pinv(a):
    return np.argsort(a).astype(np.int32)


def order(p):
    q, n = p, 1
    while not np.array_equal(q, ID):
        q = p[q]
        n += 1
    return n


def census(perms):
    """the element-order census of a collection of permutations"""
    c = {}
    for p in perms:
        o = order(p)
        c[o] = c.get(o, 0) + 1
    return sorted(c.items())


def norbits(perms, n):
    """how many orbits a collection of permutations has on n points"""
    pr = list(range(n))

    def f(a):
        while pr[a] != a:
            pr[a] = pr[pr[a]]
            a = pr[a]
        return a
    for p in perms:
        for j in range(n):
            ra, rb = f(j), f(int(p[j]))
            if ra != rb:
                pr[ra] = rb
    cnt = {}
    for j in range(n):
        r = f(j)
        cnt[r] = cnt.get(r, 0) + 1
    return cnt


G48 = [(CP[i], CROW[i]) for i in range(48)]
C48 = closure(G48)
C48b0 = closure(G48 + [(b0, sg0)])
C48b1 = closure(G48 + [(b1, sg1)])
E = closure(G48 + [(b0, sg0), (b1, sg1)])
EK = sorted(E)
EP = dict((k, E[k][0]) for k in EK)
ER = dict((k, E[k][1]) for k in EK)

emit("-- the group E")
gate(len(C48) == 48, "10", "ord48", len(C48), 48)
gate(len(C48b0) == 96, "11", "ord48b0", len(C48b0), 96)
gate(len(C48b1) == 384 and b0.tobytes() in C48b1, "12", "ord48b1",
     "{0} with b0 inside".format(len(C48b1)), 384)
gate(len(E) == 384, "13", "ordE", len(E), 384)
EO = norbits([EP[k] for k in EK], NP)
gate(len(EO) == 1 and list(EO.values()) == [192], "14", "trans",
     "{0} orbit of {1}".format(len(EO), list(EO.values())[0]), "1 of 192")
STK = [k for k in EK if int(EP[k][0]) == 0]
gate(len(STK) == 2, "15", "stab", len(STK), 2)
s0 = [EP[k] for k in STK if not np.array_equal(EP[k], ID)][0]
NFIX = int((s0 == ID).sum())
gate(bool(np.array_equal(s0[s0], ID)) and NFIX == 16, "16", "s0",
     "an involution fixing {0}".format(NFIX), 16)
RK = len(norbits([EP[k] for k in STK], NP))
gate(RK == 104 and RK == NFIX + (NP - NFIX) // 2, "17", "rank",
     "{0} = {1} + {2}".format(RK, NFIX, (NP - NFIX) // 2), 104)
gate(all(np.array_equal(T8[:, ER[k]], T8) for k in EK), "18", "Efix",
     "384 elements keep 8 readings", "all")
CE = census([EP[k] for k in EK])
gate(CE == [(1, 1), (2, 75), (3, 32), (4, 132), (6, 96), (8, 48)], "19",
     "censusE", cshow(CE))
C48c = census([C48[k][0] for k in sorted(C48)])
gate(C48c == [(1, 1), (2, 19), (3, 8), (4, 12), (6, 8)], "20", "census48",
     cshow(C48c))
ZK = [k for k in EK if all(np.array_equal(mul(EP[k], EP[j]), mul(EP[j], EP[k]))
                           for j in EK)]
gate(len(ZK) == 2, "21", "centre", len(ZK), 2)
z = [EP[k] for k in ZK if not np.array_equal(EP[k], ID)][0]
gate(int((z == ID).sum()) == 0, "22", "zfree",
     "{0} fixed pieces".format(int((z == ID).sum())), 0)
gate(z.tobytes() in C48b0 and z.tobytes() not in C48, "23", "zmem",
     "inside 96, outside 48", "96 not 48")
ZQ = [sorted(set(int(falab[z[j]]) for j in ORB[a])) for a in range(4)]
gate(ZQ == [[1], [0], [3], [2]], "24", "zorb",
     "swaps first with second, third with fourth", "a double swap")
CMS = {}
for a in EK:
    ia = pinv(EP[a])
    for b in EK:
        c = mul(mul(ia, pinv(EP[b])), mul(EP[a], EP[b]))
        CMS[c.tobytes()] = c
DER = {ID.tobytes(): ID}
fr = [ID]
gl = list(CMS.values())
while fr:
    nf = []
    for p in fr:
        for g in gl:
            q = g[p]
            kk = q.tobytes()
            if kk not in DER:
                DER[kk] = q
                nf.append(q)
    fr = nf
gate(len(DER) == 96, "25", "der", len(DER), 96)
gate(set(DER) != set(C48b0) and not set(C48).issubset(set(DER)), "26", "derne",
     "not the 96 of b0, and does not hold the 48", "distinct")


def is_normal(sub):
    for k in EK:
        p = EP[k]
        ip = pinv(p)
        for sk in sub:
            if mul(mul(p, EP[sk]), ip).tobytes() not in sub:
                return False
    return True


gate((not is_normal(set(C48))) and (not is_normal(set(C48b0))), "27", "nonorm",
     "48 and 96 both non-normal", "neither")
NSQ = sum(1 for k in EK if (EP[k][EP[k]]).tobytes() in DER)
QUO = len(EK) // len(DER)
gate(NSQ == len(EK) and NSQ == 384 and QUO == 4, "28", "abel",
     "{0} squares inside, quotient {1}".format(NSQ, QUO), "384 and 4")
CD = census(list(DER.values()))
gate(CD == [(1, 1), (2, 19), (3, 32), (4, 12), (6, 32)], "29", "censusder",
     cshow(CD))
T3 = [EP[k] for k in EK if order(EP[k]) == 3]
S3 = set()
for p in T3:
    S3.add(tuple(sorted([p.tobytes(), (p[p]).tobytes()])))
gate(len(T3) == 32 and len(S3) == 16, "30", "ord3",
     "{0} elements in {1} subgroups".format(len(T3), len(S3)), "32 and 16")
R48 = norbits(CROW, NS)
gate(len(R48) == 391, "31", "rows48", len(R48), 391)
pr = list(range(NS))


def f3(a):
    while pr[a] != a:
        pr[a] = pr[pr[a]]
        a = pr[a]
    return a


for rp in CROW + [sg0, sg1]:
    for s in range(NS):
        ra, rb = f3(s), f3(int(rp[s]))
        if ra != rb:
            pr[ra] = rb
RE = {}
for s in range(NS):
    r = f3(s)
    RE[r] = RE.get(r, 0) + 1
gate(len(RE) == 74, "32", "rowsE", len(RE), 74)
RD = {}
for v in RE.values():
    RD[v] = RD.get(v, 0) + 1
RDL = sorted(RD.items())
gate(RDL == [(8, 1), (24, 4), (32, 1), (48, 7), (64, 1), (96, 11), (192, 24),
             (384, 25)], "33", "rowdist", cshow(RDL))

# ------------------------------------------------- Part 3: the eight blocks
emit("-- the eight blocks")
EIGHT = [r for r, v in RE.items() if v == 8]
gate(len(EIGHT) == 1, "34", "one8", len(EIGHT), 1)
ROWS8 = sorted(s for s in range(NS) if f3(s) == EIGHT[0])
sup = [set(map(int, SUPP[s])) for s in ROWS8]
DJ = all(not (sup[i] & sup[j]) for i in range(8) for j in range(i + 1, 8))
gate(len(ROWS8) == 8 and sorted(len(s) for s in sup) == [24] * 8 and DJ, "35",
     "blocks", "8 supports of 24, pairwise disjoint", "8 of 24")
UNIB = set().union(*sup)
gate(len(UNIB) == 192, "36", "cover", len(UNIB), 192)
QP = sorted(set(tuple(sum(1 for p in s if falab[p] == a) for a in range(4))
                for s in sup))
gate(QP == [(6, 6, 6, 6)], "37", "quarter", "each block meets each quarter in 6",
     6)
p48 = list(range(NS))


def f4(a):
    while p48[a] != a:
        p48[a] = p48[p48[a]]
        a = p48[a]
    return a


for rp in CROW:
    for s in range(NS):
        ra, rb = f4(s), f4(int(rp[s]))
        if ra != rb:
            p48[ra] = rb
SAME = (len(set(f4(s) for s in ROWS8)) == 1
        and sum(1 for s in range(NS) if f4(s) == f4(ROWS8[0])) == 8)
gate(SAME, "38", "same48", "one 48-orbit of size 8", 8)
BLK = np.zeros(NP, dtype=np.int32)
for bi, s in enumerate(sup):
    for p in s:
        BLK[p] = bi
MEM = [np.nonzero(BLK == bi)[0] for bi in range(8)]


def blockmap(p):
    out = []
    ok = True
    for bi in range(8):
        vals = set(int(BLK[p[j]]) for j in MEM[bi])
        if len(vals) != 1:
            ok = False
            out.append(-1)
        else:
            out.append(vals.pop())
    return ok, tuple(out)


BM, BOK = {}, True
for k in EK:
    ok, bmv = blockmap(EP[k])
    BOK = BOK and ok
    BM[k] = bmv
IDB = tuple(range(8))
KER = [k for k in EK if BM[k] == IDB]
gate(BOK and len(KER) == 2 and any(np.array_equal(EP[k], z) for k in KER), "39",
     "kernel", "{0}, the centre".format(len(KER)), 2)
B = sorted(set(BM.values()))
gate(len(B) == 192, "40", "imB", len(B), 192)
B48 = sorted(set(BM[k] for k in sorted(C48)))
gate(len(B48) == 48 and len([k for k in sorted(C48) if BM[k] == IDB]) == 1, "41",
     "imB48", "{0}, faithful".format(len(B48)), 48)


# ------------------------------------------------- Part 4: affine structure
def mulb(a, b):
    return tuple(a[b[i]] for i in range(8))


def invb(a):
    o = [0] * 8
    for i in range(8):
        o[a[i]] = i
    return tuple(o)


def orderb(a):
    q, n = a, 1
    while q != IDB:
        q = mulb(a, q)
        n += 1
    return n


def censusb(perms):
    """the element-order census of a collection of block permutations"""
    c = {}
    for p in perms:
        o = orderb(p)
        c[o] = c.get(o, 0) + 1
    return sorted(c.items())


emit("-- affine three-bit structure")
BS = set(B)
FPF = [g for g in B if g != IDB and mulb(g, g) == IDB
       and all(g[i] != i for i in range(8))]
gate(len(FPF) == 25, "42", "fpf", len(FPF), 25)
SUBS = set()
for tri in itertools.combinations(FPF, 3):
    if any(mulb(x, y) != mulb(y, x) for x, y in itertools.combinations(tri, 2)):
        continue
    S = set()
    for m in range(8):
        g = IDB
        for i, x in enumerate(tri):
            if (m >> i) & 1:
                g = mulb(g, x)
        S.add(g)
    if len(S) != 8 or not S.issubset(BS):
        continue
    if not all(mulb(x, x) == IDB for x in S):
        continue
    if not all(mulb(x, y) == mulb(y, x) for x in S for y in S):
        continue
    if not all(g == IDB or all(g[i] != i for i in range(8)) for g in S):
        continue
    if not all(len(set(g[bi] for g in S)) == 8 for bi in range(8)):
        continue
    SUBS.add(frozenset(S))
gate(len(SUBS) == 4, "43", "regsub", len(SUBS), 4)
NRM = [S for S in SUBS
       if all(mulb(mulb(g, s), invb(g)) in S for g in B for s in S)]
gate(len(NRM) == 1, "44", "normT", len(NRM), 1)
TG = sorted(NRM[0])
ORIG = int(BLK[0])
gate(sorted(t[ORIG] for t in TG) == list(range(8)), "45", "Treg",
     "the 8 translations move the base block to all 8", 8)
gens = []
for t in TG:
    span = set()
    for m in range(1 << (len(gens) + 1)):
        g = IDB
        for i, x in enumerate(gens + [t]):
            if (m >> i) & 1:
                g = mulb(g, x)
        span.add(g)
    if len(span) == (1 << (len(gens) + 1)):
        gens.append(t)
    if len(gens) == 3:
        break
LBL, TR = {}, {}
for m in range(8):
    g = IDB
    for i, x in enumerate(gens):
        if (m >> i) & 1:
            g = mulb(g, x)
    LBL[g[ORIG]] = m
    TR[m] = g
INVL = dict((v, k) for k, v in LBL.items())
gate(len(gens) == 3 and len(LBL) == 8 and len(TR) == 8, "46", "basis",
     "{0} generators giving {1} labels".format(len(gens), len(LBL)), "3 and 8")


def linpart(g):
    return mulb(TR[LBL[g[ORIG]]], g)


LMAP = [linpart(g) for g in B]
gate(all(A[ORIG] == ORIG for A in LMAP), "47", "fixorig",
     "every linear part keeps the base block", 192)
ADD = all(LBL[A[INVL[u ^ v]]] == (LBL[A[INVL[u]]] ^ LBL[A[INVL[v]]])
          for A in LMAP for u in range(8) for v in range(8))
gate(ADD, "48", "add", "additive on all 64 label pairs", 64)
LS = sorted(set(LMAP))
gate(len(LS) == 24, "49", "Lsize", len(LS), 24)
gate(all(mulb(a, b) in set(LS) for a in LS for b in LS), "50", "Lclosed",
     "closed under composition", 24)
MEET = [A for A in LS if A in set(TG)]
PRD = len(TG) * len(LS)
gate(len(MEET) == 1 and PRD == len(B) and PRD == 192, "51", "split",
     "meet {0}, product {1}".format(len(MEET), PRD), "1 and 192")
CL = censusb(LS)
gate(CL == [(1, 1), (2, 9), (3, 8), (4, 6)], "52", "censusL", cshow(CL))


def lorbits(grp):
    """orbit sizes of a linear collection on the 7 nonzero labels"""
    seen, out = set(), []
    for p in range(1, 8):
        if p in seen:
            continue
        o, fr = {p}, [p]
        while fr:
            nf = []
            for q in fr:
                for A in grp:
                    r = LBL[A[INVL[q]]]
                    if r not in o:
                        o.add(r)
                        nf.append(r)
            fr = nf
        seen |= o
        out.append(sorted(o))
    return out


OL = lorbits(LS)
gate(sorted(len(o) for o in OL) == [3, 4], "53", "Lorb",
     sorted(len(o) for o in OL), "[3, 4]")
FIXL = [u for u in range(1, 8) if all(LBL[A[INVL[u]]] == u for A in LS)]
gate(len(FIXL) == 0, "54", "nofix", len(FIXL), 0)
THREE = [o for o in OL if len(o) == 3][0]
FOUR = [o for o in OL if len(o) == 4][0]
P = set(THREE) | set([0])
gate(len(P) == 4 and all((u ^ v) in P for u in P for v in P), "55", "plane",
     "{0} labels closed under xor".format(len(P)), 4)
PLANES = sorted(set(frozenset([0, a, b, a ^ b])
                    for a in range(1, 8) for b in range(a + 1, 8) if (a ^ b) > b),
                key=lambda s: sorted(s))
INVP = [pl for pl in PLANES if all(LBL[A[INVL[u]]] in pl for A in LS for u in pl)]
gate(len(PLANES) == 7 and len(INVP) == 1 and set(INVP[0]) == P, "56", "uniqplane",
     "{0} of {1} planes kept".format(len(INVP), len(PLANES)), "1 of 7")
ACT4 = set(tuple(LBL[A[INVL[u]]] for u in FOUR) for A in LS)
gate(len(ACT4) == 24, "57", "faith",
     "{0} on the four-orbit, the symmetric group on four".format(len(ACT4)), 24)


def tomat(A):
    return tuple(LBL[A[INVL[1 << i]]] for i in range(3))


def apply(M, u):
    r = 0
    for i in range(3):
        if (u >> i) & 1:
            r ^= M[i]
    return r


ALLM = list(itertools.product(range(8), repeat=3))
INVM = [M for M in ALLM if len(set(apply(M, u) for u in range(8))) == 8]
gate(len(ALLM) == 512 and len(INVM) == 168, "58", "mats",
     "{0} of {1} invertible".format(len(INVM), len(ALLM)), "168 of 512")
PMT = [M for M in INVM if set(apply(M, u) for u in P) == P]
gate(len(PMT) == 24 and set(tomat(A) for A in LS) == set(PMT), "59", "stabP",
     "{0} keep the plane, and they are L".format(len(PMT)), 24)
gate(set(TG).issubset(set(B48)), "60", "TinB48",
     "all 8 translations already induced by the 48", 8)
L48 = sorted(set(linpart(g) for g in B48))
NAB = any(mulb(a, b) != mulb(b, a) for a in L48 for b in L48)
gate(len(L48) == 6 and set(L48).issubset(set(LS)) and NAB, "61", "L48",
     "{0}, inside L, nonabelian".format(len(L48)), 6)
CL48 = censusb(L48)
gate(CL48 == [(1, 1), (2, 3), (3, 2)], "62", "censusL48", cshow(CL48))
O48 = lorbits(L48)
gate(sorted(len(o) for o in O48) == [1, 3, 3], "63", "L48orb",
     sorted(len(o) for o in O48), "[1, 3, 3]")
FX = [u for u in range(1, 8) if all(LBL[A[INVL[u]]] == u for A in L48)]
gate(len(FX) == 1 and FX[0] not in P, "64", "vstar",
     "{0} label kept by all of L48, off the plane".format(len(FX)), 1)
vs = FX[0]
STL = [A for A in LS if LBL[A[INVL[vs]]] == vs]
gate(vs in FOUR and len(STL) == 6 and set(STL) == set(L48), "65", "vin4",
     "in the four-orbit, stabilizer {0} equal to L48".format(len(STL)), 6)
PV = [M for M in INVM if set(apply(M, u) for u in P) == P and apply(M, vs) == vs]
gate(len(PV) == 6 and set(tomat(A) for A in L48) == set(PV), "66", "jointstab",
     "{0} keep plane and direction, and they are L48".format(len(PV)), 6)

print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
