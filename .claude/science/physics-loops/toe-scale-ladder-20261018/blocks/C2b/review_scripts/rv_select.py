#!/usr/bin/env python3
"""Reviewer spot-check of C2b claim (4), re-derived from the parent walk definition
(docs/TWO_QUBIT_SITE_UNFREEZES_..._2026-10-16.md, Theorems 2, 4, 5, 7):
  G(b) Gram matrix (Theorem 2); s = b0 + 2 b1 + b2; massless member: cos omega(k) = phi0^T G phi(k)
  (Theorem 7), phi(k) = (1, e1, e2, e3) of the cosines.
Route differs from scripts/kip_parameter_selection.py: s^2 = 1 is attacked via v^T G v = 1 - s^2 with
v = (1,2,1,0) and a lex Groebner basis of G v = 0 (not sympy.solve); spectra come from the scalar
dispersion cos omega = phi0^T G phi(k) (no 4x4 walk matrix is built)."""
import sys
import numpy as np
import sympy as sp
P = F = 0
def chk(n, ok):
    global P, F
    P += bool(ok); F += (not ok); print(('PASS ' if ok else 'FAIL ') + n, flush=True)
b0, b1, b2 = sp.symbols('b0 b1 b2')
G = sp.Matrix([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
               [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
               [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
               [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])
s = b0 + 2*b1 + b2
v = sp.Matrix([1, 2, 1, 0]); w = sp.Matrix([0, 1, 2, 1])
chk('v^T G v = 1 - s^2 (so s^2 = 1 and G >= 0 force G v = 0)', sp.expand((v.T*G*v)[0] - (1 - s**2)) == 0)
chk('w^T G w = s^2 and v^T G w = 0', sp.expand((w.T*G*w)[0] - s**2) == 0 and sp.expand((v.T*G*w)[0]) == 0)
GB = sp.groebner(list(G*v), b2, b1, b0, order='lex')
uni = [g for g in GB.exprs if g.free_symbols <= {b0}]
print('univariate element(s) in b0:', [sp.factor(u) for u in uni])
sols = sp.solve(GB.exprs, [b0, b1, b2], dict=True)
real = [d for d in sols if all(abs(sp.im(sp.N(d[x], 30))) < 1e-25 for x in (b0, b1, b2))]
print(f'{len(sols)} solutions, {len(real)} real')
chk('G(b) v = 0 has exactly 4 real solutions (zero-dimensional ideal)', len(real) == 4 and GB.is_zero_dimensional)
r5 = sp.sqrt(5)
bg = (sp.Rational(-5, 38) + 9*r5/38, (5*r5 - 7)/19, (71 - 29*r5)/38)
psd = []
for d in real:
    ev = np.linalg.eigvalsh(np.array(G.subs(d).evalf(40), dtype=float))
    print('  b =', [sp.N(d[x], 10) for x in (b0, b1, b2)], ' s =', sp.N(s.subs(d), 12), ' eig =', np.round(ev, 6))
    if ev.min() > -1e-12: psd.append(d)
match = all(any(all(sp.simplify(d[x] - sg*bgx) == 0 for x, bgx in zip((b0, b1, b2), bg)) for sg in (1, -1)) for d in psd)
chk('PSD ones are exactly +-b_gold (s = +1 at +b_gold, s = -1 at -b_gold)', len(psd) == 2 and match)
# dispersion of the massless member at b_gold
Gn = np.array(G.subs(dict(zip((b0, b1, b2), bg))).evalf(30), dtype=float)
phi = lambda k: np.array([1, np.cos(k).sum(), np.cos(k[0])*np.cos(k[1]) + np.cos(k[0])*np.cos(k[2]) + np.cos(k[1])*np.cos(k[2]), np.prod(np.cos(k))])
p0 = phi(np.zeros(3))
fk = lambda k: p0 @ Gn @ phi(np.asarray(k, float))
chk(f'cos omega(0) = 1 (phi0^T G phi0 = {fk([0,0,0]):.15f})', abs(fk([0, 0, 0]) - 1) < 1e-13)
e = 1e-4
om = lambda k: np.arccos(np.clip(fk(k), -1, 1))
vax = om([e, 0, 0])/e; vdg = om(np.array([e, e, e])/np.sqrt(3))/e
chk(f'b_gold Gamma cone speed axis {vax:.7f} diag {vdg:.7f} = 1', abs(vax - 1) < 1e-6 and abs(vdg - 1) < 1e-6)
chk(f'b_gold: cos omega(X) = {fk([np.pi,0,0]):.12f} = -1 (pi-mode at the axis doubler)', abs(fk([np.pi, 0, 0]) + 1) < 1e-12)
# near X, pi - omega
e = 1e-4
dpar = (np.pi - om([np.pi - e, 0, 0]))/e; dperp = (np.pi - om([np.pi, e, 0]))/e
chk(f'pi-mode cone at X: v_par = {dpar:.7f}, v_perp = {dperp:.7f}; sqrt5-2 = {np.sqrt(5)-2:.7f}',
    abs(dpar - 1) < 1e-6 and abs(dperp - (np.sqrt(5) - 2)) < 1e-6)
# two-tick clock: U^2 has eigenphases 2 omega; near X it is ~ 2(omega - pi) -> 0, i.e. a light IR mode
q = 1e-3
two = np.angle(np.exp(2j*om([np.pi, q, 0])))
chk(f'two-tick clock: X modes at quasienergy {np.angle(np.exp(2j*om([np.pi,0,0]))):.1e} with transverse speed {abs(two)/(2*q):.6f} per tick',
    abs(np.angle(np.exp(2j*om([np.pi, 0, 0])))) < 1e-6 and abs(abs(two)/(2*q) - (np.sqrt(5) - 2)) < 1e-5)
# comparator: Euclidean transfer weights on a tick rho; B4+ on the gauge sector
U_, K_, rho = sp.symbols('U K rho', positive=True)
bt, bs = 1/(U_*rho), K_*rho
rs = sp.solve(sp.Eq(bt, bs), rho)
chk(f'beta_t = beta_s <=> rho = {rs[0]}', len(rs) == 1 and sp.simplify(rs[0]*sp.sqrt(U_*K_) - 1) == 0)
chk(f'speed sqrt(beta_s/beta_t) = sqrt(UK) rho; 1/1.025 = {1/1.025:.4f} = 0.9756', sp.simplify(sp.sqrt(bs/bt) - sp.sqrt(U_*K_)*rho) == 0 and round(1/1.025, 4) == 0.9756)
print(f'TOTAL: PASS={P} FAIL={F}')
sys.exit(1 if F else 0)
