"""GUIDE check (exact, independent implementation) for gap-loop-eq-opus Section 4.

Criteria written before the run:
 K1: the 92-plaquette list S_0, built from the text of gap-means-max.md 2.4,
     has F=92, every link in exactly two plaquettes, is connected through
     links, has one cycle of plaquettes around every vertex, and chi = 1.
 K2: the exact Haar integral of prod_{p in S_0} (1/2) tr U_p, computed by
     the four SU(2) gluing rules, equals -2^(-183).
 K3: for a split S_0 = S1 + S2 into two nonempty parts, the Haar integrals
     of the two partial products are 0, so Cov_0 = -2^(-183) < 0.
FAIL at K1 means my reading of the description is wrong (not that S_0 is).
Pure Python, exact rationals; memory a few MB.
"""
from fractions import Fraction
import sys

def add(v, mu, k=1):
    w = list(v); w[mu] += k; return tuple(w)

def plaq(corner, mu, nu):
    if mu > nu: mu, nu = nu, mu
    return (tuple(corner), mu, nu)

def plaq_links(p):
    v, mu, nu = p
    return [((v, mu), +1), ((add(v, mu), nu), +1), ((add(v, nu), mu), -1), ((v, nu), -1)]

X, Y, Z, T = 0, 1, 2, 3
# boundary links of R = [0,3]x[0,2] in z=0, t=0
bdry = [((x, 0, 0, 0), X) for x in range(3)] + [((x, 2, 0, 0), X) for x in range(3)] \
     + [((0, y, 0, 0), Y) for y in range(2)] + [((3, y, 0, 0), Y) for y in range(2)]
b = ((1, 0, 0, 0), X)
M = []
for (v, d) in bdry:
    if (v, d) == b: continue
    M.append(plaq(v, d, Z)); M.append(plaq(add(v, Z, -1), d, Z))
M += [plaq((1, -1, 0, 0), X, Y), plaq((1, 0, 0, 0), X, Y)]
M += [plaq((1, -1, 0, 0), Y, Z), plaq((1, 0, -1, 0), Y, Z),
      plaq((2, -1, -1, 0), Y, Z), plaq((2, 0, 0, 0), Y, Z)]

def link_count(P):
    cnt = {}
    for p in P:
        for (l, s) in plaq_links(p):
            cnt[l] = cnt.get(l, 0) + 1
    return cnt

cM = link_count(M)
c = [l for l, k in cM.items() if k == 1]
A = [plaq(v, d, T) for (v, d) in c]
C = []
for (v, d) in bdry:
    v1 = add(v, T)
    C.append(plaq(add(v1, Z, 1), d, Z)); C.append(plaq(add(v1, Z, -2), d, Z))
for x in range(3):
    for y in range(2):
        C.append(plaq((x, y, 2, 1), X, Y)); C.append(plaq((x, y, -2, 1), X, Y))
for y0 in (-1, 0):
    for z0 in (-1, 0):
        C.append(plaq((2, y0, z0, 1), Y, Z))
C += [plaq((1, 1, -1, 1), X, Z), plaq((1, 0, -1, 1), X, Y),
      plaq((1, -1, 0, 1), X, Z), plaq((1, -1, 1, 1), X, Y)]

S0 = M + A + C
out = []
out.append("|M|=%d |c|=%d |A|=%d |C|=%d |S0|=%d distinct=%d" % (len(M), len(c), len(A), len(C), len(S0), len(set(S0))))
cnt = link_count(S0)
bad = [l for l, k in cnt.items() if k != 2]
out.append("links=%d, links not in exactly 2 plaquettes: %d" % (len(cnt), len(bad)))
verts = set()
for (v, mu) in cnt:
    verts.add(v); verts.add(add(v, mu))
F, E, V = len(set(S0)), len(cnt), len(verts)
out.append("F=%d E=%d V=%d chi=%d" % (F, E, V, V - E + F))
# connectivity through links
adj = {}
for i, p in enumerate(S0):
    for (l, s) in plaq_links(p):
        adj.setdefault(l, []).append(i)
seen = {0}; stack = [0]
while stack:
    i = stack.pop()
    for (l, s) in plaq_links(S0[i]):
        for j in adj[l]:
            if j not in seen: seen.add(j); stack.append(j)
out.append("connected: %s" % (len(seen) == len(S0)))
# one cycle of plaquettes around each vertex
def vstar_ok(v):
    ps = [i for i, p in enumerate(S0) if any(v in (l[0], add(l[0], l[1])) for (l, s) in plaq_links(p))]
    ls = set()
    g = {}
    for i in ps:
        for (l, s) in plaq_links(S0[i]):
            if v in (l[0], add(l[0], l[1])):
                g.setdefault(('p', i), []).append(('l', l)); g.setdefault(('l', l), []).append(('p', i))
    if any(len(nb) != 2 for nb in g.values()): return False
    start = next(iter(g)); seen = {start}; st = [start]
    while st:
        u = st.pop()
        for w in g[u]:
            if w not in seen: seen.add(w); st.append(w)
    return len(seen) == len(g)
out.append("one cycle around every vertex: %s" % all(vstar_ok(v) for v in verts))

# exact Haar evaluation by gluing
def inv(w): return [(l, -s) for (l, s) in reversed(w)]
def rot(w, k): return w[k:] + w[:k]

def haar(words):
    words = [list(w) for w in words]
    coef = Fraction(1)
    while True:
        occ = {}
        for wi, w in enumerate(words):
            for k, (l, s) in enumerate(w):
                occ.setdefault(l, []).append((wi, k))
        if not occ: break
        for l, o in occ.items():
            if len(o) == 1: return Fraction(0)
            if len(o) != 2: raise ValueError("link with multiplicity %d" % len(o))
        l = next(iter(occ)); (i1, k1), (i2, k2) = occ[l]
        if i1 != i2:
            w1 = rot(words[i1], k1 + 1)          # A l^s1, l last
            w2 = rot(words[i2], k2)              # l^s2 B, l first
            s1, s2 = w1[-1][1], w2[0][1]
            if s1 == s2:
                w2 = inv(w2); w2 = rot(w2, len(w2) - 1)   # l^{-s2} B^{-1}
            new = w1[:-1] + w2[1:]
            coef *= Fraction(1, 2)
            words = [w for j, w in enumerate(words) if j not in (i1, i2)] + [new]
        else:
            w = rot(words[i1], k1)               # l^s Aseg l^t Bseg
            j = k2 - k1 if k2 > k1 else k2 - k1 + len(w)
            s, t = w[0][1], w[j][1]
            Aseg, Bseg = w[1:j], w[j + 1:]
            rest = [ww for jj, ww in enumerate(words) if jj != i1]
            if s == -t:
                coef *= Fraction(1, 2); words = rest + [Aseg, Bseg]
            else:
                coef *= Fraction(-1, 2); words = rest + [Aseg + inv(Bseg)]
    return coef * Fraction(2) ** len(words)

words = [[(l, s) for (l, s) in plaq_links(p)] for p in S0]
val = haar(words) * Fraction(1, 2) ** len(S0)
out.append("Haar integral of prod x_p over S0 = %s ; equals -2^-183: %s" % ("-2^-%d" % (val.denominator.bit_length() - 1) if val < 0 else str(val), val == -Fraction(1, 2 ** 183)))
# controls: a plaquette-sphere (unit cube surface, chi=2): expect +2^(2-12) = 2^-10
cube = [plaq((0,0,0,0),X,Y), plaq((0,0,1,0),X,Y), plaq((0,0,0,0),X,Z), plaq((0,1,0,0),X,Z), plaq((0,0,0,0),Y,Z), plaq((1,0,0,0),Y,Z)]
cv = haar([plaq_links(p) for p in cube]) * Fraction(1, 2) ** 6
out.append("control, cube surface: %s (expect 1/1024)" % cv)
S1, S2 = M, A + C
v1 = haar([plaq_links(p) for p in S1]); v2 = haar([plaq_links(p) for p in S2])
out.append("K3 split M | A+C: E0[prod_M]=%s E0[prod_(A+C)]=%s ; Cov_0 = %s" % (v1, v2, "-2^-183" if (val - v1 * v2) == -Fraction(1, 2 ** 183) else val - v1 * v2))
print("\n".join(out))
