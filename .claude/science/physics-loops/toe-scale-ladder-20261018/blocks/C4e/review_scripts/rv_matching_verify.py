"""Phase C: reviewer's independent global verification of the range-2 monomial 3-magnon certificate.

Input: logs/matching_s-1.json (author's matching, dumped by rv_extract_matching.py: one source
orbit rep -> one witness image each). Everything else is reviewer code:
  * k<=2 rule from the reviewer's own U (single frozen, face glider, others static) -- this is W;
  * spectator (class D) images W(c\\z) u z (C4d Lemma S, dist > r = 2);
  * C3 images extended by T x Z^3 equivariance, with explicit stabiliser-consistency check;
then checks on ALL translation classes of 1-,2-,3-magnon configs with diameter <= 5:
  (a) pi is a radius-2 CA on the k<=3 sector: no window conflict (incl. empty window: pi(c) in N_2(c));
  (b) pi^{-1} is a radius-2 CA likewise (windows of the image);
  (c) injective on translation classes; every 3-class of diameter <= 4 is hit (surjectivity where
      3-magnon windows exist; diameter > 4 classes are all spectator classes);
  (d) T-equivariance (random samples).
"""
import os, json, itertools, time, random
import rv_core as C

HERE = os.path.dirname(os.path.abspath(__file__))
MJ = os.environ.get('MATCHING_JSON', 'matching_s-1.json')
SUF = os.environ.get('LOG_SUFFIX', '')
f = open(os.path.join(HERE, 'logs', 'matching_verify%s.txt' % SUF), 'w')
ck = C.Check(f)
t0 = time.time()
data = json.load(open(os.path.join(HERE, 'logs', MJ)))
ck(len(data) == 478, f"loaded {len(data)} matched source orbits")
O = (0, 0, 0)


def neg(a):
    return (-a[0], -a[1], -a[2])


def mdist(z, S):
    return min(C.cheb(z, y) for y in S)


def spectator(c):
    c = list(c)
    for z in c:
        rest = [y for y in c if y != z]
        if mdist(z, rest) > 2:
            return z
    return None


PAIR = {}


def W(pair):
    a, b = sorted(pair)
    rho = C.sub(b, a)
    if rho not in PAIR:
        PAIR[rho] = C.tr(C.U(frozenset([O, rho])), O)
    return C.tr(PAIR[rho], a)


Minv = {}
for M in C.T12:
    for N in C.T12:
        if all(C.apply(N, C.apply(M, e)) == e for e in C.E):
            Minv[M] = N


def keyframe(c):
    out = []
    for M in C.T12:
        r = C.act(M, c)
        t = min(r)
        out.append((tuple(sorted(C.sub(x, t) for x in r)), M, t))
    k = min(o[0] for o in out)
    return k, [(M, t) for (kk, M, t) in out if kk == k]


TABLE = {}
stab_ok = True
for e in data:
    src = frozenset(map(tuple, e['src']))
    img = frozenset(map(tuple, e['img']))
    k, frames = keyframe(src)
    ims = set()
    for M, t in frames:
        ims.add(frozenset(C.sub(x, t) for x in C.act(M, img)))
    if len(ims) != 1 or k in TABLE:
        stab_ok = False
    TABLE[k] = next(iter(ims))
ck(stab_ok and len(TABLE) == 478, f"C3 table: 478 distinct orbit keys, stabiliser-consistent images (Stab(src) fixes img) : {stab_ok}")


def pi(c):
    c = frozenset(c)
    if len(c) == 1:
        return c
    if len(c) == 2:
        return W(c)
    z = spectator(c)
    if z is not None:
        return W(c - {z}) | {z}
    k, frames = keyframe(c)
    M, t = frames[0]
    d = TABLE[k]
    return C.act(Minv[M], C.tr(d, t))


# enumerate translation classes (lexicographic-min element at origin), diameter <= 5
R = 5
vecs = [v for v in itertools.product(range(-R, R + 1), repeat=3) if v > O]
confs = [frozenset([O])] + [frozenset([O, v]) for v in vecs]
for i, a in enumerate(vecs):
    for b in vecs[i + 1:]:
        if C.cheb(a, b) <= R:
            confs.append(frozenset([O, a, b]))
ck.info(f"enumerated {len(confs)} classes (k=1..3, diam<=5) in {time.time()-t0:.0f}s")


def ball_inter(z, w):
    lo = [max(z[i], w[i]) - 2 for i in range(3)]
    hi = [min(z[i], w[i]) + 2 for i in range(3)]
    return itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)])


def check_local(c, d, table, tag):
    """d = image of c under a map claimed to be a radius-2 CA. Records windows of c."""
    # empty windows: d within N_2(c)
    for y in d:
        if mdist(y, c) > 2:
            return f"{tag}: site {y} of image outside N_2"
    cl = list(c)
    # single-magnon windows: value must equal the 1-magnon rule (x == z), sites in c u d
    for y in set(c) | set(d):
        near = [z for z in cl if C.cheb(z, y) <= 2]
        if len(near) == 1 and ((y in d) != (y in c)):
            return f"{tag}: single-window mismatch at {y}"
    # multi-magnon windows
    seen = set()
    for z, w in itertools.combinations(cl, 2):
        if C.cheb(z, w) > 4:
            continue
        for x in ball_inter(z, w):
            if x in seen:
                continue
            seen.add(x)
            win = tuple(sorted(C.sub(u, x) for u in cl if C.cheb(u, x) <= 2))
            val = x in d
            old = table.get(win)
            if old is None:
                table[win] = (val, c)
            elif old[0] != val:
                return f"{tag}: window conflict {win}: {sorted(c)} vs {sorted(old[1])}"
    return None


FT, GT = {}, {}
errF = []
errG = []
imgs = {}
inj_bad = 0
for c in confs:
    d = pi(c)
    if len(d) != len(c):
        errF.append(('N', sorted(c)))
        continue
    e = check_local(c, d, FT, 'F')
    if e:
        errF.append(e)
    e = check_local(d, c, GT, 'G')
    if e:
        errG.append(e)
    m = min(d)
    nd = frozenset(C.sub(x, m) for x in d)
    if nd in imgs:
        inj_bad += 1
    imgs[nd] = c
ck(not errF, f"(a) pi is radius-2 local on all {len(confs)} classes: {len(FT)} distinct multi-magnon windows, no conflict; errors {errF[:3]}")
ck(not errG, f"(b) pi^-1 is radius-2 local (image windows): {len(GT)} distinct windows, no conflict; errors {errG[:3]}")
ck(inj_bad == 0, f"(c) injective on translation classes (diam<=5): collisions {inj_bad}")
miss = []
n4 = 0
for c in confs:
    if len(c) == 3 and max(C.cheb(a, b) for a in c for b in c) <= 4:
        n4 += 1
        if c not in imgs:
            miss.append(sorted(c))
ck(not miss, f"(c) every one of the {n4} 3-magnon classes of diam<=4 has a preimage of diam<=5; missing {miss[:3]}")
rng = random.Random(3)
bad = 0
for _ in range(3000):
    c = rng.choice(confs)
    M = rng.choice(C.T12)
    if pi(C.act(M, c)) != C.act(M, pi(c)):
        bad += 1
ck(bad == 0, "(d) T-equivariance of the assembled pi on 3000 random classes")
ck.info(f"wall {time.time()-t0:.0f}s")
ck.total()
