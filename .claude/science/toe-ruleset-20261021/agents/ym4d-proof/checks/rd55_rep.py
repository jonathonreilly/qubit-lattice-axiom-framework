# rd55_rep.py -- exact character arithmetic over H(4) = B_4 for ROTDEF.md (T56-R4).
# Criteria: checks/rd55_rep_criteria.md (written before this script). Plain python, integers/Fractions only.
from itertools import permutations, product
from fractions import Fraction

def perm_sign(p):
    s, seen = 1, [False]*len(p)
    for i in range(len(p)):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True; j = p[j]; L += 1
            if L % 2 == 0: s = -s
    return s

def mat(p, s):  # h e_i = s_i e_{p(i)}  -> column i has s_i at row p(i)
    M = [[0]*4 for _ in range(4)]
    for i in range(4): M[p[i]][i] = s[i]
    return tuple(tuple(r) for r in M)

def mul(X, Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(4)) for j in range(4)) for i in range(4))

def tr(X): return sum(X[i][i] for i in range(4))

G, dets = [], {}
for p in permutations(range(4)):
    for s in product((1, -1), repeat=4):
        M = mat(p, s); G.append(M)
        d = perm_sign(p)
        for x in s: d *= x
        dets[M] = d
Gset = set(G)
out = []
c1 = (len(Gset) == 384) and all(mul(X, Y) in Gset for X in G for Y in G)
out.append(f"C1 group order {len(Gset)}, closed={c1} -> {'PASS' if c1 else 'FAIL'}")

def chiV(h): return tr(h)
def chiA(h): return (tr(h)**2 - tr(mul(h, h)))//2
def chiS2A(h): h2 = mul(h, h); return (chiA(h)**2 + chiA(h2))//2
def chiL2A(h): h2 = mul(h, h); return (chiA(h)**2 - chiA(h2))//2
def chiSym2V(h): return (tr(h)**2 + tr(mul(h, h)))//2
def chidiag(h): return sum(1 for i in range(4) if h[i][i] != 0)
def chi6p(h): return chiSym2V(h) - chidiag(h)
def chitriv(h): return 1
def chidet(h): return dets[h]
def chiAdet(h): return chiA(h)*dets[h]
def chiAxA(h): return chiA(h)**2

def ip(f, g):
    v = Fraction(sum(f(h)*g(h) for h in G), 384)
    return v

I = mat((0, 1, 2, 3), (1, 1, 1, 1))
nV, nA = ip(chiV, chiV), ip(chiA, chiA)
c2 = (nV == 1 and nA == 1)
out.append(f"C2 <V,V>={nV} <A,A>={nA} -> {'PASS' if c2 else 'FAIL'}")
c3 = (chiS2A(I) == 21 and chiL2A(I) == 15)
out.append(f"C3 dim S2A={chiS2A(I)} dim L2A={chiL2A(I)} -> {'PASS' if c3 else 'FAIL'}")
mt, md = ip(chitriv, chiS2A), ip(chidet, chiS2A)
out.append(f"C4 m(triv in S2A)={mt} m(det in S2A)={md} -> R1 {'HOLDS' if mt == 1 else 'FAILS'}; det-count {'as expected' if md == 1 else 'UNEXPECTED'}")
mA, mAd = ip(chiA, chiS2A), ip(chiAdet, chiS2A)
mAL, mAAA = ip(chiA, chiL2A), ip(chiA, chiAxA)
c6 = (mAL >= 1 and mAAA == mA + mAL)
out.append(f"C6 control m(A in L2A)={mAL} m(A in AxA)={mAAA} (=m(A in S2A)+m(A in L2A)? {mAAA == mA + mAL}) -> {'PASS' if c6 else 'BROKEN'}")
if c6:
    out.append(f"C5 m(A in S2A)={mA} m(Axdet in S2A)={mAd} -> R2 {'HOLDS' if mA == 0 else 'FAILS'}")
else:
    out.append("C5 not evaluated: control C6 failed (script BROKEN)")
n6, x6A = ip(chi6p, chi6p), ip(chi6p, chiA)
c8 = (n6 == 1 and x6A == 0)
out.append(f"C8 <6',6'>={n6} <6',A>={x6A} -> {'PASS' if c8 else 'FAIL'}")
out.append(f"info <A,Axdet>={ip(chiA, chiAdet)} (A ~ A x det under H(4) iff 1)")

# full decomposition of S2A against a list of candidate irreps, remainder reported
cands = {'triv': chitriv, 'det': chidet, 'V': chiV, 'Vdet': lambda h: chiV(h)*dets[h], 'A': chiA, 'Adet': chiAdet,
         "3=diag-triv": lambda h: chidiag(h) - 1, "3det": lambda h: (chidiag(h) - 1)*dets[h],
         "6'": chi6p, "6'det": lambda h: chi6p(h)*dets[h]}
dec, rem = {}, {h: chiS2A(h) for h in G}
for k, f in cands.items():
    n = ip(f, f)
    if n == 1:
        m = ip(f, chiS2A)
        if m:
            dec[k] = m
            for h in G: rem[h] -= int(m)*f(h)
remdim = rem[I]; remnorm = Fraction(sum(rem[h]*rem[h] for h in G), 384)
out.append(f"info S2A decomposition over listed irreps: {dec}; remainder dim={remdim}, <rem,rem>={remnorm}")

# C7: plane-wave evaluation of the cubic dim-6 density vs an O(4) control (exact rationals)
def Fmn(k, e): return [[k[m]*e[n] - k[n]*e[m] for n in range(4)] for m in range(4)]
def Q(k, e):
    F = Fmn(k, e); k2 = sum(x*x for x in k); e2 = sum(x*x for x in e)
    cub = Fraction(sum(k[m]**2 * F[m][n]**2 for m in range(4) for n in range(4)), k2*k2*e2)
    inv = Fraction(sum(k2 * F[m][n]**2 for m in range(4) for n in range(4)), k2*k2*e2)
    return cub, inv
q1, q2 = Q((1, 0, 0, 0), (0, 0, 1, 0)), Q((1, 1, 0, 0), (0, 0, 1, 0))
c7 = (q1[0] != q2[0]) and (q1[1] == q2[1])
out.append(f"C7 Q_cub: {q1[0]} vs {q2[0]}; Q_inv: {q1[1]} vs {q2[1]} -> {'PASS' if c7 else 'FAIL'}")
print("\n".join(out))
