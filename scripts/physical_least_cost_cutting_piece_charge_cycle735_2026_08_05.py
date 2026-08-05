"""Cycle 735. A label on the pieces that splits the least cost cuttings of the cell.

A piece is a five corner simplex of the four cube of least volume; the cost of a piece
counts the pairs of its corners more than one lattice step apart. Cycle 734 found that the
smallest cost keeping change of a cutting at the floor replaces four pieces, and that such
a change is a flip between the two floor cuts of one region. This runner asks whether
those flips act as independent switches, and finds that they do not: the free switch
picture reaches two switches and stops, and the obstruction is exhibited as two available
flips sharing a piece.

It then looks for a label carried by the pieces themselves, summed over the twenty four
pieces of a cutting and read modulo two, that reverses under every smallest move and holds
under every move on six pieces. Two such labels exist, they differ on every cutting, and
so the two sided split of the cuttings that they name is a single split rather than a
choice. Dropping the demand that the label be read off the pieces leaves two to the power
one hundred and fifty seven labellings instead.

No solver. Every count is a complete search over an explicit finite set, and every rank is
an elimination over the field with two elements carried out in whole numbers.
"""
import itertools

import numpy as np

PF = [0, 0]


def gate(ok, name, detail):
    PF[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + name + "  " + detail)


def sec(text):
    print("")
    print(text)


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

sec("the cuttings of the cell at the floor of the cost")
gate(len(SUB) == 4368 and NPIECE == 2672 and NQ == 2736 and coll == 0 and face == 0
     and CB == 3 and SB == 12810 and len(G) == 48 and NORB == 57, "base.cell",
     "{0} five-subsets of the 16 corners give {1} pieces of least volume, carrying {2} "
     "sample points with no collision and {3} on a boundary; the cell has {4} symmetries "
     "and the pieces {5} orbits".format(len(SUB), NPIECE, NQ, face, len(G), NORB))

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
gate(LO == 6 and len(MINP) == 400 and NODE[0] == 502838 and NS == 15800
     and FULL == set([24]) and NPO == 192, "base.floor",
     "a complete search over the {0} pieces of least cost {1} visits {2} nodes and finds "
     "{3} cuttings of {4} pieces each, between them using {5} pieces".format(
         len(MINP), LO, NODE[0], NS, 24, NPO))

CM = np.zeros(NPIECE, dtype=np.int64)
for i in range(NPIECE):
    b = 0
    for t in UNI[i]:
        b |= 1 << int(t)
    CM[i] = b
ALLI = np.arange(NPIECE, dtype=np.int64)


def span(pcs):
    hc, hp = 0, 0
    for i in pcs:
        hc |= int(CM[i])
        hp |= MASK[i]
    return hc, hp


def refills(hc, hp, k):
    cand = [int(j) for j in ALLI[(CM & ~hc) == 0]]
    cand = [j for j in cand if (MASK[j] & ~hp) == 0]
    out = []

    def rec2(cov, chosen, start):
        if len(chosen) == k:
            if cov == hp:
                out.append(tuple(chosen))
            return
        for a in range(start, len(cand)):
            j = cand[a]
            if MASK[j] & cov:
                continue
            chosen.append(j)
            rec2(cov | MASK[j], chosen, a + 1)
            chosen.pop()

    rec2(0, [], 0)
    return out


A = np.zeros((NS, NPO), dtype=np.float32)
for r, s in enumerate(SOL):
    A[r, [P2I[i] for i in s]] = 1.0
BAG = dict((k, []) for k in range(4, 11))
for lo in range(0, NS, 1000):
    B = A[lo:lo + 1000] @ A.T
    for r in range(B.shape[0]):
        B[r, lo + r] = -1.0
    d = (24 - B).astype(np.int16)
    for k in range(4, 11):
        rr, cc = np.nonzero(d == k)
        m = (rr + lo) < cc
        BAG[k].append(np.stack([rr[m] + lo, cc[m]]).astype(np.int32))
BYD = dict((k, np.concatenate(BAG[k], axis=1)) for k in range(4, 11))
E4 = BYD[4]
NE4 = int(E4.shape[1])

REG = {}
EREG = np.zeros(NE4, dtype=np.int32)
for j in range(NE4):
    a, b = int(E4[0, j]), int(E4[1, j])
    key = span(sorted(set(SOL[a]) - set(SOL[b])))
    if key not in REG:
        REG[key] = len(REG)
    EREG[j] = REG[key]
RL = sorted(REG, key=lambda k: REG[k])
CUTP = []
for (hc, hp) in RL:
    fl = [u for u in refills(hc, hp, 4) if sum(int(C4[j]) for j in u) == 4 * LO]
    CUTP.append(fl)
SHR = max(len(set(u[0]) & set(u[1])) for u in CUTP)
gate(len(REG) == 120 and NE4 == 46128 and set(len(u) for u in CUTP) == set([2])
     and SHR == 0, "base.region",
     "the smallest move replaces four pieces and occurs in {0} ways; those recut {1} "
     "regions, each holding exactly two cuts at the floor, and the two cuts of a region "
     "share no piece".format(NE4, len(REG)))

sec("how many of those switches a cutting offers at once")

HAS = np.zeros((NPO, NS), dtype=bool)
for i, s in enumerate(SOL):
    for p in s:
        HAS[P2I[p], i] = True
INS, BOTH = [], 0
for fl in CUTP:
    pair = []
    for u in fl:
        m = np.ones(NS, dtype=bool)
        for p in u:
            m &= HAS[P2I[p]]
        pair.append(m)
    BOTH += int((pair[0] & pair[1]).sum())
    INS.append(pair)
DEGSW = np.zeros(NS, dtype=np.int64)
for pair in INS:
    DEGSW += pair[0].astype(np.int64) + pair[1].astype(np.int64)
DEG4 = np.bincount(E4.reshape(-1), minlength=NS)
DSP = sorted((int(a), int(b)) for a, b in zip(*np.unique(DEGSW, return_counts=True)))
DSX = [(0, 144), (1, 192), (2, 624), (3, 1600), (4, 2304), (5, 1920), (6, 4448),
       (7, 1344), (8, 672), (9, 1728), (10, 192), (12, 432), (15, 192), (24, 8)]
gate(DSP == DSX and int(DEGSW.sum()) == 2 * NE4 and sum(b for _, b in DSP) == NS,
     "sw.count",
     "the number of regions a cutting fills runs {0}, over all cuttings {1} times, twice "
     "the {2} smallest moves".format(DSP, int(DEGSW.sum()), NE4))
gate(bool((DEGSW == DEG4).all()) and BOTH == 0, "sw.match",
     "cutting by cutting that number is exactly the number of smallest moves out of it, "
     "and no cutting holds both cuts of any region")

sec("the switches are not independent")

par = list(range(NS))


def find(x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x


for j in range(NE4):
    a, b = find(int(E4[0, j])), find(int(E4[1, j]))
    if a != b:
        par[a] = b
CID, CREP = {}, []
for i in range(NS):
    r = find(i)
    if r not in CID:
        CID[r] = len(CREP)
        CREP.append(i)
COMP = np.array([CID[find(i)] for i in range(NS)], dtype=np.int64)
NCOMP = len(CREP)
CSZ = np.bincount(COMP)
SSP = sorted((int(a), int(b)) for a, b in zip(*np.unique(CSZ, return_counts=True)))
gate(NCOMP == 349 and SSP == [(1, 144), (2, 96), (4, 36), (7, 48), (236, 24),
                              (9320, 1)], "grp.count",
     "under the smallest move the {0} cuttings fall into {1} groups of sizes {2}".format(
         NS, NCOMP, SSP))

CE = dict((c, []) for c in range(NCOMP))
for j in range(NE4):
    CE[int(COMP[int(E4[0, j])])].append(j)
CUBE, COV, DIMS = 0, 0, set()
for c in range(NCOMP):
    n = int(CSZ[c])
    if n & (n - 1):
        continue
    d = n.bit_length() - 1
    ed = CE[c]
    if len(ed) != d * (n // 2):
        continue
    dg = {}
    for j in ed:
        for v in (int(E4[0, j]), int(E4[1, j])):
            dg[v] = dg.get(v, 0) + 1
    if n > 1 and (len(dg) != n or set(dg.values()) != set([d])):
        continue
    lb = {}
    for j in ed:
        lb[int(EREG[j])] = lb.get(int(EREG[j]), 0) + 1
    if n > 1 and (len(lb) != d or set(lb.values()) != set([n // 2])):
        continue
    CUBE += 1
    COV += n
    DIMS.add(d)
POW = sum(1 for c in range(NCOMP) if (int(CSZ[c]) & (int(CSZ[c]) - 1)) == 0)
gate(CUBE == 276 and COV == 480 and DIMS == set([0, 1, 2]) and POW == CUBE, "grp.cube",
     "{0} of those groups are cubes on their switches, covering {1} cuttings; every one "
     "has dimension {2}, and no other group has a number of cuttings that is a power of "
     "two at all".format(CUBE, COV, sorted(DIMS)))

SEV = [c for c in range(NCOMP) if int(CSZ[c]) == 7]
SHP = set()
for sv in SEV:
    sdg = {}
    for j in CE[sv]:
        for v in (int(E4[0, j]), int(E4[1, j])):
            sdg[v] = sdg.get(v, 0) + 1
    SHP.add((len(CE[sv]), len(set(int(EREG[j]) for j in CE[sv])),
             tuple(sorted(sdg.values()))))
sed = CE[SEV[0]]
SREG, SDG = 4, [2] * 6 + [4]
gate(len(SEV) == 48 and len(SHP) == 1
     and SHP == set([(8, SREG, tuple(SDG))]), "grp.seven",
     "the smallest group whose switches interact holds 7 cuttings over {0} regions with "
     "{1} moves, one cutting meeting {2} of them and the rest {3}, against the 16 that "
     "four free switches would give".format(SREG, len(sed), 4, 2))

AV = dict((i, []) for i in range(NS))
for k, pair in enumerate(INS):
    for h in (0, 1):
        for i in np.flatnonzero(pair[h]):
            AV[int(i)].append(frozenset(CUTP[k][h]))
SH, NSH, SSPEC = 0, 0, {}
for i in range(NS):
    v = AV[i]
    h = 0
    for a in range(len(v)):
        for b in range(a + 1, len(v)):
            if v[a] & v[b]:
                h += 1
            else:
                NSH += 1
    SH += h
    SSPEC[h] = SSPEC.get(h, 0) + 1
gate(SH + NSH == sum(int(d) * (int(d) - 1) // 2 for d in DEGSW)
     and SH == 54912 and SH + NSH == 273936 and SSPEC.get(0, 0) == 8880, "grp.share",
     "of the {0} pairs of switches a cutting offers at once {1} share a piece and so "
     "cannot both be thrown; the cuttings with no sharing pair number {2}".format(
         SH + NSH, SH, SSPEC.get(0, 0)))

GI = int(np.argmax(CSZ))
GV = np.flatnonzero(COMP == GI)
GE = [j for j in CE[GI]]
adj = dict((int(v), []) for v in GV)
for j in GE:
    a, b = int(E4[0, j]), int(E4[1, j])
    adj[a].append(b)
    adj[b].append(a)
src = int(GV[0])
dist = {src: 0}
front = [src]
while front:
    nxt = []
    for v in front:
        for w in adj[v]:
            if w not in dist:
                dist[w] = dist[v] + 1
                nxt.append(w)
    front = nxt
FAR = max(dist.values())
gate(int(CSZ[GI]) == 9320 and len(GE) == 33216 and len(dist) == 9320 and FAR == 16,
     "grp.giant",
     "the largest group holds {0} of the {1} cuttings with {2} moves between them, the "
     "farthest {3} moves from the first".format(int(CSZ[GI]), NS, len(GE), FAR))

M2I = dict((int(CM[i]), i) for i in range(NPIECE))
PM = []
for (_, _, g) in G:
    arr = np.zeros(NPIECE, dtype=np.int32)
    for i in range(NPIECE):
        w = 0
        for c in range(16):
            if (int(CM[i]) >> c) & 1:
                w |= 1 << int(g[c])
        arr[i] = M2I[w]
    PM.append(arr)
SOLARR = np.array(SOL, dtype=np.int32)
KEYMAP = dict((np.sort(SOLARR[i]).tobytes(), i) for i in range(NS))
PERMS = []
for arr in PM:
    img = np.sort(arr[SOLARR], axis=1)
    PERMS.append(np.array([KEYMAP[img[i].tobytes()] for i in range(NS)], dtype=np.int32))


def orbits(items, maps):
    pos = dict((v, k) for k, v in enumerate(items))
    p = list(range(len(items)))

    def f(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for mp in maps:
        for k, v in enumerate(items):
            j = pos[mp[v]]
            a, b = f(k), f(j)
            if a != b:
                p[a] = b
    return len(set(f(k) for k in range(len(items))))


CMAPS = []
for pi in PERMS:
    CMAPS.append(dict((c, int(COMP[int(pi[CREP[c]])])) for c in range(NCOMP)))
NCO = orbits(list(range(NCOMP)), CMAPS)
RIG = [int(i) for i in np.flatnonzero(DEG4 == 0)]
RSET = set(RIG)
NRO = orbits(RIG, [dict((i, int(pi[i])) for i in RIG) for pi in PERMS])
GFIX = sum(1 for cm in CMAPS if cm[GI] == GI)
gate(NCO == 14 and len(RIG) == 144 and NRO == 6 and GFIX == len(G), "grp.orbit",
     "the {0} groups fall into {1} orbits of the cell symmetry; the {2} cuttings with no "
     "smallest move at all lie in {3} of them, and the largest group is carried to "
     "itself by all {4}".format(NCOMP, NCO, len(RIG), NRO, len(G)))

sec("a label on the pieces")


def rref(rows):
    piv = {}
    for m, r in rows:
        for c in sorted(piv):
            if (m >> c) & 1:
                m ^= piv[c][0]
                r ^= piv[c][1]
        if m == 0:
            if r:
                return None
            continue
        c = (m & -m).bit_length() - 1
        for d in sorted(piv):
            if (piv[d][0] >> c) & 1:
                piv[d] = (piv[d][0] ^ m, piv[d][1] ^ r)
        piv[c] = (m, r)
    return piv


def pmask(ps):
    m = 0
    for p in ps:
        m ^= 1 << P2I[p]
    return m


CMAT = np.zeros((NS, NPO), dtype=np.float32)
for i, s in enumerate(SOL):
    CMAT[i, [P2I[p] for p in s]] = 1.0


def indmat(vs):
    W = np.zeros((NPO, len(vs)), dtype=np.float32)
    for k, v in enumerate(vs):
        for c in range(NPO):
            if (v >> c) & 1:
                W[c, k] = 1.0
    return (CMAT @ W).astype(np.int64) & 1


def induced(vs):
    if not vs:
        return 0
    R = indmat(vs)
    piv, out = {}, 0
    for k in range(R.shape[1]):
        bits = np.packbits(R[:, k].astype(np.uint8), bitorder="little")
        x = int.from_bytes(bits.tobytes(), "little")
        for c in sorted(piv):
            if (x >> c) & 1:
                x ^= piv[c]
        if x:
            piv[(x & -x).bit_length() - 1] = x
            out += 1
    return out


def freevecs(piv):
    out = []
    for f in range(NPO):
        if f in piv:
            continue
        v = 1 << f
        for c, (m, _) in piv.items():
            if (m >> f) & 1:
                v |= 1 << c
        out.append(v)
    return out


ROWS = [(pmask(list(u[0]) + list(u[1])), 1) for u in CUTP]
E6 = BYD[6]
S6 = sorted(set(pmask(set(SOL[int(E6[0, j])]) ^ set(SOL[int(E6[1, j])]))
                for j in range(E6.shape[1])))
P1 = rref(ROWS)
F1 = freevecs(P1)
R1 = induced(F1)
gate(P1 is not None and len(P1) == 86 and len(F1) == 106 and R1 == 2, "lab.one",
     "asking that the sum of the label over a cutting reverse under every smallest move "
     "is {0} demands of rank {1} on the {2} pieces in play; they are consistent, leave "
     "{3} weights free, and the labels reach 2 to the power {4}".format(
         len(ROWS), len(P1), NPO, len(F1), R1))
P2 = rref(ROWS + [(m, 0) for m in S6])
F2 = freevecs(P2)
R2 = induced(F2)
gate(P2 is not None and len(P2) == 87 and len(F2) == 105 and R2 == 1, "lab.two",
     "asking as well that it hold under every move on six pieces raises the rank to {0}, "
     "leaves {1} free, and cuts the labels to 2 to the power {2}".format(
         len(P2), len(F2), R2))

EIDX = {}
for j in range(NE4):
    a, b = int(E4[0, j]), int(E4[1, j])
    EIDX[(min(a, b), max(a, b))] = j
RPAR = list(range(len(ROWS)))


def rfind(x):
    while RPAR[x] != x:
        RPAR[x] = RPAR[RPAR[x]]
        x = RPAR[x]
    return x


for pi in PERMS:
    for j in range(NE4):
        a, b = int(pi[int(E4[0, j])]), int(pi[int(E4[1, j])])
        u = rfind(int(EREG[j]))
        v = rfind(int(EREG[EIDX[(min(a, b), max(a, b))]]))
        if u != v:
            RPAR[u] = v
RORB = {}
for k in range(len(ROWS)):
    RORB.setdefault(rfind(k), []).append(k)


def subrank(drop):
    return len(rref([ROWS[j] for j in range(len(ROWS)) if j not in drop]))


IMP = sum(1 for i in range(len(ROWS)) if subrank(set([i])) == len(P1))
FAM = sorted((len(o), subrank(set(o))) for o in RORB.values())
gate(IMP == len(ROWS) and FAM == [(12, 84), (12, 84), (24, 75), (24, 83), (48, 64)],
     "lab.core",
     "no single one of the {0} region demands is needed: drop any one of them and the "
     "rank stays {1}; but the regions fall into {2} families under the cell symmetry, and "
     "size against rank on dropping a whole family runs {3}".format(
         len(ROWS), len(P1), len(RORB), FAM))

WM = 0
for c, (m, r) in P2.items():
    if r:
        WM |= 1 << c
SM = [pmask(s) for s in SOL]
PAR = np.array([bin(WM & SM[i]).count("1") & 1 for i in range(NS)], dtype=np.int64)
DM = indmat(F2)
DIF = None
for k in range(DM.shape[1]):
    if DM[:, k].any():
        DIF = DM[:, k]
        break
SIDES = sorted(int((PAR == t).sum()) for t in (0, 1))
gate(DIF is not None and int(DIF.sum()) == NS and SIDES == [7704, 8096], "lab.same",
     "the two labels differ on every one of the {0} cuttings, so they name the same two "
     "sided split, of sizes {1}".format(NS, SIDES))
SEP = sum(1 for m, _ in ROWS if bin(WM & m).count("1") & 1)
FLIP = [sum(1 for m, _ in ROWS if bin((WM ^ (1 << b)) & m).count("1") & 1)
        for b in range(NPO) if (WM >> b) & 1]
gate(bin(WM).count("1") == 56 and SEP == len(ROWS) and max(FLIP) < len(ROWS),
     "lab.show",
     "one such label sits on {0} of the {1} pieces and puts the two cuts of all {2} "
     "regions on opposite sides; drop any single piece from it and at least one region "
     "is left unsplit, the best such attempt reaching {3}".format(
         bin(WM).count("1"), NPO, SEP, max(FLIP)))

E7, E8 = BYD[7], BYD[8]
RV4 = int((PAR[E4[0]] != PAR[E4[1]]).sum())
RV6 = int((PAR[E6[0]] != PAR[E6[1]]).sum())
RV7 = int((PAR[E7[0]] != PAR[E7[1]]).sum())
RV8 = int((PAR[E8[0]] != PAR[E8[1]]).sum())
gate(RV4 == NE4 and RV6 == 0, "lab.move",
     "the label read back off the pieces meets both demands: every one of the {0} "
     "smallest moves reverses it and none of the {1} moves on six pieces does".format(
         RV4, int(E6.shape[1])))
gate(RV7 == 26880 and int(E7.shape[1]) == 60096
     and RV8 == 28608 and int(E8.shape[1]) == 151704, "lab.keep",
     "on larger moves it does both: {0} of {1} moves on seven pieces reverse it and {2} "
     "of {3} on eight, so it is not reversed by every move".format(
         RV7, int(E7.shape[1]), RV8, int(E8.shape[1])))
P3 = rref(ROWS + [(m, 1) for m in S6])
gate(P3 is None, "lab.flip",
     "asking instead that the move on six pieces reverse the label gives a system with no "
     "solution over the field with two elements, so no label read off the pieces does "
     "that")

par2 = list(range(NS))


def find2(x):
    while par2[x] != x:
        par2[x] = par2[par2[x]]
        x = par2[x]
    return x


for d in (4, 6):
    E = BYD[d]
    for j in range(E.shape[1]):
        a, b = find2(int(E[0, j])), find2(int(E[1, j]))
        if a != b:
            par2[a] = b
KID, KREP = {}, []
for i in range(NS):
    r = find2(i)
    if r not in KID:
        KID[r] = len(KREP)
        KREP.append(i)
KCL = np.array([KID[find2(i)] for i in range(NS)], dtype=np.int64)
NK = len(KREP)
gate(NK == 157 and len(S6) == 528, "lab.bare",
     "dropping the demand that the label be read off the pieces, the same two demands "
     "leave one free sign for each of the {0} groups under moves on four and six pieces, "
     "that is 2 to the power {0} labellings".format(NK))

KMAPS = [dict((k, int(KCL[int(pi[KREP[k]])])) for k in range(NK)) for pi in PERMS]
NKO = orbits(list(range(NK)), KMAPS)
KEPT = sum(1 for pi in PERMS if bool((PAR[pi] == PAR).all()))
gate(KEPT == len(G) and NKO == 5, "lab.sym",
     "all {0} symmetries of the cell carry the label to itself, and the {1} groups fall "
     "into {2} orbits under them".format(KEPT, NK, NKO))

FAM = sorted(set(int(LAB[p]) for p in USED))
BEST = 0
for bits in itertools.product((0, 1), repeat=len(FAM)):
    w = 0
    for c in range(NPO):
        if bits[FAM.index(int(LAB[USED[c]]))]:
            w |= 1 << c
    BEST = max(BEST, sum(1 for m, _ in ROWS if bin(w & m).count("1") & 1))
PBEST = 0
for col in range(5):
    w = 0
    for c in range(NPO):
        p = USED[c]
        if col < 4:
            t = int(V[UNI[p]][:, col].sum())
        else:
            t = int(V[UNI[p]].sum())
        if t & 1:
            w |= 1 << c
    PBEST = max(PBEST, sum(1 for m, _ in ROWS if bin(w & m).count("1") & 1))
gate(len(FAM) == 4 and BEST == 48 and PBEST == 0, "lab.local",
     "no label constant on the {0} families of pieces will do: over all {1} of them the "
     "best separates {2} of the {3} regions, and the {4} labels read from the parity of a "
     "coordinate sum separate {5}".format(
         len(FAM), 2 ** len(FAM), BEST, len(ROWS), 5, PBEST))

SIDE = {}
for c in range(NCOMP):
    v = np.flatnonzero(COMP == c)
    a = int(PAR[v].sum())
    key = (int(CSZ[c]), min(a, len(v) - a))
    SIDE[key] = SIDE.get(key, 0) + 1
SDL = sorted(SIDE.items())
gate(sum(SIDE.values()) == NCOMP and [(k[0], k[1], v) for k, v in SDL] ==
     [(1, 0, 144), (2, 1, 96), (4, 2, 36), (7, 3, 48), (236, 104, 24),
      (9320, 4616, 1)], "lab.split",
     "inside each group the label splits the cuttings as {0}, written as the size of the "
     "group, the smaller side, and how many groups do that".format(
         [(k[0], k[1], v) for k, v in SDL]))

sec("the next move up, and the cuttings that cannot move at all")

ADJ = dict((i, 0) for i in range(NS))
for j in range(NE4):
    a, b = int(E4[0, j]), int(E4[1, j])
    ADJ[a] |= 1 << b
    ADJ[b] |= 1 << a
IN6, OUT6, TWO = 0, 0, 0
for j in range(E6.shape[1]):
    a, b = int(E6[0, j]), int(E6[1, j])
    if COMP[a] == COMP[b]:
        IN6 += 1
        if ADJ[a] & ADJ[b]:
            TWO += 1
    else:
        OUT6 += 1
gate(IN6 == 21696 and OUT6 == 10272 and TWO == IN6, "six.split",
     "of the {0} moves on six pieces {1} stay inside one group of the smallest move, and "
     "every one of those joins two cuttings exactly two smallest moves apart; the other "
     "{2} join two different groups".format(int(E6.shape[1]), IN6, OUT6))

par3 = list(range(NS))


def find3(x):
    while par3[x] != x:
        par3[x] = par3[par3[x]]
        x = par3[x]
    return x


LADC, LADS = [], []
for k in range(4, 11):
    E = BYD[k]
    for j in range(E.shape[1]):
        a, b = find3(int(E[0, j])), find3(int(E[1, j]))
        if a != b:
            par3[a] = b
    rt = [find3(i) for i in range(NS)]
    cnt = {}
    for r in rt:
        cnt[r] = cnt.get(r, 0) + 1
    LADC.append(len(cnt))
    LADS.append(sum(1 for r in cnt if cnt[r] == 1))
gate(LADC == [349, 349, 157, 61, 61, 13, 1]
     and LADS == [144, 144, 48, 48, 48, 0, 0], "six.ladder",
     "allowing moves on four up to ten pieces the cuttings join into {0} groups, of which "
     "{1} hold a single cutting".format(LADC, LADS))

D8 = np.zeros(NS, dtype=np.int64)
for k in range(4, 9):
    D8 += np.bincount(BYD[k].reshape(-1), minlength=NS)
FRZ = [int(i) for i in np.flatnonzero(D8 == 0)]
D10 = np.zeros(NS, dtype=np.int64)
for k in range(4, 11):
    D10 += np.bincount(BYD[k].reshape(-1), minlength=NS)
NFO = orbits(FRZ, [dict((i, int(pi[i])) for i in FRZ) for pi in PERMS])
RSP = sorted((int(a), int(b)) for a, b in
             zip(*np.unique(D10[np.array(RIG)], return_counts=True)))
GAIN = sum(1 for i in RIG if int(D8[i]) > 0)
FSIDE = sorted(set(int(PAR[i]) for i in FRZ))
SMALL = 0 if int((PAR == 0).sum()) < int((PAR == 1).sum()) else 1
gate(len(FRZ) == 48 and NFO == 1 and GAIN == 96 and RSP == [(20, 48), (60, 48), (80, 48)]
     and FSIDE == [SMALL], "six.frozen",
     "{0} cuttings admit no cost keeping move on eight pieces or fewer and form a single "
     "orbit of the cell symmetry; of the {1} with no smallest move {2} gain one at six "
     "pieces, and over those {1} the moves on ten pieces or fewer run {3}; all {0} sit on "
     "the smaller side of the label".format(len(FRZ), len(RIG), GAIN, RSP))

print("")
print("TOTAL: PASS={0} FAIL={1}".format(PF[0], PF[1]))
