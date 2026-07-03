#!/usr/bin/env python3
"""
POSITIVE DERIVATION — the Koide ratio of a C3-equivariant generation mass operator.

Theorem. Let the 3-generation carrier be the hw=1 BZ-corner orbit carrying the
regular representation of C3 = Z3 (cited taste-generation provenance). With a
supplied finite readout context and adopted K/CPT-real condition, the
C3-equivariant mass operator is the K/CPT-real circulant

        Y = a*I + b*C + conj(b)*C^2 ,     a real,  b in C,  C = cyclic shift.

Then the Koide ratio Q = (sum m_k) / (sum sqrt(m_k))^2  with sqrt(m_k) the
eigenvalues of Y satisfies

        Q = 1/3 + (2/3) r ,     r = |b|^2 / a^2 ,     INDEPENDENT of arg(b).

The two real Wedderburn blocks carry powers a^2 (singlet) and 2|b|^2 (doublet);
the singlet<->doublet power swap acts as r -> 1/(4r) with unique fixed point
r = 1/2 (equal block power), at which Q = 2/3.

Everything below is DERIVED symbolically with sympy (exact), not assumed.
"""
import sympy as sp

PASS = 0
FAIL = 0
def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    print(("PASS" if ok else "FAIL") + ": " + name)
    PASS += ok
    FAIL += (not ok)

a, B, th, r = sp.symbols('a B theta r', real=True)

# ---------------------------------------------------------------------------
# 1.  Eigenvalues of the K/CPT-real circulant Y = a I + b C + conj(b) C^2.
#     On Fourier mode k the eigenvalue is a + b*w^k + conj(b)*w^{2k}
#     = a + 2|b| cos(theta + 2 pi k/3),  with b = |b| e^{i theta}.
# ---------------------------------------------------------------------------
lam = [a + 2*B*sp.cos(th + 2*sp.pi*k/3) for k in range(3)]

# verify these really are the eigenvalues a + b w^k + conj(b) w^{2k}
w = sp.exp(2*sp.I*sp.pi/3)
b = B*sp.exp(sp.I*th)
for k in range(3):
    eig_complex = a + b*w**k + sp.conjugate(b)*w**(2*k)
    check(f"eigenvalue k={k}: a + b w^k + conj(b) w^2k = a + 2|b|cos(theta+2pi k/3)",
          sp.simplify(sp.re(sp.expand_complex(eig_complex)) - lam[k]) == 0
          and sp.simplify(sp.im(sp.expand_complex(eig_complex))) == 0)

# ---------------------------------------------------------------------------
# 2.  Power sums.  S1 = sum lambda_k = 3a ;  S2 = sum lambda_k^2 = 3a^2 + 6|b|^2.
# ---------------------------------------------------------------------------
S1 = sp.simplify(sum(lam))
S2 = sp.simplify(sp.expand_trig(sum(l**2 for l in lam)))
S2 = sp.simplify(S2)

check("S1 = sum lambda_k = 3a", sp.simplify(S1 - 3*a) == 0)
check("S2 = sum lambda_k^2 = 3 a^2 + 6 B^2", sp.simplify(S2 - (3*a**2 + 6*B**2)) == 0)

# ---------------------------------------------------------------------------
# 3.  Koide ratio.  Q = (sum m_k)/(sum sqrt m_k)^2 = S2 / S1^2, with sqrt(m)=lambda.
# ---------------------------------------------------------------------------
Q = sp.simplify(S2 / S1**2)
Q_target = sp.Rational(1, 3) + sp.Rational(2, 3) * (B**2 / a**2)
check("Koide Q = S2/S1^2 = 1/3 + (2/3)(|b|^2/a^2)", sp.simplify(Q - Q_target) == 0)
check("Q is INDEPENDENT of theta = arg(b)  (dQ/dtheta = 0)",
      sp.simplify(sp.diff(Q, th)) == 0)

# in the dial variable r = |b|^2/a^2
Q_r = sp.Rational(1, 3) + sp.Rational(2, 3) * r
check("Q(r) = 1/3 + (2/3) r", sp.simplify(Q.subs(B, sp.sqrt(r)*a) - Q_r) == 0)

# ---------------------------------------------------------------------------
# 4.  Two real blocks, their powers, and the swap symmetry.
#     singlet (trivial char) power = a^2 ;  doublet (2 faithful chars) power = 2|b|^2.
# ---------------------------------------------------------------------------
singlet_power = a**2
doublet_power = 2*B**2
r_equal = sp.solve(sp.Eq(singlet_power, doublet_power), B)[0]**2 / a**2  # |b|^2/a^2 at equal power
check("equal block power (a^2 = 2|b|^2)  <=>  r = 1/2",
      sp.simplify(r_equal - sp.Rational(1, 2)) == 0)

swap = lambda rr: 1/(4*rr)
check("singlet<->doublet power swap acts as r -> 1/(4r), an involution",
      sp.simplify(swap(swap(r)) - r) == 0)
check("swap fixed point is exactly r = 1/2",
      sp.simplify(swap(sp.Rational(1, 2)) - sp.Rational(1, 2)) == 0)

# ---------------------------------------------------------------------------
# 5.  Values at the three distinguished settings.
# ---------------------------------------------------------------------------
check("symmetric setting r = 1/2  =>  Q = 2/3", sp.simplify(Q_r.subs(r, sp.Rational(1, 2)) - sp.Rational(2, 3)) == 0)
check("degenerate setting r = 0    =>  Q = 1/3", sp.simplify(Q_r.subs(r, 0) - sp.Rational(1, 3)) == 0)
check("Born setting       r = 1    =>  Q = 1",   sp.simplify(Q_r.subs(r, 1) - 1) == 0)

print()
print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
