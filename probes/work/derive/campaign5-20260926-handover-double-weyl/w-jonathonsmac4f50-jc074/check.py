"""The comparator's merged touching at the handover (J = 1, kappa_h = 1/2): its charge, its local form for J = 1/2, 1, 3/2,
and a certified count of all middle-band touchings at kappa_h.

Setting: open PR #9350's supplied comparator (u = +1 quadratic Majorana, J_x = J_y = 1, J_z = J, odd term kappa,
H(f) = i M(f)); the helpers in pr9350_lib.py are vendored unchanged from that PR (terms, interval clearing, Hessian test,
node enclosure, chirality sign det V).
Sections A, B exact (sympy, rationals, Q(sqrt 3, i)); section C computer-assisted: the PR's interval clearing and Hessian
test, plus a new weighted certificate at the double nodes (exact Taylor bound; float64 box cover with an explicit margin).
"""
import os, sys, time, itertools
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import sympy as sp
from mpmath import iv, mp, mpf
import pr9350_lib as L

T0 = time.time()
FAILS = []
def want(ok, label):
    print(("PASS " if ok else "FAIL ") + label, flush=True)
    if not ok:
        FAILS.append(label)
z1, z2, w = L.z1, L.z2, L.w
f = sp.symbols('f1 f2 f3', real=True)

# ---------------------------------------------------------------------------------------------
# A. The double node's effective two-band map and its degree (exact)
# ---------------------------------------------------------------------------------------------
print("== A. local form and charge at the handover node (exact)")
def bloch(J, kap, fstar):
    amp = {"xy": 2, "z": 2 * J, "odd": 2 * kap}
    M = sp.zeros(4, 4); dM = [sp.zeros(4, 4) for _ in range(3)]; ddM = [[sp.zeros(4, 4) for _ in range(3)] for _ in range(3)]
    for (a, b, n, kd) in L.TERMS:
        n = [int(x) for x in n]
        ph = sp.expand(sp.exp(2 * sp.pi * sp.I * sum(n[j] * fstar[j] for j in range(3))).rewrite(sp.cos)); phc = sp.conjugate(ph)
        M[a, b] += amp[kd] * ph; M[b, a] -= amp[kd] * phc
        for j in range(3):
            dM[j][a, b] += amp[kd] * ph * 2 * sp.pi * sp.I * n[j]; dM[j][b, a] -= amp[kd] * phc * (-2 * sp.pi * sp.I * n[j])
            for k in range(3):
                ddM[j][k][a, b] += amp[kd] * ph * (2 * sp.pi * sp.I) ** 2 * n[j] * n[k]
                ddM[j][k][b, a] -= amp[kd] * phc * (-2 * sp.pi * sp.I) ** 2 * n[j] * n[k]
    H0 = (sp.I * M).applyfunc(sp.radsimp)
    return H0, [(sp.I * x).applyfunc(sp.radsimp) for x in dM], [[(sp.I * x).applyfunc(sp.radsimp) for x in r] for r in ddM]
def pauli(h):
    R = lambda e: sp.expand(sp.radsimp(sp.expand_complex(sp.re(sp.expand(e)))))
    Im = lambda e: sp.expand(sp.radsimp(sp.expand_complex(sp.im(sp.expand(e)))))
    return sp.Matrix([R(h[0, 1]), -Im(h[0, 1]), R((h[0, 0] - h[1, 1]) / 2)]), R((h[0, 0] + h[1, 1]) / 2)
def local_form(J, kap, fstar):
    """Effective 2x2 map on the zero eigenspace: first order along the image of the linear part, second order (Loewdin)
    on its kernel plane; returns the leading weighted map and its degree (winding of the part transverse to a)."""
    H0, dH, ddH = bloch(J, kap, fstar)
    q = sp.radsimp(sum(H0[i, i] * H0[j, j] - H0[i, j] * H0[j, i] for i in range(4) for j in range(i + 1, 4)))
    Hp = H0 / sp.radsimp(-q)                                    # levels {0, 0, +-lam}: pseudo-inverse = H0/lam^2, lam^2 = -q
    ns = H0.nullspace()
    w1 = ns[0] / sp.sqrt(sp.radsimp((ns[0].H * ns[0])[0]))
    w2 = ns[1] - (w1.H * ns[1])[0] * w1; w2 = w2 / sp.sqrt(sp.radsimp((w2.H * w2)[0]))
    W = sp.Matrix.hstack(w1, w2).applyfunc(sp.radsimp)
    V = [pauli(W.H * dH[j] * W) for j in range(3)]
    Vm = sp.Matrix.hstack(*[v_[0] for v_ in V])
    eu = sp.Matrix([sp.Rational(1, 2), -sp.Rational(1, 2), 0])
    a = (Vm * eu).applyfunc(sp.radsimp)
    ker = [kv.applyfunc(sp.radsimp) for kv in Vm.nullspace(simplify=True)]
    v_, t_ = sp.symbols('v t', real=True)
    dk = v_ * ker[0] + t_ * ker[1]
    H1 = sum((dk[j] * dH[j] for j in range(3)), sp.zeros(4, 4))
    H2 = sum((dk[j] * dk[k] * ddH[j][k] / 2 for j in range(3) for k in range(3)), sp.zeros(4, 4))
    B, B0 = pauli(W.H * (H2 - H1 * Hp * H1) * W)
    ah = a / sp.sqrt(sp.radsimp((a.T * a)[0]))
    e2 = sp.Matrix([1, 0, 0]) - ah[0] * ah; e2 = (e2 / sp.sqrt(sp.radsimp((e2.T * e2)[0]))).applyfunc(sp.radsimp)
    e3 = ah.cross(e2).applyfunc(sp.radsimp)
    b2 = sp.expand(sp.radsimp((B.T * e2)[0])); b3 = sp.expand(sp.radsimp((B.T * e3)[0]))
    z, wv = sp.symbols('z wv')
    g = sp.expand((b2 + sp.I * b3).subs({v_: (z + 1 / z) / 2, t_: (z - 1 / z) / (2 * sp.I)}))
    A_, B_, C_ = [sp.radsimp(g.coeff(z, k)) for k in (2, 0, -2)]
    mods = [sp.re(sp.N(sp.Abs(r) ** 2, 30)) for r in sp.solve(A_ * wv ** 2 + B_ * wv + C_, wv)]
    wind = 2 * (sum(1 for m_ in mods if m_ < 1) - 1)
    orient = sp.sign(sp.Matrix.hstack(eu, ker[0], ker[1]).det())
    return dict(H0=H0, q=q, Vm=Vm, a=a, ker=ker, B=B, B0=B0, first_d0=[v_[1] for v_ in V], mods=mods, degree=orient * wind, sym=(v_, t_))
node_p = (sp.Rational(1, 4), sp.Rational(3, 4), sp.Rational(1, 2)); node_m = (sp.Rational(3, 4), sp.Rational(1, 4), sp.Rational(1, 2))
LF = local_form(sp.Integer(1), sp.Rational(1, 2), node_p)
want(LF['H0'].eigenvals() == {0: 2, 4 * sp.sqrt(3): 1, -4 * sp.sqrt(3): 1},
     "A1 J = 1, kappa = 1/2, f = (1/4, 3/4, 1/2): levels {0, 0, +-4 sqrt 3}; zero is a double level, the outer levels are nonzero")
want(LF['Vm'].rank(simplify=True) == 1 and [list(k) for k in LF['ker']] == [[1, 1, 0], [0, 0, 1]] and all(x == 0 for x in LF['first_d0']) and LF['B0'] == 0,
     "A2 the linear part P dH P has rank 1 with kernel span{(1,1,0), (0,0,1)}; no identity part at first or second order")
want(all(m_ < 1 - sp.Rational(1, 10) for m_ in LF['mods']),
     f"A3 transverse quadratic part: both roots of its winding polynomial lie inside the unit disk (|w|^2 = {[round(float(m_), 6) for m_ in LF['mods']]}, 30 digits), "
     "so it winds twice")
want(LF['degree'] == 2, "A4 the leading weighted map d = u a + B(v, t) (u along (1,-1,0) weight 2; v, t weight 1) has degree +2: charge +2 at (1/4, 3/4, 1/2)")
# the same leading map in the campaign's coordinates reproduces its D quartic: D = 48 |d|^2 at weighted order 4
u, v, t, P = sp.symbols('u v t P', real=True)
dcamp = sp.Matrix([2 * sp.pi * u + 2 * sp.pi ** 2 / 3 * (v ** 2 - v * t - t ** 2), 2 * sp.pi * u + 2 * sp.pi ** 2 / 3 * (-v ** 2 + 3 * v * t - t ** 2),
                   2 * sp.pi ** 2 / 3 * (-v ** 2 - v * t + t ** 2)])
Qcamp = 384 * sp.pi ** 2 * u ** 2 + 256 * sp.pi ** 3 * u * t * (v - t) + 64 * sp.pi ** 4 * (v ** 2 - v * t + t ** 2) ** 2
vL, tL = LF['sym']
dLF = (u * LF['a'] + LF['B']).applyfunc(sp.expand)
want(all(sp.simplify(e) == 0 for e in (dLF - dcamp.subs(v, 2 * vL).subs(t, tL))),
     "A5a the effective map computed here (coordinates u, v' = (d1 + d2)/2, t) equals the campaign-coordinate map d below with v = 2 v' (same kernel basis)")
want(sp.expand(48 * (dcamp.T * dcamp)[0] - Qcamp) == 0,
     "A5 48 |d|^2 is the campaign's weighted-degree-4 form 384 pi^2 u^2 + 256 pi^3 u t (v - t) + 64 pi^4 (v^2 - v t + t^2)^2 (u = d1 - d2, v = d1 + d2)")
y0 = sp.Matrix([sp.Rational(1, 3), sp.Rational(-2, 7), sp.Rational(5, 11)])
sols = sp.solve(list(dcamp - y0), [u, v, t], dict=True)
real = [s_ for s_ in sols if all(abs(sp.im(sp.N(val, 40))) < 1e-30 for val in s_.values())]
sgns = [sp.sign(sp.N(dcamp.jacobian([u, v, t]).subs(s_).det(), 40)) for s_ in real]
want(len(real) == 2 and sum(sgns) == 2, f"A6 independent count: the regular value (1/3, -2/7, 5/11) has {len(real)} real preimages, Jacobian signs {sgns} (40 digits): degree 2")
LFm = local_form(sp.Integer(1), sp.Rational(1, 2), node_m)
want(LFm['degree'] == -2, "A7 the mirror node (3/4, 1/4, 1/2) has degree -2")
for (J, kap2, xh) in [(sp.Rational(1, 2), sp.Rational(1, 12), sp.Rational(1, 3)), (sp.Rational(3, 2), sp.Rational(3, 4), sp.Rational(1, 6))]:
    assert sp.cos(2 * sp.pi * xh) == J - 1 and kap2 == J / (4 * (2 - J))
    R_ = local_form(J, sp.sqrt(kap2), (xh, 1 - xh, sp.Rational(1, 2)))
    lev = R_['H0'].eigenvals()
    want(lev.get(0) == 2 and len(lev) == 3 and R_['Vm'].rank(simplify=True) == 1 and [list(k) for k in R_['ker']] == [[1, 1, 0], [0, 0, 1]]
         and all(abs(m_ - 1) > 1e-10 for m_ in R_['mods']) and R_['degree'] == 2,
         f"A8 J = {J}, kappa_h^2 = {kap2}, node ({xh}, {1 - xh}, 1/2): levels {lev}; linear part rank 1 with the same kernel; leading map degree +2 "
         f"(|w|^2 = {[round(float(m_), 6) for m_ in R_['mods']]}, 30 digits)")
print("   [A took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# B. A weighted lower bound for D at the double node (exact)
# ---------------------------------------------------------------------------------------------
print("== B. D > 0 on the punctured weighted ball N_s <= 1/45 (exact)")
Dq = sp.expand(L.det_of(L.shifted(sp.Rational(1, 2), sp.Integer(1)), [z1, z2, w]) / (z1 * z2 * w) ** (4 * L.S))
TL = [((m[0] - 8, m[1] - 8, m[2] - 8), sp.Rational(c)) for m, c in sp.Poly(sp.expand(Dq * (z1 * z2 * w) ** 8), z1, z2, w).terms()]
NT = 12
z0 = (sp.I, -sp.I, sp.Integer(-1))
poly = 0
for (m, c) in TL:
    lin = sp.Rational(m[0] - m[1], 2) * u + sp.Rational(m[0] + m[1], 2) * v + m[2] * t
    poly += c * z0[0] ** m[0] * z0[1] ** m[1] * z0[2] ** m[2] * sum((2 * sp.I * P * lin) ** k / sp.factorial(k) for k in range(NT + 1))
poly = sp.expand(poly)
byw_u = {}
for (a, b, c), co in sp.Poly(poly, u, v, t).terms():
    byw_u.setdefault(2 * a + b + c, []).append(co)
want(sp.expand(poly - sp.conjugate(poly)) == 0 and min(byw_u) == 4
     and sp.expand(sum(co * u ** a * v ** b * t ** c for (a, b, c), co in sp.Poly(poly, u, v, t).terms() if 2 * a + b + c == 4) - Qcamp.subs(sp.pi, P)) == 0,
     "B1 Taylor polynomial of D at (1/4, 3/4, 1/2) (total degree 12): real; nothing below weighted degree 4 (so D = 0, grad D = 0); weighted-4 part = the campaign's form")
s_ = sp.Symbol('s', real=True)
q_ = t * (v - t); p_ = v ** 2 - v * t + t ** 2
polys = sp.expand(poly.subs(u, P * (s_ - q_ / 3)))
byw = {}
for (a, b, c), co in sp.Poly(polys, s_, v, t).terms():
    byw.setdefault(2 * a + b + c, []).append(co)
Q4 = sum(co * s_ ** a * v ** b * t ** c for (a, b, c), co in sp.Poly(polys, s_, v, t).terms() if 2 * a + b + c == 4)
Gq = sp.expand(p_ ** 2 - sp.Rational(2, 3) * q_ ** 2 - (v ** 2 + t ** 2) ** 2 / 4)
want(sp.expand(Q4 - 64 * P ** 4 * (6 * s_ ** 2 + p_ ** 2 - sp.Rational(2, 3) * q_ ** 2)) == 0 and sp.expand(Gq - (v - t) ** 2 * (3 * v - t) ** 2 / 12) == 0,
     "B2 with s = u/pi + t(v - t)/3: Q = 64 pi^4 [6 s^2 + p^2 - (2/3) q^2] and p^2 - (2/3) q^2 - rho^4/4 = (v - t)^2 (3v - t)^2/12 >= 0, so Q >= 16 pi^4 (s^2 + rho^4) >= 16 pi^4 N^4")
PI_UP, PI_LO = sp.Rational(355, 113), sp.Rational(333, 106)
def absup(co):
    return sum(abs(r) * PI_UP ** k for (k,), r in sp.Poly(sp.expand(co), P).terms())
Cw = {w_: sum(absup(co) for co in byw[w_]) for w_ in byw if w_ >= 5}
RW = sp.Rational(1, 45)
def bracket(r):
    b = 16 * PI_LO ** 4 - sum(Cw[w_] * r ** (w_ - 4) for w_ in Cw)
    rem = 0
    for (m, c) in TL:        # Taylor tail beyond total degree NT: |m.delta| <= (4.43 r |al| + |be| + |ga|) r for N <= r <= 1
        Lm = sp.Rational(443, 100) * r * abs(sp.Rational(m[0] - m[1], 2)) + abs(sp.Rational(m[0] + m[1], 2)) + abs(m[2])
        xx = 2 * PI_UP * Lm * r
        rem += abs(c) * xx ** (NT + 1) / sp.factorial(NT + 1) * sp.Integer(3) ** (sp.ceiling(xx) + 1)
    return b - rem / r ** 4
br = bracket(RW)
want(br > 0, f"B3 for 0 < N <= 1/45, N = max(|s|^(1/2), rho): D >= N^4 [16 pi^4 - sum_w C_w (1/45)^(w-4) - tail] = N^4 x {float(br):.2f} > 0 "
     "(exact rationals, pi in [333/106, 355/113], |u| <= 4.43 N^2)")
print("   [A-B took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# C. The count at kappa_h (computer-assisted)
# ---------------------------------------------------------------------------------------------
print("== C. every touching at J = 1, kappa = 1/2 (computer-assisted)")
Cs, h, lip, log, negs = L.clear((1.0, 1.0, 1.0), 0.5, levels=6, verbose=False)
groups = L.clusters(Cs, h)
want(negs == {2} and len(groups) == 4, f"C1 interval clearing (PR #9350's, 6 levels, half-width {h:.3g}): every cleared cube has exactly two negative levels and no "
     f"level within lip h of zero; the {len(Cs)} uncleared cubes form {len(groups)} groups")
kap, J = sp.Rational(1, 2), sp.Integer(1)
# line family at kappa = 1/2: c = cos 2 pi x = 1 - sqrt 3 (root of c^2 - 2c - 2 = 0 in (-1, 1)); exact vanishing of D and grad D modulo the line quartic
PL = sp.Poly(kap ** 2 * z1 ** 4 - z1 ** 3 + (J ** 2 - 2 * kap ** 2 - 2) * z1 ** 2 - z1 + kap ** 2, z1)
tg = [Dq] + [x * sp.diff(Dq, x) for x in (z1, z2, w)]
rl = [sp.rem(sp.Poly(sp.expand(sp.expand(e.subs({z2: 1 / z1, w: 1})) * z1 ** 12), z1), PL).as_expr() for e in tg]
want(all(sp.simplify(r) == 0 for r in rl), "C2 on f = (x, 1 - x, 0) with 4k^2c^2 - 2c + J^2 - 4k^2 - 2 = 0 (here c = 1 - sqrt 3): D and its three derivatives vanish (exact, modulo the line quartic)")
L.CPg = sp.expand(L.det_of(L.shifted(kap, J, True), [z1, z2, w, L.mu]) / (z1 * z2 * w) ** (4 * L.S))
mp.dps = 40; iv.dps = 30
xl = L.enclose_acos(1 - iv.sqrt(3), float(np.arccos(1 - np.sqrt(3)) / (2 * np.pi)))
line_nodes = [(xl, 1 - xl, iv.mpf(0)), (1 - xl, xl, iv.mpf(0))]
def refine(C, hh, levels):
    a, b, n, tt, lipb = L.build(L.terms((1.0, 1.0, 1.0), 0.5)); counts = set()
    for _ in range(levels):
        off = np.array(list(itertools.product((-0.5, 0.5), repeat=3))) * hh
        C = (C[:, None, :] + off[None, :, :]).reshape(-1, 3); hh /= 2
        r = float(L.ru(lipb * hh))
        A = L.H_intervals(C, a, b, n, tt)
        ngp, okp = L.inertia_neg(A, r); ngm, okm = L.inertia_neg(A, -r)
        cl = okp & okm & (ngp == ngm); counts |= set(np.unique(ngp[cl]).tolist()); C = C[~cl]
    return C, hh, counts
charges = {}
ok_line = True
for gi in groups:
    X = Cs[gi].copy(); X = X - np.round(X - X[0]); cen = (X.min(axis=0) + X.max(axis=0)) / 2
    if min(cen[2] % 1, 1 - cen[2] % 1) > 0.25:
        continue
    C2, h2, cnt = refine(X, h, 8)
    lo, hi = C2.min(axis=0) - h2, C2.max(axis=0) + h2
    inside = [k for k, nd in enumerate(line_nodes) if all(float(nd[j].a) - round(float(nd[j].a) - (lo[j] + hi[j]) / 2) >= lo[j] and
                                                          float(nd[j].b) - round(float(nd[j].a) - (lo[j] + hi[j]) / 2) <= hi[j] for j in range(3))]
    pd, st = L.pd_box(TL, lo, hi)
    re_, im_ = L.outer_nonzero(kap, J, line_nodes[inside[0]]) if len(inside) == 1 else (iv.mpf(0), iv.mpf(0))
    outer = not (re_.a <= 0 <= re_.b and im_.a <= 0 <= im_.b)
    ch = L.chirality(kap, J, list(line_nodes[inside[0]])) if len(inside) == 1 else 0
    charges['line x<1/2' if inside == [0] else 'line x>1/2'] = ch
    ok_line &= cnt <= {2} and len(inside) == 1 and pd and outer and ch != 0
    print(f"   line group at {np.round(cen, 4)}: refined 8 more levels to {len(C2)} cubes in a box of width {np.round(hi - lo, 6)}; Hessian of D positive definite "
          f"({pd}, min pivot {st['minpiv']:.1f}); outer levels nonzero ({outer}); chirality {ch}")
want(ok_line, "C3 each line group contains exactly its line node, where D's Hessian is positive definite on the whole box (so D > 0 there except at the node), "
     "the outer levels are nonzero, and the chirality sign det V is certified")
# double nodes: cover the group's (u, v, t) hull by the ball of B3 and boxes with a positive second-order lower bound for D
mm = np.array([m for m, _ in TL], dtype=float); cc = np.array([float(c) for _, c in TL])
AL = np.stack([(mm[:, 0] - mm[:, 1]) / 2, (mm[:, 0] + mm[:, 1]) / 2, mm[:, 2]], axis=1)
TP = 2 * np.pi
Mb = np.array([[np.sum(np.abs(cc) * TP ** 2 * np.abs(AL[:, i]) * np.abs(AL[:, j])) for j in range(3)] for i in range(3)])
MARGIN = 1e-7                                     # float64 error of D(c) and grad D(c) is below 1e-9 here (75 terms, |c_m| <= 2^9, |theta| < 40)
assert np.abs(cc).max() <= 512
def cover(f0, U0, V0, T0):
    phi = TP * (mm @ f0)
    def lower(Cc, Hh):
        th = TP * (Cc @ AL.T) + phi[None, :]
        Dv = np.cos(th) @ cc
        G = -(np.sin(th) * cc[None, :]) @ (TP * AL)
        return Dv - np.sum(np.abs(G) * Hh, axis=1) - 0.5 * np.einsum('bi,ij,bj->b', Hh, Mb, Hh) - MARGIN, np.abs(G) * Hh + 0.5 * Hh * (Hh @ Mb.T)
    def in_ball(Cc, Hh):
        um = np.abs(Cc[:, 0]) + Hh[:, 0]; vm = np.abs(Cc[:, 1]) + Hh[:, 1]; tm = np.abs(Cc[:, 2]) + Hh[:, 2]
        return np.maximum(np.sqrt(um / np.pi + tm * (vm + tm) / 3), np.sqrt(vm ** 2 + tm ** 2)) <= float(RW) * (1 - 1e-9)
    n0 = (4, 16, 16)
    grids = [(np.arange(n) + 0.5) / n * 2 * X0 - X0 for n, X0 in zip(n0, (U0, V0, T0))]
    Cc = np.array(list(itertools.product(*grids))); Hh = np.tile([U0 / n0[0], V0 / n0[1], T0 / n0[2]], (len(Cc), 1))
    nball = npos = depth = 0
    while len(Cc) and depth < 40:
        ib = in_ball(Cc, Hh); nball += int(ib.sum()); Cc, Hh = Cc[~ib], Hh[~ib]
        if not len(Cc): break
        lb, con = lower(Cc, Hh); ok = lb > 0; npos += int(ok.sum()); Cc, Hh, con = Cc[~ok], Hh[~ok], con[~ok]
        if not len(Cc): break
        k = np.argmax(con, axis=1); idx = np.arange(len(Cc))
        off = np.zeros_like(Hh); off[idx, k] = Hh[idx, k] / 2; Hn = Hh.copy(); Hn[idx, k] /= 2
        Cc = np.concatenate([Cc - off, Cc + off]); Hh = np.concatenate([Hn, Hn]); depth += 1
    return len(Cc) == 0, nball, npos, depth
ok_dbl = True
for gi in groups:
    X = Cs[gi].copy(); X = X - np.round(X - X[0]); cen = (X.min(axis=0) + X.max(axis=0)) / 2
    if min(cen[2] % 1, 1 - cen[2] % 1) <= 0.25:
        continue
    f0 = np.array([0.25, 0.75, 0.5]) if cen[0] % 1 < 0.5 else np.array([0.75, 0.25, 0.5])
    X = X - np.round(X - f0)
    cor = (X[:, None, :] + h * np.array(list(itertools.product((-1, 1), repeat=3)))[None, :, :]).reshape(-1, 3) - f0
    U0 = np.abs(cor[:, 0] - cor[:, 1]).max() * 1.001; V0 = np.abs(cor[:, 0] + cor[:, 1]).max() * 1.001; T0_ = np.abs(cor[:, 2]).max() * 1.001
    done, nball, npos, depth = cover(f0, U0, V0, T0_)
    ok_dbl &= done
    print(f"   double group at {np.round(cen, 4)}: {len(gi)} cubes inside |u| <= {U0:.4f}, |v| <= {V0:.4f}, |t| <= {T0_:.4f}; covered by {nball} boxes in the "
          f"ball of B3 and {npos} boxes with D > 0 (depth {depth})")
want(ok_dbl, "C4 each double group lies in a (u, v, t) box on which D > 0 except at its node: inside N <= 1/45 by B3, elsewhere by a second-order bound "
     "(centre value and gradient in float64 with a 1e-7 margin, exact global second-derivative bound)")
charges['double x<1/2'] = LF['degree']; charges['double x>1/2'] = LFm['degree']
want(charges.get('line x<1/2') == -1 and charges.get('line x>1/2') == 1 and sum(charges.values()) == 0
     and charges['line x<1/2'] + charges['double x<1/2'] == 1,
     f"C5 exactly four touchings at kappa_h: charges {charges}; they sum to zero, and the side x < 1/2 keeps its total +1 through the handover "
     "(PR #9350: +1 below kappa_c, -1 + 1 + 1 between kappa_c and kappa_h)")

print("   [total %.0f s]" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0]); sys.exit(1)
print("SUMMARY: PROVED (computer-assisted for the count) at J = 1, kappa_h = 1/2: the merged touching at (1/4, 3/4, 1/2) has charge +2 (exact: its leading "
      "weighted map u a + B(v, t) winds twice), its mirror -2; the same local form (rank-1 linear part along (1,-1,0), degree +2) holds at J = 1/2 and 3/2; "
      "the middle bands touch at exactly four points, the two line nodes (charges -1, +1) and the two double nodes, with a new weighted certificate "
      "D >= N^4 x 275 on N <= 1/45 replacing the Hessian test that fails there")
print("HIT: charge 2 and the exact count at the handover: at J = 1, kappa_h = 1/2 the middle bands touch at exactly four points (line nodes at cos 2 pi x = 1 - sqrt 3 "
      "with charges -+1, double nodes (1/4, 3/4, 1/2) and (3/4, 1/4, 1/2) with charges +-2); the double node's effective map is linear along (1,-1,0) and quadratic "
      "on span{(1,1,0), (0,0,1)} with degree 2, also at J = 1/2, 3/2; certified by a weighted bound D >= N^4 (16 pi^4 - ...) on N = max(|u/pi + t(v-t)/3|^(1/2), rho) <= 1/45")
