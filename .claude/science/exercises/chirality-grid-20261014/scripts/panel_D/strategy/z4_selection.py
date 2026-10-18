"""Z4 selection rules for one SM generation + nu^c (all left-handed Weyl).
X = 5(B-L) - 4Y. Check X = 1 mod 4 on all 16 (so Z4^X = Spin(10) centre = uniform Z4^F
on fermions), then the X charge (mod 4) of operators. Exact rationals only."""
from fractions import Fraction as F
fields = {  # name: (multiplicity, B-L, Y)  left-handed Weyl
 'Q':  (6, F(1,3),  F(1,6)), 'u^c':(3, F(-1,3), F(-2,3)), 'd^c':(3, F(-1,3), F(1,3)),
 'L':  (2, F(-1),   F(-1,2)), 'e^c':(1, F(1),   F(1)),    'nu^c':(1, F(1),  F(0)),
 'H':  (0, F(0),    F(1,2)),  'Hc': (0, F(0),   F(-1,2)),
}
X = {k: 5*bl - 4*y for k,(m,bl,y) in fields.items()}
for k in fields: print(f"{k:5s} X = {X[k]!s:>4}  X mod 4 = {X[k] % 4}")
nW = sum(m for m,_,_ in fields.values()); print("Weyl count:", nW)
print("sum X^3 (U(1)_X cubic):", sum(m*X[k]**3 for k,(m,_,_) in fields.items()))
print("sum X (grav-mixed):", sum(m*X[k] for k,(m,_,_) in fields.items()))
print("uniform-F cubic anomaly (all charge 1):", nW)
ops = {
 'Yukawa Q u^c H':   ['Q','u^c','H'],
 'Yukawa Q d^c Hc':  ['Q','d^c','Hc'],
 'Yukawa L nu^c H':  ['L','nu^c','H'],
 'Majorana nu^c nu^c': ['nu^c','nu^c'],
 'Weinberg L L H H':   ['L','L','H','H'],
 'proton decay Q Q Q L': ['Q','Q','Q','L'],
 'proton decay u^c u^c d^c e^c': ['u^c','u^c','d^c','e^c'],
 'n-nbar (u^c d^c d^c)^2': ['u^c','d^c','d^c','u^c','d^c','d^c'],
}
for name, fs in ops.items():
    x = sum(X[f] for f in fs)
    print(f"{name:32s} X = {x!s:>4}  mod 4 = {x % 4}  -> {'allowed' if x % 4 == 0 else 'FORBIDDEN by Z4^X'}")
