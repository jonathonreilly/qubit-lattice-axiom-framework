#!/usr/bin/env python3
"""Reviewer's exact checks for C7 (independent of scripts/c7_exact.py).

Route for the O(a) term: direct matrix-log expansion log(M U0 M) = E - E^2/2 + E^3/3
in powers of a, where U0 is built only from (i) phi(k) = phi0 - (k^2/2) w + O(k^4),
(ii) h0(0) = 0, (iii) unitarity. No O(3)-rotation identity, no omega/sin(omega).
|W| is derived from the axis-doubler: phi(X) = phi0 - 2w exactly, so h(X) = -2W.
"""
import sys, itertools
import sympy as sp

P = F = 0
def chk(name, ok):
    global P, F
    ok = bool(ok); P += ok; F += (not ok)
    print(("PASS " if ok else "FAIL ") + name)

kr = sp.kronecker_product
I2 = sp.eye(2)
t1 = sp.Matrix([[0, 1], [1, 0]]); t2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); t3 = sp.diag(1, -1)
T1, T2 = kr(t1, I2), kr(t2, I2)
S = [kr(t3, x) for x in (t1, t2, t3)]

# ---- (A) phi expansion and phi(X) = phi0 - 2w
k = sp.symbols('k1:4', real=True); e = sp.Symbol('e', positive=True)
def phi(cs):
    return sp.Matrix([1, sum(cs), cs[0]*cs[1]+cs[0]*cs[2]+cs[1]*cs[2], cs[0]*cs[1]*cs[2]])
phi0 = sp.Matrix([1, 3, 3, 1]); w = sp.Matrix([0, 1, 2, 1])
ph = phi([sp.cos(e*x) for x in k]).applyfunc(lambda z: sp.series(z, e, 0, 4).removeO())
ksq = sum(x**2 for x in k)
chk('phi(e k) = phi0 - e^2 |k|^2 w/2 + O(e^4)', (ph - phi0 + e**2*ksq*w/2).applyfunc(sp.expand) == sp.zeros(4, 1))
chk('phi(X) = phi(c=(-1,1,1)) = phi0 - 2 w exactly', phi([-1, 1, 1]) - (phi0 - 2*w) == sp.zeros(4, 1))

# |W|^2 from unitarity at the axis TRIM: g(X)=0, f_X = 1 - 2 s^2 => |h_X|^2 = 4 s^2 (1 - s^2); h_X = C(phi0 - 2w) = -2W
sS = sp.Symbol('s', real=True)
fX = 1 - 2*sS**2
chk('|W|^2 = |h_X|^2/4 = (1 - f_X^2)/4 = s^2 (1 - s^2) (given f_X = 1 - 2 s^2)', sp.expand((1 - fX**2)/4 - sS**2*(1 - sS**2)) == 0)
# f_X = 1 - 2 a.w where a = G phi0; order-k^2 unitarity forces a.w = s^2 (|g|^2 = s^2 k^2, |h|^2 = O(k^4))
aw = sp.Symbol('aw')
f0k = 1 - e**2*ksq*aw/2
uni = sp.expand(sp.series(f0k**2 + sS**2*e**2*ksq - 1, e, 0, 3).removeO())
chk('O(k^2) unitarity: f0^2 + |g|^2 = 1 forces a.w = s^2, hence f_X = 1 - 2 s^2', sp.solve(uni.coeff(e, 2), aw) == [sS**2])
# polynomial cross-check of a.w = s^2 and the |W|^2 identity using the parent's G(b) (stated in parent note)
b0, b1, b2 = sp.symbols('b0:3', real=True)
G = sp.Matrix([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
               [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
               [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
               [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])
sb = b0 + 2*b1 + b2
fXb = sp.expand((phi0.T*G*(phi0 - 2*w))[0])
chk('from G(b): f_X = phi0^T G (phi0 - 2w) = 1 - 2 s^2', sp.expand(fXb - 1 + 2*sb**2) == 0)
hX2 = sp.expand(((phi0-2*w).T*G*(phi0-2*w))[0] - fXb**2)
chk('from G(b): |h_X|^2 = phi_X^T G phi_X - f_X^2 = 4 s^2 (1 - s^2)', sp.expand(hX2 - 4*sb**2*(1 - sb**2)) == 0)

# ---- (B) direct log expansion of U = M U0 M, hhat = tau1 (gauge), W = (Wc, Ws)
a, m = sp.symbols('a m', positive=True)
p = sp.symbols('p1:4', real=True); Wc, Ws = sp.symbols('Wc Ws', real=True)
psq = sum(x**2 for x in p)
Wt = Wc*T1 + Ws*T2
sigp = sum((p[i]*S[i] for i in range(3)), sp.zeros(4))
# U0 through O(a^2): f0 = 1 - s^2 a^2 p^2/2, h0 = -(a^2 p^2/2) W, g = s a p  (+O(a^3))
U0 = (1 - sS**2*a**2*psq/2)*sp.eye(4) + sp.I*(-(a**2*psq/2)*Wt + sS*a*sigp)
Mh = sp.eye(4) + sp.I*a*m/2*T1 - (a*m/2)**2/2*sp.eye(4)
def trunc(Mx, n):
    return Mx.applyfunc(lambda z: sum(sp.expand(z).coeff(a, j)*a**j for j in range(n+1)))
U = trunc(Mh*U0*Mh, 3)
E = U - sp.eye(4)
Z = trunc(E - trunc(E*E, 3)/2 + trunc(E*E*E, 3)/3, 2)   # log through O(a^2)
H = trunc((sp.I/a*Z).applyfunc(sp.expand), 1)
alpha = [-x for x in S]; beta = -T1
HD = sS*sum((p[i]*alpha[i] for i in range(3)), sp.zeros(4)) + m*beta
chk('direct log: H_a = s alpha.p + m beta + (a/2)|p|^2 W.tau + O(a^2), alpha = -tau3 sigma, beta = -hhat.tau',
    (H - HD - a*psq/2*Wt).applyfunc(sp.expand) == sp.zeros(4))
# symmetric BCH cross-check: log(e^{A/2} e^{B} e^{A/2}) = A + B + O(3rd order) -> no extra O(a) commutator term
A_ = sp.I*a*m*T1; B_ = -sp.I*a*(sS*sum((p[i]*S[i] for i in range(3)), sp.zeros(4))*(-1) + a*psq/2*Wt)
c3 = (A_*(A_*B_ - B_*A_) - (A_*B_ - B_*A_)*A_)
chk('symmetric BCH: leading commutator [A,[A,B]] is O(a^3) in the exponent (O(a^2) in H)',
    all(sp.expand(z).coeff(a, j) == 0 for z in c3 for j in (0, 1, 2)))

# ---- (C) twist dichotomy
chi = sp.Symbol('chi', real=True); Wn = sp.Symbol('Wn', positive=True)
Wt_chi = Wn*(sp.cos(chi)*T1 + sp.sin(chi)*T2)     # hhat = tau1, chi = angle(W, hhat)
H1 = HD + a*psq/2*Wt_chi
H2 = (H1*H1).applyfunc(lambda z: sp.simplify(sp.expand(z)))
Esq = m**2 + sS**2*psq - a*m*Wn*sp.cos(chi)*psq + a**2*Wn**2*psq**2/4
chk('(H_D + (a/2)p^2 W.tau)^2 = (m^2 + s^2 p^2 - a m |W| cos(chi) p^2 + a^2|W|^2 p^4/4) 1',
    (H2 - Esq*sp.eye(4)).applyfunc(sp.simplify) == sp.zeros(4))
Gp = T2
chk('max twist: Gamma_perp = tau2 anticommutes with alpha_a and beta; beta Gamma_perp is anti-Hermitian, squares to -1, commutes with alpha_a',
    all((Gp*X + X*Gp) == sp.zeros(4) for X in alpha + [beta]) and (beta*Gp).H == -(beta*Gp)
    and (beta*Gp)**2 == -sp.eye(4) and all(beta*Gp*X - X*beta*Gp == sp.zeros(4) for X in alpha))
ep = sp.Symbol('epsilon', positive=True); phv = sp.atan(ep/m)
V = sp.cos(phv/2)*sp.eye(4) + sp.sin(phv/2)*beta*Gp
Hm = sS*sum((p[i]*alpha[i] for i in range(3)), sp.zeros(4)) + m*beta + ep*Gp
chk('V(phi) maps s alpha.p + m beta + eps Gamma_perp to s alpha.p + sqrt(m^2+eps^2) beta exactly',
    (V*Hm*V.H - (Hm - m*beta - ep*Gp + sp.sqrt(m**2 + ep**2)*beta)).applyfunc(sp.simplify) == sp.zeros(4))
# Wilson-aligned: eigenvalue shift at O(a)
Ea = sp.sqrt(Esq); E0 = sp.sqrt(m**2 + sS**2*psq)
d1 = sp.simplify(sp.series(Ea - E0, a, 0, 2).removeO())
chk('E_a - E = -a m |W| cos(chi) p^2/(2E) + O(a^2) (spectral, not removable by any unitary identification)',
    sp.simplify(d1 + a*m*Wn*sp.cos(chi)*psq/(2*E0)) == 0)

# ---- (D) vertex lemma ingredient: f = row . phi is multilinear in (c1,c2,c3)
c = sp.symbols('c1:4'); r = sp.symbols('r0:4')
fl = sp.expand((sp.Matrix([r]).T.T*phi(c))[0]) if False else sp.expand(sum(r[i]*phi(c)[i] for i in range(4)))
chk('f = r . phi(c) has degree <= 1 in each c_a (multilinear)', all(sp.degree(fl, x) == 1 for x in c))
# affine-in-each-variable => along each coordinate line extremum at endpoints (direct: second derivative 0)
chk('d^2 f / d c_a^2 = 0 for each a', all(sp.diff(fl, x, 2) == 0 for x in c))

# ---- (E) parent series coefficient
u = sp.Symbol('u', positive=True)
ser = sp.series(sp.acos(1 - u)**2, u, 0, 5).removeO()
chk('arccos(1-u)^2 = 2u + u^2/3 + 4u^3/45 + O(u^4) (u^3 coefficient 4/45, not 8/45)',
    sp.expand(ser).coeff(u, 3) == sp.Rational(4, 45) and sp.expand(ser).coeff(u, 2) == sp.Rational(1, 3))
y = sp.Symbol('y')
chk('origin of 8/45: arcsin(y)^2 = y^2 + y^4/3 + 8 y^6/45 (arccos(1-u)^2 = 4 arcsin(sqrt(u/2))^2 rescales 8/45 -> 4/45)',
    sp.expand(sp.series(sp.asin(y)**2, y, 0, 8).removeO()).coeff(y, 6) == sp.Rational(8, 45))
# isotropic k^6 shift: only the u^3 term's leading part (s^2 k^2/2)^3 changes
dx = sp.Rational(8 - 4, 45)*(sS**2/2)**3
chk('x shift = (4/45)(s^2/2)^3 = s^2 (4 s^4)/360, so x: s^2(8s^4-5s^2+2)/360 -> s^2(4s^4-5s^2+2)/360',
    sp.expand(dx - sS**2*4*sS**4/360) == 0)
xc = lambda s2: s2*(4*s2**2 - 5*s2 + 2)/360
xp = lambda s2: s2*(8*s2**2 - 5*s2 + 2)/360
chk('at s^2 = 2/3: parent x = 1/243, corrected x = 1/1215',
    xp(sp.Rational(2, 3)) == sp.Rational(1, 243) and xc(sp.Rational(2, 3)) == sp.Rational(1, 1215))

print(f"TOTAL: PASS={P} FAIL={F}")
sys.exit(1 if F else 0)
