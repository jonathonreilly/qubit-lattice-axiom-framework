"""Independent z-space verification of a mod-2 covariant symbol + exact sign lift.
Input: pickle of Mz = [[fx,hx],[fz,hz]] (sets of z-exponents).
Checks (exact):
  (1) QCA/symplectic conditions on the cube box (cliff_enum.check)
  (2) mod-2 covariance: f fixed by D4_x generators; h = C3^2 f; C3-linearity
  (3) sign lift: alpha(X_0) := +prod sigma's; need C4x(aX)=aX, C2y(aX)=-aX exactly,
      and choose overall sign so that i*aX*aZ = aY with aY := C3(aX), aZ := C3^2(aX).
"""
import sys, pickle
import numpy as np
from grp import named
from pauli import P, rotate
from cliff_lin import box, Lmat
from cliff_enum import check

G = named()
Mz = pickle.load(open(sys.argv[1] if len(sys.argv) > 1 else "Mz_transport.pkl", "rb"))
fx, hx = Mz[0]; fz, hz = Mz[1]
r = max(max(abs(c) for c in v) for S in (fx, fz, hx, hz) for v in S)
pts = box("cube", r); idx = {v: i for i, v in enumerate(pts)}
n2 = 2 * len(pts)
f = np.zeros(n2, dtype=int); h = np.zeros(n2, dtype=int)
for v in fx: f[2 * idx[v]] = 1
for v in fz: f[2 * idx[v] + 1] = 1
for v in hx: h[2 * idx[v]] = 1
for v in hz: h[2 * idx[v] + 1] = 1
print("range r =", r)
ok1, ok2 = check(f, h, pts, r)
print("(1) [f,T_v f]=0 all v:", ok1, "  [f,T_v h] = delta_v0:", ok2)
L4 = Lmat(G["C4x"], pts, idx).astype(int); L2 = Lmat(G["C2y"], pts, idx).astype(int); L3 = Lmat(G["C3"], pts, idx).astype(int)
print("(2) C4x f=f:", np.array_equal(L4 @ f % 2, f), " C2y f=f:", np.array_equal(L2 @ f % 2, f),
      " C3^2 f = h:", np.array_equal(L3 @ (L3 @ f % 2) % 2, h),
      " f + C3f + C3^2f = 0:", not ((f + L3 @ f + L3 @ (L3 @ f % 2)) % 2).any())

# exact lift
def string_from_bits(vec):
    p = P()
    for i, v in enumerate(pts):
        b = (int(vec[2 * i]), int(vec[2 * i + 1]))
        if b == (1, 0): p = p * P.single(v, 0)
        elif b == (0, 1): p = p * P.single(v, 2)
        elif b == (1, 1): p = p * P.single(v, 1)
    return p
aX = string_from_bits(f)
assert aX.is_hermitian()
c4 = rotate(aX, G["C4x"]); c2 = rotate(aX, G["C2y"])
s4 = "+" if c4 == aX else ("-" if c4 == P(2) * aX else "?")
s2 = "+" if c2 == aX else ("-" if c2 == P(2) * aX else "?")
print(f"(3) C4x(aX) = {s4} aX (need +);  C2y(aX) = {s2} aX (need -)")
aY = rotate(aX, G["C3"]); aZ = rotate(aY, G["C3"])
lhs = P(1) * aX * aZ
rel = "+" if lhs == aY else ("-" if lhs == P(2) * aY else "?")
print(f"    i*aX*aZ = {rel} aY  -> overall sign of aX to choose: {'+' if rel == '+' else '-'}")
print("    C3^3(aX) == aX:", rotate(aZ, G["C3"]) == aX)
print("EXACT COVARIANT LIFT EXISTS:", s4 == "+" and s2 == "-" and rel in "+-")
