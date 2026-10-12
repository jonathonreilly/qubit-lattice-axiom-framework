"""R6-2 check 1: the Weinberg-Witten little-group phase argument with only a discrete symmetry.

WW (1980): for null p, p' with p != p', a rotation R_theta fixing both (in their CM frame) acts on
<p',h|T^{mu nu}(0)|p,h> by the phase e^{2 i h theta}, while on symmetric rank-2 tensors it has
eigenvalues e^{i m theta}, |m| <= 2.  With continuous theta this kills the |h| >= 3/2 ... |h|>1 elements.

With a DISCRETE stabilizer C_n (theta = 2 pi / n) the element is forced to vanish only if
2h mod n is not congruent to any m in {-2..2} mod n.

(1) Table of which (h, n) give a constraint.
(2) For the LRL form Q = 7 n0^2 - n1^2 - n2^2 - n3^2 on Z^4:
    - no integer null vector (anisotropic over Q) -- brute-force check |n_i| <= 60;
    - explicit elements of Gamma_L = SO+(Q, Z) that fix a pair of distinct real null vectors:
      C4 (rotation in the n2-n3 plane) fixing (1/sqrt7, +-1, 0, 0)-direction pair;
      C3 (cyclic permutation n1->n2->n3) fixing the pair in span(e0, (0,1,1,1)).
    - Any finite-order element fixing two independent null vectors fixes a rational Lorentzian
      2-plane P pointwise and acts on the definite rational 2-plane P-perp lattice, so its order
      is in {1,2,3,4,6} (2D crystallographic restriction).  Loxodromic elements rescale null
      vectors (eigenvalues lambda, 1/lambda != 1) and parabolic elements fix one null direction only.
"""
from fractions import Fraction
import itertools
import numpy as np

print("(1) WW little-group phase constraint with C_n stabilizer: 'X' = matrix element forced to 0")
hs = [Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2), Fraction(3)]
print("   n | " + " ".join(f"h={str(h):>4}" for h in hs))
for n in range(1, 13):
    row = []
    for h in hs:
        twoh = int(2 * h)
        allowed = any((twoh - m) % n == 0 for m in range(-2, 3))
        row.append("   ." if allowed else "   X")
    print(f"  {n:2d} | " + "  ".join(row))
print("   continuous SO(2): forced to 0 iff 2|h| > 2, i.e. |h| > 1  (WW for T^{mu nu})")
print("   crystallographic orders {1,2,3,4,6}: h=2 is NEVER constrained (row entries '.').")

Q = np.diag([7, -1, -1, -1])

# anisotropy brute force
found = []
N = 60
for n0 in range(1, 25):
    t = 7 * n0 * n0
    for n1 in range(0, N + 1):
        r1 = t - n1 * n1
        if r1 < 0:
            break
        for n2 in range(0, n1 + 1):
            r2 = r1 - n2 * n2
            if r2 < 0:
                break
            n3 = int(round(np.sqrt(r2)))
            if n3 <= n2 and n3 * n3 == r2:
                found.append((n0, n1, n2, n3))
print(f"\n(2a) integer null vectors of Q with 1<=n0<=24: {len(found)} found (expected 0: 7 n0^2 is never a sum of 3 squares)")

def in_gamma(M):
    M = np.array(M)
    ok_int = np.all(M == np.round(M))
    ok_Q = np.array_equal(M.T @ Q @ M, Q)
    ok_det = round(np.linalg.det(M)) == 1
    ok_orth = M[0, 0] > 0  # time orientation (Q(e0)>0)
    return ok_int and ok_Q and ok_det and ok_orth

C4 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]]
C3 = [[1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0]]
for name, M, pair in [
    ("C4 (n2-n3 rotation)", C4, [np.array([1, np.sqrt(7), 0, 0]), np.array([1, -np.sqrt(7), 0, 0])]),
    ("C3 (n1->n2->n3)", C3, [np.array([1, a, a, a]) for a in (np.sqrt(7 / 3), -np.sqrt(7 / 3))]),
]:
    M = np.array(M, dtype=float)
    order = next(k for k in range(1, 13) if np.allclose(np.linalg.matrix_power(M, k), np.eye(4)))
    fix = [np.allclose(M @ p, p) for p in pair]
    nulls = [abs(p @ Q @ p) < 1e-9 for p in pair]
    print(f"(2b) {name}: in SO+(Q,Z)={in_gamma(M)}, order={order}, fixes pair={fix}, pair null={nulls}")

# Count finite-order elements of a small word ball? Instead: verify crystallographic restriction
# numerically for all integer 2x2 matrices preserving a definite binary form a x^2 + b xy + c y^2
orders = set()
for a, b, c in itertools.product(range(1, 6), range(-5, 6), range(1, 6)):
    if b * b - 4 * a * c >= 0:
        continue
    F = np.array([[2 * a, b], [b, 2 * c]])
    for e in itertools.product(range(-3, 4), repeat=4):
        M = np.array(e).reshape(2, 2)
        if round(np.linalg.det(M)) != 1:
            continue
        if np.array_equal(M.T @ F @ M, F):
            k = next((k for k in range(1, 13) if np.array_equal(np.linalg.matrix_power(M, k), np.eye(2, dtype=int))), None)
            orders.add(k)
print(f"(2c) orders of SO(definite binary integral form) elements found (a,c<=5,|b|<=5): {sorted(o for o in orders if o)}")
print("     => a Gamma_L element fixing two distinct null vectors has order in {1,2,3,4,6}; none constrains h=2.")
