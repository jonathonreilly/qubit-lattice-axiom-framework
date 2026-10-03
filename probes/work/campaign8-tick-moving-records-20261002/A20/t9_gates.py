"""(a) F_x = prod over 12 face-diagonal neighbours d of sigma^{perp(d)}_{x+d}: exact O-invariance (with sign),
    pairwise commuting.  (b) Heisenberg images of the Clifford circuits A=prod exp(-i pi/4 S_x),
    B=prod exp(-i pi/4 F_x) (gates commute -> order-free) computed EXACTLY with signs, compared mod 2 with the
    enumerated symbols A,B.  (c) Tick U = A then B (Heisenberg: alpha = Ad_A o Ad_B or reverse): exact covariance
    under all 24 rotations x 3 Paulis, and homomorphism alpha(Y)= i alpha(X) alpha(Z).
Heisenberg image under a commuting Clifford circuit prod_x exp(-i pi/4 G_x):  Q -> Q * prod_{x: {Q,G_x}=0} (i G_x)
(ordering inside the product irrelevant up to the exact sign bookkeeping, which we do by sequential application)."""
import itertools, pickle
import numpy as np
from grp import named, label_map
from pauli import P, rotate

O = named()["all"]
E = np.eye(3, dtype=int)


def site(v):
    return tuple(int(c) for c in v)


def star(x):
    p = P()
    for a in range(3):
        for s in (1, -1):
            p = p * P.single(site(np.add(x, s * E[a])), a)
    return p


def face(x):
    p = P()
    for a, b in itertools.combinations(range(3), 2):
        c = 3 - a - b
        for s, t in itertools.product((1, -1), repeat=2):
            p = p * P.single(site(np.add(x, s * E[a] + t * E[b])), c)
    return p


F0 = face((0, 0, 0)); S0 = star((0, 0, 0))
print("F_0 =", F0)
print("(a) F_0 exactly fixed by", sum(rotate(F0, R) == F0 for R in O), "/24 rotations; hermitian:", F0.is_hermitian())
bad = [d for d in itertools.product(range(-4, 5), repeat=3) if not F0.commutes(face(d))]
print("    offsets |d|_inf<=4 with [F_0,F_d]!=0:", bad)


def heis(Q, gate_of, centers):
    """exact: Ad of prod_x exp(-i pi/4 G_x)^dagger ... use Q -> exp(+i pi/4 G) Q exp(-i pi/4 G) = Q * (i G) if anticommute"""
    out = Q
    for x in centers:
        G = gate_of(x)
        if not out.commutes(G):
            out = out * P(1) * G      # Q (i G)
    return out


def centers_near(Q, rad):
    pts = set()
    for v in Q.s:
        for d in itertools.product(range(-rad, rad + 1), repeat=3):
            pts.add(site(np.add(v, d)))
    return sorted(pts)


def alphaA(Q):
    return heis(Q, star, centers_near(Q, 1))


def alphaB(Q):
    return heis(Q, face, centers_near(Q, 2))


def bits(p):
    return {v: b for v, b in p.s.items()}


def symbol_bits(Mz, which):
    fx, hx = Mz[0]; fz, hz = Mz[1]
    sx, sz = (fx, fz) if which == "X" else (hx, hz)
    out = {}
    for v in set(sx) | set(sz):
        out[v] = (1 if v in sx else 0, 1 if v in sz else 0)
    return out


A = pickle.load(open("Mz_A.pkl", "rb")); B = pickle.load(open("Mz_B.pkl", "rb"))
X0 = P.single((0, 0, 0), 0); Z0 = P.single((0, 0, 0), 2); Y0 = P.single((0, 0, 0), 1)
print("(b) star circuit image of X_0 matches symbol A mod 2:", bits(alphaA(X0)) == symbol_bits(A, "X"),
      "; of Z_0:", bits(alphaA(Z0)) == symbol_bits(A, "Z"))
print("    face circuit image of X_0 matches symbol B mod 2:", bits(alphaB(X0)) == symbol_bits(B, "X"),
      "; of Z_0:", bits(alphaB(Z0)) == symbol_bits(B, "Z"))

# (c) tick: first layer A then layer B in the Schrodinger picture -> Heisenberg alpha(Q) = Ad_A(Ad_B(Q))
def alpha(Q):
    return alphaA(alphaB(Q))


aX, aY, aZ = alpha(X0), alpha(Y0), alpha(Z0)
print("(c) alpha(Y_0) == i alpha(X_0) alpha(Z_0):", aY == P(1) * aX * aZ, "; hermitian:", aX.is_hermitian(), aZ.is_hermitian())
fails = 0
for R in O:
    pi, eps = label_map(R)
    for a, img in [(0, aX), (1, aY), (2, aZ)]:
        lhs = alpha(P.single((0, 0, 0), pi[a], eps[a]))   # alpha(R sigma^a_0)
        rhs = rotate(img, R)                             # R alpha(sigma^a_0)
        fails += (lhs != rhs)
print("    exact covariance failures over 24 rotations x 3 Paulis:", fails)
print("    support of alpha(X_0):", len(aX.s), "sites; max |v|_inf =", max(max(abs(c) for c in v) for v in aX.s))
