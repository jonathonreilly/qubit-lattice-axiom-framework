# dc55_2: gauge-action composition laws and cocycle orders (exact rational arithmetic; criteria in dc55_2_criteria.md)
from fractions import Fraction as F
import random

def mul(A, B):
    return ((A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]),
            (A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]))

def inv(A):
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    assert det != 0
    return ((A[1][1]/det, -A[0][1]/det), (-A[1][0]/det, A[0][0]/det))

def rnd(rng):
    while True:
        A = ((F(rng.randint(-5, 5), rng.randint(1, 4)), F(rng.randint(-5, 5), rng.randint(1, 4))),
             (F(rng.randint(-5, 5), rng.randint(1, 4)), F(rng.randint(-5, 5), rng.randint(1, 4))))
        if A[0][0]*A[1][1] - A[0][1]*A[1][0] != 0:
            return A

# a gauge on one link = pair (g_minus, g_plus); pointwise product
def gprod(g2, g1):  # (g2 g1)(x) = g2(x) g1(x)
    return (mul(g2[0], g1[0]), mul(g2[1], g1[1]))

def left(U, g):   # U^g = g(b-) U g(b+)^{-1}
    return mul(mul(g[0], U), inv(g[1]))

def right(U, g):  # U^g = g(b-)^{-1} U g(b+)
    return mul(mul(inv(g[0]), U), g[1])

rng = random.Random(20261029)
inst = []
for _ in range(25):
    inst.append((rnd(rng), (rnd(rng), rnd(rng)), (rnd(rng), rnd(rng))))
# hand-chosen non-commuting pair
a = ((F(1), F(1)), (F(0), F(1))); b = ((F(1), F(0)), (F(1), F(1)))
inst.append((((F(2), F(1)), (F(1), F(1))), (a, b), (b, a)))

L_ok = all(left(left(U, g), gp) == left(U, gprod(gp, g)) for U, g, gp in inst)
R_ok = all(right(right(U, g), gp) == right(U, gprod(g, gp)) for U, g, gp in inst)
K1 = any(left(left(U, g), gp) != left(U, gprod(g, gp)) for U, g, gp in inst)   # wrong law for left must fail somewhere
K2 = any(right(right(U, g), gp) != right(U, gprod(gp, g)) for U, g, gp in inst) # wrong law for right must fail somewhere

# cocycle models (AMENDMENT 1)
M = ((F(1), F(2)), (F(3), F(5)))
def X(V):
    return mul(mul(V, M), V)
def cL(h, V):   # X(hV) X(V)^{-1}
    return mul(X(mul(h, V)), inv(X(V)))
def cR(h, V):   # X(V)^{-1} X(Vh)
    return mul(inv(X(V)), X(mul(V, h)))

coc = []
for _ in range(25):
    coc.append((rnd(rng), rnd(rng), rnd(rng)))
coc.append((((F(2), F(1)), (F(1), F(1))), a, b))
CL_ok = all(cL(mul(h2, h1), V) == mul(cL(h2, mul(h1, V)), cL(h1, V)) for V, h1, h2 in coc)
K3a = any(cL(mul(h1, h2), V) != mul(cL(h1, V), cL(h2, mul(h1, V))) for V, h1, h2 in coc)
CR_ok = all(cR(mul(h1, h2), V) == mul(cR(h1, V), cR(h2, mul(V, h1))) for V, h1, h2 in coc)
K3b = any(cR(mul(h2, h1), V) != mul(cR(h2, mul(V, h1)), cR(h1, V)) for V, h1, h2 in coc)

print("instances:", len(inst), "cocycle instances:", len(coc))
print("(L) left action (U^g)^{g'} = U^{g'g} on all instances:", L_ok)
print("(R) right action (U^g)^{g'} = U^{gg'} on all instances:", R_ok)
print("K1 wrong law for left fails somewhere (control fires):", K1)
print("K2 wrong law for right fails somewhere (control fires):", K2)
print("cocycle left order c(h2h1,V)=c(h2,V^h1)c(h1,V) on all:", CL_ok)
print("K3a right order applied to left model fails somewhere (control fires):", K3a)
print("cocycle right order c(h1h2,V)=c(h1,V)c(h2,V^h1) on all:", CR_ok)
print("K3b left order applied to right model fails somewhere (control fires):", K3b)
verdict = L_ok and R_ok and CL_ok and CR_ok and K1 and K2 and K3a and K3b
print("VERDICT:", "PASS" if verdict else "FAIL")
