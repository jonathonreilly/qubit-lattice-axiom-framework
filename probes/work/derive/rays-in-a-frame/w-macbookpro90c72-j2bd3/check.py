#!/usr/bin/env python3
"""J:derive:rays-in-a-frame:a2 -- worker w-macbookpro90c72-j2bd3.

Rays of the ray function E^2 = a(x)^2 m^2 + w(x)^2 sum_ij g^ij(x) sin k_i sin k_j (block 62's frame,
g^ij = sum_a E_a^i E_a^j, with block 59's rates: a the rate timing the rest energy, w the rate
timing the hops).  Exact symbolic work (sympy) and exact integer matrix identities.

  R1 (a) the ray equations; block 59 T4 recovered for an isotropic frame; the fall with a full metric
  R2 (b) block 60's static field as a frame: bending/fall = 2 (weak field), (P+3Q)/(P+Q) (strong field)
  R3 (c) transverse traceless disturbance over a ray: which components, deflection, delay, drift
  R4 (d) rest energy compatible with a frame: none on-site and translation-covariant in M_2(C);
         the staggered one anticommutes with every frame (exact on a 4^3 torus) and falls as block 59
See ATTEMPT.md.
"""
import itertools
import numpy as np
import sympy as sp

NF = 0
NP = 0


def rep(tag, ok, msg):
    global NF, NP
    NF += (not ok)
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


X = sp.symbols('x1 x2 x3', real=True)
K = sp.symbols('k1 k2 k3', real=True)
m = sp.symbols('m', positive=True)
a = sp.Function('a')(*X)
w = sp.Function('w')(*X)
G = [[sp.Function('g%d%d' % (min(i, j) + 1, max(i, j) + 1))(*X) for j in range(3)] for i in range(3)]
s = [sp.sin(k) for k in K]
Q2 = sum(G[i][j] * s[i] * s[j] for i in range(3) for j in range(3))
E = sp.sqrt(a**2 * m**2 + w**2 * Q2)


def R1():
    ok = True
    for i in range(3):
        v = sp.diff(E, K[i])
        v_closed = w**2 * sum(G[i][j] * s[j] for j in range(3)) * sp.cos(K[i]) / E
        ok &= sp.simplify(v - v_closed) == 0
        f = -sp.diff(E, X[i])
        f_closed = -(m**2 * a * sp.diff(a, X[i]) + w * sp.diff(w, X[i]) * Q2
                     + w**2 / 2 * sum(sp.diff(G[j][l], X[i]) * s[j] * s[l] for j in range(3) for l in range(3))) / E
        ok &= sp.simplify(f - f_closed) == 0
    # fall at k = 0: dv_i/dt = sum_l (dv_i/dk_l) dk_l/dt with dk/dt = -grad E
    dvdk = sp.Matrix(3, 3, lambda i, l: sp.diff(sp.diff(E, K[i]), K[l]).subs({K[0]: 0, K[1]: 0, K[2]: 0}))
    dkdt = sp.Matrix([(-sp.diff(E, X[l])).subs({K[0]: 0, K[1]: 0, K[2]: 0}) for l in range(3)])
    acc = dvdk * dkdt
    fall = sp.Matrix([-w**2 * sum(G[i][l] * sp.diff(a, X[l]) for l in range(3)) / a for i in range(3)])
    ok_fall = sp.simplify(acc - fall) == sp.zeros(3, 1)
    # block 59 T4: isotropic frame g = delta/l^2, c = w/l: ray along x1 across a gradient along x3
    l = sp.Function('l')(*X)
    c = w / l
    Eiso = sp.sqrt(a**2 * m**2 + c**2 * sum(si**2 for si in s))
    sub = {G[i][j]: (1 / l**2 if i == j else 0) for i in range(3) for j in range(3)}
    same = sp.simplify(E.subs(sub) - Eiso) == 0
    E0 = Eiso.subs(m, 0)
    v3 = sp.diff(E0, K[2])
    dv3dk3 = sp.diff(v3, K[2]).subs(K[2], 0)
    dk3 = (-sp.diff(E0, X[2])).subs(K[2], 0)
    tr = sp.simplify((dv3dk3 * dk3).subs({K[1]: 0}) + c**2 * sp.diff(sp.log(c), X[2]) * sp.cos(K[0]) ** 0) == 0
    rep("R1 ray equations", ok and ok_fall and same and tr,
        "v_i = w^2 g^ij sin k_j cos k_i / E, dk_i/dt = -(m^2 a d_i a + w d_i w g^jl s_j s_l + (w^2/2) d_i g^jl s_j s_l)/E exactly; "
        "a slow body falls with dv^i/dt = -w^2 g^il d_l log a (the metric raises the index); for g = delta/l^2 this is block 59's "
        "E^2 = a^2 m^2 + c^2 sum sin^2 k with c = w/l, and a ray along an axis turns at -c^2 d_perp log c")


def R2():
    wb, lam = sp.symbols('wbar lambda', positive=True)
    ww = sp.Function('w')(X[2])
    ell = wb / ww                              # block 60, beta = 1: l = wbar/w
    c = ww / ell
    fall = sp.diff(sp.log(ww), X[2])           # a = w
    bend = sp.diff(sp.log(c), X[2])
    ok_w = sp.simplify(bend / fall - 2) == 0
    P, Q, g = sp.symbols('P Q g', positive=True)
    chi, N = 1 + Q * g, 1 - P * g              # far field of block 60 T4: l = chi^2, w = N/chi
    logc = sp.log(N / chi) - sp.log(chi**2)
    loga = sp.log(N / chi)
    ratio = sp.simplify(sp.diff(logc, g).subs(g, 0) / sp.diff(loga, g).subs(g, 0))
    ok_s = sp.simplify(ratio - (1 + 2 * Q / (P + Q))) == 0
    rep("R2 bending = 2 x fall", ok_w and ok_s,
        "block 60's static field as a frame, E = (1/l) 1 with l = wbar/w and a = w: c = w/l = w^2/wbar, so bending/fall = d log c/d log a "
        "= 2 exactly; in its strong field (l = chi^2, w = N/chi) the far-field ratio is (P + 3Q)/(P + Q) = block 60 T4(d)'s 1 + 2Q/(P+Q)")


def R3():
    t, q, z0, Ap, Ax, eps = sp.symbols('t q z0 A_p A_x epsilon', real=True)
    Om = sp.symbols('Omega', positive=True)
    kap = sp.pi / 3                            # an exact wave number with sin k > 0
    ph = q * X[2] - Om * t
    h = sp.zeros(3, 3)
    h[0, 0], h[1, 1], h[0, 1], h[1, 0] = Ap * sp.cos(ph), -Ap * sp.cos(ph), Ax * sp.cos(ph), Ax * sp.cos(ph)
    ok_tt = h.trace() == 0 and all(sp.simplify(q * h[2, j]) == 0 for j in range(3))
    ginv = sp.eye(3) - eps * h                 # first order
    Q2h = sum(ginv[i, j] * s[i] * s[j] for i in range(3) for j in range(3))
    Eh = sp.sqrt(Q2h)                          # m = 0, w = 1
    first = lambda e: sp.series(e, eps, 0, 2).removeO().coeff(eps, 1)
    ray = {K[0]: kap, K[1]: 0, K[2]: 0}
    v1 = first(sp.diff(Eh, K[0])).subs(ray)
    v2 = first(sp.diff(Eh, K[1])).subs(ray)
    v3 = first(sp.diff(Eh, K[2])).subs(ray)
    k2dot = first(-sp.diff(Eh, X[1])).subs(ray)
    k3dot = first(-sp.diff(Eh, X[2])).subs(ray)
    pos = {X[2]: z0}
    ok_rows = (sp.simplify(v1 + sp.cos(kap) * h[0, 0] / 2) == 0 and sp.simplify(v2 + h[0, 1] * sp.sign(sp.sin(kap))) == 0
               and sp.simplify(v3) == 0 and sp.simplify(k2dot) == 0
               and sp.simplify(k3dot - sp.sin(kap) * sp.diff(h[0, 0], X[2]) / 2) == 0)
    # along the unperturbed ray x3 = z0: integrate over 0 < t < T
    T = sp.symbols('T', positive=True)
    drift = sp.integrate(v2.subs(pos), (t, 0, T))
    kick = sp.integrate(k3dot.subs(pos), (t, 0, T))
    ok_int = (sp.simplify(drift + sp.sign(sp.sin(kap)) * Ax * (sp.sin(q * z0) - sp.sin(q * z0 - Om * T)) / Om) == 0
              and sp.simplify(kick + sp.sin(kap) * Ap * q * (sp.cos(q * z0 - Om * T) - sp.cos(q * z0)) / (2 * Om)) == 0)
    # a ray along the wave (axis 3) feels nothing at first order
    ray3 = {K[0]: 0, K[1]: 0, K[2]: kap}
    along = all(sp.simplify(first(sp.diff(Eh, K[i])).subs(ray3)) == 0 for i in range(3)) and \
        all(sp.simplify(first(-sp.diff(Eh, X[i])).subs(ray3)) == 0 for i in range(3))
    rep("R3 transverse traceless", ok_tt and ok_rows and ok_int and along,
        "h = (A+ (e1e1 - e2e2) + Ax (e1e2 + e2e1)) cos(q x3 - Omega t): a ray along axis j feels only the row h_j.: h_11 slows it "
        "(v1 = cos k (1 - h_11/2): delay (1/2) int h_11) and turns it towards the gradient of h_11 (dk3/dt = (sin k/2) d3 h_11), h_12 "
        "drifts it sideways (v2 = -h_12); along the unperturbed ray all three are bounded oscillations of size A/Omega (qA/Omega for "
        "the turn); a ray along q feels nothing at first order")


def R4():
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    m0, m1, m2, m3 = sp.symbols('m0:4', real=True)
    M = m0 * sp.eye(2) + m1 * sig[0] + m2 * sig[1] + m3 * sig[2]
    eqs = []
    for S_ in sig:
        eqs += list(M * S_ + S_ * M)
    sol = sp.solve(eqs, [m0, m1, m2, m3], dict=True)
    only0 = sol == [{m0: 0, m1: 0, m2: 0, m3: 0}]
    # the reduced walk's m sigma_1 anticommutes with E^j.sigma iff E_1^j = 0: a frame of rank <= 2
    e = sp.symbols('e1:4', real=True)
    Ev = e[0] * sig[0] + e[1] * sig[1] + e[2] * sig[2]
    red = sp.solve(list(sig[0] * Ev + Ev * sig[0]), e, dict=True)
    ok_red = len(red) == 1 and red[0].get(e[0], None) == 0
    # staggered mass on a 4^3 torus with a random integer frame field: {M, H} = 0 exactly; uniform frame: (H+M)^2 = H^2 + m^2
    L = 4
    rng = np.random.default_rng(7)
    sites = list(itertools.product(range(L), repeat=3))
    idx = {p: i for i, p in enumerate(sites)}
    S = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]

    def hop(frame):
        H = np.zeros((2 * L**3, 2 * L**3), complex)       # 4i * (1/2) sum_j {E^j.sigma, S_j}, S_j = (T_j - T_j^+)/(2i)
        for p in sites:
            for j in range(3):
                qn = list(p); qn[j] = (qn[j] + 1) % L; qn = tuple(qn)
                Ex = sum(frame[p][aa, j] * S[aa] for aa in range(3))
                Ey = sum(frame[qn][aa, j] * S[aa] for aa in range(3))
                x, y = idx[p], idx[qn]
                # (T_j psi)(x) = psi(x+e_j): block (x, y); T_j^+: block (y, x)
                H[2 * x:2 * x + 2, 2 * y:2 * y + 2] += Ex + Ey        # {E.sigma, T_j - T_j^+} entries, times 2i*... scale
                H[2 * y:2 * y + 2, 2 * x:2 * x + 2] -= Ex + Ey
        return H
    frame = {p: rng.integers(-3, 4, size=(3, 3)).astype(float) for p in sites}
    Hh = hop(frame)
    eps_ = np.kron(np.diag([(-1) ** (p[0] + p[1] + p[2]) for p in sites]).astype(complex), np.eye(2))
    anti = np.abs(eps_ @ Hh + Hh @ eps_).max()
    uni = {p: np.array([[2., 1, 0], [0, 1, -1], [1, 0, 3]]) for p in sites}
    Hu = hop(uni)
    mm = 5.0
    lhs = (Hu + mm * eps_) @ (Hu + mm * eps_)
    rhs = Hu @ Hu + mm**2 * np.eye(2 * L**3)
    sq = np.abs(lhs - rhs).max()
    shift = all((-1) ** (p[0] + 1 + p[1] + p[2]) == -((-1) ** (p[0] + p[1] + p[2])) for p in sites)
    rep("R4 rest energy", only0 and ok_red and anti == 0 and sq == 0 and shift,
        "no hermitian 2x2 M anticommutes with sigma_1, sigma_2, sigma_3 (sympy: M = 0), so no on-site rest energy the same at every "
        "site is compatible with a frame whose coin vectors span three axes; the reduced walk's m sigma_1 needs E_1^j = 0 (rank <= 2); "
        "the staggered term (-1)^(x1+x2+x3) m anticommutes with the hops of every frame field (4^3 torus, random integer frame: "
        "{M,H} = 0 exactly) and gives (H+M)^2 = H^2 + m^2 for a uniform frame, but changes sign under a unit translation; timed by "
        "the site rate it falls as R1: -w^2 g^il d_l log a")


def main():
    R1(); R2(); R3(); R4()
    print(f"TOTAL: PASS={NP} FAIL={NF}")
    if NF == 0:
        print("SUMMARY: PROVED (a)-(d) exactly: the ray equations of E^2 = a^2 m^2 + w^2 g^ij sin k_i sin k_j (fall -w^2 g^il d_l log a); "
              "block 60's field as a frame bends rays twice the fall (weak field) and (P+3Q)/(P+Q) times it (strong field); a ray along "
              "axis j feels only the row h_j. of a transverse traceless disturbance (h_jj: delay and turn; h_jl: sideways drift), a ray "
              "along its wave vector nothing; no translation-covariant on-site rest energy is compatible with a full frame in M_2(C), the "
              "staggered one is and falls as block 59 with the inverse metric")
        print("HIT: for block 62's frame with block 59's rates the rays of E^2 = a^2 m^2 + w^2 g^ij(x) sin k_i sin k_j fall with "
              "dv^i/dt = -w^2 g^il d_l log a and, for block 60's field written as E = (w/wbar) 1, bend twice as much (far field of the "
              "strong field: (P+3Q)/(P+Q)); a ray along axis j feels only h_jj (delay, turn) and h_jl (sideways drift) of a transverse "
              "traceless disturbance; no on-site rest energy the same at every site anticommutes with a frame spanning three coin axes, "
              "while the staggered one does for every frame")
    else:
        print(f"SUMMARY: ROUTE FAILS AT {NF} check(s) above")


if __name__ == "__main__":
    main()
