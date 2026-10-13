"""C5 R19-17 (b): the force F_I = dGamma_exc/dX^I that matter excitations exert on the lattice, for cold dust.
A dust particle of mass m with lattice-frame dispersion E(p) = sqrt(m^2 + c^2 * sum_i (2/l)^2 sin^2(p_i l/2)).
Lagrangian L(v) = p.v - E(p) at v = dE/dp. Expand the lattice-dependent part dL(v_rel, l) in the relative
velocity v_rel between dust and lattice frame: force on lattice ~ -d dL/d v_rel, strain force ~ d dL/d l.
Claim: with c = 1 (common limiting speed; the cone rows paid) dL = O(v^4) => F_I = O(eps^3) at linear order;
with c != 1, dL = O(v^2) => F_I = O(eps) (first order)."""
import sympy as sp
v1, v2, v3, l, m, c, s = sp.symbols('v1 v2 v3 l m c s', positive=True)
vx, vy, vz = [s*w for w in (v1, v2, v3)]   # s = bookkeeping order of the relative velocity
# Legendre transform order by order: L(v) = -m sqrt(1 - v^2/c^2)... do it via E(p) expansion in l and in s
p1, p2, p3 = sp.symbols('p1 p2 p3')
E = sp.sqrt(m**2 + c**2*sum((2/l)**2*sp.sin(pi*l/2)**2 for pi in (p1, p2, p3)))
E_l = sp.series(E, l, 0, 4).removeO()           # E to O(l^2)
E0 = E_l.subs(l, 0); dE = sp.simplify(E_l - E0)
# to first order in dE: dL(v) = -dE(p(v)) with p(v) the unperturbed momentum p = m v/(c^2 sqrt(1-v^2/c^2))
gam = 1/sp.sqrt(1 - (vx**2 + vy**2 + vz**2)/c**2)
pv = {p1: m*vx*gam/c**2, p2: m*vy*gam/c**2, p3: m*vz*gam/c**2}
dL = -dE.subs(pv)
ser = sp.series(dL, s, 0, 6).removeO()
print('lattice part of the dust Lagrangian, c general, to O(l^2), series in relative velocity s:')
print('  ', sp.simplify(sp.expand(ser)))
print('  lowest power of s:', min(sp.Poly(sp.expand(ser), s).monoms())[0])
# species-speed offset relative to the metric light cone (c != 1): dL_c = -(E_c - E_1) at fixed v
L_c = -m*sp.sqrt(1 - (vx**2+vy**2+vz**2)/c**2)   # E^2 = m^2 + c^2 p^2: same rest energy m as the LI reference
L_1 = -m*sp.sqrt(1 - (vx**2+vy**2+vz**2))
d_c = sp.series(L_c - L_1, s, 0, 6).removeO()
print('cone-offset part (c != 1), series in s:', sp.simplify(d_c))
print('=> with c = 1 the lattice force on cold dust is O(s^3); with c != 1 it is O(s) (first order).')
