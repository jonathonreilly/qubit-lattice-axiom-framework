"""Claim 3: Chamon excitation mobility via GF(2) linear algebra on open boxes, plus exact
non-membership certificates by restriction to the curves of V(I)."""
import numpy as np, itertools, sys, time
t0 = time.time()
E = {'x': (1, 0, 0), 'y': (0, 1, 0), 'z': (0, 0, 1)}
# generator at g: X at g+-ex, Y at g+-ey, Z at g+-ez.  A single-site X at p anticommutes with
# generators g with p-g in {+-ey,+-ez}; Z at p with p-g in {+-ex,+-ey}.
ANTI = {'X': [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)], 'Z': [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]}

class Box:
    def __init__(self, n):
        self.n = n; m = n + 1
        self.sidx = {p: i for i, p in enumerate(itertools.product(range(-m, m + 1), repeat=3))}
        ns = len(self.sidx); self.nw = (ns + 63) // 64
        rows = []
        for p in itertools.product(range(-n, n + 1), repeat=3):
            for lab in 'XZ':
                v = np.zeros(self.nw, np.uint64)
                for d in ANTI[lab]:
                    g = (p[0] - d[0], p[1] - d[1], p[2] - d[2]); i = self.sidx[g]
                    v[i >> 6] ^= np.uint64(1) << np.uint64(i & 63)
                rows.append(v)
        A = np.array(rows)
        # row echelon (pivot = lowest set bit index chosen per column order)
        piv = {}
        r = 0
        for col in range(ns):
            w, b = col >> 6, np.uint64(1) << np.uint64(col & 63)
            hits = np.nonzero(A[r:, w] & b)[0]
            if len(hits) == 0: continue
            k = r + hits[0]
            A[[r, k]] = A[[k, r]]
            rest = np.nonzero(A[:, w] & b)[0]; rest = rest[rest != r]
            A[rest] ^= A[r]
            piv[col] = r; r += 1
        self.A = A[:r]; self.piv = piv; self.rank = r

    def contains(self, mons):
        """is the syndrome pattern (set of monomials, each a defect) in the image?"""
        v = np.zeros(self.nw, np.uint64)
        for p in mons:
            if p not in self.sidx: return None
            i = self.sidx[p]; v[i >> 6] ^= np.uint64(1) << np.uint64(i & 63)
        # fully reduced echelon -> just XOR pivot rows
        for col, r in self.piv.items():
            if (v[col >> 6] >> np.uint64(col & 63)) & np.uint64(1): v ^= self.A[r]
        return not v.any()

def mul(f, g):
    out = {}
    for a in f:
        for b in g:
            c = (a[0] + b[0], a[1] + b[1], a[2] + b[2]); out[c] = out.get(c, 0) ^ 1
    return {c for c, v in out.items() if v}

def move(f, t): return mul(f, {(0, 0, 0), t})

# exact non-membership: restrict to the 4 curves x=a, y=a^s2, z=a^s3 of V(I)
CURVES = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
def restrictions(f):
    res = []
    for s2, s3 in CURVES:
        cnt = {}
        for a, b, c in f:
            e = a + s2 * b + s3 * c; cnt[e] = cnt.get(e, 0) ^ 1
        res.append(any(cnt.values()))
    return res  # True = nonzero on that curve => f not in I

fracton = {(0, 0, 0)}
lineon = {(0, 0, 0), (1, 1, 0)}                     # 1+xy
planon = mul({(0, 1, 0), (0, 0, 1)}, lineon)       # (y+z)(1+xy)
tests = []
for t in [(1, 0, 0), (0, 0, 1), (1, 1, 0), (1, -1, 0), (1, 1, 1), (1, 1, -1), (2, 0, 0), (2, 2, 0), (1, 0, 1), (0, 1, 1)]:
    tests.append(('fracton', t, move(fracton, t)))
for t in [(1, -1, 0), (2, -2, 0), (1, 0, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (1, 1, -1)]:
    tests.append(('lineon 1+xy', t, move(lineon, t)))
for t in [(1, 0, 1), (0, 1, 1), (1, -1, 0), (1, 2, 3), (1, 1, 1), (1, 0, 0), (0, 0, 1), (1, 0, -1), (1, -1, 1)]:
    tests.append(('planon (y+z)(1+xy)', t, move(planon, t)))
tests += [('create fracton', None, fracton), ('create lineon', None, lineon), ('create planon', None, planon)]

print('curve restrictions (nonzero on curves [x=y=z, x=y=1/z, x=1/y=1/z, x=1/y=z]):')
print('  fracton', restrictions(fracton), ' lineon', restrictions(lineon), ' planon', restrictions(planon))
sizes = [int(a) for a in sys.argv[1:]] or [3, 5, 7, 9]
boxes = {}
for n in sizes:
    tb = time.time(); boxes[n] = Box(n); print(f'box [-{n},{n}]^3 rank {boxes[n].rank}  built {time.time()-tb:.1f}s', flush=True)
for name, t, pat in tests:
    exact_not = any(restrictions(pat))
    res = [boxes[n].contains(pat) for n in sizes]
    print(f'{name:22s} t={t}: in image per box {res}; exact curve-certificate NOT in I: {exact_not}')
    if exact_not: assert not any(r for r in res if r)
print('time %.1fs' % (time.time() - t0))
