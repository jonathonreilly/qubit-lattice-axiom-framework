"""Independent check of the C6 note's A2 claims (reviewer code; nothing imported from the runner).
Corner graph on the L-torus, BKSF edge operators, bare loop strings, kappa, sigma, sector existence."""
import itertools, random, sys
L = int(sys.argv[1]) if len(sys.argv) > 1 else 3
random.seed(7)
DIRS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def neg(a): return tuple(-x for x in a)
def add(p, a): return tuple((p[i]+a[i]) % L for i in range(3))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
pairs = sorted({frozenset((a,b)) for a in DIRS for b in DIRS if dot(a,b)==0}, key=lambda s: sorted(s))
assert len(pairs) == 12
sites = list(itertools.product(range(L), repeat=3))
V = [(s, p) for s in sites for p in pairs]; vid = {v:i for i,v in enumerate(V)}
def P(a,b): return frozenset((a,b))
E = {}; elist = []
def addedge(u, w, kind):
    key = frozenset((u,w)); assert u != w
    if key not in E: E[key] = len(elist); elist.append((u, w, kind))
for s in sites:
    for p in pairs:
        a, b = tuple(p)
        # on-site: share one direction, other two perpendicular
        for q in pairs:
            if len(p & q) == 1:
                (x,) = tuple(p - q); (y,) = tuple(q - p)
                if dot(x,y) == 0: addedge(vid[(s,p)], vid[(s,q)], 'on')
        for d, o in ((a,b),(b,a)):
            addedge(vid[(s,p)], vid[(add(s,d), P(neg(d),o))], 'link')
nV, nE = len(V), len(elist)
deg = [0]*nV
for u,w,_ in elist: deg[u]+=1; deg[w]+=1
assert set(deg) == {6} and nE == 36*L**3, (set(deg), nE)
def eid(u,w): return E[frozenset((u,w))]
faces = []  # (type, vertex cycle)
for s in sites:
    for a in DIRS:
        perp = [b for b in DIRS if dot(a,b)==0]
        b1 = perp[0]; b2 = cross(a,b1)
        cyc = [P(a,b1), P(a,b2), P(a,neg(b1)), P(a,neg(b2))]
        faces.append(('square', [vid[(s,c)] for c in cyc]))
    for sx,sy,sz in itertools.product((1,-1),repeat=3):
        x,y,z = (sx,0,0),(0,sy,0),(0,0,sz)
        faces.append(('triangle', [vid[(s,P(x,y))], vid[(s,P(y,z))], vid[(s,P(z,x))]]))
    for i,j in ((0,1),(1,2),(0,2)):
        x = DIRS[2*i]; y = DIRS[2*j]
        cyc = [(s,P(x,y)), (add(s,x),P(neg(x),y)), (add(add(s,x),y),P(neg(x),neg(y))), (add(s,y),P(x,neg(y)))]
        faces.append(('plaquette', [vid[c] for c in cyc]))
    for i in range(3):
        a = DIRS[2*i]; t = add(s,a)
        perp = [b for b in DIRS if dot(a,b)==0]
        for b in perp:
            c = cross(a,b)  # b, c adjacent (perpendicular)
            cyc = [(s,P(a,b)), (t,P(neg(a),b)), (t,P(neg(a),c)), (s,P(a,c))]
            faces.append(('tube', [vid[x] for x in cyc]))
TYPES = ['square','triangle','plaquette','tube']
cnt = {k: sum(1 for t,_ in faces if t==k)//L**3 for k in TYPES}
assert cnt == {'square':6,'triangle':8,'plaquette':3,'tube':12}, cnt
fedges = [[eid(c[i], c[(i+1)%len(c)]) for i in range(len(c))] for _,c in faces]
fmask = [sum(1<<e for e in fe) for fe in fedges]
assert all(bin(m).count('1') == len(fe) for m,fe in zip(fmask,fedges))
nF = len(faces)
# --- GF(2) relations among faces (kernel of face->edge map) by elimination
def relations():
    piv = {}; rels = []
    for i,m in enumerate(fmask):
        x = m; tag = 1 << i
        while x:
            h = x.bit_length()-1
            if h in piv: x ^= piv[h][0]; tag ^= piv[h][1]
            else: piv[h] = (x, tag); break
        if not x: rels.append(tag)
    return rels, len(piv)
rels, rank = relations()
print(f"L={L}: V={nV} E={nE} F={nF} rank={rank} E-V+1-3={nE-nV+1-3} relations={len(rels)} (5L^3+2={5*L**3+2})")
assert rank == nE-nV+1-3
# --- Pauli: (phase k for i^k, x, z) as python ints; product X^x1 Z^z1 X^x2 Z^z2 = (-1)^{|z1&x2|} X^.. Z^..
def pmul(A, B):
    return ((A[0]+B[0]+2*(bin(A[2]&B[1]).count('1')%2)) % 4, A[1]^B[1], A[2]^B[2])
def std(A):  # phase relative to the bare tensor product (Y = i X Z => X Z = -i Y)
    return (A[0] - bin(A[1]&A[2]).count('1')) % 4
inc = [[] for _ in range(nV)]
for k,(u,w,_) in enumerate(elist): inc[u].append(k); inc[w].append(k)
def build(order):
    rk = [{e:r for r,e in enumerate(order[v])} for v in range(nV)]
    S = []
    for k,(u,w,_) in enumerate(elist):
        z = 0
        for v in (u,w):
            for l in order[v]:
                if rk[v][l] < rk[v][k]: z ^= 1 << l
        S.append((0, 1<<k, z))
    return S
def loopdata(S, label):
    kap = []; bare = []
    for (t,c), fe in zip(faces, fedges):
        A = (0,0,0); eps = 1
        for i,e in enumerate(fe):
            A = pmul(A, S[e]); j, k = c[i], c[(i+1)%len(c)]
            eps *= 1 if label[j] < label[k] else -1
        q = std(A)
        ph = (len(fe) + q) % 4
        assert ph in (0,2), "kappa not real"
        kap.append(eps * (1 if ph == 0 else -1))
        bare.append(((A[0]-q) % 4, A[1], A[2]))
    return kap, bare
def sigmas(bare):
    out = []
    for r in rels:
        A = (0,0,0)
        for i in range(nF):
            if (r>>i)&1: A = pmul(A, bare[i])
        assert A[1]==0 and A[2]==0
        assert A[0] in (0,2)
        out.append(1 if A[0]==0 else -1)
    return out
# --- independent sector test: does the group generated by signed Paulis contain -I?  (symplectic elimination with phases)
def contains_minus_I(gens):
    piv = {}
    for g in gens:
        A = g
        while True:
            v = (A[1] << nE) | A[2]
            if v == 0:
                if A[0] == 2: return True
                assert A[0] == 0; break
            h = v.bit_length()-1
            if h in piv: A = pmul(A, piv[h])
            else: piv[h] = A; break
    return False
def commute_all(bare):
    # spot check: bare loop strings commute
    for _ in range(300):
        a,b = random.randrange(nF), random.randrange(nF)
        A,B = bare[a],bare[b]
        if (bin(A[1]&B[2]).count('1') + bin(A[2]&B[1]).count('1')) % 2: return False
    return True
def conv(kind):
    if kind == 'canonical':
        return [sorted(inc[v]) for v in range(nV)], list(range(nV))
    order = [random.sample(inc[v], len(inc[v])) for v in range(nV)]
    lab = list(range(nV)); random.shuffle(lab)
    return order, lab
results = {}
uniform = lambda bitsq: [ -1 if bitsq[TYPES.index(t)] else 1 for t,_ in faces]
def gauge_flux(u):  # u: list of +-1 per edge -> F_C = prod u
    F = []
    for fe in fedges:
        x = 1
        for e in fe: x *= u[e]
        F.append(x)
    return F
def consistent(F):
    for r in rels:
        x = 1
        for i in range(nF):
            if (r>>i)&1: x *= F[i]
        if x != 1: return False
    return True
nconv = int(sys.argv[2]) if len(sys.argv) > 2 else 6
allok = True; nbad_list = []
for ci in range(nconv):
    kind = 'canonical' if ci == 0 else 'random'
    order, lab = conv(kind)
    S = build(order)
    kap, bare = loopdata(S, lab)
    assert commute_all(bare)
    sig = sigmas(bare)
    ident = all( (lambda r: __import__('math').prod(kap[i] for i in range(nF) if (r>>i)&1))(r) == s for r,s in zip(rels, sig))
    nbad = sum(1 for s in sig if s == -1)
    bare_plus = [((b[0]) % 4, b[1], b[2]) for b in bare]
    bare_cons = not contains_minus_I(bare_plus)
    # sectors: g_C = F_C kappa_C B_C
    def sector_exists(F):
        gens = [(((b[0] + (0 if F[i]*kap[i] == 1 else 2)) % 4), b[1], b[2]) for i,b in enumerate(bare)]
        return not contains_minus_I(gens)
    tests = []
    for name, bq in (('0000',(0,0,0,0)),('1011',(1,0,1,1)),('1111',(1,1,1,1)),('1010',(1,0,1,0)),('0100',(0,1,0,0)),('1000',(1,0,0,0)),('0010',(0,0,1,0))):
        F = uniform(bq); tests.append((name, consistent(F), sector_exists(F)))
    u = [random.choice((1,-1)) for _ in range(nE)]; F = gauge_flux(u)
    tests.append(('random gauge', consistent(F), sector_exists(F)))
    F2 = list(F); F2[random.randrange(nF)] *= -1
    tests.append(('random gauge, 1 face flipped', consistent(F2), sector_exists(F2)))
    F3 = [random.choice((1,-1)) for _ in range(nF)]
    tests.append(('random F', consistent(F3), sector_exists(F3)))
    ok = ident and all(c == e for _,c,e in tests) and (bare_cons == (nbad == 0))
    allok &= ok; nbad_list.append(nbad)
    print(f"conv {ci} ({kind}): identity prod kappa = sigma: {ident}; #basis rel with sigma=-1: {nbad}; all-bare-+1 consistent: {bare_cons}; "
          f"sector tests (name, consistent, exists): {[(n,c,e) for n,c,e in tests]}")
print("ALL OK" if allok else "MISMATCH", "nbad per convention:", nbad_list)
