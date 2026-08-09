"""Exact adjacency-cost bracket for dissections of one tick-box into corner pieces.

Everything here is a theorem of a SUPPLIED structural model, not of the framework
axioms alone.  The model: the box is one lattice cell carried through one tick --
three spatial coordinates and a tick coordinate, sixteen corners; a piece is the
convex hull of five corners with nonzero volume, all ten vertex pairs graded by the
spatial part of their separation; a dissection is a family of pieces with disjoint
interiors whose volumes fill the box.  The Lattice axiom supplies only the spatial
Z^3 nearest-neighbour adjacency that grades the vertex pairs and the 24 proper cubic
rotations acting here; the registered kinetic-isotropy primitive supplies only the
equal tick/edge graining under which the tick coordinate enters.  Neither supplies a
cell selection or a rule-to-tick correspondence: whether physical assembly cells are
pairwise-adjacency simplices at all, and the physical tick-Admissibility realization
bridge, are OPEN questions this runner does not touch.

The adjacency cost of a piece counts its vertex pairs whose spatial separation is
more than one step -- the pairs the supplied model grades as exceeding the axiom's
nearest-neighbour adjacency.  This runner brackets that cost from both sides, first
over the minimal-volume pieces alone and then over every corner piece.

Volume throughout is the normalized lattice 4-volume |det(v1-v0, ..., v4-v0)|, which
is 4! = 24 times the Euclidean volume, so the whole box has normalized volume 24.
This normalization is a declared convention of the runner, load-bearing in the
24-piece count and in every volume-sum check.

Everything is verified in exact integers.  No solver runs here: the bounds are carried
as integer multiplier vectors and checked directly, the attaining families are carried
as piece lists and checked to be genuine dissections, and the parity statement is
derived in-runner by elimination over the two-element field.

The negative-flavoured gates are scoped narrowly by design.  The single-orbit gate
quantifies over the 114 point-orbits of the carried invariant sample family only; the
strengthening gate tests five representative certificates only; the coarse-parity
gate shows only that THIS incidence-plus-volume certificate family does not extend
past the minimal pieces.  None of them is a universal negative.

Soundness of the sample-point device: a dissection covers every interior point of the
box exactly once, so every dissection is one of the families that cover the sample
points exactly once.  A bound proved for all such families therefore holds for all
dissections, and a family that both attains the bound and passes the disjointness
decision procedure turns the bound into an equality.

Disjointness is decided, not merely tested.  Two convex bodies have disjoint interiors
exactly when some direction separates them.  All vertices here are zero-one corners, so
differences lie in the ternary cube, and any supporting direction may be taken
orthogonal to three ternary vectors -- a three by three ternary determinant, hence
entries bounded by four.  Sweeping every direction in that range decides the question.

The runner fails closed: any failed gate makes the process exit nonzero.
"""
import json
import sys
from fractions import Fraction as F
from itertools import combinations, permutations, product
import numpy as np

GATES = []


def gate(name, ok, detail=""):
    GATES.append((name, bool(ok)))
    print("{0} {1:50s} {2}".format("PASS" if ok else "FAIL", name, detail), flush=True)


def dec(s):
    """Decode one carried integer vector from its base-26 letter form."""
    out = []
    for t in s.split(","):
        neg = t[0] == "-"
        v = 0
        for ch in (t[1:] if neg else t):
            v = 26 * v + ord(ch) - 97
        out.append(-v if neg else v)
    return np.array(out, dtype=np.int64)


COR = np.array([[(k >> (3 - j)) & 1 for j in range(4)] for k in range(16)],
               dtype=np.int64)


def det4(E):
    t = 0
    for p in permutations(range(4)):
        s = 1
        for a in range(4):
            for b in range(a + 1, 4):
                if p[a] > p[b]:
                    s = -s
        t += s * E[0][p[0]] * E[1][p[1]] * E[2][p[2]] * E[3][p[3]]
    return t


def det3(E):
    return (E[0][0] * (E[1][1] * E[2][2] - E[1][2] * E[2][1])
            - E[0][1] * (E[1][0] * E[2][2] - E[1][2] * E[2][0])
            + E[0][2] * (E[1][0] * E[2][1] - E[1][1] * E[2][0]))


CELL, V, W, DT = [], [], [], []
spec = {}
for c in combinations(range(16), 5):
    vs = COR[list(c)]
    v = abs(det4((vs[1:] - vs[0]).tolist()))
    spec[v] = spec.get(v, 0) + 1
    if v:
        CELL.append(c)
        V.append(vs)
        DT.append(v)
        W.append(sum(1 for a, b in combinations(range(5), 2)
                     if int(np.abs(vs[a, :3] - vs[b, :3]).sum()) > 1))
V = np.array(V)
W = np.array(W, dtype=np.int64)
DT = np.array(DT, dtype=np.int64)
n = len(V)
MIN = np.flatnonzero(DT == 1)
WM = W[MIN]
gate("five-corner subsets and volume spectrum",
     spec == {0: 1360, 1: 2672, 2: 320, 3: 16} and n == 3008,
     "nondegenerate {0}  spectrum {1}".format(n, sorted(spec.items())))
gate("minimal-volume pieces and cost ranges",
     len(MIN) == 2672 and (int(WM.min()), int(WM.max())) == (3, 7)
     and (int(W.min()), int(W.max())) == (3, 9),
     "minimal {0}  cost 3 to 7 minimal, 3 to 9 all".format(len(MIN)))

NR = np.zeros((n, 5, 4), dtype=np.int64)
OF = np.zeros((n, 5), dtype=np.int64)
for v in range(n):
    for k in range(5):
        rest = [j for j in range(5) if j != k]
        E = (V[v][rest[1:]] - V[v][rest[0]]).tolist()
        nr = np.array([((-1) ** i) * det3([r[:i] + r[i + 1:] for r in E])
                       for i in range(4)], dtype=np.int64)
        off = int(nr @ V[v][rest[0]])
        if int(nr @ V[v][k]) > off:
            nr, off = -nr, -off
        NR[v, k], OF[v, k] = nr, off
gate("facet normals bound each piece",
     bool(((V @ NR.transpose(0, 2, 1) - OF[:, None, :]) <= 0).all()),
     "every vertex on the inner side of all five facets")

ROT = []
for pm in permutations(range(3)):
    for sg in product((-1, 1), repeat=3):
        M = np.zeros((3, 3), dtype=np.int64)
        for i in range(3):
            M[i, pm[i]] = sg[i]
        if det3(M.tolist()) == 1:
            R = np.eye(4, dtype=np.int64)
            R[:3, :3] = M
            ROT.append(R)
ROT = np.array(ROT)
shut = all(any(bool((ROT[a] @ ROT[b] == ROT[c]).all()) for c in range(len(ROT)))
           for a in range(len(ROT)) for b in range(len(ROT)))
gate("proper rotations of the spatial lattice", len(ROT) == 24 and shut,
     "order 24, shut under composition, tick fixed")

WA = np.array([7, 31, 131, 613, 2801], dtype=np.int64)
SA = int(WA.sum())
PA = np.einsum("k,ikd->id", WA, V[MIN])

WB = np.array([101, 211, 307, 401, 503], dtype=np.int64)
SB = int(WB.sum())
CID = {tuple(x): i for i, x in enumerate(COR.tolist())}
LOOK = {c: i for i, c in enumerate(CELL)}
MPOS = -np.ones(n, dtype=np.int64)
MPOS[MIN] = np.arange(len(MIN))
ctr = np.ones(4, dtype=np.int64)
PERM = np.zeros((24, len(MIN)), dtype=np.int64)
for g, R in enumerate(ROT):
    for i, c in enumerate(MIN):
        im = ((V[c] * 2 - ctr) @ R.T + ctr) // 2
        PERM[g, i] = MPOS[LOOK[tuple(sorted(CID[tuple(x)] for x in im.tolist()))]]
gate("rotations permute the minimal pieces",
     bool((np.sort(PERM, axis=1) == np.arange(len(MIN))[None, :]).all()),
     "each rotation permutes the 2672 minimal pieces")

orb = -np.ones(len(MIN), dtype=np.int64)
oreps = []
for i in range(len(MIN)):
    if orb[i] < 0:
        orb[np.unique(PERM[:, i])] = len(oreps)
        oreps.append(i)
K = len(oreps)
osz = sorted({int((orb == o).sum()) for o in range(K)})
gate("orbits of pieces under the rotations", K == 114 and osz == [8, 24],
     "{0} orbits, sizes {1}".format(K, osz))

base = (WB[None, :, None] * V[MIN][oreps]).sum(axis=1)
pts = {tuple(x) for x in base.tolist()}
for R in ROT:
    for x in base:
        pts.add(tuple(((x * 2 - SB * ctr) @ R.T + SB * ctr) // 2))
PB = np.array(sorted(pts), dtype=np.int64)
pos = {tuple(x): i for i, x in enumerate(PB.tolist())}
img = np.array([[pos[tuple(((x * 2 - SB * ctr) @ R.T + SB * ctr) // 2)]
                 for x in PB] for R in ROT], dtype=np.int64)
porb = -np.ones(len(PB), dtype=np.int64)
lab = 0
for i in range(len(PB)):
    if porb[i] < 0:
        porb[np.unique(img[:, i])] = lab
        lab += 1
psz = sorted({int((porb == o).sum()) for o in range(lab)})
gate("sample points and their orbits",
     len(PB) == 2736 and lab == 114 and psz == [24],
     "{0} points in {1} orbits, every orbit of size 24".format(len(PB), lab))


def member(P, S):
    IN = np.zeros((n, len(P)), dtype=bool)
    face = 0
    for v in range(n):
        s = P @ NR[v].T - S * OF[v][None, :]
        IN[v] = (s < 0).all(axis=1)
        face += int(((s == 0).any(axis=1) & (s <= 0).all(axis=1)).sum())
    return IN, face


INA, faceA = member(PA, SA)
INB, faceB = member(PB, SB)
gate("no sample point meets a piece boundary", faceA == 0 and faceB == 0,
     "boundary incidences {0} and {1} across all {2} pieces".format(faceA, faceB, n))
cnt = INB.sum(axis=1)
gate("each family sits inside the pieces it should",
     bool(INA[MIN, np.arange(len(MIN))].all()) and int(cnt.min()) == 6
     and int(cnt.max()) == 1041 and bool(INB.any(axis=0).all()),
     "invariant points per piece 6 to 1041, every point used")

BO = np.zeros((n, K), dtype=np.int64)
for o in range(K):
    BO[:, o] = INB[:, porb == o].sum(axis=1)
gate("orbit counts refine the point membership",
     bool((BO.sum(axis=1) == cnt).all()) and int(BO.max()) <= 24,
     "114 orbit counts reproduce every piece's point total")
SPARSE = ("a,b,g,h,i,j,o,p,s,t,u,v,w,x,ba,bb,bc,bd,be,bf,bk,bu,bw,bx,cc,cd,ce,cf,ck,cl,co,cp,cq,cr,cs,ct,cw,cx,cy,cz,da,db,dd,dn,dw,dx,dy,dz,ea,eb,em,eu,ew,ex,ey,ez,fk,fl,fm,fn,fp,ga,gb,gd,gr,hi,hk,hm,hr,ht,hv,hy,ib,id,ie,ig,ij,io,iq,ir,iu,iv,iy,iz,jc,jd,ji,jj,jm,jn,jq,jr,ju,jv,jw,kb,kf,ki,ko,kp,kq,kr,ks,kt,kw,kx,li,lk,mj,ml,mn,mq,mr,ms,mt,mu,mv,mw,mx,mz,na,ne,ng,nh,ni,nl,oe,of,og,oh,oi,om,on,ov,oy,oz,pa,pb,pf,qc,qj,rh,ry,sp,uw,vb,vc,vi,vj,vk,vl,vm,vn,wh,wm,wt,xa,xb,xc,xd,xe,xf,xg,xk,xo,yc,yd,ye,yu,zr,beb,bec,bef,beg,beh,bek,bez,bjr,bjx,blg,bnz,bod,boe,bop,bou,bqa,bqb,bqf,bqh,bql,bqx,bra,brf,bwf,bwt,bxb,bxo,bxv,bxw,bxx,cgl,chc,ckv,ckz,cpo,cpp,cqc,cqp,cqq,cza,ddl", "-b,-b,b,b,-b,-b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,-b,-b,b,b,-b,-b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,-b,-b,-b,-b,b,b,b,-b,b,-b,b,b,-b,-b,-b,-b,b,-b,b,-b,b,b,b,b,-b,-c,-d,-b,b,b,-d,-c,b,b,c,c,b,b,c,c,b,b,-c,-c,-b,-b,-c,-c,-b,-b,-b,-b,b,b,b,b,-b,-b,-b,-b,b,b,b,b,-b,-b,b,b,b,-b,-b,-b,-b,-b,-b,b,b,b,b,b,b,b,-b,-b,-b,-b,-b,-c,-c,b,-b,-b,-b,-b,-c,b,b,b,b,b,-b,-b,-b,b,-b,-b,b,-b,-b,-b,-b,-b,-b,-b,-b,-b,-c,-b,-b,-b,b,-b,-b,-c,b,-b,b,-b,-b,b,d,d,c,b,b,b,b,b,b,b,-b,b,b,b,b,b,b,-b,-c,-b,b,b,b,-b,-b,-b,b,b,b,b,-c,-c,b,-b,-b,b,b", "e")
CERT = {
    "flo1": ("dm,-dm,dm,-co,-dm,dm,dm,dm,dm,-dm,dm,dm,dm,i,-cu,cn,-bu,dm,-dm,-dm,-dm,-dm,-dm,co,dm,i,dm,-dm,br,cf,-dm,-dm,dm,-u,a,dm,dm,-dm,dm,-dm,j,-dm,-dm,-dm,dm,-dm,-cs,-dm,-bp,-dm,dm,dm,-dm,dm,-dm,dm,dm,cz,-dm,dm,-dm,dm,dm,dm,-ch,-dm,-dm,-dm,dm,dm,dm,dm,-dl,-dm,-co,dm,-dm,-dm,dm,-cq,dm,-dm,dm,w,dm,-dm,-bq,-dm,-dm,dm,-dm,-dm,-dm,-dm,-dm,-dm,l,-dm,dm,-dm,dm,-dm,-dm,-dm,-cw,dm,dm,-v,dm,dm,dm,dm,dm,bf", "jp", 1),
    "flo2": ("-dm,cs,-dm,dm,dm,dm,-dm,cq,dm,dm,dm,dm,dm,de,dm,dm,-dm,dm,c,dm,dm,-dm,-dm,dm,ck,-dm,dm,-dm,-dm,-di,dm,-dm,dm,dm,-dm,dm,cp,-dm,cr,-dm,-dm,-dm,-dm,dm,-dm,dm,-dm,dc,-cy,-dm,co,dm,dm,dm,dm,cq,-bu,-dm,-dm,ct,-dm,-dm,dm,dm,-dm,dm,dm,-cg,-dm,-c,dm,dm,dm,ce,k,dm,-dc,-dm,cg,-dm,dm,-dm,g,-dm,dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-bk,-dm,dm,-dm,dm,-dm,-dm,dm,-dm,dm,dm,dm,dm,dm,dm,dm,dm,-di", "-ri", 2),
    "flo3": ("-dc,cr,-dm,dm,dm,dm,-dm,cr,dm,dm,dm,-m,dm,df,dm,dm,-dm,dm,i,dm,dm,-dm,-dm,di,ck,-dm,dm,-dm,-dm,-bt,dm,-dm,dm,dm,-dm,dm,cn,-dm,dm,-cp,-dm,-dm,-dm,dm,-dm,dm,-cv,dm,-dm,-dm,co,by,dm,dm,cc,cs,-bv,-dm,-dm,dm,-dm,-dm,dm,dm,-dm,dm,dm,-dm,-dm,dm,dm,dm,dm,bj,j,dm,-cz,-dm,cm,-dm,dm,-dm,f,-dm,dm,-dc,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-bl,-dm,dm,-dm,dm,-dm,-dm,dm,-dm,dk,dm,dm,dm,dm,dm,dm,dm,-dm", "-rf", 3),
    "flo6": ("-dm,dm,-dk,dm,dm,dm,-dm,dm,dm,dm,dm,dm,dm,bg,dm,dm,-dm,dm,dm,l,dm,-dm,-dm,cc,bg,-dm,-cu,-dm,-dm,-dm,-m,-dm,be,dm,-bz,dm,dm,-dm,-dm,dm,-dm,-dm,-dm,dm,-de,dm,-dm,dm,dm,-dm,dm,cc,dm,dm,bp,dm,-i,cg,-dl,dm,-ck,dm,dm,dm,-dm,-b,dm,-dm,-dm,-dm,e,dm,dm,cw,-dm,dm,cy,-dm,dm,-dm,-n,-dm,bv,-dm,dm,-dm,d,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,-dm,dm,-dm,dm,-dm,-dm,dm,dm,-dm,dm,-y,df,dm,dl,dm,dk,-dl", "-nk", 6),
    "fup1": ("dk,-dm,-dm,-dm,-dm,-l,dm,dm,-dm,dm,dm,-bt,dm,-cx,-dm,-dm,dm,dm,-dm,-dm,-dm,dm,-dm,p,dm,-cx,dm,-cq,-b,-g,dm,-dm,dm,dm,-d,e,-dm,-q,dm,-dl,bq,-dm,-dm,-cu,-dm,dm,dm,-da,-dm,-dm,q,-dm,-cu,d,-dm,dm,-dm,-dm,-s,-dm,dm,-di,-dm,dm,dm,-dm,dm,-dk,-cg,dm,dm,-dm,-dm,-dm,dm,dm,-by,dm,dm,dm,-y,dm,bl,dm,-dm,dm,dm,dm,dm,-dm,dm,dm,o,dm,dm,dm,-dm,dm,-dm,dm,-dm,x,-dm,-dm,bk,-dm,-h,-bu,bl,-dm,-dm,-dm,-dm,dm", "tf", 1),
    "fup2": ("-bz,-q,dm,-dm,-dm,-dm,-dm,dm,-dm,dc,dm,-l,dm,-dm,-dm,-dm,dm,-ba,-dm,-be,-dm,cw,dm,-dm,dm,-q,dm,-dm,dm,dm,ch,dm,dm,-dm,bh,dl,-dm,-v,dm,bf,-dm,dm,-dm,-dm,-dm,-dm,bn,-dm,-dm,-cx,-dm,-dm,-dm,dm,-bp,dm,-bt,-dm,-cr,bq,y,dm,-dm,bg,dm,-dm,dm,dm,w,-bo,dm,-dm,dh,bp,ch,-bi,-dm,-dm,-dm,dm,dm,dm,dm,dm,-dm,dm,-dm,dm,dm,-j,dm,dm,-dm,dc,dm,dm,-cv,-dm,dm,dl,-dm,cd,-dm,-dm,-dm,dm,-dm,da,-dm,-dm,-dm,-bw,-dm,dm", "mm", 2),
    "fup3": ("-dm,-dm,-cd,-dm,-dm,dm,-s,dm,dm,bz,-dg,dm,dm,-bm,be,-dc,dm,-br,dk,y,-dm,dm,-cz,-dm,dm,-bm,dm,-dl,di,dm,-dm,dm,-dm,-dm,-cg,-dm,dm,b,-dm,dm,-dm,-y,-dm,-dm,dm,-dm,-dm,-w,u,-dm,dm,dm,-dm,-dl,f,-cf,dm,-dm,-cx,dm,dm,-dm,l,-dm,dj,cy,cp,bd,dm,-bv,bu,-e,-de,-dh,-dm,dm,dm,bs,dm,ct,s,dm,-dm,dm,dm,-dm,dm,-dm,dm,-dm,dm,-dm,dj,dm,-dm,bb,-dm,dm,-dm,-dl,-cs,-dm,-dm,dm,q,-dm,dl,-dm,dm,-dm,dm,-bx,-cz,dm", "pd", 3),
    "fup6": ("bx,-x,df,-dm,cr,cx,dm,dm,-dm,-dl,dm,-cu,dm,-de,-dm,-dm,di,-e,-dm,-ba,-dm,be,ct,-dm,g,-dm,dm,bv,ca,bd,bq,cq,dm,dm,bq,y,-dm,ce,dm,-dl,dj,-dm,-dm,-dj,-dm,-dm,-dh,-dk,-dm,-dm,-dl,-cd,-ca,di,-cb,dm,bi,-dm,dm,bn,cw,-cx,-dk,-dc,dl,-dl,-dm,dm,dm,cs,dm,-dd,n,-bl,dm,dm,-ce,dh,-bc,dm,dm,dm,dm,-bj,ba,dm,-dm,ce,dm,dj,-dm,dm,-dm,-dh,bf,-dm,-dm,-dm,dm,-dm,-dm,-dm,-dm,-dm,-df,dm,m,t,bl,-da,dk,o,-cr,cj", "mv", 6),
    "min108": ("-c,a,a,a,a,a,a,b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b,a,a,a,a,a,c,a,a,a,a,a,a,a,c,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,-c,a,a,a,a,a,a,c,a,a,a,a,a,-b,a,a,a", "g", 2),
    "min128": ("-ch,-bu,-ci,-ci,ci,-ci,-be,ci,cf,ci,-ci,ci,ci,-r,-ci,-ci,bz,-ci,ci,be,-d,ci,ci,-ci,-ci,-ci,-ci,ci,-ci,-ci,-ci,a,-ci,ci,d,ci,-ci,ci,-ci,ci,ci,be,-ci,ci,-ci,bk,-ci,ci,-cf,-ci,ci,ci,-y,ci,ci,ci,ci,ci,-ch,-ci,ci,ci,-ci,-cd,y,-ce,-cf,-ce,r,ci,ci,-bd,-ch,ci,b,-ci,-ch,ci,-ci,bg,-ci,-ci,bn,-ci,cf,-ci,-bk,ci,ci,ci,x,bm,ci,-ci,-ci,-ci,-ci,-l,ci,-ci,ci,-ci,ci,ci,bl,-ci,ci,-ci,-ci,-ci,ci,-ci,ce,ci", "hq", 3),
    "mlo1": ("-db,-dc,dc,-cx,-dc,-cu,-dc,dc,dc,-cx,dc,-cx,dc,ca,bm,-cw,-e,bv,a,-cw,-dc,-db,da,-dc,dc,ca,-dc,bo,dc,-g,h,dc,-d,dc,cb,-dc,dc,-dc,dc,-dc,-db,dc,-dc,ch,-dc,-dc,dc,-b,-dc,dc,cs,-o,-bb,-dc,da,-dc,-bf,dc,-cu,bm,cz,-dc,cy,dc,-dc,cx,bx,dc,-db,-dc,ch,dc,cq,-bt,-dc,-dc,-dc,da,-dc,-ci,y,-dc,-dc,u,-dc,-dc,cp,dc,dc,-be,dc,dc,dc,-dc,-dc,-cx,dc,v,-dc,dc,-cy,cl,dc,db,-dc,-cq,-dc,bd,da,k,y,dc,da,-cz", "dj", 1),
    "mlo2": ("-l,-cn,dc,-dc,-dc,-dc,-dc,dc,dc,-dc,dc,-dc,dc,cm,cs,-da,dc,dc,-dc,cx,-dc,u,-cu,-ce,dc,db,-n,-db,cd,dc,dc,db,ci,-dc,-m,-dc,dc,db,dc,-dc,-bu,dc,-dc,-dc,-dc,-dc,dc,-dc,-dc,dc,-dc,-dc,dc,-dc,-dc,-bs,-cw,s,bw,-ci,dc,dc,bo,dc,-db,db,dc,dc,cb,-t,dc,dc,dc,ct,cn,-dc,k,-by,-dc,-dc,-n,-dc,-dc,dc,-dc,-dc,-dc,-cy,q,-bq,dc,dc,-dc,-dc,cj,-dc,dc,-dc,-q,dc,-dc,dc,-dc,-dc,cn,cz,dc,-dc,-bn,dc,dc,dc,dc,-dc", "j", 2),
    "mlo3": ("-c,-dc,dc,-o,-dc,-dc,-dc,dc,-bo,dc,dc,-dc,dc,bu,-dc,v,-dc,dc,-dc,-dc,-dc,-dc,dc,-bz,dc,bu,-dc,dc,-dc,-j,-dc,-b,dc,bc,dc,cy,-dc,-dc,dc,-dc,t,dc,-k,dc,-dc,bj,dc,-bl,-dc,dc,o,u,-da,ct,be,dc,dc,dc,-cn,dc,dc,dc,-dc,dc,-dc,dc,-bo,dc,-dc,-dc,-cp,-dc,-cv,k,-dc,-dc,dc,-dc,-dc,-bz,-dc,dc,dc,dc,-dc,-dc,-dc,dc,dc,dc,dc,dc,-dc,dc,-dc,dc,-dc,dc,-dc,dc,-dc,db,-dc,dc,-cg,cu,-dc,-dc,-cq,dc,dc,dc,-dc,-dc", "eg", 3),
    "mlo6": ("-dc,-dc,dc,-dc,-bl,-ci,-dc,dc,dc,-bo,dc,-dc,dc,co,bo,-dc,dc,t,dc,-dc,-dc,-dc,dc,-dc,dc,x,-dc,-dc,dc,da,da,-t,dc,-dc,-c,-dc,dc,-dc,dc,-dc,-dc,dc,-dc,dc,-dc,-dc,dc,bw,-dc,dc,dc,-bk,ba,-dc,-dc,dc,-h,dc,-dc,dc,db,dc,by,cw,-dc,dc,cm,dc,-dc,-dc,cu,dc,dc,-dc,-dc,-dc,-dc,dc,-dc,-dc,cc,-dc,-dc,dc,-dc,-dc,-dc,bw,dc,-dc,dc,dc,dc,-dc,-b,-dc,dc,-k,-dc,dc,-dc,dc,r,-dc,-dc,-dc,-dc,da,cx,-k,dc,dc,dc,-dc", "ci", 6),
    "mup1": ("cp,dc,-ci,db,dc,-dc,dc,dc,dc,dc,-dc,dc,cj,-bw,-bs,ct,-cw,dc,a,dc,dc,cy,-da,-cs,-bv,-dc,-dc,dc,-db,-dc,-n,bp,-dc,dc,-bo,dc,cr,dc,-dc,dc,dc,-dc,-dc,-cw,-dc,m,-dc,-by,da,-dc,-dc,l,-ch,cq,dc,-dc,cy,-dc,cw,-cw,-cy,-db,-dc,-cz,dc,-cn,-cw,-cz,ck,da,dc,-cc,-da,bw,-bf,-dc,db,-cu,bj,-dc,-dc,-dc,cy,-dc,cv,-dc,dc,dc,dc,dc,-cz,dc,dc,-bp,-dc,cp,-h,dc,cv,-dc,dc,s,dc,db,db,cy,ck,-da,f,-dc,-dc,-cg,-db,da", "-do", 1),
    "mup2": ("dc,-bp,-m,-ci,dc,dc,-dc,dc,dc,dc,-dc,dc,dc,dc,bp,dc,-dc,dc,-cp,dc,dc,-dc,-dc,ch,-bp,-dc,-dc,dc,-dc,-dc,-ct,bu,-dc,bb,ci,-l,dc,-dc,-dc,dc,bb,dc,-dc,-cu,-bf,ct,-dc,cr,dc,-cw,-dc,-dc,j,n,-dc,-dc,dc,-dc,dc,-bm,-b,-dc,-dc,-dc,a,dc,cx,-dc,dc,-cw,dc,-dc,dc,cv,-cn,-dc,-dc,dc,-i,-dc,cw,-dc,dc,-dc,dc,-dc,dc,x,dc,dc,-dc,dc,dc,-bv,-f,dc,dc,dc,-cu,-dc,dc,dc,dc,dc,-dc,-cx,dc,dc,-cy,-dc,-cs,-dc,-dc,co", "-eh", 2),
    "mup3": ("cz,-cz,-cy,-dc,o,dc,c,dc,dc,by,-dc,dc,dc,-bx,-dc,dc,-p,bw,-cb,cu,-dc,-dc,-ct,-dc,u,-dc,-dc,-t,cl,-dc,-cb,cv,-dc,da,bd,-dc,dc,-cr,-dc,dc,dc,j,-dc,-cd,dc,-dc,-dc,dc,-t,-dc,-dc,dc,-dc,cn,dc,dc,cu,-i,-cy,da,-bf,dc,-v,-dc,-dc,b,-db,g,cj,bx,cb,dc,-dc,cy,-dc,-dc,db,e,-dc,-m,ch,bc,-br,-dc,-dc,-dc,-dc,dc,dc,dc,-cf,dc,dc,dc,-dc,-bj,dc,dc,-dc,-dc,-g,-cp,b,bu,-db,-dc,dc,-cz,cy,cq,cs,-ct,-dc,ci", "ox", 3),
    "mup6": ("dc,cu,-co,da,dc,dc,cy,-h,dc,dc,-dc,dc,dc,-bp,dc,-x,-bu,cq,m,cx,cz,cd,-dc,-dc,-bu,-dc,-dc,-ct,-dc,-dc,cp,ct,-dc,cx,-dc,cl,dc,o,-dc,cy,dc,-cg,-dc,-dc,bu,-r,-dc,-ck,bw,-dc,-dc,f,-da,-cv,cw,-dc,cl,co,cq,-cz,-cc,-cw,bo,-db,dc,-bl,-cz,-cz,db,cn,dc,-dc,-da,ca,-bv,-dc,dc,bf,-m,-dc,-dc,-dc,-dc,-dc,dc,-dc,dc,-ba,dc,bm,dc,dc,dc,-dc,-dc,cs,-u,cm,bx,-cn,dc,t,dc,db,dc,dc,dc,-cy,-bz,-da,-co,-cz,u,ct", "-cx", 6),
}
FAM = {
    "108": "k,fo,le,ws,wy,bld,bnv,cdy,coz,csc,cwz,cxw,cyj,dtj,dts,dut,dvf,dwl,dyq,eab,eac,eaf,edz,eeo",
    "110": "t,ez,gj,no,wk,wy,bck,bkp,ccu,cnf,cvp,cwz,czy,dsw,dto,dut,dwg,eab,eac,eaf,ecn,edz,eeg,eeo",
    "112": "c,fw,hs,xg,bkx,bmo,bnj,boq,bux,bvn,bxu,ccn,cdy,cek,cuw,cwj,cyr,dut,eab,eac,eaf,edz,eeg,eeo",
    "114": "db,do,ee,gu,hw,jz,nj,nv,op,oy,xs,bgb,bkc,bxl,bxx,cfv,cho,cjl,cjn,dcs,dea,dtd,dxl,eld",
    "116": "ba,eu,fm,hj,hu,im,ne,ww,xq,bho,big,blj,blz,brx,byk,cdx,cer,cjl,cjt,cjx,dul,dve,dzu,dzx",
    "118": "cl,dh,gd,jb,nu,po,rz,vm,wg,wv,yg,ze,zh,bik,clz,cmp,csh,dag,dwm,dyi,dzq,ejc,eje,ejl",
    "120": "bf,df,ez,kg,ni,ot,vg,wp,xa,yl,bcm,bdj,blj,bwl,ccn,ccw,cpy,dci,dri,drn,dui,dym,efk,efn",
    "122": "bz,et,ii,jr,nu,pg,qm,ts,baf,bhy,bsv,bvm,byb,bzq,ckq,dag,ddj,dgb,dnd,dwm,egy,elj,ell,elm",
    "124": "cv,fc,hf,jw,ng,oq,ps,uf,wm,bgy,bhs,bif,bij,bio,cck,cdu,cox,cpn,cze,dbu,dqr,egy,ell,elm",
    "126": "u,bt,fd,ie,pp,ps,wm,bbl,bhy,bkx,bpr,bpt,btx,bvm,cki,ckl,dag,dal,djp,dnd,egy,elg,elo,elr",
    "128": "cf,jm,kh,la,pf,sa,se,sv,xa,bcw,clq,cpm,des,djr,dkn,dlf,dlp,dqr,dqv,dtw,eeb,eef,eet,eew",
    "c128": "co,fl,ge,gg,jq,wm,bar,bbl,bus,bwa,bxd,cfe,cfg,chv,cia,cjj,cjr,dpr,egb,egy,ehw,elj,ell,elm",
    "c68": "cf,jq,rm,sh,vh,wm,bbe,bhy,djr,dkl,dmd,doc,dri,efl,eip,ejg",
    "cover": "bx,jz,wn,bhy,bic,bkw,ble,blf,bxt,bya,cje,cjf,cjj,dcu,dcv,dgc,djq,dri,dzd,eeu,efk,efl,ejg,elr",
    "ilp": "bz,en,jv,kq,nz,ou,qp,yl,zv,bak,bsr,bxx,cqp,dcg,ddj,ded,def,deg,dgd,dhn,dip,dpz,dtd,dzq",
    "max": "bb,fj,fz,hx,nf,nr,wn,yi,bap,bbd,bbf,bdl,bfu,bgc,bil,bio,bjw,blf,cjj,eax,ecb,ehf,ejc,ejl",
    "rand": "q,ds,bku,bss,bvv,bwv,bxw,bzx,cdl,cei,cjf,coe,dfy,dpc,drg,drz,dsz,dux,dvs,dxb,egd,ehz,eif,eii",
}
CE = {}
for k in sorted(CERT):
    CE[k] = (dec(CERT[k][0]), int(dec(CERT[k][1])[0]), CERT[k][2],
             k[0] == "f", k[:3] in ("mup", "fup") or k == "min128")


def slack(u, Z, D, full, up):
    if full:
        s = D * W - (BO @ u) - DT * Z
    else:
        s = D * WM - (BO[MIN] @ u) - Z
    return -s if up else s


def total(u, Z, D):
    return F(24 * (int(u.sum()) + Z), D)


sy = np.zeros(len(MIN), dtype=np.int64)
sy[dec(SPARSE[0])] = dec(SPARSE[1])
zs = int(dec(SPARSE[2])[0])
ss = WM - (INA[MIN] @ sy) - zs
gate("fixed-weight integer bound reaches the minimum",
     int(ss.min()) == 0 and int(sy.sum()) + 24 * zs == 108,
     "support {0}  tight {1}  total {2}".format(
         int((sy != 0).sum()), int((ss == 0).sum()), int(sy.sum()) + 24 * zs))

named = {}
for k in ("min108", "min128", "flo6"):
    u, Z, D, full, up = CE[k]
    s = slack(u, Z, D, full, up)
    named[k] = (int(s.min()), total(u, Z, D), int((u != 0).sum()), int((s == 0).sum()))
gate("invariant bound at halves reaches the minimum",
     named["min108"][0] == 0 and named["min108"][1] == 108,
     "orbits used {0}  tight {1}  total {2}".format(
         named["min108"][2], named["min108"][3], named["min108"][1]))
gate("invariant bound at thirds reaches the maximum",
     named["min128"][0] == 0 and named["min128"][1] == 128,
     "orbits used {0}  tight {1}  total {2}".format(
         named["min128"][2], named["min128"][3], named["min128"][1]))
gate("coarse-piece bound at sixths reaches its own floor",
     named["flo6"][0] == 0 and named["flo6"][1] == 68,
     "orbits used {0}  tight {1}  total {2}".format(
         named["flo6"][2], named["flo6"][3], named["flo6"][1]))

least = min(int(slack(*CE[k]).min()) for k in CE)
gate("every carried bound is valid", least == 0 and len(CE) == 18,
     "{0} invariant multiplier vectors plus the fixed-weight one, least slack {1}"
     .format(len(CE), least))


def predict(tgt, D, up):
    step = F(24, D)
    q = F(tgt) / step
    return (-((-q) // 1) if up else q // 1) * step


lad = {}
for tag, tgt, up in (("mlo", 108, False), ("mup", 128, True),
                     ("flo", 68, False), ("fup", 128, True)):
    got, want = [], []
    for D in (1, 2, 3, 6):
        u, Z, DD, full, uu = CE["{0}{1}".format(tag, D)]
        got.append(total(u, Z, DD))
        want.append(predict(tgt, D, up))
    lad[tag] = (got, got == want)
gate("denominator law on the minimal-piece bracket",
     lad["mlo"][1] and lad["mup"][1],
     "floor {0}  ceiling {1}".format(
         " ".join(str(x) for x in lad["mlo"][0]),
         " ".join(str(x) for x in lad["mup"][0])))
gate("denominator law on the all-piece bracket",
     lad["flo"][1] and lad["fup"][1],
     "floor {0}  ceiling {1}".format(
         " ".join(str(x) for x in lad["flo"][0]),
         " ".join(str(x) for x in lad["fup"][0])))

bump = []
for k in ("min108", "min128", "mlo6", "flo6", "fup6"):
    u, Z, D, full, up = CE[k]
    step = -1 if up else 1
    hit = 0
    for o in range(K):
        uu = u.copy()
        uu[o] += step
        if int(slack(uu, Z, D, full, up).min()) < 0:
            hit += 1
    bump.append(hit == K and int(slack(u, Z + step, D, full, up).min()) < 0)
gate("five representative bounds refuse strengthening", all(bump) and len(bump) == 5,
     "all 114 orbit bumps and the uniform bump refuted for the five tested "
     "certificates; the other fourteen carried certificates are untested here")


def cap(m, w):
    lim = {}
    for mv in sorted(set(m.tolist())):
        lim[mv] = int(w[m == mv].min())
    ms = sorted(lim)
    best = None
    for a, b in combinations(ms, 2):
        u = F(lim[a] - lim[b], a - b)
        z = F(lim[a]) - a * u
        if all(mv * u + z <= lim[mv] for mv in ms):
            v = 24 * (u + z)
            if best is None or v > best:
                best = v
    return best


one = max(cap(BO[MIN, o], WM) for o in range(K))
gate("no single carried orbit certifies the minimum",
     one == 84 and one < 108 and named["min108"][2] == 8,
     "best of the 114 carried orbits {0}, below 108; eight carried orbits reach it; "
     "other sample families untested".format(one))

FM = {k: dec(v) for k, v in FAM.items()}
DIR = np.array([d for d in product(range(-4, 5), repeat=4) if any(d)], dtype=np.int64)
use = sorted({int(i) for f in FM.values() for i in f})
upos = {c: i for i, c in enumerate(use)}
VU = V[use]
HI = np.zeros((len(use), len(DIR)), dtype=np.int64)
LO = np.zeros((len(use), len(DIR)), dtype=np.int64)
for a in range(0, len(DIR), 1024):
    b = min(a + 1024, len(DIR))
    PR = np.tensordot(DIR[a:b], VU, axes=([1], [2]))
    HI[:, a:b] = PR.max(axis=2).T
    LO[:, a:b] = PR.min(axis=2).T


def clash(f):
    q = [upos[int(i)] for i in f]
    bad = 0
    for a in range(len(q)):
        for b in range(a + 1, len(q)):
            if not bool((HI[q[a]] <= LO[q[b]]).any()):
                bad += 1
    return bad


REP = {}
for k in sorted(FM):
    f = FM[k]
    REP[k] = (int(W[f].sum()), int(DT[f].sum()), len(f), clash(f),
              bool((INA[f].sum(axis=0) == 1).all()),
              bool((INB[f].sum(axis=0) == 1).all()))
good = [k for k in REP if k != "cover"]
gate("carried families are genuine dissections",
     len(good) == 16 and all(REP[k][1] == 24 and REP[k][3] == 0 and REP[k][4]
                             and REP[k][5] for k in good),
     "{0} families, volumes sum to 24, no overlapping pair, covered once".format(len(good)))
gate("the covering control is rejected",
     REP["cover"][3] > 0 and not REP["cover"][4] and not REP["cover"][5]
     and REP["cover"][1] == 24,
     "cost {0} family: {1} overlapping pairs, points not covered once".format(
         REP["cover"][0], REP["cover"][3]))
even = [str(x) for x in range(108, 129, 2)]
gate("attained costs over the minimal pieces",
     all(k in REP and REP[k][0] == int(k) and REP[k][2] == 24 for k in even),
     " ".join(even))
prof = []
for k in ("108", "ilp", "rand"):
    c = {}
    for x in W[FM[k]].tolist():
        c[int(x)] = c.get(int(x), 0) + 1
    prof.append(tuple(sorted(c.items())))
gate("the minimum is not a property of one stencil",
     len({p for p in prof}) == 3 and all(REP[k][0] == 108 for k in ("108", "ilp", "rand")),
     "three unlike cost profiles all at 108: {0}".format(
         " ".join(str(dict(p)) for p in prof)))
cv = {}
for x in DT[FM["c68"]].tolist():
    cv[int(x)] = cv.get(int(x), 0) + 1
gate("a coarse dissection attains the lower bracket end",
     REP["c68"][0] == 68 and REP["c68"][2] == 16 and cv == {1: 8, 2: 8},
     "{0} pieces, volumes {1}, cost {2}".format(REP["c68"][2], cv, REP["c68"][0]))


def gf2(M, T):
    rows, cols = M.shape
    A = np.concatenate([M, T], axis=1).astype(np.uint8)
    r = 0
    for c in range(cols):
        nz = np.flatnonzero(A[r:, c])
        if not len(nz):
            continue
        p = r + int(nz[0])
        if p != r:
            A[[r, p]] = A[[p, r]]
        hit = np.flatnonzero(A[:, c])
        hit = hit[hit != r]
        if len(hit):
            A[hit] ^= A[r]
        r += 1
        if r == rows:
            break
    res = A[r:, cols:]
    return r, [bool(not res[:, j].any()) for j in range(T.shape[1])]


def targets(w):
    E = np.eye(len(w), dtype=np.int64)
    return np.stack([w & 1] + [(w ^ E[i]) & 1 for i in range(7)],
                    axis=1).astype(np.uint8)


par = {}
for tag, IM, rows, ext in (("a", INA[MIN], MIN, np.ones((len(MIN), 1), dtype=np.int64)),
                           ("b", INB[MIN], MIN, np.ones((len(MIN), 1), dtype=np.int64)),
                           ("c", INB, np.arange(n), DT[:, None])):
    M = (np.concatenate([IM.astype(np.int64), ext], axis=1) & 1).astype(np.uint8)
    par[tag] = gf2(M, targets(W[rows]))
gate("cost parity is forced over the minimal pieces",
     par["a"][0] == 465 and par["b"][0] == 465 and par["a"][1][0] and par["b"][1][0]
     and sum(par["a"][1][1:]) == 0 and sum(par["b"][1][1:]) == 0,
     "rank 465 on both families, cost reached, seven unit cuts refuted")
gate("the parity certificate stops at minimal pieces",
     par["c"][0] == 465 and not par["c"][1][0] and sum(par["c"][1][1:]) == 0,
     "rank 465, cost vector outside this certificate span; no odd coarse "
     "dissection exhibited or excluded")

# No-Go Discipline N5 execution certificate: one line per resolution class,
# stating honestly what this runner resolves at that granularity for the
# narrowed negative boundaries.  Classes not exercised say so explicitly.
for line in (
    "N5_RESOLUTION_CERTIFICATE (rhetoric-resolution sweep for the narrowed "
    "negative boundaries: single-carried-orbit cap, five-certificate "
    "strengthening refusals, coarse-parity certificate non-extension)",
    "per_element: every piece's normalized volume and adjacency cost, every "
    "certificate component's slack, every witness pair's separating direction, "
    "and every two-element-field elimination step is computed "
    "element-by-element in exact integer arithmetic; the only per-element "
    "negatives asserted are these recounted slacks and refusals",
    "per_site: the sample device resolves per point -- 2736 invariant points "
    "plus one fixed-weight point per minimal piece, zero boundary incidences "
    "against all 3008 pieces, cover-once checked point-by-point for every "
    "carried family; no negative is asserted about any sample configuration "
    "other than the two carried pinned recipes",
    "per_mode: the single-orbit cap is resolved orbit-by-orbit -- each of the "
    "114 carried point-orbits gets its own exact envelope optimum, best 84 -- "
    "and the strengthening refusals certificate-by-certificate for the five "
    "tested certificates (115 refusals each); the other fourteen carried "
    "certificates are checked and not executed for strengthening (declared "
    "open)",
    "per_block: the two piece classes resolve separately -- minimal-volume "
    "(2672 pieces: parity forced even, bracket 108 to 128) and all-corner "
    "(3008 pieces: bracket 68 to 128, parity-certificate non-membership only); "
    "the coarse block carries no dissection-parity negative: no odd-cost "
    "coarse dissection is exhibited or excluded",
    "lattice_wide: checked and not executed -- every statement is about one "
    "lattice cell carried through one tick inside the supplied corner-simplex "
    "model; no lattice-wide, multi-cell, multi-tick, or physical-construction "
    "negative is claimed anywhere in this package (the tick-Admissibility and "
    "simplex-identification bridges are open)",
):
    print(line, flush=True)

npass = sum(ok for _, ok in GATES)
nfail = len(GATES) - npass
RECEIPT = {
    "claim_type": "bounded_theorem",
    "headline": ("within the supplied tick-box corner-dissection model: minimal-piece "
                 "adjacency-cost bracket [108, 128], both ends attained, exactly the "
                 "eleven even values attained; all-piece bracket [68, 128]"),
    "supplied_model": ("corner 4-simplex pieces of one lattice cell carried through "
                       "one tick, all ten vertex pairs graded by spatial L1 "
                       "separation; the piece/dissection structure is supplied here, "
                       "not derived from the Lattice axiom"),
    "open_bridges": [
        "physical tick-Admissibility realization (which rule variation corresponds "
        "to which tick)",
        "identification of physical assembly cells with pairwise-adjacency simplices",
    ],
    "volume_normalization": ("normalized lattice 4-volume |det| = 24 x Euclidean; "
                             "whole box volume 24"),
    "adjacency_cost_range_minimal_pieces": [int(WM.min()), int(WM.max())],
    "adjacency_cost_range_all_pieces": [int(W.min()), int(W.max())],
    "attained_costs_minimal_pieces": [int(x) for x in even],
    "bracket_minimal_pieces": [int(named["min108"][1]), int(named["min128"][1])],
    "bracket_all_pieces": [int(named["flo6"][1]), int(lad["fup"][0][3])],
    "coarse_witness": {"cost": REP["c68"][0], "pieces": REP["c68"][2],
                       "volume_profile": {str(k): v for k, v in sorted(cv.items())}},
    "denominator_ladder": {
        "denominators": [1, 2, 3, 6],
        "minimal_pieces_floor": [int(x) for x in lad["mlo"][0]],
        "minimal_pieces_ceiling": [int(x) for x in lad["mup"][0]],
        "all_pieces_floor": [int(x) for x in lad["flo"][0]],
        "all_pieces_ceiling": [int(x) for x in lad["fup"][0]],
    },
    "minimal_pieces": int(len(MIN)),
    "nondegenerate_pieces": int(n),
    "orbit_count": int(K),
    "orbit_sizes": [int(x) for x in osz],
    "parity_rank": int(par["a"][0]),
    "rejected_control": {"cost": REP["cover"][0],
                         "overlapping_pairs": REP["cover"][3]},
    "sample_points": {
        "boundary_incidences_fixed_weight": int(faceA),
        "boundary_incidences_invariant": int(faceB),
        "invariant_points": int(len(PB)),
        "invariant_point_orbit_size": int(psz[0]),
        "points_per_piece_range": [int(cnt.min()), int(cnt.max())],
    },
    "single_orbit_cap_carried_family": int(one),
    "single_orbit_scope": ("the 114 point-orbits of the carried invariant sample "
                           "family only; other sample families untested"),
    "local_maximality_scope": ("five representative certificates only; the thirteen "
                               "other ladder rungs and the fixed-weight certificate "
                               "are untested"),
    "parity_scope": ("minimal-piece even parity is proved; over all pieces only THIS "
                     "incidence-plus-volume certificate family is shown not to "
                     "extend; no odd coarse dissection exhibited or excluded"),
    "tight_points": {
        "fixed_weight_floor": int((ss == 0).sum()),
        "invariant_floor": int(named["min108"][3]),
        "ceiling": int(named["min128"][3]),
        "all_pieces_floor": int(named["flo6"][3]),
    },
    "volume_spectrum": {str(k): int(v) for k, v in sorted(spec.items())},
    "gates": {name: ("PASS" if ok else "FAIL") for name, ok in GATES},
    "pass": npass,
    "fail": nfail,
    "no_go_discipline": {
        "status": "PASS",
        "no_go_shipped": False,
        "checklist": "committed N1-N8 record in the note's 'No-Go Discipline "
                     "Gate' section",
        "n5_certificate": "five resolution lines (per_element/per_site/per_mode/"
                          "per_block/lattice_wide) in this runner's stdout and "
                          "cached stdout",
    },
    "review_loop": [
        {
            "iteration": 1,
            "disposition": "FIX_THEN_PROCEED",
            "reviewer": "Sol",
            "date": "2026-08-08",
            "fix": "typed the note bounded_theorem of the supplied tick-box"
                   " dissection model; narrowed the single-orbit,"
                   " local-maximality, and coarse-parity claims to their computed"
                   " scopes; removed the false monotone-stencil witness"
                   " identification; declared the volume normalization; demoted"
                   " uncarried cross-checks to provenance; made the runner fail"
                   " closed and added its pinned cache",
        },
        {
            "iteration": 2,
            "disposition": "CONFIRMATION_FAIL_FIXED",
            "reviewer": "Sol (confirmation seat)",
            "date": "2026-08-08",
            "fix": "landed the mandatory No-Go Discipline artifacts for the"
                   " surviving narrowed negative boundaries: the committed N1-N8"
                   " gate record in the note and the five-line N5 resolution"
                   " certificate (per_element/per_site/per_mode/per_block/"
                   "lattice_wide) in the primary runner's cached stdout; no"
                   " no_go claim ships and every negative stays priced to its"
                   " carried objects",
        },
    ],
}
print("RECEIPT " + json.dumps(RECEIPT, sort_keys=True), flush=True)
print("TOTAL: PASS={0} FAIL={1}".format(npass, nfail), flush=True)
sys.exit(0 if nfail == 0 else 1)
