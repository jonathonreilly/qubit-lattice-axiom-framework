#!/usr/bin/env python3
"""Independent check of the route  paired spectrum + invertible complement  ==>  scalar Schur part vanishes at every vector zero.

Supplied model (not an axiom): four-site Bloch matrix H = i M(z), z_j = exp(i theta_j), the 18 supplied network terms below, amplitudes
2 J_x, 2 J_y, 2 J_z, 2 kappa (x, y, z, odd).  Cases of the cubic-flip note: (i) J=1, kappa^2=3/20, e^{ix0}=(-2+i sqrt5)/3;
(ii) J=5/2, kappa^2=45/44, e^{ix0}=(7+5i sqrt11)/18; both nodes +-x0.  theta = (x0+x)(1,-1,0) + y(1,1,0) + z(0,0,1).

Labels:  [exact]  = sympy / rational arithmetic;  [mp]  = mpmath, 60 digits, NOT outward-rounded (CHECKED, not a certificate).
Lemma (proved in ATTEMPT.md, step 3): H Hermitian with symmetric spectrum, T invertible, C invertible with det C < 0  =>  the Schur complement
S = A - B C^-1 B^+ has det S <= 0 with equality iff S = 0 iff det H = 0; in particular (Pauli vector of Num = detC*S) = 0 forces N0 = 0.
Only numpy, scipy, sympy, mpmath.  One process.  Single run prints PASS/FAIL lines, TOTAL, optional HIT, SUMMARY.
"""
import os, sys, ast, time, random, itertools
import numpy as np
import sympy as sp
import mpmath as mp

T_START = time.time()
RESULTS = []
mp.mp.dps = 60
random.seed(20261004)
np.random.seed(20261004)


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {label}" + (f" :: {detail}" if detail else ""), flush=True)


# ------------------------------------------------------------------------------------------------------------------ supplied network terms
# (a, b, n, kind): M[a,b] += t z^n, M[b,a] -= t z^-n.  Literal copy of the supplied terms; compared with the repo scripts below if they are present.
TERMS = [(0, 1, (-1, 0, 0), 'y'), (0, 1, (0, 0, 0), 'x'), (0, 3, (0, 0, -1), 'z'), (1, 1, (-1, 0, 0), 'odd'), (1, 3, (1, 0, -1), 'odd'),
         (3, 1, (0, 0, 1), 'odd'), (0, 0, (1, 0, 0), 'odd'), (0, 2, (-1, 0, 0), 'odd'), (2, 0, (0, 0, 0), 'odd'), (2, 3, (0, -1, 0), 'y'),
         (2, 3, (0, 0, 0), 'x'), (2, 1, (0, 0, 0), 'z'), (3, 3, (0, -1, 0), 'odd'), (3, 1, (0, 1, 0), 'odd'), (1, 3, (0, 0, 0), 'odd'),
         (2, 2, (0, 1, 0), 'odd'), (2, 0, (0, -1, 1), 'odd'), (0, 2, (0, 0, -1), 'odd')]

REPO = os.environ.get("REPO_MAIN", "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/main_wt")


def optional_source_comparison():
    base = os.path.join(REPO, "scripts")
    f_cen = os.path.join(base, "composite_site_network_flux_free_certified_touching_census_across_coupling_regimes_2026_10_01.py")
    f_cub = os.path.join(base, "composite_site_network_flux_free_cubic_flip_points_have_explicit_degree_one_neighbourhoods_2026_10_01.py")
    if not (os.path.exists(f_cen) and os.path.exists(f_cub)):
        print("INFO source scripts not found; term comparison skipped (not counted)")
        return
    # census: literal list assigned to TERMS
    tree = ast.parse(open(f_cen).read())
    lit = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, 'id', None) == 'TERMS' for t in node.targets):
            try:
                lit = ast.literal_eval(node.value)
            except Exception:
                lit = None
    check("terms: literal TERMS of the census script equal the terms used here", lit is not None and [tuple(t[:2]) + (tuple(t[2]), t[3]) for t in lit] == TERMS)
    # cubic-flip script: build rules rebuilt in code; execute only the def block that builds TERMS (pure integer code)
    src = open(f_cub).read().split("\n")
    s = [i for i, l in enumerate(src) if l.startswith("def is_site")][0]
    e = [i for i, l in enumerate(src) if l.startswith("TERMS = terms_tagged()")][0]
    ns = {"np": np}
    exec("\n".join(src[s:e + 1]), ns)
    check("terms: TERMS rebuilt by the cubic-flip script from the network rules equal the terms used here",
          [tuple(t[:2]) + (tuple(t[2]), t[3]) for t in ns["TERMS"]] == TERMS)


# ================================================================================================================== S1  exact pairing identity
Jx, Jy, Jz, kap = sp.symbols("Jx Jy Jz kappa", positive=True)
z1, z2, z3, mu = sp.symbols("z1 z2 z3 mu")
AMPS = {"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz, "odd": 2 * kap}
M_sym = sp.zeros(4, 4)
for (a, b, n, kd) in TERMS:
    mon = z1 ** n[0] * z2 ** n[1] * z3 ** n[2]
    M_sym[a, b] += AMPS[kd] * mon
    M_sym[b, a] -= AMPS[kd] / mon
Minv_T = M_sym.subs({z1: 1 / z1, z2: 1 / z2, z3: 1 / z3}, simultaneous=True).T
anti = (M_sym + Minv_T).applyfunc(sp.expand) == sp.zeros(4, 4)
cp = sp.Poly(sp.expand((mu * sp.eye(4) - M_sym).det(method="berkowitz")), mu)
coef = {e[0]: sp.expand(c) for e, c in cp.terms()}
check("S1a [exact] M(z) + M(1/z)^T = 0 identically (M anti-Hermitian, H = iM Hermitian, on the real torus |z_j|=1), symbolic couplings", anti)
check("S1b [exact] det(mu - M) = mu^4 + a2 mu^2 + D: coefficients of mu^3 and mu^1 vanish identically in (z1,z2,z3,Jx,Jy,Jz,kappa)",
      coef.get(3, 0) == 0 and coef.get(1, 0) == 0 and coef[4] == 1,
      f"a2 has {len(sp.expand(coef[2]).args)} terms, D has {len(sp.expand(coef[0]).args)} terms")
M_func = sp.lambdify((z1, z2, z3, Jx, Jy, Jz, kap), M_sym, "mpmath")


# ================================================================================================================== numerical comparator
CASES = {"i": dict(J=mp.mpf(1), k2=mp.mpf(3) / 20, z0=(-2 + 1j * mp.sqrt(5)) / 3),
         "ii": dict(J=mp.mpf(5) / 2, k2=mp.mpf(45) / 44, z0=(7 + 5j * mp.sqrt(11)) / 18)}
ZETA = {"i": mp.mpf(1) / 20, "ii": mp.mpf(1) / 500}                 # box |z| <= zeta, X^2+Y^2 <= zeta^6   (cubic-flip note)
EPS0 = {"i": mp.mpf(1) / 62500, "ii": mp.mpf(1) / 2250000}          # 0 < |eps| <= eps0                       (cubic-flip note)
CF = {"i": mp.mpf(-2) / 3, "ii": mp.mpf(7) / 18}                     # cos x0 = c_F = (J-2)(J+1)/(J+2)


def Hmat(J, x0s, x, y, z, kappa):
    """H = i M(z), z_j = exp(i theta_j);  theta1 = x0s + x + y, theta2 = -(x0s + x) + y, theta3 = z."""
    t1, t2, t3 = x0s + x + y, -(x0s + x) + y, z
    amp = {"x": 2, "y": 2, "z": 2 * J, "odd": 2 * kappa}
    H = mp.zeros(4, 4)
    for (a, b, n, kd) in TERMS:
        e = mp.expj(n[0] * t1 + n[1] * t2 + n[2] * t3)
        H[a, b] += 1j * amp[kd] * e
        H[b, a] += -1j * amp[kd] * mp.conj(e)
    return H


def pair_diag_residual(H):
    ev = sorted(mp.re(v) for v in mp.eigh(H, eigvals_only=True))
    return max(abs(ev[i] + ev[3 - i]) for i in range(4)), ev


class Node:
    def __init__(self, which, sgn):
        self.which, self.sgn = which, sgn
        cs = CASES[which]
        self.J = cs["J"]
        self.kap = mp.sqrt(cs["k2"])
        self.x0p = mp.arg(cs["z0"])
        self.x0 = sgn * self.x0p
        self.name = f"{which}{'+' if sgn > 0 else '-'}"
        self.H0 = Hmat(self.J, self.x0, 0, 0, 0, self.kap)
        P = mp.eye(4) - self.H0 * self.H0 / (16 * self.J ** 2)
        Q = mp.eye(4) - P
        self.T = None
        for wc in itertools.combinations(range(4), 2):                     # first admissible column choice (as in the source)
            for uc in itertools.combinations(range(4), 2):
                T = mp.zeros(4, 4)
                for r in range(4):
                    T[r, 0], T[r, 1], T[r, 2], T[r, 3] = P[r, wc[0]], P[r, wc[1]], Q[r, uc[0]], Q[r, uc[1]]
                if abs(mp.det(T)) > mp.mpf(10) ** -20:
                    self.T, self.cols = T, (wc, uc)
                    break
            if self.T is not None:
                break
        self.detT2 = abs(mp.det(self.T)) ** 2

    def H(self, x, y, z, kappa):
        return Hmat(self.J, self.x0, x, y, z, kappa)

    def schur(self, H):
        G = self.T.H * H * self.T
        A, B, C = G[0:2, 0:2], G[0:2, 2:4], G[2:4, 2:4]
        detC = mp.re(C[0, 0] * C[1, 1] - C[0, 1] * C[1, 0])
        adj = mp.matrix([[C[1, 1], -C[0, 1]], [-C[1, 0], C[0, 0]]])
        Nm = detC * A - B * adj * B.H
        N0 = mp.re((Nm[0, 0] + Nm[1, 1]) / 2)
        Nz = mp.re((Nm[0, 0] - Nm[1, 1]) / 2)
        Nx = mp.re((Nm[0, 1] + Nm[1, 0]) / 2)
        Ny = mp.re(1j * (Nm[0, 1] - Nm[1, 0]) / 2)
        return [Nx, Ny, Nz], N0, detC, Nm

    def num(self, x, y, z, kappa):
        return self.schur(self.H(x, y, z, kappa))


def norm3(v):
    return mp.sqrt(sum(a * a for a in v))


# ================================================================================================================== S2 exact block identity and control
def gauss_rand(rng):
    return sp.Rational(rng.randint(-5, 5), rng.randint(1, 4)) + sp.I * sp.Rational(rng.randint(-5, 5), rng.randint(1, 4))


rng = random.Random(7)
ok_id = True
for trial in range(12):
    Hh = sp.zeros(4, 4)
    for i in range(4):
        Hh[i, i] = sp.Rational(rng.randint(-6, 6), rng.randint(1, 3))
        for j in range(i + 1, 4):
            v = gauss_rand(rng)
            Hh[i, j], Hh[j, i] = v, sp.conjugate(v)
    while True:
        Tm = sp.Matrix(4, 4, lambda i, j: gauss_rand(rng))
        if sp.simplify(Tm.det()) != 0:
            break
    Gm = (Tm.H * Hh * Tm)
    A, B, C = Gm[0:2, 0:2], Gm[0:2, 2:4], Gm[2:4, 2:4]
    detC = sp.simplify(C.det())
    adj = C.adjugate()
    Nm = (detC * A - B * adj * B.H).applyfunc(sp.simplify)
    N0 = sp.simplify((Nm[0, 0] + Nm[1, 1]) / 2)
    Nz = sp.simplify((Nm[0, 0] - Nm[1, 1]) / 2)
    Nx = sp.simplify((Nm[0, 1] + Nm[1, 0]) / 2)
    Ny = sp.simplify(sp.I * (Nm[0, 1] - Nm[1, 0]) / 2)
    lhs = sp.simplify(N0 ** 2 - Nx ** 2 - Ny ** 2 - Nz ** 2)
    rhs = sp.simplify(detC * (Tm.det() * sp.conjugate(Tm.det())) * Hh.det())
    ok_id = ok_id and sp.simplify(lhs - rhs) == 0
check("S2a [exact] 12 random Gaussian-rational Hermitian H, invertible T: N0^2 - |N|^2 = detC * |det T|^2 * det H  (Schur determinant formula, Nm = detC*S)", ok_id)

# control: without a paired spectrum the vector zero does not force N0 = 0  (hypothesis is load-bearing)
Hc = sp.diag(1, 1, 1, -1)
Gc = Hc
Ac, Bc, Cc = Gc[0:2, 0:2], Gc[0:2, 2:4], Gc[2:4, 2:4]
dCc = Cc.det()
Nmc = dCc * Ac - Bc * Cc.adjugate() * Bc.H
check("S2b [exact] control: unpaired H=diag(1,1,1,-1), T=1: detC=-1<0, Pauli vector 0, but N0 = %s != 0, det H = -1 < 0 (pairing is necessary)" % sp.nsimplify((Nmc[0, 0] + Nmc[1, 1]) / 2),
      dCc < 0 and Nmc[0, 1] == 0 and Nmc[0, 0] == Nmc[1, 1] != 0 and Hc.det() < 0)
Hp = sp.diag(1, -1, 1, -1)
SHp = Hp[0:2, 0:2] - Hp[0:2, 2:4] * Hp[2:4, 2:4].inv() * Hp[2:4, 0:2]
check("S2c [exact] control: paired H=diag(1,-1,1,-1), T=1, C=diag(1,-1): S = diag(1,-1) is indefinite, det S = -1 <= 0 (lemma consistent)",
      Hp[2:4, 2:4].det() < 0 and SHp == sp.diag(1, -1) and SHp.det() <= 0)

# ================================================================================================================== S3 float stress of the lemma (random paired Hermitian)
bad = 0
minneg = 1.0
for _ in range(20000):
    Qm, _r = np.linalg.qr(np.random.randn(4, 4) + 1j * np.random.randn(4, 4))
    a, b = np.random.rand(2) * 3
    Hh = Qm @ np.diag([a, b, -a, -b]) @ Qm.conj().T
    Tm = np.random.randn(4, 4) + 1j * np.random.randn(4, 4)
    G = Tm.conj().T @ Hh @ Tm
    A_, B_, C_ = G[:2, :2], G[:2, 2:], G[2:, 2:]
    dC = np.linalg.det(C_).real
    if dC < 0:
        S = A_ - B_ @ np.linalg.inv(C_) @ B_.conj().T
        dS = np.linalg.det(S).real
        minneg = min(minneg, -dS / (np.linalg.norm(S) ** 2 + 1e-300))
        if dS > 1e-9 * np.linalg.norm(S) ** 2:
            bad += 1
check("S3 [float, 20000 random paired Hermitian H and random T with detC<0] det S <= 0 in every trial", bad == 0, f"violations {bad}; min of -detS/|S|^2 = {minneg:.2e}")

# ================================================================================================================== S4 numerical pairing at the comparator's real points
worst = 0
worst_neg = mp.mpf(0)
herm = 0
for _ in range(60):
    Jv = mp.mpf(random.uniform(0.2, 3.5)); kv = mp.mpf(random.uniform(-2, 2))
    th = [mp.mpf(random.uniform(-3.14, 3.14)) for _ in range(3)]
    Mm = M_func(mp.expj(th[0]), mp.expj(th[1]), mp.expj(th[2]), 1, 1, Jv, kv)
    H = 1j * Mm
    herm = max(herm, max(abs(H[i, j] - mp.conj(H[j, i])) for i in range(4) for j in range(4)))
    r, ev = pair_diag_residual(H)
    worst = max(worst, r)
    worst_neg = min(worst_neg, mp.det(H).real)
check("S4 [mp] 60 random real (theta, J, kappa incl. kappa<0): H Hermitian, spectrum symmetric under negation, det H >= 0", herm < mp.mpf(10) ** -30 and worst < mp.mpf(10) ** -25 and worst_neg > -mp.mpf(10) ** -25,
      f"max|ev_i+ev_(3-i)|={mp.nstr(worst, 3)}, min det H={mp.nstr(worst_neg, 3)}")

optional_source_comparison()

# ================================================================================================================== S5 nodes
NODES = [Node(w, s) for w in ("i", "ii") for s in (1, -1)]
for nd in NODES:
    ev = sorted(mp.re(v) for v in mp.eigh(nd.H0, eigvals_only=True))
    Nv, N0, dC, _ = nd.num(0, 0, 0, nd.kap)
    ok = (abs(ev[0] + 4 * nd.J) < mp.mpf(10) ** -30 and abs(ev[1]) < mp.mpf(10) ** -30 and abs(ev[2]) < mp.mpf(10) ** -30 and abs(ev[3] - 4 * nd.J) < mp.mpf(10) ** -30
          and dC < 0 and norm3(Nv) < mp.mpf(10) ** -30 and abs(N0) < mp.mpf(10) ** -30)
    check(f"S5a [mp] node {nd.name}: spec H0 = {{0,0,+-4J}}, T columns {nd.cols}, |det T|^2 = {mp.nstr(nd.detT2, 6)} (NOT 1), detC0 = {mp.nstr(dC, 8)} < 0, Pauli vector and N0 vanish at the node", ok)


# shear / unfolding data reconstructed independently (m, lambda, a1, b1, mu) by high-precision numerical differentiation
def shear_data(nd):
    k0 = nd.kap
    h = mp.mpf(10) ** -12

    def Nc(i):
        return lambda x, y, z, e: nd.num(x, y, z, k0 + e)[0][i]

    def vec(o):
        return [mp.diff(Nc(i), (0, 0, 0, 0), o, h=h) for i in range(3)]
    dot = lambda u, v: sum(a * b for a, b in zip(u, v))
    nx, ny = vec((1, 0, 0, 0)), vec((0, 1, 0, 0))
    c2 = [v / 2 for v in vec((0, 0, 2, 0))]
    ee = vec((0, 0, 0, 1))
    m = dot(c2, nx) / dot(nx, nx)
    lam = dot(ee, nx) / dot(nx, nx)
    par = max(max(abs(c2[i] - m * nx[i]) for i in range(3)), max(abs(ee[i] - lam * nx[i]) for i in range(3)))
    c3 = [v / 6 for v in vec((0, 0, 3, 0))]
    nxz = vec((1, 0, 1, 0))
    nb = [c3[i] - m * nxz[i] for i in range(3)]

    def F(i):
        return lambda X, Y, z, e: nd.num(X - m * z ** 2 - lam * e, Y, z, k0 + e)[0][i]
    w1 = [mp.diff(F(i), (0, 0, 0, 0), (0, 0, 1, 1), h=h) for i in range(3)]
    a1 = dot(w1, nx) / dot(nx, nx)
    b1 = dot(w1, ny) / dot(ny, ny)
    ga = dot(w1, nb) / dot(nb, nb)
    resid = max(abs(w1[i] - a1 * nx[i] - b1 * ny[i] - ga * nb[i]) for i in range(3))
    orth = max(abs(dot(nx, ny)), abs(dot(nx, nb)), abs(dot(ny, nb)))
    return dict(m=m, lam=lam, a1=a1, b1=b1, mu=-ga, par=par, resid=resid, orth=orth,
                nrm=(norm3(nx), norm3(ny), norm3(nb)))


SH = {}
for nd in NODES:
    SH[nd.name] = shear_data(nd)
    d = SH[nd.name]
    mu_exp = (nd.J + 2) / nd.kap ** 3
    ok = (d["par"] < mp.mpf(10) ** -20 and d["resid"] < mp.mpf(10) ** -18 and d["orth"] < mp.mpf(10) ** -18 * max(d["nrm"]) ** 2
          and abs(d["mu"] - mu_exp) < mp.mpf(10) ** -18 and d["mu"] > 0)
    check(f"S5b [mp] node {nd.name}: reconstructed local form (x'=x+m z^2, lam, a1, b1; n_x,n_y,n_b orthogonal; mu = (J+2)/kappa^3 = {mp.nstr(mu_exp, 10)} reproduced)", ok,
          f"m={mp.nstr(d['m'], 8)} lam={mp.nstr(d['lam'], 8)} |a1|={mp.nstr(abs(d['a1']), 2)} |b1|={mp.nstr(abs(d['b1']), 2)}")


# ================================================================================================================== S6 complement-gap bound recomputed (the hypothesis detC < 0 on the shifted box)
def gap_margin(nd, d):
    zeta, eps = ZETA[nd.which], EPS0[nd.which]
    X = zeta ** 3 + abs(d["m"]) * zeta ** 2 + abs(d["lam"]) * eps + abs(d["a1"]) * eps * zeta
    Y = zeta ** 3 + abs(d["b1"]) * eps * zeta
    amps = {"x": 2, "y": 2, "z": 2 * nd.J, "odd": 2 * nd.kap}
    ent = [[mp.mpf(0)] * 4 for _ in range(4)]
    for (a, b, n, kd) in TERMS:
        phi = abs(n[0] - n[1]) * X + abs(n[0] + n[1]) * Y + abs(n[2]) * zeta
        dl = amps[kd] * phi + (2 * eps if kd == "odd" else 0)
        ent[a][b] += dl
        ent[b][a] += dl
    Hd = max(sum(r) for r in ent)                                         # >= ||delta H||_op  (Hermitian, max row sum of entrywise bounds)
    U = nd.T[:, 2:4]
    Uf2 = sum(abs(U[i, j]) ** 2 for i in range(4) for j in range(2))     # ||U||_F^2 >= ||U||_op^2
    G = nd.T.H * nd.H0 * nd.T
    C = G[2:4, 2:4]
    dC0 = abs(C[0, 0] * C[1, 1] - C[0, 1] * C[1, 0])
    Cn = sum(abs(C[i, j]) for i in range(2) for j in range(2))           # >= ||C0||_op
    return dC0 / Cn, Uf2 * Hd


for nd in NODES:
    lo, hi = gap_margin(nd, SH[nd.name])
    check(f"S6 [mp] node {nd.name}: min|lambda(C0)| >= {mp.nstr(lo, 5)} > ||delta C|| <= {mp.nstr(hi, 5)} on the whole shifted box and eps-range (ratio {mp.nstr(lo / hi, 4)}): C keeps one + and one - eigenvalue", lo > hi)


# ================================================================================================================== S7 sampling of the shifted box: det C < 0, identity, |N0| <= |N|
def to_xyz(nd, d, X, Y, z, e):
    return X - d["m"] * z ** 2 - d["lam"] * e - d["a1"] * e * z, Y - d["b1"] * e * z, z


for nd in NODES:
    d = SH[nd.name]
    zeta, e0 = ZETA[nd.which], EPS0[nd.which]
    maxdC, maxres, maxratio, n_ok, minslack = -mp.inf, mp.mpf(0), mp.mpf(0), 0, mp.inf
    NS = 120
    for k in range(NS):
        if k < NS // 2:                                                   # uniform in the box
            z = zeta * random.uniform(-1, 1)
            r = zeta ** 3 * mp.sqrt(random.random()); ph = 2 * mp.pi * random.random()
            e = e0 * random.uniform(-1, 1)
        else:                                                             # concentrated near the zeros (small |N|)
            s = 10 ** random.uniform(-3, 0)
            z = zeta * s * random.uniform(-1, 1)
            r = zeta ** 3 * s ** 3 * mp.sqrt(random.random()); ph = 2 * mp.pi * random.random()
            e = e0 * s ** 2 * random.uniform(-1, 1)
        X, Y = r * mp.cos(ph), r * mp.sin(ph)
        x, y, zz = to_xyz(nd, d, X, Y, mp.mpf(z), mp.mpf(e))
        H = nd.H(x, y, zz, nd.kap + e)
        Nv, N0, dC, _ = nd.schur(H)
        detH = mp.re(mp.det(H))
        res = abs(N0 ** 2 - sum(a * a for a in Nv) - dC * nd.detT2 * detH) / (abs(N0 ** 2) + sum(a * a for a in Nv) + mp.mpf(10) ** -60)
        maxres = max(maxres, res)
        maxdC = max(maxdC, dC)
        nn = norm3(Nv)
        maxratio = max(maxratio, abs(N0) / nn)
        minslack = min(minslack, nn ** 2 - N0 ** 2)
        n_ok += 1
    check(f"S7 [mp] node {nd.name}: {NS} sample points of the shifted box x eps-range: detC<0 (max {mp.nstr(maxdC, 4)}), N0^2-|N|^2 = detC*|detT|^2*detH to {mp.nstr(maxres, 2)}, |N0|<=|N| (max ratio {mp.nstr(maxratio, 3)})",
          maxdC < 0 and maxres < mp.mpf(10) ** -25 and minslack > 0 and maxratio < 1)


# ================================================================================================================== S8 vector zeros: scalar part vanishes there; doubled zero eigenvalue
def find_zero(nd, d, e, start):
    zeta = ZETA[nd.which]
    s3, sg = abs(e) ** mp.mpf("1.5"), mp.sqrt(abs(e))

    def f(u0, u1, u2):
        x, y, z = to_xyz(nd, d, u0 * s3, u1 * s3, u2 * sg, e)
        Nv, _, _, _ = nd.num(x, y, z, nd.kap + e)
        return [Nv[0] / s3, Nv[1] / s3, Nv[2] / s3]
    sol = mp.findroot(f, (mp.mpf(0), mp.mpf(0), start / sg), tol=mp.mpf(10) ** -34, maxsteps=60)
    return sol[0] * s3, sol[1] * s3, sol[2] * sg


zero_rows = []
all_zero_ok = True
for nd in NODES:
    d = SH[nd.name]
    for frac in (mp.mpf("0.6"), mp.mpf("-0.6"), mp.mpf("1.0"), mp.mpf("-1.0")):
        e = frac * EPS0[nd.which]
        starts = [mp.mpf(0)] + ([mp.sqrt(d["mu"] * e), -mp.sqrt(d["mu"] * e)] if e > 0 else [])
        sols = []
        for st in starts:
            X, Y, z = find_zero(nd, d, e, st)
            x, y, zz = to_xyz(nd, d, X, Y, z, e)
            H = nd.H(x, y, zz, nd.kap + e)
            Nv, N0, dC, _ = nd.schur(H)
            ev = sorted(mp.re(v) for v in mp.eigh(H, eigvals_only=True))
            absev = sorted(abs(v) for v in ev)
            in_box = abs(z) <= ZETA[nd.which] and X * X + Y * Y <= ZETA[nd.which] ** 6
            ok = (norm3(Nv) < mp.mpf(10) ** -30 and abs(N0) < mp.mpf(10) ** -30 and dC < 0 and in_box
                  and absev[0] < mp.mpf(10) ** -25 and absev[1] < mp.mpf(10) ** -25 and absev[2] > mp.mpf(10) ** -3 and abs(ev[0] + ev[3]) < mp.mpf(10) ** -25)
            all_zero_ok = all_zero_ok and ok
            sols.append((X, Y, z, x, y, zz))
        distinct = all(abs(sols[a][2] - sols[b][2]) > mp.mpf(10) ** -8 for a in range(len(sols)) for b in range(a))
        zero_rows.append((nd.name, e, sols, distinct))
        all_zero_ok = all_zero_ok and distinct and len(sols) == (3 if e > 0 else 1)
check("S8 [mp] 4 nodes x eps in {+-0.6 eps0, +-eps0}: Newton zeros of the vector Pauli map in the shifted box (1 for eps<0, 3 distinct for eps>0): N0 = 0 there to 1e-30, "
      "detC<0, H has exactly the double zero level plus a symmetric pair +-l, l>1e-3", all_zero_ok)


# ================================================================================================================== S9 location of the landed families inside the shifted box (CHECKED, not interval-certified)
def family_points(nd, e):
    J, kp = nd.J, nd.kap + e
    k2 = kp * kp
    cc = J * J - 4 * k2 - 2
    roots = [(1 + sg * mp.sqrt(1 - 4 * k2 * cc)) / (4 * k2) for sg in (1, -1)]
    cl = min(roots, key=lambda r: abs(r - CF[nd.which]))
    xl = mp.acos(cl)
    pts = [("line", nd.sgn * (xl - nd.x0p), mp.mpf(0))]
    if e > 0:
        xe = mp.acos(1 - J / (4 * k2))
        ze = mp.acos((J + 2) / (4 * k2) - (4 + J - J * J) / J)
        pts += [("pair+", nd.sgn * (xe - nd.x0p), ze), ("pair-", nd.sgn * (xe - nd.x0p), -ze)]
    return pts


worst_fill = {}
worst_fam = mp.mpf(0)
ok_fam = True
for nd in NODES:
    d = SH[nd.name]
    zeta, e0 = ZETA[nd.which], EPS0[nd.which]
    fill = mp.mpf(0)
    grid = [e0 * mp.mpf(10) ** (-k / mp.mpf(4)) for k in range(0, 41)] + [-e0 * mp.mpf(10) ** (-k / mp.mpf(4)) for k in range(0, 41)] + [e0 * j / 40 for j in range(1, 41)] + [-e0 * j / 40 for j in range(1, 41)]
    for e in grid:
        for (nm, x, z) in family_points(nd, e):
            X = x + d["m"] * z ** 2 + d["lam"] * e + d["a1"] * e * z
            Y = d["b1"] * e * z
            fill = max(fill, abs(z) / zeta, mp.sqrt(X * X + Y * Y) / zeta ** 3)
    worst_fill[nd.name] = fill
    ok_fam = ok_fam and fill < 1
    # family nodes are vector zeros AND scalar zeros at sampled eps, and the family D = 0 identity holds
    for e in (e0, -e0, e0 / 7, -e0 / 7):
        for (nm, x, z) in family_points(nd, e):
            H = nd.H(x, 0, z, nd.kap + e)
            Nv, N0, dC, _ = nd.schur(H)
            worst_fam = max(worst_fam, norm3(Nv), abs(N0), abs(mp.re(mp.det(H))))
            ok_fam = ok_fam and dC < 0
check("S9a [mp] families (line node; plane-(ii) pair for eps>0) from the landed closed forms lie inside the shifted box for 164 eps values per node in [-eps0,eps0]: max fill " +
      ", ".join(f"{k}:{mp.nstr(v, 3)}" for k, v in worst_fill.items()), ok_fam and all(v < 1 for v in worst_fill.values()))
check("S9b [mp] at the family points (eps = +-eps0, +-eps0/7): det H, Pauli vector and N0 all vanish (max abs %s)" % mp.nstr(worst_fam, 3), worst_fam < mp.mpf(10) ** -25)
# Newton zeros coincide with the family points
dev = mp.mpf(0)
for (nm_, e, sols, distinct) in zero_rows:
    nd = [n for n in NODES if n.name == nm_][0]
    fam = family_points(nd, e)
    got = sorted([(s[3], s[4], s[5]) for s in sols], key=lambda t: (t[2]))
    want = sorted([(x, mp.mpf(0), z) for (_, x, z) in fam], key=lambda t: t[2])
    for g, w in zip(got, want):
        dev = max(dev, abs(g[0] - w[0]), abs(g[1] - w[1]), abs(g[2] - w[2]))
check("S9c [mp] Newton zeros of the vector map coincide with the closed-form family points to %s (this is an identification diagnostic only; the logical identification is step 6)" % mp.nstr(dev, 3), dev < mp.mpf(10) ** -25)

# ================================================================================================================== output
nfail = len(RESULTS) - sum(RESULTS)
print(f"# runtime {time.time() - T_START:.1f} s", flush=True)
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={nfail}")
if nfail == 0:
    print("HIT: scoped conditional result: for the supplied comparator, a paired spectrum plus the enforced detC<0 gives det S <= 0 (so |N0| <= |N|, equality only at N=N0=0) "
          "and N0 = 0 at every vector zero of the shifted box at J=1 and J=5/2 for all |eps| <= eps0; vector zeros = band touchings there (own, unrefereed)")
print("SUMMARY: the supplied comparator has a symmetric spectrum at every real momentum and coupling (exact char-poly identity), and with det C<0 on the shifted box this forces "
      "the scalar Schur part to vanish at every vector zero (inertia argument, controls and 4-node high-precision checks agree); family location in the box is checked, not interval-certified.")
sys.exit(0 if nfail == 0 else 1)
