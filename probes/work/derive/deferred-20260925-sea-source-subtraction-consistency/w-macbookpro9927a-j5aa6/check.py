#!/usr/bin/env python3
"""Sea source and its subtraction on an evolving lattice -- worker w-macbookpro9927a-j5aa6.

Recovery of block 147 (PR #9240; frozen head b88ec3d5f3, current head 328ab48910).
Families (see ATTEMPT.md):
  K  block 146's first law dm/dlam = -3 p l^3 for the sea, its counterterm, and a
     constant-in-time subtraction.
  C  the stretched block H_l = (sigma.s/l) x tau_z + mu tau_x: [H_l1, H_l2] = 0 iff
     mu (1/l1 - 1/l2) = 0; for mu = 0, H_l = H_1/l keeps every stationary state.
  A  two-level reduction; the interband element; the first excitation amplitude.
  M  the leading adiabatic dressing 1/2 m_lam lamdot^2 and m_lam per site; the
     cross-check with the dilation part of #9259's inertia.
  N  Noether energy of L_sea + L_member.
  H  fully occupied hard-core hopping is blocked.
Everything is exact (sympy, fractions).
"""
import sys
from itertools import product

import sympy as sp

FAILS = []


def ok(tag, cond, msg=""):
    if not cond:
        FAILS.append(tag)
    print(f"{tag} {'ok' if cond else 'FAIL'} {msg}".rstrip())


lam, I0, l0, mu = sp.symbols('lambda I ell0 mu', positive=True)
ell = sp.exp(lam)

# ---------------------------------------------------------------- family K
def pressure(m):  # block 146: dm/dlam = -3 p l^3
    return sp.simplify(-sp.diff(m, lam) / (3 * ell**3))


m_sea = -I0 / ell
rho_sea = m_sea / ell**3
p_sea = pressure(m_sea)
m_ct = I0 / ell
p_ct = pressure(m_ct)
m_const = I0 / l0            # "constant per site": the sea's value at one length l0
resid = sp.simplify(m_sea + m_const)
ok("K1", sp.simplify(p_sea - rho_sea / 3) == 0 and sp.simplify(p_ct - (m_ct / ell**3) / 3) == 0
   and pressure(m_const) == 0 and sp.simplify(resid - (I0 / l0 - I0 / ell)) == 0,
   "massless sea m = -I/l: p = rho/3; the subtraction that removes it at every length is "
   "m_ct = +I/l with p_ct = rho_ct/3; a subtraction constant in time (the sea at l0) has "
   "p = 0 and leaves I/l0 - I/l != 0 for l != l0")
y = sp.symbols('y', positive=True)
em = sp.sqrt(mu**2 + y * sp.exp(-2 * lam))          # one massive mode, y = s^2
pr = pressure(-em)
ratio = sp.simplify(pr / (-em / ell**3) - (y * sp.exp(-2 * lam)) / (3 * (mu**2 + y * sp.exp(-2 * lam))))
ok("K2", ratio == 0, "massive mode -sqrt(mu^2 + s^2/l^2): p/rho = y/(3(mu^2 + y)), y = s^2/l^2 "
   "(block 147 T1(e), restated)")

# ---------------------------------------------------------------- family C
s1, s2, s3 = sp.symbols('s1 s2 s3', real=True)
l1, l2 = sp.symbols('l1 l2', positive=True)
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
A = s1 * sig[0] + s2 * sig[1] + s3 * sig[2]
Z2 = sp.zeros(2)


def Hblk(l, m):
    return sp.Matrix(sp.BlockMatrix([[A / l, m * sp.eye(2)], [m * sp.eye(2), -A / l]]))


Cm = (Hblk(l1, mu) * Hblk(l2, mu) - Hblk(l2, mu) * Hblk(l1, mu)).applyfunc(sp.expand)
fro = sp.factor(sp.expand((Cm.H * Cm).trace()))
target = 16 * mu**2 * (s1**2 + s2**2 + s3**2) * (l1 - l2)**2 / (l1**2 * l2**2)
H0l = Hblk(l1, 0)
ok("C1", sp.simplify(fro - target) == 0 and (H0l - Hblk(1, 0) / l1).applyfunc(sp.simplify) == sp.zeros(4),
   "||[H_l1, H_l2]||^2 = 16 mu^2 |s|^2 (1/l1 - 1/l2)^2: zero iff mu (l1 - l2) |s| = 0; "
   "for mu = 0, H_l = H_1/l, so every stationary state keeps its occupations for every "
   "history l(t) and the sea's energy is exactly -<|s|>/l")

# ---------------------------------------------------------------- family A
r = sp.symbols('r', real=True, nonzero=True)
tz, tx = sig[2], sig[0]
h = r * sp.exp(-lam) * tz + mu * tx
E = sp.sqrt(r**2 * sp.exp(-2 * lam) + mu**2)
ev = h.eigenvects()
vec = {}
for val, mult, vs in ev:
    v = vs[0] / sp.sqrt((vs[0].H * vs[0])[0])
    vec[sp.simplify(val - E) == 0] = v
vp, vm = vec[True], vec[False]
dh = h.diff(lam)
elem2 = sp.simplify(sp.Abs((vp.H * dh * vm)[0])**2)
elem_ok = sp.simplify(elem2 - r**2 * sp.exp(-2 * lam) * mu**2 / E**2) == 0
# first excitation amplitude: c+'(0) = -<+|d_t ->, and <+|d_lam -> = <+|d_lam h|->/(E_- - E_+)
berry = sp.simplify((vp.H * vm.diff(lam))[0])
berry_ok = sp.simplify(sp.radsimp(berry**2 - elem2 / (2 * E)**2)) == 0   # h is real symmetric: berry is real
# reduction of the 4x4 block to two such 2x2 sectors: A has eigenvalues +-|s|, independent of l
sabs = sp.sqrt(s1**2 + s2**2 + s3**2)
evA = sorted(sp.simplify(e) for e in A.eigenvals())
red_ok = set(sp.simplify(e) for e in A.eigenvals()) == {sabs, -sabs}
ok("A1", elem_ok and berry_ok and red_ok,
   "block = two sectors (+-|s|/l) tau_z + mu tau_x (sigma.s eigenvectors do not depend on l); "
   "|<+|d_lam h|->|^2 = mu^2 r^2/(l^2 E^2), and |<+|d_lam ->| = |<+|d_lam h|->|/(2E): nonzero "
   "iff mu |s| != 0; so c+(tau) = -lamdot <+|d_lam -> tau + O(tau^2) and the evolving sea "
   "leaves the instantaneous ground state right after any instant with lamdot != 0")

# ---------------------------------------------------------------- family M
lamdot = sp.symbols('lamdot', real=True)
c1sq = (lamdot * berry / (2 * E))**2            # |first-order adiabatic amplitude|^2 (berry real)
dress = sp.simplify(sp.radsimp(2 * E * c1sq))
m_two = sp.simplify(2 * elem2 / (2 * E)**3)
ok("M1", sp.simplify(dress - m_two * lamdot**2 / 2) == 0
   and sp.simplify(m_two - r**2 * sp.exp(-2 * lam) * mu**2 / (4 * E**5)) == 0,
   "first-order adiabatic dressing 2E|c+|^2 = (1/2) m lamdot^2 with m = 2|<+|d_lam h|->|^2/(2E)^3 "
   "= mu^2 r^2/(4 l^2 E^5) per sector")
# per site: two sectors per block, half a block per site -> m_lam = < mu^2 |s|^2 / (4 l^2 E^5) >
S2 = sp.symbols('S2', positive=True)
Eb = sp.sqrt(mu**2 + S2)                       # at l = 1
per_site_lam = sp.Rational(1, 2) * 2 * (mu**2 * S2 / (4 * Eb**5))
m_A_9259 = mu**2 * S2 / (16 * Eb**5)           # #9259: dilation part per unit dh, per site
ok("M2", sp.simplify(per_site_lam - 4 * m_A_9259) == 0,
   "per site m_lam = <mu^2|s|^2/(4 l^2 E^5)>; at l = 1 this is 4 times #9259's dilation part "
   "<mu^2|s|^2/(16E^5)> per unit dh (lam = h/2 at first order): the same cranking inertia")

# ---------------------------------------------------------------- family N
t = sp.symbols('t')
L_ = sp.Function('lam')(t)
mf, ef, cf, Vf = [sp.Function(n) for n in ('m', 'e', 'c', 'V')]
Ld = sp.diff(L_, t)
Lag = sp.Rational(1, 2) * (mf(L_) + cf(L_)) * Ld**2 - ef(L_) - Vf(L_)
EL = sp.diff(sp.diff(Lag, Ld), t) - sp.diff(Lag, L_)
hen = Ld * sp.diff(Lag, Ld) - Lag
ok("N1", sp.simplify(sp.diff(hen, t) - Ld * EL) == 0,
   "L = (1/2)(m_lam + c) lamdot^2 - e(lam) - V(lam): dh/dt = lamdot (Euler-Lagrange), so the "
   "energy e + V + (1/2)(m_lam + c) lamdot^2 is conserved on solutions")

# ---------------------------------------------------------------- family H
Lr = 4
full = (1,) * Lr
blocked = True
for x in range(Lr):
    yv = (x + 1) % Lr
    for (a, b) in ((x, yv), (yv, x)):     # hop b -> a needs a empty and b occupied
        blocked &= not (full[a] == 0 and full[b] == 1)
ok("H1", blocked, "fully occupied hard-core ring: every hop targets an occupied site, so the "
   "hopping annihilates the state; its energy does not depend on l (zero pressure)")

print(f"checks: {'all passed' if not FAILS else 'FAILED ' + ' '.join(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
    sys.exit(1)
print("SUMMARY: PARTIAL massless sea: exact energy -I/l for every history, p = rho/3; subtraction needs "
      "the counterterm +I/l with p = rho/3 (a time-constant one leaves I/l0 - I/l); staggered mass: the "
      "sea is left at any finite rate, leading counterterm (1/2) m_lam lamdot^2 (adiabatic expansion "
      "ASSUMED); full hard-core hopping is blocked")
print("HIT: On a uniformly stretched lattice (hopping / l) with block 146's first law dm/dlam = -3 p l^3: "
      "(a) without the staggered mass H_l = H_1/l, so the free sea keeps its occupations for every "
      "history; its energy is exactly -I/l per site with p = rho/3, and measuring energy from the sea "
      "needs the counterterm +I/l with p_ct = rho_ct/3 - a subtraction constant in time leaves "
      "I/l0 - I/l in the zero mode, so block 147 T3's 'constant per site' holds in space only. (b) With "
      "the staggered mass ||[H_l1, H_l2]||^2 = 16 mu^2|s|^2 (1/l1 - 1/l2)^2 per block, and the sea "
      "started in the instantaneous ground state is excited at first order in time in every block with "
      "mu|s| != 0 wherever lamdot != 0, so neither the instantaneous energy nor its subtraction is the "
      "evolving sea's energy; at leading adiabatic order the missing term is (1/2) m_lam lamdot^2 per "
      "site, m_lam = <mu^2|s|^2/(4 l^2 E^5)>, the dilation part of #9259's cranking inertia, and "
      "L_sea = <E> + (1/2) m_lam lamdot^2 is a conditional prescription whose energy with the member's "
      "is conserved.")
