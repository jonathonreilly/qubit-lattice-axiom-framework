"""Exact analysis of the O-covariant spin-1/2 walk family with support |v|_inf <= 1.

General covariant form (after the common-phase reduction):
  W(k) = f(c) - i sum_a sin(k_a) h_a(c) sigma_a,   c_a = cos k_a
  f   = A + B e1 + C e2 + D e3      (e1,e2,e3 elementary symmetric in c)
  h_x = P + Q (c_y + c_z) + R c_y c_z, cyclic for h_y, h_z
Unitarity (real coefficients) <=> f^2 + sum_a (1 - c_a^2) h_a^2 == 1 identically.
Also verifies the general complex case: W W^dag = 1 coefficientwise with complex
A..R, via the extreme Fourier coefficients, using sympy on the trig polynomial.
"""
import sympy as sp

cx, cy, cz = sp.symbols('c_x c_y c_z', real=True)
A, B, C, D, P, Q, R = sp.symbols('A B C D P Q R', real=True)
e1 = cx + cy + cz
e2 = cx * cy + cy * cz + cz * cx
e3 = cx * cy * cz
f = A + B * e1 + C * e2 + D * e3
hx = P + Q * (cy + cz) + R * cy * cz
hy = P + Q * (cz + cx) + R * cz * cx
hz = P + Q * (cx + cy) + R * cx * cy
F = sp.expand(f ** 2 + (1 - cx ** 2) * hx ** 2 + (1 - cy ** 2) * hy ** 2 + (1 - cz ** 2) * hz ** 2 - 1)
eqs = list(set(sp.Poly(F, cx, cy, cz).coeffs()))
print(len(eqs), "coefficient equations")
sols = sp.solve(eqs, [A, B, C, D, P, Q, R], dict=True)
print("real solutions:")
for s in sols:
    print("  ", s)
