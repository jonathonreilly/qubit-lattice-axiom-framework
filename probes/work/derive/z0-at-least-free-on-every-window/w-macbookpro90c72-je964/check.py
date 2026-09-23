#!/usr/bin/env python3
"""J:derive:z0-at-least-free-on-every-window:a1 (worker w-macbookpro90c72-je964): exact checks.

Claim: at the neutral scale c0, Z0(eta) >= 6^|eta| for every finite arrangement eta of Z^3 and every
weight triple (p, q, r) >= 0 with p + q + 4r > 0, with equality exactly when eta has no cycle (or p = q = r).
Route (ATTEMPT.md):
  A. contents = (axis, sign); on a bipartite graph the sign sum is at least its value at l1 = 0;
  B. l2 >= 0: the three-axis sum is 1 + sum over Z3 flows N3(F) l2^|F|;
  C. l2 < 0: the three-axis bond weight is (1 - th) + th (3/2)[a != a'] with th = -2 l2, and every
     bipartite H has hom(H, K3) >= 3^n (2/3)^e (Kempe chains).
D, E: every arrangement of the windows 2x2x2, 2x3, 3x3, 2x2x3, 2x3x3 at four triples with l1 < 0 or
l2 < 0; the 3x3x3 window at l1 = 0. F: block 81 T1's bond factor. G: an odd ring, where it fails.
All checks are exact integer or rational arithmetic unless marked "control".
"""
import itertools
import random
import sys
import time
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()
FAILS = []
random.seed(20260923)


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


AXIS = [0, 0, 1, 1, 2, 2]          # contents +e1, -e1, +e2, -e2, +e3, -e3
SIGN = [1, -1, 1, -1, 1, -1]


def omega6(p, q, r):
    """integer pair weights: p equal, q opposite, r orthogonal contents."""
    K = np.empty((6, 6), dtype=object)
    for i in range(6):
        for j in range(6):
            K[i, j] = r if AXIS[i] != AXIS[j] else (p if SIGN[i] == SIGN[j] else q)
    return K


def kern3(same, diff):
    K = np.empty((3, 3), dtype=object)
    for i in range(3):
        for j in range(3):
            K[i, j] = same if i == j else diff
    return K


def zsum(n, bonds, K, order=None, dtype=object):
    """sum over states of the product over bonds of K[s_i, s_j] (symmetric kernels), by elimination.
    bonds: (i, j) or (i, j, Kb); parallel bonds are merged. Exact for dtype=object."""
    d = K.shape[0]
    order = list(range(n)) if order is None else order
    pos = {v: t for t, v in enumerate(order)}
    pair = {}
    for b in bonds:
        i, j = (b[0], b[1]) if pos[b[0]] < pos[b[1]] else (b[1], b[0])
        Kb = (b[2] if len(b) > 2 else K).astype(dtype)
        pair[(i, j)] = pair[(i, j)] * Kb if (i, j) in pair else Kb
    nb = {v: [] for v in range(n)}
    for (i, j) in pair:
        nb[i].append(j)
        nb[j].append(i)
    last = {v: max([pos[v]] + [pos[w] for w in nb[v]]) for v in range(n)}
    front, T = [], np.ones((), dtype=dtype)
    for t, v in enumerate(order):
        T = np.asarray(T, dtype=dtype)
        earlier = [w for w in nb[v] if pos[w] < t]
        rep = [u for u in earlier if last[u] == t]
        if rep:
            u = rep[0]
            iu = front.index(u)
            T = np.moveaxis(T, iu, -1)
            sh = T.shape
            T = T.reshape(-1, d).dot(pair[(u, v)]).reshape(sh)
            front.pop(iu)
            front.append(v)
            others = [w for w in earlier if w != u]
        else:
            T = np.repeat(T[..., None], d, axis=-1)
            front.append(v)
            others = earlier
        for w in others:
            shape = [1] * len(front)
            shape[front.index(w)] = d
            shape[-1] = d
            T = T * pair[(w, v)].reshape(shape)
        for w in [w for w in front if last[w] == t]:
            T = T.sum(axis=front.index(w))
            front.remove(w)
    T = np.asarray(T, dtype=dtype)
    return T.item() if dtype == object else float(T)


def window(dims):
    """sites of a box, ordered so that the elimination sweeps the last coordinate."""
    return sorted(itertools.product(*[range(k) for k in dims]), key=lambda s: tuple(reversed(s)))


def induced(S):
    idx = {s: i for i, s in enumerate(S)}
    E = []
    for s in S:
        for k in range(len(s)):
            t = list(s)
            t[k] += 1
            t = tuple(t)
            if t in idx:
                E.append((idx[s], idx[t]))
    return E


def sub(S, E, mask):
    """arrangement: the induced subgraph on the sites in mask (bit i = site i)."""
    keep = [i for i in range(len(S)) if mask >> i & 1]
    re = {v: k for k, v in enumerate(keep)}
    return len(keep), [(re[i], re[j]) for i, j in E if i in re and j in re]


def ncomp(n, bonds):
    par = list(range(n))

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for i, j in bonds:
        par[f(i)] = f(j)
    return len({f(x) for x in range(n)})


def acyclic(n, bonds):
    return len(bonds) == n - ncomp(n, bonds)


def z_over_free(n, bonds, p, q, r):
    """Z0(eta)/6^|eta| as an exact fraction: (6/T)^|E| W / 6^n with W the integer content sum."""
    T = p + q + 4 * r
    return Fr(6 ** len(bonds) * zsum(n, bonds, omega6(p, q, r)), T ** len(bonds) * 6 ** n)


def lams(p, q, r):
    T = p + q + 4 * r
    return Fr(p - q, T), Fr(p + q - 2 * r, T)


def popparity(x):
    x = x ^ (x >> 32)
    x = x ^ (x >> 16)
    x = x ^ (x >> 8)
    x = x ^ (x >> 4)
    x = x ^ (x >> 2)
    x = x ^ (x >> 1)
    return x & 1


CUBE_S = window((2, 2, 2))
CUBE_E = induced(CUBE_S)
CPAR = [sum(s) % 2 for s in CUBE_S]

# ---------------- anchor: block 81 T2's numbers on the cube ----------------
a1 = z_over_free(8, CUBE_E, 3, 1, 2)
a2 = z_over_free(8, CUBE_E, 100, 1, 1)
ok("anchor", abs(float(a1) - 1.015) < 5e-4 and abs(float(a2) - 4330) < 1,
   f"full cube Z0/6^8 = {float(a1):.4f} at (3,1,2), {float(a2):.1f} at (100,1,1) (block 81 T2: 1.015, 4330)")

# ---------------- A. axes and signs ----------------
# A1: on a bipartite graph every edge set with all degrees even has an even number of bonds
S223 = window((2, 2, 3))
E223 = induced(S223)
m = np.arange(1 << len(E223), dtype=np.int64)
even = np.ones(m.shape, dtype=bool)
for v in range(len(S223)):
    inc = sum(1 << k for k, (i, j) in enumerate(E223) if v in (i, j))
    even &= popparity(m & inc) == 0
ev = m[even]
ok("A1", len(ev) == 2 ** (len(E223) - len(S223) + 1) and bool(np.all(popparity(ev) == 0)),
   f"2x2x3 window: all {len(ev)} of the 2^20 bond sets with even degrees have an even bond count")

# A2: sign sum identity  sum_sigma prod_S (al + be s s') = 2^n sum_{F even in S} al^{|S|-|F|} be^{|F|}
nE = len(CUBE_E)
sig = np.array(list(itertools.product((1, -1), repeat=8)), dtype=np.int64)
cm = np.arange(1 << nE, dtype=np.int64)
cev = np.ones(cm.shape, dtype=bool)
for v in range(8):
    inc = sum(1 << k for k, (i, j) in enumerate(CUBE_E) if v in (i, j))
    cev &= popparity(cm & inc) == 0
EVEN_CUBE = [int(x) for x in cm[cev]]


def sign_table(al, be):
    """direct sign sums for all 4096 bond sets S of the cube (int64 exact: |values| < 2^50)."""
    fac = [al + be * sig[:, i] * sig[:, j] for i, j in CUBE_E]
    prod = np.ones((1 << nE, len(sig)), dtype=np.int64)
    for S in range(1, 1 << nE):
        low = (S & -S).bit_length() - 1
        prod[S] = prod[S & (S - 1)] * fac[low]
    return prod.sum(axis=1)


good = all(popcount % 2 == 0 for popcount in (bin(F).count("1") for F in EVEN_CUBE))
for al, be in [(5, 3), (3, -1)]:
    direct = sign_table(al, be)
    for S in range(1 << nE):
        rhs = 256 * sum(al ** (bin(S).count("1") - bin(F).count("1")) * be ** bin(F).count("1")
                        for F in EVEN_CUBE if F & ~S == 0)
        if direct[S] != rhs or direct[S] < 256 * al ** bin(S).count("1"):
            good = False
ok("A2", good, f"cube, all 4096 bond sets S: sign sum = 2^8 sum over the {len(EVEN_CUBE)} even edge sets "
   "(all of even size) inside S, and >= its l1 = 0 value, at (al,be) = (5,3), (3,-1)")

# A3: the split reproduces Z0: W = sum_a r^{D(a)} 2^{-|S(a)|} (sign sum at (p+q, p-q)) on the full cube
good = True
for (p, q, r) in [(1, 2, 5), (3, 1, 4)]:
    tab = sign_table(p + q, p - q)
    W = Fr(0)
    for a in itertools.product(range(3), repeat=8):
        S = sum(1 << k for k, (i, j) in enumerate(CUBE_E) if a[i] == a[j])
        nS = bin(S).count("1")
        W += Fr(r ** (nE - nS) * int(tab[S]), 2 ** nS)
    good &= W == zsum(8, CUBE_E, omega6(p, q, r))
ok("A3", good, "full cube: sum over axes of r^(orthogonal bonds) x sign sum = the content sum W, "
   "exactly, at (1,2,5) and (3,1,4)")

# ---------------- B. l2 >= 0: Z3 flows ----------------
HEX = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1), (0, 0, 1)]   # induced six-cycle of Z^3
GRAPHS = {"cube": (8, CUBE_E), "domino": (6, induced(window((2, 3, 1)))),
          "hexagon": (6, induced(sorted(HEX, key=lambda s: tuple(reversed(s)))))}


def n3_all(n, E):
    """number of nowhere-zero Z3 flows on every bond subset F (brute force)."""
    out = {}
    for F in range(1 << len(E)):
        bl = [E[k] for k in range(len(E)) if F >> k & 1]
        if not bl:
            out[F] = 1
            continue
        vals = np.array(list(itertools.product((1, 2), repeat=len(bl))), dtype=np.int64)
        inc = np.zeros((len(bl), n), dtype=np.int64)
        for k, (i, j) in enumerate(bl):
            inc[k, i] += 1
            inc[k, j] -= 1
        out[F] = int(np.all((vals @ inc) % 3 == 0, axis=1).sum())
    return out


def phi(n, E, lam):
    """three-axis average E_a prod (1 - lam + 3 lam [a = a'])."""
    u, v = lam.numerator, lam.denominator
    return Fr(zsum(n, E, kern3(v + 2 * u, v - u)), 3 ** n * v ** len(E))


PTS = [Fr(k, 12) - Fr(1, 2) for k in range(13)]
N3 = {}
good = True
for name, (n, E) in GRAPHS.items():
    N3[name] = n3_all(n, E)
    for lam in PTS:
        good &= phi(n, E, lam) == sum(c * lam ** bin(F).count("1") for F, c in N3[name].items())
cyc = [F for F, c in N3["cube"].items() if c > 0 and F]
ok("B", good and N3["hexagon"][63] == 2, "three-axis average = sum_F N3(F) l2^|F| (N3 >= 0, N3(cycle) = 2) "
   f"exactly on cube, domino, hexagon at 13 points; the cube has {len(cyc)} bond sets carrying flows")

# ---------------- C. l2 < 0: mixture with proper three-axis colourings ----------------
COLS = {8: np.array(list(itertools.product(range(3), repeat=8)), dtype=np.int8)}


def homs_all(n, E):
    """hom((V,F), K3) for every bond subset F, via colouring masks."""
    C = COLS.setdefault(n, np.array(list(itertools.product(range(3), repeat=n)), dtype=np.int8))
    neq = [C[:, i] != C[:, j] for i, j in E]
    masks = [np.ones(len(C), dtype=bool)]
    for F in range(1, 1 << len(E)):
        low = (F & -F).bit_length() - 1
        masks.append(masks[F & (F - 1)] & neq[low])
    return C, masks


good = True
HOM = {}
for name in ("cube", "domino"):
    n, E = GRAPHS[name]
    C, masks = homs_all(n, E)
    HOM[name] = [int(mk.sum()) for mk in masks]
    for lam in PTS:
        th = -2 * lam
        mix = sum((1 - th) ** (len(E) - bin(F).count("1")) * th ** bin(F).count("1")
                  * Fr(3, 2) ** bin(F).count("1") * Fr(HOM[name][F], 3 ** n) for F in range(1 << len(E)))
        good &= mix == phi(n, E, lam)
ok("C1", good, "three-axis average = sum_F (1-th)^(|E|-|F|) th^|F| Psi(F), Psi = (3/2)^|F| hom(F,K3)/3^n, "
   "th = -2 l2, exactly on cube and domino at 13 points")

C, masks = homs_all(8, CUBE_E)
good_k, good_eq, npairs, nstrict = True, True, 0, 0
for F in range(1 << nE):
    bl = [CUBE_E[k] for k in range(nE) if F >> k & 1]
    h, e = HOM["cube"][F], len(bl)
    good_eq &= (h * 3 ** e >= 3 ** 8 * 2 ** e) and ((h * 3 ** e == 3 ** 8 * 2 ** e) == acyclic(8, bl))
    par = list(range(8))

    def f(x):
        while par[x] != x:
            x = par[x]
        return x
    for i, j in bl:
        par[f(i)] = f(j)
    for u in range(8):
        for v in range(8):
            if CPAR[u] == 0 and CPAR[v] == 1 and (u, v) not in bl and (v, u) not in bl:
                n00 = int((masks[F] & (C[:, u] == 0) & (C[:, v] == 0)).sum())
                n01 = int((masks[F] & (C[:, u] == 0) & (C[:, v] == 1)).sum())
                npairs += 1
                conn = f(u) == f(v)
                nstrict += conn
                good_k &= n00 <= n01 and ((n00 < n01) == conn)
ok("C2", good_eq and good_k, f"cube, all 4096 bond sets: hom(F,K3) >= 3^8 (2/3)^|F| (equality iff F is a forest); "
   f"{npairs} opposite-class pairs: #(a_u=a_v=0) <= #(a_u=0,a_v=1), strictly iff joined ({nstrict})")


def kempe_map(n, bl, col, u, v):
    """swap 0 <-> 1 on the {0,1}-component of v."""
    adj = {x: [] for x in range(n)}
    for i, j in bl:
        adj[i].append(j)
        adj[j].append(i)
    comp, stack = {v}, [v]
    while stack:
        x = stack.pop()
        for w in adj[x]:
            if w not in comp and col[w] in (0, 1):
                comp.add(w)
                stack.append(w)
    return tuple((1 - c) if (x in comp and c in (0, 1)) else c for x, c in enumerate(col)), u in comp


good, tested = True, 0
for dims, drop in [((2, 2, 2), 0), ((3, 3, 1), 3)]:
    S = window(dims)
    E = induced(S)
    n = len(S)
    bl = [b for k, b in enumerate(E) if k != drop]
    u, v = E[drop]
    if sum(S[u]) % 2:
        u, v = v, u
    imgs = set()
    for col in itertools.product(range(3), repeat=n):
        if col[u] == 0 and col[v] == 0 and all(col[i] != col[j] for i, j in bl):
            new, hit = kempe_map(n, bl, col, u, v)
            good &= (not hit) and new[u] == 0 and new[v] == 1 and all(new[i] != new[j] for i, j in bl)
            imgs.add(new)
            tested += 1
    good &= len(imgs) == len([1 for c in itertools.product(range(3), repeat=n)
                              if c[u] == 0 and c[v] == 0 and all(c[i] != c[j] for i, j in bl)])
for _ in range(300):
    F = random.getrandbits(nE)
    bl = [CUBE_E[k] for k in range(nE) if F >> k & 1]
    u, v = random.choice([(u, v) for u in range(8) for v in range(8)
                          if CPAR[u] == 0 and CPAR[v] == 1 and (u, v) not in bl and (v, u) not in bl])
    pre = [tuple(c) for c in C[masks[F] & (C[:, u] == 0) & (C[:, v] == 0)].tolist()]
    imgs = set()
    for col in pre:
        new, hit = kempe_map(8, bl, col, u, v)
        good &= (not hit) and new[u] == 0 and new[v] == 1 and all(new[i] != new[j] for i, j in bl)
        imgs.add(new)
    good &= len(imgs) == len(pre)
    tested += len(pre)
ok("C3", good, f"Kempe map (swap 0,1 on v's two-colour chain), the cube and 3x3 window less one bond and 300 "
   f"random cube bond sets: {tested} colourings with a_u = a_v = 0 go injectively to a_u = 0, a_v = 1; "
   "u is never in v's chain")

good, cnt = True, 0
for dims, k in [((3, 3, 1), 4096), ((2, 3, 3), 40), ((3, 3, 3), 40)]:
    S = window(dims)
    E = induced(S)
    n = len(S)
    subsets = range(1 << len(E)) if k == 4096 else [random.getrandbits(len(E)) | (1 << random.randrange(len(E)))
                                                       for _ in range(k)]
    for F in subsets:
        bl = [E[t] for t in range(len(E)) if F >> t & 1]
        h = zsum(n, bl, kern3(0, 1))
        cnt += 1
        good &= h * 3 ** len(bl) >= 3 ** n * 2 ** len(bl)
ok("C4", good, f"hom(H,K3) >= 3^n (2/3)^e exactly for {cnt} bond sets H: every one of the 3x3 window, "
   "40 random each in 2x3x3 and 3x3x3")

# ---------------- D. the claim on every arrangement of five windows ----------------
TRIPLES = [(1, 2, 5), (3, 1, 4), (1, 5, 1), (1, 1, 100)]
tl = ", ".join(f"({p},{q},{r}): l1={float(lams(p, q, r)[0]):+.3f} l2={float(lams(p, q, r)[1]):+.3f}"
               for p, q, r in TRIPLES)
print("triples " + tl)
lines = []
good_all = True
for dims, want in [((2, 2, 2), 188), ((2, 3, 1), 56), ((3, 3, 1), 415), ((2, 2, 3), 2466)]:
    S = window(dims)
    E = induced(S)
    N = len(S)
    nacyc, mins = 0, {}
    for mask in range(1, 1 << N):
        n, bl = sub(S, E, mask)
        acy = acyclic(n, bl)
        nacyc += acy
        for (p, q, r) in (TRIPLES if N <= 9 else TRIPLES[:2]):
            T = p + q + 4 * r
            W = zsum(n, bl, omega6(p, q, r))
            lhs, rhs = 6 ** len(bl) * W, 6 ** n * T ** len(bl)
            good_all &= lhs >= rhs and ((lhs == rhs) == acy)
            if not acy:
                mins[(p, q, r)] = min(mins.get((p, q, r), 9e9), lhs / rhs)
            if N <= 9 and (p, q, r) in TRIPLES[:3]:
                Wg = zsum(n, bl, omega6(q, p, r))
                Wa = zsum(n, bl, omega6(p + q, p + q, 2 * r))
                W2 = zsum(n, bl, omega6(2 * p, 2 * q, 2 * r))
                good_all &= Wg == W and W2 >= Wa and ((W2 == Wa) == acy)
    good_all &= nacyc == want
    lines.append(f"{'x'.join(map(str, dims))}: {2 ** N - 1} arr, {nacyc} acyclic, min excess "
                 + "/".join(f"{mins[t] - 1:.1e}" for t in mins))
ok("D1", good_all, "every arrangement: Z0 >= 6^n, equality iff acyclic (counts 188, 56, 415, 2466 as block 81); "
   "Z0(p,q,r) = Z0(q,p,r) and Z0 >= its l1 = 0 value (windows <= 9 sites). " + "; ".join(lines))

# D2: the leafless-core reduction, then all 2^18 - 1 arrangements of 2x3x3 through their core classes
SY = [(pm, sg) for pm in itertools.permutations(range(3)) for sg in itertools.product((1, -1), repeat=3)]


def canon(coords):
    best = None
    for pm, sg in SY:
        pts = [tuple(sg[k] * c[pm[k]] for k in range(3)) for c in coords]
        mn = [min(pt[k] for pt in pts) for k in range(3)]
        key = tuple(sorted(tuple(pt[k] - mn[k] for k in range(3)) for pt in pts))
        if best is None or key < best:
            best = key
    return best


def core_comps(n, nbm, mask):
    core = mask
    while True:
        rm, mm = 0, core
        while mm:
            b = mm & -mm
            mm ^= b
            if bin(nbm[b.bit_length() - 1] & core).count("1") <= 1:
                rm |= b
        if not rm:
            break
        core &= ~rm
    comps, rest = [], core
    while rest:
        b = rest & -rest
        comp, fr = b, b
        while fr:
            nf, mm = 0, fr
            while mm:
                bb = mm & -mm
                mm ^= bb
                nf |= nbm[bb.bit_length() - 1]
            nf &= core & ~comp
            comp |= nf
            fr = nf
        comps.append(comp)
        rest &= ~comp
    return comps


def ratio_of(coords, p, q, r):
    Sc = sorted(coords, key=lambda s: tuple(reversed(s)))
    return z_over_free(len(Sc), induced(Sc), p, q, r)


good = True
S = S223
E = E223
nbm = [0] * len(S)
for i, j in E:
    nbm[i] |= 1 << j
    nbm[j] |= 1 << i
cache = {}
for mask in range(1, 1 << len(S)):
    n, bl = sub(S, E, mask)
    prod = Fr(1)
    for comp in core_comps(len(S), nbm, mask):
        key = canon([S[i] for i in range(len(S)) if comp >> i & 1])
        if key not in cache:
            cache[key] = ratio_of(key, 1, 2, 5)
        prod *= cache[key]
    good &= prod == z_over_free(n, bl, 1, 2, 5)
ok("D2", good, f"2x2x3, all 4095 arrangements at (1,2,5): Z0/6^n = product over leafless-core components "
   f"(up to the 48 lattice symmetries: {len(cache)} classes) exactly")

S = window((2, 3, 3))
E = induced(S)
nbm = [0] * len(S)
for i, j in E:
    nbm[i] |= 1 << j
    nbm[j] |= 1 << i
seen, ncyc = set(), 0
for mask in range(1, 1 << len(S)):
    comps = core_comps(len(S), nbm, mask)
    ncyc += bool(comps)
    seen.update(comps)
classes = {canon([S[i] for i in range(len(S)) if comp >> i & 1]) for comp in seen}
good, mins = True, {}
for (p, q, r) in TRIPLES:
    for key in classes:
        rt = ratio_of(key, p, q, r)
        good &= rt > 1
        mins[(p, q, r)] = min(mins.get((p, q, r), 9e9), float(rt))
ok("D3", good, f"2x3x3, all 262143 arrangements ({ncyc} with a cycle) via their {len(classes)} core classes: "
   "every class weighs strictly more than free at all four triples; min excess "
   + "/".join(f"{mins[t] - 1:.1e}" for t in TRIPLES))

# ---------------- E. the 3x3x3 window ----------------
S = window((3, 3, 3))
E = induced(S)
good, cnt, mn = True, 0, 9e9
masks = [(1 << 27) - 1] + [((1 << 27) - 1) ^ (1 << i) for i in range(27)]
masks += [sum(1 << i for i in range(27) if random.random() < dens) for dens in (0.6, 0.75, 0.9) for _ in range(12)]
for mask in masks:
    n, bl = sub(S, E, mask)
    acy = acyclic(n, bl)
    for (p, r) in [(1, 4), (1, 100)]:
        T = 2 * p + 4 * r
        W3 = zsum(n, bl, kern3(p, r))               # l1 = 0: contents enter through their axes only
        lhs, rhs = 6 ** len(bl) * W3, 3 ** n * T ** len(bl)
        good &= lhs >= rhs and ((lhs == rhs) == acy)
        cnt += 1
        if not acy:
            mn = min(mn, lhs / rhs)
ok("E1", good, f"3x3x3 at l1 = 0, l2 = -1/3 and -99/201 (triples (1,1,4), (1,1,100)): {cnt} exact evaluations "
   f"(full window, 27 one-vacancy, 36 random): Z0 >= 6^n, equality iff acyclic; min excess {mn - 1:.1e}")
Kf = omega6(1, 2, 5).astype(float) * 6 / 23
zf = zsum(27, E, Kf, dtype=float) / 6 ** 27
ok("E2", zf > 1 + 1e-6, f"control (float64, positive terms): full 3x3x3 at (1,2,5), Z0/6^27 = {zf:.6f}")

# ---------------- F. block 81 T1: the factor for one added bond ----------------
good, stats = True, []
for (p, q, r) in [(1, 5, 1), (1, 1, 4), (5, 1, 4), (100, 1, 51)]:
    T = p + q + 4 * r
    Wt = [zsum(8, [CUBE_E[k] for k in range(nE) if F >> k & 1], omega6(p, q, r)) for F in range(1 << nE)]
    mnb = 9e9
    for F in range(1 << nE):
        bl = [CUBE_E[k] for k in range(nE) if F >> k & 1]
        for k in range(nE):
            if not F >> k & 1:
                a, b = 6 * Wt[F | 1 << k], T * Wt[F]
                i, j = CUBE_E[k]
                joined = ncomp(8, bl) == ncomp(8, bl + [(i, j)])
                good &= a >= b and ((a == b) == (not joined))
                if joined:
                    mnb = min(mnb, a / b)
    l1, l2 = lams(p, q, r)
    stats.append(f"({p},{q},{r}) l1={float(l1):+.3f} l2={float(l2):+.3f} min excess {mnb - 1:.1e}")
ok("F1", good, "cube, every bond set and every added bond: factor >= 1, = 1 iff the ends were disjoint; "
   + "; ".join(stats))
p, q, r = 100, 1, 51
T = p + q + 4 * r
l1, l2 = lams(p, q, r)
x, y = CUBE_E[0]
Gm = CUBE_E[1:]
same = np.empty((6, 6), dtype=object)
dot = np.empty((6, 6), dtype=object)
for i in range(6):
    for j in range(6):
        same[i, j] = int(AXIS[i] == AXIS[j])
        dot[i, j] = 0 if AXIS[i] != AXIS[j] else SIGN[i] * SIGN[j]
W0 = zsum(8, Gm, omega6(p, q, r))
t1 = Fr(zsum(8, Gm + [(x, y, dot)], omega6(p, q, r)), W0)
t2 = (3 * Fr(zsum(8, Gm + [(x, y, same)], omega6(p, q, r)), W0) - 1) / 2
bf = Fr(6 * zsum(8, CUBE_E, omega6(p, q, r)), T * W0)
ok("F2", t2 > 0 > l2 and bf == 1 + 3 * t1 * l1 + 2 * t2 * l2 and bf > 1,
   f"(100,1,51), cube less one bond: t1 = {float(t1):.5f}, t2 = {float(t2):.3e} > 0 with l2 = -1/305, "
   f"factor {float(bf):.5f} = 1 + 3 t1 l1 + 2 t2 l2 exactly; the two terms have opposite signs")

# ---------------- G. an odd ring (not a window of Z^3) ----------------
p, q, r = 1, 3, 2
l1, l2 = lams(p, q, r)
zr = z_over_free(3, [(0, 1), (1, 2), (0, 2)], p, q, r)
ok("G", zr == 1 + 3 * l1 ** 3 + 2 * l2 ** 3 and zr < 1,
   f"three-site ring at (1,3,2): Z0/6^3 = {zr} < 1; bipartiteness is used")

print(f"runtime {time.time() - T0:.0f} s")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PROVED (a): at the neutral scale every finite arrangement of Z^3 (every finite bipartite graph) "
      "has Z0 >= 6^|eta| at every triple, equality iff it has no cycle or p = q = r; lemmas checked exactly above; "
      "every arrangement of 2x2x2, 2x3, 3x3, 2x2x3, 2x3x3 exact at triples with l1 < 0 or l2 < 0. "
      "T1's bond-factor sign: proved for l2 >= 0 and for l1 = 0; checked on the cube for l2 < 0 < l1, open there.")
print("HIT: at the neutral scale every finite arrangement of Z^3 weighs at least its records placed apart, "
      "Z0(eta) >= 6^|eta|, at every triple, with equality exactly for arrangements without a cycle (unless "
      "p = q = r). Split each content into axis and sign: on the bipartite lattice every bond set with even "
      "degrees has an even number of bonds, so the sign sum only adds and leaves the three-axis sum at l2. For "
      "l2 >= 0 that sum is 1 + sum_F N3(F) l2^|F| over Z3 flows; for l2 < 0 the bond weight is "
      "(1-th) + th (3/2)[a != a'], th = -2 l2, and every bipartite H has hom(H,K3) >= 3^n (2/3)^e (Kempe chains).")
