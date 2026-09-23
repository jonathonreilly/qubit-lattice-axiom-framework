#!/usr/bin/env python3
"""J:derive:discrete-step-walk-under-the-clock-clause:a3 -- worker w-macbookpro90c72-jf02d.

A fourth discrete formulation of block 54's clause, and a general no-go.

The partial-swap walk on a line: two components (up, down) per site; step U = B A with
  A = product over bonds b = (x, x+1) of the rotation exp(-i eps_b sigma_x) on the pair {(up, x), (down, x+1)},
  B = the same on the pairs {(down, x), (up, x+1)};
the bond angle is the bond's clock, eps_b = eps0 sqrt(w_x w_{x+1}) (block 54's product form).

  P1  unitary and nearest-neighbour for EVERY assignment of bond angles (exact, Gaussian rationals, ring of 6)
  P2  uniform angle: tr U/2 = 1 - 2 sin^2(eps) cos^2 k, det U = 1: sin(omega/2) = sin(eps)|cos k|  (exact)
  P3  omega = 2 eps |cos k| (1 - (eps^2/6) sin^2 k) + O(eps^5): a clock up to relative O(eps^2)       (exact series)
  P4  separable dispersions omega = w(x) f(k) give exactly block 54's 1D ray law; the walk's first-order generator is,
      after psi_x -> i^x psi_x, twice block 54's line walk                                              (exact)
  P5  the walk's own ray law in closed form, and its expansion: block 54's law plus O(eps^4)           (exact)
  P6  no exact clock: U(2 eps) is not U(eps)^2 (trace; and for any field, range 2 against range 4); the flat-band
      conclusion of the theorem in ATTEMPT.md S5 is attained by a range-1 group                         (exact)
  P7  executed: a packet on a line in a uniform clock gradient against the exact discrete rays and against
      block 54's law (floating point)
See ATTEMPT.md.
"""
import numpy as np
import sympy as sp

NF = 0
NP = 0


def rep(tag, ok, msg):
    global NF, NP
    NF += (not ok)
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def step_matrix(L, cs, sn, lib=sp):
    """exact step U = B A on a ring of L sites; basis index 2x + (0 up, 1 down); bond angle given by (cos, sin)."""
    N = 2 * L
    I = sp.I if lib is sp else 1j
    A = (sp.zeros(N, N) if lib is sp else np.zeros((N, N), complex))
    B = (sp.zeros(N, N) if lib is sp else np.zeros((N, N), complex))
    for x in range(L):
        y = (x + 1) % L
        c, s = cs[x], sn[x]
        # A pairs (up, x) with (down, y); B pairs (down, x) with (up, y)
        for M, p, q in ((A, 2 * x, 2 * y + 1), (B, 2 * x + 1, 2 * y)):
            M[p, p] = c; M[q, q] = c; M[p, q] = -I * s; M[q, p] = -I * s
    return (B * A) if lib is sp else B @ A


def P1():
    L = 6
    pts = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)), (sp.Rational(8, 17), sp.Rational(15, 17)),
           (sp.Rational(7, 25), sp.Rational(24, 25)), (sp.Rational(20, 29), sp.Rational(21, 29)), (sp.Rational(9, 41), sp.Rational(40, 41))]
    U = step_matrix(L, [p[0] for p in pts], [p[1] for p in pts])
    unit = sp.simplify(U.H * U - sp.eye(2 * L)) == sp.zeros(2 * L, 2 * L)
    rng = all(U[i, j] == 0 for i in range(2 * L) for j in range(2 * L)
              if min(abs(i // 2 - j // 2), L - abs(i // 2 - j // 2)) > 2)
    # two ticks of the coined walk S R(theta_x) (R = [[cos, -sin], [sin, cos]], up steps right, down steps left) with theta_x = pi/2 - eps_x
    # equal -G U G^-1, U with angle eps_x on the bond (x, x+1), G = (down component shifted by -1, then multiplied by -i)
    N = 2 * L
    S, C, G = sp.zeros(N, N), sp.zeros(N, N), sp.zeros(N, N)
    for x in range(L):
        c_, s_ = pts[x]
        S[2 * ((x + 1) % L), 2 * x] = 1; S[2 * ((x - 1) % L) + 1, 2 * x + 1] = 1
        C[2 * x, 2 * x], C[2 * x, 2 * x + 1], C[2 * x + 1, 2 * x], C[2 * x + 1, 2 * x + 1] = s_, -c_, c_, s_    # cos theta = sin eps
        G[2 * x, 2 * x] = 1; G[2 * ((x - 1) % L) + 1, 2 * x + 1] = -sp.I
    Uc = S * C
    coin = sp.simplify(Uc * Uc + G * U * G.inv()) == sp.zeros(N, N)
    # hence U = V^2 with V = i G^-1 (S R) G of range 1
    V = sp.I * G.inv() * Uc * G
    root = sp.simplify(V * V - U) == sp.zeros(N, N) and all(
        V[i, j] == 0 for i in range(N) for j in range(N) if min(abs(i // 2 - j // 2), L - abs(i // 2 - j // 2)) > 1)
    coin = coin and root
    rep("P1 unitary and local", unit and rng and coin,
        "bond-local rotations exp(-i eps_b sigma_x) on the pairs {(up,x),(down,x+1)} then {(down,x),(up,x+1)}: U^+ U = 1 exactly for six "
        "different bond angles on a ring of 6 (rational cos, sin), and U reaches at most two sites: every assignment of bond clocks is allowed; "
        "the same U is (up to -G.G^-1, G a half-shift and a phase) two ticks of the coined walk S R(theta_x) at theta_x = pi/2 - eps_x, "
        "so U = V^2 with V = i G^-1 S R G of range 1")


def P2():
    e, k = sp.symbols('epsilon k', real=True)
    MA = sp.Matrix([[0, sp.exp(sp.I * k)], [sp.exp(-sp.I * k), 0]])
    MB = sp.Matrix([[0, sp.exp(-sp.I * k)], [sp.exp(sp.I * k), 0]])
    A = sp.cos(e) * sp.eye(2) - sp.I * sp.sin(e) * MA
    B = sp.cos(e) * sp.eye(2) - sp.I * sp.sin(e) * MB
    U = B * A
    tr = sp.simplify((U.trace() / 2 - (1 - 2 * sp.sin(e)**2 * sp.cos(k)**2)).rewrite(sp.exp))
    det = sp.simplify(U.det())
    inv = sp.simplify(MA * MA - sp.eye(2)) == sp.zeros(2, 2)
    rep("P2 dispersion", tr == 0 and det == 1 and inv,
        "the pair operators M_A = [[0,e^ik],[e^-ik,0]], M_B = M_A* are hermitian involutions, so each factor is cos eps - i sin eps M; "
        "tr U/2 = 1 - 2 sin^2(eps) cos^2 k, det U = 1: the two bands are e^(-+i omega) with sin(omega/2) = sin(eps) |cos k|")


def P3():
    e, c = sp.symbols('epsilon c', positive=True)
    om = 2 * sp.asin(sp.sin(e) * c)
    ser = sp.series(om, e, 0, 5).removeO()
    target = 2 * e * c * (1 - e**2 * (1 - c**2) / 6)
    ok = sp.simplify(sp.expand(ser - target)) == 0
    # the clock force: d omega/d eps = (omega/eps)(1 + O(eps^2))
    dom = sp.diff(om, e)
    rat = sp.series(dom * e / om, e, 0, 3).removeO()
    ok2 = sp.simplify(rat - (1 - e**2 * (1 - c**2) / 3)) == 0
    rep("P3 a clock to O(eps^2)", ok and ok2,
        "omega = 2 eps |cos k| (1 - (eps^2/6) sin^2 k) + O(eps^5): with eps = eps0 w the frequencies scale with the local clock up to a "
        "relative O(eps^2) that reshapes the band; the force on a ray is -(d omega/d eps) d eps = -omega d log w (1 - (eps^2/3) sin^2 k + ...)")


def P4():
    x, t = sp.symbols('x t', real=True)
    k = sp.Function('k')(t)
    w = sp.Function('w')(x)
    f = sp.Function('f')
    om = w * f(k)
    v = sp.diff(om, k)
    kdot = -sp.diff(om, x)
    # dv/dt along the ray: v depends on x (through w) and k
    dvdt = sp.diff(v, x) * v + sp.diff(v, k) * kdot
    u = sp.log(w)
    ueps = (f(k)**2 / 2)
    law = -w**2 * sp.diff(ueps, k, 2) * sp.diff(u, x) + 2 * v * sp.diff(u, x) * v
    ok = sp.simplify(sp.expand(dvdt - law)) == 0
    # the walk's first-order generator: symbol M_A + M_B = 2 cos k sigma_x; the gauge psi_x -> i^x psi_x shifts k by pi/2
    q = sp.symbols('q', real=True)
    MA = sp.Matrix([[0, sp.exp(sp.I * q)], [sp.exp(-sp.I * q), 0]])
    gen = (MA + MA.conjugate()).applyfunc(lambda z: sp.simplify(z.rewrite(sp.cos)))
    ok2 = sp.simplify(gen - 2 * sp.cos(q) * sp.Matrix([[0, 1], [1, 0]])) == sp.zeros(2, 2) and sp.simplify(sp.cos(q - sp.pi / 2) - sp.sin(q)) == 0
    rep("P4 block 54's law", ok and ok2,
        "for any separable omega = w(x) f(k), Hamilton's rays give dv/dt = -w^2 (f^2/2)'' d_x log w + 2 v^2 d_x log w exactly (block 54's "
        "law); the walk's first-order generator has symbol M_A + M_B = 2 cos k sigma_x, which the gauge psi_x -> i^x psi_x turns into "
        "2 sin k sigma_x: twice block 54's line walk sigma D, so to first order eps0 the step is exp(-i eps0 sqrt(w) 2 sigma D sqrt(w))")


def P5():
    e, k = sp.symbols('epsilon k', positive=True)
    Psi = 4 * sp.sin(e) * (e * sp.cos(e) - 2 * sp.sin(e) * sp.sin(k)**2) / (1 - sp.sin(e)**2 * sp.cos(k)**2)
    ok = True
    for sg in (1, -1):                                    # the two branches cos k > 0, cos k < 0 of |cos k|
        Om = 2 * sp.asin(sg * sp.sin(e) * sp.cos(k))
        Ok, Oe = sp.diff(Om, k), sp.diff(Om, e)
        Phi = e * (sp.diff(Ok, e) * Ok - sp.diff(Ok, k) * Oe)   # dv/dt = Phi d_x u along a ray, eps = eps0 e^u
        ok = ok and sp.simplify(Phi - 2 * Ok**2 - Psi) == 0
    ser = sp.series(Psi, e, 0, 6).removeO()
    tgt = 4 * e**2 * sp.cos(2 * k) + e**4 * (2 * sp.cos(2 * k) + 3 * sp.cos(4 * k) - 1) / 3
    ok2 = sp.simplify(sp.expand(sp.expand_trig(ser - tgt))) == 0
    rep("P5 the walk's ray law", ok and ok2,
        "along a ray of omega = 2 arcsin(sin eps |cos k|), eps = eps0 e^u: dv/dt = (2 v^2 + Psi) d_x u with Psi = 4 sin eps (eps cos eps - "
        "2 sin eps sin^2 k)/(1 - sin^2 eps cos^2 k) exactly (both branches); Psi = 4 eps^2 cos 2k + (eps^4/3)(2 cos 2k + 3 cos 4k - 1) "
        "+ O(eps^6): with k' = k + pi/2 the leading term is -(2 eps)^2 cos 2k', block 54's -w^2 cos 2k for E = 2 eps |sin k'|")


def P6():
    e, k = sp.symbols('epsilon k', real=True)
    cosom = 1 - 2 * sp.sin(e)**2 * sp.cos(k)**2
    tr2 = 1 - 2 * sp.sin(2 * e)**2 * sp.cos(k)**2              # tr U(2 eps)/2
    twice = 2 * cosom**2 - 1                                     # cos(2 omega(eps))
    diff = sp.simplify(tr2 - twice)
    dval = complex(sp.N(diff.subs({e: sp.Rational(1, 3), k: sp.Rational(1, 2)}), 30))
    ok_int = diff != 0 and abs(dval.imag) < 1e-25 and abs(dval.real) > 1e-3
    # any field: U[w]^2 reaches 4 sites, U[2w] (every bond angle doubled) reaches 2 (ring of 10, rational cos, sin)
    L = 10
    pts = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (12, 35, 37), (11, 60, 61), (28, 45, 53), (33, 56, 65)]
    cs = [sp.Rational(a, c) for a, b, c in pts]
    sn = [sp.Rational(b, c) for a, b, c in pts]
    U = step_matrix(L, cs, sn)
    U2 = U * U
    Ud = step_matrix(L, [c_**2 - s_**2 for c_, s_ in zip(cs, sn)], [2 * c_ * s_ for c_, s_ in zip(cs, sn)])
    far = lambda M, r: [(i, j) for i in range(2 * L) for j in range(2 * L)
                        if min(abs(i // 2 - j // 2), L - abs(i // 2 - j // 2)) > r and M[i, j] != 0]
    corner = U2[2 * 4, 2 * 0]                                  # <up, 4| U^2 |up, 0>
    ok_rng = corner == sn[0] * sn[1] * sn[2] * sn[3] and corner != 0 and not far(Ud, 2) and far(U2, 2)
    # the theorem's conclusion is attained: H = [[0, e^-ik], [e^ik, 0]] squares to 1, so e^(-icH) = cos c - i sin c H, range 1 for every c
    c1, c2, q = sp.symbols('c1 c2 q', real=True)
    H = sp.Matrix([[0, sp.exp(-sp.I * q)], [sp.exp(sp.I * q), 0]])
    V = lambda c: sp.cos(c) * sp.eye(2) - sp.I * sp.sin(c) * H
    ok_flat = sp.simplify(H * H - sp.eye(2)) == sp.zeros(2, 2) and \
        sp.simplify((V(c1) * V(c2) - V(c1 + c2)).applyfunc(sp.expand_trig)) == sp.zeros(2, 2)
    rep("P6 no exact clock", ok_int and ok_rng and ok_flat,
        "doubling the clock is not two steps: tr U(2eps)/2 - cos(2 omega(eps)) = " + f"{dval.real:.4f}"
        + " at eps = 1/3, k = 1/2; for any field, <up,x+4|U[w]^2|up,x> = sin eps_x sin eps_x+1 sin eps_x+2 sin eps_x+3 (checked on a ring "
        "of 10 with ten different angles) while U[2w] reaches 2 sites; flat bands are attained: H = [[0,e^-ik],[e^ik,0]] has H^2 = 1 and "
        "e^(-icH) = cos c - i sin c H, a group of range-1 steps (ATTEMPT.md S5)")


def P7():
    L, eps0, g = 1600, 0.6, 0.001
    x = np.arange(L)
    x0, k0, sig = 500.0, np.pi / 3, 30.0
    w = np.exp(g * (x - x0))
    epsb = eps0 * np.sqrt(w * np.roll(w, -1))
    cb, sb = np.cos(epsb), np.sin(epsb)
    xs_, ys_ = x, np.roll(x, -1)

    def step(ps):
        out = ps.copy()                                   # A: pairs (up, x) - (down, x+1)
        p_, q_ = 2 * xs_, 2 * ys_ + 1
        out[p_], out[q_] = cb * ps[p_] - 1j * sb * ps[q_], -1j * sb * ps[p_] + cb * ps[q_]
        ps = out.copy()                                   # B: pairs (down, x) - (up, x+1)
        p_, q_ = 2 * xs_ + 1, 2 * ys_
        ps[p_], ps[q_] = cb * out[p_] - 1j * sb * out[q_], -1j * sb * out[p_] + cb * out[q_]
        return ps
    # initial packet on the upper band at k0 (eigenvector of the uniform step at eps0 w(x0))
    e_ = eps0
    MA = np.array([[0, np.exp(1j * k0)], [np.exp(-1j * k0), 0]])
    MB = MA.conj()
    Uk = (np.cos(e_) * np.eye(2) - 1j * np.sin(e_) * MB) @ (np.cos(e_) * np.eye(2) - 1j * np.sin(e_) * MA)
    vals, vecs = np.linalg.eig(Uk)
    j = int(np.argmin(np.angle(vals)))                                   # e^{-i omega} with omega > 0
    chi = vecs[:, j]
    env = np.exp(-(x - x0)**2 / (4 * sig**2) + 1j * k0 * x)
    psi = np.zeros(2 * L, complex)
    psi[0::2], psi[1::2] = env * chi[0], env * chi[1]
    psi /= np.linalg.norm(psi)
    steps = 400
    for _ in range(steps):
        psi = step(psi)
    prob = np.abs(psi[0::2])**2 + np.abs(psi[1::2])**2
    xc = (prob * x).sum()

    def omega(xx, kk, exact=True):
        eps = eps0 * np.exp(g * (xx - x0))
        return 2 * np.arcsin(np.sin(eps) * abs(np.cos(kk))) if exact else 2 * eps * abs(np.cos(kk))

    def rays(exact):
        X, Kk, h = x0, k0, 1e-6
        for _ in range(steps):
            vx = (omega(X, Kk + h, exact) - omega(X, Kk - h, exact)) / (2 * h)
            fk = -(omega(X + h, Kk, exact) - omega(X - h, Kk, exact)) / (2 * h)
            X, Kk = X + vx, Kk + fk
        return X
    xr, xs = rays(True), rays(False)
    disp = xr - x0
    ok = abs(xc - xr) < 0.01 * abs(disp) and abs(xc - xs) > 5 * abs(xc - xr)
    rep("P7 line (executed)", ok,
        f"packet at k = pi/3 in eps = 0.6 exp(0.001 (x - 500)), 400 steps: centroid moved {xc - x0:.2f} sites; exact discrete rays "
        f"{disp:.2f} (off {abs(xc - xr):.3f}); block 54's separable law {xs - x0:.2f} (off {abs(xc - xs):.3f}): the O(eps^2) of P3 and P5 is seen")


def main():
    P1(); P2(); P3(); P4(); P5(); P6(); P7()
    print(f"TOTAL: PASS={NP} FAIL={NF}")
    if NF == 0:
        print("SUMMARY: PARTIAL a fourth formulation and a general no-go: the partial-swap walk (bond-local rotations exp(-i eps_b sigma_x) "
              "on alternating pairings, eps_b = eps0 sqrt(w_x w_y)) is unitary for every clock field with range 2 (two layers of nearest-neighbour bond rotations), has "
              "sin(omega/2) = sin(eps)|cos k| and a closed-form ray law equal to block 54's plus O(eps^4); a finite-range unitary step whose "
              "powers stay finite-range, or whose eigenphases scale exactly with the clock, has flat bands (S5), so in discrete steps block 54's "
              "translation identity keeps its covariance half exactly and loses its 'lambda_a times faster' half for every local rule that "
              "moves packets (S6)")
        print("HIT: the partial-swap walk -- rotations exp(-i eps_b sigma_x) on the pairs {(up,x),(down,x+1)} then {(down,x),(up,x+1)}, "
              "bond clock eps_b = eps0 sqrt(w_x w_{x+1}) -- is unitary for every clock field with range 2 (two layers of nearest-neighbour bond rotations), with sin(omega/2) = "
              "sin(eps)|cos k| and ray law dv/dt = [2v^2 + 4 sin eps (eps cos eps - 2 sin eps sin^2 k)/(1 - sin^2 eps cos^2 k)] d_x u, which is "
              "block 54's law for E = 2 eps |sin k'| (k' = k + pi/2) plus O(eps^4); and a finite-range unitary V with V, ..., V^(N(2R+2)) of "
              "range <= R, or with eigenphases c f_b(k) for all clocks c in an interval, has flat bands and never moves a walker more than "
              "(N-1)R sites")
    else:
        print(f"SUMMARY: ROUTE FAILS AT {NF} check(s) above")


if __name__ == "__main__":
    main()
