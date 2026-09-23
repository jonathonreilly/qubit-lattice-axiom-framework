#!/usr/bin/env python3
"""J:derive:the-kinetic-term-under-the-two-blindness-demands:a1 -- worker w-macbookpro90c72-j93ca (claude-opus-5-5).

The frame's kinetic term under blindness to rotations of the coin axes that vary in the label, and to relabellings that
vary in the label. Every line is exact (sympy over the rationals, symbolic functions of the label).
"""
import sys, time
import sympy as sp

T0 = time.time(); FAILS = []
def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)

# ------------------------------------------------------------------ K.rot: a rotation of the coin axes varying in the label
# frame matrix E[j, a] = e^j_a (bond direction j, coin axis a); inverse metric g^{-1} = E E^T (block 62 T1); K = Edot E^{-1}/w
w = sp.symbols("w", positive=True)
E = sp.Matrix([[2, 1, 0], [sp.Rational(1, 2), 3, 1], [0, -1, 2]])            # a generic rational frame (det != 0)
Ed = sp.Matrix(3, 3, sp.symbols("d0:9"))                                    # its rate of change, symbolic
o1, o2, o3 = sp.symbols("o1:4")
Om = sp.Matrix([[0, -o3, o2], [o3, 0, -o1], [-o2, o1, 0]])                    # Rdot^T R: any antisymmetric matrix
g = (E * E.T).inv(); gi = E * E.T
K = Ed * E.inv() / w
Kp = K + E * Om * E.inv() / w                                               # e -> R(label, place) e changes K by E Om E^{-1}/w
def inv3(Km):
    I1 = (g * Km * gi * Km.T).trace()                                       # K_jk K^jk (indices moved with the metric)
    I2 = (Km * Km).trace()                                                  # K^j_k K^k_j
    I3 = Km.trace() ** 2
    return [sp.expand(x) for x in (I1, I2, I3)]
a0, a1 = inv3(K), inv3(Kp)
good = sp.simplify((g * E * Om * E.inv()) + (g * E * Om * E.inv()).T) == sp.zeros(3, 3)       # lowered change is antisymmetric
good &= sp.expand(a1[0] + a1[1] - a0[0] - a0[1]) == 0 and sp.expand(a1[2] - a0[2]) == 0
good &= sp.expand(a1[0] - a1[1] - a0[0] + a0[1]) != 0
# the symmetric part of the lowered K is minus half the metric's rate per tick
gdot = -g * (Ed * E.T + E * Ed.T) * g
Klow = g * K
good &= sp.simplify((Klow + Klow.T) / 2 + gdot / (2 * w)) == sp.zeros(3, 3)
# first order around the identity frame: E = 1 + eps, h = -(eps + eps^T): the blind family is alpha hdot_ij hdot_ij + beta hdot^2
ep = sp.Matrix(3, 3, sp.symbols("q0:9")); epd = sp.Matrix(3, 3, sp.symbols("r0:9")); t_ = sp.symbols("t_")
E1 = sp.eye(3) + t_ * ep; E1d = t_ * epd
K1 = (E1d * (sp.eye(3) - t_ * ep))                                          # E^{-1} to first order; w = 1
S1 = (K1 + K1.T) / 2; hd = -(epd + epd.T)
good &= sp.expand(sp.series((S1 * S1).trace(), t_, 0, 3).removeO() - t_ ** 2 * (hd * hd).trace() / 4) == 0
good &= sp.expand(sp.series(K1.trace() ** 2, t_, 0, 3).removeO() - t_ ** 2 * hd.trace() ** 2 / 4) == 0
ok("K.rot", good, "e -> R(x, t) e adds E (Rdot^T R) E^-1 / w to K, whose metric-lowered form is exactly antisymmetric (generic "
   "rational frame, symbolic rates, any antisymmetric Rdot^T R); so tr(K^T K) + tr(K^2) and (tr K)^2 are blind and tr(K^T K) - "
   "tr(K^2) is not: blindness forces c1 = c2 and leaves the symmetric part, which is exactly -gdot/(2w); the blind family is "
   "(det e/w)[alpha tr(g^-1 gdot g^-1 gdot) + beta (tr g^-1 gdot)^2], at first order alpha hdot_ij hdot_ij + beta hdot^2: "
   "block 62's two numbers")

# ------------------------------------------------------------------ K.iso: the isotropic stretch and block 60 T5
al, be, Kc = sp.symbols("alpha beta K", real=True)
lamd = sp.symbols("lamdot")
hdi = 2 * lamd * sp.eye(3)
kin_iso = sp.expand(al * (hdi * hdi).trace() + be * hdi.trace() ** 2)
good = sp.expand(kin_iso - (12 * al + 36 * be) * lamd ** 2) == 0
ck = 12 * al + 36 * be
good &= sp.simplify(ck.subs({al: Kc / 4, be: -Kc / 4}) + 6 * Kc) == 0
good &= sp.simplify(ck.subs(be, -al) + 24 * al) == 0
ok("K.iso", good, "for h = 2 lam delta the kinetic term is (12 alpha + 36 beta)(dlam/dt)^2, so block 60 T5's c_k = 12 alpha + 36 beta: "
   "a closed lattice moves uniformly iff beta < -alpha/3 (alpha > 0 for real travelling disturbances); at beta = -alpha, "
   "c_k = -24 alpha, and with alpha = K/4 it is -6K, block 60 T5's comparator value")

# ------------------------------------------------------------------ K.modes: block 62 T4's determinant and what vanishes at beta = -alpha
p = sp.symbols("p1:4", real=True); X = sp.symbols("X")
hs = sp.symbols("h11 h22 h33 h12 h13 h23"); u = sp.symbols("u")
H = sp.Matrix([[hs[0], hs[3], hs[4]], [hs[3], hs[1], hs[5]], [hs[4], hs[5], hs[2]]])
P = sp.Matrix(p); p2 = sum(x ** 2 for x in p); tr = H.trace()
R1 = -((P.T * H * P)[0] - p2 * tr)
R2 = -sp.Rational(1, 4) * p2 * sum(H.multiply_elementwise(H)) + sp.Rational(1, 2) * ((H * P).T * (H * P))[0] \
     - sp.Rational(1, 2) * (P.T * H * P)[0] * tr + sp.Rational(1, 4) * p2 * tr ** 2
kin = al * sum(H.multiply_elementwise(H)) + be * tr ** 2                  # applied to hdot; w = K = 1 below
Lpot = Kc * (u * R1 + R2)                                                   # L = kinetic + K(u R1 + R2) (the ledger's F_2 = -K(u R1 + R2))
vars_ = list(hs) + [u]
# mode equations for e^{i omega t}, X = omega^2: X dkin/dh + dLpot/dh = 0, dLpot/du = 0
rows = []
for v in vars_:
    rows.append([sp.diff(X * sp.diff(kin, v) + sp.diff(Lpot, v), v2) for v2 in vars_])
M = sp.Matrix(rows)
det = sp.factor(M.det().subs(Kc, 1))
target = X ** 3 * al ** 2 * (al + be) * p2 ** 2 * (p2 - 4 * al * X) ** 2
ratio = sp.simplify(det / target)
good = ratio.free_symbols == set() and ratio != 0
null = sp.Matrix([p[0] ** 2, p[1] ** 2, p[2] ** 2, p[0] * p[1], p[0] * p[2], p[1] * p[2], 2 * al * X / Kc])
good &= sp.simplify(M.subs(be, -al) * null) == sp.zeros(7, 1)
# the exact label symmetry: h -> h + p p^T zeta(t), u -> u - (2 alpha/K) zeta''(t)
t = sp.symbols("t"); zeta = sp.Function("zeta")(t)
hf = [sp.Function(f"H{i}")(t) for i in range(6)]; uf = sp.Function("U")(t)
def Lfun(hl, ul):
    Hm = sp.Matrix([[hl[0], hl[3], hl[4]], [hl[3], hl[1], hl[5]], [hl[4], hl[5], hl[2]]])
    Hd = Hm.diff(t); trm = Hm.trace()
    r1 = -((P.T * Hm * P)[0] - p2 * trm)
    r2 = -sp.Rational(1, 4) * p2 * sum(Hm.multiply_elementwise(Hm)) + sp.Rational(1, 2) * ((Hm * P).T * (Hm * P))[0] \
         - sp.Rational(1, 2) * (P.T * Hm * P)[0] * trm + sp.Rational(1, 4) * p2 * trm ** 2
    return al * sum(Hd.multiply_elementwise(Hd)) + be * Hd.trace() ** 2 + Kc * (ul * r1 + r2), r1
shift = [p[0] ** 2, p[1] ** 2, p[2] ** 2, p[0] * p[1], p[0] * p[2], p[1] * p[2]]
L0, r1f = Lfun(hf, uf)
L1, _ = Lfun([hf[i] + shift[i] * zeta for i in range(6)], uf - 2 * al * zeta.diff(t, 2) / Kc)
dL = sp.expand(L1 - L0)
total = sp.expand(-2 * al * sp.diff(zeta.diff(t) * r1f, t))
rest = sp.expand(dL - total)
good &= sp.simplify(rest.subs(be, -al)) == 0 and sp.simplify(rest) != 0
# a transverse relabelling in the label, xi = (p2, -p1, 0) zeta(t) (p . xi = 0), is not a symmetry for any (alpha, beta)
xi = [p[1] * zeta, -p[0] * zeta, 0]
dh = [2 * p[0] * xi[0], 2 * p[1] * xi[1], 2 * p[2] * xi[2], p[0] * xi[1] + p[1] * xi[0], p[0] * xi[2] + p[2] * xi[0], p[1] * xi[2] + p[2] * xi[1]]
L2, _ = Lfun([hf[i] + dh[i] for i in range(6)], uf)
quad = sp.expand(L2 - L0).coeff(zeta.diff(t), 2)
good &= sp.simplify(quad - 2 * al * p2 * (p[0] ** 2 + p[1] ** 2)) == 0
ok("K.modes", good, "the 7x7 mode determinant of block 62 T4 is a constant times X^3 alpha^2 (alpha + beta)(p^2)^2 (p^2 - 4 alpha X)^2; "
   "at beta = -alpha, (h, u) = (p p^T, 2 alpha X/K) is a null vector for every p and X, and the quadratic Lagrangian changes under "
   "h -> h + p p^T zeta(t), u -> u - (2 alpha/K) zeta'' by the total derivative -2 alpha d(zeta' R_1)/dt exactly, and only then "
   "(without the u shift: a symmetry where R_1 is constant in the label, i.e. on the rates' constraint with content fixed); a "
   "transverse relabelling in the label costs 2 alpha p^2 |xi'|^2 for every (alpha, beta): nothing in the clauses can absorb it")

# ------------------------------------------------------------------ K.speed: what alpha/K is
good = sp.solve(sp.Eq(Kc * p2 / (4 * al), p2), al) == [Kc / 4]
ok("K.speed", good, "the travelling pair has X = K wbar^2 p^2/(4 alpha) (block 62 T4): at the walker's top speed (X = p^2, one site per "
   "ambient tick) iff alpha = K/4; no clause of blocks 53 to 65 makes the field's disturbances share the walker's light cone")
print(f"runtime {time.time() - T0:.0f} s")

if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL blindness to rotations of the coin axes that vary in the label leaves exactly block 62's two kinetic numbers; "
      "blindness to relabellings that vary in the label fixes beta = -alpha (with the rates shifting by -(2 alpha/K) zeta''), for "
      "gradient relabellings only; alpha/K stays declared")
print("HIT: a rotation of the coin axes varying in place and label adds E (Rdot^T R) E^-1/w to the frame's rate K, exactly "
      "antisymmetric once lowered with the metric, while its symmetric part is -gdot/(2w); so blindness leaves (det e/w)[alpha "
      "tr(g^-1 gdot g^-1 gdot) + beta (tr g^-1 gdot)^2], block 62's (alpha, beta), and the isotropic stretch carries "
      "(12 alpha + 36 beta) lamdot^2 = block 60 T5's c_k, negative iff beta < -alpha/3.")
print("HIT: at second order the relabelling h -> h + p p^T zeta(t) with u -> u - (2 alpha/K) zeta'' changes the Lagrangian by the "
      "total derivative -2 alpha d(zeta' R_1)/dt iff beta = -alpha (the zero of block 62 T4's determinant; the rates act as its "
      "multiplier); transverse relabellings in the label cost 2 alpha p^2 |xi'|^2 for every (alpha, beta); (K/4, -K/4) gives "
      "c_k = -6K, block 60 T5's comparator value, but alpha = K/4 (the walker's top speed) stays declared.")
