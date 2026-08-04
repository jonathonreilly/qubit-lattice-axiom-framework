"""Cycle 726: the facet-visible charge of a minimal four-box dissection splits into a
tick half and a mixed half. Complete enumerations, explicit witnesses, and one carried
integer certificate; no solver is called.

Geometry (cycle 720 onward): the unit four-box has 16 corners in big-endian lexicographic
order, COR[k][j] = (k >> (3 - j)) & 1. Coordinates 0, 1, 2 are spatial; coordinate 3 is
the tick. A cell is a 5-corner simplex; a minimal dissection uses 24 unimodular cells.

Charges. The box charge BX of a cell counts vertex pairs whose SPATIAL L1 separation
exceeds 1. The facet-visible charge FC sums, over the eight facets of the box, the same
count taken inside each facet with respect to that facet's surviving spatial axes. The
two facets normal to the tick keep all three spatial axes and contribute the TICK charge
TC; the six facets normal to a spatial axis keep two spatial axes and the tick, and
contribute the MIXED charge MC. FC = TC + MC by definition.
"""
import numpy as np
from itertools import combinations, permutations, product

PASS = []


def gate(name, ok, detail=""):
    PASS.append(bool(ok))
    print("{0} {1:44s} {2}".format("PASS" if ok else "FAIL", name, detail), flush=True)


def dnum(s, w, off):
    """Decode a carried integer vector: w base-26 letters per entry, minus offset."""
    out = []
    for i in range(0, len(s), w):
        v = 0
        for ch in s[i:i + w]:
            v = 26 * v + ord(ch) - 97
        out.append(v - off)
    return np.array(out, dtype=np.int64)


def dwit(s):
    """Decode a carried 24-cell witness: 5 corner letters per cell."""
    return [[ord(ch) - 97 for ch in s[i:i + 5]] for i in range(0, len(s), 5)]


def det3(E):
    return (E[0][0] * (E[1][1] * E[2][2] - E[1][2] * E[2][1])
            - E[0][1] * (E[1][0] * E[2][2] - E[1][2] * E[2][0])
            + E[0][2] * (E[1][0] * E[2][1] - E[1][1] * E[2][0]))


def det4(E):
    t = 0
    for pm in permutations(range(4)):
        s = 1
        for a in range(4):
            for b in range(a + 1, 4):
                if pm[a] > pm[b]:
                    s = -s
        t += s * E[0][pm[0]] * E[1][pm[1]] * E[2][pm[2]] * E[3][pm[3]]
    return t


COR = np.array([[(k >> (3 - j)) & 1 for j in range(4)] for k in range(16)], dtype=np.int64)
C3 = np.array([[(k >> (2 - j)) & 1 for j in range(3)] for k in range(8)], dtype=np.int64)
POW = np.array([4, 2, 1], dtype=np.int64)

# ---------------------------------------------------------------- cells and charges
SPEC = {}
CELL = []
for cb in combinations(range(16), 5):
    dv = abs(det4((COR[list(cb)][1:] - COR[list(cb)][0]).tolist()))
    SPEC[dv] = SPEC.get(dv, 0) + 1
    if dv == 1:
        CELL.append(list(cb))
m = len(CELL)
POS = {tuple(c): i for i, c in enumerate(CELL)}
V4 = np.array([COR[c] for c in CELL], dtype=np.int64)
gate("four-box cell census", SPEC == {0: 1360, 1: 2672, 2: 320, 3: 16} and m == 2672,
     "normalized volume spectrum {0}".format(sorted(SPEC.items())))

TC = np.zeros(m, dtype=np.int64)
MC = np.zeros(m, dtype=np.int64)
BX = np.zeros(m, dtype=np.int64)
NSL, BADV = 0, 0
for p in range(m):
    vs = V4[p]
    BX[p] = sum(1 for a, b in combinations(range(5), 2)
                if int(np.abs(vs[a, :3] - vs[b, :3]).sum()) > 1)
    for i in range(4):
        for c in (0, 1):
            sl = [a for a in range(5) if vs[a, i] == c]
            if len(sl) != 4:
                continue
            NSL += 1
            kp = [j for j in range(4) if j != i]
            if abs(det3((vs[sl][1:][:, kp] - vs[sl][0][kp]).tolist())) != 1:
                BADV += 1
            ax = [j for j in range(3) if j != i]
            t = sum(1 for a, b in combinations(sl, 2)
                    if int(np.abs(vs[a, ax] - vs[b, ax]).sum()) > 1)
            if i == 3:
                TC[p] += t
            else:
                MC[p] += t
FC = TC + MC
gate("per-cell charge ranges",
     (int(BX.min()), int(BX.max())) == (3, 7) and (int(FC.min()), int(FC.max())) == (0, 7),
     "box ({0}, {1}) facet ({2}, {3}) tick ({4}, {5}) mixed ({6}, {7})".format(
         int(BX.min()), int(BX.max()), int(FC.min()), int(FC.max()),
         int(TC.min()), int(TC.max()), int(MC.min()), int(MC.max())))
gate("every facet slice of a cell is minimal", NSL == 3584 and BADV == 0,
     "four-vertex slices {0}, of these above volume 1: {1}".format(NSL, BADV))

# ---------------------------------------------------------------- facets and squares
FAC = [(i, c) for i in range(4) for c in (0, 1)]
SQ = [(a, va, b, vb) for a, b in combinations(range(4), 2)
      for va in (0, 1) for vb in (0, 1)]
SQMAP = {tuple(sorted([(a, va), (b, vb)])): s for s, (a, va, b, vb) in enumerate(SQ)}
SQB = np.zeros((8, 6), dtype=np.int64)
for f, (i, c) in enumerate(FAC):
    kp = [j for j in range(4) if j != i]
    for pf in range(3):
        for df in (0, 1):
            SQB[f, 2 * pf + df] = SQMAP[tuple(sorted([(i, c), (kp[pf], df)]))]
inc = [int((SQB == s).sum()) for s in range(len(SQ))]
gate("square-facet incidence of the four-box",
     len(SQ) == 24 and len(FAC) == 8 and all(len(set(SQB[f].tolist())) == 6 for f in range(8))
     and set(inc) == {2},
     "squares {0} facets {1}, per facet 6, per square {2}".format(
         len(SQ), len(FAC), sorted(set(inc))))

LOCOK = True
for i, c in FAC:
    ks = [k for k in range(16) if COR[k][i] == c]
    kp = [j for j in range(4) if j != i]
    if list((COR[np.array(ks)][:, kp] * POW).sum(axis=1)) != list(range(8)):
        LOCOK = False

# ---------------------------------------------------------------- one facet, complete
S3 = {}
TET = []
for cb in combinations(range(8), 4):
    dv = abs(det3((C3[list(cb)][1:] - C3[list(cb)][0]).tolist()))
    S3[dv] = S3.get(dv, 0) + 1
    if dv == 1:
        TET.append(list(cb))
WT = np.array([13, 61, 257, 1069], dtype=np.int64)
ST = int(WT.sum())
PT = np.unique(np.array([(WT[:, None] * C3[list(cb)]).sum(axis=0)
                         for cb in combinations(range(8), 4)
                         if abs(det3((C3[list(cb)][1:] - C3[list(cb)][0]).tolist())) >= 1]),
               axis=0)


def norm3(vs):
    NR = np.zeros((4, 3), dtype=np.int64)
    OF = np.zeros(4, dtype=np.int64)
    for q in range(4):
        r = [j for j in range(4) if j != q]
        E = vs[r[1:]] - vs[r[0]]
        nr = np.array([E[0, 1] * E[1, 2] - E[0, 2] * E[1, 1],
                       E[0, 2] * E[1, 0] - E[0, 0] * E[1, 2],
                       E[0, 0] * E[1, 1] - E[0, 1] * E[1, 0]], dtype=np.int64)
        of = int(nr @ vs[r[0]])
        if int(nr @ vs[q]) > of:
            nr, of = -nr, -of
        NR[q], OF[q] = nr, of
    return NR, OF


npt = len(PT)
INT = np.zeros((len(TET), npt), dtype=bool)
GEN3 = 0
for a, t in enumerate(TET):
    NR, OF = norm3(C3[t])
    R = PT @ NR.T - ST * OF[None, :]
    GEN3 += int((R == 0).sum())
    INT[a] = (R < 0).all(axis=1)
gate("facet sample family is generic",
     npt == 58 and GEN3 == 0 and S3 == {0: 12, 1: 56, 2: 2} and LOCOK,
     "cube cells {0}, samples {1}, boundary hits {2}".format(sorted(S3.items()), npt, GEN3))

BYPT = [np.flatnonzero(INT[:, q]) for q in range(npt)]
SOLS = []


def rec(cov, chosen):
    if cov.all():
        SOLS.append(list(chosen))
        return
    q = int(np.argmin(cov))
    for a in BYPT[q]:
        if not (cov & INT[a]).any():
            rec(cov | INT[a], chosen + [a])


rec(np.zeros(npt, dtype=bool), [])
D3 = np.array([v for v in product(range(-3, 4), repeat=3) if any(v)], dtype=np.int64)
GEN = 0
for sol in SOLS:
    VS = C3[np.array([TET[a] for a in sol])]
    Pj = (D3 @ VS.reshape(-1, 3).T).reshape(len(D3), len(sol), 4)
    LO, HI = Pj.min(axis=2), Pj.max(axis=2)
    if all(((HI[:, a] <= LO[:, b]) | (HI[:, b] <= LO[:, a])).any()
           for a, b in combinations(range(len(sol)), 2)):
        GEN += 1
gate("complete facet dissection sweep",
     len(SOLS) == 180 and GEN == 180 and all(len(s) == 6 for s in SOLS),
     "sample-cover assemblies {0}, separator-certified {1}, 6 cells each".format(
         len(SOLS), GEN))

SOLKEY = {tuple(sorted(tuple(TET[a]) for a in sol)): si for si, sol in enumerate(SOLS)}
TCOST = np.zeros((8, len(TET)), dtype=np.int64)
for f, (i, c) in enumerate(FAC):
    kp = [j for j in range(4) if j != i]
    axl = [kp.index(j) for j in range(3) if j != i]
    for a, t in enumerate(TET):
        vs = C3[t][:, axl]
        TCOST[f, a] = sum(1 for u, v in combinations(range(4), 2)
                          if int(np.abs(vs[u] - vs[v]).sum()) > 1)
SCOST = np.array([[int(TCOST[f, sol].sum()) for sol in SOLS] for f in range(8)],
                 dtype=np.int64)


def spec(v):
    return dict(sorted(zip(*[x.tolist() for x in np.unique(v, return_counts=True)])))


TK = [f for f, (i, c) in enumerate(FAC) if i == 3]
MX = [f for f, (i, c) in enumerate(FAC) if i < 3]
st = [spec(SCOST[f]) for f in TK]
sm = [spec(SCOST[f]) for f in MX]
gate("tick facet charge bracket",
     all(d == {18: 16, 19: 72, 20: 84, 21: 8} for d in st) and len(TK) == 2,
     "both tick facets {0}".format(st[0]))
gate("mixed facet charge bracket",
     all(d == {8: 12, 9: 64, 10: 104} for d in sm) and len(MX) == 6,
     "all six mixed facets {0}".format(sm[0]))
FLO, FHI = 2 * 18 + 6 * 8, 2 * 21 + 6 * 10
gate("facet-wise bracket for the total", FLO == 84 and FHI == 102,
     "2 x [18, 21] plus 6 x [8, 10] gives [{0}, {1}]".format(FLO, FHI))

# ---------------------------------------------------------------- diagonal patterns
PAT = np.zeros(len(SOLS), dtype=np.int64)
BITOK = True
for si, sol in enumerate(SOLS):
    v = 0
    for pf in range(3):
        fr = [j for j in range(3) if j != pf]
        for df in (0, 1):
            sq = [q for q in range(8) if C3[q][pf] == df]
            bits = set()
            for a in sol:
                inter = [q for q in TET[a] if q in sq]
                if len(inter) != 3:
                    continue
                for u, w in combinations(inter, 2):
                    if int(np.abs(C3[u][fr] - C3[w][fr]).sum()) == 2:
                        bits.add(1 if C3[u][fr[0]] == C3[u][fr[1]] else 0)
            if len(bits) != 1:
                BITOK = False
                bits = {0}
            v |= bits.pop() << (2 * pf + df)
    PAT[si] = v
UNR = [v for v in range(64) if v not in set(PAT.tolist())]
gate("realizable square-diagonal patterns",
     BITOK and len(set(PAT.tolist())) == 58 and len(UNR) == 6
     and set(bin(v).count("1") for v in UNR) == {3},
     "realizable {0} of 64, the 6 absent all have 3 set bits".format(len(set(PAT.tolist()))))


def multi(f):
    return sum(1 for v in set(PAT.tolist())
               if len(set(SCOST[f][PAT == v].tolist())) > 1)


def par(f):
    return set(int((bin(int(PAT[si])).count("1") + int(SCOST[f, si])) & 1)
               for si in range(len(SOLS)))


gate("tick facet: charge is a pattern function",
     all(multi(f) == 0 and par(f) == {0} for f in TK),
     "patterns carrying two charges {0}, parity class {1}".format(
         multi(TK[0]), sorted(par(TK[0]))))
gate("mixed facet: that law does not survive",
     all(multi(f) > 0 and par(f) == {0, 1} for f in MX),
     "patterns carrying two charges {0}, parity class {1}".format(
         multi(MX[0]), sorted(par(MX[0]))))

# ---------------------------------------------------------------- box sample family
WA = np.array([7, 31, 131, 613, 2801], dtype=np.int64)
SA = int(WA.sum())
PA = np.unique(np.einsum("k,ikd->id", WA, V4), axis=0)
NR4 = np.zeros((m, 5, 4), dtype=np.int64)
OF4 = np.zeros((m, 5), dtype=np.int64)
for p in range(m):
    for t in range(5):
        r = [j for j in range(5) if j != t]
        E = V4[p][r[1:]] - V4[p][r[0]]
        nr = np.array([((-1) ** k) * det3(np.delete(E, k, axis=1).tolist())
                       for k in range(4)], dtype=np.int64)
        of = int(nr @ V4[p][r[0]])
        if int(nr @ V4[p][t]) > of:
            nr, of = -nr, -of
        NR4[p, t], OF4[p, t] = nr, of
IN4 = np.zeros((m, len(PA)), dtype=bool)
GEN4 = 0
for p in range(m):
    R = PA @ NR4[p].T - SA * OF4[p][None, :]
    GEN4 += int((R == 0).sum())
    IN4[p] = (R < 0).all(axis=1)
gate("box sample family is generic", len(PA) == 2672 and GEN4 == 0,
     "samples {0}, boundary hits over all {1} cells: {2}".format(len(PA), m, GEN4))

# ---------------------------------------------------------------- witnesses
D4 = np.array([v for v in product(range(-4, 5), repeat=4) if any(v)], dtype=np.int64)


def genuine(sel):
    VS = V4[np.array(sel)]
    Pj = (D4 @ VS.reshape(-1, 4).T).reshape(len(D4), len(sel), 5)
    LO, HI = Pj.min(axis=2), Pj.max(axis=2)
    return all(((HI[:, a] <= LO[:, b]) | (HI[:, b] <= LO[:, a])).any()
               for a, b in combinations(range(len(sel)), 2))


def fmatch(sel):
    cnt = {}
    for p in sel:
        for t in range(5):
            fc = tuple(sorted(CELL[p][:t] + CELL[p][t + 1:]))
            cnt[fc] = cnt.get(fc, 0) + 1
    un = 0
    for fc, n in cnt.items():
        bd = any(all(COR[k][i] == v for k in fc) for i in range(4) for v in (0, 1))
        if n != (1 if bd else 2):
            un += 1
    return len(cnt), un


def facetsum(sel):
    tot, ok = 0, True
    for f, (i, c) in enumerate(FAC):
        kp = [j for j in range(4) if j != i]
        sub = []
        for p in sel:
            sl = [k for k in CELL[p] if COR[k][i] == c]
            if len(sl) == 4:
                sub.append(tuple(sorted(int((COR[k][kp] * POW).sum()) for k in sl)))
        key = tuple(sorted(sub))
        if len(sub) != 6 or key not in SOLKEY:
            ok = False
            continue
        tot += int(SCOST[f, SOLKEY[key]])
    return tot, ok


WIT = {
    "W1": "abcejacejmacilmaijlmbcdhlbcegmbcfhlbcfjlbcfjmbefgmcfghocfgmo"
          "cfhjncfhmpcfjmncfmnpchjlpchjnpchkmociklpcikmpcjlmpcjmnphkmop",
    "W3": "abcejacejmacijmbcdglbcegnbcejnbcglnbcjlnbdfglbefgnbfglncegno"
          "cejmncemnocglnocijkmcjklocjkmocjlnocjmnodfghpdfglpfglnpglnop",
    "W4": "abcgkabegmabgikabgimbcdhlbcghlbcgklbefhmbeghmbfhlmbflmnbghil"
          "bghimbgiklbhilmbijlmbjlmnfhlmnghilmghlmpgiklmgklmoglmophlmnp",
    "W5": "abdemabdipabimpacdgiadegibdehpbdempbdilpbefhpbefmpbfinpbijlp"
          "bijnpcdgmocdilmcdlmpciklpcikmpckmopdeghodegimdehopdemopfimnp",
    "W6": "abceibcdgkbcegkbceikbdfgjbdgkobdilobefgnbegjnbegkmbeikmbgkmo"
          "bijlmbilmodfghpdfgjldfglpdikloegjmpejmnpfgjlpfgjnpgjlmpglmop",
}
KU = set()
for sg in permutations(range(4)):
    cur, path = 0, [0]
    for j in sg:
        cur |= 1 << (3 - j)
        path.append(cur)
    KU.add(tuple(sorted(path)))
SEL = {"W2": sorted(POS[c] for c in KU)}
WLEN = set()
for nm, s in WIT.items():
    WLEN.add(len(s))
    SEL[nm] = sorted(POS[tuple(sorted(c))] for c in dwit(s))

ROW = {}
for nm in ("W1", "W2", "W3", "W4", "W5", "W6"):
    sel = SEL[nm]
    nd, un = fmatch(sel)
    fs, fok = facetsum(sel)
    cov = IN4[np.array(sel)].sum(axis=0)
    ROW[nm] = (int(TC[sel].sum()), int(MC[sel].sum()), int(FC[sel].sum()),
               int(BX[sel].sum()), nd, un)
    gate(nm + " is a genuine dissection",
         len(set(sel)) == 24 and WLEN == {120} and genuine(sel)
         and int(cov.min()) == 1 and int(cov.max()) == 1
         and fok and fs == int(FC[sel].sum()),
         "tick {0} mixed {1} facet {2} box {3}, facets {4}, unmatched {5}".format(*ROW[nm]))

gate("the facet-wise ceiling is attained",
     ROW["W4"][0] == 2 * 21 and ROW["W4"][1] == 6 * 10 and ROW["W4"][2] == FHI,
     "W4 reaches 2 x 21 and 6 x 10 together, total {0}".format(ROW["W4"][2]))
gate("each half reaches its own floor alone",
     ROW["W5"][0] == 2 * 18 and ROW["W6"][1] == 6 * 8,
     "W5 tick {0} is 2 x 18, W6 mixed {1} is 6 x 8".format(ROW["W5"][0], ROW["W6"][1]))

# ---------------------------------------------------------------- carried certificate
CIDX = ("aaaaabaacaadaaeaafaagaahaaiaaoaaqaaraasaataauaavaawaaxabgabhabiabjabkablabmabn"
        "abwabxabyabzacaacbaccacdaceackacmacqacuacvacwacxacyaczadaadbadfadgadnadoaeaaee"
        "aeiaemaeqaeraesaetaeuaevaewaexafbafcafjafkafwagaageaggagiagkaguagyahkahmahoahq"
        "aiaaieaiqairaisaitaiuaivaiwaixaiyajaajcajeajgajhajiajjajkajlajmajnajwajxajyajz"
        "akaakbakcakdakmaknakoakpakqakraksaktakuakwakyalaalcalgallalmalpalqalvalwamdame"
        "anhanianlanmanransanzaoaaomaoqaowaoyapkapoaqaaqcaqeaqgaqqaquargaroarwarxaryarz"
        "asaasbascasdasjaslasmasoatfatgatratsauiauqauyavoavqavsavuawkawmayaayqaywayxayy"
        "azaazcazhaziazjazkazlazmazoazqazsazxazybaababbagbaibambanbapbaqbatbaubawbaybba"
        "bbdbbgbbhbbibbjbbkbblbbmbbnbbpbcdbcebdbbdcbdmbdobdqbdsbdwbdxbdybeabebbecbeebeh"
        "beibejbenbeobeubexbeybfcbfebfqbfsbftbfvbfzbgabgbbgqbgrbgtbgubgwbgxbgzbhnbhobiv"
        "bjabkibksbktblfblkblqblsblublwbmabmcbmhbmibmmbmpbmtbmubnbbnobofbokbsabsibsqbsr"
        "bssbstbsubsvbswbsxbtdbtfbtgbtibtzbuabulbumbvcbvkbvsbwibwkbwmbwobxebxgbyubzkbzo"
        "caqcbwccacceccfccgcchcciccjcckcclccpccqccxccycdkcdocdscdwceacebceccedceecefceg"
        "cehcelcemcetceucfgcfkcglcgmcibcikciwcjacjecjicjzckbckcckecqmcqucrccrdcrecrfcrg"
        "crhcricrjcrpcrrcrscrucslcsmcsxcsyctoctwcvccvncvocvvcvwczvczwdaedfcdfgdgidhodhq"
        "dhsdhudiediidiudiwdiydjadjkdjodmmdncdnedngdnidnydoadpodtwduadvc")
CVAL = ("bibcbcbcbcbcbcbiavavbibabbbbbbbbbabibibabbbbbbbbbabibhbbbcbcbcbcbbbhaxaxasasar"
        "auavapapavauarauatatauapapapaparatauapapauataravauauavasasbababababcbcbcbcbcbc"
        "ayaybibbbabbbbbabbbiatauauatbeaxaxayayaxaxbebeaxaxayayaxaxbebfayayazazayaybfaz"
        "ayayazauaubaayaybaaxaxaxaxaxaxaxaxaybabaayauauaxaxauauazayayazaqaqakanagamauar"
        "arauamagauararauauauauauanakazazayayazayayazaqapajapauauavbaavavbaavasapasavay"
        "auazayaxajapavavaqatauauamamauatavavavavatauatauaubabaapasatasatavarasaxasatar"
        "auauatatanatavavbcasaratataqavasauauauauauauapauauatatataxatatatbabbbbbaavavat"
        "avaxatavatasatatatanaqajapauararauapajauararauauauauauaqanatatayayatayayatblbl"
        "bkblblboaybcbcbcbcaybobfbdbdbfazazazazbobdbfbcbcbfbdbobcayaybcblblbdbdaxaxazaz"
        "azazaxbdbdaxbkbdbgbebfbdbdbfbebgaxbdbdaxaxaxbfbfbdbkbdbcayaybcayaybdblblbkamam"
        "amamaoaoaqararaqafafaganaoaoanaoaoagahahaa")
ci = dnum(CIDX, 3, 0)
cv = dnum(CVAL, 2, 22)
yv = np.zeros(len(PA), dtype=np.int64)
yv[ci] = cv
load = np.array([int(yv[IN4[p]].sum()) for p in range(m)], dtype=np.int64)
slack = 2 * FC - load
gate("carried denominator-2 lower certificate",
     len(CIDX) == 3 * 411 and len(CVAL) == 2 * 411 and len(set(ci.tolist())) == 411
     and int(slack.min()) >= 0 and int(yv.sum()) == 170,
     "support {0}, weight sum {1}, least slack {2}, values ({3}, {4})".format(
         len(ci), int(yv.sum()), int(slack.min()), int(cv.min()), int(cv.max())))
gate("joint floor 85 sits one above 84",
     int(yv.sum()) == 2 * 85 and ROW["W1"][2] == 85 and 85 == FLO + 1,
     "certificate gives at least 85, W1 attains it, facet-wise floor {0}".format(FLO))

# ---------------------------------------------------------------- square consistency
INF = 1000
MINC = np.full((8, 64), INF, dtype=np.int16)
for f in range(8):
    for si in range(len(SOLS)):
        if SCOST[f, si] < MINC[f, PAT[si]]:
            MINC[f, PAT[si]] = SCOST[f, si]
best = INF * 8
CH = 1 << 21
for lo in range(0, 1 << 24, CH):
    x = np.arange(lo, lo + CH, dtype=np.int32)
    tot = np.zeros(CH, dtype=np.int16)
    for f in range(8):
        ix = np.zeros(CH, dtype=np.int32)
        for j in range(6):
            ix |= ((x >> int(SQB[f, j])) & 1) << j
        tot += MINC[f][ix]
    best = min(best, int(tot.min()))
gate("complete sweep of the 24 square diagonals", best == 86,
     "least facet charge over consistent assignments {0}".format(best))
gate("square consistency costs at the floor",
     ROW["W1"][2] < best <= ROW["W3"][2] and ROW["W1"][5] > 0 and ROW["W3"][5] == 0,
     "free {0} below consistent {1}, face-to-face witness {2}".format(
         ROW["W1"][2], best, ROW["W3"][2]))
gate("face-to-face does not move the box bracket",
     ROW["W1"][3] == 108 and ROW["W2"][3] == 108 and ROW["W4"][3] == 128
     and ROW["W2"][5] == 0 and ROW["W4"][5] == 0,
     "face-to-face witnesses at box charge {0} and {1}".format(ROW["W2"][3], ROW["W4"][3]))
gate("stencil orbit sits above the facet floor",
     ROW["W2"][2] == 96 and ROW["W1"][3] == ROW["W2"][3] and ROW["W2"][2] > ROW["W1"][2],
     "at box charge {0}: stencil facet {1}, W1 facet {2}".format(
         ROW["W2"][3], ROW["W2"][2], ROW["W1"][2]))
gate("stencil orbit is extremal in both halves",
     ROW["W2"][0] == 2 * 18 and ROW["W2"][1] == 6 * 10
     and ROW["W5"][0] == 2 * 18 and ROW["W5"][1] < 6 * 10,
     "stencil tick {0} at floor with mixed {1} at ceiling; W5 pairs {2} with {3}".format(
         ROW["W2"][0], ROW["W2"][1], ROW["W5"][0], ROW["W5"][1]))

print("TOTAL: PASS={0} FAIL={1}".format(sum(PASS), len(PASS) - sum(PASS)), flush=True)
